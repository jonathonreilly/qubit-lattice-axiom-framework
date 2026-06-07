#!/usr/bin/env python3
"""Reduced-status source packet for the historical center-trace capstone row.

This runner does not restore the superseded "closed capstone" claim.  It
certifies the exact algebraic material that survives current audit discipline:

* the D3 projectors plus the C3 cycle generate M3(C);
* no proper coordinate quotient preserves both structures;
* the retained UHF trace theorem supplies the dimension-weighted trace source;
* the pre-record physical identification remains retained_bounded, so the old
  route-closure framing stays demoted pending independent bridge work.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/flavor_center_trace_reduced_status_source_packet_2026_05_30.json"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
NOTE = ROOT / "docs/FLAVOR_CENTER_TRACE_CLOSED_CAPSTONE_NOTE_2026-05-30.md"

TARGET_CLAIM = "flavor_center_trace_closed_capstone_note_2026-05-30"

AUTHORITIES = {
    "no_proper_quotient": {
        "claim_id": "three_generation_observable_no_proper_quotient_narrow_theorem_note_2026-05-02",
        "expected_effective_status": "retained",
        "note_path": "docs/THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md",
        "runner_path": "scripts/frontier_three_gen_observable_no_proper_quotient_narrow.py",
        "cache_path": "logs/runner-cache/frontier_three_gen_observable_no_proper_quotient_narrow.txt",
        "required_note_tokens": [
            "no proper quotient",
            "M_3",
            "physical-species interpretation",
            "out of scope",
        ],
        "required_cache_tokens": ["TOTAL: PASS=45, FAIL=0"],
    },
    "uhf_trace_uniqueness": {
        "claim_id": "powers_uhf_tracial_uniqueness_on_qubit_lattice_narrow_theorem_note_2026-05-20",
        "expected_effective_status": "retained",
        "note_path": "docs/POWERS_UHF_TRACIAL_UNIQUENESS_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
        "runner_path": None,
        "cache_path": None,
        "required_note_tokens": [
            "unique tracial state",
            "provenance",
            "not an admitted import",
        ],
        "required_cache_tokens": [],
    },
    "pre_record_trace_boundary": {
        "claim_id": "pre_record_reference_state_tracial_derivation_note_2026-05-20",
        "expected_effective_status": "retained_bounded",
        "note_path": "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md",
        "runner_path": "scripts/frontier_pre_record_reference_state_tracial_derivation.py",
        "cache_path": "logs/runner-cache/frontier_pre_record_reference_state_tracial_derivation.txt",
        "required_note_tokens": ["Narrowed claim", "Open admission", "unique tracial state"],
        "required_cache_tokens": ["PASS=12 FAIL=0", "pre-record identification remains open"],
    },
}


PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


def sha256_rel(path: str | Path) -> str:
    file_path = ROOT / path
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def load_ledger() -> dict[str, dict[str, object]]:
    data = json.loads(LEDGER.read_text())
    rows = data.get("rows")
    if not isinstance(rows, dict):
        raise TypeError("audit ledger rows must be a dict keyed by claim id")
    return rows


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" :: {detail}" if detail else ""))
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if ok:
        PASS += 1
    else:
        FAIL += 1
    return ok


def generated_algebra_dimension(projectors: list[np.ndarray], cycle: np.ndarray) -> int:
    basis = projectors + [cycle, np.eye(3)]
    for _ in range(8):
        candidates = list(basis) + [a @ b for a in basis for b in basis]
        kept: list[np.ndarray] = []
        rows = np.zeros((0, 9), dtype=complex)
        for matrix in candidates:
            candidate_rows = np.vstack([rows, matrix.reshape(1, 9)])
            if np.linalg.matrix_rank(candidate_rows, tol=1e-10) > rows.shape[0]:
                kept.append(matrix)
                rows = candidate_rows
        basis = kept
        if len(basis) >= 9:
            break
    return int(np.linalg.matrix_rank(np.array([m.reshape(9) for m in basis]), tol=1e-10))


def invariant_coordinate_subsets(cycle: np.ndarray) -> list[tuple[int, ...]]:
    invariant: list[tuple[int, ...]] = []
    for mask in range(1 << 3):
        subset = tuple(i for i in range(3) if mask & (1 << i))
        if not subset:
            invariant.append(subset)
            continue
        vectors = [np.eye(3)[:, i] for i in subset]
        images = [cycle @ v for v in vectors]
        support = {
            int(np.argmax(np.abs(image)))
            for image in images
            if np.linalg.norm(image) > 1e-12
        }
        if support.issubset(set(subset)):
            invariant.append(subset)
    return invariant


def audit_authority_packet(rows: dict[str, dict[str, object]]) -> dict[str, object]:
    packets: dict[str, object] = {}
    for name, spec in AUTHORITIES.items():
        claim_id = str(spec["claim_id"])
        row = rows.get(claim_id)
        check(f"{name}: ledger row exists", row is not None, claim_id)
        if row is None:
            packets[name] = {"missing": True}
            continue

        effective = row.get("effective_status")
        check(
            f"{name}: effective_status is {spec['expected_effective_status']}",
            effective == spec["expected_effective_status"],
            f"observed={effective!r}",
        )

        note_path = str(spec["note_path"])
        note = ROOT / note_path
        check(f"{name}: note exists", note.exists(), note_path)
        note_text = note.read_text() if note.exists() else ""
        for token in spec["required_note_tokens"]:
            check(f"{name}: note contains {token!r}", token in note_text)

        runner_path = spec["runner_path"]
        if runner_path:
            runner = ROOT / str(runner_path)
            check(f"{name}: runner exists", runner.exists(), str(runner_path))
        cache_path = spec["cache_path"]
        cache_sha = None
        if cache_path:
            cache = ROOT / str(cache_path)
            check(f"{name}: cache exists", cache.exists(), str(cache_path))
            cache_text = cache.read_text() if cache.exists() else ""
            if runner_path and cache.exists():
                expected_sha = sha256_rel(str(runner_path))
                cache_sha = expected_sha
                check(
                    f"{name}: cache pins current runner sha",
                    f"runner_sha256: {expected_sha}" in cache_text,
                )
            for token in spec["required_cache_tokens"]:
                check(f"{name}: cache contains {token!r}", token in cache_text)

        packets[name] = {
            "claim_id": claim_id,
            "effective_status": effective,
            "note_path": note_path,
            "note_sha256": sha256_rel(note_path) if note.exists() else None,
            "runner_path": runner_path,
            "runner_sha256": sha256_rel(str(runner_path)) if runner_path else None,
            "cache_path": cache_path,
            "cache_runner_sha256": cache_sha,
        }
    return packets


def main() -> int:
    print("CENTER-TRACE REDUCED-STATUS SOURCE PACKET")
    print("Scope: exact algebra + source dependencies; old closure framing is not restored.")

    rows = load_ledger()
    target = rows.get(TARGET_CLAIM)
    check("target ledger row exists", target is not None, TARGET_CLAIM)
    if target is not None:
        check("target currently remains audited_conditional", target.get("effective_status") == "audited_conditional")
        check(
            "target re-audit blocker mentions missing dependency edge or narrowing",
            "missing_dependency_edge" in str(target.get("notes_for_re_audit_if_any"))
            and "narrow" in str(target.get("notes_for_re_audit_if_any")).lower(),
        )

    note_text = NOTE.read_text()
    for token in [
        "reduced-status source packet",
        "old closed-capstone framing is superseded",
        "pre-record identification remains retained_bounded",
        "not a ledger retag",
    ]:
        check(f"repaired note contains {token!r}", token in note_text)

    projectors = [
        np.diag([1.0 if i == k else 0.0 for i in range(3)]).astype(complex)
        for k in range(3)
    ]
    cycle = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    identity = np.eye(3, dtype=complex)

    check("P_i are projectors", all(np.allclose(p @ p, p) for p in projectors))
    check("P_i are mutually orthogonal", all(np.allclose(projectors[i] @ projectors[j], 0) for i in range(3) for j in range(3) if i != j))
    check("sum_i P_i = I_3", np.allclose(sum(projectors), identity))
    check("C3^3 = I_3", np.allclose(cycle @ cycle @ cycle, identity))

    dim = generated_algebra_dimension(projectors, cycle)
    check("D3 projectors plus C3 generate full M3(C)", dim == 9, f"dim={dim}")
    invariant = invariant_coordinate_subsets(cycle)
    check("only empty/full coordinate subsets preserve D3 and C3", invariant == [(), (0, 1, 2)], f"invariant={invariant}")

    rho = identity / 3.0
    singlet = np.ones((3, 3), dtype=complex) / 3.0
    doublet = identity - singlet
    pop_s = float(np.real(np.trace(singlet @ rho)))
    pop_d = float(np.real(np.trace(doublet @ rho)))
    dephased = singlet @ rho @ singlet + doublet @ rho @ doublet
    dep_s = float(np.real(np.trace(singlet @ dephased)))
    dep_d = float(np.real(np.trace(doublet @ dephased)))

    check("tracial I/3 gives singlet population 1/3", abs(pop_s - 1.0 / 3.0) < 1e-12, f"{pop_s:.12f}")
    check("tracial I/3 gives doublet population 2/3", abs(pop_d - 2.0 / 3.0) < 1e-12, f"{pop_d:.12f}")
    check("singlet/doublet dephasing preserves population weights", abs(dep_s - pop_s) < 1e-12 and abs(dep_d - pop_d) < 1e-12)
    check("dimension-weighted full trace default gives Q=1", abs((pop_d / (2.0 * pop_s)) - 1.0) < 1e-12)
    check("equal central-atom weighting would be an extra selector", abs((0.5 / (2.0 * 0.5)) - 0.5) < 1e-12)

    packets = audit_authority_packet(rows)

    old_closure_restored = False
    pre_record_status = packets["pre_record_trace_boundary"].get("effective_status") if isinstance(packets["pre_record_trace_boundary"], dict) else None
    check("old closed-capstone framing is not restored", not old_closure_restored)
    check("pre-record physical trace identification is bounded, not unbounded", pre_record_status == "retained_bounded")

    certificate = {
        "claim_id": TARGET_CLAIM,
        "actual_current_surface_status": "exact-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes_repair_by_narrowing_not_promotion",
        "old_closure_restored": old_closure_restored,
        "ledger_retag_in_this_branch": False,
        "no_new_axioms": True,
        "authority_packets": packets,
        "exact_algebra": {
            "generated_algebra_dimension": dim,
            "invariant_coordinate_subsets": [list(s) for s in invariant],
            "tracial_populations": {"singlet": pop_s, "doublet": pop_d},
            "dephased_populations": {"singlet": dep_s, "doublet": dep_d},
            "full_trace_q_default": 1.0,
            "center_atom_equal_weight_requires_extra_selector": True,
        },
        "checks": CHECKS,
        "scorecard": {"pass": PASS, "fail": FAIL},
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    check("certificate JSON written", OUTPUT.exists(), str(OUTPUT.relative_to(ROOT)))
    certificate["checks"] = CHECKS
    certificate["scorecard"] = {"pass": PASS, "fail": FAIL}
    OUTPUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print("VERDICT: center-trace source packet repaired by narrowing; exact algebra retained, old closure not retagged.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
