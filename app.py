import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from knowledge_base import initial_facts, possible_goals
from engine import diagnosa

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'super_secret_key_diagnosa_ringan')

@app.route('/')
def beranda():
    stats = {
        'penyakit': len(possible_goals),
        'gejala': len(initial_facts)
    }
    return render_template('beranda.html', stats=stats)

@app.route('/diagnosa', methods=['GET'])
def form_diagnosa():
    # Kelompokkan gejala untuk tampilan yang lebih rapi
    kategori_gejala = {
        "Gejala Umum": ["demam", "sakit_kepala"],
        "Gejala Flu & Pernapasan": ["batuk", "pilek", "bersin"],
        "Gejala Kulit": ["gatal_gatal", "ruam_merah"],
        "Gejala Pencernaan": ["mencret", "sakit_perut"],
        "Gejala Mata": ["mata_merah", "mata_gatal", "mata_berair"],
        "Gejala Hidung": ["hidung_gatal", "hidung_berair"]
    }
    
    return render_template('pilih_gejala.html', kategori_gejala=kategori_gejala)

@app.route('/diagnosa/proses', methods=['POST'])
def proses_diagnosa():
    # Mengambil gejala yang dicentang dan nilai CF dari form
    gejala_terpilih = {}
    for key, value in request.form.items():
        if key.startswith('gejala_'):
            gejala = value
            # CF key format: cf_gejala_nama
            cf_key = f'cf_{gejala}'
            cf_val = request.form.get(cf_key, 0.6) # Default ke 0.6 (Yakin) jika tidak ada
            gejala_terpilih[gejala] = float(cf_val)

    if not gejala_terpilih:
        flash("Silakan pilih minimal 1 gejala untuk memulai diagnosa.", "warning")
        return redirect(url_for('form_diagnosa'))

    # Jalankan engine
    hasil = diagnosa(gejala_terpilih)
    
    # Simpan ke session
    session['hasil_diagnosa'] = hasil
    
    return redirect(url_for('hasil_diagnosa'))

@app.route('/diagnosa/hasil')
def hasil_diagnosa():
    if 'hasil_diagnosa' not in session:
        return redirect(url_for('form_diagnosa'))
    
    hasil = session['hasil_diagnosa']
    return render_template('hasil_diagnosa.html', hasil=hasil)

@app.route('/penyakit')
def daftar_penyakit():
    return render_template('daftar_penyakit.html', penyakit=possible_goals)

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

if __name__ == '__main__':
    app.run(debug=True)
