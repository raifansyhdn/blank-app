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
    "Ra": {"Informasi Dasar": {"Nama": "Radium", "Nomor Atom": 88, "Kategori": "Logam Alkali Tanah", "Massa Atom Relatif": 226, "Golongan": "IIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s²", "Tahun Ditemukan": 1898}, "Sifat Kimia & Fisik": {"Reaktivitas": "Memancarkan radiasi"}, "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "5.5 g/cm³"}, "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Piktogram GHS": "☢️", "Bahaya Kesehatan": "Kanker tulang", "Batas Paparan": "Sangat ketat"}, "Kegunaan": "Penelitian medis."}
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
