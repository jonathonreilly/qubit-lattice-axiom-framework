# Kill agent: F1a, frozen random sites with metric-chosen neighbours

**Agent:** Claude Opus 5.5, extra-high (xhigh).
**Refresher read (stated):** the full axioms, the primitive registry check (all three primitives), the packet's route reports and scripts, TESTS.md, and the TEST_LOG sections on K3a″ and W1.
**Scripts:** `scripts/KF1a_K1 … K5` with their outputs. The N = 4096 runs of K1 were stopped unfinished, so N goes up to 2744.

## Verdict: DEAD as a separate route (it reduces to F1b)

This is a no-go claim, so the other-vendor referee is required. Its result goes in `agents/kill_F1a_referee.md` once it returns.

**Plain version.** Averaged over all possible random site sets, the vacuum does not resist shear. But physics happens in one site set, and in any one the resistance is a random patchwork:
- it does not thin out at long wavelengths;
- it wrecks gravitational waves within about a Planck length;
- it also pushes the metric around directly.

No grid spacing avoids both this and the observed cosmic-ray energies. The only way to remove the patchwork is to let the sites move, which is F1b.

## (2) The random part

- **White noise (CHECKED, K1).** The per-site stiffness and the first-order stress both have flat sd·√N.
  - The values are 0.064–0.069 at m² = 1 and 0.080–0.084 at m² = 0.04, with fitted exponents −0.485 to −0.524 ± 0.025 against −0.5 for white noise.
  - R3's 0.035–0.040 was a five-direction average, about 1.8× too small for one channel.
- **No conserved-charge suppression (EXACT sketch, the Last–Penrose chaos expansion).**
  - The variance of any windowed local functional of a Poisson set is |V|·Σₙ(ρⁿ/n!)∫fₙ², a sum of squares. So the noise is extensive (S(0) > 0) or zero.
  - Zero would need every kernel to vanish, i.e. adding a point never changes the global stiffness, which is false.
  - Only the first kernel vanishes, because the mean is zero at every density.
  - What would suppress it is force balance (∂ᵢτᵢⱼ = 0, S ∝ q⁴), and that **needs mobile sites**.
- **The relevant quantity is k → 0, and the disorder is relevant (EXACT power counting, the Harris criterion).**
  - A white random mass² has dimension 1/length in 3D.
  - The disorder-to-gradient ratio is (σ/π²M²)(λ/a)^½: 1 at λ ≈ 25–35a, and about 4e19 at LIGO wavelengths.
  - So the disorder is **strong at every sub-cutoff wavelength**, not merely a finite mean free path. About half of all large regions have a locally negative mass².
- **Born re-derived.** R3's c6 used V = 8δμ/M², where it should be 4δμ/M². With the per-direction σ, ℓ ≈ 0.19–0.27a, and Born itself fails. The "300 l_P" in ROUTES came from an unmeasured σ = 1e-3.
- **New: a random first-order TT stress, a tadpole (CHECKED).**
  - It is white: σ_τ ≈ 0.07–0.08 per site in 3D (K1) and 0.33–0.34 in 2D Delaunay (K2d).
  - The static response is ⟨hh⟩ ≈ 0.75·R/a (K3), so **the flat metric is not even a stationary point in a single configuration**.
  - The scalar twin: the vacuum-energy density is white (0.17–0.18 per site; Poisson number noise adds about 0.9), so the Newtonian-potential variance grows ∝ R (K4).
  - "CC-granted" tunes only the uniform constant.
- **No cutoff window (K3; the cosmic-ray floor is COMPARATOR).**
  - A mean free path above 1 Gpc needs a⁻¹ ≲ 1e7 GeV.
  - Carrying 3e11 GeV cosmic rays on a lattice with bounded bandwidth needs a⁻¹ ≳ 1e11 GeV.
  - At a⁻¹ = M_Pl, σ would have to shrink by about 1e30.
- **Delaunay, CHECKED in 2D only (K2).**
  - Per configuration, E(t) has concave kinks at flips: 1.6–2.0 flips per site per unit strain.
  - **At infinitesimal amplitude the Hessian is the glass value, +0.990 ± 0.004 per site.** The random part grows as t^1.54.
  - So Lemma L protects finite-strain response, not linear response about the vacuum (ledger row S2's 1PI mass).
  - The 3D status is unresolved.

## (1) Does it assume the target? Not on the mass (reading)

- The protecting symmetry belongs to a **supplied ensemble**. Per configuration only q = 0 is protected.
- The metric must be a supplied continuum field defined between sites, and Delaunay in g is not canonical for non-uniform g.
- The graviton itself is still supplied.

## (3) One light cone

- **Tree level is fine (CHECKED, K5).** Per configuration Σₑwₑeeᵀ = V·I to 1e-12, so the scalar's k → 0 speed is exactly 1.
- **Loops are not.** With continuous time and SL(3) only in law, nothing ties time to space, so species split at O(g²/16π²) (COMPARATOR: Collins). The graviton's ḣ² and (∇h)² coefficients also differ, at O(NΛ²/16π²M²) (ARGUED).
- **T1(b) is not yet run;** the agent predicts FAIL.

## (4) Beyond the stated price

- Admissibility's covariance has no group to act on in a single configuration.
- The kinetic-isotropy primitive's Z³ × Z_τ block is lost.
- Lemma L needs a probability law on site sets, and the realized-state primitive supplies no measure.
- Every noise-tolerant cutoff contradicts a⁻¹ = M_Pl.

## (5) Already tried: partly

- The viability map (`TOE_VIABILITY_MAP_..._2026-09-27.md:797-800`, viability branch) already said a random lattice is "isotropic on average, not zero".
- R65 (`ai/probes:archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md:4974-4981`) found that re-triangulation moves log det at O(1).
- New here: the exact zero mean, the tadpole, the relevance argument and the cosmic-ray window.

## (6) Terminal obligation: it reduces to F1b's

- Frozen Poisson sets cannot have zero per-configuration TT noise.
- Correlated frozen sets fail on the mean.
- Deterministic frozen sets are not SL(3)-invariant.
- Removing the noise needs dynamical averaging or force balance, and both need mobile sites.

**Recommendation:** retire F1a. Reopen it only for a frozen site law with an exact symmetry in every configuration (none is known). Lemma L/A survives only as an ingredient of F1b.
