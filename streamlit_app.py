import streamlit as st
import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide", page_icon="🧪")

# --- DATASET GOLONGAN IA ---
# Anda dapat menambahkan golongan lain di bawah dictionary ini nanti.
unsur_data = {
    "H": {
        "Informasi Dasar": {"Nama": "Hidrogen", "Simbol": "H", "Nomor Atom": 1, "Massa Atom Relatif": 1.008, "Golongan": "IA", "Periode": 1, "Konfigurasi Elektron": "1s¹", "Kategori": "Non-logam", "Tahun Ditemukan": 1766, "Valensi": 1, "Keelektronegatifan": 2.20, "Titik Didih": "-252.87 °C", "Titik Lebur": "-259.16 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Netral (dalam bentuk H2O)", "Kelarutan (Air)": "Sedikit larut", "Kelarutan (Organik)": "Larut dalam beberapa logam", "Reaktivitas": "Sangat reaktif pada suhu tinggi, membentuk senyawa dengan hampir semua unsur."},
        "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.08988 g/L"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Bahaya Kesehatan": "Asfiksian (menggantikan oksigen di udara tertutup).", "Piktogram GHS": "🔥 (Mudah Terbakar), 🗜️ (Gas Bertekanan)", "Batas Paparan": "Tidak ada batas spesifik, batasi hingga level oksigen aman (>19.5%)."},
        "Kegunaan": "Bahan bakar roket, sel bahan bakar (fuel cells), produksi amonia (proses Haber), hidrogenasi minyak."
    },
    "Li": {
        "Informasi Dasar": {"Nama": "Litium", "Simbol": "Li", "Nomor Atom": 3, "Massa Atom Relatif": 6.94, "Golongan": "IA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1817, "Valensi": 1, "Keelektronegatifan": 0.98, "Titik Didih": "1342 °C", "Titik Lebur": "180.5 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk LiOH)", "Kelarutan (Air)": "Bereaksi dengan air (eksotermis)", "Kelarutan (Organik)": "Bereaksi", "Reaktivitas": "Sangat reaktif, mudah teroksidasi di udara, bereaksi kuat dengan air."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.534 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Bahaya Kesehatan": "Korosif pada kulit dan mata, toksik jika tertelan dalam jumlah besar.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "0.025 mg/m³ (sebagai debu/senyawa)."},
        "Kegunaan": "Baterai ion-litium, paduan logam untuk pesawat terbang, obat penstabil mood (Bipolar)."
    },
    "Na": {
        "Informasi Dasar": {"Nama": "Natrium", "Simbol": "Na", "Nomor Atom": 11, "Massa Atom Relatif": 22.990, "Golongan": "IA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1807, "Valensi": 1, "Keelektronegatifan": 0.93, "Titik Didih": "883 °C", "Titik Lebur": "97.79 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk NaOH)", "Kelarutan (Air)": "Bereaksi hebat dengan air", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Sangat reaktif, bereaksi eksplosif dengan air membentuk gas hidrogen."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.968 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang (bahaya fisik tinggi)", "Bahaya Kesehatan": "Memicu luka bakar termal dan kimia yang parah jika terkena kulit basah.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "2 mg/m³ (sebagai NaOH)."},
        "Kegunaan": "Garam dapur (NaCl), lampu jalan (lampu natrium), pendingin di reaktor nuklir."
    },
    "K": {
        "Informasi Dasar": {"Nama": "Kalium", "Simbol": "K", "Nomor Atom": 19, "Massa Atom Relatif": 39.098, "Golongan": "IA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1807, "Valensi": 1, "Keelektronegatifan": 0.82, "Titik Didih": "759 °C", "Titik Lebur": "63.5 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk KOH)", "Kelarutan (Air)": "Bereaksi sangat hebat dengan air", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Lebih reaktif dari Natrium, menyala spontan saat kontak dengan air."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.862 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Bahaya Kesehatan": "Luka bakar korosif parah, hiperkalemia jika kelebihan dosis dalam tubuh.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "2 mg/m³ (sebagai KOH)."},
        "Kegunaan": "Pupuk (NPK), sabun cair, menjaga keseimbangan elektrolit dalam tubuh."
    },
    "Rb": {
        "Informasi Dasar": {"Nama": "Rubidium", "Simbol": "Rb", "Nomor Atom": 37, "Massa Atom Relatif": 85.468, "Golongan": "IA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1861, "Valensi": 1, "Keelektronegatifan": 0.82, "Titik Didih": "688 °C", "Titik Lebur": "39.3 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk RbOH)", "Kelarutan (Air)": "Bereaksi secara eksplosif", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Menyala spontan di udara, bereaksi sangat eksplosif dengan air."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Sangat lunak)", "Warna": "Abu-abu keperakan", "Massa Jenis": "1.532 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah hingga Sedang", "Bahaya Kesehatan": "Luka bakar termal dan kimia akibat reaksi dengan kelembapan kulit.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "Belum ada standar khusus, ditangani seperti logam alkali lainnya."},
        "Kegunaan": "Jam atom, kaca khusus, kembang api (warna ungu/merah)."
    },
    "Cs": {
        "Informasi Dasar": {"Nama": "Sesium", "Simbol": "Cs", "Nomor Atom": 55, "Massa Atom Relatif": 132.905, "Golongan": "IA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1860, "Valensi": 1, "Keelektronegatifan": 0.79, "Titik Didih": "671 °C", "Titik Lebur": "28.5 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk CsOH)", "Kelarutan (Air)": "Bereaksi secara eksplosif", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Logam paling reaktif, meledak saat kontak dengan air dingin atau udara."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (Cair pada hari yang panas)", "Warna": "Keperakan-Emas", "Massa Jenis": "1.93 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Toksisitas radionuklida tinggi untuk isotop Cs-137)", "Bahaya Kesehatan": "Luka bakar luar biasa parah.", "Piktogram GHS": "🔥 (Sangat Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "Tidak ada standar khusus unsur stabil."},
        "Kegunaan": "Jam atom paling akurat, cairan pemboran minyak, sel fotolistrik."
    },
    "Fr": {
        "Informasi Dasar": {"Nama": "Fransium", "Simbol": "Fr", "Nomor Atom": 87, "Massa Atom Relatif": 223, "Golongan": "IA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s¹", "Kategori": "Logam Alkali", "Tahun Ditemukan": 1939, "Valensi": 1, "Keelektronegatifan": "0.7 (estimasi)", "Titik Didih": "677 °C (estimasi)", "Titik Lebur": "27 °C (estimasi)"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk FrOH)", "Kelarutan (Air)": "Diasumsikan bereaksi sangat eksplosif", "Kelarutan (Organik)": "Tidak diketahui", "Reaktivitas": "Secara teoritis logam basa paling reaktif, namun karena waktu paruh sangat singkat, sulit diteliti."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat (estimasi)", "Warna": "Metalik (estimasi)", "Massa Jenis": "1.87 g/cm³ (estimasi)"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Bahaya Kesehatan": "Kerusakan jaringan akibat radiasi tinggi.", "Piktogram GHS": "☢️ (Radioaktif)", "Batas Paparan": "Dilarang terpapar, penanganan di fasilitas khusus."},
        "Kegunaan": "Hanya digunakan untuk tujuan penelitian dasar (tidak ada kegunaan komersial)."
    }
}

# --- APLIKASI UTAMA ---
st.title("Tabel Periodik Unsur Kimia Interaktif ⚛️")
st.write("Jelajahi sifat dan informasi mendetail tentang unsur-unsur kimia. Pilih unsur pada grid di sebelah kiri untuk melihat detailnya.")
st.markdown("---")

# Menggunakan Session State untuk mengingat unsur yang dipilih
if 'unsur_terpilih' not in st.session_state:
    st.session_state.unsur_terpilih = 'H'

# Layout Kiri (Tabel/Pilihan Unsur) dan Kanan (Detail)
col_tabel, col_detail = st.columns([1, 4])

with col_tabel:
    st.subheader("Gol. IA")
    # Membuat tombol bersusun ke bawah menyerupai kolom Tabel Periodik
    for simbol in unsur_data.keys():
        if st.button(simbol, use_container_width=True):
            st.session_state.unsur_terpilih = simbol
    
    st.markdown("*Note: Golongan lain akan ditambahkan di versi berikutnya.*")

with col_detail:
    # Mengambil data dari unsur yang sedang dipilih di session state
    unsur_aktif = unsur_data[st.session_state.unsur_terpilih]
    
    st.header(f"{unsur_aktif['Informasi Dasar']['Nama']} ({st.session_state.unsur_terpilih})")
    st.caption(f"Nomor Atom: {unsur_aktif['Informasi Dasar']['Nomor Atom']} | Kategori: {unsur_aktif['Informasi Dasar']['Kategori']}")
    
    # Membuat 5 Tabs Sesuai Permintaan
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Informasi Dasar", 
        "Sifat Kimia & Fisik", 
        "Wujud Fisik", 
        "Kesehatan & Keselamatan", 
        "Kegunaan"
    ])
    
    with tab1:
        st.subheader("Informasi Dasar")
        # Mengubah dictionary menjadi dataframe untuk tampilan tabel yang rapi
        df_dasar = pd.DataFrame(list(unsur_aktif["Informasi Dasar"].items()), columns=["Properti", "Nilai"])
        # Menyembunyikan index saat render
        st.dataframe(df_dasar, hide_index=True, use_container_width=True)

    with tab2:
        st.subheader("Sifat Kimia & Fisik")
        for key, value in unsur_aktif["Sifat Kimia & Fisik"].items():
            st.markdown(f"**{key}:** {value}")

    with tab3:
        st.subheader("Wujud Fisik")
        col_wujud1, col_wujud2, col_wujud3 = st.columns(3)
        col_wujud1.metric("Wujud (25°C)", unsur_aktif["Wujud Fisik"]["Wujud (25°C)"])
        col_wujud2.metric("Warna", unsur_aktif["Wujud Fisik"]["Warna"])
        col_wujud3.metric("Massa Jenis", unsur_aktif["Wujud Fisik"]["Massa Jenis"])

    with tab4:
        st.subheader("Kesehatan & Keselamatan")
        st.info(f"**Piktogram GHS:** {unsur_aktif['Kesehatan & Keselamatan']['Piktogram GHS']}")
        st.write(f"**Tingkat Toksisitas:** {unsur_aktif['Kesehatan & Keselamatan']['Toksisitas']}")
        st.write(f"**Bahaya Kesehatan:** {unsur_aktif['Kesehatan & Keselamatan']['Bahaya Kesehatan']}")
        st.write(f"**Batas Paparan Kerja:** {unsur_aktif['Kesehatan & Keselamatan']['Batas Paparan']}")

    with tab5:
        st.subheader("Kegunaan Utama di Dunia Nyata")
        st.success(unsur_aktif["Kegunaan"])

"Be": {
        "Informasi Dasar": {"Nama": "Berilium", "Simbol": "Be", "Nomor Atom": 4, "Massa Atom Relatif": 9.012, "Golongan": "IIA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1798, "Valensi": 2, "Keelektronegatifan": 1.57, "Titik Didih": "2469 °C", "Titik Lebur": "1287 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sedikit asam (dalam bentuk garam terlarut)", "Kelarutan (Air)": "Tidak larut", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Reaktivitas rendah pada suhu ruang, tidak bereaksi dengan air karena membentuk lapisan oksida pelindung."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu baja", "Massa Jenis": "1.85 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi", "Bahaya Kesehatan": "Karsinogenik. Menghirup debunya memicu Beriliosis (penyakit paru-paru yang fatal).", "Piktogram GHS": "☠️ (Beracun), 🫁 (Bahaya Kesehatan)", "Batas Paparan": "0.0002 mg/m³ (sangat ketat)."},
        "Kegunaan": "Paduan tembaga-berilium (alat bebas percikan api), jendela tabung sinar-X, komponen pesawat ruang angkasa."
    },
    "Mg": {
        "Informasi Dasar": {"Nama": "Magnesium", "Simbol": "Mg", "Nomor Atom": 12, "Massa Atom Relatif": 24.305, "Golongan": "IIA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1755, "Valensi": 2, "Keelektronegatifan": 1.31, "Titik Didih": "1090 °C", "Titik Lebur": "650 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Basa Lemah (Membentuk Mg(OH)2)", "Kelarutan (Air)": "Bereaksi lambat dengan air panas", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Terbakar di udara dengan nyala putih yang sangat terang dan menyilaukan."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu mengkilap", "Massa Jenis": "1.74 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Bahaya Kesehatan": "Debu atau pita magnesium sangat mudah terbakar dan sulit dipadamkan.", "Piktogram GHS": "🔥 (Mudah Terbakar)", "Batas Paparan": "10 mg/m³ (sebagai debu total)."},
        "Kegunaan": "Paduan aluminium (velg mobil/pesawat), obat antasida (obat maag), kembang api, klorofil pada tumbuhan."
    },
    "Ca": {
        "Informasi Dasar": {"Nama": "Kalsium", "Simbol": "Ca", "Nomor Atom": 20, "Massa Atom Relatif": 40.078, "Golongan": "IIA", "Periode": 4, "Konfigurasi Elektron": "[Ar] 4s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1808, "Valensi": 2, "Keelektronegatifan": 1.00, "Titik Didih": "1484 °C", "Titik Lebur": "842 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Basa Kuat (Membentuk Ca(OH)2)", "Kelarutan (Air)": "Bereaksi membentuk gas hidrogen", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Cukup reaktif di udara terbuka, bereaksi stabil dengan air."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Keperakan-putih (kusam jika teroksidasi)", "Massa Jenis": "1.55 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Penting bagi tubuh)", "Bahaya Kesehatan": "Logam murni bersifat korosif pada kulit yang lembab karena reaksi basa.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "2 mg/m³ (sebagai Kalsium Oksida)."},
        "Kegunaan": "Bahan baku semen dan beton, pembuatan baja, suplemen tulang, koagulasi darah dalam tubuh."
    },
    "Sr": {
        "Informasi Dasar": {"Nama": "Stronsium", "Simbol": "Sr", "Nomor Atom": 38, "Massa Atom Relatif": 87.62, "Golongan": "IIA", "Periode": 5, "Konfigurasi Elektron": "[Kr] 5s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1790, "Valensi": 2, "Keelektronegatifan": 0.95, "Titik Didih": "1382 °C", "Titik Lebur": "777 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Basa Kuat (Membentuk Sr(OH)2)", "Kelarutan (Air)": "Bereaksi kuat dengan air", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Sangat reaktif di udara (harus disimpan dalam minyak), terbakar dengan nyala merah tua."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan (Cepat menguning di udara)", "Massa Jenis": "2.64 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Bentuk stabil)", "Bahaya Kesehatan": "Isotop Sr-90 sangat radioaktif dan berbahaya bagi tulang.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Korosif)", "Batas Paparan": "Tidak ada standar khusus untuk logam murni stabil."},
        "Kegunaan": "Pewarna merah pada kembang api dan suar, pasta gigi untuk gigi sensitif (Stronsium klorida)."
    },
    "Ba": {
        "Informasi Dasar": {"Nama": "Barium", "Simbol": "Ba", "Nomor Atom": 56, "Massa Atom Relatif": 137.327, "Golongan": "IIA", "Periode": 6, "Konfigurasi Elektron": "[Xe] 6s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1774, "Valensi": 2, "Keelektronegatifan": 0.89, "Titik Didih": "1897 °C", "Titik Lebur": "727 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk Ba(OH)2)", "Kelarutan (Air)": "Bereaksi sangat kuat dengan air", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Sangat reaktif, mudah teroksidasi, terbakar dengan nyala hijau apel."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu keperakan", "Massa Jenis": "3.51 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Terutama garam terlarutnya)", "Bahaya Kesehatan": "Garam barium terlarut beracun dan menyebabkan kram otot hingga gangguan jantung.", "Piktogram GHS": "🔥 (Mudah Terbakar), ☠️ (Beracun)", "Batas Paparan": "0.5 mg/m³."},
        "Kegunaan": "Pewarna hijau pada kembang api, cairan kontras untuk rontgen saluran pencernaan (Barium sulfat), cairan pengeboran sumur minyak."
    },
    "Ra": {
        "Informasi Dasar": {"Nama": "Radium", "Simbol": "Ra", "Nomor Atom": 88, "Massa Atom Relatif": 226, "Golongan": "IIA", "Periode": 7, "Konfigurasi Elektron": "[Rn] 7s²", "Kategori": "Logam Alkali Tanah", "Tahun Ditemukan": 1898, "Valensi": 2, "Keelektronegatifan": 0.9, "Titik Didih": "1140 °C (estimasi)", "Titik Lebur": "700 °C"},
        "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (Membentuk Ra(OH)2)", "Kelarutan (Air)": "Bereaksi sangat kuat dengan air", "Kelarutan (Organik)": "Tidak larut", "Reaktivitas": "Secara kimia mirip dengan Barium, namun memancarkan radiasi alfa, beta, dan gamma."},
        "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih keperakan (bercahaya biru samar di kegelapan)", "Massa Jenis": "5.5 g/cm³"},
        "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Radioaktif", "Bahaya Kesehatan": "Penumpukan di dalam tulang memicu kanker tulang dan penyakit radiasi.", "Piktogram GHS": "☢️ (Radioaktif)", "Batas Paparan": "Diatur sangat ketat, fasilitas nuklir/medis khusus."},
        "Kegunaan": "Pengobatan kanker (historis), cat bercahaya pada jam tangan kuno (kini dilarang karena mematikan)."
    }
