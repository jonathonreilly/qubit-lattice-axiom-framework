"""Generic T-junction exchange sign for same-site charge patterns of a translation-invariant Pauli stabilizer model.
gens: list of dicts {(offset tuple, qubit): (xbit, zbit)} ; q qubits per site; D dims.
Leg to d: Pauli P supported in a box around segment [0,d] whose syndrome is exactly c(0)+c(d).
sign = lam(W1,W2) lam(W2,W3) lam(W3,W1)."""
import itertools, random

def box(d, r):
    D = len(d)
    lo = [min(0, d[k]) - r for k in range(D)]; hi = [max(0, d[k]) + r for k in range(D)]
    return list(itertools.product(*[range(lo[k], hi[k] + 1) for k in range(D)]))

def solve_gf2(rows, nvar):
    """rows: list of int (bits 0..nvar-1 coefficients, bit nvar rhs). Returns one solution (int) and nullspace basis, or None."""
    piv = {}
    for row in rows:
        v = row
        while True:
            m = v & ((1 << nvar) - 1)
            if m == 0:
                if v >> nvar: return None
                break
            hb = m.bit_length() - 1
            if hb in piv: v ^= piv[hb]
            else: piv[hb] = v; break
    # back-substitute to reduced form
    keys = sorted(piv)
    for k in keys:
        for k2 in keys:
            if k2 != k and (piv[k2] >> k) & 1: piv[k2] ^= piv[k]
    x = 0
    for k, v in piv.items():
        if (v >> nvar) & 1: x |= 1 << k
    free = [j for j in range(nvar) if j not in piv]
    null = []
    for f in free:
        y = 1 << f
        for k, v in piv.items():
            if (v >> f) & 1: y |= 1 << k
        null.append(y)
    return x, null

def leg(gens, q, c, d, r, rng=None):
    D = len(d); B = box(d, r); idx = {}
    for s in B:
        for a in range(q): idx[(s, a)] = len(idx)
    nq = len(idx); nvar = 2 * nq        # var 2k = x bit, 2k+1 = z bit of qubit k
    origin = tuple([0]*D); dd = tuple(d)
    # all generator translates overlapping B
    trans = set()
    for g in gens:
        for (o, a) in g:
            for s in B: trans.add(tuple(s[k] - o[k] for k in range(D)))
    rows = []
    for gi, g in enumerate(gens):
        for t in trans:
            row = 0
            for (o, a), (xb, zb) in g.items():
                site = tuple(t[k] + o[k] for k in range(D))
                if (site, a) in idx:
                    k = idx[(site, a)]
                    if zb: row |= 1 << (2*k)      # P's x bit pairs with gen z bit
                    if xb: row |= 1 << (2*k + 1)
            if row == 0: continue
            rhs = (c[gi] if t == origin else 0) ^ (c[gi] if t == dd else 0)
            rows.append(row | (rhs << nvar))
    sol = solve_gf2(rows, nvar)
    if sol is None: return None
    x, null = sol
    if rng is not None:
        for y in null:
            if rng.random() < 0.5: x ^= y
    W = {}
    for (s, a), k in idx.items():
        xb, zb = (x >> (2*k)) & 1, (x >> (2*k + 1)) & 1
        if xb or zb: W[(s, a)] = (xb, zb)
    return W

def lam(W1, W2):
    p = 0
    for key, (x1, z1) in W1.items():
        if key in W2:
            x2, z2 = W2[key]; p ^= (x1 & z2) ^ (z1 & x2)
    return -1 if p else 1

def tsign(gens, q, c, dirs, rmax=3, rng=None, rmin=0):
    Ws = []
    for d in dirs:
        W = None
        for r in range(rmin, rmax + 1):
            W = leg(gens, q, c, d, r, rng)
            if W is not None: break
        if W is None: return None
        Ws.append(W)
    return lam(Ws[0], Ws[1]) * lam(Ws[1], Ws[2]) * lam(Ws[2], Ws[0])

def all_patterns(gens, q, dirs, rmax=3, trials=3, rmin=0):
    out = {}
    for c in itertools.product((0, 1), repeat=len(gens)):
        if not any(c): continue
        s0 = tsign(gens, q, c, dirs, rmax, None, rmin)
        if s0 is None: out[c] = None; continue
        rng = random.Random(hash(c) & 0xffff)
        ss = [tsign(gens, q, c, dirs, rmax, rng, rmin) for _ in range(trials)]
        out[c] = (s0, ss)
    return out

if __name__ == '__main__':
    # 2D toric code validation
    X, Z = (1, 0), (0, 1)
    A = {((0, 0), 0): X, ((0, 0), 1): X, ((-1, 0), 0): X, ((0, -1), 1): X}
    Bp = {((0, 0), 0): Z, ((0, 1), 0): Z, ((0, 0), 1): Z, ((1, 0), 1): Z}
    for dirs in [((2, 0), (0, 2), (-2, 0)), ((4, 0), (0, 4), (-4, -4)), ((2, 0), (0, 2), (2, 2))]:
        print('2D toric, legs', dirs, all_patterns([A, Bp], 2, dirs, trials=3))
    # 3D toric code (vertex X on 6 edges, plaquette Z): e should be a boson
    def e3(a, s): v = [0, 0, 0]; v[a] = s; return tuple(v)
    A3 = {}
    for a in range(3): A3[((0, 0, 0), a)] = X; A3[(e3(a, -1), a)] = X
    Bs = []
    for cax in range(3):
        a, b = [k for k in range(3) if k != cax]
        Bp3 = {((0, 0, 0), a): Z, (e3(b, 1), a): Z, ((0, 0, 0), b): Z, (e3(a, 1), b): Z}
        Bs.append(Bp3)
    print('3D toric, legs 2e_x,2e_y,2e_z', all_patterns([A3] + Bs, 3, ((2, 0, 0), (0, 2, 0), (0, 0, 2)), trials=2))
