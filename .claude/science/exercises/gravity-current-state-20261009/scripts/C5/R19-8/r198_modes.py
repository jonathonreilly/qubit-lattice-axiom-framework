#!/usr/bin/env python3
"""R19-8 [M]: per-mode O(G noise^2) mean source of E2 + N_c (friction law, harmonic gauge), all six R15-2 channel variables,
insertion family T^{ab} = (-g)^{a/4-1} J^{ab} (a = 2 is the weight-1 record sqrt(-g) T^{ab}).
E2 law (R12-7 E-H2, gothic form as in R18-7 sec. 3): (box - gam d_t) hgoth^{ab} = -16 pi tau_rec^{ab};
equivalently G_{mn}[g] = 8 pi T_eff with (-g) T_eff^{ab} = (-g)^{a/4} J^{ab} + Xt^{ab} (+ Lambda/Pi bookkeeping),
Xt^{ab} = -(gam/16 pi) d_t hgoth^{ab}  (the friction's linear stress = the sink's linear source).
Linear solution for one frame mode theta = k z - w t, J = J0 cos(theta):
   hbar = 16 pi J0 [ p cos(theta) + q sin(theta) ],  p = Re G_gam = (k^2-w^2)/Dn,  q = -Im G_gam = -gam w/Dn,
   Dn = (k^2-w^2)^2 + gam^2 w^2.   (p, q kept as free symbols; gam enters only through p, q and Xt.)
Mean source per mode: tau_{mn} = <T_eff^(2)_{mn}> - <G^(2)_{mn}[h1,h1]>/(8 pi), theta-averaged; the second-order part of Xt
from O(h1^2) gothic terms is a d_t of a stationary product and averages to zero (checked below on the explicit pieces).
Subtraction: none.  G = c = 1.  Run: OMP_NUM_THREADS=2 python3 r198_modes.py
"""
import sympy as sp, time, pickle
t0 = time.time()
w, k = sp.symbols('omega k', positive=True)
a, eps, gam = sp.symbols('a epsilon gamma')
p, q = sp.symbols('p q', real=True)
C, S = sp.symbols('C S')
X = w / k
eta = sp.diag(-1, 1, 1, 1)
def dth(f):
    f = sp.expand(f); return sp.diff(f, C) * (-S) + sp.diff(f, S) * C
def D(mu, f):
    if mu == 0: return -w * dth(f)
    if mu == 3: return k * dth(f)
    return sp.Integer(0)
MOM = {(0, 0): 1, (2, 0): sp.Rational(1, 2), (0, 2): sp.Rational(1, 2), (4, 0): sp.Rational(3, 8),
       (0, 4): sp.Rational(3, 8), (2, 2): sp.Rational(1, 8)}
def avg(e):
    P_ = sp.Poly(sp.expand(e), C, S); out = 0
    for (i, j), cf in P_.terms():
        if i % 2 == 0 and j % 2 == 0: out += cf * MOM[(i, j)]
        # odd powers average to zero
    return sp.expand(out)
def trunc(e, top=2):
    e = sp.expand(e); return sum(e.coeff(eps, pp) * eps**pp for pp in range(1, top + 1))
def einstein2(h):
    g = eta + eps * h
    ginv = eta - eps * eta * h * eta + eps**2 * eta * h * eta * h * eta
    n = 4
    dg = [[[D(l, g[m, qq]) for l in range(n)] for qq in range(n)] for m in range(n)]
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for al in range(n):
        for m in range(n):
            for qq in range(m, n):
                v = sum(ginv[al, b] * (dg[b][m][qq] + dg[b][qq][m] - dg[m][qq][b]) for b in range(n)) / 2
                v = trunc(v); Gam[al][m][qq] = v; Gam[al][qq][m] = v
    Ric = sp.zeros(n, n)
    for m in range(n):
        for qq in range(m, n):
            v = 0
            for al in range(n):
                v += D(al, Gam[al][m][qq]) - D(qq, Gam[al][m][al])
                for b in range(n):
                    v += Gam[al][al][b] * Gam[b][m][qq] - Gam[al][qq][b] * Gam[b][m][al]
            v = trunc(v); Ric[m, qq] = v; Ric[qq, m] = v
    R = trunc(sum(ginv[m, qq] * Ric[m, qq] for m in range(n) for qq in range(n)))
    Gt = sp.zeros(n, n)
    for m in range(n):
        for qq in range(n):
            Gt[m, qq] = trunc(Ric[m, qq] - g[m, qq] * R / 2)
    return Gt

rho, Tp, jx, jy, tp, tc = sp.symbols('rho T_perp j_x j_y t_p t_c', real=True)
J0 = sp.zeros(4, 4)
J0[0, 0] = rho; J0[0, 3] = J0[3, 0] = X * rho; J0[3, 3] = X**2 * rho
J0[0, 1] = J0[1, 0] = jx; J0[1, 3] = J0[3, 1] = X * jx
J0[0, 2] = J0[2, 0] = jy; J0[2, 3] = J0[3, 2] = X * jy
J0[1, 1] = Tp / 2 + tp; J0[2, 2] = Tp / 2 - tp; J0[1, 2] = J0[2, 1] = tc
J = J0 * C                                   # contravariant record mode
cons = [sp.simplify(D(0, J[0, nu]) + D(3, J[3, nu])) for nu in range(4)]
print("[M0] flat conservation of J (six channels):", cons)
Jl = eta * J * eta
J0l = eta * J0 * eta
hbar_l = 16 * sp.pi * J0l * (p * C + q * S)       # lower-index trace-reversed perturbation (harmonic gauge)
trb = sum(eta[i, i] * hbar_l[i, i] for i in range(4))
h = hbar_l - eta * trb / 2                         # metric perturbation h_mn, g = eta + eps h
# harmonic condition d^m hbar_mn = 0 (eta^{mm} D(m, .))
harm = [sp.simplify(sum(eta[m, m] * D(m, hbar_l[m, nu]) for m in range(4))) for nu in range(4)]
print("[M1] harmonic condition d^m hbar_mn on the friction solution:", harm)
# friction stress Xt_mn = -(gam/16 pi) d_t hbar_mn  (lower; contravariant = eta Xt eta at first order)
Xt_l = (-gam / (16 * sp.pi)) * hbar_l.applyfunc(lambda e: D(0, e))
Xt_u = eta * Xt_l * eta
consX = [sp.simplify(sum(D(m, Xt_u[m, nu]) for m in range(4))) for nu in range(4)]
print("[M2] flat conservation of the linear sink stress Xt (d_m Xt^{mn}):", consX)
G = einstein2(h)
# linear law: G1 = 8 pi (J + Xt) must hold once p, q are the friction response
lin = sp.zeros(4, 4)
Dn = (k**2 - w**2)**2 + gam**2 * w**2
sub_pq = {p: (k**2 - w**2) / Dn, q: -gam * w / Dn}
bad = 0
for m in range(4):
    for qq in range(m, 4):
        e = sp.simplify((G[m, qq].coeff(eps, 1) - 8 * sp.pi * (Jl[m, qq] + Xt_l[m, qq])).subs(sub_pq))
        if e != 0: bad += 1
print("[M3] E2 linear law G^(1)[h1] = 8 pi (J + Xt) with p = Re G_gam, q = -Im G_gam: components failing =", bad, "of 10")
# second-order mean source
trh = sp.expand(sum(eta[i, i] * h[i, i] for i in range(4)))   # (-g)^(1)
tau = sp.zeros(4, 4)
for m in range(4):
    for qq in range(4):
        T2 = (a / 4 - 1) * trh * Jl[m, qq]
        for al in range(4):
            for b in range(4):
                T2 += h[m, al] * eta[qq, b] * J[al, b] + eta[m, al] * h[qq, b] * J[al, b]
        # Xt second-order cross terms: (-g)^{-1} Xt^{ab} lowered with g
        X2 = (-1) * trh * Xt_l[m, qq]
        for al in range(4):
            for b in range(4):
                X2 += h[m, al] * eta[qq, b] * Xt_u[al, b] + eta[m, al] * h[qq, b] * Xt_u[al, b]
        tau[m, qq] = sp.expand(avg(T2) + avg(X2) - avg(G[m, qq].coeff(eps, 2)) / (8 * sp.pi))
        if m == qq or (m == 0):
            pass
xX = [sp.simplify(avg(sp.expand((-1) * trh * Xt_l[0, 0]))), sp.simplify(avg(sp.expand(h[1, 1] * Xt_u[1, 1])))]
print("[M4] sample Xt cross-term averages (expected 0 by phase):", xX)
t00 = sp.expand(tau[0, 0]); tkk = sp.expand(tau[1, 1] + tau[2, 2] + tau[3, 3])
print("[M5] mean momentum tau_0i:", [sp.simplify(tau[0, i]) for i in (1, 2, 3)])
xs = sp.Symbol('x', positive=True)
mons = [rho**2, rho*Tp, Tp**2, jx**2, jy**2, tp**2, tc**2, rho*jx, rho*tp, jx*jy, tp*tc, Tp*tp, jx*tp, jy*tc]
# structure in (p, q): decompose each coefficient into p^2, q^2, pq, p, q parts
print("\n[M6] structure of the per-mode coefficients in (p, q) [units pi/k^2, with p, q in units 1/k^2]:")
res = {}
for lab, ex in (("tau_00", t00), ("tau_kk", tkk)):
    Pl = sp.Poly(sp.expand(ex * k**2 / sp.pi), rho, Tp, jx, jy, tp, tc)
    for mon in mons:
        cf = sp.expand(sp.sympify(Pl.coeff_monomial(mon)))
        cf = sp.expand(cf.subs({p: p / k**2, q: q / k**2}).subs(w, xs * k))
        cf = sp.expand(cf.subs(gam, 0)) if False else cf
        Pq = sp.Poly(cf, p, q) if cf != 0 else None
        parts = {}
        if Pq is not None:
            for (i, j), c in Pq.terms():
                parts[(i, j)] = sp.factor(sp.simplify(c))
        res[(lab, mon)] = parts
        if parts:
            print("     %s [%s]: %s" % (lab, mon, {"p^%d q^%d" % kk: v for kk, v in parts.items()}))
# Test the hypothesis: q^2 coefficient == p^2 coefficient, no pq, no linear q, so tau = c_hh |G|^2 + c_hJ Re G
ok = True
for kk, parts in res.items():
    c20 = parts.get((2, 0), 0); c02 = parts.get((0, 2), 0); c11 = parts.get((1, 1), 0); c01 = parts.get((0, 1), 0)
    if sp.simplify(c20 - c02) != 0 or sp.simplify(c11) != 0 or sp.simplify(c01) != 0:
        ok = False; print("     hypothesis fails at", kk, parts)
# gam appears explicitly only via Xt cross terms; check gam-dependence of coefficients
gdep = any(sp.sympify(v).has(gam) for parts in res.values() for v in parts.values())
print("[M7] per-mode mean depends on (p, q) only through p^2 + q^2 = |G_gam|^2 and p = Re G_gam (no pq, no q-linear term):", ok)
print("     explicit gam-dependence of the coefficients (beyond p, q):", gdep)
# E1 limit (q = 0, p = 1/(1 - x^2)) must equal R19-2's Poisson table at a = 2 (Theorem G) and R18-11 harmonic for all a
r192 = {("tau_00", rho**2): 2*a*xs**2 + 2*a - 3*xs**2 - 7, ("tau_00", rho*Tp): -a, ("tau_00", Tp**2): 0,
        ("tau_00", jx**2): 4, ("tau_00", tp**2): 4*(xs**2 + 1)/((xs - 1)**2*(xs + 1)**2),
        ("tau_kk", rho**2): (xs**2 + 1)*(2*a*xs**2 - 4*xs**2 - 1), ("tau_kk", rho*Tp): a*xs**2 + 2*a - 2*xs**2 - 2,
        ("tau_kk", Tp**2): -(a - 2), ("tau_kk", jx**2): -4, ("tau_kk", tp**2): -4*(xs**2 - 3)/((xs - 1)**2*(xs + 1)**2)}
def coef_at(kk, pv, qv):
    parts = res[kk]; return sp.simplify(sum(c * pv**i * qv**j for (i, j), c in parts.items()))
pE1 = 1 / (1 - xs**2)
agreeA2 = [sp.simplify((coef_at(kk, pE1, 0) - v).subs(a, 2)) == 0 for kk, v in r192.items()]
print("\n[M8] gam -> 0 (E1 in harmonic gauge) vs R19-2 Poisson table at a = 2: %d of %d entries agree (Theorem G check)" % (sum(agreeA2), len(agreeA2)))
diffs = {kk: sp.factor(sp.simplify(coef_at(kk, pE1, 0) - v)) for kk, v in r192.items()}
print("     harmonic minus Poisson, general a:", {str(kk): v for kk, v in diffs.items() if v != 0})
print("     runtime %.1f s" % (time.time() - t0))
pickle.dump({str(kk): {str(i): str(c) for i, c in parts.items()} for kk, parts in res.items()}, open('r198_coef.pkl', 'wb'))
