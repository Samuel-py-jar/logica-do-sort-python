#Raís do Código
#Root of the code
#lista.sort()
#list.sort()
#maybe that's the sort command to put in numerical order
#Talvez pareça assim o comando sort para colocar em ordem numérica na lista.
def ordenar(lista = [],como=">d"):
  lista2 = []
  fim = 0
  cont= len(lista)
  while True:
    fim += 1
    for i in range(0,len(lista)):
        if como == "help":
            return "<c : crescente\n>d : decrescente\nhelp : ajuda"
        elif como == ">d":
                if i == 0:
                    menor = lista[i]
                if menor < lista[i]:
                    menor = lista[i]
                if i == len(lista)-1:
                    lista2.append(menor)
                    lista.remove(menor)    
        else:
            if i == 0:
                menor = lista[i]
            if menor > lista[i]:
                menor = lista[i]
            if i == len(lista)-1:
                lista2.append(menor)
                lista.remove(menor)
      
    if fim == cont:
        return lista2
        break

            