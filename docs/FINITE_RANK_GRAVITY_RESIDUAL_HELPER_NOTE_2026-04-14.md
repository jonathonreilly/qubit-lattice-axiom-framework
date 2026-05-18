# Finite-Rank Gravity Residual Helper Module

**Date:** 2026-04-14 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded helper-module wrapper for the finite-rank gravity
support operator and its exact Woodbury/Dyson source renormalization.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper module.
**Primary runner / module:** `scripts/frontier_finite_rank_gravity_residual.py`

## Purpose

This wrapper note documents the finite-rank gravity residual helper module
so downstream notes (notably
[FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md](FINITE_RANK_SOURCE_TO_METRIC_THEOREM_NOTE.md))
can register a one-hop dependency rather than carry the helper as an
unattributed Python `SourceFileLoader` import.

## What this module provides

The helper module constructs the exact finite-rank support operator
acting on the lattice Hamiltonian:

```
H_W  =  H_0  -  P W P^T,
G_0  =  H_0^{-1},
G_S  =  P^T G_0 P.
```

with:
- `H_0`: the bare lattice Hamiltonian (positive, self-adjoint, invertible).
- `P`: the support projector onto the finite-rank source channel.
- `W`: the finite-rank self-energy matrix on the support channel.

The exact Woodbury/Dyson identity gives the renormalized propagator

```
G_W P  =  G_0 P (I  -  W G_S)^{-1}.
```

so every bare support source vector `m` induces the exact renormalized
source

```
q_eff  =  (I  -  W G_S)^{-1} m
```

and the exact exterior field

```
phi  =  G_0 P q_eff.
```

This is implemented in the module function `exact_finite_rank_field()`.

## Verification

The companion runner of the downstream theorem note verifies the
Woodbury identity to numerical zero (residual `6.939e-17`), confirming
the finite-rank operator construction reproduces the bare propagator
identity on the support channel.

## Boundary

This wrapper note records the bounded helper-module character of the
finite-rank gravity residual module. It does not claim:

- a framework-level derivation of the finite-rank support structure
  itself (the choice of `P` and `W` is a separate framework input);
- a tensorial `3 + 1` lift from the scalar exterior field to the full
  lapse-shift-spatial metric;
- closure of any downstream gravity theorem.

Its only function is to provide a citeable one-hop authority for the
finite-rank Woodbury/Dyson source renormalization and exterior-field
construction so downstream notes register the import cleanly instead of
carrying it as a `SourceFileLoader` runner import without a wrapper.
