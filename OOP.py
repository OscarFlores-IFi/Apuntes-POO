# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:10:03 2021

@author: OF
"""

class YourClass(object):
    
    classy = 'class attribute'
    
    def __init__ (self):
        self.classy = 'instance attribute'
        
    def change_classy (self, value):
        self.classy = 'other value'
        
asdf = YourClass()
print(asdf.classy) #instance attribute

asdf.change_classy('other attribute')
print(asdf.classy) #other attribute

del asdf.classy
print(asdf.classy) #class attribute

asdf.classy = 'broken encapsulation attribute'
print(asdf.classy) #broken encapsulation attribute
