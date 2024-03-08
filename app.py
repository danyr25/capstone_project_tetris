import streamlit as st
import pandas as pd
import pickle
import altair as alt
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title='Rumah Itu Mahal, Emang Iya?',
    layout='wide',
    initial_sidebar_state='expanded')

df = pd.read_csv('https://drive.usercontent.google.com/download?id=1mLztUISLkt7Ar94biHO1To4yEAWotBzv&export=download&authuser=2&confirm=t&uuid=4984e942-e4c1-411e-a255-01d986b2d0f7&at=APZUnTV0ivDs0uSNFPWkyDXGkoTX:1709878413817')

city_dict = {
        'Bandung': 'bandung',
        'Bekasi': 'bekasi',
        'Depok': 'depok',
        'Jakarta Barat': 'jakarta barat',
        'Jakarta Selatan': 'jakarta selatan',
        'Jakarta Timur': 'jakarta timur',
        'Jakarta Utara': 'jakarta utara',
        'Surabaya': 'surabaya',
        'Tangerang': 'tangerang',
        'Tangerang Selatan': 'tangerang selatan'
    }

with st.sidebar:
    st.title('Rumah Itu Mahal, Emang Iya?')
    st.caption('Dibuat oleh Dany Rahman')
    st.image('https://i0.wp.com/www.emporioarchitect.com/upload/portofolio/1280/desain-rumah-klasik-2-lantai-18180122-44542826230922123843.jpg')
    with st.expander('Disclaimer'):
        text = 'Data yang digunakan pada app ini adalah 810 data yang diekstrak dari situs rumah123.com'

        st.write(text)
    with st.expander('Contact'):
        st.write('danyrahman1225@gmail.com')
        st.write('https://www.linkedin.com/in/dany-rahman-8bba0723b/')
        st.write('https://github.com/danyr25/')

home, dashboard, app= st.tabs(['Beranda', 'Dashboard', 'App'])

with home:
    st.header('Latar Belakang')
    p1 = st.container(border=True)
    p1.write('Rumah adalah salah satu hal yang tidak dapat dipisahkan dari kehidupan manusia. Selain sebagai pemenuhan kebutuhan papan manusia, rumah beserta tanahnya merupakan salahs satu objek investasi yang menjanjikan. Layaknya jual beli barang, jual beli rumah pun sudah tersedia secara online seperti pada situs rumah123 yang menyediakan berbagai macam penawaran rumah untuk dibeli.')
    p2 = st.container(border=True)
    p2.write('Dalam praktik jual belinya, kebanyakan orang hanya menetapkan nilai dari rumah dengan sedikit aspek. Aspek yang paling sering digunakan untuk mengukur nilai suatu rumah adalah luas tanah dan luas bangunan. Namun, apakah hanya dengan melihat hal tersebut sudah cukup? Sayangnya hal tersebut tidak cukup untuk mendapatkan nilai jual yang ideal dan realistis. Oleh karena itu, diperlukan suatu alat yang dapat mengukur nilai dari suatu rumah.')
    p3 = st.container(border=True)
    p3.write('Meski memang rumah atau tanah merupakan suatu kebutuhan dan objek investasi yang menjanjikan, namun apakah seseorang dapat memilikinya tanpa kesulitan? Dengan memiliki aset sebuah rumah memang memiliki banyak nilai positif, namun apakah rumah dapat dimiliki sembari memenuhi kebutuhan lainnya?')

with dashboard:
    st.subheader('Banyak Penjualan Rumah di Kota di Indonesia')
    st.image('Count_City.png')
    st.divider()

    st.subheader('Sebaran Harga Rumah di Indonesia')
    hist_indo = alt.Chart(df).mark_bar().encode(
        x='price',
        y='count()'
    )
    st.altair_chart(hist_indo, use_container_width=True)
    st.subheader('Sebaran Harga Rumah di Daerah di Indonesia')
    city = st.selectbox("Kota/Kabupaten", ['Bandung', 'Bekasi', 'Depok', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Surabaya', 'Tangerang', 'Tangerang Selatan'])

    df_local = df[df['city']==city_dict[city]]
    hist_local = alt.Chart(df_local).mark_bar().encode(
        x='price',
        y='count()')
    st.altair_chart(hist_local, use_container_width=True)
    st.divider()

    st.subheader('Banyak Post Penjualan Dengan Tag Nego')

    df['negotiable'] = df['negotiable'].replace([0, 1], ['Tidak', 'Ya'])

    col1, col2 = st.columns(2)

    with col1:
        nego_count = alt.Chart(df).mark_bar().encode(
            x='negotiable',
            y='count()')
        st.altair_chart(nego_count, use_container_width=True)
    with col2:
        interpret_nego = st.container()
        interpret_nego.write('Terlihat terdapat banyak sekali post penjualan yang menawarkan proses negosiasi. Hal ini dapat menunjukkan usaha penjual untuk menarik pembeli dengan tag nego ataupun dapat menunjukkan keraguan penjual dalam memberikan nilai pada rumah yang dijual sehingga ingin mendahulukan proses diskusi dengan pembeli untuk menentukan nilai jual dari rumah tersebut.')
    st.divider()

    st.subheader('Perbandingan Nominal KPR dengan UMR')
    kpr_desc1 = st.container()
    kpr_desc1.write('Salah satu metode untuk membeli rumah adalah dengan Kredit Pemilikan Rumah (KPR) yang merupakan sistem cicilan. Sistem cicilan ini biasanya dilakukan selama 5-30 tahun dengan besar bunga yang beragam. Hal ini tentu dapat sangat membantu seseorang untuk memiliki sebuah rumah. Namun tentu seseorang tidak dapat melupakan kebutuhan lainnya yang lebih penting daripada KPR. Banyak ahli ekonomi memberikan rekomendasi untuk memiliki cicilan bulanan yang tidak lebih dari 40% penghasilan bulanan. Dengan berpaku pada hal tersebut dan UMR daerah, maka dapat diukur apakah sebuah rumah relatif mahal atau tidak.')

    bar1, bar2 = st.columns(2)

    with bar1:
        st.subheader('Indonesia')

        umr_indo = 3129822
        med_installment_indo = df['est_installment'].median()

        installment_indo = pd.DataFrame({
            'Kategori': ['Estimasi KPR', 'UMR', '40% UMR'],
            'Nominal' : [med_installment_indo, umr_indo, 0.4*umr_indo]
        })

        install_chart_indo = alt.Chart(installment_indo).mark_bar().encode(
            x='Kategori:N',
            y='Nominal:Q')
        st.altair_chart(install_chart_indo, use_container_width=True)

    with bar2:
        st.subheader('Kota/Kabupaten')

        city_installment = st.selectbox("Kabupaten/Kota", ['Bandung', 'Bekasi', 'Depok', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Surabaya', 'Tangerang', 'Tangerang Selatan'])

        umr_local = df[df['city']==city_dict[city_installment]]['city_min_wage'].median()
        med_installment_local = df[df['city']==city_dict[city_installment]]['est_installment'].median()

        installment_local = pd.DataFrame({
            'Kategori': ['Estimasi KPR', 'UMR', '40% UMR'],
            'Nominal' : [med_installment_local, umr_local, 0.4*umr_local]
        })

        install_chart_local = alt.Chart(installment_local).mark_bar().encode(
            x='Kategori:N',
            y='Nominal:Q')
        st.altair_chart(install_chart_local, use_container_width=True)
    kpr_desc2 = st.container()
    kpr_desc2.write('Dari semua perbandingan, baik perbandingan di Indonesia maupun di Kota/Kabupaten, besar penghasilan yang diwakili oleh nilai UMR selalu lebih kecil dibandingkan dengan estimasi KPR yang diperlukan. Hal ini menunjukkan bahwa akan terjadi kesulitan dalam pembayaran KPR untuk banyak kalangan di Indonesia. Sehingga dapat dikatakan bahwa rumah itu mahal.')
    kpr_desc2.write('Untuk dapat membeli rumah dengan metode KPR, maka penghasilan yang direkomendasikan adalah sekitar 30 juta rupiah agar seseorang dapat membayar KPR tanpa masalah. Tentu hal ini bukanlah sesuatu yang dimiliki oleh banyak orang')
    st.divider()

    st.subheader('Pengaruh Beberapa Aspek yang Dimiliki Rumah Terhadap Harga Suatu Rumah')

    heat1, heat2 = st.columns(2)

    with heat1:
        st.image('Spear.png')

    with heat2:
        st.image('Kendall.png')

    corr_desc = st.container()
    corr_desc.write('Berdasarkan heatmap, dapat diketahui bahwa beberapa aspek yang berpengaruh besar terhadap nilai jual suatu rumah adalah sebagai berikut:')

    high_corr = ['Luas Bangunan', 'Luas Tanah', 'Banyak Kamar Tidur', 'Banyak Kamar Mandi', 'Banyak Lantai', 'UMR/Daerah']
    
    daftar = ''

    for i in high_corr:
        daftar += '- '+ i + '\n'

    st.markdown(daftar)

with app:
    model = pickle.load(open('regression_houseprice.sav', 'rb'))

    app_desc1 = st.container()
    app_desc1.write('App ini dibuat dengan menggunakan regresi linear')

    st.subheader('Pertambahan Harga Rumah untuk Setiap Satuan')

    var1, var2 = st.columns(2)
    var3, var4 = st.columns(2)

    with var1:
        val=815.00
        st.metric(
            label='UMR',
            value=f'Rp{val:3,.2f}'
        )
    with var2:
        val=1744134492.92
        st.metric(
            label='Banyak Lantai',
            value=f'Rp{val:3,.2f}'
        )
    with var3:
        val=5641025.96
        st.metric(
            label='Luas Bangunan',
            value=f'Rp{val:3,.2f}'
        )
    with var4:
        val=325380095.10
        st.metric(
            label='Carport',
            value=f'Rp{val:3,.2f}'
        )
    
    input1, input2 = st.columns(2)
    input3, input4 = st.columns(2)

    with input1:
        city_wage = st.number_input(
            'UMR',
            min_value=0,
            step=1,
            value=1
        )
    with input2:
        floor_count = st.number_input(
            'Banyak Lantai',
            min_value=0,
            step=1,
            value=1
        )
    with input3:
        building_area = st.number_input(
            'Luas Bangunan',
            min_value=0,
            step=1,
        value=1
        )
    with input4:
        carport = st.number_input(
            'Carport',
            min_value=0,
            step=1,
            value=1
        )
    x=pd.DataFrame(data=[[city_wage, floor_count, building_area, carport]], columns=['city_min_wage', 'floor_count', 'building_area', 'carport'])
    prediksi = st.button('Prediksi')
    y_pred = 0
    if prediksi == True:
        y_pred = round(model.predict(x)[0][0], 2)

    st.metric(
            label='Estimasi Harga Rumah',
            value=f'Rp{y_pred:3,.2f}'
        )
    
    # output1, output2, output3 = st.columns(3)

    # with output1:
    #     st.metric(
    #         label='Estimasi Harga Rumah',
    #         value=f'Rp{y:3,.2f}'
    #     )
    # with output2:
        
    #     st.metric(
    #         label='Estimasi KPR (20 Tahun, Bunga 7,5%)',
    #         value=f'Rp{val:3,.2f}'
    #     )
    # with output3:
    #     st.metric(
    #         label='Rekomendasi Penghasilan',
    #         value=f'Rp{val:3,.2f}'
    #     )
