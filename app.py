import streamlit as st

# ================= SETTING =================
st.set_page_config(
    page_title="COD Analysis IPAL",
    page_icon="💧",
    layout="wide"
)

# ================= BACKGROUND + STYLE =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dbeafe, #f0f9ff, #e0f2fe);
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

h1, h2, h3 {
    color: #0f172a;
}

.big-text {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["🏠 Beranda", "🧪 Analisis COD"]
)

# ================= BAKU MUTU COD =================
baku_mutu = {
    "Kelas I (Air baku minum)": 10,
    "Kelas II (Rekreasi/ikan)": 25,
    "Kelas III (Peternakan/ikan)": 50,
    "Kelas IV (Irigasi)": 100
}

# ================= BERANDA =================
if menu == "🏠 Beranda":
    st.title("💧 Aplikasi Analisis COD IPAL")

    st.markdown("""
    <div class="card">
    <h3>🌊 Apa itu Kelas Air?</h3>

    <b>Kelas I</b> → Air baku air minum (paling bersih)<br>
    <b>Kelas II</b> → Rekreasi & perikanan air tawar<br>
    <b>Kelas III</b> → Peternakan & budidaya ikan<br>
    <b>Kelas IV</b> → Irigasi pertanian

    <hr>

    Aplikasi ini digunakan untuk:
    <ul>
        <li>Menghitung COD inlet & outlet</li>
        <li>Menghitung efisiensi IPAL</li>
        <li>Mengevaluasi apakah memenuhi baku mutu PP 22/2021</li>
    </ul>

    <b>Satuan:</b> mg/L
    </div>
    """, unsafe_allow_html=True)

# ================= ANALISIS =================
elif menu == "🧪 Analisis COD":

    st.title("🧪 Analisis COD IPAL")

    jenis_air = st.selectbox(
        "🌊 Jenis Air",
        ["Inlet IPAL", "Outlet IPAL", "Air Sungai"]
    )

    kelas = st.selectbox(
        "📌 Kelas Baku Mutu",
        list(baku_mutu.keys())
    )

    st.markdown("---")

    cod_in = st.number_input("COD Inlet (mg/L)", min_value=0.0)
    cod_out = st.number_input("COD Outlet (mg/L)", min_value=0.0)

    if st.button("🔍 Analisis COD"):

        batas = baku_mutu[kelas]

        # ================= PERHITUNGAN =================
        penurunan = cod_in - cod_out

        if cod_in > 0:
            efisiensi = (penurunan / cod_in) * 100
        else:
            efisiensi = 0

        # ================= STATUS BAKU MUTU =================
        lolos = cod_out <= batas

        # ================= EVALUASI KUALITAS =================
        if cod_out <= 25:
            status_air = "Baik (Tidak tercemar berat)"
        elif cod_out <= 50:
            status_air = "Sedang (Tercemar ringan–sedang)"
        else:
            status_air = "Buruk (Tercemar berat)"

        # ================= OUTPUT =================
        st.markdown("## 📊 HASIL ANALISIS")

        st.write(f"🌊 Jenis Air: **{jenis_air}**")
        st.write(f"📌 Kelas Acuan: **{kelas}**")

        st.markdown("### 🧪 Nilai COD")
        st.write("Inlet :", cod_in, "mg/L")
        st.write("Outlet:", cod_out, "mg/L")

        st.markdown("### 📉 Hasil Perhitungan")
        st.write("Penurunan COD:", penurunan, "mg/L")
        st.write("Efisiensi IPAL:", round(efisiensi, 2), "%")

        st.markdown("### 🧠 Evaluasi Kualitas Air")
        st.info(status_air)

        st.markdown("### 📌 Kesesuaian Baku Mutu")

        if lolos:
            st.success("✅ MEMENUHI BAKU MUTU PP 22/2021")
            kesimpulan = "Air sudah sesuai standar lingkungan dan aman dibuang."
        else:
            st.error("❌ TIDAK MEMENUHI BAKU MUTU")
            kesimpulan = "Perlu pengolahan lanjutan sebelum dibuang ke lingkungan."

        st.info(kesimpulan)

        st.markdown("---")
        st.write(f"📏 Baku mutu {kelas}: {batas} mg/L")
