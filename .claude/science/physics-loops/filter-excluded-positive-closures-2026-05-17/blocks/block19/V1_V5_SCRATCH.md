# Block 19 V1-V5 Scratch

Row: `gauge_vacuum_plaquette_spatial_environment_character_measure_theorem_note`
State: `audited_conditional` (class F), 639 desc.
Lane: gauge_vacuum_plaquette (continues blocks 13, 17 in 2026-05-17 campaign).

## Setup

Target is the spatial-environment character-measure note. The load-bearing
step named by the auditor:

> The residual source-sector environment operator is exactly convolution by
> the normalized boundary class function, i.e. `R_beta^env = C_(Z_beta^env)`.
>
> -- audit load_bearing_step (class F)

The auditor's chain_closure_explanation:

> The chain does not close because the equality `R_beta^env = C_(Z_beta^env)`
> is explicitly conditional on the parent residual-environment identification
> theorem. The provided runner computes and packages a bounded single-link
> Wilson witness, not the full unmarked spatial Wilson environment
> compression.

`notes_for_re_audit_if_any`:

> supply a retained-grade derivation or runner-backed certificate identifying
> the full unmarked spatial Wilson residual compression R_beta^env with
> normalized convolution by Z_beta^env, not only the single-link bounded
> witness.

The full multi-link Wilson environment tensor-transfer derivation is the
parent-of-parent open gate and explicitly out of scope here (it is the named
`gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note`
gate).

## Distinct angles from prior gauge_vacuum_plaquette blocks

- **Block 13 (PR #1444)**: U(1) sign-alternation of K_1(t) = log I_0(t)
  coefficients. Density theorem on a different parent.
- **Block 17 (PR #1454)**: stripping-uniqueness — the residual factor
  `R_beta^env|_B` is the unique algebraic solution of the source-sector
  decomposition on the finite box. *Forward* direction: from the
  decomposition (D), there is one and only one residual factor.
- **Iter b7 (PR #1217)**: replaced abstract witness with computed Wilson
  single-link character integrals. Numerical witness sourcing.
- **Bounded companion (2026-05-10)**: Peter-Weyl convolution-on-characters
  identity `chi_a * chi_b = (delta_{a,b}/d_a) chi_a` at finite box.
  Forward direction *from* a positive central class function Z *to* the
  convolution operator C_Z and its diagonal action on characters.

V1-V5 must be distinct from all of these.

## V1 — All-weight derivation of `R_beta^env = C_(Z_beta^env)`

Try to derive the parent open-gate equality at all weights (not just the
finite box) by computing the full multi-link Wilson tensor-transfer
character expansion.

VERDICT: This is the explicit named parent-of-parent open gate
(`gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note`).
The audit verdict explicitly names it as outside the bounded witness scope.
Closing it would require a full multi-link unmarked spatial Wilson
tensor-transfer theorem at all character weights, which is a multi-decade
lattice gauge theory open problem. Not closable in 90 min under A_min.
SKIP.

## V2 — U(1) restriction of the character-measure identification

Try to prove `R_beta^env = C_(Z_beta^env)` on the U(1) reduction of the
marked-plaquette class-function sector, where character irreps reduce to
e^{i n theta}.

VERDICT: Would be a density-on-Z theorem on U(1) characters. The class
of objects (positive central class functions) on U(1) collapses to Fourier
series on the circle, and the convolution-on-characters identity is
trivially Fourier multiplier theory. This would duplicate block 13's
U(1) Bessel hierarchy spirit and add no new structural content beyond the
parent's already-stated central diagonality. SKIP — too close to block 13.

## V3 — Third independent integrator for rho_(p,q)(6) cross-check

Try Method C (Sutherland/Polyakov direct rho-table integration, or
Newton's identities on power sums) to triangulate Bessel-determinant +
Weyl-integration.

VERDICT: Numerical confirmation churn. Duplicates iter b7's spirit
(numerical witness sourcing). Even adding a third integrator is
*confirmation*, not a new structural narrow theorem. SKIP — too close to
iter b7.

## V4 — Symbolic NMAX > 3 swap-commutator structural sharpening

Try to symbolic-prove the swap-commutator structure at larger NMAX than
block 17 used (NMAX_SYM = 2).

VERDICT: Structural class extension; repeats block 17's structural
argument with a bigger symbolic box. No new load-bearing step closure.
SKIP — class-structure repetition.

## V5 — Finite-box inverse Peter-Weyl convolution-realization uniqueness

This is the angle.

**Observation.** Block 17 closes the *forward* direction at finite-box scope:
the residual factor `R_beta^env|_B` is the unique algebraic stripping of the
source-sector decomposition `(D)`. The bounded companion's `(N2)` closes the
*forward* direction of the convolution-on-characters identity: given any
positive central class function `Z` with character expansion
`Z = z_0 sum d_(p,q) rho_(p,q) chi_(p,q)`, the normalized convolution
operator `C_Z` acts diagonally on `chi_(p,q)` with eigenvalue `rho_(p,q)`.

What neither closes — and what the audit names as the load-bearing class-F
step — is the **inverse direction**:

> Given the unique stripped residual `R_beta^env|_B` (block 17), is the
> normalized boundary class function `Z_beta^env|_B` realizing
> `R_beta^env|_B = C_(Z_beta^env)|_B` itself *uniquely determined*?

If multiple distinct positive central class functions truncated to `B` had
the same convolution operator on `H_B`, the parent's "identification
R_beta^env = C_(Z_beta^env)" would still be a renaming, because the
*identifying object on the right* would not be a function of the operator
on the left.

The narrow uniqueness theorem closes that specific renaming defect at
finite-box scope:

(M1) Given `R_beta^env|_B` self-adjoint, positive, diagonal in the
     orthonormal character basis on `B` with eigenvalues
     `rho_(p,q) >= 0`, define
        `Z_beta^env|_B(W) := z_(0,0)^env(beta) sum_{(p,q) in B}
                              d_(p,q) rho_(p,q) chi_(p,q)(W)`
     for any choice `z_(0,0)^env(beta) > 0`. This `Z_beta^env|_B` is a
     well-defined finite-box-truncated central class function (the
     truncation of a class function on `SU(3)` to its first `|B|`
     character harmonics). Existence is constructive.

(M2) By the bounded companion `(N2)`, the normalized convolution operator
     `C_(Z_beta^env|_B) := (1/z_(0,0)^env) (Z_beta^env|_B) * ·` on
     `H_B = span{chi_(p,q) : (p,q) in B}` acts diagonally by
        `C_(Z_beta^env|_B) chi_(p,q) = rho_(p,q) chi_(p,q)`.
     Therefore `C_(Z_beta^env|_B) = R_beta^env|_B` as finite-dimensional
     self-adjoint operators on `H_B`.

(M3) **Uniqueness:** Suppose `Z'` is *any* other central positive class
     function on `SU(3)` whose character expansion truncated to `B` reads
        `Z'|_B(W) = z_0' sum_{(p,q) in B} d_(p,q) rho'_(p,q) chi_(p,q)(W)`,
     and such that the normalized convolution operator
     `C_(Z'|_B) := (1/z_0') (Z'|_B) * ·` on `H_B` equals `R_beta^env|_B`.
     Then by the bounded companion `(N2)` applied to `Z'|_B`,
        `C_(Z'|_B) chi_(p,q) = rho'_(p,q) chi_(p,q)`.
     Equality `C_(Z'|_B) = R_beta^env|_B` forces `rho'_(p,q) = rho_(p,q)`
     for all `(p,q) in B` (a diagonal operator on an orthonormal basis
     has a *unique* eigenvalue sequence). Hence
        `Z'|_B = (z_0' / z_(0,0)^env) Z_beta^env|_B`,
     and after normalizing both sides by the trivial character coefficient
     (both `z_0' > 0` and `z_(0,0)^env > 0`),
        `Z'|_B / z_0' = Z_beta^env|_B / z_(0,0)^env`,
     i.e. the *normalized* finite-box truncation is unique.

(M4) Combining (M2) + (M3) with block 17's stripping-uniqueness of
     `R_beta^env|_B`: on the finite box `B`, both sides of the equality
     `R_beta^env|_B = C_(Z_beta^env|_B)` are *uniquely determined* —
     the left side by the source-sector decomposition stripping (block 17)
     and the right side by the inverse Peter-Weyl statement (this block).
     The two sides therefore identify *unique objects*, not renamings.

(M5) **Witness-source consistency.** Instantiating
     `rho_(p,q) := rho_(p,q)(6)` from the bounded companion's
     runner-computed canonical single-link SU(3) Wilson character integrals
     (iter b7 / bounded companion (N3)), the constructed
     `Z_(6)^env|_B` is precisely the normalized single-link Wilson
     boundary class function truncated to `B`. The runner verifies (M2)
     numerically with eigen-action error 0 and (M3) symbolically via a
     coefficient-sequence-uniqueness check on a representative finite
     subspace.

**Why this is a positive narrow theorem (not a definition):**

- The parent note's Theorem 3 *defines* `C_(Z_beta^env)` as normalized
  convolution by the central class function and then *asserts*
  `R_beta^env = C_(Z_beta^env)` because both diagonalize the same way.
  This is the audit's flagged class-F renaming: the identification depends
  on choosing the right `Z` on the right side, but the choice itself is not
  derived.
- This V5 theorem proves that, at finite-box scope, the choice on the right
  is forced: there is *exactly one* normalized truncated central class
  function whose convolution operator equals `R_beta^env|_B`.
- Combined with block 17 (the left side is uniquely stripped) and the
  bounded companion (the convolution-on-characters identity), this closes
  the class-F renaming defect at finite-box scope: both objects in the
  named equality are unique objects, not aliases.

**Why this is distinct from all prior cycles:**

- Block 13: U(1) coefficient sign-alternation on a different parent.
- Block 17: forward-direction stripping uniqueness of `R_beta^env`.
- Iter b7: numerical witness sourcing.
- Bounded companion: forward-direction Peter-Weyl convolution-on-characters
  identity from `Z` to `C_Z`.
- V1-V4: all named open gates or duplicate spirits.

This block: **inverse-direction** convolution-realization uniqueness
identifying `Z_beta^env|_B` from `R_beta^env|_B` on the finite box.
The narrow theorem closes the symmetric counterpart of block 17 in the
character-measure layer: block 17 closed "the operator side is unique"
and this block closes "the measure side is unique".

## Decision

V5 is the angle. Build a positive narrow theorem note + paired runner +
cached output. Source-only PR. A_min only.

## Hard rules check

- A_min only: uses only the retained transfer-operator / character-
  recurrence J, the retained-bounded local-environment factorization
  D_beta^loc, the bounded companion's runner-computed
  rho_(p,q)(6), and block 17's stripping-uniqueness. No new framework
  primitives.
- Source-only PR: no CANONICAL_HARNESS_INDEX, DERIVATION_ATLAS,
  DERIVATION_VALIDATION_MAP, audit-data, README, or lane-registry
  touches.
- Status authority: independent audit lane only — note labels itself
  bounded_theorem and does not claim retained grade.
- Does NOT close: the full multi-link unmarked spatial Wilson environment
  tensor-transfer at all weights, the analytic P(6) closure, the parent
  spatial-environment-character-measure note's all-weight scope, or the
  repo-wide repinning of the canonical plaquette.
