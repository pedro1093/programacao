Algoritmo "Est� apto a dirigir?"
//  Cria um algoritmo para descobrir a idade
//  Se idade for maior que 18 esta apto a dirigir caso contrario n�o
Var
   a, an, idade: inteiro
Inicio
   escreva("Ano de nascimento: ")
   leia(a)
   escreva("Ano atual: ")
   leia(an)
   idade <- (an - a)
   se (idade >= 18) entao
      escreval("Voc� esta apto a dirigir")
   senao
      escreval("Voc� n�o pode dirigir um carro!")
   fimse
Fimalgoritmo