from data import kelas

data = kelas["Kelas 10"]["RPL"]
nama_lengkap = data["Nama Lengkap"]
nama_panggilan = data["Nama Panggilan"]

print("Nama Lengkap :")
print(len(nama_lengkap))
for name in nama_lengkap:
    print(f"- {name}")

print("Nama Panggilan :")
print(len(nama_panggilan))
for name in nama_panggilan:
    print(f"- {name}")