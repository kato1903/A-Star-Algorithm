# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:57:25 2019

@author: toprak.kesgin
"""


import random
import matplotlib.pyplot as plt
import copy
from Environment import Environment
from Astar import Astar
from State import State
import time

harita = Environment(30,30)
harita.randomMap()
start = [2,5]
end =  [25,29]
harita.showMap()

astar = Astar(start,end,harita,100)
aStarYol = astar.astar()
astar.ShowMap(aStarYol)


