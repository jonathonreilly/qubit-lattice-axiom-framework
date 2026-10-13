# C5 R19-1: graviton production from the Z₂ window. Can a tensor branch be light-like at or near the RK point?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). Ran 2026-10-13, 03:50Z to about 04:22Z.
- **Unrefereed.** Worker reading: **NEITHER** (§7).
  - **RK-Z2 is not established.** The proofs here cover four things: βU = 0 exactly; every finite Rayleigh–Ritz (multi-mode SMA) branch, under an exponential-clustering hypothesis (R2); every exact isolated branch whose remainder is regular (Theorem 6, (R2) plus (Iso)); and the f-sum class at every finite βU. None of them covers every exact branch of the class at βU > 0.
  - **LIGHT-LIKE-SMA fails.** The registered ensemble has a k⁰ TT f-sum at every finite βU (proved). So a linear SMA bound would need S_TT ∝ 1/|k|. The measured S_TT is finite and flat (checked, βU ≤ 3, L = 6, 8). Under a second reversible generator, the actual TT relaxation is a flat, k-independent exponential decay (checked, §4b).
  - Several pieces are no-go type: Lemma 3, Proposition 4, Theorem 5 and Theorem 6. **They need the sol referee before they are recorded.**
- I edited no repository file and downloaded nothing. Every run used OMP_NUM_THREADS=2 and finished in under 5 minutes; the longest took 247 s.
- The method was fixed before any run (`S/METHOD_preregistered.md`, about 03:58Z), including the equilibration criterion.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`.
  - R19-1 is at `TESTS:7149-7182`: FIXED readings `:7174-7178`, expectation `:7179-7182`.
  - Round-19 rules `:7117-7131`; round-18 rules `:6395-6406`; round-17 rules `:5688-5706`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `vR18-1` = `P/agents/C5_R18-1_referee_verdict.md`, and likewise `vR18-10`, `vR17-1`, `vR17-6`. `rR18-1` = `P/agents/C5_R18-1_report.md`. `S26` = `P/agents/C5_S26_synthesis.md`.
- `S` = `scratchpad/C5/R19-1/`. Scripts and `.out` files are in `S/scripts/`, pickled data in `S/data/`.

**Labels.**
- **proved:** derived here, unrefereed.
- **checked:** numerics run here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature, RECALLED, not fetched.

---

## 0. Plain words

- **The question.**
  - At a Rokhsar–Kivelson (RK) point, the quantum Hamiltonian is a classical Markov generator in disguise. Its excitation energies equal the relaxation rates of the classical ensemble whose weights are |ψ₀|².
  - A graviton needs a branch with ω = c|k|. Can the Z₂ tensor ensemble of R18-1 supply one at, or just off, the RK point?
- **The answer here: no, at the level that can be computed. A complete proof for the class is still missing.**
  - **The f-sum is k⁰ (proved).** Every registered move (cube, μ8) can change the TT label sum at k = 0, which equals changing the γ-dipole. At every finite βU this happens with positive probability, uniformly in the volume. So the TT f-sum tends to a positive constant as k → 0.
  - **So the SMA bound is a gap, not a cone (checked).** ω_SMA,TT = f/S is flat in k along the axis, face and body directions. It falls with βU: about 8.7, 4.9, 1.0 and 0.14 (units of t) at βU = 0.5, 1, 2 and 3, the same at L = 6 and 8.
    - The vector channel's bound is higher and rises with k.
    - The bound only caps the lowest excitation. It does not prove a gap.
  - **At βU = 0 everything is exact (proved).** Every slot-label observable decays at exactly 8t (diagonal slots) or 12t (face slots). That gives flat, strictly gapped TT, V and S bands, and a whole-generator gap ≥ 2t (8t at L = 2).
  - **Why no RK branch can be light-like in any computable approximation (proved, Theorem 5).** An RK Hamiltonian is a first-order (relaxational) generator: its eigenvalues are decay rates. For any finite set of local modes, the rates along a ray k = t·k̂ are analytic, non-negative functions of the signed coordinate t, when correlations decay exponentially. A non-negative analytic function that vanishes at k = 0 vanishes to even order. So each such branch is gapped or goes as k² or faster.
    - A light-like ω = c|k| is a square root of an analytic ω², which is the structure of a wave equation (second order), not of relaxation.
  - **The same holds for exact isolated branches (proved, Theorem 6).** If a T₂ branch is an isolated atom over a remainder with regular moments, exponential clustering forces its dispersion to be gapped or O(k²). Branches that sit on a low-energy continuum are not covered.
- **What a light-like branch needs (proved as an exhaustive fork at SMA level).**
  - The f-sum is an even trigonometric polynomial in k, so it goes as k^{2a} (a = 0, 1, 2 for the k⁰, k² and k⁴ classes).
  - A linear SMA then needs S_TT ∝ |k|^{2a−1}: S ∝ 1/|k| in the k⁰ class, S ∝ |k| in the k² class, S ∝ |k|³ in the k⁴ class. Each is an odd power, a long-range (non-screened) equal-time correlation.
  - **At an RK point the equal-time S is the classical one.** In the screened regime it is analytic, so all three are excluded. A classical pinch-point (Coulomb) ensemble gives a finite S_TT (comparator), so that is excluded too.
  - So a light-like tensor branch needs a non-RK quantum phase with zero-point TT fluctuations of odd power. The registered target "S_TT ∝ |k|" is the k² case. To reach the k² class, the moves must conserve the six label totals (P143). The leading t ≠ v correction to S_TT is analytic in the screened regime (suggested), so the |k| cannot come from perturbing the RK point.
- **A side result (outside the registered move set).** With R18-10's dipole-conserving moves (P143), the f-sum is k² exactly. If S_TT stays finite, the SMA then shows a gapless T₂ relaxation mode with ω ≤ Ck². That is a diffusive "graviton" (z = 2), not a light-like one.

---

## 1. Setting, hypotheses, readout bridge (`TESTS:7157-7161`)

**Ensemble (as R18-1, literal).**
- Slots and stencil: N0914's slots and integer stencil, labels n ∈ {0,1}, the mod-2 law (Gn even), γ = Gn/2 ∈ {−1, 0, 1}.
- Weight π ∝ exp(−βU Σ_edges γ²).
- Moves: XOR of the cube and the three μ8 orientations, at every translate.
- Sector: the trivial coset of the move span (`rR18-1:47-50,85-87`).
- I copied and reused R18-1's `common.py` and `mc.py`. Rechecks are in §2.

**RK Hamiltonian (literal registration "H = Σ_moves [−t·flip + v·(potential)] at t = v").**
- H = Σ_m t[−X^{p_m} + e^{−βU Δ_m(C)/2}], where Δ_m(C) = E(C ⊕ p_m) − E(C) and E = Σγ². This is the standard stochastic-matrix RK form (Castelnovo–Chamon–Mudry–Pujol; comparator).
- **Signs of law data (rule `TESTS:7125`).** The classical weights and rates are positive (unsigned). The quantum off-diagonal elements are −t: stoquastic, so signed only in that sense. No signed law weights are used anywhere.
- **Readout bridge.** X-basis labels (P113, carried). The RK identity makes equal-time S classical, which is the registered bridge (`TESTS:6438`; `S26:320`). Here it is extended to dynamics by Lemma 1, which is an identity, not a further bridge.
- **Excluded (as registered):** integer-law lifts; non-local moves; degenerate grounds (so βU = ∞ is not used); the t ≠ v phase beyond leading order.
- **Removed hypothesis (`TESTS:7167`):** statics only. Kept: locality, finite fugacity, the mod-2 law, R18-1's move set.
- **Invariance (rule `TESTS:7130`).** The ground state |ψ₀|² = π is invariant under the shift action of all 24 rotations. The weight is invariant (24/24) and the trivial coset maps to itself (`vR18-1:5`). This is P112, carried.

---

## 2. Prior art (each counted once) and rechecks

**Prior art.**
1. **R18-1 / vR18-1.** The ensemble; frozen at βU = ∞; numerical reading OPEN because βU = 4 is not equilibrated (`vR18-1:9`); Theorem Z₀ in the uniformly LR-local class (`vR18-1:11`); the same-component control rule (`vR18-1:7`).
2. **R18-10 / vR18-10.** The dipole is six label totals (`vR18-10:3`). Fixed-N screening (`:7`). Planar laws fake axis zeros (`:11`). Reading OPEN (`:13`). Its fixed-dipole sector is P143 (`S26:420`).
3. **R17-6 / vR17-6.** Theorems G, Z, Z′. "Gapped" means a uniform spectral gap including continua (`vR17-6:13`). Identity V narrowed (`:15`).
4. **R17-1 / vR17-1.** The moment identity M₀ = −N·D(γ_δ) and the k⁰/k²/k⁴ classification (`vR17-1:10`). The CSS k⁰ model (`:16`). The TFIM duality (`:19`).
5. **R15-5 (worker).** k³ at strong coupling. z = 2 options are excluded by GW timing (`P/agents/C5_R15-5_report.md:176`, reading there).
6. **Repository U(1) lane: the vector analogue of this question** (grep "Rokhsar"; counted once as one prior-art item):
   - `docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:105-118`: the RK point does not by itself give a linearly dispersing photon ("special RK scaling"). The photon phase is an external input on the δV < 0 side.
   - `docs/THE_PURE_SPIN_HALF_LINK_MODEL_..._QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_BOUNDED_NOTE_2026-09-04.md:4`: a finite quadratic transverse mode; no Maxwell photon established.
   - `docs/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_..._2026-09-24.md:53`: the RK term as a weighted flip-graph Laplacian.
   - R19-1 is the rank-2 Z₂ version of the same question. Its answer has the same structure.
7. **Comparators (RECALLED):**
   - z = 2 RK dynamics of classical Coulomb phases (Henley; Moessner–Sondhi);
   - ω ∝ k in the quantum Coulomb phase off the RK point (Hermele–Fisher–Balents);
   - rank-2 and lattice-graviton qubit models (Xu; Gu–Wen; Pretko);
   - the SMA bound (Bijl–Feynman);
   - Rellich's theorem on analytic Hermitian families (Kato);
   - quadratic dispersion in gapless frustration-free systems (Masaoka–Soejima–Watanabe 2024; Gosset–Mozgunov), cited only as a comparator;
   - Bravyi–Hastings–Michalakis gap stability (comparator only).

**Rechecks of the archived runners before relying on them.**
- **`common.py` / `mc.py` (R18-1).**
  - (i) `s1`: built the L = 2 RK Hamiltonian independently from `G_matrix` and `pattern_vectors`.
  - (ii) `s2`: my numba f-sum estimator, applied to exact enumeration, reproduces s1's f exactly (6.00000, 1.24920, 0.13911 at βU = 0, 1, 2).
  - (iii) At βU = 0 the MC reproduces the exact solution (§4).
  - (iv) E/edge matches R18-1's table at every accepted point (`s4_summary.out`).
  - L = 2 MC (single-sweep sampling, no error bars) is 4–16% off exact at βU = 1–2 (`s2_check_L2.out`). That is slow mixing at L = 2, where s1 shows generator gaps of 0.84 and 0.088. The production runs are at L = 6, 8.
- **R17-1, R17-6 and R18-10 runners.** Not rerun. I use only their refereed statements: the moment identity (`vR17-1:10`); dipole = label totals (`vR18-10:3`); Z₀'s scope (`vR18-1:11`). The one ingredient I need from R17-1's pattern data, the values of ε:M₀ on the four patterns, is recomputed independently in `s3`.

---

## 3. Probe (a): the RK-point f-sum (proved; checked)

**Lemma 1 (RK structure; proved; checked at L = 2 in `s1`).**
- (i) **Frustration-free.** Each move term restricted to {C, C ⊕ p} is t·[[e^{−βUΔ/2}, −1], [−1, e^{βUΔ/2}]], with eigenvalues 0 and 2t·cosh(βUΔ/2), and its null vector is ψ₀ ∝ e^{−βUE/2}. So H ≥ 0 and Hψ₀ = 0.
- (ii) **Markov form.** 𝓛 = −Ψ⁻¹HΨ (Ψ = diag ψ₀) is the Markov generator with rates r_m(C) = t·e^{−βUΔ_m(C)/2}, reversible with respect to π.
- (iii) **Spectral identity.** For a diagonal observable O, ⟨Oψ₀, φ(H) Oψ₀⟩ = ⟨O, φ(−𝓛) O⟩_π. So the quantum spectral measure of O equals the classical relaxation spectral measure, and the quantum imaginary-time correlation equals the classical autocorrelation.
- (iv) **f-sum = Dirichlet form.** Exactly,
  **f(k, ε) := ½⟨[O†,[H,O]]⟩ = (1/2V) Σ_m ⟨ r_m · |Σ_{s∈p_m} e^{−ik·pos_s} c_s σ_s|² ⟩_π**, with σ_s = 1 − 2n_s, and c = ε_jj on diagonal slots and 2ε_ij on face slots (R18-1's normalization).
  - Also f = Σ_n ω_n |⟨n|O|0⟩|², using the real basis and |O_{−k}| = |O_k|.
- **Checked (`s1`), L = 2, βU = 0–4:**
  - |H − Hᵀ| = 0 and |Hψ₀| ≤ 5.5e-15;
  - the Markov rows sum to zero, with detailed balance to ≤ 1e-18;
  - the quantum double commutator equals the classical formula in every (k, channel) entry, to all printed digits.

**Lemma 2 (βU = 0 exact solution; proved; checked).**
- At βU = 0, −𝓛 = tΣ_m(1 − X_m). The characters χ_v(C) = (−1)^{v·C} are eigenfunctions with eigenvalue 2t·#{m : v·p_m odd}.
- **Whole-generator gap.** On the coset, nonconstant classes have v ∉ span⊥, so at least one move pairs oddly with v. Hence gap ≥ 2t, uniformly in V. At L = 2 the gap is 8.000t (`s1`).
- **Slot-linear observables.** n_s − ½ = −½χ_{e_s} has eigenvalue 2tN_type. Here N_type = 4 for diagonal slots and 6 for face slots (`s1` header: [4 4 4 6 6 6]).
  - So every slot-linear observable, including every TT, V and S channel at every k, has spectral measure ‖O_diag‖²δ(ω − 8t) + ‖O_face‖²δ(ω − 12t). The two parts are orthogonal as eigenfunctions with different eigenvalues.
  - **Two flat, strictly gapped bands**; whole-zone v_max = 0 for these bands.
- **Checked:** at L = 2 all weight sits at ω = 12.000 (`s1`). At L = 6 the MC gives f_TT2,axis = 6.008(11) against exact 6, S = 0.4875(143) against exact ½, and f/S = 12.3(4) against exact 12. For TT1: 1.9987(27) against 2, 0.2478(69) against ¼, and 8.06(22) against 8 (`../data/test_L6_b0.pkl`, `an_fs.py`). This is the same-component, same-normalization control (rule `TESTS:7127`).

**Lemma 3 (the TT f-sum is k⁰ at every finite βU, uniformly in V; proved; ingredients checked in `s3`).**
- **Form of f.** f(k, ε) = Σ_Δ F(Δ) cos(k·Δ), where Δ runs over the finitely many intra-pattern separations and F(Δ) is a π-average of bounded local functions. So f is an even trigonometric polynomial with V-uniformly bounded coefficients, and |f(k) − f₀| ≤ Ck².
- **f₀ is the γ-dipole jump.** f₀(ε) = (1/2)Σ_types ⟨r · |ε:M₀(σ|_p)|²⟩_per-site. By the moment identity M₀(δ) = −2D(Δγ) (`vR17-1:10`), this is the rate-weighted square of the change in the γ-dipole.
- **Positivity.** Fix ε. By `s3`, for every TT1, TT2, V1, V2 and S polarization along the axis, face and body directions:
  - some pattern type p admits a sign pattern with ε:M₀ ≠ 0;
  - there is a move q sharing exactly one slot s₀ with p, with c_{s₀}(ε) ≠ 0 (at least 6 such q in every case).
- **The map n ↦ n ⊕ q** is a bijection of the coset. It sends {ε:M₀ = 0} into its complement, because the sum changes by −2c_{s₀}σ_{s₀} ≠ 0. It changes E by at most 12, since each move touches 12 edges (`s3b`; empirical maximum 8) and γ² ∈ {0,1}.
  - Correction during the run: `s3`'s last line counted 6/4 edges, using the all-ones lift only, which cancels on half the edges. `s3b` gives the correct count, 12 for every move type.
- Hence P_π(ε:M₀ ≠ 0) ≥ e^{−12βU}/(1 + e^{−12βU}). Also r ≥ t·e^{−6βU}. So:
  **f₀(ε) ≥ (t/2) μ_min(ε)² e^{−18βU}/(1 + e^{−12βU}) > 0**,
  where μ_min is the smallest nonzero |ε:M₀| over sign patterns. This holds for every finite βU, every V, and every TT polarization in every direction. ∎
  - The bound is crude. The measured values are much larger (§4).
- **Reading.** The registered ensemble is in R17-1's k⁰ class at every finite βU. The likeliest failure registered in the expectation (`TESTS:7181`) is realized.

---

## 4. Probe (b): the SMA bound along axis, face and body (checked)

**Runs.**
- L = 6 and 8; βU ∈ {0.5, 1, 2, 3, 3.5}; two seeds each, plus longer reruns at βU = 3 (L = 6) and βU = 3.5.
- Equilibration criterion fixed in advance (METHOD (b)):
  - (i) E/edge within 2% of R18-1's s5b table, for each seed;
  - (ii) two passing seeds agree on f and S at the smallest axis k within 3σ.
- **Applied conservatively.** Every seed that was run must pass (i). No seed is selected after the fact. I state this reading of METHOD (b) here because the text says "two seeds" and more were run.
- Result (`s4_summary.out`):
  - **accepted:** L = 6 and 8 at βU = 0.5, 1, 2; L = 8 at βU = 3.
  - **Not accepted:**
    - L = 6, βU = 3: seeds at +3.9%, −0.5%, +4.6% and +1.1%, even with 400 000 equilibration sweeps;
    - βU = 3.5 at both L: L = 6 at +1.2%, +9.2%, +1.5%, −6.7%; L = 8 at +1.4%, −3.9%, −6.1%, +0.3%.
  - The seed scatter at fixed, long run length is slow mixing (suggested), consistent with the activated rates below. This agrees with `vR18-1:9`, which accepts data only through βU ≤ 3.5 and found βU = 4 unequilibrated.
  - The βU = 0 runs are a single seed per L. They are checked against the exact solution (Lemma 2) instead.
- **βU = 3.5, informational only (not accepted):** in all four L = 8 seeds, ω_SMA,TT2 on the axis is 0.047–0.057 at m = 1 and 0.053–0.057 at m = 2. The V bound is 0.29 at m = 1 and 0.73 at m = 2. Same flat, gap-type pattern; the conclusions do not rest on these points.

**The table (L = 8, seed-averaged, units t; full table in `s4_summary.out`).** Each cell gives ω_SMA = f/S at m = 1, then m = 2 (k = π/4, π/2 along the axis), except the face column, which gives TT1 / TT2 at m = 1. The body column is TT1.

| βU | TT2 (T₂), axis | TT1 (E), axis | TT1 / TT2, face, m = 1 | TT1, body | V1, axis | S, axis |
|---|---|---|---|---|---|---|
| 0.5 | 8.66, 8.63 | 5.99, 6.02 | 7.23 / 8.66 | 8.39, 8.15 | 9.03, 9.98 | 6.26, 6.62 |
| 1 | 4.89, 4.91 | 3.56, 3.53 | 4.29 / 4.77 | 4.79, 4.84 | 5.51, 7.01 | 3.86, 4.51 |
| 2 | 0.973, 1.022 | 0.745, 0.755 | 0.984 / 0.940 | 1.068, 1.073 | 1.66, 2.95 | 0.97, 1.38 |
| 3 | 0.140, 0.150 | 0.105, 0.118 | 0.155 / 0.136 | 0.171, 0.177 | 0.50, 1.14 | 0.19, 0.30 |

- **f_TT and S_TT are both flat in k (checked).**
  - βU = 2, TT2, axis: f = 1.112 and 1.160, S = 1.142 and 1.136 at q² = 0.59 and 2.0.
  - βU = 3: f = 0.194 and 0.208, S = 1.389 and 1.387.
  - L = 6 (k = π/3, 2π/3) gives the same ω_SMA within a few percent, for example 0.983 and 1.033 at βU = 2. So there is no L dependence beyond errors at the accepted points.
- **The two TT polarizations have the softest SMA bounds;** along the axis the E polarization (TT1) is lowest. The V bound lies above TT in every direction at βU ≥ 1 (at βU = 0.5 the body V1 bound, 8.10, is slightly below TT1's 8.39), and grows with k: R18-1's screening suppresses S_V at short wavelength. The S bound along the axis lies above TT1.
- **This is not a proof of strict V/S gaps.** The SMA is an upper bound.
- **Six-mode Rayleigh–Ritz (`s5`).** This is the generalized eigenproblem F v = λ G v on all six slot types at each k. The lowest RR rate at L = 8 (axis, m = 1, then m = 2) is:
  - 5.94, 5.96 (βU = 0.5);
  - 3.53, 3.52 (βU = 1);
  - 0.744, 0.753 (βU = 2);
  - 0.103, 0.117 (βU = 3).

  The three lowest RR branches are flat in k. The three highest grow with k. None is linear.
- **Off-axis rule (`TESTS:7128`).** Face and body channels are reported. They show the same flat, gapped-type SMA bound as the axis.
- **βU scaling (suggested).** ω_SMA,TT falls by about e^{1.9} per unit βU between βU = 2 and 3. The L = 2 generator gap falls by about e^{2.0} (0.0876 → 0.0114; `s1`). So TT relaxation is activated, with a barrier near 2 (rate ~ e^{−2βU}): flat and slow, not light-like.
- **Reading for (b).** At every accepted point, the SMA bound in the TT channel is a k-independent constant, positive and finite, along all three directions. It is uninformative about gaplessness. It is exactly the "gap" form the expectation names as the likeliest failure.

### 4b. Beyond the SMA: the actual relaxation of each channel (checked; a different generator in the same class)

- **What was run (`s6_dyn_autocorr.py`; added after the main runs; not pre-registered).**
  - The time autocorrelation C(k,τ) of each channel under R18-1's random-sequential Metropolis dynamics.
  - Its rates are min(1, e^{−βUΔ}) per move per sweep. That is a different reversible local generator from the literal registered H, which has rates e^{−βUΔ/2}.
  - By Lemma 1 it is the relaxation spectrum of another RK Hamiltonian in the class, with hopping −t·e^{−βU|Δ|/2}. **It is a new completion and is reported as such** (rule `TESTS:7124`). I could not afford the literal square-root rates without a rejection-free (BKL) code in the time available.
  - 40 000 sweeps per run, one seed each. Time unit = one sweep. The printed E/edge is a final snapshot, not an average.
- **βU = 2** (L = 6 and L = 8 agree; `s6_dyn_L6_b2.out`, `s6_dyn_L8_b2.out`).
  - C_TT(k,τ) decays exponentially at a rate Γ_TT ≈ 0.16–0.19 per sweep. Γ is the same at m = 1 and m = 2, and along the axis, face and body directions. For example, L = 8 axis TT2: Γ = 0.182 at k = π/4 and 0.190 at π/2; body: 0.187 and 0.186.
  - The vector channel decays faster, and faster at larger k: axis V1, Γ = 0.29 and 0.47.
  - So the TT relaxation is a flat, k-independent band at these k: not light-like, and not diffusive.
- **βU = 1, L = 8** (`s6_dyn_L8_b1.out`).
  - The decay is faster than one sweep. C(1)/C(0) = 0.10–0.19 for TT, the same at m = 1 and 2 to within 0.007.
  - The fit window [1, 6] is unusable there (Γ printed as nan); C(1)/C(0) is the reported quantity.
- **Scope.** Two finite L, two k per direction, one generator outside the literal registration. This is checked evidence of a flat TT band, not a proof of a uniform gap.

---

## 5. Probe (c): analytic results (proved unless marked)

**Proposition 4 (no linear SMA without an odd-power S; proved).**
- f(t·k̂) is even and analytic in t (Lemma 3). Its leading term is f_{2a}(k̂)·t^{2a}, with a ∈ {0, 1, 2, …}.
- So ω_SMA(t·k̂) ∝ |t| along a ray if and only if S_TT(t·k̂) ∝ |t|^{2a−1}, which is an odd power.
- **In a screened RK ensemble** (truncated correlations of the readout decaying exponentially, uniformly in V), S is even and analytic in t. Then ω_SMA ∝ t^{2j} for an integer j, never ∝ |t|.
- **In a classical pinch-point ensemble,** S_TT has a finite direction-dependent limit. Then ω_SMA → f₀/S₀(k̂), or ∝ t² if f₀ = 0. Not linear.
- **In the registered ensemble,** f₀ > 0 (Lemma 3). So a linear SMA would need S_TT ∝ 1/|k|: a divergent TT structure factor. The measured S_TT is finite and flat (checked through βU = 3).
- **Exhaustive fork (rule `TESTS:7123`).** For the SMA in the stated class, the cases are:
  - (A) f₀ > 0, S bounded ⇒ an SMA "gap";
  - (B) f₀ = 0, f ∝ k², S → S₀ > 0 ⇒ z_SMA = 2;
  - (C) an odd-power S matched to the f-class ⇒ linear;
  - **NEITHER:** a nodal f₂ₐ(k̂) or log-corrected S, which gives some other power (not linear).

  The registered ensemble is in (A) at every accepted βU.

**Theorem 5 (even-order relaxation branches; proved under (R2)).**
- **Data.** Let a₁ … a_r be local observables, and a_i(k) their V^{−1/2} Fourier sums. Let G(k) be the connected static matrix ⟨a_i(k); a_j(k)⟩_π. Let F(k) = 𝓔(a_i(k), a_j(k)) = ⟨a_i(k), −𝓛 a_j(k)⟩_π be the Dirichlet (f-sum) matrix.
- **Hypotheses:**
  - (R1) finite-range moves with bounded rates (true here: |Δ| ≤ 12, `s3b`);
  - (R2) exponential clustering of π, uniformly in V. This is proved at βU = 0, where correlations of local functions are of finite range because the measure is a coset-uniform character measure. At βU > 0 it is a hypothesis, supported by R18-1's screening through βU ≤ 3.5 (`vR18-1:13`);
  - (R3) G(k) positive definite near k = 0.
- **Statement.** Along each ray k = t·k̂ the generalized eigenvalues of F v = λ G v can be labelled as real-analytic functions μ_j(t) ≥ 0 near t = 0. So each branch is either gapped (μ_j(0) > 0) or μ_j(t) = c·t^{2m}(1 + O(t)) with m ≥ 1. No Rayleigh–Ritz branch is ∝ |t|.
- **Proof.**
  - F is a finite trigonometric polynomial, because the Dirichlet form is local: a move contributes only if it overlaps both supports.
  - G is analytic by (R2).
  - G^{−1/2}FG^{−1/2} is then an analytic Hermitian family in one real variable, so Rellich's theorem gives analytic eigenvalue branches (comparator for the theorem; its use is standard).
  - Each branch is ≥ 0 because F ≥ 0.
  - A non-negative real-analytic function with a zero at t = 0 has a zero of even order. ∎
- **What it bounds.** Each μ_j(t) is a spectral mean of the true measure of a definite observable. So the lowest true excitation reachable from span{a_i(k)} lies at or below μ₁(t).
- **Contrast (reading).** For a quantum wave, ω² is the analytic object (a dynamical matrix), and ω = c|k| is its square root. At an RK point the rate itself is the eigenvalue of a non-negative analytic object. That is the structural reason RK points give z = 2 or a gap (as in Henley's and HFB's U(1) analyses, comparator).

**Theorem 6 (exact many-body branches, bounded class: no isolated light-like branch over a regular remainder; proved under (R1), (R2) and (Iso)).**
- **Hypothesis (Iso).** Along a ray k = t·k̂ near t = 0, the exact spectral measure of the T₂ readout O(k) has the form ρ_k = Z(k)·δ_{ω(k)} + ρ_hi(k), with:
  - Z(k) > 0 for t ≠ 0;
  - supp ρ_hi(k) ⊂ [Δ, ∞) for a fixed Δ > 0;
  - the remainder moments h_j(t) = ∫ω^j ρ_hi (j = 0, 1, 2) even and real-analytic in t.
- **Statement.** ω(t) is then a ratio of even analytic functions. So it is gapped, or ω(t) = O(t²). A light-like ω ∝ |t| is impossible. This holds whether the branch is statically visible or not, and in every f-sum class.
- **Proof.**
  - The full moments m_j(k) = ⟨O, (−𝓛)^j O⟩_π (Lemma 1(iii)) are even and real-analytic under (R1) and (R2).
    - m₁ = f is a trigonometric polynomial.
    - For j = 0 and 2, m_j(k) = Σ_d e^{ik·d} × (a π-covariance of two local functions at separation d). For j = 0 the two functions are o and τ_d o. For j = 2 they are 𝓛o and τ_d 𝓛o, which are local because 𝓛 is local, and have mean zero. So the coefficients decay exponentially by (R2).
  - Hence Z = m₀ − h₀, Zω = m₁ − h₁ and Zω² = m₂ − h₂ are even and analytic.
  - Then ω = (Zω²)/(Zω) has an expansion in even powers of t, and ω ≥ 0. ∎
- **What it covers and what it does not.**
  - This is an exact statement about the true many-body spectral measure, not a variational one.
  - (Iso) is restrictive. It excludes branches that sit on, or exchange weight with, a continuum reaching ω → 0. Such a continuum could carry compensating non-analytic moments; positivity alone does not forbid that.
- **Reading.** The proof uses RK only through the fact that the ground state's diagonal correlations are those of π. So at an RK point, screening of the classical ensemble (exponential clustering) is precisely what forbids an isolated light-like branch.
  - Quantum light-like phases evade this through algebraic ground-state correlations. In Maxwell, S_E ∝ |k| is not analytic.
  - That is §6's requirement (1) again, now at the level of exact isolated branches.

**What is not proved (the gap to RK-Z2).**
- Theorem 5 covers finite-mode (variational) branches. Theorem 6 covers exact isolated branches over a regular remainder, (Iso). Neither covers exact branches that touch or exchange weight with a low-energy continuum. Neither proves (R2) at βU > 0. So a light-like exact branch is not excluded in the full class.
- **Suggested:** it would need a non-analytic static matrix (long-range correlations), which (R2) forbids. Turning that into a proof needs a fibre decomposition of the generator on local observables, with control of the k → 0 quotient (total derivatives have vanishing norm). I did not do this.
- **Not proved either:** a uniform spectral gap at 0 < βU. Two comparator routes exist:
  - high-temperature gap stability for local reversible dynamics (Dobrushin–Shlosman / Martinelli);
  - BHM stability for the frustration-free perturbation of the βU = 0 stabilizer Hamiltonian, which is a commuting X-type CSS code with Gauss constraints.

  Neither was carried out. So gaplessness at intermediate βU is not excluded.
- The L = 2 exact data show a unique zero mode and a generator gap for βU ≤ 3 (8.000, 0.840, 0.0876, 0.0114). At βU = 4 the gap is below numerical resolution: the dynamic range is 1e11 and the min eigenvalue is 5e-7, which is not physical.

**The dipole-conserving variant (outside the registered move set; proved conditionally).**
- If every allowed move conserves the six label totals (R18-10's filter, P143), then ΔO_m(k = 0) = ε:ΔN = 0 for every move. So f₀ = 0 and f = O(k²) exactly.
- With S_TT(0⁺) > 0, the SMA gives a T₂ excitation at ω ≤ Ck², so the T₂ channel is gapless with z ≥ 2 at the SMA level. R18-10 reports S finite with R18-1's ξ (`vR18-10:7`), but S_TT(0⁺) > 0 is not proved here.
- **Reading.** P143 buys something dynamical, a diffusive (z = 2) tensor mode of the conserved label densities, but not a light-like one. This corrects nothing in `S26:420`, which concerned statics only.

---

## 6. Probe (d): what a light-like branch needs; the t ≠ v correction

**Requirements (from Proposition 4 and Theorems 5–6; proved at the SMA/RR level and for isolated branches under (Iso), suggested beyond).**
1. **An odd-power equal-time TT structure factor matched to the f-class.**
   - In the k² class, this is S_TT ∝ |k|. That is the registered target (`TESTS:7155`), the E-type reading: zero-point fluctuations ω/(2U), as in the Maxwell E-field (comparator).
   - In the k⁰ class, which is where R18-1's ensemble sits, it is S_TT ∝ 1/|k|. That is the h-type reading: the labels act as the metric potential, ⟨|h_k|²⟩ ∝ 1/ω.
   - Both are equally light-like at the SMA level. The f-class fixes which one is needed.
2. **Not an RK ground state.**
   - At an RK point S is classical. A screened classical ensemble has analytic S (excluded). A classical Coulomb/pinch ensemble has finite S_TT (excluded). An odd power would need power-law classical TT correlations with an odd-power Fourier singularity: C(r) ∝ r^{−2} for 1/|k|, or a hyperuniform C(r) ∝ −r^{−4} for |k|. That means a critical or otherwise long-range-correlated classical ensemble. None is seen in this one-parameter family through βU ≤ 3.5, where S_TT is finite and flat (suggested that none exists at larger βU; not tested).
3. **For the k² route, moves that conserve the TT label at k = 0.** This is P143's six label totals, or the R17-1 class (ii) (`vR17-1:10`: D(γ_δ) = 0 with γ_δ ≠ 0). Integer-lifted moves (γ_δ = 0) give k⁴ and need S ∝ |k|³; R16-7/R16-11 cap that class.
4. **Strict V/S gaps,** plus a pinch point in χ: Z₀'s requirement in its class (`vR18-1:11`).

**The leading t ≠ v correction (suggested).**
- Write H(v) = H_RK + δv·W, with W = Σ_m e^{−βUΔ_m/2} diagonal and δv = v − t.
- First order: δS_TT(k) = −2δv ∫₀^∞ dτ ⟨|O_k|²(τ); W(0)⟩_{π,c}. This is a time-integrated classical connected correlation of local functions under the RK Markov dynamics, using Lemma 1(iii).
- If the dynamics mixes exponentially in space–time (screened, gapped), this is even and analytic in k. So **at O(δv) the RK point acquires no |k| or 1/|k| term**.
- An odd power must therefore come non-perturbatively: a phase transition off the RK line into a quantum tensor Coulomb phase. In the U(1) analogue, that phase is reached from an unscreened classical Coulomb RK point (the δV < 0 side, comparator and repo note above).
- Here the only unscreened point is βU = ∞, which is frozen and degenerate (`vR18-1:5`; P130).
- **Reading.** The non-RK deformation must supply what the RK point lacks: a reactive, second-order (E, h) pair with positive stiffness for both. That is P96 stated dynamically. It cannot be obtained by perturbing this RK ensemble.

---

## 7. Readings against the FIXED clauses (`TESTS:7174-7178`)

- **RK-Z2: not met.**
  - Proved: βU = 0 (strict gap, flat bands); every finite Rayleigh–Ritz branch under (R2) (Theorem 5); every exact isolated branch over a regular remainder under (R2) and (Iso) (Theorem 6).
  - Not proved: exact branches outside (Iso), such as branches on or exchanging weight with a gapless continuum; and (R2) itself at βU > 0. The data support it through βU ≤ 3.5 (`vR18-1:13`), and a cluster expansion would give it at small βU (suggested, not carried out).
  - No refereed proof covers the class.
- **LIGHT-LIKE-SMA: not met, and excluded in the registered ensemble wherever S_TT is bounded.**
  - The f-sum is k⁰ (Lemma 3, proved), so a linear SMA needs a divergent S_TT ∝ 1/|k|.
  - The measured S_TT is finite and flat at every accepted point (βU ≤ 2 at L = 6 and 8; βU = 3 at L = 8; checked). The same holds at the unaccepted βU = 3.5 points (informational).
  - The strict V/S gaps are not checked either: the SMA only bounds from above.
- **NEITHER: yes (worker reading).** Both positive branches fail. The registered example, "the bound is z = 2 on samples but no proof covers the class", is realized in its gap form. The SMA bound is a flat gap on samples. The proofs cover βU = 0, the RR level, and exact isolated branches under (Iso), not the class.
- **OPEN:** not chosen. NEITHER's text applies literally.
- **For the referee.** Lemma 3, Proposition 4, Theorems 5 and 6, and the dipole-conserving corollary are no-go-type statements and must go to sol before they are recorded.
- **Expectation check (`TESTS:7179-7182`).**
  - "RK-Z2" was not reached as a proof.
  - "Likeliest failure: a k⁰ f-sum making the SMA uninformative (a gap) → NEITHER or OPEN": **realized exactly** (Lemma 3; §4).
  - "If RK-Z2 holds, the window becomes a non-RK phase with S_TT ∝ |k|": the conditional is not triggered. §6 nonetheless gives the sharpened target: an odd-power S_TT matched to the f-class (1/|k| for this ensemble's k⁰ class, |k| only after P143's conservation).

---

## 8. (e) Prices (named, never adopted)

| Price | Status | Axiom touched | Buys |
|---|---|---|---|
| **P-r19-1a: RK tuning v = t** | new, named. The RK point is one tuned ratio in the (t, v) family. Admissibility supplies no Hamiltonian (`AX:114-123`) | Admissibility dynamics (`AX:57-61,114-123`) | exact relaxational dynamics with classical statics. **Counting basis:** one number for the whole Hamiltonian, not per species |
| **(RK bridge)** | carried, unnumbered (`S26:320`). Lemma 1 extends it to dynamics as an identity, adding no structure | Record readout `AX:82-83` | classical MC for S and f |
| **P96** (emergent constraint / non-RK tensor Coulomb phase) | sharpened, no new number: "a reactive phase with an odd-power S_TT matched to its f-class". Not reachable at O(δv) from the screened RK line (suggested) | Admissibility dynamics | the only light-like route |
| **P143** (dipole conservation on the moves) | count once (`S26:420`). New dynamical content, conditional: k² f-sum, so diffusive T₂ modes (z_SMA = 2). Still not light-like | Admissibility | the k² class that "S_TT ∝ \|k\|" presupposes |
| **P112, P113, P110** | carried | `AX:37-41`, `AX:82-90`, `AX:47` | the setting |
| **P130** | carried (βU = ∞ frozen) | Admissibility dynamics | the only unscreened parent; not used |

**Counting convention.** No tuning counts arise beyond P-r19-1a's single ratio. All other numbers are measured rates, f-sums and S.

---

## 9. Rules checklist (rounds 17–19) and scope

- **v_max.**
  - βU = 0: flat bands, so the whole-zone group velocity is 0 (exact).
  - βU > 0: no dispersion law is proposed. The H terms have norm ≤ 2t·cosh(6βU), so the Lieb–Robinson velocity is ≤ C·t·cosh(6βU) (suggested; constant not computed).
  - No gauge-field symbol is used.
- **Counting:** see §8. **Λ:** not applicable.
- **Locality of vertices / vertex conservation:** no TT or stress vertex is used.
- **Bounded classes for spectra:**
  - "gapped" is used only at βU = 0, where the whole generator has a uniform gap ≥ 2t, continua included;
  - the SMA and RR values are upper bounds, never called gaps.
- **Certificates:** no CONFLICT is claimed.
- **Equilibration stated in advance:** METHOD (b). Applied mechanically, with failures reported (§4).
- **Same-component controls:** βU = 0 exact solution, same estimator, component and normalization. No Z₂ positive control for a light-like branch exists.
- **Off-axis checks:** face and body are in every table.
- **Thresholds recomputed:**
  - Lemma 3's bound is an exact symbolic expression (e^{−18βU} and μ_min);
  - the N_type counts 4 and 6 are exact (`s1`);
  - the edges touched per move, 12, are exact (`s3b`, which corrects `s3`).
- **Invariance:** the RK ground state is shift-action invariant (§1).
- **Literal first:** R18-1's ensemble and moves as written. The dipole-conserving variant is reported as outside the setting and priced (P143).
- **Exhaustive forks:** the registered four-way reading, and Proposition 4's fork with its NEITHER branch.
- **Readout bridge:** X-basis labels plus the RK bridge.
- **Changed hypothesis:** statics removed (§1).
- **Generic GR:** not applicable.

**Strong words.** "Exactly" is used only for algebraic identities (Lemmas 1 and 2, f₀ = 0 under P143) and the L = 2 enumeration. "Proved" means unrefereed.

**Not covered.**
- Exact many-body branches at βU > 0 outside (Iso), and (R2) at βU > 0.
- A uniform gap at βU > 0.
- βU > 3.5.
- L > 8 for the f-sum.
- Non-trivial coset sectors.
- The t ≠ v phase beyond O(δv), where the O(δv) statement is itself only suggested.
- Any identification of the readout with geometry.

## Files (`S/`)

- `METHOD_preregistered.md`.
- `scripts/`:
  - `common.py`, `mc.py` (copied from R18-1);
  - `fsum.py` (the f-sum estimator), `run_fs.py`, `an_fs.py`;
  - `s1_ed_L2.{py,out}` (exact RK Hamiltonian at L = 2);
  - `s2_check_L2.{py,out}` (estimator check);
  - `s3_f0_positivity.{py,out}` (Lemma 3 ingredients; its last line is superseded by `s3b_edges_touched.{py,out}`);
  - `s4_summary.{py,out}` (equilibration criterion plus the full SMA table);
  - `s5_rayleigh_ritz.{py,out}` (six-mode RR; it uses seeds 1–2 at every βU, so its L = 6, βU = 3 rows are from a not-accepted point and are informational only);
  - `s6_dyn_autocorr.py`, `s6_dyn_L6_b2.out`, `s6_dyn_L8_b1.out`, `s6_dyn_L8_b2.out` (Metropolis-generator autocorrelations, §4b);
  - `runall*.log`, `jobs*.txt`.
- `data/`: pickled S and f matrices per run (`fs_L*_b*_s*.pkl`), plus `test_L6_b0.pkl`.
