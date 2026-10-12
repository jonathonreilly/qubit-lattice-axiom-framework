# C5 R3-3: LRL propagation, lensing and curved spacetime

**Worker.** Claude Opus 5.5 (probe R3-3), the same model family as R2-2, O1–O5 and the supervisor. **Not refereed.** Run 2026-10-12, 12:27Z to 12:58Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R3-3/`:
- `r33_A_L7_layers.py` → `r33_A_R150.out`, `r33_A_R300.out` (mean layer and link kernels of L₇-LRL);
- `r33_D_perrealization_links.py` → `r33_D_perrealization_links.out` (one realization against the ensemble mean);
- `r33_E_inband_split.py` → `r33_E_inband_split.out` (smooth versus lattice-scale part of that difference);
- `r33_B_dS_points.py` → `r33_B_dS_points.out` (an exact LRL on de Sitter);
- `r33_C_defect_noise.py` → `r33_C_defect_noise.out` (curvature carried by defects: noise estimates);
- this report.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5", the round-1 results, round 2 and round 3 (`TESTS.md:2302-2704`; R3-3 at `:2685-2694`); `C5_O5_synthesis.md` §§F6, 2.0–2.1; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §§1–2, §5 and the v6 wrap-up; `C4_RL2_report.md` and `C4_RL2_referee.md`; `C3_G-L_referee.md` (the report itself only in part); `RZ_referee.md`; `scratchpad/C5/R2-2/R2-2_report.md`; the **R2-2 referee**, which finished during this run (`scratchpad/C5/ref_R2-2/REFEREE_VERDICT.md`, `R2-2_referee.md`: CONFIRMED WITH CORRECTIONS).

**Labels.**
- *proved*: a complete argument written here (same family, unrefereed).
- *checked*: a numerical check in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator*: an outside result used for comparison.
- *RECALLED*: a literature fact from memory, not re-derived here.

**Conditionality.** The R2-2 referee confirms LRL's basic claims: invariance in law, cocompactness, the Bragg gap |G²| ≥ (2π)²/7, and exact ideal 1→1 Bloch silence in band. It **narrows** the claim of in-band silence "at all orders". Covariance alone does not give linear dynamics, convergent orbit sums, or control of "forward-dispersion", defect and curvature effects (`ref_R2-2/R2-2_referee.md:166-189`). Nothing below is conditional on a rejected claim. §2.6 measures one of the forward effects the referee left open.

---

## 0. In plain words

- **In flat spacetime, the average one-hop kernel is right.**
  - On the Lorentz-random lattice (LRL), every pair of neighbours ("links") is separated by a proper time² of 1 to 7 lattice units.
  - The average link kernel is therefore a sum of seven thin hyperbolic shells. At long range it is exactly the massless retarded kernel, with corrections of relative size (a/r)², as for random sprinkling (checked).
- **The Poisson machinery does not carry over.**
  - Poisson's d'Alembertian weights (BD) give the wrong average on LRL: the 1/k² term survives (checked).
  - RL2's proof that the average propagator focuses like GR (√Δ) used a property only Poisson has: given one point, the others are still independent. On LRL, one point fixes the whole crystal (proved).
  - So RL2's √Δ result does not transfer. LRL would need its own weights and its own argument.
- **One realization is not the average.**
  - In a single realization, the one-hop link sum of a smooth source differs from the ensemble average by about 30–40% of Poisson's random scatter, with the same fall-off with distance (checked).
  - That difference is smooth (in band). It changes with the realization's frame.
  - It is a deterministic anisotropy, not noise, and at physical scales it is tiny for one hop. Whether it builds up along propagators is the open "forward-dispersion" question that the R2-2 referee flagged.
- **GR focusing could come from the effective law, not from the average.**
  - Suppose the long-wavelength law in each realization is a symmetric (action-derived) second-order operator, and its point density equals its metric's volume. Then the operator is exactly □_g + V, and its Green function carries GR's √Δ focusing in each realization, not just on average (proved, given the effective law).
  - Whether that effective law exists is R3-1's question.
  - The curved test geometries used for Poisson (plane waves, conformal lenses) have no exact LRL. So the focusing cannot yet be checked directly.
- **Curved spacetime.**
  - **(i) Exact on de Sitter.** An exact curved LRL exists for de Sitter (and anti-de Sitter) space: the integer points on a large hyperboloid, given a random Haar frame (proved from standard theorems, checked).
    - But de Sitter light rays do not focus (Δ = 1), so it cannot test lensing.
    - With integer coefficients it also has light-like separated pairs (checked). Avoiding them needs a form over ℤ[√2].
  - **(ii) Generic curvature.** For curvature with no symmetry, a crystal must carry defects.
    - The only weak-field option compatible with LRL's discrete symmetry is dislocations, i.e. curvature carried as torsion. Disclinations would have to be ≥ 90° rotations or boosts with cosh η ≥ 8.
    - Under that model, the fraction of disordered sites is about |T|·a ≈ (Φ/L)·ℓ_P. For a galaxy lens that is 4e-62, and for a neutron star 3e-40.
    - That is 30 or more decades below what RZ's noise would need to reappear (f ≳ 5e-10). The classical scatter from the dislocations' positions is below 1e-20 rad² (suggested).
- **Reading: INCONCLUSIVE.**
  - No FAIL: there is no O(1) focusing mismatch, and the curvature-noise estimates sit far below the bar.
  - No PASS: GR focusing on LRL is shown only conditionally on R3-1's effective law, and the noise estimate rests on an assumed defect model with no defect dynamics.

---

## 1. Against the FIXED readings (`TESTS.md:2689-2694`)

| Clause | What was found | Label |
|---|---|---|
| **PASS, part 1:** the mean propagation reproduces GR focusing | **Not shown.** Flat mean kernels are right (§2.1–2.2). RL2's √Δ mechanism is Poisson-specific (§2.5). On LRL the √Δ route is per-realization: a symmetric second-order effective law gives □_g exactly, hence Δ^{1/2} (§3). It depends on R3-1's effective law, and no exact curved LRL with focusing exists to compute on (§4.1) | proved (operator identity) + conditional |
| **PASS, part 2:** curvature-induced noise below RZ's bar for physical lenses | **Holds in the defect model, by ≥ 30 decades in the core-disorder fraction** (§4.3). The model is suggested; defect dynamics are not supplied | suggested |
| **FAIL:** an O(1) mismatch | None found. The flat mean has the massless pole with O(k² ln k) corrections (§2.2). The one-hop per-realization difference is O((a/D)^~1) (§2.6) | checked |
| **FAIL:** curvature noise above the bar | Not in the dislocation model. The disclination and grain-boundary options are worse (O(1) conical defects; quasi-periodic interfaces) but are not forced (§4.2) | suggested |

**Reading: INCONCLUSIVE**, as expected (`TESTS.md:2694`).
- It leans PASS on the noise clause, conditional on a defect model.
- It is open on the focusing clause, which reduces to R3-1's effective law.
- A new caveat comes in (§2.6): in-band forward responses differ from realization to realization.

---

## 2. (a) Mean link and propagator kernels on L₇-LRL

Units: physical x = (√7 n₀, n₁, n₂, n₃) with n ∈ ℤ⁴. x² = −7n₀² + |n|² (signature −+++). Density ρ = 1/√7. For future-timelike v, m := τ² = 7n₀² − |n|² ∈ {1, 2, …}.

### 2.1 Structure of every mean kernel (proved)

- Let K be a kernel built covariantly from one realization: K(x, y) = k(N(y−x), m(y−x)) for y in the causal future of x. Here N is the interval count, which depends only on v = y − x ∈ gL₇, since g preserves the causal order and the lattice is translation-invariant.
- N is Γ_L-invariant: γ ∈ Γ_L maps the diamond D(0, v) onto D(0, γv) and L₇ onto itself.
  - *Checked* (`r33_A_*.out` [2]): 394 directly counted cubic classes whose vectors reduce to a smaller n₀ under integral reflections. There were 0 mismatches.
- Unfolding the Haar average over SO⁺(1,3)/Γ_L orbit by orbit gives the ensemble mean
  K̄(x) = Σ_m C_m(k) θ(x⁰) δ(x² + m), with C_m(k) = Σ_N k(N, m)·C_{m,N}.
  - Here C_{m,N} is the density of lattice vectors of norm m and interval count N, per unit invariant hyperboloid measure.
  - Each orbit of a timelike vector has a finite stabilizer, so each orbit contributes a constant times the invariant measure on its hyperboloid.
- **Check of the C's** (Siegel average): the mean of C_m over m = 1…40 is 0.3818 at R = 300, against ρ = 0.3780. C_m converges at the 1–3% level between R = 150 and R = 300 (`r33_A_R150.out`, `r33_A_R300.out`).

### 2.2 The link kernel (checked)

- **Where the links are** (`r33_A_R300.out` [3], [4]): every link has τ² ∈ {1, …, 7}.
  - Every vector with n₀ = 1 is a link.
  - The link densities per shell are C^link_m = 0.504, 0.744, 0.250, 0.249, 0.311, 0.127, 0.020 for m = 1…7.
  - Shells m = 1, 2, 3 and 5 are links throughout. Shells 4, 6 and 7 are split by interval count.
- **Mean link kernel:** Σ_{m≤7} C^link_m θδ(x² + m).
  - Total weight W_LRL = 2.205, against W_Poisson = √(6ρ) = 1.506 at the same density. ⟨τ²⟩_link = 2.81 against Poisson's 5.07.
- **Fourier transform** (spacelike k): F(k) = Σ C_m (2π√m/k) K₁(k√m) = (2πW/k²)[1 + O(k²⟨m⟩ ln k)]. The ratios F/(2πW/k²) are:

  | k | 0.001 | 0.01 | 0.1 | 0.3 | 1 |
  |---|---|---|---|---|---|
  | LRL | 0.99999 | 0.99935 | 0.967 | 0.835 | 0.403 |
  | Poisson | 0.99999 | 0.99942 | 0.971 | 0.852 | 0.462 |

- **Result.** In flat spacetime the LRL mean link kernel is the massless retarded kernel with (a/r)²-type corrections, just as for Poisson (E1′; `PRICE_NOTE.md` §1: "E[aL] tends to the massless retarded light-cone kernel"). Only the normalization differs: a = 1/(2πW).

### 2.3 Poisson-tuned layer weights fail on LRL (checked)

- **The test.** The 4D BD weights (1, −9, 16, −8) on the layers N = 0…3 give, on LRL:
  - Σ_m C^BD_m = 11.35, where it must be 0 to remove the 1/k² term;
  - Σ C^BD_m m = 69.7, where it must be 0 to remove ln k (`r33_A_R300.out` [5]).
- **So** the mean of the Poisson-tuned operator on LRL is not a d'Alembertian.
- **What LRL needs instead.** LRL needs its own shell weights. Making the mean symbol −c k² + O(k⁴ ln k) takes four moment conditions on finitely many shells: Σ C w = Σ C w m = Σ C w m ln m = Σ C w m² = 0. Any five shells with a non-degenerate system solve them (*suggested*; not solved here).
- **RL1/RL2's three stable six-layer operators are Poisson-specific.** Their stability analysis does not transfer.

### 2.4 Mean of the per-realization inverse, i.e. RL2's object (proved structural point)

- **Why RL2's reduction worked.** RL2's exact reduction H̄ = f̄ + ρ f̄ ∗ H̄ (`C4_RL2_report.md:39-42`) rests on the Poisson Palm/Mecke identity: given points, the rest stays Poisson. This makes the mean inverse the inverse of the mean.
- **Why it fails on LRL.** On LRL the reduced Palm distribution is the deterministic lattice gL₇ ∖ {0}. A chain's interval counts are fully correlated, so E[(I − N)⁻¹] ≠ (I − N̄)⁻¹ in general.
- **What the mean inverse is instead.** It is the Haar average of per-realization lattice Green functions. It is Lorentz-invariant in flat space (by invariance in law) and is a function Σ_m h_m θδ(x² + m) over integer shells. Here h_m is the Γ_L-orbit value of the realization's inverse, which is finite for each pair because every interval holds finitely many points.
- **Not computed.**
- **Consequence.** RL2's chain-rule proof of √Δ (`C4_RL2_report.md:96-103`) has no LRL analogue.

### 2.5 No bounded law is nontrivial (proved; ergodic input RECALLED)

**Lemma.** Every bounded operator on ℓ²(L₇) that commutes with the L₇-translations and with Γ_L is a multiple of the identity.

*Proof.*
1. Such an operator is a multiplier B̂ ∈ L^∞(𝕋⁴) on the dual torus, invariant under the dual action of Γ_L.
2. Γ_L acts on the characters (the dual lattice) with infinite orbits on every G ≠ 0, because Γ_L is infinite and its stabilizers have infinite index.
3. A group of toral automorphisms with no finite non-trivial character orbit acts ergodically (RECALLED, standard).
4. So B̂ is constant almost everywhere. ∎

**Consequences:**
- every non-trivial Γ_L-covariant law is unbounded or distributional. This agrees with O1's Lemma C′ and the R2-2 referee's "convergent orbit sums" caveat;
- the per-realization symbol is a Γ_L-invariant distribution, singular where q + G is null for some reciprocal vector G (suggested; a dense set);
- in-band momenta are kinematically coupled to on-shell trans-Planckian modes k − G, with ω′ ≥ κ²/(4ω) (`R2-2_report.md:177-181`). The invariant phase space at fixed invariants is non-compact. Whether these "far umklapp" channels attenuate the coherent amplitude is **open**. They are out of band, so they do not feed RZ's in-band noise, but they bear on the mean.

### 2.6 One realization against the mean: the forward response (checked)

**Set-up** (`r33_D_perrealization_links.py`).
- Take a smooth source J: a Gaussian of Euclidean width W = D/5, centred on the past light cone of a realization point at null distance D.
- φ_g = Σ_{links v} J(−gv) for 60 frames g = R₁·B(η ≤ 1)·R₂.
- Compare with the ensemble mean Σ C^link_m ∫θδ(x² + m)J.
- Link vectors were enumerated to |x|_E ≤ 880, which covers every frame used ("reach" ≤ 853).

**Results** (`r33_D_perrealization_links.out`):

| D (lattice units) | 10 | 20 | 40 | 80 | 120 |
|---|---|---|---|---|---|
| frame-to-frame sd / mean | 0.149 | 0.117 | 0.037 | 0.020 | 0.0137 |
| Poisson √(3/mean) (E1′-b leading bound) | 0.555 | 0.277 | 0.138 | 0.069 | 0.046 |
| ratio | 0.27 | 0.42 | 0.27 | 0.29 | 0.30 |

- **Scaling.** The deviation falls roughly as D⁻¹ (local exponent 0.9–1.2; 60 frames give about 9% uncertainty on each sd).
- **Size.** It is about 0.3–0.4 times the Poisson scatter at the same mean count.
- **Where it sits** (`r33_E_inband_split.out`). Link vectors were enumerated to 600, untruncated for η ≤ 1, with 30 frames. Fit a linear trend across 12 nearby lattice translates of the evaluation point; that removes the smooth gradient of J. The frame-to-frame variation then sits almost entirely in the smooth (in-band) part:

  | D | 20 | 40 | 80 |
  |---|---|---|---|
  | sd/mean at one point | 0.097 | 0.057 | 0.028 |
  | sd/mean of the smooth part | 0.100 | 0.056 | 0.028 |
  | lattice-scale sd/mean within one frame | 0.016 | 0.0039 | 0.0012 |
  | Poisson √(3/mean) | 0.277 | 0.138 | 0.069 |

  - The smooth part falls as about D^{−0.85…−1}. The lattice-scale (out-of-band) part falls faster, as about D^{−1.7…−2}.
  - With this frame sample the ratio to Poisson is 0.35–0.41. Frame samples differ between runs: 0.037 against 0.057 at D = 40 with 60 and 30 frames. "About 0.3–0.4 of Poisson" is the honest summary.

**Reading.**
- Even in flat space, a single realization's one-hop response to an in-band source is not Lorentz-invariant. It is a Γ_L-invariant, frame-dependent, smooth anisotropy of relative size ~(a/D)^~1.
- Ensemble invariance does not remove it in our one universe. This is the referee's "realization-specific Bragg pattern" (`ref_R2-2/R2-2_referee.md:179-189`), seen at q ≈ 0.
- For one hop at physical scales it is harmless (relative ~(a/D) ≲ 1e-28 for sub-Planckian windows).
- If a term of the form (aω)^δ with δ ≤ 1 entered a per-realization dispersion relation, time-of-flight bounds would exclude it.
  - Example: δ = 1 gives a phase of about 5e4 rad for optical light over 1 Gpc; δ = 1.2 gives about 0.08 rad (arithmetic in §8).
  - Whether it does is R3-1(b)'s "non-polynomial" question. Zariski density does not protect non-polynomial Γ_L-invariant terms, but measurable Γ_L-invariant functions of a null direction are a.e. constant, because the lattice acts ergodically on the sphere at infinity (RECALLED). So the leading on-shell anisotropy may vanish in the limit D → ∞ (suggested).
- **Not computed.**

---

## 3. Where GR focusing could come from on LRL (proved identity; conditional)

**The comparator.**
- The G-L referee showed that a smooth scalar operator □_g + A^a∇_a + B has direct multiplier exp(−½∫A·k dλ) relative to Δ^{1/2} (`C3_G-L_referee.md:71-87`).
- Hadamard's direct coefficient of □_g is Δ^{1/2} (RECALLED, comparator).

**Identity (proved, elementary).**
- Let P = a^{μν}∂_μ∂_ν + b^μ∂_μ + c be symmetric with respect to the measure √|g| d⁴x, where g_{μν} is the inverse of a^{μν}.
- Then b^μ = |g|^{−1/2}∂_ν(|g|^{1/2}a^{μν}), so P = □_g + c.
- *Proof.* P − P† is first order with coefficient 2b^μ − 2|g|^{−1/2}∂_ν(|g|^{1/2}a^{μν}). Setting it to zero gives the claim. ∎

**Consequence (conditional).** GR focusing per realization, not just on average, follows if a realization's long-wavelength effective law satisfies all three of:
- (i) it is local, second order and normally hyperbolic, with principal metric g;
- (ii) it comes from a quadratic action, so it is symmetric with respect to the counting measure;
- (iii) its counting measure is ρ√−g. For a crystal whose metric is its own lattice metric, this holds by construction.

Then:
- A = 0 and the propagator's direct part is Δ^{1/2}.
- (i) is R3-1's open effective law. §2.5 shows it can only come from unbounded, distributional laws.
- **Failure mode.** A retarded-only (non-symmetric) law may couple to the defect torsion: A^μ = c·T^μ is allowed by local Lorentz invariance. That multiplies the focusing by exp(−½c∫T·k dλ) = 1 + O(c·Φ·D/L) (suggested). For a galaxy lens that is an O(1e-6) flux error.

**Why the Poisson geometries cannot be reused.**
- RL2 used plane waves and the conformal lens (`C4_RL2_report.md:46-48`). Neither has an exact LRL: a plane wave's isometry group has no boosts, and a lens has no isometries at all.
- So the focusing clause cannot be checked by direct computation on any LRL that exists today.

**Links are not the candidate.** G-L's FAIL concerns the one-hop mean on Poisson, (νΔ)^{−1/2}. On LRL the one-hop kernel is a fixed number-theoretic shell set (§2.2). Its curved behaviour depends on how defects cut the needle diamonds (§4.4). It is not a focusing mechanism.

---

## 4. (b) Curved versions

### 4.1 An exact curved LRL on de Sitter or anti-de Sitter (proved from RECALLED inputs; checked)

**Construction.**
- Let Q₅ = −n₀² + n₁² + … + n₄², and let Y_N = {n ∈ ℤ⁵ : Q₅(n) = N}. This is a discrete subset of the de Sitter hyperboloid of radius √N.
- Γ = SO(Q₅)(ℤ) is a lattice in SO(1,4) (Borel–Harish-Chandra, RECALLED), and Γ preserves Y_N.
- Y_N has finitely many Γ-orbits (RECALLED finiteness), and each orbit's stabilizer is a lattice in SO(1,3) (Borel–Harish-Chandra again).
- So X = gY_N, with g ~ Haar on SO(1,4)/Γ, is a point process on dS₄ that is **invariant in law under the full de Sitter group**, with finite intensity ρ ∝ vol(H/Γ_p)/vol(G/Γ) (proved; same unfolding as R2-2 Prop. (a)).

**Checks** (`r33_B_dS_points.out`):
- Reflections in r₁ = (1,1,1,0,0) and r₃ = (1,−1,−1,0,0), with Q = 1 and B = −3, give an integral orthochronous element γ with det 1 and γ₀₀ = 17, 577, 19601, … (unbounded). It maps Y_50 to itself.
- Pair values Q₅(n − n′) are even integers.
- The crude density near the waist is 0.091 per unit 4-volume, against an O(𝔖/(2√N)) = 0.071·𝔖 Hardy–Littlewood scale.

**Limits:**
1. **Null pairs.** The ℤ-form is isotropic (Meyer, RECALLED). Null-separated pairs exist: 97,536 among 7,080 points with |n₀| ≤ 4 (checked).
   - The no-null, hard-core version needs a form anisotropic over its field, e.g. −√2 x₀² + Σx_i² over ℤ[√2], whose Galois conjugate is definite (cocompact).
   - Its points are a cut-and-project set. |Q(n − n′)| ≥ 1/max σ(Q(n − n′)) > 0 by the norm argument (proved; not checked numerically).
2. **No lensing test.** de Sitter null rays have Δ = ν = 1 (`C3_G-L_referee.md:58`), so the construction cannot test focusing.
3. **No in-band silence shown.** Γ is non-abelian. The "Bragg spectrum" becomes the automorphic spectrum of the fixed Γ with non-zero SO(1,3)-periods, and its low-lying members sit at Hubble-scale transfers (suggested).
4. **Not flat-L₇ locally.** Locally the set is a curved cut of ℤ⁵, i.e. quasi-periodic, not an L₇ crystal (suggested).

**Prior art.** None in the repository (grep "integral points": 0 files).

### 4.2 Generic curvature needs defects (suggested; prior art Kleinert's world crystal, `OUTSIDE_VIEW.md:45`)

A lens has no isometries, so there is no invariance-in-law construction. Each realization must be a crystal whose own lattice metric is curved. Three ways to carry the incompatibility:

| Option | Mechanism | Assessment |
|---|---|---|
| **Disclinations** | The holonomy must lie in Γ_L. Its smallest elements are 90° rotations (n₁, n₂, n₃ permutations) and boosts with cosh η ≥ 8 (R2-2) | O(1) conical defects. Weak curvature R would need O(1) deficits spaced by ~L_curv: cosmic-string-like image splitting. Not usable for weak fields |
| **Grain boundaries** | Interfaces between gL₇ and g′L₇ with g⁻¹g′ ∉ Γ_L | Incommensurate interfaces. Their differences of reciprocal vectors G − G′ are dense, so in-band spectral weight is expected. A noisy option, not forced |
| **Dislocations (torsion)** | The flat lattice connection plus torsion realizes any metric (teleparallel; Kröner; Katanaev–Volovich; RECALLED). In 4D a dislocation is a codimension-2 worldsheet with Burgers vector b ∈ L₇, \|b\| ≳ a | The weak-field option. Minimal torsion over a region of size L is \|T\| ≈ R·L ≈ Φ/L, since the Lorentz holonomy R L² of a loop must be carried around its perimeter. The worldsheet density is n_d = \|T\|/b |

**Smooth strain is not where curvature goes.**
- The metric is the crystal's own, so cells are locally perfect L₇.
- In any case strain cannot close the gap: |SG|_E ≥ (1 − ‖ε‖)|G|_E ≥ (1 − ‖ε‖)·2π/(√7 a) in the observer's frame (proved, trivial; `r33_C_defect_noise.out` N3).
- Oppenheim–Margulis density of G² values for an irrational strained form (RECALLED) is irrelevant in band, because in-band transfers need small Euclidean |q|, not small q².

### 4.3 Noise from the defects (suggested; `r33_C_defect_noise.out`)

**Two channels:**
- **(N1) Disordered cores.**
  - The fraction of events in cores is f ≈ n_d a² ≈ |T|·a.
  - If only those events are random, the RZ/RL ladder's rung scales as f and its rate as √f (RL2: z ∝ √ε, `C4_RL2_report.md:153-160`). So the variance e-folds are ≈ √f × 45,258, the proved rate e-folds at 1 s / 1 Gpc (`RZ_referee.md:17`).
  - Thresholds: ≤ 1 variance e-fold needs f < 4.9e-10. N_B/S < 1, after the 122 e-fold in-band penalty (`RZ_referee.md:7`), needs f < 7.3e-6.
- **(N2) Granularity of dislocation positions.**
  - This is a classical random metric made of the long-range b/r fields.
  - For Poisson-placed dislocations, Var(Δφ) ≈ ω²·D·n_d·b²·δ between rays a distance δ apart. Ordered arrays would be quieter.

**Results** (a = ℓ_P):

| object | Φ | L (m) | \|T\| (m⁻¹) | f = \|T\|a | (a/L_curv)² | √f·45,258 e-folds | Var Δφ, EHT 1.3 mm, δ = 1e7 m (rad²) |
|---|---|---|---|---|---|---|---|
| Earth lab | 7e-10 | 6.4e6 | 1.1e-16 | 1.8e-51 | 4.5e-93 | 1.9e-21 | 2.6e-30 |
| Sun | 2.1e-6 | 7e8 | 3.0e-15 | 4.9e-50 | 1.1e-93 | 1.0e-20 | 1.7e-24 |
| galaxy lens | 7e-7 | 3e20 | 2.3e-27 | 3.8e-62 | 2.0e-117 | 8.8e-27 | 2.6e-27 |
| cluster lens | 1.1e-5 | 3e22 | 3.7e-28 | 5.9e-63 | 3.2e-120 | 3.5e-27 | 4.2e-26 |
| M87* photon ring | 0.5 | 1.9e13 | 2.6e-14 | 4.3e-49 | 3.6e-97 | 3.0e-20 | 1.9e-21 |
| neutron star | 0.2 | 1.2e4 | 1.7e-5 | 2.7e-40 | 3.6e-79 | 7.4e-16 | 7.5e-22 |
| cosmology (\|T\| ~ H₀/c, 1 Gpc path) | n/a | n/a | 7.6e-27 | 1.2e-61 | 1.5e-122 | 1.6e-26 | 8.8e-22 |

- **Margin.** The largest f, at a neutron-star surface, is 30 decades below the 1-e-fold threshold. With a = 1e-19 m instead of ℓ_P, the largest f is 1.7e-24, still 14 decades below.
- **(a/L_curv)² is not the right scale.** The defect fraction scales as |T|a ≈ (a/L_curv)·√Φ. That is larger than the pre-registered (a/L_curv)² guess by L/a ~ 1e39–1e57, and still negligible.
- **So in this model, curvature noise is far below RZ's bar for every physical lens listed (suggested).**

### 4.4 What §4.3 assumes and does not cover

- **The defect model is not derived.** Nothing in the axioms says how a curved geometry is made from LRL. The dislocation route is the cheapest known one, not shown to be forced.
- **Defect dynamics are not supplied.**
  - As the geometry changes, dislocations must be created and must move.
  - FRW expansion at fixed ρ needs net creation of points at a rate of about ρ·3H per unit 4-volume. Dislocation climb is one way to do that, and it may bear on "Records form" (reading).
  - A defect law that is covariant in law with finite density is impossible if its orientations are drawn from a Lorentz-invariant law, because the Grassmannian of timelike 2-planes is non-compact (BHS-like, suggested). Orientations must therefore come from the state (T is set by the matter), not the law.
- **Cores are modelled crudely** as "Poisson-like disorder in a fraction f". The √f ladder scaling borrows RL2's √ε law, whose exponent ½ is itself suggested (`C4_RL2_referee.md:11`).
- **Link kernels near dislocations.** A dislocation crossing a link's needle diamond (probability ~ |T|·r over null distance r) re-wires far links. This bears on one-hop kernels, not on effective-law propagators (§3).

---

## 5. Prior art (counted once)

- **Repository:**
  - R2-2's report and referee (LRL, the gap, the narrowed in-band silence);
  - RL2 and its referee (Poisson √Δ through the Volterra reduction and the Van Vleck chain rule);
  - G-L and its referee (one-hop (νΔ)^{−1/2}, NEC signs, the multiplier exp(−½∫A·k));
  - E1′/E1′-b (the flat link mean and the Var ≤ 3N̄ bound);
  - RZ (the bar);
  - `OUTSIDE_VIEW.md:45`: Kleinert's world crystal, where defects carry curvature. The packet notes that "a dislocation is a change of adjacency";
  - `R1_condensed_matter.md:19` (Kröner defects as matter: fails equivalence; a different use);
  - `docs/ADMISSIBILITY_RULE_BOND_STRAINS_…_2026-09-21.md:38` (a teleparallel frame on the grid; a different object).
- **Literature, RECALLED:**
  - Borel–Harish-Chandra and Godement;
  - closed orbits of lattices (Raghunathan);
  - Meyer's theorem;
  - Oppenheim–Margulis;
  - equidistribution of lattice orbits on hyperboloids (Duke; Eskin–McMullen);
  - teleparallel gravity, Kröner, Katanaev–Volovich, Kleinert (gr-qc/0307033).
- **Not found:** the de Sitter integer-point LRL (§4.1) and the per-realization one-hop anisotropy measurement (§2.6), in the repository and in memory. No web search was run.

## 6. Scope, hypotheses and outside realizations

- **Hypotheses.**
  - §2: L₇ = diag(√7, 1, 1, 1)ℤ⁴, Haar frames, flat spacetime, kernels that are covariant functionals of the realization (interval counts and τ²).
  - §3: R3-1's effective law, conditions (i)–(iii).
  - §4.3: dislocation-carried curvature with b ≈ a, minimal torsion |T| ≈ Φ/L, Poisson-placed defects, and √f ladder scaling.
- **Excluded realizations:**
  - other arithmetic forms (only L₇ was computed);
  - isotropic ℤ⁴-LRL, with its cusp and null Bragg peaks;
  - non-covariant couplings;
  - tensor or photon propagation (everything here is scalar);
  - interacting matter;
  - the graviton (R3-2).
- **Strong words checked.**
  - "Exact" is used only for the invariance-in-law constructions and for the operator identity of §3.
  - "Far below the bar" is a model estimate, labelled suggested.
  - "Proved" is used for §2.1 (structure), §2.4 (Palm), §2.5 (lemma, with RECALLED ergodicity), §3 (identity), the §4.1 construction (RECALLED inputs) and the §4.2 strain inequality.

## 7. Price implications (named, none adopted)

- **Focusing.** On LRL, √Δ cannot come from Poisson-style averaging (§2.4). It must come from a per-realization effective law that is symmetric, local and second order. That is R3-1's open price: quasi-local, unbounded Γ_L-covariant laws (§2.5).
- **Curved spacetime.** This adds a defect sector to the LRL candidate:
  - **Lattice:** "the points of a crystal with dislocations" in place of a fixed lattice;
  - **Admissibility or Record:** a rule for creating and moving defects. This is downstream content, possibly where "Records form" acts (reading).
- **Two new open hazards for R3-1:**
  - the per-realization, smooth, frame-dependent forward anisotropy (§2.6);
  - the far-umklapp channels to trans-Planckian on-shell modes (§2.5).
- **Needs codex referee:** nothing here is a FAIL or no-go. The §2.5 lemma, the §3 identity and the §4.1 construction are positive claims that a referee could check cheaply.

## 8. Arithmetic notes

- **Optical phase under a hypothetical per-realization term (aω)^δ, over 1 Gpc:**
  - ωD = (2π/6e-7 m)·3.1e25 m ≈ 3e32 rad, and aω = 1.6e-35·1e7 ≈ 1.6e-28;
  - δ = 1: 3e32 × 1.6e-28 ≈ 5e4 rad;
  - δ = 1.2: (1.6e-28)^{1.2} ≈ 2.5e-34, so about 0.08 rad;
  - δ = 2: about 1e-23 rad.
- **The §2.6 split** was run with Rbig = 600 and η ≤ 1, so every frame's reach (≤ 568) lies inside the enumeration. An earlier Rbig = 300 run with η ≤ 1.2 was truncated at D = 40 and is superseded.
