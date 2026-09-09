# V2CustomGeminiAUD — Latihan Gem V6 Kod Tajuk

Laman latihan Custom Gemini untuk Analisis Laporan Audit, dikemas kini menggunakan lima fail terkini Gem V6 Kod Tajuk. HTML/CSS/JavaScript statik; reka bentuk, susunan dan aliran 11 slaid mengikuti [laman asal CustomGeminiAUD](https://akmal4244.github.io/CustomGeminiAUD/#1).

**Laman:** https://akmal4244.github.io/V2CustomGeminiAUD/#1

Laluan GitHub Pages peka huruf besar/kecil: gunakan `V2CustomGeminiAUD` dengan V besar.

## Mulakan analisis

1. Buka [Gem analisis audit](https://gemini.google.com/gem/1V-Tcts6MVW--dL2D6SRqQ4YIxiX-flui?usp=sharing) melalui butang utama.
2. Muat naik dokumen audit sesi semasa yang dibenarkan organisasi.
3. Salin Prompt Penuh V6 pada slaid 5. Teksnya sama dengan fail prompt sumber.
4. Semak enam bahagian, ID, kategori, bukti dan kelengkapan risiko terhadap sumber asal.
5. Pindahkan analisis yang disemak ke templat slaid dan jana rumusan visual sokongan dalam sembang Gemini baharu.

Akses Gem tertakluk pada akaun dan kebenaran perkongsian. Laman tidak memuat naik laporan pengguna. Semua contoh latihan ialah sintetik.

## Aliran slaid asal, kandungan V6

1. Pengenalan Custom Gemini untuk analisis laporan audit.
2. Tujuan latihan dan aliran langkah demi langkah.
3. Pautan terus ke Gem V6 dan rujukan sumber pilihan.
4. Muat naik dokumen pengauditan dan tetapkan skop.
5. Prompt penuh V6 Kod Tajuk yang sama dengan fail sumber.
6. Semak enam bahagian dan tujuh kategori.
7. Sepuluh contoh prompt: sembilan susulan analisis, satu penyusunan isi slaid selepas semakan.
8. Semakan juruaudit terhadap bukti, ID, kategori dan risiko.
9. Pindahkan hasil ke templat pembentangan seragam.
10. Prompt JSON V6 untuk rumusan visual Gemini Image.
11. Senarai semak akhir untuk mengulang aliran secara kendiri.

Pautan [templat pembentangan asal](https://docs.google.com/presentation/d/1qAY56GkkvYxQsKS5fhZaSlzfs1uqvOBn/edit?usp=sharing&ouid=105726279532383248637&rtpof=true&sd=true) dikekalkan sebagai rujukan susun atur. Data contoh dan kategori dalam templat perlu diganti dengan analisis V6, tujuh kategori, Kod Tajuk dan julat risiko yang betul. Templat luaran itu tidak diubah oleh laman ini.

Gem audit menjalankan analisis V6. Bonus 10 dan slaid 10 ialah penyusunan bahan pembentangan selepas semakan juruaudit, dalam sembang Gemini baharu. Prompt JSON ialah arahan penjanaan imej yang dihantar bersama analisis yang disemak. Ia mengekalkan Kod Tajuk/ID, kategori dan status SEPARA jika risiko belum lengkap; visual tidak menggantikan daftar penuh serta bukti sumber.

## Kaedah V6 Kod Tajuk

Bahagian 2A menetapkan Kod Tajuk bermakna, unik dan berasaskan tema audit sebenar serta singkatan Entiti/PTj jika perlu. Kekalkan kod dalam Bahagian 2B hingga Bahagian 6. ID Penemuan menggunakan `PU-[KOD TAJUK]-[NN]`, dengan nombor turutan dua digit; kod dalam ID mesti sepadan tepat dengan Bahagian 2A. Contoh kaedah: `PKEND` → `PU-PKEND-01`. Kod Tajuk berbeza daripada kategori K1–K7.

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
- [Panduan 7 kategori V6 (.txt)](downloads/Panduan_7_Kategori_Isu_Audit_V6.txt)
- [Panduan format V6 Kod Tajuk (.txt)](downloads/Panduan_Format_Analisis_Audit_V6_Kod_Tajuk.txt)
- [Arahan Gem V6 Kod Tajuk (.txt)](downloads/Instruction_Gem_Penganalisis_Audit_V6_Kod_Tajuk.txt)
- [Prompt kali pertama V6 Kod Tajuk (.txt)](downloads/Prompt_Kali_Pertama_Analisis_V6_Kod_Tajuk.txt)

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
