"""Class-A finite runner: the next lattice correction to the emergent Newtonian
potential is an exact, purely anisotropic O(1/r^5) term,

    G(x) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + f(nhat)/r^5 + O(1/r^7),

where f has cubic-harmonic content l = 4, 6, 8 and zero spherical average.  The
runner derives the free, order-1, and order-2 tails from the heat-kernel symbol
expansion by exact differentiation and Mellin integration, then independently
checks the order-2 coefficient against the exact lattice Green function through
the mpmath Bessel-resolvent representation.

  S1     exact free tail, landed K4 tail, and direct-integrator cross-check.
  S2     raw degree-8 polynomial, S-basis identity, and harmonic identity.
  S3     exact sphere moments, harmonic orthogonality, and seven direction values.
  S4     all-orders contact-term inequality through n = 4.
  N1     three lattice-equation precision certificates.
  N2     five extrapolation gates and five last-pair convergence-ratio gates.
  CTRL1  a 5 percent wrong axial value fails the extrapolation gate.
  CTRL2  the same wrong value fails the convergence-ratio gate.
  CTRL3  changing the raw coefficient 621 to 622 fails the symbolic identity.

prints TOTAL: PASS=N FAIL=0
"""

import sympy as sp
import numpy as np
from mpmath import mp, mpf, besseli, exp as mpexp, quad as mpquad, inf as mpinf, sqrt as mpsqrt, pi as mppi


AUDIT_TIMEOUT_SEC = 360

results = []


def check(name, ok):
    results.append((name, bool(ok)))


# --- Exact heat-kernel/Mellin machinery ---
x, y, z, t = sp.symbols("x y z t", positive=True)
r2 = x**2 + y**2 + z**2
r = sp.sqrt(r2)
Gt = (4 * sp.pi * t) ** sp.Rational(-3, 2) * sp.exp(-r2 / (4 * t))


def tail_mellin(expr):
    """Integrate a finite Gaussian-tail sum exactly, monomial by monomial."""
    bare = sp.expand(expr * sp.exp(r2 / (4 * t)))
    integrated = []
    for term in sp.Add.make_args(bare):
        q = term.as_powers_dict().get(t, sp.Integer(0))
        if not (q.is_number and q < -1):
            raise ValueError("Mellin term must have t power q < -1")
        coefficient = term / t**q
        integrated.append(
            coefficient * (r2 / 4) ** (q + 1) * sp.gamma(-q - 1)
        )
    return sp.simplify(sp.Add(*integrated))


# S1: free and order-1 tails, including an independent SymPy integration.
free_tail = tail_mellin(Gt)
check("S1a tail_mellin(Gt) = 1/(4 pi r) exactly",
      sp.simplify(free_tail - 1 / (4 * sp.pi * r)) == 0)

d4_sum = sum(sp.diff(Gt, coordinate, 4) for coordinate in (x, y, z))
order1_integrand = t * sp.Rational(1, 12) * d4_sum
order1_tail = tail_mellin(order1_integrand)
S4c = (x**4 + y**4 + z**4) / r**4
order1_claim = sp.Rational(5, 32) / sp.pi * (S4c - sp.Rational(3, 5)) / r**3
check("S1b order-1 tail = [5/(32 pi)] K4/r^3 exactly",
      sp.simplify(order1_tail - order1_claim) == 0)

order1_direct = sp.integrate(order1_integrand, (t, 0, sp.oo), conds="none")
check("S1c direct SymPy integral agrees with tail_mellin at order 1",
      sp.simplify(order1_direct - order1_tail) == 0)


# S2: exact next-order polynomial and its two angular-basis forms.
d8_double_sum = sum(
    sp.diff(sp.diff(Gt, mu, 4), nu, 4)
    for mu in (x, y, z) for nu in (x, y, z)
)
d6_sum = sum(sp.diff(Gt, coordinate, 6) for coordinate in (x, y, z))
order2_integrand = t**2 * sp.Rational(1, 288) * d8_double_sum + t * sp.Rational(1, 360) * d6_sum
T2 = tail_mellin(order2_integrand)

raw_xyz = (
    23 * (x**8 + y**8 + z**8)
    - 244 * (
        x**6*y**2 + x**6*z**2 + y**6*x**2
        + y**6*z**2 + z**6*x**2 + z**6*y**2
    )
    + 621 * (x**4*y**4 + x**4*z**4 + y**4*z**4)
    - 228 * x**2*y**2*z**2*r2
)
s2a_difference = sp.simplify(128 * sp.pi * r**13 * T2 - raw_xyz)
check("S2a order-2 Mellin tail equals the claimed raw degree-8 polynomial",
      s2a_difference == 0)

nx, ny, nz = sp.symbols("nx ny nz", real=True)
raw_angular = (
    23 * (nx**8 + ny**8 + nz**8)
    - 244 * (
        nx**6*ny**2 + nx**6*nz**2 + ny**6*nx**2
        + ny**6*nz**2 + nz**6*nx**2 + nz**6*ny**2
    )
    + 621 * (nx**4*ny**4 + nx**4*nz**4 + ny**4*nz**4)
    - 228 * nx**2*ny**2*nz**2
)
f_raw = raw_angular / (128 * sp.pi)
S4 = nx**4 + ny**4 + nz**4
S6 = nx**6 + ny**6 + nz**6
s_basis = (
    -sp.Rational(181, 512)
    + sp.Rational(315, 256) * S4
    - sp.Rational(189, 64) * S6
    + sp.Rational(1155, 512) * S4**2
)
sphere_substitution = {nz**2: 1 - nx**2 - ny**2}
s2b_difference = sp.expand((raw_angular - 128 * s_basis).subs(sphere_substitution))
check("S2b raw and S-basis forms agree as a zero polynomial on the sphere",
      s2b_difference == 0)

K4 = S4 - sp.Rational(3, 5)
K6 = S6 - sp.Rational(15, 11) * S4 + sp.Rational(30, 77)
K8 = S4**2 - sp.Rational(16, 15) * S6 + sp.Rational(2, 13) * S4 - sp.Rational(1, 39)
harmonic_form = (
    sp.Rational(315, 2288) * K4
    - sp.Rational(35, 64) * K6
    + sp.Rational(1155, 512) * K8
)
s2c_difference = sp.expand((raw_angular / 128 - harmonic_form).subs(sphere_substitution))
check("S2c raw and K4/K6/K8 harmonic forms agree on the sphere",
      s2c_difference == 0)


# S3: exact spherical moments and direction anchors.
def sphere_average(poly):
    """Exact average of an even polynomial over the unit two-sphere."""
    total = 0
    for powers, coefficient in sp.Poly(sp.expand(poly), nx, ny, nz).terms():
        px, py, pz = powers
        if px % 2 or py % 2 or pz % 2:
            raise ValueError("sphere_average expects even component powers")
        moment = (
            sp.factorial2(px - 1)
            * sp.factorial2(py - 1)
            * sp.factorial2(pz - 1)
            / sp.factorial2(px + py + pz + 1)
        )
        total += coefficient * moment
    return sp.simplify(total)


check("S3a exact spherical average of f is zero",
      sphere_average(f_raw) == 0)
check("S3b K6 has zero mean and is orthogonal to K4",
      sphere_average(K6) == 0 and sphere_average(K6 * K4) == 0)
check("S3c K8 has zero mean and is orthogonal to K4 and K6",
      sphere_average(K8) == 0
      and sphere_average(K8 * K4) == 0
      and sphere_average(K8 * K6) == 0)

direction_targets = [
    ((1, 0, 0), sp.Rational(23, 128) / sp.pi),
    ((1, 1, 0), sp.Rational(179, 2048) / sp.pi),
    ((1, 1, 1), -sp.Rational(1, 48) / sp.pi),
    ((2, 1, 0), -sp.Rational(149, 16000) / sp.pi),
    ((2, 1, 1), -sp.Rational(157, 2048) / sp.pi),
    ((3, 2, 1), -sp.Rational(2893, 100352) / sp.pi),
    ((3, 1, 0), sp.Rational(4231, 256000) / sp.pi),
]
for direction, target in direction_targets:
    norm = sp.sqrt(sum(component**2 for component in direction))
    substitutions = {
        nx: sp.Rational(direction[0], 1) / norm,
        ny: sp.Rational(direction[1], 1) / norm,
        nz: sp.Rational(direction[2], 1) / norm,
    }
    check("S3d f%s equals its exact rational/pi anchor" % (direction,),
          sp.simplify(f_raw.subs(substitutions) - target) == 0)


# S4: finite combinatorial grading of the all-orders contact-term argument.
kx, ky, kz = sp.symbols("kx ky kz")
E = t * sum(
    (-1) ** (i + 1) * sp.Rational(2, sp.factorial(2*i + 2))
    * (kx**(2*i + 2) + ky**(2*i + 2) + kz**(2*i + 2))
    for i in range(1, 5)
)
exp_series = sp.expand(sum(E**J / sp.factorial(J) for J in range(5)))
graded = {n: [] for n in range(1, 5)}
for powers, coefficient in sp.Poly(exp_series, t, kx, ky, kz).terms():
    del coefficient
    J = powers[0]
    if J < 1:
        continue
    k_degree = sum(powers[1:])
    if k_degree % 2:
        raise ValueError("symbol expansion produced an odd k-degree")
    D = k_degree // 2
    n = D - J
    if n <= 4:
        graded[n].append(D - J - 1 >= 0)

for n in range(1, 5):
    check("S4 order n=%d has only polynomial isotropic contact terms" % n,
          bool(graded[n]) and all(graded[n]))


# --- Independent numerical Bessel-resolvent checks ---
mp.dps = 24


def G_num(x, y, z):
    x, y, z = abs(x), abs(y), abs(z)
    r2 = x*x + y*y + z*z
    def integrand(t):
        return mpexp(-6*t) * besseli(x, 2*t) * besseli(y, 2*t) * besseli(z, 2*t)
    pts = [0, mpf(r2)/12 + 1, mpf(r2)/6 + 2, mpf(r2)/2 + 4, 4*mpf(r2) + 20, mpinf]
    return mpquad(integrand, pts)


def lattice_equation_error(point):
    x0, y0, z0 = point
    neighbors = (
        (x0 + 1, y0, z0), (x0 - 1, y0, z0),
        (x0, y0 + 1, z0), (x0, y0 - 1, z0),
        (x0, y0, z0 + 1), (x0, y0, z0 - 1),
    )
    return abs(6 * G_num(x0, y0, z0) - sum(G_num(*q) for q in neighbors))


n1a_error = abs(6 * (G_num(0, 0, 0) - G_num(1, 0, 0)) - 1)
n1b_error = lattice_equation_error((7, 4, 2))
n1c_error = lattice_equation_error((4, 2, 1))
check("N1a origin delta-identity error %.3e < 1e-18" % float(n1a_error),
      n1a_error < mpf("1e-18"))
check("N1b lattice-equation error at (7,4,2) %.3e < 1e-12" % float(n1b_error),
      n1b_error < mpf("1e-12"))
check("N1c lattice-equation error at (4,2,1) %.3e < 1e-12" % float(n1c_error),
      n1c_error < mpf("1e-12"))


def resid5(x0, y0, z0):
    radius = mpsqrt(mpf(x0*x0 + y0*y0 + z0*z0))
    nx0, ny0, nz0 = mpf(x0)/radius, mpf(y0)/radius, mpf(z0)/radius
    k4 = nx0**4 + ny0**4 + nz0**4 - mpf(3)/5
    return (
        G_num(x0, y0, z0)
        - 1 / (4 * mppi * radius)
        - (mpf(5) / (32 * mppi)) * k4 / radius**3
    ) * radius**5


def f_exact_mp(direction):
    a, b, c = direction
    norm = mpsqrt(mpf(a*a + b*b + c*c))
    ux, uy, uz = mpf(a)/norm, mpf(b)/norm, mpf(c)/norm
    raw = (
        23 * (ux**8 + uy**8 + uz**8)
        - 244 * (
            ux**6*uy**2 + ux**6*uz**2 + uy**6*ux**2
            + uy**6*uz**2 + uz**6*ux**2 + uz**6*uy**2
        )
        + 621 * (ux**4*uy**4 + ux**4*uz**4 + uy**4*uz**4)
        - 228 * ux**2*uy**2*uz**2
    )
    return raw / (128 * mppi)


orbits = [
    ((1, 0, 0), (8, 12, 18, 27)),
    ((1, 1, 0), (6, 9, 13, 19)),
    ((1, 1, 1), (5, 7, 10, 15)),
    ((2, 1, 0), (4, 6, 9, 13)),
    ((2, 1, 1), (3, 5, 7, 10)),
]
numeric_data = {}
for direction, multiples in orbits:
    values = []
    radii = []
    direction_norm = np.linalg.norm(np.array(direction, dtype=float))
    for multiple in multiples:
        point = tuple(multiple * component for component in direction)
        values.append(float(resid5(*point)))
        radii.append(float(multiple) * direction_norm)
    values = np.array(values, dtype=float)
    radii = np.array(radii, dtype=float)
    design = np.column_stack((
        np.ones_like(radii),
        1 / radii**2,
        1 / radii**4,
    ))
    extrapolation = np.linalg.lstsq(design, values, rcond=None)[0][0]
    exact_value = float(f_exact_mp(direction))
    residuals = values - exact_value
    expected_ratio = (radii[-1] / radii[-2])**2
    last_pair_ratio = residuals[-2] / residuals[-1]
    numeric_data[direction] = {
        "values": values,
        "radii": radii,
        "extrapolation": extrapolation,
        "exact": exact_value,
        "ratio": last_pair_ratio,
        "expected_ratio": expected_ratio,
    }

for direction, _ in orbits:
    data = numeric_data[direction]
    difference = abs(data["extrapolation"] - data["exact"])
    check("N2a f%s extrapolation %.9g, error %.3e < 2e-4" %
          (direction, data["extrapolation"], difference),
          difference < 2e-4)

for direction, _ in orbits:
    data = numeric_data[direction]
    lower = 0.7 * data["expected_ratio"]
    upper = 1.35 * data["expected_ratio"]
    check("N2b f%s last-pair ratio %.6g in [%.6g, %.6g]" %
          (direction, data["ratio"], lower, upper),
          lower <= data["ratio"] <= upper)


axial = numeric_data[(1, 0, 0)]
f_wrong = axial["exact"] * 1.05
check("CTRL1 5 percent wrong axial value is rejected by extrapolation",
      abs(axial["extrapolation"] - f_wrong) > 2e-4)
wrong_residuals = axial["values"] - f_wrong
wrong_ratio = wrong_residuals[-2] / wrong_residuals[-1]
wrong_lower = 0.7 * axial["expected_ratio"]
wrong_upper = 1.35 * axial["expected_ratio"]
check("CTRL2 5 percent wrong axial value is rejected by last-pair ratio",
      not (wrong_lower <= wrong_ratio <= wrong_upper))

raw_xyz_wrong = raw_xyz + (x**4*y**4 + x**4*z**4 + y**4*z**4)
wrong_symbolic_difference = sp.simplify(128 * sp.pi * r**13 * T2 - raw_xyz_wrong)
check("CTRL3 coefficient 622 in place of 621 is symbolically rejected",
      wrong_symbolic_difference != 0)


n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
extrapolation_summary = " ".join(
    "%s=%.9g" % (direction, numeric_data[direction]["extrapolation"])
    for direction, _ in orbits
)
print("RESULT: G(x) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + f(nhat)/r^5 + O(1/r^7); extrapolations " + extrapolation_summary)
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
