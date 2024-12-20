# Anime_List_scrap
Sebuah script Python sederhana untuk mengambil data anime yang sedang tayang (currently airing) dari MyAnimeList. Script ini akan mengambil data dari 2 halaman pertama top airing anime dan menyimpannya dalam format CSV.
Fitur

Mengambil data dari halaman Top Airing Anime MyAnimeList
Mengekstrak informasi seperti:

- Ranking
- Judul Anime
- Score
- Tahun Rilis


Menyimpan hasil scraping ke file CSV
Menggunakan delay untuk menghindari rate limiting
Error handling untuk stabilitas script

## Persyaratan

Python 3.x
Paket Python yang diperlukan ada di requirements.txt

## Cara Penggunaan

Clone repository ini:
```bash
https://github.com/nopaldev/Anime_List_scrap.git
```
## Install dependencies yang diperlukan:
```bash
pip install -r requirements.txt
```
## Jalankan script:
```bash
python3 scrap_mal.py
```
atau
```bash
python scrap_mal.py
```

### Hasil scraping akan disimpan dalam file daftar_anime_top_myanimelist.csv

## Script akan menghasilkan file CSV dengan kolom berikut:

- Rank: Peringkat anime
- Title: Judul anime
- Score: Nilai rating anime
- Year: Tahun rilis anime

## Catatan

Script ini menggunakan delay 3 detik antara request untuk menghindari pembatasan dari server
Pastikan untuk memiliki koneksi internet yang stabil saat menjalankan script
Hasil scraping mungkin berbeda tergantung waktu pengambilan data karena konten MyAnimeList yang dinamis

## Author

- Nama: Naufal Sadam Sunu Iskandar
- NIM: 23.83.0952
- Kelas: 23TK01
