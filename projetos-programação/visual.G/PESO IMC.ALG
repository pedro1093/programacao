Algoritmo "Peso IMC"
// Fa�a umacalculadora que calcule o imc
Var
  m, a, imc:real
Inicio
      escreva("Qual seu peso (Kg): ")
      leia(m)
      escreva("Qual sua altura (m): ")
      leia(a)
      imc <- m / (a ^ 2)
      escreval("Seu IMC �: ", imc:5:2)
      se (imc >= 18.5) e (imc < 25) entao
         escreval("Parab�ns, voc� est� no seu peso ideal!")
      senao
         escreval("Voc� n�o esta na faixa de peso ideal!")
      fimse
      



Fimalgoritmo