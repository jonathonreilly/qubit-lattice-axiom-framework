"""Block 60's curvature member solved self-consistently with moving records as its sources.

Clause (supplied): H = m sum_{x in C} w_x + sum_{b in dC} g(kappa_b), kappa_b = sqrt(w_x w_y)/(chi_x chi_y) (block 110's
crossing factor), dC = interior bonds with exactly one end occupied, g(k) = g1 (k-1) + g2 (k-1)^2/2 + g3 (k-1)^3/6 + ...
Block 171's clauses: rest only (g = 0) and activity (g = mu k/2, i.e. g1 = mu/2, g2 = g3 = 0 up to a constant).
Member (block 60 T4 bond form, block 110 T2(a) site equations), walls held at w = l = 1, eps = 1/(8K).
Exact sections A-C (sympy / Fractions); floating-point sections D-E labelled.
"""
import sys, time, itertools
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)

def box(L):
    interior = [p for p in itertools.product(range(L), repeat=3) if all(0 < c < L - 1 for c in p)]
    idx = {p: i for i, p in enumerate(interior)}
    nbrs = {p: [tuple(p[k] + (d if k == a else 0) for k in range(3)) for a in range(3) for d in (-1, 1)] for p in interior}
    ibonds = sorted({tuple(sorted((p, q))) for p in interior for q in nbrs[p] if q in idx})
    return interior, idx, nbrs, ibonds

# ---------------------------------------------------------------------------------------------
# A. The member's site equations from its bond form, with the record clause (exact, symbolic)
# ---------------------------------------------------------------------------------------------
print("== A. site equations from F + H (exact, symbolic, side-4 box: 8 interior sites)")
K, m, g1, g2, g3 = sp.symbols('K m g1 g2 g3', positive=True)
L = 4
interior, idx, nbrs, ibonds = box(L)
U = {p: sp.Symbol('u_%d%d%d' % p, real=True) for p in interior}
C = {p: sp.Symbol('c_%d%d%d' % p, positive=True) for p in interior}
def wv(p): return sp.exp(U[p]) if p in U else sp.Integer(1)
def cv(p): return C[p] if p in C else sp.Integer(1)
allbonds = sorted({tuple(sorted((p, q))) for p in interior for q in nbrs[p]})
F = -8 * K * sum((wv(q) * cv(q) - wv(p) * cv(p)) * (cv(q) - cv(p)) for p, q in allbonds)
conf = {(1, 1, 1), (2, 1, 1), (1, 2, 2)}
dC = [(p, q) for p, q in ibonds if (p in conf) != (q in conf)]
def g(k): return g1 * (k - 1) + g2 * (k - 1)**2 / 2 + g3 * (k - 1)**3 / 6
def gp(k): return g1 + g2 * (k - 1) + g3 * (k - 1)**2 / 2
kap = {b: sp.exp((U[b[0]] + U[b[1]]) / 2) / (C[b[0]] * C[b[1]]) for b in dC}
H = m * sum(wv(p) for p in conf) + sum(g(kap[b]) for b in dC)
ok_all = True
for p in interior:
    lap_c = sum(cv(q) for q in nbrs[p]) - 6 * cv(p)
    lap_N = sum(wv(q) * cv(q) for q in nbrs[p]) - 6 * wv(p) * cv(p)
    e_p = m * wv(p) * (1 if p in conf else 0) + sum(gp(kap[b]) * kap[b] / 2 for b in dC if p in b)
    tau_p = sum(gp(kap[b]) * kap[b] / 2 for b in dC if p in b)
    ok_all &= sp.simplify(sp.diff(F, U[p]) - 8 * K * wv(p) * cv(p) * lap_c) == 0
    ok_all &= sp.simplify(sp.diff(F, C[p]) - 8 * K * (wv(p) * lap_c + lap_N)) == 0
    ok_all &= sp.simplify(sp.diff(H, U[p]) - e_p) == 0
    ok_all &= sp.simplify(-C[p] / 2 * sp.diff(H, C[p]) - tau_p) == 0
want(ok_all, "A1 dF/du = 8K w chi Lap chi, dF/dchi = 8K(w Lap chi + Lap N); the clause gives e = m w n + sum_b g'(k)k/2, tau = sum_b g'(k)k/2 "
     "(lambda = 2 log chi); so stationarity is Lap chi = -e/(8K w chi), Lap N = (e + 2 tau)/(8K chi) (block 110 T2(a))")
mu = sp.Symbol('mu', positive=True)
H_act = m * sum(wv(p) for p in conf) + sum(mu * kap[b] / 2 for b in dC)          # block 171's activity clause
H_chg = m * sum(wv(p) for p in conf) + sum(mu * (kap[b] - 1) / 2 for b in dC)    # only the field's change of the activity
same = all(sp.simplify(sp.diff(H_act - H_chg, U[p])) == 0 and sp.simplify(sp.diff(H_act - H_chg, C[p])) == 0 for p in interior)
tau_act = {p: sp.simplify(-C[p] / 2 * sp.diff(H_act, C[p])) for p in interior}
want(same and all(sp.simplify(tau_act[p].subs({U[q]: 0 for q in interior}).subs({C[q]: 1 for q in interior})
                              - mu * sum(1 for b in dC if p in b) / 4) == 0 for p in interior),
     "A2 the field's change of the crossing activity, (mu/2) sum (k - 1), has the same (e, tau) as block 171's activity clause; "
     "at zero field tau = mu/4 per movable bond end: its hop energy vanishes with the field, its tau does not")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. Self-consistent solution as an exact series in eps = 1/(8K) (side-5 box: 27 interior sites)
# ---------------------------------------------------------------------------------------------
print("== B. exact self-consistent series (eps = 1/8K) on the side-5 box")
from sympy.polys.matrices import DomainMatrix
eps = sp.Symbol('eps')
def green(L):
    interior, idx, nbrs, ibonds = box(L); n = len(interior)
    rows = [[0] * n for _ in range(n)]
    for p in interior:
        i = idx[p]; rows[i][i] = 6
        for q in nbrs[p]:
            if q in idx: rows[i][idx[q]] = -1
    Minv = DomainMatrix([[sp.Integer(v) for v in r] for r in rows], (n, n), sp.QQ).inv().to_Matrix()
    return interior, idx, nbrs, ibonds, Minv
ORD = 3
def tr(e, k=ORD):
    e = sp.expand(e)
    return sum(e.coeff(eps, j) * eps**j for j in range(k + 1))
def inv1(a, k):       # 1/(1 + a), a = O(eps)
    return tr(1 - a + a**2 - a**3, k)
def sqrt1(a, k):      # sqrt(1 + a)
    return tr(1 + a / 2 - a**2 / 8 + a**3 / 16, k)
def solve_series(L, conf, G_=None, gsyms=(g1, g2, g3)):
    interior, idx, nbrs, ibonds, Ginv = G_
    n = len(interior)
    dC = [(p, q) for p, q in ibonds if (p in conf) != (q in conf)]
    G1_, G2_, G3_ = gsyms
    chi = {p: sp.Integer(1) for p in interior}; N = {p: sp.Integer(1) for p in interior}
    def sources(chi, N, k):
        ic = {p: inv1(chi[p] - 1, k) for p in interior}
        w = {p: tr(N[p] * ic[p], k) for p in interior}
        kap = {b: tr(sqrt1(tr(w[b[0]] * w[b[1]] - 1, k), k) * ic[b[0]] * ic[b[1]], k) for b in dC}
        hop = {b: tr((G1_ + G2_ * (kap[b] - 1) + G3_ * (kap[b] - 1)**2 / 2) * kap[b] / 2, k) for b in dC}
        e = {p: tr(m * w[p] * (1 if p in conf else 0) + sum(hop[b] for b in dC if p in b), k) for p in interior}
        tau = {p: sum((hop[b] for b in dC if p in b), sp.Integer(0)) for p in interior}
        iw = {p: tr(chi[p] * inv1(N[p] - 1, k), k) for p in interior}   # 1/w = chi/N
        r1 = {p: tr(e[p] * iw[p] * ic[p], k) for p in interior}          # e/(w chi)
        r2 = {p: tr((e[p] + 2 * tau[p]) * ic[p], k) for p in interior}   # (e + 2 tau)/chi
        return r1, r2, e, tau, w
    for it in range(ORD - 1):     # fields correct to eps^(it+1)
        r1, r2, *_ = sources(chi, N, it)
        v1 = sp.Matrix([r1[p] for p in interior]); v2 = sp.Matrix([r2[p] for p in interior])
        s1 = Ginv * v1; s2 = Ginv * v2
        chi = {p: tr(1 + eps * s1[idx[p]], it + 1) for p in interior}
        N = {p: tr(1 - eps * s2[idx[p]], it + 1) for p in interior}
    r1, r2, e, tau, w = sources(chi, N, ORD - 1)
    PmQ = tr(eps * sum(r2[p] - r1[p] for p in interior), ORD)
    return PmQ, dC, chi, N
interior5, idx5, nbrs5, ibonds5, Ginv5 = G5 = green(5)
def nGn_S(conf, G_):
    interior, idx, nbrs, ibonds, Ginv = G_
    nv = sp.Matrix([1 if p in conf else 0 for p in interior]); Gn = Ginv * nv
    dC = [(p, q) for p, q in ibonds if (p in conf) != (q in conf)]
    return (nv.T * Gn)[0], sum(Gn[idx[p]] + Gn[idx[q]] for p, q in dC), len(dC)
tests = [{(2, 2, 2)}, {(1, 1, 1)}, {(2, 2, 2), (2, 2, 3)}, {(1, 1, 1), (3, 3, 3)}, {(1, 2, 3), (2, 2, 2), (3, 2, 1)}]
for conf in tests:
    PmQ, dC, chi, N = solve_series(5, conf, G5)
    nGn, S, B = nGn_S(conf, G5)
    c1 = sp.simplify(PmQ.coeff(eps, 1)); c2 = sp.simplify(PmQ.coeff(eps, 2).subs(g1, 0))
    want(sp.simplify(c1 - 2 * g1 * B) == 0, f"B1 conf {sorted(conf)}: [eps^1](P - Q) = 2 g'(1) B = {2*B} g1 (B = {B} movable bonds)")
    want(sp.simplify(c2 - (-4 * m * g2 * S - 2 * m**2 * nGn)) == 0,
         f"B2 conf {sorted(conf)}: at g'(1)=0, [eps^2](P - Q) = -4 m g''(1) S - 2 m^2 n.Gn, S = {S}, n.Gn = {nGn}")
PmQc, *_ = solve_series(5, {(2, 2, 2)}, G5)
c3 = sp.factor(sp.simplify(PmQc.coeff(eps, 3).subs(g1, 0)))
nGn_c, S_c, B_c = nGn_S({(2, 2, 2)}, G5)
g2star_c = -m * nGn_c / (2 * S_c)
c3_at = sp.factor(sp.simplify(c3.subs(g2, g2star_c)))
want(sp.diff(c3_at, g3) != 0, f"B3 centre record, g'(1) = 0, g''(1) tuned: [eps^3](P - Q) = {c3_at} (depends on g'''(1): each order needs its own tuning)")
print("   [A-B took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# C. What balances: exact values on the side-5 box (uniform law) and the side-6 box
# ---------------------------------------------------------------------------------------------
print("== C. balance at the first nonvanishing order (exact)")
def fast(G_):
    interior, idx, nbrs, ibonds, Ginv = G_
    n = len(interior); Gf = [[Fr(int(sp.numer(Ginv[i, j])), int(sp.denom(Ginv[i, j]))) for j in range(n)] for i in range(n)]
    def f(conf):
        occ = [idx[p] for p in conf]
        Gn = [sum(Gf[i][j] for j in occ) for i in range(n)]
        nGn = sum(Gn[i] for i in occ)
        dC = [(idx[p], idx[q]) for p, q in ibonds if (p in conf) != (q in conf)]
        return nGn, sum(Gn[i] + Gn[j] for i, j in dC), len(dC)
    return f
fast5 = fast(G5)
def nGn_S(conf, G_, _cache={}):
    if G_ is G5:
        a, b, c = fast5(conf); return sp.Rational(a.numerator, a.denominator), sp.Rational(b.numerator, b.denominator), c
    interior, idx, nbrs, ibonds, Ginv = G_
    nv = sp.Matrix([1 if p in conf else 0 for p in interior]); Gn = Ginv * nv
    dC = [(p, q) for p, q in ibonds if (p in conf) != (q in conf)]
    return (nv.T * Gn)[0], sum(Gn[idx[p]] + Gn[idx[q]] for p, q in dC), len(dC)
def gstar(conf, G_):
    nGn, S, B = nGn_S(conf, G_)
    return None if S == 0 else sp.nsimplify(-nGn / (2 * S))
classes = {'centre': {(2, 2, 2)}, 'face': {(1, 2, 2)}, 'edge': {(1, 1, 2)}, 'corner': {(1, 1, 1)}}
vals = {k: gstar(c, G5) for k, c in classes.items()}
print("   single record, g''(1)*/m by site:", vals)
want(len(set(vals.values())) == 4 and all(v < 0 for v in vals.values()), "C1 single record on side 5: the balancing curvature is negative and differs at every site class")
def law_avg(Nrec, G_):
    interior = G_[0]; tot_nGn = Fr(0); tot_S = Fr(0); cnt = 0
    for cf in itertools.combinations(interior, Nrec):
        a, b, c = fast5(set(cf)); tot_nGn += a; tot_S += b; cnt += 1
    A = tot_nGn / cnt; Sv = tot_S / cnt
    return sp.Rational(A.numerator, A.denominator), sp.Rational(Sv.numerator, Sv.denominator)
law = {}
for Nrec in (1, 2, 3):
    a_, s_ = law_avg(Nrec, G5); law[Nrec] = sp.nsimplify(-a_ / (2 * s_))
    print(f"   uniform law, N = {Nrec}: <n.Gn> = {a_}, <S> = {s_}, balancing g''(1)/m = {law[Nrec]} = {float(law[Nrec]):.6f}")
want(len(set(law.values())) == 3, "C2 uniform law on side 5: the balancing curvature differs for N = 1, 2, 3, so no clause fixed once balances two bodies")
# every linear or convex clause, and the jammed box, give P < Q at the first nonvanishing order
full = set(interior5)
nGn_f, S_f, B_f = nGn_S(full, G5)
want(S_f == 0 and B_f == 0 and nGn_f > 0, "C3 a jammed box (every interior site occupied) has no movable bond: [eps^2](P-Q) = -2 m^2 n.Gn < 0")
ok = True
for cf in itertools.combinations(interior5, 2):
    nGn, S, B = nGn_S(set(cf), G5)
    ok &= (nGn > 0 and S > 0)
want(ok, "C4 every two-record configuration on side 5 has n.Gn > 0 and S > 0: g''(1) >= 0 (linear, convex, rest only) gives P < Q at order eps^2")
G6 = green(6)
v6 = gstar({(2, 2, 2)}, G6); v6b = gstar({(2, 2, 2), (3, 3, 3)}, G6)
want(v6 != vals['centre'] and v6 != v6b, f"C5 side 6: near-centre single record {v6}, pair {v6b}: the box also moves the value")
print("   [A-C took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# D. FLOATING POINT: the full nonlinear self-consistent member (Newton) against the series
# ---------------------------------------------------------------------------------------------
print("== D. FLOATING POINT: nonlinear site equations solved by Newton vs the exact series")
import numpy as np
from scipy.optimize import fsolve
def nonlinear(L, conf, mm, gg1, gg2, gg3, ep):
    interior, idx, nbrs, ibonds = box(L); n = len(interior)
    dC = [(p, q) for p, q in ibonds if (p in conf) != (q in conf)]
    occ = np.array([1.0 if p in conf else 0.0 for p in interior])
    def unpack(v): return v[:n], v[n:]
    def resid(v):
        chi, N = unpack(v); w = N / chi
        e = mm * w * occ; tau = np.zeros(n)
        for p, q in dC:
            i, j = idx[p], idx[q]; k = np.sqrt(w[i] * w[j]) / (chi[i] * chi[j])
            hh = (gg1 + gg2 * (k - 1) + gg3 * (k - 1)**2 / 2) * k / 2
            e[i] += hh; e[j] += hh; tau[i] += hh; tau[j] += hh
        lc = -6 * chi.copy(); lN = -6 * N.copy()
        for p in interior:
            i = idx[p]
            for q in nbrs[p]:
                lc[i] += chi[idx[q]] if q in idx else 1.0
                lN[i] += N[idx[q]] if q in idx else 1.0
        return np.concatenate([lc + ep * e / (w * chi), lN - ep * (e + 2 * tau) / chi])
    v = fsolve(resid, np.ones(2 * n), xtol=1e-14)
    chi, N = unpack(v); w = N / chi
    e = mm * w * occ; tau = np.zeros(n)
    for p, q in dC:
        i, j = idx[p], idx[q]; k = np.sqrt(w[i] * w[j]) / (chi[i] * chi[j])
        hh = (gg1 + gg2 * (k - 1) + gg3 * (k - 1)**2 / 2) * k / 2
        e[i] += hh; e[j] += hh; tau[i] += hh; tau[j] += hh
    return ep * np.sum((e + 2 * tau) / chi - e / (w * chi)), np.max(np.abs(resid(v)))
g2c = float(g2star_c.subs(m, 1))
c3num = float(c3_at.subs({m: 1, g3: 0}))
c2rest = float(-2 * nGn_c)
rows = []
for ep in (0.04, 0.02, 0.01):
    pq_t, r_t = nonlinear(5, {(2, 2, 2)}, 1.0, 0.0, g2c, 0.0, ep)
    pq_r, r_r = nonlinear(5, {(2, 2, 2)}, 1.0, 0.0, 0.0, 0.0, ep)
    rows.append((ep, pq_t / ep**3, pq_r / ep**2))
    print(f"   eps={ep}: tuned (P-Q)/eps^3 = {pq_t/ep**3:.6f} (series {c3num:.6f}); rest only (P-Q)/eps^2 = {pq_r/ep**2:.6f} (series {c2rest:.6f}); residuals {r_t:.1e}, {r_r:.1e}")
want(abs(rows[-1][1] - c3num) < 0.05 * abs(c3num) + 1e-3 and abs(rows[-1][2] - c2rest) < 0.05 * abs(c2rest),
     "D1 the nonlinear self-consistent member reproduces the series: tuned curvature leaves only the eps^3 term; rest only gives -2 m^2 G(0) eps^2")

# ---------------------------------------------------------------------------------------------
# E. FLOATING POINT: dilute versus compact bodies on a larger box
# ---------------------------------------------------------------------------------------------
print("== E. FLOATING POINT: balancing curvature for dilute and compact bodies (side 17 box)")
import scipy.sparse as sps, scipy.sparse.linalg as spl
Lb = 17
interiorB, idxB, nbrsB, ibondsB = box(Lb); nB = len(interiorB)
Arows, Acols, Avals = [], [], []
for p in interiorB:
    i = idxB[p]; Arows.append(i); Acols.append(i); Avals.append(6.0)
    for q in nbrsB[p]:
        if q in idxB: Arows.append(i); Acols.append(idxB[q]); Avals.append(-1.0)
A = sps.csc_matrix((Avals, (Arows, Acols)), shape=(nB, nB)); lu = spl.splu(A)
def gstar_f(conf):
    nv = np.array([1.0 if p in conf else 0.0 for p in interiorB]); Gn = lu.solve(nv)
    S = sum(Gn[idxB[p]] + Gn[idxB[q]] for p, q in ibondsB if (p in conf) != (q in conf))
    return -(nv @ Gn) / (2 * S)
c0 = (8, 8, 8)
single = gstar_f({c0})
dilute = gstar_f({(4, 4, 4), (12, 12, 12), (4, 12, 8), (12, 4, 8)})
cube = lambda s: {(c0[0] + i, c0[1] + j, c0[2] + k) for i in range(s) for j in range(s) for k in range(s)}
compact = [gstar_f(cube(s)) for s in (2, 3, 4, 5)]
print(f"   single {single:.5f}; four far apart {dilute:.5f}; compact cubes s=2..5: " + ", ".join(f"{v:.4f}" for v in compact))
watson = 0.25273100985866300303
print(f"   infinite-lattice single-record value -G(0)/(2(12G(0)-1)) = {-watson/(2*(12*watson-1)):.5f}")
want(all(compact[i + 1] < compact[i] for i in range(3)) and abs(dilute - single) < 0.1 * abs(single),
     "E1 dilute bodies need about the single-record curvature; compact cubes need a curvature that grows in size with the body")

print("   [total %.0f s]" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED at weak field for the self-consistent member with record sources: (i) a clause with g'(1) != 0 "
      "(including the field's change of the crossing activity, which has block 171's activity (e, tau)) gives P - Q = 2 g'(1) B eps + O(eps^2); "
      "(ii) with g'(1) = 0, P - Q = eps^2 [-4 m g''(1) S - 2 m^2 n.Gn] + O(eps^3) exactly on any held-wall box, S = sum over movable bonds "
      "of (Gn)_x + (Gn)_y; so g'(1) != 0 misses at order eps (sign of g'(1)); with g'(1) = 0 every g''(1) >= 0 (rest only included) and a jammed box give P < Q; balance needs a concave clause "
      "tuned to g''(1) = -m n.Gn/(2S); (iii) in a stationary law the tuned value is -m<n.Gn>/(2<S>), which differs between N = 1, 2, 3 on the 5^3 box "
      "(exact) and grows with a compact body's size (floating point), so no clause fixed once balances two bodies")
print("HIT: self-consistent member with record sources at weak field: P - Q = 2 g'(1) B eps + eps^2[-4 m g''(1) S - 2 m^2 n.Gn] + O(eps^3) "
      "(eps = 1/8K, exact on held-wall boxes); a hop energy vanishing with the field (g'(1)=0) balances only for a concave clause with "
      "g''(1) = -m n.Gn/(2S) (law: -m<n.Gn>/(2<S>)), a value that differs between bodies (5^3 uniform law: N=1,2,3 distinct), so no clause fixed "
      "once balances; the field's change of the crossing activity is block 171's activity clause in (e, tau)")
