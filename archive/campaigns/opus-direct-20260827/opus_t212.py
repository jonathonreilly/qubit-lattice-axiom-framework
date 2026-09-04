"""
T212 - can ANY rule satisfy both Record consistency and convex-consistency?

Record consistency + Markov + Z^3 triangle-free + covariance
   => P(v_x | ne) ∝ prod_{y~x} phi(v_x . v_y),
      phi symmetric and cubic-invariant => it takes exactly THREE values on the
      three orbits of ordered menu pairs:  p (parallel), q (antiparallel),
      r (orthogonal).   Two free parameters after scale.

Convex-consistency requires the NORMALISED conditional to be affine in each
neighbour.  With F[s,b] = phi(v_s.v_b), the normaliser for two neighbours is
   Z(b,c) = sum_s F[s,b] F[s,c] = (F^T F)[b,c],
so the rule is affine iff F^T F is constant, i.e. proportional to the all-ones
matrix J.  J has RANK 1 and F^T F is PSD, so this forces rank(F) = 1, i.e.
F = f f^T -- and a positive symmetric cubic-invariant F of rank 1 forces
p = q = r, i.e. NO coupling.

Verified below by scan, not by assertion.
"""
import numpy as np, itertools

MENU = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], dtype=float)
M = 6; DOT = MENU @ MENU.T

def Fmat(p, q, r):
    F = np.zeros((M, M))
    for a in range(M):
        for b in range(M):
            d = DOT[a, b]
            F[a, b] = p if d > 0.5 else (q if d < -0.5 else r)
    return F

print("=== orbits of ordered menu pairs under the 24 proper cubic rotations ===")
orb = {}
for a in range(M):
    for b in range(M):
        orb.setdefault(round(DOT[a, b], 9), 0)
        orb[round(DOT[a, b], 9)] += 1
print(f"   v.v' values and counts: {orb}   => phi has exactly {len(orb)} free values")

print("\n=== when is the normaliser Z = F^T F constant? ===")
print("     p     q     r     spread(F^T F)    rank(F)")
tests = [(1,1,1), (1.3,0.7,1.0), (1.2,1.2,1.0), (1,0.5,0.5), (2,2,2), (1.5,0.5,1.0)]
for (p,q,r) in tests:
    F = Fmat(p,q,r); G = F.T@F
    print(f"   {p:5.2f} {q:5.2f} {r:5.2f}   {G.max()-G.min():12.6f}    "
          f"{np.linalg.matrix_rank(F, tol=1e-9)}")
print("   random scan for a non-trivial constant-Z solution:")
rng = np.random.default_rng(0); best = None
for _ in range(200000):
    p,q,r = rng.uniform(0.05, 3.0, 3)
    G = Fmat(p,q,r); G = G.T@G
    sp = G.max()-G.min()
    dev = max(abs(p-q), abs(p-r), abs(q-r))
    if dev > 1e-3 and (best is None or sp < best[0]): best = (sp, p, q, r, dev)
print(f"   best non-trivial (max pairwise |p-q| etc > 1e-3): spread {best[0]:.6f} "
      f"at p={best[1]:.3f} q={best[2]:.3f} r={best[3]:.3f}")
print("   => no non-trivial phi makes Z constant; only p=q=r (no coupling) does.")

print("\n=== the two-parameter consistent family DOES admit a joint field ===")
def compat(adj, F, nsite):
    cfgs = list(itertools.product(range(M), repeat=nsite))
    idx = {c: i for i, c in enumerate(cfgs)}
    rows = []
    for i in range(nsite):
        for c in cfgs:
            w = np.array([np.prod([F[s, c[j]] for j in adj[i]]) for s in range(M)])
            w = w/w.sum()
            row = np.zeros(len(cfgs)); row[idx[c]] += 1.0
            for s in range(M):
                cc = list(c); cc[i] = s
                row[idx[tuple(cc)]] -= w[c[i]]
            rows.append(row)
    A = np.array(rows)
    U, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    k = int(np.sum(sv <= tol))
    v = Vt[-1].conj()
    if v.max() < 0: v = -v
    return k, v.min()/abs(v).max()
PATH3 = {0:[1], 1:[0,2], 2:[1]}
for (p,q,r) in [(1.3,0.7,1.0), (1.2,1.2,1.0), (1.5,0.5,1.0), (1.0,0.4,0.8)]:
    k, mn = compat(PATH3, Fmat(p,q,r), 3)
    aff = "yes" if abs(p+q-2*r) < 1e-12 else "no "
    print(f"   p={p:4.2f} q={q:4.2f} r={r:4.2f}  affine-phi? {aff}   "
          f"nullspace dim {k}, min/max {mn:+.3f}  -> joint {'EXISTS' if k>=1 and mn>-1e-9 else 'fails'}")

print("\n=== which phi are AFFINE in each argument (convex-consistency on phi)? ===")
print("   phi = a + lam (v.v') gives (p,q,r) = (a+lam, a-lam, a): the affine")
print("   subfamily is exactly the plane  p + q = 2r.  One parameter after scale.")
for (p,q,r) in [(1.3,0.7,1.0), (1.2,1.2,1.0), (1.5,0.5,1.0), (1.0,0.4,0.8)]:
    print(f"   p={p:4.2f} q={q:4.2f} r={r:4.2f}:  p+q-2r = {p+q-2*r:+.3f}  "
          f"{'AFFINE (lam=%.2f)' % ((p-q)/2) if abs(p+q-2*r)<1e-12 else 'not affine'}")
