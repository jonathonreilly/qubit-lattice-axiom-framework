# Occupancy Atom Is the Outcome Dictionary; the Conditioned Flow Selects Outcome Equipartition Invariantly

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict, and it does not edit the
audit-lane-owned Tier-A registry or any audit data file.
**Primary runner:** `scripts/frontier_occupancy_atom_outcome_dictionary_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_occupancy_atom_outcome_dictionary_2026_06_12.txt`

## Boundary

This note proves the four statements below on the supplied 2-outcome
registered surface. It does not discriminate the fork, select a cell, fix `r`,
correct any landed note, or resolve the dictionary. The `(1,2)` and `(1,1)`
weightings are both stated as supplied bookkeeping conventions.

FIREWALL: no fork branch or occupancy cell is discriminated or selected here.
The conditioned-flow route cannot by itself discriminate between them; `r` is
never fixed by the route alone. The landed R-D chain is sharpened by making its
conditionality explicit, not contradicted; this is not a correction. The
occupancy binary stays open. This is a sharpening, not a correction.

## The Supplied Surface

In the supplied readout context, the Record axiom names the outcome object,
not the weight attached to it:
"Given a readout context with a finite central-sector decomposition and a fixed
`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized
central sector."

Record does not supply the readout context, central-sector decomposition,
`K`/CPT structure, weighting, normalization, probability rule, measurement
dynamics, or occupancy rule used on this supplied surface.

On the supplied surface, the two registered outcomes are the singlet outcome
`s` and the doublet `K`-orbit outcome `d`. Write the outcome-weight ratio as
`x = p_d/p_s`. The agreement-conditioned double-registration update squares
registered weights and renormalizes, hence

```text
x' = (p_d^2/Z)/(p_s^2/Z) = (p_d/p_s)^2 = x^2.
```

Two bookkeeping dictionaries are stipulated:

- Component dictionary `(1,2)`: `x = 2r`. The doublet outcome carries two
  components, so `p_d = 2|b|^2` and `p_s = a^2`.
- Slot dictionary `(1,1)`: `x = r`. There is one slot per outcome at equal
  per-slot weight.

## Theorem

**Invariant selection.** For any bookkeeping dictionary
`x = phi(r)` with `phi` a strictly monotone bijection on the relevant domain,
the flow in `r`-coordinates is

```text
r -> phi^{-1}(phi(r)^2).
```

The fixed-point equation is `phi(r) = phi(r)^2`, so the outcome-space fixed
values are `phi(r) in {0,1}`. The interior fixed point is therefore
`r* = phi^{-1}(1)`. The invariant selection is `x = 1`, i.e. outcome
equipartition: equal registered weight on `s` and `d`. This statement is
independent of the dictionary. `[checks 1-4]`

For the two explicit dictionaries, the maps are:

- `x = 2r`: `r -> (2r)^2/2 = 2r^2`, with finite fixed set `{0, 1/2}`.
- `x = r`: `r -> r^2`, with finite fixed set `{0, 1}`.

**Dictionary-as-atom.** Under the component dictionary `x = 2r`,
the invariant selection `x = 1` reads `r* = 1/2`, the orbit cell. Under the
slot dictionary `x = r`, the same invariant selection reads `r* = 1`, the
sector cell. Re-solving in each coordinate gives exactly `{0, 1/2}` versus
`{0, 1}`, with the projective doublet endpoint represented by `s = 1/r = 0`
in both charts. The two occupancy cells are the two dictionaries' readings of
the same outcome-space selection. `[checks 5-6]`

**Tri-guise identity on the supplied labels.** The dictionary choice is the
same two-label bookkeeping choice written three ways:

- Supplied kernel-normalization bookkeeping: the doublet Berezin block scales as
  `det(lambda K) = lambda^k det(K)`, so the two block conventions carry the
  lambda-exponent pair `{2, 1}` for `2x2` versus `1x1` blocks.
- Supplied corner mode-set bookkeeping: the two doublet weights are `Z_d = 2pi/g` and
  `Z_d = pi/g`.
- Supplied flow coordinate: the dictionary pair is `x = 2r` and `x = r`.

The pairwise bijections are explicit. The supplied rho-map orientation is
`rho = (pi/g)/Z_d`, `r = 1/(2 rho)`. Thus `Z_d = pi/g` gives `rho = 1` and
`r = 1/2`, matching the component dictionary's fixed-point reading
`x = 2r`; `Z_d = 2pi/g` gives `rho = 1/2` and `r = 1`, matching the slot
dictionary's fixed-point reading `x = r`. The kernel exponent labels map to
the same two dictionary labels by block size. The composed maps agree with the
direct maps, so the three two-element descriptions form the same binary, not
three independent binaries. `[checks 7-8]`

**Consequence stated with care.** The conditioned-flow route selects
outcome equipartition invariantly and therefore cannot by itself discriminate
between the occupancy cells. In `x`-space both dictionaries select `x* = 1`;
only after a dictionary is supplied do the `r`-readings differ. The landed R-D
chain's reading of the fixed point as `r = 1/2` is conditional on the
component dictionary supplied in that chain. This sharpens its conditionality
and is fully consistent with its own stated side conditions; it is not a
correction. On this supplied surface, the occupancy atom is the
outcome-to-component dictionary: one binary appearing identically in the
measure, the Fock bookkeeping, and the flow coordinate. `[checks 9-11]`

## Consequence

For this bounded source lane, the remaining open content is a supplied
dictionary choice, the statistics atom `wave-8a`, and the durability-to-weight
coupling. The bijections exhibited here show how a future resolution of one
guise would propagate across the supplied labels. Nothing here resolves any of
them; the route is live.

## Does NOT

- Does not discriminate either fork branch.
- Does not select either occupancy cell.
- Does not fix `r`.
- Does not correct any landed note.
- Does not contradict the landed R-D chain.
- Does not resolve the dictionary.
- Does not close the occupancy binary; the occupancy binary stays open.

## Dependencies

- [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
- [`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

Context only, reproven inline here or in the runner: `wave-8a anatomy note`,
`R-D chain note`, `independence note`, `rho-map`, `wave-4 companion`,
`wave-6 companion`, `wave-7b companion`.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
