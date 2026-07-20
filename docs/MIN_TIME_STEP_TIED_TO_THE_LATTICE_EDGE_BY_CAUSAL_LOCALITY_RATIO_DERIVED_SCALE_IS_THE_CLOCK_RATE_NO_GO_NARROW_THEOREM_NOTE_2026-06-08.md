# Tying the Lattice Minimum Connection to the Minimum Time Step: One Tick = One Edge (Causal Locality); the Ratio is Derived, the Absolute Scale is the Clock-Rate No-Go — Narrow Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a derivation of the time-step ↔ lattice-edge tie + the ratio/scale split)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py`](../scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py)
**Cached output:** [`logs/runner-cache/min_time_step_tied_to_lattice_edge_by_locality_runner.txt`](../logs/runner-cache/min_time_step_tied_to_lattice_edge_by_locality_runner.txt)

## Source boundary (2026-06-12)

**Boundary:** renaming / bounded reachability support only. Effective status
is audit-derived; this source records only the claim boundary.

The runner checks finite 6-NN reachability and no-diagonal arithmetic, but the
identity between update tick, record tick, `a_tau`, and one lattice edge is
introduced as the row's naming convention.

This note may be cited only for the finite reachability facts and for the
explicit scale-boundary split. It may not be cited as a retained derivation of
the physical minimum time step, record/update tick identity, clock-rate
normalization, or absolute time/length scale.

Promotion beyond renaming support requires a retained bridge theorem deriving
the record/update tick as the time coordinate rather than defining it.

## Audit context

The framework's spatial minimum is one `Z³` nearest-neighbor edge. Whether a
record tick is a dynamical update, whether that update is `R`-local on the
nearest-neighbor relation, and whether a tick defines physical elapsed time are
separate open bridges. `LATTICE_NN_LIGHT_CONE_NOTE.md` is historical context
only here: its currently unaudited theorem says that a separately declared
`R`-local update confines realized differences to `C_t`. It does not supply the
update relation, make every allowed dependency active, identify record ticks
with update ticks, derive a metric, or fix a physical speed or time/edge ratio.

## Historical Candidate Statement (Superseded)

The theorem wording in this section is preserved as provenance for the paired
runner. It is superseded by the source boundary and audit context above and is
not a live conclusion of this note.

**Theorem (one tick = one edge; ratio derived, scale = no-go).**

1. **One minimum time step reaches exactly one edge.** The minimum time step is one elementary
   dynamical update = one record **tick**. Under the local (6-NN) update, one tick propagates influence
   to **exactly the 6 nearest neighbors** — graph-distance 1, Euclidean reach **1.000 edge** (verified
   by BFS). So **one tick ≡ one hop**: the lattice spatial minimum `a_s` and the time minimum `a_τ` are
   the **same elementary causal event**, locked together.
2. **"No diagonals" is load-bearing.** With diagonals (26-NN) one tick reaches **26** sites out to
   Euclidean **√3** — body diagonals — so the tick would span up to `√3` edges and **decouple** from
   the edge. The `LATTICE` axiom's **no-diagonal** clause is precisely what **pins** `a_τ ↔ a_s` to one
   edge per tick.
3. **The forward cone is one edge per tick.** The reachability front advances exactly one graph-edge
   per tick (verified to 5 ticks) — the front speed `v_front = a_s/a_τ`. The reconstructed dispersion's
   group velocity `v_LR = max|∇E| ≤ 1` is the **signal** speed *within* this cone (≤ the front).
4. **Ratio derived; absolute scale = the clock-rate no-go.** The **ratio** `a_τ/a_s = 1/v_front` (one
   tick per edge) is **derived** — causal locality (the declared reachability relation) + the no-diagonal clause
   — and is the **conformal class** (this session's records-derived causal structure). The **absolute
   scale** (`a_s` in metres, `a_τ` in seconds) is the **conformal factor** = the records' clock-rate
   **boundary** ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   `retained_no_go`; [`RECORD_CLOCK_RATE_NORMALIZATION_GATE`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md),
   `retained`): the records give the tick/edge **count**, not the physical unit — the approved
   scale-reference primitive sets the common absolute scale.

## Historical Candidate Answer (Superseded)

**The lattice minimum connection and the minimum time step are tied because they are the same
elementary causal event — one nearest-neighbor hop is one record tick — with "no diagonals" locking
`a_τ ↔ a_s` to one edge per tick. That fixes their *ratio* (`= 1/v_front`, records-derived); their
common *absolute* scale is the records-clock-rate boundary supplied by the approved
scale-reference primitive.**

This is the clean resolution of "where does the minimum time step come from": it is **not** an
independent input — it is the spatial edge, read along the causal (time) direction. Only the shared
unit (the conformal factor) remains a supplied primitive.

## Live Boundary

- **The ratio is not derived here.** If separate bridges identify a record tick
  with an `R`-local update tick and identify graph-edge/tick coordinates with
  physical space/time coordinates, then the chosen 6-NN relation gives a
  conditional one-edge-per-tick support bound. Those bridges are not supplied
  by the finite-graph theorem or this BFS.
- **Reachability locality, reproduced conditionally.** The BFS constructs the
  potential support of a chosen nearest-neighbor relation. The finite-graph
  theorem gives containment only after `R`-locality is supplied; it neither
  guarantees that all six neighbors change nor ties an update tick to physical
  time. The displayed group velocity is a separate model calculation, not a
  consequence of the finite-graph theorem.

## Forbidden imports check

No new axiom. The BFS uses a chosen 6-NN relation; the finite-graph theorem is
currently unaudited and supplies only conditional support containment. The
reconstructed dispersion and clock-rate boundary are separate surfaces. All
computations are finite and memory-safe (BFS on a 9³ open lattice; no large
matrices).

## Runner check breakdown

The labels below are the historical runner's own candidate labels. They report
BFS and model arithmetic; they are not four independent theorem-grade checks
and do not override the live boundary above.

Class A: (A1) one tick reaches exactly one edge (6 NN, Euclidean reach 1.0); (A2) no-diagonals
load-bearing (diagonals span `√3`/tick, decoupling); (A3) the forward cone is one edge per tick,
`v_LR ≤ 1` in-cone; (A4) the ratio is derived, the absolute scale is the clock-rate no-go. Expected
`runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Source-Side Runner Interpretation

The BFS confirms the cumulative support set of the chosen 6-NN relation and
the wider Euclidean radius of a separately chosen 26-NN relation. The group
velocity is computed on another model surface. Neither calculation establishes
that all allowed neighbors change, that the framework realizes either update
relation, that a record tick is an update tick, or that graph coordinates are
physical space/time coordinates. The physical tick/edge ratio therefore
remains open here. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py
```
