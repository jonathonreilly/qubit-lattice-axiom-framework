#!/usr/bin/env python3
"""R19-8 [K]: E2's sink inside the conserving completion Pi.
 [K1] R18-7's Pi: i p_b K^{ab} = -D^a for any S; at k = 0 (homogeneous) K^{00} = -S^{00}, K^{0i} = -S^{0i}, K^{ij} = 0 (pressureless).
 [K2] the frame dipole Phi1 = (G M gam / 2)(w.xhat) (R12-7 out, R14-2 sec 3.2) is the Newtonian field of the sink's linear stress
      Xt^{00} = -(gam/16 pi G) d_t hbar^{00} of a body moving at w.
 [K3] per mode: field-to-sink energy rate <Q^0[h1; Xt1]> and the noise's work <Q^0[h1; J]>, Q^a[h;X] = Gam^a_{bm}[h] X^{bm} - X^{ab} d_b ln sqrt(-g);
      stationary balance <Q^0[h1; J + Xt1]> = 0 (LL identity d_b Lambda^{ab} = Q^a[h1; G1/8pi] and stationarity).
 [K4] FRW/budget numbers: E2's stationary near-cone TT content vs E1's at t_H (R14-2 T_eq = e^{-gamma_E}/gamma); the R12-7 split sink (gam/3H) rho_GW;
      the size of friction acting on the homogeneous (background) mode if the law were lifted that way (suggested).
Subtraction: none.  G = c = 1 in [K1]-[K3].  Run: OMP_NUM_THREADS=2 python3 r198_sink.py
"""
import sympy as sp, numpy as np, time
t0 = time.time()
# ---------------- [K1] ----------------
w, k1, k2, k3 = sp.symbols('omega k1 k2 k3', real=True)
eta = sp.diag(-1, 1, 1, 1)
pu = sp.Matrix([w, k1, k2, k3])                 # p^a (contravariant), p_a = eta p
pl = eta * pu
p2 = (pu.T * eta * pu)[0]
Ssym = sp.Matrix(4, 4, lambda i, j: sp.Symbol('S%d%d' % (min(i, j), max(i, j))))
Dv = sp.I * Ssym * pl                           # D^a = i p_b S^{ab}
pD = (pl.T * Dv)[0]
K = sp.I * (pu * Dv.T + Dv * pu.T) / p2 - sp.I * pu * pu.T * pD / p2**2
chk = sp.simplify(sp.I * K * pl + Dv)
print("[K1] i p_b K^{ab} + D^a (general S, k):", list(chk))
K0 = sp.simplify(K.subs({k1: 0, k2: 0, k3: 0}))
print("     k = 0: K^{00} = %s ; K^{0i} = %s ; K^{ij} = %s" % (K0[0, 0], [K0[0, i] for i in (1, 2, 3)], [K0[i, j] for i in (1, 2, 3) for j in (i, 3)]))
# ---------------- [K2] ----------------
xx, yy, zz, M, gam, wx = sp.symbols('x y z M gamma w_x', real=True)
r = sp.sqrt(xx**2 + yy**2 + zz**2)
U = M / r                                        # G = 1
# body moving at w along x: hbar^{00} = 4 U(x - w t) -> d_t hbar^{00} = -4 w dU/dx
Xt00 = -(gam / (16 * sp.pi)) * (-4 * wx * sp.diff(U, xx))
Phi1 = (M * gam / 2) * (wx * xx / r)
lap = sp.simplify(sp.diff(Phi1, xx, 2) + sp.diff(Phi1, yy, 2) + sp.diff(Phi1, zz, 2) - 4 * sp.pi * Xt00)
print("\n[K2] nabla^2 Phi1 - 4 pi Xt^{00} with Phi1 = (M gam/2)(w.xhat):", lap, " (r != 0)")
print("     monopole of Xt^{00} over a sphere |x| < R0 (angular integral of x/r^3 times r^2 dr):",
      sp.integrate(sp.integrate((xx / r**3).subs({xx: sp.Symbol('rr') * sp.cos(sp.Symbol('th')), yy: 0, zz: sp.Symbol('rr') * sp.sin(sp.Symbol('th'))})
                                * sp.sin(sp.Symbol('th')), (sp.Symbol('th'), 0, sp.pi)), (sp.Symbol('rr'), 1, 2)))
# ---------------- [K3] ----------------
om, k = sp.symbols('omega k', positive=True)
p, q = sp.symbols('p q', real=True)
C, Sn = sp.symbols('C S')
X = om / k
def dth(f):
    f = sp.expand(f); return sp.diff(f, C) * (-Sn) + sp.diff(f, Sn) * C
def Dd(mu, f):
    if mu == 0: return -om * dth(f)
    if mu == 3: return k * dth(f)
    return sp.Integer(0)
MOM = {(0, 0): 1, (2, 0): sp.Rational(1, 2), (0, 2): sp.Rational(1, 2)}
def avg(e):
    P_ = sp.Poly(sp.expand(e), C, Sn); out = 0
    for (i, j), cf in P_.terms():
        if i % 2 == 0 and j % 2 == 0: out += cf * MOM[(i, j)]
    return sp.expand(out)
rho, Tp, jx, tp = sp.symbols('rho T_perp j_x t_p', real=True)
J0 = sp.zeros(4, 4)
J0[0, 0] = rho; J0[0, 3] = J0[3, 0] = X * rho; J0[3, 3] = X**2 * rho
J0[0, 1] = J0[1, 0] = jx; J0[1, 3] = J0[3, 1] = X * jx
J0[1, 1] = Tp / 2 + tp; J0[2, 2] = Tp / 2 - tp
J = J0 * C
hbar_l = 16 * sp.pi * (eta * J0 * eta) * (p * C + q * Sn)
trb = sum(eta[i, i] * hbar_l[i, i] for i in range(4))
h = hbar_l - eta * trb / 2
gm = sp.Symbol('gamma', positive=True)
Xt_u = eta * ((-gm / (16 * sp.pi)) * hbar_l.applyfunc(lambda e: Dd(0, e))) * eta
trh = sum(eta[i, i] * h[i, i] for i in range(4))
def Q0(Xu):
    tot = 0
    for b in range(4):
        for m in range(4):
            Gam0 = sp.Rational(1, 2) * eta[0, 0] * (Dd(b, h[0, m]) + Dd(m, h[0, b]) - Dd(0, h[b, m]))
            tot += Gam0 * Xu[b, m]
    for b in range(4):
        tot -= Xu[0, b] * Dd(b, trh / 2)
    return avg(tot)
QX = sp.factor(sp.expand(Q0(Xt_u)))
QJ = sp.factor(sp.expand(Q0(J)))
SJ = sp.factor(avg(sum(J[0, b] * Dd(b, trh / 2) for b in range(4))))   # <d_b (1/2 trh J^{0b})> pieces: J^{0b} d_b trh/2 (dJ = 0)
print("\n[K3] per mode (p = Re G_gam, q = -Im G_gam; for the friction law q = -gam w |G_gam|^2):")
print("     <Q^0[h1; Xt1]> (field energy change due to the sink) =", QX)
print("     <Q^0[h1; J]>   (field energy change due to the record noise) =", QJ)
print("     <J^{0b} d_b trh/2> (a = 2 insertion term)            =", SJ)
Dn = (k**2 - om**2)**2 + gm**2 * om**2
sub = {p: (k**2 - om**2) / Dn, q: -gm * om / Dn}
tot = sp.simplify((QX + QJ).subs(sub))
print("     with the friction response: <Q^0[h1; J + Xt1]> =", tot, "(stationary balance: the sink absorbs exactly the noise's work)")
print("     TT channel alone: sink rate -<Q^0[h1;Xt1]> =", sp.factor(sp.simplify((-QX).subs({rho: 0, Tp: 0, jx: 0}).subs(sub))))
print("     rho channel alone: sink rate -<Q^0[h1;Xt1]> =", sp.factor(sp.simplify((-QX).subs({Tp: 0, jx: 0, tp: 0}).subs(sub))))
print("     (TT and rho channels heat the sink (>= 0); the V channel and the rho-T_perp cross term are sign-indefinite in the LL bookkeeping: see [K3b] bracket)")

# ---------------- [K3b] sink heating at the complete least-decoherence split (R19-2 B2 powers; E2 powers = E1/|R|) ----------------
xs = sp.Symbol('x', positive=True)
poly = sp.expand(-QX / (2*sp.pi*gm*om**2*(p**2 + q**2)) * k**4)   # bracket B such that sink rate = 2 pi gam w^2 |G|^2 B / k^4
B = sp.expand(poly.subs(om, xs*k) / k**4)
print("\n[K3b] sink rate per mode = 2 pi gam w^2 |G_gam|^2 B / k^4 with B =", sp.factor(B))
for region, sgn in (("spacelike", 1), ("timelike", -1)):
    g11 = (1 - xs**2)/2; gm_ = sp.Rational(1, 2)/g11; Dl = 1/(2*sgn*g11); p2s = sp.simplify(sgn*g11/(2*sp.Rational(1, 4)))
    p1 = sp.simplify(p2s*gm_**2 + Dl); qq = sp.simplify(-p2s*gm_); Pj = sp.Rational(1, 4); Pt = sgn*(1 - xs**2)/4
    # second-moment substitution: rho^2 -> p1, rho*T_perp -> qq, j_x^2 -> 2 Pj (two components), t_p^2 -> 2 Pt (two polarizations)
    Bc = sp.expand(B)
    val = (Bc.coeff(rho, 2)*p1 + Bc.coeff(rho, 1).coeff(Tp, 1)*qq + Bc.coeff(jx, 2)*2*Pj + Bc.coeff(tp, 2)*2*Pt)
    print("      %s, complete split: B = %s" % (region, sp.factor(sp.simplify(val))))
print("      => at the complete split the record noise heats the sink only through timelike modes (spacelike rate exactly 0, as Theorem I0)")
# ---------------- [K4] ----------------
print("\n[K4] budget numbers (SI; rho_L, H0 as R19-2/R18-7: H0 = 67.7 km/s/Mpc, Omega_L = 0.69):")
c = 2.998e8; H0 = 67.7e3 / 3.0857e22; tH = 1 / H0; gE = 0.5772156649
for ctau in (1.49e-3, 1.21e-4, 5e-6):
    ck = c / ctau
    for gH in (0.016, 0.047):
        gamma = gH * H0; Teq = np.exp(-gE) / gamma
        r_ = np.log(ck * Teq) / np.log(ck * tH)
        print("    c tau = %.2e m, gamma = %.3f H0: T_eq = %.1f t_H ; near-cone TT content E2(stationary)/E1(t_H) ~ ln(ck T_eq)/ln(ck t_H) = %.4f ;"
              " on a t_H history E2 keeps exp(-gamma t_H) = %.4f of E1's ; R12-7 split sink (gamma/3H0) = %.4f rho_GW"
              % (ctau, gH, Teq / tH, r_, np.exp(-gH), gH / 3))
print("    R19-2 D:17: rho_GW = 3.6e-5 rho_L at the tau_c corner -> E2's -rho_GW/3 term changes by <= 5%%; split sink <= %.1e rho_L" % (0.047 / 3 * 3.6e-5))
print("    friction on the homogeneous (background) mode, IF the FRW lift applied it there: relative O(gamma/H) = 0.016-0.047 in the expansion law (suggested size)")
print("    runtime %.1f s" % (time.time() - t0))
