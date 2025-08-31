import curses
import os
import time
from typing import List, Dict, Optional

class PDSXEditor:
    def __init__(self):
        self.screen = None
        self.buffer: List[str] = []
        self.cursor_y = 0
        self.cursor_x = 0
        self.offset_y = 0
        self.status_message = ""
        self.highlight_line = -1
        self.command_history: List[str] = []
        self.history_pos = 0
        self.modified = False
        self.filename: Optional[str] = None
        self.syntax_colors = {}
        
    def init_colors(self):
        """Renk çiftlerini başlat"""
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Başlık çubuğu
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Anahtar kelimeler
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Strings
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Sayılar
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)  # Hatalar
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Yorumlar

    def start(self):
        """Editörü başlat"""
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        self.init_colors()
        self.main_loop()

    def main_loop(self):
        """Ana döngü"""
        while True:
            self.draw_screen()
            ch = self.screen.getch()
            if ch == ord('q'):  # Ctrl+Q ile çıkış
                if self.modified:
                    self.save_prompt()
                break
            elif ch == ord('s'):  # Ctrl+S ile kaydet
                self.save_file()
            elif ch == curses.KEY_UP:
                self.move_cursor(-1, 0)
            elif ch == curses.KEY_DOWN:
                self.move_cursor(1, 0)
            elif ch == curses.KEY_LEFT:
                self.move_cursor(0, -1)
            elif ch == curses.KEY_RIGHT:
                self.move_cursor(0, 1)
            elif ch == ord('\n'):
                self.insert_newline()
            elif ch == curses.KEY_BACKSPACE or ch == 127:
                self.backspace()
            elif ch == curses.KEY_DC:  # Delete tuşu
                self.delete_char()
            elif ch == ord('\t'):
                self.insert_tab()
            else:
                self.insert_char(ch)

    def draw_screen(self):
        """Ekranı çiz"""
        self.screen.clear()
        height, width = self.screen.getmaxyx()
        
        # Başlık çubuğu
        title = f" PDSX Editor - {self.filename or 'Untitled'} "
        if self.modified:
            title += "[Modified]"
        self.screen.attron(curses.color_pair(1))
        self.screen.addstr(0, 0, title + " " * (width - len(title)))
        self.screen.attroff(curses.color_pair(1))

        # Metin alanı
        for i in range(height - 2):
            line_num = self.offset_y + i
            if line_num < len(self.buffer):
                line = self.buffer[line_num]
                # Sözdizimi renklendirme
                self.draw_syntax_line(i + 1, line)
            else:
                self.screen.addstr(i + 1, 0, "~")

        # Durum çubuğu
        status = f" {self.cursor_y+1},{self.cursor_x+1} "
        if self.status_message:
            status += f" - {self.status_message}"
        self.screen.attron(curses.color_pair(1))
        self.screen.addstr(height-1, 0, status + " " * (width - len(status)))
        self.screen.attroff(curses.color_pair(1))

        # İmleç konumlandırma
        self.screen.move(self.cursor_y - self.offset_y + 1, self.cursor_x)
        self.screen.refresh()

    def draw_syntax_line(self, y: int, line: str):
        """Sözdizimi renklendirme ile satır çiz"""
        x = 0
        tokens = self.tokenize_line(line)
        for token, token_type in tokens:
            if token_type == "keyword":
                self.screen.attron(curses.color_pair(2))
            elif token_type == "string":
                self.screen.attron(curses.color_pair(3))
            elif token_type == "number":
                self.screen.attron(curses.color_pair(4))
            elif token_type == "comment":
                self.screen.attron(curses.color_pair(6))
                
            self.screen.addstr(y, x, token)
            
            if token_type:
                self.screen.attroff(curses.color_pair(2))
                self.screen.attroff(curses.color_pair(3))
                self.screen.attroff(curses.color_pair(4))
                self.screen.attroff(curses.color_pair(6))
                
            x += len(token)

    def tokenize_line(self, line: str):
        """Satırı token'lara ayır ve tiplerini belirle"""
        tokens = []
        i = 0
        while i < len(line):
            if line[i:].startswith("REM "):  # Yorum satırı
                tokens.append((line[i:], "comment"))
                break
            elif line[i].isspace():  # Boşluk
                j = i + 1
                while j < len(line) and line[j].isspace():
                    j += 1
                tokens.append((line[i:j], None))
                i = j
            elif line[i].isalpha():  # Kelime
                j = i + 1
                while j < len(line) and (line[j].isalnum() or line[j] == '_'):
                    j += 1
                word = line[i:j]
                if word.upper() in self.keywords:
                    tokens.append((word, "keyword"))
                else:
                    tokens.append((word, None))
                i = j
            elif line[i].isdigit():  # Sayı
                j = i + 1
                while j < len(line) and (line[j].isdigit() or line[j] == '.'):
                    j += 1
                tokens.append((line[i:j], "number"))
                i = j
            elif line[i] == '"':  # String
                j = i + 1
                while j < len(line) and line[j] != '"':
                    j += 1
                if j < len(line):
                    j += 1
                tokens.append((line[i:j], "string"))
                i = j
            else:  # Diğer karakterler
                tokens.append((line[i], None))
                i += 1
        return tokens

    def move_cursor(self, dy: int, dx: int):
        """İmleci taşı"""
        new_y = self.cursor_y + dy
        new_x = self.cursor_x + dx
        
        if new_y < 0:
            new_y = 0
        elif new_y >= len(self.buffer):
            new_y = len(self.buffer) - 1
            
        if new_x < 0:
            if new_y > 0:
                new_y -= 1
                new_x = len(self.buffer[new_y])
            else:
                new_x = 0
        elif new_x > len(self.buffer[new_y]):
            if new_y < len(self.buffer) - 1:
                new_y += 1
                new_x = 0
            else:
                new_x = len(self.buffer[new_y])
                
        self.cursor_y = new_y
        self.cursor_x = new_x
        
        # Scroll if needed
        height = self.screen.getmaxyx()[0]
        if self.cursor_y < self.offset_y:
            self.offset_y = self.cursor_y
        elif self.cursor_y >= self.offset_y + height - 2:
            self.offset_y = self.cursor_y - height + 3

    def insert_char(self, ch: int):
        """Karakter ekle"""
        if 32 <= ch <= 126:  # Yazdırılabilir karakter
            line = self.buffer[self.cursor_y]
            self.buffer[self.cursor_y] = line[:self.cursor_x] + chr(ch) + line[self.cursor_x:]
            self.cursor_x += 1
            self.modified = True

    def insert_newline(self):
        """Yeni satır ekle"""
        current_line = self.buffer[self.cursor_y]
        self.buffer[self.cursor_y] = current_line[:self.cursor_x]
        self.buffer.insert(self.cursor_y + 1, current_line[self.cursor_x:])
        self.cursor_y += 1
        self.cursor_x = 0
        self.modified = True

    def backspace(self):
        """Karakter sil (backspace)"""
        if self.cursor_x > 0:
            line = self.buffer[self.cursor_y]
            self.buffer[self.cursor_y] = line[:self.cursor_x-1] + line[self.cursor_x:]
            self.cursor_x -= 1
            self.modified = True
        elif self.cursor_y > 0:
            # Satır birleştirme
            self.cursor_x = len(self.buffer[self.cursor_y-1])
            self.buffer[self.cursor_y-1] += self.buffer[self.cursor_y]
            self.buffer.pop(self.cursor_y)
            self.cursor_y -= 1
            self.modified = True

    def delete_char(self):
        """Karakter sil (delete)"""
        if self.cursor_x < len(self.buffer[self.cursor_y]):
            line = self.buffer[self.cursor_y]
            self.buffer[self.cursor_y] = line[:self.cursor_x] + line[self.cursor_x+1:]
            self.modified = True
        elif self.cursor_y < len(self.buffer) - 1:
            # Satır birleştirme
            self.buffer[self.cursor_y] += self.buffer[self.cursor_y+1]
            self.buffer.pop(self.cursor_y+1)
            self.modified = True

    def insert_tab(self):
        """Tab ekle"""
        self.buffer[self.cursor_y] = (self.buffer[self.cursor_y][:self.cursor_x] + 
                                    "    " + 
                                    self.buffer[self.cursor_y][self.cursor_x:])
        self.cursor_x += 4
        self.modified = True

    def save_file(self):
        """Dosyayı kaydet"""
        if not self.filename:
            self.status_message = "Filename: "
            # TODO: Filename input implementation
            return
            
        try:
            with open(self.filename, 'w') as f:
                f.write('\n'.join(self.buffer))
            self.modified = False
            self.status_message = f"Saved to {self.filename}"
        except Exception as e:
            self.status_message = f"Error saving file: {str(e)}"

    def save_prompt(self):
        """Kaydetme sorgusu"""
        if self.modified:
            # TODO: Save prompt implementation
            pass

    def load_file(self, filename: str):
        """Dosya yükle"""
        try:
            with open(filename, 'r') as f:
                self.buffer = f.read().splitlines()
            if not self.buffer:
                self.buffer = [""]
            self.filename = filename
            self.modified = False
        except Exception as e:
            self.status_message = f"Error loading file: {str(e)}"
            self.buffer = [""]

    def cleanup(self):
        """Editörü temizle ve kapat"""
        if self.screen:
            self.screen.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

    @property
    def keywords(self):
        """PDSX anahtar kelimeleri"""
        return {
            'AND', 'AS', 'ASSERT', 'BREAK', 'CASE', 'CATCH', 'CLASS', 'CONST',
            'CONTINUE', 'DATA', 'DIM', 'DO', 'ELSE', 'END', 'ERROR', 'EXIT',
            'EXPORT', 'FINALLY', 'FOR', 'FUNCTION', 'GLOBAL', 'GOTO', 'GOSUB',
            'IF', 'IMPORT', 'IN', 'INPUT', 'IS', 'LET', 'LOOP', 'MOD', 'MODULE',
            'NEXT', 'NOT', 'ON', 'OR', 'PRINT', 'PRIVATE', 'PUBLIC', 'READ',
            'REM', 'RESTORE', 'RETURN', 'SELECT', 'SHARED', 'STATIC', 'STEP',
            'STOP', 'SUB', 'SYSTEM', 'THEN', 'THIS', 'THROW', 'TO', 'TRY',
            'UNTIL', 'WEND', 'WHILE', 'WITH', 'XOR'
        }

def main(filename=None):
    """Ana fonksiyon"""
    editor = PDSXEditor()
    try:
        if filename:
            editor.load_file(filename)
        editor.start()
    finally:
        editor.cleanup()

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else None)
