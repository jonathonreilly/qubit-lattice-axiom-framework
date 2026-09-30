"""K2 (kill check on T18): ONE qubit per site of Z^2, bounded-range plaquette rule (Wen 2003):
F_p = X(a,b) Y(a+1,b) X(a+1,b+1) Y(a,b+1).   Levin-Wen T-junction sign for three hop operators
that move one excitation of a given type to a common site:  sign = (-1)^(c12+c13+c23),
c_ij = 1 iff W_i, W_j anticommute (Pauli strings).  -1 => fermion, +1 => boson.

Hop operators are found by exact F2 linear algebra restricted to a thin strip around each leg, all
nullspace shifts (= multiplying by any stabiliser/strip-supported centraliser element) enumerated or
sampled, to show the sign does not depend on the representative.
Types: e = single plaquette on sublattice (a+b) even; m = single plaquette on sublattice odd;
eps = one e at p and one m at p+(1,0)  (composite).
"""
import itertools, random
import numpy as np

N = 14                      # N x N sites, open boundary
random.seed(1)


def plaquettes():
    return [(a, b) for a in range(N - 1) for b in range(N - 1)]


PL = plaquettes()
PIDX = {p: i for i, p in enumerate(PL)}
# F_p letters at corners
def corners(p):
    a, b = p
    return [((a, b), 'X'), ((a + 1, b), 'Y'), ((a + 1, b + 1), 'X'), ((a, b + 1), 'Y')]


def xz(letter):
    return {'X': (1, 0), 'Y': (1, 1), 'Z': (0, 1)}[letter]


def syndrome_row(site, kind):
    """plaquettes flipped by Pauli `kind` at `site` -> list of plaquette indices"""
    out = []
    xk, zk = xz(kind)
    for p in PL:
        for (s, L) in corners(p):
            if s == site:
                xf, zf = xz(L)
                if (xk * zf + zk * xf) % 2:
                    out.append(PIDX[p])
    return out


def solve_f2(A, t):
    """solve A v = t over F2 (A: rows x cols numpy uint8).  returns (particular, nullspace basis) or None"""
    A = A.copy() % 2
    t = t.copy() % 2
    rows, cols = A.shape
    M = np.concatenate([A, t.reshape(-1, 1)], axis=1).astype(np.uint8)
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if M[i, c]:
                pr = i; break
        if pr is None:
            continue
        M[[r, pr]] = M[[pr, r]]
        for i in range(rows):
            if i != r and M[i, c]:
                M[i] ^= M[r]
        piv.append(c); r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if M[i, -1]:
            return None
    v0 = np.zeros(cols, np.uint8)
    for i, c in enumerate(piv):
        v0[c] = M[i, -1]
    free = [c for c in range(cols) if c not in piv]
    null = []
    for f in free:
        v = np.zeros(cols, np.uint8); v[f] = 1
        for i, c in enumerate(piv):
            if M[i, f]:
                v[c] = 1
        null.append(v)
    return v0, null


def strip_sites(p_from, p_to, width=2):
    (a0, b0), (a1, b1) = p_from, p_to
    n = max(abs(a1 - a0), abs(b1 - b0), 1)
    sites = set()
    for k in range(n + 1):
        ca = a0 + (a1 - a0) * k / n
        cb = b0 + (b1 - b0) * k / n
        for da in range(-width, width + 2):
            for db in range(-width, width + 2):
                s = (int(round(ca)) + da, int(round(cb)) + db)
                if 0 <= s[0] < N and 0 <= s[1] < N:
                    sites.add(s)
    return sorted(sites)


def hop_operator(center_pl, leg_pl, sites, rng):
    """random Pauli (dict site->(x,z)) supported on `sites` with syndrome = center_pl xor leg_pl"""
    tgt = np.zeros(len(PL), np.uint8)
    for p in center_pl + leg_pl:
        tgt[PIDX[p]] ^= 1
    cols = []
    for s in sites:
        for kind in ('X', 'Z'):
            col = np.zeros(len(PL), np.uint8)
            for pi in syndrome_row(s, kind):
                col[pi] = 1
            cols.append(col)
    A = np.stack(cols, axis=1)
    sol = solve_f2(A, tgt)
    if sol is None:
        return None
    v0, null = sol
    v = v0.copy()
    for nv in null:
        if rng.random() < 0.5:
            v ^= nv
    P = {}
    for k, s in enumerate(sites):
        x, z = int(v[2 * k]), int(v[2 * k + 1])
        if x or z:
            P[s] = (x, z)
    return P


def anticommute(P, Q):
    c = 0
    for s, (x1, z1) in P.items():
        if s in Q:
            x2, z2 = Q[s]
            c ^= (x1 * z2 + z1 * x2) % 2
    return c


def tjunction(center, legs, ptype, trials=200, rng=random):
    """center, legs: plaquette coordinates of the base point of the excitation; ptype in e,m,eps"""
    def cluster(p):
        a, b = p
        if ptype == 'e':
            return [p]                       # caller guarantees parity
        if ptype == 'm':
            return [p]
        return [p, (a + 1, b)]               # eps: p (even) + neighbour (odd)
    c_cl = cluster(center)
    signs = {}
    for _ in range(trials):
        Ws = []
        for lg in legs:
            sites = strip_sites(center, lg)
            W = hop_operator(c_cl, cluster(lg), sites, rng)
            if W is None:
                return None
            Ws.append(W)
        sgn = (-1) ** (anticommute(Ws[0], Ws[1]) + anticommute(Ws[0], Ws[2]) + anticommute(Ws[1], Ws[2]))
        signs[sgn] = signs.get(sgn, 0) + 1
    return signs


def weight_stat(center, legs, ptype):
    def cluster(p):
        a, b = p
        return [p] if ptype != 'eps' else [p, (a + 1, b)]
    ws = []
    for lg in legs:
        W = hop_operator(cluster(center), cluster(lg), strip_sites(center, lg), random.Random(0))
        ws.append(len(W))
    return ws


if __name__ == "__main__":
    rng = random.Random(7)
    # e: even-parity plaquette base, m: odd-parity plaquette base, eps: even base (+ right neighbour)
    cases = {
        'e   (sublattice even)': ('e', (6, 6)),
        'm   (sublattice odd) ': ('m', (6, 7)),
        'eps (e+m composite)  ': ('eps', (6, 6)),
    }
    print(f"Wen plaquette model, {N}x{N} sites (one qubit per site), F_p = X Y X Y around each unit square")
    for name, (ptype, c) in cases.items():
        # three legs of length 4 in the -x, +x, +y directions from centre (T-junction; all same sublattice class)
        legs = [(c[0] - 4, c[1]), (c[0] + 4, c[1]), (c[0], c[1] + 4)]
        res = tjunction(c, legs, ptype, trials=300, rng=rng)
        legs2 = [(c[0], c[1] - 4), (c[0] + 4, c[1]), (c[0], c[1] + 4)]
        res2 = tjunction(c, legs2, ptype, trials=300, rng=rng)
        legs3 = [(c[0] - 4, c[1] - 4), (c[0] + 4, c[1]), (c[0], c[1] + 4)]
        res3 = tjunction(c, legs3, ptype, trials=300, rng=rng)
        print(f"  {name}: T-junction sign counts over 300 random representatives per geometry: "
              f"(-x,+x,+y) {res}   (-y,+x,+y) {res2}   (diag,+x,+y) {res3}")
    print("  hop-operator Pauli weights (eps, leg length 4, one representative each):", weight_stat((6, 6), [(2, 6), (10, 6), (6, 10)], 'eps'))
