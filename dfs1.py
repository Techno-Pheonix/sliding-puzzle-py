class dfs:
    etat_initial = [[3, 2, 7], [8, 6, 0], [1, 5, 4]]

    def estEtatFinal(self, t, etat_final):
        return etat_final == t

    def position_case_vide(self, t):
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == 0:
                    return [i, j]

    def numero(self, t, x, y):
        return t[x][y]

    def afficher_taquin(self, t):
        for row in t:
            print('+++++++++++++')
            print('|', row[0], '|', row[1], '|', row[2], '|')
            print('+++++++++++++')
        from copy import deepcopy

    def permuter(self, t, c1, c2):
        tperm = deepcopy(t)
        a = tperm[c1[0]][c1[1]]
        tperm[c1[0]][c1[1]] = tperm[c2[0]][c2[1]]
        tperm[c2[0]][c2[1]] = a
        return tperm

    def valid(self, x, y):
        return x > -1 and x < 3 and y > -1 and y < 3

    def transitions(self, t):
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

    def recherche(self, node, etat):
        trace = []
        visited = []
        global success
        success = False

        if (success == False and node not in visited):
            trace.append(node)
            i = 0
            for x in self.labels:
                if (node[i//3][i % 3] == "0"):
                    x["fg"] = "white"
                else:
                    x["fg"] = "black"
                x["text"] = node[i//3][i % 3]
                i = i+1
            if estEtatFinal(node, etat):
                success = True
            visited.append(node)
            tab = transitions(node)
            for w in tab:
                if w not in visited and success == False:
                    self.dfs(w, etat)
