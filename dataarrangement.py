# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 20:46:00 2021

@author: SB00747428
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
