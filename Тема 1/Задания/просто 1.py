from itertools import permutations

table = "12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86"
graph = "AG GA GD DG DE ED DB BD EB BE EH HE GF FG AF FA FH HF HC CH CB BC"

for p in permutations("ABCDEFGH"):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
