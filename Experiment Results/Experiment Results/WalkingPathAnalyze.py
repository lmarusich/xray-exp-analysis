# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 00:32:31 2022

@author: hguo2
"""

import matplotlib.pyplot as plt
import numpy as np
import random

with open ('YuYenTaggingTime.txt') as f:
    lines = f.readlines()

positionCounter = 1
sphereCounter = 0
mapXRaySwitch = 2
    
x_Map = []
z_Map = []
MapSphere = []

x_XRay = []
z_XRay = []
XRaySphere = []

for i in lines:
    if i[0] == "M" and i[1] == "a":
        mapXRaySwitch = 0
        sphereCounter = 0
    elif i[0] == "X":
        mapXRaySwitch = 1
        sphereCounter = 0
    if i[0] == "S":
        if mapXRaySwitch == 0:
            MapSphere.append(sphereCounter)
        elif mapXRaySwitch == 1:
            XRaySphere.append(sphereCounter)
        # sphereCounter = 0
    if i[0] == "(" and positionCounter == 1:
        sphereCounter += 1
        i = i.replace("(","")
        i = i.replace(")","")
        i = i.replace("\n","")
        i = i.split(", ")
        if mapXRaySwitch == 0:
            x_Map.append(float(i[0]))
            z_Map.append(float(i[2]))
        elif mapXRaySwitch == 1:
            x_XRay.append(float(i[0]))
            z_XRay.append(float(i[2]))
        positionCounter = 0
    elif i[0] == " ":
        positionCounter = 1

# plt.scatter(x,z)

x_bound = [-2, 0, 2, 0, -2]
z_bound = [0, 2, 0, -2, 0]


colorList = ['red', 'green', 'blue', 'purple', 'black']

plt.plot(x_bound, z_bound, '-o', color='orange')

for i in range(4):
    if i == 0:
        plt.plot(x_XRay[0:XRaySphere[i]+1], z_XRay[0:XRaySphere[i]+1], colorList[0])
    plt.plot(x_XRay[XRaySphere[i]:XRaySphere[i+1]+1], z_XRay[XRaySphere[i]:XRaySphere[i+1]+1], colorList[i+1])

plt.savefig('YuYenXRay.png')

plt.clf()

plt.plot(x_bound, z_bound, '-o', color='orange')

for i in range(4):
    if i == 0:
        plt.plot(x_Map[0:MapSphere[i]+1], z_Map[0:MapSphere[i]+1], colorList[0])
    plt.plot(x_Map[MapSphere[i]:MapSphere[i+1]+1], z_Map[MapSphere[i]:MapSphere[i+1]+1], colorList[i+1])

plt.savefig('YuYenMap.png')








