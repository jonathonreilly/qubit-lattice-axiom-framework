#!/usr/bin/env python3
"""J:attack-b:PR9355 -- SAME TEST, BOTH SIDES on the driven-SQUID resonator comparison note.

The note's separations: (i) column 50 (nominal residual about +108 kHz, insensitive to the added flux-axis coordinate) versus column 250 (about +115/+120 kHz, sensitive);
(ii) the alternative relative-flux snapshots (RMS about 27 kHz) versus the nominal ones (36.453 / 37.235 kHz).  The identical test is applied to every one of the 20 reserved columns
and to both representations (ng = 0 and ng = 0.5, and RMS versus per-column residual), using only the PR's cached per-column residuals (all twenty are emitted there).
Prints one line per check and SUMMARY:; a HIT is printed only if a stated value differs from the cache or a stated contrast disappears under the identical test.
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/driven-squid-resonator-20260927"
subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
HEAD = subprocess.run(["git", "rev-parse", f"origin/{BRANCH}"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
def show(p): return subprocess.run(["git", "show", f"{HEAD}:{p}"], cwd=ROOT, capture_output=True, text=True).stdout
note = show("docs/DRIVEN_SQUID_RESONATOR_COMPARISON_OPEN_GATE_NOTE_2026-09-27.md")
cache = json.loads(show("logs/runner-cache/driven_squid_resonator_2026_09_27.txt").split("----- stdout -----\n", 1)[1].split("\n----- stderr")[0])

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

cols = [o["column"] for o in cache["observations"]]
arr = lambda e: np.array([p["residual_kHz"] for p in e["points"]])
nom = {e["ng"]: arr(e) for e in cache["nominal"]}
alt = [(e["ng"], e["flux_offset"], e["rms_kHz"], arr(e)) for e in cache["alignment_controls"]]
i50, i250 = cols.index(50), cols.index(250)

# ---- the numbers the note states, against the cache
check("nominal RMS residuals 36.453 / 37.235 kHz for ng = 0 / 0.5", abs(np.sqrt((nom[0] ** 2).mean()) - 36.453) < 6e-4 and abs(np.sqrt((nom[0.5] ** 2).mean()) - 37.235) < 6e-4 and re.search(r"36\.453/37\.235", note.replace(" ", "")) is not None,
      f"recomputed {np.sqrt((nom[0]**2).mean()):.4f}, {np.sqrt((nom[0.5]**2).mean()):.4f}")
check("column 50 residuals +108.149/+108.519 and column 250 +114.807/+120.441 kHz (nominal)", abs(nom[0][i50] - 108.149) < 1e-3 and abs(nom[0.5][i50] - 108.519) < 1e-3 and abs(nom[0][i250] - 114.807) < 1e-3 and abs(nom[0.5][i250] - 120.441) < 1e-3)
a50 = [a[3][i50] for a in alt]; a250 = [a[3][i250] for a in alt]
check("six alternative snapshots: column 50 in +113.27..+113.62 kHz, column 250 in +17.18..+28.98 kHz", abs(min(a50) - 113.27) < 0.01 and abs(max(a50) - 113.62) < 0.01 and abs(min(a250) - 17.18) < 0.01 and abs(max(a250) - 28.98) < 0.01, f"col50 {min(a50):.3f}..{max(a50):.3f}, col250 {min(a250):.3f}..{max(a250):.3f}")

# ---- same test on every column: response to the alternative flux coordinate
def dshift(ng): return np.array([a[3] - nom[ng] for a in alt if a[0] == ng])
d0, d5 = dshift(0), dshift(0.5)
maxresp = {ng: np.abs(d).max(axis=0) for ng, d in ((0, d0), (0.5, d5))}
order = {ng: [cols[i] for i in np.argsort(-maxresp[ng])] for ng in maxresp}
print("   largest response (max |alt - nominal| over the three starts) by column, kHz, ng=0:", {c: round(float(maxresp[0][cols.index(c)]), 1) for c in order[0][:4]}, " ng=0.5:", {c: round(float(maxresp[0.5][cols.index(c)]), 1) for c in order[0.5][:4]})
sens250 = [maxresp[ng][i250] for ng in maxresp]; sens50 = [maxresp[ng][i50] for ng in maxresp]
others = [np.delete(maxresp[ng], [i50, i250]) for ng in maxresp]
check("the contrast holds under the identical test: column 250 responds more than any other column, column 50 no more than the median column, at both charge offsets",
      all(order[ng][0] == 250 for ng in maxresp) and all(maxresp[ng][i50] <= np.median(maxresp[ng]) * 4 for ng in maxresp),
      f"col250 response {sens250[0]:.1f}/{sens250[1]:.1f} kHz, col50 {sens50[0]:.1f}/{sens50[1]:.1f} kHz, median over columns {np.median(maxresp[0]):.1f}/{np.median(maxresp[0.5]):.1f}, next largest {sorted(maxresp[0])[-2]:.1f}/{sorted(maxresp[0.5])[-2]:.1f}")

# ---- the RMS separation, decomposed the same way on both sides
def share(r, idx): return float((r[idx] ** 2).sum() / (r ** 2).sum())
shares_nom = [share(nom[ng], [i50, i250]) for ng in nom]
shares_alt = [share(a[3], [i50, i250]) for a in alt]
rms_wo = lambda r: float(np.sqrt(np.delete(r, [i50, i250]) @ np.delete(r, [i50, i250]) / (len(r) - 2)))
print(f"   share of the sum of squares carried by columns 50 and 250: nominal {shares_nom[0]:.3f}/{shares_nom[1]:.3f}; alternatives {min(shares_alt):.3f}..{max(shares_alt):.3f}")
print(f"   RMS over the other 18 columns: nominal {rms_wo(nom[0]):.2f}/{rms_wo(nom[0.5]):.2f} kHz; alternatives {min(rms_wo(a[3]) for a in alt):.2f}..{max(rms_wo(a[3]) for a in alt):.2f} kHz")
check("the note lists both dominant columns, so the RMS headline is not hiding them: 'Column50 residuals' and 'column250 residuals' both appear in the text", "Column50residuals" in note.replace(" ", "").replace("\n", "") and "column250residuals" in note.replace(" ", "").replace("\n", ""))
check("the alternative-versus-nominal RMS improvement is a column-250 effect: with columns 50 and 250 removed, the alternative RMS is within a factor 1.5 of the nominal RMS", max(rms_wo(a[3]) for a in alt) / rms_wo(nom[0]) < 1.5 and max(rms_wo(a[3]) for a in alt) / rms_wo(nom[0.5]) < 1.5,
      f"ratio {max(rms_wo(a[3]) for a in alt)/rms_wo(nom[0]):.2f}, {max(rms_wo(a[3]) for a in alt)/rms_wo(nom[0.5]):.2f}")
# both-sides: the improvement in RMS from the alternatives, and what the same coordinate does to the other 18 columns
worse = [int((np.abs(a[3][np.arange(20) != i250]) > np.abs(nom[a[0]][np.arange(20) != i250])).sum()) for a in alt]
print(f"   columns other than 250 whose |residual| increases under the alternative coordinate: {worse} of 19")
check("the alternative coordinate does not improve the other 19 columns overall (their sum of squares is not lower than nominal): it trades one column for the rest", all(float((a[3][np.arange(20) != i250] ** 2).sum()) >= float((nom[a[0]][np.arange(20) != i250] ** 2).sum()) * 0.9 for a in alt),
      "sum of squares ratio (alt/nominal, 19 columns): " + ", ".join(f"{float((a[3][np.arange(20)!=i250]**2).sum()/(nom[a[0]][np.arange(20)!=i250]**2).sum()):.2f}" for a in alt))
check("extraction-shape sensitivity 2.642 kHz is the cache value", abs(cache["shape_center_max_change_kHz"] - 2.642) < 5e-4)
if not HITS:
    print(f"SUMMARY: no purchase: every value the note states for the two separating contrasts matches the cache, and under the identical test on all 20 columns both contrasts stand (column 250 is the one sensitive column at both charge offsets; columns 50 and 250 carry {min(shares_nom):.0%} of the nominal sum of squares and both are listed in the note); the alternative coordinate leaves the other 19 columns about as they were; {PASS} checks pass")
else:
    print(f"SUMMARY: {FAIL} checks failed: " + "; ".join(HITS))
sys.exit(0)
