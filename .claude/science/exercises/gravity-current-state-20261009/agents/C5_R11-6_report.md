# C5 R11-6 report: assembled Sokolov three-body box law with subtracted channel tails (d = 1)

**Author and provenance.** Claude Opus 5.5 probe, same model family as the supervisor and as the R7-6, R8-1 and R9-3 workers. Unrefereed. Ran 2026-10-12 18:36Z–19:06Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R11-6/`; scripts and outputs in `S/scripts/`:
- `PREREG_c.txt`: the (c) analysis, written at about 18:47Z, before any (c) run.
- `r116_core.py`: the dense assembly in the free-chart (FC) prescription: B_a, B_b, B_c, the S3 packing, M_BT, H_BT, H_S, H_a.
- `r116_check.py` with `r116_check_L{96,160,240,320}_a.out`: (a), (d) and the S3 tails.
- `r116_s4.py` with `r116_s4_L*_K*.out`: the S4 packing (ordered product); (a), (d), and the registered (c) on the assembled operators.
- `r116_algebra.py` with `r116_algebra_L{96,128,160}{,_K8}.out`: (b).
- `r116_smin.{py,out}`, `r116_s2check.{py,out}`, `r116_nullvec.py` with `r116_nullvec_L*_P0.4.out`: invertibility of the packing's A, and where its near-null vector sits.
- `r116_tails.py` with `r116_tails_*.out`: large-r subtracted-tail components, matrix-free, using R9-3's exact reduction.
- `r116_fit.{py,out}` and `r116_fit2.{py,out}`: the pre-registered AICc comparison.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:2302-2320` (C5 method), `:4064-4263` (round 11, R11-6 at `:4247-4263`); `agents/C5_R9-3_report.md`; `C5_R9-3_referee_verdict.md`; `C5_R7-6_report.md`; `C5_R8-1_referee_verdict.md`; `SUMMARY.md` §§21–24 (`:534-635`).
- In part: `C5_R7-6_referee_verdict.md:60-176`; `C5_S11_synthesis.md` (grep hits plus `:315-349`, `:514-530`); `TESTS.md:3496-3512, 3785-3800, 3895-3910`.
- Scripts: `scripts/C5/R9-3/r93_packing_cluster.py` and `scripts/C5/R7-6/r76_threebody_naive.py:1-80`.

**Prior-art grep** (`docs/`, `.claude/science/`; "Sokolov", "packing operator", "packing unitar"). Each counts once:
- R7-6 and its referee;
- R9-3 and its referee;
- R7-1 (`C5_R7-1_report.md:57,165`, RECALLED mentions);
- R8-4 (`C5_R8-4_report.md:95`; `C5_R8-4_referee_verdict.md:79`; Keister–Polyzou BT failure plus Sokolov restoration, as cited there);
- R9-10 (`C5_R9-10_report.md:100`; Lev's packed EM current, an abstract cite);
- S8, S11, TESTS.

No hit in `docs/`. Nothing found assembles the packed three-body operators.

**Labels.**
- **proved:** argued here in full.
- **checked:** numerics run here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** someone else's number, used for comparison.
- **RECALLED:** literature taken from memory, not verified.

**Subtractions, named before any run** (new rule `TESTS.md:4074`; `PREREG_c.txt`):
- T_B(r) = ‖(B − B_a)ψ_r‖/‖ψ_r‖. The subtracted limit is the channel-a packing limit B_a.
- T_H(r) = ‖(H_S − H_a⊗1 − 1⊗h₃)ψ_r‖/‖ψ_r‖. The subtracted limit is the channel-a generator: the pair-12 BT law plus a free spectator.
- The un-subtracted U_B = ‖(B − 1)ψ‖ and U_H = ‖(H_S − H_BT)ψ‖ are reported only as contrasts.

**Convention.** The registration writes H_S = B H_BT B† (`TESTS.md:4256`). This report uses R9-3's convention, H_S = B† H_BT B with B → B_a in channel a (`C5_R9-3_report.md:142`). It is the same object with B ↔ B†.

---

## 0. In plain words

1. **The packed three-body law is now built as explicit matrices (checked; d = 1; one stated prescription).**
   - B, H_S = B†H_BT B and K_S were assembled on grids of five sizes (L = 96–320), for two packings.
     - **S3:** the polar part of 1 + Σ_c(B_c − 1).
     - **S4:** an ordered product of polar steps in the pair coupling. This is a discretized version of R7-6's Construction S.
   - B is orthogonal to 1e-14.
   - S4 converges in its step number: T_B agrees to 5 digits for K = 8, 16 and 32.
2. **The algebra and the trimer mass hold by construction in this prescription (proved; checked).**
   - The trimer's invariant mass is identical at P = 0, ±0.2 and ±0.4 to ≤ 5e-14.
   - As the grid refines it converges to R7-6's ring trimer: 0.734926, 0.734349 and 0.734289 at L = 160, 240 and 320, against 0.734266 (R7-6, ring L = 300).
   - The algebra residuals on P-packets fall with L: 4.1e-3, 7.4e-6 and 7.6e-7 (S3). For S4 they are not monotone.
3. **The registered tail test cannot be decided on the assembled matrices (checked).**
   - On grids of up to 3136 states, the chart changes alias once the spectator is farther than about L/6. The subtracted tails can be followed only to r ≈ 48.
   - Inside that window, the dimer and spectator are not yet separated for r ≲ 24. T_B then falls from 0.18 to 0.012 between r = 24 and 68 (P = 0.4, L = 320).
   - The registered full-range comparison is "undecided" for T_B and "power" for T_H. That is not evidence for a power law: the series is non-monotone and resolution-limited.
4. **At large separation, every computed ingredient of the subtracted tail falls faster than any tested power (checked; finite window).** This is the result that carries the physics.
   - Matrix-free exact reductions extend the range to r = 20–640, 1.5 decades. The components are:
     - ‖(B_b − 1)ψ_r‖: 0.14 → 2.0e-7;
     - ‖(B_b† − 1)B_aψ_r‖: 0.14 → 2.8e-7;
     - ‖D_b B_aψ_r‖, the generator part: 0.054 → 4.2e-8.
   - Each beats a power law by the same pre-registered AICc: +27 to +31 over the full range, and +3.7 to +19 on the operator range r ≥ 80.
   - The local log-slopes rise from about 1 to about 6–7.
   - The proved Lemma P bounds S3's subtracted tail by the first two components, and Lemma G bounds T_H with the third as its leading part.
   - These are **bound ingredients**, not the registered observable. The bound's constant is not controlled (§4.5).
5. **A trap found and defused (checked; suggested reading).**
   - On every dense grid, the packing's A = 1 + Σ(B_c − 1) (and R9-3's S2 mean) loses invertibility as L grows: s_min = 0.39, 0.16 and 4e-5 at P = 0.4 for L = 128, 160 and 240.
   - The near-null vector is a dimer with the spectator at the ring's antipode: 99.7% of its weight lies at |x₃| > L/4. That is exactly where spline chart changes alias.
   - So this is a discretization artefact, not evidence that the continuum packing is singular.
   - It does mean that no dense-grid s_min can stand in for the continuum constant in Lemma P.
6. **Reading: INCONCLUSIVE.** PASS fails on (c). FAIL is not supported: nothing found decays like a power.

---

## 1. Hypotheses and class (stated before titles)

- **Inherited unchanged.** H-lat, H-box, H-P (P = Q, an added bridge, `C5_R7-6_referee_verdict.md:85-91`) and H-L3 (the box sector equals the continuum fibre; conditional, `:71-79`).
- **Pair law.** R7-6/R8-1's d = 1 fermion pair law:
  - M_pair = M₀(q) + λ|g⟩⟨g|, with g(q) = (q/κ)·sstep(1 − q²/κ²), which is odd and C^∞ with support in |q| < κ;
  - m = 0.3, κ = 0.25, λ = −3;
  - the dimer μ_b → 0.5152799 (continuum 0.51527993; R7-6: 0.5152799267).
  - R8-1's own parameter set (m = 0.5, κ = 0.4) was not run.
  - The plateau is c(P_ij) = 1, as R7-6's plateau covers the region used.
  - Normalization: the pair kernel is the restriction of W to the antisymmetric pair sector, the ½-lift (`TESTS.md:3796-3798`).
- **Prescription for P ≠ 0 rings (stated; the registration's requirement, `vR9-3:110`).**
  - *FC (free-chart) prescription.* The P-fibre of a ring of size L is the free boost Λ_P of the P = 0 rest-frame fibre, so every fibre uses the same internal grid.
  - The internal plane uses channel a's Jacobi chart (p₃, q₁₂), on a uniform cell-centred grid of spacing h = 2π/L over |p₃|, |q₁₂| < 0.55. States are half-densities.
  - Channel c's operators act on its own Jacobi chart (s, q > 0, odd sector, |q| < κ + 4h). Chart changes are 2D cubic-spline interpolation with exact half-density Jacobians.
  - An edge taper W = Π_i sstep((0.48 − |p_i|)/0.10) multiplies B_c − 1 on both sides, to remove grid-edge loss.
  - **What it is not.** This is a chart quadrature with ring spacing. It is not the lattice ring's own lab grid at P ≠ 0 (which, by `vR9-3:§5`, the continuum chart cannot preserve), and K is not built from site positions.
- **Packing unitaries in FC.** B_c^FC = R_M R₀† is the lab-chart B_c = R₀†R_M (`C5_R9-3_report.md:148-153`) conjugated by Λ_P, since Λ_P = R₀† in each channel's coordinates (proved, two lines). At P = 0, B_c = 1.
- **Packings.** Each is unitary, commutes with P and is symmetric in the three channels:
  - (S3) B = polar(A), A = 1 + Σ_c(B_c − 1);
  - (S4) B = U_K⋯U_1, with U_k = polar(1 + Σ_c[B_c(s_k)B_c(s_{k−1})† − 1]), s_k = k/K, where B_c(s) is built with coupling sλ;
  - (S2) is R9-3's symmetric mean (`C5_R9-3_report.md:140`); only its invertibility was checked.
- **BT and the packed law.**
  - M_BT = M₀ + Σ_c(M_(c) − M₀), with M_(c) − M₀ = √(M_pair² + s²) − √(M₀pair² + s²) at fixed spectator s.
  - H_BT(P) = √(M_BT² + P²); H_S = B†H_BT B; H_a = B_a†√(M_(a)² + P²)B_a.
  - K_S = ½{H_S, B†X₀B}, with X₀ = i∂_P across fibres.
- **Particles.** Labels 1, 2, 3 are distinguishable on the grid. The law acts only on odd pair sectors. The fermionic sector is the antisymmetric restriction, and the distinguishable cluster residual bounds the fermionic one: ‖A(H_S − H_a)ψ‖ ≤ ‖(H_S − H_a)ψ‖, because H_S commutes with permutations and the antisymmetrizer is a projector (proved, one line; permutation symmetry holds on the grid only to interpolation accuracy).
- **Test states (channel a = (12)(3)).** ψ_r = χ_b(q₁₂) ⊗ G(p₃)e^{−ip₃r}: the bound dimer, with a spectator Gaussian (σ = 0.08) whose rest-frame centre is −0.10. P = 0.4 is primary, P = 0.2 secondary, and P = 0 is the control.
  - The large-r runs use the same state in the lab a-chart: lab centre k₃ = 0.040 (the boost image of −0.10), width 0.08. This exact product state of H_a is a declared deviation from `PREREG_c.txt`, which fixed the state in master coordinates.
- **Excluded realizations (not addressed):**
  - d ≥ 2; N ≥ 4 (the tower);
  - pair creation; gravity;
  - the ⊗M₂ ungraded composition;
  - a site-position (lattice-native) K;
  - the lab-ring grid at P ≠ 0;
  - R8-1's parameter set;
  - boosted regimes P ≳ M.

## 2. Prior art (each counted once)

- **R7-6** (`TESTS.md:3506-3510`).
  - Proposition BT0: M_BT = H_pair(0).
  - Construction S, the ordered exponential, which S4 discretizes.
  - Theorem N, the pair-sum drift.
  - The T-risk.
- **R7-6 referee.** B_a = 1 at P = 0; B_a is long-range in the spectator; the full Sokolov claim is open (`C5_R7-6_referee_verdict.md:101-137`).
- **R9-3 and its referee** (`TESTS.md:3902-3907`):
  - the support reduction B_b − 1 = Q_G(B_b − 1)Q_G, which is reused here;
  - the component tails track the Fourier proxies;
  - the registration defect: B → B_a ≠ I and H_S − H_BT → H_a − B_aH_aB_a† ≠ 0 (`vR9-3:3,26,43,110`).
  - **The subtractions used here are exactly the referee's repair** (`vR9-3:§6 "Registration issue 1"`).
- **R8-1 referee:** the support identity f(M) − f(M₀) = Q_G[·]Q_G (`C5_R8-1_referee_verdict.md` item 5).
- **Literature:** Keister–Polyzou and Coester–Polyzou, as cited in R9-3 (strong cluster limits, with no rate given); Sokolov (RECALLED).

---

## 3. Three proved lemmas (exact, finite-dimensional, or with domains as stated)

**Lemma P (polar packing bound) — proved.**
- **Setting.** Let A = B_a + E, with B_a unitary, A invertible, s = s_min(A) > 0, and B = A(A†A)^{−1/2}. Write T = A†A.
- **Claim.** For every ψ,

  ‖(B − B_a)ψ‖ ≤ ‖Eψ‖ + (1 + ‖E‖)/(s(1 + s)) · [(1 + ‖E‖)‖Eψ‖ + ‖E†B_aψ‖].

- **Proof.**
  - B − B_a = B_a(T^{−1/2} − 1) + E T^{−1/2}.
  - T^{−1/2} − 1 = f(T)(T − 1), with f(t) = −1/(√t(1 + √t)), so ‖f(T)‖ ≤ 1/(s(1 + s)).
  - T − 1 = B_a†E + E†B_a + E†E, and ‖E T^{−1/2}ψ‖ ≤ ‖Eψ‖ + ‖E‖‖(T^{−1/2} − 1)ψ‖. ∎
- For S3, E = (B_b − 1) + (B_c − 1) and ‖E‖ ≤ 4.
- So the S3 subtracted tail is bounded by e₁ = ‖Eψ‖ and e₂ = ‖E†B_aψ‖, **provided s_min(A) ≥ s₀ > 0 uniformly**. That proviso is not established (§4.5).

**Lemma T (S4 telescoping) — proved, finite-dimensional.**
- **Setting.** Let V_k = B_a(s_k)B_a(s_{k−1})†, so V_k⋯V_1 = B_a(s_k), and B_a(1) = B_a.
- **Identity.**

  B − B_a = Σ_k (U_K⋯U_{k+1})(U_k − V_k)B_a(s_{k−1}).

- **Hence**

  ‖(B − B_a)ψ‖ ≤ Σ_k ‖(U_k − V_k)B_a(s_{k−1})ψ‖,

  and each term is bounded by Lemma P with A_k = V_k + E_k, E_k = Σ_{c=b,c}[B_c(s_k)B_c(s_{k−1})† − 1].
- **Corollary.** S4 clusters (B → B_a strongly) whenever E_k → 0 strongly on the a-cluster states B_a(s)ψ_r, with s_min(A_k) bounded below.
- **Continuum form (K → ∞, generators Ĝ_c(s) = −i∂_sB_c(s)·B_c(s)† on a common invariant domain; Duhamel).**

  B − B_a = i∫₀¹ W(1,s)[Ĝ_b(s) + Ĝ_c(s)]B_a(s) ds, so ‖(B − B_a)ψ‖ ≤ ∫₀¹ ‖(Ĝ_b + Ĝ_c)(s)B_a(s)ψ‖ ds.

  - The algebra is proved. The domain hypothesis is suggested only.
  - This form needs **no invertibility at all**, so S4 is the right object for the tail question (reading).

**Lemma G (generator subtraction) — proved, algebraic.**
- **Setting.** Let Δ = B − B_a and E_H = H_BT − B_aH_aB_a†.
- **Identity.**

  H_S − H_a = B†E_H B + Δ†B_aH_a + H_aB_a†Δ + Δ†B_aH_aB_a†Δ.

- **Bound.**

  T_H ≤ ‖E_H B_aψ‖ + (‖E_H‖ + 3‖H_a‖)T_B + ‖Δ†B_a(H_aψ)‖,

  with H_aψ_r = E_b(k₃)ψ_r exactly for the dimer product state.
- **The E_H term (suggested reduction).** E_H B_aψ is the FC difference √(M_BT² + P²) − √(M_(a)² + P²) acting on an a-cluster eigenstate. By the resolvent integral √a − √b = (2/π)∫t²(a + t²)^{−1}(a − b)(b + t²)^{−1}dt, it is controlled by D = (M_(b) − M₀) + (M_(c) − M₀) acting on a smooth family of a-cluster states. This is a Lemma-Sm-type reduction, labelled suggested. The computed proxy is ‖D B_aψ‖.

---

## 4. Results

### 4.1 (a) Assembly (checked)

| quantity | L = 128 | L = 160 | L = 240 | L = 320 |
|---|---|---|---|---|
| dimension N | 484 | 784 | 1764 | 3136 |
| dimer μ_b (continuum 0.51527993) | 0.514919 | 0.515315 | 0.515264 | 0.515277 |
| ‖BᵀB − 1‖ (S3 and S4) | 2e-14 | ≤ 7e-14 | ≤ 7e-14 | ≤ 5e-14 |
| ‖(B_aᵀB_a − 1)ψ_r‖, r = 3 → 48 (P = 0.4) | — | — | 9e-4 → 2e-2 | 9e-4 → 3e-3 |

- **S4 converges in K** (L = 160, P = 0.4, r = 24): T_B = 0.18112, 0.18111 and 0.18111 for K = 8, 16 and 32 (`r116_s4_L160_K*.out`).
- **S4 versus grid size.** L = 240 (K = 16) and L = 320 (K = 8) give the same T_B on the test states:
  - to within 1.2e-3 relative for r ≤ 34;
  - to within 5% at r = 48.
- **P = 0 control:** B = B_c = 1 exactly; s_min = 1.
- **B_c is not unitary on the whole grid.** ‖B_cᵀB_c − 1‖₂ = 0.5–1.0, from grid-scale and antipodal modes (§4.5). On the test states the defect is small, as tabulated.

### 4.2 (b) Algebra (proved by construction; checked)

- **Proved.** In FC, [H_S, P] = 0 fibre by fibre. If B(P) is unitary in each fibre, then [K_S, P] = iH_S and [K_S, H_S] = B†[X₀, H_BT]B·(sym) = iP, because M_BT does not depend on P in the free chart.
- **What the numerics test.** The residuals measure only the unitarity of B and the P-discretization of ∂_P, with ΔP = 2π/L (`r116_algebra.py`).
- **Packet.** w(P) is Gaussian with centre 0.3 and width 0.06, times an interior state.

| L | S3 [K,P] − iH | S3 [K,H] − iP | S4 (K = 8) [K,H] − iP | BT reference |
|---|---|---|---|---|
| 96 | 4.1e-3 | 5.1e-3 | 5.1e-3 | 5.0e-3 |
| 128 | 7.4e-6 | 9.9e-6 | 9.9e-6 | 9.7e-6 |
| 160 | 7.6e-7 | 6.9e-7 | **1.2e-4** | 4.7e-8 |

- [H, P] = 0 to 1e-16 in every case.
- **S4 at L = 160 is not monotone.** The packet's P-range reaches 0.8. There the near-singular polar steps (§4.5) make B(P) rough in P, which spoils the spectral derivative. (checked; the reading is suggested.)

### 4.3 (d) Trimer invariant mass (proved exact in FC; checked)

- **Proved.** spec H_S(P) = spec √(M_BT² + P²) for any fibrewise-unitary B.
- **Checked.** max|spec H_S − √(spec M_BT² + P²)| ≤ 5.4e-14 at every L, every P and both packings.
- **The lowest state is P₁₂-odd.**

| L | 160 | 240 | 320 | R7-6 ring (comparator) |
|---|---|---|---|---|
| M_trimer at P = 0, ±0.2, ±0.4 (identical) | 0.734926248 | 0.734349499 | 0.734288536 | 0.734266071 (L = 300) |

- The values converge toward R7-6's lattice-exact pair-sum trimer, which BT0 says is M_BT's ground state. This is an independent cross-check of the FC quadrature of M_BT = H_pair(0).
- **The flatness itself is by construction.** It is not a test of the lattice.
- Cyclic (fermionic) symmetry of the lowest state was not checked separately. The match with R7-6's fermion trimer is the evidence (comparator).
- The P values are continuous fibre labels: P₁ = 0.2 and P₂ = 0.4.

### 4.4 (c) Registered measurement on the assembled operators (checked; registered comparison run as fixed)

**S4, P = 0.4, dimer family, r = 3·2^{k/2}** (`r116_s4_L320_K8.out`; L = 240 in `r116_s4_L240_K16.out`):

| r | 3 | 6 | 12 | 17 | 24 | 34 | 48 | 68 | 96 |
|---|---|---|---|---|---|---|---|---|---|
| T_B, L = 320 | 0.115 | 0.123 | 0.163 | 0.195 | 0.182 | 0.087 | 0.037 | 0.012 | 0.035 |
| T_H, L = 320 | 0.070 | 0.071 | 0.075 | 0.073 | 0.054 | 0.023 | 0.0085 | 0.013 | 0.066 |
| U_B = ‖(B−1)ψ‖ (contrast) | 0.17 | 0.18 | 0.21 | 0.27 | 0.39 | 0.57 | 0.80 | 1.09 | 1.45 |
| ‖(B_aᵀB_a − 1)ψ‖ | 9e-4 | 9e-4 | 1e-3 | 1e-3 | 1e-3 | 2e-3 | 3e-3 | 1e-2 | 7e-2 |

- **Registered AICc over the full range** (`r116_fit2.out`).
  - L = 320: T_B ΔAICc = +0.86 (**undecided**); T_H −3.95 (**power**).
  - L = 240: T_B −3.6 (power); T_H +2.6 (super-polynomial).
  - P = ±0.2 (L = 240): every series is undecided (|ΔAICc| < 2).
- **Floor flags** (L = 240 against L = 320, change > 30%): r = 68 and 96 for T_B; r = 48, 68 and 96 for T_H. The secondary fit on the unflagged points gives super-polynomial (+4.0 and +7.9). But it contains no separated tail regime, only the plateau and the onset of the fall.
- **Contrast with the un-subtracted quantity.** The subtracted T_B falls once the cluster separates (r ≥ 24). The un-subtracted U_B grows: 0.17 → 0.80 by r = 48. This shows directly that the subtraction removes R9-3's registration defect (checked).
- **Reading.** The registered comparison is not a valid discriminator on these series. They are non-monotone, because r ≲ 20 is not yet a cluster (dimer size ≈ 6 and spectator packet ≈ 6 in position), and they are resolution-limited beyond r ≈ 48. The "power" outcomes measure the window, not a tail.

### 4.5 Invertibility of A on the dense grids (checked; reading suggested)

| P | L = 128 | 160 | 240 | 320 |
|---|---|---|---|---|
| s_min(A_S3), P = 0.2 | 0.80 | 0.70 | 0.39 | 0.079 |
| s_min(A_S3), P = 0.4 | 0.39 | 0.16 | 4e-5 | 0.000 |
| s_min(A_S2) (R9-3's mean), P = 0.4 | 0.39 | 0.16 | 1.7e-5 | — |
| ‖B_a − 1‖₂, P = 0.4 | 0.77 | 1.03 | 1.63 | 1.87 |

- **Where the near-null vector sits** (`r116_nullvec_L240_P0.4.out`):
  - 97% of its weight has |x₁₂| < L/8, so pair 12 is together;
  - 99.7% has |x₃| > L/4, so the spectator is at the ring antipode (mean |x₃| = 113 of a maximum of 120).
  - That is where the spline chart change samples e^{−ip₃x₃} at ≈ 2 points per period.
- **Why it cannot be continuum physics.** For a true a-cluster state A = B_a + E with Eψ → 0, so ‖Aψ‖ → 1. The near-singularity is therefore a discretization artefact (suggested, strongly supported).
- **The same artefact explains three other numbers:**
  - S4's per-step s_min floor: min s_min(A_k) = 0.051, 0.038 and 0.031 for K = 8, 16 and 32 at L = 160, P = 0.4. It does not → 1 as K grows.
  - ‖B − 1‖₂ = 2 for S4 at L ≥ 240, P = 0.4.
  - The S4 algebra glitch in §4.2.
- **Consequence.** No dense-grid s_min is a valid stand-in for the continuum constant in Lemma P. Lemma P's constant for S3 or S2 is therefore **not controlled here**.
- The growth of ‖B_a − 1‖₂ toward 2 is consistent with a dilation-type packing whose spectrum fills the circle (suggested; RECALLED from the R7-6 mechanism).

### 4.6 (c) Large-r subtracted-tail components (checked; post-registration, declared; same AICc rule)

- **Method.** Matrix-free, at P = 0.4, using R9-3's exact reduction B_c − 1 = Q_G(B_c − 1)Q_G (`r116_tails.py`).
- **States.** ψ_r is the dimer ⊗ packet product. B_aψ_r is evaluated analytically.
- **Symmetry check.** Channel c equals channel b to all printed digits (ψ is odd under 1↔2), as it must.

| r | ‖(B_b−1)ψ‖ | ‖(B_b†−1)B_aψ‖ | ‖D_b B_aψ‖ | ‖(B_b(½λ)−1)ψ(½λ)‖ |
|---|---|---|---|---|
| 20 | 1.44e-1 | 1.40e-1 | 5.37e-2 | 7.40e-2 |
| 40 | 3.79e-2 | 3.98e-2 | 1.21e-2 | 1.85e-2 |
| 80 | 4.15e-3 | 4.30e-3 | 8.83e-4 | 1.63e-3 |
| 160 | 4.86e-4 | 6.18e-4 | 9.04e-5 | 2.46e-4 |
| 320 | 1.60e-5 | 1.66e-5 | 3.09e-6 | 1.11e-5 |
| 453 | 1.31e-6 | 1.57e-6 | 4.09e-7 | 1.32e-6 |
| 640 | 1.99e-7 | 2.82e-7 | 4.18e-8 | 9.78e-8 |

(11 points in all, r = 20·2^{k/2}; see the `.out` files.)

- **AICc** (`r116_fit.out`, `r116_fit2.out`):

| component | ΔAICc(W−S), full 20–640 | ΔAICc, r ≥ 80 | fitted β | local slopes |
|---|---|---|---|---|
| B | +29.8 | +7.1 | — | 1.0 → 7.2, last 5.4 |
| B† on B_a | +26.7 | +3.7 | — | 1.1 → 6.8, last 5.0 |
| D | +30.8 | +19.0 | — | 1.5 → 6.6, monotone |
| s = ½ indicator | +23.5 | +25.2 | — | — |

  - Every comparison prefers super-polynomial. The best-fit β is 0.3–0.45, consistent with R9-3's exp(−c√r) form-factor class (`vR9-3:43`, comparator).
- **Controls.**
  - Convergence: ppo 12 → 20 and hfac 0.03 → 0.015 leave r = 226, 320 and 453 unchanged to 5 digits (`r116_tails_b_B_P0.40_conv.out`).
  - P = 0 control: 3.2e-11 (`r116_tails_b_B_P0.00_P0.out`).
- **What these numbers are.**
  - For S3, Lemma P gives T_B ≤ e₁ + C(s)(5e₁ + e₂), with e₁ ≤ 2‖(B_b − 1)ψ‖ and e₂ ≤ 2‖(B_b† − 1)B_aψ‖ (b ↔ c symmetry). Both fall super-polynomially on this window, but C(s) is uncontrolled (§4.5).
  - For S4, Lemma T needs Ĝ_c(s) on B_a(s)ψ_r for s < 1. That was **not computed**. The s = ½ column is an indicator on a different state (the half-coupling dimer), not that integrand.
  - For T_H, Lemma G needs ‖E_H B_aψ‖. The computed ‖D B_aψ‖ is its suggested leading proxy, plus Δ† terms of the same type.
- **Same caveat as R9-3** (`vR9-3:§6`). The full window 20–640 includes the r ≲ 60 packet and dimer overlap regime. Only 0.9 decades are operator-dominated, and the r ≥ 80 preferences are weaker for B and B† (+7.1 and +3.7). A finite window cannot certify an asymptotic class.

---

## 5. Reading against the FIXED readings (`TESTS.md:4259-4263`)

**PASS: not met.**
- (b) **Met for S3** (residuals 4.1e-3 → 7.4e-6 → 7.6e-7). For S4 the residuals are not monotone at L = 160, traced to the antipodal artefact.
- (d) **Met.** The mass is flat to ≤ 5e-14, by construction in the stated prescription.
- (c) **Not met.**
  - On the assembled operators, the registered comparison over the registered range is undecided or power (L = 320: +0.86 and −3.95). The series is resolution-limited and contains no separated tail.
  - The super-polynomial evidence (§4.6) is for bound ingredients, matrix-free, post-registration, with an uncontrolled constant for S3 and a missing integrand for S4.
- "Checked" for (c) is therefore not met.

**FAIL: not met.**
- No subtracted channel deviation was found or proved to decay like a power.
- Every subtracted quantity that could be followed decays super-polynomially by the comparison in its operator range (§4.6).
- The registered "power" outcome in §4.4 is a window artefact.

**INCONCLUSIVE: the worker reading.** This matches the expectation (`TESTS.md:4263`).

**What changed against R9-3.**
- The operators are now assembled: B (S3, S4), H_S and K_S exist on five grid sizes.
- The subtraction repair works as the referee said. Subtracted T_B falls once the cluster separates, while un-subtracted U_B grows: 0.17 → 0.80 (r = 3 → 48).
- Three new proved lemmas reduce the subtracted tails to single-channel components.
- The adjoint component ‖(B_b† − 1)B_aψ‖ and the generator component ‖D_b B_aψ‖, new here, track the already-known ‖(B_b − 1)ψ‖ (R9-3's object) over 20–640.
- The dense-grid "singular packing" is an antipodal artefact, which disarms a trap for later probes.

## 6. Strong-word check

- **"Assembled"** means dense matrices in the FC chart-quadrature prescription, with cubic-spline chart changes and an edge taper. It is not the lattice ring's own lab grid at P ≠ 0, and K is not built from site positions.
- **"Exact" or "by construction"** (algebra, trimer flatness) means conjugation identities in the FC prescription, where M_BT does not depend on P by definition. They test unitarity and the ∂_P discretization, not lattice physics.
- **"Super-polynomial"** is a finite-window AICc preference on components over 20–640 (0.9 operator-dominated decades). It is not an operator bound and not the registered observable.
- **"Artefact"** (§4.5) is supported by the antipodal localization of the near-null vector and the a-cluster argument. A continuum invertibility proof of S2 or S3 is **not** given.
- **"Proved"** covers Lemmas P, T (finite-dimensional) and G (algebraic). The continuum Duhamel form and the E_H → D reduction are suggested.
- **Nothing here** bears on d ≥ 2, N ≥ 4, pair creation, gravity, Ward identities or the ⊗M₂ composition.

## 7. Price (named, not adopted)

- **Unchanged from R7-6 §8 and R9-3 §8:**
  - a tower of connected many-body terms;
  - instant form, forced by H-P (an added bridge);
  - R7-1's prices (non-quasi-analytic form factors, frame-fixed box, inert edge).
- **Added, a reading:**
  - The packing that avoids any invertibility hypothesis is the ordered exponential (Construction S, Lemma T). Its tail is governed by the coupling-flow generators Ĝ_c(s) on a-cluster states. Those are the objects a quasi-locality proof must bound.
  - A finite-grid realization needs a chart-change prescription that stays unitary up to the ring antipode. Cubic splines do not.
- No axiom text changes. Admissibility does not fix the dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-130`).

## 8. For the referee

1. **Lemma P and Lemma T** (§3), and the claim that S4 needs no invertibility in its K → ∞ form.
2. **Reruns** (OMP_NUM_THREADS = 2):
   - `python3 r116_s4.py L=240 K=16 Ps=0.4 kinds=dimer`: confirm T_B = 0.0868 and 0.0390 at r = 33.9 and 48.
   - `python3 r116_tails.py ch=b op=Bdag rs=80,160,320`: confirm 4.30e-3, 6.18e-4 and 1.66e-5.
3. **§4.5's diagnosis.** Is the near-null vector of A an antipodal discretization artefact? `python3 r116_nullvec.py L=240 P=0.4`.
4. **§4.4's registered comparison.** Does it read as "not discriminating", or literally as the PASS-blocking undecided/power? INCONCLUSIVE holds either way.
5. **The cheapest decisive next step.** Compute the Lemma-T integrand ‖Ĝ_c(s)B_a(s)ψ_r‖ for s ∈ (0, 1] matrix-free. B_a(s)ψ is smooth in q₁₂, so a 2D spline in (k₃ fine, q₁₂ coarse) suffices. Together with a uniform lower bound on Lemma P's per-step constant, this would turn §4.6 into a checked bound on T_B for S4.
