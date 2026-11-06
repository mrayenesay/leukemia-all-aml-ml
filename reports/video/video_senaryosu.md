# Ara Rapor Tanıtım Videosu — Senaryo (hedef süre: 8–9 dk, üst sınır 10 dk)

Kurallar (rehber Bölüm 10): yüzünüz açılışta ve kod anlatımında köşede görünsün, anlatım
kendi sesinizle olsun (yapay ses/avatar yok). YouTube "liste dışı" veya Google Drive linki,
en az 6 ay erişilebilir. Link raporun ilk sayfasındaki `\VideoURL` satırına yazılacak.

Kayıt önerisi: OBS Studio → ekran + webcam köşede. Ekranda sırayla: PDF rapor, VS Code,
terminal.

---

## 0:00–0:45 — Açılış ve problem (yüz tam ekran → rapor ilk sayfa)
- Kendinizi tanıtın: ad, öğrenci no, ders.
- Problem: ALL ve AML'nin ikisi de akut lösemi alt tipi; biri lenfoid, diğeri miyeloid
  kökenli. Tedavi protokolleri farklı olduğu için doğru ayrım klinik açıdan kritik.
- Modüldeki "non-cancer" etiketi biyolojik olarak yanlış; çalışmada "ALL vs. AML alt tip
  sınıflandırması" diyoruz.
- Mikrodizi tek cümleyle: binlerce genin mRNA düzeyini aynı anda ölçen çip.

## 0:45–1:30 — Araştırma soruları (rapor Bölüm I)
- AS1: Sızıntısız nested CV'de üç yöntem (elastic-net LR, SVM, RF) anlamlı farklı mı?
- AS2: Modüldeki 38/34 tek bölme, nested CV güven aralığının içinde mi?
- AS3: Sinyal kohortlar/platformlar arası taşınıyor mu?
- AS4 (bonus): Derin öğrenme ve TabPFN klasik yöntemleri geçiyor mu?

## 1:30–3:00 — Literatür (Tablo I)
- Arama protokolü: Crossref, Europe PMC, PubMed; 6 Kasım'da hedefli ek tarama; 52 kaynak (31'i
  2021 ve sonrası); 47 tam metin, 4 özet, 1 künye (yapay zekâ destekli okuma).
- Güncel odak: sızıntı (Kapoor 2023, Rosenblatt 2024), dış doğrulama (Zheng 2026, Riley 2024),
  lösemi (Mulet 2025). Klasikler veri ve özgün yöntemlerle sınırlı.
- **Ana mesaj — boşluk:** yeni dört çalışmada %97–99,9 doğruluklar raporlanmış ama protokoller farklı;
  bazıları gen seçimini CV dışında yapıyor (Ambroise & McLachlan seçim yanlılığı). Güven
  aralığı ve bağımsız kohort testi nadir. Bu proje bunları hedefliyor.

## 3:00–4:15 — Veri setleri (Tablo II, Ek Şekil 7)
- Golub: 72 hasta, 7.129 prob, Hu6800; 38/34 bölme; 47 ALL / 25 AML.
- MILE (GSE13159): çok merkezli, U133 Plus 2.0; 2.096 örnekten yalnızca ALL ve AML alındı → 1.292 (750 ALL / 542 AML).
  İlginç bulgu: GEO "sinyal" diyor ama değerler dizi başına [0, 1] ölçekli log yoğunluk (ArrayExpress tablosuyla doğrulandı).
  Neden: aynı soru, çok daha büyük kohort, derin öğrenme ön eğitimi için uygun.
- Andersson (GSE7186): 121 çocuk lösemisi, iki renkli cDNA dizisi, log-oran, eksik
  değerler. Neden: farklı teknoloji + pediatrik → zor bir dış test; B4 bonusu.
- Uyumlaştırma: prob → gen sembolü, ortak gen sayısı (Tablo II / Bölüm III).

## 4:15–7:15 — EDA ve CANLI KOD (webcam köşede!)
1. **Terminalde çalıştırın:** `python scripts/run_eda.py --only golub`
   (çalışırken anlatın; ~20 sn sürer).
2. **VS Code'da `src/leukemia/data.py` → `load_golub`:**
   - CSV'de hasta sütunları sırasız (1–27, 34–38, 28–33) → etiketi sütun sırasıyla değil,
     hasta numarasıyla birleştiriyoruz; `assert`'ler sınıf sayılarını doğruluyor.
3. **Şekil 1 (kalite):** değerlerin %28,7'si negatif; nedeni MAS4 "average difference" =
   PM − MM; Absent çağrıları negatif/düşük değerlerle örtüşüyor. INF/NaN yok.
4. **Ek Şekil 8 (log dönüşümü):** clip [20, 16000] + log2 → çarpıklık 7,1'den 0,55'e; ortalama–
   varyans bağımlılığı (ρ 0,95 → 0,18) kayboluyor. Ölçeğe duyarlı modeller için şart.
5. **Ek Şekil 6 (PCA / t-SNE):** PC1 tek başına AUC 0,98 → güçlü sinyal; yöntem farkları küçük
   olacak, bu yüzden güven aralığı ve istatistiksel test şart.
6. **Ek Şekil 5 + Ek Tablo V (ayırt edici genler):** CST3, CD33, MPO, ZYX (AML), TCF3, CD79B,
   CD19, DNTT (ALL) — bilinen biyolojiyle uyumlu. Uyarı: bu sıralama sadece betimseldir,
   modelde öznitelik seçimi için kullanılırsa sızıntı olur.
7. **Ek Şekil 4 (batch etkisi):** test seti daha "sönük"; sınıf içi KS testinde ALL için genlerin
   %17,7'si p<0,05 (beklenen %5) → tek 34 örneklik test skoru yanıltıcı olabilir (AS2).
8. **Şekil 2 (kohortlar arası):** t istatistikleri kohortlar arası pozitif korelasyonlu, ortak
   üst genler şanstan fazla; ama ölçekler farklı → birleşik PCA'da PC1'i kohort belirliyor,
   kohort içi z-skor sonrası sınıf ekseni ortaya çıkıyor.

## 7:15–8:30 — Fizibilite pilotu ve final planı (Tablo III, Ek Şekil 3, Bölüm V)
- Pilot (ön bulgu, sabit ayar): rastgele etiketle sızıntılı protokol 0,91, doğru protokol 0,50;
  sabit aktarımda 6 yönün 4'ünde AUC 0,965–0,992, dengeli doğruluk 0,50. Bu desen sepsiste de
  bildirildi (Zheng 2026); özgün soru sıra dönüşümünün neden kurtarmadığı ve eşik kaymasının kaynağı.
- Kilitli dış testler: Golub 34 örnek, MILE aşama 2 (693 akut lösemi), TARGET (RNA-seq).
- Pipeline şeması: clip/log2 durumsuz; filtre, imputasyon, z-skor, SelectKBest **her eğitim
  katında yeniden fit** ediliyor (sklearn Pipeline).
- Protokol: (a) 38/34 bölme, test bir kez; (b) 72 örnek üzerinde 5×5 tekrarlı nested CV,
  5 seed. Metrikler: Accuracy, Balanced Acc., Precision, Recall, Specificity, F1, ROC-AUC,
  karışıklık matrisi; düzeltilmiş t-testi + Holm, McNemar.
- Bonuslar: B1 MLP/autoencoder (+MILE ön eğitim), B2 TabPFN + GenePT, B3 IEEE EMBC 2027 adayı (hocanın yazılı onayıyla),
  B4 Andersson.

## 8:30–9:00 — Kapanış
- Üç bulgu: güçlü biyolojik sinyal; train/test kayması; platform farkı → sızıntısız nested
  CV ve kohort içi standardizasyon gerekli.
- Tekrarlanabilirlik: `python run_all.py`, sabit seed 42, rapordaki her sayı betikten.
- GenAI beyanı: Claude kullanıldı, ayrıntılar Ek A'da.
