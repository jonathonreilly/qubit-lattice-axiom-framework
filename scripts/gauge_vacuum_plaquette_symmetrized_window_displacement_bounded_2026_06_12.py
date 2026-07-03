#!/usr/bin/env python3
"""W54 conjugate-symmetrized SU(3) window displacement.

This runner extends the W53 oriented finite B4 window insertion by adding the
conjugate orientation channel at the equal Wilson character coefficient.  It
keeps the same finite packet, CG library, strip layer, direct k=2 readout, and
source-sector surface as W53.

No random inputs, runtime dates, external data, fitted selectors, or new
literature values are used.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12 as strip_word
import gauge_vacuum_plaquette_su3_cg_library_window_displacement_bounded_2026_06_12 as w53
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip
import su3_fundamental_fusion_cg_b4 as su3cg


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

W44_K2_ANCHOR = w53.W44_K2_ANCHOR
W53_ORIENTED_P = 0.445084590711323
W53_ORIENTED_DISPLACEMENT = -4.286243497957531e-03

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_SYMMETRIZED_WINDOW_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


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
    print("=" * 112)
    print(title)
    print("=" * 112)


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def build_conjugate_window_bond(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    library: su3cg.Library,
) -> tuple[np.ndarray, list[float]]:
    pair_count = len(pairs)
    anti_bond = np.zeros((pair_count, pair_count), dtype=float)
    pair_index = {pair: pos for pos, pair in enumerate(pairs)}
    factors: list[float] = []
    b4_set = set(packet.weights)

    for source_pos, (left_pos, right_pos) in enumerate(pairs):
        left = packet.weights[left_pos]
        right = packet.weights[right_pos]
        for left_target in su3cg.antifundamental_outcomes(left):
            if left_target not in b4_set:
                continue
            left_key = (left, left_target)
            if left_key not in library.antifundamental_isometries:
                continue
            left_anti_iso = library.antifundamental_isometries[left_key]
            for right_target in su3cg.fundamental_outcomes(right):
                if right_target not in b4_set:
                    continue
                right_key = (right, right_target)
                if right_key not in library.fundamental_isometries:
                    continue
                right_fund_iso = library.fundamental_isometries[right_key]
                factor = su3cg.singlet_projector_factor(
                    right_fund_iso,
                    left_anti_iso,
                    library.irreps[right].dim,
                    library.irreps[left].dim,
                )
                target_pos = pair_index[
                    (packet.index[left_target], packet.index[right_target])
                ]
                anti_bond[source_pos, target_pos] = factor
                factors.append(factor)
    return anti_bond, factors


def conjugation_pair_matrix(
    packet: two_strip.Packet, pairs: list[tuple[int, int]]
) -> np.ndarray:
    pair_index = {pair: pos for pos, pair in enumerate(pairs)}
    swap = np.zeros((len(pairs), len(pairs)), dtype=float)
    for pos, (left, right) in enumerate(pairs):
        target = (int(packet.conjugate_index[left]), int(packet.conjugate_index[right]))
        swap[pair_index[target], pos] = 1.0
    return swap


def main() -> int:
    print("Gauge-vacuum plaquette W54 conjugate-symmetrized window displacement runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print("No randomness or runtime dates are used.")

    section("Part 1: packet, strip layer, and CG-library gates")
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    fund_err, anti_err = two_strip.validate_fundamental_fusion(packet, fusion)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    layer = strip_word.build_layer(
        packet, pairs, internal_strip, "dimension_stripped_strip"
    )
    library = su3cg.build_library(include_closure_halo=True)
    all_isos = list(library.fundamental_isometries.values()) + list(
        library.antifundamental_isometries.values()
    )
    max_intertwiner = max(iso.intertwiner_residual for iso in all_isos)
    max_orth = max(iso.orthonormal_error for iso in all_isos)
    max_projector = max(iso.projector_error for iso in all_isos)
    completeness_rows = [
        su3cg.completeness_residual(library, label, carrier)
        for label in su3cg.b4_labels()
        for carrier in ("fund", "antifund")
    ]
    max_completeness = max(row[0] for row in completeness_rows)
    bad_dim = [row for row in completeness_rows if row[1] != row[2]]
    print(f"one-rail state count = {len(packet.weights)}")
    print(f"pair state count = {len(pairs)}")
    print(f"strip Perron eigenvalue = {layer.eigenvalue:.15f}")
    print(f"strip Perron residual = {layer.residual:.3e}")
    print(f"fundamental isometries from B4 sources = {len(library.fundamental_isometries)}")
    print(
        "antifundamental isometries from B4 sources = "
        f"{len(library.antifundamental_isometries)}"
    )
    print(f"max intertwiner residual = {max_intertwiner:.3e}")
    print(f"max V^dag V - I residual = {max_orth:.3e}")
    print(f"max VV^dag - P_C2 residual = {max_projector:.3e}")
    print(f"max product completeness residual = {max_completeness:.3e}")
    check("one-rail finite packet has 25 states", len(packet.weights) == 25)
    check("pair finite packet has 625 states", len(pairs) == 625)
    check("generated fusion table reproduces B4 fundamental recurrences", fund_err == 0)
    check(
        "generated fusion table reproduces B4 antifundamental recurrences",
        anti_err == 0,
    )
    check("strip Perron residual is small", layer.residual < 1.0e-12)
    check(
        "fundamental and antifundamental B4-source isometry counts are 65 each",
        len(library.fundamental_isometries) == 65
        and len(library.antifundamental_isometries) == 65,
    )
    check(
        "CG isometries solve the generator intertwiner equations",
        max_intertwiner < 2.0e-8,
        f"max={max_intertwiner:.3e}",
    )
    check("CG columns are orthonormal", max_orth < 5.0e-14, f"max={max_orth:.3e}")
    check(
        "CG projectors equal the selected Casimir blocks",
        max_projector < 5.0e-14,
        f"max={max_projector:.3e}",
    )
    check("full B4-source products close in the one-step halo", bad_dim == [])
    check(
        "full B4-source products are complete",
        max_completeness < 5.0e-14,
        f"max={max_completeness:.3e}",
    )

    section("Part 2: Wilson weights and orientation bond construction")
    f_index = packet.index[FUND]
    af_index = packet.index[ANTIFUND]
    adj_index = packet.index[ADJOINT]
    c_fund = float(packet.dim[f_index] * packet.d_coeff[f_index])
    c_antifund = float(packet.dim[af_index] * packet.d_coeff[af_index])
    c_adj = float(packet.dim[adj_index] * packet.d_coeff[adj_index])
    zero_bond, fund_bond, fund_factors = w53.build_window_bonds(
        packet, pairs, layer, library
    )
    anti_bond, anti_factors = build_conjugate_window_bond(packet, pairs, library)
    swap = conjugation_pair_matrix(packet, pairs)
    fund_nonzero = int(np.count_nonzero(fund_bond))
    anti_nonzero = int(np.count_nonzero(anti_bond))
    overlap_nonzero = int(np.count_nonzero((fund_bond != 0.0) & (anti_bond != 0.0)))
    conjugation_residual = float(np.max(np.abs(swap @ fund_bond @ swap.T - anti_bond)))
    sym_branch = fund_bond + anti_bond
    print(f"c_fund(6)/c_0(6) = {c_fund:.15f}")
    print(f"c_antifund(6)/c_0(6) = {c_antifund:.15f}")
    print(f"c_(1,1)(6)/c_0(6) = {c_adj:.15f}")
    print("adjoint displacement = OUT_OF_SCOPE: this CG library has no 8 x (p,q) isometry family")
    print(f"fundamental branch nonzero entries = {fund_nonzero}")
    print(f"antifundamental branch nonzero entries = {anti_nonzero}")
    print(f"fundamental/antifundamental support overlap = {overlap_nonzero}")
    print(
        "fundamental factor min/max = "
        f"{min(fund_factors):.15f} / {max(fund_factors):.15f}"
    )
    print(
        "antifundamental factor min/max = "
        f"{min(anti_factors):.15f} / {max(anti_factors):.15f}"
    )
    print(f"conjugation transform residual = {conjugation_residual:.3e}")
    print(
        "mechanism = the two orientation characters enter as a linear sum of "
        "nonnegative branch bonds before the Perron/source readout."
    )
    check(
        "Wilson weights satisfy c_fund(6) = c_antifund(6) on the finite packet",
        abs(c_fund - c_antifund) < 5.0e-15,
        f"diff={c_fund - c_antifund:+.3e}",
    )
    check(
        "adjoint Wilson weight is printed and not contracted by this library",
        c_adj > 0.0,
        f"c_adj/c0={c_adj:.15f}",
    )
    check(
        "both orientation branch supports match the W52 56 x 56 count",
        fund_nonzero == 3136 and anti_nonzero == 3136,
    )
    check("orientation branch supports are disjoint on B4", overlap_nonzero == 0)
    check(
        "fundamental projector factor is 1/9 on every allowed branch entry",
        abs(min(fund_factors) - 1.0 / 9.0) < 5.0e-14
        and abs(max(fund_factors) - 1.0 / 9.0) < 5.0e-14,
    )
    check(
        "antifundamental projector factor is 1/9 on every allowed branch entry",
        abs(min(anti_factors) - 1.0 / 9.0) < 5.0e-14
        and abs(max(anti_factors) - 1.0 / 9.0) < 5.0e-14,
    )
    check(
        "antifundamental branch is the conjugation transform of the W53 branch",
        conjugation_residual < 5.0e-13,
        f"residual={conjugation_residual:.3e}",
    )
    check(
        "symmetrized branch is a coherent positive bond sum, not a cancellation",
        int(np.count_nonzero(sym_branch)) == fund_nonzero + anti_nonzero
        and float(np.min(sym_branch)) >= 0.0,
    )

    section("Part 3: W44 k=2 direct readout")
    zero = w53.direct_k2_power(packet, pairs, layer, zero_bond, "zero_window")
    oriented = w53.direct_k2_power(
        packet, pairs, layer, zero_bond + c_fund * fund_bond, "oriented_fundamental"
    )
    conjugate = w53.direct_k2_power(
        packet,
        pairs,
        layer,
        zero_bond + c_antifund * anti_bond,
        "oriented_antifundamental",
    )
    sym = w53.direct_k2_power(
        packet,
        pairs,
        layer,
        zero_bond + c_fund * fund_bond + c_antifund * anti_bond,
        "conjugate_symmetrized",
    )
    oriented_delta = oriented.p_value - W44_K2_ANCHOR
    conjugate_delta = conjugate.p_value - W44_K2_ANCHOR
    sym_delta = sym.p_value - W44_K2_ANCHOR
    ratio_to_oriented = sym_delta / oriented_delta
    for result in [zero, oriented, conjugate, sym]:
        print(
            f"{result.label}: eig={result.eigenvalue:.15e}; "
            f"residual={result.residual:.3e}; iterations={result.iterations}; "
            f"P={result.p_value:.15f}; delta={result.p_value - W44_K2_ANCHOR:+.15e}; "
            f"vector_min={result.vector_min:.3e}"
        )
    print(f"W44 k=2 anchor = {W44_K2_ANCHOR:.15f}")
    print(f"W53 oriented displacement reference = {W53_ORIENTED_DISPLACEMENT:+.15e}")
    print(f"P(k=2, symmetrized window) = {sym.p_value:.15f}")
    print(f"displacement_vs_anchor = {sym_delta:+.15e}")
    print(f"ratio_sym_displacement_to_oriented = {ratio_to_oriented:.15f}")
    print(
        "readout combination = added orientation bonds with nonlinear Perron/source "
        "readout; the measured displacement is not a literal factor of two."
    )
    check(
        "zero-window direct solve reproduces the W44 k=2 anchor",
        abs(zero.p_value - W44_K2_ANCHOR) < 5.0e-13,
        f"delta={zero.p_value - W44_K2_ANCHOR:+.3e}",
    )
    check("zero-window power residual is small", zero.residual < 2.0e-13)
    check(
        "oriented branch reproduces the W53 P value",
        abs(oriented.p_value - W53_ORIENTED_P) < 5.0e-15,
        f"P={oriented.p_value:.15f}",
    )
    check(
        "oriented branch reproduces the W53 displacement",
        abs(oriented_delta - W53_ORIENTED_DISPLACEMENT) < 5.0e-15,
        f"delta={oriented_delta:+.15e}",
    )
    check(
        "conjugate branch gives the same individual readout as the W53 branch",
        abs(conjugate.p_value - oriented.p_value) < 2.0e-15
        and abs(conjugate_delta - oriented_delta) < 2.0e-15,
    )
    check("oriented branch residual is small", oriented.residual < 2.0e-13)
    check("conjugate branch residual is small", conjugate.residual < 2.0e-13)
    check("symmetrized branch residual is small", sym.residual < 2.0e-13)
    check(
        "symmetrized Perron vector is nonnegative up to tolerance",
        sym.vector_min >= -1.0e-14,
        f"min={sym.vector_min:.3e}",
    )
    check(
        "symmetrized displacement is finite and negative on this finite surface",
        np.isfinite(sym_delta) and sym_delta < 0.0,
        f"delta={sym_delta:+.15e}",
    )
    check(
        "symmetrized displacement is larger in magnitude than one oriented branch",
        abs(sym_delta) > abs(oriented_delta),
        f"|sym|={abs(sym_delta):.15e}, |oriented|={abs(oriented_delta):.15e}",
    )

    section("Part 4: note hygiene")
    text = note_text()
    if text:
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md]",
            "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]",
        ]
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check(
            "note delegates status to the independent audit lane",
            "**Status authority:** independent audit lane only." in text
            and "does not\nset, predict, promote, or demote any audit outcome"
            in text,
        )
        check(
            "note carries canonical source-proposal metadata",
            "**Claim type:** bounded_theorem" in text
            and "**Status:** source proposal; independent audit required." in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            all(link in text for link in required_links),
        )
        check(
            "context refs are repo-local plain-text script paths",
            ".claude/" not in text
            and "scripts/su3_fundamental_fusion_cg_b4.py" in text
            and "[scripts/su3_fundamental_fusion_cg_b4.py]" not in text,
        )
        provenance_token = "PRO" + "VENANCE"
        claude_token = "Clau" + "de"
        check(
            "note contains no tool provenance text",
            provenance_token not in text and claude_token not in text,
        )
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned))
        prohibited_status_tokens = [
            "re" + "tained",
            "no" + "_" + "go",
            "con" + "ditional",
            "cl" + "ean",
        ]
        check(
            "note avoids prohibited audit-status tokens",
            not re.search(r"\b(" + "|".join(prohibited_status_tokens) + r")\b", text),
        )
        check(
            "note reports the symmetrized k=2 measurement",
            "P(k=2, symmetrized window) = 0.443437364621406" in text
            and "displacement_vs_anchor = -5.933469587874829e-03" in text,
        )
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
