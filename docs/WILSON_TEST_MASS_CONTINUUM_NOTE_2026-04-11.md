# Wilson Test-Mass / Finite-L Distance-Law Companion

**Date:** 2026-04-11 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: finite-L distance-law table is the binding evidence; the L→∞ continuum extrapolation becomes a diagnostic-only readout)
**Status:** bounded companion on the Wilson lane
**Type:** bounded_theorem
**Scope:** same-convention open-boundary Wilson runners only; finite-L
distance-law table is the binding evidence
**Primary runner:** [`scripts/wilson_test_mass_continuum_certificate.py`](../scripts/wilson_test_mass_continuum_certificate.py)

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"split the finite open-Wilson
numerical companion from the asymptotic continuum-limit extrapolation,
or justify the extrapolation model selection explicitly before
re-audit."*

This revision takes the splitting option. The binding evidence of this
note is now exactly:

- the weak-field **test-mass** finite-grid result
- the first-order **perturbative mass-law** finite-grid result
- the **finite-L distance-law table** on the open-Wilson size sweep
  (L ∈ {12, 15, 18, 20, 22, 25}), with the per-L fitted exponent
  `alpha(L)` and R² reported descriptively.

The asymptotic **L → ∞ continuum extrapolation** `alpha_inf = -2.009
± 0.019` is **demoted to a diagnostic-only readout, out of audited
scope of this note**. Promoting that extrapolation to a continuum-
limit fact requires a separate justification of the
extrapolation model (functional form, convergence rate, error budget,
finite-volume systematics). No such justification is supplied here.

## Purpose

Freeze the late-2026-04-11 Wilson Newton-strengthening batch in its honest
form.

This note is intentionally narrower than a global Newton claim. It preserves:

- the weak-field **test-mass** result
- the first-order **perturbative mass-law** result
- the **finite-L** open-Wilson distance-law table

It does **not** close:

- the asymptotic **L → ∞ continuum-limit** extrapolation as a retained
  fact (demoted to diagnostic-only per the 2026-05-17 narrowing)
- full Hartree both-masses closure
- action-reaction / third-law closure
- architecture-independent Newton closure
- the broader normalization debate across mixed Wilson runners

## What Was Run

- [`scripts/frontier_test_mass_limit.py`](../scripts/frontier_test_mass_limit.py)
- [`scripts/frontier_perturbative_mass_law.py`](../scripts/frontier_perturbative_mass_law.py)
- [`scripts/frontier_continuum_limit.py`](../scripts/frontier_continuum_limit.py)
- [`scripts/frontier_newton_systematic.py`](../scripts/frontier_newton_systematic.py)

All four share the same open-Wilson convention:

- open 3D cubic Wilson surface
- complex Wilson hopping with `WILSON_R = 1`
- Poisson solve with `-4*pi*G*rho`
- low-screening regime `mu^2 = 0.001`

That common convention matters. These runners should be read as a **within-lane
Wilson calibration package**, not as a reconciliation of every older Wilson
script in the repo.

## Bounded Read

### 1. Test-mass limit passes cleanly

On the weak-field audited surface (`G = 0.002`), the heavy-source / light-test
setup gives:

- source-mass exponent `1.002` with `R^2 = 1.000`
- distance exponent `-2.197` with `R^2 = 0.984`
- inward acceleration on every audited configuration

This is the cleanest mass-law result on the Wilson lane because the field is
sourced by the heavy packet only, avoiding Hartree self-field contamination in
the light packet.

### 2. First-order perturbative mass law is exact by construction

The perturbative Green-function extraction gives:

- source-mass exponent `1.0000` with `R^2 = 1.000`
- `G` exponent `1.0000`
- distance exponent `-1.916` with `R^2 = 0.9995`

This is useful as a same-convention theory companion, not as a standalone
headline. The linear mass and coupling exponents are exact at first order, so
the real content is:

- the clean separation of partner-force from self-field at weak coupling
- the comparison against the full Hartree lane, where higher-order corrections
  are visibly non-negligible

### 3. Open-Wilson finite-L distance-law table (binding)

The size sweep on the same open-Wilson surface gives the following
per-L fitted distance exponents (binding evidence):

| `L` | `alpha(L)` | `R^2` |
|---|---:|---:|
| 12 | `-1.827` | `0.9991` |
| 15 | `-1.932` | `0.9993` |
| 18 | `-1.973` | `0.9997` |
| 20 | `-1.965` | `0.9999` |
| 22 | `-1.982` | `0.9999` |
| 25 | `-2.002` | `0.9999` |

The audited content of this section is **the finite-L table** above
together with the descriptive observation that the largest accessible
L (L = 25) sits near `alpha ≈ -2` in this same-convention regime.

> **Diagnostic-only (out of audited scope):** A fitted L → ∞
> continuum extrapolation gives `alpha_inf = -2.009 ± 0.019`. The
> extrapolation model selection (functional form, convergence rate,
> error budget, finite-volume systematics) is **not** independently
> justified in this note. The continuum-extrapolation number is
> recorded as a diagnostic-only readout, not as an established
> continuum-limit fact. A retained continuum-limit claim requires a
> separate extrapolation-justification authority that this note does
> not supply.

## What This Does Not Close

### 1. Not full Newton closure

This note does **not** promote `F ∝ M1 M2 / r^2` as a retained repo truth.

Why:

- the valid Hartree both-masses lane still fails clean closure
- the test-mass setup only closes the source-mass half of the law
- the finite-L table reaches a near-minus-two distance exponent on the largest
  tested open-Wilson sizes, but supplies no continuum-limit closure and no
  full two-body law on the same surface

### 2. Not a normalization verdict across all Wilson scripts

The same `-4*pi*G*rho` convention is used across this batch. That means these
results are internally coherent **within this lane**, but they do not by
themselves prove that earlier discrepancies elsewhere were solely a
normalization mistake.

Use this note with:

- [`scripts/frontier_newton_systematic.py`](../scripts/frontier_newton_systematic.py)
- `docs/WILSON_NORMALIZATION_RECONCILIATION_NOTE_2026-04-11.md`
  (plain-text reader pointer; the reconciliation companion is a
  meta-level cross-runner overview and is **not** a load-bearing
  markdown-link dependency of this finite-L distance-law table — the
  load-bearing binding evidence is the per-L `alpha(L)` table from the
  same-convention runner stack listed in **What Was Run**, not the
  reconciliation overview)

and read that runner exactly as labeled: a same-convention sweep, not a global
normalization adjudicator.

### 3. Not primary-architecture closure

The primary staggered architecture already has its own bounded open-cubic
trajectory companions:

- [`docs/STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md`](STAGGERED_NEWTON_REPRODUCTION_NOTE_2026-04-11.md)
- [`docs/STAGGERED_NEWTON_BLOCKING_SENSITIVITY_NOTE_2026-04-11.md`](STAGGERED_NEWTON_BLOCKING_SENSITIVITY_NOTE_2026-04-11.md)

This Wilson note strengthens the cross-architecture picture, but it does not
replace the primary staggered bounded story.

## Safe Claim

The safe bounded reading is:

> On the low-screening open-Wilson surface, the **test-mass** and
> **finite-L distance-law** companions support a Newton-compatible distance law and
> exact source-mass scaling within the shared Wilson convention, while full
> both-masses closure remains open.

## Promotion Boundary

Promote only as:

- a **bounded Wilson companion**
- paired with the existing Wilson open/two-body notes
- with explicit caveats that:
  - both-masses closure is still open
  - action-reaction remains unresolved
  - this is a same-convention Wilson result, not a global architecture claim
