# PMNS Oriented Cycle Selection Structure

**Date:** 2026-04-16 (2026-05-18: claim_scope formalized as bounded
conditional algebraic reduction of the oriented-cycle channel; 2026-05-19:
admitted-context boundary recorded; 2026-05-25: raw-matrix repair narrows
the row to the finite matrix identities alone).
**Claim type:** bounded_theorem
**Claim scope (2026-05-25 raw-matrix repair):** the claim is exactly the
three finite matrix identities below, with no physical carrier, no native
observable/value law, and no graph-derived interpretation imported into
the row.
**Status authority:** independent audit lane only.
**Status:** support - structural or confirmatory support note
**Primary runner:** `scripts/frontier_pmns_oriented_cycle_selection_structure.py`

## Raw Matrix Identities

This row is a raw-matrix repair. It uses only the named `3 x 3` matrices
and linear maps displayed here:

- `C = E_12 + E_23 + E_31`;
- `I_3`, the `3 x 3` identity matrix;
- `P_23`, the permutation matrix swapping basis vectors `2` and `3`;
- the forward-cycle subspace
  `A_fwd(c) = c_1 E_12 + c_2 E_23 + c_3 E_31`;
- the prescribed swap-conjugation map
  `S(A) = P_23 A^dagger P_23`.

The row proves only these finite identities.

1. Conjugation by `C` cyclically permutes the coefficients of
   `A_fwd(c)`:

   `(c_1, c_2, c_3) -> (c_2, c_3, c_1)`.

   Therefore the exact `C_3` fixed locus in this subspace is
   `c_1 = c_2 = c_3 = sigma`, equivalently `A_fwd = sigma C`.

2. On the specified identity matrix `I_3`, the forward-cycle coefficients
   are all zero. Hence `sigma = 0` for this specified identity input.

3. On the prescribed map `S(A) = P_23 A^dagger P_23`, the fixed locus
   inside the forward-cycle subspace is exactly
   `c_1 = conjugate(c_3)` and `c_2` real. A generic complex coefficient
   triple is not fixed by this map.

## Explicit Non-Claims

This row does not claim the carrier or native observable/value law.

It does not claim that the specified identity block is any physical
free-point block.

It does not claim that graph-first induces the prescribed swap-conjugation map.

The carrier and observable law remain outside this repaired row.

The row also does not claim a PMNS value-selection theorem, a PMNS angle
prediction, a physical mixing law, or any derivation from primitives. The
result is a bounded finite-dimensional algebra lemma about the displayed
matrices and maps.

## Question

Given the displayed cycle subspace and the displayed involutive
swap-conjugation map, what exact finite matrix structure follows?

## Answer

Three exact statements follow:

- exact `C_3` covariance collapses the displayed cycle subspace to one
  complex slot `sigma C`;
- at the specified identity input, `sigma = 0`;
- the prescribed swap-conjugation map reduces the displayed cycle subspace
  to the `3`-real fixed family
  `c_1 = conjugate(c_3)`, `c_2 real`.

## Exact Chain

### 1. Exact `C_3` covariance

Write

`A_fwd = c_1 E_12 + c_2 E_23 + c_3 E_31`.

Conjugation by the displayed cycle matrix `C` sends the coefficient triple
to

`(c_1, c_2, c_3) -> (c_2, c_3, c_1)`.

The fixed locus of this cyclic permutation is

`c_1 = c_2 = c_3 = sigma`,

equivalently

`A_fwd = sigma C`.

### 2. Specified identity input

For the specified matrix `I_3`, the entries in the `E_12`, `E_23`, and
`E_31` slots are all zero. Its forward-cycle coefficient triple is

`(0, 0, 0)`.

Therefore the specified identity input gives `sigma = 0` on the exact
`C_3` fixed locus.

### 3. Prescribed swap-conjugation map

For the prescribed finite map

`S(A) = P_23 A^dagger P_23`,

direct matrix multiplication gives the fixed-locus conditions

- `c_1 = conjugate(c_3)`;
- `c_2` real.

Thus the prescribed map reduces the displayed cycle subspace from three
complex coefficients to three real parameters:

- `Re c_1`;
- `Im c_1`;
- `c_2`.

## Consequence

The finite algebra is complete, but its interpretation is deliberately
narrow. Any future PMNS value-selection theorem would have to supply the
carrier, native observable/value law, and bridge from a physical route to
the displayed matrices. Those are not part of this row.

## Boundary

This is a bounded finite matrix lemma. It closes only the three runner
checks listed in `Raw Matrix Identities`:

- the `C_3` fixed-locus identity;
- the zero forward-cycle coefficients of the specified identity matrix;
- the fixed locus of the prescribed `P_23` swap-conjugation map.

No audit verdict is applied by this source edit. The independent audit
lane owns the final status.

## Command

```bash
python3 scripts/frontier_pmns_oriented_cycle_selection_structure.py
```

## Audit Repair Record

Earlier audits accepted the raw finite-dimensional algebra but blocked
full retention because the source prose also carried physical readings:
the carrier/native law, the physical identity-block interpretation, and a
graph-first-to-swap-conjugation bridge. This 2026-05-25 repair takes the
alternate re-audit path: keep only the raw matrix identities and exclude
those readings from the claim.

The source row is therefore ready for re-audit as a dependency-free
bounded matrix theorem.
