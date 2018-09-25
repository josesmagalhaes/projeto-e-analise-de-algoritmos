def merge(esquerda,direita):#laço para fazer a verificaçao inicial e separaçao.
	resultado = []#vetor para armazenar o resultado.
	i,j = 0, 0
	while i<len(esquerda) and j < len(direita):
		if esquerda[i] <= direita[j]:
			resultado.append(esquerda[i])
			i+=1
		else:
			resultado.append(direita[j])
			j+=1

	resultado += esquerda[i:]#fusao dos resultados
	resultado += direita[j:]#fusao dos resultados
	return resultado


def mergesort(lst):#parte da analise para o caso de combinaçao ordenada.
	if(len(lst) <= 1):
		return lst
	meio = int(len(lst)/2)
	esquerda = mergesort(lst[:meio])
	direita = mergesort(lst[meio:])
	return merge(esquerda,direita)


arr = [23,20,21,28,27,22,25,24,29]
print(mergesort(arr))

#Codigo desenvolvido com carinho e noites de sono perdidas por:
#José de Sousa Magalhaes
#Acadêmico do curso de Sistemas de Informaçao da UFPI.
