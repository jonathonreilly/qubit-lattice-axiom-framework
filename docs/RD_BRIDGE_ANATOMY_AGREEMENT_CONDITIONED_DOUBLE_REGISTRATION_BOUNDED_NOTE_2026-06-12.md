# R-D Bridge Anatomy: Pinching Is Idempotent, the Supplied Flow Is Agreement-Conditioned Double Registration, and One Statistics Atom Remains (Bounded Note)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. This note proves the
bounded algebraic anatomy below and names one unresolved statistics atom. It
does not set or predict an audit outcome, adopt R-D, fix `r`, or edit any
registry or audit data file.
**Status authority:** audit status remains set only by the independent audit
lane. This file is not status authority for any premise, registry row, or
promotion decision.
**Primary runner:** `scripts/frontier_rd_bridge_anatomy_agreement_conditioning_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_rd_bridge_anatomy_agreement_conditioning_2026_06_12.txt`
**No-promotion statement:** this note does not promote, demote, retire, route,
or adopt any premise. R-D remains proposed; the statistics atom is named, not
consumed.

## Boundary

This note proves G1 and G2 and names the G3 atom. The atom is named, not
discharged. The note does not adopt R-D, does not import a probability rule,
does not discharge the statistics atom, does not select a cell, and does not
fix `r`.

The weight bookkeeping used below is a reconstruction-level device per
guardrail G3 of the record principle: Record supplies outcome structure and
explicitly does not supply weighting, normalization, probability, or an
occupancy rule. The bookkeeping is therefore stated conditionally, not
imported as a probability law.

## The Supplied Surface

Work on the supplied 2-sector surface with orthogonal projectors

```text
P_s = diag(1, 0, 0),   P_d = diag(0, 1, 1),   P_s + P_d = I.
```

The sector split is the supplied singlet/doublet partition. The supplied
bookkeeping is

```text
(p_s, p_d) = (a^2, 2|b|^2)
```

up to common normalization, with `r = |b|^2/a^2`, so `p_d/p_s = 2r`. The
`(1,2)` weighting is only the component count of the supplied
singlet/doublet split.

## Theorem

**(G1) Naive route trivial: pinching is idempotent.** Define the canonical
registration map

```text
D(M) = P_s M P_s + P_d M P_d.
```

For every generic symbolic `3 x 3` matrix `M`, direct computation gives
`D(D(M)) = D(M)` entrywise [check 1]. The induced weights
`p_i = Tr(P_i rho P_i)` are unchanged under a second application of `D` on a
generic diagonal-plus-offdiagonal `rho` [check 2]. Therefore re-registration
modeled as re-pinching induces the identity on the weight bookkeeping. The
R-D flow cannot arise as naive re-pinching [check 8].

**(G2) The supplied flow is agreement-conditioned double registration.** If a
second registration of the same partition composes independently on the
bookkeeping and the retained cases are conditioned on agreement of the two
outcomes, then

```text
p_i' = p_i^2 / (p_s^2 + p_d^2).
```

In the coordinate `x = p_d/p_s`, this is exactly `x -> x^2` [check 3]. With
`x = 2r`, the same identity is exactly

```text
r -> 2r^2
```

in both algebraic directions [check 4]. Reading the same identity backward
gives `x -> sqrt(x)`, hence

```text
g(r) = sqrt(r/2),
```

the retained inverse direction [check 5]. The finite fixed points are
`r = 0` and `r = 1/2`, with the projective doublet endpoint also fixed
[check 6].

**(G3) The remaining atom.** Therefore the R-D bridge premise,
"re-registration composes by a member of the retained flow family", reduces
on this surface to one named statistics atom:

```text
independent composition of repeated registration on the weight bookkeeping.
```

Agreement-conditioning then forces the retained map [check 7]. The atom is a
statistics-layer statement. A perfectly correlated second registration gives
`p_i' = p_i` instead, so the atom does real work and is not a restatement of
pinching idempotence [check 7]. The Born/unraveling assembly chain is the
framework lane positioned to discharge this kind of atom; it is context here,
unaudited for this use, and not consumed.

## Consequence

Combined with the named companion pieces
`RD_FIXEDNESS_IS_ARROW_INVARIANT_ON_THE_RETAINED_FLOW_FAMILY_BOUNDED_NOTE_2026-06-12.md`
and
`CORNER_MODE_SET_FORK_RESOLUTION_LAYER_IS_RECORD_DYNAMICS_BOUNDED_NOTE_2026-06-12.md`,
and with the OO/R-D realization equivalence context, the occupancy lane's
remaining open content is:

- this single statistics atom;
- the coarse-graining prong, custody selector (i);
- the durability-to-weight coupling as stated by the R-D chain.

Each is named. None is resolved here. The route is live.

## Does NOT

- Does not discharge the statistics atom; the atom is named, not discharged.
- Does not adopt R-D; R-D stays proposed.
- Does not import a probability rule.
- Does not force `r` or select an occupancy cell.
- Does not consume the Born/unraveling assembly lane.
- Does not collapse the coarse-graining prong or durability-to-weight
  coupling.
- The occupancy binary stays open.

## Dependencies

- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
  - the retained sharpening map G2 identifies.
- [`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)
  - the retained inverse direction.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  - the Record boundary. It supplies no weighting, normalization,
  probability, or occupancy rule; this is why the atom is an atom.

## Context

Backticked only, not load-bearing:

- `KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  - the R-D chain note.
- `KOIDE_OCCUPANCY_DURABILITY_PREMISE_EQUIVALENCE_ON_REGISTERED_SURFACE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  - the OO/R-D realization equivalence context.
- `RD_FIXEDNESS_IS_ARROW_INVARIANT_ON_THE_RETAINED_FLOW_FAMILY_BOUNDED_NOTE_2026-06-12.md`
  - fixedness/arrow-invariance companion context.
- `CORNER_MODE_SET_FORK_RESOLUTION_LAYER_IS_RECORD_DYNAMICS_BOUNDED_NOTE_2026-06-12.md`
  - registration-blind fork companion context.
- `RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
  - canonical record-principle context.
- `UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  - the Born/unraveling assembly lane positioned to discharge the atom, named
  as context, unaudited for this use, and not consumed.

## Verification

Run:

```bash
python3 scripts/frontier_rd_bridge_anatomy_agreement_conditioning_2026_06_12.py
```

Expected: at least 14 `[PASS]` lines, `FAIL=0`, a no-git local
diff-stat-style new-file inventory, and a `SUMMARY` line. Exit code is zero
iff every check passes.
