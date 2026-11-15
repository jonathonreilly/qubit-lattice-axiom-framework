#!/usr/bin/env python3
"""r55b_dip.py -- REVIEW55_BFTB (reviewer claude-opus-5-5). Criteria: checks/r55b_dip_criteria.md (written first).

Exact arithmetic only (fractions.Fraction, Python ints). No numpy, no BLAS, no floats in any verdict.
Independent construction: nothing is copied from bb9b/bb10/bb11.

Model: d = 2, L = 3, k = 2, coarse side T = 3 (level sides 27, 9, 3); roots = block centres;
linearised root map Q with ONE fixed axial order (coordinate 0 then 1):
  (Q A)(X, mu) = 3^{-2} sum_{y in B(X)} int_{T_y} A,  T_y = a(c_X -> y) . S_y . a(c_{X+e_mu} -> y + 3 e_mu)^{-1}.
"""
from fractions import Fraction as F
import random

d = 2
L = 3
K = 2
T = 3
SIDE = {l: T * L ** (K - l) for l in range(K + 1)}   # 27, 9, 3
OFF = (L - 1) // 2                                     # 1: block-centre offset
random.seed(5502)

results = []
def record(tag, ok, note=""):
    results.append((tag, ok, note))
    print(f"{tag}: {'PASS' if ok else 'FAIL'}  {note}", flush=True)

def wrap(l, z):
    n = SIDE[l]
    return tuple(c % n for c in z)

def sites(l):
    n = SIDE[l]
    return [(a, b) for a in range(n) for b in range(n)]

def links(l):
    return [(z, mu) for z in sites(l) for mu in range(d)]

def e(mu):
    return tuple(1 if i == mu else 0 for i in range(d))

def add(z, w, s=1):
    return tuple(a + s * b for a, b in zip(z, w))

def root(l, X):
    """level-l site (unwrapped integer coords) of the root of level-(l+1) site X (unwrapped)"""
    return tuple(L * c + OFF for c in X)

# ---------------- paths as lists of (wrapped link, sign) on level l ----------------
def step(l, z, mu, s):
    """one step from unwrapped site z in direction mu with sign s; returns (link, sign), new z"""
    if s > 0:
        return (wrap(l, z), mu), +1, add(z, e(mu))
    else:
        z2 = add(z, e(mu), -1)
        return (wrap(l, z2), mu), -1, z2

def axial(l, c, y):
    """axial path from c to y (unwrapped), coordinate 0 first, then 1; monotone in each"""
    out = []
    z = c
    for mu in range(d):
        while z[mu] != y[mu]:
            s = 1 if y[mu] > z[mu] else -1
            b, sg, z = step(l, z, mu, s)
            out.append((b, sg))
    assert z == y
    return out

def straight(l, y, mu, length):
    out = []
    z = y
    for _ in range(length):
        b, sg, z = step(l, z, mu, +1)
        out.append((b, sg))
    return out

def block(l, X):
    """unwrapped level-l sites of the block B(X) of unwrapped level-(l+1) site X"""
    base = tuple(L * c for c in X)
    return [add(base, (i, j)) for i in range(L) for j in range(L)]

def contours(l, X, mu):
    """list of contours T_y (each a list of (link, sign)) for level-(l+1) link (X, mu), X unwrapped"""
    cX = root(l, X)
    cY = root(l, add(X, e(mu)))
    out = []
    for y in block(l, X):
        y2 = add(y, e(mu), L)
        Ty = axial(l, cX, y) + straight(l, y, mu, L) + [(b, -sg) for (b, sg) in reversed(axial(l, cY, y2))]
        out.append(Ty)
    return out

def current(path, w=F(1)):
    J = {}
    for b, sg in path:
        J[b] = J.get(b, F(0)) + w * sg
    return {b: v for b, v in J.items() if v != 0}

def addto(A, B, w=F(1)):
    for b, v in B.items():
        A[b] = A.get(b, F(0)) + w * v
    return {b: v for b, v in A.items() if v != 0}

def Qmap(l, A):
    """level-l 1-form A (dict) -> level-(l+1) 1-form"""
    out = {}
    for (X, mu) in links(l + 1):
        s = F(0)
        for Ty in contours(l, X, mu):
            for b, sg in Ty:
                s += sg * A.get(b, F(0))
        out[(X, mu)] = s / (L ** d)
    return out

def QT_delta(l, X, mu):
    """Q_l^T delta_{(X,mu)}: level-l 1-form"""
    J = {}
    for Ty in contours(l, X, mu):
        J = addto(J, current(Ty), F(1, L ** d))
    return J

def QT(l, s):
    """Q_l^T s for a level-(l+1) 1-form s (dict)"""
    J = {}
    for (X, mu), v in s.items():
        if v != 0:
            J = addto(J, QT_delta(l, X, mu), v)
    return J

def dfun(l, lam):
    return {(z, mu): lam[wrap(l, add(z, e(mu)))] - lam[z] for (z, mu) in links(l)}

def dstar1(l, v):
    """d* on 1-forms -> functions: (d*v)(z) = sum_mu [v(z - e_mu, mu) - v(z, mu)]"""
    out = {z: F(0) for z in sites(l)}
    for (z, mu), val in v.items():
        out[z] -= val
        out[wrap(l, add(z, e(mu)))] += val
    return out

def d1(l, A):
    """d on 1-forms -> 2-forms (plaquette at z, directions (0,1))"""
    return {z: A.get((z, 0), F(0)) + A.get((wrap(l, add(z, e(0))), 1), F(0))
               - A.get((wrap(l, add(z, e(1))), 0), F(0)) - A.get((z, 1), F(0)) for z in sites(l)}

def dstar2(l, G):
    """transpose of d1: (d*G)(w,0) = G(w) - G(w - e1); (d*G)(w,1) = G(w - e0) - G(w)"""
    out = {}
    for z, g in G.items():
        if g == 0:
            continue
        # plaquette z touches: (z,0) +, (z+e0,1) +, (z+e1,0) -, (z,1) -
        for b, s in (((z, 0), 1), ((wrap(l, add(z, e(0))), 1), 1), ((wrap(l, add(z, e(1))), 0), -1), ((z, 1), -1)):
            out[b] = out.get(b, F(0)) + s * g
    return {b: v for b, v in out.items() if v != 0}

def ev(l, lam):
    """level-l function -> level-(l+1) function (evaluation at roots)"""
    return {X: lam[wrap(l, root(l, X))] for X in sites(l + 1)}

def evT(l, g):
    """level-(l+1) function -> level-l function placed at the roots"""
    out = {z: F(0) for z in sites(l)}
    for X, v in g.items():
        out[wrap(l, root(l, X))] += v
    return out

def pair(A, B):
    return sum((v * B.get(b, F(0)) for b, v in A.items()), F(0))

def rand_fun(l):
    return {z: F(random.randint(-5, 5)) for z in sites(l)}

def rand_form(l):
    return {b: F(random.randint(-5, 5)) for b in links(l)}

def gauss_solve(rows, rhs, nvar):
    """exact solve of rows (list of dict var->coef) x = rhs; returns solution list (free vars = 0) or None"""
    M = [dict(r) for r in rows]
    b = list(rhs)
    piv_of_row = []
    r = 0
    where = {}
    for c in range(nvar):
        p = None
        for i in range(r, len(M)):
            if M[i].get(c, F(0)) != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]; b[r], b[p] = b[p], b[r]
        pv = M[r][c]
        M[r] = {k: v / pv for k, v in M[r].items()}; b[r] = b[r] / pv
        for i in range(len(M)):
            if i != r and M[i].get(c, F(0)) != 0:
                f = M[i][c]
                for k, v in M[r].items():
                    M[i][k] = M[i].get(k, F(0)) - f * v
                M[i] = {k: v for k, v in M[i].items() if v != 0}
                b[i] = b[i] - f * b[r]
        where[c] = r
        r += 1
        if r == len(M):
            break
    for i in range(r, len(M)):
        if not M[i] and b[i] != 0:
            return None
        if M[i] and all(v == 0 for v in M[i].values()) and b[i] != 0:
            return None
    # check consistency of all rows
    x = [F(0)] * nvar
    for c, i in where.items():
        x[c] = b[i]
    for i, row in enumerate(rows):
        if sum((v * x[k] for k, v in row.items()), F(0)) != rhs[i]:
            return None
    return x

# ================================ D1 ================================
ok = True
for _ in range(5):
    lam = rand_fun(1)
    lhs = Qmap(1, dfun(1, lam))
    rhs = dfun(2, ev(1, lam))
    ok = ok and all(lhs[b] == rhs[b] for b in links(2))
ok0 = True
for _ in range(3):
    lam = rand_fun(0)
    lhs = Qmap(0, dfun(0, lam))
    rhs = dfun(1, ev(0, lam))
    ok0 = ok0 and all(lhs[b] == rhs[b] for b in links(1))
record("D1", ok and ok0, f"root covariance Q d = d ev exactly (level 1->2: {ok}; level 0->1: {ok0})")

# ================================ D2-D4, D8 ================================
Xc = (1, 1)
Gstore = {}
for mu in range(d):
    tag = f"[mu={mu}]"
    path = current(straight(1, root(1, Xc), mu, L))           # c_X -> c_X + 3 e_mu at level 1
    QTd = QT_delta(1, Xc, mu)
    v = addto(dict(path), QTd, F(-1))
    # (a) co-closed
    dv = dstar1(1, v)
    a_ok = all(val == 0 for val in dv.values())
    # (b) support in R = B(X) u B(X+e_mu) (unwrapped coordinates -> wrapped set)
    Rsites = set(wrap(1, z) for z in block(1, Xc) + block(1, add(Xc, e(mu))))
    b_ok = all((b[0] in Rsites) and (wrap(1, add(b[0], e(b[1]))) in Rsites) for b in v)
    # (c) solve d*G = v with G on plaquettes whose 4 corners lie in R
    plaqs = [z for z in sites(1)
             if all(wrap(1, add(z, w)) in Rsites for w in ((0, 0), (1, 0), (0, 1), (1, 1)))]
    pidx = {z: i for i, z in enumerate(plaqs)}
    # equations: for every level-1 link touched by some plaquette in plaqs, (d*G)(link) = v(link)
    touched = set()
    for z in plaqs:
        for b in ((z, 0), (wrap(1, add(z, e(0))), 1), (wrap(1, add(z, e(1))), 0), (z, 1)):
            touched.add(b)
    v_outside_ok = all(b in touched for b in v)               # v must vanish off the touched links
    rows, rhs = [], []
    for b in sorted(touched):
        row = {}
        for z in plaqs:
            Gz = {z: F(1)}
            val = dstar2(1, Gz).get(b, F(0))
            if val != 0:
                row[pidx[z]] = val
        rows.append(row); rhs.append(v.get(b, F(0)))
    sol = gauss_solve(rows, rhs, len(plaqs))
    c_ok = (sol is not None) and v_outside_ok
    G = {z: sol[pidx[z]] for z in plaqs} if sol is not None else {}
    G = {z: g for z, g in G.items() if g != 0}
    if sol is not None:
        c_ok = c_ok and (dstar2(1, G) == {b: val for b, val in v.items() if val != 0})
    Gstore[mu] = (path, G, v)
    # (d) identity on 20 random chains
    d_ok = True
    d4_fired = False
    d8_ok = True
    b_link = (Xc, mu)
    for _ in range(20):
        x1 = rand_form(1)
        lhs = pair(path, x1)
        Qx = Qmap(1, x1)[b_link]
        dx = d1(1, x1)
        rhs_ = Qx + sum((g * dx[z] for z, g in G.items()), F(0))
        d_ok = d_ok and (lhs == rhs_)
        if lhs != Qx:
            d4_fired = True
        # D8: <delta_b, r_1(x)> - <path, x_1> = -<G, dx_1>, with x_2 = 0 so r_1 = Q x_1
        d8_ok = d8_ok and (Qx - lhs == -sum((g * dx[z] for z, g in G.items()), F(0)))
    record("D2" + tag, a_ok and b_ok and c_ok and d_ok,
           f"(a) d*v=0:{a_ok} (b) supp v in R:{b_ok} (c) d*G=v solvable in R:{c_ok} (#plaq={len(plaqs)}, |supp G|={len(G)}, max|G|={max((abs(g) for g in G.values()), default=0)}) (d) identity on 20 chains:{d_ok}")
    # D3 non-vacuity
    Dpath = evT(0, dstar1(1, path))                            # D(S^j) for j_1 = path as a level-0 function
    D3 = (len(v) > 0) and (len(G) > 0) and any(val != 0 for val in Dpath.values())
    nz = sorted([z for z, val in Dpath.items() if val != 0])
    record("D3" + tag, D3, f"|supp v|={len(v)}, |supp G|={len(G)}, D(path) nonzero at level-0 sites {nz} (level-2 roots 9X+4)")
    record("D4" + tag + " control", d4_fired, "identity with G := 0 FAILS on some chain (control fires)" if d4_fired else "control did NOT fire")
    record("D8" + tag, d8_ok, "<delta_b, r_1(x)> - <path_b, x_1> = -<G, dx_1> on 20 chains")

# ================================ D5 ================================
mu = 0
b_link = (Xc, mu)
QTd = QT_delta(1, Xc, mu)
div = dstar1(1, QTd)                                          # d*(Q_1^T delta_b), level-1 function
delta_b = {b_link: F(1)}
pred = evT(1, dstar1(2, delta_b))                             # ev^{(1->2)T} d* delta_b
roots_l1 = set(wrap(1, root(1, X)) for X in sites(2))
nonzero = any(val != 0 for val in div.values())
rootsupp = all((val == 0) or (z in roots_l1) for z, val in div.items())
total0 = sum(div.values(), F(0)) == 0
equal = all(div[z] == pred[z] for z in sites(1))
D5_full = evT(0, div)                                         # D(S^s) as a level-0 function (S_0 = 0)
record("D5", nonzero and rootsupp and total0 and equal,
       f"d*(Q_1^T delta_b) nonzero:{nonzero}, root-supported:{rootsupp}, total 0:{total0}, = ev^T d* delta_b:{equal}; "
       f"D(S^s) nonzero at level-0 sites {sorted(z for z, v_ in D5_full.items() if v_ != 0)}")

# ================================ D6 ================================
ok6 = True
for _ in range(3):
    s0 = rand_form(1)
    S0 = QT(0, s0)                                            # level-0 1-form
    S1 = {b: -v_ for b, v_ in s0.items()}
    D = dstar1(0, S0)
    D = {z: D[z] + w for z, w in evT(0, dstar1(1, S1)).items()}
    ok6 = ok6 and all(val == 0 for val in D.values())
record("D6", ok6, "lower residual slot s_0 (random, 3 draws): D(S) = 0 at every level-0 site")

# ================================ D7 ================================
path0, G0, v0 = Gstore[0]
S1 = addto(dict(QT_delta(1, Xc, 0)), path0, F(-1))          # s_1 = delta_b contributes Q_1^T delta_b; j_1 = -path_b
DS = evT(0, dstar1(1, S1))                                    # S_0 = 0
DSj = evT(0, dstar1(1, {b: -val for b, val in path0.items()}))
c1 = all(val == 0 for val in DS.values())
c2 = any(val != 0 for val in DSj.values())
record("D7", c1 and c2, f"D(S) = 0 pointwise:{c1}; D(S^j) != 0 somewhere:{c2}  "
       f"(S = residual delta_b + plain current -path_b satisfies (CC-0) while its plain part does not)")

allpass = all(ok for tag, ok, _ in results)
print("VERDICT r55b_dip:", "ALL PASS (D4 controls fired)" if allpass else "NOT ALL PASS")
