# C5 R17-8 report: can mixing, field-dependent or altered generators supply constant shifts with physical momentum (P-r175a)?

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Not refereed. 2026-10-13, 00:51Z to 01:18Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R17-8/`.
- `S/r178_mix.py` and `S/r178_mix.out`: every check below. Four blocks, about 3.5 s at `OMP_NUM_THREADS=2`.
- `S/recheck/R16-5/` and `S/recheck/R17-5/`: the R16-5 and R17-5 runners, copied unmodified from `P/scripts/C5/{R16-5,R17-5}`. Both reruns are byte-identical to the saved `.out` files (`diff` empty).
  - **Defect found in the repo copy of the R17-5 runner:** it imports `r99_profiles_copy` from `../r165_recheck`, which does not exist under `P/scripts/C5/`. As committed, it fails with `ModuleNotFoundError`. It runs, identically, once the R16-5 profile file is placed beside it.
- No downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - the C5 method (`:2302-2320`);
  - R13-5 (`:4668-4680`) and its worker reading (`:4707-4713`);
  - R16-5 (`:5130-5149`), its worker reading (`:5325-5337`) and its referee reading (`:5437-5447`);
  - R17-5 (`:5849-5868`) and its worker reading (`:6048-6059`);
  - RFW in full (`:2237-2300`; F2 is `:2268-2280`);
  - R17-8 (`:6061-6087`). This is the FIXED text I report against.
- `agents/C5_R16-5_report.md` in full; `agents/C5_R16-5_referee_verdict.md` (`vR16-5`) in full.
- `agents/C5_R17-5_report.md` in full.
- The R17-5 referee finished during this run. I read `.../scratchpad/C5/ref_R17-5/REFEREE_VERDICT.md` (`vR17-5`) in full: **CONFIRMED WITH CORRECTIONS, EXCLUDED-MB**.
- `agents/RFW_F2_report.md` in full.
- `agents/C4_F1_report.md:1-60,195-260` and `agents/C4_F1_referee.md` (verdict items).

**Not read.** R9-9 and R8-2 reports. The graviton enters only through its quadratic Hamiltonian and its multiplier/mixing action, and I used R16-5's statement of them (`C5_R16-5_report.md:44-57`). I also did not read the other R17 scratch reports.

**Labels.**
- **proved:** complete under the stated hypotheses.
- **checked:** numerics in `r178_mix.out`.
- **suggested:** argued, not proved.
- **reading:** interpretation.
- **comparator:** literature or a standard mathematical fact, RECALLED unless verified.

---

## 0. In plain words

The item asks whether the last finite-band, local route (P-r175a) can give a grid where constant shifts are gauge and matter carries real, redshifting momentum. That route changes how the shift acts, and has three forms.

1. **"Altered" generators: locked by Noether (proved).**
   - The shift N_i couples to the momentum density T^{0i}, and the gauge rule includes time-dependent shifts (δN_i = ∂_tξ_i).
   - Together these force the matter part of the shift generator to be exactly ∫T^{0i}, up to terms that vanish on shell.
   - So "move matter with one operator while gravity sees a different momentum" is impossible in any canonical (Hamiltonian) matter theory.
   - This matters because the decoupled version would be a trivial escape: shifts act on nothing, while the density stays physical.
2. **Mixing generators: a finite menu of shift values (proved for one band; proved for many bands with analytic symbols).**
   - A shift that mixes stress components acts, on each mode, by one of the eigenvalues of a fixed finite matrix M(q). That matrix has at most A values, where A is the number of coupled components (9).
   - The momentum symbol would need a continuum of different increments g(k+q) − g(k) across the zone. The checked count is 1434–4000 distinct values against the 9 allowed.
   - Finitely many values cannot track a continuously varying periodic function. The only way out is constant spectra, which brings back R17-5's "labels, not momentum" (refereed) and its redshift failure.
3. **Field-dependent generators: the identity survives only "on shell", and there it becomes a winding statement (proved for single or isolated bands, given two standard topology facts).**
   - Field-dependent terms can absorb everything that is off the matter energy shell. They enter multiplied by the graviton's inverse propagator, which was checked symbolically.
   - What is left is a condition along each energy surface: along the surface, momentum must change exactly as the wave number does.
   - On a torus-shaped zone, the energy surfaces of a band are organised by a graph with at most one loop. Real translations need three independent windings.
   - So no band can carry physical momentum. The checked least-squares residual stays at 0.72–0.77 out to 342 Fourier functions.
   - A one-axis band would escape. The control shows the residual going to 3e-4 as the band is made one-dimensional. Real matter is not one-axis.
4. **What is left.**
   - Mixing and field-dependent generators used together (only a sketch here).
   - Multi-band mixing with several small shift eigenvalues, when the symbol is merely continuous.
   - Field-dependent generators with crossing bands.
   - Outside this class, and unchanged: the tower (P64), discontinuous symbols (P90), interacting matter, non-symmetric couplings, and a non-projectable lapse.

**Worker reading: OPEN.** It comes with a substantial no-go for the referee, covering mixing and linear field-dependent generators separately, but not their combination. EXCLUDED-MIX needs a refereed no-go covering both, so it is not claimable here. No ESCAPE was found.

---

## 1. Hypotheses and classes (stated before any title)

- **H-mat.** Free quadratic matter on Z³ × ℝ.
  - N < ∞ bands; continuous Hermitian Bloch h(k).
  - As R17-5's 𝓜_N (`C5_R17-5_report.md:62-66`), and containing it.
  - **H-an** (used where stated): every symbol is real-analytic in k. That is automatic for finite-range kernels and for exponentially decaying ones.
- **H-ker.** Coupled densities T^α(q) = Σ_k a†_{k+q}F^α(k,k+q)a_k + (pair parts), with kernels continuous on T³ × T³. α runs over the A coupled components.
  - In R9-9's projectable setting: T^{0l} (3, coupled to N_l) and T^{(il)} (6, coupled to h_il). So A = 9.
  - ∫T^{00} is coupled only globally, to N(t).
  - The pair parts drop out of every forward identity used here, by R16-5's grading lemma (`vR16-5:19`). This is confirmed for massive matter and extended in `vR17-5` to positive-energy bands.
- **H-W1.** W1_pf as in R16-5 (`C5_R16-5_report.md:46-49`), including **time-dependent** shifts δN_i = ∂_tξ_i, with symmetric coupled stress.
- **H-gen (the removed hypothesis, `TESTS:6077`).** Constant shifts act by:
  - (i) on matter at O(√κ): any local-in-time transformation linear in ξ (generator symbol Γ_j(k), not assumed equal to Π_j);
  - (ii) on the graviton fields (h_ij, π^ij, N_i) at O(h): any translation-covariant matrix multiplier. The matter identity then carries a mixing matrix M_j(q) on the A components, continuous at q = 0 (**mixing**);
  - (iii) on all fields at O(√κ), through canonical cubic generator corrections Q = ∫(h·Y + π·Z + N·W) + π_N-terms, with continuous kernels (**field-dependent, linear in the fields**).
- **H-grav.** R9-9's N-type graviton at quadratic order (`C5_R16-5_report.md:44`):
  - H_g = ∫(π·Gπ + h·K(q)h), with K(q) = O(q²) and G the DeWitt metric;
  - the momentum constraint N_i H^i with H^i linear in π and O(q);
  - projectable lapse.
- **H-RB (redshift bridge; a hypothesis on `AX:187`, as in `C5_R17-5_report.md:79-82`).** Near an IR-regular extremum, R(k) = Σ_i F^{ii}(k,k) = p·v at leading order. This is bridge-conditional, as both referees state (`vR16-5:19`; `vR17-5:9`).
- **Zeroth moment (necessary condition used throughout).** Invariance of the vertex under constant ξ at O(κ), coefficient of each gravity field times φ†φ (R16-5 §1, `C5_R16-5_report.md:58-64`):
  - Γ_j(k+q)F^α − F^αΓ_j(k) = Σ_β M_j^{αβ}(q)F^β + (field-dependent terms) (★).
- **Excluded realizations (outside, with why).**
  - Single band with multiplier shifts (R16-5) and multiband with multiplier shifts (R17-5): covered, counted once.
  - Towers N = ∞ (P64) and discontinuous symbols (P90): excluded by the item (`TESTS:6075`).
  - Interacting matter, non-symmetric couplings and a non-projectable lapse: not in R17-5's class either (`vR17-5:15`).
- **Subtractions (named before any run).** None. All values are raw: counts, least-squares residuals, symbolic coefficients.
- **Order.** W1_pf exact at O(√κ). The zeroth moment at O(κ) exactly at finite q (mixing). For field-dependent generators: on the matter energy shell, through first order in q.

## 2. Prior art (each counted once)

- **R16-5 and its verdict.**
  - T_pf, single band, multiplier θ (`vR16-5:11`).
  - The 1D-separable mixing result, repairable but narrow; "general 3D mixing remains open" (`vR16-5:17`).
  - The zeroth moment is necessary "only in the stated deformation class… field-dependent/non-block-diagonal generators, operator mixing… expressly outside" (`vR16-5:9`).
  - R16-5 already let the generator symbol g be arbitrary, closing RFW F2's "altered leading generators" in its class (`C5_R16-5_report.md:91`). It did so *with* g identified as T^{0j}'s forward value. §3.1 shows that identification is forced.
- **R17-5 and its verdict** (`vR17-5:3-17`), CONFIRMED WITH CORRECTIONS, EXCLUDED-MB:
  - MB-A, including degeneracies (`C5_R17-5_report.md:116-130`; `vR17-5:5`);
  - Lemma F and MB-B (`:148-171`; `vR17-5:7`, with corrections: C¹ regularity of h; only the eigenspace-compressed forward stress vanishes in c = 0 sectors);
  - Lemma RB (`:173-189`; bridge-conditional, `vR17-5:9`);
  - the winding test (`:191-195`).
  - Its open list (`:217`) says "The MB-A partner step breaks there [mixing], because mixing terms enter at the same order q as θ." §3.2 shows that statement is too pessimistic: the partner step survives with a finite set of shifts.
- **RFW F2** (`TESTS:2268-2280`; `RFW_F2_report.md`).
  - At constant ξ every field-dependent piece "either drop[s] out or enter[s] only through functions of q", and "A function of q cannot cancel" a function of matter momentum (`RFW_F2_report.md:19-26`).
  - B-terms vanish on shell (`:59`), and X enters through K(q) = O(q²) (`:60`).
  - §3.2 is that mechanism made exact at finite q. §3.4 is its Hamiltonian, FDiff analogue. Counted once.
  - Open there: "Changing the matter's Killing generators" (`:199`). That is §3.1 here.
- **C4 F1** (`C4_F1_report.md:207-219`; referee `C4_F1_referee.md:9`): "Lapse transport gives the same obstruction in the fixed-generator, single-band ansatz". It does not bear on mixing beyond that.
- **I1/I2** (via `C5_R17-5_report.md:105,107`): determinant winding, and the −β zone-mean anomaly. Same family of mechanism; counted once.
- **Repo grep** for "Reeb", "energy shell", "on-shell", "Noether lock" and "mixing generator" in `TESTS.md`: the hits are only RFW F2's on-shell B-terms and R16-5/R17-5's open lists. No prior on-shell or winding treatment of the FDiff translation identity exists.

---

## 3. Results

### 3.1 (altered generators) Lemma N, the Noether lock. Proved

**Statement.** Under H-W1 (time-dependent shifts), suppose the O(√κ) matter transformation is δφ = −i√κ 𝒢_{ξ(t)}φ, with 𝒢 linear in ξ(t,·), local in time, and possibly accompanied by EOM-proportional (trivial) terms. Then 𝒢 is Hermitian, and 𝒢^j = T^{0j} as bilinear kernels, up to kernels that vanish on the matter shell. In particular, **Γ_j(k) = Π_j(k) := F^{0j}(k,k).**

**Proof.**
1. The variation of ∫⟨φ, i∂_tφ⟩ is √κ∫⟨φ, 𝒢_{∂_tξ}φ⟩ + √κ∫⟨φ, i(𝒢 − 𝒢†)_ξ ∂_tφ⟩.
2. The vertex variation is −√κ∫(∂_tξ_iT^{0i} + D_iξ_jT^{ij}). δH_m contains no ∂_tξ and no φ̇.
3. The φ̇·ξ term can be cancelled by nothing else off shell, so 𝒢 = 𝒢†.
4. After integrating the ∂_tξ terms by parts, the coefficient −∂_t(𝒢^j − T^{0j}) contains φ̇ off shell. So 𝒢^j − T^{0j} vanishes, up to on-shell-trivial kernels, which have the form (ε(k+q) − ε(k))X or [h, X]-type.
5. At q = 0, such a kernel's eigenspace compression vanishes. Both Γ_j and Π_j commute with h: Γ_j because the constant-ξ generator is conserved, and Π_j by Lemma F's order q⁰.
6. So Γ_j − Π_j commutes with h and has zero compression on every eigenspace of h. Hence Γ_j = Π_j. ∎

**Scope.**
- Transformations depending on ∂_tξ are not covered by the proof. The same commutator argument suggests the conclusion (**suggested**).
- Non-canonical (non-Hamiltonian) matter is outside the class; that is price P-r178a.

**Why it is load-bearing.** Without the lock, Γ ≡ 0, M ≡ 0 satisfies (★) trivially while Π_j stays physical, i.e. a spurious ESCAPE. RFW F2's "altered leading generators" (`TESTS:2275`) are therefore not a separate route in the canonical FDiff class. Changing Γ changes Π, which R16-5 and R17-5 already let be arbitrary.

### 3.2 (a) Mixing, single band. Theorem MIX-1. Proved

**Statement.** Take a single band, continuous g_j = Γ_j = Π_j (Lemma N), the exact identity (★) without field-dependent terms, and any finite A with any M_j(q) (no continuity needed). Then **g ≡ 0**.

**Proof.**
1. (★) reads (Δ_q(k) − M_j(q))F(k,k+q) = 0, with Δ_q(k) = g_j(k+q) − g_j(k) and F ∈ C^A. So wherever F(k,k+q) ≠ 0, Δ_q(k) ∈ spec M_j(q), a set of at most A values.
2. Let U = {k : F(k,k) ≠ 0}. On a closed ball K ⊂ U, F(k,k+q) ≠ 0 for |q| < r_K, by uniform continuity.
3. Δ_q is continuous in k and takes finitely many values on the connected set K, so it is constant on K: Δ_q = θ_K(q).
4. Telescoping gives θ_K(q₁+q₂) = θ_K(q₁) + θ_K(q₂), and θ_K is continuous in q. So θ_K is linear, and g_j is affine near every point of U.
5. Hence g_j is affine on each component Ũ of the lift of U. g_j = F^{0j}(k,k) is a component of F, so g_j = 0 on ∂Ũ.
6. R16-5's half-space argument (`vR16-5:11`) applies verbatim. It does not need Ũ ∩ H = ∅: Ũ ∩ W is clopen in each open half-space W of ℝ³ \ H. So the slope is 0.
7. g_j is then constant on each component of U and zero on ∂U, so g_j ≡ 0 unless U = T³. In that case g_j is a constant, and the C₂ rotation that reverses k_j makes it 0. ∎

**Checked** (`r178_mix.out:1-24`). G, NN and L at m = 1 and 0.3:
- The forward values span all 9 components (rank 9). So M_j(0) = 0 is forced by the q = 0 identity.
- The number of distinct values of Δ_q(k)/|q| over 4000 random k is 1434–4000, against the ≤ 9 the identity allows.
- The best unconstrained 9×9 M(q) leaves relative residual 0.978–0.995 at |q| = 1e-1, 1e-2 and 1e-3.
- **Continuum control** (g = k, ε = √(m²+k²)): residual 6.8e-16 to 2.3e-15, with M = q_x·1 recovered to ≤ 8e-17. So the test finds mixing solutions where they exist.

This closes the "general 3D component mixing" counter-route of `vR16-5:3,17` for single-band matter (any finite mixing, exact identity).

### 3.3 (a) Mixing, multiband. Theorem MIX-2

**Step 1, reduction at q = 0 (proved, continuous class).**
- Write Φ_k(w) := Σ_α w_αF^α(k,k) for row vectors w. The q = 0 identity is [Γ_j, Φ(w)] = Φ(wM_j(0)).
- ad_{Γ_j} is diagonalizable with real spectrum. So Φ sends the generalized μ-eigenspace of M_j(0) (acting on rows) into the μ-eigenspace of ad_{Γ_j}, and it annihilates the non-semisimple (Jordan-chain) parts.
- With Lemma N, Π_j = Φ(e_{0j}) commutes with Γ_j = Π_j. So Π_j = Φ(w₀), where w₀ is e_{0j}'s component in the generalized 0-eigenspace.
- Let Π_j(k)y = γy with γ ≠ 0, and Y(q) := F(k,k+q)y ∈ C^N ⊗ C^A. Then w₀·(R₀Y(0)) = Π_jy = γy ≠ 0, where R₀(q) is the Riesz projector of M_j(q) for its eigenvalue group Σ₀(q) → {0}. So R₀(q)Y(q) ≠ 0 for small q.
- **This proves the mixing partner step:** γ ∈ spec Π_j(k+q) − Σ₀(q), because Π_j(k+q)⊗1 − 1⊗M_j(q) has spectrum equal to the set of differences.
- This answers R17-5's "the partner step breaks" (`C5_R17-5_report.md:217`). It survives, with the finite set Σ₀(q) in place of {θ(q)}.

**Step 2a, a single small shift (proved).** Σ₀(q) = {θ(q)} is a single value. This includes every multiplier, and every multiplier plus nilpotent mixing. Then R17-5's MB-A (`vR17-5:5`) applies verbatim: θ ≡ 0 near 0, and spec Π_j is k-independent. Standard W2_pf has M_j(q) = q_j·1 + O(q³), so Corollary S extends to it: no nonzero momentum density.

**Step 2b, several distinct small shifts, under H-an (proved).**
- Restrict to a lattice line k(t) = k₀ + t e_x. By Rellich's theorem (comparator, RECALLED, Kato), the eigenvalues are analytic branches γ_n(t).
- At a point t₀ where γ_n ≠ 0 and γ_n is separated from the other distinct branches, the partner of γ_n(t) at t + t′ must be γ_n itself for small t′.
- So γ_n(t + t′) − γ_n(t) ∈ Σ₀(t′e_x), a finite set. It is continuous in t, hence constant in t near t₀. By additivity it is linear, so γ_n is affine on an interval.
- By analyticity γ_n is affine on ℝ, and it is bounded, so it is constant.
- Repeat along y- and z-lines: the nonzero spectrum of Π_j is k-independent.

**Step 2b without H-an (suggested).** The finite-set mechanism forces branches to be piecewise affine, with turning points allowed only where partners can switch.
- **Checked** (`r178_mix.out:30-32`): the zigzag spectrum {+tri, −tri} with shifts {+q, −q} satisfies the partner relation to ≤ 9e-16 away from its peaks. At the peak k = ±π it fails by 0.74–1.0·q.
- So the obstruction sits at turning points, but I have no general proof for continuous symbols.

**Step 3, consequences (proved, given steps 2a/2b).** Every nonzero momentum symbol has k-independent spectrum, and H-W1 gives [h, Π_j] = 0.
- **RB-gen.** Take a band that is simple near an IR-regular extremum, punctured neighbourhood allowed. Its diagonal entry π_{a,i}(k) is an eigenvalue of Π_i in a finite constant set, so it is constant there.
- Then R = v·c_a exactly as in Lemma RB (`C5_R17-5_report.md:175-179`), which fails at leading order.
- Commutativity of the Π_i is not needed. That matters because mixing at q = 0 allows [Π_i, Π_j] ≠ 0.
- Protected multiplets (h exactly degenerate on E(k)): leading-order RB forces Π|_E(k₀) = 0. Constant spectrum then forces Π|_E ≡ 0, so R ≡ 0.
- **Example (checked, `r178_mix.out:27-29`).** Rotation-like mixing M_j(0) = iε_j makes the momenta an su(2) multiplet, Π_j = S_j, with constant spectrum.
  - [h, S_j] = 0 for all j makes h scalar on the multiplet (Schur).
  - W1's symmetric forward stress then needs v_iS_j = v_jS_i. The checked maximum mismatch is 0.981 (G) and 0.607 (NN), so v = 0: a flat band, excluded.
- **The bridge-free lattice-translation test** (R17-5 §3.5, refereed) fails for any continuous finite-band generator, whatever its action on densities. Field-dependent parts vanish at zero gravity fields. Counted once.

### 3.4 (b) Field-dependent generators: Lemma FD. Proved in the H-grav class; checked symbolically

**Statement.** Let Q = ∫(h·Y + π·Z) be a canonical cubic correction, with H_g quadratic and π-metric c. The π·φφ coefficient of {Q, H_m + H_g} must vanish, since the vertex has no π coupling. That forces Y = ad_ω Z/c. The h·φφ coefficient then changes by −(cK(q) − ad_ω²)Z/c: the graviton's inverse propagator at (ad_ω, q), applied to Z.

**Checked symbolically** (`r178_mix.out:34-37`), one graviton mode and one matter transition (sympy Poisson brackets):
- the forced Y is Z(e₂ − e₁)/c;
- the remaining h-coefficient is Z(cK_q − (e₂ − e₁)²)/c.

**The shift (N_i) sector** changes by:
- D(q)·Y, via the momentum constraint;
- ad_ω W, from N-dependent terms;
- D(q)D(q)ᵀX/c = O(q²), from π_N-type terms.

**Consequence (proved).** With linear field-dependent generators, (★) is enforced exactly only on the matter energy shell (ε_a(k+q) = ε_b(k)), and up to O(q²). Off-shell parts are absorbable. This is the Hamiltonian analogue of RFW F2's "B vanishes on shell; X enters through K(q) = O(q²)" (`RFW_F2_report.md:59-60`). Counted once.

**Note against R16-5.** R16-5's operator identity [P_j, T(q)] = θT(q) (`C5_R16-5_report.md:58`) is therefore stronger than necessary once field-dependent generators are allowed. Its no-go must be re-derived from on-shell content, which is what Theorem W does.

### 3.5 (b) Theorem W (on-shell translation identity is a winding obstruction)

**Statement.** Assume H-an, a band b that is isolated (simple everywhere), linear field-dependent generators, and a multiplier θ_j(q) = C_j·q + O(q²). Lemma N gives the band's momentum π_{b,j} = Γ eigenvalue. Then:
- **(i)** wherever π_b ≠ 0 and v_b ≠ 0: t·∇π_{b,j} = C_j·t for every t ⊥ v_b (proved);
- **(ii)** H-RB at an IR-regular extremum forces rank C = 3 (proved);
- **(iii)** if π_b ≢ 0, then rank C ≤ 1 (proved, given two RECALLED facts below).

So **π_b ≡ 0, and RB fails, for every isolated band. This holds for standard W2_pf (C = 1) and for every deformed multiplier.**

**Proof.**
- **(i).** On-shell q near 0 lies on the energy surface through k, q = s t + O(s²) with t ⊥ v_b. The on-shell identity is (π_{b,j}(k+q) − π_{b,j}(k) − θ_j(q))π_{b,i}(k) + O(q) corrections = O(q²). Its first order in s gives (i).
- **(ii).** Integrating (i) on the small level spheres around k₀ gives π_b = Cp + f(level). RB requires R = v·π = p·v + o(p²).
  - Massive case (v = Mp, M > 0): this forces f(k₀-level) = 0 and sym(MC) = M, so C = 1 + M⁻¹A with A antisymmetric, and det(1 + M^{−1/2}AM^{−1/2}) > 0. Hence rank 3.
  - Massless case: by the degree count of `C5_R17-5_report.md:177`.
- **(iii), step 1.** Let ψ_j = π_{b,j} − C_j·k on the lift ℝ³. Lift ε_b to ℝ³ too. By (i), ψ_j is locally constant along each lifted level component, on U = {π_b ≠ 0}.
- **(iii), step 2.** With C invertible, ∂U ⊂ {π_b = 0} ⊂ {k = −C⁻¹f(ρ(k))}, where ρ is the Reeb quotient. That set is at most one point per Reeb point, so under H-an it is a finite union of rectifiable curves.
- **(iii), step 3.** A closed set of dimension ≤ 1 cannot separate T³ (dimension theory, RECALLED). So either U = ∅, or U is T³ minus that set. In the second case it is dense in every level surface, and by continuity ψ_j is constant on every level component of the lift.
- **(iii), step 4.** If a level component L in T³ has a loop with lattice winding n, its lift contains both k and k + 2πn. Then ψ_j(k + 2πn) − ψ_j(k) = −2πC_j·n = 0. So C annihilates every class carried by a level component.
- **(iii), step 5.** The Reeb quotient induces a surjection π₁(T³) = Z³ → π₁(Reeb), a free group, whose kernel is generated by the level components' π₁ images (**comparator, RECALLED**: standard for Morse/analytic functions on closed manifolds). An abelian image in a free group is cyclic (comparator, standard). So the kernel has rank ≥ 2, and rank C ≤ 1. ∎

**Checked** (`r178_mix.out:39-46`).
- Least-squares minimum of the relative tangential residual ‖P_⊥(∇π_x − e_x)‖/‖P_⊥e_x‖ over trigonometric polynomials:
  - NN, m = 0.3: 0.896, 0.799, 0.757 and 0.745 at R = 1, 2, 4 and 6 (up to 294 coefficients);
  - G, m = 0.3: 0.885, 0.814, 0.734 and 0.716;
  - full Fourier basis, no parity imposed (342 functions): 0.769 (NN) and 0.761 (G).
- **Control, the one-axis (Reeb-cycle) escape.** NN with transverse dispersion scaled by δ: residual 0.757, 2.1e-2 and 2.7e-4 at δ = 1, 0.1 and 0.01. A band whose level sets carry the x-winding absorbs the x-identity. It cannot carry the y- and z-windings too (step 5).
- The residual floors are consistent with (iii). They are not a proof of a positive L² infimum.

**Scope.**
- Isolated (simple) bands only.
- Crossing or braided bands are **suggested** to fail the same way: a braid lifts to a finite cover of T³, which is again a 3-torus.

### 3.6 Mixing and field-dependent generators together. OPEN; suggested for a single cubic band

- **At q = 0.** Single band: the field-dependent terms vanish at q = 0 (ad₀ = 0, K(0) = 0), so M_j(0) = 0 still holds (rank 9, checked).
- **First order on shell.** (t·M_{1j} − t·∇g_j)φ(k) = 0 for t ⊥ v, with φ = (g, sym(v⊗g)).
- **Expansion near an RB extremum (g = p + O(p³), v ∝ p).** The O(p) and O(p²) orders force M_{1j} to be the standard δ_{jμ}·1 plus terms proportional to (t·g). These vanish on the tangent plane near the bottom. The identity then reads (t·∇g_j − t_j)g_i = (t·g)(Y_j^i + ½S_j^{i,n}v_n).
- **Where g ∥ v.** For example R8-2's g = εv. The right-hand side vanishes, which gives Theorem W's equation.
- **Where g ∦ v.** Consistency across i forces X_j ∥ g. A constant-coefficient linear map of v cannot be parallel to g everywhere unless g ∥ v.
- So the case reduces to Theorem W (**suggested**; this is a sketch, not a proof).
- Multiband with combined generators is **not treated**.

### 3.7 (c) and (d)

- **(c) Not reached.** No solution passes W2_pf with a nonzero physical momentum in any treated class, so R17-5's redshift and translation tests have nothing to run on. The translation test fails a priori for every continuous finite-band generator (§3.3, step 3).
- **(d) Prices.** See §5.

---

## 4. Against the FIXED readings (`TESTS:6083-6086`)

**Worker reading: OPEN.**
- **ESCAPE: not met.** No explicit finite-band local law with W2_pf, nonzero physical momentum and correct redshift was found. Every treated class is proved to have none.
- **EXCLUDED-MIX: not claimable.** It needs a *refereed* no-go covering mixing and linear field-dependent generators. What is proved here, for the referee:
  - Lemma N (altered generators; canonical, ξ̇-free class);
  - MIX-1 (single band, any finite mixing);
  - MIX-2 (multiband; any finite mixing under H-an, or a single small shift eigenvalue for continuous symbols);
  - Lemma FD plus Theorem W (linear field-dependent generators with multiplier shifts, isolated analytic bands).
- **What is not covered:**
  - the combination of mixing and field-dependent generators (§3.6: suggested for a single band, untreated for multiband);
  - continuous non-analytic multi-shift mixing;
  - field-dependent generators with crossing bands.
- **Scope question for the referee.** Does "covering mixing and linear field-dependent generators" require the joint class? If separate coverage suffices, the reading would be EXCLUDED-MIX restricted to H-an or isolated bands.

**Against the expectation (`TESTS:6087`): partly as expected.**
- Each route separately is excluded in the treated class. That leaves P64, P90, or giving up W2_pf.
- The mechanism is more specific than "mixing cannot change a winding":
  - Mixing is excluded by a counting argument: a finite menu of shift values cannot follow a continuous symbol.
  - The winding argument is needed only after field-dependent generators push the identity onto the energy shell. There the winding becomes a Reeb-graph statement.
- **Not expected.**
  - Field-dependent generators genuinely weaken R16-5's operator identity to its on-shell part.
  - That on-shell part has a real one-axis loophole (control, §3.5), closed only because translations need three independent windings.
  - The "altered generator" route is closed by W1 itself (Lemma N), not by W2.

## 5. Prices (named, not adopted)

- **P64 (tower) and P90 (discontinuous symbol):** unchanged, counted once.
  - Theorem W's topological step uses the compact torus T³. A non-compact momentum space (the tower or continuum) or a discontinuous symbol is exactly what evades it.
- **P-r178a, non-canonical or ξ̇-dependent shift action on matter.** This is what would decouple the shift generator from the coupled momentum density (escaping Lemma N).
  - It gives up the Hamiltonian/Noether structure of matter under FDiff.
  - It touches `AX:187` (source/action) and AX's statement that Admissibility does not choose a Hamiltonian (`AX:116-123`). Neither axiom supplies it.
- **P-r178b, one-axis matter.** Bands whose energy surfaces carry a lattice winding (Reeb cycle) absorb that one direction only.
  - Not a viable price: it needs all three directions, and b₁(Reeb) ≤ 1 on T³.
  - It is an exclusion, like R17-5's axis movers (comparator: every observed particle propagates isotropically, RECALLED).
- **Still open, unpriced:**
  - joint mixing plus field-dependent generators (multiband);
  - continuous non-analytic multi-shift mixing;
  - crossing bands under field-dependent generators;
  - and, outside this item's class: interacting matter, non-symmetric couplings, non-projectable lapse (`vR17-5:15`).

## 6. Strong-word check

- **"Proved":**
  - Lemma N (canonical, ξ̇-free transformations);
  - MIX-1 (single band, any finite mixing, exact identity);
  - MIX-2 step 1 (any continuous M) and step 2a (single small shift; relies on refereed MB-A);
  - MIX-2 step 2b (under H-an; relies on RECALLED Rellich);
  - RB-gen (simple bands near the extremum, and protected multiplets);
  - Lemma FD (H-grav class);
  - Theorem W (i)–(ii), and (iii) given two RECALLED topological facts (Reeb π₁ surjection with fibre-generated kernel; separation needs dimension ≥ 2).
- **"Checked":** every number cited from `r178_mix.out`, and the two byte-identical reruns.
- **"Suggested":**
  - Lemma N with ξ̇-dependence;
  - MIX-2 step 2b for continuous symbols;
  - §3.6 (joint class, single band);
  - Theorem W for crossing bands.
- **"No / every":** only within the stated classes. Nothing here covers towers, discontinuous symbols, interactions, non-symmetric couplings or a non-projectable lapse.
- **RECALLED:**
  - Rellich/Kato analytic perturbation;
  - the Reeb-graph π₁ facts;
  - free-group abelian subgroups being cyclic;
  - dimension-theory separation;
  - the isotropy comparator.
- **Standard / deformed:** each statement says which. MIX-1, MIX-2 and Theorem W cover both standard θ = q and every deformation in the stated class.

## 7. For the referee

1. Lemma N: is the off-shell φ̇ argument sound, and does it exhaust "altered leading generators" in a canonical FDiff theory? Is the on-shell-trivial remainder correctly shown to have zero forward value?
2. MIX-1: the finite-spectrum step, the telescoping additivity, and the half-space step with U = {F(k,k) ≠ 0} instead of {g ≠ 0}.
3. MIX-2 step 1 (Riesz-projector partner step with Jordan blocks), and step 2b's use of Rellich along lattice lines.
4. Lemma FD: is "enforced only on the matter energy shell, up to O(q²)" the correct necessary content once canonical cubic generator corrections (including N- and π_N-dependent terms) are allowed?
5. Theorem W (iii): the RECALLED Reeb facts, and the density/continuity step that extends ψ's constancy across ∂U.
6. Scope: is OPEN right, given separate (not joint) coverage of mixing and field-dependent generators?

## 8. Files

- `S/r178_mix.py` and `S/r178_mix.out`. Blocks:
  - (1) single-band mixing: rank, distinct-value counts, best-M least squares, continuum control;
  - (2) multiband: su(2) mixing and the symmetric-stress test; the zigzag partner check;
  - (3) Lemma FD, sympy Poisson brackets;
  - (4) Theorem W least squares, the anisotropy control and the full-basis run.
- `S/recheck/R16-5/{r165_tpf.py, r99_profiles_copy.py, r165_tpf.out, rerun.out}`: identical rerun.
- `S/recheck/R17-5/{r175_mb.py, r175_mb.out, rerun.out, r99_profiles_copy.py}`: identical rerun, after supplying the profile file the committed runner cannot find (§Scratch).
