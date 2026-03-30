from funcFileTrack import bfs_file_duplicate_tracker

# Graph: struktur direktori sebagai adjacency list
graph = {
    "C:// (Root)": ["Documents", "Downloads", "Desktop"],
    "Documents": ["Tugas", "Foto"],
    "Downloads": ["Modul", "Lagu"],
    "Desktop": ["Aplikasi", "Lain-lain"],
    "Tugas": ["essay.pdf", "Tugas.pdf"],
    "Foto": ["kucing.jpg"],
    "Modul": ["Modul 1.pdf"],
    "Lagu": ["Cinta Satu Malam.mp3"],
    "Aplikasi": ["Notion"],
    "Lain-lain": ["essay.pdf", "foto.png"],
}

# Kumpulkan semua folder (node yang punya children)
folders = [key for key in graph]

# Kumpulkan semua file (leaf node yang tidak ada di graph keys)
all_files = set()
for children in graph.values():
    for child in children:
        if child not in graph:
            all_files.add(child)
all_files = sorted(all_files)

# Pilih state awal (folder)
print("=" * 40)
print("  PILIH DIREKTORI AWAL")
print("=" * 40)
for i, folder in enumerate(folders, 1):
    print(f"  {i}. {folder}")
print()
while True:
    pilihan_awal = input("Masukkan nomor direktori awal: ")
    if pilihan_awal.isdigit() and 1 <= int(pilihan_awal) <= len(folders):
        state_awal = folders[int(pilihan_awal) - 1]
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
    pilihan_akhir = input("Masukkan nomor file yang dicari: ")
    if pilihan_akhir.isdigit() and 1 <= int(pilihan_akhir) <= len(all_files):
        state_akhir = all_files[int(pilihan_akhir) - 1]
        break
    print("  Input tidak valid, coba lagi.")

bfs_file_duplicate_tracker(graph, state_awal, state_akhir)
