#!/usr/bin/env python3
"""R19-6 [K]: relative channel normalization behind the I0 zero.  The least-decoherence powers of R19-2 (P = 1/(2|G|)
per channel, S block on R15-2's K_rr-floor family) are built on the exchange kernel G of R15-2 Lemma A, quoted in
r192_split.py as  S: [[(1-x^2)/2, 1/2],[1/2, 0]],  V (per j_a): -2,  TT (per t): 2/(1-x^2)   (units 16 pi G = 1, k = 1).
Check: the exchange form J^{mu nu} h_{mu nu}[J] of the Poisson-gauge solution solved in r196_setA.py ([A1]),
converted from G = 1 to 16 pi G = 1 (8 pi -> 1/2), reproduces that kernel in one convention for all channels.
Subtraction: none.
"""
import sympy as sp
om, k = sp.symbols('omega k', positive=True)
x = sp.Symbol('x', positive=True)
rho, Tp, jx, tp = sp.symbols('rho T_perp j_x t_p', real=True)
X = om / k
pi = sp.pi
# r196_setA.out [A1] (G = 1): Phi, Psi, S_x, h_+
Phi = -4*pi*(Tp*k**2 + k**2*rho - 2*om**2*rho)/k**4
Psi = -4*pi*rho/k**2
Sx = -16*pi*jx/k**2
hp = 16*pi*tp/((k - om)*(k + om))
h = sp.zeros(4, 4)
h[0, 0] = -2*Phi; h[0, 1] = h[1, 0] = Sx
for i in (1, 2, 3):
    h[i, i] = -2*Psi
h[1, 1] += hp; h[2, 2] += -hp
J = sp.zeros(4, 4)
J[0, 0] = rho; J[0, 3] = J[3, 0] = X*rho; J[3, 3] = X**2*rho
J[0, 1] = J[1, 0] = jx; J[1, 3] = J[3, 1] = X*jx
J[1, 1] = Tp/2 + tp; J[2, 2] = Tp/2 - tp
E = sp.expand(sum(J[m, n]*h[m, n] for m in range(4) for n in range(4)))
E16 = sp.expand((E/(16*pi)).subs(om, x*k)*k**2)        # G = 1 -> 16 pi G = 1 means divide by 16 pi
P = sp.Poly(E16, rho, Tp, jx, tp)
print("[K1] exchange form J.h[J] in units 16 pi G = 1, k = 1:")
for mon in (rho**2, rho*Tp, Tp**2, jx**2, tp**2, rho*jx, rho*tp):
    print("     %-8s %s" % (mon, sp.factor(P.coeff_monomial(mon))))
print("[K2] quoted kernel: rho^2 (1-x^2)/2, rho T_perp 2*(1/2) = 1, T_perp^2 0, j^2 -2, t^2 2/(1-x^2): match =",
      all(sp.simplify(P.coeff_monomial(m) - v) == 0 for m, v in
          ((rho**2, (1 - x**2)/2), (rho*Tp, 1), (Tp**2, 0), (jx**2, -2), (tp**2, 2/(1 - x**2)))))
