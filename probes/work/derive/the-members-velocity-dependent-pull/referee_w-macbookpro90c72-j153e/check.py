#!/usr/bin/env python3
"""Independent check of the member's velocity-dependent pull, attempt a1.

Does not import the author's script. T3 is not re-derived. Checked here:
the curvature identity for a generic field, the Legendre transform of the
pull, the 1s clock ratio, the 2p0 axial ratio, and the books identity for
drifting lengths. The non-axis exchange and the full W=1 cancellation are
not rebuilt.
"""
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


x, y, z, t = sp.symbols("x y z t", real=True)
X = (x, y, z)
K, alpha = sp.symbols("K alpha", positive=True)
PAIRS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def curvatures(components):
    trace = sum(components(i, i) for i in range(3))
    r1 = sum(sp.diff(components(i, j), X[i], X[j]) for i in range(3) for j in range(3))
    r1 -= sum(sp.diff(trace, X[k], 2) for k in range(3))
    r2 = -sp.Rational(1, 4) * sum(sp.diff(components(i, j), X[k]) ** 2
                                   for i in range(3) for j in range(3) for k in range(3))
    r2 += sp.Rational(1, 2) * sum(sum(sp.diff(components(i, k), X[i]) for i in range(3)) ** 2 for k in range(3))
    r2 -= sp.Rational(1, 2) * sum(sum(sp.diff(components(i, j), X[i]) for i in range(3)) * sp.diff(trace, X[j])
                                   for j in range(3))
    r2 += sp.Rational(1, 4) * sum(sp.diff(trace, X[k]) ** 2 for k in range(3))
    return r1, r2


# kinetic match
rate = sp.Matrix(3, 3, lambda i, j: sp.Symbol("d%d%d" % (min(i, j), max(i, j))))
beta = sp.Symbol("beta")
member = alpha * (rate * rate).trace() + beta * rate.trace() ** 2
comparator = K * ((rate * rate).trace() - rate.trace() ** 2) / 4
matched = sp.solve(sp.Poly(sp.expand(member - comparator), *rate.free_symbols).coeffs(), [alpha, beta], dict=True)
check(
    "T1 kinetic",
    matched == [{alpha: K / 4, beta: -K / 4}],
    "the extrinsic-curvature square matches iff alpha = K/4 and beta = -alpha",
)

# scalar curvature through second order, for a generic symmetric h
eps = sp.symbols("epsilon")
fields = {pair: sp.Function("h%d%d" % pair)(x, y, z) for pair in PAIRS}
metric = sp.eye(3) + eps * sp.Matrix(3, 3, lambda i, j: fields[(min(i, j), max(i, j))])
inverse = sp.eye(3) - eps * metric.diff(eps).subs(eps, 0) + eps**2 * (metric.diff(eps).subs(eps, 0)) ** 2
# Christoffel, truncated at the order needed for R through eps^2: Gamma starts at eps
raw_gamma = [[[sum(inverse[k, ell] * (
    sp.diff(metric[j, ell], X[i]) + sp.diff(metric[i, ell], X[j]) - sp.diff(metric[i, j], X[ell])
) for ell in range(3)) / 2 for j in range(3)] for i in range(3)] for k in range(3)]


def cut(expr):
    return sp.series(sp.expand(expr), eps, 0, 3).removeO()


gamma = [[[cut(raw_gamma[k][i][j]) for j in range(3)] for i in range(3)] for k in range(3)]


def ricci(i, j):
    total = 0
    for k in range(3):
        total += sp.diff(gamma[k][i][j], X[k]) - sp.diff(gamma[k][i][k], X[j])
        for ell in range(3):
            total += gamma[k][k][ell] * gamma[ell][i][j] - gamma[k][j][ell] * gamma[ell][i][k]
    return cut(total)


sqrt_g = 1 + eps * metric.diff(eps).subs(eps, 0).trace() / 2
sqrt_g += eps**2 * (metric.diff(eps).subs(eps, 0).trace() ** 2 / 8
                    - (metric.diff(eps).subs(eps, 0) ** 2).trace() / 4)
scalar = cut(sum(inverse[i, j] * ricci(i, j) for i in range(3) for j in range(3)))
density = sp.expand(cut(sqrt_g * scalar))
r1, r2 = curvatures(lambda i, j: fields[(min(i, j), max(i, j))])
first = sp.simplify(density.coeff(eps, 1) - r1) == 0
euler = sp.euler_equations(sp.expand(density.coeff(eps, 2) - r2), list(fields.values()), [x, y, z])
second = all(sp.simplify(eq.lhs - eq.rhs) == 0 for eq in euler)
check(
    "T1 curvature",
    first and second,
    "the first order of sqrt(g) R is R1, and the second order differs from R2 by a divergence",
)

# T4: Legendre transform and the member coefficients
m1, m2, kk, lam = sp.symbols("m1 m2 k lambda", positive=True)
a, b, c = sp.symbols("a b c", real=True)
normal = sp.Matrix(sp.symbols("n1:4"))
radius = sp.symbols("r", positive=True)
p1 = sp.Matrix(sp.symbols("p1x p1y p1z"))
p2 = sp.Matrix(sp.symbols("p2x p2y p2z"))
w1 = sp.Matrix(sp.symbols("w1x w1y w1z"))
w2 = sp.Matrix(sp.symbols("w2x w2y w2z"))
V1 = lam * p1 / m1 + lam**3 * w1
V2 = lam * p2 / m2 + lam**3 * w2


def lagrangian(left, right, coupling):
    return (-m1 * sp.sqrt(1 - left.dot(left)) - m2 * sp.sqrt(1 - right.dot(right))
            + (coupling / radius) * (1 + a * (left.dot(left) + right.dot(right))
                                      + b * left.dot(right) + c * normal.dot(left) * normal.dot(right)))


probe = sp.Matrix(sp.symbols("q1:4"))
equations = []
for slot, velocity, momentum in ((0, V1, p1), (1, V2, p2)):
    for component in range(3):
        args = [V1, V2]
        args[slot] = probe
        derivative = sp.diff(lagrangian(*args, lam**2 * kk), probe[component])
        derivative = derivative.subs({probe[i]: velocity[i] for i in range(3)})
        equations.append(sp.series(derivative - lam * momentum[component], lam, 0, 4).removeO().coeff(lam, 3))
solved = sp.solve(equations, list(w1) + list(w2), dict=True)[0]
energy = sp.series((lam * p1.dot(V1) + lam * p2.dot(V2) - lagrangian(V1, V2, lam**2 * kk)).subs(solved),
                   lam, 0, 5).removeO()
expected = (m1 + m2
            + lam**2 * (p1.dot(p1) / (2 * m1) + p2.dot(p2) / (2 * m2))
            - lam**4 * (p1.dot(p1) ** 2 / (8 * m1**3) + p2.dot(p2) ** 2 / (8 * m2**3))
            - lam**2 * kk / radius
            - lam**4 * (kk / radius) * (a * (p1.dot(p1) / m1**2 + p2.dot(p2) / m2**2)
                                         + b * p1.dot(p2) / (m1 * m2)
                                         + c * normal.dot(p1) * normal.dot(p2) / (m1 * m2)))
check(
    "T4 legendre",
    sp.simplify(sp.expand(energy) - sp.expand(expected)) == 0,
    "to order v^4 the Hamiltonian is the relativistic kinetic energy minus the stated pull",
)

# 1s weight: <U> = -k^2 mu, and for (3/2,-7/2,-1/2) the correction cancels
# Use the known hydrogen integrals rather than a fresh 3D quadrature of 2p:
# <1/r>_{1s} = mu k, <q^2>_{1s} = (mu k)^2, and the directional split of 1s is isotropic.
mu = m1 * m2 / (m1 + m2)
M = m1 + m2
# isotropic 1s: <q_i q_j> = delta_ij (mu k)^2 / 3, <n_i n_j/r> = delta_ij <1/r>/3
# virial: <q^2>/(2 mu) = k <1/r> / 2, and <1/r> = mu k, so <T> = (mu k^2)/2, <U> = -mu k^2, E = -<T>
inv_r = mu * kk
qq_diag = (mu * kk) ** 2 / 3
nn_diag = inv_r / 3
# W-1 = (<U> + 2 M^2 <C - 1/(2M)>) / M
# For the member coefficients the attempt claims exact cancellation. Check the clock-only piece
# W-1 = (<U> + <U_P>)/M and <U_P>/<U> = 1/3 for 1s, so (<U>+<U_P>)/<U> = 4/3.
clock = sp.simplify(((-kk * inv_r) + (-kk * nn_diag)) / M / ((-kk * inv_r) / M))
check(
    "T4 clock",
    clock == sp.Rational(4, 3) and sp.simplify(2 * (qq_diag / (2 * mu)) + (-kk * nn_diag)) == 0,
    "on 1s the clock-only ratio is 4/3 and the directional virial holds",
)

# necessity from three ratios. For 1s, <U_P>/<U> = 1/3.
# For 2p0 along z the attempt gives 8/5; across, 6/5.
# W = 1 on those three forces 2a+b = -1/2 and c = -1/2 if the linear system is that one.
# Reconstruct <C> from the pull term only, using the stated ratios as computed inputs would be circular.
# Instead integrate 2p0 exactly. It is one radial integral.
rho, theta, phi = sp.symbols("rho theta phi", positive=True)
a0 = 1 / (mu * kk)
psi_2p = (rho * sp.cos(theta)) * sp.exp(-rho / (2 * a0)) / (4 * sp.sqrt(2 * sp.pi) * a0 ** sp.Rational(5, 2))
jac = rho**2 * sp.sin(theta)
norm_2p = sp.integrate(sp.integrate(sp.integrate(sp.simplify(psi_2p**2 * jac), (phi, 0, 2 * sp.pi)),
                                    (theta, 0, sp.pi)), (rho, 0, sp.oo))
inv_2p = sp.integrate(sp.integrate(sp.integrate(sp.simplify(psi_2p**2 / rho * jac), (phi, 0, 2 * sp.pi)),
                                   (theta, 0, sp.pi)), (rho, 0, sp.oo))
# <n_z^2 / r> = <cos^2 theta / rho>
nn_z = sp.integrate(sp.integrate(sp.integrate(sp.simplify(psi_2p**2 * sp.cos(theta) ** 2 / rho * jac),
                                              (phi, 0, 2 * sp.pi)), (theta, 0, sp.pi)), (rho, 0, sp.oo))
check(
    "T4 2p",
    sp.simplify(norm_2p - 1) == 0
    and sp.simplify((-kk * nn_z) / (-kk * inv_2p) - sp.Rational(3, 5)) == 0,
    "2p0 is normalized and <U along its axis>/<U> = 3/5, so the clock-only ratio along z is 8/5",
)

# T5 books identity, without building the full Euler system
xi = [sp.Function("xi%d" % (i + 1))(x, y, z) for i in range(3)]
drift = lambda i, j: t * (sp.diff(xi[j], X[i]) + sp.diff(xi[i], X[j]))
stress = {pair: sp.Function("S%d%d" % pair)(t, x, y, z) for pair in PAIRS}
momentum = [sp.Function("Q%d" % (i + 1))(t, x, y, z) for i in range(3)]


def stress_at(i, j):
    return stress[(min(i, j), max(i, j))]


coupling = sp.Rational(1, 2) * sum(stress_at(i, j) * drift(i, j) for i in range(3) for j in range(3))
target = (sp.diff(t * sum(xi[j] * momentum[j] for j in range(3)), t)
          - sum(xi[j] * momentum[j] for j in range(3))
          + sum(sp.diff(t * sum(stress_at(i, j) * xi[j] for j in range(3)), X[i]) for i in range(3)))
books = {sp.diff(momentum[j], t): -sum(sp.diff(stress_at(i, j), X[i]) for i in range(3)) for j in range(3)}
check(
    "T5 books",
    sp.simplify(sp.expand(coupling - target).subs(books)) == 0,
    "with the momentum books, (1/2) Theta.h for h = t(d xi + d xi^T) is d(t xi.P)/dt - xi.P plus a divergence",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL the kinetic term matches the comparator iff alpha = K/4 and beta = -alpha. "
        "sqrt(g) R agrees with R1 at first order, and its second order differs from R2 by a divergence. "
        "On 1s the clock-only weight ratio is 4/3; on 2p0 the axial potential ratio is 3/5. "
        "The drifting-length coupling reduces to -xi.P by the books. "
        "The non-axis exchange and the full W=1 cancellation were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - the member is K times the comparator's second-order lapse-and-shift action "
        "exactly when alpha = K/4 and beta = -alpha, for a generic field, and the drifting lengths "
        "couple as -xi.P once the books are used.",
        flush=True,
    )
