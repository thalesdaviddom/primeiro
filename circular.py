# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:28:53 2020

@author: thale
"""

def circular(amigo_de):
    É_circular = False
    var = True
    a = 0
    i = 0
    while var:
        a = amigo_de[a]
        i += 1
        if a == 0:
            var = False
    if i == len(amigo_de):
        É_circular = True
    return É_circular
circular([0,1,2,3,4,5])