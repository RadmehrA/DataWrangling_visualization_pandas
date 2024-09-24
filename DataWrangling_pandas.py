{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import matplotlib.pyplot as plt\
import seaborn as sns\
\
# Load OpenAQ Air Quality Data\
df = pd.read_csv('openaq_data.csv')  # Download and rename your file accordingly\
\
# Data Cleaning: Handle Missing Values\
df.fillna(df.mean(), inplace=True)\
\
# Data Analysis: Average Air Quality by City\
city_avg = df.groupby('city')['air_quality_index'].mean().reset_index()\
\
# Visualization: Average Air Quality by City\
plt.figure(figsize=(10,6))\
sns.barplot(data=city_avg, x='city', y='air_quality_index')\
plt.title('Average Air Quality Index by City')\
plt.xticks(rotation=45)\
plt.show()\
}