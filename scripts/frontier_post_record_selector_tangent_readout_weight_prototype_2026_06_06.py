#!/usr/bin/env python3
"""Exact finite-packet arithmetic under an explicit supplied-data contract."""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SuppliedFinitePacket:
    """All non-derived inputs to the narrowly scoped arithmetic theorem."""

    carrier: tuple[str, ...]
    carrier_weights: tuple[Fraction, ...]
    endpoint_map: tuple[str, ...]
    readout_map: tuple[str, ...]
    tangent_metric_or_hessian: tuple[
        tuple[Fraction, Fraction], tuple[Fraction, Fraction]
    ]
    tangent_vector: tuple[Fraction, Fraction]


def supplied_packet() -> SuppliedFinitePacket:
    carrier = tuple(f"c{i}" for i in range(16))
    return SuppliedFinitePacket(
        carrier=carrier,
        carrier_weights=(Fraction(1),) * len(carrier),
        endpoint_map=tuple(
            "endpoint_lo" if i < 4 else "endpoint_hi" for i in range(16)
        ),
        readout_map=tuple("ground" if i == 0 else "excited" for i in range(16)),
        tangent_metric_or_hessian=(
            (Fraction(3), Fraction(1)),
            (Fraction(1), Fraction(2)),
        ),
        tangent_vector=(Fraction(1), Fraction(1, 2)),
    )


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def diagnostic(label: str, detail: str = "") -> None:
    """Print mutable inventory information without making it a theorem gate."""

    suffix = f" :: {detail}" if detail else ""
    print(f"INFO {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    flat = " ".join(text.split())
    report(f"{path} exists", (ROOT / path).exists())
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text or needle in flat)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(weights: dict[str, Fraction]) -> dict[str, Fraction]:
    if any(value < 0 for value in weights.values()):
        raise ValueError("negative supplied weight")
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        raise ValueError("nonpositive supplied total")
    return {key: value / total for key, value in weights.items()}


def pushforward_weights(
    packet: SuppliedFinitePacket, labels: tuple[str, ...]
) -> dict[str, Fraction]:
    if len(labels) != len(packet.carrier):
        raise ValueError("supplied map is not total on the carrier")
    pushed: dict[str, Fraction] = {}
    for label, weight in zip(labels, packet.carrier_weights, strict=True):
        pushed[label] = pushed.get(label, Fraction(0)) + weight
    return normalize(pushed)


def quadratic(
    metric: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
    vector: tuple[Fraction, Fraction],
) -> Fraction:
    x, y = vector
    return (
        metric[0][0] * x * x
        + (metric[0][1] + metric[1][0]) * x * y
        + metric[1][1] * y * y
    )


def is_spd_2x2(metric: tuple[tuple[Fraction, ...], ...]) -> bool:
    if len(metric) != 2 or any(len(row) != 2 for row in metric):
        return False
    return (
        metric[0][1] == metric[1][0]
        and metric[0][0] > 0
        and metric[0][0] * metric[1][1] - metric[0][1] * metric[1][0] > 0
    )


def packet_contract_is_accepted(packet: SuppliedFinitePacket) -> bool:
    """Check every premise of the local supplied-packet bridge theorem."""

    return (
        bool(packet.carrier)
        and len(set(packet.carrier)) == len(packet.carrier)
        and len(packet.carrier_weights) == len(packet.carrier)
        and len(packet.endpoint_map) == len(packet.carrier)
        and len(packet.readout_map) == len(packet.carrier)
        and len(packet.tangent_vector) == 2
        and any(packet.tangent_vector)
        and all(weight >= 0 for weight in packet.carrier_weights)
        and sum(packet.carrier_weights, Fraction(0)) > 0
        and is_spd_2x2(packet.tangent_metric_or_hessian)
    )


def selector_authority(has_weight_certificate: bool, has_selector_rule: bool) -> str:
    if has_weight_certificate and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md",
        [
            "selector_tangent_readout_weight",
            "Type:** bounded_theorem",
            "Claim type:** bounded_theorem",
            "Explicit supplied-packet bridge theorem",
            "The supplied packet",
            "C = \\{c_0, \\ldots, c_{15}\\}",
            "u(c_i)=1",
            "e(c_i)=\\texttt{endpoint_lo}",
            "r(c_0)=\\texttt{ground}",
            "G=\\begin{pmatrix}3&1\\\\1&2\\end{pmatrix}",
            "v=\\begin{pmatrix}1\\\\1/2\\end{pmatrix}",
            "2026-06-18 Record-axiom non-supply repair",
            "finite readout/tangent weight arithmetic inside the explicitly accepted packet",
            "not selector/tangent/readout authority",
            "explicitly accepted as local mathematical hypotheses",
            "Does not derive a selector, tangent metric, Hessian",
            "Does not derive a readout context, central-sector decomposition",
            "scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py",
        ],
    )
    require_text(
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        [
            "### Record / Fixed Reality",
            "Records form.",
            "Only records are readable.",
            "Further physical structure requires a retained derivation or bridge",
            "context selection, measurement basis selection, Born weights, probability",
            "source/action and physical-observable identification",
        ],
    )
    require_text(
        "docs/audit/data/axiom_premise_nodes.json",
        [
            "\"minimal_axioms\"",
            "\"current_path\": \"docs/MINIMAL_AXIOMS_2026-06-29.md\"",
            "It still supplies no context-selection rule, formation rule",
            "weighting, normalization, probability, update law",
            "law-level dependence on an unfixed choice",
            "or downstream theory consequence.",
        ],
    )


def certificate_checks() -> None:
    section("Explicit supplied-packet bridge theorem checks")
    packet = supplied_packet()
    expected_carrier = tuple(f"c{i}" for i in range(16))
    expected_endpoint_map = tuple(
        "endpoint_lo" if i < 4 else "endpoint_hi" for i in range(16)
    )
    expected_readout_map = tuple(
        "ground" if i == 0 else "excited" for i in range(16)
    )

    report(
        "supplied finite packet contract is explicitly accepted",
        packet_contract_is_accepted(packet),
    )
    report(
        "supplied finite carrier matches the note exactly",
        packet.carrier == expected_carrier,
        str(packet.carrier),
    )
    report(
        "supplied raw weights match the note exactly",
        packet.carrier_weights == (Fraction(1),) * 16,
    )
    report(
        "supplied endpoint map matches the note exactly",
        packet.endpoint_map == expected_endpoint_map,
    )
    report(
        "supplied readout map matches the note exactly",
        packet.readout_map == expected_readout_map,
    )
    report(
        "supplied tangent metric/Hessian matches the note exactly",
        packet.tangent_metric_or_hessian
        == ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2))),
    )
    report(
        "supplied tangent vector matches the note exactly",
        packet.tangent_vector == (Fraction(1), Fraction(1, 2)),
    )

    weights = pushforward_weights(packet, packet.endpoint_map)
    report(
        "finite supplied readout weights normalize",
        weights
        == {"endpoint_lo": Fraction(1, 4), "endpoint_hi": Fraction(3, 4)},
        str(weights),
    )
    metric = packet.tangent_metric_or_hessian
    report("supplied tangent metric/Hessian is symmetric SPD", is_spd_2x2(metric), str(metric))
    report(
        "supplied tangent metric/Hessian determinant is exact",
        metric[0][0] * metric[1][1] - metric[0][1] * metric[1][0] == 5,
    )
    report(
        "quadratic tangent norm is exact",
        quadratic(metric, packet.tangent_vector) == Fraction(9, 2),
    )
    projection = pushforward_weights(packet, packet.readout_map)
    report(
        "projection/readout weights normalize",
        projection
        == {"ground": Fraction(1, 16), "excited": Fraction(15, 16)},
        str(projection),
    )

    has_weight_certificate = bool(weights)
    has_selector_rule = False
    report(
        "weight certificate without selector stays blocked",
        selector_authority(has_weight_certificate, has_selector_rule) == "blocked_missing_selector",
    )
    report(
        "selector rule is still needed",
        selector_authority(has_weight_certificate, not has_selector_rule) == "conditional_selector_ready",
    )

    edge_cases: list[tuple[str, bool]] = []
    for label, weights_to_test in [
        ("zero supplied total is rejected", {"zero": Fraction(0)}),
        ("negative supplied weight is rejected", {"bad": Fraction(-1), "good": Fraction(2)}),
    ]:
        try:
            normalize(weights_to_test)
            rejected = False
        except ValueError:
            rejected = True
        edge_cases.append((label, rejected))
    try:
        pushforward_weights(packet, packet.readout_map[:-1])
        short_map_rejected = False
    except ValueError:
        short_map_rejected = True
    edge_cases.extend(
        [
            ("non-total supplied map is rejected", short_map_rejected),
            (
                "asymmetric supplied matrix is rejected",
                not is_spd_2x2(
                    ((Fraction(3), Fraction(1)), (Fraction(0), Fraction(2)))
                ),
            ),
            (
                "semidefinite supplied matrix is rejected",
                not is_spd_2x2(
                    ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1)))
                ),
            ),
            (
                "indefinite supplied matrix is rejected",
                not is_spd_2x2(
                    ((Fraction(1), Fraction(2)), (Fraction(2), Fraction(1)))
                ),
            ),
            (
                "malformed supplied matrix is rejected",
                not is_spd_2x2(((Fraction(1),),)),
            ),
            (
                "malformed supplied tangent vector is rejected",
                not packet_contract_is_accepted(
                    replace(packet, tangent_vector=(Fraction(1),))
                ),
            ),
            (
                "zero supplied tangent vector is rejected",
                not packet_contract_is_accepted(
                    replace(packet, tangent_vector=(Fraction(0), Fraction(0)))
                ),
            ),
            (
                "incomplete supplied weight list is rejected",
                not packet_contract_is_accepted(
                    replace(packet, carrier_weights=(Fraction(1),) * 15)
                ),
            ),
        ]
    )
    for label, ok in edge_cases:
        report(label, ok)


def selector_rows() -> list[dict]:
    import frontier_post_record_measure_weight_normalization_subdivision_2026_06_06 as measure

    return [
        row
        for row in measure.measure_rows()
        if measure.measure_lane(row) == "selector_tangent_readout_weight"
    ]


def row_checks() -> list[dict]:
    section("Selector/tangent row checks")
    try:
        before = digest(LEDGER)
        rows = selector_rows()
        after = digest(LEDGER)
    except Exception as exc:
        diagnostic("mutable selector/tangent inventory unavailable (not a theorem premise)", repr(exc))
        return []
    diagnostic("selector/tangent live row count (not a theorem premise)", str(len(rows)))
    ids = {row.get("claim_id") for row in rows}
    for claim_id in [
        "strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12",
        "teleportation_preparation_readout_probe_note",
        "yt_exact_hessian_selector_uniqueness_note",
    ]:
        diagnostic(f"representative row currently present: {claim_id}", str(claim_id in ids))
    diagnostic(
        "audit ledger hash unchanged during diagnostic read (not a theorem premise)",
        f"{before == after} :: {before}",
    )
    print()
    print("Selector/tangent/readout rows:")
    for row in rows:
        print(
            "  "
            + f"{row.get('claim_id')} | "
            + f"effective {row.get('effective_status')} | {row.get('claim_type')} | "
            + f"{row.get('note_path')}"
        )
    return rows


def scope_declarations() -> None:
    section("Non-derived scope declarations (informational, not executable checks)")
    for label in [
        "no audit verdict is applied",
        "no selector authority is derived",
        "no Record-derived readout context, weighting, normalization, metric, Hessian, or Born law is claimed",
        "no physical measure, production dynamics, measurement dynamics, or physical arrow is derived",
    ]:
        diagnostic(label)


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    rows = row_checks()
    scope_declarations()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print(f"SELECTOR_TANGENT_READOUT_WEIGHT_ROWS={len(rows)}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("SELECTOR_AUTHORITY_DERIVED=FALSE")
    print("READOUT_CONTEXT_DERIVED_FROM_RECORD=FALSE")
    print("CENTRAL_SECTOR_DECOMPOSITION_DERIVED_FROM_RECORD=FALSE")
    print("KCPT_STRUCTURE_DERIVED_FROM_RECORD=FALSE")
    print("WEIGHTING_RULE_DERIVED_FROM_RECORD=FALSE")
    print("NORMALIZATION_AUTHORITY_DERIVED_FROM_RECORD=FALSE")
    print("PHYSICAL_MEASURE_SELECTED=FALSE")
    print("READOUT_PRIMITIVE_DERIVED_FROM_RECORD=FALSE")
    print("TANGENT_METRIC_DERIVED_FROM_RECORD=FALSE")
    print("HESSIAN_DERIVED_FROM_RECORD=FALSE")
    print("GENERATION_OR_KOIDE_DIAL_SELECTED=FALSE")
    print("BORN_LAW_DERIVED_FROM_RECORD=FALSE")
    print("MEASUREMENT_DYNAMICS_DERIVED_FROM_RECORD=FALSE")
    print("PRODUCTION_DYNAMICS_DERIVED=FALSE")
    print("PHYSICAL_ARROW_DERIVED_FROM_RECORD=FALSE")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
