import matplotlib.pyplot as plt
from matplotlib.pylab import ion, draw
import matplotlib.cm as cm
import numpy as np 



class Plot(object):


  def __init__(self):
    # establish an empty plot

    self.columnDimensionsL4 = 100
    self.columnDimensionsL3 = 100
    self.sensoryInputDim = 100
    self.motorInputDim = 100

    self.l4Activity = np.zeros((self.columnDimensionsL4, 1))
    self.l3Activity = np.zeros((self.columnDimensionsL3, 1))

    self.plot = plt.figure()
    plt.clf()
    plt.gca().invert_yaxis()


  def update(self, model):
    """
    update figure 
    """

    L4_active = np.zeros((self.columnDimensionsL4, 1))
    L3_active = np.zeros((self.columnDimensionsL3, 1))
    if len(model.experimentRunner.tm.mmGetTraceActiveColumns().data)>0:
        L4_active[list(model.experimentRunner.tm.mmGetTraceActiveColumns().data[-1])] = 1

    self.l4Activity = np.concatenate((self.l4Activity, L4_active),1)
    print self.l4Activity.shape[1]

    if len(model.experimentRunner.tp.mmGetTraceActiveCells().data)>0:
        L3_active[list(model.experimentRunner.tp.mmGetTraceActiveCells().data[-1])] = 1
    self.l3Activity = np.concatenate((self.l3Activity, L3_active),1)
    
    if self.l4Activity.shape[1] > 20:
        self.l4Activity = self.l4Activity[:,-20:]
        self.l3Activity = self.l3Activity[:,-20:]

    self.display()


  def display(self):
    nrol = 2
    ion() # interactive mode on
    plt.subplot(nrol, 1, 1)
    plt.imshow(self.l3Activity, cmap = cm.Greys_r, \
                aspect="auto",interpolation="nearest")    
    plt.ylabel(' L3 Activity ')

    plt.subplot(nrol, 1, 2)
    plt.imshow(self.l4Activity, cmap = cm.Greys_r, \
                aspect="auto",interpolation="nearest")
    plt.ylabel(' L4 Activity ')
    draw()