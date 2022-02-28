#!/usr/bin/env python

# Author: Karanpreet Kaur
# date: 2022-02-28

import numpy as np
import os
import pandas as pd

file_path = os.path.join('./data/raw/', 'athlete_events.csv')

# Read athlete data from raw folder 
try:
    abs_path = os.path.abspath(file_path)
except FileNotFoundError:
    raise ("Absolute path to {input_file} not found in home directory")
else:
    olympic_data = pd.read_csv(abs_path)

# Filter data for olympics happened in and after 2000's
olympic_data_2000 = olympic_data[olympic_data['Year'] >= 2000]
olympic_data_2000 = olympic_data_2000.dropna()
olympic_data_2000['Sex'].replace({'F':'Female', 'M':'Male'}, inplace=True)

# Save olympic_data_2000 in processed folder
output_file_path = os.path.join('./data/processed/', 'athlete_events_2000.csv')
try:
    olympic_data_2000.to_csv(output_file_path, index = False, encoding='utf-8')
except:
    os.makedirs(os.path.dirname(output_file_path))
    olympic_data_2000.to_csv(output_file_path, index = False, encoding='utf-8')