# Variância e Desvio Padrão

## 1. Variância

A **variância** mede o quanto os valores de um conjunto de dados estão dispersos em relação à **média**.

Quanto maior a variância, maior tende a ser a dispersão dos dados.

### Fórmula — População

$$
\sigma^2 = \frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}
$$

Onde:

* $\sigma^2$ = variância
* $x_i$ = cada valor do conjunto de dados
* $\mu$ = média da população
* $N$ = quantidade total de valores

### Fórmula — Amostra

Quando estamos trabalhando com uma **amostra** dos dados:

$$
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
$$

Onde:

* $s^2$ = variância amostral
* $x_i$ = cada valor da amostra
* $\bar{x}$ = média da amostra
* $n$ = quantidade de valores da amostra
* $n-1$ = correção de Bessel

---

## 2. Como calcular a variância manualmente

Considere os valores:

$$
10,\ 12,\ 14,\ 16,\ 18
$$

### Passo 1 — Calcular a média

$$
\bar{x} = \frac{10+12+14+16+18}{5}
$$

$$
\bar{x}=14
$$

### Passo 2 — Calcular a diferença para a média

| Valor | Valor - Média |
| ----: | ------------: |
|    10 |            -4 |
|    12 |            -2 |
|    14 |             0 |
|    16 |             2 |
|    18 |             4 |

### Passo 3 — Elevar as diferenças ao quadrado

| Valor | Diferença | Diferença² |
| ----: | --------: | ---------: |
|    10 |        -4 |         16 |
|    12 |        -2 |          4 |
|    14 |         0 |          0 |
|    16 |         2 |          4 |
|    18 |         4 |         16 |

Somando:

$$
16+4+0+4+16=40
$$

### Passo 4 — Dividir pela quantidade de valores

Considerando que os dados representam uma **população**:

$$
\sigma^2 = \frac{40}{5}
$$

$$
\boxed{\sigma^2=8}
$$

Portanto, a **variância é 8**.

---

# 3. Desvio Padrão

O **desvio padrão** é a raiz quadrada da variância.

$$
\sigma=\sqrt{\sigma^2}
$$

No exemplo anterior:

$$
\sigma=\sqrt{8}
$$

$$
\boxed{\sigma\approx2,83}
$$

Portanto:

* **Variância:** 8
* **Desvio padrão:** 2,83

---

# 4. Qual é a diferença?

A principal diferença é a **unidade de medida**.

### Variância

A variância fica na unidade **ao quadrado**.

Se os dados estão em metros:

$$
m^2
$$

### Desvio padrão

O desvio padrão volta para a **mesma unidade dos dados**.

Se os dados estão em metros:

$$
m
$$

Por isso, o desvio padrão costuma ser mais fácil de interpretar.

---

# 5. Interpretação

Considere:

$$
\text{Média}=14
$$

$$
\text{Desvio padrão}\approx2,83
$$

Isso indica que os valores apresentam uma dispersão em torno da média de aproximadamente **2,83 unidades**, considerando a medida de dispersão pelo desvio padrão.

Uma forma simplificada de visualizar:

$$
14-2,83 \approx 11,17
$$

$$
14+2,83 \approx 16,83
$$

Ou seja, **média ± 1 desvio padrão** corresponde aproximadamente ao intervalo:

$$
[11,17,\ 16,83]
$$

> **Importante:** esse intervalo não significa que todos os valores obrigatoriamente estarão dentro dele. A interpretação probabilística de ±1 desvio padrão depende da distribuição dos dados.

---

# 6. Variância × Desvio Padrão

| Medida        | O que representa                        | Unidade  |
| ------------- | --------------------------------------- | -------- |
| Variância     | Dispersão quadrática em relação à média | Unidade² |
| Desvio padrão | Dispersão na mesma escala dos dados     | Unidade  |

A relação entre eles é:

$$
\boxed{\text{Desvio Padrão}=\sqrt{\text{Variância}}}
$$

e

$$
\boxed{\text{Variância}=(\text{Desvio Padrão})^2}
$$

---

# 7. Em Python

Com `pandas`:

```python
import pandas as pd

dados = pd.Series([10, 12, 14, 16, 18])

# Variância amostral
variancia = dados.var()

# Desvio padrão amostral
desvio_padrao = dados.std()

print("Variância:", variancia)
print("Desvio padrão:", desvio_padrao)
```

Por padrão, o Pandas utiliza:

$$
n-1
$$

ou seja, calcula a **variância e o desvio padrão amostrais**.

Para calcular considerando os dados como uma população:

```python
variancia = dados.var(ddof=0)

desvio_padrao = dados.std(ddof=0)
```

Nesse caso:

```text
Variância = 8
Desvio padrão = 2.8284
```

---

# 8. Resumo

$$
\boxed{\text{Variância}=
\frac{\sum(x_i-\bar{x})^2}{n}}
$$

$$
\boxed{\text{Desvio Padrão}=\sqrt{\text{Variância}}}
$$

**Em resumo:**

> A **variância** mede a dispersão elevando os desvios em relação à média ao quadrado. O **desvio padrão** é a raiz quadrada da variância e retorna a medida para a mesma escala dos dados.
