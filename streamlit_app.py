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
