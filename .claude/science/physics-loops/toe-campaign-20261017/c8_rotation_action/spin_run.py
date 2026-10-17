import sys, itertools
import numpy as np
exec(open('spin.py').read())
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
stab = [M for M in O if H[bk.rot_order(M, o0)] == H[o0]]
C3 = next(M for M in stab if int(round(np.trace(M))) == 0)
C2 = next(M for M in stab if int(round(np.trace(M))) == -1)
print('ordering', o0, 'C3 =', C3.tolist(), 'C2 =', C2.tolist(), flush=True)
# choose plaquette signs so that the signed group does not contain -1 (check relations)
def valid(G):
    M = np.array([np.concatenate([g[0], g[1]]) for g in G]); r, N = c1.f2_rank_and_null(M)
    for c in N:
        R_ = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
        for i in np.nonzero(c)[0]: R_ = mulp(R_, G[i])
        if R_[2] % 4: return False
    return True
for signs in itertools.product((0, 1), repeat=3):
    G, lab = gens(o0, signs)
    if valid(G): break
print('plaquette signs', signs, 'valid:', valid(G), flush=True)
def analyse(Mrot, power, name):
    perm = perm_of(Mrot)
    # signs of rotated generators
    bad = []
    for i, g in enumerate(G):
        gp = apply_perm(g, perm)
        h = express(G, gp)
        assert h is not None, 'rotated generator not in group'
        bad.append(0 if h[2] == gp[2] else 1)   # mismatch iff phases differ (both Hermitian -> differ by 2)
    bad = np.array(bad, np.uint8)
    # F: omega(F, P g P^-1) = bad_g for all g  (solve on images)
    imgs = [apply_perm(g, perm) for g in G]
    Msym = np.array([np.concatenate([im[1], im[0]]) for im in imgs])   # omega(F,im) = F.x.im.z + F.z.im.x
    w = gf2_solve(Msym, bad)
    assert w is not None
    F = [w[:n].astype(np.uint8), w[n:].astype(np.uint8), 0]
    if (F[2] - int(F[0] @ F[1])) % 2: F[2] = 1
    W = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]; Fk = F
    for _ in range(power):
        W = mulp(W, Fk); Fk = apply_perm(Fk, perm)
    # W commutes with all generators?
    comm = all(omega(W, g) == 0 for g in G)
    # fermion legs from the origin (rotation centre) and between distant points
    def leg(start, d, length):
        a, s = bk.DIRS[d]; P = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]; v = start
        for _ in range(length):
            if s == 1: base = v; v = tuple(v[i] + E[a][i] for i in range(3))
            else: v = tuple(v[i] - E[a][i] for i in range(3)); base = v
            P = mulp(P, from_op(bk.A(base, a, o0)))
        return P
    centre = [omega(W, leg((0,0,0), d, 2)) for d in range(6)]
    away = [omega(W, leg((2,1,0), d, 1)) for d in range(6)] + [omega(W, leg((1,2,2), d, 1)) for d in range(6)]
    print(f'{name}: |F| support {int(F[0].sum() + F[1].sum())}, W commutes with all stabilizers: {comm}, '
          f'W weight {int((W[0] | W[1]).sum())}; omega(W, legs from centre) {centre}; omega(W, legs away from centre) {away}', flush=True)
analyse(C3, 3, 'C3^3')
analyse(C2, 2, 'C2^2')
