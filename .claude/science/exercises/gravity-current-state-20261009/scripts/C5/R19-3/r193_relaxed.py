"""R19-3 addendum: literal N's own source.  R16-14 (rR16-14:68,143) and R18-7 source the metric through the harmonic-gauge
relaxed equations, box hbar^{ab} = -16 pi G tau^{ab},  tau = (-g)(T + t_LL) + t_H,
   (-g) t_H^{ab} = (1/16 pi G) [ d_m hh^{an} d_n hh^{bm} - hh^{mn} d_m d_n hh^{ab} ],   hh^{ab} = eta^{ab} - sqrt(-g) g^{ab}
(Poisson-Will form, RECALLED; the identity d_m d_n H = -box hh - 16 pi G t_H holds when d_n hh^{mn} = 0).
Per-mode vacuum value of t_H and of tau_vac = <(-g)t_LL> + <t_H> in the harmonic family (beta = 1/2), for several xi and
xi -> 0 (exact harmonic).  Machinery and normalization as r193_gauge_family.py (exec of its first part)."""
src = open(__file__.rsplit('/', 1)[0] + '/r193_gauge_family.py').read().split('# ---- sanity')[0]
exec(src)
gg = (sqrtg*gi).applyfunc(trunc)
hh = (ei - gg).applyfunc(trunc)                 # O(s) + O(s^2); only O(s) matters in the quadratic t_H
hh1 = hh.applyfunc(lambda z: sp.expand(z).coeff(s, 1)*s)
TH = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        if b < a: continue
        expr = sum(D(hh1[a, n], m)*D(hh1[b, m], n) for m in idx for n in idx) \
             - sum(hh1[m, n]*D(D(hh1[a, b], m), n) for m in idx for n in idx)
        TH[a, b] = TH[b, a] = sp.expand(expr)
QH = (eta*TH*eta).applyfunc(avg2)               # lowered; physical t_H = QH/(16 pi G)
print(f'expansion done {time.time()-T0:.1f}s')
xi, beta = sp.symbols("xi beta", positive=True)
emat = sp.Matrix(4, 4, lambda a, b: esym(a, b))
tre = sum(ei[a, a]*emat[a, a] for a in idx)
Fv = [sum(kup[m]*emat[m, n] for m in idx) - beta*k[n]*tre for n in idx]
def hess(q): return sp.Matrix(len(evars), len(evars), lambda i, j: 2*sp.diff(q, evars[i], evars[j]))
KEH = hess(QL)
LGF = sp.expand(-(1/(2*xi))*sp.Rational(1, 2)*sum(ei[n, n]*Fv[n]**2 for n in idx))
KGF = hess(LGF)
def PF(a, b, c, d): return sp.Rational(1, 2)*(eta[a, c]*eta[b, d] + eta[a, d]*eta[b, c] - eta[a, b]*eta[c, d])
PFmat = sp.Matrix(10, 10, lambda i, j: PF(*keys[i], *keys[j]))
K1 = (KEH + KGF).subs({xi: 1, beta: sp.Rational(1, 2)})
cnorm = 1/sp.simplify(K1.inv()*(k0**2 - kz**2)*PFmat.inv())[0, 0]
def wick_cov(q, Cov):
    q = sp.expand(q); p = sp.Poly(q, *evars); out = 0
    for mon, co in p.terms():
        pos = [i for i, m in enumerate(mon) for _ in range(m)]
        out += co*Cov[pos[0], pos[1]]
    return out
Kx = (KEH + KGF).subs({beta: sp.Rational(1, 2)})
Cov = (cnorm*Kx.inv()).applyfunc(lambda z: sp.cancel(z))
for name, Q, fac in (('t_H', QH, 4), ('(-g)t_LL  [treatment (A)]', QA, -8)):
    expr = sp.cancel(sp.together(wick_cov(Q[0, 0], Cov).subs(kz, 1)))
    c = sp.simplify(fac*sp.residue(expr, k0, 1))
    full = []
    for a, b in ((0, 3), (3, 3), (1, 1)):
        e2 = sp.cancel(sp.together(wick_cov(Q[a, b], Cov).subs(kz, 1)))
        full.append(sp.simplify(fac*sp.residue(e2, k0, 1)))
    print(f'harmonic family: {name:26s} t_00(xi) = {c};  t_03, t_33, t_11 = {full};  xi -> 0: {sp.limit(c, xi, 0)}')
print(f'time {time.time()-T0:.1f}s')
