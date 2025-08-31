#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOMPLE TEST RUNNER - Tum BASIC komutlarini test eder
Unicode sorunlari tamamen cozuldu, simdi tum komutlari test edelim
"""

import subprocess
import sys
import os
import time
from datetime import datetime
import json
import glob

class CompleteTestRunner:
    def __init__(self):
        self.test_dir = os.getcwd()
        self.interpreter = "pdsXv11g.py"
        self.results = {
            "passed": [],
            "failed": [],
            "skipped": [],
            "stats": {}
        }
        
    def create_test_files(self):
        """Tum temel BASIC komutlari icin test dosyalari olustur"""
        
        test_cases = {
            "test_print.basx": '''
REM Test PRINT komutlari
PRINT "Hello World"
PRINT "Sayi: ", 42
PRINT "Toplam: ", 10 + 5
            ''',
            
            "test_variables.basx": '''
REM Test degisken atamalari
A = 10
B = 20
C = A + B
PRINT "A =", A
PRINT "B =", B
PRINT "C =", C
            ''',
            
            "test_math.basx": '''
REM Test matematik islemleri
PRINT "Toplama: ", 10 + 5
PRINT "Cikarma: ", 20 - 8
PRINT "Carpma: ", 6 * 7
PRINT "Bolme: ", 15 / 3
PRINT "Mod: ", 17 MOD 5
PRINT "Us: ", 2 ^ 3
            ''',
            
            "test_if_then.basx": '''
REM Test IF-THEN yapisi
A = 10
IF A > 5 THEN PRINT "A buyuk"
IF A < 20 THEN PRINT "A kucuk"
IF A = 10 THEN PRINT "A esit"
            ''',
            
            "test_for_loop.basx": '''
REM Test FOR dongusu
FOR I = 1 TO 5
    PRINT "Sayi: ", I
NEXT I
            ''',
            
            "test_while_loop.basx": '''
REM Test WHILE dongusu  
I = 1
WHILE I <= 3
    PRINT "While: ", I
    I = I + 1
WEND
            ''',
            
            "test_select_case.basx": '''
REM Test SELECT CASE
A = 2
SELECT CASE A
    CASE 1
        PRINT "Bir"
    CASE 2
        PRINT "Iki"
    CASE 3
        PRINT "Uc"
    CASE ELSE
        PRINT "Diger"
END SELECT
            ''',
            
            "test_arrays.basx": '''
REM Test diziler - pdsXv11 syntax
DIM ARR(5)
LET ARR(1) = 10
LET ARR(2) = 20
LET ARR(3) = 30
PRINT "Dizi[1] = ", ARR(1)
PRINT "Dizi[2] = ", ARR(2)
PRINT "Dizi[3] = ", ARR(3)
            ''',
            
            "test_functions.basx": '''
REM Test temel fonksiyonlar - pdsXv11 syntax
PRINT "SIN(0): ", SIN(0)
PRINT "LEN('Hello'): ", LEN("Hello")  
PRINT "LEFT$('Hello', 3): ", LEFT$("Hello", 3)
PRINT "=== Test Complete ==="
            ''',
            
            "test_string_ops.basx": '''
REM Test string islemleri - pdsXv11 syntax
LET A = "Hello"
LET B = "World" 
PRINT A; " "; B
PRINT "Uzunluk: "; LEN(A)
            ''',
            
            "test_goto_gosub.basx": '''
REM Test GOTO - pdsXv11 syntax
PRINT "Baslangic"
GOTO 100
PRINT "Bu calismaz"
100:
PRINT "GOTO calisti"
            '''
        }
        
        created_count = 0
        for filename, content in test_cases.items():
            filepath = os.path.join(self.test_dir, filename)
            if not os.path.exists(filepath):
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content.strip())
                    created_count += 1
                    print(f"✓ {filename} olusturuldu")
                except Exception as e:
                    print(f"✗ {filename} olusturulamadi: {e}")
        
        print(f"\n📋 {created_count} test dosyasi olusturuldu")
        return created_count
        
    def run_single_test(self, test_file):
        """Tek bir test dosyasini calistir"""
        try:
            start_time = time.time()
            
            # Test dosyasini calistir
            result = subprocess.run(
                [sys.executable, self.interpreter, test_file],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8',
                errors='ignore'
            )
            
            duration = time.time() - start_time
            
            # Sonucu degerlendir - daha katı kontrol
            success = True
            error_indicators = [
                "error occurred:",
                "sozdizimi hatasi",
                "Tanimlanmamis degisken:",
                "Bilinmeyen komut:",
                "charmap' codec can't encode",
                "Etiket bulunamadi:",
                "Traceback (most recent call last):",
                "Exception:",
                "Error:",
                "SyntaxError:",
                "NameError:",
                "ValueError:"
            ]
            
            # Stdout ve stderr'da hata göstergelerini ara
            output_text = result.stdout + result.stderr
            for indicator in error_indicators:
                if indicator in output_text:
                    success = False
                    break
            
            # Return code da kontrol et
            if result.returncode != 0:
                success = False
            
            if success:
                return {
                    "status": "PASSED",
                    "duration": duration,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
            else:
                return {
                    "status": "FAILED",
                    "duration": duration,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "returncode": result.returncode,
                    "error_found": "Ciktida hata gostergesi bulundu"
                }
                
        except subprocess.TimeoutExpired:
            return {
                "status": "TIMEOUT",
                "duration": 10.0,
                "error": "Test 10 saniye icinde tamamlanamadi"
            }
        except Exception as e:
            return {
                "status": "ERROR", 
                "error": str(e),
                "duration": 0
            }
    
    def run_all_tests(self):
        """Tum testleri calistir"""
        print("🚀 KOMPLE TEST SUITE BASLATILIYOR")
        print("=" * 60)
        
        # Once test dosyalarini olustur
        self.create_test_files()
        
        # Tum test dosyalarini bul
        test_files = glob.glob("test_*.basx")
        
        if not test_files:
            print("❌ Test dosyasi bulunamadi!")
            return
            
        print(f"\n📊 {len(test_files)} test dosyasi bulundu")
        print("=" * 60)
        
        passed_count = 0
        failed_count = 0
        
        for i, test_file in enumerate(test_files, 1):
            print(f"\n🔍 [{i}/{len(test_files)}] Test: {test_file}")
            print("-" * 40)
            
            result = self.run_single_test(test_file)
            
            if result["status"] == "PASSED":
                print(f"✅ BASARILI ({result['duration']:.2f}s)")
                if result["stdout"].strip():
                    print("📤 Cikti:")
                    for line in result["stdout"].strip().split('\n')[-5:]:  # Son 5 satir
                        print(f"   {line}")
                self.results["passed"].append({
                    "file": test_file,
                    "duration": result["duration"],
                    "output": result["stdout"]
                })
                passed_count += 1
                
            else:
                print(f"❌ BASARISIZ ({result.get('duration', 0):.2f}s)")
                if "stdout" in result and result["stdout"].strip():
                    print("📤 Cikti:")
                    for line in result["stdout"].strip().split('\n')[-3:]:
                        print(f"   {line}")
                if "stderr" in result and result["stderr"].strip():
                    print("⚠️ Hata:")
                    for line in result["stderr"].strip().split('\n')[-3:]:
                        print(f"   {line}")
                        
                self.results["failed"].append({
                    "file": test_file,
                    "error": result.get("error", "Bilinmeyen hata"),
                    "duration": result.get("duration", 0),
                    "returncode": result.get("returncode", -1)
                })
                failed_count += 1
        
        # Ozet rapor
        print("\n" + "=" * 60)
        print("📊 KOMPLE TEST RAPORU")
        print("=" * 60)
        print(f"✅ Basarili testler: {passed_count}")
        print(f"❌ Basarisiz testler: {failed_count}")
        print(f"📈 Toplam test: {len(test_files)}")
        print(f"🎯 Basari orani: {(passed_count/len(test_files)*100):.1f}%")
        
        # JSON rapor kaydet
        self.results["stats"] = {
            "total": len(test_files),
            "passed": passed_count,
            "failed": failed_count,
            "success_rate": passed_count/len(test_files)*100,
            "timestamp": datetime.now().isoformat()
        }
        
        report_file = f"complete_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, ensure_ascii=False, indent=2)
            print(f"📋 JSON rapor: {report_file}")
        except Exception as e:
            print(f"⚠️ Rapor kaydedilemedi: {e}")
        
        if failed_count > 0:
            print(f"\n⚠️ {failed_count} test basarisiz oldu.")
            print("Basarisiz testler:")
            for fail in self.results["failed"]:
                print(f"   • {fail['file']}")
        else:
            print("\n🎉 TUM TESTLER BASARILI!")
            
        return passed_count, failed_count

def main():
    runner = CompleteTestRunner()
    runner.run_all_tests()

if __name__ == "__main__":
    main()
