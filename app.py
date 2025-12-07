import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import List, Dict, Optional

#import data wisata dari data_wisata.py
from data_wisata import get_all_wisata, get_locations, get_categories, get_connections

# ==================== IMPLEMENTASI LINKED LIST ====================
class Node:
    def __init__(self, kunci: str, nilai: Dict):
        self.kunci = kunci
        self.nilai = nilai
        self.berikutnya = None

class LinkedList:
    def __init__(self):
        self.head = None

    def update(self, kunci: str, nilai: Dict):
        if not self.head:
            self.head = Node(kunci, nilai)
            return

        current = self.head
        while current:
            if current.kunci == kunci:
                current.nilai = nilai
                return
            if not current.berikutnya:
                break
            current = current.berikutnya
        
        current.berikutnya = Node(kunci, nilai)
    
    def ambil(self, kunci: str) -> Optional[Dict]:
        current = self.head
        while current:
            if current.kunci == kunci:
                return current.nilai
            current = current.berikutnya
        return None
    
    def hapus(self, kunci: str) -> bool:
        current = self.head
        prev = None

        if current and current.kunci == kunci:
            self.head = current.berikutnya
            return True

        while current and current.kunci != kunci:
            prev = current
            current = current.berikutnya

        if not current:
            return False

        prev.berikutnya = current.berikutnya
        return True

    def ambil_semua(self) -> List[Dict]:
        items = []
        current = self.head
        while current:
            items.append(current.nilai)
            current = current.berikutnya
        return items

# ==================== HASH TABLE ====================
class TabelHash:
    def __init__(self, ukuran=50):
        self.ukuran = ukuran
        self.tabel = [LinkedList() for _ in range(ukuran)]
    
    def _hash(self, kunci: str) -> int:
        nilai_hash = 0
        for i, char in enumerate(kunci):
            nilai_hash = (nilai_hash + ord(char) * i) % self.ukuran
        return nilai_hash
    
    def tambah(self, kunci: str, nilai: Dict):
        idx = self._hash(kunci)
        self.tabel[idx].update(kunci, nilai)
    
    def ambil(self, kunci: str) -> Optional[Dict]:
        idx = self._hash(kunci)
        return self.tabel[idx].ambil(kunci)
    
    def hapus(self, kunci: str) -> bool:
        idx = self._hash(kunci)
        return self.tabel[idx].hapus(kunci)
    
    def ambil_semua(self) -> List[Dict]:
        items = []
        for lst in self.tabel:
            items.extend(lst.ambil_semua())
        return items

# ==================== STACK ====================
class Stack:
    def __init__(self):
        self._items = []
    
    def kosong(self):
        return not self._items
    
    def push(self, item: str):
        self._items.append(item)
    
    def pop(self) -> Optional[str]:
        if not self.kosong():
            return self._items.pop()
        return None
    
    def lihat(self) -> List[str]:
        return self._items[-5:][::-1]

# ==================== BINARY SEARCH TREE ====================
class NodeBST:
    def __init__(self, kunci: float, data: Dict):
        self.kunci = kunci
        self.data = data
        self.kiri = None
        self.kanan = None

class BST:
    def __init__(self):
        self.root = None
    
    def tambah(self, kunci: float, data: Dict):
        node_baru = NodeBST(kunci, data)
        if self.root is None:
            self.root = node_baru
            return

        current = self.root
        while True:
            if kunci < current.kunci:
                if current.kiri is None:
                    current.kiri = node_baru
                    return
                current = current.kiri
            else: 
                if current.kanan is None:
                    current.kanan = node_baru
                    return
                current = current.kanan
    
    def ambil_tertinggi(self, batas: int = 10) -> List[Dict]:
        hasil = []
        stack = []
        current = self.root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.kanan
            
            if stack:
                current = stack.pop()
                hasil.append(current.data)
                
                if len(hasil) >= batas:
                    break
                
                current = current.kiri
        return hasil

# ==================== GRAPH (konesksi antar lokasi)====================
class Graph:
    def __init__(self):
        self.adjacency = {}
    
    def tambah_vertex(self, vertex: str):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []
    
    def tambah_edge(self, v1: str, v2: str, bobot: int):
        self.adjacency[v1].append({'node': v2, 'bobot': bobot})
        self.adjacency[v2].append({'node': v1, 'bobot': bobot})
    
    def cari_terdekat(self, vertex_awal: str, jarak_max: int) -> List[Dict]:
        terdekat = []
        visited = set()
        queue = [{'vertex': vertex_awal, 'jarak': 0}]
        
        while queue:
            current = queue.pop(0)
            vertex = current['vertex']
            jarak = current['jarak']
            
            if vertex in visited:
                continue
            visited.add(vertex)
            
            if jarak > 0 and jarak <= jarak_max:
                terdekat.append({'lokasi': vertex, 'jarak': jarak})
            
            if vertex in self.adjacency:
                for neighbor in self.adjacency[vertex]:
                    if neighbor['node'] not in visited:
                        queue.append({
                            'vertex': neighbor['node'],
                            'jarak': jarak + neighbor['bobot']
                        })
        
        return sorted(terdekat, key=lambda x: x['jarak'])

# ==================== QUICK SORT ====================
def quick_sort(arr: List[Dict], key: str, naik: bool = True) -> List[Dict]:
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    if naik:
        kiri = [x for x in arr if x[key] < pivot[key]]
        tengah = [x for x in arr if x[key] == pivot[key]]
        kanan = [x for x in arr if x[key] > pivot[key]]
    else:
        kiri = [x for x in arr if x[key] > pivot[key]]
        tengah = [x for x in arr if x[key] == pivot[key]]
        kanan = [x for x in arr if x[key] < pivot[key]]
    
    return quick_sort(kiri, key, naik) + tengah + quick_sort(kanan, key, naik)

# ==================== APLIKASI UTAMA ====================
class AplikasiWisata:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rekomendasi Wisata Provinsi Lampung")
        self.root.geometry("1100x700")
        self.root.configure(bg='#f0f4f8')
        
        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.setup_style()
        
        # Struktur Data
        self.data_wisata = TabelHash()
        self.graph_lokasi = Graph()
        self.list_wisata = []
        self.bst_rating = BST()
        self.stack_history = Stack()
        
        self.id_terpilih = tk.StringVar(value="")
        
        # Kategori Anggaran
        self.kat_anggaran = {
            'murah': {'label': 'Murah', 'min': 0, 'max': 50000, 'warna': '#10b981'},
            'sedang': {'label': 'Sedang', 'min': 50001, 'max': 150000, 'warna': '#f59e0b'},
            'premium': {'label': 'Premium', 'min': 150001, 'max': 1000000, 'warna': '#ef4444'}
        }
        
        # Load data
        self.lokasi = get_locations()
        self.kategori = get_categories()
        
        self.init_data()
        self.buat_ui()
        self.load_data()
    
    def setup_style(self):
        self.style.configure('TNotebook', background='#f0f4f8', borderwidth=0)
        self.style.configure('TNotebook.Tab', 
                             font=('Segoe UI', 10),
                             padding=[15, 8])
        self.style.map('TNotebook.Tab',
                      background=[('selected', '#2563eb')],
                      foreground=[('selected', 'white')])
        
        # Button Styles
        styles = {
            'Success.TButton': ('#10b981', '#059669'),
            'Primary.TButton': ('#3b82f6', '#2563eb'),
            'Warning.TButton': ('#f59e0b', '#d97706'),
            'Danger.TButton': ('#ef4444', '#dc2626'),
            'Secondary.TButton': ('#64748b', '#475569')
        }
        
        for name, (bg, bg_active) in styles.items():
            self.style.configure(name, 
                                 background=bg, 
                                 foreground='white',
                                 font=('Segoe UI', 9),
                                 borderwidth=0,
                                 padding=8)
            self.style.map(name, background=[('active', bg_active)])

    def rebuild_bst(self):
        self.bst_rating = BST()
        for wisata in self.list_wisata:
            self.bst_rating.tambah(wisata['rating'], wisata)

    def init_data(self):
        for lok in self.lokasi:
            self.graph_lokasi.tambah_vertex(lok)
        
        koneksi = get_connections()
        for v1, v2, bobot in koneksi:
            self.graph_lokasi.tambah_edge(v1, v2, bobot)
        
        data = get_all_wisata()
        for wisata in data:
            self.data_wisata.tambah(wisata['id'], wisata)
            self.list_wisata.append(wisata)
        
        self.rebuild_bst()
    
    def buat_ui(self):
        frame_main = tk.Frame(self.root, bg='#f0f4f8')
        frame_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Header
        frame_header = tk.Frame(frame_main, bg='#1e40af', relief=tk.FLAT)
        frame_header.pack(fill=tk.X, pady=(0, 10))
        
        lbl_header = tk.Label(
            frame_header,
            text="SISTEM REKOMENDASI WISATA PROVINSI LAMPUNG",
            font=('Segoe UI', 16, 'bold'),
            bg='#1e40af',
            fg='white'
        )
        lbl_header.pack(pady=12)
        
        # Notebook
        self.notebook = ttk.Notebook(frame_main)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab Filter
        self.tab_filter = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.tab_filter, text='Filter & Rekomendasi')
        self.buat_tab_filter()
        
        # Tab Kelola
        self.tab_kelola = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.tab_kelola, text='Manajemen Data')
        self.buat_tab_kelola()
        
        # Tab Daftar
        self.tab_daftar = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.tab_daftar, text='Daftar Wisata')
        self.buat_tab_daftar()
    
    def buat_tab_filter(self):
        frame_filter = tk.LabelFrame(
            self.tab_filter,
            text=" Filter Pencarian ",
            font=('Segoe UI', 11, 'bold'),
            bg='white',
            padx=20,
            pady=15
        )
        frame_filter.pack(fill=tk.X, padx=15, pady=10)
        
        # Row 1
        row1 = tk.Frame(frame_filter, bg='white')
        row1.pack(fill=tk.X, pady=5)
        
        tk.Label(row1, text="Cari Nama:", font=('Segoe UI', 10), bg='white', 
                 width=14, anchor='w').pack(side=tk.LEFT, padx=5)
        self.entry_cari = ttk.Entry(row1, font=('Segoe UI', 10), width=25)
        self.entry_cari.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row1, text="Lokasi:", font=('Segoe UI', 10), bg='white', 
                 width=10, anchor='w').pack(side=tk.LEFT, padx=5)
        self.var_lokasi = tk.StringVar(value='Semua Lokasi')
        combo_lok = ttk.Combobox(row1, textvariable=self.var_lokasi, 
                                 font=('Segoe UI', 10), width=20, state='readonly')
        combo_lok['values'] = ['Semua Lokasi'] + self.lokasi
        combo_lok.pack(side=tk.LEFT, padx=5)
        
        # Row 2
        row2 = tk.Frame(frame_filter, bg='white')
        row2.pack(fill=tk.X, pady=5)
        
        tk.Label(row2, text="Anggaran:", font=('Segoe UI', 10), bg='white', 
                 width=14, anchor='w').pack(side=tk.LEFT, padx=5)
        self.var_anggaran = tk.StringVar(value='Semua')
        combo_ang = ttk.Combobox(row2, textvariable=self.var_anggaran, 
                                 font=('Segoe UI', 10), width=23, state='readonly')
        combo_ang['values'] = ['Semua', 'Murah (< 50rb)', 'Sedang (50-150rb)', 'Premium (> 150rb)']
        combo_ang.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row2, text="Kategori:", font=('Segoe UI', 10), bg='white', 
                 width=10, anchor='w').pack(side=tk.LEFT, padx=5)
        self.var_kategori = tk.StringVar(value='Semua')
        combo_kat = ttk.Combobox(row2, textvariable=self.var_kategori, 
                                 font=('Segoe UI', 10), width=20, state='readonly')
        combo_kat['values'] = ['Semua'] + list(self.kategori.values())
        combo_kat.pack(side=tk.LEFT, padx=5)
        
        # Tombol
        frame_btn = tk.Frame(frame_filter, bg='white')
        frame_btn.pack(fill=tk.X, pady=10)
        
        ttk.Button(frame_btn, text="Filter", style='Primary.TButton',
                   command=self.filter).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_btn, text="Rekomendasi", 
                   style='Success.TButton',
                   command=self.rekomendasi).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_btn, text="Rating Terbaik ", 
                   style='Warning.TButton',
                   command=self.rating_terbaik).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_btn, text="Reset", style='Secondary.TButton',
                   command=self.reset_filter).pack(side=tk.LEFT, padx=5)

        # Riwayat (Stack)
        frame_history = tk.Frame(self.tab_filter, bg='#f8fafc', relief='solid', bd=1)
        frame_history.pack(fill=tk.X, padx=15, pady=(0, 10))
        
        tk.Label(frame_history, text="Riwayat (Stack):", 
                 font=('Segoe UI', 9, 'bold'), bg='#f8fafc').pack(side=tk.LEFT, padx=10, pady=8)
        self.lbl_history = tk.Label(frame_history, text="Belum ada riwayat", 
                                    font=('Segoe UI', 9), bg='#f8fafc', fg='#64748b')
        self.lbl_history.pack(side=tk.LEFT, padx=10, pady=8)

        # Hasil
        frame_hasil = tk.LabelFrame(
            self.tab_filter,
            text=" Hasil Pencarian ",
            font=('Segoe UI', 11, 'bold'),
            bg='white',
            padx=15,
            pady=10
        )
        frame_hasil.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        
        self.text_hasil = scrolledtext.ScrolledText(
            frame_hasil,
            font=('Consolas', 9),
            wrap=tk.WORD,
            bg='#fafafa',
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.text_hasil.pack(fill=tk.BOTH, expand=True)
    
    def buat_tab_kelola(self):
        frame_form = tk.LabelFrame(
            self.tab_kelola,
            text=" Form Input/Update Wisata ",
            font=('Segoe UI', 11, 'bold'),
            bg='white',
            padx=20,
            pady=15
        )
        frame_form.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # ID (hidden)
        tk.Label(frame_form, text="ID (Mode Update):", 
                 font=('Segoe UI', 8), bg='white', 
                 fg='#94a3b8').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        tk.Label(frame_form, textvariable=self.id_terpilih, 
                 font=('Segoe UI', 8), bg='white', 
                 fg='#94a3b8').grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        # Isi
        fields = [
            ("Nama Wisata", "nama", 1),
            ("Lokasi", "lokasi", 2),
            ("Anggaran (Rp)", "anggaran", 3),
            ("Kategori Anggaran", "kat_anggaran", 4),
            ("Kategori", "kategori", 5),
            ("Rating (1-5)", "rating", 6),
            ("Deskripsi", "deskripsi", 7)
        ]
        
        self.form = {}
        for label, field, row in fields:
            tk.Label(
                frame_form,
                text=label + ":",
                font=('Segoe UI', 10),
                bg='white',
                width=18,
                anchor='w'
            ).grid(row=row, column=0, sticky='w', padx=5, pady=5)
            
            if field in ['lokasi', 'kat_anggaran', 'kategori']:
                var = tk.StringVar()
                widget = ttk.Combobox(frame_form, textvariable=var, 
                                     font=('Segoe UI', 10), width=38, state='readonly')
                
                if field == 'lokasi':
                    widget['values'] = self.lokasi
                elif field == 'kat_anggaran':
                    widget['values'] = ['murah', 'sedang', 'premium']
                elif field == 'kategori':
                    widget['values'] = list(self.kategori.keys())
                
                widget.grid(row=row, column=1, sticky='ew', padx=5, pady=5)
                self.form[field] = var
            else:
                var = tk.StringVar()
                widget = ttk.Entry(frame_form, textvariable=var, font=('Segoe UI', 10))
                widget.grid(row=row, column=1, sticky='ew', padx=5, pady=5)
                self.form[field] = var

        frame_form.grid_columnconfigure(1, weight=1)
        
        # Tombol
        frame_btn = tk.Frame(frame_form, bg='white')
        frame_btn.grid(row=len(fields) + 1, column=0, columnspan=2, pady=15)
        
        ttk.Button(frame_btn, text="Tambah", style='Success.TButton',
                   command=self.tambah).pack(side=tk.LEFT, padx=5)

        ttk.Button(frame_btn, text="Update", style='Primary.TButton',
                   command=self.update).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_btn, text="Reset", style='Secondary.TButton',
                   command=self.reset_form).pack(side=tk.LEFT, padx=5)
    
    def buat_tab_daftar(self):
        frame_kontrol = tk.Frame(self.tab_daftar, bg='white')
        frame_kontrol.pack(fill=tk.X, padx=15, pady=10)
        
        tk.Label(frame_kontrol, text="Total:", font=('Segoe UI', 10, 'bold'),
                 bg='white').pack(side=tk.LEFT, padx=10)
        
        self.lbl_jumlah = tk.Label(frame_kontrol, text="0", 
                                    font=('Segoe UI', 10, 'bold'),
                                    bg='white', fg='#3b82f6')
        self.lbl_jumlah.pack(side=tk.LEFT, padx=5)

        ttk.Button(frame_kontrol, text="Update", 
                   style='Warning.TButton',
                   command=self.muat_update).pack(side=tk.RIGHT, padx=10)
        
        ttk.Button(frame_kontrol, text="Refresh", style='Primary.TButton',
                   command=self.load_data).pack(side=tk.RIGHT, padx=5)
        
        # Treeview
        frame_tree = tk.Frame(self.tab_daftar, bg='white')
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        
        scroll_v = ttk.Scrollbar(frame_tree, orient="vertical")
        scroll_h = ttk.Scrollbar(frame_tree, orient="horizontal")
        
        self.tree = ttk.Treeview(
            frame_tree,
            columns=('ID', 'Nama', 'Lokasi', 'Anggaran', 'Kategori', 'Rating'),
            show='headings',
            yscrollcommand=scroll_v.set,
            xscrollcommand=scroll_h.set
        )
        
        scroll_v.config(command=self.tree.yview)
        scroll_h.config(command=self.tree.xview)
        
        # Kolom
        cols = [
            ('ID', 80, 'center'),
            ('Nama', 250, 'w'),
            ('Lokasi', 130, 'center'),
            ('Anggaran', 130, 'center'),
            ('Kategori', 120, 'center'),
            ('Rating', 80, 'center')
        ]
        
        for col, width, anchor in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=anchor)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        scroll_v.grid(row=0, column=1, sticky='ns')
        scroll_h.grid(row=1, column=0, sticky='ew')
        
        frame_tree.grid_rowconfigure(0, weight=1)
        frame_tree.grid_columnconfigure(0, weight=1)
        
        # Tombol Hapus
        frame_hapus = tk.Frame(self.tab_daftar, bg='white')
        frame_hapus.pack(fill=tk.X, padx=15, pady=(0, 10))
        
        ttk.Button(frame_hapus, text="Hapus", 
                   style='Danger.TButton',
                   command=self.hapus).pack(side=tk.LEFT, padx=5)
    
    def muat_update(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih satu wisata!")
            return
        
        id_wisata = self.tree.item(selected[0])['values'][0]
        wisata = self.data_wisata.ambil(id_wisata)
        
        if wisata:
            self.id_terpilih.set(id_wisata)
            self.form['nama'].set(wisata['nama'])
            self.form['lokasi'].set(wisata['lokasi'])
            self.form['anggaran'].set(str(wisata['anggaran']))
            self.form['kat_anggaran'].set(wisata['kategori_anggaran'])
            self.form['kategori'].set(wisata['kategori'])
            self.form['rating'].set(str(wisata['rating']))
            self.form['deskripsi'].set(wisata['deskripsi'])
            
            self.notebook.select(self.tab_kelola)
            messagebox.showinfo("Sukses", f"Data '{wisata['nama']}' dimuat!")

    def update(self):
        id_wisata = self.id_terpilih.get().strip()
        if not id_wisata:
            messagebox.showwarning("Peringatan", "Tidak ada data untuk update!")
            return

        try:
            nama = self.form['nama'].get().strip()
            lokasi = self.form['lokasi'].get().strip()
            anggaran = self.form['anggaran'].get().strip()
            kat_ang = self.form['kat_anggaran'].get().strip()
            kategori = self.form['kategori'].get().strip()
            rating = self.form['rating'].get().strip()
            desk = self.form['deskripsi'].get().strip()
            
            if not all([nama, lokasi, anggaran, kat_ang, kategori, rating, desk]):
                messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                return
            
            anggaran = int(anggaran)
            rating = float(rating)
            if rating < 1 or rating > 5:
                messagebox.showwarning("Peringatan", "Rating harus 1-5!")
                return
            
            wisata_baru = {
                'id': id_wisata,
                'nama': nama,
                'lokasi': lokasi,
                'anggaran': anggaran,
                'kategori_anggaran': kat_ang,
                'kategori': kategori,
                'rating': rating,
                'deskripsi': desk
            }
            
            self.data_wisata.tambah(id_wisata, wisata_baru)
            
            for i, w in enumerate(self.list_wisata):
                if w['id'] == id_wisata:
                    self.list_wisata[i] = wisata_baru
                    break
            
            self.rebuild_bst()
            messagebox.showinfo("Sukses", f"Wisata '{nama}' berhasil diupdate!")
            self.reset_form()
            self.load_data()
            
        except ValueError:
            messagebox.showerror("Error", "Format anggaran/rating tidak valid!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def tambah(self):
        if self.id_terpilih.get().strip():
            messagebox.showwarning("Peringatan", "Reset form untuk tambah data baru!")
            return

        try:
            nama = self.form['nama'].get().strip()
            lokasi = self.form['lokasi'].get().strip()
            anggaran = self.form['anggaran'].get().strip()
            kat_ang = self.form['kat_anggaran'].get().strip()
            kategori = self.form['kategori'].get().strip()
            rating = self.form['rating'].get().strip()
            desk = self.form['deskripsi'].get().strip()
            
            if not all([nama, lokasi, anggaran, kat_ang, kategori, rating, desk]):
                messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                return
            
            anggaran = int(anggaran)
            rating = float(rating)
            
            if rating < 1 or rating > 5:
                messagebox.showwarning("Peringatan", "Rating harus 1-5!")
                return
            
            id_baru = f"W{str(len(self.list_wisata) + 1).zfill(3)}"
            
            wisata = {
                'id': id_baru,
                'nama': nama,
                'lokasi': lokasi,
                'anggaran': anggaran,
                'kategori_anggaran': kat_ang,
                'kategori': kategori,
                'rating': rating,
                'deskripsi': desk
            }
            
            self.data_wisata.tambah(id_baru, wisata)
            self.list_wisata.append(wisata)
            self.bst_rating.tambah(wisata['rating'], wisata)
            
            messagebox.showinfo("Sukses", f"Wisata '{nama}' berhasil ditambahkan!")
            self.reset_form()
            self.load_data()
            
        except ValueError:
            messagebox.showerror("Error", "Format anggaran/rating tidak valid!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    
    def hapus(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih wisata yang akan dihapus!")
            return
        
        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus?"):
            for item in selected:
                values = self.tree.item(item)['values']
                id_wisata = values[0]
                
                self.data_wisata.hapus(id_wisata)
                self.list_wisata = [w for w in self.list_wisata if w['id'] != id_wisata]
            
            self.rebuild_bst()
            messagebox.showinfo("Sukses", "Wisata berhasil dihapus!")
            self.load_data()
    
    def filter(self):
        hasil = self.list_wisata.copy()
        
        # Filter nama
        keyword = self.entry_cari.get().strip().lower()
        if keyword:
            hasil = [w for w in hasil if keyword in w['nama'].lower()]
        
        # Filter lokasi
        lokasi = self.var_lokasi.get()
        if lokasi != 'Semua Lokasi':
            hasil = [w for w in hasil if w['lokasi'] == lokasi]
        
        # Filter anggaran
        anggaran = self.var_anggaran.get()
        if anggaran != 'Semua':
            map_ang = {
                'Murah (< 50rb)': 'murah',
                'Sedang (50-150rb)': 'sedang',
                'Premium (> 150rb)': 'premium'
            }
            kat_ang = map_ang[anggaran]
            hasil = [w for w in hasil if w['kategori_anggaran'] == kat_ang]
        
        # Filter kategori
        kategori = self.var_kategori.get()
        if kategori != 'Semua':
            key_kat = None
            for key, val in self.kategori.items():
                if val == kategori:
                    key_kat = key
                    break
            if key_kat:
                hasil = [w for w in hasil if w['kategori'] == key_kat]
        
        self.tampilkan(hasil, sumber=" Pariwisata Lampung")
        self.catat_history(hasil)
    
    def rekomendasi(self):
        hasil = self.list_wisata.copy()
        
        # Filter Graph
        lokasi = self.var_lokasi.get()
        if lokasi != 'Semua Lokasi':
            terdekat = self.graph_lokasi.cari_terdekat(lokasi, 50)
            lok_terdekat = [lokasi] + [n['lokasi'] for n in terdekat]
            hasil = [w for w in hasil if w['lokasi'] in lok_terdekat]
        
        # Filter anggaran
        anggaran = self.var_anggaran.get()
        if anggaran != 'Semua':
            map_ang = {
                'Murah (< 50rb)': 'murah',
                'Sedang (50-150rb)': 'sedang',
                'Premium (> 150rb)': 'premium'
            }
            kat_ang = map_ang[anggaran]
            hasil = [w for w in hasil if w['kategori_anggaran'] == kat_ang]
        
        # Filter kategori
        kategori = self.var_kategori.get()
        if kategori != 'Semua':
            key_kat = None
            for key, val in self.kategori.items():
                if val == kategori:
                    key_kat = key
                    break
            if key_kat:
                hasil = [w for w in hasil if w['kategori'] == key_kat]
        
        # QuickSort
        hasil = quick_sort(hasil, 'rating', naik=False)
        
        self.tampilkan(hasil[:10], rekomendasi=True, sumber="QuickSort + Graph BFS")
        self.catat_history(hasil)
    
    def rating_terbaik(self):
        hasil = self.bst_rating.ambil_tertinggi(batas=10)
        self.tampilkan(hasil, rekomendasi=True, sumber="BST Traversal")
        self.catat_history(hasil)
        
    def catat_history(self, hasil):
        if hasil:
            nama_top = hasil[0]['nama']
            self.stack_history.push(nama_top)
        
        items = self.stack_history.lihat()
        if items:
            text = " → ".join(items[:3])
            self.lbl_history.config(text=text, fg='#3b82f6')
        else:
            self.lbl_history.config(text="Belum ada riwayat", fg='#94a3b8')

    def tampilkan(self, hasil, rekomendasi=False, sumber="Filter"):
        self.text_hasil.delete('1.0', tk.END)
        
        if not hasil:
            self.text_hasil.insert(tk.END, "\n\n")
            self.text_hasil.insert(tk.END, "      TIDAK ADA HASIL DITEMUKAN      \n", 'error')
            self.text_hasil.insert(tk.END, "\n")
            self.text_hasil.insert(tk.END, "Coba ubah kriteria filter Anda!\n", 'tips')
            return
        
        # Header
        judul = "REKOMENDASI WISATA TERBAIK" if rekomendasi else "HASIL PENCARIAN"
        
        self.text_hasil.insert(tk.END, "\n")
        self.text_hasil.insert(tk.END, "=" * 100 + "\n", 'border')
        self.text_hasil.insert(tk.END, f"{judul:^100}\n", 'judul')
        self.text_hasil.insert(tk.END, f"Sumber: {sumber:^92}\n", 'subjudul')
        self.text_hasil.insert(tk.END, f"Total: {len(hasil)} Destinasi{' ' * 80}\n", 'subjudul')
        self.text_hasil.insert(tk.END, "=" * 100 + "\n\n", 'border')
        
        for i, w in enumerate(hasil, 1):
            # Header wisata
            self.text_hasil.insert(tk.END, f"[{i:02d}] ", 'nomor')
            self.text_hasil.insert(tk.END, f"{w['nama']}\n", 'header')
            self.text_hasil.insert(tk.END, "-" * 100 + "\n", 'line')
            
            kat_label = self.kategori.get(w['kategori'], w['kategori'])
            ang_info = self.kat_anggaran[w['kategori_anggaran']]
            
            # 1. Kategori
            self.text_hasil.insert(tk.END, f"Kategori  : {kat_label}\n", 'info')
            
            # 2. Anggaran (Perbaikan Badge Warna)
            ang_key = w['kategori_anggaran']
            if ang_key == 'murah': tag_style = 'badge_murah'
            elif ang_key == 'sedang': tag_style = 'badge_sedang'
            else: tag_style = 'badge_premium'
            
            self.text_hasil.insert(tk.END, f"Anggaran  : Rp {w['anggaran']:>10,} ", 'info')
            
            self.text_hasil.insert(tk.END, f"[{ang_info['label']}]", tag_style)
            self.text_hasil.insert(tk.END, "\n", 'info') # Newline untuk stacking
            
            # 3. Lokasi
            self.text_hasil.insert(tk.END, f"Lokasi    : {w['lokasi']}\n", 'info')
            
            # 4. Rating (Perbaikan Warna Bintang Kosong)
            stars = int(w['rating'])
            half = 1 if (w['rating'] - stars) >= 0.5 else 0
            bintang_kosong_count = 5 - stars - half
            
            bintang_penuh_visual = "⭐" * stars
            if half:
                bintang_penuh_visual += "✨"
            
            bintang_kosong_visual = "☆" * bintang_kosong_count
            
            self.text_hasil.insert(tk.END, f"Rating    : ", 'info') 
            self.text_hasil.insert(tk.END, bintang_penuh_visual, 'rating') 
            self.text_hasil.insert(tk.END, bintang_kosong_visual, 'rating_kosong') 
            self.text_hasil.insert(tk.END, f" {w['rating']}/5.0\n", 'rating') 
            
            # 5. Deskripsi
            self.text_hasil.insert(tk.END, f"Deskripsi : {w['deskripsi']}\n", 'desc')
            self.text_hasil.insert(tk.END, "\n")
        
        # Footer
        self.text_hasil.insert(tk.END, "=" * 100 + "\n", 'footer')
        self.text_hasil.insert(tk.END, "Selamat berwisata di Lampung!\n", 'footer')
        self.text_hasil.insert(tk.END, "=" * 100 + "\n", 'footer')
        
        # Style tags (Ditambahkan tag badge warna)
        self.text_hasil.tag_config('border', foreground='#0ea5e9', font=('Consolas', 9, 'bold'))
        self.text_hasil.tag_config('judul', foreground='#059669', font=('Segoe UI', 12, 'bold'))
        self.text_hasil.tag_config('subjudul', foreground='#0c4a6e', font=('Segoe UI', 9))
        self.text_hasil.tag_config('nomor', foreground='#dc2626', font=('Segoe UI', 10, 'bold'))
        self.text_hasil.tag_config('header', foreground='#1e40af', font=('Segoe UI', 11, 'bold'))
        self.text_hasil.tag_config('line', foreground='#cbd5e1')
        self.text_hasil.tag_config('info', foreground='#374151', font=('Segoe UI', 9))
        
        # Penambahan tag warna badge
        self.text_hasil.tag_config('badge_murah', foreground='#ffffff', background='#10b981', font=('Segoe UI', 8, 'bold'))
        self.text_hasil.tag_config('badge_sedang', foreground='#ffffff', background='#f59e0b', font=('Segoe UI', 8, 'bold'))
        self.text_hasil.tag_config('badge_premium', foreground='#ffffff', background='#ef4444', font=('Segoe UI', 8, 'bold'))
        
        self.text_hasil.tag_config('rating', foreground='#f59e0b', font=('Segoe UI', 9, 'bold'))
        self.text_hasil.tag_config('rating_kosong', foreground='#cbd5e1', font=('Segoe UI', 9)) 
        
        self.text_hasil.tag_config('desc', foreground='#4b5563', font=('Segoe UI', 9))
        self.text_hasil.tag_config('footer', foreground='#7c3aed', font=('Segoe UI', 10))
        self.text_hasil.tag_config('error', foreground='#dc2626', font=('Segoe UI', 12, 'bold'))
        self.text_hasil.tag_config('tips', foreground='#059669', font=('Segoe UI', 9))
    
    def reset_filter(self):
        self.entry_cari.delete(0, tk.END)
        self.var_lokasi.set('Semua Lokasi')
        self.var_anggaran.set('Semua')
        self.var_kategori.set('Semua')
        self.text_hasil.delete('1.0', tk.END)
        self.stack_history = Stack()
        self.catat_history([])
        messagebox.showinfo("Info", "Filter direset!")
    
    def reset_form(self):
        for var in self.form.values():
            var.set('')
        self.id_terpilih.set("")
    
    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for w in self.list_wisata:
            ang_label = self.kat_anggaran[w['kategori_anggaran']]['label']
            kat_label = self.kategori[w['kategori']]
            
            self.tree.insert('', tk.END, values=(
                w['id'],
                w['nama'],
                w['lokasi'],
                f"Rp {w['anggaran']:,} ({ang_label})",
                kat_label,
                f"{w['rating']}/5"
            ))
        
        self.lbl_jumlah.config(text=str(len(self.list_wisata)))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiWisata(root)
    root.mainloop()

{
        'id': 'W085',
        'nama': 'Menara Siger',
        'lokasi': 'Lampung Selatan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Ikon titik nol Sumatera dengan arsitektur mahkota siger emas yang megah',
        'rating': 4.3
    },
    {
        'id': 'W086',
        'nama': 'Pulau Pisang',
        'lokasi': 'Pesisir Barat',
        'anggaran': 150000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pulau eksotis dengan pasir putih halus dan habitat lumba-lumba',
        'rating': 4.8
    },
    {
        'id': 'W087',
        'nama': 'Temiangan Hill',
        'lokasi': 'Lampung Barat',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Negeri di atas awan dengan pemandangan sunrise yang spektakuler',
        'rating': 4.7
    },
    {
        'id': 'W088',
        'nama': 'Masjid Baitus Shobur (99 Cahaya)',
        'lokasi': 'Tulang Bawang Barat',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Masjid unik tanpa kubah dengan arsitektur vertikal yang filosofis',
        'rating': 4.8
    },
    {
        'id': 'W089',
        'nama': 'Pulau Kelagian Besar',
        'lokasi': 'Pesawaran',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau tak berpenghuni dengan pasir putih lembut dan air gradasi biru',
        'rating': 4.6
    },
    {
        'id': 'W090',
        'nama': 'Pantai Marina',
        'lokasi': 'Lampung Selatan',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai hits dengan jajaran karang estetik dan deburan ombak kuat',
        'rating': 4.4
    },
    {
        'id': 'W091',
        'nama': 'Taman Merdeka Metro',
        'lokasi': 'Metro',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Alun-alun kota Metro yang asri, pusat kegiatan warga dan kuliner malam',
        'rating': 4.2
    },
    {
        'id': 'W092',
        'nama': 'Pemandian Way Bekhak',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Mata air alami yang sangat jernih dan segar di kaki Gunung Tanggamus',
        'rating': 4.4
    },
    {
        'id': 'W093',
        'nama': 'Pantai Ketapang',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Dermaga utama penyeberangan ke pulau-pulau sekaligus spot mancing',
        'rating': 4.1
    },
    {
        'id': 'W094',
        'nama': 'Ekowisata Mangrove Petengoran',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Hutan bakau dengan jalur kayu panjang dan spot kuliner seafood',
        'rating': 4.3
    },
    {
        'id': 'W095',
        'nama': 'Pemandian Air Panas Way Belerang',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Kolam air panas belerang alami dari Gunung Rajabasa untuk kesehatan',
        'rating': 4.2
    },
    {
        'id': 'W096',
        'nama': 'Kampung Tua Gedung Batin',
        'lokasi': 'Way Kanan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Desa wisata budaya dengan rumah panggung tua berusia ratusan tahun',
        'rating': 4.5
    },
    {
        'id': 'W097',
        'nama': 'Pantai Tembakak',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan pasir hitam eksotis dan bebatuan karang unik',
        'rating': 4.3
    },
    {
        'id': 'W098',
        'nama': 'Arung Jeram Way Besai',
        'lokasi': 'Lampung Barat',
        'anggaran': 150000,
        'kategori_anggaran': 'sedang',
        'kategori': 'gunung',
        'deskripsi': 'Wisata adrenalin rafting menyusuri sungai berbatu grade 3',
        'rating': 4.7
    },
    {
        'id': 'W099',
        'nama': 'Pantai M-Beach (Embe)',
        'lokasi': 'Lampung Selatan',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai pasir putih bersih dengan fasilitas glamping dan spot foto',
        'rating': 4.5
    },
    {
        'id': 'W100',
        'nama': 'Samber Park',
        'lokasi': 'Metro',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Lapangan multifungsi pusat konser dan bazar kuliner di Kota Metro',
        'rating': 4.1
    },
    {
        'id': 'W101',
        'nama': 'Lengkung Langit 2',
        'lokasi': 'Bandar Lampung',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman wisata alam dengan spot foto kaca dan nuansa asri Kemiling',
        'rating': 4.3
    },
    {
        'id': 'W102',
        'nama': 'Pulau Pasaran',
        'lokasi': 'Bandar Lampung',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'kuliner',
        'deskripsi': 'Sentra produksi ikan asin dan teri terbesar di Lampung',
        'rating': 4.4
    },
    {
        'id': 'W103',
        'nama': 'Bukit Pematang Sunrise',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Spot camping dengan view 360 derajat laut dan perbukitan',
        'rating': 4.5
    },
    {
        'id': 'W104',
        'nama': 'Air Terjun Ciupang',
        'lokasi': 'Pesawaran',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun dengan dinding batu hitam yang artistik dan mudah dijangkau',
        'rating': 4.3
    },
    {
        'id': 'W105',
        'nama': 'Pulau Sebesi',
        'lokasi': 'Lampung Selatan',
        'anggaran': 100000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pulau berpenghuni terdekat dengan Gunung Anak Krakatau',
        'rating': 4.6
    },
    {
        'id': 'W106',
        'nama': 'Danau Asam',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Danau vulkanik di kawasan Suoh dengan air yang memiliki pH rendah',
        'rating': 4.4
    },
    {
        'id': 'W107',
        'nama': 'Pantai Batu Tihang',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan ikon batu karang menjulang tinggi di bibir pantai',
        'rating': 4.4
    },
    {
        'id': 'W108',
        'nama': 'Pasar Yosomulyo Pelangi (Payungi)',
        'lokasi': 'Metro',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'kuliner',
        'deskripsi': 'Pasar kreatif warga dengan jajanan tradisional dan nuansa ceria',
        'rating': 4.6
    },
    {
        'id': 'W109',
        'nama': 'Las Sengok',
        'lokasi': 'Tulang Bawang Barat',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Hutan wisata adat yang sejuk dengan pepohonan rimbun dan asri',
        'rating': 4.2
    },
    {
        'id': 'W110',
        'nama': 'Taman Sabin',
        'lokasi': 'Pringsewu',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata sawah instagramable dengan jembatan kayu dan lampu hias',
        'rating': 4.3
    },
