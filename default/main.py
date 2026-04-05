from collections import deque


# di file ini berfungsi sebagai callee yang akan dipanggil oleh run.py
from collections import deque

def bfs_file_duplicate_tracker(graph, state_awal, state_akhir):
    """
    BFS untuk mendeteksi file duplikat dalam sistem file manager.

    Parameters:
        graph       : dict - struktur direktori (adjacency list)
        state_awal  : str  - direktori awal pencarian (root)
        state_akhir : str  - nama file yang dicari duplikatnya

    Returns:
        list - daftar jalur (path) file duplikat yang ditemukan
    """
    queue = deque()
    queue.append((state_awal, [state_awal]))

    found_paths = []
    iteration = 0  # dihitung untuk SEMUA node yang dikunjungi (folder + file)

    print(f"\n{'='*60}")
    print(f"  APLIKASI DETEKSI FILE DUPLIKAT")
    print(f"  Direktori awal   : {state_awal}")
    print(f"  File yang dicari : '{state_akhir}'")
    print(f"{'='*60}")
    print(f"\nProses BFS:")
    print("-" * 60)

    while queue:
        currentNode, path = queue.popleft()
        print(f"\nCurrent node: '{currentNode}'")
        print(f"Current path: {path}")
        iteration += 1  
        full_path = " - ".join(path)

        if currentNode not in graph:
            # Node ini adalah FILE (leaf node), cek apakah ini file yang dicari
            if currentNode.lower() == state_akhir.lower():
                found_paths.append(path)
                if len(found_paths) == 1:
                    print(f"  {iteration}. {full_path}")
                    print(f"      -> '{state_akhir}' adalah file yang ingin kita cari duplikatnya, iterasi ke {iteration}")
                else:
                    print(f"  {iteration}. {full_path}")
                    print(f"      -> DITEMUKAN FILE DUPLIKAT!, iterasi ke {iteration}")
            else:
                print(f"  {iteration}. {full_path} <- iterasi ke {iteration}")

            if len(found_paths) >= 2:
                remaining = len(queue)
                if remaining > 0:
                    print(f"\n  >> {remaining} node tidak dikunjungi (BFS selesai)")
                break
        else:
            # Node ini adalah FOLDER, cetak dan masukkan children ke queue
            print(f"  {iteration}. {full_path} (folder) <- iterasi ke {iteration}")
            for child in graph[currentNode]:
                queue.append((child, path + [child]))
    
    # Cetak hasil
    print(f"\n{'='*60}")
    print("HASIL PENCARIAN:")
    print("-" * 60)

    if len(found_paths) >= 2:
        print(f"Rute: Terdapat {len(found_paths)} lintasan dari {state_awal} ke {state_akhir}\n")
        for i, p in enumerate(found_paths, 1):
            print(f"  {i}. {' - '.join(p)}")
        print(f"\nTotal iterasi BFS: {iteration}")
        print(f"\n>> Ditemukan {len(found_paths) - 1} file duplikat!")
    elif len(found_paths) == 1:
        print(f"File '{state_akhir}' hanya ditemukan 1 kali.")
        print("Tidak ada duplikat.")
        print(f"\nTotal iterasi BFS: {iteration}")
    else:
        print(f"File '{state_akhir}' tidak ditemukan.")
        print(f"\nTotal iterasi BFS: {iteration}")

    print(f"{'='*60}")

    return found_paths


# ============================================================
# Contoh penggunaan sesuai studi kasus
# ============================================================

# Graph: struktur direktori sebagai adjacency list
graph = {
    "C:// (Root)": ["Desktop", "Downloads", "Documents"],
    "Desktop": ["Aplikasi", "Lain-lain"],
    "Downloads": ["Modul", "Lagu"],
    "Documents": ["Foto", "Tugas"],
    "Aplikasi": ["Notion.apk"],
    "Lain-lain": ["foto.png", "Essay.pdf"],
    "Modul": ["Modul 1.pdf"],
    "Lagu": ["telepatia-KaliUchis.mp3"],
    "Foto": ["kucing.jpg"],
    "Tugas": ["Tugas SMT 1", "Tugas SMT 2", "Tugas SMT 3"],
    "Tugas SMT 1": ["Modul Matdis 1.pdf", "Tugas 1 Matdis.docs"],
    "Tugas SMT 2": ["Tugas ADSI 5.pdf"],
    "Tugas SMT 3": ["Resume RKPL 7.pdf", "Essay.pdf", "Praktikum 1.pdf"],
}

state_awal = "C:// (Root)"   # Direktori root (node awal)
state_akhir = "Essay.pdf"    # Nama file yang dicari duplikatnya

# Jalankan BFS
hasil = bfs_file_duplicate_tracker(graph, state_awal, state_akhir)
