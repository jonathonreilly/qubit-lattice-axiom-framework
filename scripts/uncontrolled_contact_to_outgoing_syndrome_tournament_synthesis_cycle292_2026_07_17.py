#!/usr/bin/env python3
"""Cycle 292: cold synthesis of ordinary-contact action routes."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "UNCONTROLLED_CONTACT_TO_OUTGOING_SYNDROME_TOURNAMENT_SYNTHESIS_CYCLE292_NOTE_2026-07-17.md"
)
RUNNERS = {
    285: (
        "scripts/actual_contact_action_syndrome_tournament_cycle285_2026_07_17.py",
        "SUMMARY PASS 22 FAIL 0",
        "CYCLE285_ACTUAL_CONTACT_ACTION_SYNDROME_GREEN",
    ),
    289: (
        "scripts/uncontrolled_contact_collision_current_syndrome_cycle289_2026_07_17.py",
        "SUMMARY PASS 13 FAIL 0",
        "CYCLE289_UNCONTROLLED_CONTACT_COLLISION_CURRENT_GREEN",
    ),
    290: (
        "scripts/unconditional_two_cell_contact_interferometer_cycle290_2026_07_17.py",
        "SUMMARY: 13 passed, 0 failed",
        "",
    ),
    291: (
        "scripts/open_boundary_actual_contact_action_detector_cycle291_2026_07_17.py",
        "SUMMARY PASS 14 FAIL 0",
        "CYCLE291_OPEN_BOUNDARY_ACTUAL_ACTION_DETECTOR_GREEN",
    ),
}
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", chr(96), ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> str:
    if not NOTE.exists():
        check("the Cycle-292 note exists", False, NOTE)
        return ""
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "constitutional effect: none",
        "three independent fixed-number constructive routes",
        "e g_coarse = g_physical e",
        "cycle 251 exact bounded sectorwise physical operator/update compiler",
        "actual graph-exchange residual 2 sqrt(2)",
        "macro support 4l-1",
        "first-wrap wilson residual 2",
        "no route may be spliced",
        "route a — collision-current transducer",
        "route b — compact two-cell interferometer",
        "route c — open outgoing carrier",
        "updated six-wall ledger",
        "toe lane percentages after reconnoitering both bridge ends",
        "complete supplied-structure inventory",
        "full no-go discipline n1-n8",
        "optimal next campaign",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis note preserves its full contract", not missing, missing)
    return text


def cold_runs() -> None:
    rows = []
    failures = []
    for cycle, (relative, summary, result) in RUNNERS.items():
        run = subprocess.run(
            [sys.executable, str(ROOT / relative)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=420,
            check=False,
        )
        row = (
            cycle,
            run.returncode,
            summary in run.stdout,
            not result or result in run.stdout,
        )
        rows.append(row)
        if row[1] or not row[2] or not row[3]:
            failures.append((row, run.stdout[-2000:]))
    check(
        "Cycles 285 and 289-291 cold-run with exact green totals",
        not failures,
        {"rows": rows, "failures": failures},
    )


def route_contracts(text: str) -> None:
    residuals = (
        "0.637795123412256",
        "1.0573994819069698e-33",
        "6.260264453411745e-34",
        "2.4516244678865193e-35",
        "0.9612752029752994",
        "1.5972415263976283",
        "8.881784197001252e-16",
        "3.3306690738754696e-16",
        "0.03383632719698277",
        "5.004680467665246e-34",
        "0.3616154319649619",
        "0.7986207631988143",
        "0.9612752029752999",
        "52+3r m2",
        "r=47, h=46, 193 m2",
    )
    check(
        "all route values and residuals are explicit",
        all(item in text for item in residuals),
        residuals,
    )
    supports = ("53 m2", "36 m2", "54 m2", "6 m2 per step")
    check(
        "all bounded support and propagation costs are explicit",
        all(item in text for item in supports),
        supports,
    )
    controls = (
        "fixed total particle number",
        "equal q-active-cell count",
        "ordinary marker-independent w_g action",
        "one-particle mass fixture",
        "zero local-check/wilson leakage",
        "held l=6",
        "all 24 proper-cubic frames times all 27",
        "occupancy-only trace dephases",
        "exact inverse and bounded backward retarget",
        "split false closes",
    )
    check(
        "mass, leakage, held-size, covariance, and fault controls are retained",
        all(item in text for item in controls),
        controls,
    )


def ledger_contracts(text: str) -> None:
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    check(
        "the six-wall ledger is complete",
        all(item in text for item in walls),
        walls,
    )
    scores = (
        "operational quantum / records | 53% | 24% | 76% | 2.7/5",
        "causal time / clock | 33% | 17% | 60% | 1.7/5",
        "inertia / matter | 62% | 27% | 82% | 3.1/5",
        "gravity / source / resource | 34% | 12% | 58% | 1.7/5",
        "born / probability / realized history | 33% | 14% | 79% | 1.7/5",
    )
    check(
        "all five lanes have exact integrated, strict, conditional, and maturity scores",
        all(item in text for item in scores),
        scores,
    )
    ends = (
        "axiomatic three-dimensional lattice is spatial",
        "conditional resource/retarded/static response spine",
        "conditional trace/frequency/process",
        "selected full matter law",
        "lawful record typing/protection",
    )
    check(
        "every scored bridge identifies its far end",
        all(item in text for item in ends),
        ends,
    )


def inventory_contracts(text: str) -> None:
    supplies = (
        "fixed-number coherent branch preparation",
        "collision-swap or code-to-carrier isometry",
        "open boundary, fresh targets",
        "occurrence, actual-member selection",
        "clock event equivalence",
        "born/repeated-history numerical law",
        "additive source/energy/stress",
        "one common homogeneous nearest-neighbor law",
    )
    check(
        "the supplied-structure inventory is cross-lane complete",
        all(item in text for item in supplies),
        supplies,
    )
    firewalls = (
        "no supplied carrier is renamed a record",
        "no phase is renamed energy",
        "no gate generator is renamed a rate",
        "no schedule or rail coordinate is renamed time",
        "resource count is not a source law",
    )
    check(
        "Record, energy, rate, time, and source semantics remain separate",
        all(item in text for item in firewalls),
        firewalls,
    )


def discipline_contracts(text: str) -> None:
    sections = tuple(f"n{number} —" for number in range(1, 9))
    check(
        "all N1-N8 sections are present",
        all(item in text for item in sections),
        sections,
    )
    check(
        "N1 has twelve literal synthesis attempts and no inherited exclusion marker",
        text.count("attempted") >= 12 and "ruled out by prior" not in text,
        {"attempted_count": text.count("attempted")},
    )
    pairs = (
        "p,h", "p,o", "p,k", "p,t", "p,b", "p,s",
        "h,o", "h,k", "h,t", "h,b", "h,s",
        "o,k", "o,t", "o,b", "o,s",
        "k,t", "k,b", "k,s", "t,b", "t,s", "b,s",
    )
    check(
        "N2 has all 21 bidirectional collapsed-wall pairs",
        all(f"| {pair} | no | no | yes |" in text for pair in pairs),
        {"pair_count": len(pairs)},
    )
    hidden = (
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard qft",
        "registered",
        "canonical",
    )
    check(
        "N3 classifies the full required phrase scan",
        all(item in text for item in hidden),
        hidden,
    )
    check(
        "N4 drops both nonmatching witnesses",
        "cycle 276 | common prepared full-fock physical compiler remains open | action-detector closure | no" in text
        and "cycle 270 | far-end lane reconnaissance | action-detector closure | no" in text,
        "Cycle 276 and 270 are not detector witnesses",
    )
    resolutions = ("per-element", "per-site", "per-mode", "per-block", "lattice-wide")
    check(
        "N5 has five resolutions and explicit unknown scopes",
        all(item in text for item in resolutions)
        and text.count("unknown / not claimed") >= 12,
        {"unknown_count": text.count("unknown / not claimed")},
    )
    closing = (
        "live constructive retirement paths",
        "strongest hostile steelman",
        "cross-cycle echo",
        "n1-n8 status: pass",
        "n1-n8 status: fail",
    )
    check(
        "N6-N8 and both scoped gate verdicts are explicit",
        all(item in text for item in closing),
        closing,
    )


def scope_contracts(text: str) -> None:
    scope = (
        "scoped to the routes, controls, sizes, and code surfaces cold-run here",
        "unreviewed encodings, homogeneous apparatus laws, state preparations",
        "no route-independent failure appears",
        "there is no evidence-based axiom pressure",
        "broad no-go fails n1",
        "minimum-content theorem, or evidence-based axiom-pressure claim",
    )
    check(
        "obstruction and axiom-pressure language is evidence scoped",
        all(item in text for item in scope),
        scope,
    )
    check(
        "unused bounded prior art is not centered",
        "thirring" not in text,
        "Thirring absent",
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    text = note_contract()
    cold_runs()
    route_contracts(text)
    ledger_contracts(text)
    inventory_contracts(text)
    discipline_contracts(text)
    scope_contracts(text)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE292_UNCONTROLLED_CONTACT_TO_OUTGOING_SYNDROME_SYNTHESIS_GREEN"
        if FAIL == 0
        else "CYCLE292_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
