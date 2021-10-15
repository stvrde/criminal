from collections import deque

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  path=[]
  q = deque(start)
  while q:
    v = q.popleft()
    path.append(v)
    q.extend(w for w in graph[v] if w not in q and w not in path)
    #print (q, path)
  
  return sorted(path) 

def radi_male(clan,novi):

  noviji={}
  for c in clan:
    noviji[c]=novi[c]
  return noviji
def nesto(graph): 

    povezani=[]
    duljine=[]
    novi={}
    noviji={}
    for i in graph:
      if iterative_bfs(graph, graph[i]) not in povezani:
        povezani.append(iterative_bfs(graph, graph[i]))
        duljine.append(len(iterative_bfs(graph, graph[i])))
      novi[i]=len(graph[i])
    print(povezani,"ovo su povezane grupe u grafu")
    print(duljine)
    """
    #ovo radi listu dictionariya koja ce nan tribat za zadnji korak izracunavanja randoma
    mozda stavit sve u neku funkciju da bude bolje
    vjerojatno ako su ove dvi liste jednake moze se zakljucit da je ista skupina ljudi
    """
    nekalista=[]
    for clan in povezani:
      #print(radi_male(clan))
      my_dict2={}
      #ovo je za okrenit i napravit dict koji nam triba za racunat aliase
      for k,v in radi_male(clan,novi).items(): 
          my_dict2[v]= my_dict2.get(v,[])
          my_dict2[v].append(k)
      nekalista.append(my_dict2)
      #print(my_dict2)
    return nekalista,povezani,duljine



def first(str1,str2):
    if len(str1)!=len(str2):
        return -1
    nova=[]
    ime=[]
    for s in str1:
        s=s.split()
        nova.extend(s)
        ime.append(s)
    #print(nova)
    #print(ime)
    ljudi=list(set(nova))
    #print(ljudi)
    nova2=[]
    ime2=[]
    for s in str2:
        s=s.split()
        nova2.extend(s)
        ime2.append(s)
    #print(nova2)
    ljudi2=list(set(nova2))
    #print(ljudi2)
    if len(ljudi)!=len(ljudi2):
        return -1
    print("sve pet")
    print(novi_dic(ljudi2,ime2),"novi dic")
    #print(novi_dic(ljudi,ime))
    prvi=novi_dic(ljudi,ime)
    drugi=novi_dic(ljudi2,ime2)
    """
    ode dobijemo dvi konacne liste iz kojih ocitavamo kombele
    """
    print(nesto(prvi))
    print(nesto(drugi))
    data,veze,dlina1=nesto(prvi)
    field,veze2,dlina2=nesto(drugi)
    print(data,"\n",field)
    #dul i dulf je u biti len od svakog kljuca
    dul=[]
    dulf=[]
    for dat in data:
        for d in dat:
            dul.append(len(dat[d]))
    for fie in field:
        for f in fie:
            dulf.append(len(fie[f]))
    print(dul,"dul")
    print(dulf,"dulf")
    #ovo ako je svaki veci od 1 samo vrati sumu i imamo sve kombele
    print(sum(dul))

    #nakon ove provjere samo triba jos nac sve aliase
    if sorted(dlina1)==sorted(dlina2) and sorted(dul)==sorted(dulf):
        suma=0
        for index, dic in enumerate(data):
            print(dic)
            for k, v in dic.items():
                if len(v) == 1:
                    if data[index][k] == field[index][k]:
                        #print(data[index][k], field[index][k])
                        #print("ovo vridi 0")
                        suma+=0
                    else:
                        #print(data[index][k], field[index][k])
                        #print("ovo vridi 1")
                        suma+=1
                else:
                    suma+=int(len(v))
        print(suma)
            
    else:
        return -1


def novi_dic(ljudi,ime):
    dica={}
    for k in ljudi:
        for l in ime:
            if k in l:
             
                if k in dica:
                    dica[k].extend(l[:])

                else:

                    dica[k]=l[:]

    for s in dica:
        dica[s]=list(set(dica[s]))
    for key,value in dica.items():
        if key in value:

            value.remove(key)

    #print(dica,"dica iz novi")
    lista_indexa=[]
    for i,v in dica.items():
        lista_indexa.append(len(v))

    return dica  

def main():

    str1=["A B","A C","AA BB","AA CC","AA DD"]
    str2=["A B","A C","AA BB","AA CC","AA DD"]
    print(first(str1,str2),"first")

if __name__=='__main__':
    main()