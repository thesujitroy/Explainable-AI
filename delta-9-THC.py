# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:46:00 2021

@author: SB00747428
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy import stats
from scipy.stats import norm, skew
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


dataset = pd.read_csv('sujit_data_export.csv', sep=',') 
value = []
for i in dataset['result']:
    if i == 'ND':
        y = 0
    if i == 'NT':
        y = 0
    else: 
       for s in i.split():
           if s.isdigit():
               y = int(s)
    value.append(y)
dataset['value'] = value

scalp_hair = dataset[dataset['sample_type__type'] == 'Scalp Hair']
body_hair = dataset[dataset['sample_type__type'] == 'Body Hair']
urine = dataset[dataset['sample_type__type'] == 'Urine']
facial_hair = dataset[dataset['sample_type__type'] == 'Facial Hair']
nails = dataset[dataset['sample_type__type'] == 'Nail Clippings']

position1 = scalp_hair[scalp_hair['position'] == 1]
position2 = scalp_hair[scalp_hair['position'] == 2]
position3 = scalp_hair[scalp_hair['position'] == 3]
position4 = scalp_hair[scalp_hair['position'] == 4]
position5 = scalp_hair[scalp_hair['position'] == 5]
position6 = scalp_hair[scalp_hair['position'] == 6]

drugslist_cocaine= ['Cocaine', 'Benzoylecgonine', 'Cocaethylene', 'Norcocaine', 'Anhydroecgonine methyl ester']

drugslist_cannabis = ['delta-9-THC', 'Cannabidiol', 'Cannabinol']


"""
Cocaine
"""
pos1 = pd.DataFrame()
pos2 = pd.DataFrame()
pos3 = pd.DataFrame()
pos4 = pd.DataFrame()
pos5 = pd.DataFrame()
pos6 = pd.DataFrame()
#cocaine["client_pk"]= position1[position1['testable']== 'Cocaine'].client_pk
x = position1[position1['testable']== 'delta-9-THC']
pos1[['instruction_fnumber', 'value']] = x[['instruction_fnumber', 'value']]
# = position1[position1['testable']== 'delta-9-THC'].value

y = position2[position2['testable']== 'delta-9-THC']
pos2[['instruction_fnumber', 'value1']] = y[['instruction_fnumber', 'value']]

z = position3[position3['testable']== 'delta-9-THC']
pos3[['instruction_fnumber', 'value2']] = z[['instruction_fnumber', 'value']]

a = position4[position4['testable']== 'delta-9-THC']
pos4[['instruction_fnumber', 'value3']] = a[['instruction_fnumber', 'value']]

b = position5[position5['testable']== 'delta-9-THC']
pos5[['instruction_fnumber', 'value4']] = b[['instruction_fnumber', 'value']]

c = position6[position6['testable']== 'delta-9-THC']
pos6[['instruction_fnumber', 'value5']] = c[['instruction_fnumber', 'value']]

merged = pd.merge(pos1, pos2, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos4, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos5, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos6, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()
merged.to_csv('merged_delta-9-THC.csv',index=False)
fig = px.parallel_coordinates(merged, color=merged.index, labels={"index": "client number",
                "value": "value", "value1": "value1",
                "value2": "value2", "value3": "value3", "value4": "value4","value5": "value5",},
                             color_continuous_scale=px.colors.diverging.Tealrose,
                             color_continuous_midpoint=2)
fig.show()
