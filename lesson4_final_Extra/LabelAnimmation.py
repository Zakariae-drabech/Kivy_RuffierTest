# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:52:57 2023

@author: laptop pro
"""

 
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.label import Label


from kivy.uix.boxlayout import BoxLayout


class AnimLabel(Label):
   value = NumericProperty(0) # how many moves have been made
   finished = BooleanProperty(False) # have all the moves been made


   def __init__(self,
               total=10,  steptime=1, autorepeat=True,
               **kwargs):


       super().__init__(**kwargs)


       self.total = total
       self.autorepeat = autorepeat
       self.animation = (Animation(color=(1, 0 , 0, 1),font_size=25, duration=steptime/2)
                       + Animation(color=(1, 0, 0.5, 0.8),font_size=17, duration=steptime/2))
       self.animation.on_progress = self.next


   '''def restart(self, total):
       self.total = total
       self.start()'''


   def start(self):
       self.value = 0
       self.finished = False
       if self.autorepeat:
           self.animation.repeat = True
       self.animation.start(self)


   def next(self, widget, step):
       if step == 1.0:
           self.value += 1
           if self.value >= self.total:
               self.animation.repeat = False
               self.finished = True
