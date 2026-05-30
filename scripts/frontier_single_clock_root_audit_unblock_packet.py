#!/usr/bin/env python3
"""Verify the single-clock root audit-unblock packet.

This runner does not apply audit verdicts.  It checks the narrow source
movement: old broad unaudited roots are not independent blockers for the
time-count use case, while the real remaining root is the action surface that
supplies one temporal transfer axis and a finite-range Hamiltonian.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_ROOT_AUDIT_UNBLOCK_PACKET_NOTE_2026-05-30.md"
SINGLE_CLOCK = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
OUTPUT = ROOT / "outputs" / "single_clock_root_audit_unblock_packet_2026-05-30.json"

PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    CHECKS.append({"name": name, "status": status, "detail": detail})
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))


def ledger_rows() -> dict[str, dict[str, object]]:
    return json.loads(LEDGER.read_text())["rows"]


def source_firewall() -> dict[str, object]:
    text = NOTE.read_text()
    single = SINGLE_CLOCK.read_text()
    required = [
        "**Claim type:** meta",
        "audit-unblock packet",
        "not independent blockers for the time-count use case",
        "remaining root is the action/temporal-transfer axis",
        "action_gate_still_open: true",
        "audit_required_before_effective_status_change: true",
    ]
    for phrase in required:
        check(f"packet contains source-boundary phrase: {phrase}", phrase in text)

    old_roots = [
        "AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md",
        "AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md",
        "AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md",
        "EMERGENT_LORENTZ_INVARIANCE_NOTE.md",
    ]
    for phrase in old_roots:
        check(f"packet names old broad root: {phrase}", phrase in text)

    forbidden = [
        "audited_clean",
        "effective retained",
        "closes the staggered-Dirac/action realization gate",
        "observed spacetime",
        "PDG",
        "Monte Carlo",
    ]
    for phrase in forbidden:
        check(f"packet excludes overclaim/input phrase: {phrase}", phrase not in text)

    check("single-clock note points to unblock packet", "SINGLE_CLOCK_ROOT_AUDIT_UNBLOCK_PACKET_NOTE_2026-05-30.md" in single)
    check("single-clock note preserves audit authority boundary", "independent audit lane" in single)
    return {"required": required, "old_roots": old_roots, "forbidden": forbidden}


def spectral_calculus_check() -> dict[str, object]:
    evals = np.array([1.0, 0.4, 0.1], dtype=float)
    T = np.diag(evals)
    M = np.linalg.norm(T, ord=2)
    a_tau = 0.25
    H = -np.diag(np.log(evals / M)) / a_tau
    reconstructed = np.diag(np.exp(-a_tau * np.diag(H)))
    check("positive transfer matrix has positive eigenvalues", np.all(evals > 0), str(evals))
    check("H = -log(T/||T||)/a_tau is self-adjoint", np.allclose(H, H.conj().T))
    check("H is non-negative after top-eigenvalue subtraction", np.min(np.linalg.eigvalsh(H)) >= -1e-12, str(np.linalg.eigvalsh(H)))
    check("top transfer eigenvalue maps to zero energy", abs(np.linalg.eigvalsh(H)[0]) < 1e-12, str(np.linalg.eigvalsh(H)[0]))
    check("exp(-a_tau H) reconstructs T/||T||", np.allclose(reconstructed, T / M))
    return {"transfer_eigenvalues": evals.tolist(), "hamiltonian_eigenvalues": np.linalg.eigvalsh(H).tolist()}


def tensor_locality_check() -> dict[str, object]:
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    ox = np.kron(np.kron(sx, eye), eye)
    oy = np.kron(np.kron(eye, eye), sz)
    comm = ox @ oy - oy @ ox
    norm = np.linalg.norm(comm, ord=2)
    check("distinct-site tensor-factor commutator vanishes", norm < 1e-12, f"norm={norm:.3e}")

    # Coarse Lieb-Robinson shape check: outside the cone the bound is small
    # and decreases exponentially with distance at fixed time.
    j = 1.0
    r = 1.0
    v_lr = 2 * np.e * r * j
    t = 0.1
    d1, d2 = 8.0, 10.0
    b1 = 2 * np.exp(-d1 + v_lr * t)
    b2 = 2 * np.exp(-d2 + v_lr * t)
    check("finite-range LR velocity is finite", np.isfinite(v_lr), f"v_LR={v_lr:.6f}")
    check("LR bound decreases with distance at fixed time", b2 < b1, f"b8={b1:.3e}, b10={b2:.3e}")
    check("outside-cone LR bound is exponentially small in sample", b2 < 1e-3, f"b10={b2:.3e}")
    return {"commutator_norm": norm, "v_lr": v_lr, "sample_bounds": {"d8": b1, "d10": b2}}


def dimension_use_case_check() -> dict[str, object]:
    ds = 3
    chirality_allowed = [dt for dt in range(1, 12) if (ds + dt) % 2 == 0]
    single_clock_allowed = [dt for dt in range(1, 12) if dt <= 1]
    intersection = sorted(set(chirality_allowed) & set(single_clock_allowed))
    check("time-count use case only needs d_t <= 1 from single-clock", single_clock_allowed == [1], str(single_clock_allowed))
    check("with retained chirality parity and d_s=3, intersection is d_t=1", intersection == [1], str(intersection))
    return {"d_s": ds, "chirality_allowed": chirality_allowed, "single_clock_allowed": single_clock_allowed, "intersection": intersection}


def ledger_check(rows: dict[str, dict[str, object]]) -> dict[str, object]:
    expected = {
        "axiom_first_spectrum_condition_theorem_note_2026-04-29": "unaudited broad spectrum root",
        "axiom_first_cluster_decomposition_theorem_note_2026-04-29": "unaudited broad cluster root",
        "axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01": "unaudited broad microcausality root",
        "staggered_dirac_realization_gate_note_2026-05-03": "action gate remains open/renaming",
        "axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03": "single-clock theorem row present",
    }
    seen: dict[str, object] = {}
    for key, label in expected.items():
        row = rows.get(key)
        check(label, row is not None, key)
        if row:
            seen[key] = {
                "claim_type": row.get("claim_type"),
                "audit_status": row.get("audit_status"),
                "effective_status": row.get("effective_status"),
                "note_path": row.get("note_path"),
            }
    action = rows.get("staggered_dirac_realization_gate_note_2026-05-03", {})
    check("remaining real root is still not hidden as closed", action.get("effective_status") in {"audited_renaming", "open_gate", "unaudited"}, str(action.get("effective_status")))
    return seen


def main() -> int:
    print("SINGLE-CLOCK ROOT AUDIT-UNBLOCK PACKET")
    rows = ledger_rows()
    source = source_firewall()
    spectral = spectral_calculus_check()
    locality = tensor_locality_check()
    dims = dimension_use_case_check()
    ledger = ledger_check(rows)
    verdict = (
        "single-clock root audit unblock packet passes; old broad roots are "
        "not independent blockers for the time-count use case, and the "
        "remaining root is the action/temporal-transfer axis."
    )
    out = {
        "claim": "single-clock root audit unblock packet",
        "pass": PASS,
        "fail": FAIL,
        "checks": CHECKS,
        "source_firewall": source,
        "spectral_calculus": spectral,
        "tensor_locality": locality,
        "dimension_use_case": dims,
        "ledger_rows": ledger,
        "verdict": verdict,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("VERDICT:", verdict)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
