# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:06:13 2016

@author: 633
"""

import pandas as pd
import re

def readin(filename, encoding = 'gb18030'):
    if(re.match('.txt$', filename)):
        df = pd.read_table(filename, encoding = encoding)
    elif(re.match('.csv$', filename)):
        df = pd.read_csv(filename, encoding = encoding)
    elif(re.match('.xls$', filename) or re.match('.xlsx$', filename)):
        df = pd.read_excel(filename)
    else:
        pass
    return df


is.NULL(re.findall('.txt', 'F:/Django/xz_up/tmpfiles/bac/data1.txt'))
  
pd.read_table('F:/Django/xz_up/tmpfiles/bac/data1.txt')
pd.read_excel('F:/Django/xz_up/test.xlsx')

F:\Django\xz_up
re.compile