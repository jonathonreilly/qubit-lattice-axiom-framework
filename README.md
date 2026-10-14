# Lattice-Qubit-Admissibility-Record Framework

This repository is the public working record of a four-axiom discrete-physics
program. A note that has landed on `main` is a working record. Ratification
is a separate step. The generated status snapshot, not this README, is the
authority for audit counts.

The four axioms are **Lattice**, **Qubit**, **Admissibility**, and **Record**.
Their statements live only in
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](docs/MINIMAL_AXIOMS_2026-06-29.md).
That memo is edited in place under explicit owner approvals, recorded in
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](docs/audit/AXIOM_MINIMALITY_POLICY.md)
section 6. The earlier three-axiom base (Lattice, Quantum, Record), the
`Quantum` axiom name, and the older `A1`/`A2`/`A3` numbering are historical.

## What is supplied

The supplied foundation is the axiom set plus three approved primitives:

- the scale reference `a^{-1}` (units only),
- kinetic isotropy `c_t = c_s` (regulator graining),
- the realized-state interface (a slot for one law-admissible realized state;
  it selects no state).

They are registered in
[`docs/audit/data/axiom_premise_nodes.json`](docs/audit/data/axiom_premise_nodes.json).

Three open derivation obligations carry zero premise weight. They are the AC
occupancy statistical grain, the R-eta h-class/h-unit readout, and theta's
independent quark-determinant cross-sector readout, tracked in
[`docs/audit/data/derivation_obligations.json`](docs/audit/data/derivation_obligations.json).
Superseded admission-era decisions are provenance in
[`docs/audit/data/premise_decision_history.json`](docs/audit/data/premise_decision_history.json).

The past-hypothesis low-entropy magnitude is a scope condition, not a premise.
Results that use it say so.

Born weights, measurement and readout contexts, record-formation rules
(which admissible possibility a new record locks, at which site, with what
weight, at what rate), dynamics and the time metric, kinetic-branch
selection, source and action structure, and physical-observable identification
are downstream. They bear load only through retained-grade work, or through an
explicit axiom or approved-primitive review. The audit ledger is that record.
The words `retained` and `promoted` inside a source note are not a ledger grade.
Retained-grade `effective_status` values are `retained`, `retained_no_go`, and
`retained_bounded`.

## Read this first

1. [Minimal axiom memo](docs/MINIMAL_AXIOMS_2026-06-29.md)
2. [Start here](docs/START_HERE.md)
3. [Generated front-door status snapshot](docs/repo/FRONT_DOOR_STATUS.md).
   This is a pipeline count, not a physics claim. Read the file for the
   current counts. The refresh command is
   `bash docs/audit/scripts/run_pipeline.sh`.
4. [Key science index](docs/KEY_SCIENCE.md). A listing there grants no status.

The generated retained-row list is
[`docs/repo/RETAINED_BACKBONE.md`](docs/repo/RETAINED_BACKBONE.md). Read it
with the current status snapshot. Ledger shards live
under `docs/audit/data/ledger/`, summarized in
[`docs/audit/data/effective_status_summary.json`](docs/audit/data/effective_status_summary.json).

[State of the theory, 2026-07-16](docs/repo/STATE_OF_THE_THEORY_2026-07-16.md)
is historical orientation. Its counts are the 2026-07-17 ledger.

## Archived forecasts and numbers

The flagship paper package was deferred on 2026-09-03. The snapshot from that
date is `archive/publication/ci3_z3/`. The tier rules are in
[`archive/README.md`](archive/README.md). That tree is a record, not a claim
surface. Forecast numbers and reusable-value tables stay in the snapshot,
with the catalog's own conditionality note. Reuse a number when the ledger
shard for that claim shows a retained-grade `effective_status`.

## If you opened the file list

[`docs/repo/ROOT_FILE_GUIDE.md`](docs/repo/ROOT_FILE_GUIDE.md) says what the
root files are. `AUTOPILOT_*`, `SCALING_*`, and `toy_event_physics.py` are
legacy. [`AGENTS.md`](AGENTS.md) and [`CLAUDE.md`](CLAUDE.md) send agents to
the `ai/execution` branch, which does not merge into `main`.

Leave these directories until a specific note sends you there: `archive/`,
`archive_unlanded/`, `docs/work_history/`, `docs/audit/data/ledger/`,
`logs/`, `outputs/`, and `.claude/`.

Lane maps under [`docs/lanes`](docs/lanes/README.md) are historical
navigation. The April 2026 active-lane list is not the current work queue.

## Boundaries

A landed note, and a row captured in the archived paper package, is not
thereby audit-retained. Measurement, an arrow of time, selector weights, a
kinetic branch, and a physical observable identification are not supplied by
the axiom names in this README. What each axiom supplies is the axiom memo.
The archived non-claim notes are
[`archive/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md`](archive/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md)
and
[`archive/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md`](archive/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md).
