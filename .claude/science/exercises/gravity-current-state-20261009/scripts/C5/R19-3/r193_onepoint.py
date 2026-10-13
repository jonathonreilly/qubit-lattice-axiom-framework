"""R19-3 (a)-(c): one-loop one-point gravitational vacuum stress, per mode, in three treatments.

Method (exact symbolic, sympy):
  g = eta + s*h,  h_{mu nu}(x) = e_{mu nu} f(theta),  theta = k_mu x^mu  (one Fourier mode, real polarization e).
  Derivatives act by the chain rule d_mu F_n = k_mu F_{n+1}  (F_n = f^(n)(theta)).
  We expand to O(s^2):
     G2_{mu nu}    = second-order Einstein tensor (lower indices)                 -> treatment (B), Isaacson-type
     GD2^{ab}      = second-order part of (-g) G^{ab}  (upper-index density)       -> treatment (A): by the Landau-Lifshitz
                     identity (-g) t_LL^{ab} = (1/16 pi G) d_m d_n H^{ambn} - (-g) G^{ab}/(8 pi G), and <d d H> = 0 in any
                     translation-invariant state, so <(-g) t_LL^{ab}> = -<GD2^{ab}>/(8 pi G) exactly at this order.
     G1_{mu nu}    = linear Einstein tensor (to classify modes).
  Phase average over theta (f = cos): <F1^2> = 1/2, <F0 F2> = -1/2.  (v0 of this script set <F1^2> = 1, a factor-2
  normalization slip; its output is kept as r193_onepoint_v0_unhalved.out and every number there is 2x.)
  Vacuum expectation: Wick replacement e_ab e_cd -> Cov(ab, cd) (the polarization factor of the Wightman function):
     TT (reduced phase space; also Coulomb/Poisson gauge, whose linear vacuum fluctuations are TT only):
         k along z: Cov(xx,xx)=Cov(yy,yy)=Cov(xy,xy)=1/2, Cov(xx,yy)=-1/2.
     FdD (harmonic de Donder gauge, Feynman weighting, gauge-fixed Gupta-Bleuler vacuum):
         Cov(ab,cd) = (eta_ac eta_bd + eta_ad eta_bc - eta_ab eta_cd)/2.
  Normalization: <h_ab h_cd> = 32 pi G Cov/(2 w V) per mode; a classical phase average carries <cos^2>=1/2, so the quantum
  per-mode value of a quadratic form Q is 2*(32 pi G/(2 w V))*E_Cov[Q_avg].  Then t = -Q/(8 pi G) gives
     t_{mu nu}(per mode, units of w/V) = -4 E_Cov[ G2_avg ] / w^2      (w = 1 here, k null).
  Calibration: TT must give t_00 = 1 (two polarizations x w/2).
"""
import sympy as sp, itertools, time
T0 = time.time()
s = sp.Symbol('s')
F = sp.symbols('F0:6')
eta = sp.diag(-1, 1, 1, 1)
idx = range(4)
E = {}
for a in idx:
    for b in idx:
        if a <= b:
            E[(a, b)] = sp.Symbol(f'e{a}{b}')
def esym(a, b):
    return E[(min(a, b), max(a, b))]
evars = list(E.values())

def D(expr, mu, k):
    """chain-rule derivative d_mu of an expression in F0..F4"""
    out = 0
    for n in range(5):
        dn = sp.diff(expr, F[n])
        if dn != 0:
            out += dn*F[n+1]
    return sp.expand(k[mu]*out)

def trunc(expr, order=2):
    expr = sp.expand(expr)
    return sum(expr.coeff(s, n)*s**n for n in range(order+1))

def compute(k):
    h = sp.Matrix(4, 4, lambda a, b: esym(a, b)*F[0])
    g = eta + s*h
    ei = eta.inv()
    gi = ei - s*ei*h*ei + s**2*ei*h*ei*h*ei
    gi = gi.applyfunc(trunc)
    dg = [[[D(g[a, b], m, k) for b in idx] for a in idx] for m in idx]   # dg[m][a][b] = d_m g_ab
    Gam = [[[trunc(sum(sp.Rational(1, 2)*gi[a, d]*(dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in idx))
             for c in idx] for b in idx] for a in idx]
    Ric = sp.zeros(4, 4)
    for b in idx:
        for c in idx:
            if c < b:
                continue
            term = sum(D(Gam[a][b][c], a, k) for a in idx) - sum(D(Gam[a][b][a], c, k) for a in idx)
            term += sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for a in idx for d in idx)
            Ric[b, c] = trunc(term); Ric[c, b] = Ric[b, c]
    Rs = trunc(sum(gi[b, c]*Ric[b, c] for b in idx for c in idx))
    G = (Ric - sp.Rational(1, 2)*g*Rs).applyfunc(trunc)
    detg = trunc(-(g.det()))   # -g
    GU = (gi*G*gi).applyfunc(trunc)
    GD = (detg*GU).applyfunc(trunc)
    return G, GD

def avg2(expr):
    """s^2 coefficient, phase-averaged: <F0 F2> = -<F1^2> = -1, <F1^2> = 1"""
    p = sp.Poly(sp.expand(sp.expand(expr).coeff(s, 2)), F[0], F[1], F[2], F[3])
    out = 0
    for mon, co in p.terms():
        if mon == (0, 2, 0, 0):
            out += co/2
        elif mon == (1, 0, 1, 0):
            out += -co/2
        elif mon == (0, 0, 0, 0):
            out += 0
        else:
            raise ValueError(f'unexpected monomial {mon}')
    return sp.expand(out)

def lin1(expr):
    return sp.expand(sp.expand(expr).coeff(s, 1))

def cov_FdD(a, b, c, d):
    return sp.Rational(1, 2)*(eta[a, c]*eta[b, d] + eta[a, d]*eta[b, c] - eta[a, b]*eta[c, d])

def cov_TT_z(a, b, c, d):
    pair = lambda x, y: (min(x, y), max(x, y))
    P1, P2 = pair(a, b), pair(c, d)
    tbl = {((1, 1), (1, 1)): sp.Rational(1, 2), ((2, 2), (2, 2)): sp.Rational(1, 2), ((1, 1), (2, 2)): -sp.Rational(1, 2),
           ((2, 2), (1, 1)): -sp.Rational(1, 2), ((1, 2), (1, 2)): sp.Rational(1, 2)}
    return tbl.get((P1, P2), 0)

def cov_TT_x(a, b, c, d):
    # TT for k along x: polarizations in (y,z) = indices (2,3)
    pair = lambda x, y: (min(x, y), max(x, y))
    P1, P2 = pair(a, b), pair(c, d)
    tbl = {((2, 2), (2, 2)): sp.Rational(1, 2), ((3, 3), (3, 3)): sp.Rational(1, 2), ((2, 2), (3, 3)): -sp.Rational(1, 2),
           ((3, 3), (2, 2)): -sp.Rational(1, 2), ((2, 3), (2, 3)): sp.Rational(1, 2)}
    return tbl.get((P1, P2), 0)

def wick(q, cov):
    """E[q] for q quadratic in the e's with covariance cov(ab,cd) (polarization Wick contraction)"""
    q = sp.expand(q)
    p = sp.Poly(q, *evars)
    out = 0
    keys = list(E.keys())
    for mon, co in p.terms():
        pos = [i for i, m in enumerate(mon) for _ in range(m)]
        assert len(pos) == 2, mon
        (a, b), (c, d) = keys[pos[0]], keys[pos[1]]
        out += co*cov(a, b, c, d)
    return sp.nsimplify(sp.expand(out))

if __name__ == '__main__':
    for kname, k, covTT in (('k || z', [-1, 0, 0, 1], cov_TT_z), ('k || x', [-1, 1, 0, 0], cov_TT_x)):
        G, GD = compute(k)
        print(f'=== mode {kname}: k_mu = {k} (null, w = 1); symbolic O(s^2) done at {time.time()-T0:.1f}s ===')
        kk = sp.Matrix(4, 4, lambda a, b: k[a]*k[b])
        # (B): lower-index G2;  (A): density GD2 with indices lowered by eta
        B_avg = G.applyfunc(avg2)
        A_avg = (eta*GD*eta).applyfunc(avg2)
        for tname, cov in (('TT (reduced; Coulomb/Poisson)', covTT), ('FdD (harmonic, Feynman)', cov_FdD)):
            tB = B_avg.applyfunc(lambda q: -4*wick(q, cov))
            tA = A_avg.applyfunc(lambda q: -4*wick(q, cov))
            print(f'  [{tname}]')
            print(f'    (B) t_mn per mode / (w/V) = {tB.tolist()}')
            print(f'        (B) - c k_m k_n with c = t_00: residual = {(tB - tB[0,0]*kk).applyfunc(sp.simplify).tolist()}')
            print(f'    (A) t_mn per mode / (w/V) = {tA.tolist()}')
            print(f'        (A) - c k_m k_n with c = t_00: residual = {(tA - tA[0,0]*kk).applyfunc(sp.simplify).tolist()}')
        # classify: linear Einstein tensor of each basis polarization (on-shell modes: G1 = 0 iff physical or pure gauge)
        if kname == 'k || z':
            G1 = G.applyfunc(lin1)
            print('  linear G1_00 per polarization component (coefficient of F2):')
            for key, sym in E.items():
                g1 = G1.applyfunc(lambda q: sp.expand(q).coeff(sym))
                nz = any(sp.simplify(x) != 0 for x in g1)
                print(f'    e{key}: G1 != 0 ? {nz}')
    print(f'total time {time.time()-T0:.1f}s')
