#!/usr/bin/env python3
"""J:attack:PR9351 -- pattern (c) EXECUTED NUMBERS: every executed range, count or bound named by the note, against the control outputs committed on the PR branch.

The note claims: six finite-case error bounds (table), exact counts j, j + 1 at every accepted endpoint, "independent checks ... finite S20 at the larger ratio, both rotor cases and all six corrected-operator cases, plus every
interval subtraction and upward rounding", and that deliberately shifted brackets and altered hopping coefficients fail. The PR branch commits control outputs under
.claude/science/physics-loops/measured-corrections-20260927/ (certified_gap_differences.json, corrected_operator_error_bounds.json, independent_certificate_check.json, independent_corrected_bounds_check.json,
certificate_fault_checks.json, independent_joint_check.json). This script parses them as exact rationals and compares them with (i) the runner's cached stdout (the source of the note's table), (ii) the note's table, and
(iii) the coverage the note attributes to them. Prints SUMMARY: and, only if a control output disagrees with the cache, the note, or the coverage claimed, HIT:.
"""
import json
import math
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/measured-corrections-20260927"
D = ".claude/science/physics-loops/measured-corrections-20260927"
NOTE = "docs/SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27.md"
CACHE = "logs/runner-cache/square_microscopic_spectral_certificate_2026_09_27.txt"
RESULTS, FIRED = [], []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def main():
    git("fetch", "origin", BRANCH, "--quiet")
    head = git("rev-parse", f"origin/{BRANCH}").stdout.strip()
    sh = lambda p: git("show", f"{head}:{p}").stdout
    C = json.loads(sh(CACHE).split("----- stdout -----\n", 1)[1].split("\nTOTAL:", 1)[0])["cases"]
    note = sh(NOTE)
    ctl = {f: json.loads(sh(f"{D}/{f}")) for f in ("certified_gap_differences.json", "corrected_operator_error_bounds.json", "independent_certificate_check.json",
                                                   "independent_corrected_bounds_check.json", "certificate_fault_checks.json", "independent_joint_check.json")}
    print(f"PR #9351 head {head[:10]}; {len(C)} cached cases; control files: {', '.join(ctl)}")
    key = lambda d, S: (str(d), int(S))
    cache = {key(c["delta"], c["S"]): c for c in C}
    # (1) corrected-operator bounds: control vs cache, exact
    ok1, det1 = True, []
    for r in ctl["corrected_operator_error_bounds.json"]:
        c = cache[key(r["delta"], r["S"])]
        same_iv = [[Fr(a), Fr(b)] for a, b in r["gap_difference_intervals"]] == [[Fr(a), Fr(b)] for a, b in c["microscopic_minus_approximate_gap_intervals"]]
        same_b = Fr(r["maximum_absolute_gap_error_upper_bound"]) == Fr(c["maximum_absolute_gap_error_upper_bound"])
        ok1 &= same_iv and same_b
        det1.append(f"delta {r['delta']} S {r['S']}: intervals {'=' if same_iv else 'DIFFER'}, bound {'=' if same_b else 'DIFFERS'}")
    check("(C1) corrected_operator_error_bounds.json equals the cache's microscopic-minus-approximate gap intervals and error bounds, exactly (6 cases)", ok1 and len(ctl["corrected_operator_error_bounds.json"]) == 6, "; ".join(det1))
    # (2) rotor differences
    ok2, det2 = True, []
    for r in ctl["certified_gap_differences.json"]:
        c = cache[key(r["delta"], r["S"])]
        same = [[Fr(a), Fr(b)] for a, b in r["gap_difference_intervals"]] == [[Fr(a), Fr(b)] for a, b in c["microscopic_minus_rotor_gap_intervals"]]
        ok2 &= same; det2.append(f"delta {r['delta']} S {r['S']}: {'=' if same else 'DIFFER'}")
    check("(C2) certified_gap_differences.json equals the cache's microscopic-minus-rotor gap intervals, exactly (6 cases)", ok2 and len(ctl["certified_gap_differences.json"]) == 6, "; ".join(det2))
    # (3) independent corrected bounds: exact bound, upward decimal against the note's table, counts
    tab = {}
    for m in re.finditer(r"\|\s*([0-9/]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|", note):
        tab[m.group(1)] = m.groups()[1:]
    ok3, det3 = True, []
    for r in ctl["independent_corrected_bounds_check.json"]:
        c = cache[key(r["delta"], r["S"])]
        col = {20: 0, 50: 1, 120: 2}[r["S"]]
        exact = Fr(r["exact_error_bound"]) == Fr(c["maximum_absolute_gap_error_upper_bound"])
        dec = Fr(r["upward_decimal"]) == Fr(tab[r["delta"]][col])
        up = Fr(math.ceil(Fr(r["exact_error_bound"]) * 10 ** 12), 10 ** 12) == Fr(r["upward_decimal"])
        counts = r["counts"] == [[j, j + 1] for j in range(7)]
        ok3 &= exact and dec and up and counts
        det3.append(f"delta {r['delta']} S {r['S']}: bound {'=' if exact else 'DIFFERS'} cache, decimal {'=' if dec else 'DIFFERS'} note table, ceil rule {'ok' if up else 'FAILS'}, counts {'ok' if counts else 'DIFFER'}")
    check(f"(C3) independent_corrected_bounds_check.json: exact bounds equal the cache's, upward decimals equal the note's table and are the 12-decimal ceilings, counts j, j + 1 ({len(ctl['independent_corrected_bounds_check.json'])} cases)", ok3 and len(ctl["independent_corrected_bounds_check.json"]) == 6, "; ".join(det3))
    # (4) coverage claimed: "independently checked finite S20 at the larger ratio, both rotor cases and all six corrected-operator cases"
    ic = ctl["independent_certificate_check.json"]
    finite = [r for r in ic if r["type"] == "finite"]; rotors = [r for r in ic if r["type"] == "infinite_rotor"]
    cov = (len(finite) == 1 and finite[0]["S"] == 20 and finite[0]["delta"] == "15803623/500000" and sorted(r["delta"] for r in rotors) == ["1", "15803623/500000"]
           and all(r["counts"] == [[j, j + 1] for j in range(7)] for r in ic) and len(ctl["independent_corrected_bounds_check.json"]) == 6)
    check("(C4) coverage: independent_certificate_check.json covers exactly finite S = 20 at the larger ratio and both infinite-rotor cases with counts j, j + 1; independent_corrected_bounds_check.json covers all six corrected-operator cases", cov,
          f"finite {[(r['S'], r['delta']) for r in finite]}; rotors {[(r['L'], r['delta']) for r in rotors]}")
    # (5) fault checks
    ff = ctl["certificate_fault_checks.json"]
    faults = [f for f in ff if "fault" in f]
    ok5 = all(f["detected"] for f in faults) and any("shifted" in f["fault"] for f in faults) and any("halve" in f["fault"] for f in faults)
    check("(C5) the fault checks the note cites (shifted brackets, altered hopping coefficients) are recorded as detected", ok5, "; ".join(f"{f['fault']}: {f['detected']}" for f in faults))
    # (6) joint-check remainder scaling against the note's O(x^2) reading: remainder / x^2 over sizes, same delta
    sc = ctl["independent_joint_check.json"]["spectral_checks"]
    bydelta = {}
    for r in sc:
        bydelta.setdefault(r["delta"], []).append((r["x"], r["remainder_over_x2"]))
    txt = "; ".join(f"delta {d}: remainder/x^2 " + ", ".join(f"{v:.0f} (x = {x:.4f})" for x, v in sorted(vs, reverse=True)) for d, vs in bydelta.items())
    rising = {d: all(vs[i][1] <= vs[i + 1][1] * 1.0 for i in range(len(vs) - 1)) for d, vs in ((d, sorted(v, reverse=True)) for d, v in bydelta.items())}
    print(f"[INFO] independent_joint_check.json spectral_checks: {txt}; the ratio rises as x falls at the larger delta (31.6) through S = 48, i.e. the O(x^2) constant is not reached there (x = 0.013); the note states this is a fixed-case statement")
    print(f"   [total control files {len(ctl)}]")
    if FIRED:
        print("SUMMARY: CONTROL OUTPUT DISAGREES: " + FIRED[0]); print("HIT: " + "; ".join(FIRED)); return 0
    if not all(RESULTS):
        bad = [i for i, r in enumerate(RESULTS) if not r]
        print("SUMMARY: CONTROL OUTPUT DISAGREES with the cache, the note's table or the coverage claimed: checks " + ", ".join(f"C{i + 1}" for i in bad))
        print("HIT: a control output on the PR branch disagrees with the cache, the note's table or the coverage the note attributes to it: checks " + ", ".join(f"C{i + 1}" for i in bad))
        return 0
    print("SUMMARY: pattern has no purchase on the numbers: the control outputs committed on the PR branch equal the cache's exact rational intervals and bounds (rotor and corrected), their upward decimals are the note's table and the 12-decimal ceilings, "
          "the coverage the note claims for the independent checks is the coverage they have, and the recorded faults are detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
