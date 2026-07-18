#!/usr/bin/env python3
"""Exact checks for the matrix-fiber trace-norm lemma and feed note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_MATRIX_FIBER_TRACE_NORM_LEMMA_AND_FEED_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK08_NOTE = ROOT / (
    "docs/MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK07_NOTE = ROOT / (
    "docs/MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK04_NOTE = ROOT / (
    "docs/MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_LABELS = [
    "M1", "M1b", "M2", "M3", "M4", "M5", "M6", "M7",
    "N1", "N2", "N3", "N4", "N6", "N5",
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


I2 = sp.eye(2)
ANN = sp.Matrix([[0, 1], [0, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def c_op(j, n):
    return kron(*([SZ] * j + [ANN] + [I2] * (n - j - 1)))


def com(a, b):
    return a * b - b * a


def acom(a, b):
    return a * b + b * a


def is_zero(m):
    return sp.simplify(m) == sp.zeros(*m.shape)


def op_norm(m):
    return sp.sqrt(max((m.H * m).eigenvals()))


def main():
    checks = CheckRunner()

    # Four modes: 0,1 = site-x fibers; 2,3 = site-y fibers.
    n_modes = 4
    c = [c_op(j, n_modes) for j in range(n_modes)]
    cd = [m.H for m in c]

    def pair_term(k):
        T = sp.zeros(2**n_modes, 2**n_modes)
        for a in range(2):
            for b in range(2):
                T += k[a, b] * cd[a] * c[2 + b]
        return T + T.H

    # M1 -- the pair trace-norm lemma on seven instances.
    instances = [
        sp.Matrix([[1, 0], [0, 0]]),
        sp.Matrix([[0, 1], [0, 0]]),
        sp.Matrix([[1, 1], [0, 0]]),
        sp.eye(2),
        sp.Matrix([[1, 0], [0, 2]]),
        sp.Matrix([[1, 1], [1, -1]]),
        sp.Matrix([[2, 1], [0, 1]]),
        sp.Matrix([[sp.I, 1], [0, 2]]),
    ]
    lemma_ok = True
    nonnormal_val = None
    for k in instances:
        lhs = op_norm(pair_term(k))
        rhs = sum(sp.Matrix(k).singular_values())
        if sp.simplify(lhs - rhs) != 0:
            lemma_ok = False
    nonnormal_val = sp.simplify(op_norm(pair_term(instances[6])))
    complex_val = sp.simplify(op_norm(pair_term(instances[7])))
    checks.check(
        "M1 pair trace-norm lemma ||T + T^H|| = ||k||_S1 on eight "
        "instances incl. non-normal ([[2,1],[0,1]]: both sides sqrt(10)), "
        "a COMPLEX kernel, and identity fiber (both sides 2 > op norm 1)",
        lemma_ok
        and sp.simplify(nonnormal_val - sp.sqrt(10)) == 0
        and sp.simplify(
            complex_val
            - sum(sp.Matrix(instances[7]).singular_values())
        )
        == 0
        and sp.simplify(op_norm(pair_term(sp.eye(2))) - 2) == 0,
    )

    # M1b -- n_f = 3 with DEGENERATE singular values (2, 2, 1/2):
    # six modes, norm = 9/2 via explicit eigenvector + triangle bound
    # (no 64x64 eigendecomposition needed).
    n6 = 6
    c6 = [c_op(j, n6) for j in range(n6)]
    cd6 = [m.H for m in c6]
    sigs = [sp.Integer(2), sp.Integer(2), sp.Rational(1, 2)]
    # ADJACENT mode pairs (2i, 2i+1): no JW string inside a pair, so
    # the product plus-combination is an explicit top eigenvector.
    T6 = sp.zeros(2**n6, 2**n6)
    for i, s in enumerate(sigs):
        T6 += s * (cd6[2 * i] * c6[2 * i + 1] + cd6[2 * i + 1] * c6[2 * i])
    vec = sp.zeros(2**n6, 1)
    for bits in range(8):
        idx = 0
        for i in range(3):
            occ_first = (bits >> i) & 1
            mode = 2 * i if occ_first else 2 * i + 1
            idx |= 1 << (n6 - 1 - mode)
        vec[idx] = 1
    tv = T6 * vec
    target = sum(sigs) * vec
    hop_norms_ok = all(
        sp.simplify(
            op_norm(
                s * (cd6[2 * i] * c6[2 * i + 1] + cd6[2 * i + 1] * c6[2 * i])
            )
            - s
        )
        == 0
        for i, s in enumerate(sigs)
    )
    checks.check(
        "M1b n_f = 3 with degenerate singular values (2, 2, 1/2): "
        "explicit eigenvector achieves 9/2 and the triangle bound "
        "matches, so ||T|| = ||k||_S1 = 9/2 without 64x64 "
        "eigendecomposition",
        sp.simplify(sp.expand(tv - target)) == sp.zeros(2**n6, 1)
        and hop_norms_ok
        and sum(sigs) == sp.Rational(9, 2),
    )

    # M2 -- mode rotation preserves the CAR (rational orthogonal).
    u = sp.Rational(1, 5) * sp.Matrix([[3, 4], [-4, 3]])
    C1 = u[0, 0] * c[0] + u[0, 1] * c[1]
    C2 = u[1, 0] * c[0] + u[1, 1] * c[1]
    car_ok = (
        is_zero(acom(C1, C2))
        and is_zero(acom(C1, C1.H) - sp.eye(2**n_modes))
        and is_zero(acom(C2, C2.H) - sp.eye(2**n_modes))
        and is_zero(acom(C1, C2.H))
    )
    uc = sp.Matrix([[sp.Rational(3, 5), 4 * sp.I / 5],
                    [sp.Rational(4, 5), -3 * sp.I / 5]])
    D1 = sp.conjugate(uc[0, 0]) * c[0] + sp.conjugate(uc[1, 0]) * c[1]
    D2 = sp.conjugate(uc[0, 1]) * c[0] + sp.conjugate(uc[1, 1]) * c[1]
    car_cplx = (
        is_zero(sp.expand(uc.H * uc - sp.eye(2)))
        and is_zero(acom(D1, D2))
        and is_zero(acom(D1, D1.H) - sp.eye(2**n_modes))
        and is_zero(acom(D2, D2.H) - sp.eye(2**n_modes))
        and is_zero(acom(D1, D2.H))
    )
    checks.check(
        "M2 particle-conserving mode rotations preserve the CAR: real "
        "orthogonal AND complex unitary instances, all anticommutators "
        "recomputed",
        car_ok and car_cplx,
    )

    # M3 -- rotated hops: disjoint-mode commutation, spectrum, sum norm.
    s1v, s2v = sp.Integer(1), sp.Integer(2)
    hop1 = cd[0] * c[2] + cd[2] * c[0]
    hop2 = cd[1] * c[3] + cd[3] * c[1]
    spec1 = set((s1v * hop1).eigenvals().keys())
    joint = set((s1v * hop1 + s2v * hop2).eigenvals().keys())
    expected_joint = {
        a + b for a in (-s1v, sp.Integer(0), s1v)
        for b in (-s2v, sp.Integer(0), s2v)
    }
    checks.check(
        "M3 rotated-hop structure: disjoint-mode hops commute, single "
        "hop spectrum {-s, 0, s}, FULL joint spectrum = all sums, and "
        "the sum's norm adds (1 + 2 = 3)",
        is_zero(com(hop1, hop2))
        and spec1 == {-s1v, sp.Integer(0), s1v}
        and joint == expected_joint
        and sp.simplify(op_norm(s1v * hop1 + s2v * hop2) - 3) == 0,
    )

    # M4 -- on-site strictness and saturation.
    n_site = 2
    csx = [c_op(j, n_site) for j in range(n_site)]
    cdx = [m.H for m in csx]

    def onsite(k):
        T = sp.zeros(2**n_site, 2**n_site)
        for a in range(2):
            for b in range(2):
                T += k[a, b] * cdx[a] * csx[b]
        return T

    checks.check(
        "M4 on-site bound: diag(1,-1) gives norm 1 < S1 = 2 (strict); "
        "diag(1,2) gives norm 3 = S1 (saturated)",
        sp.simplify(op_norm(onsite(sp.diag(1, -1))) - 1) == 0
        and sp.simplify(op_norm(onsite(sp.diag(1, 2))) - 3) == 0
        and sum(abs(e) for e in (1, -1)) == 2
        and sum(abs(e) for e in (1, 2)) == 3,
    )

    # M5 -- S1 <= n_f * op with identity-fiber attainment.
    k_nn = instances[6]
    svals = sp.Matrix(k_nn).singular_values()
    s1_nn = sum(svals)
    op_nn = max(svals)
    id_svals = sp.eye(2).singular_values()
    checks.check(
        "M5 S1 <= n_f * op (instances) with equality at the identity "
        "fiber (2 = 2 * 1)",
        sp.simplify(s1_nn - 2 * op_nn).is_nonpositive is True
        and sum(id_svals) == 2
        and max(id_svals) == 1
        and sum(id_svals) == 2 * max(id_svals),
    )

    # M6 -- evenness of fiber bilinears.
    parity4 = kron(SZ, SZ, SZ, SZ)
    parity2 = kron(SZ, SZ)
    checks.check(
        "M6 fiber terms are even (pair terms vs total parity, non-normal "
        "and complex instances; on-site term vs site parity)",
        is_zero(com(pair_term(instances[6]), parity4))
        and is_zero(com(pair_term(instances[7]), parity4))
        and is_zero(com(onsite(sp.diag(1, -1)), parity2)),
    )

    # M7 -- the n_f-scaled envelope arithmetic.
    n_f = sp.Symbol("n_f", positive=True, integer=True)
    series_146 = 2 * sp.Rational(1, 2) * (
        13 + 10 * sp.Rational(1, 2) + sp.Rational(1, 4)
    ) / (1 - sp.Rational(1, 2)) ** 3
    inherited_env = n_f * (1 + 4 * series_146)
    direct_env = n_f * (1 + 2 * series_146)
    checks.check(
        "M7 both fiber envelopes at x = 1/2: direct exact-pair 293 n_f K "
        "and sibling-compatible inherited 585 n_f K; n_f = 1 recovers "
        "the sibling values (293/585); n_f = 3 gives 879/1755",
        sp.simplify(series_146 - 146) == 0
        and sp.simplify(direct_env.subs(n_f, 1) - 293) == 0
        and sp.simplify(inherited_env.subs(n_f, 1) - 585) == 0
        and sp.simplify(direct_env.subs(n_f, 3) - 879) == 0
        and sp.simplify(inherited_env.subs(n_f, 3) - 1755) == 0,
    )

    # Needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 sibling names the matrix-fiber item this note takes",
        BLOCK08_NOTE,
        (
            "a **scalar fiber**; matrix-valued (internal-component) "
            "kernels need a fiber-dimension envelope, named open.",
            "scalar fiber declared, matrix fibers named open",
        ),
    )
    checks.needle(
        "N2 block07 class and display consumed unchanged",
        BLOCK07_NOTE,
        (
            "microcausality_weighted_quasilocal_class_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Theorem (weighted quasilocal all-time volume-uniform "
            "Lieb-Robinson bound).**",
        ),
    )
    checks.needle(
        "N3 block04 graded disjoint-commutation authority",
        BLOCK04_NOTE,
        (
            "microcausality_fermionic_even_car_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Graded locality lemma (rebuilt from the CAR relations; "
            "local alias L-F).**",
        ),
    )
    checks.needle(
        "N4 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    CT_NOTE = ROOT / (
        "docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_"
        "NARROW_THEOREM_NOTE_2026-06-13.md"
    )
    checks.needle(
        "N6 CT note declares U(1) AND SU(2) block kernels (the "
        "source-scope correction's quotes)",
        CT_NOTE,
        (
            "any compact gauge group `G` (here `U(1)` and `SU(2)`)",
            "Per-site commuting-mode / block-kernel convention",
        ),
    )
    checks.needle(
        "N5 target identifiers, exact-lemma sentence, non-claims, Status",
        TARGET_NOTE,
        (
            "microcausality_matrix_fiber_trace_norm_lemma_and_feed_"
            "bounded_theorem_note_2026-07-18",
            "**Pair trace-norm lemma (exact identity, rebuilt).**",
            "`||T + T^†|| = Σ_i σ_i = ||k||_{S1}`",
            "Does **not** claim the on-site norm equals the trace norm",
            "**Status: PASS**",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
