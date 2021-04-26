from copy import deepcopy

class taquin:
  initial_state = [[1,2,3],[8,6,0],[7,5,4]]
  final_state = [[1,2,3],[8,0,4],[7,6,5]]
  core=[]
  def __init__(self):
    self.core == self.initial_state
  def est_etat_final():
    return self.core == self.final_state
tf =[[1,2,3],[8,0,4],[7,6,5]]
t = [[1,2,3],[8,6,0],[7,5,4]]
def permuter(t,c1,c2):
    tperm = deepcopy(t)
    tp=tperm[c2[0]][c2[1]] 
    tperm[c2[0]][c2[1]]=tperm[c1[0]][c1[1]]
    tperm[c1[0]][c1[1]]=tp
    return tperm
def position_case_vide(t):
      for row in range(len(t)):
        for col in range(len(t[row])):
            if t[row][col] == 0 : 
                return (row,col)
def transitions(t) :
    pos=position_case_vide(t)
    tab = []
    if pos[0]>0:
      tab.append((pos[0]-1,pos[1]))
    if pos[1]>0:
      tab.append((pos[0],pos[1]-1))
    if pos[1]<len(t)-1:
      tab.append((pos[0],pos[1]+1))
    if pos[0]<len(t)-1:
      tab.append((pos[0]+1,pos[1]))
    nvmatrice=[]
    for i in tab :
      nvmatrice.append(permuter(t,pos,i))
    return nvmatrice
def afficher_taquin(l):
    for row in l:
      print("-------------")
      print("|",row[0],"|",row[1],"|",row[2],"|")
    print("-------------")
def h(etat, etat_final):
  nb=0
  for i in range(len(etat)):
    for j in range(len(etat[i])):
      if (etat[i][j]!=etat_final[i][j])and (etat[i][j]!=0):
        nb=nb+1
  return nb
def recherche(s,goal):
  niveux = 0
  free_nodes = []
  free_nodes.append(s)
  closed_nodes = []
  success = False
  while (free_nodes!=[]) and (not success) and (niveux < 100):
    first_node = free_nodes[0]
    niveux += 1
    afficher_taquin(first_node)
    free_nodes.remove(first_node)
    closed_nodes.append(first_node)
    generated_states = transitions(first_node)

    for s in generated_states:
      if s == goal:
        success = True
        goal_node = s
    free_nodes = free_nodes + generated_states
    free_nodes.sort(key = lambda el:(niveux+h(el,goal)))

  if niveux == 100:
    print("Recherche non conclussive")
  else:
    print("Recherche finit apres",niveux," iterations")  
taq = taquin()
taquin.core.extend(taquin.initial_state)
recherche(taq.core,taq.final_state)