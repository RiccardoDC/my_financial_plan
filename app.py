# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header('Ciao Eug, clicca qui sotto 🌎!')
if st.button('Balloons?'):
    st.balloons()


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def load_data(sheets_url):
    return pd.read_csv(sheets_url)


df = load_data(st.secrets["public_gsheets_url"])

# Print results.
st.write(df)

df["return with commissions"] = df["return with commissions"].str.rstrip('%').astype('float') 
df.index = df.ticker

fig, ax = plt.subplots()
ax = df.plot.bar(y = "return with commissions")
ax = ax.set_ylabel('[%]')

st.bar_chart(data = df, x = "ticker", y = "return with commissions")