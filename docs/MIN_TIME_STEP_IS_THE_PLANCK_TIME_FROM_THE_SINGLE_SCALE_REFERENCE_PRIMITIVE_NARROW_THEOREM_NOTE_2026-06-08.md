# Minimum Time Step Planck-Time Boundary From the Scale Reference and Tick/Edge Tie

**Date:** 2026-06-08 (2026-06-16 kinetic-form `c` bridge repair; 2026-10-03 companion-status repair)
**Claim type:** bounded_theorem
**Scope:** bounded-support re-audit packet. The Planck-time arithmetic closes
from the registered scale-reference primitive, the registered
kinetic-isotropy primitive, the tick/edge tie of the companion row (an open
gate, used here as a supplied premise), and the explicit physical-`c` unit
normalization. This row does not derive the
physical value of `c` from emergent Lorentz dynamics; the
kinetic-isotropy primitive authorizes the lattice-unit normalization
`c_lattice = 1`, and the exact SI value of `c` is used only as the unit
conversion between the supplied edge/tick bridge and seconds.
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

The companion tick/edge row is an `open_gate` whose current effective status
is `unaudited`; its note introduces the identity between update tick, record
tick, `a_τ` and one lattice edge as that row's naming convention. This packet
therefore uses the tick/edge tie as a supplied premise, states the Planck-time
identification conditionally on it, and keeps the `c`-normalization
certificate explicit. It does not edit any audit verdict; it only updates the
source packet for re-audit against the current dependency surface.

The companion tie (one record tick = one nearest-neighbor edge, by causal
locality + the no-diagonal clause) fixes the **ratio** `a_τ/a_s` once it is
supplied. The approved *kinetic-isotropy* primitive supplies
the structural OS0 normalization `c_t = c_s`, i.e. the lattice-unit bridge
`c_lattice = 1` for the edge/tick surface; it does not supply a physical
seconds/metres value. The approved *scale-reference* primitive is the
framework's single dimensionful ruler. With the
supplied tick/edge tie, the kinetic-form bridge, and explicit physical-`c` unit
normalization, the arithmetic identifies `a_τ = l_P/c = t_P`.

## Safe statement

**Bounded theorem for re-audit (the one accepted scale reference fixes both
minima once the tick/edge tie, an open gate, is supplied and read in SI units).**

1. **The framework accepts one dimensionful scale reference: `a_s = l_P`.** The
   [`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (owner-approved, registered in
   `docs/audit/data/axiom_premise_nodes.json`) declares the framework's **single** dimensionful
   reference: `a⁻¹ = M_Pl` (the `PLANCK_SCALE_LANE_STATUS` package pin). Hence the lattice spacing
   `a_s` = the **Planck length** `l_P` — *already supplied*, carrying **zero** dimensionless content.
   Per `AXIOM_MINIMALITY_POLICY` §6 this is an approved framework primitive
   rather than a new axiom or bounded-status source. The
   independent audit lane still decides this row's actual status from the
   repaired source packet.
2. **If the one-tick-one-edge tie is supplied, it gives `a_τ = a_s/c`.** One minimum time step (one record tick) spans
   exactly one nearest-neighbor edge in the companion packet
   [`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md),
   checked by
   [`scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py`](../scripts/min_time_step_tied_to_lattice_edge_by_locality_runner.py).
   That companion row is an `open_gate` (current effective status `unaudited`);
   it introduces the tick/edge identity as a naming convention, so this step is
   a supplied premise, not a derived bridge.
3. **The emergent-`c` bridge is the registered kinetic-form primitive.**
   The approved
   [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
   declares `c_t = c_s`: the emergent tick is grained on the same footing
   as the spatial edge. On the supplied tick/edge surface this is the
   lattice-unit statement `c_lattice = a_s/a_τ = 1`. It carries no
   physical value of `c`, no dynamics, and no dimensionless observable.
4. **The physical-`c` normalization is explicit.** This packet uses the SI value
   `c = 299792458 m/s` exactly as the physical-unit conversion from one
   edge/tick to seconds. That is a unit-normalization certificate, not a
   derivation of the physical light speed from this row.
5. **Then, conditional on the tie, the minimum time step is the Planck time:** `a_τ = l_P/c = t_P`
   (`5.3912464×10^-44 s`, verified by the runner at rounded-fixture relative difference `< 1e-7`).
6. **One scale reference, two minima inside the supplied bridge.** The single approved scale-reference
   primitive (`a⁻¹ = M_Pl`) fixes **both** the minimum length (`a_s = l_P`) **and** the
   minimum time step (`a_τ = t_P`), because the one-tick-one-edge tie welds them. This is consistent
   with the clock-rate no-go ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   a `no_go` row, currently `unaudited`): the **records** supply the tick/edge *count* (the structure), not the physical
   rate; the **rate** comes from the accepted scale reference. No contradiction — the no-go is about
   the records, the unit is the one accepted anchor.

## The correction this records

The companion note framed the absolute scale as "an open no-go needing a supplied Planck/clock
primitive." That primitive is **already in the framework** (the registered scale-reference primitive).
So the picture completes:

- the records and the supplied tick/edge tie supply the **dimensionless structure** (one tick = one edge; the cone);
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
- The tick/edge row is an `open_gate` with current effective status
  `unaudited`. This packet uses its tie as a supplied one-hop premise from the
  record/update tick to the lattice edge/time-step ratio; the Planck-time
  identification holds only if that gate is closed by a bridge theorem.
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
packet and cache are present, and its current ledger status (an `open_gate`,
`unaudited`) is read from the sharded ledger and matched by this note; (A4)
the physical-`c` normalization is explicit and
`l_P/c = t_P` is verified at rounded-fixture relative difference `< 1e-7`; (A5) the
bounded-support conclusion is stated without adding a new axiom, admission,
primitive, or physical-`c` derivation, and the clock-rate no-go's current
ledger status is matched. Expected
`runner_check_breakdown = {A: 20, B: 0, C: 0, D: 0, total_pass: 20}`.

The single-clock evolution theorem is conditional on its supplied axis, step
and single-clock clauses; it does not derive that supply. See
[its B-AXIS premises](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md).
The runner pins the mutable primitive registry, baseline, ledger rows and
companion evidence through `AUDIT_INPUT_PATHS`. The self-contained companion
cache is checked against its runner SHA and successful exit; the review gate
also verifies its governed freshness.

## Numerical fixture boundary

The runner compares the supplied rounded length `1.616255×10^-35 m` divided
by the exact SI conversion `299792458 m/s` with a separate computation
`√(ħG/c^5)` using supplied numerical fixtures `ħ=1.054571817×10^-34 J s`
and `G=6.67430×10^-11 m^3 kg^-1 s^-2`. Their relative difference is an
arithmetic consistency check of these rounded fixtures. It does not
assert empirical accuracy at `10^-7`, derive G or ħ, or promote those
fixtures to framework primitives. The formula `l_P/c=t_P` is conditional
on the standard supplied definitions; identifying a physical update tick
with this quantity still requires the open tick/edge bridge.

## Honest auditor read

The framework's registered scale-reference primitive fixes the lattice spacing
to the Planck length (`a⁻¹ = M_Pl`). The registered kinetic-isotropy primitive
authorizes the lattice-unit edge/tick normalization (`c_lattice = 1`) at
structural scope only. The companion one-tick-one-edge row is an
`open_gate` (`unaudited`), so `a_τ = a_s/c` holds only when that tie is
supplied; with the explicit SI `c` normalization this gives
`a_τ = l_P/c = t_P`, verified at rounded-fixture relative difference `< 1e-7`. The single
accepted dimensionful anchor then fixes both the spatial and temporal minima.
The note adds no dimensionless content and no new primitive. This row's
effective status remains for the audit lane until re-audit.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py
```
