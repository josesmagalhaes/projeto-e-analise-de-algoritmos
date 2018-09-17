import math

print("""MINISTÉRIO DA EDUCAÇÃO 
UNIVERSIDADE FEDERAL DO PIAUÍ 
CENTRO DE EDUCAÇÃO ABERTA E A DISTÂNCIA 
CURSO DE SISTEMAS DE INFORMAÇÃO 
PROJETO E ANÁLISE DE ALGORITMOS\n
1ª LISTA DE EXERCÍCIOS DE PROJETO E ANÁLISE DE ALGORITMOS
Desenvolvido por: Jose de Sousa Magalhaes\n""")
#variavel que recebe a opção desejada do usuario.
opcao =0
while (opcao!=9):
    print("MENU\n1. Questao 03\n2. Questao 04\n3. Questao 05\n4. Questao 06\n5. Questao 07\n6. Questao 08\n7. Questão 10\n9. Sair")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao==1):
        #o usuário entra com o valor em microssegundos qu é calculado para gerar cada linha da tabela,
        # conforme seguem os calculos abaixo.
        print("""3.	Para cada função f(n) e cada tempo t na tabela a seguir, determine
    o maior tamanho n de um problema que pode ser resolvido no tempo t,
    supondo-se que o algoritmo para resolver o problema demore f(n) 
    microssegundos. """)

        n = int(input("Insira o valor de N em Microssegundos: "));

        print("Gerando o maior tamanho de n...")
        print("Log n: ", round(math.log10(n), 2))
        print("n: ", n)
        print('n^2: %.2e' % n ** 2)
        print('n^3: %.2e' % n ** 3)
        print('2^n: 2^', n)
    elif (opcao==2):
        print("""4.	Sejam A e B dois algoritmos cujas complexidades são respectivamente
    determinadas pelas funções f(n) e g(n) dadas abaixo. Para cada caso, 
    determine os valores inteiros positivos de n para os quais o
    algoritmo A leve menos tempo para executar do que o algoritmo B. 
    a)	f(n)= 2n² -2 e g(n)= 3n +5 
    b)	f (n) = 3n4 +2n²+1  e g(n) = 4n² + 1\n""")
        #Este dois laços, vão testando valores, ate que A seja mais eficiente que B,
        # e imprime os valores abaxo se for o caso.
        res=int(input("Qual letra deseja fazer?\n1-A\n2-B"))
        if (res==1):
            print("Letra A:")
            print("N |TA(n)|TB(N)")
            for n in range(10):
                f = 2 * (n * n) - 2
                g = 3 * n + 5

                print(n, "|", f, " |", g, " |")
                if (f > g):
                    break
            print("Resposta: n <", n)
        elif(res==2):
            print("Letra B:")
            print("N |TA(n)|TB(N)")
            for n in range(10):
                f = 3 * (n ** 4) + 2 * (n * n) + 1
                g = 4 * (n * n) + 1

                print(n, "|", f, " |", g, " |")
                if (f >= g):
                    print("Resposta: n <", n)
                    break
            print("Resposta: A nunca levará menos tempo que B para n > 0!")
        else:
            print("Estao nao disponivel!")
    elif (opcao==3):
        #Assim como na questão anterior, o algoritmo testa valores até que a soluçao
        #seja atendida e para o programa.
        print("""5.	Suponha que estamos comparando uma implementação do algoritmo
    de ordenação por inserção, com uma implementação do mergesort. O primeiro 
    consome 8n² unidades de tempo quando aplicado a um vetor de comprimento n, 
    segundo consome 64nlog2 n. Para que valores de n o primeiro é mais rápido que
    o segundo? """)
        resp=int(input("Digite 1 para responder: "))
        if (resp== 1):

            n = 1
            print("N | A | B ")
            for n in range(2, 128, n ** 2):

                A = 8 * (n * n)
                B = 64 * n * (math.log2(n))

                print(n, "|", A, " |", round(B, 1), " |")
                if (B < A):
                    print("Até N = ", n-1, " o primeiro é mais rápido que o segundo!")
                    break
        else:
            break
    elif (opcao==4):
        #Com as opçoes 4, 5 e 6 segue a mesma logica. O usuario entra com os valores da constante
        #e numeros naturais suficientemente grandes. o algoritmo checa a condiçao, e imprime o resultado.
        print("6.	É verdade que n² + 2000n +5466 = O(n²)? Justifique. ")
        c= int(input("Digite um valor para a constante C: "))
        ns = int(input("Digite um numero natural: "))
        nzero = (ns * ns) + (2000 * ns) + 5466
        costante = c * (ns ** 2)
        print(nzero)
        print(costante)
        if (nzero<costante):
            print("Sim, pois existem uma constante c >0, tal que para"
            " n suficientemente grande, n² + 2000n +5466 < c.n². \n"
            "Basta escolher c=",c," e n0=",ns," temos que n² + 2000n +5466 <",c,"n², para todo n >=",ns,")")
        else:
            print("Nao, pois não existe uma constante c >0, tal que para n suficientemente grande, n² + 2000n +5466 < c.n²")
    elif (opcao==5):
        print("7.	É verdade que n² - 2000n +5466 = O(n)? Justifique. ")
        c= int(input("Digite um valor para a constante C: "))
        ns = int(input("Digite um numero natural: "))
        nzero = (ns * ns) - (2000 * ns) + 5466
        costante = c * (ns)
        print(nzero)
        print(costante)
        if (nzero<costante):
            print("Sim, pois existem uma constante c >0, tal que para"
            " n suficientemente grande, n² - 2000n +5466 < c.n. \n"
            "Basta escolher c=",c," e n0=",ns," temos que n² - 2000n +5466 < ",c,"n², para todo n >=",ns,")")
        else:
            print("Nao, pois não existe uma constante c >0, tal que para n suficientemente grande, n² - 2000n +5466 < c.n²")
    elif (opcao==6):
        print("8.	É verdade que n4 -99988889n2 +5000008 = O(n3)? Justifique. ")
        c= int(input("Digite um valor para a constante C: "))
        ns = int(input("Digite um numero natural: "))
        nzero = (ns **4) - 99988889 * (ns*ns) + 5000008
        costante = c * (ns**3)
        print(nzero)
        print(costante)
        if (nzero<costante):
            print("Sim, pois existem uma constante c >0, tal que para"
            " n suficientemente grande, n4 -99988889n2 +5000008 < c.n3. \n"
            "Basta escolher c=",c," e n0=",ns," temos que n4 -99988889n2 +5000008 < ",c,"n3, para todo n >=",ns,")")
        else:
            print("Nao, pois não existe uma constante c >0, tal que para n suficientemente grande, n4 -99988889n2 +5000008 < c.n3")
    elif (opcao==7):
        print("10.	Através do Método Mestre, determinar limites assintóticos para as seguintes recorrências. ")
        print("a)	T(n) = 4T(n/2) + n \nb)	T(n) = 4T(n/2) + n² \nc)	T(n) = 7T(n/8) + n² ")
        opcaodez = int(input("Qual questão deseja fazer: \n1-A\n2-B\n3-C"))
        if (opcaodez == 1):
            fn = 2
            n=2
            a=int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            n2=n**(math.log(a,b))
            if (n2>fn):
                print("n → O(n",n,")")
            elif (n2<fn):
                print("n",n," → O(n2)")
            elif (n2==fn):
                print("n → O (n",n,"log n)")
        elif (opcaodez == 2):
            fn = 4
            n=2
            a=int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            n2=n**(math.log(a,b))
            if (n2>fn):
                print("n → O(n",n,")")
            elif (n2<fn):
                print("n",n," → O(n2)")
            elif (n2==fn):
                print("n → O (n",n,"log n)")
        elif (opcaodez == 3):
            fn = 2
            n=2
            a=int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            n2=n**(math.log(a,b))
            if (n2>fn):
                print("n → O(n",n,")")
            elif (n2<fn):
                print("n",n," → O(n2)")
            elif (n2==fn):
                print("n → O (n",n,"log n)")
    elif (opcao==9):
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")
		
#Neste última questão, o algoritmo compara o valor das questões com base no
#que afirma o teorema:
#Se log a/b > c, então, T(n) = O(nloga/b)
#Se log a/b < c, então, T(n) = O(nc)
#Se log a/b = c, então, T(n) = O(nc log n)		
