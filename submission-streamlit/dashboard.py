import streamlit as st
from streamlit_option_menu import option_menu

# Persiapan Awal

# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# SIDEBAR SETTING
with st.sidebar :
    selected = option_menu('Dashboard Visualization',
    ['Top 5 Seller City',
    'Customer Favorite Payment',
    'Product High Sales'],
    default_index = 0)

#Import Dataset untuk semua visualisasi
all_data = pd.read_csv('all_data.csv')

# VISUALIZATION TOP 5 SELLER CITY
# create data frame visualisasi Top 5 Seller City
def create_seller_city(df) :
    by_seller_city = all_data.groupby('seller_city').seller_id.nunique().sort_values(ascending = False).reset_index().head(6)
    by_seller_city.rename(columns = {
    'seller_id' : 'city_seller_count'
    }, inplace = True)
    return by_seller_city

by_seller_city = create_seller_city(all_data) #data df

if (selected == 'Top 5 Seller City') :
    st.header('Visualization')
    st.subheader('Top 5 Seller City')

    fig_seller_city = plt.figure(figsize = (10, 5))
    plt.grid(linestyle = '--')

    sns.barplot(
    y = 'city_seller_count', 
    x = 'seller_city',
    data = by_seller_city.sort_values('city_seller_count', ascending = False).head(5),
    )

    plt.title('Top 5 Seller City', loc = "center", fontsize = 15)
    plt.ylabel(None)
    plt.xlabel('Seller City')
    plt.tick_params(axis = 'x', labelsize = 12)
    plt.show();

    st.pyplot(fig_seller_city)

#expander untuk tampilan KESIMPULAN
    with st.expander('Lihat kesimpulan'):
        st.write('\
                Berdasarkan visualisasi data diatas didapatkan jika Sao Paolo, Curitiba, Rio De Janeiro, Belo Horizonte dan Ribeiro Preto merupakan 5 kota teratas dengan jumlah seller terbanyak. Sao Paolo merupakan peringkat paling pertama.')


# VISUALIZATION CUSTOMER FAVORITE PAYMENTS
# create data frame Customer Favorite payments
def create_fav_payments(df) :
    fav_payments = all_data.groupby('payment_type').order_id.nunique().sort_values(ascending = False).reset_index()
    fav_payments.rename(columns = {
    'order_id' : 'payment_count'
    }, inplace = True)
    return fav_payments

fav_payments = create_fav_payments(all_data) #data df

if (selected == 'Customer Favorite Payment') :
    st.header('Visualization')
    st.subheader('Top Customer Favorite Payments')

    fig_fav_payment = plt.figure(figsize = (10, 5))
    plt.grid(linestyle = '--')

    sns.barplot(
        y = 'payment_count', 
        x = 'payment_type',
        data = fav_payments.sort_values('payment_count', ascending = False).head(5),
    )

    plt.title('Customer Favorite Payments', loc = "center", fontsize = 15)
    plt.ylabel(None)
    plt.xlabel('Payments')
    plt.tick_params(axis = 'x', labelsize = 12);

    st.pyplot(fig_fav_payment)

#expander untuk tampilan KESIMPULAN
    with st.expander('Lihat kesimpulan ') :
        st.write('\
                Didapatkan credit card merupakan metode pembayaran favorite para customer karna mereka paling banyak menggunakan credit card sebagai pembayaran. Dari sini bisa kita ambil peluang jika ingin meningkatkan penjualan atau menarik customer untuk berbelanja dapat dilakukannya promosi. bisa berupa potongan harga atau mendapatkan coin/point yang bisa dikumpulkan dan ditukarkan kemudian hari jika pembayaran menggunakan credit card.')


# VISUALIZATION HIGH SALES PRODUCT
# create data frame High Sales Product
def create_high_sales(df) :
    high_sales = all_data.groupby('product_category_name').price.nunique().sort_values(ascending = False).reset_index().head(10)
    high_sales.rename(columns = {
    'price' : 'price_total'
    }, inplace = True)
    return high_sales

high_sales = create_high_sales(all_data) #data df

if (selected == 'Product High Sales') :
    st.header('Visualization')
    st.subheader('Top Product High Sales')

    fig_high_sales = plt.figure(figsize = (10,5))
    plt.grid(linestyle = '--')

    sns.barplot(
        y = 'price_total',
        x = 'product_category_name',
        data = high_sales.sort_values('product_category_name', ascending = True).head(10)
    )

    plt.title('High Sales Product', loc = "center", fontsize = 15)
    plt.ylabel(None)
    plt.xlabel('Product')
    plt.tick_params(axis = 'x', labelsize = 10, rotation = 45);

    st.pyplot(fig_high_sales)

#expander untuk tampilan KESIMPULAN
    with st.expander('Lihat kesimpulan   ') :
        st.write('\
                Dari hasil visualisasi diatas didapatkan 10 high sales product. 3 produk dengan penjualan paling tinggi ialah beleza_saude, esporte_lazer dan utilidades_domesticas.Jadi para seller bisa meningkatkan quantity kepada produk dengan penjualan teratas agar bisa memenuhi permintaan pembelian customer dan bisa mendapatkan peluang meningkatkan pemasukan dengan penjualan yang meningkat juga. Para seller juga dapat melakukan banyak promosi seperti diskon atau pembelian paket terhadap produk dengan sales teratas agar dapat memancing minat customer.')