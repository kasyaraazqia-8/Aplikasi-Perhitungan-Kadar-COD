import streamlit as st

# ================= SETTING =================
st.set_page_config(
    page_title="Aplikasi COD Air",
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

# ================= NAVIGASI =================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["🏠 Beranda", "🧪 Analisis COD"]
)

# ================= BAKU MUTU COD PP 22/2021 =================
baku_mutu_cod = {
    "Kelas I": 10,
    "Kelas II": 25,
    "Kelas III": 50,
    "Kelas IV": 100
}

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.title("💧 Aplikasi Analisis COD (Chemical Oxygen Demand)")

    st.markdown("""
    <div class="card">
    <h3>Selamat Datang 👋</h3>
    Aplikasi ini digunakan untuk:
    <ul>
        <li>Menganalisis nilai COD (mg/L)</li>
        <li>Membandingkan dengan baku mutu PP No. 22 Tahun 2021</li>
        <li>Menentukan status: memenuhi / tidak memenuhi</li>
    </ul>

    <b>Satuan:</b> mg/L
    </div>
    """, unsafe_allow_html=True)

# ================= ANALISIS COD =================
elif menu == "🧪 Analisis COD":

    st.title("🧪 Analisis COD Air")

    # -------- PILIH JENIS AIR --------
    jenis_air = st.selectbox(
        "🌊 Jenis Air",
        ["Inlet IPAL", "Outlet IPAL", "Air Sungai / Badan Air"]
    )

    # -------- PILIH KELAS --------
    kelas = st.selectbox(
        "📌 Kelas Baku Mutu (PP 22/2021)",
        list(baku_mutu_cod.keys())
    )

    st.markdown("---")

    # -------- INPUT COD --------
    cod = st.number_input("Masukkan nilai COD (mg/L)", min_value=0.0)

    # ================= PROSES =================
    if st.button("🔍 Analisis COD"):

        batas = baku_mutu_cod[kelas]

        status_lolos = cod <= batas

        st.markdown("## 📊 HASIL ANALISIS")

        st.write(f"🌊 Jenis Air: **{jenis_air}**")
        st.write(f"📌 Kelas Acuan: **{kelas}**")

        st.markdown("---")

        # ================= HASIL =================
        if status_lolos:
            st.success("✅ MEMENUHI BAKU MUTU COD")

            deskripsi = (
                "Nilai COD masih berada di bawah ambang batas baku mutu. "
                "Kualitas air tergolong aman sesuai PP No. 22 Tahun 2021."
            )
        else:
            st.error("❌ TIDAK MEMENUHI BAKU MUTU COD")

            deskripsi = (
                "Nilai COD melebihi ambang batas baku mutu. "
                "Menunjukkan adanya pencemaran organik yang tinggi dan perlu pengolahan IPAL."
            )

        st.info(deskripsi)

        # ================= DETAIL =================
        st.markdown("### 📌 Detail COD")

        st.write("💧 COD aktual:", cod, "mg/L")
        st.write("📏 Batas baku mutu:", batas, "mg/L")

        if status_lolos:
            st.write("Status: ✔ Sesuai standar")
        else:
            st.write("Status: ❌ Melebihi standar")
