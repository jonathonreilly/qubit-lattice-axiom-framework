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
# (b) O-invariance with on-site signed Majorana permutations: gamma_{v,d} -> eps(d) gamma_{Mv, Rd}
def image_word(ws, M, eps):
    sgn = 1; out = []
    for (v, d) in ws:
        sgn *= eps[d]; out.append((tuple(int(x) for x in M @ np.array(v)), bk.rotdir(M, d)))
    return sgn, out
def image_gen(g, ws, M, eps):
    base = word(ws); kadj = (g[2] - base[2]) % 4
    sgn, out = image_word(ws, M, eps)
    P = word(out); return [P[0], P[1], (P[2] + kadj + (0 if sgn == 1 else 2)) % 4]
def perm_sign(p):
    p = list(p); s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s
res = Counter(); good_eps = {}
for sec in ((0, 0, 0), (1, 1, 1)):
    G, lab, words = gens(sec)
    Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
    for k, M in enumerate(O):
        pi = [bk.rotdir(M, d) for d in range(6)]
        ok_eps = []
        for eps in itertools.product((1, -1), repeat=6):
            if np.prod(eps) != perm_sign(pi): continue        # preserve B (det +1)
            imgs = [image_gen(g, ws, M, eps) for g, ws in zip(G, words)]
            W, okk = rb.solve_multi(Mg, np.array([np.concatenate([im[0], im[1]]) for im in imgs]).T)
            if not okk.all(): continue
            bad = 0
            for j, im in enumerate(imgs):
                R = rb.one()
                for i in np.nonzero(W[:, j])[0]: R = rb.mulp(R, G[i])
                if R[2] != im[2]: bad += 1; break
            if bad == 0: ok_eps.append(eps)
        res[(sec, bk.kind(M), len(ok_eps) > 0)] += 1
        good_eps[(sec, k)] = ok_eps
    print('sector', sec, {kk: v for kk, v in res.items() if kk[0] == sec}, flush=True)
import pickle; pickle.dump(good_eps, open('good_eps_L%d.pkl' % L, 'wb'))
