# Okuma Rehberi / Reading Guide

Hazırlanma tarihi: 2026-11-06. Raporda 52 kaynak var: 31'i 2021 ve sonrasından, 28'i 2022 ve sonrasından. Bu rehber önce güncel kaynakları öne alır; eski kaynakları yalnızca veri setimizin veya kullandığımız yöntemin özgün kaynağıysa öne çıkarır. Özetler [okuma notlarından](reading_notes.md) türetildi. Notların büyük bölümünü yapay zekâ okuyucu ajanlar çıkardı, yani özetler kaynağın kendisini okumanın yerini tutmaz.

*Prepared on 2026-11-06. The report has 52 references: 31 from 2021 or later, 28 from 2022 or later. This guide puts recent sources first and keeps older ones in front only when they are the origin of our data or methods. Summaries derive from the [reading notes](reading_notes.md), most of which were produced by AI reader agents, so they do not replace reading the sources.*

**Dil notu:** Makalelerin tam Türkçe çevirisi yok, çünkü çoğu telifli. Her öncelikli kaynak için kendi cümlelerimizle Türkçe ve İngilizce özet ile özgün metnin bağlantısı var.

**Erişim:** 🟢 ücretsiz tam metin bulundu · 🟡 ücretsiz sürüm farklı veya dolaylı · 🔴 abonelik gerekiyor (ESOGÜ kütüphanesini dene).

## Nasıl okumalısın?

1. Öncelik 1'deki yedi kaynağı oku. Hoca ya da hakem sorduğunda bunlara dayanarak cevap vereceksin.
2. Her makalede üç soruyu cevapla: Soru neydi? Doğrulama nasıl yapıldı? Bizim çalışmamız bundan neyi farklı yapıyor?
3. Literatür cümlelerini ancak kaynağa bakarak yaz. Ara raporda bellekten yazılan 8 iddia yanlış çıkmıştı.

---

## Öncelik 1: Mutlaka oku / Must read

### 1. Zheng ve Chen 2026 🟢
**High AUROC can mask decision failure in sepsis transcriptomic classifiers.** *PLOS One.* [doi:10.1371/journal.pone.0357585](https://doi.org/10.1371/journal.pone.0357585)

- **TR:** Makalemiz için en kritik kaynak. Mikrodiziden RNA-seq'e aktarımda AUROC 0,999 iken 0,5 eşiğinde dengeli doğruluk 0,50 çıkar. Yani "sıralama taşınıyor, eşik taşınmıyor" fikri bizim keşfimiz değildir. Onlarda örnek içi sıra dönüşümü eşiği kurtarır (0,95–1,00), bizim pilotta kurtarmaz. Eşik kaymasının platformdan mı, prevalanstan mı geldiğini ayıramadıklarını yazarlar; özgün katkımız bu noktalarda.
- **EN:** The most critical source for our paper. In microarray-to-RNA-seq transfer, AUROC is 0.999 while balanced accuracy at a 0.5 threshold is 0.50, so "ranking transfers, the threshold does not" is not our discovery. Their within-sample rank rescues the threshold (0.95–1.00); ours does not. They state they cannot separate platform from prevalence effects, and our contribution lies in these points.
- **Odaklan / Focus:** Ön işleme kolları ve sınırlılıklar bölümü.

### 2. Kapoor ve Narayanan 2023 🟢
**Leakage and the reproducibility crisis in machine-learning-based science.** *Patterns.* [doi:10.1016/j.patter.2023.100804](https://doi.org/10.1016/j.patter.2023.100804)

- **TR:** Sızıntının 17 alanda en az 294 makaleyi etkilediğini derler ve sızıntıyı türlere ayırır. Genlerin tüm veride seçilmesi bu türlerden biridir. Raporumuzdaki sızıntı dilinin çağdaş dayanağıdır.
- **EN:** Compiles leakage affecting at least 294 papers across 17 fields and sorts it into types. Selecting features on all the data is one of them. It is the current basis for how our report talks about leakage.
- **Odaklan / Focus:** Sızıntı sınıflaması ve "model bilgi sayfası" önerisi.

### 3. Golub ve ark. 1999 🟡
**Molecular Classification of Cancer: Class Discovery and Class Prediction by Gene Expression Monitoring.** *Science.* [doi:10.1126/science.286.5439.531](https://doi.org/10.1126/science.286.5439.531)

- **TR:** Ana veri setimizin kaynağı, eski ama zorunlu. 34 bağımsız örneğin 29'u güçlü tahmin alır ve hepsi doğrudur. Tüm ALL hastaları çocuktur.
- **EN:** Source of our main data set; old but required. Of 34 independent samples, 29 receive strong predictions, all correct. All ALL patients are children.

### 4. Ambroise ve McLachlan 2002 🟢
**Selection bias in gene extraction on the basis of microarray gene-expression data.** *PNAS.* [doi:10.1073/pnas.102102699](https://doi.org/10.1073/pnas.102102699)

- **TR:** Seçim yanlılığını Golub verisinde gösteren temel çalışma. Karıştırılmış etiketlerde iç hata sıfıra yaklaşır, dış hata 0,40–0,45 kalır. Pilotumuz aynı olguyu tek işlem hattında ölçer; bu yüzden birinci iddiamız bir ölçümdür, keşif değildir.
- **EN:** The core study showing selection bias on Golub data. With shuffled labels the internal error nears zero while the external error stays at 0.40–0.45. Our pilot measures the same effect in one pipeline, so our first claim is a measurement, not a discovery.

### 5. Warnat-Herresthal ve ark. 2020 🟢
**Scalable Prediction of Acute Myeloid Leukemia Using High-Dimensional Machine Learning and Blood Transcriptomics.** *iScience.* [doi:10.1016/j.isci.2019.100780](https://doi.org/10.1016/j.isci.2019.100780)

- **TR:** Lösemide en yakın rakibimiz. 12.029 örnekte AML'yi diğer tüm örneklerden ayırır. GSE13159'u da içerir (1.860 örnek). Ham platform aktarımı başarısız olur, gen bazlı sıra dönüşümü çözer. AUC bildirmez; görevi bizimkinden farklıdır.
- **EN:** Our closest competitor in leukemia. It separates AML from all others in 12,029 samples and includes GSE13159 (1,860 samples). Raw platform transfer fails and a gene-wise rank transform solves it. It reports no AUC, and its task differs from ours.

### 6. Mulet-Lazaro ve ark. 2025 🟢
**Transcriptional profiling directs the classification of acute leukemias of ambiguous lineage into AML, B-ALL, or T-ALL.** *HemaSphere.* [doi:10.1002/hem3.70195](https://doi.org/10.1002/hem3.70195)

- **TR:** ALL/AML görevine en yakın güncel çalışma. RNA-seq ile iç içe CV yapar; dış veride %97,5 duyarlılık, %93,7 kesinlik bildirir. Tek platformdur, eşik aktarımını incelemez.
- **EN:** The closest recent study to the ALL/AML task. It uses nested CV on RNA-seq and reports 97.5% recall and 93.7% precision on external data. It is single-platform and does not study threshold transfer.

### 7. Riley ve ark. 2024 🟢
**Evaluation of clinical prediction models (part 2): how to undertake an external validation study.** *BMJ.* [doi:10.1136/bmj-2023-074820](https://doi.org/10.1136/bmj-2023-074820)

- **TR:** Dış doğrulamanın nasıl yapılacağını anlatır. Tek ölçüt yetmez; c istatistiği vaka karışımına bağlıdır. Finalde eğim, kesişim ve O/E ölçmemizin dayanağı budur; pilotta kalibrasyon ölçmedik.
- **EN:** Explains how to run an external validation. No single measure is enough, and the c statistic depends on case mix. This is why we will measure slope, intercept and O/E in the final; the pilot did not measure calibration.

---

## Öncelik 2: Makaleden önce oku / Read before writing the paper

| Kaynak / Source | Türkçe | English | Bağlantı |
|---|---|---|---|
| Rosenblatt 2024 🟢 | Bağlantı modellerinde sızıntı; dikkat tahmininde r 0,01'den 0,48'e. Etki sinyal zayıfken en büyük | Leakage in connectome models; attention r from 0.01 to 0.48. Largest when signal is weak | [doi](https://doi.org/10.1038/s41467-024-46150-w) |
| Demircioğlu 2021 🟢 | 10 radyomik veri setinde CV öncesi seçim; AUC'de 0,149'a kadar yanlılık | Selection before CV in 10 radiomics sets; bias up to 0.149 AUC | [doi](https://doi.org/10.1186/s13244-021-01115-1) |
| Bates 2024 🟢 | CV neyi tahmin eder; olağan aralıklar dar olabilir. Kabul edilmiş el yazması okundu | What CV estimates; naive intervals can be narrow. Accepted manuscript read | [doi](https://doi.org/10.1080/01621459.2023.2197686) |
| Lee 2025 🟢 | Eşleşmiş örneklerde uyum %81; göreli gen sırası platformla değişiyor. Sıra sonucumuz için olası açıklama | Matched samples agree 81%; relative gene order shifts with platform. Possible reason for our rank result | [doi](https://doi.org/10.1038/s41698-025-01228-6) |
| Van Calster 2023 🟢 | "Doğrulanmış model" yoktur; kalibrasyon ayrımdan daha açıktır | No model is "validated"; calibration is more exposed than discrimination | [doi](https://doi.org/10.1186/s12916-023-02779-w) |
| Collins 2024 (bölüm 1) 🟢 | Klinik modellerin değerlendirilmesi; eğim ve kesişim tanımları | Evaluating clinical models; slope and intercept definitions | [doi](https://doi.org/10.1136/bmj-2023-074819) |
| TRIPOD+AI 2024 🟢 | Raporlama listesi; eşiğin nasıl belirlendiği yazılmalı | Reporting checklist; state how thresholds were set | [doi](https://doi.org/10.1136/bmj-2023-078378) |
| Foltz 2023 🟢 | Karışık platform eğitimi; z-skor en değişken yöntem | Mixed-platform training; z-score is the most variable method | [doi](https://doi.org/10.1038/s42003-023-04588-6) |
| Kervancı 2026 🟢 | Akciğerde mikrodiziden RNA-seq'e; ComBat'sız çöküş. İddiamıza kısmi karşı örnek | Lung, microarray to RNA-seq; collapse without ComBat. Partial counterexample | [doi](https://doi.org/10.3390/diagnostics16203413) |
| Botan 2026 🟢 | Meme kanserinde ayrım korunur, kalibrasyon eğimi bozulur | Breast cancer: discrimination holds, calibration slope degrades | [doi](https://doi.org/10.1186/s13058-026-02298-5) |
| Kolev 2026 🟢 | Sepsiste karşılaştırma grubu değişince dengeli doğruluk 0,527; etiket karıştırma örneği | Sepsis: balanced accuracy 0.527 when comparator changes; permutation control | [doi](https://doi.org/10.3390/ijms27209273) |
| Hollmann 2025 🟢 | TabPFN; B2 bonusu. n≈72 ve gen ifadesi için kanıt yok | TabPFN; bonus B2. No evidence for n≈72 or gene expression | [doi](https://doi.org/10.1038/s41586-024-08328-6) |
| Grinsztajn 2022 🟢 | Ağaçlar tablo verisinde önde; p≫n'e doğrudan taşınmaz | Trees lead on tabular data; not directly valid for p≫n | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2022/hash/0378c7692da36807bdec87ab043cdadc-Abstract-Datasets_and_Benchmarks.html) |
| Cui 2026 🟢 | Sıra dönüşümlü derin model; görülmemiş kohortlarda AML yok | Rank-based deep model; unseen cohorts contain no AML | [doi](https://doi.org/10.1038/s41698-026-01556-1) |
| Beder 2023 🟢 | ALLCatchR; 21 B-ALL alt tipi, dışarıda tutulan kohortlarda 0,957 | ALLCatchR; 21 B-ALL subtypes, 0.957 in hold-out cohorts | [doi](https://doi.org/10.1097/hs9.0000000000000939) |
| Jung 2026 🟢 | AML'de IDH tahmini; yüksek olasılıklar fazla tahmin ediliyor | IDH prediction in AML; high probabilities overestimated | [doi](https://doi.org/10.1093/nargab/lqag058) |
| Xie, Rezaee, Awotunde 2022; Selvaraj 2024 🟢 | Boşluk paragrafının dayanağı; %97–99,9, güven aralığı yok. Sızıntı yorumu anlatım sırasından çıkarım, kesin kanıt değil | Basis of our gap paragraph; 97–99.9%, no CIs. The leakage reading is inferred from their text, not proof | [Xie](https://doi.org/10.1186/s12859-022-04848-y) · [Rezaee](https://doi.org/10.1049/syb2.12044) · [Awotunde](https://doi.org/10.3390/s22249689) · [Selvaraj](https://doi.org/10.1007/s12672-024-01337-x) |

---

## Öncelik 3: Klasik ve başvuru kaynakları / Classics and reference

| Kaynak / Source | Neden gerekli / Why needed | Bağlantı |
|---|---|---|
| Haferlach 2010 🟢 | MILE veri setinin kaynağı / source of MILE | [doi](https://doi.org/10.1200/JCO.2009.23.4732) |
| Kohlmann 2008 🟢 | MILE ön fazı / MILE prephase | [doi](https://doi.org/10.1111/j.1365-2141.2008.07261.x) |
| Andersson 2007 🔴 | Üçüncü veri setinin kaynağı; tam metnini okuyamadık, kütüphaneden edin / source of the third data set; full text not read | [doi](https://doi.org/10.1038/sj.leu.2404688) |
| Varma ve Simon 2006 🟢 | İç içe CV'nin dayanağı / basis of nested CV | [doi](https://doi.org/10.1186/1471-2105-7-91) |
| Dudoit 2002 🟡 | Ön işleme; teknik rapor okundu / preprocessing; technical report read | [doi](https://doi.org/10.1198/016214502753479248) |
| Guyon 2002 🟢 | SVM-RFE; sızıntı tartışmasının klasik örneği / classic leakage example | [doi](https://doi.org/10.1023/A:1012487302797) |
| Furey 2000 🟡 | Golub'da erken SVM / early SVM on Golub | [doi](https://doi.org/10.1093/bioinformatics/16.10.906) |
| Tibshirani 2002 🟢 | Küçültülmüş merkezler; Golub testinde 2/34 hata / shrunken centroids; 2/34 test errors | [doi](https://doi.org/10.1073/pnas.082099299) |
| Zou ve Hastie 2005 🟢 | Elastic net; birinci yöntemimiz / elastic net, our first method | [doi](https://doi.org/10.1111/j.1467-9868.2005.00503.x) |
| Breiman 2001 🟢 | Rastgele ormanın özgün makalesi / original random forest | [doi](https://doi.org/10.1023/A:1010933404324) |
| Díaz-Uriarte 2006 🟢 | Mikrodizide rastgele orman / random forest on microarrays | [doi](https://doi.org/10.1186/1471-2105-7-3) |
| Nadeau ve Bengio 2003 🟢 | Düzeltilmiş t testi / corrected t-test | [doi](https://doi.org/10.1023/A:1024068626366) |
| Demšar 2006 🟢 | Çoklu veri setinde testler / tests across data sets | [JMLR](https://www.jmlr.org/papers/v7/demsar06a.html) |
| Leek 2010 🟢 | Batch etkileri / batch effects | [doi](https://doi.org/10.1038/nrg2825) |
| Johnson 2007 🟢 | ComBat | [doi](https://doi.org/10.1093/biostatistics/kxj037) |
| Benjamini ve Hochberg 1995 🔴 | FDR düzeltmesi; yalnızca künye / FDR; citation only | [doi](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) |
| van der Maaten 2008 🟢 | t-SNE | [JMLR](https://www.jmlr.org/papers/v9/vandermaaten08a.html) |
| Pedregosa 2011 🟢 | scikit-learn | [JMLR](https://www.jmlr.org/papers/v12/pedregosa11a.html) |
| Warnat-Herresthal 2021 🟢 | Swarm learning | [doi](https://doi.org/10.1038/s41586-021-03583-3) |
| Gorishniy 2021 🟢 | FT-Transformer | [NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/9d86d83f925f2149e9edb0ac3b49229c-Abstract.html) |
| Chen ve Zou 2025 🟡 | GenePT; ön baskı okundu / preprint read | [doi](https://doi.org/10.1038/s41551-024-01284-6) |
| Alharbi 2023 🟢 | Gen ifadesinde ML derlemesi / review of ML on gene expression | [doi](https://doi.org/10.3390/bioengineering10020173) |
| Alhenawi 2022 🔴 | Öznitelik seçimi derlemesi; özet okundu / feature selection review; abstract read | [doi](https://doi.org/10.1016/j.compbiomed.2021.105051) |
| Whalen 2022 🔴 | Genomikte ML tuzakları; özet okundu / ML pitfalls in genomics; abstract read | [doi](https://doi.org/10.1038/s41576-021-00434-9) |
| Bernett 2024 🔴 | Biyolojik ML'de sızıntı soruları; özet okundu / leakage questions; abstract read | [doi](https://doi.org/10.1038/s41592-024-02362-y) |

---

## Raporda olmayan ama işine yarayacak iki kaynak / Two useful sources outside the report

- **Zhou ve ark. 2025** 🟢 [doi:10.1101/2025.08.15.670537](https://doi.org/10.1101/2025.08.15.670537): TabPFN'in RNA-seq'teki sınırları. **Hakemden geçmemiş bioRxiv ön baskısı**; ders rehberinin andığı çalışma büyük olasılıkla budur. / A non-peer-reviewed preprint on TabPFN limits for RNA-seq, probably the one the course guide names.
- **Patil ve ark. 2015** 🟢 [doi:10.1093/bioinformatics/btv157](https://doi.org/10.1093/bioinformatics/btv157): Birlikte normalleştirilen örnekler değişince aynı hastanın tahmini değişebilir; z-skor kolumuz için uyarı. Eski kaynak olduğu için rapora eklemedim. / A patient's prediction can change with the samples normalised alongside it; a warning for our z-score arm. Left out of the report because it is old.

## Finale kalan tarama / Remaining search for the final

Bu tarama Europe PMC ve Crossref ile yapıldı. Rehber IEEE Xplore, Scopus ve Google Scholar gibi tabanları örnek veriyor; finalde bunları da taramalıyız.

*This search used Europe PMC and Crossref. The guide names IEEE Xplore, Scopus and Google Scholar as examples, so they should be searched for the final.*
