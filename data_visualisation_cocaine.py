# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:18:48 2021

@author: sujit
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import stats
from scipy.stats import norm, skew
import numpy as np
merged = pd.read_csv('cocaine.csv', sep=',')
unaffectedsection = merged['unaffectedsection']
merged = merged.drop(['unaffectedsection', 'unaffectedsection1', 'unaffectedsection2', 'unaffectedsection3', 'unaffectedsection4', 'unaffectedsection5'], axis = 1)
merged_new = merged.apply(lambda x: np.log1p(x) if np.issubdtype(x.dtype, np.number) else x)

merged_new = merged
merged_new['unaffectedsection'] = unaffectedsection

nodye = merged_new[merged_new['unaffectedsection'] == 12]
af_section1 = merged_new[merged_new['unaffectedsection'] == 0]
un_section1 = merged_new[merged_new['unaffectedsection'] == 1]
un_section1_2 = merged_new[merged_new['unaffectedsection'] == 2]
un_section1_3 = merged_new[merged_new['unaffectedsection'] == 3]
un_section1_4 = merged_new[merged_new['unaffectedsection'] == 4]
un_section1_5 = merged_new[merged_new['unaffectedsection'] == 5]
un_section1_6 = merged_new[merged_new['unaffectedsection'] == 6]

"""-------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------"""

""" data description of no dye at all in all hair length removing the zeroes"""
#section1
df_nodye_nozeroes_s1 = pd.DataFrame()
df_nodye_nozeroes_s1 = nodye[nodye['value']!= 0]
df_nodye_nozeroes_s1['value'].describe()

df_nodye_nozeroes_s2 = pd.DataFrame()
df_nodye_nozeroes_s2 = nodye[nodye['value1']!= 0]
df_nodye_nozeroes_s2= df_nodye_nozeroes_s2.value1.dropna()
df_nodye_nozeroes_s2.describe()


df_nodye_nozeroes_s3 = pd.DataFrame()
df_nodye_nozeroes_s3 = nodye[nodye['value2']!= 0]
df_nodye_nozeroes_s3= df_nodye_nozeroes_s3.value2.dropna()
df_nodye_nozeroes_s3.describe()


df_nodye_nozeroes_s4 = pd.DataFrame()
df_nodye_nozeroes_s4 = nodye[nodye['value3']!= 0]
df_nodye_nozeroes_s4= df_nodye_nozeroes_s4.value3.dropna()
df_nodye_nozeroes_s4.describe()

df_nodye_nozeroes_s5 = pd.DataFrame()
df_nodye_nozeroes_s5 = nodye[nodye['value4']!= 0]
df_nodye_nozeroes_s5= df_nodye_nozeroes_s5.value4.dropna()
df_nodye_nozeroes_s5.describe()

df_nodye_nozeroes_s6 = pd.DataFrame()
df_nodye_nozeroes_s6 = nodye[nodye['value5']!= 0]
df_nodye_nozeroes_s6= df_nodye_nozeroes_s6.value5.dropna()
df_nodye_nozeroes_s6.describe()

"""-------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------"""

""" data description of dye in specific section 1 in and no dye in specific section at all in all hair length removing the zeroes"""

df_dye_nozeroes_s1 = pd.DataFrame()
df_dye_nozeroes_s1 = af_section1[af_section1['value']!= 0]
df_dye_nozeroes_s1['value'].describe()

nodye_nozeroes_s1 = pd.DataFrame()
nodye_nozeroes_s1 = un_section1[un_section1['value']!= 0]
nodye_nozeroes_s1['value'].describe()

nodye_nozeroes_s12 = pd.DataFrame()
nodye_nozeroes_s12 = un_section1_2[un_section1_2['value']!= 0]
nodye_nozeroes_s12['value'].describe()

nodye_nozeroes_s13 = pd.DataFrame()
nodye_nozeroes_s13 = un_section1_3[un_section1_3['value']!= 0]
nodye_nozeroes_s13['value'].describe()

nodye_nozeroes_s14 = pd.DataFrame()
nodye_nozeroes_s14 = un_section1_4[un_section1_4['value']!= 0]
nodye_nozeroes_s14['value'].describe()


frames = [nodye_nozeroes_s1, nodye_nozeroes_s12, nodye_nozeroes_s13, nodye_nozeroes_s14]
no_dye_section1 = pd.concat(frames)
no_dye_section1['value'].describe()

#bins = np.linspace(0, 100, 50)

x = no_dye_section1['value']
y = df_dye_nozeroes_s1['value']
x = np.log10(x)
y = np.log10(y)
plt.hist(x, bins= 'auto', facecolor='g', alpha=0.5, label='nodye')
plt.hist(y, bins = 'auto', facecolor='r', alpha=0.5, label='dye')
plt.xlabel('log10 of quantity')
plt.ylabel('frequency')
plt.title('Histogram of dye vs no dye')
plt.legend(loc='upper right')
plt.show()

#Violin Plot

df = pd.DataFrame({'nodye': x, 'dye': y})
df2 = df.melt().assign(x='vars')
sns.violinplot(data=df2, x='x', y='value', hue='variable', split=True, inner='quart')

"""-------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------"""

""" data description of dye in specific section 2 in and no dye in specific section
 at all in all hair length removing the zeroes""""""




