exec(open('part.py').read().split('stat = Counter()')[0])
h0 = H[o0]
os_ = classes[h0]
# hop types of code h0 per direction: representative orderings
types = {}
for a in range(3):
    parts = []
    for o in os_:
        for P in parts:
            if same(P[0], o, a): P.append(o); break
        else: parts.append([o])
    types[a] = parts
def tindex(o, a):
    return next(k for k, P in enumerate(types[a]) if any(same(p, o, a) for p in P[:1]))
stab = [M for M in O if H[bk.rot_order(M, o0)] == h0]
def redge(M, a):
    d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0]); return b, int(d[b]) == -1
# rotation maps hop A^{o}_{(0,a)} to A^{Ro}_{R edge}; edge reversal is fine (A_e is the hop along that edge either way)
act = {}
for M in stab:
    for a in range(3):
        b, rev = redge(M, a)
        act[(bk.kind(M), id(M), a)] = [(b, tindex(bk.rot_order(M, P[0]), b)) for P in types[a]]
for k, v in act.items(): print(k[0], 'dir', k[2], '->', v)
fixed = []
for t in itertools.product(range(6), repeat=3):
    if all(all(act[(bk.kind(M), id(M), a)][t[a]] == (redge(M, a)[0], t[redge(M, a)[0]]) for a in range(3)) for M in stab):
        fixed.append(t)
print('D3-invariant hop-type assignments for copy 0:', fixed)
