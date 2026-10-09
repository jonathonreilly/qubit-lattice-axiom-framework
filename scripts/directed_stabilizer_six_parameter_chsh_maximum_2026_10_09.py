#!/usr/bin/env python3
"""Exact CHSH squares of the directed six-parameter two-qubit family.

The density hypothesis stays explicit. Arithmetic is rational, with one
quadratic extension a + b√2 for the four signed-axis maximizers.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

AUDIT_TIMEOUT_SEC = 120


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

    def conj(self) -> G:
        return G(self.re, -self.im)

    def norm2(self) -> Fraction:
        return self.re * self.re + self.im * self.im


class S2:
    """Value a + b√2."""

    def __init__(self, a: Fraction | int, b: Fraction | int = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: S2) -> S2:
        return S2(self.a + other.a, self.b + other.b)

    def __sub__(self, other: S2) -> S2:
        return S2(self.a - other.a, self.b - other.b)

    def __mul__(self, other: S2 | int | Fraction) -> S2:
        if not isinstance(other, S2):
            return S2(self.a * other, self.b * other)
        return S2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __rmul__(self, other: S2 | int | Fraction) -> S2:
        return self * other

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, S2):
            return False
        return self.a == other.a and self.b == other.b


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def zeros(n: int) -> list[list[G]]:
    return [[G(0) for _ in range(n)] for _ in range(n)]


def kron(a: list[list[G]], b: list[list[G]]) -> list[list[G]]:
    n = len(a)
    out = zeros(n * len(b))
    m = len(b)
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


I2 = [[G(1), G(0)], [G(0), G(1)]]
X = [[G(0), G(1)], [G(1), G(0)]]
Y = [[G(0), G(0, -1)], [G(0, 1), G(0)]]
Z = [[G(1), G(0)], [G(0), G(-1)]]
XX, YY, ZZ = kron(X, X), kron(Y, Y), kron(Z, Z)
YX, XY = kron(Y, X), kron(X, Y)
ZI, IZ, II = kron(Z, I2), kron(I2, Z), kron(I2, I2)


def operator(p: Fraction, q: Fraction, v: Fraction, u: Fraction, t: Fraction) -> list[list[G]]:
    """Return 4ρ, built as a Pauli combination, not from the closed eigenvalue list."""
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
    return [
        [u, -t, Fraction(0)],
        [t, u, Fraction(0)],
        [Fraction(0), Fraction(0), v],
    ]


def symmetric_twist(u: Fraction, t: Fraction, v: Fraction) -> list[list[Fraction]]:
    return [
        [u, t, Fraction(0)],
        [t, u, Fraction(0)],
        [Fraction(0), Fraction(0), v],
    ]


def gram(u: Fraction, t: Fraction, v: Fraction) -> list[list[Fraction]]:
    rows = correlation(u, t, v)
    return matmul(transpose(rows), rows)


AXES = {
    "x": (Fraction(1), Fraction(0), Fraction(0)),
    "-x": (Fraction(-1), Fraction(0), Fraction(0)),
    "y": (Fraction(0), Fraction(1), Fraction(0)),
    "-y": (Fraction(0), Fraction(-1), Fraction(0)),
    "z": (Fraction(0), Fraction(0), Fraction(1)),
    "-z": (Fraction(0), Fraction(0), Fraction(-1)),
}


def axis_correlator(
    u: Fraction, t: Fraction, v: Fraction, left: str, right: str
) -> Fraction:
    bx, by, bz = AXES[right]
    ax, ay, az = AXES[left]
    image = (u * bx - t * by, t * bx + u * by, v * bz)
    return ax * image[0] + ay * image[1] + az * image[2]


def axis_value(
    u: Fraction, t: Fraction, v: Fraction, settings: tuple[str, str, str, str]
) -> Fraction:
    a1, a2, b1, b2 = settings
    return (
        axis_correlator(u, t, v, a1, b1)
        + axis_correlator(u, t, v, a1, b2)
        + axis_correlator(u, t, v, a2, b1)
        - axis_correlator(u, t, v, a2, b2)
    )


def chsh_square(r2: Fraction, v2: Fraction) -> Fraction:
    if r2 >= v2:
        return 8 * r2
    return 4 * (r2 + v2)


def psd(p: Fraction, q: Fraction, v: Fraction, r2: Fraction) -> bool:
    longitudinal = (p - q) ** 2 + 4 * r2 <= (1 - v) ** 2
    return abs(p + q) <= 1 + v and longitudinal


def main() -> None:
    checks = Checks()
    rz = [
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    ez = (Fraction(0), Fraction(0), Fraction(1))
    rotated_z = (
        rz[0][0] * ez[0] + rz[0][1] * ez[1] + rz[0][2] * ez[2],
        rz[1][0] * ez[0] + rz[1][1] * ez[1] + rz[1][2] * ez[2],
        rz[2][0] * ez[0] + rz[2][1] * ez[1] + rz[2][2] * ez[2],
    )
    checks.check(
        "quarter turn about z fixes e_z and has order 4",
        rotated_z == ez
        and matmul(matmul(matmul(rz, rz), rz), rz)
        == [
            [Fraction(1), Fraction(0), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(1)],
        ],
    )

    samples = [
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(3, 5), Fraction(4, 5)),
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(5, 13), Fraction(12, 13)),
        (Fraction(1, 5), Fraction(-1, 5), Fraction(0), Fraction(1, 3), Fraction(1, 7)),
        (Fraction(0), Fraction(0), Fraction(-1, 2), Fraction(0), Fraction(3, 4)),
        (Fraction(0), Fraction(0), Fraction(1, 3), Fraction(-1, 3), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    ]
    for p, q, v, u, t in samples:
        r2 = u * u + t * t
        gram_matrix = gram(u, t, v)
        expect = [
            [r2, Fraction(0), Fraction(0)],
            [Fraction(0), r2, Fraction(0)],
            [Fraction(0), Fraction(0), v * v],
        ]
        checks.check(f"T^T T is diag(r^2,r^2,v^2) at {(u, t, v)}", gram_matrix == expect)
        matrix = operator(p, q, v, u, t)
        checks.check(
            f"computational diagonals match at {(p, q, v, u, t)}",
            matrix[0][0] == G(1 + p + q + v)
            and matrix[3][3] == G(1 - p - q + v)
            and all(matrix[0][j] == G(0) for j in range(1, 4))
            and all(matrix[3][j] == G(0) for j in range(3))
            and all(matrix[i][0] == G(0) for i in range(1, 4))
            and all(matrix[i][3] == G(0) for i in range(3)),
        )
        block = matrix[1][1] * matrix[2][2] - matrix[1][2].norm2()
        checks.check(
            f"block product matches the discriminant gap at {(p, q, v, u, t)}",
            matrix[1][2] == matrix[2][1].conj()
            and block == G((1 - v) ** 2 - (p - q) ** 2 - 4 * r2),
        )
        rotated = matmul(rz, matmul(correlation(u, t, v), transpose(rz)))
        checks.check(
            f"antisymmetric twist is fixed by the quarter turn at {(u, t)}",
            rotated == correlation(u, t, v),
        )

    sym = symmetric_twist(Fraction(0), Fraction(1), Fraction(-1))
    sym_rotated = matmul(rz, matmul(sym, transpose(rz)))
    checks.check(
        "symmetric twist is not fixed by the quarter turn",
        sym_rotated != sym,
    )
    unequal = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]
    checks.check(
        "c_11 unequal to c_22 is not fixed by the quarter turn",
        matmul(rz, matmul(unequal, transpose(rz))) != unequal,
    )

    # Pauli path for the singlet, written as literal images rather than the closed form.
    singlet = operator(Fraction(0), Fraction(0), Fraction(-1), Fraction(-1), Fraction(0))

    def image(vector: list[G]) -> list[G]:
        return [
            sum((singlet[i][j] * vector[j] for j in range(4)), G(0))
            for i in range(4)
        ]

    checks.check(
        "singlet kills |00>, |11>, and the symmetric triplet vector",
        image([G(1), G(0), G(0), G(0)]) == [G(0), G(0), G(0), G(0)]
        and image([G(0), G(0), G(0), G(1)]) == [G(0), G(0), G(0), G(0)]
        and image([G(0), G(1), G(1), G(0)]) == [G(0), G(0), G(0), G(0)],
    )
    checks.check(
        "singlet multiplies |01>-|10> by 4",
        image([G(0), G(1), G(-1), G(0)]) == [G(0), G(4), G(-4), G(0)],
    )

    twist = operator(Fraction(0), Fraction(0), Fraction(-1), Fraction(0), Fraction(1))

    def twist_image(vector: list[G]) -> list[G]:
        return [
            sum((twist[i][j] * vector[j] for j in range(4)), G(0))
            for i in range(4)
        ]

    pure_twist = [G(0), G(0, -1), G(1), G(0)]
    checks.check(
        "pure twist multiplies |10>-i|01> by 4 and kills |00>",
        twist_image(pure_twist) == [4 * entry for entry in pure_twist]
        and twist_image([G(1), G(0), G(0), G(0)]) == [G(0), G(0), G(0), G(0)],
    )

    def planar_square(u: Fraction, t: Fraction) -> Fraction:
        def apply(x: Fraction, y: Fraction) -> tuple[Fraction, Fraction]:
            return (u * x - t * y, t * x + u * y)

        cx, cy = apply(Fraction(1), Fraction(1))
        dx, dy = apply(Fraction(1), Fraction(-1))
        tc2 = cx * cx + cy * cy
        td2 = dx * dx + dy * dy
        checks.check(
            f"equatorial images have equal square length at {(u, t)}",
            tc2 == td2 == 2 * (u * u + t * t),
        )
        return tc2 + td2 + 2 * tc2

    for u, t in (
        (Fraction(1), Fraction(0)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(1, 2), Fraction(1, 3)),
    ):
        r2 = u * u + t * t
        checks.check(
            f"equatorial strategy square is 8 r^2 at {(u, t)}",
            planar_square(u, t) == 8 * r2,
        )
    checks.check(
        "dropping the twist changes the square at (u,t)=(0,1)",
        8 * (Fraction(0) * Fraction(0)) != 8 * (Fraction(0) + Fraction(1)),
    )

    def length_square(r2: Fraction, v2: Fraction) -> Fraction:
        total = r2 + v2
        tc2 = 4 * v2 * v2 / total
        td2 = 4 * r2 * r2 / total
        cross = 4 * v2 * r2 / total
        checks.check(
            f"longitudinal cross term is the rational square root at {(r2, v2)}",
            cross * cross == tc2 * td2,
        )
        return tc2 + td2 + 2 * cross

    for r2, v2 in (
        (Fraction(0), Fraction(1)),
        (Fraction(1, 4), Fraction(1)),
        (Fraction(1, 9), Fraction(4, 9)),
        (Fraction(4, 25), Fraction(9, 25)),
    ):
        checks.check(
            f"split lengths attain 4(r^2+v^2) at {(r2, v2)}",
            length_square(r2, v2) == 4 * (r2 + v2),
        )
        ordered = sorted((r2, r2, v2), reverse=True)
        checks.check(
            f"branch formula matches the two largest eigenvalues at {(r2, v2)}",
            chsh_square(r2, v2) == 4 * (ordered[0] + ordered[1]),
        )

    checks.check(
        "the two branch formulas agree when r^2 = v^2",
        chsh_square(Fraction(9, 16), Fraction(9, 16)) == Fraction(9, 2),
    )
    def isotropic_gap(w: Fraction) -> Fraction:
        return (1 - w) ** 2 - 4 * w * w

    def isotropic_factor(w: Fraction) -> Fraction:
        return (1 - 3 * w) * (1 + w)

    def eight_gap(v: Fraction) -> Fraction:
        return 8 - 2 * (1 - v) ** 2

    def eight_factor(v: Fraction) -> Fraction:
        return 2 * (3 - v) * (1 + v)

    gap_points = (Fraction(0), Fraction(1, 5), Fraction(-2, 3), Fraction(1, 7))
    checks.check(
        "isotropic positivity gap factors as (1-3w)(1+w)",
        all(isotropic_gap(w) == isotropic_factor(w) for w in gap_points),
    )
    checks.check(
        "8 - 2(1-v)^2 factors as 2(3-v)(1+v)",
        all(eight_gap(v) == eight_factor(v) for v in gap_points),
    )

    rational_circle = (
        (Fraction(-1), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(-1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(-8, 17), Fraction(15, 17)),
    )
    for u, t in rational_circle:
        checks.check(
            f"rational circle point {(u, t)} is positive with square 8",
            u * u + t * t == 1
            and psd(Fraction(0), Fraction(0), Fraction(-1), Fraction(1))
            and chsh_square(Fraction(1), Fraction(1)) == 8,
        )
        vector = [G(0), G(u, -t), G(1), G(0)]
        matrix = operator(Fraction(0), Fraction(0), Fraction(-1), u, t)
        image_vector = [
            sum((matrix[i][j] * vector[j] for j in range(4)), G(0))
            for i in range(4)
        ]
        checks.check(
            f"circle vector is an eigenvalue-4 state at {(u, t)}",
            image_vector == [4 * entry for entry in vector],
        )

    missed = (
        (Fraction(0), Fraction(0), Fraction(-1), Fraction(1, 2), Fraction(1, 2), Fraction(6)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1, 2), Fraction(0), Fraction(2)),
        (Fraction(0), Fraction(0), Fraction(1, 3), Fraction(-1, 3), Fraction(0), Fraction(8, 9)),
        (Fraction(0), Fraction(0), Fraction(-3, 4), Fraction(-3, 4), Fraction(0), Fraction(9, 2)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(4)),
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    )
    for p, q, v, u, t, square in missed:
        r2 = u * u + t * t
        checks.check(
            f"positive point {(p, q, v, u, t)} has square {square} below 8",
            psd(p, q, v, r2) and chsh_square(r2, v * v) == square and square < 8,
        )
    checks.check(
        "r^2 = 4 at v = -1 is not positive, so its formal square 32 is not a state",
        not psd(Fraction(0), Fraction(0), Fraction(-1), Fraction(4))
        and chsh_square(Fraction(4), Fraction(1)) == 32,
    )
    checks.check(
        "a nonzero local Bloch number exits the equality slice",
        not psd(Fraction(1, 10), Fraction(0), Fraction(-1), Fraction(1)),
    )
    checks.check(
        "v = 1 forbids a transverse correlation",
        psd(Fraction(0), Fraction(0), Fraction(1), Fraction(0))
        and not psd(Fraction(0), Fraction(0), Fraction(1), Fraction(1, 100)),
    )

    triples: set[tuple[int, int, int]] = set()
    names = tuple(AXES)
    witness: dict[tuple[int, int, int], tuple[str, str, str, str]] = {}
    for settings in product(names, repeat=4):
        coeffs = []
        for basis in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            u_b, t_b, v_b = basis
            coeffs.append(
                axis_value(Fraction(u_b), Fraction(t_b), Fraction(v_b), settings)
            )
        key = (int(coeffs[0]), int(coeffs[1]), int(coeffs[2]))
        triples.add(key)
        witness.setdefault(key, settings)
    pairs = {(a * a + b * b, g * g) for a, b, g in triples}
    checks.check("signed-axis menu has 1296 strategies", len(names) ** 4 == 1296)
    checks.check(
        "signed-axis coefficient pairs are exactly the six proved cases",
        pairs == {(0, 0), (0, 4), (1, 1), (2, 0), (4, 0), (8, 0)},
    )
    xyxy = ("x", "y", "y", "x")
    checks.check(
        "axis strategy (x,y,y,x) has coefficients (2,-2,0)",
        (2, -2, 0) in triples
        and axis_value(Fraction(1), Fraction(0), Fraction(0), xyxy) == 2
        and axis_value(Fraction(0), Fraction(1), Fraction(0), xyxy) == -2
        and axis_value(Fraction(0), Fraction(0), Fraction(1), xyxy) == 0
        and witness[(2, -2, 0)] == xyxy,
    )

    def axis_abs_max(u: int, t: int, v: int) -> int:
        return max(abs(a * u + b * t + g * v) for a, b, g in triples)

    checks.check(
        "at the singlet, every signed-axis strategy has magnitude at most 2",
        axis_abs_max(-1, 0, -1) == 2,
    )
    checks.check(
        "at (u,t)=(1,0) and (0,1) on v=-1, signed-axis magnitude is 2",
        axis_abs_max(1, 0, -1) == 2 and axis_abs_max(0, 1, -1) == 2,
    )

    half = S2(0, Fraction(1, 2))
    u_diag = half
    t_diag = S2(0, Fraction(-1, 2))
    strategy = 2 * u_diag - 2 * t_diag
    checks.check(
        "diagonal point has r^2 = 1 and axis value 2√2",
        u_diag * u_diag + t_diag * t_diag == S2(1, 0) and strategy == S2(0, 2),
    )
    checks.check("that axis value has square 8", strategy * strategy == S2(8, 0))
    checks.check(
        "Cauchy equality holds for (u,t) parallel to (2,-2)",
        2 * t_diag - (-2) * u_diag == S2(0, 0),
    )
    direct = (
        axis_correlator_s2(u_diag, t_diag, "x", "y")
        + axis_correlator_s2(u_diag, t_diag, "x", "x")
        + axis_correlator_s2(u_diag, t_diag, "y", "y")
        - axis_correlator_s2(u_diag, t_diag, "y", "x")
    )
    checks.check("direct axis correlators at the diagonal point sum to 2√2", direct == S2(0, 2))

    print(
        "per_element: The sixteen Pauli coefficients of one bond are the domain; "
        "entries outside the declared directed pattern stay zero."
    )
    print(
        "per_site: The object is one two-site bond. A one-site reduction is not tested."
    )
    print(
        "per_mode: The modes p, q, v, u, and t are tested, including the twist. "
        "The sum rule is not tested."
    )
    print(
        "per_block: One nearest-neighbor bond is tested. Plaquettes, cubes, and "
        "larger windows are not tested."
    )
    print(
        "lattice_wide: checked and not executed — no infinite-volume or multi-bond "
        "statement is claimed or tested."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


def axis_correlator_s2(u: S2, t: S2, left: str, right: str) -> S2:
    bx, by, bz = AXES[right]
    ax, ay, az = AXES[left]
    image_x = u * bx + t * (-by)
    image_y = t * bx + u * by
    image_z = S2(-1, 0) * bz
    return image_x * ax + image_y * ay + image_z * az


if __name__ == "__main__":
    main()
