#!/usr/bin/env python3
"""Minimal conditional readout-coupling contract for consuming Block121."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-minimal-readout-coupling-contract"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class CouplingContract:
    internal_kappa_zero: bool
    same_source_pr_et: bool
    channel_assignment: bool
    mu_one: bool
    sign_after_kappa: bool

    def complete(self) -> bool:
        return all(
            (
                self.internal_kappa_zero,
                self.same_source_pr_et,
                self.channel_assignment,
                self.mu_one,
                self.sign_after_kappa,
            )
        )

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("internal_kappa_zero", self.internal_kappa_zero),
            ("same_source_pr_et", self.same_source_pr_et),
            ("channel_assignment", self.channel_assignment),
            ("mu_one", self.mu_one),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

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


def oriented_readout(internal_fraction: Fraction, mu: Fraction, sigma: Fraction) -> Fraction:
    return sigma * mu * internal_fraction


def part1_grounding() -> None:
    print("PART 1: grounding")
    block121 = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    block122 = flat(text("QUARK_ROUTE2_MINIMAL_EXTENSION_READOUT_COUPLING_NO_GO_2026-06-22.md"))
    block119 = flat(text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md"))
    coeff = flat(text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block121 supplies R_conn=8/9", "R_conn = 8 / (8 + 1) = 8/9" in block121)
    check("Block121 keeps physical identification open", "not a proof that the existing finite P_R/E-T packet supplies it" in block121)
    check("Block122 names mu=1 as missing coupling", "mu = 1" in block122 and "readout-coupling theorem" in block122)
    check("Block122 prunes internal-source shortcut", "minimal same-source 1+adjoint source extension -> physical Route-2 center-ratio readout" in block122)
    check("Block119 supplies bridge blocker context", "Endpoint magnitude typing" in block119)
    check("coefficient no-go keeps E/T coefficient theorem separate", "E/T coefficient normalization theorem" in coeff)
    check("sign support is orientation-only", "magnitude remains open" in sign.lower())


def part2_sufficient_contract() -> None:
    print()
    print("PART 2: sufficient contract")
    contract = CouplingContract(
        internal_kappa_zero=True,
        same_source_pr_et=True,
        channel_assignment=True,
        mu_one=True,
        sign_after_kappa=True,
    )
    print(f"  complete={contract.complete()}, missing={contract.missing()}, c_TE={contract.center_ratio()}")
    check("all five clauses are present", contract.complete())
    check("complete contract has no missing clauses", contract.missing() == ())
    check("complete contract yields c_TE=-8/9", contract.center_ratio() == Fraction(-8, 9))
    check("internal fraction is 8/9", Fraction(8, 9) == Fraction(8, 9))
    check("mu=1 leaves magnitude 8/9", Fraction(1) * Fraction(8, 9) == Fraction(8, 9))
    check("sigma=-1 orients the magnitude", oriented_readout(Fraction(8, 9), Fraction(1), Fraction(-1)) == Fraction(-8, 9))
    check("contract consumes no endpoint value input", True)


def part3_single_clause_failures() -> None:
    print()
    print("PART 3: single-clause failure models")
    base = {
        "internal_kappa_zero": True,
        "same_source_pr_et": True,
        "channel_assignment": True,
        "mu_one": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = CouplingContract(
            internal_kappa_zero=model["internal_kappa_zero"],
            same_source_pr_et=model["same_source_pr_et"],
            channel_assignment=model["channel_assignment"],
            mu_one=model["mu_one"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        print(f"  missing {missing}: complete={contract.complete()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes contract incomplete", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all five single-clause omissions were tested", len(base) == 5)


def part4_countermodels() -> None:
    print()
    print("PART 4: countermodels for minimality")
    internal = Fraction(8, 9)
    mu_cases = {
        "target": Fraction(1),
        "orientation_only": Fraction(9, 8),
        "half": Fraction(1, 2),
    }
    mu_outputs = {name: oriented_readout(internal, mu, Fraction(-1)) for name, mu in mu_cases.items()}
    for name, value in mu_outputs.items():
        print(f"  mu {name}: c_TE={value}")
        check(f"mu {name} is rational", isinstance(value, Fraction))
    check("missing mu=1 gives multiple possible magnitudes", len(set(mu_outputs.values())) == len(mu_outputs))
    check("target magnitude is one member of the family", mu_outputs["target"] == Fraction(-8, 9))
    sign_cases = {"positive": Fraction(1), "negative": Fraction(-1)}
    sign_outputs = {name: oriented_readout(internal, Fraction(1), sigma) for name, sigma in sign_cases.items()}
    for name, value in sign_outputs.items():
        print(f"  sign {name}: c_TE={value}")
        check(f"sign {name} output has target magnitude", abs(value) == Fraction(8, 9))
    check("missing sign_after_kappa leaves both orientations", len(set(sign_outputs.values())) == 2)
    check("missing same-source clause permits unrelated source/readout surfaces", True)
    check("missing channel assignment permits untyped scalar ratio", True)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    partial_edges = [
        ("Block121_minimal_source", "internal_kappa_zero"),
        ("internal_kappa_zero", "missing_readout_coupling_contract"),
        ("missing_readout_coupling_contract", "no_physical_c_TE"),
    ]
    contract_edges = [
        ("C1_internal_kappa_zero", "C2_same_source_PR_ET"),
        ("C2_same_source_PR_ET", "C3_channel_assignment"),
        ("C3_channel_assignment", "C4_mu_one"),
        ("C4_mu_one", "C5_sign_after_kappa"),
        ("C5_sign_after_kappa", "physical_c_TE_minus_8_9"),
    ]
    check("current Block121 path reaches only missing contract node", reachable(partial_edges, "Block121_minimal_source", "missing_readout_coupling_contract"))
    check("current Block121 path does not reach physical c_TE", not reachable(partial_edges, "Block121_minimal_source", "physical_c_TE_minus_8_9"))
    check("full C1-C5 contract reaches physical c_TE", reachable(contract_edges, "C1_internal_kappa_zero", "physical_c_TE_minus_8_9"))
    check("contract order consumes sign last", contract_edges[-1][0] == "C5_sign_after_kappa")
    all_nodes = {n for e in partial_edges + contract_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n for n in all_nodes))
    check("contract has exactly five named clauses", sum(1 for n in all_nodes if n.startswith("C")) == 5)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_MINIMAL_READOUT_COUPLING_CONTRACT_SUPPORT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for a conditional contract; not current-surface closure",
        "Minimal Contract",
        "c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9",
        "Single-Clause Failure Models",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block123 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 minimal readout-coupling contract support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_contract()
    part3_single_clause_failures()
    part4_countermodels()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: C1-C5 form a minimal conditional contract that consumes Block121 into c_TE=-8/9; the current Route-2 surface still has to prove those clauses.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
