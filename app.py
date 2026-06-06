import streamlit as st

# ================= SETTING =================
st.set_page_config(
    page_title="Aplikasi COD IPAL",
    page_icon="💧",
    layout="wide"
)

# ================= STYLE =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #dbeafe, #f8fafc);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    color: #0f172a;
}
</style>
""", unsafe_allow_html=True)

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["🏠 Beranda", "🧪 Perhitungan COD"]
)

# ================= BAKU MUTU COD =================
baku_mutu_cod = {
    "Kelas I": 10,
    "Kelas II": 25,
    "Kelas III": 50,
    "Kelas IV": 100
}

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.title("💧 Aplikasi Perhitungan COD IPAL")

    st.markdown("""
    <div class="card">
    <h3>Selamat Datang 👋</h3>
    Aplikasi ini digunakan untuk:
    <ul>
        <li>Menghitung penurunan COD (inlet vs outlet)</li>
        <li>Menghitung efisiensi IPAL (%)</li>
        <li>Membandingkan dengan baku mutu PP No. 22 Tahun 2021</li>
    </ul>

    <b>Satuan:</b> mg/L
    </div>
    """, unsafe_allow_html=True)

# ================= ANALISIS COD =================
elif menu == "🧪 Perhitungan COD":

    st.title("🧪 Perhitungan COD IPAL")

    # -------- INPUT --------
    jenis_air = st.selectbox(
        "🌊 Jenis Air",
        ["Inlet IPAL", "Outlet IPAL"]
    )

    kelas = st.selectbox(
        "📌 Kelas Baku Mutu",
        list(baku_mutu_cod.keys())
    )

    st.markdown("---")

    cod_in = st.number_input("COD Inlet (mg/L)", min_value=0.0)
    cod_out = st.number_input("COD Outlet (mg/L)", min_value=0.0)

    # ================= HITUNG =================
    if st.button("🔍 Hitung COD"):

        batas = baku_mutu_cod[kelas]

        # 📌 PERHITUNGAN
        penurunan = cod_in - cod_out

        if cod_in != 0:
            efisiensi = (penurunan / cod_in) * 100
        else:
            efisiensi = 0

        # 📊 CEK BAKU MUTU (OUTLET YANG DINILAI)
        status = cod_out <= batas

        # ================= HASIL =================
        st.markdown("## 📊 HASIL PERHITUNGAN")

        st.write(f"🌊 Jenis Air: **{jenis_air}**")
        st.write(f"📌 Kelas Acuan: **{kelas}**")

        st.markdown("### 🧪 Hasil COD")

        st.write("COD Inlet :", cod_in, "mg/L")
        st.write("COD Outlet:", cod_out, "mg/L")

        st.markdown("### 📉 Perhitungan")

        st.write("Penurunan COD =", penurunan, "mg/L")
        st.write("Efisiensi =", round(efisiensi, 2), "%")

        st.markdown("---")

        # ================= STATUS =================
        if status:
            st.success("✅ MEMENUHI BAKU MUTU COD")
            kesimpulan = "COD outlet berada di bawah baku mutu, sehingga aman sesuai PP 22/2021."
        else:
            st.error("❌ TIDAK MEMENUHI BAKU MUTU COD")
            kesimpulan = "COD outlet melebihi baku mutu, perlu pengolahan lanjutan IPAL."

        st.info(kesimpulan)

        st.write(f"📏 Baku mutu kelas {kelas}: {batas} mg/L")
