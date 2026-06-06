st.title("📊 Evaluasi Kualitas Air vs Baku Mutu PP 22/2021")

# ---------------- PILIH JENIS AIR ----------------
jenis_air = st.selectbox(
    "🌊 Pilih jenis air",
    ["Inlet IPAL", "Outlet IPAL", "Air Sungai / Badan Air"]
)

# ---------------- PILIH KELAS AIR ----------------
kelas = st.selectbox(
    "📌 Pilih kelas baku mutu",
    ["Kelas I", "Kelas II", "Kelas III", "Kelas IV"]
)

# ---------------- INPUT PARAMETER ----------------
cod = st.number_input("COD (mg/L)")
bod = st.number_input("BOD (mg/L)")
tss = st.number_input("TSS (mg/L)")

# ---------------- NILAI BAKU MUTU (SIMPLIFIKASI UMUM) ----------------
baku_mutu = {
    "Kelas I": {"COD": 10, "BOD": 2, "TSS": 50},
    "Kelas II": {"COD": 25, "BOD": 3, "TSS": 50},
    "Kelas III": {"COD": 50, "BOD": 6, "TSS": 100},
    "Kelas IV": {"COD": 100, "BOD": 12, "TSS": 400}
}

# ---------------- EVALUASI ----------------
if st.button("🔍 Analisis Kualitas Air"):

    batas = baku_mutu[kelas]

    hasil = {}

    hasil["COD"] = cod <= batas["COD"]
    hasil["BOD"] = bod <= batas["BOD"]
    hasil["TSS"] = tss <= batas["TSS"]

    lolos_semua = all(hasil.values())

    st.subheader("📊 HASIL ANALISIS")

    st.write(f"🌊 Jenis Air: **{jenis_air}**")
    st.write(f"📌 Dibandingkan dengan: **{kelas}**")

    st.markdown("---")

    # ---------------- STATUS UTAMA ----------------
    if lolos_semua:
        st.success("✅ AIR MEMENUHI BAKU MUTU")
        deskripsi = "Kualitas air masih berada dalam batas aman sesuai PP No. 22 Tahun 2021."
    else:
        st.error("❌ AIR TIDAK MEMENUHI BAKU MUTU")
        deskripsi = "Kualitas air melebihi salah satu atau lebih parameter baku mutu sehingga perlu pengolahan lanjutan."

    st.info(deskripsi)

    # ---------------- DETAIL PARAMETER ----------------
    st.markdown("### 📌 Detail Parameter")

    st.write("💧 COD:", cod, "mg/L →", "✔" if hasil["COD"] else "❌")
    st.write("🧪 BOD:", bod, "mg/L →", "✔" if hasil["BOD"] else "❌")
    st.write("🌫 TSS:", tss, "mg/L →", "✔" if hasil["TSS"] else "❌")
