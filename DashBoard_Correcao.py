import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout = 'wide')
df = pd.read_csv('supermarket_sales.csv',sep=';',decimal = ',')


#Organizando o dataFrame
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by = ['Date'])
df['Mes'] = df['Date'].apply(lambda x:str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox("Mês",df['Mes'].unique())

#Filtrando por mes
df_filtered = df[df["Mes"] == month]
#df_filtered

#Criando espacos pros gráficos/Ele cria de acordo como ele encontra
col1,col2 = st.columns(2)
col3,col4,col5 = st.columns(3)

#Criando gráficos --
#Faturamento
fig_date = px.bar(df_filtered, x ='Date', y= 'Total',color = 'City',title='Faturamento por dia por unidade')
col1.plotly_chart(fig_date,use_container_width = True)

#Tipo de produto
fig_type = px.bar(df_filtered,x = 'Date',y='Product line',color = 'City',title ='Faturamento por tipo de produto',
                  orientation = 'h')
col2.plotly_chart(fig_type,use_container_width = True)


#Contribuição por filial  
city_total = df_filtered.groupby('City')['Total'].sum().reset_index()
fig_city = px.bar(city_total,x = 'City',y='Total',title ='Faturamento por filial')
col3.plotly_chart(fig_city,use_container_width = True)

#Criando um gráfico do tipo pie
pie = px.pie(df_filtered,values = 'Total',names ='Payment',title ='Faturamento por tipo de pagamento')
col4.plotly_chart(pie,use_container_width = True)

#Avaliacao Media por cidade
rating_city = df_filtered.groupby('City')['Rating'].mean().reset_index()
r = px.bar(rating_city, x = 'Rating',y = 'City',title = 'Avaliação por cidade')
col5.plotly_chart(r,use_container_width = True)
##WARNINGS -> PESQUISAR O RESET INDEX E A FUNCAO LAMBDA
