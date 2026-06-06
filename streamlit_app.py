import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman (Lebar Penuh agar tabel muat)
st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide", page_icon="🧪")

# 2. Inisialisasi Session State (Ingatan Aplikasi)
if 'status_masuk' not in st.session_state:
    st.session_state.status_masuk = False

if 'unsur_terpilih' not in st.session_state:
    st.session_state.unsur_terpilih = "H"

# 3. Logika Antarmuka (Halaman Welcome vs Aplikasi Utama)
if not st.session_state.status_masuk:
    # ===================================================
    # TAMPILAN SELAMAT DATANG SIMPEL (TANPA SIDEBAR/KOLOM)
    # ===================================================
    st.markdown("<br><br><br>", unsafe_allow_html=True) # Memberi jarak dari atas agar teks di tengah
    st.markdown("<h1 style='text-align: center;'>👋 Selamat Datang di Tabel Periodik Interaktif</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #888;'>Aplikasi ensiklopedia simpel untuk mengeksplorasi properti dan sifat unsur kimia.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tombol lurus yang simpel untuk masuk ke aplikasi utama
    if st.button("🚀 Mulai Eksplorasi Unsur", type="primary", use_container_width=True):
        st.session_state.status_masuk = True
        st.rerun()

else:
    # ===================================================
    # APLIKASI UTAMA (SETELAH TOMBOL MASUK DIKLIK)
    # ===================================================
    
    # Tombol untuk keluar / kembali ke Halaman Welcome (Ditaruh di Sidebar)
    if st.sidebar.button("🏠 Keluar ke Beranda"):
        st.session_state.status_masuk = False
        st.rerun()
        
    st.sidebar.divider()

    # --- DATASET (GOLONGAN IA & IIA) ---
    unsur_data = {
        # GOLONGAN IA
        "H": {
            "Informasi Dasar": {"Nama": "Hidrogen", "Nomor Atom": 1, "Massa Atom Relatif": 1.008, "Golongan": "IA", "Periode": 1, "Konfigurasi": "1s¹", "Kategori": "Non-logam", "Tahun": 1766, "Valensi": 1, "Keelektronegatifan": 2.20, "Titik Didih": "-252.87 °C", "Titik Lebur": "-259.16 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Netral", "Kelarutan (Air)": "1.6 mg/L", "Kelarutan (Organik)": "Sedikit larut", "Reaktivitas": "Tinggi dengan Oksigen/Halogen"},
            "Wujud Fisik": {"Wujud (25°C)": "Gas", "Warna": "Tidak Berwarna", "Massa Jenis": "0.00008988 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Bahaya": "Asfiksian jika pekat", "Piktogram GHS": "🔥 Mudah Terbakar", "Batas Paparan": "N/A"},
            "Kegunaan": "Bahan bakar roket, industri amonia, hidrogenasi minyak."
        },
        "Li": {
            "Informasi Dasar": {"Nama": "Litium", "Nomor Atom": 3, "Massa Atom Relatif": 6.94, "Golongan": "IA", "Periode": 2, "Konfigurasi": "[He] 2s¹", "Kategori": "Logam Alkali", "Tahun": 1817, "Valensi": 1, "Keelektronegatifan": 0.98, "Titik Didih": "1342 °C", "Titik Lebur": "180.5 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (LiOH)", "Kelarutan (Air)": "Bereaksi eksotermis", "Kelarutan (Organik)": "Larut dalam amonia cair", "Reaktivitas": "Sangat Reaktif dengan Air/Udara"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih Keperakan", "Massa Jenis": "0.534 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Bahaya": "Korosif pada kulit basah", "Piktogram GHS": "🔥 Korosif & Mudah Terbakar", "Batas Paparan": "0.025 mg/m³"},
            "Kegunaan": "Baterai Li-ion, paduan logam pesawat, obat bipolar."
        },
        "Na": {
            "Informasi Dasar": {"Nama": "Natrium", "Nomor Atom": 11, "Massa Atom Relatif": 22.99, "Golongan": "IA", "Periode": 3, "Konfigurasi": "[Ne] 3s¹", "Kategori": "Logam Alkali", "Tahun": 1807, "Valensi": 1, "Keelektronegatifan": 0.93, "Titik Didih": "883 °C", "Titik Lebur": "97.72 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (NaOH)", "Kelarutan (Air)": "Bereaksi hebat/meledak", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Sangat Tinggi"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat (Lunak)", "Warna": "Putih Keperakan", "Massa Jenis": "0.968 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Bahaya": "Luka bakar kimia parah", "Piktogram GHS": "🔥💥 Reaktif Air, Korosif", "Batas Paparan": "2 mg/m³"},
            "Kegunaan": "Lampu jalan, pendingin reaktor nuklir, garam dapur (senyawa NaCl)."
        },
        "K": {
            "Informasi Dasar": {"Nama": "Kalium", "Nomor Atom": 19, "Massa Atom Relatif": 39.10, "Golongan": "IA", "Periode": 4, "Konfigurasi": "[Ar] 4s¹", "Kategori": "Logam Alkali", "Tahun": 1807, "Valensi": 1, "Keelektronegatifan": 0.82, "Titik Didih": "759 °C", "Titik Lebur": "63.5 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (KOH)", "Kelarutan (Air)": "Bereaksi sangat keras/meledak disertai api", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Lebih reaktif dari Natrium"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat (Sangat Lunak)", "Warna": "Putih Keperakan", "Massa Jenis": "0.89 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi", "Bahaya": "Luka bakar parah dan ledakan kontak kulit basah", "Piktogram GHS": "🔥💥 Sangat Reaktif & Korosif", "Batas Paparan": "N/A"},
            "Kegunaan": "Pupuk (NPK), pembuatan sabun cair, industri kaca khusus."
        },
        "Rb": {
            "Informasi Dasar": {"Nama": "Rubidium", "Nomor Atom": 37, "Massa Atom Relatif": 85.47, "Golongan": "IA", "Periode": 5, "Konfigurasi": "[Kr] 5s¹", "Kategori": "Logam Alkali", "Tahun": 1861, "Valensi": 1, "Keelektronegatifan": 0.82, "Titik Didih": "688 °C", "Titik Lebur": "39.3 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa (RbOH)", "Kelarutan (Air)": "Bereaksi spontan meledak", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Sangat Tinggi, menyala spontan di udara"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat/Cair (Lunak)", "Warna": "Putih Keperakan/Sedikit Abu", "Massa Jenis": "1.53 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Bahaya": "Luka bakar termal dan kimia akibat reaksi air", "Piktogram GHS": "🔥💥 Sangat Korosif & Piroporik", "Batas Paparan": "N/A"},
            "Kegunaan": "Jam atom, penelitian biosains, sel fotolistrik."
        },
        "Cs": {
            "Informasi Dasar": {"Nama": "Sesium", "Nomor Atom": 55, "Massa Atom Relatif": 132.9, "Golongan": "IA", "Periode": 6, "Konfigurasi": "[Xe] 6s¹", "Kategori": "Logam Alkali", "Tahun": 1860, "Valensi": 1, "Keelektronegatifan": 0.79, "Titik Didih": "671 °C", "Titik Lebur": "28.5 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Sangat Basa Kuat (CsOH)", "Kelarutan (Air)": "Reaksi hebat berenergi tinggi bahkan pada es (-116°C)", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Luar biasa aktif"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat/Cair (Sangat Lunak)", "Warna": "Emas Muda/Putih", "Massa Jenis": "1.93 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sedang", "Bahaya": "Bahaya ledakan tinggi dan luka bakar instan", "Piktogram GHS": "🔥💥 Bahaya Ledakan Besar & Korosif", "Batas Paparan": "N/A"},
            "Kegunaan": "Standar detik jam atom internasional, fluida pengeboran minyak."
        },
        "Fr": {
            "Informasi Dasar": {"Nama": "Fransium", "Nomor Atom": 87, "Massa Atom Relatif": 223, "Golongan": "IA", "Periode": 7, "Konfigurasi": "[Rn] 7s¹", "Kategori": "Logam Alkali (Radioaktif)", "Tahun": 1939, "Valensi": 1, "Keelektronegatifan": 0.79, "Titik Didih": "677 °C (Prediksi)", "Titik Lebur": "27 °C (Prediksi)"},
            "Sifat Kimia & Fisik": {"pH Larutan": "N/A (Sangat tidak stabil)", "Kelarutan (Air)": "Bereaksi hebat (Teoretis)", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Paling reaktif di golongan IA namun cepat meluruh"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat (Sangat tidak stabil)", "Warna": "Metalik (Prediksi)", "Massa Jenis": "1.87 g/cm³ (Prediksi)"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Bahaya Radiasi)", "Bahaya": "Radioaktif tinggi, menghancurkan jaringan tubuh instant", "Piktogram GHS": "☢️ Bahaya Radioaktif Ekstrim", "Batas Paparan": "N/A"},
            "Kegunaan": "Hanya untuk penelitian ilmiah skala laboratorium khusus."
        },

        # GOLONGAN IIA
        "Be": {
            "Informasi Dasar": {"Nama": "Berilium", "Nomor Atom": 4, "Massa Atom Relatif": 9.012, "Golongan": "IIA", "Periode": 2, "Konfigurasi": "[He] 2s²", "Kategori": "Logam Alkali Tanah", "Tahun": 1798, "Valensi": 2, "Keelektronegatifan": 1.57, "Titik Didih": "2471 °C", "Titik Lebur": "1287 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Amfoter", "Kelarutan (Air)": "Tidak bereaksi pada suhu ruang", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Rendah pada suhu ruang, membentuk lapisan oksida"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Abu-abu Baja", "Massa Jenis": "1.85 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Karsinogenik)", "Bahaya": "Menyebabkan berylliosis (kerusakan paru-paru kronis)", "Piktogram GHS": "💀☠️ Beracun, Karsinogen", "Batas Paparan": "0.00005 mg/m³"},
            "Kegunaan": "Komponen pesawat luar angkasa, kaca jendela sinar-X, pegas arloji."
        },
        "Mg": {
            "Informasi Dasar": {"Nama": "Magnesium", "Nomor Atom": 12, "Massa Atom Relatif": 24.305, "Golongan": "IIA", "Periode": 3, "Konfigurasi": "[Ne] 3s²", "Kategori": "Logam Alkali Tanah", "Tahun": 1755, "Valensi": 2, "Keelektronegatifan": 1.31, "Titik Didih": "1090 °C", "Titik Lebur": "650 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Basa Lemah", "Kelarutan (Air)": "Bereaksi lambat dengan air dingin, cepat dengan uap air", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Mudah terbakar di udara dengan cahaya putih terang"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih Keperakan", "Massa Jenis": "1.738 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Bahaya": "Serbuk halus mudah meledak/terbakar, debu mengiritasi mata", "Piktogram GHS": "🔥 Mudah Terbakar (Logam)", "Batas Paparan": "10 mg/m³ (debu oksida)"},
            "Kegunaan": "Paduan logam otomotif (ringan), kembang api, obat maag (Mg(OH)2)."
        },
        "Ca": {
            "Informasi Dasar": {"Nama": "Kalsium", "Nomor Atom": 20, "Massa Atom Relatif": 40.078, "Golongan": "IIA", "Periode": 4, "Konfigurasi": "[Ar] 4s²", "Kategori": "Logam Alkali Tanah", "Tahun": 1808, "Valensi": 2, "Keelektronegatifan": 1.00, "Titik Didih": "1484 °C", "Titik Lebur": "842 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Basa Kuat (Ca(OH)2)", "Kelarutan (Air)": "Bereaksi sedang dengan air membentuk gas H2", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Reaktif, perlahan kusam di udara terbuka"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat (Agak Keras)", "Warna": "Putih Keperakan / Abu kekuningan", "Massa Jenis": "1.54 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Rendah", "Bahaya": "Reaksi senyawa oksida (semen basah) iritatif/korosif kulit", "Piktogram GHS": "⚠️ Iritan, Korosif jika basah", "Batas Paparan": "2 mg/m³"},
            "Kegunaan": "Industri semen/bangunan, nutrisi tulang, agen pereduksi ekstraksi logam."
        },
        "Sr": {
            "Informasi Dasar": {"Nama": "Stronsium", "Nomor Atom": 38, "Massa Atom Relatif": 87.62, "Golongan": "IIA", "Periode": 5, "Konfigurasi": "[Kr] 5s²", "Kategori": "Logam Alkali Tanah", "Tahun": 1790, "Valensi": 2, "Keelektronegatifan": 0.95, "Titik Didih": "1382 °C", "Titik Lebur": "777 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Basa Kuat", "Kelarutan (Air)": "Bereaksi giat dengan air", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Sangat reaktif, menyala merah terang saat dibakar"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Kuning Keperakan", "Massa Jenis": "2.64 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Rendah (Isotop stabil), Tinggi (Isotop Sr-90 radioaktif)", "Bahaya": "Serbuk murni mudah menyala spontan", "Piktogram GHS": "🔥 Reaktif Udara", "Batas Paparan": "N/A"},
            "Kegunaan": "Pewarna merah kembang api & suar darurat, magnet ferit."
        },
        "Ba": {
            "Informasi Dasar": {"Nama": "Barium", "Nomor Atom": 56, "Massa Atom Relatif": 137.33, "Golongan": "IIA", "Periode": 6, "Konfigurasi": "[Xe] 6s²", "Kategori": "Logam Alkali Tanah", "Tahun": 1808, "Valensi": 2, "Keelektronegatifan": 0.89, "Titik Didih": "1897 °C", "Titik Lebur": "727 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Basa Sangat Kuat (Ba(OH)2)", "Kelarutan (Air)": "Bereaksi sangat giat dengan air", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Sangat Tinggi, disimpan di dalam minyak"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih Keperakan / Abu-abu", "Massa Jenis": "3.51 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Tinggi (Senyawa larut)", "Bahaya": "Keracunan barium mengganggu fungsi jantung dan saraf parah", "Piktogram GHS": "☠️ Beracun", "Batas Paparan": "0.5 mg/m³"},
            "Kegunaan": "Cairan kontras pemindaian medis gastrointestinal (BaSO4), industri kaca."
        },
        "Ra": {
            "Informasi Dasar": {"Nama": "Radium", "Nomor Atom": 88, "Massa Atom Relatif": 226, "Golongan": "IIA", "Periode": 7, "Konfigurasi": "[Rn] 7s²", "Kategori": "Logam Alkali Tanah (Radioaktif)", "Tahun": 1898, "Valensi": 2, "Keelektronegatifan": 0.9, "Titik Didih": "1737 °C", "Titik Lebur": "700 °C"},
            "Sifat Kimia & Fisik": {"pH Larutan": "Basa Kuat (Teoretis)", "Kelarutan (Air)": "Bereaksi giat dengan air", "Kelarutan (Organik)": "N/A", "Reaktivitas": "Sangat reaktif, berpendar dalam gelap (luminesensi)"},
            "Wujud Fisik": {"Wujud (25°C)": "Padat", "Warna": "Putih Murni (berubah hitam terpapar udara)", "Massa Jenis": "5.5 g/cm³"},
            "Kesehatan & Keselamatan": {"Toksisitas": "Sangat Tinggi (Radioaktif)", "Bahaya": "Karsinogenik parah, akumulasi di tulang merusak sumsum", "Piktogram GHS": "☢️ Bahaya Radioaktif", "Batas Paparan": "N/A"},
            "Kegunaan": "Dahulu untuk cat menyala gelap (kini dilarang), terapi kanker target khusus."
        }
    }

    # --- LAYOUT TABEL PERIODIK INTERAKTIF ---
    st.title("Tabel Periodik Unsur Kimia Interaktif ⚛️")
    st.caption("Klik tombol simbol unsur di bawah ini untuk melihat detail lengkapnya.")

    st.markdown("### 📅 Golongan IA & IIA")

    # Membuat grid tombol tabel periodik
    c1, c2, c3, c4 = st.columns([1, 1, 1, 7])

    with c1:
        st.subheader("Golongan IA")
        if st.button("H (1)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "H" else "secondary"):
            st.session_state.unsur_terpilih = "H"
        if st.button("Li (3)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Li" else "secondary"):
            st.session_state.unsur_terpilih = "Li"
        if st.button("Na (11)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Na" else "secondary"):
            st.session_state.unsur_terpilih = "Na"
        if st.button("K (19)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "K" else "secondary"):
            st.session_state.unsur_terpilih = "K"
        if st.button("Rb (37)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Rb" else "secondary"):
            st.session_state.unsur_terpilih = "Rb"
        if st.button("Cs (55)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Cs" else "secondary"):
            st.session_state.unsur_terpilih = "Cs"
        if st.button("Fr (87)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Fr" else "secondary"):
            st.session_state.unsur_terpilih = "Fr"

    with c2:
        st.subheader("Golongan IIA")
        st.write("") # Pengisi jarak agar baris sejajar Periode 2
        if st.button("Be (4)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Be" else "secondary"):
            st.session_state.unsur_terpilih = "Be"
        if st.button("Mg (12)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Mg" else "secondary"):
            st.session_state.unsur_terpilih = "Mg"
        if st.button("Ca (20)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Ca" else "secondary"):
            st.session_state.unsur_terpilih = "Ca"
        if st.button("Sr (38)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Sr" else "secondary"):
            st.session_state.unsur_terpilih = "Sr"
        if st.button("Ba (56)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Ba" else "secondary"):
            st.session_state.unsur_terpilih = "Ba"
        if st.button("Ra (88)", use_container_width=True, type="primary" if st.session_state.unsur_terpilih == "Ra" else "secondary"):
            st.session_state.unsur_terpilih = "Ra"

    # --- TAMPILAN INFORMASI DETAIL UNSUR YANG DIKLIK ---
    st.divider()

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
            st.warning(f"**Piktogram Keselamatan GHS:** {unsur_aktif['Kesehatan & Keselamatan']['Piktogram GHS']}")
            st.markdown(f"**Tingkat Toksisitas:** {unsur_aktif['Kesehatan & Keselamatan']['Toksisitas']}")
            st.markdown(f"**Bahaya Kesehatan:** {unsur_aktif['Kesehatan & Keselamatan']['Bahaya']}")
            st.markdown(f"**Batas Paparan Kerja:** {unsur_aktif['Kesehatan & Keselamatan']['Batas Paparan']}")

        with tab5:
            st.info(f"💡 **Kegunaan Utama di Dunia Nyata:** {unsur_aktif['Kegunaan']}")
