Estudo de Estatística

Estudo estatístico sobre as condições de manutenção e conservação do pavimento das rodovias federais brasileiras, utilizando dados disponibilizados pelo Departamento Nacional de Infraestrutura de Transportes (DNIT).

Objetivo

Analisar, por meio de técnicas estatísticas e exploratórias, os dados referentes às condições do pavimento das rodovias federais, buscando identificar padrões, distribuições e diferenças entre as Unidades da Federação (UFs).

Fonte dos dados

Os dados utilizados são provenientes do DNIT — Departamento Nacional de Infraestrutura de Transportes, por meio do conjunto de dados Condições do Pavimento — Levantamentos.

Condições do Pavimento

Os dados apresentam informações por Unidade da Federação (UF) relacionadas ao Índice de Condição da Manutenção (ICM).

O ICM contempla a avaliação das condições de:

manutenção do pavimento;

conservação das rodovias federais.

Período analisado

O estudo utiliza os levantamentos mensais mais recentes disponíveis no conjunto de dados, permitindo a análise da evolução das condições do pavimento ao longo do período selecionado.

Levantamento de agosto de 2026

O conjunto de dados de agosto de 2026 corresponde ao arquivo:

levantamentos_pavimentada_2026_08.csv

Estrutura dos dados

Os dados são organizados por Unidade da Federação e contêm informações relacionadas às condições do pavimento e aos indicadores utilizados na avaliação da manutenção e conservação das rodovias.

O arquivo é disponibilizado em formato CSV, com separador ;.

Análise estatística

A análise poderá contemplar:

estatística descritiva;

distribuição dos dados;

medidas de tendência central;

medidas de dispersão;

comparação entre UFs;

identificação de padrões e possíveis outliers;

análise temporal dos indicadores;

visualização gráfica dos resultados.

Tecnologias utilizadas

Python

Pandas

NumPy

Matplotlib

Seaborn

Jupyter Notebook

Estrutura do projeto
estudo_estatistica/
│
├── dados/
│   └── raw/
│       └── levantamentos_pavimentada/
│           └── *.csv
│
├── notebooks/
│   └── *.ipynb
│
├── src/
│   └── *.py
│
├── README.md
└── requirements.txt

Objetivo do estudo

O projeto busca aplicar conceitos de estatística à análise de dados reais de infraestrutura rodoviária, utilizando os indicadores de condição do pavimento para compreender as características dos dados e as diferenças observadas entre as Unidades da Federação.

Fonte

Departamento Nacional de Infraestrutura de Transportes — DNIT

Conjunto de dados: Condições do Pavimento — Levantamentos