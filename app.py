import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Sistem Perhitungan COD Air",
    page_icon="💧",
    layout="wide"
)

# ==========================================
# CSS DAN BACKGROUND
# ==========================================
st.markdown("""
<style>

/* Background gambar air */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1500375592092-40eb2168fd21?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Overlay transparan */
.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(255,255,255,0.25);
    z-index:-1;
}

/* Container utama */
.block-container{
    background:rgba(255,255,255,0.88);
    padding:2rem;
    border-radius:20px;
    box-shadow:0px 0px 20px rgba(0,0,0,0.2);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #003366,
        #0077b6
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Banner */
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

/* Card */
.card{
    background:#f5fbff;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #0077b6;
}

/* Tombol */
.stButton > button{
    width:100%;
    border-radius:10px;
    font-weight:bold;
    background:#0077b6;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# MENU
# ==========================================
menu = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Beranda",
        "🧮 Perhitungan COD",
        "📚 Referensi"
    ]
)

# ==========================================
# BERANDA
# ==========================================
if menu == "🏠 Beranda":

    st.markdown("""
    <div class="banner">
        <h1>💧 SISTEM PERHITUNGAN KADAR COD AIR</h1>
        <h3>Evaluasi Berdasarkan PP No. 22 Tahun 2021</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>Fungsi Aplikasi</h3>

    ✅ Menghitung COD dari data titrasi

    ✅ Membandingkan hasil COD dengan baku mutu

    ✅ Menentukan kesesuaian kualitas air

    ✅ Mengacu pada PP Nomor 22 Tahun 2021
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Rumus Perhitungan COD")

    st.latex(
        r"COD=\frac{(A-B)\times N\times8000}{V}"
    )

    st.write("""
    Keterangan:

    • A = Volume blanko (mL)

    • B = Volume sampel (mL)

    • N = Normalitas FAS

    • V = Volume sampel yang digunakan (mL)
    """)

# ==========================================
# PERHITUNGAN COD
# ==========================================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD")

    nama = st.text_input(
        "Nama Sampel"
    )

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
            "Volume Blanko (A) (mL)",
            min_value=0.00,
            format="%.2f"
        )

        B = st.number_input(
            "Volume Sampel (B) (mL)",
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
            "Volume Sampel (V) (mL)",
            min_value=0.01,
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

        st.markdown("### Substitusi Rumus")

        st.latex(
            rf"COD=\frac{{({A}-{B})\times{N}\times8000}}{{{V}}}"
        )

        st.metric(
            label="Hasil COD",
            value=f"{cod:.4f} mg/L"
        )

        st.write(
            f"Baku Mutu COD = {baku_mutu} mg/L"
        )

        if cod <= baku_mutu:

            st.success(
                f"""
                ✅ MEMENUHI BAKU MUTU

                COD = {cod:.4f} mg/L

                COD ≤ {baku_mutu} mg/L
                """
            )

        else:

            st.error(
                f"""
                ❌ TIDAK MEMENUHI BAKU MUTU

                COD = {cod:.4f} mg/L

                COD > {baku_mutu} mg/L
                """
            )

# ==========================================
# REFERENSI
# ==========================================
elif menu == "📚 Referensi":

    st.title("📚 Referensi Baku Mutu COD")

    st.write("Acuan: PP Nomor 22 Tahun 2021")

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
            "Irigasi/Pertanian"
        ],
        "COD Maksimum (mg/L)": [
            10,
            25,
            50,
            100
        ]
    })

    st.info("""
Kelas 1 : Air baku air minum

Kelas 2 : Rekreasi air

Kelas 3 : Perikanan

Kelas 4 : Irigasi/Pertanian
""")
