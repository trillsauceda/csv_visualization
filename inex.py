#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: <Isaiah Sauceda, Jaime Zeng>
Date: <5/1/17>
Class: CSC 250
Description:
<This program will visualize csv data>
'''
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import sys, numpy as np

plt.style.use('ggplot')

print('INEX: Set data source:')
p_file = sys.stdin.readline().strip()

a_df = pd.read_csv(p_file, encoding = "ISO-8859-1")

print('INEX: What column(s) would you like to summarize?')
cols = sys.stdin.readline().strip()

print('INEX: What type of plot should be generated? (text or graphical)')
graph = sys.stdin.readline().strip()


fig,ax = plt.subplots(figsize=(8,6))
cols = cols.split('|')

if len(cols) == 1:
    if graph.lower() == 'text':
        return None
    
    elif graph.lower() == 'graphical':
        a_df[cols[0]].value_counts().plot(ax=ax, kind='bar')
        
else:
    x, y = cols
    if graph.lower() == 'text':
        return None
    
    elif graph.lower() == 'graphical':
        t_df = a_df[[x.strip(), y.strip()]].groupby(x.strip()).agg(['sum','count'])
        t_df[y.strip()]['sum'] / t_df[y.strip()]['count'].plot(ax=ax, kind='bar')
        
