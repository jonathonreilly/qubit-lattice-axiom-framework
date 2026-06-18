# Poisson Self-Field Supplied-Branch Core Bounded Note

**Date:** 2026-06-18
**Type:** bounded_theorem source proposal
**Claim type:** bounded_theorem
**Status:** source-side bounded support split for the supplied Poisson branch.
This is not an audit verdict, not a retained derivation of gravity, and not a
new axiom.
**Parent/context:** `POISSON_SELF_FIELD_NOTE.md` is context only, not a
load-bearing authority for this bounded core.
**Primary runner:** [`scripts/poisson_self_field_supplied_branch_core_2026_06_18.py`](../scripts/poisson_self_field_supplied_branch_core_2026_06_18.py)
**Runner cache:** [`logs/runner-cache/poisson_self_field_supplied_branch_core_2026_06_18.txt`](../logs/runner-cache/poisson_self_field_supplied_branch_core_2026_06_18.txt)
**Computation source:** [`scripts/poisson_self_field.py`](../scripts/poisson_self_field.py)

## Authority disclaimer

This source note proposes a narrowed bounded-support claim for independent
review and audit. It does not set `audit_status`, `effective_status`, ledger
tags, publication status, or retained status. The independent audit lane decides
whether the narrowed claim closes.

The load-bearing surface is the finite runner/computation source listed above,
plus the supplied inputs declared below. The parent note is cited only to show
which older mixed-scope surface this split repairs.

## Question

What, if anything, closes if the Poisson equation, point source, boundary
condition, normalization, physical readout, and longitudinal factor are treated
as supplied inputs rather than framework-derived ingredients?

## Answer

The finite supplied-branch computation closes. Given those supplied inputs, the
runner verifies the branch-local numerical consequences on the declared lattice:

- a 50-sweep Gauss-Seidel solution of the supplied per-layer 2D discrete
  Poisson problem, with zero Dirichlet boundary and max residual
  `<= 3.19e-05` on the tested lattice;
- positive TOWARD centroid shifts for all three declared graph families;
- near-linear response, with `F~M = 0.9997`, `0.9993`, and `0.9994`;
- machine-precision Born cancellation on the active Poisson branch,
  `Born |I3|/P <= 1.5e-15`;
- exact null behavior at `s=0`.

## Supplied Inputs

| Input | Status in this note |
| --- | --- |
| 2D per-layer discrete Poisson equation | supplied |
| point source location and source strength | supplied |
| zero Dirichlet boundary on the transverse grid | supplied |
| Gauss-Seidel iteration count and tolerance budget | finite numerical branch |
| longitudinal factor `1/(dx+0.1)` | imposed |
| centroid readout as gravity proxy | supplied diagnostic readout |
| interpretation as physical gravity | not claimed |

PDE, source, boundary condition, normalization, physical gravity readout, and
longitudinal falloff remain supplied or imposed. This note proves no
framework-native origin for any of them.

## Bounded Theorem Statement

For the constants and graph families used in `scripts/poisson_self_field.py`,
let each layer use the supplied transverse grid equation

```text
laplacian_perp(f) = -source(iy, iz)
```

with source at `iy=0`, `iz=round(z_src/H)`, zero boundary values, and effective
per-layer strength

```text
eff_s = s / (abs(layer*H - x_src) + 0.1) * H * H .
```

Then the runner computes, rather than hard-codes, the finite supplied-branch
claims listed in the Answer section. The theorem is bounded to that finite
branch and to the stated constants.

## Non-Claims

This note does not claim:

- a retained derivation of gravity;
- a framework-native derivation of the Poisson equation;
- a framework-native derivation of the source, boundary condition,
  normalization, readout, or longitudinal falloff;
- a full 3D field equation;
- a continuum, asymptotic, retarded, or time-dependent law;
- a physical Newton constant or physical mass-source closure.

## Why This Helps Audit

The parent note previously mixed a useful finite computation with language that
could be read as a derived transverse field law. This split preserves the useful
science while making the boundary explicit. An auditor can now review the
narrow claim directly: "given the supplied branch, do the finite computed
consequences follow?" Broader gravity derivation questions remain open.

## No New Axiom

This split adds no repo-wide axiom and no new physical postulate. It is a
source-boundary repair around an already supplied numerical branch.
