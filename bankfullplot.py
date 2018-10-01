# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# Import `os` 
import os
import pandas as pd
import matplotlib.pyplot as plt


# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory 
os.chdir("/home/gisele/Desktop")

# List all files and directories in current directory
os.listdir('.')

# Load csv
data = pd.read_csv("bankfull.csv",dtype=str)

# changing values to binary
data.loan[data.loan == 'yes'] = 1 
data.loan[data.loan == 'no'] = 0

# changing values of loan and y columns to binary
data.y[data.y == 'yes'] = 1 
data.y[data.y == 'no'] = 0

# creating columns for job, loan and y
dfobj= pd.DataFrame(data, columns=['job', 'loan', 'y'])
 	
# ploting the  graphs sum

df = dfobj.groupby(['job'])['loan','y'].sum()
plt.figure(figsize=(12, 8))
df.plot.bar()



