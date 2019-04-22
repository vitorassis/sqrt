# sqrt

O estudo de caso é baseado na premissa de que toda raíz quadrada de um número com raíz perfeita é a soma de n números ímpares consecutivos.

Exemplos:<br><br>

sqrt(1) = 1 (1) <br>
sqrt(4) = 2 (1+3)<br>
sqrt(9) = 3 (1+3+5)<br>
sqrt(16) = 4 (1+3+5+7)<br>
...<br>
sqrt(81) = 9 (1+3+5+7+9+11+13+15+17)<br>

e assim sucessivamente.<br>

Tomando o explicado acima como alicerce, indaguei-me: "e os números que não tem raíz certa?"<br>
Pensei na seguinte coisa:<br>

(cada O representa uma unidade, isso seria a representação de um quadrado, repare que a base e a altura deles são exatamente a sua raíz,
 cada X representa uma unidade que poderia estar presente mas não está pois o número não é grande o sufiente.) <br><br>

sqrt(4) = 1/1 + 3/3 = 2                      <br>
O  O<br>
__<br>
O |O<br>
<br><br>


mas, quando temos 5, por exemplo, fica:<br><br>

sqrt(5) ~= 1/1 + 3/3 + 1/5 = 2.2                <br>

O  X   X<br>
_______<br>
O  O  |X<br>
__    <br>
O |O  |X<br><br>

(as frações são => espaçosOcupados/ímpar)<br>
