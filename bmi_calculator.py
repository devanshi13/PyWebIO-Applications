# -*- coding: utf-8 -*-
"""
Created on Tue May  4 23:36:08 2021

@author: devan
"""

from pywebio.input import*
from pywebio.output import*

def bmi_calculator():
    height = input("Enter your height (in cm)", type=FLOAT)
    weight = input("Enter your weight (in kg)", type=FLOAT)
    
    bmi = weight/(height/100)**2
    
    bmi_output = [(16, 'Severly Underweight'),(18.5, 'Underweight'),(25, 'Normal'),(30, 'Overweight'),(35, 'Moderately obese'),(float('inf'), 'Severly obese')]
    
    for val1,val2 in bmi_output:
        if bmi <= val1:
            put_text('Your BMI is %.2f and you are %s.' %(bmi,val2))
            break;         
    
if __name__ == '__main__':
    bmi_calculator()
