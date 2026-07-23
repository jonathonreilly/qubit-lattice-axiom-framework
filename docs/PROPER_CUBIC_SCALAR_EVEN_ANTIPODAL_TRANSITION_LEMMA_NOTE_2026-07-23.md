# Proper-Cubic Scalar–Even Antipodal Transition Lemma

Date: 2026-07-23

Claim type: positive_theorem

Runner: [`scripts/frontier_proper_cubic_scalar_even_antipodal_transition_lemma_2026_07_23.py`](../scripts/frontier_proper_cubic_scalar_even_antipodal_transition_lemma_2026_07_23.py)

Runner cache: [`logs/runner-cache/frontier_proper_cubic_scalar_even_antipodal_transition_lemma_2026_07_23.txt`](../logs/runner-cache/frontier_proper_cubic_scalar_even_antipodal_transition_lemma_2026_07_23.txt)

## Claim

Let the six directed nearest-neighbor labels be paired by reversal, and let

```text
P_s = |s><s|,
P_e = (I + R)/2 - P_s,
P_v = (I - R)/2,
```

where `R` reverses each directed edge and
`|s> = (1,1,1,1,1,1)/sqrt(6)`.  For any real `beta` for which
`tan(beta/2)` is finite, define

```text
C(beta) = exp[-i tan(beta/2)]
          (P_s - P_e + exp(i beta) P_v).
```

Choose any normalized `|e>` in the even subspace and set

```text
|+> = (|s> + |e>)/sqrt(2),
|-> = (|s> - |e>)/sqrt(2).
```

Then

```text
C(beta)|+> = exp[-i tan(beta/2)] |->,
C(beta)|-> = exp[-i tan(beta/2)] |+>.
```

The same identities hold after every proper-cubic reorientation of `|e>`.
Consequently the scalar–even two-dimensional subspace has a projective
period-two recurrence under this supplied coin family.

## Proof

The three displayed projectors are mutually orthogonal and sum to the
identity.  The vectors `|s>` and `|e>` therefore have coin eigenvalues
`exp[-i tan(beta/2)]` and `-exp[-i tan(beta/2)]`, respectively.  Substitution
into the definitions of `|+>` and `|->` gives the two swap identities.

A proper-cubic direction permutation fixes `|s>` and preserves all three
projectors.  It sends `|e>` to another normalized vector in the even
subspace, so the same two-line calculation applies in every frame.

## Verification

The runner:

- constructs the reversal projectors independently and verifies their
  Hermitian, idempotent, orthogonal resolution of the six-dimensional space;
- verifies the scalar/even eigenvalue argument and the resulting swap, inverse,
  and square identities over train and held `beta` values;
- compares the independently constructed matrix against the existing
  [`common_matter_field_coin_family_cycle219_2026_07_16.py`](../scripts/common_matter_field_coin_family_cycle219_2026_07_16.py)
  implementation;
- checks the transported identity for all 24 proper-cubic frames using
  [`proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py`](../scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py);
  and
- includes a mutation control in which the even-sector phase is moved away
  from `-1`, causing the exact swap gate to fail.

The implementation comparison is a regression check, not a premise of the
proof.

## Import and support inventory

- The projector decomposition and the displayed matrix family are explicit
  hypotheses of this finite-dimensional theorem.
- The phase coordinate `beta`, its selection, and any physical interpretation
  are not derived here.
- Proper-cubic reorientation uses finite direction-permutation matrices; it
  adds no dynamical or observational input.
- No measured, fitted, literature, normalization, or empirical value is used.

## Scope

This is a conditional algebraic lemma about one supplied six-dimensional coin
family.  Projective recurrence is not a clock, a duration, a rate, an energy,
a framework Record, an occurrence law, or proper time.  The lemma supplies no
preparation, transport, readout, calibration, state-selection, or probability
rule.  Those physical bridges remain separate questions.

The independent audit lane assigns any audit or effective status.
