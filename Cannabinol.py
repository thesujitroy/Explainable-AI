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

scalp_hair['sample_dye_line_length'] = scalp_hair['sample_dye_line_length'].fillna(-1)
unaffectedsection = []
for i in scalp_hair['sample_dye_line_length']:
    if i == -1:
        unaffectedsection.append(12)
    elif i > 0 and i < 1.2:
        unaffectedsection.append(0)
    elif i>= 1.2 and i < 2.4:
        unaffectedsection.append(1)
    elif i>= 2.4 and i < 3.6:
        unaffectedsection.append(2)
    elif i>= 3.6 and i < 4.8:
        unaffectedsection.append(3)
    elif i>= 4.8 and i < 6.0:
        unaffectedsection.append(4)
    elif i>= 6.0 and i < 7.2:
        unaffectedsection.append(5)
    else:
        unaffectedsection.append(6)
        
scalp_hair['unaffectedsection'] = unaffectedsection

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
x = position1[position1['testable']== 'Cannabinol']
pos1[['instruction_fnumber', 'value', 'unaffectedsection']] = x[['instruction_fnumber', 'value', 'unaffectedsection']]
# = position1[position1['testable']== 'Cocaine'].value

y = position2[position2['testable']== 'Cannabinol']
pos2[['instruction_fnumber', 'value1', 'unaffectedsection1']] = y[['instruction_fnumber', 'value', 'unaffectedsection']]

z = position3[position3['testable']== 'Cannabinol']
pos3[['instruction_fnumber', 'value2', 'unaffectedsection2']] = z[['instruction_fnumber', 'value', 'unaffectedsection']]

a = position4[position4['testable']== 'Cannabinol']
pos4[['instruction_fnumber', 'value3', 'unaffectedsection3']] = a[['instruction_fnumber', 'value', 'unaffectedsection']]

b = position5[position5['testable']== 'Cannabinol']
pos5[['instruction_fnumber', 'value4', 'unaffectedsection4']] = b[['instruction_fnumber', 'value', 'unaffectedsection']]

c = position6[position6['testable']== 'Cannabinol']
pos6[['instruction_fnumber', 'value5', 'unaffectedsection5']] = c[['instruction_fnumber', 'value', 'unaffectedsection']]

merged = pd.merge(pos1, pos2, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos4, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos5, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()

merged = merged.merge(pos6, on ='instruction_fnumber', how = 'left')
merged = merged.drop_duplicates()
merged.to_csv('Cannabinol.csv',index=False)

