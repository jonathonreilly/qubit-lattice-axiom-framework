# C5 R9-3 report: the Sokolov-packed three-body box law in d = 1

**Author and provenance.** Written by a Claude Opus 5.5 probe. It is the same model family as the supervisor and as the R7-6 and R8-1 workers. It has not been refereed. It ran on 2026-10-12 from 16:43Z to about 17:30Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R9-3/`. The scripts and outputs are in `S/scripts/`.
- `r93_packing_cluster.py` is the main runner. It applies the packing operators B_a, B_b and B_c to states in which one cluster has been moved away.
  - `r93_packing_cluster_v1.py` is the first version. It produced the files with no suffix, plus `_centre`, `_try` and `_sanity`.
- `r93_fit.py` with `r93_fit.out` runs the pre-registered model comparison.
- `r93_ff_proxy.{py,out}` computes the Fourier-tail proxy of form factor × packet for the smoothness family s = 0.5, 1, 2 and the analytic g.
- The `*.out` files hold the results, one per run. Each `log_R*.txt` copies the console output of the matching run.
- `r93_conv_check_ppo24_hfac0.015.out` is the convergence check.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`:
  - :2302-2440 (the C5 method and round 1);
  - :3240-3260 and :3373-3575 (rounds 7 and 8, with their referee results);
  - :3575-3811 (round 9, plus the round-8 referee results with the dated ½-prefactor correction).
- In full: `agents/C5_R7-6_report.md`, `C5_R7-6_referee_verdict.md`, `C5_R8-1_report.md` and `C5_R8-1_referee_verdict.md`.
- `C5_S8_synthesis.md`, from the grep hits and :270-320.
- `SUMMARY.md` §§21-23.
- `C5_R7-1_referee_verdict.md`:125-137 (Lemma Sm).
- The scripts `scripts/C5/R7-6/r76_threebody_naive.py` and `r76_packing_range.{py,out}`, and `scripts/C5/R8-1/r81_common.py`.

**Prior-art grep.** I searched `docs/` and `.claude/science/` for "Sokolov", "packing operator", "cluster separab" and "Bakamjian". The only hits were R7-1, R7-6, the R7-6 referee verdict, S8 and TESTS. Each counts once.

**Labels.**
- **proved:** argued here in full.
- **checked:** numerics run here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** someone else's result, used for comparison.
- **RECALLED:** taken from memory, not verified.
- **VERIFIED-CITE:** the abstract or record was fetched on the web this session; the content was not re-derived.

**Normalisation.** The ½ quartic prefactor is correct (dated correction, `TESTS.md:3796-3798`). The pair law here uses R7-6's normalisation (`r76_packing_range.py:45`): M = M₀ + λ dq g gᵀ, with m = 0.3, κ = 0.25 and λ = −3. It reproduces the dimer M_b = 0.51527993 (R7-6: 0.5152799267).

---

## 0. In plain words

1. **The cure's key step works numerically, but slowly (checked; d = 1; no threshold power law seen).**
   - For Sokolov's construction to work, the packing operator of a pair must switch off when that pair is pulled apart. The case that matters is the cluster limit: a third particle receding from a pair, which leaves its *spectator* far away as well. R7-6 tested the spectator only at the pair's centre.
   - Here the receding geometry is computed, for the operators B_b (pair 23) and B_c (pair 31). Their effect falls from 6e-4–1e-3 at separation D = 80 to 3e-8 at D = 640.
   - The fall gets steeper with distance. Over the whole range a super-polynomial law beats a power law clearly (ΔAICc = +25), though the small-D part of that range is set by the test packets. On the operator-only part of the range, the longest run fits exp(−0.52 D^0.53). That matches the exp(−0.5√D) expected from the smoothness of the form factor at its support edge.
   - Replacing the smooth step with an analytic form factor makes the fall reach the 4e-11 numerical floor by D = 160, where the step-shaped one is still at 1e-4. So the tail is set by the form factor, not by a threshold singularity.
   - **Main new evidence: the tail tracks the form factor's Fourier tail (checked).**
     - I varied the smoothness class of the step (exp(−1/x^s), s = 0.5, 1, 2).
     - The measured fall tracks the Fourier tail of form factor × packet in every case. The local log-slopes agree to within 0.4 on the intervals from D = 320 onward, and within 0.7 from D = 226 onward (320→453: s = 1, 5.9 against 6.0; s = 2, 8.0 against 7.7; s = 0.5, 2.4 against 2.6).
     - The Fourier transform of a smooth compactly supported function falls faster than any power (standard). So the fall is super-polynomial, with the form factor's own rate (suggested, strongly supported).
   - **Caveat on the registered test.** For s = 0.5, which is equally smooth and compactly supported, the pre-registered AICc test prefers a power law (p ≈ 2.7) over 80–640, and so does its exactly super-polynomial Fourier proxy. On reachable ranges the registered test cannot tell slow super-polynomial classes from power laws.
2. **The packing unitary and H_S − H_BT do not fall off, and cannot (proved, given one Lemma-Sm limit; checked).**
   - The packing unitary of the cluster that stays together keeps acting at any distance. Its effect is 0.26–0.43 at D = 80–320, against a maximum possible of 0.67.
   - The non-separability of BT's Hamiltonian shows up as ‖[B_a, H_a]ψ_D‖. It grows from 2.4e-3 at D = 10 to 3.0e-2 at D = 320.
   - So any cluster-separable packed law must differ from the BT law by an amount that does not decay. Probe (d)'s "H_S − H_BT super-polynomial" therefore cannot hold together with (c). The PASS clause, as registered, cannot be met.
3. **The algebra and the trimer mass are exact by construction (proved); the full H_S was not assembled.**
   - H_S = B†H_BT B is a unitary conjugate of the BT law by a B that commutes with P. So the algebra closes exactly, and the trimer's invariant mass is exactly the same at every P: it equals the P = 0 pair-sum trimer, 0.734266 at L = 300.
   - H_S and K_S were **not** built as numerical lattice operators.
   - On a finite ring the BT and packed three-body laws are not ring-grid operators at P ≠ 0 (proved, §3.4). So "(b) on three ring sizes" needs an interpolation prescription that is not in the registration.
4. **Reading: INCONCLUSIVE.**
   - PASS is not met. (b) was not run. (c) was measured on the packing differences that control separability, not on the assembled H_S and K_S. (d) cannot be met, by point 2.
   - FAIL is not met. The connected term itself was not computed. The packing differences that control it track a super-polynomial Fourier tail, and no power law is proved.
   - The FAIL clause's literal "the packing unitary has … slower tails" *is* true in the spectator direction. But every Sokolov packing has that property, the continuum one included, so I flag it as a registration issue for the referee rather than claim FAIL (§6).

---

## 1. Hypotheses and class (stated before titles)

- **H-lat, H-box, H-P.** These are as in R7-6 (`C5_R7-6_report.md:66-73`):
  - graded CAR (one complex fermion per site of Z, continuous time);
  - a frame-fixed momentum box;
  - P = Q. This is an added bridge, not axiom content (`C5_R7-6_referee_verdict.md:85-91`).
- **H-L3.** The box sector of the lattice law equals the continuum fibre at fixed P. This is R7-6 Lemma L3, which the referee found "correct but conditional" (`C5_R7-6_referee_verdict.md:71-79`). All numerics here run on the continuum fibre at fixed total P, as R7-6's script 4 did. They are box-sector statements only through H-L3.
- **H-pair.** The pair law is R7-6's d = 1 fermion pair law:
  - g(q) = (q/κ)·sstep(1 − q²/κ²), which is odd, C^∞, compactly supported and Gevrey-2;
  - m = 0.3, κ = 0.25, λ = −3;
  - R8-1's d = 1 law has the same structure (`r81_common.py:58-59`); its parameters (m = 0.5, κ = 0.4) were not run.
  - The plateau is c(P_ij) = 1 wherever it is used.
- **Test states.** Lab product Gaussians at fixed P:
  - particle 2 at 0, particle 3 at D, particle 1 at y;
  - y = 0 gives the 2+1 cluster limit (3 recedes from the 12 pair);
  - centres k = (0.10, 0.15, 0.15) unless stated, widths σ_k = 0.05 or 0.10.
- **Excluded realizations (not addressed):**
  - d ≥ 2; pair creation; gravity;
  - N ≥ 4 (the tower of four-body and higher terms);
  - the ⊗M₂ ungraded composition;
  - a K-residual computation (§4.3);
  - R8-1's parameter set;
  - any interpolated ring version of H_S.

## 2. Prior art (each counted once)

- **R7-6** (`TESTS:3506-3510`; `C5_R7-6_report.md:206-267`): BT0 (M_BT = H_pair|_{P=0}), Construction S, and the T-risk.
- **R7-6 referee** (`C5_R7-6_referee_verdict.md:93-137`):
  - B_a = 1 at P = 0 is confirmed;
  - B_a is long-range in the spectator coordinate;
  - over 40–320 a power law fits better than exp(−0.8√r) for one packet;
  - the full Sokolov claim is open.
- **R7-1 Lemma Sm** (`C5_R7-1_referee_verdict.md:131-137`): √(M²+P²) − √(M₀²+P²) has a smooth kernel with faster-than-power decay.
- **R8-1 referee identity** (`C5_R8-1_referee_verdict.md:25-30`): f(M) − f(M₀) = Q_G[f(M) − f(M₀)]Q_G. It is used and extended in §3.3.
- **Literature (VERIFIED-CITE).**
  - Keister–Polyzou, arXiv:1109.6575 (abstract): BT "is known formally to fail the constraint of cluster separability" for N ≥ 3. A recursive unitary construction restores it, but is "difficult in practice".
  - Polyzou–Keister, arXiv:1110.1367 (abstract): Sokolov's recursive method restores cluster properties "at significant computational expense".
  - Polyzou, nucl-th/0201013 (text, first 100k characters):
    - cluster properties are stated as strong limits ‖(U − ⊗U_a)T_a χ‖ → 0, for "sufficiently short-range interactions";
    - **no decay rate or quasi-locality bound is given**.

    So the continuum theorems do not settle R9-3's rate question.
  - Coester–Polyzou, Phys. Rev. D 26, 1348 (1982), via the Iowa repository record: an explicit N-body construction with cluster separability; the N-body strength decreases rapidly with N.
  - Sokolov (1977): RECALLED, cited as in R7-6.

---

## 3. Construction (a): explicit formulas, built here; not assembled as a lattice operator

### 3.1 The pieces in the free rest-frame chart (proved, elementary; 1+1, no spin)

**Free chart.** At total P the free chart is (P, p₁, p₂), with p₃ = −p₁ − p₂ the rest-frame momenta. X₀ = i∂_P at fixed p. Λ_P is the free-boost change of variables to lab momenta.

**Cluster a = (12)(3).** Take H_a = H₁₂ + ε₃, where H₁₂ is R7-1/R8-1's two-body BT law, and let M_a = (H_a² − P²)^{1/2}. In the free chart:
- M_(a) := B_a M_a B_a† = √(M₁₂² + p₃²) + √(m² + p₃²);
- M₁₂ = M₀₁₂(q₁₂) + λ|g⟩⟨g| acts on q₁₂ at fixed p₃.

Reason: B_a = R₀†R_M identifies the spectator rest-frame momentum computed with cluster mass M₁₂ (the a-system) with the one computed with M₀₁₂ (the free chart). This is R7-6's identification (`C5_R7-6_report.md:259`).

**BT law.**
- M_BT = M₀ + Σ_a (M_(a) − M₀).
- Since p_k = −P_ij at P = 0, this equals R7-6's pair-sum H_pair at P = 0, on the ring's own grid. That is BT0 re-derived.
- H_BT(P) = Λ_P √(M_BT² + P²) Λ_P†, and K_BT = ½{H_BT, X₀}.

### 3.2 The Sokolov packing (proved as a construction; the choice of symmetric B is free)

Any unitary B with three properties works:
- (i) [B, P] = 0 and B commutes with particle permutations;
- (ii) B → B_a whenever B_b, B_c → 1;
- (iii) B → 1 when all three → 1.

Two explicit choices:
- **(S1)** B = exp(i Σ_a G_a), with G_a = −i Log B_a. This needs −1 ∉ spec B_a (suggested).
- **(S2)** The polar part B = A(A†A)^{−1/2} of the symmetric mean A = (1/6) Σ_π B_{π(a)} B_{π(b)} B_{π(c)}. It is unitary and permutation-symmetric wherever A is invertible (proved). It satisfies (ii) because each ordered product tends strongly to B_a (suggested: this needs strong limits of products and uniform invertibility of A).

**The packed law.** H_S = B†H_BT B, K_S = B†K_BT B, P_S = P.

**Status.** These are explicit formulas. They were **not assembled** as numerical operators on a three-body grid. The cost is 2D functional calculus of M_BT, plus the 2D chart changes for B_b and B_c.

### 3.3 Exact reduction used in every run (proved)

Write B_b = R₀†R_M, with:
- R_M = Σ_n |χ_n⟩⟨χ_n| ⊗ R_{μ_n} (spectral resolution of M₂₃);
- R₀ = Σ_j |q_j⟩⟨q_j| ⊗ R_{M₀(q_j)};
- R_μ: k₁ ↦ q₁(P, k₁; μ), the spectator rest-frame momentum.

Then B_b − 1 = R₀†[F(M) − F(M₀)], where F(μ) = R_μ is operator-valued.

The two reducing subspaces are G = L²(supp g)_odd ⊗ L²(k₁) and its complement. M and M₀ agree on the complement. So their spectral measures agree there, which gives F(M) − F(M₀) = (Q_G ⊗ 1)[F(M) − F(M₀)](Q_G ⊗ 1). That is the R8-1 referee's identity extended to operator-valued F.

Hence B_b − 1 = (B_b − 1)(Q_G^odd ⊗ 1) exactly. The runner therefore diagonalises M only on the odd sector of (0, κ). This is the step that makes D up to 640 affordable.

### 3.4 Ring non-representability at P ≠ 0 (proved, short)

- The pair-(12) part of M_BT preserves p₃ and changes q₁₂.
- In lab variables at fixed P ≠ 0, k₃ = m sinh(asinh(p₃/m) + Θ₀), with tanh Θ₀ = P/√(M₀² + P²) and M₀ = √(M₀₁₂(q₁₂)² + p₃²) + ε(p₃).
- Changing q₁₂ therefore moves k₃ by a continuous, non-constant amount.
- So the kernel of H_BT(P) − H_pair(P), and of H_S, connects k₃ to off-grid k₃′.
- A finite ring carries the BT and packed laws only through an interpolation prescription. On the infinite lattice, with continuous momentum, H-L3 applies.

This is why R7-6 found the check needed off-grid interpolation (`C5_R7-6_report.md:267`). The registered "(b) on rings of three sizes" is therefore not well-posed without a stated prescription (reading).

---

## 4. Results

### 4.1 (b) Algebra: proved by conjugation; not run on rings

- H_S and K_S are B†(·)B of H_BT and K_BT, with [B, P] = 0.
- So [K_S, P] = B†[K_BT, P]B = iH_S, [K_S, H_S] = iP and [H_S, P] = 0 hold on B†𝒟. This is proved, given the BT algebra (`C5_R7-6_referee_verdict.md:95-102`, confirmed) and the domain invariance of B. That invariance is suggested only (R7-6 Lemma R, `C5_R7-6_report.md:148-150`).
- No ring residuals were computed (§3.4).

### 4.2 (e) Trimer invariant mass: proved exactly P-independent; lattice check only at P = 0 (comparator)

- For any packed law, spec H_S(P) = spec H_BT(P) = spec √(M_BT² + P²). So the trimer mass is the bottom of spec M_BT at **every** P (proved). The drift is identically zero.
- By §3.1, M_BT is H_pair at P = 0. Its ring trimer is 0.734256054, 0.734265439 and 0.734266071 at L = 180, 240 and 300 (comparator, `scripts/C5/R7-6/r76_threebody_naive_fermi_lam-3.0_kap0.25.out:28`, as cited at `C5_R7-6_referee_verdict.md:16-22`).
- No lattice computation at ±P₁ or ±P₂ was run, because H_S was not assembled.

### 4.3 (c) Cluster separability: the packing differences on 2+1 cluster states (checked)

**What was measured.** ‖(B_b − 1)ψ_D‖/‖ψ‖ (pair 23, spectator 1) and ‖(B_c − 1)ψ_D‖ (pair 31, spectator 2), with particle 3 translated by D away from particles 1 and 2.

**Why these quantities.** These are the operators that Sokolov's B must turn off in the a-limit. To first order (suggested), H_S − H_a = Δ†H_a + H_aΔ + B_a†E B_a + O(Δ², ΔE), where:
- Δ = B_a†B − 1 is controlled by G_b and G_c (and BCH commutators with G_a) acting on 2+1 states;
- E = √(M_BT² + P²) − √(M_(a)² + P²) is a Lemma-Sm-type pair term for b and c.

So the H_S cluster residual inherits the decay of the quantities below, plus Lemma Sm's. The H_S and K_S residuals themselves were **not** computed. The K residual is expected to carry an extra factor of order D, from the X₀ terms (suggested).

**Numerical checks:**
- **P = 0 sanity.** B = 1, residual 2e-11 (`r93_packing_cluster_b_2+1_P0.00_comm_P0sanity.out`).
- **Convergence.** Raising the points per q-oscillation from 14 to 24 and halving the spectator step leaves D = 80–226 unchanged to 5 digits (`r93_conv_check_ppo24_hfac0.015.out` against `log_R1.txt`).
- **Floor.** About 4e-11 at the hfac = 0.03 used (from the analytic-form-factor run).

**Data (P = 0.4 unless stated; ‖ψ‖-normalised; the odd-G weight of ψ is 0.707):**

| D | B_b, σ_k = 0.10 (R1) | B_b, P = 0.6 (R4) | B_c (R5) | B_b, pair approaching (R6) | B_b, receding (R7) | B_b, σ_k = 0.05 (R10) | B_b, analytic g (R3) |
|---|---|---|---|---|---|---|---|
| 80 | 5.65e-4 | 9.96e-4 | 9.93e-4 | 2.54e-3 | 3.50e-3 | 5.53e-4 | 4.29e-4 |
| 113 | 2.49e-4 | 2.27e-4 | 3.91e-4 | 1.59e-3 | 1.51e-3 | 1.46e-5 | 1.99e-7 |
| 160 | 9.64e-5 | 5.53e-5 | 1.36e-4 | 4.88e-4 | 4.24e-4 | 5.14e-6 | 3.6e-11 (floor) |
| 226 | 1.80e-5 | 9.75e-6 | 2.08e-5 | 1.10e-4 | 6.71e-5 | 1.84e-7 | floor |
| 320 | 2.12e-6 | 1.26e-6 | 2.12e-6 | 1.49e-5 | 6.41e-6 | 5.55e-9 | floor |
| 453 | 2.75e-7 | 2.05e-7 | — | — | — | 6.1e-11 (≈ floor) | — |
| 640 | 2.96e-8 | — | — | — | — | — | — |

- For D ≤ 57 the values (0.01–0.1) are dominated by the overlap of the Gaussian packets. The test packet's pair-relative amplitude ∝ exp(−σ_k² r²/2) reaches 1e-11 at r ≈ 70 for σ_k = 0.1.
- **Comparator geometry** (R7-6's (A), spectator at the pair centre, σ_k = 0.05, older grid; `r93_packing_cluster_b_centre_P0.40.out`): 1.6e-4, 9.0e-7, 7.8e-10 and 2.1e-12 at D = 80, 160, 320 and 640.

**Pre-registered model comparison** (`r93_fit.out`). AICc on ln residuals; the super-polynomial model is a − c·D^β with β profiled; the power model is a − p·ln D.

| series | full range (as registered): ΔAICc(power − super) | operator range D ≥ 80: ΔAICc | fitted super-poly, D ≥ 80 |
|---|---|---|---|
| R1, 13 pts to 640 | **+25.3** (super) | **+8.4** (super) | c = 0.52, β = 0.53 |
| R4, P = 0.6 | +17.7 (super) | +1.0 | — |
| R5, B_c | +12.8 (super) | −1.2 | — |
| R6, approaching | 0.0 | −4.0 (power, p = 3.7) | — |
| R7, receding | +8.9 (super) | +3.5 | — |
| R10, σ_k = 0.05 | −10.0 (power, p = 8.0; ragged: dip at 113) | −19.0 | — |
| R3, analytic g | +14.7 (super) | n/a (floor) | — |
| R11, smoothness s = 2 | +38.9 (super) | +23.9 (super) | c = 1.3e-3, β = 1.42 |
| R12, smoothness s = 0.5 | +0.6 | −8.7 (power, p = 2.67) | — |

- **The "full range" result is driven partly by the packets.** It includes the Gaussian packet-overlap regime, which is super-polynomial because of the test state, not the operator. I report it as registered, but it is not decisive on its own.
- **On the operator-dominated range the evidence is mixed by count (3–3).** It is decisive only in the longest series (R1, 0.9 decades, 7 points), where it gives exp(−0.52 D^0.53).
- **Local log-slopes rise in most sstep series (R10 is ragged):**
  - R1: 2.4, 2.7, 4.9, 6.2, 5.9, 6.5;
  - R7: 2.4, 3.7, 5.3, 6.8;
  - R6: 1.4, 3.4, 4.3, 5.8.

  A rising slope is the super-polynomial signature, but over less than one decade it cannot exclude a power p ≳ 6.

**Expected law (suggested).** The edge of the form factor behaves as g ≈ exp(−κ/(2u)) with u = κ − q. Its Fourier transform at distance r, by saddle point, is ~ exp(−√(κ r)). For κ = 0.25 that is exp(−0.5√r), with local slope about 0.25√D: 2.2 at D = 80, 4.5 at 320 and 6.3 at 640. R1's fitted exp(−0.52 D^0.53) agrees with this (suggested agreement, one series).

**Threshold diagnostic (checked).**
- Both form factors vanish linearly at the q = 0 threshold.
- With the analytic g, B_b − 1 falls to the 4e-11 floor by D = 160, against 9.6e-5 for sstep.
- So no form-factor-independent (threshold) tail exists above 4e-11 at D ≥ 160 for this state.
- Read this as a bound on the size of any threshold term, not as a theorem.

**Gevrey-family test (checked; `r93_packing_cluster_b_2+1_P0.40_gs{0.5,2}.out`, `r93_ff_proxy.{py,out}`).**
- **Setup.**
  - g_s(q) = (q/κ)·sstep_s(1 − q²/κ²), with sstep_s built from exp(−1/x^s). s = 1 is the law; s = 0.5 and s = 2 were added.
  - λ was retuned to the same dimer mass. A check run with s = 1 and λ fixed by `mb` reproduces R1 to 5 digits (`log_R13.txt`).
  - The proxy is F_s(r) = |∫₀^κ g_s(q) e^{−q²/(2·0.07²)} sin(qr) dq|, enveloped over r ∈ [D, 1.2D].
  - Every F_s falls faster than any power, by the standard Fourier bound for C_c^∞ functions (proved, standard). For example, F_1 reaches 2e-19 by D = 5120, and F_0.5 reaches 3e-12.
- **Local log-slopes between consecutive D in 80…640:**

| s | data ‖(B_b − 1)ψ_D‖ | proxy F_s(D) |
|---|---|---|
| 0.5 | 3.6, 2.0, 2.4, 3.1, 2.4, 2.9 | 7.5, 2.9, 4.2, 3.0, 2.6, 3.3 |
| 1 (law) | 2.4, 2.7, 4.9, 6.2, 5.9, 6.5 | 4.4, 6.5, 5.2, 5.7, 6.0, 6.7 |
| 2 | 1.1, 1.8, 3.1, 5.5, 8.0 | 1.6, 2.1, 3.9, 4.8, 7.7 |

- **The ordering matches.** At D ≤ 320, s = 2 is slowest, because its transition is sharper. The order flips at large D: at D = 453 in the data, and between 453 and 640 in the proxy. On the intervals from D = 320 onward the slopes agree to within 0.4; from D = 226 onward, within 0.7.
- **Reading (suggested, strongly supported).** In the 2+1 cluster limit, the packing difference's tail is the Fourier tail of form factor × packet. It is therefore faster than any power for every C^∞ compact form factor, at that form factor's own rate.
- **Registered AICc on the s = 0.5 series (D ≥ 80):** power preferred, ΔAICc = −8.7, p = 2.67. The registered comparison therefore *misclassifies* a member of the "smooth plateau, box-supported" class whose proxy is super-polynomial exactly. It is not a valid discriminator on 0.9-decade ranges.

**Kinematic heuristic (suggested).**
- Why no non-decaying stationary-phase piece appears: the packing difference's μ-sensitivity acts like an internal time of order D·ε₁Pμ/(M²E₂₃).
- The receding pair needs a time of order D/v_rel ≥ D/2 to meet.
- The ratio is ≲ P/M < 1 inside the box budget.
- So no stationary point exists, and the decay is set by the smoothness of g. Not proved; the boosted regime P ≳ M is untested.

### 4.4 (d) Tails of the packing unitary and of H_S − H_BT (checked; proved non-decaying in one direction)

- **Pair-separation direction.** As in §4.3: super-polynomial in the best series, mixed by AICc on short series.
- **Spectator direction.** The pair stays together while the spectator recedes (`r93_packing_cluster_a_2+1_P0.40_comm.out`). ‖(B_a − 1)ψ_D‖ = 0.059, 0.087, 0.153, 0.278, 0.426 and 0.260 at D = 10, 20, 40, 80, 160 and 320 (checked). The upper bound is 2 × 0.333, the odd-G weight. This confirms R7-6's (B) (`C5_R7-6_referee_verdict.md:109-117`).
- **Any Sokolov B inherits this (proved).** By (ii), B → B_a in the a-limit. So B − 1 does not decay in the spectator direction for any choice of B.
- **BT's cluster defect (checked).** ‖[B_a, H_a]ψ_D‖ = 2.4e-3, 3.2e-3, 5.4e-3, 1.0e-2, 1.9e-2 and 3.0e-2 at D = 10–320. It grows roughly in proportion to D: a dilation-type term.
- **Consequence (proved, given that M_BT − M_(a) → 0 on these states, a Lemma-Sm-type limit, suggested).**
  - In the a-limit, H_BT → B_aH_aB_a†.
  - If H_S → H_a (cluster separability), then ‖(H_S − H_BT)B_aψ_D‖ → ‖[H_a, B_a]ψ_D‖. That does not decay; it grows.
  - So (d)'s "H_S − H_BT super-polynomial" contradicts (c). It is unattainable for **every** cluster-separable packed law, the continuum included.

---

## 5. What fails or stays open

1. **H_S and K_S as assembled numerical operators.**
   - Not built: they require 2D functional calculus of M_BT and 2D chart changes for B_b and B_c.
   - The cheapest next step is the first-order formula of §4.3 on 2+1 states, then the full (S2) packing on a P-fibre grid at about 200² internal points.
2. **Ring versions.** These need an interpolation prescription (§3.4). The registration should name one, or run on the continuous-momentum lattice through H-L3.
3. **Tail law.**
   - It is checked that the tail tracks the form factor's Fourier tail at three smoothness classes (§4.3).
   - It is not proved for the operator. A proof would bound B_b − 1 on 2+1 states by the form factor's Fourier tail, through a non-stationary-phase lemma using the kinematic ratio ≲ P/M < 1.
   - The registered AICc test cannot certify the class on 0.9-decade ranges (the s = 0.5 counterexample).
4. **K residual.** Not computed.
5. **N ≥ 4.** The tower of terms is open, as stated in R7-6.

## 6. Reading against the FIXED readings (`TESTS.md:3700-3702`)

- **PASS: not met.**
  - (b) was not run on rings, and §3.4 shows it needs a prescription.
  - (c) was computed for the packing differences that govern separability, not for the assembled H_S and K_S. The full-range comparison favours super-polynomial; the operator range is mixed.
  - (d) cannot be met in its H_S − H_BT part by any cluster-separable law (§4.4, proved given the Lemma-Sm-type limit).
  - (e) is proved exact, but the lattice check covers P = 0 only.
- **FAIL: not met as a power-law no-go.**
  - No power-law tail of the connected term is proved. The best data favour exp(−0.52 D^0.53). The analytic-g contrast bounds any threshold term below 4e-11 at D ≥ 160.
  - **Registration issue for the referee.** The clause "the packing unitary has power-law or slower tails" is literally true in the spectator direction: proved for every Sokolov B, and checked. But that is the defining property of a packing operator (B → B_a), shared by the continuum construction that Sokolov's theorem validates. Read literally, the clause would turn a structural feature into a FAIL. I read the intended object as the connected term and the cluster residual, and do not claim FAIL. If the referee reads it literally, the reading becomes FAIL on a criterion that does not discriminate.
- **INCONCLUSIVE: the worker reading.** The expectation (`TESTS.md:3703`) is met.
- **The bounded positive result to record (checked, d = 1, one law, H-L3).** In the true 2+1 cluster geometry, the packing operators that Sokolov's construction needs to switch off do so:
  - from 1e-3 at D = 80 to 3e-8 at D = 640;
  - with a fit of exp(−0.52 D^0.53) (ΔAICc = +8.4 against a power law).

  At three smoothness classes the fall tracks the Fourier tail of form factor × packet, to within 0.4 in local slope from D = 320 onward (within 0.7 from D = 226). That tail falls faster than any power for every C^∞ compact form factor.

  This sharpens the R7-6 referee's 40–320 power-law preference (`C5_R7-6_referee_verdict.md:125-128`). That preference is what a slow super-polynomial Fourier tail looks like over one decade, and the s = 0.5 run reproduces the effect. It is a component result, not a check of H_S.
- **Registration issue 2.** The pre-registered AICc test misclassifies a C^∞ compact form factor (s = 0.5) as power law on reachable ranges (§4.3). A future registration should test the form-factor class through a family comparison (as in §4.3) rather than by AICc over one decade.

## 7. Strong-word check

- **"Exact" (algebra, trimer mass)** means unitary conjugation identities on B†𝒟. Domain invariance of B is suggested only.
- **"Super-polynomial"** is a model-comparison statement over D ≤ 640, at most 0.9 decades in the operator-dominated range. It is not a proved bound.
- **"Checked"** covers B_b − 1, B_c − 1, B_a − 1 and [B_a, H_a] on Gaussian 2+1 states at P = 0.4 and 0.6, for one pair law. It does not cover H_S, K_S, rings, R8-1's parameters, or high boosts.
- **"Unattainable (d)"** rests on two things: BT's checked non-separability ([B_a, H_a] growing), and the suggested Lemma-Sm limit M_BT − M_(a) → 0 on 2+1 states.
- **Nothing here** bears on gravity, Ward identities, pair creation or d ≥ 2.

## 8. Price (named, not adopted)

- Unchanged from R7-6 §8 (`C5_R7-6_report.md:318-329`):
  - a tower of connected many-body terms;
  - instant form forced by H-P;
  - R7-1's prices.
- **Added detail (suggested):**
  - The connected terms decay only as fast as the form factor's Fourier tail. For C^∞ compact (Gevrey-2) form factors that is exp(−c√D) with c ~ √κ (lattice units).
  - Inside the box law, the packing unitary is non-local in the spectator direction by construction.
- No axiom text changes. Admissibility does not fix dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-125`).

## 9. For the referee

1. Check §3.3's extension of the R8-1 identity to operator-valued F, and the P = 0 sanity run (2e-11).
2. Rerun `python3 r93_packing_cluster.py P=0.4 sk=0.1 hfac=0.03 Ds=80,160,320`. It takes about 1 min with OMP_NUM_THREADS=2. Confirm 5.65e-4, 9.64e-5 and 2.12e-6.
3. Rule on §6's registration issue: the literal "packing unitary" clause, and the unattainable (d) for H_S − H_BT.
4. Run `r93_fit.py` with other floor and D_min choices.
