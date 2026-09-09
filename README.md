# V2CustomGeminiAUD — Latihan Gem V6

Laman latihan Custom Gemini untuk Analisis Laporan Audit, dikemas kini menggunakan lima fail Gem V6. HTML/CSS/JavaScript statik; reka bentuk dan navigasi 11 slaid dikekalkan.

**Laman:** https://akmal4244.github.io/V2CustomGeminiAUD/#1

Laluan GitHub Pages peka huruf besar/kecil: gunakan `V2CustomGeminiAUD` dengan V besar.

## Mulakan analisis

1. Buka [Gem analisis audit](https://gemini.google.com/gem/f90a8edf1a04?usp=sharing) melalui butang utama.
2. Muat naik dokumen audit sesi semasa yang dibenarkan organisasi.
3. Salin Prompt Penuh V6 pada slaid 5. Teksnya sama dengan fail prompt sumber.
4. Semak enam bahagian, ID, kategori, bukti dan kelengkapan risiko terhadap sumber asal.

Akses Gem tertakluk pada akaun dan kebenaran perkongsian. Laman tidak memuat naik laporan pengguna. Semua contoh latihan ialah sintetik.

## Kaedah V6

- K1 — Tadbir Urus
- K2 — Tiada Mandat
- K3 — Kesilapan / Isu Teknikal
- K4 — Kecuaian
- K5 — Pembaziran
- K6 — Pemborosan
- K7 — Penyelewengan / Ketirisan

Enam bahagian analisis wajib; QA dijalankan sebelum respons akhir. Semua ID Bahagian 3 mesti muncul dalam Bahagian 5. R=L×I; L/I 1–4. Rendah 1–4, Sederhana 5–8, Tinggi 9–12, Kritikal 13–16.

N ialah semua ID, N_sah ialah penemuan dengan L/I lengkap, N_belum ialah penilaian belum lengkap. N_sah+N_belum=N. Kekalkan komponen L atau I yang disokong bukti. Jika N_belum>0, statistik subset menggunakan N_sah dan dilabel SEPARA; status keseluruhan SEPARA — BELUM LENGKAP, tanpa tahap muktamad. Jika lengkap, nilai keseluruhan bukti dan kawalan, bukan purata semata-mata. Cadangan pengurusan mengikut isu dan bukti, dengan ID sama.

## Muat turun

Lima fail sumber disalin tanpa mengubah kandungan. `downloads/manifest-v6.json` merekod nama asal dan SHA256 untuk menyemak kesetiaan fail:

- [Matriks risiko 4×4 (.pdf)](downloads/Markah_Risiko_4x4.pdf)
- [Panduan 7 kategori V6 (.md)](downloads/Panduan_7_Kategori_Isu_Audit_V6.md)
- [Panduan format analisis V6 (.md)](downloads/Panduan_Format_Analisis_Audit_V6.md)
- [Arahan penuh Gem V6 (.txt)](downloads/Instruction_Gem_Penganalisis_Audit_V6.txt)
- [Prompt kali pertama V6 (.txt)](downloads/Prompt_Pertama_Analisis_V6.txt)

Bahan latihan tambahan:
- [Contoh sintetik V6](downloads/Contoh_Latihan_Sintetik_V6.md)
- [Templat fokus pengurusan V6](downloads/Templat_Fokus_Pengurusan_V6.md)

## Semakan dan penerbitan

```sh
python tests/check_site.py
python -m http.server 8765 --bind 127.0.0.1 --directory .
```

Workflow `.github/workflows/pages.yml` menjalankan semakan kemudian menerbitkan hanya HTML, aset dan fail muat turun yang disenaraikan. Push ke main mencetuskan GitHub Pages. Bahan versi terdahulu tersedia dalam sejarah Git.

Jangan terbitkan laporan audit sebenar, maklumat akses, token atau kata laluan. Arahan/knowledge ialah rujukan kaedah, bukan sumber dapatan. Hasil Gem ialah draf bantuan AI untuk semakan juruaudit.

## Kredit

Sistem Dibangunkan Sepenuhnya Oleh Akmal Marvis ©2026. Reka bentuk dan aset dikekalkan daripada laman asal CustomGeminiAUD.
