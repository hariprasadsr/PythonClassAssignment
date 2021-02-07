# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:51:53 2021

@author: T480s
"""

MyUniqueList = []
MyLeftover =[]

def AddNewElement(EnteredValue):
    if EnteredValue in MyUniqueList:
        MyLeftover.append(EnteredValue)
        return True
    else:
        MyUniqueList.append(EnteredValue)
        return False
    
EnteredValue = input("Add a new element to the list :  ")
AddNewElement(EnteredValue)

print('My unique list is : '+ str(MyUniqueList))
print('my left over list is : ' + str(MyLeftover))

   

