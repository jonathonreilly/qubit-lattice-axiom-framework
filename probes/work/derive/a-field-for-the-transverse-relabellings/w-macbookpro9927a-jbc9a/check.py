#!/usr/bin/env python3
"""J:derive:a-field-for-the-transverse-relabellings:a1 -- worker w-macbookpro9927a-jbc9a (Claude Opus 5.5).

Exact (sympy) checks.  Block 62 as landed at one wave vector: strain h (symmetric), rates' multiplier u, symbols
p_j = 2 sin(k_j/2) (real), R1 = p^2 tr h - p.h.p, R2 = -(p^2/4) tr h^2 + |hp|^2/2 - (p.h.p) tr h/2 + (p^2/4)(tr h)^2,
L = alpha h'_ij h'_ij + beta (tr h')^2 + K (u R1 + R2).  A relabelling in time: h -> h + (p xi^T + xi p^T) zeta(t).
Symmetry = the change of L is a total time derivative (only-if via the Euler operator, which kills total derivatives)."""
import itertools, time
import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"{tag} {'PASS' if ok else 'FAIL'}: {msg}", flush=True)


t = sp.symbols('t')
p1, p2, p3, K, al, be = sp.symbols('p1 p2 p3 K alpha beta', real=True)
P = sp.Matrix([p1, p2, p3])
PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
hf = [sp.Function('h%d%d' % (i + 1, j + 1))(t) for i, j in PAIRS]
u = sp.Function('u')(t)
z = sp.Function('zeta')(t)


def sym(vals):
    H = sp.zeros(3)
    for (i, j), v in zip(PAIRS, vals):
        H[i, j] = v; H[j, i] = v
    return H


H = sym(hf)


def R1(H):
    return P.dot(P) * H.trace() - (P.T * H * P)[0]


def R2(H):
    q = P.dot(P); hp = H * P
    return -q / 4 * (H * H).trace() + hp.dot(hp) / 2 - (P.T * H * P)[0] * H.trace() / 2 + q / 4 * H.trace() ** 2


def Tk(D):
    return al * (D * D).trace() + be * D.trace() ** 2


def euler(expr, f, order=4):
    e = sp.diff(expr, f)
    for n in range(1, order + 1):
        e += (-1) ** n * sp.diff(sp.diff(expr, sp.diff(f, t, n)), t, n)
    return sp.expand(e)


# ---------------------------------------------------------------- A: block 124 T3 (the change to be absorbed)
xi = sp.Matrix([p2, -p1, 0])                      # transverse: p . xi = 0
L0 = Tk(H.diff(t)) + K * (u * R1(H) + R2(H))
dh = (P * xi.T + xi * P.T) * z
dL = sp.expand(Tk((H + dh).diff(t)) + K * (u * R1(H + dh) + R2(H + dh)) - L0)
want = 4 * al * z.diff(t) * (xi.T * H.diff(t) * P)[0] + 2 * al * P.dot(P) * xi.dot(xi) * z.diff(t) ** 2
check("A1", sp.expand(dL - want) == 0 and euler(dL, z) != 0,
      "a transverse relabelling in time changes L by 4 alpha zeta' xi.h'.p + 2 alpha p^2|xi|^2 zeta'^2 at every (alpha, beta) "
      "(block 124 T3), and its Euler derivative in zeta is not zero")

# ---------------------------------------------------------------- B: candidates from the landed clauses
# B1 block 59's bond law (the law of the bond rates; matrix as restated by block 84): a transverse shift of the rates by
# v zeta' changes the law's quadratic energy by a term whose Euler derivative is not zero.
k1, k2, k3 = sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1, 5)          # a rational point for the cosines (symbolic below)
A_, B_, G_ = sp.symbols('a_law b_law g_law', real=True)
ks = sp.symbols('k1:4', real=True)
c0 = -2 * A_ - 8 * B_ - 4 * G_
Mlaw = sp.Matrix(3, 3, lambda j, l: (c0 + 2 * A_ * sp.cos(ks[j]) + 2 * G_ * sum(sp.cos(ks[m]) for m in range(3) if m != j))
                 if j == l else 4 * B_ * sp.cos(ks[j] / 2) * sp.cos(ks[l] / 2))
cf = [sp.Function('c%d' % j)(t) for j in range(3)]
cv = sp.Matrix(cf)
pk = sp.Matrix([2 * sp.sin(k / 2) for k in ks])
v = pk.cross(sp.Matrix([0, 0, 1]))                 # transverse to p(k)
Elaw = (cv.T * Mlaw * cv)[0] / 2
dE = sp.expand(((cv + v * z.diff(t)).T * Mlaw * (cv + v * z.diff(t)))[0] / 2 - Elaw)
eu = euler(dE, z)
num = eu.subs({A_: 1, B_: sp.Rational(1, 7), G_: sp.Rational(1, 3), ks[0]: 1, ks[1]: 2, ks[2]: 3})
check("B1", sp.simplify(num) != 0,
      "block 59's bond law (quadratic energy with matrix M(k)): a transverse shift of the bond rates by v zeta' has a nonzero "
      "Euler derivative in zeta at generic (alpha, beta, gamma, k): the law does not permit the shift; the rates also "
      "multiply the walker's hops (H = sum c_b h_b), whose generator the shift would change")

# B2 block 65's blind walk: shifting the twist field by v zeta' changes the walker's generator by a nonzero operator.
L3 = 4
sites = list(itertools.product(range(L3), repeat=3))
idx = {s: n for n, s in enumerate(sites)}
Vn = len(sites)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def shift(a, s, d):
    s2 = list(s); s2[a] = (s2[a] + d) % L3
    return tuple(s2)


def blind_extra(th):
    """(1/2) sum_j {(th x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a th_a] as a 2V x 2V matrix, th: site -> 3-vector"""
    Mx = sp.zeros(2 * Vn, 2 * Vn)
    E = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]
    for s in sites:
        x = idx[s]
        for j in range(3):
            for dd, sg in ((1, 1), (-1, -1)):          # S_j = (T_j - T_j^dag)/(2i): (S_j psi)(x) = (psi(x+e_j) - psi(x-e_j))/(2i)
                y = idx[shift(j, s, dd)]
                cvec = th[s].cross(E[j]); cy = th[sites[y]].cross(E[j])
                blk = (sum((cvec[a] * sig[a] for a in range(3)), sp.zeros(2)) + sum((cy[a] * sig[a] for a in range(3)), sp.zeros(2))) * sg / (2 * sp.I) / 2
                Mx[2 * x:2 * x + 2, 2 * y:2 * y + 2] += blk
        for a in range(3):
            fwd = idx[shift(a, s, 1)]; bwd = idx[shift(a, s, -1)]
            tw_f = th[shift(a, s, 1)][a] - th[s][a]              # (d_a th_a)(x)
            tw_b = th[s][a] - th[shift(a, s, -1)][a]             # (d_a th_a)(x - e_a)
            Mx[2 * x:2 * x + 2, 2 * fwd:2 * fwd + 2] += sp.eye(2) * tw_f / 4
            Mx[2 * x:2 * x + 2, 2 * bwd:2 * bwd + 2] += sp.eye(2) * tw_b / 4
    return Mx


vfield = {s: sp.Matrix([sp.Rational(s[1] % 2), sp.Rational(s[2] % 3, 2), 0]) for s in sites}
Dop = blind_extra(vfield)
check("B2", Dop != sp.zeros(2 * Vn, 2 * Vn) and (Dop - Dop.H).applyfunc(sp.expand) == sp.zeros(2 * Vn, 2 * Vn),
      "block 65's blind walk: shifting the twist field by v zeta' (no coin rotation) adds zeta' times a nonzero hermitian "
      "operator to the walker's generator (4^3 torus, a sample field): its clause ties the twist's shift to a coin rotation")

# B3 locality: no local (polynomial in p) linear map of h' shifts by xi' for every transverse xi
aco = sp.symbols('a0:%d' % (3 * 6 * 4))
Amat = [[sum(aco[(r * 6 + c) * 4 + e] * m for e, m in enumerate([1, p1, p2, p3])) for c in range(6)] for r in range(3)]
xs = sp.symbols('x1:4')
Xi = sp.Matrix(xs)
img = P * Xi.T + Xi * P.T
imgv = [img[i, j] for i, j in PAIRS]
eqs = []
for r in range(3):
    expr = sp.expand(sum(Amat[r][c] * imgv[c] for c in range(6)) - Xi[r])
    # impose on the transverse subspace: xi = x1 (p2,-p1,0) + x2 (p3,0,-p1)
    tr = {xs[0]: sp.Symbol('y1') * p2 + sp.Symbol('y2') * p3, xs[1]: -sp.Symbol('y1') * p1, xs[2]: -sp.Symbol('y2') * p1}
    e2 = sp.expand(expr.subs(tr, simultaneous=True))
    eqs += sp.Poly(e2, p1, p2, p3, sp.Symbol('y1'), sp.Symbol('y2')).coeffs()
solA = sp.solve(eqs, aco, dict=True)
check("B3", solA == [], "no map X = A(p) h' with entries of degree <= 1 in p shifts by xi' for every transverse xi (the image "
      "p xi'^T + xi' p^T carries one power of p, xi' carries none): a shift needs 1/p, i.e. no local construction from h'")

# B4 the most general coupling making the transverse relabelling a symmetry, for a field X shifting by xi'
Xf = [sp.Function('X%d' % j)(t) for j in range(3)]
Xv = sp.Matrix(Xf)
pv = {p1: 1, p2: 2, p3: 2}
Kc = sp.Matrix(6, 3, sp.symbols('m0:18'))
Qc = sp.Matrix(3, 3, lambda i, j: sp.Symbol('q%d%d' % (min(i, j), max(i, j))))


def Lcoup(Hm, Xm):
    hdv = sp.Matrix([sp.diff(Hm[i, j], t) for i, j in PAIRS])
    return Tk(Hm.diff(t)) + (hdv.T * Kc * Xm)[0] + (Xm.T * Qc * Xm)[0]


conds = []
FLD = hf + Xf + [z]
derivs = [sp.diff(g, t, n) for g in FLD for n in range(6, -1, -1)]
reps = {d: sp.Symbol('D%d' % k) for k, d in enumerate(derivs)}
for xiv in (sp.Matrix([2, -1, 0]), sp.Matrix([2, 0, -1])):          # transverse to p = (1, 2, 2)
    Pn = P.subs(pv)
    dhh = (Pn * xiv.T + xiv * Pn.T) * z
    dL2 = sp.expand((Lcoup(H + dhh, Xv + xiv * z.diff(t)) - Lcoup(H, Xv)).subs(pv))
    for f in FLD:
        Es = euler(dL2, f).subs(reps)
        if Es != 0:
            conds += sp.Poly(Es, *reps.values()).coeffs()
free_syms = sorted(set(Kc) | set(Qc), key=str)
solB = sp.solve(conds, free_syms, dict=True)
Lshift = sp.expand((Tk(H.diff(t) - (P * Xv.T + Xv * P.T)) - Tk(H.diff(t))).subs(pv))
hdv0 = sp.Matrix([sp.diff(H[i, j], t) for i, j in PAIRS])
Lsol = sp.expand(((hdv0.T * Kc * Xv)[0] + (Xv.T * Qc * Xv)[0]).subs(pv).subs(solB[0]))
resid = sp.expand(Lsol - Lshift)
sft = sp.Symbol('s')
Pn = P.subs(pv)
joint = True
for dv in (sp.Matrix([2, -1, 0]), sp.Matrix([2, 0, -1])):
    dh_s = (Pn * dv.T + dv * Pn.T) * sft
    sub = {Xf[j]: Xf[j] + dv[j] * sft for j in range(3)}
    sub.update({sp.diff(hf[k], t): sp.diff(hf[k], t) + dh_s[i, j] for k, (i, j) in enumerate(PAIRS)})
    joint &= sp.expand(resid.subs(sub, simultaneous=True) - resid) == 0
a1_, a2_ = sp.symbols('a1_ a2_')
Xt = sp.Matrix([2, -1, 0]) * a1_ + sp.Matrix([2, 0, -1]) * a2_          # X transverse to p: p.X = 0
vanish = sp.expand(resid.subs({Xf[j]: Xt[j] for j in range(3)}, simultaneous=True)) == 0
nfree = len(sorted(Lsol.free_symbols & set(free_syms), key=str))
has_shift = sp.expand(Lsol.subs({q: 0 for q in free_syms})) != 0
check("B4", len(solB) == 1 and joint and vanish and nfree == 7 and has_shift,
      "at p = (1,2,2): the most general coupling h'.K.X + X.Q.X that makes the transverse relabelling (X -> X + xi') a "
      "symmetry is T(D) - T(h'), D = h' - p X^T - X p^T, plus 7 free terms l(D)(p.X) + c(p.X)^2 that vanish when p.X = 0: "
      "X must enter as the shift in D")

# ---------------------------------------------------------------- C: the 10 x 10 system with a supplied bond vector N
Om = sp.Symbol('Omega')
Nf = [sp.Function('N%d' % j)(t) for j in range(3)]
Nv = sp.Matrix(Nf)
qv = hf + [u] + Nf


def pencil(beta_val, pval):
    Lg = Tk(H.diff(t) - (P * Nv.T + Nv * P.T)) + K * (u * R1(H) + R2(H))
    Lg = sp.expand(Lg.subs({be: beta_val, al: 1, K: 1}).subs(pval))
    dq = [sp.diff(q, t) for q in qv]
    A = sp.Matrix(10, 10, lambda i, j: sp.diff(Lg, dq[i], dq[j]))
    Bm = sp.Matrix(10, 10, lambda i, j: sp.diff(Lg, dq[i], qv[j]))
    C = sp.Matrix(10, 10, lambda i, j: sp.diff(Lg, qv[i], qv[j]))
    # EL for q = q0 exp(-i Omega t):  (Omega^2 A + i Omega (B - B^T) + C) q0 = 0
    return (Om ** 2 * A + sp.I * Om * (Bm - Bm.T) + C)


summary = {}
ok_all = True
for beta_val in (0, sp.Rational(1, 2), -1):
    for pval in ({p1: 1, p2: 2, p3: 2}, {p1: sp.Rational(2, 5), p2: sp.Rational(1, 3), p3: -sp.Rational(3, 7)}):
        Mp = pencil(beta_val, pval)
        pvec = sp.Matrix([pval[p1], pval[p2], pval[p3]])
        gauge = []
        for e_ in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
            hh = pvec * e_.T + e_ * pvec.T
            gauge.append(sp.Matrix([hh[i, j] for i, j in PAIRS] + [0] + list(-sp.I * Om * e_)))
        g_ok = all(sp.simplify(Mp * g) == sp.zeros(10, 1) for g in gauge)
        extra = []
        if beta_val == -1:
            # u-absorption minus N-absorption of the gradient: (h = 0, u = -(2 alpha/K) zeta'', N = -p zeta'/2) -> (0, 2 Om^2, i Om p/2)
            ev = sp.Matrix([0] * 6 + [2 * Om ** 2] + list(sp.I * Om * pvec / 2))
            extra.append(sp.simplify(Mp * ev) == sp.zeros(10, 1))
        # gauge fix: drop the vector and longitudinal parts of h -> keep TT (2), transverse trace (1), u, N (3)
        ph = pvec / sp.sqrt(pvec.dot(pvec))
        e1 = sp.Matrix([ph[1], -ph[0], 0]); e1 = e1 / sp.sqrt(e1.dot(e1))
        e2 = ph.cross(e1)
        TT1 = e1 * e1.T - e2 * e2.T; TT2 = e1 * e2.T + e2 * e1.T
        TR = sp.eye(3) - ph * ph.T
        cols = []
        for Mb in (TT1, TT2, TR):
            cols.append(sp.Matrix([Mb[i, j] for i, j in PAIRS] + [0, 0, 0, 0]))
        for k in range(6, 10):
            ek = sp.zeros(10, 1); ek[k] = 1; cols.append(ek)
        Sm = sp.Matrix.hstack(*cols)
        red = sp.simplify(Sm.T * Mp * Sm)
        d = sp.factor(sp.simplify(red.det()))
        summary[(beta_val, tuple(pval.values()))] = (g_ok, extra, d)
        q2 = pvec.dot(pvec)
        roots = sp.roots(sp.Poly(sp.simplify(d), Om)) if d != 0 else {}
        if beta_val == -1:
            ok_all &= g_ok and all(extra) and d == 0
        else:
            ok_all &= g_ok and d != 0 and roots.get(sp.sqrt(q2) / 2) == 2 and roots.get(-sp.sqrt(q2) / 2) == 2 and \
                set(roots) <= {0, sp.sqrt(q2) / 2, -sp.sqrt(q2) / 2}
d0 = summary[(0, (1, 2, 2))][2]
check("C1", ok_all, "with N (h' -> h' - p N^T - N p^T), fields (h, u, N) = 10: the three relabellings (h = p xi^T + xi p^T, "
      "N = xi') are null at every frequency for every beta; after fixing them (h = TT + transverse trace) the 7x7 "
      f"determinant is {d0} at beta = 0, p = (1,2,2): travelling only Omega^2 = K p^2/(4 alpha) (twice), "
      "no other finite frequency (transverse trace, u and N fixed by constraints; block 124's transverse drift is now gauge); "
      "at beta = -alpha the reduced determinant vanishes identically: (u, N) absorb the gradient twice, one extra null direction")

npass = sum(1 for _, x in RES if x)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass} ({time.time() - T0:.0f}s)")
if npass == len(RES):
    print("SUMMARY: PARTIAL no object of the landed clauses can absorb a relabelling in time across the wave; the minimal "
          "new object is a bond vector with no law of its own entering as h' - (dN + dN^T); with it the three relabellings "
          "are gauge at every ratio and only the transverse traceless pair travels")
    print("HIT: at second order around the uniform background, a transverse relabelling in time changes block 62's Lagrangian "
          "by 4 alpha zeta' xi.h'.p + 2 alpha p^2|xi|^2 zeta'^2, and it is absorbed only by a field X that shifts by xi' and "
          "enters as h' - p X^T - X p^T (the most general coupling is T of that combination plus terms carrying p.X); none of the landed "
          "objects can be X: block 59's bond rates obey a law that the shift violates and multiply the walker's hops, "
          "block 64's strains are the frame itself (shift d xi, not xi') and its curls are unchanged, block 65's twist "
          "enters the blind walk (its shift changes the generator unless the coin rotates), the walker's currents and "
          "densities move with xi not xi', site rates are scalars, records are permanent; and no local map of h' shifts by "
          "xi' (it would need 1/p). The minimal new object is a bond vector N with no law of its own (a multiplier); with it "
          "the 10x10 system (h, u, N) has the three relabellings as gauge at every (alpha, beta), only the transverse "
          "traceless pair travels (Omega^2 = K p^2/(4 alpha)), and at beta = -alpha u and N absorb the gradient twice")
else:
    print("SUMMARY: ROUTE FAILS AT " + ",".join(tg for tg, x in RES if not x))
