# High-p Dispersion Tiebreaker

**Date:** 2026-04-09
**Status (narrowed 2026-05-18):** PARTIAL RESOLUTION — extending the momentum range to p=0–6 (from p=0–2) tabulates four candidate dispersion fits. The Schrödinger and Linear fits (both scored in ω-space) tie statistically (R²=0.97 vs 0.96, 4:4 per-seed split). The linearized Klein-Gordon fit (scored in ω²-space) reports R²=0.78 with 0/8 per-seed wins, but the R² values are **not directly comparable** to the ω-space fits without a same-dependent-variable refit; the original "Klein-Gordon eliminated" inference is therefore narrowed to an open follow-up (see audit-conditional repair section). The dispersion curve has structure beyond any simple two-parameter form: a smooth region at low p, a gap/dropout near p≈2.5, and steep negative ω at high p.

## Setup

- Fam1 grown DAG, H=0.5, 8 seeds
- p_z ∈ {0, 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0}
- Nyquist = π/H = 6.28

## Key result: tabulated R² values (comparator scope caveat)

| Form | R² (seed-mean, 12 pts) | Per-seed winner tally |
| --- | ---: | ---: |
| **Schrödinger** (ω-space residual) | **0.974** | **4/8** |
| Linear (ω-space residual) | 0.958 | 4/8 |
| Klein-Gordon, linearized (ω²-space residual) | 0.780 | 0/8 |
| sqrt-KG (ω-space residual) | −0.59 | 0/8 |

**Caveat (added 2026-05-18, see audit-conditional repair section below):**
The Schrödinger / Linear / sqrt-KG R² values are computed against residuals
in ω-space, while the linearized Klein-Gordon R² is computed against
residuals in ω²-space (the fit is ω² = a·p² + m²). These R² values are
**not directly comparable** across the variants because they refer to
different dependent variables. The original "Klein-Gordon eliminated"
inference is therefore narrowed: the linearized-KG ω²-space fit does not
match the Schrödinger/Linear ω-space fits, and a same-dependent-variable
refit is queued as follow-up before any elimination claim is closed. The
sqrt-KG variant (ω-space) is consistent across the comparator, and is
clearly worse than Schrödinger/Linear on this momentum range.

What can be reported without the comparator issue:
- The per-seed winner tally (0/8 for both KG variants) is comparator-
  agnostic in the sense that each seed's ranking is internally consistent,
  but the tally still inherits the ω vs ω² R² choice for each variant.
- The Schrödinger (R²=0.97) vs Linear (R²=0.96) ω-space comparison is
  apples-to-apples and gives a 4:4 per-seed split — no clean winner.

## What the dispersion actually looks like

| p | <ω> | σ | R² | Phase? |
| ---: | ---: | ---: | ---: | --- |
| 0.0 | +0.535 | 0.009 | 0.999 | Smooth |
| 1.0 | +0.477 | 0.009 | 0.998 | Smooth |
| 2.0 | +0.207 | 0.023 | 0.992 | Smooth |
| 2.5 | — | — | — | **Dropout** |
| 3.0 | −0.308 | 0.043 | 0.967 | Noisy |
| 4.0 | −0.983 | 0.241 | 0.984 | Noisy |
| 5.0 | −1.295 | 0.413 | 0.955 | Very noisy |

Three regimes:
1. **p < 2:** Clean, concave-down (KG-like curvature), all 8 seeds clean
2. **p ≈ 2.5:** Mode drops out — fewer than 3 seeds give clean phase
3. **p > 3:** ω goes large negative, high seed variance, mixed curvature

The curvature diagnostic (d²ω/dp²) is **concave down** at p < 2 and **flips sign** at p > 3. This is consistent with band structure rather than a simple free-particle dispersion.

## Interpretation

The lattice has finite transverse extent PW=6 with spacing H=0.5, giving 25 transverse nodes per layer. The first Brillouin zone boundary is at p ≈ π/H = 6.28, but effective boundary effects start much earlier because:
- The angular weight exp(−β·θ²) with β=0.8 cuts off modes with θ > ~1 rad
- The transverse connectivity (max_d=3·H = 6 nodes) limits high-p propagation
- The DAG's random node positions alias high-p modes

The dropout at p≈2.5 likely marks where the mode's wavelength λ = 2π/p ≈ 2.5 becomes comparable to the effective transverse connectivity range, causing the mode to decohere across seeds.

## What this establishes (revised 2026-05-18)

1. **Linearized-KG ω²-space fit vs Schrödinger/Linear ω-space fits do
   not agree** under the runner's current comparator (R²=0.78 vs
   0.97/0.96), and the linearized-KG variant wins 0/8 per-seed. The
   stronger claim that "Klein-Gordon is eliminated as a relativistic
   propagator" is **not closed** by the present table because the
   variants are scored against different dependent variables; a same-
   dependent-variable refit is queued as follow-up (see audit-
   conditional repair section).
2. **The Schrödinger fit works for p < 2** and marginally for the full
   range, but the dispersion has non-trivial band structure at p > 2.5.
3. **The earlier near-tie at p∈{0..2} was an artifact of the limited
   p-range**: at low p, Schrödinger and KG are both approximately
   quadratic. Whether the high-p extension actually breaks the
   degeneracy depends on the comparator-refit follow-up.
4. **Schrödinger and Linear are statistically tied** on the apples-to-
   apples ω-space comparison (R²=0.97 vs 0.96, 4:4 per-seed). The
   linear fit gives c = −0.387, i.e. a group-velocity-like slope of
   ≈ 0.39 at high p, but this should be read as a phenomenological
   fit-coefficient, not as a derived dispersion relation.

## Lensing and eikonal implications — split out as open follow-ups

The original version of this note carried two further inferences
("the −1.43 lensing slope is unaffected" and "the eikonal comparison
remains the best theoretical baseline because Klein-Gordon is
eliminated"). Both extend the tabulated numerical result into the
lensing/eikonal sector without a retained citation chain inside this
note's runner scope. They are therefore **split out as open follow-
ups** rather than supported claims:

- **(Open follow-up, lensing)** Whether the low-p regime (p ≈ 0.2–0.3)
  used in the lensing analysis is "well-characterized" by Schrödinger
  vs Linear on this DAG. The current table only documents that the
  low-p region is smooth and concave-down; mapping this onto the
  −1.43 lensing slope requires a separate retained derivation.
- **(Open follow-up, eikonal)** Whether the eikonal comparison is
  preferred over a KG-relativistic baseline. The original justification
  ("KG is eliminated → eikonal is the best baseline") depends on the
  KG-elimination claim that this revision narrows. Until the same-
  dependent-variable refit lands, neither baseline preference is
  established here.

Both items are flagged as out-of-scope for this row's numerical-
table-backed claim and will be promoted to their own source-rows if
and when a retained citation chain or independent derivation closes
them.

## 2026-05-18 audit-conditional repair: narrowed comparator scope + split lensing/eikonal implications

Per the 2026-05-17 audit verdict, the KG-elimination inference was not
closed because Schrodinger/Linear R² were computed in omega space while
KG R² was computed in omega-squared space. This revision narrows the
inference to "the linearized KG fit in omega-squared space does not match
the omega-space Schrodinger/Linear fits; a same-dependent-variable refit
is queued as follow-up". The lensing/eikonal extensions were also split:
they are now flagged as implications outside the runner-backed table
scope, awaiting either retained citation or independent derivation.

## Artifact chain

- [`scripts/dispersion_high_p_tiebreaker.py`](../scripts/dispersion_high_p_tiebreaker.py)

## Bottom line (narrowed 2026-05-18)

> "Extending the dispersion measurement to p=0–6 tabulates four fit
> variants. On the apples-to-apples ω-space comparison, Schrödinger
> (R²=0.97) and Linear (R²=0.96) are statistically tied with a 4:4
> per-seed split. The linearized-KG variant scored against ω²-space
> residuals reports R²=0.78 with 0/8 per-seed wins, but its R² is not
> directly comparable to the ω-space fits; a same-dependent-variable
> refit is queued before any KG-elimination claim is closed. The
> dispersion has non-trivial band structure at p>2.5 (mode dropout,
> curvature sign flip) that no simple two-parameter model captures.
> The earlier Schrödinger/KG near-tie at p∈{0..2} is consistent with
> both being approximately quadratic at low p. Lensing and eikonal
> implications are split out as open follow-ups awaiting a retained
> citation chain or independent derivation."
