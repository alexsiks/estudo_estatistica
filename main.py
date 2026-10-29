import pandas as pd
import requests as rq
import glob
import os
import re
import streamlit as st

class BancoDados:
    def __init__(self,path_list):
        self.path_list=path_list
        self.dfs = []

    # Realizar a leitura de todos os arquivos.
    def ler_base_dados(self):
        self.path_list=glob.glob(self.path_list)

        #  Para cada arquivo da lista do Diretório.
        for path in self.path_list:
            df=pd.read_csv(path,sep=";")
            df["arquivo"]=path

            # Adicionar df na lista de dfs.
            self.dfs.append(df)

        return pd.concat(self.dfs,ignore_index=True)

def main():
    # atribuindo ao objeto as propriedades da classe de Banco de dados.
    dados=BancoDados("dados/raw/levantamentos_pavimentada/*.csv")

    # ler a base de dados.
    st.write("Iniciando Aplicação.")

        
if __name__ == "__main__":
    main()
