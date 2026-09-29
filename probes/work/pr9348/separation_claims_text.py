#!/usr/bin/env python3
"""J:attack-b:PR9348 -- same test, both sides: does the transmon holdout note make a separation claim (model A has property X, model B lacks it)?

The note fixes four calibration coordinates in a supplied single-cosine transmon-plus-resonator model and reports nonzero residuals on three unused transitions. A 'both sides' attack needs a claim of the form
'this model has X where that model lacks X'. This script reads the note at the PR head as text and lists every sentence that could carry such a claim (words: reject, exclude, separate, distinguish, better, worse,
harmonic, alternative, rule out, unique, only), and checks each against the note's own disclaimers, then states whether any comparison between two models is asserted. Nothing is fitted here.
Prints SUMMARY:; HIT: only if a separation claim is asserted without the same test applied to the other side.
"""
import re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
git("fetch", "origin", "pull/9348/head", "--quiet"); HEAD = git("rev-parse", "FETCH_HEAD").stdout.strip()
files = git("diff", "--name-only", f"origin/main...{HEAD}").stdout.split()
note_path = [f for f in files if f.startswith("docs/") and f.endswith(".md") and "audit" not in f][0]
note = git("show", f"{HEAD}:{note_path}").stdout
body = note.split("\n---\n", 2)[-1]
text = re.sub(r"\s+", " ", body)
sents = re.split(r"(?<=[.;:!?]) ", text)
KEY = re.compile(r"reject|exclud|separat|distinguish|better|worse|harmonic|alternative|rule out|unique|only|no-go|compatible|selected", re.I)
hits = [s for s in sents if KEY.search(s)]
print(f"note {note_path[:90]}...: {len(sents)} sentences, {len(hits)} with a separation-type word")
for s in hits: print("   -", s[:230])
disclaimers = ["not a statistical rejection", "not exclusion of every model", "not a theorem excluding other models", "not uniquely identify", "no universal negative", "found root, not global uniqueness", "comparators, not conclusions"]
found = {d: (d in text or d.replace("not a", "not") in text) for d in disclaimers}
# the note's own scope phrases, checked literally
lit = [("not a statistical rejection or a theorem excluding other models", "not a statistical rejection or a theorem excluding other models" in text),
       ("Existing conventional explanations are comparators, not conclusions", "Existing conventional explanations are comparators, not conclusions" in text),
       ("does not derive Josephson harmonics or uniquely identify the missing physical correction", "does not derive Josephson harmonics or uniquely identify the missing physical correction" in text),
       ("not exclusion of every model compatible", "not exclusion of every model compatible" in text)]
for k, v in lit: print(f"   [{'PASS' if v else 'FAIL'}] scope sentence present: {k}")
asserted = [s for s in hits if re.search(r"(model|correction|harmonic)s? (that|which|with) (lack|has|have)|cannot|fails to|is excluded|are excluded|separates", s, re.I)]
print("   sentences asserting one model has a property another lacks:", asserted)
ok = all(v for _, v in lit) and not asserted
if ok:
    print("SUMMARY: no purchase: the note asserts no separation between models; it states residuals of one supplied single-cosine model under its calibration and disclaims rejection, exclusion of other models and identification of the missing correction, so there is no second object to which the identical test must be applied")
else:
    print("SUMMARY: a separation-type sentence was found: " + "; ".join(asserted[:2])); print("HIT: " + "; ".join(asserted[:2]))
sys.exit(0)
