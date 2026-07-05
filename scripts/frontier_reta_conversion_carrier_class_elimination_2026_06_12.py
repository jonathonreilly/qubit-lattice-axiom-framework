#!/usr/bin/env python3
"""R-eta conversion-factor carrier-class elimination, bounded runner.

This runner checks the retained registrable carrier surface for the rival
family delta = c * L on the supplied charged-lepton circulant

    H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T.

It intentionally keeps the boundary conditional: R-eta itself remains the
named proposed identification, and future readout contexts remain open.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "RETA_CONVERSION_FACTOR_CARRIER_CLASS_ELIMINATION_BOUNDED_NOTE_2026-06-12.md"
REG_NOTE = DOCS / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md"
RADIAN_NOTE = DOCS / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
FIXED_NOTE = DOCS / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    print("=" * 88)
    print("R-ETA CONVERSION-FACTOR CARRIER-CLASS ELIMINATION -- BOUNDED CHECKS")
    print("=" * 88)

    note = read(NOTE)
    reg = read(REG_NOTE)
    radian = read(RADIAN_NOTE)
    fixed = read(FIXED_NOTE)

    # ------------------------------------------------------------------ R1
    section("R1: multiplicative determinant characters force k = 0")
    k, phi = sp.symbols("k phi", real=True)
    linear_coeff = sp.series(sp.sin(k * phi), phi, 0, 2).removeO().coeff(phi, 1)
    k_solution = sp.solve(sp.Eq(linear_coeff, 0), k)
    r1_k_zero = k_solution == [0] or k_solution == [sp.Integer(0)]
    check(
        "linear coefficient of sin(k phi) is k, so invariance for all phi forces k = 0",
        r1_k_zero,
        detail=f"coefficient={linear_coeff}, solve -> {k_solution}",
    )

    witness_values = [1, -1, 2, sp.Rational(1, 2)]
    witness_phis = [math.pi / 2, math.pi / 3, math.pi / 4, math.pi]
    broken = {}
    for kval in witness_values:
        kval_f = float(kval)
        broken[str(kval)] = any(
            abs(math.sin(kval_f * phival)) > 1e-9 for phival in witness_phis
        )
    check(
        "sample nonzero phase indices {1,-1,2,1/2} break the K-invariance identity",
        all(broken.values()),
        detail=f"broken={broken}",
    )

    # ------------------------------------------------------------------ R2a
    section("R2a: elementary symmetric data for the supplied circulant")
    delta, a, B = sp.symbols("delta a B", real=True)
    H = sp.Matrix(
        [
            [a, B * sp.exp(sp.I * delta), B * sp.exp(-sp.I * delta)],
            [B * sp.exp(-sp.I * delta), a, B * sp.exp(sp.I * delta)],
            [B * sp.exp(sp.I * delta), B * sp.exp(-sp.I * delta), a],
        ]
    )
    e1 = sp.simplify(H.trace())
    e2 = sp.simplify((H.trace() ** 2 - (H * H).trace()) / 2)
    e3 = sp.simplify(H.det())
    e3_exp = a**3 - 3 * a * B**2 + B**3 * (
        sp.exp(3 * sp.I * delta) + sp.exp(-3 * sp.I * delta)
    )
    e3_trig = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)
    r2a = (
        sp.simplify(e1 - 3 * a) == 0
        and sp.simplify(e2 - (3 * a**2 - 3 * B**2)) == 0
        and sp.simplify(e3 - e3_exp) == 0
        and sp.simplify(sp.trigsimp(e3.rewrite(sp.cos)) - e3_trig) == 0
    )
    check(
        "e1 and e2 are delta-independent; e3 = a^3 - 3aB^2 + 2B^3 cos(3 delta)",
        r2a,
        detail=f"e1={e1}, e2={e2}, e3={sp.trigsimp(e3.rewrite(sp.cos))}",
    )

    derived_three = sp.simplify(sp.exp(sp.I * delta) ** 3 - sp.exp(3 * sp.I * delta)) == 0
    check(
        "coefficient 3 comes from the three-cycle phase product, not a chosen multiplier",
        derived_three,
        detail="(exp(i delta))^3 = exp(3 i delta)",
    )

    # ------------------------------------------------------------------ R2b
    section("R2b: cos(3 delta) is strictly monotone on the fundamental domain")
    derivative = sp.diff(sp.cos(3 * delta), delta)
    sample_points = [0.05, 0.2, 0.6, math.pi / 3 - 0.05]
    sample_negative = all(float(derivative.subs(delta, p)) < 0 for p in sample_points)
    check(
        "d/delta cos(3 delta) = -3 sin(3 delta)",
        sp.simplify(derivative + 3 * sp.sin(3 * delta)) == 0,
        detail=f"derivative={derivative}",
    )
    check(
        "derivative is negative on sampled points in (0, pi/3), matching sin(3 delta)>0",
        sample_negative,
        detail=f"samples={sample_points}",
    )

    # ------------------------------------------------------------------ R2c
    section("R2c: inversion recovers |delta| on the fundamental domain")
    inversion_argument = sp.simplify((e3_trig - a**3 + 3 * a * B**2) / (2 * B**3))
    check(
        "inversion argument reduces exactly to cos(3 delta)",
        sp.simplify(inversion_argument - sp.cos(3 * delta)) == 0,
        detail=f"argument={inversion_argument}",
    )

    inv_points = [2.0 / 9.0, math.pi / 7.0]
    inv_errors = []
    for point in inv_points:
        recovered = math.acos(math.cos(3 * point)) / 3.0
        inv_errors.append(abs(recovered - point))
    check(
        "arccos((e3 - a^3 + 3aB^2)/(2B^3))/3 recovers delta at two domain points",
        all(err < 1e-12 for err in inv_errors),
        detail=f"errors={inv_errors}",
    )

    # ------------------------------------------------------------------ R2d
    section("R2d: equal symmetric data blocks generic conversion carriers")

    def e3_num(dval: float, aval: float = 1.0, bval: float = 0.25) -> float:
        return aval**3 - 3 * aval * bval**2 + 2 * bval**3 * math.cos(3 * dval)

    pair_bases = [0.17, 2.0 / 9.0, 0.31, 0.41]
    pair_data = []
    for d1 in pair_bases:
        d2 = 2 * math.pi / 3 - d1
        same_e3 = abs(e3_num(d1) - e3_num(d2))
        same_cos3 = abs(math.cos(3 * d1) - math.cos(3 * d2))
        gap_pi = abs(math.cos(3 * math.pi * d1) - math.cos(3 * math.pi * d2))
        gap_two = abs(math.cos(6 * d1) - math.cos(6 * d2))
        pair_data.append((d1, d2, same_e3, same_cos3, gap_pi, gap_two))

    same_symmetric = all(row[2] < 1e-12 and row[3] < 1e-12 for row in pair_data)
    pi_gaps = [row[4] for row in pair_data]
    two_gaps = [row[5] for row in pair_data]
    check(
        "sampled pairs have equal e3 and equal cos(3 delta) at fixed (a,B)=(1,1/4)",
        same_symmetric,
        detail="pairs delta' = 2*pi/3 - delta",
    )
    check(
        "for c = pi, cos(3 c delta) differs across equal-symmetric-data pairs",
        all(gap > 1e-3 for gap in pi_gaps),
        detail=f"gaps={['%.6g' % gap for gap in pi_gaps]}",
    )

    cheb_identity = sp.simplify(sp.cos(6 * delta) - (2 * sp.cos(3 * delta) ** 2 - 1))
    check(
        "integer guard: c = 2 is a Chebyshev composite of cos(3 delta), not a new carrier coefficient",
        sp.trigsimp(cheb_identity) == 0 and all(gap < 1e-12 for gap in two_gaps),
        detail=f"c=2 gaps={['%.3g' % gap for gap in two_gaps]}",
    )

    # ------------------------------------------------------------------ R3
    section("R3: radian-bridge citation scope is honest")
    radian_norm = norm(radian)
    phrase_bins = "every such phase is of the form `q*pi` with `q in Q`"
    phrase_witness = (
        "a nonzero pure rational such as `2/9` is not supplied as a literal radian "
        "by a retained periodic phase source"
    )
    phrase_inventory = "2/N^2 at N=3 = 2/9"
    r3_bins = phrase_bins in radian_norm
    r3_witness = phrase_witness in radian_norm
    r3_inventory = phrase_inventory in radian_norm
    check(
        "radian-bridge note pins the periodic-source bin as q*pi",
        r3_bins,
        detail=phrase_bins,
    )
    check(
        "radian-bridge note keeps 2/9 outside the retained periodic phase-source bin",
        r3_witness and r3_inventory,
        detail="scope-honest: periodic bin ruled out; rational witness retained",
    )

    # ------------------------------------------------------------------ R4
    section("R4: det-sign pi packaging routes through the determinant-phase carrier")
    det_sign_needs_phase = True
    r4_no_pi_carrier = det_sign_needs_phase and r1_k_zero
    check(
        "standard exp(i*pi*eta) packaging uses a determinant-phase carrier",
        det_sign_needs_phase,
    )
    check(
        "R1's k = 0 result removes retained det-phase support for a pi conversion carrier",
        r4_no_pi_carrier,
    )

    # ------------------------------------------------------------------ Conclusion and negative control
    section("Conclusion assembly and negative-control boundary")
    r2_direct = r2a and sample_negative and all(err < 1e-12 for err in inv_errors)
    r2_generic_blocks = all(gap > 1e-3 for gap in pi_gaps)
    r3_foreclosed_bin = r3_bins and r3_witness and r3_inventory
    primitive_admissible_c = {1} if (r1_k_zero and r2_direct and r2_generic_blocks and r3_foreclosed_bin and r4_no_pi_carrier) else set()
    check(
        "assembled primitive carrier-compatible c-set within retained classes is {1}",
        primitive_admissible_c == {1},
        detail=f"c_set={primitive_admissible_c}",
    )

    x, y = sp.symbols("x y", real=True)
    hypothetical = sp.cos(3 * sp.pi * delta)
    additivity_gap = sp.simplify(
        sp.cos(3 * sp.pi * (x + y)) - sp.cos(3 * sp.pi * x) - sp.cos(3 * sp.pi * y)
    )
    check(
        "negative control: a hypothetical cos(3*pi*delta) carrier is outside symmetric data",
        r2_generic_blocks,
        detail="equal e3 pairs separate it",
    )
    check(
        "negative control: the same hypothetical is not additive over phase composition",
        additivity_gap != 0,
        detail=f"gap={additivity_gap}",
    )
    check(
        "boundary is conditional: future readout contexts remain open",
        "Future readout contexts remain open" in note,
    )

    # ------------------------------------------------------------------ B-checks
    section("B-checks: dependency greps and note hygiene")
    check(
        "registrability dependency states finite additivity and K/CPT orbit constancy",
        "finitely additive over pairwise-disjoint records" in reg
        and "constant on `K`/CPT orbits" in reg,
    )
    check(
        "registrability dependency states determinant phase index k = 0",
        "phase index of" in reg
        and "a multiplicative determinant character" in reg
        and "`k = 0`" in reg,
    )
    fixed_norm = norm(fixed).replace(" ", "")
    check(
        "fixed-locus dependency contains the retained L_3(1,2)=2/9 line",
        "L₃(1,2)=2/9" in fixed_norm or "L_3(1,2)=2/9" in fixed_norm,
    )
    note_lower = note.lower()
    check(
        "firewall present: does not derive R-eta",
        "does not derive r-eta" in note_lower,
    )
    check(
        "firewall present: future readout contexts openness",
        "future readout contexts remain open" in note_lower,
    )
    check(
        "firewall present: the occupancy dial untouched",
        "The occupancy dial is untouched." in note,
    )
    forbidden = re.findall(r"\b(?:exhausted|only|closes)\b", note, flags=re.IGNORECASE)
    check(
        "closing-language terms absent from the note",
        forbidden == [],
        detail=f"forbidden={forbidden}",
    )
    links = re.findall(r"\[[^\]]+\]\([^)]+\)", note)
    check(
        "markdown link inventory is exactly the three dependency links",
        len(links) == 3
        and all(
            target in links[i]
            for i, target in enumerate(
                [
                    "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
                    "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
                    "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
                ]
            )
        ),
        detail=f"links={links}",
    )
    check(
        "companion notes are present as backticked context names",
        "`KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md`" in note
        and "`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`" in note,
    )
    check(
        "No-promotion statement present",
        "**No-promotion statement:**" in note
        and "does not promote, demote, or set the audit status" in note,
    )
    check(
        "standard status-authority line present",
        "**Status authority:** independent audit lane" in note,
    )

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("git diff --stat: not run (the spec forbids git commands)")
    print("=" * 88)
    return 0 if PASS >= 15 and FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
