# Minimum Time Step Planck-Time Boundary From the Scale Reference and Tick/Edge Tie

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Scope:** conditional-support boundary packet. The Planck-time arithmetic
closes after the tick/edge and `c`-normalization inputs are supplied, but this
row does not itself derive the record/update tick as the physical time
coordinate.
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py`](../scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py)
**Cached output:** [`logs/runner-cache/min_time_step_is_planck_time_from_scale_reference_primitive_runner.txt`](../logs/runner-cache/min_time_step_is_planck_time_from_scale_reference_primitive_runner.txt)

## Audit context

The independent audit blocker for this row was:

```text
missing_dependency_edge: include the retained companion one-tick-one-edge authority
and an explicit emergent-c-to-physical-c normalization certificate, then re-audit
the algebraic closure and tighten the runner tolerance to match the note.
```

The current ledger does **not** make the companion tick/edge row a retained
authority. It is `audited_renaming`: the finite reachability facts check, but
the identity between update tick, record tick, `a_tau`, and the physical time
coordinate remains a naming/definition bridge rather than a retained
derivation. This repair therefore takes the honest path: it exposes the
companion packet and the `c`-normalization certificate, but it narrows this row
to conditional/minimality support rather than claiming full positive closure.

The companion tie (one record tick = one nearest-neighbor edge, by causal
locality + the no-diagonal clause) fixes the **ratio** `a_τ/a_s` only after
that tick/time identification is accepted. The approved *scale-reference*
primitive is the framework's single dimensionful ruler, not a Tier-A admitted
premise. With both inputs supplied, the arithmetic identifies `a_τ = l_P/c =
t_P`.

## Safe statement

**Conditional boundary theorem (the one accepted scale reference fixes both
minima once the tick/edge time bridge is supplied).**

1. **The framework accepts one dimensionful scale reference: `a_s = l_P`.** The
   [`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (owner-approved, registered in
   `docs/audit/data/axiom_premise_nodes.json`) declares the framework's **single** dimensionful
   reference: `a⁻¹ = M_Pl` (the `PLANCK_SCALE_LANE_STATUS` package pin). Hence the lattice spacing
   `a_s` = the **Planck length** `l_P` — *already supplied*, carrying **zero** dimensionless content.
   Per `AXIOM_MINIMALITY_POLICY` §6 this is an approved framework primitive
   rather than a new axiom, Tier-A admission, or bounded-status source. The
   independent audit lane still decides this row's actual status from the
   remaining tick/time and physical-`c` bridges.
2. **The one-tick-one-edge tie gives `a_τ = a_s/c`.** One minimum time step (one record tick) spans
   exactly one nearest-neighbor edge in the companion packet
   [`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md),
   checked by
   [`scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py`](../scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py).
   Current audit status for that companion is `audited_renaming`, not retained.
3. **The `c` normalization is explicit.** This packet uses the SI value
   `c = 299792458 m/s` exactly as the physical-unit conversion from one
   edge/tick to seconds. That is a unit-normalization certificate, not a
   derivation of the physical light speed from this row.
4. **Then the minimum time step is the Planck time:** `a_τ = l_P/c = t_P`
   (`5.391×10^-44 s`, verified by the runner at relative error `< 1e-7`).
5. **One scale reference, two minima inside the supplied bridge.** The single approved scale-reference
   primitive (`a⁻¹ = M_Pl`) fixes **both** the minimum length (`a_s = l_P`) **and** the
   minimum time step (`a_τ = t_P`), because the one-tick-one-edge tie welds them. This is consistent
   with the clock-rate no-go ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   `retained_no_go`): the **records** supply the tick/edge *count* (the structure), not the physical
   rate; the **rate** comes from the accepted scale reference. No contradiction — the no-go is about
   the records, the unit is the one accepted anchor.

## The correction this records

The companion note framed the absolute scale as "an open no-go needing a supplied Planck/clock
primitive." That primitive is **already in the framework** (the registered scale-reference primitive).
So the picture completes:

- the records supply the **dimensionless structure** (one tick = one edge; the cone);
- the one accepted dimensionful anchor (`a⁻¹ = M_Pl`) supplies the **unit**;
- together they fix **both** the minimum length (`l_P`) and the minimum time step (`t_P`) — the time
  minimum costs **no extra primitive** (the same one ruler serves both).

## Boundary (honest)

- **Zero new dimensionless content.** `t_P = l_P/c` is the standard definitional relation; the content
  here is *structural*: the framework's **single** anchor + the locality tie suffice for both minima
  (a minimality statement), and the minimum time step is *identified* as the Planck time.
- The scale anchor itself is the accepted (owner-approved) primitive, not a derivation — the framework
  carries one ruler, as the scale-reference primitive states.
- The tick/edge row is currently `audited_renaming`. This packet is therefore
  not a retained derivation of physical time unless a later retained bridge
  derives the record/update tick as the time coordinate.
- `c` is used here as the physical unit conversion `299792458 m/s`; the
  runner checks the normalization explicitly. This packet does not derive the
  emergent-Lorentz-to-physical-`c` bridge.

## Primitive note (the type matters)

The scale reference is **not** a Tier-A admitted premise; it is an **approved framework primitive**
(`scale_reference_primitive`, registered in `axiom_premise_nodes.json`, owner-approved per
`AXIOM_MINIMALITY_POLICY` §6). Per that policy, approved primitives **chain-satisfy dependencies
without bounding downstream status**, whereas Tier-A admitted derivation targets chain-satisfy only at `retained_bounded`.
The scale reference is not the blocker in this row. The open blocker is the
tick/time bridge plus physical-`c` normalization, both now exposed as explicit
checks. This packet should not be read as bare retained until independent audit
accepts those bridges.

## Forbidden premise check

No **new** axiom, admitted premise, **or** primitive. It *uses* the already-approved scale-reference primitive
(`a⁻¹ = M_Pl`) and the companion locality tie; it adds no second dimensionful reference (that is the
point). Finite, memory-safe arithmetic + a tiny BFS.

## Runner check breakdown

Class A/checkable boundary: (A1) the framework scale-reference primitive is
registered; (A2) the companion tick/edge packet and cache are present and the
current ledger status is exposed; (A3) the `c` normalization is explicit and
`l_P/c = t_P` is verified at relative error `< 1e-7`; (A4) the conditional
minimality conclusion is stated without claiming a retained tick/time bridge.
Expected `runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The framework's registered scale-reference primitive fixes the lattice spacing
to the Planck length (`a⁻¹ = M_Pl`). If the companion one-tick-one-edge row is
accepted as the physical time-coordinate bridge, then `a_τ = a_s/c`; with the
explicit SI `c` normalization this gives `a_τ = l_P/c = t_P`, verified at
relative error `< 1e-7`. The single accepted dimensionful anchor then fixes
both the spatial and temporal minima. The note adds no dimensionless content
and no new primitive, but it does not by itself repair the companion
`audited_renaming` status. Effective status remains for the audit lane.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py
```
