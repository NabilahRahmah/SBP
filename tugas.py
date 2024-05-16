# SISTEM PAKAR DIAGNOSA PENYAKIT PADA BUNGA KRISAN UPAYA PENGENDALIAN
rule_penyakit = {
    'K001': ['G003', 'G018', 'G022', 'G024'],
    'K002': ['G001', 'G002', 'G003', 'G024'],
    'K003': ['G005', 'G011', 'G021', 'G026'],
    'K004': ['G016', 'G020', 'G028', 'G031'],
    'K005': ['G010', 'G012', 'G014'],
    'K006': ['G010', 'G013', 'G016'],
    'K007': ['G001', 'G002', 'G031', 'G033', 'G024'],
    'K008': ['G002', 'G008', 'G010'],
    'K009': ['G002', 'G004', 'G009'],
    'K010': ['G002', 'G004', 'G020'],
    'K011': ['G005', 'G023', 'G025', 'G027'],
    'K012': ['G005', 'G030', 'G033', 'G035'],
    'K013': ['G001', 'G006', 'G010'],
    'K014': ['G001', 'G002', 'G010', 'G018']
}

data_nilai_pakar = {
    'K001': {'G003': 0.7, 'G018': 0.3, 'G022': 0.4, 'G024': 0.2},
    'K002': {'G001': 0.4, 'G002': 0.4, 'G003': 0.7, 'G024': 0.2},
    'K003': {'G005': 0.1, 'G011': 0.4, 'G021': 0.1, 'G026': 0.6},
    'K004': {'G016': 0.1, 'G020': 0.2, 'G028': 0.9, 'G031': 0.1},
    'K005': {'G010': 0.5, 'G012': 0.7, 'G014': 0.1},
    'K006': {'G010': 0.5, 'G013': 0.9, 'G016': 0.1},
    'K007': {'G001': 0.4, 'G002': 0.4, 'G031': 0.1, 'G033': 0.2, 'G024': 0.2},
    'K008': {'G002': 0.4, 'G008': 0.3, 'G010': 0.5},
    'K009': {'G002': 0.4, 'G004': 0.6, 'G009': 0.2},
    'K010': {'G002': 0.4, 'G004': 0.6, 'G020': 0.2},
    'K011': {'G005': 0.1, 'G023': 0.6, 'G025': 0.5, 'G027': 0.2},
    'K012': {'G005': 0.1, 'G030': 0.5, 'G033': 0.2, 'G035': 0.6},
    'K013': {'G001': 0.4, 'G006': 0.2, 'G010': 0.5},
    'K014': {'G001': 0.4, 'G002': 0.4, 'G010': 0.5, 'G018': 0.3},
}

data_gejala = {
    'G001': 'Daun Menguning',
    'G002': 'Daun Mengering',
    'G003': 'Daun Layu dan Gugur',
    'G004': 'Daun Cekung dan Rapuh',
    'G005': 'Daun Kerdil atau Berkerucut',
    'G006': 'Daun Menguning Terutama pada Bagian Bawah',
    'G007': '',
    'G008': 'Daun Tertutupi Lapisan Hitam Seperti Jelaga Hitam',
    'G009': 'Lapisan Tepung pada Permukaan Daun',
    'G010': 'Serangan Pada Daun Bagian Bawah/Seluruh Daun',
    'G011': 'Adanya Bercak-Bercak Daun Bagian Bawah/Seluruh',
    'G012': 'Bintik Kuning Pada Permukaan Atas Daun',
    'G013': 'Bintik Coklat atau Hitam di permukaan atas Daun',
    'G014': 'Bintik Putih Pada Permukaan Bawah Daun',
    'G015': '',
    'G016': 'Terdapat Koloni Puton dibagian Bawah Daun',
    'G017': '',
    'G018': 'Tersisa Hanya Tulang Daun Pada Tanaman',
    'G019': '',
    'G020': 'Bercak Coklat Pada Pinggir Daun',
    'G021':	'Bercak-Bercak Kehitaman Pada Mahkota Bunga',
    'G022':	'Epidermis atau Bagian Atas Daun Rusak/Transparan',
    'G023':	'Tidak Membentuk Tunas Samping',
    'G024':	'Hama Memakan Tunas dan Bunga',
    'G025':	'Berbunga Lebih Awal dari Tanaman Sehat',
    'G026':	'Bunga Bergaris-Garis',
    'G027':	'Warna Bunga Terlihat Pucat',
    'G028':	'Tangkai Bunga yang Pucat',
    'G029':	'',
    'G030': 'Pangkal Batang Membusuk',
    'G031':	'Tanaman Membusuk atau Mati',
    'G032':	'',
    'G033':	'Tanaman Layu',
    'G034':	'Pertumbuhan Angin atas Terhambat',
    'G035':	'Akar Berwarna Coklat Sampai Hitam'
}

data_penyakit = {
    'K001':	'Ulat Grayak',
    'K002':	'Penggrorok daun',
    'K003':	'Thrips',
    'K004':	'Kutu Kebul',
    'K005':	'Karat Putih',
    'K006':	'Karat Hitam',
    'K007':	'Layu Fusarium',
    'K008':	'Virus Kerdil',
    'K009':	'Embun Tepung',
    'K010':	'Hawar Daun',
    'K011':	'Busuk Pangkal',
    'K012':	'Kapang Kelabu',
    'K013':	'Bercak Daun',
    'K014':	'Kapang Daun'
}

# Menampilkan keterangan gejala
print("Keterangan Gejala:")
for kode_gejala, nama_gejala in data_gejala.items():
    print(f"{kode_gejala}: {nama_gejala}")
print()

# Menampilkan keterangan penyakit
print("Keterangan Penyakit:")
for kode_penyakit, nama_penyakit in data_penyakit.items():
    print(f"{kode_penyakit}: {nama_penyakit}")
print()


def hitung_cf(data_nilai_pakar, gejala_terpilih):
    cf_total = {}
    
    # Inisialisasi faktor keyakinan total untuk setiap penyakit
    for penyakit in data_penyakit.keys():
        cf_total[penyakit] = 0.0
    
    # Perhitungan faktor keyakinan untuk setiap penyakit
    for penyakit, gejala_penyakit in rule_penyakit.items():
        for gejala in gejala_terpilih:
            if gejala in gejala_penyakit:
                cf_gejala = data_nilai_pakar[penyakit][gejala]
                if cf_gejala != 0:
                    if cf_gejala >= 0:
                        cf_total[penyakit] = max(cf_total[penyakit], cf_gejala)
                    else:
                        cf_total[penyakit] = max(cf_total[penyakit], -cf_gejala * (1 - cf_total[penyakit]))
    
    return cf_total

def diagnosa_penyakit(gejala_terpilih):
    cf_total = hitung_cf(data_nilai_pakar, gejala_terpilih)
    
    # Menemukan penyakit dengan faktor keyakinan tertinggi
    penyakit_terpilih = max(cf_total, key=cf_total.get)
    faktor_keyakinan_tertinggi = cf_total[penyakit_terpilih]
    
    # Menemukan penyakit yang memiliki faktor keyakinan tertinggi
    penyakit_ditemukan = data_penyakit[penyakit_terpilih]
    
    return penyakit_ditemukan, faktor_keyakinan_tertinggi

def tampilkan_gejala():
    print("Berikut adalah daftar gejala yang mungkin:")
    for kode_gejala, gejala in data_gejala.items():
        print(f"{kode_gejala}: {gejala}")

def main():
    tampilkan_gejala()
    gejala_terpilih = input("\nMasukkan kode gejala yang dialami (pisahkan dengan spasi): ").split()
    
    penyakit, cf = diagnosa_penyakit(gejala_terpilih)
    print("\n======= Hasil Diagnosa =======")
    print("Penyakit yang mungkin:", penyakit)
    print("Faktor Keyakinan:", cf)

if __name__ == "__main__":
    main()