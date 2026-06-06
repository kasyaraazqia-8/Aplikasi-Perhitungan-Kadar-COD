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
# CSS + BACKGROUND
# =====================================
st.markdown("""
<style>

/* Background */
.stApp{
    background-image: url("https://images.unsplash.com/photo-1500375592092-40eb2168fd21");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Kontainer utama */
.block-container{
    background: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    margin-top: 1rem;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #003366,
        #006699
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Judul */
h1{
    color:#003366;
    text-align:center;
}

h2,h3{
    color:#004d66;
}

/* Tombol */
.stButton > button{
    background-color:#0088cc;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    padding:10px 20px;
}

.stButton > button:hover{
    background-color:#006699;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================
menu = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Beranda",
        "🧮 Evaluasi COD",
        "🌊 Sarana Pengolahan Air",
        "ℹ️ Tentang COD"
    ]
)

# =====================================
# BERANDA
# =====================================
if menu == "🏠 Beranda":

    st.title("💧 SISTEM EVALUASI KADAR COD AIR")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk:

    ✅ Mengevaluasi hasil COD laboratorium

    ✅ Membandingkan hasil dengan baku mutu PP No. 22 Tahun 2021

    ✅ Menentukan kesesuaian kualitas air berdasarkan peruntukannya

    ✅ Membantu mahasiswa dan praktisi lingkungan
    dalam evaluasi kualitas air
    """)

    st.info("""
    Acuan:
    PP Nomor 22 Tahun 2021
    tentang Penyelenggaraan Perlindungan dan
    Pengelolaan Lingkungan Hidup.
    """)

# =====================================
# EVALUASI COD
# =====================================
elif menu == "🧮 Evaluasi COD":

    st.title("🧮 Evaluasi Kadar COD")

    nama = st.text_input(
        "Nama Sampel"
    )

    jenis_air = st.selectbox(
        "Pilih Jenis Air",
        [
            "Air Baku Air Minum (Kelas 1)",
            "Rekreasi Air (Kelas 2)",
            "Budidaya Ikan Air Tawar (Kelas 2)",
            "Peternakan (Kelas 2)",
            "Perikanan (Kelas 3)",
            "Pertanian / Irigasi (Kelas 4)"
        ]
    )

    cod = st.number_input(
        "Masukkan Hasil COD (mg/L)",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("🔍 Evaluasi"):

        if "Kelas 1" in jenis_air:
            baku_mutu = 10

        elif "Kelas 2" in jenis_air:
            baku_mutu = 25

        elif "Kelas 3" in jenis_air:
            baku_mutu = 50

        else:
            baku_mutu = 100

        st.markdown("---")

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

                Karena {cod:.2f} ≤ {baku_mutu}
                """
            )

        else:

            st.error(
                f"""
                ❌ TIDAK MEMENUHI BAKU MUTU

                COD = {cod:.2f} mg/L

                Baku Mutu = {baku_mutu} mg/L

                Karena {cod:.2f} > {baku_mutu}
                """
            )

# =====================================
# SARANA PENGOLAHAN AIR
# =====================================
elif menu == "🌊 Sarana Pengolahan Air":

    st.title("🌊 Sarana Pengolahan Air")

    st.subheader("1. Koagulasi")
    st.write(
        "Penambahan bahan kimia (koagulan) untuk menggumpalkan partikel koloid."
    )

    st.subheader("2. Flokulasi")
    st.write(
        "Pengadukan lambat untuk membentuk flok yang lebih besar."
    )

    st.subheader("3. Sedimentasi")
    st.write(
        "Pengendapan flok yang telah terbentuk."
    )

    st.subheader("4. Filtrasi")
    st.write(
        "Penyaringan partikel yang masih tersisa."
    )

    st.subheader("5. Desinfeksi")
    st.write(
        "Membunuh mikroorganisme patogen menggunakan klorin, UV, atau ozon."
    )

# =====================================
# TENTANG COD
# =====================================
elif menu == "ℹ️ Tentang COD":

    st.title("ℹ️ Tentang COD")

    st.write("""
    Chemical Oxygen Demand (COD) merupakan jumlah oksigen
    yang dibutuhkan untuk mengoksidasi bahan organik dalam air
    secara kimia.

    Semakin tinggi nilai COD maka semakin tinggi pula tingkat
    pencemaran organik pada badan air.
    """)

    st.subheader("📚 Baku Mutu COD (PP No. 22 Tahun 2021)")

    st.table({
        "Kelas":[
            "Kelas 1",
            "Kelas 2",
            "Kelas 3",
            "Kelas 4"
        ],
        "Peruntukan":[
            "Air Baku Air Minum",
            "Rekreasi Air/Budidaya Ikan",
            "Perikanan/Peternakan",
            "Pertanian/Irigasi"
        ],
        "COD (mg/L)":[
            "≤ 10",
            "≤ 25",
            "≤ 50",
            "≤ 100"
        ]
    })

    st.info(
        "Referensi: PP Nomor 22 Tahun 2021."
    )
/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #003366,
        #006699
    );
}

[data-testid="stSidebar"] *{
    color: white;
}

/* Judul */
h1{
    color:#003366;
    text-align:center;
}

h2,h3{
    color:#004d66;
}

/* Tombol */
.stButton>button{
    background-color:#0088cc;
    color:white;
    border-radius:10px;
    border:none;
    padding:10px 20px;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#006699;
    color:white;
}

/* Input */
.stTextInput input,
.stNumberInput input{
    border-radius:10px;
}

/* Tabel */
[data-testid="stTable"]{
    background:white;
}

</style>
""", unsafe_allow_html=True)
.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}

.block-container{
    background-color: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 20px;
}

h1,h2,h3{
    color:#003366;
}

[data-testid="stSidebar"]{
    background-color:#003366;
}

[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================
menu = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Beranda",
        "🧮 Evaluasi COD",
        "🌊 Sarana Pengolahan Air",
        "ℹ️ Tentang COD"
    ]
)

# ==================================
# BERANDA
# ==================================
if menu == "🏠 Beranda":

    st.title("💧 SISTEM EVALUASI KADAR COD AIR")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk:

    ✅ Mengevaluasi hasil COD laboratorium

    ✅ Membandingkan hasil dengan baku mutu air

    ✅ Menentukan kesesuaian kualitas air

    ✅ Mengacu pada PP Nomor 22 Tahun 2021

    ---
    """)

    st.info("""
    Peraturan Pemerintah Nomor 22 Tahun 2021
    tentang Penyelenggaraan Perlindungan dan
    Pengelolaan Lingkungan Hidup.
    """)

    st.image(
        "https://images.unsplash.com/photo-1500375592092-40eb2168fd21",
        use_container_width=True
    )

# ==================================
# EVALUASI COD
# ==================================
elif menu == "🧮 Evaluasi COD":

    st.title("🧮 Evaluasi Kadar COD")

    nama = st.text_input(
        "Nama Sampel"
    )

    jenis_air = st.selectbox(
        "Pilih Jenis Air",
        [
            "Air Baku Air Minum (Kelas 1)",
            "Rekreasi Air (Kelas 2)",
            "Budidaya Ikan Air Tawar (Kelas 2)",
            "Peternakan (Kelas 2)",
            "Perikanan (Kelas 3)",
            "Pertanian / Irigasi (Kelas 4)"
        ]
    )

    cod = st.number_input(
        "Masukkan Hasil COD (mg/L)",
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

        st.write(f"**Nama Sampel :** {nama}")
        st.write(f"**Jenis Air :** {jenis_air}")
        st.write(f"**COD Hasil :** {cod:.2f} mg/L")
        st.write(f"**Baku Mutu COD :** {baku_mutu} mg/L")

        if cod <= baku_mutu:

            st.success(
                f"✅ COD {cod:.2f} mg/L ≤ {baku_mutu} mg/L\n\n"
                f"Memenuhi baku mutu untuk {jenis_air}"
            )

        else:

            st.error(
                f"❌ COD {cod:.2f} mg/L > {baku_mutu} mg/L\n\n"
                f"Tidak memenuhi baku mutu untuk {jenis_air}"
            )

    st.markdown("---")

    st.subheader("📚 Acuan Baku Mutu COD")

    st.table({
        "Kelas":[
            "Kelas 1",
            "Kelas 2",
            "Kelas 3",
            "Kelas 4"
        ],
        "Peruntukan":[
            "Air Baku Air Minum",
            "Rekreasi Air, Budidaya Ikan",
            "Perikanan, Peternakan",
            "Pertanian, Irigasi"
        ],
        "COD (mg/L)":[
            "≤ 10",
            "≤ 25",
            "≤ 50",
            "≤ 100"
        ]
    })

# ==================================
# SARANA PENGOLAHAN AIR
# ==================================
elif menu == "🌊 Sarana Pengolahan Air":

    st.title("🌊 Sarana Pengolahan Air")

    st.subheader("1. Koagulasi")
    st.write(
        "Penambahan koagulan untuk menggumpalkan partikel koloid."
    )

    st.subheader("2. Flokulasi")
    st.write(
        "Pembentukan flok agar mudah diendapkan."
    )

    st.subheader("3. Sedimentasi")
    st.write(
        "Mengendapkan flok yang telah terbentuk."
    )

    st.subheader("4. Filtrasi")
    st.write(
        "Penyaringan partikel yang masih tersisa."
    )

    st.subheader("5. Desinfeksi")
    st.write(
        "Membunuh mikroorganisme patogen menggunakan klorin, UV, atau ozon."
    )

# ==================================
# TENTANG COD
# ==================================
elif menu == "ℹ️ Tentang COD":

    st.title("ℹ️ Tentang COD")

    st.write("""
    Chemical Oxygen Demand (COD) merupakan jumlah oksigen
    yang dibutuhkan untuk mengoksidasi senyawa organik
    dalam air secara kimia.

    Nilai COD yang tinggi menunjukkan tingginya
    kandungan bahan organik yang dapat mencemari
    badan air.
    """)

    st.info("""
    Semakin rendah nilai COD, semakin baik kualitas air.
    """)

    st.markdown("### Referensi")

    st.write("""
    PP Nomor 22 Tahun 2021 tentang Penyelenggaraan
    Perlindungan dan Pengelolaan Lingkungan Hidup.
    """)
st.markdown("---")

# ====================
# INPUT
# ====================
nama = st.text_input(
    "Nama Sampel"
)

cod = st.number_input(
    "Masukkan Hasil COD (mg/L)",
    min_value=0.0,
    format="%.2f"
)

# ====================
# PROSES
# ====================
if st.button("Evaluasi"):

    st.markdown("## Hasil Evaluasi")

    st.write(f"**Nama Sampel:** {nama}")
    st.write(f"**COD:** {cod:.2f} mg/L")

    st.markdown("---")

    if cod <= 10:

        st.success(
            "KELAS 1"
        )

        st.info("""
        Peruntukan:
        - Air baku air minum
        - Memenuhi baku mutu COD ≤ 10 mg/L
        """)

    elif cod <= 25:

        st.success(
            "KELAS 2"
        )

        st.info("""
        Peruntukan:
        - Sarana rekreasi air
        - Budidaya ikan air tawar
        - Peternakan
        - COD ≤ 25 mg/L
        """)

    elif cod <= 50:

        st.success(
            "KELAS 3"
        )

        st.info("""
        Peruntukan:
        - Perikanan
        - Peternakan
        - Irigasi
        - COD ≤ 50 mg/L
        """)

    elif cod <= 100:

        st.success(
            "KELAS 4"
        )

        st.info("""
        Peruntukan:
        - Pertanian
        - Irigasi
        - COD ≤ 100 mg/L
        """)

    else:

        st.error(
            "Tidak Memenuhi Kelas 1–4"
        )

        st.warning(
            "COD > 100 mg/L"
        )

# ====================
# TABEL ACUAN
# ====================
st.markdown("---")

st.subheader("Tabel Acuan PP No. 22 Tahun 2021")

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
        "Perikanan/Peternakan",
        "Pertanian"
    ],
    "COD (mg/L)":[
        "≤ 10",
        "≤ 25",
        "≤ 50",
        "≤ 100"
    ]
})
