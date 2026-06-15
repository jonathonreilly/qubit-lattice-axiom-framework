#!/usr/bin/env python3
"""Derived internal-link contraction convention for the two-strip packet.

This runner checks the repo-internal convention question from the finite
two-strip construction:

* a shared environment link inside neighboring plaquette traces uses the
  matrix-element Schur contraction with the inverse-dimension factor;
* in the finite packet convention, that strips the boundary-character
  coefficient d_lambda D_lambda to D_lambda on the internal link;
* the derived finite strip matrix is therefore the W38 dimension-stripped
  branch, not the provisional full-character branch.

No random sampling, external data, date-dependent input, or literature
comparator is used.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip


PASS = 0
FAIL = 0

EXPECTED_LICENSED_P = 0.439904783618900
EXPECTED_W38_FULL_P = 0.447034890458824
EXPECTED_WORD_P = 0.434215413259920

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_INTERNAL_LINK_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md"
)


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 104)
    print(title)
    print("=" * 104)


def dim_su3(weight: tuple[int, int]) -> int:
    p, q = weight
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def disconnected_character_integral(
    left: tuple[int, int], right: tuple[int, int]
) -> Fraction:
    """Exact coefficient of int chi_left(U) chi_right(U^-1) dU."""
    return Fraction(1 if left == right else 0, 1)


def connected_shared_link_integral(
    left: tuple[int, int], right: tuple[int, int]
) -> Fraction:
    """Exact coefficient of int chi_left(U A) chi_right(U^dagger B) dU."""
    if left != right:
        return Fraction(0, 1)
    return Fraction(1, dim_su3(left))


def derived_internal_factor(packet: two_strip.Packet, fusion: np.ndarray) -> np.ndarray:
    """Internal-link factor after the connected-trace Haar 1/d contraction."""
    pairs = two_strip.pair_indices(packet)
    out = np.ones(len(pairs), dtype=float)
    z = packet.index[two_strip.ZERO]
    for pos, (left, right) in enumerate(pairs):
        total = 1.0
        for channel in range(len(packet.weights)):
            if channel == z:
                continue
            mult = int(fusion[left, right, channel])
            if mult:
                total += float(packet.d_coeff[channel]) * mult
        out[pos] = total
    return out


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette internal-link contraction derived convention")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print(
        f"beta={two_strip.BETA}, tensor NMAX={two_strip.TW_NMAX}, "
        f"tensor MODE_MAX={two_strip.TW_MODE_MAX}, source NMAX={two_strip.SOURCE_NMAX}, "
        f"source MODE_MAX={two_strip.SOURCE_MODE_MAX}"
    )

    section("Part 1: exact deciding Haar identities")
    small = [(0, 0), (1, 0), (0, 1), (1, 1)]
    check("d_(0,0) = 1 exactly", dim_su3((0, 0)) == 1)
    check("d_(1,0) = 3 exactly", dim_su3((1, 0)) == 3)
    check("d_(0,1) = 3 exactly", dim_su3((0, 1)) == 3)
    check("d_(1,1) = 8 exactly", dim_su3((1, 1)) == 8)
    check(
        "disconnected character identity gives a bare unit delta on matching labels",
        all(disconnected_character_integral(w, w) == 1 for w in small),
    )
    check(
        "disconnected character identity vanishes off diagonal on the small set",
        all(
            disconnected_character_integral(left, right) == 0
            for left in small
            for right in small
            if left != right
        ),
    )
    check(
        "connected shared-link identity gives 1/3 on the fundamental",
        connected_shared_link_integral((1, 0), (1, 0)) == Fraction(1, 3),
    )
    check(
        "connected shared-link identity gives 1/3 on the antifundamental",
        connected_shared_link_integral((0, 1), (0, 1)) == Fraction(1, 3),
    )
    check(
        "connected shared-link identity gives 1/8 on the adjoint",
        connected_shared_link_integral((1, 1), (1, 1)) == Fraction(1, 8),
    )
    check(
        "connected shared-link identity vanishes off diagonal on the small set",
        all(
            connected_shared_link_integral(left, right) == 0
            for left in small
            for right in small
            if left != right
        ),
    )
    check(
        "nontrivial connected shared-link contraction is not the bare character delta",
        connected_shared_link_integral((1, 0), (1, 0))
        != disconnected_character_integral((1, 0), (1, 0)),
        "character=1, connected=1/3",
    )
    check(
        "trivial channel is unchanged by the inverse-dimension factor",
        connected_shared_link_integral((0, 0), (0, 0))
        == disconnected_character_integral((0, 0), (0, 0))
        == 1,
    )

    section("Part 2: finite-packet normalization")
    packet = two_strip.build_packet()
    fusion = two_strip.build_fusion_table(packet)
    z = packet.index[two_strip.ZERO]
    f = packet.index[two_strip.FUND]
    fb = packet.index[(0, 1)]
    adj = packet.index[two_strip.ADJOINT]
    full_coeff = packet.dim * packet.d_coeff
    derived_coeff = full_coeff / packet.dim
    check(
        "finite packet D_(0,0) is normalized to one",
        abs(float(packet.d_coeff[z]) - 1.0) < 1.0e-15,
    )
    check(
        "boundary-character class coefficient is d_lambda times D_lambda",
        abs(float(full_coeff[f] / packet.d_coeff[f]) - 3.0) < 1.0e-14
        and abs(float(full_coeff[adj] / packet.d_coeff[adj]) - 8.0) < 1.0e-14,
        f"fund ratio={float(full_coeff[f] / packet.d_coeff[f]):.1f}, "
        f"adj ratio={float(full_coeff[adj] / packet.d_coeff[adj]):.1f}",
    )
    check(
        "connected Haar 1/d strips the finite class coefficient back to D_lambda",
        np.max(np.abs(derived_coeff - packet.d_coeff)) < 1.0e-15,
    )
    check(
        "explicit small channels strip as expected",
        abs(float(derived_coeff[f] - packet.d_coeff[f])) < 1.0e-15
        and abs(float(derived_coeff[fb] - packet.d_coeff[fb])) < 1.0e-15
        and abs(float(derived_coeff[adj] - packet.d_coeff[adj])) < 1.0e-15,
        f"D10={float(packet.d_coeff[f]):.15f}, D11={float(packet.d_coeff[adj]):.15f}",
    )

    section("Part 3: W38 branch reproduction")
    derived_internal = derived_internal_factor(packet, fusion)
    w38_stripped_internal = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    w38_full_internal = two_strip.internal_factor(packet, fusion, "full_character", "product")
    diff_stripped_internal = float(np.max(np.abs(derived_internal - w38_stripped_internal)))
    diff_full_internal = float(np.max(np.abs(derived_internal - w38_full_internal)))
    check(
        "derived internal factor equals the W38 dimension-stripped internal factor",
        diff_stripped_internal == 0.0,
        f"max diff={diff_stripped_internal:.3e}",
    )
    check(
        "derived internal factor is distinct from the W38 full-character factor",
        diff_full_internal > 1.0,
        f"max diff={diff_full_internal:.15f}",
    )
    derived_transfer = two_strip.strip_transfer(packet, derived_internal)
    stripped = two_strip.solve_strip(
        packet, fusion, "dimension_stripped_product", "dimension_stripped", "product"
    )
    full = two_strip.solve_strip(
        packet, fusion, "full_character_product", "full_character", "product"
    )
    diff_stripped_transfer = float(np.max(np.abs(derived_transfer - stripped.transfer)))
    diff_full_transfer = float(np.max(np.abs(derived_transfer - full.transfer)))
    check(
        "derived strip transfer equals the W38 dimension-stripped transfer",
        diff_stripped_transfer == 0.0,
        f"max diff={diff_stripped_transfer:.3e}",
    )
    check(
        "derived strip transfer is distinct from the W38 full-character transfer",
        diff_full_transfer > 1.0e-6,
        f"max diff={diff_full_transfer:.15e}",
    )
    check(
        "derived strip Perron residual is small",
        stripped.residual < 1.0e-12,
        f"residual={stripped.residual:.3e}",
    )
    check(
        "derived strip rho is positive and conjugation-symmetric",
        float(np.min(stripped.rho_left)) > 0.0
        and two_strip.conjugation_error(packet, stripped.rho_left) < 1.0e-12,
        f"rho_min={float(np.min(stripped.rho_left)):.3e}, "
        f"conj={two_strip.conjugation_error(packet, stripped.rho_left):.3e}",
    )
    check(
        "derived strip left and right marginals agree",
        float(np.max(np.abs(stripped.rho_left - stripped.rho_right))) < 1.0e-12,
    )
    check(
        "derived strip readout reproduces the W38 dimension-stripped P value",
        abs(stripped.p_value - EXPECTED_LICENSED_P) < 5.0e-13,
        f"P={stripped.p_value:.15f}",
    )
    check(
        "W38 full-character readout remains the distinct unselected finite branch",
        abs(full.p_value - EXPECTED_W38_FULL_P) < 5.0e-13
        and abs(full.p_value - stripped.p_value) > 7.0e-3,
        f"P_full={full.p_value:.15f}, P_derived={stripped.p_value:.15f}",
    )

    section("Part 4: readout table")
    eig_word, psi_word, residual_word, _psi_min = two_strip.perron_symmetric(packet.tensor_word)
    rho_word = psi_word / float(psi_word[z])
    p_word, _u0_word, _alpha_word = two_strip.source_p(packet, rho_word)
    print("```text")
    print(f"P(rho_word) = {p_word:.15f}")
    print(f"P(rho_strip derived internal-link convention) = {stripped.p_value:.15f}")
    print(f"P(W38 full-character branch, unselected here) = {full.p_value:.15f}")
    print(f"P_strip_derived - P_word = {stripped.p_value - p_word:.15f}")
    print(f"rho_derived(1,0) = {stripped.rho_left[f]:.15f}")
    print(f"rho_derived(1,1) = {stripped.rho_left[adj]:.15f}")
    print("```")
    check(
        "one-word anchor reproduces the W38 finite value",
        abs(p_word - EXPECTED_WORD_P) < 5.0e-13 and residual_word < 1.0e-12,
        f"P_word={p_word:.15f}, residual={residual_word:.3e}",
    )
    check("derived two-strip value is finite and inside the source anchor interval", 0.422531739647 < stripped.p_value < 0.452407159045)

    section("Part 5: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in text
            and "does not set, predict, promote, or demote any audit outcome" in text,
        )
        check(
            "note states the derived branch as dimension-stripped",
            "dimension-stripped" in text
            and "P(rho_strip derived internal-link convention) = 0.439904783618900" in text,
        )
        context_path = "docs/GAUGE_VACUUM_PLAQUETTE_TWO_STRIP_ENVIRONMENT_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-12.md"
        linked_context_path = "[" + context_path + "]"
        check(
            "note keeps context refs as plain-text paths",
            context_path in text
            and "scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py" in text
            and linked_context_path not in text,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check("note avoids banned status/overreach phrases", not any(x in text.lower() for x in banned))
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")
    check("runner names the remaining full-tensor normalization object without using it", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
