# data_wisata.py
# File ini berisi semua data wisata di Provinsi Lampung

# Daftar lokasi di Provinsi Lampung
LOCATIONS = [
    'Bandar Lampung', 'Metro', 'Lampung Selatan', 'Lampung Tengah',
    'Lampung Utara', 'Lampung Barat', 'Lampung Timur', 'Tanggamus',
    'Pesawaran', 'Pringsewu', 'Tulang Bawang', 'Way Kanan',
    'Mesuji', 'Tulang Bawang Barat', 'Pesisir Barat'
]


CATEGORIES = {
    'pantai': 'Pantai',
    'gunung': 'Gunung',
    'air_terjun': 'Air Terjun',
    'edukasi': 'Edukasi',
    'kuliner': 'Kuliner',
    'sejarah': 'Sejarah',
    'taman': 'Taman'
}

# Koneksi antar lokasi (lokasi1, lokasi2, jarak_km)
LOCATION_CONNECTIONS = [
    ('Bandar Lampung', 'Lampung Selatan', 15),
    ('Bandar Lampung', 'Pesawaran', 25),
    ('Bandar Lampung', 'Pringsewu', 35),
    ('Bandar Lampung', 'Tanggamus', 50),
    ('Metro', 'Lampung Tengah', 20),
    ('Lampung Tengah', 'Lampung Utara', 40),
    ('Lampung Tengah', 'Lampung Timur', 45),
    ('Lampung Barat', 'Tanggamus', 30),
    ('Lampung Barat', 'Pesisir Barat', 45),
    ('Lampung Timur', 'Way Kanan', 35),
    ('Lampung Timur', 'Tulang Bawang', 40),
    ('Way Kanan', 'Tulang Bawang', 30),
    ('Tulang Bawang', 'Mesuji', 25),
    ('Tulang Bawang', 'Tulang Bawang Barat', 20),
]

# Data wisata
# Format: id, nama, lokasi, anggaran, kategori_anggaran, kategori, deskripsi, rating
WISATA_DATA = [
    {
        'id': 'W001',
        'nama': 'Pantai Mutun',
        'lokasi': 'Lampung Selatan',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai indah dengan pasir putih dan air jernih, cocok untuk keluarga',
        'rating': 4.5
    },
    {
        'id': 'W002',
        'nama': 'Way Kambas National Park',
        'lokasi': 'Lampung Timur',
        'anggaran': 75000,
        'kategori_anggaran': 'sedang',
        'kategori': 'edukasi',
        'deskripsi': 'Taman nasional dengan konservasi gajah sumatera',
        'rating': 4.8
    },
    {
        'id': 'W003',
        'nama': 'Gunung Rajabasa',
        'lokasi': 'Lampung Selatan',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Gunung dengan pemandangan Selat Sunda yang menakjubkan',
        'rating': 4.3
    },
    {
        'id': 'W004',
        'nama': 'Pahawang Island',
        'lokasi': 'Pesawaran',
        'anggaran': 200000,
        'kategori_anggaran': 'premium',
        'kategori': 'pantai',
        'deskripsi': 'Pulau eksotis dengan snorkeling dan diving terbaik',
        'rating': 4.7
    },
    {
        'id': 'W005',
        'nama': 'Curug Tujuh',
        'lokasi': 'Lampung Barat',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun bertingkat dengan tujuh tingkatan yang indah',
        'rating': 4.4
    },
    {
        'id': 'W006',
        'nama': 'Museum Lampung',
        'lokasi': 'Bandar Lampung',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Museum dengan koleksi budaya dan sejarah Lampung',
        'rating': 4.1
    },
    {
        'id': 'W007',
        'nama': 'Taman Wisata Lembah Hijau',
        'lokasi': 'Bandar Lampung',
        'anggaran': 45000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman rekreasi dengan berbagai wahana dan pemandangan hijau',
        'rating': 4.2
    },
    {
        'id': 'W008',
        'nama': 'Pantai Sari Ringgung',
        'lokasi': 'Pesawaran',
        'anggaran': 180000,
        'kategori_anggaran': 'premium',
        'kategori': 'pantai',
        'deskripsi': 'Resort pantai dengan cottage dan fasilitas lengkap',
        'rating': 4.6
    },
    {
        'id': 'W009',
        'nama': 'Pantai Klara',
        'lokasi': 'Lampung Selatan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan suasana tenang dan pemandangan sunset yang indah',
        'rating': 4.3
    },
    {
        'id': 'W010',
        'nama': 'Danau Ranau',
        'lokasi': 'Lampung Barat',
        'anggaran': 50000,
        'kategori_anggaran': 'sedang',
        'kategori': 'taman',
        'deskripsi': 'Danau vulkanik terbesar kedua di Sumatera dengan pemandangan memukau',
        'rating': 4.7
    },
    {
        'id': 'W011',
        'nama': 'Bukit Mas',
        'lokasi': 'Lampung Tengah',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit dengan hamparan kebun teh dan udara yang sejuk',
        'rating': 4.4
    },
    {
        'id': 'W012',
        'nama': 'Pantai Teluk Kiluan',
        'lokasi': 'Tanggamus',
        'anggaran': 150000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pantai terkenal dengan atraksi lumba-lumba liar di pagi hari',
        'rating': 4.8
    },
    {
        'id': 'W013',
        'nama': 'Air Terjun Curup Gangsa',
        'lokasi': 'Tanggamus',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun indah dengan kolam alami yang jernih',
        'rating': 4.5
    },
    {
        'id': 'W014',
        'nama': 'Pulau Tegal Mas',
        'lokasi': 'Pesawaran',
        'anggaran': 250000,
        'kategori_anggaran': 'premium',
        'kategori': 'pantai',
        'deskripsi': 'Pulau pribadi dengan snorkeling spot dan penginapan eksklusif',
        'rating': 4.6
    },
    {
        'id': 'W015',
        'nama': 'Benteng Kuto Besak',
        'lokasi': 'Bandar Lampung',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Benteng peninggalan Kesultanan Banten dengan nilai sejarah tinggi',
        'rating': 4.0
    },
    {
        'id': 'W016',
        'nama': 'Pantai Gigi Hiu',
        'lokasi': 'Tanggamus',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai unik dengan formasi batu karang runcing yang instagramable',
        'rating': 4.6
    },
    {
        'id': 'W017',
        'nama': 'Air Terjun Putri Malu',
        'lokasi': 'Way Kanan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun setinggi 80 meter dengan suasana hutan tropis yang asri',
        'rating': 4.7
    },
    {
        'id': 'W018',
        'nama': 'Lembah Batu Brak',
        'lokasi': 'Lampung Barat',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata lembah dengan suasana alam pedesaan dan pegunungan',
        'rating': 4.3
    },
    {
        'id': 'W019',
        'nama': 'Pantai Minang Rua',
        'lokasi': 'Lampung Selatan',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai cantik dengan tebing batu dan spot foto yang menarik',
        'rating': 4.6
    },
    {
        'id': 'W020',
        'nama': 'Taman Kupu-Kupu Gita Persada',
        'lokasi': 'Bandar Lampung',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Taman konservasi kupu-kupu dengan lingkungan hutan lindung',
        'rating': 4.4
    },
    {
        'id': 'W021',
        'nama': 'Bukit Sakura',
        'lokasi': 'Bandar Lampung',
        'anggaran': 40000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bukit dengan tema ala Jepang dan spot foto bunga sakura artifisial',
        'rating': 4.2
    },
    {
        'id': 'W022',
        'nama': 'Wira Garden',
        'lokasi': 'Bandar Lampung',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman rekreasi keluarga dengan udara segar dan banyak wahana foto',
        'rating': 4.1
    },
    {
        'id': 'W023',
        'nama': 'Pantai Sebalang',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan sunset terbaik dan area nongkrong anak muda',
        'rating': 4.4
    },
    {
        'id': 'W024',
        'nama': 'Bendungan Batu Tegi',
        'lokasi': 'Tanggamus',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bendungan besar dengan pemandangan danau yang luas dan tenang',
        'rating': 4.3
    },
    {
        'id': 'W025',
        'nama': 'Taman Purbakala Pugung Raharjo',
        'lokasi': 'Lampung Timur',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Situs bersejarah dengan peninggalan megalitikum dan taman terbuka',
        'rating': 4.2
    },
    {
        'id': 'W026',
        'nama': 'Curup Kedaton',
        'lokasi': 'Pesawaran',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tersembunyi dengan kolam alami berwarna kehijauan',
        'rating': 4.5
    },
    {
        'id': 'W027',
        'nama': 'Taman Asmoro',
        'lokasi': 'Pringsewu',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman keluarga dengan area bermain dan spot foto romantis',
        'rating': 4.0
    },
    {
        'id': 'W028',
        'nama': 'Pantai Batu Lapis',
        'lokasi': 'Lampung Selatan',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan formasi batuan berlapis unik di tepi laut',
        'rating': 4.6
    },
    {
        'id': 'W029',
        'nama': 'Kampung Vietnam',
        'lokasi': 'Bandar Lampung',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Tempat wisata dengan spot foto perbukitan dan pemandangan laut',
        'rating': 4.1
    },
    {
        'id': 'W030',
        'nama': 'Pantai Mandiri',
        'lokasi': 'Pesisir Barat',
        'anggaran': 50000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan ombak besar yang cocok untuk surfing',
        'rating': 4.7
    },
    {
        'id': 'W031',
        'nama': 'Bukit Pangonan',
        'lokasi': 'Pringsewu',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bukit dengan view luas, spot foto unik, dan udara segar',
        'rating': 4.4
    },
    {
        'id': 'W032',
        'nama': 'Pantai Walur',
        'lokasi': 'Pesisir Barat',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai pasir putih yang luas dan cocok untuk bersantai bersama keluarga',
        'rating': 4.4
    },
    {
        'id': 'W033',
        'nama': 'Bukit Kabut Bawang Bakung',
        'lokasi': 'Lampung Barat',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit dengan pemandangan kabut pagi yang menakjubkan',
        'rating': 4.5
    },
    {
        'id': 'W034',
        'nama': 'Talang Indah',
        'lokasi': 'Pringsewu',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman rekreasi dengan spot foto dan jembatan gantung panjang',
        'rating': 4.2
    },
    {
        'id': 'W035',
        'nama': 'Pantai Laguna',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan suasana alami dan air laut yang jernih',
        'rating': 4.3
    },
    {
        'id': 'W036',
        'nama': 'Gunung Seminung',
        'lokasi': 'Lampung Barat',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Gunung yang mengelilingi Danau Ranau dengan jalur pendakian menantang',
        'rating': 4.6
    },
    {
        'id': 'W037',
        'nama': 'Air Terjun Way Lalaan',
        'lokasi': 'Tanggamus',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun dua tingkat yang mudah dijangkau dan fotogenik',
        'rating': 4.5
    },
    {
        'id': 'W038',
        'nama': 'Puncak Mas',
        'lokasi': 'Bandar Lampung',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Destinasi hits dengan rumah pohon dan view kota dari ketinggian',
        'rating': 4.4
    },
    {
        'id': 'W039',
        'nama': 'Sumber Jaya Green Village',
        'lokasi': 'Lampung Barat',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman hijau dengan suasana pedesaan dan spot foto kreatif',
        'rating': 4.2
    },
    {
        'id': 'W040',
        'nama': 'Pantai Tanjung Setia',
        'lokasi': 'Pesisir Barat',
        'anggaran': 50000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan ombak kelas dunia, favorit para peselancar',
        'rating': 4.8
    },
    {
        'id': 'W041',
        'nama': 'Gunung Pesagi',
        'lokasi': 'Lampung Barat',
        'anggaran': 40000,
        'kategori_anggaran': 'sedang',
        'kategori': 'gunung',
        'deskripsi': 'Gunung tertinggi di Lampung dengan jalur pendakian menantang',
        'rating': 4.7
    },
    {
        'id': 'W042',
        'nama': 'Air Terjun Curug Sidok',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun kecil namun indah dengan kolam alami yang jernih',
        'rating': 4.3
    },
    {
        'id': 'W043',
        'nama': 'Kebun Karet Trikora',
        'lokasi': 'Lampung Tengah',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Area kebun karet luas untuk edukasi dan foto outdoor',
        'rating': 4.1
    },
    {
        'id': 'W044',
        'nama': 'Pantai Dewi Mandapa',
        'lokasi': 'Pesawaran',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan spot perahu kayu dan rumah-rumah estetis di laut',
        'rating': 4.6
    },
    {
        'id': 'W045',
        'nama': 'Taman Agro Wisata BBI',
        'lokasi': 'Metro',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Agrowisata edukasi tentang tanaman dan bibit unggul',
        'rating': 4.0
    },
    {
        'id': 'W046',
        'nama': 'Bukit Idaman',
        'lokasi': 'Tanggamus',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bukit dengan gardu pandang dan panorama indah',
        'rating': 4.3
    },
    {
        'id': 'W047',
        'nama': 'Pantai Karang Nyimbor',
        'lokasi': 'Pesisir Barat',
        'anggaran': 45000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pantai populer untuk surfing dengan ombak besar',
        'rating': 4.7
    },
    {
        'id': 'W048',
        'nama': 'Curup Penataran',
        'lokasi': 'Lampung Utara',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tersembunyi dengan akses yang masih alami',
        'rating': 4.2
    },
    {
        'id': 'W049',
        'nama': 'Kebun Raya Liwa',
        'lokasi': 'Lampung Barat',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Kebun raya dengan koleksi tanaman endemik Sumatera',
        'rating': 4.5
    },
    {
        'id': 'W050',
        'nama': 'Waterpark Citra Garden',
        'lokasi': 'Bandar Lampung',
        'anggaran': 45000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Waterpark populer dengan berbagai wahana seru untuk keluarga',
        'rating': 4.2
    },
    {
        'id': 'W051',
        'nama': 'Taman Dipangga',
        'lokasi': 'Lampung Utara',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman kota sederhana untuk bersantai dan olahraga ringan',
        'rating': 4.0
    },
    {
        'id': 'W052',
        'nama': 'Pantai Mandasari',
        'lokasi': 'Pesisir Barat',
        'anggaran': 55000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan ombak besar dan panorama karang yang eksotis',
        'rating': 4.6
    },
    {
        'id': 'W053',
        'nama': 'Pulau Mahitam',
        'lokasi': 'Pesawaran',
        'anggaran': 250000,
        'kategori_anggaran': 'premium',
        'kategori': 'pantai',
        'deskripsi': 'Pulau kecil dengan jembatan pasir dan snorkeling yang memukau',
        'rating': 4.7
    },
    {
        'id': 'W054',
        'nama': 'Bukit Aslan',
        'lokasi': 'Bandar Lampung',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata bukit kekinian dengan instalasi seni patung, taman bunga, dan pemandangan kota',
        'rating': 4.5
    },
    {
        'id': 'W055',
        'nama': 'Slanik Waterpark',
        'lokasi': 'Lampung Selatan',
        'anggaran': 45000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Waterpark terbesar di Lampung dengan kolam ombak dan seluncuran ekstrem',
        'rating': 4.5
    },
    {
        'id': 'W056',
        'nama': 'Muncak Teropong Laut',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit dengan pemandangan Teluk Lampung yang memukau dari ketinggian',
        'rating': 4.3
    },
    {
        'id': 'W057',
        'nama': 'Pantai Wartawan',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai unik yang memiliki sumber air panas alami di tepi laut',
        'rating': 4.2
    },
    {
        'id': 'W058',
        'nama': 'Curup Kereta',
        'lokasi': 'Way Kanan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun lebar dan bertingkat yang sering disebut sebagai Niagara Mini Way Kanan',
        'rating': 4.6
    },
    {
        'id': 'W059',
        'nama': 'Kawah Nirwana Suoh',
        'lokasi': 'Lampung Barat',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Wisata geotermal dengan kawah keramik alami dan danau asam yang eksotis',
        'rating': 4.7
    },
    {
        'id': 'W060',
        'nama': 'Pantai Labuhan Jukung',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Ikon wisata Krui, spot terbaik menikmati sunset dan melihat peselancar',
        'rating': 4.5
    },
    {
        'id': 'W061',
        'nama': 'Mata Air Way Sumpuk',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Kolam mata air alami yang sangat jernih, populer untuk foto underwater',
        'rating': 4.4
    },
    {
        'id': 'W062',
        'nama': 'Bukit Cendana',
        'lokasi': 'Pesawaran',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Camping ground dengan pemandangan perbukitan hijau dan laut dari kejauhan',
        'rating': 4.3
    },
    {
        'id': 'W063',
        'nama': 'Pantai Kahai',
        'lokasi': 'Lampung Selatan',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Kawasan wisata pantai lengkap dengan resort dan waterboom',
        'rating': 4.1
    },
    {
        'id': 'W064',
        'nama': 'Lembah Durian Farm',
        'lokasi': 'Bandar Lampung',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Agrowisata durian dengan suasana camping ground yang asri dan sejuk',
        'rating': 4.5
    },
    {
        'id': 'W065',
        'nama': 'Taman Nasional Bukit Barisan Selatan',
        'lokasi': 'Lampung Barat',
        'anggaran': 50000,
        'kategori_anggaran': 'sedang',
        'kategori': 'edukasi',
        'deskripsi': 'Hutan hujan tropis Situs Warisan Dunia UNESCO, habitat Badak dan Harimau',
        'rating': 4.8
    },
    {
        'id': 'W066',
        'nama': 'Pantai Kedu Warna',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai kekinian dengan view Gunung Rajabasa dan dekorasi lampu',
        'rating': 4.3
    },
    {
        'id': 'W067',
        'nama': 'Lengkung Langit',
        'lokasi': 'Bandar Lampung',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Spot foto instagramable dengan gerbang unik dan latar pemandangan kota',
        'rating': 4.2
    },
    {
        'id': 'W068',
        'nama': 'Pantai Tanjung Tuha',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan tebing curam dan pemandangan laut lepas yang dramatis',
        'rating': 4.4
    },
    {
        'id': 'W069',
        'nama': 'Air Terjun Lembah Pelangi',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tinggi di kawasan Ulubelu yang sering membiaskan pelangi',
        'rating': 4.5
    },
    {
        'id': 'W070',
        'nama': 'Pantai Tapak Kera',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Hidden gem dengan medan menantang, menyajikan laguna biru dan karang tajam',
        'rating': 4.6
    },
    {
        'id': 'W071',
        'nama': 'Tugu Rato Nago Besanding',
        'lokasi': 'Tulang Bawang Barat',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Ikon patung naga yang megah dan artistik di simpang tiga Tubaba',
        'rating': 4.5
    },
    {
        'id': 'W072',
        'nama': 'Pulau Mengkudu',
        'lokasi': 'Lampung Selatan',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau ikonik dengan fenomena pasir timbul (jembatan pasir) saat air surut',
        'rating': 4.7
    },
    {
        'id': 'W073',
        'nama': 'Bendungan Way Rarem',
        'lokasi': 'Lampung Utara',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bendungan seluas 49 hektar dengan taman bermain dan pemandangan air',
        'rating': 4.2
    },
    {
        'id': 'W074',
        'nama': 'Gua Matu',
        'lokasi': 'Pesisir Barat',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Gua keramat di tebing pantai dengan pemandangan Samudera Hindia',
        'rating': 4.4
    },
    {
        'id': 'W075',
        'nama': 'Taman Kehati Mesuji',
        'lokasi': 'Mesuji',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman Keanekaragaman Hayati dengan kebun binatang mini dan kolam renang',
        'rating': 4.1
    },
    {
        'id': 'W076',
        'nama': 'Pantai Cemara Sewu',
        'lokasi': 'Lampung Selatan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai landai dengan deretan pohon cemara udang yang rimbun dan teduh',
        'rating': 4.3
    },
    {
        'id': 'W077',
        'nama': 'Curup Jarum',
        'lokasi': 'Way Kanan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun kembar dengan debit air deras di tengah hutan karet',
        'rating': 4.5
    },
    {
        'id': 'W078',
        'nama': 'Uluan Nughik',
        'lokasi': 'Tulang Bawang Barat',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Desa budaya dengan rumah panggung khas Lampung dan suasana pedesaan',
        'rating': 4.6
    },
    {
        'id': 'W079',
        'nama': 'Pantai Kerang Mas',
        'lokasi': 'Lampung Timur',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai wisata keluarga di pesisir timur dengan fasilitas gazebo',
        'rating': 4.2
    },
    {
        'id': 'W080',
        'nama': 'Air Terjun Anglo',
        'lokasi': 'Pesawaran',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tersembunyi dengan kolam jernih berwarna biru toska',
        'rating': 4.5
    },
    {
        'id': 'W081',
        'nama': 'Danau Hijau Ulubelu',
        'lokasi': 'Tanggamus',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Danau air panas vulkanik berwarna hijau di kawasan geothermal PLTP Ulubelu',
        'rating': 4.4
    },
    {
        'id': 'W082',
        'nama': 'Bukit Selalau',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Bukit karang di tepi laut, spot terbaik memandang garis pantai Krui',
        'rating': 4.6
    },
    {
        'id': 'W083',
        'nama': 'Pantai Guci Batu Kapal',
        'lokasi': 'Lampung Selatan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan legenda batu karang besar menyerupai kapal yang karam',
        'rating': 4.3
    },
    {
        'id': 'W084',
        'nama': 'Dam Raman',
        'lokasi': 'Metro',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bendungan irigasi yang disulap menjadi tempat wisata air dan taman keluarga',
        'rating': 4.3
    },

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
    {
        'id': 'W111',
        'nama': 'Lanakila Lake',
        'lokasi': 'Pringsewu',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata bendungan dengan suasana piknik dan penyewaan perahu',
        'rating': 4.2
    },
    {
        'id': 'W112',
        'nama': 'Air Terjun Lamuran',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun ganda yang tersembunyi di kaki Gunung Tanggamus',
        'rating': 4.3
    },
    {
        'id': 'W113',
        'nama': 'Curug Anggal',
        'lokasi': 'Way Kanan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun lebar yang indah namun memerlukan perjalanan ekstra',
        'rating': 4.4
    },
    {
        'id': 'W114',
        'nama': 'Bendungan Tirta Shinta',
        'lokasi': 'Lampung Utara',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Bendungan air tenang yang cocok untuk bersantai sore hari',
        'rating': 4.0
    },
    {
        'id': 'W115',
        'nama': 'Masjid Agung Al-Furqon',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Masjid terbesar di Bandar Lampung dengan menara tinggi (lift) melihat kota',
        'rating': 4.7
    },
    {
        'id': 'W116',
        'nama': 'Vihara Thay Hin Bio',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Vihara tertua di Lampung yang terletak di kawasan pecinan Teluk Betung',
        'rating': 4.4
    },
    {
        'id': 'W117',
        'nama': 'Pulau Kelagian Kecil',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau mungil berpasir putih bersih, tempat favorit untuk snorkeling pemula',
        'rating': 4.7
    },
    {
        'id': 'W118',
        'nama': 'Pantai Bensam',
        'lokasi': 'Pesawaran',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai keluarga dengan fasilitas lengkap dan ombak yang tenang',
        'rating': 4.2
    },
    {
        'id': 'W119',
        'nama': 'Pulau Wayang',
        'lokasi': 'Pesawaran',
        'anggaran': 250000,
        'kategori_anggaran': 'premium',
        'kategori': 'pantai',
        'deskripsi': 'Gugusan pulau karang yang disebut sebagai Raja Ampat-nya Lampung',
        'rating': 4.8
    },
    {
        'id': 'W120',
        'nama': 'Grand Elty Krakatoa',
        'lokasi': 'Lampung Selatan',
        'anggaran': 75000,
        'kategori_anggaran': 'sedang',
        'kategori': 'pantai',
        'deskripsi': 'Kawasan resort dan pantai eksklusif dengan fasilitas watersport lengkap',
        'rating': 4.6
    },
    {
        'id': 'W121',
        'nama': 'Pantai Bagus',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai rakyat yang ramai dikunjungi dengan view Gunung Rajabasa',
        'rating': 4.1
    },
    {
        'id': 'W122',
        'nama': 'Rest Area Puncak Sumber Jaya',
        'lokasi': 'Lampung Barat',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Rest area dengan patung tugu dan pemandangan lembah hijau yang luas',
        'rating': 4.4
    },
    {
        'id': 'W123',
        'nama': 'Pinus Ecopark',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Hutan pinus yang sejuk, cocok untuk piknik dan hammock',
        'rating': 4.3
    },
    {
        'id': 'W124',
        'nama': 'Pantai Melasti',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Pantai tempat upacara Melasti umat Hindu dengan Pura di tepi laut',
        'rating': 4.5
    },
    {
        'id': 'W125',
        'nama': 'Pantai Way Redak',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai tenang yang dekat dengan pusat kota Krui',
        'rating': 4.2
    },
    {
        'id': 'W126',
        'nama': 'Pantai Terbaya',
        'lokasi': 'Tanggamus',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan hamparan batu kerikil unik dan pemandangan Teluk Semaka',
        'rating': 4.2
    },
    {
        'id': 'W127',
        'nama': 'Air Terjun Tirai',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun berbentuk melebar seperti tirai di tengah hutan rimbun',
        'rating': 4.4
    },
    {
        'id': 'W128',
        'nama': 'Wisata Sawah Bertingkat Bantul',
        'lokasi': 'Metro',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Area persawahan dengan konsep terasering buatan untuk spot foto',
        'rating': 4.0
    },
    {
        'id': 'W129',
        'nama': 'Tugu Pepadun',
        'lokasi': 'Lampung Tengah',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Landmark ikonik Lampung Tengah berupa patung tangan dan singgasana adat',
        'rating': 4.1
    },
    {
        'id': 'W130',
        'nama': 'Danau Tirta Gangga',
        'lokasi': 'Lampung Tengah',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Danau buatan yang memiliki patung Bima dan nuansa budaya Bali',
        'rating': 4.3
    },
    {
        'id': 'W131',
        'nama': 'Pintu Langit',
        'lokasi': 'Bandar Lampung',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Spot foto dengan konsep pintu kaca menghadap pemandangan kota',
        'rating': 4.2
    },
    {
        'id': 'W132',
        'nama': 'Alam Wawai',
        'lokasi': 'Bandar Lampung',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman wisata eco-friendly dengan amphitheater alam dan camping ground',
        'rating': 4.3
    },
    {
        'id': 'W133',
        'nama': 'Pantai Klara 2',
        'lokasi': 'Pesawaran',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Lanjutan Pantai Klara dengan fasilitas pondokan yang lebih banyak',
        'rating': 4.2
    },
    {
        'id': 'W134',
        'nama': 'Bronjong Way Lima',
        'lokasi': 'Pesawaran',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata sungai berbatu dengan air jernih, cocok untuk bermain air anak-anak',
        'rating': 4.1
    },
    {
        'id': 'W135',
        'nama': 'Pantai Alau-Alau',
        'lokasi': 'Lampung Selatan',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai pasir putih luas yang sering digunakan untuk gathering perusahaan',
        'rating': 4.3
    },
    {
        'id': 'W136',
        'nama': 'Pantai Tanjung Beo',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai baru dengan banyak spot foto buatan yang warna-warni',
        'rating': 4.1
    },
    {
        'id': 'W137',
        'nama': 'Lumbok Seminung Resort',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Area resort milik Pemda di tepi Danau Ranau dengan pemandangan gunung',
        'rating': 4.5
    },
    {
        'id': 'W138',
        'nama': 'Gereja Katedral Kristus Raja',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Gereja bersejarah di pusat kota dengan arsitektur klasik yang indah',
        'rating': 4.4
    },
    {
        'id': 'W139',
        'nama': 'Pantai Belebuk',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai nelayan yang tenang dengan pasir putih dan air dangkal',
        'rating': 4.0
    },
    {
        'id': 'W140',
        'nama': 'Bukit Foggy',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit yang hampir selalu tertutup kabut, memberikan nuansa mistis dan sejuk',
        'rating': 4.3
    },
    {
        'id': 'W141',
        'nama': 'Wisata Alam 21',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Kawasan agrowisata durian dan spot foto di perbukitan',
        'rating': 4.1
    },
    {
        'id': 'W142',
        'nama': 'Pantai Canti',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Dermaga penyeberangan ke Pulau Sebesi yang memiliki pemandangan indah',
        'rating': 4.2
    },
    {
        'id': 'W143',
        'nama': 'Air Terjun Sinar Tiga',
        'lokasi': 'Pesawaran',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tinggi di kawasan Padang Cermin yang masih sangat alami',
        'rating': 4.3
    },
    {
        'id': 'W144',
        'nama': 'Taman Wisata Muara Indah',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Taman di tepi laut Kota Agung, ikon pariwisata Tanggamus',
        'rating': 4.1
    },
    {
        'id': 'W145',
        'nama': 'Pantai Rio by The Beach',
        'lokasi': 'Lampung Selatan',
        'anggaran': 35000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai viral dengan pasir putih bersih dan fasilitas bean bag yang estetik',
        'rating': 4.7
    },
    {
        'id': 'W146',
        'nama': 'Pringsewu Ranch',
        'lokasi': 'Pringsewu',
        'anggaran': 20000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Wisata berkuda dan peternakan dengan nuansa ala peternakan Amerika',
        'rating': 4.2
    },
    {
        'id': 'W147',
        'nama': 'Bukit Blitar',
        'lokasi': 'Pringsewu',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit sederhana untuk melihat pemandangan sawah Pringsewu dari atas',
        'rating': 4.0
    },
    {
        'id': 'W148',
        'nama': 'Telaga Gupit',
        'lokasi': 'Pringsewu',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Telaga alami di kaki bukit yang cocok untuk memancing dan bersantai',
        'rating': 4.1
    },
    {
        'id': 'W149',
        'nama': 'Air Terjun Pagasan',
        'lokasi': 'Pringsewu',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun musiman yang sangat indah saat musim penghujan',
        'rating': 4.0
    },
    {
        'id': 'W150',
        'nama': 'Grojogan Sewu Pringsewu',
        'lokasi': 'Pringsewu',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Replika air terjun dengan bendungan kecil dan suasana pedesaan',
        'rating': 3.9
    },
    {
        'id': 'W151',
        'nama': 'Sungai Kabung',
        'lokasi': 'Mesuji',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wisata sungai untuk memancing dan melihat kehidupan rawa Mesuji',
        'rating': 4.0
    },
    {
        'id': 'W152',
        'nama': 'Islamic Center Sukadana',
        'lokasi': 'Lampung Timur',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Pusat kegiatan keagamaan dengan taman yang luas di Lampung Timur',
        'rating': 4.3
    },
    {
        'id': 'W153',
        'nama': 'Danau Kemuning',
        'lokasi': 'Lampung Timur',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Danau kecil yang asri, sering digunakan untuk kemah pramuka',
        'rating': 4.0
    },
    {
        'id': 'W154',
        'nama': 'Wisata Mangrove Sriminosari',
        'lokasi': 'Lampung Timur',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Hutan mangrove di pesisir timur dengan jembatan warna-warni',
        'rating': 4.2
    },
    {
        'id': 'W155',
        'nama': 'Danau Beringin',
        'lokasi': 'Lampung Timur',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Danau irigasi yang menjadi tempat rekreasi murah meriah warga sekitar',
        'rating': 3.9
    },
    {
        'id': 'W156',
        'nama': 'Kolam Renang Palem Indah',
        'lokasi': 'Metro',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Wahana kolam renang keluarga favorit di Kota Metro',
        'rating': 4.3
    },
    {
        'id': 'W157',
        'nama': 'Jembatan Gantung Way Sekampung',
        'lokasi': 'Pringsewu',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Jembatan gantung terpanjang di Lampung, spot foto ikonik Pringsewu',
        'rating': 4.4
    },
    {
        'id': 'W158',
        'nama': 'Air Terjun Batu Lapis',
        'lokasi': 'Tanggamus',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun dengan dinding tebing berlapis-lapis seperti kue lapis',
        'rating': 4.5
    },
    {
        'id': 'W159',
        'nama': 'Pantai Saw Mill',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai alami di pesisir Tanggamus yang belum banyak terjamah',
        'rating': 4.1
    },
    {
        'id': 'W160',
        'nama': 'Air Terjun Sepapa Kiri',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun di dalam kawasan Taman Nasional Bukit Barisan Selatan',
        'rating': 4.6
    },
    {
        'id': 'W161',
        'nama': 'Goa Kelelawar',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Goa alami habitat ribuan kelelawar, aroma cukup menyengat namun eksotis',
        'rating': 4.0
    },
    {
        'id': 'W162',
        'nama': 'Makam Radin Intan II',
        'lokasi': 'Lampung Selatan',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Makam Pahlawan Nasional asal Lampung di Kalianda',
        'rating': 4.5
    },
    {
        'id': 'W163',
        'nama': 'Benteng Orange',
        'lokasi': 'Tulang Bawang',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Situs sejarah bekas benteng pertahanan di masa kolonial',
        'rating': 3.8
    },
    {
        'id': 'W164',
        'nama': 'Pantai Duta Wisata',
        'lokasi': 'Bandar Lampung',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai legendaris di Teluk Betung dengan pemandangan aktivitas laut',
        'rating': 3.9
    },
    {
        'id': 'W165',
        'nama': 'Pantai Tirtayasa',
        'lokasi': 'Bandar Lampung',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai yang bersebelahan dengan Duta Wisata, populer tahun 90-an',
        'rating': 3.8
    },
    {
        'id': 'W166',
        'nama': 'Pantai Puri Gading',
        'lokasi': 'Bandar Lampung',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai di bawah perumahan elit dengan akses jembatan menuju laut',
        'rating': 4.0
    },
    {
        'id': 'W167',
        'nama': 'Pantai Suak',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai sepi yang tenang, cocok untuk menyendiri dan mencari inspirasi',
        'rating': 4.2
    },
    {
        'id': 'W168',
        'nama': 'Pantai Batu Mandi',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan gugusan batu vulkanik hitam di tepi laut',
        'rating': 4.1
    },
    {
        'id': 'W169',
        'nama': 'Pantai Setigi Heni',
        'lokasi': 'Lampung Selatan',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai pasir putih di Kalianda dengan ombak yang cukup bersahabat',
        'rating': 4.3
    },
    {
        'id': 'W170',
        'nama': 'Air Terjun Way Tayas',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun di kaki Gunung Rajabasa dengan suasana hutan kakao',
        'rating': 4.4
    },
    {
        'id': 'W171',
        'nama': 'Air Terjun Cicurug',
        'lokasi': 'Lampung Selatan',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun kecil yang sering dijadikan tempat bermain air anak-anak desa',
        'rating': 4.0
    },
    {
        'id': 'W172',
        'nama': 'Air Terjun Kota Batu',
        'lokasi': 'Lampung Tengah',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun unik di perbatasan Lamteng dan Tanggamus',
        'rating': 4.2
    },
    {
        'id': 'W173',
        'nama': 'Pantai Karang Bolong',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai yang memiliki batu karang besar berlubang akibat abrasi',
        'rating': 4.1
    },
    {
        'id': 'W174',
        'nama': 'Pantai Biha',
        'lokasi': 'Pesisir Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai panjang yang landai, sering jadi rest area lintas barat',
        'rating': 4.1
    },
    {
        'id': 'W175',
        'nama': 'Curug Kincir',
        'lokasi': 'Way Kanan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun dengan debit air yang tidak terlalu deras, aman untuk mandi',
        'rating': 4.0
    },
    {
        'id': 'W176',
        'nama': 'Patung Empat Marga',
        'lokasi': 'Tulang Bawang Barat',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Monumen relief wajah empat tokoh adat (Megow Pak) Tulang Bawang',
        'rating': 4.3
    },
    {
        'id': 'W177',
        'nama': 'Wisata Alam Kubu Perahu',
        'lokasi': 'Lampung Barat',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Pintu masuk TNBBS dengan sungai jernih dan pohon raksasa',
        'rating': 4.5
    },
    {
        'id': 'W178',
        'nama': 'Puncak Jaya Genting',
        'lokasi': 'Pesawaran',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Spot melihat laut Teluk Lampung dari ketinggian bukit Tahura',
        'rating': 4.2
    },
    {
        'id': 'W179',
        'nama': 'Pulau Balak',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau berpasir putih luas, salah satu dari tiga pulau serangkai di Punduh',
        'rating': 4.5
    },
    {
        'id': 'W180',
        'nama': 'Pulau Lok',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau tetangga Pulau Balak, lebih sepi dan alami',
        'rating': 4.4
    },
    {
        'id': 'W181',
        'nama': 'Pulau Lunik',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pulau terkecil di gugusan Punduh Pidada, spot makan siang saat hopping island',
        'rating': 4.3
    },
    {
        'id': 'W182',
        'nama': 'Pantai Mutun 2 (MS Town)',
        'lokasi': 'Pesawaran',
        'anggaran': 30000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pengembangan kawasan Mutun dengan konsep lebih modern',
        'rating': 4.2
    },
    {
        'id': 'W183',
        'nama': 'Pantai Tembikil',
        'lokasi': 'Pesawaran',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai tersembunyi dekat markas marinir dengan karang yang bagus',
        'rating': 4.3
    },
    {
        'id': 'W184',
        'nama': 'Pantai Batu Alif',
        'lokasi': 'Lampung Selatan',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan batu besar berdiri tegak menyerupai huruf Alif',
        'rating': 4.4
    },
    {
        'id': 'W185',
        'nama': 'Pantai Cukuh Balak',
        'lokasi': 'Tanggamus',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai nelayan dengan ikan segar murah dan pemandangan teluk',
        'rating': 4.0
    },
    {
        'id': 'W186',
        'nama': 'Pantai Karang Putih',
        'lokasi': 'Tanggamus',
        'anggaran': 15000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan dominasi batuan karang berwarna putih bersih',
        'rating': 4.3
    },
    {
        'id': 'W187',
        'nama': 'Pantai Karang Bebai',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai dengan legenda batu pengantin, bebatuan unik tersebar di pantai',
        'rating': 4.2
    },
    {
        'id': 'W188',
        'nama': 'Air Terjun Beringin',
        'lokasi': 'Lampung Utara',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun tinggi yang dikelilingi pohon beringin tua',
        'rating': 4.1
    },
    {
        'id': 'W189',
        'nama': 'Bukit Neba',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'gunung',
        'deskripsi': 'Bukit dengan pemandangan ilalang dan view Gunung Tanggamus yang megah',
        'rating': 4.3
    },
    {
        'id': 'W190',
        'nama': 'Green Canyon',
        'lokasi': 'Way Kanan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun unik dengan kontur tebing batu cadas yang eksotis',
        'rating': 4.2
    },
    {
        'id': 'W191',
        'nama': 'Pantai Kedu',
        'lokasi': 'Lampung Selatan',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai yang terkenal dengan kerangka kapal karam yang artistik',
        'rating': 4.2
    },
    {
        'id': 'W192',
        'nama': 'Pantai Muara Indah',
        'lokasi': 'Tanggamus',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'pantai',
        'deskripsi': 'Pantai reklamasi di Kota Agung yang rapi dengan patung lumba-lumba',
        'rating': 4.2
    },
    {
        'id': 'W193',
        'nama': 'Masjid Al-Anwar',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Masjid tertua di Bandar Lampung yang menjadi saksi letusan Krakatau 1883',
        'rating': 4.5
    },
    {
        'id': 'W194',
        'nama': 'Agro Wisata PKK Agropark',
        'lokasi': 'Bandar Lampung',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Taman edukasi pertanian dan peternakan di tengah kota, Sabah Balau',
        'rating': 4.1
    },
    {
        'id': 'W195',
        'nama': 'Hutan Kera Tirtosari',
        'lokasi': 'Bandar Lampung',
        'anggaran': 5000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Hutan kota kecil yang dihuni kawanan kera ekor panjang jinak',
        'rating': 3.8
    },
    {
        'id': 'W196',
        'nama': 'Sumur Putri',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'murah',
        'kategori': 'sejarah',
        'deskripsi': 'Situs legenda asal mula Teluk Betung dengan pemandangan sungai',
        'rating': 3.9
    },
    {
        'id': 'W197',
        'nama': 'Bukit Randu',
        'lokasi': 'Bandar Lampung',
        'anggaran': 0,
        'kategori_anggaran': 'premium',
        'kategori': 'kuliner',
        'deskripsi': 'Restoran dan hotel di atas bukit dengan view terbaik kota malam hari',
        'rating': 4.6
    },
    {
        'id': 'W198',
        'nama': 'Desa Wisata Rigis Jaya',
        'lokasi': 'Lampung Barat',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'edukasi',
        'deskripsi': 'Kampung Kopi, sentra perkebunan kopi robusta Lampung Barat',
        'rating': 4.5
    },
    {
        'id': 'W199',
        'nama': 'Air Terjun Kaca',
        'lokasi': 'Pesawaran',
        'anggaran': 10000,
        'kategori_anggaran': 'murah',
        'kategori': 'air_terjun',
        'deskripsi': 'Air terjun yang aliran airnya jernih seperti kaca, dekat Tahura',
        'rating': 4.2
    },
    {
        'id': 'W200',
        'nama': 'Puncak Mas 2 (Tegal Mas View)',
        'lokasi': 'Bandar Lampung',
        'anggaran': 25000,
        'kategori_anggaran': 'murah',
        'kategori': 'taman',
        'deskripsi': 'Spot baru perluasan area wisata Sukadanaham dengan view laut',
        'rating': 4.3
    }
]
#mengambil seluruh data wisata dari file data_wisata.py
def get_all_wisata():
    return WISATA_DATA.copy()
#mengambil daftar lokasi
def get_locations():
    return LOCATION.copy()
#mengambil daftar kategori wisata
def get_categories():
    return CATEGORIES.copy()
#mengambil data koneksi antar lokasi 
def get_connections():
    return LOCATION_CONNECTIONS.copy()
