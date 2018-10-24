# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:50:48 2018

@author: Thurstan.Green
"""


###how to divide 

import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randint(1, 5, size=(5, 2)), columns=['a', 'b'])
 
# divide is equivalent to df['a']/df['b']
# but with support to substitute a fill_value for missing data
 
# introduce missing data
df.loc[1, 'a'] = None
print(df) 

df['c'] = df['a'].divide(df['b'], fill_value=1)
df['d'] = df['a']/df['b']

df['e'] = df['a']/2

print(df) 

del df


####stacked bar chart

import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.xlabel('TG random')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()