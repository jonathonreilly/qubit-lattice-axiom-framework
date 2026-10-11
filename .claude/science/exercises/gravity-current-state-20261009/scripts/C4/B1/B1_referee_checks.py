"""Independent exact checks for the C4/RB/B1 referee.

These checks deliberately do not reuse the worker's numerical implementation.
They target four load-bearing or correction-bearing formulas:

1. a smooth 1D band for which the additive fixed-N lift closes after adjoining
   the central particle number, so the worker's universal soccer-ball wording
   is too strong;
2. the advertised Magueijo--Smolin coefficient is not C1 on the Brillouin
   circle, although a smooth periodic replacement is easy;
3. the nearest-neighbour d=2 Hessian collision used by Theorem D;
4. the quadratic LIV scale of the axis lattice dispersion.
"""

import sympy as sp


k, m, A, v, a, H, N, Htot = sp.symbols(
    "k m A v a H N Htot", positive=True, real=True
)

print("=== 1D affine-deformation / fixed-N additive closure ===")
omega = m + A * (1 - sp.cos(k))
V = v
P = sp.simplify(V * sp.diff(omega, k))
F = sp.simplify(V * sp.diff(P, k))
F_of_H = sp.simplify(F.subs(sp.cos(k), (m + A - H) / A))
sum_F_fixed_N = sp.expand(v**2 * (N * (m + A) - Htot))
print("omega =", omega)
print("P =", P)
print("F =", F, "=", F_of_H)
print("sum_i F_i at fixed N =", sum_F_fixed_N)
print("orbit integral =", sp.simplify(sp.integrate(F_of_H, (H, m, m + 2 * A))))

print("\n=== half-angle MS coefficient is not smooth on T^1 ===")
omega_kg = sp.sqrt(m**2 + 2 * (1 - sp.cos(k)))
V_half = omega_kg * sp.cos(k / 2)
dV_half = sp.diff(V_half, k)
print("V(-pi), V(pi) =", sp.simplify(V_half.subs(k, -sp.pi)), sp.simplify(V_half.subs(k, sp.pi)))
print("V'(-pi), V'(pi) =", sp.simplify(dV_half.subs(k, -sp.pi)), sp.simplify(dV_half.subs(k, sp.pi)))
V_smooth = sp.simplify(omega_kg * (1 + sp.cos(k)))
print("smooth periodic replacement V =", V_smooth)
print("replacement V'(-pi)-V'(pi) =", sp.simplify(sp.diff(V_smooth, k).subs(k, -sp.pi) - sp.diff(V_smooth, k).subs(k, sp.pi)))

print("\n=== Theorem D: exact d=2 nearest-neighbour collision ===")
k1, k2 = sp.symbols("k1 k2", real=True)
u = m**2 / 2 + 2 - sp.cos(k1) - sp.cos(k2)
grad = sp.Matrix([sp.diff(u, k1), sp.diff(u, k2)])
hess = sp.hessian(u, (k1, k2))
X = {k1: sp.pi, k2: 0}
Xp = {k1: 0, k2: sp.pi}
print("u(X)-u(X') =", sp.simplify(u.subs(X) - u.subs(Xp)))
print("grad(X), grad(X') =", grad.subs(X).T, grad.subs(Xp).T)
print("Hess(X) =", hess.subs(X))
print("Hess(X') =", hess.subs(Xp))
print("Hess difference =", hess.subs(X) - hess.subs(Xp))

print("\n=== quadratic lattice LIV scale ===")
energy = 2 * sp.sin(a * k / 2) / a
energy_sq_series = sp.series(energy**2, k, 0, 6)
print("E^2 series =", energy_sq_series)
print("matching E^2=p^2[1-(p/E_QG,2)^2] gives E_QG,2 = sqrt(12)/a")
