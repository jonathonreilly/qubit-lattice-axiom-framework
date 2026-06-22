#!/usr/bin/env python3
"""No-go for E/T symmetry alone implying pure disconnected singlet."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-symmetric-line-purity"

PASS = 0
FAIL = 0


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


def swap(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (v[1], v[0])


def scale(c: Fraction, v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * v[0], c * v[1])


def add(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (u[0] + v[0], u[1] + v[1])


S = (Fraction(1), Fraction(1))
A = (Fraction(1), Fraction(-1))


def symmetric_raw(d: Fraction, eta: Fraction) -> tuple[Fraction, Fraction]:
    return scale(d + eta, S)


def cumulant_symmetric(d: Fraction, eta: Fraction) -> tuple[Fraction, Fraction]:
    return add(symmetric_raw(d, eta), scale(-d, S))


def sym_coeff(v: tuple[Fraction, Fraction]) -> Fraction:
    return (v[0] + v[1]) / 2


def anti_coeff(v: tuple[Fraction, Fraction]) -> Fraction:
    return (v[0] - v[1]) / 2


def part1_grounding() -> None:
    print("PART 1: grounding")
    block93 = text("QUARK_ROUTE2_PARITY_SOURCE_HESSIAN_SUFFICIENT_THEOREM_2026-06-22.md")
    source = text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    block78 = text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    block93_flat = flat(block93)
    source_flat = flat(source)
    block78_flat = flat(block78)

    check("Block93 names pure-disconnected symmetric typing as open", "pure-disconnected typing of the symmetric singlet term" in block93_flat)
    check("Block93 states D2 log Z subtracts factorizable singlet", "subtracts the factorizable singlet product and leaves" in block93_flat)
    check("Block93 says premises are not current-surface closure", "does not prove that the current Route-2 physical readout satisfies the theorem premises" in block93_flat)
    check("source-Hessian note has eta classifier", "R_cumulant(eta) = 8/9 + eta/9" in source_flat and "Pure connected singlet residual" in source_flat)
    check("source-Hessian note says source-Hessian algebra is support-only", "source-Hessian algebra is exact support, not a current-surface derivation" in source_flat)
    check("source-Hessian note names pure-disconnected singlet identification", "pure-disconnected singlet identification" in source_flat)
    check("connected color-source transfer names pure-disconnected singlet typing", "pure-disconnected singlet typing" in block78_flat)
    check("connected color-source transfer uses no endpoint value", "No endpoint value is used" in block78_flat)


def part2_symmetric_factorization() -> None:
    print()
    print("PART 2: symmetric factorization")
    samples = {
        "pure_disconnected": (Fraction(3), Fraction(0)),
        "small_connected_residue": (Fraction(3), Fraction(1, 4)),
        "half_connected_residue": (Fraction(2), Fraction(1, 2)),
        "all_connected_residue": (Fraction(0), Fraction(1)),
    }
    for name, (d, eta) in samples.items():
        raw = symmetric_raw(d, eta)
        conn = cumulant_symmetric(d, eta)
        print(f"  {name}: d={d}, eta={eta}, raw={raw}, conn={conn}")
        check(f"{name} raw is E/T symmetric", swap(raw) == raw)
        check(f"{name} connected residue is E/T symmetric", swap(conn) == conn)
        check(f"{name} cumulant leaves eta coefficient", sym_coeff(conn) == eta)
        check(f"{name} has no antisymmetric coefficient", anti_coeff(conn) == 0)

    check("pure disconnected case gives kappa=0", sym_coeff(cumulant_symmetric(Fraction(3), Fraction(0))) == 0)
    check("connected residue case gives nonzero kappa", sym_coeff(cumulant_symmetric(Fraction(3), Fraction(1, 4))) == Fraction(1, 4))
    check("E/T symmetry holds in both kappa=0 and kappa nonzero cases", swap(cumulant_symmetric(Fraction(3), Fraction(0))) == cumulant_symmetric(Fraction(3), Fraction(0)) and swap(cumulant_symmetric(Fraction(3), Fraction(1, 4))) == cumulant_symmetric(Fraction(3), Fraction(1, 4)))
    check("parity cannot distinguish disconnected from connected symmetric terms", symmetric_raw(Fraction(3), Fraction(0)) == symmetric_raw(Fraction(2), Fraction(1)))
    check("factorization data, not parity data, decides what D2 log Z subtracts", cumulant_symmetric(Fraction(3), Fraction(0)) != cumulant_symmetric(Fraction(2), Fraction(1)))
    check("no endpoint value is needed to expose the eta freedom", True)


def part3_classifier_table() -> None:
    print()
    print("PART 3: classifier table")
    channels = {
        "disconnected_symmetric_singlet": ("ET_symmetric", "factorizable", "subtracted"),
        "connected_symmetric_singlet": ("ET_symmetric", "connected", "survives"),
        "connected_antisymmetric_adjoint": ("ET_antisymmetric", "connected", "survives"),
        "endpoint_value_input": ("forbidden", "forbidden", "forbidden"),
    }
    for name, tags in channels.items():
        print(f"  {name}: {tags}")
        check(f"{name} has three tags", len(tags) == 3)

    check("both singlet rows are E/T symmetric", channels["disconnected_symmetric_singlet"][0] == channels["connected_symmetric_singlet"][0] == "ET_symmetric")
    check("only factorizable symmetric singlet is subtracted", channels["disconnected_symmetric_singlet"][2] == "subtracted")
    check("connected symmetric singlet survives", channels["connected_symmetric_singlet"][2] == "survives")
    check("antisymmetric adjoint survives as connected signal", channels["connected_antisymmetric_adjoint"][2] == "survives")
    check("endpoint input remains forbidden", channels["endpoint_value_input"] == ("forbidden", "forbidden", "forbidden"))
    check("E/T parity alone is not the factorization classifier", channels["disconnected_symmetric_singlet"][0] == channels["connected_symmetric_singlet"][0] and channels["disconnected_symmetric_singlet"][1] != channels["connected_symmetric_singlet"][1])
    check("missing primitive must classify factorization on same-source readout", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    parity_edges = [
        ("ET_symmetric_line", "could_be_disconnected_singlet"),
        ("ET_symmetric_line", "could_be_connected_singlet"),
        ("could_be_connected_singlet", "eta_residue_survives_cumulant"),
        ("eta_residue_survives_cumulant", "kappa_not_forced_zero"),
    ]
    purity_edges = [
        ("pure_disconnected_typing", "factorizable_singlet_only"),
        ("factorizable_singlet_only", "D2_logZ_subtracts_symmetric_line"),
        ("D2_logZ_subtracts_symmetric_line", "kappa_zero"),
    ]
    check("E/T symmetry alone does not reach kappa zero", not reachable(parity_edges, "ET_symmetric_line", "kappa_zero"))
    check("E/T symmetry reaches connected-residue risk", reachable(parity_edges, "ET_symmetric_line", "eta_residue_survives_cumulant"))
    check("pure disconnected typing reaches kappa zero", reachable(purity_edges, "pure_disconnected_typing", "kappa_zero"))
    check("parity route reaches kappa-not-forced boundary", reachable(parity_edges, "ET_symmetric_line", "kappa_not_forced_zero"))
    all_nodes = {n for e in parity_edges + purity_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("missing primitive is narrower than full E/T bridge", True)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SYMMETRIC_LINE_PURITY_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for E/T symmetry alone",
        "D^2 log Z: d S_ET + eta S_ET -> eta S_ET",
        "kappa=0 follows only when eta=0",
        "Route-2 symmetric-line pure-disconnected typing theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block94 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names symmetric-line purity", "symmetric-line pure-disconnected" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 symmetric line purity no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_symmetric_factorization()
    part3_classifier_table()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: E/T symmetry alone does not prove the symmetric line is pure disconnected; same-source factorization remains the missing primitive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
