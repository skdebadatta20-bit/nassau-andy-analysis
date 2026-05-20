import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")

# Load Data
df = pd.read_csv('nassau_cleaned.csv')

# KPIs
df['Gross_Margin_%'] = (df['Gross Profit'] / df['Sales']) * 100
df['Profit_per_Unit'] = df['Gross Profit'] / df['Units']

st.title("🍬 Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Analysis")

# Top KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Gross Profit'].sum():,.0f}")
col3.metric("Avg Margin", f"{df['Gross_Margin_%'].mean():.1f}%")
col4.metric("Total Products", df['Product Name'].nunique())

st.divider()

# Chart 1 - Margin by Product
st.subheader("📊 Gross Margin by Product")
fig1 = px.bar(
    df.groupby('Product Name')['Gross_Margin_%'].mean().reset_index(),
    x='Product Name', y='Gross_Margin_%',
    color='Gross_Margin_%', color_continuous_scale='Greens'
)
st.plotly_chart(fig1, use_container_width=True)

# Chart 2 - Division Performance
st.subheader("🏭 Revenue vs Profit by Division")
div = df.groupby('Division')[['Sales','Gross Profit']].sum().reset_index()
fig2 = px.bar(div, x='Division', y=['Sales','Gross Profit'], barmode='group')
st.plotly_chart(fig2, use_container_width=True)

# Chart 3 - Profit Contribution
st.subheader("🥧 Profit Contribution by Product")
fig3 = px.pie(
    df.groupby('Product Name')['Gross Profit'].sum().reset_index(),
    names='Product Name', values='Gross Profit'
)
st.plotly_chart(fig3, use_container_width=True)

# Data Table
st.subheader("📋 Full Data")
st.dataframe(df)