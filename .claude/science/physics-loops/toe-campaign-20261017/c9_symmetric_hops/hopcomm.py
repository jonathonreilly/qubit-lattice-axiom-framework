exec(open('equiv.py').read().split("if __name__ == '__main__':\n    for t in fixed")[0])
for t in fixed:
    Oj = copy_orders(t)
    z = (0, 0, 0)
    for j in range(4):
        hops = []
        for d in range(6):
            a, s = bk.DIRS[d]
            base = z if s == 1 else tuple(-E[a][i] for i in range(3))
            hops.append(bk.A(base, a, Oj[j][a]))
        tab = [[bk.anti(hops[x], hops[y]) for y in range(6)] for x in range(6)]
        print(t, 'copy', j, 'adjacent-hop anticommutation at a vertex:', tab)
