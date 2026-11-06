# Ara Rapor Videosu — Konuşma Metni

**Hedef süre:** 7–8 dakika. Konuşma kısmı yaklaşık 830 kelime; normal hızda 6,5–7 dakika sürer, ekran geçişleri ve canlı kodla 7–8 dakikayı bulur. Rehberde üst sınır 15 dakika, ara rapor için 5–10 dakika yeterli. Köşeli parantezli satırlar **ekrana ne getireceğini** söyler; onları okuma.

**Kayıttan önce:**
- OBS veya benzeri bir programla ekranı kaydet, webcam sağ alt köşede açık olsun (rehber: yüz açılışta ve kod anlatımında görünmeli, ses senin olmalı).
- Açık olsun: `reports/sunum/slides.pdf` (tam ekran), VS Code'da `src/leukemia/data.py` ve `src/leukemia/preprocessing.py`, proje klasöründe bir terminal.
- Terminalde bir kere önceden `python scripts/run_eda.py --only golub` çalıştır; kayıtta yaklaşık 25 saniye sürer ve sen konuşurken biter.
- Metni ezberlemen gerekmiyor, ama kelimesi kelimesine de okuma. Kendi cümlelerinle söylemen hem daha doğal olur hem de konuyu anladığını gösterir.

---

## 1. Açılış — 0:00–0:25

[EKRAN: Slayt 1 — başlık. Webcam büyük ya da tam ekran olabilir.]

> Merhaba, ben Enes Ay, öğrenci numaram 503020260092. Bu video, Makine Öğrenmesi ve Anomali
> Tespiti dersi dönem projemin ara rapor sunumu. Konu, gen ifadesi verisinden iki akut lösemi
> türünü, ALL ve AML'yi ayırmak. Bu aşamada literatürü, veri setlerini ve keşifsel analizi
> anlatacağım; modeller finalde gelecek.

## 2. Problem ve araştırma soruları — 0:25–1:20

[EKRAN: Slayt 2 — Problem ve motivasyon.]

> ALL lenfoid, AML miyeloid kökenli ve tedavileri farklı; bu yüzden doğru ayrım klinik olarak
> önemli. İkisi de kanser olduğu için modüldeki "non-cancer" etiketi yanlış; problemi ALL ve AML
> alt tip sınıflandırması olarak tanımladım. Mikrodizi, binlerce genin mRNA düzeyini tek deneyde
> ölçer. Golub verisinde 72 hasta ve 7.129 prob var; özellik sayısı örnek sayısının yaklaşık yüz
> katı. Asıl zorluk bu: model kolayca ezberler ve yanlış protokolle başarı olduğundan yüksek
> görünür.
>
> Dört sorum var. Sızıntısız iç içe çapraz doğrulamada üç yöntem farklı mı? 38'e 34'lük tek
> bölme bununla tutarlı mı ve sızıntı sonucu ne kadar şişirir? Sinyal başka hasta gruplarına ve
> platformlara taşınıyor mu? Bonus olarak derin öğrenme ve TabPFN klasik yöntemleri geçiyor mu?

## 3. Literatür — 1:20–2:10

[EKRAN: Slayt 3 — Literatür taraması.]

> Literatürü yapay zekâ desteğiyle taradım ve rapordaki iddiaları kaynak metinlerle denetledim;
> bu denetim gerçek hatalar yakaladı. Örneğin Dudoit'nun alt eşiği 20 değil 100'müş. Sonuçta 52
> kaynak var, 31'i 2021 ve sonrasından.
>
> Asıl boşluk şu: son dört Golub çalışması yüzde 97 ile 99,9 arasında doğruluk bildiriyor, ama
> protokoller farklı ve hiçbirinde güven aralığı yok. Bazıları genleri çapraz doğrulamadan önce
> seçiyor görünüyor. Bunun iyimser sonuç verdiği 2002'den beri biliniyor; 2023 tarihli bir tarama
> da sızıntının 17 alanda en az 294 makaleyi etkilediğini bildiriyor. Okuduğumuz Golub
> çalışmalarında model başka bir kohorta da aktarılmıyor.

## 4. Veri setleri — 2:10–2:45

[EKRAN: Slayt 4 — Veri setleri tablosu ve sınıf dağılımı.]

> Üç veri seti kullanıyorum. Golub ana veri seti: 47 ALL, 25 AML; 38 eğitim, 34 test örneği.
> MILE çok merkezli ve büyük: 2.096 örnekten yalnızca ALL ve AML'yi aldım, 1.292 örnek kaldı.
> Aynı klinik soruyu soruyor ve ön eğitim için yeterince büyük. Andersson 121 çocuk hastadan
> oluşuyor ve bilerek zor bir seçim: iki renkli cDNA dizisi, değerler log oran ve yaklaşık yüzde 7
> eksik değer var. Üçünde de sınıflar ALL ağırlıklı.

## 5. Canlı kod — 2:45–3:45

[EKRAN: Terminal, webcam köşede. Komutu yaz ve çalıştır: `python scripts/run_eda.py --only golub`]

> Golub analizini başlatıyorum; sonuçlar üretilirken kodun iki kritik yerini göstereyim.

[EKRAN: VS Code, `src/leukemia/data.py` → `load_golub` fonksiyonu.]

> Birincisi etiket eşleme. CSV'de hasta sütunları sırasız: 1'den 27'ye gidiyor, sonra 34–38,
> sonra 28–33 geliyor. Sütun sırasıyla eşleseydim bazı hastalar yanlış etiket alırdı. Bu yüzden
> hasta numarasıyla birleştiriyorum ve `assert` satırlarıyla sınıf sayılarının 27'ye 11, 20'ye 14
> olduğunu doğruluyorum.

[EKRAN: `src/leukemia/preprocessing.py` → `FoldChangeFilter` sınıfı.]

> İkincisi sızıntı. Bu filtre hangi genleri tutacağına `fit` sırasında, yalnızca eğitim verisine
> bakarak karar veriyor; `transform` sadece bu kararı uyguluyor. Finalde bu adımlar Pipeline içinde
> her eğitim katında yeniden öğrenilecek.

[EKRAN: Terminale dön; betik bitmiş olmalı.]

> Betik sayıları bir JSON dosyasına yazıyor ve rapordaki sayılar buradan makro olarak geliyor.
> Seed 42 sabit, yani her sonuç yeniden üretilebilir.

## 6. Veri kalitesi ve dönüşüm — 3:45–4:30

[EKRAN: Slayt 5 — Veri kalitesi ve dönüşüm.]

> Golub'da eksik veya sonsuz değer yok; yani modüldeki INF doldurma adımı özgün dosyada bir şey
> değiştirmiyor. Ama değerlerin yüzde 28,7'si negatif. Nedeni ölçüm yöntemi: eski Affymetrix
> yazılımı tam eşleşen probun sinyalinden uyumsuz probunkini çıkarıyor, ifade edilmeyen genlerde
> bu fark negatif olabiliyor. Absent çağrıları da bu değerlerle örtüşüyor. Bu yüzden değerleri 20
> ile 16.000 arasına kırpıp log2 aldım. Çarpıklık 7,08'den 0,55'e, ortalama ile standart sapma
> korelasyonu 0,95'ten 0,18'e indi. Böylece birkaç parlak gen SVM ve PCA gibi yöntemlere hâkim
> olmuyor.

## 7. Sinyal ve ayırt edici genler — 4:30–5:10

[EKRAN: Slayt 6 — Sinyal: boyut indirgeme ve ayırt edici genler.]

> İlk bileşen varyansın yalnızca yüzde 11'ini açıklıyor, ama tek başına ALL ve AML'yi 0,984 AUC ile
> ayırıyor. Sinyal bu kadar güçlü olunca yöntem farkları küçük çıkacak; bu yüzden güven aralığı ve
> istatistiksel test şart. Welch t testi ve Benjamini–Hochberg düzeltmesiyle 945 gen anlamlı çıktı.
> Üst genler biyolojiyle uyumlu: CST3, CD33 ve MPO AML'de, CD19, CD79B ve TCF3 ALL'de yüksek. Ama
> bu sıralama tüm veriyle yapıldı, yani yalnızca betimsel; modelde kullanılırsa sızıntı olur.

## 8. Batch etkisi ve kohortlar arası farklar — 5:10–5:50

[EKRAN: Slayt 7 — Batch etkisi ve kohortlar arası farklar.]

> Eğitim ve testi her sınıfın içinde karşılaştırdım ki sınıf oranı sonucu karıştırmasın. ALL'de
> genlerin yüzde 17,7'si farklı çıktı; beklenen yüzde 5. Yani 34 örneklik tek bir test skoru çapraz
> doğrulamadan sapabilir. Kohortlar arasında ise biyoloji taşınıyor: gen istatistikleri Golub ile
> MILE arasında 0,56 korele ve ilk 100 genin 33'ü ortak. Ama ölçek taşınmıyor: birleşik PCA'da ilk
> bileşenin yüzde 99,8'ini veri setinin kimliği açıklıyor. Kohort içinde standartlaştırınca sınıf
> ekseni ortaya çıkıyor.

## 9. Fizibilite pilotu — 5:50–6:45

[EKRAN: Slayt 8 — Fizibilite pilotu.]

> Finaldeki ölçümlerin mümkün olduğunu görmek için sabit ayarlı küçük bir pilot yapıldı; bu bir
> model karşılaştırması değil. Etiketleri rastgele karıştırdığımızda, genler çapraz doğrulamadan
> önce seçilirse dengeli doğruluk 0,91; doğru protokolde 0,50, yani şans düzeyi. Aktarımda ise
> altı yönün dördünde AUC 0,965 ile 0,992 arasındayken dengeli doğruluk 0,50: model hastaları iyi
> sıralıyor, ama karar eşiği tutmuyor.
>
> Bu desen 2026'da sepsiste bildirildi, yani yeni değil. Bizim özgün sorumuz, orada eşiği kurtaran
> sıra dönüşümünün burada neden kurtarmadığı ve eşik kaymasının platformdan mı sınıf oranından mı
> geldiği. Bunlar ön bulgu. Golub'un 34 test örneği hiçbir modele girmedi; MILE'ın ikinci aşaması ve
> TARGET RNA-seq verisiyle birlikte finale kadar kilitli.

## 10. Final planı ve kapanış — 6:45–7:30

[EKRAN: Slayt 9 — Bulgulardan final planına.]

> Finalde elastic-net lojistik regresyon, SVM ve random forest'ı karşılaştıracağım. 38'e 34'lük
> bölmede test bir kez kullanılacak; 72 örnekte beş seed ile 5×5 iç içe çapraz doğrulama yapılacak.
> Öznitelik seçimi her eğitim katının içinde olacak, sonuçlar güven aralığı ve düzeltilmiş t testiyle
> karşılaştırılacak. Bonus olarak derin öğrenme, TabPFN, üçüncü veri seti ve hocamın onayıyla
> uluslararası bir IEEE konferansına İngilizce makale planlıyorum; aday konferans IEEE EMBC 2027.

[EKRAN: Slayt 10 — Teşekkürler. Webcam büyütülebilir.]

> Kod GitHub'da ve tek komutla yeniden üretilebiliyor. Kod, literatür okuması ve metin için
> Anthropic'in Claude modelini kullandım; ayrıntılar GenAI beyanında. Dinlediğiniz için teşekkür
> ederim.

---

### Olası sorular için kısa notlar (videoda okumana gerek yok)

- **Neden negatif değer var?** MAS4 average difference = PM − MM ortalaması; MM > PM ise negatif.
- **P/A/M nedir?** Present/Marginal/Absent tespit çağrısı; probun gerçekten ifade edilip edilmediğinin istatistiksel kararı.
- **Neden iç içe CV?** Hiperparametre ve gen seçimi aynı katlarda hem ayarlanıp hem değerlendirilirse skor iyimser olur (Varma & Simon 2006).
- **Welch t-testi neden?** Sınıf varyansları eşit varsayılmıyor; Mann–Whitney ise dağılım varsayımı yapmıyor.
- **ARI nedir?** Kümeleme ile gerçek sınıfların uyumu; 1 tam uyum, 0 rastgele.
- **Neden taban 20, Dudoit'nun 100'ü değil?** 20 rehberden; taban 100 ile aynı süzgeç Dudoit'nun 3.571 genini birebir veriyor, 20 ile 3.859.
- **KS testi neyi gösteriyor?** Bir genin eğitim ve testteki dağılımlarının aynı olup olmadığını; kayma yoksa p-değerleri düzgün dağılır.
- **Ham aktarımda model neden tek sınıfa yığılıyor?** Eğitim kohortunun ölçeği hedef kohorta uymuyor; skorlar eşiğin hep aynı tarafına düşüyor, ama aralarındaki sıra korunabiliyor. Bu yüzden AUC yüksek, dengeli doğruluk 0,50 olabiliyor.
- **Hedef kohortun z-skoru neden sabit aktarım sayılmıyor?** Hedef kohortun ortalaması ve standart sapması kullanılıyor; tek hastaya uygulanamaz ve sınıf oranına bağlıdır.
- **Sepsis çalışmasından farkınız ne?** Görev ALL/AML; orada eşiği kurtaran örnek içi sıra dönüşümü bizim pilotta kurtarmıyor; eşik kaymasını sınıf oranından ayırmayı hedefliyoruz. Pilot sonuçları ön bulgudur.

