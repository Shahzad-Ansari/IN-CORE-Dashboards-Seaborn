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



def randomPreato(dims):
    
    SolId = list(range(1,51))
    
    x = random.sample(range(0, 300), 50)
    y = random.sample(range(0, 1000), 50)
    if dims == 3:
        z = random.sample(range(0, 3500), 50)
        df = pd.DataFrame(list(zip(SolId,x,y,z)),columns = ['SolId','x','y','z'])
    else:
        df = pd.DataFrame(list(zip(SolId,x,y)),columns = ['SolId','x','y'])
        
   
   
    return df
   


def randomNoSolution(dims):
    
    
    x = random.randint(500, 2000)
    y = random.randint(300, 1000)
    z = random.randint(650, 3500)
    b = random.randint(0,100)
    
    df = pd.DataFrame()
    
    if dims == 3:   
        df['x'] = [x]
        df['y'] = [y]
        df['z'] = [z]
        df['b'] = [b]
    else:
        df['x'] = [x]
        df['y'] = [y]
        df['b'] = [b]
    
    
    
    return df


def randomLatLong():
    minLong = -96.51695
    maxLong = -97.033364
    
    minLat = 32.590792
    maxLat = 33.21801
    
    
    lats = []
    longs = []
    
    for i in range(500):
        lats.append(np.random.uniform(minLat,maxLat))
        longs.append(np.random.uniform(minLong,maxLong))
   
    return pd.DataFrame(list(zip(lats,longs)),columns = ['lat','long'])

def getBuildingUpgrades(coords):
    
    solutionList = []
    
    for i in range(50):
        df = pd.DataFrame()
        df = coords
        df['upGrade'] = np.random.randint(0, 3, df.shape[0])
        solutionList.append(df)
    
    return solutionList
      
def getSolution(solutionList,sol_Id):
    return solutionList[sol_Id+1]
    
