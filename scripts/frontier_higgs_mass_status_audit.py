#!/usr/bin/env python3
"""Content checks for the Higgs mass status-correction repair packet."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

TARGET_NOTE = ROOT / "docs" / "HIGGS_MASS_FROM_AXIOM_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md"
PARENT_NOTE = ROOT / "docs" / "HIGGS_MASS_FROM_AXIOM_NOTE.md"
CYCLE5_NOTE = ROOT / "docs" / "YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md"
CYCLE9_NOTE = ROOT / "docs" / "GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md"
CLUSTER_CONTEXT = ROOT / "docs" / "LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CACHE_DIR = ROOT / "logs" / "runner-cache"

ROWS = {
    "cycle5": "yt_ew_matching_rule_m_note_2026-05-02",
    "cycle9": "gauge_scalar_temporal_observable_bridge_no_go_theorem_note_2026-05-03",
    "target": "higgs_mass_from_axiom_status_correction_audit_note_2026-05-02",
    "parent": "higgs_mass_from_axiom_note",
}

RETAINED_AUTHORITY_STATUSES = {"retained", "retained_bounded", "retained_no_go"}


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{status}: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_rows() -> dict:
    return json.loads(read(LEDGER))["rows"]


def markdown_link_targets(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def squash(text: str) -> str:
    return " ".join(text.split())


def cache_total(cache_name: str) -> tuple[int, int, str]:
    text = read(CACHE_DIR / cache_name)
    fail_matches = [int(x) for x in re.findall(r"FAIL=(\d+)", text)]
    pass_matches = [int(x) for x in re.findall(r"PASS=(\d+)", text)]
    if not fail_matches or not pass_matches:
        return 0, 1, "missing PASS/FAIL summary"
    return sum(pass_matches), max(fail_matches), text


def lines_with_positive_pole_prediction(surface: str) -> list[str]:
    suspect: list[str] = []
    for line in surface.splitlines():
        lower = line.lower()
        mentions_prediction = "higgs-mass prediction" in lower or "higgs-pole prediction" in lower
        mentions_pole_derivation = "derive the higgs-mass pole" in lower
        if not (mentions_prediction or mentions_pole_derivation):
            continue
        if "not" in lower or "does not" in lower or "no " in lower:
            continue
        suspect.append(line.strip())
    return suspect


def section_contains(text: str, heading: str, needle: str) -> bool:
    start = text.find(heading)
    if start < 0:
        return False
    next_heading = text.find("\n## ", start + len(heading))
    section = text[start:] if next_heading < 0 else text[start:next_heading]
    return needle in section


def main() -> int:
    getcontext().prec = 32
    gate = Gate()

    target = read(TARGET_NOTE)
    parent = read(PARENT_NOTE)
    cycle5 = read(CYCLE5_NOTE)
    cycle9 = read(CYCLE9_NOTE)
    rows = ledger_rows()

    print("Higgs status-correction content audit")

    for label, path in [
        ("target note", TARGET_NOTE),
        ("parent note", PARENT_NOTE),
        ("cycle 5 authority note", CYCLE5_NOTE),
        ("cycle 9 authority note", CYCLE9_NOTE),
        ("cluster context pointer", CLUSTER_CONTEXT),
        ("audit ledger", LEDGER),
    ]:
        gate.check(f"{label} exists", path.exists(), str(path.relative_to(ROOT)))

    target_row = rows.get(ROWS["target"], {})
    cycle5_row = rows.get(ROWS["cycle5"], {})
    cycle9_row = rows.get(ROWS["cycle9"], {})

    gate.check(
        "target ledger row points to the registered runner",
        target_row.get("runner_path") == "scripts/frontier_higgs_mass_status_audit.py",
        str(target_row.get("runner_path")),
    )
    gate.check(
        "target ledger row points to the repaired note",
        target_row.get("note_path") == "docs/HIGGS_MASS_FROM_AXIOM_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md",
        str(target_row.get("note_path")),
    )
    gate.check(
        "cycle 5 authority row is markdown-linkable by ledger metadata",
        cycle5_row.get("effective_status") in RETAINED_AUTHORITY_STATUSES
        and cycle5_row.get("note_path") == "docs/YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md",
        f"{cycle5_row.get('effective_status')} {cycle5_row.get('claim_type')}",
    )
    gate.check(
        "cycle 9 authority row is markdown-linkable by ledger metadata",
        cycle9_row.get("effective_status") in RETAINED_AUTHORITY_STATUSES
        and cycle9_row.get("note_path")
        == "docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md",
        f"{cycle9_row.get('effective_status')} {cycle9_row.get('claim_type')}",
    )
    gate.check(
        "unaudited cluster synthesis is not used as authority",
        "docs/LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md is\n  context only"
        in target
        and "[`LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md`]" not in target,
    )

    gate.check(
        "status authority block is present",
        "**Status authority:** independent audit lane only. This source note does\nnot set or predict an audit outcome."
        in target,
    )
    gate.check(
        "target declares open-gate demotion/status-correction source type",
        "**Claim type:** open_gate." in target
        and "**Type:** demotion / status-correction packet." in target,
    )
    gate.check(
        "target has source-correction audit firewall",
        "## 2026-06-12 audit firewall: source correction only" in target
        and "does not add a new axiom, Tier-A admission, external\ncomparator, or audit status" in target
        and "future bridge remains open" in target
        and "does not set downstream\neffective status" in target,
    )
    gate.check(
        "target has dated 2026-06-12 repair section",
        "## 7. 2026-06-12 authority repair" in target,
    )
    gate.check(
        "target has source-side no-go discipline scope gate",
        "## 8. No-go discipline scope gate (2026-06-12)" in target,
    )

    links = markdown_link_targets(target)
    gate.check(
        "target contains no external markdown links",
        all(not link.startswith("http://") and not link.startswith("https://") for link in links),
        ", ".join(link for link in links if link.startswith(("http://", "https://"))),
    )
    for expected in [
        "HIGGS_MASS_FROM_AXIOM_NOTE.md",
        "YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md",
        "GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md",
    ]:
        gate.check(f"target markdown-links one-hop authority {expected}", expected in links)

    gate.check(
        "cycle 5 authority consumed at same-shape claim site",
        section_contains(
            target,
            "## 2. Same-shape obstruction as cycles 5 and 9",
            "[`YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md`](YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md)",
        )
        and "does not supply a retained selector\n  promoting it to the physical EW current matching rule M"
        in target
        and "no\n  retained selector deriving exact physical EW matching rule M" in target,
    )
    gate.check(
        "cycle 9 authority consumed at same-shape claim site",
        section_contains(
            target,
            "## 2. Same-shape obstruction as cycles 5 and 9",
            "[`GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md`](GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md)",
        )
        and "two admissible completions agree on the retained packet and give different" in target,
    )
    gate.check(
        "target scopes same-shape classification to current-packet non-derivation",
        "They do not prove a global theorem that no future bridge can exist." in target
        and "not\nderived by the current packet unless an independent scalar-normalization" in target,
    )

    gate.check(
        "cycle 5 note states exact algebraic fraction",
        "F_adj = (N_c^2 - 1) / N_c^2 = 8/9" in cycle5,
    )
    gate.check(
        "cycle 5 note states no retained selector promotes to physical M",
        "does not contain a retained selector that promotes this algebraic\n   fraction to the physical EW current matching rule M"
        in cycle5,
    )
    gate.check(
        "cycle 5 note forbids broad global finite-Nc no-go",
        "no longer claims a global theorem" in cycle5
        and "not an exhaustive proof" in cycle5,
    )
    n_c = Fraction(3, 1)
    f_adj = (n_c * n_c - 1) / (n_c * n_c)
    gate.check("cycle 5 algebra recomputes F_adj exactly", f_adj == Fraction(8, 9), f"F_adj={f_adj}")

    beta = Fraction(6, 1)
    c = Fraction(1, 10_000_000)
    delta = c * beta**6
    gate.check(
        "cycle 9 note declares two completion witnesses",
        "beta_eff^-(beta) = beta + a beta^5" in cycle9
        and "beta_eff^+(beta) = beta + a beta^5 + c beta^6" in cycle9,
    )
    gate.check(
        "cycle 9 witness delta is recomputed exactly",
        delta == Fraction(729, 156250),
        f"delta={delta} decimal={float(delta):.7f}",
    )
    gate.check(
        "cycle 9 note records the same witness delta",
        "beta_eff^+(6) - beta_eff^-(6) = c 6^6 = 0.0046656 > 0" in cycle9,
    )
    gate.check(
        "cycle 9 note uses distinct readouts for non-entailment",
        "R_O(beta_eff^+(6)) != R_O(beta_eff^-(6))" in cycle9
        and "two different\nBRIDGE readouts" in cycle9,
    )
    gate.check(
        "cycle 9 note names nonperturbative escape objects",
        "exact beta-6 Wilson plaquette spectral measure" in cycle9
        and "exact independently selected `beta_eff(6)`" in cycle9,
    )

    yt_pass, yt_fail, _ = cache_total("frontier_yt_ew_matching_rule_m_current_packet_boundary.txt")
    gs_pass, gs_fail, gs_cache = cache_total("frontier_gauge_scalar_temporal_observable_bridge_no_go.txt")
    gate.check("cycle 5 cached runner total parses with FAIL=0", yt_fail == 0 and yt_pass >= 29, f"PASS={yt_pass} FAIL={yt_fail}")
    gate.check(
        "cycle 9 cached runner summary parses with FAIL=0",
        gs_fail == 0 and "SUMMARY: THEOREM PASS=9 SUPPORT=4 FAIL=0" in gs_cache,
        f"parsed PASS={gs_pass} FAIL={gs_fail}",
    )

    u0 = Decimal("0.877681381")
    v = Decimal("246.22")
    m_curv = v / (Decimal(2) * u0)
    rounded = m_curv.quantize(Decimal("0.1"))
    gate.check("parent diagnostic value recomputes to 140.3 GeV", rounded == Decimal("140.3"), f"m_curv={m_curv}")
    gate.check(
        "parent labels v/(2u0) as diagnostic m_curv_tree",
        "`m_curv_tree^2 := (|V_taste''(0)|/N_taste) v^2\n= v^2/(4 u_0^2)`. This is a defined diagnostic scale, NOT an observable\nidentification."
        in parent,
    )
    gate.check(
        "parent explicitly rejects Higgs-pole prediction reading",
        "NOT a Higgs-mass prediction" in parent
        and "This note does NOT derive the Higgs-mass pole." in parent,
    )
    gate.check(
        "target records bounded diagnostic reading",
        "The parent expression `v/(2u_0)` is read as a bounded diagnostic definition"
        in squash(target)
        and "not as a Higgs-pole prediction" in squash(target),
    )
    surface = "\n".join([target, parent, cycle5, cycle9])
    positives = lines_with_positive_pole_prediction(surface)
    gate.check(
        "dependency surface has no positive Higgs-pole prediction wiring",
        not positives,
        "; ".join(positives[:3]),
    )

    forbidden_overreach = [
        "only route",
        "last route",
        "exhausted",
        "closes the program",
        "cannot be derived from standard QFT alone",
        "standard QFT analytical machinery",
        "After this PR lands",
        "transitive descendants inherit",
    ]
    for phrase in forbidden_overreach:
        gate.check(f"target avoids overreach phrase {phrase!r}", phrase not in target)

    for label in [f"N{i}" for i in range(1, 9)]:
        gate.check(f"no-go discipline gate includes {label}", f"**{label}" in target)

    ok = gate.fail_count == 0
    print(f"TOTAL: PASS={gate.pass_count}, FAIL={gate.fail_count}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
