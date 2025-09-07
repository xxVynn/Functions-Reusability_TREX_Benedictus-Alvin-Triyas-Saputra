def konversi_suhu(nilai, dari_satuan, ke_satuan):
    # Cek satuan
    valid = {"c", "f", "k"}
    dari = dari_satuan.lower()
    ke = ke_satuan.lower()
    if dari not in valid or ke not in valid:
        return "Satuan salah. Harus C, F, atau K."
    if dari == "k" and nilai < 0:
        return "Nilai Kelvin tidak bisa negatif."

    # Ubah ke Celsius
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5 / 9
    else:  # dari == "k"
        c = nilai - 273.15

    # Ubah Celsius ke satuan yang diinginkan
    if ke == "c":
        return c
    elif ke == "f":
        return c * 9 / 5 + 32
    else:  # ke == "k"
        return c + 273.15
