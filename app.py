import streamlit as st

# ==================================
# KONFIGURASI HALAMAN
# ==================================
st.set_page_config(
    page_title="Sistem Evaluasi COD Air",
    page_icon="💧",
    layout="wide"
)

# ==================================
# CSS
# ==================================
st.markdown("""
<style>

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
