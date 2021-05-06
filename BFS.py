from copy import deepcopy
import time


class bfs:
    def __init__(self, labels, values):
        self.values = values
        self.labels = labels
        self.tab = self.values[0]

    def est_etat_final(self, first_node):
        return first_node == self.values[1]

    def pos_case_vid(self, first_node):
        for i in range(len(first_node)):
            for j in range(len(first_node[i])):
                if first_node[i][j] == "0":
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

    def recherche(self, s, goal, label, label_1):
        start_time = time.time()
        niveux = 0
        free_nodes = []
        free_nodes.append(s)
        closed_nodes = []
        success = False
        first_node = []

        while (free_nodes != []) and not(self.est_etat_final(first_node)) and (niveux < 100):
            niveux += 1
            first_node = free_nodes[0]
            i = 0
            for x in self.labels:
                if (first_node[i//3][i % 3] == "0"):
                    x["fg"] = "white"
                else:
                    x["fg"] = "black"
                x["text"] = first_node[i//3][i % 3]
                i = i+1

            free_nodes.remove(first_node)
            closed_nodes.append(first_node)
            gen_state = self.tansition(first_node)

            generated_states = []

            for x in gen_state:
                if not(x in closed_nodes or x in free_nodes):
                    generated_states.append(x)

            free_nodes.extend(generated_states)
        if (self.est_etat_final(first_node)):
            label["text"] = "Sucess"
        else:
            label["text"] = "Failure"
            label["fg"] = "red"

        print("Process finished --- %s seconds ---" %
              (time.time() - start_time))
        label_1["text"] = time.time() - start_time
        return closed_nodes
