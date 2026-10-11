# Lane RW, probe W1 (cancellation by dressing): report

Worker: Claude Opus 5.5 (same family as the supervisor). Run 16:53Z to about 17:45Z, 2026-10-11. No repository files were edited. Scratch folder: `.../scratchpad/C4/W1/` (scripts `w1_*.py`, outputs `w1_*.out`, quadric data `w1_quadric_*.npz`). Not refereed.

## Reading against the FIXED line

**W1: FAIL (bounded), pending a codex referee.**

- Within the stated ansatz, cancellation exists but needs one tuned parameter per channel.
  - The ansatz: local O(λ) dressings, linear in h, quartic or quadratic in the fields, range ≤ r, cubic-covariant, on the RN L2 design.
  - μ_E = μ_T2 = 0 at O(λ²) is achievable: E from range 1, T2 only from range 2.
  - The solution set is a codimension-one sphere in each channel.
  - Nothing in the matter law picks a point on it. The two principled points tested both miss it, one of them by a factor of 23.
- A second interaction adds its own conditions.
  - Nearest-neighbour φ²φ² already gives μ_E at O(λ′), and the onsite solution does not cancel its O(λ′²) term.
  - So each interaction adds one more tuning per channel.
- **The one cancelling dressing with no free parameter lies outside the ansatz and is a tuning by construction.**
  - It is the dressing that reproduces the non-local full flow's vacuum integrand. It is exponentially local and needs terms in h².
  - It is built from the vacuum energy integrand itself: the energy denominators at a shifted total momentum.
- **Not computed:** the vacuum-annihilating dressed momentum (a P₄ principle). It is the one principled candidate left open. See §4.

## 1. Setting and the exact reduction (PROVED, short)

**Coupling.** H(h) = U_h H₂ U_h† + λ:H₄:₀ + λε Σ_a c_a :O_a:₀ + (quadratic dressings).

- U_h is the RN L2 free unitary strain flow, f = sin k, with φ transported as a density.
- H₄ = (1/24)Σφ_x⁴ is normal-ordered with respect to the **unstrained** free vacuum. This is the L2 tadpole-subtracted design.
- O_a are local quartic operators with vertex b_a(k₁..k₄) on K = Σk = 0.
- The O_a have ℓ1-diameter ≤ r and are projected onto the channel's cubic pattern. The channels are E, with h = ε·diag(1,−1,0), and T2, with h_xy = h_yx = ε.

**O(λ) vanishes.** ⟨φ_x²⟩ is invariant under the flow, so ⟨:H₄:₀⟩_ε = 3(G_ε − G₀)² = 0. A normal-ordered dressing has ⟨ε:O:₀⟩_ε = ε·O(ε²), so it adds nothing to the Hessian. Quadratic dressings enter μ linearly at O(λ). At O(λ²) they add only a term that is negative-semidefinite or zero, so they do not affect feasibility.

**O(λ²), exact.** Only the dressed basketball survives:

μ₂(c) = −(1/24)·[A + 4 c·L + 2 cᵀQc]

with:
- A = ∂²_ε ∫_{K=0} w_ε, where w_ε(k) = ∫dt Π_i J(k_i)e^{−tΩ(k_i)}/(2Ω(k_i)) and Ω = ω∘Φ_ε;
- L_a = ∂_ε ∫ b_a w_ε, using the exact ġ;
- Q_ab = ∫ b_a b_b w₀, which is positive semidefinite.

μ is **quadratic** in c, not linear. But |L| ≫ |A|, so the linear term dominates (see §2).

**The solution set.** In Q-orthonormal coordinates y it is the sphere |y + L̃|² = ℓ − A/2, with ℓ = LᵀQ⁺L. It is non-empty iff A ≤ 2ℓ, and it has dimension N_eff − 1.

**Numerics.**
- Everything is in position space by FFT, which is exactly the lattice momentum sum on an L³ torus.
- The t-integral uses 24-node Gauss–Laguerre; its 1/s error is ≤ 8e-15 on s ∈ [3.9, 16].
- **Controls:**
  - A reproduces L2: μ_E = −1.00931e-6·λ² and μ_T2 = +1.61082e-8·λ² at m = 1.
  - The exact ġ matches finite differences to ≤ 2e-8 relative in both channels (`w1_test1.out`).

## 2. Can μ_E = μ_T2 = 0 be achieved, and how big is the solution space? (CHECKED, L-converged)

Values at m = 1 and L = 24, in units of λ² per cell (`w1_mu2_m1.out`). L = 20 and L = 24 agree to ≤ 1e-6 relative.

| Channel | r | N_eff | A | μ₂(c = 0) | ℓ = LᵀQ⁺L | max_c μ₂ | Feasible | min ‖y‖ / ‖V‖_w |
|---|---|---|---|---|---|---|---|---|
| E | 1 | 2 | 2.42235e-5 | −1.0093e-6 | 6.9406e-4 | +5.68e-5 | yes | 2.31e-4 / 1.287e-2 (1.8%) |
| E | 2 | 21 | 2.42235e-5 | −1.0093e-6 | 7.0285e-4 | +5.76e-5 | yes | 2.29e-4 (1.8%) |
| T2 | 1 | 0 | −3.86596e-7 | +1.6108e-8 | — | — | **no dressing exists** | — |
| T2 | 2 | 9 | −3.86596e-7 | +1.6108e-8 | 2.9119e-5 | +2.44e-6 | yes | 1.79e-5 (0.14%) |

**(a) Achievability.**
- Yes, for r ≥ 2 in both channels.
- At r = 1, T2 has **no** cubic-covariant dressing. Every ℓ1-diameter-1 quartic operator is even under each axis reflection (PROVED), so μ_T2 = +1.61e-8·λ² cannot be cancelled at range 1.

**(b) Dimension of the solution space.**
- E: 1 at r = 1, and 20 at r = 2.
- T2: 8 at r = 2.
- E and T2 together: 28 at r = 2. The two channels' coefficients are independent irreps.
- The cancelling dressing is tiny, a 1.8% (E) or 0.14% (T2) change of the vertex. A generic small dressing in this class shifts μ by up to about 5e-5·λ², fifty times the quantity being cancelled.

**Second mass, m = 0.3** (`w1_mu2_m0.3.out`, L = 16, 24, 32):
- E: A = 7.350e-5 at L = 32, a 0.3% change from L = 24. μ(0) = −3.06e-6. ℓ = 1.2644e-3. Feasible.
- T2: A = −1.663e-6 at L = 32, still drifting by 3% between L = 24 and 32. μ(0) = +6.9e-8. Feasible.
- **Converged at the level used:** ℓ, to 5 digits. Feasibility is robust because |A| ≪ 2ℓ.

## 3. Is there a distinguished solution? (c)

### 3a. "Unitary flow of the full H" with the free K: quantifying the failure (PROVED identity; CHECKED by Monte Carlo)

With density transport, the full flow e^{−iK}(λH₄)e^{iK} has lab vertex δ(Σ_iΦ_ε(k_i)) in place of δ(Σk).

- So E2_full(ε) = −(1/24)∫δ(ΣΦ_ε)w_ε = const, by change of variables.
- At first order the deviation from translation is the explicit-position operator (λ/6)εĥ_ij Σ_y y_j φ_y³ D_iφ(y). Its total Σ_y φ_y³D_iφ ∝ [P,H₄] is nonzero, so the operator is not translation-invariant and is undefined on a torus.

**Its local part depends on a convention.** Where the anomaly density is placed is fixed only modulo divergences ∇_l B_il, and that freedom shifts the local part by −ΣB_ij, an arbitrary local tensor operator. That is the whole dressing space. Two natural conventions:

- **Site convention** (anomaly at the interaction site): local part = 0, i.e. c = 0. Then μ₂ = L2's values, which are nonzero.
- **Centroid convention** (symmetric in k): the local vertex is v_loc(κ) = 1/det[¼Σ_iDΦ_ε(k_i*)], with ΣΦ(k*) = 0. This includes its h² part.

Monte Carlo, E channel, m = 1, 1.6e6 samples, common random numbers; the E flow is solved exactly as Φ = 2 atan2(e^{±ε} sin(k/2), cos(k/2)) (`w1_fullflow_mc_m1.out`):

| Coupling | H = ∂²_ε(vacuum integral) | μ₂/λ² |
|---|---|---|
| L2 design (control; exact 2.4224e-5) | 2.354e-5 ± 0.11e-5 | −0.98e-6 |
| full flow, ∫w(k*)v_loc (isospectral control) | (−0.27 ± 0.68)e-6, consistent with 0 | ≈ 0 |
| local part, centroid convention, ∫v_loc²w | **−5.604e-4 ± 0.004e-4** | **+2.335e-5** |

So the local part of the full free flow is not a cancelling dressing. With the centroid convention it is 23 times larger than the L2 response, and of the opposite sign.

**The explicit-position (anomaly) terms that a local coupling must drop carry +5.6e-4 per cell in the vacuum Hessian.** That is about 23 times the whole L2 response, not a small correction. This quantifies the brief's note: the full flow is "not the translation of the interaction term".

### 3b. The exact cancelling local dressing exists, but it is a tuning (PROVED; reading)

The pointwise vertex v_R(κ)² = w_ε(k*)v_loc(κ)/w_ε(κ) reproduces the full flow's vacuum integrand exactly, so μ₂ = 0.

- It is analytic for m > 0, so it is exponentially local.
- It is fixed by H₂, H₄ and P, with no free number.
- It needs terms in h², so it is outside the "linear in h" ansatz.
- It is built from w, the vacuum energy integrand: the energy denominators evaluated at the total momentum K* shifted by the strain. So it is the cancellation condition imposed point by point, a function's worth of renormalization condition that refers to the vacuum state.
- READING: this is a tuning, not a law fixed independently of μ.
- It does not carry over to other states, or to the next order, where the integrand changes.

### 3c. "Minimal O(κ) algebra defect" (ARGUED)

By the refereed C3 lemma, every h-linear dressing vanishes at h = Gᵀξ for Killing ξ. So the Killing-sector (Poincaré) defect does not depend on the dressing, and it cannot select one. The affine-strain sector was not computed.

### Answer to (c)

Within the ansatz:
- no principle tested fixes the point;
- the two flow-derived principled points (c = 0 in the site convention, and v_loc in the centroid convention) both miss the sphere;
- the only exact solution with no free number (v_R) is outside the ansatz and is defined by the cancellation itself.

So cancellation is a free tuning: one parameter per channel, about 2 at O(λ²).

## 4. Next order and a second interaction (d)

### Nearest-neighbour (λ′/4)Σφ_x²φ_{x+μ}² (CHECKED; L = 16, r = 2, m = 1; `w1_bond_m1_L16.out`)

- **O(λ′), new:** ⟨:φ_x²φ_y²:₀⟩_ε = 2(ΔG_xy)². That gives μ_E = λ′Σ_μĠ(e_μ)² = **+1.964e-2·λ′ per cell**, with Ġ(e_x) = +0.0991. In T2 it is 0 by parity.
  - Cancelling it needs a quadratic dressing with a tuned coefficient.
  - Re-normal-ordering in the strained vacuum without its h² c-number overshoots, to −λ′ΣĠ².
- **O(λ′²):** μ_E = −1.879e-4·λ′² and μ_T2 = +8.28e-6·λ′² undressed.
  - The onsite minimum-norm dressing, applied with the same operators and coefficients, leaves −1.847e-4 and +8.27e-6. It is not cancelled.
  - The cosines between L_onsite and L_bond are 0.634 (E) and 0.211 (T2), so the conditions are independent.
  - With both interactions present, the joint solution set has dimension 19 (E) and 7 (T2), one less in each channel.
- **L-convergence:** only L = 16 was run. Onsite numbers at L = 16 agree with L = 24 to 4e-5 relative.

### O(λ³) (NOT COMPUTED; ARGUED)

- At O(λ³) the vacuum ring of three bubbles gives a new number per channel. Its dressing dependence, through the O(λ) coefficients c, is not the O(λ²) condition.
- So each order needs an O(λ^{n−1}) retuning unless a principle forces it.
- The candidate principle is the P₄ principle below.

### The P₄ principle: the one principled route left open (ARGUED)

Choose the O(λ) momentum correction so that the dressed momentum annihilates the interacting vacuum. That gives P₄'s 0→4 kernel as VΣf/Σω, which is analytic because Σω ≥ 4m. Then take the local part of the flow it generates, which includes O(λ²) couplings.

- In the 0↔4 sector its anomaly has zero total, so it is local and unambiguous there.
- ARGUED, signs not verified: its first-order lab vertex is local, d₁^{P4}(κ) = −¼Σ_i div v(k_i) + (¼Σ_i∇ω(k_i))·Σ_j v(k_j)/Σ_j ω(k_j), with v = ĥ sin k.
  - The first term is the centroid local part.
  - The second is the off-shell energy-denominator correction.
  - A full test also needs its h² and λ² parts. That is the hand-off for a follow-up probe.
- Whether its vacuum μ₂ vanishes was not computed.
- At O(λ³) the 2↔2 sector enters. There P₄ = VΣf/(ω₁+ω₂−ω₃−ω₄) is singular on the resonance shell (principal value), so it has power-law, non-local tails. This is the RN L2 obstruction again.
- Expected: at best a principled O(λ²) cancellation whose continuation needs non-local dressing.

## Against the supervisor's expectation

The expectation was "one tuned parameter per channel, so FAIL".

- **Confirmed:** codimension 1 per channel, and no selection by the principles tested.
- **Not foreseen:**
  - T2 cannot be dressed at range 1.
  - The cancelling dressing is tiny (≤ 2% of the vertex) while generic dressings move μ fifty times further. The cancellation is easy to achieve and entirely unprotected.
  - The local part of the full flow misses by a factor of 23.
  - The φ²φ² interaction gives μ already at O(λ′).

## Labels

- **PROVED (same family):**
  - the O(λ²) reduction and the sphere structure;
  - O(λ) vanishing for normal-ordered dressings;
  - no range-1 T2 dressing;
  - the full-flow identity E2_full = −(1/24)∫δ(ΣΦ)w = const;
  - the local-part ambiguity;
  - the existence of v_R.
- **CHECKED:** every table. L-convergence is explicit for onsite (L = 12 to 24 at m = 1; 16 to 32 at m = 0.3, where T2 still drifts by 3%). The bond results are L = 16 only. The full-flow values are Monte Carlo with the stated errors.
- **ARGUED:** the P₄ principle, O(λ³), and the Killing-blindness of the algebra-defect principle.
- **READING:** v_R is a tuning.
- **Not done:** O(λ³) numerics, the P₄ construction, T2 for the full-flow test, and the half-density (referee K_h) convention.

## Files

All in `.../scratchpad/C4/W1/`:
- `w1_core.py`
- `w1_test0.py` / `.out`
- `w1_mu2.py` with `w1_mu2_m1.out`, `w1_mu2_m0.3.out`, `w1_mu2_quick.out`
- `w1_bond.py` / `w1_bond_m1_L16.out`
- `w1_fullflow_mc.py` / `w1_fullflow_mc_m1.out`
- `w1_quadric_*.npz`
