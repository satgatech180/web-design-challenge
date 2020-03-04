# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:27:23 2020

@author: chris
"""

import pandas as pd

cities_file = "Resources/cities.csv"

cities_data = pd.read_csv(cities_file)

cities_data.head()

html = cities_data.to_html()
print(html)

