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
city_min = {
        'Bandung': '285 juta',
        'Bekasi': '370 juta',
        'Depok': '225 juta',
        'Jakarta Barat': '594 juta',
        'Jakarta Selatan': '335 juta',
        'Jakarta Timur': '500 juta',
        'Jakarta Utara': '451 juta',
        'Surabaya': '725 juta',
        'Tangerang': '117 juta',
        'Tangerang Selatan': '464 juta'
    }
city_max = {
        'Bandung': '87 miliar',
        'Bekasi': '93 miliar',
        'Depok': '95 miliar',
        'Jakarta Barat': '85 miliar',
        'Jakarta Selatan': '87 miliar',
        'Jakarta Timur': '99 miliar',
        'Jakarta Utara': '98 miliar',
        'Surabaya': '75 miliar',
        'Tangerang': '91 miliar',
        'Tangerang Selatan': '95 miliar'
    }
city_modus = {
        'Bandung': '3 miliar',
        'Bekasi': '2 miliar',
        'Depok': '6 miliar',
        'Jakarta Barat': '5 miliar',
        'Jakarta Selatan': '5 miliar',
        'Jakarta Timur': '1 miliar',
        'Jakarta Utara': '5 miliar',
        'Surabaya': '2,5 miliar',
        'Tangerang': '5 miliar',
        'Tangerang Selatan': '2 miliar dan 65 miliar'
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

home, dashboard, app, summary= st.tabs(['Beranda', 'Dashboard', 'Prediksi Harga Rumah', 'Ringkasan'])

with home:
    st.header('Latar Belakang')
    p1 = st.container(border=True)
    p1.write('Rumah adalah salah satu hal yang tidak dapat dipisahkan dari kehidupan manusia. Selain sebagai pemenuhan kebutuhan papan manusia, rumah beserta tanahnya merupakan salahs satu objek investasi yang menjanjikan. Layaknya jual beli barang, jual beli rumah pun sudah tersedia secara online seperti pada situs rumah123 yang menyediakan berbagai macam penawaran rumah untuk dibeli.')
    p2 = st.container(border=True)
    p2.write('Dalam praktik jual belinya, kebanyakan orang hanya menetapkan nilai dari rumah dengan sedikit aspek. Aspek yang paling sering digunakan untuk mengukur nilai suatu rumah adalah luas tanah dan luas bangunan. Namun, apakah hanya dengan melihat hal tersebut sudah cukup? Sayangnya hal tersebut tidak cukup untuk mendapatkan nilai jual yang ideal dan realistis. Oleh karena itu, diperlukan suatu alat yang dapat mengukur nilai dari suatu rumah.')
    p3 = st.container(border=True)
    p3.write('Berdasarkan situs katadata.co.id, terdapat sekitar 10,5 juta warga Indonesia tidak memiliki rumah (data dapat dilihat pada grafik di bawah). Angka ini didominasi oleh generasi milenial. Karena hal tersebut, beberapa kelompok masyarakat beranggapan bahwa generasi milenial tidak dapat mengelola keuangan dengan baik atau rumah bukanlah prioritas mereka. Namun, benarkah hal tersebut yang terjadi? Menteri Keuangan Sri Mulyani pernah mengatakan bahwa generasi milenial bukanlah tidak butuh rumah, namun harga rumahnya lebih tinggi dibanding daya beli mereka. Benarkah hal itu yang sebenarnya terjadi?')
    p3.image('Backlog_katadata.png')
    p3.write('Sumber: https://katadata.co.id/cek-data/64f5514d97595/cek-data-mengapa-milenial-sulit-punya-rumah')

with dashboard:
    st.markdown('<div style="text-align: center;"><h4>Banyak Penjualan Rumah di Kota di Indonesia</h4></div>', unsafe_allow_html=True)

    _, img, _ = st.columns([0.25, 0.5, 0.25])

    with img:
        st.image('Count_City.png')
    
    st.write('Dari data yang diekstrak, 10 kota dengan post penjualan rumah terbanyak adalah Bandung, Jakarta Selatan, Tangerang, Jakarta Timur, Jakarta Barat, Surabaya, Bekasi, Tangerang Selatan, Jakarta Utara, dan Depok. Banyak post penjualan rumah di Bandung memiliki perbedaan yang sangat signifikan dibandingkan dengan kota lain dengan banyak post penjualan rumah 175 buah')

    st.divider()

    st.markdown('<div style="text-align: center;"><h4>Sebaran Harga Rumah di Indonesia</h4></div>', unsafe_allow_html=True)
    hist_indo = alt.Chart(df).mark_bar().encode(
        x='price',
        y='count()'
    )
    st.altair_chart(hist_indo, use_container_width=True)

    st.write('Sebaran harga rumah di Indonesia berada pada rentang 117 juta hingga 99 miliar Rupiah. Meski rentangnya sangat lebar, namun kebanyakan rumah di Indonesia memiliki harga di sekitar 5 miliar Rupiah.')

    st.markdown('<div style="text-align: center;"><h4>Sebaran Harga Rumah di Daerah di Indonesia</h4></div>', unsafe_allow_html=True)
    city = st.selectbox("Kota/Kabupaten", ['Bandung', 'Bekasi', 'Depok', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Surabaya', 'Tangerang', 'Tangerang Selatan'])
    
    df_local = df[df['city']==city_dict[city]]
    hist_local = alt.Chart(df_local).mark_bar().encode(
        x='price',
        y='count()')
    st.altair_chart(hist_local, use_container_width=True)
    
    range_min = city_min[city]
    range_max = city_max[city]
    modus = city_modus[city]

    st.write(f'Layaknya pada sebaran harga rumah di Indonesia, sebaran harga rumah di {city} memiliki rentang yang lebar juga, yaitu pada rentang {range_min} hingga {range_max} Rupiah. Pada rentang tersebut, kebanyakan harga rumah di daerah {city} berada di sekitar {modus} Rupiah.')

    st.divider()

    st.markdown('<div style="text-align: center;"><h4>Banyak Post Penjualan Dengan Tag Nego</h4></div>', unsafe_allow_html=True)

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

    st.markdown('<div style="text-align: center;"><h4>Perbandingan Nominal KPR dengan UMR</h4></div>', unsafe_allow_html=True)
    kpr_desc1 = st.container()
    kpr_desc1.write('Salah satu metode untuk membeli rumah adalah dengan Kredit Pemilikan Rumah (KPR) yang merupakan sistem cicilan. Sistem cicilan ini biasanya dilakukan selama 5-30 tahun dengan besar bunga yang beragam. Hal ini tentu dapat sangat membantu seseorang untuk memiliki sebuah rumah. Namun tentu seseorang tidak dapat melupakan kebutuhan lainnya yang lebih penting daripada KPR. Banyak ahli ekonomi memberikan rekomendasi untuk memiliki cicilan bulanan yang tidak lebih dari 40% penghasilan bulanan. Dengan berpaku pada hal tersebut dan UMR daerah, maka dapat diukur apakah sebuah rumah relatif mahal atau tidak.')
    
    bar1, bar2 = st.columns(2)

    with bar1:
        city_installment1 = st.selectbox("Kolom 1", ['Indonesia','Bandung', 'Bekasi', 'Depok', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Surabaya', 'Tangerang', 'Tangerang Selatan'])

    with bar2:
        city_installment2 = st.selectbox("Kolom 2", ['Indonesia','Bandung', 'Bekasi', 'Depok', 'Jakarta Barat', 'Jakarta Selatan', 'Jakarta Timur', 'Jakarta Utara', 'Surabaya', 'Tangerang', 'Tangerang Selatan'])

    if city_installment1 == 'Indonesia':
        umr1 = 3129822
        installment1 = df['est_installment'].median()
    else:
        umr1 = df[df['city']==city_dict[city_installment1]]['city_min_wage'].median()
        installment1 = df[df['city']==city_dict[city_installment1]]['est_installment'].median()
    
    if city_installment2 == 'Indonesia':
        umr2 = 3129822
        installment2 = df['est_installment'].median()
    else:
        umr2 = df[df['city']==city_dict[city_installment2]]['city_min_wage'].median()
        installment2 = df[df['city']==city_dict[city_installment2]]['est_installment'].median()

    installment = pd.DataFrame({
        'Kategori': ['Estimasi KPR', 'UMR', '40% UMR']*2,
        'Nominal' : [installment1, umr1, 0.4*umr1, installment2, umr2, 0.4*umr2],
        'Daerah' : [city_installment1]*3 + [city_installment2]*3
    })

    install_col1, _, _ = st.columns([0.25, 0.375, 0.375])

    with install_col1:
        install_chart = alt.Chart(installment).mark_bar().encode(
            y='Nominal:Q',
            x=alt.X('Daerah:N', axis=alt.Axis(labelAngle=0, labelLimit=500)),
            column='Kategori:N',
            color='Daerah:N'
        )
        st.altair_chart(install_chart, use_container_width=True)


    kpr_desc2 = st.container()
    kpr_desc2.write('Dari semua perbandingan, baik perbandingan di Indonesia maupun di Kota/Kabupaten, besar penghasilan yang diwakili oleh nilai UMR selalu lebih kecil dibandingkan dengan estimasi KPR yang diperlukan. Hal ini menunjukkan bahwa akan terjadi kesulitan dalam pembayaran KPR untuk banyak kalangan di Indonesia. Sehingga dapat dikatakan bahwa rumah itu mahal.')
    kpr_desc2.write('Untuk dapat membeli rumah dengan metode KPR, maka penghasilan yang direkomendasikan adalah sekitar 30 juta rupiah agar seseorang dapat membayar KPR tanpa masalah. Tentu hal ini bukanlah sesuatu yang dimiliki oleh banyak orang')
    st.divider()

    st.markdown('<div style="text-align: center;"><h4>Pengaruh Beberapa Aspek yang Dimiliki Rumah Terhadap Harga Suatu Rumah', unsafe_allow_html=True)

    heat1, heat2 = st.columns(2)

    with heat1:
        st.image('Spear.png')

    with heat2:
        st.image('Kendall.png')

    corr_desc = st.container()
    corr_desc.write('Berdasarkan heatmap, dapat diketahui terdapat beberapa aspek yang mempengaruhi harga sebuah rumah. Besar pengaruh tersebut dapat dinyatakan dalam bentuk persentase konstribusi terhadap harga rumah. Berikut adalah beberapa aspek dengan persentase terbesar:')

    high_corr = ['Luas Bangunan', 'Luas Tanah', 'Banyak Kamar Tidur', 'Banyak Kamar Mandi', 'Banyak Lantai', 'UMR/Daerah']
    
    det_coef_percentage = [(0.66**2)*100, (0.63**2)*100, (0.56**2)*100, (0.54**2)*100, (0.22**2)*100, (0.18**2)*100]

    daftar = ''

    for i in range(len(high_corr)):
        daftar += '- ' + f'{high_corr[i]} ({det_coef_percentage[i]:.2f}%)' + '\n'

    st.markdown(daftar)

with app:
    model = pickle.load(open('regression_houseprice.sav', 'rb'))

    st.markdown('<div style="text-align:center"><h3>Pertambahan Harga Rumah untuk Setiap Satuan</h3></div>', unsafe_allow_html=True)

    var1, var2, var3 = st.columns(3)

    with var1:
        val=141.06
        st.metric(
            label='UMR (dalam Rupiah)',
            value=f'Rp{val:3,.2f}'
        )
    with var2:
        val=7992342.55
        st.metric(
            label='Luas Bangunan (dalam m\u00b2)',
            value=f'Rp{val:3,.2f}'
        )
    with var3:
        val=8764550.41
        st.metric(
            label='Luas Tanah  (dalam m\u00b2)',
            value=f'Rp{val:3,.2f}'
        )
    
    input1, input2, input3 = st.columns(3)

    with input1:
        city_wage = st.number_input(
            'UMR (dalam Rupiah)',
            min_value=0,
            step=1,
            value=1
        )
    with input2:
        building = st.number_input(
            'Luas Bangunan (dalam m\u00b2)',
            min_value=0,
            step=1,
            value=1
        )
    with input3:
        land = st.number_input(
            'Luas Tanah (dalam m\u00b2)',
            min_value=0,
            step=1,
        value=1
        )
    
    x=pd.DataFrame(data=[[city_wage, building, land]], columns=['city_min_wage', 'building_area', 'land_area'])
    prediksi = st.button('Prediksi')
    y_pred = 0
    if prediksi == True:
        y_pred = round(model.predict(x)[0][0], 2)

    st.metric(
            label='Estimasi Harga Rumah',
            value=f'Rp{y_pred:3,.2f}'
        )
    st.text('Akurasi prediksi ini adalah 61.45%')

    output1, output2 = st.columns(2)

    with output1:
        kpr_est = (y_pred*0.8/240)+(y_pred*0.8*0.05*20/240)
        st.metric(
            label='Estimasi KPR',
            value=f'Rp{kpr_est:3,.2f}'
        )
    st.text('20 Tahun, DP 20%, Bunga 5% Fixed Rate')
    with output2:
        salary = kpr_est/0.4
        st.metric(
            label='Rekomendasi Penghasilan',
            value=f'Rp{salary:3,.2f}'
        )
with summary:
    st.subheader('Kesimpulan')
    conc = st.container(border=True)
    conc.write('- Sebaran harga rumah di Indonesia maupun di daerah-daerahnya memiliki rentang yang sangat lebar.\n- Berdasarkan banyaknya post penjualan rumah yang menggunakan tag nego, dapat diprediksi bahwa terdapat banyak ketidaktahuan atau keraguan akan standar harga suatu rumah.\n- Di Indonesia dan di daerah-daerahnya memiliki besar KPR yang jauh lebih tinggi daripada UMR daerah tersebut. Hal ini menunjukkan tingginya ketidakmampuan masyarakat untuk memiliki sebuah rumah.\n- Terdapat beberapa aspek yang berpengaruh pada harga suatu rumah, di antaranya adalah luas bangunan, luas tanah, banyak kamar tidur serta kamar mandi, banyak lantai, dan UMR atau daerah lokasi rumah tersebut.')
    st.divider()

    st.subheader('Interpretasi Regresi Linier')
    conc = st.container(border=True)
    conc.write('- Setiap Rp1.00 UMR akan menambah nilai jual rumah sebesar Rp141.06.\n- Setiap 1 mm\u00b2 luas bangunan akan menambah nilai jual rumah sebesar Rp7,992,342.55.\n- Setiap 1 mm\u00b2 luas tanah akan menambah nilai jual rumah sebesar Rp8,764,550.41.')
    st.divider()

    st.subheader('Saran')
    adv = st.container(border=True)
    adv.write('- Gunakan lebih banyak data untuk meningkatkan akurasi model prediksi.\n- Diperlukan lebih banyak eksplorasi, feature engineering, dan mencoba model regresi lain untuk meningkatkan akurasi prediksi.')