#!/usr/bin/env python3
"""Exact checks for the volume-uniform sequence-count bounds note."""

import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md"
SIBLING_NOTE = ROOT / "docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md"
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


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

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


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


def op_norm_sq(m):
    return max((m.H * m).eigenvals())


def main():
    checks = CheckRunner()

    bond = {1: kron(SX, SX, I2), 2: kron(I2, SZ, SZ)}
    hamiltonian = bond[1] + bond[2]
    site_a = kron(SZ, I2, I2)
    probe_x3 = kron(I2, I2, SX)
    probe_z3 = kron(I2, I2, SZ)

    def nested(sequence, operator):
        for label in reversed(sequence):
            operator = com(bond[label], operator)
        return operator

    # Group W1 -- multinomial sequence expansion.
    for order in (2, 3):
        direct = site_a
        for _ in range(order):
            direct = com(hamiltonian, direct)
        summed = sp.zeros(8)
        for sequence in itertools.product((1, 2), repeat=order):
            summed += nested(sequence, site_a)
        checks.check(
            f"W1-k{order} multinomial expansion equals the sequence sum",
            is_zero(direct - summed),
        )

    # Group W2 -- dead sequences and below-cone recovery.
    checks.check(
        "W2a inner-miss sequences vanish exactly",
        is_zero(nested((1, 2), site_a)) and is_zero(nested((2, 2), site_a)),
    )
    bond4_12 = kron(SX, SX, I2, I2)
    bond4_34 = kron(I2, I2, SZ, SZ)
    site4_a = kron(SZ, I2, I2, I2)
    checks.check(
        "W2b later-miss sequences vanish exactly (four-site instance)",
        is_zero(com(bond4_34, com(bond4_12, site4_a))),
    )
    checks.check(
        "W2c every length-1 sequence stays below the cone",
        all(
            is_zero(com(nested((label,), site_a), probe_x3))
            for label in (1, 2)
        ),
    )

    # Group W3 -- local bond counts and the product-form bound.
    unit_vectors = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def incident_bonds(sites):
        bonds = set()
        for site in sites:
            for vec in unit_vectors:
                plus = tuple(a + b for a, b in zip(site, vec))
                minus = tuple(a - b for a, b in zip(site, vec))
                bonds.add(tuple(sorted((site, plus))))
                bonds.add(tuple(sorted((minus, site))))
        return bonds

    single = incident_bonds([(0, 0, 0)])
    pair = incident_bonds([(0, 0, 0), (1, 0, 0)])
    checks.check(
        "W3a exact incident-bond counts respect the 6s bound",
        len(single) == 6
        and len(pair) == 11
        and len(single) <= 6 * 1
        and len(pair) <= 6 * 2,
    )
    m_sites = 1
    product_bound = lambda k: sp.prod(
        [6 * (m_sites + j) for j in range(k)]
    )
    surviving = {
        order: sum(
            0 if is_zero(nested(seq, site_a)) else 1
            for seq in itertools.product((1, 2), repeat=order)
        )
        for order in (1, 2, 3)
    }
    checks.check(
        "W3b strengthened product bound dominates the exact surviving counts",
        product_bound(1) == 6
        and product_bound(2) == 72
        and surviving[1] <= 6
        and surviving[2] <= 72
        and surviving[1] >= 1
        and surviving[2] >= 1,
    )
    chain_bonds_touching = {1: 2, 2: 2}
    checks.check(
        "W3c recurrence instance on the chain: N_{k+1} <= (touching bonds) * N_k",
        surviving[1] == 1
        and surviving[2] == 2
        and surviving[2] <= 2 * surviving[1]
        and surviving[3] <= 2 * surviving[2],
    )

    # Group W4 -- coefficient bound at k=2 and the parity exhibit at k=3.
    ad2 = com(hamiltonian, com(hamiltonian, site_a))
    coeff_norm_sq = op_norm_sq(com(ad2, probe_x3))
    j_bound_sq = max(op_norm_sq(bond[1]), op_norm_sq(bond[2]))
    a_norm_sq = op_norm_sq(site_a)
    b_norm_sq = op_norm_sq(probe_x3)
    rhs_sq = (
        4 * a_norm_sq * b_norm_sq
        * (4 * j_bound_sq) ** 2
        * sp.Integer(72) ** 2
    )
    checks.check(
        "W4a volume-uniform coefficient bound holds at k=2 with exact norms",
        sp.simplify(rhs_sq - coeff_norm_sq).is_nonnegative is True,
    )
    parity_terms = [
        nested(seq, site_a)
        for seq in itertools.product((1, 2), repeat=3)
    ]
    checks.check(
        "W4b parity exhibit: every k=3 sequence commutes with X3 and Z3",
        all(
            is_zero(com(term, probe_x3)) and is_zero(com(term, probe_z3))
            for term in parity_terms
        )
        and is_zero(com(sum(parity_terms, sp.zeros(8)), probe_x3)),
    )
    SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    probe_y3 = kron(I2, I2, SY)
    checks.check(
        "W4b2 k=2 registers against X3 and the Y3-type probe, Z3 silent",
        (not is_zero(com(ad2, probe_x3)))
        and (not is_zero(com(ad2, probe_y3)))
        and is_zero(com(ad2, probe_z3)),
    )
    ad3_total = sum(parity_terms, sp.zeros(8))
    checks.check(
        "W4c k=3 support retreat: every site-3 probe is silent",
        is_zero(com(ad3_total, probe_z3))
        and is_zero(com(ad3_total, probe_x3)),
    )
    ad4_total = com(hamiltonian, ad3_total)
    checks.check(
        "W4d k=4 re-arrival against X3 while Z3 stays silent at k=2 and k=4",
        (not is_zero(com(ad4_total, probe_x3)))
        and is_zero(com(ad4_total, probe_z3))
        and is_zero(com(ad2, probe_z3)),
    )

    # Group W5 -- term ratio, monotonicity, window, geometric tail.
    m_sym, k_sym = sp.symbols("m_sym k_sym", positive=True)
    monotonicity = sp.expand(
        (m_sym + k_sym) * (k_sym + 2)
        - (m_sym + k_sym + 1) * (k_sym + 1)
    )
    checks.check(
        "W5a ratio monotonicity reduces exactly to m >= 1",
        sp.simplify(monotonicity - (m_sym - 1)) == 0,
    )
    j_val = sp.Integer(1)
    d_val = 2
    m_loc = 1
    window_t = sp.Rational(d_val + 1, 12 * j_val * (m_loc + d_val)) / 2
    ratio_at_window = 12 * j_val * window_t * sp.Rational(
        m_loc + d_val, d_val + 1
    )
    checks.check(
        "W5b exact window instance gives ratio one-half",
        ratio_at_window == sp.Rational(1, 2)
        and ratio_at_window < 1,
    )
    a_sym, r_sym = sp.symbols("a_sym r_sym", positive=True)
    k_idx = sp.symbols("k_idx", nonnegative=True, integer=True)
    half_sum = sp.summation(
        a_sym * sp.Rational(1, 2) ** k_idx, (k_idx, 0, sp.oo)
    )
    telescope = sp.expand((a_sym / (1 - r_sym)) * (1 - r_sym) - a_sym)
    checks.check(
        "W5c geometric tail: exact half-ratio sum and the telescoping identity",
        sp.simplify(half_sum - 2 * a_sym) == 0 and telescope == 0,
    )

    # Group N -- needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 sibling names the volume-uniform constant as needing the path argument",
        SIBLING_NOTE,
        "a genuine volume-uniform\nLieb-Robinson constant would need the interaction-path argument",
    )
    checks.needle(
        "N2 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        "Admissibility is not a dynamics axiom.",
    )
    checks.needle(
        "N3 target identifier and labels",
        TARGET_NOTE,
        (
            "microcausality_volume_uniform_sequence_count_coefficient_bounds_bounded_theorem_note_2026-07-18",
            "**W2 (dead-sequence lemma, exact).**",
            "**W5 (volume-uniform bound on an exact local time window).**",
            "remains open exactly as the sibling names it",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
