# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 06:18:49 2018

@author: Thurstan.Green
"""

import pandas as pd
pd.set_option('display.max_columns', 10)
import numpy as np

vm = pd.read_csv('C:/Users/thurstan.green/OneDrive - PERFORM GROUP/1810 python viewing/viewingwithlapse181022.txt',sep='|')

print(vm.head(10))
print(vm.columns.values)


print(vm.groupby(['NFL_SEASON']).count())

#[] where clause goes here
vm.groupby(["NFL_SEASON","NFL_WEEK"]).count()


print(
        vm      
        .groupby(["NFL_SEASON","NFL_WEEK"])
        ["SECONDS_WATCHED"].agg([np.mean, np.sum, np.size,np.count_nonzero])
        )



print(
        vm  [
         ((vm["NFL_SEASON"]== 2018)) #where clause
            ]
        .groupby(["NFL_SEASON","NFL_WEEK","VIEWINGBAND1"])
        ["SECONDS_WATCHED"].agg([np.mean, np.size])
        )

print(
        vm  [
         ((vm["NFL_SEASON"]== 2018)) #where clause
            ]
        .groupby(["NFL_SEASON","NFL_WEEK","VIEWINGBAND1"])
        ["SECONDS_WATCHED","DESKTOP_PERC"].agg([np.mean,np.size])
        )


print(
        vm  [
         ((vm["NFL_SEASON"]== 2018)) #where clause
            ]
        .groupby(["NFL_SEASON","NFL_WEEK","VIEWINGBAND1"])
        .agg({"SECONDS_WATCHED" : np.sum, "DESKTOP_PERC" : np.mean,"PERSONAL_PERC" : np.mean})
        )



import matplotlib.pyplot as plt