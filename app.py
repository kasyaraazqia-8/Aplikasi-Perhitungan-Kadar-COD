import streamlit as st

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Sistem Evaluasi COD Air",
    page_icon="💧",
    layout="wide"
)

# ==========================================
# CSS
# ==========================================
st.markdown("""
<style>

.stApp{
    background-color:#eaf6ff;
}

.main-title{
    text-align:center;
    color:#003366;
    font-size:40px;
    font-weight:bold;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.15);
}

.banner{
    border-radius:20px;
    overflow:hidden;
}

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #003366,
        #0088cc
    );
}

[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
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

    st.markdown(
        "<div class='main-title'>💧 SISTEM PERHITUNGAN KADAR COD AIR</div>",
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80",
        use_container_width=True
    )

    st.markdown("## Tentang Aplikasi")

    st.info("""
Aplikasi ini digunakan untuk menghitung Chemical Oxygen Demand (COD)
berdasarkan data titrasi laboratorium dan membandingkannya dengan
baku mutu kualitas air sesuai PP Nomor 22 Tahun 2021.
""")

    st.markdown("""
### Fitur

✅ Perhitungan COD otomatis

✅ Evaluasi baku mutu air

✅ Air Minum (Kelas 1)

✅ Rekreasi Air (Kelas 2)

✅ Perikanan (Kelas 3)

✅ Irigasi/Pertanian (Kelas 4)
""")

# ==========================================
# PERHITUNGAN COD
# ==========================================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD")

    col1, col2 = st.columns(2)

    with col1:

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

    with col2:

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

    if st.button("🔍 Hitung COD"):

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
            f"{cod:.2f} mg/L"
        )

        st.metric(
            "Baku Mutu",
            f"{baku} mg/L"
        )

        if cod <= baku:

            st.success(
                f"""
✅ MEMENUHI BAKU MUTU

COD = {cod:.2f} mg/L ≤ {baku} mg/L
"""
            )

        else:

            st.error(
                f"""
❌ TIDAK MEMENUHI BAKU MUTU

COD = {cod:.2f} mg/L > {baku} mg/L
"""
            )

# ==========================================
# REFERENSI
# ==========================================
elif menu == "📚 Referensi":

    st.title("📚 Referensi Baku Mutu COD")

    st.write(
        "PP Nomor 22 Tahun 2021"
    )

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

    st.info("""
Kelas 1 : Air baku air minum

Kelas 2 : Rekreasi air

Kelas 3 : Perikanan

Kelas 4 : Irigasi/Pertanian
""")
