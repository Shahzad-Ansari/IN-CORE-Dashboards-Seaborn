# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:28:54 2022

@author: ShahzadAnsari
"""

import random
import pandas as pd
import random 
import numpy as np
random.seed(10)

cLat = 32.779193
cLong = -96.7929680


def randomNoSolution():
    x = random.sample(range(500, 2000))
    y = random.sample(range(300, 1000))
    z = random.sample(range(650, 3500))
    
    return [x,y,z]

def randomLatLong():
    minLong = -96.51695
    maxLong = -97.033364
    
    minLat = 32.590792
    maxLat = 33.21801
    
    
    lats = []
    longs = []
    
    for i in range(100):
        lats.append(np.random.uniform(minLat,maxLat))
        longs.append(np.random.uniform(minLong,maxLong))
   
    return pd.DataFrame(list(zip(lats,longs)),columns = ['lat','long'])

def getBuildingUpgrades(coords,preatoFrontier):
    
    solutionList = []
    
    for i in range(50):
        df = pd.DataFrame()
        df = coords
        df['upGrade'] = np.random.randint(0, 3, df.shape[0])
        solutionList.append(df)
    
    return solutionList
      
def getSolution(solutionList,sol_Id):
    return solutionList[sol_Id+1]
    





