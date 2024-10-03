# Bike Sharing Data Analysis

**Nama**: Paulus Simon Halomoan Sigalingging

**Email**: email.paul.belajar@gmail.com

# Project Description

Proyek ini bertujuan untuk menganalisis dataset penyewaan sepeda guna memperoleh wawasan tentang perilaku pengguna, seperti waktu penyewaan terbanyak, pengaruh cuaca, serta perbedaan antara pengguna kasual dan terdaftar. Analisis dilakukan dengan menggunakan Python dan Pandas, sementara visualisasinya dibuat menggunakan Streamlit.

## Outline Program

### Program ini bertujuan untuk menjawab beberapa pertanyaan analisis data berikut:
1 Pada Jam berapa permintaan sewa sepeda paling banyak ?
2 Bagaimana kondisi musim mempengaruhi tingkat penggunaan sepeda ? dan pada musim kapan permintaan terbanyak ?
3 Bagaimana kondisi cuaca mempengaruhi tingkat penggunaan sepeda ? dan pada cuaca kapan permintaan terbanyak ?
4 Bagaimana penggunaan sepeda dalam tahun 2011 dan 2012 serta mana yang lebih unggul?


### Data Wrangling: 
   - Mengubah tipe data, membersihkan data, dan melakukan pemrosesan awal dataset.
   
### Exploratory Data Analysis (EDA)
   - Analisis pola penyewaan sepeda berdasarkan cuaca, waktu, hari libur, dan suhu udara.

### Visualizing Data
   - Menampilkan grafik bar dan garis untuk menunjukkan hubungan antara variabel-variabel yang dianalisis.

### Drawing Conclusions
   - Menyajikan kesimpulan dari hasil analisis data.

### Dataset yang Digunakan
- `day.csv`: Berisi data penyewaan sepeda harian.
- `hour.csv`: Berisi data penyewaan sepeda per jam.

## Cara Menjalankan Program

### Prasyarat
- Python 3.x sudah terinstal di komputer Anda.
- Pastikan Anda sudah menginstal beberapa pustaka Python yang diperlukan:
  ```bash
  pip install streamlit pandas seaborn matplotlib
  ```

### Langkah Menjalankan Program
#### Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

#### Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Run steamlit app
```
streamlit run dashboard/dashboard.py
```

### Struktur Direktori
```
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───bike_sharing.ipynb
├───README.md
└───requirements.txt
└───url.txt
```
