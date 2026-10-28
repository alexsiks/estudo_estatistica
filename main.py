import pandas as pd
import requests as rq
import glob
import os
import re
import streamlit as st

class BancoDados:
    def __init__(self,df,path):
        self.df = df    
        self.path = path
    
    def ler_base_dados():
        path_list=glob.glob(f"dados/raw/levantamentos_pavimentada/*.csv")

        dfs=[]
        for path in path_list:
            df=pd.read_csv(path,sep=";")
            df["arquivo"]=path
            dfs.append(df)

        df_combined = pd.concat(dfs,ignore_index=True)
        print(df_combined)