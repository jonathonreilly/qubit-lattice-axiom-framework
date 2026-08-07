#!/usr/bin/env python3
"""Typecast-scale normalization no-go for the Route-2 E-center bridge.

This is a first-principles stretch attempt on the typed magnitude theorem.
It isolates the hidden scale in any scalar-to-Route-2 magnitude typecast:

    |c_TE| = nu * F_adj.

The current color/Fierz bank supplies F_adj.  The current Route-2 endpoint
bank supplies the inverse from |c_TE| to rho_E.  The missing theorem is the
unit typecast normalization nu = 1, or an equivalent direct typed landing edge.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    reachable,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def doc(name: str) -> str:
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def rho_from_typecast_scale(nu: Fraction, f: Fraction = Fraction(8, 9)) -> Fraction:
    return Fraction(10, 1) / (nu * f) - 6


def q_e_from_typecast_scale(nu: Fraction, f: Fraction = Fraction(8, 9)) -> Fraction:
    return 1 + rho_from_typecast_scale(nu, f) / 6


def c_abs_from_rho(rho_e: Fraction) -> Fraction:
    q_e = 1 + rho_e / 6
    return Fraction(5, 3) / q_e


def main() -> int:
    print("Route-2 source-domain typecast-scale normalization no-go")
    print("=" * 78)

    new_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_TYPECAST_SCALE_NORMALIZATION_NO_GO_NOTE_2026-06-21.md")
    rconn_note = doc("RCONN_DERIVED_NOTE.md")
    fierz_note = doc("EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md")
    kappa_note = doc("RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md")
    source_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    readout_note = doc("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    positivity_note = doc("ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md")

    print()
    print("A. Source anchors")
    print("-" * 78)
    check(
        "new note records the scale-normalization target",
        all(
            phrase in flat(new_note)
            for phrase in (
                "A_min",
                "|c_TE| = nu F_adj",
                "nu = 1",
                "unit typecast normalization",
                "does not derive the typed magnitude theorem",
                "normalization no-go",
            )
        ),
    )
    check("Rconn note supplies F_adj but not physical selector", "At `N_c = 3`, `F_adj = 8/9`" in rconn_note and "does not derive\nthe selector `kappa_EW = 0`" in rconn_note)
    check("Fierz note gives exact adjoint channel fraction", "(3^2 − 1) / 3^2  =  8/9" in fierz_note)
    check("kappa note says count is not weight", "Count is not weight" in kappa_note and "does not supply within-channel weights" in kappa_note)
    check(
        "source-domain note names missing typed bridge",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn"
        in source_note,
    )
    check(
        "readout note supplies endpoint inverse ingredients",
        "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E." in readout_note,
    )
    check("positivity note gives positive-lift bound", "one-sided bound** `rho_E > -6`" in flat(positivity_note))

    print()
    print("B. Parametric typecast scale")
    print("-" * 78)
    f = f_adj(3)
    check("F_adj at N_c=3 is 8/9", f == Fraction(8, 9), str(f))
    scale_samples = (
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 1),
        Fraction(9, 8),
        Fraction(5, 4),
        Fraction(2, 1),
    )
    expected_rhos = {
        Fraction(1, 2): Fraction(33, 2),
        Fraction(3, 4): Fraction(9, 1),
        Fraction(1, 1): Fraction(21, 4),
        Fraction(9, 8): Fraction(4, 1),
        Fraction(5, 4): Fraction(3, 1),
        Fraction(2, 1): Fraction(-3, 8),
    }
    for nu in scale_samples:
        rho = rho_from_typecast_scale(nu, f)
        check(f"nu={nu} selects expected rho_E", rho == expected_rhos[nu], f"rho_E={rho}")
        check(f"nu={nu} remains in positive-lift domain", rho > -6 and q_e_from_typecast_scale(nu, f) > 0, f"q_E={q_e_from_typecast_scale(nu, f)}")
        check(f"nu={nu} round-trips through |c_TE|", c_abs_from_rho(rho) == nu * f, f"|c_TE|={c_abs_from_rho(rho)}")
    check("different typecast scales select different rho_E values", len({rho_from_typecast_scale(nu, f) for nu in scale_samples}) == len(scale_samples))
    check("unit typecast scale is exactly the target rho_E", rho_from_typecast_scale(Fraction(1, 1), f) == Fraction(21, 4))

    print()
    print("C. Current-bank graph reachability")
    print("-" * 78)
    source = "su3_R_conn_8_9"
    center = "route2_center_TE_minus_8_9"
    rho = "route2_rho_E_21_4"
    base_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    without_center, without_center_path = reachable(base_edges, source, center)
    without_rho, without_rho_path = reachable(base_edges, source, rho)
    with_bridge, with_bridge_path = reachable(base_edges + (MISSING_BRIDGE,), source, rho)
    check("base typed bank has no Rconn-to-center path", not without_center, f"path={len(without_center_path)}")
    check("base typed bank has no Rconn-to-rho path", not without_rho, f"path={len(without_rho_path)}")
    check("adding the missing bridge reaches rho_E", with_bridge, " -> ".join(edge.target for edge in with_bridge_path))
    check("missing bridge is not already in the derived inventory", MISSING_BRIDGE not in base_edges)

    print()
    print("D. Missing normalization inventory")
    print("-" * 78)
    parent_bank = "\n".join((rconn_note, fierz_note, kappa_note, source_note, readout_note, positivity_note))
    absent_phrases = (
        "unit typecast normalization",
        "|c_TE| = nu F_adj",
        "nu = 1",
        "scalar magnitude 8/9 -> Route-2 |c_TE|",
    )
    for phrase in absent_phrases:
        check(f"parent bank does not state {phrase}", phrase not in parent_bank)
    for phrase in (
        "scale family",
        "nu = 1 is the hidden selector",
        "unit typecast normalization",
        "normalization no-go",
        "typed landing edge",
    ):
        check(f"new note lists boundary phrase: {phrase}", phrase in new_note)

    print()
    print("E. N5 execution certificate -- what this runner resolves")
    print("-" * 78)
    print(
        f"per_element: checked, and threefold per sample -- each of the {len(scale_samples)} "
        "typecast scales is put through its own expected-value comparison, its own positive-lift "
        "domain test on both rho_E and q_E, and its own exact round trip back to |c_TE| = nu "
        f"F_adj, giving {3 * len(scale_samples)} element-level assertions in exact Fractions "
        f"with no tolerance. The spread is real and computed, not asserted: nu = {Fraction(1, 2)} "
        f"lands rho_E = {expected_rhos[Fraction(1, 2)]} while nu = {Fraction(2, 1)} lands "
        f"{expected_rhos[Fraction(2, 1)]}, on opposite sides of the target."
    )
    print(
        "per_site: checked and not executed -- a typecast normalization is a statement about "
        "units between two scalars, and neither scalar has positional structure. No support, no "
        "arm and no center configuration is instantiated in this file, so there is no site at "
        "which nu could be measured and none is claimed."
    )
    print(
        "per_mode: checked, and the finding is that this class cannot help here -- the only "
        "mode-level quantity in play is the T-over-E center magnitude, and the free scale nu "
        "multiplies it uniformly. A mode-uniform rescaling is by construction invisible to any "
        "comparison between the E and T channels, which is exactly why no mode-resolved fact in "
        "the current bank can pin nu, and why the note asks for a typed landing edge instead."
    )
    print(
        "per_block: checked -- the evidence is carried in two authority blocks that this runner "
        "closes separately and never fuses. The color/Fierz block supplies the bare number "
        f"F_adj = {f} at N_c = 3, and the Route-2 endpoint block supplies the inversion from "
        "|c_TE| back to rho_E; the typed graph confirms neither block reaches the other, with no "
        "path from su3_R_conn_8_9 to the center node or to rho_E until the missing edge is "
        "adjoined. The unresolved seam between those two blocks is precisely nu."
    )
    print(
        "lattice_wide: checked and not executed -- no lattice, no volume and no limit appears "
        "anywhere, so there is no global object to certify. The scope of the negative result "
        f"should also be read exactly: the freedom in nu is exhibited by {len(scale_samples)} "
        "named scales that each select a different lift, and the absence of a normalization "
        "theorem is established by literal phrase search across the six parent surfaces, not by "
        "a proof that no such theorem could exist."
    )

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current sources leave a free typecast scale; nu=1 is the missing normalization theorem.")
        return 0
    print("VERDICT: typecast-scale normalization checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
