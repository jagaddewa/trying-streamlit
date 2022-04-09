import pandas as pd
import numpy as np
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import locale
locale.setlocale(locale.LC_ALL, 'en_US')


#Buka file
file_csv="test.csv"
df=pd.read_csv(file_csv)
df=df.astype({'Sales':'int64','Profit':'int64','Assets':'int64','Market Value':'int64'}).drop(columns=['Rank'])
pd.set_option('display.float_format',lambda x: '%.2f' % x)
df.index=df.index+1


df_country=df[['Country']]
df_sort_country_count=df_country.value_counts().sort_index(ascending=False).sort_values(ascending=False).reset_index(name="Total")
df_sort_country_count.index=df_sort_country_count.index+1

with st.container():
    st.title('Merasakan Mengolah Data: Sebuah Pengalaman Data Analyst/Data Science')
    st.subheader('Daftar Perusahaan Global Top 2000 tahun 2021 Menurut Forbes')
    st.dataframe(df)
    st.write('Berikut ini adalah daftar perusahaan top global 2000 di tahun 2021 menurut Forbes. Rincian data-data di atas terdiri dari kolom Sales, kolom Profit, kolom Assets, dan kolom Market Value. Semua kolom di atas menggunakan mata uang USD/US$/Dollar Amerika Serikat.')
    txt_url="https://www.kaggle.com/datasets/shivamb/fortune-global-2000-companies-till-2021"
    txt_url_2="https://www.forbes.com/lists/global2000/"
    st.write('Data di atas bersumber dari',txt_url_2,'diolah menjadi data ini:',txt_url,'. Yang selanjutnya saya olah kembali dengan mengubahnya mnejadi angka yang bisa dihitung rata-ratanya.')
    
    
    df_2=df.copy()
    kolom=df_2.drop(columns=['Name','Country'])
    
    st.write("")
    st.write("")
    
    
    option=st.selectbox('Pilih kolom mana yang mau dihitung rata-ratanya',kolom.columns,key="1")
    
    if option == "Sales":
        
        st.write('Anda memilih **Sales** untuk dibandingkan')        
        df_average_sales=df[['Country','Sales']].groupby("Country").mean().rename(columns={"Sales":"Sales (USD)"}).reset_index()
        df_average_sales.index=df_average_sales.index+1
        option_avg_sales=st.multiselect("Pilih negara yang mau dibandingkan rata-rata Sales-nya",df_average_sales,key="2")
       
        if len(option_avg_sales)>=2 and len(option_avg_sales)<=5: 
            average_country_sales=df_average_sales.copy()
            sales_country=average_country_sales.set_index('Country')
            sales_country=sales_country.loc[option_avg_sales]
                    
            fig,ax=plt.subplots()
            plt.bar(x=option_avg_sales,height=sales_country["Sales (USD)"])
            ax.get_yaxis().set_major_formatter(tick.FuncFormatter(lambda x,p:format(int(x),',')))
            ax.set_xlabel("Countries",loc='center')
            ax.set_ylabel("Sales (USD)", loc='center')
            st.pyplot(fig)
            
            st.write('Anda memilih {0} negara'.format(len(option_avg_sales)))
            
            for x in sales_country:
                st.write(sales_country[x].round(2))
                
                sales_country_2=sales_country.copy().reset_index()
                
                max_value=sales_country_2.max()
                min_value=sales_country_2.min()
                
                st.write('Sales tertinggi pada perbandingan ini: {0} - **{1}** '.format(locale.currency(max_value['Sales (USD)'],grouping=True),sales_country_2.loc[sales_country_2['Sales (USD)']==sales_country_2['Sales (USD)'].max(),'Country'].values[0]))
                st.write('Sales terendah pada perbandingan ini: {0} - **{1}**'.format(locale.currency(min_value['Sales (USD)'],grouping=True),sales_country_2.loc[sales_country_2['Sales (USD)']==sales_country_2['Sales (USD)'].min(),'Country'].values[0]))
                
                selisih_sales=max_value['Sales (USD)']-min_value['Sales (USD)']
                
                st.write('Selisih didapat antara Sales tertinggi dan terendah adalah **{0}**'.format(locale.currency(selisih_sales,grouping=True)))
                
        elif len(option_avg_sales)>5:
            st.error('Anda tidak bisa memilih lebih dari 5 negara')
    
    if option == "Profit":
        st.write('Anda memilih **Profit** untuk dibandingkan')
        df_average_profit=df[['Country','Profit']].groupby("Country").mean().rename(columns={"Profit":"Profit (USD)"}).reset_index()
        df_average_profit.index=df_average_profit.index+1
        df_average_profit.astype({'Profit (USD)':'int64'})
        
        option_avg_profit=st.multiselect("Pilih negara yang mau dibandingkan rata-rata Profit-nya",df_average_profit,key="3")
        
        if len(option_avg_profit)>=2 and len(option_avg_profit)<=5:
            average_country_profit=df_average_profit.copy()
            profit_country=average_country_profit.set_index('Country')
            profit_country=profit_country.loc[option_avg_profit]
            
            fig,ax=plt.subplots()
            plt.bar(x=option_avg_profit,height=profit_country["Profit (USD)"])
            ax.get_yaxis().set_major_formatter(tick.FuncFormatter(lambda x,p:format(int(x),',')))
            ax.set_xlabel("Countries",loc='center')
            ax.set_ylabel("Profit (USD)", loc='center')
            st.pyplot(fig)
            
            st.write('Anda memilih {0} negara'.format(len(option_avg_profit)))
            
            for x in profit_country:
                st.write(profit_country[x].round(2))
                
                profit_country_2=profit_country.copy().reset_index()
                
                max_value=profit_country_2.max()
                min_value=profit_country_2.min()
                
                st.write('Profit tertinggi pada perbandingan ini: {0} - **{1}** '.format(locale.currency(max_value['Profit (USD)'],grouping=True),profit_country_2.loc[profit_country_2['Profit (USD)']==profit_country_2['Profit (USD)'].max(),'Country'].values[0]))
                st.write('Profit terendah pada perbandingan ini: {0} - **{1}**'.format(locale.currency(min_value['Profit (USD)'],grouping=True),profit_country_2.loc[profit_country_2['Profit (USD)']==profit_country_2['Profit (USD)'].min(),'Country'].values[0]))
                
                selisih_profit=max_value['Profit (USD)']-min_value['Profit (USD)']
                st.write('Selisih didapat antara Profit tertinggi dan terendah adalah **{0}**'.format(locale.currency(selisih_profit,grouping=True)))
            
        
        elif len(option_avg_profit)>5:
            st.error('Anda tidak bisa memilih lebih dari 5 negara')
    
    if option == "Assets":
        st.write('Anda memilih **Assets** untuk dibandingkan')
        df_average_assets=df[['Country','Assets']].groupby("Country").mean().rename(columns={"Assets":"Assets (USD)"}).reset_index()
        df_average_assets.index=df_average_assets.index+1
        df_average_assets.astype({'Assets (USD)':'int64'})
        
        option_avg_assets=st.multiselect("Pilih negara yang mau dibandingkan rata-rata Assets-nya",df_average_assets,key="4")
        
        if len(option_avg_assets)>=2 and len(option_avg_assets)<=5: 
            average_country_assets=df_average_assets.copy()
            assets_country=average_country_assets.set_index('Country')
            assets_country=assets_country.loc[option_avg_assets]
            
            fig,ax=plt.subplots()
            plt.bar(x=option_avg_assets,height=assets_country["Assets (USD)"])
            ax.get_yaxis().set_major_formatter(tick.FuncFormatter(lambda x,p:format(int(x),',')))
            ax.set_xlabel("Countries",loc='center')
            ax.set_ylabel("Assets (USD)", loc='center')
            st.pyplot(fig)
            
            for x in assets_country:
                st.write(assets_country[x].round(2))
                
                assets_country_2=assets_country.copy().reset_index()
                
                max_value=assets_country_2.max()
                min_value=assets_country_2.min()
                
                st.write('Assets tertinggi pada perbandingan ini: {0} - **{1}** '.format(locale.currency(max_value['Assets (USD)'],grouping=True),assets_country_2.loc[assets_country_2['Assets (USD)']==assets_country_2['Assets (USD)'].max(),'Country'].values[0]))
                st.write('Assets terendah pada perbandingan ini: {0} - **{1}**'.format(locale.currency(min_value['Assets (USD)'],grouping=True),assets_country_2.loc[assets_country_2['Assets (USD)']==assets_country_2['Assets (USD)'].min(),'Country'].values[0]))
                
                selisih_assets=max_value['Assets (USD)']-min_value['Assets (USD)']
                st.write('Selisih didapat antara Sales tertinggi dan terendah adalah **{0}**'.format(locale.currency(selisih_assets,grouping=True)))
            
        elif len(option_avg_assets)>5:
            st.error('Anda tidak bisa memilih lebih dari 5 negara')
    
    if option == 'Market Value':
        st.write('Anda memilih **Market Value** untuk dibandingkan')
        df_average_marval=df[['Country','Market Value']].groupby("Country").mean().rename(columns={"Market Value":"Market Value (USD)"}).reset_index()
        df_average_marval.index=df_average_marval.index+1
        df_average_marval.astype({'Market Value (USD)':'int64'})
        
        option_avg_marval=st.multiselect("Pilih negara yang mau dibandingkan rata-rata Market Value-nya",df_average_marval,key="5")
        
        if len(option_avg_marval)>=2 and len(option_avg_marval)<=5:
            average_country_marval=df_average_marval.copy()
            marval_country=average_country_marval.set_index('Country')
            marval_country=marval_country.loc[option_avg_marval]
            
            fig,ax=plt.subplots()
            plt.bar(x=option_avg_marval,height=marval_country["Market Value (USD)"])
            ax.get_yaxis().set_major_formatter(tick.FuncFormatter(lambda x,p:format(int(x),',')))
            ax.set_xlabel("Countries",loc='center')
            ax.set_ylabel("Market Value (USD)", loc='center')
            st.pyplot(fig)
            
            for x in marval_country:
                st.write(marval_country[x].round(2))
                
                marval_country_2=marval_country.copy().reset_index()
                
                max_value=marval_country_2.max()
                min_value=marval_country_2.min()
                
                st.write('Assets tertinggi pada perbandingan ini: {0} - **{1}** '.format(locale.currency(max_value['Market Value (USD)'],grouping=True),marval_country_2.loc[marval_country_2['Market Value (USD)']==marval_country_2['Market Value (USD)'].max(),'Country'].values[0]))
                st.write('Assets terendah pada perbandingan ini: {0} - **{1}**'.format(locale.currency(min_value['Market Value (USD)'],grouping=True),marval_country_2.loc[marval_country_2['Market Value (USD)']==marval_country_2['Market Value (USD)'].min(),'Country'].values[0]))
                
                selisih_marval=max_value['Market Value (USD)']-min_value['Market Value (USD)']
                st.write('Selisih didapat antara Market Value tertinggi dan terendah adalah **{0}**'.format(locale.currency(selisih_marval,grouping=True)))
            
        elif len(option_avg_marval)>5:
            st.error('Anda tidak bisa memilih lebih dari 5 negara')
