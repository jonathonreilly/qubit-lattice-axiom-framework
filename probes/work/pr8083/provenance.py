#!/usr/bin/env python3
"""J:provenance:PR8083 — theorem numbers vs PR branch runner / note / authenticated packet."""
from __future__ import annotations

import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "origin/codex/native-quartic-ward-20260910"
RUNNER = "scripts/native_quartic_ward_2026_09_10.py"
NOTE = "docs/NATIVE_QUARTIC_WARD_NOTE_2026-09-10.md"
CHECKER = (
    ".claude/science/physics-loops/native-quartic-ward-20260910/"
    "source_draft/check.py"
)
RESULT = (
    ".claude/science/physics-loops/native-quartic-ward-20260910/"
    "source_draft/packet/RESULT.json"
)
ACCEPT = (
    ".claude/science/physics-loops/native-quartic-ward-20260910/"
    "source_draft/packet/ROOT_ACCEPTANCE.json"
)
CACHE = "logs/runner-cache/native_quartic_ward_2026_09_10.txt"

# Numbers in the theorem statements / result-up-front of the note.
NUMBERS = [
    ("1.3838", "residual E upper (4 dp)"),
    ("66.6052", "residual F upper (4 dp)"),
    ("-465.2922", "residual alpha lo (4 dp)"),
    ("609.3813", "residual alpha hi (4 dp)"),
    ("1.1428", "variational E upper (4 dp)"),
    ("66.7061", "variational F upper (4 dp)"),
    ("-468.7459", "variational alpha lo (4 dp)"),
    ("629.7689", "variational alpha hi (4 dp)"),
    ("1/4", "δ in D≥δI and quartic envelope"),
    ("15", "unordered pairs with repetition from {1,2,4,8,16}"),
    ("60", "fixed quartic candidates (15×2 modes×2 P/O)"),
    ("√8", "F_A bound √8 E_A"),
    ("12", "P channels combined by sums of squares"),
    ("3", "O channels combined by sums of squares"),
    ("4√15", "X in posterior enclosure"),
    ("32√30", "V in posterior enclosure"),
    ("6", "posterior prefactor ℰ=6{…}"),
    ("8", "alpha interval denominator /8"),
    ("255", "original degree20 event chronology"),
    ("97", "new output events"),
    ("8 files", "output hash membership"),
    ("1.72", "external seconds"),
    ("54951936", "external RSS bytes"),
    ("101793792", "sampled tree peak bytes"),
    ("30", "time cap seconds"),
    ("384", "MiB RSS cap"),
    ("6 mutants", "coherent metadata/interval/identity mutants"),
]


def git_show(path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{BRANCH}:{path}"], cwd=ROOT, text=True, stderr=subprocess.STDOUT
    )


def git_exists(path: str) -> bool:
    r = subprocess.run(
        ["git", "cat-file", "-e", f"{BRANCH}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return r.returncode == 0


def alts_for(token: str) -> list[str]:
    # Context-rich forms first so short integers are not matched inside other numbers.
    spelled = {
        "15": ["fifteen unordered", "fifteen valid"],
        "60": ["sixty fixed", "('majorant_candidates',60)"],
        "12": ["twelve P"],
        "3": ["three O channels"],
        "6": [r"\mathcal E=6", "ℰ=6"],
        "8": [r"/8]", r")/8"],
        "8 files": ["eight files", "eight outputs"],
        "6 mutants": ["Six coherent", "semantic_mutants"],
        "1/4": [r"\delta=1/4", "δ=1/4", "F(1,4)", "d=F(1,4)"],
        "√8": [r"\sqrt8", r"\sqrt{8}"],
        "4√15": [r"4\sqrt{15}", r"4\sqrt15"],
        "32√30": [r"32\sqrt{30}", r"32\sqrt30"],
        "54951936": ["54,951,936", "54951936"],
        "101793792": ["101,793,792", "101793792"],
        "384": ["384 MiB", "384*1048576"],
        "97": ["97 events", "('events',97)"],
        "30": ["within 30 seconds", "external_seconds'],30"],
        "255": ["255-event"],
        "1.72": ["1.72 seconds", "1.72"],
    }
    if token in spelled:
        return list(dict.fromkeys(spelled[token]))
    return [token]


def is_digit_soup(line: str) -> bool:
    return len(line) > 200 and sum(ch.isdigit() for ch in line) > 80


def find_line(blob: str, token: str) -> str | None:
    numeric = token.lstrip("-").replace(".", "").replace("/", "").isdigit() and len(token) <= 4
    for alt in alts_for(token):
        if numeric and alt == token:
            pat = re.compile(r"(?<![0-9])" + re.escape(alt) + r"(?![0-9])")
        else:
            pat = re.compile(re.escape(alt))
        for line in blob.splitlines():
            if "sha256" in line.lower() or is_digit_soup(line):
                continue
            if pat.search(line):
                return line.strip()
    return None


def round4(q: Fraction) -> str:
    return format(float(q), ".4f")


def main() -> None:
    runner = git_show(RUNNER)
    note = git_show(NOTE)
    checker = git_show(CHECKER)
    result_text = git_show(RESULT)
    accept_text = git_show(ACCEPT)
    blobs = [
        ("note", note),
        ("runner", runner),
        ("checker", checker),
        ("packet/ROOT_ACCEPTANCE", accept_text),
    ]
    cache_present = git_exists(CACHE)
    unsourced = 0
    hits: list[str] = []

    for token, role in NUMBERS:
        src = None
        for name, blob in blobs:
            hit_line = find_line(blob, token)
            if hit_line:
                src = f"{name}: {hit_line[:140]}"
                break
        if src:
            status = "OK"
        else:
            src = "NOT IN RUNNER, CHECKER, PACKET, OR NOTE LINE"
            status = "UNSOURCED"
            unsourced += 1
            hits.append(f"{token} ({role})")
        print(f"{token} | {role} | {src} | {status}")

    r = json.loads(result_text)
    a = json.loads(accept_text)
    table = [
        ("1.3838", r["rows"][0]["E_upper"]),
        ("66.6052", r["rows"][0]["F_upper"]),
        ("-465.2922", r["rows"][0]["new_alpha"][0]),
        ("609.3813", r["rows"][0]["new_alpha"][1]),
        ("1.1428", r["rows"][1]["E_upper"]),
        ("66.7061", r["rows"][1]["F_upper"]),
        ("-468.7459", r["rows"][1]["new_alpha"][0]),
        ("629.7689", r["rows"][1]["new_alpha"][1]),
    ]
    mismatch = 0
    for shown, exact in table:
        got = round4(Fraction(exact))
        if got != shown:
            mismatch += 1
            hits.append(f"table {shown} is float4 {got} from packet")
            print(f"TABLE | {shown} vs packet float4 {got} | MISMATCH")
        else:
            print(f"TABLE | {shown} equals packet float4 | OK")

    if r.get("events") != 97 or r.get("majorant_candidates") != 60:
        mismatch += 1
        hits.append("RESULT census 97/60 mismatch")
        print("CENSUS | RESULT events/candidates | MISMATCH")
    else:
        print("CENSUS | events=97 majorant_candidates=60 | OK")
    if (
        a.get("external_seconds") != 1.72
        or a.get("external_rss_bytes") != 54951936
        or a.get("sampled_whole_tree_peak") != 101793792
    ):
        mismatch += 1
        hits.append("acceptance resource fields mismatch note")
        print("RESOURCES | ROOT_ACCEPTANCE vs note 1.72/54951936/101793792 | MISMATCH")
    else:
        print("RESOURCES | 1.72s 54951936 RSS 101793792 peak | OK")
    names = set(a.get("output_hashes", {}).keys())
    if len(names) != 8:
        mismatch += 1
        hits.append(f"output_hashes count {len(names)} != 8")
        print(f"FILES | output_hashes={len(names)} | MISMATCH")
    else:
        print("FILES | eight output hashes | OK")

    pairs = [(t, u) for i, t in enumerate((1, 2, 4, 8, 16)) for u in (1, 2, 4, 8, 16)[i:]]
    if len(pairs) != 15 or 15 * 2 * 2 != 60:
        mismatch += 1
        hits.append("15-pair/60-candidate identity failed")
        print("IDENTITY | 15 pairs with repetition, 60 candidates | MISMATCH")
    else:
        print("IDENTITY | 15 unordered pairs with repetition; 15×2×2=60 | OK")

    print(
        f"SUMMARY: {len(NUMBERS)} theorem numbers, {unsourced} unsourced, "
        f"{mismatch} packet mismatches; runner-cache present={cache_present}"
    )
    if unsourced or mismatch:
        print("HIT: " + "; ".join(hits))


if __name__ == "__main__":
    main()
