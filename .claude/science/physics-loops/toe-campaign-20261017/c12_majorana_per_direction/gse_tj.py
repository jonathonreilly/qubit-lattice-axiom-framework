exec(open('gse.py').read().split("if __name__ == '__main__':")[0])
MAJ = list(range(6))
# (a) statistics: straight legs of edge operators, Levin-Wen sign over the 20 triples of directions
def leg(d, nsteps=2):
    a, s = DIRS[d]; v = (0, 0, 0); ws = []
    for _ in range(nsteps):
        if s == 1: base = v; v = tuple(v[i] + E[a][i] for i in range(3))
        else: v = tuple(v[i] - E[a][i] for i in range(3)); base = v
        ws += edge_word(base, a)
    return word(ws)
om = lambda P, Q: int((P[0].astype(int) @ Q[1].astype(int) + P[1].astype(int) @ Q[0].astype(int)) % 2)
legs = [leg(d) for d in range(6)]
G0, lab0, words0 = gens((0, 0, 0))
# legs must commute with all plaquettes and flip only B at the ends
Bs = [g for g, l in zip(G0, lab0) if l[0] == 'B']; Ss = [g for g, l in zip(G0, lab0) if l[0] == 'S']
print('legs commute with all plaquettes:', all(om(lg, s) == 0 for lg in legs for s in Ss),
      ' flip exactly 2 vertex terms:', all(sum(om(lg, b) for b in Bs) == 2 for lg in legs))
tj = Counter((-1) ** (om(legs[a], legs[b]) + om(legs[b], legs[c]) + om(legs[a], legs[c])) for a, b, c in itertools.combinations(range(6), 3))
print('T-junction signs over 20 triples:', dict(tj), flush=True)
