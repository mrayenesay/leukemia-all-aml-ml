# Okuma notları: ALL/AML ara raporunun kaynakları

Hazırlanma tarihi: 2026-11-05. Bu dosya `reports/ara_rapor/main.tex` içindeki 38 kaynağın erişim düzeyini ve içeriğini kaydeder. Metinler yalnızca yasal kaynaklardan alındı: açık erişim, yayıncının ücretsiz sunduğu kopya, yazar veya kurum kopyası. Korsan kaynak kullanılmadı. Tüm özetler kendi cümlelerimizledir.

## Erişim özeti

| Erişim düzeyi | Sayı | Kaynaklar |
|---|---:|---|
| Tam metin | 31 | golub1999, haferlach2010, kohlmann2008, furey2000, guyon2002, dudoit2002, tibshirani2002, diazuriarte2006, zou2005, ambroise2002, varma2006, cawley2010, leek2010, johnson2007, warnatherresthal2020, warnatherresthal2021, gorishniy2021, grinsztajn2022, hollmann2025, chen2025genept, alharbi2023, xie2022, rezaee2022, awotunde2022, selvaraj2024, breiman2001, cortes1995, nadeau2003, demsar2006, vandermaaten2008, pedregosa2011 |
| Yalnızca özet | 6 | andersson2007, armstrong2002, feltes2019, statnikov2005, alhenawi2022, liu2006 |
| Yalnızca künye | 1 | benjamini1995 |
| **Toplam** | **38** | |

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
- **Sınırlılık:** Ana metinde sayısal doğruluk yok (şekil ve ek tablolarda); yöntem eki ve Tablo S1 elimizde olmadığından GSE13159'un dahil olup olmadığı doğrulanamadı. Veriler farklı amaçlı çalışmalardan havuzlanmış, prospektif doğrulama yok; metindeki alt grup sayılarının toplamı 7.881 ediyor, verilen toplam 7.884.

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

