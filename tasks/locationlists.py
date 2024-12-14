import os
import numpy as np


class LocationLists:
    def __init__(self, list1=None, list2=None):
        if list1==None or list2==None:
            self.list1 = np.ndarray(1)
            self.list2 = np.ndarray(1)
            self.len   = -1
        else:
            self._set_list(list1,list2)

    def get_distance(self):
        l1=np.sort(self.list1)
        l2=np.sort(self.list2)
        return np.sum(np.abs(l1-l2))      

    def load_list(self,filename):
        # load from text file
        d=np.fromfile(filename,sep=" ")
        list1 = d[range(0,len(d),2)]
        list2 = d[range(1,len(d),2)]
        self._set_list(list1,list2)
    
    def _set_list(self,list1,list2):
        # set list directly
        if list1.shape ==list2.shape:
            self.list1 = list1
            self.list2 = list2
            self.len   = len(list1)
        else:
            os.error('unequal shape of list1 & list2')