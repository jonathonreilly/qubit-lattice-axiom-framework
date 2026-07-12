#!/usr/bin/env python3
"""Axiom-reconciliation rescan (2026-07-12).

Rebuilds the campaign index of surfaces that still carry pre-reset axiom
naming or superseded Record wording, against the current tree and the
current audit ledger. The 2026-07-03 index (2,278-row session artifact)
was never banked; this script makes the index regenerable.

Scope: docs/**/*.md and scripts/*.py at the checked-out commit. Detection
is textual needle matching only; classification into re-key / content-flip
/ reopened-wall / historical is triage work recorded in the index note,
not here.

Output: deterministic summary on stdout plus a TSV at
logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv
(one row per hit file: path, needle categories, hit counts, ledger
claim_id, audit_status, effective_status, claim_type, lane bucket).
"""

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "docs" / "audit" / "data" / "audit_ledger.json"
OUT_TSV = REPO / "logs" / "runner-cache" / "axiom_reconciliation_rescan_2026_07_12.tsv"

# Files whose old-wording quotes are intentional historical record or the
# superseded memos themselves. These are listed in the summary but carry
# bucket=excluded-historical instead of a lane.
EXCLUDED_HISTORICAL = (
    "docs/MINIMAL_AXIOMS_2026-04-11.md",
    "docs/MINIMAL_AXIOMS_2026-05-03.md",
    "docs/MINIMAL_AXIOMS_2026-05-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-05.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/AXIOM_MINIMALITY_POLICY.md",
    # campaign's own surfaces quote the needles as documentation
    "docs/AXIOM_RECONCILIATION_INDEX_2026-07-12.md",
)

# Needle categories. Each entry: (category, severity, compiled regex).
# severity "hard" = wording that cannot appear in a post-reset-consistent
# surface outside a marked historical quote; "soft" = naming that is often
# legitimate historical context and needs triage.
# Multi-word needles use \s+ between words: prose in this repo is hard-wrapped,
# so a literal-space needle misses any phrase broken across a line (found the
# hard way: the objectivity note's firewall paragraph, 2026-07-12).
def _p(words: str) -> str:
    return words.replace(" ", r"\s+")


NEEDLES = [
    # -- legacy axiom-set naming ------------------------------------------
    ("three-framework-axioms", "hard",
     re.compile(_p(r"[Tt]hree [Ff]ramework [Aa]xioms"))),
    ("lattice-quantum-record", "hard",
     re.compile(r"Lattice\s*[,/]\s*Quantum\s*[,/]\s*(?:and\s+)?Record")),
    ("quantum-axiom-name", "soft",
     re.compile(_p(r"Quantum axiom|axiom named Quantum"))),
    ("three-axiom-baseline", "soft",
     re.compile(r"\bthree[-\s]+axiom\b|\b3-axiom\b")),
    ("superseded-memo-cite", "soft",
     re.compile(r"MINIMAL_AXIOMS_2026-0(?:4-11|5-03|5-20|6-04|6-05)")),
    # -- superseded Record wording ----------------------------------------
    ("durable-registration", "hard",
     re.compile(_p(r"durable (?:registration of the realized outcome|"
                   r"realized-outcome registration)"))),
    ("kcpt-orbit-realized", "hard",
     re.compile(_p(r"CPT orbit of the realized"))),
    ("central-sector-readout-context", "hard",
     re.compile(_p(r"readout context with a finite central-sector "
                   r"decomposition"))),
    ("locks-one-nonadmissible", "hard",
     re.compile(_p(r"locks exactly one local possibility"))),
    ("site-need-not-carry", "hard",
     re.compile(_p(r"[Aa] site need not carry a record"))),
    ("subset-available-under-admissibility", "hard",
     re.compile(_p(r"from the subset available at that site under "
                   r"Admissibility"))),
    ("invariant-repeated-readout", "hard",
     re.compile(_p(r"invariant under repeated readout"))),
]

LANE_BUCKETS = [
    ("flavor-koide", re.compile(r"koide|flavor|pmns|ckm|lepton|tm2", re.I)),
    ("gauge-theta", re.compile(r"theta|gauge|plaquette|wilson|center|"
                               r"character|abj|color", re.I)),
    ("matter-kinetic", re.compile(r"kinetic|isotropy|dispersion|staggered|"
                                  r"dirac|taste|mass|wep|matter", re.I)),
    ("gravity-records", re.compile(r"gravit|clock|pocket|green|source|"
                                   r"deposition|registration", re.I)),
    ("hierarchy", re.compile(r"hierarch|delta0|decimation", re.I)),
    ("probability-born", re.compile(r"born|gleason|measure|probabilit", re.I)),
    ("foundations-record-dynamics", re.compile(r"record|dynamic|admissib|"
                                               r"axiom|realiz|arrow", re.I)),
]


def lane_for(path: str) -> str:
    name = Path(path).name
    for lane, pat in LANE_BUCKETS:
        if pat.search(name):
            return lane
    return "misc"


def main() -> int:
    commit = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
        capture_output=True, text=True, check=True).stdout.strip()

    ledger_by_path = {}
    rows = json.loads(LEDGER.read_text())["rows"]
    for r in rows.values():
        p = r.get("note_path")
        if p:
            ledger_by_path.setdefault(p, r)

    self_path = Path(__file__).resolve()
    targets = sorted(
        p for p in REPO.glob("docs/**/*.md")
        if "docs/audit/data/" not in p.as_posix()
    ) + sorted(p for p in REPO.glob("scripts/*.py")
               if p.resolve() != self_path)

    hits = []
    for path in targets:
        rel = path.relative_to(REPO).as_posix()
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        cats = {}
        for cat, sev, pat in NEEDLES:
            n = len(pat.findall(text))
            if n:
                cats[cat] = (sev, n)
        if not cats:
            continue
        row = ledger_by_path.get(rel)
        hits.append({
            "path": rel,
            "cats": cats,
            "hard": sum(n for s, n in cats.values() if s == "hard"),
            "soft": sum(n for s, n in cats.values() if s == "soft"),
            "claim_id": row["claim_id"] if row else "",
            "audit_status": row["audit_status"] if row else "",
            "effective_status": (row.get("effective_status") or "") if row else "",
            "claim_type": (row.get("claim_type") or "") if row else "",
            "bucket": ("excluded-historical" if rel in EXCLUDED_HISTORICAL
                       else lane_for(rel)),
        })

    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w") as f:
        f.write("path\thard_hits\tsoft_hits\tcategories\tclaim_id\t"
                "audit_status\teffective_status\tclaim_type\tbucket\n")
        for h in hits:
            catstr = ",".join(f"{c}:{n}" for c, (s, n) in sorted(h["cats"].items()))
            f.write("\t".join([
                h["path"], str(h["hard"]), str(h["soft"]), catstr,
                h["claim_id"], h["audit_status"], h["effective_status"],
                h["claim_type"], h["bucket"]]) + "\n")

    live = [h for h in hits if h["bucket"] != "excluded-historical"]
    hard = [h for h in live if h["hard"] > 0]
    soft_only = [h for h in live if h["hard"] == 0]

    print(f"axiom-reconciliation rescan @ {commit}")
    print(f"scanned files: {len(targets)}")
    print(f"hit files (any needle): {len(hits)} "
          f"(excluded-historical: {len(hits) - len(live)})")
    print(f"live hard-needle files: {len(hard)}")
    print(f"live soft-only files: {len(soft_only)}")
    print()
    print("hard-needle files by lane:")
    for lane, n in sorted(Counter(h["bucket"] for h in hard).items()):
        print(f"  {n:4d}  {lane}")
    print()
    print("hard-needle files by audit_status:")
    for st, n in sorted(Counter(h["audit_status"] or "(no ledger row)"
                                for h in hard).items()):
        print(f"  {n:4d}  {st}")
    print()
    print("needle category totals (live files, files-with-hit):")
    cat_files = Counter()
    for h in live:
        for c in h["cats"]:
            cat_files[c] += 1
    for c, n in sorted(cat_files.items()):
        print(f"  {n:4d}  {c}")
    print()
    danger = [h for h in hard
              if h["audit_status"] in ("audited_clean", "audited_conditional",
                                       "audited_numerical_match")]
    print(f"hard-needle files with retained audit status: {len(danger)}")
    for h in sorted(danger, key=lambda x: x["path"]):
        print(f"  {h['audit_status']:20s} {h['path']}")
    print()
    print(f"TSV: {OUT_TSV.relative_to(REPO).as_posix()}")
    print(f"TOTAL: HARD={len(hard)} SOFT_ONLY={len(soft_only)} "
          f"RETAINED_STATUS_HARD={len(danger)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
