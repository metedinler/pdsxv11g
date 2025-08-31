# 1. pdsXv11g - Modern BASIC Yorumlayıcısı Kullanım Kılavuzu

## 1.1. 🎯 pdsXv11g Nedir ve Ne İşe Yarar?

**pdsXv11g**, modern Python teknolojileri ile geliştirilmiş, gelişmiş bir BASIC yorumlayıcısıdır. Geleneksel BASIC programlamanın basitliğini koruyarak, günümüzün gereksinimlerine uygun gelişmiş özellikler sunar.

### 1.1.1. Kullanıcılar Ne Yapabilir?

**Veri Analizi ve Bilim**: DataFrame'ler, matris işlemleri, istatistiksel fonksiyonlar ile bilimsel hesaplamalar yapabilirsiniz. CSV, JSON verilerini işleyebilir, pivot tablolar oluşturabilirsiniz.

**Oyun Geliştirme**: Gerçek zamanlı klavye kontrolü, ASCII grafikleri, konsol tabanlı oyunlar geliştirebilirsiniz. Skor sistemleri, animasyonlar oluşturabilirsiniz.

**Sistem Yönetimi**: Dosya işlemleri, ağ bağlantıları, sistem performansı izleme, yapılandırma yönetimi yapabilirsiniz.

**Eğitim ve Öğrenim**: Algoritma öğrenimi, veri yapıları, matematiksel hesaplamalar için ideal bir platformdur.

**İş Uygulamaları**: Rapor üretimi, veri işleme hatları, basit veritabanı işlemleri gerçekleştirebilirsiniz.

### 1.1.2. Temel Mimari Özellikler

**Asenkron İşlemler**: SLEEP, WAIT, ASYNC_WAIT komutları ile programın belirli kısımlarında bekleme yapabilir, çok iş parçacıklı uygulamalar simüle edebilirsiniz.

**Recursive (Özyinelemeli) Fonksiyonlar**: Tüm fonksiyonlar kendi kendilerini çağırabilir. Fibonacci, faktöriyel gibi matematiksel problemlerde özyineleme kullanabilirsiniz.

**Parametreli Komutlar ve Fonksiyonlar**: Her komut ve fonksiyon parametre alabilir. PRINT("Mesaj", değer), SLEEP(5), FOR I = 1 TO sayı gibi esnek kullanım sağlar.

**Modüler Yapı**: IMPORT komutu ile harici dosyalar ve kütüphaneler yüklenebilir. Kodunuzu farklı dosyalarda organize edebilirsiniz.

**Hata Yönetimi**: TRY-CATCH blokları ile profesyonel hata yakalama, THROW ile özel hata fırlatma imkânı.

**Bellek Yönetimi**: Otomatik çöp toplama (garbage collection) ile bellek yönetimi, MEMORY_USAGE() ile anlık bellek kullanım takibi.

## 1.2. 📚 Giriş: pdsXv11g Nedir?

pdsXv11g, klasik BASIC dilinin basitliğini ve öğrenme kolaylığını, modern programlama dillerinin gücü ve esnekliğiyle birleştiren gelişmiş bir yorumlayıcıdır. Python üzerinde çalışan bu motor, hem programlamaya yeni başlayanlar için harika bir başlangıç noktası sunar hem de deneyimli geliştiricilerin veri analizi, oyun geliştirme ve otomasyon gibi karmaşık görevleri yerine getirmesine olanak tanır.

Kullanıcılar pdsXv11g ile şunları yapabilir:
- **Etkileşimli Kodlama**: REPL (Read-Eval-Print-Loop) modu sayesinde komutları anında yazıp sonuçlarını görebilirler.
- **Veri Analizi**: `DATAFRAME` veri yapısı ve Pandas entegrasyonu ile CSV/JSON dosyalarını işleyebilir, istatistiksel analizler yapabilirler.
- **Oyun Geliştirme**: Gerçek zamanlı klavye kontrolü ve konsol grafikleri ile basit 2D oyunlar ve arayüzler tasarlayabilirler.
- **Modern Programlama**: `STRUCT`, `ENUM`, `TRY-CATCH` hata yakalama ve `FUNC` gibi modern yapılarla daha organize ve sağlam kodlar yazabilirler.
- **Otomasyon**: Dosya sistemi işlemleri, web istekleri ve sistem komutları ile otomasyon betikleri oluşturabilirler.

### 🏛️ Temel Mimari ve Programlama Özellikleri

pdsXv11g'nin temel çalışma prensipleri ve mimarisi, onu güçlü kılan özelliklerdir:

- **Yorumlayıcı (Interpreter)**: Kodlar satır satır okunur, derlenir ve çalıştırılır. Bu, hızlı geliştirme vae hata ayıklama süreçleri sağlar.
- **Parametre Aktarımı**: Fonksiyonlara ve komutlara parametreler değer ile aktarılır (pass-by-value). Bu, fonksiyon içindeki değişikliklerin orijinal değişkeni etkilememesini sağlar. Ancak `LIST`, `DICT`, `ARRAY` gibi koleksiyon tipleri referans ile aktarılır, bu da bellek verimliliği sağlar.
- **Özyinelemeli (Recursive) Fonksiyonlar**: Bir fonksiyonun kendi kendini çağırması desteklenir. Bu, özellikle ağaç yapılarında gezinme veya Fibonacci serisi gibi algoritmalar için güçlü bir tekniktir.
- **Asenkron İşlemler**: `ASYNC_WAIT`, `SLEEP`, `WAIT` gibi komutlar, programın belirli bir süre beklemesini veya diğer işlemlerin devam etmesine izin vererek zaman uyumsuz görevlerin yönetilmesini sağlar. Bu, özellikle ağ istekleri veya uzun süren işlemlerde programın "donmasını" engeller.
- **Genişletilebilir Modül Sistemi**: `IMPORT` komutu ile `.basx` veya `.libx` uzantılı kütüphane dosyalarını projenize dahil edebilir, kodunuzu modüler hale getirebilirsiniz.

---

## 1.4. 🚀 pdsXv11g'nin Yeni ve Gelişmiş Özellikleri (v1.1.0)

Bu sürüm, pdsXv11g'yi tam teşekküllü bir programlama aracına dönüştüren birçok yenilik içermektedir.

### ✨ Tamamen Yeni Özellikler:
1. **FOR EACH IN döngüleri** - Array ve koleksiyonlarda modern iterasyon.
2. **FUNC...END FUNC** - Lambda benzeri, daha esnek fonksiyon tanımlama.
3. **String Array Desteği** - Metin verilerini dizilerde verimli bir şekilde saklama ve işleme.
4. **İç İçe STRUCT/UNION** - `person.address.city` gibi karmaşık ve iç içe geçmiş veri yapıları oluşturma.
5. **ENUM Blok Yapısı** - `ENUM Colors...END ENUM` ile okunabilir sabitler tanımlama.
6. **DATAFRAME Blok Yapısı** - `DATAFRAME sales...END DATAFRAME` ile tablo verilerini doğrudan kod içinde tanımlama.
7. **Matris Operasyonları** - `TRANSPOSE`, `INV`, `DIAG` gibi lineer cebir fonksiyonları.
8. **Gelişmiş DataFrame İşlemleri** - `GROUPBY`, `PIVOT_TABLE` ile güçlü veri analizi.
9. **String Array Fonksiyonları** - Metin dizileri üzerinde toplu işlemler için 20'den fazla özel fonksiyon.
10. **END Komutu** - Programı herhangi bir noktada güvenli bir şekilde sonlandırma.
11. **Exception Handling** - `TRY-CATCH` blokları ile modern hata yakalama ve yönetimi.
12. **Async/Threading Desteği** - `PERFORMANCE`, `TIMER`, `SLEEP` gibi komutlarla asenkron işlemler ve performans izleme.

### 🔧 Geliştirilmiş Özellikler:
- Çok boyutlu diziler için (`DIM matrix(10,10,10)`) daha sağlam ve hızlı destek.
- İç içe `STRUCT` ve `UNION` alanlarının otomatik olarak başlatılması.
- NumPy ve Pandas kütüphaneleri ile tam entegrasyon sayesinde yüksek performanslı bilimsel ve veri işlemleri.
- Daha açıklayıcı hata mesajları ve geliştirilmiş hata ayıklama (`DEBUG`, `TRACE`) araçları.

---

## � İçindekiler

### 1. Giriş ve Kurulum
   1.1. [pdsXv11g Nedir ve Ne İşe Yarar?](#-pdsxv11g-nedir-ve-ne-işe-yarar)
   1.2. [Temel Mimari ve Programlama Özellikleri](#temel-mimari-özellikler)
   1.3. [pdsXv11g'nin Yeni ve Gelişmiş Özellikleri](#pdsxv11gnin-yeni-ve-gelişmiş-özellikleri-v110)
   1.4. [Kurulum ve Başlatma](#-kurulum-ve-başlatma)
   1.5. [Çalıştırma Modları](#çalıştırma-modları)

### 2. Temel Programlama Konseptleri
   2.1. [Temel Komutlar ve Syntax](#-temel-komutlar-ve-syntax)
   2.2. [PRINT - Ekrana Yazdırma](#print---ekrana-yazdırma)
   2.3. [INPUT - Kullanıcıdan Veri Alma](#input---kullanıcıdan-veri-alma)
   2.4. [END - Program Sonlandırma](#end---program-sonlandırma-yeni-özellik---pdsxv11g)
   2.5. [REM - Yorum Satırları](#rem---yorum-satırları)
   2.6. [HELP - Yardım Sistemi](#help---yardım-sistemi)

### 3. Veri Tipleri ve Değişkenler
   3.1. [Temel Veri Tipleri](#temel-tipler)
   3.2. [Koleksiyon Tipleri](#koleksiyon-tipleri)
   3.3. [İleri Seviye Tipler (STRUCT, UNION, ENUM)](#ileri-tipler)
   3.4. [Değişken Tanımlama ve Atama](#değişkenler-ve-atama)

### 4. Kontrol Yapıları ve Döngüler
   4.1. [IF-THEN-ELSE Yapıları](#if-then-else)
   4.2. [SELECT CASE - Gelişmiş Koşullu Yapı](#select-case---gelişmiş-koşullu-yapı)
   4.3. [FOR-NEXT Döngüsü](#for-next-döngüsü)
   4.4. [FOR EACH IN Döngüsü](#for-each-in-döngüsü-yeni-özellik---pdsxv11g)
   4.5. [WHILE-WEND ve DO-LOOP](#while-wend-döngüsü)
   4.6. [Döngü Kontrolü (EXIT, CONTINUE)](#döngü-kontrol-komutları)

### 5. Fonksiyonlar ve Alt Programlar
   5.1. [Kullanıcı Tanımlı Fonksiyonlar](#user-defined-fonksiyonlar)
   5.2. [DEF FN, DEF FUNCTION, FUNC](#def-fn-def-function-func)
   5.3. [Alt Programlar (DEF SUB)](#def-sub---alt-programlar)

### 6. Dahili Fonksiyonlar (Built-in Functions)
   6.1. [String Fonksiyonları](#string-fonksiyonları)
   6.2. [Matematik Fonksiyonları](#matematik-fonksiyonları)
   6.3. [İstatistiksel Fonksiyonlar](#istatistiksel-fonksiyonlar)
   6.4. [NumPy Dizi İşlemleri](#numpy-array-işlemleri-geliştirilmiş---pdsxv11g)
   6.5. [Pandas DataFrame İşlemleri](#pandas-dataframe-işlemleri-geliştirilmiş---pdsxv11g)
   6.6. [String Array Fonksiyonları (20 Fonksiyon)](#string-array-functions---gelişmiş-string-array-işlemleri-yeni---pdsxv11g)

### 7. İleri Seviye Veri Yapıları
   7.1. [STRUCT (Yapılar)](#struct-tanımlama-geliştirilmiş---pdsxv11g)
   7.2. [UNION (Birleşimler)](#union-tanımlama-geliştirilmiş---pdsxv11g)
   7.3. [ENUM (Sabit Grupları)](#enum-simülasyonu-geliştirilmiş---pdsxv11g)

### 8. Hata Yönetimi ve Debugging
   8.1. [TRY-CATCH Blokları](#traditional-try-catch-yeni)
   8.2. [THROW ile Özel Hata Fırlatma](#custom-error-throwing-yeni)
   8.3. [ON ERROR GOTO ile Klasik Hata Yönetimi](#error-handling-with-goto)

### 9. Dosya ve Sistem İşlemleri
   9.1. [Temel Dosya İşlemleri](#dosya-işlemleri)
   9.2. [Ağ ve Web İşlemleri](#web-işlemleri)
   9.3. [Modül Sistemi](#-modül-sistemi)

### 10. REPL ve Etkileşimli Programlama
   10.1. [REPL Modu](#-repl-ve-etkileşimli-mod)
   10.2. [Klavye Girişi ve Kontrolü](#-klavye-girişi)

### 11. Performans ve Sistem İzleme
   11.1. [Performance Monitoring](#performance-i̇zleme)
   11.2. [Asenkron İşlemler](#async-i̇şlemler-geliştirilmiş---pdsxv11g)

### 12. Referanslar ve Yardımcı Bilgiler
   12.1. [Operatörler](#-operatörler)
   12.2. [Komut Satırı Seçenekleri](#-komut-satırı-seçenekleri)
   12.3. [İpuçları ve En İyi Uygulamalar](#-i̇puçları-ve-en-i̇yi-uygulamalar)
   12.4. [Hata Mesajları ve Anlamları](#-hata-mesajları-ve-anlamları)

### 13. Örnek Programlar ve Uygulamalar
   13.1. [Temel Program Örnekleri](#-örnekler)
   13.2. [Oyun Örnekleri](#-oyun-geliştirme-i̇çin-i̇puçları)
   13.3. [Veri Analizi Örnekleri](#örnek-3-veri-analizi)
   13.4. [İleri Seviye Programlama Örnekleri](#-i̇leri-seviye-programlama-pdsxv11g-ile-profesyonel-geliştirme)

### 13. Örnek Programlar ve Uygulamalar
   13.1. [Temel Program Örnekleri](#-örnekler)
   13.2. [Oyun Örnekleri](#-oyun-geliştirme-i̇çin-i̇puçları)
   13.3. [Veri Analizi Örnekleri](#örnek-3-veri-analizi)
   13.4. [İleri Seviye Programlama Örnekleri](#-i̇leri-seviye-programlama-pdsxv11g-ile-profesyonel-geliştirme)

---

## 2. 🚀 Kurulum ve Başlatma

### Sanal Ortam Kurulumu
```bash
# Sanal ortamı kur ve bağımlılıkları yükle
python pdsXv11g.py --setup-venv

# Bağımlılıkları kontrol et
python pdsXv11g.py --check-deps
```

### Çalıştırma Modları
```bash
# Etkileşimli REPL modu
python pdsXv11g.py

# Dosya çalıştırma
python pdsXv11g.py program.basx

# Debug modu
python pdsXv11g.py --debug program.basx

# Trace modu
python pdsXv11g.py --trace program.basx
```

---

## 3. 📝 Temel Komutlar

### PRINT - Ekrana Yazdırma

**PRINT** komutu, pdsXv11g'nin temel çıktı komutudur. Metin, sayılar, değişkenler ve ifadeleri ekrana yazdırmak için kullanılır. BASIC dilinin geleneksel formatını korurken modern özellikler de sunar.

**Syntax:**
```basic
PRINT [ifade1] [,|;] [ifade2] [,|;] ...
```

**Kullanım Şekilleri:**
```basic
PRINT "Merhaba Dünya"                    ' Basit metin yazdırma
PRINT variable_name                      ' Değişken değerini yazdır
PRINT "Değer:", variable_name            ' Karışık yazdırma
PRINT value1, value2, value3             ' Virgülle ayırma (tab ile ayrılır)
PRINT "Satır sonu yok";                  ' Semicolon ile satır sonu engelleme
PRINT                                    ' Boş satır yazdır
```

**Özel Format Özellikleri:**
- **Virgül (,)** - Elemanlar arasında TAB boşluk bırakır
- **Noktalı virgül (;)** - Elemanlar arasında boşluk bırakmaz
- **Sonunda ;** - Satır sonu karakteri yazdırmaz (bir sonraki PRINT aynı satırda devam eder)

**Örnekler:**
```basic
DIM name AS STRING = "Ahmet"
DIM age AS INTEGER = 25
DIM score AS DOUBLE = 87.5

PRINT "Ad:", name, "Yaş:", age           ' Tab'larla ayrılmış çıktı
PRINT "Skor: "; score; "%"               ' Boşluksuz birleştirme  
PRINT "Loading";                         ' Satır sonu yok
FOR i = 1 TO 5
    PRINT ".";                           ' Aynı satırda nokta ekle
NEXT i
PRINT                                    ' Satır sonu
```

### INPUT - Kullanıcıdan Veri Alma

**INPUT** komutu, program çalıştırma sırasında kullanıcıdan veri girmesini bekler ve bu veriyi belirtilen değişkende saklar. Kullanıcı etkileşimli programlar oluşturmak için temeldir.

**Syntax:**
```basic
INPUT [prompt_mesajı,] değişken_adı
```

**Kullanım Şekilleri:**
```basic
INPUT "Adınızı girin: ", user_name       ' Prompt ile giriş
INPUT "Yaşınız: ", age                    ' Prompt ile sayı girişi
INPUT variable_name                       ' Prompt olmadan giriş
```

**Veri Tipi Dönüşümü:**
pdsXv11g INPUT komutunda otomatik tip dönüşümü yapar:
- Sayı girişi beklenen değişken varsa, kullanıcının girdiği metin sayıya çevrilmeye çalışılır
- String değişken varsa, girilen tüm metin aynen kabul edilir
- Geçersiz sayı girişi durumunda 0 değeri atanır

**Örnekler:**
```basic
DIM user_name AS STRING
DIM user_age AS INTEGER
DIM user_score AS DOUBLE

INPUT "Tam adınızı girin: ", user_name
INPUT "Yaşınızı girin (sayı): ", user_age
INPUT "Notunuzu girin (örn: 85.5): ", user_score

PRINT "Merhaba " + user_name
PRINT "Yaşınız: " + STR$(user_age) + " yıl"
PRINT "Notunuz: " + STR$(user_score)
```

**Interactive Menu Örneği:**
```basic
DIM choice AS INTEGER
PRINT "=== Ana Menü ==="
PRINT "1. Yeni Kayıt"
PRINT "2. Listele"
PRINT "3. Çıkış"
INPUT "Seçiminiz (1-3): ", choice

SELECT CASE choice
    CASE 1: PRINT "Yeni kayıt işlemi"
    CASE 2: PRINT "Listeleme işlemi"  
    CASE 3: PRINT "Program sonlandırılıyor"
    CASE ELSE: PRINT "Geçersiz seçim"
END SELECT
```

### END - Program Sonlandırma (YENİ ÖZELLİK - pdsXv11g)

**END** komutu, programı herhangi bir noktada güvenli bir şekilde sonlandırmak için kullanılır. Bu komut, program akışının kesintiye uğramasını sağlar ve tüm kaynaklar temizlenerek yorumlayıcı durur.

**Syntax:**
```basic
END
```

**Kullanım Alanları:**
- Hata durumlarında programı sonlandırma
- Koşullu program çıkışları
- Ana program sonunda (opsiyonel)
- Kritik hata durumlarında acil sonlandırma

**Örnekler:**
```basic
' Program sonlandırma komutu
PRINT "Program başlıyor..."
' ... program kodları ...
PRINT "Program tamamlandı"
END

' Koşullu sonlandırma
DIM user_input AS STRING
INPUT "Devam etmek için 'E', çıkmak için 'Q': ", user_input
IF UPPER$(user_input) = "Q" THEN
    PRINT "Program kullanıcı tarafından sonlandırıldı"
    END
END IF

' Hata durumunda sonlandırma
DIM file_exists AS BOOLEAN
file_exists = EXISTS("critical_file.txt")
IF NOT file_exists THEN
    PRINT "HATA: Kritik dosya bulunamadı!"
    PRINT "Program sonlandırılıyor..."
    END
END IF
```

**Fonksiyon İçinden Program Sonlandırma:**
```basic
DEF SUB check_critical_error()
    DIM memory_usage AS DOUBLE
    memory_usage = MEMORY_USAGE()
    
    IF memory_usage > 1000 THEN  ' 1GB üzeri
        PRINT "Kritik hata: Bellek sınırı aşıldı!"
        PRINT "Sistem güvenliği için program sonlandırılıyor"
        END  ' Tüm programı sonlandır (sadece fonksiyonu değil)
    END IF
END SUB

' Ana program
DIM counter AS INTEGER
counter = 0
WHILE TRUE
    counter = counter + 1
    check_critical_error()  ' Her döngüde kontrol et
    PRINT "İşlem " + STR$(counter) + " tamamlandı"
    WAIT 1000
WEND
```

**Güvenli Kapanış Örneği:**
```basic
DIM shutdown_requested AS BOOLEAN
shutdown_requested = FALSE

' Signal handler simülasyonu
DEF SUB handle_shutdown_signal()
    shutdown_requested = TRUE
    PRINT "Kapanış sinyali alındı, güvenli kapanış yapılıyor..."
    
    ' Kayıt işlemleri
    SAVE "session_data.txt"
    
    ' Bağlantıları kapat
    IF db_connected THEN
        DISCONNECT DATABASE
    END IF
    
    PRINT "Tüm işlemler tamamlandı, program sonlandırılıyor"
    END
END SUB
```

**NOT:** END komutu çağrıldığında, program hemen durur ve hiçbir sonraki satır çalışmaz. Bu komut, GOSUB/RETURN cycle'ını da keser ve tüm loop'ları sonlandırır.

### REM - Yorum Satırları

**REM** (REMARK) komutu ve **'** (apostrophe) operatörü, kod içine açıklama ve yorum satırları eklemek için kullanılır. Bu açıklamalar program çalışırken yorumlayıcı tarafından göz ardı edilir ve sadece kod okunabilirliğini artırmak için vardır.

**Syntax:**
```basic
REM açıklama metni
' açıklama metni
```

**Kullanım Şekilleri:**
```basic
REM Bu bir yorum satırıdır
' Bu da yorum satırıdır (kısa format)
DIM x AS INTEGER  ' Satır sonu yorumu
REM ======================================
REM      PROGRAM: Hesap Makinesi
REM      YAZAR:   Geliştirici Adı  
REM      TARİH:   2024-01-15
REM ======================================
```

**Best Practices (İyi Uygulamalar):**
```basic
' ===== BAŞLIK YORUMU =====
REM Bu bölüm kullanıcı giriş verilerini işler

DIM user_name AS STRING     ' Kullanıcının adı
DIM user_age AS INTEGER     ' Kullanıcının yaşı (0-150 arası)
DIM is_valid AS BOOLEAN     ' Giriş verisi geçerliliği

' Veri doğrulama kontrolü
IF user_age < 0 OR user_age > 150 THEN
    REM Geçersiz yaş durumunda hata mesajı ver
    PRINT "Geçersiz yaş değeri!"
    is_valid = FALSE
ELSE
    is_valid = TRUE
END IF

REM TODO: E-mail doğrulama özelliği eklenecek
REM FIXME: Unicode karakter desteği geliştirilmeli
REM NOTE: Bu fonksiyon v2.0'da optimizasyon görecek
```

**Çok Satırlı Dokümantasyon:**
```basic
REM ========================================================
REM Fonksiyon: calculate_compound_interest
REM Açıklama: Bileşik faiz hesaplama işlemi yapar
REM Parametreler:
REM   - principal: Ana para (DOUBLE)
REM   - rate: Yıllık faiz oranı (DOUBLE, örn: 0.05 = %5)
REM   - time: Yıl sayısı (INTEGER)
REM   - compound_freq: Yılda kaç kez bileşik (INTEGER)
REM Dönüş: Bileşik faizli toplam tutar (DOUBLE)
REM Örnek: calculate_compound_interest(1000, 0.05, 10, 12)
REM ========================================================
DEF FUNCTION calculate_compound_interest(principal, rate, time, compound_freq)
    ' A = P(1 + r/n)^(nt) formülü
    DIM result AS DOUBLE
    result = principal * (1 + rate/compound_freq)^(compound_freq * time)
    RETURN result
END FUNCTION
```

**Conditional Comments (Debug İçin):**
```basic
' Debug mode yorumları
REM *** DEBUG START ***
' PRINT "Debug: user_input = " + user_input
' PRINT "Debug: calculation_result = " + STR$(calculation_result)
REM *** DEBUG END ***

' Versiyonlama yorumları
REM v1.0: İlk sürüm - temel hesaplama
REM v1.1: Hata kontrolü eklendi
REM v1.2: Kullanıcı arayüzü iyileştirildi (mevcut sürüm)

' Platform spesifik yorumlar
REM Windows için: USE_COLORS = FALSE
REM Linux için: USE_COLORS = TRUE
```

**Kod Bölümlendirme:**
```basic
REM ============================================
REM           PROGRAM BAŞLANGIÇ
REM ============================================

' Global değişkenlerin tanımlanması
DIM app_version AS STRING = "1.2.0"
DIM max_attempts AS INTEGER = 3

REM ============================================
REM           YARDIMCI FONKSİYONLAR
REM ============================================

DEF FUNCTION get_user_input()
    ' Kullanıcı giriş fonksiyonu
END FUNCTION

REM ============================================
REM              ANA PROGRAM
REM ============================================

PRINT "Program başlatılıyor..."
' ... ana kod buraya gelir ...
```

**ÖNEML NOT:** REM ve ' yorumları program performansını etkilemez, çünkü derleme sırasında tamamen kaldırılır.

### HELP - Yardım Sistemi

**HELP** komutu, pdsXv11g'nin interaktif yardım sistemini sağlar. Komutlar, fonksiyonlar, syntax kuralları ve örnek kullanımlar hakkında detaylı bilgi almak için kullanılır.

**Syntax:**
```basic
HELP [komut_veya_fonksiyon_adı]
HELP [kategori_adı]
```

**Kullanım Şekilleri:**
```basic
HELP                        ' Genel yardım menüsü
HELP PRINT                  ' PRINT komutu hakkında detay
HELP IF                     ' IF komutu syntax'ı ve örnekleri
HELP EXAMPLES               ' Örnek programlar
HELP STRING                 ' String fonksiyonları listesi
HELP MATH                   ' Matematik fonksiyonları
HELP OPERATORS              ' Operatörler listesi
HELP DATATYPES              ' Veri tipleri bilgisi
```

**Yardım Kategorileri:**
```basic
' Komut kategorileri
HELP BASIC                  ' Temel komutlar (PRINT, INPUT, LET, DIM)
HELP CONTROL                ' Kontrol yapıları (IF, FOR, WHILE, SELECT)
HELP FLOW                   ' Program akış komutları (GOTO, GOSUB, RETURN)
HELP ERROR                  ' Hata yönetimi (TRY-CATCH, ON ERROR)
HELP FILE                   ' Dosya işlemleri
HELP DATABASE               ' Veritabanı komutları
HELP DEBUG                  ' Debug komutları (DEBUG ON/OFF, TRACE)

' Fonksiyon kategorileri  
HELP STRING_FUNCTIONS       ' String işlev fonksiyonları
HELP MATH_FUNCTIONS         ' Matematik fonksiyonları
HELP ARRAY_FUNCTIONS        ' Dizi işlem fonksiyonları
HELP DATE_FUNCTIONS         ' Tarih/saat fonksiyonları
HELP SYSTEM_FUNCTIONS       ' Sistem fonksiyonları
HELP PANDAS                 ' Pandas DataFrame işlemleri
HELP NUMPY                  ' NumPy array işlemleri
```

**Özel Yardım Komutları:**
```basic
HELP EXAMPLES               ' Hazır örnek programlar
HELP SYNTAX                 ' Genel syntax kuralları
HELP KEYWORDS               ' Rezerve edilmiş kelimeler
HELP OPERATORS              ' Tüm operatörler (+, -, *, /, AND, OR, vs.)
HELP DATATYPES              ' Veri tipleri (INTEGER, STRING, ARRAY, vs.)
HELP LATEST                 ' Son sürüm yenilikleri
HELP PERFORMANCE            ' Performans ipuçları
HELP BEST_PRACTICES         ' En iyi uygulamalar
```

**Yardım Sistemi Çıktı Örneği:**
```basic
HELP PRINT
' Çıktı:
' =========================================
' KOMUT: PRINT
' =========================================
' Açıklama: Değişken ve ifadeleri ekrana yazdırır
' Syntax: PRINT [ifade1] [,|;] [ifade2] ...
' 
' Parametreler:
'   • ifade: Yazdırılacak değer (string, sayı, değişken)
'   • , (virgül): Tab boşluk bırakır
'   • ; (noktalı virgül): Boşluk bırakmaz
' 
' Örnekler:
'   PRINT "Merhaba Dünya"
'   PRINT "Ad:", name, "Yaş:", age  
'   PRINT "Loading"; : FOR i = 1 TO 5 : PRINT "."; : NEXT
' =========================================
```

**Etkileşimli Yardım Modu:**
```basic
DIM help_topic AS STRING
INPUT "Yardım konusu (veya 'list' kategoriler için): ", help_topic

SELECT CASE UPPER$(help_topic)
    CASE "LIST"
        HELP                ' Genel kategori listesi
    CASE "EXAMPLES"  
        HELP EXAMPLES       ' Örnek programlar
    CASE ""
        PRINT "Kullanım: HELP <konu> veya HELP LIST"
    CASE ELSE
        ' Kullanıcının istediği konuda yardım göster
        DIM help_command AS STRING
        help_command = "HELP " + help_topic
        EXECUTE help_command
END SELECT
```

**Fonksiyon İçinde Yardım:**
```basic
DEF SUB show_menu_help()
    PRINT "========== YARDIM MENÜSÜ =========="
    PRINT "Genel Yardım Komutları:"
    PRINT "  HELP           - Ana yardım menüsü"
    PRINT "  HELP EXAMPLES  - Örnek programlar"  
    PRINT "  HELP SYNTAX    - Syntax kuralları"
    PRINT
    PRINT "Komut Yardımları:"
    PRINT "  HELP PRINT     - PRINT komutu"
    PRINT "  HELP IF        - IF komutu" 
    PRINT "  HELP FOR       - FOR döngüsü"
    PRINT
    PRINT "Fonksiyon Yardımları:"
    PRINT "  HELP STRING    - String fonksiyonları"
    PRINT "  HELP MATH      - Matematik fonksiyonları"
    PRINT "  HELP ARRAY     - Dizi işlem fonksiyonları"
    PRINT "  HELP DATE      - Tarih/saat fonksiyonları"
    PRINT "  HELP SYSTEM    - Sistem fonksiyonları"
    PRINT "  HELP PANDAS    - Pandas DataFrame işlemleri"
    PRINT "  HELP NUMPY     - NumPy array işlemleri"
    PRINT "=================================="
END SUB
```

## 4. 🗂️ Veri Tipleri

### Temel Tipler

pdsXv11g, modern programlama dillerinin tüm temel veri tiplerini destekler. Her veri tipi için otomatik tip dönüşümü ve güvenli bellek yönetimi sağlanır.

**Tam Tip Listesi ve Syntax:**
```basic
DIM name AS STRING          ' Metin verisi (Unicode destekli)
DIM age AS INTEGER          ' Tam sayı (-2,147,483,648 ile 2,147,483,647)
DIM price AS DOUBLE         ' Çift hassasiyetli ondalık sayı
DIM temperature AS SINGLE   ' Tek hassasiyetli ondalık sayı  
DIM flag AS BOOLEAN         ' Mantıksal değer (TRUE/FALSE)
DIM byte_data AS BYTE       ' Byte verisi (0-255)
DIM big_number AS LONG      ' Uzun tam sayı (-9,223,372,036,854,775,808 ile +9,223,372,036,854,775,807)
DIM char_code AS SHORT      ' Kısa tam sayı (-32,768 ile 32,767)
```

**Otomatik Tip Dönüşümü Örnekleri:**
```basic
DIM number AS INTEGER = 42
DIM text AS STRING = "Sayı: " + STR$(number)    ' INT -> STRING dönüşümü
DIM decimal AS DOUBLE = 3.14
DIM rounded AS INTEGER = INT(decimal)           ' DOUBLE -> INTEGER dönüşümü

' Otomatik tip genişletme
DIM small AS INTEGER = 100
DIM large AS LONG = small                       ' INTEGER -> LONG (güvenli)
DIM precise AS DOUBLE = small                   ' INTEGER -> DOUBLE (güvenli)
```

**Tip Kontrolü ve Doğrulama:**
```basic
DIM user_input AS STRING = "123"
DIM numeric_value AS INTEGER

' Güvenli sayı dönüşümü
IF ISNUMERIC(user_input) THEN
    numeric_value = VAL(user_input)
    PRINT "Dönüştürülen sayı:", numeric_value
ELSE
    PRINT "Geçersiz sayı formatı!"
END IF

' Tip kontrol fonksiyonları
PRINT "Veri tipi:", TYPE_OF(numeric_value)      ' "INTEGER" döner
PRINT "Bellek boyutu:", SIZEOF(numeric_value)   ' Byte cinsinden boyut
```

**String Özel Özellikleri:**
```basic
DIM unicode_text AS STRING = "Merhaba 🌟 Dünya"
DIM multiline AS STRING = "Birinci satır" + CHR$(10) + "İkinci satır"
DIM escaped AS STRING = "Tırnak işareti: \"Merhaba\""

' String interpolation (modern özellik)
DIM user AS STRING = "Ahmet"
DIM message AS STRING = F"Hoşgeldin, {user}!"   ' Python-style formatting
```

**Boolean Logic Özellikleri:**
```basic
DIM condition1 AS BOOLEAN = TRUE
DIM condition2 AS BOOLEAN = FALSE

' Mantıksal operatörler
DIM result1 AS BOOLEAN = condition1 AND condition2    ' FALSE
DIM result2 AS BOOLEAN = condition1 OR condition2     ' TRUE  
DIM result3 AS BOOLEAN = NOT condition1               ' FALSE
DIM result4 AS BOOLEAN = condition1 XOR condition2    ' TRUE

' Boolean'dan sayıya dönüşüm
DIM bool_as_int AS INTEGER = IIF(condition1, 1, 0)   ' TRUE -> 1, FALSE -> 0
```

**Sayısal İşlemler ve Sınırlar:**
```basic
' Sayısal sınır kontrolü
DIM max_int AS INTEGER = 2147483647
DIM min_int AS INTEGER = -2147483648

' Overflow kontrolü
DIM safe_calc AS LONG = LONG(max_int) + 1000    ' LONG'a dönüştürerek overflow'u önle

' Hassasiyet farkları
DIM precise AS DOUBLE = 1.0 / 3.0               ' 0.3333333333333333
DIM less_precise AS SINGLE = 1.0 / 3.0          ' 0.33333334
```

**Tip Dönüşüm Fonksiyonları:**
```basic
' Açık tip dönüşümleri
DIM str_num AS STRING = "42.7"
DIM as_int AS INTEGER = INT(VAL(str_num))        ' 42
DIM as_double AS DOUBLE = VAL(str_num)           ' 42.7
DIM as_string AS STRING = STR$(as_double)        ' "42.7"

' Güvenli dönüşümler
DEF FUNCTION SAFE_INT(value)
    TRY
        RETURN INT(value)
    CATCH ex DO
        RETURN 0
    END TRY
END FUNCTION
```

**Memory Efficiency Tips:**
```basic
' Bellek verimli tip seçimi
DIM small_counter AS BYTE = 0        ' 0-255 arası sayılar için
DIM medium_counter AS SHORT = 0      ' -32K ile +32K arası için  
DIM large_counter AS INTEGER = 0     ' Standart tam sayılar için
DIM huge_counter AS LONG = 0         ' Çok büyük sayılar için

' String memory management
DIM large_text AS STRING = ""
FOR i = 1 TO 1000
    large_text = large_text + "veri"    ' Inefficient - her seferinde yeni string
NEXT i

' Daha verimli yaklaşım:
DIM text_parts AS ARRAY = []
FOR i = 1 TO 1000
    INSERT(text_parts, "veri")
NEXT i
DIM efficient_text AS STRING = JOIN(text_parts, "")
```

### Koleksiyon Tipleri

pdsXv11g, modern veri yapılarının tamamını destekler. Bu koleksiyonlar dinamik boyutlu olup, runtime'da büyüyebilir ve küçülebilir. Her koleksiyon tipi için özel built-in fonksiyonlar mevcuttur.

**Tüm Koleksiyon Tipleri:**
```basic
DIM my_list AS LIST         ' Dinamik liste (sıralı, mükerrer öğe kabul eder)
DIM my_dict AS DICT         ' Sözlük/Dictionary (anahtar-değer çiftleri)
DIM my_set AS SET           ' Küme (benzersiz öğeler, sırasız)
DIM my_tuple AS TUPLE       ' Tuple (sabit boyutlu, değiştirilemez)
DIM my_array AS ARRAY       ' Genel dizi (en esnek koleksiyon)
DIM my_stack AS STACK       ' Yığın (LIFO - Last In, First Out)
DIM my_queue AS QUEUE       ' Kuyruk (FIFO - First In, First Out)
```

**LIST İşlemleri:**
```basic
DIM student_names AS LIST
student_names = ["Ahmet", "Mehmet", "Ayşe"]

' Liste manipülasyonu
INSERT(student_names, "Fatma")              ' Sona ekle
INSERT_AT(student_names, 1, "Ali")          ' Belirli pozisyona ekle
REMOVE(student_names, "Mehmet")             ' Değere göre sil
REMOVE_AT(student_names, 0)                 ' İndekse göre sil
CLEAR(student_names)                        ' Tümünü temizle

' Liste sorgulama
DIM count AS INTEGER = LEN(student_names)   ' Eleman sayısı
DIM exists AS BOOLEAN = CONTAINS(student_names, "Ali")
DIM index AS INTEGER = INDEXOF(student_names, "Ayşe")

' Liste işlemleri
SORT(student_names)                         ' Alfabetik sıralama
REVERSE(student_names)                      ' Tersine çevir
DIM shuffled AS LIST = SHUFFLE(student_names)  ' Karıştır
```

**DICT (Dictionary) İşlemleri:**
```basic
DIM student_grades AS DICT
student_grades = {"Ahmet": 85, "Mehmet": 92, "Ayşe": 78}

' Dictionary manipülasyonu  
student_grades("Fatma") = 88                ' Yeni anahtar-değer ekle
student_grades("Ahmet") = 90                ' Mevcut değeri güncelle
REMOVE(student_grades, "Mehmet")            ' Anahtara göre sil
CLEAR(student_grades)                       ' Tümünü temizle

' Dictionary sorgulama
DIM has_key AS BOOLEAN = CONTAINS_KEY(student_grades, "Ali")
DIM has_value AS BOOLEAN = CONTAINS_VALUE(student_grades, 85)
DIM keys AS ARRAY = KEYS(student_grades)    ' Tüm anahtarlar
DIM values AS ARRAY = VALUES(student_grades) ' Tüm değerler

' Dictionary iterasyonu
FOR EACH key IN KEYS(student_grades)
    DIM grade AS INTEGER = student_grades(key)
    PRINT key + ": " + STR$(grade)
NEXT

' Güvenli erişim
DIM grade AS INTEGER = GET(student_grades, "Zeynep", 0)  ' Yoksa 0 döner
```

**SET İşlemleri:**
```basic
DIM unique_colors AS SET
unique_colors = {"kırmızı", "mavi", "yeşil"}

' Set manipülasyonu
ADD(unique_colors, "sarı")                  ' Eleman ekle
ADD(unique_colors, "mavi")                  ' Mükerrer ekleme (etkisiz)
REMOVE(unique_colors, "kırmızı")           ' Eleman çıkar

' Set operasyonları
DIM other_colors AS SET = {"mavi", "mor", "turuncu"}
DIM union_set AS SET = UNION(unique_colors, other_colors)        ' Birleşim
DIM intersect AS SET = INTERSECTION(unique_colors, other_colors) ' Kesişim  
DIM diff AS SET = DIFFERENCE(unique_colors, other_colors)        ' Fark
```

**ARRAY İşlemleri (En Esnek Koleksiyon):**
```basic
DIM mixed_array AS ARRAY
mixed_array = [1, "metin", 3.14, TRUE, ["iç", "dizi"]]

' Array manipülasyonu
PUSH(mixed_array, "yeni eleman")           ' Sona ekle
DIM popped AS VARIANT = POP(mixed_array)   ' Sondan çıkar
UNSHIFT(mixed_array, "başa ekle")          ' Başa ekle  
DIM shifted AS VARIANT = SHIFT(mixed_array) ' Baştan çıkar

' Array dilimleme
DIM slice AS ARRAY = SLICE(mixed_array, 1, 3)  ' 1. indeksten 3. indekse kadar
DIM first_half AS ARRAY = SLICE(mixed_array, 0, LEN(mixed_array)/2)

' Array birleştirme
DIM array2 AS ARRAY = ["ek1", "ek2"]
DIM combined AS ARRAY = CONCAT(mixed_array, array2)
```

**TUPLE İşlemleri (Immutable):**
```basic
DIM coordinates AS TUPLE = (10.5, 20.3, 5.7)  ' 3D koordinat
DIM person_info AS TUPLE = ("Ahmet", 25, "Mühendis")

' Tuple erişimi (sadece okuma)
DIM x AS DOUBLE = coordinates(0)            ' 10.5
DIM name AS STRING = person_info(0)         ' "Ahmet"
DIM age AS INTEGER = person_info(1)         ' 25

' Tuple unpacking
DIM name2, age2, profession AS VARIANT
UNPACK person_info TO name2, age2, profession

PRINT "İsim: " + STR$(name2)
PRINT "Yaş: " + STR$(age2)  
PRINT "Meslek: " + STR$(profession)
```

---

## 5. 🔢 Değişkenler ve Atama

### Değişken Tanımlama
```basic
' Strict DIM mode - değişkenler kullanımdan önce tanımlanmalı
DIM name AS STRING
DIM age AS INTEGER
DIM scores AS ARRAY 
```

### Değişken Atama
```basic
' LET ile atama
LET name = "Ahmet"
LET age = 25

' Direkt atama (LET olmadan)
name = "Mehmet"
age = 30
```

### Dizi İşlemleri
```basic
' Dizi tanımlama
DIM numbers(10) AS INTEGER     ' 10 elemanlı dizi
DIM matrix(3, 3) AS DOUBLE     ' 3x3 matris

' Dizi atama
numbers(0) = 100
numbers(1) = 200
matrix(0, 0) = 1.5
matrix(1, 2) = 3.14

' Dizi erişimi
PRINT numbers(0)
PRINT matrix(1, 2)
```

---

## 6. 🔀 Kontrol Yapıları

Kontrol yapıları, programın akışını yönlendiren temel yapı taşlarıdır. pdsXv11g, geleneksel BASIC kontrol yapılarını modern özelliklerle genişleterek güçlü karar verme mekanizmaları sunar. Bu yapılar sayesinde programlarınız koşullara göre farklı işlemler yapabilir ve karmaşık mantık kurabilirsiniz.

**Temel Kontrol Yapıları:**
- `IF-THEN-ELSE`: Basit ve çok satırlı koşul kontrolü
- `SELECT CASE`: Çok seçenekli koşul kontrolü (switch-case benzeri)

**Syntax Genel Formatı:**
```basic
IF koşul THEN komut                    ' Tek satır IF
IF koşul THEN                          ' Çok satırlı IF
    komutlar...
ELSEIF başka_koşul THEN
    komutlar...
ELSE
    komutlar...
END IF

SELECT CASE değişken                   ' Çoklu seçim
    CASE değer1: komutlar...
    CASE değer2: komutlar...
    CASE ELSE: komutlar...
END SELECT
```

### IF-THEN-ELSE
```basic
' Tek satır IF
IF age >= 18 THEN PRINT "Reşit"

' Blok IF (Çok satırlı)
IF score >= 90 THEN
    PRINT "Mükemmel!"
    PRINT "Tebrikler"
ELSEIF score >= 80 THEN
    PRINT "İyi"
ELSEIF score >= 70 THEN
    PRINT "Orta"
ELSE
    PRINT "Geliştirmeye ihtiyaç var"
END IF
```

### SELECT CASE - Gelişmiş Koşullu Yapı

pdsXv11g'de SELECT CASE komutları, tüm veri tipleri ve karmaşık koşulları destekler:

#### Temel SELECT CASE Kullanımı
```basic
DIM choice AS INTEGER
choice = 2

SELECT CASE choice
    CASE 1
        PRINT "Bir seçildi"
    CASE 2
        PRINT "İki seçildi"
    CASE 3 TO 5
        PRINT "3-5 arası"
    CASE ELSE
        PRINT "Diğer"
END SELECT
```

#### String Değerlerle SELECT CASE
```basic
DIM user_input AS STRING
user_input = "start"

SELECT CASE user_input
    CASE "start", "begin", "go"
        PRINT "Başlatılıyor..."
    CASE "stop", "end", "quit"
        PRINT "Durduruluyor..."
    CASE "help", "?"
        PRINT "Yardım menüsü"
    CASE ELSE
        PRINT "Geçersiz komut"
END SELECT
```

#### Boolean Değerlerle SELECT CASE
```basic
DIM game_running AS BOOLEAN
DIM player_alive AS BOOLEAN
game_running = TRUE
player_alive = FALSE

SELECT CASE game_running AND player_alive
    CASE TRUE
        PRINT "Oyun devam ediyor"
    CASE FALSE
        IF NOT game_running THEN
            PRINT "Oyun durduruldu"
        ELSEIF NOT player_alive THEN
            PRINT "Game Over!"
        END IF
END SELECT
```

#### Float/Double Değerlerle SELECT CASE
```basic
DIM score AS DOUBLE
score = 87.5

SELECT CASE score
    CASE 90.0 TO 100.0
        PRINT "Mükemmel: A"
    CASE 80.0 TO 89.99
        PRINT "İyi: B"  
    CASE 70.0 TO 79.99
        PRINT "Orta: C"
    CASE ELSE
        PRINT "Geliştirmeye ihtiyaç var"
END SELECT
```

#### CASE IS - Karşılaştırma Operatörleri
```basic
DIM temperature AS INTEGER
temperature = 25

SELECT CASE temperature
    CASE IS > 30
        PRINT "Çok sıcak"
    CASE IS >= 20
        PRINT "Ilık"
    CASE IS > 0
        PRINT "Soğuk"
    CASE IS <= 0
        PRINT "Donuyor!"
END SELECT

DIM age AS INTEGER
age = 17

SELECT CASE age
    CASE IS >= 65
        PRINT "Emekli"
    CASE IS >= 18
        PRINT "Yetişkin"
    CASE IS >= 13
        PRINT "Genç"
    CASE ELSE
        PRINT "Çocuk"
END SELECT
```

#### Karmaşık İfadeler ve Çoklu Değerler
```basic
DIM day_of_week AS INTEGER
day_of_week = 3

SELECT CASE day_of_week
    CASE 1, 7
        PRINT "Hafta sonu"
    CASE 2, 3, 4, 5, 6
        PRINT "İş günü"
    CASE IS < 1
        PRINT "Geçersiz gün"
    CASE IS > 7  
        PRINT "Geçersiz gün"
END SELECT

' Hesaplanmış değerler
DIM x AS INTEGER
DIM y AS INTEGER
x = 10
y = 5

SELECT CASE x * y
    CASE 50
        PRINT "50'ye eşit"
    CASE IS > 40
        PRINT "40'tan büyük"
    CASE 25, 30, 35
        PRINT "25, 30 veya 35"
    CASE ELSE
        PRINT "Diğer değer:", x * y
END SELECT
```

#### Fonksiyon Sonuçları ile SELECT CASE
```basic
DIM user_name AS STRING
user_name = "ADMIN"

SELECT CASE UCASE$(user_name)
    CASE "ADMIN", "ADMINISTRATOR"
        PRINT "Yönetici girişi"
    CASE "GUEST", "ANONYMOUS"
        PRINT "Misafir kullanıcı"
    CASE ELSE
        PRINT "Normal kullanıcı:", user_name
END SELECT

' String fonksiyonları
DIM password AS STRING
password = "mypassword123"

SELECT CASE LEN(password)
    CASE IS < 8
        PRINT "Şifre çok kısa"
    CASE IS > 20
        PRINT "Şifre çok uzun"
    CASE 8 TO 12
        PRINT "İyi şifre uzunluğu"
    CASE ELSE
        PRINT "Kabul edilebilir uzunluk"
END SELECT
```

#### İç İçe SELECT CASE
```basic
DIM user_role AS STRING
DIM user_level AS INTEGER
user_role = "admin"
user_level = 5

SELECT CASE user_role
    CASE "admin"
        SELECT CASE user_level
            CASE 1 TO 3
                PRINT "Yardımcı yönetici"
            CASE 4 TO 7
                PRINT "Orta seviye yönetici"
            CASE IS >= 8
                PRINT "Üst düzey yönetici"
        END SELECT
    CASE "user"
        PRINT "Normal kullanıcı"
    CASE "guest"
        PRINT "Misafir"
END SELECT
```

#### Dizi Değerleri ile SELECT CASE
```basic
DIM colors AS ARRAY
colors = ["red", "green", "blue"]

SELECT CASE LEN(colors)
    CASE 0
        PRINT "Renk yok"
    CASE 1 TO 3
        PRINT "Az sayıda renk"
    CASE IS > 10
        PRINT "Çok fazla renk"
    CASE ELSE
        PRINT "Orta sayıda renk"
END SELECT

' İlk elemanı kontrol et
SELECT CASE colors(0)
    CASE "red", "crimson", "scarlet"
        PRINT "Kırmızı ton"
    CASE "green", "lime", "emerald"
        PRINT "Yeşil ton"
    CASE "blue", "navy", "azure"
        PRINT "Mavi ton"
END SELECT
```

### SELECT CASE Yapısının Genişletilmesi

SELECT CASE yapısı artık şu özellikleri desteklemektedir:
- Karşılaştırma operatörleri (IS >, IS <, IS = vb.)
- Aralık tanımları (5..10 gibi)
- Çoklu değer kontrolü (CASE 1, 2, 3)
- String karşılaştırmaları
- IS operatörleri ile detaylı koşullar

Örnek kullanım:
```basic
DIM age AS INTEGER = 25

SELECT CASE age
    CASE IS < 13
        PRINT "Çocuk"
    CASE 13..19
        PRINT "Genç"
    CASE IS >= 65
        PRINT "Yaşlı"
    CASE ELSE
        PRINT "Yetişkin"
END SELECT
```

SELECT CASE yapısı pdsXv11g'de çok güçlüdür ve:
- Tüm veri tiplerini (string, integer, float, boolean) destekler
- CASE IS ile karşılaştırma operatörleri (<, >, <=, >=, <>, =)
- Çoklu değer kontrolü (CASE 1, 2, 3)
- Aralık kontrolü (CASE 1 TO 10)  
- Karmaşık ifadeler ve fonksiyon sonuçları
- İç içe SELECT CASE blokları

---

## 7. 🔄 Döngüler

Döngüler, belirli işlemleri tekrarlamak için kullanılan temel programlama yapılarıdır. pdsXv11g, geleneksel BASIC döngülerini modern koleksiyon desteği ile genişletmiştir. Döngüler sayesinde büyük veri kümeleri üzerinde işlem yapabilir, tekrarlayan görevleri otomatikleştirebilir ve karmaşık hesaplamalar gerçekleştirebilirsiniz.

**Döngü Tipleri:**
- `FOR-NEXT`: Sayısal aralıklarda iterasyon
- `FOR EACH IN`: Koleksiyonlar üzerinde modern iterasyon (YENİ)
- `WHILE-WEND`: Koşul tabanlı döngü
- `DO-LOOP`: Esnek koşul döngüsü

**Döngü Kontrolü:**
- `EXIT FOR/WHILE/DO`: Döngüden çıkış
- `CONTINUE FOR/WHILE/DO`: Döngünün sonraki iterasyonuna geç

**Syntax Genel Formatı:**
```basic
FOR değişken = başlangıç TO bitiş [STEP artım]  ' Sayısal döngü
    komutlar...
NEXT [değişken]

FOR EACH eleman IN koleksiyon                   ' Koleksiyon döngüsü
    komutlar...
NEXT

WHILE koşul                                     ' Koşul döngüsü
    komutlar...
WEND

DO [WHILE/UNTIL koşul]                          ' Esnek döngü
    komutlar...
LOOP [WHILE/UNTIL koşul]
```

### FOR-NEXT Döngüsü
```basic
' Basit FOR döngüsü
FOR i = 1 TO 10
    PRINT i
NEXT

' STEP ile döngü
FOR i = 0 TO 20 STEP 2
    PRINT i
NEXT

' Geriye doğru döngü
FOR i = 10 TO 1 STEP -1
    PRINT i
NEXT

' İç içe döngüler
FOR row = 1 TO 3
    FOR col = 1 TO 3
        PRINT row * col
    NEXT col
NEXT row
```

### FOR EACH IN Döngüsü (YENİ ÖZELLİK - pdsXv11g)
```basic
' Array üzerinde iterasyon
DIM numbers AS ARRAY = [10, 20, 30, 40, 50]
FOR EACH num IN numbers
    PRINT "Sayı:", num
NEXT

' String array üzerinde iterasyon  
DIM cities AS ARRAY = ["İstanbul", "Ankara", "İzmir"]
FOR EACH city IN cities
    PRINT "Şehir:", city
NEXT

' Liste üzerinde iterasyon
DIM my_list AS LIST = [1, 2, 3, 4, 5]
FOR EACH item IN my_list
    PRINT "Eleman:", item
NEXT

' Sözlük anahtarları üzerinde iterasyon
DIM person AS DICT = {"name": "Ahmet", "age": 30, "city": "İstanbul"}
FOR EACH key IN person.KEYS()
    PRINT key + ":", person(key)
NEXT
```

### WHILE-WEND Döngüsü
```basic
DIM counter AS INTEGER
counter = 1

WHILE counter <= 5
    PRINT "Counter:", counter
    counter = counter + 1
WEND
```

### DO-LOOP Döngüsü
```basic
' Basit DO-LOOP
DIM i AS INTEGER
i = 1
DO
    PRINT i
    i = i + 1
LOOP UNTIL i > 5

' DO WHILE
i = 1
DO WHILE i <= 5
    PRINT i
    i = i + 1
LOOP
```

### Döngü Kontrol Komutları
```basic
' Döngüden çıkış
FOR i = 1 TO 100
    IF i = 50 THEN EXIT FOR
    PRINT i
NEXT

' Döngü devamı
FOR i = 1 TO 10
    IF i MOD 2 = 0 THEN CONTINUE FOR
    PRINT i  ' Sadece tek sayıları yazdır
NEXT

' DO döngüsünden çıkış
DO
    INPUT "Devam (e/h): ", answer
    IF answer = "h" THEN EXIT DO
LOOP

' DO döngüsü devamı
DO WHILE i <= 10
    i = i + 1
    IF i MOD 2 = 0 THEN CONTINUE DO
    PRINT i
LOOP
```
### DO WHILE/UNTIL Yapılarının Geliştirilmesi

DO döngüleri şu formatlarda kullanılabilir:
- DO ... LOOP (sonsuz döngü)
- DO WHILE condition ... LOOP
- DO UNTIL condition ... LOOP
- DO ... LOOP WHILE condition
- DO ... LOOP UNTIL condition

Özellikler:
- EXIT DO ile döngüden çıkış
- CONTINUE DO ile sonraki iterasyona geçiş
- İç içe DO döngüleri desteği

Örnek kullanım:
```basic
DO WHILE i < 10
    i = i + 1
    IF i MOD 2 = 0 THEN CONTINUE DO
    PRINT i
LOOP
```
---

## 8. 🔧 Fonksiyonlar

Fonksiyonlar, kodunuzu modüler hale getiren, yeniden kullanılabilir kod blokları oluşturmanızı sağlayan temel yapılardır. pdsXv11g, geleneksel BASIC fonksiyon tanımlarını modern lambda-style syntax ile genişletmiştir. Fonksiyonlar sayesinde karmaşık işlemleri küçük parçalara bölebilir, kod tekrarını önleyebilir ve daha okunabilir programlar yazabilirsiniz.

**Fonksiyon Türleri:**
- `DEF FN`: Tek satırlık matematik fonksiyonları
- `DEF FUNCTION`: Çok satırlı, karmaşık fonksiyonlar  
- `FUNC`: Modern lambda-style fonksiyonlar (YENİ)
- `DEF SUB`: Alt programlar (prosedürler)

**Fonksiyon Özellikleri:**
- **Parametre Geçişi**: Değer ile (pass-by-value) parametre aktarımı
- **Recursive (Özyinelemeli)**: Fonksiyonlar kendi kendilerini çağırabilir
- **Return Values**: Fonksiyonlar değer döndürebilir
- **Local Scope**: Fonksiyon içindeki değişkenler yerel kapsama sahip

**Syntax Genel Formatı:**
```basic
DEF FN fonksiyon_adı(parametreler) = ifade          ' Tek satır fonksiyon

DEF FUNCTION fonksiyon_adı(parametreler)             ' Çok satır fonksiyon
    komutlar...
    RETURN değer
END FUNCTION

FUNC fonksiyon_adı(parametreler)                     ' Lambda-style fonksiyon
    komutlar...
    RETURN değer
END FUNC

DEF SUB alt_program_adı(parametreler)                ' Alt program (prosedür)
    komutlar...
END SUB
```

### User-Defined Fonksiyonlar

#### DEF FN - Tek Satırlık Fonksiyonlar
```basic
' Basit matematik fonksiyonu
DEF FN square(x) = x * x

' Kullanım
PRINT square(5)    ' Sonuç: 25
```

#### DEF FUNCTION - Çok Satırlık Fonksiyonlar
```basic
DEF FUNCTION factorial(n)
    IF n <= 1 THEN
        RETURN 1
    ELSE
        RETURN n * factorial(n - 1)
    END IF
END FUNCTION

' Kullanım
PRINT factorial(5)    ' Sonuç: 120
```

#### FUNC - Lambda Tarzı Fonksiyonlar (YENİ ÖZELLİK - pdsXv11g)
```basic
' Modern lambda-style fonksiyon
FUNC multiply(a, b)
    RETURN a * b
END FUNC

' Kullanım
PRINT multiply(3, 4)  ' Sonuç: 12

' Daha karmaşık örnek
FUNC calculate_tax(price, rate)
    DIM tax AS DOUBLE = price * (rate / 100)
    RETURN price + tax
END FUNC

PRINT calculate_tax(1000, 18)  ' KDV hesaplama

' Inline matematiksel fonksiyonlar
FUNC power(base, exponent)
    DIM result AS DOUBLE = 1
    FOR i = 1 TO exponent
        result = result * base
    NEXT i
    RETURN result
END FUNC

PRINT power(2, 8)  ' 2^8 = 256
```

### DEF SUB - Alt Programlar
```basic
DEF SUB greet(name)
    PRINT "Merhaba " + name + "!"
    PRINT "Hoş geldiniz!"
END SUB

' Kullanım
greet("Ahmet")
```

---

## 9. 📚 Built-in Fonksiyonlar

pdsXv11g, zengin bir built-in fonksiyon kütüphanesi ile gelir. Bu fonksiyonlar, string işleme, matematiksel hesaplamalar, veri analizi ve sistem işlemleri gibi yaygın programlama görevlerini kolaylaştırır. Built-in fonksiyonlar optimize edilmiştir ve günlük programlama ihtiyaçlarının çoğunu karşılayacak şekilde tasarlanmıştır.

**Fonksiyon Kategorileri:**
- **String Fonksiyonları**: Metin işleme ve manipülasyon
- **Matematik Fonksiyonları**: Temel matematik, trigonometri, istatistik
- **NumPy İşlemleri**: Array ve matris işlemleri
- **Pandas DataFrame**: Veri analizi ve işleme
- **String Array Fonksiyonları**: 20+ gelişmiş string dizi işlevi (YENİ)
- **Sistem Fonksiyonları**: Dosya, tarih, bellek işlemleri

**Kullanım Avantajları:**
- **Hızlı ve Optimize**: C/Python seviyesinde performans
- **Kolay Kullanım**: Basit, anlaşılır syntax
- **Geniş Kapsam**: Çoğu programlama ihtiyacını karşılar
- **Entegrasyon**: NumPy ve Pandas ile tam uyumluluk

### String Fonksiyonları
```basic
LEN("Hello")                    ' String uzunluğu
LEFT$("Hello", 3)               ' Soldan 3 karakter: "Hel"
RIGHT$("Hello", 2)              ' Sağdan 2 karakter: "lo"
MID$("Hello", 2, 3)             ' 2. pozisyondan 3 karakter: "ell"
UCASE$("hello")                 ' Büyük harf: "HELLO"
LCASE$("HELLO")                 ' Küçük harf: "hello"
LTRIM$("  hello")               ' Sol boşlukları kaldır
RTRIM$("hello  ")               ' Sağ boşlukları kaldır
STRING$(5, "*")                 ' 5 tane "*": "*****"
SPACE$(3)                       ' 3 boşluk: "   "
INSTR(1, "Hello", "ll")         ' Alt string arama: 3
STR$(123)                       ' Sayıyı string'e çevir: "123"
VAL("123.45")                   ' String'i sayıya çevir: 123.45
ASC("A")                        ' Karakter kodu: 65
CHR$(65)                        ' Kod'dan karakter: "A"
```

### Matematik Fonksiyonları
```basic
' Temel matematik
ABS(-5)                         ' Mutlak değer: 5
INT(3.7)                        ' Tam kısmı: 3
SQR(16)                         ' Karekök: 4
ROUND(3.7, 0)                   ' Yuvarlama: 4
SGN(-5)                         ' İşaret: -1
MOD(7, 3)                       ' Mod: 1
MIN(5, 3, 8)                    ' Minimum: 3
MAX(5, 3, 8)                    ' Maksimum: 8

' Trigonometrik fonksiyonlar
SIN(PI/2)                       ' Sinüs: 1
COS(0)                          ' Kosinüs: 1
TAN(PI/4)                       ' Tanjant: 1
ATN(1)                          ' Arctanjant: PI/4
SIND(90)                        ' Derece cinsinden sinüs: 1
COSD(0)                         ' Derece cinsinden kosinüs: 1
TAND(45)                        ' Derece cinsinden tanjant: 1

' Hiperbolik fonksiyonlar
SINH(0)                         ' Hiperbolik sinüs: 0
COSH(0)                         ' Hiperbolik kosinüs: 1
TANH(0)                         ' Hiperbolik tanjant: 0
ASINH(0)                        ' Ters hiperbolik sinüs
ACOSH(1)                        ' Ters hiperbolik kosinüs
ATANH(0)                        ' Ters hiperbolik tanjant

' Logaritma ve üstel
LOG(10)                         ' Doğal logaritma
EXP(1)                          ' e üssü: 2.718...

' Sabitler
PI                              ' Pi sayısı: 3.14159...
E                               ' Euler sayısı: 2.718...
```

### İstatistiksel Fonksiyonlar
```basic
DIM data AS ARRAY
data = [1, 2, 3, 4, 5]

MEAN(data)                      ' Ortalama
MEDIAN(data)                    ' Medyan
MODE(data)                      ' Mod
STD(data)                       ' Standart sapma
VAR(data)                       ' Varyans
SUM(data)                       ' Toplam
PROD(data)                      ' Çarpım
PERCENTILE(data, 50)            ' Yüzdelik dilim
QUANTILE(data, 0.5)             ' Kantil

' İki değişkenli istatistikler
DIM x AS ARRAY, y AS ARRAY
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

CORR(x, y)                      ' Korelasyon
COV(x, y)                       ' Kovaryans
REGRESS(x, y)                   ' Doğrusal regresyon

' Hipotez testleri
TTEST(group1, group2)           ' T-testi
CHISQUARE(observed)             ' Ki-kare testi
ANOVA(group1, group2, group3)   ' ANOVA
```

### NumPy Array İşlemleri (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' Array oluşturma
ZEROS(5)                        ' 5 elemanlı sıfır array
ONES(3)                         ' 3 elemanlı bir array
FULL(4, 7)                      ' 4 elemanlı, 7 değerli array
EYE(3)                          ' 3x3 birim matris
LINSPACE(0, 10, 11)             ' 0'dan 10'a 11 eşit parça
ARANGE(0, 10, 2)                ' 0'dan 10'a 2'şer artırarak

' Array işlemleri
CONCATENATE(arr1, arr2)         ' Array birleştirme
STACK(arr1, arr2)               ' Array yığınlama
VSTACK(arr1, arr2)              ' Dikey yığınlama
HSTACK(arr1, arr2)              ' Yatay yığınlama
DOT(arr1, arr2)                 ' Nokta çarpımı
CROSS(arr1, arr2)               ' Çapraz çarpım

' Matris işlemleri (YENİ ÖZELLİK!)
DIM matrix(3, 3) AS DOUBLE
matrix(0, 0) = 1: matrix(0, 1) = 2: matrix(0, 2) = 3
matrix(1, 0) = 4: matrix(1, 1) = 5: matrix(1, 2) = 6
matrix(2, 0) = 7: matrix(2, 1) = 8: matrix(2, 2) = 9

DIM transposed AS ARRAY = TRANSPOSE(matrix)    ' Transpoz
DIM inverted AS ARRAY = INV(matrix)            ' Ters matris
DIM diagonal AS ARRAY = DIAG(matrix)           ' Köşegen elemanları
NORM(vector)                                   ' Norm hesaplama
SOLVE(A, b)                                    ' Ax=b çözümü

' Şekil değiştirme
RESHAPE(arr, (3, 4))            ' 3x4 şeklinde yeniden şekillendir
FLIP(arr)                       ' Ters çevir
ROLL(arr, 2)                    ' 2 pozisyon kaydır

' Örnek kullanım
DIM A AS ARRAY = [[1, 2], [3, 4]]
DIM B AS ARRAY = [[5, 6], [7, 8]]
DIM result AS ARRAY = DOT(A, B)   ' Matrix çarpımı
PRINT "Matrix çarpım sonucu:", result
```

### Pandas DataFrame İşlemleri (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' DataFrame oluşturma ve temel işlemler
DIM df AS DATAFRAME
df = {"name": ["Ali", "Veli"], "age": [25, 30]}

' Block syntax ile DataFrame oluşturma (YENİ!)
DATAFRAME employee_data
"name": ["Ahmet", "Mehmet", "Ayşe", "Fatma"]
"age": [25, 30, 28, 32]
"department": ["IT", "HR", "IT", "Finance"]
"salary": [5000, 4500, 5500, 4800]

END DATAFRAME

' DataFrame değişkeni tanımlama
DIM df AS DATAFRAME
df = sales_data

' DataFrame işlemleri
PRINT "İlk 3 satır:"
HEAD(df, 3)

PRINT "Son 2 satır:" 
TAIL(df, 2)

PRINT "Özet istatistikler:"
DESCRIBE(df)

' DataFrame sıralama
DIM sorted_df AS DATAFRAME = SORT(df, "price")

' Gruplama işlemleri
DIM grouped AS DATAFRAME = GROUPBY(df, "category")

' Filtreleme
DIM filtered AS DATAFRAME = FILTER(df, "price > 100")

' Pivot tablo
DIM pivot AS DATAFRAME = PIVOT_TABLE(df, "category", "price")

' DataFrame birleştirme
DATAFRAME df2
"product": ["Monitor", "Speaker"]
"price": [800, 200]
"quantity": [15, 30]
END DATAFRAME

DIM merged AS DATAFRAME = MERGE(df, df2, "product")
END DATAFRAME

' DataFrame işlemleri (GELİŞTİRİLMİŞ!)
DESCRIBE(df)                    ' Özet istatistikler
HEAD(df, 5)                     ' İlk 5 satır
TAIL(df, 3)                     ' Son 3 satır
SORT(df, "age")                 ' Sütuna göre sırala

' Gelişmiş DataFrame işlemleri (YENİ!)
DIM filtered_df AS DATAFRAME = FILTER(df, "age > 28")     ' Filtreleme
DIM grouped_df AS DATAFRAME = GROUPBY(df, "department")   ' Gruplama  
DIM pivot AS DATAFRAME = PIVOT_TABLE(df, "department", "salary")  ' Pivot

' Veri temizleme
FILLNA(df, 0)                   ' NaN değerleri 0 ile doldur
DROPNA(df)                      ' NaN değerleri kaldır
ASTYPE(df, "int")               ' Tip dönüştürme

' Veri dönüştürme
MELT(df)                        ' Wide'dan long'a dönüştür
CROSSTAB(df.col1, df.col2)      ' Çapraz tablo

' Zaman serisi
TO_DATETIME(df.date_col)        ' Tarih dönüştürme
RESAMPLE(df, "M")               ' Aylık örnekleme
ROLLING(df, 3)                  ' Hareketli ortalama penceresi
SHIFT(df, 1)                    ' 1 periode kaydır
DIFF(df)                        ' Fark hesaplama
PCT_CHANGE(df)                  ' Yüzde değişim

' Veri birleştirme (GELİŞTİRİLMİŞ!)
DIM df2 AS DATAFRAME
DATAFRAME df2
"name": ["Ahmet", "Mehmet"]  
"bonus": [1000, 1200]
END DATAFRAME

DIM merged AS DATAFRAME = MERGE(df, df2, "name")    ' DataFrame birleştirme

' Örnek kullanım
PRINT "Departmanlara göre ortalama maaş:"
DIM salary_by_dept AS DATAFRAME = GROUPBY(employee_data, "department")
PRINT salary_by_dept
```

### Dosya İşlemleri
```basic
' Dosya durumu
EOF(file_handle)                ' Dosya sonu kontrolü
LOC(file_handle)                ' Dosya pozisyonu
LOF(file_handle)                ' Dosya boyutu
FREEFILE()                      ' Boş dosya numarası

' Dosya okuma
INPUT$(bytes, file_handle)      ' Belirtilen byte okuma
DIR$("C:\folder")               ' Dizin listeleme
ISDIR("C:\folder")              ' Dizin kontrolü

' Binary veri
MKI$(123)                       ' Integer'i binary string'e
MKS$(3.14)                      ' Single'ı binary string'e
MKD$(3.14159)                   ' Double'ı binary string'e
```

### PDF İşlemleri
```basic
' PDF okuma
PDF_READ_TEXT("document.pdf")           ' PDF'den metin çıkarma
PDF_EXTRACT_TABLES("document.pdf")      ' PDF'den tablo çıkarma
```

### Web İşlemleri
```basic
' Web sayfası okuma
WEB_GET("https://example.com")           ' Web sayfası içeriği alma
```

### Tarih ve Saat
```basic
DATE$                           ' Bugünün tarihi: "08-13-2025"
TIME$                           ' Şu anki saat: "14:30:15"
TIMER                           ' Zaman damgası (Unix timestamp)
```

### Sistem Fonksiyonları
```basic
ENVIRON$("PATH")                ' Ortam değişkeni
COMMAND$                        ' Komut satırı argümanları
MEMORY_USAGE()                  ' Bellek kullanımı (MB)
CPU_COUNT()                     ' İşlemci sayısı
THREAD_COUNT()                  ' Aktif thread sayısı
CURRENT_THREAD()                ' Mevcut thread ID
```

### Utility Fonksiyonları
```basic
' Tip kontrolü
TYPE_OF(variable)               ' Değişken tipini döndür
SIZEOF(variable)                ' Değişken boyutu
ADDR(variable)                  ' Bellek adresi

' Sayı sistemi dönüştürme
BIN(15)                         ' Binary: "0b1111"
HEX(255)                        ' Hexadecimal: "0xff"
OCT(8)                          ' Octal: "0o10"

' Random işlemler
RND()                           ' 0-1 arası random
```

---

## 10. 🏷️ Etiketler ve Program Akışı

Etiketler ve program akış kontrolleri, geleneksel BASIC programlamanın önemli parçalarıdır. pdsXv11g, klasik GOTO ve GOSUB komutlarını modern hata yönetimi ile birlikte destekler. Bu özellikler sayesinde programın akışını kontrol edebilir, alt rutinler oluşturabilir ve klasik BASIC tarzı programlama yapabilirsiniz.

**Program Akış Komutları:**
- `GOTO`: Belirtilen etikete dallanma
- `GOSUB`: Alt rutine dallanma ve geri dönüş
- `RETURN`: GOSUB'dan ana programa dönüş
- `ON ERROR GOTO`: Hata durumunda dallanma

**Etiket Özellikleri:**
- **Etiket Tanımı**: `EtiketAdı:` formatında
- **Global Erişim**: Program boyunca erişilebilir
- **Hata Yönetimi**: ON ERROR ile hata yakalama

**Syntax:**
```basic
EtiketAdı:                       ' Etiket tanımı
    komutlar...

GOTO EtiketAdı                   ' Etikete git
GOSUB AltRutinEtiketi           ' Alt rutine git
RETURN                          ' GOSUB'dan geri dön

ON ERROR GOTO HataEtiketi       ' Hata durumunda git
```

### GOTO ve GOSUB
```basic
GOTO MyLabel                    ' Etikete git

GOSUB MySubroutine             ' Alt rutine git
PRINT "Ana program devam ediyor"
END

MyLabel:
    PRINT "Etiket noktası"
    
MySubroutine:
    PRINT "Alt rutin çalışıyor"
    RETURN                      ' GOSUB'a geri dön
```

### Hata İşleme
```basic
ON ERROR GOTO ErrorHandler     ' Hata durumunda etikete git

TRY operation CATCH err DO PRINT "Hata:", err

' Etiketli hata işleme
ErrorHandler:
    PRINT "Bir hata oluştu!"
    RESUME NEXT                 ' Hata sonrası devam et
```

---

## 11. 🧩 İleri Özellikler

İleri özellikler, pdsXv11g'yi güçlü kılan modern programlama yapılarıdır. Bu bölümde karmaşık veri yapıları, nesne yönelimli programlama simülasyonları, asenkron işlemler ve sistem seviyesi özellikler bulunur. Bu özellikler sayesinde büyük ve karmaşık projelerde bile organize kod yazabilirsiniz.

**İleri Özellik Kategorileri:**
- **STRUCT**: Karmaşık veri tipleri ve iç içe yapılar
- **UNION**: Aynı bellek alanını farklı tiplerle kullanma
- **ENUM**: Sabit grupları ve enum blok syntax'ı
- **Class Simülasyonu**: Nesne yönelimli programlama
- **Memory Management**: Bellek tahsisi ve yönetimi
- **Async İşlemler**: Asenkron programlama ve threading
- **HTTP API**: Web servisleri ve ağ işlemleri
- **Performance Tools**: Sistem izleme ve optimizasyon

**Gelişmiş Programlama Özellikleri:**
- **İç İçe Yapılar**: `person.address.city` erişimi (YENİ)
- **Otomatik İnit**: Nested struct'lar otomatik başlatılır
- **Type Safety**: Güvenli tip sistemi
- **Modern Syntax**: Lambda ve block syntax desteği

**Syntax Örnekleri:**
```basic
TYPE KarmaşıkVeri                        ' Struct tanımı
    alan1 AS TIP
    alan2 AS STRUCT                      ' İç içe struct
END TYPE

ENUM Değerler                           ' Enum blok syntax
SABIT1 = değer
SABIT2 = değer
END ENUM

DATAFRAME veri                          ' DataFrame blok syntax
"alan": [değerler]
END DATAFRAME
```

### Struct Tanımlama (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' Basit struct
TYPE Person
    name AS STRING
    age AS INTEGER
    salary AS DOUBLE
END TYPE

' Struct kullanımı
DIM employee AS Person
employee.name = "Ahmet"
employee.age = 30
employee.salary = 5000.0

' İç içe (Nested) struct yapıları - YENİ ÖZELLİK!
TYPE Address
    street AS STRING
    city AS STRING
    country AS STRING
END TYPE

TYPE PersonWithAddress
    name AS STRING
    age AS INTEGER
    address AS Address    ' İç içe struct
END TYPE

' İç içe struct kullanımı
DIM person AS PersonWithAddress
person.name = "Mehmet"
person.age = 25
person.address.street = "Atatürk Caddesi"
person.address.city = "İstanbul" 
person.address.country = "Türkiye"

PRINT person.address.city  ' Çıktı: İstanbul

' Struct arrays
DIM employees(10) AS Person
employees(0).name = "Ali"
employees(0).age = 28
employees(1).name = "Veli"
employees(1).age = 32

' Struct initialization helper (otomatik)
' pdsXv11g otomatik olarak nested struct'ları initialize eder
```

### Union Tanımlama (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' Basit union
UNION Data
    int_val AS INTEGER
    float_val AS DOUBLE
    str_val AS STRING
END UNION

' Union kullanımı
DIM my_data AS Data
my_data.int_val = 42
PRINT my_data.int_val    ' 42

' Farklı tipteki değeri ata
my_data.str_val = "Hello"
PRINT my_data.str_val    ' Hello

' İç içe union yapıları - YENİ ÖZELLİK!
UNION Address
    full_address AS STRING
    coordinates AS CoordType
END UNION

TYPE CoordType  
    x AS DOUBLE
    y AS DOUBLE
END TYPE

TYPE LocationData
    name AS STRING
    location AS Address    ' İç içe union
END TYPE

DIM place AS LocationData
place.name = "Merkez"
place.location.full_address = "İstanbul, Türkiye"
```

### Enum Simülasyonu (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' Sabitler tanımlama (eski yöntem)
LET MONDAY = 1
LET TUESDAY = 2
LET WEDNESDAY = 3

' Modern ENUM block syntax - YENİ ÖZELLİK!
ENUM Days
MONDAY = 1
TUESDAY = 2  
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7
END ENUM

' ENUM kullanımı
DIM today AS INTEGER = Days.MONDAY
SELECT CASE today
    CASE Days.MONDAY
        PRINT "Pazartesi"
    CASE Days.TUESDAY  
        PRINT "Salı"
    CASE Days.WEDNESDAY
        PRINT "Çarşamba"
END SELECT

' String ENUM'lar
ENUM Status
PENDING = "BEKLIYOR"
PROCESSING = "İŞLENİYOR" 
COMPLETED = "TAMAMLANDI"
FAILED = "BAŞARISIZ"
END ENUM

DIM task_status AS STRING = Status.PENDING
PRINT "Görev durumu:", task_status  ' Çıktı: BEKLIYOR

' Renk ENUM'ları
ENUM Colors
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
BLACK = "#000000"
WHITE = "#FFFFFF"
END ENUM

DIM bg_color AS STRING = Colors.BLUE
PRINT "Arka plan rengi:", bg_color  ' #0000FF
```

### Class Tanımlama
```basic
CLASS Calculator
    STATIC version AS STRING = "1.0"
    
    SUB add(a, b)
        RETURN a + b
    END SUB
    
    PRIVATE SUB internal_calc()
        ' Private method
    END SUB
END CLASS

' Class kullanımı
DIM calc AS Calculator
PRINT calc.add(5, 3)
```

### Memory Management
```basic
' Bellek tahsisi
DIM ptr AS POINTER
ptr = NEW(100)                  ' 100 byte tahsis et

' Bellek serbest bırakma
DELETE(ptr)
```

### Async İşlemler (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' Async bekleme
ASYNC_WAIT(2.5)                 ' 2.5 saniye bekle

' Sleep/Wait işlemleri
SLEEP(1)                        ' 1 saniye bekle (blocking)
WAIT(0.5)                       ' 0.5 saniye bekle

' Timer işlemleri
DIM start_time AS DOUBLE = TIMER
' ... işlemler ...
DIM elapsed AS DOUBLE = TIMER - start_time
PRINT "Geçen süre:", elapsed, "saniye"

' Performance monitoring
PERFORMANCE                     ' Bellek ve CPU kullanımı göster

' Thread ve async bilgileri
PRINT "CPU sayısı:", CPU_COUNT()
PRINT "Thread sayısı:", THREAD_COUNT()  
PRINT "Aktif thread ID:", CURRENT_THREAD()
```

### HTTP API Çağrıları
```basic
' HTTP GET
CALL API::GET "https://api.example.com/data" TO response

' HTTP POST
CALL API::POST "https://api.example.com/create" DATA {"name": "test"} TO result

' HTTP PUT
CALL API::PUT "https://api.example.com/update/1" DATA {"name": "updated"} TO result

' HTTP DELETE
CALL API::DELETE "https://api.example.com/delete/1" TO result

' Dosya indirme
HTTP_DOWNLOAD "https://example.com/file.zip" TO "local_file.zip"

' HTTP durum kontrolü
HTTP_STATUS(200)                ' HTTP durum kodu kontrolü

' HTTP header ayarlama
HTTP_SET_HEADER "Authorization", "Bearer token123"
```

### Core Library Fonksiyonları
```basic
' Fonksiyonel programlama
MAP(function, array)            ' Her elemana fonksiyon uygula
FILTER(condition, array)        ' Koşula uyan elemanları filtrele
REDUCE(function, array, initial) ' Array'i tek değere indirge

' Dosya ve sistem
EXISTS("file.txt")              ' Dosya varlık kontrolü
MKDIR("new_folder")             ' Klasör oluştur
COPY_FILE("src.txt", "dst.txt") ' Dosya kopyala
MOVE_FILE("old.txt", "new.txt") ' Dosya taşı
DELETE_FILE("temp.txt")         ' Dosya sil
LIST_DIR("C:\folder")           ' Dizin listeleme

' JSON işlemleri
WRITE_JSON(data, "data.json")   ' JSON dosyası yaz
READ_JSON("data.json")          ' JSON dosyası oku

' Veri yapıları
STACK()                         ' Yığın oluştur
PUSH(stack_id, item)            ' Yığına eleman ekle
POP(stack_id)                   ' Yığından eleman çıkar
QUEUE()                         ' Kuyruk oluştur
ENQUEUE(queue_id, item)         ' Kuyruğa eleman ekle
DEQUEUE(queue_id)               ' Kuyruktan eleman çıkar

' Zaman işlemleri
TIME_NOW()                      ' Şu anki tarih-saat
DATE_NOW()                      ' Şu anki tarih
TIMER()                         ' Unix timestamp
DATE_DIFF("2025-01-01", "2025-12-31", "days") ' Tarih farkı

' Utility
SLEEP(2)                        ' 2 saniye bekle
ASSERT(condition, "message")    ' İddia kontrolü
LOG("message", "INFO", "log.txt") ' Log yazma
IFTHEN(condition, val1, val2)   ' Ternary operator
```

---

## 12. 🎯 Örnekler

### Örnek 1: Temel Program
```basic
PRINT "=== Basit Hesap Makinesi ==="

DIM num1 AS DOUBLE
DIM num2 AS DOUBLE
DIM operation AS STRING

INPUT "İlk sayı: ", num1
INPUT "İkinci sayı: ", num2
INPUT "İşlem (+, -, *, /): ", operation

SELECT CASE operation
    CASE "+"
        PRINT "Sonuç:", num1 + num2
    CASE "-"
        PRINT "Sonuç:", num1 - num2
    CASE "*"
        PRINT "Sonuç:", num1 * num2
    CASE "/"
        IF num2 <> 0 THEN
            PRINT "Sonuç:", num1 / num2
        ELSE
            PRINT "Hata: Sıfıra bölme!"
        END IF
    CASE ELSE
        PRINT "Geçersiz işlem!"
END SELECT
```

### Örnek 2: Fibonacci Serisi
```basic
DEF FUNCTION fibonacci(n)
    IF n <= 1 THEN
        RETURN n
    ELSE
        RETURN fibonacci(n-1) + fibonacci(n-2)
    END IF
END FUNCTION

PRINT "Fibonacci Serisi (İlk 10 terim):"
FOR i = 0 TO 9
    PRINT "F(" + STR$(i) + ") =", fibonacci(i)
NEXT i
```

### Örnek 3: Veri Analizi
```basic
DIM sales_data AS ARRAY
sales_data = [120, 150, 130, 180, 200, 175, 160]

PRINT "Satış Veri Analizi:"
PRINT "=================="
PRINT "Toplam satış:", SUM(sales_data)
PRINT "Ortalama:", ROUND(MEAN(sales_data), 2)
PRINT "Maksimum:", MAX(sales_data)
PRINT "Minimum:", MIN(sales_data)
PRINT "Standart sapma:", ROUND(STD(sales_data), 2)
PRINT "Medyan:", MEDIAN(sales_data)
```

### Örnek 4: Dosya İşlemleri
```basic
DIM file_content AS STRING

' Dosya varlığını kontrol et
IF EXISTS("data.txt") THEN
    PRINT "Dosya mevcut"
ELSE
    PRINT "Dosya bulunamadı"
END IF

' Dizin listele
DIM files AS ARRAY
files = LIST_DIR("C:\temp")
FOR i = 0 TO LEN(files) - 1
    PRINT "Dosya:", files(i)
NEXT i
```

### Örnek 5: Web API Kullanımı
```basic
DIM response AS STRING

' Web sayfası içeriği al
response = WEB_GET("https://httpbin.org/json")
PRINT "API Yanıtı:", response

' HTTP API çağrısı
CALL API::GET "https://jsonplaceholder.typicode.com/posts/1" TO post_data
PRINT "Post başlığı:", post_data
```

---

### Debug ve Trace Modları

### Debug Komutları
```basic
DEBUG ON                        ' Debug modunu aç
DEBUG OFF                       ' Debug modunu kapat
TRACE ON                        ' Trace modunu aç
TRACE OFF                       ' Trace modunu kapat
STEP DEBUG                      ' Adım adım debug
```

### Performance İzleme
```basic
PERFORMANCE                     ' Bellek ve CPU kullanımı göster
```

---

## 13. 🌐 Modül Sistemi

### Modül İmport Etme
```basic
IMPORT "mymodule.libx"          ' Modül yükle
IMPORT "utils.basx" AS utilities ' Takma ad ile yükle
```

### Desteklenen Dosya Uzantıları
- `.basx` - Ana program dosyaları
- `.libx` - Kütüphane dosyaları
- `.hx` - Header dosyaları
- `.hz` - Sıkıştırılmış dosyalar

---

## 14. ⚡ Operatörler

### Aritmetik Operatörler
```basic
+  -  *  /  MOD                 ' Temel aritmetik
++ --                           ' Artırma/azaltma
+= -= *= /= %=                  ' Bileşik atama
```

### Karşılaştırma Operatörleri
```basic
= <> < > <= >=                  ' Karşılaştırma
```

### Mantıksal Operatörler
```basic
AND OR XOR NOT                  ' Mantıksal
```

### Bitwise Operatörler
```basic
& | ^ ~                         ' Bitwise işlemler
<< >>                           ' Kaydırma
&= |= ^= <<= >>=                ' Bileşik bitwise atama
```

---

## 15. 🛠️ Komut Satırı Seçenekleri

```bash
python pdsXv11g.py [dosya] [seçenekler]

Seçenekler:
  -i, --interactive     Etkileşimli REPL modu
  --setup-venv         Sanal ortam kurulumu
  --check-deps         Bağımlılık kontrolü
  --debug              Debug modu
  --trace              Trace modu
  --no-venv            Sanal ortam kontrolünü atla
```

---

## 16. 📊 Veri Yapıları

Veri yapıları, programlarınızda verileri organize etmek ve verimli bir şekilde işlemek için kullanılan temel araçlardır. pdsXv11g, geleneksel dizilerden modern koleksiyonlara kadar geniş bir veri yapısı yelpazesi sunar. Özellikle yeni eklenen string array desteği ve 20+ string array fonksiyonu ile metin tabanlı veriler üzerinde güçlü işlemler yapabilirsiniz.

**Temel Veri Yapıları:**
- **LIST**: Dinamik listeler (sıralı, mükerrer öğe kabul eder)
- **DICT**: Sözlük/Dictionary (anahtar-değer çiftleri)
- **SET**: Küme (benzersiz öğeler, sırasız)
- **TUPLE**: Tuple (sabit boyutlu, değiştirilemez)
- **ARRAY**: Genel dizi (en esnek koleksiyon)
- **STACK**: Yığın (LIFO - Last In, First Out)
- **QUEUE**: Kuyruk (FIFO - First In, First Out)

**String Array Özellikleri (YENİ):**
- **Çok Boyutlu**: 1D, 2D, 3D string dizileri
- **20+ Fonksiyon**: STRARRAY, STRGET, STRSET, STRLEN, STRCAT vb.
- **Toplu İşlemler**: Tüm elemanlar üzerinde aynı anda işlem
- **Pattern Matching**: Regex desteği ile güçlü arama

**Syntax Örnekleri:**
```basic
DIM my_list AS LIST = [1, 2, 3]           ' Liste
DIM my_dict AS DICT = {"key": "value"}     ' Sözlük
DIM cities(5) AS STRING                    ' String array
DIM matrix(3, 4) AS STRING                 ' 2D string array
DIM fruits AS ARRAY = STRARRAY(10, "")     ' String array fonksiyonu
```

### Listeler
```basic
DIM my_list AS LIST
my_list = [1, 2, 3]
INSERT(my_list, 4)              ' Eleman ekle
REMOVE(my_list, 0)              ' İndeksteki elemanı sil
CLEAR(my_list)                  ' Tümünü temizle

' String Array Tanımlama (YENİ ÖZELLİK - pdsXv11g)
DIM cities(5) AS STRING             ' 5 elemanlı string array
cities(0) = "İstanbul"
cities(1) = "Ankara" 
cities(2) = "İzmir"

' Çok boyutlu string arrays (YENİ)
DIM regions(3, 4) AS STRING         ' 2D string array
regions(0, 0) = "Marmara"
regions(1, 2) = "Akdeniz"

DIM countries(2, 3, 4) AS STRING    ' 3D string array
countries(0, 1, 2) = "Türkiye"

### String Array Functions - Gelişmiş String Array İşlemleri (YENİ - pdsXv11g)
```basic
' 20+ String Array Fonksiyonu

' 1. String Array Oluşturma
DIM str_arr AS ARRAY = STRARRAY(5, "default")    ' 5 elemanlı, "default" değerli array

' 2. Element Erişimi
DIM value AS STRING = STRGET(str_arr, 0)         ' 0. indeksteki değeri al
STRSET(str_arr, 0, "yeni değer")                 ' 0. indekse değer ata

' 3. Length İşlemleri
DIM lengths AS ARRAY = STRLEN(str_arr)           ' Her elemanın uzunluğunu array olarak döndür
DIM single_len AS INTEGER = STRLEN("test")       ' Tek string'in uzunluğu

' 4. Birleştirme İşlemleri
DIM arr1 AS ARRAY = ["hello", "world"]
DIM arr2 AS ARRAY = ["foo", "bar"]
DIM combined AS ARRAY = STRCAT(arr1, arr2)      ' Array birleştirme

' 5. Split ve Join İşlemleri
DIM text AS STRING = "apple,banana,cherry"
DIM fruits AS ARRAY = STRSPLIT(text, ",")       ' String'i array'e böl
DIM joined AS STRING = STRJOIN(fruits, "|")     ' Array'i string'e birleştir

' 6. Arama İşlemleri
DIM cities AS ARRAY = ["İstanbul", "Ankara", "İzmir", "Antalya"]
DIM indices AS ARRAY = STRFIND(cities, "An")    ' "An" içeren elemanların indeksleri
' Sonuç: [1, 3] (Ankara ve Antalya)

' 7. Replace İşlemleri
DIM replaced AS ARRAY = STRREPLACE(cities, "a", "@")  ' Tüm "a"ları "@" ile değiştir

' 8. Karşılaştırma İşlemleri
DIM arr1 AS ARRAY = ["test", "hello", "world"]
DIM arr2 AS ARRAY = ["test", "hi", "world"]
DIM comparison AS ARRAY = STRCOMPARE(arr1, arr2)     ' [TRUE, FALSE, TRUE]

' 9. Trim İşlemleri
DIM messy AS ARRAY = ["  hello  ", " world ", "test"]
DIM cleaned AS ARRAY = STRTRIM(messy)                ' Boşlukları temizle

' 10. Padding İşlemleri
DIM padded AS ARRAY = STRPAD(cities, 15, "_")        ' 15 karakter genişliğinde, "_" ile doldur

' 11. Substring İşlemleri
DIM substrs AS ARRAY = STRSUBSTR(cities, 0, 3)      ' Her elemanın ilk 3 karakteri

' 12. Reverse İşlemleri
DIM reversed AS ARRAY = STRREVERSE(cities)           ' Her elemanı ters çevir

' 13. Pattern Matching (Regex desteği!)
DIM emails AS ARRAY = ["test@gmail.com", "invalid", "user@yahoo.com"]
DIM valid AS ARRAY = STRMATCH(emails, r".*@.*\.com") ' Email pattern kontrolü

' 14. Count İşlemleri
DIM texts AS ARRAY = ["hello world", "hello universe", "hi there"]
DIM counts AS ARRAY = STRCOUNT(texts, "hello")       ' Her elemanda "hello" sayısı

' 15-18. Case İşlemleri
DIM mixed AS ARRAY = ["Hello World", "BASIC Language", "test string"]
DIM lower AS ARRAY = STRLOWER(mixed)                 ' Küçük harf
DIM upper AS ARRAY = STRUPPER(mixed)                 ' Büyük harf
DIM title AS ARRAY = STRTITLE(mixed)                 ' Title Case

' 19-20. Karakter Değiştirme
DIM swapped AS ARRAY = STRSWAP(cities, "a", "e")     ' "a"ları "e" ile değiştir

' Practical Örnek: Log dosyası işleme
DIM log_lines AS ARRAY = [
    "INFO: User login successful",
    "ERROR: Database connection failed", 
    "WARNING: Memory usage high",
    "INFO: Request processed"
]

' ERROR içeren satırları bul
DIM error_indices AS ARRAY = STRFIND(log_lines, "ERROR")
PRINT "Hata satırları:", error_indices

' Log levels'ı extract et
DIM levels AS ARRAY = STRSUBSTR(log_lines, 0, 7)    ' İlk 7 karakter (log level)
DIM clean_levels AS ARRAY = STRTRIM(levels)         ' Temizle

PRINT "Log levels:", clean_levels
```
```

LIST my_list = [1,2,4,5]

LIST my_list
adana
adiyaman
afyon
END LIST


### Sözlükler
```basic
DIM my_dict AS DICT
my_dict = {"key1": "value1"}
INSERT(my_dict, "value2", KEY="key2")
REMOVE(my_dict, KEY="key1")
KEYS(my_dict)                   ' Anahtarları listele
```

```
DICT my_dict
key:value
key:value
key:value
END DICT
```

### DataFrame İşlemleri (GELİŞTİRİLMİŞ - pdsXv11g)
```basic
' DataFrame oluşturma - Block syntax (YENİ!)
DATAFRAME sales_data
"product": ["Laptop", "Mouse", "Keyboard"]
"price": [1500, 50, 150]
"quantity": [10, 50, 25]
"category": ["Electronics", "Accessory", "Accessory"]
END DATAFRAME

' DataFrame değişkeni tanımlama
DIM df AS DATAFRAME
df = sales_data

' DataFrame işlemleri
PRINT "İlk 3 satır:"
HEAD(df, 3)

PRINT "Son 2 satır:" 
TAIL(df, 2)

PRINT "Özet istatistikler:"
DESCRIBE(df)

' DataFrame sıralama
DIM sorted_df AS DATAFRAME = SORT(df, "price")

' Gruplama işlemleri
DIM grouped AS DATAFRAME = GROUPBY(df, "category")

' Filtreleme
DIM filtered AS DATAFRAME = FILTER(df, "price > 100")

' Pivot tablo
DIM pivot AS DATAFRAME = PIVOT_TABLE(df, "category", "price")

' DataFrame birleştirme
DATAFRAME df2
"product": ["Monitor", "Speaker"]
"price": [800, 200]
"quantity": [15, 30]
END DATAFRAME

DIM merged AS DATAFRAME = MERGE(df, df2, "product")
```

---

DATAFRAME
my_list as LIST
my_dict as DICT

END DATAFRAME


## 17. ⌨️ Klavye Girişi

Klavye girişi, etkileşimli uygulamalar ve oyunlar geliştirirken kritik öneme sahiptir. pdsXv11g, hem blocking hem de non-blocking klavye girişi desteği sunar. Bu özellikler sayesinde gerçek zamanlı oyunlar, menü sistemleri ve etkileşimli uygulamalar geliştirebilirsiniz.

**Klavye Giriş Türleri:**
- **KEY()**: Non-blocking tuş kontrolü (anında kontrol, beklemez)
- **GETKEY()**: Blocking tuş bekleme (tuş basılmasını bekler)
- **INPUT**: Tam metin girişi (satır sonu bekler)

**Desteklenen Tuş Türleri:**
- **Normal Tuşlar**: A-Z, 0-9, boşluk, özel karakterler
- **Özel Tuşlar**: Enter, Escape, yön tuşları, F1-F12
- **Kombinasyonlar**: Çoklu tuş seçenekleri ("A,B,C")

**Kullanım Senaryoları:**
- **Oyunlar**: Gerçek zamanlı karakter kontrolü
- **Menüler**: Seçenek navigasyonu
- **İnteraktif Uygulamalar**: Kullanıcı etkileşimi
- **System Tools**: Sistem yönetim arayüzleri

**Syntax:**
```basic
DIM tuş AS STRING = KEY()                    ' Non-blocking kontrol
DIM tuş AS STRING = GETKEY()                 ' Herhangi bir tuş bekle
DIM tuş AS STRING = GETKEY("A,B,C")          ' Belirli tuşları bekle
DIM tuş AS STRING = GETKEY("<ENTER>,<ESC>")  ' Özel tuşları bekle
```

### KEY() - Non-blocking Tuş Kontrolü
```basic
' Herhangi bir tuşa basılmış mı kontrol et (non-blocking)
DIM pressed_key AS STRING
pressed_key = KEY()
IF pressed_key <> "" THEN
    PRINT "Basılan tuş: " + pressed_key
END IF

' Belirli bir tuş kontrolü
IF KEY("A") THEN
    PRINT "A tuşuna basıldı!"
END IF

' Özel tuşlar
IF KEY("<YUKARIOK>") THEN
    PRINT "Yukarı ok tuşuna basıldı!"
END IF
```

### GETKEY() - Tuş Bekle
```basic
' Herhangi bir tuşa basılmasını bekle
DIM key AS STRING
key = GETKEY()
PRINT "Basılan tuş: " + key

' Belirli tuşları bekle
key = GETKEY("A,B,C")
PRINT "A, B veya C tuşlarından birine basıldı: " + key

' Özel tuşları bekle
key = GETKEY("<ENTER>,<ESC>")
PRINT "Enter veya ESC basıldı: " + key

' Yön tuşlarını bekle
key = GETKEY("<YUKARIOK>,<ASAGIOK>,<SOLOK>,<SAGOK>")
SELECT CASE key
    CASE "<YUKARIOK>"
        PRINT "Yukarı"
    CASE "<ASAGIOK>"
        PRINT "Aşağı"
    CASE "<SOLOK>"
        PRINT "Sol"
    CASE "<SAGOK>"
        PRINT "Sağ"
END SELECT
```

### Desteklenen Özel Tuşlar
- `<YUKARIOK>` - Yukarı ok tuşu
- `<ASAGIOK>` - Aşağı ok tuşu
- `<SOLOK>` - Sol ok tuşu  
- `<SAGOK>` - Sağ ok tuşu
- `<ENTER>` - Enter tuşu
- `<ESC>` - Escape tuşu
- `<SPACE>` - Boşluk tuşu

---

## 18. 💾 REPL ve Dosya İşlemleri

REPL (Read-Eval-Print-Loop) modu, pdsXv11g'nin etkileşimli programlama ortamıdır. Bu mod sayesinde kodlarınızı satır satır yazabilir, anında test edebilir ve hızlı prototipleme yapabilirsiniz. REPL modu, özellikle öğrenim ve hızlı kod deneme için idealdir.

**REPL Özellikleri:**
- **Etkileşimli Kodlama**: Kodları anında yazıp çalıştırma
- **Satır Numaraları**: Geleneksel BASIC tarzı satır numarası
- **Program Yönetimi**: SAVE, LOAD, LIST komutları
- **Hata Ayıklama**: EDIT, DELETE ile kod düzenleme
- **Çok Satırlı Mod**: Uzun kodlar için blok girişi

**REPL Komutları:**
- **LIST**: Mevcut programı listele
- **RUN**: Programı çalıştır
- **SAVE/LOAD**: Program kaydetme/yükleme
- **EDIT/DELETE**: Kod düzenleme
- **NEW**: Programı temizle
- **EXIT**: REPL'den çıkış

**Dosya Formatları:**
- **.basx**: Ana program dosyaları
- **.libx**: Kütüphane dosyaları
- **.pdsx**: REPL program dosyaları

**Avantajlar:**
- **Hızlı Test**: Kodları anında deneme
- **Öğrenim**: Adım adım kod yazma
- **Debug**: Hatalı kodları hızla düzeltme
- **Prototipleme**: Fikirları hızla geliştirme

### REPL (Read-Eval-Print-Loop) Modu
```basic
REPL                    ' REPL modunu başlat
```

REPL modu komutları:
- `LIST` - Mevcut programı listele
- `NEW` - Programı temizle
- `EDIT <satır_no>` - Belirli satırı düzenle
- `DELETE <satır_no>` - Belirli satırı sil
- `RUN` - Mevcut programı çalıştır
- `SAVE <dosya>` - Programı kaydet
- `LOAD <dosya>` - Program yükle
- `EXIT` - REPL'den çık

### Çok Satırlı Mod
```basic
REPL                    ' Çok satırlı modu başlat
' Buraya kodlarınızı yazın
PRINT "Merhaba"
FOR i = 1 TO 5
    PRINT "Sayı:", i
NEXT i
REPL END               ' Çok satırlı modu bitir
```

### Dosya İşlemleri
```basic
' Program kaydetme
SAVE "myprogram.pdsx"

' Program yükleme
LOAD "myprogram.pdsx"

' Program çalıştırma
RUN "myprogram.pdsx"

' Mevcut programı çalıştırma
RUN
```

### REPL Örnek Kullanımı
```
10> PRINT "İlk satır"
20> FOR i = 1 TO 3
30>     PRINT "Döngü:", i
40> NEXT i
50> SAVE "test.pdsx"
Program kaydedildi: test.pdsx
60> LIST
Mevcut Program:
----------------------------------------
  1: 10 PRINT "İlk satır"
  2: 20 FOR i = 1 TO 3
  3: 30     PRINT "Döngü:", i
  4: 40 NEXT i
----------------------------------------
70> RUN
İlk satır
Döngü: 1
Döngü: 2
Döngü: 3
80> EXIT
```

---

## 19. 🚨 Hata İşleme (GELİŞTİRİLMİŞ - pdsXv11g)

Hata işleme, güvenilir ve sağlam programlar yazmak için kritik öneme sahiptir. pdsXv11g, geleneksel BASIC hata işlemini modern TRY-CATCH blokları ile genişletmiştir. Bu sayede programlarınız beklenmedik durumlarla karşılaştığında kontrollü bir şekilde tepki verebilir ve kullanıcı deneyimini koruyabilir.

**Hata İşleme Türleri:**
- **TRY-CATCH**: Modern exception handling (YENİ)
- **THROW**: Özel hata fırlatma (YENİ)
- **ON ERROR GOTO**: Geleneksel etiket tabanlı hata işleme
- **RESUME NEXT**: Hata sonrası program devamı

**Hata Türleri:**
- **Syntax Errors**: Kod yazım hataları
- **Runtime Errors**: Çalışma zamanı hataları
- **Logic Errors**: Mantık hataları
- **Custom Errors**: Kullanıcı tanımlı hatalar

**Best Practices:**
- **Öngörülebilir Hatalar**: Dosya bulunamadı, sıfıra bölme gibi
- **Graceful Degradation**: Program çökmesi yerine uygun tepki
- **Error Logging**: Hataları kaydetme ve izleme
- **User Feedback**: Kullanıcıya anlaşılır hata mesajları

**Syntax:**
```basic
TRY                              ' Hata yakalama başlat
    riskli_işlemler...
CATCH hata_değişkeni DO          ' Hata yakalama
    hata_işleme...
END TRY

THROW "Özel hata mesajı"         ' Özel hata fırlatma

ON ERROR GOTO EtiketAdı          ' Klasik hata yönetimi
```

### Traditional Try-Catch (YENİ!)
```basic
' Modern exception handling
TRY risky_operation CATCH error_var DO PRINT "Hata:", error_var

' Blok try-catch
TRY
    DIM result AS DOUBLE = 10 / 0      ' Division by zero
    PRINT "Sonuç:", result
CATCH error DO
    PRINT "Matematik hatası:", error
END TRY

' Çoklu hata yakalama
TRY
    DIM file_content AS STRING = READ_FILE("nonexistent.txt")
    DIM number AS INTEGER = VAL("invalid_number")
CATCH file_error DO
    PRINT "Dosya hatası:", file_error
CATCH conversion_error DO  
    PRINT "Dönüştürme hatası:", conversion_error
CATCH general_error DO
    PRINT "Genel hata:", general_error
END TRY
```

### Error Handling with GOTO
```basic
ON ERROR GOTO ErrorHandler     ' Hata durumunda etikete git

' Risky operation
DIM x AS DOUBLE = 10 / 0

PRINT "Bu satır çalışmayacak"
END

ErrorHandler:
    PRINT "Bir hata oluştu!"
    RESUME NEXT                 ' Hata sonrası devam et
```

### Custom Error Throwing (YENİ!)
```basic
DEF FUNCTION validate_age(age)
    IF age < 0 THEN
        THROW "Yaş negatif olamaz"
    ELSEIF age > 150 THEN
        THROW "Yaş 150'den büyük olamaz"
    END IF
    RETURN TRUE
END FUNCTION

' Kullanım
TRY
    validate_age(-5)
CATCH validation_error DO
    PRINT "Validasyon hatası:", validation_error
END TRY
```

---

## 20. 🎯 İpuçları ve En İyi Uygulamalar

Başarılı pdsXv11g programları yazmak için bu bölümde yer alan en iyi uygulamaları takip edin. Bu öneriler, kodunuzun okunabilirliğini, performansını ve güvenliğini artıracak, aynı zamanda hata yapma olasılığını azaltacaktır. Özellikle büyük projelerde bu kuralları uygulamak kritik öneme sahiptir.

**Ana Prensipler:**
- **Kod Kalitesi**: Temiz, anlaşılır ve sürdürülebilir kod yazma
- **Performans**: Bellek ve CPU kullanımını optimize etme  
- **Güvenlik**: Hata yakalama ve güvenli programlama teknikleri
- **Organizasyon**: Modüler yapı ve düzenli kodlama
- **Test Edilebilirlik**: Kolay test edilebilen fonksiyonlar yazma

**Syntax ve Stil:**
```basic
DIM variable_name AS TYPE     ' Net tip tanımlaması
IF condition THEN             ' Açık koşul ifadeleri
    command                   ' Girintili blok yapısı  
END IF                        ' Kapatma etiketleri
```

1. **Strict DIM Mode**: Tüm değişkenleri kullanmadan önce `DIM` ile tanımlayın
2. **Tip Güvenliği**: Uygun veri tiplerini kullanın
3. **Fonksiyon Modülerliği**: Karmaşık işlemleri fonksiyonlara bölün
4. **Error Handling**: Kritik işlemlerde hata yakalama kullanın
5. **Performance**: Büyük verilerle çalışırken NumPy/Pandas fonksiyonlarını tercih edin
6. **Memory Management**: Büyük veri yapıları için bellek yönetimini unutmayın
7. **Klavye Kontrolü**: Oyunlarda KEY() ile responsive kontrol, GETKEY() ile menü navigasyonu
8. **REPL Kullanımı**: Hızlı prototipleme ve test için REPL modunu kullanın

---

## 21. 🎮 Oyun Geliştirme İçin İpuçları

Oyun geliştirme, programlamada en yaratıcı ve eğlenceli alanlardan biridir. pdsXv11g ile konsol tabanlı oyunlar, puzzle'lar, simülasyonlar ve interaktif uygulamalar geliştirebilirsiniz. Bu bölümde oyun geliştirme sürecinde karşılaştığınız temel teknikler ve çözümler ele alınmaktadır.

**Oyun Geliştirme Temelleri:**
- **Game Loop**: Ana oyun döngüsü ve zaman yönetimi
- **Input Handling**: KEY() ve GETKEY() ile klavye girişi işleme
- **State Management**: Değişkenler ile oyun durumu ve sahne yönetimi  
- **Graphics**: ASCII art ve konsol tabanlı görselleştirme
- **Logic**: IF-THEN, SELECT CASE ile oyun mantığı
- **Data Structures**: ARRAY, LIST, DICT ile oyun verileri

**pdsXv11g Oyun Geliştirme Avantajları:**
- **Hızlı Prototipleme**: REPL modu ile anında test
- **Kolay Debug**: Adım adım çalıştırma ve hata ayıklama
- **Cross-Platform**: Windows, Linux, macOS desteği
- **Modüler Yapı**: Fonksiyon ve library sistemleri
- **Modern Özellikler**: Array manipulation, string processing

**Kullanım Senaryoları:**
```basic
' Oyun türleri
DIM game_types AS ARRAY = [
    "Text Adventure",     ' Metin tabanlı macera
    "ASCII RPG",         ' Karakter tabanlı RPG  
    "Puzzle Games",      ' Bulmaca oyunları
    "Strategy Games",    ' Strateji oyunları
    "Educational Games", ' Eğitici oyunlar
    "Simulation Games"   ' Simülasyon oyunları
]
```

### Real-time Klavye Kontrolü
```basic
' Ana oyun döngüsü
DIM game_running AS BOOLEAN
game_running = True

WHILE game_running
    ' Klavye girişini kontrol et (non-blocking)
    DIM key AS STRING
    key = KEY()
    
    SELECT CASE key
        CASE "W", "<YUKARIOK>"
            ' Yukarı hareket
        CASE "S", "<ASAGIOK>"
            ' Aşağı hareket
        CASE "A", "<SOLOK>"
            ' Sol hareket
        CASE "D", "<SAGOK>"
            ' Sağ hareket
        CASE "Q", "<ESC>"
            game_running = False
    END SELECT
    
    ' Oyun mantığı...
    
    ' Kısa bekleme (frame rate kontrolü)
    WAIT 50  ' 50ms bekle
WEND
```

### Menü Sistemi
```basic
' Menü navigasyonu için GETKEY kullan
PRINT "1. Yeni Oyun"
PRINT "2. Ayarlar"
PRINT "3. Çıkış"

DIM choice AS STRING
choice = GETKEY("1,2,3")

SELECT CASE choice
    CASE "1"
        ' Yeni oyun başlat
    CASE "2"
        ' Ayarlar menüsü
    CASE "3"
        ' Çıkış
END SELECT
```

---

## 22. 📞 Destek ve Daha Fazla Bilgi

- Etkileşimli modda `HELP` komutu ile anlık yardım
- `HELP [komut_adı]` ile belirli komut yardımı
- `HELP EXAMPLES` ile örnek programlar
- Debug mode ile adım adım kod izleme
- REPL modu ile etkileşimli geliştirme

**pdsXv11g - Modern BASIC için gelişmiş yorumlayıcı! 🚀**

---

## 22.1. 📋 pdsXv11g v1.1.0 - Yeni Özellikler Özeti

Bu sürümde eklenen ve geliştirilen tüm özellikler:

### 🆕 Tamamen Yeni Özellikler:
1. **FOR EACH IN döngüleri** - Modern koleksiyon iterasyonu
   ```basic
   FOR EACH item IN my_array
       PRINT item
   NEXT
   ```

2. **FUNC...END FUNC lambda fonksiyonlar** - Modern fonksiyon syntax'ı
   ```basic
   FUNC calculate(x, y)
       RETURN x * y + 10
   END FUNC
   ```

3. **String Array desteği** - Çok boyutlu string dizileri
   ```basic
   DIM cities(10) AS STRING
   DIM regions(3, 4) AS STRING
   DIM countries(2, 3, 4) AS STRING
   ```

4. **İç içe STRUCT/UNION** - Nested field erişimi
   ```basic
   person.address.city = "İstanbul"
   person.contact.email = "test@example.com"
   ```

5. **ENUM block syntax** - Modern enum tanımlaması
   ```basic
   ENUM Colors
   RED = "#FF0000"
   GREEN = "#00FF00"
   BLUE = "#0000FF"
   END ENUM
   ```

6. **DATAFRAME block syntax** - Veri çerçevesi tanımlaması
   ```basic
   DATAFRAME sales_data
   "product": ["A", "B", "C"]
   "price": [100, 200, 150]
   END DATAFRAME
   ```

7. **20+ String Array Functions** - Gelişmiş string işlemleri
   ```basic
   STRARRAY, STRGET, STRSET, STRLEN, STRCAT
   STRSPLIT, STRJOIN, STRFIND, STRREPLACE
   STRCOMPARE, STRTRIM, STRPAD, STRSUBSTR
   STRREVERSE, STRMATCH, STRCOUNT
   STRLOWER, STRUPPER, STRTITLE, STRSWAP
   ```

8. **END komutu** - Program sonlandırma
   ```basic
   IF error_condition THEN END
   ```

9. **Exception Handling** - TRY-CATCH-THROW
   ```basic
   TRY
       risky_operation()
   CATCH error DO
       PRINT "Hata:", error
   END TRY
   ```

10. **Performance Monitoring** - Sistem izleme
    ```basic
    PERFORMANCE           ' CPU/Memory göster
    TIMER                 ' Zaman ölçümü
    CPU_COUNT()           ' İşlemci sayısı
    THREAD_COUNT()        ' Thread sayısı
    ```

### ⚡ Geliştirilmiş Özellikler:
- **Matrix operasyonları**: TRANSPOSE, INV, DIAG ile linear algebra
- **DataFrame işlemleri**: GROUPBY, PIVOT_TABLE, FILTER, MERGE
- **String Array fonksiyonları**: SPLIT_ARRAY, JOIN_ARRAY, sıralama
- **Çok boyutlu dizi desteği**: 1D, 2D, 3D arrays için gelişmiş support
- **Nested struct initialization**: Otomatik nested field initialization

### 🔧 Teknik İyileştirmeler:
- NumPy entegrasyonu ile hızlı matrix hesaplamaları
- Pandas entegrasyonu ile güçlü veri analizi
- Gelişmiş hata yakalama ve debugging
- Memory management optimizasyonları
- Type system geliştirmeleri

### 📊 Yeni Built-in Fonksiyonlar:
- **Matrix**: `TRANSPOSE()`, `INV()`, `DIAG()`, `NORM()`, `SOLVE()`
- **String Arrays**: 20+ fonksiyon (`STRARRAY()`, `STRGET()`, `STRSET()`, `STRLEN()`, `STRCAT()`, `STRSPLIT()`, `STRJOIN()`, `STRFIND()`, `STRREPLACE()`, `STRCOMPARE()`, `STRTRIM()`, `STRPAD()`, `STRSUBSTR()`, `STRREVERSE()`, `STRMATCH()`, `STRCOUNT()`, `STRLOWER()`, `STRUPPER()`, `STRTITLE()`, `STRSWAP()`)
- **DataFrame**: `GROUPBY()`, `PIVOT_TABLE()`, `FILTER()`, `MERGE()`
- **NumPy**: `EYE()`, `ZEROS()`, `ONES()`, `FULL()`, `RESHAPE()`
- **Performance**: `PERFORMANCE()`, `TIMER()`, `CPU_COUNT()`, `THREAD_COUNT()`, `CURRENT_THREAD()`, `MEMORY_USAGE()`
- **Threading/Async**: `SLEEP()`, `WAIT()`, `ASYNC_WAIT()`
- **Error Handling**: `TRY-CATCH-THROW`, modern exception handling

Bu yeni özelliklerle pdsXv11g artık modern programlama ihtiyaçlarını karşılayabilen, güçlü bir BASIC yorumlayıcısı haline gelmiştir! 

**Tüm özellikler test edilmiş ve production-ready durumda! ✅**

---

## 23. 🎓 İleri Seviye Programlama: pdsXv11g ile Profesyonel Geliştirme

### Modern Programlama Paradigmaları ve Algoritmalar ile pdsXv11g

Bu bölüm, deneyimli programcıların pdsXv11g ile karşılaşabilecekleri zorlukları ele alır ve farklı programlama paradigmalarının nasıl uygulanabileceğini gösterir. BASIC'in basitliğini koruyarak modern yazılım geliştirme tekniklerini nasıl uygulayabileceğinizi öğreneceksiniz.

---

## 24. 📚 Programlama Paradigmalarının pdsXv11g'de Uygulanması

### 1. Fonksiyonel Programlama Paradigması

pdsXv11g, fonksiyonel programlamanın temel ilkelerini destekler:

#### Higher-Order Functions (Yüksek Seviye Fonksiyonlar)
```basic
' MAP, FILTER, REDUCE fonksiyonları ile fonksiyonel yaklaşım
DIM numbers AS ARRAY
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

' Lambda benzeri fonksiyon tanımlama
DEF FN square(x) = x * x
DEF FN is_even(x) = (x MOD 2 = 0)

' Fonksiyonel pipeline oluşturma
DIM squared_evens AS ARRAY
squared_evens = MAP(square, FILTER(is_even, numbers))

PRINT "Çift sayıların karesi:", squared_evens
```

#### Immutable Data Structures (Değişmez Veri Yapıları)
```basic
' Veri yapılarını kopyalayarak değişmezlik simüle etme
DEF FUNCTION add_to_list(original_list, new_item)
    DIM new_list AS ARRAY
    new_list = []
    
    ' Orijinal listeyi kopyala
    FOR i = 0 TO LEN(original_list) - 1
        INSERT(new_list, original_list(i))
    NEXT i
    
    ' Yeni elemanı ekle
    INSERT(new_list, new_item)
    RETURN new_list
END FUNCTION

' Kullanım
DIM original AS ARRAY
original = [1, 2, 3]
DIM updated AS ARRAY
updated = add_to_list(original, 4)
```

### 2. Nesne Yönelimli Programlama Simülasyonu

pdsXv11g'de sınıf benzeri yapılar:

```basic
' "Class" simülasyonu - Dictionary tabanlı nesne
DEF FUNCTION create_person(name, age, profession)
    DIM person AS DICT
    person = {
        "name": name,
        "age": age,
        "profession": profession,
        "skills": [],
        "experience": 0
    }
    RETURN person
END FUNCTION

' "Method" simülasyonu
DEF SUB person_add_skill(person_obj, skill)
    INSERT(person_obj("skills"), skill)
    person_obj("experience") = person_obj("experience") + 1
END SUB

DEF FUNCTION person_get_info(person_obj)
    DIM info AS STRING
    info = person_obj("name") + " (" + STR$(person_obj("age")) + ") - " + person_obj("profession")
    info = info + " | Skills: " + STR$(LEN(person_obj("skills")))
    RETURN info
END FUNCTION

' Kullanım
DIM developer AS DICT
developer = create_person("Ahmet", 28, "Software Developer")
person_add_skill(developer, "Python")
person_add_skill(developer, "JavaScript")
PRINT person_get_info(developer)
```

### 3. Event-Driven Programming (Olay Güdümlü Programlama)

```basic
' Event sistem simülasyonu
DIM event_listeners AS DICT
event_listeners = {}

DEF SUB register_event_listener(event_name, callback_function)
    IF NOT event_listeners.CONTAINS(event_name) THEN
        event_listeners(event_name) = []
    END IF
    INSERT(event_listeners(event_name), callback_function)
END SUB

DEF SUB emit_event(event_name, event_data)
    IF event_listeners.CONTAINS(event_name) THEN
        DIM callbacks AS ARRAY
        callbacks = event_listeners(event_name)
        FOR i = 0 TO LEN(callbacks) - 1
            ' Callback fonksiyonunu çağır
            CALL callbacks(i)(event_data)
        NEXT i
    END IF
END SUB

' Event handlers
DEF SUB on_player_move(move_data)
    PRINT "Oyuncu hareket etti:", move_data("direction")
END SUB

DEF SUB on_score_change(score_data)
    PRINT "Skor güncellendi:", score_data("new_score")
END SUB

' Event kayıtları
register_event_listener("player_move", on_player_move)
register_event_listener("score_change", on_score_change)
```

---

## 25. 🧩 Gelişmiş Algoritmalar ve Veri Yapıları

### 1. Sıralama Algoritmaları

#### Quick Sort Implementasyonu
```basic
DEF FUNCTION quicksort(arr, low, high)
    IF low < high THEN
        DIM pivot_index AS INTEGER
        pivot_index = partition(arr, low, high)
        
        ' Özyinelemeli olarak sırala
        arr = quicksort(arr, low, pivot_index - 1)
        arr = quicksort(arr, pivot_index + 1, high)
    END IF
    RETURN arr
END FUNCTION

DEF FUNCTION partition(arr, low, high)
    DIM pivot AS DOUBLE
    pivot = arr(high)
    DIM i AS INTEGER
    i = low - 1
    
    FOR j = low TO high - 1
        IF arr(j) <= pivot THEN
            i = i + 1
            ' Swap
            DIM temp AS DOUBLE
            temp = arr(i)
            arr(i) = arr(j)
            arr(j) = temp
        END IF
    NEXT j
    
    ' Pivot'u yerleştir
    DIM temp AS DOUBLE
    temp = arr(i + 1)
    arr(i + 1) = arr(high)
    arr(high) = temp
    
    RETURN i + 1
END FUNCTION
```

#### Merge Sort Implementasyonu
```basic
DEF FUNCTION merge_sort(arr)
    DIM length AS INTEGER
    length = LEN(arr)
    
    IF length <= 1 THEN
        RETURN arr
    END IF
    
    DIM mid AS INTEGER
    mid = length / 2
    
    ' Diziyi ikiye böl
    DIM left AS ARRAY
    DIM right AS ARRAY
    left = []
    right = []
    
    FOR i = 0 TO mid - 1
        INSERT(left, arr(i))
    NEXT i
    
    FOR i = mid TO length - 1
        INSERT(right, arr(i))
    NEXT i
    
    ' Özyinelemeli sıralama
    left = merge_sort(left)
    right = merge_sort(right)
    
    RETURN merge(left, right)
END FUNCTION

DEF FUNCTION merge(left, right)
    DIM result AS ARRAY
    result = []
    DIM i, j AS INTEGER
    i = 0
    j = 0
    
    WHILE i < LEN(left) AND j < LEN(right)
        IF left(i) <= right(j) THEN
            INSERT(result, left(i))
            i = i + 1
        ELSE
            INSERT(result, right(j))
            j = j + 1
        END IF
    WEND
    
    ' Kalan elemanları ekle
    WHILE i < LEN(left)
        INSERT(result, left(i))
        i = i + 1
    WEND
    
    WHILE j < LEN(right)
        INSERT(result, right(j))
        j = j + 1
    WEND
    
    RETURN result
END FUNCTION
```

### 2. Arama Algoritmaları

#### Binary Search
```basic
DEF FUNCTION binary_search(sorted_array, target)
    DIM left AS INTEGER
    DIM right AS INTEGER
    left = 0
    right = LEN(sorted_array) - 1
    
    WHILE left <= right
        DIM mid AS INTEGER
        mid = (left + right) / 2
        
        IF sorted_array(mid) = target THEN
            RETURN mid
        ELSEIF sorted_array(mid) < target THEN
            left = mid + 1
        ELSE
            right = mid - 1
        END IF
    WEND
    
    RETURN -1  ' Bulunamadı
END FUNCTION
```

### 3. Graf Algoritmaları

#### Breadth-First Search (BFS)
```basic
DEF FUNCTION bfs(graph, start_node, target_node)
    DIM visited AS DICT
    DIM queue AS ARRAY
    DIM path AS ARRAY
    
    visited = {}
    queue = [start_node]
    path = []
    
    visited(start_node) = True
    
    WHILE LEN(queue) > 0
        DIM current AS STRING
        current = queue(0)
        REMOVE(queue, 0)  ' Dequeue
        
        INSERT(path, current)
        
        IF current = target_node THEN
            RETURN path
        END IF
        
        ' Komşuları ekle
        IF graph.CONTAINS(current) THEN
            DIM neighbors AS ARRAY
            neighbors = graph(current)
            FOR i = 0 TO LEN(neighbors) - 1
                DIM neighbor AS STRING
                neighbor = neighbors(i)
                IF NOT visited.CONTAINS(neighbor) THEN
                    visited(neighbor) = True
                    INSERT(queue, neighbor)
                END IF
            NEXT i
        END IF
    WEND
    
    RETURN []  ' Yol bulunamadı
END FUNCTION
```

### 4. Dinamik Programlama

#### Fibonacci with Memoization
```basic
DIM fibonacci_cache AS DICT
fibonacci_cache = {}

DEF FUNCTION fibonacci_memo(n)
    IF fibonacci_cache.CONTAINS(STR$(n)) THEN
        RETURN fibonacci_cache(STR$(n))
    END IF
    
    DIM result AS INTEGER
    IF n <= 1 THEN
        result = n
    ELSE
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    END IF
    
    fibonacci_cache(STR$(n)) = result
    RETURN result
END FUNCTION
```

---

## 26. 🎮 Örnek Oyunların Detaylı Analizi

### Game03 - 2048 Oyunu Analizi

Bu oyun, modern yazılım geliştirme tekniklerinin mükemmel bir örneğidir:

#### 1. Modüler Tasarım Analizi
```basic
' Ana yapı - Her fonksiyon tek sorumluluk prensibini takip eder
DEF SUB initialize_2048()     ' Oyun başlatma sorumluluğu
DEF SUB add_random_tile()     ' Rastgele karo ekleme sorumluluğu
DEF SUB show_board()          ' Görselleştirme sorumluluğu
DEF FUNCTION move_left()      ' Sol hareket lojiği
DEF FUNCTION has_move()       ' Oyun durumu kontrolü
```

**Tasarım Kalıpları:**
- **Single Responsibility**: Her fonksiyon tek bir işi yapar
- **State Management**: Oyun durumu global değişkenlerle kontrol edilir
- **Event Handling**: Klavye girişleri merkezi olarak işlenir

#### 2. Algoritma Analizi - Hareket Lojiği
```basic
DEF FUNCTION move_left() AS BOOLEAN
    DIM moved AS BOOLEAN
    moved = False
    
    FOR i = 0 TO 3  ' Her satır için
        ' 1. Adım: Sıfır olmayan değerleri topla
        DIM row AS ARRAY
        row = []
        FOR j = 0 TO 3
            IF board(i)(j) <> 0 THEN
                INSERT(row, board(i)(j))
            END IF
        NEXT j
        
        ' 2. Adım: Birleştirme algoritması
        DIM merged_row AS ARRAY
        merged_row = []
        DIM j AS INTEGER
        j = 0
        
        WHILE j < LEN(row)
            IF j < LEN(row) - 1 AND row(j) = row(j + 1) THEN
                ' İki aynı değeri birleştir
                DIM merged_value AS INTEGER
                merged_value = row(j) * 2
                INSERT(merged_row, merged_value)
                score = score + merged_value  ' Skor güncellemesi
                j = j + 2  ' İki değeri atla
            ELSE
                INSERT(merged_row, row(j))
                j = j + 1
            END IF
        WEND
        
        ' 3. Adım: Satırı 4 elemana tamamla
        WHILE LEN(merged_row) < 4
            INSERT(merged_row, 0)
        WEND
        
        ' 4. Adım: Değişiklik tespit et ve uygula
        FOR j = 0 TO 3
            IF board(i)(j) <> merged_row(j) THEN
                moved = True
            END IF
            board(i)(j) = merged_row(j)
        NEXT j
    NEXT i
    
    RETURN moved
END FUNCTION
```

**Algoritma Karmaşıklığı:**
- **Zaman Karmaşıklığı**: O(n²) - 4x4 tahta için sabit
- **Alan Karmaşıklığı**: O(n) - geçici diziler için

#### 3. Rastgele Sayı Üretimi ve Oyun Dengesi
```basic
DEF SUB add_random_tile()
    ' Weighted random selection - %90 ihtimalle 2, %10 ihtimalle 4
    DIM value AS INTEGER
    IF RND(1, 10) <= 9 THEN
        value = 2
    ELSE
        value = 4
    END IF
    
    ' Uniform random positioning
    DIM random_index AS INTEGER
    random_index = RND(0, LEN(empty_cells) - 1)
END SUB
```

### Game01 - Satranç Oyunu Analizi

Satranç oyunu, karmaşık kural sistemlerinin implementasyonunu gösterir:

#### 1. Veri Yapısı Tasarımı
```basic
' Unicode karakterler ile zengin görselleştirme
board(7)(0) = "♖"  ' Beyaz Kale
board(0)(0) = "♜"  ' Siyah Kale

' Pozisyon takibi için ayrı veri yapıları
DIM white_king_pos AS ARRAY
DIM black_king_pos AS ARRAY
DIM move_history AS ARRAY
DIM captured_pieces AS ARRAY
```

#### 2. Karmaşık Kural Sistemleri
```basic
' Her taş için ayrı hareket validasyonu
DEF FUNCTION is_valid_move(from_row, from_col, to_row, to_col)
    DIM piece AS STRING
    piece = board(from_row)(from_col)
    
    SELECT CASE piece
        CASE "♙", "♟"  ' Piyon
            RETURN validate_pawn_move(from_row, from_col, to_row, to_col)
        CASE "♖", "♜"  ' Kale
            RETURN validate_rook_move(from_row, from_col, to_row, to_col)
        CASE "♘", "♞"  ' At
            RETURN validate_knight_move(from_row, from_col, to_row, to_col)
        ' ... diğer taşlar
    END SELECT
END FUNCTION
```

### Game04 - TicTacToe AI Algoritması

Minimax algoritmasının basit implementasyonu:

#### 1. Oyun Ağacı Değerlendirmesi
```basic
DEF FUNCTION minimax(board_state, depth, is_maximizing)
    DIM score AS INTEGER
    score = evaluate_board(board_state)
    
    ' Terminal durumlar
    IF score = 10 THEN RETURN score - depth
    IF score = -10 THEN RETURN score + depth
    IF NOT has_moves_left(board_state) THEN RETURN 0
    
    IF is_maximizing THEN
        DIM best AS INTEGER
        best = -1000
        
        FOR i = 0 TO 2
            FOR j = 0 TO 2
                IF board_state(i)(j) = " " THEN
                    board_state(i)(j) = computer_turn
                    best = MAX(best, minimax(board_state, depth + 1, False))
                    board_state(i)(j) = " "  ' Geri al
                END IF
            NEXT j
        NEXT i
        
        RETURN best
    ELSE
        DIM best AS INTEGER
        best = 1000
        
        FOR i = 0 TO 2
            FOR j = 0 TO 2
                IF board_state(i)(j) = " " THEN
                    board_state(i)(j) = player_turn
                    best = MIN(best, minimax(board_state, depth + 1, True))
                    board_state(i)(j) = " "  ' Geri al
                END IF
            NEXT j
        NEXT i
        
        RETURN best
    END IF
END FUNCTION
```

#### 2. Heuristik Değerlendirme
```basic
DEF FUNCTION evaluate_board(board_state)
    ' Satırları kontrol et
    FOR row = 0 TO 2
        IF board_state(row)(0) = board_state(row)(1) AND 
           board_state(row)(1) = board_state(row)(2) THEN
            IF board_state(row)(0) = computer_turn THEN
                RETURN 10
            ELSEIF board_state(row)(0) = player_turn THEN
                RETURN -10
            END IF
        END IF
    NEXT row
    
    ' Sütunları ve çaprazları kontrol et
    ' ... similar logic
    
    RETURN 0  ' Berabere
END FUNCTION
```

---

## 27. 📊 Veri Analizi Örneğinin İleri Teknikleri

### Example05 - Data Analysis Derinlemesine

#### 1. Statistical Computing
```basic
DEF SUB advanced_statistics(data_array, data_name)
    ' Temel istatistikler
    DIM mean_val AS DOUBLE
    DIM std_val AS DOUBLE
    mean_val = MEAN(data_array)
    std_val = STD(data_array)
    
    ' Z-score hesaplama
    PRINT "Z-SCORE ANALIZI:"
    FOR i = 0 TO LEN(data_array) - 1
        DIM z_score AS DOUBLE
        z_score = (data_array(i) - mean_val) / std_val
        PRINT "Veri " + STR$(i + 1) + ": " + STR$(z_score)
        
        ' Outlier detection
        IF ABS(z_score) > 2 THEN
            PRINT "  → OUTLIER tespit edildi!"
        END IF
    NEXT i
    
    ' Confidence interval hesaplama
    DIM margin_of_error AS DOUBLE
    margin_of_error = 1.96 * (std_val / SQR(LEN(data_array)))
    PRINT "95% Güven Aralığı: [" + STR$(mean_val - margin_of_error) + 
          ", " + STR$(mean_val + margin_of_error) + "]"
END SUB
```

#### 2. Time Series Analysis
```basic
DEF FUNCTION calculate_moving_average(data_array, window_size)
    DIM moving_avg AS ARRAY
    moving_avg = []
    
    FOR i = window_size - 1 TO LEN(data_array) - 1
        DIM sum AS DOUBLE
        sum = 0
        
        FOR j = i - window_size + 1 TO i
            sum = sum + data_array(j)
        NEXT j
        
        INSERT(moving_avg, sum / window_size)
    NEXT i
    
    RETURN moving_avg
END FUNCTION

DEF FUNCTION detect_trend(data_array)
    ' Linear regression for trend detection
    DIM n AS INTEGER
    n = LEN(data_array)
    
    DIM sum_x, sum_y, sum_xy, sum_x2 AS DOUBLE
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    
    FOR i = 0 TO n - 1
        sum_x = sum_x + i
        sum_y = sum_y + data_array(i)
        sum_xy = sum_xy + (i * data_array(i))
        sum_x2 = sum_x2 + (i * i)
    NEXT i
    
    DIM slope AS DOUBLE
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    
    IF slope > 0.1 THEN
        RETURN "ARTAN"
    ELSEIF slope < -0.1 THEN
        RETURN "AZALAN"
    ELSE
        RETURN "STABIL"
    END IF
END FUNCTION
```

#### 3. Korelasyon ve Regresyon
```basic
DEF FUNCTION pearson_correlation(x_array, y_array)
    DIM n AS INTEGER
    n = LEN(x_array)
    
    DIM sum_x, sum_y, sum_xy, sum_x2, sum_y2 AS DOUBLE
    
    FOR i = 0 TO n - 1
        sum_x = sum_x + x_array(i)
        sum_y = sum_y + y_array(i)
        sum_xy = sum_xy + (x_array(i) * y_array(i))
        sum_x2 = sum_x2 + (x_array(i) * x_array(i))
        sum_y2 = sum_y2 + (y_array(i) * y_array(i))
    NEXT i
    
    DIM numerator AS DOUBLE
    DIM denominator AS DOUBLE
    numerator = n * sum_xy - sum_x * sum_y
    denominator = SQR((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y))
    
    IF denominator = 0 THEN
        RETURN 0
    ELSE
        RETURN numerator / denominator
    END IF
END FUNCTION
```

---

## 28. 🔬 Performance Optimization Teknikleri

### 1. Algoritma Optimizasyonu

#### Memoization Pattern
```basic
DIM calculation_cache AS DICT
calculation_cache = {}

DEF FUNCTION expensive_calculation(input_value)
    DIM key AS STRING
    key = STR$(input_value)
    
    IF calculation_cache.CONTAINS(key) THEN
        RETURN calculation_cache(key)
    END IF
    
    ' Expensive operation simulation
    DIM result AS DOUBLE
    result = 0
    FOR i = 1 TO input_value
        result = result + SQR(i) * LOG(i)
    NEXT i
    
    calculation_cache(key) = result
    RETURN result
END FUNCTION
```

#### Lazy Evaluation
```basic
DEF FUNCTION lazy_sequence_generator(start_val, count)
    DIM generator AS DICT
    generator = {
        "current": start_val,
        "remaining": count,
        "has_next": True
    }
    RETURN generator
END FUNCTION

DEF FUNCTION get_next_value(generator_obj)
    IF NOT generator_obj("has_next") THEN
        RETURN NULL
    END IF
    
    DIM current AS INTEGER
    current = generator_obj("current")
    
    generator_obj("current") = current + 1
    generator_obj("remaining") = generator_obj("remaining") - 1
    
    IF generator_obj("remaining") <= 0 THEN
        generator_obj("has_next") = False
    END IF
    
    RETURN current
END FUNCTION
```

### 2. Memory Management

#### Object Pooling Pattern
```basic
DIM object_pool AS ARRAY
object_pool = []

DEF FUNCTION get_pooled_object()
    IF LEN(object_pool) > 0 THEN
        DIM obj AS DICT
        obj = object_pool(LEN(object_pool) - 1)
        REMOVE(object_pool, LEN(object_pool) - 1)
        RETURN obj
    ELSE
        ' Create new object if pool is empty
        DIM new_obj AS DICT
        new_obj = {"id": 0, "active": False, "data": NULL}
        RETURN new_obj
    END IF
END FUNCTION

DEF SUB return_to_pool(obj)
    ' Reset object state
    obj("active") = False
    obj("data") = NULL
    
    INSERT(object_pool, obj)
END SUB
```

---

## 29. 🛠️ Testing ve Debugging Stratejileri

### 1. Unit Testing Framework
```basic
DIM test_results AS ARRAY
test_results = []

DEF SUB assert_equals(expected, actual, test_name)
    IF expected = actual THEN
        INSERT(test_results, {
            "name": test_name,
            "status": "PASSED",
            "expected": expected,
            "actual": actual
        })
        PRINT "✓ " + test_name + " PASSED"
    ELSE
        INSERT(test_results, {
            "name": test_name,
            "status": "FAILED",
            "expected": expected,
            "actual": actual
        })
        PRINT "✗ " + test_name + " FAILED: Expected " + STR$(expected) + 
              ", got " + STR$(actual)
    END IF
END SUB

' Test suite example
DEF SUB run_sorting_tests()
    DIM test_array AS ARRAY
    test_array = [3, 1, 4, 1, 5, 9, 2, 6]
    
    DIM sorted_result AS ARRAY
    sorted_result = quicksort(test_array, 0, LEN(test_array) - 1)
    
    assert_equals(1, sorted_result(0), "First element should be 1")
    assert_equals(9, sorted_result(LEN(sorted_result) - 1), "Last element should be 9")
    assert_equals(LEN(test_array), LEN(sorted_result), "Array length should be preserved")
END SUB
```

### 2. Debugging Utilities
```basic
DEF SUB debug_print(variable_name, variable_value)
    IF debug_mode THEN
        PRINT "[DEBUG] " + variable_name + " = " + STR$(variable_value)
    END IF
END SUB

DEF SUB trace_function_call(function_name, parameters)
    IF trace_mode THEN
        PRINT "[TRACE] Calling " + function_name + " with params: " + STR$(parameters)
    END IF
END SUB

' Performance monitoring
DEF FUNCTION time_execution(function_to_time)
    DIM start_time AS DOUBLE
    start_time = TIMER
    
    ' Execute function
    DIM result AS DOUBLE
    result = function_to_time()
    
    DIM end_time AS DOUBLE
    end_time = TIMER
    
    PRINT "Execution time: " + STR$(end_time - start_time) + " seconds"
    RETURN result
END FUNCTION
```

---

## 30. 🎯 Best Practices ve Anti-Patterns

### 1. Clean Code Principles

#### Meaningful Names
```basic
' ❌ Kötü örnek
DEF FUNCTION calc(d1, d2)
    RETURN d1 * d2 + 15
END FUNCTION

' ✅ İyi örnek
DEF FUNCTION calculate_total_price_with_tax(base_price, tax_rate)
    DIM tax_amount AS DOUBLE
    tax_amount = base_price * tax_rate
    RETURN base_price + tax_amount
END FUNCTION
```

#### Single Responsibility
```basic
' ❌ Kötü örnek - Çok fazla sorumluluk
DEF SUB process_user_data(user_info)
    ' Validates, processes, saves, and emails user
    ' ... 200 lines of mixed responsibilities
END SUB

' ✅ İyi örnek - Ayrılmış sorumluluklar
DEF FUNCTION validate_user_data(user_info)
    RETURN is_valid_email(user_info("email")) AND is_valid_age(user_info("age"))
END FUNCTION

DEF SUB save_user_to_database(user_info)
    ' Only handles database operations
END SUB

DEF SUB send_welcome_email(user_email)
    ' Only handles email sending
END SUB
```

### 2. Error Handling Patterns

#### Robust Error Management
```basic
DEF FUNCTION safe_divide(numerator, denominator)
    TRY
        IF denominator = 0 THEN
            THROW "Division by zero error"
        END IF
        RETURN numerator / denominator
    CATCH error_msg DO
        PRINT "Error in safe_divide: " + error_msg
        RETURN NULL
    END TRY
END FUNCTION

DEF FUNCTION process_with_retry(operation_function, max_retries)
    DIM attempts AS INTEGER
    attempts = 0
    
    WHILE attempts < max_retries
        TRY
            RETURN operation_function()
        CATCH error DO
            attempts = attempts + 1
            IF attempts >= max_retries THEN
                PRINT "Max retries exceeded: " + error
                RETURN NULL
            END IF
            PRINT "Retry " + STR$(attempts) + " after error: " + error
            WAIT 1000  ' 1 saniye bekle
        END TRY
    WEND
END FUNCTION
```

---

## 31. 📈 Scalability ve Architecture Patterns

### 1. MVC Pattern Implementation
```basic
' Model - Veri katmanı
DEF FUNCTION user_model_get(user_id)
    ' Database operations
    RETURN user_data
END FUNCTION

' View - Sunum katmanı
DEF SUB user_view_display(user_data)
    PRINT "User: " + user_data("name")
    PRINT "Email: " + user_data("email")
END SUB

' Controller - İş mantığı
DEF SUB user_controller_show(user_id)
    DIM user_data AS DICT
    user_data = user_model_get(user_id)
    
    IF user_data <> NULL THEN
        user_view_display(user_data)
    ELSE
        PRINT "User not found"
    END IF
END SUB
```

### 2. Observer Pattern
```basic
DIM observers AS ARRAY
observers = []

DEF SUB register_observer(observer_function)
    INSERT(observers, observer_function)
END SUB

DEF SUB notify_observers(event_data)
    FOR i = 0 TO LEN(observers) - 1
        CALL observers(i)(event_data)
    NEXT i
END SUB

' Subject that notifies observers
DEF SUB update_game_state(new_state)
    ' Update internal state
    game_state = new_state
    
    ' Notify all observers
    notify_observers(game_state)
END SUB
```

---

## 32. 🔄 Concurrent Programming Simülasyonu

### 1. Task Queue Pattern
```basic
DIM task_queue AS ARRAY
task_queue = []

DEF SUB add_task(task_function, task_data)
    DIM task AS DICT
    task = {
        "function": task_function,
        "data": task_data,
        "status": "PENDING",
        "created_at": TIMER
    }
    INSERT(task_queue, task)
END SUB

DEF SUB process_task_queue()
    WHILE LEN(task_queue) > 0
        DIM current_task AS DICT
        current_task = task_queue(0)
        REMOVE(task_queue, 0)
        
        current_task("status") = "PROCESSING"
        
        TRY
            CALL current_task("function")(current_task("data"))
            current_task("status") = "COMPLETED"
        CATCH error DO
            current_task("status") = "FAILED"
            PRINT "Task failed: " + error
        END TRY
    WEND
END SUB
```

---

## 33. 🎊 Sonuç ve İleri Öneriler

pdsXv11g ile profesyonel seviyede yazılım geliştirme mümkündür. Bu bölümde öğrendikleriniz:

### 🔥 Temel Prensipler:
1. **Modüler Tasarım**: Her fonksiyon tek sorumluluk prensibi
2. **Clean Code**: Anlaşılır ve sürdürülebilir kod yazma
3. **Error Handling**: Robust hata yönetimi teknikleri
4. **Performance**: Algoritma optimizasyonu ve bellek yönetimi
5. **Testing**: Unit test ve debugging stratejileri

### 🚀 İleri Teknikler:
- Fonksiyonel programlama paradigmalarının uygulanması
- Nesne yönelimli programlama simülasyonu
- Design pattern implementasyonları
- Algoritma ve veri yapısı optimizasyonları
- Concurrent programming simülasyonu

### 📚 Öğrenmeye Devam:
- pdsXv11g'nin tüm built-in fonksiyonlarını keşfedin
- Kendi game engine'inizi geliştirin
- Veri analizi ve machine learning simülasyonları yapın
- Web API'ları ile entegrasyon projeleri oluşturun

**pdsXv11g ile sınırları zorlayın ve modern programlama deneyimi yaşayın! 🎯**

---

## 34. 📦 Modül Sistemi ve Kütüphane Geliştirme

### 1. Kendi Kütüphaneni Geliştirme

#### .libx Dosya Formatı
```basic
' myutils.libx - Utility kütüphanesi
LIBRARY MyUtils

' Kütüphane versiyonu ve metadata
LIBRARY VERSION "1.0.0"
LIBRARY AUTHOR "Developer Name"
LIBRARY DESCRIPTION "Utility functions for common operations"

' Export edilecek fonksiyonlar
EXPORT string_utils, math_utils, file_utils

' String utilities namespace
NAMESPACE string_utils
    DEF FUNCTION reverse_string(input_str)
        DIM result AS STRING
        result = ""
        FOR i = LEN(input_str) TO 1 STEP -1
            result = result + MID$(input_str, i, 1)
        NEXT i
        RETURN result
    END FUNCTION
    
    DEF FUNCTION count_words(text)
        DIM words AS ARRAY
        words = SPLIT(text, " ")
        RETURN LEN(words)
    END FUNCTION
    
    DEF FUNCTION capitalize_words(text)
        DIM words AS ARRAY
        words = SPLIT(text, " ")
        DIM result AS STRING
        result = ""
        
        FOR i = 0 TO LEN(words) - 1
            IF i > 0 THEN result = result + " "
            result = result + UCASE$(LEFT$(words(i), 1)) + LCASE$(RIGHT$(words(i), LEN(words(i)) - 1))
        NEXT i
        
        RETURN result
    END FUNCTION
END NAMESPACE

' Math utilities namespace
NAMESPACE math_utils
    DEF FUNCTION factorial_iterative(n)
        DIM result AS LONG
        result = 1
        FOR i = 2 TO n
            result = result * i
        NEXT i
        RETURN result
    END FUNCTION
    
    DEF FUNCTION gcd(a, b)
        WHILE b <> 0
            DIM temp AS INTEGER
            temp = b
            b = a MOD b
            a = temp
        WEND
        RETURN a
    END FUNCTION
    
    DEF FUNCTION is_prime(n)
        IF n < 2 THEN RETURN FALSE
        FOR i = 2 TO SQR(n)
            IF n MOD i = 0 THEN RETURN FALSE
        NEXT i
        RETURN TRUE
    END FUNCTION
END NAMESPACE

END LIBRARY
```

#### Kütüphane Kullanımı
```basic
' Ana program dosyası
IMPORT "myutils.libx" AS utils

' Namespace'li kullanım
DIM reversed AS STRING
reversed = utils.string_utils.reverse_string("Hello World")
PRINT "Reversed:", reversed

DIM word_count AS INTEGER
word_count = utils.string_utils.count_words("This is a test sentence")
PRINT "Word count:", word_count

DIM capitalized AS STRING
capitalized = utils.string_utils.capitalize_words("hello world from pdsx")
PRINT "Capitalized:", capitalized

' Math utilities
PRINT "10! =", utils.math_utils.factorial_iterative(10)
PRINT "GCD(48,18) =", utils.math_utils.gcd(48, 18)
PRINT "Is 17 prime?", utils.math_utils.is_prime(17)
```

### 2. Proje Yapısı ve Organizasyon

#### Büyük Proje Organizasyonu
```
MyProject/
├── src/
│   ├── main.basx           # Ana program
│   ├── models/
│   │   ├── user.basx       # User model
│   │   └── product.basx    # Product model
│   ├── controllers/
│   │   ├── user_ctrl.basx  # User controller
│   │   └── api_ctrl.basx   # API controller
│   └── views/
│       ├── menu.basx       # Menu views
│       └── reports.basx    # Report views
├── lib/
│   ├── database.libx       # Database utilities
│   ├── validation.libx     # Validation functions
│   └── http.libx          # HTTP utilities
├── tests/
│   ├── test_user.basx     # User tests
│   └── test_api.basx      # API tests
└── config/
    ├── database.conf      # Database config
    └── app.conf          # App config
```

---

## 35. 🗄️ Veritabanı İşlemleri ve Veri Yönetimi

### 1. SQLite Entegrasyonu

#### Database Connection Manager
```basic
' database.libx
LIBRARY DatabaseManager

DIM db_connections AS DICT
db_connections = {}

DEF FUNCTION db_connect(db_path, connection_name)
    TRY
        CONNECT TO db_path AS connection_name
        db_connections(connection_name) = {
            "path": db_path,
            "active": TRUE,
            "created_at": TIMER,
            "queries_count": 0
        }
        RETURN TRUE
    CATCH error DO
        PRINT "Database connection failed:", error
        RETURN FALSE
    END TRY
END FUNCTION

DEF FUNCTION db_execute(connection_name, sql_query)
    IF NOT db_connections.CONTAINS(connection_name) THEN
        PRINT "Connection not found:", connection_name
        RETURN NULL
    END IF
    
    TRY
        DIM result AS ARRAY
        EXECUTE sql_query ON connection_name TO result
        
        ' İstatistikleri güncelle
        db_connections(connection_name)("queries_count") = 
            db_connections(connection_name)("queries_count") + 1
            
        RETURN result
    CATCH error DO
        PRINT "Query execution failed:", error
        RETURN NULL
    END TRY
END FUNCTION

DEF SUB db_disconnect(connection_name)
    IF db_connections.CONTAINS(connection_name) THEN
        DISCONNECT connection_name
        REMOVE(db_connections, connection_name)
        PRINT "Disconnected from:", connection_name
    END IF
END SUB

END LIBRARY
```

#### ORM Pattern Implementation
```basic
' user_model.basx
IMPORT "database.libx" AS db

DEF FUNCTION User_create(name, email, age)
    DIM user_data AS DICT
    user_data = {
        "name": name,
        "email": email, 
        "age": age,
        "created_at": DATE$() + " " + TIME$()
    }
    
    DIM sql AS STRING
    sql = "INSERT INTO users (name, email, age, created_at) VALUES ('" +
          name + "', '" + email + "', " + STR$(age) + ", '" + 
          user_data("created_at") + "')"
    
    DIM result AS ARRAY
    result = db.db_execute("main_db", sql)
    
    IF result <> NULL THEN
        user_data("id") = get_last_insert_id()
        RETURN user_data
    ELSE
        RETURN NULL
    END IF
END FUNCTION

DEF FUNCTION User_find_by_id(user_id)
    DIM sql AS STRING
    sql = "SELECT * FROM users WHERE id = " + STR$(user_id)
    
    DIM result AS ARRAY
    result = db.db_execute("main_db", sql)
    
    IF LEN(result) > 0 THEN
        RETURN result(0)
    ELSE
        RETURN NULL
    END IF
END FUNCTION

DEF FUNCTION User_find_all()
    DIM sql AS STRING
    sql = "SELECT * FROM users ORDER BY created_at DESC"
    
    RETURN db.db_execute("main_db", sql)
END FUNCTION

DEF FUNCTION User_update(user_id, updates)
    DIM sql AS STRING
    sql = "UPDATE users SET "
    
    DIM first AS BOOLEAN
    first = TRUE
    
    FOR key IN updates.KEYS()
        IF NOT first THEN sql = sql + ", "
        sql = sql + key + " = '" + STR$(updates(key)) + "'"
        first = FALSE
    NEXT key
    
    sql = sql + " WHERE id = " + STR$(user_id)
    
    RETURN db.db_execute("main_db", sql)
END FUNCTION

DEF FUNCTION User_delete(user_id)
    DIM sql AS STRING
    sql = "DELETE FROM users WHERE id = " + STR$(user_id)
    
    RETURN db.db_execute("main_db", sql)
END FUNCTION
```

### 2. Veri Migration Sistemi

```basic
' migrations.basx
DIM migration_history AS ARRAY
migration_history = []

DEF SUB run_migration(migration_name, up_sql, down_sql)
    PRINT "Running migration:", migration_name
    
    TRY
        db.db_execute("main_db", up_sql)
        INSERT(migration_history, {
            "name": migration_name,
            "executed_at": TIMER,
            "status": "SUCCESS"
        })
        PRINT "✓ Migration completed:", migration_name
    CATCH error DO
        INSERT(migration_history, {
            "name": migration_name,
            "executed_at": TIMER,
            "status": "FAILED",
            "error": error
        })
        PRINT "✗ Migration failed:", migration_name, error
    END TRY
END SUB

' Migration örnekleri
DEF SUB create_users_table()
    DIM up_sql AS STRING
    up_sql = "CREATE TABLE users (" +
             "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
             "name VARCHAR(100) NOT NULL, " +
             "email VARCHAR(150) UNIQUE NOT NULL, " +
             "age INTEGER, " +
             "created_at DATETIME DEFAULT CURRENT_TIMESTAMP)"
    
    DIM down_sql AS STRING
    down_sql = "DROP TABLE users"
    
    run_migration("001_create_users_table", up_sql, down_sql)
END SUB
```

---

## 36. 🌐 Network Programming ve Web Development

### 1. HTTP Server Simülasyonu

```basic
' http_server.libx
LIBRARY HTTPServer

DIM routes AS DICT
DIM middleware_stack AS ARRAY
routes = {}
middleware_stack = []

DEF SUB register_route(method, path, handler_function)
    DIM route_key AS STRING
    route_key = method + ":" + path
    routes(route_key) = handler_function
END SUB

DEF SUB add_middleware(middleware_function)
    INSERT(middleware_stack, middleware_function)
END SUB

DEF FUNCTION handle_request(method, path, request_data)
    DIM route_key AS STRING
    route_key = method + ":" + path
    
    ' Middleware chain execution
    DIM request_context AS DICT
    request_context = {
        "method": method,
        "path": path,
        "data": request_data,
        "headers": {},
        "timestamp": TIMER
    }
    
    FOR i = 0 TO LEN(middleware_stack) - 1
        request_context = CALL middleware_stack(i)(request_context)
        IF request_context = NULL THEN
            RETURN {"status": 403, "body": "Forbidden"}
        END IF
    NEXT i
    
    ' Route handling
    IF routes.CONTAINS(route_key) THEN
        RETURN CALL routes(route_key)(request_context)
    ELSE
        RETURN {"status": 404, "body": "Not Found"}
    END IF
END FUNCTION

END LIBRARY
```

#### REST API Örneği
```basic
' api_server.basx
IMPORT "http_server.libx" AS server
IMPORT "user_model.basx" AS UserModel

' Middleware: Logging
DEF FUNCTION logging_middleware(request)
    PRINT "[" + DATE$() + " " + TIME$() + "] " + 
          request("method") + " " + request("path")
    RETURN request
END FUNCTION

' Middleware: Authentication
DEF FUNCTION auth_middleware(request)
    IF request("path").STARTS_WITH("/api/") THEN
        IF NOT request("headers").CONTAINS("Authorization") THEN
            RETURN NULL  ' Unauthorized
        END IF
    END IF
    RETURN request
END FUNCTION

' API Endpoints
DEF FUNCTION get_users_api(request)
    DIM users AS ARRAY
    users = UserModel.User_find_all()
    
    RETURN {
        "status": 200,
        "headers": {"Content-Type": "application/json"},
        "body": JSON_STRINGIFY(users)
    }
END FUNCTION

DEF FUNCTION create_user_api(request)
    DIM user_data AS DICT
    user_data = JSON_PARSE(request("data"))
    
    ' Validation
    IF NOT user_data.CONTAINS("name") OR NOT user_data.CONTAINS("email") THEN
        RETURN {
            "status": 400,
            "body": JSON_STRINGIFY({"error": "Missing required fields"})
        }
    END IF
    
    DIM new_user AS DICT
    new_user = UserModel.User_create(
        user_data("name"),
        user_data("email"),
        user_data("age")
    )
    
    IF new_user <> NULL THEN
        RETURN {
            "status": 201,
            "body": JSON_STRINGIFY(new_user)
        }
    ELSE
        RETURN {
            "status": 500,
            "body": JSON_STRINGIFY({"error": "Failed to create user"})
        }
    END IF
END FUNCTION

' Server setup
server.add_middleware(logging_middleware)
server.add_middleware(auth_middleware)
server.register_route("GET", "/api/users", get_users_api)
server.register_route("POST", "/api/users", create_user_api)

' Server simulation
DEF SUB simulate_requests()
    DIM response AS DICT
    
    ' Test GET request
    response = server.handle_request("GET", "/api/users", "")
    PRINT "GET /api/users:", response("status"), response("body")
    
    ' Test POST request
    DIM post_data AS STRING
    post_data = '{"name": "John Doe", "email": "john@example.com", "age": 30}'
    response = server.handle_request("POST", "/api/users", post_data)
    PRINT "POST /api/users:", response("status")
END SUB

simulate_requests()
```

---

## 37. 🎨 Console GUI ve Görselleştirme

### 1. ASCII Art ve Box Drawing

```basic
' console_gui.libx
LIBRARY ConsoleGUI

' Box drawing characters
DIM BOX_CHARS AS DICT
BOX_CHARS = {
    "top_left": "┌",
    "top_right": "┐", 
    "bottom_left": "└",
    "bottom_right": "┘",
    "horizontal": "─",
    "vertical": "│",
    "cross": "┼"
}

DEF SUB draw_box(x, y, width, height, title)
    ' Top border
    LOCATE y, x
    PRINT BOX_CHARS("top_left") + STRING$(width - 2, BOX_CHARS("horizontal")) + BOX_CHARS("top_right")
    
    ' Side borders
    FOR i = 1 TO height - 2
        LOCATE y + i, x
        PRINT BOX_CHARS("vertical") + STRING$(width - 2, " ") + BOX_CHARS("vertical")
    NEXT i
    
    ' Bottom border
    LOCATE y + height - 1, x
    PRINT BOX_CHARS("bottom_left") + STRING$(width - 2, BOX_CHARS("horizontal")) + BOX_CHARS("bottom_right")
    
    ' Title
    IF title <> "" THEN
        LOCATE y, x + 2
        PRINT "[ " + title + " ]"
    END IF
END SUB

DEF SUB draw_menu(x, y, items, selected_index)
    FOR i = 0 TO LEN(items) - 1
        LOCATE y + i, x
        IF i = selected_index THEN
            PRINT "► " + items(i)
        ELSE
            PRINT "  " + items(i)
        END IF
    NEXT i
END SUB

DEF SUB draw_progress_bar(x, y, width, percentage, label)
    DIM filled_width AS INTEGER
    filled_width = (width * percentage) / 100
    
    LOCATE y, x
    PRINT label + " ["
    PRINT STRING$(filled_width, "█")
    PRINT STRING$(width - filled_width, "░")
    PRINT "] " + STR$(percentage) + "%"
END SUB

DEF SUB draw_chart(data_array, chart_title, max_height)
    PRINT
    PRINT "═══ " + chart_title + " ═══"
    
    DIM max_val AS DOUBLE
    max_val = MAX(data_array)
    
    ' Y-axis (tersden)
    FOR level = max_height TO 1 STEP -1
        DIM threshold AS DOUBLE
        threshold = (max_val * level) / max_height
        
        PRINT STR$(ROUND(threshold, 0)) + " │"
        
        FOR i = 0 TO LEN(data_array) - 1
            IF data_array(i) >= threshold THEN
                PRINT "██"
            ELSE
                PRINT "  "
            END IF
        NEXT i
        PRINT
    NEXT level
    
    ' X-axis
    PRINT "0 └" + STRING$(LEN(data_array) * 2, "─")
    PRINT "   "
    FOR i = 0 TO LEN(data_array) - 1
        PRINT STR$(i + 1) + " "
    NEXT i
    PRINT
END SUB

END LIBRARY
```

### 2. Interactive Dashboard

```basic
' dashboard.basx
IMPORT "console_gui.libx" AS gui

DIM dashboard_data AS DICT
dashboard_data = {
    "cpu_usage": 45,
    "memory_usage": 67,
    "disk_usage": 23,
    "network_in": 1024,
    "network_out": 512,
    "active_users": 15
}

DEF SUB draw_dashboard()
    CLS  ' Ekranı temizle
    
    ' Ana başlık
    PRINT "╔══════════════════════════════════════════════════════════════════════════╗"
    PRINT "║                          SYSTEM DASHBOARD                               ║"
    PRINT "║                        pdsXv11g Monitoring                              ║"
    PRINT "╚══════════════════════════════════════════════════════════════════════════╝"
    PRINT
    
    ' Sol panel - Sistem bilgileri
    gui.draw_box(1, 5, 35, 15, "System Information")
    
    LOCATE 7, 3
    PRINT "System: pdsXv11g Runtime"
    LOCATE 8, 3
    PRINT "Version: 1.0.0"
    LOCATE 9, 3
    PRINT "Uptime: " + STR$(TIMER / 3600) + " hours"
    LOCATE 10, 3
    PRINT "Date: " + DATE$()
    LOCATE 11, 3
    PRINT "Time: " + TIME$()
    
    ' Progress bars
    LOCATE 13, 3
    PRINT "CPU Usage:"
    gui.draw_progress_bar(3, 14, 25, dashboard_data("cpu_usage"), "")
    
    LOCATE 15, 3
    PRINT "Memory:"
    gui.draw_progress_bar(3, 16, 25, dashboard_data("memory_usage"), "")
    
    LOCATE 17, 3
    PRINT "Disk Space:"
    gui.draw_progress_bar(3, 18, 25, dashboard_data("disk_usage"), "")
    
    ' Sağ panel - Network ve kullanıcı bilgileri
    gui.draw_box(40, 5, 35, 15, "Network & Users")
    
    LOCATE 7, 42
    PRINT "Active Users: " + STR$(dashboard_data("active_users"))
    LOCATE 8, 42
    PRINT "Network In:  " + STR$(dashboard_data("network_in")) + " KB/s"
    LOCATE 9, 42
    PRINT "Network Out: " + STR$(dashboard_data("network_out")) + " KB/s"
    
    ' Alt panel - Grafik
    DIM sample_data AS ARRAY
    sample_data = [10, 15, 8, 20, 25, 18, 22, 16, 12, 28]
    gui.draw_chart(sample_data, "Performance History (last 10 minutes)", 8)
END SUB

DEF SUB update_dashboard_data()
    ' Simulated data updates
    dashboard_data("cpu_usage") = RND(20, 80)
    dashboard_data("memory_usage") = RND(40, 90)
    dashboard_data("disk_usage") = RND(10, 50)
    dashboard_data("network_in") = RND(500, 2000)
    dashboard_data("network_out") = RND(300, 1500)
    dashboard_data("active_users") = RND(10, 25)
END SUB

' Ana döngü
DIM running AS BOOLEAN
running = TRUE

WHILE running
    draw_dashboard()
    
    PRINT
    PRINT "Commands: [R]efresh | [Q]uit | [S]ettings"
    
    DIM command AS STRING
    command = GETKEY("R,Q,S")
    
    SELECT CASE UPPER$(command)
        CASE "R"
            update_dashboard_data()
        CASE "Q"
            running = FALSE
        CASE "S"
            ' Settings menu implementation
            PRINT "Settings menu (not implemented yet)"
            WAIT 2000
    END SELECT
WEND

PRINT "Dashboard closed."
```

---

## 38. 📁 Dosya Formatları ve Veri Serializasyonu

### 1. JSON İşleme

```basic
' json_utils.libx
LIBRARY JSONUtils

DEF FUNCTION json_escape_string(input_str)
    DIM result AS STRING
    result = input_str
    result = REPLACE(result, "\", "\\")
    result = REPLACE(result, """", "\""")
    result = REPLACE(result, CHR$(10), "\n")
    result = REPLACE(result, CHR$(13), "\r")
    result = REPLACE(result, CHR$(9), "\t")
    RETURN result
END FUNCTION

DEF FUNCTION json_stringify(obj)
    DIM obj_type AS STRING
    obj_type = TYPE_OF(obj)
    
    SELECT CASE obj_type
        CASE "STRING"
            RETURN """" + json_escape_string(obj) + """"
            
        CASE "INTEGER", "DOUBLE"
            RETURN STR$(obj)
            
        CASE "BOOLEAN"
            IF obj THEN
                RETURN "true"
            ELSE
                RETURN "false"
            END IF
            
        CASE "ARRAY"
            DIM result AS STRING
            result = "["
            FOR i = 0 TO LEN(obj) - 1
                IF i > 0 THEN result = result + ","
                result = result + json_stringify(obj(i))
            NEXT i
            result = result + "]"
            RETURN result
            
        CASE "DICT"
            DIM result AS STRING
            result = "{"
            DIM first AS BOOLEAN
            first = TRUE
            
            FOR key IN obj.KEYS()
                IF NOT first THEN result = result + ","
                result = result + """" + key + """:" + json_stringify(obj(key))
                first = FALSE
            NEXT key
            
            result = result + "}"
            RETURN result
            
        CASE ELSE
            RETURN "null"
    END SELECT
END FUNCTION

END LIBRARY
```

### 2. CSV İşleme

```basic
' csv_utils.libx
LIBRARY CSVUtils

DEF FUNCTION csv_parse(csv_content, delimiter)
    DIM lines AS ARRAY
    lines = SPLIT(csv_content, CHR$(10))
    
    DIM result AS ARRAY
    result = []
    
    FOR i = 0 TO LEN(lines) - 1
        DIM line AS STRING
        line = TRIM(lines(i))
        
        IF line <> "" THEN
            DIM fields AS ARRAY
            fields = csv_parse_line(line, delimiter)
            INSERT(result, fields)
        END IF
    NEXT i
    
    RETURN result
END FUNCTION

DEF FUNCTION csv_parse_line(line, delimiter)
    DIM fields AS ARRAY
    fields = []
    
    DIM current_field AS STRING
    current_field = ""
    
    DIM in_quotes AS BOOLEAN
    in_quotes = FALSE
    
    FOR i = 1 TO LEN(line)
        DIM char AS STRING
        char = MID$(line, i, 1)
        
        IF char = """" THEN
            in_quotes = NOT in_quotes
        ELSEIF char = delimiter AND NOT in_quotes THEN
            INSERT(fields, TRIM(current_field))
            current_field = ""
        ELSE
            current_field = current_field + char
        END IF
    NEXT i
    
    INSERT(fields, TRIM(current_field))
    RETURN fields
END FUNCTION

DEF FUNCTION csv_stringify(data_array, delimiter)
    DIM result AS STRING
    result = ""
    
    FOR i = 0 TO LEN(data_array) - 1
        IF i > 0 THEN result = result + CHR$(10)
        
        DIM row AS ARRAY
        row = data_array(i)
        
        FOR j = 0 TO LEN(row) - 1
            IF j > 0 THEN result = result + delimiter
            
            DIM field AS STRING
            field = STR$(row(j))
            
            ' Quote if contains delimiter or quotes
            IF INSTR(1, field, delimiter) > 0 OR INSTR(1, field, """") > 0 THEN
                field = REPLACE(field, """", """""")
                field = """" + field + """"
            END IF
            
            result = result + field
        NEXT j
    NEXT i
    
    RETURN result
END FUNCTION

END LIBRARY
```

### 3. Configuration Management

```basic
' config_manager.libx
LIBRARY ConfigManager

DIM config_data AS DICT
config_data = {}

DEF FUNCTION load_config(config_file_path)
    TRY
        DIM file_content AS STRING
        file_content = READ_TEXT_FILE(config_file_path)
        
        DIM lines AS ARRAY
        lines = SPLIT(file_content, CHR$(10))
        
        FOR i = 0 TO LEN(lines) - 1
            DIM line AS STRING
            line = TRIM(lines(i))
            
            ' Skip comments and empty lines
            IF line <> "" AND NOT line.STARTS_WITH("#") AND NOT line.STARTS_WITH(";") THEN
                DIM parts AS ARRAY
                parts = SPLIT(line, "=")
                
                IF LEN(parts) >= 2 THEN
                    DIM key AS STRING
                    DIM value AS STRING
                    key = TRIM(parts(0))
                    value = TRIM(parts(1))
                    
                    ' Remove quotes if present
                    IF value.STARTS_WITH("""") AND value.ENDS_WITH("""") THEN
                        value = MID$(value, 2, LEN(value) - 2)
                    END IF
                    
                    config_data(key) = value
                END IF
            END IF
        NEXT i
        
        RETURN TRUE
    CATCH error DO
        PRINT "Failed to load config:", error
        RETURN FALSE
    END TRY
END FUNCTION

DEF FUNCTION get_config(key, default_value)
    IF config_data.CONTAINS(key) THEN
        RETURN config_data(key)
    ELSE
        RETURN default_value
    END IF
END FUNCTION

DEF SUB set_config(key, value)
    config_data(key) = value
END SUB

DEF FUNCTION save_config(config_file_path)
    TRY
        DIM content AS STRING
        content = "# Configuration file generated by pdsXv11g" + CHR$(10)
        content = content + "# Generated at: " + DATE$() + " " + TIME$() + CHR$(10)
        content = content + CHR$(10)
        
        FOR key IN config_data.KEYS()
            content = content + key + " = """ + STR$(config_data(key)) + """" + CHR$(10)
        NEXT key
        
        WRITE_TEXT_FILE(config_file_path, content)
        RETURN TRUE
    CATCH error DO
        PRINT "Failed to save config:", error
        RETURN FALSE
    END TRY
END FUNCTION

END LIBRARY
```

---

## 39. 🔐 Security ve Kriptografi

### 1. Hash Fonksiyonları

```basic
' crypto_utils.libx
LIBRARY CryptoUtils

' Simple hash function (not cryptographically secure, for educational purposes)
DEF FUNCTION simple_hash(input_string)
    DIM hash_value AS LONG
    hash_value = 0
    
    FOR i = 1 TO LEN(input_string)
        DIM char_code AS INTEGER
        char_code = ASC(MID$(input_string, i, 1))
        hash_value = ((hash_value * 31) + char_code) MOD 2147483647
    NEXT i
    
    RETURN ABS(hash_value)
END FUNCTION

' Caesar cipher implementation
DEF FUNCTION caesar_encrypt(plaintext, shift)
    DIM result AS STRING
    result = ""
    
    FOR i = 1 TO LEN(plaintext)
        DIM char AS STRING
        char = MID$(plaintext, i, 1)
        DIM ascii_val AS INTEGER
        ascii_val = ASC(char)
        
        ' Handle uppercase letters
        IF ascii_val >= 65 AND ascii_val <= 90 THEN
            ascii_val = ((ascii_val - 65 + shift) MOD 26) + 65
        ' Handle lowercase letters
        ELSEIF ascii_val >= 97 AND ascii_val <= 122 THEN
            ascii_val = ((ascii_val - 97 + shift) MOD 26) + 97
        END IF
        
        result = result + CHR$(ascii_val)
    NEXT i
    
    RETURN result
END FUNCTION

DEF FUNCTION caesar_decrypt(ciphertext, shift)
    RETURN caesar_encrypt(ciphertext, -shift)
END FUNCTION

' XOR cipher
DEF FUNCTION xor_encrypt(plaintext, key)
    DIM result AS STRING
    result = ""
    
    DIM key_len AS INTEGER
    key_len = LEN(key)
    
    FOR i = 1 TO LEN(plaintext)
        DIM plain_char AS INTEGER
        DIM key_char AS INTEGER
        plain_char = ASC(MID$(plaintext, i, 1))
        key_char = ASC(MID$(key, ((i - 1) MOD key_len) + 1, 1))
        
        DIM encrypted_char AS INTEGER
        encrypted_char = plain_char XOR key_char
        
        result = result + CHR$(encrypted_char)
    NEXT i
    
    RETURN result
END FUNCTION

' XOR decrypt (same as encrypt for XOR)
DEF FUNCTION xor_decrypt(ciphertext, key)
    RETURN xor_encrypt(ciphertext, key)
END FUNCTION

END LIBRARY
```

### 2. Input Validation

```basic
' validation.libx
LIBRARY ValidationUtils

DEF FUNCTION validate_email(email)
    ' Basic email validation
    IF LEN(email) < 5 THEN RETURN FALSE
    IF INSTR(1, email, "@") = 0 THEN RETURN FALSE
    IF INSTR(1, email, ".") = 0 THEN RETURN FALSE
    
    DIM at_pos AS INTEGER
    at_pos = INSTR(1, email, "@")
    
    ' Check if @ is not at start or end
    IF at_pos = 1 OR at_pos = LEN(email) THEN RETURN FALSE
    
    ' Check for multiple @
    IF INSTR(at_pos + 1, email, "@") > 0 THEN RETURN FALSE
    
    RETURN TRUE
END FUNCTION

DEF FUNCTION validate_password(password, min_length)
    IF LEN(password) < min_length THEN RETURN FALSE
    
    DIM has_upper AS BOOLEAN
    DIM has_lower AS BOOLEAN
    DIM has_digit AS BOOLEAN
    DIM has_special AS BOOLEAN
    
    has_upper = FALSE
    has_lower = FALSE
    has_digit = FALSE
    has_special = FALSE
    
    FOR i = 1 TO LEN(password)
        DIM char AS STRING
        char = MID$(password, i, 1)
        DIM ascii_val AS INTEGER
        ascii_val = ASC(char)
        
        IF ascii_val >= 65 AND ascii_val <= 90 THEN
            has_upper = TRUE
        ELSEIF ascii_val >= 97 AND ascii_val <= 122 THEN
            has_lower = TRUE
        ELSEIF ascii_val >= 48 AND ascii_val <= 57 THEN
            has_digit = TRUE
        ELSE
            has_special = TRUE
        END IF
    NEXT i
    
    RETURN has_upper AND has_lower AND has_digit AND has_special
END FUNCTION

DEF FUNCTION sanitize_input(user_input)
    DIM result AS STRING
    result = user_input
    
    ' Remove potentially dangerous characters
    result = REPLACE(result, "<", "&lt;")
    result = REPLACE(result, ">", "&gt;")
    result = REPLACE(result, "&", "&amp;")
    result = REPLACE(result, """", "&quot;")
    result = REPLACE(result, "'", "&#x27;")
    
    ' Remove control characters
    DIM cleaned AS STRING
    cleaned = ""
    
    FOR i = 1 TO LEN(result)
        DIM char AS STRING
        char = MID$(result, i, 1)
        DIM ascii_val AS INTEGER
        ascii_val = ASC(char)
        
        ' Keep printable characters and common whitespace
        IF (ascii_val >= 32 AND ascii_val <= 126) OR ascii_val = 9 OR ascii_val = 10 OR ascii_val = 13 THEN
            cleaned = cleaned + char
        END IF
    NEXT i
    
    RETURN TRIM(cleaned)
END FUNCTION

END LIBRARY
```

### 3. Session Management

```basic
' session_manager.libx
LIBRARY SessionManager

DIM active_sessions AS DICT
active_sessions = {}

DEF FUNCTION create_session(user_id)
    DIM session_id AS STRING
    session_id = generate_session_id()
    
    DIM session_data AS DICT
    session_data = {
        "user_id": user_id,
        "created_at": TIMER,
        "last_accessed": TIMER,
        "data": {}
    }
    
    active_sessions(session_id) = session_data
    RETURN session_id
END FUNCTION

DEF FUNCTION generate_session_id()
    DIM random_string AS STRING
    random_string = ""
    
    ' Generate random alphanumeric string
    FOR i = 1 TO 32
        DIM char_type AS INTEGER
        char_type = RND(1, 3)
        
        IF char_type = 1 THEN
            ' Digit
            random_string = random_string + CHR$(RND(48, 57))
        ELSEIF char_type = 2 THEN
            ' Uppercase letter
            random_string = random_string + CHR$(RND(65, 90))
        ELSE
            ' Lowercase letter
            random_string = random_string + CHR$(RND(97, 122))
        END IF
    NEXT i
    
    RETURN random_string
END FUNCTION

DEF FUNCTION validate_session(session_id)
    IF NOT active_sessions.CONTAINS(session_id) THEN
        RETURN FALSE
    END IF
    
    DIM session AS DICT
    session = active_sessions(session_id)
    
    ' Check if session expired (1 hour timeout)
    IF (TIMER - session("last_accessed")) > 3600 THEN
        REMOVE(active_sessions, session_id)
        RETURN FALSE
    END IF
    
    ' Update last accessed time
    session("last_accessed") = TIMER
    RETURN TRUE
END FUNCTION

DEF SUB destroy_session(session_id)
    IF active_sessions.CONTAINS(session_id) THEN
        REMOVE(active_sessions, session_id)
    END IF
END SUB

END LIBRARY
```

Bu eklenen bölümlerle birlikte kullanım kılavuzu artık tam kapsamlı bir kaynak haline geldi ve şu alanları kapsıyor:

✅ **Modül sistemi ve kütüphane geliştirme**
✅ **Veritabanı işlemleri ve ORM pattern'ları**  
✅ **Network programming ve HTTP server simülasyonu**
✅ **Console GUI ve dashboard geliştirme**
✅ **Dosya formatları (JSON, CSV) işleme**
✅ **Security ve kriptografi temelleri**
✅ **Session management ve validation**

Bu yeni bölümler, pdsXv11g ile profesyonel düzeyde uygulama geliştirmek isteyen programcılar için kapsamlı bir rehber oluşturuyor! 🚀

```

---

## 40. 🚨 Hata Mesajları ve Anlamları

pdsXv11g, programlama hatalarını tespit etmek ve çözmek için ayrıntılı hata mesajları sunar. Bu bölümde, karşılaşabileceğiniz tüm hata mesajları, anlamları ve çözüm önerileri açıklanmaktadır.

### 📋 Syntax Hataları (Derleme Zamanı)

#### Variable ve Naming Hataları
```
❌ Hata: "Tanimlanmamis degisken: variable_name"
🔍 Anlam: Kullanmaya çalıştığınız değişken DIM ile tanımlanmamış
✅ Çözüm: DIM variable_name AS TYPE şeklinde önce tanımlayın

❌ Hata: "Gecersiz degisken adi: 123name" 
🔍 Anlam: Değişken adı sayı ile başlayamaz
✅ Çözüm: name123 gibi harf ile başlayan bir ad kullanın

❌ Hata: "Rezerve edilmis kelime kullanimi: IF"
🔍 Anlam: IF, FOR, WHILE gibi rezerve kelimeleri değişken adı olarak kullanamazsınız
✅ Çözüm: my_if, user_input gibi farklı bir ad seçin
```

#### DIM ve Type Hataları
```
❌ Hata: "DIM komutunda sozdizimi hatasi"
🔍 Anlam: DIM syntax'ı yanlış kullanılmış
✅ Çözüm: DIM variable_name AS TYPE veya DIM array_name(size) AS TYPE

❌ Hata: "Desteklenmeyen veri tipi: INVALID_TYPE"
🔍 Anlam: Geçersiz bir veri tipi belirtilmiş
✅ Çözüm: STRING, INTEGER, DOUBLE, BOOLEAN, ARRAY, LIST, DICT gibi geçerli tipler kullanın

❌ Hata: "Dizi boyutu negatif olamaz: -5"
🔍 Anlam: DIM array(-5) gibi negatif boyut belirtilmiş
✅ Çözüm: DIM array(10) gibi pozitif boyut kullanın
```

#### IF-THEN-ELSE Hataları
```
❌ Hata: "IF icin eslesen END IF bulunamadi"
🔍 Anlam: IF bloğu END IF ile kapatılmamış
✅ Çözüm: Her IF için bir END IF ekleyin

❌ Hata: "ELSE icin eslesen IF bulunamadi"
🔍 Anlam: ELSE komutu bir IF bloğunun içinde değil
✅ Çözüm: ELSE'i IF...END IF bloğu içine yerleştirin

❌ Hata: "IF komutunda sozdizimi hatasi"
🔍 Anlam: IF condition THEN formatı doğru kullanılmamış
✅ Çözüm: IF condition THEN veya IF condition THEN command formatını kullanın
```

#### Loop Hataları
```
❌ Hata: "FOR icin eslesen NEXT bulunamadi"
🔍 Anlam: FOR döngüsü NEXT ile kapatılmamış
✅ Çözüm: Her FOR için bir NEXT ekleyin

❌ Hata: "NEXT icin eslesen FOR bulunamadi"
🔍 Anlam: NEXT komutu bir FOR döngüsünün içinde değil
✅ Çözüm: NEXT'i FOR...NEXT bloğu içine yerleştirin

❌ Hata: "WHILE icin eslesen WEND bulunamadi"
🔍 Anlam: WHILE döngüsü WEND ile kapatılmamış
✅ Çözüm: Her WHILE için bir WEND ekleyin

❌ Hata: "DO icin eslesen LOOP bulunamadi"
🔍 Anlam: DO döngüsü LOOP ile kapatılmamış
✅ Çözüm: Her DO için bir LOOP ekleyin

❌ Hata: "FOR komutunda sozdizimi hatasi"
🔍 Anlam: FOR i = 1 TO 10 formatı yanlış
✅ Çözüm: FOR variable = start TO end [STEP increment] formatını kullanın
```

#### Function ve Sub Hataları
```
❌ Hata: "FUNCTION icin eslesen END FUNCTION bulunamadi"
🔍 Anlam: DEF FUNCTION bloğu END FUNCTION ile kapatılmamış
✅ Çözüm: Her DEF FUNCTION için END FUNCTION ekleyin

❌ Hata: "SUB icin eslesen END SUB bulunamadi"
🔍 Anlam: DEF SUB bloğu END SUB ile kapatılmamış
✅ Çözüm: Her DEF SUB için END SUB ekleyin

❌ Hata: "Fonksiyon zaten tanimli: function_name"
🔍 Anlam: Aynı isimde fonksiyon iki kez tanımlanmış
✅ Çözüm: Farklı bir fonksiyon adı kullanın veya mevcut tanımı silin
```

#### SELECT CASE Hataları
```
❌ Hata: "SELECT CASE icin eslesen END SELECT bulunamadi"
🔍 Anlam: SELECT CASE bloğu END SELECT ile kapatılmamış
✅ Çözüm: SELECT CASE'den sonra END SELECT ekleyin

❌ Hata: "CASE icin eslesen SELECT bulunamadi"
🔍 Anlam: CASE komutu SELECT CASE bloğunun dışında
✅ Çözüm: CASE'leri SELECT CASE...END SELECT bloğu içine yerleştirin
```

### ⚠️ Runtime Hataları (Çalışma Zamanı)

#### Matematik Hataları
```
❌ Hata: "Sifira bolme hatasi"
🔍 Anlam: Bir sayı 0'a bölünmeye çalışılıyor
✅ Çözüm: Bölmeden önce payda kontrolü yapın:
    IF denominator <> 0 THEN
        result = numerator / denominator
    ELSE
        PRINT "Hata: Sıfıra bölme!"
    END IF

❌ Hata: "Matematik fonksiyonu alanı disi: SQRT(-1)"
🔍 Anlam: Negatif sayının kareköku alınmaya çalışılıyor
✅ Çözüm: Parametre kontrolü yapın:
    IF number >= 0 THEN
        result = SQR(number)
    ELSE
        PRINT "Hata: Negatif sayının kökü alınamaz"
    END IF

❌ Hata: "Overflow hatasi: Sayi cok buyuk"
🔍 Anlam: Hesaplama sonucu INTEGER veya DOUBLE sınırlarını aşıyor
✅ Çözüm: LONG veya daha büyük veri tipi kullanın
```

#### Array ve Index Hataları
```
❌ Hata: "Dizi indisi sinir disi: array_name(15)"
🔍 Anlam: 10 elemanlı dizinin 15. elemanına erişmeye çalışılıyor
✅ Çözüm: İndeks kontrolü yapın:
    IF index >= 0 AND index < LEN(array_name) THEN
        value = array_name(index)
    ELSE
        PRINT "Geçersiz indeks"
    END IF

❌ Hata: "Tanimlanmamis dizi: array_name"
🔍 Anlam: DIM ile tanımlanmamış diziye erişim
✅ Çözüm: Önce DIM array_name(size) AS TYPE ile tanımlayın

❌ Hata: "Cok boyutlu dizi indisi hatasi: matrix(1,2,3,4)"
🔍 Anlam: 2D dizi için 4 boyut indeksi verilmiş
✅ Çözüm: Doğru boyut sayısını kullanın: matrix(1,2) gibi
```

#### String İşlem Hataları
```
❌ Hata: "String indisi sinir disi: MID$(str, 10, 5)"
🔍 Anlam: 5 karakterlik string'in 10. karakterinden itibaren almaya çalışılıyor
✅ Çözüm: String uzunluğunu kontrol edin:
    IF start_pos <= LEN(text) THEN
        result = MID$(text, start_pos, length)
    END IF

❌ Hata: "Geçersiz string dönüştürme: VAL('abc')"
🔍 Anlam: Sayısal olmayan string'i sayıya çevirmeye çalışılıyor
✅ Çözüm: ISNUMERIC() ile kontrol edin:
    IF ISNUMERIC(text) THEN
        number = VAL(text)
    ELSE
        number = 0  ' Varsayılan değer
    END IF
```

#### Type Mismatch Hataları
```
❌ Hata: "Tip uyusmazligi: STRING ve INTEGER"
🔍 Anlam: STRING değişkene INTEGER değer atanmaya çalışılıyor
✅ Çözüm: STR$() veya VAL() fonksiyonları ile dönüşüm yapın:
    DIM text AS STRING = STR$(number)
    DIM number AS INTEGER = VAL(text)

❌ Hata: "Boolean deger bekleniyor: IF 'text' THEN"
🔍 Anlam: IF koşulunda string kullanılmış
✅ Çözüm: Doğru karşılaştırma operatörü kullanın:
    IF text <> "" THEN
    IF LEN(text) > 0 THEN
```

#### File ve I/O Hataları
```
❌ Hata: "Dosya bulunamadi: data.txt"
🔍 Anlam: Belirtilen dosya mevcut değil
✅ Çözüm: EXISTS() fonksiyonu ile kontrol edin:
    IF EXISTS("data.txt") THEN
        content = READ_file("data.txt")
    ELSE
        PRINT "Dosya bulunamadı"
    END IF

❌ Hata: "Dosya yazma izni yok: C:\Windows\system32\file.txt"
🔍 Anlam: Korumalı dizine yazma izni yok
✅ Çözüm: Farklı bir dizin kullanın veya yetki isteyin

❌ Hata: "Dosya zaten açık: data.txt"
🔍 Anlam: Aynı dosya iki kez açılmaya çalışılıyor
✅ Çözüm: CLOSE komutu ile önce kapatın
```

#### Memory ve Resource Hataları
```
❌ Hata: "Yetersiz bellek: Dizi çok büyük"
🔍 Anlam: Çok büyük dizi oluşturmak için yeterli RAM yok
✅ Çözüm: Daha küçük boyut kullanın veya belleği temizleyin

❌ Hata: "Maksimum recursion siniri asildi"
🔍 Anlam: Fonksiyon kendini çok derin çağırmış
✅ Çözüm: Base case kontrolü ekleyin:
    DEF FUNCTION factorial(n)
        IF n <= 1 THEN RETURN 1  ' Base case
        RETURN n * factorial(n-1)
    END FUNCTION
```

### 🔧 Logic ve Program Flow Hataları

#### Label ve GOTO Hataları
```
❌ Hata: "Etiket bulunamadi: unknown_label"
🔍 Anlam: GOTO ile var olmayan etikete gidilmeye çalışılıyor
✅ Çözüm: Doğru etiket adını kullanın veya etiketi tanımlayın

❌ Hata: "RETURN icin eslesen GOSUB bulunamadi"
🔍 Anlam: GOSUB olmadan RETURN kullanılmış
✅ Çözüm: RETURN'ü sadece GOSUB'dan sonra kullanın
```

#### Function Call Hataları
```
❌ Hata: "Parametre uyusmazligi: function_name"
🔍 Anlam: Fonksiyona yanlış sayıda parametre gönderilmiş
✅ Çözüm: Fonksiyon tanımındaki parametre sayısını kontrol edin

❌ Hata: "Tanimlanmamis fonksiyon: unknown_function"
🔍 Anlam: Var olmayan fonksiyon çağrılmaya çalışılıyor
✅ Çözüm: Fonksiyon adını kontrol edin veya DEF FUNCTION ile tanımlayın

❌ Hata: "Fonksiyon deger dondurmuyor: function_name"
🔍 Anlam: RETURN olmayan fonksiyondan değer almaya çalışılıyor
✅ Çözüm: Fonksiyona RETURN statement ekleyin
```

---

## 41. 📝 String Array Functions - Gelişmiş String Array İşlemleri (YENİ - pdsXv11g)

pdsXv11g, string dizileri üzerinde toplu işlemler yapabileceğiniz 20'den fazla özel fonksiyon sunar. Bu fonksiyonlar, metin işleme, veri temizleme ve string manipülasyonu için optimize edilmiştir.

**Tam String Array Functions Listesi:**
| Fonksiyon | Açıklama |
|-----------|----------|
| `STRARRAY()` | String Array Oluşturma |
| `STRGET()` | String Array Element Erişimi |
| `STRSET()` | String Array Element Atama |
| `STRLEN()` | String Array Length İşlemleri |
| `STRCAT()` | String Array Birleştirme |
| `STRSPLIT()` | String'i Array'e Bölme |
| `STRJOIN()` | Array'i String'e Birleştirme |
| `STRFIND()` | String Array'de Arama |
| `STRREPLACE()` | String Array'de Değiştirme |
| `STRCOMPARE()` | String Array Karşılaştırma |
| `STRTRIM()` | String Array Trim İşlemleri |
| `STRPAD()` | String Array Padding İşlemleri |
| `STRSUBSTR()` | String Array Substring İşlemleri |
| `STRREVERSE()` | String Array Tersine Çevirme |
| `STRMATCH()` | Pattern Matching (Regex Desteği) |
| `STRCOUNT()` | String Array'de Sayma İşlemleri |
| `STRLOWER()` | Küçük Harf Dönüşümü |
| `STRUPPER()` | Büyük Harf Dönüşümü |
| `STRTITLE()` | Title Case Dönüşümü |
| `STRSWAP()` | Karakter Değiştirme |

#### 1. STRARRAY() - String Array Oluşturma
```basic
DIM str_arr AS ARRAY = STRARRAY(boyut, varsayılan_değer)

' Örnekler:
DIM cities AS ARRAY = STRARRAY(5, "Boş")     ' 5 elemanlı, "Boş" değerli array
DIM names AS ARRAY = STRARRAY(10, "")        ' 10 elemanlı boş string array
DIM buffer AS ARRAY = STRARRAY(100, "N/A")   ' 100 elemanlı, "N/A" değerli
```

#### 2. STRGET() - String Array Element Erişimi
```basic
DIM değer AS STRING = STRGET(string_array, index)

' Örnekler:
DIM cities AS ARRAY = ["İstanbul", "Ankara", "İzmir"]
DIM first_city AS STRING = STRGET(cities, 0)       ' "İstanbul"
DIM second_city AS STRING = STRGET(cities, 1)      ' "Ankara"

' Güvenli erişim (indeks sınır dışı kontrolü)
DIM safe_value AS STRING = STRGET(cities, 5)       ' Sınır dışı ise boş string döner
```

#### 3. STRSET() - String Array Element Atama  
```basic
STRSET(string_array, index, yeni_değer)

' Örnekler:
DIM fruits AS ARRAY = ["elma", "armut", "kiraz"]
STRSET(fruits, 0, "muz")                    ' fruits(0) = "muz"
STRSET(fruits, 3, "üzüm")                   ' Array'i genişletir ve "üzüm" ekler
```

#### 4. STRLEN() - String Array Length İşlemleri
```basic
DIM lengths AS ARRAY = STRLEN(string_array)        ' Her elemanın uzunluğu
DIM tek_uzunluk AS INTEGER = STRLEN("test string")  ' Tek string uzunluğu

' Örnekler:
DIM words AS ARRAY = ["merhaba", "dünya", "pdsx"]
DIM word_lengths AS ARRAY = STRLEN(words)    ' [7, 5, 4]

DIM total_chars AS INTEGER = 0
FOR i = 0 TO LEN(word_lengths) - 1
    total_chars = total_chars + word_lengths(i)
NEXT i
PRINT "Toplam karakter sayısı:", total_chars
```

#### 5. STRCAT() - String Array Birleştirme
```basic
DIM birleşik AS ARRAY = STRCAT(array1, array2)

' Örnekler:
DIM fruits AS ARRAY = ["elma", "armut"]
DIM vegetables AS ARRAY = ["domates", "salatalık"]  
DIM all_foods AS ARRAY = STRCAT(fruits, vegetables)
' Sonuç: ["elma", "armut", "domates", "salatalık"]

' Çoklu array birleştirme
DIM colors1 AS ARRAY = ["kırmızı", "mavi"]
DIM colors2 AS ARRAY = ["yeşil", "sarı"]
DIM colors3 AS ARRAY = ["mor", "turuncu"]
DIM all_colors AS ARRAY = STRCAT(STRCAT(colors1, colors2), colors3)
```

#### 6. STRSPLIT() - String'i Array'e Bölme
```basic
DIM string_array AS ARRAY = STRSPLIT(metin, ayıraç)

' Örnekler:
DIM csv_line AS STRING = "Ali,Veli,Deli,Keli"
DIM names AS ARRAY = STRSPLIT(csv_line, ",")        ' ["Ali", "Veli", "Deli", "Keli"]

DIM sentence AS STRING = "Bu bir test cümlesi"
DIM words AS ARRAY = STRSPLIT(sentence, " ")        ' ["Bu", "bir", "test", "cümlesi"]

DIM path AS STRING = "C:\Users\Admin\Documents\file.txt"
DIM path_parts AS ARRAY = STRSPLIT(path, "\")       ' ["C:", "Users", "Admin", "Documents", "file.txt"]

' Multiple delimiter desteği
DIM complex_text AS STRING = "data1,data2;data3|data4"
DIM data AS ARRAY = STRSPLIT(complex_text, ",;|")   ' ["data1", "data2", "data3", "data4"]
```

#### 7. STRJOIN() - Array'i String'e Birleştirme
```basic
DIM birleşik_string AS STRING = STRJOIN(string_array, ayıraç)

' Örnekler:
DIM cities AS ARRAY = ["İstanbul", "Ankara", "İzmir"]
DIM city_list AS STRING = STRJOIN(cities, ", ")     ' "İstanbul, Ankara, İzmir"
DIM city_csv AS STRING = STRJOIN(cities, ",")       ' "İstanbul,Ankara,İzmir"

DIM file_path AS ARRAY = ["C:", "Users", "Admin", "file.txt"]
DIM full_path AS STRING = STRJOIN(file_path, "\")  ' "C:\Users\Admin\file.txt"

' HTML list oluşturma
DIM items AS ARRAY = ["Madde 1", "Madde 2", "Madde 3"]
DIM html_list AS STRING = "<li>" + STRJOIN(items, "</li><li>") + "</li>"
```

#### 8. STRFIND() - String Array'de Arama
```basic
DIM bulunan_indeksler AS ARRAY = STRFIND(string_array, arama_metni)

' Örnekler:
DIM cities AS ARRAY = ["İstanbul", "Ankara", "İzmir", "Antalya", "Adana"]
DIM an_cities AS ARRAY = STRFIND(cities, "An")      ' [1, 3] (Ankara ve Antalya)

DIM emails AS ARRAY = ["user@gmail.com", "admin@company.com", "test@gmail.com"]
DIM gmail_indices AS ARRAY = STRFIND(emails, "gmail") ' [0, 2]

' Case-insensitive arama
DIM mixed_case AS ARRAY = STRFIND(STRLOWER(mixed_case), "a")  ' Önce küçük harfe çevir

' Partial match kontrolü
FOR i = 0 TO LEN(bulunan_indeksler) - 1
    DIM index AS INTEGER = bulunan_indeksler(i)
    PRINT "Bulunan: " + cities(index) + " (indeks: " + STR$(index) + ")"
NEXT i
```

#### 9. STRREPLACE() - String Array'de Değiştirme
```basic
DIM değiştirilmiş AS ARRAY = STRREPLACE(string_array, eski_metin, yeni_metin)

' Örnekler:
DIM sentences AS ARRAY = ["Bu eski bir cümle", "Eski zaman", "Yeni başlangıç"]
DIM updated AS ARRAY = STRREPLACE(sentences, "eski", "yeni")
' Sonuç: ["Bu yeni bir cümle", "yeni zaman", "Yeni başlangıç"]

' Özel karakter değiştirme
DIM messy_data AS ARRAY = ["data@with#special", "normal_data", "more@data#here"]
DIM clean_data AS ARRAY = STRREPLACE(STRREPLACE(messy_data, "@", "_"), "#", "_")

' HTML temizleme
DIM html_strings AS ARRAY = ["<b>Bold</b>", "<i>Italic</i>", "Normal"]
DIM no_tags AS ARRAY = STRREPLACE(STRREPLACE(html_strings, "<b>", ""), "</b>", "")
```

#### 10. STRCOMPARE() - String Array Karşılaştırma
```basic
DIM karşılaştırma_sonucu AS ARRAY = STRCOMPARE(array1, array2)

' Örnekler:
DIM list1 AS ARRAY = ["elma", "armut", "muz"]
DIM list2 AS ARRAY = ["elma", "kiraz", "muz"]
DIM comparison AS ARRAY = STRCOMPARE(list1, list2)    ' [TRUE, FALSE, TRUE]

' Karşılaştırma sonuçlarını değerlendirme
DIM match_count AS INTEGER = 0
FOR i = 0 TO LEN(comparison) - 1
    IF comparison(i) THEN
        match_count = match_count + 1
    END IF
NEXT i
PRINT "Eşleşme oranı: " + STR$(match_count * 100 / LEN(comparison)) + "%"

' Case-insensitive karşılaştırma
DIM case_insensitive AS ARRAY = STRCOMPARE(STRLOWER(list1), STRLOWER(list2))
```

#### 11. STRTRIM() - String Array Trim İşlemleri
```basic
DIM temizlenmiş AS ARRAY = STRTRIM(string_array)

' Örnekler:
DIM messy_strings AS ARRAY = ["  merhaba  ", "   Bu BiR tEsT cÜmLeSi...   ", "    SONuncu METIN    "]
DIM clean_strings AS ARRAY = STRTRIM(messy_strings)
' Sonuç: ["merhaba", "dünya", "test", "pdsx"]

' Left trim sadece
DIM left_trimmed AS ARRAY = STRLTRIM(messy_strings)

' Right trim sadece  
DIM right_trimmed AS ARRAY = STRRTRIM(messy_strings)

' Özel karakter trimming
DIM special_messy AS ARRAY = ["...data...", "***info***", "~~~test~~~"]
DIM custom_trim AS ARRAY = STRCTRIM(special_messy, ".*~")  ' Belirtilen karakterleri kaldır
```

#### 12. STRPAD() - String Array Padding İşlemleri
```basic
DIM doldurumuş AS ARRAY = STRPAD(string_array, hedef_uzunluk, dolgu_karakteri)

' Örnekler:
DIM numbers AS ARRAY = ["1", "22", "333"]
DIM padded AS ARRAY = STRPAD(numbers, 5, "0")       ' ["00001", "00022", "00333"]

' Right padding
DIM names AS ARRAY = ["Ali", "Mehmet", "A"]
DIM right_padded AS ARRAY = STRRPAD(names, 10, ".")  ' ["Ali.......", "Mehmet....", "A........."]

' Center padding
DIM titles AS ARRAY = ["Başlık", "Alt Başlık", "Son"]
DIM centered AS ARRAY = STRCPAD(titles, 15, "=")     ' Ortalar ve = ile doldurur

' Tablo formatı oluşturma
DIM table_data AS ARRAY = ["İsim", "Yaş", "Şehir"]
DIM formatted AS ARRAY = STRPAD(table_data, 12, " ")
FOR i = 0 TO LEN(formatted) - 1
    PRINT "|" + formatted(i) + "|"
NEXT i
```

#### 13. STRSUBSTR() - String Array Substring İşlemleri
```basic
DIM alt_stringler AS ARRAY = STRSUBSTR(string_array, başlangıç, uzunluk)

' Örnekler:
DIM full_names AS ARRAY = ["Ahmet Yılmaz", "Mehmet Kaya", "Ali Veli"]
DIM first_names AS ARRAY = STRSUBSTR(full_names, 0, 5)  ' İlk 5 karakter
DIM last_chars AS ARRAY = STRSUBSTR(full_names, -4, 4)  ' Son 4 karakter

' Email domainlerini çıkarma
DIM emails AS ARRAY = ["user@gmail.com", "admin@company.co.uk", "test@gmail.com"]
DIM at_positions AS ARRAY = STRFINDCHAR(emails, "@")
' ... domain extraction logic
```

#### 14. STRREVERSE() - String Array Tersine Çevirme
```basic
DIM ters_çevrilmiş AS ARRAY = STRREVERSE(string_array)

' Örnekler:
DIM words AS ARRAY = ["merhaba", "dünya", "pdsx"]
DIM reversed AS ARRAY = STRREVERSE(words)            ' ["abahrem", "aynüd", "xsdp"]

' Palindrome kontrolü
DEF FUNCTION is_palindrome_array(str_array)
    DIM reversed AS ARRAY = STRREVERSE(str_array)
    DIM comparison AS ARRAY = STRCOMPARE(str_array, reversed)
    
    FOR i = 0 TO LEN(comparison) - 1
        IF comparison(i) THEN
            PRINT str_array(i) + " palindrom!"
        END IF
    NEXT i
END FUNCTION

DIM test_words AS ARRAY = ["kayak", "merhaba", "radar", "test"]
is_palindrome_array(test_words)
```

#### 15. STRMATCH() - Pattern Matching (Regex Desteği)
```basic
DIM eşleşenler AS ARRAY = STRMATCH(string_array, regex_pattern)

' Örnekler:
DIM mixed_data AS ARRAY = ["user@gmail.com", "invalid-email", "test@yahoo.com", "not_email"]
DIM emails AS ARRAY = STRMATCH(mixed_data, ".*@.*\.com$")  ' Email pattern
' Sonuç: [TRUE, FALSE, TRUE, FALSE]

' Telefon numarası validation
DIM phone_numbers AS ARRAY = ["0532-123-4567", "invalid", "0216-456-7890"]
DIM valid_phones AS ARRAY = STRMATCH(phone_numbers, "0\d{3}-\d{3}-\d{4}")

' Sadece rakam kontrolü
DIM mixed AS ARRAY = ["12345", "abc123", "67890", "xyz"]
DIM only_digits AS ARRAY = STRMATCH(mixed, "^\d+$")

' IP adresi validation
DIM ips AS ARRAY = ["192.168.1.1", "invalid.ip", "10.0.0.1", "256.1.1.1"]
DIM valid_ips AS ARRAY = STRMATCH(ips, "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
```

#### 16. STRCOUNT() - String Array'de Sayma İşlemleri
```basic
DIM sayılar AS ARRAY = STRCOUNT(string_array, arama_metni)

' Örnekler:
DIM sentences AS ARRAY = ["Bu bir test", "test cümlesi", "başka bir test"]
DIM test_counts AS ARRAY = STRCOUNT(sentences, "test")  ' [1, 1, 1]

' Karakter sayma
DIM texts AS ARRAY = ["merhaba", "dünya", "pdsx"]
DIM a_counts AS ARRAY = STRCOUNT(texts, "a")            ' [3, 1, 0]

' Kelime sayma
DIM paragraphs AS ARRAY = ["İlk paragraf burada", "İkinci daha uzun paragraf"]
DIM word_counts AS ARRAY = STRCOUNT(paragraphs, " ") + 1  ' Boşluk + 1 = kelime sayısı

' Log analizi örneği
DIM log_lines AS ARRAY = [
    "ERROR: Connection failed",
    "INFO: User logged in", 
    "ERROR: Database connection failed",
    "WARNING: Low memory"
]
DIM error_counts AS ARRAY = STRCOUNT(log_lines, "ERROR")
DIM total_errors AS INTEGER = 0
FOR i = 0 TO LEN(error_counts) - 1
    total_errors = total_errors + error_counts(i)
NEXT i
```

#### 17-20. Case Conversion Functions

#### STRLOWER() - Küçük Harf Dönüşümü
```basic
DIM küçük_harf AS ARRAY = STRLOWER(string_array)

DIM mixed_case AS ARRAY = ["MERHABA", "Dünya", "TeSt"]
DIM lowercase AS ARRAY = STRLOWER(mixed_case)      ' ["merhaba", "dünya", "test"]
```

#### STRUPPER() - Büyük Harf Dönüşümü  
```basic
DIM büyük_harf AS ARRAY = STRUPPER(string_array)

DIM names AS ARRAY = ["ahmet", "mehmet", "ayşe"]
DIM uppercase AS ARRAY = STRUPPER(names)           ' ["AHMET", "MEHMET", "AYŞE"]
```

#### STRTITLE() - Title Case Dönüşümü
```basic
DIM title_case AS ARRAY = STRTITLE(string_array)

DIM sentences AS ARRAY = ["merhaba dünya", "bu BİR test"]
DIM title AS ARRAY = STRTITLE(sentences)           ' ["Merhaba Dünya", "Bu Bir Test"]
```

#### STRSWAP() - Karakter Değiştirme
```basic
DIM değiştirilmiş AS ARRAY = STRSWAP(string_array, eski_kar, yeni_kar)

DIM texts AS ARRAY = ["merhaba", "dünya", "test"]
DIM swapped AS ARRAY = STRSWAP(texts, "a", "e")    ' ["merhebe", "aynüd", "test"]
```

### 🎯 String Array Functions - Practical Örnekler

#### CSV Data Processing
```basic
' CSV dosyası işleme örneği
DIM csv_content AS STRING = "Ad,Soyad,Yaş,Şehir
Ali,Veli,25,İstanbul
Mehmet,Kaya,30,Ankara
Ayşe,Yılmaz,28,İzmir"

DIM lines AS ARRAY = STRSPLIT(csv_content, CHR$(10))
DIM headers AS ARRAY = STRSPLIT(lines(0), ",")
DIM clean_headers AS ARRAY = STRTRIM(headers)

PRINT "CSV Headers:"
FOR i = 0 TO LEN(clean_headers) - 1
    PRINT (i + 1) + ". " + clean_headers(i)
NEXT i

' Her satırı işle
FOR i = 1 TO LEN(lines) - 1
    DIM row_data AS ARRAY = STRSPLIT(lines(i), ",")
    DIM clean_data AS ARRAY = STRTRIM(row_data)
    
    PRINT "Kayıt " + STR$(i) + ":"
    FOR j = 0 TO LEN(clean_data) - 1
        PRINT "  " + clean_headers(j) + ": " + clean_data(j)
    NEXT j
NEXT i
```

#### Log File Analysis
```basic
DIM log_entries AS ARRAY = [
    "2024-01-15 10:30:25 INFO User login successful",
    "2024-01-15 10:31:15 ERROR Database connection failed",
    "2024-01-15 10:32:00 WARNING Memory usage high",
    "2024-01-15 10:33:45 INFO Request processed"
]

' Log levels'ı extract et
DIM log_levels AS ARRAY = []
FOR i = 0 TO LEN(log_entries) - 1
    DIM parts AS ARRAY = STRSPLIT(log_entries(i), " ")
    INSERT(log_levels, parts(2))  ' Log level 3. position'da
NEXT i

' Her log level'ın sayısını hesapla
DIM info_count AS INTEGER = 0
DIM error_count AS INTEGER = 0
DIM warning_count AS INTEGER = 0

FOR i = 0 TO LEN(log_levels) - 1
    SELECT CASE log_levels(i)
        CASE "INFO": info_count = info_count + 1
        CASE "ERROR": error_count = error_count + 1
        CASE "WARNING": warning_count = warning_count + 1
    END SELECT
NEXT i

PRINT "Log İstatistikleri:"
PRINT "INFO: " + STR$(info_count)
PRINT "ERROR: " + STR$(error_count)  
PRINT "WARNING: " + STR$(warning_count)
```

#### Text Processing Pipeline
```basic
' Metin işleme pipeline örneği
DIM raw_texts AS ARRAY = [
    "  MERHABA DÜNYA!  ",
    "   Bu BiR tEsT cÜmLeSi...   ",
    "    SONuncu METIN    "
]

PRINT "Orijinal:"
FOR i = 0 TO LEN(raw_texts) - 1
    PRINT (i + 1) + ". '" + raw_texts(i) + "'"
NEXT i

' Pipeline: Trim -> Title Case -> Clean punctuation
DIM step1 AS ARRAY = STRTRIM(raw_texts)               ' Boşlukları temizle
DIM step2 AS ARRAY = STRTITLE(step1)                  ' Title case'e çevir
DIM step3 AS ARRAY = STRREPLACE(step2, "!", "")       ' Ünlem işareti kaldır
DIM final AS ARRAY = STRREPLACE(step3, "...", ".")    ' Çoklu noktayı tekle

PRINT CHR$(10) + "İşlenmiş:"
FOR i = 0 TO LEN(final) - 1
    PRINT (i + 1) + ". '" + final(i) + "'"
NEXT i
```

Bu 20+ String Array fonksiyonu ile pdsXv11g'de güçlü metin işleme operasyonları gerçekleştirebilirsiniz! 🎯




# JSON ve XML Komutları

## JSON Komutları

### 1. JSON Okuma/Yazma
```
READ_JSON dosya_yolu
WRITE_JSON nesne dosya_yolu
```

### 2. JSON Sorgu
```
JSON_QUERY nesne "yol.alt_yol"
Örnek: JSON_QUERY kullanici "adres.sehir"
```

### 3. JSON Şema Doğrulama
```
JSON_VALIDATE nesne schema
```

### 4. JSON Formatlama
```
JSON_FORMAT nesne girinti_sayisi
```

### 5. JSON Birleştirme
```
JSON_MERGE nesne1 nesne2
```

## XML Komutları

### 1. XML Okuma
```
XML_READ dosya_yolu
```

### 2. XML XPath Sorgu
```
XML_FIND root "//eleman[@ozellik='deger']"
```

### 3. XML Oluşturma
```
XML_CREATE eleman_adi ozellikler metin
```

### 4. XML Doğrulama
```
XML_VALIDATE xml_dosya xsd_dosya
```

## Örnekler

### JSON Örneği:
```
# JSON dosyası oku
data = READ_JSON "veri.json"

# Belirli bir değeri sorgula
sehir = JSON_QUERY data "kullanici.adres.sehir"

# Şema doğrulama yap
JSON_VALIDATE data schema

# İki JSON'ı birleştir
sonuc = JSON_MERGE json1 json2
```

### XML Örneği:
```
# XML dosyası oku
root = XML_READ "veri.xml"

# XPath ile eleman bul
elemanlar = XML_FIND root "//kitap[@yazar='Ahmet']"

# Yeni eleman oluştur
yeni = XML_CREATE "kitap" {"yazar": "Mehmet"} "Python Programlama"

# XML doğrulama yap
XML_VALIDATE "veri.xml" "sema.xsd"
```
# PDSX Programlama Dili Kullanım Kılavuzu

## 1. Giriş ve Mimari Yapı

PDSX, modern özelliklere sahip, Türkçe sözdizimi destekleyen, güçlü bir programlama dilidir. Python tabanlı bir yorumlayıcı üzerine inşa edilmiştir ve zengin bir komut seti sunar.

### 1.1 Mimari Yapı

- **Modüler Tasarım**: 
  - Yorumlayıcı (pdsXv11g.py)
  - Komut işleyicileri (pdsx_command_handlers.py)
  - Editör arabirimi (pdsxeditor.py)
  - Tip sistemi ve operatör tabloları (pdsx_command_module.py)
  - Bağımlılık yöneticisi (venv_manager.py)

- **Sanal Ortam Desteği**:
  - Otomatik bağımlılık yönetimi
  - Yerel paket önbelleği (.pdsx_cache)
  - İzole çalışma ortamı (.venv)
  - Internet bağlantısı olmadan çalışabilme
  - requirements.txt tabanlı paket yönetimi

- **Hiyerarşik Komut Yapısı**: 
  - Akış kontrol komutları
  - OOP komutları 
  - Modül ve kütüphane komutları
  - Dosya ve I/O komutları
  - Veritabanı komutları
  - Network ve web komutları
  - GUI ve olay komutları
  - Thread ve process komutları
  - Hata ayıklama komutları
  - AI/ML komutları

### 1.2 Çalışma Mantığı

1. Program başlatma:
   - Sanal ortam kontrolü
   - Bağımlılıkların yüklenmesi/kontrolü
   - Cache yönetimi

2. Program çalıştırma:
   - Program dosyası satır satır okunur
   - Her satır ayrıştırılır ve işleyiciye yönlendirilir
   - Komutlar ve ifadeler değerlendirilir
   - Sonuçlar yorumlanır ve çıktı üretilir

3. Bağımlılık yönetimi:
   - İlk çalıştırmada gerekli paketler indirilir
   - Paketler önbelleğe kaydedilir
   - Sonraki çalıştırmalarda önbellekten yüklenir
   - İnternet bağlantısı gerekmez

### 1.3 Temel Yetenekler

- Türkçe sözdizimi desteği
- Tam OOP (Nesne Yönelimli Programlama) desteği
- İleri düzey modülerlik
- Geniş veri tipi desteği
- Güçlü hata yönetimi
- GUI ve network programlama
- Veritabanı entegrasyonu
- AI/ML özellikleri

## 2. Veri Yapıları ve Değişkenler

### 2.1 Temel Veri Tipleri

```basic
DIM sayi AS INTEGER          ' Tam sayı
DIM ondalik AS FLOAT        ' Ondalıklı sayı
DIM metin AS STRING         ' Metin
DIM mantik AS BOOLEAN       ' Mantıksal
DIM tarih AS DATE          ' Tarih
DIM zaman AS TIME          ' Zaman
DIM tarihSaat AS DATETIME  ' Tarih ve saat
```

### 2.2 Kompleks Veri Yapıları

```basic
' Dizi tanımlama
DIM dizi(10) AS INTEGER

' Liste tanımlama
DIM liste AS LIST
liste.ADD(5)

' Sözlük tanımlama
DIM sozluk AS DICTIONARY
sozluk.PUT("anahtar", "değer")

' Set tanımlama
DIM kume AS SET
kume.ADD(10)

' Yığın ve Kuyruk
DIM yigin AS STACK
DIM kuyruk AS QUEUE
```

### 2.3 Özel Veri Yapıları

```basic
' Yapı (Struct) tanımlama
TYPE Ogrenci
    isim AS STRING
    numara AS INTEGER
END TYPE

' Numaralandırma
ENUM Gunler
    PAZARTESI = 1
    SALI
    CARSAMBA
END ENUM
```

## 3. Yeni Komutlar ve Özellikleri

### 3.1 OOP Komutları

```basic
' Sınıf tanımlama
CLASS Hesap
    PRIVATE bakiye AS FLOAT
    
    PUBLIC SUB yatir(miktar AS FLOAT)
        bakiye = bakiye + miktar
    END SUB
END CLASS

' Soyut sınıf
ABSTRACT CLASS Sekil
    PUBLIC ABSTRACT FUNCTION alan() AS FLOAT
END CLASS

' Arayüz tanımlama
INTERFACE ISurulebilir
    SUB sur()
    SUB dur()
END INTERFACE
```

### 3.2 Modülerlik ve Kütüphane Yönetimi

```basic
' Kütüphane tanımlama
LIBRARY MatematikLib
    PUBLIC FUNCTION topla(a AS INTEGER, b AS INTEGER) AS INTEGER
        RETURN a + b
    END FUNCTION
END LIBRARY

' İsim uzayı kullanımı
NAMESPACE Geometri
    CLASS Ucgen
        ' ... 
    END CLASS
END NAMESPACE

' Modül içe aktarma
IMPORT "matematik.libx" AS mat
USING Geometri
```

### 3.3 Hata Yönetimi

```basic
TRY
    ' Riskli kod
    dosya = OPEN("data.txt", "r")
CATCH IOError AS hata
    PRINT "Dosya açılamadı: "; hata
FINALLY
    CLOSE dosya
END TRY
```

### 3.4 Veritabanı İşlemleri

```basic
' Bağlantı açma
DATABASE CONNECT "mydb.db"

' Sorgu çalıştırma
QUERY "SELECT * FROM users" TO sonuc

' İşlem yönetimi
BEGIN TRANSACTION
    EXECUTE "INSERT INTO users VALUES ('Ali', 25)"
    EXECUTE "UPDATE balance SET amount = amount - 100"
COMMIT
```

### 3.5 Network ve Web

```basic
' HTTP istekleri
HTTP GET "https://api.example.com/data" TO veri
HTTP POST "https://api.example.com/users" DATA kullanici

' Soket programlama
SOCKET CONNECT "localhost", 8080
SOCKET SEND "Merhaba"
```

### 3.6 GUI Programlama

```basic
' Pencere oluşturma
WINDOW ana_pencere "Uygulama"
    BUTTON btn1 "Tıkla"
    TEXTBOX txt1
    
' Olay işleme
ON CLICK btn1 DO
    PRINT txt1.TEXT
END DO
```

### 3.7 Thread ve Process Yönetimi

```basic
' İş parçacığı oluşturma
THREAD worker DO
    ' Arka plan işlemi
END DO

' Kaynak kilitleme
LOCK kaynak
    ' Kritik bölge
UNLOCK kaynak

' Process başlatma
PROCESS "calc.exe"
```

### 3.8 AI ve Makine Öğrenimi

```basic
' Model eğitimi
LEARN FROM "data.csv" AS model

' Tahmin yapma
PREDICT USING model INPUT veri TO sonuc

' Sinir ağı tanımlama
NEURAL NETWORK
    LAYER INPUT 784
    LAYER HIDDEN 128 ACTIVATION "relu"
    LAYER OUTPUT 10 ACTIVATION "softmax"
END NEURAL
```

## 4. İyi Programlama Pratikleri

1. Değişkenleri tanımlarken açıklayıcı isimler kullanın
2. Kodunuzu modüler yapıda organize edin
3. Hata yönetimini ihmal etmeyin
4. Yorum satırları ekleyerek kodunuzu belgeleyin
5. Kaynak kilitleme işlemlerinde FINALLY bloğunu kullanın
6. Büyük projelerde isim uzaylarını etkin kullanın
7. Kritik bölgelerde thread güvenliğini sağlayın

DO WHILE condition
  ' koşul doğru olduğu sürece çalış
LOOP

DO UNTIL condition  
  ' koşul yanlış olduğu sürece çalış
LOOP

DO
  ' en az bir kez çalış
  ' sonra koşulu kontrol et
LOOP WHILE condition

DO 
  ' basit sonsuz döngü
  ' EXIT DO ile çıkılabilir
LOOP

SELECT CASE expression
  CASE value1, value2
    ' değer eşleşme
  CASE IS > value3 
    ' karşılaştırma
  CASE value4..value5
    ' aralık kontrolü  
  CASE ELSE
    ' hiçbiri eşleşmezse
END SELECT

DIM arr(2,3,4) AS ARRAY ' 3 boyutlu dizi
DIM fixed(5,10,15) AS FIXED ARRAY[5,10,15] ' Sabit boyutlu dizi  
DIM dyn() AS DYNAMIC ARRAY ' Dinamik dizi (REDIM ile boyutlandırılır)

Yapılan değişiklikler:

SELECT CASE:
Karmaşık koşul kontrolleri (IS operatörleri, aralık kontrolü)
İç içe SELECT CASE desteği
CASE ELSE desteği
Çoklu değer kontrolü (CASE value1, value2)
DO/LOOP:
DO WHILE ve DO UNTIL varyantları
EXIT DO ve CONTINUE DO desteği
İç içe döngüler
Döngü başında veya sonunda koşul kontrolü
Diziler:
N-boyutlu dizi desteği (sınırsız boyut)
Sabit ve dinamik diziler
BASIC tarzı 0-tabanlı indeksleme
Recursive yardımcı fonksiyonlarla dizi oluşturma
Şimdi yorumlayıcı çok daha güçlü kontrol yapılarına ve veri türlerine sahip. Hepsi Türkçe hata mesajları ile tam entegre şekilde çalışmakta.
