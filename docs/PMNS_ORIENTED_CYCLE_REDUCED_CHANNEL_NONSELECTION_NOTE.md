# PMNS Oriented Cycle Reduced-Channel Nonselection

**Date:** 2026-04-16  
**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_pmns_oriented_cycle_reduced_channel_nonselection.py`
**Primary runner:** `scripts/frontier_pmns_oriented_cycle_reduced_channel_nonselection.py`

## Inputs

This note depends on:

- [PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md](./PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md)
- [PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md](./PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
- [PMNS_ACTIVE_FOUR_REAL_SOURCE_FROM_TRANSPORT_NOTE.md](./PMNS_ACTIVE_FOUR_REAL_SOURCE_FROM_TRANSPORT_NOTE.md)

The selection-structure note supplies the displayed residual antiunitary map
that pins the reduced matrix family to
`(u, v, w) <-> (u + i v, w, u - i v)`. The stable-path cycle-coordinate note
supplies only the bounded algebraic identity
`(c_1, c_2, c_3) = diag(A C^dagger)` for a supplied `3 x 3` block. The
response construction used below is a target-constructed fixture round trip
and is consistency-only, not independent physical realization evidence.

## Question

On the explicitly supplied graph-first-symmetric oriented-cycle family, do
residual symmetry, coordinate extraction, and a target-constructed fixture
select the remaining cycle values?

## Answer

No.

On the explicitly supplied reduced matrix family:

- the residual symmetry reduction is an exact matrix identity;
- the bounded coordinate extractor returns `(u,v,w)` exactly;
- the coordinate map itself does not select a unique point.

This note does not use the coordinate extractor as a physical observable or
Record readout.

The exact reduced family is

`A_fwd(u,v,w) = (u + i v) E_12 + w E_23 + (u - i v) E_31`

and every point of that `3`-real family:

- satisfies the residual antiunitary symmetry
  `A_fwd = P_23 A_fwd^dagger P_23`
- has its coordinates extracted exactly by the bounded algebraic lemma
- can be round-tripped through a target-constructed response fixture as a
  consistency check

The fixture round trip does not prove physical realization or current-bank
exhaustiveness.

## Exact chain

### 1. Reduced graph-first family

The graph-first selected-axis route reduces the oriented cycle channel to the
`3`-real family

`(u,v,w) <-> (c_1,c_2,c_3) = (u + i v, w, u - i v)`.

Equivalently,

- `c_1 = conjugate(c_3)`
- `c_2` real

### 2. Exact algebraic coordinate extraction on the reduced family

For a supplied block, the bounded coordinate-extraction lemma gives

`(c_1,c_2,c_3) = diag(A C^dagger)`.

So on the reduced family, the remaining real coordinates are read exactly as

- `u = Re(c_1)`
- `v = Im(c_1)`
- `w = Re(c_2)`

No further projection ambiguity remains.

### 3. Target-constructed response round trip

For any reduced-channel point `(u,v,w)`, the active block

`A = xbar I_3 + A_fwd(u,v,w)`

is encoded into a spectator-extended fixture, converted to response columns,
and recovered by inverting that same construction.

This is a consistency-only round trip because the fixture is constructed from
the target `A`. It is not an independent lower-level derivation of `A`, a
physical carrier, or a Record-compatible readout.

### 4. Nonselection theorem

There exist distinct reduced-channel points `(u,v,w) != (u',v',w')` such that:

- both satisfy the graph-first residual antiunitary symmetry
- both sit on the specified diagonal-plus-forward-cycle support
- both have different algebraically extracted coordinate tuples
- both can be passed through the same target-constructed consistency fixture

Therefore coordinate extraction does not select a unique reduced-channel
value. A broader current-bank nonselection theorem requires separate retained
carrier, readout, realization, and exhaustiveness premises.

## Consequence

The coordinate tuple is bounded algebraic data on a supplied matrix, not a
physical observable supplied by this row. The retained carrier,
Record-compatible readout, and matrix/value-selection bridges remain open.

## Boundary

This is not a positive value-selection theorem.

It is an algebraic nonselection check for the explicitly supplied reduced
matrix family. The response fixture is consistency-only.

## Command

```bash
python3 scripts/frontier_pmns_oriented_cycle_reduced_channel_nonselection.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [pmns_oriented_cycle_channel_value_law_note](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
