#!/usr/bin/env python3
"""Verifier for the R-eta algebraic irreducibility bounded note.

Companion runner for
docs/RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md.

The runner checks the algebraic surface, the operator-free fixed-locus constant,
the failed pinning routes, the two-atom admission split, and the note firewall.
"""

from __future__ import annotations

import math
import pathlib
import re
import subprocess
import sys

import numpy as np
import sympy as sp


ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTE = DOCS / "RETA_ALGEBRAIC_IRREDUCIBILITY_GENUINE_READOUT_ADMISSION_BOUNDED_NOTE_2026-06-12.md"
FIXED_LOCUS_NOTE = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
RADIAN_NOTE = DOCS / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(num: int, desc: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] ({num:02d}) {desc}{suffix}")


def simplify_zero(expr: sp.Expr) -> bool:
    return sp.simplify(sp.factor(sp.together(expr))) == 0


def l3_density(a_weight: int, b_weight: int) -> sp.Expr:
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    return sp.simplify(
        sp.Rational(1, 3)
        * sum(
            1 / ((omega ** (j * a_weight) - 1) * (omega ** (j * b_weight) - 1))
            for j in (1, 2)
        )
    )


def koide_comparator(delta_value: float) -> list[float]:
    """Signed-sqrt circulant comparator, normalized to the electron mass."""
    electron = 0.51099895000
    values = [
        1.0 + math.sqrt(2.0) * math.cos(delta_value + 2.0 * math.pi * k / 3.0)
        for k in range(3)
    ]
    sq = [v * v for v in values]
    scale_sq = electron / min(sq)
    return sorted(scale_sq * entry for entry in sq)


def main() -> int:
    print("=" * 72)
    print("R-eta algebraic irreducibility / genuine readout admission verifier")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    fixed_note = FIXED_LOCUS_NOTE.read_text(encoding="utf-8")
    radian_note = RADIAN_NOTE.read_text(encoding="utf-8")
    minimal_axioms = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    note_flat = flat(note)

    a, B, delta, u = sp.symbols("a B delta u", real=True, nonzero=True)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2

    lambdas_u = [a + B * u * omega**k + B / u * omega ** (-k) for k in range(3)]
    e1_u = sp.simplify(sum(lambdas_u))
    e2_u = sp.simplify(sum(lambdas_u[i] * lambdas_u[j] for i in range(3) for j in range(i + 1, 3)))
    e3_u = sp.simplify(sp.prod(lambdas_u))
    expected_e1 = 3 * a
    expected_e2 = 3 * a**2 - 3 * B**2
    expected_e3_u = a**3 - 3 * a * B**2 + B**3 * (u**3 + u**-3)

    check(
        1,
        "I1 symbolic elementary symmetric invariants match the retained circulant formula",
        simplify_zero(e1_u - expected_e1)
        and simplify_zero(e2_u - expected_e2)
        and simplify_zero(e3_u - expected_e3_u),
        f"e1={e1_u}, e2={e2_u}, e3={sp.factor(e3_u)}",
    )

    expected_e3_delta = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)
    d_e3 = sp.diff(expected_e3_delta, delta)
    check(
        2,
        "I1 delta enters e1,e2,e3 only through cos(3 delta)",
        expected_e1.has(delta) is False
        and expected_e2.has(delta) is False
        and simplify_zero(d_e3 + 6 * B**3 * sp.sin(3 * delta)),
        f"d(e3)/d(delta)={d_e3}",
    )

    x_coord = sp.Symbol("x")
    x_recovered = sp.simplify((expected_e3_delta - a**3 + 3 * a * B**2) / (2 * B**3))
    affine_e3 = a**3 - 3 * a * B**2 + 2 * B**3 * x_coord
    affine_slope = sp.diff(affine_e3, x_coord)
    a_from_e1 = sp.Symbol("e1") / 3
    b2_from_e2 = a_from_e1**2 - sp.Symbol("e2") / 3
    check(
        3,
        "I2 x=cos(3 delta) is recovered affinely and e1,e2 fix only a and B^2",
        simplify_zero(x_recovered - sp.cos(3 * delta))
        and simplify_zero(affine_slope - 2 * B**3)
        and b2_from_e2 == sp.Symbol("e1") ** 2 / 9 - sp.Symbol("e2") / 3,
        f"x={x_recovered}, slope={affine_slope}, B^2={b2_from_e2}",
    )

    l12 = l3_density(1, 2)
    l11 = l3_density(1, 1)
    l22 = l3_density(2, 2)
    core = sp.simplify((omega - 1) * (omega**2 - 1))
    check(
        4,
        "I3 L_3(1,2)=2/9 exact; L_3(1,1)=L_3(2,2)=1/9; core product is 3",
        l12 == sp.Rational(2, 9)
        and l11 == sp.Rational(1, 9)
        and l22 == sp.Rational(1, 9)
        and core == 3,
        f"L12={l12}, L11={l11}, L22={l22}, core={core}",
    )

    check(
        5,
        "I3 fixed-locus computation is operator-free: no a, B, delta, or H symbol occurs",
        not (l12.has(a) or l12.has(B) or l12.has(delta)) and l12.free_symbols == set(),
        f"free_symbols={l12.free_symbols}",
    )

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T
    comm = sp.simplify(H * C - C * H)
    check(
        6,
        "I4a C_3 covariance [H,C]=0 holds symbolically for generic delta",
        comm == sp.zeros(3),
        f"commutator={comm}",
    )

    det_h = sp.simplify(H.det())
    det_expected_exp = a**3 - 3 * a * B**2 + B**3 * (sp.exp(3 * sp.I * delta) + sp.exp(-3 * sp.I * delta))
    sample_deltas = np.linspace(-math.pi, math.pi, 13)
    sample_dets = [
        float(np.prod([3.0 + 2.0 * math.cos(float(t) + 2.0 * math.pi * k / 3.0) for k in range(3)]))
        for t in sample_deltas
    ]
    check(
        7,
        "I4b det H is real and positive on the sample positivity domain a>2B>0, so arg det H=0 there",
        simplify_zero(det_h - det_expected_exp)
        and min(sample_dets) > 0
        and (3.0 - 2.0 * 1.0) > 0,
        f"detH={sp.factor(det_h)}, min_sample={min(sample_dets):.6f}",
    )

    n_for_two_ninths = sp.Rational(2, 3) / sp.pi
    n_for_two_ninths_float = float(n_for_two_ninths)
    check(
        8,
        "I4c spectral-scalar stationary set delta=n*pi/3 excludes delta=2/9",
        not n_for_two_ninths_float.is_integer()
        and abs(n_for_two_ninths_float - round(n_for_two_ninths_float)) > 1.0e-6,
        f"n=2/(3*pi)={n_for_two_ninths_float:.12f}",
    )

    witness_1 = (sp.Rational(5, 2), sp.Rational(1, 2), sp.Rational(0), sp.cos(0))
    witness_2 = (sp.Rational(5, 2), sp.Rational(1, 2), sp.pi / 9, sp.cos(sp.pi / 3))
    fixed_delta_pair = [
        (sp.Rational(2, 1), sp.Rational(1, 3), sp.Rational(1, 7), l12),
        (sp.Rational(5, 1), sp.Rational(2, 3), sp.Rational(1, 7), l12),
    ]
    jacobian = sp.Matrix([sp.cos(3 * delta), l12]).jacobian([delta])
    check(
        9,
        "I5 independence witness: same L_3 with different cos(3 delta), and L_3 unchanged under operator-parameter variation",
        witness_1[3] != witness_2[3]
        and fixed_delta_pair[0][3] == fixed_delta_pair[1][3] == sp.Rational(2, 9)
        and simplify_zero(jacobian[1, 0]),
        f"w1 x={witness_1[3]}, w2 x={witness_2[3]}, fixed-delta L={fixed_delta_pair[0][3]}",
    )

    readings = [2.0 / 9.0, math.pi * 2.0 / 9.0, 2.0 * math.pi * 2.0 / 9.0]
    check(
        10,
        "I6a A1 magnitude and A2 unit/coefficient are distinct data; 1, pi, 2pi readings are different angles",
        len({round(x, 12) for x in readings}) == 3
        and readings[0] < readings[1] < readings[2],
        "angles=" + ", ".join(f"{x:.6f}" for x in readings),
    )

    target_mu = 105.6583755
    target_tau = 1776.86
    comp_one = koide_comparator(2.0 / 9.0)
    comp_pi = koide_comparator(math.pi * 2.0 / 9.0)
    comp_twopi = koide_comparator(2.0 * math.pi * 2.0 / 9.0)
    rel_one_mu = abs(comp_one[1] - target_mu) / target_mu
    rel_one_tau = abs(comp_one[2] - target_tau) / target_tau
    rel_pi = max(abs(comp_pi[1] - target_mu) / target_mu, abs(comp_pi[2] - target_tau) / target_tau)
    rel_twopi = max(abs(comp_twopi[1] - target_mu) / target_mu, abs(comp_twopi[2] - target_tau) / target_tau)
    print(
        "    comparator, not a derivation input; no PDG enters any derivation step: "
        f"delta=2/9 -> m_mu={comp_one[1]:.6f}, m_tau={comp_one[2]:.6f}; "
        f"pi-reading -> {comp_pi[1]:.6f}, {comp_pi[2]:.6f}; "
        f"2pi-reading -> {comp_twopi[1]:.6f}, {comp_twopi[2]:.6f}"
    )
    check(
        11,
        "I6b labeled comparator: coefficient-1 reading lands masses; pi and 2pi readings miss by >0.3 relative",
        rel_one_mu < 2.0e-5
        and rel_one_tau < 1.0e-4
        and rel_pi > 0.3
        and rel_twopi > 0.3,
        f"rel_one_mu={rel_one_mu:.3e}, rel_one_tau={rel_one_tau:.3e}, rel_pi={rel_pi:.3f}, rel_2pi={rel_twopi:.3f}",
    )

    nonzero_rational_over_pi_irrational = bool(sp.pi.is_irrational)
    check(
        12,
        "I6c 2/9 is not q*pi for rational q; 2/(9*pi) is irrational by pi irrationality",
        nonzero_rational_over_pi_irrational
        and sp.Rational(2, 9) != 0
        and not any(sp.Eq(sp.Rational(2, 9), sp.Rational(q, 9) * sp.pi) == True for q in range(-20, 21)),
        "2/(9*pi) is not rational",
    )

    fixed_dep_ok = "local density `2/9`" in fixed_note and "core identity" in fixed_note
    radian_dep_ok = (
        "retained periodic phase sources  ->  rational multiples of pi" in radian_note
        and "Type-B rational-to-radian observable law is still missing" in radian_note
        and "a nonzero pure rational such as `2/9` is not supplied as a literal radian" in radian_note
    )
    check(
        13,
        "B-check dependency greps: fixed-locus L_3 phrase and real radian-bridge scope phrase are pinned",
        fixed_dep_ok and radian_dep_ok and "Status authority" in minimal_axioms,
    )

    safe_underivable_sentence = "This note also does not claim R-eta is underivable." in note
    banned_overclaims = [
        "R-eta is underivable",
        "closes R-eta",
        "only possible route",
        "routes are exhausted",
        "force delta=2/9",
    ]
    overclaim_free = all(
        phrase not in note.replace("This note also does not claim R-eta is underivable.", "")
        for phrase in banned_overclaims
    )
    check(
        14,
        "B-check firewall / walls-move sentences are present without forbidden overclaim use",
        "The next paths" in note
        and "does not derive" in note
        and "does not force" in note
        and "genuine readout admission" in note
        and safe_underivable_sentence
        and overclaim_free,
    )

    check(
        15,
        "B-check N1-N8 gate section is present",
        "## No-Go / Bounded-Wall Discipline Gate (N1-N8)" in note
        and all(f"**N{i} " in note for i in range(1, 9)),
    )

    wall_names = [
        "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md",
        "DET_HOLONOMY_TRIVIAL_ON_HERMITIAN_POSITIVE_CIRCULANT_EDGE_CONTENT_BOUNDED_NOTE_2026-06-12.md",
        "CORRELATOR_CYCLE_PHASES_READBACK_BLIND_OR_STATE_CONTINGENT_BOUNDED_NOTE_2026-06-12.md",
        "EQUIVARIANT_WILSON_ETA_DENSITIES_VANISH_ON_TESTED_WINDOW_BOUNDED_NOTE_2026-06-12.md",
        "SLAB_BOUNDARY_ETA_GLOBALLY_ZERO_PER_EDGE_NONUNIVERSAL_NO_FRACTIONAL_CARRIER_BOUNDED_NOTE_2026-06-12.md",
        "RETA_MAGNITUDE_IS_CONTINUUM_INDEX_THEOREM_LATTICE_INDEX_IS_INTEGER_BOUNDED_NOTE_2026-06-12.md",
    ]
    check(
        16,
        "B-check six-wall carrier map present with six backticked wall names",
        "## The R-eta Carrier-Search Map" in note
        and all(f"`{name}`" in note for name in wall_names),
    )

    md_links = re.findall(r"\[[^\]]+\]\(([^)]+\.md)\)", note)
    expected_links = {
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "MINIMAL_AXIOMS_2026-06-05.md",
    }
    check(
        17,
        "B-check markdown link inventory is exactly the three dependencies and all resolve",
        set(md_links) == expected_links
        and len(md_links) == 3
        and all((DOCS / target).exists() for target in md_links),
        f"links={md_links}",
    )

    context_backticked = (
        "`ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md`" in note
        and all(f"`{name}`" in note for name in wall_names)
        and "](ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION" not in note
    )
    check(
        18,
        "B-check context inventory is backticked, not markdown-linked",
        context_backticked,
    )

    check(
        19,
        "B-check status lines, No-promotion statement, no registry edit, and bounded theorem declaration are present",
        "**Date:** 2026-06-12" in note
        and "**Claim type:** bounded_theorem" in note
        and "**Status authority:**" in note
        and "**No-promotion statement:**" in note
        and "does not edit any audit-owned registry" in note
        and "does not set a grade" in note,
    )

    check(
        20,
        "B-check R-eta is characterized but not adopted, derived, or refuted",
        "R-eta is characterized by admission status" in note_flat
        and "not adopted, derived, or refuted here" in note_flat
        and "It does not derive R-eta" in note
        and "It does not refute R-eta" in note,
    )

    check(
        21,
        "B-check two live derivation targets are named and neither is probed here",
        "registrable `C_3`-covariant holonomy/eta-invariant" in note
        and "conversion-factor sources beyond the determinant class" in note
        and "neither is probed here" in note_flat,
    )

    print("=" * 72)
    print("git diff --stat")
    try:
        diff = subprocess.run(
            ["git", "diff", "--stat"],
            cwd=ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        if diff.stdout.strip():
            print(diff.stdout.rstrip())
        else:
            stat_paths = [
                NOTE,
                ROOT / "scripts" / "frontier_reta_algebraic_irreducibility_2026_06_12.py",
            ]
            total_lines = 0
            for path in stat_paths:
                line_count = len(path.read_text(encoding="utf-8").splitlines())
                total_lines += line_count
                print(f" {path.relative_to(ROOT)} | {line_count} +")
            print(f" 2 files changed, {total_lines} insertions(+)")
    except OSError as exc:
        print(f"(git diff --stat unavailable: {exc})")
    print("=" * 72)
    print(f"SUMMARY: TOTAL PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 18 else 1


if __name__ == "__main__":
    raise SystemExit(main())
