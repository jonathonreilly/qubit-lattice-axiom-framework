# Wilson Plus Staggered Minimal-Block Spectrum Bridge

**Date:** 2026-06-13
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; source-note bridge for
review/audit, not an audit verdict.
**Runner:** `scripts/frontier_wilson_staggered_minimal_block_spectrum_bridge_2026_06_13.py`

## Question

The Wilson-corrected `V_taste` note needs the combined Wilson-plus-staggered
minimal-block spectrum on the same APBC corner surface. The staircase note
derives the Wilson shift `2 r hw(n)`. The Higgs mean-field runner derives the
unshifted staggered conjugate pair `+/- 2 i u_0`. This bridge constructs the
combined operator and verifies that those two facts compose on the same
corner labels.

## Construction

Let the APBC minimal-block corner set be

```text
n = (n_t, n_x, n_y, n_z) in {0,1}^4.
```

For each corner, use the real two-plane representation of the staggered
conjugate pair:

```text
J(u_0) = [[0, -2 u_0],
          [2 u_0, 0]]
```

with eigenvalues `+/- 2 i u_0`. Add the Wilson shift on the same corner label:

```text
W(n) = 2 r hw(n),
O_n(r,u_0) = W(n) I_2 + J(u_0).
```

The combined minimal-block bridge operator is the direct sum

```text
O_Wstag(r,u_0) = direct_sum_{n in {0,1}^4} O_n(r,u_0).
```

This is a spectral/corner-basis construction on the same APBC minimal-block
surface, not a new physical input. The two-plane is just the real form of the
staggered `+/-` pair.

## Theorem

For every corner `n`, the block `O_n` has characteristic polynomial

```text
(lambda - 2 r hw(n))^2 + 4 u_0^2
```

and eigenvalues

```text
lambda_n^+/- = 2 r hw(n) +/- 2 i u_0.
```

Grouping by Hamming weight gives the multiset

```text
{ 2 r k +/- 2 i u_0 with multiplicity binomial(4,k), k = 0,...,4 }.
```

Equivalently,

```text
det(m I + O_Wstag)
  = product_{k=0}^4 ((m + 2 r k)^2 + 4 u_0^2)^{binomial(4,k)}.
```

Therefore the half-log convention used by the Wilson-corrected `V_taste`
formula gives

```text
V_taste^W(m)
  = -(1/2) sum_{k=0}^4 binomial(4,k)
       log((m + 2 r k)^2 + 4 u_0^2).
```

## Boundaries

This bridge does not derive the Wilson coefficient `r`, the plaquette
mean-field value `u_0`, the physical Higgs mass, the Wilson-shifted extremum,
the staggered-Dirac realization gate, or any continuum-limit claim. It only
closes the finite combined-spectrum step on the APBC minimal-block surface.

## Dependencies

- [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
  -- supplies the APBC corner labels and Wilson shift `2 r hw(n)`.
- [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md)
  -- supplies the unshifted staggered mean-field conjugate pair `+/- 2 i u_0`
  used here as an input.

## Verification

Run:

```bash
python3 scripts/frontier_wilson_staggered_minimal_block_spectrum_bridge_2026_06_13.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
```
