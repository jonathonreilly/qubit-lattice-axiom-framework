# Block 17 V1-V5 Scratch

Row: `gauge_vacuum_plaquette_residual_environment_identification_theorem_note`
State: `audited_conditional` (class F renaming), 637 desc.
Lane: gauge_vacuum_plaquette (continues blocks 03, 13; distinct sub-problem
from each).

## Setup

Target is the residual source-sector operator `R_beta^env` defined by the
source-sector decomposition

```
K_beta^src = exp[(beta/2) J] D_beta^loc R_beta^env exp[(beta/2) J]
```

on the marked-plaquette `SU(3)` class-function sector, where

- `J = (chi_(1,0) + chi_(0,1)) / 6` is the explicit self-adjoint source
  operator,
- `D_beta^loc chi_(p,q) = a_(p,q)(beta)^4 chi_(p,q)` is the exact normalized
  mixed-kernel local Wilson four-link factor (already retained-bounded via
  the local-environment factorization theorem),
- `K_beta^src` is the one-step Wilson source-sector kernel (already retained
  via the transfer-operator / character-recurrence theorem).

The parent note already proves structural class (positive, self-adjoint,
central, diagonal, conjugation-symmetric) and that the eigenvalues
`rho_(p,q)(beta)` exist. Iter b7 (PR #1217) replaced the prior hand-picked
witness with computed canonical Wilson single-link character integrals
on the finite box.

The audit verdict (`audited_conditional`, class F renaming) flagged that
the load-bearing step is identification by renaming rather than derivation:
the parent shows `R_beta^env` is a positive diagonal operator and the b7
runner now uses computed Wilson coefficients on the finite box, but neither
proves the operator `R_beta^env` is *uniquely* fixed by the decomposition
above on that finite box. If multiple admissible positive diagonal residuals
solved the same decomposition, the parent's "identification" would be
ill-posed even within the bounded finite-box scope.

## Distinct angles from prior gauge_vacuum_plaquette blocks

- **Block 03 (PR #1217 / iter b7)**: replaced the finite-box witness with
  computed canonical Wilson single-link boundary character coefficients
  `rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q) c_(0,0)(6))` from the Schur-Weyl
  Bessel-determinant identity. This is *numerical witness sourcing*.
- **Block 13 (PR #1444)**: positive narrow sharpening of the U(1) instance
  of the parent infinite-hierarchy obstruction — sign-alternation of
  `c_{2k}` of `K_1(t) = log I_0(t)` via the Bessel Riccati recurrence.
  This is *U(1) coefficient density* for an entirely different parent row.
- **Iter b7**: see Block 03 above.
- **This block (17)**: structural *uniqueness* of the residual factor as
  an algebraic stripping consequence on the finite box, independent of
  any specific witness or computed coefficient sequence.

V1-V5 must be distinct from all of these.

## V1 — Derive all-weight identification `R_beta^env = C_(Z_beta^env)`

Try to prove the parent open-gate equality at all weights, not just on the
finite box.

VERDICT: This is the explicit "what this does not close" item in the
parent note ("the all-weight or full tensor-transfer coefficients of the
actual unmarked spatial Wilson environment"). Closing it would require a
full multi-link unmarked spatial Wilson tensor-transfer theorem, which is
the explicit open gate `gauge_vacuum_plaquette_spatial_environment_tensor_transfer_theorem_note`.
That gate is the parent of the parent. Not closable in 90 min under
A_min. SKIP.

## V2 — Derive analytic framework-point `P(6)`

Try to derive the analytic Perron expectation `P(6)` from the factorized
source-sector law `exp(3 J) D_6^loc R_6^env exp(3 J)`.

VERDICT: This is the explicit "what this does not close" item ("analytic
closure of canonical `P(6)`"). Requires the all-weight closure first.
SKIP.

## V3 — Recompute `rho_(p,q)(6)` via a different integrator and cross-check

Try Method C (e.g., direct Monte-Carlo, Newton's identity on power sums,
or recursive Clebsch-Gordan reduction) to triangulate against the existing
Bessel-determinant + Weyl-integration cross-check.

VERDICT: This duplicates the spirit of iter b7 (witness replacement /
computational cross-check). Even if it added a third independent integrator,
it would still be a *numerical confirmation* of the same finite-box
coefficients, not a new structural narrow theorem. SKIP — too close to
iter b7.

## V4 — Quantitative sharpening of U(1) sign-alternation to SU(3)

Try to lift the block 13 U(1) sign-alternation on `c_{2k}` to `SU(3)`
boundary character coefficients.

VERDICT: This is a direct extension of block 13. Even if it succeeded
(would require a multi-mode Riccati equivalent for SU(3) characters,
which is open in the literature), it would be one-step variant churn on
block 13's sub-problem, violating V5 distinctness. SKIP.

## V5 — Stripping-uniqueness of the residual factor on the finite box

This is the angle.

**Observation:** On the finite truncation box `0 <= p,q <= NMAX`,
`exp[(beta/2) J]` and `D_beta^loc` are both positive operators in the
finite-dimensional character-basis representation. `exp[(beta/2) J]` is
positive because `J` is self-adjoint (so `exp(tau J)` has strictly positive
eigenvalues for any real `tau`). `D_beta^loc` is positive because
`a_(p,q)(beta) > 0` for all `(p,q)` in the finite box (the trivial-channel
normalization `a_(0,0)(beta) = 1` and the single-link Wilson character
integrals `c_(p,q)(beta) > 0` are both strictly positive for `beta > 0`).
Strictly positive operators on a finite-dimensional space are invertible.

Therefore, on the finite box, the source-sector decomposition

```
K_beta^src = exp[(beta/2) J] D_beta^loc R_beta^env exp[(beta/2) J]
```

algebraically inverts to

```
R_beta^env = (D_beta^loc)^{-1} exp[-(beta/2) J] K_beta^src exp[-(beta/2) J]   (*)
```

so the finite-box residual factor `R_beta^env` is **uniquely determined** by
`K_beta^src`, `D_beta^loc`, and `exp[(beta/2) J]` on that box. There is no
admissibility freedom in the residual within the parent's "positive diagonal
central conjugation-symmetric" class beyond what `(*)` already fixes.

**Why this is a positive narrow theorem (not a definition):**

- The parent note's Theorem 1 *defines* `R_beta^env` as "what remains after
  stripping" and then proves its structural class (Theorem 2). It does not
  prove uniqueness of the stripped object, only its existence and structural
  type.
- The bounded companion (`...FINITE_BOX_BOUNDED_COEFFICIENT_NARROW_NOTE`)
  takes the decomposition as a *definition* of `R_beta^env` and instantiates
  the `rho_(p,q)(6)` from the b7 computed coefficients (N3). It does not
  prove that the decomposition uniquely determines `R_beta^env`.
- The audit verdict (`audited_conditional`, class F renaming) names this
  exact gap: the load-bearing step is "identification by renaming" rather
  than a derivation that the named object is the *only* object that fits.
- This V5 theorem closes that specific renaming defect within finite-box
  scope: on the finite box, `R_beta^env` is *the* unique stripped factor,
  and the parent's class-F renaming is upgraded from "name only" to
  "uniquely-determined named object".

**What this lands as:**

A narrow positive theorem statement and runner that proves:

(U1) `exp[(beta/2) J]` is invertible on the finite character-basis truncation
     (positive eigenvalues, so positive determinant);
(U2) `D_beta^loc` is invertible on the finite character-basis truncation
     (positive diagonal entries);
(U3) the stripped residual factor on the finite box is uniquely determined
     by `(*)` from `K_beta^src`, `D_beta^loc`, `exp[(beta/2) J]`;
(U4) the unique stripped residual factor satisfies the parent's structural
     class (positive, self-adjoint, central, diagonal, conjugation-symmetric)
     iff `K_beta^src` does;
(U5) on the finite box `0 <= p,q <= NMAX`, the unique stripped residual
     factor's diagonal eigenvalues equal `rho_(p,q)(beta)` from the b7
     computed coefficients up to machine precision (no witness substitution
     freedom).

**Why this is distinct from all prior cycles:**

- Block 03 / iter b7: numerical witness sourcing; this block is a structural
  uniqueness/inversion theorem.
- Block 13: U(1) coefficient sign-alternation on a different parent
  (`...infinite_hierarchy_obstruction_note`); this block is on the residual
  environment identification parent and proves an SU(3) algebraic
  uniqueness lemma.
- Parent gates (V1, V2): far beyond scope; this block is a strict subset
  closing the specific renaming defect.
- V3, V4: cross-check / SU(3) extension churn; this block is a new
  structural inversion theorem with explicit (U1)-(U5) closures.

## Decision

V5 is the angle. Build a positive narrow theorem note +
paired runner + cached output. Source-only PR. A_min only.
