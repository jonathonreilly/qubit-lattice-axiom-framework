"""R19-3 check of treatment (A): the explicit Landau-Lifshitz formula (MTW eq. 20.22, RECALLED) against the identity
   (-g) t_LL^{ab} = (1/16pi) d_m d_n H^{ambn} - (-g) G^{ab}/(8 pi),   H^{ambn} = gg^{ab} gg^{mn} - gg^{an} gg^{bm},
   gg^{ab} = sqrt(-g) g^{ab}  (G = 1).
Pointwise in theta (not averaged), to O(s^2), for an off-shell wave vector and a random rational polarization.
If they agree, (i) the recalled formula is right and (ii) the vacuum value <(-g) t_LL> = -<[(-g)G]^(2)>/(8 pi) used in
r193_onepoint / r193_gauge_family is the Landau-Lifshitz pseudotensor (the d d H term has zero expectation in any
translation-invariant state)."""
import sympy as sp, random
random.seed(7)
s = sp.Symbol('s'); F = sp.symbols('F0:6')
eta = sp.diag(-1, 1, 1, 1); ei = eta.inv(); idx = range(4)
k = [sp.Rational(-13, 10), sp.Rational(2, 5), sp.Rational(-1, 5), sp.Rational(7, 10)]   # off shell
e = sp.zeros(4, 4)
for a in idx:
    for b in idx:
        if a <= b:
            e[a, b] = e[b, a] = sp.Rational(random.randint(-9, 9), random.randint(1, 5))
def D(expr, mu):
    out = 0
    for n in range(5):
        dn = sp.diff(expr, F[n])
        if dn != 0: out += dn*F[n+1]
    return sp.expand(k[mu]*out)
def trunc(x, o=2):
    x = sp.expand(x); return sum(x.coeff(s, n)*s**n for n in range(o+1))
h = e*F[0]; g = eta + s*h
gi = (ei - s*ei*h*ei + s**2*ei*h*ei*h*ei).applyfunc(trunc)
mdet = trunc(-(g.det())); a1 = mdet.coeff(s, 1); a2 = mdet.coeff(s, 2)
sq = 1 + s*a1/2 + s**2*(a2/2 - a1**2/8)
gg = (sq*gi).applyfunc(trunc)
dgg = [[[D(gg[a, b], m) for b in idx] for a in idx] for m in idx]      # dgg[m][a][b] = gg^{ab}_{,m}
# Einstein tensor
dg = [[[D(g[a, b], m) for b in idx] for a in idx] for m in idx]
Gam = [[[trunc(sum(sp.Rational(1, 2)*gi[a, d]*(dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in idx)) for c in idx] for b in idx] for a in idx]
Ric = sp.zeros(4, 4)
for b in idx:
    for c in idx:
        if c < b: continue
        t = sum(D(Gam[a][b][c], a) for a in idx) - sum(D(Gam[a][b][a], c) for a in idx)
        t += sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for a in idx for d in idx)
        Ric[b, c] = Ric[c, b] = trunc(t)
Rs = trunc(sum(gi[b, c]*Ric[b, c] for b in idx for c in idx))
G = (Ric - sp.Rational(1, 2)*g*Rs).applyfunc(trunc)
GDU = (mdet*(gi*G*gi)).applyfunc(trunc)
pi = sp.pi
def H(a, m, b, n): return trunc(gg[a, b]*gg[m, n] - gg[a, n]*gg[b, m])
ident = sp.zeros(4, 4); expl = sp.zeros(4, 4)
for al in idx:
    for be in idx:
        if be < al: continue
        ddH = sum(D(D(H(al, m, be, n), m), n) for m in idx for n in idx)
        ident[al, be] = sp.expand(trunc(ddH/(16*pi) - GDU[al, be]/(8*pi)).coeff(s, 2))
        # at O(s^2) every term is (O(s) gothic derivative)^2, so prefactors are needed only at O(1): g -> eta, g^-1 -> eta^-1
        g_, gi_ = eta, ei
        d1 = [[[sp.expand(dgg[m][a][b]).coeff(s, 1)*s for b in idx] for a in idx] for m in idx]
        X = 0
        X += sum(d1[l][al][be]*d1[m][l][m] for l in idx for m in idx)
        X -= sum(d1[l][al][l]*d1[m][be][m] for l in idx for m in idx)
        X += sp.Rational(1, 2)*sum(gi_[al, be]*g_[l, m]*d1[r][l][n]*d1[n][r][m] for l in idx for m in idx for n in idx for r in idx)
        X -= sum(gi_[al, l]*g_[m, n]*d1[r][be][n]*d1[l][m][r] + gi_[be, l]*g_[m, n]*d1[r][al][n]*d1[l][m][r]
                 for l in idx for m in idx for n in idx for r in idx)
        X += sum(g_[l, m]*gi_[n, r]*d1[n][al][l]*d1[r][be][m] for l in idx for m in idx for n in idx for r in idx)
        X += sp.Rational(1, 8)*sum((2*gi_[al, l]*gi_[be, m] - gi_[al, be]*gi_[l, m])*(2*g_[n, r]*g_[sg, t] - g_[r, sg]*g_[n, t])
                                   *d1[l][n][t]*d1[m][r][sg]
                                   for l in idx for m in idx for n in idx for r in idx for sg in idx for t in idx)
        expl[al, be] = sp.expand(trunc(X/(16*pi)).coeff(s, 2))
diff = (ident - expl).applyfunc(sp.simplify)
print('identity side O(s^2) contains F0*F2 terms:', any(sp.expand(ident[a, b]).has(F[0]) for a in idx for b in idx))
print('max |identity - explicit MTW(20.22)| over components (exact):', max(abs(diff[a, b]) for a in idx for b in idx if b >= a))
