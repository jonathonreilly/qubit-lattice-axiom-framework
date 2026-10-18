# Exercise: the hierarchy wall (2026-10-18)

## The wall in plain words

The weak-force scale is about 10⁻¹⁷ of the grid's own scale, and fermion masses span about 10⁶. We want the grid's rules to produce these tiny numbers instead of having them put in by hand. The scale-ladder campaign (PR #9783) showed that climbing from the grid to everyday scales cannot do it. See WALL.md.

## What the exercise did

1. **Four simulated physicists**, each Opus 5.5 at xhigh, same family as the supervisor. Each read the axioms and primitive rules and checked main for prior art, then proposed routes and ran first tests:
   - R1, particle naturalness: clockwork, relaxion, supersymmetry, compositeness, warping, anthropic selection;
   - R2, condensed matter: tunnelling order, codes;
   - R3, quantum gravity and information: counts, entropy, cosmology;
   - R4, dynamical systems and RG: integer balance, slow passage, spirals.
2. **A kill round** on every route.
3. **The decisive test of the last open route**: does a spiral appear in the RG flow of irreversible record formation?

## Results (checked or proved; none refereed by another vendor)

| Route | Verdict after the kill round | What it established |
|---|---|---|
| Clockwork / walls (R1) | KILLED as a source of v | Bulk covariance gives only a decay length. Walls in Z³ leave 2+1D physics. A lattice of walls slows light fields by the same factor. Taste clockwork needs a supplied ratio. |
| Relaxion (R1) | Kill survives (toy only) | A local relaxion's floor tracks the size of the scanned region, not the rate. |
| Tunnelling order (R2) | Survives | The rule alone can force minimal flips of 18–62 sites, giving tiny amplitudes from O(1) couplings. But finite flips never link periodic vacua (Lemma 2), and the endpoints are detuned. So the result is a scale for heavy objects or defects, not v. Vacuum splittings need a region size L. |
| Counts and cosmology (R3) | Growing counts killed by data | Every growing count drifts v by 10⁵ × the clock bounds. The frozen horizon count (R_Λ/a ≈ 10⁶¹) merges this wall into Lane 5. |
| Integer balance (R4) | Wounded | It reduces to a supplied amplitude ratio (about 40, shared-rate case) or to n small factors. Main's α¹⁶ fits that shape, with nothing selecting the 16. |
| Slow passage (R4) | Survives in 1D | A hierarchy needs a ghost tuned to below 1%, or weak coupling. |
| Spiral (R4, kill-corrected) | **ABSENT in the native class** | Lemma C: bounded-rate, irreversible formation has a finite correlation length at every coupling. So there is no fixed point to spiral around, and a long passage needs a rate ratio of at least e^35. |

## What the wall is now (reading)

Every route tried trades the hierarchy for a number the axioms do not fix. The candidates:
- an integer extent, such as a region size or wall spacing;
- a ratio of rates or amplitudes;
- a frozen cosmological count;
- a supplied coupling, which HIER-3 places at g² ≈ 0.285.

This is consistent with a general observation from R4: an exact self-consistency gives exact marginality and no scale, so a hierarchy is always the size of a small miss.

The exercise did **not** prove that an extra number is unavoidable in general. It proved it only within each class above.

## Light-cone test (T-LIGHTCONE, run on request)

- **Reading: OPEN under the registered rule. In substance, no native slow passage.**
- The landed level-time bilayer is an O(3) Heisenberg critical point, and its relevant exponent is y_t ≈ 1.40, which is fast. Using it for a hierarchy needs a supplied tuning of β to about 1e-23.
- There is no spiral.
- The one near-marginal direction known for this class, cubic anisotropy, is exactly zero by symmetry.
- OPEN only because the slowest irrelevant exponent was not resolved, and irrelevant directions cannot make a scale.

## Still open

- **Symmetric defect pairs** (R2). These would give a defect-level scale only.

## Files

- WALL.md and TESTS.md.
- R1–R4/, K/ and T/, each with REPORT.md, scripts and outputs.
