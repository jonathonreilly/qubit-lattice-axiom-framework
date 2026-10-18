#!/usr/bin/env python3
"""C2_check ck1: independent route for C2's homogeneous lemma (claim 1).

Statement checked: a pointwise density V2 quadratic in h_ij (d = 3 spatial, symmetric) with at most 2 derivatives in total
on the two h factors, with ARBITRARY (non-isotropic, x-independent at the point) coefficients, satisfies
delta_xi V2 = 0 pointwise under delta h_ij = d_i xi_j + d_j xi_i only if V2 = 0.
Why this covers C2's S2: with N arbitrary, int N delta V2 = 0 for all N forces delta V2 = 0 pointwise; matter factors
(phi, pi and their jets, <= 2 derivatives shared with h) enter V2 only through pointwise coefficients that the h-shift does
not touch, so for each fixed matter jet the problem is this one, with fewer derivatives on h.  No isotropy is assumed
(stronger than C2's 28-dim isotropic ansatz).  This is jet-space linear algebra, a different route from kb.py's Fourier
kernels.  Positive controls: (i) engine annihilates the exact invariant R1 x R1 (linearised Ricci, 4 derivatives);
(ii) kernel of the pure d^2h x d^2h block = 21 = dim Sym^2(6 components of linearised Ricci in d = 3).
Rank is computed both in floating point (SVD) and exactly modulo a large prime.
"""
import itertools, time
import numpy as np

T0 = time.time()
RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.1f}s] {msg}", flush=True)

d = 3
COMP = [(i, j) for i in range(d) for j in range(d) if i <= j]
def multis(n):
    return sorted({tuple(sorted(c)) for c in itertools.combinations_with_replacement(range(d), n)})
def hjets(maxn):
    return [(c, a) for n in range(maxn + 1) for a in multis(n) for c in COMP]

def build(pairs):
    """pairs: list of (hjet1, hjet2) unordered monomials. Returns matrix: rows = (xi-jet, h-jet) monomials."""
    rows = {}
    entries = []
    for col, (J1, J2) in enumerate(pairs):
        for (Jv, Jo) in ((J1, J2), (J2, J1)):   # vary one factor, keep the other
            (i, j), al = Jv
            # delta h_ij,al = xi_j,(al+i) + xi_i,(al+j)
            for (comp, extra) in ((j, i), (i, j)):
                xj = (comp, tuple(sorted(al + (extra,))))
                key = (xj, Jo)
                r = rows.setdefault(key, len(rows))
                entries.append((r, col, 1))
    A = np.zeros((len(rows), len(pairs)), dtype=np.int64)
    for r, c, v in entries:
        A[r, c] += v
    return A

def rank_modp(A, p=2_147_483_647):
    M = (A % p).astype(object)
    M = [list(map(int, row)) for row in M]
    nr, nc = len(M), len(M[0]) if M else 0
    rk, r = 0, 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if M[i][c] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1; rk += 1
        if r == nr:
            break
    return rk

def null_dim(A):
    s = np.linalg.svd(A.astype(float), compute_uv=False)
    rk_f = int(np.sum(s > 1e-9 * s[0]))
    rk_p = rank_modp(A)
    return A.shape[1] - rk_f, A.shape[1] - rk_p

# ---- main lemma: all unordered pairs of h-jets with |a1| + |a2| <= 2
J = hjets(2)
pairs = [(J[a], J[b]) for a in range(len(J)) for b in range(a, len(J)) if len(J[a][1]) + len(J[b][1]) <= 2]
A = build(pairs)
nf, npr = null_dim(A)
print(f"   general (non-isotropic) h^2 densities with <= 2 derivatives: {len(pairs)} monomials, {A.shape[0]} equations")
check("H1", nf == 0 and npr == 0, f"no non-zero h^2 density with <= 2 derivatives is pointwise invariant under the linear "
      f"gauge shift (null dim float {nf}, mod-p {npr}); with matter jets as pointwise coefficients this is C2's lemma "
      f"without the isotropy restriction")

# ---- positive control (ii): pure d^2 h x d^2 h block
J2 = [x for x in hjets(2) if len(x[1]) == 2]
pairs2 = [(J2[a], J2[b]) for a in range(len(J2)) for b in range(a, len(J2))]
A2 = build(pairs2)
nf2, np2 = null_dim(A2)
check("H2", nf2 == 21 and np2 == 21, f"control: d^2h x d^2h block ({len(pairs2)} monomials) has invariant subspace of dim "
      f"{nf2} (float) / {np2} (mod p); expected 21 = Sym^2 of the 6 linearised-Ricci components (d = 3)")

# ---- positive control (i): R1_ij R1_ij is annihilated (explicit vector)
def ricci1(i, j):
    """linearised Ricci R_ij = 1/2 (d_k d_i h_kj + d_k d_j h_ki - d_k d_k h_ij - d_i d_j h_kk) as {hjet: coeff}"""
    out = {}
    def add(c, a, v):
        key = ((min(c), max(c)), tuple(sorted(a)))
        out[key] = out.get(key, 0) + v
    for k in range(d):
        add((k, j), (k, i), 0.5); add((k, i), (k, j), 0.5); add((i, j), (k, k), -0.5); add((k, k), (i, j), -0.5)
    return out
idx = {p: n for n, p in enumerate(pairs2)}
vec = np.zeros(len(pairs2))
for i in range(d):
    for j in range(d):
        Ri = ricci1(i, j)
        for a, va in Ri.items():
            for b, vb in Ri.items():
                key = (a, b) if (a, b) in idx else (b, a)
                vec[idx[key]] += va * vb
check("H3", np.abs(A2.astype(float) @ vec).max() < 1e-12 and np.abs(vec).max() > 0,
      "control: the explicit 4-derivative invariant R1_ij R1_ij is annihilated by the engine -- so the lemma is sharp in "
      "derivative order: with 4 derivatives V2 is NOT fixed by V1 (e.g. sqrt g Ric^2 phi^2 is a free homogeneous seagull)")

# ---- scope: N constant (integration by parts allowed) -- the linearised EH density is invariant up to a divergence;
# shown here by the counter-statement that it is NOT pointwise invariant (it varies by a total derivative):
def fp_density():
    """L = 1/2 d_k h_ij d_k h_ij - d_k h_ki d_j h_ji + d_i h_ij d_j h - 1/2 d_k h d_k h  (Fierz-Pauli, linear EH quadratic)."""
    out = {}
    def add(c1, a1, c2, a2, v):
        k1 = ((min(c1), max(c1)), (a1,)); k2 = ((min(c2), max(c2)), (a2,))
        key = (k1, k2) if (k1, k2) in idx1 else (k2, k1)
        out[key] = out.get(key, 0) + v
    for i, j, k in itertools.product(range(d), repeat=3):
        add((i, j), k, (i, j), k, 0.5)
        add((k, i), k, (j, i), j, -1.0)
        add((i, j), i, (k, k), j, 1.0)
        add((i, i), k, (j, j), k, -0.5)
    return out
J1 = [x for x in hjets(1) if len(x[1]) == 1]
pairs1 = [(J1[a], J1[b]) for a in range(len(J1)) for b in range(a, len(J1))]
idx1 = {p: n for n, p in enumerate(pairs1)}
A1 = build(pairs1)
v1 = np.zeros(len(pairs1))
for key, v in fp_density().items():
    v1[idx1[key]] += v
check("H4", np.abs(A1.astype(float) @ v1).max() > 0.1,
      "scope: the Fierz-Pauli density (gauge invariant only up to a total derivative) is NOT pointwise invariant -- the "
      "'arbitrary N' quantifier is load-bearing: with constant N, phi^2 x FP would be a homogeneous solution")
print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.1f}s)")
