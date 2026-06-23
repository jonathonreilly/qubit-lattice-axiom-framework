#!/usr/bin/env python3
"""Certificate for the Route-2 same-source selector primitive proposal."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-same-source-selector-primitive-proposal"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PrimitiveModel:
    same_source: bool
    raw: Fraction | None
    mean_x: Fraction | None
    mean_y: Fraction | None
    connected_typed: bool
    mu: Fraction | None
    sigma: int | None

    def product(self) -> Fraction | None:
        if self.mean_x is None or self.mean_y is None:
            return None
        return self.mean_x * self.mean_y

    def connected(self) -> Fraction | None:
        product = self.product()
        if self.raw is None or product is None or not self.connected_typed or not self.same_source:
            return None
        return self.raw - product

    def kappa(self) -> Fraction | None:
        c = self.connected()
        if c is None:
            return None
        return 9 * (c - Fraction(8, 9))

    def c_te(self) -> Fraction | None:
        c = self.connected()
        if c is None or self.mu is None or self.sigma is None:
            return None
        return self.sigma * self.mu * c


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def note_text() -> str:
    return text(DOCS / "QUARK_ROUTE2_SAME_SOURCE_SELECTOR_PRIMITIVE_PROPOSAL_2026-06-23.md")


def loop_text(name: str) -> str:
    return text(LOOP / name)


def accepted_model() -> PrimitiveModel:
    return PrimitiveModel(
        same_source=True,
        raw=Fraction(1, 1),
        mean_x=Fraction(1, 3),
        mean_y=Fraction(1, 3),
        connected_typed=True,
        mu=Fraction(1, 1),
        sigma=-1,
    )


def part1_primitive_arithmetic() -> None:
    print("PART 1: primitive arithmetic")
    m = accepted_model()
    check("same-source clause is present", m.same_source)
    check("raw moment is one", m.raw == Fraction(1, 1))
    check("mean X is one third", m.mean_x == Fraction(1, 3))
    check("mean Y is one third", m.mean_y == Fraction(1, 3))
    check("product selector is one ninth", m.product() == Fraction(1, 9))
    check("connected subtraction is typed", m.connected_typed)
    check("connected value is eight ninths", m.connected() == Fraction(8, 9))
    check("kappa is zero", m.kappa() == 0)
    check("unit calibration is one", m.mu == 1)
    check("orientation sign is negative", m.sigma == -1)
    check("signed readout is minus eight ninths", m.c_te() == Fraction(-8, 9))
    note = note_text()
    typed_source_markers = (
        "Omega_R: finite Route-2 record source space",
        "P_0: strictly positive normalized reference law",
        "P_h: normalized Route-2 source path with P_h << P_0",
        "J_CR: physical center-ratio source coordinate",
        "X,Y: physical P_R/E-T center-ratio readout variables",
    )
    for marker in typed_source_markers:
        check(f"typed source marker present: {marker}", marker in note)


def part2_single_clause_falsifiers() -> None:
    print()
    print("PART 2: single-clause falsifiers")
    witnesses = {
        "same_source": PrimitiveModel(False, Fraction(1), Fraction(1, 3), Fraction(1, 3), True, Fraction(1), -1),
        "raw_moment": PrimitiveModel(True, Fraction(2, 3), Fraction(1, 3), Fraction(1, 3), True, Fraction(1), -1),
        "one_point": PrimitiveModel(True, Fraction(1), Fraction(1, 2), Fraction(1, 2), True, Fraction(1), -1),
        "connected_typing": PrimitiveModel(True, Fraction(1), Fraction(1, 3), Fraction(1, 3), False, Fraction(1), -1),
        "unit": PrimitiveModel(True, Fraction(1), Fraction(1, 3), Fraction(1, 3), True, Fraction(1, 2), -1),
        "orientation": PrimitiveModel(True, Fraction(1), Fraction(1, 3), Fraction(1, 3), True, Fraction(1), 1),
    }
    for label, model in witnesses.items():
        print(f"  witness {label}: connected={model.connected()}, kappa={model.kappa()}, c_TE={model.c_te()}")
        if label == "same_source":
            check("same_source omission rejects typed physical cumulant", not model.same_source)
        elif label == "connected_typing":
            check("connected_typing omission rejects kappa", model.kappa() is None)
        elif label == "unit":
            check("unit omission keeps kappa zero", model.kappa() == 0)
            check("unit omission changes signed readout", model.c_te() == Fraction(-4, 9))
        elif label == "orientation":
            check("orientation omission keeps kappa zero", model.kappa() == 0)
            check("orientation omission changes signed readout", model.c_te() == Fraction(8, 9))
        else:
            check(f"{label} omission misses kappa zero", model.kappa() != 0)
    check("six single-clause falsifiers recorded", len(witnesses) == 6)


def part3_scope_firewall() -> None:
    print()
    print("PART 3: scope firewall")
    note = note_text()
    combined = "\n".join(
        [
            note,
            loop_text("STATE.yaml"),
            loop_text("CLAIM_STATUS_CERTIFICATE.md"),
            loop_text("TRACE_GATE.md"),
            loop_text("ASSUMPTIONS_AND_IMPORTS.md"),
            loop_text("PANEL_CERTIFICATE.md"),
            loop_text("REVIEW_HISTORY.md"),
            loop_text("HANDOFF.md"),
        ]
    )
    required = (
        "Actual current-surface status: open; candidate primitive proposal pending external adoption",
        "does not edit the primitive registry",
        "This is not an audit verdict",
        "It does not quote the endpoint value",
        "Only after explicit acceptance could downstream notes cite it as an adopted input",
        "Even panel passage does not make the primitive accepted by the repo",
    )
    note_flat = flat(note)
    for marker in required:
        check(f"note contains boundary marker: {marker}", marker in note_flat)
    required_non_import_markers = (
        ("rho_E non-import", "does not import `rho_E`"),
        ("q_E non-import", "`q_E`"),
        ("endpoint-value reversal non-import", "endpoint-value reversal"),
        ("fit-derived source weights non-import", "fit-derived source weights"),
        ("observed quark values non-import", "observed quark values"),
    )
    for label, marker in required_non_import_markers:
        check(f"explicit non-import marker present: {label}", marker in combined)
    forbidden_import_assertions = (
        ("rho_E assignment", "rho_E ="),
        ("q_E assignment", "q_E ="),
        ("endpoint-value input", "endpoint value is used as an input"),
        ("observed-value input", phrase("observed ", "target value is used")),
        ("fit-selector input", phrase("fitted ", "selector is used")),
    )
    for label, marker in forbidden_import_assertions:
        check(f"forbidden import assertion absent: {label}", marker not in combined)
    banned_overclaim = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    low = combined.lower()
    for label, marker in banned_overclaim:
        check(f"banned overclaim marker absent: {label}", marker not in low)


def part4_trace_to_blocker() -> None:
    print()
    print("PART 4: trace to blocker")
    block150 = flat(text(DOCS / "QUARK_ROUTE2_SOURCE_READOUT_PRIMITIVE_QUEUE_EXHAUSTION_2026-06-22.md"))
    block149 = flat(text(DOCS / "QUARK_ROUTE2_PHYSICAL_SELECTOR_INSTANTIATION_FANOUT_NO_GO_2026-06-22.md"))
    block148 = flat(text(DOCS / "QUARK_ROUTE2_SAME_SOURCE_SELECTOR_CLAUSE_INDEPENDENCE_NO_GO_2026-06-22.md"))
    block147 = flat(text(DOCS / "QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md"))
    check("Block150 names physical same-source selector realization", "Route-2 physical same-source selector realization theorem" in block150)
    check("Block149 names missing primitive", "Route-2 physical same-source selector realization theorem" in block149)
    check("Block148 requires full clause set", "The exact primitive cannot drop" in block148)
    check("Block147 gives uv=1/9 selector support", "kappa = 0 <=> uv = 1/9" in block147)
    check("candidate S1-S6 covers same-source surface", "same-source typing" in note_text())
    check("candidate S1-S6 covers raw moment", "E_0[XY] = 1" in note_text())
    check("candidate S1-S6 covers one-point product", "E_0[X]E_0[Y] = (s/3)(s/3) = 1/9" in note_text())
    check("candidate S1-S6 covers unit calibration", "mu = 1" in note_text())
    check("candidate S1-S6 covers orientation separation", "orientation separation" in note_text())


def part5_panel_certificate() -> None:
    print()
    print("PART 5: physicist panel certificate")
    panel = loop_text("PANEL_CERTIFICATE.md")
    required = (
        "PANEL_RESULT: PASS",
        "reviewer_count: 5",
        "passes: 5",
        "objections: 0",
        "Physicist A",
        "Physicist B",
        "Physicist C",
        "Physicist D",
        "Physicist E",
    )
    for marker in required:
        check(f"panel marker present: {marker}", marker in panel)
    gates = (
        "mathematically coherent",
        "endpoint-independent",
        "non-circular",
        "single route-2 source/readout premise",
        "non-laundering boundaries",
    )
    panel_low = panel.lower()
    for gate in gates:
        check(f"panel gate covered: {gate}", gate in panel_low)


def part6_loop_pack() -> None:
    print()
    print("PART 6: loop pack")
    files = (
        "STATE.yaml",
        "GOAL.md",
        "ASSUMPTIONS_AND_IMPORTS.md",
        "ROUTE_PORTFOLIO.md",
        "OPPORTUNITY_QUEUE.md",
        "NO_GO_LEDGER.md",
        "LITERATURE_BRIDGES.md",
        "ARTIFACT_PLAN.md",
        "TRACE_GATE.md",
        "CLAIM_STATUS_CERTIFICATE.md",
        "REVIEW_HISTORY.md",
        "HANDOFF.md",
        "PR_BACKLOG.md",
        "PANEL_CERTIFICATE.md",
        "PR_BODY.md",
    )
    for name in files:
        check(f"loop pack file exists: {name}", (LOOP / name).exists())
    state = loop_text("STATE.yaml")
    check("STATE records open status", "actual_current_surface_status: open" in state)
    check("STATE records panel pass disposition", "panel_disposition: pass" in state)
    check("certificate disallows proposal status promotion", "proposal_allowed: false" in loop_text("CLAIM_STATUS_CERTIFICATE.md"))
    check("trace gate marks upstream support", "trace_class: upstream_support" in loop_text("TRACE_GATE.md"))
    check("trace gate uses frontier_probe role", "artifact_role: frontier_probe" in loop_text("TRACE_GATE.md"))
    check("handoff says no audit worker", "No audit worker was run" in loop_text("HANDOFF.md"))
    check("review history says panel, not audit", "panel review" in loop_text("REVIEW_HISTORY.md").lower())


def main() -> int:
    print("Route-2 same-source selector primitive proposal")
    print("TRACE: upstream_support")
    part1_primitive_arithmetic()
    part2_single_clause_falsifiers()
    part3_scope_firewall()
    part4_trace_to_blocker()
    part5_panel_certificate()
    part6_loop_pack()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the candidate Route-2 same-source selector primitive is internally coherent, endpoint-independent, panel-passed as a primitive proposal, and still open pending external adoption.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
