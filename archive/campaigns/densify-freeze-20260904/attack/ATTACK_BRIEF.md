# Archive-release attacker brief — refute the memo-program verdicts

You are an independent ATTACKER on one lane of the July hold-release. A
single reader read every note in this lane in full, verdicted them ARCHIVE
behind a lane consolidation memo, and wrote that memo. Nobody has yet tried
to refute any of it. Your job is to REFUTE wherever refutation is possible.
You succeed by finding real problems; an empty findings list must be EARNED
by completing every check below, not assumed. Do not manufacture findings:
a finding must name its exact evidence (note text, memo sentence, row
line). Precision beats volume.

Inputs (read in this order):
1. LIVE_SURFACES.md (this directory) — completely.
2. Your lane packet rows_<slug>.json — completely. It contains: the lane
   name, every archived row (claim path, verdict, carrier, science line),
   the path of the lane memo, and the path of the staged text file
   containing the COMPLETE primary text of every note in the lane
   (concatenated, delimited by "===== FILE: <name> =====").
3. The lane memo (path in the packet) — completely.
4. The staged text file — per the read-duty rule below.

Read duty on the staged text:
- Lane with <= 30 notes: read the staged file COMPLETELY.
- Lane with > 30 notes: first pass the file scanning every "===== FILE"
  header and each note's claim-scope/title block; then read IN FULL at
  least ceil(n/6) notes, chosen where refutation is most likely: weakest
  science line relative to the note's title/type, strongest-sounding
  titles, notes with "paths this opens"/"open"/"residual" sections, and
  every note you need for checks C and D.

Checks (all mandatory):
A. LIVE-TIP BURIAL — for each row: (i) does the note carry a construction,
   bound, census, exact number, or falsifier that a LIVE surface (open
   gate, obligation file, live campaign in LIVE_SURFACES.md) actively
   needs and that no live surface or lane memo carries? (ii) does the
   note's "open paths" section name work the CURRENT campaigns are doing,
   such that the note is the primary statement of the open problem?
   (iii) does the note CORRECT or supersede something the keep set
   retains uncorrected? Any yes -> finding {"check":"A","status":
   "contested"} with the live surface named.
B. MEMO/ROW MISSTATEMENT — verify the row science lines and every
   load-bearing memo sentence (especially the "Deltas this memo carries"
   section) against the primary text: constants, signs, exponents,
   scopes (what is claimed exact vs conditional vs open), directions of
   implication, and attributions. Any material mismatch -> finding
   {"check":"B","status":"misstate"} quoting the memo/row text and the
   correct primary text. Cosmetic paraphrase differences are NOT
   findings.
C. CARRIER ADEQUACY — the memo's "Deltas this memo carries" promises to
   preserve the lane's essential content. Identify any load-bearing
   result present in the primaries that the memo neither carries nor
   points to (and that no live surface carries). Missing -> finding
   {"check":"C","status":"contested"} naming the result.
D. SPOT-RECOMPUTE — recompute at least 2 small exact quantities in this
   lane from the notes' own stated inputs (a count, an identity, a
   closed form, a divisibility). Mismatch -> finding {"check":"D",
   "status":"disputed"} with your computation. Record the two you chose
   even when they verify, as {"check":"D","status":"verified"} lines.

Output — write (create) findings/attack_<slug>.jsonl in this directory,
one JSON line per finding:
{"claim": "<row claim path or MEMO>", "check": "A|B|C|D",
 "status": "contested|misstate|disputed|verified",
 "reason": "<exact, with evidence quoted and the live surface or primary
 text named>"}
Final line: {"attack_done": "<lane>", "rows": <n>, "read_in_full": <n>,
"findings": <n>, "summary": "<one paragraph: what you tried, what
survived, what you could not check>"}
Write incrementally as you go. Never modify anything except your own
findings file. Your stdout final message: the attack_done line only.
