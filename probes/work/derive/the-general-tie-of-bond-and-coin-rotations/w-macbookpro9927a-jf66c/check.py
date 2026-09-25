"""check.py -- the-general-tie-of-bond-and-coin-rotations a2 (worker w-macbookpro9927a-jf66c).

Part (a) at REACH TWO (a1's open item 1): the local translation-invariant ties B = T theta whose strain on the bond
(x, x + e_a) reads theta at the 38 sites within two steps of either end, with T^dagger J = 0 on every stationary state,
are exactly the relabelling ties B = d(M theta) with M on the 25-site ball of radius two (75 per rotation component).
Method as in the refereed a1: the constraint P~_{k1} X_{k1 k2} P~_{k2} = 0 for every pair (k1, k2) in one eigenspace,
mapped by a ring homomorphism Z[1/2][i, sqrt2, sqrt3, sqrt5] -> F_p (p = 1 mod 120); rank over K >= rank mod p.
Validation: the same code reproduces a1's reach-one ranks (87 on 6^3, 81 on 4^3). Run from the repository root.
"""
import itertools, os, sys, time
import numpy as np
from sympy import isprime
from sympy.ntheory import sqrt_mod
import sympy as sp

T0 = time.time(); FAILS = []; NOK = 0
def ok(name, cond, detail=""):
    global NOK
    if cond: NOK += 1
    else: FAILS.append(name); print("FAIL", name, detail)

p = next(q for q in range(1 << 20, 1 << 21) if q % 120 == 1 and isprime(q))
Ii, R2, R3, R5 = (int(sqrt_mod(v, p)) for v in (p - 1, 2, 3, 5))
inv = lambda a: pow(int(a) % p, p - 2, p)
z8 = (1 + Ii) * inv(R2) % p
z6 = (1 + Ii * R3) * inv(2) % p
ok("A1 embedding into F_p (p = 1 mod 120): i^2 = -1, sqrt2, sqrt3, sqrt5; zeta8 = (1+i)/sqrt2 and zeta6 = (1+i sqrt3)/2 primitive",
   Ii * Ii % p == p - 1 and R2 * R2 % p == 2 and R3 * R3 % p == 3 and R5 * R5 % p == 5 and pow(z8, 8, p) == 1 and pow(z8, 4, p) == p - 1
   and pow(z6, 6, p) == 1 and pow(z6, 3, p) == p - 1, f"p = {p}")
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
l1 = lambda v: sum(abs(t) for t in v)
SIG = np.array([[[0, 1], [1, 0]], [[0, (p - Ii) % p], [Ii, 0]], [[1, 0], [0, p - 1]]], dtype=np.int64)
ID = np.eye(2, dtype=np.int64)

def stencil(reach):
    Dl = [[d for d in itertools.product(range(-reach, reach + 2), repeat=3) if min(l1(d), l1(tuple(d[i] - E[a][i] for i in range(3)))) <= reach] for a in range(3)]
    cols = [(a, j, d) for a in range(3) for j in range(3) for d in Dl[a]]
    return Dl, cols

def rows_gen(Lt, cols, chunk_pairs=3000):
    """yield constraint rows (mod p) in chunks: 4 entries of P~_{k1} X P~_{k2} per ordered pair in each eigenspace"""
    z = {4: Ii, 6: z6, 8: z8}[Lt]
    zp = np.array([pow(z, e, p) for e in range(Lt)], dtype=np.int64)
    ep = lambda n: int(zp[n % Lt])
    sn = lambda n: (ep(n) - ep(-n)) * inv(2 * Ii) % p
    ks = list(itertools.product(range(Lt), repeat=3))
    # group momenta by |s|^2 (as an integer label valid on these tori) and store s, e^{ik}, e^{-ik}
    def s2label(kk):
        return tuple(sorted((min(n % Lt, (Lt - n) % Lt) % (Lt // 2) if Lt % 2 == 0 else n) for n in kk))
    shells = {}
    for kk in ks:
        # exact |s|^2 = sum sin^2(2 pi n / L): use its value mod p as the grouping key (injective on these small sets, checked below)
        s = [sn(n) for n in kk]; ssq = sum(v * v for v in s) % p
        shells.setdefault(ssq, []).append(kk)
    # square roots of |s|^2 consistent with the embedding: built from sqrt2, sqrt3, sqrt5
    half = inv(2)
    table = {0: 0}
    for m in range(1, 7):     # 8^3: |s|^2 = m/2
        cand = {1: inv(R2), 2: 1, 3: R3 * inv(R2), 4: R2, 5: R5 * inv(R2), 6: R3}[m]
        table[m * half % p] = cand
    for c in range(1, 4):      # 6^3: |s|^2 = 3c/4 ; 4^3: |s|^2 = c
        table[3 * c * inv(4) % p] = {1: R3 * inv(2) % p, 2: R2 * R3 * inv(2) % p, 3: 3 * inv(2) % p}[c]
        table.setdefault(c % p, {1: 1, 2: R2, 3: R3}[c])
    Dl_arr = np.array([d for (a, j, d) in cols], dtype=np.int64)
    a_arr = np.array([a for (a, j, d) in cols]); j_arr = np.array([j for (a, j, d) in cols])
    for ssq, lst in shells.items():
        r = table[ssq]
        assert r * r % p == ssq
        karr = np.array(lst, dtype=np.int64)
        S = np.array([[sn(n) for n in kk] for kk in lst], dtype=np.int64)            # (n, 3)
        EP = np.array([[ep(n) for n in kk] for kk in lst], dtype=np.int64); EM = np.array([[ep(-n) for n in kk] for kk in lst], dtype=np.int64)
        branches = [None] if ssq == 0 else [r, (p - r) % p]
        for br in branches:
            if br is None:
                Pt = np.broadcast_to(ID, (len(lst), 2, 2)).copy()
            else:
                Pt = (br * ID[None] + np.einsum('ka,aij->kij', S, SIG)) % p
            pairs = [(i1, i2) for i1 in range(len(lst)) for i2 in range(len(lst))]
            for s0 in range(0, len(pairs), chunk_pairs):
                pr = np.array(pairs[s0:s0 + chunk_pairs]); i1, i2 = pr[:, 0], pr[:, 1]
                q = (karr[i2] - karr[i1]) % Lt                                                   # (m, 3)
                ph = zp[(-(q @ Dl_arr.T)) % Lt]                                                  # (m, NC)
                f = ph * ((EP[i2][:, a_arr] + EM[i1][:, a_arr]) % p) % p
                f = f * ((S[i2][:, j_arr] + S[i1][:, j_arr]) % p) % p                            # (m, NC)
                # Xa = Pt[k1] sigma_a Pt[k2], entries (m, 3, 2, 2)
                Xa = np.einsum('mij,ajk->maik', Pt[i1], SIG) % p
                Xa = np.einsum('maik,mkl->mail', Xa, Pt[i2]) % p
                Xc = Xa[:, a_arr]                                                                # (m, NC, 2, 2)
                for e1, e2 in ((0, 0), (0, 1), (1, 0), (1, 1)):
                    yield f * Xc[:, :, e1, e2] % p

class ModRank:
    def __init__(self, nc):
        self.B = np.zeros((0, nc), dtype=np.int64); self.piv = []
    def reduce(self, C):
        if len(self.piv):
            coeff = C[:, self.piv].astype(np.float64)
            C = (C - np.rint(coeff @ self.B.astype(np.float64)).astype(np.int64) % p) % p     # exact: sums < 2^53
        return C
    def add(self, C):
        C = self.reduce(C % p)
        nzrows = np.nonzero(C.any(axis=1))[0]
        C = C[nzrows]
        while C.shape[0]:
            row0 = C[0]; col = int(np.nonzero(row0)[0][0])
            r = row0 * inv(row0[col]) % p
            if len(self.piv):
                self.B = (self.B - np.outer(self.B[:, col], r) % p) % p
            self.B = np.vstack([self.B, r]); self.piv.append(col)
            C = (C - np.outer(C[:, col], r) % p) % p
            C = C[np.nonzero(C.any(axis=1))[0]]
        return self
    def rank(self): return len(self.piv)

def relabellings(Dl, cols, reach):
    cidx = {c: i for i, c in enumerate(cols)}
    ball = [d for d in itertools.product(range(-reach, reach + 1), repeat=3) if l1(d) <= reach - 1] if reach == 1 else \
           [d for d in itertools.product(range(-reach, reach + 1), repeat=3) if l1(d) <= reach]
    if reach == 1:
        ball = [(0, 0, 0)] + [tuple(s * E[a][i] for i in range(3)) for a in range(3) for s in (1, -1)]
    rel = []
    for j0 in range(3):
        for dp in ball:
            t = np.zeros(len(cols), dtype=np.int64)
            for a in range(3):
                t[cidx[(a, j0, tuple(E[a][i] + dp[i] for i in range(3)))]] += 1
                t[cidx[(a, j0, dp)]] -= 1
            rel.append(t % p)
    return np.array(rel), len(ball)

def run(Lt, reach):
    Dl, cols = stencil(reach); NC = len(cols)
    rel, nb = relabellings(Dl, cols, reach)
    MR = ModRank(NC); nrows = 0; viol = 0
    relf = rel.T.astype(np.float64)
    for C in rows_gen(Lt, cols):
        nrows += C.shape[0]
        viol += int(np.count_nonzero(np.rint(C.astype(np.float64) @ relf).astype(np.int64) % p))
        if MR.rank() < NC:
            MR.add(C)
    relrank = sp.Matrix([[int(v) if v < p // 2 else int(v) - p for v in row] for row in rel]).rank()
    return NC, nrows, MR.rank(), relrank, viol, [len(x) for x in Dl]

# validation against a1 (refereed): reach one on 4^3 and 6^3
NC1, n4, r4, rel1, v4, _ = run(4, 1)
_, n6, r6, _, v6, _ = run(6, 1)
ok("B1 reach one reproduces a1: 108 unknowns, 21 relabellings; rank mod p 81 on 4^3 and 87 on 6^3 (a1's numbers, confirmed by referee)",
   NC1 == 108 and rel1 == 21 and r4 == 81 and r6 == 87 and v4 == 0 and v6 == 0, f"{NC1} {rel1} {r4} {r6} {v4} {v6} rows {n4} {n6}")
_, n8a, r8a, _, v8a, _ = run(8, 1)
ok("B2 reach one on 8^3: rank 87 as well (no new ties, no aliasing artefacts)", r8a == 87 and v8a == 0, f"{r8a} rows {n8a}")
# the new result: reach two on 8^3
NC2, n8, r8, rel2, v8, sizes = run(8, 2)
ok("C1 reach two: 38 sites per bond direction, 342 unknowns per rotation component; relabellings on the 25-site ball: 75 independent",
   sizes == [38, 38, 38] and NC2 == 342 and rel2 == 75, f"{sizes} {NC2} {rel2}")
ok("C2 every relabelling tie satisfies all constraints on 8^3 (mod p)", v8 == 0, str(v8))
ok("C3 reach two on 8^3: rank 267 = 342 - 75 mod p, so over K the ties are exactly the relabellings (dimension 75 per component)",
   r8 == 267, f"rank {r8} rows {n8}")
print(f"rows: reach one 4^3 {n4}, 6^3 {n6}, 8^3 {n8a}; reach two 8^3 {n8}; ranks {r4}, {r6}, {r8a}, {r8}; p = {p}; {time.time() - T0:.0f} s")

print(f"checks passed {NOK}, failed {len(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL (a) decided exactly at reach two (a1's open item 1): every translation-invariant tie B = T theta whose strain on a bond "
      "reads theta within two steps of either end (38 sites, 342 unknowns per component) and has T^dagger J = 0 on every stationary state "
      "of the 8^3 torus is a relabelling tie B = d(M theta) with M on the radius-two ball (75 per component; rank 267 mod p against 75 exact "
      "solutions), so on Z^3 too the tied rotation is pure gauge and the nine-plus-three variables stay forced; the code reproduces a1's reach-one ranks")
print("HIT: no genuine tie of bond and coin rotations at reach two either: the ties with T^dagger J = 0 on every stationary state that read theta "
      "within two steps of the bond's ends are exactly the relabellings B = d(M theta), M on the radius-two ball (75 per rotation component; "
      "constraint rank 267 of 342 on the 8^3 torus via a ring homomorphism into F_p), extending the refereed reach-one result; the nine-plus-three "
      "variables are forced at reach two")
