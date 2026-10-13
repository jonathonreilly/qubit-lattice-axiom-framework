"""R19-3: gauge-parameter dependence of the one-point vacuum stress, and the harmonic-gauge BRST/background-field total.

Same plane-wave machinery as r193_onepoint.py, but with an OFF-SHELL symbolic wave vector k_mu = (-k0, 0, 0, kz),
so that covariant gauges with double poles (xi != 1) can be evaluated.

Objects (all to O(s^2), phase-averaged over theta = k.x with f = cos: <F1^2> = 1/2, <F0 F2> = -1/2):
  B : G2_{mu nu} (lower)                         t_B  = -(1/8piG) <G2>          (Isaacson-type, treatment (B))
  A : [(-g) G^{ab}]^(2), lowered with eta        t_A  = -(1/8piG) <...>         (= <(-g) t_LL> exactly, treatment (A))
  A': [sqrt(-g) G^{ab}]^(2), lowered with eta    t_A' = -(1/8piG) <...>         (EH part of the background-field stress)
  L : [sqrt(-g) R]^(2)   -> kinetic matrix K_EH(k);   gauge fixing  L_GF = -(1/(2 xi)) F_nu F^nu,
      F_nu = d^mu h_{mu nu} - beta d_nu h   (beta = 1/2: harmonic / de Donder).  Units: L' = 16 pi G L.
Covariance of the polarization coordinates e_ab (a <= b) in gauge (xi, beta):  Cov = c K^{-1}, with c fixed by
  xi = 1, beta = 1/2:  c K^{-1} = P_FdD/(k0^2 - kz^2)   (checked below, entry by entry).
Per spatial mode, symmetric Wightman expectation = Res_{k0 = +w}[ Q(k0) Cov(k0) ]  (w = |kz| = 1; double poles = the
  m^2-derivative of the massive Wightman function).  Per-mode stress in units of w/V:  t = -8 Res[...] for G-type Q
  (equals -4 E_PFdD[Q(w)]/w at xi = 1).  TT calibration: t_00 = 1 = two polarizations x w/2.
Also: the gauge-fixing (Hilbert) stress at xi = 1 on a constant background gbar = eta + delta, to test
  BFM total = t_A' + t_GF + t_ghost  against the TT value, with t_ghost = -8 real scalars (4 complex Grassmann
  vector components with the box operator; FP determinant counting, comparator).
"""
import sympy as sp, time, itertools
T0 = time.time()
s = sp.Symbol('s'); k0, kz = sp.symbols('k0 kz', real=True)
F = sp.symbols('F0:6')
eta = sp.diag(-1, 1, 1, 1); ei = eta.inv()
idx = range(4)
E = {}
for a in idx:
    for b in idx:
        if a <= b:
            E[(a, b)] = sp.Symbol(f'e{a}{b}')
keys = list(E.keys()); evars = list(E.values())
def esym(a, b): return E[(min(a, b), max(a, b))]
k = [-k0, 0, 0, kz]          # lower-index wave vector; k^mu = (k0, 0, 0, kz)
kup = [k0, 0, 0, kz]

def D(expr, mu):
    out = 0
    for n in range(5):
        dn = sp.diff(expr, F[n])
        if dn != 0:
            out += dn*F[n+1]
    return sp.expand(k[mu]*out)
def trunc(expr, order=2):
    expr = sp.expand(expr)
    return sum(expr.coeff(s, n)*s**n for n in range(order+1))

h = sp.Matrix(4, 4, lambda a, b: esym(a, b)*F[0])
g = eta + s*h
gi = (ei - s*ei*h*ei + s**2*ei*h*ei*h*ei).applyfunc(trunc)
dg = [[[D(g[a, b], m) for b in idx] for a in idx] for m in idx]
Gam = [[[trunc(sum(sp.Rational(1, 2)*gi[a, d]*(dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in idx))
         for c in idx] for b in idx] for a in idx]
Ric = sp.zeros(4, 4)
for b in idx:
    for c in idx:
        if c < b: continue
        term = sum(D(Gam[a][b][c], a) for a in idx) - sum(D(Gam[a][b][a], c) for a in idx)
        term += sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for a in idx for d in idx)
        Ric[b, c] = trunc(term); Ric[c, b] = Ric[b, c]
Rs = trunc(sum(gi[b, c]*Ric[b, c] for b in idx for c in idx))
G = (Ric - sp.Rational(1, 2)*g*Rs).applyfunc(trunc)
mdet = trunc(-(g.det()))
a1 = sp.expand(mdet).coeff(s, 1); a2 = sp.expand(mdet).coeff(s, 2)
sqrtg = 1 + s*a1/2 + s**2*(a2/2 - a1**2/8)
GU = (gi*G*gi).applyfunc(trunc)
GA = (eta*(mdet*GU).applyfunc(trunc)*eta)          # (-g) G^{ab}, lowered
GAp = (eta*(sqrtg*GU).applyfunc(trunc)*eta)        # sqrt(-g) G^{ab}, lowered
Lag = trunc(sqrtg*Rs)
print(f'symbolic O(s^2) expansion done: {time.time()-T0:.1f}s')

def avg2(expr):
    p = sp.Poly(sp.expand(sp.expand(expr).coeff(s, 2)), F[0], F[1], F[2], F[3])
    out = 0
    for mon, co in p.terms():
        if mon == (0, 2, 0, 0): out += co/2
        elif mon == (1, 0, 1, 0): out += -co/2
        else: raise ValueError(mon)
    return sp.expand(out)

QB = G.applyfunc(avg2); QA = GA.applyfunc(avg2); QAp = GAp.applyfunc(avg2); QL = avg2(Lag)
print(f'phase averages done: {time.time()-T0:.1f}s')

# ---- sanity: pure gauge e = k v + v k (on shell) gives zero, and pure gauge x TT bilinear gives zero
def sub_e(q, emat):
    return sp.expand(q.subs({E[kk]: emat[kk[0], kk[1]] for kk in keys}))
v = sp.symbols('v0:4')
egauge = sp.Matrix(4, 4, lambda a, b: k[a]*v[b] + k[b]*v[a])
eTT = sp.zeros(4, 4); eTT[1, 1] = 1; eTT[2, 2] = -1; eTT[1, 2] = eTT[2, 1] = sp.Symbol('x')
on = {k0: 1, kz: 1}
for name, Q in (('B', QB), ('A', QA), ("A'", QAp)):
    pg = max(abs(sp.simplify(sub_e(Q[a, b], egauge).subs(on))) != 0 for a in idx for b in idx)
    mix = sp.Matrix(4, 4, lambda a, b: sp.expand(sub_e(Q[a, b], egauge + eTT) - sub_e(Q[a, b], egauge) - sub_e(Q[a, b], eTT)).subs(on))
    print(f'sanity {name:2s}: Q(pure gauge) == 0 on shell: {not pg};  2Q(pure gauge, TT) == 0 on shell: {mix == sp.zeros(4,4)}')

# ---- kinetic matrices
def hess(q):
    return sp.Matrix(len(evars), len(evars), lambda i, j: 2*sp.diff(q, evars[i], evars[j]))   # <L> = (1/4) e^T K e
KEH = hess(QL)
xi, beta = sp.symbols('xi beta', positive=True)
# gauge fixing on the plane wave: d_a h = -k_a e sin(theta);  F_nu = -sin * (k^mu e_{mu nu} - beta k_nu tr_eta(e))
emat = sp.Matrix(4, 4, lambda a, b: esym(a, b))
tre = sum(ei[a, a]*emat[a, a] for a in idx)
Fv = [sum(kup[m]*emat[m, n] for m in idx) - beta*k[n]*tre for n in idx]
LGF = sp.expand(-(1/(2*xi))*sp.Rational(1, 2)*sum(ei[n, n]*Fv[n]**2 for n in idx))    # <sin^2> = 1/2
KGF = hess(LGF)
def PF(a, b, c, d): return sp.Rational(1, 2)*(eta[a, c]*eta[b, d] + eta[a, d]*eta[b, c] - eta[a, b]*eta[c, d])
PFmat = sp.Matrix(10, 10, lambda i, j: PF(*keys[i], *keys[j]))
K1 = (KEH + KGF).subs({xi: 1, beta: sp.Rational(1, 2)})
M1 = sp.simplify(K1.inv())
ratio = sp.simplify(M1*(k0**2 - kz**2)*PFmat.inv())
print('xi=1, beta=1/2:  K^{-1} (k0^2-kz^2) P_FdD^{-1} =', ratio if ratio.is_diagonal() and len(set(ratio.diagonal())) == 1 else 'NOT proportional',
      '(scalar => Cov = c K^{-1} with c = 1/ratio)')
cnorm = 1/ratio[0, 0]

def wick_cov(q, Cov):
    q = sp.expand(q); p = sp.Poly(q, *evars); out = 0
    for mon, co in p.terms():
        pos = [i for i, m in enumerate(mon) for _ in range(m)]
        out += co*Cov[pos[0], pos[1]]
    return out

def per_mode(Q, Cov, factor):
    out = sp.zeros(4, 4)
    for a in idx:
        for b in idx:
            if b < a: out[a, b] = out[b, a]; continue
            expr = sp.cancel(sp.together(wick_cov(Q[a, b], Cov).subs(kz, 1)))
            out[a, b] = sp.nsimplify(sp.simplify(factor*sp.residue(expr, k0, 1)))
    return out

kk_on = sp.Matrix(4, 4, lambda a, b: [-1, 0, 0, 1][a]*[-1, 0, 0, 1][b])
print('\nper-mode one-point stress t_mn (units w/V), k || z, w = 1; TT value is 1 x k_m k_n:')
results = {}
for xv in (1, 2, sp.Rational(1, 2), sp.Rational(1, 10)):
    Kx = (KEH + KGF).subs({xi: xv, beta: sp.Rational(1, 2)})
    Cov = cnorm*Kx.inv()
    Cov = Cov.applyfunc(lambda z: sp.cancel(z))
    row = []
    for name, Q in (('B', QB), ('A', QA), ("A'", QAp)):
        t = per_mode(Q, Cov, -8)
        c = t[0, 0]
        resid = (t - c*kk_on).applyfunc(sp.simplify)
        row.append((name, c, resid == sp.zeros(4, 4)))
        results[(xv, name)] = c
    print(f'  harmonic family xi = {str(xv):5s}: ' + ';  '.join(f'({n}) t = {c} x kk [pure kk: {ok}]' for n, c, ok in row)
          + f'   [{time.time()-T0:.0f}s]')
# xi-dependence in closed form for (B), (A), (A')
Kx = (KEH + KGF).subs({beta: sp.Rational(1, 2)})
Cov = (cnorm*Kx.inv()).applyfunc(lambda z: sp.cancel(z))
for name, Q in (('B', QB), ('A', QA), ("A'", QAp)):
    expr = sp.cancel(sp.together(wick_cov(Q[0, 0], Cov).subs(kz, 1)))
    c = sp.simplify(-8*sp.residue(expr, k0, 1))
    print(f'  closed form, harmonic family: ({name}) t_00(xi) = {c};  xi -> 0 (exact harmonic): {sp.limit(c, xi, 0)}')
print(f'[{time.time()-T0:.0f}s]')

# ---- gauge-fixing Hilbert stress at xi = 1, beta = 1/2 on a constant background gbar = eta + d
dl = {}
for a in idx:
    for b in idx:
        if a <= b: dl[(a, b)] = sp.Symbol(f'd{a}{b}')
dm = sp.Matrix(4, 4, lambda a, b: dl[(min(a, b), max(a, b))])
gb = eta + dm
gbi = (ei - ei*dm*ei)                      # first order in d suffices
sq = 1 + sp.Rational(1, 2)*sum(ei[a, a]*dm[a, a] for a in idx)
trg = sum(gbi[a, b]*emat[a, b] for a in idx for b in idx)
Fb = [sum(gbi[m, al]*kup_l*emat[m, n] for m in idx for al, kup_l in enumerate(k)) - sp.Rational(1, 2)*k[n]*trg for n in idx]
# note: d_alpha h = -k_alpha e sin ; gbar^{m al} d_al h_{m n} -> -sin * gbar^{m al} k_al e_{mn}
LGFb = sp.expand(-sp.Rational(1, 2)*sq*sp.Rational(1, 2)*sum(gbi[n, l]*Fb[n]*Fb[l] for n in idx for l in idx))
TGF = sp.zeros(4, 4)
for (a, b), sym in dl.items():
    dLd = sp.expand(sp.diff(LGFb, sym).subs({x: 0 for x in dl.values()}))
    val = 2*dLd if a == b else dLd           # T^{ab} = 2 dL/dgbar_ab (symmetric)
    TGF[a, b] = TGF[b, a] = val
TGFl = eta*TGF*eta
Cov1 = (cnorm*K1.inv()).applyfunc(lambda z: sp.cancel(z))
tGF = per_mode(TGFl, Cov1, 2*2)   # t = 2*E[T'] with T' in 16piG units; residue factor 2w => x2 more
tAp = per_mode(QAp, Cov1, -8)
print('\nBRST/background-field total at xi = 1 (harmonic, Feynman):')
print(f"  t_A' (EH part) = {tAp[0,0]} x kk;  t_GF = {tGF[0,0]} x kk  [pure kk: {(tGF - tGF[0,0]*kk_on).applyfunc(sp.simplify) == sp.zeros(4,4)}]")
print(f"  EH + GF = {tAp[0,0] + tGF[0,0]} x kk   (10 real bosonic components with the box operator would give 10 x 1/2 = 5)")
print(f"  ghosts (4 complex Grassmann components, box operator; FP counting): -8 x 1/2 = -4 x kk")
print(f"  BFM total = {tAp[0,0] + tGF[0,0] - 4} x kk   (TT value: 1)")
print(f'total time {time.time()-T0:.1f}s')
