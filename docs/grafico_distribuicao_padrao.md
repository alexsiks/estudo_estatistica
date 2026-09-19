📈 Exemplo — Gráfico de Distribuição Normal
1. Criar os dados

Vamos utilizar um conjunto de valores:

$$ 10,\ 12,\ 14,\ 16,\ 18 $$

Esses valores serão utilizados para encontrar os parâmetros da distribuição.

2. Calcular a média

Primeiro calculamos a média:

$$ \mu = \frac{10+12+14+16+18}{5} $$ $$ \boxed{\mu=14} $$

A média será o centro da distribuição normal.

3. Calcular o desvio padrão

Para esses dados:

$$ \sigma \approx 2,83 $$

Portanto, temos:

Média: 14
Desvio padrão: 2,83
4. Criar o eixo X

Agora precisamos criar vários valores no eixo X.

Por exemplo:

$$ 5,\ 6,\ 7,\ 8,\ ...,\ 22,\ 23 $$

Quanto mais pontos utilizarmos, mais suave ficará a curva.

Uma prática comum é utilizar valores entre:

$$ \mu-4\sigma $$

e

$$ \mu+4\sigma $$

No nosso exemplo:

$$ 14-4(2,83)\approx2,68 $$

e

$$ 14+4(2,83)\approx25,32 $$

Assim, o eixo X pode ficar aproximadamente entre 2,68 e 25,32.

5. Calcular a densidade normal

Para cada valor de X precisamos calcular a altura da curva.

A função da distribuição normal é:

$$ f(x)= \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2} $$

Onde:

$x$ = valor que estamos analisando
$\mu$ = média
$\sigma$ = desvio padrão
$\pi$ = constante matemática
$e$ = número de Euler
6. Entender o cálculo

Imagine que queremos calcular a altura da curva para:

$$ x=14 $$

Como:

$$ \mu=14 $$

temos:

$$ x-\mu=14-14=0 $$

Então:

$$ \frac{x-\mu}{\sigma}=0 $$

Esse ponto está exatamente na média.

Por isso, a curva apresenta seu ponto máximo próximo da média.

7. Repetir para todos os valores de X

O processo é repetido para cada ponto do eixo X:

X
↓
Calcular distância até a média
↓
Dividir pelo desvio padrão
↓
Elevar ao quadrado
↓
Aplicar na fórmula normal
↓
Obter Y

No final teremos pares:

$$ (x,y) $$

Esses pares formarão a curva.

8. Criar a curva

Agora podemos representar os valores:

Y
│
│                    ●
│                 ●     ●
│              ●           ●
│            ●               ●
│          ●                   ●
│       ●                         ●
│____●_____________________________●____ X
       5     10    14    18    23
                    ↑
                  MÉDIA

A média fica no centro da curva.

9. Adicionar a linha da média

Podemos adicionar uma linha vertical em:

$$ x=\mu $$

No exemplo:

$$ x=14 $$

Essa linha mostra exatamente onde está a média.

10. Adicionar o desvio padrão

Também podemos marcar:

-1σ
$$ 14-2,83=11,17 $$
+1σ
$$ 14+2,83=16,83 $$

Então:

       -1σ             MÉDIA             +1σ
        ↓                 ↓                 ↓
───────────────┬──────────┼──────────┬───────────────
             11,17       14        16,83
11. Estrutura final do gráfico

Para um gráfico didático no Plotly, podemos ter:

Curva normal
Linha da média
Linha de -1σ
Linha de +1σ
Eixo X = valores
Eixo Y = densidade de probabilidade

A estrutura lógica fica:

$$ \boxed{ \text{Dados} \rightarrow \text{Média} \rightarrow \text{Desvio Padrão} \rightarrow \text{Eixo X} \rightarrow \text{Distribuição Normal} \rightarrow \text{Gráfico} } $$
🔎 Conceito importante

A curva normal não é criada simplesmente desenhando uma curva em formato de sino.

Primeiro calculamos a densidade normal para cada valor de X. Depois conectamos esses pontos para formar a curva.

Isso é justamente o que permite construir a distribuição normal matematicamente.