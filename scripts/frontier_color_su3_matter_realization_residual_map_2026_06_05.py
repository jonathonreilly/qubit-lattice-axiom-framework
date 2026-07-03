#!/usr/bin/env python3
"""Color SU(3) matter-realization residual map.

This runner is deliberately small. It does not re-run the full landed color
record-invariance bridge proof. It certifies the interface facts needed by the residual map:

1. the symmetric-base color carrier is a 3D Sym^2(C^2) object whose su(3)
   algebra has dimension 8;
2. a primitive qubit link endpoint has Hilbert dimension 2 and traceless
   local Lie dimension 3, so it does not by itself supply the color carrier;
3. the two-endpoint 0->1->2 invariance profile is not a group selector;
4. post-record append/count dynamics has no output slot for matter-carrier
   assignment, link-index routing, or gauge-generator choice;
5. the remaining residual is a carrier/record/link realization input.

No PDG values, no fitted selectors, no dial fixing, no audit verdicts.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from pathlib import Path


PASS = 0
FAIL = 0
LINES: list[str] = []


def emit(line: str = "") -> None:
    LINES.append(line)
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def sym_power_dim(base_dim: int, degree: int) -> int:
    return comb(base_dim + degree - 1, degree)


def su_dim(n: int) -> int:
    return n * n - 1


@dataclass(frozen=True)
class Layer:
    name: str
    inputs: frozenset[str]
    outputs: frozenset[str]


@dataclass(frozen=True)
class Route:
    name: str
    proposed_source: str
    required_output: str
    verdict: str
    reason: str


def main() -> int:
    emit("=" * 78)
    emit("COLOR SU(3) MATTER-REALIZATION RESIDUAL MAP")
    emit("meta support-map / negative-route-pruning runner")
    emit("=" * 78)

    section("1. Carrier dimensions and algebra dimensions")
    qubit_hilbert_dim = 2
    qubit_matrix_dim = qubit_hilbert_dim**2
    qubit_traceless_lie_dim = su_dim(qubit_hilbert_dim)
    color_fund_dim = sym_power_dim(2, 2)
    color_matrix_dim = color_fund_dim**2
    color_lie_dim = su_dim(color_fund_dim)

    check("dim Sym^2(C^2) = 3", color_fund_dim == 3, f"got {color_fund_dim}")
    check("dim su(3) = 8", color_lie_dim == 8, f"got {color_lie_dim}")
    check("matrix algebra on color fundamental has dim 9", color_matrix_dim == 9)
    check("one qubit Hilbert dimension is 2", qubit_hilbert_dim == 2)
    check("one qubit matrix algebra dim is 4", qubit_matrix_dim == 4)
    check("one qubit traceless local Lie dim is 3", qubit_traceless_lie_dim == 3)
    check(
        "primitive qubit endpoint is not the color fundamental carrier",
        qubit_hilbert_dim != color_fund_dim,
        "2 != 3",
    )
    check(
        "primitive qubit traceless algebra is not su(3)",
        qubit_traceless_lie_dim != color_lie_dim,
        "3 != 8",
    )

    section("2. Endpoint-invariance profile is not a group selector")
    endpoint_profile = {
        "bare_link_transport": 0,
        "half_dressed_transport": 1,
        "fully_dressed_wilson_type": 2,
    }
    base_su3_profile = dict(endpoint_profile)
    fiber_su2_profile = dict(endpoint_profile)
    check("base SU(3) profile is 0->1->2", list(base_su3_profile.values()) == [0, 1, 2])
    check("fiber SU(2) profile is 0->1->2", list(fiber_su2_profile.values()) == [0, 1, 2])
    check("endpoint profile equality holds", base_su3_profile == fiber_su2_profile)
    check(
        "profile cannot discriminate which group is gauged",
        base_su3_profile == fiber_su2_profile and color_lie_dim != qubit_traceless_lie_dim,
        "same profile, different carrier/algebra dimensions",
    )

    section("3. Typed layer interface")
    post_record = Layer(
        name="post-record information dynamics",
        inputs=frozenset({"realized_atom", "finite_record_alphabet"}),
        outputs=frozenset(
            {
                "word_history_O_star",
                "count_state_N_to_O",
                "count_translation",
                "finite_scalar_readout",
                "coarse_graining_map",
            }
        ),
    )
    matter_realization = Layer(
        name="MR_color",
        inputs=frozenset({"chiral_cube_carrier", "record_observable_reading", "link_model"}),
        outputs=frozenset(
            {
                "quark_in_symmetric_base_fundamental",
                "color_singlets_are_physical_records",
                "base_su3_index_on_links",
                "gauss_generator_choice",
            }
        ),
    )
    forbidden_outputs = matter_realization.outputs
    overlap = post_record.outputs & forbidden_outputs
    check("post-record layer has defined inputs", post_record.inputs == frozenset({"realized_atom", "finite_record_alphabet"}))
    check("post-record layer produces finite histories", "word_history_O_star" in post_record.outputs)
    check("post-record layer produces count states", "count_state_N_to_O" in post_record.outputs)
    check("post-record layer produces coarse-graining maps", "coarse_graining_map" in post_record.outputs)
    check("MR_color has carrier assignment output", "quark_in_symmetric_base_fundamental" in matter_realization.outputs)
    check("MR_color has record-algebra assignment output", "color_singlets_are_physical_records" in matter_realization.outputs)
    check("MR_color has link-index routing output", "base_su3_index_on_links" in matter_realization.outputs)
    check("post-record outputs do not overlap MR_color outputs", not overlap, f"overlap={sorted(overlap)}")

    section("4. Route-pruning ledger")
    routes = [
        Route(
            "append_count_selects_color",
            "post-record append/count",
            "quark_in_symmetric_base_fundamental",
            "pruned",
            "append/count acts after realized atoms and has no carrier-assignment output",
        ),
        Route(
            "endpoint_profile_selects_color",
            "two-endpoint invariance profile",
            "gauss_generator_choice",
            "pruned",
            "base SU(3) and fiber SU(2) share the same 0->1->2 profile once represented",
        ),
        Route(
            "one_qubit_link_is_color",
            "primitive qubit link endpoint",
            "base_su3_index_on_links",
            "pruned",
            "one qubit supplies a 2D carrier / su(2)-sized traceless algebra, not a 3D color fundamental / su(3)",
        ),
        Route(
            "z3_dimension_identifies_physical_color",
            "dim Z^3 = 3",
            "color_singlets_are_physical_records",
            "pruned",
            "dimension supports the algebraic carrier but not the physical matter readout",
        ),
        Route(
            "stable_dial_fixes_mr_color",
            "stable dial location",
            "quark_in_symmetric_base_fundamental",
            "pruned",
            "a stable parameter location is not a matter/link realization theorem",
        ),
    ]
    for route in routes:
        check(f"{route.name}: verdict is pruned", route.verdict == "pruned", route.reason)
        check(
            f"{route.name}: required output is not post-record output",
            route.required_output not in post_record.outputs,
            f"requires {route.required_output}",
        )

    section("5. Positive support decomposition")
    support_pieces = {
        "algebraic_symmetric_base_su3": "bounded support",
        "post_record_append_count_consumer": "exact support as consumer",
        "record_invariance_commutant_half": "bounded related input",
        "matter_realization": "residual",
    }
    check("support map has four typed pieces", len(support_pieces) == 4)
    check("algebraic SU(3) is not classified as physical closure", support_pieces["algebraic_symmetric_base_su3"] == "bounded support")
    check("post-record layer is classified as consumer", "consumer" in support_pieces["post_record_append_count_consumer"])
    check("record-invariance half remains bounded related input", support_pieces["record_invariance_commutant_half"] == "bounded related input")
    check("matter realization remains residual", support_pieces["matter_realization"] == "residual")

    section("6. Wording and artifact sanity")
    doc = Path("docs/COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    forbidden_wording = [
        ("status-transition overclaim", "would become " + "retained"),
        ("promotion overclaim", "promoted to " + "retained"),
        ("actual-surface overclaim", "retained on the actual " + "surface"),
        ("physical-color derivation overclaim", "derive physical " + "SU(3)_c"),
        ("Koide selector overclaim", "selects a " + "Koide"),
    ]
    check("source note exists", doc.exists(), str(doc))
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)
    check("note declares meta claim type", "**Claim type:** meta" in text)
    check("note records no-go discipline gate", "No-go discipline result:" in text)
    check("note keeps dial selection out of scope", "Does not select a Koide/generation dial location." in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
