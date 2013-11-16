# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
from pylab import *

def drawBymatplotlib():
    listCPU=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
    listRSIZE=[2,3,4,5,6,7,8,9]
    listVSIZE=[3,4,5,6,7,8,9,10]

    f, axarr = plt.subplots(2,2)
    axarr[0,0].axis([0, listCPU.__len__()-0.5,(min(listCPU))-0.1, max(listCPU)+0.3])
    axarr[0,0].plot(listCPU,'-r*')
    axarr[0,0].set_title('CPU Usage')
    axarr[0,0].set_xlabel('Game Event',fontsize=12)
    axarr[0,0].set_ylabel('CPU Usage (%)',fontsize=12)
    for i in range(0,listCPU.__len__()):
        axarr[0,0].text(i,float(listCPU[i])+0.1,str(listCPU[i])+"%")
    axarr[0,0].grid(True)
    
    axarr[0,1].axis([0, listRSIZE.__len__()-0.5, int(min(listRSIZE))-1, int(max(listRSIZE))+3])
    axarr[0,1].plot(listRSIZE,'-r*')
    axarr[0,1].set_title('Real Memory Usage')
    axarr[0,1].set_xlabel('Game Event',fontsize=12)
    axarr[0,1].set_ylabel('Real Memory Usage (MB)',fontsize=12)
    for i in range(0,listRSIZE.__len__()):
        axarr[0,1].text(i,int(listRSIZE[i])+1.5,str(listRSIZE[i])+"MB")
    axarr[0,1].grid(True)

    axarr[1,0].axis([0, listVSIZE.__len__()-0.5, int(min(listVSIZE))-1, int(max(listVSIZE))+3])
    axarr[1,0].plot(listVSIZE,'-r*')
    axarr[1,0].set_title('Virtual Memory Usage')
    axarr[1,0].set_xlabel('Game Event',fontsize=12)
    axarr[1,0].set_ylabel('Virtual Memory Usage (MB)',fontsize=12)
    for i in range(0,listRSIZE.__len__()):
        axarr[1,0].text(i,int(listVSIZE[i])+1.5,str(listVSIZE[i])+"MB")
    axarr[1,0].grid(True)

    plt.show()

if __name__ == "__main__":
    drawBymatplotlib()
