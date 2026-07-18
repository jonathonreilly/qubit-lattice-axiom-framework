#!/usr/bin/env python3
"""Exact checks for the fermionic even-CAR walk-expansion LR note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / (
    "docs/MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK03_NOTE = ROOT / (
    "docs/MICROCAUSALITY_ALL_TIME_VOLUME_UNIFORM_WALK_EXPANSION_"
    "LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
BLOCK01_NOTE = ROOT / (
    "docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_"
    "BOUNDED_THEOREM_NOTE_2026-07-18.md"
)
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


EXPECTED_GATES = 25


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        ok = bool(condition)
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

    def anti_needle(self, label, path, forbidden):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(forbidden, str):
            forbidden = (forbidden,)
        self.check(
            label,
            all(normalized_whitespace(f) not in haystack for f in forbidden),
        )

    def finish(self):
        total = self.passed + self.failed
        if total != EXPECTED_GATES:
            print(
                f"FAIL: gate-manifest drift: ran {total}, "
                f"expected {EXPECTED_GATES}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
ANN = sp.Matrix([[0, 1], [0, 0]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def com(a, b):
    return a * b - b * a


def acom(a, b):
    return a * b + b * a


def is_zero(m):
    return sp.simplify(m) == sp.zeros(*m.shape)


def op_norm_sq(m):
    return max((m.H * m).eigenvals())


N_SITES = 4


def c_op(j):
    return kron(*([SZ] * j + [ANN] + [I2] * (N_SITES - j - 1)))


def main():
    checks = CheckRunner()

    c = [c_op(j) for j in range(N_SITES)]
    cd = [m.H for m in c]
    iden = sp.eye(2**N_SITES)
    zero = sp.zeros(2**N_SITES, 2**N_SITES)

    # Group C -- CAR representation and the graded lemma.
    car_ok = True
    for i in range(N_SITES):
        for j in range(N_SITES):
            car_ok &= is_zero(acom(c[i], c[j]))
            car_ok &= is_zero(acom(cd[i], cd[j]))
            tgt = iden if i == j else zero
            car_ok &= is_zero(acom(c[i], cd[j]) - tgt)
    checks.check(
        "C1 CAR relations hold in the JW representation (all pairs, 4 sites)",
        car_ok,
    )
    cross = all(
        is_zero(acom(a, b))
        for a, b in (
            (c[0], c[2]),
            (c[0], cd[2]),
            (cd[0], c[2]),
            (cd[0], cd[2]),
        )
    )
    even_02 = cd[0] * c[1]
    checks.check(
        "C2 lemma ingredients: cross-site generators anticommute; "
        "even monomial passes a disjoint generator with sign +1",
        cross and is_zero(com(even_02, c[2])) and is_zero(com(even_02, cd[2])),
    )
    hop01 = cd[0] * c[1] + cd[1] * c[0]
    hop23 = cd[2] * c[3] + cd[3] * c[2]
    n2 = cd[2] * c[2]
    n3 = cd[3] * c[3]
    odd0 = c[0] + cd[0]
    odd3 = c[3] + cd[3]
    checks.check(
        "C3 graded table: even-disjoint commutes (even, density, odd); "
        "odd-odd disjoint anticommutes with nonzero commutator",
        is_zero(com(hop01, hop23))
        and is_zero(com(hop01, n3))
        and is_zero(com(hop01, odd3))
        and is_zero(acom(odd0, odd3))
        and not is_zero(com(odd0, odd3)),
    )
    pairing01 = cd[0] * cd[1] + c[1] * c[0]
    parity = kron(SZ, SZ, SZ, SZ)
    checks.check(
        "C4 hopping and pairing: Hermitian, even (commute with parity), "
        "exact norm 1 each",
        is_zero(hop01 - hop01.H)
        and is_zero(pairing01 - pairing01.H)
        and is_zero(com(hop01, parity))
        and is_zero(com(pairing01, parity))
        and sp.simplify(op_norm_sq(hop01) - 1) == 0
        and sp.simplify(op_norm_sq(pairing01) - 1) == 0
        and is_zero(com(pairing01, odd3))
        and is_zero(com(pairing01, n3)),
    )
    checks.check(
        "C5 odd-term necessity: an odd disjoint pair anticommutes, so the "
        "reduction step fails without evenness",
        not is_zero(com(odd0, odd3)) and is_zero(acom(odd0, odd3)),
    )
    gens_left = [c[0], cd[0], c[1], cd[1]]
    gens_right = [c[2], cd[2], c[3], cd[3]]

    def monomials(gens):
        out = [(sp.eye(2**N_SITES), 0)]
        for r in range(1, len(gens) + 1):
            for combo in itertools.combinations(range(len(gens)), r):
                m = gens[combo[0]]
                for idx in combo[1:]:
                    m = m * gens[idx]
                out.append((m, r))
        return out

    left = monomials(gens_left)
    right = monomials(gens_right)
    pq_law_holds = True
    pplusq_law_fails_somewhere = False
    for a_mat, p in left:
        for b_mat, q in right:
            sign_pq = (-1) ** (p * q)
            if not is_zero(a_mat * b_mat - sign_pq * (b_mat * a_mat)):
                pq_law_holds = False
            sign_pplusq = (-1) ** (p + q)
            if sign_pq != sign_pplusq and not is_zero(a_mat * b_mat):
                if not is_zero(
                    a_mat * b_mat - sign_pplusq * (b_mat * a_mat)
                ):
                    pplusq_law_fails_somewhere = True
    checks.check(
        "C6 exhaustive graded sign law: all 256 basis pairs obey "
        "(-1)^(p*q), and the (-1)^(p+q) law is explicitly violated",
        len(left) == 16
        and len(right) == 16
        and pq_law_holds
        and pplusq_law_fails_somewhere,
    )

    # Group R -- reduction and flow instances.
    hop12 = cd[1] * c[2] + cd[2] * c[1]
    ham = hop01 + hop12 + hop23
    n0 = cd[0] * c[0]
    checks.check(
        "R1 fermionic boundary reduction: far hops commute exactly and "
        "[H, n_0] = [hop_01, n_0] != 0",
        is_zero(com(hop12, n0))
        and is_zero(com(hop23, n0))
        and is_zero(com(ham, n0) - com(hop01, n0))
        and not is_zero(com(hop01, n0)),
    )
    checks.check(
        "R2 self-drop: [h, h] = 0 and [H, hop_01] = [hop_12, hop_01]",
        is_zero(com(hop01, hop01))
        and is_zero(com(ham, hop01) - com(hop12, hop01))
        and not is_zero(com(hop12, hop01)),
    )
    gen_sum = hop01 + hop12
    checks.check(
        "R3 generator sums stay Hermitian and even (H-tilde hypothesis)",
        is_zero(gen_sum - gen_sum.H) and is_zero(com(gen_sum, parity)),
    )

    # Group K -- cone instances at d = 3 on the four-site chain.
    ad1 = com(ham, n0)
    ad2 = com(ham, ad1)
    ad3 = com(ham, ad2)
    checks.check(
        "K1 below-cone vanishing k = 0, 1, 2 against BOTH parities of probe",
        is_zero(com(n0, n3))
        and is_zero(com(n0, odd3))
        and is_zero(com(ad1, n3))
        and is_zero(com(ad1, odd3))
        and is_zero(com(ad2, n3))
        and is_zero(com(ad2, odd3)),
    )
    checks.check(
        "K2 cone arrival at k = d = 3 against both probes",
        not is_zero(com(ad3, n3)) and not is_zero(com(ad3, odd3)),
    )
    checks.check(
        "K3 parity preservation exhibit: the adjoint chain of an even "
        "observable stays even",
        is_zero(com(ad1, parity))
        and is_zero(com(ad2, parity))
        and is_zero(com(ad3, parity)),
    )

    # Group S -- the JW-string exhibit.
    hop13 = cd[1] * c[3] + cd[3] * c[1]
    x2_qubit = kron(I2, I2, SX, I2)
    checks.check(
        "S1 JW image of the JW-nonadjacent hop is NOT a qubit operator on "
        "its two factors (fails against the intermediate qubit X)",
        not is_zero(com(hop13, x2_qubit)),
    )
    checks.check(
        "S2 CAR locality holds regardless: the same hop commutes with the "
        "odd intermediate generators and the even intermediate density",
        is_zero(com(hop13, c[2]))
        and is_zero(com(hop13, cd[2]))
        and is_zero(com(hop13, n2)),
    )

    # Group T -- theorem assembly.
    zeroth = com(odd0, odd3)
    checks.check(
        "T1 odd-odd zeroth term is genuinely needed: ||[A, B]|| = 2 at t = 0",
        sp.simplify(op_norm_sq(zeroth) - 4) == 0,
    )
    checks.check(
        "T2 even-sector zeroth term vanishes (either observable even, "
        "both orientations)",
        is_zero(com(n0, odd3))
        and is_zero(com(odd0, n3))
        and is_zero(com(hop01, n3)),
    )
    j_sym, n_sym, k_sym = sp.symbols("j_sym n_sym k_sym", positive=True)
    checks.check(
        "T3 coefficient assembly re-gate (2J)^k n 10^(k-1) = (n/10)(20J)^k",
        sp.simplify(
            (2 * j_sym) ** k_sym * n_sym * 10 ** (k_sym - 1)
            - (n_sym / sp.Integer(10)) * (20 * j_sym) ** k_sym
        )
        == 0,
    )

    # Group N -- source needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 sibling names the fermionic transfer bridge as open",
        BLOCK03_NOTE,
        "the fermionic transfer bridge",
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
        "N3 sibling chain authorities: theorem heading, volume-uniform "
        "constants, directed-time symmetry",
        BLOCK03_NOTE,
        (
            "microcausality_all_time_volume_uniform_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**G6 (theorem: all-time volume-uniform Lieb-Robinson bound).**",
            "obtained by the `H → −H` symmetry",
        ),
    )
    checks.needle(
        "N3b sibling class conventions (block01: Hermitian bond terms)",
        BLOCK01_NOTE,
        "whose terms `h_b` are Hermitian",
    )
    checks.needle(
        "N4 target identifiers, lemma, theorem, non-attempt, hypothesis",
        TARGET_NOTE,
        (
            "microcausality_fermionic_even_car_walk_expansion_"
            "lieb_robinson_bounded_theorem_note_2026-07-18",
            "**Graded locality lemma (rebuilt from the CAR relations; "
            "local alias L-F).**",
            "**Theorem (fermionic all-time volume-uniform Lieb-Robinson "
            "bound).**",
            "is **not attempted** and remains open",
            "`X ∩ Y = ∅`, equivalently `d ≥ 1` — required throughout",
            "with `||[A, B]|| = 0` whenever `A` or `B` is even",
        ),
    )
    checks.needle(
        "N5 theorem inequality with zeroth term pinned in frontmatter "
        "AND body",
        TARGET_NOTE,
        (
            "||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A||||B||(n_X/10) "
            "Σ_{k≥d} (20J|t|)^k/k!",
            "`||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10)",
        ),
    )
    checks.anti_needle(
        "N6 clean arbitrary-parity form is rejected (must not reappear)",
        TARGET_NOTE,
        (
            "arbitrary-parity A, B with d ≥ 1, ||[τ_t(A), B]|| ≤ "
            "2||A||||B||(n_X/10)",
            "for arbitrary parities the series starts with no zeroth term",
        ),
    )
    checks.needle(
        "N7 No-Go section structure: all eight items and the Status line",
        TARGET_NOTE,
        (
            "**N1 route inventory",
            "**N2 hypothesis independence (pairwise).**",
            "**N3 hidden-wall scan.**",
            "**N4 dependency roles, per citation",
            "**N5 rhetoric audit.**",
            "**N6 partial-closure scan.**",
            "**N7 steelman (strongest counterarguments found in review,",
            "**N8 prior-wall echo (repo-wide disposition).**",
            "**Status: PASS**",
            "KS_ETA_VS_JW_STRING_CAR_LOCALITY_NO_GO_NOTE_2026-06-02.md",
            "FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_"
            "NO_GO_NOTE_2026-05-28.md",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
