import pandas as pd
import glob
import streamlit as st
import plotly.express as px

class BancoDados:

    def __init__(self, path_list):
        self.path_list = path_list
        self.dfs = []

    def ler_base_dados(self):
        arquivos = glob.glob(self.path_list)

        self.dfs = [
            pd.read_csv(path, sep=";").assign(arquivo=path)
            for path in arquivos
        ]

        if not self.dfs:
            return pd.DataFrame()

        return pd.concat(self.dfs, ignore_index=True)

class Grafico:

    def __init__(self,df):
        self.df = df

    def barras(self,x,y,titulo):
        st.bar_chart(self.df, x=x, y=y, title=titulo)

class App:

    def __init__(self):
        st.set_page_config(
            page_title="Leitura de Dados",
            layout="wide"
        )

        self.banco = BancoDados(
            "dados/raw/levantamentos_pavimentada/*.csv"
        )
        self.grafico = Grafico(self.banco.ler_base_dados())

    def executar(self):
        st.title("Leitura de Bases de Dados")
        st.write("Iniciando aplicação.")

        df = self.banco.ler_base_dados()


        if df.empty:
            st.warning("Nenhum arquivo CSV encontrado.")
            return

        st.subheader("Prévia dos dados")
        st.dataframe(df.head(10), use_container_width=True)

        st.subheader("Informações da base")
        st.metric("Total de registros", f"{len(df):,}")
        st.metric("Total de colunas", len(df.columns))

        st.subheader("Colunas disponíveis")
        st.write(df.columns.tolist())


if __name__ == "__main__":
    app = App()
    app.executar()