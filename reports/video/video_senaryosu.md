# Ara Rapor Tanıtım Videosu — Senaryo (hedef süre: 7–8 dk, üst sınır 9 dk)

Kurallar (rehber Bölüm 10): yüzünüz açılışta ve kod anlatımında köşede görünsün, anlatım kendi sesinizle olsun (yapay ses/avatar yok). YouTube "liste dışı" veya Google Drive linki, en az 6 ay erişilebilir. Link raporun ilk sayfasındaki `\VideoURL` satırına yazılacak.

Kayıt önerisi: OBS Studio → ekran + webcam köşede. Ekranda sırayla: `reports/sunum/slides.pdf`, VS Code, terminal.

| Süre | Slayt | Vurgu |
|---|---|---|
| 0:00–0:25 | 1 Başlık | Ad, öğrenci no, konu; modeller finalde |
| 0:25–1:20 | 2 Problem | "non-cancer" yanlış; p≫n neden zor; dört araştırma sorusu |
| 1:20–2:10 | 3 Literatür | 52 kaynak; denetim hata yakaladı; %97–99,9 sonuçlar ve boşluk |
| 2:10–2:45 | 4 Veri setleri | Golub, MILE, Andersson ve seçilme nedenleri |
| 2:45–3:45 | Canlı kod | `run_eda.py --only golub`; `load_golub` etiket eşleme; `FoldChangeFilter` fit/transform |
| 3:45–4:30 | 5 Kalite ve dönüşüm | %28,7 negatif ve nedeni; kırpma + log2; 7,08 → 0,55 ve 0,95 → 0,18 |
| 4:30–5:10 | 6 Sinyal | PC1 AUC 0,984; 945 gen; biyolojik uyum; sıralama yalnızca betimsel |
| 5:10–5:50 | 7 Batch ve kohortlar | ALL içinde %17,7; ρ 0,56, 33 ortak gen; PC1'de kohort %99,8 |
| 5:50–6:45 | 8 Pilot | Rastgele etiket 0,91 ve 0,50; AUC 0,965–0,992, DD 0,50; sepsiste bildirildi; özgün soru; kilitli setler |
| 6:45–7:30 | 9–10 Plan ve kapanış | 3 yöntem, iki protokol, bonuslar, EMBC adayı; GenAI beyanı |

Rapordaki karşılıklar: literatür Bölüm II ve Tablo I; veri Bölüm III ve Tablo II; EDA Bölüm IV, Şekil 1–2 ve Ek C; pilot ve plan Bölüm V, Tablo III ve Ek Şekil 3.
