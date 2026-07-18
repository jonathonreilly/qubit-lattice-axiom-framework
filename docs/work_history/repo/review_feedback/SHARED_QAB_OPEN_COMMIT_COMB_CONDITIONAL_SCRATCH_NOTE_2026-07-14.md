# Shared q/a/b OPEN–COMMIT Comb — Conditional Scratch Certificate

**Date:** 2026-07-14  
**Authority: none.** This scratch note does not amend an axiom, register a
primitive, issue an audit verdict, or authorize a foundation edit.

## Exact result

From the completed Cycle-57 builder **plus eight completed Cycle-52 rail
slices**, one static exact-nearest-neighbour table constructs role-distinct
`OPEN` and `COMMIT` records for the official targets

```text
q=(0,-1,0), a=(1,0,0), b=(2,0,0),
```

then performs the three designated `VALUE` writes.  The table has 35 canonical
inputs and 52 declared additions.  Exhaustion of every asynchronous append
order gives:

```text
71,425 reachable states;
405,708 directed edges;
1 complete terminal;
0 parasite writes;
0 output conflicts.
```

Every state containing `VALUE_Q`, `VALUE_A`, or `VALUE_B` already contains the
matching role-distinct `OPEN` and `COMMIT`.  The auxiliary footprint avoids the
complete Cycle-43 official support except for the three designated target
writes, avoids 32 Cycle-52 rail slices, has no raw input collision with the
Cycle-52 or Cycle-57 tables, and stays quiescent through 108 further rail
writes.

The schedule-critical repair is explicit: `COMMIT_A` forms before `M0`, and
`M0` requires `COMMIT_A`.  Reversing those two dependencies lets the later
`CAP0` rule permanently mistype the still-open `COMMIT_A` site.

## Exact boundary

This is **not** a live state-zero closure.  At the exact Cycle-57 state zero,
the conditional table's `H0`-only `START` input also writes the official future
support sites `(1,0,2)` and `(1,2,0)`.  The runner retains this as a positive
failing control.  A completion-sensitive start gate is still required.

The fourth target `c=(3,0,0)` also remains open.  A one-order extension reaches
it, but its second shell has three schedule-expanded writes; declaring those
writes produces nine incomplete terminals, and the naive tolerance closure
introduces permanent mistypes.  No `c` closure is claimed here.

Companion scratch runner:

```text
scripts/shared_qab_open_commit_comb_conditional_scratch_2026_07_14.py
```
