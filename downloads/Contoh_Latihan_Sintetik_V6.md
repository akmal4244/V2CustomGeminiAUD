# Contoh Latihan Sintetik — Gem V6 Kod Tajuk

Semua kes ialah rekaan untuk latihan sahaja, bukan laporan atau dapatan audit sebenar. Bahan ini bukan fail knowledge untuk analisis laporan sebenar. Nyatakan UJIAN SINTETIK apabila menggunakannya.

## Pengelasan kategori

| Kes rekaan | Kategori yang disokong |
|---|---|
| Polisi tidak menetapkan pengasingan tugas kutipan dan rekonsiliasi. | K1 — Tadbir Urus |
| Daftar kuasa mengesahkan pelulus tidak diberi kuasa bagi transaksi. | K2 — Tiada Mandat |
| Formula hamparan menyalin jumlah ke kolum salah; ralat teknikal disahkan. | K3 — Kesilapan / Isu Teknikal |
| SOP mewajibkan pemeriksaan bulanan tetapi enam pemeriksaan tidak dibuat. | K4 — Kecuaian |
| Peralatan program yang dibatalkan terbiar dan tidak pernah digunakan. | K5 — Pembaziran |
| Kemudahan berguna tetapi spesifikasi dan kos melebihi keperluan munasabah, disokong perbandingan setara. | K6 — Pemborosan |
| Rekod bank dan resit menunjukkan petunjuk kutipan dialihkan tanpa kebenaran. | K7 — Penyelewengan / Ketirisan; perlu semakan lanjut, bukan tuduhan muktamad |
| Catatan hanya menyebut isu pengurusan tanpa bukti khusus. | Belum dapat dikelaskan — bukti tidak mencukupi |

Satu kategori utama setiap ID. Kategori belum dapat ditentukan ialah status, bukan K8.

## Contoh risiko separa

```text
UJIAN SINTETIK — bukan dapatan audit sebenar.
Pasangan L/I berikut diberi untuk latihan kaedah sahaja.

Pemetaan Bahagian 2A (rekaan):
PPK-PTJA = Pengurusan Pentadbiran dan Kewangan — PTj A.
PKEND = Pengurusan Kenderaan.
Kod yang sama digunakan dalam Bahagian 2B hingga Bahagian 6.

ID Penemuan       Kategori/status             L   I   R    Tahap
PU-PPK-PTJA-01   K1 — Tadbir Urus             3   3   9    Tinggi
PU-PPK-PTJA-02   K3 — Isu Teknikal            2   2   4    Rendah
PU-PKEND-01   K4 — Kecuaian                4   —   —    Belum dapat ditentukan
PU-PKEND-02   Belum dapat dikelaskan       —   3   —    Belum dapat ditentukan

Semua empat ID kekal dalam B3 dan B5.
N = 4; N_sah = 2; N_belum = 2; 2 + 2 = 4.
K1=1; K2=0; K3=1; K4=1; K5=0; K6=0; K7=0; belum dikelaskan=1.
Jumlah kategori + belum dikelaskan = 4.

Statistik risiko SEPARA (subset N_sah=2):
Tinggi = 1/2 × 100 = 50%; Rendah = 1/2 × 100 = 50%.
Angka ini tidak mewakili keseluruhan empat penemuan.

Kekalkan L=4 bagi PU-PKEND-01 dan I=3 bagi PU-PKEND-02.
Minta bukti impak PU-PKEND-01 serta kemungkinan dan kategori PU-PKEND-02.
Jangan isi komponen yang hilang atau mereka tahap.

STATUS PENILAIAN RISIKO KESELURUHAN: SEPARA — BELUM LENGKAP
Tiada Tahap Risiko Keseluruhan muktamad.
PU-PPK-PTJA-01 memerlukan fokus tindakan berdasarkan risiko Tinggi yang sah.
PU-PKEND-01 dan PU-PKEND-02 memerlukan maklumat tambahan sebelum risiko dapat dilengkapkan.
```

## Semakan tambahan

- L=1, I=4: R=4, Rendah. L=2, I=3: R=6, Sederhana. L=3, I=4: R=12, Tinggi. L=4, I=4: R=16, Kritikal.
- N_sah=0: jangan kira peratus atau purata subset kerana penyebut sifar.
- N=0: laporkan tiada penemuan berdasarkan skop tersedia; bukan automatik risiko Rendah.
- Jika N_belum=0 dan N>0, nilai risiko keseluruhan berdasarkan corak risiko, isu berulang, keluasan impak dan kawalan; bukan label daripada purata sahaja.
- Cadangan pengurusan mesti menggunakan ID B3/B5 dan bilangan yang sesuai dengan bukti.

- Semua Kod Tajuk mesti unik, bermakna, ditetapkan dalam Bahagian 2A dan konsisten dalam Bahagian 2B hingga Bahagian 6. ID menggunakan PU-[KOD TAJUK]-[NN], dengan nombor turutan dua digit. Kod Tajuk bukan kod kategori K1–K7.
