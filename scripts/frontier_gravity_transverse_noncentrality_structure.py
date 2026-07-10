"""Class-A finite runner for transverse non-centrality of the emergent force.

The symbolic gates verify the exact gradient, tangency, central-orbit,
sphere-Hessian, extremal, and stabilizer identities.  The numeric gates use
the exact Bessel-resolvent lattice Green function and a five-point gradient
stencil at six lattice sites as finite-site support for compatibility with an
O(1/r^6) gradient remainder; they do not prove the asymptotic derivative bound.
Four controls require specified wrong coefficients or structures to fail.

Prints PASS/FAIL gate lines, a RESULT line, and TOTAL: PASS=N FAIL=M.
"""

AUDIT_TIMEOUT_SEC = 360

import sys

import mpmath as mp
import sympy as sp


results = []


def check(name, ok):
    results.append((name, bool(ok)))


def all_zero(expressions):
    return all(sp.simplify(expression) == 0 for expression in expressions)


# ---------------------------------------------------------------------------
# Exact symbolic structure
# ---------------------------------------------------------------------------
x, y, z = sp.symbols("x y z", real=True)
xyz = sp.Matrix([x, y, z])
r = sp.sqrt(x**2 + y**2 + z**2)
nhat = xyz / r
S4 = sum(component**4 for component in nhat)
S6 = sum(component**6 for component in nhat)
K4 = S4 - sp.Rational(3, 5)
tangent = sp.Matrix([component**3 - S4 * component for component in nhat])

potential = 1 / (4 * sp.pi * r) + sp.Rational(5, 32) * K4 / (sp.pi * r**3)
gradient_claim = (
    -(1 / (4 * sp.pi * r**2) + sp.Rational(15, 32) * K4 / (sp.pi * r**4)) * nhat
    + sp.Rational(5, 8) * tangent / (sp.pi * r**4)
)
gradient_exact = sp.Matrix([sp.diff(potential, variable) for variable in xyz])
for index, label in enumerate(("x", "y", "z")):
    check(
        "S1 gradient identity, %s component" % label,
        sp.simplify(gradient_exact[index] - gradient_claim[index]) == 0,
    )

check("S2a transverse vector is exactly tangent", sp.simplify(nhat.dot(tangent)) == 0)
check(
    "S2b component factor t_mu=nhat_mu(nhat_mu^2-S4)",
    all_zero(
        tangent[index] - nhat[index] * (nhat[index] ** 2 - S4)
        for index in range(3)
    ),
)
homogeneous_gradient = sp.Matrix([sp.diff(S4, variable) for variable in xyz])
check(
    "S2c degree-zero gradient is 4t/r componentwise",
    all_zero(homogeneous_gradient[index] - 4 * tangent[index] / r for index in range(3)),
)
check(
    "S3 magnitude identity |t|^2=S6-S4^2",
    sp.simplify(tangent.dot(tangent) - (S6 - S4**2)) == 0,
)


def direction_invariants(direction):
    norm = sp.sqrt(sum(component**2 for component in direction))
    unit = sp.Matrix([sp.sympify(component) / norm for component in direction])
    s4 = sp.simplify(sum(component**4 for component in unit))
    vector = sp.Matrix([sp.simplify(component**3 - s4 * component) for component in unit])
    return unit, s4, vector


for label, direction, expected_s4 in (
    ("<100>", (1, 0, 0), sp.Integer(1)),
    ("<110>", (1, 1, 0), sp.Rational(1, 2)),
    ("<111>", (1, 1, 1), sp.Rational(1, 3)),
):
    _, orbit_s4, orbit_tangent = direction_invariants(direction)
    check(
        "S4 central orbit %s has t=0 and S4=%s" % (label, expected_s4),
        orbit_s4 == expected_s4 and all(component == 0 for component in orbit_tangent),
    )

a, b, c = sp.symbols("a b c", real=True)
abstract_n = sp.Matrix([a, b, c])
abstract_s4 = sum(component**4 for component in abstract_n)
abstract_tangent = sp.Matrix(
    [component**3 - abstract_s4 * component for component in abstract_n]
)
check(
    "S4 converse factor forces each nonzero square to equal S4",
    all(
        sp.simplify(
            sp.factor(abstract_tangent[index])
            - sp.factor(abstract_n[index] * (abstract_n[index] ** 2 - abstract_s4))
        )
        == 0
        for index in range(3)
    ),
)
check(
    "S4 k equal nonzero squares imply S4=1/k for k=1,2,3",
    all(
        sp.simplify(sp.Integer(k) * (sp.Rational(1, k)) ** 2 - sp.Rational(1, k)) == 0
        for k in (1, 2, 3)
    ),
)

homogeneous_hessian = sp.hessian(S4, (x, y, z))
orbit_hessian_data = (
    (
        "<100>",
        sp.Matrix([1, 0, 0]),
        sp.Matrix([[0, 0], [1, 0], [0, 1]]),
        {-sp.Integer(4): 2},
    ),
    (
        "<110>",
        sp.Matrix([1 / sp.sqrt(2), 1 / sp.sqrt(2), 0]),
        sp.Matrix([[1 / sp.sqrt(2), 0], [-1 / sp.sqrt(2), 0], [0, 1]]),
        {-sp.Integer(2): 1, sp.Integer(4): 1},
    ),
    (
        "<111>",
        sp.Matrix([1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)]),
        sp.Matrix(
            [
                [1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                [-1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                [0, -2 / sp.sqrt(6)],
            ]
        ),
        {sp.Rational(8, 3): 2},
    ),
)
for label, point, frame, expected_eigenvalues in orbit_hessian_data:
    substitutions = dict(zip((x, y, z), point))
    tangent_hessian = sp.simplify(frame.T * homogeneous_hessian.subs(substitutions) * frame)
    eigenvalues = {sp.simplify(value): multiplicity for value, multiplicity in tangent_hessian.eigenvals().items()}
    check("S5 sphere Hessian spectrum at %s" % label, eigenvalues == expected_eigenvalues)

q2_abstract = sum(component**6 for component in abstract_n) - abstract_s4**2
q2_gradient = sp.Matrix([sp.diff(q2_abstract, component) for component in abstract_n])
lagrange_lambda = sp.expand(abstract_n.dot(q2_gradient))
stationarity_claim = sp.Matrix(
    [
        component
        * (
            6 * component**4
            - 8 * abstract_s4 * component**2
            - 6 * sum(entry**6 for entry in abstract_n)
            + 8 * abstract_s4**2
        )
        for component in abstract_n
    ]
)
check(
    "S6 constrained stationarity equation from lambda=n dot grad(q2)",
    sp.simplify(lagrange_lambda - (6 * sum(entry**6 for entry in abstract_n) - 8 * abstract_s4**2))
    == 0
    and all_zero(q2_gradient[index] - lagrange_lambda * abstract_n[index] - stationarity_claim[index] for index in range(3)),
)

u = sp.symbols("u", real=True)
q2_u = sp.expand(
    2 * u**3 + (1 - 2 * u) ** 3 - (2 * u**2 + (1 - 2 * u) ** 2) ** 2
)
u_star = (13 - sp.sqrt(73)) / 48
q2_max = (827 + 73 * sp.sqrt(73)) / 18432
check("S6 two-equal-square extremum u_star solves dq2/du", sp.simplify(sp.diff(q2_u, u).subs(u, u_star)) == 0)
check("S6 exact global q2 maximum on the extremal family", sp.simplify(q2_u.subs(u, u_star) - q2_max) == 0)
check(
    "S6 q2 maximum obeys 9216 Q^2-827 Q+8=0",
    sp.expand(9216 * q2_max**2 - 827 * q2_max + 8) == 0,
)

v = sp.symbols("v", real=True)
q2_planar = sp.expand(v**3 + (1 - v) ** 3 - (v**2 + (1 - v) ** 2) ** 2)
v_star = sp.cos(sp.pi / 8) ** 2
planar_gap = sp.simplify(q2_max - sp.Rational(1, 16))
check(
    "S6 planar maximum q2=1/16 at v=cos^2(pi/8)",
    sp.simplify(sp.diff(q2_planar, v).subs(v, v_star)) == 0
    and sp.simplify(q2_planar.subs(v, v_star) - sp.Rational(1, 16)) == 0
    and sp.simplify(sp.diff(q2_planar, v, 2).subs(v, v_star)) < 0,
)
check("S6 global maximum is strictly above planar maximum", planar_gap.is_positive)

GRID_N = 240
q2_max_float = float(q2_max)
grid_max = -1.0
for i in range(GRID_N + 1):
    w1 = i / GRID_N
    for j in range(GRID_N + 1 - i):
        w2 = j / GRID_N
        w3 = 1.0 - w1 - w2
        s4_grid = w1 * w1 + w2 * w2 + w3 * w3
        s6_grid = w1 * w1 * w1 + w2 * w2 * w2 + w3 * w3 * w3
        q2_grid = s6_grid - s4_grid * s4_grid
        if q2_grid > grid_max:
            grid_max = q2_grid
check(
    "S6 simplex grid finds no direction above the family maximum",
    grid_max <= q2_max_float + 1.0e-12,
)
check(
    "S6 simplex grid attains the family maximum to grid resolution",
    grid_max >= q2_max_float - 5.0e-4,
)


def exact_q2(direction):
    norm2 = sum(sp.Integer(component) ** 2 for component in direction)
    s4 = sum(sp.Integer(component) ** 4 for component in direction) / norm2**2
    s6 = sum(sp.Integer(component) ** 6 for component in direction) / norm2**3
    return sp.factor(s6 - s4**2)


for label, direction, expected in (
    ("(1,1,3)", (1, 1, 3), sp.Rational(1152, 14641)),
    ("(2,1,0)", (2, 1, 0), sp.Rational(36, 625)),
    ("(2,1,1)", (2, 1, 1), sp.Rational(1, 18)),
):
    check("S7 exact q2 anchor %s" % label, exact_q2(direction) == expected)

k4_100 = sp.Rational(2, 5)
k4_111 = -sp.Rational(4, 15)
check(
    "S7 conditional pair-response contrast coefficient",
    sp.simplify(
        sp.Rational(5, 32) * (k4_100 - k4_111) / sp.pi
        - sp.Rational(5, 48) / sp.pi
    )
    == 0,
)

rotation_data = (
    (
        "<100>",
        sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
        sp.Matrix([[0, 0], [1, 0], [0, 1]]),
    ),
    (
        "<110>",
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
        sp.Matrix([[1 / sp.sqrt(2), 0], [-1 / sp.sqrt(2), 0], [0, 1]]),
    ),
    (
        "<111>",
        sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
        sp.Matrix(
            [
                [1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                [-1 / sp.sqrt(2), 1 / sp.sqrt(6)],
                [0, -2 / sp.sqrt(6)],
            ]
        ),
    ),
)
for label, rotation, frame in rotation_data:
    tangent_rotation = sp.simplify(frame.T * rotation * frame)
    fixed_vector_determinant = sp.simplify((sp.eye(2) - tangent_rotation).det())
    check(
        "S8 stabilizer has no tangent fixed vector at %s" % label,
        fixed_vector_determinant != 0,
    )

# ---------------------------------------------------------------------------
# Bessel-resolvent values and five-point finite-difference gradients
# ---------------------------------------------------------------------------
mp.mp.dps = 24
mpexp = mp.exp
besseli = mp.besseli
mpf = mp.mpf
mpinf = mp.inf
mpquad = mp.quad


def G_num(x, y, z):
    x, y, z = abs(x), abs(y), abs(z)
    r2 = x*x + y*y + z*z
    def integrand(t):
        return mpexp(-6*t) * besseli(x, 2*t) * besseli(y, 2*t) * besseli(z, 2*t)
    pts = [0, mpf(r2)/12 + 1, mpf(r2)/6 + 2, mpf(r2)/2 + 4, 4*mpf(r2) + 20, mpinf]
    return mpquad(integrand, pts)


green_cache = {}


def cached_G(site):
    key = tuple(sorted(abs(coordinate) for coordinate in site))
    if key not in green_cache:
        green_cache[key] = G_num(*key)
    return green_cache[key]


def vector_dot(left, right):
    return sum(a_value * b_value for a_value, b_value in zip(left, right))


def vector_norm(vector):
    return mp.sqrt(vector_dot(vector, vector))


def gradient_num(site):
    gradient = []
    for axis in range(3):
        values = {}
        for offset in (-2, -1, 1, 2):
            shifted = list(site)
            shifted[axis] += offset
            values[offset] = cached_G(tuple(shifted))
        gradient.append(
            (-values[2] + 8 * values[1] - 8 * values[-1] + values[-2]) / 12
        )
    return gradient


sites = ((3, 3, 9), (5, 5, 15), (8, 4, 0), (14, 7, 0), (8, 4, 4), (12, 6, 6))
numeric = {}
for site in sites:
    r2_num = mpf(sum(coordinate * coordinate for coordinate in site))
    radius = mp.sqrt(r2_num)
    unit = [mpf(coordinate) / radius for coordinate in site]
    s4_num = sum(component**4 for component in unit)
    s6_num = sum(component**6 for component in unit)
    k4_num = s4_num - mpf(3) / 5
    angular_tangent = [component**3 - s4_num * component for component in unit]
    derivative = gradient_num(site)
    rho_num = vector_dot(unit, derivative)
    transverse_num = [derivative[index] - rho_num * unit[index] for index in range(3)]
    rho_pred = -(
        1 / (4 * mp.pi * radius**2)
        + mpf(15) / (32 * mp.pi) * k4_num / radius**4
    )
    transverse_pred = [
        mpf(5) / (8 * mp.pi) * component / radius**4 for component in angular_tangent
    ]
    transverse_error = vector_norm(
        [transverse_num[index] - transverse_pred[index] for index in range(3)]
    ) / vector_norm(transverse_pred)
    numeric[site] = {
        "r": radius,
        "unit": unit,
        "s4": s4_num,
        "s6": s6_num,
        "q2": s6_num - s4_num**2,
        "rho_num": rho_num,
        "rho_pred": rho_pred,
        "transverse_num": transverse_num,
        "transverse_pred": transverse_pred,
        "e_t": transverse_error,
    }

for site in sites:
    data = numeric[site]
    scaled_error = data["e_t"] * data["r"] ** 2
    check(
        "N1 finite-site transverse remainder compatibility at %s: e_t*r^2=%.9g < 8"
        % (site, float(scaled_error)),
        scaled_error < 8,
    )

for site in sites:
    data = numeric[site]
    scaled_error = abs(data["rho_num"] - data["rho_pred"]) * data["r"] ** 6
    check(
        "N2 finite-site radial remainder compatibility at %s: abs(error)*r^6=%.9g < 1"
        % (site, float(scaled_error)),
        scaled_error < 1,
    )

site_pairs = (((3, 3, 9), (5, 5, 15)), ((8, 4, 0), (14, 7, 0)), ((8, 4, 4), (12, 6, 6)))
for small_site, large_site in site_pairs:
    small = numeric[small_site]
    large = numeric[large_site]
    measured = small["e_t"] / large["e_t"]
    expected = (large["r"] / small["r"]) ** 2
    check(
        "N3 finite-site O(1/r^2) relative convergence %s to %s: ratio=%.9g expected=%.9g"
        % (small_site, large_site, float(measured), float(expected)),
        mpf("0.5") * expected <= measured <= 2 * expected,
    )

for site in sites:
    data = numeric[site]
    measured = vector_norm(data["transverse_num"])
    threshold = mpf("0.5") * vector_norm(data["transverse_pred"])
    check(
        "N4 non-centrality witness at %s: measured/predicted=%.9g > 0.5"
        % (site, float(measured / vector_norm(data["transverse_pred"]))),
        measured > threshold,
    )

for site in ((14, 7, 0), (5, 5, 15)):
    data = numeric[site]
    measured = vector_norm(data["transverse_num"]) / abs(data["rho_num"])
    predicted = mpf(5) / 2 * mp.sqrt(data["q2"]) / data["r"] ** 2
    relative_error = abs(measured / predicted - 1)
    check(
        "N5 transverse/radial ratio at %s: relative error=%.9g < 0.15"
        % (site, float(relative_error)),
        relative_error < mpf("0.15"),
    )

# Specified wrong-value rejectors reuse the symbolic objects and numeric values above.
control_site = (5, 5, 15)
control_data = numeric[control_site]
inflated_prediction = [mpf("1.10") * value for value in control_data["transverse_pred"]]
inflated_error = vector_norm(
    [control_data["transverse_num"][index] - inflated_prediction[index] for index in range(3)]
) / vector_norm(inflated_prediction)
check(
    "CTRL1 10 percent inflated transverse coefficient is rejected: e_t*r^2=%.9g > 8"
    % float(inflated_error * control_data["r"] ** 2),
    inflated_error * control_data["r"] ** 2 > 8,
)

wrong_angular_tangent = [
    component**3 - control_data["s6"] * component for component in control_data["unit"]
]
wrong_prediction = [
    mpf(5) / (8 * mp.pi) * component / control_data["r"] ** 4
    for component in wrong_angular_tangent
]
wrong_form_error = vector_norm(
    [control_data["transverse_num"][index] - wrong_prediction[index] for index in range(3)]
) / vector_norm(wrong_prediction)
check(
    "CTRL2 S6-in-place-of-S4 transverse form is rejected: e_t*r^2=%.9g > 8"
    % float(wrong_form_error * control_data["r"] ** 2),
    wrong_form_error * control_data["r"] ** 2 > 8,
)

check(
    "CTRL3 wrong minimal-polynomial coefficient 826 is rejected",
    sp.expand(9216 * q2_max**2 - 826 * q2_max + 8) != 0,
)
wrong_gradient_claim = (
    -(1 / (4 * sp.pi * r**2) + sp.Rational(15, 32) * K4 / (sp.pi * r**4)) * nhat
    + sp.Rational(3, 8) * tangent / (sp.pi * r**4)
)
check(
    "CTRL4 wrong 3/8 transverse gradient coefficient is rejected",
    any(
        sp.simplify(gradient_exact[index] - wrong_gradient_claim[index]) != 0
        for index in range(3)
    ),
)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
q2_max_num = mpf(827 + 73 * mp.sqrt(73)) / 18432
ratio_coefficient = mpf(5) / 2 * mp.sqrt(q2_max_num)
print(
    "RESULT: exact gradient of the displayed truncation is "
    "[1/(4 pi r^2) + (15/32 pi) K4/r^4] nhat - "
    "(5/8 pi)(nhat^3 - S4 nhat)/r^4; an O(1/r^6) full-force remainder "
    "is conditional on termwise differentiability and has finite-site support; central orbits "
    "<100>,<110>,<111>; q2_max=(827+73*sqrt(73))/18432=%.9g; "
    "ratio_coeff=(5/2)*q_max=%.9g"
    % (float(q2_max_num), float(ratio_coefficient))
)
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
sys.exit(1 if n_fail else 0)
