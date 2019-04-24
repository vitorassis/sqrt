# sqrt - _MÉTODO DE CAMADAS_

O estudo de caso é baseado na premissa de que toda raíz quadrada de um número com raíz perfeita é a soma de n números ímpares consecutivos.

O nome dado ao método deve-se à construção de quadrados por camadas, de dentro pra fora, sem spoilers, tem mais exemplossobre isso abaixo

-- Podemos representar os quadrados graficamente (exemplos mais abaixo) , de modo que terão lado n, que coincide com os n números ímpares. 

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
 <br><br>
 <table>
  <thead>
   <th colspan=2>
    Legendas
   </th>
  </thead>
  <tbody>
   <tr><td>O</td><td>Unidade preenchida</td></tr>
   <tr><td>X</td><td>Unidade vaga</td></tr>
  </tbody>
 </table>

sqrt(4) = 1/1 + 3/3 = 2                      <br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sq4.PNG'>


mas, quando temos 5 ou 20, por exemplo, fica:<br><br>

sqrt(5) ~= 1/1 + 3/3 + 1/5 = 2.2                <br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sqr5.png'>
<br><br>
sqrt(20) ~= 1/1 + 3/3 + 5/5 + 7/7 + 4/9 = 4.4444444444444<br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sq20.png'>
<br><br>
(as frações são => espaçosOcupados/ímpar)<br>


Todavia, percebi que havia uma margem de erro na raiz (quando se eleva ela ao quadrado e compara com o número original) que tende de 0 a 0.25 (como observável no gráfico 'projeção (Num x Num-(result^2))'). Isso foi notado no ano passado (2018), continuarei com isso mais a frente.<br><br>

Outro problema encontrado foi também com os números entre 0 e 1, pois, a menor camada seria 1 logo, a raiz de 0.5, por exemplo, seria 0.5/1, ou seja, ele mesmo quando deveria ser 0.707106781!
<br><br>
Algebrando um pouco podemos perceber que:
<br>
sqrt(0.5) = sqrt(0.5 * 100)/10
<br>PROBLEMA RESOLVIDO!<br>
<br>
Notei então que, estranhamente, a diferença entre a raíz "canônica" que eu obtive era MUITO menor que nos número que não estavam entre 0 e 1, e, PRONTO, A SOLUÇÃO PRO PEPINO ANTERIOR VEIO-ME!
<br><br>
sqrt(2) = 1.414213562 (CANÔNICO)<br>
sqrt(2) = 1.333333333 (MEU ALGORITMO)<br>
sqrt(200) = 14.142135624 -> sqrt(2) = 14.142135624/10 (APLICANDO A LÓGICA ANTERIOR)<br><br>

___________________________________________________________________________________________

_Ensaio sobre a precisão dos números_

Quanto maior o número, maior será a precisão da sua raíz (pelo meu método), FATO.<br>
POR QUÊ?<br>
Pois, quanto maior for o número, mais ímpares serão aplicados sobre ele e, quanto maior numerador de uma fração, melhor a sua demonstração do número real desejado, "Quanto mais detalhada a régua, melhor a medição".<br><br>
Exemplo:<br><br>

1/2 ~= 7/12 <br>
0.5 ~= 0.5888888888<br>
