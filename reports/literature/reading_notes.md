# Okuma notları: ALL/AML ara raporunun kaynakları

Hazırlanma tarihi: 2026-11-05. Bu dosya `reports/ara_rapor/main.tex` içindeki 38 kaynağın erişim düzeyini ve içeriğini kaydeder. Metinler yalnızca yasal kaynaklardan alındı: açık erişim, yayıncının ücretsiz sunduğu kopya, yazar veya kurum kopyası. Korsan kaynak kullanılmadı. Tüm özetler kendi cümlelerimizledir.

## Erişim özeti

Rapordaki güncel durum (2026-11-06, 52 kaynak):

| Erişim düzeyi | Sayı |
|---|---:|
| Tam metin | 47 |
| Yalnızca özet | 4 (andersson2007, alhenawi2022, whalen2022, bernett2024) |
| Yalnızca künye | 1 (benjamini1995) |

Güncel kaynaklara ağırlık vermek için 2026-11-06'da armstrong2002, statnikov2005, feltes2019, cawley2010, liu2006 ve cortes1995 rapordan çıkarıldı. Notları aşağıda arşiv olarak duruyor. Yeni 20 kaynağın notları dosyanın sonundadır.

İlk 38 kaynağın 2026-11-05 tarihli dökümü:

| Erişim düzeyi | Sayı | Kaynaklar |
|---|---:|---|
| Tam metin | 31 | golub1999, haferlach2010, kohlmann2008, furey2000, guyon2002, dudoit2002, tibshirani2002, diazuriarte2006, zou2005, ambroise2002, varma2006, cawley2010, leek2010, johnson2007, warnatherresthal2020, warnatherresthal2021, gorishniy2021, grinsztajn2022, hollmann2025, chen2025genept, alharbi2023, xie2022, rezaee2022, awotunde2022, selvaraj2024, breiman2001, cortes1995, nadeau2003, demsar2006, vandermaaten2008, pedregosa2011 |
| Yalnızca özet | 6 | andersson2007, armstrong2002, feltes2019, statnikov2005, alhenawi2022, liu2006 |
| Yalnızca künye | 1 | benjamini1995 |

Tam metinlerin okuma derinliği:

| Okuma derinliği | Sayı | Kaynaklar |
|---|---:|---|
| Gövdenin tamamı | 23 | golub1999, haferlach2010, kohlmann2008, guyon2002, tibshirani2002, zou2005, ambroise2002, varma2006, cawley2010, leek2010, warnatherresthal2020, warnatherresthal2021, gorishniy2021, grinsztajn2022, hollmann2025, chen2025genept, selvaraj2024, breiman2001, cortes1995, nadeau2003, demsar2006, vandermaaten2008, pedregosa2011 |
| Hedefli okuma (yöntem, veri, sonuç bölümleri) | 8 | furey2000, dudoit2002, diazuriarte2006, johnson2007, alharbi2023, xie2022, rezaee2022, awotunde2022 |

Notlar:

- Tam metne erişim her zaman yayımlanan son sürümün okunduğu anlamına gelmez. `dudoit2002` için JASA yerine 2000 tarihli teknik rapor, `chen2025genept` için dergi yerine bioRxiv preprint'leri, `leek2010` için yazar el yazması, `breiman2001` için yazar kopyası okundu.
- İstatistik, yöntem ve tablo verisi kaynaklarından 18'ini iki yapay zekâ okuyucu ajan yerel metinlerden okudu ("okuyucu ajan" ile işaretli). Belirleyici iddialarının bir bölümü kaynak metinde örneklem olarak denetlendi, tümü değil. Bu dosya yazarın kendi okuması yerine geçmez; GenAI beyanında buna göre yazılmalıdır.
- `furey2000` ve `johnson2007`, OUP'un ücretsiz sunduğu PDF'lerin, `golub1999` ise Broad Institute kopyasının Internet Archive kayıtlarından okundu.
- Erişilemeyenler: `andersson2007`, `armstrong2002`, `feltes2019`, `liu2006` abonelik gerektiriyor; `statnikov2005` için OUP bot denetimi aşılmadı; `alhenawi2022` için depoda indirilebilir dosya bulunamadı; `benjamini1995` için yasal olduğu kesin bir kopya bulunamadı.

## Raporda bulunmayan yardımcı kaynaklar

Bunlar yalnızca taban 20 sorusu için kullanıldı. İkisinin de tam metni okunmadı; yalnızca ilgili yöntem bölümü görüldü ve 38 kaynağa sayılmadı.

- **Ramaswamy ve ark. 2001, PNAS 98(26):15149-15154, doi:10.1073/pnas.211566398 (PMC64998).** Yöntem bölümünde Hu6800 ve Hu35KsubA dizileri için 20 birim eşik, 16.000 birim tavan, 5 kat ve 500 birim süzgeci verilir. Veri seti Golub lösemi değil, çok tümörlü bir kümedir. Taban 20 için bulunan tek açık kaynak budur.
- **Niijima ve Kuhara 2006, BMC Bioinformatics (PMC1790716).** Lösemi verisi için taban 100, tavan 16.000 ve 10 tabanlı log kullanıldığını bildirir; Dudoit bulgusunu bağımsız olarak doğrular.

## Kaynak notları

### golub1999

- **Künye anahtarı:** `golub1999`
- **Erişim düzeyi:** tam metin (Broad Institute'ün barındırdığı yazar kopyası, Internet Archive kaydı üzerinden; Şekil 3B sayfa görüntüsünden okundu). Gövde ve notların tamamı okundu.
- **Çalışmanın sorusu:** Kanser sınıfları önceden biyolojik bilgi olmadan, yalnızca gen ifadesiyle keşfedilip yeni örneklere atanabilir mi?
- **Veri:** 38 kemik iliği örneği (27 ALL, 11 AML) ve 34 bağımsız örnek (24 kemik iliği, 10 periferik kan; 20 ALL, 14 AML). Metin 6817 gen der. Tüm ALL'ler çocukluk bankalarından (DFCI 27+17, St. Jude 3); AML'lerin 15'i erişkin, 10'u çocuk.
- **Yöntem:** Sinyal-gürültü tipi korelasyon ölçütü P(g,c) ile 50 bilgi verici gen, ağırlıklı oylama ve tahmin gücü (PS) eşiği 0,3; sınıf keşfi için SOM.
- **Doğrulama protokolü:** 38 örnekte, gen seçimini her turda baştan yapan birini dışarıda bırakma CV'si; ardından 34 örneklik bağımsız küme.
- **Ana sonuç:** CV'de 38 örneğin 36'sı atandı, hepsi doğru, 2'si belirsiz. Bağımsız kümede 34 örneğin 29'u güçlü tahmin aldı, hepsi doğru, 5'i eşik altında kaldı. 10-200 gen arası öngörücüler de benzer sonuç verdi.
- **Bu projeyle ilgisi:** Ana veri setinin kaynağı; ayrıca veri kümesinin ağırlıklı olarak çocuk hastalardan oluştuğunu gösterir, raporun "mostly adult" ifadesi bununla çelişir. Şekil 3B'de AML-yüksek genler arasında Cystatin C, Zyxin ve CD33 vardır.
- **Sınırlılık:** Tek merkezli olmayan ama küçük bir örneklem; yazarlar testin mevcut tanıyı tamamlaması gerektiğini ve örnek hazırlığının standartlaştırılması gerektiğini vurgular. Tibshirani 2002 aynı yöntem için 4/34 test hatası aktarır, bu sayı Golub'un metninde yoktur.

### haferlach2010

- **Künye anahtarı:** `haferlach2010`
- **Erişim düzeyi:** tam metin (PMC5569671 HTML; XML uç noktası hata verdi). Gövdenin tamamı okundu, tablo hücreleri tek tek incelenmedi.
- **Çalışmanın sorusu:** Gen ifadesi profili, lösemileri standart alt tiplere ayıran tek bir test olarak klinikte işe yarar mı?
- **Veri:** 3 kıtada 11 laboratuvar, 3.334 hasta. Evre I: 2.143 profil, kalite sonrası 2.096 örnek, 18 sınıf, HG-U133 Plus 2.0. Evre II: 1.191 prospektif örnek, 1.152'si geçerli, özel AmpliChip Leukemia dizisi. Evre I'de akut lösemi sayısı 1.292.
- **Yöntem:** Özetleme ve kuantil normalleştirme (DQN); tüm sınıf çiftleri için doğrusal ikili SVM ve oylama. Her CV turunda çift başına t istatistiğine göre en iyi 100 prob seti seçilir.
- **Doğrulama protokolü:** Evre I'de üç bağımsız 30 katlı CV; evre II'de evre I modelinin kör, bağımsız sınaması.
- **Ana sonuç:** Evre I CV doğruluğu 18 sınıfta %92,2 (medyan özgüllük %99,7). Evre II'de 18 sınıfta %88,1, 14 akut lösemi sınıfında %91,5; medyan duyarlılık %95,6, özgüllük %99,8 (n=693).
- **Bu projeyle ilgisi:** MILE kohortunun birincil kaynağı. Projenin 1.292 örneği makaledeki akut lösemi sayısıyla örtüşür. Makale ham veri için GSE13204 üst serisini verir; GEO'ya göre GSE13159 bunun evre I alt serisidir.
- **Sınırlılık:** %92,2 prospektif değil CV değeridir. Altın standart tanı merkezler arasında standart değildir, yani etiketler merkezden merkeze değişebilir. Örnekler merkezlere eşit dağılmamıştır. Çalışma Roche destekli.

### kohlmann2008

- **Künye anahtarı:** `kohlmann2008`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC2654477). Gövdenin tamamı okundu, ek dosyalar yok.
- **Çalışmanın sorusu:** Mikrodizi iş akışı, hasta örnekleri işlenmeden önce 11 laboratuvarda tekrarlanabilir hale getirilebilir mi?
- **Veri:** 204 mikrodizi analizi; iki hücre hattı (MCF-7, HepG2) ve lösemi hastası lizatları; HG-U133 Plus 2.0.
- **Yöntem:** MILE ön fazı: aynı ekipmanla yerinde protokol eğitimi, ardından bağımsız yeterlik testi; denetimsiz PCA ve r² korelasyonları.
- **Doğrulama protokolü:** Sınıflandırıcı doğrulaması yoktur; laboratuvar içi ve laboratuvarlar arası tekrarlanabilirlik ölçülür.
- **Ana sonuç:** Profiller merkeze değil örnek tipine göre kümelenir. HepG2'de ortalama r² laboratuvar içinde 0,973-0,988, Merkez 3 ile diğerleri arasında 0,959-0,985. Az sayıda aykırı örnek işaretlenmiştir.
- **Bu projeyle ilgisi:** "Standardised protocols" ifadesinin doğrudan dayanağıdır; MILE'daki merkez etkisinin neden sınırlı olabileceğini açıklar.
- **Sınırlılık:** Kanıt hücre hatları ve kopya lizatlara dayanır, hasta kohortuna değil. Roche çalışanları yazardır. Ek dosyalar okunmadı.

### andersson2007

- **Künye anahtarı:** `andersson2007`
- **Erişim düzeyi:** yalnızca özet (Europe PMC özeti ve nature.com sayfası) artı GEO GSE7186 kaydı. Dergi metni aboneliğe tabi; Lund Üniversitesi deposunda dosya yok.
- **Çalışmanın sorusu:** Ardışık bir çocukluk lösemi serisinde gen ifadesi alt tip, genetik grup ve MRD durumunu öngörebilir mi?
- **Veri:** Tek merkezde 8 yılda toplanan 121 lösemi (87 B-soy ALL, 11 T-ALL, 23 AML). GEO: 108 kemik iliği, 13 periferik kan, ayrıca 6 normal kemik iliği.
- **Yöntem:** k-en yakın komşu öngörücüleri, denetimsiz analiz. GEO işleme notu: pin tabanlı lowess, hastaneye göre ortalama merkezleme, %40 varlık filtresi; örnek Cy3, referans Cy5.
- **Doğrulama protokolü:** Özete göre bağımsız bir veri setinde doğrulama; ayrıntı görülmedi.
- **Ana sonuç:** Özete göre alt tiplerde yüksek doğruluk; yüksek MRD'li T-ALL'lerde tanıda %100. Sayısal alt tip doğrulukları görülmedi.
- **Bu projeyle ilgisi:** Üçüncü veri setinin kaynağı. Raporun k-NN, 121 vaka ve 108/13 bilgileri özet ve GEO ile örtüşür, ama 108/13 için kaynak makale değil GEO'dur.
- **Sınırlılık:** Tam metin okunmadı. Özet tek merkez derken GEO hastaneye göre merkezlemeden söz eder; bunun açıklaması makalede olabilir.

### armstrong2002

- **Künye anahtarı:** `armstrong2002`
- **Erişim düzeyi:** yalnızca özet (Europe PMC). Dergi metni aboneliğe tabi; yasal açık kopya bulunamadı.
- **Çalışmanın sorusu:** MLL translokasyonlu lenfoblastik lösemiler ayrı bir ifade profiline sahip midir?
- **Veri:** Özette örnek sayısı yok; MLL, ALL ve AML grupları.
- **Yöntem:** Kümeleme ve sınıflandırma; ayrıntı görülmedi.
- **Doğrulama protokolü:** Görülmedi.
- **Ana sonuç:** Özete göre MLL translokasyonlu ALL'ler klasik ALL ve AML'den ayrılır; yazarlar bunu ayrı bir hastalık olarak önerir.
- **Bu projeyle ilgisi:** ALL/AML ikiliğinin altındaki alt tip yapısını hatırlatır.
- **Sınırlılık:** Özet düzeyinde; özet "MLL'li ALL" der, raporun "MLL-rearranged leukemias" ifadesi daha geniştir.

### feltes2019

- **Künye anahtarı:** `feltes2019`
- **Erişim düzeyi:** yalnızca özet (Europe PMC). Dergi metni aboneliğe tabi.
- **Çalışmanın sorusu:** Kanser mikrodizileri için makine öğrenmesi kıyaslamasına uygun küratörlü bir veri tabanı oluşturulabilir mi?
- **Veri:** GEO'daki 30.000'den fazla deneyden seçilen 78 Homo sapiens mikrodizi veri seti.
- **Yöntem:** Arka plan düzeltme, normalleştirme, örnek kalite analizi, hatalı probların ayıklanması; PCA ve t-SNE ile inceleme.
- **Doğrulama protokolü:** Çeşitli ML yöntemleriyle taban doğruluk; ayrıntı görülmedi.
- **Ana sonuç:** CuMiDa kıyaslama amaçlı veri tabanı olarak sunulur.
- **Bu projeyle ilgisi:** Selvaraj 2024'ün ikinci veri kaynağı; raporda kıyaslama kaynağı olarak anılır.
- **Sınırlılık:** Özet düzeyinde; Golub verisini içerip içermediği görülmedi.

### furey2000

- **Künye anahtarı:** `furey2000`
- **Erişim düzeyi:** tam metin (OUP'un ücretsiz sunduğu PDF'in Internet Archive kaydı; OUP güncel adresi bot denetimi nedeniyle açılmadı). Hedefli okuma: yöntem, yumurtalık ve AML/ALL sonuçları; kolon kısmı ve kapanış okunmadı.
- **Çalışmanın sorusu:** SVM mikrodizi verisiyle doku sınıflandırabilir ve hatalı etiketli örnekleri bulabilir mi?
- **Veri:** 31 yumurtalık dokusu (97.802 klon), Golub 72 örnek (7129 gen), Alon kolon 62 örnek.
- **Yöntem:** Skaler çarpım çekirdekli SVM, diyagonal faktör ayarı; Golub'unkine yakın bir skorla gen sıralama.
- **Doğrulama protokolü:** Birini dışarıda bırakma; gen sıralaması her turda yalnızca bilinen örneklerle yapılır. Golub için 38 eğitim ve 34 test (metinde 24 yazım hatası).
- **Ana sonuç:** Golub eğitiminde LOOCV hatasız; testte 34 örneğin 30-32'si doğru. Yazarlara göre hiçbir teknik diğerlerinden anlamlı üstün değil, perseptron türevleri de SVM ile yakın.
- **Bu projeyle ilgisi:** SVM'nin Golub verisine erken uygulaması ve CV içinde seçim yapan erken bir örnek.
- **Sınırlılık:** Makale SVM'nin mikrodizide varsayılan yöntem olduğunu söylemez; diyagonal faktör CV sonuçlarına bakılarak seçilir.

### guyon2002

- **Künye anahtarı:** `guyon2002`
- **Erişim düzeyi:** tam metin (Springer ücretsiz PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Korelasyon temelli tek değişkenli sıralama yerine, çok değişkenli bir SVM'nin ağırlıklarıyla daha küçük ve daha iyi gen altkümeleri bulunabilir mi?
- **Veri:** Golub lösemi (7129 gen, 38 eğitim, 34 test; 72 örneğin tümü de kullanılır) ve Alon kolon verisi (62 doku, 2000 gen).
- **Yöntem:** SVM-RFE: doğrusal SVM eğitilir, ağırlık karesi en küçük genler özyinelemeli çıkarılır; yazarlar bunu geriye doğru eleme örneği olarak tanımlar. Lösemide her adımda genlerin yarısı atılır.
- **Doğrulama protokolü:** Eğitimde LOO ve sabit test (lösemi 38/34, kolon 31/31), ayrıca tüm veri üzerinde LOO. Gen seçiminin LOO katları içinde yinelendiğine dair bir ifade yoktur; tablolar test verisinde en iyi gen sayısını raporlar.
- **Ana sonuç:** Lösemide SVM genleriyle 8 veya 16 gende 0/34 test hatası, Golub genleriyle 64 gende 1/34; tüm veride seçilen 2 gen sıfır LOO hatası verir. Kolonda 4 genle %98'e karşı %86 bildirilir. Seçilen genler sınıflandırıcıdan daha belirleyicidir.
- **Bu projeyle ilgisi:** SVM kolunun ve gen seçiminin tarihsel dayanağıdır; ayrıca Golub eğitim ve test dağılımlarının veri kaynağına bağlı olarak farklılaştığını bildirir.
- **Sınırlılık:** Bildirilen LOO değerleri seçim yanlılığına açıktır; Ambroise ve McLachlan bu nedenle içsel CV'yi eleştirir. Yazarlar yanlılığı tartışmaz, ancak mutlak sonuçlara küçük örneklem nedeniyle temkinle bakılmasını ister ve LOO hatası sıfır olan bir gen çiftinin testte 13/34 hata yaptığını aktarır.

### dudoit2002

- **Künye anahtarı:** `dudoit2002`
- **Erişim düzeyi:** tam metin (UC Berkeley İstatistik teknik raporu no. 576, Haziran 2000). JASA 2002 sürümü değildir. Hedefli okuma: giriş, veri, tasarım, sonuç ve tartışma; yöntem bölümü taranmıştır.
- **Çalışmanın sorusu:** Tümör sınıflandırmasında basit ve karmaşık ayırma yöntemleri nasıl karşılaştırılır?
- **Veri:** Lenfoma (81 örnek, 4.682 gen), Golub lösemi (72 örnek), NCI 60 (61 örnek, 5.244 gen).
- **Yöntem:** Lösemide taban 100, tavan 16.000, max/min ve max-min süzgeci, 10 tabanlı log; 72×3571 matris (Pablo Tamayo'dan kişisel iletişim). BSS/WSS seçimi; FLDA, DLDA, DQDA, k-NN, CART, bagging, boosting, Golub oylaması.
- **Doğrulama protokolü:** 2:1 rastgele öğrenme/test bölmesi, 150 tekrar; gen seçimi (lösemide p=40) her turda yalnızca öğrenme kümesinde yapılır.
- **Ana sonuç:** Basit DLDA ve k-NN en düşük hataları verir, FLDA en kötüdür; iki sınıflı lösemide DLDA'nın medyan hatası sıfırdır. Golub'un 38/34 bölmesinin hatası rastgele bölmelerdekine benzer; öğrenme ve test etiketini ayırma denemesinde hata yaklaşık %25'tir.
- **Bu projeyle ilgisi:** Raporun taban değerini ona atfetmesi hatalıdır. Proje verisinde taban 100 ve iki koşullu süzgeç tam 3.571 gen verdi, taban 20 ise 3.859 gen verdi.
- **Sınırlılık:** Süzgeç cümlesi "ve" bağlacıyla yazılmıştır; 3.571 sayısı ancak koşullardan biri sağlanmayınca dışlama ile elde edildi. Yayımlanan JASA metni okunmadı.

### tibshirani2002

- **Künye anahtarı:** `tibshirani2002`
- **Erişim düzeyi:** tam metin (PMC124443 HTML; XML uç noktası hata verdi). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Az sayıda gen kullanan, yorumu kolay ve çok sınıfa uygun bir kanser sınıflandırıcısı kurulabilir mi?
- **Veri:** SRBCT (2308 gen, 63 eğitim, 25 test, testin 5'i SRBCT değil) ve Golub lösemi verisi (7129 gen, 38 eğitim, 34 test).
- **Yöntem:** Sınıf merkezlerini standartlaştırılmış farklar üzerinde yumuşak eşikleme ile küçülten en yakın küçültülmüş merkez yöntemi; Δ büyüdükçe gen sayısı düşer.
- **Doğrulama protokolü:** Eğitimde 10 katlı CV ve sabit test kümesi. SRBCT'de Δ=4,34 hem CV hem test hatasının en düşük olduğu nokta olarak bildirilir; lösemide Δ=4,06, CV hatasının hızla yükselmeye başladığı noktadır.
- **Ana sonuç:** SRBCT'de 43 genle eğitim ve test hatası sıfırdır. Golub'da CV 1/38, test 2/34, 21 gen elde edilir; Golub yöntemi için tabloda 3/38, 4/34 ve 50 gen yer alır. CV minimumu Δ yaklaşık 1,4'te olup yaklaşık 1000 gen bırakır.
- **Bu projeyle ilgisi:** Golub için doğrudan karşılaştırma değeri sağlar ve seyrek, yorumlanabilir bir referans yöntem sunar.
- **Sınırlılık:** Test eğrisi ayarlama sırasında görünürdür; Varma ve Simon SRBCT seçimini bu yüzden eleştirir. Tek bölme ve küçük test kümesi vardır; metin lösemi verisini bir yerde 34 örnek diye özetler.

### diazuriarte2006

- **Künye anahtarı:** `diazuriarte2006`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC1363357). Hedefli okuma: özet, veri ve tablolar, yöntem ve hata tahmini, tartışma karşılaştırmaları.
- **Çalışmanın sorusu:** Rastgele orman mikrodizi sınıflandırmasında ne kadar iyidir ve gen seçimi için kullanılabilir mi?
- **Veri:** Simülasyon ve dokuz mikrodizi çalışması (Tablo 1'de 10 satır). Lösemi satırı 3.051 gen, 38 hastadır; yani Golub'un eğitim kümesi, 72 örnek değil.
- **Yöntem:** Değişken önemine göre geriye doğru eleme; karşılaştırma SVM, k-NN, DLDA (F oranına göre 200 gen), küçültülmüş merkezler ve NN.vs.
- **Doğrulama protokolü:** 200 örneklemli .632+ bootstrap tüm seçim sürecine uygulanır; seçimdeki OOB hatası raporlanan hata değildir.
- **Ana sonuç:** Lösemide .632+ hata: SVM 0,014, k-NN 0,029, DLDA 0,020, seçimsiz RF 0,051, seçimli RF 0,087 ve 0,075. Yöntem çok az gen seçer (lösemide 2).
- **Bu projeyle ilgisi:** RF kolunun dayanağı. Rapordaki 0,051 seçimsiz RF'ye aittir ve 38 örnek üzerindedir.
- **Sınırlılık:** Hatalar yöntemler arasında çoğu kez benzerdir; lösemi 38 örnekle sınırlıdır.

### statnikov2005

- **Künye anahtarı:** `statnikov2005`
- **Erişim düzeyi:** yalnızca özet (Europe PMC). OpenAlex ücretsiz OUP kopyası gösteriyor, ama OUP otomatik erişimi ve tarayıcıyı bot doğrulamasıyla durdurdu; bu denetim aşılmaya çalışılmadı, arşiv kopyası da bulunamadı.
- **Çalışmanın sorusu:** Çok sınıflı kanser tanısında en iyi sınıflandırıcı, gen seçimi ve CV birleşimi hangisidir?
- **Veri:** 74 tanı kategorisini kapsayan 11 veri seti.
- **Yöntem:** Çok sınıflı SVM'ler, k-NN, sinir ağları, topluluklar, gen seçimi; GEMS sistemi.
- **Doğrulama protokolü:** Özete göre iki CV tasarımı; ayrıntı görülmedi.
- **Ana sonuç:** Özete göre çok sınıflı SVM'ler en etkilidir; gen seçimi yardımcı olur, topluluklar en iyi tekil modeli genelde geçmez.
- **Bu projeyle ilgisi:** SVM'nin yüksek boyutlu mikrodizide güçlü olduğunun dayanağı.
- **Sınırlılık:** Özet düzeyinde; ikili ALL/AML için doğrudan sayı görülmedi.

### zou2005

- **Künye anahtarı:** `zou2005`
- **Erişim düzeyi:** tam metin (Hastie'nin Stanford sayfasındaki yazar kopyası). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Lasso'nun p>n durumunda en çok n değişken seçmesi ve ilişkili değişken gruplarından tek üye alması sorunları giderilebilir mi?
- **Veri:** Prostat kanseri verisi (8 değişken, 67/30), dört benzetim senaryosu ve Golub lösemi verisi (7129 gen, 38 eğitim, 34 test).
- **Yöntem:** L1 ve L2 cezasını birleştiren en küçük kareler regresyonu (elastik ağ), yeniden ölçeklenmiş tahminci ve LARS-EN algoritması; gruplama etkisi kuramsal olarak gösterilir.
- **Doğrulama protokolü:** Lösemide 0-1 kodlu yanıt ve 0,5 eşiği, eğitimde 10 katlı CV, sabit 34 örnekli test; en anlamlı 1000 gen t istatistiğiyle her eğitim katında ayrı ayrı önelenir.
- **Ana sonuç:** Elastik ağ lasso'dan genelde daha doğrudur. Lösemide λ=0,01 ve 82. adımda CV hatası 3/38, test hatası 0/34, seçilen gen sayısı 45'tir.
- **Bu projeyle ilgisi:** Seyreklik ve ilişkili genleri birlikte tutma gerekçesinin kaynağıdır ve Golub bölmesinde doğrudan sonuç verir; ceza terimi için uygun atıftır.
- **Sınırlılık:** Lojistik kayıp işlenmez; sınıflandırma kare kayıplı regresyonla yapılır, binom sapma yalnızca olasılık olarak anılıp gelecek çalışmaya bırakılır. Tek bölme vardır ve yöntemler arası fark birkaç örnekten oluşur.

### ambroise2002

- **Künye anahtarı:** `ambroise2002`
- **Erişim düzeyi:** tam metin (PMC124442 HTML; XML uç noktası hata verdi). Gövdenin tamamı okundu; şekil değerleri metinden alındı.
- **Çalışmanın sorusu:** Gen seçimi hata tahmininin dışında bırakılırsa bildirilen hata ne kadar iyimser olur, nasıl düzeltilir?
- **Veri:** Alon kolon (62 doku, 2.000 gen) ve Golub lösemi (72 örnek, 7.129 gen).
- **Yöntem:** Doğrusal SVM ile RFE ve Fisher ayırıcı ile ileri seçim.
- **Doğrulama protokolü:** İçsel LOO hatası, seçimi de kapsayan dış 10 katlı CV ve .632+ bootstrap; 50 rastgele eğitim-test bölmesi (lösemide 38/34, Golub'un sabit bölmesi değil); etiket karıştırma denemesi.
- **Ana sonuç:** İçsel hata birkaç genle sıfıra iner, dış hata inmez. Seçim yanlılığı lösemide 38/34 bölmede yaklaşık %5, 72 örneğin tümüyle %2-3; kolonda daha büyüktür. Karıştırılmış etiketlerde de içsel hata sıfıra yaklaşır, dış hata 0,40-0,45 kalır.
- **Bu projeyle ilgisi:** Projenin katlar içinde seçim kararının temel dayanağıdır; 10 katlı CV'yi LOO'ya tercih eder.
- **Sınırlılık:** Rakamlar iki veri setinden ve şekillerden gelir; yazarlar Fisher kuralındaki 400 gen ön seçiminin küçük bir yanlılık taşıdığını kabul eder.

### varma2006

- **Künye anahtarı:** `varma2006`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC1397873). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Parametreleri CV hatasını en aza indirerek ayarlanmış bir sınıflandırıcının bu minimum CV hatası, bağımsız veride beklenen gerçek hatayı doğru tahmin eder mi?
- **Veri:** Yalnızca benzetim: her senaryoda en az 1000 veri kümesi, 40 örnek (20/20), 6000 sentetik özellik; "null" veride sınıf farkı yok, "non-null" veride 10 gen fark taşır; gerçek hata 20000 bağımsız örnekle ölçülür. Gerçek mikrodizi verisi kullanılmaz.
- **Yöntem:** Küçültülmüş merkezler (Δ, 10 katlı CV ile) ve Gauss çekirdekli SVM (C ve γ, LOOCV ile; her katta en iyi 3 gen t istatistiğiyle seçilir).
- **Doğrulama protokolü:** Ayarlı minimum CV hatası ile iç içe CV (dış döngü LOOCV) karşılaştırılır; iç içe CV gövdede küçültülmüş merkezler için null, SVM için non-null veride uygulanır.
- **Ana sonuç:** Null veride ortalama CV hatası %37,8 (merkezler) ve %41,7 (SVM), gerçek hata %50; iç içe CV %54,2'ye karşı %50 ve %35,3'e karşı %32,0 verir. Yanlılık büyük ölçüde azalır, kalan fark karamsar yöndedir; yazarlar sonucu "neredeyse yansız" olarak niteler.
- **Bu projeyle ilgisi:** Ayarlamanın dış döngü içinde yapılması gerektiğinin dayanağıdır; ancak yazarlar bu sonucu dış döngüde dışarıda bırakılan örnek sayısının çok büyük olmaması koşuluna bağlar, projenin 5 katlı dış döngüsü bundan farklıdır.
- **Sınırlılık:** Bulgular bağımsız normal dağılımlı benzetime dayanır; hatanın %30'un altında kaldığı SVM denemeleri için özette %38, Tablo 1'de %22,2 verilir.

### cawley2010

- **Künye anahtarı:** `cawley2010`
- **Erişim düzeyi:** tam metin (JMLR PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Model seçim ölçütünün varyansı, model seçiminde aşırı uyuma ve ardından başarım değerlendirmesinde seçim yanlılığına ne ölçüde yol açar?
- **Veri:** Ripley temelli sentetik problem ile Rätsch ve arkadaşlarının 13 kıyas veri kümesi (çoğunda 100, image ve splice için 20 bölme).
- **Yöntem:** Çekirdek sırt regresyonu, çekirdek lojistik regresyon ve Gauss süreci sınıflandırıcısı; RBF ve ARD çekirdekleri, PRESS ve Bayesçi kanıt ölçütleri.
- **Doğrulama protokolü:** Her bölmede yeniden seçim yapan "internal" protokol ile "median" ve seçimi CV dışında yapan "external" protokoller karşılaştırılır; yöntem sıralamaları Demšar'ın kritik fark diyagramıyla gösterilir.
- **Ana sonuç:** Düşük varyans en az yansızlık kadar önemlidir; seçimin dışarıda yapılması 13 kümenin tümünde iyimser yönde fark üretir (Tablo 8: yaklaşık 0,02 ile 1,19 puan) ve bu fark algoritmalar arası farklarla kıyaslanabilir büyüklükte olabilir.
- **Bu projeyle ilgisi:** Seçim her dış eğitim kümesinde yeniden yapılmalı ve karşılaştırma "algoritma + seçim yöntemi" birleşimleri için yorumlanmalıdır; yöntemlere farklı arama stratejileri uygulamak bu nedenle yorumu etkiler.
- **Sınırlılık:** İç içe CV yalnızca girişte adıyla anılır; çalışma tahminin varyansının ya da seçim aşamasındaki aşırı uyumun kendisinin ortadan kalktığını söylemez, veriler de düşük boyutludur.

### leek2010

- **Künye anahtarı:** `leek2010`
- **Erişim düzeyi:** tam metin (PMC3880143 HTML, yazar el yazması; XML uç noktası hata verdi). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Yüksek verimli ölçümlerde toplu iş (batch) etkileri ne kadar yaygındır, sonuçları nelerdir ve nasıl ele alınmalıdır?
- **Veri:** Yayımlanmış mesane kanseri örneği ve dokuz veri kümesinin yeniden analizi: gen ifadesi, kütle spektrometrisi, kopya sayısı, metilasyon ve 1000 Genom dizileme verisi.
- **Yöntem:** Tarih veya işleme grubunu vekil alarak doğrusal modeller, varyans analizi ve temel bileşen analizi; deneysel tasarım ve istatistiksel çözümlerin derlemesi.
- **Doğrulama protokolü:** Sınıflandırıcı doğrulaması yoktur; özellik başına ilişki testleri, FDR ve temel bileşenlerin vekil değişkenlerle karşılaştırılması kullanılır.
- **Ana sonuç:** Özelliklerin %32,1-99,5'i işleme tarihi veya grubuyla ilişkilidir; teknik değişkenlik çoğu kez biyolojiden daha etkilidir, normalleştirme bunu gidermez ve genler arası korelasyonlar bile değişebilir.
- **Bu projeyle ilgisi:** Kohortlar arası aktarımda kohort ile sınıf bileşiminin karışmasına dikkat etmeyi ve gen bazında standardizasyonu tek başına yeterli saymamayı gerekçelendirir.
- **Sınırlılık:** Düzeltme yöntemleri ayrıntılı karşılaştırılmaz; ComBat yalnızca web sitesi ve kaynakçayla anılır, SVA daha ayrıntılıdır. Yöntemlerin toplu iş biyolojiyle güçlü karıştığında zayıfladığı belirtilir. Yazar el yazması sürümü okunmuştur, ek bilgi kutusu dahil değildir.

### johnson2007

- **Künye anahtarı:** `johnson2007`
- **Erişim düzeyi:** tam metin (OUP'un ücretsiz sunduğu PDF'in Internet Archive kaydı). Hedefli okuma: özet, giriş, konum-ölçek bölümü, tartışma.
- **Çalışmanın sorusu:** Küçük toplu işlerde (batch) gen ifadesi verisi nasıl güvenilir biçimde düzeltilir?
- **Veri:** İki örnek veri seti; biri HG-U133A ile fibroblast deneyi, ikincisinin ayrıntısı ek dosyada.
- **Yöntem:** Parametrik ve parametrik olmayan ampirik Bayes konum-ölçek düzeltmesi; genler arası bilgi paylaşımı.
- **Doğrulama protokolü:** Düzeltme öncesi ve sonrası kümeleme ve aşağı akış analizleri; sınıflandırıcı doğrulaması yok.
- **Ana sonuç:** Yöntem küçük toplu işlerde aykırı değerlere dayanıklıdır, büyük örneklerde mevcut yöntemlerle kıyaslanabilir.
- **Bu projeyle ilgisi:** Kohortlar arası düzeltme için aday. Makale toplu iş başına basit standardizasyonu en sade konum-ölçek düzeltmesi sayar, dengesiz tasarımlarda daha genel model gerektiğini söyler; kohortların sınıf oranları farklı olduğu için bu önemlidir.
- **Sınırlılık:** "ComBat" adı makale metninde geçmez, yazılım yalnızca adresle verilir. Örnekler platformlar arası aktarım değildir.

### warnatherresthal2020

- **Künye anahtarı:** `warnatherresthal2020`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC6992905; Transparent Methods ve ek tablolar yok). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Uzman girdisi ve önceden gen seçimi olmadan, kan transkriptomundan makine öğrenmesiyle AML öngörülebilir mi; bu öngörü çalışmalar ve platformlar arasında korunur mu?
- **Veri:** GEO'dan 105 çalışma, 12.029 PBMC veya kemik iliği örneği: HG-U133A (2.500), HG-U133 2.0 (8.348), RNA-seq (1.181). 4.145 AML'ye karşı 7.884 AML dışı örnek; negatif sınıfta ALL (3.466), CLL, CML, MDS, sağlıklı kontroller ve lösemi dışı hastalıklar var.
- **Yöntem:** Her platform ayrı normalize edilmiş (RMA, DESeq2), ortak 12.708 gen kullanılmış; ana model L1 cezalı lojistik regresyon (lasso), yanında dokuz sınıflandırıcı ve derin ağ denenmiş.
- **Doğrulama protokolü:** %20 test payıyla 100 yinelemeli rastgele ayırma, eğitim ve test çalışmalarının tümüyle ayrık olduğu çapraz-çalışma senaryosu, bir platformda eğitip başka platformda sınama; ayrıca kontrollerin yalnızca diğer lösemiler ve MDS olduğu ayırıcı tanı senaryosu.
- **Ana sonuç:** Yüksek boyutlu modeller doğru ve sağlam bulunmuş. Çapraz-çalışma başarımı rastgele ayırmadan düşük, fark yalnızca en büyük veri setinde neredeyse kapanıyor; U133A'dan RNA-seq'e aktarım ham haliyle başarısız, sıra dönüşümüyle düzeliyor. Derin ağlar lassoya benzer sonuç vermiş.
- **Bu projeyle ilgisi:** Görev AML'ye karşı geri kalanlar olduğu için ALL negatif sınıfın yalnızca bir parçası; doğrudan ALL/AML ikili görevi değil. Çapraz-platform bulguları ve sıra dönüşümü RQ3 için yol gösterici.
- **Sınırlılık:** Ana metinde sayısal doğruluk yok (şekil ve ek tablolarda); 2026-11-06'da ek dosyalar okundu: GSE13159 veri seti 2'de 1.860 örnekle yer alır (AML 538, ALL 520); GSE7186 yoktur. Veriler farklı amaçlı çalışmalardan havuzlanmış, prospektif doğrulama yok; metindeki alt grup sayılarının toplamı 7.881 ediyor, verilen toplam 7.884.

### warnatherresthal2021

- **Künye anahtarı:** `warnatherresthal2021`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC8189907; ek bilgiler yok). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Ham veri paylaşılmadan ve merkezi bir koordinatör olmadan, dağıtık tıbbi verilerle hastalık sınıflandırıcısı eğitilebilir mi?
- **Veri:** 127 klinik çalışmadan 16.400'den fazla kan transkriptomu ve 95.000'den fazla göğüs röntgeni; dört kullanım alanı lösemi, tüberküloz, akciğer patolojileri ve COVID-19. Lösemi kısmı 2020 çalışmasının A1-A3 veri setleri (2.500, 8.348 ve 1.181 örnek).
- **Yöntem:** Swarm Learning: düğümler yerel eğitim yapıp yalnızca model parametrelerini izinli blokzincir ağı üzerinden birleştiriyor. Varsayılan model sekiz gizli katmanlı Keras sinir ağı; lasso da denenmiş.
- **Doğrulama protokolü:** Havuzlanmış veri, örtüşmeyen eğitim ve küresel test kümelerine ayrılmış; eğitim örnekleri düğümlere farklı dağılımlarla yerleştirilerek senaryolar benzetilmiş. AML ve ALL senaryoları 100 permütasyon, tek yönlü Wilcoxon testi. Düğümler iki sunucudaki Docker kapsayıcıları (3-32 düğüm).
- **Ana sonuç:** Swarm, tek tek düğümlerin tümünden iyi; AML'de merkezi modelin biraz gerisinde veya ona yakın. ALL vaka senaryoları, dört lösemi türlü çok sınıflı görev ve lasso ile bulgular yinelenmiş.
- **Bu projeyle ilgisi:** Lösemi düğümleri gerçek merkezler değil, havuzlanmış kamu verisinin benzetilmiş bölümleri; bir senaryoda düğümlere ayrı çalışmalar atanmış. Kontroller AML dışındaki tüm örnekler, yani ALL/AML ikili görevi değil. Merkez kökenli alt veri setleri yalnızca COVID-19 kısmında (E1-E8).
- **Sınırlılık:** Ana metinde sayısal lösemi doğruluğu yok; sonuçlar ek tablolarda ve bunlar elimizde yok. Bazı senaryolarda hiperparametreler başarım için ayarlanmış, ayarın hangi veride yapıldığı ana metinde belirtilmemiş. Yazarların bir bölümü yazılımı geliştiren HPE çalışanı.

### gorishniy2021

- **Künye anahtarı:** `gorishniy2021`
- **Erişim düzeyi:** tam metin (NeurIPS bildiri PDF, ek materyal yok). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Tablo verisi için derin mimariler aynı protokolde karşılaştırıldığında hangisi en iyi, derin modeller GBDT'yi geçebiliyor mu?
- **Veri:** Herkese açık 11 veri seti; örnek sayısı 20.640 ile yaklaşık 1,2 milyon, öznitelik sayısı 8 ile 2.000 arasında.
- **Yöntem:** ResNet benzeri bir model ile FT-Transformer öneriliyor; MLP, SNN, NODE, TabNet, GrowNet, DCN V2, AutoInt ile XGBoost ve CatBoost karşılaştırılıyor.
- **Doğrulama protokolü:** Her veri setinde tek sabit eğitim-doğrulama-test ayrımı; ayar yalnızca doğrulama kümesinde, çoğunlukla Optuna ile; 15 tohum ve beşer modelli üç topluluk.
- **Ana sonuç:** FT-Transformer derin modeller arasında görevlerin çoğunda en iyi. Ayarlı GBDT ise bazı veri setlerinde önde (California Housing, Adult, Yahoo); yazarlara göre evrensel bir üstün çözüm yok ve kıyaslama derin öğrenmeye hafifçe yatkın.
- **Bu projeyle ilgisi:** Üstünlük iddiası derin modeller içindir ve TabPFN'den önceye ait. Dikkat maliyeti öznitelik sayısıyla karesel arttığından, binlerce genle doğrudan kullanım zor olabilir.
- **Sınırlılık:** En küçük veri seti bile yirmi bin örneğin üzerinde, dolayısıyla p≫n ve küçük n değerlendirilmemiş; tek ayrım kullanılmış. Ek materyal elimizde yok.

### grinsztajn2022

- **Künye anahtarı:** `grinsztajn2022`
- **Erişim düzeyi:** tam metin (NeurIPS bildiri PDF, Ek A yok). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Tipik tablo verisinde ağaç tabanlı modeller derin öğrenmeden neden hâlâ üstün, bu farkı hangi tümevarımsal eğilimler açıklıyor?
- **Veri:** OpenML ağırlıklı 45 veri seti. Ölçütler: heterojen sütunlar, d/n oranı 1/10'un altında, d 500'ün altında, en az 3.000 örnek ve 4 öznitelik; eğitim kümesi 10.000 örnekte kesilmiş, sınıflar dengelenmiş, çok kolay veri setleri çıkarılmış.
- **Yöntem:** Random Forest, GBT ve XGBoost ile MLP, ResNet, FT-Transformer ve SAINT karşılaştırılmış; ardından veri dönüşümleriyle eğilimler incelenmiş.
- **Doğrulama protokolü:** Model ve veri seti başına yaklaşık 400 yinelemeli rastgele arama; en iyi model doğrulama kümesinde seçilip test kümesinde değerlendirilmiş, arama sırası 15 kez karıştırılmış; toplam skor normalize edilmiş.
- **Ana sonuç:** Orta boyutlu veride ağaçlar her arama bütçesinde üstün kalmış. Nedenler arasında sinir ağlarının düzensiz hedef fonksiyonlarında zorlanması, MLP türü ağların bilgi taşımayan özniteliklere duyarlılığı ve dönme değişmezliği var.
- **Bu projeyle ilgisi:** Sonuç p≫n mikrodizilere doğrudan taşınamaz, çünkü bu rejim dışlanmış ve Golub boyut ve örnek ölçütlerini sağlamaz. Bilgi taşımayan özniteliklere duyarlılık bulgusu MLP bonusu için ayrıca önemli.
- **Sınırlılık:** Küçük ve çok büyük veri setleri açıkça gelecek çalışmaya bırakılmış; sınıflandırma ikiliye indirilmiş ve doğrulukla ölçülmüş. Ek A elimizdeki metinde yok.

### hollmann2025

- **Künye anahtarı:** `hollmann2025`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC11711098). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Sentetik veri kümeleri üzerinde önceden eğitilmiş bir temel model, küçük ve orta boyutlu tablo verisinde ayarlanmış geleneksel yöntemleri geçebilir mi?
- **Veri:** Ön eğitim için yapısal nedensel modellerden üretilen yaklaşık 100 milyon sentetik veri seti. Değerlendirme AutoML Benchmark ve OpenML-CTR23'ten en çok 10.000 örnek, 500 öznitelik ve 10 sınıflı 29 sınıflandırma ile 28 regresyon veri seti; ek olarak Grinsztajn ve TabZilla kıyaslamaları ile beş Kaggle yarışması.
- **Yöntem:** Bağlam içi öğrenme yapan, satır ve sütun boyunca iki yönlü dikkat kullanan transformer; eğitim ve tahmin tek ileri geçişte yapılıyor. Rakipler Random Forest, XGBoost, CatBoost, LightGBM, doğrusal modeller, SVM, MLP ve AutoGluon.
- **Doğrulama protokolü:** Veri seti başına 10 tekrar, %90 eğitim ve %10 test; rakipler beş katlı çapraz doğrulamayla 30 saniyeden 4 saate kadar ayarlanmış; skorlar veri seti başına normalize edilmiş.
- **Ana sonuç:** Bu aralıkta TabPFN, 4 saat ayarlanmış ağaç yöntemlerini ve AutoGluon'u sınıflandırmada ortalama 2,8 saniyede geçmiş; yine de bazı veri setlerinde CatBoost önde. Daha büyük veri ve çok pürüzlü regresyonda ağaç yöntemleri ve AutoGluon'un önde olması bekleniyor.
- **Bu projeyle ilgisi:** 500 gen eşiği yazarların değerlendirdiği üst sınırla örtüşüyor. Metinde "v2" adı geçmiyor, gen ifadesi veya n≈72 için doğrudan kanıt da yok; genetik veri yalnızca gelecek çalışma olarak anılıyor.
- **Sınırlılık:** 10.000 örnek ve 500 öznitelik kesin yazılım sınırı değil, değerlendirme aralığı; yazarlar bunun ötesine ölçeklenme kanıtı sunmadıklarını belirtiyor. Ön eğitimde öznitelik sayısı en çok 160. FT-Transformer rakipler arasında yok, ek veri tablolarının içeriği elimizde değil. İki yazar PriorLabs ile bağlantılı.

### chen2025genept

- **Künye anahtarı:** `chen2025genept`
- **Erişim düzeyi:** tam metin (bioRxiv preprint PDF ve PMC10614824 preprint metni; Nature Biomedical Engineering sürümü okunmadı). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Gen ve hücre biyolojisi, ifade verisiyle ön eğitim yerine genlerin metin açıklamalarının dil modeli gömmeleriyle temsil edilebilir mi?
- **Veri:** NCBI Gene özetleri (yaklaşık 33.000 gen, ortalama 73 sözcük); gen düzeyi görevler için hazır kıyaslamalar, hücre düzeyi görevler için tek hücreli RNA-seq veri setleri (preprint sürüm 1'de dört, sürüm 2'de altı).
- **Yöntem:** Özetler GPT-3.5 olarak anılan text-embedding-ada-002 ile 1.536 boyutlu gen gömmelerine çevriliyor. GenePT-w hücreyi ifade ağırlıklı ortalama, GenePT-s ise ifadeye göre sıralı gen adlarından oluşan cümlenin gömmesi olarak temsil ediyor.
- **Doğrulama protokolü:** Gömmeler üzerinde lojistik regresyon, Random Forest ve k-NN; beş katlı çapraz doğrulama veya rastgele ayırma; kümelemede ARI ve AMI; Geneformer, scGPT ve Gene2vec ile karşılaştırma.
- **Ana sonuç:** Gen özelliklerinde ve etkileşim tahmininde güçlü; hücre düzeyinde Geneformer'la kıyaslanabilir veya daha iyi, scGPT ile benzer. Hasta kaynaklı toplu etki azalıyor.
- **Bu projeyle ilgisi:** Bulk mikrodizi veya lösemi sınıflandırması test edilmemiş; projedeki kullanım kaynağın kapsamı dışında bir uyarlamadır. Girdi örnek etiketi değil gen metni ve gen adlarıdır; olası sızıntı yolu özet metinlerdeki hastalık bilgisi olabilir.
- **Sınırlılık:** Bu not dergi sürümüne değil bioRxiv preprint'lerine dayanıyor (PDF sürüm 1, PMC sürüm 2), bu ikisi temel yöntemde örtüşüyor; sızıntı analizi, protein etkileşimi ve Llama-7B yalnızca sürüm 2'de. Yöntem belgelenmemiş işlevleri kaçırabilir ve doku bağlamını iyi yansıtmayabilir.

### alhenawi2022

- **Künye anahtarı:** `alhenawi2022`
- **Erişim düzeyi:** yalnızca özet (Europe PMC). Griffith deposunda indirilebilir metin dosyası bulunamadı.
- **Çalışmanın sorusu:** Son yedi yılda mikrodizi özellik seçiminde hangi araştırma yönleri öne çıkmıştır?
- **Veri:** Üç yayıncıdan 132 çalışma.
- **Yöntem:** Sistematik derleme; çalışmalar dokuz yöne ayrılır ve altı açıdan incelenir.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** En sık araştırma yönü hibrit özellik seçimi önermektir (%34,9); diğerleri %13,6 ile %3 arasındadır.
- **Bu projeyle ilgisi:** Rapordaki hibrit seçim cümlesinin tek dayanağı.
- **Sınırlılık:** %34,9 bir araştırma yönü payıdır; özet ne filtre-sarmalayıcı ayrıntısını ne de başarım üstünlüğünü gösterir.

### alharbi2023

- **Künye anahtarı:** `alharbi2023`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC9952758). Hedefli okuma: özet, giriş, özellik mühendisliği bölümleri, hibrit ve sonuç kısımları.
- **Çalışmanın sorusu:** Gen ifadesiyle kanser sınıflandırmada klasik ve derin öğrenme yöntemleri nasıl özetlenir?
- **Veri:** Mikrodizi ve RNA-seq çalışmaları; ağırlık RNA-seq'tedir.
- **Yöntem:** Anlatısal derleme: filtre, sarmalayıcı, gömülü ve hibrit özellik mühendisliği; MLP, CNN, RNN, GNN ve transformer.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** Hibrit yaklaşım yalnızca kısa bir alt başlıkta, birçok çalışmanın kullandığı bir seçenek olarak anılır; baskın olduğuna dair ifade bulunmadı. Metin, baskın veri biçimi olarak RNA-seq'ten söz eder.
- **Bu projeyle ilgisi:** Genel arka plan; "hibrit baskındır" savını desteklemez.
- **Sınırlılık:** Golub verisi veya bir nicel sayım içermez; tam metnin tamamı okunmadı.

### xie2022

- **Künye anahtarı:** `xie2022`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC9327232). Hedefli okuma: deneyler, tablolar, veri ve yöntem özeti.
- **Çalışmanın sorusu:** Gen ilişkisi bilgisini grafik sinir ağıyla kullanarak az sayıda biyobelirteç seçilebilir mi?
- **Veri:** DLBCL, Golub lösemi (72 örnek, 47/25, 7129 özellik), prostat, ALL_4; GeneMANIA.
- **Yöntem:** t testiyle 100 özellik, GNN ile bağlantı tahmini, kümeleme, sekiz değerlendirici ve sıra birleştirme; SVM sınıflandırıcı.
- **Doğrulama protokolü:** Seçilen nihai altkümede 10 katlı CV. Metin önce seçimi, sonra CV'yi anlatır; seçimin katlar içinde yinelendiği söylenmez ve küme sayısı CV sonuçlarıyla birlikte incelenir.
- **Ana sonuç:** Lösemide 2 özellikle doğruluk 0,971 (Tablo 3); Tablo 2'de tek özellikle aynı değer görünür.
- **Bu projeyle ilgisi:** Yeni yüksek sonuç örneği; anlatıma göre seçim CV dışında göründüğü için "unclear" notu yumuşak kalır.
- **Sınırlılık:** Güven aralığı yok, bağımsız test yok, sızıntı konusu tartışılmaz.

### rezaee2022

- **Künye anahtarı:** `rezaee2022`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC9290776). Hedefli okuma: gen seçimi, veri, ayar, sonuç tabloları ve sonuç.
- **Çalışmanın sorusu:** Yumuşak topluluk gen seçimi ve yığılmış derin ağ mikrodizi sınıflandırmasını iyileştirir mi?
- **Veri:** DLBCL, Golub lösemi (72 örnek, 47/25, 7129 gen), prostat; genellenebilirlik için SRBCT ve MS verileri.
- **Yöntem:** ROC, Wilcoxon ve SNR ile k-NN sarmalayıcıya dayalı topluluk seçim, yığılmış otokodlayıcı.
- **Doğrulama protokolü:** K katlı CV (K=5, 10, 15, 20) ve "training data" içinde 10 katlı ayrım anılır; seçimin dış test kıvrımını görüp görmediği açık değildir, gen sayısı sonuçlara bakılarak tartışılır.
- **Ana sonuç:** Lösemide ortalama doğruluk %99,6; bazı koşullarda 100 görünür.
- **Bu projeyle ilgisi:** Raporun "unclear" notu adildir.
- **Sınırlılık:** Bazı ayrıntılar tutarsızdır (örneğin prostat verisi için 125.333 gen yazılması); doğruluk için güven aralığı verilmez.

### awotunde2022

- **Künye anahtarı:** `awotunde2022`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC9785310). Hedefli okuma: veri, deney, sonuç ve tablolar.
- **Çalışmanın sorusu:** Hiperparametreleri optimize edilmiş CNN, IoMT ortamında lösemi tanısını iyileştirir mi?
- **Veri:** "UCI" diye anılan 72 örnek, 7129 gen, 25 AML ve 47 ALL. Ancak metin ve Tablo 4 ayrıca CML, CLL ve sağlıklı sınıflardan söz eder; Golub verisinde bunlar yoktur.
- **Yöntem:** PSO ile 2323 gen, HORD ile CNN hiperparametre ayarı.
- **Doğrulama protokolü:** Rastgele %70/30 ve %80/20 bölmeler, üç deneme; CV hiç geçmez. Hiperparametreler bu veri setinde en iyi sonuca göre seçilir; PSO'nun bölmeden önce mi sonra mı çalıştığı belirtilmez.
- **Ana sonuç:** Metinde %99,6 ve %99,9 değerleri birlikte geçer; karşılaştırma tablosunda %99,9.
- **Bu projeyle ilgisi:** "High" sızıntı notu adildir; ayrıca sonucun gerçekten Golub verisine ait olup olmadığı şüphelidir.
- **Sınırlılık:** Sınıf tanımı veriyle çelişir, güven aralığı yok, "36 attributes" ile 2323 gen anlatımı örtüşmez.

### selvaraj2024

- **Künye anahtarı:** `selvaraj2024`
- **Erişim düzeyi:** tam metin (Europe PMC XML, PMC11436508). Gövdenin tamamı okundu.
- **Çalışmanın sorusu:** Heterojen öğrenicilerden kurulan süper öğrenici lösemi tipini daha iyi sınıflandırır mı?
- **Veri:** 7129 gen içeren AML-ALL verisi ve çok sınıflı CuMiDa verisi. Çalışma kendi veri setinin örnek sayısını söylemez; 72 sayısı yalnızca başka bir çalışmanın özetinde geçer.
- **Yöntem:** RF ile entropi temelli önem skoru, FI 0,04 altı genler atılır; LR, SVM-RBF, k-NN, MLP, RF ve Bayes aday öğreniciler, RF üst öğrenici.
- **Doğrulama protokolü:** Önem skoru önce "veri seti" üzerinde hesaplanır, seçilen genler sonra %20 test payıyla tabakalı 10 katlı CV'ye girer; seçimin katlar içinde yinelendiği yazılmaz.
- **Ana sonuç:** AML-ALL doğruluğu 0,98, CuMiDa 0,97; AUC %95 ve %91.
- **Bu projeyle ilgisi:** "High (ranking before CV)" notu metnin anlatım sırasına dayanan adil bir okumadır.
- **Sınırlılık:** Güven aralığı yok; F1 değeri (0,92) kesinlik ve duyarlılıkla (0,97 ve 0,96) uyuşmaz. Yaklaşık 15 örnekli bir test kümesinde 0,98 tek bir ayrımdan çıkamaz (bu çıkarım bize aittir), raporlama belirsizdir.

### breiman2001

- **Künye anahtarı:** `breiman2001`
- **Erişim düzeyi:** tam metin (Breiman'ın Berkeley sayfasındaki yazar kopyası, Ocak 2001; sayfa numaraları dergiden farklı). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Rastgele özelliklerle büyütülen ağaç topluluklarının genelleme hatası neye bağlıdır ve doğruluğu Adaboost ile yarışabilir mi?
- **Veri:** Ağırlıklı olarak UCI'dan 13 küçük veri kümesi, 3 büyük küme, 4 sentetik küme ve 1000 girdili benzetim; mikrodizi verisi yoktur.
- **Yöntem:** Bagging ile düğümde rastgele girdi (Forest-RI) veya rastgele doğrusal birleşim (Forest-RC) seçen budanmamış ağaçlar; güç-korelasyon sınırı ve torba dışı tahminler.
- **Doğrulama protokolü:** Küçük kümelerde %10 test ayrılarak 100 tekrar, büyük kümelerde sabit test, ayrıca torba dışı hata ve permütasyonla değişken önemi.
- **Ana sonuç:** Ağaç sayısı arttıkça hata bir sınıra yakınsar; doğruluk Adaboost ile kıyaslanabilir, etiket gürültüsüne daha dayanıklıdır ve düğümdeki özellik sayısına duyarlılık düşüktür.
- **Bu projeyle ilgisi:** Rastgele orman kolunun ve torba dışı permütasyon öneminin birincil kaynağıdır; bu önem ilişkili değişkenler için temkinli okunmalıdır, çünkü yazar özdeş iki değişkenin ayrı ayrı önemli görünebileceğini örnekler.
- **Sınırlılık:** Çalışmada p çok büyük, n küçük bir gerçek veri yoktur; ölçek değişmezliği veya doğrusal olmama özelliği açıkça ileri sürülmez. Okunan metin Ocak 2001 tarihli yazar kopyasıdır, sayfa numaraları dergiden farklıdır.

### cortes1995

- **Künye anahtarı:** `cortes1995`
- **Erişim düzeyi:** tam metin (Springer ücretsiz PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Optimal ayırıcı hiperdüzlem fikri, hatasız ayrılamayan eğitim verisine ve yüksek boyutlu özellik uzaylarına nasıl genişletilir?
- **Veri:** Rakam tanıma: US Postal Service (7300 eğitim, 2000 test) ve NIST karışımı (60000 eğitim, 10000 test); mikrodizi verisi yoktur.
- **Yöntem:** Yumuşak marjlı destek vektör ağları; çekirdek ile yüksek boyutlu uzayda doğrusal karar yüzeyi, deneylerde polinom çekirdekler. Radyal taban fonksiyonu olanağı da anılır.
- **Doğrulama protokolü:** Sabit eğitim ve test kümeleri; sonuçlar yayımlanmış sınıflandırıcılarla ve OCR kıyas çalışmasıyla karşılaştırılır.
- **Ana sonuç:** Polinom derecesi arttığında başarım neredeyse değişmez; destek vektör sayısına dayalı sınır deneylerde tutar. NIST'te dördüncü derece polinomla %1,1 test hatası elde edilir.
- **Bu projeyle ilgisi:** Projedeki SVM yönteminin ve yumuşak marj parametresi C'nin özgün kaynağıdır.
- **Sınırlılık:** Örnek sayısı girdi boyutunu aşar; p>>n verisi veya gen ifadesi ele alınmaz, bu nedenle mikrodiziyle ilgili bir sav için kaynak olamaz. Metin OCR kaynaklı yazım hataları içerir.

### nadeau2003

- **Künye anahtarı:** `nadeau2003`
- **Erişim düzeyi:** tam metin (Springer ücretsiz PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Eğitim kümesi seçiminden gelen değişkenliği de hesaba katarak CV tipi genelleme hatası tahmininin varyansı nasıl tahmin edilir ve algoritmalar nasıl test edilir?
- **Veri:** Benzetim: Gauss regresyonu ve iki Gauss popülasyonu (n=200 ve 2000) ile Letter Recognition'dan 300 örneklik altkümeler; her senaryoda 1000 veri kümesi.
- **Yöntem:** Birbirinden bağımsız J rastgele eğitim/test bölmesi üzerine kuram; düzeltilmiş yeniden örnekleme t'si (varyans çarpanı 1/J + n2/n1, J-1 serbestlik derecesi) ve muhafazakâr Z önerilir.
- **Doğrulama protokolü:** Yedi çıkarım yöntemi gerçek boyut ve güç açısından karşılaştırılır; Dietterich 5×2 cv ve McNemar'a yakın t testi de dahildir.
- **Ana sonuç:** Yalnızca CV sonuçlarına dayanan genel bir yansız varyans tahmincisi yoktur; düzeltilmiş t, boyutu nominale yakın ve hesabı kolay bir seçenektir, ancak korelasyon varsayımı kaba olduğundan liberal de kalabilir. J için yaklaşık 15 önerilir.
- **Bu projeyle ilgisi:** 25 dış kat için güven aralığı ve ikili karşılaştırmanın en yakın dayanağıdır; 5 katlı CV'de n2/n1 yaklaşık 0,25 olduğundan düzeltme belirgindir.
- **Sınırlılık:** Test kümeleri örtüşebilen rastgele bölmeler incelenir; test kümeleri ayrık standart k katlı CV açıkça gelecek çalışmaya bırakılır, benzetimlerdeki örneklem 72'den büyüktür ve karşılaştırma iki algoritma içindir.

### demsar2006

- **Künye anahtarı:** `demsar2006`
- **Erişim düzeyi:** tam metin (JMLR PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Birden çok sınıflandırıcı birden çok veri kümesinde karşılaştırılırken hangi istatistiksel testler uygundur?
- **Veri:** 1999-2003 ICML makalelerinin taraması ve UCI'dan 40 gerçek veri kümesi; denemelerde onar veri kümesi rastgele seçilir.
- **Yöntem:** Eşli t, Wilcoxon, işaret testi, ANOVA, Friedman ve Nemenyi ile Holm gibi sonradan testlerin varsayımları kuramsal ve deneysel olarak incelenir; CD diyagramı önerilir.
- **Doğrulama protokolü:** Örneklem birimi veri kümesidir; yeniden örnekleme yalnızca her küme için tek bir başarım puanı üretmekte kullanılır. Değerlendirme, ret oranı ve tekrarlanabilirlik üzerindendir.
- **Ana sonuç:** Çoklu veri kümesi ortamında iki sınıflandırıcı için Wilcoxon, daha fazlası için Friedman ve sonradan testleri önerilir.
- **Bu projeyle ilgisi:** Yalnızca kohort düzeyinde kullanılabilir ve üç kohort çok azdır; yazar, örtüşen eğitim verisi nedeniyle tek kümedeki katların bağımsız gözlem sayılamayacağını ve bunu hesaba katan bir test bilmediğini belirtir.
- **Sınırlılık:** Tip I/II hata oranı ölçülmez; tek veri kümesi problemi kapsam dışıdır, McNemar yalnızca geçerken ve Dietterich'e atıfla anılır.

### benjamini1995

- **Künye anahtarı:** `benjamini1995`
- **Erişim düzeyi:** yalnızca künye. Bulunan tek açık kopya bir ders sayfasındaydı, yasal olduğu kesin olmadığından okunmadan silindi.
- **Çalışmanın sorusu:** Okunmadı.
- **Veri:** Okunmadı.
- **Yöntem:** Raporda yalnızca FDR düzeltmesi için atıf yapılır.
- **Doğrulama protokolü:** Okunmadı.
- **Ana sonuç:** Okunmadı.
- **Bu projeyle ilgisi:** Çoklu test düzeltmesinin standart atfı.
- **Sınırlılık:** Hiçbir içerik sav olarak kullanılmamalıdır.

### liu2006

- **Künye anahtarı:** `liu2006`
- **Erişim düzeyi:** yalnızca özet (Europe PMC). Dergi metni aboneliğe tabi.
- **Çalışmanın sorusu:** Hangi ifade algoritması doğru farkları az yanlış pozitifle yakalar ve tahlil değişimlerine dayanıklıdır?
- **Veri:** Affymetrix Latin kare verisi ve aynı kemik iliğiyle iki deney seti.
- **Yöntem:** PQN ve DQN: kuantil normalleştirmeli kırpılmış ortalamalar; RMA, GCRMA, dChip, PLIER ve MAS5 ile karşılaştırma.
- **Doğrulama protokolü:** Karşılaştırmalı değerlendirme; ayrıntı görülmedi.
- **Ana sonuç:** Özet, dizi tipi veya tahlil değişiminde prob seti düzeyinde kuantil normalleştirmenin gerekli olduğunu söyler.
- **Bu projeyle ilgisi:** GEO GSE13159 işleme notu ve Haferlach 2010 bu yöntemi MILE için bildirir.
- **Sınırlılık:** Özet düzeyinde.

### vandermaaten2008

- **Künye anahtarı:** `vandermaaten2008`
- **Erişim düzeyi:** tam metin (JMLR PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Yüksek boyutlu veriyi hem yerel yapıyı hem de kümelenmeleri koruyarak iki ya da üç boyutlu haritada nasıl gösterebiliriz?
- **Veri:** MNIST, Olivetti yüzleri, COIL-20, kelime özellikleri ve Netflix verisi.
- **Yöntem:** Simetrik SNE'nin düşük boyutta bir serbestlik dereceli Student-t dağılımı kullanan biçimi (t-SNE); karışıklık (perplexity) etkin komşu sayısı gibi yorumlanır, tipik değerleri 5 ile 50 arasındadır.
- **Doğrulama protokolü:** Sınıf etiketleri yalnızca renklendirmede kullanılır; haritalar Sammon, Isomap, LLE gibi yöntemlerle görsel olarak karşılaştırılır. Deneylerde önce PCA ile 30 boyuta inilir.
- **Ana sonuç:** t-SNE, karşılaştırılan yöntemlerden daha ayrışık haritalar üretir ve kalabalıklaşma sorununu hafifletir.
- **Bu projeyle ilgisi:** Keşifsel görselleştirme için uygun atıftır; perplexity 10 belirtilen aralıktadır.
- **Sınırlılık:** Maliyet fonksiyonu dışbükey değildir, sonuç başlangıca bağlı olabilir ve iç boyutu yüksek veri iki boyutta tam temsil edilemez; yöntem hipotez testi aracı olarak sunulmaz, gen ifadesi verisi de denenmez.

### pedregosa2011

- **Künye anahtarı:** `pedregosa2011`
- **Erişim düzeyi:** tam metin (JMLR PDF). Gövdenin tamamı okundu (okuyucu ajan).
- **Çalışmanın sorusu:** Python'da uzman olmayanların da kullanabileceği, tutarlı arayüzlü bir makine öğrenmesi kütüphanesi nasıl sunulur?
- **Veri:** Bilimsel bir veri analizi yoktur; süre karşılaştırmasında Madelon verisi (4400 örnek, 500 öznitelik) kullanılır.
- **Yöntem:** NumPy ve SciPy üzerine kurulu, LibSVM ve LibLinear'ı içeren ortak tahminci arayüzü; çapraz doğrulama yineleyicileri, GridSearchCV ve Pipeline nesneleri.
- **Doğrulama protokolü:** Birim testleri, kod kapsamı ve diğer Python araçlarıyla çalışma süresi karşılaştırması.
- **Ana sonuç:** Kütüphane BSD lisanslı, belgelenmiş ve kullanımı kolay bir araç sunar; hesaplama verimliliğine özen gösterildiği tablo ile desteklenir.
- **Bu projeyle ilgisi:** Raporda kullanılan yazılımın doğru atfıdır; Pipeline ve GridSearchCV, her katta yeniden uydurulan adımların teknik temelini oluşturur.
- **Sınırlılık:** Sınıflandırıcıların istatistiksel geçerliliğine dair kanıt taşımaz; 2011 sürümünü anlatır, güncel API ayrıntıları için kaynak değildir.

## 2026-11-06 eklenen kaynaklar

Bu notları bir yapay zekâ ajanı metinleri okuyarak çıkardı; merkez sayıların bir bölümü kaynak metinde örneklem olarak denetlendi. `patil2015` ve `zhou2025tabpfn` raporda yer almaz. Akciğer çalışmasındaki AUROC değeri özgün tablodan denetlendi.

### Sızıntı ve çapraz doğrulama (İddia 1)

### kapoor2023

- **Künye anahtarı:** `kapoor2023`
- **Hakemli mi:** evet (Patterns, Crossref journal-article).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, öne çıkanlar, sızıntı sınıflandırması, iç savaş bölümünün bir kısmı).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10499856/fullTextXML
- **Çalışmanın sorusu:** Makine öğrenmesi kullanan bilimlerde sızıntı ne kadar yaygın, hangi türleri var, nasıl önlenir?
- **Veri:** 17 alandan 22 derleme makalesinin taraması; bunlar toplam 294 makaleyi etkiliyor. Ayrıca iç savaş tahmini üzerine yeniden üretim çalışması.
- **Yöntem:** Önceki derlemelerin taranması, sekiz tipli sızıntı sınıflandırması, "model bilgi sayfası" önerisi.
- **Doğrulama protokolü:** İç savaş makalelerinin hatalar düzeltilerek yeniden çalıştırılması.
- **Ana sonuç:** 17 alanda en az 294 makale etkilenmiş (Özet, Şekil 1). L1.3 tipi, gen seçiminin tüm veri üzerinde yapılmasıdır (sınıflandırma bölümü). Hatalar düzeltilince karmaşık modeller lojistik regresyondan belirgin biçimde iyi çıkmıyor (Özet).
- **Bu projeyle ilgisi:** İddia 1 için hata türünü adlandırır: bizim "dışarıda seçim" kolumuz L1.3'tür. L3 tipi (test kümesi hedef dağılımdan gelmiyor) İddia 2 ile kavramsal olarak ilişkilidir ama sıralama/eşik ayrımı yapmaz.
- **Sınırlılık:** Sayı önceki derlemelere dayanır, sistematik yaygınlık tahmini değildir. Okunan kısımlarda gen ifadesine özgü bir ölçüm yok.

### whalen2022

- **Künye anahtarı:** `whalen2022`
- **Hakemli mi:** dergi derlemesi (Nature Reviews Genetics). Hakem süreci özetten doğrulanamadı.
- **Erişim düzeyi:** yalnızca özet. Tam metne yasal erişim bulunamadı.
- **Okunan URL:** Europe PMC özet kaydı (DOI araması), https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41576-021-00434-9%22&resultType=core
- **Çalışmanın sorusu:** Genomikte denetimli makine öğrenmesinin yaygın tuzakları nelerdir?
- **Veri:** Derleme; özette veri seti bilgisi yok.
- **Yöntem:** Özette ayrıntı yok.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** Özete göre modellerin ve performans değerlendirmelerinin varsayımları biyolojik sistemlerde sık sık tutmaz ve genomik verinin yapısı değerlendirmeyi yanlı kılabilir. Sayısal sonuç okunmadı.
- **Bu projeyle ilgisi:** Yalnızca genel arka plan (İddia 1). Belirli bir tuzak türü bu kaynağa bağlanmamalı, çünkü metin okunmadı.
- **Sınırlılık:** Özet düzeyi; ayrıntılı atıf yapılamaz.

### bernett2024

- **Künye anahtarı:** `bernett2024`
- **Hakemli mi:** dergi makalesi (Nature Methods). Makale türü ve hakem süreci özetten doğrulanamadı.
- **Erişim düzeyi:** yalnızca özet. Tam metne yasal erişim bulunamadı.
- **Okunan URL:** Europe PMC özet kaydı (DOI araması), https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1038/s41592-024-02362-y%22&resultType=core
- **Çalışmanın sorusu:** Biyolojik makine öğrenmesinde sızıntıyı önlemek için hangi sorular sorulmalı?
- **Veri:** Özette yalnızca örnekler üzerinde uygulandığı söylenir.
- **Yöntem:** Yedi yönlendirici soru.
- **Doğrulama protokolü:** Özette ayrıntı yok.
- **Ana sonuç:** Sızıntı, eğitim ve test verisi arasında bilgi paylaşımı olarak tanımlanır ve biyolojik verideki bağımlılıklar yüzünden fark edilmesi zordur (Özet). Soruların içeriği okunmadı.
- **Bu projeyle ilgisi:** İddia 1 için genel gerekçe.
- **Sınırlılık:** Yedi sorunun içeriğine atıf yapılamaz.

### rosenblatt2024

- **Künye anahtarı:** `rosenblatt2024`
- **Hakemli mi:** evet (Nature Communications).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, giriş, gen seçimi sızıntısı ve örneklem bölümleri, temel model yöntemi, sınırlılıklar).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10901797/fullTextXML
- **Çalışmanın sorusu:** Beş sızıntı türü, bağlantısal (connectome) tahmin modellerinin performansını ne kadar değiştirir?
- **Veri:** ABCD (N=7.822-7.969), HBN (N=1.024-1.201), HCPD (N=424-605), PNC (N=1.104-1.126); üç fenotip.
- **Yöntem:** Sırt (ridge) regresyonu, 400'den fazla işlem hattı. Altın standart modelde katlar içinde en anlamlı %5 özellik seçilir.
- **Doğrulama protokolü:** 5 katlı CV, 100 yineleme; hiperparametre için iç katlar. Ayrıca N=100, 200, 300, 400 yeniden örneklemeleri.
- **Ana sonuç:** HCPD'de özellik sızıntısı yaşta küçük (Δr=0,03), matris akıl yürütmede orta (Δr=0,17), dikkat sorunlarında en büyüktür (Δr=0,47). Dikkat sorunları r=0,01'den r=0,48'e çıkar (Bulgular, "Feature leakage"; Şekil 3). Örneklem küçüldükçe sızıntının etkisi daha değişken olur (Bulgular, "Effect of sample size"; Şekil 9).
- **Bu projeyle ilgisi:** İddia 1'in en güçlü güncel paraleli: etki, temel sinyal zayıfken en büyüktür. Bizim karıştırılmış etiket deneyimiz bunun uç hali sayılır. n=38 için küçük örneklem uyarısı da işimize yarar.
- **Sınırlılık:** Nörogörüntüleme ve sürekli fenotip regresyonudur; sınıflandırma ve gen ifadesi değildir. Yazarlar sızıntı türlerinin tamamını kapsayamadıklarını belirtir.

### demircioglu2021

- **Künye anahtarı:** `demircioglu2021`
- **Hakemli mi:** evet (Insights into Imaging).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, veri ve CV yöntemi, Bulgular, Tartışma).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8613324/fullTextXML
- **Çalışmanın sorusu:** Özellik seçimi CV'den önce yapılırsa yanlılık ne kadar büyür?
- **Veri:** PLOS One'dan 10 açık radyomik veri seti.
- **Yöntem:** 7 özellik seçme yöntemi (LASSO, t-skoru, f-skoru, MRMRe, ReliefF, MIM, SVM-RFE) ve çeşitli sınıflandırıcılar; 50.000'den fazla model.
- **Doğrulama protokolü:** Tabakalı 10 katlı CV; seçim CV öncesinde ve her katın içinde olmak üzere iki şema.
- **Ana sonuç:** Yanlılık AUC-ROC'ta en çok 0,149 (Hosny2018C), en az 0,02 (Song2020); AUC-F1'de 0,293'e, doğrulukta 0,17'ye kadar çıkar (Bulgular, Tablo 2; Özet). Özellik başına örnek azaldıkça yanlılık artar (R=-0,72, p=0,02; Şekil 3).
- **Bu projeyle ilgisi:** İddia 1'in farklı alanda doğrudan ölçümü. Bizim etkimiz daha büyüktür ama bizimki karıştırılmış etiketlerde, bu çalışmaki gerçek etiketlerde ölçülmüştür; sayılar doğrudan karşılaştırılmamalı.
- **Sınırlılık:** Yazara göre bağımsız doğrulama kümesi olmadığından yanlılığın gerçek boyutu belirlenemez. Normalleştirme ve eksik veri tamamlama CV dışında yapılmıştır.

### bates2024

- **Künye anahtarı:** `bates2024`
- **Hakemli mi:** evet (JASA). Okunan sürüm kabul edilmiş yazar el yazmasıdır.
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, giriş, Bölüm 1.1, Bölüm 4 başlangıcı).
- **Okunan URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11412612/
- **Çalışmanın sorusu:** CV tam olarak neyi tahmin eder ve güven aralıkları ne kadar güvenilirdir?
- **Veri:** Kuramsal sonuçlar ve benzetimler.
- **Yöntem:** Sıradan en küçük kareler için ispat; iç içe CV ile varyans tahmini.
- **Doğrulama protokolü:** Benzetimle kapsama oranı ölçümü.
- **Ana sonuç:** CV, eldeki modelin hatasını değil, aynı popülasyondan gelen başka eğitim kümeleriyle kurulan modellerin ortalama hatasını tahmin eder (Özet). n=90, p=1000 seyrek lojistik örnekte hedef %10 hatalı kapsama %31 çıkar ve aralıkların yaklaşık 1,6 kat genişlemesi gerekir (Bölüm 1.1).
- **Bu projeyle ilgisi:** Final aşamasındaki iç içe CV planının gerekçesi; İddia 1'in güven aralıkları için önemli, çünkü n=38 ve p büyük. Sızıntıyı değil, sızıntısız CV'nin aralığını ele alır.
- **Sınırlılık:** İspat doğrusal model içindir. Uygun aralığın sağlandığı "birçok örnekte" denir, her durumda değil.

### Platformlar arası taşınma ve eşik (İddia 2)

### zheng2026

- **Künye anahtarı:** `zheng2026`
- **Hakemli mi:** evet (PLOS One, Crossref journal-article). Yenilik değerlendirmesinin merkez kaynağı.
- **Erişim düzeyi:** tam metin (PMC13541173 XML). Gövdenin tamamı okundu. Ek dosya (S1 File) açılmadı.
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13541173/fullTextXML
- **Çalışmanın sorusu:** Transkriptom sınıflandırıcıda yüksek AUROC, kohort ve platform aktarımından sonraki sabit eşik başarısızlığını gizler mi? Ön işleme, sonradan kalibrasyondan daha mı önemlidir?
- **Veri:** Dört GEO tam kan kohortu. GSE65682 keşif (mikrodizi, ana analizde n=93), GSE95233 dış mikrodizi (n=73), GSE154918 RNA-seq (n=79; 39 pozitif, 40 negatif), GSE28750 zorlama kohortu (n=30; ikincil analizde n=21). Ana analizde 9.508 ortak gen.
- **Yöntem:** L2 lojistik regresyon (C=1, dengeli sınıf ağırlığı). Dört ön işleme: eğitimden standart ölçekleme, eğitimden dayanıklı ölçekleme, örnek içi yüzdelik sıra artı eğitimden ölçekleme, dış kohort istatistikleriyle dayanıklı ölçekleme. Sigmoid ve izotonik kalibrasyon.
- **Doğrulama protokolü:** Keşif kohortunda 5 katlı CV (imputasyon ve ölçekleme kat içinde). Sabit dış test, eşik 0,5 ve eğitimden türetilen eşik. 2.000 tabakalı bootstrap. Dış etiket hiçbir ayarda kullanılmamış.
- **Ana sonuç:** İç CV'de AUROC ve dengeli doğruluk 1,00. Eğitimden z-skorda üç dış kohortta dengeli doğruluk 0,50, buna karşılık AUROC 1,00 / 0,999 / 1,00; pozitif tahmin oranı 0,0 (Bulgular, "Diagnostic threshold instability"; Şekil 3). Eğitimden dayanıklı ölçekleme 0,57 / 0,50 / 0,55. Örnek içi sıra 1,00 / 0,974 / 0,95. Dış referanslı ölçekleme 0,961 / 0,949 / 1,00 (Bulgular, "Strict-inductive and adaptive strategies"). Sigmoid ve izotonik kalibrasyon başarısız iş akışlarını kurtarmamış. Zor karşılaştırmada (n=21) AUROC 0,873 ve 0,836 iken dengeli doğruluk 0,50; sıra 0,70 (GA 0,55-0,85), dış referanslı 0,805 (GA 0,614-0,950).
- **Bu projeyle ilgisi:** İddia 2'nin aynısı, başka hastalıkta. Yazarlar ayrıca dış kohort istatistiği kullanan ölçeklemeyi sabit aktarım değil, etiketsiz kohort uyarlaması sayar; bizim z-skor kolumuz bu sınıfa girer. Eşiğin platformdan mı, prevalanstan mı, vaka karışımından mı kaydığını ayıramadıklarını yazarlar açıkça söyler; bu bizim için boşluktur.
- **Sınırlılık:** Sınıflar kolay (sepsise karşı sağlıklı, iç AUROC 1,00). Eğitim n=93, zorlama kohortu küçük. Yalnızca lojistik regresyon; kalibrasyon ve eşik taramaları revizyonda eklenmiş tanı analizleridir. Süreç tek 0,5 eşiği üzerinden anlatılır, eğitimden türetilen eşik sonuçları ek tablolardadır ve okunmadı.

### lee2025

- **Künye anahtarı:** `lee2025`
- **Hakemli mi:** evet (npj Precision Oncology, 10(1):37; Crossref yayın tarihi 2025-12-20).
- **Erişim düzeyi:** tam metin (PMC12819530 XML). Gövdenin tamamı okundu, ek şekiller okunmadı.
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12819530/fullTextXML
- **Çalışmanın sorusu:** Pankreas kanseri alt tip sınıflandırıcısı PurIST, tüm transkriptom RNA-seq, ekzon yakalamalı RNA-seq ve NanoString arasında aynı kararı verir mi?
- **Veri:** Eşleştirilmiş 79 retrospektif örnek (tüm transkriptom ve ekzon yakalama), PANCREAS denemesinden 40 örnek (RNA-seq ve NanoString).
- **Yöntem:** Sekiz gen çiftine (TSP) dayalı tek örnek sınıflandırıcı; Cohen kappa, eşleştirilmiş Wilcoxon, Kaplan-Meier ve Cox.
- **Doğrulama protokolü:** Aynı örneklerde kafa kafaya karşılaştırma; referans tüm transkriptom RNA-seq.
- **Ana sonuç:** Uyum %81,0 (64/79), kappa 0,402. Bazal benzeri oranı %8,9'dan %27,8'e çıkar; 15 uyumsuz örneğin tamamı aynı yöne kayar. Olasılıklar ekzon yakalamada sistematik yüksektir (P=1,491e-13; Bulgular, Şekil 1). NanoString ile uyum %95 (38/40), kappa 0,722 (Şekil 4). Yazarlar seçenekler arasında başka bir olasılık eşiğini de sayar (Tartışma).
- **Bu projeyle ilgisi:** İddia 2'yi eşleştirilmiş örnekte destekler: olasılık ölçeği kayınca karar değişir. Daha önemlisi, sıra temelli gen çifti yöntemlerinin bile platforma bağışık olmadığını gösterir; genler arası göreli sıra platforma göre değişir. Bu, pilotumuzdaki sıra başarısızlığı için kaynaklı bir mekanizma adayıdır.
- **Sınırlılık:** AUC raporlanmaz, dolayısıyla "sıralama korundu" sonucu bu kaynaktan çıkarılamaz. Düşük bazal prevalans (%9), küçük örneklem. Yazarlardan ikisi PurIST patent sahibidir.

### kervanci2026

- **Künye anahtarı:** `kervanci2026`
- **Hakemli mi:** evet (Diagnostics, MDPI).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, veri, eşik yöntemi, dış doğrulama, Tablo 10-11).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13703602/fullTextXML
- **Çalışmanın sorusu:** Akciğer adenokarsinomunda sürücü mutasyon alt tipleri, mikrodizi ile eğitilip RNA-seq'e aktarılan bir modelle üç sınıflı olarak tahmin edilebilir mi?
- **Veri:** Mikrodizi iç kohort n=774 (GSE31210, GSE13213, GSE72094), dış RNA-seq TCGA-LUAD n=508.
- **Yöntem:** Referans partili ComBat, SHAP ile 500 gen, beş öğrenicili topluluk, sınıf bazlı olasılık eşiği (eşikler iç doğrulama alt kümesinde).
- **Doğrulama protokolü:** 5 katlı CV, dış test, tek kohort dışarıda bırakma, eşik seçiminin beş bölmede tekrarı.
- **Ana sonuç:** ComBat olmadan model tek sınıfa çöker: F1-makro 0,245, MCC 0,000, AUROC 0,580. ComBat ile F1 0,673, AUROC 0,850; eşik ayarı F1'i 0,700'e çıkarır (Tablo 11). KRAS eşiği 0,15 beş bölme aralığının (0,33-0,50) dışındadır; yazarlar temsilî değeri 0,66-0,68 olarak verir (Tablo 10, Özet).
- **Bu projeyle ilgisi:** İddia 2'yi yalnızca kısmen destekler. Olasılık dağılımında sistematik kayma bildirilir, ama harmonizasyonsuz durumda AUROC da çöker; yani burada sıralama taşınmaz. Bu, İddia 2'nin evrensel olmadığının kanıtıdır. Eşik kararsızlığı için ayrıca yararlıdır.
- **Sınırlılık:** İç CV'de ComBat ve seçim bölmeden önce kestirilmiş (yazarlar tek katta ΔF1=-0,019 ölçer). Üç sınıflı görev.

### botan2026

- **Künye anahtarı:** `botan2026`
- **Hakemli mi:** evet (Breast Cancer Research).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, skorlama yöntemi, sabit z-skor ve kalibrasyon bölümleri).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13474601/fullTextXML
- **Çalışmanın sorusu:** PAM50'den daha az genle prognostik performans korunabilir mi ve bu skor platformlar arasında geçerli midir?
- **Veri:** SCAN-B (N=3.069, RNA-seq), TCGA-BRCA (N=1.072), METABRIC (N=1.978), GSE20685 (N=327), GSE1456 (N=159).
- **Yöntem:** Cox elastik ağ, ön tanımlı eşdeğerlik sınırı (ΔC=0,010). Ana skorlama kohort içi z-skorudur; duyarlılık analizinde eğitim ortalaması ve standart sapması donduruluyor.
- **Doğrulama protokolü:** Dört dış kohort, rastgele etkili meta-analiz, lojistik yeniden kalibrasyon.
- **Ana sonuç:** 24 gen, katlar dışı C-indeksi 0,670. Havuzlanmış HR 1,37 (GA 1,24-1,52) (Özet). Dondurulmuş z-skorda C değişimi TCGA'da +0,0002, METABRIC'te +0,0007, GSE20685'te -0,036, GSE1456'da -0,040. Kalibrasyon eğimi eğitimde 0,96, dışta 1,57-2,74 (Bulgular, Tartışma).
- **Bu projeyle ilgisi:** İddia 2'yi dolaylı destekler: ayrım büyük ölçüde korunurken kalibrasyon bozulur. Ayrıca kohort içi z-skorun tek hasta skorlamasını karşılamadığını gösterir; bizim z-skor kolumuz için aynı uyarı geçerlidir.
- **Sınırlılık:** Sağkalım görevi, sınıflandırma eşiği değil. TCGA eğimi kısa izlem ve düşük olay oranıyla da ilişkilendirilir, yani yalnızca platforma bağlanamaz.

### kolev2026

- **Künye anahtarı:** `kolev2026`
- **Hakemli mi:** evet (International Journal of Molecular Sciences, MDPI).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, klinik kullanışlılık bölümü, sınırlılıklar, yöntemin eşik kısmı).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13704978/fullTextXML
- **Çalışmanın sorusu:** Sepsis gen imzası şanstan ve rastgele gen listelerinden daha iyi midir?
- **Veri:** GSE65682 (n=359), GSE57065 (n=53; 28 sepsis, 25 sağlıklı); 9.983 ortak gen.
- **Yöntem:** İç içe CV ile 10 gen, L1 lojistik; 1.000 etiket karıştırma, 2.000 rastgele panel, 200 bootstrap.
- **Doğrulama protokolü:** Yeniden uydurmadan dış uygulama; enfekte olmayan yoğun bakım hastaları için çapraz uydurma.
- **Ana sonuç:** Dış AUROC 1,000, karıştırma p=0,001. Rastgele panellerin %12,5'i imzayı yakalar. Enfekte olmayan yoğun bakım karşılaştırmasında AUROC 0,730 (GA 0,642-0,818), 0,5 eşiğinde 75 hastanın 70'i sepsis denir, dengeli doğruluk 0,527, kalibrasyon kesişimi -0,689, eğimi 0,240 (Özet; klinik kullanışlılık bölümü, Tablo 3).
- **Bu projeyle ilgisi:** İddia 1 için etiket karıştırma kontrolünün çağdaş örneği. İddia 2 için aynı platformda karşılaştırma grubu değişince çalışma noktasının anlamını yitirdiğini gösterir.
- **Sınırlılık:** Her iki kohort da mikrodizi. Özgüllük sonucu dış kohortta doğrulanmamış (yazarlar söyler). AUROC da düşmüştür, dolayısıyla "sıralama korundu" örneği değildir.

### foltz2023

- **Künye anahtarı:** `foltz2023`
- **Hakemli mi:** evet (Communications Biology).
- **Erişim düzeyi:** tam metin, hedefli okuma (giriş, Bulgular, Tartışma, veri ve sınıflandırma yöntemi). Sayısal Kappa değerleri şekillerde ve ek veridedir, okunmadı.
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9968332/fullTextXML
- **Çalışmanın sorusu:** Mikrodizi ve RNA-seq verisini birlikte eğitmek için hangi normalleştirme uygundur?
- **Veri:** TCGA, aynı tümörlerin iki platformdaki ölçümleri: BRCA 520, GBM 150 eşleşmiş örnek. Eğitim kümeleri 348 ve 102.
- **Yöntem:** LOG, NPN, QN, QN (CN), QN-Z, TDM, z-skor ve dönüşümsüz veri; LASSO, doğrusal SVM, rastgele orman. RNA-seq oranı %0'dan %100'e kademeli artırılır.
- **Doğrulama protokolü:** Eğitimde 5 katlı CV, tek platformlu ayrı test kümeleri, on tekrar. Ana ölçüt Kappa.
- **Ana sonuç:** QN, TDM ve NPN, RNA-seq oranı orta düzeydeyken iyi çalışır. QN uç oranlarda (%0, %100) referans dağılım olmadığı için kötüleşir. Z-skor en değişken yöntemdir; dönüşümsüz veri her düzeyde kötüdür (Bulgular, Şekil 2).
- **Bu projeyle ilgisi:** İddia 2 için dolaylı: eğitimi tek platformdan, testi diğerinden alan uç durumun zor olduğunu ve z-skorun değişkenliğini destekler. Yazarlar metrikler arası sonuçların benzer olduğunu söyler; bu, metrikler arası ayrışmanın her düzende beklenmemesi gerektiğini gösterir.
- **Sınırlılık:** İki TCGA veri seti. Eşik veya kalibrasyon incelenmez. Etiketler mikrodizi verisinden türetilmiştir. Yazarlar doğrusal olmayan modellere ve küçük örneklemlere genellemeyi sınırlar.

### patil2015

- **Künye anahtarı:** `patil2015`
- **Hakemli mi:** evet (Bioinformatics). Beş yıl dışında; yalnızca yenilik değerlendirmesi için.
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, giriş, tahmin bölümü, sonuç).
- **Okunan URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4495301/
- **Çalışmanın sorusu:** Test verisinin başka hastalarla birlikte normalleştirilmesi tek hastanın tahminini değiştirir mi?
- **Veri:** Küratörlü açık meme kanseri mikrodizi kümeleri (örnek: GSE7390, n=198).
- **Yöntem:** PAM50 ve sıra temelli sürümü; alt kümelerle yeniden normalleştirme.
- **Doğrulama protokolü:** Aynı hastanın farklı grup büyüklükleri ve ER bileşimleriyle normalleştirilip tahminlerin karşılaştırılması.
- **Ana sonuç:** Küçük gruplarda normalleştirilince aynı hastanın tahmini değişir; sonuç ER bileşimine de bağlıdır (Şekil 2). Sıra temelli özellikler bu yanlılığı önler ve platformlar arasında doğru sınıflamayı korur (Özet).
- **Bu projeyle ilgisi:** Kohort içi z-skor kolumuzun sınıf bileşimine duyarlı olması beklenir. Bu, İddia 2'nin raporlanan 0,59-0,94 aralığı için doğrudan bir tehdittir ve bir deneyle ölçülmelidir.
- **Sınırlılık:** Eski kaynak. Sıra yönteminin platformlar arası iyi çalıştığı sonucu pilotumuzla ve `lee2025` ile çelişir; tek başına genellenmemeli.

### Kalibrasyon ve dış doğrulama çerçevesi (İddia 2)

### vancalster2023

- **Künye anahtarı:** `vancalster2023`
- **Hakemli mi:** dergi makalesi (BMC Medicine; görüş niteliğinde metodolojik metin). Hakem bilgisi okunan metinde görülmedi.
- **Erişim düzeyi:** tam metin (PMC9951847 XML). Gövdenin tamamı okundu.
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9951847/fullTextXML
- **Çalışmanın sorusu:** İç veya tek dış doğrulama, bir modelin geçerli olduğunu söylemeye yeter mi?
- **Veri:** Özgün veri yok; yayınlardan örnekler ve bir over kanseri veri seti.
- **Yöntem:** Üç gerekçeli kavramsal tartışma: popülasyon, ölçüm ve zaman değişir.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** Yazarlara göre kalibrasyon coğrafi ve zamansal heterojenliğe ayrımdan genellikle daha açıktır (Sonuçlar). Wang COVID modeli: havuzlanmış c 0,77, O:E 0,65, eğim 0,50. EuroSCORE: c 0,79-0,85 arasında sistematik bozulma yokken gözlenen ölüm %4,1'den %2,8'e düşer, ortalama tahmin %5,6'dan %7,6'ya çıkar (Neden 1 ve 3 örnekleri). Ölçüm farkı (ör. kit ve cihaz) özellikle kalibrasyonu etkileyebilir (Neden 2). Kabaca en küçük sınıfta 100-200 vaka önerilir (Sonuçlar).
- **Bu projeyle ilgisi:** İddia 2'nin klinik tahmin alanındaki kuramsal dayanağı: ayrım-kalibrasyon ayrışması alanın bildiği bir olgudur. Ayrıca Golub'un 38 örneği bu ölçütün çok altındadır; test kohortu Golub olan satırlar zayıf okunmalıdır.
- **Sınırlılık:** Örnekler klinik değişkenlerdir, gen ifadesi değildir. Görüş makalesi.

### collins2024part1

- **Künye anahtarı:** `collins2024part1`
- **Hakemli mi:** evet (BMJ; metinde dış hakem değerlendirmesinden geçtiği belirtilir).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, sözlük kutuları, kalibrasyon ve güncelleme geçen bölümler).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10772854/fullTextXML
- **Çalışmanın sorusu:** Klinik tahmin modeli nasıl anlamlı biçimde değerlendirilir?
- **Veri:** Yok (yöntem rehberi).
- **Yöntem:** İç, iç-dış ve dış doğrulama ile heterojenlik ve genellenebilirlik anlatımı.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** Ayrım c istatistiğiyle ölçülür; kalibrasyon grafik, eğim (ideal 1) ve kalibrasyon-büyük-ölçek (ideal 0) ile değerlendirilir (sözlük). Değerlendirme sonucunda modelin güncellenmesi, ör. yeniden kalibrasyon, gerekebilir (Giriş).
- **Bu projeyle ilgisi:** İddia 2'de "kalibrasyon" sözcüğünü kullanacaksak ölçmemiz gerekenleri tanımlar. Bizim pilotta bunlar yok.
- **Sınırlılık:** Genel rehber, gen ifadesine özgü değil.

### riley2024part2

- **Künye anahtarı:** `riley2024part2`
- **Hakemli mi:** dergi makalesi (BMJ). Hakem ifadesi okunan metinde görülmedi. Bu kaynak aday listesinde yoktu, `collins2024part1` ile birlikte bulundu.
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, kalibrasyon ve ayrım bölümleri, Tablo 1).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10788734/fullTextXML
- **Çalışmanın sorusu:** Dış doğrulama çalışması nasıl yürütülür?
- **Veri:** İkili ve sağkalım sonlanımlı iki örnek model.
- **Yöntem:** Beş adım: veri, tahmin, performans, klinik kullanışlılık, raporlama.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** Tek ölçüt yetmez: ikili örnekte O/E 1,01 ama eğim 0,72 (0,70-0,75); sağkalım örneğinde eğim 1,10 ama O/E 1,27 (1,22-1,32) (Tablo 1 ve ilgili metin). c istatistiği vaka karışımına bağlıdır. Eşik önemliyse klinik yarar o eşikte değerlendirilmelidir.
- **Bu projeyle ilgisi:** Doğrudan yöntem kılavuzu: AUC ve 0,5 eşiğindeki dengeli doğruluğa eğim, kesişim ve O/E eklenmeli. AUC'nin vaka karışımına bağımlılığı, kohortlar arası AUC karşılaştırmasını da sınırlar.
- **Sınırlılık:** Genel rehber.

### collins2024tripod

- **Künye anahtarı:** `collins2024tripod`
- **Hakemli mi:** evet (BMJ, raporlama kılavuzu; metinde dış hakem değerlendirmesinden geçtiği belirtilir). `10.1136/bmj.q902` makale değil, bu kaydın düzeltme bildirimidir; atıf e078378'e yapılmalı.
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, tanımlar, kontrol listesi öğeleri).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11019967/fullTextXML
- **Çalışmanın sorusu:** Regresyon veya makine öğrenmesi kullanan klinik tahmin modelleri nasıl raporlanmalı?
- **Veri:** Yok (uzlaşı süreci).
- **Yöntem:** Uzlaşı temelli kılavuz güncellemesi.
- **Doğrulama protokolü:** Uygulanmaz.
- **Ana sonuç:** 27 maddelik liste ve 13 maddelik özet listesi; TRIPOD 2015'in yerini alır (Özet ve bulgular). Öğe 12e değerlendirme ölçütlerini, 12f güncellemeyi, 15 sınıflandırma eşiğinin nasıl belirlendiğinin gerekçesini ister.
- **Bu projeyle ilgisi:** Final makalesinin yöntem bölümünde eşiğin nereden geldiğini yazma gerekçesi.
- **Sınırlılık:** Raporlama kılavuzudur; bir bulgu kanıtı değildir.

### Lösemi transkriptom sınıflandırma

### mulet2025

- **Künye anahtarı:** `mulet2025`
- **Hakemli mi:** evet (HemaSphere).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, tahmin yöntemi, sınıflandırıcı ve dış kohort bölümleri).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12362175/fullTextXML
- **Çalışmanın sorusu:** Transkriptom, belirsiz soylu akut lösemileri AML, B-ALL veya T-ALL'a atamaya yardım eder mi?
- **Veri:** Eğitim için AML n=145, B-ALL n=223, T-ALL n=85 (RNA-seq). Belirsiz soylu lösemi n=30, dış belirsiz kohort n=24. Munich Leukemia Laboratory dış verisi (büyüklüğü ana metinde okunmadı).
- **Yöntem:** log TPM, en değişken 8.000 gen; altı algoritma karşılaştırılıp lasso çok terimli lojistik (E-CAL) seçilir. Soy kararı olasılık farkı 0,25'e dayanır.
- **Doğrulama protokolü:** İç içe CV (5 iç, 10 dış), Munich dış testi, MDACC belirsiz kohortu.
- **Ana sonuç:** İç içe CV'de %100 kesinlik ve duyarlılık, dış veride %97,5 duyarlılık ve %93,7 kesinlik (Bulgular). Belirsiz lösemilerin 27/30'u soya atanır; dış kohortta %75 uyum (Özet).
- **Bu projeyle ilgisi:** ALL/AML ayrımının en yakın güncel örneği: RNA-seq içinde ALL ile AML ayrımı dış veride de yüksektir. Bu, eşik sorununun görevin kendisinden değil, platform farkından kaynaklandığı fikrini güçlendirir (dolaylı çıkarım).
- **Sınırlılık:** Tek platform (RNA-seq). Eşik ve kalibrasyon değerlendirilmez. En değişken gen seçiminin kat içinde mi yapıldığı okunan kısımda görülmedi. Dış metrikler ek tablodadır.

### cui2026

- **Künye anahtarı:** `cui2026`
- **Hakemli mi:** evet (npj Precision Oncology).
- **Erişim düzeyi:** tam metin (PMC13594159 XML). Ana metnin tamamı okundu, ek veri okunmadı.
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13594159/fullTextXML
- **Çalışmanın sorusu:** Sıra dönüşümlü derin öğrenme, akut lösemi soyu ve 20 B-ALL alt tipini platformlar arasında sınıflayabilir mi?
- **Veri:** St. Jude Cloud n=1.606 (284 AML, 1.223 B-ALL, 99 T-ALL); SCMC n=1.144 (1.009 B-ALL, 135 T-ALL); Bld.2020 n=138 (115 B-ALL, 23 T-ALL); tek hücre RNA-seq.
- **Yöntem:** Örnek içi sıra dönüşümü, 476 gen, gürültü ile sıra artırımı, LSTM. AL modeli (229 gen) soy ayrımı yapar.
- **Doğrulama protokolü:** %80/%20 geliştirme ve görülmemiş kohortlar. Gen silme deneyleri.
- **Ana sonuç:** AL modeli görülmemiş SCMC'de %99,38 (Allspice %94,20), Bld.2020'de %98,56; B-ALL modeli St. Jude'da %93,84, Bld.2020'de %93,04 (Bulgular, Şekil 2). AL modelinde 229 genin 50'si silinince doğruluk %98'in üzerinde kalır (Şekil 2E).
- **Bu projeyle ilgisi:** Sıra dönüşümünün lösemide işe yaradığı en güncel iddia. Ancak **AL modelinin iki dış kohortunda AML yoktur**; metindeki kohort bileşimlerine göre AML ayrımı dışarıda test edilmemiştir. Bu nedenle bu kaynak, sıra dönüşümünün AML/ALL'da platform aşırı çalıştığının kanıtı olarak kullanılmamalı.
- **Sınırlılık:** Tümü RNA-seq; "platform" burada büyük ölçüde kuantifikasyon ve hizalama hattıdır, mikrodizi denenmez. Eşik ve kalibrasyon yok. Gen seçiminin bir kısmı literatür ve elle düzenleme içerir.

### beder2023

- **Künye anahtarı:** `beder2023`
- **Hakemli mi:** evet (HemaSphere).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, veri, sınıflandırıcı, doğruluk bölümleri).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10461941/fullTextXML
- **Çalışmanın sorusu:** RNA-seq gen ifadesi B-öncül ALL'yi 21 moleküler alt tipe ayırabilir mi?
- **Veri:** 3.532 örnekten eleme sonrası 2.998; eğitim n=1.869 (4 kohort), üç dışarıda tutulan çalışma n=1.129 (atanmış alt tipli n=1.018).
- **Yöntem:** LASSO ile gen seçimi, doğrusal SVM ve en yakın komşu birleşimi; log, z-dönüşüm ve 0-1 ölçekleme. Alt tipe özgü eşikler.
- **Doğrulama protokolü:** Tabakalı 10 katlı CV ve kohort düzeyinde dışarıda tutma.
- **Ana sonuç:** Doğruluk eğitimde 0,952, dışarıda tutulanlarda 0,957; St Jude 0,978, CLIP 0,965, MLL 0,914 (Bulgular, Şekil 3). Yüksek güvenli tahmin %83,7, doğruluğu %98,9; sınıflanamayan %1,2 (Özet).
- **Bu projeyle ilgisi:** Karşı örnek olarak değerlidir: aynı teknoloji içinde kohort değişince tanımlı eşiklerle doğruluk yüksek kalıyor. Bu, İddia 2'yi "kohort" değil "platform" üzerinden kurmayı destekler (bizim yorumumuz).
- **Sınırlılık:** ALL/AML değil, alt tip görevi; yalnızca RNA-seq. Eşiklerin hangi veriden tanımlandığı ek tablolarla netleşir, okunmadı.

### jung2026

- **Künye anahtarı:** `jung2026`
- **Hakemli mi:** evet (NAR Genomics and Bioinformatics).
- **Erişim düzeyi:** tam metin, hedefli okuma (özet, veri birleştirme, model ve TCGA doğrulama bölümleri, kalibrasyon geçen kısımlar).
- **Okunan URL:** https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13244157/fullTextXML
- **Çalışmanın sorusu:** AML'de IDH mutasyon durumu gen ifadesinden tahmin edilebilir mi?
- **Veri:** 19 kohort, 5.844 örnek; 1.546 etiketli eğitim örneği (285 mutant, 1.261 yabanıl tip); TCGA-LAML n=150 (29 mutant, 121 yabanıl tip).
- **Yöntem:** pyComBat ile toplu düzeltme; ileri beslemeli ağ ve lojistik regresyon.
- **Doğrulama protokolü:** İç içe CV ve TCGA-LAML bağımsız test.
- **Ana sonuç:** Lojistik regresyon için AUC 0,994±0,007, doğruluk 0,983±0,006, dengeli doğruluk 0,979±0,005 (Özet). TCGA'da 29/29 mutant ve 119/121 yabanıl tip doğru (Bulgular, Şekil 4). Brier 0,015 olmasına rağmen yüksek olasılıklarda sistematik fazla tahmin vardır; yazarlar olasılıkların olabilirlik gibi okunmamasını ister.
- **Bu projeyle ilgisi:** AML transkriptom verisinde ayrım ile kalibrasyonun ayrışabildiğini gösterir, ama bu iç CV'de görülür, platform aktarımında değil. ComBat ile hizalanmış veride karar iyi çalışır; bu, hizalamanın eşik sorununu çözebileceğine işaret edebilir (bizim yorumumuz).
- **Sınırlılık:** Metne göre 19 küme birlikte düzeltilmiştir; TCGA-LAML de buna dahilse dış test etiketsiz biçimde de olsa harmonizasyonu görmüştür. Bu ayrıntı açıkça doğrulanamadı. Görev ALL/AML değil.

### TabPFN ve gen ifadesi

### zhou2025tabpfn

- **Künye anahtarı:** `zhou2025tabpfn`
- **Hakemli mi:** **hayır, bioRxiv preprint** (v1, 2025-08-21; Crossref türü posted-content). Dergi sürümü bulunamadı. Proje rehberindeki bioRxiv 2025 atfıyla konu ve yıl olarak örtüşüyor; rehber künye vermediği için kesin eşleşme doğrulanamaz.
- **Erişim düzeyi:** tam metin (bioRxiv JATS XML, CC BY-NC). Gövdenin tamamı okundu. Tablo görselleri XML'de yoktu; sayılar metinden alındı.
- **Okunan URL:** https://www.biorxiv.org/content/early/2025/08/21/2025.08.15.670537.source.xml
- **Çalışmanın sorusu:** TabPFN, yüksek boyutlu RNA-seq verisine uyarlanabilir mi?
- **Veri:** Age-ARCHS4 (57.873 örnek, 10.000 gen; regresyon) ve IBD (2.490 örnek, 10.000 gen; üç sınıf).
- **Yöntem:** Özdenetimli gömmeler, BulkFormer, topluluklar, TabICL, TabFlex ve üstveri ile alt gruplama. Karşılaştırma: rastgele orman, XGBoost, MLP.
- **Doğrulama protokolü:** 5 katlı tabakalı CV.
- **Ana sonuç:** 500 özellik ve eşit koşulda TabPFN R²=0,606, rastgele orman 0,541, XGBoost 0,528. Klasik yöntemler tüm genleri kullanınca 3 katmanlı MLP R²=0,75; TabPFN uyarlamaları 0,4606-0,627. IBD'de TabPFN %63,7, TabICL %57,8, TabFlex %51,5, klasik yöntemler 0,74 dengeli doğruluk. Organ ve cinsiyetle alt gruplama R²=0,75 (Bulgular).
- **Bu projeyle ilgisi:** İki iddiayı doğrudan etkilemez. Golub'daki gen sayısı için TabPFN denenirse özellik sınırının gen seçimini zorunlu kıldığını ve bu seçimin CV içinde yapılması gerektiğini hatırlatır (bu ikinci kısım bizim çıkarımımız).
- **Sınırlılık:** Hakem görmemiş. Görevler lösemi değil. Yazar kurumu şirkettir (Biostate AI). Preprint TabPFN için Hollmann 2023'ü gösterir; rehber TabPFN v2 der. 500 özellik sınırının projede kullanılacak sürüm için geçerli olup olmadığı `hollmann2025` notundan ayrıca kontrol edilmeli.

## 4. Warnat-Herresthal 2020: GSE13159 dahil mi?

**Yanıt: evet.** Kaynak: Europe PMC ek dosya paketi (`PMC6992905/supplementaryFiles`), `mmc2.xlsx` (Tablo S1), `mmc1.pdf` (Transparent Methods), `mmc3.xlsx` (Tablo S3).

- `Annotation` sayfasında GSE13159 veri seti 2'de **1.860 örnekle** yer alır ve veri setinin (n=8.348) en büyük çalışmasıdır. `Study Search Dataset 2` sayfası da GSE13159 için OK verir.
- Dağılım: AML 538, ALL 520, KLL 448, MDS 204, KML 76, sağlıklı 74.
- **Fark:** Projede GSE13159'da 1.292 örnek (750 ALL, 542 AML) var; Warnat ALL'yi 520, AML'yi 538 sayar. Yani yaklaşık 230 ALL örneği Warnat'ta yok. Nedeni okunan dosyalarda görülmedi.
- GSE7186 dizgesi Tablo S1'in hiçbir sayfasında yok. GSE13164 ve GSE13204 de `Annotation` sayfasında görülmedi.

İddia 2 için bu kaynak sanılandan önemlidir:

- Ana metne göre HG-U133A ile eğitilen modeller RNA-seq verisinde tahmin yapamaz, sıra dönüşümüyle bu çözülür ve ntrain arttıkça sonuç kötüleşir (Translation of Classifiers across Technical Platforms, Şekil 5).
- Tablo S3'te veri seti 1'den 3'e, ntrain=2.500: ham doğruluk %45,3, sıra dönüşümlü %95,43.
- **Uyarı 1:** Ham satırdaki değerler kendi içinde tutarsız görünüyor. Duyarlılık 44,01, özgüllük 96,55 ve veri seti 3'ün 508 AML / 673 kontrol dağılımıyla doğruluk yaklaşık %74 olmalıydı, %45,3 değil. Ayrıca veri seti 2'den 3'e ham ve sıra satırlarının ortalamaları birebir aynı. Tablo S3'ün ham sayılarına dayanılmamalı; yalnızca ana metindeki nitel ifade kullanılmalı.
- **Uyarı 2:** Warnat'ın sıra dönüşümü **gen bazlı ve veri seti içindedir**: her gen tüm örnekler üzerinde sıralanıp normal dağılıma çevrilir (Transparent Methods, "Rank transformation to normality"). Bu, örnek içi sıra değildir; test kohortunun dağılımını kullanır ve bizim kohort içi z-skor kolumuzun yakın akrabasıdır. Dolayısıyla Warnat'ın bulgusu bizim z-skor sonucumuzla uyumlu, sıra sonucumuzla çelişmez.
- **AUC yoktur.** Tablo S3'te yalnızca doğruluk, duyarlılık, özgüllük var; "sıralama korunurken eşik bozuldu" sonucu bu kaynaktan çıkarılamaz.

## 5. Yenilik değerlendirmesi: İddia 2 ne kadar yeni?

**Soru:** Gen ifadesi sınıflandırıcılarında AUC'nin platformlar arasında taşındığını, karar eşiğinin veya kalibrasyonun taşınmadığını daha önce gösteren oldu mu?

**Yanıt: Evet, genel haliyle gösterildi.** `zheng2026` bunu ana bulgu olarak verir: "High AUROC can mask fixed-threshold failure" (Zheng ve Chen 2026, Özet). Mikrodizi ile eğitilen model RNA-seq kohortunda AUROC 0,999 iken 0,5 eşiğinde dengeli doğruluk 0,50 verir. Bu, bizim sonucumuzun neredeyse birebir karşılığıdır.

| Kaynak | Alan | Platform değişiyor mu? | Sıralama korunuyor mu? | Eşik veya kalibrasyon bozuluyor mu? | İddia 2 ile ilişkisi |
|---|---|---|---|---|---|
| `zheng2026` | Sepsis | evet (mikrodizi, RNA-seq) | evet, AUROC 0,999-1,00 | evet, dengeli doğruluk 0,50 | Doğrudan aynı bulgu |
| `botan2026` | Meme kanseri, sağkalım | evet | büyük ölçüde (dondurulmuş ve kohort içi z-skor farkı ΔC -0,040 ile +0,0007) | evet, eğim 1,57-2,74 | Sağkalım tarafında paralel |
| `lee2025` | Pankreas kanseri | evet, eşleşmiş örnek | ölçülmedi | evet, olasılık kayması | Eşik kaymasını destekler |
| `kervanci2026` | Akciğer | evet | **hayır**, AUROC 0,58 | evet | Kısmi, karşı yön de içerir |
| `kolev2026` | Sepsis | hayır, karşılaştırma grubu | kısmen, AUROC 0,73 | evet, eğim 0,24 | Benzer, başka neden |
| `warnatherresthal2020` | AML (lösemi) | evet | AUC yok | doğruluk çöküyor, gen bazlı sıra ile düzeliyor | Lösemide öncül, ayrım yapmaz |
| `vancalster2023` | Klinik modeller | ölçüm farkı dahil | evet (örneklerde) | evet | Genel ilke |

**Değerlendirme:**

- "AUC taşınır, eşik taşınmaz" genel iddiası yeni değildir. Bu cümle yenilik olarak yazılırsa hakem `zheng2026`'yı gösterir.
- Lösemide öncül de vardır (Warnat 2020), ama bu kaynak AUC raporlamadığı için ayrışmayı göstermez.
- Taramamızda ALL ve AML ayrımı için, sıralama ile eşik davranışını aynı anda raporlayan bir çalışma bulunmadı. Bu "ilk" demek değildir; yalnızca aşağıdaki tarama sınırları içinde "bulunamadı" demektir.

**Hâlâ özgün olabilecek noktalar (güçlüden zayıfa):**

1. **Örnek içi sıra dönüşümünün eşiği kurtarmaması.** `zheng2026`'da rank artı eğitimden ölçekleme 0,95-1,00 verir. Bizim `results/feasibility.json` sonuçlarında aynı biçimdeki kol 0,50-0,70 verir; hatta MILE'dan Golub'a AUC 0,660'a düşer. `lee2025` bunun için kaynaklı bir mekanizma sunar: göreli gen sırası platforma göre değişir. Bu ayrışma doğrulanırsa makalenin en ilginç bulgusu olur.
2. **Eşik kaymasının kaynağını ayırmak.** `zheng2026` platform, prevalans, vaka karışımı ve teknik parti etkisini ayıramadığını söyler. Örnekleme ile prevalansı sabitleyen bir deney bu boşluğu doldurur.
3. **Görev ve platform aralığı.** Üç farklı dizi platformu (GPL80, GPL570, GPL4861) arasında üç kohortlu, çift yönlü ALL/AML aktarımı. Bu tek başına küçük bir katkıdır.

**Pilotla ilgili düzeltilmesi gereken üç nokta:**

- **0,59-0,94 ve 0,93-0,99 aralıkları yalnızca kohort içi z-skor satırlarından gelir** (`scripts/run_feasibility.py`, `prepare`). Bu yöntem test kohortunun kendi ortalama ve standart sapmasını kullanır. `zheng2026`'nın terimiyle sabit aktarım değil, etiketsiz kohort uyarlamasıdır; `patil2015` terimiyle test kümesi yanlılığına açıktır. Metinde bu açıkça yazılmalı.
- **Sabit aktarım durumu daha serttir.** Ham satırların dördünde dengeli doğruluk 0,50, AUC 0,965-0,992. Bu `zheng2026` ile aynı desendir ve aslında daha temiz kanıttır. Ama MILE'dan Golub'a ve Andersson'a ham satırlar 0,835 ve 0,918 verir, yani çöküş evrensel değildir.
- **"Sıralama taşınır" her kolda doğru değildir** (sıra kolunda AUC 0,660). "Kalibrasyon" sözcüğü de şimdilik kullanılmamalı: pilot eğim, kesişim veya O/E ölçmüyor, yalnızca 0,5 eşiğini ölçüyor (`riley2024part2`, `collins2024part1`).

**Önerilen deneyler (final aşaması):**

- Kalibrasyon kesişimi, eğimi, O/E ve Brier ekle.
- Prevalansı sabitleyen alt örnekleme ile eşik kaymasını sınıf karışımından ayır.
- Kohort içi z-skoru küçük referans kümeleriyle test et (`zheng2026` n=5 referansta ortalama 0,897, en az 0,679 bulur).
- Eğitimden türetilen eşik ve az etiketli yeniden kalibrasyonu karşılaştır.
- Golub testlerinde örneklem uyarısını yaz (`vancalster2023`).

**Önerilen çerçeve:** Bulguyu yenilik olarak değil, `zheng2026`'nın lösemi ve ALL/AML görevindeki bağımsız tekrarı olarak sun; özgün katkıyı sıra dönüşümünün başarısızlığı ve eşik kaymasının kaynağı üzerine kur. İddia 1 de yeni değildir (`ambroise2002`, `demircioglu2021`, `rosenblatt2024`); tek işlem hattında ölçüm olarak sunulmalıdır.

**Tarama sınırları:** Europe PMC (yaklaşık 35 sorgu) ve Crossref; 2026-11-06 tarihinde. Google Scholar, Scopus ve Web of Science kullanılmadı. Çoğu sorgu güncel 2026 sonuçlarını öne çıkardı, eski çalışmalar kaçmış olabilir. Sonuçların çoğu başlıktan elendi, her biri okunmadı.
