import streamlit as st
import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Tabel Periodik Interaktif", page_icon="🧪", layout="wide")

st.title("🧪 Tabel Periodik Unsur Kimia Interaktif")
st.markdown("Pilih unsur kimia dari *dropdown* di bawah ini untuk melihat detail lengkapnya. (Data contoh meliputi sebagian unsur Golongan IA)")
st.divider()

# 2. Dataset Contoh: Golongan IA
unsur_data = {
    "Hidrogen": {
        "Informasi Dasar": {
            "Simbol": "H", "Nomor Atom": 1, "Massa Atom Relatif": 1.008,
            "Golongan": "IA", "Periode": 1, "Konfigurasi Elektron": "1s¹",
            "Kategori Unsur": "Non-logam", "Tahun Ditemukan": 1766,
            "Valensi": 1, "Kelektronegatifan": 2.20,
            "Titik Didih": "-252.87 °C", "Titik Lebur": "-259.16 °C"
        },
        "Sifat Kimia & Fisik": {
            "pH Larutan": "Netral (dalam air)", 
            "Kelarutan (Air)": "1.6 mg/L (20°C)",
            "Kelarutan (Organik)": "Sedikit larut", 
            "Reaktivitas": "Sangat reaktif dengan unsur halogen dan oksigen."
        },
        "Wujud Fisik": {
            "Wujud (25°C)": "Gas", "Warna": "Tidak berwarna", "Massa Jenis": "0.00008988 g/cm³"
        },
        "Kesehatan & Keselamatan": {
            "Tingkat Toksisitas": "Rendah (Asfiksian ringan)", 
            "Bahaya Kesehatan": "Dapat menyebabkan sesak napas dalam konsentrasi tinggi karena menggantikan oksigen.",
            "Piktogram GHS": "🔥 (Gas Mudah Terbakar)", 
            "Batas Paparan": "Tidak ada batas spesifik, pastikan kadar oksigen > 19.5%"
        },
        "Kegunaan": "Sintesis amonia, pemurnian minyak bumi, bahan bakar hidrogen, dan pendingin generator."
    },
    "Litium": {
        "Informasi Dasar": {
            "Simbol": "Li", "Nomor Atom": 3, "Massa Atom Relatif": 6.94,
            "Golongan": "IA", "Periode": 2, "Konfigurasi Elektron": "[He] 2s¹",
            "Kategori Unsur": "Logam Alkali", "Tahun Ditemukan": 1817,
            "Valensi": 1, "Kelektronegatifan": 0.98,
            "Titik Didih": "1342 °C", "Titik Lebur": "180.5 °C"
        },
        "Sifat Kimia & Fisik": {
            "pH Larutan": "Sangat Basa (membentuk LiOH dalam air)", 
            "Kelarutan (Air)": "Bereaksi eksotermis (membentuk gas hidrogen)",
            "Kelarutan (Organik)": "Larut dalam amonia cair", 
            "Reaktivitas": "Reaktif terhadap air dan oksigen, harus disimpan dalam minyak."
        },
        "Wujud Fisik": {
            "Wujud (25°C)": "Padat", "Warna": "Putih keperakan", "Massa Jenis": "0.534 g/cm³"
        },
        "Kesehatan & Keselamatan": {
            "Tingkat Toksisitas": "Sedang hingga Tinggi", 
            "Bahaya Kesehatan": "Sangat korosif. Reaksi dengan uap air di kulit menyebabkan luka bakar kimia.",
            "Piktogram GHS": "☠️🔥 (Korosif, Mudah Terbakar, Beracun)", 
            "Batas Paparan": "0.025 mg/m³ (sebagai hidrida/hidroksida)"
        },
        "Kegunaan": "Pembuatan baterai ion-litium, paduan logam untuk pesawat terbang, pengobatan gangguan bipolar (Litium karbonat)."
    },
    "Natrium": {
        "Informasi Dasar": {
            "Simbol": "Na", "Nomor Atom": 11, "Massa Atom Relatif": 22.99,
            "Golongan": "IA", "Periode": 3, "Konfigurasi Elektron": "[Ne] 3s¹",
            "Kategori Unsur": "Logam Alkali", "Tahun Ditemukan": 1807,
            "Valensi": 1, "Kelektronegatifan": 0.93,
            "Titik Didih": "883 °C", "Titik Lebur": "97.72 °C"
        },
        "Sifat Kimia & Fisik": {
            "pH Larutan": "Sangat Basa (membentuk NaOH)", 
            "Kelarutan (Air)": "Bereaksi sangat keras/meledak di air",
            "Kelarutan (Organik)": "Tidak larut dalam pelarut organik biasa", 
            "Reaktivitas": "Sangat reaktif terhadap air dan kelembapan udara."
        },
        "Wujud Fisik": {
            "Wujud (25°C)": "Padat (Lunak)", "Warna": "Putih keperakan", "Massa Jenis": "0.968 g/cm³"
        },
        "Kesehatan & Keselamatan": {
            "Tingkat Toksisitas": "Tinggi", 
            "Bahaya Kesehatan": "Luka bakar termal dan kimia yang sangat parah jika terkena kulit basah.",
            "Piktogram GHS": "💥🔥 (Eksplosif dengan Air, Korosif)", 
            "Batas Paparan": "2 mg/m³ (sebagai NaOH)"
        },
        "Kegunaan": "Lampu jalan (lampu uap natrium), pendingin reaktor nuklir, sintesis bahan kimia, dan garam dapur (sebagai senyawa NaCl)."
    }
}

# 3. Antarmuka Pencarian / Pemilihan
daftar_unsur = list(unsur_data.keys())
unsur_terpilih = st.selectbox("🔍 Cari dan Pilih Unsur Kimia:", daftar_unsur)

# Ambil data berdasarkan unsur yang dipilih
data = unsur_data[unsur_terpilih]

st.header(f"{unsur_terpilih} ({data['Informasi Dasar']['Simbol']})")

# 4. Membuat Tabs untuk Kategorisasi Informasi
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📑 Informasi Dasar", 
    "🧪 Sifat Kimia & Fisik", 
    "🧊 Wujud Fisik", 
    "⚠️ Kesehatan & Keselamatan", 
    "🏭 Kegunaan"
])

# Fungsi bantuan untuk merender dictionary ke dalam 2 kolom agar rapi
def render_dict_to_columns(data_dict):
    col1, col2 = st.columns(2)
    items = list(data_dict.items())
    mid = (len(items) + 1) // 2
    for k, v in items[:mid]:
        col1.markdown(f"**{k}:** {v}")
    for k, v in items[mid:]:
        col2.markdown(f"**{k}:** {v}")

# Tab 1: Informasi Dasar
with tab1:
    st.subheader("Data Dasar Unsur")
    render_dict_to_columns(data["Informasi Dasar"])

# Tab 2: Sifat Kimia & Fisik
with tab2:
    st.subheader("Reaktivitas dan Sifat Lainnya")
    render_dict_to_columns(data["Sifat Kimia & Fisik"])

# Tab 3: Wujud Fisik
with tab3:
    st.subheader("Keadaan Fisik pada Suhu Ruang")
    render_dict_to_columns(data["Wujud Fisik"])

# Tab 4: Kesehatan & Keselamatan
with tab4:
    st.subheader("Protokol Keselamatan dan Bahaya")
    # Menggunakan expander untuk informasi tambahan di dalam tab ini
    for k, v in data["Kesehatan & Keselamatan"].items():
        if k == "Piktogram GHS":
            st.warning(f"**{k}:** {v}")
        else:
            st.markdown(f"**{k}:** {v}")

# Tab 5: Kegunaan
with tab5:
    st.subheader("Aplikasi di Dunia Nyata")
    st.info(data["Kegunaan"])
