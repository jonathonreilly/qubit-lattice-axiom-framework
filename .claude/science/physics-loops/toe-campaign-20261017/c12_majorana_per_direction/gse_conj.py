exec(open('gse_pair2.py').read().split("if __name__ == '__main__':")[0])
import pickle
chosen = pickle.load(open('valid_group_choices.pkl', 'rb'))
def mat(k, eps):
    M = O[k]; P = np.zeros((6, 6), int)
    for d in range(6): P[bk.rotdir(M, d), d] = eps[d]
    return P
c4 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C4'); c3 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C3')
e4, e3 = chosen[0]
gens_ = [mat(c4, e4), mat(c3, e3)]
key = lambda P: tuple(P.flatten())
elems = {key(np.eye(6, dtype=int)): np.eye(6, dtype=int)}; fr = [np.eye(6, dtype=int)]
while fr:
    nf = []
    for A in fr:
        for g in gens_:
            B = g @ A
            if key(B) not in elems: elems[key(B)] = B; nf.append(B)
    fr = nf
print('group order', len(elems))
G, lab, words = gens((0, 0, 0))
seen = set()
for B in elems.values():
    perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
    Mrot = np.zeros((3, 3), int)
    for a in range(3):
        b, s = bk.DIRS[perm[a]]; Mrot[b, a] = s
    kd = bk.kind(Mrot)
    if kd not in ('C2axis', 'C2edge'): continue
    kk = key(Mrot) + (kd,)
    if kk in seen: continue
    seen.add(kk)
    eps = tuple(int(B[perm[d], d]) for d in range(6))
    Rmat = bitmap(Mrot, eps)
    xs = [x for x in itertools.product(range(-2, 3), repeat=3) if 3 <= linf(x, tuple(int(c) for c in Mrot @ np.array(x))) <= 5][:4]
    print(kd, Mrot.tolist(), eps, [(x, pair(G, lab, Mrot, eps, x, Rmat)) for x in xs], flush=True)
