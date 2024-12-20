# Naufal Sadam Sunu Iskandar
# 23.83.0952
# 23TK01
# Pemrograman Python
import requests  # untuk mengambil halaman web
from bs4 import BeautifulSoup  # untuk parsing HTML
import csv  # untuk menyimpan data ke file CSV
import time  # untuk memberikan jeda waktu

# Konfigurasi header untuk request
browser_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Membuat list untuk menyimpan semua data anime
daftar_semua_anime = []

# URL halaman pertama dan kedua
halaman_pertama = "https://myanimelist.net/topanime.php?type=airing"
halaman_kedua = "https://myanimelist.net/topanime.php?type=airing&limit=50"

# List untuk menyimpan URL
daftar_halaman = [halaman_pertama, halaman_kedua]

# Melakukan perulangan untuk setiap halaman
for halaman in daftar_halaman:
    print("="*50)
    print(f"Sedang mengambil data dari halaman ke 2")
    print("="*50)
    
    # Mengambil konten HTML dari halaman web
    try:
        hasil_request = requests.get(halaman, headers=browser_headers)
        
        # Mengecek apakah request berhasil
        if hasil_request.status_code == 200:
            print("Berhasil mengambil halaman!")
        else:
            print(f"Gagal mengambil halaman. Status code: {hasil_request.status_code}")
            continue
            
    except Exception as error:
        print(f"Terjadi kesalahan saat mengambil halaman: {error}")
        continue

    # Membuat objek BeautifulSoup untuk parsing HTML
    halaman_html = BeautifulSoup(hasil_request.text, 'html.parser')
    
    # Mencari semua anime di halaman tersebut
    daftar_anime_dihalaman = halaman_html.find_all('tr', class_='ranking-list')
    
    # Loop untuk setiap anime yang ditemukan
    for anime in daftar_anime_dihalaman:
        try:
            # Mengambil ranking anime
            bagian_ranking = anime.find('td', class_='rank ac')
            if bagian_ranking:
                ranking_anime = bagian_ranking.text.strip()
            else:
                ranking_anime = "Tidak ada ranking"
            
            # Mengambil judul anime
            bagian_judul = anime.find('div', class_='di-ib clearfix')
            if bagian_judul:
                judul_anime = bagian_judul.find('h3', class_='anime_ranking_h3')
                if judul_anime:
                    judul_anime = judul_anime.text.strip()
                else:
                    judul_anime = "Judul tidak ditemukan"
            else:
                judul_anime = "Judul tidak ditemukan"
            
            # Mengambil score anime
            bagian_score = anime.find('span', class_='score-label')
            if bagian_score:
                score_anime = bagian_score.text.strip()
            else:
                score_anime = "Tidak ada score"
            
            # Mengambil tahun rilis anime
            bagian_informasi = anime.find('div', class_='information di-ib mt4')
            if bagian_informasi:
                informasi_text = bagian_informasi.text.strip()
                baris_informasi = informasi_text.split('\n')
                
                if len(baris_informasi) > 1:
                    tahun_rilis = baris_informasi[1].split('-')[0].strip()
                else:
                    tahun_rilis = "Tahun tidak ditemukan"
            else:
                tahun_rilis = "Tahun tidak ditemukan"
            
            # Membuat dictionary untuk menyimpan data anime
            data_satu_anime = {
                'Rank': ranking_anime,
                'Title': judul_anime,
                'Score': score_anime,
                'Year': tahun_rilis
            }
            
            # Menambahkan data anime ke list utama
            daftar_semua_anime.append(data_satu_anime)
            
            # Print informasi anime yang berhasil diambil
            print(f"Berhasil mengambil data anime: {judul_anime}")
            
        except Exception as error:
            print(f"Terjadi kesalahan saat mengambil data anime: {error}")
            continue
    
    # Memberikan jeda waktu sebelum mengambil halaman berikutnya
    print("sabar.............")
    time.sleep(3)

# Menyimpan semua data ke file CSV
nama_file = "daftar_anime_top_myanimelist.csv"

try:
    # Membuka file CSV untuk menulis data
    with open(nama_file, mode='w', newline='', encoding='utf-8') as file_csv:
        # Membuat writer object
        penulis_csv = csv.DictWriter(file_csv, fieldnames=['Rank', 'Title', 'Score', 'Year'])
        
        # Menulis header
        penulis_csv.writeheader()
        
        # Menulis semua data anime
        for data_anime in daftar_semua_anime:
            penulis_csv.writerow(data_anime)
            
    print("="*50)
    print(f"Berhasil menyimpan {len(daftar_semua_anime)} data anime ke file {nama_file}")
    print("="*50)
    
except Exception as error:
    print(f"Terjadi kesalahan saat menyimpan file CSV: {error}")