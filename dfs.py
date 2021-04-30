from copy import deepcopy


class dfs:
    def __init__(self, labels, values):
        self.values = values
        self.labels = labels
        self.tab = self.values[0]

    def est_etat_final(self, first_node):
        return first_node == self.values[1]

    def numero(self, x, y):
        return self.tab[x][y]

    def afficher_taquin(self, l):
        for row in l:
            print("-------------")
            print("|", row[0], "|", row[1], "|", row[2], "|")
        print("-------------")

    def pos_case_vid(self, first_node):
        for i in range(len(first_node)):
            for j in range(len(first_node[i])):
                if first_node[i][j] == 0:
                    return (i, j)

    def permuter(self, first_node, c1, c2):
        l = deepcopy(first_node)
        l[c1[0]][c1[1]], l[c2[0]][c2[1]] = l[c2[0]][c2[1]], l[c1[0]][c1[1]]
        return l

    def tansition(self, first_node):
        p = self.pos_case_vid(first_node)
        trans = []
        if (p[0] > 0):
            trans.append((p[0]-1, p[1]))
        if (p[0] < len(self.tab)-1):
            trans.append((p[0]+1, p[1]))
        if (p[1] > 0):
            trans.append((p[0], p[1]-1))
        if (p[1] < len(self.tab[1])-1):
            trans.append((p[0], p[1]+1))

        new_pos = []

        for pos in trans:
            new_pos.append(self.permuter(first_node, p, pos))

        return new_pos

    def recherche(self, s, goal):
        niveux = 0
        free_nodes = []
        free_nodes.append(s)
        closed_nodes = []
        success = False
        first_node = []

        while (free_nodes != []) and not(self.est_etat_final(first_node)) and (niveux < 100):

            first_node = free_nodes[0]
            i = 0
            for x in self.labels:
                x["text"] = first_node[i]
                i = i+1
            # print(first_node)
            niveux += 1

            free_nodes.remove(first_node)
            closed_nodes.append(first_node)
            print(self.afficher_taquin(first_node))
            gen_state = self.tansition(first_node)

            generated_states = []

            for x in gen_state:
                if not(x in closed_nodes or x in free_nodes):
                    generated_states.append(x)

            # for s in generated_states:
                # if s == goal:
                    # print("horray")
                    #success = True
                    #goal_node = s

            for x in reversed(generated_states):
                free_nodes.insert(0, x)

        if niveux == 7000:
            print("Recherche non conclussive")
        else:
            print("Recherche finit apres", niveux, " iterations")
        return closed_nodes
