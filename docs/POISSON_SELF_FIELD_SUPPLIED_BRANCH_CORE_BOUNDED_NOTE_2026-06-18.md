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
**Helper runners (audit packet must include):** [`scripts/poisson_self_field.py`](../scripts/poisson_self_field.py) — SHA-pinned cache [`logs/runner-cache/poisson_self_field.txt`](../logs/runner-cache/poisson_self_field.txt). The primary runner dynamically loads this helper via `importlib.util.spec_from_file_location("poisson_self_field", scripts/poisson_self_field.py)` (see `load_parent()`), so the load-bearing computation lives here. The primary runner calls the helper's `grow`, `_make_poisson_field` (which internally calls `_solve_poisson_2d`), `_prop_beam`, `_cz`, and `_dp`, plus the constants `BETA, K, MAX_D_PHYS, H, NL, PW, MASS_Z, S, FAMILIES`. This helper source plus its cache must be in the restricted audit packet for the load-bearing calls to be verifiable.

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

### Supplied finite-algorithm surface

The bounded theorem also treats the following implementation choices as
supplied finite conditions, not as framework-derived physics:

| Surface | Supplied definition used by the runners |
| --- | --- |
| lattice window | `H=0.5`, `NL=30`, `PW=8`, `MAX_D_PHYS=3` |
| source and response samples | `MASS_Z=3.0`, primary strength `S=0.004`, and `F~M` strengths `{0.001, 0.002, 0.004, 0.008}` |
| graph families | deterministic seed `0` with `(drift, restore)` equal to `(0.20, 0.70)`, `(0.05, 0.30)`, and `(0.50, 0.90)` |
| graph construction | `grow`'s Gaussian transverse drift, restoring map, and adjacency cutoff `round(MAX_D_PHYS/H)` |
| propagation | `_prop_beam` with `K=5.0`, edge phase `K L (1-f_avg)`, angular weight `exp(-BETA theta^2)` at `BETA=0.8`, and transfer weight `H^2/L^2` |
| centroid diagnostic | `_cz`'s intensity-weighted final-layer `z` centroid |
| detector diagnostic | `_dp`'s summed final-layer intensity and the declared one-, two-, and three-slit source combinations used for `I3` |

The helper source is the exact definition of these finite algorithms. No
literature value, observational comparator, or fitted target is used to prove
the reported residual, sign, scaling, cancellation, or null predicates.

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

## Repair Log

### 2026-06-20 — runner_artifact_issue repair

Included the `scripts/poisson_self_field.py` helper source plus its SHA-pinned
cache excerpt (load-bearing functions `grow`, `_make_poisson_field` →
`_solve_poisson_2d`, `_prop_beam`, `_cz`, `_dp`, and the supplied constants
`H, K, NL, PW, MASS_Z, S, FAMILIES`) in the restricted packet, addressing the
re-audit `runner_artifact_issue` ("include scripts/poisson_self_field.py in
the restricted packet and re-audit the primary runner's load-bearing calls").
The "Helper runners (audit packet must include)" reference above now names the
helper source and its SHA-pinned cache so the audit packet builder ships them.
No derived value changed — the primary runner cache still reports
`SUMMARY: PASS=18 FAIL=0`, and the helper cache still reports the same residual
budget, TOWARD shifts, `F~M` slopes, Born ratio, and `s=0` null.

The primary runner loads the helper via
`importlib.util.spec_from_file_location` (a dynamic load inside
`load_parent()`), not via `from scripts import poisson_self_field`. The
import-form parser fix landed in PR #4424 targets the `from scripts import X`
static form, so it does **not** auto-populate `helper_runner_paths` for this
dynamic load. The audit packet must therefore include this helper via the
note-side reference above (the same packaging convention used by other notes
whose helpers are loaded dynamically).

Status authority: independent audit lane only. This repair sets no
`audit_status`, `effective_status`, ledger tag, or retained status; it is the
exact audit-named packaging repair and nothing more.

### 2026-07-12 — deterministic restricted-packet repair

The generated packet dependency manifest had remained stale even though the
citation graph and audit-ledger row named `scripts/poisson_self_field.py` as a
helper. Both packet dependency resolvers now explicitly register that helper
for this claim in addition to detecting the dynamic load. Validation-time
regeneration and a direct restricted-prompt render confirm that the packet
contains all four inspectable artifacts:

1. this bounded source note;
2. `scripts/poisson_self_field_supplied_branch_core_2026_06_18.py` and its
   SHA-pinned cache;
3. the complete `scripts/poisson_self_field.py` helper source; and
4. `logs/runner-cache/poisson_self_field.txt`, whose header pins the helper to
   SHA-256 `1c0e140b3bc17b18e25aa175800e12ce59c3d3e2046854c878e66c10f4774180`.

This addresses only the auditor's `runner_artifact_issue`: it makes `grow`,
`_make_poisson_field` / `_solve_poisson_2d`, `_prop_beam`, `_cz`, `_dp`, and
the used constants visible for independent inspection alongside their cached
execution. It does not alter the supplied-input boundary or promote the claim;
an independent re-audit remains required and owns the verdict.
