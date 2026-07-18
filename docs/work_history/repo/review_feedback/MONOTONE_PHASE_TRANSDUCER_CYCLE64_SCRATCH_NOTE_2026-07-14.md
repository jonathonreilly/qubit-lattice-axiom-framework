# Monotone Phase Transducer — Cycle 64 Scratch

**Date:** 2026-07-14

**Type:** rejected authority-free constructive scratch candidate

**Status:** **RED / superseded by the Cycle-65 mixed-context rejection.**
This file preserves the proposed construction and its failure surface; it is
not a positive result.

**Authority: none.** This note is not an axiom proposal, primitive, retained
theorem, audit verdict, law-selection claim, commit, push, or PR. It changes no
foundation, registry, policy, queue, or audit state. No axiom edit follows.

Companion runner:

```text
scripts/monotone_phase_transducer_cycle64_scratch_2026_07_14.py
```

## Superseding result

Cycle 65 rejects this candidate as written. The runner ends `20 PASS / 1
FAIL`: all fifteen `A` targets also admit output `P`, and `L2=(0,-2,0)` also
admits output `X_B`. A stronger mixed-context scan finds 371 bad contexts
across 95 target/output triples, including off-footprint writes and writes of
the wrong content at declared targets.

The exact rejection, minimal witnesses, and scoped N1-N8 gate are recorded in:

```text
scripts/mixed_local_context_phase_cycle65_2026_07_14.py
docs/work_history/repo/review_feedback/MIXED_LOCAL_CONTEXT_PHASE_CYCLE65_NOTE_2026-07-14.md
```

This rejects only the frozen Cycle-64 table. It is not a no-go for a
strict-nearest-neighbour phase transducer or evidence for an axiom addition.

## Original candidate claim (rejected)

Conditional on the exact completed Cycle-60 reservation comb, this scratch
constructs a finite strict-nearest-neighbour route

```text
OPEN_C -> C at q -> X at b -> independent endpoint Z at a and c.
```

The earlier staged one-parent shell was schedule-fragile. This version instead
declares the complete finite one-A and one-T continuation boundaries and
tabulates every radius-one occupancy subset that preserves the named causal
parents. The resulting object has:

```text
152 permanent additions
142 canonical exact rows
all 24 proper-cubic images live
zero canonical output conflicts
zero off-footprint writes in the complete local-subset scan
```

The auxiliary footprint avoids both the current and next translated official
blocks. In particular, next-cell `q',a',b',c'` stay open. The only current
official writes are the intended `C_Q`, `X_B`, `Z_A`, and `Z_C` records.

The global confluence statement is analytic rather than a sampled preferred
schedule. Roles are ranked

```text
F < A < T < P < GUIDE < HEAD < L2 < C_Q
  < Q0 < Q1 < Q2 < PHASE_E < X_B < {Z_A,Z_C}.
```

For every target, every local subset retaining its lower-rank parents is an
installed exact row. Therefore the lowest unfinished rank remains enabled in
every incomplete configuration. Every maximal append order has the same
complete terminal. The two endpoint-Z records are peers after `X_B` and may
form in either order.

## Historical scope

The claim below was the intended scope before the mixed-context audit. It does
**not** close the bounded phase-distribution geometry, even conditional on the
completed Cycle-60 terminal, because the table is not target-typed. The
remaining compiler obligations are still candidate-law tasks, not missing
Record prose and not evidence for an axiom add.
