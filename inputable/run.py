#DI file ini berfungsi sebagai runner dengan memanggil fungsi
# yang ada di funcFileTrack.py
from funcFileTrack import bfs_file_duplicate_tracker

# Graph: struktur direktori sebagai adjacency list
graph = {
    "C:// (Root)": ["Desktop", "Downloads", "Documents"],
    "Desktop": ["Aplikasi", "Lain-lain"],
    "Downloads": ["Modul", "Lagu"],
    "Documents": ["Tugas", "Foto"],
    "Aplikasi": ["Notion.apk"],
    "Lain-lain": ["foto.png", "Essay.pdf"],
    "Modul": ["Modul1.pdf"],
    "Lagu": ["telepatia-KaliUchis.mp3"],
    "Foto": ["kucing.jpg"],
    "Tugas": ["Tugas SMT 1", "Tugas SMT 2", "Tugas SMT 3"],
    "Tugas SMT 1": ["Modul Matdis 1.pdf", "Tugas 1 Matdis.docs"],
    "Tugas SMT 2": ["Tugas ADSI 5.pdf"],
    "Tugas SMT 3": ["Resume RKPL 7.pdf", "Essay.pdf", "Praktikum 1.pdf"],
}

# Kumpulkan semua folder (node yang punya children)
folders = [key for key in graph]
#nampilin berapa banyak folder yang ada di graph
print("Ada sebanyak", len(folders), "folder yang tersedia.")
print("Daftar folder:", folders)  # Debug: tampilkan daftar folder yang tersedia

# Kumpulkan semua file (leaf node yang tidak ada di graph keys)
all_files = set()
for children in graph.values():
    print("Children:", children)  # Debug: tampilkan children yang sedang diproses  
    for child in children:
        print("Processing child:", child)  # Debug: tampilkan child yang sedang diproses
        if child not in graph:
            print("Adding file:", child)  # Debug: tampilkan file yang ditambahkan
            all_files.add(child)
            print("Current all_files set:", all_files)  # Debug: tampilkan isi all_files setelah penambahan
all_files = sorted(all_files)

# Pilih state awal (folder)
print("=" * 40)
print("  PILIH DIREKTORI AWAL")
print("=" * 40)
for i, folder in enumerate(folders, 1):
    print(f"  {i}. {folder}")
print()
while True:
    pilihan_keadaan_awal = input("Masukkan nomor direktori awal: ")
    if pilihan_keadaan_awal.isdigit() and 1 <= int(pilihan_keadaan_awal) <= len(folders):
        state_awal = folders[int(pilihan_keadaan_awal) - 1] #argument penting untuk menentukan state awal yang dipilih user
        break
    print("  Input tidak valid, coba lagi.")

# Pilih state akhir (file yang dicari)
print()
print("=" * 40)
print("  PILIH FILE YANG DICARI")
print("=" * 40)
for i, file in enumerate(all_files, 1):
    print(f"  {i}. {file}")
print()
while True:
    pilihan_keadaan_akhir = input("Masukkan nomor file yang dicari: ")
    if pilihan_keadaan_akhir.isdigit() and 1 <= int(pilihan_keadaan_akhir) <= len(all_files):
        state_akhir = all_files[int(pilihan_keadaan_akhir) - 1] #argument penting untuk menentukan state akhir yang dipilih user
        break
    print("  Input tidak valid, coba lagi.")

bfs_file_duplicate_tracker(graph, state_awal, state_akhir)
