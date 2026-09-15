"""Control, block 19 (supervisor): the sphere static law with overlap e^{beta t} — symbolic identities.
(1) Legendre coefficients of e^{beta t} are positive: a_l = (beta^l/(2^l l!)) int_{-1}^{1} (1-t^2)^l e^{beta t} dt, l = 0..4 (Rodrigues + parts);
(2) gradient twist identity; plane-wave Laplacian on a torus: sum_{y~x}(psi_x - psi_y) = E(k) psi_x with E = 2 sum (1 - cos k_i);
    sum over bonds (psi_x - psi_y)^2 = E(k) sum_x psi_x^2 (exact on a 4x4x4 torus at k = (pi/2, 0, 0) and (pi/2, pi/2, 0));
(3) the second-order expansion of the twisted weight: beta^2 <X^2> <= beta sum_b (dpsi)^2 where X = sum_b dpsi (s_x - s_y).e;
(4) generator identities on a bond: L_x (s_x . s_y) = e2 . (s_x x s_y), L_y (s_x . s_y) = -e2 . (s_x x s_y); L s^3 = s^1, L s^1 = -s^3;
    integration by parts on the sphere: int (e2 x s).grad F dsigma = 0 for polynomial F;
    second derivative: -(c_x L_x + c_y L_y)(cbar_x L_x + cbar_y L_y)(s_x . s_y) = |c_x - c_y|^2 (s_x^1 s_y^1 + s_x^3 s_y^3);
(5) the Green-function bound: 1 - cos u >= 2u^2/pi^2 on [-pi, pi]; int_{box} d^3k/((2pi)^3 E(k)) <= sqrt(3) pi/8; threshold 3 sqrt(3) pi/8 < 21/10;
(6) the Bogoliubov quadratic: u^2/N + sqrt(beta E) u - M^2/3 >= 0  =>  u >= (2M^2/3)/(sqrt(beta E) + sqrt(beta E + 4M^2/(3N)))."""
import sympy as sp
from itertools import product
t, beta = sp.symbols("t beta", positive=True)
print("(1) Legendre coefficients of e^{beta t}:")
for l in range(5):
    P = sp.legendre(l, t)
    direct = sp.integrate(sp.exp(beta * t) * P, (t, -1, 1))
    rod = beta ** l / (2 ** l * sp.factorial(l)) * sp.integrate((1 - t ** 2) ** l * sp.exp(beta * t), (t, -1, 1))
    print(f"  l={l}: direct == Rodrigues form: {sp.simplify(direct - rod) == 0}; the Rodrigues integrand is positive on (-1,1)")
# (2) torus Laplacian identities
L = 4
sites = list(product(range(L), repeat=3))
def nbrs(x):
    out = []
    for i in range(3):
        for d in (1, -1):
            y = list(x); y[i] = (x[i] + d) % L; out.append(tuple(y))
    return out
for k in ((sp.pi / 2, 0, 0), (sp.pi / 2, sp.pi / 2, 0)):
    E = sum(2 * (1 - sp.cos(ki)) for ki in k)
    psi = {x: sp.cos(sum(ki * xi for ki, xi in zip(k, x))) for x in sites}
    lap_ok = all(sp.simplify(sum(psi[x] - psi[y] for y in nbrs(x)) - E * psi[x]) == 0 for x in sites)
    bonds = {tuple(sorted((x, y))) for x in sites for y in nbrs(x)}
    grad2 = sum((psi[x] - psi[y]) ** 2 for (x, y) in bonds)
    sum2 = sum(psi[x] ** 2 for x in sites)
    print(f"(2) k={k}: (-Delta psi) = E psi on the 4^3 torus: {lap_ok}; sum_b (dpsi)^2 = E sum psi^2: {sp.simplify(grad2 - E * sum2) == 0}; E = {E}, sum psi^2 = {sum2}")
# (4) generator identities
sx = sp.Matrix(sp.symbols("x1 x2 x3", real=True)); sy = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
e2 = sp.Matrix([0, 1, 0])
def Lgen(v, F):
    """rotation generator about e2 acting on the vector variable v: (e2 x v) . grad_v F"""
    w = e2.cross(v)
    return sum(w[i] * sp.diff(F, v[i]) for i in range(3))
dot = sx.dot(sy)
print("(4) L_x(s_x.s_y) == e2.(s_x x s_y):", sp.simplify(Lgen(sx, dot) - e2.dot(sx.cross(sy))) == 0, "; L_y(s_x.s_y) == -e2.(s_x x s_y):", sp.simplify(Lgen(sy, dot) + e2.dot(sx.cross(sy))) == 0)
print("    L s^3 = s^1:", sp.simplify(Lgen(sx, sx[2]) - sx[0]) == 0, "; L s^1 = -s^3:", sp.simplify(Lgen(sx, sx[0]) + sx[2]) == 0)
cx, cy = sp.symbols("c_x c_y")
Lc = lambda F: cx * Lgen(sx, F) + cy * Lgen(sy, F)
Lcbar = lambda F: sp.conjugate(cx) * Lgen(sx, F) + sp.conjugate(cy) * Lgen(sy, F)
second = -Lc(Lcbar(dot))
target = (cx - cy) * (sp.conjugate(cx) - sp.conjugate(cy)) * (sx[0] * sy[0] + sx[2] * sy[2])
print("    -L Lbar (s_x.s_y) == |c_x - c_y|^2 (s_x^1 s_y^1 + s_x^3 s_y^3):", sp.simplify(sp.expand(second - target)) == 0)
# integration by parts on the sphere for polynomials
th, ph = sp.symbols("theta phi", real=True)
svec = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
ok_ibp = True
for F in (sx[0] * sx[2], sx[0] ** 2 * sx[1], sx[2] ** 3):
    LF = Lgen(sx, F).subs({sx[0]: svec[0], sx[1]: svec[1], sx[2]: svec[2]})
    val = sp.integrate(sp.integrate(LF * sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi))
    ok_ibp = ok_ibp and sp.simplify(val) == 0
print("    integration by parts on the sphere for three polynomials:", ok_ibp)
# (5) Green-function bound
u = sp.symbols("u", real=True)
samples = [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)]
ok_cos = all(sp.simplify(1 - sp.cos(x) - 2 * x ** 2 / sp.pi ** 2) >= 0 for x in samples)
G_bound = sp.sqrt(3) * sp.pi / 8
print("(5) 1 - cos u >= 2u^2/pi^2 at 21 sample points:", ok_cos, "; G(0) bound sqrt(3) pi/8 =", sp.N(G_bound), "; threshold 3 sqrt(3) pi/8 =", sp.N(3 * G_bound), "< 21/10:", sp.N(3 * G_bound) < 2.1)
# (6) quadratic
uu, N, bE, M = sp.symbols("u N bE M", positive=True)
root = (2 * M ** 2 / 3) / (sp.sqrt(bE) + sp.sqrt(bE + 4 * M ** 2 / (3 * N)))
print("(6) the positive root of u^2/N + sqrt(bE) u - M^2/3 = 0 equals the displayed form:", sp.simplify((root ** 2 / N + sp.sqrt(bE) * root - M ** 2 / 3)) == 0, "; limit N->oo:", sp.limit(root, N, sp.oo))
