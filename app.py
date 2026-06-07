import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Sistem Evaluasi COD Air",
    page_icon="💧",
    layout="wide"
)

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #dff6ff,
        #b8e8fc,
        #7fd8ff
    );
}

.block-container{
    background:white;
    padding:2rem;
    border-radius:20px;
    box-shadow:0px 0px 20px rgba(0,0,0,0.15);
}

[data-testid="stSidebar"]{
    background:#003366;
}

[data-testid="stSidebar"] *{
    color:white;
}

.banner{
    background:linear-gradient(
        135deg,
        #0077b6,
        #00b4d8
    );
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.card{
    background:#f8fbff;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #0077b6;
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
        "🧮 Perhitungan COD",
        "📚 Referensi"
    ]
)

# =====================================
# BERANDA
# =====================================
if menu == "🏠 Beranda":

    st.markdown("""
    <div class="banner">
        <h1>💧 SISTEM PERHITUNGAN KADAR COD AIR</h1>
        <h3>PP Nomor 22 Tahun 2021</h3>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1527066236128-2ff79f7b9705",
        use_container_width=True
    )

    st.markdown("""
    <div class="card">
    <h3>Fungsi Aplikasi</h3>

    ✅ Menghitung COD dari data titrasi

    ✅ Membandingkan dengan baku mutu kualitas air

    ✅ Menentukan kesesuaian kualitas air

    ✅ Mengacu pada PP No. 22 Tahun 2021
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Rumus COD")

    st.latex(
        r"COD=\frac{(A-B)\times N\times8000}{V}"
    )

# =====================================
# PERHITUNGAN COD
# =====================================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD")

    nama = st.text_input("Nama Sampel")

    jenis_air = st.selectbox(
        "Jenis Air",
        [
            "Air Baku Air Minum (Kelas 1)",
            "Rekreasi Air (Kelas 2)",
            "Perikanan (Kelas 3)",
            "Irigasi/Pertanian (Kelas 4)"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        A = st.number_input(
            "Volume Blanko (A) mL",
            min_value=0.00,
            format="%.2f"
        )

        B = st.number_input(
            "Volume Sampel (B) mL",
            min_value=0.00,
            format="%.2f"
        )

    with col2:
        N = st.number_input(
            "Normalitas FAS (N)",
            min_value=0.00,
            format="%.2f"
        )

        V = st.number_input(
            "Volume Sampel (V) mL",
            min_value=0.01,
            format="%.2f"
        )

    if st.button("Hitung COD"):

        cod = ((A - B) * N * 8000) / V

        if "Kelas 1" in jenis_air:
            baku = 10

        elif "Kelas 2" in jenis_air:
            baku = 25

        elif "Kelas 3" in jenis_air:
            baku = 50

        else:
            baku = 100

        st.subheader("📋 Hasil Perhitungan")

        st.write(f"Nama Sampel : {nama}")
        st.write(f"Jenis Air : {jenis_air}")

        st.latex(
            rf"COD=\frac{{({A}-{B})\times{N}\times8000}}{{{V}}}"
        )

        st.metric(
            "Hasil COD",
            f"{cod:.4f} mg/L"
        )

        st.write(
            f"Baku Mutu COD : {baku} mg/L"
        )

        if cod <= baku:

            st.success(
                f"""
                MEMENUHI BAKU MUTU

                COD = {cod:.4f} mg/L

                ≤ {baku} mg/L
                """
            )

        else:

            st.error(
                f"""
                TIDAK MEMENUHI BAKU MUTU

                COD = {cod:.4f} mg/L

                > {baku} mg/L
                """
            )

# =====================================
# REFERENSI
# =====================================
elif menu == "📚 Referensi":

    st.title("📚 Referensi Baku Mutu COD")

    st.table({
        "Kelas":[
            "Kelas 1",
            "Kelas 2",
            "Kelas 3",
            "Kelas 4"
        ],
        "Peruntukan":[
            "Air Baku Air Minum",
            "Rekreasi Air",
            "Perikanan",
            "Irigasi/Pertanian"
        ],
        "COD Maksimum (mg/L)":[
            10,
            25,
            50,
            100
        ]
    })

    st.info(
        "Acuan: PP Nomor 22 Tahun 2021."
    )
