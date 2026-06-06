import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Sistem Evaluasi Kadar COD Air",
    page_icon="💧",
    layout="wide"
)

# =========================
# CSS
# =========================
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

h1,h2,h3{
    color:#003366;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 Pilih Menu",
    [
        "🏠 Beranda",
        "🧮 Perhitungan COD",
        "📊 Klasifikasi Mutu Air",
        "🌊 Sarana Pengolahan Air",
        "ℹ️ Tentang COD"
    ]
)

# =========================
# BERANDA
# =========================
if menu == "🏠 Beranda":

    st.title("💧 SISTEM EVALUASI KADAR COD AIR")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk:

    - Menghitung efisiensi penurunan COD
    - Menentukan kelas mutu air
    - Membandingkan hasil dengan PP No. 22 Tahun 2021
    - Membantu evaluasi kualitas air

    ---
    """)

    st.info(
        "PP Nomor 22 Tahun 2021 digunakan sebagai acuan "
        "baku mutu air nasional."
    )

# =========================
# PERHITUNGAN COD
# =========================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD")

    nama = st.text_input("Nama Sampel")

    inlet = st.number_input(
        "COD Inlet (mg/L)",
        min_value=0.0
    )

    outlet = st.number_input(
        "COD Outlet (mg/L)",
        min_value=0.0
    )

    if st.button("Hitung COD"):

        if inlet == 0:
            st.warning("Masukkan COD Inlet terlebih dahulu")

        else:

            efisiensi = (
                (inlet - outlet)
                / inlet
            ) * 100

            st.success(
                f"Efisiensi Pengolahan = {efisiensi:.2f}%"
            )

            st.write(
                f"COD Outlet = {outlet:.2f} mg/L"
            )

            if outlet <= 10:
                st.success(
                    "Memenuhi Baku Mutu Air Kelas 1"
                )

            else:
                st.error(
                    "Tidak Memenuhi Baku Mutu Air Kelas 1"
                )

# =========================
# KLASIFIKASI MUTU AIR
# =========================
elif menu == "📊 Klasifikasi Mutu Air":

    st.title("📊 Klasifikasi Mutu Air")

    cod = st.number_input(
        "Masukkan Nilai COD (mg/L)",
        min_value=0.0
    )

    if st.button("Evaluasi"):

        if cod <= 10:

            st.success("""
            KELAS 1

            Air Baku Air Minum

            COD ≤ 10 mg/L
            """)

        elif cod <= 25:

            st.success("""
            KELAS 2

            Rekreasi Air,
            Budidaya Ikan Air Tawar

            COD ≤ 25 mg/L
            """)

        elif cod <= 50:

            st.success("""
            KELAS 3

            Peternakan,
            Perikanan,
            Irigasi

            COD ≤ 50 mg/L
            """)

        elif cod <= 100:

            st.success("""
            KELAS 4

            Pertanian

            COD ≤ 100 mg/L
            """)

        else:

            st.error("""
            COD > 100 mg/L

            Tidak memenuhi
            Kelas 1–4
            """)

    st.markdown("---")

    st.subheader("Tabel Acuan PP No.22 Tahun 2021")

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
            "Pertanian"
        ],
        "COD (mg/L)": [
            "≤10",
            "≤25",
            "≤50",
            "≤100"
        ]
    })

# =========================
# SARANA PENGOLAHAN AIR
# =========================
elif menu == "🌊 Sarana Pengolahan Air":

    st.title("🌊 Sarana Pengolahan Air")

    st.subheader("1. Koagulasi")
    st.write(
        "Proses penambahan koagulan "
        "untuk menggumpalkan partikel."
    )

    st.subheader("2. Flokulasi")
    st.write(
        "Proses pembentukan flok "
        "agar mudah diendapkan."
    )

    st.subheader("3. Sedimentasi")
    st.write(
        "Mengendapkan flok yang terbentuk."
    )

    st.subheader("4. Filtrasi")
    st.write(
        "Menyaring partikel tersisa."
    )

    st.subheader("5. Desinfeksi")
    st.write(
        "Membunuh mikroorganisme patogen."
    )

# =========================
# TENTANG COD
# =========================
elif menu == "ℹ️ Tentang COD":

    st.title("ℹ️ Tentang COD")

    st.write("""
    Chemical Oxygen Demand (COD)
    adalah jumlah oksigen yang
    diperlukan untuk mengoksidasi
    senyawa organik dalam air
    secara kimia.

    Semakin tinggi COD,
    semakin tinggi tingkat
    pencemaran bahan organik.
    """)

    st.info(
        "Parameter COD sering digunakan "
        "untuk evaluasi kualitas air "
        "dan air limbah."
    )
