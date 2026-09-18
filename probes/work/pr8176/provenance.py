#!/usr/bin/env python3
"""J:provenance:PR8176 — theorem/result-up-front numbers vs PR #8176 runner-cache."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = (
    "origin/physics-loop/admissibility-induced-law-block32-minimal-marked-tree-"
    "family-constant-at-least-one-tree-route-floor-20260917"
)
CACHE = (
    "logs/runner-cache/admissibility_rule_six_axis_formation_threshold_"
    "minimal_marked_tree_family_constant_at_least_one_exact_certificates_"
    "and_the_tree_route_floor_2026_09_17.txt"
)
NOTE_DERIV = {
    # stated as exact one-variable calculus in T4.2, not a runner print
    "t=2/27 argmax of t(4/27-t)": "note T4.2: argmax of t(4/27-t) at t=2/27",
}

# Distinctive numbers in Result-up-front + T1–T4 (not section enumerations).
NUMBERS = [
    ("4165", "block 30 region restated"),
    ("2", "block 31 construction constant restated"),
    ("3/4", "c*(W1)"),
    ("4/11", "W2 cheap-tree ratio"),
    ("99/100", "c just below 1"),
    ("101/100", "c just above 1"),
    ("3/50", "Z_A min at c=99/100"),
    ("2/25", "Z_B min at c=99/100"),
    ("-1/10", "Z_A min at c=101/100"),
    ("42", "Z_A component ones"),
    ("46", "Z_A total ones"),
    ("60", "Z_B component ones"),
    ("69", "Z_B total ones"),
    ("6", "Z_A optimal E=|A|"),
    ("9", "Z_B optimal E=|A|"),
    ("8", "W1 optimal |A|"),
    ("7", "W2 tree E"),
    ("11", "W2 |A| / located strength restated"),
    ("17", "W3 |A|"),
    ("453", "stake (453,1,2)"),
    ("232", "stake (232,1,1)"),
    ("905", "stake (905,2,4)"),
    ("677", "stake (677,1,3)"),
    ("4/729", "floor max_t t(4/27-t)"),
    ("367", "floor crossing below"),
    ("368", "floor crossing above / p=368"),
    ("4/27", "recursion domain edge"),
    ("19", "executed checks"),
    ("8", "mutations (also W1 |A|)"),
    ("90", "single-seed brute-force batch"),
    ("51", "multi-seed batch"),
    ("10^4", "hill-climb realizations"),
    ("6×6×8", "largest climb window"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def alts_for(token: str) -> list[str]:
    out = [token, token.replace("×", "x"), token.replace("10^4", "10⁴")]
    if token == "10^4":
        out += ["10^4", "10⁴", "~10^4", "about 10^4"]
    if token == "6×6×8":
        out += ["6x6x8", "6×6×8"]
    return list(dict.fromkeys(out))


def find_line(blob: str, token: str) -> str | None:
    import re
    for alt in alts_for(token):
        pat = re.compile(r"(?<![0-9A-Fa-f])" + re.escape(alt) + r"(?![0-9A-Fa-f])")
        for line in blob.splitlines():
            if "sha256" in line.lower():
                continue
            if pat.search(line):
                return line.strip()
    return None


def main() -> None:
    cache = git_show(CACHE)
    note = git_show(
        "docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_THE_MINIMAL_MARKED_TREE_"
        "THE_COUNTED_FAMILYS_CONSTANT_IS_AT_LEAST_ONE_EXACT_CERTIFICATES_AND_THE_TREE_"
        "ROUTES_FLOOR_BOUNDED_THEOREM_NOTE_2026-09-17.md"
    )
    unsourced = 0
    for token, role in NUMBERS:
        hit_line = find_line(cache, token)
        note_line = find_line(note, token)
        if hit_line:
            src = f"cache: {hit_line[:140]}"
            status = "OK"
        elif token in NOTE_DERIV:
            src = NOTE_DERIV[token]
            status = "OK"
        elif note_line and ("Proof" in note_line or "exactly" in note_line or "Executed" in note_line):
            src = f"note: {note_line[:140]}"
            status = "OK"
        else:
            src = "NOT IN CACHE"
            status = "UNSOURCED"
            unsourced += 1
        print(f"{token} | {role} | {src} | {status}")
    n = len(NUMBERS)
    print(f"SUMMARY: {n} numbers, {unsourced} unsourced")
    if unsourced:
        print("HIT: unsourced numbers")


if __name__ == "__main__":
    main()
