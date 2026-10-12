# C5 R10-2 report: set B with box symbols. Does reflection positivity allow box-exact O(4) symbols on Euclidean Z⁴, and do they reduce the 11 graviton tunings?

**Author and status.** Claude Opus 5.5 probe. This is the same model family as the supervisor and every other C5 worker. The report is unrefereed. Run 2026-10-12, 17:50Z to about 18:35Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R10-2/`. Scripts and outputs are in `S/scripts/`. Each script runs in under 2 s with `OMP_NUM_THREADS=2`.
- `r102_rp_hankel.py` → `.out`: OS Hankel tests on k₄-slices (box, SLAC and NN laws, at 40 digits).
- `r102_slac_link.py` → `.out`: whole-zone SLAC slices under site and link RP, over the zone's c range; kernel shapes near π.
- `r102_cube_anisotropy.py` → `.out`, and `r102_cube_anisotropy_n.py` → `r102_cube_anisotropy_conv.out`: a proxy for the one-loop mass-form anisotropy, with grid convergence.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (cited `AX`).
- `TESTS.md` (cited `T`): C5 method and round 1 (`T:2302-2420`); round 2 pre-registration and results (`T:2433-2760`); R3-2 (`T:2757-2763`); R6-2 (`T:3331-3337`); R8-5 (`T:3807`); R9-9 refereed (`T:3939-3951`); R10 (`T:3955-3986`); K1 (`T:1663-1667`).
- Agents: `C4_K1_report.md` and `C4_K1_referee.md`; `C5_R2-1_referee_verdict.md`; `C5_R2-4_referee.md`; `C5_R6-2_referee_verdict.md`; `C5_R7-1_report.md` and `C5_R7-1_referee_verdict.md`. Scratch: `R6-1_report.md` §6 and `R9-9_report.md` §§0–2.

**Labels.**
- **proved**: a complete argument is given here.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: interpretation.
- **comparator**: literature. "Web-verified" means checked online at the level of an abstract or secondary sources. "RECALLED" means from memory.

---

## 0. In plain words

- **Reflection positivity and box symbols cannot coexist.** The question asked whether reflection positivity survives non-analytic box symbols. It does not.
  - Reflection positivity is what turns a Euclidean weight into a quantum theory.
  - It forces every two-point function, at fixed spatial momentum, to be an analytic function of the "time" momentum k₄ everywhere except k₄ = 0 and k₄ = π.
  - A box symbol is the continuum symbol on a box, glued smoothly to a periodic band outside it. The glue makes it non-analytic at the box edge, which lies strictly between 0 and π. So every smooth box law fails reflection positivity.
  - The failure is not small. Normalized OS minors are −0.13 (site) and −1.2 (link) for R7-1's matter profile. They are −0.010 and −0.011 for R8-5/R9-9's graviton profile.
- **Moving the glue does not help.** If exactness holds on any open box, analyticity carries the continuum formula across the whole k₄ zone. The result is the SLAC (sawtooth) form, which has a kink at the zone face k₄ = π.
  - A smooth law cannot have that kink (proved).
  - Under site reflection the kink has the forbidden sign (proved).
  - Under link reflection the whole-zone SLAC propagator passes every OS test I ran (checked). But reflection positivity then forces a gapless continuum of zero-energy "time-doubler" states at every spatial momentum (proved). That is R2-1's tower in a new form.
  - Even that survivor does not reduce the count. Its loops run over a cube, not a ball, so the W(B4)-only mass split comes back at the same size as the nearest-neighbour law's (checked proxy).
- **Without reflection positivity, the count falls but not to 2.** Use O(4) ball-supported vertices. The one-loop graviton self-energy is then exactly O(4) near q = 0 (proved; checked).
  - The registered count (K1's definition) falls from 11 = 3 + 8 to 5 = 2 + 3, plus Λ.
  - Only the TT-restricted count reaches "mass + Λ" = 2. The K1 referee ruled that restriction is not a physical floor.
  - So PASS is out of reach even in the non-RP class.
- **R2-4 (γ ≤ ½) binds unchanged.** Box symbols do not touch positivity or the reality of the source (proved; a one-line extension).
- **R2-1's analyticity premise is restored in set B by reflection positivity.** This holds per variable, off k_μ ∈ πZ. That closes the non-analytic escape that the box route used (proved for Euclidean two-point functions). Re-deriving Theorem T itself inside set B is suggested only.
- **Worker reading against the FIXED readings: FAIL (bounded).** The disjunct met is "OS positivity fails for box symbols in a stated class". The class is stated in §1 and §3. Referee required.

---

## 1. Hypotheses and classes (stated before any title)

- **H-E (Euclidean law).**
  - A probability measure on real or complex boson fields over Λ_L × Z.
  - Λ_L is the spatial torus L³; any L, and statements are per L. Time is the infinite axis.
  - The law is invariant under time translations and the time reflection θ.
  - It is reflection positive for one choice of reflection:
    - **site RP:** the plane passes through a slice, and E[θ(F)‾F] ≥ 0 for F measurable in τ ≥ 0;
    - **link RP:** the plane lies midway between slices, and the same inequality holds for F in τ ≥ 1.
  - For set B, W(B4) covariance makes every axis a reflection axis. It is used only in §3.3 and §4.
  - Grassmann (fermion) laws are covered by Lemma A and B through the standard Grassmann OS reconstruction (comparator: Osterwalder–Seiler 1978; Lüscher 1977; Menotti–Pelissetto 1987, web-verified via secondary sources). Lemma C is boson-only.
- **H-OS (standard reconstruction; comparator, RECALLED).** RP plus time-translation invariance give:
  - an OS Hilbert space;
  - a transfer operator T (one step) that is self-adjoint with spectrum in [−1, 1];
  - E[θ(A)‾ α_τ(B)] = ⟨A, T^τ B⟩ for observables A and B at slice 0, with τ ≥ 0 (site). Under link RP the same holds with a shift by one slice.
  - Under link RP with T ≥ 0 (as for Wilson actions, Lüscher 1977), the spectrum lies in [0, 1].
- **H-box (box symbols, the class under test).**
  - The symbol equals an O(4)-covariant continuum symbol on an open box |k_μ| < b with b < π. It is periodic outside the box and C¹ (in the R6-1/R7-1/R8-2/R8-5/R9-9 class, C^∞) at the zone face along the reflection axis.
  - Concretely, matter has D̃(k) = Σ s(k_μ)² + m², with R7-1's s (b = 2.0, b₂ = 3.1; `C5_R7-1_report.md`, §3).
  - The graviton TT sector uses R8-5/R9-9's d(q) (c₁ = 1, c₂ = 2.5; `R9-9_report.md`, §1).
- **H-SLAC (the limiting case, b → π).** The symbol is O(4) on the whole open cube (−π, π)⁴ and non-smooth at the faces.
- **Excluded or outside realizations, not addressed:**
  - non-RP weights (a price, §6);
  - continuous Euclidean time Z³ × ℝ (not set B);
  - RP for reflections not orthogonal to a lattice axis (suggested to work the same);
  - whole-zone SLAC fermions (the jump in the k₄γ₄ component is not tested);
  - interacting laws beyond the perturbative corollary A2;
  - the graviton's nonlinear sector;
  - two loops.

## 2. Prior art (each counted once)

- **R6-1 §6** (scratch `R6-1/R6-1_report.md:156-160`, unrefereed) gives a *suggested* no-go for set B. It runs: gap ⇒ Laplace transform ⇒ strip analyticity in k₄; W(B4) and Hartogs ⇒ joint analyticity; the weak step is the pole surface. **This report upgrades and corrects it:**
  - no gap and no Hartogs are needed;
  - a one-variable argument suffices;
  - the smooth box class is closed (proved);
  - whole-zone SLAC is **not** closed by RP alone under link reflection (checked).
- **R2-1 referee** (`C5_R2-1_referee_verdict.md:3,5`; `T:2752`). The Gaussian time-blocked perfect-action covariance fails OS minors (−2.25e-3, −1.83e-4). Same diagnostic, different law; counted once.
- **R2-4** (`T:2728-2735`; `C5_R2-4_referee.md:7-9`). Lemma W, a ≤ 1/3 ⇒ γ ≤ ½. The free linearized-curvature two-point function is RP (`C5_R2-4_referee.md:31`).
- **K1** (`T:1663-1667`; `C4_K1_referee.md:3,9`). The W(B4) forms are 3 mass + 9 kinetic. The O(4) subspace is 4 kinetic, with EH the unique gauge-invariant direction. Codimension 11. The TT rank of 5 is not a physical floor.
- **R6-2** (`T:3336`): O(4) counts 2 + 4, confirmed. **R3-2** (`T:2757-2763`): the analogous drop from 11 to 5 for LRL was not accepted as "≤ mass + CC".
- **R7-1, R8-2, R8-5, R9-9** (`T:3939-3951`): the box route on Z^d × ℝ.
  - R9-9's refereed Theorem T: the TT speed anomaly is carried by the edge.
  - Its INV control protects the speed but leaves one mass number (`R9-9_report.md:§0`).
- **Comparator, web-verified (abstract): K. Usui, arXiv:1201.3415 (2012).** Lattice RP, translation invariance, hermiticity and polynomial boundedness give a Källén–Lehmann representation with positive spectral density; the paper also finds that an overlap scalar boson model violates RP. Lemmas A and C are one-variable consequences of the same structure; the box and SLAC results below are not in that abstract.
- **Comparator, web search.** I found no source that settles RP for the SLAC derivative. Non-local, non-covariant counterterms for SLAC fermions coupled to gauge fields (Karsten–Smit) are confirmed in secondary sources. So "SLAC violates RP" is **not** a literature fact I can cite. My numerics say site-RP fails, and link-RP passes for the free scalar.
- **Repository search.** I grepped TESTS.md and the agents for "reflection positiv", "OS", "Hankel" and "SLAC". Beyond R2-1, R2-4, R6-1 §6 and K2's "coupled RP unproved", I found no prior RP analysis of box or SLAC symbols.

---

## 3. Results: reflection positivity

### 3.1 Lemma A (RP ⇒ analyticity off πZ). Proved, given H-OS.

**Claim.** Let A and B be observables localized in a finite time slab, at fixed spatial momentum k, with finite second moments. Let C(τ) = E[θ(A)‾ α_τ(B)]. Its Fourier series F(θ) = Σ_τ C(τ)e^{−iθτ}, restricted to T¹ ∖ {0, π}, is a real-analytic function. Under link RP with T ≥ 0, it is analytic on T¹ ∖ {0}.

**Proof.**
- For τ beyond the slab width w, C(τ) = ⟨Â, T^{τ−w′}B̂⟩ = ∫_{[−1,1]} λ^{τ−w′} dν(λ). Here ν is a complex measure with total variation at most ‖Â‖‖B̂‖ (spectral theorem). The τ < 0 side is the same with the roles exchanged.
- So F = (trigonometric polynomial) + ∫dν(λ) e^{−iθw″}/(1 − λe^{−iθ}) + (mirror).
- For real θ₀ ∉ πZ, |1 − λe^{−iθ}| ≥ |sin θ₀|/2 uniformly in λ ∈ [−1, 1] and in θ within a small complex disc around θ₀.
- Hence the integral is holomorphic there, by dominated convergence.
- The atoms at λ = ±1 give distributions supported at θ ∈ πZ only. ∎

**Remarks.**
- No gap, clustering or W(B4) is used.
- Positivity of ν is not used. Only the OS Hilbert space and a self-adjoint contraction T are needed. So the lemma applies to every pair of time-local observables, including gauge-invariant ones and components with time indices.
- **Corollary A1 (direct exclusion of the box class; proved).** Suppose, at some spatial k, a time-local two-point function is non-analytic at some θ₀ ∉ πZ. Then the law is not RP.
  - For a Gaussian law with C^∞ symbol D̃ > 0, the covariance slice is 1/D̃(θ, k).
  - R7-1's s(θ) is non-analytic at θ = b = 2.0. On (−b, b), s² = θ². On (b, b₂), s² − θ² = −(1 − ρ)(θ − sin θ)(s + θ) ≠ 0, so s² cannot be analytic at b (identity theorem). The same holds for 1/D̃.
  - The same argument applies to d(q) at c₁ = 1 and c₂ = 2.5.
  - **So every R6-1/R7-1/R8-2/R8-5/R9-9-type box law, placed on Euclidean Z⁴ with any axis as Euclidean time, is not reflection positive.**
- **Corollary A2 (perturbative interactions; proved under a stated hypothesis).** Suppose a family μ_g has time correlators C_g(τ) → C_0(τ) for every τ as g → 0, with C_0 a Gaussian box law. Then μ_g is not RP for all sufficiently small g. Reason: a finite OS Hankel minor of C_0 is strictly negative (§3.4), and finite minors are continuous.

### 3.2 Lemma B (box-exactness propagates across the zone; smoothness fails at the face). Proved.

**Claim.** Assume:
- at fixed spatial k, F = F_k is C¹ on T¹ and RP-analytic (Lemma A);
- on (−b, b) ∖ {0}, F = h, where h is real-analytic on a neighbourhood of [−π, π].

Then:
- F = h on all of (−π, π) (identity theorem on (0, π) and (−π, 0) separately);
- C¹ across the periodic seam gives h′(π) = h′(−π);
- if F is C^∞, then h^{(n)}(π) = h^{(n)}(−π) for every n. If h is analytic on ℝ, it is therefore 2π-periodic.

**Corollary B1 (scalar O(4); proved).** Take h(θ) = g(θ² + c), with g real-analytic and c = |k|² + m² ranging over an open interval I (spatial k in the box). Then h′(π) = −h′(−π) = 2πg′(π² + c). So C¹ forces g′ = 0 on π² + I, and g is constant.

**Corollary B2 (any O(4)-covariant tensor; proved).** Let H(k) be O(4)-covariant and real-analytic on ℝ⁴. This holds for massive symbols, and for massless ones on the connected set k ≠ 0. Suppose H is periodic in k₄ for an open set of spatial k.
- By the identity theorem, H(k + 2πe₄) = H(k) on ℝ⁴.
- Covariance gives H(k + 2πRe₄) = ρ(R)H(R⁻¹k + 2πe₄)ρ(R)⁻¹ = H(k) for every R ∈ SO(4).
- So H is invariant under all translations of length 2π, hence under all translations. It is constant, i.e. a pure contact term.

**Consequence (proved).** No RP law has a C¹ (scalar) or C^∞ (tensor) two-point function of time-local observables that is O(4)-covariant and non-constant on any open k₄-interval at an open set of spatial momenta. This holds regardless of what the symbol does outside the box. Exact O(4) on an open set is impossible for smooth RP laws.

### 3.3 Whole-zone SLAC: the only RP-compatible exact-O(4) form, and what it costs

- **Forced form (proved).** With W(B4), apply Lemma B axis by axis, without smoothness. Exactness on an open box forces the two-point function to be h(k) on the whole open cube (−π, π)⁴. That is the whole-zone SLAC form: the box must be the whole zone.
- **Lemma C (site RP forbids the SLAC kink; proved).**
  - Under site RP, ν ≥ 0 on [−1, 1] and F = ∫dν P_λ, with P_λ the Poisson kernel.
  - Split ν at λ = −1 + δ. The part on [−1 + δ, 1] is analytic at π.
  - The part S on [−1, −1 + δ) is a positive mixture of P_λ(π + φ), each maximal at φ = 0. So S(φ) ≤ S(0), with S(0) finite by Fatou.
  - The SLAC slice has F(π + φ) − F(π) = −h′(π)|φ| + O(φ²), with h′(π) = 2πg′(π² + c) < 0 for any continuum Källén–Lehmann (Stieltjes) g.
  - That is an upward V, which contradicts S(φ) ≤ S(0). ∎
  - Checked: site minima are −0.0385 for the scalar and −0.0232 for the TT graviton (`r102_rp_hankel.out`). They are −0.0011 to −0.050 across c ∈ [0.0025, 29.86] (`r102_slac_link.out`).
- **Link RP allows the kink.** For λ < 0 the link kernel 2Re[e^{iθ}/(1 − λe^{iθ})] is a *dip* at θ = π: −200 at φ = 0 and +0.78 at φ = 0.3, for λ = −0.99 (checked, `r102_slac_link.out`). So the upward V has the allowed sign.
  - Checked: the whole-zone SLAC slices 1/(θ² + c) pass the link-RP Hankel test [G(1+i+j)] ⪰ 0 up to N = 14, at 50 digits, for all six c values. The minimum eigenvalue stays positive and decays geometrically, as moment Hankels do.
  - They fail [G(2+i+j)] ⪰ 0, at −0.0114 to −0.0129. So T is not positive.
  - Not proved: link RP of the whole-zone SLAC Gaussian. This is a numerical finding at finite N.
- **Lemma D (the forced gapless continuum; proved).**
  - Suppose any RP law (site or link) has F = h on (−π, π) with h′(π) ≠ 0.
  - Then the OS spectral measure at that spatial momentum has support accumulating at λ = −1.
  - Reason: if supp ν ⊂ [−r, 1] with r < 1, the kernel is analytic at θ = π, contradicting the kink.
  - Near λ = −1, |λ| = e^{−E} with E → 0. These are zero-energy states (for T²) with alternating sign in Euclidean time ("time doublers").
  - With W(B4) this holds at **every** spatial momentum in the zone, for massive matter too. For the dip kernel, an |φ| kink needs density ∝ (1 + λ), i.e. a spectral weight ∝ E near E = 0 (suggested; leading-order matching only).
  - Reading: a gapless, momentum-independent continuum created by the matter field at the percent level of its norm. There is no mass gap for "massive" SLAC matter. This repeats R2-1's lesson (`C5_R2-1_referee_verdict.md:3`): exactness on an open set of momenta costs infinitely many states per momentum. There they are a pure-point ladder; here they are a gapless continuum.

### 3.4 Numbers (checked; `r102_rp_hankel.out`)

Setup: fixed spatial momentum k = (0.3, 0.2, 0.1); m = 0.5 for the scalar; massless TT graviton. Each entry is the normalized minimum eigenvalue (min/max) at N = 9. "site" is the Hausdorff pair [G(i+j)] and [G(i+j) − G(i+j+2)]; "link" is [G(1+i+j)].

| k₄-slice of the two-point function | site H0 | site H2 | link G1 | verdict |
|---|---|---|---|---|
| NN scalar (control) | −9e-42 (zero) | −5e-41 (zero) | −3e-41 (zero) | RP (rank-1 Hankel) |
| R7-1 box scalar s(k), b = 2.0, b₂ = 3.1 | **−0.127** | **−0.161** | **−1.18** | not RP |
| R8-5/R9-9 box TT graviton d(q) (gauge-invariant spatial-TT h) | **−0.0096** | **−0.023** | **−0.0109** | not RP |
| whole-zone SLAC scalar | **−0.0385** | **−0.0517** | +8e-14 (PSD) | site no, link yes (to N = 14) |
| whole-zone SLAC TT graviton | **−0.0232** | **−0.0424** | +5e-14 (PSD) | site no, link yes |
| SLAC + 0.05θ² contact | −0.0056 | −0.0087 | −0.093 | not RP |

- Violations are visible already at N = 2 and are stable in N, so they are not round-off. The NN control is zero to 40 digits.
- The box-scalar G(τ) alternates in sign: 0.161, 0.476, −0.084, 0.227, … No positive mixture of λ^τ does that with this pattern.

---

## 4. Results: the tuning count (tree level and one loop)

**Tree level.**
- **Non-RP box class.** Choose the box graviton symbol EH-shaped (R9-9's tree level is exact, `T:3940-3945`). That needs 0 graviton tunings at tree level (proved by construction).
- **RP class.**
  - The box graviton symbol itself is excluded (Lemma A; table row 3, a gauge-invariant observable).
  - Whole-zone SLAC graviton: allowed under link RP only, with Lemma D's continuum.
  - Analytic RP symbols, such as K2's free lattice Fierz–Pauli action with its exact gauge identity (`T:1669-1672`), need nothing at tree level, as before.

**One loop, non-RP class: C^∞ box symbols plus O(4) ball-supported vertices.**
- **Exactness (proved).** The loop integrand is O(4)-covariant on its support, which is a ball inside the box. So Π^{μνρσ}(q) is exactly O(4)-covariant for |q| small enough that p + q stays in the box.
- **Check (proxy).** R := ∫v₁⁴G²/(3∫v₁²v₂²G²) gives R − 1 = +1.6e-5, +1.1e-5 and −1.3e-6 at n = 40, 56, 72: grid error only.
- **Forms.** The W(B4) forms collapse to O(4): 2 mass forms (h:h, (tr h)²) and 4 kinetic forms (F1–F4), with EH the unique gauge-invariant one (refereed counts `C4_K1_referee.md:3`, `T:3336`).
- **Registered count (K1's definition): 2 + 3 = 5, plus Λ.** Down from 11. Whether all 5 are generated is not computed here (suggested: the ball form factor breaks the momentum-shift Ward argument, as in R9-9's INV control, `R9-9_report.md:§0`).
- **TT-restricted count: 1 TT mass + 0 speed, plus Λ = 2.** This equals the PASS number "mass plus Λ", but K1's referee ruled the TT restriction is not a physical floor (`C4_K1_referee.md:3,9`). With exact O(4), the 3 non-EH kinetic forms propagate vector/scalar modes unless tuned to EH, and the mass forms must take the Fierz–Pauli ratio. That gives a physical count of 5 + Λ (comparator, RECALLED: Fierz–Pauli/van Nieuwenhuizen ghost-freedom). The same verdict was given for R3-2's 11 → 5 (`T:2757-2763`).

**One loop, RP class.**
- **Smooth box laws:** excluded (§3).
- **Whole-zone SLAC (link-RP survivor).** Its loops run over the cube. The O(4) integrand on a cubic domain regenerates the W(B4)-only split: R − 1 = −0.256 (checked; stable for n = 40–72). Compare NN at −0.465 and the C^∞ box with edge modes at −0.193.
  - So the count does not fall below the W(B4) structure on this route. The M1/M2 split is checked as a proxy; the full 11 is suggested (K1-type generation).
  - Adding ball-supported vertices makes the vertex functions non-analytic in the external momenta off πZ. I expect that to break RP at O(g²) (suggested). Lemma A applies to each finite g, but carrying it to the O(g²) coefficient needs uniform bounds I did not prove.

**Summary of the count.**

| class | RP? | one-loop count (registered) | TT-restricted |
|---|---|---|---|
| set B, W(B4), analytic (K1) | yes | 11 (+Λ) | 5 (+Λ) |
| smooth box symbols + O(4) ball vertices | **no** (Lemma A/B, proved) | 5 (+Λ) (forms exact; generation suggested) | 1 (+Λ) |
| whole-zone SLAC, no ball vertices | link: checked numerically; site: no (proved) | no O(4) reduction (proxy R − 1 = −0.26, checked) | — |
| whole-zone SLAC + ball vertices | expected no (suggested) | 5 (+Λ) | 1 (+Λ) |

---

## 5. Do R2-1 and R2-4 bind?

- **R2-4 (γ ≤ ½): binds unchanged (proved, small extension).**
  - Lemma W needs only that the second-variation source kernel S_ij have a Fourier transform bounded near p = 0, so it cannot change a 1/p² residue (`C5_R2-4_referee.md:7`).
  - Any summable kernel gives a bounded, continuous transform. Box kernels decay super-polynomially (`C5_R7-1_report.md`, §4.2).
  - So for any positive Euclidean box weight with real sources, the trace projector still forces a ≤ 1/3, γ ≤ ½ (`T:2730`).
  - Box symbols change the tuning count, not positivity. Set B's γ problem is independent of the symbols.
- **R2-1 (Theorem T, tower).** The binding is partial.
  - **The escape is closed (proved).** The box route's escape from Theorem T was non-analytic symbols. R2-1's added premise is globally analytic periodic one-particle matrices (`C5_R2-1_referee_verdict.md:3`; R7-1 W2). In set B, Lemma A restores Euclidean analyticity in each k_μ off πZ, and Lemma B closes the smooth-box escape, both for Euclidean two-point functions.
  - **Re-deriving Theorem T itself inside set B is suggested only.** It needs the Euclidean-to-one-particle pole-surface step (R6-1 §6's weak step). It also needs the determinant argument redone with analyticity cut by the hyperplanes k_μ ∈ πZ, where the cells are not connected.
  - **The surviving SLAC route pays a tower-like price** (Lemma D, reading).
- **R2-5 (RP plus permanence): not addressed.** Its theorem covers nearest-neighbour classical slice laws, and box laws are outside that class.
- **O1 (hypercubic protection of dimension-4 matter operators): untouched.**

---

## 6. Reading against the FIXED readings (`T:3984-3986`)

- **PASS: not met.**
  - In the RP class, smooth box symbols are excluded (proved).
  - Whole-zone SLAC survives link RP (checked) but gives no O(4) loop reduction without non-analytic vertices.
  - In the non-RP class, the registered count is 5 + Λ, not ≤ 2. Only the TT restriction gives 2, and it is not accepted as a physical floor.
- **FAIL: worker reading FAIL (bounded); referee required.** Disjunct: "OS positivity fails for box symbols in a stated class". The stated class:
  - translation-invariant, site- or link-RP (boson or Grassmann) Euclidean laws on Λ_L × Z;
  - any two-point function of time-local observables that, at fixed spatial momentum, is non-analytic at some k₄ ∉ πZ (Lemma A).
  - This class contains every smooth plateau box symbol of R6-1/R7-1/R8-2/R8-5/R9-9 along any W(B4) axis, and perturbative interactions around them (Corollary A2).
  - More strongly, it contains any C¹ (scalar) or C^∞ (tensor) two-point function that is exactly O(4) and non-constant on an open set of momenta (Lemma B), regardless of where the non-analyticity is placed.
- **Outside the class** (if the referee requires it, the strongest reading for this corner is INCONCLUSIVE):
  - whole-zone SLAC symbols (b = π, non-smooth faces) under link RP;
  - whole-zone SLAC fermions.
  - For the corner I prove that RP forces a gapless time-doubler continuum at every momentum (Lemma D), and I check that its cube loops do not reduce the count.
- **Expectation versus outcome.** R6-1 §6 had suggested this closure via gap and Hartogs. The proof here is simpler and stronger for smooth symbols. It is weaker than R6-1's wording for whole-zone SLAC, which RP alone does not close under link reflection.

**Prices, named, not adopted.** Keeping box symbols in set B costs one of the following.
- **(P-RP):** give up reflection positivity of the Euclidean weight. That gives up the OS Hilbert space and physical probabilities for the Admissibility distribution in set B (`AX:57-73`; R2-4's reading).
- **(P-SLAC):** whole-zone SLAC in all four directions. That brings 1/r² tails (RD) and non-smooth zone faces, link RP only, a forced gapless zero-energy continuum at every momentum, and still no count reduction unless vertices are added that are expected to break RP.

## 7. Strong-word check

- **"Excluded" or "not RP".** These are proved for the stated class, relying on standard OS reconstruction (H-OS; comparator, RECALLED). Hankel numbers illustrate; they are not the proof.
- **"Exactly O(4)" for Π (non-RP class).** This is proved for |q| below the ball-to-box margin; it is not about generation of all 5 forms.
- **"Link RP passes" for SLAC.** This is checked for finite Hankel sizes N ≤ 14 at six c values. It is not proved.
- **"Gapless continuum" (Lemma D).** Accumulation of spectral support at λ = −1 is proved. The density ∝ E is suggested, from leading-order matching only. The physical unacceptability is a reading.
- **"Count 5".** This is K1's registered operator-codimension count under O(4) (refereed form counts). It is not a proved generation statement.
- **Physical sizes:** none claimed.
- **Fermions.** Lemmas A and B are claimed through the Grassmann OS reconstruction; this is RECALLED and not rechecked numerically here.
