# Truncated-Fock equal-split recoil bookkeeping support

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional support

Claim type: bounded_theorem

Runners:

- [`frontier_truncated_fock_equal_split_support_2026_07_28.py`](../scripts/frontier_truncated_fock_equal_split_support_2026_07_28.py)
- [`frontier_truncated_fock_equal_split_independent_check_2026_07_28.py`](../scripts/frontier_truncated_fock_equal_split_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, framework
primitive, registry, policy, audit result, or audit status.

## Result

On the explicitly supplied two-cell slice
`n_left,n_right <= 2`, the six-mode local hop preserves matter occupation
number and admits the conditional recoil ledger

```text
Delta P_matter = -2 d
P_component_1 = +d
P_component_2 = +d
```

when the equal two-component split is supplied. The certificate derives:

- local matter-mask counts `1 / 6 / 15` and active-channel counts
  `0 / 6 / 24` for `n = 0 / 1 / 2`;
- exact number preservation and zero cross-layer amplitude over
  `2 * 7 * 22^2 = 6,776` endpoint/q/two-cell columns;
- the conditional layer-1 transition weight
  `sin(0.8 * 3 * tan(0.15))^2 = 0.12589921612871374`;
- fixed-basis transpose symmetry in each certified number block and for
  real-bilinear superpositions;
- sensitivity of the number commutator to a deliberate `n=2 -> n=1`
  mutation, with Frobenius norm `sqrt(2)`.

This is a finite algebraic support result for a future physical input port.
It is not that port.

## Exact supplied fixture

The package is self-contained. Its supplied conditions are:

- six ordered directional modes
  `(+x,-x,+y,-y,+z,-z)`, paired by reversal;
- the canonical six-mode CAR hop
  `c_dagger(reverse(d)) c(d)` between a reservoir q state and a directional
  q state;
- the two-cell cutoff `n_left,n_right <= 2`;
- `beta = -0.3`, the dimensionless coupling `0.8`, and the fixture angle
  `theta = 0.8 * 3 * tan(-beta/2)`;
- a directional q-state total ledger weight `2d`;
- the equal split `(1,1)` of that total into two bookkeeping components.

The scripts contain these values and definitions directly; they do not import
the historical Cycle-320 or Cycle-322 implementation closure.

## What is derived and what is conventional

The matter recoil, channel counts, number preservation, transition weights,
truncated enumeration, and transpose symmetry are derived from the supplied
fixture.

The equal split is not selected by conservation. For every real `alpha`,

```text
P_component_1 = alpha d
P_component_2 = (2-alpha) d
```

has the same conserved total. The runners explicitly exercise unequal values
of `alpha`; `(1,1)` remains a named supplied condition.

The optional names `(F_d,A_d)` for the two components are kept on the
non-authoritative meta surface
`TRUNCATED_FOCK_COMPONENT_NAMING_NOTE_2026-07-28.md`. Those names are
not a theorem premise and do not assert distinct carrier degrees of freedom.

## Scope boundary

The complete six-mode Fock space contains 64 local masks in layers
`n=0,...,6`; its corresponding two-cell endpoint/q enumeration would contain
`2 * 7 * 64^2 = 57,344` columns. This package certifies only the 22-mask
`n<=2` slice and makes no all-layer claim.

The package also makes no claim about a separately constructed auxiliary
state, a two-endpoint physical seam port, AB/BA intertwining, contact
preservation, simultaneous-source response, source selection, calibration,
or gravity. Fixed-basis transpose symmetry is not promoted to an arbitrary
complex bra/ket reciprocity statement.
