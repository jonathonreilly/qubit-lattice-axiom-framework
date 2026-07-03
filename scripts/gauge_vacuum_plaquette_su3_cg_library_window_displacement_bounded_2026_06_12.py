#!/usr/bin/env python3
"""W53 SU(3) B4 fundamental-fusion CG library and window displacement.

This runner builds the deterministic SU(3) fundamental/antifundamental
Clebsch-Gordan isometry library needed by W52, evaluates the phase-insensitive
window projector factor on the B4 pair labels, and inserts the resulting
non-diagonal fundamental window bond into the existing W44 k=2 direct readout.

No random inputs, runtime dates, external data, fitted selectors, or new
literature values are used.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12 as strip_word
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip
import su3_fundamental_fusion_cg_b4 as su3cg


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)

W44_K2_ANCHOR = 0.449370834209281

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_SU3_CG_LIBRARY_WINDOW_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class WindowSolve:
    label: str
    eigenvalue: float
    residual: float
    vector_min: float
    iterations: int
    p_value: float
    rho: np.ndarray


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


def b4_transition_counts(
    packet: two_strip.Packet,
    library: su3cg.Library,
) -> tuple[int, int, int]:
    fund = 0
    anti = 0
    pair = 0
    b4_set = set(packet.weights)
    for source in packet.weights:
        f_targets = [
            target
            for target in su3cg.fundamental_outcomes(source)
            if target in b4_set and (source, target) in library.fundamental_isometries
        ]
        a_targets = [
            target
            for target in su3cg.antifundamental_outcomes(source)
            if target in b4_set and (source, target) in library.antifundamental_isometries
        ]
        fund += len(f_targets)
        anti += len(a_targets)
    for left in packet.weights:
        f_targets = [
            target
            for target in su3cg.fundamental_outcomes(left)
            if target in b4_set and (left, target) in library.fundamental_isometries
        ]
        for right in packet.weights:
            a_targets = [
                target
                for target in su3cg.antifundamental_outcomes(right)
                if target in b4_set and (right, target) in library.antifundamental_isometries
            ]
            pair += len(f_targets) * len(a_targets)
    return fund, anti, pair


def build_window_bonds(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    layer: strip_word.LayerObject,
    library: su3cg.Library,
) -> tuple[np.ndarray, np.ndarray, list[float]]:
    pair_count = len(pairs)
    zero_bond = np.zeros((pair_count, pair_count), dtype=float)
    fund_bond = np.zeros((pair_count, pair_count), dtype=float)
    pair_index = {pair: pos for pos, pair in enumerate(pairs)}
    factors: list[float] = []

    for pos in range(pair_count):
        zero_bond[pos, pos] = 1.0 / float(layer.dim_layer[pos])

    b4_set = set(packet.weights)
    for source_pos, (left_pos, right_pos) in enumerate(pairs):
        left = packet.weights[left_pos]
        right = packet.weights[right_pos]
        for left_target in su3cg.fundamental_outcomes(left):
            if left_target not in b4_set:
                continue
            fund_key = (left, left_target)
            if fund_key not in library.fundamental_isometries:
                continue
            fund_iso = library.fundamental_isometries[fund_key]
            for right_target in su3cg.antifundamental_outcomes(right):
                if right_target not in b4_set:
                    continue
                anti_key = (right, right_target)
                if anti_key not in library.antifundamental_isometries:
                    continue
                anti_iso = library.antifundamental_isometries[anti_key]
                factor = su3cg.singlet_projector_factor(
                    fund_iso,
                    anti_iso,
                    library.irreps[left].dim,
                    library.irreps[right].dim,
                )
                target_pos = pair_index[(packet.index[left_target], packet.index[right_target])]
                fund_bond[source_pos, target_pos] = factor
                factors.append(factor)
    return zero_bond, fund_bond, factors


def direct_k2_power(
    packet: two_strip.Packet,
    pairs: list[tuple[int, int]],
    layer: strip_word.LayerObject,
    bond: np.ndarray,
    label: str,
    tolerance: float = 2.0e-13,
    max_iterations: int = 1000,
) -> WindowSolve:
    n = len(packet.weights)
    d_pair = layer.d_layer.reshape(n, n)
    outer = d_pair[:, :, None, None] * d_pair[None, None, :, :]
    middle = d_pair[:, :, None, None] * bond.reshape(n, n, n, n) * d_pair[None, None, :, :]
    word_bond = np.asarray(packet.word_bond, dtype=float)

    def matvec(vec: np.ndarray) -> np.ndarray:
        arr = vec.reshape(n, n, n, n).copy()
        arr *= outer
        for axis in range(4):
            arr = strip_word.apply_axis(arr, word_bond.T, axis)
        arr *= middle
        for axis in range(4):
            arr = strip_word.apply_axis(arr, word_bond, axis)
        arr *= outer
        return arr.ravel()

    x = np.ones(n**4, dtype=float)
    x /= np.linalg.norm(x)
    iterations = 0
    for iterations in range(1, max_iterations + 1):
        y = matvec(x)
        if float(y[0]) < 0.0:
            y = -y
        norm = float(np.linalg.norm(y))
        if norm <= 1.0e-300:
            raise RuntimeError(f"{label}: zero vector in power iteration")
        y /= norm
        if float(np.max(np.abs(y - x))) < tolerance:
            x = y
            break
        x = y

    ax = matvec(x)
    eig = float(np.vdot(x, ax).real / np.vdot(x, x).real)
    residual = float(np.linalg.norm(ax - eig * x, ord=np.inf))
    if float(x[0]) < 0.0:
        x = -x
    eta_matrix = layer.eta.reshape(n, n)
    raw_pair = np.tensordot(
        x.reshape(n, n, n, n),
        eta_matrix,
        axes=([2, 3], [0, 1]),
    ).ravel()
    p_value, rho = strip_word.source_from_pair_raw(packet, pairs, raw_pair)
    return WindowSolve(
        label=label,
        eigenvalue=eig,
        residual=residual,
        vector_min=float(np.min(x)),
        iterations=iterations,
        p_value=float(p_value),
        rho=rho,
    )


def main() -> int:
    print("Gauge-vacuum plaquette W53 SU(3) CG-library window displacement runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print("No randomness or runtime dates are used.")

    section("Part 1: B4-plus-closure SU(3) irrep library")
    library = su3cg.build_library(include_closure_halo=True)
    b4 = su3cg.b4_labels()
    closure = su3cg.closure_labels()
    fconst = su3cg.structure_constants()
    b4_dims = [library.irreps[label].dim for label in b4]
    closure_dims = [library.irreps[label].dim for label in closure]
    max_comm = max(su3cg.commutator_residual(library.irreps[label], fconst) for label in b4)
    max_c2 = max(su3cg.casimir_residual(library.irreps[label]) for label in b4)
    print(f"B4 irrep count = {len(b4)}")
    print(f"one-step closure irrep count = {len(closure)}")
    print(f"B4 max dimension = {max(b4_dims)} at (4,4)")
    print(f"closure max dimension = {max(closure_dims)}")
    print(f"C2-degenerate B4 fundamental products = {library.c2_degenerate_products}")
    print(f"max B4 commutator residual = {max_comm:.3e}")
    print(f"max B4 C2 residual = {max_c2:.3e}")
    check("all 25 B4 irreps are realized", all(label in library.irreps for label in b4))
    check("B4 dimensions match the SU(3) dimension formula", all(library.irreps[label].dim == su3cg.dim_su3(label) for label in b4))
    check("B4 max dimension is dim(4,4) = 125", library.irreps[(4, 4)].dim == 125 and max(b4_dims) == 125)
    check("no B4 fundamental-product C2 degeneracy required a fallback", library.c2_degenerate_products == ())
    check("B4 generators satisfy SU(3) commutators", max_comm < 5.0e-13, f"max={max_comm:.3e}")
    check("B4 generators have the target quadratic Casimir", max_c2 < 5.0e-12, f"max={max_c2:.3e}")

    section("Part 2: fundamental and antifundamental CG isometries")
    all_isos = list(library.fundamental_isometries.values()) + list(library.antifundamental_isometries.values())
    max_intertwiner = max(iso.intertwiner_residual for iso in all_isos)
    max_orth = max(iso.orthonormal_error for iso in all_isos)
    max_projector = max(iso.projector_error for iso in all_isos)
    completeness_rows: list[tuple[tuple[int, int], str, float, int, int]] = []
    for label in b4:
        for carrier in ("fund", "antifund"):
            err, product_dim, target_sum = su3cg.completeness_residual(library, label, carrier)
            completeness_rows.append((label, carrier, err, product_dim, target_sum))
    max_completeness = max(row[2] for row in completeness_rows)
    bad_dim = [row for row in completeness_rows if row[3] != row[4]]
    w50_overlap = su3cg.w50_singlet_overlap(library)
    print(f"fundamental isometries from B4 sources = {len(library.fundamental_isometries)}")
    print(f"antifundamental isometries from B4 sources = {len(library.antifundamental_isometries)}")
    print(f"max intertwiner residual = {max_intertwiner:.3e}")
    print(f"max V^dag V - I residual = {max_orth:.3e}")
    print(f"max VV^dag - P_C2 residual = {max_projector:.3e}")
    print(f"max product completeness residual = {max_completeness:.3e}")
    print(f"W50 |<vec(I)/sqrt(3), V_(3 x 3bar -> 1)>| = {w50_overlap:.15f}")
    check("fundamental and antifundamental B4-source isometry counts are 65 each", len(library.fundamental_isometries) == 65 and len(library.antifundamental_isometries) == 65)
    check("CG isometries solve the generator intertwiner equations", max_intertwiner < 2.0e-8, f"max={max_intertwiner:.3e}")
    check("CG columns are orthonormal", max_orth < 5.0e-14, f"max={max_orth:.3e}")
    check("CG projectors equal the selected Casimir blocks", max_projector < 5.0e-14, f"max={max_projector:.3e}")
    check("full B4-source product dimensions close in the one-step halo", bad_dim == [])
    check("full B4-source products are complete", max_completeness < 5.0e-14, f"max={max_completeness:.3e}")
    check("W50 3 x 3bar -> 1 isometry matches vec(I)/sqrt(3) up to phase", abs(w50_overlap - 1.0) < 5.0e-14)

    section("Part 3: phase-insensitive B4 window bond factor")
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
    fund_count, anti_count, pair_support = b4_transition_counts(packet, library)
    zero_bond, fund_bond, factors = build_window_bonds(packet, pairs, layer, library)
    factor_min = min(factors)
    factor_max = max(factors)
    nonzero_fund_bond = int(np.count_nonzero(fund_bond))
    print(f"B4 fundamental transitions a x 3 -> c = {fund_count}")
    print(f"B4 antifundamental transitions b x 3bar -> d = {anti_count}")
    print(f"B4 pair-window support entries = {pair_support}")
    print(f"nonzero fundamental bond entries = {nonzero_fund_bond}")
    print(f"CG projector factor min/max = {factor_min:.15f} / {factor_max:.15f}")
    print("factor formula: Tr[(VV^dag x WW^dag)(P_singlet x I)] / (dim target_left dim target_right)")
    print("phase check: only VV^dag and WW^dag enter the bond factor.")
    check("generated fusion table reproduces B4 fundamental recurrences", fund_err == 0 and anti_err == 0)
    check("B4 transition counts match W52 support", fund_count == 56 and anti_count == 56 and pair_support == 3136)
    check("fundamental window bond support matches the transition product count", nonzero_fund_bond == 3136)
    check("CG projector factor is phase-insensitive and equals 1/9 on every B4 transition", abs(factor_min - 1.0 / 9.0) < 5.0e-14 and abs(factor_max - 1.0 / 9.0) < 5.0e-14)
    check("zero-window bond is the W44 diagonal inverse-dimension bond", np.count_nonzero(zero_bond) == len(pairs) and abs(zero_bond[0, 0] - 1.0) < 1.0e-15)

    section("Part 4: W44 k=2 direct readout with the non-diagonal window bond")
    f_index = packet.index[FUND]
    wilson_strength = float(packet.dim[f_index] * packet.d_coeff[f_index])
    full_bond = zero_bond + wilson_strength * fund_bond
    zero = direct_k2_power(packet, pairs, layer, zero_bond, "zero_window")
    full = direct_k2_power(packet, pairs, layer, full_bond, "trivial_plus_fundamental_window")
    displacement = full.p_value - W44_K2_ANCHOR
    sign = "positive" if displacement > 0.0 else "negative" if displacement < 0.0 else "zero"
    print(f"c_fund(6)/c_0(6) = {wilson_strength:.15f}")
    print(f"zero-window direct eig = {zero.eigenvalue:.15e}; residual={zero.residual:.3e}; iterations={zero.iterations}")
    print(f"full-window direct eig = {full.eigenvalue:.15e}; residual={full.residual:.3e}; iterations={full.iterations}")
    print(f"P(k=2, window -> 0) = {zero.p_value:.15f}")
    print(f"W44 k=2 anchor        = {W44_K2_ANCHOR:.15f}")
    print(f"delta_zero_window     = {zero.p_value - W44_K2_ANCHOR:+.15e}")
    print(f"P(k=2, windowed fundamental) = {full.p_value:.15f}")
    print(f"displacement_vs_anchor = {displacement:+.15e}")
    print(f"sign = {sign}")
    print(f"magnitude = {abs(displacement):.15e}")
    check("zero-window direct solve reproduces the W44 k=2 anchor", abs(zero.p_value - W44_K2_ANCHOR) < 5.0e-13, f"delta={zero.p_value - W44_K2_ANCHOR:+.3e}")
    check("zero-window power residual is small", zero.residual < 2.0e-13, f"residual={zero.residual:.3e}")
    check("windowed fundamental direct solve is finite", np.isfinite(full.p_value) and np.isfinite(full.eigenvalue))
    check("windowed fundamental power residual is small", full.residual < 2.0e-13, f"residual={full.residual:.3e}")
    check("windowed fundamental Perron vector is nonnegative up to tolerance", full.vector_min >= -1.0e-14, f"min={full.vector_min:.3e}")
    check("windowed fundamental displacement is reported numerically", isinstance(displacement, float) and np.isfinite(displacement))

    section("Part 5: note hygiene")
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
            "**Claim type:** bounded_theorem" in text
            and "**Status:** source proposal; independent audit required." in text
            and "**Status authority:** independent audit lane." in text
            and "**No-promotion statement:**" in text,
        )
        check("note uses markdown links for one-hop authorities", all(link in text for link in required_links))
        check(
            "context refs and script pointers are repo-local plain-text paths",
            ".claude/" not in text
            and ("Generated " + "with") not in text
            and ("PROVEN" + "ANCE") not in text
            and "scripts/su3_fundamental_fusion_cg_b4.py" in text
            and "[scripts/su3_fundamental_fusion_cg_b4.py]" not in text,
        )
        check("note avoids overreach closure phrases", not any(phrase in text.lower() for phrase in banned))
        check(
            "note does not use retained/no_go/conditional/clean status labels",
            not re.search(r"\b(retained|no_go|conditional|clean)\b", text),
        )
        check("note reports the W53 numeric displacement", "P(k=2, windowed fundamental)" in text and "displacement_vs_anchor" in text)
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
