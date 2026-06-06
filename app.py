import streamlit as st

st.set_page_config(
    page_title="Evaluasi Kadar COD",
    page_icon="💧",
    layout="centered"
)

# ====================
# CSS
# ====================
st.markdown("""
<style>

.stApp{
background-image:url(
'https://images.unsplash.com/photo-1513828583688-c52646db42da');
background-size:cover;
background-position:center;
background-attachment:fixed;
}

.block-container{
background: rgba(255,255,255,0.92);
padding: 2rem;
border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# ====================
# JUDUL
# ====================
st.title("💧 Evaluasi Kadar COD Air")
st.subheader("Berdasarkan PP Nomor 22 Tahun 2021")

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
