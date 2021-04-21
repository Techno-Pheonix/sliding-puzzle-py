from copy import deepcopy;

def permuter (t, c1, c2):
  x=t[c1[0]][c1[1]]
  t[c1[0]][c1[1]]=t[c2[0]][c2[1]]
  t[c2[0]][c2[1]]=x
  return t
def transitions(t):
  tab=[]
  x,y=position_case_vide(t)
  l=[]
  if(x-1>=0):
    l.append(((x-1),y))

  if(y-1>=0):
    l.append((x,(y-1)))


  if(x+1<3):
    l.append(((x+1),y))

  if(y+1<3):
    l.append((x,(y+1)))
  for i in range(len(l)):
    t1=deepcopy(t)
    tab.append(permuter(t1,position_case_vide(t1),l[i]))
  return tab
def recherche(t,goal,depthfirst):
  freenodes=[t]
  closednodes=[]
  goalnodes=[]
  generatedStates=[]
  success=False
  n=0
  while (len(freenodes)>0) and (not success) and (n<10) :
    n=n+1
    firstNode=freenodes[0]
    del freenodes[0]
    #for i in freenodes:
      #affiche_taquin(i)

    closednodes.append(firstNode)
    generatedStates=transitions(firstNode)

    for j in generatedStates:
      if ((j in freenodes) or (j in closednodes)):
        del generatedStates[generatedStates.index(j)]


      print("fi west for mta3 generated")

    for s in generatedStates:
      if etat_final(s):
        success=True
        goalnodes.append(s)
        affiche_taquin(s)
      print("fi west for mta3 s mta3 generated")

    if depthfirst==True:
      freenodes=generatedStates +freenodes
    else:
      freenodes=freenodes+generatedStates

    for i in generatedStates:
      affiche_taquin(i)

    print("amel doura fil while ")
