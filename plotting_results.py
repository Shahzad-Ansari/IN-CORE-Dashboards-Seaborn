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

#%%
yr1000_Buildings = qt1000.b.sum().tolist()
yr1000_Repair_Time = np.sum(qt1000.b*qt1000.Q_t_hat).tolist()
yr1000_Population_Dislocation = np.sum(qt1000.b*qt1000.d_ijk).tolist()
yr1000_Economic_Loss = np.sum(qt1000.b*qt1000.l).tolist()
Yr1000 ={
    ('Buildings'):yr1000_Buildings,
    ('Economic Loss'):yr1000_Economic_Loss,
    ('Population Dislocation'):yr1000_Population_Dislocation,
    ('Repair Time (Days)'):yr1000_Repair_Time
}
Yr1000 = pd.DataFrame(Yr1000.items(),columns = ['Community Metrics','1000 Year Event Stats'])
Yr1000 = Yr1000.round(decimals=0)
Yr1000
#%%
Fmin500_B20 = yr500B20[yr500B20.Functionality == yr500B20.Functionality.min()].iloc[0]
Dmin500_B20 = yr500B20[yr500B20.Dislocation == yr500B20.Dislocation.min()].iloc[0]
Emin500_B20 = yr500B20[yr500B20.Economic_loss == yr500B20.Economic_loss.min()].iloc[0]
Fmin500_B40 = yr500B40[yr500B40.Functionality == yr500B40.Functionality.min()].iloc[0]
Dmin500_B40 = yr500B40[yr500B40.Dislocation == yr500B40.Dislocation.min()].iloc[0]
Emin500_B40 = yr500B40[yr500B40.Economic_loss == yr500B40.Economic_loss.min()].iloc[0]
Fmin500_B60 = yr500B60[yr500B60.Functionality == yr500B60.Functionality.min()].iloc[0]
Dmin500_B60 = yr500B60[yr500B60.Dislocation == yr500B60.Dislocation.min()].iloc[0]
Emin500_B60 = yr500B60[yr500B60.Economic_loss == yr500B60.Economic_loss.min()].iloc[0]
Fmin1000_B20 = yr1000B20[yr1000B20.Functionality == yr1000B20.Functionality.min()].iloc[0]
Dmin1000_B20 = yr1000B20[yr1000B20.Dislocation == yr1000B20.Dislocation.min()].iloc[0]
Emin1000_B20 = yr1000B20[yr1000B20.Economic_loss == yr1000B20.Economic_loss.min()].iloc[0]
Fmin1000_B40 = yr1000B40[yr1000B40.Functionality == yr1000B40.Functionality.min()].iloc[0]
Dmin1000_B40 = yr1000B40[yr1000B40.Dislocation == yr1000B40.Dislocation.min()].iloc[0]
Emin1000_B40 = yr1000B40[yr1000B40.Economic_loss == yr1000B40.Economic_loss.min()].iloc[0]
Fmin1000_B60 = yr1000B60[yr1000B60.Functionality == yr1000B60.Functionality.min()].iloc[0]
Dmin1000_B60 = yr1000B60[yr1000B60.Dislocation == yr1000B60.Dislocation.min()].iloc[0]
Emin1000_B60 = yr1000B60[yr1000B60.Economic_loss == yr1000B60.Economic_loss.min()].iloc[0]
#%%
# print("Solution Selected for Least Repair Time in 500 year event :",Fmin500_B20['S'])
# print("Solution Selected for Least Economic Loss in 500 year event :",Emin500_B20['S'])
# print("Solution Selected for Least Population Dislocation in 500 year event :",Dmin500_B20['S'])
# print("Solution Selected for Least Repair Time in 500 year event :",Fmin500_B40['S'])
# print("Solution Selected for Least Economic Loss in 500 year event :",Emin500_B40['S'])
# print("Solution Selected for Least Population Dislocation in 500 year event :",Dmin500_B40['S'])
# print("Solution Selected for Least Repair Time in 500 year event :",Fmin500_B60['S'])
# print("Solution Selected for Least Economic Loss in 500 year event :",Emin500_B60['S'])
# print("Solution Selected for Least Population Dislocation in 500 year event :",Dmin500_B60['S'])
# print("Solution Selected for Least Repair Time in 1000 year event :",Fmin1000_B20['S'])
# print("Solution Selected for Least Economic Loss in 1000 year event :",Emin1000_B20['S'])
# print("Solution Selected for Least Population Dislocation in 1000 year event :",Dmin1000_B20['S'])
# print("Solution Selected for Least Repair Time in 1000 year event :",Fmin1000_B40['S'])
# print("Solution Selected for Least Economic Loss in 1000 year event :",Emin1000_B40['S'])
# print("Solution Selected for Least Population Dislocation in 1000 year event :",Dmin1000_B40['S'])
# print("Solution Selected for Least Repair Time in 1000 year event :",Fmin1000_B60['S'])
# print("Solution Selected for Least Economic Loss in 1000 year event :",Emin1000_B60['S'])
# print("Solution Selected for Least Population Dislocation in 1000 year event :",Dmin1000_B60['S'])
#%%
Op1_500B20 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B20_X0.csv")
Op2_500B20 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B20_X79.csv")
Op3_500B20 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B20_X42.csv")
Op1_1000B20 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B20_X0.csv")
Op2_1000B20 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B20_X199.csv")
Op3_1000B20 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B20_X18.csv")
Op1_500B40 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B40_X0.csv")
Op2_500B40 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B40_X376.csv")
Op3_500B40 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B40_X122.csv")
Op1_1000B40 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B40_X0.csv")
Op2_1000B40 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B40_X119.csv")
Op3_1000B40 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B40_X196.csv")
Op1_500B60 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B60_X0.csv")
Op2_500B60 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B60_X235.csv")
Op3_500B60 = pd.read_csv("Optimization_Model/500_yr_Results/decision_variable_B60_X44.csv")
Op1_1000B60 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B60_X0.csv")
Op2_1000B60 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B60_X259.csv")
Op3_1000B60 = pd.read_csv("Optimization_Model/1000_yr_Results/decision_variable_B60_X205.csv")
#%%
### PLAN 1


subset0_Op1_500B20 = Op1_500B20[Op1_500B20["K"] == 0]
subset1_Op1_500B20 = Op1_500B20[Op1_500B20["K"] == 1]
subset2_Op1_500B20 = Op1_500B20[Op1_500B20["K"] == 2]
subset3_Op1_500B20 = Op1_500B20[Op1_500B20["K"] == 3]
P1NumB050020 = round(subset0_Op1_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P1NumB150020 = round(subset1_Op1_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P1NumB250020 = round(subset2_Op1_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P1NumB350020 = round(subset3_Op1_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op1_1000B20 = Op1_1000B20[Op1_1000B20["K"] == 0]
subset1_Op1_1000B20 = Op1_1000B20[Op1_1000B20["K"] == 1]
subset2_Op1_1000B20 = Op1_1000B20[Op1_1000B20["K"] == 2]
subset3_Op1_1000B20 = Op1_1000B20[Op1_1000B20["K"] == 3]
P1NumB0100020 = round(subset0_Op1_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P1NumB1100020 = round(subset1_Op1_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P1NumB2100020 = round(subset2_Op1_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P1NumB3100020 = round(subset3_Op1_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event


### PLAN 2 
subset0_Op2_500B20 = Op2_500B20[Op2_500B20["K"] == 0]
subset1_Op2_500B20 = Op2_500B20[Op2_500B20["K"] == 1]
subset2_Op2_500B20 = Op2_500B20[Op2_500B20["K"] == 2]
subset3_Op2_500B20 = Op2_500B20[Op2_500B20["K"] == 3]
P2NumB050020 = round(subset0_Op2_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P2NumB150020 = round(subset1_Op2_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P2NumB250020 = round(subset2_Op2_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P2NumB350020 = round(subset3_Op2_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op2_1000B20 = Op2_1000B20[Op2_1000B20["K"] == 0]
subset1_Op2_1000B20 = Op2_1000B20[Op2_1000B20["K"] == 1]
subset2_Op2_1000B20 = Op2_1000B20[Op2_1000B20["K"] == 2]
subset3_Op2_1000B20 = Op2_1000B20[Op2_1000B20["K"] == 3]
P2NumB0100020 = round(subset0_Op2_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P2NumB1100020 = round(subset1_Op2_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P2NumB2100020 = round(subset2_Op2_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P2NumB3100020 = round(subset3_Op2_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event


### PLAN 3

subset0_Op3_500B20 = Op3_500B20[Op3_500B20["K"] == 0]
subset1_Op3_500B20 = Op3_500B20[Op3_500B20["K"] == 1]
subset2_Op3_500B20 = Op3_500B20[Op3_500B20["K"] == 2]
subset3_Op3_500B20 = Op3_500B20[Op3_500B20["K"] == 3]
P3NumB050020 = round(subset0_Op3_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P3NumB150020 = round(subset1_Op3_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P3NumB250020 = round(subset2_Op3_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P3NumB350020 = round(subset3_Op3_500B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op3_1000B20 = Op3_1000B20[Op3_1000B20["K"] == 0]
subset1_Op3_1000B20 = Op3_1000B20[Op3_1000B20["K"] == 1]
subset2_Op3_1000B20 = Op3_1000B20[Op3_1000B20["K"] == 2]
subset3_Op3_1000B20 = Op3_1000B20[Op3_1000B20["K"] == 3]
P3NumB0100020 = round(subset0_Op3_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P3NumB1100020 = round(subset1_Op3_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P3NumB2100020 = round(subset2_Op3_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P3NumB3100020 = round(subset3_Op3_1000B20.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event
#%%
Budget1 = {
    ("500 Year Event Plan 1"):(Emin500_B20['Economic_loss'],Emin500_B20['Dislocation'],Emin500_B20['Functionality'],P1NumB050020,P1NumB150020,P1NumB250020,P1NumB350020),
    ("500 Year Event Plan 2"):(Dmin500_B20['Economic_loss'],Dmin500_B20['Dislocation'],Dmin500_B20['Functionality'],P2NumB050020,P2NumB150020,P2NumB250020,P2NumB350020),
    ("500 Year Event Plan 3"):(Fmin500_B20['Economic_loss'],Fmin500_B20['Dislocation'],Fmin500_B20['Functionality'],P3NumB050020,P3NumB150020,P3NumB250020,P3NumB350020),
    
    ("1000 Year Event Plan 1"):(Emin1000_B20['Economic_loss'],Emin1000_B20['Dislocation'],Emin1000_B20['Functionality'],P1NumB0100020,P1NumB1100020,P1NumB2100020,P1NumB3100020),
    ("1000 Year Event Plan 2"):(Dmin1000_B20['Economic_loss'],Dmin1000_B20['Dislocation'],Dmin1000_B20['Functionality'],P2NumB0100020,P2NumB1100020,P2NumB2100020,P2NumB3100020),
    ("1000 Year Event Plan 3"):(Fmin1000_B20['Economic_loss'],Fmin1000_B20['Dislocation'],Fmin1000_B20['Functionality'],P3NumB0100020,P3NumB1100020,P3NumB2100020,P3NumB3100020),
}
#%%
Budget1_df = pd.DataFrame(list(Budget1.items()),columns = ['Budget $40,000,000','column2']) 
new_col_list = ['Economic_Loss','Population_Dislocation','Repair_Time (Days)','Number of Buildings not Retrofitted','Number of Buildings Retrofitted to Option 1','Number of Buildings Retrofitted to Option 2','Number of Buildings Retrofitted to Option 3']
for n,col in enumerate(new_col_list):
    Budget1_df[col] = Budget1_df['column2'].apply(lambda column2: column2[n])

Budget1_df = Budget1_df.drop('column2',axis=1)
Budget1_df = Budget1_df.round(decimals=0)
Budget1_df.to_csv("Budget1_OptionsTable.csv")
Budget1_df
#%%
### PLAN 1

subset0_Op1_500B40 = Op1_500B40[Op1_500B40["K"] == 0]
subset1_Op1_500B40 = Op1_500B40[Op1_500B40["K"] == 1]
subset2_Op1_500B40 = Op1_500B40[Op1_500B40["K"] == 2]
subset3_Op1_500B40 = Op1_500B40[Op1_500B40["K"] == 3]
P1NumB050040 = round(subset0_Op1_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P1NumB150040 = round(subset1_Op1_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P1NumB250040 = round(subset2_Op1_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P1NumB350040 = round(subset3_Op1_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op1_1000B40 = Op1_1000B40[Op1_1000B40["K"] == 0]
subset1_Op1_1000B40 = Op1_1000B40[Op1_1000B40["K"] == 1]
subset2_Op1_1000B40 = Op1_1000B40[Op1_1000B40["K"] == 2]
subset3_Op1_1000B40 = Op1_1000B40[Op1_1000B40["K"] == 3]
P1NumB0100040 = round(subset0_Op1_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P1NumB1100040 = round(subset1_Op1_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P1NumB2100040 = round(subset2_Op1_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P1NumB3100040 = round(subset3_Op1_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event

### PLAN 2

subset0_Op2_500B40 = Op2_500B40[Op2_500B40["K"] == 0]
subset1_Op2_500B40 = Op2_500B40[Op2_500B40["K"] == 1]
subset2_Op2_500B40 = Op2_500B40[Op2_500B40["K"] == 2]
subset3_Op2_500B40 = Op2_500B40[Op2_500B40["K"] == 3]
P2NumB050040 = round(subset0_Op2_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P2NumB150040 = round(subset1_Op2_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P2NumB250040 = round(subset2_Op2_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P2NumB350040 = round(subset3_Op2_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op2_1000B40 = Op2_1000B40[Op2_1000B40["K"] == 0]
subset1_Op2_1000B40 = Op2_1000B40[Op2_1000B40["K"] == 1]
subset2_Op2_1000B40 = Op2_1000B40[Op2_1000B40["K"] == 2]
subset3_Op2_1000B40 = Op2_1000B40[Op2_1000B40["K"] == 3]
P2NumB0100040 = round(subset0_Op2_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P2NumB1100040 = round(subset1_Op2_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P2NumB2100040 = round(subset2_Op2_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P2NumB3100040 = round(subset3_Op2_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event


#### PLAN 3

subset0_Op3_500B40 = Op3_500B40[Op3_500B40["K"] == 0]
subset1_Op3_500B40 = Op3_500B40[Op3_500B40["K"] == 1]
subset2_Op3_500B40 = Op3_500B40[Op3_500B40["K"] == 2]
subset3_Op3_500B40 = Op3_500B40[Op3_500B40["K"] == 3]
P3NumB050040 = round(subset0_Op3_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P3NumB150040 = round(subset1_Op3_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P3NumB250040 = round(subset2_Op3_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P3NumB350040 = round(subset3_Op3_500B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op3_1000B40 = Op3_1000B40[Op3_1000B40["K"] == 0]
subset1_Op3_1000B40 = Op3_1000B40[Op3_1000B40["K"] == 1]
subset2_Op3_1000B40 = Op3_1000B40[Op3_1000B40["K"] == 2]
subset3_Op3_1000B40 = Op3_1000B40[Op3_1000B40["K"] == 3]
P3NumB0100040 = round(subset0_Op3_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P3NumB1100040 = round(subset1_Op3_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P3NumB2100040 = round(subset2_Op3_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P3NumB3100040 = round(subset3_Op3_1000B40.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event

Budget2 = {
    ("500 Year Event Plan 1"):(Emin500_B40['Economic_loss'],Emin500_B40['Dislocation'],Emin500_B40['Functionality'],P1NumB050040,P1NumB150040,P1NumB250040,P1NumB350040),
    ("500 Year Event Plan 2"):(Dmin500_B40['Economic_loss'],Dmin500_B40['Dislocation'],Dmin500_B40['Functionality'],P2NumB050040,P2NumB150040,P2NumB250040,P2NumB350040),
    ("500 Year Event Plan 3"):(Fmin500_B40['Economic_loss'],Fmin500_B40['Dislocation'],Fmin500_B40['Functionality'],P3NumB050040,P3NumB150040,P3NumB250040,P3NumB350040),
    
    ("1000 Year Event Plan 1"):(Emin1000_B40['Economic_loss'],Emin1000_B40['Dislocation'],Emin1000_B40['Functionality'],P1NumB0100040,P1NumB1100040,P1NumB2100040,P1NumB3100040),
    ("1000 Year Event Plan 2"):(Dmin1000_B40['Economic_loss'],Dmin1000_B40['Dislocation'],Dmin1000_B40['Functionality'],P2NumB0100040,P2NumB1100040,P2NumB2100040,P2NumB3100040),
    ("1000 Year Event Plan 3"):(Fmin1000_B40['Economic_loss'],Fmin1000_B40['Dislocation'],Fmin1000_B40['Functionality'],P3NumB0100040,P3NumB1100040,P3NumB2100040,P3NumB3100040),
}
Budget2_df = pd.DataFrame(list(Budget2.items()),columns = ['Budget $80,000,000','column2']) 
new_col_list = ['Economic_Loss','Population_Dislocation','Repair_Time (Days)','Number of Buildings not Retrofitted','Number of Buildings Retrofitted to Option 1','Number of Buildings Retrofitted to Option 2','Number of Buildings Retrofitted to Option 3']
for n,col in enumerate(new_col_list):
    Budget2_df[col] = Budget2_df['column2'].apply(lambda column2: column2[n])

Budget2_df = Budget2_df.drop('column2',axis=1)
Budget2_df = Budget2_df.round(decimals=0)
Budget2_df.to_csv("Budget2_OptionsTable.csv")
Budget2_df

#%%
### PLAN 1

subset0_Op1_500B60 = Op1_500B60[Op1_500B60["K"] == 0]
subset1_Op1_500B60 = Op1_500B60[Op1_500B60["K"] == 1]
subset2_Op1_500B60 = Op1_500B60[Op1_500B60["K"] == 2]
subset3_Op1_500B60 = Op1_500B60[Op1_500B60["K"] == 3]
P1NumB050060 = round(subset0_Op1_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P1NumB150060 = round(subset1_Op1_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P1NumB250060 = round(subset2_Op1_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P1NumB350060 = round(subset3_Op1_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op1_1000B60 = Op1_1000B60[Op1_1000B60["K"] == 0]
subset1_Op1_1000B60 = Op1_1000B60[Op1_1000B60["K"] == 1]
subset2_Op1_1000B60 = Op1_1000B60[Op1_1000B60["K"] == 2]
subset3_Op1_1000B60 = Op1_1000B60[Op1_1000B60["K"] == 3]
P1NumB0100060 = round(subset0_Op1_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P1NumB1100060 = round(subset1_Op1_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P1NumB2100060 = round(subset2_Op1_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P1NumB3100060 = round(subset3_Op1_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event

### PLAN 2

subset0_Op2_500B60 = Op2_500B60[Op2_500B60["K"] == 0]
subset1_Op2_500B60 = Op2_500B60[Op2_500B60["K"] == 1]
subset2_Op2_500B60 = Op2_500B60[Op2_500B60["K"] == 2]
subset3_Op2_500B60 = Op2_500B60[Op2_500B60["K"] == 3]
P2NumB050060 = round(subset0_Op2_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P2NumB150060 = round(subset1_Op2_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P2NumB250060 = round(subset2_Op2_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P2NumB350060 = round(subset3_Op2_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op2_1000B60 = Op2_1000B60[Op2_1000B60["K"] == 0]
subset1_Op2_1000B60 = Op2_1000B60[Op2_1000B60["K"] == 1]
subset2_Op2_1000B60 = Op2_1000B60[Op2_1000B60["K"] == 2]
subset3_Op2_1000B60 = Op2_1000B60[Op2_1000B60["K"] == 3]
P2NumB0100060 = round(subset0_Op2_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P2NumB1100060 = round(subset1_Op2_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P2NumB2100060 = round(subset2_Op2_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P2NumB3100060 = round(subset3_Op2_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event

### PLAN 3

subset0_Op3_500B60 = Op3_500B60[Op3_500B60["K"] == 0]
subset1_Op3_500B60 = Op3_500B60[Op3_500B60["K"] == 1]
subset2_Op3_500B60 = Op3_500B60[Op3_500B60["K"] == 2]
subset3_Op3_500B60 = Op3_500B60[Op3_500B60["K"] == 3]
P3NumB050060 = round(subset0_Op3_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 500 yr event
P3NumB150060 = round(subset1_Op3_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 500 yr event
P3NumB250060 = round(subset2_Op3_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 500 yr event
P3NumB350060 = round(subset3_Op3_500B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 500 yr event
subset0_Op3_1000B60 = Op3_1000B60[Op3_1000B60["K"] == 0]
subset1_Op3_1000B60 = Op3_1000B60[Op3_1000B60["K"] == 1]
subset2_Op3_1000B60 = Op3_1000B60[Op3_1000B60["K"] == 2]
subset3_Op3_1000B60 = Op3_1000B60[Op3_1000B60["K"] == 3]
P3NumB0100060 = round(subset0_Op3_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 0 for 1000 yr event
P3NumB1100060 = round(subset1_Op3_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 1 for 1000 yr event
P3NumB2100060 = round(subset2_Op3_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 2 for 1000 yr event
P3NumB3100060 = round(subset3_Op3_1000B60.Values.sum(), 0) #Number of Buildings in Retrofit Op 3 for 1000 yr event

Budget3 = {
    ("500 Year Event Plan 1"):(Emin500_B60['Economic_loss'],Emin500_B60['Dislocation'],Emin500_B60['Functionality'],P1NumB050060,P1NumB150060,P1NumB250060,P1NumB350060),
    ("500 Year Event Plan 2"):(Dmin500_B60['Economic_loss'],Dmin500_B60['Dislocation'],Dmin500_B60['Functionality'],P2NumB050060,P2NumB150060,P2NumB250060,P2NumB350060),
    ("500 Year Event Plan 3"):(Fmin500_B60['Economic_loss'],Fmin500_B60['Dislocation'],Fmin500_B60['Functionality'],P3NumB050060,P3NumB150060,P3NumB250060,P3NumB350060),
    
    ("1000 Year Event Plan 1"):(Emin1000_B60['Economic_loss'],Emin1000_B60['Dislocation'],Emin1000_B60['Functionality'],P1NumB0100060,P1NumB1100060,P1NumB2100060,P1NumB3100060),
    ("1000 Year Event Plan 2"):(Dmin1000_B60['Economic_loss'],Dmin1000_B60['Dislocation'],Dmin1000_B60['Functionality'],P2NumB0100060,P2NumB1100060,P2NumB2100060,P2NumB3100060),
    ("1000 Year Event Plan 3"):(Fmin1000_B60['Economic_loss'],Fmin1000_B60['Dislocation'],Fmin1000_B60['Functionality'],P3NumB0100060,P3NumB1100060,P3NumB2100060,P3NumB3100060),
}

Budget3_df = pd.DataFrame(list(Budget3.items()),columns = ['Budget $120,000,000','column2']) 
new_col_list = ['Economic_Loss','Population_Dislocation','Repair_Time (Days)','Number of Buildings not Retrofitted','Number of Buildings Retrofitted to Option 1','Number of Buildings Retrofitted to Option 2','Number of Buildings Retrofitted to Option 3']
for n,col in enumerate(new_col_list):
    Budget3_df[col] = Budget3_df['column2'].apply(lambda column2: column2[n])

Budget3_df = Budget3_df.drop('column2',axis=1)
Budget3_df = Budget3_df.round(decimals=0)
Budget3_df.to_csv("Budget3_OptionsTable.csv")
Budget3_df


















