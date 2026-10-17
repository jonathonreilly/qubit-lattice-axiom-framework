"""Mobile same-site charge subspace and T-junction signs on all of it (legs combined bilinearly)."""
import itertools, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from stats import box, solve_gf2, leg, lam

def rowreduce(vecs):
    piv = {}
    for v in vecs:
        while v:
            hb = v.bit_length() - 1
            if hb in piv: v ^= piv[hb]
            else: piv[hb] = v; break
    return list(piv.values())

def intersect(U, V, k):
    """subspace intersection over GF(2) of spans of U and V (ints with k bits)."""
    # solve sum a_i u_i = sum b_j v_j ; use combined vectors (u_i | e_i<<k), (v_j | 0)
    rows = [u | (1 << (k + i)) for i, u in enumerate(U)] + [v for v in V]
    piv = {}; res = []
    for r in rows:
        x = r
        while x & ((1 << k) - 1):
            hb = (x & ((1 << k) - 1)).bit_length() - 1
            if hb in piv: x ^= piv[hb]
            else: piv[hb] = x; break
        else:
            if x: # combination of U equal to combination of V
                coeffs = x >> k; w = 0
                for i in range(len(U)):
                    if (coeffs >> i) & 1: w ^= U[i]
                res.append(w)
    return rowreduce([w for w in res if w])

def movable(gens, q, d, r):
    D = len(d); B = box(d, r); idx = {}
    for s in B:
        for a in range(q): idx[(s, a)] = len(idx)
    nq = len(idx); nvar = 2*nq; k = len(gens)
    origin = tuple([0]*D); dd = tuple(d)
    trans = set()
    for g in gens:
        for (o, a) in g:
            for s in B: trans.add(tuple(s[j] - o[j] for j in range(D)))
    rows = []
    for gi, g in enumerate(gens):
        for t in trans:
            row = 0
            for (o, a), (xb, zb) in g.items():
                site = tuple(t[j] + o[j] for j in range(D))
                if (site, a) in idx:
                    kk = idx[(site, a)]
                    if zb: row |= 1 << (2*kk)
                    if xb: row |= 1 << (2*kk + 1)
            if t in (origin, dd): row |= 1 << (nvar + gi)
            if row: rows.append(row)
    x, null = solve_gf2(rows, nvar + k)
    return rowreduce([(y >> nvar) for y in null if y >> nvar])

def mobile_signs(gens, q, dirs, r=2):
    k = len(gens)
    Vs = [movable(gens, q, d, r) for d in dirs]
    M = Vs[0]
    for V in Vs[1:]: M = intersect(M, V, k)
    legs = []
    for m in M:
        c = [(m >> i) & 1 for i in range(k)]
        Ls = []
        for d in dirs:
            W = None
            for rr in range(0, r + 2):
                W = leg(gens, q, c, d, rr)
                if W is not None: break
            assert W is not None
            Ls.append(W)
        legs.append(Ls)
    def xor(Wa, Wb):
        out = dict(Wa)
        for key, (x, z) in Wb.items():
            x0, z0 = out.get(key, (0, 0)); v = (x0 ^ x, z0 ^ z)
            if v == (0, 0): out.pop(key, None)
            else: out[key] = v
        return out
    signs = {}
    for coeffs in itertools.product((0, 1), repeat=len(M)):
        if not any(coeffs): continue
        c = 0; Ls = [{}, {}, {}]
        for b, m, lg in zip(coeffs, M, legs):
            if b:
                c ^= m; Ls = [xor(Ls[i], lg[i]) for i in range(3)]
        signs[c] = lam(Ls[0], Ls[1]) * lam(Ls[1], Ls[2]) * lam(Ls[2], Ls[0])
    return [len(V) for V in Vs], len(M), signs

if __name__ == '__main__':
    X, Z = (1, 0), (0, 1)
    A = {((0, 0), 0): X, ((0, 0), 1): X, ((-1, 0), 0): X, ((0, -1), 1): X}
    Bp = {((0, 0), 0): Z, ((0, 1), 0): Z, ((0, 0), 1): Z, ((1, 0), 1): Z}
    print('2D toric', mobile_signs([A, Bp], 2, ((2, 0), (0, 2), (-2, 0))))
    def e3(a, s): v = [0, 0, 0]; v[a] = s; return tuple(v)
    A3 = {}
    for a in range(3): A3[((0, 0, 0), a)] = X; A3[(e3(a, -1), a)] = X
    Bs = []
    for cax in range(3):
        a, b = [kk for kk in range(3) if kk != cax]
        Bs.append({((0, 0, 0), a): Z, (e3(b, 1), a): Z, ((0, 0, 0), b): Z, (e3(a, 1), b): Z})
    print('3D toric', mobile_signs([A3] + Bs, 3, ((2, 0, 0), (0, 2, 0), (0, 0, 2))))
    # 2D toric stacked in xy layers (embedding in 3D): no 3D-mobile charge expected
    A2 = {((0, 0, 0), 0): X, ((0, 0, 0), 1): X, ((-1, 0, 0), 0): X, ((0, -1, 0), 1): X}
    B2 = {((0, 0, 0), 0): Z, ((0, 1, 0), 0): Z, ((0, 0, 0), 1): Z, ((1, 0, 0), 1): Z}
    print('2D toric layers in 3D', mobile_signs([A2, B2], 3, ((2, 0, 0), (0, 2, 0), (0, 0, 2))))
