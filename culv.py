# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:03:30 2020

@author: karakusb
"""
import subprocess
batFile=r'C:\Projects\culv5\culv5.bat'
result=r'C:\Projects\culv5\Examples\example9.lis'
subprocess.call([batFile])

import pandas as pd

df=pd.read_csv(result)