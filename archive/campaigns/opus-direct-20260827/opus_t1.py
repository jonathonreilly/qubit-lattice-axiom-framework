"""T1 — THE UNIFORM-WEIGHT (VOLUME) THEOREM, general form.
Carrier: on the exterior algebra of R^d, put degree-k weight
    W_k = rho_k * Lambda^k(g^-1)      (Lambda^k = the induced minor metric)
with INDEPENDENT positive scalars rho_k.  Gamma_a = eps_a + eps_a^ddagger
(adjoint w.r.t. this weight).  QUESTION: for which rho does the Clifford
relation {Gamma_a, Gamma_b} = 2 (g^-1)_{ab} hold?
PREDICTION: iff all rho_k are equal.  The landed D3 carrier has
rho = (V, V, det g / V, det g / V), so closure <=> V^2 = det g."""
import sympy as sp
from itertools import combinations

def basis(d):
    out = []
    for k in range(d + 1):
        out += [tuple(c) for c in combinations(range(d), k)]
    return out

def lam(ginv, I, J):
    if len(I) != len(J): return sp.Integer(0)
    if len(I) == 0: return sp.Integer(1)
    return sp.Matrix(len(I), len(I), lambda a, b: ginv[I[a], J[b]]).det()

def build(d, g, rho):
    B = basis(d); n = len(B); idx = {b: i for i, b in enumerate(B)}
    ginv = sp.together(g.inv())
    D = sp.zeros(n, n)
    for I in B:
        for J in B:
            if len(I) == len(J):
                D[idx[I], idx[J]] = sp.cancel(rho[len(I)] * lam(ginv, I, J))
    def eps(a):
        M = sp.zeros(n, n)
        for S in B:
            if a in S: continue
            T = tuple(sorted(S + (a,)))
            M[idx[T], idx[S]] = (-1) ** sum(1 for i in S if i < a)
        return M
    return B, idx, D, ginv, eps

for d in (2, 3):
    print(f"\n===== d = {d}", flush=True)
    if d == 2:
        c = sp.Symbol("c"); g = sp.Matrix([[1, c], [c, 1]])
    else:
        ctx, cty, cxy = sp.symbols("c_tx c_ty c_xy")
        g = sp.Matrix([[1, ctx, cty], [ctx, 1, cxy], [cty, cxy, 1]])
    rho = sp.symbols(f"rho0:{d+1}", positive=True)
    B, idx, D, ginv, eps = build(d, g, rho)
    Dinv = sp.together(D.inv())
    Gam = [sp.Matrix(sp.expand(eps(a) + Dinv * eps(a).T * D)) for a in range(d)]
    conds = set()
    n = len(B)
    for a in range(d):
        for b in range(d):
            AC = sp.expand(Gam[a] * Gam[b] + Gam[b] * Gam[a])
            tgt = sp.expand(2 * ginv[a, b] * sp.eye(n))
            for i in range(n):
                for j in range(n):
                    r = sp.cancel(sp.together(AC[i, j] - tgt[i, j]))
                    if r != 0:
                        num = sp.factor(sp.numer(r))
                        conds.add(num)
    if not conds:
        print("  Clifford relation holds for ARBITRARY rho (unexpected)", flush=True)
    else:
        # reduce: collect the distinct irreducible factors involving rho
        facs = set()
        for cnd in conds:
            for f, _ in sp.factor_list(cnd)[1]:
                if f.free_symbols & set(rho):
                    facs.add(sp.expand(f))
        print(f"  rho-conditions (distinct irreducible factors that must vanish):", flush=True)
        for f in sorted(facs, key=str):
            print(f"     0 = {f}", flush=True)
    # now impose the LANDED two-half assignment and read the selector
    V = sp.Symbol("V", positive=True)
    detg = sp.factor(sp.expand(g.det()))
    half = {rho[k]: (V if k <= d // 2 and (d % 2 == 1 or k < d/2) else detg / V) for k in range(d + 1)}
    # landed convention: lower half V, upper half det g / V (d=3: k<=1 -> V; d=2: k=0 -> V, k=2 -> detg/V, k=1 = middle)
    if d == 3:
        half = {rho[0]: V, rho[1]: V, rho[2]: detg / V, rho[3]: detg / V}
    else:
        half = {rho[0]: V, rho[1]: V, rho[2]: detg / V}
    sub = [sp.factor(sp.simplify(f.subs(half))) for f in facs]
    print(f"  landed two-half assignment rho = {[sp.factor(half[r]) for r in rho]}", flush=True)
    print(f"  => selector conditions: {sorted({str(s) for s in sub})}", flush=True)
    print(f"  det g = {detg}", flush=True)
