# Opportunity Queue — audit-unlock-toe-20260724

Ranked per skill criteria: retained-positive probability, missing-import count,
runner/test availability, review landability, blast radius/branch size,
independence from any just-blocked lane.

## 1. Audit-loop drain of the root-ready frontier (lane A) — ACTIVE

- **What:** independent codex audit-loop worker(s) on clean origin/main clones,
  argument-less coordinator drain (`orchestrate_audit_loop.py`), max-workers 2
  per clone for machine-load care.
- **Why ranked #1:** zero missing imports (pure backlog work), highest blast
  radius per unit compute — 551 root-ready rows gate 2,403 blocked rows; the
  top root-ready row by transitive unaudited fanout
  (`abj_epsilon_index_square_block_no_go_note_2026-05-30`) alone gates 1,244.
- **State:** worker `audit-w-20260724-a` dispatched 2026-07-24 on a clean
  clone; coordinator owns target selection (no per-row CLI targeting exists,
  verified in the argparse surface).
- **Independence:** fully independent of science lanes.

## 2. KCPT Unit 20 landing + chain continuation (lane B) — ACTIVE

- **What:** land the block-bicommutant dim-992 unit (note + runner PASS=26 +
  cache) via worktree PR and codex review-loop; then design Unit 21 on the
  landed surface (candidate directions recorded in ROUTE_PORTFOLIO.md).
- **Why ranked #2:** runner already green under my own re-run; review complete
  and clean; landability high (19 consecutive KCPT units landed); serves
  obligation #1's structural surface.
- **Blast radius:** small (3-file triple), builds strictly on landed unaudited
  chain — cites only U18/U19 notes.

## 3. TOE-obligation stretch target: theta cross-sector readout (lane B)

- **What:** a bounded unit connecting the U14 CP-completion / U17 Dirac-radius
  grading to the `theta_quark_determinant_cross_sector_readout` obligation's
  registered surface — e.g. what the H-level structure registers about
  determinant reality across sectors.
- **Why ranked #3:** higher payoff, lower certainty; algebra-before-spec
  required (Fable derivation sketch first). No new imports needed for the
  structural step.

## 4. Fix-class repair: unit-singlet physical-consumer projection repair

- **What:** ACTIVE_REVIEW_QUEUE item
  `2026-07-19-unit-singlet-physical-consumer-projection-repair` — a known
  repair-shaped unit (same-day landable class per the audit-unlock fix-class
  campaign pattern).
- **Why ranked #4:** landable and useful, but smaller blast radius than 1-3;
  take it when lanes 1-3 are all waiting on background workers.

## Refresh rule

Re-rank after each landed block or audit-loop worker exit; a blocked lane
records its blocker in NO_GO_LEDGER.md / APPROACH_REGISTRY.md and the next item
is taken (Campaign Rule: per-route blockers never stop the campaign).
