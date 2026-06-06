import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Evaluasi Kadar COD Air",
    page_icon="💧",
    layout="wide"
)

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}

.block-container{
    background: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 20px;
}

[data-testid="stSidebar"]{
    background-color:#003366;
}

[data-testid="stSidebar"] *{
    color:white;
}

h1,h2,h3{
    color:#003366;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "🧮 Evaluasi COD",
        "📚 Referensi"
    ]
)

# =====================================
# BERANDA
# =====================================
if menu == "🏠 Beranda":

    st.title("💧 Sistem Evaluasi Kadar COD Air")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk mengevaluasi kualitas air berdasarkan parameter **Chemical Oxygen Demand (COD)**.

    Hasil COD akan dibandingkan dengan baku mutu sesuai **PP Nomor 22 Tahun 2021** berdasarkan kelas dan peruntukan air.
    """)

    st.info("""
    Pilih menu Evaluasi COD untuk mulai melakukan penilaian kualitas air.
    """)

# =====================================
# EVALUASI COD
# =====================================
elif menu == "🧮 Evaluasi COD":

    st.title("🧮 Evaluasi Kadar COD")

    nama = st.text_input("Nama Sampel")

    jenis_air = st.selectbox(
        "Pilih Jenis Air",
        [
            "Air Baku Air Minum (Kelas 1)",
            "Rekreasi Air (Kelas 2)",
            "Perikanan (Kelas 3)",
            "Irigasi / Pertanian (Kelas 4)"
        ]
    )

    cod = st.number_input(
        "Masukkan Nilai COD (mg/L)",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Evaluasi"):

        if "Kelas 1" in jenis_air:
            baku_mutu = 10

        elif "Kelas 2" in jenis_air:
            baku_mutu = 25

        elif "Kelas 3" in jenis_air:
            baku_mutu = 50

        else:
            baku_mutu = 100

        st.subheader("📋 Hasil Evaluasi")

        st.write(f"**Nama Sampel:** {nama}")
        st.write(f"**Jenis Air:** {jenis_air}")
        st.write(f"**COD Hasil:** {cod:.2f} mg/L")
        st.write(f"**Baku Mutu COD:** {baku_mutu} mg/L")

        if cod <= baku_mutu:

            st.success(
                f"""
                ✅ MEMENUHI BAKU MUTU

                COD = {cod:.2f} mg/L

                Baku Mutu = {baku_mutu} mg/L
                """
            )

        else:

            st.error(
                f"""
                ❌ TIDAK MEMENUHI BAKU MUTU

                COD = {cod:.2f} mg/L

                Baku Mutu = {baku_mutu} mg/L
                """
            )

# =====================================
# REFERENSI
# =====================================
elif menu == "📚 Referensi":

    st.title("📚 Referensi Baku Mutu COD")

    st.write("""
    Acuan: PP Nomor 22 Tahun 2021
    """)

    st.table({
        "Kelas": [
            "Kelas 1",
            "Kelas 2",
            "Kelas 3",
            "Kelas 4"
        ],
        "Peruntukan": [
            "Air Baku Air Minum",
            "Rekreasi Air",
            "Perikanan",
            "Irigasi / Pertanian"
        ],
        "COD (mg/L)": [
            "≤ 10",
            "≤ 25",
            "≤ 50",
            "≤ 100"
        ]
    })
