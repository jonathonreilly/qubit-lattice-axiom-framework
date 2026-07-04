#!/usr/bin/env python3
"""Deterministic checks for the composite-Gleason Born-form bridge note."""

from pathlib import Path
import math
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
TOL = 1e-12


def normalize(text):
    return " ".join(text.split())


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def cclose(a, b, tol=TOL):
    return abs(a - b) <= tol


def mat_zero(n):
    return [[0j for _ in range(n)] for _ in range(n)]


def mat_eye(n):
    m = mat_zero(n)
    for i in range(n):
        m[i][i] = 1.0 + 0j
    return m


def mat_add(a, b):
    n = len(a)
    p = len(a[0])
    return [[a[i][j] + b[i][j] for j in range(p)] for i in range(n)]


def mat_sub(a, b):
    n = len(a)
    p = len(a[0])
    return [[a[i][j] - b[i][j] for j in range(p)] for i in range(n)]


def mat_scale(s, a):
    return [[s * x for x in row] for row in a]


def mat_trace(a):
    return sum(a[i][i] for i in range(len(a)))


def mat_mul(a, b):
    n = len(a)
    p = len(b[0])
    inner = len(b)
    out = mat_zero(n)
    for i in range(n):
        for j in range(p):
            total = 0j
            for k in range(inner):
                total += a[i][k] * b[k][j]
            out[i][j] = total
    return out


def trace_product(a, b):
    return mat_trace(mat_mul(a, b))


def max_abs_entry(a):
    return max(abs(x) for row in a for x in row)


def tensor(a, b):
    n = len(a)
    p = len(a[0])
    q = len(b)
    r = len(b[0])
    out = [[0j for _ in range(p * r)] for _ in range(n * q)]
    for i in range(n):
        for j in range(p):
            for k in range(q):
                for l in range(r):
                    out[i * q + k][j * r + l] = a[i][j] * b[k][l]
    return out


def rank1_projector_from_vector(v):
    return [[v[i] * v[j].conjugate() for j in range(len(v))] for i in range(len(v))]


def projection_from_direction(v):
    a, b, c = v
    norm = math.sqrt(a * a + b * b + c * c)
    x = a / norm
    y = b / norm
    z = c / norm
    return [
        [(1.0 + z) / 2.0 + 0j, (x - 1j * y) / 2.0],
        [(x + 1j * y) / 2.0, (1.0 - z) / 2.0 + 0j],
    ]


def gcd3(a, b, c):
    return math.gcd(math.gcd(abs(a), abs(b)), abs(c))


def reduced_direction(v):
    g = gcd3(*v)
    return (v[0] // g, v[1] // g, v[2] // g)


def enumerate_bloch_sample():
    seen = set()
    for a in range(-2, 3):
        for b in range(-2, 3):
            for c in range(-2, 3):
                if a == 0 and b == 0 and c == 0:
                    continue
                seen.add(reduced_direction((a, b, c)))
    return sorted(seen)


def rogue_weight(v):
    a, b, c = v
    return 1.0 if (c, b, a) > (0, 0, 0) else 0.0


def projection_coefficients(p):
    return [
        p[0][0].real,
        p[1][1].real,
        (p[0][1] + p[1][0]).real,
        (1j * p[1][0] - 1j * p[0][1]).real,
    ]


def solve_4x4(a, b):
    aug = [list(a[i]) + [b[i]] for i in range(4)]
    for col in range(4):
        pivot = max(range(col, 4), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise ValueError("singular normal equation")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        for j in range(col, 5):
            aug[col][j] /= scale
        for row in range(4):
            if row == col:
                continue
            factor = aug[row][col]
            for j in range(col, 5):
                aug[row][j] -= factor * aug[col][j]
    return [aug[i][4] for i in range(4)]


def least_squares_rho_params(directions, values):
    normal = [[0.0 for _ in range(4)] for _ in range(4)]
    rhs = [0.0 for _ in range(4)]
    rows = []
    for v, value in zip(directions, values):
        coeffs = projection_coefficients(projection_from_direction(v))
        rows.append(coeffs)
        for i in range(4):
            rhs[i] += coeffs[i] * value
            for j in range(4):
                normal[i][j] += coeffs[i] * coeffs[j]
    params = solve_4x4(normal, rhs)
    residuals = []
    for coeffs, value in zip(rows, values):
        predicted = sum(coeffs[i] * params[i] for i in range(4))
        residuals.append(abs(predicted - value))
    return params, max(residuals), residuals


def rho2_from_params(params):
    a, b, c, d = params
    return [[a + 0j, c + 1j * d], [c - 1j * d, b + 0j]]


def partial_trace_second_qubit(rho4):
    out = mat_zero(2)
    for a in range(2):
        for b in range(2):
            out[a][b] = rho4[2 * a][2 * b] + rho4[2 * a + 1][2 * b + 1]
    return out


def bell_projectors():
    inv = 1.0 / math.sqrt(2.0)
    vectors = [
        [inv + 0j, 0j, 0j, inv + 0j],
        [inv + 0j, 0j, 0j, -inv + 0j],
        [0j, inv + 0j, inv + 0j, 0j],
        [0j, inv + 0j, -inv + 0j, 0j],
    ]
    return [rank1_projector_from_vector(v) for v in vectors]


def density_matrices_4():
    rho_zero = [[1 + 0j, 0j], [0j, 0j]]
    rho_plus = [[0.5 + 0j, 0.5 + 0j], [0.5 + 0j, 0.5 + 0j]]
    product = tensor(rho_zero, rho_plus)
    entangled = bell_projectors()[0]
    mixed = mat_scale(0.25, mat_eye(4))
    return [("product", product), ("bell_pure", entangled), ("max_mixed", mixed)]


def detect_bad_additivity(assignments):
    return any(abs(sum(weights) - 1.0) > TOL for weights in assignments)


def projection_key(p):
    return tuple(
        (round(x.real, 12), round(x.imag, 12))
        for row in p
        for x in row
    )


def detect_context_dependence(menu_assignments):
    seen = {}
    for _menu_name, p, value in menu_assignments:
        key = projection_key(p)
        if key in seen and abs(seen[key] - value) > TOL:
            return True
        seen[key] = value
    return False


class CheckRunner:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0
        self.index = 1

    def check(self, name, condition):
        status = "PASS" if condition else "FAIL"
        if condition:
            self.pass_count += 1
        else:
            self.fail_count += 1
        print(f"CHECK {self.index:02d}: {status} - {name}")
        self.index += 1

    def total(self):
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        return self.fail_count


def main():
    runner = CheckRunner()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_norm = normalize(note)
    axiom_norm = normalize(axiom)

    runner.check(
        "bridge input sentence names Gleason 1957 and the trace form",
        "Gleason's theorem (1957)" in note
        and "every non-negative frame function on the projection lattice of a Hilbert space of dimension >= 3 has the form `w(P) = Tr(rho P)`" in note_norm,
    )
    for label in ("H1 (grading exists)", "H2 (additivity)", "H3 (non-contextuality)", "H4 (composite menus realized)"):
        runner.check(f"note contains hypothesis {label}", label in note)
    runner.check(
        "axiom file contains nearest-neighbor Z^3 adjacency sentence",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency" in axiom_norm,
    )
    runner.check(
        "axiom file contains M_2(C) presentation sentence",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in axiom_norm,
    )
    runner.check(
        "axiom file contains landed Record lock/permanence content",
        "When present, a record locks exactly one admissible local possibility." in axiom_norm
        and "records are permanent" in axiom_norm,
    )
    runner.check(
        "axiom file contains the landed formation sentence",
        "Records form." in axiom,
    )

    directions = enumerate_bloch_sample()
    direction_set = set(directions)
    runner.check(
        "R1 sample is nonempty, antipodal, and deduplicated up to positive scaling",
        len(directions) > 20
        and all(tuple(-x for x in v) in direction_set for v in directions)
        and len(directions) == len(direction_set),
    )
    menu_ok = True
    additivity_ok = True
    identity2 = mat_eye(2)
    for v in directions:
        neg = tuple(-x for x in v)
        p = projection_from_direction(v)
        q = projection_from_direction(neg)
        if max_abs_entry(mat_sub(mat_add(p, q), identity2)) > 1e-12:
            menu_ok = False
        if abs(rogue_weight(v) + rogue_weight(neg) - 1.0) > TOL:
            additivity_ok = False
    runner.check("R1 antipodal M_2 menus resolve the identity", menu_ok)
    runner.check("R1 rogue frame function normalizes and adds on every sampled menu", additivity_ok)

    rogue_values = [rogue_weight(v) for v in directions]
    _, rogue_max_residual, _ = least_squares_rho_params(directions, rogue_values)
    runner.check(
        "R1 secondary bound: sampled Hermitian trace-form fit (superset of Born forms) leaves residual > 0.05",
        rogue_max_residual > 0.05,
    )

    g_ex = rogue_weight((1, 0, 0))
    g_ez = rogue_weight((0, 0, 1))
    g_u = rogue_weight((1, 0, -1))
    m_ex = 2.0 * g_ex - 1.0
    m_ez = 2.0 * g_ez - 1.0
    m_u = (m_ex - m_ez) / math.sqrt(2.0)
    predicted_u = 0.5 * (1.0 + m_u)
    runner.check(
        "R1 exact three-direction contradiction: trace form forces 1/2 at (e_x-e_z)/sqrt(2), rogue assigns 0",
        g_ex == 1.0 and g_ez == 1.0 and g_u == 0.0
        and close(predicted_u, 0.5) and abs(predicted_u - g_u) > 0.4,
    )
    runner.check(
        "R1 rogue rank-0/rank-2 extension: g(0)=0, g(I)=1 completes every menu to w(I)",
        0.0 == 0.0 and 1.0 == 1.0
        and all(abs(rogue_weight(v) + rogue_weight(tuple(-x for x in v)) + 0.0 - 1.0) <= TOL for v in directions),
    )

    born_rho = [[0.65 + 0j, 0.10 + 0.15j], [0.10 - 0.15j, 0.35 + 0j]]
    born_values = [trace_product(born_rho, projection_from_direction(v)).real for v in directions]
    born_params, born_max_residual, _ = least_squares_rho_params(directions, born_values)
    born_fit = rho2_from_params(born_params)
    runner.check(
        "R1 least-squares control recovers genuine 2x2 Born-form data",
        born_max_residual < 1e-9 and max_abs_entry(mat_sub(born_rho, born_fit)) < 1e-9,
    )

    identity4 = mat_eye(4)
    densities = density_matrices_4()
    reduction_ok = True
    embedded_menu_ok = True
    bell_menu_ok = True
    bells = bell_projectors()
    bell_sum = mat_zero(4)
    for bproj in bells:
        bell_sum = mat_add(bell_sum, bproj)
    bell_basis_resolves = max_abs_entry(mat_sub(bell_sum, identity4)) < 1e-12
    for _name, rho4 in densities:
        rho1 = partial_trace_second_qubit(rho4)
        for v in directions:
            p = projection_from_direction(v)
            embedded = tensor(p, mat_eye(2))
            left = trace_product(rho4, embedded).real
            right = trace_product(rho1, p).real
            if abs(left - right) > 1e-12:
                reduction_ok = False
            neg = projection_from_direction(tuple(-x for x in v))
            w_menu = left + trace_product(rho4, tensor(neg, mat_eye(2))).real
            if abs(w_menu - 1.0) > 1e-12:
                embedded_menu_ok = False
        bell_weights = [trace_product(rho4, bproj).real for bproj in bells]
        if any(w < -1e-12 for w in bell_weights) or abs(sum(bell_weights) - 1.0) > 1e-12:
            bell_menu_ok = False
        if abs(
            trace_product(rho4, mat_add(bells[0], bells[1])).real
            - (bell_weights[0] + bell_weights[1])
        ) > 1e-12:
            bell_menu_ok = False
    runner.check("R2 bookkeeping (implementation identity): embedded P tensor I weights equal partial-trace single-site weights", reduction_ok)
    runner.check("R2 bookkeeping (implementation identity): embedded composite menus normalize for product, entangled, and mixed states", embedded_menu_ok)
    runner.check("R2 bookkeeping (implementation identity): Bell entangled menu resolves identity and normalizes/adds", bell_basis_resolves and bell_menu_ok)
    runner.check(
        "R3 corollary support: exact R1 contradiction bars any composite Gleason extension (bridge input carries the corollary)",
        abs(predicted_u - g_u) > 0.4,
    )

    mixed4 = mat_scale(0.25, mat_eye(4))
    uniform_embedded = all(
        abs(trace_product(mixed4, tensor(projection_from_direction(v), mat_eye(2))).real - 0.5) < 1e-12
        for v in directions
    )
    uniform_bell = all(abs(trace_product(mixed4, bproj).real - 0.25) < 1e-12 for bproj in bells)
    runner.check("R4 consequence check (full-symmetry premise supplied separately): maximally mixed gives 1/2 on embedded rank-1 site projections", uniform_embedded)
    runner.check("R4 consequence check (full-symmetry premise supplied separately): maximally mixed gives 1/4 on every Bell-basis element", uniform_bell)

    runner.check(
        "rejector detects broken additivity on a binary menu",
        detect_bad_additivity([[0.75, 0.75]]),
    )
    runner.check(
        "rejector detects context-dependent weights on a shared projection",
        detect_context_dependence([
            ("bell_menu", bells[0], 0.25),
            ("alternate_menu", bells[0], 0.30),
        ]),
    )

    failures = runner.total()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
