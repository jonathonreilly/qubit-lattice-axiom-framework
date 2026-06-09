# The Gravity Sign Is a Unitarity Datum: Reflection Positivity Forbids a Physical Spin-2 Ghost, Reducing G>0 to Emergent Diffeomorphism Invariance

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** reduction + theorem-connection (ties the gravity sign to reflection positivity; relocates the residual)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.py`](../scripts/gravity_sign_from_reflection_positivity_unitarity_dewitt_lambda_2026_06_08.py) (PASS=4).

## The harder frontier

[`GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK...`](GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md)
(in review) showed the gravity sign is **one residual** (attraction = TT graviton kinetic health = `sign G`)
and that the framework's **matter** effective action provably **cannot** source it (the spin-2 graviton is
in the exact kernel of `W`'s rank-1 longitudinal metric-Hessian). So the sign must be a **geometric +
unitarity** datum. This note supplies the unitarity half and **reduces the sign to emergent
diffeomorphism invariance**, tying it to a framework theorem.

## The argument

- **(H1) Reflection positivity forbids a physical ghost.** Reflection positivity (RP) is a framework
  theorem ([`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)).
  By Osterwalder-Schrader, RP ⇒ a **positive-norm** physical Hilbert space + `H ≥ 0`. A negative-norm
  (ghost) state cannot be physical. Hence **a propagating *physical* mode has a healthy (non-ghost)
  kinetic sign** — verified: an RP (PSD) reconstructed Gram has all norms `≥ 0`, while an indefinite
  (non-RP) Gram carries a ghost direction.

- **(H2) The healthy-graviton structure = the DeWitt `λ=1` signature.** On symmetric 2-tensors (`d=3`)
  with `G(λ)^{ij,kl} = ½(g^{ik}g^{jl}+g^{il}g^{jk}) − λ g^{ij}g^{kl}`: the **TT (spin-2)** eigenvalue is
  `+1` (`λ`-independent), and the **conformal/trace** eigenvalue is `1 − λd`. At the GR value `λ=1`
  (`d=3`): TT `+1`, trace `−2` — **opposite signs**: two positive-norm TT polarizations plus one
  wrong-sign conformal mode that **diffeomorphism makes gauge** (non-propagating). The framework's
  **natural** field-space metric `−Tr(D⁻¹hD⁻¹k)` is **degenerate**: **trace and shear (TT) have the same
  sign** (both `−b⁻²`), the convention-free statement of "not the `λ=1` split"
  ([`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md) /
  degenerate-supermetric no-go). In the `G(λ)` form above this is the **no-conformal-term `λ=0`** case (the
  no-go runner's label); the alternative loose label `λ=1/d` denotes the point where the trace eigenvalue
  `1−λd` vanishes — either way it is **not** the healthy `λ=1` (trace/TT opposite-sign) structure, so the
  natural metric does **not** by itself supply the clean healthy-TT / gauge-conformal split.

- **(H3) The reduction.** Combining H1+H2: **`G>0` (healthy TT) follows from RP** *conditional on* (a) the
  emergent graviton's TT modes being **physical RP excitations**, and (b) **emergent diffeomorphism
  invariance** making the conformal mode gauge (so it is not a physical ghost). RP alone (a theorem)
  guarantees no *physical* ghost; (a)+(b) say the TT graviton **is** the physical content and the
  conformal mode **is** gauge. So the sign is no longer an independent coefficient to compute by hand —
  **it is fixed by unitarity once the emergent graviton is a physical diffeomorphism-covariant mode.**

## Result

**The gravity sign `G>0` is a unitarity datum, not a free coefficient.** Reflection positivity (a
framework theorem) forbids a physical spin-2 ghost; therefore *if* the emergent graviton is a physical RP
mode with emergent diffeomorphism invariance (conformal mode gauge — the DeWitt `λ=1` structure), its TT
kinetic term is healthy and `G>0` (attraction). This **reduces the deepest gravity-sign residual** — the
geometric graviton kinetic sign, with the matter route provably dead — **to the single question of
emergent diffeomorphism invariance**, and **connects it to a framework theorem (RP)**.

## What is and is not claimed

- **Is:** RP (framework theorem) ⇒ no physical ghost (H1); the healthy graviton structure is the DeWitt
  `λ=1` signature (TT `+`, conformal `−`-but-gauge) (H2); hence `G>0` follows from RP **conditional on**
  the emergent graviton being a physical RP mode with diffeomorphism invariance (H3). The gravity sign is
  thereby tied to RP and the residual relocated to emergent diffeomorphism invariance.
- **Is not:** does **not** unconditionally close the sign. Honestly, the conditional (a)+(b) is close to
  "the graviton is healthy," so this is a **reduction/connection**, not a magic closure: its content is
  (i) the matter route is dead, (ii) the sign is a *unitarity* question tied to the RP theorem, and (iii)
  the precise open piece is **emergent diffeomorphism invariance** (the `λ=1` / conformal-gauge structure),
  which the framework's **degenerate** natural supermetric does **not** yet supply. Does not derive that
  structure; does not touch any registered scale (`G_Newton`).

## Boundaries (honest)

- **Near-circularity, acknowledged.** "(a) the graviton is a physical RP mode" is close to "(the graviton
  is healthy)"; the value is the *connection to RP* + the precise statement that the open piece is the
  diffeomorphism/conformal-gauge structure (a well-posed geometric question), not an independent sign.
- **The conformal mode.** RP forbids *physical* ghosts; the conformal mode's wrong-sign kinetic term is
  consistent with RP only if it is **gauge** (non-physical) — i.e. emergent diffeomorphism invariance is
  required, and is the open residual.
- **The supermetric degeneracy is cited, not recomputed** (the retained `UNIVERSAL_GR` blocker).

## Load-bearing inputs

- [`GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md`](GRAVITY_SIGN_IS_ONE_RESIDUAL_AT_THE_TT_KERNEL_BLOCK_NARROW_THEOREM_NOTE_2026-06-08.md)
  — the sign = one residual; the matter route is dead (TT-kernel) (in review).
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — RP ⇒ positive-norm physical Hilbert space + `H ≥ 0` (the no-physical-ghost input).
- [`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md)
  — the framework's natural supermetric is degenerate (the `λ≠1` blocker; the open diffeo structure).

## Forbidden-imports check

No PDG / fitted value. RP ⇒ PSD is standard Osterwalder-Schrader; the DeWitt-`λ` eigenvalues are exact
linear algebra (reproduced in the runner); the framework's degenerate supermetric is cited, not
recomputed. Form/sign level only.
