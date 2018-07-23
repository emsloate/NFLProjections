#Exploratory Analysis, Gathering Data Together
import numpy as np
import pandas as pd



df_qb_combine = pd.read_csv("Data/QB_combine_data.csv")
df_rb_combine = pd.read_csv("Data/RB_combine_data.csv")
df_wr_combine = pd.read_csv("Data/WR_combine_data.csv")
df_te_combine = pd.read_csv("Data/TE_combine_data.csv")
df_qb_bdays = pd.read_csv("Data/qb_bdays.csv")
df_rb_bdays = pd.read_csv("Data/rb_bdays.csv")
df_wr_bdays = pd.read_csv("Data/wr_bdays.csv")
df_te_bdays = pd.read_csv("Data/te_bdays.csv")