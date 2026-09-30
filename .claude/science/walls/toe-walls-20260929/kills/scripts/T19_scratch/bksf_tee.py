"""Test B: topological entropy of the BKSF vacuum on a square-lattice torus (qubits on edges).
Stabilizers: B_v (Z on the 4 incident edges) and loop words sum_{e in loop} A_e, where
A_e = X_e * Z(preceding edges at tail) * Z(preceding edges at head).  Phases irrelevant for ranks.
S_R = |R| - dim{stabilizers supported in R}.  Kitaev-Preskill gamma on a disc split in 3 sectors.
Controls: toric code (star X, plaquette Z) -> 1 bit ; product state (all Z_e) -> 0.
"""
import numpy as np, sys, itertools, math

def gf2_rank(M):
    M = M.copy() % 2
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        for i in range(rows):
            if i != r and M[i, c]: M[i] ^= M[r]
        r += 1
        if r == rows: break
    return r

def gf2_nullity_left(M):
    """dimension of {c : c M = 0}"""
    return M.shape[0] - gf2_rank(M)

class Torus:
    def __init__(self, L):
        self.L = L
        self.n = 2 * L * L
    def v(self, i, j): return (i % self.L) * self.L + (j % self.L)
    def e(self, i, j, d): return 2 * self.v(i, j) + d
    def incident(self, i, j):  # ordering at vertex: +x, +y, -x, -y
        return [self.e(i, j, 0), self.e(i, j, 1), self.e(i - 1, j, 0), self.e(i, j - 1, 1)]

def vec(n, xs=(), zs=()):
    a = np.zeros(2 * n, dtype=np.uint8)
    for q in xs: a[q] ^= 1
    for q in zs: a[n + q] ^= 1
    return a

def omega(a, b, n):
    return int((a[:n] @ b[n:] + a[n:] @ b[:n]) % 2)

def bksf(L):
    T = Torus(L); n = T.n
    def A(i, j, d):
        tail = (i, j); head = (i + 1, j) if d == 0 else (i, j + 1)
        e = T.e(i, j, d)
        zs = []
        for (a, b) in (tail, head):
            lst = T.incident(a % L, b % L)
            zs += lst[:lst.index(e)]
        return vec(n, xs=[e], zs=zs)
    gens = []
    for i in range(L):
        for j in range(L):
            gens.append(vec(n, zs=T.incident(i, j)))          # B_v
    for i in range(L):
        for j in range(L):                                       # plaquette loops
            g = A(i, j, 0) ^ A((i + 1) % L, j, 1) ^ A(i, (j + 1) % L, 0) ^ A(i, j, 1)
            gens.append(g)
    gens.append(sum(A(i, 0, 0) for i in range(L)) % 2)          # noncontractible loops
    gens.append(sum(A(0, j, 1) for j in range(L)) % 2)
    G = np.array(gens, dtype=np.uint8)
    return T, G

def toric(L):
    T = Torus(L); n = T.n
    gens = []
    for i in range(L):
        for j in range(L):
            gens.append(vec(n, xs=T.incident(i, j)))            # star X
            gens.append(vec(n, zs=[T.e(i, j, 0), T.e(i + 1, j, 1), T.e(i, j + 1, 0), T.e(i, j, 1)]))  # plaquette Z
    return T, np.array(gens, dtype=np.uint8)

def product(L):
    T = Torus(L); n = T.n
    return T, np.array([vec(n, zs=[q]) for q in range(n)], dtype=np.uint8)

def entropy(G, n, R):
    """S_R (bits) of stabilizer state with generator matrix G (rows, 2n cols)."""
    R = sorted(R)
    outside = [q for q in range(n) if q not in set(R)]
    cols = outside + [n + q for q in outside]
    if not cols: return len(R) - 0
    M = G[:, cols]
    k = gf2_nullity_left(M)  # number of independent combos supported in R
    return len(R) - k

def check_state(G, n):
    m = G.shape[0]
    for a in range(m):
        for b in range(a + 1, m):
            assert omega(G[a], G[b], n) == 0, "generators do not commute"
    return gf2_rank(G)

def disc_regions(T, cx, cy, rad):
    """edges inside a disc of vertices around (cx,cy): edge included if both endpoints in disc.
    split into 3 sectors by angle; return three sets of edges"""
    L = T.L
    def inside(i, j): return (i - cx) ** 2 + (j - cy) ** 2 <= rad * rad
    def angle_sector(x, y):
        ang = math.atan2(y - cy, x - cx) % (2 * math.pi)
        return int(ang // (2 * math.pi / 3))
    sec = [set(), set(), set()]
    for i in range(L):
        for j in range(L):
            for d in (0, 1):
                a = (i, j); b = (i + 1, j) if d == 0 else (i, j + 1)
                if inside(*a) and inside(*b):
                    mx = (a[0] + b[0]) / 2 + 1e-6; my = (a[1] + b[1]) / 2 + 2e-6
                    sec[angle_sector(mx, my)].add(T.e(i, j, d))
    return sec

def kp(G, n, sec):
    A, B, C = sec
    S = lambda R: entropy(G, n, R)
    return S(A) + S(B) + S(C) - S(A | B) - S(B | C) - S(A | C) + S(A | B | C)

if __name__ == '__main__':
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    for name, f in (('BKSF vacuum', bksf), ('toric code', toric), ('product (JW-like)', product)):
        T, G = f(L)
        rk = check_state(G, T.n)
        print(f"{name}: L={L}, n={T.n}, generators={G.shape[0]}, rank={rk} (pure iff rank=n={T.n})")
        for (cx, cy, rad) in [(L / 2 - .5, L / 2 - .5, 2.2), (L / 2 - .5, L / 2 - .5, 2.9), (L / 2, L / 2, 3.2), (L / 2 + .3, L / 2 - .2, 3.6)]:
            sec = disc_regions(T, cx, cy, rad)
            print(f"   disc c=({cx:.1f},{cy:.1f}) r={rad}: sector sizes {[len(s) for s in sec]}, KP gamma = {kp(G, T.n, sec)} bits")
