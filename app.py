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
# CSS + BACKGROUND + ANIMASI
# =========================
st.markdown("""
<style>

st.markdown("""
<style>

/* ===== BACKGROUND GAMBAR (FIX) ===== */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1587502536263-9298a8c4c1c1?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* overlay biar teks tetap kebaca */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0.35);
    z-index: 0;
}

/* isi konten di atas overlay */
.main {
    position: relative;
    z-index: 1;
}

/* card efek kaca */
.block-container {
    background: rgba(255,255,255,0.85);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 6px 25px rgba(0,0,0,0.2);
}

h1,h2,h3 {
    color:#003366;
}

/* sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.75);
}

/* bubble animation */
.bubble {
    position: fixed;
    bottom: -100px;
    width: 18px;
    height: 18px;
    background: rgba(255,255,255,0.35);
    border-radius: 50%;
    animation: rise 12s infinite ease-in;
    z-index: 0;
}

.bubble:nth-child(1){left:10%; animation-duration:8s;}
.bubble:nth-child(2){left:20%; animation-duration:10s;}
.bubble:nth-child(3){left:35%; animation-duration:9s;}
.bubble:nth-child(4){left:50%; animation-duration:11s;}
.bubble:nth-child(5){left:70%; animation-duration:7s;}
.bubble:nth-child(6){left:85%; animation-duration:13s;}

@keyframes rise {
    0% {transform: translateY(0); opacity: 0;}
    50% {opacity: 0.6;}
    100% {transform: translateY(-110vh); opacity: 0;}
}

</style>

<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>
<div class="bubble"></div>

""", unsafe_allow_html=True)
""", unsafe_allow_html=True)

# =========================
# SIDEBAR MENU
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
# BAKU MUTU COD (PP 22/2021)
# =========================
baku_mutu = {
    "Kelas 1 (Air baku minum)": 10,
    "Kelas 2 (Rekreasi/Perikanan)": 25,
    "Kelas 3 (Budidaya ikan)": 50,
    "Kelas 4 (Irigasi)": 100
}

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
    - Evaluasi kualitas air berbasis IPAL

    ---

    🌊 **Kelas Air:**
    - Kelas 1 → Air minum (paling ketat)
    - Kelas 2 → Rekreasi & perikanan
    - Kelas 3 → Budidaya ikan
    - Kelas 4 → Irigasi
    """)

# =========================
# PERHITUNGAN COD
# =========================
elif menu == "🧮 Perhitungan COD":

    st.title("🧮 Perhitungan COD IPAL")

    nama = st.text_input("Nama Sampel")

    kelas = st.selectbox(
        "📌 Pilih Kelas Baku Mutu",
        list(baku_mutu.keys())
    )

    inlet = st.number_input("COD Inlet (mg/L)", min_value=0.0)
    outlet = st.number_input("COD Outlet (mg/L)", min_value=0.0)

    if st.button("Hitung COD"):

        batas = baku_mutu[kelas]

        if inlet == 0:
            st.warning("COD inlet tidak boleh 0")
        else:

            penurunan = inlet - outlet
            efisiensi = (penurunan / inlet) * 100

            st.markdown("## 📊 HASIL")

            st.write("Nama Sampel:", nama)
            st.write("COD Inlet:", inlet, "mg/L")
            st.write("COD Outlet:", outlet, "mg/L")

            st.write("Penurunan COD:", penurunan, "mg/L")
            st.write("Efisiensi:", round(efisiensi, 2), "%")

            st.write("Baku Mutu:", batas, "mg/L")

            if outlet <= batas:
                st.success("✅ MEMENUHI BAKU MUTU")
            else:
                st.error("❌ TIDAK MEMENUHI BAKU MUTU")

# =========================
# KLASIFIKASI MUTU AIR
# =========================
elif menu == "📊 Klasifikasi Mutu Air":

    st.title("📊 Klasifikasi COD")

    cod = st.number_input("Masukkan COD (mg/L)", min_value=0.0)

    if st.button("Evaluasi"):

        if cod <= 10:
            st.success("Kelas 1 - Air Baku Minum")
        elif cod <= 25:
            st.success("Kelas 2 - Rekreasi & Perikanan")
        elif cod <= 50:
            st.success("Kelas 3 - Budidaya Ikan")
        elif cod <= 100:
            st.success("Kelas 4 - Irigasi")
        else:
            st.error("❌ Di atas baku mutu")

# =========================
# SARANA PENGOLAHAN AIR
# =========================
elif menu == "🌊 Sarana Pengolahan Air":

    st.title("🌊 Teknologi Pengolahan Air")

    st.markdown("""
    - Koagulasi → penggumpalan partikel
    - Flokulasi → pembentukan flok
    - Sedimentasi → pengendapan
    - Filtrasi → penyaringan
    - Desinfeksi → pembunuhan mikroorganisme
    """)

# =========================
# TENTANG COD
# =========================
elif menu == "ℹ️ Tentang COD":

    st.title("ℹ️ Tentang COD")

    st.write("""
    COD (Chemical Oxygen Demand) adalah
    jumlah oksigen yang dibutuhkan untuk
    mengoksidasi bahan organik dalam air.

    Semakin tinggi COD → semakin tercemar air.
    """)

    st.info("Parameter penting untuk evaluasi IPAL dan kualitas air")
