# Fix-layer checker brief

You are an independent CHECKER attacking the REPAIR LAYER of an archive
freeze: the corrective text blocks appended to ledger rows (and mirrored
in lane memos) during the 2026-09-04 attack-pass repair. Your job is to
REFUTE them. Everything is read-only except your own findings file.

For each assigned lane you get:
- `checkfix/blocks_<slug>.json` — the new text blocks. Each block has the
  claim path and the appended corrective text. THIS TEXT IS THE ATTACK
  SURFACE.
- `memos/<Lane>.md` — the repaired lane memo. Sentences added by the
  repair are identifiable by corrective vocabulary (e.g. "attack-pass
  verified 2026-09-04", "(carried)", "(corrected)", ALL-CAPS flag words,
  inventory counts). Check those sentences too.
- `/tmp/lane_<slug>.txt` — the staged full primary text of every note in
  the lane. READ DUTY: every factual assertion, quote, number, formula,
  scope word, and attribution in a block MUST be verified against this
  staged text before you pass it. A block referencing a FRONT surface or
  live campaign may cite content outside the staged text — mark those
  `unverifiable-here` rather than guessing.

Report ONLY defects in the NEW text (not in the primaries, not in the
pre-existing memo text): misquotes, wrong numbers/formulas/signs, scope
broader or narrower than the primary, wrong attributions (note, cycle,
date), claims the primary does not support, and internal contradictions
between a block and its memo mirror.

Output: append one JSON line per finding to your assigned findings file:
{"lane": "...", "claim": "...", "severity": "material|minor",
 "defect": "...", "primary_evidence": "exact quote from staged text"}
Finish with: {"check_done": "<seat>", "lanes": [...], "blocks_checked": N,
 "findings": N, "summary": "..."}
Write incrementally. One focused deliverable; short stdout summary only.
