import streamlit as st

st.set_page_config(page_title="Perhitungan COD Air Limbah")

st.title("Perhitungan COD Air Limbah")

inlet = st.number_input(
    "COD Inlet (mg/L)",
    min_value=0.0,
    format="%.2f"
)

outlet = st.number_input(
    "COD Outlet (mg/L)",
    min_value=0.0,
    format="%.2f"
)

if st.button("Hitung"):

    if inlet == 0:
        st.warning("Masukkan nilai COD Inlet terlebih dahulu.")
    else:

        efisiensi = ((inlet - outlet) / inlet) * 100

        st.subheader("Hasil Perhitungan")

        st.write(
            f"Efisiensi Pengolahan = {efisiensi:.2f}%"
        )

        st.write(
            f"COD Outlet = {outlet:.2f} mg/L"
        )

        baku_mutu = 10

        st.info(
            "Baku Mutu Air Kelas 1 (Air Baku Air Minum) "
            "berdasarkan PP Nomor 22 Tahun 2021: "
            "COD ≤ 10 mg/L"
        )

        if outlet <= baku_mutu:
            st.success(
                f"COD Outlet = {outlet:.2f} mg/L ≤ 10 mg/L\n\n"
                "Memenuhi Baku Mutu Air Kelas 1."
            )
        else:
            st.error(
                f"COD Outlet = {outlet:.2f} mg/L > 10 mg/L\n\n"
                "Tidak Memenuhi Baku Mutu Air Kelas 1."
            )
