# Tier-A K/CPT Determinant And Orientation Invariance: Bounded Candidate Route

**Date:** 2026-06-09
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry.
**Primary runner:** [`scripts/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.py`](../scripts/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.py)
**Runner cache:** [`logs/runner-cache/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.txt`](../logs/runner-cache/frontier_tier_a_korbit_determinant_orientation_invariance_2026_06_09.txt)

## Boundary

This note preserves a useful algebraic route without claiming the Tier-A
registry has already changed.

It proves two bounded facts:

1. In a supplied determinant-class readout whose scalar readouts are the
   standard continuous multiplicative determinant characters
   `|z|^s exp(i k arg z)`, K/CPT invariance kills the determinant phase
   character: `k = 0`.
2. For the `AC_phi_lambda` circulant gate used in the staggered-Dirac
   realization lane, conjugation maps `delta` to `-delta`, while the unordered
   spectrum is invariant under that flip.

It does not discharge the strong-CP mass-orientation premise by itself, strip
the `AC_phi_lambda` admission by itself, derive `|delta| = 2/9`, derive the
strong-CP action-form premise, or change `docs/audit/data/tier_a_admissions.json`.
Those moves require later registry/audit handling and any missing bridge named
below.

## Determinant Readout Lemma

The Record axiom supplies durable realized-outcome readout only after a readout
context, finite central-sector decomposition, and fixed K/CPT conjugation are
already supplied. It does not supply the determinant readout context.

Given such a supplied determinant-class context, the standard multiplicative
determinant character family has phase part

```text
chi_k(z) = exp(i k arg z).
```

K/CPT conjugation sends `z` to `conj(z)`, so `arg z` goes to `-arg z`. Requiring
the character to be invariant under that conjugation gives

```text
exp(i k phi) = exp(-i k phi) for all phi,
```

hence `sin(k phi) = 0` for all `phi`, so `k = 0`. Therefore the invariant
members of this determinant-character family are phase-free functions of
`|det|`.

This is a candidate route for the mass-orientation part of the strong-CP
surface, not a completed discharge. To discharge that premise, a later retained
bridge must show that the physical `arg det(M_u M_d)` contribution used by
[`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) is exhausted by
this determinant-class registrable readout, and that no phase-sensitive
non-multiplicative or action-level datum remains relevant to that premise.
Until that bridge exists, the positive-real mass orientation remains an explicit
condition of the strong-CP selected surface.

The hostile guard is important: K/CPT orbit invariance alone gives evenness,
not phase erasure. For example `cos(arg z)` is K-invariant and still depends on
the phase. The phase-erasure conclusion applies only inside the supplied
multiplicative determinant-character class.

## `AC_phi_lambda` Orientation Lemma

For the circulant gate surface used by
[`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md),
write the relevant Hermitian circulant as

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T.
```

Complex conjugation sends this matrix exactly to `H(-delta)`. The elementary
symmetric polynomials of the three eigenvalues agree at `delta` and `-delta`;
the flip permutes the eigenvalue labels by `k -> -k`.

Therefore, conditional on the registrable species surface being exactly the
unordered mass multiset and on the `k -> -k` relabel being convention, the sign
of `delta` is not extra registrable content. The even datum, equivalently
`cos(3 delta)` or `|delta|` on the chosen fundamental domain, is the remaining
candidate atom.

This does not derive the magnitude `|delta| = 2/9`. It also does not rule out a
future orientation-sensitive bridge if the registrable surface is enlarged
beyond the unordered multiset.

## Registry Consequence

The only supported consequence is a candidate route for future Tier-A registry
review:

- strong-CP theta: the determinant lemma may help remove the positive-real
  mass-orientation condition only after the determinant-readout bridge above is
  retained;
- `AC_phi_lambda`: the orientation lemma may help reduce the admission to a
  magnitude-only atom only after the unordered-multiset registrability bridge is
  retained or confirmed as already supplied by existing audited surfaces.

No new axiom, primitive, admission, normalization, probability rule, comparator,
or audit verdict is introduced here.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the narrow
  Record axiom boundary.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) for the
  selected-surface strong-CP premise whose mass-orientation part is only a
  candidate target here.
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  for the determinant-orbit context.
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  for the `AC_phi_lambda` gate context.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status
authority.
