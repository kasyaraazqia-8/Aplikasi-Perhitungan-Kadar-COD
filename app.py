import streamlit as st

# ---------------- SETTING UI ----------------
st.set_page_config(page_title="Aplikasi COD Air", page_icon="💧", layout="wide")

# Background CSS biar tidak kosong
page_bg = """
<style>
.stApp {
    background: linear-gradient(to right, #dbeafe, #f0f9ff);
}
h1, h2, h3 {
    color: #0f172a;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------------- SIDEBAR NAVIGASI ----------------
menu = st.sidebar.selectbox(
    "📌 Navigasi",
    ["🏠 Beranda", "🧪 Kalkulator COD", "📊 Info Baku Mutu"]
)

# ---------------- DATA BAKU MUTU PP 22/2021 ----------------
baku_mutu = {
    "Kelas I (Air baku air minum)": 10,
    "Kelas II (Wisata/rekreasi)": 25,
    "Kelas III (Perikanan)": 50,
    "Kelas IV (Pertanian/irigasi)": 100
}

# ---------------- BERANDA ----------------
if menu == "🏠 Beranda":
    st.title("💧 Aplikasi Perhitungan COD Air Limbah")
    
    st.markdown("""
    <div class="card">
    <h3>Selamat datang 👋</h3>
    Aplikasi ini digunakan untuk:
    <ul>
        <li>Menghitung nilai COD (Chemical Oxygen Demand)</li>
        <li>Membandingkan hasil dengan baku mutu PP No. 22 Tahun 2021</li>
        <li>Mengklasifikasikan kualitas air</li>
    </ul>
    <b>Satuan hasil:</b> mg/L
    </div>
    """, unsafe_allow_html=True)

# ---------------- KALKULATOR COD ----------------
elif menu == "🧪 Kalkulator COD":
    st.title("🧪 Kalkulator COD Inlet - Outlet")

    st.markdown("Masukkan nilai COD dari hasil pengukuran:")

    cod_inlet = st.number_input("COD Inlet (mg/L)", min_value=0.0)
    cod_outlet = st.number_input("COD Outlet (mg/L)", min_value=0.0)

    if st.button("Hitung COD"):
        if cod_inlet > 0:

            penurunan = cod_inlet - cod_outlet
            efisiensi = (penurunan / cod_inlet) * 100

            st.success(f"Penurunan COD = {penurunan:.2f} mg/L")
            st.success(f"Efisiensi penyisihan = {efisiensi:.2f} %")

            # Klasifikasi outlet berdasarkan PP 22/2021
            if cod_outlet <= 10:
                status = "Kelas I (Sangat baik)"
            elif cod_outlet <= 25:
                status = "Kelas II"
            elif cod_outlet <= 50:
                status = "Kelas III"
            elif cod_outlet <= 100:
                status = "Kelas IV"
            else:
                status = "Di atas baku mutu (tercemar)"

            st.info(f"Kualitas air outlet: {status}")

        else:
            st.error("COD inlet tidak boleh 0")

# ---------------- INFO BAKU MUTU ----------------
elif menu == "📊 Info Baku Mutu":
    st.title("📊 Baku Mutu COD (PP No. 22 Tahun 2021)")

    st.markdown("""
    <div class="card">
    <h3>Standar COD berdasarkan kelas air:</h3>
    </div>
    """, unsafe_allow_html=True)

    for k, v in baku_mutu.items():
        st.write(f"💧 **{k}** : {v} mg/L")

    st.markdown("""
    <br>
    <i>Sumber: PP No. 22 Tahun 2021 tentang Penyelenggaraan Perlindungan dan Pengelolaan Lingkungan Hidup</i>
    """, unsafe_allow_html=True)
