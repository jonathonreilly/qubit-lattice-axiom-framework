"""Refuting pass, block 19 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the Legendre coefficients of e^{beta t} by the generating-function route: the series coefficients of e^{beta t} expanded in
     P_l via the orthogonality relation applied to the Taylor series in t, compared with the Rodrigues integrals, l <= 3,
     at beta = 1 and beta = 3 exactly (modified spherical Bessel forms);
(R2) the gradient sum by direct bond enumeration on a 6x4x4 torus at k = (pi/3, 0, 0): sum over bonds (dpsi)^2 versus E(k) sum psi^2
     with E = 2(1 - cos(pi/3)) = 1;
(R3) the single-bond second-derivative identity with the generator about e_1 instead of e_2 (the transverse pair becomes (s^2, s^3));
(R4) the integral bound by a second inequality: E(k) >= (2/pi^2) |k|^2 ... no: use 1 - cos u >= u^2/(2) - u^4/24 (Taylor lower bound) to
     confirm the sample-point inequality independently at the 21 points; and the ball integral by spherical coordinates symbolically.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import sys
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
r19 = importlib.import_module("admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15")
t = sp.symbols("t", real=True)
ok1 = True
for b in (1, 3):
    for l in range(4):
        # orthogonality route: a_l = (2l+1)/2 int e^{bt} P_l dt computed from the Taylor series of e^{bt} to order 40
        series = sum(sp.Rational(b ** n, sp.factorial(n)) * t ** n for n in range(41))
        a_series = sp.Rational(2 * l + 1, 2) * sp.integrate(series * sp.legendre(l, t), (t, -1, 1))
        a_rod = sp.Rational(2 * l + 1, 2) * sp.Integer(b) ** l / (2 ** l * sp.factorial(l)) * sp.integrate((1 - t ** 2) ** l * sp.exp(b * t), (t, -1, 1))
        gap = abs(sp.N(a_series - a_rod, 30))
        ok1 = ok1 and gap < sp.Rational(1, 10 ** 12) and a_rod > 0
print("R1 orthogonality route (Taylor to order 40) agrees with the Rodrigues integrals for l <= 3 at beta = 1, 3, all positive:", ok1)
L = (6, 4, 4)
sites = list(product(range(L[0]), range(L[1]), range(L[2])))
def nbrs(x):
    out = []
    for i in range(3):
        for d in (1, -1):
            y = list(x); y[i] = (x[i] + d) % L[i]; out.append(tuple(y))
    return out
k = (sp.pi / 3, 0, 0)
E = sum(2 * (1 - sp.cos(ki)) for ki in k)
psi = {x: sp.cos(sum(ki * xi for ki, xi in zip(k, x))) for x in sites}
bonds = {tuple(sorted((x, y))) for x in sites for y in nbrs(x)}
grad2 = sp.simplify(sum((psi[x] - psi[y]) ** 2 for (x, y) in bonds))
sum2 = sp.simplify(sum(psi[x] ** 2 for x in sites))
print("R2 6x4x4 torus at k = (pi/3,0,0): E =", E, "; sum_b (dpsi)^2 =", grad2, "; E sum psi^2 =", sp.simplify(E * sum2), "; equal:", sp.simplify(grad2 - E * sum2) == 0, "; N/2 =", len(sites) / 2)
sx = sp.Matrix(sp.symbols("x1 x2 x3", real=True)); sy = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
e1 = sp.Matrix([1, 0, 0])
def Lg(v, F):
    w = e1.cross(v)
    return sum(w[i] * sp.diff(F, v[i]) for i in range(3))
cx, cy = sp.symbols("c_x c_y")
dot = sx.dot(sy)
Lc = lambda F: cx * Lg(sx, F) + cy * Lg(sy, F)
Lcb = lambda F: sp.conjugate(cx) * Lg(sx, F) + sp.conjugate(cy) * Lg(sy, F)
second = -Lc(Lcb(dot))
target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[1] * sy[1] + sx[2] * sy[2])
print("R3 second-derivative identity with the generator about e_1 (transverse pair (s^2, s^3)):", sp.simplify(sp.expand(second - target)) == 0)
u = sp.symbols("u", real=True)
samples = [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)]
ok4 = all(sp.simplify(1 - sp.cos(x) - 2 * x ** 2 / sp.pi ** 2) >= 0 for x in samples) and all((1 - sp.cos(x)) >= (x ** 2 / 2 - x ** 4 / 24) for x in samples if abs(x) <= sp.pi)
r, th, ph = sp.symbols("r theta phi", positive=True)
ball = sp.integrate(sp.integrate(sp.integrate(sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)), (r, 0, sp.sqrt(3) * sp.pi))  # int d^3k/|k|^2 = int r^2 sin / r^2
print("R4 cosine inequalities at the sample points:", ok4, "; the ball integral in spherical coordinates =", sp.simplify(ball), "= 4 pi sqrt(3) pi:", sp.simplify(ball - 4 * sp.pi * sp.sqrt(3) * sp.pi) == 0)
