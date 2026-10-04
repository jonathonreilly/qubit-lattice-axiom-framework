# Minimum Time Step Planck-Time Boundary From the Scale Reference and Tick/Edge Tie

**Date:** 2026-06-08 (2026-06-16 kinetic-form `c` bridge repair; 2026-10-03 companion-status repair)
**Claim type:** bounded_theorem
**Scope:** bounded-support re-audit packet. Conditional reference-unit
arithmetic: if the physical spacing ratio `r=a_s/l_P` and the tick/edge tie
are supplied, `a_τ=r t_P`. The numerical fixture chooses `r=1`; this does
not derive the physical spacing ratio. The packet uses the registered
scale-reference primitive, the registered
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
normalization, the arithmetic gives `a_τ = a_s/c = r t_P`, with
`r=a_s/l_P` still supplied/open. The displayed fixture chooses `r=1`.

## Safe statement

**Bounded theorem for re-audit (reference-unit arithmetic, conditional on
the spacing ratio and tick/edge tie).** Let `r=a_s/l_P>0` denote the
physical spacing ratio. The supplied tick/edge tie and physical-`c` conversion
give `a_τ=a_s/c=r(l_P/c)=r t_P`. Equality `a_τ=t_P` requires `r=1`;
the units reference alone does not prove this physical self-consistency.

1. **The framework accepts one dimensionful scale reference.** The
   [`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (owner-approved, registered in
   `docs/audit/data/axiom_premise_nodes.json`) declares the framework's **single** dimensionful
   reference: `a⁻¹ = M_Pl` as the chosen units conversion. The primitive
   explicitly does not assert `a/l_P = 1` as a derived theorem: physical
   self-consistency remains an open gravity derivation. The numerical fixture
   uses Planck reference units; it does not close that dimensionless ratio.
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
5. **Then, conditional on the tie and the chosen `r=1` fixture, the reference tick is the Planck time:** `a_τ = l_P/c = t_P`
   (`5.3912464×10^-44 s`, verified by the runner at rounded-fixture relative difference `< 1e-7`).
6. **One scale reference, a conditional length/time ratio.** The supplied
   spacing `a_s=r l_P` and tick/edge tie give `a_τ=r t_P`. For the reference
   fixture `r=1`, the two displayed values are `l_P` and `t_P`. No physical
   minimum is proved equal to its reference unit by that convention. This is consistent
   with the clock-rate no-go ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   a `no_go` row, currently `unaudited`): the **records** supply the tick/edge *count* (the structure), not the physical
   rate; a physical rate still needs the supplied spacing and clock bridge.
   The accepted reference supplies units without selecting that bridge.

## The correction this records

The companion note framed the absolute scale as "an open no-go needing a supplied Planck/clock
primitive." That primitive is **already in the framework** (the registered scale-reference primitive).
The registered ruler supplies units; the physical spacing and clock bridges
remain separate obligations:

- the records and the supplied tick/edge tie supply the **dimensionless structure** (one tick = one edge; the cone);
- the one accepted dimensionful anchor (`a⁻¹ = M_Pl`) supplies the **unit**;
- the supplied spacing ratio and tick/edge bridge give `a_τ=r t_P`;
  `r=1` is the reference fixture here, not a derived physical minimum.

## Boundary (honest)

- **Zero newly adopted dimensionless content.** `t_P = l_P/c` is the
  supplied definitional relation. The spacing ratio `r` is not derived or
  registered as a primitive. The conditional result is `a_τ=r t_P`; the
  numerical choice `r=1` is a fixture, not an adopted physical theorem.
- The scale anchor itself is the accepted (owner-approved) primitive, not a derivation — the framework
  carries one ruler, as the scale-reference primitive states.
- The kinetic-form bridge itself is the accepted kinetic-isotropy primitive:
  it authorizes `c_lattice = 1` on the edge/tick surface and nothing more.
- The tick/edge row is an `open_gate` with current effective status
  `unaudited`. This packet uses its tie as a supplied one-hop premise from the
  record/update tick to the lattice edge/time-step ratio; the Planck-time
  identification with a physical minimum also needs the spacing ratio
  `r=1` to be derived or explicitly supplied, in addition to that bridge.
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
The registered units reference is not itself a blocker. The physical
spacing-ratio and tick/edge suppliers remain open. The kinetic-form bridge is
also now explicit: the approved kinetic-isotropy primitive supplies
`c_lattice = 1` at structural scope. The physical-`c` normalization is exposed
as an exact SI unit-conversion check, not hidden as a derived dynamics claim.
This packet should not be read as bare retained until independent audit
accepts the repaired bridge surface.

## Forbidden premise check

No **new** axiom or primitive. It *uses* the
already-approved scale-reference primitive (`a⁻¹ = M_Pl`), the
already-approved kinetic-isotropy primitive (`c_t = c_s`, structural
kinetic form only), and the supplied companion locality tie. The spacing
ratio `r` remains conditional/open rather than becoming a primitive; this
packet adds no second dimensionful reference or adopted dimensionless
dynamical value. Finite,
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
`runner_check_breakdown = {A: 21, B: 0, C: 0, D: 0, total_pass: 21}`.

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
on the standard supplied definitions. Identifying a physical update tick
with this quantity requires both the open tick/edge bridge and the supplied
or derived spacing ratio `r=1`.

## Honest auditor read

The framework's registered scale-reference primitive chooses Planck
reference units (`a⁻¹ = M_Pl`); it does not derive the physical ratio
`a/l_P = 1`. The registered kinetic-isotropy primitive
authorizes the lattice-unit edge/tick normalization (`c_lattice = 1`) at
structural scope only. The companion one-tick-one-edge row is an
`open_gate` (`unaudited`), so `a_τ = a_s/c` holds only when that tie is
supplied; with the explicit SI `c` normalization this gives
`a_τ = a_s/c = r t_P`. Only the supplied reference fixture `r=1` gives
`a_τ = l_P/c = t_P`, checked at rounded-fixture relative difference
`< 1e-7`. Neither physical minimum is selected by that numerical check.
The note adds no dimensionless content and no new primitive. This row's
effective status remains for the audit lane until re-audit.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_is_planck_time_from_scale_reference_primitive_runner.py
```
