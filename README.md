
# 🚲 Bike Sharing Analysis Dashboard

Proyek ini merupakan bagian dari submission proyek akhir kelas **Analisis Data** di Dicoding. Saya menggunakan **Bike Sharing Dataset** (`day.csv` dan `hour.csv`) untuk menjawab pertanyaan bisnis seputar tren peminjaman sepeda berdasarkan musim, bulan, cuaca, dan hari kerja.

Dashboard interaktif dibangun menggunakan **Streamlit**.

---

## 📁 Struktur Folder

```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── data_1.csv
│   └── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## 🛠️ Setup Environment

### Via Anaconda

```bash
conda create --name bike-analysis python=3.9
conda activate bike-analysis
pip3 install -r requirements.txt
```

### Via Shell/Terminal

```bash
pipenv install
pipenv shell
pip3 install -r requirements.txt
```

---

## ▶️ Menjalankan Streamlit App

```bash
cd submission/dashboard
streamlit run dashboard.py
```

---

## 📌 Insight Proyek

- Bulan dengan peminjaman tertinggi adalah bulan ke-6.
- Musim dingin cenderung memiliki peminjaman paling rendah.
- Hari kerja memiliki rata-rata peminjaman yang lebih tinggi dibanding hari libur.
- Suhu menunjukkan korelasi positif terhadap jumlah peminjaman.

---

Proyek ini dibuat sebagai bentuk latihan eksplorasi data dan penyajian visual secara interaktif. 🚀
