from utils import konversi_suhu  

def main():
    print("=== Konversi Suhu ===")
    nilai = float(input("Masukan Nilai suhu: "))
    dari = input("Dari Satuan (C/F/K): ")
    ke = input("Ke Satuan (C/F/K): ")
    hasil = konversi_suhu(nilai, dari, ke)
    if isinstance(hasil, str):
        print(hasil)
    else:
        print(f"Hasil: {nilai} {dari.upper()} = {hasil} {ke.upper()}")

main()
