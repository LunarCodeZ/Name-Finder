
from data import kelas
import time
siswa_sudah = []
siswa_belum = []

def display_interface():
    print("_ " * 12)
    print("      Name Finder      ")
    print("          Tool          ")
    print("_ " * 12)
    print("\n")
    text = input(str("Masukkan teks: "))
    category_selection_1(text)


def start():
    display_interface()
    

def category_selection_1(text_input):
    category = ['AK', 'BD', 'DKV', 'LPB', 'MP', 'RPL']
    print("\n")
    print("- - Daftar Kelas - -")
    for categories in category:
        print(f"- {categories}")
    print("")
    select_category_1 = input(str("Pilih Kelas: "))
    print("\n")

    match select_category_1:
        case "AK" | "DKV":
            category_selection_2() # Hadir pada versi berikutnya
        case _:
            data = kelas["Kelas 10"][select_category_1]
            result(-1,text_input,data)

# Akan dibuat di versi berikutnya
def category_selection_2():
    pass

def result(counter_amount,text_input,text_data):
    nama_lengkap = text_data["Nama Lengkap"]
    nama_panggilan = text_data["Nama Panggilan"]

    if counter_amount < len(nama_panggilan) - 1:
        counter_amount += 1
        if nama_lengkap[counter_amount] in text_input or nama_panggilan[counter_amount] in text_input:
            siswa_sudah.append(nama_panggilan[counter_amount])
        else:
            siswa_belum.append(nama_panggilan[counter_amount])
        result(counter_amount, text_input, text_data)

    elif counter_amount < len(nama_panggilan):
        print("_ _ _ _ Hasil _ _ _ _")
        print("\n Siswa sudah:")
        for students in siswa_sudah:
            print(f"- {students}")
        print("\n Siswa belum:")
        for students in siswa_belum:
            print(f"- {students}")
        print("")
        print("_ " * 11)
        print("\n\n")
    
   
    
start()

text_sample = """ Daftar petugas upacara siswa kelas X -Rayden -Ben
"""