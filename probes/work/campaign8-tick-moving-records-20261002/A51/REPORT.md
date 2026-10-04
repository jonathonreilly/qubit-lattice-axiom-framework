# A51 report: long-reach inverse search for the parton background

Everything is in `SP/c8/A51/`, where SP is `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. The running log is `NOTES.md`; `chain.log` holds every run's output. I made no repo edits, git writes or PRs, and ran no audit or review lanes. Every rule here is a supplied exploration under decisions 22 and 28; nothing is adopted.

## 1. Verdict

- **No reach makes the parton nearly steady in a way specific to it (CHECKED).**
  - At fixed reach the floor does not shrink with size. With |d|² ≤ 4 the lowest relative variance is 0.0032, 0.0029 and 0.0029 at 6³, 8³ and 10³. With |d|² ≤ 12 it is 0.0028, 0.0022 and 0.0023.
  - Longer reach does lower it at fixed size: to 0.0026, 0.0015 and 0.00075 at full reach. But the gain comes from smooth terms spanning the whole torus that measure long-wavelength spin fluctuations. The single smallest-q term alone gives 0.0077, 0.0025 and 0.00098, close to S(q_min)².
  - Once long wavelengths (|q| ≤ π/2) are removed from the rule's size, the floor is flat in both reach and size, at 0.0054–0.0073.
- **The weakly ordered references gain at least as much from reach (CHECKED).**
  - The Néel/parton ratio falls with reach: 1.34 → 1.19 at 6³ and 1.78 → 1.35 at 8³.
  - At 10³, projected Néel (m = 0.05) ends *below* the parton: 0.00051 against 0.00075.
  - A columnar dimer (valence-bond) state is an EXACT eigenstate of a closed-form covariant two-place rule of reach |d|² ≤ 12. Being steady is cheap.
  - Haldane–Shastry-like 1/r² profiles do poorly (0.011–0.046).
- **Forward test: the parton beats every rival tried, but is not the calmest state where that can be checked exactly (CHECKED).**
  - Under its own finite-reach best rule it lies below projected Néel and collinear states by 7–13σ at 6³, 8³ and 10³. The margins do not shrink, so the A45 criterion is met against this set of rivals.
  - However, the rule's classical (Luttinger–Tisza) minimum is degenerate over a large volume of the zone, and every collinear spin-wave state is unstable.
  - On the 16-site cluster, the exact ground state of the same short rules lies 0.54–0.56 per site (about 0.12 per unit rule size) below the parton, with overlap 2×10⁻⁴.
  - **How far must the rule reach?** No finite reach found.

## 2. Question

With rules allowed beyond six neighbours, is there a covariant rule under which the parton (λ′ = 0, and 0.1) is nearly steady and also the calmest state? How far must such a rule reach?

## 3. Answers

### 3.1 Basis and two traps

- **Basis.** Dual-frame Heisenberg class sums O_c = Σ_{torus pairs in class c} σ_i·σ_j, one per class of |d_a| (up to signs and permutations) with folded components ≤ L/2. That gives 19, 34 and 55 classes at 6³, 8³ and 10³, plus A49's eight four-spin star terms.
- **Covariance (EXACT, CHECKED).** The soldered image is Σ_b ε_b(d) σ^bσ^b with ε_b(d) = (−1)^{d_{b+1}+d_{b+2}}. A turn sends the complement pair {b+1, b+2} to {π(b)+1, π(b)+2}, so ε is invariant.
  - For 11 classes up to (1,3,4): covariance defect 0.0, and each image equals its own 24-turn average to 4e-16.
  - The (0,0,1) image equals A49's dual J1 to 6e-17.
- **Estimator (EXACT).** σ·σ conserves S^z, the parton is an exact singlet in S^z = 0, and every operator is dual-SU(2) invariant. So the rank-0 estimator in S^z = 0 gives the full covariance.
- **Cross-check against A49** (plain metric, same operator sets):

| Set | A51 6³ | A51 8³ | A51 10³ | A49 6³ / 8³ |
|---|---|---|---|---|
| 3 invariant bilinears | 0.0412(20) | 0.0410(50) | 0.0428(60) | 0.0399(11) / 0.0402(69) |
| S1inv (11 operators) | 0.00291(30) | 0.00281(20) | 0.00287(20) | 0.00257(21) / 0.00247(20) |

  All agree within about 1σ.

- **Trap 1: the Casimir (EXACT).**
  - The sum of all classes is 2S² − 3N/2, which annihilates every singlet up to a constant. So the full-reach minimum in the plain metric is trivially zero: it came out at −1.3e-14, at the all-ones vector to within 6e-11.
  - Fix: I measure a rule's size modulo the Casimir (G′ = G − ggᵀ/‖Cas‖²) and minimise over the quotient (a Schur-complement solver, unit-tested against brute force to 1e-8).
- **Trap 2: long-wavelength terms (ARGUED + CHECKED).**
  - A q-orbit term P_Q has relative variance ≈ S̄(Q)² in a Gaussian estimate; for any singlet or spin liquid, S̄ → 0 as q → 0.
  - Measured at the smallest Q: 0.0077 against S̄² = 0.0073 (6³), 0.0025 against 0.0027 (8³), 0.00098 against 0.0012 (10³). S̄(2π/L) behaves roughly as q^1.8.
  - I therefore also report an "LW" metric, which removes the Casimir and all q-orbits with |q| ≤ π/2 from the rule size.

### 3.2 Relative variance against reach and size (parton λ′ = 0; four-spin set; Casimir-removed metric; 16-block jackknife)

| Reach, \|d\|² ≤ | 6³ | 8³ | 10³ |
|---|---|---|---|
| 4 | 0.00319(37) | 0.00292(22) | 0.00286(20) |
| 9 | 0.00280(30) | 0.00236(12) | 0.00242(20) |
| 12 | 0.00275(40) | 0.00219(10) | 0.00225(20) |
| 27 | **0.00263(40)** (full) | 0.00170(10) | 0.00141(7) |
| 48 | — | **0.00154(11)** (full) | 0.00092(7) |
| 75 | — | — | **0.00075(5)** (full) |
| Two-place terms only, full reach | 0.0061(11) | 0.00189(20) | 0.00077(5) |
| LW metric, \|d\|² ≤ 4 → full | 0.0073 → 0.0065 | 0.0059 → 0.0054 | 0.0069 → 0.0061 |

- Samples: 34,138 at 6³, 9,448 at 8³, 3,259 at 10³.
- Bias corrections are at most 10%; for example, 0.00082 at full reach on 10³.
- **Does the minimum keep falling with reach?** Only in the Casimir-removed metric, and only through the long-wavelength mechanism. In the LW metric it is flat.
- **Does it shrink with L at the best reach?** It does at full reach, but that tracks S̄(2π/L)². At fixed reach it is L-independent.

### 3.3 References (same set and metric; |d|² ≤ 4 / full reach)

| State | 6³ | 8³ | 10³ |
|---|---|---|---|
| parton | 0.00319 / 0.00263 | 0.00292 / 0.00154 | 0.00286 / 0.00075 |
| λ′ = 0.1 | 0.00332 / 0.00245 | 0.00281 / 0.00137 | — |
| Néel, m = 0.05 | 0.00427 / 0.00313 | 0.00520 / 0.00208 | 0.00443 / **0.00051** |
| collinear, m = 0.1 | 0.00576 / 0.00312 | 0.00488 / 0.00182 | — |
| 0-flux projected Fermi sea (singlet) | 0.088 / 0.031 | 0.086 / 0.020 | — |
| Néel/parton ratio, LW metric (short → full) | 1.38 → 1.38 | 1.86 → 1.56 | 1.52 → 1.48 |

- **Does the gap to the ordered references widen?** No. It narrows in the Casimir-removed metric, inverts at 10³, and is flat at about 1.4–1.6 in the LW metric.
- λ′ = 0.1 matches λ′ = 0 at every reach, within error.
- The 0-flux Fermi sea is 10–30× worse, so the search does tell π-flux from 0-flux.
- **Columnar VBS (EXACT, CHECKED).**
  - A product of dimer singlets is annihilated by the inter-dimer coupling exactly when J₁₁ + J₂₂ = J₁₂ + J₂₁ for every pair of dimers.
  - Solved by hand: J = j on (001), (011), (111); j/2 on (002), (012), (112); j/4 on (022), (122); j/8 on (222); zero beyond.
  - The VMC minimiser at |d|² ≤ 12 is exactly this vector, with zero spread across samples. The control is the parton under the same rule: relative variance 0.027.
  - The VBS has structural zeros, but for two-place rules VMC sees exactly 1/3 of each dimer-pair excitation, so zero here means zero (EXACT).
  - The VBS values in the four-spin set are not claimed.

### 3.4 The best rule's profile; Haldane–Shastry-like ansatz

- **Finite-reach best rules** (every class with components < L/2, plus four-spin terms; J_NN = 1; all couplings antiferromagnetic):
  - **6³** (components ≤ 2): face-diagonal 0.775(9), (111) 0.057(25), (002) 0.370(14). Everything beyond is ≤ 0.03 and consistent with zero, so the rule is effectively star-supported.
  - **8³** (≤ 3): 0.807, 0.225, 0.412, 0.149, 0.128, 0.084, 0.062, …, then 0.009 at |d| = 4.1 and 0 at 4.7.
  - **10³** (≤ 4): 0.84, 0.43, 0.53, 0.34, 0.31, 0.25, 0.21, …, then 0.06 at |d| = 4 and about 0 at 5.7.
  - **Fits.** Exponential decay fits better than a power law at 10³ (ξ = 1.09, χ² 67, against α = 2.3, χ² 223), though neither fits well; at 8³ both are poor (ξ 0.63, α 3.4).
  - **Reading.** The profile's width grows with whatever reach is allowed while the LW floor stays flat. The extra reach builds a small-q filter, not a physical tail. Its J(q) is a sharp peak at q = 0 over a flat floor.
- **Full-reach rules.** Antiferromagnetic out to |d| ≈ 4, then a negative far tail (−0.28 at (4,4,4) on 8³), which is the long-wavelength admixture. The power-law fit there (α = 1.67) is not meaningful.
  - At full reach a rule is defined only modulo the Casimir. I fixed it with the most-local gauge.
- **Four-spin coefficients** stay large relative to J_NN: C0 0.54–1.0, T0 0.44–0.84.
- **Haldane–Shastry-like ansatz** (J ∝ s(d)/D², with D² = Σ_a (L/π)² sin²(πd_a/L)):
  - All antiferromagnetic: 0.046, 0.028 and 0.023 at 6³, 8³ and 10³; with the star four-spin terms optimised on top, 0.018, 0.014 and 0.011.
  - Staggered or fitted signs: 0.04–0.2.
  - The best exponent is α = 1 (0.0039 at 10³ with four-spin terms), which is again small-q dominated.
- **Local cluster Casimirs** are not the rule. The star Casimir alone gives 2.0–2.8, or 0.0047–0.0052 with four-spin terms; the cube Casimir gives 0.023–0.035.

### 3.5 Forward test (CHECKED)

- **Luttinger–Tisza** (40³ grid, finite-reach rules). The fraction of the zone within 1% of the span above the minimum is 19%, 23% and 47% for the 6³, 8³ and 10³ rules; within 5% it is 45%, 61% and 92%. The minimum set is volume-like, which means extreme frustration with no unique order.
- **Spin waves.** I tested ferromagnet, (π,0,0), (π,π,0) and Néel, with the four-spin terms in Hartree form (exact at quadratic order for collinear states). All are unstable at 6³ and 8³. Classical collinear energies are ≥ −0.80 per site, against the parton's −1.66 to −1.73.
- **VMC contest under the parton's own finite-reach rule** (J_NN = 1; ref − parton per site):

| | 6³ (norm 4.61) | 8³ (norm 4.79) | 10³ (norm 5.79) |
|---|---|---|---|
| parton E/site | −1.72680(12) | −1.69469(11) | −1.66264(14) |
| λ′ = 0.1 | +0.00014(20) | −0.00008(22) | — |
| Néel, m = 0.05 | +0.00270(36), 7.5σ | +0.00360(47), 7.6σ | +0.00374(45), 8.4σ |
| collinear, m = 0.1 | +0.00389(30), 13σ | +0.00471(39), 12σ | — |
| 0-flux Fermi sea | +0.318 | +0.271 | — |
| columnar VBS | +0.225 | +0.195 | — |

  - The 6³ rule carried over to 8³ gives the same ordering: +0.0030(5) and +0.0053(4).
  - I report the contest only for finite-reach rules. At full reach a Casimir admixture shifts non-singlet energies by 2μ⟨S²⟩/N, which is comparable to these margins.
- **16-site exact test** (A49's fwd16 machinery; the |d|² ≤ 4 rules from 6³ and 8³):
  - E₀/N = −2.335 and −2.303, against the parton's −1.775 and −1.766. Overlap with the ground state is 0.0002; Néel and collinear sit just above the parton.
  - That the parton also lies well below the true calmest state at 6³ and 8³ is ARGUED, not checked.
- **Side result.** Under the VBS's own exact parent rule, the VBS sits at −1.5 per site and the parton at −1.5008, a tie within error. Being an exact eigenstate does not imply being the calmest state.

## 4. Methods

- **Frames.** As in A44/A49: operators in the soldered frame, states in the Klein-dual frame.
- **States.** I extended A49 code (`a51lib.py`, which imports `a49lib`/`a46lib`). New states are:
  - columnar VBS: dimer orbitals, with a fixed starting configuration;
  - 0-flux projected Fermi sea: spin-independent hopping with a slight twist.
- **Class estimators.** The full ratio matrix G = P_a Q (N×N), then X0_ij = z_i z_j + (1 − z_i z_j)(R_i R_j − G_ij G_ji), binned by class. Cost was 10 ms (8³) and 40 ms (10³) per sample.
- **VMC.** The A44/A46/A49 move set (nearest-neighbour exchanges at fixed S^z = 0). One 268-second batch gives about 17k samples at 6³, about 3.15k at 8³, and about 650 at 10³ with 100 thermalisation sweeps.
- **Analysis.**
  - Per-site covariance C and per-site Gram matrix G (diagonal 3m_c/2 for classes; A49's G4 for the four-spin terms).
  - Metrics: Casimir-removed, and LW. Both minimise over the quotient.
  - Errors: jackknife for relative variances, binning for energies.
- **Forward tools.** LT on the L-grid and on a 40³ grid; single-Q spin waves (`fwd51.py`); 16-site Lanczos (`fwd16_51.py` with `rules16.npz`).

## 5. Checks

| Run | Runtime | Peak memory |
|---|---|---|
| basis51 (covariance, tables, timing) | 8.7 s | 638 MB |
| VMC 6³: 3 parton batches + 4 references | 268 s each | 68–75 MB |
| VMC 6³: pol / cs / VBS controls | 6 / 7 / 50 s | 54–59 MB |
| VMC 8³: 3 parton batches + Néel, collinear, Fermi sea, λ′ = 0.1 | 268 s each | 93–193 MB |
| VMC 8³: VBS | 175 s | 93 MB |
| VMC 10³: 5 parton + 2 Néel batches | 269 s each | about 500 MB |
| fwd16_51 (16-site exact) | 85 s | 329 MB |
| analysis scripts (anal51, anal51b, fwd51, control51, vbs_check, qtest51, lswt_check, mk16) | 0.1–4.3 s | 28–199 MB |

- **Controls (all pass):**
  - Polarised product state: 7 predicted null classes, 7 eigenvalues ≤ 6e-16, next 0.44.
  - Compass-staggered product state: 9 predicted, 9 eigenvalues ≤ 2e-16, next 0.96.
  - Casimir estimator constant per sample to 9e-12 (6³), 1.4e-10 (8³) and 2e-10 (10³).
  - Spin waves reproduce A47's Néel J1–J2 value at j = 0.2: −0.9069 against −0.9072.
  - Nearest-neighbour ⟨σ·σ⟩ per bond: −1.0098, −1.0042 and −1.0031, in line with A44.
  - Matrix-update drift ≤ 5e-11.
- **Run conditions.** Every run went through run.sh, one at a time. Load was 2.8–4.7 and free memory 30–39%. There were 4 SKIPPED attempts, all because my own orphaned job held the lock. The lock is now free.
- **Flagged:**
  - The first two 10³ batches hit the 288-second alarm during thermalisation and saved nothing; a third I killed. Fixed by capping time during thermalisation as well.
  - My first pass wrongly put the VBS's relative variance at zero in the four-spin set. That claim is withdrawn (§3.3).
  - A full-reach row in the LW metric was wrong before I added the quotient solver. It has been corrected.
  - run.sh tags drop the seed, so per-batch output files were overwritten; `chain.log` keeps all of them.

## 6. Open edges

1. Long-range four-spin terms, and the full covariant weight-4 and weight-6 spaces.
2. Stronger rivals at 6³ and 8³: optimised projected states, or ground states of ED or DMRG quality. The exact test covers only |d|² ≤ 4 rules on 16 sites.
3. A measure of rule size that penalises all-to-all couplings on its own terms; the π/2 cut in the LW metric is a choice.
4. λ′ beyond 0.1, and λ′ in the full operator space.
5. Whether the columnar VBS is the calmest state of its closed-form parent rule.

## 7. Plain-language summary

We let the rule's links stretch as far as the grid allows, then searched again for a rule under which the two-part background barely changes. Longer links did reduce the leftover restlessness, but in a trivial way. Very long, smooth links only check how evenly spin is spread across the whole grid, and nearly any quiet-looking state passes that check. Slightly magnet-like states gained as much or more, and on the largest grid one beat the background. Once those trivial pieces are set aside, the restlessness stays the same however far the links reach and however big the grid. A simple pattern of locked pairs turned out to be perfectly steady under a short rule, so steadiness is easy to come by. Under its own best rules the background beat every rival we tried. But on a small grid that can be solved exactly, the true calmest state sits well below it.