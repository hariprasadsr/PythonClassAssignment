# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:24:34 2021

@author: T480s
"""

#Need to make a gaming board

gameboard = ""

for game in range(10):
   w = 80

   def display():
       size(1000,800)
    
   def boxes():
       x,y = 0,0
       for row in gameboard:
           for col in row:
               rect(x,y,w,w)
               x = x + w
           y = y + w
           x = 0
print(gameboard)
  
            