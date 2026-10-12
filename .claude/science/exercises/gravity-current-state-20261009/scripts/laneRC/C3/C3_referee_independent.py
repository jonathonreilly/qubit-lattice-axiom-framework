"""Independent checks for the Lane RC / C3 referee.

This deliberately does not import either c3_* worker script.  It uses exact
Fractions for a compact-support real-space check and SymPy for the p=0
certificate and improved-dispersion expansions.
"""

from fractions import Fraction as F
import itertools

import numpy as np
import sympy as sp


AXES = range(3)


def shift(a, axis, step):
    return np.roll(a, -step, axis=axis)


def diff(a, axis):
    return shift(a, axis, 1) - a


def lap(a):
    return sum(shift(a, j, 1) + shift(a, j, -1) - 2 * a for j in AXES)


def central(a, axis):
    return (shift(a, axis, 1) - shift(a, axis, -1)) * F(1, 2)


def average(a, axis):
    return (shift(a, axis, 1) + shift(a, axis, -1)) * F(1, 2)


def t00(phi, pi):
    out = F(1, 2) * pi**2 + F(1, 8) * phi**2
    for j in AXES:
        dj = diff(phi, j)
        out += F(1, 4) * (dj**2 + shift(dj, j, -1) ** 2)
    return out


def momentum(phi, pi):
    return [F(1, 2) * (pi + shift(pi, j, 1)) * diff(phi, j) for j in AXES]


def directional(fun, phi, pi, axis):
    a, b = central(phi, axis), central(pi, axis)
    plus, minus = fun(phi + a, pi + b), fun(phi - a, pi - b)
    if isinstance(plus, list):
        return [(x - y) * F(1, 2) for x, y in zip(plus, minus)]
    return (plus - minus) * F(1, 2)


def energy_cos(phi, pi, axis):
    omega2_phi = -lap(phi) + F(1, 4) * phi
    return np.sum(
        F(1, 2) * pi * average(pi, axis)
        + F(1, 2) * phi * average(omega2_phi, axis)
    )


def momentum_cos(phi, pi, c, a):
    return np.sum(momentum(average(phi, c), pi)[a])


def exact_real_space_check():
    rng = np.random.default_rng(884422)
    side, pad, support = 9, 3, 3
    phi = np.zeros((side,) * 3, dtype=object)
    pi = np.zeros((side,) * 3, dtype=object)
    s = slice(pad, pad + support)
    phi[s, s, s] = rng.integers(-3, 4, (support,) * 3).astype(object)
    pi[s, s, s] = rng.integers(-3, 4, (support,) * 3).astype(object)
    x = np.indices((side,) * 3)

    zero = F(0)
    translational = zero
    for c in AXES:
        translational = max(translational, abs(np.sum(directional(t00, phi, pi, c))))
        for term in directional(momentum, phi, pi, c):
            translational = max(translational, abs(np.sum(term)))

    hm = np.sum(t00(phi, pi))
    ptot = [np.sum(term) for term in momentum(phi, pi)]
    dphi_dt, dpi_dt = pi, lap(phi) - F(1, 4) * phi
    d_t00 = (t00(phi + dphi_dt, pi + dpi_dt) - t00(phi - dphi_dt, pi - dpi_dt)) * F(1, 2)
    hh = max(abs(np.sum(x[b] * d_t00) + ptot[b]) for b in AXES)

    boost = zero
    defect = zero
    omega2_phi = -lap(phi) + F(1, 4) * phi
    for b, c in itertools.product(AXES, repeat=2):
        lhs = np.sum(x[b] * directional(t00, phi, pi, c))
        rhs = -(b == c) * energy_cos(phi, pi, c)
        boost = max(boost, abs(lhs - rhs))
    for c in AXES:
        rhs = -F(1, 4) * np.sum(diff(pi, c) ** 2 + diff(phi, c) * diff(omega2_phi, c))
        defect = max(defect, abs((energy_cos(phi, pi, c) - hm) - rhs))

    rotation = zero
    for a, b, c in itertools.product(AXES, repeat=3):
        if a >= b:
            continue
        d_p = directional(momentum, phi, pi, c)
        lhs = np.sum(x[b] * d_p[a]) - np.sum(x[a] * d_p[b])
        rhs = -((b == c) * momentum_cos(phi, pi, c, a) - (a == c) * momentum_cos(phi, pi, c, b))
        rotation = max(rotation, abs(lhs - rhs))

    print("exact Fraction residuals")
    print("  translations:", translational)
    print("  {K,H}+P:", hh)
    print("  boost closed form:", boost)
    print("  boost defect formula:", defect)
    print("  rotation closed form:", rotation)


def stencil_check():
    # Direct adjoints of the 09-14 rows.  xi_j is stored on the j-edge
    # based at x.  A is antisymmetric, so its discrete symmetric gradient
    # vanishes including diagonal and face slots.
    A = np.array([[0, 2, -3], [-2, 0, 5], [3, -5, 0]], dtype=int)
    v = np.array([7, -4, 1], dtype=int)

    def xi(j, x):
        edge_center = np.asarray(x, dtype=object)
        edge_center[j] += F(1, 2)
        return F(v[j]) + sum(F(A[j, k]) * edge_center[k] for k in AXES)

    points = list(itertools.product(range(-2, 3), repeat=3))
    diagonal = []
    off_diagonal = []
    for x_tuple in points:
        x = np.array(x_tuple, dtype=int)
        for j in AXES:
            ej = np.eye(3, dtype=int)[j]
            diagonal.append(xi(j, x - ej) - xi(j, x))
        for i in AXES:
            for j in range(i + 1, 3):
                ei, ej = np.eye(3, dtype=int)[i], np.eye(3, dtype=int)[j]
                off_diagonal.append(
                    xi(j, x) - xi(j, x + ei) + xi(i, x) - xi(i, x + ej)
                )

    # Direct adjoint of the S row on an affine lapse.
    n0 = F(11)
    slope = np.array([F(2), F(-3), F(5)], dtype=object)

    def lapse(x):
        return n0 + sum(slope[k] * F(int(x[k])) for k in AXES)

    scalar_diag = []
    scalar_off = []
    for x_tuple in points:
        x = np.array(x_tuple, dtype=int)
        for j in AXES:
            val = F(0)
            for i in AXES:
                if i == j:
                    continue
                ei = np.eye(3, dtype=int)[i]
                val += lapse(x - ei) + lapse(x + ei) - 2 * lapse(x)
            scalar_diag.append(val)
        for i in AXES:
            for j in range(i + 1, 3):
                ei, ej = np.eye(3, dtype=int)[i], np.eye(3, dtype=int)[j]
                scalar_off.append(
                    -lapse(x) + lapse(x + ei) + lapse(x + ej) - lapse(x + ei + ej)
                )

    print("09-14 adjoint-stencil residuals")
    print("  G^T(rotation), diagonal slots:", max(map(abs, diagonal)))
    print("  G^T(rotation), face slots:", max(map(abs, off_diagonal)))
    print("  S^T(affine lapse), diagonal slots:", max(map(abs, scalar_diag)))
    print("  S^T(affine lapse), face slots:", max(map(abs, scalar_off)))


def p_zero_certificate():
    # The pi-pi component alone suffices.  At p=0 the completion gate
    # 1-cos(p) and its first derivative vanish.  Momentum-density columns
    # have no pi-pi component.  The derivative of the lattice LHS is
    # -i cos(q)/2, which cannot be a q-independent multiple of H_pp=1/2.
    i = sp.I
    lattice_A = sp.Matrix([[sp.Rational(1, 2)], [sp.Rational(1, 2)]])
    lattice_b = sp.Matrix([-i * sp.Rational(1, 2), 0])  # q=0, pi/2
    continuum_b = sp.Matrix([-i * sp.Rational(1, 2), -i * sp.Rational(1, 2)])
    print("p=0 first-Taylor-coefficient certificate (exact SymPy ranks)")
    print("  lattice rank A, rank[A|b]:", lattice_A.rank(), lattice_A.row_join(lattice_b).rank())
    print("  continuum rank A, rank[A|b]:", lattice_A.rank(), lattice_A.row_join(continuum_b).rank())
    print("  d/dp completion gate at p=0:", sp.diff(1 - sp.cos(sp.Symbol("p")), sp.Symbol("p")).subs(sp.Symbol("p"), 0))


def dispersion_check():
    k = sp.symbols("k", real=True)
    coefficients = [sp.Rational(1), sp.Rational(1, 12), sp.Rational(1, 90), sp.Rational(1, 560), sp.Rational(1, 3150)]
    s2 = (2 * sp.sin(k / 2)) ** 2
    print("improved-dispersion exact checks")
    for r in range(1, 6):
        u = sp.Rational(1, 2) * sum(coefficients[n] * s2 ** (n + 1) for n in range(r))
        anomaly = sp.expand_trig(sp.diff(u, k, 2) - 1)
        leading = sp.series(anomaly, k, 0, 2 * r + 2).removeO().as_leading_term(k)
        zone_average = sp.simplify((sp.diff(u, k).subs(k, sp.pi) - sp.diff(u, k).subs(k, -sp.pi)) / (2 * sp.pi) - 1)
        print(f"  r={r}: leading A={leading}; <A>={zone_average}; A(pi)={sp.simplify(anomaly.subs(k, sp.pi))}")


if __name__ == "__main__":
    stencil_check()
    exact_real_space_check()
    p_zero_certificate()
    dispersion_check()
