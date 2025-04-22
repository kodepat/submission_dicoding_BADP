import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Load data
@st.cache_data
def load_data():
    day = pd.read_csv("data/data_1.csv")
    return day

day = load_data()

# Preprocessing
categorical_columns = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
for col in categorical_columns:
    day[col] = day[col].astype('category')

st.title("🚲 Bike Sharing Data Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_month = st.sidebar.selectbox("Pilih Bulan", sorted(day['mnth'].unique()))
filtered = day[day['mnth'] == selected_month]

# Section: Overview
st.subheader("📊 Total Peminjaman Sepeda per Bulan")
monthly_rentals = day.groupby('mnth')['cnt'].sum()
fig1, ax1 = plt.subplots()
monthly_rentals.plot(kind='bar', ax=ax1)
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Total Peminjaman")
ax1.set_title("Total Peminjaman Sepeda per Bulan")
st.pyplot(fig1)

# Section: Peminjaman Berdasarkan Musim
st.subheader("❄️ Peminjaman per Musim")
season_rentals = day.groupby('season')['cnt'].mean()
fig2, ax2 = plt.subplots()
sns.barplot(x=season_rentals.index, y=season_rentals.values, ax=ax2)
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Peminjaman")
ax2.set_title("Rata-rata Jumlah Peminjaman per Musim")
st.pyplot(fig2)

# Section: Hari Kerja vs Libur
st.subheader("🏖️ Hari Kerja vs Hari Libur")
workingday_rentals = day.groupby('workingday')['cnt'].mean()
fig3, ax3 = plt.subplots()
sns.barplot(x=workingday_rentals.index, y=workingday_rentals.values, ax=ax3)
ax3.set_xticklabels(['Libur', 'Hari Kerja'])
ax3.set_ylabel("Rata-rata Peminjaman")
ax3.set_title("Rata-rata Peminjaman: Hari Kerja vs Libur")
st.pyplot(fig3)

# Section: Korelasi Cuaca
st.subheader("🌦️ Korelasi Cuaca dengan Jumlah Peminjaman")
fig4, ax4 = plt.subplots()
sns.heatmap(day[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax4)
ax4.set_title("Heatmap Korelasi")
st.pyplot(fig4)

# Detail data bulan terpilih
st.subheader("📅 Detail Data Bulan Terpilih")
st.dataframe(filtered[['dteday', 'cnt', 'temp', 'hum', 'windspeed']].reset_index(drop=True))
