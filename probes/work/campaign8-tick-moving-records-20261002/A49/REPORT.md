All runs are complete; the λ′ = 0.1 and 8³ reference results confirm the picture. The final message below is the report. I did not write REPORT.md, per my harness rules.

# A49 report: is the projected parton background a steady state of a local covariant rule?

All scripts and outputs are in `SP/c8/A49/`, where SP is `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad`. There were no repo edits, no git writes and no PRs. Every rule here is a supplied exploration, not adopted. S2 terms (body diagonals, plaquettes) reach beyond one star and need decision 22.

## 1. Verdict
- **No near-null rule was found in the tested spaces** (CHECKED).
  - The parton's lowest relative variance is 0.0026 ± 0.0002 (S1, 18 operators) and 0.0025 ± 0.0002 (S1∪S2, 23 operators) at both 6³ and 8³.
  - It does not shrink with size: the 6³ → 8³ ratio is 0.96 ± 0.11.
  - The much smaller 16-site values (1.7e-4, or exactly 0 in S1∪S2) are cluster artifacts.
- **The parton is only mildly closer to a steady state than the weakly ordered states** (CHECKED). It is 1.5–2× below projected Néel (m = 0.05) and collinear (m = 0.1) states, which are small deformations of it.
  - The best rule is the same at every size: the Klein dual of a strongly frustrated SU(2)-invariant J1–J2–J3 Heisenberg rule (J2/J1 ≈ 0.75, J3/J1 ≈ 0.37), plus four-spin star terms.
  - λ′ = 0.1 changes nothing within error.
- **Forward test, 16 sites exact (CHECKED).** Under that rule the parton sits 0.09–0.12 per site above the exact ground state, with overlap 0.0002 with it. It is close to an eigenstate deep in the spectrum, not the calmest state.
  - Side result (EXACT): the compass-staggered product state is an exact zero-energy eigenstate of the covariant nearest-neighbour rule J = K, on any lattice. Being an eigenstate of a covariant rule is therefore cheap; calmness is what discriminates.

## 2. Question
- Is the projected parton state (λ′ = 0, and λ′ ≈ 0.1–0.2) close to an eigenstate of some rule in a stated space of covariant, Hermitian, time-reversal-even, translation-invariant local rules?
- If so, is it that rule's calmest state?
- Method (COMPARATOR technique: Chertkov–Clark 2018, Qi–Ranard 2019, Greiter et al. 2018): minimise cᵀCc / cᵀGc.
  - C is the per-site covariance matrix of the operators.
  - G is the per-site Hilbert–Schmidt Gram matrix.

## 3. Answers

### 3.1 The basis (EXACT; covariance CHECKED)
Each operator is a group average under the 24 exact soldered turns, normalized to unit per-site HS norm. Every one has covariance defect 0.0, real coefficients and even weight. The named operators span the group averages of all 9 Pauli seeds in each bond class (rank 3/4/3/3).

| Class | Operators | n |
|---|---|---|
| S1, nearest neighbour | J1 = σ·σ, K1 = σᵃσᵃ, D1 = eₐ·(σ×σ) | 3 |
| S1, face diagonal | J2, Kn2 = σᶜσᶜ (c the face normal), Kd2 = (σ·d̂)², D2 = d̂·(σ×σ) | 4 |
| S1, axis-2 | J3, K3, D3 | 3 |
| S1, four-spin star terms | Klein duals of SU(2)-invariant (σ·σ)(σ·σ) on star four-sets: T-shape 2, corner 1, diamond 2, Y-shape 3 | 8 |
| **S1 total** | | **18** |
| S2, body diagonal | J4, Kd4, D4 | 3 |
| S2, plaquette four-spin | Klein-dual pairings; A46's ring term is one combination | 2 |
| **S1∪S2 total** | | **23** |

- The full covariant weight-4 space is 129 operators on star supports and 15 on the plaquette. Only the SU(2)-dual subset above was used.
- The four-spin terms are verified Klein duals of SU(2)-invariant operators: gavg(Klein seed) = Klein(position average) to 0.0. This confirms A44 (iii) for these terms.

### 3.2 Lowest relative variances for the parton, λ′ = 0

Lowest eigenvalue, with the next two after the semicolon. 6³ and 8³ are VMC with 16-block jackknife errors.

| Set | 16 sites, exact | 6³ (16,659 samples) | 8³ (3,134 samples) |
|---|---|---|---|
| NN (3) | 0.304 | 0.192(13) | 0.222(43) |
| S1 bilinears (10) | 0.0292 | 0.0399(11) | 0.0402(69) |
| **S1 (18)** | **1.7e-4**; 0.023, 0.058 | **0.00257(21)**; 0.046(3), 0.079(2) | **0.00247(20)**; 0.035(1), 0.083(7) |
| **S1∪S2 (23)** | **0** (twisted Casimir, artifact); 6.3e-4 once it is removed | **0.00248(20)**; 0.039(2), 0.063(2) | **0.00231(15)**; 0.031(2), 0.067(5) |

- Jackknife bias corrections are 1–3%.
- **The minimizing vector is the same at all three sizes** (normalized to the largest component):
  - dual J2: 1.00
  - dual J1: 0.94
  - J3: 0.33
  - C0 (corner four-spin): 0.32
  - T0 (T-shape four-spin): 0.28
- Here dual J1 = −J1 + 1.155 K1 and dual J2 = −J2 + 1.155 Kn2. In the dual frame the rule is about 0.21 Σ_NN σ·σ + 0.16 Σ_FD σ·σ + 0.08 Σ_A2 σ·σ plus four-spin star terms.
- Four-spin star terms reduce λ about 15× (0.040 → 0.0026). Adding S2 reduces it only 4–6%.

### 3.3 λ′ and the references (relative variance; CHECKED)

| State | 16 sites, S1 | 16 sites, S1∪S2 without the Casimir | 6³, S1inv / S1∪S2inv | 8³, S1inv / S1∪S2inv |
|---|---|---|---|---|
| parton λ′ = 0 | 1.7e-4 | 6.3e-4 | 0.00257(21) / 0.00248(20) | 0.00247(20) / 0.00231(15) |
| parton λ′ = 0.1 | 3.2e-4 | 8.4e-4 | 0.00234(8) / 0.00229(8) | — |
| parton λ′ = 0.2 | 2.6e-3 | 3.9e-3 | — | — |
| Néel m = 0.05 (projected) | 1.0e-3 | 1.9e-3 | 0.00397(21) / 0.00383(20) | 0.00415(28) / 0.00380(27) |
| Néel m = 0.1 / 0.3 | 3.4e-3 / 0.017 | 4.5e-3 / 6.6e-3 | — | — |
| collinear m = 0.1 | 2.6e-3 | 5.0e-3 | 0.00503(20) / 0.00491(21) | — |
| collinear m = 0.4 | 0.025 | 0.012 | — | — |
| compass-staggered product | 0 (exact) | 0 | 0 (VMC 1e-12) | — |

- "inv" means the dual-SU(2)-invariant subspace. The parton's minimum lies exactly in it at all sizes; at 16 sites the λ′ = 0.1 minimum lies in it to within 4%.
- At 16 sites, the order axis (dual z or 111) leaves the lowest value unchanged.
- Going from 16 sites to 6³, the parton's λ grows 15×, Néel's 4× and collinear's 2×. So the 16-site cluster flatters the parton most.

### 3.4 Controls (all pass)

| Control | Result |
|---|---|
| Exact ground state of soldered Heisenberg J1, 16 sites (E0 −1.298194 per bond, as A44) | Null vector J1 at −2.1e-13. S1 also has 2 extra null directions: cluster identities. |
| Exact ground state of the Klein-dual Heisenberg rule | Null vector dual J1 at 2.5e-13 |
| Polarized product state, n = (1,2,3)/√14 (soldered frame) | Null J1 (and D1, which is EXACT: uniform DM is a total derivative): 0 at 16 sites; −2e-12 by VMC at 6³ |
| Compass-staggered product | Null J1 + 0.577 K1, i.e. J = K: −1e-16 at 16 sites; −2e-15 by VMC at 6³. Proof by hand: pair flips vanish per bond and single flips cancel per site. |
| Estimators against exact, 16 sites | Full mode 1e-12. Wigner–Eckart split 1.9e-13; code against masked split 1.3e-12; generic singlet 2e-14. |
| VMC against A44 | ⟨J1⟩ = 0.3366 (6³) and 0.3353 (8³), against 0.3379(13) and 0.3361(9) |

### 3.5 Forward test (16 sites exact, dual S^z = 0 sector, rules normalized; CHECKED)

| Rule from | E₀/N | Parton ⟨H⟩/N (variance/N) | Overlap with ground space | Néel 0.05 / collinear 0.1 ⟨H⟩/N |
|---|---|---|---|---|
| 16-site minimizer | −0.4192 (3-fold) | −0.3772 (2.9e-4) | 0.0000 | −0.3766 / −0.3759 |
| 6³ minimizer | −0.4941 | −0.3706 (1.5e-3) | 0.0002 | −0.3700 / −0.3693 |
| 8³ minimizer | −0.4607 | −0.3711 (2.6e-3) | 0.0002 | −0.3704 / −0.3698 |

- With the opposite sign, E₀/N ≈ −2.65 while the parton sits at +0.37.
- At 6³ under the 6³ rule (VMC), the parton is the lowest of the three trial states: −0.36074(3), against −0.36047(7) for Néel and −0.35985(5) for collinear.
- Spin-wave-corrected competitors were not computed (the rule has four-spin terms).

## 4. Methods
- **Frames.** Operators are built in the soldered frame. The state is the projected π-flux singlet in the Klein-dual frame (A44). Operators map by σᵇₓ → Rₓ(b)σᵇₓ.
- **16 sites (exact).** C comes from exact vectors hᵢψ on the 2¹⁶ space, applied string by string with no dense matrices. Lanczos runs on a LinearOperator.
- **6³ and 8³ (VMC).** The A44/A46 move set; Gᵢⱼ entries only for displacements up to 2; four-site determinant ratios.
- **Key subtlety (EXACT).** The λ′ = 0 state is zero outside S^z = 0, so the naive estimator ⟨Eᵢ*Eⱼ⟩ silently drops every S^z-changing operator part. I used the Wigner–Eckart split instead:
  - C = Cov(rank 0) + Σ_c⟨O1_c O1_c⟩ + (3/2)Σ_m⟨O2_m O2_m⟩;
  - only S^z-conserving q = 0 operators enter: σ·σ, (σ×σ)_z and T_zz.
- **λ′ = 0.1.** The odd-sector weight is about 1e-4, so S^z-changing estimators are unusable. I used the invariant subspace, sampled in S^z = 0; the bias is O(1e-4).
- **Errors.** Jackknife over 16 blocks.

## 5. Checks
- **Runtime and peak memory per run:**

| Run | Runtime | Peak memory |
|---|---|---|
| basis_check | 0.6 s | 36 MB |
| ed16 | 55 s | 140 MB |
| val16 | 106 s | 128 MB |
| val16b | 42 s | 570 MB |
| VMC 6³ batches (5) | 270 s each | 167–174 MB |
| pol / cs controls | 8 / 14 s | 88 / 87 MB |
| VMC 8³ batches (2) | 270 s each | 212–223 MB |
| fwd16 | 194 s | 331 MB |
| anal49 (final) | 26 s | 302 MB |

- Load was 1.4–3.2 and free memory 30–41%. Every job went through run.sh, one at a time.
- **Flagged runs:**
  - The first anal49 run and val16 part (b) put D1–D4 into the invariant subspace through a name-prefix bug. Their reference numbers were invalid; the bug is fixed and those runs are superseded.
  - val16b's "lowest lam S1" line used a wrong slice and should be ignored.
  - A stray `cat >` in a shell line blocked on stdin. No job ran, but it created an empty `/tmp/dummy_never_used`, which I deleted.
- **16-site cluster defects:**
  - the Gram matrix has rank 17 of 23 (D2–D4 vanish by aliasing);
  - the π-flux state is zero on 4128 of the 12870 S^z = 0 configurations;
  - none of 300 random configurations is singular at 6³, nor 120 at 8³.

## 6. Open edges
1. The full 129-operator covariant weight-4 star space and weight-6 star terms. These need a rank ≤ 4 Wigner–Eckart split. The S1 → S1∪S2 trend says multi-spin structure matters more than range.
2. Longer range (decision 22). COMPARATOR: in 1D, the Gutzwiller-projected Fermi sea's parent rule (Haldane–Shastry) is 1/r² long-range.
3. λ′ ≠ 0 in the full operator space via sector-resolved chains; the bridge estimators are already recorded.
4. Corrected ordered competitors (Lanczos-step or spin waves) under the minimizing rule at 6³ and 8³.
5. A 16-site cluster without structural zeros (twisted boundaries).

## 7. Plain-language summary
We asked the question backwards. Instead of guessing a rule and checking whether the two-part background is its calmest state, we started from the background. We then searched all the simple rules that the grid's turns allow for one under which it would barely change at all. On a tiny 16-place grid such a rule seemed to exist, but that was a quirk of the tiny grid. On grids of 216 and 512 places, the best rule always leaves a small, definite restlessness that does not shrink as the grid grows. Slightly magnet-like states are only a little more restless under their own best rules. Under the best rule, the background also sits well above the rule's true calmest state on the small grid. So, among the rules tested, the background is not a calmest state.