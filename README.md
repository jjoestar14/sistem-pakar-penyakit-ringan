# Sistem Pakar Diagnosa Penyakit Ringan

Aplikasi web Sistem Pakar untuk mendiagnosa penyakit ringan menggunakan metode **Forward Chaining** dan **Certainty Factor (CF)**. Dibangun menggunakan Python (Flask) dan antarmuka modern (HTML5, CSS3, Vanilla JS).

## Fitur Utama

- **Forward Chaining**: Pencocokan gejala pengguna dengan rule (aturan pakar).
- **Certainty Factor**: Perhitungan probabilitas/persentase keyakinan diagnosa berdasarkan tingkat keyakinan pengguna dan pakar.
- **Desain Modern**: UI/UX responsif bernuansa soft pink.

## Prasyarat

- Python 3.8+

## Cara Menjalankan di Lokal (Development)

1. Clone repositori atau buka folder project ini.
2. Buat virtual environment (opsional namun disarankan):
   ```bash
   python -m venv venv
   # Di Windows:
   venv\Scripts\activate
   # Di Linux/Mac:
   source venv/bin/activate
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi Flask:
   ```bash
   flask run
   ```
5. Buka browser di alamat `http://127.0.0.1:5000`.

## Cara Menjalankan di Production (Gunicorn)

Gunakan perintah gunicorn yang telah didefinisikan pada `Procfile`:
```bash
gunicorn app:app
```

## Struktur File Utama

- `app.py`: Route utama Flask.
- `engine.py`: Logika sistem pakar (Forward Chaining & CF).
- `knowledge_base.py`: Basis pengetahuan (Gejala, Rule, Penyakit).
- `templates/`: File HTML/Jinja2.
- `static/`: File CSS, JS, dan Gambar (jika ada).
