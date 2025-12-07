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
