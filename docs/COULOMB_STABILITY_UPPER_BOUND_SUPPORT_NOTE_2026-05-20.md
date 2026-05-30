# Coulomb Stability Upper-Bound Support

**Date:** 2026-05-20
**Claim type:** bounded_theorem
**Status:** source-side proposal; independent audit lane only
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

The landable support claim is narrower, and is stated explicitly conditional
on the admitted external premises (P1)-(P3) recorded in the Inputs section
below:

> **Conditional scaling lemma.** Given (P1) the d-dimensional continuum
> Coulomb Hamiltonian `H_d = -(hbar^2/2m) Delta_d - alpha/r^(d-2)` as an
> external admitted form, (P2) standard d-dimensional continuum quantum
> mechanics (radial Schrödinger equation, scaled-trial-state expectations,
> hydrogenic `d = 3` spectrum) as admitted background, and (P3) a
> Coulomb/scalar potential-form sector identification (no gauge coupling or
> electromagnetic sector derived from the framework), then the elementary
> trial-state scaling argument exhibits `d = 4` as the critical dimension:
> `d >= 5` is unbounded below, while `d = 3` is the canonical case with the
> Rydberg accumulation spectrum.

The argument is purely algebraic once (P1)-(P3) are admitted. This note does
not derive (P1), (P2), or (P3) from already retained framework authority. It
supports the existing named-import wrapper by writing out the elementary
scaling step explicitly, conditional on those admissions.

## Inputs

All three inputs below are explicitly admitted external premises. None is
derived in the restricted packet of this note.

1. **(P1) d-dimensional continuum Coulomb Hamiltonian (admitted external
   premise).** The dimensional potential pattern is linked to
   [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md), whose
   audited binding scope is cache-backed `d = 3` and `d = 4` rows only. Use of
   the general-`d` continuum Coulomb law
   `H_d = -(hbar^2/2m) Delta_d - alpha/r^(d-2)` is an explicit external
   admission and is not retained as a universal framework-internal law.
2. **(P2) Standard d-dimensional continuum quantum mechanics (admitted
   external premise).** The radial Schrödinger equation in `d` dimensions,
   the scaled-trial-state expectations
   `<T>_{psi_lambda} = lambda^2 T`, `<V>_{psi_lambda} = -lambda^(d-2) U`,
   and the hydrogenic `d = 3` Rydberg spectrum are admitted as external
   continuum-QM background. The corresponding spectral/domain classification
   (self-adjoint extensions, accumulation at threshold) is admitted with
   them and is not re-derived in the restricted packet.
3. **(P3) Coulomb/scalar sector identification (admitted external premise).**
   The note treats `H_d` as a Coulomb/scalar potential-form analogue. The
   identification with a physical electromagnetic sector, a derived gauge
   coupling, or a framework-internal `alpha` is not admitted by this note.

## Scaling Argument

Given admissions (P1)-(P3) above, the algebraic step proceeds as follows.
For the d-dimensional Coulomb Hamiltonian admitted in (P1),

```text
H_d = -(hbar^2 / 2m) Delta_d - alpha / r^(d-2),
```

take a normalized trial state `psi_lambda(r) = lambda^(d/2) psi(lambda r)`
of the form admitted in (P2). The kinetic and potential expectations scale
as

```text
<T>_{psi_lambda} = lambda^2 T,
<V>_{psi_lambda} = -lambda^(d-2) U,
```

with `T, U > 0` for a suitable compactly supported trial state. Therefore

```text
<H_d>_{psi_lambda} = lambda^2 T - lambda^(d-2) U.          (1)
```

For `d >= 5`, the attractive potential term grows faster than the kinetic
term as `lambda -> infinity`, so the Hamiltonian is unbounded below.

For `d = 4`, both terms scale as `lambda^2`; this is the marginal inverse-square
case. Boundedness depends on the coupling and domain choice, so it does not
give the canonical Coulomb spectrum by itself.

For `d = 3`, the standard Coulomb problem admitted in (P2) has the
hydrogenic spectrum

```text
E_n = -m alpha^2 / (2 hbar^2 n^2),     n = 1, 2, 3, ...
```

with bound states accumulating at threshold. This spectrum is consumed as
admitted external continuum-QM background and is not re-derived here.

## Relation To Dimension Selection

This note supports the upper-bound side of `DIMENSION_SELECTION_NOTE.md` only
in the bounded sense above. It complements
`BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`, but it does
not close the D=3 chain by itself and does not promote the minimal-axioms
spatial-substrate line.

The lower-bound bridge and single-clock uniqueness gaps remain open as
described in `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`.

## What This Does Not Close

- It does not retire the higher-dimensional atomic-stability import completely.
- It does not establish a retained universal dimensional Coulomb law for all
  integer `d`.
- It does not derive (P1) the d-dimensional continuum Coulomb Hamiltonian
  from already retained framework authority.
- It does not derive (P2) standard d-dimensional continuum quantum mechanics
  or the hydrogenic `d = 3` spectrum from already retained framework
  authority.
- It does not derive (P3) the electromagnetic / gauge sector identification
  or a coupling value from the framework.
- It does not settle the lower-bound force-sign bridge.
- It does not promote any parent row or audit status.
