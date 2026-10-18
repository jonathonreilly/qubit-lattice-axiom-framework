#!/usr/bin/env python3
"""C2_check ck4: independent (canonical-transformation) derivation of C2's S4 free direction (claim 1, {C,C} part).

Minimal theory in variables (gt, Pt, phi, pit) with C~ = (1/sqrt gt)(Pt.Pt - trPt^2/2) - K sqrt gt R[gt] + pit^2/(2 sqrt gt)
+ sqrt gt (c/2 gt^ij dphi dphi + mu/2 phi^2)  (alpha = 1/4, 16 pi G = 1/K units as in C2 S4).  Point transformation
gt = W g, W = 1 - 2 s phi^2 (spatial metric), lapse N~ = sqrt(W) N  =>  P = W Pt, pi = pit + W'(phi) g_ij Pt^ij,
C = sqrt(W) C~ (from int N~ C~ = int N C).  Expanded to first order in s and second order in matter, at h = 0
(flat g), this predicts the coefficients of zeta phi^2 sqrt g R(g) [via the h-linear part], cp lap(phi^2), w trP phi pi,
phi^2 (y1 trPP + y2 trP^2).  C2's S4 found (zeta, cp, w, y1, y2) = (2s, -4s, 4s, 2s, -s) with K = 1 by brackets.
The 3D conformal identity R[W g] is computed explicitly (sympy, general conformally flat metric), not quoted.
"""
import sympy as sp
x = sp.symbols("x0:3"); s, K = sp.symbols("s K")
f = sp.Function("f")(*x)                     # phi^2 profile placeholder: W = 1 - 2 s f
W = 1 - 2 * s * f
g = W * sp.eye(3)
gi = g.inv()
Gam = [[[sum(gi[l, m] * (sp.diff(g[m, a], x[b]) + sp.diff(g[m, b], x[a]) - sp.diff(g[a, b], x[m])) for m in range(3)) / 2
         for b in range(3)] for a in range(3)] for l in range(3)]
R = 0
for a in range(3):
    for b in range(3):
        Rab = sum(sp.diff(Gam[l][a][b], x[l]) - sp.diff(Gam[l][a][l], x[b]) for l in range(3))
        Rab += sum(Gam[l][l][m] * Gam[m][a][b] - Gam[l][b][m] * Gam[m][a][l] for l in range(3) for m in range(3))
        R += gi[a, b] * Rab
sqrtgt = W ** sp.Rational(3, 2)
grav = -K * sp.sqrt(W) * sqrtgt * R           # sqrt(W) x (-K sqrt gt R[gt]) at flat g
grav1 = sp.simplify(sp.series(sp.simplify(grav), s, 0, 2).removeO().coeff(s, 1))
lap_f = sum(sp.diff(f, xi, 2) for xi in x)
cp = sp.simplify(grav1 / lap_f)
print("   O(s) gravity-potential term at flat g:", grav1, " -> cp/s =", cp)
# zeta: h-linear part.  For g = (1+eps) delta-type conformal h this is not general; instead use the scalar structure
# sqrt(W) sqrt gt R[gt] = W^2 sqrt g (R[g] + ...) for constant f:  coefficient of f sqrt g R(g) at O(s)
zeta = sp.series(-K * sp.sqrt(W) * W ** sp.Rational(3, 2) / W, s, 0, 2).removeO().coeff(s, 1) / f   # W^{1/2} W^{3/2} W^{-1}
zeta = sp.simplify(zeta * s)   # C contains -K sqrt g R + zeta phi^2 sqrt g R  (run 1 had a spurious sign flip and dropped s)
print("   zeta =", zeta, "(coefficient of +phi^2 sqrt g R in C, K units)")
# kinetic: (1/sqrt gt)(Pt.Pt - trPt^2/2) with Pt = P/W, gt = W g: Pt.Pt|_gt = P.P|_g (indices), so kin = W^{-3/2} W^0 kin_g
kin_fac = sp.series(sp.sqrt(W) * W ** sp.Rational(-3, 2), s, 0, 2).removeO().coeff(s, 1) / f
print("   phi^2 (trPP - trP^2/2) coefficient / s =", sp.simplify(kin_fac), " -> y1 =", sp.simplify(kin_fac), ", y2 =", sp.simplify(-kin_fac / 2))
# matter momentum: pit = pi - W' g_ij Pt^ij = pi + 4 s phi trP (to O(s)); pit^2/(2 sqrt gt) cross term
phi, pi, trP = sp.symbols("phi pi trP")
Wp = sp.diff(1 - 2 * s * phi ** 2, phi)
pit = pi - Wp * trP
cross = sp.expand(pit ** 2 / 2).coeff(pi, 1).coeff(trP, 1)
print("   w (coefficient of trP phi pi) =", sp.simplify(cross / phi))
ok = (sp.simplify(s * cp - (-4 * s * K)) == 0 and sp.simplify(zeta - 2 * s * K) == 0 and sp.simplify(s * kin_fac - 2 * s) == 0
      and sp.simplify(cross / phi - 4 * s) == 0)
print(("PASS" if ok else "FAIL") + ": J1 canonical Jordan-frame map reproduces C2 S4's free direction (zeta, cp, w, y1, y2) = "
      "(2sK, -4sK, 4s, 2s, -s) independently of the bracket engine; so the {C,C} freedom is a field redefinition and "
      "zeta (at O(phi^2), linear order) is a frame label")
print(f"TOTAL: PASS={int(ok)} FAIL={int(not ok)}")
