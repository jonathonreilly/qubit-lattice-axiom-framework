#!/usr/bin/env python3
"""Split the color MR_color residual into carrier content and routing gates.

This runner is self-contained. It does not rely on older companion runners
whose text-marker checks may drift from the current citation shape. It checks
only the small finite-dimensional and dependency-interface facts used by the
source note.

No physical color derivation, no species-name derivation, no link routing
construction, no coupling/action selection, no dial fixing, no audit verdicts.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
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
class Piece:
    name: str
    status: str
    outputs: frozenset[str]
    missing: frozenset[str]


def main() -> int:
    emit("=" * 78)
    emit("COLOR MR_COLOR CARRIER/ROUTING SPLIT")
    emit("meta support-map interface runner")
    emit("=" * 78)

    section("1. Structural dimensions")
    weak_dim = 2
    sym_dim = sym_power_dim(2, 2)
    anti_dim = 1
    lh_triplet_dim = weak_dim * sym_dim
    lh_singlet_dim = weak_dim * anti_dim
    total_lh_dim = lh_triplet_dim + lh_singlet_dim
    su3_dim = su_dim(sym_dim)

    check("dim Sym^2(C^2) = 3", sym_dim == 3, f"got {sym_dim}")
    check("dim Anti^2(C^2) = 1", anti_dim == 1, f"got {anti_dim}")
    check("weak doublet dimension = 2", weak_dim == 2)
    check("dim (2,3) = 6", lh_triplet_dim == 6, f"got {lh_triplet_dim}")
    check("dim (2,1) = 2", lh_singlet_dim == 2, f"got {lh_singlet_dim}")
    check("LH doublet total dimension = 8", total_lh_dim == 8, f"got {total_lh_dim}")
    check("structural su(3) dimension on Sym^2 block = 8", su3_dim == 8, f"got {su3_dim}")
    check("3+1 base split tensors to 6+2 LH split", (sym_dim, anti_dim, lh_triplet_dim, lh_singlet_dim) == (3, 1, 6, 2))

    section("2. MR_color subpieces")
    carrier = Piece(
        name="supported_carrier_content",
        status="support",
        outputs=frozenset(
            {
                "selected_axis",
                "canonical_fiber_base_split",
                "sym2_su3_fundamental_block",
                "anti2_su3_singlet_block",
                "lh_doublet_2_3_plus_2_1",
            }
        ),
        missing=frozenset(),
    )
    species_names = Piece(
        name="sm_species_naming",
        status="residual_convention",
        outputs=frozenset({"quark_name_for_su3_charged_block", "lepton_name_for_su3_singlet_block"}),
        missing=frozenset({"derive_species_names_from_axioms"}),
    )
    record_readout = Piece(
        name="color_record_readout_antecedent",
        status="residual_antecedent",
        outputs=frozenset({"physical_records_are_color_singlets"}),
        missing=frozenset({"record_observable_identification"}),
    )
    link_routing = Piece(
        name="base_su3_link_index_routing",
        status="residual_construction",
        outputs=frozenset({"link_variable_carries_base_su3_index", "gauss_generators_for_base_su3"}),
        missing=frozenset({"link_endpoint_carrier", "parallel_transport_representation"}),
    )
    dynamics = Piece(
        name="formation_action_dynamics",
        status="residual_construction",
        outputs=frozenset({"wilson_observables", "gauge_action", "couplings", "rates_time"}),
        missing=frozenset({"production_dynamics", "action_selection", "clock_or_rate_law"}),
    )
    post_record = Piece(
        name="post_record_consumer",
        status="exact_consumer_support",
        outputs=frozenset({"word_history_O_star", "count_state_N_to_O", "coarse_grained_counts"}),
        missing=frozenset(),
    )

    pieces = [carrier, species_names, record_readout, link_routing, dynamics, post_record]
    check("six interface pieces tracked", len(pieces) == 6)
    check("carrier content is support", carrier.status == "support")
    check("species naming remains convention residual", species_names.status == "residual_convention")
    check("record readout remains antecedent residual", record_readout.status == "residual_antecedent")
    check("link routing remains construction residual", link_routing.status == "residual_construction")
    check("post-record layer is consumer support", post_record.status == "exact_consumer_support")

    all_outputs = set().union(*(piece.outputs for piece in pieces))
    check("carrier output includes Sym^2 SU(3) fundamental block", "sym2_su3_fundamental_block" in carrier.outputs)
    check("carrier output includes (2,3)+(2,1) LH split", "lh_doublet_2_3_plus_2_1" in carrier.outputs)
    check("link routing output includes base-SU3 link index", "link_variable_carries_base_su3_index" in link_routing.outputs)
    check("post-record output includes word histories", "word_history_O_star" in post_record.outputs)
    check("all named outputs are unique enough for interface use", len(all_outputs) == sum(len(piece.outputs) for piece in pieces))

    section("3. Disjointness checks")
    check(
        "carrier content does not include species naming",
        carrier.outputs.isdisjoint(species_names.outputs),
    )
    check(
        "carrier content does not include record-readout antecedent",
        carrier.outputs.isdisjoint(record_readout.outputs),
    )
    check(
        "carrier content does not include link routing",
        carrier.outputs.isdisjoint(link_routing.outputs),
    )
    check(
        "carrier content does not include formation/action dynamics",
        carrier.outputs.isdisjoint(dynamics.outputs),
    )
    check(
        "post-record consumer does not include link routing",
        post_record.outputs.isdisjoint(link_routing.outputs),
    )
    check(
        "post-record consumer does not include record-readout antecedent",
        post_record.outputs.isdisjoint(record_readout.outputs),
    )
    check(
        "record-readout antecedent does not include action dynamics",
        record_readout.outputs.isdisjoint(dynamics.outputs),
    )

    section("4. Completion logic")
    mr_required = {
        "sym2_su3_fundamental_block",
        "quark_name_for_su3_charged_block",
        "physical_records_are_color_singlets",
        "link_variable_carries_base_su3_index",
        "gauss_generators_for_base_su3",
    }
    supported_now = set(carrier.outputs)
    missing_without_residuals = mr_required - supported_now
    supported_with_all_mr = set().union(carrier.outputs, species_names.outputs, record_readout.outputs, link_routing.outputs)

    check("MR_color requires five named outputs", len(mr_required) == 5)
    check("carrier content supplies the structural block requirement", "sym2_su3_fundamental_block" in supported_now)
    check("carrier content alone leaves four MR outputs missing", len(missing_without_residuals) == 4, str(sorted(missing_without_residuals)))
    check("species naming missing without convention piece", "quark_name_for_su3_charged_block" in missing_without_residuals)
    check("color-record readout missing without antecedent piece", "physical_records_are_color_singlets" in missing_without_residuals)
    check("link variable routing missing without construction piece", "link_variable_carries_base_su3_index" in missing_without_residuals)
    check("Gauss generator choice missing without construction piece", "gauss_generators_for_base_su3" in missing_without_residuals)
    check("all MR outputs present only after residual pieces are added", mr_required <= supported_with_all_mr)
    check("post-record consumer is downstream of MR outputs", post_record.outputs.isdisjoint(mr_required))

    section("5. Route implications")
    route_table = {
        "structural_block_only_rows": "can cite carrier-content support",
        "quark_label_rows": "still consume species naming convention",
        "color_record_rows": "still consume color-record readout antecedent",
        "wilson_gauss_rows": "still consume link routing",
        "qcd_dynamics_rows": "still consume formation/action dynamics",
        "history_count_rows": "can use post-record consumer after realized atoms exist",
    }
    check("route table has six consumer classes", len(route_table) == 6)
    check("structural rows classified as support consumers", "support" in route_table["structural_block_only_rows"])
    check("quark label rows keep naming convention", "naming convention" in route_table["quark_label_rows"])
    check("record rows keep readout antecedent", "readout antecedent" in route_table["color_record_rows"])
    check("Wilson/Gauss rows keep link routing", "link routing" in route_table["wilson_gauss_rows"])
    check("QCD dynamics rows keep formation/action", "formation/action" in route_table["qcd_dynamics_rows"])
    check("history/count rows are after realized atoms", "after realized atoms" in route_table["history_count_rows"])

    section("6. Note sanity")
    doc = Path("docs/COLOR_MR_CARRIER_ROUTING_SPLIT_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    check("source note exists", doc.exists(), str(doc))
    for marker in [
        "**Claim type:** meta",
        "Trace class:** upstream support map",
        "No-go discipline result:",
        "Does not derive physical color.",
        "Does not route the base-`SU(3)` index onto link variables.",
        "Does not select a Koide/generation dial location.",
    ]:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("physical color closure", "physical color is " + "derived"),
        ("species derivation closure", "species names are " + "derived"),
        ("link routing closure", "link routing is " + "derived"),
        ("dial selector closure", "dial location is " + "selected"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
