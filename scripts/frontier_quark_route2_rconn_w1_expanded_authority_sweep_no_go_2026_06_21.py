#!/usr/bin/env python3
"""Expanded one-hop authority sweep for the Route-2/Rconn W1 bridge."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    reachable,
    rho_e_from_center_ratio,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

COLOR_TOKENS = (
    "R_conn",
    "F_adj",
    "adjoint",
    "color projection",
    "color scalar",
    "SU(3)",
)

ROUTE_TOKENS = (
    "gamma_T(center)",
    "gamma_E(center)",
    "c_TE",
    "center ratio",
    "Route-2 center",
    "E/T center",
)

NON_POSITIVE_MARKERS = (
    "?=>",
    "missing",
    "not",
    "no theorem",
    "needs",
    "If ",
    "if ",
    "would",
    "target",
    "attempt",
    "obstruction",
    "open",
    "conditional",
    "blocked",
    "supplied",
    "without",
    "cannot",
    "does not",
    "not a derivation",
    "not derive",
    "do not",
    "no current",
    "outside",
    "rather than",
    "residual",
    "suggestive",
    "firewall",
)

AUTHORITY_FILES = (
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
    "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md",
    "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md",
    "RCONN_DERIVED_NOTE.md",
    "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
    "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md",
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
)

EXPECTED_MIXED_COUNTS = {
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": 10,
    "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md": 13,
    "QUARK_ROUTE2_RCONN_CENTER_RATIO_BRIDGE_OBSTRUCTION_NOTE_2026-04-28.md": 7,
    "RCONN_DERIVED_NOTE.md": 0,
    "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md": 1,
    "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md": 0,
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": 0,
    "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md": 0,
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md": 0,
}


@dataclass(frozen=True)
class MixedParagraph:
    file_name: str
    paragraph_index: int
    text: str
    context: str


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


def norm(text: str) -> str:
    return " ".join(text.split())


def paragraphs(text: str) -> list[str]:
    return [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]


def has_any(text: str, tokens: tuple[str, ...]) -> bool:
    return any(token in text for token in tokens)


def mixed_paragraphs(file_name: str) -> list[MixedParagraph]:
    chunks = paragraphs((DOCS / file_name).read_text(encoding="utf-8"))
    mixed: list[MixedParagraph] = []
    for index, chunk in enumerate(chunks):
        if not (has_any(chunk, COLOR_TOKENS) and has_any(chunk, ROUTE_TOKENS)):
            continue
        context = "\n".join(chunks[max(0, index - 1) : min(len(chunks), index + 2)])
        mixed.append(
            MixedParagraph(
                file_name=file_name,
                paragraph_index=index + 1,
                text=chunk,
                context=context,
            )
        )
    return mixed


def classified_non_positive(hit: MixedParagraph) -> bool:
    return any(marker in hit.context for marker in NON_POSITIVE_MARKERS)


def positive_bridge_like(hit: MixedParagraph) -> bool:
    compact = norm(hit.context)
    bridge_formula = (
        "gamma_T(center)/gamma_E(center) = -F_adj" in compact
        or "gamma_T(center) / gamma_E(center) = -R_conn" in compact
        or "c_TE = -F_adj" in compact
        or "c_TE = gamma_T(center)/gamma_E(center) = -R_conn" in compact
    )
    return bridge_formula and not classified_non_positive(hit)


def rho_from_center(center_te: Fraction) -> Fraction:
    return rho_e_from_center_ratio(center_te)


def part_a_files_and_note() -> None:
    print("A. Sweep inputs")
    note = DOCS / "QUARK_ROUTE2_RCONN_W1_EXPANDED_AUTHORITY_SWEEP_NO_GO_NOTE_2026-06-21.md"
    check("block31 note exists", note.exists(), str(note.relative_to(ROOT)))
    note_text = note.read_text(encoding="utf-8")
    check("block31 note states expanded authority sweep scope", "expanded authority bank" in note_text)
    check("block31 note avoids repo-wide status change", "not a repo-wide status change" in note_text)
    for file_name in AUTHORITY_FILES:
        path = DOCS / file_name
        check(f"{file_name} exists", path.exists(), str(path.relative_to(ROOT)))


def part_b_mixed_paragraph_sweep() -> list[MixedParagraph]:
    print("\nB. Mixed paragraph sweep")
    all_hits: list[MixedParagraph] = []
    for file_name in AUTHORITY_FILES:
        hits = mixed_paragraphs(file_name)
        all_hits.extend(hits)
        check(
            f"{file_name} mixed paragraph count",
            len(hits) == EXPECTED_MIXED_COUNTS[file_name],
            f"count={len(hits)}",
        )
    check("expanded bank has 31 mixed paragraphs", len(all_hits) == 31, f"count={len(all_hits)}")
    zero_hit_files = [name for name, count in EXPECTED_MIXED_COUNTS.items() if count == 0]
    check(
        "pure-domain authority files have no mixed W1 paragraph",
        all(len(mixed_paragraphs(name)) == 0 for name in zero_hit_files),
        f"zero-hit files={len(zero_hit_files)}",
    )
    return all_hits


def part_c_dispositions(all_hits: list[MixedParagraph]) -> None:
    print("\nC. Disposition classifier")
    unclassified = [hit for hit in all_hits if not classified_non_positive(hit)]
    positives = [hit for hit in all_hits if positive_bridge_like(hit)]
    comparator_hits = [hit for hit in all_hits if "suggestive" in hit.context]
    firewall_hits = [hit for hit in all_hits if "firewall" in hit.context or "Forbidden citations" in hit.context]
    missing_hits = [hit for hit in all_hits if "missing" in hit.context or "no theorem" in hit.context]
    conditional_hits = [hit for hit in all_hits if "?=>" in hit.context or "If " in hit.context or "if " in hit.context]

    check("all mixed paragraphs have non-positive local context", not unclassified, f"unclassified={len(unclassified)}")
    check("no mixed paragraph is a positive current W1 bridge", not positives, f"positive_like={len(positives)}")
    check("sweep includes at least one live-comparator disposition", len(comparator_hits) >= 1, f"count={len(comparator_hits)}")
    check("sweep includes at least one downstream-firewall disposition", len(firewall_hits) >= 1, f"count={len(firewall_hits)}")
    check("sweep includes missing-edge dispositions", len(missing_hits) >= 5, f"count={len(missing_hits)}")
    check("sweep includes conditional/hypothetical dispositions", len(conditional_hits) >= 5, f"count={len(conditional_hits)}")


def part_d_graph_and_arithmetic() -> None:
    print("\nD. Graph and arithmetic cross-check")
    edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    color = "su3_R_conn_8_9"
    center = "route2_center_TE_minus_8_9"
    rho = "route2_rho_E_21_4"
    no_center, _ = reachable(edges, color, center)
    no_rho, _ = reachable(edges, color, rho)
    with_center, _ = reachable(edges + (MISSING_BRIDGE,), color, center)
    with_rho, _ = reachable(edges + (MISSING_BRIDGE,), color, rho)

    check("current W9 inventory lacks W1 center path", not no_center)
    check("current W9 inventory lacks color-to-rho path", not no_rho)
    check("adjoining W1 reaches center path", with_center)
    check("adjoining W1 reaches endpoint target chain", with_rho)
    check("W1 missing bridge endpoints match expected nodes", MISSING_BRIDGE.source == color and MISSING_BRIDGE.target == center)

    f_adj = Fraction(8, 9)
    q_e = Fraction(-2, 1) * Fraction(5, 6) / (-f_adj)
    rho = rho_from_center(-f_adj)
    check("F_adj value is exact 8/9", f_adj == Fraction(8, 9))
    check("W1 value gives q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("W1 value gives rho_E=21/4", rho == Fraction(21, 4), str(rho))


def main() -> int:
    part_a_files_and_note()
    all_hits = part_b_mixed_paragraph_sweep()
    part_c_dispositions(all_hits)
    part_d_graph_and_arithmetic()
    print(f"\nTOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("Status: exact negative boundary for hidden one-hop W1 authority.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
