grauFun = int(input("Qual o grau da função? "))

if grauFun < 1 or grauFun > 2:
    print("Grau inválido")

elif grauFun == 1:
    print('A equação é do primeiro grau: \n')
    coefAng = float(input("Qual o valor de 'a'? "))

    if coefAng == 0 :
        print("Valor de a inválido")
    else:
        coefLin = float(input("Qual o valor de 'b'? "))

    fun1Solu = (-(coefLin)/coefAng) # .2f
    print(f'{fun1Solu:.2f}')

elif grauFun == 2:
    print("A equação é do segundo grau: \n")
    var_a = float(input("Qual o valor de 'a'? "))
    if var_a == 0 :
        print('Valor de a inválido')
    else:
        var_b = float(input("Qual o valor de 'b'? "))
        var_c = float(input("Qual o valor de 'c'? "))
        fun2Delta = (var_b**2) - (4*var_a*var_c)
        if fun2Delta < 0 :
            print("A equação não possui raízes reais")
        elif fun2Delta == 0 :
            print("A equação possui apenas uma raiz real")
            fun2Raiz = (-(var_b) + fun2Delta**0.5) / (2*var_a)
            print(f'{fun2Raiz:.2f}')
        elif fun2Delta > 0 :
            print("A equação possui duas raízes reais")
            fun2RaizPos = (-(var_b) + fun2Delta**0.5) / (2*var_a)
            fun2RaizNeg = (-(var_b) - fun2Delta**0.5) / (2*var_a)
            if fun2RaizPos > fun2RaizNeg :
                print(fun2RaizNeg, "\n", fun2RaizPos)
            else:
                print(fun2RaizPos, "\n", fun2RaizNeg)