import streamlit as st

st.set_page_config(
    page_title="Perhitungan COD Air Limbah",
    page_icon="💧",
    layout="centered"
)

# CSS Custom
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}

.title {
    text-align:center;
    color:#003366;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#1e3a5f;
    font-size:18px;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.2);
}

.result{
    background:#f8f9fa;
    padding:20px;
    border-radius:15px;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='title'>💧 Perhitungan COD Air Limbah</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Perbandingan dengan Baku Mutu Air Kelas 1 (PP No. 22 Tahun 2021)</div><br>",
    unsafe_allow_html=True
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

inlet = st.number_input(
    "🔹 COD Inlet (mg/L)",
    min_value=0.0,
    format="%.2f"
)

outlet = st.number_input(
    "🔹 COD Outlet (mg/L)",
    min_value=0.0,
    format="%.2f"
)

hitung = st.button("📊 Hitung")

st.markdown("</div>", unsafe_allow_html=True)

if hitung:

    if inlet == 0:
        st.warning("Masukkan nilai COD Inlet terlebih dahulu.")
    else:

        efisiensi = ((inlet - outlet) / inlet) * 100

        st.markdown("<div class='result'>", unsafe_allow_html=True)

        st.subheader("📋 Hasil Perhitungan")

        st.metric(
            "Efisiensi Pengolahan",
            f"{efisiensi:.2f}%"
        )

        st.metric(
            "COD Outlet",
            f"{outlet:.2f} mg/L"
        )

        st.info(
            "📖 Baku Mutu Air Kelas 1 (Air Baku Air Minum) "
            "berdasarkan PP Nomor 22 Tahun 2021: "
            "COD ≤ 10 mg/L"
        )

        if outlet <= 10:
            st.success(
                f"✅ COD Outlet = {outlet:.2f} mg/L ≤ 10 mg/L\n\n"
                "Memenuhi Baku Mutu Air Kelas 1."
            )
        else:
            st.error(
                f"❌ COD Outlet = {outlet:.2f} mg/L > 10 mg/L\n\n"
                "Tidak Memenuhi Baku Mutu Air Kelas 1."
            )

        st.markdown("</div>", unsafe_allow_html=True)
