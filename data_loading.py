import pandas as pd
import numpy as np


df_JCT_CICT = pd.read_excel("JCT_CICT.xlsx")    #load JCT-CICT excel data sheet
# print(df_JCT_CICT.head())
# print(len(df_JCT_CICT))

df_JCT_SAGT = pd.read_excel("JCT_SAGT.xlsx")    #load JCT-SAGT excel data sheet
# print(df_JCT_SAGT.head())
# print(len(df_JCT_SAGT))

df_CICT_JCT = pd.read_excel("CICT_JCT.xlsx")     #load CICT-JCT excel data sheet
# print(df_CICT_JCT.head())
# print(len(df_CICT_JCT))

df_CICT_SAGT = pd.read_excel("CICT_SAGT.xlsx")  #load CICT-SAGT excel data sheet
# print(df_CICT_SAGT.head())
# print(len(df_CICT_SAGT))

df_SAGT_JCT = pd.read_excel("SAGT_JCT.xlsx")     #load SAGT-JCT excel data sheet
# print(df_SAGT_JCT.head())
# print(len(df_SAGT_JCT))

df_SAGT_CICT = pd.read_excel("SAGT_CICT.xlsx")      #load SAGT-CICT excel data sheet
# print(df_SAGT_CICT.head())
# print(len(df_SAGT_CICT))

df_JCT_to_Other = pd.read_excel("JCT_to_Other.xlsx")   #load JCT_to_Other data sheet
# print(df_JCT_to_Other.head())
# print(len(df_JCT_to_Other))

df_CICT_to_Other = pd.read_excel("CICT_to_Other.xlsx")   #load CICT_to_Other data sheet
# print(df_CICT_to_Other.head())
# print(len(df_CICT_to_Other))

df_SAGT_to_Other = pd.read_excel("SAGT_to_Other.xlsx")   #load SAGT_to_Other data sheet
# print(df_SAGT_to_Other.head())
# print(len(df_SAGT_to_Other))