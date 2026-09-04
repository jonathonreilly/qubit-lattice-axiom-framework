# Panel 6 — Lens 5: STRATEGY (sequencing and resources)

## 0. Recommendation
CANDIDATE-FIRST, census-second, R1-R3 in parallel. Today: freeze the specs to disk, launch solve-only
workers, land nothing. Tomorrow: a fresh session lands the candidate battery and runs the census; the
codex pool takes R1-R3 and the mechanical repairs. Three blocks, not one and not four.

## 1. (a) Order — candidate-first, and it is not close
SHARED MACHINERY. Both need one object: the exact-rational table of normalized slice-Gram weight
profiles W over the committed fixtures at full-quotient scope, joined to record-frequency profiles,
with the half-support control. The census reads it for collisions, the candidate for ratios — build it
once, whichever verdict lands first.

INFORMATION PER BLOCK. Census-first yields exactly one bit (forced = theorem / chosen = axiom), about
an object the program may discard — if W-ratios are transport-blind the generator is physics-empty by
our own shim theorem, and the block answered a dead candidate's question. Candidate-first yields four
measurements — well-definedness on record classes, sum-to-1, compositionality, transport sensitivity — plus the table itself.

THE SHORT-CIRCUIT (decisive). "Is W(extended)/W(trail) a function of the RECORD class, or does it depend
on which trail in the class you took?" A failure there is a record-does-not-determine-weight finding — a
collision of exactly the census's type, as a by-product. Candidate-first can return the census's answer
early; census-first can never return the candidate's.

THE DOWNGRADE. If transport sensitivity fails, the census drops from top item to low priority (§5).
PARALLEL is available but not free: two simultaneous workers duplicate the enumerator and forfeit the short-circuit. Sequence them over the shared table instead.

## 2. (b) Launchable TODAY by this long session
The perishable asset is not worker time — it is this session's unwritten context. Workers and fresh
sessions are cheap; a compacted head is not. Priority order:
1. FREEZE THE SPECS TO DISK (§6). Highest value, low context cost, survives every other decision. Do
   this first even if nothing else happens today.
2. Launch the c679 cross-lane PIN CONFIRMATION as a small read-only worker. It gates both the census and R1-R3, is self-contained, and confirming it today removes a serial dependency from tomorrow.
3. Launch the CANDIDATE BATTERY (B1) as a solve-only worker writing to a fixed path.

LAND NOTHING TODAY. Solves are cross-context and cost the supervisor almost nothing; landing chains
(fences, sweeps, --deep, main-gate, checker cycles) are what consumed this session. A block landed on
the last of a compacted context is this campaign's error class — cf. the checkpoint-28 date misread.

RISK OF LAUNCH-NOW: a spec written under compaction may be subtly wrong and the fresh session pays to
find out. Mitigation: keep B1 measurement-heavy and interpretation-light; have it emit exact-rational
tables plus the built-in control so it is self-checking; treat its output as re-derivable evidence, never
a trusted pin. If the fresh session distrusts it, it reruns from the frozen spec.

## 3. (c) Granularity — three blocks
B1 CANDIDATE WELL-POSEDNESS + TRANSPORT (emits the shared table). B2 THE FINGERPRINT-COLLISION CENSUS
(reads the table; independently re-derived by its checker, never trusted from B1). B3 THE R1-R3 JOINT
TEST. Do not merge B1+B2 into one verdict: B2 may go to the owner's bar and needs its own fence and
checker, so a correction to one cannot retract the other. If the enumerator dominates cost, one block
with TWO independently fenced verdicts is acceptable — merge the runner, never the fences (checkpoint 28
flagged under-merging at 167/168; the fix is merging machinery, not verdicts). B2 and B3 are independent
— R1-R3's predictions are pre-registered — so they run in parallel, in different pools.

## 4. (d) Codex tomorrow vs Opus today
OPUS TODAY, solve-only: the c679 pin confirmation; B1.
FRESH SESSION TOMORROW: land B1, run B2. The census verdict may need judgment at the owner's bar —
keep it supervised, not cold-pooled.
CODEX (Aug 22, 12:35), cold-executable by design: B3 (R1-R3, bounded-read discipline, c679 pins); the
FOUR NSIMPLIFY REPAIRS (shear_gauge:511, adm_seam:861, quotient_gate:633, quotient_gate:1622/1623
fail-quiet) — named files, named lines, mechanical, non-verdict-bearing, the ideal cold item; the
b141/b142 audit-not-correction only if the owner authorizes it.

## 5. (e) Failure asymmetries
CENSUS COLLIDES EARLY → the collision IS the memo. Exit on first hit (a zero-collision claim needs
exhaustion, a one-collision claim does not); reproduce it at a second fixture size to rule out a scope
artifact (same runner, one extra size); then one page: the two colliding profiles as exact rationals;
fixture and scope pins; the half-support control showing the machinery detects collisions where
expected; the axiom in the exact one sentence Jon must approve; what it buys and what it does not
(nothing about nature — CYCLE913). Do NOT widen scope before the bar — that is post-decision work.

CANDIDATE FAILS CONSISTENCY → three dispositions, pre-registered:
- TRANSPORT SENSITIVITY fails: physics-empty by our own shim theorem. The census still decides
  theorem-vs-axiom for the bridge as such, but nothing should pay for it until a new candidate exists —
  demoted, not cancelled; "which W is transport-sensitive?" is an owner-bar design question, not a block.
- WELL-DEFINEDNESS fails: a collision-type finding — report as an early partial census result, then the memo path above.
- SUM-TO-1 fails: almost certainly a partition/normalization definition error, not physics. Repair the
  definition and rerun; pre-register that this does not kill the program.

## 6. (f) Specs a fresh session needs — `.claude/science/physics-loops/generator-20260821/`
- `GOAL.md` — the owner directive verbatim; the candidate P(next record class | trail) =
  W(extended)/W(trail); the three-block plan; what is the owner's call.
- `PINS.md` — committed fixture ids and the four lattice sizes; full-quotient scope and the half-support
  control; chain head #7146 (170) on #7136 (169); the main-gate value recorded at 169's landing
  (38109c45), to be RE-VERIFIED not trusted; the c679 Record/Born contract pins; the b169 transport
  census as the transport-sensitivity machinery; the anti-shim standard quoted;
  RECORD_BORN_FREQUENCY_BOUNDARY; the CYCLE913 caution.
- `CANDIDATE_SPEC.md` (B1) — the four checks, each with a pre-registered PASS/FAIL rule and its §5
  disposition; the table emission format; exact rationals; `nsimplify` banned in new runners.
- `CENSUS_SPEC.md` (B2) — as staged in DECISION_MEMO_20260821.md §5, plus early-exit-on-collision and the second-size reproduction.
- `R1R3_SPEC.md` (B3) — panel 4's spec; R1 pass / R2 pass / R3 Gram-fails-no-verdict-flip; falsifier =
  any verdict flip; merge acceptance carries the anti-shim standard.
Nothing in these may reference this session's memory. Source of record otherwise:
`CAMPAIGN_20260820_48H_HANDOFF.md`.

## 7. Owner's call vs executable
OWNER'S CALL: adding the bridge as an axiom (reachable only if the census collides); the b141/b142
re-pin disposition (touches landed artifacts); theta-prime adoption, open since #7011; the e_x = -1
class registration; any registered-premise class for a support-pattern change; and, if the candidate
is transport-blind, the choice of a replacement W.
EXECUTABLE NOW, NO ASK: the specs; the c679 pin confirmation; B1; B2 (the memo's default stages it);
B3 under pre-registration; the four nsimplify repairs.
