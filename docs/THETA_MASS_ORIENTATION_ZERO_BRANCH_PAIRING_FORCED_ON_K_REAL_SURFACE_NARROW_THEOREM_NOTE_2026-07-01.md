# Theta Mass-Orientation Zero Branch Is Pairing-Forced on the K-Real Staggered Surface

**Date:** 2026-07-01
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** on the supplied staggered-only Case-A surface (real
antisymmetric `M_KS` with bipartite `ε`-grading, any tested real/Z2 gauge
background) with real scalar mass or a supplied Hermitian generation mass
operator on the flavor tensor factor, the mass-side determinant satisfies
`det ≥ 0` for EVERY real mass value and every real Hermitian flavor spectrum —
including negative masses and negative signed-Brannen roots — so the discrete
mass-orientation `arg det ∈ {0, π}` collapses to the `0` branch structurally,
with no residual sign freedom and no use of the positive-mass convention.
Refutation legs: breaking the antisymmetric pairing (real symmetric
perturbation) produces `det < 0` at real mass; a non-K-real (non-Hermitian)
flavor block leaves `{0, π}` entirely. No claim about `theta_gauge`, Wilson
surfaces, non-commuting flavor-kinetic couplings, the physical
determinant-channel identification, or Tier-A registry status.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit any audit-owned registry.
**Primary runner:**
[`scripts/theta_mass_orientation_zero_branch_pairing_forced_2026_07_01.py`](../scripts/theta_mass_orientation_zero_branch_pairing_forced_2026_07_01.py)
**Runner cache:**
[`logs/runner-cache/theta_mass_orientation_zero_branch_pairing_forced_2026_07_01.txt`](../logs/runner-cache/theta_mass_orientation_zero_branch_pairing_forced_2026_07_01.txt)

## Why this note exists

The Tier-A `theta` registry row's mass-side minimum statement localizes the
residual to "the discrete orientation `arg det M in {0, pi} -> 0` on the
K-real reading, localized onto the named determinant-readout bridge"
(`docs/audit/data/premise_decision_history.json`, minimum form 2026-06-11). The
landed chain around that residual currently splits as:

- continuous determinant phase characters are erased by K/CPT orbit
  registration (`k = 0`;
  `THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
  and
  `STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`),
  leaving exactly the discrete set `{0, π}`;
- complex scalar mass phases are rejected on the bounded operator-basis
  surface, but the remaining SIGN selection is carried as a convention:
  "The positive sign `m > 0` remains the repo's standard Euclidean
  positive-mass convention, not a new derived axiom"
  (`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`,
  Theorem 3.4);
- the landed Case-A positivity theorem
  (`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`) proves
  `det(M_KS + m·I) > 0` for `m > 0` only, because `m > 0` was the
  load-bearing input its reflection-positivity consumer needed.

So the `{0, π} -> 0` selection has, until now, rested on the positive-mass
convention. This note removes that dependence: on the same Case-A surface the
zero branch is forced by the `±iλ` pairing for BOTH signs of the mass, for
every Hermitian flavor spectrum (signed Brannen roots included), and for the
squared mass class identically. The orientation component of the mass-side
residual is thereby removed on this surface; what remains supplied is only
the determinant-channel readout identification itself (the K-real reading),
not any orientation choice.

## Statement

Let `M_KS` be the staggered-only Case-A kinetic operator on a finite
bipartite lattice: real, antisymmetric (`M_KS^T = -M_KS`, equivalently
anti-Hermitian and K-real), anticommuting with the site-parity grading `ε`
(`{ε, M_KS} = 0`), in any background that preserves reality and
antisymmetry (identity and random Z2 links are tested). Its spectrum is
purely imaginary in exact `±iλ` pairs and its kernel has even dimension.

**(T2) Scalar mass, both signs.** For every real `m`,

```text
    det(M_KS + m·I)  =  ( Π_{pairs λ>0} (m² + λ²) ) · m^{2z}  >=  0,        (1)
```

with `2z` the (even) kernel dimension; the determinant is strictly positive
for every real `m ≠ 0` and is an EVEN function of `m`
(`det(M_KS + m·I) = det(M_KS − m·I)`, from antisymmetry under transpose).
Hence `arg det(M_KS + m·I) = 0` on the whole real mass line: the zero
orientation branch does not consume the `m > 0` convention.

**(T3) Hermitian generation mass on the flavor factor, signed roots
included.** For a supplied Hermitian generation operator `A` acting on the
flavor tensor factor (the registered instance is the Brannen circulant
`A = a·I + b·C + conj(b)·C^T`,
`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`),
with real eigenvalues `a_1, a_2, a_3` of EITHER sign,

```text
    det( M_KS ⊗ I_3  +  I ⊗ A )  =  Π_k det( M_KS + a_k·I )  >=  0.         (2)
```

Every factor is nonnegative by (T2), so the composed determinant sits on the
zero branch for EVERY dial value `(a, |b|, δ)` — including quark-type dials
whose signed-Brannen roots contain negative entries. The signed `sqrt(m)`
data (load-bearing in the Koide signed readout) is erased in the
determinant channel by the pairing.

**(T4) Squared mass class.** For a mass operator supplied in the squared
class `M = A²` (any square matrix `A` with real determinant),
`det M = (det A)² >= 0` identically: the sign of `det A` never reaches the
orientation.

**(T5, T6) The hypotheses are load-bearing (refutation legs).**
(T5) Perturbing `M_KS` by a real SYMMETRIC term (breaking the `±iλ`
pairing while keeping the determinant real) produces `det < 0` at real
mass values: without the pairing, the K-real surface alone does NOT select
the zero branch, so (1) is not a triviality of realness.
(T6) A non-K-real (non-Hermitian) flavor block produces
`arg det ∉ {0, π}`: K-reality is what discretizes the orientation to
`{0, π}`; the pairing is what then selects `0`.

## Proof

**(T2).** `M_KS` real antisymmetric: eigenvalues are purely imaginary and
come in conjugate pairs `±iλ` (`λ > 0`), and the kernel of a real
antisymmetric matrix has even dimension (its rank is even). Then

`det(M_KS + m·I) = Π_j (m + μ_j)` over the eigenvalue multiset
`{±iλ_j} ∪ {0^(2z)}`, which regroups as
`Π_{λ>0} (m + iλ)(m − iλ) · m^{2z} = Π_{λ>0} (m² + λ²) · m^{2z}`.
Every factor is `> 0` for real `m ≠ 0` (and `m² + λ² > 0` even at
`m = 0` for `λ > 0`). Evenness in `m`: transpose invariance of the
determinant gives `det(M_KS + m·I) = det(M_KS^T + m·I) = det(−M_KS + m·I) =
det(M_KS − m·I)` (the last step multiplies by `det(−I)^{...}` on an
even-dimensional space — verified exactly by the runner rather than by
dimension bookkeeping in prose). ∎

**(T3).** Diagonalize `A = U Λ U†` (Hermitian, `Λ = diag(a_k)` real). The
conjugation `I ⊗ U` commutes with `M_KS ⊗ I_3`, so
`det(M_KS ⊗ I + I ⊗ A) = det(M_KS ⊗ I + I ⊗ Λ) = Π_k det(M_KS + a_k I)`,
and each factor is `>= 0` by (T2) applied at the real value `a_k` of either
sign. ∎

**(T4).** `det(A²) = (det A)²`. ∎

**(T5), (T6).** Existence claims, exhibited constructively by the runner
(deterministic seeds): a real symmetric perturbation of the same magnitude
class with `det < 0` at a real mass value, and a non-Hermitian flavor
block with `arg det` bounded away from `{0, π}`. ∎

## What this narrows (and what it does not)

- The `theta` mass-side residual "`arg det M in {0, pi} -> 0` on the K-real
  reading" carries, on this surface, NO residual orientation freedom: the
  `0` branch is forced for every real mass of either sign, every Hermitian
  flavor dial value, and the squared class — the positive-mass convention
  is not load-bearing for the orientation. The supplied content that
  remains is the determinant-channel readout identification itself (the
  K-real reading and channel supply named by the registry and by
  `STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`),
  which this note does not derive.
- For the theta-bar assembly interface wall `W_mass_determinant_action`
  (named in the assembly bridge PR line), the ORIENTATION component is
  removed on this surface; the IDENTIFICATION component (that the
  physical mass determinant/action entry reads this supplied class) stands
  and is the next path this opens.
- Wilson-shifted surfaces (`+ r·d·I`), non-commuting flavor-kinetic
  couplings (mass operators not acting purely on the flavor tensor factor),
  and the gauge side (`theta_gauge`, winding/multi-plaquette account) are
  outside this note's surface.
- No Tier-A registry action, registry edit, or audit status is claimed or
  predicted.

## Hypothesis set used

- Retained Case-A surface and pairing machinery:
  [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  (real antisymmetric `M_KS`, `{ε, M_KS} = 0`, `±λ` pairing; its
  strictly-positive statement is for `m > 0` — extended here to all real
  `m` and to Hermitian flavor spectra).
- Registered K-real generation form (flavor instance for T3):
  [`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md)
  (the Brannen form; couplings remain the free dial — nothing here selects
  them).
- Context only, no dependency edge: the theta registry minimum statement
  (`docs/audit/data/premise_decision_history.json`);
  `STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`
  (whose positive-mass convention this note makes non-load-bearing for the
  orientation);
  `THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
  and
  `STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`
  (the continuous-phase erasure that leaves `{0, π}`).

No new axiom, admission, comparator, or fitted parameter is consumed. The
flavor dial `(a, |b|, δ)` is scanned, never selected.

## Runner and cache

```bash
python3 scripts/theta_mass_orientation_zero_branch_pairing_forced_2026_07_01.py
```

Deterministic (fixed seeds), finite-dimensional, runtime well under a
minute. Checks: exact antisymmetry/grading/pairing structure (T1); the
pairing product formula (1) at machine precision, positivity and evenness
across the signed mass grid, multiple backgrounds and both `d = 1, 2`
(T2); exact tensor factorization (2) and positivity across a Brannen dial
grid that includes negative-root dials (T3); the squared-class identity
with `det A < 0` exhibited (T4); the two refutation legs (T5, T6).

## Changelog

- **2026-07-01** — initial note. Zero orientation branch pairing-forced on
  the Case-A K-real staggered surface for all real masses of both signs,
  all Hermitian flavor spectra (signed-Brannen roots included), and the
  squared class; positive-mass convention shown non-load-bearing for the
  orientation; refutation legs for pairing and K-reality. Runner
  `PASS=18 FAIL=0`.
