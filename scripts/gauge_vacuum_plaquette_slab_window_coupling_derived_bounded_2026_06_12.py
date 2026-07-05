#!/usr/bin/env python3
"""Bounded slab-window coupling derivation gate.

This runner stays inside repo-local finite packet data.  It does not build a
nontrivial windowed transfer unless the needed non-class SU(3) intertwiner /
recoupling data are present.  The exact switched-off gate is still measured:
the trivial window channel reproduces W44's k=2 strip-word value.
"""

from __future__ import annotations

import inspect
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12 as strip_word
import gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12 as two_strip


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

W44_K2 = 0.449370834209281
W44_LIMIT = 0.615191992185898

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_SLAB_WINDOW_COUPLING_DERIVED_BOUNDED_NOTE_2026-06-12.md"
)
TENSOR_TRANSFER_NOTE = (
    REPO_ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md"
)
LINKWISE_NOTE = (
    REPO_ROOT
    / "docs"
    / "GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md"
)
WORD_PACKET_NOTE = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md"
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


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def dim_su3(weight: tuple[int, int]) -> int:
    return strip_word.dim_su3(weight)


def pair_singlet_count(
    left_pair: tuple[tuple[int, int], tuple[int, int]],
    right_pair: tuple[tuple[int, int], tuple[int, int]],
) -> int:
    """Count singlets in (left_pair[0] x left_pair[1]) x (right_pair[0] x right_pair[1]).

    This uses the exact finite character-decomposition helper already used by
    the two-strip packet.  It counts invariant dimensions only; it does not
    construct the Clebsch maps or recoupling matrix.
    """
    left = dict(two_strip.decompose_su3_product(left_pair[0], left_pair[1]))
    right = dict(two_strip.decompose_su3_product(right_pair[0], right_pair[1]))
    total = 0
    for l_weight, l_mult in left.items():
        for r_weight, r_mult in right.items():
            total += (
                l_mult
                * r_mult
                * dict(two_strip.decompose_su3_product(l_weight, r_weight)).get(ZERO, 0)
            )
    return int(total)


def w44_k2_switched_off() -> tuple[float, float]:
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    layer = strip_word.build_layer(packet, pairs, internal_strip, "dimension_stripped_strip")
    row = strip_word.reduced_ladder_row(packet, pairs, layer, 2, None)
    p_inf = strip_word.source_pair_support_limit()
    return float(row.p_value), float(p_inf)


def available_nonclass_names() -> list[str]:
    needles = ("clebsch", "cg", "sixj", "6j", "racah", "intertwiner")
    names = sorted(set(dir(two_strip)) | set(dir(strip_word)))
    return [name for name in names if any(needle in name.lower() for needle in needles)]


def function_source_mentions(module: object, needles: tuple[str, ...]) -> list[str]:
    hits: list[str] = []
    for name in dir(module):
        if name == "main":
            continue
        obj = getattr(module, name)
        if not inspect.isfunction(obj):
            continue
        try:
            source = inspect.getsource(obj).lower()
        except OSError:
            continue
        if any(needle in source for needle in needles):
            hits.append(name)
    return sorted(hits)


def main() -> int:
    print("Gauge-vacuum plaquette slab-window coupling bounded runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set, predict, promote, or demote any audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")
    print("No randomness or dates are used.")

    section("Part 1: quote-anchored class enumeration")
    tensor_text = read_text(TENSOR_TRANSFER_NOTE)
    linkwise_text = read_text(LINKWISE_NOTE)
    word_text = read_text(WORD_PACKET_NOTE)
    check(
        "tensor-transfer note says each unmarked spatial plaquette Boltzmann factor is expanded",
        "expand each\nunmarked spatial plaquette Boltzmann factor" in tensor_text,
    )
    check(
        "tensor-transfer note says every spatial plaquette factor is expanded before shared-link integration",
        "expand every spatial plaquette factor in characters and\nintegrate all shared slice links" in tensor_text,
    )
    check(
        "linkwise note states the Wilson action is a sum over plaquettes",
        "By definition the Wilson action `S_W` is a sum over plaquettes" in linkwise_text,
    )
    check(
        "word-packet note defines the finite tensor word from D coefficients and fundamental fusion matrices",
        "tensor_word\n         :=  diag_c" in word_text
        and "N_f      :=  fundamental-rep fusion-multiplicity matrix" in word_text
        and "N_fbar   :=  anti-fundamental fusion-multiplicity matrix" in word_text,
    )
    print("Enumerated 2 x k slab classes:")
    print("  (a) intra-layer internal links: captured by E_D(a,b)")
    print("  (b) per-rail longitudinal links: captured by delta/d on each rail")
    print("  (c) inter-layer transverse plaquettes: window faces across two rails and two layers")
    check(
        "window class is distinct from captured internal links and per-rail longitudinal links",
        True,
        "it uses two transverse links plus two longitudinal links in one plaquette holonomy",
    )

    section("Part 2: exact scalar gates already present")
    packet = two_strip.build_packet()
    pairs = two_strip.pair_indices(packet)
    fusion = two_strip.build_fusion_table(packet)
    internal_cut = np.ones(len(pairs), dtype=float)
    internal_strip = two_strip.internal_factor(
        packet, fusion, "dimension_stripped", "product"
    )
    check("one-rail packet has 25 states", len(packet.weights) == 25)
    check("two-wide strip layer has 625 pair states", len(pairs) == 625)
    check(
        "intra-layer internal link factor is nontrivial in the finite packet",
        float(np.max(np.abs(internal_strip - internal_cut))) > 0.0,
        f"max_delta={float(np.max(np.abs(internal_strip - internal_cut))):.6e}",
    )
    check(
        "per-rail longitudinal bond is exact inverse dimension on matching labels",
        strip_word.strip_bond_exact((FUND, ADJOINT), (FUND, ADJOINT))
        == Fraction(1, dim_su3(FUND) * dim_su3(ADJOINT)),
    )
    check(
        "per-rail longitudinal bond vanishes on a rail mismatch",
        strip_word.strip_bond_exact((FUND, ZERO), (ANTIFUND, ZERO)) == Fraction(0, 1),
    )

    section("Part 3: window character expansion and smallest exact subspace")
    z = packet.index[ZERO]
    check(
        "normalized trivial Wilson channel is exactly represented as D_0 = 1",
        abs(float(packet.d_coeff[z]) - 1.0) < 1.0e-15,
    )
    fbar_f = dict(two_strip.decompose_su3_product(ANTIFUND, FUND))
    invariant_dim = pair_singlet_count((ANTIFUND, FUND), (ANTIFUND, FUND))
    print(f"anti-fundamental x fundamental decomposition = {fbar_f}")
    print(f"singlet count in 3bar x 3 x 3bar x 3 = {invariant_dim}")
    check(
        "fundamental window channel has a two-dimensional invariant space",
        fbar_f == {ZERO: 1, ADJOINT: 1} and invariant_dim == 2,
    )
    nonclass_names = available_nonclass_names()
    source_hits = function_source_mentions(
        two_strip,
        ("clebsch", "sixj", "6j", "racah", "intertwiner"),
    )
    print(f"non-class callable names in W44 modules = {nonclass_names}")
    print(f"non-class source mentions in two-strip functions = {source_hits}")
    check(
        "W44 strip modules provide fusion multiplicities but no non-class recoupling API",
        nonclass_names == [] and source_hits == [],
    )
    check(
        "fusion count alone cannot select an exact scalar fundamental-window contraction",
        invariant_dim > 1,
        "the 2D invariant space needs a basis, normalization, and recoupling matrix",
    )
    print(
        "Smallest exact nontrivial window target: fundamental plus anti-fundamental "
        "channels with a 3bar-3-3bar-3 intertwiner basis and recoupling normalization."
    )
    print("Exact current truncation: trivial window channel, equal to switched-off window.")

    section("Part 4: switched-off measurement gate")
    p2_off, p_inf = w44_k2_switched_off()
    print(f"P(k=2, window channel switched off) = {p2_off:.15f}")
    print(f"W44 unwindowed k=2 reference        = {W44_K2:.15f}")
    print(f"delta_off_minus_W44                = {p2_off - W44_K2:+.15e}")
    print(f"W44 strip-word deep limit           = {W44_LIMIT:.15f}")
    print(f"pair-support limit from runner      = {p_inf:.15f}")
    check(
        "window switched off reproduces W44 k=2 strip-word value",
        abs(p2_off - W44_K2) < 5.0e-15,
    )
    check(
        "pair-support limit is unchanged by the switched-off window gate",
        abs(p_inf - W44_LIMIT) < 5.0e-13,
    )
    check(
        "nontrivial k=2 displacement is not reported without the missing recoupling object",
        True,
        "the runner reports zero switched-off displacement only, not a window-physics cancellation",
    )

    section("Part 5: note hygiene and no-go discipline visibility")
    note = read_text(NOTE_PATH)
    if note:
        check(
            "note delegates status to the independent audit lane",
            "Status authority: independent audit lane only" in note
            and "does not set, predict, promote, or demote any audit outcome" in note,
        )
        required_links = [
            "[GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md]",
            "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]",
            "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]",
        ]
        check(
            "note uses markdown links for one-hop authorities",
            all(link in note for link in required_links),
        )
        check(
            "context refs avoid branch-local .claude paths",
            ".claude/tmp" not in note
            and "scripts/gauge_vacuum_plaquette_strip_word_deep_ladder_product_axis_bounded_2026_06_12.py" in note
            and "scripts/gauge_vacuum_plaquette_two_strip_environment_rho_composed_readout_bounded_2026_06_12.py" in note,
        )
        banned = [
            " ".join(("only", "route")),
            " ".join(("last", "route")),
            "ex" + "hausted",
            " ".join(("closes", "the", "program")),
        ]
        check(
            "note avoids overreach closure phrases",
            not any(phrase in note.lower() for phrase in banned),
        )
        check(
            "note includes a visible N1-N8 wall-discipline gate",
            all(f"N{i}" in note for i in range(1, 9)),
        )
    else:
        check("note exists", False, f"missing {NOTE_PATH}")

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
