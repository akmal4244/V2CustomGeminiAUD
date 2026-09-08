# V2CustomGeminiAUD — Latihan Gem V4.4.1

Versi kedua laman slaid latihan **Custom Gemini untuk Analisis Laporan Audit**, diselaraskan dengan Gem V4.4.1 dan tujuh kategori. HTML/CSS/JavaScript statik tanpa framework atau build dependency.

**Laman V2:** https://akmal4244.github.io/V2CustomGeminiAUD/#1

**Laman asal (tidak diubah):** https://akmal4244.github.io/CustomGeminiAUD/#1

## Mulakan analisis

Gem V4.4.1 sudah siap digunakan. Butang utama **Mulakan Analisis dengan Gem V4.4.1** pada slaid 1 membuka [Gem sedia ada](https://gemini.google.com/gem/10xOZ5ybA6Eqc0A9xzykmgTHPl_rq9sBK?usp=sharing), bukan pengurus atau editor Gem.

1. Buka Gem dan log masuk dengan akaun Google yang mempunyai akses.
2. Muat naik laporan yang dibenarkan organisasi dalam perbualan Gem.
3. Salin Prompt Penuh pada slaid 5 ke perbualan yang sama, hantar dan semak draf terhadap sumber asal.

Tiada langkah membina atau memasang Gem. Laman latihan kekal terbuka; tiada pengalihan automatik atau muat naik dokumen melalui laman ini. Akses tertakluk pada akaun dan kebenaran perkongsian. Jika akses ditolak, semak akaun atau hubungi pemilik.

## Kandungan

Sebelas slaid mengekalkan perjalanan lapan langkah: buka Gem sedia ada, dokumen, prompt standard, struktur laporan, prompt susulan, semakan juruaudit, rangka pembentangan dan rumusan visual. Navigasi menyokong butang, papan kekunci, hash `#1`–`#11`, skrin penuh dan dialog QR.

| Kod | Kategori |
|---|---|
| K1 | Tiada Mandat |
| K2 | Tadbir Urus |
| K3 | Kesilapan / Isu Teknikal |
| K4 | Kecuaian |
| K5 | Pembaziran |
| K6 | Pemborosan |
| K7 | Penyelewengan / Ketirisan |

Kategori bukan tahap keseriusan. Struktur laporan kekal enam bahagian + Bahagian7 QA. R=L×I, L/I integer1–4. Tahap R: Rendah1–4, Sederhana5–8, Tinggi9–12, Kritikal13–16; skor4 ialah Rendah. Risiko keseluruhan menggunakan Formula Hibrid, bukan purata sahaja.

## Bahan muat turun pilihan

Fail ini ialah rujukan dan sandaran; peserta tidak perlu memuat turun atau memasangnya untuk menggunakan Gem yang sudah siap.

Dalam `downloads/`:
- `Arahan_Gem_v4.4.1.md` — rujukan/sandaran arahan penuh Gem.
- `Panduan_Format_Analisis_Audit_v4.4.1.md` — rujukan knowledge format/kaedah sejajar.
- `Panduan_7_Kategori_Isu_Audit_v4.4.1.md` — rujukan knowledge kategori sejajar.
- `Rangka_Pembentangan_v4.4.1.md` — templat teks kosong, bukan fail PowerPoint.
- `Contoh_Latihan_Sintetik_v4.4.1.md` — kes rekaan dan jangkaan semakan, bukan dapatan audit sebenar atau knowledge bagi laporan sebenar.

Arahan dan knowledge bukan sumber dapatan. Muat naik laporan audit sebenar hanya dalam perbualan yang dibenarkan organisasi. Jangan terbit laporan, lampiran, hasil audit sensitif, token atau kata laluan dalam repo ini.

Pautan editor pemilik tidak diterbitkan. Laman ini tidak mengubah kebenaran perkongsian Gem atau menyediakan akses tanpa akaun.

## Jalankan setempat

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory .
```

Buka `http://127.0.0.1:8765/#1`. Semua aset dan muat turun menggunakan laluan relatif supaya berfungsi di bawah sublaluan GitHub Pages.

## Deployment

Repo baharu ini menggunakan **GitHub Actions Pages** melalui `.github/workflows/pages.yml`, dicetuskan pada push `main` atau secara manual. Dalam Settings → Pages, sumber ialah GitHub Actions.

Workflow hanya menyalin HTML, tiga aset yang dinamakan dan lima fail metodologi/latihan yang dinamakan ke `_site`. Ia tidak menerbitkan keseluruhan repo atau folder sandaran. Tiada cPanel, kata laluan hosting atau SSH diperlukan.

## Semakan sebelum terbit

- Semua tajuk/prompt/salinan kategori dan julat risiko sejajar.
- Tiada ID hilang/ganda dalam contoh, taburan kategori + belum dikelaskan = N.
- JSON persediaan dan prompt penjanaan imej berasingan.
- QR menuju URL V2; semua pautan dalaman dan muat turun berfungsi.
- Navigasi11slaid, clipboard, skrin penuh/dialog, desktop dan skrin sempit diuji.
- Semak kandungan yang bakal di-commit: bahan latihan sahaja, tiada dokumen audit sebenar atau maklumat akses.

Keluaran Gem ialah **draf bantuan AI untuk semakan juruaudit**, bukan pensijilan, markah rasmi atau keputusan undang-undang. Semakan laman/sintetik bukan jaminan semua respons AI tepat.

## Kredit

Sistem Dibangunkan Sepenuhnya Oleh Akmal Marvis ©2026. Reka bentuk dan aset digunakan semula daripada laman CustomGeminiAUD asal. Logo Jata Negara: aset asal berasaskan Wikimedia Commons seperti didokumenkan dalam repo sumber. Penggunaan identiti pada bahan latihan tidak bermaksud pengesahan rasmi semua keluaran AI.
