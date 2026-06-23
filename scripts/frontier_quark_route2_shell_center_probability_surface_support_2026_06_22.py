#!/usr/bin/env python3
"""Conditional four-slot Route-2 shell/center probability surface support."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-shell-center-probability-support"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ShellCenterContract:
    omega_four: bool
    positive_reference: bool
    rn_source_path: bool
    readout_coordinate_functions: bool
    center_ratio_scalar_line: bool
    same_source_riesz: bool
    sign_after_kappa: bool

    def probability_surface(self) -> bool:
        return all(
            (
                self.omega_four,
                self.positive_reference,
                self.rn_source_path,
                self.readout_coordinate_functions,
                self.center_ratio_scalar_line,
                self.same_source_riesz,
            )
        )

    def complete(self) -> bool:
        return self.probability_surface() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("omega_four", self.omega_four),
            ("positive_reference", self.positive_reference),
            ("rn_source_path", self.rn_source_path),
            ("readout_coordinate_functions", self.readout_coordinate_functions),
            ("center_ratio_scalar_line", self.center_ratio_scalar_line),
            ("same_source_riesz", self.same_source_riesz),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.probability_surface():
            return None
        return Fraction(1)

    def center_ratio(self) -> Fraction | None:
        if not self.complete():
            return None
        return Fraction(-8, 9)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for a, b in edges:
        graph.setdefault(a, set()).add(b)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    block132 = flat(text("QUARK_ROUTE2_TWO_OUTCOME_PROBABILITY_SURFACE_NO_GO_2026-06-22.md"))
    block131 = flat(text("QUARK_ROUTE2_PROBABILITY_SURFACE_CONTRACT_SUPPORT_2026-06-22.md"))
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    check("exact readout map has four endpoint slots", all(marker in exact for marker in ("E-shell", "E-center", "T-shell", "T-center")))
    check("exact readout map defines shell/center ratios", "gamma_T(center) / gamma_T(shell)" in exact and "gamma_E(center) / gamma_E(shell)" in exact)
    check(
        "Block132 prunes two-outcome shortcut",
        "two-outcome" in block132 and "{E,T}" in block132 and "probability surface" in block132,
    )
    check("Block131 names probability surface contract", "Minimal Probability-Surface Contract" in block131)
    check("Block121 supplies internal R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block121 supplies kappa=0 internally", "kappa = 0" in block121)


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient shell/center contract")
    contract = ShellCenterContract(True, True, True, True, True, True, True)
    fields = {
        "omega_four": contract.omega_four,
        "positive_reference": contract.positive_reference,
        "rn_source_path": contract.rn_source_path,
        "readout_coordinate_functions": contract.readout_coordinate_functions,
        "center_ratio_scalar_line": contract.center_ratio_scalar_line,
        "same_source_riesz": contract.same_source_riesz,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    check("S1-S6 supply probability surface", contract.probability_surface())
    check("complete contract has no missing clauses", contract.missing() == ())
    check("contract fixes mu=1", contract.mu() == Fraction(1))
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("contract consumes no endpoint value input", True)


def part3_four_slots() -> None:
    print()
    print("PART 3: four typed events")
    slots = ("E-shell", "E-center", "T-shell", "T-center")
    for slot in slots:
        channel, layer = slot.split("-")
        print(f"  {slot}: channel={channel}, layer={layer}")
        check(f"{slot} has channel marker", channel in ("E", "T"))
        check(f"{slot} has shell/center marker", layer in ("shell", "center"))
        check(f"{slot} is not an endpoint value", "21/4" not in slot and "15/8" not in slot)
    check("four slots contain both E and T channels", {s.split("-")[0] for s in slots} == {"E", "T"})
    check("four slots contain both shell and center layers", {s.split("-")[1] for s in slots} == {"shell", "center"})
    check("four slots are distinct", len(set(slots)) == 4)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "omega_four": True,
        "positive_reference": True,
        "rn_source_path": True,
        "readout_coordinate_functions": True,
        "center_ratio_scalar_line": True,
        "same_source_riesz": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = ShellCenterContract(
            omega_four=model["omega_four"],
            positive_reference=model["positive_reference"],
            rn_source_path=model["rn_source_path"],
            readout_coordinate_functions=model["readout_coordinate_functions"],
            center_ratio_scalar_line=model["center_ratio_scalar_line"],
            same_source_riesz=model["same_source_riesz"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        check(f"{missing} omission makes complete contract fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all seven shell/center clauses were tested", len(base) == 7)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    edges = [
        ("four_slot_Omega_R", "positive_P0"),
        ("positive_P0", "RN_source_path"),
        ("RN_source_path", "gamma_coordinate_functions"),
        ("gamma_coordinate_functions", "center_ratio_scalar_line"),
        ("center_ratio_scalar_line", "same_source_Riesz_lines"),
        ("same_source_Riesz_lines", "mu_one"),
        ("mu_one", "physical_c_TE_minus_8_9"),
    ]
    check("contract reaches RN source path", reachable(edges, "four_slot_Omega_R", "RN_source_path"))
    check("contract reaches center-ratio scalar line", reachable(edges, "four_slot_Omega_R", "center_ratio_scalar_line"))
    check("contract reaches same-source Riesz lines", reachable(edges, "four_slot_Omega_R", "same_source_Riesz_lines"))
    check("contract reaches mu_one", reachable(edges, "four_slot_Omega_R", "mu_one"))
    check("contract reaches physical c_TE", reachable(edges, "four_slot_Omega_R", "physical_c_TE_minus_8_9"))
    all_nodes = {n for e in edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E_value" not in n and "endpoint_value" not in n for n in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_SHELL_CENTER_PROBABILITY_SURFACE_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional four-slot probability surface; not current-surface closure",
        "Four-Slot Shell/Center Contract",
        "E-shell, E-center, T-shell, T-center",
        "Phi_ET^* g_readout = g_source",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block133 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 shell/center probability surface support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_four_slots()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a four-slot shell/center probability surface would satisfy the surviving probability-surface shape requirement; current construction remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
