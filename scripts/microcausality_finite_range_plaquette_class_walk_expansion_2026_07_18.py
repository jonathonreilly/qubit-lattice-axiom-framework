#!/usr/bin/env python3
"""Exact checks for the finite-range plaquette-class walk-expansion LR note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_FINITE_RANGE_PLAQUETTE_CLASS_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK03_NOTE = ROOT / (
    "docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
CT_NOTE = ROOT / (
    "docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_"
    "NARROW_THEOREM_NOTE_2026-06-13.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"

def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "G1", "G2", "G3", "G4", "G5", "G6",
    "R1", "R2",
    "M1", "M2", "M3", "M4",
    "Z1", "Z2", "Z3",
    "T1", "T2",
    "N1", "N2", "N3", "N4", "N5",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(n) in haystack for n in needles),
        )

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def add(p, q):
    return tuple(a + b for a, b in zip(p, q))


def terms_in_box(radius):
    """All bonds and faces whose sites lie in the centered box."""
    rng = range(-radius, radius + 1)
    bonds, faces = set(), set()
    for x in itertools.product(rng, repeat=3):
        for i in range(3):
            y = add(x, AXES[i])
            if all(-radius <= c <= radius for c in y):
                bonds.add(frozenset((x, y)))
            for j in range(i + 1, 3):
                y2 = add(x, AXES[j])
                y3 = add(y, AXES[j])
                quad = (x, y, y2, y3)
                if all(-radius <= c <= radius for pt in quad for c in pt):
                    faces.add(frozenset(quad))
    return bonds, faces


def site_index(terms):
    idx = {}
    for t in terms:
        for s in t:
            idx.setdefault(s, set()).add(t)
    return idx


def adjacent_terms(term, idx):
    out = set()
    for s in term:
        out |= idx[s]
    out.discard(term)
    return out


def l1(p, q):
    return sum(abs(a - b) for a, b in zip(p, q))


def geometry(radius):
    """Degrees for EVERY bond orientation (3) and face orientation (3)."""
    bonds, faces = terms_in_box(radius)
    allt = bonds | faces
    idx = site_index(allt)
    origin = (0, 0, 0)
    bond_reps = [frozenset((origin, AXES[i])) for i in range(3)]
    face_reps = []
    for i in range(3):
        for j in range(i + 1, 3):
            face_reps.append(
                frozenset((origin, AXES[i], AXES[j], add(AXES[i], AXES[j])))
            )
    bond_rows = []
    for b in bond_reps:
        nb = adjacent_terms(b, idx)
        bond_rows.append(
            (
                len([t for t in nb if len(t) == 2]),
                len([t for t in nb if len(t) == 4]),
            )
        )
    face_rows = []
    for f in face_reps:
        nf = adjacent_terms(f, idx)
        face_rows.append(
            (
                len([t for t in nf if len(t) == 2]),
                len([t for t in nf if len(t) == 4]),
            )
        )
    stats = {
        "bonds_per_site": len([t for t in idx[origin] if len(t) == 2]),
        "faces_per_site": len([t for t in idx[origin] if len(t) == 4]),
        "bond_rows": bond_rows,
        "face_rows": face_rows,
    }
    return stats, idx, origin


def main():
    checks = CheckRunner()

    stats4, idx4, origin = geometry(4)
    stats5, idx5, _ = geometry(5)

    # Group G -- exhaustive geometry, box-stable.
    checks.check(
        "G1 terms per site: 6 bonds and 12 faces (radii 4 and 5)",
        stats4["bonds_per_site"] == 6
        and stats4["faces_per_site"] == 12
        and stats5["bonds_per_site"] == 6
        and stats5["faces_per_site"] == 12,
    )
    checks.check(
        "G2 bond degrees: (10 bonds, 20 faces) for EVERY bond "
        "orientation (radii 4 and 5)",
        stats4["bond_rows"] == [(10, 20)] * 3
        and stats5["bond_rows"] == [(10, 20)] * 3,
    )
    ie = 4 * 12 - (4 * 4 + 2 * 1) + 4 * 1 - 1
    checks.check(
        "G3 face degrees: (20 bonds, 32 faces) for EVERY face "
        "orientation, box-stable, and the hand inclusion-exclusion "
        "48-18+4-1 = 33 minus self = 32 agrees",
        stats4["face_rows"] == [(20, 32)] * 3
        and stats5["face_rows"] == [(20, 32)] * 3
        and ie == 33
        and ie - 1 == 32,
    )
    diam = lambda t: max(l1(p, q) for p in t for q in t)
    b0 = frozenset(((0, 0, 0), (1, 0, 0)))
    f0 = frozenset(((0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)))
    checks.check(
        "G4 support diameters: bond 1, face 2",
        diam(b0) == 1 and diam(f0) == 2,
    )
    starts = sorted(idx5[origin], key=lambda t: sorted(t))
    walks2 = [
        (t1, t2) for t1 in starts for t2 in adjacent_terms(t1, idx5)
    ]
    checks.check(
        "G5 mixed length-2 walks from one site: 804 <= 936 = 18*52",
        len(starts) == 18 and len(walks2) == 804 and 804 <= 18 * 52,
    )
    max_d1 = max(
        l1(origin, s) for t1 in starts for s in t1
    )
    max_d2 = max(l1(origin, s) for _, t2 in walks2 for s in t2)
    max_d3 = 0
    for _, t2 in walks2:
        for t3 in adjacent_terms(t2, idx5):
            for s in t3:
                dd = l1(origin, s)
                if dd > max_d3:
                    max_d3 = dd
    checks.check(
        "G6 reach is exactly 2k at k = 1, 2, 3",
        max_d1 == 2 and max_d2 == 4 and max_d3 == 6,
    )

    # Group R -- series start and sharpness.
    ceil_ok = all(
        sp.ceiling(sp.Rational(d, 2)) == expect
        and 2 * (expect - 1) < d <= 2 * expect
        for d, expect in ((1, 1), (2, 1), (3, 2), (4, 2), (5, 3))
    )
    r_int = sp.Symbol("r_int", integer=True, positive=True)
    even_case = sp.ceiling(2 * r_int / 2) == r_int
    odd_ceiling = sp.ceiling((2 * r_int + 1) / sp.Integer(2))
    odd_case = sp.simplify(odd_ceiling - (r_int + 1)) == 0
    boundary = (2 * (r_int + 1) >= 2 * r_int + 1) == True
    failing = sp.simplify((2 * r_int) - (2 * r_int + 1)) == -1
    checks.check(
        "R1 series start: 2k >= d iff k >= ceil(d/2) — symbolic even/odd "
        "ceiling cases with the k = r boundary failure, plus instances "
        "d = 1..5",
        ceil_ok
        and bool(even_case)
        and bool(odd_case)
        and bool(boundary)
        and bool(failing),
    )
    I2 = sp.eye(2)
    SX = sp.Matrix([[0, 1], [1, 0]])
    SZ = sp.Matrix([[1, 0], [0, -1]])

    def kron(*mats):
        out = mats[0]
        for m in mats[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out

    def com(a, b):
        return a * b - b * a

    def is_zero(m):
        return sp.simplify(m) == sp.zeros(*m.shape)

    face_term = kron(SX, SX, SX, SX)
    z_corner = kron(SZ, I2, I2, I2)
    z_opposite = kron(I2, I2, I2, SZ)
    checks.check(
        "R2 face-jump sharpness: one adjoint step reaches distance 2 "
        "(k=0 commutes, k=1 does not)",
        is_zero(com(z_corner, z_opposite))
        and not is_zero(com(com(face_term, z_corner), z_opposite)),
    )

    # Group M -- mixed-dimension chain (dims 2, 3, 2).
    I3 = sp.eye(3)
    Q = sp.diag(1, 2, 3)
    Qp = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])

    def kron3(a, b, c):
        return sp.Matrix(
            sp.kronecker_product(sp.kronecker_product(a, b), c)
        )

    h12 = kron3(SX, Q, I2)
    h23 = kron3(I2, Qp, SX)
    ham = h12 + h23
    a1 = kron3(SZ, I3, I2)
    z3 = kron3(I2, I3, SZ)
    checks.check(
        "M1 mixed-dim reduction: [h23, A] = 0 and [H, A] = [h12, A] != 0",
        is_zero(com(h23, a1))
        and is_zero(com(ham, a1) - com(h12, a1))
        and not is_zero(com(h12, a1)),
    )
    ad1 = com(ham, a1)
    ad2 = com(ham, ad1)
    checks.check(
        "M2 mixed-dim cone: k = 0, 1 below (d = 2), k = 2 arrives",
        is_zero(com(a1, z3))
        and is_zero(com(ad1, z3))
        and not is_zero(com(ad2, z3)),
    )
    checks.check(
        "M3 mixed-dim terms Hermitian with exact Kronecker norms "
        "(||X ⊗ diag(1,2,3)|| = 3)",
        is_zero(h12 - h12.H)
        and is_zero(h23 - h23.H)
        and sp.simplify(max((h12.H * h12).eigenvals()) - 9) == 0,
    )

    def kron_list(ms):
        out = ms[0]
        for m_ in ms[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m_))
        return out

    face_mixed = kron_list([SX, Q, SX, SX, I2])
    z_c1 = kron_list([SZ, I3, I2, I2, I2])
    z_c4 = kron_list([I2, I3, I2, SZ, I2])
    z_far = kron_list([I2, I3, I2, I2, SZ])
    checks.check(
        "M4 mixed-dim FOUR-SITE face term: Hermitian, commutes with the "
        "far factor, and one adjoint step reaches the opposite corner",
        is_zero(face_mixed - face_mixed.H)
        and is_zero(com(face_mixed, z_far))
        and is_zero(com(z_c1, z_c4))
        and not is_zero(com(com(face_mixed, z_c1), z_c4)),
    )

    # Group Z -- Z2 KS-shaped instance (factors l1, l3, l2, l4, l5).
    def kron5(ms):
        out = ms[0]
        for m in ms[1:]:
            out = sp.Matrix(sp.kronecker_product(out, m))
        return out

    def op_on(which, mat):
        mats = [I2] * 5
        mats[which] = mat
        return kron5(mats)

    # factor order: 0 = l1, 1 = l3 (both at site v00), 2 = l2 (v10),
    # 3 = l4 (v01), 4 = l5 (far site w)
    b_p = kron5([SX, I2, SX, SX, I2]) * op_on(1, SX)
    e_l1 = op_on(0, SZ)
    checks.check(
        "Z1 magnetic plaquette term is face-supported: commutes with "
        "every operator on the far link",
        is_zero(com(b_p, op_on(4, SZ))) and is_zero(com(b_p, op_on(4, SX))),
    )
    checks.check(
        "Z2 electric link term is bond-supported: commutes with "
        "operators on l2, l4, l5",
        is_zero(com(e_l1, op_on(2, SX)))
        and is_zero(com(e_l1, op_on(3, SX)))
        and is_zero(com(e_l1, op_on(4, SX))),
    )
    checks.check(
        "Z3 the gauge dynamics is nontrivial: [B_p, E_l1] != 0",
        not is_zero(com(b_p, e_l1)),
    )

    # Group T -- assembly.
    j_sym, n_sym, k_sym = sp.symbols("j_sym n_sym k_sym", positive=True)
    checks.check(
        "T1 coefficient assembly (2J)^k n 52^(k-1) = (n/52)(104J)^k",
        sp.simplify(
            (2 * j_sym) ** k_sym * n_sym * 52 ** (k_sym - 1)
            - (n_sym / sp.Integer(52)) * (104 * j_sym) ** k_sym
        )
        == 0,
    )
    x_val = sp.Rational(3, 2)
    tail_lhs = sum(x_val**k / sp.factorial(k) for k in range(2, 40))
    tail_rhs = x_val**2 / 2 * sp.exp(x_val)
    k5, d2 = 5, 2
    checks.check(
        "T2 tail mechanism re-gate: binomial domination d!/k! <= 1/(k-d)! "
        "plus an exact 38-term partial-sum instance below the closed form",
        sp.binomial(k5, d2) >= 1
        and sp.Rational(sp.factorial(d2), sp.factorial(k5))
        <= sp.Rational(1, sp.factorial(k5 - d2))
        and sp.simplify(tail_rhs - tail_lhs).is_positive is True,
    )

    # Group N -- source needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 CT note names the U-integrated case open (its own words)",
        CT_NOTE,
        "The `U`-integrated / dynamical gauge-measure case — the "
        "fixed-`U` resolvent bound does not control gauge-field "
        "correlations; **open**.",
    )
    checks.needle(
        "N2 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N3 sibling chain authorities",
        BLOCK03_NOTE,
        (
            "microcausality_all_time_volume_uniform_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**G6 (theorem: all-time volume-uniform Lieb-Robinson bound).**",
            "obtained by the `H → −H` symmetry",
        ),
    )
    checks.needle(
        "N4 target identifiers, theorem, non-sharpness, non-claims",
        TARGET_NOTE,
        (
            "microcausality_finite_range_plaquette_class_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Theorem (finite-range all-time volume-uniform "
            "Lieb-Robinson bound).**",
            "**Neither `104J` (the class activity scale) nor `208eJ` is "
            "claimed sharp**",
            "no gauge measure is integrated",
            "`d = d(X, Y) ≥ 1` as the standing scoping hypothesis",
        ),
    )
    checks.needle(
        "N5 No-Go section structure: all eight items and the Status line",
        TARGET_NOTE,
        (
            "**N1 route inventory (residuals first).**",
            "**N2 hypothesis independence (pairwise).**",
            "**N3 hidden-wall scan.**",
            "**N4 dependency roles, per citation",
            "**N5 rhetoric audit.**",
            "**N6 partial-closure scan.**",
            "**N7 steelman (strongest counterarguments, answered).**",
            "**N8 prior-wall echo.**",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
