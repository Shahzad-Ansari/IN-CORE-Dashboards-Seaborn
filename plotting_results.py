# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:33:18 2022

@author: ShahzadAnsari
"""

##
#%%
# from pyincore.analyses.housingunitallocation import HousingUnitAllocation
# from pyincore.analyses.populationdislocation import PopulationDislocation, PopulationDislocationUtil
# from pyincore.analyses.cumulativebuildingdamage import CumulativeBuildingDamage
# from pyincore.analyses.buildingdamage import BuildingDamage
# from pyincore import IncoreClient, Dataset, FragilityService, MappingSet, DataService
import os
import pandas as pd
#import geopandas as gpd
#import contextily as ctx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams["figure.figsize"] = 20, 20

#%%
qt500 = pd.read_csv("Optimization_Model/seaside_qt_data_500.csv")
qt1000 = pd.read_csv("Optimization_Model/seaside_qt_data_1000.csv")
sc500 = pd.read_csv("Optimization_Model/seaside_sc_data_500.csv")
sc1000 = pd.read_csv("Optimization_Model/seaside_sc_data_1000.csv")
#%%
yr500B20 = pd.read_csv("Optimization_Model/500_yr_Results/results_B20_.csv")
yr500B40 = pd.read_csv("Optimization_Model/500_yr_Results/results_B40_.csv")
yr500B60 = pd.read_csv("Optimization_Model/500_yr_Results/results_B60_.csv")
yr1000B20 = pd.read_csv("Optimization_Model/1000_yr_Results/results_B20_.csv")
yr1000B40 = pd.read_csv("Optimization_Model/1000_yr_Results/results_B40_.csv")
yr1000B60 = pd.read_csv("Optimization_Model/1000_yr_Results/results_B60_.csv")
#%%
def optimal_points(list_loss,list_dislocation,list_func):
    
    """
    This funciton is  to select the optimal points of objective function  from feasible points
    input: 
    list_loss: list of economic values 
    list_dislocation: list of population dislocation values
    list_func: list of functionality values
    return:
    loss_optimal: list of optimal values of economic loss
    dislocation_optimal:list of optimal values of population dislocatio
    func_optimal:list of optimal values of funcitonality
    
    """ 
    
    l_com = []
    for i in range(0,len(list_loss)):
        l_com.append(tuple([list_loss[i],list_dislocation[i],list_func[i]]))
    # remove the repeated the points
    set_com = set(l_com)
    
    # change the set to list
    list_temp = []
    for x in set_com:
        list_temp.append(x)
    #print("new order:")
    #print(list_temp)
    # if loss and dislocation values  are same as the last loop, find the best value for functionality
    final_f = []
    f_temp = []
    for i in range(len(list_temp)): 
        for j in range(i+1,len(list_temp)):
            if list_temp[i][0] == list_temp[j][0] and list_temp[i][1] ==  list_temp[j][1]:
                if list_temp[i][2] > list_temp[j][2]:
                    f_temp.append(list_temp[i])
                    
                elif list_temp[j][2] > list_temp[i][2]:
                    f_temp.append(list_temp[j])
    final_f = list(set(list_temp) - set(f_temp))
    #print("functionality")
    #print(final_f)
    
    # find the optimal value for dislocation if loss and functionality are same as the last loop
    final_d = []  
    d_temp = []
    for i in range(len(final_f)):
        for j in range(i+1,len(final_f)):
            if final_f[i][0] == final_f[j][0] and final_f[i][2] ==  final_f[j][2]:
                if final_f[i][1] < final_f[j][1]:
                    d_temp.append(final_f[j])
                elif final_f[i][1] > final_f[j][1]:
                    d_temp.append(final_f[i]) 
          
    final_d = list(set(final_f) - set(d_temp))
    #print('dislocation')
    #print(final_d)
    
    # find the optimal value for loss if dislocation and functionality are same as the last loop
    final_l = []
    l_temp = []
    for i in range(len(final_d)):
        for j in range(i+1,len(final_d)):
            if final_d[i][1] == final_d[j][1] and final_d[i][2] ==  final_d[j][2]:
                if final_d[i][0] < final_d[j][0]:
                    l_temp.append(final_d[j])
                elif final_d[i][0] > final_d[j][0]:
                    l_temp.append(final_d[i]) 
    final_l = list(set(final_d) - set(l_temp))
    
    #print('loss')
    #print(final_l)        
    loss_optimal = []
    dislocation_optimal = []
    func_optimal = []
    for x in final_l:
        loss_optimal.append(x[0])
        dislocation_optimal.append(x[1])
        func_optimal.append(x[2])
        
    return loss_optimal,dislocation_optimal,func_optimal

# adding formatting to make plots show $ and millions
def millions(x, pos):
    return '$%1.0fM' % (x*1e-6)
formatter = FuncFormatter(millions)
#%%

loss_500optimal20 = yr500B20['Economic_loss']
dislocation_500optimal20 = yr500B20['Dislocation']
func_500optimal20 = yr500B20['Functionality']
loss_500optimal40 = yr500B40['Economic_loss']
dislocation_500optimal40 = yr500B40['Dislocation']
func_500optimal40 = yr500B40['Functionality']
loss_500optimal60 = yr500B60['Economic_loss']
dislocation_500optimal60 = yr500B60['Dislocation']
func_500optimal60 = yr500B60['Functionality']

#%%
loss_1000optimal20 = yr1000B20['Economic_loss']
dislocation_1000optimal20 = yr1000B20['Dislocation']
func_1000optimal20 = yr1000B20['Functionality']
loss_1000optimal40 = yr1000B40['Economic_loss']
dislocation_1000optimal40 = yr1000B40['Dislocation']
func_1000optimal40 = yr1000B40['Functionality']
loss_1000optimal60 = yr1000B60['Economic_loss']
dislocation_1000optimal60 = yr1000B60['Dislocation']
func_1000optimal60 = yr1000B60['Functionality']
#%%
loss_500optimal20, dislocation_500optimal20,func_500optimal20 = optimal_points(loss_500optimal20,dislocation_500optimal20,func_500optimal20)
loss_500optimal40, dislocation_500optimal40,func_500optimal40 = optimal_points(loss_500optimal40,dislocation_500optimal40,func_500optimal40)
loss_500optimal60, dislocation_500optimal60,func_500optimal60 = optimal_points(loss_500optimal60,dislocation_500optimal60,func_500optimal60)
#%%
loss_1000optimal20, dislocation_1000optimal20,func_1000optimal20 = optimal_points(loss_1000optimal20,dislocation_1000optimal20,func_1000optimal20)
loss_1000optimal40, dislocation_1000optimal40,func_1000optimal40 = optimal_points(loss_1000optimal40,dislocation_1000optimal40,func_1000optimal40)
loss_1000optimal60, dislocation_1000optimal60,func_1000optimal60 = optimal_points(loss_1000optimal60,dislocation_1000optimal60,func_1000optimal60)
#%%
#20% Budget Options ($40,000,000)
print("Range of Repair Time:",min(func_500optimal20),",",max(func_500optimal20))
print("Range of Population Dislocation:",min(dislocation_500optimal20),",",max(dislocation_500optimal20))
print("Range of Economic loss($Million Dollar):",min(loss_500optimal20),",",max(loss_500optimal20))
#%%
print("Range of Repair Time:",min(func_1000optimal20),",",max(func_1000optimal20))
print("Range of Population Dislocation:",min(dislocation_1000optimal20),",",max(dislocation_1000optimal20))
print("Range of Economic loss($Million Dollar):",min(loss_1000optimal20),",",max(loss_1000optimal20))
#%%
#500 year event
#%%
#1000 year event 
print("Range of Repair Time:",min(func_1000optimal20),",",max(func_1000optimal20))
print("Range of Population Dislocation:",min(dislocation_1000optimal20),",",max(dislocation_1000optimal20))
print("Range of Economic loss($Million Dollar):",min(loss_1000optimal20),",",max(loss_1000optimal20))
#%%
#.... missing many cells 


#%%
yr500_Buildings = qt500.b.sum().tolist()
yr500_Repair_Time = np.sum(qt500.b*qt500.Q_t_hat).tolist()
yr500_Population_Dislocation = np.sum(qt500.b*qt500.d_ijk).tolist()
yr500_Economic_Loss = np.sum(qt500.b*qt500.l).tolist()
Yr500 ={
    ('Buildings'):yr500_Buildings,
    ('Economic Loss'):yr500_Economic_Loss,
    ('Population Dislocation'):yr500_Population_Dislocation,
    ('Repair Time (Days)'):yr500_Repair_Time
}
Yr500 = pd.DataFrame(Yr500.items(),columns = ['Community Metrics','500 Year Event Stats'])
Yr500 = Yr500.round(decimals=0)
Yr500





































