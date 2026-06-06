import streamlit as st
import streamlit as st
import pandas as pd

# Konfigurasi Halaman (Lebar Penuh agar tabel muat)
st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide", page_icon="🧪")

# --- DATASET (GOLONGAN IA & IIA) ---
unsur_data = {
    # GOLONGAN IA
    "H": {"Informasi Dasar": {"Nama": "Hidrogen", "Nomor Atom": 1, "Kategori": "Non-logam", "Massa Atom Relatif": 1.008, "Golongan": "IA", "Periode": 1, "Konfigurasi Elektron": "1s¹", "Tahun Ditemukan": 1766}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif pada suhu tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.08988 g/L"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Asfiksian", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Bahan bakar roket, amonia."},
    "Li": {"Informasi Dasar": {"Nama": "Litium", "Nomor Atom": 3, "Kategori": "Logam Alkali", "Massa Atom Relatif": 6.94, "Golongan": "IA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s¹", "Tahun Ditemukan": 1817}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, mudah teroksidasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.534 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Korosif pada kulit", "Batas Paparan": "0.025 mg/m³"}, "Kegunaan": "Baterai ion-litium."},
    "Na": {"Informasi Dasar": {"Nama": "Natrium", "Nomor Atom": 11, "Kategori": "Logam Alkali", "Massa Atom Relatif": 22.99, "Golongan": "IA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s¹", "Tahun Ditemukan": 1807}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi eksplosif dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.968 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar termal/kimia", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Garam dapur (NaCl)."},
    "K": {"Informasi Dasar": {"Nama": "Kalium", "Nomor Atom": 19, "Kategori": "Logam Alkali", "Massa Atom Relatif": 39.10, "Golongan": "IA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s¹", "Tahun Ditemukan": 1807}, "Sifat Kimia & Fisik": {"Reaktivitas": "Menyala spontan saat kontak air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.862 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar korosif parah", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Pupuk (NPK), sabun cair."},
    "Rb": {"Informasi Dasar": {"Nama": "Rubidium", "Nomor Atom": 37, "Kategori": "Logam Alkali", "Massa Atom Relatif": 85.47, "Golongan": "IA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s¹", "Tahun Ditemukan": 1861}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat eksplosif dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "1.53 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar", "Batas Paparan": "Belum ada"}, "Kegunaan": "Jam atom."},
    "Cs": {"Informasi Dasar": {"Nama": "Sesium", "Nomor Atom": 55, "Kategori": "Logam Alkali", "Massa Atom Relatif": 132.91, "Golongan": "IA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s¹", "Tahun Ditemukan": 1860}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam basa paling reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-Emas", "Massa Jenis": "1.93 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Luka bakar luar biasa", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Cairan pemboran minyak."},
    "Fr": {"Informasi Dasar": {"Nama": "Fransium", "Nomor Atom": 87, "Kategori": "Logam Alkali", "Massa Atom Relatif": 223, "Golongan": "IA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s¹", "Tahun Ditemukan": 1939}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diasumsikan sangat eksplosif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik", "Massa Jenis": "1.87 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi tinggi", "Batas Paparan": "Dilarang terpapar"}, "Kegunaan": "Penelitian medis/nuklir."},
    
    # GOLONGAN IIA
    "Be": {"Informasi Dasar": {"Nama": "Berilium", "Nomor Atom": 4, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 9.012, "Golongan": "IIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s²", "Tahun Ditemukan": 1798}, "Sifat Kimia & Fisik": {"Reaktivitas": "Reaktivitas rendah"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "1.85 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Karsinogenik (Beriliosis)", "Batas Paparan": "0.0002 mg/m³"}, "Kegunaan": "Komponen pesawat ruang angkasa."},
    "Mg": {"Informasi Dasar": {"Nama": "Magnesium", "Nomor Atom": 12, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 24.305, "Golongan": "IIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s²", "Tahun Ditemukan": 1755}, "Sifat Kimia & Fisik": {"Reaktivitas": "Terbakar di udara dengan nyala terang"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu mengkilap", "Massa Jenis": "1.74 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Sangat mudah terbakar", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Velg mobil/pesawat, kembang api."},
    "Ca": {"Informasi Dasar": {"Nama": "Kalsium", "Nomor Atom": 20, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 40.078, "Golongan": "IIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s²", "Tahun Ditemukan": 1808}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-putih", "Massa Jenis": "1.55 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Korosif pada kulit lembab", "Batas Paparan": "2 mg/m³"}, "Kegunaan": "Bahan baku semen dan beton."},
    "Sr": {"Informasi Dasar": {"Nama": "Stronsium", "Nomor Atom": 38, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 87.62, "Golongan": "IIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s²", "Tahun Ditemukan": 1790}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.64 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Isotop Sr-90 radioaktif", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Pewarna merah pada suar."},
    "Ba": {"Informasi Dasar": {"Nama": "Barium", "Nomor Atom": 56, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 137.33, "Golongan": "IIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s²", "Tahun Ditemukan": 1774}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, mudah teroksidasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "3.51 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "🔥, ☠️", "Bahaya Kesehatan": "Garam larut sangat beracun", "Batas Paparan": "0.5 mg/m³"}, "Kegunaan": "Cairan pengeboran minyak."},
    "Ra": {"Informasi Dasar": {"Nama": "Radium", "Nomor Atom": 88, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 226, "Golongan": "IIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s²", "Tahun Ditemukan": 1898}, "Sifat Kimia & Fisik": {"Reaktivitas": "Memancarkan radiasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "5.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kanker tulang", "Batas Paparan": "Sangat ketat"}, "Kegunaan": "Penelitian medis."},

    # GOLONGAN IIIB (3)
    "Sc": {"Informasi Dasar": {"Nama": "Skandium", "Nomor Atom": 21, "Kategori": "Logam Transisi", "Massa Atom Relatif": 44.956, "Golongan": "IIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹ 4s²", "Tahun Ditemukan": 1879}, "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi dengan asam, mudah teroksidasi di udara"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.985 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Debu mudah terbakar", "Batas Paparan": "Belum ditetapkan"}, "Kegunaan": "Paduan aluminium untuk kerangka sepeda dan tongkat bisbol."},
    "Y": {"Informasi Dasar": {"Nama": "Itrium", "Nomor Atom": 39, "Kategori": "Logam Transisi", "Massa Atom Relatif": 88.906, "Golongan": "IIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹ 5s²", "Tahun Ditemukan": 1794}, "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil di udara kering, bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "4.472 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (debu)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Penyakit paru-paru akibat inhalasi debu", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Fosfor merah pada layar TV tabung, laser garnet, superkonduktor."},
    
    # GOLONGAN IVB (4)
    "Ti": {"Informasi Dasar": {"Nama": "Titanium", "Nomor Atom": 22, "Kategori": "Logam Transisi", "Massa Atom Relatif": 47.867, "Golongan": "IVB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d² 4s²", "Tahun Ditemukan": 1791}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi (membentuk lapisan oksida pelindung)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik", "Massa Jenis": "4.506 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅ (Non-B3)", "Bahaya Kesehatan": "Secara biologis inert, sangat aman untuk tubuh", "Batas Paparan": "10 mg/m³ (debu)"}, "Kegunaan": "Implan medis/tulang, bodi pesawat terbang, pigmen putih (TiO2)."},
    "Zr": {"Informasi Dasar": {"Nama": "Zirkonium", "Nomor Atom": 40, "Kategori": "Logam Transisi", "Massa Atom Relatif": 91.224, "Golongan": "IVB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d² 5s²", "Tahun Ditemukan": 1789}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi, tidak bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keputihan", "Massa Jenis": "6.52 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuk halus mudah menyala secara spontan di udara", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Selongsong bahan bakar reaktor nuklir, permata sintetis (Cubic Zirconia)."},
    "Hf": {"Informasi Dasar": {"Nama": "Hafnium", "Nomor Atom": 72, "Kategori": "Logam Transisi", "Massa Atom Relatif": 178.49, "Golongan": "IVB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d² 6s²", "Tahun Ditemukan": 1923}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat mirip zirkonium, menyerap neutron sangat baik"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "13.31 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "🔥", "Bahaya Kesehatan": "Bubuknya mudah terbakar/eksplosif", "Batas Paparan": "0.5 mg/m³"}, "Kegunaan": "Batang kendali reaktor nuklir, mikroprosesor (chip komputer)."},

    # GOLONGAN VB (5)
    "V": {"Informasi Dasar": {"Nama": "Vanadium", "Nomor Atom": 23, "Kategori": "Logam Transisi", "Massa Atom Relatif": 50.941, "Golongan": "VB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d³ 4s²", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan terhadap basa, asam sulfat, dan asam klorida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan muda", "Massa Jenis": "6.11 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (senyawanya)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Beracun jika terhirup (V2O5)", "Batas Paparan": "0.05 mg/m³"}, "Kegunaan": "Campuran baja tahan karat (perkakas, kunci pas, as roda)."},
    "Nb": {"Informasi Dasar": {"Nama": "Niobium", "Nomor Atom": 41, "Kategori": "Logam Transisi", "Massa Atom Relatif": 92.906, "Golongan": "VB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁴ 5s¹", "Tahun Ditemukan": 1801}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada suhu ruang, mengoksidasi pada suhu tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "8.57 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi mata dan kulit (debu)", "Batas Paparan": "Belum ada standar khusus"}, "Kegunaan": "Baja paduan untuk pipa gas, superkonduktor dalam pemindai MRI."},
    "Ta": {"Informasi Dasar": {"Nama": "Tantalum", "Nomor Atom": 73, "Kategori": "Logam Transisi", "Massa Atom Relatif": 180.95, "Golongan": "VB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d³ 6s²", "Tahun Ditemukan": 1802}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan terhadap serangan zat kimia pada suhu di bawah 150°C"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu kebiruan terang", "Massa Jenis": "16.69 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅ (Non-B3)", "Bahaya Kesehatan": "Biokompatibel (tidak bereaksi dengan cairan tubuh)", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Kapasitor pada ponsel pintar (smartphone), peralatan bedah."},

    # GOLONGAN VIB (6)
    "Cr": {"Informasi Dasar": {"Nama": "Kromium", "Nomor Atom": 24, "Kategori": "Logam Transisi", "Massa Atom Relatif": 51.996, "Golongan": "VIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s¹", "Tahun Ditemukan": 1797}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tahan korosi, tidak bereaksi dengan air"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak metalik keras", "Massa Jenis": "7.19 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Kromium Heksavalen / Cr VI)", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Cr(VI) sangat karsinogenik dan mematikan. Cr(III) esensial bagi tubuh.", "Batas Paparan": "0.005 mg/m³ (Cr VI)"}, "Kegunaan": "Baja tahan karat (stainless steel), pelapisan krom pelindung kendaraan."},
    "Mo": {"Informasi Dasar": {"Nama": "Molibdenum", "Nomor Atom": 42, "Kategori": "Logam Transisi", "Massa Atom Relatif": 95.95, "Golongan": "VIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s¹", "Tahun Ditemukan": 1778}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tidak larut dalam asam klorida dan asam fluorida"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "10.28 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Toksisitas rendah, tetapi hindari paparan kronis debunya", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Filamen listrik, paduan pemanas untuk mesin jet, pupuk tanaman."},
    "W": {"Informasi Dasar": {"Nama": "Tungsten (Wolfram)", "Nomor Atom": 74, "Kategori": "Logam Transisi", "Massa Atom Relatif": 183.84, "Golongan": "VIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁴ 6s²", "Tahun Ditemukan": 1783}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat kuat dan inert; titik lebur tertinggi di antara semua logam"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keabu-abuan", "Massa Jenis": "19.25 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅ (Non-B3)", "Bahaya Kesehatan": "Aman untuk dipegang, tetapi senyawa terlarutnya sedikit beracun", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Filamen bola lampu pijar, mata bor berat bermaterial Tungsten Carbide."},

    # GOLONGAN VIIB (7)
    "Mn": {"Informasi Dasar": {"Nama": "Mangan", "Nomor Atom": 25, "Kategori": "Logam Transisi", "Massa Atom Relatif": 54.938, "Golongan": "VIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁵ 4s²", "Tahun Ditemukan": 1774}, "Sifat Kimia & Fisik": {"Reaktivitas": "Perlahan teroksidasi di udara, berkarat di air seperti besi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan padat", "Massa Jenis": "7.21 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Inhalasi debu terus-menerus memicu kerusakan saraf pusat (Manganisme).", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Paduan rel kereta api (baja keras), baterai alkaline."},
    "Tc": {"Informasi Dasar": {"Nama": "Teknesium", "Nomor Atom": 43, "Kategori": "Logam Transisi", "Massa Atom Relatif": 98, "Golongan": "VIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁵ 5s²", "Tahun Ditemukan": 1937}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi, larut dalam asam nitrat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "11.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Semua isotop bersifat radioaktif", "Batas Paparan": "Ditangani di lab radioisotop"}, "Kegunaan": "Pelacak radiodiagnostik tulang dan alat ukur pemindai medis (Isotop Tc-99m)."},
    "Re": {"Informasi Dasar": {"Nama": "Renium", "Nomor Atom": 75, "Kategori": "Logam Transisi", "Massa Atom Relatif": 186.21, "Golongan": "VIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁵ 6s²", "Tahun Ditemukan": 1925}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi parah, stabil secara mekanik pada suhu ekstrim"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan cerah", "Massa Jenis": "21.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya dalam wujud aslinya", "Batas Paparan": "Belum ditentukan"}, "Kegunaan": "Superalloy suhu tinggi untuk mesin pesawat tempur jet."},

    # GOLONGAN VIIIB (8, 9, 10)
    "Fe": {"Informasi Dasar": {"Nama": "Besi", "Nomor Atom": 26, "Kategori": "Logam Transisi", "Massa Atom Relatif": 55.845, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁶ 4s²", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mudah berkarat saat terkena kelembapan dan oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak berkilau keabu-abuan", "Massa Jenis": "7.874 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Penting bagi darah)", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Kelebihan zat besi menyebabkan kerusakan hati (Hemokromatosis).", "Batas Paparan": "5 mg/m³ (sebagai asap oksida)"}, "Kegunaan": "Tulang punggung infrastruktur (baja, jembatan, bangunan, hemoglobin darah)."},
    "Ru": {"Informasi Dasar": {"Nama": "Rutenium", "Nomor Atom": 44, "Kategori": "Logam Transisi", "Massa Atom Relatif": 101.07, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁷ 5s¹", "Tahun Ditemukan": 1844}, "Sifat Kimia & Fisik": {"Reaktivitas": "Inert pada sebagian besar bahan kimia, sangat keras"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik keperakan", "Massa Jenis": "12.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Senyawa)", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Rutenium tetroksida (RuO4) sangat beracun dan menodai kulit.", "Batas Paparan": "Belum ada"}, "Kegunaan": "Kontak listrik tahan aus, ujung pulpen mahal (dicampur platinum/osmium)."},
    "Os": {"Informasi Dasar": {"Nama": "Osmium", "Nomor Atom": 76, "Kategori": "Logam Transisi", "Massa Atom Relatif": 190.23, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁶ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat keras dan rapuh, bereaksi lambat dengan oksigen"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik kebiruan", "Massa Jenis": "22.59 g/cm³ (Unsur paling padat di Bumi)"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Oksidanya)", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Osmium tetroksida menguap di udara, menyebabkan kebutaan dan kematian.", "Batas Paparan": "0.002 mg/m³"}, "Kegunaan": "Jarum pemutar piringan hitam, poros instrumen (karena kekerasannya yang ekstrim)."},
    "Co": {"Informasi Dasar": {"Nama": "Kobal", "Nomor Atom": 27, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.933, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁷ 4s²", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Feromagnetik, bereaksi pelan dengan udara basah"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak abu-abu mengkilap", "Massa Jenis": "8.90 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Iritan paru-paru dan karsinogen potensial; penting untuk Vitamin B12.", "Batas Paparan": "0.02 mg/m³"}, "Kegunaan": "Baterai Lithium-ion (EV, smartphone), paduan turbin gas suhu tinggi."},
    "Rh": {"Informasi Dasar": {"Nama": "Rodium", "Nomor Atom": 45, "Kategori": "Logam Transisi", "Massa Atom Relatif": 102.91, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d⁸ 5s¹", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Salah satu logam mulia paling tidak reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan, memantulkan cahaya kuat", "Massa Jenis": "12.41 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Sebagai logam murni)", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya dalam wujud aslinya", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Konverter katalitik mobil (pembersih asap knalpot), perhiasan mahal."},
    "Ir": {"Informasi Dasar": {"Nama": "Iridium", "Nomor Atom": 77, "Kategori": "Logam Transisi", "Massa Atom Relatif": 192.22, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁷ 6s²", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam paling tahan korosi di dunia"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih kekuningan terang", "Massa Jenis": "22.56 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Serbuk iridium bisa menjadi iritan sekunder, bentuk balok sangat aman.", "Batas Paparan": "Belum ditetapkan"}, "Kegunaan": "Busi berperforma tinggi, ujung kompas, standar meteran dan kilogram awal."},
    "Ni": {"Informasi Dasar": {"Nama": "Nikel", "Nomor Atom": 28, "Kategori": "Logam Transisi", "Massa Atom Relatif": 58.693, "Golongan": "VIIIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d⁸ 4s²", "Tahun Ditemukan": 1751}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi tinggi (feromagnetik ringan)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan sedikit kuning emas", "Massa Jenis": "8.908 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️, 🫁", "Bahaya Kesehatan": "Pemicu alergi kontak tersering pada perhiasan tiruan, debu bersifat karsinogen.", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Baterai rechargable, paduan koin, pelapisan pelindung, baja stainless."},
    "Pd": {"Informasi Dasar": {"Nama": "Paladium", "Nomor Atom": 46, "Kategori": "Logam Transisi", "Massa Atom Relatif": 106.42, "Golongan": "VIIIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰", "Tahun Ditemukan": 1803}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mampu menyerap gas hidrogen hingga 900 kali volume dirinya"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan baja", "Massa Jenis": "12.02 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Logam aslinya aman, senyawanya dapat menyebabkan iritasi mata.", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Konverter katalitik pengurang emisi mobil, perhiasan emas putih, elektronik."},
    "Pt": {"Informasi Dasar": {"Nama": "Platina", "Nomor Atom": 78, "Kategori": "Logam Transisi", "Massa Atom Relatif": 195.08, "Golongan": "VIIIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d⁹ 6s¹", "Tahun Ditemukan": 1735}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat lembam (inert), tidak berkarat pada suhu berapa pun"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih metalik", "Massa Jenis": "21.45 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Non-toksik dalam bentuk logam. Beberapa senyawa digunakan sebagai obat kemoterapi.", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Perhiasan elit, obat kemoterapi (Cisplatin), alat pacu jantung."},

    # GOLONGAN IVB (Periode 7)
    "Rf": {
        "Informasi Dasar": {"Nama": "Rutherfordium", "Nomor Atom": 104, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "267 (estimasi)", "Golongan": "IVB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d² 7s²", "Tahun Ditemukan": 1964},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Hafnium dan Zirkonium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "23.2 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Hanya ada di laboratorium nuklir"},
        "Kegunaan": "Hanya untuk penelitian ilmiah dan eksperimen fisika partikel."
    },
    
    # GOLONGAN VB (Periode 7)
    "Db": {
        "Informasi Dasar": {"Nama": "Dubnium", "Nomor Atom": 105, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "268 (estimasi)", "Golongan": "VB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d³ 7s²", "Tahun Ditemukan": 1967},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Tantalum"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "29.3 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Hanya diproduksi beberapa atom dalam satu waktu"},
        "Kegunaan": "Hanya untuk penelitian ilmiah murni."
    },
    
    # GOLONGAN VIB (Periode 7)
    "Sg": {
        "Informasi Dasar": {"Nama": "Seaborgium", "Nomor Atom": 106, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "269 (estimasi)", "Golongan": "VIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁴ 7s²", "Tahun Ditemukan": 1974},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi membentuk oksida asam mirip dengan Tungsten"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "35.0 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Eksperimen laboratorium berpelindung ketat"},
        "Kegunaan": "Hanya untuk penelitian ilmiah."
    },
    
    # GOLONGAN VIIB (Periode 7)
    "Bh": {
        "Informasi Dasar": {"Nama": "Bohrium", "Nomor Atom": 107, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "270 (estimasi)", "Golongan": "VIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁵ 7s²", "Tahun Ditemukan": 1981},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Renium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "37.1 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Tidak diterapkan secara umum"},
        "Kegunaan": "Penelitian ilmiah (sifat kimianya sangat sulit diuji karena meluruh terlalu cepat)."
    },
    
    # GOLONGAN VIIIB (Periode 7)
    "Hs": {
        "Informasi Dasar": {"Nama": "Hassium", "Nomor Atom": 108, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "277 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁶ 7s²", "Tahun Ditemukan": 1984},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diketahui membentuk Hassium tetroksida (HsO4) yang sangat mudah menguap, mirip Osmium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "40.7 g/cm³ (Diprediksi - mungkin unsur terpadat)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi ionisasi ekstrem", "Batas Paparan": "Hanya untuk ahli fisika nuklir"},
        "Kegunaan": "Penelitian ilmiah murni."
    },
    "Mt": {
        "Informasi Dasar": {"Nama": "Meitnerium", "Nomor Atom": 109, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "278 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁷ 7s²", "Tahun Ditemukan": 1982},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi merupakan logam mulia mirip Iridium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "37.4 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi tinggi (meluruh dalam milidetik)", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Tidak ada kegunaan komersial, hanya eksperimen percepatan partikel."
    },
    "Ds": {
        "Informasi Dasar": {"Nama": "Darmstadtium", "Nomor Atom": 110, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "281 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁸ 7s² (Diprediksi)", "Tahun Ditemukan": 1994},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi sangat tidak reaktif, mirip Platina"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Putih keperakan (Diprediksi)", "Massa Jenis": "34.8 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Meluruh terlalu cepat untuk berdampak secara kimiawi, bahaya murni dari radiasi", "Batas Paparan": "Siklotron/pemercepat partikel eksklusif"},
        "Kegunaan": "Memperluas pemahaman manusia tentang nukleus dan tabel periodik.",
    },
    # GOLONGAN IVB (Periode 7)
    "Rf": {
        "Informasi Dasar": {"Nama": "Rutherfordium", "Nomor Atom": 104, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "267 (estimasi)", "Golongan": "IVB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d² 7s²", "Tahun Ditemukan": 1964},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Hafnium dan Zirkonium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "23.2 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Hanya ada di laboratorium nuklir"},
        "Kegunaan": "Hanya untuk penelitian ilmiah dan eksperimen fisika partikel."
    },
    
    # GOLONGAN VB (Periode 7)
    "Db": {
        "Informasi Dasar": {"Nama": "Dubnium", "Nomor Atom": 105, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "268 (estimasi)", "Golongan": "VB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d³ 7s²", "Tahun Ditemukan": 1967},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Tantalum"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "29.3 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Hanya diproduksi beberapa atom dalam satu waktu"},
        "Kegunaan": "Hanya untuk penelitian ilmiah murni."
    },
    
    # GOLONGAN VIB (Periode 7)
    "Sg": {
        "Informasi Dasar": {"Nama": "Seaborgium", "Nomor Atom": 106, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "269 (estimasi)", "Golongan": "VIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁴ 7s²", "Tahun Ditemukan": 1974},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi membentuk oksida asam mirip dengan Tungsten"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "35.0 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Eksperimen laboratorium berpelindung ketat"},
        "Kegunaan": "Hanya untuk penelitian ilmiah."
    },
    
    # GOLONGAN VIIB (Periode 7)
    "Bh": {
        "Informasi Dasar": {"Nama": "Bohrium", "Nomor Atom": 107, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "270 (estimasi)", "Golongan": "VIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁵ 7s²", "Tahun Ditemukan": 1981},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi mirip dengan Renium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "37.1 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Paparan radiasi mematikan", "Batas Paparan": "Tidak diterapkan secara umum"},
        "Kegunaan": "Penelitian ilmiah (sifat kimianya sangat sulit diuji karena meluruh terlalu cepat)."
    },
    
    # GOLONGAN VIIIB (Periode 7)
    "Hs": {
        "Informasi Dasar": {"Nama": "Hassium", "Nomor Atom": 108, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "277 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁶ 7s²", "Tahun Ditemukan": 1984},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diketahui membentuk Hassium tetroksida (HsO4) yang sangat mudah menguap, mirip Osmium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "40.7 g/cm³ (Diprediksi - mungkin unsur terpadat)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi ionisasi ekstrem", "Batas Paparan": "Hanya untuk ahli fisika nuklir"},
        "Kegunaan": "Penelitian ilmiah murni."
    },
    "Mt": {
        "Informasi Dasar": {"Nama": "Meitnerium", "Nomor Atom": 109, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "278 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁷ 7s²", "Tahun Ditemukan": 1982},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi merupakan logam mulia mirip Iridium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "37.4 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi tinggi (meluruh dalam milidetik)", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Tidak ada kegunaan komersial, hanya eksperimen percepatan partikel."
    },
    "Ds": {
        "Informasi Dasar": {"Nama": "Darmstadtium", "Nomor Atom": 110, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "281 (estimasi)", "Golongan": "VIIIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d⁸ 7s² (Diprediksi)", "Tahun Ditemukan": 1994},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi sangat tidak reaktif, mirip Platina"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Putih keperakan (Diprediksi)", "Massa Jenis": "34.8 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Meluruh terlalu cepat untuk berdampak secara kimiawi, bahaya murni dari radiasi", "Batas Paparan": "Siklotron/pemercepat partikel eksklusif"},
        "Kegunaan": "Memperluas pemahaman manusia tentang nukleus dan tabel periodik."
    },
    # GOLONGAN IB (11)
    "Cu": {"Informasi Dasar": {"Nama": "Tembaga", "Nomor Atom": 29, "Kategori": "Logam Transisi", "Massa Atom Relatif": 63.546, "Golongan": "IB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s¹", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Tidak reaktif terhadap air, konduktor listrik yang sangat baik"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Merah-oranye metalik", "Massa Jenis": "8.96 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Esensial bagi tubuh, tetapi racun dalam dosis tinggi", "Batas Paparan": "1 mg/m³ (debu)"}, "Kegunaan": "Kabel listrik, pipa air, koin, paduan perunggu dan kuningan."},
    "Ag": {"Informasi Dasar": {"Nama": "Perak", "Nomor Atom": 47, "Kategori": "Logam Transisi", "Massa Atom Relatif": 107.87, "Golongan": "IB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s¹", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Logam mulia, konduktivitas termal dan listrik tertinggi dari semua logam"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan mengkilap", "Massa Jenis": "10.49 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Paparan kronis dapat menyebabkan Argyria (kulit membiru)", "Batas Paparan": "0.1 mg/m³"}, "Kegunaan": "Perhiasan, panel surya, cermin, kontak listrik, fotografi (dulu)."},
    "Au": {"Informasi Dasar": {"Nama": "Emas", "Nomor Atom": 79, "Kategori": "Logam Transisi", "Massa Atom Relatif": 196.97, "Golongan": "IB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s¹", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat inert (tidak reaktif), hanya larut dalam air raja (aqua regia)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Kuning keemasan", "Massa Jenis": "19.30 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman dan sering digunakan pada gigi atau makanan (gold leaf)", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Perhiasan, investasi ekonomi, konektor elektronik anti-karat."},
    "Rg": {"Informasi Dasar": {"Nama": "Roentgenium", "Nomor Atom": 111, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "282 (estimasi)", "Golongan": "IB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s¹ (Diprediksi)", "Tahun Ditemukan": 1994}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi sebagai logam mulia yang sangat reaktif"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Keperakan/Emas (Diprediksi)", "Massa Jenis": "28.7 g/cm³ (Diprediksi)"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi murni", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Penelitian ilmiah."},

    # GOLONGAN IIB (12)
    "Zn": {"Informasi Dasar": {"Nama": "Seng", "Nomor Atom": 30, "Kategori": "Logam Transisi", "Massa Atom Relatif": 65.38, "Golongan": "IIB", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s²", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif, terbakar dengan nyala biru kehijauan"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu kebiruan", "Massa Jenis": "7.14 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Menghirup asap oksida seng menyebabkan 'demam asap logam'", "Batas Paparan": "5 mg/m³"}, "Kegunaan": "Pelapisan anti-karat (galvanisasi), paduan kuningan, baterai."},
    "Cd": {"Informasi Dasar": {"Nama": "Kadmium", "Nomor Atom": 48, "Kategori": "Logam Transisi", "Massa Atom Relatif": 112.41, "Golongan": "IIB", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s²", "Tahun Ditemukan": 1817}, "Sifat Kimia & Fisik": {"Reaktivitas": "Mirip dengan seng, tahan korosi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan dengan rona kebiruan", "Massa Jenis": "8.65 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Karsinogenik, merusak ginjal dan tulang (penyakit Itai-Itai)", "Batas Paparan": "0.01 mg/m³"}, "Kegunaan": "Baterai isi ulang (Ni-Cd), pigmen kuning/merah, pelapisan logam."},
    "Hg": {"Informasi Dasar": {"Nama": "Raksa (Merkuri)", "Nomor Atom": 80, "Kategori": "Logam Transisi", "Massa Atom Relatif": 200.59, "Golongan": "IIB", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s²", "Tahun Ditemukan": "Zaman Kuno"}, "Sifat Kimia & Fisik": {"Reaktivitas": "Satu-satunya logam yang cair pada suhu ruang, melarutkan emas (amalgam)"}, "Wujud Fisik": {"Wujud (25°C)": "Cair", "Warna": "Perak mengkilap", "Massa Jenis": "13.53 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Uapnya merusak sistem saraf pusat fatal (Penyakit Minamata)", "Batas Paparan": "0.025 mg/m³"}, "Kegunaan": "Termometer lawas, lampu neon, amalgam gigi, penambangan emas."},
    "Cn": {"Informasi Dasar": {"Nama": "Kopernisium", "Nomor Atom": 112, "Kategori": "Logam Transisi (Superberat)", "Massa Atom Relatif": "285 (estimasi)", "Golongan": "IIB", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s²", "Tahun Ditemukan": 1996}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat volatil, diprediksi berbentuk gas atau cair pada suhu ruang"}, "Wujud Fisik": {"Wujud (25°C)": "Cair/Gas (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "23.7 g/cm³ (Diprediksi)"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Berbahaya secara radiologis", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Penelitian ilmiah."},

    # GOLONGAN IIIA (13)
    "B": {"Informasi Dasar": {"Nama": "Boron", "Nomor Atom": 5, "Kategori": "Metaloid", "Massa Atom Relatif": 10.81, "Golongan": "IIIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p¹", "Tahun Ditemukan": 1808}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat keras, semikonduktor suhu tinggi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Hitam-coklat", "Massa Jenis": "2.34 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Beracun jika tertelan dalam jumlah besar", "Batas Paparan": "10 mg/m³"}, "Kegunaan": "Kaca tahan panas (Borosilikat/Pyrex), sabun cuci, pengontrol reaktor nuklir."},
    "Al": {"Informasi Dasar": {"Nama": "Aluminium", "Nomor Atom": 13, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 26.982, "Golongan": "IIIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p¹", "Tahun Ditemukan": 1825}, "Sifat Kimia & Fisik": {"Reaktivitas": "Membentuk lapisan oksida kuat yang melindunginya dari karat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "2.70 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Debu halusnya dapat memicu masalah paru-paru", "Batas Paparan": "1 mg/m³"}, "Kegunaan": "Badan pesawat terbang, kaleng minuman, kertas foil, kabel listrik."},
    "Ga": {"Informasi Dasar": {"Nama": "Galium", "Nomor Atom": 31, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 69.723, "Golongan": "IIIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 3p¹", "Tahun Ditemukan": 1875}, "Sifat Kimia & Fisik": {"Reaktivitas": "Meleleh pada suhu yang sangat rendah (29.76°C, bisa meleleh di telapak tangan)"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Perak kebiruan", "Massa Jenis": "5.91 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Dapat menyebabkan iritasi kulit/mata", "Batas Paparan": "Belum ditentukan"}, "Kegunaan": "Semikonduktor canggih (GaAs) untuk LED, laser, dan radar."},
    "In": {"Informasi Dasar": {"Nama": "Indium", "Nomor Atom": 49, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 114.82, "Golongan": "IIIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p¹", "Tahun Ditemukan": 1863}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat lembut, dapat dipotong dengan pisau dan meninggalkan 'jejak' di kertas"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan mengkilap", "Massa Jenis": "7.31 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Sedikit beracun, hindari konsumsi", "Batas Paparan": "0.1 mg/m³"}, "Kegunaan": "Lapisan konduktif transparan pada layar sentuh (LCD/OLED), solder khusus."},
    "Tl": {"Informasi Dasar": {"Nama": "Talium", "Nomor Atom": 81, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 204.38, "Golongan": "IIIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "Tahun Ditemukan": 1861}, "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif di udara lembab, teroksidasi dengan cepat"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan (menghitam di udara)", "Massa Jenis": "11.85 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Sangat beracun, menyebabkan rambut rontok dan kerusakan saraf fatal", "Batas Paparan": "0.1 mg/m³"}, "Kegunaan": "Elektronik optik inframerah, sebelumnya digunakan sebagai racun tikus (kini dilarang)."},
    "Nh": {"Informasi Dasar": {"Nama": "Nihonium", "Nomor Atom": 113, "Kategori": "Logam Pasca-Transisi (Superberat)", "Massa Atom Relatif": "286 (estimasi)", "Golongan": "IIIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹ (Diprediksi)", "Tahun Ditemukan": 2003}, "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi kurang reaktif dibanding unsur di atasnya"}, "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "16 g/cm³ (Diprediksi)"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi murni", "Batas Paparan": "Tidak ada"}, "Kegunaan": "Hanya untuk keperluan penelitian ilmiah murni."},

    # GOLONGAN IVA (14) - KELOMPOK KARBON
    "C": {
        "Informasi Dasar": {"Nama": "Karbon", "Nomor Atom": 6, "Kategori": "Non-logam", "Massa Atom Relatif": 12.011, "Golongan": "IVA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p²", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Mampu membentuk rantai polimer panjang (dasar kehidupan organik)"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Hitam (Grafit) / Bening (Intan)", "Massa Jenis": "2.26 g/cm³ (Grafit)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman, tetapi debu grafit dosis tinggi mengiritasi paru-paru", "Batas Paparan": "2 mg/m³ (debu)"},
        "Kegunaan": "Intan perhiasan, pensil grafit, filter arang aktif, serat karbon otomotif."
    },
    "Si": {
        "Informasi Dasar": {"Nama": "Silikon", "Nomor Atom": 14, "Kategori": "Metaloid", "Massa Atom Relatif": 28.085, "Golongan": "IVA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p²", "Tahun Ditemukan": 1824},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup lembam pada suhu kamar, larut dalam asam campuran"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu gelap mengkilap", "Massa Jenis": "2.33 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Inhalasi debu silika kronis menyebabkan Silikosis", "Batas Paparan": "0.025 mg/m³ (silika respirabel)"},
        "Kegunaan": "Bahan utama cip komputer (mikroprosesor), panel surya, kaca, lem silikon."
    },
    "Ge": {
        "Informasi Dasar": {"Nama": "Germanium", "Nomor Atom": 32, "Kategori": "Metaloid", "Massa Atom Relatif": 72.63, "Golongan": "IVA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 4p²", "Tahun Ditemukan": 1886},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil di udara dan air, bereaksi dengan asam pekat"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keabu-abuan berkilau", "Massa Jenis": "5.32 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Tidak berbahaya secara industri", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Lensa optik inframerah (kamera malam), serat optik telekomunikasi, transistor."
    },
    "Sn": {
        "Informasi Dasar": {"Nama": "Timah", "Nomor Atom": 50, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 118.71, "Golongan": "IVA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p²", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Tahan korosi air laut, tidak mudah teroksidasi"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih perak kemilau", "Massa Jenis": "7.31 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Logam)", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Senyawa timah organik bisa beracun bagi saraf", "Batas Paparan": "2 mg/m³"},
        "Kegunaan": "Pelapis kaleng makanan anti-karat, kawat solder elektronik, logam perunggu."
    },
    "Pb": {
        "Informasi Dasar": {"Nama": "Timbal", "Nomor Atom": 82, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 207.2, "Golongan": "IVA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat lambat bereaksi dengan asam sulfat dan klorida"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu kebiruan kusam", "Massa Jenis": "11.34 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Akumulasi logam berat merusak otak dan ginjal (Plumbisme)", "Batas Paparan": "0.05 mg/m³"},
        "Kegunaan": "Aki kendaraan bermotor, pelindung radiasi sinar-X, beban pancing."
    },
    "Fl": {
        "Informasi Dasar": {"Nama": "Flerovium", "Nomor Atom": 114, "Kategori": "Logam Pasca-Transisi (Superberat)", "Massa Atom Relatif": "289 (estimasi)", "Golongan": "IVA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p² (Diprediksi)", "Tahun Ditemukan": 1998},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Diprediksi menunjukkan sifat gas mulia karena efek relativistik"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "14 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi tinggi", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Hanya untuk penelitian ilmiah dan fisika nuklir."
    },

    # GOLONGAN VA (15) - KELOMPOK NITROGEN (PNIKTOGEN)
    "N": {
        "Informasi Dasar": {"Nama": "Nitrogen", "Nomor Atom": 7, "Kategori": "Non-logam", "Massa Atom Relatif": 14.007, "Golongan": "VA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p³", "Tahun Ditemukan": 1772},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tidak reaktif (inert) dalam wujud gas diatomik ($N_2$)"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "1.25 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️ (Gas bertekanan)", "Bahaya Kesehatan": "Dapat memicu asfiksia jika menggantikan oksigen di ruangan tertutup", "Batas Paparan": "Suhu kriogenik cair berbahaya bagi kulit"},
        "Kegunaan": "Pupuk urea, pengawetan makanan kemasan, nitrogen cair pembeku medis."
    },
    "P": {
        "Informasi Dasar": {"Nama": "Fosfor", "Nomor Atom": 15, "Kategori": "Non-logam", "Massa Atom Relatif": 30.974, "Golongan": "VA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p³", "Tahun Ditemukan": 1669},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Fosfor putih sangat reaktif dan terbakar spontan di udara"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih kekuningan / Merah", "Massa Jenis": "1.82 g/cm³ (Fosfor putih)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Fosfor Putih)", "Piktogram GHS": "☠️, 🔥", "Bahaya Kesehatan": "Fosfor putih menyebabkan luka bakar parah dan nekrosis tulang rahang", "Batas Paparan": "0.1 mg/m³"},
        "Kegunaan": "Kepala korek api (fosfor merah), pupuk fosfat, bahan peledak flare."
    },
    "As": {
        "Informasi Dasar": {"Nama": "Arsenik", "Nomor Atom": 33, "Kategori": "Metaloid", "Massa Atom Relatif": 74.922, "Golongan": "VA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 4p³", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Menyublim saat dipanaskan, membentuk senyawa arsen oksida beracun"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik", "Massa Jenis": "5.73 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Racun sistemik mematikan, karsinogenik kuat", "Batas Paparan": "0.01 mg/m³"},
        "Kegunaan": "Pestisida pertanian (dulu), pengeras paduan timbal, semikonduktor."
    },
    "Sb": {
        "Informasi Dasar": {"Nama": "Antimon", "Nomor Atom": 51, "Kategori": "Metaloid", "Massa Atom Relatif": 121.76, "Golongan": "VA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p³", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Lambat diserang asam encer, bereaksi cepat dengan halogen"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu perak berkilau", "Massa Jenis": "6.69 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang - Tinggi", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Iritasi parah pada saluran pernapasan dan kulit", "Batas Paparan": "0.5 mg/m³"},
        "Kegunaan": "Bahan penghambat api (flame retardant), pengeras peluru, dioda elektronik."
    },
    "Bi": {
        "Informasi Dasar": {"Nama": "Bismut", "Nomor Atom": 83, "Kategori": "Logam Pasca-Transisi", "Massa Atom Relatif": 208.98, "Golongan": "VA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Logam berat paling aman, lambat teroksidasi di udara membentuk lapisan warna-warni"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan dengan semburat merah muda", "Massa Jenis": "9.78 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Rendah", "Piktogram GHS": "✅", "Bahaya Kesehatan": "Aman digunakan, toksisitas terendah dibanding tetangganya", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Bahan aktif obat sakit perut (Pepto-Bismol), kosmetik, pengganti timbal ramah lingkungan."
    },
    "Mc": {
        "Informasi Dasar": {"Nama": "Moscovium", "Nomor Atom": 115, "Kategori": "Logam Pasca-Transisi (Superberat)", "Massa Atom Relatif": "290 (estimasi)", "Golongan": "VA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³ (Diprediksi)", "Tahun Ditemukan": 2003},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sifat kimia belum banyak diketahui karena kelimpahan atom yang sangat sedikit"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "13.5 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Risiko kerusakan radiasi ekstrem", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Hanya untuk kepentingan studi ilmiah laboratorium fisika partikel."
    },

    # GOLONGAN VIA (16) - KELOMPOK OKSIGEN (KALKOGEN)
    "O": {
        "Informasi Dasar": {"Nama": "Oksigen", "Nomor Atom": 8, "Kategori": "Non-logam", "Massa Atom Relatif": 15.999, "Golongan": "VIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p⁴", "Tahun Ditemukan": 1774},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, agen pengoksidasi kuat, mendukung pembakaran"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "1.43 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Esensial", "Piktogram GHS": "🔥 (Oksidator)", "Bahaya Kesehatan": "Oksigen murni 100% pada tekanan tinggi dapat memicu toksisitas paru", "Batas Paparan": "Kondisi atmosferik normal aman"},
        "Kegunaan": "Respirasi makhluk hidup, tabung medis rumah sakit, las oksiasetilen, bahan bakar roket."
    },
    "S": {
        "Informasi Dasar": {"Nama": "Belerang (Sulfur)", "Nomor Atom": 16, "Kategori": "Non-logam", "Massa Atom Relatif": 32.06, "Golongan": "VIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p⁴", "Tahun Ditemukan": "Zaman Kuno"},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Terbakar menghasilkan gas belerang dioksida berbau menyengat"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Kuning lemon terang", "Massa Jenis": "2.07 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Debunya mengiritasi mata, senyawanya ($H_2S$) sangat beracun", "Batas Paparan": "Tidak ada batas ketat logam murni"},
        "Kegunaan": "Bahan baku asam sulfat, vulkanisasi karet ban, obat jerawat kulit, bubuk mesiu."
    },
    "Se": {
        "Informasi Dasar": {"Nama": "Selenium", "Nomor Atom": 34, "Kategori": "Non-logam", "Massa Atom Relatif": 78.971, "Golongan": "VIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 4p⁴", "Tahun Ditemukan": 1817},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Bersifat fotokonduktif (menghantarkan listrik lebih baik saat terkena cahaya)"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu metalik / Merah", "Massa Jenis": "4.81 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "☠️", "Bahaya Kesehatan": "Mikronutrien penting, tetapi kelebihan memicu keracunan (Selenosis)", "Batas Paparan": "0.2 mg/m³"},
        "Kegunaan": "Mesin fotokopi tua, kaca penangkal radiasi matahari, sampo anti ketombe (Selenium sulfida)."
    },
    "Te": {
        "Informasi Dasar": {"Nama": "Telurium", "Nomor Atom": 52, "Kategori": "Metaloid", "Massa Atom Relatif": 127.6, "Golongan": "VIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p⁴", "Tahun Ditemukan": 1782},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sedikit reaktif, terbakar dengan nyala api hijau-biru"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan berkilau mika", "Massa Jenis": "6.24 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Paparan kronis menyebabkan napas dan keringat berbau bawang putih tajam", "Batas Paparan": "0.1 mg/m³"},
        "Kegunaan": "Campuran logam baja agar mudah dipotong, panel surya CdTe termutakhir."
    },
    "Po": {
        "Informasi Dasar": {"Nama": "Polonium", "Nomor Atom": 84, "Kategori": "Metaloid", "Massa Atom Relatif": "209 (estimasi)", "Golongan": "VIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", "Tahun Ditemukan": 1898},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat volatil, melepaskan energi panas tinggi akibat peluruhan radiasi alfa"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "9.20 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Salah satu zat paling mematikan di dunia dalam jumlah mikrogram", "Batas Paparan": "Hanya di fasilitas nuklir militer"},
        "Kegunaan": "Pembangkit listrik satelit luar angkasa (RTG), sikat pembersih debu film statis."
    },
    "Lv": {
        "Informasi Dasar": {"Nama": "Livermorium", "Nomor Atom": 116, "Kategori": "Logam Pasca-Transisi (Superberat)", "Massa Atom Relatif": "293 (estimasi)", "Golongan": "VIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴ (Diprediksi)", "Tahun Ditemukan": 2000},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Waktu paruh sangat singkat (sekitar 60 milidetik), sifat kimia teoretis"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "12.9 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi ionisasi mematikan", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Hanya digunakan untuk penelitian sintesis unsur superberat baru."
    },
# GOLONGAN VIIA (17) - HALOGEN
    "F": {
        "Informasi Dasar": {"Nama": "Fluor", "Nomor Atom": 9, "Kategori": "Non-logam (Halogen)", "Massa Atom Relatif": 18.998, "Golongan": "VIIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p⁵", "Tahun Ditemukan": 1886},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Unsur paling reaktif dan elektronegatif, bereaksi dengan hampir semua elemen"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Kuning pucat", "Massa Jenis": "1.696 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Piktogram GHS": "☠️, 🔥", "Bahaya Kesehatan": "Gasnya sangat beracun dan korosif", "Batas Paparan": "0.1 ppm"},
        "Kegunaan": "Pasta gigi (mencegah karies), pelapis anti-lengket (Teflon), pendingin freon."
    },
    "Cl": {
        "Informasi Dasar": {"Nama": "Klorin", "Nomor Atom": 17, "Kategori": "Non-logam (Halogen)", "Massa Atom Relatif": 35.45, "Golongan": "VIIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p⁵", "Tahun Ditemukan": 1774},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif, agen pengoksidasi yang kuat"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Kuning kehijauan", "Massa Jenis": "3.2 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "☠️, ⚠️", "Bahaya Kesehatan": "Iritasi parah pada sistem pernapasan, beracun jika terhirup", "Batas Paparan": "0.5 ppm"},
        "Kegunaan": "Disinfektan air minum dan kolam renang, pemutih pakaian, pembuatan plastik PVC."
    },
    "Br": {
        "Informasi Dasar": {"Nama": "Bromin", "Nomor Atom": 35, "Kategori": "Non-logam (Halogen)", "Massa Atom Relatif": 79.904, "Golongan": "VIIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 4p⁵", "Tahun Ditemukan": 1826},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Satu-satunya unsur non-logam yang cair pada suhu ruang"},
        "Wujud Fisik": {"Wujud (25°C)": "Cair", "Warna": "Merah kecoklatan", "Massa Jenis": "3.10 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Piktogram GHS": "☠️, 🫁", "Bahaya Kesehatan": "Uapnya sangat mengiritasi mata dan paru-paru", "Batas Paparan": "0.1 ppm"},
        "Kegunaan": "Bahan anti-api (flame retardant), disinfektan kolam, fotografi film (AgBr)."
    },
    "I": {
        "Informasi Dasar": {"Nama": "Iodin (Yodium)", "Nomor Atom": 53, "Kategori": "Non-logam (Halogen)", "Massa Atom Relatif": 126.90, "Golongan": "VIIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p⁵", "Tahun Ditemukan": 1811},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Halogen paling tidak reaktif yang stabil, menyublim menjadi gas ungu"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Ungu kehitaman mengkilap", "Massa Jenis": "4.93 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Esensial)", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Penting untuk tiroid, tetapi beracun dalam dosis sangat tinggi", "Batas Paparan": "0.1 ppm"},
        "Kegunaan": "Antiseptik luka (Betadine), suplemen garam beryodium, pewarna kontras medis."
    },
    "At": {
        "Informasi Dasar": {"Nama": "Astatin", "Nomor Atom": 85, "Kategori": "Metaloid (Halogen)", "Massa Atom Relatif": "210 (estimasi)", "Golongan": "VIIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵", "Tahun Ditemukan": 1940},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sifat kimia mirip iodin tetapi jauh lebih radioaktif dan langka"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Hitam metalik (Diprediksi)", "Massa Jenis": "7 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya paparan radiasi", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Riset terapi radiasi alfa untuk mengobati kanker (masih eksperimental)."
    },
    "Ts": {
        "Informasi Dasar": {"Nama": "Tenesin", "Nomor Atom": 117, "Kategori": "Logam Pasca-Transisi (Superberat)", "Massa Atom Relatif": "294 (estimasi)", "Golongan": "VIIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵ (Diprediksi)", "Tahun Ditemukan": 2010},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Waktu paruh sepersekian detik, sifat diprediksi mirip logam bukan halogen biasa"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Metalik (Diprediksi)", "Massa Jenis": "7.2 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi ekstrem", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Hanya eksperimen ilmiah laboratorium."
    },

    # GOLONGAN VIIIA (18) - GAS MULIA
    "He": {
        "Informasi Dasar": {"Nama": "Helium", "Nomor Atom": 2, "Kategori": "Gas Mulia", "Massa Atom Relatif": 4.0026, "Golongan": "VIIIA", "Periode": 1, "Konfigurasi Elektron": "1s²", "Tahun Ditemukan": 1868},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat inert (tidak reaktif), titik didih paling rendah dari semua unsur"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.1786 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️ (Gas bertekanan)", "Bahaya Kesehatan": "Dapat menyebabkan asfiksia jika terhirup menggantikan oksigen", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Pengisi balon udara/pesta, pendingin magnet superkonduktor MRI, gas pernapasan penyelam laut dalam."
    },
    "Ne": {
        "Informasi Dasar": {"Nama": "Neon", "Nomor Atom": 10, "Kategori": "Gas Mulia", "Massa Atom Relatif": 20.180, "Golongan": "VIIIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s² 2p⁶", "Tahun Ditemukan": 1898},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Inert secara kimia, berpendar merah oranye terang jika dialiri listrik"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.900 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Asfiksian ringan", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Papan reklame terang (Lampu Neon), laser gas, indikator tegangan tinggi."
    },
    "Ar": {
        "Informasi Dasar": {"Nama": "Argon", "Nomor Atom": 18, "Kategori": "Gas Mulia", "Massa Atom Relatif": 39.948, "Golongan": "VIIIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s² 3p⁶", "Tahun Ditemukan": 1894},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Inert, kelimpahan cukup tinggi di atmosfer bumi (hampir 1%)"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "1.784 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Asfiksian di ruang tertutup", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Gas pelindung pada pengelasan (TIG/MIG), pengisi bohlam lampu pijar."
    },
    "Kr": {
        "Informasi Dasar": {"Nama": "Kripton", "Nomor Atom": 36, "Kategori": "Gas Mulia", "Massa Atom Relatif": 83.798, "Golongan": "VIIIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 3d¹⁰ 4s² 4p⁶", "Tahun Ditemukan": 1898},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Umumnya inert, tetapi bisa membentuk beberapa senyawa dengan fluorin pada kondisi ekstrem"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "3.749 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Asfiksian ringan", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Lampu flash fotografi kecepatan tinggi, lampu neon putih-kuning pendar bandara."
    },
    "Xe": {
        "Informasi Dasar": {"Nama": "Xenon", "Nomor Atom": 54, "Kategori": "Gas Mulia", "Massa Atom Relatif": 131.29, "Golongan": "VIIIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 4d¹⁰ 5s² 5p⁶", "Tahun Ditemukan": 1898},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Mampu membentuk senyawa kimia stabil pertama dari gas mulia (misal: Xenon heksafluorida)"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "5.894 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Non-toksik", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Asfiksian ringan", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Lampu proyektor bioskop, lampu depan mobil kelas atas (HID), anestesi medis khusus."
    },
    "Rn": {
        "Informasi Dasar": {"Nama": "Radon", "Nomor Atom": 86, "Kategori": "Gas Mulia", "Massa Atom Relatif": "222 (estimasi)", "Golongan": "VIIIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "Tahun Ditemukan": 1899},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Gas mulia yang sangat radioaktif, hasil peluruhan uranium/radium di tanah"},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "9.73 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Karsinogenik (Radioaktif)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Penyebab utama kedua kanker paru-paru setelah merokok jika terakumulasi di basement", "Batas Paparan": "Serendah mungkin (4 pCi/L batas aksi US EPA)"},
        "Kegunaan": "Terapi radiasi kanker (dulu, sekarang diganti yang lebih aman), pelacakan kebocoran geologis."
    },
    "Og": {
        "Informasi Dasar": {"Nama": "Oganeson", "Nomor Atom": 118, "Kategori": "Gas Mulia (Superberat)", "Massa Atom Relatif": "294 (estimasi)", "Golongan": "VIIIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶ (Diprediksi)", "Tahun Ditemukan": 2002},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Efek relativistik mungkin membuatnya berwujud padat dan cukup reaktif (tidak inert seperti gas mulia lainnya)"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Tidak diketahui", "Massa Jenis": "Tidak diketahui"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Hanya meluruh dalam ukuran milidetik", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Menyelesaikan periode 7 pada tabel periodik modern, murni untuk penelitian ilmiah."
    },
# BLOK-F: LANTANIDA
    "La": {
        "Informasi Dasar": {"Nama": "Lantanum", "Nomor Atom": 57, "Kategori": "Lantanida", "Massa Atom Relatif": 138.91, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 5d¹ 6s²", "Tahun Ditemukan": 1839},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif, teroksidasi perlahan di udara membentuk lantanum oksida"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "6.16 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Debunya dapat mengiritasi paru-paru jika terhirup", "Batas Paparan": "Belum ditentukan secara ketat"},
        "Kegunaan": "Kaca lensa optik kualitas tinggi (kamera/teleskop), batu pemantik api, paduan baterai hibrida."
    },
    "Ce": {
        "Informasi Dasar": {"Nama": "Serium", "Nomor Atom": 58, "Kategori": "Lantanida", "Massa Atom Relatif": 140.12, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹ 5d¹ 6s²", "Tahun Ditemukan": 1803},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Lantanida yang paling reaktif, mudah memercikkan api jika tergores"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "6.77 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Paparan kronis dapat menyebabkan gatal dan lesi kulit", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Katalis pada konverter gas buang mobil, pemantik api (ferrocerium), serbuk pemoles kaca."
    },
    "Pr": {
        "Informasi Dasar": {"Nama": "Praseodimium", "Nomor Atom": 59, "Kategori": "Lantanida", "Massa Atom Relatif": 140.91, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f³ 6s²", "Tahun Ditemukan": 1885},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Bereaksi lambat dengan oksigen, membentuk lapisan oksida hijau yang rapuh"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan pucat", "Massa Jenis": "6.77 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Iritasi ringan pada kulit dan mata", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Kacamata pelindung tukang las (kaca didymium), paduan magnet kekuatan tinggi."
    },
    "Nd": {
        "Informasi Dasar": {"Nama": "Neodimium", "Nomor Atom": 60, "Kategori": "Lantanida", "Massa Atom Relatif": 144.24, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁴ 6s²", "Tahun Ditemukan": 1885},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Ternoda di udara, membutuhkan lapisan pelindung agar tidak hancur"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "7.01 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Debunya sangat mudah terbakar dan menyebabkan iritasi mata", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Magnet terkuat di dunia (motor listrik, hard drive, headphone, turbin angin)."
    },
    "Pm": {
        "Informasi Dasar": {"Nama": "Prometium", "Nomor Atom": 61, "Kategori": "Lantanida", "Massa Atom Relatif": "145 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁵ 6s²", "Tahun Ditemukan": 1945},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Satu-satunya unsur lantanida yang sangat radioaktif dan tidak memiliki isotop stabil"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Logam metalik (memancarkan cahaya biru-hijau karena radiasi)", "Massa Jenis": "7.26 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Radioaktif)", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi beta, merusak sel tubuh jika tertelan", "Batas Paparan": "Sangat dikontrol ketat"},
        "Kegunaan": "Baterai nuklir jangka panjang untuk wahana antariksa dan pacu jantung buatan (dulu)."
    },
    "Sm": {
        "Informasi Dasar": {"Nama": "Samarium", "Nomor Atom": 62, "Kategori": "Lantanida", "Massa Atom Relatif": 150.36, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁶ 6s²", "Tahun Ditemukan": 1879},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Ternoda di udara dan terbakar secara spontan pada suhu 150°C"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "7.52 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Dapat mengiritasi selaput lendir", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Magnet SmCo (Samarium-Kobalt) yang tahan suhu tinggi, obat pereda nyeri kanker tulang."
    },
    "Eu": {
        "Informasi Dasar": {"Nama": "Europium", "Nomor Atom": 63, "Kategori": "Lantanida", "Massa Atom Relatif": 151.96, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁷ 6s²", "Tahun Ditemukan": 1901},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Lantanida paling reaktif, langsung bereaksi dengan air mirip kalsium"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan (cepat kusam di udara)", "Massa Jenis": "5.26 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Serbuk logamnya bahaya kebakaran ekstrem", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Fosfor merah dan biru pada layar TV/Monitor, fitur anti-pemalsuan pada uang kertas Euro."
    },
    "Gd": {
        "Informasi Dasar": {"Nama": "Gadolinium", "Nomor Atom": 64, "Kategori": "Lantanida", "Massa Atom Relatif": 157.25, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁷ 5d¹ 6s²", "Tahun Ditemukan": 1880},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif pada suhu tinggi, bersifat feromagnetik pada suhu dingin (< 20°C)"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "7.90 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Dalam bentuk bebas cukup beracun, aman dalam bentuk kelat (senyawa terikat) untuk medis", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Agen kontras untuk pemindaian MRI medis, batang pengendali reaktor nuklir."
    },
    "Tb": {
        "Informasi Dasar": {"Nama": "Terbium", "Nomor Atom": 65, "Kategori": "Lantanida", "Massa Atom Relatif": 158.93, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f⁹ 6s²", "Tahun Ditemukan": 1843},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup stabil di udara, memancarkan cahaya hijau terang (berpendar) bila disinari elektron"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan pucat", "Massa Jenis": "8.23 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Mirip lantanida lainnya, debunya iritatif", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Fosfor hijau di lampu neon/layar, sonar laut dalam, paduan memori bentuk."
    },
    "Dy": {
        "Informasi Dasar": {"Nama": "Disprosium", "Nomor Atom": 66, "Kategori": "Lantanida", "Massa Atom Relatif": 162.50, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁰ 6s²", "Tahun Ditemukan": 1886},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Mudah teroksidasi oleh udara dan air pada suhu tinggi"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Logam keperakan mengkilap", "Massa Jenis": "8.54 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Menimbulkan iritasi jika masuk ke pernapasan", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Campuran pembuat magnet neodymium tahan panas (untuk turbin/mobil listrik), sistem pendingin laser."
    },
    "Ho": {
        "Informasi Dasar": {"Nama": "Holmium", "Nomor Atom": 67, "Kategori": "Lantanida", "Massa Atom Relatif": 164.93, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹¹ 6s²", "Tahun Ditemukan": 1878},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Memiliki momen magnetik paling tinggi dari semua unsur di alam"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "8.79 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Diyakini memiliki tingkat toksisitas akut yang rendah", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Pusat kutub magnet buatan terkuat, laser bedah mata dan gigi."
    },
    "Er": {
        "Informasi Dasar": {"Nama": "Erbium", "Nomor Atom": 68, "Kategori": "Lantanida", "Massa Atom Relatif": 167.26, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹² 6s²", "Tahun Ditemukan": 1843},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Stabil secara kimia, oksidanya berwarna merah muda khas"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "9.07 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Debunya berpotensi membakar ringan di mata", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Penguat sinyal kabel serat optik bawah laut, laser kosmetik kulit, kaca penyerap inframerah."
    },
    "Tm": {
        "Informasi Dasar": {"Nama": "Tulium", "Nomor Atom": 69, "Kategori": "Lantanida", "Massa Atom Relatif": 168.93, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹³ 6s²", "Tahun Ditemukan": 1879},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Paling tidak melimpah dari lantanida alami, perlahan bereaksi dengan air"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan terang", "Massa Jenis": "9.32 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Sangat sedikit info racunnya, ditangani hati-hati secara industri", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Mesin sinar-X portabel kecil tanpa listrik (menggunakan isotop radioaktifnya), laser operasi presisi."
    },
    "Yb": {
        "Informasi Dasar": {"Nama": "Iterbium", "Nomor Atom": 70, "Kategori": "Lantanida", "Massa Atom Relatif": 173.05, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 6s²", "Tahun Ditemukan": 1878},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Cukup reaktif, disimpan dalam wadah tertutup kedap udara"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan pucat pucat", "Massa Jenis": "6.90 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah-Sedang", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Menyebabkan iritasi pada kulit dan paru-paru jika tertelan debunya", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Paduan baja anti karat, sensor pendeteksi getaran gempa, bahan pembuat jam atom presisi."
    },
    "Lu": {
        "Informasi Dasar": {"Nama": "Lutetium", "Nomor Atom": 71, "Kategori": "Lantanida", "Massa Atom Relatif": 174.97, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 6, "Konfigurasi Elektron": "[Xe] 4f¹⁴ 5d¹ 6s²", "Tahun Ditemukan": 1907},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Elemen lantanida paling berat dan paling keras"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "9.84 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Piktogram GHS": "⚠️", "Bahaya Kesehatan": "Tingkat toksisitas diperkirakan rendah", "Batas Paparan": "Belum ditentukan"},
        "Kegunaan": "Katalis proses pemurnian minyak bumi, bahan pemindai PET (Positron Emission Tomography) medis."
    },

    # BLOK-F: AKTINIDA
    "Ac": {
        "Informasi Dasar": {"Nama": "Aktinium", "Nomor Atom": 89, "Kategori": "Aktinida", "Massa Atom Relatif": "227 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 6d¹ 7s²", "Tahun Ditemukan": 1899},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat reaktif dengan udara membentuk lapisan putih zink-oksida seperti aktinium oksida"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan (Bercahaya biru karena radiasi)", "Massa Jenis": "10.0 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Radioaktif)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Bahaya radiasi setara radium, mematikan jika terhirup atau tertelan", "Batas Paparan": "Fasilitas Nuklir Khusus"},
        "Kegunaan": "Terapi radiasi mutakhir untuk pengobatan kanker tulang dan organ (Targeted Alpha Therapy)."
    },
    "Th": {
        "Informasi Dasar": {"Nama": "Torium", "Nomor Atom": 90, "Kategori": "Aktinida", "Massa Atom Relatif": 232.04, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 6d² 7s²", "Tahun Ditemukan": 1829},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Lemah secara radioaktif, perlahan menghitam di udara karena oksida"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "11.7 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Radioaktif & Kimiawi)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Debu torium memicu kanker paru dan merusak tulang, serta liver", "Batas Paparan": "Sangat Dibatasi"},
        "Kegunaan": "Potensi besar sebagai bahan bakar reaktor nuklir generasi masa depan (LFTR), kaca lensa tahan panas."
    },
    "Pa": {
        "Informasi Dasar": {"Nama": "Protaktinium", "Nomor Atom": 91, "Kategori": "Aktinida", "Massa Atom Relatif": 231.04, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f² 6d¹ 7s²", "Tahun Ditemukan": 1913},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Logam yang sangat langka dan mahal, bersinar kuat secara radiologi"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan terang mengkilap", "Massa Jenis": "15.37 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Sangat Radioaktif)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Tingkat radiasi mematikan dan bersifat akumulatif di tubuh", "Batas Paparan": "Fasilitas Nuklir Tertutup"},
        "Kegunaan": "Sebagian besar murni untuk penelitian ilmiah fundamental tentang fisika bumi purba."
    },
    "U": {
        "Informasi Dasar": {"Nama": "Uranium", "Nomor Atom": 92, "Kategori": "Aktinida", "Massa Atom Relatif": 238.03, "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f³ 6d¹ 7s²", "Tahun Ditemukan": 1789},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Dapat pecah (fisi) ketika ditembak dengan neutron, melepaskan energi luar biasa besar"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja keperakan", "Massa Jenis": "19.05 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Beracun & Radioaktif)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Paparan radiasi dan keracunan logam berat yang menyebabkan gagal ginjal fatal", "Batas Paparan": "Regulasi ketat militer/energi"},
        "Kegunaan": "Bahan bakar utama Pembangkit Listrik Tenaga Nuklir (PLTN), amunisi penembus baja (depleted uranium), hulu ledak militer."
    },
    "Np": {
        "Informasi Dasar": {"Nama": "Neptunium", "Nomor Atom": 93, "Kategori": "Aktinida", "Massa Atom Relatif": "237 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁴ 6d¹ 7s²", "Tahun Ditemukan": 1940},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Unsur sintesis radioaktif, membentuk berbagai tingkat oksidasi"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan", "Massa Jenis": "20.45 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Radioaktif)", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Mengendap di dalam tulang dan menyebarkan radiasi fatal internal", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Digunakan sebagai bahan pendeteksi partikel neutron tingkat tinggi, bahan antara produksi Plutonium."
    },
    "Pu": {
        "Informasi Dasar": {"Nama": "Plutonium", "Nomor Atom": 94, "Kategori": "Aktinida", "Massa Atom Relatif": "244 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁶ 7s²", "Tahun Ditemukan": 1940},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Logam buatan manusia, memanas sendiri dengan melepaskan radiasi partikel alfa"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih perak terang", "Massa Jenis": "19.82 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Sangat Radioaktif & Karsinogenik)", "Piktogram GHS": "☢️, ☠️", "Bahaya Kesehatan": "Sangat beracun, ukuran debu mikroskopis dapat menyebabkan kanker yang mematikan", "Batas Paparan": "Fasilitas Pertahanan & Luar Angkasa"},
        "Kegunaan": "Hulu ledak senjata nuklir utama, baterai abadi penjelajah planet luar angkasa (seperti rovers Mars)."
    },
    "Am": {
        "Informasi Dasar": {"Nama": "Amerisium", "Nomor Atom": 95, "Kategori": "Aktinida", "Massa Atom Relatif": "243 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁷ 7s²", "Tahun Ditemukan": 1944},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Logam radioaktif buatan sintetik, bereaksi lambat dengan air atau asam"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "12.0 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Radioaktif)", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Terkunci dalam casing aman untuk komersial, sangat berbahaya jika menelan logam murni", "Batas Paparan": "Diatur Ketat"},
        "Kegunaan": "Satu-satunya unsur sintetis di rumah (digunakan di dalam detektor asap rumah tangga komersial)."
    },
    "Cm": {
        "Informasi Dasar": {"Nama": "Kurium", "Nomor Atom": 96, "Kategori": "Aktinida", "Massa Atom Relatif": "247 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁷ 6d¹ 7s²", "Tahun Ditemukan": 1944},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat radioaktif, melepaskan energi sangat tinggi yang memancarkan pendaran merah/ungu"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan pucat", "Massa Jenis": "13.51 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Radioaktif)", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Mengancam nyawa, kerusakan jaringan berat karena partikel alfa", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Tenaga listrik termoelektrik untuk ruang angkasa, sumber partikel spektrometer X-Ray Alpha."
    },
    "Bk": {
        "Informasi Dasar": {"Nama": "Berkelium", "Nomor Atom": 97, "Kategori": "Aktinida", "Massa Atom Relatif": "247 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f⁹ 7s²", "Tahun Ditemukan": 1949},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Memiliki umur peluruhan sedang hingga lambat, dibuat khusus melalui pemboman neutron"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan (Diprediksi)", "Massa Jenis": "14.78 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi ekstrem", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Bahan target khusus untuk memproduksi (mensintesis) unsur-unsur yang lebih berat."
    },
    "Cf": {
        "Informasi Dasar": {"Nama": "Kalifornium", "Nomor Atom": 98, "Kategori": "Aktinida", "Massa Atom Relatif": "251 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁰ 7s²", "Tahun Ditemukan": 1950},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Pemancar neutron terkuat yang bisa diandalkan, logam sangat padat dan mahal"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan", "Massa Jenis": "15.1 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Ekstrem (Sangat Radioaktif)", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Menyebabkan kerusakan sumsum tulang fatal", "Batas Paparan": "Ditangani pakai robot"},
        "Kegunaan": "Deteksi lapisan minyak atau kandungan perak/emas dalam tanah, terapi kanker otak radiasi tinggi."
    },
    "Es": {
        "Informasi Dasar": {"Nama": "Einsteinium", "Nomor Atom": 99, "Kategori": "Aktinida", "Massa Atom Relatif": "252 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹¹ 7s²", "Tahun Ditemukan": 1952},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Ditemukan pertama kali dari sisa-sisa ledakan bom hidrogen pertama di dunia"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Metalik (Memancarkan cahaya kuat)", "Massa Jenis": "8.84 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Radiasi destruktif dalam hitungan detik", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Riset fisika elementer saja."
    },
    "Fm": {
        "Informasi Dasar": {"Nama": "Fermium", "Nomor Atom": 100, "Kategori": "Aktinida", "Massa Atom Relatif": "257 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹² 7s²", "Tahun Ditemukan": 1952},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Elemen terberat yang pernah dibentuk oleh tumbukan partikel reaktor nuklir normal"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Tidak diketahui", "Massa Jenis": "Belum ditentukan"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya radiasi fatal", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Eksperimen murni ilmu pengetahuan alam."
    },
    "Md": {
        "Informasi Dasar": {"Nama": "Mendelevium", "Nomor Atom": 101, "Kategori": "Aktinida", "Massa Atom Relatif": "258 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹³ 7s²", "Tahun Ditemukan": 1955},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Elemen pertama yang disintesis dari atom satu-per-satu di laboratorium akselerator partikel"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Tidak diketahui", "Massa Jenis": "Belum ditentukan"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya tinggi radiasi dan toksisitas akut", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Studi kimia dan fisika lanjut."
    },
    "No": {
        "Informasi Dasar": {"Nama": "Nobelium", "Nomor Atom": 102, "Kategori": "Aktinida", "Massa Atom Relatif": "259 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 7s²", "Tahun Ditemukan": 1966},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Sangat tidak stabil secara atomik, mudah mengalami fisi atau peluruhan partikel alfa"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Tidak diketahui", "Massa Jenis": "Belum ditentukan"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Bahaya fisi dan radiasi intens tinggi", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Hanya eksperimen ilmiah teoritis."
    },
    "Lr": {
        "Informasi Dasar": {"Nama": "Lawrensium", "Nomor Atom": 103, "Kategori": "Aktinida", "Massa Atom Relatif": "266 (estimasi)", "Golongan": "Golongan 3 (Transisi Dalam)", "Periode": 7, "Konfigurasi Elektron": "[Rn] 5f¹⁴ 7s² 7p¹", "Tahun Ditemukan": 1961},
        "Sifat Kimia & Fisik": {"Reaktivitas": "Anggota terakhir dari seri aktinida dan elemen blok-f terberat"},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Diprediksi)", "Warna": "Tidak diketahui", "Massa Jenis": "16.1 g/cm³ (Diprediksi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Pemancar alfa destruktif, hanya diproduksi sebagian fraksi atom", "Batas Paparan": "Tidak ada"},
        "Kegunaan": "Penelitian ilmiah untuk membuktikan model batas-batas fisika tabel periodik."
    },
}
st.title("Tabel Periodik Unsur Kimia Interaktif ⚛️")
st.write("Klik pada unsur yang tersedia (warna dapat diklik) untuk melihat detailnya di bagian bawah.")

# Menyimpan unsur yang diklik
if 'unsur_terpilih' not in st.session_state:
    st.session_state.unsur_terpilih = 'H'

# --- LAYOUT MATRIKS TABEL PERIODIK ---
# Daftar baris mewakili 7 Periode dan 18 Golongan. Spasi kosong diisi dengan string kosong ("")
grid_tabel = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "*", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "**", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
]

# Menggambar Tabel Periodik
for baris in grid_tabel:
    kolom = st.columns(18) # Membagi layar menjadi 18 kolom sama besar
    for i, unsur in enumerate(baris):
        with kolom[i]:
            if unsur != "":  
                if unsur in unsur_data:
                    # Jika unsur ada di dictionary, jadikan tombol yang bisa diklik
                    if st.button(unsur, use_container_width=True, type="primary"):
                        st.session_state.unsur_terpilih = unsur
                else:
                    # Jika unsur belum ditambahkan, buat tombol menjadi "disabled" (abu-abu)
                    st.button(unsur, use_container_width=True, disabled=True)

# Tambahan untuk Lantanida & Aktinida di bawah
st.write("")
st.caption("Blok-f (Lantanida & Aktinida)")
blok_f = [
    ["", "", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", ""],
    ["", "", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", ""]
]
for baris in blok_f:
    kolom = st.columns(18)
    for i, unsur in enumerate(baris):
        with kolom[i]:
            if unsur != "":
                if unsur in unsur_data:
                    if st.button(unsur, use_container_width=True, key=f"f_{unsur}", type="primary"):
                        st.session_state.unsur_terpilih = unsur
                else:
                    st.button(unsur, use_container_width=True, disabled=True, key=f"f_{unsur}")

st.markdown("---")

# --- DETAIL UNSUR (DITAMPILKAN DI BAWAH TABEL) ---
if st.session_state.unsur_terpilih in unsur_data:
    unsur_aktif = unsur_data[st.session_state.unsur_terpilih]
    
    st.header(f"🔎 Detail Unsur: {unsur_aktif['Informasi Dasar']['Nama']} ({st.session_state.unsur_terpilih})")
    st.caption(f"Nomor Atom: {unsur_aktif['Informasi Dasar']['Nomor Atom']} | Kategori: {unsur_aktif['Informasi Dasar']['Kategori']}")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Informasi Dasar", "Sifat Kimia & Fisik", "Wujud Fisik", "Kesehatan & Keselamatan", "Kegunaan"
    ])
    
    with tab1:
        df_dasar = pd.DataFrame(list(unsur_aktif["Informasi Dasar"].items()), columns=["Properti", "Nilai"])
        st.dataframe(df_dasar, hide_index=True, use_container_width=True)

    with tab2:
        for key, value in unsur_aktif["Sifat Kimia & Fisik"].items():
            st.markdown(f"**{key}:** {value}")

    with tab3:
        c1, c2, c3 = st.columns(3)
        c1.metric("Wujud (25°C)", unsur_aktif["Wujud Fisik"].get("Wujud (25°C)", "-"))
        c2.metric("Warna", unsur_aktif["Wujud Fisik"].get("Warna", "-"))
        c3.metric("Massa Jenis", unsur_aktif["Wujud Fisik"].get("Massa Jenis", "-"))

    with tab4:
        st.info(f"**Piktogram GHS:** {unsur_aktif['Kesehatan & Keselamatan'].get('Piktogram GHS', '-')}")
        for key, value in unsur_aktif["Kesehatan & Keselamatan"].items():
            if key != "Piktogram GHS":
                st.write(f"**{key}:** {value}")

    with tab5:
        st.success(unsur_aktif.get("Kegunaan", "Belum ada data kegunaan."))
import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Tabel Periodik Interaktif", page_icon="🧪", layout="wide")

# 2. Dataset Contoh: Golongan IA
unsur_data = {
    "Hidrogen": {
        "Informasi Dasar": {"Simbol": "H", "Nomor Atom": 1, "Massa Atom Relatif": 1.008, "Golongan": "IA", "Periode": 1, "Konfigurasi Elektron": "1s¹", "Kategori Unsur": "Non-logam", "Tahun Ditemukan": 1766, "Valensi": 1, "Kelektronegatifan": 2.20, "Titik Didih": "-252.87 °C", "Titik Lebur": "-259.16 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Netral (dalam air)", "Kelarutan (Air)": "1.6 mg/L (20°C)", "Kelarutan (Organik)": "Sedikit larut", "Reaktivitas": "Sangat reaktif dengan unsur halogen dan oksigen."},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.00008988 g/cm³"},
        "Kesehatan & Keselamatan": {"Tingkat Toksisitas": "Rendah (Asfiksian ringan)", "Bahaya Kesehatan": "Dapat menyebabkan sesak napas dalam konsentrasi tinggi karena menggantikan oksigen.", "Piktogram GHS": "🔥 (Gas Mudah Terbakar)", "Batas Paparan": "Tidak ada batas spesifik, pastikan kadar oksigen > 19.5%"},
        "Kegunaan": "Sintesis amonia, pemurnian minyak bumi, bahan bakar hidrogen, dan pendingin generator."
    },
    "Litium": {
        "Informasi Dasar": {"Simbol": "Li", "Nomor Atom": 3, "Massa Atom Relatif": 6.94, "Golongan": "IA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s¹", "Kategori Unsur": "Logam Alkali", "Tahun Ditemukan": 1817, "Valensi": 1, "Kelektronegatifan": 0.98, "Titik Didih": "1342 °C", "Titik Lebur": "180.5 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (membentuk LiOH dalam air)", "Kelarutan (Air)": "Bereaksi eksotermis (membentuk gas hidrogen)", "Kelarutan (Organik)": "Larut dalam amonia cair", "Reaktivitas": "Reaktif terhadap air dan oksigen, harus disimpan dalam minyak."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.534 g/cm³"},
        "Kesehatan & Keselamatan": {"Tingkat Toksisitas": "Sedang hingga Tinggi", "Bahaya Kesehatan": "Sangat korosif. Reaksi dengan uap air di kulit menyebabkan luka bakar kimia.", "Piktogram GHS": "☠️🔥 (Korosif, Mudah Terbakar, Beracun)", "Batas Paparan": "0.025 mg/m³ (sebagai hidrida/hidroksida)"},
        "Kegunaan": "Pembuatan baterai ion-litium, paduan logam untuk pesawat terbang, pengobatan gangguan bipolar (Litium karbonat)."
    },
    "Natrium": {
        "Informasi Dasar": {"Simbol": "Na", "Nomor Atom": 11, "Massa Atom Relatif": 22.99, "Golongan": "IA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s¹", "Kategori Unsur": "Logam Alkali", "Tahun Ditemukan": 1807, "Valensi": 1, "Kelektronegatifan": 0.93, "Titik Didih": "883 °C", "Titik Lebur": "97.72 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (membentuk NaOH)", "Kelarutan (Air)": "Bereaksi sangat keras/meledak di air", "Kelarutan (Organik)": "Tidak larut dalam pelarut organik biasa", "Reaktivitas": "Sangat reaktif terhadap air dan kelembapan udara."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Lunak)", "Warna": "Putih keperakan", "Massa Jenis": "0.968 g/cm³"},
        "Kesehatan & Keselamatan": {"Tingkat Toksisitas": "Tinggi", "Bahaya Kesehatan": "Luka bakar termal dan kimia yang sangat parah jika terkena kulit basah.", "Piktogram GHS": "💥🔥 (Eksplosif dengan Air, Korosif)", "Batas Paparan": "2 mg/m³ (sebagai NaOH)"},
        "Kegunaan": "Lampu jalan (lampu uap natrium), pendingin reaktor nuklir, sintesis bahan kimia, dan garam dapur (sebagai senyawa NaCl)."
    }
}

# 3. Sidebar / Header Pencarian
st.sidebar.title("Navigasi Unsur")
st.sidebar.markdown("Silakan pilih unsur untuk melihat detailnya.")

# Membuat opsi default untuk memicu Halaman Welcome
opsi_beranda = "🏠 Beranda (Selamat Datang)"
daftar_pilihan = [opsi_beranda] + list(unsur_data.keys())

# Pindahkan dropdown ke sidebar agar area utama lebih bersih
unsur_terpilih = st.sidebar.selectbox("Cari dan Pilih Unsur Kimia:", daftar_pilihan)

st.sidebar.divider()
st.sidebar.caption("© 2026 - Aplikasi Tabel Periodik")

# 4. Logika Tampilan (Welcome Screen vs Detail Unsur)
if unsur_terpilih == opsi_beranda:
    # ==========================================
    # TAMPILAN SELAMAT DATANG (WELCOME SCREEN)
    # ==========================================
    st.title("👋 Selamat Datang di Ensiklopedia Unsur Kimia")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Aplikasi ini adalah **Tabel Periodik Interaktif** yang dirancang untuk membantu Anda mempelajari berbagai unsur kimia dengan mudah dan detail. 
        
        Melalui aplikasi ini, Anda dapat mengeksplorasi:
        * 📑 **Informasi Dasar** (Massa atom, konfigurasi elektron, dll)
        * 🧪 **Sifat Kimia & Fisik** (Reaktivitas, kelarutan)
        * 🧊 **Wujud Fisik** (Massa jenis, wujud pada suhu ruang)
        * ⚠️ **Kesehatan & Keselamatan** (Piktogram GHS dan tingkat toksisitas)
        * 🏭 **Kegunaan** (Aplikasi di dunia nyata)
        """)
        
        st.info("👈 **Cara Penggunaan:** Silakan buka menu dropdown di sebelah kiri (Sidebar) dan pilih unsur kimia yang ingin Anda pelajari!")

    with col2:
        # Menampilkan gambar ilustrasi sains (menggunakan placeholder/emoji besar jika tidak ada file gambar)
        st.markdown(
            """
            <div style="text-align: center; font-size: 100px;">
                🔬🧪⚛️
            </div>
            """, 
            unsafe_allow_html=True
        )

else:
    # ==========================================
    # TAMPILAN DETAIL UNSUR KIMIA (TABS)
    # ==========================================
    data = unsur_data[unsur_terpilih]
    
    st.title(f"🧪 {unsur_terpilih} ({data['Informasi Dasar']['Simbol']})")
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📑 Informasi Dasar", 
        "🧪 Sifat Kimia & Fisik", 
        "🧊 Wujud Fisik", 
        "⚠️ Kesehatan & Keselamatan", 
        "🏭 Kegunaan"
    ])

    def render_dict_to_columns(data_dict):
        col1, col2 = st.columns(2)
        items = list(data_dict.items())
        mid = (len(items) + 1) // 2
        for k, v in items[:mid]:
            col1.markdown(f"**{k}:** {v}")
        for k, v in items[mid:]:
            col2.markdown(f"**{k}:** {v}")

    with tab1:
        st.subheader("Data Dasar Unsur")
        render_dict_to_columns(data["Informasi Dasar"])

    with tab2:
        st.subheader("Reaktivitas dan Sifat Lainnya")
        render_dict_to_columns(data["Sifat Kimia & Fisik"])

    with tab3:
        st.subheader("Keadaan Fisik pada Suhu Ruang")
        render_dict_to_columns(data["Wujud Fisik"])

    with tab4:
        st.subheader("Protokol Keselamatan dan Bahaya")
        for k, v in data["Kesehatan & Keselamatan"].items():
            if k == "Piktogram GHS":
                st.warning(f"**{k}:** {v}")
            else:
                st.markdown(f"**{k}:** {v}")

    with tab5:
        st.subheader("Aplikasi di Dunia Nyata")
        st.success(data["Kegunaan"])
