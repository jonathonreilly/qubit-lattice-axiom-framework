# Coulomb Stability Upper-Bound Support

**Date:** 2026-05-20
**Claim type:** bounded_theorem
**Status:** source-side proposal; independent audit lane only
**Related wrapper:** `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`

## Claim Boundary

This note records a bounded support argument for the atomic-stability half of
the D=3 upper-bound route. It does not claim a repo-wide axiom change and it
does not claim a complete framework-internal derivation of higher-dimensional
atomic stability.

The landable support claim is narrower:

> For the continuum d-dimensional Coulomb Hamiltonian
> `H_d = -(hbar^2/2m) Delta_d - alpha/r^(d-2)`, scaling at the origin makes
> `d = 4` the critical dimension: `d >= 5` is unbounded below, while `d = 3`
> is the canonical case with the Rydberg accumulation spectrum.

This supports the existing named-import wrapper by making the elementary
scaling part explicit. The full spectral classification remains standard
quantum mechanics unless separately derived and audited.

## Inputs

1. **Framework-connected potential form.** The dimensional potential pattern
   is linked to [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md).
   Its audited binding scope is cache-backed `d = 3` and `d = 4` rows; use of
   a general `d` continuum Coulomb law is an explicit bounded extrapolation.
2. **Standard d-dimensional quantum mechanics.** The radial Schrödinger
   equation, scaling of trial states, and hydrogenic `d = 3` spectrum are
   admitted background. This note writes out the scaling argument but does not
   re-derive the whole spectral theory.
3. **Sector identification.** The note uses a Coulomb/scalar potential-form
   analogy. It does not derive the full electromagnetic sector or a gauge
   coupling from the framework.

## Scaling Argument

For the d-dimensional Coulomb Hamiltonian

```text
H_d = -(hbar^2 / 2m) Delta_d - alpha / r^(d-2),
```

take a normalized trial state `psi_lambda(r) = lambda^(d/2) psi(lambda r)`.
The kinetic and potential expectations scale as

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

For `d = 3`, the standard Coulomb problem has the hydrogenic spectrum

```text
E_n = -m alpha^2 / (2 hbar^2 n^2),     n = 1, 2, 3, ...
```

with bound states accumulating at threshold.

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
- It does not derive the electromagnetic gauge sector or a coupling value.
- It does not settle the lower-bound force-sign bridge.
- It does not promote any parent row or audit status.
