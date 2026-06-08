# The Minimum Time Step IS the Planck Time, Fixed by the Framework's Single Already-Imported Scale Reference — Not a Second Import (Narrow Theorem)

**Date:** 2026-06-08
**Claim type:** bounded_theorem (units/minimality closure: one scale import fixes both spatial and temporal minima)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/min_time_step_is_planck_time_from_single_scale_import_runner.py`](../scripts/min_time_step_is_planck_time_from_single_scale_import_runner.py)
**Cached output:** [`logs/runner-cache/min_time_step_is_planck_time_from_single_scale_import_runner.txt`](../logs/runner-cache/min_time_step_is_planck_time_from_single_scale_import_runner.txt)

## Audit context

The companion tie (one record tick = one nearest-neighbor edge, by causal locality + the no-diagonal
clause) fixed the **ratio** `a_τ/a_s` and left the **absolute scale** as "a supplied primitive." This
note records that the framework **already imports exactly that primitive** — so the absolute scale is
not an open gap, and the minimum time step is fully determined as the **Planck time**.

## Safe statement

**Theorem (one import fixes both minima; the minimum time step is the Planck time).**

1. **The framework imports one dimensionful scale: `a_s = l_P`.** The
   [`SCALE_REFERENCE_PRIMITIVE`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) (owner-approved, registered in
   `docs/audit/data/axiom_premise_nodes.json`) declares the framework's **single** dimensionful
   reference: `a⁻¹ = M_Pl` (the `PLANCK_SCALE_LANE_STATUS` package pin). Hence the lattice spacing
   `a_s` = the **Planck length** `l_P` — *already supplied*, carrying **zero** dimensionless content.
2. **The one-tick-one-edge tie gives `a_τ = a_s/c`.** One minimum time step (one record tick) spans
   exactly one nearest-neighbor edge (the companion tie; reproduced here by BFS: one tick → the 6
   nearest neighbors), with `c` the emergent causal/front speed (one edge per tick).
3. **Therefore the minimum time step is the Planck time:** `a_τ = l_P/c = t_P` (`5.391×10⁻⁴⁴ s`,
   verified to a relative `10⁻⁷` — `l_P/c` *is* `t_P`).
4. **One import, two minima — the minimum time step is not a second import.** The single
   scale-reference primitive (`a⁻¹ = M_Pl`) fixes **both** the minimum length (`a_s = l_P`) **and** the
   minimum time step (`a_τ = t_P`), because the one-tick-one-edge tie welds them. This is consistent
   with the clock-rate no-go ([`POST_RECORD_CLOCK_RATE_INTERFACE`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
   `retained_no_go`): the **records** supply the tick/edge *count* (the structure), not the physical
   rate; the **rate** comes from the imported scale primitive. No contradiction — the no-go is about
   the records, the unit is the one accepted anchor.

## The correction this records

The companion note framed the absolute scale as "an open no-go needing a supplied Planck/clock
primitive." That primitive is **already in the framework** (the registered scale-reference primitive).
So the picture completes:

- the records supply the **dimensionless structure** (one tick = one edge; the cone);
- the one accepted dimensionful anchor (`a⁻¹ = M_Pl`) supplies the **unit**;
- together they fix **both** the minimum length (`l_P`) and the minimum time step (`t_P`) — the time
  minimum costs **no extra import**.

## Boundary (honest)

- **Zero new dimensionless content.** `t_P = l_P/c` is the standard definitional relation; the content
  here is *structural*: the framework's **single** anchor + the locality tie suffice for both minima
  (a minimality statement), and the minimum time step is *identified* as the Planck time.
- The scale anchor itself is the accepted (owner-approved) primitive, not a derivation — the framework
  carries one ruler, as the scale-reference primitive states.
- `c` is the emergent causal/front speed (the cone normalization, one edge per tick); the
  identification with the physical light speed is the emergent-Lorentz normalization.

## Forbidden imports check

No **new** axiom or import. It *uses* the already-registered scale-reference primitive (`a⁻¹ = M_Pl`)
and the companion locality tie; it adds no second dimensionful reference (that is the point). Finite,
memory-safe arithmetic + a tiny BFS.

## Runner check breakdown

Class A: (A1) the framework imports one scale, `a_s = l_P`; (A2) one tick = one edge ⟹ `a_τ = a_s/c`;
(A3) `a_τ = l_P/c = t_P` (relative `10⁻⁷`); (A4) one import fixes both minima, consistent with the
clock-rate no-go. Expected `runner_check_breakdown = {A: 4, B: 0, C: 0, D: 0, total_pass: 4}`.

## Honest auditor read

The framework's registered scale-reference primitive fixes the lattice spacing to the Planck length
(`a⁻¹ = M_Pl`); the companion one-tick-one-edge tie (reproduced by BFS) gives `a_τ = a_s/c`; so the
minimum time step is `l_P/c = t_P`, the Planck time (verified to `10⁻⁷`). The single accepted
dimensionful anchor therefore fixes both the spatial and temporal minima — the minimum time step is
not a second import — and this is consistent with the records-clock-rate no-go (the records give the
count, the anchor gives the unit). The note adds no dimensionless content and no new import; it records
a units/minimality closure and the identification of the minimum time step with the Planck time.
Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/min_time_step_is_planck_time_from_single_scale_import_runner.py
```
