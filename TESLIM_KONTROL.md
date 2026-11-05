# Ara Rapor — Teslim Kontrol Listesi

Ders rehberinin "4. Ara Rapor isterleri" bölümündeki her madde ve nerede karşılandığı.
✅ = hazır, ⬜ = öğrencinin yapması gereken.

## Teslim paketi

| İster | Durum | Nerede |
|---|---|---|
| Ara rapor PDF'i, kapakta ad ve öğrenci no | ✅ | `reports/ara_rapor/main.pdf`, sayfa 1 |
| Kapakta video URL'si | ⬜ | `reports/ara_rapor/main.tex` satır 20 (`\VideoURL`), sonra yeniden derle |
| Kapakta kod deposu URL'si | ✅ | sayfa 1 dipnotu |
| Kod deposu: README, requirements.txt, sabit seed | ✅ | `README.md`, `requirements.txt`, `src/leukemia/config.py` (SEED = 42) |
| Depo hocanın erişebileceği durumda | ✅ | Herkese açık: https://github.com/mrayenesay/leukemia-all-aml-ml |
| Tanıtım videosu (5–10 dk, kendi sesin, yüz görünür) | ⬜ | Metin: `reports/video/konusma_metni.md`; slaytlar: `reports/sunum/slides.pdf` |
| GenAI kullanım beyanı | ✅ / ⬜ | `reports/genai/main.pdf`; bölüm 6'daki doğrulama listesini işaretle ve imzala |

## İçerik isterleri

| İster | Puan | Durum | Nerede |
|---|---|---|---|
| 1. Problem tanımı, klinik önem, mikrodizi açıklaması, ≥2 test edilebilir araştırma sorusu | – | ✅ | Bölüm I (4 araştırma sorusu, H0 tanımlı) |
| 1. "non-cancer" terminolojisinin düzeltilmesi | – | ✅ | Bölüm I, "Clinical problem" |
| 2. ≥15 kaynak, ≥10 hakemli, ≥5 son 5 yıl | A2 | ✅ | 38 kaynak, 38 hakemli, 11 tanesi 2021+; DOI'ler Crossref'te doğrulandı; 31 tam metin, 6 özet, 1 künye (`reports/literature/reading_notes.md`, `claim_audit.md`) |
| 2. Veritabanları, arama sorguları, tarih aralığı, dahil etme/dışlama ölçütleri | A2 | ✅ | Bölüm II "Search protocol"; ayrıntı: `reports/literature/search_log.md` |
| 2. Literatür özet tablosu (yazar/yıl · veri · ön işleme · yöntem · doğrulama · sonuç · not) | A2 | ✅ | Tablo I (özet) + Ek A (30 çalışmanın tamamı) |
| 2. Golub sonuçlarının karşılaştırmalı özeti + literatürdeki boşluk | A2 | ✅ | Tablo I "Best result / Leakage risk" sütunları; Bölüm II "Gap" paragrafı |
| 3. Ana + ≥1 benzer açık veri seti (ad, DOI, GEO no, lisans) | A3 | ✅ | Bölüm III: Golub, MILE (GSE13159), Andersson (GSE7186) |
| 3. Biyolojik bağlam, platform, n, p, sınıflar, dağılım | A3 | ✅ | Bölüm III + Tablo II + Ek Şekil 7 |
| 3. Seçim gerekçesi, ortak gen sayısı, platform farkları | A3 | ✅ | Bölüm III "Why it was chosen" ve "Harmonisation" |
| 3. Tüm veri setlerini yan yana özetleyen tek tablo | A3 | ✅ | Tablo II |
| 4. Veri kalitesi: eksik/INF, negatif/uç değer, P/A/M, etiket–sütun doğrulaması | A1 | ✅ | Bölüm IV-A, Şekil 1; MILE ölçek kontrolü |
| 4. Betimsel istatistik, sınıf dağılımı, log öncesi/sonrası dağılım | A1 | ✅ | Bölüm IV-B, Ek Şekil 7–8, 11, 15 |
| 4. PCA (açıklanan varyans), t-SNE | A1 | ✅ | Bölüm IV-C, Şekil 2, Ek Şekil 9, 12, 16 |
| 4. Sınıflar arası testler, ısı haritası, hiyerarşik kümeleme | A1 | ✅ | Bölüm IV-D, Şekil 3, Ek Tablo IV, Ek Şekil 10, 13–14, 17–18 |
| 4. Eğitim/test karşılaştırması (batch) ve veri setleri arası farklar | A1 | ✅ | Bölüm IV-E (Ek Şekil 6), IV-F (Şekil 4) |
| 4. Veri analitik aracı (Python) ve her şeklin yorumlanması | A1 | ✅ | Ana metin + ek şekil altyazıları |
| 4. Bulguların numaralı özeti ve modelleme çıkarımları | A1 | ✅ | Bölüm IV-G (7 madde) |
| 5. 3 ML yöntemi ve gerekçesi, hedeflenen bonuslar, takvim, riskler | – | ✅ | Bölüm V, Ek Şekil 5 (pipeline) |
| 6. GenAI beyanı (A4) | A4 | ✅ / ⬜ | `reports/genai/main.pdf` + raporda "Yapay Zekâ Kullanım Beyanı" bölümü |
| 6. Tanıtım videosu (A5) | A5 | ⬜ | yukarıya bak |
| IEEE şablonu, ≤6 sayfa + kaynaklar + ekler | – | ✅ | IEEEtran, Türkçe; ana metin 6. sayfada bitiyor |

## Yeniden üretme (hoca kontrol ederse)

```bash
pip install -r requirements.txt
python run_all.py            # veriyi indirir, EDA, makrolar, 3 PDF
```

Son uçtan uca test: 2026-11-03, hatasız (`python run_all.py --skip-download`).

## Bonuslar (finalde puanlanır)

| Bonus | Ara aşamadaki durum |
|---|---|
| B1 Derin öğrenme | Planlandı (Bölüm V); final deneyleriyle aynı protokolde yapılacak |
| B2 LLM / transformer (TabPFN, GenePT) | Planlandı |
| B3 IEEE konferansına gönderim | Finalden sonra; hocanın yazılı onayı gerekli, gönderimi öğrenci yapar |
| B4 Üçüncü veri seti | Andersson seçildi, A kriterleri (EDA) tamam; F kriterleri (modeller) finalde |
