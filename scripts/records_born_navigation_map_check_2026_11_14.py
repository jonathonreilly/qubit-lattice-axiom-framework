#!/usr/bin/env python3
"""Checks the statements that the records-born navigation map makes.

docs/RECORDS_BORN_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md is a navigation
map with no science of its own. What it does state is checkable: that each
"Carried notes" section quotes its carried note's current claim_scope verbatim
and names that note's own runner, that the map covers each carried note once,
that its logged table lists exactly the nine logged source PRs, that the counts
in its own claim_scope (14 source notes, five carried, nine logged) match those
sections, and that every repository link in the map resolves. This runner checks
those statements. Three controls alter the map (one quotation, one runner link,
one logged row) and each must be rejected.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60

ROOT = Path(__file__).resolve().parents[1]
MAP = "docs/RECORDS_BORN_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md"
AUDIT_INPUT_PATHS = (
    "docs/RECORDS_BORN_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md",
    "docs/RECORDS_NEVER_CONDITION_THE_ODDS_FORMATION_LAW_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md",
    "docs/RECORDS_THAT_NEVER_CONDITION_THE_ODDS_GIVE_NO_ZENO_FULL_FRINGES_AND_CHSH_2_SQRT_2_WHILE_BARE_TWO_TIME_RECORDS_NEED_A_POINTER_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/RECORDING_EVERY_SITE_INCLUDING_RISHONS_AND_EDGE_REGISTERS_CHANGES_NO_ODDS_LEVEL_PREDICTION_AND_NO_RECORD_OF_ONE_HALF_TICK_EMPTIES_A_SUPPORT_BOUNDED_THEOREM_NOTE_2026-10-22.md",
    "docs/HISTORY_ACTUALITY_REPRODUCES_THE_READABLE_BORN_ODDS_AND_WHICH_WAY_COMPLEMENTARITY_BUT_NEEDS_A_TICK_FORM_THE_CHIRAL_WEIGHTING_LACKS_BOUNDED_THEOREM_NOTE_2026-10-23.md",
)
CARRIED_PRS = {9873, 9893, 9930, 9995, 10054}
LOGGED_PRS = {9866, 9867, 9869, 9871, 9885, 9886, 9887, 9970, 9989}

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: object = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += not ok
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail != "" else ""))
    return ok


def frontmatter_field(text: str, field: str) -> str | None:
    """One frontmatter scalar; a quoted scalar may continue on indented lines (YAML folds them with spaces)."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    lines = m.group(1).split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(field + ":")]
    if len(starts) != 1:
        return None
    i = starts[0]
    raw = lines[i][len(field) + 1:].strip()
    if raw[:1] in "\"'" and not (len(raw) >= 2 and raw.endswith(raw[0]) and not raw.endswith("\\" + raw[0])):
        q = raw[0]
        for cont in lines[i + 1:]:
            raw += " " + cont.strip()
            if cont.rstrip().endswith(q) and not cont.rstrip().endswith("\\" + q):
                break
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        raw = raw[1:-1].replace('\\"', '"') if raw[0] == '"' else raw[1:-1].replace("''", "'")
    return " ".join(raw.split())


def part(text: str, heading: str) -> str:
    return text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]


def sections(text: str):
    """Yield (pr, heading, body) for each '### #' section of the 'Carried notes' part."""
    for chunk in re.split(r"^### ", part(text, "Carried notes"), flags=re.M)[1:]:
        head, _, body = chunk.partition("\n")
        m = re.match(r"#(\d+):", head.strip())
        yield (int(m.group(1)) if m else None), head.strip(), body


def quoted_scope(body: str) -> str | None:
    lines = [l[2:] if l.startswith("> ") else l[1:] for l in body.splitlines() if l.startswith(">")]
    return " ".join(" ".join(lines).split()) if lines else None


def linked(body: str, label: str, ext: str) -> str | None:
    m = re.search(rf"{label}: \[[^\]]+\]\(([^)]+\.{ext})\)", body)
    return m.group(1) if m else None


def compare(map_text: str):
    """Per carried section: (pr, note path, quote matches scope, runner link matches the note's runner field)."""
    out = []
    for pr, head, body in sections(map_text):
        rel = linked(body, "- Note", "md")
        run = linked(body, "Runner", "py")
        note = ROOT / "docs" / rel if rel else None
        text = note.read_text(encoding="utf-8") if note and note.is_file() else ""
        scope, runner = frontmatter_field(text, "claim_scope"), frontmatter_field(text, "runner")
        quote = quoted_scope(body)
        run_rel = str(Path("docs", run)).replace("docs/../", "") if run else None
        out.append((pr, rel, quote is not None and scope is not None and quote == scope,
                    runner is not None and run_rel == runner))
    return out


def logged_prs(map_text: str) -> list[int]:
    rows = [l for l in part(map_text, "Logged notes (historical reported results, unverified here)").splitlines()
            if re.match(r"\| #\d+ \|", l)]
    return [int(re.match(r"\| #(\d+) \|", r).group(1)) for r in rows]


def in_tree(rel: str) -> bool:
    """A repository path exists on disk, or in the checked-out commit (a sparse worktree omits files on disk)."""
    p = (ROOT / "docs" / rel).resolve()
    if p.exists():
        return True
    try:
        rp = p.relative_to(ROOT).as_posix()
    except ValueError:
        return False
    r = subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", f"HEAD:{rp}"], capture_output=True)
    return r.returncode == 0


def coverage(map_text: str):
    scope = frontmatter_field(map_text, "claim_scope") or ""
    m = re.search(r"of (\d+) source notes", scope)
    stated_total = int(m.group(1)) if m else None
    carried = [r[0] for r in compare(map_text)]
    logged = logged_prs(map_text)
    words = ("Five source notes are carried" in scope, "Nine source notes are logged" in scope)
    ok = (set(carried) == CARRIED_PRS and len(carried) == 5 and sorted(logged) == sorted(LOGGED_PRS)
          and len(logged) == 9 and not set(carried) & set(logged) and stated_total == len(carried) + len(logged)
          and all(words))
    return ok, carried, logged, stated_total


def main() -> int:
    text = (ROOT / MAP).read_text(encoding="utf-8")
    print("=" * 78)
    print("Navigation map check: records-born carried and logged notes")
    print("=" * 78)

    results = compare(text)
    notes = [r[1] for r in results]
    check("the map has 5 'Carried notes' sections, each naming one carried note and its source PR",
          len(results) == 5 and all(notes) and {r[0] for r in results} == CARRIED_PRS,
          f"{len(results)} sections, PRs {sorted(r[0] for r in results if r[0])}")
    check("no carried note appears in two sections", len(set(notes)) == len(notes))
    bad = [r[0] for r in results if not r[2]]
    check("each section quotes its carried note's current claim_scope verbatim", not bad,
          f"{len(results) - len(bad)} of {len(results)} match" + (f"; mismatched: {bad}" if bad else ""))
    badr = [r[0] for r in results if not r[3]]
    check("each section's Runner link is its carried note's own frontmatter runner", not badr,
          f"{len(results) - len(badr)} of {len(results)} match" + (f"; mismatched: {badr}" if badr else ""))
    ok, carried, logged, total = coverage(text)
    check("coverage: 5 carried and exactly the 9 logged source PRs, disjoint, = the 14 that the map's claim_scope states",
          ok, f"carried {sorted(carried)}; logged {sorted(logged)}; stated total {total}")

    links = re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text)
    local = [l for l in links if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", l)]
    missing = sorted({l for l in local if not in_tree(l)})
    check("every repository link in the map resolves (on disk or in the checked-out commit)", not missing and len(local) > 0,
          f"{len(local)} links" + (f"; missing: {missing[:3]}" if missing else ""))

    # controls: each alters the map and must be rejected by the check it targets
    first = next(sections(text))[2]
    words = (quoted_scope(first) or "").split()
    altered = text.replace(" ".join(words[-3:]), " ".join(words[-3:-1]), 1) if len(words) > 3 else text
    check("control rejects mutant 1: a quotation with its last word dropped", not all(r[2] for r in compare(altered)))
    runs = [linked(b, "Runner", "py") for _, _, b in sections(text)]
    swapped = text
    if len(runs) >= 2 and all(runs[:2]):
        swapped = text.replace(runs[0], "\0", 1).replace(runs[1], runs[0], 1).replace("\0", runs[1], 1)
    check("control rejects mutant 2: the runner links of two sections swapped", not all(r[3] for r in compare(swapped)))
    row = next((l for l in part(text, "Logged notes (historical reported results, unverified here)").splitlines()
                if l.startswith("| #9886 |")), None)
    dropped = text.replace(row + "\n", "", 1) if row else text
    check("control rejects mutant 3: one logged row removed", not coverage(dropped)[0])

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("Scope: the map's quotations, runner wiring, coverage and links. The carried notes' science is checked by "
          "their own runners; the logged notes and the campaign inputs named in the map are not checked here.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
