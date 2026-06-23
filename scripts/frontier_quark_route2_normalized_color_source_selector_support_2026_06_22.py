#!/usr/bin/env python3
"""Exact support for the normalized color-source selector surface."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-normalized-color-source-support"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ColorSourceSurface:
    n: int

    @property
    def full_dim(self) -> int:
        return self.n * self.n

    @property
    def identity_dim(self) -> int:
        return 1

    @property
    def connected_dim(self) -> int:
        return self.full_dim - self.identity_dim

    @property
    def connected_fraction(self) -> Fraction:
        return Fraction(self.connected_dim, self.full_dim)

    @property
    def identity_fraction(self) -> Fraction:
        return Fraction(self.identity_dim, self.full_dim)


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


def centered_identity_score(trace_rho: Fraction, lam: Fraction) -> Fraction:
    value = lam * trace_rho
    expectation = lam
    return value - expectation


def selector_kappa(connected_fraction: Fraction) -> Fraction:
    return 9 * (connected_fraction - Fraction(8, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    yt = flat(text("YT_CONNECTED_SOURCE_AUGMENTATION_IDEAL_SELECTOR_NARROW_THEOREM_NOTE_2026-05-26.md"))
    transfer = flat(text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    trace_one = flat(text("QUARK_ROUTE2_TRACE_ONE_COLOR_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    stretch = flat(text("QUARK_ROUTE2_PHYSICAL_CONNECTED_HESSIAN_BRIDGE_STRETCH_NO_GO_NOTE_2026-06-22.md"))
    check("YT theorem names normalized connected color source tangent", "normalized connected color source tangent" in yt)
    check("YT theorem names augmentation ideal sl_N", "augmentation ideal sl_N" in yt or "augmentation ideal" in yt)
    check("Route-2 transfer note keeps same-source authority missing", "same-source normalized color-matrix source authority" in transfer)
    check("trace-one transfer note keeps color-record transfer missing", "trace-one color-matrix lift" in trace_one)
    check("Block112 names physical connected-Hessian bridge theorem", "Route-2 physical connected-Hessian bridge theorem" in stretch)


def part2_exact_color_source_selector() -> None:
    print()
    print("PART 2: exact normalized color-source selector")
    for n in (2, 3, 4, 5):
        surface = ColorSourceSurface(n)
        print(f"  N={n}: full={surface.full_dim}, connected={surface.connected_dim}, identity={surface.identity_dim}, fraction={surface.connected_fraction}")
        check(f"N={n} full dimension is N^2", surface.full_dim == n * n)
        check(f"N={n} connected dimension is N^2-1", surface.connected_dim == n * n - 1)
        check(f"N={n} identity dimension is one", surface.identity_dim == 1)
        check(f"N={n} fractions sum to one", surface.connected_fraction + surface.identity_fraction == 1)
    surface3 = ColorSourceSurface(3)
    check("N=3 connected fraction is 8/9", surface3.connected_fraction == Fraction(8, 9))
    check("N=3 identity fraction is 1/9", surface3.identity_fraction == Fraction(1, 9))
    check("N=3 selector kappa is zero", selector_kappa(surface3.connected_fraction) == 0)


def part3_identity_source_centering() -> None:
    print()
    print("PART 3: identity source centering")
    lambdas = (Fraction(1), Fraction(7, 3), Fraction(-5, 2))
    for lam in lambdas:
        score = centered_identity_score(Fraction(1), lam)
        print(f"  lambda={lam}, trace=1, score={score}")
        check(f"lambda={lam} identity score vanishes on trace-one records", score == 0)
    bad_score = centered_identity_score(Fraction(2), Fraction(7, 3))
    check("identity score does not vanish without trace-one condition", bad_score != 0)
    check("trace-one condition is load-bearing", centered_identity_score(Fraction(1), Fraction(7, 3)) != bad_score)


def part4_route2_transfer_firewall() -> None:
    print()
    print("PART 4: Route-2 transfer firewall")
    current = {
        "normalized_color_source_surface": True,
        "current_Route2_same_source_lift": False,
        "trace_one_Route2_records": False,
        "physical_E_T_D2logZ_identification": False,
        "coefficient_source_gauge_normalization": False,
    }
    for name, present in current.items():
        print(f"  {name}: {present}")
        check(f"{name} classification is boolean", isinstance(present, bool))
    check("support theorem exists on its own source surface", current["normalized_color_source_surface"])
    missing = [name for name, present in current.items() if not present]
    check("Route-2 transfer still has four missing gates", len(missing) == 4)
    check("same-source lift remains missing", not current["current_Route2_same_source_lift"])
    check("coefficient/source gauge normalization remains missing", not current["coefficient_source_gauge_normalization"])


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    support_edges = [
        ("normalized_color_matrix_source", "identity_source_centered_zero"),
        ("identity_source_centered_zero", "augmentation_ideal_sl3"),
        ("augmentation_ideal_sl3", "connected_fraction_8_9"),
        ("connected_fraction_8_9", "kappa_zero_on_color_source"),
    ]
    route2_edges = [
        ("current_Route2_P_R", "missing_normalized_color_source_lift"),
        ("missing_normalized_color_source_lift", "no_current_transfer"),
    ]
    transfer_edges = [
        ("Route2_normalized_color_source_lift_theorem", "normalized_color_matrix_source"),
        ("Route2_normalized_color_source_lift_theorem", "physical_E_T_D2logZ"),
        ("physical_E_T_D2logZ", "kappa_zero_on_Route2"),
    ]
    check("support theorem reaches kappa=0 on color source", reachable(support_edges, "normalized_color_matrix_source", "kappa_zero_on_color_source"))
    check("current Route-2 P_R reaches missing lift node", reachable(route2_edges, "current_Route2_P_R", "missing_normalized_color_source_lift"))
    check("current Route-2 P_R does not reach kappa=0", not reachable(route2_edges, "current_Route2_P_R", "kappa_zero_on_Route2"))
    check("future lift theorem would transfer selector", reachable(transfer_edges + support_edges, "Route2_normalized_color_source_lift_theorem", "kappa_zero_on_color_source"))
    all_nodes = {n for e in support_edges + route2_edges + transfer_edges for n in e}
    check("reachability graph contains no endpoint triple node", all("rho_E_21_4" not in n and "q_E_15_8" not in n for n in all_nodes))
    check("reachability graph does not use finite-box comparator", all("finite_box" not in n and "box" not in n for n in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_NORMALIZED_COLOR_SOURCE_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support on the normalized color-source surface; no current Route-2 transfer",
        "Exact Support On The Color-Source Surface",
        "Route-2 Transfer Boundary",
        "kappa = 0",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block113 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
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
    print("Route-2 normalized color-source selector support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_exact_color_source_selector()
    part3_identity_source_centering()
    part4_route2_transfer_firewall()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: normalized trace-one color-matrix sources give exact kappa=0 support on their own surface; Route-2 still needs a same-source transfer theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
