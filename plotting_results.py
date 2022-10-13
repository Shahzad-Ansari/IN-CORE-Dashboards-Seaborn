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


