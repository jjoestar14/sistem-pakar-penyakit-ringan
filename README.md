# Sistem Pakar Diagnosa Penyakit Ringan Menggunakan Metode Forward Chaining dan Certainty Factor (CF)

## Nama dan NIM Kelompok :
1.	Muhamad Jakaria // 20241020012
2.	Kelvin Neta Andrea // 20241020018
3.	Dava Dharmansyah // 20241020023
4.	Ridho Ramdhan // 20241020045
5.	Muhammad Hakim // 20241020052

## Deskripsi Aplikasi

MedScreen adalah aplikasi web sistem pakar yang membantu pengguna melakukan skrining awal terhadap penyakit ringan berdasarkan gejala yang dirasakan. Aplikasi ini menggunakan metode Forward Chaining untuk proses penalaran dan Certainty Factor untuk menghitung tingkat keyakinan diagnosis. Hasil yang ditampilkan berupa kemungkinan penyakit beserta persentase keyakinan dan saran penanganan awal.

## Metode Yang Digunakan

- **Forward Chaining**: Sistem memulai proses penalaran dari gejala-gejala yang dipilih pengguna. Gejala tersebut kemudian dicocokkan dengan aturan yang telah dibuat berdasarkan pengetahuan pakar untuk menentukan kemungkinan penyakit yang sesuai.
- **Certainty Factor (CF)**: Metode ini digunakan untuk menghitung tingkat keyakinan hasil diagnosis. Perhitungannya menggabungkan bobot keyakinan dari pakar dengan tingkat keyakinan yang dipilih pengguna, mulai dari “Sedikit Yakin” hingga “Pasti”. Dengan cara ini, hasil yang diberikan menjadi lebih realistis dan tidak bersifat mutlak.
- **Partial & Full Matching**: Sistem tidak hanya menampilkan diagnosis utama ketika semua gejala cocok, tetapi juga dapat memberikan kemungkinan penyakit lain apabila hanya sebagian gejala yang sesuai. Hal ini membantu pengguna memperoleh gambaran yang lebih lengkap mengenai kondisi yang mungkin dialami.

## Cara Penggunaan

1. Buka aplikasi melalui browser.
2. Klik tombol “Mulai Diagnosa” pada halaman utama.
3. Pilih gejala-gejala yang Anda rasakan dengan mencentang kotak yang tersedia.
4. Tentukan tingkat keyakinan Anda terhadap setiap gejala.
5. Klik “Proses Diagnosa”.
6. Sistem akan menampilkan hasil analisis berupa persentase kemungkinan penyakit yang dialami beserta saran penanganan awal.