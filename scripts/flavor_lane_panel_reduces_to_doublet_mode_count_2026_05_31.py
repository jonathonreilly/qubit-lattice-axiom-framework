"""20-physicist panel + 4 meta-exercises (wf_9028152c): the channel-vs-lane question, resolved.

User invoked the panel ("ask the 20 physicists if we're stuck"), framed as find-the-escape. Results:

(D1) UNANIMOUS (24/24, no dissent): Q is a SINGLE observable Q=1/3+(2/3)r (the ratio channel);
     the three values {1/3, 2/3, 1} are three SETTINGS of r = three LANES, NOT three channels of one
     sector. The genuine orthogonal channels are {scale a (Q-invariant), ratio r (sets Q), phase
     delta (Q-orthogonal CP)} + topological 2/9. This CORRECTS the prior four-channel capstone, which
     mislabeled Q=1/3 and Q=1 as separate channels. (The user's lane reading is the correct one.)

(ASSIGNMENT) open_confirmed: no escape in this packet forces r=1/2 from framework baseline+emergent-spacetime.
     The panel synthesis organizes the surviving candidate structure:
  - STRONG convergence (10+ specialties) on "r=1/2 = self-dual fixed point of the singlet<->doublet
    swap r->1-r" -- but this is the GEOMETRY of r=1/2, NOT a forcing. The swap is a scalar relabeling:
    it changes the Casimir Tr(H^2) except at r=1/2, so it is NOT realized by any C_3-covariant
    operator involution. Escape KILLED (verified).
  - The CPT antilinear Theta=diag(1,1,-1) is a reflection WITHIN the doublet plane; it imposes no
    singlet:doublet ratio constraint -> does not force equal-block (matches retained no-go). Killed.
  - TRIPLE convergence (Adversarial-no-go + Math-Rigor meta + retained ledger) on the OBSTRUCTION:
    the genuine equipartition theorem PER QUADRATIC DOF gives r=1 (Q=1); r=1/2 needs the BLOCK /
    HOLOMORPHIC (det_C) measure that nothing on the retained surface fixes.

(BRANCH ALGEBRA) the runner verifies the two named finite branches of the det_C/det_R proposal:
  block-count (1,1) vs dimension-count (1,2)  ==  det_C vs det_R  ==  doublet is ONE complex mode vs
  TWO real modes. Verified: equal-per-BLOCK -> 3a^2=6|b|^2 -> r=1/2 -> Q=2/3 (det_C);
  equal-per-real-DIM -> 3a^2=3|b|^2 -> r=1 -> Q=1 (det_R). The stronger thesis that every admissible
  lane-selection route is exhausted by this metric choice remains open route support, not proved here.

(THE DECIDABLE NEXT CALC, honest survivor escape) the field-space metric on the doublet coefficient b,
  derived from the Quantum axiom's one-qubit coherent-state resolution-of-identity restricted to the hw=1 C_3 orbit:
  if HOLOMORPHIC |d b|^2 (one complex mode, phase=gauge) -> det_C -> r=1/2; if doubled-real
  (d Re b)^2+(d Im b)^2 (two modes) -> det_R -> r=1. This is framework-internal and novel (NOT the
  U(1)_b route the retained no-go closed; NOT the discrete-reflection route the panel killed).
"""
import json
from pathlib import Path

import numpy as np

import frontier_action_normalization as action_normalization
import frontier_koide_frobenius_isotype_split_uniqueness as frobenius_isotype


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs/FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31.md"
LEDGER = REPO_ROOT / "docs/audit/data/audit_ledger.json"
FROBENIUS_NOTE = REPO_ROOT / "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md"
ACTION_NOTE = REPO_ROOT / "docs/ACTION_NORMALIZATION_NOTE.md"
FROBENIUS_CACHE = REPO_ROOT / "logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt"
ACTION_CACHE = REPO_ROOT / "logs/runner-cache/frontier_action_normalization.txt"


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def ledger_row(claim_id):
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    return rows[claim_id]


def dependency_packet_checks():
    text = NOTE.read_text(encoding="utf-8")
    frobenius_text = FROBENIUS_NOTE.read_text(encoding="utf-8")
    action_text = ACTION_NOTE.read_text(encoding="utf-8")
    frobenius_cache = FROBENIUS_CACHE.read_text(encoding="utf-8")
    action_cache = ACTION_CACHE.read_text(encoding="utf-8")
    frobenius_row = ledger_row("koide_frobenius_isotype_split_uniqueness_note_2026-04-21")
    action_row = ledger_row("action_normalization_note")

    checks = []
    checks.append(check(
        "DEP1 target note links Frobenius isotype no-go note",
        "KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md" in text,
        "graph-visible dependency for the scalar/traceless isotype freedom no-go",
    ))
    checks.append(check(
        "DEP2 target note links action-normalization no-go note",
        "ACTION_NORMALIZATION_NOTE.md" in text,
        "graph-visible dependency for convention-free action-normalization failure",
    ))
    checks.append(check(
        "DEP3 target note links both dependency runner paths",
        "scripts/frontier_koide_frobenius_isotype_split_uniqueness.py" in text
        and "scripts/frontier_action_normalization.py" in text,
        "restricted packet can locate both source runners",
    ))
    checks.append(check(
        "DEP4 target note links both dependency caches",
        "logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt" in text
        and "logs/runner-cache/frontier_action_normalization.txt" in text,
        "restricted packet can locate both cached outputs",
    ))
    checks.append(check(
        "DEP5 Frobenius dependency is current retained_no_go in ledger",
        frobenius_row["audit_status"] == "audited_clean"
        and frobenius_row["effective_status"] == "retained_no_go",
        f"status={frobenius_row['audit_status']}/{frobenius_row['effective_status']}",
    ))
    checks.append(check(
        "DEP6 action-normalization dependency is current retained_no_go in ledger",
        action_row["audit_status"] == "audited_clean"
        and action_row["effective_status"] == "retained_no_go",
        f"status={action_row['audit_status']}/{action_row['effective_status']}",
    ))
    checks.append(check(
        "DEP7 Frobenius source/cached certificate is present",
        "Frobenius Isotype-Weight Freedom No-Go" in frobenius_text
        and "PASS=24 FAIL=0" in frobenius_cache,
        "Frobenius runner cache carries PASS=24 FAIL=0",
    ))
    checks.append(check(
        "DEP8 action-normalization source/cached certificate is present",
        "Convention-Free Selection No-Go" in action_text
        and "status: ok" in action_cache
        and "NARROWED: The coefficient c" in action_cache,
        "action-normalization cache is present and records the narrowed no-go",
    ))
    checks.append(check(
        "DEP9 dependency runner modules expose their checked primitives",
        hasattr(frobenius_isotype, "algebra_checks")
        and hasattr(action_normalization, "measure_rescaling_degeneracy"),
        "imports expose Frobenius algebra checks and action rescaling-degeneracy checks",
    ))
    return checks


def TrH2(a, babs):
    return 3 * a ** 2 + 6 * babs ** 2


def Q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def main():
    passed = []
    passed.extend(dependency_packet_checks())
    a = 1.0

    # D1: Q is scale-invariant single observable; lanes not channels (re-anchor)
    def Q_full(a_, babs, delta):
        lam = np.array([a_ + 2 * babs * np.cos(delta + 2 * np.pi * k / 3) for k in range(3)])
        return (lam ** 2).sum() / (lam.sum() ** 2)
    grid = [Q_full(A, np.sqrt(r) * A, d) for A in (1.0, 4.0) for r in (0.0, 0.5, 1.0) for d in (0.0, 0.7, 1.3)]
    # group by r: should be {1/3, 2/3, 1} independent of a and delta
    by_r = {r: {round(Q_full(A, np.sqrt(r) * A, d), 10) for A in (1.0, 4.0) for d in (0.0, 0.7, 1.3)} for r in (0.0, 0.5, 1.0)}
    passed.append(check(
        "D1 Q is a SINGLE observable = 1/3+(2/3)r, scale- and delta-invariant; {1/3,2/3,1} are r-LANES not channels",
        all(len(s) == 1 for s in by_r.values())
        and abs(min(by_r[0.0]) - 1/3) < 1e-9 and abs(min(by_r[0.5]) - 2/3) < 1e-9 and abs(min(by_r[1.0]) - 1) < 1e-9,
        f"r=0 -> {min(by_r[0.0]):.4f}, r=1/2 -> {min(by_r[0.5]):.4f}, r=1 -> {min(by_r[1.0]):.4f} (each unique over a,delta)"))

    # Escape [1] KILLED: r->1-r changes the Casimir except at r=1/2 -> not a covariant involution
    diffs = {r: abs(TrH2(a, np.sqrt(r) * a) - TrH2(a, np.sqrt(1 - r) * a)) for r in (0.2, 0.5, 0.8)}
    passed.append(check(
        "ESC1-KILLED r->1-r changes Tr(H^2) except at r=1/2 -> NOT a C_3-covariant operator involution (scalar relabeling)",
        diffs[0.2] > 1e-6 and diffs[0.8] > 1e-6 and diffs[0.5] < 1e-9,
        f"|Tr(H^2;r) - Tr(H^2;1-r)|: r=0.2->{diffs[0.2]:.3f}, r=0.5->{diffs[0.5]:.3f}, r=0.8->{diffs[0.8]:.3f}"))

    # (CPT-nonforcing — that an antilinear CPT/real-structure involution does NOT force equal-block —
    #  is the retained no-go koide_real_rep_block_count_permitted_not_forced; cited, not re-toy-modeled here.)

    # BRANCH ALGEBRA: block-count (det_C) -> r=1/2 ; dimension-count (det_R) -> r=1
    r_block = 3.0 / 6.0            # 3a^2 = 6|b|^2  (equal per BLOCK)
    r_dim = (6.0 / 2.0) / 3.0      # 3a^2/1 = 6|b|^2/2  (equal per real DIM)
    passed.append(check(
        "BRANCH det_C block-count (doublet=1 complex mode): 3a^2=6|b|^2 -> r=1/2 -> Q=2/3",
        abs(r_block - 0.5) < 1e-12 and abs(Q_of_r(r_block) - 2/3) < 1e-12,
        f"r_block={r_block:.3f} -> Q={Q_of_r(r_block):.4f}"))
    passed.append(check(
        "BRANCH det_R dimension-count (doublet=2 real modes): 3a^2=3|b|^2 -> r=1 -> Q=1",
        abs(r_dim - 1.0) < 1e-12 and abs(Q_of_r(r_dim) - 1.0) < 1e-12,
        f"r_dim={r_dim:.3f} -> Q={Q_of_r(r_dim):.4f}  => named decider candidate: doublet = 1 complex vs 2 real modes"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (20-physicist panel + 4 meta, wf_9028152c): D1 UNANIMOUS -- Q is one observable, {1/3,2/3,1}")
    print("are LANES not channels (corrects the four-channel capstone). Assignment open_confirmed: runner verifies")
    print("the two branch consequences of the det_C/det_R candidate = block-count(det_C, r=1/2) vs")
    print("dimension-count(det_R, r=1) = doublet as one complex vs two real modes. The stronger panel")
    print("exhaustiveness thesis remains open pending a restricted bridge theorem. The converged 'r=1/2 = self-dual")
    print("swap fixed point' escape is a scalar")
    print("relabeling (changes the Casimir; no covariant involution) -- KILLED, alongside the CPT-reflection route.")
    print("The honest decidable next calc: is the doublet-coefficient's emergent kinetic metric HOLOMORPHIC")
    print("(det_C -> r=1/2) or doubled-REAL (det_R -> r=1)? -- derived from the Quantum axiom's one-qubit coherent-state measure.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
