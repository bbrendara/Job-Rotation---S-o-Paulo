sequencia=[0,1]
#indices a serem acessados
x=0

#Determinei que a sequencia deve terminar em 20 posições


while(x<=20):
    print("{",*sequencia,"...}")
    valorinfo=int(input("Informe um numero para seguir com a sequencia de Fibonacci:"))
    if valorinfo==sequencia[x]+sequencia[x+1]:
        sequencia.append(valorinfo)
        x=x+1
       
    else:
        print('\n O numero informado não pertence a sequencia, tente novamente.')



