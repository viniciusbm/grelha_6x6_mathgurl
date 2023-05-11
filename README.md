# Grelha 6x6 - Solução

Programa que resolve o desafio "Grelha 6x6", proposto pela MathGurl em seu [vídeo](https://www.youtube.com/watch?v=N2Lr1NVLGVw), usando uma biblioteca de programação linear.

## Problema

Preencher todas as células de uma grelha $6 \times 6$ com números inteiros entre $1$ e $8$ de modo que a distância (vertical + horizontal) entre quaisquer duas células preenchidas com o mesmo número seja maior que esse número. 

## Em linguagem matemática

Dados $m$, $n$ e $y$, preencher uma matrix $X$ de dimensões $m\times n$ com inteiros $1\leq x_{ij}\leq k$ de modo que $\left|i-i'\right|+\left|j-j'\right|\gt x_{ij}$ para todos $(i, j)$ e $(i', j')$ distintos tais que $x_{ij}=x_{i'j'}$.

O objetivo é resolver este problema com $m=n=6$ e $k=8$.

## Modelagem com programação linear inteira

Podemos tornar o problema mais interessante se quisermos encontrar uma solução com o menor $y$, isto é, reduzindo o valor máximo utilizado. 

