# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:30:33 2023

@author: User
"""
from statistics import median
from math import isnan
from itertools import filterfalse

data = [20.7, float('NaN'),19.2, 18.3, float('NaN'), 14.4]
sorted(data)  # This has surprising behavior

print(median(data))  # This result is unexpected


print(sum(map(isnan, data)))    # Number of missing values
clean = list(filterfalse(isnan, data))  # Strip NaN values
print(clean)

sorted(clean)  # Sorting now works as expected

print(median(clean))       # This result is now well defined
