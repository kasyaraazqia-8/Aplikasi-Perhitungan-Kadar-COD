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
# MENU SIDEBAR
# =====================================
menu = st.sidebar.radio(
    "Pilih Menu",
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

    st.title("💧 Sistem Evaluasi Kadar COD Air")

    st.markdown("""
    ### Selamat Datang

    Aplikasi ini digunakan untuk:

    - Mengevaluasi hasil COD laboratorium
    - Membandingkan hasil COD dengan baku mutu
    - Menentukan kesesuaian kualitas air
    - Mengacu pada PP Nomor 22 Tahun 2021
    """)

    st.info(
        "Aplikasi ini membandingkan nilai COD dengan baku mutu "
        "sesuai kelas dan peruntukan air."
    )

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
            "Budidaya Ikan Air Tawar (Kelas 2)",
            "Peternakan (Kelas 2)",
            "Perikanan (Kelas 3)",
            "Pertanian / Irigasi (Kelas 4)"
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

        st.subheader("Hasil Evaluasi")

        st.write("Nama Sampel :", nama)
        st.write("Jenis Air :", jenis_air)
        st.write("COD Hasil :", f"{cod:.2f} mg/L")
        st.write("Baku Mutu :", f"{baku_mutu} mg/L")

        if cod <= baku_mutu:

            st.success(
                f"Memenuhi baku mutu. "
                f"COD {cod:.2f} mg/L ≤ {baku_mutu} mg/L"
            )

        else:

            st.error(
                f"Tidak memenuhi baku mutu. "
                f"COD {cod:.2f} mg/L > {baku_mutu} mg/L"
            )

# =====================================
# SARANA PENGOLAHAN AIR
# =====================================
elif menu == "🌊 Sarana Pengolahan Air":

    st.title("🌊 Sarana Pengolahan Air")

    st.subheader("1. Koagulasi")
    st.write(
        "Proses penambahan koagulan untuk menggumpalkan partikel."
    )

    st.subheader("2. Flokulasi")
    st.write(
        "Proses pembentukan flok yang lebih besar."
    )

    st.subheader("3. Sedimentasi")
    st.write(
        "Proses pengendapan flok."
    )

    st.subheader("4. Filtrasi")
    st.write(
        "Proses penyaringan partikel tersisa."
    )

    st.subheader("5. Desinfeksi")
    st.write(
        "Proses membunuh mikroorganisme patogen."
    )

# =====================================
# TENTANG COD
# =====================================
elif menu == "ℹ️ Tentang COD":

    st.title("ℹ️ Tentang COD")

    st.write("""
    Chemical Oxygen Demand (COD) adalah jumlah oksigen
    yang dibutuhkan untuk mengoksidasi bahan organik
    dalam air secara kimia.
    """)

    st.subheader("Baku Mutu COD")

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
            "Perikanan/Peternakan",
            "Pertanian/Irigasi"
        ],
        "COD (mg/L)": [
            "≤ 10",
            "≤ 25",
            "≤ 50",
            "≤ 100"
        ]
    })

    st.info(
        "Referensi: PP Nomor 22 Tahun 2021."
    )
