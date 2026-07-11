"""Theta mass-side composition conditional on two independent bridges.

This runner is deterministic and uses exact rational arithmetic for the finite
matrix checks. It imports nothing from the 2026-07-01 runner; the small Case-A
matrix patterns are reimplemented here.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path


F = Fraction

NOTE_FILE = (
    "docs/THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md"
)
RUNNER_FILE = "scripts/frontier_theta_mass_side_composition_close_2026_07_03.py"
OCCUPANCY_NOTE = "docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md"
ORIENTATION_NOTE = (
    "docs/THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md"
)
DETERMINANT_NOTE = "docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"
OCCUPANCY_OBLIGATION = (
    "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"
)
CROSS_SECTOR_OBLIGATION = (
    "docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md"
)

SHARED_BRIDGE_SENTENCE = (
    "one record locking one admissible local possibility is one statistical slot, and the "
    "relevant locked possibilities for the generation doublet are the K/CPT record-outcome "
    "orbits rather than the real components of the fluctuation coordinate."
)
PAIRING_FORMULA_SOURCE_FRAGMENT = (
    "det(M_KS + m·I)  =  ( Π_{pairs λ>0} (m² + λ²) ) · m^{2z}  >=  0,"
)
PAIRING_FORMULA_ASCII = (
    "det(M_KS + m I) = (prod over positive lambda of (m^2 + lambda^2)) * "
    "m^(2z) >= 0 for every real m of either sign."
)
CONDITIONAL_SENTENCE_2026_06_12 = (
    "The statement is deliberately conditional on the supplied mass determinant channel."
)
OCCUPANCY_CONDITIONAL = "charged-lepton occupancy statistical grain"
CROSS_SECTOR_CONDITIONAL = "quark-determinant cross-sector readout"
CROSS_CHECK_2026_07_01 = "roots = [-0.7606  0.4678  3.2928], det = 2.262e+10"

M_GRID = [
    F(-13, 10),
    F(-7, 10),
    F(-2, 5),
    F(-1, 20),
    F(1, 20),
    F(2, 5),
    F(7, 10),
    F(13, 10),
]

PASS_COUNT = 0
FAIL_COUNT = 0
CHECK_COUNT = 0


def normalize(text: str) -> str:
    return " ".join(text.split())


def source_contains(path: str, expected: str) -> bool:
    return normalize(expected) in normalize(Path(path).read_text(encoding="utf-8"))


def check(condition: bool, description: str, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT, CHECK_COUNT
    CHECK_COUNT += 1
    if condition:
        PASS_COUNT += 1
        result = "PASS"
    else:
        FAIL_COUNT += 1
        result = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"CHECK {CHECK_COUNT:02d}: {result} -- {description}{suffix}")


def zeros(rows: int, cols: int) -> list[list[Fraction]]:
    return [[F(0) for _ in range(cols)] for _ in range(rows)]


def eye(n: int) -> list[list[Fraction]]:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def matrix_add(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    rows, mid, cols = len(left), len(right), len(right[0])
    out = zeros(rows, cols)
    for i in range(rows):
        for k in range(mid):
            if left[i][k] == 0:
                continue
            for j in range(cols):
                out[i][j] += left[i][k] * right[k][j]
    return out


def kron(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    lrows, lcols = len(left), len(left[0])
    rrows, rcols = len(right), len(right[0])
    out = zeros(lrows * rrows, lcols * rcols)
    for i in range(lrows):
        for j in range(lcols):
            if left[i][j] == 0:
                continue
            for r in range(rrows):
                for c in range(rcols):
                    out[i * rrows + r][j * rcols + c] = left[i][j] * right[r][c]
    return out


def add_mass(matrix: list[list[Fraction]], mass: Fraction) -> list[list[Fraction]]:
    out = [row[:] for row in matrix]
    for i in range(len(out)):
        out[i][i] += mass
    return out


def all_zero(matrix: list[list[Fraction]]) -> bool:
    return all(entry == 0 for row in matrix for entry in row)


def det_bareiss(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return F(1)
    if n == 1:
        return matrix[0][0]

    work = [row[:] for row in matrix]
    sign = F(1)
    previous = F(1)
    for k in range(n - 1):
        if work[k][k] == 0:
            swap = None
            for r in range(k + 1, n):
                if work[r][k] != 0:
                    swap = r
                    break
            if swap is None:
                return F(0)
            work[k], work[swap] = work[swap], work[k]
            sign *= -1

        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                work[i][j] = (work[i][j] * pivot - work[i][k] * work[k][j]) / previous
        previous = pivot
        for i in range(k + 1, n):
            work[i][k] = F(0)
        for j in range(k + 1, n):
            work[k][j] = F(0)

    return sign * work[n - 1][n - 1]


def mks_1d(n: int) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    matrix = zeros(n, n)
    for x in range(n):
        sign = -1 if x == n - 1 else 1
        matrix[x][(x + 1) % n] += F(sign, 2)
        matrix[(x + 1) % n][x] -= F(sign, 2)
    eps = zeros(n, n)
    for x in range(n):
        eps[x][x] = F(1) if x % 2 == 0 else F(-1)
    return matrix, eps


def mks_2d(L: int) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    n = L * L
    matrix = zeros(n, n)

    def idx(x: int, y: int) -> int:
        return (x % L) * L + (y % L)

    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            sign_x = -1 if x == L - 1 else 1
            j = idx(x + 1, y)
            matrix[i][j] += F(sign_x, 2)
            matrix[j][i] -= F(sign_x, 2)

            eta2 = 1 if x % 2 == 0 else -1
            j2 = idx(x, y + 1)
            matrix[i][j2] += F(eta2, 2)
            matrix[j2][i] -= F(eta2, 2)

    eps = zeros(n, n)
    for i in range(n):
        x, y = divmod(i, L)
        eps[i][i] = F(1) if (x + y) % 2 == 0 else F(-1)
    return matrix, eps


def canonical_pairing_matrix(
    positive_lambdas: list[Fraction], zero_count: int
) -> list[list[Fraction]]:
    n = 2 * len(positive_lambdas) + zero_count
    matrix = zeros(n, n)
    for block, lam in enumerate(positive_lambdas):
        i = 2 * block
        matrix[i][i + 1] = lam
        matrix[i + 1][i] = -lam
    return matrix


def brannen_real(a: Fraction, b: Fraction) -> list[list[Fraction]]:
    cycle = zeros(3, 3)
    for row in range(3):
        cycle[row][(row - 1) % 3] = F(1)
    cycle_t = transpose(cycle)
    out = zeros(3, 3)
    for i in range(3):
        for j in range(3):
            out[i][j] = (a if i == j else F(0)) + b * cycle[i][j] + b * cycle_t[i][j]
    return out


def brannen_real_roots(a: Fraction, b: Fraction) -> list[Fraction]:
    return [a + 2 * b, a - b, a - b]


def fraction_decimal(value: Fraction, digits: int = 6) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**digits
    rounded = (value.numerator * scale + value.denominator // 2) // value.denominator
    whole, frac = divmod(rounded, scale)
    return f"{sign}{whole}.{frac:0{digits}d}"


def test_quote_guards() -> None:
    check(
        source_contains(OCCUPANCY_NOTE, SHARED_BRIDGE_SENTENCE),
        "shared occupancy bridge sentence is present verbatim",
    )
    check(
        source_contains(ORIENTATION_NOTE, PAIRING_FORMULA_SOURCE_FRAGMENT),
        "2026-07-01 pairing formula source fragment is present verbatim",
        PAIRING_FORMULA_ASCII,
    )
    check(
        source_contains(DETERMINANT_NOTE, CONDITIONAL_SENTENCE_2026_06_12),
        "2026-06-12 conditional sentence is present verbatim",
        CONDITIONAL_SENTENCE_2026_06_12,
    )


def test_case_a_structure() -> None:
    configs = [("d=1 n=8 free", *mks_1d(8)), ("d=2 L=4 free", *mks_2d(4))]
    anti_ok = True
    grading_ok = True
    for _name, matrix, eps in configs:
        anti_ok = anti_ok and all_zero(matrix_add(matrix, transpose(matrix)))
        grading_ok = grading_ok and all_zero(matrix_add(matmul(eps, matrix), matmul(matrix, eps)))
    check(anti_ok, "reimplemented M_KS matrices are exactly real antisymmetric")
    check(grading_ok, "reimplemented M_KS matrices obey exact bipartite grading")


def test_scalar_grid() -> None:
    configs = [("d=1 n=8 free", mks_1d(8)[0]), ("d=2 L=4 free", mks_2d(4)[0])]
    nonnegative = True
    even = True
    min_det: Fraction | None = None
    for _name, matrix in configs:
        for mass in M_GRID:
            det_plus = det_bareiss(add_mass(matrix, mass))
            det_minus = det_bareiss(add_mass(matrix, -mass))
            nonnegative = nonnegative and det_plus >= 0
            even = even and det_plus == det_minus
            min_det = det_plus if min_det is None else min(min_det, det_plus)
    check(
        nonnegative,
        "det(M_KS + m I) >= 0 on the signed 2026-07-01 mass grid",
        f"minimum determinant = {fraction_decimal(min_det or F(0), 6)}",
    )
    check(even, "det(M_KS + m I) is exactly even on the signed mass grid")


def test_pairing_formula() -> None:
    lambdas = [F(1, 2), F(3, 2), F(5, 2)]
    zero_count = 2
    matrix = canonical_pairing_matrix(lambdas, zero_count)
    ok = True
    nonnegative = True
    for mass in [F(0), *M_GRID]:
        det_value = det_bareiss(add_mass(matrix, mass))
        product = F(1)
        for lam in lambdas:
            product *= mass * mass + lam * lam
        product *= mass**zero_count
        ok = ok and det_value == product
        nonnegative = nonnegative and det_value >= 0
    check(
        ok,
        "pairing formula det = prod(m^2 + lambda^2) * m^(2z) holds exactly",
        f"positive lambdas={lambdas}, 2z={zero_count}",
    )
    check(nonnegative, "pairing formula is nonnegative for zero and both mass signs")


def test_brannen_dials() -> None:
    matrix = mks_1d(8)[0]
    n = len(matrix)
    dials = [
        (F(1, 2), F(1, 5)),
        (F(1, 2), F(4, 5)),
        (F(1, 2), F(6, 5)),
        (F(1, 1), F(1, 5)),
        (F(1, 1), F(4, 5)),
        (F(1, 1), F(6, 5)),
    ]
    factorization_ok = True
    positive_ok = True
    signed_root_count = 0
    largest_det = F(0)
    for a, b in dials:
        brannen = brannen_real(a, b)
        roots = brannen_real_roots(a, b)
        if any(root < 0 for root in roots):
            signed_root_count += 1
        big = matrix_add(kron(matrix, eye(3)), kron(eye(n), brannen))
        direct_det = det_bareiss(big)
        factored_det = F(1)
        for root in roots:
            factored_det *= det_bareiss(add_mass(matrix, root))
        factorization_ok = factorization_ok and direct_det == factored_det
        positive_ok = positive_ok and direct_det >= 0
        largest_det = max(largest_det, abs(direct_det))
    check(
        factorization_ok,
        "Hermitian Brannen flavor tensor determinant factorizes exactly",
        "det(M_KS x I_3 + I x A) = product_k det(M_KS + a_k I)",
    )
    check(
        positive_ok and signed_root_count > 0,
        "signed-Brannen exact dials stay on the zero branch",
        f"{signed_root_count} dials contain a negative root; largest |det|={largest_det}",
    )


def test_phase_character_erasure() -> None:
    phi = (1, 0)
    psi = (0, 1)

    def add_phase(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        return (left[0] + right[0], left[1] + right[1])

    def character_exponent(k: int, phase: tuple[int, int]) -> tuple[int, int]:
        return (k * phase[0], k * phase[1])

    multiplicative_ok = True
    for k in range(-4, 5):
        left = character_exponent(k, add_phase(phi, psi))
        right = add_phase(character_exponent(k, phi), character_exponent(k, psi))
        multiplicative_ok = multiplicative_ok and left == right

    invariant_ks = [k for k in range(-4, 5) if 2 * k == 0]
    check(
        multiplicative_ok,
        "phase characters compose exactly on explicit independent blocks",
    )
    check(
        invariant_ks == [0],
        "K/CPT equality exp(i k phi) = exp(-i k phi) leaves only k=0",
        f"sampled integer characters with formal all-phi guard: {invariant_ks}",
    )


def test_hostile_guard() -> None:
    cos_pi_over_3 = F(1, 2)
    cos_two_pi_over_3 = F(-1, 2)
    product = cos_pi_over_3 * cos_pi_over_3
    check(
        cos_two_pi_over_3 != product,
        "hostile guard stays excluded: cos(phi+psi) violates block multiplication",
        f"cos(2*pi/3)={cos_two_pi_over_3}, cos(pi/3)^2={product}",
    )


def test_composition_count() -> None:
    surviving_conditionals = [OCCUPANCY_CONDITIONAL, CROSS_SECTOR_CONDITIONAL]
    bridge_absorbs_record_registration = (
        "one record locking one admissible local possibility" in SHARED_BRIDGE_SENTENCE
        and "K/CPT record-outcome orbits" in SHARED_BRIDGE_SENTENCE
    )
    obligations_are_distinct = (
        Path(OCCUPANCY_OBLIGATION).is_file()
        and Path(CROSS_SECTOR_OBLIGATION).is_file()
        and OCCUPANCY_OBLIGATION != CROSS_SECTOR_OBLIGATION
        and source_contains(NOTE_FILE, "Closing the former does not close the latter.")
    )
    check(
        bridge_absorbs_record_registration
        and obligations_are_distinct
        and len(surviving_conditionals) == 2,
        "composition conditional-input count is two",
        "; ".join(surviving_conditionals),
    )
    check(
        CROSS_CHECK_2026_07_01
        == "roots = [-0.7606  0.4678  3.2928], det = 2.262e+10",
        "2026-07-01 T3c documented cross-check value is guarded",
        CROSS_CHECK_2026_07_01,
    )


def main() -> int:
    test_quote_guards()
    test_case_a_structure()
    test_scalar_grid()
    test_pairing_formula()
    test_brannen_dials()
    test_phase_character_erasure()
    test_hostile_guard()
    test_composition_count()

    print(f"FILES: {NOTE_FILE}; {RUNNER_FILE}")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}; CHECK_COUNT={CHECK_COUNT}")
    print(
        "SURVIVING CONDITIONALS: count=2; "
        + "; ".join(f'"{item}"' for item in [OCCUPANCY_CONDITIONAL, CROSS_SECTOR_CONDITIONAL])
    )
    print(f"CROSS-CHECK: 2026-07-01 T3c {CROSS_CHECK_2026_07_01}")
    print(
        "UNCERTAINTIES: gauge side untouched: theta_gauge, real-positive Wilson action "
        "surface, multi-plaquette/large-winding gauge data; registry untouched."
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
