# Ara Rapor Videosu — Konuşma Metni

**Hedef süre:** yaklaşık 10 dakika. Konuşma kısmı ~1.300 kelime; Türkçe normal hızda (dakikada
~120–130 kelime) okununca bölüm süreleri aşağıdaki gibi çıkar. Rehberde üst sınır 15 dk,
ara rapor için 5–10 dk yeterli sayılıyor. 10 dakikayı geçersen **[KISALTILABİLİR]**
işaretli paragrafları atla. Köşeli parantezli satırlar **ekrana ne getireceğini** söyler;
onları okuma.

**Kayıttan önce:**
- OBS veya benzeri bir programla ekranı kaydet, webcam sağ alt köşede açık olsun
  (rehber: yüz açılışta ve kod anlatımında görünmeli, ses senin olmalı).
- Açık olsun: `reports/sunum/slides.pdf` (tam ekran), VS Code'da `src/leukemia/data.py`
  ve `src/leukemia/preprocessing.py`, proje klasöründe bir terminal.
- Terminalde bir kere önceden `python scripts/run_eda.py --only golub` çalıştır ki
  Python önbelleği ısınsın; kayıtta ~25 saniye sürer.
- Metni ezberlemen gerekmiyor ama kelimesi kelimesine okuma; kendi cümlelerinle
  söylemen hem daha doğal olur hem de "anladığını gösterme" şartına uyar.

---

## 1. Açılış — 0:00–0:40

[EKRAN: Slayt 1 — başlık. Webcam büyük ya da tam ekran olabilir.]

> Merhaba, ben Enes Ay, öğrenci numaram 503020260092. Bu video, Makine Öğrenmesi ve
> Anomali Tespiti dersinin dönem projesi için ara rapor sunumum. Projenin konusu, gen
> ifadesi mikrodizi verisinden akut lenfoblastik lösemi, yani ALL, ile akut miyeloid
> lösemi, yani AML, ayrımını yapmak. Bu ara aşamada literatür taramasını, veri setlerini
> ve keşifsel veri analizini anlatacağım; model eğitimi final aşamasında olacak.

## 2. Problem ve araştırma soruları — 0:40–1:45

[EKRAN: Slayt 2 — Problem ve motivasyon.]

> Önce problemi doğru tanımlamak istiyorum. ALL lenfoid, AML ise miyeloid kökenli bir
> lösemi; yani ikisi de kanser. Ders modülündeki veri hazırlama adımlarında ALL için
> "non-cancer" ifadesi geçiyor, bu biyolojik olarak yanlış. Bu yüzden ben problemi
> "ALL ve AML alt tip sınıflandırması" olarak tanımladım. İki hastalığın tedavi
> protokolleri farklı, bu yüzden doğru ayrım klinik olarak doğrudan önemli.
>
> Mikrodizi, binlerce genin mRNA düzeyini tek bir deneyde ölçen bir çip. Ana veri
> setimiz Golub ve arkadaşlarının 1999 verisi: 72 hasta ve 7.129 prob. Yani öznitelik
> sayısı örnek sayısından yaklaşık yüz kat fazla; buna "p, n'den çok büyük" problemi
> deniyor ve projenin bütün zorluğu buradan geliyor.
>
> Dört araştırma sorum var. Birincisi: sızıntısız bir iç içe çapraz doğrulamada üç
> yöntem arasında anlamlı fark var mı? İkincisi: modüldeki 38'e 34'lük tek bölme, çapraz
> doğrulamanın güven aralığıyla tutarlı mı? Üçüncüsü: sinyal farklı hasta grupları ve
> farklı platformlar arasında taşınıyor mu? Dördüncüsü, bonus olarak: derin öğrenme ve
> transformer tabanlı modeller klasik yöntemlerden daha iyi mi?

## 3. Literatür — 1:45–2:45

[EKRAN: Slayt 3 — Literatür taraması.]

> Literatür taramasını yapay zekâ desteğiyle yürüttüm. Crossref, Europe PMC ve PubMed
> üzerinden arama yapıldı, ardından sızıntı ve dış doğrulama için hedefli ek tarama yapıldı.
> Sonuçta 52 kaynak var ve 31'i 2021 ve sonrasından; klasikleri veri ve özgün yöntemlerle
> sınırlı tuttum. 47 kaynağın tam metnine erişildi, 4'ünde yalnızca özet, birinde yalnızca
> künye görüldü. Rapordaki iddiaları kaynak
> metinlerle karşılaştırdık; bu denetim gerçek hatalar yakaladı. Örneğin Dudoit'nun
> alt eşiği 20 değil 100'müş, Golub'un hastalarının çoğu da yetişkin değil, çocukmuş.
> Bunları düzelttim; bütün notlar depoda duruyor.
>
> Literatürde gördüğüm asıl boşluk şu: Son dört Golub çalışmasında
> yüzde 97 ile 99,9 arasında doğruluklar raporlanmış, ama bu sayılar birbiriyle
> karşılaştırılamıyor. Bazı çalışmalar gen seçimini çapraz doğrulamanın dışında yapıyor
> görünüyor. Bunun iyimser sonuç verdiği 2002'den beri biliniyor; 2023 tarihli bir tarama da
> sızıntının 17 alanda en az 294 makaleyi etkilediğini bildiriyor. Bu dört çalışmada güven
> aralığı yok; okuduğumuz Golub çalışmalarında da model bağımsız bir kohorta aktarılmıyor.
> Bu proje bu eksikleri hedefliyor.

## 4. Veri setleri — 2:45–3:45

[EKRAN: Slayt 4 — Veri setleri tablosu ve sınıf dağılımı.]

> Üç veri seti kullanıyorum. Birincisi ana veri seti Golub: Affymetrix Hu6800 çipi,
> 47 ALL ve 25 AML; 38 eğitim, 34 bağımsız test örneği.
>
> İkincisi MILE çalışması, GEO numarası GSE13159. Çok merkezli bir çalışma; 2.096
> örnek ve 18 sınıf var. Ben bunlardan sadece ALL ve AML alt tiplerini aldım; KLL,
> KML, MDS ve sağlıklı örnekleri çıkardım. Geriye 750 ALL ve 542 AML, toplam 1.292
> örnek kaldı. Bu veri setini seçtim çünkü aynı klinik soruyu soruyor ve derin
> öğrenme bonusu için ön eğitimde kullanılabilecek kadar büyük.
>
> Üçüncüsü Andersson ve arkadaşlarının çocukluk çağı lösemi verisi, GSE7186. Bu
> farklı bir teknoloji: iki renkli cDNA dizisi, değerler referansa göre log oranı ve
> yaklaşık yüzde 7 eksik değer var. Bu veri seti, bulguların farklı bir platformda ve
> çocuk hastalarda geçerli olup olmadığını test etmek için zor bir dış test; aynı
> zamanda üçüncü veri seti bonusunu karşılıyor.
>
> Üç veri setinin de sınıf dağılımı ALL ağırlıklı; Golub'da oran yaklaşık yüzde 65'e 35.

## 5. Canlı kod — 3:45–5:15

[EKRAN: VS Code, `src/leukemia/data.py` → `load_golub` fonksiyonu. Webcam köşede.]

> Şimdi kodun kritik bir kısmını göstermek istiyorum. Golub CSV dosyasında hasta
> sütunları numara sırasında değil: eğitim dosyasında 1'den 27'ye kadar gidiyor, sonra
> 34–38, sonra 28–33 geliyor. Etiketleri sütun sırasına göre eşleseydim bazı hastalara
> yanlış etiket verilecekti. Bu yüzden etiketleri hasta numarası üzerinden
> birleştiriyorum. Burada da `assert` satırlarıyla eğitim ID'lerinin tam olarak 1'den
> 38'e, test ID'lerinin 39'dan 72'ye olduğunu ve sınıf sayılarının 27'ye 11, 20'ye 14
> olduğunu kontrol ediyorum.

[EKRAN: `src/leukemia/preprocessing.py` → `FoldChangeFilter` sınıfı.]

> Bu dosyada ön işleme adımları var. Hepsi scikit-learn dönüştürücüsü olarak yazıldı.
> Örneğin bu filtre, hangi genleri tutacağına `fit` sırasında, yani yalnızca eğitim
> verisine bakarak karar veriyor; `transform` ise sadece o kararı uyguluyor. Finalde bu
> adımlar bir Pipeline içinde her eğitim katında yeniden fit edilecek. Veri sızıntısını
> engelleyen şey tam olarak bu ayrım.

[EKRAN: Terminal. Komutu yaz ve çalıştır: `python scripts/run_eda.py --only golub`]

> Şimdi Golub için analiz betiğini çalıştırıyorum. Betik bütün şekilleri ve sayıları
> üretiyor ve bunları bir JSON dosyasına yazıyor. Raporu derleyen betik de bu
> sayıları LaTeX makrolarına çeviriyor. Yani rapordaki hiçbir sayıyı elle yazmadım;
> hocam herhangi bir sonucu bu komutla yeniden üretebilir. Rastgelelik için sabit
> seed 42 kullanılıyor.

[Betik bitince `results/figures` klasöründe yeni oluşan bir şekli kısaca aç, sonra slayta dön.]

## 6. Veri kalitesi ve dönüşüm — 5:15–6:05

[EKRAN: Slayt 5 — Veri kalitesi.]

> Veri kalitesine bakınca, Golub verisinde hiç eksik ya da sonsuz değer yok. Yani
> modüldeki "INF değerleri ortalamayla doldur" adımı orijinal dosyalarda aslında hiçbir
> şey değiştirmiyor. Ama değerlerin yüzde 28,7'si negatif. Bunun nedeni ölçüm yöntemi:
> eski Affymetrix yazılımı, tam eşleşen probun sinyalinden uyumsuz probun sinyalini
> çıkarıyor; ifade edilmeyen genlerde bu fark negatif olabiliyor. Nitekim "Absent"
> olarak işaretlenen ölçümler, yani yüzde 70, tam da bu düşük ve negatif değerler.

[EKRAN: Slayt 6 — Dönüşüm.]

> Bu yüzden değerleri rehberdeki gibi 20 ile 16.000 arasına kırpıp log2 dönüşümü uyguladım. Çarpıklık
> 7,08'den 0,55'e düştü. Genin ortalaması ile standart sapması arasındaki korelasyon da
> 0,95'ten 0,18'e indi. Yani dönüşüm, parlak birkaç genin SVM veya PCA gibi mesafeye
> dayalı yöntemlere baskın çıkmasını engelliyor.

## 7. Boyut indirgeme ve ayırt edici genler — 6:05–7:00

[EKRAN: Slayt 7 — Boyut indirgeme.]

> PCA'da varyans epey dağınık: ilk bileşen varyansın yalnızca yüzde 11'ini açıklıyor.
> Ama sadece bu ilk bileşen bile ALL ile AML'yi 0,984 AUC ile ayırıyor. MILE'da bu
> değer 0,987. Sinyal bu kadar güçlü olduğu için finalde yöntemler arasındaki farklar
> küçük çıkacak; bu yüzden güven aralığı ve istatistiksel test kullanmak zorunlu.

[EKRAN: Slayt 8 — Ayırt edici genler.]

> Her gen için Welch t-testi ve Mann–Whitney testi yaptım, çoklu test için
> Benjamini–Hochberg düzeltmesi uyguladım. Golub'da 945 gen anlamlı çıktı. En üstteki
> genler biyolojiyle uyumlu: CST3, CD33 ve MPO AML'de yüksek; TCF3, CD79B ve CD19 gibi
> B hücresi genleri ALL'de yüksek. Burada önemli bir uyarı var: bu sıralama tüm veri
> kullanılarak yapıldı, yani sadece betimsel. Modelde öznitelik seçimi için kullanılırsa
> veri sızıntısı olur.
>
> **[KISALTILABİLİR]** İlginç bir bulgu da Andersson verisinde çıktı: T hücreli ALL
> örnekleri, B hücresi programını taşımadıkları için kümelemede AML'nin yanına düşüyor.

## 8. Batch etkisi ve kohortlar arası analiz — 7:00–8:00

[EKRAN: Slayt 9 — Eğitim ve test seti.]

> Golub'un eğitim ve test setlerini karşılaştırdım. Test dizileri daha sönük: 75.
> yüzdelik değerin medyanı eğitimde 482, testte 421. Sınıf kompozisyonunun etkisini
> ayırmak için testi her sınıfın kendi içinde yaptım. ALL'de genlerin yüzde 17,7'si
> eğitim ile test arasında anlamlı farklı çıktı; dağılım kayması olmasaydı bu oran
> yüzde 5 civarında olurdu. Yani 34 örneklik tek bir test skoru, çapraz doğrulamadan
> sapabilir. İkinci araştırma sorum tam olarak bunu test edecek.

[EKRAN: Slayt 10 — Kohortlar arası karşılaştırma.]

> Üç veri setindeki ortak genlere baktığımda, genlerin t istatistikleri kohortlar
> arasında pozitif korelasyonlu: Golub ile MILE arasında 0,56. Her kohortun ilk 100
> geninden 33'ü Golub ve MILE'da ortak, ve hepsi aynı yönde değişiyor; bu tesadüfle
> açıklanamayacak kadar güçlü. Yani biyoloji taşınıyor. Ama ölçekler taşınmıyor: üç
> veriyi doğrudan birleştirince ilk ana bileşenin yüzde 99,8'ini hangi veri setinden
> geldiği açıklıyor. Her kohortu kendi içinde standartlaştırınca bu etki kayboluyor ve
> sınıf ayrımı ortaya çıkıyor.
>
> **[KISALTILABİLİR]** Bir de MILE ile ilgili bir veri kalitesi bulgusu var:
> GEO değerleri sinyal olarak tanımlıyor, ama her dizi tam olarak 0 ile 1 arasında. Bir
> örneği ArrayExpress'teki ham tablosuyla karşılaştırdım; değerler aslında ölçeklenmiş
> log yoğunluk. Bu kontrolü de koda ekledim.

## 9. Final planı ve kapanış — 8:00–9:00

[EKRAN: Slayt 11 — Bulgular ve modelleme kararları.]

> Bu bulguları doğrudan modelleme kararlarına çevirdim. Öznitelik seçimi her eğitim
> katının içinde yapılacak. Sınıf dengesizliği için katmanlı bölme ve dengeli doğruluk
> kullanılacak. Andersson'daki eksik değerler kat içinde doldurulacak. Kohortlar arası
> testte de her kohort kendi içinde standartlaştırılacak.

[EKRAN: Slayt 12 — Fizibilite pilotu.]

> Finalde planlanan ölçümler mümkün mü diye sabit ayarlı küçük bir pilot deneme yapıldı. Bu
> bir model karşılaştırması değil. Birincisi: etiketler rastgele karıştırıldığında bile, genler
> çapraz doğrulamadan önce seçilirse dengeli doğruluk 0,91 çıkıyor; doğru protokolde 0,50, yani
> şans düzeyinde. İkincisi: bir kohortta eğitilen model yalnızca eğitim istatistikleriyle başka
> kohorta aktarılınca, altı yönün dördünde AUC 0,965 ile 0,992 arasındayken dengeli doğruluk
> 0,50'ye düşüyor. Bu desen 2026'da sepsiste de bildirildi, yani yeni değil. Bizim özgün
> sorumuz şu: orada eşiği kurtaran sıra dönüşümü burada kurtarmıyor, ve eşik kaymasının
> platformdan mı sınıf oranından mı geldiği ayrılmamış. Bunlar ön bulgu. Golub'un 34 test
> örneği, MILE'ın ikinci aşaması ve TARGET verisi finale kadar kapalı tutuluyor.

[EKRAN: Slayt 13 — Final planı.]

> Finalde üç yöntem karşılaştıracağım: elastic-net lojistik regresyon, SVM ve random
> forest; modüldeki karar ağacı da taban model olarak kalacak. İki protokol olacak: 38'e
> 34'lük sabit bölmede test seti yalnızca bir kez kullanılacak, 72 örneğin tamamında da
> beş farklı seed ile tekrarlanan 5×5 iç içe çapraz doğrulama yapılacak. Bonus olarak MLP
> ve autoencoder, TabPFN, üçüncü veri seti ve hocamın onayıyla uluslararası bir IEEE
> konferansına İngilizce makale gönderimi planlıyorum; aday konferans IEEE EMBC 2027.

[EKRAN: Slayt 14 — Teşekkürler. Webcam büyütülebilir.]

> Kod deposu GitHub'da ve tek komutla bütün sonuçlar yeniden üretilebiliyor. Bu
> çalışmada kod, literatür okuması ve metin için Anthropic'in Claude modelini kullandım; nasıl
> kullandığımı ve neleri doğruladığımı GenAI beyanında ayrıntılı olarak yazdım.
> Dinlediğiniz için teşekkür ederim.

---

### Olası sorular için kısa notlar (videoda okumana gerek yok)

- **Neden negatif değer var?** MAS4 average difference = PM − MM ortalaması; MM > PM ise negatif.
- **P/A/M nedir?** Present/Marginal/Absent tespit çağrısı; probun gerçekten ifade edilip edilmediğinin istatistiksel kararı.
- **Neden iç içe CV?** Hiperparametre ve gen seçimi aynı katlarda hem ayarlanıp hem değerlendirilirse skor iyimser olur (Varma & Simon 2006).
- **Welch t-testi neden?** Sınıf varyansları eşit varsayılmıyor; Mann–Whitney ise dağılım varsayımı yapmıyor.
- **ARI nedir?** Kümeleme ile gerçek sınıfların uyumu; 1 tam uyum, 0 rastgele.
- **Neden taban 20, Dudoit'nun 100'ü değil?** 20 rehberden; taban 100 ile aynı süzgeç Dudoit'nun 3.571 genini birebir veriyor, 20 ile 3.859.
- **KS testi neyi gösteriyor?** Bir genin eğitim ve testteki dağılımlarının aynı olup olmadığını; kayma yoksa p-değerleri düzgün dağılır.
