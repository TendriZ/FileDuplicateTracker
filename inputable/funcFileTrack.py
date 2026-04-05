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