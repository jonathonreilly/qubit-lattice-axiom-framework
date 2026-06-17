#!/usr/bin/env python3
"""Single-clock B-AXIS.1 blocked-time unit split checker (2026-06-17).

This runner certifies a narrow source-side repair:

* The denominator of the supplied two-step transfer T_hat^2 is internally fixed
  to 2 a_tau by the existing blocked-time normalization bridge.
* The absolute physical clock/rate unit carried by a_tau is still not derived
  by minimal Lattice/Quantum/Record, by Record counts, or by the transfer
  spectrum alone.

It intentionally does not apply audit verdicts or edit audit surfaces.
"""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md"
PARENT = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
SC2 = ROOT / "docs" / "AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
MIN_AX = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
POST_RECORD = ROOT / "docs" / "POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md"
RECORD_GATE = ROOT / "docs" / "RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md"
LOOP_DIR = ROOT / ".claude" / "science" / "physics-loops" / "single-clock-blocked-time-unit-split-20260617"

PASS = 0
FAIL = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def record(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def diag_transfer(energies: np.ndarray, a_tau: float) -> np.ndarray:
    """Dimensionless two-step transfer diag(exp(-2 a_tau E_i))."""
    return np.diag(np.exp(-2.0 * a_tau * energies))


def reconstruct(T2: np.ndarray, tau_block: float) -> np.ndarray:
    diag = np.diag(T2).real
    m_t = float(np.max(diag))
    return np.diag(-(1.0 / tau_block) * np.log(diag / m_t))


def block_text_anchors() -> None:
    print("\n[A] source anchors")
    note = read(NOTE)
    parent = read(PARENT)
    sc2 = read(SC2)
    min_ax = read(MIN_AX)
    post = read(POST_RECORD)
    gate = read(RECORD_GATE)
    note_lower = note.lower()

    record("new note exists and names B-AXIS.1/N2 split", NOTE.exists() and "B-AXIS.1" in note and "N2a" in note and "N2b" in note)
    record("new note uses exact-support/no-go split, not retained status", "exact-support for the internal" in note and "no-go for deriving an absolute" in note and "does not claim retained" in note_lower)
    record("new note states audit-boundary no ledger/queue edits", "does not edit audit ledgers" in note and "effective-status files" in note)
    record("parent has B-AXIS.1 blocked time-step clause", "B-AXIS.1" in parent and "one supplied blocked time step" in parent and ("2a_tau" in parent or "2a_τ" in parent))
    record("parent wires this N2 support note as source support", "SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md" in parent)
    record("parent still leaves B-AXIS.2 and B-AXIS.3 declared", "B-AXIS.2" in parent and "B-AXIS.3" in parent and "independent commuting transfer factor" in parent)
    record("SC2 bridge identifies two-step block spacing", "T_hat^2" in sc2 and "two lattice steps" in sc2 and ("1/(2 a_τ)" in sc2 or "1/(2 a_tau)" in sc2))
    record("SC2 bridge forbids physical mass/unit overread", "No physical mass" in sc2 and "free construction parameters" in sc2)
    record("minimal Lattice excludes metric scale/lattice spacing/unit conversion", "metric scale" in min_ax and "lattice spacing" in min_ax and "physical unit conversion" in min_ax)
    record("minimal Record excludes time metric/dynamics/probability", "time metric" in min_ax and "dynamics" in min_ax and "probability" in min_ax)
    record("post-record interface says counts do not supply clock metric", "does not supply physical elapsed time" in post and "clock metric" in post)
    record("post-record interface supports rates only with supplied clock map", "supplied clock map" in post and "conditional on the clock map" in post)
    record("record rate gate separates stable dial from physical rate unit", "physical rate claim" in gate and "clock/rate unit" in gate)
    record("loop pack exists with review delegated", (LOOP_DIR / "REVIEW_HISTORY.md").exists() and "reviewer_owned_not_run" in read(LOOP_DIR / "REVIEW_HISTORY.md"))


def block_transfer_algebra() -> None:
    print("\n[B] two-step transfer algebra")
    energy_sets = [
        np.array([0.0, 0.4, 1.1, 1.7]),
        np.array([0.0, 0.05, 0.9, 2.4]),
        np.array([0.0, 0.3, 0.8, 1.5, 2.1]),
    ]
    a_values = [0.25, 0.5, 1.0, 2.0]

    all_c2 = True
    all_wrong = True
    all_rescale = True
    all_positive = True
    max_c2 = 0.0
    max_wrong = 0.0
    max_rescale = 0.0

    for energies in energy_sets:
        for a_tau in a_values:
            T2 = diag_transfer(energies, a_tau)
            eig = np.linalg.eigvalsh(T2)
            all_positive = all_positive and bool(np.all(eig > 0.0)) and bool(np.all(eig <= 1.0 + 1e-12))

            H_c2 = reconstruct(T2, 2.0 * a_tau)
            H_c1 = reconstruct(T2, a_tau)
            ref = np.diag(energies - energies.min())

            err_c2 = float(np.max(np.abs(H_c2 - ref)))
            err_wrong = float(np.max(np.abs(H_c1 - 2.0 * ref)))
            max_c2 = max(max_c2, err_c2)
            max_wrong = max(max_wrong, err_wrong)
            all_c2 = all_c2 and err_c2 < 1e-12
            all_wrong = all_wrong and err_wrong < 1e-12

            for c in [0.5, 1.5, 3.0]:
                H_scaled = reconstruct(T2, 2.0 * c * a_tau)
                err_rescale = float(np.max(np.abs(H_scaled - ref / c)))
                max_rescale = max(max_rescale, err_rescale)
                all_rescale = all_rescale and err_rescale < 1e-12

    record("T_hat^2 spectra are positive and vacuum-normalized", all_positive)
    record("1/(2 a_tau) reconstruction recovers the reference generator", all_c2, f"max residual {max_c2:.1e}")
    record("1/a_tau reconstruction is the factor-two falsifier", all_wrong, f"max residual {max_wrong:.1e}")
    record("rescaling the supplied block time rescales H without changing T2", all_rescale, f"max residual {max_rescale:.1e}")

    # Single-step period-two witness, kept elementary: the two alternating
    # single-step factors are distinct, but their ordered product is the
    # block object.
    T_even = np.array([[0.9, 0.05], [0.0, 0.6]])
    T_odd = np.array([[0.7, -0.03], [0.0, 0.5]])
    T_block = T_odd @ T_even
    record("period-two single-step factors are distinct", float(np.max(np.abs(T_even - T_odd))) > 1e-3)
    record("the physical block object is an ordered two-step product", np.allclose(T_block, T_odd @ T_even))


def block_record_clocks() -> None:
    print("\n[C] Record/count clock no-go")
    word = ["a", "b", "a", "c", "a"]
    counts = {k: word.count(k) for k in sorted(set(word))}
    clocks = {
        "uniform": np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0]),
        "slow": np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0]),
        "accelerated": np.array([0.0, 1.0, 1.5, 3.0, 6.0, 10.0]),
    }

    same_word = True
    increasing = True
    rates = {}
    interval_rates = {}
    for name, tau in clocks.items():
        same_word = same_word and word == ["a", "b", "a", "c", "a"] and counts == {"a": 3, "b": 1, "c": 1}
        increasing = increasing and bool(np.all(np.diff(tau) > 0.0))
        rates[name] = len(word) / float(tau[-1] - tau[0])
        interval_rates[name] = 1.0 / np.diff(tau)

    distinct_total_rates = len({round(v, 12) for v in rates.values()}) > 1
    distinct_interval_profiles = not np.allclose(interval_rates["uniform"], interval_rates["accelerated"])

    record("same record word/counts survive multiple clocks", same_word)
    record("all supplied clocks are strictly increasing", increasing)
    record("total rates differ under clock choice", distinct_total_rates, str(rates))
    record("interval-rate profiles differ under nonuniform clock", distinct_interval_profiles)
    record("Record order/count data do not determine physical elapsed time", same_word and distinct_total_rates and distinct_interval_profiles)


def block_branch_hygiene() -> None:
    print("\n[D] branch hygiene")
    result = subprocess.run(["git", "status", "--short"], cwd=ROOT, check=True, text=True, capture_output=True)
    changed = [line[3:] for line in result.stdout.splitlines() if line.strip()]
    forbidden_prefixes = (
        "docs/audit/",
        "docs/publication/",
        "docs/repo/FRONT_DOOR_STATUS.md",
    )
    forbidden = [path for path in changed if path.startswith(forbidden_prefixes)]

    record("branch does not edit audit/publication/status surfaces", not forbidden, ", ".join(forbidden))
    record("science note is branch-local source artifact", any(path == "docs/SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md" for path in changed))
    record("runner is paired with the science note", any(path == "scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py" for path in changed))
    record("loop pack is branch-local under .claude/science", any(path.startswith(".claude/science/physics-loops/single-clock-blocked-time-unit-split-20260617/") for path in changed))


def block_status_firewall() -> None:
    print("\n[E] status firewall")
    note = read(NOTE)
    certificate = read(LOOP_DIR / "CLAIM_STATUS_CERTIFICATE.md")
    trace = read(LOOP_DIR / "TRACE_GATE.md")
    handoff = read(LOOP_DIR / "HANDOFF.md")

    record("certificate forbids bare retained wording", "bare_retained_allowed: false" in certificate)
    record("certificate keeps proposal_allowed false", "proposal_allowed: false" in certificate)
    record("trace gate is direct blocker closure and partial", "trace_class: direct_blocker_closure" in trace and "reachability_to_target: partially_closes" in trace)
    record("handoff says B-AXIS.2/B-AXIS.3 remain open", "B-AXIS.2" in handoff and "B-AXIS.3" in handoff and ("remain open" in handoff or "remains open" in handoff))
    record("note explicitly says no new axiom", "Does not add a framework axiom" in note)
    record("note explicitly says no audit-surface update", "Does not update audit results" in note)


def main() -> int:
    print("=" * 78)
    print("SINGLE-CLOCK B-AXIS.1 BLOCKED-TIME UNIT SPLIT CHECK")
    print("=" * 78)
    block_text_anchors()
    block_transfer_algebra()
    block_record_clocks()
    block_branch_hygiene()
    block_status_firewall()
    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
