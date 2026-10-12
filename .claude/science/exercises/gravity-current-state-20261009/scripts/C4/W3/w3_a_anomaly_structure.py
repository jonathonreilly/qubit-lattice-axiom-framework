"""C4 / RW / W3 part A: what the C3 anomaly fixes in the quadratic action.
(a) dS_anom = a int[ grad B.grad eps - grad chi.grad Phi ] is the gauge variation of the SVT-local
    functional F = a[ -grad Phi.grad E - 1/2 (grad(B - E_dot))^2 ]   (trivial in SVT-local cohomology);
(b) W2's WZ term equals I - F up to total derivatives, I := F evaluated on the Stueckelberg invariants
    U = Phi + pi_dot, V = B - pi + zeta_dot, W = E + zeta  (so V - W_dot = sigma - pi);
(c) F vanishes in W2's gauge B = E = 0, so W2's gauge-fixed spectrum is that of the invariant theory
    L_GR + F + L_WZ = L_GR + I, i.e. of the unitary-gauge action L_GR + F;
(d) no F that is LOCAL in h_mu nu exists among the five rotation-invariant mass terms
    (h00^2, h0i h0i, hij hij, hii^2, h00 hii): the cocycle is non-trivial in the h-local class, so the
    anomaly is the coefficient of a fixed h-NONLOCAL structure (Polyakov-like), everything else is free."""
import sys; sys.path.insert(0, '.')
import sympy as sp
from w3_lib import *

a, Mp2 = sp.symbols('a M_p2', real=True)
Phi, B, Psi, E, pi_, zeta, eps, chi = [F(n) for n in ('Phi', 'B', 'Psi', 'E', 'pi', 'zeta', 'eps', 'chi')]
gauge = {Phi: dt(eps), B: -eps + dt(chi), E: chi, Psi: sp.Integer(0), pi_: -eps, zeta: -chi}
anom = a*(dot(grad(B), grad(eps)) - dot(grad(chi), grad(Phi)))
sig = B - dt(E)
Ffun = lambda P, Bf, Ef: a*(-dot(grad(P), grad(Ef)) - sp.Rational(1, 2)*dot(grad(Bf - dt(Ef)), grad(Bf - dt(Ef))))
Fm = Ffun(Phi, B, E)
ok, f, el = euler_zero(sp.expand(vary(Fm, gauge) - anom), None)
print("(a) delta F - dS_anom is a total derivative:", ok)

U = Phi + dt(pi_); V = B - pi_ + dt(zeta); Wf = E + zeta
for nm, q in (('U', U), ('V', V), ('W', Wf)):
    print(f"    {nm} gauge invariant:", sp.simplify(vary(q, gauge)) == 0)
I = Ffun(U, V, Wf)
ok, f, el = euler_zero(sp.expand(vary(I, gauge)), None)
print("    I = F[U,V,W] gauge invariant (up to total derivative):", ok)
L_WZ = a*(dot(grad(B), grad(pi_)) - dot(grad(zeta), grad(Phi)) + dot(grad(dt(zeta)), grad(pi_))
          - sp.Rational(1, 2)*dot(grad(pi_), grad(pi_)))
ok, f, el = euler_zero(sp.expand(L_WZ - (I - Fm)), None)
print("(b) L_WZ(W2) - (I - F) is a total derivative:", ok)
print("(c) F at B = E = 0:", sp.simplify(Fm.subs({B: 0, E: 0}).doit()))

# unitary-gauge spectrum of L_GR + F (fields Phi, B, Psi, E) vs W2's root
L_GR = Mp2*(-3*dt(Psi)**2 + dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi)) - 2*dt(Psi)*lap(sig))
M = fourier_matrix(L_GR + Fm, [Phi, B, Psi, E])
det = sp.factor(sp.simplify(M.det()))
print("    unitary gauge L_GR + F: det M =", det)
Wsym = sp.symbols('W')
print("    roots in w^2:", sp.solve(sp.Eq(sp.simplify(det.subs(w, sp.sqrt(Wsym))), 0), Wsym), " (W2: a k^2/(3a - 2 Mp2 k^2))")

# (d) h-local mass-term class: h00 = Phi (normalisation irrelevant), h0i = d_i B, hij = -2 Psi delta + 2 d_i d_j E
cs = sp.symbols('c0:5')
h00 = Phi; h0 = grad(B)
hij = [[-2*Psi*(1 if i == j else 0) + 2*sp.diff(E, X[i], X[j]) for j in range(3)] for i in range(3)]
tr = sum(hij[i][i] for i in range(3))
masses = [h00**2, dot(h0, h0), sum(hij[i][j]**2 for i in range(3) for j in range(3)), tr**2, h00*tr]
Floc = sum(c*m for c, m in zip(cs, masses))
total = sp.expand(vary(Floc, gauge) - anom)
eqs = []
for fld in [Phi, B, Psi, E, eps, chi]:
    res = sp.euler_equations(total, [fld], [t, x, y, z])
    el = sp.expand(res[0].lhs if res else 0)
    if el == 0: continue
    derivs = sorted(el.atoms(sp.Derivative).union(el.atoms(sp.Function)), key=str)
    eqs += [sp.expand(cf) for cf in sp.Poly(el, *derivs).coeffs()]
print("(d) h-local mass terms solving delta F_loc = dS_anom:", sp.solve(eqs, cs, dict=True), "(empty => none: non-trivial in the h-local class)")
