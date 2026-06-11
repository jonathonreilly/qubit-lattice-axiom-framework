# Theta P2 K/CPT Determinant-Character Phase Erasure: Bounded Candidate Route

**Date:** 2026-06-10 (split from
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
so the strong-CP mass-orientation route stands on the theta surface alone,
with no dependency on the `AC_phi_lambda` staggered gate)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry.
**Primary runner:** [`scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py`](../scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py)
**Runner cache:** [`logs/runner-cache/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.txt`](../logs/runner-cache/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.txt)

## Boundary

This note proves one bounded fact:

1. In a supplied determinant-class readout whose scalar readouts are the
   standard continuous multiplicative determinant characters
   `|z|^s exp(i k arg z)`, K/CPT invariance kills the determinant phase
   character: `k = 0`.

It does not discharge the strong-CP mass-orientation premise by itself,
derive the strong-CP action-form premise, or change
`docs/audit/data/tier_a_admissions.json`. Those moves require later
registry/audit handling and the missing bridge named below.

## Determinant Readout Lemma

The Record axiom supplies durable realized-outcome readout only after a
readout context, finite central-sector decomposition, and fixed K/CPT
conjugation are already supplied. It does not supply the determinant readout
context.

Given such a supplied determinant-class context, the standard multiplicative
determinant character family has phase part

```text
chi_k(z) = exp(i k arg z).
```

K/CPT conjugation sends `z` to `conj(z)`, so `arg z` goes to `-arg z`.
Requiring the character to be invariant under that conjugation gives

```text
exp(i k phi) = exp(-i k phi) for all phi,
```

hence `sin(k phi) = 0` for all `phi`, so `k = 0`. Therefore the invariant
members of this determinant-character family are phase-free functions of
`|det|`.

The hostile guard is important: K/CPT orbit invariance alone gives evenness,
not phase erasure. For example `cos(arg z)` is K-invariant and still depends
on the phase. The phase-erasure conclusion applies only inside the supplied
multiplicative determinant-character class.

## Named Open: The Determinant-Readout Bridge

This lemma is a candidate route for the mass-orientation part of the
strong-CP surface, not a completed discharge. To discharge that premise, a
later retained bridge must show that the physical `arg det(M_u M_d)`
contribution used by
[`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) is exhausted
by this determinant-class registrable readout, and that no phase-sensitive
non-multiplicative or action-level datum remains relevant to that premise.
Until that bridge exists, the positive-real mass orientation remains an
explicit condition of the strong-CP selected surface.

## Registry Consequence

The only supported consequence is a candidate route for future Tier-A
registry review: the determinant lemma may help remove the positive-real
mass-orientation condition of the strong-CP selected surface only after the
determinant-readout bridge above is retained.

No new axiom, primitive, admission, normalization, probability rule,
comparator, or audit verdict is introduced here.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the
  narrow Record axiom boundary.
- [`STRONG_CP_THETA_ZERO_NOTE.md`](STRONG_CP_THETA_ZERO_NOTE.md) for the
  selected-surface strong-CP premise whose mass-orientation part is the
  candidate target here.

The `AC_phi_lambda` orientation lemma that previously shared a note with
this lemma remains in
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
(context, not load-bearing here: this lemma uses nothing from the staggered
gate surface).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only
status authority.
