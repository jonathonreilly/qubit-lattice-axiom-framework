# C5 R5-2: infinite-orbit kernels on LRL. Can a per-realization effective law exist at all?

**Worker.** Claude Opus 5.5 (probe R5-2), the same model family as every C5 worker and the supervisor. **Not refereed.** Run 2026-10-12, 13:39Z to about 14:20Z. No repository file was edited.

**Reading returned: INCONCLUSIVE.** No explicit PASS kernel was found, and no class-wide no-go is proved. The question is reduced to an exact arithmetic condition. Every natural infinite-orbit family is checked to fail it, and the mechanism is identified: **retardation**.

**Scratch** (`scratchpad/C5/R5-2/scripts/`):
- `r52_A_cone_sums.py` → `r52_A_R50.out`, `r52_A_R77.out` (and `.npz`): 3+1 per-frame sums over whole vector classes of L₇.
- `r52_B_mellin_check.py` → `.out`: closed-form Mellin transform of R4-1's Selberg transform, and its residue expansion.
- `r52_C_infinite_smooth_recheck.py` → `.out`: infinite-orbit smooth kernels with mean □, on R4-1's shell data (`.npz` loaded with `allow_pickle=False`).
- `r52_D_1plus1_analog.py` → `.out`: the exactly solvable 1+1 analog over a full period of its quotient circle.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full.
- `TESTS.md:2302-2898`: the C5 method, rounds 1–5. R5-2 is at `:2877-2884`.
- `SUMMARY.md` §§21–22.
- `C5_R3-1_report.md` and its referee (refereed); `C5_R3-3_report.md`.
- R4-1 report and scripts (unrefereed; its referee is running, and `ref_R4-1/codex_run.log` had no verdict at 13:40Z).
- `R4-3_report.md` §4 (unrefereed).

**Labels.**
- *proved*: complete argument here (same family, unrefereed).
- *proved mod RECALLED*: complete except for a named standard theorem.
- *checked*: numerical, in the scratch files.
- *suggested*: argued only.
- *reading*: interpretation.
- *comparator*: outside literature.

---

## 0. In plain words

- **What R4-1 left open.** The average d'Alembertian on the random-frame lattice (LRL) can be built, but one realization's version drifts with the observer's frame. For kernels on finitely many shells, the drift grows like (ℓ/a)³ relative to □φ. The escape was kernels spread over **all** shells with weights that fall off.
- **What an escape must do.** I turned the requirement into exact form (§2). For each vibration mode j of the quotient manifold, define the weighted Dirichlet series D_j(s) = Σ_m f_m Ψ_j(m) m^(−s). Here Ψ_j(m) is the sum of mode j over the shell-m points. PASS holds **if and only if** D_j vanishes at the three points s = ½ + ir_j/2 − k, k = 0, 1, 2, for every mode j, with infinitely many modes. That is three exact identities per mode.
- **Exact cancellation does exist, but only where there is no d'Alembertian.**
  - If the kernel uses **all** lattice vectors (past, future and spacelike) with polynomial weights, Poisson summation makes the frame-dependence exponentially small (proved; checked to 1e-12).
  - But such a kernel's symbol sits at k = 0. It measures moments of φ and is not □.
- **Retardation destroys the cancellation.**
  - Keep only the causal past, which a retarded law must do. The cancellation then fails even for the simplest infinite kernel, weight 1 on every past point.
  - In the exactly solvable 1+1 analog this is a theorem (mod Hecke theory). There, "timelike" is a congruence condition, (m/7) = −1. Restricting to it brings in an odd character whose Gamma factor is shifted by one unit from the kernel's. The leading drift coefficient in every mode is then a nonzero L-value.
  - In 3+1 the same picture is checked numerically. Weight 1 on all past points drifts at 0.15–0.55 times the rate of a 7-shell kernel, and the drift grows over ℓ = 4–8a.
- **Smooth, decaying infinite kernels with mean □ still drift like (ℓ/a)³ (checked).** For f_m = e^(−m/L²)·cubic on all shells (L = 1.5, 2, 2.5), the fitted growth slopes are +3.7 to +4.0. Smoothing the weights shrinks the prefactor, not the exponent.
  - The prefactor is a Dirichlet-series value. It falls like Λ⁻³ for weights with F(0) ≠ 0, and faster than any power only for weights that are flat at m = 0 (suggested; this is R4-3's mesoscale escape).
  - Even then it is not zero, so a fixed law of this kind never meets PASS.
- **Open.** Whether **some** infinite-orbit weight sequence satisfies all three identities in every mode. No natural mechanism (Poisson, cusp vanishing, trivial zeros) supplies them for retarded kernels. I have no proof that none exists.

---

## 1. Against the FIXED readings (`TESTS.md:2881-2884`)

| Clause | Finding | Label |
|---|---|---|
| **PASS:** "an explicit infinite-orbit retarded kernel whose mean is □ to O(a²) and whose per-realization rms deviation falls at least as (a/ℓ)², checked" | **Not met.** Every infinite-orbit kernel tested drifts with growing or non-decaying amplitude: smooth mean-□ families (slopes +3.7…+4.0, §4.1); f ≡ 1 and f = m on all past shells in 3+1 (§3.4) and in 1+1 (§3.3). No construction of the §2 identities was found | checked |
| **FAIL:** "a no-go covering every infinite-orbit kernel with convergent tube symbol (refereed)" | **Not met.** Proved: the exact equivalence of PASS with infinitely many Dirichlet-series identities (§2); that Poisson-exact kernels have no □ (§3.1); and the 1+1 analog's nonvanishing for the scale-free retarded family (§3.3). **Not proved:** that no weight sequence satisfies the §2 identities | proved / proved mod RECALLED, in the stated sub-classes only |
| **INCONCLUSIVE** | **Returned** | reading |

**Strongest correct statement (worker).** Consider a retarded Γ_L ⋉ L₇-invariant kernel with f_m = O(m^(−A)), A > 5. Its per-realization deviation on observer-frame Gaussians satisfies Δ_ℓ = O(ℓ⁻⁴), relative (a/ℓ)², **if and only if** D_j(½ + ir_j/2 − k) = 0 for k = 0, 1, 2 and every non-constant automorphic mode j. The analogous conditions apply at exceptional and r = 0 modes. Finitely supported f never satisfy them (R4-1, unrefereed). The explicit infinite families tried do not satisfy them (checked). The only exactly cancelling families found are non-retarded or carry no d'Alembertian (proved).

---

## 2. The exact reduction (proved mod RECALLED)

### 2.1 Hypotheses (stated before titles)
- **(H1)–(H3)** as in R4-1 (`R4-1_report.md:73-77`): one realization g(L₇ + u); a retarded linear kernel f_m on the future-timelike shells Q(v) = −m; the ensemble mean via R3-3's unfolding.
- **(H4)** R4-1's spectral expansion on 𝒳 = Γ_L∖H³ (`R4-1_report.md:177-191`; unrefereed; RECALLED Selberg/Harish-Chandra):
  Δ_ℓ(u) = Σ_{j≥1} ψ_j(u)·c_j(ℓ),   c_j(ℓ) = Σ_m f_m Ψ_j(m)·H_{r_j}(m/2ℓ²),
  with H_r(β) = (4π/r)∫₀^∞ e^(−β cosh 2d) sinh d sin(rd) dd and Ψ_j(m) = Σ_{ŵ∈Γ∖shell m} ψ_j(ŵ)/|Γ_ŵ|.
- **(H5)** Decay: |f_m| ≤ C m^(−A) with A > 5.

### 2.2 Closed-form Mellin transform (proved; checked)
For Re s > ½:

H̃_r(s) := ∫₀^∞ β^(s−1) H_r(β) dβ = (π/(ir))·2^(s−2)·[Γ(s/2+¼+ir/4)Γ(s/2−¼−ir/4) − Γ(s/2−¼+ir/4)Γ(s/2+¼−ir/4)].

- **Proof.** Mellin in β gives Γ(s)(cosh 2d)^(−s). Write sinh d sin rd = (1/2i)[cos((r−i)d) − cos((r+i)d)]. Then use ∫₀^∞ cosh^(−2a)x cos bx dx = 2^(2a−2)Γ(a+ib/2)Γ(a−ib/2)/Γ(2a).
- **Poles.** Simple poles at s = ½ ± ir/2 − k for **every** k ≥ 0 (k even from one Gamma pair, k odd from the other). All residues are nonzero for real r ≠ 0.
- **Checks** (`r52_B_mellin_check.out`):
  - The closed form agrees with the numerical Mellin integral to 1e-11 to 1e-15 at r = 1, 2.5 and s = 1.1, 1.7, 2.5.
  - Residue sums through k = 0…3 reproduce H_r(β) at β = 1e-2 to 1e-4. The relative error falls by about a factor β per order, down to the quadrature floor of 2.5e-10.
  - This also confirms R4-1's leading asymptotic (`R4-1_report.md:193-196`), which is the k = 0 residue.

### 2.3 Proposition 1 (proved mod RECALLED)
Under (H1)–(H5):

c_j(ℓ) = (1/2πi)∫_{(σ)} H̃_{r_j}(s)(2ℓ²)^s D_j(s) ds,   D_j(s) := Σ_m f_m Ψ_j(m) m^(−s).

1. **Bounds.** |Ψ_j(m)| ≤ ‖ψ_j‖_∞·C_m·(m/2)·vol(𝒳), from the unfolding normalisation (H3). So D_j is absolutely convergent and bounded on Re s ≥ 2 − A + δ.
2. **Contour shift.** Shift the contour to Re s = −5/2 + ε, which is allowed since A > 5. Then

   c_j(ℓ) = Σ_{k=0}^{2} Σ_± R_{k,±}(r_j)·(2ℓ²)^(½ ± ir_j/2 − k)·D_j(½ ± ir_j/2 − k) + E_j(ℓ),   |E_j(ℓ)| ≤ C ℓ^(−5+2ε)·poly(r_j)·e^(−π r_j/4)·‖ψ_j‖_∞.

   The e^(−πr/4) factor comes from Stirling on the two Gamma products.
3. **Sufficiency.** Assume D_j(½ ± ir_j/2 − k) = 0 for k ≤ 2 and all j. Then Σ_j |E_j|² ≤ C ℓ^(−10+4ε). The inputs are Weyl's law and the sup-norm bound ‖ψ_j‖_∞ ≲ r_j on a compact 3-orbifold (RECALLED, Avakumović–Levitan–Hörmander; the torsion points are assumed harmless). So PASS holds: ‖Δ_ℓ‖ = O(ℓ⁻⁴), i.e. relative O((a/ℓ)²).
4. **Necessity.** PASS gives |c_j(ℓ)| ≤ ‖Δ_ℓ‖ ≤ Cℓ⁻⁴ for each j (Parseval). The k = 0, 1, 2 terms scale as ℓ¹, ℓ⁻¹, ℓ⁻³ with phases ℓ^(±ir_j) that rotate in ln ℓ. With nonzero residues, they must vanish in turn. This is R4-1 step (iii) (`R4-1_report.md:200`) extended to three orders. Since f and ψ_j are real, D_j(s̄) = conj D_j(s), so one complex condition per (j, k) suffices.
5. **Other modes.** Exceptional modes (r = iτ) give the same conditions at real points ½ ± τ/2 − k. A mode with r = 0 has double poles, and needs D_j = D_j′ = 0 at ½ − k.

**Reading.** An infinite-orbit escape is an infinite moment problem. The weight sequence f must be orthogonal to the vectors (Ψ_j(m) m^(−½ + ir_j/2 + k))_m for every j and k ≤ 2. It must also meet R4-1's four mean conditions with a nonzero normalisation. R4-1 (iv) excludes finitely supported f (unrefereed). Whether an infinitely supported solution exists is exactly the open question.

### 2.4 Theta-lift form (proved identity; automorphy RECALLED)
Put y = 1/(4πℓ²) and let Θ(τ, u) = Σ_{v∈L₇} e(−Q(v)x) e^(−2πy|v|²_u) be the Siegel theta. Then

F_ℓ(u) = c + ∫₀¹ Θ(x+iy, u)·G(x) dx,   G(x) := Σ_{m≥1} f_m e(−mx)

(term-by-term; proved). So D_j is the f-weighted Dirichlet series of the **positive-index (timelike) Fourier coefficients only** of g_j(τ) = ⟨Θ(τ,·), ψ_j⟩. RECALLED: g_j is the Siegel theta lift of ψ_j, a weight-1 form for a congruence subgroup. Since V = ℚ⁴ with Q is anisotropic, it has no constant term (as R4-3 §4.2 suggested, `R4-3_report.md:221-224`). The negative-index coefficients belong to spacelike vectors (periods over totally geodesic surfaces). A retarded kernel can never weight them.

---

## 3. Where exact cancellation does and does not occur

### 3.1 All-vector polynomial kernels: exact, but no d'Alembertian (proved; checked)
- **Poisson summation.** For any polynomial P, Σ_{v∈gL₇} P(Q(v))φ_ℓ(v) = ρ∫P(Q)φ_ℓ + O(e^(−cℓ²)). The reason: P(Q)φ_ℓ is Schwartz with Fourier transform P(−□_k)·(Gaussian of width 1/ℓ), and the dual lattice in any observer frame has Euclidean minimum ≥ e^(−η)·min|L₇*| > 0. The per-realization deviation is therefore exponentially small in every frame.
- **Checked.** The full-lattice sum F (P = 1) is frame-independent to 1e-12 for ℓ = 4–8 (`r52_A_R77.out`, block [F]; the 3e-7 at ℓ = 9 is the reach). In 1+1 it is flat to 1e-13 for ℓ = 3–36 (`r52_D_1plus1_analog.out`).
- **But the symbol is P(−□_k)δ⁴(k)** (proved, elementary). Such a kernel computes moments of φ. It is not a d'Alembertian.
- **The same holds for periodic weights c(Q(v) mod q)**, by Poisson on cosets of qL₇ (suggested). They give δ-supported or Bragg-shifted symbols, and the kernel is not retarded.

### 3.2 Why a d'Alembertian needs non-smooth lattice weights (suggested)
- An invariant kernel whose symbol is −k² + … must be concentrated near v = 0, so by Lorentz invariance near the whole light cone.
- At Euclidean radius |v| ~ ℓ near the cone, any fixed F(Q(v)) varies on scale Λ/ℓ ≪ a. The lattice aliases it, the dual terms are O(1), and the cancellation must instead be arithmetic (the §2 identities).
- This is the deterministic analogue of the BD mesoscale (comparator: Sorkin gr-qc/0703099).

### 3.3 1+1 analog: retardation breaks the cancellation in every mode (proved mod RECALLED Hecke theory; checked)
**Setting.** Q = −7n₀² + n₁². Here Γ = ⟨ε⟩ with ε = 8 + 3√7, and 𝒳 is a circle of length η₀ = ln ε = 2.76866. Modes are e^(2πiku/η₀), with r_k = 2πk/η₀ and ν_k = r_k/2. The analogue of H_r is K_{iν}(β), whose Mellin transform is 2^(s−2)Γ((s+iν)/2)Γ((s−iν)/2).

1. **Genus fact (proved; checked).** Q ≡ n₁² (mod 7), and (−1/7) = −1. So for 7 ∤ m the shell Q = −m is timelike exactly when (m/7) = −1. The check found sign(Q) = (|Q|/7) for every represented |Q| < 400 (`r52_D_1plus1_analog.out:1`).
2. **Ideal-theoretic form.** Z[√7] is the maximal order of class number 1, and every unit has norm +1. So the timelike shell sums are Ψ_k^T(m) = ½ Σ_{N𝔞=m}(1 − σ(𝔞))χ_k(𝔞). Here χ_k is the Grössencharacter |α/α′|^(iν_k), and σ = sgn N is the narrow-class (genus) character, equal to (·/7)∘N off 7. With f ≡ 1, D_k(s) = ½[L(s, χ_k) − L(s, χ_kσ)].
3. **Gamma factors (RECALLED Hecke).**
   - L(s, χ_k) has Gamma factor Γ_R(s+iν_k)Γ_R(s−iν_k), which is exactly the kernel's Mellin factor. Its half of c_k(ℓ) has an entire integrand and is O(ℓ^(−∞)).
   - σ is odd at both real places, so L(s, χ_kσ) has Γ_R(s+1+iν_k)Γ_R(s+1−iν_k). The kernel's poles at s = ±iν_k − 2n are not cancelled.
   - The leading coefficient is ∝ Γ(iν_k) L(iν_k, χ_kσ). By the functional equation it is a nonzero multiple of L(1 − iν_k, conjugate character), which is ≠ 0 because Hecke L-functions do not vanish on Re s = 1 (RECALLED).
   - Hence **every mode k ≠ 0 carries an O(1), log-periodic drift.** The full-lattice sum (both signs of the norm) is good in every mode.
4. **Any periodic weight on timelike shells contains odd characters (proved).** Suppose a function on (ℤ/q)^× (7 | q) is supported on {(m/7) = −1} and is even under m → −m. Since m → −m swaps the two classes, it vanishes. So the shifted Gamma factor always enters "periodic × polynomial" retarded weights. Whether combinations of odd twists can cancel the L-values in every mode at once is open; I suggest it is generically impossible.
5. **Checked** (`r52_D_1plus1_analog.out`; 64 rapidities over one full period, which is the exact Haar average):
   - sd_u of the retarded f ≡ 1 sum: 2.7e-2, 5.8e-2, 8.8e-2, 6.9e-2, 2.5e-2, 4.3e-2, 8.4e-2, 8.6e-2, 5.3e-2, 1.1e-2 at ℓ = 2…36. It does not decay; it is log-periodic.
   - Single shell m = 3: 0.02–0.25.
   - f = m: 0.02–0.16.
   - Full lattice: below 4e-12 for ℓ ≥ 3.

### 3.4 3+1: the same failure, checked
The retarded scale-free sums do not cancel (`r52_A_R77.out`; 12 frames, η ≤ 0.2, reach 77, 6.6e7 vectors; `r52_A_R50.out` for ℓ ≤ 5). Frame sd:

| ℓ | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|
| f ≡ 1, all past shells (T0) | 1.2e-3 | 7.9e-3 | 0.069 | 0.17 | 0.25 | 0.24 |
| f = m, all past shells (T1) | 0.017 | 0.12 | 0.16 | 0.11 | 0.055 | 0.31 |
| finite reference m ≤ 7 (Tfin) | 6.4e-3 | 0.053 | 0.18 | 0.34 | 0.46 | 0.46 |
| single shell m = 1 | 3.3e-3 | 0.041 | 0.060 | 6.4e-3 | 0.096 | 0.16 |
| full lattice (F) | 1.4e-12 | 3.5e-12 | 7.9e-12 | 1.3e-11 | 2.4e-10 | 3.2e-7 (reach) |

- **Reading.** T0's frame dependence is 0.15–0.55 times the finite-orbit kernel's and grows over ℓ = 4–8. The full lattice is flat to rounding.
- **Suggested.** The 3+1 mechanism is that of §3.3. The timelike (special-point) part of the theta lift alone has no trivial zeros at ½ ± ir/2 − k; only the timelike-plus-spacelike combination is modular. In 3+1, unlike 1+1, timelike and spacelike shells with the same |m| coexist, so no genus character separates them.
- **Caveats.** Only frames with η ≤ 0.2 were sampled, so the sd is a lower proxy for the 𝒳-rms. T0 and T1 are not mean-□ kernels; they are mechanism tests. Their means are ∝ □⁻² and □⁻³ (the retarded Green functions of □² and □³ in 4D; comparator).

---

## 4. Smooth, decaying infinite-orbit kernels with mean □

### 4.1 Checked: the exponent stays at about 3
The family is f_m = e^(−m/L²)·(c₀ + c₁x + c₂x² + c₃x³), x = m/L², on **all** shells. The coefficients solve the four mean conditions on the infinite sums, using the exact Siegel C_m (R4-1 A, m ≤ 200). The omitted tail Σ_{m>200}|g_m| is < 6e-32, 2e-16 and 1.4e-9 for L = 1.5, 2, 2.5. The per-realization operator uses R4-1's shell sums (M = 160, 40 frames, η ≤ 1), where |f_m| ≤ 1.1e-9 for m > 160 (`r52_C_infinite_smooth_recheck.out`).

| L | mean/□ at ℓ = 15 | rms rel dev ℓ = 6 / 10 / 15 | slope (ℓ ≥ 6) |
|---|---|---|---|
| 1.5 | 0.916 | 15.7 / 64 / 348 | +3.66 |
| 2.0 | 0.879 | 6.5 / 29 / 116 | +4.01 |
| 2.5 | 0.841 | 0.76 / 15 / 22.5 | +3.85 |

- These **are** infinite-orbit retarded kernels (weights on every shell, tending to zero), and they do not escape.
- The mean converges to □ like (a/ℓ)²·ln, as in R4-1.
- This independently reproduces R4-1's smooth-family finding on its unrefereed data, with my own weight construction.

### 4.2 The prefactor (suggested; conditional on the continuation of D_j)
Write f_m = Λ⁻³F̂(m/Λ), Λ = L². The Λ⁻³ comes from the normalisation (π/16)ΣC_m f_m m² ln m = −1.

D_j(s₀) = (1/2πi)∫F̂~(w)Λ^(w−3)L_j^T(s₀+w)dw,   L_j^T(s) := Σ_m Ψ_j(m)m^(−s).

- **If F̂ is smooth at 0 with F̂(0) ≠ 0** (the e^(−x)·cubic family): shifting the contour gives D_j(s₀) ≈ Λ⁻³F̂(0)L_j^T(s₀) + O(Λ⁻⁴). The relative drift then scales as L⁻⁶(ℓ/a)³. R4-1 fitted L^(−4.5) over L ≤ 4, which is consistent with an asymptotic L⁻⁶ but does not establish it.
- **If F̂ is flat at 0** (all derivatives zero, e.g. e^(−x−1/x)·cubic): D_j(s₀) = O(Λ^(−B)) for every B. This needs L_j^T to continue entire with polynomial vertical growth (true in 1+1 by §3.3; suggested in 3+1). This is R4-3's mesoscale escape (`R4-3_report.md:221-229`).
- In both cases **D_j(s₀) ≠ 0 generically**. In 1+1 with F̂(0) ≠ 0 it is ∝ L(iν_k, χ_kσ) ≠ 0 (§3.3). So the (ℓ/a)³ growth persists, and **no fixed law of this type meets PASS**. Only the prefactor can be pushed down.

---

## 5. Scope, hypotheses, outside realizations

**Proved here:**
- the Mellin closed form (§2.2);
- Proposition 1 for |f_m| = O(m^(−A)), A > 5, given R4-1's expansion (H4, unrefereed), Weyl's law and the sup-norm bound;
- Poisson exactness for all-vector polynomial kernels, and their δ-supported symbols (§3.1);
- the 1+1 genus fact and the odd-character lemma;
- 1+1 nonvanishing in every mode for f ≡ 1, mod RECALLED Hecke theory (class number 1, Gamma factors, functional equation, nonvanishing on Re s = 1).

**Checked:**
- 3+1: T0, T1, Tfin, a single shell and the full lattice for ℓ ≤ 9, 12 frames with η ≤ 0.2;
- 3+1: smooth mean-□ infinite kernels for L ≤ 2.5 and ℓ ≤ 15, 40 frames with η ≤ 1;
- 1+1: full-period sums for ℓ ≤ 36.

**Outside, open:**
1. **Non-smooth infinite weight sequences** solving the §2 identities: arithmetic, Hecke-adapted, or orbit-dependent within shells. Not excluded.
2. **Weights growing faster than polynomially, or distributional kernels.** Proposition 1 assumes A > 5. Polynomially bounded weights still have tube symbols (R3-1 referee), but the contour argument needs a continuation of D_j.
3. **Orbit-dependent weights.** Several Γ-orbits per shell give extra freedom; Proposition 1 holds with orbits in place of shells.
4. **Non-retarded kernels.** These have exact cancellation (§3.1) but no ordinary tube symbol (R3-1 Prop. R, refereed) and no □.
5. **Tensor or spinor operators; other cocompact arithmetic forms; curved realizations.**
6. **A kernel scale tied to ℓ.** That is not one law.

**Hypotheses used but not proved here:**
- R4-1's spectral expansion and its Haar/Palm identification (unrefereed).
- Siegel's C_m with class number one (R4-1, unrefereed; affects §4.1 only through the mean conditions).
- The theta-lift automorphy and continuation in 3+1 (RECALLED/suggested).

**Strong words.**
- "Exact" is used for the Mellin formula, the Poisson cancellation and the 1+1 genus fact.
- "Every mode" is used in §3.3 only (1+1, f ≡ 1).
- "Never meets PASS" in §4.2 is conditional on D_j(s₀) ≠ 0, which is proved only in 1+1.
- The fitted slopes (+3.66 to +4.01) are log-periodic and noisy. Read them as "≈ 3 or more", never as precise.

## 6. Prior art (counted once)

- **R4-1** (unrefereed): the finite-orbit theorem, the A_j(f) conditions (k = 0 only) and the smooth families. Here: k = 0, 1, 2; the exact Mellin form; infinite support; a recheck.
- **R4-3 §4.2** (unrefereed): the theta-lift/cusp suggestion and the mesoscale escape. Here: made precise via D_j, with the prefactor's Λ-dependence tied to F̂'s Taylor data.
- **R3-1** (refereed): Lemma A, and Prop. R (retarded laws converge only in the tube).
- **R3-3:** the one-hop per-realization drift is in band.
- **Packet:** `C3_exercise_G_graviton.md:95` records BD's per-history noise as Sorkin's reason for a non-locality scale.
- **Repository grep** (`docs/` and the packet; "Hecke" as a word, "Grössencharacter"/"Hecke character", "genus character", "theta lift"), run 14:15Z:
  - "Hecke" hits only Funk–Hecke (spherical harmonics) in `docs/ADMISSIBILITY_READABILITY_…_2026-09-13.md:248` and in PR8137 work-history files, which are unrelated, plus the R5-2 prompt itself (`TESTS.md:2879`).
  - "theta lift" hits only `TESTS.md:2879` and `agents/C5_R4-3_report.md`.
  - "Grössencharacter" and "genus character": no hits.
- **Comparators (RECALLED):**
  - Hecke (Grössencharacter L-functions; nonvanishing on Re s = 1);
  - the Siegel theta and Siegel–Weil; Kudla–Millson; Katok–Sarnak (CM-point and geodesic periods as coefficients of a single lift);
  - Sorkin gr-qc/0703099; Benincasa–Dowker 2010.

## 7. Price implications (named; none adopted)

- **A per-realization effective □ on LRL needs one of the following.** None is supplied by the axioms.
  - **(i)** An arithmetic miracle: infinitely many exact identities, three per automorphic mode, among the shell periods, with no known mechanism for retarded kernels.
  - **(ii)** Giving up retardation. This regains exact cancellation, but loses both the tube symbol (R3-1 Prop. R) and the d'Alembertian.
  - **(iii)** Accepting a mesoscale. Weights flat at m = 0 on a proper-time scale ℓ_k leave the (ℓ/a)³ growth with a prefactor that is suggested to fall faster than any power of ℓ_k/a. R4-3's numbers (`R4-3_report.md:225-229`) give a hierarchy of order 10²a at a = ℓ_P, untested.
  - **(iv)** An ensemble-only law, where only the mean is physical.
- **Consequence for set B′ (LRL).** The open escape listed at `TESTS.md:2878` narrows. Decaying smooth infinite-orbit kernels do not escape (checked), and scale-free ones fail by retardation (1+1 proved mod RECALLED; 3+1 checked). What remains is (i) or (iii).

## 8. Needs codex referee (only if anything here is used as a no-go)

1. Proposition 1: the bounds, the contour shift, the necessity for k = 1, 2, and the uniformity over j.
2. The 1+1 theorem: class number, the narrow-class character's infinity type, and L(iν, χσ) ≠ 0 via the functional equation.
3. Whether §4.2's D_j(s₀) ≈ Λ⁻³F̂(0)L_j^T(s₀) is right, including whether L_j^T continues in 3+1.
4. The reading: INCONCLUSIVE.
