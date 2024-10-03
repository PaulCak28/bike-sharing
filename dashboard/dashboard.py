import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def get_total_count_by_hour_df(hour_df):
    hour_count_df =  hour_df.groupby(by="hours").agg({"count_cr": ["sum"]})
    return hour_count_df

def count_by_day_df(day_df):
    day_df_count_2011 = day_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011

def total_registered_df(day_df):
   reg_df =  day_df.groupby(by="dteday").agg({
      "registered": "sum"
    })
   reg_df = reg_df.reset_index()
   reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return reg_df

def total_casual_df(day_df):
   cas_df =  day_df.groupby(by="dteday").agg({
      "casual": ["sum"]
    })
   cas_df = cas_df.reset_index()
   cas_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return cas_df

def sum_order (hour_df):
    sum_order_items_df = hour_df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df


days_df = pd.read_csv("day.csv")
hours_df = pd.read_csv("hour.csv")

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

min_date_hour = hours_df["dteday"].min()
max_date_hour = hours_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQG2X9OxyrhWL2BXMg2_1ujwjrxv18jCPkAjQ&s")
    
        # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])
  
main_df_days = days_df[(days_df["dteday"] >= str(start_date)) & 
                       (days_df["dteday"] <= str(end_date))]

main_df_hour = hours_df[(hours_df["dteday"] >= str(start_date)) & 
                        (hours_df["dteday"] <= str(end_date))]

hour_count_df = get_total_count_by_hour_df(main_df_hour)
day_df_count_2011 = count_by_day_df(main_df_days)
reg_df = total_registered_df(main_df_days)
cas_df = total_casual_df(main_df_days)
sum_order_items_df = sum_order(main_df_hour)

#Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.header('Bike Sharing :sparkles:')

st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_df_count_2011.count_cr.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = reg_df.register_sum.sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = cas_df.casual_sum.sum()
    st.metric("Total Casual", value=total_sum)

st.subheader("Performa penjualan perusahaan dalam beberapa tahun terakhir")

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    days_df["dteday"],
    days_df["count_cr"],
    marker='*', 
    linewidth=2,
    color="#D95319"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("pada jam berapa yang paling banyak dan paling sedikit disewa?")
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(35, 15))

# Visualisasi jam-jam dengan penyewaan tertinggi
top_hours = sum_order_items_df.head(5)
sns.barplot(x="hours", y="count_cr", data=top_hours, palette="YlOrRd", ax=ax_left)
ax_left.set_ylabel("")
ax_left.set_xlabel("Jam (PM)", fontsize=25)
ax_left.set_title("Periode dengan Penyewaan Sepeda Tertinggi", fontsize=35)
ax_left.tick_params(axis='both', labelsize=30)
ax_left.tick_params(axis='x', labelsize=25)

# Visualisasi jam-jam dengan penyewaan terendah
bottom_hours = sum_order_items_df.sort_values(by="hours").head(5)
sns.barplot(x="hours", y="count_cr", data=bottom_hours, palette="YlOrRd", ax=ax_right)
ax_right.set_ylabel("")
ax_right.set_xlabel("Jam (AM)", fontsize=25)
ax_right.set_title("Periode dengan Penyewaan Sepeda Terendah", fontsize=35)
ax_right.invert_xaxis()
ax_right.yaxis.set_label_position("right")
ax_right.yaxis.tick_right()
ax_right.tick_params(axis='both', labelsize=30)
ax_right.tick_params(axis='x', labelsize=25)

st.pyplot(fig)
st.subheader("Pada musim apa yang paling banyak disewa?")

colors = "YlOrRd"
fig, ax = plt.subplots(figsize=(35, 15))
sns.barplot(
        y="count_cr", 
        x="season",
        data=days_df,
        palette=colors,
        ax=ax
    )
ax.set_title("Jumlah Pengguna Sepeda berdasarkan Kondisi Musim", loc="center", fontsize=30)
ax.set_ylabel('Kondisi Musim',fontsize=20)
ax.set_xlabel('Jumlah Pengguna Sepeda',fontsize=20)
ax.tick_params(axis='x', labelsize=25,)
ax.tick_params(axis='y', labelsize=25,)
st.pyplot(fig)

st.subheader("Pada cuaca apa yang paling banyak disewa?")

colors = "YlOrRd"
fig, ax = plt.subplots(figsize=(35, 15))
sns.barplot(
        y="count_cr", 
        x="weather_situation",
        data=days_df,
        palette=colors,
        ax=ax
    )
ax.set_title("Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca", loc="center", fontsize=30)
ax.set_ylabel('Kondisi Cuaca',fontsize=20)
ax.set_xlabel('Jumlah Pengguna Sepeda',fontsize=20)
ax.tick_params(axis='x', labelsize=25,)
ax.tick_params(axis='y', labelsize=30,)
st.pyplot(fig)

st.caption('Copyright © Paulus Simon Haloman Sigalingging 2024')