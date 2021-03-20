# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:05:03 2019

@author: 111

可视化街区
"""

import json 
import matplotlib.pyplot as plt
import numpy as np

#区域id,边界和中心
regions = json.load(open('region_beijing_countfilter10.json'))
center = regions['center']
region = regions['boundary']



plt.figure(figsize=(8,5),dpi=200)
for i in range(len(center)):
    tmp = center[i]
    temp = region[i]
    #plt.plot(tmp[0],tmp[1],'.')
    plt.plot(np.array(region[i])[:,0],np.array(region[i])[:,1],linewidth=0.8)
plt.xlim([116.1,116.7])
plt.ylim([39.7,40.2])
plt.yticks(size = 16)
plt.xticks(size = 16)
plt.xlabel('Longitude',fontsize=18)
plt.ylabel('Latitude',fontsize=18)
plt.show()