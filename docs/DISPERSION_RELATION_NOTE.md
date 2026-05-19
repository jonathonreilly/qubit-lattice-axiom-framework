# Dispersion Relation: Geometry-Dependent, Not Decisively Relativistic or Non-Relativistic

**Date:** 2026-04-08 (updated same day with 3D + grown DAG results)
**Claim type:** bounded_theorem
**Status:** NARROWED (2026-05-18 audit-conditional repair) — under the
restricted runner packet currently attached to this note (primary runner
`scripts/lattice_dispersion_relation.py` + the 2D h=0.5 fresh stdout in
`logs/2026-04-08-lattice-dispersion.txt`), only the **2D regular-lattice
h=0.5** dispersion fit closes from sources in-tree. The 3D regular-lattice
and Fam1 grown-DAG conclusions previously summarized here depend on
omitted helper runners and logs and are **queued out-of-scope follow-ups**
pending attachment of their fresh stdout and sources. The narrowed bounded
claim of this note is the 2D h=0.5 Schrödinger fit result described in the
Result section below.

## Artifact chain

- [`scripts/lattice_dispersion_relation.py`](../scripts/lattice_dispersion_relation.py) — 2D lattice (h=1.0, h=0.5)
- [`scripts/lattice_dispersion_fine.py`](../scripts/lattice_dispersion_fine.py) — 2D lattice (h=0.25)
- [`scripts/dispersion_3d_lattice.py`](../scripts/dispersion_3d_lattice.py) — 3D regular lattice (h=1.0)
- [`scripts/dispersion_3d_fine.py`](../scripts/dispersion_3d_fine.py) — 3D regular lattice (h=0.5)
- [`scripts/dispersion_grown_dag.py`](../scripts/dispersion_grown_dag.py) — **Fam1 grown DAG** (H=0.5, H=0.35)
- [`logs/2026-04-08-lattice-dispersion.txt`](../logs/2026-04-08-lattice-dispersion.txt)

## Method

1. On a 2D regular lattice with the standard kernel `exp(i·K·L)·exp(-β·θ²)/L·h²`, initialize a plane-wave source at layer 0: `amp_j = exp(i·p·y_j)`.
2. Propagate forward (free field, no slits, no mass).
3. At each downstream layer, project onto the p-mode: `M(x) = Σ_j amp_j · exp(-i·p·y_j)`.
4. Extract `ω(p) = dφ/dx` from the unwrapped phase φ(x) = arg(M(x)).
5. Sweep p from 0 to 3.0 at two spacings (h=0.5, h=0.25).
6. Fit ω(p) to three candidate functional forms.

All phase fits are perfectly linear in x: R² = 1.0000000 at every (p, h) point tested at h=0.5, and R² > 0.9999 at h=0.25. The measurement is clean.

## Result

### Full geometry comparison

> 2026-05-18 audit-conditional repair: only the **2D lattice h=0.5** row
> below is in-scope for the bounded claim of this note. The other rows
> are retained for historical narrative continuity and are explicitly
> queued as out-of-scope follow-ups (see the audit-conditional repair
> section at the bottom of this note); they do not close from the
> currently attached restricted runner packet.

| Geometry | Schrödinger R² | Klein-Gordon R² | Linear R² | Winner |
| --- | ---: | ---: | ---: | --- |
| **2D lattice h=0.5 (IN-SCOPE)** | **0.99947** | 0.96156 | 0.92045 | Schrödinger (decisive) |
| 2D lattice h=0.25 (QUEUED — `scripts/lattice_dispersion_fine.py` source/log not in restricted packet) | 0.99827 | 0.73744 | 0.91395 | (queued) |
| 3D lattice h=0.5 (QUEUED — `scripts/dispersion_3d_fine.py` source/log not in restricted packet) | 0.677 | 0.656 | 0.404 | (queued) |
| Grown DAG H=0.5 (QUEUED — `scripts/dispersion_grown_dag.py` source/log not in restricted packet) | 0.994 | 0.992 | 0.877 | (queued) |
| Grown DAG H=0.35 (QUEUED — `scripts/dispersion_grown_dag.py` source/log not in restricted packet) | 0.988 | 0.980 | 0.949 | (queued) |

**In-scope finding (2D h=0.5 only):** On the 2D regular lattice at h=0.5,
the Schrödinger functional form is the decisive winner against
Klein-Gordon and linear alternatives (Schrödinger R²=0.99947 vs KG
R²=0.96156, linear R²=0.92045). The previously stated "critical finding"
that Schrödinger ≈ Klein-Gordon on the 3D grown DAG, and the broader
narrative that "the 2D result was misleading", depend on queued
out-of-scope rows above and are not in-scope under this note's narrowed
bounded claim.

### Fit parameters

| Parameter | h=0.5 | h=0.25 | Converged? |
| --- | ---: | ---: | --- |
| a (curvature) | −0.0919 | −0.0742 | Not yet (Δ=0.018) |
| b (rest phase) | −0.2365 | +0.4347 | Sign flipped |
| m_eff = −1/(2a) | 5.44 | 6.74 | Not yet |

The **functional form** (quadratic in p) is stable across refinement. The **coefficients** are not converged — the rest phase ω₀ = b depends on h because the per-edge phase K·h contributes a spacing-dependent background. This is expected: ω₀ is a gauge-like quantity that depends on the reference frame. The physically meaningful quantity is the curvature a = 1/(2m_eff), which changes by 19% between h=0.5 and h=0.25 (improving but not converged).

### Raw data (h=0.5)

| p | ω | R² |
| ---: | ---: | ---: |
| 0.00 | −0.2365 | 1.000 |
| 0.10 | −0.2380 | 1.000 |
| 0.30 | −0.2489 | 1.000 |
| 0.50 | −0.2661 | 1.000 |
| 1.00 | −0.3219 | 1.000 |
| 2.00 | −0.5940 | 1.000 |
| 3.00 | −1.0735 | 1.000 |

## Why it's Schrödinger

The angular weight `exp(−β·θ²)` at small angles gives `w ≈ exp(−β·(Δy/Δx)²)`. For a plane wave with transverse momentum p, the contribution from a node at transverse offset Δy picks up a phase factor `exp(i·p·Δy)`. The combined effect is:

```
Σ_Δy  exp(−β·(Δy/h)²) · exp(i·p·Δy) / L
    ∝ exp(−p²·h²/(4β))  (Gaussian integral)
```

This is a **Gaussian damping in p-space** which, per layer, gives a phase advance:

```
ω(p) ≈ ω₀ − α·p²
```

with α determined by β and the edge geometry. This IS the discrete Schrödinger propagator kernel: the Gaussian angular weight plays the role of the non-relativistic kinetic energy `exp(i·p²/(2m)·Δt)`, except with a real (damping) exponent instead of imaginary (oscillatory). The two give the SAME dispersion relation shape (quadratic in p), differing only in whether the propagation is unitary (imaginary exponent) or decaying (real exponent).

## Implications

> 2026-05-18 audit-conditional repair: the in-scope implications under
> the narrowed bounded claim of this note are the 2D h=0.5 lattice ones
> only. The 3D / grown-DAG implications below are retained as historical
> narrative and queued out-of-scope until their helper-runner sources
> and fresh stdout are attached. They do not load-bear under the narrowed
> claim.

### For the continuum limit (2D h=0.5 — in-scope)

The 2D h=0.5 regular-lattice Schrödinger dispersion fit (Schrödinger
R²=0.99947 vs KG R²=0.96156) provides a prediction for what the 2D
continuum theory of the free propagator with the standard kernel should
look like at this spacing: quadratic ω(p) curvature with the fit
parameters in the Fit-parameters subsection.

### Queued (out-of-scope under restricted runner packet)

**For the lensing invariant (QUEUED):**
The lensing work found kubo_true(b) ∝ b^(−1.43) and all attempts to derive it from relativistic ray optics failed. This was previously argued to be EXPLAINED if the propagator is Schrödinger and not relativistic. ~~The correct comparison for the −1.43 slope is non-relativistic scattering from a 1/r potential~~ — RETRACTED in the original 3D follow-up because the grown DAG does not decisively distinguish Schrödinger from Klein-Gordon. Both the original explanation and the retraction depend on the queued 3D / grown-DAG runners and are out-of-scope here.

**For the continuum limit on 3D / grown DAG (QUEUED):**
The previously stated claim that "the 3D / grown-DAG continuum theory is less clear — the dispersion form is not yet determined" depends on the queued 3D and grown-DAG runners.

**For the project's physics claims (QUEUED):**
~~Any claim about "emergent general relativity" is premature: the propagator is fundamentally non-relativistic~~ — the original NARROWED statement that "the propagator's dispersion type is undetermined on the grown DAG" depends on the queued grown-DAG runner and is out-of-scope under this note's narrowed bounded claim. No claim about the 3D / grown-DAG dispersion type is asserted here.

## What this does NOT establish (under narrowed 2D h=0.5 scope)

- The 3D regular-lattice dispersion (queued; depends on
  `scripts/dispersion_3d_lattice.py` and `scripts/dispersion_3d_fine.py`).
- The Fam1 grown-DAG dispersion (queued; depends on
  `scripts/dispersion_grown_dag.py`).
- The h=0.25 2D lattice convergence behavior (queued; depends on
  `scripts/lattice_dispersion_fine.py`).
- Whether a different angular weight could give decisive Klein-Gordon.
- Whether the −1.43 lensing slope matches non-relativistic OR relativistic scattering theory.
- The continuum-limit value of m_eff (parameters not converged at h=0.5 alone).
- Any statement that the 2D Schrödinger result transfers or fails to transfer to 3D / grown-DAG geometry under this note's narrowed bounded claim.

## 3D correction: what changed (QUEUED — historical narrative, out-of-scope)

> 2026-05-18 audit-conditional repair: this subsection is retained for
> historical continuity but is out-of-scope under the narrowed bounded
> claim of this note. The three numbered points below depend on the
> 3D regular-lattice and grown-DAG runners whose sources and fresh
> stdout are not attached in the current restricted packet.

The original analysis (2D only) concluded "decisively non-relativistic." The 3D follow-up (same day) was previously summarized as **misleading**:

1. **3D regular lattice**: neither form fits (band structure, R²<0.68). The extra transverse dimension creates non-trivial band effects absent in 2D.
2. **3D grown DAG**: the randomness smooths out the band structure (R²≈0.99), but Schrödinger and Klein-Gordon become nearly indistinguishable.
3. **Implication**: the clean 2D Schrödinger result is a property of 2D geometry + the angular weight, not necessarily of the 3D propagator. The actual physics geometry doesn't pick a winner.

These three points remain queued pending attachment of the helper-runner sources and fresh stdout.

## Frontier map adjustment (QUEUED — historical narrative, out-of-scope)

> 2026-05-18 audit-conditional repair: this table is retained for
> historical continuity but is out-of-scope under the narrowed bounded
> claim of this note. Each "After 3D correction" cell depends on the
> queued 3D and grown-DAG runners.

| Row | Before (2D only) | After 3D correction (QUEUED) |
| --- | --- | --- |
| Propagator type | "Schrödinger (decisive)" | Undetermined on grown DAG; Schrödinger ≈ KG (R² Δ=0.002) |
| Lensing failure explanation | "Expected: propagator is non-relativistic" | Cannot determine; both relativistic and non-relativistic remain viable |
| Next lensing direction | "Non-relativistic 2D Born scattering" | Need to test both NR and relativistic predictions against the 3D data |

## Bottom line (narrowed to 2D h=0.5 in-scope scope)

> "On the 2D regular lattice at h=0.5, the free-propagator dispersion
> relation fits the Schrödinger functional form decisively (R²=0.99947)
> against Klein-Gordon (R²=0.96156) and linear (R²=0.92045) alternatives,
> with the fit parameters and raw-data points listed above. No claim
> about 3D regular-lattice, 2D h=0.25, or Fam1 grown-DAG dispersion is
> asserted under this note's narrowed bounded claim; those geometries
> are queued out-of-scope follow-ups pending attachment of their helper
> runners' sources and fresh stdout."

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `3d_correction_master_note` (see-also; the 3D follow-up note that documents the corrections summarized above; converted from markdown link to backticked form 2026-05-10 to break citation cycle-0003 — this back-reference is informational only, with the load-bearing direction running `3D_CORRECTION_MASTER_NOTE.md` → `DISPERSION_RELATION_NOTE.md` as the forward update record)

## 2026-05-18 audit-conditional repair: narrowed to primary 2D h=0.5 runner scope

Per the 2026-05-17 audit verdict, only the 2D h=0.5 regular-lattice fit numbers
close from the primary runner + fresh stdout in the restricted packet. The 3D
regular-lattice and Fam1 grown-DAG conclusions depend on omitted helper runners
and logs. This revision narrows the bounded claim to the 2D h=0.5 result only,
and queues the 3D / Fam1 grown-DAG conclusions as out-of-scope follow-ups
awaiting attached fresh stdout + sources for `lattice_dispersion_fine.py`,
`dispersion_3d_lattice.py`, `dispersion_3d_fine.py`, and `dispersion_grown_dag.py`.

Concretely, the narrowing applied above:

- Marked the **2D lattice h=0.5** row as IN-SCOPE in the geometry-comparison
  table and tagged the 2D h=0.25, 3D-lattice, and grown-DAG rows as QUEUED
  with named missing-runner pointers.
- Rewrote the "Critical finding" prose so the in-scope assertion is the
  decisive 2D h=0.5 Schrödinger fit; the "2D result was misleading"
  narrative is explicitly moved out-of-scope.
- Rewrote "Implications" to keep only the 2D h=0.5 continuum-limit
  implication in-scope; moved lensing, 3D continuum, and project physics-claim
  implications into a "Queued (out-of-scope under restricted runner packet)"
  subsection that names the missing helper runners.
- Rewrote "What this does NOT establish" to enumerate the queued items
  by missing helper runner.
- Tagged the "3D correction: what changed" and "Frontier map adjustment"
  sections as QUEUED / historical narrative, out-of-scope.
- Rewrote "Bottom line" to assert only the 2D h=0.5 result and explicitly
  decline any 3D / grown-DAG dispersion claim under the narrowed scope.

This is a scope narrowing only. No data is fabricated, no number is changed,
and no claim that the audit closed is asserted; the previously stated 3D and
grown-DAG content is preserved verbatim in QUEUED subsections so that a future
repair PR attaching the helper-runner sources and fresh stdout can promote
those rows back to in-scope without re-stating their numbers.
