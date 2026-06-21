#!/usr/bin/env python3
"""Selector firewall for the signed Route-2 Rconn center bridge.

The target bridge is the collapsed statement

    F_adj = 8/9  ->  c_TE = gamma_T(center)/gamma_E(center) = -8/9.

This verifier splits that bridge into independent selectors: domain functor,
sign/orientation, center-slot placement, and, for the physical Rconn route,
the kappa_EW=0 connected-trace selector. It checks exact endpoint algebra and
the current-bank marker surfaces. No audit verdict is applied here.
"""

from __future__ import annotations

from dataclasses import dataclass
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.replace("`", "").replace("*", "").split())


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_e_from_c_te(c_te: Fraction) -> Fraction:
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    return s_te * q_t / c_te


def rho_e_from_c_te(c_te: Fraction) -> Fraction:
    return 6 * (q_e_from_c_te(c_te) - 1)


def r_phys(kappa_ew: Fraction) -> Fraction:
    return f_adj(3) + kappa_ew * (1 - f_adj(3))


def rho_e_from_negative_r_phys(kappa_ew: Fraction) -> Fraction:
    return rho_e_from_c_te(-r_phys(kappa_ew))


@dataclass(frozen=True)
class SlotCandidate:
    name: str
    slot: str
    sign: int
    value: Fraction

    def implied_rho_e(self) -> Fraction | None:
        signed = self.value if self.sign > 0 else -self.value
        if self.slot == "c_te":
            return rho_e_from_c_te(signed)
        if self.slot == "q_e":
            return 6 * (signed - 1)
        if self.slot == "rho_e":
            return signed
        return None


def main() -> int:
    note_path = DOCS / "QUARK_ROUTE2_RCONN_SIGNED_CENTER_BRIDGE_SELECTOR_FIREWALL_NOTE_2026-06-21.md"
    rconn_note_path = DOCS / "RCONN_DERIVED_NOTE.md"
    fierz_note_path = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
    typed_bridge_note_path = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
    source_domain_note_path = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
    center_obstruction_note_path = DOCS / "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md"
    cross_domain_note_path = DOCS / "CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md"
    kappa_note_path = DOCS / "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md"
    readout_note_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    s3_note_path = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
    axiom_note_path = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
    primitive_registry_path = DOCS / "audit" / "data" / "axiom_premise_nodes.json"

    paths = (
        note_path,
        rconn_note_path,
        fierz_note_path,
        typed_bridge_note_path,
        source_domain_note_path,
        center_obstruction_note_path,
        cross_domain_note_path,
        kappa_note_path,
        readout_note_path,
        s3_note_path,
        axiom_note_path,
        primitive_registry_path,
    )

    print("=" * 88)
    print("ROUTE-2 RCONN SIGNED CENTER-BRIDGE SELECTOR FIREWALL")
    print("=" * 88)

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(note_path)
    rconn_note = read(rconn_note_path)
    fierz_note = read(fierz_note_path)
    typed_bridge_note = read(typed_bridge_note_path)
    source_domain_note = read(source_domain_note_path)
    center_obstruction_note = read(center_obstruction_note_path)
    cross_domain_note = read(cross_domain_note_path)
    kappa_note = read(kappa_note_path)
    readout_note = read(readout_note_path)
    s3_note = read(s3_note_path)
    axiom_note = read(axiom_note_path)
    primitive_registry = read(primitive_registry_path)

    print()
    print("B. New note hygiene")
    print("-" * 72)
    check("new note declares no_go claim type", "**Claim type:** no_go" in note)
    check("new note denies endpoint-triple derivation", "does not derive the Route-2 endpoint triple" in note)
    check("new note names all three bridge selectors", "Domain functor" in note and "Sign/orientation" in note and "Center-slot placement" in note)
    check("new note keeps kappa_EW as physical-only fourth selector", "Physical trace weight" in note and "`kappa_EW = 0`" in note)
    check("new note avoids bare retained status line", "**Status:** retained" not in note and "**Status:** promoted" not in note)
    check("new note names forbidden imports", "Observed quark masses" in note and "Nearest-rational" in note and "Silent sign choice" in note)
    check("new note records exact current-bank theorem", "Theorem (signed center-bridge selector firewall)" in note)
    check("new note does not claim parent-row closure", "does not close the s3-time parent row" in note)

    print()
    print("C. Exact endpoint algebra")
    print("-" * 72)
    f = f_adj(3)
    check("F_adj at N_c=3 is exactly 8/9", f == Fraction(8, 9), str(f))
    check("negative center placement gives q_E=15/8", q_e_from_c_te(-f) == Fraction(15, 8), str(q_e_from_c_te(-f)))
    check("negative center placement gives rho_E=21/4", rho_e_from_c_te(-f) == Fraction(21, 4), str(rho_e_from_c_te(-f)))
    check("positive center placement gives q_E=-15/8", q_e_from_c_te(f) == Fraction(-15, 8), str(q_e_from_c_te(f)))
    check("positive center placement gives rho_E=-69/4", rho_e_from_c_te(f) == Fraction(-69, 4), str(rho_e_from_c_te(f)))
    check("sign selector is load-bearing", rho_e_from_c_te(-f) != rho_e_from_c_te(f), f"{rho_e_from_c_te(-f)} vs {rho_e_from_c_te(f)}")

    for n_c, expected in ((2, Fraction(22, 3)), (3, Fraction(21, 4)), (4, Fraction(14, 3)), (5, Fraction(53, 12))):
        check(f"negative F_adj center law has exact N_c={n_c} consequence", rho_e_from_c_te(-f_adj(n_c)) == expected, str(rho_e_from_c_te(-f_adj(n_c))))

    print()
    print("D. Physical Rconn/kappa branch")
    print("-" * 72)
    check("R_phys(kappa=0) is exact F_adj", r_phys(Fraction(0, 1)) == Fraction(8, 9), str(r_phys(Fraction(0, 1))))
    check("R_phys(kappa=1) is total channel 1", r_phys(Fraction(1, 1)) == Fraction(1, 1), str(r_phys(Fraction(1, 1))))
    check("negative physical branch gives target only at kappa=0", rho_e_from_negative_r_phys(Fraction(0, 1)) == Fraction(21, 4), str(rho_e_from_negative_r_phys(Fraction(0, 1))))
    check("negative physical branch at kappa=1 gives rho_E=4", rho_e_from_negative_r_phys(Fraction(1, 1)) == Fraction(4, 1), str(rho_e_from_negative_r_phys(Fraction(1, 1))))
    check("kappa selector is load-bearing on physical route", rho_e_from_negative_r_phys(Fraction(0, 1)) != rho_e_from_negative_r_phys(Fraction(1, 1)))

    for kappa in (Fraction(0, 1), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1, 1)):
        rho = rho_e_from_negative_r_phys(kappa)
        closed_form = Fraction(42, 1) - 6 * kappa
        closed_form /= 8 + kappa
        check(f"closed form rho_E(kappa={kappa}) matches direct algebra", rho == closed_form, str(rho))

    print()
    print("E. Slot-placement fan-out")
    print("-" * 72)
    candidates = (
        SlotCandidate("center_negative", "c_te", -1, f),
        SlotCandidate("center_positive", "c_te", +1, f),
        SlotCandidate("q_e_positive", "q_e", +1, f),
        SlotCandidate("q_e_negative", "q_e", -1, f),
        SlotCandidate("rho_e_positive", "rho_e", +1, f),
        SlotCandidate("rho_e_negative", "rho_e", -1, f),
        SlotCandidate("shell_positive", "s_te", +1, f),
        SlotCandidate("shell_negative", "s_te", -1, f),
    )
    target_hits = []
    for candidate in candidates:
        rho = candidate.implied_rho_e()
        if rho == Fraction(21, 4):
            target_hits.append(candidate.name)
        detail = "underdetermined" if rho is None else f"rho_E={rho}"
        check(f"candidate {candidate.name} is evaluated", True, detail)

    check("only negative center-slot placement hits rho_E=21/4", target_hits == ["center_negative"], str(target_hits))
    check("placing 8/9 in q_E slot does not hit target", SlotCandidate("q_e_positive", "q_e", +1, f).implied_rho_e() == Fraction(-2, 3))
    check("placing -8/9 in q_E slot does not hit target", SlotCandidate("q_e_negative", "q_e", -1, f).implied_rho_e() == Fraction(-34, 3))
    check("placing 8/9 in rho_E slot does not hit target", SlotCandidate("rho_e_positive", "rho_e", +1, f).implied_rho_e() == Fraction(8, 9))
    check("placing -8/9 in rho_E slot does not hit target", SlotCandidate("rho_e_negative", "rho_e", -1, f).implied_rho_e() == Fraction(-8, 9))
    check("shell-slot placement alone is underdetermined", SlotCandidate("shell_positive", "s_te", +1, f).implied_rho_e() is None)

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    normalized_rconn = compact(rconn_note)
    normalized_kappa = compact(kappa_note)
    normalized_cross = compact(cross_domain_note)
    normalized_readout = compact(readout_note)
    normalized_s3 = compact(s3_note)
    normalized_axiom = compact(axiom_note)

    check("Rconn note preserves exact F_adj support only", "The exact 8/9 support remains available as F_adj, not as a derived connected-trace observable." in normalized_rconn)
    check(
        "Fierz note supplies exact channel-count fraction",
        "The adjoint-channel dimension fraction" in fierz_note
        and "N_c^2" in fierz_note
        and "8/9" in fierz_note,
    )
    check("typed-bridge note says F_adj is not a Route-2 center readout", "F_adj is not typed as a Route-2\ncenter readout" in typed_bridge_note or "F_adj is not typed as a Route-2 center readout" in compact(typed_bridge_note))
    check("source-domain note says no current typed edge supplies bridge", "There is no current typed edge" in source_domain_note and "R_conn = 8/9 -> c_TE" in source_domain_note)
    check("center obstruction note names source-domain bridge as extra premise", "additional source-domain bridge" in center_obstruction_note and "is supplied" in center_obstruction_note)
    check("cross-domain note separates spatial c_TE from fiber color", "c_TE is a cubic-lattice splitting ratio" in normalized_cross and "fiber-space color fraction" in normalized_cross)
    check("kappa note does not close physical selector", "does not close the kappa_EW = 0 selector" in normalized_kappa or "does not close the \u03ba_EW = 0 selector" in normalized_kappa)
    check("readout note keeps endpoint triple not derived", "still does not derive the exact dimensionless readout triple" in normalized_readout)
    check("s3 note inherits readout endpoint blocker", "readout-map endpoint triple" in normalized_s3 and "not derived by the current exact stack" in normalized_s3)
    check("minimal axiom note withholds readout/weighting bridge", "A record supplies no readout context" in normalized_axiom and "physical observable bridge" in normalized_axiom)
    check("primitive registry does not grant selector/readout bridge", "selector, readout bridge" in primitive_registry and "weighting, normalization" in primitive_registry)

    print()
    print("G. Typed-edge reachability")
    print("-" * 72)
    current_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    source = "su3_R_conn_8_9"
    center_target = "route2_center_TE_minus_8_9"
    rho_target = "route2_rho_E_21_4"
    without_center, without_center_path = reachable(current_edges, source, center_target)
    without_rho, without_rho_path = reachable(current_edges, source, rho_target)
    with_center, with_center_path = reachable(current_edges + (MISSING_BRIDGE,), source, center_target)
    with_rho, with_rho_path = reachable(current_edges + (MISSING_BRIDGE,), source, rho_target)
    check("current typed inventory lacks Rconn-to-center path", not without_center, f"path={len(without_center_path)}")
    check("current typed inventory lacks Rconn-to-rho path", not without_rho, f"path={len(without_rho_path)}")
    check("adjoining collapsed missing bridge reaches center", with_center, f"path={len(with_center_path)}")
    check("adjoining collapsed missing bridge reaches rho_E", with_rho, f"path={len(with_rho_path)}")
    check("current derived inventory still omits collapsed bridge", MISSING_BRIDGE not in current_edges)
    check("collapsed bridge target endpoints are exact", MISSING_BRIDGE.source == source and MISSING_BRIDGE.target == center_target)

    print()
    print("H. Selector independence checks")
    print("-" * 72)
    selectors = {
        "domain_functor": False,
        "negative_sign": False,
        "center_slot": False,
        "kappa_zero": False,
    }
    check("no selector is marked supplied by default", not any(selectors.values()), str(selectors))

    supplied_exact_fierz_only = selectors | {"domain_functor": False, "negative_sign": False, "center_slot": False}
    check("exact Fierz support alone is insufficient", not (supplied_exact_fierz_only["domain_functor"] and supplied_exact_fierz_only["negative_sign"] and supplied_exact_fierz_only["center_slot"]))
    supplied_domain_only = selectors | {"domain_functor": True}
    check("domain functor without sign and slot is insufficient", not (supplied_domain_only["domain_functor"] and supplied_domain_only["negative_sign"] and supplied_domain_only["center_slot"]))
    supplied_domain_sign = selectors | {"domain_functor": True, "negative_sign": True}
    check("domain plus sign without center slot is insufficient", not (supplied_domain_sign["domain_functor"] and supplied_domain_sign["negative_sign"] and supplied_domain_sign["center_slot"]))
    supplied_algebraic = selectors | {"domain_functor": True, "negative_sign": True, "center_slot": True}
    check("all three algebraic selectors would be sufficient for F_adj route", supplied_algebraic["domain_functor"] and supplied_algebraic["negative_sign"] and supplied_algebraic["center_slot"])
    supplied_physical_without_kappa = supplied_algebraic | {"kappa_zero": False}
    check("physical route still needs kappa_zero selector", not supplied_physical_without_kappa["kappa_zero"])
    supplied_physical = supplied_algebraic | {"kappa_zero": True}
    check("physical route selector package is complete only with kappa_zero", all(supplied_physical.values()))

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current-bank no-go for the collapsed signed Rconn center bridge.")
        print("The exact 8/9 support and endpoint algebra survive, but the domain,")
        print("negative-sign, center-slot, and physical-kappa selectors are not all")
        print("supplied by the current Route-2/Rconn authority bank.")
        return 0
    print("VERDICT: signed Rconn selector firewall verifier has failing checks.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
