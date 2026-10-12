# Lane RS, probe S2: gauge-mediated interactions (staggered QED at O(e²))

Worker: Claude Opus 5.5 (same family as the supervisor; not refereed). Run 19:50Z–20:15Z, 2026-10-10. No repository files edited.
Scratch: this folder. Scripts `s2_*.py`; outputs `s2_*.out`.

## Reading against the FIXED lines: FAIL (bounded). Needs a codex sol referee before it is recorded.

**Class tested:**
- Kogut–Susskind staggered fermions on Z^d (d = 2, 3; d = 1 control), mass m ∈ {0, 0.5}.
- Noncompact Yee photon in Coulomb gauge. Gauss's law is solved, which gives the instantaneous lattice Coulomb term plus 2 transverse polarizations with ω(p) = |2 sin(p/2)|.
- Minimal coupling U = e^{ieA}, expanded to O(e²). This gives:
  - the O(e) vertex, with form factor cos(K_i + p_i/2);
  - the O(e²) seagull, with form factor −sin(K_i + (p_i − p′_i)/2).
- Channels at O(e²):
  - Møller: Coulomb plus retarded transverse exchange, direct minus exchange;
  - Compton: s- and u-channel with the full 8-band resolvent (Z-graphs included), plus the seagull.

**Result.** No conserved charge has a nonzero taste-universal slope, and none has a nonzero photon slope.
- **Fermion slope.** For every conserved charge that is analytic in e and whose one-body symbol is C¹ (this includes every exponentially quasi-local density), the taste- and spin-averaged one-fermion slope is zero.
  - So no charge has a nonzero taste-universal slope at the taste corners.
  - Matrix-valued (taste × spin) charges are included. The averaged slope is the trace of a 4×4 matrix (2×2 in 2D).
- **Photon slope.** The polarization-averaged one-photon slope is also forced to zero, for any polarization-matrix photon charge.
- **Survivors in the direct matrix null spaces:** only number and energy, or number and photon number. All have zero slope.

## 1. Analytic results

**(A) Cherenkov bound. PROVED.**

For + band states and every full-zone transfer Q ≡ k − k′ (mod π-shifts), |ε(k) − ε(k′)| ≤ ω(Q), with equality only on a measure-zero set.

*Proof.* Write sin k′_i = ±sin(k_i − Q_i). Then:
- |√(a²+m²) − √(b²+m²)| ≤ |a − b|;
- |sin k_i − sin(k_i − Q_i)| = 2|cos(k_i − Q_i/2)|·|sin(Q_i/2)| ≤ 2|sin(Q_i/2)|.

Checked: over 4.8e5 random (k, k′, Q), the maximum of |Δε| − ω is −0.017 (`s2_control1d.out` (iv)).

Consequences:
- K3a's O(e) resonances are all band-changing, i.e. pair-type γ ↔ e⁺e⁻.
- The Born Møller amplitude has **no transverse pole**. It is real-analytic on the regular Møller manifold, away from the Coulomb forward point.

**(B) Reduction to the Born T-matrix. PROVED (same family). This is the standard on-shell elimination.**

Write Q = Q₀ + eQ₁ + e²Q₂ + … with [H, Q] = 0. Then:
- At O(e), Q₁'s off-shell part is fixed by [H₀, Q₁] = −[V, Q₀]. Its denominators do not vanish, by (A), and pair intermediate states cost energy.
- Q₀'s on-shell photon-changing part vanishes away from measure-zero resonance sets.
- At O(e²), between degenerate free two-fermion states, the intermediate-state charges cancel, the photon charge included. What remains is

  (P̃(k₃)⊗1 + 1⊗P̃(k₄)) T = T (P̃(k₁)⊗1 + 1⊗P̃(k₂)),

  with T = W_Coulomb + V(E − H₀)⁻¹V on the + band, antisymmetrized, and P̃ the + band block (n₊ × n₊, n₊ = 2^{d−1}) of Q₀'s one-body symbol.

This condition is necessary, not sufficient. It inherits the RN L2 referee's scope: regular families analytic in e, and a nonzero one-particle action.

**(C) Trace lemma. PROVED.**

Wherever T is invertible, D_out = T D_in T⁻¹, so tr D_out = tr D_in. So f(k) = tr P̃(k)/n₊ obeys the *scalar* collision equation f₁ + f₂ = f₃ + f₄.

- T is real-analytic on the regular manifold, by (A).
- It is invertible at every one of more than 3000 sampled shells (next paragraph).
- So det T ≢ 0, and T is invertible on a dense full-measure set. By continuity, a C¹ f satisfies the equation on the whole regular manifold. (This assumes the regular manifold is connected; that was not checked separately.)

Checked: in 3D, min-sv/max-sv of the 16×16 matrix T has minimum 6.5e-5 (m = 0.5) and 4.9e-6 (m = 0), with median ≈ 0.2. In 2D (4×4), the minimum is 1e-4 and the median 0.63 (`s2_moller_*.out`).

**(D) The staggered band is lattice Klein–Gordon. PROVED (an identity).**

ε_stag(k) = √(m² + Σ sin²k_i) = ½ ω_KG(2k; 2m), where ω_KG(q; μ) = √(μ² + Σ 4 sin²(q_i/2)). Checked to 0.0 (`s2_identity.out`).

Under k → 2k, conservation mod π becomes conservation mod 2π. So the scalar Møller relation for staggered fermions *is* the lattice KG relation at mass 2m.

- **m > 0.** The RN L2 referee-confirmed statement (Spohn: only aε + c, no nonzero odd periodic C¹ invariant) applies directly. So f has zero odd part, and **tr ∂_j P̃(0) = 0**.
- **m = 0.** Spohn's Hessian hypothesis fails at the cone point, so this case is CHECKED only (§2).

**(E) Analytic charges need only low-energy collisions. ARGUED.**

- For an exponentially quasi-local charge, the symbol is analytic.
- On a low-energy patch where only normal processes occur, collisions force f = a + b·k + cε locally (standard local collision-invariant lemma; not re-proved here).
- Analytic continuation then makes f − b·k − cε vanish identically on R^d.
- Periodicity then forces b = 0.

So **the obstruction is analyticity plus periodicity, not umklapp.** This agrees with L2 §1b.

**(F) Photon slope. PROVED, given (D) and invertibility of the Compton T_C.**

- **Trace lemma for Compton.** The trace lemma applied to the Compton T_C (size n₊(d−1)) gives f(k) + γ̃(p) = f(k′) + γ̃(p′), where γ̃ = tr g/(d−1) for *any* polarization-matrix photon charge g.
- **Chaining.** With f = a + cε, the function γ̃ − cω is constant on Compton-connected pairs. Forward-near Compton reaches an open set of p′ around every p, so γ̃ − cω is constant on the torus. The odd part of γ̃ is therefore zero.
- **No regularity of γ̃ is needed.**

Checked: T_C is generically invertible. In 3D (8×8), min-sv/max-sv has minimum 8.5e-3 and median 0.33. In 2D (2×2), T_C is proportional to a unitary (ratio 1.00 at all 600 shells).

**(G) Other processes can only remove invariants. PROVED.**

The conditions from different processes are conjunctive. So adding pair annihilation e⁺e⁻ → γγ, Bhabha scattering, or (in compact U(1)) the O(e²) γγ contact from the B⁴ term can only shrink the set of invariants. None of them can rescue a slope.

Compact link photons give the same Møller and Compton amplitudes at O(e²). The FAIL therefore carries over to perturbative compact QED.

**Answer to "do the different photon and fermion dispersions alone kill additive invariants?" No.**
- In the continuum, a massless photon and a massive electron conserve p.
- On a lattice patch, b·k + cε survives normal collisions.
- What kills the invariants is analytic periodic symbols plus zone-spanning collisions, the same mechanism as for one species.
- The photon's different dispersion only means that Compton alone suffices. The Compton-alone scalar null space is {0}; see §2.

## 2. Numerics (CHECKED)

**Common settings.**
- Fermion basis: sin(2n·k), |n|∞ ≤ R.
- Photon basis: sin(n·p).
- Tolerance: absolute 1e-10 plus relative 1e-9.
- Rows: sampled on-shell shells, with energy residual ≤ 1e-12.
- Sampling mix: generic, low total momentum K, and low energy.

| Test | Size | Null dim | sv min / max |
|---|---|---|---|
| 3D Møller, scalar odd f, m = 0.5 | R ≤ 4, 364 functions, 2400 shells | 0 | 0.508 / 3.04 |
| 3D Møller, scalar odd f, m = 0 | R ≤ 4 | 0 | 0.509 / 3.09 |
| 2D Møller, scalar odd f, m = 0.5 and m = 0 | R ≤ 8, 144 functions | 0 | 0.44 / 2.5 and 0.43 / 2.5 |
| 3D Compton alone, odd (f, γ̃) | 728 functions | 0 | 0.117 / 4.28 |
| 3D Compton + Møller | | 0 | |
| 3D γ̃ alone | 364 functions | 0 | |
| 2D Compton | | 0 | 0.11 / 2.6 |

**Direct matrix-valued null spaces** (`s2_matrix*.out`, `s2_matrix_compton*.out`).
- **The class:** every translation-covariant one-body operator of range r, with all 2^d sublattice/taste phases. [h, P] = 0 is *not* imposed, which enlarges the class. The photon is a 3×3 link-component matrix M(p) projected onto transverse polarizations. Its off-diagonal entries get both integer frequencies and frequencies shifted by (e_i + e_j)/2, which accounts for the twisted periodicity of the frame.
- **The redundancy is consistent in every run:** null dim = params − class dim + survivors.

| Run | Surviving + band symbols | Slopes | Smallest non-null sv / max |
|---|---|---|---|
| 2D, r = 2 and r = 4 | 2 | max slope-matrix entry ≤ 1.3e-11 | |
| 3D, r = 1 | 2 | all slopes zero | 27 / 1363 |
| 3D, r = 2 (2000 params, 400 shells) | 2 | all slopes zero | 2.34 / 2525 |
| 3D Møller + Compton, fermion r = 1, photon Rp = 1 | 2 | fermion slope ≤ 1.5e-12, photon slope ≤ 1.2e-14 | 0.15 / 427 |

- The two survivors are number and energy, or number and photon number. Their slope matrices are exactly zero, including traceless (non-singlet) slopes.
- The matrix runs' relative gaps (1e-3 to 2e-2) are 6–8 orders above the tolerance, but they are not order-one. The order-one gaps are in the scalar tests, which carry the proof via (C) and (D).

**Controls.**
- **e = 0.** There are no collision rows. The free taste-universal momentum ½ sin(2k_x)·1 lies in the r ≥ 2 class with + band slope matrix exactly diag(1, 1, 1, 1), and it is exactly conserved by the free Hamiltonian. With e ≠ 0 its Møller defect is O(1).
- **1D, m = 0.** The Coulomb T vanishes on every nontrivial generic shell (0 of 400). So every f passes: null 16 of 16. This is the solver's pass control.
- **1D, m = 0.5.** T ≠ 0 on every shell, and the odd null space is {0}.
- **1D special branch** K = π/2, (k, π/2−k) → (−k, π/2+k): sin 2k fails.
- **Permutation-only rows.** The null dim is the full 8 with absolute + relative tolerance. A relative-only rule would report 0 (the RN L2 referee's pitfall).
- **Ward identities** (`s2_ward.out`). The O(e) vertex obeys Σ ŝ_i V^i = [h, ρ] exactly (constant 1.000000, residual ≤ 2e-15). The seagull obeys its second-order gauge identity with constant −1.000000, residual ≤ 1e-15, in both 2D and 3D. So the form factors are verified.
- **Deliberate resonant sampling** (`s2_resonant.out`).
  - Near O(e) poles: of 30,000 shells, 0 lie within 2% of a pole. This is consistent with (A), so the Møller amplitude has no poles to sample.
  - K = 0 shells constrain no odd f (trivial).
  - Zone-boundary-K shells are consistent but underdetermined alone.

## 3. Other gauge-mediated class: Z₂ gauge field with staggered fermions (ARGUED, not run)

- In the deconfined regime (large plaquette K), the Z₂ gauge sector is gapped. It has no massless asymptotic species, so there is no photon-slope requirement.
- Integrating it out gives exponentially local multi-fermion interactions (ring exchange, at order Γ·t⁴/K and beyond). That is S1's class: short-range taste-matrix interactions.
- Wherever the effective two-body T is generically invertible, the trace lemma (C) and identity (D) apply unchanged. So the result is **the same condition and the same FAIL**, provided invertibility holds. That was not checked for Z₂.
- The confined and nonperturbative regimes are not covered.

## 4. Passer follow-through

None found. Stress, first-class closure, G and γ were not pursued.

## Scope: what is NOT covered

- Charges that are nonperturbative or non-analytic in e, and strong coupling, including compact-U(1) confinement in 2+1D.
- Charges whose one-particle action is zero at leading order but appears at a higher order in e (ARGUED to reduce to the same condition).
- Asymptotic and IR dressing beyond Born level. This does not affect the O(e²) on-shell identity.
- Connectivity of the regular Møller manifold (assumed in (C)).
- m = 0 is CHECKED only (the Spohn hypothesis fails at the cone).
- The full Dirac constraint analysis. This is lane RN's question and is not asked here.
- Non-analytic, power-law-tailed symbols. The momentum-cutoff construction from L2 remains a price option outside the locality class.

## Against the supervisor expectation

- **Matches:** FAIL (bounded).
- **Different mechanism:**
  - Taste structure does not supply discrete charges that help.
  - The generically invertible T-matrix collapses every matrix-valued charge onto its trace.
  - The staggered single-fermion collision problem is literally lattice Klein–Gordon at (2k, 2m).
- **No degenerate resonant submanifold rescue was found.**
- **The price is unchanged:** non-local momentum, or an exact lattice momentum not in the axioms.

## Labels and strong words

- **PROVED (same family, unrefereed):**
  - (A), the Cherenkov bound;
  - (B), the reduction, within the L2 referee's scope;
  - (C), the trace lemma;
  - (D), the identity;
  - (F), the photon chaining;
  - (G), monotonicity.
- **Conditional on CHECKED inputs:** the generic invertibility of T and T_C.
- **PROVED via cited theorem:** m > 0 rests on Spohn and the RN L2 referee's confirmed KG statement.
- **CHECKED:** all null spaces, gaps, controls and Ward identities.
- **ARGUED:** (E), the Z₂ reduction, and the higher-order slope.
- **"Exact"** is used only for the identities and the Ward checks with the stated residuals.

## Files

| Script | What it does | Outputs |
|---|---|---|
| `s2_core.py` | model, vertices, Møller T, sampler | — |
| `s2_ward.py` | Ward identities | `s2_ward.out` |
| `s2_moller.py` | T invertibility and scalar null spaces | `s2_moller_d{2,3}_m{0,0.5}.out` |
| `s2_matrix.py` | matrix Møller null spaces | `s2_matrix_d2_m0.5_r{2,4}.out`, `s2_matrix_d3_m0.5_r{1,2}.out` |
| `s2_compton.py`, `s2_compton_lib.py` | Compton | `s2_compton_d{2,3}_m0.5.out` |
| `s2_matrix_compton.py` | joint matrix test with the photon polarization matrix | `s2_matrix_compton_r1_Rp1.out` |
| `s2_resonant.py` | resonant-branch sampling | `s2_resonant.out` |
| `s2_control1d.py` | 1D controls and the Cherenkov bound | `s2_control1d.out` |
| — | dispersion identity check | `s2_identity.out` |
