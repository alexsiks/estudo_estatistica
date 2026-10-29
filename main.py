import pandas as pd
import requests as rq
import glob
import os
import re


class BancoDados:
    def __init__(self,path_list):
        self.path_list=path_list
        self.df = None
        self.dfs = []
    
    def ler_base_dados(self):
        lista_arquivos=glob.glob(self.path_list)

        
        for caminho in lista_arquivos:
            self.df=pd.read_csv(caminho,sep=";")
            self.df["arquivo"]=caminho
            self.dfs.append(self.df)

        df_combined = pd.concat(self.dfs,ignore_index=True)
        print(df_combined)

if __name__ == "__main__":
    amostras=BancoDados("dados/raw/levantamento_pavimentada/*.csv")
    amostras.ler_base_dados() 