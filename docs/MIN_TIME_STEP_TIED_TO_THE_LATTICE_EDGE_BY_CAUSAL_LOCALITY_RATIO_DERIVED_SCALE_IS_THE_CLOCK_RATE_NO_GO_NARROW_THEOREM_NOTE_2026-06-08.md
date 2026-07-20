# Minimum-Time / Lattice-Edge Identification Boundary

**Date:** 2026-06-08
**Claim type:** open_gate
**Status:** open physical tick/edge identification gate with bounded
combinatorial reachability support. Audit outcome and effective status belong
exclusively to the independent audit lane.
**Primary runner:** [`scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py`](../scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py)
**Cached output:** [`logs/runner-cache/min_time_step_tied_to_lattice_edge_by_locality_runner.txt`](../logs/runner-cache/min_time_step_tied_to_lattice_edge_by_locality_runner.txt)

## Source boundary (2026-06-12)

**Boundary:** open tick/edge identification gate with bounded reachability
support only. Effective status is audit-derived; this source records only the
claim boundary.

The runner checks finite 6-NN reachability and no-diagonal arithmetic, but the
identity between update tick, record tick, `a_tau`, and one lattice edge is
introduced as the row's naming convention.

This note may be cited only for the finite reachability facts and for the
explicit scale-boundary split. It may not be cited as a derivation of the
physical minimum time step, record/update tick identity, clock-rate
normalization, or absolute time/length scale.

Closing the gate requires an independently audited bridge theorem deriving the
record/update tick as the time coordinate rather than defining it.

## Audit context

The framework's spatial minimum is one `Z³` nearest-neighbor edge. Whether a
record tick is a dynamical update, whether that update is `R`-local on the
nearest-neighbor relation, and whether a tick defines physical elapsed time are
separate open bridges. `LATTICE_NN_LIGHT_CONE_NOTE.md` is historical context
only here: its currently unaudited theorem says that a separately declared
`R`-local update confines realized differences to `C_t`. It does not supply the
update relation, make every allowed dependency active, identify record ticks
with update ticks, derive a metric, or fix a physical speed or time/edge ratio.

## Historical Provenance

Earlier versions bundled the runner's chosen update relation with a physical
one-tick/one-edge interpretation. That interpretation was not derived. Git
history preserves the superseded wording; it is intentionally not repeated on
this live source surface.

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

The runner performs four bounded diagnostics: the chosen 6-NN one-step count
and Euclidean radius, the chosen 26-neighbor comparison, the five-step 6-NN
BFS graph radius, and a separate model's finite-grid group velocity. They are
not four independent theorem-grade checks and do not override the live
boundary above. The classification is
`runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Source-Side Runner Interpretation

The BFS confirms the cumulative support set of the chosen 6-NN relation and
the wider Euclidean radius of a separately chosen 26-NN relation. The group
velocity is computed on another model surface. Neither calculation establishes
that all allowed neighbors change, that the framework realizes either update
relation, that a record tick is an update tick, or that graph coordinates are
physical space/time coordinates. The physical tick/edge ratio therefore
remains open here. Effective status is pipeline-derived after independent
audit.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py
```
