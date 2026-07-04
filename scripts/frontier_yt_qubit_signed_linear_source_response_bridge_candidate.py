#!/usr/bin/env python3
"""Finite C^6 signed-linear source-response support for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_qubit_signed_linear_source_response_bridge_candidate_2026-05-25.json"

NOTE = DOCS / "YT_QUBIT_SIGNED_LINEAR_SOURCE_RESPONSE_BRIDGE_CANDIDATE_NOTE_2026-05-25.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
DEMOCRATIC = DOCS / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
TOP_UNDERDETERMINATION = DOCS / "YT_TOP_RESPONSE_COEFFICIENT_UNDERDETERMINATION_NO_GO_NOTE_2026-05-25.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any] | None:
    ledger = json.loads(read(LEDGER))
    rows = ledger["rows"]
    if isinstance(rows, dict):
        return rows.get(claim_id)
    iterable = rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    return None


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors")
    for path in (NOTE, AXIOMS, LSP, DEMOCRATIC, TOP_UNDERDETERMINATION, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    check("note claim type is bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note type excludes physical bridge", "**Type:** exact finite support / physical bridge excluded" in note)
    for phrase in (
        "2026-06-07 Finite-Support Boundary",
        "Axiom-First Fork",
        "Exact Democratic Source",
        "Projective Probability Versus Signed Linear Response",
        "Boundary To Physical Y_T",
        "Why This Is Not The Old Ward Trap",
        "Current Status",
        "Firewalls",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    status_rows = {
        "source_action": ledger_row("yt_source_action_support_packet_note_2026-05-22"),
        "lsp_projective": ledger_row("lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22"),
        "democratic_c6": ledger_row("yt_qubit_democratic_top_coefficient_candidate_note_2026-05-25"),
        "top_underdetermination": ledger_row("yt_top_response_coefficient_underdetermination_no_go_note_2026-05-25"),
    }
    statuses = {key: None if row is None else row.get("effective_status") for key, row in status_rows.items()}
    check("source-action support row is present in the audit ledger (presence only)", status_rows["source_action"] is not None)
    check("LSP projective readout row is present in the audit ledger (presence only)", status_rows["lsp_projective"] is not None)
    check("S6-democratic C6 support row is present in the audit ledger (presence only)", status_rows["democratic_c6"] is not None)
    print(f"  [info] live effective statuses (audit-lane-owned; not gated): {statuses}")
    check(
        "top-response underdetermination note is not used as retained dependency",
        status_rows["top_underdetermination"] is not None
        and "boundary pointer only; it is not used here as a retained dependency" in note,
        statuses["top_underdetermination"],
    )
    check("minimal axioms are qubit-on-Z3 framed", "Reality is a qubit at every lattice site" in read(AXIOMS))
    check("LSP note records K_P = P", "K_P = P" in read(LSP))
    check("democratic note records 1/sqrt(6)", "1/sqrt(6)" in read(DEMOCRATIC))
    return statuses


def part2_baseline_alone_do_not_select() -> None:
    print("\nPart 2: baseline alone does not select coefficient")
    theta = sp.symbols("theta", real=True)
    u_theta = sp.Matrix([sp.cos(theta), sp.sin(theta), 0, 0, 0, 0])
    norm = (u_theta.T * u_theta)[0]
    amp_0 = u_theta[0]
    check("one-parameter normalized family exists in C^6", is_zero(norm - 1), norm)
    check("component amplitude varies with theta", sp.diff(amp_0, theta) != 0, sp.diff(amp_0, theta))
    check("theta=0 amplitude differs from theta=pi/4", sp.simplify(amp_0.subs(theta, 0) - amp_0.subs(theta, sp.pi / 4)) != 0)


def part3_democratic_source() -> None:
    print("\nPart 3: democratic source amplitude")
    n = 6
    entries = sp.symbols("u0:6")
    equations = [sp.Eq(entries[i], entries[i + 1]) for i in range(n - 1)]
    solution = sp.solve(equations, entries[1:], dict=True)[0]
    check("S6 transposition invariance forces equal entries", all(solution[entries[i]] == entries[0] for i in range(1, n)), solution)

    u_dem = sp.Matrix([1 / sp.sqrt(n)] * n)
    check("democratic vector unit norm", is_zero((u_dem.T * u_dem)[0] - 1), (u_dem.T * u_dem)[0])
    for i in range(n):
        amp = u_dem[i]
        check(f"component {i} signed amplitude is 1/sqrt(6)", is_zero(amp - 1 / sp.sqrt(n)), amp)


def part4_probability_vs_linear_source() -> dict[str, Any]:
    print("\nPart 4: projective probability versus signed linear source")
    n = 6
    u_dem = sp.Matrix([1 / sp.sqrt(n)] * n)
    i = 2
    projector = sp.zeros(n)
    projector[i, i] = 1
    probability = (u_dem.T * projector * u_dem)[0]
    amplitude = u_dem[i]
    check("LSP component projective probability is 1/6", is_zero(probability - sp.Rational(1, 6)), probability)
    check("signed linear component amplitude is 1/sqrt(6)", is_zero(amplitude - 1 / sp.sqrt(6)), amplitude)
    check("probability is the square of amplitude", is_zero(probability - amplitude**2), probability - amplitude**2)
    check("probability is not the desired amplitude", not is_zero(probability - amplitude), sp.simplify(probability - amplitude))

    s = sp.symbols("s")
    o = sp.symbols("O0:6")
    source_action = s * sum(u_dem[j] * o[j] for j in range(n))
    tangent = sp.diff(source_action, s).coeff(o[i])
    check("linear source/action tangent returns signed amplitude", is_zero(tangent - amplitude), tangent)
    return {
        "projective_probability": "1/6",
        "signed_linear_amplitude": "1/sqrt(6)",
        "linear_source_tangent": str(tangent),
    }


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG values",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "top Yukawa coefficient y_33 equals that signed-linear tangent",
        "top response/correlator",
        "retained top-coefficient theorem",
        "physical top-response bridge open",
    ):
        check(f"physical-bridge boundary phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "Status: retained",
        "proposed_retained",
        "`y_33` is derived",
        "`y_t` is derived",
        "positive Y_T closure has been obtained",
        "full retained closure",
        "physical top-response bridge is closed",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T QUBIT SIGNED-LINEAR SOURCE RESPONSE FINITE SUPPORT")
    print("=" * 78)

    statuses = part1_anchors()
    part2_baseline_alone_do_not_select()
    part3_democratic_source()
    fork = part4_probability_vs_linear_source()
    part5_firewalls()

    result = {
        "status": "bounded exact finite support: signed-linear democratic source tangent gives 1/sqrt(6); physical top-response bridge remains open",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The finite-dimensional signed-linear source tangent is exact, but the packet "
            "does not prove that the physical top Yukawa coefficient is this tangent."
        ),
        "fork": fork,
        "upstream_statuses": statuses,
        "remaining_bridge": "strict top Yukawa coefficient equals signed linear action-tangent component of democratic Q_L source",
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_QUBIT_SIGNED_LINEAR_SOURCE_RESPONSE_BRIDGE_CANDIDATE_NOTE_2026-05-25.md",
            "scripts/frontier_yt_qubit_signed_linear_source_response_bridge_candidate.py",
            "outputs/yt_qubit_signed_linear_source_response_bridge_candidate_2026-05-25.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
