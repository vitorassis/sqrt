# sqrt

O estudo de caso é baseado na premissa de que toda raíz quadrada de um número com raíz perfeita é a soma de n números ímpares consecutivos.

Exemplos:

sqrt(1) = 1 (1) 
sqrt(4) = 2 (1+3)
sqrt(9) = 3 (1+3+5)
sqrt(16) = 4 (1+3+5+7)
...
sqrt(81) = 9 (1+3+5+7+9+11+13+15+17)

e assim sucessivamente.

Tomando o explicado acima como alicerce, indaguei-me: "e os números que não tem raíz certa?"
Pensei na seguinte coisa:

(cada O representa uma unidade, isso seria a representação de um quadrado, repare que a base e a altura deles são exatamente a sua raíz,
 cada X representa uma unidade que poderia estar presente mas não está pois o número não é grande o sufiente.) 

sqrt(4) = 1/1 + 3/3 = 2                      
O  O
__
O |O



mas, quando temos 5, por exemplo, fica:

sqrt(5) ~= 1/1 + 3/3 + 1/5 = 2.2                

O  X   X
_______
O  O  |X
__    |
O |O  |X

(as frações são => espaçosOcupados/ímpar)
