from copy import deepcopy
import time


def estEtatFinal(t, etat_final):
    return etat_final == t


def position_case_vide(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == "0":
                return [i, j]


def numero(t, x, y):
    return t[x][y]


def afficher_taquin(t):
    for row in t:
        print('+++++++++++++')
        print('|', row[0], '|', row[1], '|', row[2], '|')
    print('+++++++++++++')


def permuter(t, c1, c2):
    tperm = deepcopy(t)
    a = tperm[c1[0]][c1[1]]
    tperm[c1[0]][c1[1]] = tperm[c2[0]][c2[1]]
    tperm[c2[0]][c2[1]] = a
    return tperm


def valid(x, y):
    return x > -1 and x < 3 and y > -1 and y < 3


def transitions(t):
    pos = position_case_vide(t)
    tab = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        if(valid(pos[0]+dx[i], pos[1]+dy[i])):
            tab.append([pos[0]+dx[i], pos[1]+dy[i]])
    nvmatrice = []
    for i in tab:
        nvmatrice.append(permuter(t, pos, i))
    return nvmatrice


trace = []
visited = []
success = False


def dfs(node, etat):

    n = 0
    global success
    if (success == False and node not in visited and n < 100):
        n += 1

        trace.append(node)
        if estEtatFinal(node, etat):
            success = True
        visited.append(node)
        tab = transitions(node)
        for w in tab:
            if w not in visited and success == False:
                dfs(w, etat)

    print("Process finished --- %s seconds ---" % (time.time() - start_time))
