# Coulomb Stability Upper-Bound Support

**Date:** 2026-05-20
**Claim type:** bounded_theorem
**Status:** source-side proposal; independent audit lane only
**Primary runner:** [`scripts/frontier_coulomb_stability_scaling_repair.py`](../scripts/frontier_coulomb_stability_scaling_repair.py)
**Related wrapper:** `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The algebraic scaling step follows from the admitted Hamiltonian and trial-state expectations, but those are explicit external premises rather than retained results in the restricted packet. The missing closures are the general-d Coulomb Ha"*

with repair: *"missing_bridge_theorem: add retained bridge theorems or cited retained dependencies deriving P1, P2, and P3, or keep the claim explicitly conditional on those external admissions."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The elementary trial-state scaling argument — given the admitted d-dimensional Coulomb Hamiltonian (P1) and scaling expectations (P2) — which shows algebraically that `d >= 5` is unbounded below and identifies `d = 4` as the critical dimension, with `d = 3` as the canonical Rydberg case; this algebra is runner-verified and closes exactly within the admitted premises.
- **NON-load-bearing (split off / admitted):** The general-d Coulomb Hamiltonian form (P1), the d-dimensional continuum quantum mechanics background (P2), and the Coulomb/scalar sector identification (P3) are all explicit external admissions, not retained results derived from framework authority; these bridge premises remain admitted, non-load-bearing inputs until retained derivations for them land.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Claim Boundary

This note records a bounded support argument for the atomic-stability half of
the D=3 upper-bound route. It does not claim a repo-wide axiom change and it
does not claim a complete framework-internal derivation of higher-dimensional
atomic stability.

The landable support claim is narrower:

> **Green-kernel scaling lemma.** For integer `d >= 3`, let
> `G_d(r) = r^(2-d)` on `R^d \ {0}` and consider the quadratic form
> `Q_d[psi] = kappa int |grad psi|^2 dx - alpha int G_d(|x|)|psi|^2 dx`
> on smooth compactly supported test functions away from the origin, with
> `kappa, alpha > 0`. Then `Delta G_d = 0` away from the origin, the scaled
> functions `psi_lambda(x) = lambda^(d/2) psi(lambda x)` preserve norm, and
> `Q_d[psi_lambda] = lambda^2 T - lambda^(d-2) U`. Therefore the attractive
> Green-kernel form is unbounded below for every integer `d >= 5`; `d = 4`
> is the marginal inverse-square exponent; and the scaling test alone does
> not prove a physical `d = 3` hydrogen spectrum.

The result is a bounded continuum-math support lemma. It retires the
load-bearing import of the trial-state scaling algebra inside this row, but
it does not supply a framework-native electromagnetic sector, gauge coupling,
or full spectral theorem. Those remain outside this note.

## Inputs

The binding calculation uses only the following mathematical inputs:

1. **Euclidean radial calculus.** For a radial function `f(r)` on
   `R^d \ {0}`,

   ```text
   Delta f = f''(r) + ((d-1)/r) f'(r).
   ```

   Substituting `f(r) = r^a` gives

   ```text
   Delta r^a = a(a + d - 2) r^(a-2).
   ```

   With `a = 2 - d`, this gives `Delta r^(2-d) = 0` away from the origin.
   The singular source normalization at the origin is not used.
2. **Compactly supported test functions.** The form is evaluated on
   smooth compactly supported `psi` with support avoiding the origin and with
   `T = kappa int |grad psi|^2 dx > 0` and
   `U = alpha int r^(2-d) |psi|^2 dx > 0`.
3. **Dilation.** For `lambda > 0`,

   ```text
   psi_lambda(x) = lambda^(d/2) psi(lambda x).
   ```

   This is a change-of-variables calculation, not an admitted spectral fact.

No physical electromagnetic-sector identification is used in the binding
lemma. The symbols `alpha` and `kappa` are positive form coefficients only.

## Scaling Proof

For integer `d >= 3`, define

```text
Q_d[psi] = kappa int |grad psi(x)|^2 dx
           - alpha int |x|^(2-d) |psi(x)|^2 dx.
```

The radial identity above shows that `|x|^(2-d)` is the harmonic Green-kernel
shape away from the origin. For the dilation `psi_lambda`, the norm obeys

```text
int |psi_lambda(x)|^2 dx
= int lambda^d |psi(lambda x)|^2 dx
= int |psi(y)|^2 dy.
```

The gradient term scales as

```text
int |grad psi_lambda(x)|^2 dx
= lambda^2 int |grad psi(y)|^2 dy,
```

and the attractive Green-kernel term scales as

```text
int |x|^(2-d) |psi_lambda(x)|^2 dx
= lambda^(d-2) int |y|^(2-d) |psi(y)|^2 dy.
```

Therefore

```text
Q_d[psi_lambda] = lambda^2 T - lambda^(d-2) U.          (1)
```

For every integer `d >= 5`, the attractive term in (1) grows with exponent
`d - 2 > 2`, so `Q_d[psi_lambda] -> -infinity` as `lambda -> infinity`.
Thus the form is unbounded below on this test-function family.

For `d = 4`, both terms scale as `lambda^2`; this is the marginal
inverse-square exponent. The scaling argument alone does not decide
boundedness without a coupling/domain theorem.

For `d = 3`, the attractive term scales as `lambda`, so this ultraviolet
collapse test does not make the form unbounded below. This note does not
claim the hydrogenic spectrum, threshold accumulation, self-adjoint-extension
classification, or physical Rydberg scale.

## Runner Certificate

`scripts/frontier_coulomb_stability_scaling_repair.py` verifies the restricted
claim by checking:

- the radial Laplacian formula `Delta r^a = a(a+d-2) r^(a-2)`;
- the Green-kernel substitution `a = 2-d`;
- norm preservation for `psi_lambda`;
- kinetic scaling by `lambda^2`;
- potential scaling by `lambda^(d-2)`;
- the exponent ordering for `d = 3`, `d = 4`, and all checked `d >= 5`;
- concrete large-`lambda` examples showing negative divergence for `d >= 5`.

## Relation To Dimension Selection

This note supports the upper-bound side of `DIMENSION_SELECTION_NOTE.md` only
in the bounded sense above. It complements
`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`, but it does
not close the D=3 chain by itself and does not promote the minimal-axioms
spatial-substrate line.

The lower-bound bridge and single-clock uniqueness gaps remain separate
open issues recorded in `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`.

## What This Does Not Close

- It does not retire the higher-dimensional atomic-stability import completely:
  it retires only the Green-kernel scaling sublemma.
- It does not establish a framework-native electromagnetic sector, gauge
  coupling, or physical value of `alpha`.
- It does not prove a full hydrogenic `d = 3` spectrum, threshold
  accumulation, or self-adjoint-extension classification.
- It does not prove a universal dimensional Coulomb law as a physical
  framework theorem for all `d`; the binding statement is a bounded
  continuum-math lemma about the stated Green-kernel form.
- It does not settle the lower-bound force-sign bridge.
- It does not promote any parent row or audit status.
