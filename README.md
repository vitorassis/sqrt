# Square Root - _LAYER METHOD_

I developed this study based on the logic that every integer square root is the sum of n sequential odd numbers.

The name was given because of the format the square gets: layers, from inside to outside, no spoilers, there will be examples below.

-- We can represent squares graphicaly (samples after it) and they will measure n per side, that is exactly the n odd numbers.

Examples:<br><br>

sqrt(1) = 1 (1) <br>
sqrt(4) = 2 (1+3)<br>
sqrt(9) = 3 (1+3+5)<br>
sqrt(16) = 4 (1+3+5+7)<br>
...<br>
sqrt(81) = 9 (1+3+5+7+9+11+13+15+17)<br>

And it goes to infinity.<br>

Using the above as our base, I was thinking: "and what about the numbers those don't have an integer root?"<br>
Then I built this:<br>
 <br><br>
 <table>
  <thead>
   <th colspan=2>
    Subtitles
   </th>
  </thead>
  <tbody>
   <tr><td>O</td><td>Used unity slot</td></tr>
   <tr><td>X</td><td>Empty unity slot</td></tr>
  </tbody>
 </table>

 -- See the squares! There're layers!! ^_^

sqrt(4) = 1/1 + 3/3 = 2                      <br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sq4.PNG'>

but, when we have 5 or 20, for example, it become:<br><br>

sqrt(5) ~= 1/1 + 3/3 + 1/5 = 2.2                <br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sqr5.png'>
<br><br>
sqrt(20) ~= 1/1 + 3/3 + 5/5 + 7/7 + 4/9 = 4.4444444444444<br>
<img src='https://raw.githubusercontent.com/vitorassis/sqrt/master/imgs/sq20.png'>
<br><br>
(the divisions are => UsedUnitySlots/odd)<br>

However, I saw that there was a considerable error in result (when you multiplies the resultant number itself and compare with original) which floats between 0 and 0.25 (as you can see in 'projeção (Num x Num-(result^2))'). I percepted that last year (2018), I'll continue with this problem after.<br><br>

Other trouble I found was either with numbers between 0 and 1, beacause the last layers is 1, so, the square root of 0.5 would be 0.5/1 = 0.5, but the correct is 0.707106781!
<br><br>

Calculating a little bit we can see that:
<br>
sqrt(0.5) = sqrt(0.5 * 100)/10
<br>PROBLEM SOLVED!<br>
<br>
Then I saw that, weirdly, the difference between the "canonical" root and the one I got were PRETTY lower than for the number outside this interval, so, I'ts finished, I FOUND THE SOLUTION FOR THE PREVIOUS PROBLEM!
<br><br>
sqrt(2) = 1.414213562 (CANONICAL)<br>
sqrt(2) = 1.333333333 (MY ALGORYTHM)<br>
sqrt(200) = 14.142135624 -> sqrt(2) = 14.142135624/10 (APPLYING THE LOGIC ABOVE)<br><br>

___________________________________________________________________________________________

_Thinking about number's precision_

How big the number is, bigger will be it's root precision either (using my method), FACT.<br>
BUT, WHY?<br>
Because a big odd means more slots to be filled. "Increasing the ruler we increase the measurement".<br><br>
Samples:<br><br>

1/2 ~= 7/12 <br>
0.5 ~= 0.5888888888<br>
___________________________________________________________________________________________

_HOW TO IMPLEMENT THIS CODE?_

Clone this repository, move ```sqrt.py``` to your project directory, then:
<br><br>
```
   from sqrt import sqrt
   ...
   root = sqrt(num)
```
<br><br>
___________________________________________________________________________________________<br>
THANK YOU

I'm thankful for your attention, questions, critics or suggestions, call me:vitor.a.camargo0209@gmail.com ;)

___________________________________________________________________________________________
___________________________________________________________________________________________

# Raiz Quadrada - _MÉTODO DE CAMADAS_

O estudo que desenvolvi é baseado na premissa de que toda raíz quadrada de um número com raíz inteira é a soma de n números ímpares consecutivos.

O nome dado ao método deve-se à construção de quadrados por camadas, de dentro pra fora, sem spoilers, tem exemplos sobre isso abaixo.

-- Podemos representar os quadrados graficamente (exemplos mais abaixo) de modo que terão lado n, que coincide com os n números ímpares. 
<br>
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

 -- Observe os quadrados, eis as camadas ^_^

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

___________________________________________________________________________________________

_COMO IMPLEMENTAR O ALGORITMO?_<br><br>

Clone o repositório, mova o sqrt.py para o diretório do seu projeto, ai então use:
<br><br>
```
   from sqrt import sqrt
   ...
   root = sqrt(num)
```


_________________________________________________________________________________________

_OBRIGADO_

Obrigado pela atenção, duvidas, críticas ou sugestões, contacte-me: vitor.a.camargo0209@gmail.com
;)
