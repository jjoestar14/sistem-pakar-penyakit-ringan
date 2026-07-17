# Sistem Pakar Diagnosa Penyakit Ringan Menggunakan Metode Forward Chaining dan Certainty Factor (CF)

## Nama dan NIM Kelompok :
1.	Muhamad Jakaria // 20241020012
2.	Kelvin Neta Andrea // 20241020018
3.	Dava Dharmansyah // 20241020023
4.	Ridho Ramdhan // 20241020045
5.	Muhammad Hakim // 20241020052

## Deskripsi Aplikasi

MedScreen (Sistem Pakar Diagnosa Penyakit Ringan) adalah sebuah aplikasi berbasis web yang dirancang sebagai alat bantu skrining kesehatan awal secara mandiri untuk mendiagnosa penyakit ringan seperti Flu, Alergi Kulit, Demam Ringan, Iritasi Mata, Diare, dan Alergi Ringan/Rhinitis.

Aplikasi ini bekerja dengan cara mencocokkan gejala-gejala yang dirasakan pengguna serta tingkat keyakinan mereka terhadap gejala tersebut guna menghasilkan diagnosis dengan tingkat akurasi persentase tertentu.

## Metode Yang Digunakan

- **Forward Chaining**: Sistem memulai penalaran dari fakta-fakta (gejala yang dipilih pengguna) lalu mencocokkannya dengan aturan (rules) pakar untuk menarik kesimpulan berupa kemungkinan penyakit.
- **Certainty Factor (CF)**: Mengakomodasi ketidakpastian klinis dengan menghitung persentase keyakinan hasil diagnosis. Perhitungan ini menggabungkan bobot keyakinan dari pakar medis (CF Pakar) dengan tingkat keyakinan subjektif yang dipilih pengguna (CF User seperti "Sedikit Yakin" hingga "Pasti").
- **Partial & Full Matching**: Sistem dapat menyajikan diagnosis utama (gejala cocok sepenuhnya) sekaligus "Kemungkinan Lain" (gejala cocok sebagian) secara proporsional agar hasil analisis lebih informatif bagi pengguna.

## Cara Penggunaan

1. Akses aplikasi melalui browser.
2. Klik tombol "Mulai Diagnosa" pada halaman utama.
3. Pilih gejala-gejala yang Anda rasakan dengan mencentang kotak yang tersedia.
4. Sesuaikan tingkat keyakinan Anda untuk setiap gejala (Sedikit Yakin hingga Pasti).
5. Klik "Proses Diagnosa" untuk mendapatkan hasil.
6. Sistem akan menampilkan persentase kemungkinan penyakit yang Anda alami beserta saran penanganan awal.