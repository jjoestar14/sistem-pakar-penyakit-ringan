from knowledge_base import rules, possible_goals

def combine_cf(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)

def diagnosa(gejala_terpilih: dict):
    hasil_cf = {}
    match_type = {}

    for rule in rules:
        premises = rule["premises"]
        matched = [g for g in premises if g in gejala_terpilih]
        match_count = len(matched)

        if match_count == 0:
            continue

        conclusion = rule["conclusion"]

        if match_count == len(premises):
            cf_user_gabungan = min(float(gejala_terpilih[g]) for g in premises)
            cf_akhir = cf_user_gabungan * rule["cf_pakar"]
            tipe = "full"
        else:
            rasio = match_count / len(premises)
            cf_user_gabungan = min(float(gejala_terpilih[g]) for g in matched)
            cf_akhir = cf_user_gabungan * rule["cf_pakar"] * rasio
            tipe = "partial"
        if conclusion in hasil_cf:
            hasil_cf[conclusion] = combine_cf(hasil_cf[conclusion], cf_akhir)
            if tipe == "full":
                match_type[conclusion] = "full"
        else:
            hasil_cf[conclusion] = cf_akhir
            match_type[conclusion] = tipe

    kandidat = []
    for penyakit_id, cf in hasil_cf.items():
        persentase = round(cf * 100, 1)
        kandidat.append({
            "id": penyakit_id,
            "nama": possible_goals[penyakit_id]["nama"],
            "deskripsi": possible_goals[penyakit_id]["deskripsi"],
            "saran": possible_goals[penyakit_id]["saran"],
            "icon": possible_goals[penyakit_id].get("icon", "activity"),
            "cf": cf,
            "persentase": persentase,
            "tipe_match": match_type.get(penyakit_id, "partial")
        })

    kandidat.sort(key=lambda x: x["cf"], reverse=True)
    return kandidat
