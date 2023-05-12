# Grelha 6x6 — Solução

Programa que resolve o desafio "Grelha 6x6", proposto pela MathGurl (Inês Guimarães) no
seu [vídeo](https://www.youtube.com/watch?v=N2Lr1NVLGVw), usando uma biblioteca de programação linear.

## Desafio

Preencher todas as células de uma grelha $6 \times 6$ com números inteiros entre $1$ e $8$ de modo que a distância (
vertical + horizontal) entre quaisquer duas células preenchidas com o mesmo número seja maior que esse número.

## Em linguagem matemática

Dados $m$, $n$ e $y$, preencher uma matrix $X$ de dimensões $m\times n$ com inteiros $1\leq x_{ij}\leq k$ de modo que
$\left|i-i'\right|+\left|j-j'\right|\gt x_{ij}$ para todos $(i, j)$ e $(i', j')$ distintos tais que $x_{ij}=x_{i'j'}$.

O objetivo é resolver este problema com $m=n=6$ e $k=8$.

## Modelagem com programação linear inteira

### Problema de minimização (inicialmente não linear)

Podemos tornar o desafio mais interessante se quisermos encontrar uma solução com o menor $y$, isto é, reduzindo o
valor máximo utilizado.

Queremos minimizar $y$ sujeito às restrições:

- $x_{i, j}\geq 1$ para todo $(i, j)$;
- $y\geq x_{i, j}$ para todo $(i, j)$;
- $\left|i-i'\right|+\left|j-j'\right|\gt x_{ij}$ para todos $(i, j)$ e $(i', j')$ tais que $(i, j) \neq (i', j')$ e $`x_
  {ij}=x_{i'j'}`$.

De modo a obter restrições *lineares* correspondentes ao último item, vamos introduzir duas variáveis para cada $(i, j)$
e $(i', j')$ distintos (sem necessidade de repetição):

- $`z_{iji'j'} = \begin{cases} 0, & \text{se } x_{ij} \leq x_{i'j'} \\ 1, & \text{se } x_{ij} \gt x_{i'j'}; \end{cases}`$
- $`w_{iji'j'} = \begin{cases} 0, & \text{se } x_{ij} \geq x_{i'j'} \\ 1, & \text{se } x_{ij} \lt x_{i'j'}.\end{cases}`$

Uma solução trivial do problema (sem considerar o valor máximo) é preencher a grelha com todos os números naturais entre
$1$ e $m\ n$. Logo, podemos considerar apenas soluções em que quaisquer dois valores preenchidos têm diferença inferior
a $m\ n$.

### Transformação para restrições lineares

As seguintes restrições, para todos $(i, j)$ e $(i', j')$, garantem que os valores de $z_{iji'j'}$ e $w_{iji'j'}$ sejam
escolhidos conforme a definição acima:

- $0 \leq z_{iji'j'} \leq 1$;
- $0 \leq w_{iji'j'} \leq 1$;
- $z_{iji'j'} + w_{iji'j'} \leq 1$;
- $x_{ij} + m\ n\ w_{iji'j'} \geq x_{i'j'} + z_{iji'j'}$;
- $x_{ij} - m\ n\ z_{iji'j'} \leq x_{i'j'} - w_{iji'j'}$.

**Demonstração.** Essas restrições garantem que os únicos casos possíveis para $(z_{iji'j'}, w_{iji'j'})$ são $(0, 0)$,
$(0, 1)$ e $(1, 0)$. No primeiro caso, as duas últimas restrições se reduzem a $x_{ij}\geq x_{iji'j'}$ e
$x_{ij}\leq x_{iji'j'}$, garantindo o que pede a definição; no segundo caso, a penúltima restrição é sempre satisfeita
($x_{ij} + m\ n \geq x_{i'j'}$, i.e. $x_{i'j'} - x_{ij} \leq m\ n$),
e a última restrição se reduz a $x_{ij} \leq x_{i'j'} - 1$,
garantindo que $x_{ij}\lt x_{i'j'}$ conforme exigido pela definição; e o último caso é análogo ao anterior,
invertendo-se as desigualdades.

Com isto, podemos reescrever a restrição principal do problema da seguinte maneira:

- $\left|i-i'\right|+\left|j-j'\right| + m\ n\ (z_{iji'j'} + w_{iji'j'}) \gt x_{ij}$ para todos $(i, j)$ e $(i', j')$
  distintos.

**Demonstração.** É imediato que $z_{iji'j'} + w_{iji'j'}=0 \iff z_{iji'j'} = w_{iji'j'}=0 \iff x_{ij}=x_{i'j'}$. Logo,
sempre que essa igualdade ocorre, a restrição acima se reduz a $\left|i-i'\right|+\left|j-j'\right| \gt x_{ij}$, que é
precisamente a condição desejada. Quando a igualdade não ocorre, tem-se $z_{iji'j'} + w_{iji'j'} = 1$, e a restrição
acima equivale a $\left|i-i'\right|+\left|j-j'\right| + m\ n \gt x_{ij}$, o que é sempre verdadeiro porque
$x_{ij} \leq m\ n$ e
$\left|i-i'\right|+\left|j-j'\right|\gt 0$ sempre que $(i, j) \neq (i', j')$; portanto, quando os valores são
diferentes, nenhuma condição é imposta, como esperado.

### O problema de programação linear

Conforme demonstrado acima, o seguinte problema de programação linear modela o desafio em questão:

**Minimizar** $y$

**sujeito a**
$`\begin{cases}
1\leq x_{i, j}\leq y \\
0 \leq z_{iji'j'} \leq 1 \\
0 \leq w_{iji'j'} \leq 1 \\
z_{iji'j'} + w_{iji'j'} \leq 1 \\
x_{ij} + m\ n\ w_{iji'j'} \geq x_{i'j'} + z_{iji'j'} \\
x_{ij} - m\ n\ z_{iji'j'} \leq x_{i'j'} - w_{iji'j'} \\
\left|i-i'\right|+\left|j-j'\right| + m\ n\ (z_{iji'j'} + w_{iji'j'}) \gt x_{ij}
\end{cases}`$

para quaisquer $(i, j)$ e $(i', j')$ distintos, sem necessidade de considerar repetições, com $i$ e $i'$ de $0$ a $m-1$
e $j$ e $j'$ de $0$ a $n - 1$.

### A implementação em Python

O programa [grelha.py](grelha.py) recebe $m$ e $n$ como argumentos (ambos $6$) por padrão e produz uma solução do
desafio com o menor valor máximo possível.

Além do Python 3.10 ou mais recente, a única dependência é o
pacote [OR-Tools](https://developers.google.com/optimization/install) para Python, que faz o
cálculo da solução do problema de programação linear inteira:

```shell
pip install ortools
```

Então, para executar o programa, basta digitar

```shell
python grelha.py 6 6
```

(ou `python3` em vez de `python`, dependendo da instalação) para obter uma solução no terminal.

Convém notar que, como nesta modelagem há $O(m^2 n^2)$ variáveis e restrições, a resposta não é instantânea e pode não
ser obtida se a grelha for muito grande. Porém, para $m = n = 6$, o programa termina em poucos segundos. 
