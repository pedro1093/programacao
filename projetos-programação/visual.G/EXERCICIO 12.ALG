Algoritmo "semnome"
//
//

Var
peso,op,resul:real

inicio
escreval(" Digite o peso:")
leia(peso)
escreval(" Digite forma de compara��o de peso: 1 para peso em Mercurio, 2 para peso em V�nus, 3 para peso em Marte, 4 para peso em J�piter, 5 para peso em Saturno e 6 para peso em Urano ")
leia (op)
escolha op
     caso 1
     resul <- (peso/10*0.37)
           escreval(" O peso ficara de ", resul, " na gravidade de mercurio ")
     caso 2
     resul <- (peso/10*0.88)
           escreval(" O peso ficara em ", resul, " na gravidade de V�nus ")
     caso 3
     resul <- (peso/10*0.38)
           escreval(" O peso ficara em ", resul, " na gvidade de Marte ")
     caso 4
     resul <- (peso/10*2.64)
           escreval(" O peso ficara de ", resul, " na gravidade de Jup�ter ")
     caso 5
     resul <- (peso/10*1.15)
           escreval(" O peso ficara de ", resul, " na gravidade de Saturno ")
     caso 6
     resul <- (peso/10*1.17)
           escreval(" O peso ficara de ", resul, " na gravidade de Urano ")
     outrocaso
           escreval (" digite uma forma de peso valida! " )
fimescolha

Fimalgoritmo