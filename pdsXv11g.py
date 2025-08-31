# pdsXv11g.py - Modern BASIC Interpreter with Virtual Environment Management

# Sistem modülleri
import sys
import os
import subprocess
import argparse
import json
import logging
import traceback
import collections
import time
import re
import math
import random
import struct
import shutil
import glob
import socket
import sqlite3
import ast
import asyncio
import datetime
import threading
import queue
import io
import importlib.util
import importlib
import ctypes
import inspect

# Bağımlılık yönetimi ve paket gereksinimleri
REQUIRED_PACKAGES = {
    'numpy': {'version': '1.21.0', 'module': None},  
    'pandas': {'version': '1.3.0', 'module': None},
    'scipy': {'version': '1.7.0', 'module': None},
    'requests': {'version': '2.26.0', 'module': None}, 
    'psutil': {'version': '5.8.0', 'module': None},
    'pdfplumber': {'version': '0.7.0', 'module': None}
}

def check_import(package_name):
    try:
        spec = importlib.util.find_spec(package_name)
        if spec is None:
            print(f"{package_name} paketi bulunamadı.")
            return None
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"{package_name} import edilirken hata oluştu: {str(e)}")
        return None

np = check_import('numpy')
pd = check_import('pandas')

scipy = check_import('scipy')
if scipy:
    stats = scipy.stats
else:
    stats = None

requests = check_import('requests')
psutil = check_import('psutil') 
pdfplumber = check_import('pdfplumber')
try:
    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    import requests
    import psutil
    import pdfplumber
    import socket
    import ctypes
    import threading
    import multiprocessing
    import datetime
    import queue
    import io
    import json
    import re
    import math
    import random
    import struct
    import shutil
    import glob
    import sqlite3
    import ast
    import asyncio
    from packaging import version

try:
    import numpy as np
except ImportError:
    np = None

from pathlib import Path
from collections import defaultdict, namedtuple
from datetime import datetime
from types import SimpleNamespace
from abc import ABC, abstractmethod

# Sanal Ortam ve Bagimlilik Yonetim Sistemi
class VirtualEnvironmentManager:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.venv_dir = self.project_dir / "pdsxv11_venv"
        self.requirements = REQUIRED_PACKAGES
        self.installed_packages_file = self.venv_dir / "installed_packages.json"
        
    def _check_dependencies(self):
        """Tüm gerekli paketlerin yüklü olup olmadığını kontrol et"""
        return all(self._check_package_installed(pkg) for pkg in self.requirements)
        
    def _check_package_installed(self, package_name):
        """Paketin yüklü olup olmadığını kontrol et"""
        return package_name in REQUIRED_PACKAGES and REQUIRED_PACKAGES[package_name]['module'] is not None
    
    def import_modules(self):
        """Gerekli modülleri import et"""
        if not self._check_dependencies():
            return False
            
        # Modülleri yükle
        self.install_requirements()
        return True
    
    def get_venv_python(self):
        """Sanal ortam Python yolunu dondur"""
        if os.name == 'nt':  # Windows
            return self.venv_dir / "Scripts" / "python.exe"
        else:  # Linux/Mac
            return self.venv_dir / "bin" / "python"
    
    def get_venv_pip(self):
        """Sanal ortam pip yolunu dondur"""
        if os.name == 'nt':  # Windows
            return self.venv_dir / "Scripts" / "pip.exe"
        else:  # Linux/Mac
            return self.venv_dir / "bin" / "pip"
    
    def _save_installed_packages(self):
        """Kurulu kütüphaneleri kaydet"""
        try:
            self.venv_dir.mkdir(parents=True, exist_ok=True)
            with open(self.installed_packages_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "packages": {
                        name: pkg_info["version"] 
                        for name, pkg_info in self.requirements.items()
                        if self._check_package_installed(name)
                    },
                    "timestamp": time.time()
                }, f)
        except Exception as e:
            print(f"Paket kayıt hatası: {str(e)}")

    def _load_installed_packages(self):
        """Kurulu kütüphaneleri yükle"""
        try:
            if self.installed_packages_file.exists():
                with open(self.installed_packages_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get("packages", {})
        except Exception as e:
            print(f"Paket okuma hatası: {str(e)}")
        return {}

    def is_package_installed(self, package):
        """Paketin kurulu olup olmadigini kontrol et"""
        python_path = self.get_venv_python()
        try:
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            env['PYTHONLEGACYWINDOWSSTDIO'] = '1'
            
            # Paket adini temizle (versiyonu varsa kaldir)
            clean_package = package.split('=')[0].split('>')[0].split('<')[0].strip()
            
            # Bazi paketlerin import adi farkli olabilir
            import_name_map = {
                'beautifulsoup4': 'bs4',
                'pillow': 'PIL',
                'pdfplumber': 'pdfplumber',
                'packaging': 'packaging'
            }
            
            import_name = import_name_map.get(clean_package, clean_package)
            
            result = subprocess.run([
                str(python_path), '-c', f'import {import_name}'
            ], check=True, capture_output=True, text=True, env=env)
            return True
        except subprocess.CalledProcessError:
            return False

    def install_requirements(self):
        """Gerekli kütüphaneleri kur"""
        pip_path = self.get_venv_pip()
        
        for package_name, pkg_info in self.requirements.items():
            # Once kurulu mu kontrol et
            if self.is_package_installed(package_name):
                print(f"{package_name} zaten yüklü.")
                continue
                
            try:
                # Windows encoding fix for Turkish characters
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                env['PYTHONLEGACYWINDOWSSTDIO'] = '1'
                
                # Paket versiyonunu al
                package_spec = f"{package_name}=={pkg_info['version']}"
                
                # Paketi kur
                result = subprocess.run(
                    [str(pip_path), 'install', package_spec],
                    check=True,
                    capture_output=True,
                    text=True,
                    env=env
                )
                print(f"✓ {package_name} başarıyla kuruldu")
                
                # Modülü yükle
                try:
                    pkg_info['module'] = check_import(package_name)
                except Exception as e:
                    print(f"Modül yükleme hatası ({package_name}): {str(e)}")
                    return False
                    
            except subprocess.CalledProcessError as e:
                print(f"✗ {package_name} kurulamadı: {e}")
                print(f"Hata oluştu: {str(e)}")
                return False
        
        # Kurulu paketleri kaydet
        self._save_installed_packages()
        print("Tüm kütüphaneler başarıyla kuruldu!")
        return True

    def is_venv_ready(self):
        """Sanal ortamın hazır olup olmadığını kontrol et"""
        try:
            # 1. Sanal ortam dizini var mı?
            if not self.venv_dir.exists():
                return False
                
            # 2. Python ve pip çalıştırılabilir dosyaları var mı?
            python_path = self.get_venv_python()
            pip_path = self.get_venv_pip()
            if not python_path.exists() or not pip_path.exists():
                return False
                
            # 3. Versiyonları kontrol et
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            # Python versiyonunu kontrol et
            result = subprocess.run(
                [str(python_path), '--version'],
                check=True, capture_output=True, text=True, env=env
            )
            python_version = result.stdout.strip()
            if not python_version.startswith('Python 3.'):
                return False
                
            # pip versiyonunu kontrol et  
            result = subprocess.run(
                [str(pip_path), '--version'],
                check=True, capture_output=True, text=True, env=env
            )
            if 'pip' not in result.stdout.lower():
                return False
            
            # 4. Kritik paketleri kontrol et
            critical_packages = ['numpy', 'pandas', 'requests']
            for pkg in critical_packages:
                if pkg in self.requirements and not self.is_package_installed(pkg):
                    return False
                    
            return True
            
        except (subprocess.CalledProcessError, OSError, Exception) as e:
            print(f"Sanal ortam kontrolünde hata: {str(e)}")
            return False
        if not self.installed_packages_file.exists():
            return False
            
        try:
            with open(self.installed_packages_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                cached_packages = set(data.get("packages", []))
                required_packages = set(self.requirements)
                
                # Tum paketler cache'de var mi?
                if not required_packages.issubset(cached_packages):
                    return False
                    
            # Hizli import testi - sadece kritik paketleri test et
            python_path = self.get_venv_python()
            env = os.environ.copy()
            env['PYTHONIOENCODING'] = 'utf-8'
            
            # Kritik paketleri test et
            critical_packages = ['requests', 'numpy', 'pandas', 'bs4']  # bs4 for beautifulsoup4
            
            for pkg in critical_packages:
                try:
                    result = subprocess.run([
                        str(python_path), '-c', f'import {pkg}'
                    ], check=True, capture_output=True, text=True, env=env, timeout=10)
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                    return False
                    
            return True
            
        except Exception:
            return False

    def setup_environment(self):
        """Ortamı ve bağımlılıkları yönet"""
        missing = []
        for pkg_name in self.requirements:
            if not self.is_package_installed(pkg_name):
                missing.append(pkg_name)
        
        if missing:
            print(f"Eksik kütüphaneler: {missing}")
            return self.install_requirements()
        
        return True
        
    def _check_dependencies(self):
        """Gerekli paketleri kontrol et"""
        missing = []
        for pkg_name in REQUIRED_PACKAGES:
            if not self._check_package_installed(pkg_name):
                missing.append(pkg_name)
        
        if missing:
            print(f"Eksik kütüphaneler: {missing}")
            return False
        return True
    
    def run_in_venv(self, script_args):
        """Scripti sanal ortamda çalıştır"""
        # Sanal ortamı kontrol et
        if not self.is_venv_ready():
            print("Sanal ortam hazır değil. Lütfen önce --setup-venv ile kurun.")
            return False
            
        python_path = self.get_venv_python()
        
        # Mevcut scriptin yolunu al
        try:
            current_script = Path(sys.argv[0]).resolve()
        except Exception as e:
            print(f"Script yolu alınamadı: {str(e)}")
            return False
        
        # Script argümanlarını işle - dosya yolunu absolute yap
        processed_args = []
        for arg in script_args:
            if arg.endswith(('.basx', '.pdsx', '.bas', '.libx', '.hx')):
                try:
                    file_path = Path(arg)
                    if not file_path.is_absolute():
                        file_path = Path.cwd() / file_path
                    if not file_path.exists():
                        print(f"Uyarı: {arg} dosyası bulunamadı")
                        return False
                    processed_args.append(str(file_path))
                except Exception as e:
                    print(f"Dosya yolu işlenirken hata: {str(e)}")
                    return False
            else:
                processed_args.append(arg)
        
        # Sanal ortamda çalıştır
        cmd = [str(python_path), str(current_script)] + processed_args + ['--no-venv']
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            if result.stderr:
                print(f"Uyarı: {result.stderr}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Program çalıştırma hatası: {str(e)}")
            if e.stdout:
                print(f"Program çıktısı:\n{e.stdout}")
            if e.stderr:
                print(f"Hata çıktısı:\n{e.stderr}")
            return False

def setup_argument_parser():
    """Komut satiri argumanlarini kur"""
    parser = argparse.ArgumentParser(
        description='pdsXv11 - Modern BASIC Yorumlayicisi',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Kullanim Ornekleri:
  python pdsxv11g.py                    # Etkilesimli REPL modu
  python pdsxv11g.py program.basx       # Dosya calistir
  python pdsxv11g.py -i                 # Zorla etkilesimli mod
  python pdsxv11g.py --setup-venv       # Sanal ortami kur
  python pdsxv11g.py --check-deps       # Bagimliliklari kontrol et
        """)
    
    parser.add_argument('file', nargs='?', help='Calistirilacak .basx dosyasi')
    parser.add_argument('-i', '--interactive', action='store_true', 
                       help='Etkilesimli REPL modunu zorla')
    parser.add_argument('--setup-venv', action='store_true',
                       help='Sanal ortami kur ve gereksinimleri yukle')
    parser.add_argument('--check-deps', action='store_true',
                       help='Bagimliliklari kontrol et')
    parser.add_argument('--no-venv', action='store_true',
                       help='Sanal ortam kontrolunu atla (dahili kullanim)')
    parser.add_argument('--debug', action='store_true',
                       help='Hata ayiklama modunu etkinlestir')
    parser.add_argument('--trace', action='store_true',
                       help='İz surme modunu etkinlestir')
    
    return parser

# Ana program başlatma mantığı
def main():
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    if args.debug:
        print("Ana program başlatılıyor...")
        print(f"Argümanlar: {args}")
    
    venv_manager = VirtualEnvironmentManager()
    
    # Sanal ortam yönetimi
    if not args.no_venv:
        if args.setup_venv:
            if venv_manager.install_requirements():
                print("Sanal ortam hazır!")
                sys.exit(0)
            else:
                print("Sanal ortam kurulumu başarısız!")
                sys.exit(1)
        
        if args.check_deps:
            if venv_manager._check_dependencies():
                print("Tüm bağımlılıklar mevcut!")
                sys.exit(0)
            else:
                print("Eksik bağımlılıklar var!")
                sys.exit(1)
        
        # Otomatik ortam kontrolü
        if not venv_manager.is_venv_ready():
            print("Sanal ortam hazır değil. Lütfen önce --setup-venv ile kurun.")
            sys.exit(1)
            
        # Bağımlılıkları kontrol et
        if not venv_manager._check_dependencies():
            print("Eksik bağımlılıklar var. Yükleniyor...")
            if not venv_manager.install_requirements():
                print("Bağımlılık yüklemesi başarısız!")
                sys.exit(1)

    # Bu noktada tüm gerekli modüller yüklendi
    return run_interpreter(args)

def run_interpreter(args):
    """Ana yorumlayıcıyı çalıştır"""
    try:
        # Global referansları güncelle
        globals().update({
            'np': REQUIRED_PACKAGES['numpy']['module'],
            'pd': REQUIRED_PACKAGES['pandas']['module'],
            'stats': REQUIRED_PACKAGES.get('scipy.stats', {}).get('module'),
            'requests': REQUIRED_PACKAGES['requests']['module'],
            'psutil': REQUIRED_PACKAGES['psutil']['module'],
            'pdfplumber': REQUIRED_PACKAGES['pdfplumber']['module']
        })

        if args.debug:
            print("Ana yorumlayıcı başlatılıyor...")
        
    except ImportError as e:
        print(f"error occurred: {str(e)}")
        print("Lutfen sanal ortami kurun: python pdsxv11g.py --setup-venv")
        sys.exit(1)
    
    # Yorumlayiciyi baslat
    if args.debug:
        print("pdsXv11 Yorumlayicisi baslatiliyor...")
    interpreter = pdsXv11()
    
    if args.debug:
        interpreter.debug_mode = True
    
    if args.file:
        # Dosya modu
        if not os.path.exists(args.file):
            print(f"Hata: Dosya bulunamadi: {args.file}")
            sys.exit(1)
        
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                code = f.read()
            interpreter.run(code)
        except Exception as e:
            print(f"Dosya calistirma hatasi: {e}")
            sys.exit(1)
    else:
        # Etkilesimli mod
        interpreter.start_repl()

# Loglama Ayarlari
logging.basicConfig(filename='interpreter_errors.log', level=logging.ERROR, format='%(asctime)s - %(message)s')

# Yardimci Siniflar
class MemoryManager:
    def __init__(self):
        self.heap = {}
        self.ref_counts = {}

    def allocate(self, size: int):
        ptr = id(bytearray(size))
        self.heap[ptr] = bytearray(size)
        self.ref_counts[ptr] = 1
        return ptr

    def release(self, ptr: int):
        if ptr in self.ref_counts:
            self.ref_counts[ptr] -= 1
            if self.ref_counts[ptr] == 0:
                del self.heap[ptr]
                del self.ref_counts[ptr]

    def dereference(self, ptr: int):
        return self.heap.get(ptr, None)

    def set_value(self, ptr: int, value):
        if ptr in self.heap:
            if isinstance(value, (int, float)):
                self.heap[ptr][:] = struct.pack('d', float(value))
            elif isinstance(value, str):
                self.heap[ptr][:] = value.encode()

    def sizeof(self, obj):
        if isinstance(obj, (int, float)):
            return 8
        elif isinstance(obj, str):
            return len(obj.encode())
        elif isinstance(obj, (list, np.ndarray)):
            return obj.nbytes if hasattr(obj, 'nbytes') else len(obj) * 8
        return 0

class StructInstance:
    def __init__(self, fields, type_table):
        self.fields = {name: None for name, _ in fields}
        self.field_types = {name: type_name for name, type_name in fields}
        self.type_table = type_table
        self.sizes = {name: self._get_size(type_name) for name, type_name in fields}
        self.offsets = {}
        offset = 0
        for name in self.fields:
            self.offsets[name] = offset
            offset += self.sizes[name]

    def set_field(self, field_name, value):
        if field_name not in self.fields:
            raise ValueError(f"Gecersiz alan: {field_name}")
        expected_type = self.type_table.get(self.field_types[field_name].upper(), object)
        if not isinstance(value, expected_type):
            try:
                value = expected_type(value)
            except Exception:
                raise TypeError(f"{field_name} icin beklenen tip {expected_type.__name__}, ancak {type(value).__name__} alindi")
        self.fields[field_name] = value

    def get_field(self, field_name):
        if field_name not in self.fields:
            raise ValueError(f"Gecersiz alan: {field_name}")
        return self.fields[field_name]

    def _get_size(self, type_name):
        size_map = {
            "INTEGER": 4, "DOUBLE": 8, "STRING": 8, "BYTE": 1,
            "SHORT": 2, "LONG": 8, "SINGLE": 4, "LIST": 8, "ARRAY": 8, "DICT": 8
        }
        return size_map.get(type_name.upper(), 8)

class UnionInstance:
    def __init__(self, fields, type_table):
        self.fields = {name: None for name, _ in fields}  # Uyumluluk için fields dictionary
        self.field_types = {name: type_name for name, type_name in fields}
        self.type_table = type_table
        self.active_field = None
        self.value = bytearray(8)
        self.sizes = {name: self._get_size(type_name) for name, type_name in fields}

    def set_field(self, field_name, value):
        if field_name not in self.field_types:
            raise ValueError(f"Gecersiz alan: {field_name}")
        expected_type = self.type_table.get(self.field_types[field_name].upper(), object)
        if not isinstance(value, expected_type):
            try:
                value = expected_type(value)
            except Exception:
                raise TypeError(f"{field_name} icin beklenen tip {expected_type.__name__}, ancak {type(value).__name__} alindi")
        
        # Fields dictionary'yi de guncelle
        self.fields[field_name] = value
        self.active_field = field_name
        fmt = {"INTEGER": "i", "DOUBLE": "d", "STRING": "8s", "BYTE": "b",
               "SHORT": "h", "LONG": "q", "SINGLE": "f"}.get(self.field_types[field_name].upper(), "8s")
        if fmt == "8s":
            value = str(value).encode('utf-8')[:8].ljust(8, b'\0')
        else:
            value = struct.pack(fmt, value)
        self.value[:len(value)] = value

    def get_field(self, field_name):
        if field_name not in self.field_types:
            raise ValueError(f"Gecersiz alan: {field_name}")
        if self.active_field != field_name:
            raise ValueError(f"{field_name} alani aktif degil")
        
        # Once fields dictionary'den donmeyi dene
        if field_name in self.fields and self.fields[field_name] is not None:
            return self.fields[field_name]
            
        fmt = {"INTEGER": "i", "DOUBLE": "d", "STRING": "8s", "BYTE": "b",
               "SHORT": "h", "LONG": "q", "SINGLE": "f"}.get(self.field_types[field_name].upper(), "8s")
        try:
            if fmt == "8s":
                return self.value.decode('utf-8').rstrip('\0')
            return struct.unpack(fmt, self.value[:self.sizes[field_name]])[0]
        except Exception:
            raise ValueError(f"{field_name} alanindan veri okunamadi")

    def _get_size(self, type_name):
        size_map = {
            "INTEGER": 4, "DOUBLE": 8, "STRING": 8, "BYTE": 1,
            "SHORT": 2, "LONG": 8, "SINGLE": 4, "LIST": 8, "ARRAY": 8, "DICT": 8
        }
        return size_map.get(type_name.upper(), 8)

class Pointer:
    def __init__(self, address, target_type, interpreter):
        self.address = address
        self.target_type = target_type
        self.interpreter = interpreter

    def dereference(self):
        if self.address not in self.interpreter.memory_pool:
            raise ValueError(f"Gecersiz isaretci adresi: {self.address}")
        value = self.interpreter.memory_pool[self.address]["value"]
        expected_type = self.interpreter.type_table.get(self.target_type.upper(), object)
        if not isinstance(value, expected_type):
            raise TypeError(f"Beklenen tip {expected_type.__name__}, ancak {type(value).__name__} bulundu")
        return value

    def set(self, value):
        if self.address not in self.interpreter.memory_pool:
            raise ValueError(f"Gecersiz isaretci adresi: {self.address}")
        expected_type = self.interpreter.type_table.get(self.target_type.upper(), object)
        if not isinstance(value, expected_type):
            try:
                value = expected_type(value)
            except Exception:
                raise TypeError(f"Beklenen tip {expected_type.__name__}, ancak {type(value).__name__} alindi")
        self.interpreter.memory_pool[self.address]["value"] = value

    def add_offset(self, offset):
        new_address = self.address + offset
        if new_address not in self.interpreter.memory_pool:
            raise ValueError(f"Gecersiz isaretci aritmetigi: {new_address}")
        return Pointer(new_address, self.target_type, self.interpreter)

# STRUCT nested field initialization helper
def _initialize_nested_struct_fields(interpreter, struct_instance, fields):
    """Nested STRUCT field'larını initialize et"""
    for field_name, field_type in fields:
        if field_type in interpreter.types:
            # Bu bir user-defined type
            type_info = interpreter.types[field_type]
            if type_info["kind"] == "STRUCT":
                # Nested STRUCT oluştur
                nested_struct = StructInstance(type_info["fields"], interpreter.type_table)
                _initialize_nested_struct_fields(interpreter, nested_struct, type_info["fields"])
                struct_instance.set_field(field_name, nested_struct)
            elif type_info["kind"] == "UNION":
                # Nested UNION oluştur
                nested_union = UnionInstance(type_info["fields"], interpreter.type_table)
                struct_instance.set_field(field_name, nested_union)
        else:
            # Basic type - default değer ile initialize et
            default_value = interpreter.type_table.get(field_type.upper(), lambda: None)()
            if default_value is not None:
                struct_instance.set_field(field_name, default_value)

# LibXCore Sinifi
class LibXCore:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.default_encoding = "utf-8"
        self.supported_encodings = [
            "utf-8", "cp1254", "iso-8859-9", "ascii", "utf-16", "utf-32",
            "cp1252", "iso-8859-1", "windows-1250", "latin-9",
            "cp932", "gb2312", "gbk", "euc-kr", "cp1251", "iso-8859-5",
            "cp1256", "iso-8859-6", "cp874", "iso-8859-7", "cp1257", "iso-8859-8"
        ]
        self.metadata = {"libx_core": {"version": "1.0.0", "dependencies": []}}
        self.stacks = {}
        self.queues = {}
        
        # Gerekli modülleri al
        self.np = REQUIRED_PACKAGES['numpy']['module']
        self.pd = REQUIRED_PACKAGES['pandas']['module']
        self.stats = REQUIRED_PACKAGES.get('scipy.stats', {}).get('module')
        self.requests = REQUIRED_PACKAGES['requests']['module']
        self.psutil = REQUIRED_PACKAGES['psutil']['module']
        self.pdfplumber = REQUIRED_PACKAGES['pdfplumber']['module']

    def omega(self, *args):
        params = args[:-1]
        expr = args[-1]
        return lambda *values: eval(expr, {p: v for p, v in zip(params, values)})

    def list_lib(self, lib_name):
        module = self.interpreter.modules.get(lib_name, {})
        return {"functions": list(module.get("functions", {}).keys()), "classes": list(module.get("classes", {}).keys())}

    def each(self, func, iterable):
        for item in iterable:
            func(item)

    def select(self, func, iterable):
        return [item for item in iterable if func(item)]

    def insert(self, collection, value, index=None, key=None):
        if isinstance(collection, list):
            if index is None:
                collection.append(value)
            else:
                collection.insert(index, value)
        elif isinstance(collection, dict):
            if key is None:
                raise Exception("DICT icin anahtar gerekli")
            collection[key] = value
        else:
            raise Exception("Gecersiz veri tipi")

    def remove(self, collection, index=None, key=None):
        if isinstance(collection, list):
            if index is None:
                raise Exception("Liste icin indeks gerekli")
            collection.pop(index)
        elif isinstance(collection, dict):
            if key is None:
                raise Exception("DICT icin anahtar gerekli")
            collection.pop(key, None)
        else:
            raise Exception("Gecersiz veri tipi")

    def clear(self, collection):
        if isinstance(collection, (list, dict)):
            collection.clear()
        else:
            raise Exception("Gecersiz veri tipi")

    def slice(self, iterable, start, end=None):
        return iterable[start:end]

    def keys(self, obj):
        if isinstance(obj, dict):
            return list(obj.keys())
        raise Exception("Yalnizca DICT icin gecerli")

    def time_now(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def date_now(self):
        return datetime.now().strftime("%Y-%m-%d")

    def timer(self):
        return time.time()

    def random_int(self, min_val, max_val):
        return random.randint(min_val, max_val)

    def assert_(self, condition, message):
        if not condition:
            raise Exception(f"Assert hatasi: {message}")

    def log(self, message, level="INFO", target=None):
        log_message = f"[{level}] {message}"
        if target:
            with open(target, "a", encoding=self.default_encoding) as f:
                f.write(log_message + "\n")
        else:
            print(log_message)

    def ifthen(self, condition, value1, value2):
        return value1 if condition else value2

    def exists(self, path):
        return os.path.exists(path)

    def mkdir(self, path):
        os.makedirs(path, exist_ok=True)

    def getenv(self, name):
        return os.getenv(name)

    def exit(self, code):
        sys.exit(code)

    def join_path(self, *parts):
        return os.path.join(*parts)

    def copy_file(self, src, dst):
        shutil.copy(src, dst)

    def move_file(self, src, dst):
        shutil.move(src, dst)

    def delete_file(self, path):
        os.remove(path)

    def floor(self, x):
        return math.floor(x)

    def ceil(self, x):
        return math.ceil(x)

    def split(self, s, sep):
        return s.split(sep)

    def join(self, iterable, sep):
        return sep.join(iterable)

    def read_lines(self, path):
        with open(path, "r", encoding=self.default_encoding) as f:
            return f.readlines()

    def write_json(self, obj, path):
        with open(path, "w", encoding=self.default_encoding) as f:
            json.dump(obj, f)

    def read_json(self, path):
        """JSON dosyasını oku"""
        with open(path, "r", encoding=self.default_encoding) as f:
            return json.load(f)
            
    def json_query(self, obj, query):
        """JSON nesnesinde sorgu yap (örn: "user.address.city")"""
        parts = query.split('.')
        result = obj
        try:
            for part in parts:
                if isinstance(result, dict):
                    result = result[part]
                elif isinstance(result, list) and part.isdigit():
                    result = result[int(part)]
                else:
                    raise KeyError(f"Geçersiz yol: {part}")
            return result
        except (KeyError, IndexError, TypeError) as e:
            raise Exception(f"JSON sorgu hatası: {str(e)}")
            
    def json_validate(self, obj, schema):
        """JSON şemasına göre doğrulama yap"""
        try:
            from jsonschema import validate
            validate(instance=obj, schema=schema)
            return True
        except Exception as e:
            raise Exception(f"JSON şema doğrulama hatası: {str(e)}")
            
    def json_format(self, obj, indent=2):
        """JSON nesnesini formatla"""
        return json.dumps(obj, indent=indent, ensure_ascii=False)
        
    def json_schema_create(self, obj):
        """JSON şeması oluştur"""
        def get_type(value):
            if isinstance(value, dict):
                return {
                    "type": "object",
                    "properties": {k: get_type(v) for k, v in value.items()},
                    "required": list(value.keys())
                }
            elif isinstance(value, list):
                if value:
                    return {
                        "type": "array",
                        "items": get_type(value[0])
                    }
                return {"type": "array"}
            elif isinstance(value, bool):
                return {"type": "boolean"}
            elif isinstance(value, int):
                return {"type": "integer"}
            elif isinstance(value, float):
                return {"type": "number"}
            elif isinstance(value, str):
                return {"type": "string"}
            elif value is None:
                return {"type": "null"}
            return {}

        try:
            schema = get_type(obj)
            schema["$schema"] = "http://json-schema.org/draft-07/schema#"
            return schema
        except Exception as e:
            raise Exception(f"JSON şema oluşturma hatası: {str(e)}")
            
    def json_to_csv(self, obj, file_path, flatten=False):
        """JSON'ı CSV'ye dönüştür"""
        try:
            import pandas as pd
            if isinstance(obj, list):
                df = pd.json_normalize(obj) if flatten else pd.DataFrame(obj)
            else:
                df = pd.json_normalize([obj]) if flatten else pd.DataFrame([obj])
            df.to_csv(file_path, index=False, encoding='utf-8')
            return True
        except Exception as e:
            raise Exception(f"JSON->CSV dönüşüm hatası: {str(e)}")
            
    def json_to_yaml(self, obj, file_path):
        """JSON'ı YAML'a dönüştür"""
        try:
            import yaml
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(obj, f, allow_unicode=True, sort_keys=False)
            return True
        except Exception as e:
            raise Exception(f"JSON->YAML dönüşüm hatası: {str(e)}")
            
    def xml_to_csv(self, xml_path, csv_path, xpath="./*"):
        """XML'i CSV'ye dönüştür"""
        try:
            import pandas as pd
            from lxml import etree
            tree = etree.parse(xml_path)
            data = []
            for element in tree.xpath(xpath):
                row = {}
                for child in element:
                    row[child.tag] = child.text
                data.append(row)
            df = pd.DataFrame(data)
            df.to_csv(csv_path, index=False, encoding='utf-8')
            return True
        except Exception as e:
            raise Exception(f"XML->CSV dönüşüm hatası: {str(e)}")
            
    def xml_to_yaml(self, xml_path, yaml_path):
        """XML'i YAML'a dönüştür"""
        try:
            import yaml
            from lxml import etree
            def xml_to_dict(element):
                result = {}
                for child in element:
                    if len(child) > 0:
                        value = xml_to_dict(child)
                    else:
                        value = child.text or ''
                    if child.tag in result:
                        if not isinstance(result[child.tag], list):
                            result[child.tag] = [result[child.tag]]
                        result[child.tag].append(value)
                    else:
                        result[child.tag] = value
                return result
                
            tree = etree.parse(xml_path)
            root = tree.getroot()
            data = {root.tag: xml_to_dict(root)}
            
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, allow_unicode=True, sort_keys=False)
            return True
        except Exception as e:
            raise Exception(f"XML->YAML dönüşüm hatası: {str(e)}")
            
    def json_visualize(self, obj, title="JSON Görselleştirme"):
        """JSON'ı görselleştir"""
        try:
            import networkx as nx
            import matplotlib.pyplot as plt
            
            G = nx.Graph()
            pos = {}
            labels = {}
            
            def add_nodes(data, parent=None, x=0, y=0):
                if isinstance(data, dict):
                    for i, (key, value) in enumerate(data.items()):
                        node_id = f"{key}_{id(value)}"
                        G.add_node(node_id)
                        labels[node_id] = key
                        pos[node_id] = (x, y-i)
                        if parent:
                            G.add_edge(parent, node_id)
                        if isinstance(value, (dict, list)):
                            add_nodes(value, node_id, x+1, y-i)
                        else:
                            child_id = f"{value}_{id(value)}"
                            G.add_node(child_id)
                            labels[child_id] = str(value)
                            pos[child_id] = (x+1, y-i)
                            G.add_edge(node_id, child_id)
                elif isinstance(data, list):
                    for i, item in enumerate(data):
                        node_id = f"item_{i}_{id(item)}"
                        G.add_node(node_id)
                        labels[node_id] = f"[{i}]"
                        pos[node_id] = (x, y-i)
                        if parent:
                            G.add_edge(parent, node_id)
                        if isinstance(item, (dict, list)):
                            add_nodes(item, node_id, x+1, y-i)
                        else:
                            child_id = f"{item}_{id(item)}"
                            G.add_node(child_id)
                            labels[child_id] = str(item)
                            pos[child_id] = (x+1, y-i)
                            G.add_edge(node_id, child_id)
            
            add_nodes(obj)
            plt.figure(figsize=(12, 8))
            nx.draw(G, pos=pos, labels=labels, with_labels=True, 
                   node_color='lightblue', node_size=2000, 
                   font_size=8, font_weight='bold')
            plt.title(title)
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise Exception(f"JSON görselleştirme hatası: {str(e)}")
            
    def xml_visualize(self, xml_path, title="XML Görselleştirme"):
        """XML'i görselleştir"""
        try:
            import networkx as nx
            import matplotlib.pyplot as plt
            from lxml import etree
            
            tree = etree.parse(xml_path)
            root = tree.getroot()
            
            G = nx.Graph()
            pos = {}
            labels = {}
            
            def add_nodes(element, parent=None, x=0, y=0):
                node_id = f"{element.tag}_{id(element)}"
                G.add_node(node_id)
                labels[node_id] = element.tag
                pos[node_id] = (x, y)
                
                if parent:
                    G.add_edge(parent, node_id)
                    
                if element.text and element.text.strip():
                    text_id = f"text_{id(element.text)}"
                    G.add_node(text_id)
                    labels[text_id] = element.text.strip()
                    pos[text_id] = (x+0.5, y)
                    G.add_edge(node_id, text_id)
                    
                for i, child in enumerate(element):
                    add_nodes(child, node_id, x+1, y-i)
                    
                for i, (key, value) in enumerate(element.attrib.items()):
                    attr_id = f"{key}_{id(value)}"
                    G.add_node(attr_id)
                    labels[attr_id] = f"@{key}={value}"
                    pos[attr_id] = (x+0.5, y+i+1)
                    G.add_edge(node_id, attr_id)
            
            add_nodes(root)
            plt.figure(figsize=(12, 8))
            nx.draw(G, pos=pos, labels=labels, with_labels=True,
                   node_color='lightgreen', node_size=2000,
                   font_size=8, font_weight='bold')
            plt.title(title)
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise Exception(f"XML görselleştirme hatası: {str(e)}")
            
    def json_merge(self, obj1, obj2):
        """İki JSON nesnesini birleştir"""
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            result = obj1.copy()
            for key, value in obj2.items():
                if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = self.json_merge(result[key], value)
                else:
                    result[key] = value
            return result
        elif isinstance(obj1, list) and isinstance(obj2, list):
            return obj1 + obj2
        else:
            raise Exception("JSON birleştirme hatası: Uyumsuz tipler")
            
    def debug_inspect(self, obj, max_depth=5):
        """Nesne içeriğini detaylı incele ve raporla"""
        try:
            report = []
            def inspect_recursive(obj, depth=0, path=""):
                if depth > max_depth:
                    return ["[Maksimum derinliğe ulaşıldı]"]
                    
                if isinstance(obj, dict):
                    lines = [f"{path} (Dict, {len(obj)} eleman):"]
                    for k, v in obj.items():
                        lines.extend(inspect_recursive(v, depth+1, f"{path}.{k}" if path else k))
                    return lines
                elif isinstance(obj, list):
                    lines = [f"{path} (List, {len(obj)} eleman):"]
                    for i, v in enumerate(obj):
                        lines.extend(inspect_recursive(v, depth+1, f"{path}[{i}]"))
                    return lines
                else:
                    return [f"{path}: {type(obj).__name__} = {repr(obj)}"]
                    
            report.extend(inspect_recursive(obj))
            return "\n".join(report)
        except Exception as e:
            return f"İnceleme hatası: {str(e)}"
            
    def debug_validate(self, obj, rules):
        """Nesneyi kurallara göre doğrula ve rapor oluştur"""
        try:
            report = []
            for rule in rules:
                try:
                    condition = rule.get("condition", lambda x: True)
                    message = rule.get("message", "Doğrulama hatası")
                    if not condition(obj):
                        report.append(f"HATA: {message}")
                except Exception as e:
                    report.append(f"Kural hatası: {str(e)}")
            return report if report else ["Tüm doğrulamalar başarılı"]
        except Exception as e:
            return [f"Doğrulama hatası: {str(e)}"]
            
    def debug_compare(self, obj1, obj2):
        """İki nesneyi karşılaştır ve farklılıkları raporla"""
        try:
            report = []
            def compare_recursive(obj1, obj2, path=""):
                if type(obj1) != type(obj2):
                    return [f"{path}: Tip uyuşmazlığı ({type(obj1).__name__} vs {type(obj2).__name__})"]
                    
                if isinstance(obj1, dict):
                    diffs = []
                    all_keys = set(obj1.keys()) | set(obj2.keys())
                    for key in all_keys:
                        if key not in obj1:
                            diffs.append(f"{path}.{key}: Sadece ikinci nesnede var")
                        elif key not in obj2:
                            diffs.append(f"{path}.{key}: Sadece birinci nesnede var")
                        else:
                            diffs.extend(compare_recursive(obj1[key], obj2[key], f"{path}.{key}"))
                    return diffs
                elif isinstance(obj1, list):
                    diffs = []
                    for i, (v1, v2) in enumerate(zip(obj1, obj2)):
                        diffs.extend(compare_recursive(v1, v2, f"{path}[{i}]"))
                    if len(obj1) != len(obj2):
                        diffs.append(f"{path}: Farklı uzunluklar ({len(obj1)} vs {len(obj2)})")
                    return diffs
                elif obj1 != obj2:
                    return [f"{path}: {obj1} != {obj2}"]
                return []
                
            differences = compare_recursive(obj1, obj2)
            return differences if differences else ["Nesneler aynı"]
        except Exception as e:
            return [f"Karşılaştırma hatası: {str(e)}"]
            
    def debug_log(self, message, level="INFO", to_file=None):
        """Hata ayıklama mesajı kaydet"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_msg = f"[{timestamp}] {level}: {message}"
            
            if to_file:
                with open(to_file, "a", encoding="utf-8") as f:
                    f.write(log_msg + "\n")
            else:
                print(log_msg)
        except Exception as e:
            print(f"Loglama hatası: {str(e)}")
            
    def debug_profile(self, func, *args, **kwargs):
        """Fonksiyon performansını ölç"""
        try:
            import cProfile
            import pstats
            import io
            
            pr = cProfile.Profile()
            pr.enable()
            result = func(*args, **kwargs)
            pr.disable()
            
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats()
            
            return {
                "result": result,
                "stats": s.getvalue()
            }
        except Exception as e:
            return {
                "error": f"Profilleme hatası: {str(e)}"
            }
            
    def xml_read(self, path):
        """XML dosyasını oku"""
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(path)
            return tree.getroot()
        except Exception as e:
            raise Exception(f"XML okuma hatası: {str(e)}")
            
    def xml_find(self, root, xpath):
        """XML'de XPath ile eleman bul"""
        try:
            import xml.etree.ElementTree as ET
            return root.findall(xpath)
        except Exception as e:
            raise Exception(f"XML arama hatası: {str(e)}")
            
    def xml_create(self, tag, attrib=None, text=None):
        """Yeni XML elemanı oluştur"""
        try:
            import xml.etree.ElementTree as ET
            elem = ET.Element(tag, attrib or {})
            if text:
                elem.text = text
            return elem
        except Exception as e:
            raise Exception(f"XML oluşturma hatası: {str(e)}")
            
    def xml_validate(self, xml_path, xsd_path=None, dtd_path=None):
        """XML'i XSD veya DTD ile doğrula"""
        try:
            from lxml import etree
            xml_doc = etree.parse(xml_path)
            
            if dtd_path:
                dtd = etree.DTD(open(dtd_path))
                return dtd.validate(xml_doc)
            elif xsd_path:
                xsd_doc = etree.parse(xsd_path)
                schema = etree.XMLSchema(xsd_doc)
                return schema.validate(xml_doc)
            else:
                raise Exception("XSD veya DTD yolu belirtilmeli")
        except Exception as e:
            raise Exception(f"XML doğrulama hatası: {str(e)}")
            
    def xml_transform(self, xml_path, xslt_path, output_path=None):
        """XSLT dönüşümü uygula"""
        try:
            from lxml import etree
            xml_doc = etree.parse(xml_path)
            xslt_doc = etree.parse(xslt_path)
            transform = etree.XSLT(xslt_doc)
            result = transform(xml_doc)
            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(etree.tostring(result))
            return str(result)
        except Exception as e:
            raise Exception(f"XSLT dönüşüm hatası: {str(e)}")
            
    def list_dir(self, path):
        return os.listdir(path)

    def ping(self, host):
        try:
            response = requests.get(f"http://{host}", timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def sum(self, iterable):
        return sum(iterable)

    def mean(self, iterable):
        return sum(iterable) / len(iterable) if iterable else 0

    def min(self, iterable):
        return min(iterable) if iterable else None

    def max(self, iterable):
        return max(iterable) if iterable else None

    def round(self, x, digits=0):
        return round(x, digits)

    def trim(self, s):
        return s.strip()

    def replace(self, s, old, new):
        return s.replace(old, new)

    def format(self, s, *args):
        return s.format(*args)

    def trace(self):
        return traceback.format_stack()

    def try_catch(self, block, handler):
        try:
            return block()
        except Exception as e:
            return handler(str(e))

    def sleep(self, seconds):
        time.sleep(seconds)

    def date_diff(self, date1, date2, unit="days"):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        delta = d2 - d1
        if unit == "days":
            return delta.days
        elif unit == "seconds":
            return delta.total_seconds()
        raise Exception("Gecersiz birim")

    async def run_async(self, func):
        return await asyncio.to_thread(func)

    def wait(self, tasks):
        for t in tasks:
            t.join()

    def merge(self, col1, col2):
        if isinstance(col1, list) and isinstance(col2, list):
            return col1 + col2
        elif isinstance(col1, dict) and isinstance(col2, dict):
            return {**col1, **col2}
        raise Exception("Gecersiz veri tipi")

    def sort(self, iterable, key=None):
        return sorted(iterable, key=key)

    def memory_usage(self):
        try:
            import psutil
            process = psutil.Process()
            return process.memory_info().rss / 1024 / 1024
        except Exception:
            return 0

    def cpu_count(self):
        return multiprocessing.cpu_count()

    def type_of(self, value):
        if isinstance(value, int):
            return "INTEGER"
        elif isinstance(value, float):
            return "FLOAT"
        elif isinstance(value, str):
            return "STRING"
        elif isinstance(value, list):
            return "LIST"
        elif isinstance(value, dict):
            return "DICT"
        return "UNKNOWN"

    def is_empty(self, collection):
        return len(collection) == 0

    def len(self, obj):
        return len(obj)

    def val(self, s):
        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                raise Exception(f"Gecersiz deger: {s}")

    def str(self, value):
        return str(value)

    def listfile(self, path, pattern="*"):
        files = glob.glob(os.path.join(path, pattern))
        return [{"name": f, "metadata": {"compressed": f.endswith(".hz")}} for f in files]

    def stack(self):
        stack_id = id([])
        self.stacks[stack_id] = []
        return stack_id

    def push(self, stack_id, item):
        if stack_id in self.stacks:
            self.stacks[stack_id].append(item)
        else:
            raise Exception("Gecersiz yigin")

    def pop(self, stack_id):
        if stack_id in self.stacks and self.stacks[stack_id]:
            return self.stacks[stack_id].pop()
        raise Exception("Yigin bos veya gecersiz")

    def queue(self):
        queue_id = id([])
        self.queues[queue_id] = []
        return queue_id

    def enqueue(self, queue_id, item):
        if queue_id in self.queues:
            self.queues[queue_id].append(item)
        else:
            raise Exception("Gecersiz kuyruk")

    def dequeue(self, queue_id):
        if queue_id in self.queues and self.queues[queue_id]:
            return self.queues[queue_id].pop(0)
        raise Exception("Kuyruk bos veya gecersiz")

    def map(self, func, iterable):
        return [func(x) for x in iterable]

    def filter(self, func, iterable):
        return [x for x in iterable if func(x)]

    def reduce(self, func, iterable, initial):
        result = initial
        for x in iterable:
            result = func(result, x)
        return result

    def load_hz(self, path):
        with open(path, "r", encoding=self.default_encoding) as f:
            return f.read()

    def open(self, file_path, mode, encoding="utf-8"):
        return open(file_path, mode, encoding=encoding)

    def load_dll(self, dll_name):
        try:
            return ctypes.WinDLL(dll_name)
        except Exception as e:
            logging.error(f"DLL yukleme hatasi: {dll_name}, {e}")
            raise Exception(f"DLL yukleme hatasi: {e}")

    def load_api(self, url):
        return SimpleNamespace(
            ask=lambda query: requests.post(url, json={"query": query}).json().get("response", "")
        )

    def version(self, lib_name):
        return self.metadata.get(lib_name, {}).get("version", "unknown")

    def require_version(self, lib_name, required_version):
        current = self.version(lib_name)
        if not self._check_version(current, required_version):
            raise Exception(f"Versiyon uyumsuzlugu: {lib_name} {required_version} gerekli, {current} bulundu")

    def _check_version(self, current, required):
        return version.parse(current) >= version.parse(required)

    def set_encoding(self, encoding):
        if encoding in self.supported_encodings:
            self.default_encoding = encoding
        else:
            raise Exception(f"Desteklenmeyen encoding: {encoding}")

    async def async_wait(self, seconds):
        await asyncio.sleep(seconds)

    def pdf_read_text(self, file_path):
        if not os.path.exists(file_path):
            return "PDF bulunamadi"
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text

    def pdf_extract_tables(self, file_path):
        if not os.path.exists(file_path):
            return []
        tables = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                tables.extend(page_tables)
        return tables

    def map(self, func, iterable):
        return [func(x) for x in iterable]

    def filter(self, func, iterable):
        return [x for x in iterable if func(x)]

    def reduce(self, func, iterable, initial):
        result = initial
        for x in iterable:
            result = func(result, x)
        return result

    async def async_wait(self, seconds):
        await asyncio.sleep(seconds)

    def load_hz(self, path):
        with open(path, "r", encoding=self.default_encoding) as f:
            return f.read()

    def open(self, file_path, mode, encoding="utf-8"):
        return open(file_path, mode, encoding=encoding)

    def load_dll(self, dll_name):
        try:
            return ctypes.WinDLL(dll_name)
        except Exception as e:
            logging.error(f"DLL yukleme hatasi: {dll_name}, {e}")
            raise Exception(f"DLL yukleme hatasi: {e}")

    def load_api(self, url):
        return SimpleNamespace(
            ask=lambda query: requests.post(url, json={"query": query}).json().get("response", "")
        )

    def version(self, lib_name):
        return self.metadata.get(lib_name, {}).get("version", "unknown")

    def require_version(self, lib_name, required_version):
        current = self.version(lib_name)
        if not self._check_version(current, required_version):
            raise Exception(f"Versiyon uyumsuzlugu: {lib_name} {required_version} gerekli, {current} bulundu")

    def _check_version(self, current, required):
        try:
            from packaging import version as pkg_version
            return pkg_version.parse(current) >= pkg_version.parse(required)
        except ImportError:
            # Fallback icin basit string karsilastirmasi
            return current >= required

    def set_encoding(self, encoding):
        if encoding in self.supported_encodings:
            self.default_encoding = encoding
        else:
            raise Exception(f"Desteklenmeyen encoding: {encoding}")

    def web_get(self, url):
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            return f"Hata: {e}"

# Interpreter Cekirdegi
from pdsx_command_handlers import PDSXCommandHandlers

class pdsXv11(PDSXCommandHandlers):
    def __init__(self):
        # Global imports - Sanal ortamda calistirildiginda kullanilabilir olacak
        global requests, ctypes, threading, psutil, multiprocessing, np, pd, stats, pdfplumber
        global ABC, abstractmethod, defaultdict, sqlite3, ast, re, struct, asyncio
        global namedtuple, datetime, random, math, shutil, glob, socket
        
        self.global_vars = {}
        self.shared_vars = defaultdict(list)
        self.local_scopes = [{}]
        self.types = {}
        self.classes = {}
        self.functions = {}
        self.subs = {}
        self.labels = {}
        
        # Komut ve fonksiyon tablolari
        self.command_table = {
            # Program akis kontrolleri
            'IF': {'syntax': 'IF <condition> THEN <command> [ELSE <command>]', 'description': 'Kosullu dallanma'},
            'GOTO': {'syntax': 'GOTO <label>', 'description': 'Etiketli satira dallanma'},
            'GOSUB': {'syntax': 'GOSUB <label>', 'description': 'Alt program cagrisi'},
            'RETURN': {'syntax': 'RETURN', 'description': 'Alt programdan donus'},
            'FOR': {'syntax': 'FOR <var> = <start> TO <end> [STEP <step>]', 'description': 'For dongusu'},
            'NEXT': {'syntax': 'NEXT', 'description': 'For dongusu sonu'},
            'WHILE': {'syntax': 'WHILE <condition>', 'description': 'While dongusu'},
            'WEND': {'syntax': 'WEND', 'description': 'While dongusu sonu'},
            'DO': {'syntax': 'DO [WHILE/UNTIL <condition>]', 'description': 'Do dongusu'},
            'LOOP': {'syntax': 'LOOP', 'description': 'Do dongusu sonu'},
            
            # OOP Komutlari
            'CLASS': {'syntax': 'CLASS <name> [EXTENDS <parent>]', 'description': 'Sinif tanimi'},
            'END CLASS': {'syntax': 'END CLASS', 'description': 'Sinif tanimi sonu'},
            'ABSTRACT CLASS': {'syntax': 'ABSTRACT CLASS <name> [EXTENDS <parent>]', 'description': 'Soyut sinif tanimi'},
            'INTERFACE': {'syntax': 'INTERFACE <name>', 'description': 'Arayuz tanimi'},
            'END INTERFACE': {'syntax': 'END INTERFACE', 'description': 'Arayuz tanimi sonu'},
            'IMPLEMENTS': {'syntax': 'IMPLEMENTS <interface>', 'description': 'Arayuz implementasyonu'},
            
            # Erisim belirlecleri
            'PRIVATE': {'syntax': 'PRIVATE <name>', 'description': 'Özel erisim'},
            'PUBLIC': {'syntax': 'PUBLIC <name>', 'description': 'Genel erisim'},
            'PROTECTED': {'syntax': 'PROTECTED <name>', 'description': 'Korunumlu erisim'},
            'STATIC': {'syntax': 'STATIC <name>', 'description': 'Statik degisken/metod'},
            'SHARED': {'syntax': 'SHARED <name>', 'description': 'Paylasimli degisken'},
            'FINAL': {'syntax': 'FINAL <name>', 'description': 'Son hali (override edilemez)'},
            'CONST': {'syntax': 'CONST <name>', 'description': 'Sabit tanimlama'},
            
            # Modul/Library komutlari
            'LIBRARY': {'syntax': 'LIBRARY <name>', 'description': 'Kutuphane tanimi'},
            'END LIBRARY': {'syntax': 'END LIBRARY', 'description': 'Kutuphane tanimi sonu'},
            'NAMESPACE': {'syntax': 'NAMESPACE <name>', 'description': 'İsim uzayi tanimi'},
            'END NAMESPACE': {'syntax': 'END NAMESPACE', 'description': 'İsim uzayi tanimi sonu'},
            'IMPORT': {'syntax': 'IMPORT <module> [AS <alias>]', 'description': 'Modul/kutuphane import'},
            'USING': {'syntax': 'USING <namespace>', 'description': 'İsim uzayi kullanimi'},
            
            # Hata yonetimi
            'TRY': {'syntax': 'TRY', 'description': 'Hata yakalama blogu'},
            'CATCH': {'syntax': 'CATCH <error> [AS <var>]', 'description': 'Hata yakalama'},
            'FINALLY': {'syntax': 'FINALLY', 'description': 'Her durumda calisacak blok'},
            'END TRY': {'syntax': 'END TRY', 'description': 'Hata yakalama sonu'},
            'THROW': {'syntax': 'THROW <error>', 'description': 'Hata firlatma'},
            
            # I/O ve Sistem
            'PRINT': {'syntax': 'PRINT <expr>', 'description': 'Ekrana yazma'},
            'INPUT': {'syntax': 'INPUT "<prompt>", <var>', 'description': 'Kullanici girisi alma'},
            'OPEN': {'syntax': 'OPEN <file> FOR <mode>', 'description': 'Dosya acma'},
            'CLOSE': {'syntax': 'CLOSE <file>', 'description': 'Dosya kapatma'},
            'CALL': {'syntax': 'CALL <sub/dll/api>', 'description': 'Alt program/DLL/API cagrisi'},
            'SHELL': {'syntax': 'SHELL <command>', 'description': 'Sistem komutu calistirma'},
            
            # Veri yapilari
            'DIM': {'syntax': 'DIM <var> [AS <type>]', 'description': 'Degisken tanimlama'},
            'TYPE': {'syntax': 'TYPE <name>', 'description': 'Ozel tip tanimi'},
            'END TYPE': {'syntax': 'END TYPE', 'description': 'Ozel tip tanimi sonu'},
            'ENUM': {'syntax': 'ENUM <name>', 'description': 'Numaralandirma tanimi'},
            'END ENUM': {'syntax': 'END ENUM', 'description': 'Numaralandirma sonu'},
            'STRUCT': {'syntax': 'STRUCT <name>', 'description': 'Yapi tanimi'},
            'END STRUCT': {'syntax': 'END STRUCT', 'description': 'Yapi tanimi sonu'},
            
            # Veritabani
            'DATABASE': {'syntax': 'DATABASE <name>', 'description': 'Veritabani baglantisi'},
            'QUERY': {'syntax': 'QUERY <sql>', 'description': 'SQL sorgusu'},
            'EXECUTE': {'syntax': 'EXECUTE <query>', 'description': 'Sorgu calistirma'},
            'COMMIT': {'syntax': 'COMMIT', 'description': 'İslem onaylama'},
            'ROLLBACK': {'syntax': 'ROLLBACK', 'description': 'İslem geri alma'},
            
            # Network/Web
            'HTTP GET': {'syntax': 'HTTP GET <url> [TO <var>]', 'description': 'HTTP GET istegi'},
            'HTTP POST': {'syntax': 'HTTP POST <url> <data>', 'description': 'HTTP POST istegi'},
            'DOWNLOAD': {'syntax': 'DOWNLOAD <url> TO <file>', 'description': 'Dosya indirme'},
            'UPLOAD': {'syntax': 'UPLOAD <file> TO <url>', 'description': 'Dosya yukleme'},
            'SOCKET': {'syntax': 'SOCKET <host> <port>', 'description': 'Soket baglantisi'},
            
            # GUI/Event
            'WINDOW': {'syntax': 'WINDOW <name>', 'description': 'Pencere olusturma'},
            'BUTTON': {'syntax': 'BUTTON <name> "<text>"', 'description': 'Dugme olusturma'},
            'TEXTBOX': {'syntax': 'TEXTBOX <name>', 'description': 'Metin kutusu'},
            'ON EVENT': {'syntax': 'ON <event> <handler>', 'description': 'Olay isleyici'},
            
            # Threading/Process
            'THREAD': {'syntax': 'THREAD <name> <sub>', 'description': 'İs parcacigi olusturma'},
            'LOCK': {'syntax': 'LOCK <resource>', 'description': 'Kaynak kilitleme'},
            'UNLOCK': {'syntax': 'UNLOCK <resource>', 'description': 'Kilit acma'},
            'PROCESS': {'syntax': 'PROCESS <command>', 'description': 'İslem baslatma'},
            
            # Debug/Test
            'DEBUG': {'syntax': 'DEBUG ON/OFF', 'description': 'Hata ayiklama modu'},
            'TRACE': {'syntax': 'TRACE ON/OFF', 'description': 'İzleme modu'},
            'ASSERT': {'syntax': 'ASSERT <condition>', 'description': 'Kosul dogrulama'},
            'TEST': {'syntax': 'TEST <name>', 'description': 'Test tanimi'},
            'END TEST': {'syntax': 'END TEST', 'description': 'Test sonu'},
            
            # Memory/Performance 
            'GC': {'syntax': 'GC', 'description': 'Cop toplama'},
            'DISPOSE': {'syntax': 'DISPOSE <var>', 'description': 'Bellek temizleme'},
            'PROFILE': {'syntax': 'PROFILE <code>', 'description': 'Performans olcumu'},
            'MEMORY': {'syntax': 'MEMORY', 'description': 'Bellek kullanimi'},
            
            # AI/ML
            'LEARN': {'syntax': 'LEARN FROM <data>', 'description': 'Makine ogrenimi'},
            'PREDICT': {'syntax': 'PREDICT <input>', 'description': 'Tahmin yapma'},
            'TRAIN': {'syntax': 'TRAIN <model>', 'description': 'Model egitimi'},
            'NEURAL': {'syntax': 'NEURAL <topology>', 'description': 'Sinir agi tanimi'}
        }
        
        # Operator tablosu
        self.operator_table = {
            # Aritmetik operatorler
            '+': {'type': 'arithmetic', 'description': 'Toplama'},
            '-': {'type': 'arithmetic', 'description': 'Cikarma'},
            '*': {'type': 'arithmetic', 'description': 'Carpma'},
            '/': {'type': 'arithmetic', 'description': 'Bolme'},
            '^': {'type': 'arithmetic', 'description': 'Us alma'},
            'MOD': {'type': 'arithmetic', 'description': 'Mod alma'},
            'DIV': {'type': 'arithmetic', 'description': 'Tam bolme'},
            
            # Mantiksal operatorler
            'AND': {'type': 'logical', 'description': 'Mantiksal VE'},
            'OR': {'type': 'logical', 'description': 'Mantiksal VEYA'},
            'NOT': {'type': 'logical', 'description': 'Mantiksal DEGIL'},
            'XOR': {'type': 'logical', 'description': 'Ozel VEYA'},
            
            # Karsilastirma operatorleri
            '=': {'type': 'comparison', 'description': 'Esitlik'},
            '<>': {'type': 'comparison', 'description': 'Esit degil'},
            '<': {'type': 'comparison', 'description': 'Kucuktur'},
            '>': {'type': 'comparison', 'description': 'Buyuktur'},
            '<=': {'type': 'comparison', 'description': 'Kucuk esit'},
            '>=': {'type': 'comparison', 'description': 'Buyuk esit'},
            'IS': {'type': 'comparison', 'description': 'Tip kontrolu'},
            'LIKE': {'type': 'comparison', 'description': 'Pattern esleme'},
            
            # Bit operatorleri
            'BAND': {'type': 'bitwise', 'description': 'Bit VE'},
            'BOR': {'type': 'bitwise', 'description': 'Bit VEYA'},
            'BXOR': {'type': 'bitwise', 'description': 'Bit XOR'},
            'BNOT': {'type': 'bitwise', 'description': 'Bit DEGIL'},
            'SHL': {'type': 'bitwise', 'description': 'Sola kaydir'},
            'SHR': {'type': 'bitwise', 'description': 'Saga kaydir'},
            
            # Dizi operatorleri
            '()': {'type': 'array', 'description': 'Dizi erisim'},
            '+': {'type': 'array', 'description': 'Dizi birlestirme'},
            'IN': {'type': 'array', 'description': 'Eleman kontrolu'},
            
            # String operatorleri
            '&': {'type': 'string', 'description': 'String birlestirme'},
            '+': {'type': 'string', 'description': 'String toplama'},
            '*': {'type': 'string', 'description': 'String tekrar'},
            
            # Nesne operatorleri
            '.': {'type': 'object', 'description': 'Uye erisim'},
            'NEW': {'type': 'object', 'description': 'Nesne olusturma'},
            'DELETE': {'type': 'object', 'description': 'Nesne silme'},
            'INSTANCEOF': {'type': 'object', 'description': 'Tip kontrolu'}
        }
        
        # Genisletilmis tip tablosu
        self.type_table = {
            # Temel tipler
            'INTEGER': int,
            'LONG': int,
            'FLOAT': float,
            'DOUBLE': float,
            'STRING': str,
            'BOOLEAN': bool,
            'DATE': datetime.date,
            'TIME': datetime.time,
            'DATETIME': datetime,
            'BYTE': int,
            'CHAR': str,
            'OBJECT': object,
            
            # Veri yapilari
            'ARRAY': list,
            'LIST': list,
            'DICTIONARY': dict,
            'SET': set,
            'TUPLE': tuple,
            'STACK': list,
            'QUEUE': collections.deque,
            'LINKEDLIST': list,
            'HASHMAP': dict,
            'TREE': dict,
            'GRAPH': dict,
            
            # Veri analizi
            'DATAFRAME': pd.DataFrame if pd is not None else dict,
            'SERIES': pd.Series if pd is not None else list,
            'MATRIX': np.ndarray if np is not None else list,
            'VECTOR': np.ndarray if np is not None else list,
            
            # Dosya/IO tipleri
            'FILE': io.IOBase,
            'STREAM': io.IOBase,
            'BINARY': bytes,
            'SOCKET': socket.socket,
            'PROCESS': subprocess.Popen,
            
            # GUI/Event tipleri
            'WINDOW': object,
            'BUTTON': object,
            'TEXTBOX': object,
            'EVENT': object,
            'TIMER': object,
            
            # Threading/Process
            'THREAD': threading.Thread,
            'LOCK': threading.Lock,
            'SEMAPHORE': threading.Semaphore,
            'QUEUE': queue.Queue,
            
            # Database
            'CONNECTION': object,
            'CURSOR': object,
            'RECORDSET': object,
            
            # Web/Network
            'URL': str,
            'HTTP': object,
            'JSON': dict,
            'XML': object,
            
            # AI/ML
            'MODEL': object,
            'TENSOR': np.ndarray if np is not None else list,
            'NEURAL': object
        }
        
        # Veri yapilari tablosu
        self.data_structure_table = {
            # Listeler ve Diziler
            'LIST': {'operations': ['ADD', 'REMOVE', 'INSERT', 'CLEAR', 'SORT', 'REVERSE']},
            'ARRAY': {'operations': ['RESIZE', 'FILL', 'COPY', 'SLICE']},
            'TUPLE': {'operations': ['PACK', 'UNPACK']},
            
            # Koleksiyonlar
            'SET': {'operations': ['ADD', 'REMOVE', 'UNION', 'INTERSECT', 'DIFFERENCE']},
            'DICTIONARY': {'operations': ['PUT', 'GET', 'REMOVE', 'CLEAR', 'KEYS', 'VALUES']},
            'QUEUE': {'operations': ['ENQUEUE', 'DEQUEUE', 'PEEK', 'CLEAR']},
            'STACK': {'operations': ['PUSH', 'POP', 'PEEK', 'CLEAR']},
            
            # Agac ve Graf
            'TREE': {'operations': ['INSERT', 'DELETE', 'SEARCH', 'TRAVERSE']},
            'GRAPH': {'operations': ['ADD_NODE', 'ADD_EDGE', 'REMOVE_NODE', 'REMOVE_EDGE']},
            
            # Veri analizi
            'DATAFRAME': {'operations': ['LOAD', 'SAVE', 'FILTER', 'SORT', 'GROUP', 'JOIN']},
            'SERIES': {'operations': ['GET', 'SET', 'FILTER', 'SORT', 'PLOT']},
            'MATRIX': {'operations': ['ADD', 'SUBTRACT', 'MULTIPLY', 'INVERSE', 'TRANSPOSE']},
            
            # Dosya/IO
            'FILE': {'operations': ['OPEN', 'CLOSE', 'READ', 'WRITE', 'SEEK']},
            'STREAM': {'operations': ['READ', 'WRITE', 'FLUSH', 'CLOSE']},
            'SOCKET': {'operations': ['CONNECT', 'SEND', 'RECEIVE', 'CLOSE']},
            
            # GUI/Event
            'WINDOW': {'operations': ['SHOW', 'HIDE', 'MOVE', 'RESIZE', 'CLOSE']},
            'CONTROL': {'operations': ['ENABLE', 'DISABLE', 'FOCUS', 'REFRESH']},
            'EVENT': {'operations': ['BIND', 'UNBIND', 'TRIGGER', 'WAIT']},
            
            # Threading/Process
            'THREAD': {'operations': ['START', 'STOP', 'PAUSE', 'RESUME', 'JOIN']},
            'PROCESS': {'operations': ['START', 'STOP', 'KILL', 'WAIT']},
            'LOCK': {'operations': ['ACQUIRE', 'RELEASE', 'TRY_ACQUIRE']},
            
            # Database
            'CONNECTION': {'operations': ['OPEN', 'CLOSE', 'COMMIT', 'ROLLBACK']},
            'RECORDSET': {'operations': ['FIRST', 'NEXT', 'PREVIOUS', 'LAST', 'UPDATE']},
            
            # AI/ML
            'MODEL': {'operations': ['TRAIN', 'PREDICT', 'SAVE', 'LOAD', 'EVALUATE']},
            'NEURAL': {'operations': ['ADD_LAYER', 'COMPILE', 'FIT', 'PREDICT']}
        }
        
        # Access modifiers tablosu
        self.access_modifiers = {
            'PUBLIC': {'scope': 'all', 'description': 'Her yerden erisilebilir'},
            'PRIVATE': {'scope': 'class', 'description': 'Sadece sinif ici erisim'},
            'PROTECTED': {'scope': 'inheritance', 'description': 'Sadece kalitim yoluyla erisim'},
            'STATIC': {'scope': 'class_level', 'description': 'Sinif seviyesinde erisim'},
            'FINAL': {'scope': 'constant', 'description': 'Degistirilemez'},
            'ABSTRACT': {'scope': 'inheritance', 'description': 'Soyut, implemente edilmeli'},
            'SYNCHRONIZED': {'scope': 'thread', 'description': 'Thread-safe erisim'},
            'VOLATILE': {'scope': 'memory', 'description': 'Thread-safe bellek erisimi'},
            'TRANSIENT': {'scope': 'serialization', 'description': 'Serializasyonda yoksayilir'},
            'NATIVE': {'scope': 'system', 'description': 'Sistem seviyesi implementasyon'}
        }
        
        # User-defined fonksiyon ve alt program destegi
        self.user_functions = {}  # DEF FN ve FUNCTION...END FUNCTION tanimlari
        self.user_subs = {}       # SUB...END SUB tanimlari
        self.inline_functions = {}  # FUNC...END FUNC (lambda tarzi)
        self.function_definitions = {}  # Fonksiyon kodlarini sakla
        
        # Function execution stack - her fonksiyon icin ayri context
        self.execution_stack = []  # Her eleman: {'type': 'function'/'sub', 'name': 'func_name', 'pc': 0, 'loop_stack': [], 'body': []}
        self.function_counter = 0  # Her fonksiyon cagrisi icin unique ID
        
        self.program = []
        self.program_counter = 0
        self.call_stack = []
        self.running = False
        self.db_connections = {}
        self.file_handles = {}
        self.error_handler = None
        self.gosub_handler = None
        self.debug_mode = False
        self.trace_mode = False
        self.loop_stack = []
        self.select_stack = []
        self.if_stack = []
        self.data_list = []
        self.data_pointer = 0
        self.transaction_active = {}
        self.modules = {"core": {"functions": {}, "classes": {}, "program": []}}
        self.current_module = "main"
        self.repl_mode = False
        self.language = "en"
        self.translations = self.load_translations("lang.json")
        self.memory_manager = MemoryManager()
        
        # REPL ozellikleri
        self.repl_history = []
        self.repl_line_number = 0
        self.repl_buffer = []
        self.repl_running = False
        
        # Klavye girisi icin ozel imports
        try:
            if os.name == 'nt':  # Windows
                import msvcrt
                self.msvcrt = msvcrt
            else:  # Linux/Mac icin termios
                import termios
                import tty
                self.termios = termios
                self.tty = tty
        except ImportError:
            self.msvcrt = None
            self.termios = None
            self.tty = None
        self.memory_pool = {}
        self.next_address = 1000
        self.expr_cache = {}
        self.variable_cache = {}
        self.bytecode = []
        self.core = LibXCore(self)
        self.async_tasks = []
        self.performance_metrics = {"start_time": time.time(), "memory_usage": 0}
        self.supported_encodings = [
            "utf-8", "cp1254", "iso-8859-9", "ascii", "utf-16", "utf-32",
            "cp1252", "iso-8859-1", "windows-1250", "latin-9",
            "cp932", "gb2312", "gbk", "euc-kr", "cp1251", "iso-8859-5",
            "cp1256", "iso-8859-6", "cp874", "iso-8859-7", "cp1257", "iso-8859-8"
        ]

        self.type_table = {
            "STRING": str, "INTEGER": int, "LONG": int, "SINGLE": float, "DOUBLE": float,
            "BYTE": int, "SHORT": int, "UNSIGNED INTEGER": int, "CHAR": str,
            "LIST": list, "DICT": dict, "SET": set, "TUPLE": tuple,
            "ARRAY": list, "DATAFRAME": dict, "POINTER": None,  # Fallback values
            "STRUCT": dict, "UNION": None, "ENUM": dict, "VOID": None, "BITFIELD": int
        }

        self.function_table = {
            "MID$": lambda s, start, length: s[int(start)-1:int(start)-1+int(length)],
            "LEN": len, "RND": random.random, "ABS": abs, "INT": int,
            "LEFT$": lambda s, n: s[:int(n)], "RIGHT$": lambda s, n: s[-int(n):] if int(n) > 0 else "",
            "LTRIM$": lambda s: s.lstrip(), "RTRIM$": lambda s: s.rstrip(),
            "STRING$": lambda n, c: c * int(n), "SPACE$": lambda n: " " * int(n),
            "INSTR": lambda start, s, sub: s.find(sub, int(start)-1) + 1,
            "UCASE$": lambda s: s.upper(), "LCASE$": lambda s: s.lower(),
            "STR$": lambda n: str(n), 
            "SQR": math.sqrt if np is None else np.sqrt, 
            "SIN": math.sin if np is None else np.sin,
            "COS": math.cos if np is None else np.cos, 
            "TAN": math.tan if np is None else np.tan, 
            "LOG": math.log if np is None else np.log, 
            "EXP": math.exp if np is None else np.exp,
            "ATN": math.atan if np is None else np.arctan, "FIX": lambda x: int(float(x)), "ROUND": lambda x, n=0: round(float(x), int(n) if n != 0 else 0),
            "SGN": lambda x: -1 if x < 0 else (1 if x > 0 else 0),
            "MOD": lambda x, y: x % y, "MIN": lambda *args: min(args),
            "MAX": lambda *args: max(args), "TIMER": lambda: time.time(),
            "DATE$": lambda: time.strftime("%m-%d-%Y"),
            "TIME$": lambda: time.strftime("%H:%M:%S"),
            "INKEY$": lambda: input()[:1], "ENVIRON$": lambda var: os.environ.get(var, ""),
            "COMMAND$": lambda: " ".join(sys.argv[1:]),
            "CSRLIN": lambda: 1, "POS": lambda x: 1, "VAL": lambda s: float(s) if str(s).replace(".", "").replace("-", "").isdigit() else 0,
            "ASC": lambda c: ord(str(c)[0]) if c else 0,
            
            # Klavye giris fonksiyonlari
            "KEY": self.check_key_state,
            "GETKEY": self.get_key_wait,
            
            # REPL ve dosya islemleri
            "SAVE": self.save_program,
            "LOAD": self.load_program,
            "RUN": self.run_program,
            # İstatistiksel Fonksiyonlar - guvenli import
        }
        
        # NumPy fonksiyonlarini guvenli sekilde ekle
        if np is not None:
            numpy_functions = {
                "MEAN": np.mean, "MEDIAN": np.median, "STD": np.std, "VAR": np.var, 
                "PERCENTILE": np.percentile, "QUANTILE": np.quantile,
                "CORR": lambda x, y: np.corrcoef(x, y)[0, 1], "COV": np.cov,
                "CONCATENATE": np.concatenate, "STACK": np.stack, "VSTACK": np.vstack,
                "HSTACK": np.hstack, "DOT": np.dot, "CROSS": np.cross,
            }
            self.function_table.update(numpy_functions)
        else:
            # NumPy olmadan temel alternatifler
            basic_functions = {
                "MEAN": lambda x: sum(x) / len(x), 
                "MEDIAN": lambda x: sorted(x)[len(x)//2], 
                "STD": lambda x: (sum((i - sum(x)/len(x))**2 for i in x) / len(x))**0.5,
                "VAR": lambda x: sum((i - sum(x)/len(x))**2 for i in x) / len(x),
            }
            self.function_table.update(basic_functions)
        
        # SciPy stats fonksiyonlarini guvenli sekilde ekle
        try:
            import scipy.stats as stats
            stats_functions = {
                "MODE": lambda x: stats.mode(x)[0][0],
                "TTEST": lambda sample1, sample2: stats.ttest_ind(sample1, sample2),
                "CHISQUARE": lambda observed: stats.chisquare(observed),
                "ANOVA": lambda *groups: stats.f_oneway(*groups),
                "REGRESS": lambda x, y: stats.linregress(x, y),
            }
            self.function_table.update(stats_functions)
        except ImportError:
            pass
        
        # Pandas fonksiyonlarini guvenli sekilde ekle
        try:
            import pandas as pd
            pandas_functions = {
                "DESCRIBE": lambda df: df.describe(), 
                "GROUPBY": lambda df, col: df.groupby(col),
                "FILTER": lambda df, cond: df.query(cond),
                "SORT": lambda df, col: df.sort_values(col),
                "HEAD": lambda df, n=5: df.head(n), 
                "TAIL": lambda df, n=5: df.tail(n),
                "MERGE": lambda df1, df2, on: pd.merge(df1, df2, on=on),
            }
            self.function_table.update(pandas_functions)
        except ImportError:
            pass
        
        # Temel fonksiyonlari ekle
        basic_extra = {
            "WHERE": self.core.filter,  # Eski FILTER fonksiyonu artik WHERE olarak adlandirildi
        }
        self.function_table.update(basic_extra)
        
        # NumPy linear algebra ve array fonksiyonlari
        if np is not None:
            try:
                linalg_functions = {
                    "NORM": np.linalg.norm, "INV": np.linalg.inv, "SOLVE": np.linalg.solve,
                    "LINSPACE": np.linspace, "ARANGE": np.arange, "ZEROS": np.zeros,
                    "ONES": np.ones, "FULL": np.full, "EYE": np.eye, "DIAG": np.diag,
                    "RESHAPE": np.reshape, "TRANSPOSE": np.transpose, "FLIP": np.flip,
                    "ROLL": np.roll,
                }
                self.function_table.update(linalg_functions)
            except AttributeError:
                pass
        
        # Pandas functions - advanced
        try:
            import pandas as pd
            pandas_advanced = {
                "PIVOT_TABLE": lambda df, **kwargs: df.pivot_table(**kwargs),
                "CROSSTAB": pd.crosstab, 
                "FILLNA": lambda df, value: df.fillna(value),
                "DROPNA": lambda df, **kwargs: df.dropna(**kwargs),
                "ASTYPE": lambda df, dtype: df.astype(dtype),
                "MELT": lambda df, **kwargs: pd.melt(df, **kwargs),
                "CUT": pd.cut, "QCUT": pd.qcut, "TO_DATETIME": pd.to_datetime,
                "RESAMPLE": lambda df, rule, **kwargs: df.resample(rule, **kwargs),
                "ROLLING": lambda df, window: df.rolling(window),
                "EWMA": lambda df, **kwargs: df.ewm(**kwargs).mean(),
                "SHIFT": lambda df, periods: df.shift(periods),
                "DIFF": lambda df, periods=1: df.diff(periods),
                "PCT_CHANGE": lambda df: df.pct_change(),
            }
            self.function_table.update(pandas_advanced)
        except ImportError:
            pass
        
        # File functions
        file_functions = {
            # Dosya İslemleri
            "EOF": lambda n: self.file_handles[n].eof() if hasattr(self.file_handles[n], 'eof') else False,
            "LOC": lambda n: self.file_handles[n].tell(),
            "LOF": lambda n: os.path.getsize(self.file_handles[n].name),
            "FREEFILE": lambda: min(set(range(1, 100)) - set(self.file_handles.keys())),
            "CHR$": lambda n: chr(int(n)),
            "INPUT$": lambda n, f: self.file_handles[f].read(n),
            "MKI$": lambda n: struct.pack("i", n).decode('latin1'),
            "MKS$": lambda n: struct.pack("f", n).decode('latin1'),
            "MKD$": lambda n: struct.pack("d", n).decode('latin1'),
            "DIR$": lambda path: os.listdir(path),
            "ISDIR": lambda path: os.path.isdir(path),
            
            # String Array İşlemleri
            "STRARRAY": lambda size, default="": ["" for _ in range(size)] if isinstance(size, int) else [default] * len(size),
            "STRGET": lambda arr, index: arr[index] if 0 <= index < len(arr) else "",
            "STRSET": lambda arr, index, value: self._strset(arr, index, value),
            "STRLEN": lambda arr: [len(s) for s in arr] if isinstance(arr, list) else len(arr),
            "STRCAT": lambda arr1, arr2: arr1 + arr2 if isinstance(arr1, list) and isinstance(arr2, list) else str(arr1) + str(arr2),
            "STRSPLIT": lambda s, delimiter=",": s.split(delimiter),
            "STRJOIN": lambda arr, delimiter=",": delimiter.join(arr) if isinstance(arr, list) else str(arr),
            "STRFIND": lambda arr, substr: [i for i, s in enumerate(arr) if substr in s] if isinstance(arr, list) else arr.find(substr),
            "STRREPLACE": lambda arr, old, new: [s.replace(old, new) for s in arr] if isinstance(arr, list) else arr.replace(old, new),
            "STRCOMPARE": lambda arr1, arr2: [a == b for a, b in zip(arr1, arr2)] if isinstance(arr1, list) and isinstance(arr2, list) else arr1 == arr2,
            "STRTRIM": lambda arr: [s.strip() for s in arr] if isinstance(arr, list) else arr.strip(),
            "STRPAD": lambda arr, width, char=" ": [s.ljust(width, char) for s in arr] if isinstance(arr, list) else arr.ljust(width, char),
            "STRSUBSTR": lambda arr, start, length=None: [s[start:start+length] if length else s[start:] for s in arr] if isinstance(arr, list) else (arr[start:start+length] if length else arr[start:]),
            "STRREVERSE": lambda arr: [s[::-1] for s in arr] if isinstance(arr, list) else arr[::-1],
            "STRMATCH": lambda arr, pattern: [re.match(pattern, s) is not None for s in arr] if isinstance(arr, list) else re.match(pattern, arr) is not None,
            "STRCOUNT": lambda arr, substr: [s.count(substr) for s in arr] if isinstance(arr, list) else arr.count(substr),
            "STRLOWER": lambda arr: [s.lower() for s in arr] if isinstance(arr, list) else arr.lower(),
            "STRUPPER": lambda arr: [s.upper() for s in arr] if isinstance(arr, list) else arr.upper(),
            "STRTITLE": lambda arr: [s.title() for s in arr] if isinstance(arr, list) else arr.title(),
            "STRSWAP": lambda arr, char1, char2: [s.replace(char1, char2) for s in arr] if isinstance(arr, list) else arr.replace(char1, char2),
            
            # PDF İslemleri
            "PDF_READ_TEXT": self.core.pdf_read_text,
            "PDF_EXTRACT_TABLES": self.core.pdf_extract_tables,
            # Web İslemleri
            "WEB_GET": self.core.web_get,
            # İleri Matematik Fonksiyonlari
            "SINH": math.sinh,
            "COSH": math.cosh,
            "TANH": math.tanh,
            "ASINH": math.asinh,
            "ACOSH": math.acosh,
            "ATANH": math.atanh,
            "SIND": lambda x: math.sin(math.radians(x)),
            "COSD": lambda x: math.cos(math.radians(x)),
            "TAND": lambda x: math.tan(math.radians(x)),
            "PI": math.pi,
            "E": math.e,
            "BIN": bin,
            "HEX": hex,
            "OCT": oct,
            "ADDR": lambda x: id(x),
            "SIZEOF": lambda x: self.memory_manager.sizeof(x),
            # Memory Management
            "NEW": self.memory_manager.allocate,
            "DELETE": self.memory_manager.release,
            # Async İslemler
            "ASYNC_WAIT": self.core.async_wait,
            "THREAD_COUNT": lambda: threading.active_count(),
            "CURRENT_THREAD": lambda: threading.get_ident(),
            # Fonksiyonel Programlama
            "MAP": self.core.map,
            "REDUCE": self.core.reduce
        }

        self.operator_table = {
            '++': lambda x: x + 1,
            '--': lambda x: x - 1,
            '<<': lambda x, y: x << y,
            '>>': lambda x, y: x >> y,
            '&': lambda x, y: x & y,
            '|': lambda x, y: x | y,
            '^': lambda x, y: x ^ y,
            '~': lambda x: ~x,
            'AND': lambda x, y: x and y,
            'OR': lambda x, y: x or y,
            'XOR': lambda x, y: bool(x) != bool(y),
            'NOT': lambda x: not x,
            '+=': lambda x, y: x + y,
            '-=': lambda x, y: x - y,
            '*=': lambda x, y: x * y,
            '/=': lambda x, y: x / y,
            '%=': lambda x, y: x % y,
            '&=': lambda x, y: x & y,
            '|=': lambda x, y: x | y,
            '^=': lambda x, y: x ^ y,
            '<<=': lambda x, y: x << y,
            '>>=': lambda x, y: x >> y
        }

    def load_translations(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Dil dosyasi bulunamadi. Varsayilan İngilizce kullanilacak.")
            return {"en": {"PRINT": "Print", "ERROR": "Error"}}

    def translate(self, key):
        return self.translations.get(self.language, {}).get(key, key)

    def _strset(self, arr, index, value):
        """String array helper - set value at index"""
        if isinstance(arr, list) and 0 <= index < len(arr):
            arr[index] = str(value)
        return arr

    def current_scope(self):
        return self.local_scopes[-1]

    def _initialize_nested_struct_fields(self, struct_instance, fields):
        """Nested STRUCT field'larını initialize et"""
        for field_name, field_type in fields:
            if field_type in self.types:
                # Bu bir user-defined type
                type_info = self.types[field_type]
                if type_info["kind"] == "STRUCT":
                    # Nested STRUCT oluştur
                    nested_struct = StructInstance(type_info["fields"], self.type_table)
                    self._initialize_nested_struct_fields(nested_struct, type_info["fields"])
                    struct_instance.set_field(field_name, nested_struct)
                elif type_info["kind"] == "UNION":
                    # Nested UNION oluştur
                    nested_union = UnionInstance(type_info["fields"], self.type_table)
                    struct_instance.set_field(field_name, nested_union)
            else:
                # Basic type - default değer ile initialize et
                default_value = self.type_table.get(field_type.upper(), lambda: None)()
                if default_value is not None:
                    struct_instance.set_field(field_name, default_value)

    def call_user_function(self, func_name, args_str, scope_name=None):
        """User-defined fonksiyon cagir (DEF FN ve DEF FUNCTION)"""
        if func_name not in self.user_functions:
            raise Exception(f"Tanimlanmamis fonksiyon: {func_name}")
        
        func_def = self.user_functions[func_name]
        
        # Argumanlari parse et
        args = []
        if args_str.strip():
            current_arg = ""
            paren_count = 0
            in_quotes = False
            
            for char in args_str:
                if char == '"' and (not current_arg or current_arg[-1] != '\\'):
                    in_quotes = not in_quotes
                elif char == '(' and not in_quotes:
                    paren_count += 1
                elif char == ')' and not in_quotes:
                    paren_count -= 1
                elif char == ',' and not in_quotes and paren_count == 0:
                    args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
                    current_arg = ""
                    continue
                current_arg += char
            
            if current_arg.strip():
                args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
        
        # Parametre sayisi kontrolu
        if len(args) != len(func_def['params']):
            raise Exception(f"Fonksiyon {func_name} {len(func_def['params'])} parametre bekliyor, {len(args)} verildi")
        
        # Yeni scope olustur
        old_scope = self.local_scopes.copy()
        self.local_scopes.append({})
        
        # Parametreleri local scope'a ekle
        for i, param in enumerate(func_def['params']):
            self.current_scope()[param] = args[i]
        
        try:
            if func_def['type'] == 'inline':
                # DEF FN - tek satirlik ifade
                result = self.evaluate_expression(func_def['expression'], None)  # Current scope kullan
            else:
                # DEF FUNCTION - cok satirlik - yeni execution system kullan
                result = self.execute_function_body(func_def['body'], func_name)
            return result
        finally:
            # Scope'u restore et
            self.local_scopes = old_scope

    def call_inline_function(self, func_name, args_str, scope_name=None):
        """Inline fonksiyon cagir (FUNC ... END FUNC)"""
        if func_name not in self.inline_functions:
            raise Exception(f"Tanimlanmamis inline fonksiyon: {func_name}")
        
        func_def = self.inline_functions[func_name]
        
        # Argumanlari parse et
        args = []
        if args_str.strip():
            current_arg = ""
            paren_count = 0
            in_quotes = False
            
            for char in args_str:
                if char == '"' and (not current_arg or current_arg[-1] != '\\'):
                    in_quotes = not in_quotes
                elif char == '(' and not in_quotes:
                    paren_count += 1
                elif char == ')' and not in_quotes:
                    paren_count -= 1
                elif char == ',' and not in_quotes and paren_count == 0:
                    args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
                    current_arg = ""
                    continue
                current_arg += char
            
            if current_arg.strip():
                args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
        
        # Parametre sayisi kontrolu
        if len(args) != len(func_def['params']):
            raise Exception(f"Inline fonksiyon {func_name} {len(func_def['params'])} parametre bekliyor, {len(args)} verildi")
        
        # Yeni scope olustur
        old_scope = self.local_scopes.copy()
        self.local_scopes.append({})
        
        # Parametreleri local scope'a ekle
        for i, param in enumerate(func_def['params']):
            self.current_scope()[param] = args[i]
        
        try:
            # FUNC body'sini yeni execution system ile calistir
            result = self.execute_function_body(func_def['body'], func_name)
            return result
        finally:
            # Scope'u restore et
            self.local_scopes = old_scope

    def call_user_sub(self, sub_name, args_str, scope_name=None):
        """User-defined subroutine cagir (DEF SUB ... END SUB)"""
        if sub_name not in self.user_subs:
            raise Exception(f"Tanimlanmamis subroutine: {sub_name}")
        
        sub_def = self.user_subs[sub_name]
        
        # Argumanlari parse et
        args = []
        if args_str.strip():
            current_arg = ""
            paren_count = 0
            in_quotes = False
            
            for char in args_str:
                if char == '"' and (not current_arg or current_arg[-1] != '\\'):
                    in_quotes = not in_quotes
                elif char == '(' and not in_quotes:
                    paren_count += 1
                elif char == ')' and not in_quotes:
                    paren_count -= 1
                elif char == ',' and not in_quotes and paren_count == 0:
                    args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
                    current_arg = ""
                    continue
                current_arg += char
            
            if current_arg.strip():
                args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
        
        # Parametre sayisi kontrolu
        if len(args) != len(sub_def['params']):
            raise Exception(f"Subroutine {sub_name} {len(sub_def['params'])} parametre bekliyor, {len(args)} verildi")
        
        # Yeni scope olustur
        old_scope = self.local_scopes.copy()
        self.local_scopes.append({})
        
        # Parametreleri local scope'a ekle
        for i, param in enumerate(sub_def['params']):
            self.current_scope()[param] = args[i]
        
        try:
            for line in sub_def['body']:
                if line.strip().upper() == "EXIT SUB":
                    break
                else:
                    self.execute_command(line, None)  # Current scope kullan
        finally:
            # Scope'u restore et
            self.local_scopes = old_scope

    def execute_function_body(self, body, func_name):
        """Function body'sini ayri execution context ile calistir"""
        self.function_counter += 1
        func_id = self.function_counter
        
        # Execution context olustur
        execution_context = {
            'type': 'function',
            'name': func_name,
            'id': func_id,
            'pc': 0,
            'body': body,
            'loop_stack': [],  # Bu fonksiyon icin ayri loop stack
            'running': True,
            'return_value': None
        }
        
        self.execution_stack.append(execution_context)
        
        try:
            # Function body'sini calistir
            while execution_context['running'] and execution_context['pc'] < len(body):
                line = body[execution_context['pc']].strip()
                if not line:
                    execution_context['pc'] += 1
                    continue
                    
                # RETURN kontrolu
                if line.upper().startswith("RETURN"):
                    return_expr = line[6:].strip()
                    if return_expr:
                        try:
                            # Complex expression icin ozel parsing
                            execution_context['return_value'] = self.evaluate_expression(return_expr, None)
                        except Exception as e:
                            # Fallback: daha basit parsing dene
                            try:
                                execution_context['return_value'] = self.evaluate_single_part(return_expr, None)
                            except Exception as e2:
                                raise Exception(f"RETURN expression hatasi: {return_expr} - {str(e)}")
                    else:
                        execution_context['return_value'] = None
                    execution_context['running'] = False
                    break
                
                # FOR/NEXT icin ozel islem
                line_upper = line.upper()
                if line_upper.startswith("FOR"):
                    next_pc = self.execute_for_in_function(line, execution_context)
                    if next_pc is not None:
                        execution_context['pc'] = next_pc
                    else:
                        execution_context['pc'] += 1
                elif line_upper.startswith("NEXT"):
                    next_pc = self.execute_next_in_function(line, execution_context)
                    if next_pc is not None:
                        execution_context['pc'] = next_pc
                    else:
                        execution_context['pc'] += 1
                elif line_upper.startswith("IF") and line_upper.endswith("THEN"):
                    # IF block icin ozel islem
                    next_pc = self.execute_if_in_function(line, execution_context)
                    if next_pc is not None:
                        execution_context['pc'] = next_pc
                    else:
                        execution_context['pc'] += 1
                elif line_upper == "ELSE":
                    # ELSE: END IF'e atla
                    next_pc = self.find_end_if_in_function(execution_context)
                    execution_context['pc'] = next_pc
                elif line_upper.startswith("ELSEIF"):
                    # ELSEIF: END IF'e atla
                    next_pc = self.find_end_if_in_function(execution_context)
                    execution_context['pc'] = next_pc
                elif line_upper == "END IF":
                    # END IF - sadece devam et
                    execution_context['pc'] += 1
                else:
                    # Normal komut
                    self.execute_command(line, None)
                    execution_context['pc'] += 1
                    
            return execution_context['return_value']
        finally:
            self.execution_stack.pop()

    def execute_for_in_function(self, command, execution_context):
        """Function icinde FOR komutu"""
        match = re.match(r"FOR\s+(\w+)\s*=\s*(.+?)\s+TO\s+(.+?)(?:\s+STEP\s+(.+?))?$", command, re.IGNORECASE)
        if match:
            var_name, start_expr, end_expr, step_expr = match.groups()
            start = self.evaluate_expression(start_expr, None)
            end = self.evaluate_expression(end_expr, None)
            step = self.evaluate_expression(step_expr, None) if step_expr else 1
            self.current_scope()[var_name] = start
            execution_context['loop_stack'].append({
                "start": execution_context['pc'] + 1,  # Bir sonraki satira isaret et
                "type": "FOR",
                "var": var_name,
                "end": end,
                "step": step
            })
            return None
        else:
            raise Exception("FOR komutunda sozdizimi hatasi")

    def execute_next_in_function(self, command, execution_context):
        """Function icinde NEXT komutu"""
        if execution_context['loop_stack'] and execution_context['loop_stack'][-1]["type"] == "FOR":
            loop_info = execution_context['loop_stack'][-1]
            var_name = loop_info["var"]
            current_value = self.current_scope()[var_name]
            # Degiskeni artir
            current_value += loop_info["step"]
            self.current_scope()[var_name] = current_value
            
            # Dongu devam etsin mi kontrol et
            if (loop_info["step"] > 0 and current_value <= loop_info["end"]) or \
               (loop_info["step"] < 0 and current_value >= loop_info["end"]):
                # Dongu basina don (FOR satirindan sonraki ilk satira)
                return loop_info["start"]
            else:
                # Dongu bitti
                execution_context['loop_stack'].pop()
            return None
        else:
            raise Exception("NEXT icin eslesen FOR bulunamadi")
    
    def execute_if_in_function(self, command, execution_context):
        """Function icinde IF komutu"""
        match = re.match(r"IF\s+(.+)\s+THEN\s*$", command, re.IGNORECASE)
        if match:
            condition = match.group(1)
            if self.evaluate_expression(condition, None):
                # Kosul dogru, normal devam et
                return None
            else:
                # Kosul yanlis, ELSE veya END IF'e atla
                return self.find_else_or_end_if_in_function(execution_context)
        else:
            raise Exception("IF komutunda sozdizimi hatasi")
    
    def find_else_or_end_if_in_function(self, execution_context):
        """ELSE veya END IF'i bul"""
        body = execution_context['body']
        current_pc = execution_context['pc'] + 1
        if_count = 1
        
        while current_pc < len(body) and if_count > 0:
            line = body[current_pc].strip().upper()
            
            if line.startswith("IF") and line.endswith("THEN"):
                if_count += 1
            elif line == "END IF":
                if_count -= 1
                if if_count == 0:
                    return current_pc + 1  # END IF'ten sonra
            elif line == "ELSE" and if_count == 1:
                return current_pc + 1  # ELSE'ten sonra
            elif line.startswith("ELSEIF") and if_count == 1:
                # ELSEIF kosulunu kontrol et
                elseif_match = re.match(r"ELSEIF\s+(.+)\s+THEN\s*$", line, re.IGNORECASE)
                if elseif_match:
                    elseif_condition = elseif_match.group(1)
                    if self.evaluate_expression(elseif_condition, None):
                        return current_pc + 1  # ELSEIF'ten sonra
            
            current_pc += 1
        
        # END IF bulunamadi
        raise Exception("IF icin eslesen END IF bulunamadi")
    
    def find_end_if_in_function(self, execution_context):
        """END IF'i bul"""
        body = execution_context['body']
        current_pc = execution_context['pc'] + 1
        if_count = 1
        
        while current_pc < len(body) and if_count > 0:
            line = body[current_pc].strip().upper()
            
            if line.startswith("IF") and line.endswith("THEN"):
                if_count += 1
            elif line == "END IF":
                if_count -= 1
                if if_count == 0:
                    return current_pc + 1  # END IF'ten sonra
            
            current_pc += 1
        
        # END IF bulunamadi
        raise Exception("IF icin eslesen END IF bulunamadi")

    def parse_program(self, code, module_name="main", lightweight=False, as_library=False):
        self.current_module = module_name
        self.modules[module_name] = {
            "program": [],
            "functions": {},
            "subs": {},
            "classes": {},
            "types": {},
            "labels": {}
        }
        current_sub = None
        current_function = None
        current_type = None
        current_enum = None
        current_class = None
        type_fields = {}
        class_info = {}
        enum_values = {}
        lines = code.split("\n")
        i = 0
        select_stack = []
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith("'") or line.startswith("REM"):  # Yorumlari atla
                i += 1
                continue
            line_upper = line.upper()

            # SELECT CASE bloklarinin ayristirilmasi
            if line_upper.startswith("SELECT CASE"):
                # SELECT CASE ifadesini ve CASE bloklarini topla
                select_case_header = line
                select_case_body = []
                i += 1
                while i < len(lines):
                    inner_line = lines[i].strip()
                    if inner_line.upper().startswith("END SELECT"):
                        break
                    select_case_body.append(inner_line)  # Sadece string olarak ekle
                    i += 1
                # END SELECT satirini da ekle
                select_case_body.append("END SELECT")
                self.program.append(select_case_header)
                for body_line in select_case_body:
                    self.program.append(body_line)
                i += 1
                continue
            
            # User-defined fonksiyon tanimlari
            if line_upper.startswith("DEF FN"):
                # DEF FN name(params) = expression
                match = re.match(r"DEF FN\s+(\w+)\s*\(([^)]*)\)\s*=\s*(.+)", line, re.IGNORECASE)
                if match:
                    func_name, params_str, expr = match.groups()
                    params = [p.strip() for p in params_str.split(',')] if params_str.strip() else []
                    self.user_functions[func_name] = {
                        'type': 'inline',
                        'params': params,
                        'expression': expr,
                        'module': module_name
                    }
                    i += 1
                    continue
                else:
                    raise Exception(f"DEF FN sozdizimi hatasi: {line}")
                    
            elif line_upper.startswith("DEF SUB"):
                # DEF SUB name(params) ... END SUB
                match = re.match(r"DEF SUB\s+(\w+)\s*\(([^)]*)\)", line, re.IGNORECASE)
                if match:
                    sub_name, params_str = match.groups()
                    params = [p.strip() for p in params_str.split(',')] if params_str.strip() else []
                    
                    # SUB body'sini bul
                    i += 1
                    sub_body = []
                    while i < len(lines):
                        sub_line = lines[i].strip()
                        if sub_line.upper().startswith("END SUB"):
                            break
                        sub_body.append(sub_line)
                        i += 1
                    
                    self.user_subs[sub_name] = {
                        'params': params,
                        'body': sub_body,
                        'module': module_name
                    }
                    i += 1
                    continue
                else:
                    raise Exception(f"DEF SUB sozdizimi hatasi: {line}")
                    
            elif line_upper.startswith("DEF FUNCTION"):
                # DEF FUNCTION name(params) ... END FUNCTION
                match = re.match(r"DEF FUNCTION\s+(\w+)\s*\(([^)]*)\)", line, re.IGNORECASE)
                if match:
                    func_name, params_str = match.groups()
                    params = [p.strip() for p in params_str.split(',')] if params_str.strip() else []
                    
                    # FUNCTION body'sini bul
                    i += 1
                    func_body = []
                    while i < len(lines):
                        func_line = lines[i].strip()
                        if func_line.upper().startswith("END FUNCTION"):
                            break
                        func_body.append(func_line)
                        i += 1
                    
                    self.user_functions[func_name] = {
                        'type': 'block',
                        'params': params,
                        'body': func_body,
                        'module': module_name
                    }
                    i += 1
                    continue
                else:
                    raise Exception(f"DEF FUNCTION sozdizimi hatasi: {line}")
            elif line_upper.startswith("FUNCTION ") and not line_upper.startswith("DEF FUNCTION"):
                # FUNCTION name(params) ... END FUNCTION (normal BASIC syntax)
                match = re.match(r"FUNCTION\s+(\w+)\s*\(([^)]*)\)", line, re.IGNORECASE)
                if match:
                    func_name, params_str = match.groups()
                    params = [p.strip() for p in params_str.split(',')] if params_str.strip() else []
                    
                    # FUNCTION body'sini bul
                    i += 1
                    func_body = []
                    while i < len(lines):
                        func_line = lines[i].strip()
                        if func_line.upper().startswith("END FUNCTION"):
                            break
                        func_body.append(func_line)
                        i += 1
                    
                    self.user_functions[func_name] = {
                        'type': 'block',
                        'params': params,
                        'body': func_body,
                        'module': module_name
                    }
                    i += 1
                    continue
                else:
                    raise Exception(f"FUNCTION sozdizimi hatasi: {line}")
                    
            elif line_upper.startswith("FUNC"):
                # FUNC name(params) ... END FUNC (lambda tarzi)
                match = re.match(r"FUNC\s+(\w+)\s*\(([^)]*)\)", line, re.IGNORECASE)
                if match:
                    func_name, params_str = match.groups()
                    params = [p.strip() for p in params_str.split(',')] if params_str.strip() else []
                    
                    # FUNC body'sini bul
                    i += 1
                    func_body = []
                    while i < len(lines):
                        func_line = lines[i].strip()
                        if func_line.upper().startswith("END FUNC"):
                            break
                        func_body.append(func_line)
                        i += 1
                    
                    self.inline_functions[func_name] = {
                        'params': params,
                        'body': func_body,
                        'module': module_name
                    }
                    i += 1
                    continue
                else:
                    raise Exception(f"FUNC sozdizimi hatasi: {line}")
            
            # Mevcut parsing logic devam ediyor...
            if line_upper.startswith("SUB "):
                sub_name = line[4:].split("(")[0].strip()
                self.subs[sub_name] = i + 1
                self.modules[module_name]["subs"][sub_name] = i + 1
                current_sub = sub_name
                i += 1
            elif line_upper.startswith("FUNCTION "):
                func_name = line[8:].split("(")[0].strip()
                self.functions[func_name] = i + 1
                self.modules[module_name]["functions"][func_name] = i + 1
                current_function = func_name
                i += 1
            elif line_upper.startswith("TYPE "):
                type_name = line[5:].strip()
                current_type = type_name
                type_fields[type_name] = []
                i += 1
            elif line_upper.startswith("END TYPE"):
                self.types[current_type] = {"kind": "STRUCT", "fields": type_fields[current_type]}
                self.modules[module_name]["types"][current_type] = self.types[current_type]
                current_type = None
                i += 1
            elif line_upper.startswith("UNION "):
                union_name = line[6:].strip()
                current_type = union_name
                type_fields[union_name] = []
                i += 1
            elif line_upper.startswith("END UNION"):
                self.types[current_type] = {"kind": "UNION", "fields": type_fields[current_type]}
                self.modules[module_name]["types"][current_type] = self.types[current_type]
                current_type = None
                i += 1
            elif line_upper.startswith("ENUM "):
                enum_name = line[5:].strip()
                current_enum = enum_name
                enum_values[enum_name] = {}
                i += 1
            elif line_upper.startswith("END ENUM"):
                self.types[current_enum] = {"kind": "ENUM", "values": enum_values[current_enum]}
                self.modules[module_name]["types"][current_enum] = self.types[current_enum]
                current_enum = None
                i += 1
            elif current_enum:
                # ENUM value parsing: Red = 1 or just Red
                if '=' in line:
                    enum_item, enum_value = line.split('=', 1)
                    enum_item = enum_item.strip()
                    enum_value = enum_value.strip()
                    try:
                        enum_values[current_enum][enum_item] = int(enum_value)
                    except ValueError:
                        enum_values[current_enum][enum_item] = enum_value.strip('"\'')
                else:
                    enum_item = line.strip()
                    if enum_item:
                        # Auto-increment value
                        next_val = len(enum_values[current_enum])
                        enum_values[current_enum][enum_item] = next_val
                i += 1
            elif current_type:
                match = re.match(r"(\w+)\s+AS\s+(\w+)", line, re.IGNORECASE)
                if match:
                    field_name, field_type = match.groups()
                    type_fields[current_type].append((field_name, field_type))
                else:
                    raise Exception(f"TYPE tanimi hatasi: {line}")
                i += 1
            elif line_upper.startswith("ABSTRACT CLASS "):
                match = re.match(r"ABSTRACT CLASS\s+(\w+)(?:\s+EXTENDS\s+(\w+))?", line, re.IGNORECASE)
                if match:
                    class_name, parent_name = match.groups()
                    current_class = class_name
                    class_info[class_name] = {
                        'methods': {},
                        'private_methods': {},
                        'static_vars': {},
                        'parent': parent_name,
                        'abstract': True
                    }
                    i += 1
                else:
                    raise Exception("ABSTRACT CLASS komutunda sozdizimi hatasi")
            elif line_upper.startswith("CLASS "):
                match = re.match(r"CLASS\s+(\w+)(?:\s+EXTENDS\s+(\w+))?", line, re.IGNORECASE)
                if match:
                    class_name, parent_name = match.groups()
                    current_class = class_name
                    class_info[class_name] = {
                        'methods': {},
                        'private_methods': {},
                        'static_vars': {},
                        'parent': parent_name,
                        'abstract': False
                    }
                    i += 1
                else:
                    raise Exception("CLASS komutunda sozdizimi hatasi")
            elif line_upper.startswith("END CLASS"):
                if current_class is None:
                    raise Exception("CLASS tanimi bulunamadi")
                class_name = str(current_class)
                parent_class = class_info[current_class]['parent']
                parent_methods = self.classes.get(parent_class, type('', (), {'_vars': {}})()).__dict__ if parent_class else {}
                parent_static_vars = class_info.get(parent_class, {}).get('static_vars', {})
                if class_info[current_class]['abstract']:
                    class_def = type(class_name, (ABC, self.classes.get(parent_class, object)), {
                        '_vars': {},
                        '_static_vars': {**parent_static_vars, **class_info[current_class]['static_vars']},
                        '__init__': lambda self: None,
                        'private_methods': class_info[current_class]['private_methods'],
                        **{k: abstractmethod(v) if k.startswith('_') else v for k, v in class_info[current_class]['methods'].items()},
                        **{k: v for k, v in parent_methods.items() if k not in class_info[current_class]['methods'] and k != 'private_methods'}
                    })
                else:
                    class_def = type(class_name, (self.classes.get(parent_class, object),), {
                        '_vars': {},
                        '_static_vars': {**parent_static_vars, **class_info[current_class]['static_vars']},
                        '__init__': lambda self: None,
                        'private_methods': class_info[current_class]['private_methods'],
                        **{k: v for k, v in class_info[current_class]['methods'].items()},
                        **{k: v for k, v in parent_methods.items() if k not in class_info[current_class]['methods'] and k != 'private_methods'}
                    })
                self.classes[current_class] = class_def
                self.modules[module_name]["classes"][current_class] = class_def
                current_class = None
                i += 1
            elif current_class and line_upper.startswith(("SUB ", "PRIVATE SUB ", "FUNCTION ", "PRIVATE FUNCTION ")):
                is_private = line_upper.startswith(("PRIVATE SUB ", "PRIVATE FUNCTION "))
                prefix = "PRIVATE " if is_private else ""
                method_type = "SUB" if line_upper.startswith((prefix + "SUB ")) else "FUNCTION"
                match = re.match(rf"{prefix}{method_type}\s+(\w+)(?:\(.*\))?", line, re.IGNORECASE)
                if match:
                    method_name = match.group(1)
                    method_body = []
                    j = i + 1
                    while j < len(lines) and lines[j].strip().upper() != f"END {method_type}":
                        method_body.append(lines[j].strip())
                        j += 1
                    params = re.search(r"\((.*?)\)", line, re.IGNORECASE)
                    params = params.group(1).split(",") if params else []
                    params = [p.strip() for p in params]
                    method_lambda = lambda self, *args, **kwargs: self.execute_method(method_name, method_body, params, args, scope_name=current_class)
                    if is_private:
                        class_info[current_class]['private_methods'][method_name] = method_lambda
                    else:
                        class_info[current_class]['methods'][method_name] = method_lambda
                    i = j + 1
                else:
                    raise Exception(f"{method_type} tanimi hatasi: {line}")
            elif current_class and line_upper.startswith("STATIC "):
                match = re.match(r"STATIC\s+(\w+)\s+AS\s+(\w+)", line, re.IGNORECASE)
                if match:
                    var_name, var_type = match.groups()
                    type_constructor = self.type_table.get(var_type, lambda: 0)
                    class_info[current_class]['static_vars'][var_name] = type_constructor()
                    i += 1
                else:
                    raise Exception("STATIC komutunda sozdizimi hatasi")
            elif current_class and line_upper.startswith("DIM "):
                match = re.match(r"DIM\s+(\w+)\s+AS\s+(\w+)", line, re.IGNORECASE)
                if match:
                    var_name, var_type = match.groups()
                    class_info[current_class]['methods']['__init__'] = lambda self: self._vars.update({var_name: self.type_table.get(var_type, None)()})
                    i += 1
                else:
                    raise Exception("DIM komutunda sozdizimi hatasi")
            elif line_upper == "END SUB" or line_upper == "END FUNCTION":
                current_sub = None
                current_function = None
                i += 1
            elif line_upper.startswith("LABEL "):
                label_name = line[6:].strip()
                self.labels[label_name] = i
                self.modules[module_name]["labels"][label_name] = i
                i += 1
            elif line.strip().endswith(":") and not line.strip().startswith("REM") and not line.strip().startswith("'"):
                # EtiketAdi: formatini destekle
                label_name = line.strip()[:-1]  # ":" karakterini kaldir
                # Sadece tek kelime olan ve komut olmayan etiketleri kabul et
                if " " not in label_name and label_name.upper() not in ["IF", "FOR", "WHILE", "SUB", "FUNCTION", "CLASS", "SELECT", "CASE", "TRY", "CATCH"]:
                    self.labels[label_name] = i
                    self.modules[module_name]["labels"][label_name] = i
                i += 1
            elif line_upper.startswith("DATA "):
                data_items = line[5:].split(",")
                self.data_list.extend([item.strip() for item in data_items])
                i += 1
            elif line_upper.startswith("STRUCT "):
                struct_name = line[7:].strip()
                current_type = struct_name
                type_fields[struct_name] = []
                i += 1
                while i < len(lines) and not lines[i].strip().upper().startswith("END STRUCT"):
                    field_line = lines[i].strip()
                    if field_line:
                        field_name, field_type = [x.strip() for x in field_line.split("AS")]
                        type_fields[struct_name].append((field_name, field_type))
                    i += 1
                self.types[current_type] = {"kind": "STRUCT", "fields": type_fields[current_type]}
                current_type = None  # Reset current_type
                i += 1  # END STRUCT satırını atla
            elif line_upper.startswith("UNION "):
                union_name = line[6:].strip()
                current_type = union_name
                type_fields[union_name] = []
                i += 1
                while i < len(lines) and not lines[i].strip().upper().startswith("END UNION"):
                    field_line = lines[i].strip()
                    if field_line:
                        field_name, field_type = [x.strip() for x in field_line.split("AS")]
                        type_fields[union_name].append((field_name, field_type))
                    i += 1
                self.types[current_type] = {"kind": "UNION", "fields": type_fields[current_type]}
                current_type = None  # Reset current_type
                i += 1  # END UNION satırını atla
            elif line_upper.startswith("DATAFRAME "):
                # DATAFRAME var_name ... END DATAFRAME syntax
                dataframe_name = line[10:].strip()
                dataframe_data = {}
                i += 1
                while i < len(lines) and not lines[i].strip().upper().startswith("END DATAFRAME"):
                    data_line = lines[i].strip()
                    if data_line and not data_line.startswith("'") and not data_line.startswith("REM"):
                        # "column_name": [values] formatını parse et
                        if ':' in data_line:
                            col_name, col_values = data_line.split(':', 1)
                            col_name = col_name.strip().strip('"')
                            col_values = col_values.strip()
                            
                            # Array formatını parse et [value1, value2, ...]
                            if col_values.startswith('[') and col_values.endswith(']'):
                                col_values = col_values[1:-1]  # [] karakterlerini kaldır
                                values = []
                                for val in col_values.split(','):
                                    val = val.strip().strip('"')
                                    # Değeri uygun tipe çevir
                                    try:
                                        if '.' in val:
                                            values.append(float(val))
                                        else:
                                            values.append(int(val))
                                    except ValueError:
                                        values.append(val)  # String olarak kalsın
                                dataframe_data[col_name] = values
                    i += 1
                
                # DataFrame oluştur ve global_vars'a ekle
                if pd is not None:
                    df = pd.DataFrame(dataframe_data)
                    self.global_vars[dataframe_name] = df
                else:
                    # Pandas yoksa basit dict olarak sakla
                    self.global_vars[dataframe_name] = dataframe_data
                i += 1  # END DATAFRAME satırını atla
            elif line_upper.startswith("COMPILE"):
                self.bytecode = self.compile_to_bytecode(code)
                return None
            else:
                if current_sub or current_function:
                    self.program.append((line, current_sub or current_function))
                    self.modules[module_name]["program"].append((line, current_sub or current_function))
                else:
                    self.program.append((line, None))
                    self.modules[module_name]["program"].append((line, None))
                i += 1

    def import_module(self, file_name, module_name=None):
        ext = os.path.splitext(file_name)[1].lower()
        if ext not in (".basx", ".libx", ".hx", ".hz"):
            for try_ext in [".hz", ".hx"]:
                if os.path.exists(file_name + try_ext):
                    file_name = file_name + try_ext
                    ext = try_ext
                    break
            else:
                raise Exception("Desteklenmeyen dosya uzantisi. Uzanti .basX, .libX, .hX veya .hz olmali")
        if not os.path.exists(file_name):
            raise Exception(f"Dosya bulunamadi: {file_name}")
        module_name = module_name or os.path.splitext(os.path.basename(file_name))[0]
        if module_name in self.modules:
            raise Exception(f"Modul zaten yuklu: {module_name}")
        with open(file_name, 'r', encoding='utf-8') as f:
            code = f.read()
        old_program = self.program
        old_functions = self.functions.copy()
        old_subs = self.subs.copy()
        old_classes = self.classes.copy()
        old_types = self.types.copy()
        old_labels = self.labels.copy()
        old_module = self.current_module
        self.program = []
        self.functions.clear()
        self.subs.clear()
        self.classes.clear()
        self.types.clear()
        self.labels.clear()
        if ext == ".hz":
            self.parse_program(code, module_name, lightweight=True)
        elif ext == ".hx":
            self.parse_definitions(code, module_name)
        elif ext == ".libx":
            self.parse_program(code, module_name, as_library=True)
        else:
            self.parse_program(code, module_name)
        self.program = old_program
        self.functions.update(old_functions)
        self.subs.update(old_subs)
        self.classes.update(old_classes)
        self.types.update(old_types)
        self.labels.update(old_labels)
        self.current_module = old_module

    def parse_definitions(self, code, module_name):
        pass

    def execute_method(self, method_name, method_body, params, args, scope_name):
        if len(args) != len(params):
            raise Exception(f"Parametre uyusmazligi: {method_name}")
        local_scope = {p: a for p, a in zip(params, args)}
        self.local_scopes.append(local_scope)
        for line_item in method_body:
            if isinstance(line_item, tuple):
                line = line_item[0]
                line_scope = line_item[1] if len(line_item) > 1 else scope_name
            else:
                line = line_item
                line_scope = scope_name
            self.execute_command(line, line_scope)
        self.local_scopes.pop()
        return local_scope.get('RETURN', None)

    def evaluate_expression(self, expr, scope_name=None):
        """İfadeleri degerlendir - BASIC syntax'ini destekler
        
        Array erişimi için N-boyutlu dizi desteği:
        - array(i)
        - array(i,j)
        - array(i,j,k)
        - array(i,j,k,l,m,...) şeklinde sınırsız boyut desteği
        """
        try:
            expr = expr.strip()
            
            # Arithmetic operation parsing (*, -, /, +) - daha gelismis
            arithmetic_ops = ['*', '/', '-', '+']
            for op in arithmetic_ops:
                if op in expr:
                    # Operator parsing
                    parts = []
                    current_part = ""
                    in_quotes = False
                    paren_count = 0
                    i = 0
                    
                    while i < len(expr):
                        char = expr[i]
                        if char == '"' and (i == 0 or expr[i-1] != '\\'):
                            in_quotes = not in_quotes
                            current_part += char
                        elif char == '(' and not in_quotes:
                            paren_count += 1
                            current_part += char
                        elif char == ')' and not in_quotes:
                            paren_count -= 1
                            current_part += char
                        elif char == op and not in_quotes and paren_count == 0:
                            # Operator bulundu
                            if current_part.strip():
                                parts.append(current_part.strip())
                            current_part = ""
                        else:
                            current_part += char
                        i += 1
                    
                    if current_part.strip():
                        parts.append(current_part.strip())
                    
                    if len(parts) > 1:
                        # Parcalari degerlendir
                        evaluated_parts = []
                        has_string = False
                        
                        for part in parts:
                            part_value = self.evaluate_single_part(part.strip(), scope_name)
                            evaluated_parts.append(part_value)
                            if isinstance(part_value, str) and op == '+':
                                has_string = True
                        
                        # String concatenation sadece + icin
                        if has_string and op == '+':
                            result = ""
                            for val in evaluated_parts:
                                result += str(val) if val is not None else ""
                            return result
                        else:
                            # Arithmetic operations
                            result = evaluated_parts[0]
                            for val in evaluated_parts[1:]:
                                if op == '+':
                                    result += val
                                elif op == '-':
                                    result -= val
                                elif op == '*':
                                    result *= val
                                elif op == '/':
                                    result /= val
                            return result
            
            # Tek parca degerlendirme
            return self.evaluate_single_part(expr, scope_name)
                    
        except Exception as e:
            # Fallback - basit degisken degerlendirmesi
            if expr in self.current_scope():
                return self.current_scope()[expr]
            elif expr in self.global_vars:
                return self.global_vars[expr]
            else:
                raise e
    
    def evaluate_single_part(self, expr, scope_name=None):
        """Tek bir ifade parcasini degerlendir
        
        N-boyutlu dizi erişimi ve ataması için geliştirilmiş destek:
        - array(i), array(i,j), array(i,j,k), array(i,j,k,l,m,...)
        - recursive fonksiyonlarla sınırsız boyut desteği
        """
        expr = expr.strip()
        
        # String literal
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        
        # Nested field access kontrolu (person.address.city)
        if '.' in expr and not expr.replace('.', '').isdigit():
            parts = expr.split('.')
            if len(parts) > 1:
                # İlk parçayı degerlendır
                base_var = parts[0]
                if base_var in self.current_scope():
                    obj = self.current_scope()[base_var]
                elif base_var in self.global_vars:
                    obj = self.global_vars[base_var]
                else:
                    raise Exception(f"Tanimlanmamis degisken: {base_var}")
                
                # Nested field access
                for field_name in parts[1:]:
                    if isinstance(obj, (StructInstance, UnionInstance)):
                        if hasattr(obj, 'get_field'):
                            obj = obj.get_field(field_name)
                        elif hasattr(obj, 'fields') and field_name in obj.fields:
                            obj = obj.fields[field_name]
                        else:
                            raise Exception(f"Gecersiz alan: {field_name}")
                    elif isinstance(obj, dict):
                        if field_name in obj:
                            obj = obj[field_name]
                        else:
                            raise Exception(f"Gecersiz alan: {field_name}")
                    elif hasattr(obj, field_name):
                        obj = getattr(obj, field_name)
                    else:
                        raise Exception(f"Gecersiz alan: {field_name}")
                return obj
        
        # Sayi literal
        try:
            if '.' in expr and expr.replace('.', '').isdigit():
                return float(expr)
            elif expr.isdigit():
                return int(expr)
        except ValueError:
            pass
        
        # Dizi erisimi kontrolu (name(index) veya name(index1, index2, ...))  # Support for n-dimensional arrays
        array_match = re.match(r'(\w+)\s*\(([^)]+)\)', expr)  # Array access with any number of dimensions
                    if array_match:
                        var_name, indices_str = array_match.groups()
                        if var_name in self.current_scope() or var_name in self.global_vars:
                            array_var = self.current_scope().get(var_name) or self.global_vars.get(var_name)
                            if isinstance(array_var, (list, tuple)):
                                # İndisleri degerlendir
                                indices = []
                                for index_expr in indices_str.split(','):
                                    index_val = self.evaluate_single_part(index_expr.strip(), scope_name)
                                    indices.append(int(index_val))
                                
                                try:
                                    # Recursive function to access n-dimensional array
                                    def access_nd_array(array, indices):
                                        if len(indices) == 1:
                                            return array[indices[0]]
                                        return access_nd_array(array[indices[0]], indices[1:])
                                    
                                    return access_nd_array(array_var, indices)
                                except IndexError:
                                    raise Exception(f"Dizi indisi sinir disi: {var_name}({indices_str})")
                                # Eger dizi degilse fonksiyon cagrisi olarak isle        # Fonksiyon cagrisi kontrolu
        if '(' in expr and expr.endswith(')'):
            func_match = re.match(r'(\w+\$?)\((.*)\)', expr)
            if func_match:
                func_name, args_str = func_match.groups()
                
                # User-defined fonksiyon kontrolu
                if func_name in self.user_functions:
                    return self.call_user_function(func_name, args_str, scope_name)
                elif func_name in self.inline_functions:
                    return self.call_inline_function(func_name, args_str, scope_name)
                elif func_name in self.function_table:
                    # Built-in fonksiyon
                    if args_str.strip():
                        args = []
                        current_arg = ""
                        paren_count = 0
                        in_quotes = False
                        
                        for char in args_str:
                            if char == '"' and (not current_arg or current_arg[-1] != '\\'):
                                in_quotes = not in_quotes
                            elif char == '(' and not in_quotes:
                                paren_count += 1
                            elif char == ')' and not in_quotes:
                                paren_count -= 1
                            elif char == ',' and not in_quotes and paren_count == 0:
                                args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
                                current_arg = ""
                                continue
                            current_arg += char
                        
                        if current_arg.strip():
                            args.append(self.evaluate_single_part(current_arg.strip(), scope_name))
                        
                        return self.function_table[func_name](*args)
                    else:
                        return self.function_table[func_name]()
        
        # Degisken
        if expr in self.current_scope():
            return self.current_scope()[expr]
        elif expr in self.global_vars:
            return self.global_vars[expr]
        elif expr in self.function_table:
            return self.function_table[expr]
        
        # User-defined fonksiyon adi (parametresiz cagri)
        if expr in self.user_functions:
            return self.call_user_function(expr, "", scope_name)
        elif expr in self.inline_functions:
            return self.call_inline_function(expr, "", scope_name)
        
        # Python ifadesi olarak degerlendir (son care)
        try:
            namespace = {}
            namespace.update(self.global_vars)
            namespace.update(self.current_scope())
            namespace.update(self.function_table)
            
            # AST kullanarak guvenli degerlendirme
            tree = ast.parse(expr, mode='eval')
            compiled = compile(tree, '<string>', 'eval')
            return eval(compiled, namespace)
        except:
            # Hicbir sey ise yaramazsa string olarak dondur
            return expr

    async def run_async(self, code):
        self.parse_program(code)
        self.running = True
        self.program_counter = 0
        while self.running and self.program_counter < len(self.program):
            prog_item = self.program[self.program_counter]
            if isinstance(prog_item, tuple):
                command = prog_item[0]
                scope = prog_item[1] if len(prog_item) > 1 else None
            else:
                command = prog_item
                scope = None
            if self.debug_mode:
                print(f"DEBUG: Satir {self.program_counter + 1}: {command}")
                await asyncio.sleep(0)
            next_pc = self.execute_command(command, scope)
            if next_pc is not None:
                self.program_counter = next_pc
            else:
                self.program_counter += 1
        self.running = False

    def execute_command(self, command, scope_name=None):
        """Komut çalıştırma"""
        if isinstance(command, tuple):
            command, scope = command
        else:
            scope = scope_name
            
        command = str(command).strip()
        if not command:
            return None
            
        # Program sayacını integer olarak tut
        try:
            self.program_counter = int(self.program_counter)
        except (ValueError, TypeError):
            self.program_counter = 0
            
        # Komutu parçalara ayır
        command_parts = command.split()
        if not command_parts:
            return None
            
        # Komut türünü belirle
        cmd = command_parts[0].upper()
        command_upper = command.upper()
            
        # SELECT CASE özel durumu
        if cmd == "SELECT" and len(command_parts) > 1 and command_parts[1].upper() == "CASE":
            return self._handle_select_case(command, scope)
            
        # DO WHILE/LOOP desteği
        if cmd in ["DO", "LOOP", "EXIT"]:
            if cmd == "DO" or (cmd == "EXIT" and len(command_parts) > 1 and command_parts[1].upper() == "DO") or cmd == "LOOP":
                return self._handle_do_loop(command, scope)
                
        # Diğer kontrol yapıları
        if cmd in ['IF', 'GOTO', 'GOSUB', 'RETURN', 'FOR', 'NEXT', 'WHILE', 'WEND']:
            return self._execute_flow_control(command_parts)
        elif cmd in ['CLASS', 'END CLASS', 'ABSTRACT', 'INTERFACE', 'END INTERFACE', 'IMPLEMENTS']:
            return self._execute_oop_command(command_parts)
        elif cmd in ['PRIVATE', 'PUBLIC', 'PROTECTED', 'STATIC', 'SHARED', 'FINAL', 'CONST']:
            return self._execute_access_modifier(command_parts)
        elif cmd in ['LIBRARY', 'END LIBRARY', 'NAMESPACE', 'END NAMESPACE', 'IMPORT', 'USING']:
            return self._execute_module_command(command_parts)
        elif cmd in ['TRY', 'CATCH', 'FINALLY', 'END TRY', 'THROW']:
            return self._execute_error_handling(command_parts)
        elif cmd in ['PRINT', 'INPUT', 'OPEN', 'CLOSE', 'CALL', 'SHELL']:
            return self._execute_io_command(command_parts)
        elif cmd in ['DIM', 'TYPE', 'END TYPE', 'ENUM', 'END ENUM', 'STRUCT', 'END STRUCT']:
            return self._execute_data_structure(command_parts)
        elif cmd in ['DATABASE', 'QUERY', 'EXECUTE', 'COMMIT', 'ROLLBACK']:
            return self._execute_database_command(command_parts)
        elif cmd in ['HTTP', 'DOWNLOAD', 'UPLOAD', 'SOCKET']:
            return self._execute_network_command(command_parts)
        elif cmd in ['WINDOW', 'BUTTON', 'TEXTBOX', 'ON']:
            return self._execute_gui_command(command_parts)
        elif cmd in ['THREAD', 'LOCK', 'UNLOCK', 'PROCESS']:
            return self._execute_threading_command(command_parts)
        elif cmd in ['DEBUG', 'TRACE', 'ASSERT', 'TEST', 'END TEST']:
            return self._execute_debug_command(command_parts)
        elif cmd in ['GC', 'DISPOSE', 'PROFILE', 'MEMORY']:
            return self._execute_memory_command(command_parts)
        elif cmd in ['LEARN', 'PREDICT', 'TRAIN', 'NEURAL']:
            return self._execute_ai_command(command_parts)
        else:
            return self._execute_expression(command)
            
    def _handle_do_loop(self, command, scope_name=None):
        """DO WHILE döngüsünü işler"""
        command_upper = command.strip().upper()
        
        if command_upper.startswith("DO"):
            # DO WHILE veya basit DO
            match = re.match(r"DO(\s+WHILE\s+(.+))?", command, re.IGNORECASE)
            if not match:
                raise Exception("DO komutunda sozdizimi hatasi")
                
            condition = match.group(2) if match.group(1) else "TRUE"
            self.loop_stack.append(("DO", self.program_counter, condition, scope_name))
            return None
            
        elif command_upper == "LOOP":
            if not self.loop_stack:
                raise Exception("LOOP komutu DO olmadan kullanilamaz")
                
            loop_type, start_pc, condition, loop_scope = self.loop_stack[-1]
            if loop_type != "DO":
                raise Exception("LOOP komutu DO ile eslemiyor")
                
            # Koşulu değerlendir
            if condition != "TRUE":
                if not self.evaluate_expression(condition, loop_scope):
                    self.loop_stack.pop()  # Çık
                    return None
                    
            # Döngüyü devam ettir
            return start_pc + 1  # DO satırının sonrasına dön
            
        elif command_upper == "EXIT DO":
            # En yakın DO döngüsünden çık
            if not any(lt == "DO" for lt, *_ in self.loop_stack):
                raise Exception("EXIT DO komutu DO blogu disinda kullanilamaz")
                
            while self.loop_stack and self.loop_stack[-1][0] != "DO":
                self.loop_stack.pop()
                
            if self.loop_stack:
                self.loop_stack.pop()
                
            # En yakın LOOP'u bul ve atla
            current_pc = self.program_counter
            loop_count = 1
            while current_pc < len(self.program):
                current_pc += 1
                if current_pc >= len(self.program):
                    break
                    
                next_line = self.program[current_pc]
                if isinstance(next_line, tuple):
                    next_line = next_line[0]
                    
                next_line = next_line.strip().upper()
                if next_line == "LOOP":
                    loop_count -= 1
                    if loop_count == 0:
                        return current_pc + 1
                elif next_line.startswith("DO"):
                    loop_count += 1
                    
            raise Exception("DO icin eslesen LOOP bulunamadi")
            
        return None
        
    def _execute_expression(self, expr):
        """İfadeyi değerlendirir ve sonucunu döndürür"""
        if not expr:
            return None
            
        # İfadeyi değerlendirmeye çalış
        try:
            # Değişken atama
            if '=' in expr and not expr.startswith('='):
                var_name, value = expr.split('=', 1)
                var_name = var_name.strip()
                value = value.strip()
                
                # Değeri hesapla
                result = self.evaluate_expression(value)
                
                # Değişkene ata
                self.set_variable(var_name, result)
                return result
                
            # Normal ifade
            return self.evaluate_expression(expr)
            
        except Exception as e:
            self.error(f"İfade değerlendirme hatası: {str(e)}")
            return None
            
    def set_variable(self, name, value):
        """Değişken değerini ayarlar"""
        # Geçerli kapsamı bul
        scope = self._get_current_scope()
        
        # Değişkenin tipi belirtilmiş mi?
        type_match = re.match(r'(\w+)\s+AS\s+(\w+)', name)
        if type_match:
            var_name = type_match.group(1)
            var_type = type_match.group(2).upper()
            
            # Tip dönüşümü yap
            try:
                if var_type in self.type_table:
                    value = self.type_table[var_type](value)
            except:
                raise Exception(f"Tip dönüşüm hatası: {name}")
                
            name = var_name
            
        # Global/local değişken kontrolü
        if name.startswith('GLOBAL '):
            name = name.replace('GLOBAL ', '')
            self.global_vars[name] = value
        else:
            scope[name] = value
            
    def _get_current_scope(self):
        """Geçerli kapsamı döndürür"""
        if not self.local_scopes:
            self.local_scopes.append({})
        return self.local_scopes[-1]
        
    def error(self, message):
        """Hata mesajı basar ve loga kaydeder"""
        error_msg = f"HATA: {message}"
        print(error_msg)
        logging.error(error_msg)
        
    def _pattern_match(self, text, pattern):
        """LIKE operatörü için pattern eşleştirme"""
        # % -> .*, _ -> .
        pattern = pattern.replace('%', '.*').replace('_', '.')
        return bool(re.match(f'^{pattern}$', text))
        
    def _handle_select_case(self, command, scope_name=None):
        """SELECT CASE yapısını işler"""
        # SELECT CASE <expr>
        command_upper = command.strip().upper()
        self.current_scope_name = scope_name
        
        if command_upper.startswith("SELECT CASE"):
            match = re.match(r"SELECT CASE\s+(.+)", command, re.IGNORECASE)
            if not match:
                raise Exception("SELECT CASE komutunda sozdizimi hatasi")
                
            select_expr = match.group(1)
            self.case_value = self.evaluate_expression(select_expr, scope_name)
            self.in_case_block = True
            self.case_matched = False
            return None
            
        elif command_upper.startswith("CASE"):
            if not self.in_case_block:
                raise Exception("CASE komutu SELECT CASE olmadan kullanilamaz")
                
            # CASE ELSE kontrolü
            if command_upper == "CASE ELSE":
                if not self.case_matched:
                    self.case_matched = True
                    return None
                return "SKIP"
                
            # Normal CASE
            case_values = self._parse_case_values(command)
            if not self.case_matched and self._case_value_matches(case_values):
                self.case_matched = True
                return None
            return "SKIP"
            
        elif command_upper == "END SELECT":
            self.in_case_block = False
            self.case_matched = False
            return None
            
        return None
        
    def _parse_select_case(self, command):
        """SELECT CASE ifadesini ayrıştırır ve değeri hesaplar"""
        match = re.match(r"SELECT CASE\s+(.+)", command, re.IGNORECASE)
        if not match:
            raise Exception("SELECT CASE komutunda sozdizimi hatasi")
            
        select_expr = match.group(1)
        return self.evaluate_expression(select_expr)
        
    def _find_case_blocks(self):
        """CASE bloklarını bulur ve döndürür"""
        case_blocks = []
        current_block = None
        current_pc = self.program_counter + 1
        
        while current_pc < len(self.program):
            prog_item = self.program[current_pc]
            line, scope = self._get_line_and_scope(prog_item)
            line_upper = line.strip().upper()
            
            if line_upper.startswith("CASE"):
                if current_block is not None:
                    case_blocks.append(current_block)
                current_block = {"header": line, "body": [], "pc": current_pc}
            elif line_upper.startswith("END SELECT"):
                if current_block is not None:
                    case_blocks.append(current_block)
                break
            else:
                if current_block is not None:
                    current_block["body"].append(prog_item)
            current_pc += 1
            
        return case_blocks
        
    def _get_line_and_scope(self, prog_item):
        """Program satırını ve kapsamını ayıklar"""
        if isinstance(prog_item, tuple):
            line = prog_item[0]
            scope = prog_item[1] if len(prog_item) > 1 else None
        else:
            line = prog_item
            scope = None
            
        return line, scope
        
    def _evaluate_case_blocks(self, case_blocks, select_value):
        """CASE bloklarını değerlendirir ve uygun olanı çalıştırır"""
        matched = False
        else_block = None
        
        for block in case_blocks:
            header = block["header"].strip()
            
            # CASE ELSE kontrolü
            if header.upper().startswith("CASE ELSE"):
                else_block = block
                continue
                
            # Normal CASE değerlendirmesi
            if self._evaluate_case_match(header, select_value):
                matched = True
                self._execute_case_block(block)
                break
                
        # Eşleşme yoksa CASE ELSE
        if not matched and else_block is not None:
            self._execute_case_block(else_block)
            
    def _evaluate_case_match(self, header, select_value):
        """Bir CASE ifadesinin eşleşip eşleşmediğini kontrol eder"""
        case_match = re.match(r"CASE\s+(.+)", header, re.IGNORECASE)
        if not case_match:
            return False
            
        case_values = case_match.group(1).split(",")
        for case_value in case_values:
            case_value = case_value.strip()
            
            if self._check_case_value(case_value, select_value):
                return True
                
        return False
        
    def _check_case_value(self, case_value, select_value):
        """Tek bir case değerini kontrol eder"""
        # Aralık kontrolü
        if ".." in case_value:
            start, end = case_value.split("..")
            start_val = self.evaluate_expression(start)
            end_val = self.evaluate_expression(end)
            return start_val <= select_value <= end_val
            
        # Karşılaştırma operatörü kontrolü
        if case_value.startswith("<") or case_value.startswith(">") or case_value.startswith("="):
            condition = f"{select_value} {case_value}"
            return self.evaluate_expression(condition)
            
        # Tek değer kontrolü
        case_val = self.evaluate_expression(case_value)
        return select_value == case_val
        
    def _handle_do_loop(self, command, scope_name=None):
        """DO WHILE döngüsünü işler"""
        command_upper = command.strip().upper()
        
        if command_upper.startswith("DO"):
            # DO WHILE veya basit DO
            match = re.match(r"DO(\s+WHILE\s+(.+))?", command, re.IGNORECASE)
            if not match:
                raise Exception("DO komutunda sozdizimi hatasi")
                
            condition = match.group(2) if match.group(1) else "TRUE"
            self.loop_stack.append(("DO", self.program_counter, condition, scope_name))
            return None
            
        elif command_upper == "LOOP":
            if not self.loop_stack:
                raise Exception("LOOP komutu DO olmadan kullanilamaz")
                
            loop_type, start_pc, condition, loop_scope = self.loop_stack[-1]
            if loop_type != "DO":
                raise Exception("LOOP komutu DO ile eşleşmiyor")
                
            # Koşulu değerlendir
            if condition != "TRUE":
                if not self.evaluate_expression(condition, loop_scope):
                    self.loop_stack.pop()  # Çık
                    return None
                    
            # Döngüyü devam ettir
            return start_pc + 1  # DO satırının sonrasına dön
            
        elif command_upper == "EXIT DO":
            # En yakın DO döngüsünden çık
            if not any(lt == "DO" for lt, *_ in self.loop_stack):
                raise Exception("EXIT DO komutu DO bloğu dışında kullanılamaz")
                
            while self.loop_stack and self.loop_stack[-1][0] != "DO":
                self.loop_stack.pop()
                
            if self.loop_stack:
                self.loop_stack.pop()
                
            # En yakın LOOP'u bul ve atla
            current_pc = self.program_counter
            loop_count = 1
            while current_pc < len(self.program):
                current_pc += 1
                if current_pc >= len(self.program):
                    break
                    
                next_line = self.program[current_pc]
                if isinstance(next_line, tuple):
                    next_line = next_line[0]
                    
                next_line = next_line.strip().upper()
                if next_line == "LOOP":
                    loop_count -= 1
                    if loop_count == 0:
                        return current_pc + 1
                elif next_line.startswith("DO"):
                    loop_count += 1
                    
            raise Exception("DO için eşleşen LOOP bulunamadı")
            
        return None
        
    def _execute_case_block(self, block):
        """Bir CASE bloğunun içindeki komutları çalıştırır"""
        for line in block["body"]:
            if isinstance(line, tuple):
                self.execute_command(line[0], line[1])
            else:
                self.execute_command(line)
            # SELECT CASE <expr>
            match = re.match(r"SELECT CASE\s+(.+)", command, re.IGNORECASE)
            if not match:
                raise Exception("SELECT CASE komutunda sozdizimi hatasi")
            select_expr = match.group(1)
            select_value = self.evaluate_expression(select_expr, scope_name)
            # CASE bloklarini bul ve uygun olani calistir
            case_blocks = []
            current_block = None
            current_pc = self.program_counter + 1
            while current_pc < len(self.program):
                prog_item = self.program[current_pc]
                # Satir tuple mi string mi?
                if isinstance(prog_item, tuple):
                    line = prog_item[0]
                    scope = prog_item[1] if len(prog_item) > 1 else None
                else:
                    line = prog_item
                    scope = None
                line_upper = line.strip().upper()
                if line_upper.startswith("CASE"):
                    if current_block is not None:
                        case_blocks.append(current_block)
                    current_block = {"header": line, "body": [], "pc": current_pc}
                elif line_upper.startswith("END SELECT"):
                    if current_block is not None:
                        case_blocks.append(current_block)
                    break
                else:
                    if current_block is not None:
                        # Satiri oldugu gibi ekle (tuple veya string)
                        current_block["body"].append(prog_item)
                current_pc += 1
            # CASE bloklarini sirayla kontrol et
            matched = False
            else_block = None
            for block in case_blocks:
                header = block["header"].strip()
                if header.upper().startswith("CASE ELSE"):
                    else_block = block
                    continue
                case_match = re.match(r"CASE\s+(.+)", header, re.IGNORECASE)
                if not case_match:
                    continue
                case_cond = case_match.group(1)
                # Coklu deger/kosul destegi: CASE 1,2,3 veya CASE IS > 5
                conds = [c.strip() for c in case_cond.split(",")]
                for cond in conds:
                    if cond.upper().startswith("IS "):
                        # CASE IS > 5 gibi
                        op_match = re.match(r"IS\s*([<>=!]+)\s*(.+)", cond, re.IGNORECASE)
                        if op_match:
                            op, val = op_match.groups()
                            val_eval = self.evaluate_expression(val, scope_name)
                            try:
                                if op == "=":
                                    if select_value == val_eval:
                                        matched = True
                                elif op == ">":
                                    if select_value > val_eval:
                                        matched = True
                                elif op == "<":
                                    if select_value < val_eval:
                                        matched = True
                                elif op == ">=":
                                    if select_value >= val_eval:
                                        matched = True
                                elif op == "<=":
                                    if select_value <= val_eval:
                                        matched = True
                                elif op == "<>" or op == "!=" or op == "!=":
                                    if select_value != val_eval:
                                        matched = True
                            except Exception:
                                pass
                        if matched:
                            break
                    else:
                        # CASE 1,2,3 gibi
                        val_eval = self.evaluate_expression(cond, scope_name)
                        try:
                            if select_value == val_eval:
                                matched = True
                                break
                        except Exception:
                            pass
                if matched:
                    # Bu CASE blogunu calistir
                    for case_line in block["body"]:
                        # Satir tuple ise unpack et, degilse string olarak gonder
                        if isinstance(case_line, tuple):
                            self.execute_command(case_line[0], case_line[1] if len(case_line) > 1 else scope_name)
                        else:
                            self.execute_command(case_line, scope_name)
                    # END SELECT'e atla
                    self.program_counter = current_pc
                    return self.program_counter
            # CASE ELSE varsa ve hicbiri eslesmediyse
            if else_block:
                for case_line in else_block["body"]:
                    if isinstance(case_line, tuple):
                        self.execute_command(case_line[0], case_line[1] if len(case_line) > 1 else scope_name)
                    else:
                        self.execute_command(case_line, scope_name)
                self.program_counter = current_pc
                return self.program_counter
            # Hicbir CASE eslesmediyse, END SELECT'e atla
            self.program_counter = current_pc
            return self.program_counter

        if command_upper.startswith("CASE") or command_upper.startswith("END SELECT"):
            # SELECT CASE blogu icindeki satirlar, ana akista burada islenmez
            return None

        if self.trace_mode:
            print(f"TRACE: Satir {self.program_counter + 1}: {command}")

        try:
            # REPL ve dosya islemi komutlari
            if command_upper == "REPL":
                self.start_repl()
                return None
                
            if command_upper.startswith("SAVE"):
                match = re.match(r"SAVE\s+([^\s]+)", command, re.IGNORECASE)
                if match:
                    filename = match.group(1)
                    self.save_program(filename)
                else:
                    print("Kullanim: SAVE <dosya_adi>")
                return None
                
            if command_upper.startswith("LOAD"):
                match = re.match(r"LOAD\s+([^\s]+)", command, re.IGNORECASE)
                if match:
                    filename = match.group(1)
                    self.load_program(filename)
                else:
                    print("Kullanim: LOAD <dosya_adi>")
                return None
                
            if command_upper.startswith("RUN"):
                if len(command.split()) > 1:
                    # RUN filename
                    match = re.match(r"RUN\s+([^\s]+)", command, re.IGNORECASE)
                    if match:
                        filename = match.group(1)
                        self.run_program(filename)
                else:
                    # RUN (mevcut programi calistir)
                    if self.program:
                        old_pc = self.program_counter
                        self.program_counter = 0
                        try:
                            # Program zaten parse edilmis durumda, sadece calistir
                            old_running = self.running
                            self.running = True
                            
                            while self.running and self.program_counter < len(self.program):
                                prog_item = self.program[self.program_counter]
                                if isinstance(prog_item, tuple):
                                    command = prog_item[0]
                                    scope = prog_item[1] if len(prog_item) > 1 else None
                                else:
                                    command = prog_item
                                    scope = None
                                
                                next_pc = self.execute_command(command, scope)
                                if next_pc is not None:
                                    self.program_counter = next_pc
                                else:
                                    self.program_counter += 1
                            
                            self.running = old_running
                        finally:
                            self.program_counter = old_pc
                    else:
                        print("Calistirilacak program yok.")
                return None
            if command_upper.startswith("IMPORT"):
                match = re.match(r"IMPORT\s+([^\s]+)(?:\s+AS\s+(\w+))?", command, re.IGNORECASE)
                if match:
                    file_name, alias = match.groups()
                    module_name = alias or os.path.splitext(os.path.basename(file_name))[0]
                    self.import_module(file_name, module_name)
                    return None
                else:
                    raise Exception("IMPORT komutunda sozdizimi hatasi")

            if command_upper.startswith("ON ERROR GOTO"):
                match = re.match(r"ON ERROR GOTO\s+(\w+)", command, re.IGNORECASE)
                if match:
                    label = match.group(1)
                    if label in self.labels:
                        self.error_handler = self.labels[label]
                    else:
                        raise Exception(f"Etiket bulunamadi: {label}")
                    return None
                else:
                    raise Exception("ON ERROR GOTO komutunda sozdizimi hatasi")

            if command_upper.startswith("ON GOSUB"):
                match = re.match(r"ON GOSUB\s+(\w+)", command, re.IGNORECASE)
                if match:
                    label = match.group(1)
                    if label in self.labels:
                        self.gosub_handler = self.labels[label]
                    else:
                        raise Exception(f"Etiket bulunamadi: {label}")
                    return None
                else:
                    raise Exception("ON GOSUB komutunda sozdizimi hatasi")

            if command_upper.startswith("PRINT"):
                print_expr = command[5:].strip()
                if print_expr:
                    # Semicolon kontrolu - satir sonu yazdirilmayacak mi?
                    newline = True
                    if print_expr.endswith(';'):
                        newline = False
                        print_expr = print_expr[:-1].strip()
                    
                    # Virgulle ayrilmis ifadeler
                    if ',' in print_expr or ';' in print_expr:
                        parts = []
                        separators = []  # Ayraclarin turunu takip et
                        current_part = ""
                        in_quotes = False
                        paren_count = 0
                        
                        for char in print_expr:
                            if char == '"' and (not current_part or current_part[-1] != '\\'):
                                in_quotes = not in_quotes
                            elif char == '(' and not in_quotes:
                                paren_count += 1
                            elif char == ')' and not in_quotes:
                                paren_count -= 1
                            elif (char == ',' or char == ';') and not in_quotes and paren_count == 0:
                                parts.append(current_part.strip())
                                separators.append(char)  # Ayiraci kaydet
                                current_part = ""
                                continue
                            current_part += char
                        
                        if current_part.strip():
                            parts.append(current_part.strip())
                        
                        values = []
                        for part in parts:
                            try:
                                result = self.evaluate_expression(part, scope_name)
                                values.append(result)
                            except Exception as e:
                                # Fallback - string literal kontrolu
                                if part.startswith('"') and part.endswith('"'):
                                    values.append(part[1:-1])
                                elif part in self.current_scope():
                                    values.append(self.current_scope()[part])
                                elif part in self.global_vars:
                                    values.append(self.global_vars[part])
                                else:
                                    values.append(part)
                        
                        # BASIC tarzi yazdirma: ; icin bosluk yok, , icin tab benzeri
                        output = ""
                        for i, value in enumerate(values):
                            output += str(value)
                            if i < len(separators):
                                if separators[i] == ',':
                                    output += "\t"  # Virgul icin tab
                                elif separators[i] == ';':
                                    pass  # Semicolon icin bosluk ekleme
                        
                        if newline:
                            print(output)
                        else:
                            print(output, end="")
                    else:
                        # Tek ifade
                        try:
                            result = self.evaluate_expression(print_expr, scope_name)
                            if newline:
                                print(result)
                            else:
                                print(result, end="")
                        except Exception as e:
                            # Fallback - string literal kontrolu
                            if print_expr.startswith('"') and print_expr.endswith('"'):
                                value = print_expr[1:-1]
                            elif print_expr in self.current_scope():
                                value = self.current_scope()[print_expr]
                            elif print_expr in self.global_vars:
                                value = self.global_vars[print_expr]
                            else:
                                value = print_expr
                            
                            if newline:
                                print(value)
                            else:
                                print(value, end="")
                else:
                    print()  # Bos satir
                return None

            if command_upper.startswith("INPUT"):
                match = re.match(r"INPUT\s+\"([^\"]+)\",\s*(\w+)", command, re.IGNORECASE)
                if match:
                    prompt, var_name = match.groups()
                    value = input(prompt)
                    self.current_scope()[var_name] = value
                    return None
                else:
                    raise Exception("INPUT komutunda sozdizimi hatasi")

            # Nested field assignment kontrolu (person.address.city = value)
            nested_field_assign_match = re.match(r"([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)+)\s*=\s*(.+)", command, re.IGNORECASE)
            if nested_field_assign_match:
                field_path, expr = nested_field_assign_match.groups()
                value = self.evaluate_expression(expr, scope_name)
                
                # Field path'i parse et (person.address.city -> ['person', 'address', 'city'])
                parts = field_path.split('.')
                if len(parts) < 2:
                    raise Exception("Gecersiz field path")
                
                # İlk objeyi bul
                base_var = parts[0]
                if base_var in self.current_scope():
                    obj = self.current_scope()[base_var]
                elif base_var in self.global_vars:
                    obj = self.global_vars[base_var]
                else:
                    raise Exception(f"Tanimlanmamis degisken: {base_var}")
                
                # Son field haricindeki tum field'lari traverse et
                for field_name in parts[1:-1]:
                    if isinstance(obj, (StructInstance, UnionInstance)):
                        if hasattr(obj, 'get_field'):
                            obj = obj.get_field(field_name)
                        elif hasattr(obj, 'fields') and field_name in obj.fields:
                            obj = obj.fields[field_name]
                        else:
                            raise Exception(f"Gecersiz alan: {field_name}")
                    elif isinstance(obj, dict):
                        if field_name in obj:
                            obj = obj[field_name]
                        else:
                            raise Exception(f"Gecersiz alan: {field_name}")
                    else:
                        raise Exception(f"Gecersiz field access: {field_name}")
                
                # Son field'a degeri ata
                final_field = parts[-1]
                if isinstance(obj, (StructInstance, UnionInstance)):
                    obj.set_field(final_field, value)
                elif isinstance(obj, dict):
                    obj[final_field] = value
                else:
                    raise Exception(f"Gecersiz field assignment: {final_field}")
                
                return None

            # Direkt atama kontrolu (var = value veya array(index) = value)
            # LET olmadan direkt atama yapilabilir
            direct_array_assign_match = re.match(r"(\w+)\s*\(([^)]+)\)\s*=\s*(.+)", command, re.IGNORECASE)
            if direct_array_assign_match:
                var_name, indices_str, expr = direct_array_assign_match.groups()
                value = self.evaluate_expression(expr, scope_name)
                
                # İndisleri degerlendir
                indices = []
                for index_expr in indices_str.split(','):
                    index_val = self.evaluate_expression(index_expr.strip(), scope_name)
                    indices.append(int(index_val))
                
                # N-boyutlu dizi atama
                if var_name in self.current_scope():
                    array_var = self.current_scope()[var_name]
                elif var_name in self.global_vars:
                    array_var = self.global_vars[var_name]
                else:
                    raise Exception(f"Tanimlanmamis dizi: {var_name}")
                
                try:
                    # Recursive function to assign to n-dimensional array
                    def assign_nd_array(array, indices, value):
                        if len(indices) == 1:
                            array[indices[0]] = value
                            return
                        assign_nd_array(array[indices[0]], indices[1:], value)
                    
                    assign_nd_array(array_var, indices, value)
                except IndexError:
                    raise Exception(f"Dizi indisi sinir disi: {var_name}({indices_str})")
                return None

            # Normal direkt atama kontrolu (var = value)
            direct_assign_match = re.match(r"(\w+)\s*=\s*(.+)", command, re.IGNORECASE)
            if direct_assign_match:
                var_name, expr = direct_assign_match.groups()
                # Bu komutlari direkt atama olarak isleme - bunlar baska komutlar
                if var_name.upper() in ['FOR', 'IF', 'WHILE', 'DIM', 'PRINT', 'INPUT', 'GOSUB', 'GOTO', 'RETURN', 'END', 'REM', 'CALL']:
                    pass  # Bu bir komut, direkt atama degil
                else:
                    # Degisken tanimli mi kontrol et
                    if var_name not in self.current_scope() and var_name not in self.global_vars:
                        raise Exception(f"Tanimlanmamis degisken: {var_name}. Once DIM ile tanimlayin.")
                    value = self.evaluate_expression(expr, scope_name)
                    self.current_scope()[var_name] = value
                    return None

            if command_upper.startswith("LET"):
                # Dizi atamasi kontrolu (LET array(index) = value)
                array_assign_match = re.match(r"LET\s+(\w+)\s*\(([^)]+)\)\s*=\s*(.+)", command, re.IGNORECASE)
                if array_assign_match:
                    var_name, indices_str, expr = array_assign_match.groups()
                    value = self.evaluate_expression(expr, scope_name)
                    
                    # İndisleri degerlendir
                    indices = []
                    for index_expr in indices_str.split(','):
                        index_val = self.evaluate_expression(index_expr.strip(), scope_name)
                        indices.append(int(index_val))
                    
                    # Dizi atama
                    if var_name in self.current_scope():
                        array_var = self.current_scope()[var_name]
                    elif var_name in self.global_vars:
                        array_var = self.global_vars[var_name]
                    else:
                        raise Exception(f"Tanimlanmamis dizi: {var_name}")
                    
                    try:
                        # Recursive function to assign to n-dimensional array
                        def assign_nd_array(array, indices, value):
                            if len(indices) == 1:
                                array[indices[0]] = value
                                return
                            assign_nd_array(array[indices[0]], indices[1:], value)
                        
                        assign_nd_array(array_var, indices, value)
                    except IndexError:
                        raise Exception(f"Dizi indisi sinir disi: {var_name}({indices_str})")
                    return None
                
                # Normal degisken atamasi (LET var = value)
                normal_assign_match = re.match(r"LET\s+(\w+)\s*=\s*(.+)", command, re.IGNORECASE)
                if normal_assign_match:
                    var_name, expr = normal_assign_match.groups()
                    value = self.evaluate_expression(expr, scope_name)
                    self.current_scope()[var_name] = value
                    return None
                
                raise Exception("LET komutunda sozdizimi hatasi")

            if command_upper.startswith("DIM"):
                    # N-boyutlu dizi yaratma yardımcı fonksiyonları
                    def create_nd_array(dimensions, default_value):
                        """N-boyutlu dizi yaratır
                        Args:
                            dimensions: Boyut listesi
                            default_value: Başlangıç değeri
                        Returns:
                            N-boyutlu dizi"""
                        if len(dimensions) == 1:
                            return [default_value] * dimensions[0]
                        return [create_nd_array(dimensions[1:], default_value) for _ in range(dimensions[0])]
                    
                    def parse_dimensions(dimensions_str):
                        """Boyut string'ini parse eder
                        Args:
                            dimensions_str: "N1,N2,...,Nn" formatında string
                        Returns:
                            [N1, N2, ..., Nn] listesi"""
                        return [int(d.strip()) + 1 for d in dimensions_str.split(',')] # +1 for BASIC style indexing
                    
                    # DIM AS STRING ARRAY
                    string_array_match = re.match(r"DIM\s+(\w+)\s*\(([^)]+)\)\s+AS\s+STRING", command, re.IGNORECASE)
                    if string_array_match:
                        var_name, dimensions = string_array_match.groups()
                        dims = parse_dimensions(dimensions)
                        self.current_scope()[var_name] = create_nd_array(dims, "")
                        return None
                    
                    # DIM AS ARRAY 
                    array_type_match = re.match(r"DIM\s+(\w+)\s*\(([^)]+)\)\s+AS\s+ARRAY", command, re.IGNORECASE)
                    if array_type_match:
                        var_name, dimensions = array_type_match.groups()
                        dims = parse_dimensions(dimensions)
                        self.current_scope()[var_name] = create_nd_array(dims, None)
                        return None
                    
                    # DIM name(size1,size2,...) - numeric array
                    array_match = re.match(r"DIM\s+(\w+)\s*\(([^)]+)\)", command, re.IGNORECASE)
                    if array_match:
                        var_name, dimensions = array_match.groups() 
                        dims = parse_dimensions(dimensions)
                        self.current_scope()[var_name] = create_nd_array(dims, 0)
                        return None                # Normal degisken tanimlamasi (DIM name AS type)
                type_match = re.match(r"DIM\s+(\w+)\s+AS\s+(\w+)", command, re.IGNORECASE)
                if type_match:
                    var_name, var_type = type_match.groups()
                    if var_type.upper() == "STRUCT":
                        self.current_scope()[var_name] = StructInstance([], self.type_table)
                    elif var_type.upper() == "UNION":
                        self.current_scope()[var_name] = UnionInstance([], self.type_table)
                    elif var_type.upper() == "LIST":
                        self.current_scope()[var_name] = []
                    elif var_type.upper() == "DICT":
                        self.current_scope()[var_name] = {}
                    elif var_type.upper() == "SET":
                        self.current_scope()[var_name] = set()
                    elif var_type.upper() == "TUPLE":
                        self.current_scope()[var_name] = ()
                    elif var_type.upper() == "DATAFRAME":
                        # DataFrame oluştur
                        if pd is not None:
                            self.current_scope()[var_name] = pd.DataFrame()
                        else:
                            self.current_scope()[var_name] = {}
                    elif var_type.upper() == "ARRAY":
                        # Temel array tipi
                        self.current_scope()[var_name] = []
                    elif var_type.upper().startswith("FIXED ARRAY["):
                        # Sabit boyutlu dizi (FIXED ARRAY[10,5,3] gibi)
                        match = re.match(r"FIXED\s+ARRAY\[([^\]]+)\]", var_type, re.IGNORECASE)
                        if match:
                            dimensions = [int(d.strip()) + 1 for d in match.group(1).split(',')]  # +1 for BASIC style indexing
                            def create_fixed_array(dims):
                                if len(dims) == 1:
                                    return [None] * dims[0]
                                return [create_fixed_array(dims[1:]) for _ in range(dims[0])]
                            self.current_scope()[var_name] = create_fixed_array(dimensions)
                        else:
                            raise Exception(f"FIXED ARRAY tanımında sözdizimi hatası: {var_type}")
                    elif var_type.upper().startswith("DYNAMIC ARRAY"):
                        # Dinamik dizi
                        self.current_scope()[var_name] = []  # Başlangıçta boş liste, REDIM ile boyutlandırılacak
                    elif var_type in self.types:
                        # Kullanici tanimli tip
                        type_info = self.types[var_type]
                        if type_info["kind"] == "STRUCT":
                            struct_instance = StructInstance(type_info["fields"], self.type_table)
                            # Nested STRUCT field'larını initialize et
                            self._initialize_nested_struct_fields(struct_instance, type_info["fields"])
                            self.current_scope()[var_name] = struct_instance
                        elif type_info["kind"] == "UNION":
                            self.current_scope()[var_name] = UnionInstance(type_info["fields"], self.type_table)
                        else:
                            self.current_scope()[var_name] = self.type_table.get(var_type.upper(), object)()
                    else:
                        self.current_scope()[var_name] = self.type_table.get(var_type.upper(), object)()
                    return None
                
                # Basit degisken tanimlamasi (DIM name)
                simple_match = re.match(r"DIM\s+(\w+)\s*$", command, re.IGNORECASE)
                if simple_match:
                    var_name = simple_match.group(1)
                    self.current_scope()[var_name] = 0  # Varsayilan deger
                    return None
                
                raise Exception("DIM komutunda sozdizimi hatasi")

            if command_upper.startswith("IF"):
                # İki tur IF: tek satir (IF...THEN...ELSE) ve blok (IF...THEN...END IF)
                if re.match(r"IF\s+.+\s+THEN\s+.+", command, re.IGNORECASE) and not command.upper().endswith("END IF"):
                    # Tek satir IF THEN
                    match = re.match(r"IF\s+(.+)\s+THEN\s+(.+?)(?:\s+ELSE\s+(.+))?$", command, re.IGNORECASE)
                    if match:
                        condition, then_cmd, else_cmd = match.groups()
                        if self.evaluate_expression(condition, scope_name):
                            return self.execute_command(then_cmd, scope_name)
                        elif else_cmd:
                            return self.execute_command(else_cmd, scope_name)
                        return None
                    else:
                        raise Exception("Tek satir IF komutunda sozdizimi hatasi")
                else:
                    # Blok IF (IF ... THEN ... END IF)
                    match = re.match(r"IF\s+(.+)\s+THEN\s*$", command, re.IGNORECASE)
                    if match:
                        condition = match.group(1)
                        if self.evaluate_expression(condition, scope_name):
                            # IF kosulu dogru, normal calismaya devam
                            return None
                        else:
                            # IF kosulu yanlis, ELSE veya END IF'e kadar atla
                            if_count = 1
                            current_pc = self.program_counter + 1
                            found_else = False
                            while current_pc < len(self.program) and if_count > 0:
                                prog_item = self.program[current_pc]
                                if isinstance(prog_item, tuple):
                                    line = prog_item[0].upper().strip()
                                else:
                                    line = prog_item.upper().strip()
                                if line.startswith("IF") and line.endswith("THEN"):
                                    if_count += 1
                                elif line == "END IF":
                                    if_count -= 1
                                    if if_count == 0:
                                        # END IF bulundu, oraya atla
                                        return current_pc
                                elif line == "ELSE" and if_count == 1:
                                    # Ayni seviyedeki ELSE bulundu
                                    found_else = True
                                    return current_pc
                                elif line.startswith("ELSEIF") and if_count == 1:
                                    # ELSEIF bulundu - kosulu kontrol et
                                    elseif_match = re.match(r"ELSEIF\s+(.+)\s+THEN\s*$", line, re.IGNORECASE)
                                    if elseif_match:
                                        elseif_condition = elseif_match.group(1)
                                        if self.evaluate_expression(elseif_condition, scope_name):
                                            # ELSEIF kosulu dogru, buradan devam et
                                            return current_pc
                                current_pc += 1
                            # END IF bulunamadi
                            if if_count > 0:
                                raise Exception("IF icin eslesen END IF bulunamadi")
                            return current_pc
                    else:
                        raise Exception("IF komutunda sozdizimi hatasi")
                        
            if command_upper == "ELSE":
                # ELSE'e gelinmisse, IF blogu calismisti, END IF'e atla
                if_count = 1
                current_pc = self.program_counter + 1
                while current_pc < len(self.program) and if_count > 0:
                    prog_item = self.program[current_pc]
                    if isinstance(prog_item, tuple):
                        line = prog_item[0].upper().strip()
                    else:
                        line = prog_item.upper().strip()
                    if line.startswith("IF") and line.endswith("THEN"):
                        if_count += 1
                    elif line == "END IF":
                        if_count -= 1
                    current_pc += 1
                return current_pc - 1  # END IF'in bir oncesi
                
            if command_upper.startswith("ELSEIF"):
                # ELSEIF'e gelinmisse, onceki kosul dogruydu, END IF'e atla
                if_count = 1
                current_pc = self.program_counter + 1
                while current_pc < len(self.program) and if_count > 0:
                    prog_item = self.program[current_pc]
                    if isinstance(prog_item, tuple):
                        line = prog_item[0].upper().strip()
                    else:
                        line = prog_item.upper().strip()
                    if line.startswith("IF") and line.endswith("THEN"):
                        if_count += 1
                    elif line == "END IF":
                        if_count -= 1
                    current_pc += 1
                return current_pc - 1  # END IF'in bir oncesi
                
            if command_upper.startswith("SELECT CASE"):
                # SELECT CASE yapısını işle
                match = re.match(r"SELECT CASE\s+(.+)", command, re.IGNORECASE)
                if match:
                    expr = match.group(1)
                    value = self.evaluate_expression(expr, scope_name)
                    self.loop_stack.append({
                        "type": "SELECT_CASE",
                        "value": value,
                        "matched": False
                    })
                    return None
                else:
                    raise Exception("SELECT CASE komutunda sözdizimi hatası")
                
            if command_upper.startswith("CASE"):
                if not self.loop_stack or self.loop_stack[-1]["type"] != "SELECT_CASE":
                    raise Exception("CASE için eşleşen SELECT CASE bulunamadı")
                    
                if self.loop_stack[-1]["matched"]:
                    # Önceki CASE eşleşti, diğerlerini atla
                    return None
                    
                loop_info = self.loop_stack[-1]
                value = loop_info["value"]
                
                if command_upper == "CASE ELSE":
                    # CASE ELSE her zaman çalışır
                    loop_info["matched"] = True
                    return None
                    
                match = re.match(r"CASE\s+(.+)", command, re.IGNORECASE)
                if match:
                    cases = match.group(1).split(",")
                    for case in cases:
                        case = case.strip()
                        if case.startswith("IS "):
                            # IS = veya IS > gibi karşılaştırmalar
                            op_match = re.match(r"IS\s*([=<>!]+)\s*(.+)", case)
                            if op_match:
                                op, case_val = op_match.groups()
                                case_val = self.evaluate_expression(case_val, scope_name)
                                if eval(f"{value} {op} {case_val}"):
                                    loop_info["matched"] = True
                                    return None
                        elif ".." in case:
                            # Aralık kontrolü (5..10 gibi)
                            start, end = case.split("..")
                            start = self.evaluate_expression(start.strip(), scope_name)
                            end = self.evaluate_expression(end.strip(), scope_name)
                            if start <= value <= end:
                                loop_info["matched"] = True
                                return None
                        else:
                            # Tek değer kontrolü
                            case_val = self.evaluate_expression(case, scope_name)
                            if value == case_val:
                                loop_info["matched"] = True
                                return None
                    return None
                else:
                    raise Exception("CASE komutunda sözdizimi hatası")
            
            if command_upper == "END SELECT":
                if not self.loop_stack or self.loop_stack[-1]["type"] != "SELECT_CASE":
                    raise Exception("END SELECT için eşleşen SELECT CASE bulunamadı")
                self.loop_stack.pop()
                return None
                
            if command_upper.startswith("DO"):
                # DO / DO WHILE / DO UNTIL
                match = re.match(r"DO(?:\s+(WHILE|UNTIL)\s+(.+))?", command, re.IGNORECASE)
                if match:
                    loop_type, condition = match.groups()
                    loop_info = {
                        "type": "DO",
                        "condition_type": loop_type,  # WHILE, UNTIL veya None
                        "condition": condition,       # Koşul ifadesi veya None
                        "start": self.program_counter + 1
                    }
                    
                    if loop_type:  # DO WHILE/UNTIL - başlangıçta kontrol et
                        condition_result = self.evaluate_expression(condition, scope_name)
                        if (loop_type == "WHILE" and not condition_result) or \
                           (loop_type == "UNTIL" and condition_result):
                            # Koşul sağlanmıyor, LOOP'a kadar atla
                            while self.program_counter < len(self.program):
                                prog_item = self.program[self.program_counter]
                                line = prog_item[0] if isinstance(prog_item, tuple) else prog_item
                                if line.strip().upper() == "LOOP":
                                    break
                                self.program_counter += 1
                            return None
                    
                    self.loop_stack.append(loop_info)
                    return None
                else:
                    raise Exception("DO komutunda sözdizimi hatası")
            
            if command_upper == "LOOP":
                if not self.loop_stack or self.loop_stack[-1]["type"] != "DO":
                    raise Exception("LOOP için eşleşen DO bulunamadı")
                
                loop_info = self.loop_stack[-1]
                condition_type = loop_info["condition_type"]
                condition = loop_info["condition"]
                
                if condition_type:  # WHILE/UNTIL koşulu kontrol et
                    condition_result = self.evaluate_expression(condition, scope_name)
                    if (condition_type == "WHILE" and condition_result) or \
                       (condition_type == "UNTIL" and not condition_result):
                        # Koşul sağlanıyor, döngü başına dön
                        return loop_info["start"]
                    else:
                        # Koşul artık sağlanmıyor, döngüden çık
                        self.loop_stack.pop()
                        return None
                else:  # Basit DO - koşulsuz dön
                    return loop_info["start"]

            if command_upper == "END IF":
                # END IF - sadece devam et
                return None

            if command_upper == "END DATAFRAME":
                # END DATAFRAME - sadece devam et
                return None

            if command_upper.startswith("FOR"):
                # FOR EACH var IN collection kontrolu
                for_each_match = re.match(r"FOR\s+EACH\s+(\w+)\s+IN\s+(.+)", command, re.IGNORECASE)
                if for_each_match:
                    var_name, collection_expr = for_each_match.groups()
                    collection = self.evaluate_expression(collection_expr, scope_name)
                    
                    # Collection'ı list'e çevir
                    if isinstance(collection, dict):
                        items = list(collection.values())
                    elif isinstance(collection, (list, tuple, set)):
                        items = list(collection)
                    elif hasattr(collection, '__iter__') and not isinstance(collection, str):
                        items = list(collection)
                    else:
                        raise Exception(f"FOR EACH: {collection_expr} iterable değil")
                    
                    # İlk elemanı ata
                    if items:
                        self.current_scope()[var_name] = items[0]
                        self.loop_stack.append({
                            "start": self.program_counter + 1,
                            "type": "FOR_EACH",
                            "var": var_name,
                            "items": items,
                            "index": 0
                        })
                    else:
                        # Boş collection - NEXT'e kadar atla
                        depth = 1
                        next_pc = self.program_counter + 1
                        while next_pc < len(self.program) and depth > 0:
                            prog_item = self.program[next_pc]
                            line = prog_item[0] if isinstance(prog_item, tuple) else prog_item
                            line_upper = line.strip().upper()
                            if line_upper.startswith("FOR"):
                                depth += 1
                            elif line_upper.startswith("NEXT"):
                                depth -= 1
                            next_pc += 1
                        return next_pc - 1
                    return None
                
                # Normal FOR döngüsü
                match = re.match(r"FOR\s+(\w+)\s*=\s*(.+?)\s+TO\s+(.+?)(?:\s+STEP\s+(.+?))?$", command, re.IGNORECASE)
                if match:
                    var_name, start_expr, end_expr, step_expr = match.groups()
                    start = self.evaluate_expression(start_expr, scope_name)
                    end = self.evaluate_expression(end_expr, scope_name)
                    step = self.evaluate_expression(step_expr, scope_name) if step_expr else 1
                    self.current_scope()[var_name] = start
                    self.loop_stack.append({
                        "start": self.program_counter + 1,  # Bir sonraki satira isaret et
                        "type": "FOR",
                        "var": var_name,
                        "end": end,
                        "step": step
                    })
                    return None
                else:
                    raise Exception("FOR komutunda sozdizimi hatasi")

            if command_upper.startswith("EXIT FOR"):
                if self.loop_stack and self.loop_stack[-1]["type"] == "FOR":
                    while self.program_counter < len(self.program):
                        prog_item = self.program[self.program_counter]
                        line = prog_item[0] if isinstance(prog_item, tuple) else prog_item
                        if line.upper().strip() == "NEXT":
                            break
                        self.program_counter += 1
                    self.loop_stack.pop()
                    return None
                else:
                    raise Exception("EXIT FOR icin eslesen FOR bulunamadi")

            if command_upper.startswith("CONTINUE FOR"):
                if self.loop_stack and self.loop_stack[-1]["type"] == "FOR":
                    loop_info = self.loop_stack[-1]
                    var_name = loop_info["var"]
                    current_value = self.current_scope()[var_name]
                    current_value += loop_info["step"]
                    self.current_scope()[var_name] = current_value
                    return loop_info["start"]
                else:
                    raise Exception("CONTINUE FOR icin eslesen FOR bulunamadi")

            if command_upper.startswith("NEXT"):
                if self.loop_stack and self.loop_stack[-1]["type"] == "FOR":
                    loop_info = self.loop_stack[-1]
                    var_name = loop_info["var"]
                    current_value = self.current_scope()[var_name]
                    # Degiskeni artir
                    current_value += loop_info["step"]
                    self.current_scope()[var_name] = current_value
                    
                    # Dongu devam etsin mi kontrol et
                    if (loop_info["step"] > 0 and current_value <= loop_info["end"]) or \
                       (loop_info["step"] < 0 and current_value >= loop_info["end"]):
                        # Dongu basina don (FOR satirindan sonraki ilk satira)
                        return loop_info["start"]
                    else:
                        # Dongu bitti
                        self.loop_stack.pop()
                    return None
                elif self.loop_stack and self.loop_stack[-1]["type"] == "FOR_EACH":
                    loop_info = self.loop_stack[-1]
                    var_name = loop_info["var"]
                    items = loop_info["items"]
                    current_index = loop_info["index"]
                    
                    # Sonraki elemana geç
                    current_index += 1
                    
                    if current_index < len(items):
                        # Sonraki elemanı ata
                        self.current_scope()[var_name] = items[current_index]
                        loop_info["index"] = current_index
                        # Döngü başına dön
                        return loop_info["start"]
                    else:
                        # Döngü bitti
                        self.loop_stack.pop()
                    return None
                else:
                    raise Exception("NEXT icin eslesen FOR bulunamadi")

            if command_upper.startswith("WHILE"):
                match = re.match(r"WHILE\s+(.+)", command, re.IGNORECASE)
                if match:
                    condition = match.group(1)
                    self.loop_stack.append({
                        "start": self.program_counter,
                        "type": "WHILE",
                        "condition": condition
                    })
                    if not self.evaluate_expression(condition, scope_name):
                        # WEND'e guvenli atlama
                        while self.program_counter < len(self.program):
                            prog_item = self.program[self.program_counter]
                            line = prog_item[0] if isinstance(prog_item, tuple) else prog_item
                            if line.strip().upper() == "WEND":
                                break
                            self.program_counter += 1
                    return None
                else:
                    raise Exception("WHILE komutunda sozdizimi hatasi")

            if command_upper == "WEND":
                if self.loop_stack and self.loop_stack[-1]["type"] == "WHILE":
                    loop_info = self.loop_stack[-1]
                    if self.evaluate_expression(loop_info["condition"], scope_name):
                        return loop_info["start"]
                    else:
                        self.loop_stack.pop()
                    return None
                else:
                    raise Exception("WEND icin eslesen WHILE bulunamadi")

            if command_upper.startswith("DO"):
                match = re.match(r"DO\s+(WHILE|UNTIL)?\s*(.+)?", command, re.IGNORECASE)
                if match:
                    loop_type, condition = match.groups()
                    self.loop_stack.append({
                        "start": self.program_counter,
                        "type": loop_type or "NONE",
                        "condition": condition or "True"
                    })
                    return None
                else:
                    raise Exception("DO komutunda sozdizimi hatasi")

            if command_upper.startswith("EXIT DO"):
                if self.loop_stack and self.loop_stack[-1]["type"] in ("WHILE", "UNTIL", "NONE"):
                    # LOOP satirina guvenli atlama
                    while self.program_counter < len(self.program):
                        prog_item = self.program[self.program_counter]
                        line = prog_item[0] if isinstance(prog_item, tuple) else prog_item
                        if line.strip().upper() == "LOOP":
                            break
                        self.program_counter += 1
                    self.loop_stack.pop()
                    return None
                else:
                    raise Exception("EXIT DO icin eslesen DO bulunamadi")
            if command_upper.startswith("CONTINUE DO"):
                if self.loop_stack and self.loop_stack[-1]["type"] in ("WHILE", "UNTIL", "NONE"):
                    return self.loop_stack[-1]["start"]
                else:
                    raise Exception("CONTINUE DO icin eslesen DO bulunamadi")

            if command_upper.startswith("LOOP"):
                if self.loop_stack and self.loop_stack[-1]["type"] in ("WHILE", "UNTIL", "NONE"):
                    loop_info = self.loop_stack[-1]
                    condition = loop_info["condition"]
                    if loop_info["type"] == "WHILE" and not self.evaluate_expression(condition, scope_name):
                        self.loop_stack.pop()
                    elif loop_info["type"] == "UNTIL" and self.evaluate_expression(condition, scope_name):
                        self.loop_stack.pop()
                    elif loop_info["type"] == "NONE":
                        return loop_info["start"]
                    return None
                else:
                    raise Exception("LOOP icin eslesen DO bulunamadi")

            if command_upper.startswith("GOTO"):
                match = re.match(r"GOTO\s+(\w+)", command, re.IGNORECASE)
                if match:
                    label = match.group(1)
                    if label in self.labels:
                        return self.labels[label]
                    else:
                        raise Exception(f"Etiket bulunamadi: {label}")
                else:
                    raise Exception("GOTO komutunda sozdizimi hatasi")

            if command_upper.startswith("GOSUB"):
                match = re.match(r"GOSUB\s+(\w+)", command, re.IGNORECASE)
                if match:
                    label = match.group(1)
                    if label in self.labels:
                        self.call_stack.append(self.program_counter + 1)
                        return self.labels[label]
                    else:
                        raise Exception(f"Etiket bulunamadi: {label}")
                else:
                    raise Exception("GOSUB komutunda sozdizimi hatasi")

            if command_upper == "RETURN":
                if self.call_stack:
                    return self.call_stack.pop()
                else:
                    raise Exception("RETURN icin eslesen GOSUB bulunamadi")

            if command_upper.startswith("TRY"):
                match = re.match(r"TRY\s+(.+)\s+CATCH\s+(\w+)\s+DO\s+(.+)", command, re.IGNORECASE)
                if match:
                    try_block, error_var, catch_block = match.groups()
                    try:
                        self.execute_command(try_block, scope_name)
                    except Exception as e:
                        self.current_scope()[error_var] = str(e)
                        self.execute_command(catch_block, scope_name)
                    return None
                else:
                    raise Exception("TRY...CATCH komutunda sozdizimi hatasi")

            if command_upper == "DEBUG ON":
                self.debug_mode = True
                return None
            if command_upper == "DEBUG OFF":
                self.debug_mode = False
                return None
            if command_upper == "TRACE ON":
                self.trace_mode = True
                return None
            if command_upper == "TRACE OFF":
                self.trace_mode = False
                return None
            if command_upper == "STEP DEBUG":
                self.debug_mode = True
                input(f"Satir {self.program_counter + 1}: {command}\nDevam icin Enter...")
                return None

            if command_upper.startswith("PERFORMANCE"):
                try:
                    import psutil
                    process = psutil.Process()
                    memory = process.memory_info().rss / 1024 / 1024
                    cpu = psutil.cpu_percent()
                    elapsed = time.time() - self.performance_metrics["start_time"]
                    print(f"Performans: Bellek: {memory:.2f} MB, CPU: {cpu:.2f}%, Sure: {elapsed:.2f}s")
                except Exception as e:
                    print(f"error occurred: {str(e)}")
                return None

            if command_upper.startswith("SET LANGUAGE"):
                match = re.match(r"SET LANGUAGE\s+(\w+)", command, re.IGNORECASE)
                if match:
                    lang = match.group(1).lower()
                    if lang in self.translations:
                        self.language = lang
                    else:
                        raise Exception(f"Desteklenmeyen dil: {lang}")
                    return None
                else:
                    raise Exception("SET LANGUAGE komutunda sozdizimi hatasi")

            if command_upper.startswith("CALL"):
                if command_upper.startswith("CALL API::GET"):
                    match = re.match(r'CALL API::GET\s+"([^"]+)"\s*,?\s*(.*)', command, re.IGNORECASE)
                    if match:
                        url = match.group(1)
                        params_str = match.group(2).strip()
                        params = None
                        if params_str:
                            try:
                                params = json.loads(params_str)
                            except Exception:
                                params = params_str
                        try:
                            import requests
                            resp = requests.get(url, params=params if isinstance(params, dict) else None)
                            try:
                                result = resp.json()
                            except Exception:
                                result = resp.text
                            print(result)
                            return result
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return ""
                elif command_upper.startswith("CALL API::POST"):
                    match = re.match(r'CALL API::POST\s+"([^"]+)"\s*,?\s*(.*)', command, re.IGNORECASE)
                    if match:
                        url = match.group(1)
                        data_str = match.group(2).strip()
                        data = None
                        if data_str:
                            try:
                                data = json.loads(data_str)
                            except Exception:
                                data = data_str
                        try:
                            import requests
                            resp = requests.post(url, json=data if isinstance(data, dict) else None, data=None if isinstance(data, dict) else data)
                            try:
                                result = resp.json()
                            except Exception:
                                result = resp.text
                            print(result)
                            return result
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return ""
                elif command_upper.startswith("CALL API::PUT"):
                    match = re.match(r'CALL API::PUT\s+"([^"]+)"\s*,?\s*(.*)', command, re.IGNORECASE)
                    if match:
                        url = match.group(1)
                        data_str = match.group(2).strip()
                        data = None
                        if data_str:
                            try:
                                data = json.loads(data_str)
                            except Exception:
                                data = data_str
                        try:
                            import requests
                            resp = requests.put(url, json=data if isinstance(data, dict) else None, data=None if isinstance(data, dict) else data)
                            try:
                                result = resp.json()
                            except Exception:
                                result = resp.text
                            print(result)
                            return result
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return ""
                elif command_upper.startswith("CALL API::DELETE"):
                    match = re.match(r'CALL API::DELETE\s+"([^"]+)"', command, re.IGNORECASE)
                    if match:
                        url = match.group(1)
                        try:
                            import requests
                            resp = requests.delete(url)
                            try:
                                result = resp.json()
                            except Exception:
                                result = resp.text
                            print(result)
                            return result
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return ""
                elif command_upper.startswith("HTTP_DOWNLOAD"):
                    match = re.match(r'HTTP_DOWNLOAD\s+"([^"]+)"\s*,\s*"([^"]+)"', command, re.IGNORECASE)
                    if match:
                        url, path = match.groups()
                        try:
                            import requests
                            resp = requests.get(url)
                            with open(path, "wb") as f:
                                f.write(resp.content)
                            print(f"Dosya indirildi: {path}")
                            return path
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return ""
                elif command_upper.startswith("HTTP_STATUS"):
                    match = re.match(r'HTTP_STATUS\s+"([^"]+)"', command, re.IGNORECASE)
                    if match:
                        url = match.group(1)
                        try:
                            import requests
                            resp = requests.get(url)
                            print(resp.status_code)
                            return resp.status_code
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                            return 0
                elif command_upper.startswith("HTTP_SET_HEADER"):
                    match = re.match(r'HTTP_SET_HEADER\s+"([^"]+)"\s*,\s*"([^"]+)"', command, re.IGNORECASE)
                    if match:
                        key, value = match.groups()
                        if not hasattr(self, "_http_headers"):
                            self._http_headers = {}
                        self._http_headers[key] = value
                        print(f"Header ayarlandi: {key}={value}")
                        return self._http_headers
                elif command_upper.startswith("HTTP_SESSION_START"):
                    try:
                        import requests
                        self._http_session = requests.Session()
                        print("HTTP oturumu baslatildi.")
                    except Exception as e:
                        print(f"error occurred: {str(e)}")
                    return None
                elif command_upper.startswith("HTTP_SESSION_END"):
                    if hasattr(self, "_http_session"):
                        self._http_session.close()
                        del self._http_session
                        print("HTTP oturumu kapatildi.")
                    return None
                # ...diger CALL komutlari ve DLL cagrisi...
                elif command_upper.startswith("CALL"):
                    # Once user-defined subroutine kontrolu
                    match = re.match(r"CALL\s+(\w+)\s*\(([^)]*)\)", command, re.IGNORECASE)
                    if match:
                        sub_name, args_str = match.groups()
                        if sub_name in self.user_subs:
                            self.call_user_sub(sub_name, args_str, scope_name)
                            return None
                    
                    # Basit CALL (argumansiz)
                    match = re.match(r"CALL\s+(\w+)", command, re.IGNORECASE)
                    if match:
                        sub_name = match.group(1)
                        if sub_name in self.user_subs:
                            self.call_user_sub(sub_name, "", scope_name)
                            return None
                    
                    # DLL fonksiyon cagrisi
                    match = re.match(r"CALL\s+(\w+)::(\w+)\((.*)\)", command, re.IGNORECASE)
                    if match:
                        dll_name, func_name, args = match.groups()
                        dll = self.core.load_dll(dll_name)
                        func = getattr(dll, func_name)
                        arg_list = [self.evaluate_expression(arg.strip(), scope_name) for arg in args.split(",") if arg.strip()]
                        result = func(*arg_list)
                        print(result)
                        return result
                raise Exception("CALL komutunda sozdizimi hatasi")

            if command_upper.startswith("HELP"):
                match = re.match(r"HELP\s*(\w+)?", command, re.IGNORECASE)
                if match:
                    lib_name = match.group(1)
                    self.show_help(lib_name)
                    return None
                else:
                    raise Exception("HELP komutunda sozdizimi hatasi")

            if command_upper.startswith("CORE."):
                func_name = command_upper.split(".")[1]
                args = re.match(r"CORE\.(\w+)\((.*)\)", command, re.IGNORECASE)
                if args:
                    _, arg_str = args.groups()
                    arg_list = [self.evaluate_expression(arg.strip(), scope_name) for arg in arg_str.split(",") if arg.strip()]
                    return getattr(self.core, func_name.lower())(*arg_list)
                else:
                    return getattr(self.core, func_name.lower())()

            # END komutu kontrolu
            if command_upper == "END":
                self.running = False
                return None

            raise Exception(f"Bilinmeyen komut: {command}")

        except Exception as e:
            logging.error(f"Hata: {str(e)}\n{''.join(traceback.format_stack())}")
            if self.error_handler:
                return self.error_handler
            elif self.gosub_handler:
                return self.gosub_handler
            else:
                raise e

    def repl(self):
        self.repl_mode = True
        print("pdsXv11 REPL - Cok satirli komut icin 'REPL END' yazip Enter'a basin, cikis icin 'EXIT'")
        buffer = []
        REPL_STIRNO = 0
        while True:
            try:
                line = input("[PDS-X] ")
                if line.upper() == "EXIT":
                    break
                if line.upper() == "REPL END":
                    cmd = "\n".join(buffer)
                    buffer = []
                    if cmd.strip():
                        try:
                            self.execute_command(cmd)
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                    continue
                buffer.append(line)
            except Exception as e:
                print(f"error occurred: {str(e)}")
        self.repl_mode = False

    def compile_to_bytecode(self, code):
        self.bytecode = []
        lines = code.split("\n")
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            tokens = line.split(maxsplit=1)
            opcode = tokens[0].upper()
            operands = tokens[1] if len(tokens) > 1 else ""
            self.bytecode.append({"opcode": opcode, "operands": operands, "line": i + 1})
        return self.bytecode

    def execute_bytecode(self):
        self.running = True
        pc = 0
        while self.running and pc < len(self.bytecode):
            instruction = self.bytecode[pc]
            opcode = instruction["opcode"]
            operands = instruction["operands"]
            try:
                if opcode == "PRINT":
                    print(self.evaluate_expression(operands))
                elif opcode == "LET":
                    var, val = operands.split("=", 1)
                    self.current_scope()[var.strip()] = self.evaluate_expression(val.strip())
                elif opcode == "DIM":
                    var_name, var_type = operands.split("AS")
                    self.current_scope()[var_name.strip()] = self.type_table.get(var_type.strip().upper(), object)()
                elif opcode == "IF":
                    condition, then_cmd = operands.split("THEN")
                    if self.evaluate_expression(condition.strip()):
                        self.execute_command(then_cmd.strip())
                elif opcode == "GOTO":
                    label = operands.strip()
                    for i, instr in enumerate(self.bytecode):
                        if instr["opcode"] == "LABEL" and instr["operands"] == label:
                            pc = i
                            break
                pc += 1
            except Exception as e:
                logging.error(f"Bayt kodu hatasi: Satir {instruction['line']}, {str(e)}")
                if self.error_handler:
                    pc = self.error_handler
                else:
                    raise e
        self.running = False

    def run(self, code):
        """Kodu calistir"""
        try:
            self.parse_program(code)
            self.running = True
            self.program_counter = 0
            
            while self.running and self.program_counter < len(self.program):
                prog_item = self.program[self.program_counter]
                if isinstance(prog_item, tuple):
                    command, scope = prog_item
                else:
                    command = prog_item
                    scope = None
                
                if self.debug_mode:
                    print(f"DEBUG: Satir {self.program_counter + 1}: {command}")
                    input("Devam etmek icin Enter tusuna basin...")
                
                next_pc = self.execute_command(command, scope)
                if next_pc is not None:
                    self.program_counter = next_pc
                else:
                    self.program_counter += 1
                    
        except Exception as e:
            logging.error(f"Program calistirma hatasi: {str(e)}")
            print(f"error occurred: {str(e)}")
            if self.debug_mode:
                traceback.print_exc()
        finally:
            self.running = False

    def show_help(self, command):
        """Yardim goster"""
        try:
            # JSON help dosyasini oku
            import json
            help_file = Path(__file__).parent / "pdsxv11_help.json"
            
            if not help_file.exists():
                print("Yardim dosyasi bulunamadi: pdsxv11_help.json")
                self._show_basic_help()
                return
                
            with open(help_file, 'r', encoding='utf-8') as f:
                help_data = json.load(f)
            
            # Komut parametresini parse et
            parts = command.split()
            if len(parts) == 1:  # Sadece HELP
                self._show_full_help(help_data)
            elif len(parts) == 2:  # HELP <komut>
                command_name = parts[1].upper()
                self._show_command_help(help_data, command_name)
            else:
                print("Kullanim: HELP veya HELP <komut_adi>")
                
        except Exception as e:
            print(f"error occurred: {str(e)}")
            self._show_basic_help()
    
    def _show_full_help(self, help_data):
        """Tum yardim bilgilerini goster"""
        print("=" * 80)
        print(f"{help_data['interpreter_info']['name']} v{help_data['interpreter_info']['version']}")
        print(f"{help_data['interpreter_info']['description']}")
        print("=" * 80)
        
        # Ozellikler
        print("\n🚀 OZELLİKLER:")
        for feature in help_data['interpreter_info']['features']:
            print(f"  • {feature}")
        
        # Komut kategorileri
        print("\n📋 KOMUT KATEGORİLERİ:")
        for category, commands in help_data['commands'].items():
            category_names = {
                'basic_commands': '🔤 Temel Komutlar',
                'control_flow': '🔄 Kontrol Yapilari',
                'program_flow': '➡️ Program Akisi',
                'error_handling': '❌ Hata Yonetimi',
                'file_operations': '📁 Dosya İslemleri',
                'database_operations': '🗄️ Veritabani İslemleri',
                'debug_commands': '🐛 Debug Komutlari',
                'memory_commands': '💾 Bellek Yonetimi',
                'import_commands': '📦 Modul İslemleri',
                'special_commands': '⚙️ Ozel Komutlar'
            }
            print(f"  {category_names.get(category, category.title())}:")
            for cmd in commands.keys():
                print(f"    - {cmd}")
        
        # Fonksiyon kategorileri
        print("\n🔧 FONKSİYON KATEGORİLERİ:")
        for category, functions in help_data['functions'].items():
            category_names = {
                'string_functions': '📝 String Fonksiyonlari',
                'math_functions': '🧮 Matematik Fonksiyonlari',
                'array_functions': '📊 Dizi Fonksiyonlari',
                'date_time_functions': '⏰ Tarih/Saat Fonksiyonlari',
                'file_functions': '📄 Dosya Fonksiyonlari',
                'pdf_functions': '📕 PDF Fonksiyonlari',
                'web_functions': '🌐 Web Fonksiyonlari',
                'system_functions': '⚙️ Sistem Fonksiyonlari'
            }
            print(f"  {category_names.get(category, category.title())}:")
            for func in functions.keys():
                print(f"    - {func}")
        
        # CLI kullanimi
        print("\n💻 KOMUT SATIRI KULLANIMI:")
        print(f"  {help_data['cli_options']['basic_usage']}")
        for option, desc in help_data['cli_options']['options'].items():
            print(f"  {option:<20} : {desc}")
        
        print("\n📖 Ozel komut yardimi icin: HELP <komut_adi>")
        print("💡 Ornek programlar icin: HELP EXAMPLES")
        print("=" * 80)
    
    def _show_command_help(self, help_data, command_name):
        """Belirli komut yardimini goster"""
        command_found = False
        
        if command_name == "EXAMPLES":
            self._show_examples(help_data)
            return
        
        # Komutlarda ara
        for category, commands in help_data['commands'].items():
            if command_name in commands:
                cmd_info = commands[command_name]
                print("=" * 60)
                print(f"📋 KOMUT: {command_name}")
                print("=" * 60)
                print(f"Aciklama: {cmd_info['description']}")
                print(f"Syntax: {cmd_info['syntax']}")
                
                if cmd_info.get('parameters'):
                    print("\nParametreler:")
                    for param, desc in cmd_info['parameters'].items():
                        print(f"  • {param}: {desc}")
                
                if cmd_info.get('examples'):
                    print("\nOrnekler:")
                    for example in cmd_info['examples']:
                        print(f"  {example}")
                
                print("=" * 60)
                command_found = True
                break
        
        # Fonksiyonlarda ara
        if not command_found:
            for category, functions in help_data['functions'].items():
                if command_name in functions:
                    func_info = functions[command_name]
                    print("=" * 60)
                    print(f"🔧 FONKSİYON: {command_name}")
                    print("=" * 60)
                    print(f"Aciklama: {func_info['description']}")
                    print(f"Syntax: {func_info['syntax']}")
                    
                    if func_info.get('parameters'):
                        print("\nParametreler:")
                        for param, desc in func_info['parameters'].items():
                            print(f"  • {param}: {desc}")
                    
                    if func_info.get('examples'):
                        print("\nOrnekler:")
                        for example in func_info['examples']:
                            print(f"  {example}")
                    
                    print("=" * 60)
                    command_found = True
                    break
        
        # Operatorlerde ara
        if not command_found:
            for category, operators in help_data['operators'].items():
                if command_name in operators:
                    print("=" * 60)
                    print(f"⚙️ OPERATOR: {command_name}")
                    print("=" * 60)
                    print(f"Kategori: {category.title()}")
                    print(f"Aciklama: {operators[command_name]}")
                    print("=" * 60)
                    command_found = True
                    break
        
        # Veri tiplerinde ara  
        if not command_found:
            if command_name in help_data['data_types']:
                type_info = help_data['data_types'][command_name]
                print("=" * 60)
                print(f"📊 VERİ TİPİ: {command_name}")
                print("=" * 60)
                print(f"Aciklama: {type_info['description']}")
                print(f"Aralik: {type_info['range']}")
                print(f"Ornek: {type_info['example']}")
                print("=" * 60)
                command_found = True
        
        if not command_found:
            print(f"❌ '{command_name}' komutu, fonksiyonu veya operatoru bulunamadi!")
            print("💡 Tum komutlari gormek icin: HELP")
            print("💡 Ornek programlar icin: HELP EXAMPLES")
    
    def _show_examples(self, help_data):
        """Ornek programlari goster"""
        print("=" * 80)
        print("💡 ORNEK PROGRAMLAR")
        print("=" * 80)
        
        for example_name, example_info in help_data['examples'].items():
            print(f"\n📝 {example_info['description']}:")
            print("-" * 40)
            for line in example_info['code']:
                print(f"  {line}")
        
        print("\n" + "=" * 80)
    
    def check_key_state(self, key=None):
        """KEY komutu - Tus basili mi kontrol eder (non-blocking)"""
        if os.name == 'nt' and self.msvcrt:
            if self.msvcrt.kbhit():
                pressed_key = self.msvcrt.getch().decode('utf-8', errors='ignore')
                if key is None:
                    return pressed_key
                else:
                    # Ozel tuslar icin kontrol
                    key = key.upper()
                    if key == '<YUKARIOK>' and ord(pressed_key) == 72:  # Up arrow
                        return True
                    elif key == '<ASAGIOK>' and ord(pressed_key) == 80:  # Down arrow
                        return True
                    elif key == '<SOLOK>' and ord(pressed_key) == 75:  # Left arrow  
                        return True
                    elif key == '<SAGOK>' and ord(pressed_key) == 77:  # Right arrow
                        return True
                    elif key == '<ENTER>' and ord(pressed_key) == 13:
                        return True
                    elif key == '<ESC>' and ord(pressed_key) == 27:
                        return True
                    elif key == '<SPACE>' and ord(pressed_key) == 32:
                        return True
                    elif pressed_key.upper() == key:
                        return True
                return False
            else:
                return False
        else:
            # Linux/Mac icin basit implementasyon
            return input("Press Enter to continue...")[:1] if key is None else False
    
    def get_key_wait(self, keys=None):
        """GETKEY komutu - Belirtilen tuslardan birine basilmasini bekler"""
        if keys is None:
            # Herhangi bir tus bekle
            if os.name == 'nt' and self.msvcrt:
                return self.msvcrt.getch().decode('utf-8', errors='ignore')
            else:
                return input("Press any key...")[:1]
        else:
            # Belirtilen tuslar listesi
            if isinstance(keys, str):
                keys = [keys]
            
            while True:
                if os.name == 'nt' and self.msvcrt:
                    if self.msvcrt.kbhit():
                        key = self.msvcrt.getch().decode('utf-8', errors='ignore')
                        
                        # Ozel tuslari kontrol et
                        for target_key in keys:
                            target_key = target_key.upper()
                            if target_key == '<YUKARIOK>' and ord(key) == 72:
                                return '<YUKARIOK>'
                            elif target_key == '<ASAGIOK>' and ord(key) == 80:
                                return '<ASAGIOK>'
                            elif target_key == '<SOLOK>' and ord(key) == 75:
                                return '<SOLOK>'
                            elif target_key == '<SAGOK>' and ord(key) == 77:
                                return '<SAGOK>'
                            elif key.upper() == target_key:
                                return key
                else:
                    # Linux/Mac fallback
                    key = input(f"Press one of {keys}: ")[:1]
                    if key.upper() in [k.upper() for k in keys]:
                        return key
                
                time.sleep(0.01)  # CPU kullanimini azalt
    
    def save_program(self, filename):
        """SAVE komutu - Mevcut programi dosyaya kaydet"""
        try:
            if not filename.endswith('.pdsx'):
                filename += '.pdsx'
            
            with open(filename, 'w', encoding='utf-8') as f:
                if self.repl_mode and self.repl_buffer:
                    # REPL buffer'indan kaydet
                    for line in self.repl_buffer:
                        f.write(line + '\n')
                else:
                    # Program listesinden kaydet
                    for line in self.program:
                        f.write(line + '\n')
            
            print(f"Program kaydedildi: {filename}")
            return True
        except Exception as e:
            print(f"error occurred: {str(e)}")
            return False
    
    def load_program(self, filename):
        """LOAD komutu - Dosyadan program yukle"""
        try:
            if not filename.endswith('.pdsx'):
                filename += '.pdsx'
            
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.rstrip('\n\r') for line in f.readlines()]
            
            if self.repl_mode:
                self.repl_buffer = lines
            else:
                self.program = lines
                self.program_counter = 0
            
            print(f"Program yuklendi: {filename}")
            return True
        except FileNotFoundError:
            print(f"Dosya bulunamadi: {filename}")
            return False
        except Exception as e:
            print(f"error occurred: {str(e)}")
            return False
    
    def run_program(self, filename):
        """RUN komutu - Dosyadan program yukleyip calistir"""
        if self.load_program(filename):
            if self.repl_mode:
                # REPL buffer'indaki programi calistir
                old_repl = self.repl_mode
                self.repl_mode = False
                old_program = self.program[:]
                self.program = self.repl_buffer[:]
                self.program_counter = 0
                try:
                    # Program zaten yuklendi, parse et
                    self.parse_program('\n'.join(self.program))
                    
                    old_running = self.running
                    self.running = True
                    
                    while self.running and self.program_counter < len(self.program):
                        if isinstance(self.program[self.program_counter], tuple):
                            command, scope = self.program[self.program_counter]
                        else:
                            command = self.program[self.program_counter]
                            scope = None
                        
                        next_pc = self.execute_command(command, scope)
                        if next_pc is not None:
                            self.program_counter = next_pc
                        else:
                            self.program_counter += 1
                    
                    self.running = old_running
                finally:
                    self.repl_mode = old_repl
                    self.program = old_program
            else:
                # Normal program calistirma
                code_str = '\n'.join(self.program)
                self.run(code_str)
            return True
        return False
    
    def start_repl(self):
        """REPL modu baslat"""
        self.repl_mode = True
        self.repl_running = True
        self.repl_buffer = []
        self.repl_line_number = 10
        
        print("pdsXv11g REPL Modu")
        print("Cok satirli mod: REPL ... REPL END")
        print("Kaydetme: SAVE <dosya>")
        print("Yukleme: LOAD <dosya>")
        print("Calistirma: RUN [dosya]")
        print("Liste: LIST")
        print("Cikis: EXIT")
        print()
        
        while self.repl_running:
            try:
                if self.repl_mode:
                    line = input(f"{self.repl_line_number}> ")
                else:
                    line = input("... ")
                
                line = line.strip()
                
                if line.upper() == "EXIT":
                    break
                elif line.upper() == "LIST":
                    self.list_program()
                    continue
                elif line.upper().startswith("EDIT"):
                    self.edit_line(line)
                    continue
                elif line.upper().startswith("DELETE"):
                    self.delete_line(line)
                    continue
                elif line.upper() == "REPL":
                    print("Cok satirli mod basladi. REPL END ile bitirin.")
                    self.repl_mode = False
                    continue
                elif line.upper() == "REPL END":
                    print("Cok satirli mod bitti.")
                    self.repl_mode = True
                    continue
                elif line.upper() == "NEW":
                    self.repl_buffer = []
                    self.repl_line_number = 10
                    print("Program temizlendi.")
                    continue
                elif line.upper() == "RUN":
                    # Mevcut buffer'i calistir
                    if self.repl_buffer:
                        old_program = self.program[:]
                        old_pc = self.program_counter
                        
                        self.program = self.repl_buffer[:]
                        self.program_counter = 0
                        try:
                            # Buffer'i string'e cevir ve parse et
                            code_str = '\n'.join(self.repl_buffer)
                            self.run(code_str)
                        except Exception as e:
                            print(f"error occurred: {str(e)}")
                        finally:
                            self.program = old_program
                            self.program_counter = old_pc
                    else:
                        print("Calistirilacak program yok.")
                    continue
                elif line.upper().startswith("SAVE "):
                    filename = line[5:].strip()
                    self.save_program(filename)
                    continue
                elif line.upper().startswith("LOAD "):
                    filename = line[5:].strip()
                    self.load_program(filename)
                    continue
                elif line.upper().startswith("RUN "):
                    filename = line[4:].strip()
                    self.run_program(filename)
                    continue
                
                if line:
                    if self.repl_mode:
                        # Satir numarali mod
                        self.repl_buffer.append(f"{self.repl_line_number} {line}")
                        self.repl_line_number += 10
                        self.repl_history.append(line)
                    else:
                        # Cok satirli mod
                        self.repl_buffer.append(line)
                
            except KeyboardInterrupt:
                print("\nREPL cikisi yapiliyor...")
                break
            except EOFError:
                print("\nREPL sonlandirildi.")
                break
            except Exception as e:
                print(f"error occurred: {str(e)}")
        
        self.repl_running = False
    
    def list_program(self):
        """LIST komutu - Program listesini goster"""
        if self.repl_buffer:
            print("\nMevcut Program:")
            print("-" * 40)
            for i, line in enumerate(self.repl_buffer):
                print(f"{i+1:3}: {line}")
            print("-" * 40)
        else:
            print("Program bos.")
    
    def edit_line(self, command):
        """EDIT komutu - Satir duzenleme"""
        try:
            parts = command.split(" ", 1)
            if len(parts) < 2:
                print("Kullanim: EDIT <satir_no>")
                return
            
            line_no = int(parts[1]) - 1
            if 0 <= line_no < len(self.repl_buffer):
                print(f"Mevcut: {self.repl_buffer[line_no]}")
                new_line = input("Yeni: ")
                if new_line.strip():
                    self.repl_buffer[line_no] = new_line
                    print("Satir guncellendi.")
            else:
                print("Gecersiz satir numarasi.")
        except ValueError:
            print("Gecersiz satir numarasi.")
        except Exception as e:
            print(f"error occurred: {str(e)}")
    
    def delete_line(self, command):
        """DELETE komutu - Satir silme"""
        try:
            parts = command.split(" ", 1)
            if len(parts) < 2:
                print("Kullanim: DELETE <satir_no>")
                return
            
            line_no = int(parts[1]) - 1
            if 0 <= line_no < len(self.repl_buffer):
                deleted = self.repl_buffer.pop(line_no)
                print(f"Silindi: {deleted}")
            else:
                print("Gecersiz satir numarasi.")
        except ValueError:
            print("Gecersiz satir numarasi.")
        except Exception as e:
            print(f"error occurred: {str(e)}")
    
    def _show_basic_help(self):
        """Temel yardim (JSON dosyasi yoksa)"""
        print("pdsXv11 Yorumlayicisi - Yardim")
        print("==============================")
        print("Temel komutlar:")
        print("  PRINT <ifade>     - Ekrana yazdir")
        print("  LET <var> = <val> - Degiskene deger ata")
        print("  INPUT <prompt>, <var> - Kullanicidan veri al")
        print("  IF <kosul> THEN <komut> - Kosullu calistir")
        print("  FOR/WHILE/DO donguleri")
        print("  HELP <komut>      - Belirli komut yardimi")
        print("  CLS               - Ekrani temizle")
        print("  EXIT              - Cikis")

# Bu kod blogu, sanal ortam kurulduktan sonra calisacak
if __name__ == "__main__":
    main()