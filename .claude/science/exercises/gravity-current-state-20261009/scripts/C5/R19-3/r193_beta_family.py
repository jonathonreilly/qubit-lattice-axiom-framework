"""R19-3 (second family): beta-xi scan of the one-point stress (gauge CONDITION varied, not only the weight).
Built from r193_gauge_family.py (identical machinery up to the kinetic matrices).
R19-3: gauge-parameter dependence of the one-point vacuum stress, and the harmonic-gauge BRST/background-field total.

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
print('\nper-mode t_00 (units w/V, k || z, w = 1) for F_nu = d^mu h_mu nu - beta d_nu h, weight 1/(2 xi); TT value 1:')
for bv in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(3, 4), 2):
    for xv in (1, 3):
        Kx = (KEH + KGF).subs({xi: xv, beta: bv})
        if Kx.det() == 0:
            print(f'  beta = {bv}, xi = {xv}: singular'); continue
        Cov = (cnorm*Kx.inv()).applyfunc(lambda z: sp.cancel(z))
        out = []
        for name, Q in (('B', QB), ('A', QA), ("A'", QAp)):
            t = per_mode(Q, Cov, -8)
            c = t[0, 0]
            ok = (t - c*kk_on).applyfunc(sp.simplify) == sp.zeros(4, 4)
            out.append(f'({name}) {c} [kk: {ok}]')
        print(f'  beta = {str(bv):4s} xi = {xv}: ' + ';  '.join(out) + f'   [{time.time()-T0:.0f}s]')
print(f'total time {time.time()-T0:.1f}s')
