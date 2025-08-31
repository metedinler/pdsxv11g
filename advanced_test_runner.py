#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gelismis Test Calistirici ve Analiz Sistemi
pdsXv11g.py interpreter'i icin kapsamli test otomasyonu
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    END = '\033[0m'

class AdvancedTestLogger:
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = log_dir / f"advanced_test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.error_log = log_dir / f"error_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.results = []
    
    def log(self, level: str, message: str, details: str = ""):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {level}: {message}"
        if details:
            log_entry += f"\n    Detaylar: {details}"
        
        print(log_entry)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + "\n")
    
    def log_error_analysis(self, test_name: str, issues: List[str]):
        """Hata analizi sonuclarini ayri dosyaya kaydet"""
        with open(self.error_log, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Test: {test_name}\n")
            f.write(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'='*60}\n")
            
            if issues:
                f.write("TESPİT EDİLEN SORUNLAR:\n")
                f.write("-" * 30 + "\n")
                for i, issue in enumerate(issues, 1):
                    f.write(f"{i}. {issue}\n")
            else:
                f.write("Sorun tespit edilmedi.\n")
            
            f.write("\n")

class AdvancedTestRunner:
    def __init__(self, test_dir: str = None):
        self.base_dir = Path(__file__).parent if test_dir is None else Path(test_dir)
        self.test_dir = self.base_dir
        self.log_dir = self.base_dir / "test_logs"
        self.interpreter_path = self.base_dir / "pdsXv11g.py"
        
        self.logger = AdvancedTestLogger(self.log_dir)
        
        # Test kategorileri
        self.test_categories = {
            'basic': [],
            'advanced': [],
            'select_case': [],
            'variables': [],
            'functions': [],
            'arrays': [],
            'loops': [],
            'other': []
        }
        
    def discover_tests(self) -> List[Path]:
        """Test dosyalarini kesfet"""
        test_files = list(self.test_dir.glob("*.basx"))
        test_files.extend(list(self.test_dir.glob("test_*.basx")))
        
        # Duplikatlari kaldir
        seen = set()
        unique_tests = []
        for test_file in test_files:
            if test_file not in seen:
                seen.add(test_file)
                unique_tests.append(test_file)
        
        self.logger.log("INFO", f"{len(unique_tests)} test dosyasi kesfedildi")
        return unique_tests
    
    def categorize_tests(self, test_files: List[Path]) -> Dict[str, List[Path]]:
        """Test dosyalarini kategorilere ayir"""
        categories = {
            'basic': [],
            'advanced': [],
            'select_case': [],
            'variables': [],
            'functions': [],
            'arrays': [],
            'loops': [],
            'other': []
        }
        
        for test_file in test_files:
            name = test_file.name.lower()
            
            if 'basic' in name or 'test1' in name:
                categories['basic'].append(test_file)
            elif 'select' in name or 'case' in name:
                categories['select_case'].append(test_file)
            elif 'variable' in name or 'var' in name or 'degisken' in name:
                categories['variables'].append(test_file)
            elif 'function' in name or 'fonksiyon' in name or 'func' in name:
                categories['functions'].append(test_file)
            elif 'array' in name or 'dizi' in name:
                categories['arrays'].append(test_file)
            elif 'loop' in name or 'dongu' in name or 'for' in name or 'while' in name:
                categories['loops'].append(test_file)
            elif 'advanced' in name or 'gelismis' in name:
                categories['advanced'].append(test_file)
            else:
                categories['other'].append(test_file)
        
        return categories
    
    def is_problematic_test(self, test_file: Path) -> bool:
        """Test dosyasinin problematik olup olmadigini kontrol et"""
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read().upper()
                
            # Problematik durumlar
            problematic_patterns = [
                'INPUT',           # Kullanici girisi gerekiyor
                'INPUTBOX(',       # Dialog box gerektiren fonksiyon
                'MSGBOX(',         # Dialog box
                'WHILE 1',         # Sonsuz dongu
                'WHILE TRUE',      # Sonsuz dongu
                'DO WHILE 1',      # Sonsuz dongu
                'GOTO',            # Problematik kontrol akisi
            ]
            
            for pattern in problematic_patterns:
                if pattern in content:
                    return True
                    
            return False
            
        except Exception as e:
            self.logger.log("ERROR", f"Test dosyasi okunamadi: {test_file.name}", str(e))
            return True
    
    def analyze_output_for_errors(self, output: str, test_name: str) -> List[str]:
        """Test ciktisini hata analizi icin kontrol et"""
        issues = []
        if not output:
            return issues
            
        lines = output.split('\n')
        
        for i, line in enumerate(lines, 1):
            line_clean = line.strip().lower()
            
            # Hata tespiti
            error_patterns = [
                ('hata:', 'Hata mesaji'),
                ('error:', 'İngilizce hata'),
                ('exception', 'Exception'),
                ('traceback', 'Python traceback'),
                ('tanimlanmamis', 'Tanimlanmamis element'),
                ('bilinmeyen', 'Bilinmeyen komut/degisken'),
                ('syntax error', 'Soz dizimi hatasi'),
                ('name error', 'İsim hatasi'),
                ('type error', 'Tur hatasi'),
                ('value error', 'Deger hatasi'),
                ('division by zero', 'Sifira bolme'),
                ('out of range', 'Aralik disi'),
            ]
            
            for pattern, description in error_patterns:
                if pattern in line_clean:
                    issues.append(f"Satir {i}: {description} - {line.strip()}")
            
            # SELECT CASE ozel kontrolleri
            if 'select case' in line_clean:
                if any(err in line_clean for err in ['hata', 'error', 'tanimlanmamis']):
                    issues.append(f"Satir {i}: SELECT CASE ile ilgili sorun - {line.strip()}")
        
        return issues
    
    def run_single_test(self, test_file: Path, timeout: int = 15) -> Tuple[bool, str, List[str]]:
        """Tek bir test dosyasini calistir ve analiz et"""
        try:
            # Komut hazirla
            cmd = [sys.executable, str(self.interpreter_path), str(test_file)]
            
            # Subprocess baslat
            start_time = time.time()
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'  # Unicode hatalarini handle et
            )
            end_time = time.time()
            
            duration = end_time - start_time
            output = (result.stdout or "") + (result.stderr or "")
            
            # Cikti analizi
            issues = self.analyze_output_for_errors(output, test_file.name)
            
            # Basari durumu
            success = result.returncode == 0
            
            # Log kaydet
            self.logger.log(
                "SUCCESS" if success else "FAIL",
                f"Test: {test_file.name} ({duration:.2f}s)",
                f"Return code: {result.returncode}"
            )
            
            if output.strip():
                self.logger.log("OUTPUT", f"Cikti - {test_file.name}", output.strip())
            
            if issues:
                self.logger.log("WARNING", f"Potansiyel sorunlar - {test_file.name}", "; ".join(issues))
                self.logger.log_error_analysis(test_file.name, issues)
            
            return success, output, issues
            
        except subprocess.TimeoutExpired:
            self.logger.log("TIMEOUT", f"Test zaman asimi: {test_file.name}", f"{timeout}s")
            return False, "Zaman asimi", ["Test belirlenen surede tamamlanamadi"]
            
        except Exception as e:
            self.logger.log("ERROR", f"Test calistirma hatasi: {test_file.name}", str(e))
            return False, str(e), [f"Calistirma hatasi: {str(e)}"]
    
    def run_all_tests(self):
        """Tum testleri calistir"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}🚀 GELİSMİS TEST CALISTIRICI{Colors.END}")
        print(f"{Colors.BLUE}📂 Test dizini: {self.test_dir}{Colors.END}")
        
        # Test dosyalarini kesfet
        test_files = self.discover_tests()
        if not test_files:
            print(f"{Colors.RED}❌ Hic test dosyasi bulunamadi!{Colors.END}")
            return
        
        # Kategorilere ayir
        categories = self.categorize_tests(test_files)
        
        # İstatistikler
        total_tests = len(test_files)
        total_passed = 0
        total_failed = 0
        total_skipped = 0
        total_issues = 0
        
        all_results = []
        
        print(f"{Colors.GREEN}📊 {total_tests} test dosyasi kesfedildi{Colors.END}\n")
        
        # Kategoriler halinde test et
        for category, files in categories.items():
            if not files:
                continue
                
            print(f"\n{Colors.BOLD}{Colors.YELLOW}📁 {category.upper()} KATEGORİSİ ({len(files)} test){Colors.END}")
            print("=" * 70)
            
            for test_file in files:
                print(f"\n{Colors.CYAN}🔍 Test: {test_file.name}{Colors.END}")
                
                # Problematik test kontrolu
                if self.is_problematic_test(test_file):
                    print(f"{Colors.YELLOW}⚠️  Test atlandi - İnteraktif/problematik kod{Colors.END}")
                    self.logger.log("SKIP", f"Problematik test atlandi: {test_file.name}")
                    total_skipped += 1
                    
                    all_results.append({
                        'file': test_file.name,
                        'category': category,
                        'success': None,
                        'skipped': True,
                        'issues': ["İnteraktif/problematik kod"],
                        'output': "",
                        'duration': 0
                    })
                    continue
                
                # Test calistir
                start_time = time.time()
                success, output, issues = self.run_single_test(test_file)
                duration = time.time() - start_time
                
                # Sonucu goster
                if success:
                    if issues:
                        print(f"{Colors.YELLOW}⚠️  BASARILI ama sorunlu ({duration:.2f}s){Colors.END}")
                        print(f"{Colors.YELLOW}   Sorunlar: {len(issues)} adet{Colors.END}")
                        total_issues += len(issues)
                    else:
                        print(f"{Colors.GREEN}✅ BASARILI ({duration:.2f}s){Colors.END}")
                    total_passed += 1
                else:
                    print(f"{Colors.RED}❌ BASARISIZ ({duration:.2f}s){Colors.END}")
                    if issues:
                        print(f"   Sorunlar: {len(issues)} adet")
                    total_failed += 1
                
                # Ciktiyi goster (kisaltilmis)
                if output and output.strip():
                    output_lines = output.strip().split('\n')
                    if len(output_lines) > 3:
                        print(f"{Colors.WHITE}📄 Cikti (ilk 3 satir):{Colors.END}")
                        for line in output_lines[:3]:
                            print(f"   {line}")
                        print(f"   ... (+{len(output_lines)-3} satir daha)")
                    else:
                        print(f"{Colors.WHITE}📄 Cikti:{Colors.END}")
                        for line in output_lines:
                            print(f"   {line}")
                
                # Hatalari goster
                if issues:
                    print(f"{Colors.MAGENTA}🔍 Tespit edilen sorunlar:{Colors.END}")
                    for issue in issues[:3]:  # İlk 3 sorunu goster
                        print(f"   • {issue}")
                    if len(issues) > 3:
                        print(f"   ... (+{len(issues)-3} sorun daha)")
                
                # Sonucu kaydet
                all_results.append({
                    'file': test_file.name,
                    'category': category,
                    'success': success,
                    'skipped': False,
                    'issues': issues,
                    'output': output,
                    'duration': duration
                })
                
                print("-" * 70)
        
        # OZET RAPORU
        print(f"\n{Colors.BOLD}{Colors.WHITE}📊 DETAYLI TEST RAPORU{Colors.END}")
        print("=" * 50)
        print(f"{Colors.GREEN}✅ Basarili testler: {total_passed}{Colors.END}")
        print(f"{Colors.RED}❌ Basarisiz testler: {total_failed}{Colors.END}")
        print(f"{Colors.YELLOW}⚠️  Atlanan testler: {total_skipped}{Colors.END}")
        print(f"{Colors.MAGENTA}🔍 Toplam tespit edilen sorun: {total_issues}{Colors.END}")
        print(f"{Colors.CYAN}📈 Toplam test: {total_tests}{Colors.END}")
        
        if (total_tests - total_skipped) > 0:
            success_rate = (total_passed / (total_tests - total_skipped)) * 100
            print(f"{Colors.BLUE}🎯 Basari orani: {success_rate:.1f}%{Colors.END}")
        else:
            success_rate = 0
        
        # JSON raporu kaydet
        json_report = {
            'summary': {
                'total_tests': total_tests,
                'passed': total_passed,
                'failed': total_failed,
                'skipped': total_skipped,
                'issues_found': total_issues,
                'success_rate': round(success_rate, 1) if (total_tests - total_skipped) > 0 else 0
            },
            'results': all_results,
            'timestamp': datetime.now().isoformat(),
            'categories': {cat: len(files) for cat, files in categories.items() if files}
        }
        
        json_file = self.log_dir / f"advanced_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_report, f, ensure_ascii=False, indent=2)
        
        print(f"\n{Colors.BOLD}💾 Raporlar kaydedildi:{Colors.END}")
        print(f"📄 Metin log: {self.logger.log_file}")
        print(f"❗ Hata log: {self.logger.error_log}")
        print(f"📋 JSON rapor: {json_file}")
        
        # Kritik sorunlari ozetle
        if total_failed > 0 or total_issues > 0:
            print(f"\n{Colors.BOLD}{Colors.RED}⚠️  DİKKATE DEGER DURUMLAR:{Colors.END}")
            if total_failed > 0:
                print(f"   • {total_failed} test basarisiz oldu")
            if total_issues > 0:
                print(f"   • {total_issues} potansiyel sorun tespit edildi")
            print(f"   • Detayli analiz icin {self.logger.error_log} dosyasini inceleyin")
        
        return json_report

def main():
    """Ana fonksiyon"""
    runner = AdvancedTestRunner()
    return runner.run_all_tests()

if __name__ == "__main__":
    main()
