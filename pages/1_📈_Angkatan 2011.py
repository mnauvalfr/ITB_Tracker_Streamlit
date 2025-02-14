import streamlit as st
import pandas as pd
import plotly.express as px

#title
st.title("Angkatan 2011")
st.write("Data Angkatan Tahun 2011 (Tahun Survey 2018)", st.session_state["Fakultas"], "Prodi", st.session_state["Jurusan"])

#read data responden
df = pd.read_excel(
    io= "Data responden 2018-2022.xlsx",
    engine="openpyxl",
    sheet_name="sarjana_2018_ ang.2011",
    usecols="A:I",
    nrows=50,
)

#filter dataframe
selected_major = st.session_state["Jurusan"]
filtered_data = df[df['PRODI'] == selected_major]
row = df[df['PRODI'] == selected_major].index[0]
N = df["Status Pengisian Kuesioner"][row]
Total = df["Total Alumni (N)"][row]
N_persen = round(df["%"][row]*100)

#show
st.subheader("Data Responden")
st.write("Yang telah mengisi kuisioner: ", N)
st.write("Total alumni: ", Total)
st.write("Persentase data responden: ", N_persen,"%")
st.dataframe(filtered_data)




