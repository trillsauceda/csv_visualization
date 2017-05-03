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
    #TEXT: Single column
    if graph.lower() == 'text':
        #Header
        c_label = cols[0]
        print('-' * 45)
        if len(c_label) > 8:
            print('|' + '{:.8}'.format(c_label) + ' |' + ' ' * 32 + ' |')
        else:
            print('|' + '{:^8}'.format(c_label) + ' |' + ' ' * 32 + ' |')
        print('|' + '-' * 43 + '|')
        #Data
        b_series = a_df[cols[0].strip()].value_counts().sort_index()
        MAXVAL = 0
        for col1, col2 in b_series.iteritems():
            if MAXVAL < col2.item():
                MAXVAL = col2
        for col1, col2 in b_series.iteritems():
            reps = ((col2.item() / MAXVAL) * 32)
            print('|' + '{:>8}'.format(col1) + ' |' + '#' * int(reps.item()) + ' ' * (32 - int(reps.item())) + ' |')
        print('-' * 45)
        
    elif graph.lower() == 'graphical':
        a_df[cols[0].strip()].value_counts().sort_index().plot(ax=ax, kind='bar')
        plt.xlabel(cols[0])
        plt.ylabel('counts')
        plt.subplots_adjust(bottom=0.25)
        plt.setp(ax.get_xticklabels(),rotation='horizontal')
        plt.show()
        
else:
    x, y = cols
    #TEXT: Two columns
    if graph.lower() == 'text':
        #Header
        print('-' * 45)
        if len(y.strip()) > 32:
            y = y[32:]
        if len(x.strip()) > 8:
            print('|' + '{:.8}'.format(x) + ' |' + '{:^32}'.format(y) + ' |')
        else:
            print('|' + '{:^8}'.format(x) + ' |' + '{:^32}'.format(y) + ' |')
        print('|' + '-' * 43 + '|')
        #Data
        b_series = a_df[[x.strip(), y.strip()]].groupby(x.strip()).agg(['sum','count'])
        c_series = b_series[y.strip()]['sum'] / b_series[y.strip()]['count']
        MAXVAL = 0
        for col1, col2 in c_series.iteritems():
            if MAXVAL < col2.item():
                MAXVAL = col2
        for col1, col2 in c_series.iteritems():
            reps = ((col2.item() / MAXVAL) * 32)
            print('|' + '{:>8}'.format(col1) + ' |' + '#' * int(reps.item()) + ' ' * (32 - int(reps.item())) + ' |')
        print('|' + '-' * 43 + '|')
    
    elif graph.lower() == 'graphical':
        t_df = a_df[[x.strip(), y.strip()]].groupby(x.strip()).agg(['sum','count'])
        m_df = t_df[y.strip()]['sum'] / t_df[y.strip()]['count']
        m_df.plot(ax=ax, kind='bar')
        plt.xlabel(x.strip())
        plt.ylabel(y.strip())
        plt.subplots_adjust(bottom=0.25)
        plt.setp(ax.get_xticklabels(),rotation='horizontal')
        plt.show()