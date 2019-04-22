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


Todavia, percebi que havia uma margem de erro na raiz (quando se eleva ela ao quadrado e compara com o número original) que tende de 0 a 0.25 (como observável no gráfico 'projeção (Num x Num-(result^2))'). Isso foi notado no ano passado (2018), continuarei com isso mais a frente.<br><br>

Outro problema encontrado foi também com os números entre 0 e 1, pois, a menor camada seria 1 logo, a raiz de 0.5, por exemplo, seria 0.5/1, ou seja, ele mesmo quando deveria ser 0707106781!
<br><br>
Algebrando um pouco podemos perceber que:
<br>
sqrt(0.5) = sqrt(50)/10
<br>PROBLEMA RESOLVIDO!<br>
<br>
Notei então que, estranhamente, a diferença entre a raíz "canônica" que eu obtive era MUITO menor que nos número que não estavam entre 0 e 1, e, PRONTO, A SOLUÇÃO PRO PEPINO ANTERIOR VEIO-ME!
<br><br>
sqrt(2) = 1.414213562 (CANÔNICO)<br>
sqrt(2) = 1.333333333 (MEU ALGORITIMO)<br>
sqrt(200) = 14.142135624 -> sqrt(2) = 14.142135624/10 (APLICANDO A LÓGICA ANTERIOR)<br><br>

___________________________________________________________________________________________

_Ensaio sobre a precisão dos números_

Quanto maior o número, maior será a precisão da sua raíz (pelo meu método), FATO.<br>
POR QUÊ?<br>
Pois, quanto maior for o número, mais ímpares serão aplicados sobre ele e, quanto maior numerador de uma fração, melhor a sua demonstração do número real desejado, "Quanto mais detalhada a régua, melhor a medição".<br><br>
Exemplo:<br><br>

1/2 ~= 7/12 <br>
0.5 ~= 0.5888888888<br>