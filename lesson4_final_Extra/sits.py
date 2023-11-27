# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:53:42 2023

@author: laptop pro
"""


from kivy.uix.label import Label
from kivy.clock import Clock


class Sits(Label):
   def __init__(self, total, **kwargs):
       self.current = 0
       self.total = total
       my_text = "Squats left: " + str(self.total)
       super().__init__(text=my_text, **kwargs)


   def next(self, *args):
       self.current += 1
       remain = max(0, self.total - self.current)
       my_text = "Squats left: " + str(remain)
       self.text=my_text


