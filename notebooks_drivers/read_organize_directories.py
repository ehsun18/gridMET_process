# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import pandas as pd
import numpy as np
import random
import os, os.path, pickle, sys


import matplotlib
import matplotlib.pyplot as plt

# %%
dpi_, map_dpi_ = 300, 300

# %%
data_base = "/Users/hn/Documents/01_research_data/Ehsan/wheat/Data/"

# %%
file_list = os.listdir(data_base)
file_list = [x for x in file_list if x.endswith("xlsx")]
file_list[:3]

# %%
df = pd.read_excel(data_base + file_list[0])
df.head(3)

# %%
### Check if all files share thew same columns

# %%
# %%time

no_cols = 0

for a_file in file_list:
    df = df = pd.read_excel(data_base + a_file)
    
    if no_cols == 0:
        no_cols = df.shape[1]
        columns_set = set(df.columns)
    else:
        if df.shape[1] != no_cols:
            print (f"{a_file} column count is different")
        
        if columns_set != set(df.columns):
            print (f"{a_file} has different columns")

# %% [markdown]
# #### Good. Now let us read and concatenate all the files.

# %%
all_files = pd.DataFrame()

# Example: read all CSV files in a folder
for a_file in file_list:
    print (a_file)
    df = pd.read_excel(data_base + a_file)
    df['location'] = a_file.replace(".xlsx", "").replace(". ", "_").replace(" ", "_").lower()
    all_files = pd.concat([all_files, df], ignore_index=True)

# %%
# we do not need hour:minute:second:
all_files['date'] = pd.to_datetime(all_files['date']).apply(lambda x: x.date())
all_files.head(2)

# %%
all_files.location.unique()

# %%
all_files.Final_Season.unique()

# %%
sorted(df.columns)

# %%
column_names = {'AEt': "",
                 'DGDD': "",
                 'Dtr': "diurnal_temp_c",
                 'FDD': "freez_dd_c",
                 'Final_Season': "final_season",
                 'GDD_C': "gdd_c",
                 'HDD': "hdd_c",
                 'PDSI': "",
                 'PEt': "",
                 'Pr': "",
                 'PrDtr': "",
                 'RHAvg': "",
                 'RHMax': "",
                 'RHMin': "",
                 'SH': "",
                 'SM': "",
                 'SPEI': "",
                 'SRad': "shortwave_wm2",
                 'Season': "",
                 'Stage': "stage",
                 'TAvg': "",
                 'TMax': "",
                 'TMin': "",
                 'VPD': "",
                 'WD': "",
                 'WS': "",
                 'dap': ""}

# %%
