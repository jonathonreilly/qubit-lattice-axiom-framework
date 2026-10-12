# C5 R16-12 report: W7's fork at degree 3. Does the algebra force (α), or allow (β)?

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. **Unrefereed.** Ran 2026-10-12 from 23:28Z to about 23:56Z. No repository file was edited. No downloads and no web lookups; literature items are RECALLED.

**Scratch.** `S/` = `.../scratchpad/C5/R16-12/`. Each script runs in under 2 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r1612_degree3.py` / `.out`: the degree-3 Killing-sector equations, solved per matter mode.
- `S/scripts/r1612_controls.py` / `.out`: sign-flip control, rigidity (null space), strong-closure test, factorisation.
- `S/scripts/r1612_population.py` / `.out`: edge-quantum Boltzmann factors (for (c), reading only).
- `S/scripts/sublum_copy.py`: R14-1's S(b)/G(b) symbols. It is byte-identical to `scripts/C5/R14-1/sublum.py`.
- `S/recheck/`: the archived R16-8 and R12-1 runners, rerun.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS` is `P/TESTS.md`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full.
- `vR16-8` = `P/agents/C5_R16-8_referee_verdict.md`. `vR16-8full` = `scratchpad/C5/ref_R16-8/R16-8_referee_verdict.md`.
- `vR12-1` = `P/agents/C5_R12-1_referee_verdict.md`. `vR16-5` = `P/agents/C5_R16-5_referee_verdict.md`.

**Read.**
- `AX`, in full.
- `TESTS`:
  - the C5 method (`:2302-2320`);
  - R12-1 and its verdict (`:4335-4348`, `:4477-4485`);
  - R13-4 and its verdict (`:4644-4664`, `:4771-4777`);
  - R14-1's verdict (`:4808-4813`);
  - R16-5 and its verdict (`:5130-5149`, `:5437-5446`);
  - R16-8 and its worker and referee summaries (`:5341-5358`, `:5514-5525`, `:5587-5591`);
  - this item (`:5527-5549`).
- `P/agents/`:
  - `C5_R16-8_report.md` in full;
  - `vR16-8`, and also `vR16-8full`;
  - `C5_R12-1_report.md` in full, and `vR12-1`;
  - `C5_R16-5_report.md` §§0–2, and `vR16-5`.

**Rechecks of archived runners** (all reproduce):
- `scripts/C5/R16-8/r168_kernel.py`: its `.out` is byte-identical.
- `scripts/C5/R12-1/r121_matter_bilinear.py` and `r121_completion_and_gravity.py`: stdout is identical to the archived `.out`.
- `scripts/C5/R16-8/r168_jets.py` was rerun once from its archive path. It writes its `.out` beside itself, so it overwrote the archive copy. The new output was byte-identical, and `git status` was clean afterwards. All other reruns were made in `S/recheck/`.

**Labels.**
- **proved:** complete under the stated hypotheses; unrefereed.
- **checked:** numerics here.
- **suggested:** argued, not proved.
- **reading:** interpretation.
- **comparator:** literature, RECALLED.

---

## 0. In plain words

1. **R16-8's dangerous term is repairable, and the repair already exists.** R16-8 asked who cancels the non-local term κ³∫ξE·(B∗Ȯ_D) that keeps the momentum constraint true in time. Answer: an h-linear singular term in the momentum constraint, as in (β). It needs no new term in the Hamiltonian.
   - The only Hamiltonian input it uses is the ordinary matter–gravity stress coupling ½h_ijT^ij. Its value is already fixed at degree 2.
   - The check has no free parameter, and it holds identically (proved; checked). With the opposite sign of the stress coupling it fails (checked).
2. **The (β) term is the JJ repair.** R16-8 asked whether (β) is compatible with the JJ (translation–rotation) Killing jets. It is the same object: the divergence of the forced h-term is exactly what cancels the matter's translation–rotation defect (proved; checked to 1e-9).
3. **Subluminality is needed.** The helicity-2 part of the repair has the denominator |q|² − (q·v)².
   - For every edge mode of R14-1's subluminal S(1.4) and G(1.4) laws this denominator is positive.
   - For the superluminal literal box (|v| = 3.6) it vanishes on a cone. That is a Cherenkov resonance, and it forces a non-local Hamiltonian (proved; checked).
4. **The wall is in the boost, not the translation.** The standard algebra also demands {H[x_b], H[1]} = D[e_b] at degree 3, the center-of-energy theorem dK/dt = P.
   - The total momentum now contains the non-local cross term, so the boost charge must contain its time integral.
   - With a quasi-local Hamiltonian this forces a kernel X_T = 2i b_T/(q·v) in the boost generator. It blows up on the whole plane q ⊥ v. In real space it is the Coulomb field of the moving defect integrated along its entire straight world-line.
   - So in the stated class 𝒞 (homogeneous kernels bounded on the sphere), no completion with a quasi-local Hamiltonian exists. (β) as registered fails, and so does the variant with ∂N-type singular terms in the Hamiltonian constraint. This is proved at leading order, unrefereed, and checked over 5 decades.
5. **But "(α) vs (β)" is not an invariant question.** The (β) correction factorizes as Φ_c = δ_c·Ξ, where δ_c is the "fake translation" mismatch of the lattice momentum. Hence Φ_c = {P⁰_c, W} for one singular W.
   - So the (β) system is the canonical image, by the non-local map e^W, of a system with the bare momentum and a non-local Hamiltonian.
   - Which generator looks non-local therefore depends on the variables chosen. That is the referee's "canonical relocation" made explicit (proved at first order; checked).
   - Only an observable invariant under the completed constraints can decide physical locality, and none is built.
6. **Reading: OPEN.**
   - Not QUASI-LOCAL: no full degree-3 completion. Translations close (weakly, at leading order); boosts do not, in 𝒞.
   - Not NON-LOCAL: Theorem B3 is an unrefereed, class-bound and presentation-bound no-go for (β). (α) itself is not constructed, and no bounded invariant observable or distant-response size exists.
   - Any effect needs lattice-momentum quanta, which are Boltzmann-suppressed by 10^(−3.3e31) at T_CMB (reading).

---

## 1. Hypotheses and the class 𝒞 (stated before any title)

- **H-grade (R12-1, `C5_R12-1_report.md:47-54`).**
  - Gravity fields (h, E) have degree 1 and matter bilinears degree 2.
  - The κ³ terms of the registration are the degree-3 parts of the brackets, linear in matter bilinears and linear in (h, E).
- **H-conv (fixed once; calibrated by the continuum).**
  - {h_ij(x), E_kl(y)} = δ.
  - C_s[N] = ∫N R1(h) + ∫N[E·E − ½(trE)²] + ½∫N h·𝒦h + T00[N] + (deg 3) + ….
  - R1 = ∂_i∂_jh_ij − ∇²trh, i.e. R1(q) = −s(q)·h(q) with s_ij = q_iq_j − |q|²δ_ij.
  - C_j[ξ] = ∫Kill(ξ)·E + P^m[ξ] + P^g[ξ] + (deg 3) + ….
  - 𝒢E := 2E − (trE)I, so ḣ = 𝒢E. 𝒦 := the linearized Einstein tensor, so Ė = −𝒦h. Its TT eigenvalue is |q|²/2, so the graviton has ω_g = |q|.
  - With these normalizations, {C_s[N], C_s[M]} = C_j[M∂N − N∂M] holds:
    - at degree 1 (gravity seed: computed, 2α = 2 with α = 1);
    - at degree 2 for matter with P = ∂(ε²/2).
  - Also {C_j[e_c], C_s[N]} = −C_s[∂_cN] (continuum calibration).
  - **Standard (undeformed) HDA** throughout.
- **H-mat.** Free, number-conserving, one-band separable matter in d = 3:
  - m = 0.3; R14-1's S(1.4) and G(1.4) (whole-zone v_max 0.9927 and 0.9939, refereed in `vR16-8full:134-140`); the L-box(2.0) (v_max 4.121) as a superluminal control;
  - current-aligned momentum P = ∂(ε²/2) = εv (R16-8 Lemma P);
  - defect Δ_cb = ε(∂_bP_c − δ_bc).
- **H-lead (leading order in the smearing momentum q).** Matter bilinears are treated in their leading gradient (Lie–Poisson / Vlasov) form: matter bilinear ↔ ∫a(x,k)f(x,k), with {∫af, ∫bf} = ∫{a,b}f.
  - This is exact for the leading homogeneous symbols, which are all that decide singular (non-analytic) structure at q → 0.
  - Off-forward placements (Lemma S) enter only at subleading orders.
  - Per matter Fourier mode (q, k): ω := q·v(k) and δ_c := q·Δ_c(k)/ε(k), the fake-translation mismatch {P^m_c, ·} − (true translation).
- **H-comp.** Degree-3 completions have the R12-1 form (`C5_R12-1_report.md:70-73`): (h or E)-linear × matter-bilinear, with translation-covariant symbols.
  - In C_j[e_c]: Φ_c = Σ_{q,k}[E(−q)·B_c + h(−q)·A_c] f(q,k).
  - In H = C_s[1]: H_int = Σ[E·τ + h·σ]f.
  - In C_s[N]'s first lapse-momentum jet (the boost generator): K_b^sing = Σ[E·X_b + h·Y_b]f.
- **Class 𝒞.**
  - Every singular symbol is, at leading order, homogeneous in q with angular dependence **bounded on the sphere** (Calderón–Zygmund-type kernels such as 1/r^{d−1}, 1/r^d).
  - **(β) means H = C_s[1] quasi-local**, i.e. τ and σ are C^∞ in q.
  - Closure is **weak**: residuals proportional to the linear constraints are allowed, which covers field-dependent lapse/shift and matter-dependent structure functions. Concretely, E-coefficients modulo L = Im Kill(q) (the q̂q̂ and vector-longitudinal parts) and h-coefficients modulo T = Im s(q) (the transverse trace I − q̂q̂).
  - The strong version is also tested (§4.4).
- **Excluded, and not covered below:**
  - pairing and the SLAC/P-pf1 matter (as registered);
  - pair-creating and interacting matter;
  - nonlinear gravity beyond the degree-3 bookkeeping;
  - degree-4 singular terms acting through cutoff shells (see §5.3);
  - auxiliary or second-class formulations;
  - deformed algebras;
  - qubit gravity; Λ;
  - non-Killing smearings at degree 3. Only the Killing (global-charge) sector is solved. By R12-1's Theorem K logic it carries the singular content, but that is a local-germ statement (`vR12-1:3-15`).

## 2. Prior art (each counted once)

- **R16-8 and its verdict.**
  - Lemma D's uncancelled term and the (α)/(β) candidates (`C5_R16-8_report.md:246-259`).
  - The verdict confirms the term but not the dichotomy. It lists the missing classes: higher momentum-constraint terms, structure functions, constraint-proportional cancellations, canonical relocations and auxiliaries (`vR16-8:9`; `vR16-8full:95-108`).
  - Lemma B's kernel: s·B = D, 1/r² (`C5_R16-8_report.md:167-180`; confirmed at `vR16-8full:14-24`).
  - Lemma P holds only as a Killing-jet/local-germ statement: "no singular scalar completion is forced by the checked Killing jets" (`vR16-8full:41-56`).
  - Physical non-locality needs a bounded observable invariant under the completed constraints (`vR16-8:17`; `TESTS:5587-5591`).
- **R12-1 and its verdict.** Theorem K reduces degree-2 closure to Killing jets, as a local germ only. Off-box jets need a degree −1 completion (`C5_R12-1_report.md:105-146`; `vR12-1:15`).
- **R13-4.** The criterion: a bounded gauge-invariant observable at distance r (`TESTS:4644-4664`). (ii) is OPEN (`TESTS:4776`).
- **R16-5's grading lemma.** The identity separates by particle-number grade, so pair terms cannot repair number-conserving defects (`vR16-5:19,25`). Used in §5.3.
- **RFW's first-jet obstruction** (`TESTS:2263-2300`, as cited by R16-8 at `C5_R16-8_report.md:117`): regular completions cannot absorb off-box Killing defects. It is used only through B_T.
- **R14-1:** the subluminal S/G laws and A ≤ 0 (`TESTS:4808-4813`).
- **Comparators (RECALLED):**
  - the ADM linearization;
  - the center-of-energy theorem (dK/dt = P);
  - hidden momentum (field cross terms);
  - Cherenkov resonance;
  - first-order dressing by energy denominators;
  - Coulomb-gauge QED, whose boosts act with compensating non-local gauge transformations while the physics stays local.

---

## 3. (a) The degree-3 brackets: every term carrying B

Write Φ_c = Φ_c^E + Φ_c^h, with Φ^E = Σ E·B f (B singular, s·B fixed at degree 2) and Φ^h = Σ h·A f.

**{D, H} = {C_j[ξ], C_s[N]}, degree 3** (target: −C_s^{(3)}[ξ·∂N]).
1. {Φ^E[ξ], T00[N]} carries **B**. At N = 1 it is R16-8's term, which in H-lead reads −iω E·B f (proved).
2. {Φ^E[ξ], ½∫N h𝒦h} carries **B**: −h·𝒦(NB) f (h-linear).
3. {Φ^h[ξ], ∫N[E·E − ½(trE)²]}: +E·𝒢(NA) f.
4. {Φ^h[ξ], T00[N]}: −iω h·A f.
5. {P^m[ξ] + P^g[ξ], H_int[N]}: +iδ (E·τ + h·σ) f, the fake-translation mismatch of the regular couplings. It is zero on the box.
6. {G(E)[ξ], C_s^{(4)}[N]} and {C_j^{(4)}[ξ], R1[N]}: zero for ξ = e_c and N = 1 (Kill(e_c) = 0, 𝓡*1 = 0), up to the shell terms excluded in §1.

**{H, H} = {C_s[N], C_s[M]}, degree 3** (target: C_j^{(3)}[M∂N − N∂M] + h-structure-function terms).
- No B appears on the left side when C_s has only regular completions.
- **B appears on the right side** through C_j^{(3)}[M∂N − N∂M] ∋ Φ^E. At (N, M) = (x_b, 1) this is Φ_b. This is the source of Theorem B3.

**{D, D} = {C_j[ξ], C_j[η]}, degree 3.**
- {Φ^E[ξ], P^m[η] + P^g[η]} carries **B**: the fake-versus-true transport of B.
- The right side C_j^{(3)}[[ξ, η]] carries **B**.
- At constant ξ, η: {P_c, P_d} = 0 holds identically, by the factorization of §4.5 (proved).

**Killing-sector reduction.** At ξ = e_c and N = 1, items 1–5 give (proved, H-lead):

  {P_c^tot, H}^{(3)} = Σ_{q,k} [ E·(−iωB_c + 𝒢A_c + iδ_cτ) + h·(−iωA_c − 𝒦B_c + iδ_cσ) ] f(q,k).   (T)

**Degree-2 inputs** (proved; the same conventions):
- The JS jet {C_j[e_c], C_s[N]} forces s·B_c = −i q·Δ_c f. So the transverse-trace coefficient of B_c is **b_T = i q·Δ_c/(2|q|²)**, of degree −1. This is R16-8's Lemma B in these conventions.
- The strain bracket {C_j[ξ], C_s[1]} = 0 forces the forward h-coupling of H to be **σ₀ = ½ v⊗P = (ε/2) v⊗v**, the W1 forward stress (`vR16-5:19`: F^{ij}(k,k) = v_i g_j).

## 4. (b) The translation sector: (β) is constructed at leading order (weak)

### 4.1 Theorem T3 (proved, H-lead, class 𝒞, weak; checked)

Take τ = 0 and σ = σ₀. Then (T) ≈ 0 is solved by:
- a_qq = −iω b_T = ½(q̂·v)(q̂·Δ_c);
- A_vL = ½(q̂·Δ_c)(q̂⊗v_⊥ + v_⊥⊗q̂);
- B_TT = −2iδ_c σ₀^{TT}/(ω² − |q|²), and A_TT = iωB_TT/2;
- B_L and a_T free.

Here A is of degree 0, B of degree −1, and every angular factor is bounded when |v| < 1.

**Proof.** (T) decomposes by helicity, because 𝒢, 𝒦 and the projections commute with rotations about q̂.
- **Helicity 0.** The E-coefficient's T-component gives −iωb_T − a_qq = 0, using (𝒢A)_T = −a_qq. The h-coefficient's q̂q̂ component gives −iωa_qq + iδ_cσ_qq = 0, using (𝒦B)_qq = 0 by Bianchi.
  - These have **no free parameter**. Eliminating a_qq gives σ_qq = εω²/(2|q|²) = (ε/2)(q̂·v)².
  - That is exactly q̂·σ₀·q̂.
- **Helicity 1.** −iωA_vL + iδ_cσ_vL = 0, and σ_vL ∝ (q̂·v), so the 1/ω cancels.
- **Helicity 2.** Two equations, with determinant ∝ (ω² − |q|²). ∎

**Checked** (`r1612_degree3.out` (1), (4); `r1612_controls.out` (A)):
- The full 8-equation weak system is solved with relative residual ≤ 1.3e-15 for every defect-carrying edge mode sampled (S(1.4) at (1.6, 1.6, 0); G(1.4) at four k), over 200 random q̂ each.
- The helicity-0 identity holds to 3e-17.
- **Control:** with σ → −σ₀ the residual is 7.2e-2. The match is not automatic; it selects the W1 sign.

### 4.2 Lemma J3: the (β) term is the JJ repair (proved; checked)

- q·A_c = ½(q·Δ_c) v. This is analytic: the angular parts of a_qq and A_vL recombine.
- Then, for every vector field η:

  {Φ_c^h, ∫Kill(η)·E} = −2∫η_j ∂_iα_ij = +∫∂_bη_j Δ_cb v_j f.

- The matter bracket is {P^m_c, P^m[η]} = −P^m[∂_cη] − ∫∂_bη_jΔ_cbv_jf.
- So the degree-2 {C_j[e_c], C_j[η]} defect cancels **for every η**, including the translation–rotation Killing jets that R16-8 said need a singular P^{(1,h)}.
- **Checked:** |q·A − ½(q·Δ_c)v|/|q| ≤ 3.7e-8 (finite-difference floor) at every sampled mode (`r1612_degree3.out` (1)).
- **Answer to R16-8's referee question 5** (`C5_R16-8_report.md:354`): (β) is compatible with the JJ jets. It *is* the JJ completion.

### 4.3 Lemma C: subluminality is necessary for (β) (proved, H-lead; checked)

- The helicity-2 solution needs |q|² − (q·v)² ≠ 0 on the sphere, i.e. |v(k)| < 1 for every defect-carrying mode.
- Otherwise the pole on the Cherenkov cone q̂·v = ±1 can be removed only by τ_TT = 2iσ_TT/ω, which has degree −1 (a non-local H).
- **Checked** (`r1612_degree3.out` (2), (2b)):
  - min over q̂ of (1 − (q̂·v)²) > 0 at all sampled S/G edge modes (smallest +0.018);
  - −12.1 for the L-box mode at (2.6, 0.1, −0.4), where |v| = 3.62;
  - near that cone |q|²|B| grows as 1/angle: 1.6e-2, 1.9e-1, 2.0 at angles 1e-1, 1e-2, 1e-3.
- **Finite q** (checked at one k per law, 2e5 random q): max |ε(k+q/2) − ε(k−q/2)|/|2 sin(q/2)| is 0.908 for S(1.4) and 0.538 for G(1.4). No finite-q resonance at the sampled k.

### 4.4 Weak, not strong

- With τ = 0 and σ = σ₀, the strong (componentwise) equations need A_T and B_vL ∝ 1/(q̂·v), which are unbounded (checked, `r1612_controls.out` (C): 8.1e1, 8.7e2, 8.8e3 as q̂·v goes 2.3e-2 → 2.3e-4).
- So in 𝒞 the translation sector closes only up to constraint-proportional residuals. Their coefficients are bounded and of degree 1. Written as structure functions, they carry 1/r^{d−1} kernels: a **matter-dependent deformation** of the standard {D, H}, or equivalently a non-local constraint basis change (suggested).
- Strong closure with additional regular τ and σ was not explored.

### 4.5 Lemma W: factorization and canonical relocation (proved at first order; checked)

- Every forced component of Φ_c is δ_c times a c-independent tensor: Φ_c = δ_c·Ξ.
- Hence:
  - {P_c^tot, P_d^tot}^{(3)} = i(δ_cδ_d − δ_dδ_c)Ξ = 0;
  - **Φ_c = {P⁰_c, W}**, with P⁰ = P^m + P^g and W = −iΣ_{q,k}(E·Ξ_E + h·Ξ_h)f, singular.
- Consequently (Jacobi, with {P⁰, H₀} = 0): (T) ≈ 0 ⟺ {P⁰_c, H + {W, H₀}} ≈ 0.
  - The (β) system (P⁰ + {P⁰, W}, quasi-local H) is the first-order canonical image under e^{ad W} of the system (bare P⁰, **non-local** H′ = H + {W, H₀}).
  - (α)- and (β)-type presentations are therefore canonical relocations of each other at this order. "H quasi-local" is not an invariant property.
- **Checked:** Φ_c/δ_c agrees between c = 0 and c = 1 to ≤ 7.2e-15 at three modes (`r1612_controls.out` (D)).

## 5. (b) The boost sector: Theorem B3, no completion with quasi-local H in 𝒞

### 5.1 Statement and proof (proved, H-lead; unrefereed)

**Statement.**
- Assume class 𝒞, H-mat with at least one defect-carrying mode with v(k) ∦ Δ_b-direction (generic), and Φ_b as forced by degree 2 and Theorem T3.
- The standard {C_s[x_b], C_s[1]} = C_j[e_b] at degree 3, i.e. **{K_b^tot, H} ≈ P_b^tot**, has no solution with H = C_s[1] quasi-local.
- The helicity-0 part forces, rigidly:

  **Y_qq = b_T,   X_T = 2i b_T/ω = −(q·Δ_b)/(|q|²(q·v))**,

  which is unbounded on the great circle q̂·v = 0 wherever q̂·Δ_b ≠ 0.

**Proof.**
1. The right side contains Φ_b. Its B_T and a_qq parts multiply E_T and h_qq, which are not constraint components, so they are not weakly regular.
2. With τ and σ regular, every left-side contribution is regular except {K_b^sing, H₀}. These include the regular boost completions, the x_b-weighted brackets, and the h-structure-function term.
3. K_b^sing is the first lapse-momentum jet of the scalar completions. It has the form Σ(E·X_b + h·Y_b)f, because their p_N = 0 value (H) is regular.
4. {K_b^sing, H₀} = E·(−iωX + 𝒢Y) + h·(−iωY − 𝒦X). In helicity 0 the weak equations are −iωX_T − Y_qq = b_T and −iωY_qq = a_qq = −iωb_T (Theorem T3).
5. Regular τ_T changes a_qq only at relative order q.
6. Adding constraint-proportional terms to K (E_L·Z or h_T·Z) moves only L- and T-components. So the two equations are rigid. ∎

**Checked** (`r1612_degree3.out` (3); `r1612_controls.out` (B)):
- |q|²|X_T| grows exactly as 1/(q̂·v) over 5 decades at four edge modes. For example G(1.4) at (2.6, 0.1, −0.4): 2.2e2 → 2.4e6 as q̂·v goes 2.3e-2 → 2.3e-6.
- It matches 2ib_T/ω to ≤ 1e-5, with system residuals ≤ 5e-10.
- The weak boost operator has rank 8 and a 4-dimensional null space with **zero** X_T and Y_qq components (2.2e-15, 2.1e-16). So X_T is forced, not a minimal-norm artifact.

### 5.2 What the forced kernel is (reading)

- PV 1/(q·v) is a line along v. Convolved with the dipole-Coulomb factor (q·Δ_b)/|q|², X_T is the defect's Coulomb field **integrated along its whole straight world-line**. It falls off as 1/r_⊥ away from the line and does not decay along it.
- Center-of-energy reading: P_b^tot contains the non-local cross term Φ_b, the hidden momentum carried by the fields. So dK/dt = P forces K to carry ∫dt of that cross term.
- The resonance is between ω = 0 matter transitions (q along the energy shell) and the non-propagating, zero-frequency scalar gravity sector. In GR Φ ≡ 0, so it never arises.
- The two helicity-0 contributions add (2b_T) rather than cancel. The sign is the one selected by §4.1's control.

### 5.3 Escapes outside 𝒞 (not decided)

1. **(α): non-local H.**
   - With singular τ_T the helicity-0 boost equations can be met, but then the translation equation needs singular σ too (suggested).
   - The boost of singular H terms ({K^reg, H^sing}) was not computed.
   - **(α) is not constructed.**
2. **World-line kernels in the boost generator** (non-homogeneous). Whether {P_c, K_b} = δ_bcH and {K_a, K_b} = J then close at degree 3 is not checked.
3. **Degree-4 singular terms acting through cutoff shells** (Lemma-F-type).
   - A shell bracket yields q-independent bulk coefficients unless the degree-4 kernel factorizes into a global E-moment × a Φ-type bilinear (suggested).
   - Excluded from 𝒞.
4. **Canonical relocations** (§4.5). By construction they leave 𝒞, so B3 is **presentation-bound**.
5. **Auxiliary / second-class formulations.** The R16-8 referee notes an elliptic auxiliary with a non-local multiplier (`vR16-8full:78-93`). Excluded.
6. **Pair channels.** They cannot cancel this number-conserving obstruction, by R16-5's grading lemma (`vR16-5:19`). This transfer is suggested.
7. **States with no defect-carrying quanta.** Every term above is ∝ Δ and is inert there (R16-8 Lemma S scope; `vR16-8full:58-67`).

## 6. (c) The R13-4 criterion and the size of a distant response

- **No observable is claimed.** (α) is not forced (§5.3 escapes 1–2 are open) and not constructed. No bounded observable invariant under the completed constraints is built, as the coordinator and `vR16-8:17` require. In particular, the R16-8 curvature R[B] is not Dirac-invariant (`vR16-8full:25-33`).
- By Lemma W, the gauge-invariant content of the Hamiltonian is presentation-independent only at the level of the Dirac observables. Those are unbuilt.
- **Conditional size (reading only, if some response ∝ the edge-quantum population exists).**
  - Defect-carrying modes have one-quantum energy ≥ 1.44/a (S(1.4)) and ≥ 1.49/a (G(1.4)) at m = 0.3, and ≥ 1.41/a at m = 0. That is ≥ 1.7e19 GeV at a = ℓ_P (`r1612_population.out`).
  - Thermal occupation e^{−ε/T}:
    - 10^(−3.3e31) at T_CMB;
    - 10^(−7.7e15) at 1 TeV;
    - 10^(−7.7e2) at 1e16 GeV;
    - O(10^(−0.8)) only at T ≈ 1e19 GeV.
  - R16-8's per-quantum kernel factor at 1 m is ≲ 4e-70 in Planck units (`C5_R16-8_report.md:273`; reading there).
  - With number-conserving matter, the population is whatever the initial state has.

## 7. (d) Prices (named, not adopted)

| price | content | axiom touched | buys |
|---|---|---|---|
| **P-W7K (new)** | The boost generator carries the world-line kernel X_T = 2ib_T/(q·v), or H is non-local (P-W7α). Forced in 𝒞 by the center-of-energy theorem at degree 3 | Admissibility `AX:57-61` (range of the rule); Poincaré/dynamics structure is downstream (`AX:116-123`) | the degree-3 {H[x_b], H[1]} scalar sector only |
| **P-W7sf (new)** | Translation closure only weakly: matter-dependent structure functions with 1/r^{d−1} kernels, or a non-local constraint basis change | none directly; it deforms the standard HDA that the setting assumes | degree-3 {D[e_c], H[1]} |
| **P-W7v (necessity, reading)** | Every defect-carrying mode subluminal, |v| < 1 (Cherenkov, Lemma C). Met by R14-1 S/G; fails for the L-box | Admissibility `AX:57-61`, already priced by R14-1 | (β)'s helicity-2 sector |
| P50 (R16-8), P-W7α | unchanged | `AX:57-58` | — |

## 8. Against the FIXED readings (`TESTS:5545-5548`)

- **QUASI-LOCAL (β): not met.**
  - The translation sector is constructed (weak; leading order; subluminal; Theorem T3 and Lemmas J3, C).
  - The boost sector has no completion with quasi-local H in 𝒞 (Theorem B3).
  - Non-Killing degree-3 smearings are not built.
- **NON-LOCAL (α): not met.**
  - Theorem B3 is an unrefereed proof that (β) is inconsistent in 𝒞. It is presented for the referee.
  - But (α) is not constructed, Lemma W shows the (α)/(β) split is presentation-dependent, and no bounded observable invariant under the completed constraints exists. So no distant-response size can be stated beyond the conditional reading in §6.
- **Worker reading: OPEN.**
- **Against the expectation** ("NON-LOCAL in the class, effect suppressed by the edge-quanta population", `TESTS:5549`):
  - (β) does fail in a stated class, but **in the boost bracket**. R16-8's translation-sector term is repaired by (β) with no new Hamiltonian input.
  - The population suppression agrees (reading).

## 9. Strong-word check

- **"Proved":** Theorem T3, Lemma J3, Lemma C, Lemma W (first order) and Theorem B3. All are at leading order in q (H-lead), in class 𝒞, for the Killing sector only, unrefereed.
- **"Exactly" / "identically":**
  - the helicity-0 identity σ_qq = q̂σ₀q̂ (given current-aligned P);
  - q·A = ½(q·Δ_c)v;
  - Φ_c = δ_cΞ.
  All three are at leading order.
- **"Forced" / "rigid":** within the weak helicity-0 equations of §5.1, given B_T from degree 2 and regular H.
- **"Non-local":** used for symbols that are non-analytic at q = 0. It is never used of observables.
- **Numbers:**
  - |q| = 1e-3 in (1)–(2b) and |q| = 1 in (3) and the controls, which is legitimate because the leading symbols are homogeneous;
  - finite differences at steps 1e-4/1e-5 (floor about 1e-8);
  - nothing is subtracted anywhere.
- **v_max** is stated for every law (§1). **Ward/HDA:** standard throughout. The weak closure is named as a deformation where it is one (§4.4).
- **Not claimed:**
  - non-Killing degree-3 brackets;
  - {P, K} and {K, K} at degree 3;
  - (α)'s construction;
  - any physical (Dirac-observable) non-locality.

## 10. For the referee

1. **Conventions.** Check H-conv, especially the sign link between b_T (JS jet) and σ₀ (strain bracket). §4.1's sign-flip control shows that the translation sector selects it.
2. **Theorem B3.** Is the helicity-0 rigidity complete? In particular:
   - can a regular K-completion's x_b-weighted bracket with H_int produce a 1/(q·v) term? (I argue no: regular × regular.)
   - is the exclusion of degree-4 shell terms (§5.3, item 3) fair?
3. **Lemma W.** Does the first-order canonical-relocation identity hold beyond the Killing sector? If W extends to all smearings, the whole (α)/(β) question reduces to Dirac observables.
4. **Lemma J3.** Confirm that q·A = ½(q·Δ_c)v cancels the {C_j[e_c], C_j[η]} defect for every η.

## 11. Files (all in `S/`)

- `scripts/r1612_degree3.py` / `.out`:
  - (1) the translation-sector weak solve with the JJ check;
  - (2), (2b) Cherenkov denominators;
  - (3) boost-sector X_T growth;
  - (4) the helicity-0 identity;
  - (5) finite-q resonance scan.
  - The function `solve_boost` there is an unused stub.
- `scripts/r1612_controls.py` / `.out`: (A) sign flip; (B) null space; (C) strong closure; (D) factorization.
- `scripts/r1612_population.py` / `.out`: edge-mode minimum energies and Boltzmann exponents.
- `scripts/sublum_copy.py`: R14-1's symbols, unmodified.
- `recheck/`: the R16-8 and R12-1 runners and their reproduced outputs.
