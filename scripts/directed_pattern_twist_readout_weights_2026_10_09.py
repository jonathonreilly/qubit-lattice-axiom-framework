#!/usr/bin/env python3
"""Readout weights of the directed six-parameter pair, exact and finite.

Conditional on the same density pattern as the parent CHSH note. This runner
does not compute a CHSH square. Local projective weights and symmetric joint
weights are compared with the antisymmetric coordinate weight, and one
improper reflection is applied to the correlation matrix.
"""

from __future__ import annotations

from fractions import Fraction

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/DIRECTED_PATTERN_TWIST_READOUT_WEIGHTS_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


class G:
    """Gaussian rational x + y i."""

    def __init__(self, re: Fraction | int = 0, im: Fraction | int = 0) -> None:
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other: G | Fraction | int) -> G:
        o = other if isinstance(other, G) else G(other)
        return G(self.re + o.re, self.im + o.im)

    def __radd__(self, other: G | Fraction | int) -> G:
        return self + other

    def __sub__(self, other: G | Fraction | int) -> G:
        o = other if isinstance(other, G) else G(other)
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, other: G | Fraction | int) -> G:
        o = other if isinstance(other, G) else G(other)
        return G(
            self.re * o.re - self.im * o.im,
            self.re * o.im + self.im * o.re,
        )

    def __rmul__(self, other: G | Fraction | int) -> G:
        return self * other

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, G):
            other = G(other)  # type: ignore[arg-type]
        return self.re == other.re and self.im == other.im

    def __neg__(self) -> G:
        return G(-self.re, -self.im)


def zeros(n: int) -> list[list[G]]:
    return [[G(0) for _ in range(n)] for _ in range(n)]


def matmul(a: list[list[G]], b: list[list[G]]) -> list[list[G]]:
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for j in range(n):
            acc = G(0)
            for k in range(n):
                acc = acc + a[i][k] * b[k][j]
            out[i][j] = acc
    return out


def trace(a: list[list[G]]) -> G:
    acc = G(0)
    for i in range(len(a)):
        acc = acc + a[i][i]
    return acc


def kron(a: list[list[G]], b: list[list[G]]) -> list[list[G]]:
    n = len(a)
    m = len(b)
    out = zeros(n * m)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                for ell in range(m):
                    out[i * m + k][j * m + ell] = a[i][j] * b[k][ell]
    return out


def add_scaled(acc: list[list[G]], term: list[list[G]], scale: Fraction | int) -> None:
    s = G(scale)
    for i in range(len(acc)):
        for j in range(len(acc)):
            acc[i][j] = acc[i][j] + s * term[i][j]


def scale_matrix(a: list[list[G]], scale: Fraction) -> list[list[G]]:
    out = zeros(len(a))
    s = G(scale)
    for i in range(len(a)):
        for j in range(len(a)):
            out[i][j] = s * a[i][j]
    return out


def add_matrix(a: list[list[G]], b: list[list[G]]) -> list[list[G]]:
    out = zeros(len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            out[i][j] = a[i][j] + b[i][j]
    return out


I2 = [[G(1), G(0)], [G(0), G(1)]]
X = [[G(0), G(1)], [G(1), G(0)]]
Y = [[G(0), G(0, -1)], [G(0, 1), G(0)]]
Z = [[G(1), G(0)], [G(0), G(-1)]]
PAULI = {"x": X, "y": Y, "z": Z}
XX, YY, ZZ = kron(X, X), kron(Y, Y), kron(Z, Z)
YX, XY = kron(Y, X), kron(X, Y)
ZI, IZ, II = kron(Z, I2), kron(I2, Z), kron(I2, I2)


def operator(
    p: Fraction, q: Fraction, v: Fraction, u: Fraction, t: Fraction
) -> list[list[G]]:
    """Return 4ρ from the Pauli pattern, not from a closed eigenvalue list."""
    acc = zeros(4)
    add_scaled(acc, II, 1)
    add_scaled(acc, ZI, q)
    add_scaled(acc, IZ, p)
    add_scaled(acc, XX, u)
    add_scaled(acc, YY, u)
    add_scaled(acc, YX, t)
    add_scaled(acc, XY, -t)
    add_scaled(acc, ZZ, v)
    return acc


def correlation(u: Fraction, t: Fraction, v: Fraction) -> list[list[Fraction]]:
    z = Fraction(0)
    return [
        [u, -t, z],
        [t, u, z],
        [z, z, v],
    ]


def matmul_r(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def transpose_r(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def det3(a: list[list[int]]) -> int:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def partial_trace_qubit2(h: list[list[G]]) -> list[list[G]]:
    """Trace out the fast index. Kronecker order is qubit1, then qubit2."""
    out = zeros(2)
    for i in range(2):
        for j in range(2):
            acc = G(0)
            for k in range(2):
                acc = acc + h[i * 2 + k][j * 2 + k]
            out[i][j] = acc
    return out


def partial_trace_qubit1(h: list[list[G]]) -> list[list[G]]:
    out = zeros(2)
    for k in range(2):
        for ell in range(2):
            acc = G(0)
            for i in range(2):
                acc = acc + h[i * 2 + k][i * 2 + ell]
            out[k][ell] = acc
    return out


def rational_matrix(a: list[list[G]]) -> list[list[Fraction]] | None:
    out: list[list[Fraction]] = []
    for row in a:
        acc: list[Fraction] = []
        for entry in row:
            if entry.im != 0:
                return None
            acc.append(entry.re)
        out.append(acc)
    return out


def bloch_z(reduced_h: list[list[Fraction]]) -> Fraction:
    """Return the z Bloch number of ρ = H_reduced / 4."""
    rho = [[entry / 4 for entry in row] for row in reduced_h]
    # (I + r Z)/2 has diagonal ((1+r)/2, (1-r)/2) and zero off-diagonal.
    return rho[0][0] - rho[1][1]


def expectation(h: list[list[G]], obs: list[list[G]]) -> Fraction:
    value = trace(matmul(h, obs))
    if value.im != 0:
        raise RuntimeError("non-real correlator")
    return value.re / 4


def born_plus(reduced_h: list[list[Fraction]], axis: str) -> Fraction:
    rho = [[entry / 4 for entry in row] for row in reduced_h]
    if axis == "z":
        proj = scale_matrix(
            add_matrix([[G(1), G(0)], [G(0), G(1)]], Z), Fraction(1, 2)
        )
    elif axis == "x":
        proj = scale_matrix(
            add_matrix([[G(1), G(0)], [G(0), G(1)]], X), Fraction(1, 2)
        )
    else:
        proj = scale_matrix(
            add_matrix([[G(1), G(0)], [G(0), G(1)]], Y), Fraction(1, 2)
        )
    rho_g = [[G(entry) for entry in row] for row in rho]
    value = trace(matmul(rho_g, proj))
    if value.im != 0:
        raise RuntimeError("non-real Born weight")
    return value.re


def isqrt(n: int) -> int | None:
    if n < 0:
        return None
    r = 0
    bit = 1 << (n.bit_length() + 1)
    while bit:
        trial = r + bit
        if trial * trial <= n:
            r = trial
        bit >>= 1
    if r * r == n:
        return r
    return None


def spectrum(p: Fraction, q: Fraction, v: Fraction, u: Fraction, t: Fraction) -> list[Fraction] | None:
    disc = (p - q) ** 2 + 4 * (u * u + t * t)
    n_sqrt = isqrt(disc.numerator)
    d_sqrt = isqrt(disc.denominator)
    if n_sqrt is None or d_sqrt is None:
        return None
    root = Fraction(n_sqrt, d_sqrt)
    return sorted(
        [
            1 + p + q + v,
            1 - p - q + v,
            (1 - v) + root,
            (1 - v) - root,
        ],
        key=lambda value: (value.numerator, value.denominator),
    )


def quadratic_form(u: Fraction, t: Fraction, v: Fraction, a: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    ax, ay, az = a
    rows = correlation(u, t, v)
    total = Fraction(0)
    vec = (ax, ay, az)
    for i in range(3):
        for j in range(3):
            total += vec[i] * rows[i][j] * vec[j]
    return total


def joint_weight(
    u: Fraction,
    t: Fraction,
    v: Fraction,
    weights: dict[tuple[str, str], Fraction],
) -> Fraction:
    axes = ("x", "y", "z")
    total = Fraction(0)
    rows = correlation(u, t, v)
    index = {"x": 0, "y": 1, "z": 2}
    for left in axes:
        for right in axes:
            w = weights.get((left, right), Fraction(0))
            total += w * rows[index[left]][index[right]]
    return total


def main() -> None:
    checks = Checks()
    p_refl = [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1],
    ]
    checks.check("P = diag(1,-1,1) has determinant -1", det3(p_refl) == -1)
    checks.check(
        "P is an involution",
        matmul_r(
            [[Fraction(x) for x in row] for row in p_refl],
            [[Fraction(x) for x in row] for row in p_refl],
        )
        == [
            [Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(1)],
        ],
    )

    samples = (
        (Fraction(2), Fraction(3), Fraction(-1)),
        (Fraction(0), Fraction(1), Fraction(-1)),
        (Fraction(0), Fraction(-1), Fraction(-1)),
        (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)),
    )
    p_frac = [[Fraction(x) for x in row] for row in p_refl]
    for u, t, v in samples:
        flipped = matmul_r(matmul_r(p_frac, correlation(u, t, v)), p_frac)
        checks.check(
            f"P T P replaces t by -t at {(u, t, v)}",
            flipped == correlation(u, -t, v),
        )
        checks.check(
            f"P moves T exactly when t is nonzero at {(u, t, v)}",
            (flipped == correlation(u, t, v)) == (t == 0),
        )

    generic = (Fraction(0), Fraction(0), Fraction(-1), Fraction(2), Fraction(3))
    p0, q0, v0, u0, t0 = generic
    h = operator(p0, q0, v0, u0, t0)
    index = {"x": 0, "y": 1, "z": 2}
    rows = correlation(u0, t0, v0)
    for left in ("x", "y", "z"):
        for right in ("x", "y", "z"):
            obs = kron(PAULI[left], PAULI[right])
            got = expectation(h, obs)
            checks.check(
                f"operator correlator {left}{right} equals T",
                got == rows[index[left]][index[right]],
            )

    for u, t, v in samples:
        hh = operator(Fraction(0), Fraction(0), v, u, t)
        odd = expectation(hh, YX) - expectation(hh, XY)
        checks.check(f"antisymmetric coordinate weight equals 2t at t={t}", odd == 2 * t)

    pure = (
        (Fraction(0), Fraction(1), Fraction(-1)),
        (Fraction(0), Fraction(-1), Fraction(-1)),
    )
    odd_values = []
    for u, t, v in pure:
        hh = operator(Fraction(0), Fraction(0), v, u, t)
        odd_values.append(expectation(hh, YX) - expectation(hh, XY))
        checks.check(
            f"diagonal correlators ignore the sign of t={t}",
            expectation(hh, XX) == u
            and expectation(hh, YY) == u
            and expectation(hh, ZZ) == v,
        )
        spec = spectrum(Fraction(0), Fraction(0), v, u, t)
        checks.check(
            f"pure twist t={t} has spectrum 0,0,0,4",
            spec == [Fraction(0), Fraction(0), Fraction(0), Fraction(4)],
        )
    checks.check("the two pure twists are separated by 4", odd_values[0] - odd_values[1] == 4)
    checks.check("those readouts are +2 and -2", odd_values == [Fraction(2), Fraction(-2)])

    reductions = (
        (Fraction(0), Fraction(0), Fraction(4), Fraction(-2), Fraction(7)),
        (Fraction(0), Fraction(3, 5), Fraction(-1), Fraction(1, 2), Fraction(9)),
        (Fraction(-2, 7), Fraction(0), Fraction(1, 4), Fraction(8), Fraction(-3)),
        (Fraction(1, 3), Fraction(-1, 5), Fraction(2), Fraction(0), Fraction(11)),
    )
    for p, q, v, u, t in reductions:
        hh = operator(p, q, v, u, t)
        left = rational_matrix(partial_trace_qubit2(hh))
        right = rational_matrix(partial_trace_qubit1(hh))
        checks.check(f"reductions are real at {(p, q, u, t, v)}", left is not None and right is not None)
        if left is None or right is None:
            continue
        checks.check(
            f"wing-1 Bloch vector is (0,0,q) at q={q}",
            left[0][1] == 0
            and left[1][0] == 0
            and bloch_z(left) == q
            and born_plus(left, "x") == Fraction(1, 2)
            and born_plus(left, "y") == Fraction(1, 2)
            and born_plus(left, "z") == (1 + q) / 2,
        )
        checks.check(
            f"wing-2 Bloch vector is (0,0,p) at p={p}",
            right[0][1] == 0
            and right[1][0] == 0
            and bloch_z(right) == p
            and born_plus(right, "x") == Fraction(1, 2)
            and born_plus(right, "y") == Fraction(1, 2)
            and born_plus(right, "z") == (1 + p) / 2,
        )
        other = operator(p, q, v, u, -t - 4)
        left2 = rational_matrix(partial_trace_qubit2(other))
        right2 = rational_matrix(partial_trace_qubit1(other))
        checks.check(
            f"local reductions ignore t at {(p, q)}",
            left2 == left and right2 == right,
        )

    vectors = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(3), Fraction(-4), Fraction(5)),
    )
    for a in vectors:
        u, t, v = Fraction(2), Fraction(5), Fraction(-3)
        even = u * (a[0] * a[0] + a[1] * a[1]) + v * a[2] * a[2]
        checks.check(
            f"same-direction weight ignores t at {a}",
            quadratic_form(u, t, v, a) == even
            and quadratic_form(u, -t, v, a) == even,
        )

    u, t, v = Fraction(2), Fraction(5), Fraction(-3)
    symmetric = {
        ("x", "y"): Fraction(4),
        ("y", "x"): Fraction(4),
        ("x", "x"): Fraction(1),
        ("y", "y"): Fraction(1),
        ("z", "z"): Fraction(1),
    }
    antisymmetric = {("y", "x"): Fraction(1), ("x", "y"): Fraction(-1)}
    checks.check(
        "a symmetric joint weight ignores t",
        joint_weight(u, t, v, symmetric) == joint_weight(u, -t, v, symmetric) == 2 * u + v,
    )
    checks.check(
        "the coordinate antisymmetric weight equals 2t",
        joint_weight(u, t, v, antisymmetric) == 2 * t,
    )
    for left in ("x", "y", "z"):
        for right in ("x", "y", "z"):
            coeff = Fraction(0)
            if (left, right) == ("y", "x"):
                coeff = Fraction(1)
            if (left, right) == ("x", "y"):
                coeff = Fraction(-1)
            basis = {(left, right): Fraction(1)}
            got_t = joint_weight(Fraction(0), Fraction(1), Fraction(0), basis)
            got_u = joint_weight(Fraction(1), Fraction(0), Fraction(0), basis)
            got_v = joint_weight(Fraction(0), Fraction(0), Fraction(1), basis)
            checks.check(
                f"basis weight {left}{right} has coefficients (u,t,v)",
                got_t == coeff and got_u == (1 if left == right and left != "z" else 0)
                and got_v == (1 if left == right == "z" else 0),
            )

    print(
        "per_element: Nine coordinate joint weights and the two local "
        "projective instruments on x, y, and z. No POVM is tested."
    )
    print(
        "per_site: Both one-site reductions of one bond. A third site is not tested."
    )
    print(
        "per_mode: The twist sign is tested, including t and -t. "
        "u, v, p, and q are varied only as controls. No CHSH square is tested."
    )
    print(
        "per_block: One nearest-neighbor bond. Plaquettes and cubes are not tested."
    )
    print(
        "lattice_wide: checked and not executed — no infinite-volume or multi-bond "
        "statement is claimed or tested."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
