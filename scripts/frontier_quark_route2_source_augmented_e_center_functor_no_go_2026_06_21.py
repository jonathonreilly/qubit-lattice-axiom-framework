#!/usr/bin/env python3
"""Source-augmented E-center functor no-go for the Route-2 endpoint.

The current source bank supplies the exact color scalar F_adj = 8/9.  This
runner checks whether simply adjoining that scalar to E-center-blind Route-2
endpoint data can select the E-center lift.  It cannot: all sampled readout
maps have the same source-augmented blind signature but different E-center
lifts.  A positive repair must add a typed landing edge that actually evaluates
the E-center column, or an equivalent readout primitive.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_e_center_blindness_no_go import (
    E_CENTER,
    E_SHELL,
    ReducedReadout,
    e_center_blind_signature,
)
from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    reachable,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

F_ADJ = Fraction(8, 9)
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


def source_augmented_blind_signature(
    readout: ReducedReadout,
) -> tuple[object, ...]:
    """Data visible before an E-center typed landing is supplied."""
    return (
        ("source_scalar", "F_adj", F_ADJ),
        ("source_scalar", "R_conn", F_ADJ),
        ("endpoint_blind", e_center_blind_signature(readout)),
    )


def q_e(readout: ReducedReadout) -> Fraction:
    shell = readout.apply(E_SHELL)[0]
    center = readout.apply(E_CENTER)[0]
    return center / shell


def c_te_abs(readout: ReducedReadout) -> Fraction:
    return abs(readout.center_te)


def rho_from_abs_center_ratio(c_abs: Fraction) -> Fraction:
    # With granted q_T=5/6 and shell T/E=-2, |c_TE| = (5/3) / q_E.
    q = Fraction(5, 3) / c_abs
    return 6 * (q - 1)


def main() -> int:
    print("Route-2 source-augmented E-center functor no-go")
    print("=" * 78)

    new_note = doc("QUARK_ROUTE2_SOURCE_AUGMENTED_E_CENTER_FUNCTOR_NO_GO_NOTE_2026-06-21.md")
    s3_note = doc("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    blindness_note = doc("QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    source_bridge_note = doc("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    rconn_note = doc("RCONN_DERIVED_NOTE.md")
    lift_attempt_note = doc("QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")

    print()
    print("A. Source anchors")
    print("-" * 78)
    check(
        "new note records the source-augmented blind-signature target",
        all(
            phrase in flat(new_note)
            for phrase in (
                "source-augmented blind signature",
                "typed landing edge",
                "does not select the E-center lift",
                "F_adj = 8/9",
                "functoriality no-go",
            )
        ),
    )
    check(
        "S3 gate names endpoint triple as the open theorem target",
        "readout-map endpoint triple" in s3_note
        and "not derived by the current exact stack" in s3_note
        and "not closed" in s3_note,
    )
    check(
        "E-center blindness note requires an E-center-seeing primitive",
        "blind to the E-center column cannot derive those values" in blindness_note
        and "must supply a genuine E-center lift" in blindness_note,
    )
    check(
        "source-domain bridge note names the missing typed edge",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn"
        in source_bridge_note,
    )
    check(
        "Rconn note supplies F_adj as source scalar",
        "At `N_c = 3`, `F_adj = 8/9`" in rconn_note
        and "not as a derived connected-trace observable" in flat(rconn_note),
    )
    check(
        "E-center lift attempt names the required typed E-channel computation",
        "derive gamma_E(center)/gamma_E(shell) = 15/8" in lift_attempt_note
        and "not a derivation of the bridge" in lift_attempt_note,
    )

    print()
    print("B. Source-augmented blind-signature invariance")
    print("-" * 78)
    sample_rhos = (
        Fraction(-1, 1),
        Fraction(0, 1),
        Fraction(1, 1),
        Fraction(21, 4),
        Fraction(9, 1),
    )
    signatures = [
        source_augmented_blind_signature(ReducedReadout(rho))
        for rho in sample_rhos
    ]
    first_signature = signatures[0]
    for rho, signature in zip(sample_rhos, signatures):
        readout = ReducedReadout(rho)
        check(
            f"rho_E={rho} has the same source-augmented blind signature",
            signature == first_signature,
            f"q_E={q_e(readout)}, |c_TE|={c_te_abs(readout)}",
        )
    check(
        "same source-augmented blind signature supports multiple E-center lifts",
        len({q_e(ReducedReadout(rho)) for rho in sample_rhos}) == len(sample_rhos),
    )
    check(
        "same source-augmented blind signature supports multiple center magnitudes",
        len({c_te_abs(ReducedReadout(rho)) for rho in sample_rhos}) == len(sample_rhos),
    )
    check(
        "rho_E=0 and rho_E=21/4 are indistinguishable to any blind-signature selector",
        source_augmented_blind_signature(ReducedReadout(Fraction(0)))
        == source_augmented_blind_signature(ReducedReadout(Fraction(21, 4)))
        and q_e(ReducedReadout(Fraction(0))) != q_e(ReducedReadout(Fraction(21, 4))),
    )

    print()
    print("C. What the missing typed landing would add")
    print("-" * 78)
    target = ReducedReadout(Fraction(21, 4))
    check("target q_E is 15/8", q_e(target) == Fraction(15, 8), str(q_e(target)))
    check("target center magnitude is F_adj", c_te_abs(target) == F_ADJ, str(c_te_abs(target)))
    check(
        "|c_TE|=F_adj would select the target inside endpoint algebra",
        rho_from_abs_center_ratio(F_ADJ) == Fraction(21, 4),
        str(rho_from_abs_center_ratio(F_ADJ)),
    )
    for rho in (Fraction(-1), Fraction(0), Fraction(1), Fraction(9)):
        readout = ReducedReadout(rho)
        check(
            f"rho_E={rho} shares the blind signature but fails |c_TE|=F_adj",
            c_te_abs(readout) != F_ADJ
            and source_augmented_blind_signature(readout) == first_signature,
            f"|c_TE|={c_te_abs(readout)}",
        )

    print()
    print("D. Typed-edge reachability")
    print("-" * 78)
    source = "su3_R_conn_8_9"
    center = "route2_center_TE_minus_8_9"
    rho = "route2_rho_E_21_4"
    base_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    without_center, without_center_path = reachable(base_edges, source, center)
    without_rho, without_rho_path = reachable(base_edges, source, rho)
    with_bridge, with_bridge_path = reachable(base_edges + (MISSING_BRIDGE,), source, rho)
    check("base typed bank has no source-to-center landing path", not without_center, f"path={len(without_center_path)}")
    check("base typed bank has no source-to-rho landing path", not without_rho, f"path={len(without_rho_path)}")
    check("adding the missing typed landing reaches the target", with_bridge, " -> ".join(edge.target for edge in with_bridge_path))
    check("missing typed landing is not already in the current bank", MISSING_BRIDGE not in base_edges)

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: adding source scalar F_adj to E-center-blind data still leaves the E-center lift free; a typed landing edge is required.")
        return 0
    print("VERDICT: source-augmented E-center functor checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
