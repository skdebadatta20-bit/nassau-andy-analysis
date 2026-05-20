import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Nassau Candy Distributor.csv')

df.dropna(subset=['Sales', 'Gross Profit'], inplace=True)

df = df[df['Sales'] > 0]

df['Gross_Margin_%'] = (df['Gross Profit'] / df['Sales']) * 100
df['Profit_per_Unit'] = df['Gross Profit'] / df['Units']
df['Revenue_Contribution'] = df['Sales'] / df['Sales'].sum()
df['Profit_Contribution'] = df['Gross Profit'] / df['Gross Profit'].sum()

print("✅ KPIs Done!")
print(df[['Product Name', 'Gross_Margin_%', 'Profit_per_Unit']].head(10))

df.to_csv('nassau_cleaned.csv', index=False)
print("✅ File saved!")