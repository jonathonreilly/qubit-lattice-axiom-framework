"""R2-1 probe (a), graviton sector at kappa^0: a gauge-covariant (Whitney/DEC-type) linear blocking
of linearized gravity on Z^d. Continuum gauge map dh_{mn} = d_m xi_n + d_n xi_m.
Blocked gauge parameter: Xi_n(x) = int_0^1 xi_n(x + s e_n) ds          (link average along n)
Blocked metric:          H_{mn}(x) = int_0^1 int_0^1 h_{mn}(x + s e_m + u e_n) ds du  (m != n, plaquette)
                         H_{nn}(x) = (1/2) int_0^1 int_0^1 h_{nn}(x + (s+u) e_n) ds du (tent, two links)
Claim (exact): B_h(dh) = D_m Xi_n + D_n Xi_m with D the FORWARD difference, i.e. the blocked free
graviton inherits an exact, strictly local lattice gauge identity (K2's K7a-type placement).
Transverse smearing (any kernel along the other axes, same for all components) commutes with this.
Checked symbolically in d=2 for a random cubic polynomial xi plus a trig term."""
import sympy as sp
x, y, s, u = sp.symbols('x y s u', real=True)
X = [x, y]
import random
random.seed(3)
def rpoly():
    return sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4)) * x**i * y**j
               for i in range(4) for j in range(4 - i)) + sp.sin(x + 2*y) * sp.Rational(1, 3)
xi = [rpoly(), rpoly()]
e = [{x: x + s, y: y}, {x: x, y: y + s}]
def shift(f, n, amt):
    return f.subs(X[n], X[n] + amt)
def Xi(n):
    return sp.integrate(shift(xi[n], n, s), (s, 0, 1))
def D(f, mdir):
    return sp.simplify(shift(f, mdir, 1) - f)
h = [[sp.diff(xi[nn], X[mm]) + sp.diff(xi[mm], X[nn]) for nn in range(2)] for mm in range(2)]
ok = True
for mm in range(2):
    for nn in range(2):
        if mm != nn:
            Hb = sp.integrate(sp.integrate(shift(shift(h[mm][nn], mm, s), nn, u), (s, 0, 1)), (u, 0, 1))
        else:
            Hb = sp.Rational(1, 2) * sp.integrate(sp.integrate(shift(h[nn][nn], nn, s + u), (s, 0, 1)), (u, 0, 1))
        rhs = D(Xi(nn), mm) + D(Xi(mm), nn) if mm != nn else 2 * D(Xi(nn), nn) / 2 * 1
        if mm == nn:
            rhs = D(Xi(nn), nn)  # H_nn defined with the 1/2: B(2 d_n xi_n)/2 ... see below
            Hb = Hb  # H_nn = (1/2) tent-average of h_nn = tent-average of d_n xi_n = D_n Xi_n
        diff = sp.simplify(sp.expand(Hb - rhs))
        print("component (%d,%d): blocked(dh) - lattice gauge term = %s" % (mm, nn, diff))
        ok = ok and diff == 0
print("EXACT:", ok, "-> with H_nn normalized as above, delta H_mn = D_m Xi_n + D_n Xi_m (m!=n), delta H_nn = D_n Xi_n")
print("   (i.e. delta H = D Xi + (D Xi)^T with the diagonal carrying the conventional factor 1/2).")
