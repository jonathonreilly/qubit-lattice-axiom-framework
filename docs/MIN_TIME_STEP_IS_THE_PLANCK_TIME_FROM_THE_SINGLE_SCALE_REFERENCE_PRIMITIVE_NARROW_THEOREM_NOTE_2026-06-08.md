# Minimum Time Step Planck-Time Boundary From the Scale Reference and Tick/Edge Tie

**Date:** 2026-06-08 (2026-06-16 kinetic-form `c` bridge repair)
**Claim type:** bounded_theorem
**Scope:** bounded-support re-audit packet. The Planck-time arithmetic closes
from the registered scale-reference primitive, the registered
kinetic-isotropy primitive, the now-retained tick/edge companion, and the
explicit physical-`c` unit normalization. This row does not derive the
physical value of `c` from emergent Lorentz dynamics; the
kinetic-isotropy primitive authorizes the lattice-unit normalization
`c_lattice = 1`, and the exact SI value of `c` is used only as the unit
conversion between the retained edge/tick bridge and seconds.
**Status:** source repaired for re-audit. The current effective status remains
owned by the independent audit lane.
**Primary runner:** [`scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py`](../scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py)
**Cached output:** [`logs/runner-cache/min_time_step_is_planck_time_from_scale_reference_primitive_runner.txt`](../logs/runner-cache/min_time_step_is_planck_time_from_scale_reference_primitive_runner.txt)

## Audit context

The independent audit blocker for this row was:

```text
missing_dependency_edge: include the retained companion one-tick-one-edge authority
and an explicit emergent-c-to-physical-c normalization certificate, then re-audit
the algebraic closure and tighten the runner tolerance to match the note.
```

The current generated ledger exposes the companion tick/edge row with
effective status `retained_bounded`. This repair consumes that retained-grade
companion as the one-hop tick/edge authority and keeps the `c`-normalization
certificate explicit. It does not edit any audit verdict; it only updates the
source packet for re-audit against the current dependency surface.

The companion tie (one record tick = one nearest-neighbor edge, by causal
locality + the no-diagonal clause) fixes the **ratio** `a_τ/a_s` on a
retained-bounded surface. The approved *kinetic-isotropy* primitive supplies
the structural OS0 normalization `c_t = c_s`, i.e. the lattice-unit bridge
`c_lattice = 1` for the edge/tick surface; it does not supply a physical
seconds/metres value. The approved *scale-reference* primitive is the
framework's single dimensionful ruler. With the
retained companion, the kinetic-form bridge, and explicit physical-`c` unit
normalization, the arithmetic identifies `a_τ = l_P/c = t_P`.

## Safe statement

**Bounded theorem for re-audit (the one accepted scale reference fixes both
minima once the retained tick/edge bridge is read in SI units).**

1. **The framework accepts one dimensionful scale reference: `a_s = l_P`.** The
   [`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (owner-approved, registered in
   `docs/audit/data/axiom_premise_nodes.json`) declares the framework's **single** dimensionful
   reference: `a⁻¹ = M_Pl` (the `PLANCK_SCALE_LANE_STATUS` package pin). Hence the lattice spacing
   `a_s` = the **Planck length** `l_P` — *already supplied*, carrying **zero** dimensionless content.
   Per `AXIOM_MINIMALITY_POLICY` §6 this is an approved framework primitive
   rather than a new axiom or bounded-status source. The
   independent audit lane still decides this row's actual status from the
   repaired source packet.
2. **The one-tick-one-edge tie gives `a_τ = a_s/c`.** One minimum time step (one record tick) spans
   exactly one nearest-neighbor edge in the companion packet
   [`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md),
   checked by
   [`scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py`](../scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py).
   The current generated ledger exposes that companion with effective status
   `retained_bounded`.
3. **The emergent-`c` bridge is the registered kinetic-form primitive.**
   The approved
   [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
   declares `c_t = c_s`: the emergent tick is grained on the same footing
   as the spatial edge. On the retained tick/edge surface this is the
   lattice-unit statement `c_lattice = a_s/a_τ = 1`. It carries no
   physical value of `c`, no dynamics, and no dimensionless observable.
4. **The physical-`c` normalization is explicit.** This packet uses the SI value
   `c = 299792458 m/s` exactly as the physical-unit conversion from one
   edge/tick to seconds. That is a unit-normalization certificate, not a
   derivation of the physical light speed from this row.
5. **Then the minimum time step is the Planck time:** `a_τ = l_P/c = t_P`
   (`5.391×10^-44 s`, verified by the runner at relative error `< 1e-7`).
6. **One scale reference, two minima inside the supplied bridge.** The single approved scale-reference
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
- The kinetic-form bridge itself is the accepted kinetic-isotropy primitive:
  it authorizes `c_lattice = 1` on the edge/tick surface and nothing more.
- The tick/edge row currently has effective status `retained_bounded`.
  This packet consumes it as the one-hop bridge from the record/update tick
  to the lattice edge/time-step ratio.
- `c` is used here as the physical unit conversion `299792458 m/s`; the
  runner checks the normalization explicitly. The emergent-`c` side is the
  lattice-unit `c_lattice = 1` from the kinetic primitive; the SI `c` is a
  unit conversion, not a new physical derivation.

## Primitive note (the type matters)

The scale reference is an **approved framework primitive**
(`scale_reference_primitive`, registered in `axiom_premise_nodes.json`, owner-approved per
`AXIOM_MINIMALITY_POLICY` §6). Per that policy, approved primitives **chain-satisfy dependencies
without bounding downstream status**. No admission class exists; unresolved
derivation conditions remain open and carry zero premise weight.
The scale reference is not the blocker in this row. The kinetic-form bridge is
also now explicit: the approved kinetic-isotropy primitive supplies
`c_lattice = 1` at structural scope. The physical-`c` normalization is exposed
as an exact SI unit-conversion check, not hidden as a derived dynamics claim.
This packet should not be read as bare retained until independent audit
accepts the repaired bridge surface.

## Forbidden premise check

No **new** axiom or primitive. It *uses* the
already-approved scale-reference primitive (`a⁻¹ = M_Pl`), the
already-approved kinetic-isotropy primitive (`c_t = c_s`, structural
kinetic form only), and the companion locality tie; it adds no second
dimensionful reference and no dimensionless dynamical value. Finite,
memory-safe arithmetic + a tiny BFS.

## Runner check breakdown

Class A/checkable boundary: (A1) the framework scale-reference primitive is
registered; (A2) the kinetic-isotropy primitive is registered and supplies
only `c_lattice = 1` / OS0 kinetic-form scope; (A3) the companion tick/edge
packet and cache are present and its current `retained_bounded` effective
status is exposed; (A4) the physical-`c` normalization is explicit and
`l_P/c = t_P` is verified at relative error `< 1e-7`; (A5) the
bounded-support conclusion is stated without adding a new axiom, admission,
primitive, or physical-`c` derivation. Expected
`runner_check_breakdown = {A: 17, B: 0, C: 0, D: 0, total_pass: 17}`.

## Honest auditor read

The framework's registered scale-reference primitive fixes the lattice spacing
to the Planck length (`a⁻¹ = M_Pl`). The registered kinetic-isotropy primitive
authorizes the lattice-unit edge/tick normalization (`c_lattice = 1`) at
structural scope only. The companion one-tick-one-edge row is now
`retained_bounded`, so `a_τ = a_s/c` is available on that repaired bounded
surface; with the explicit SI `c` normalization this gives
`a_τ = l_P/c = t_P`, verified at relative error `< 1e-7`. The single
accepted dimensionful anchor then fixes both the spatial and temporal minima.
The note adds no dimensionless content and no new primitive. This row's
effective status remains for the audit lane until re-audit.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py
```
