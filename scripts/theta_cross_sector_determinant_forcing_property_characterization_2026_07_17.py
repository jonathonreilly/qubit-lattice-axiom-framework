#!/usr/bin/env python3
"""Exact checks for the theta forcing-property characterization note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md"
OBLIGATION = ROOT / "docs/THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md"
PHASE_ERASURE_NOTE = ROOT / "docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
REGISTRABLE_NOTE = ROOT / "docs/REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"


def normalized_whitespace(text):
    return " ".join(text.split())


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        try:
            ok = bool(condition)
        except (TypeError, ValueError):
            ok = condition == sp.true
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
            all(normalized_whitespace(needle) in haystack for needle in needles),
        )

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def main():
    checks = CheckRunner()
    print(
        "FLAG: P1/T1 are not consequences of finite disjoint-record additivity "
        "alone. They are checked only with the separately supplied "
        "conjugation-pair/trivial-sector normalization."
    )

    # Group C -- conjugation and the phase functional.
    radius = sp.symbols("r", positive=True, real=True)
    phi = sp.symbols("phi", real=True)
    z = radius * sp.exp(sp.I * phi)
    checks.check(
        "C1 symbolic conjugation reverses the phase",
        sp.simplify(sp.conjugate(z) - radius * sp.exp(-sp.I * phi)) == 0,
    )

    principal_witnesses = (sp.S.Zero, sp.pi / 4, sp.pi / 2, 3 * sp.pi / 4)
    checks.check(
        "C1 principal-branch argument reversal at exact witnesses",
        all(
            sp.simplify(
                sp.arg(sp.conjugate(sp.Rational(7, 3) * sp.exp(sp.I * angle)))
                + sp.arg(sp.Rational(7, 3) * sp.exp(sp.I * angle))
            )
            == 0
            for angle in principal_witnesses
        ),
    )

    formal_value = sp.symbols("f")
    checks.check(
        "C2 formal odd-and-even elimination",
        sp.solve(sp.Eq(formal_value, -formal_value), formal_value) == [0],
    )

    c1 = sp.symbols("c1")
    odd_family = c1 * sp.sin(phi)
    evenness_equation = sp.Eq(odd_family - odd_family.subs(phi, -phi), 0)
    checks.check(
        "C2 generic odd-family evenness forces its coefficient to zero",
        sp.simplify(evenness_equation.lhs - 2 * c1 * sp.sin(phi)) == 0
        and sp.solve(evenness_equation, c1) == [0],
    )

    # Group P -- the two named odd-side consequences.
    h_phi, h_neg_phi, h_sum, h_trivial = sp.symbols(
        "h_phi h_neg_phi h_sum h_trivial"
    )
    additive_elimination = sp.solve(
        (
            sp.Eq(h_sum, h_phi + h_neg_phi),
            sp.Eq(h_sum, h_trivial),
            sp.Eq(h_trivial, 0),
        ),
        (h_neg_phi, h_sum, h_trivial),
        dict=True,
    )
    checks.check(
        "P1 additivity plus conjugation-pair normalization implies oddness",
        additive_elimination
        == [{h_neg_phi: -h_phi, h_sum: 0, h_trivial: 0}],
    )

    phi1 = sp.pi / 6
    phi2 = sp.pi / 3
    z1 = sp.exp(sp.I * phi1)
    z2 = sp.exp(sp.I * phi2)
    checks.check(
        "P2 principal-range argument is additive at exact witnesses",
        sp.arg(z1 * z2) == sp.arg(z1) + sp.arg(z2) == sp.pi / 2,
    )

    k = sp.symbols("k", integer=True)
    alpha, beta = sp.symbols("alpha beta", real=True)
    checks.check(
        "P2 character exponent is additive identically",
        sp.expand(k * (alpha + beta) - (k * alpha + k * beta)) == 0,
    )

    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    b11, b12, b21, b22 = sp.symbols("b11 b12 b21 b22")
    matrix_a = sp.Matrix(((a11, a12), (a21, a22)))
    matrix_b = sp.Matrix(((b11, b12), (b21, b22)))
    block_matrix = sp.diag(matrix_a, matrix_b)
    checks.check(
        "P2 symbolic two-by-two block determinant law",
        sp.expand(block_matrix.det() - matrix_a.det() * matrix_b.det()) == 0,
    )

    # Group W -- exact registering witnesses and the silent control.
    k_nonzero = sp.symbols("k_nz", integer=True, nonzero=True)
    character_phase = k_nonzero * phi
    checks.check(
        "W1a nonzero-character phase functional is odd identically",
        sp.expand(character_phase.subs(phi, -phi) + character_phase) == 0,
    )

    character_product = sp.exp(sp.I * k_nonzero * phi1) * sp.exp(
        sp.I * k_nonzero * phi2
    )
    checks.check(
        "W1a character composes multiplicatively at exact witnesses",
        sp.simplify(
            sp.exp(sp.I * k_nonzero * (phi1 + phi2)) - character_product
        )
        == 0,
    )

    orbit_value = sp.exp(sp.I * sp.pi / 2)
    conjugate_orbit_value = sp.exp(-sp.I * sp.pi / 2)
    checks.check(
        "W1b k=1 character breaks orbit constancy",
        orbit_value == sp.I
        and conjugate_orbit_value == -sp.I
        and orbit_value != conjugate_orbit_value,
    )

    checks.check(
        "W1c k=1 character registers phase",
        sp.exp(sp.I * 0) == 1
        and sp.exp(sp.I * sp.pi / 2) == sp.I
        and sp.exp(sp.I * 0) != sp.exp(sp.I * sp.pi / 2),
    )

    cosine_probe = sp.cos(phi)
    checks.check(
        "W2a cosine is even identically",
        sp.trigsimp(cosine_probe.subs(phi, -phi) - cosine_probe) == 0,
    )

    checks.check(
        "W2a cosine is not odd",
        cosine_probe.subs(phi, 0) == 1
        and -cosine_probe.subs(phi, 0) == -1
        and cosine_probe.subs(phi, 0) != -cosine_probe.subs(phi, 0),
    )

    checks.check(
        "W2b cosine breaks multiplicative homomorphism",
        sp.cos(sp.pi) == -1
        and sp.cos(sp.pi / 2) * sp.cos(sp.pi / 2) == 0
        and sp.cos(sp.pi) != sp.cos(sp.pi / 2) * sp.cos(sp.pi / 2),
    )

    cosine_pair_sum = cosine_probe.subs(phi, -phi) + cosine_probe
    checks.check(
        "W2c cosine breaks the additivity-oddness consequence",
        sp.trigsimp(cosine_pair_sum - 2 * sp.cos(phi)) == 0
        and cosine_pair_sum.subs(phi, 0) == 2
        and cosine_pair_sum.subs(phi, 0) != 0,
    )

    checks.check(
        "W2d cosine registers phase",
        sp.cos(0) == 1 and sp.cos(sp.pi) == -1 and sp.cos(0) != sp.cos(sp.pi),
    )

    s = sp.symbols("s", real=True)
    modulus_character = sp.Abs(z) ** s
    conjugate_modulus_character = sp.Abs(sp.conjugate(z)) ** s
    checks.check(
        "W3 k=0 modulus character is orbit-constant and phase-silent",
        sp.simplify(modulus_character - radius**s) == 0
        and sp.simplify(conjugate_modulus_character - modulus_character) == 0
        and sp.diff(modulus_character, phi) == 0
        and sp.simplify(
            modulus_character.subs(phi, 0)
            - modulus_character.subs(phi, sp.pi / 2)
        )
        == 0,
    )

    # Extra witnesses adopted from the adversarial lens round.
    phi_wrap = 3 * sp.pi / 4
    wrapped_product_arg = sp.arg(sp.exp(sp.I * phi_wrap) * sp.exp(sp.I * phi_wrap))
    checks.check(
        "X1 wrapping witness: principal argument composes modulo two pi",
        wrapped_product_arg == -sp.pi / 2
        and sp.simplify((phi_wrap + phi_wrap) - wrapped_product_arg - 2 * sp.pi)
        == 0,
    )
    checks.check(
        "X2 branch convention: the branch point z=-1 maps to itself under "
        "conjugation with principal argument pi",
        sp.arg(sp.Integer(-1)) == sp.pi
        and sp.arg(sp.conjugate(sp.Integer(-1))) == sp.pi,
    )
    silent_witness_values = tuple(
        1 + sp.Abs(sp.Rational(5, 4) * sp.exp(sp.I * angle))
        for angle in (sp.S.Zero, sp.pi / 2, sp.pi)
    )
    silent_pair = 1 + sp.Abs(sp.S.One * sp.S.One)
    silent_add = (1 + sp.Abs(sp.S.One)) + (1 + sp.Abs(sp.S.One))
    silent_mul = (1 + sp.Abs(sp.S.One)) * (1 + sp.Abs(sp.S.One))
    checks.check(
        "X3 silent-without-properties witness: 1+|z| is orbit-constant and "
        "phase-silent yet neither additive nor multiplicative under blocks",
        all(sp.simplify(v - sp.Rational(9, 4)) == 0 for v in silent_witness_values)
        and sp.simplify(
            (1 + sp.Abs(sp.conjugate(sp.Rational(5, 4) * sp.exp(sp.I * sp.pi / 3))))
            - sp.Rational(9, 4)
        )
        == 0
        and silent_pair == 2
        and silent_add == 4
        and silent_mul == 4
        and silent_pair != silent_add
        and silent_pair != silent_mul,
    )
    sine_consequence = sp.sin(phi)
    checks.check(
        "X4 additive-route consequence-level witness: sin is odd, registers, "
        "and is not even",
        sp.trigsimp(sine_consequence.subs(phi, -phi) + sine_consequence) == 0
        and sp.sin(0) == 0
        and sp.sin(sp.pi / 2) == 1
        and sp.sin(0) != sp.sin(sp.pi / 2)
        and sp.sin(sp.pi / 2) != sp.sin(-sp.pi / 2),
    )

    # Group T -- assemble the two forward cells and the necessity witnesses.
    forward_value, forward_negative = sp.symbols(
        "forward_value forward_negative"
    )
    odd_even_solution = sp.solve(
        (
            sp.Eq(forward_negative, -forward_value),
            sp.Eq(forward_negative, forward_value),
        ),
        (forward_value, forward_negative),
        dict=True,
    )
    checks.check(
        "T1 landed additive-plus-orbit mechanism re-derived",
        odd_even_solution == [{forward_value: 0, forward_negative: 0}],
    )

    character_evenness_difference = sp.exp(sp.I * k * phi) - sp.exp(
        -sp.I * k * phi
    )
    generic_k_candidates = sp.solve(sp.Eq(sp.sin(k * phi), 0), k)
    phi_independent_candidates = [
        candidate for candidate in generic_k_candidates if not candidate.has(phi)
    ]
    identity_coefficient = sp.diff(sp.sin(k * phi), phi).subs(phi, 0)
    checks.check(
        "T2 character-family evenness for all phases forces k=0",
        sp.simplify(
            character_evenness_difference - 2 * sp.I * sp.sin(k * phi)
        )
        == 0
        and phi_independent_candidates == [0]
        and identity_coefficient == k
        and sp.solve(sp.Eq(identity_coefficient, 0), k) == [0],
    )

    w1_exponent_odd_side = (
        sp.expand(
            k_nonzero * (alpha + beta)
            - (k_nonzero * alpha + k_nonzero * beta)
        )
        == 0
    )
    w1_homomorphic_odd_side = (
        sp.simplify(
            sp.exp(sp.I * k_nonzero * (phi1 + phi2)) - character_product
        )
        == 0
    )
    w1_not_orbit_constant_and_registers = (
        orbit_value != conjugate_orbit_value
        and sp.exp(sp.I * 0) != sp.exp(sp.I * sp.pi / 2)
    )
    w2_orbit_constant = (
        sp.trigsimp(cosine_probe.subs(phi, -phi) - cosine_probe) == 0
    )
    w2_neither_odd_side_and_registers = (
        cosine_pair_sum.subs(phi, 0) != 0
        and sp.cos(sp.pi) != sp.cos(sp.pi / 2) * sp.cos(sp.pi / 2)
        and sp.cos(0) != sp.cos(sp.pi)
    )
    checks.check(
        "T3 characterization corollary: W1 removes orbit constancy on the "
        "homomorphic route, sin removes it at the additive route's "
        "consequence level, W2 removes the odd side",
        w1_exponent_odd_side
        and w1_homomorphic_odd_side
        and w1_not_orbit_constant_and_registers
        and w2_orbit_constant
        and w2_neither_odd_side_and_registers,
    )

    # Group N -- normalized-whitespace source needles.  The Verification
    # __TOTAL__ placeholder is deliberately neither parsed nor matched.
    checks.needle(
        "N1 obligation exact-target needle",
        OBLIGATION,
        "Derive from the retained framework chain whether the charged-lepton "
        "`K`/CPT occupancy carrier is the same physical channel",
    )
    checks.needle(
        "N2 obligation insufficiency needle",
        OBLIGATION,
        "similarity, shared notation, and historical decision text are insufficient",
    )
    checks.needle(
        "N3 phase-erasure hostile-guard needle",
        PHASE_ERASURE_NOTE,
        "K/CPT orbit invariance alone gives evenness, not phase erasure",
    )
    checks.needle(
        "N4 registrable-note mechanism needle",
        REGISTRABLE_NOTE,
        "homomorphism forces odd; even forces zero",
    )
    checks.needle(
        "N5 characterization-note identifier, properties, and reduction needle",
        TARGET_NOTE,
        (
            "theta_cross_sector_determinant_forcing_property_characterization_bounded_theorem_note_2026-07-17",
            "**(P-add)**",
            "**(P-hom)**",
            "**(P-orb)**",
            "one transported property",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
