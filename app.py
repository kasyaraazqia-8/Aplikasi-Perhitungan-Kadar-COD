import streamlit as st

# ================= SETTING =================
st.set_page_config(
    page_title="Analisis COD IPAL",
    page_icon="💧",
    layout="wide"
)

# ================= BACKGROUND GAMBAR =================
# GANTI nama file gambar sesuai punyamu
bg_image = "water_bg.jpg"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.card {{
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    backdrop-filter: blur(5px);
}}

h1, h2, h3 {{
    color: #0f172a;
}}
</style>
""", unsafe_allow_html=True)

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["🏠 Beranda", "🧪 Analisis COD"]
)

# ================= BAKU MUTU =================
baku_mutu = {
    "Kelas I (Air baku minum)": 10,
    "Kelas II (Rekreasi/perikanan)": 25,
    "Kelas III (Budidaya ikan)": 50,
    "Kelas IV (Irigasi)": 100
}

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.title("💧 Analisis COD IPAL")

    st.markdown("""
    <div class="card">
    <h3>🌊 Kelas Air (PP 22/2021)</h3>

    <b>Kelas I</b> → Air baku minum<br>
    <b>Kelas II</b> → Rekreasi & perikanan<br>
    <b>Kelas III</b> → Budidaya ikan<br>
    <b>Kelas IV</b> → Irigasi

    <hr>

    Aplikasi ini digunakan untuk:
    <ul>
        <li>Perhitungan COD inlet & outlet</li>
        <li>Efisiensi IPAL (%)</li>
        <li>Evaluasi baku mutu</li>
    </ul>

    <b>Satuan:</b> mg/L
    </div>
    """, unsafe_allow_html=True)

# ================= ANALISIS =================
elif menu == "🧪 Analisis COD":

    st.title("🧪 Analisis COD IPAL")

    kelas = st.selectbox(
        "📌 Pilih Kelas Baku Mutu",
        list(baku_mutu.keys())
    )

    cod_in = st.number_input("COD Inlet (mg/L)", min_value=0.0)
    cod_out = st.number_input("COD Outlet (mg/L)", min_value=0.0)

    if st.button("🔍 Analisis COD"):

        batas = baku_mutu[kelas]

        # ================= HITUNG =================
        penurunan = cod_in - cod_out
        efisiensi = (penurunan / cod_in * 100) if cod_in > 0 else 0

        # ================= STATUS =================
        lolos = cod_out <= batas

        if cod_out <= 25:
            status = "Baik (relatif tidak tercemar)"
        elif cod_out <= 50:
            status = "Sedang (tercemar ringan–sedang)"
        else:
            status = "Buruk (tercemar berat)"

        # ================= OUTPUT =================
        st.markdown("## 📊 HASIL ANALISIS")

        st.write(f"📌 Kelas Acuan: **{kelas}**")

        st.markdown("### 🧪 COD")
        st.write("Inlet :", cod_in, "mg/L")
        st.write("Outlet:", cod_out, "mg/L")

        st.markdown("### 📉 Perhitungan")
        st.write("Penurunan COD:", penurunan, "mg/L")
        st.write("Efisiensi:", round(efisiensi, 2), "%")

        st.markdown("### 🧠 Evaluasi")
        st.info(status)

        if lolos:
            st.success("✅ MEMENUHI BAKU MUTU PP 22/2021")
        else:
            st.error("❌ TIDAK MEMENUHI BAKU MUTU")

        st.write(f"📏 Baku mutu {kelas}: {batas} mg/L")
