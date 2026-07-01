from knowledge_base import rules, possible_goals

def combine_cf(cf1, cf2):
    """Menggabungkan dua nilai CF dengan rumus CF1 + CF2 * (1 - CF1)"""
    return cf1 + cf2 * (1 - cf1)

def diagnosa(gejala_terpilih: dict):
    """
    Menjalankan algoritma Forward Chaining dan Certainty Factor.
    gejala_terpilih: dict berisi {nama_gejala: nilai_cf_user}
    """
    hasil_cf = {} # {conclusion: cf_akhir}

    for rule in rules:
        # Cek apakah semua premis (gejala) pada rule ada di gejala_terpilih
        if all(g in gejala_terpilih for g in rule["premises"]):
            # Hitung CF user gabungan (nilai minimum dari semua gejala di premis)
            cf_user_gabungan = min(float(gejala_terpilih[g]) for g in rule["premises"])
            
            # Hitung CF akhir untuk rule ini
            cf_akhir = cf_user_gabungan * rule["cf_pakar"]
            conclusion = rule["conclusion"]

            # Jika sudah ada penyakit yang sama ditemukan di rule lain, gabungkan CF-nya
            if conclusion in hasil_cf:
                hasil_cf[conclusion] = combine_cf(hasil_cf[conclusion], cf_akhir)
            else:
                hasil_cf[conclusion] = cf_akhir

    # Format hasil menjadi list of dictionaries dan urutkan berdasarkan CF tertinggi
    kandidat = []
    for penyakit_id, cf in hasil_cf.items():
        persentase = round(cf * 100, 1)
        kandidat.append({
            "id": penyakit_id,
            "nama": possible_goals[penyakit_id]["nama"],
            "deskripsi": possible_goals[penyakit_id]["deskripsi"],
            "saran": possible_goals[penyakit_id]["saran"],
            "cf": cf,
            "persentase": persentase
        })
    
    kandidat.sort(key=lambda x: x["cf"], reverse=True)
    return kandidat
