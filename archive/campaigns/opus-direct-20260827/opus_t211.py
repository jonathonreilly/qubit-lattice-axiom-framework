"""
T211 - the tension.  Are R104's convex-consistency and Record consistency
compatible at all?

  Record consistency (a joint field over permanent records exists)
     + Markov + Z^3 triangle-free
     => mu = prod over EDGES phi(v_x,v_y)
     => the site rule is a PRODUCT over neighbours.

  Convex-consistency (R104): the rule's OUTPUT, as a map from a neighbour's
  state, is affine -- P(. | mixture) = mixture of P(. | .).
     => the site rule is affine in the SUM.

A product rule's normaliser Z depends on the neighbours, so the NORMALISED
product rule need not be affine.  Measured here, both ways, with the order in
lambda identified.
"""
import numpy as np, itertools

MENU = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], dtype=float)
M = len(MENU); DOT = MENU @ MENU.T

def nullspace_dim(A):
    """robust: eigen-decompose A^T A rather than SVD of a tall thin matrix"""
    G = A.T @ A
    w = np.linalg.eigvalsh(G)
    w = np.clip(w, 0, None)
    sv = np.sqrt(w)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    return int(np.sum(sv <= tol)), sv

def compat_dim(adj, cond, nsite):
    cfgs = list(itertools.product(range(M), repeat=nsite))
    idx = {c: i for i, c in enumerate(cfgs)}
    rows = []
    for i in range(nsite):
        for c in cfgs:
            r = np.zeros(len(cfgs)); r[idx[c]] += 1.0
            p = cond(i, c, adj)
            for s in range(M):
                cc = list(c); cc[i] = s
                r[idx[tuple(cc)]] -= p[c[i]]
            rows.append(r)
    return nullspace_dim(np.array(rows))

def make_cond(kind, lam):
    def cond(i, c, adj):
        ne = adj[i]; w = np.zeros(M)
        for s in range(M):
            if kind == "product": w[s] = np.prod([1+lam*DOT[s, c[j]] for j in ne])
            elif kind == "sum":   w[s] = 1 + lam*sum(DOT[s, c[j]] for j in ne)
        return w/np.sum(w)
    return cond

PATH3 = {0:[1], 1:[0,2], 2:[1]}

print("=== 1. the normaliser of the product rule is not constant ===")
print("   Z(b,c) = sum_s prod_y (1 + lam v_s.v_y)   for a site with 2 neighbours")
for lam in (0.1, 0.2, 0.4):
    Z = np.array([[sum((1+lam*DOT[s,b])*(1+lam*DOT[s,c]) for s in range(M))
                   for c in range(M)] for b in range(M)])
    pred = np.array([[6 + 2*lam**2*DOT[b,c] for c in range(M)] for b in range(M)])
    print(f"   lam={lam}: spread(Z) = {Z.max()-Z.min():.6f}   "
          f"matches 6 + 2 lam^2 (b.c) to {np.max(np.abs(Z-pred)):.2e}")

print("\n=== 2. is the NORMALISED product rule affine in each neighbour? ===")
print("   fit P(s | b,c) to the multi-affine span {1, b_i} x {1, c_j}; report residual")
BAS = []
for i in range(4):
    for j in range(4):
        F = np.zeros((M, M))
        for b in range(M):
            for c in range(M):
                cb = 1.0 if i == 0 else MENU[b][i-1]
                cc = 1.0 if j == 0 else MENU[c][j-1]
                F[b, c] = cb*cc
        BAS.append(F.ravel())
BAS = np.array(BAS).T
for kind in ("product", "sum"):
    print(f"   -- {kind} --")
    for lam in (0.05, 0.1, 0.2, 0.4):
        cond = make_cond(kind, lam)
        worst = 0.0
        for s in range(M):
            tgt = np.array([[cond(1, (b, s, c), PATH3)[s] for c in range(M)]
                            for b in range(M)]).ravel()
            co, *_ = np.linalg.lstsq(BAS, tgt, rcond=None)
            worst = max(worst, np.max(np.abs(BAS@co - tgt)))
        print(f"      lam={lam:5.2f}  max multi-affine fit residual = {worst:.3e}"
              f"   ({'AFFINE' if worst < 1e-12 else 'NOT affine'})")

print("\n=== 3. joint-field existence, and the order in lambda of the failure ===")
print("   kind      lam     nullspace dim    smallest sv")
prev = {}
for kind in ("product", "sum"):
    for lam in (0.0, 0.025, 0.05, 0.1, 0.2, 0.4):
        k, sv = compat_dim(PATH3, make_cond(kind, lam), 3)
        s = sv[0] if sv[0] > 0 else 0.0
        extra = ""
        if kind == "sum" and lam > 0 and prev.get("last"):
            lp, sp = prev["last"]
            extra = f"   ratio {(s/sp):.2f} for lam x{lam/lp:.0f} (lam^2 => {(lam/lp)**2:.0f})"
        print(f"   {kind:8s} {lam:5.3f}      {k:3d}         {s:.4e}{extra}")
        if kind == "sum" and lam > 0: prev["last"] = (lam, s)
