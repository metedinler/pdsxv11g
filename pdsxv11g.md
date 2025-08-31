# pdsXv11 Yorumlayıcısı
PDS-X BASIC, 1990 larda kullanimi biten QuickBasic 7.1 in gunumuzde var olsaydi ne olurdu,kolayca yazilan programlar ve daha degisik progralama mantalielerini ile yeni duzunce tarzlarini programlamaya yeni baslayan veya hizlica prototipleme yapmak isteyenlere yonelik guclu ve esnek bir dildir.

Bir cok versiyonu vardir. V11g mantiksal programlama olmayan nesne yonelimli ve fonksiyonel, yapisal bir programlama dilidir. Boru hatlari, olay yonetimi, sonraki versiyonlarda daha gelismis olarak yazilmistir. bu versiyonda olay yonetimi temel, temel ustu olarak sistemde denenmistir. boru hatti programlamasina girilmemistir.

PDS-X Basic yinede oldukca guclu bir dildir. Moduler tasarimlara izin verir. Dusuk seviye programcilik icin daha sonraki versiyonlarda ileri seviye modulleri ve eklemeleri vardir. Ancak kullanim icin simdilik bunlar interpretere eklenmemis, kafa karisikligi yaratilmamistir.

pdsXv11, Python ile geliştirilmiş, modern ve genişletilebilir bir programlama dili yorumlayıcısıdır. Klasik BASIC lehçelerinin basitliğini ve okunabilirliğini temel alırken, günümüz programlama dünyasının ihtiyaçlarına cevap veren güçlü ve esnek yeteneklerle donatılmıştır. Bu proje, sadece temel programlama yapılarını (değişkenler, döngüler, koşullar) desteklemekle kalmaz, aynı zamanda nesne yönelimli programlama (OOP), modülerlik, gelişmiş veri yapıları (listeler, sözlükler, veri çerçeveleri), alt seviye hafıza yönetimi ve hatta doğrudan internet ve API erişimi gibi karmaşık özellikleri de bünyesinde barındırır.Ayrica hafif fonksiyonel programlama komulari icerir, pdsXv11, hem bir betik dosyasını baştan sona çalıştırabilen bir motor hem de kullanıcıların komutları anlık olarak test edip sonuçlarını görebileceği etkileşimli bir REPL (Read-Eval-Print Loop) ortamı sunarak öğrenme, prototipleme ve uygulama geliştirme süreçlerini kolaylaştırmayı hedefler.

Projenin mimarisi, ana yorumlayıcı çekirdeği (`pdsXv11` sınıfı) ve dile gömülü standart fonksiyonları içeren `LibXCore` kütüphanesi olmak üzere iki ana bileşen üzerine kuruludur. Bu modüler yapı, dilin çekirdek mantığını temiz tutarken yeni fonksiyonlar ve yetenekler eklemeyi basitleştirir. Yorumlayıcı, `requests` ile HTTP istekleri yapmaktan `pdfplumber` ile PDF dosyalarını işlemeye, `pandas` ve `numpy` ile veri analizinden `ctypes` ile harici DLL (Dinamik Bağlantı Kütüphanesi) dosyalarını kullanmaya kadar geniş bir yelpazede işlevsellik sunar. Hata yönetimi için `TRY...CATCH` ve `ON ERROR GOTO` gibi mekanizmalar, kodun daha sağlam ve güvenilir olmasını sağlar. pdsXv11, bu özellikleriyle hem eğitim amaçlı basit betikler yazmak hem de daha karmaşık, veri odaklı ve ağ bağlantılı uygulamalar geliştirmek için güçlü bir platform oluşturur.

# Kullanım

pdsXv11 yorumlayıcısı iki ana modda çalıştırılabilir:

1.  **Dosya Modu:** Önceden yazılmış bir `.basx` veya benzeri uzantılı bir betik dosyasını çalıştırmak için kullanılır.
    ```shell
    python pdsXv11g.py programim.basx
    ```

2.  **Etkileşimli Mod (REPL):** Komutları doğrudan terminale yazarak anında sonuç almak için kullanılır.
    ```shell
    python pdsXv11g.py
    ```
    Veya `-i` bayrağı ile:
    ```shell
    python pdsXv11g.py -i
    ```

---

# Komut Referansı

## Ana Komutlar

- `PRINT`: Belirtilen ifadelerin değerlerini konsol ekranına yazdırır.
- `INPUT "mesaj", degisken`: Kullanıcıya bir mesaj gösterir ve girilen veriyi bir değişkene atar.
- `LET degisken = deger`: Bir değişkene bir ifadenin sonucunu atar.
- `DIM degisken AS TIP`: Bir veya daha fazla değişkeni belirli bir veri tipiyle bildirir ve bellekte yer ayırır.
- `IF kosul THEN komut`: Bir koşulun doğru olup olmadığını kontrol eder ve doğruysa belirtilen komutu çalıştırır.
- `SELECT CASE ifade` ... `END SELECT`: Çoklu koşullu yapı. Tüm veri tiplerini (string, integer, float, boolean) destekler. `CASE IS >`, `CASE IS <`, `CASE 1,2,3`, `CASE 1 TO 10`, `CASE ELSE` gibi gelişmiş koşulları kullanabilir.
- `FOR i = baslangic TO bitis STEP artis` ... `NEXT`: Bir kod bloğunu belirli bir aralıkta ve adımla tekrar tekrar çalıştırır.
- `WHILE kosul` ... `WEND`: Belirtilen koşul doğru olduğu sürece bir kod bloğunu tekrar eder.
- `DO` ... `LOOP [WHILE|UNTIL kosul]`: Bir kod bloğunu, döngünün başında veya sonunda bir koşul sağlanana kadar veya sağlandığı sürece tekrar eder.
- `GOTO etiket`: Programın çalışmasını belirtilen bir etikete (LABEL) koşulsuz olarak yönlendirir.
- `GOSUB etiket` ... `RETURN`: Program akışını bir alt programa yönlendirir ve `RETURN` komutuyla geri döner.
- `FUNCTION isim(parametreler)` ... `END FUNCTION`: Belirli bir işi yapan ve bir değer döndüren bir kod bloğu tanımlar.
- `SUB isim(parametreler)` ... `END SUB`: Belirli bir işi yapan ancak bir değer döndürmeyen bir kod bloğu (alt program) tanımlar.
- `CLASS isim [EXTENDS ana_sinif]` ... `END CLASS`: Nesne Yönelimli Programlama için özellikler ve metotlar içeren bir sınıf şablonu oluşturur.
- `IMPORT "dosyaadi" [AS takma_ad]`: Harici bir kod kütüphanesini veya modülünü mevcut programa dahil ederek fonksiyonlarını ve sınıflarını kullanılabilir hale getirir.
- `ON ERROR GOTO etiket`: Çalışma zamanı hatası oluştuğunda program kontrolünü belirtilen bir hata işleme rutinini başlatır.
- `TRY ... CATCH ... DO`: Hata oluşturabilecek kodları bir blok içine alır ve hata oluşması durumunda alternatif bir kod bloğunun çalıştırılmasını sağlar.
- `DEBUG ON|OFF`: Programın adım adım çalıştırılması ve değişkenlerin izlenmesi için hata ayıklama modunu etkinleştirir veya devre dışı bırakır.
- `TRACE ON|OFF`: Program çalışırken her bir komut satırının yürütülmeden önce ekrana yazdırılmasını sağlayarak program akışının izlenmesini kolaylaştırır.
- `KEY()`: Klavyede herhangi bir tuşa basılıp basılmadığını kontrol eder. Basılmışsa TRUE, basılmamışsa FALSE döndürür.
- `GETKEY()`: Klavyeden basılan tuşu bekler ve tuşun karakterini döndürür. Blokant bir fonksiyondur.
- `REPL`: Programın çalışması sırasında etkileşimli REPL moduna geçer. Değişkenleri incelemek ve test komutları çalıştırmak için kullanılır.
- `SAVE "dosyaadi"`: Mevcut program kodunu belirtilen dosya adıyla kaydeder.
- `LOAD "dosyaadi"`: Belirtilen dosyadan program kodunu yükler ve hafızaya alır.
- `RUN [dosyaadi]`: Hafızadaki programı çalıştırır. Dosya adı belirtilirse o dosyayı yükleyip çalıştırır.
- `HELP [komut]`: Belirtilen komut veya tüm komutlar hakkında yardım ve kullanım bilgilerini gösterir.
- `EXIT`: Yorumlayıcının etkileşimli REPL ortamını sonlandırır.

## REPL Ortamı Komutları

- `SAVE "program_adi"`: Etkileşimli modda yazılan programı belirtilen isimle bir `.basx` dosyasına kaydeder.
- `LOAD "program_adi"`: Belirtilen isimdeki `.basx` dosyasını belleğe yükler.
- `LIST`: Bellekteki mevcut programın kod satırlarını ekranda gösterir.
- `DELETE "program_adi"`: Belirtilen isimdeki `.basx` program dosyasını diskten siler.
- `CLS`: Konsol ekranını temizler.
- `RUN`: Bellekteki programı baştan sona çalıştırır.
- `REPL END`: Etkileşimli modda çok satırlı komut veya program girişini tamamlamak için kullanılır.

## İnternet ve API Komutları

- `CALL API::GET "url", [params_json]`: Belirtilen URL'ye bir HTTP GET isteği gönderir ve sunucudan gelen yanıtı döndürür.
- `CALL API::POST "url", [data_json]`: Belirtilen URL'ye, genellikle bir JSON verisi ile birlikte, bir HTTP POST isteği gönderir.
- `CALL API::PUT "url", [data_json]`: Belirtilen URL'deki bir kaynağı güncellemek için bir HTTP PUT isteği gönderir.
- `CALL API::DELETE "url"`: Belirtilen URL'deki bir kaynağı silmek için bir HTTP DELETE isteği gönderir.
- `HTTP_DOWNLOAD "url", "kayit_yolu"`: Bir URL'den dosya indirir ve belirtilen yola kaydeder.
- `HTTP_STATUS "url"`: Bir URL'ye yapılan isteğin HTTP durum kodunu (örn: 200, 404) döndürür.
- `HTTP_SET_HEADER "anahtar", "deger"`: Sonraki API çağrıları için özel bir HTTP başlığı (header) ayarlar.
- `HTTP_SESSION_START` / `HTTP_SESSION_END`: Birden çok istekte aynı ayarları (cookie, header) koruyan bir oturum başlatır veya sonlandırır.
- `WEB_GET(url)`: Bir web sayfasının ham HTML içeriğini bir metin olarak alır.

## Diğer Gelişmiş Komutlar

- `CALL dll_adi::fonksiyon(parametreler)`: Harici bir Dinamik Bağlantı Kütüphanesindeki (DLL) bir fonksiyonu belirtilen parametrelerle çağırır.
- `PDF_READ_TEXT(dosya_yolu)`: Belirtilen PDF dosyasının içindeki metinleri okur ve birleştirerek döndürür.
- `PDF_EXTRACT_TABLES(dosya_yolu)`: Belirtilen PDF dosyasının içindeki tabloları ayıklar ve bir liste olarak döndürür.
- `CORE.fonksiyon_adi(...)`: Dile gömülü olan çekirdek kütüphanedeki (`LibXCore`) bir fonksiyonu doğrudan çağırır.

---

# Fonksiyon Referansı

## String Fonksiyonları

- `MID$(str, baslangic, uzunluk)`: Bir metnin belirtilen pozisyonundan itibaren belirli bir uzunluktaki alt metni alır.
- `LEFT$(str, n)`: Bir metnin solundan belirtilen sayıda karakteri alır.
- `RIGHT$(str, n)`: Bir metnin sağından belirtilen sayıda karakteri alır.
- `LEN(nesne)`: Bir metnin, listenin veya dizinin uzunluğunu (eleman sayısını) döndürür.
- `UCASE$(str)`: Bir metnin tüm harflerini büyük harfe çevirir.
- `LCASE$(str)`: Bir metnin tüm harflerini küçük harfe çevirir.
- `LTRIM$(str)`: Bir metnin solundaki boşlukları temizler.
- `RTRIM$(str)`: Bir metnin sağındaki boşlukları temizler.
- `STRING$(n, karakter)`: Belirtilen karakteri n defa tekrarlayarak bir metin oluşturur.
- `SPACE$(n)`: Belirtilen sayıda boşluk karakteri içeren bir metin oluşturur.
- `INSTR(baslangic, str, alt_str)`: Bir metin içinde başka bir metnin başlangıç pozisyonunu arar.
- `STR$(sayi)`: Sayısal bir değeri metin (string) formatına dönüştürür.
- `VAL(str)`: Metin formatındaki bir sayıyı sayısal bir değere dönüştürür.
- `CHR$(kod)`: ASCII koduna karşılık gelen karakteri döndürür.
- `ASC(karakter)`: Bir karakterin ASCII kodunu döndürür.

## Matematiksel Fonksiyonlar

- `ABS(x)`: Bir sayının mutlak değerini döndürür.
- `INT(x)`: Bir ondalık sayının tam sayı kısmını alır.
- `SQR(x)`: Bir sayının karekökünü hesaplar.
- `RND()`: 0 ile 1 arasında rastgele bir ondalık sayı üretir.
- `SIN(x)`, `COS(x)`, `TAN(x)`: Radyan cinsinden bir açının sinüs, kosinüs veya tanjantını hesaplar.
- `LOG(x)`, `EXP(x)`: Bir sayının doğal logaritmasını veya e'nin belirtilen üssünü hesaplar.
- `ATN(x)`: Bir sayının arktanjantını radyan olarak döndürür.
- `FIX(x)`: Bir sayının ondalık kısmını atarak tam sayıya dönüştürür (negatif sayılarda farklı çalışabilir).
- `ROUND(x, n)`: Bir sayıyı belirtilen ondalık basamak sayısına göre yuvarlar.
- `SGN(x)`: Bir sayının işaretini döndürür (-1, 0 veya 1).
- `MOD(x, y)`: Bir sayının diğerine bölümünden kalanı verir.
- `MIN(...)`, `MAX(...)`: Verilen sayılar listesindeki en küçük veya en büyük değeri bulur.
- `PI`, `E`: Pi (π) ve Euler (e) sabitlerini döndürür.
- `BIN(x)`, `HEX(x)`, `OCT(x)`: Bir sayıyı ikilik, onaltılık veya sekizlik tabanda metin olarak gösterir.

## Veri Analizi ve İstatistik (Numpy/Pandas/Scipy)

- `MEAN(liste)`, `MEDIAN(liste)`, `MODE(liste)`: Bir veri setinin ortalamasını, medyanını veya modunu hesaplar.
- `STD(liste)`, `VAR(liste)`, `SUM(liste)`, `PROD(liste)`: Bir veri setinin standart sapmasını, varyansını, toplamını veya elemanlarının çarpımını hesaplar.
- `PERCENTILE(liste, q)`, `QUANTILE(liste, q)`: Bir veri setinin belirtilen yüzdelik veya kantil değerini bulur.
- `CORR(x, y)`, `COV(x, y)`: İki veri seti arasındaki korelasyon veya kovaryansı hesaplar.
- `DESCRIBE(dataframe)`: Bir veri çerçevesinin (DataFrame) temel istatistiksel özetini oluşturur.
- `GROUPBY(dataframe, sutun)`: Bir veri çerçevesini belirtilen sütuna göre gruplar.
- `FILTER(dataframe, kosul_str)`: Bir veri çerçevesindeki verileri belirtilen koşula göre filtreler.
- `SORT(dataframe, sutun)`: Bir veri çerçevesini belirtilen sütuna göre sıralar.
- `HEAD(dataframe, n)`, `TAIL(dataframe, n)`: Bir veri çerçevesinin ilk veya son n satırını gösterir.
- `MERGE(df1, df2, on=...)`: İki veri çerçevesini belirtilen sütunlara göre birleştirir.
- `TTEST(ornek1, ornek2)`, `CHISQUARE(gozlenen)`, `ANOVA(...)`: İstatistiksel testler (T-testi, Ki-kare, ANOVA) uygular.
- `REGRESS(x, y)`: İki değişken arasında doğrusal regresyon analizi yapar.
- `LINSPACE(...)`, `ARANGE(...)`, `ZEROS(...)`, `ONES(...)`: Belirli aralıklarda veya boyutlarda sayısal diziler (array) oluşturur.
- `RESHAPE(...)`, `TRANSPOSE(...)`: Bir dizinin şeklini değiştirir veya transpozunu alır.
- `PIVOT_TABLE(...)`, `CROSSTAB(...)`: Özet tablolar veya çapraz tablolar oluşturur.
- `FILLNA(...)`, `DROPNA(...)`: Eksik verileri doldurur veya eksik veri içeren satırları kaldırır.

## Dosya ve Sistem Fonksiyonları

- `DIR$(yol)`: Belirtilen dizindeki dosya ve klasörleri listeler.
- `ISDIR(yol)`: Belirtilen yolun bir dizin olup olmadığını kontrol eder.
- `EOF(dosya_no)`: Bir dosyanın sonuna ulaşılıp ulaşılmadığını kontrol eder.
- `LOC(dosya_no)`: Bir dosyada okuma/yazma imlecinin mevcut konumunu döndürür.
- `LOF(dosya_no)`: Bir dosyanın toplam boyutunu byte olarak döndürür.
- `FREEFILE()`: Kullanılmayan bir dosya tanıtıcı numarası bulur.
- `INPUT$(n, dosya_no)`: Bir dosyadan belirtilen sayıda karakter okur.
- `ENVIRON$(degisken)`: Bir ortam değişkeninin değerini döndürür.
- `COMMAND$()`: Programı çalıştıran komut satırı argümanlarını döndürür.

## Zaman ve Tarih Fonksiyonları

- `TIMER()`: Programın başlangıcından bu yana geçen süreyi saniye olarak döndürür.
- `DATE$()`: Mevcut sistem tarihini "AA-GG-YYYY" formatında döndürür.
- `TIME$()`: Mevcut sistem saatini "SS:DD:SS" formatında döndürür.

## Hafıza ve İş Parçacığı Fonksiyonları

- `ADDR(degisken)`: Bir değişkenin bellekteki adresini döndürür.
- `SIZEOF(degisken)`: Bir değişkenin bellekte kapladığı alanı byte olarak döndürür.
- `NEW(boyut)`, `DELETE(adres)`: Belirtilen boyutta yeni bir bellek alanı ayırır veya ayrılmış bir alanı serbest bırakır.
- `THREAD_COUNT()`: Aktif olarak çalışan iş parçacığı (thread) sayısını döndürür.
- `CURRENT_THREAD()`: Mevcut iş parçacığının kimliğini (ID) döndürür.
- `ASYNC_WAIT(saniye)`: Programın çalışmasını belirtilen saniye kadar eşzamansız olarak bekletir.

## Diğer Fonksiyonlar

- `MAP(fonksiyon, liste)`: Bir listedeki her elemana belirtilen fonksiyonu uygular ve sonuçlardan yeni bir liste oluşturur.
- `WHERE(fonksiyon, liste)`: Bir listedeki elemanları belirtilen fonksiyona göre filtreler ve koşulu sağlayanlardan yeni bir liste oluşturur.
- `REDUCE(fonksiyon, liste, baslangic)`: Bir listedeki elemanları belirtilen fonksiyonu kullanarak tek bir değere indirger.

---

# Operatör Referansı

## Aritmetik ve Atama

- `+`, `-`, `*`, `/`, `^` (üs alma)
- `+=`, `-=`, `*=`, `/=`

## Mantıksal ve Karşılaştırma

- `=`, `<>`, `<`, `>`, `<=`, `>=`
- `AND`, `OR`, `XOR`, `NOT`

## Bit Düzeyinde (Bitwise)

- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT)
- `<<` (sola kaydır), `>>` (sağa kaydır)
- `&=`, `|=`, `^=`, `<<=`, `>>=`

## Diğer

- `++` (bir artır), `--` (bir azalt)

---

# Klavye Girişi

## KEY() - Non-blocking Tuş Kontrolü

`KEY()` fonksiyonu, klavyede herhangi bir tuşa basılıp basılmadığını kontrol eder ve programa akışını engellemez (non-blocking). Program çalışmasını durdurmadan tuş girişi olup olmadığını anlık olarak sorgular.

```basic
' Klavye kontrolü örneği
WHILE TRUE
  IF KEY() THEN
    pressed_key = GETKEY()
    PRINT "Basılan tuş: ", pressed_key
    IF pressed_key = "q" THEN EXIT
  END IF
  PRINT "Program çalışıyor..."
  SLEEP 1
WEND
```

## GETKEY() - Tuş Bekle

`GETKEY()` fonksiyonu, kullanıcıdan bir tuşa basmasını bekler (blocking) ve basılan tuşun karakterini döndürür. Program bu komutta durur ve tuş girişini bekler.

```basic
PRINT "Herhangi bir tuşa basın..."
key = GETKEY()
PRINT "Basılan tuş: ", key

IF key = "y" THEN
  PRINT "Evet seçildi"
ELSE
  PRINT "Hayır seçildi"
END IF
```

---

# Program Yönetimi Komutları

## REPL - Etkileşimli Mod

`REPL` komutu, program çalışması sırasında etkileşimli moda geçer. Bu modda değişkenleri inceleyebilir, test komutları çalıştırabilir ve hata ayıklama yapabilirsiniz.

```basic
x = 10
y = 20
PRINT "Değişkenler ayarlandı"

REPL  ' Etkileşimli moda geç

' REPL'te çalıştırılabilir:
' PRINT x + y
' VAR
' x = x * 2
' EXIT
```

## SAVE - Program Kaydetme

`SAVE "dosyaadi"` komutu, mevcut program kodunu belirtilen dosya adıyla kaydeder.

```basic
' Program içinde kendini kaydetme
SAVE "backup_program.pdsx"
PRINT "Program kaydedildi"
```

---

# SELECT CASE - Gelişmiş Koşullu Kontrol

pdsXv11g'de SELECT CASE komutları, tüm veri tiplerini destekleyen güçlü bir koşullu yapıdır. Diğer BASIC lehçelerinden farklı olarak, sadece sayılarla değil, string, boolean, float ve karmaşık ifadelerle de çalışabilir.

## Temel Özellikler

- **Tüm veri tipleri**: string, integer, float, boolean destekler
- **Karşılaştırma operatörleri**: `CASE IS >`, `CASE IS <`, `CASE IS >=`, `CASE IS <=`, `CASE IS <>` 
- **Çoklu değerler**: `CASE 1, 2, 3` veya `CASE "start", "begin", "go"`
- **Aralık desteği**: `CASE 1 TO 10` (sayılar için)
- **Hesaplanmış ifadeler**: Fonksiyon sonuçları ve matematik işlemleri
- **İç içe yapılar**: SELECT CASE blokları içinde başka SELECT CASE'ler

## Syntax

```basic
SELECT CASE ifade
    CASE deger1, deger2, deger3
        ' Kodlar
    CASE IS > deger
        ' Kodlar  
    CASE aralık_başı TO aralık_son
        ' Kodlar
    CASE ELSE
        ' Varsayılan kodlar
END SELECT
```

## Örnekler

### String Kontrolü
```basic
DIM komut AS STRING
komut = "HELP"

SELECT CASE UCASE$(komut)
    CASE "START", "BEGIN", "GO"
        PRINT "Program başlıyor..."
    CASE "HELP", "H", "?"
        PRINT "Yardım menüsü"  
    CASE "QUIT", "EXIT", "Q"
        PRINT "Program sonlanıyor..."
    CASE ELSE
        PRINT "Bilinmeyen komut:", komut
END SELECT
```

### Sayısal Karşılaştırma
```basic
DIM puan AS INTEGER
puan = 85

SELECT CASE puan
    CASE IS >= 90
        PRINT "A - Mükemmel!"
    CASE IS >= 80
        PRINT "B - Çok İyi!"
    CASE IS >= 70
        PRINT "C - İyi"
    CASE IS >= 60
        PRINT "D - Geçer"
    CASE ELSE
        PRINT "F - Kaldı"
END SELECT
```

### Boolean ve Karma Kontrol
```basic
DIM kullanıcı_aktif AS BOOLEAN
DIM yetki_seviyesi AS INTEGER
kullanıcı_aktif = TRUE
yetki_seviyesi = 3

SELECT CASE kullanıcı_aktif
    CASE TRUE
        SELECT CASE yetki_seviyesi
            CASE 1, 2
                PRINT "Temel kullanıcı"
            CASE 3, 4
                PRINT "Orta seviye kullanıcı"
            CASE IS >= 5
                PRINT "Yönetici seviyesi"
        END SELECT
    CASE FALSE
        PRINT "Kullanıcı aktif değil"
END SELECT
```

### Dosya Uzantısı Kontrolü
```basic
DIM dosya_adı AS STRING
dosya_adı = "belge.pdf"

SELECT CASE UCASE$(RIGHT$(dosya_adı, 4))
    CASE ".TXT", ".DOC"
        PRINT "Metin belgesi"
    CASE ".PDF"
        PRINT "PDF belgesi"
    CASE ".JPG", ".PNG", ".GIF"
        PRINT "Resim dosyası"
    CASE ".MP3", ".WAV", ".OGG"
        PRINT "Ses dosyası"
    CASE ELSE
        PRINT "Bilinmeyen dosya türü"
END SELECT
```

Bu gelişmiş SELECT CASE desteği, pdsXv11g'yi diğer BASIC lehçelerinden ayıran önemli özelliklerden biridir.

---

## LOAD - Program Yükleme

`LOAD "dosyaadi"` komutu, belirtilen dosyadan program kodunu yükler ve hafızaya alır.

```basic
' Başka bir programı yükle
LOAD "utils.pdsx"
PRINT "Yardımcı program yüklendi"
```

## RUN - Program Çalıştırma

`RUN` komutu hafızadaki programı çalıştırır. Dosya adı belirtilirse o dosyayı yükleyip çalıştırır.

```basic
' Hafızadaki programı çalıştır
RUN

' Belirli bir dosyayı çalıştır
RUN "game.pdsx"
```

---

# Örnek Uygulamalar

## Basit Oyun Kontrolü

```basic
' Klavye kontrolü ile basit oyun
x = 40
y = 12
running = TRUE

WHILE running
  CLS
  ' Oyuncu pozisyonunu göster
  LOCATE y, x: PRINT "@"
  
  ' Klavye girişini kontrol et (non-blocking)
  IF KEY() THEN
    key = GETKEY()
    SELECT CASE key
      CASE "w", "W": IF y > 1 THEN y = y - 1
      CASE "s", "S": IF y < 24 THEN y = y + 1
      CASE "a", "A": IF x > 1 THEN x = x - 1
      CASE "d", "D": IF x < 79 THEN x = x + 1
      CASE "q", "Q", "ESC": running = FALSE
      CASE "p", "P": 
        PRINT "Oyun duraklatıldı. Devam için bir tuşa basın..."
        GETKEY()
    END SELECT
  END IF
  
  SLEEP 50  ' 50ms bekle
WEND

PRINT "Oyun bitti!"
```

## Gelişmiş SELECT CASE Örnekleri

### Farklı Veri Tipleri ile SELECT CASE

```basic
' String kontrolü
DIM user_command AS STRING
user_command = "START"

SELECT CASE UCASE$(user_command)
    CASE "START", "BEGIN", "GO"
        PRINT "Program başlatılıyor..."
    CASE "STOP", "END", "QUIT", "EXIT"
        PRINT "Program sonlandırılıyor..."
    CASE "HELP", "H", "?"
        PRINT "Yardım menüsü gösteriliyor..."
    CASE ELSE
        PRINT "Bilinmeyen komut:", user_command
END SELECT

' Sayısal aralık kontrolü
DIM score AS DOUBLE
score = 85.5

SELECT CASE score
    CASE IS >= 90
        PRINT "Mükemmel! Harf notu: A"
    CASE IS >= 80
        PRINT "Çok iyi! Harf notu: B"
    CASE IS >= 70
        PRINT "İyi! Harf notu: C"
    CASE IS >= 60
        PRINT "Geçer! Harf notu: D"
    CASE ELSE
        PRINT "Kaldınız! Harf notu: F"
END SELECT

' Boolean ve karma kontrol
DIM is_admin AS BOOLEAN
DIM user_level AS INTEGER
is_admin = TRUE
user_level = 5

SELECT CASE is_admin
    CASE TRUE
        SELECT CASE user_level
            CASE 1 TO 3
                PRINT "Düşük seviye yönetici"
            CASE 4 TO 7
                PRINT "Orta seviye yönetici"
            CASE IS >= 8
                PRINT "Üst düzey yönetici"
        END SELECT
    CASE FALSE
        PRINT "Normal kullanıcı - Erişim kısıtlı"
END SELECT

' Hesaplanmış değerler
DIM day AS INTEGER
DIM month AS INTEGER
day = 15
month = 12

SELECT CASE month * 100 + day
    CASE 1225  ' 25 Aralık
        PRINT "Noel günü!"
    CASE 101   ' 1 Ocak
        PRINT "Yılbaşı!"
    CASE 1414 TO 1420  ' 14-20 Şubat arası
        PRINT "Sevgililer haftası"
    CASE IS >= 1200 AND IS <= 1231
        PRINT "Aralık ayında"
    CASE ELSE
        PRINT "Normal gün:", day, "/", month
END SELECT
```

### Fonksiyon Sonuçları ile SELECT CASE
```basic
DIM filename AS STRING
filename = "document.pdf"

SELECT CASE UCASE$(RIGHT$(filename, 4))
    CASE ".TXT", ".DOC"
        PRINT "Metin dosyası"
    CASE ".PDF"
        PRINT "PDF belgesi"
    CASE ".JPG", ".PNG", ".GIF"
        PRINT "Resim dosyası"
    CASE ".MP3", ".WAV"
        PRINT "Ses dosyası"
    CASE ELSE
        PRINT "Bilinmeyen dosya türü"
END SELECT

' String uzunluğu kontrolü
DIM password AS STRING
password = "mySecretPass123"

SELECT CASE LEN(password)
    CASE IS < 8
        PRINT "Şifre çok kısa!"
    CASE 8 TO 12
        PRINT "İyi şifre uzunluğu"
    CASE 13 TO 20
        PRINT "Çok güvenli şifre"
    CASE IS > 20
        PRINT "Şifre çok uzun olabilir"
END SELECT
```

## Program Yönetimi Örneği

```basic
' Ana program
PRINT "Ana program başladı"

' Kullanıcıdan seçim al
PRINT "1. Oyun çalıştır"
PRINT "2. Hesap makinesi çalıştır"
PRINT "3. Çıkış"
PRINT "Seçiminiz: ";
choice = GETKEY()

SELECT CASE choice
  CASE "1"
    RUN "game.pdsx"
  CASE "2"
    RUN "calculator.pdsx"
  CASE "3"
    PRINT "Çıkılıyor..."
    EXIT
END SELECT
```
