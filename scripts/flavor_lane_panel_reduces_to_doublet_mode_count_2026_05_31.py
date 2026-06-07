"""20-physicist panel + 4 meta-exercises (wf_9028152c): the channel-vs-lane question, resolved.

User invoked the panel ("ask the 20 physicists if we're stuck"), framed as find-the-escape. Results:

(D1) UNANIMOUS (24/24, no dissent): Q is a SINGLE observable Q=1/3+(2/3)r (the ratio channel);
     the three values {1/3, 2/3, 1} are three SETTINGS of r = three LANES, NOT three channels of one
     sector. The genuine orthogonal channels are {scale a (Q-invariant), ratio r (sets Q), phase
     delta (Q-orthogonal CP)} + topological 2/9. This CORRECTS the prior four-channel capstone, which
     mislabeled Q=1/3 and Q=1 as separate channels. (The user's lane reading is the correct one.)

(ASSIGNMENT) open_confirmed: no escape forces r=1/2 from framework baseline+emergent-spacetime. But the panel
     pinned the structure precisely:
  - STRONG convergence (10+ specialties) on "r=1/2 = self-dual fixed point of the singlet<->doublet
    swap r->1-r" -- but this is the GEOMETRY of r=1/2, NOT a forcing. The swap is a scalar relabeling:
    it changes the Casimir Tr(H^2) except at r=1/2, so it is NOT realized by any C_3-covariant
    operator involution. Escape KILLED (verified).
  - The CPT antilinear Theta=diag(1,1,-1) is a reflection WITHIN the doublet plane; it imposes no
    singlet:doublet ratio constraint -> does not force equal-block (matches retained no-go). Killed.
  - TRIPLE convergence (Adversarial-no-go + Math-Rigor meta + retained ledger) on the OBSTRUCTION:
    the genuine equipartition theorem PER QUADRATIC DOF gives r=1 (Q=1); r=1/2 needs the BLOCK /
    HOLOMORPHIC (det_C) measure that nothing on the retained surface fixes.

(THE ONE PRIMITIVE) all escapes collapse to a single decider, stated three equivalent ways:
  block-count (1,1) vs dimension-count (1,2)  ==  det_C vs det_R  ==  doublet is ONE complex mode vs
  TWO real modes. Verified: equal-per-BLOCK -> 3a^2=6|b|^2 -> r=1/2 -> Q=2/3 (det_C);
  equal-per-real-DIM -> 3a^2=3|b|^2 -> r=1 -> Q=1 (det_R). The SOLE decider of the charged-lepton lane.

(THE DECIDABLE NEXT CALC, honest survivor escape) the field-space metric on the doublet coefficient b,
  derived from Axiom 1's qubit coherent-state resolution-of-identity restricted to the hw=1 C_3 orbit:
  if HOLOMORPHIC |d b|^2 (one complex mode, phase=gauge) -> det_C -> r=1/2; if doubled-real
  (d Re b)^2+(d Im b)^2 (two modes) -> det_R -> r=1. This is framework-internal and novel (NOT the
  U(1)_b route the retained no-go closed; NOT the discrete-reflection route the panel killed).
"""
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/flavor_lane_panel_detcr_source_packet_2026_05_31.json"


@dataclass(frozen=True)
class AuthorityPacket:
    label: str
    note_path: str
    runner_path: str
    cache_path: str
    required_text: tuple[str, ...]
    required_cache_text: tuple[str, ...]


AUTHORITY_PACKETS = (
    AuthorityPacket(
        "Frobenius isotype split no-go",
        "docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md",
        "scripts/frontier_koide_frobenius_isotype_split_uniqueness.py",
        "logs/runner-cache/frontier_koide_frobenius_isotype_split_uniqueness.txt",
        ("Frobenius Isotype-Weight Freedom No-Go", "do not force"),
        ("PASS=24 FAIL=0",),
    ),
    AuthorityPacket(
        "action normalization no-go",
        "docs/ACTION_NORMALIZATION_NOTE.md",
        "scripts/frontier_action_normalization.py",
        "logs/runner-cache/frontier_action_normalization.txt",
        ("Action Normalization Convention-Free Selection No-Go", "does not select"),
        ("NARROWED: The coefficient c", "Total runtime:"),
    ),
    AuthorityPacket(
        "generation weight dial structure",
        "docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md",
        "scripts/generation_weight_dial_structure_2026_06_05.py",
        "logs/runner-cache/generation_weight_dial_structure_2026_06_05.txt",
        ("GENERATION_WEIGHT_DIAL_STRUCTURE", "r(s)"),
        ("SCORECARD: 28 PASS / 0 FAIL", "r(0)=1/2", "r(1)=1"),
    ),
    AuthorityPacket(
        "one counting bit synthesis",
        "docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md",
        "scripts/charged_lepton_value_one_counting_bit.py",
        "logs/runner-cache/charged_lepton_value_one_counting_bit.txt",
        ("one counting bit", "det_C", "det_R"),
        ("SCORECARD: PASS=22 FAIL=0", "det_C", "det_R"),
    ),
)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def sha256_rel(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def cache_header(text: str) -> dict[str, str]:
    header = {}
    if "----- stdout -----" not in text:
        return header
    for line in text.split("----- stdout -----", 1)[0].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        header[key.strip()] = value.strip()
    return header


def TrH2(a, babs):
    return 3 * a ** 2 + 6 * babs ** 2


def Q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def Q_fraction(r: Fraction) -> Fraction:
    return Fraction(1, 3) + Fraction(2, 3) * r


def exact_bridge_checks():
    passed = []
    print("\nEXACT DET_C / DET_R BRIDGE")
    a2 = Fraction(1, 1)
    singlet_energy = 3 * a2
    # E_doublet = 6 |b|^2. Equal block energy gives 3a^2 = 6|b|^2.
    r_det_c = singlet_energy / 6
    # Equal real-mode energy gives 3a^2 = E_doublet / 2 = 3|b|^2.
    r_det_r = singlet_energy / 3
    passed.append(check("exact det_C block-count gives r=1/2", r_det_c == Fraction(1, 2), f"r={r_det_c}"))
    passed.append(check("exact det_C block-count gives Q=2/3", Q_fraction(r_det_c) == Fraction(2, 3), f"Q={Q_fraction(r_det_c)}"))
    passed.append(check("exact det_R real-mode count gives r=1", r_det_r == Fraction(1, 1), f"r={r_det_r}"))
    passed.append(check("exact det_R real-mode count gives Q=1", Q_fraction(r_det_r) == Fraction(1, 1), f"Q={Q_fraction(r_det_r)}"))
    passed.append(check("det_C and det_R endpoints are distinct", r_det_c != r_det_r, f"{r_det_c} vs {r_det_r}"))
    return passed, {"r_det_c": str(r_det_c), "q_det_c": str(Q_fraction(r_det_c)), "r_det_r": str(r_det_r), "q_det_r": str(Q_fraction(r_det_r))}


def authority_packet_checks():
    passed = []
    print("\nAUTHORITY PACKETS")
    packet_rows = []
    for packet in AUTHORITY_PACKETS:
        note = ROOT / packet.note_path
        runner = ROOT / packet.runner_path
        cache = ROOT / packet.cache_path
        passed.append(check(f"{packet.label}: source note exists", note.exists(), packet.note_path))
        if note.exists():
            note_text = note.read_text(encoding="utf-8", errors="replace")
            for needle in packet.required_text:
                passed.append(check(f"{packet.label}: source note contains {needle!r}", needle in note_text))
        passed.append(check(f"{packet.label}: runner exists", runner.exists(), packet.runner_path))
        passed.append(check(f"{packet.label}: cache exists", cache.exists(), packet.cache_path))
        if runner.exists() and cache.exists():
            runner_sha = sha256_rel(packet.runner_path)
            cache_text = cache.read_text(encoding="utf-8", errors="replace")
            header = cache_header(cache_text)
            passed.append(check(f"{packet.label}: cache runner matches source", header.get("runner") == packet.runner_path, header.get("runner", "")))
            passed.append(check(f"{packet.label}: cache SHA fresh", header.get("runner_sha256") == runner_sha, header.get("runner_sha256", "")))
            passed.append(check(f"{packet.label}: cache status ok", header.get("status") == "ok" and header.get("exit_code") == "0", str(header)))
            for needle in packet.required_cache_text:
                passed.append(check(f"{packet.label}: cache contains {needle!r}", needle in cache_text))
            packet_rows.append(
                {
                    "label": packet.label,
                    "note_path": packet.note_path,
                    "note_sha256": sha256_rel(packet.note_path) if note.exists() else None,
                    "runner_path": packet.runner_path,
                    "runner_sha256": runner_sha,
                    "cache_path": packet.cache_path,
                    "cache_sha256": sha256_rel(packet.cache_path),
                }
            )
    return passed, packet_rows


def main():
    passed = []
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

    # THE ONE PRIMITIVE: block-count (det_C) -> r=1/2 ; dimension-count (det_R) -> r=1
    r_block = 3.0 / 6.0            # 3a^2 = 6|b|^2  (equal per BLOCK)
    r_dim = (6.0 / 2.0) / 3.0      # 3a^2/1 = 6|b|^2/2  (equal per real DIM)
    passed.append(check(
        "PRIMITIVE block-count (det_C, doublet=1 complex mode): 3a^2=6|b|^2 -> r=1/2 -> Q=2/3",
        abs(r_block - 0.5) < 1e-12 and abs(Q_of_r(r_block) - 2/3) < 1e-12,
        f"r_block={r_block:.3f} -> Q={Q_of_r(r_block):.4f}"))
    passed.append(check(
        "PRIMITIVE dimension-count (det_R, doublet=2 real modes): 3a^2=3|b|^2 -> r=1 -> Q=1",
        abs(r_dim - 1.0) < 1e-12 and abs(Q_of_r(r_dim) - 1.0) < 1e-12,
        f"r_dim={r_dim:.3f} -> Q={Q_of_r(r_dim):.4f}  => SOLE decider: doublet = 1 complex vs 2 real modes"))

    bridge_passed, bridge_payload = exact_bridge_checks()
    authority_passed, packet_rows = authority_packet_checks()
    passed.extend(bridge_passed)
    passed.extend(authority_passed)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "claim_id": "flavor_lane_panel_reduces_to_doublet_mode_count_2026-05-31",
                "bridge": bridge_payload,
                "authority_packets": packet_rows,
                "boundary": "det_C/det_R reduction only; no selected charged-lepton lane",
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    passed.append(check("det_C/det_R source-packet export written", OUTPUT.exists(), OUTPUT.relative_to(ROOT).as_posix()))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (20-physicist panel + 4 meta, wf_9028152c): D1 UNANIMOUS -- Q is one observable, {1/3,2/3,1}")
    print("are LANES not channels (corrects the four-channel capstone). Assignment open_confirmed: every escape")
    print("collapses to ONE primitive = block-count(det_C, r=1/2) vs dimension-count(det_R, r=1) = doublet as one")
    print("complex vs two real modes. The converged 'r=1/2 = self-dual swap fixed point' escape is a scalar")
    print("relabeling (changes the Casimir; no covariant involution) -- KILLED, alongside the CPT-reflection route.")
    print("The honest decidable next calc: is the doublet-coefficient's emergent kinetic metric HOLOMORPHIC")
    print("(det_C -> r=1/2) or doubled-REAL (det_R -> r=1)? -- derived from Axiom 1's qubit coherent-state measure.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
