# Okuma Rehberi / Reading Guide

Hazırlanma tarihi: 2026-11-06. Bu rehber 38 kaynağı ne kadar öncelikli okuman gerektiğine göre sıralar. Özetler [okuma notlarından](reading_notes.md) türetildi. Notların bir bölümünü yapay zekâ okuyucu ajanlar çıkardı, yani bu özetler kaynağın kendisini okumanın yerini tutmaz.

*Prepared on 2026-11-06. This guide ranks the 38 references by reading priority. Summaries derive from the [reading notes](reading_notes.md), part of which were produced by AI reader agents, so they do not replace reading the sources.*

**Dil notu:** Makalelerin tam Türkçe çevirisini vermedim, çünkü çoğu telifli. Aşağıda her öncelikli kaynak için kendi cümlelerimizle Türkçe ve İngilizce özet ile özgün metnin bağlantısı var.

**Erişim işaretleri:** 🟢 ücretsiz tam metin bulundu · 🟡 ücretsiz sürüm farklı veya dolaylı · 🔴 abonelik gerekiyor (ESOGÜ kütüphanesini dene).

## Nasıl okumalısın?

1. Önce Öncelik 1'deki altı makaleyi oku. Hoca ya da hakem sorduğunda bunlara dayanarak cevap vereceksin.
2. Her makalede şu üç soruyu cevapla: Soru neydi? Doğrulama nasıl yapıldı? Bizim çalışmamız bundan neyi farklı yapıyor?
3. Literatür cümlelerini ancak kaynağa bakarak yaz. Ara raporda bellekten yazılan 8 iddia yanlış çıkmıştı.

---

## Öncelik 1: Mutlaka oku / Must read

### 1. Golub ve ark. 1999 🟡
**Molecular Classification of Cancer: Class Discovery and Class Prediction by Gene Expression Monitoring.** *Science.* [doi:10.1126/science.286.5439.531](https://doi.org/10.1126/science.286.5439.531)

- **TR:** Ana veri setimizin kaynağı. 38 örnekte 50 genli ağırlıklı oylama öngörücüsü kurulur ve 34 bağımsız örnekte sınanır: 29 örnek güçlü tahmin alır, hepsi doğrudur, 5'i eşiğin altında kalır. Tüm ALL hastaları çocuktur; AML'lerin 15'i erişkin, 10'u çocuktur.
- **EN:** Source of our main data set. A 50-gene weighted-voting predictor is built on 38 samples and tested on 34 independent ones: 29 receive strong predictions, all correct, and 5 fall below the threshold. All ALL patients are children; 15 AML patients are adults and 10 are children.
- **Odaklan / Focus:** Veri bölümü ve Şekil 3B. Ücretsiz kopya için Broad Institute arşivini ara.

### 2. Ambroise ve McLachlan 2002 🟢
**Selection bias in gene extraction on the basis of microarray gene-expression data.** *PNAS.* [doi:10.1073/pnas.102102699](https://doi.org/10.1073/pnas.102102699)

- **TR:** Makalemizin birinci iddiasının temeli. Genler hata tahmininin dışında seçilirse iç hata sıfıra iner, ama seçimi kapsayan dış hata inmez. Karıştırılmış etiketlerde de iç hata sıfıra yaklaşır, dış hata 0,40–0,45 kalır. Bizim pilotumuz aynı olguyu tek işlem hattında gösteriyor.
- **EN:** Foundation of our first claim. If genes are selected outside error estimation, the internal error drops to zero while the external error does not. With shuffled labels the internal error also approaches zero, while the external error stays at 0.40–0.45. Our pilot shows the same effect in one pipeline.
- **Odaklan / Focus:** Etiket karıştırma denemesi ve seçim yanlılığı rakamları.

### 3. Varma ve Simon 2006 🟢
**Bias in error estimation when using cross-validation for model selection.** *BMC Bioinformatics.* [doi:10.1186/1471-2105-7-91](https://doi.org/10.1186/1471-2105-7-91)

- **TR:** İç içe CV'nin dayanağı. Parametreler CV hatasına göre ayarlanırsa bu minimum hata iyimser olur. Benzetimde iç içe CV neredeyse yansız, hafif kötümser sonuç verir. Çalışmada gerçek mikrodizi verisi yoktur.
- **EN:** The basis for nested CV. Tuning on CV error makes that minimum error optimistic. In simulation, nested CV is almost unbiased and slightly pessimistic. No real microarray data are used.
- **Odaklan / Focus:** Yöntem bölümü ve dış döngü koşulu; bizim 5 katlı dış döngümüz onlarınkinden farklıdır.

### 4. Warnat-Herresthal ve ark. 2020 🟢
**Scalable Prediction of Acute Myeloid Leukemia Using High-Dimensional Machine Learning and Blood Transcriptomics.** *iScience.* [doi:10.1016/j.isci.2019.100780](https://doi.org/10.1016/j.isci.2019.100780)

- **TR:** Makalemizin en yakın rakibi. 105 çalışmadan 12.029 örnekte AML'yi diğer tüm örneklerden ayırır; çalışma-ayrık ve platformlar arası testler yapar. U133A'dan RNA-seq'e ham aktarım başarısız olur, sıra dönüşümü bunu düzeltir. Bizim görevimiz ikili ALL/AML'dir. Farkımızı bu makaleye göre kurmalıyız.
- **EN:** Our closest competitor. It separates AML from all other samples in 12,029 samples from 105 studies, with study-disjoint and cross-platform tests. Raw transfer from U133A to RNA-seq fails and a rank transform repairs it. Our task is binary ALL/AML, and our novelty must be defined against this paper.
- **Odaklan / Focus:** Çapraz çalışma ve çapraz platform sonuçları. Ek tablolarda GSE13159'un dahil olup olmadığını kontrol et; biz bunu doğrulayamadık.

### 5. Haferlach ve ark. 2010 🟢
**Clinical Utility of Microarray-Based Gene Expression Profiling in the Diagnosis and Subclassification of Leukemia.** *J Clin Oncol.* [doi:10.1200/JCO.2009.23.4732](https://doi.org/10.1200/JCO.2009.23.4732) · [PMC5569671](https://pmc.ncbi.nlm.nih.gov/articles/PMC5569671/)

- **TR:** MILE kohortunun kaynağı. Aşama 1'de 18 sınıfta CV doğruluğu %92,2, kör aşama 2'de %88,1'dir. Bizim kilitli test setimiz olan aşama 2 buradan gelir.
- **EN:** Source of the MILE cohort. Stage 1 reaches 92.2% CV accuracy over 18 classes, and blind stage 2 reaches 88.1%. Stage 2 is our locked test set.
- **Odaklan / Focus:** Aşama 1 ve 2 tasarımı, etiketlerin merkezler arasında standart olmaması.

### 6. Dudoit, Fridlyand ve Speed 2002 🟡
**Comparison of Discrimination Methods for the Classification of Tumors Using Gene Expression Data.** *JASA.* [doi:10.1198/016214502753479248](https://doi.org/10.1198/016214502753479248)

- **TR:** Basit yöntemlerin (DLDA, k-NN) karmaşık yöntemlerle yarıştığını gösterir. Ön işlememizin dayanağıdır; taban 100 ile bizim veride tam 3.571 gen üretildi. Biz JASA sürümünü değil, 2000 tarihli Berkeley teknik raporunu (no. 576) okuduk.
- **EN:** Shows that simple methods (DLDA, k-NN) rival complex ones. It underpins our preprocessing; a floor of 100 reproduced exactly 3,571 genes on our data. We read the 2000 Berkeley technical report (no. 576), not the JASA version.
- **Odaklan / Focus:** Ön işleme adımları ve 150 tekrarlı bölme tasarımı.

---

## Öncelik 2: Makale yazmadan önce oku / Read before writing the paper

### 7. Andersson ve ark. 2007 🔴
**Microarray-based classification of a consecutive series of 121 childhood acute leukemias.** *Leukemia.* [doi:10.1038/sj.leu.2404688](https://doi.org/10.1038/sj.leu.2404688)

- **TR:** Üçüncü veri setimizin kaynağı. Tam metnini okuyamadık; yalnızca özet ve GEO kaydı var. Makalede kullanmadan önce kütüphaneden tam metni edin.
- **EN:** Source of our third data set. We could not read the full text, only the abstract and the GEO record. Obtain it through the library before using it in the paper.

### 8. Hollmann ve ark. 2025 🟢
**Accurate predictions on small data with a tabular foundation model (TabPFN).** *Nature.* [doi:10.1038/s41586-024-08328-6](https://doi.org/10.1038/s41586-024-08328-6)

- **TR:** B2 bonusunun temeli. 10.000 örnek ve 500 özniteliğe kadar ayarlı ağaç yöntemlerini geçer. Gen ifadesi veya n≈72 için doğrudan kanıt yoktur; bu bizim sınayacağımız boşluk.
- **EN:** Basis of bonus B2. It beats tuned tree methods up to 10,000 samples and 500 features. It offers no direct evidence for gene expression or n≈72, which is the gap we will test.

### 9. Grinsztajn, Oyallon ve Varoquaux 2022 🟢
**Why do tree-based models still outperform deep learning on typical tabular data?** *NeurIPS.* [Bildiri](https://proceedings.neurips.cc/paper_files/paper/2022/hash/0378c7692da36807bdec87ab043cdadc-Abstract-Datasets_and_Benchmarks.html)

- **TR:** Ağaçlar orta boyutlu tablo verisinde derin ağları geçer. Ders rehberi de buna atıf yapar. Ancak d<500 ve n≥3.000 rejimidir, p≫n mikrodizilere doğrudan taşınmaz.
- **EN:** Trees beat deep networks on medium-sized tabular data, and the course guide cites this. However, the regime is d<500 and n≥3,000, so it does not transfer directly to p≫n microarrays.

### 10. Nadeau ve Bengio 2003 🟢
**Inference for the Generalization Error.** *Machine Learning.* [doi:10.1023/A:1024068626366](https://doi.org/10.1023/A:1024068626366)

- **TR:** Düzeltilmiş yeniden örnekleme t testinin kaynağı. Rastgele bölmeler için türetilmiştir; standart k katlı CV'ye uygulamamızın sınırını makalede açıkça yazmalıyız.
- **EN:** Source of the corrected resampled t-test. It was derived for random splits, so the paper must state the limits of applying it to standard k-fold CV.

### 11. Demšar 2006 🟢
**Statistical Comparisons of Classifiers over Multiple Data Sets.** *JMLR.* [Makale](https://www.jmlr.org/papers/v7/demsar06a.html)

- **TR:** Friedman testi veri setleri içindir, tek veri setindeki katlar için değil. Planımızı bu yüzden değiştirdik.
- **EN:** The Friedman test is for data sets, not for folds within one data set. This is why we changed our plan.

### 12. Leek ve ark. 2010 🟢
**Tackling the widespread and critical impact of batch effects in high-throughput data.** *Nat Rev Genet.* [doi:10.1038/nrg2825](https://doi.org/10.1038/nrg2825) · [PMC3880143](https://pmc.ncbi.nlm.nih.gov/articles/PMC3880143/)

- **TR:** Batch etkisinin neden yaygın olduğunu ve normalizasyonun bunu tek başına gidermediğini anlatır. İkinci iddiamızın arka planıdır.
- **EN:** Explains why batch effects are widespread and why normalisation alone does not remove them. It is the background to our second claim.

### 13. Johnson, Li ve Rabinovic 2007 🟢
**Adjusting batch effects in microarray expression data using empirical Bayes methods (ComBat).** *Biostatistics.* [doi:10.1093/biostatistics/kxj037](https://doi.org/10.1093/biostatistics/kxj037)

- **TR:** Küçük batch'lerde deneysel Bayes düzeltmesi. Dengesiz tasarımda dikkat ister; kohortlarımızın sınıf oranları farklı olduğu için bu önemlidir.
- **EN:** Empirical Bayes correction for small batches. It needs care under unbalanced designs, which matters because our cohorts differ in class ratio.

### 14. Guyon ve ark. 2002 🟢
**Gene Selection for Cancer Classification using Support Vector Machines.** *Machine Learning.* [doi:10.1023/A:1012487302797](https://doi.org/10.1023/A:1012487302797)

- **TR:** SVM-RFE'nin kaynağı. Golub testinde 8 veya 16 genle 0/34 hata bildirir, ama gen seçimi LOO katları içinde yinelenmemiş görünür. Sızıntı tartışmasının klasik örneğidir.
- **EN:** Source of SVM-RFE. It reports 0/34 test errors with 8 or 16 genes, but gene selection does not appear to be repeated inside the LOO folds. It is a classic example for the leakage discussion.

### 15. Yeni yüksek sonuçlu çalışmalar / Recent high-accuracy studies 🟢

- **Xie ve ark. 2022** [doi:10.1186/s12859-022-04848-y](https://doi.org/10.1186/s12859-022-04848-y) · **Rezaee ve ark. 2022** [doi:10.1049/syb2.12044](https://doi.org/10.1049/syb2.12044) · **Awotunde ve ark. 2022** [doi:10.3390/s22249689](https://doi.org/10.3390/s22249689) · **Selvaraj ve ark. 2024** [doi:10.1007/s12672-024-01337-x](https://doi.org/10.1007/s12672-024-01337-x)
- **TR:** Boşluk paragrafımızın dayanağı. %97–99,9 bildirirler, güven aralığı vermezler. Sızıntı yorumumuz makalelerin anlatım sırasından çıkarımdır, kesin kanıt değildir. Makalede eleştirirken bu yüzden dikkatli olmalısın; yöntem bölümlerini kendin oku.
- **EN:** The basis of our gap paragraph. They report 97–99.9% with no confidence intervals. Our leakage reading is inferred from the order of their descriptions and is not proof, so be careful when criticising them and read their methods yourself.

---

## Öncelik 3: Başvuru kaynakları / Reference material

| Kaynak / Source | Türkçe | English | Bağlantı / Link |
|---|---|---|---|
| Tibshirani 2002 🟢 | En yakın küçültülmüş merkezler; Golub testinde 2/34 hata, 21 gen | Nearest shrunken centroids; 2/34 test errors on Golub, 21 genes | [doi](https://doi.org/10.1073/pnas.082099299) |
| Zou ve Hastie 2005 🟢 | Elastic net; birinci yöntemimizin cezası | Elastic net; the penalty of our first method | [doi](https://doi.org/10.1111/j.1467-9868.2005.00503.x) |
| Breiman 2001 🟢 | Rastgele ormanın özgün makalesi | Original random forest paper | [doi](https://doi.org/10.1023/A:1010933404324) |
| Cortes ve Vapnik 1995 🟢 | SVM'nin özgün makalesi | Original SVM paper | [doi](https://doi.org/10.1007/BF00994018) |
| Díaz-Uriarte 2006 🟢 | Mikrodizide rastgele orman ve gen seçimi | Random forest and gene selection on microarrays | [doi](https://doi.org/10.1186/1471-2105-7-3) |
| Furey 2000 🟡 | Golub verisinde erken SVM; gen sıralaması CV içinde | Early SVM on Golub; gene ranking inside CV | [doi](https://doi.org/10.1093/bioinformatics/16.10.906) |
| Cawley ve Talbot 2010 🟢 | Model seçiminde aşırı uyum; seçim varyansı önemli | Over-fitting in model selection; selection variance matters | [JMLR](https://www.jmlr.org/papers/v11/cawley10a.html) |
| Kohlmann 2008 🟢 | MILE ön fazı; 11 laboratuvarda tekrarlanabilirlik | MILE prephase; reproducibility across 11 labs | [doi](https://doi.org/10.1111/j.1365-2141.2008.07261.x) |
| Warnat-Herresthal 2021 🟢 | Swarm learning; merkeziyetsiz eğitim, benzetimli merkezler | Swarm learning; decentralised training on simulated sites | [doi](https://doi.org/10.1038/s41586-021-03583-3) |
| Gorishniy 2021 🟢 | FT-Transformer; küçük n veya p≫n sınanmamış | FT-Transformer; small n or p≫n not tested | [NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/9d86d83f925f2149e9edb0ac3b49229c-Abstract.html) |
| Chen ve Zou 2025 🟡 | GenePT; tek hücre, bizdeki kullanım bir uyarlama. Ön baskı okundu | GenePT; single-cell, our use is an adaptation. Preprint read | [doi](https://doi.org/10.1038/s41551-024-01284-6) |
| Alharbi 2023 🟢 | Gen ifadesinde ML derlemesi | Review of ML on gene expression | [doi](https://doi.org/10.3390/bioengineering10020173) |
| Alhenawi 2022 🔴 | Öznitelik seçimi sistematik derlemesi; özet okundu | Systematic review of feature selection; abstract read | [doi](https://doi.org/10.1016/j.compbiomed.2021.105051) |
| Armstrong 2002 🔴 | MLL'li ALL ayrı bir ifade profili taşır; özet okundu | MLL-translocated ALL has a distinct profile; abstract read | [doi](https://doi.org/10.1038/ng765) |
| Statnikov 2005 🔴 | Çok sınıflı SVM karşılaştırması; özet okundu | Multicategory SVM comparison; abstract read | [doi](https://doi.org/10.1093/bioinformatics/bti033) |
| Feltes 2019 🔴 | CuMiDa kıyas veri tabanı; özet okundu | CuMiDa benchmark database; abstract read | [doi](https://doi.org/10.1089/cmb.2018.0238) |
| Liu 2006 🔴 | PQN/DQN normalizasyonu; MILE işlemesinde kullanılır, özet okundu | PQN/DQN normalisation used for MILE; abstract read | [doi](https://doi.org/10.1016/j.jtbi.2006.06.017) |
| Benjamini ve Hochberg 1995 🔴 | FDR düzeltmesi; yalnızca künye | FDR correction; citation only | [doi](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x) |
| van der Maaten 2008 🟢 | t-SNE | t-SNE | [JMLR](https://www.jmlr.org/papers/v9/vandermaaten08a.html) |
| Pedregosa 2011 🟢 | scikit-learn | scikit-learn | [JMLR](https://www.jmlr.org/papers/v12/pedregosa11a.html) |

---

## Finalde bulunması gereken yeni kaynaklar / New sources needed for the final

Bunları henüz taramadık; hedef liste olarak düşün.

- Kullanacağımız TARGET verisinin kaynak makaleleri / the source papers of the TARGET data.
- Dış doğrulamada karar eşiği ve kalibrasyon kaymasını inceleyen klinik tahmin çalışmaları / clinical prediction studies on threshold and calibration shift under external validation.
- Platformlar arası gen ifadesi normalizasyonu çalışmaları / cross-platform gene expression normalisation studies.
- Ders rehberinin andığı, TabPFN'in RNA-seq'teki kısıtını gösteren 2025 bioRxiv çalışması / the 2025 bioRxiv study on TabPFN limits on RNA-seq named in the course guide.
