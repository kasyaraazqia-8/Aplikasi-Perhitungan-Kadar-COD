import streamlit as st

# ======================================
# KONFIGURASI HALAMAN
# ======================================
st.set_page_config(
    page_title="Sistem Perhitungan COD Air",
    page_icon="💧",
    layout="wide"
)

# ======================================
# CSS & BACKGROUND
# ======================================
st.markdown("""
<style>

st.markdown("""
<style>

/* Background Air */
.stApp{
    background-image: url("https://images.unsplash.com/photo-1544551763-46a013bb70d5");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Efek gelap transparan agar teks tetap terbaca */
.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.25);
    z-index:-1;
}

/* Kotak konten */
.block-container{
    background:rgba(255,255,255,0.75);
    padding:2rem;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.3);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:rgba(0,51,102,0.95);
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Judul */
h1,h2,h3{
    color:#003366;
    font-weight:bold;
}

/* Tombol */
.stButton > button{
    background:#0099ff;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# SIDEBAR
# ======================================
menu = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Beranda",
        "🧮 Perhitungan COD",
        "📚 Referensi Baku Mutu"
    ]
)

# ======================================
# BERANDA
# ======================================
if menu == "🏠 Beranda":

    st.title("💧 Sistem Perhitungan dan Evaluasi COD Air")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk:

    ✅ Menghitung COD dari data titrasi

    ✅ Membandingkan hasil COD dengan baku mutu

    ✅ Menentukan kesesuaian kualitas air

    ✅ Mengacu pada PP Nomor 22 Tahun 2021

    ---
    """)

    st.info("""
    Rumus COD yang digunakan:

    COD = ((A - B) × N × 8000) / V

    A = Volume blanko (mL)

    B = Volume sampel (mL)

    N = Normalitas FAS

    V = Volume sampel yang digunakan (mL)
    """)

# ======================================
# PERHITUNGAN COD
# ======================================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD")

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

    A = st.number_input(
        "Volume Blanko (A) (mL)",
        min_value=0.0,
        format="%.2f"
    )

    B = st.number_input(
        "Volume Sampel (B) (mL)",
        min_value=0.0,
        format="%.2f"
    )

    N = st.number_input(
        "Normalitas FAS (N)",
        min_value=0.000,
        format="%.3f"
    )

    V = st.number_input(
        "Volume Sampel (V) (mL)",
        min_value=0.1,
        format="%.2f"
    )

    if st.button("Hitung COD"):

        cod = ((A - B) * N * 8000) / V

        if "Kelas 1" in jenis_air:
            baku_mutu = 10

        elif "Kelas 2" in jenis_air:
            baku_mutu = 25

        elif "Kelas 3" in jenis_air:
            baku_mutu = 50

        else:
            baku_mutu = 100

        st.subheader("📋 Hasil Perhitungan")

        st.write(f"Nama Sampel : {nama}")
        st.write(f"Jenis Air : {jenis_air}")

        st.markdown("### Perhitungan")

        st.latex(
            rf"COD=\frac{{({A}-{B}) \times {N} \times 8000}}{{{V}}}"
        )

        st.success(
            f"Hasil COD = {cod:.2f} mg/L"
        )

        st.markdown("### Evaluasi Baku Mutu")

        st.write(
            f"Baku Mutu COD = {baku_mutu} mg/L"
        )

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

# ======================================
# REFERENSI
# ======================================
elif menu == "📚 Referensi Baku Mutu":

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

    st.info("""
    Interpretasi:

    Kelas 1 = Air baku air minum

    Kelas 2 = Rekreasi air

    Kelas 3 = Perikanan

    Kelas 4 = Irigasi/Pertanian
    """)
