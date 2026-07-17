initial_facts = [
    "demam", "batuk", "pilek", "bersin", "sakit_kepala",
    "gatal_gatal", "ruam_merah", "mencret", "sakit_perut",
    "mata_merah", "mata_gatal", "mata_berair",
    "hidung_gatal", "hidung_berair"
]

rules = [
    # Flu: batuk + pilek + bersin
    {"premises": ["batuk", "pilek", "bersin"], "conclusion": "flu", "cf_pakar": 0.8},
    # Alergi ringan: hidung berair + hidung gatal (bersin juga sering terjadi)
    {"premises": ["hidung_berair", "hidung_gatal", "bersin"], "conclusion": "alergi_ringan", "cf_pakar": 0.75},
    # Demam ringan: demam + sakit kepala (batuk juga bisa menyertai)
    {"premises": ["demam", "sakit_kepala", "batuk"], "conclusion": "demam_ringan", "cf_pakar": 0.7},
    # Alergi kulit
    {"premises": ["gatal_gatal", "ruam_merah"], "conclusion": "alergi_kulit", "cf_pakar": 0.75},
    # Iritasi mata
    {"premises": ["mata_merah", "mata_gatal", "mata_berair"], "conclusion": "iritasi_mata", "cf_pakar": 0.85},
    # Diare
    {"premises": ["mencret", "sakit_perut"], "conclusion": "diare", "cf_pakar": 0.8},
    # Alergi ringan versi 2: hidung berair + hidung gatal (tanpa bersin)
    {"premises": ["hidung_berair", "hidung_gatal"], "conclusion": "alergi_ringan", "cf_pakar": 0.65},
    # Demam ringan versi 2: demam + sakit kepala (tanpa batuk)
    {"premises": ["demam", "sakit_kepala"], "conclusion": "demam_ringan", "cf_pakar": 0.6},
]

possible_goals = {
    "flu": {
        "nama": "Flu",
        "deskripsi": "Infeksi virus yang menyerang sistem pernapasan (hidung, tenggorokan, dan paru-paru).",
        "gejala_umum": "Batuk, pilek, bersin, terkadang disertai demam ringan.",
        "saran": "Istirahat cukup, perbanyak minum air putih, dan konsumsi obat pereda gejala flu. Jika tidak membaik dalam 3 hari, konsultasikan ke dokter.",
        "icon": "thermometer-snowflake"
    },
    "alergi_kulit": {
        "nama": "Alergi Kulit",
        "deskripsi": "Reaksi sistem kekebalan tubuh terhadap zat tertentu yang menyebabkan masalah pada kulit.",
        "gejala_umum": "Gatal-gatal, ruam merah pada kulit.",
        "saran": "Hindari pemicu alergi, gunakan losion calamine untuk meredakan gatal. Jika ruam menyebar, segera periksa ke dokter.",
        "icon": "bandage"
    },
    "demam_ringan": {
        "nama": "Demam Ringan",
        "deskripsi": "Peningkatan suhu tubuh di atas normal sebagai respons tubuh melawan infeksi.",
        "gejala_umum": "Demam dan sakit kepala.",
        "saran": "Istirahat, kompres air hangat, dan minum paracetamol jika perlu. Pastikan tubuh tetap terhidrasi.",
        "icon": "thermometer"
    },
    "iritasi_mata": {
        "nama": "Iritasi Mata",
        "deskripsi": "Kondisi di mana mata mengalami peradangan akibat debu, kotoran, atau alergi.",
        "gejala_umum": "Mata merah, gatal, dan berair.",
        "saran": "Hindari mengucek mata, gunakan obat tetes mata ringan (air mata buatan). Jika nyeri atau penglihatan kabur, segera ke dokter mata.",
        "icon": "eye"
    },
    "diare": {
        "nama": "Diare",
        "deskripsi": "Gangguan pencernaan yang ditandai dengan buang air besar lebih sering dan encer.",
        "gejala_umum": "Mencret dan sakit perut.",
        "saran": "Perbanyak minum oralit atau air putih untuk mencegah dehidrasi, hindari makanan pedas/asam.",
        "icon": "droplets"
    },
    "alergi_ringan": {
        "nama": "Alergi Ringan (Rhinitis)",
        "deskripsi": "Reaksi alergi pada saluran pernapasan atas, biasanya karena debu, serbuk sari, atau bulu hewan.",
        "gejala_umum": "Hidung berair dan gatal.",
        "saran": "Hindari paparan debu/alergen, gunakan masker saat keluar rumah. Antihistamin ringan dapat membantu.",
        "icon": "flower"
    }
}
