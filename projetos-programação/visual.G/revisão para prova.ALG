Algoritmo "semnome"
Var
   x,y,resultado : real
   operacao : caractere

funcao soma(a, b:real):real
var
   res: real
Inicio
    res <- a + b
    retorne res
fimfuncao

funcao multiplica(a, b:real): real
var
   res:real
inicio
   res <- a * b
   retorne res
fimfuncao

funcao divide(a, b:real): real
var
   res:real
inicio
   se b <> 0 entao
      res <- a / b
   senao
        escreval("Erro: Divis�o por zero!")
   fimse
   retorne res
fimfuncao

inicio
    escreval("Digite o primeiro n�mero : ")
    leia(x)
    
    escreval("Digite a opera��o que deseja: (+, *, /):")
    leia(operacao)
    
    escreval("Digite o segundo n�mero : ")
    leia(y)
    
    escolha operacao
       caso "+"
           resultado <- soma(x, y)
       caso "*"
           resultado <- multiplica(x, y)
       caso "/"
           resultado <- divide(x, y)
       caso contrario
            escreval("Opera��o invalida!")
    fimescolha

    escreval("Resultado: ", resultado)

Fimalgoritmo