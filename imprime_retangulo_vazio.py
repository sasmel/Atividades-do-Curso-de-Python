largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = 1 
a = 1 #Primeira linha
while a <= altura: #Primeira linha
   print('#' * largura, end = '') #Linha completa
   print() #Nova linha
   a = a + 1 #Sai da primeira linha
   while a > 1 and a < altura: #Começa linha vazada
      print('#' + ' ' * (largura - 2) + '#') #Linha vazada até a penúltima linha
      a = a + 1 #Passa pra nova linha. Quando chegar à última linha, sai do while interno e volta ao while externo imprimindo uma linha cheia.