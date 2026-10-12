# C5 R16-5 report: a preferred-frame second-order Ward identity (W2_pf) and the graviton–matter poles under it

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Not refereed. 2026-10-12, 22:44Z to 23:05Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R16-5/`.
- `S/scripts/r165_tpf.py` and `.out`: every check below (runs in 0.5 s at `OMP_NUM_THREADS=2`).
- `S/scripts/r99_profiles_copy.py`: R9-9's band profiles G, L, NN, copied unmodified from `.../C5/R13-5/scripts/`.
- No downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`); RN L3 results (`:864-875`); C4 first-wave results (`:1398-1453`); RFW results (`:2263-2300`); Round 16 in full (`:5037-5163`), R16-5 is `:5130-5149`; the R15 verdicts (`:5164-5209`).
- `agents/C5_S17_synthesis.md` at the R16-5 lines (`:103,107,179,218,263,415-434`); C5_S14 was not re-read beyond what S17 quotes.
- `SUMMARY.md` §17's root-obstruction statement (`:397-413`). §§21–25 were not read in full; I used S17 and the verdicts below.
- Reports and verdicts: `C5_R13-5_report.md` in full and `C5_R13-5_referee_verdict.md` (`vR13-5`); `C5_R13-8_referee_verdict.md` (`vR13-8`); `C5_R14-5_referee_verdict.md:80-95` (`vR14-5`); `C5_R15-1_referee_verdict.md` (`vR15-1`); `C4_F1_referee.md` and `C4_F1_report.md` (grep hits at `:26,49-54,99,103,207-219,250`).

**What I did not read.** R8-2 and R9-9 reports directly (used through R13-5's citations); C5 rounds 6–12 in full (used through S17 and verdicts); RN L3's report (used through its refereed summary at `TESTS:870`).

**Labels.** **proved**: complete under the stated hypotheses. **checked**: numerics here. **suggested**: argued, not proved. **reading**: interpretation. **comparator**: literature, RECALLED unless verified.

**Pending-item note.** I relied on no unrefereed R15/R16 scratch report.

---

## 0. In plain words

1. **A preferred frame does not remove the wall. It moves it from boosts to translations.**
   - The foliation-preserving group still contains every spatial shift, including the constant one, which is a plain translation.
   - On the grid, the momentum that is supposed to generate those translations is a periodic function of the wave number. A periodic function has slope zero on average across the zone. A translation needs slope one everywhere.
   - This is the same zone-mean mismatch that blocked boosts (`SUMMARY.md:397-413`). In the preferred frame it sits in the translation and strain part of the algebra instead.
2. **Allowing any deformation does not help, in the class stated.** If constant shifts act on the graviton by any multiplier θ(q) and on matter through the momentum constraint with a continuous symbol, then the identity forces θ ≡ 0 near q = 0, and the matter momentum density's forward value is zero everywhere (proved, §3.2).
3. **That trivial solution is excluded by observation.** With a zero forward momentum density, matter has no forward response to a uniform stretch of space. Light would not redshift as the universe expands (proved, given the stated linear response; the observed redshift is a comparator). Rotating bodies would not drag frames (suggested).
4. **The pair-creating stress does enter the preferred-frame identity (new against R13-5), but it cannot repair it.** Pairs enter the strain and shear moments ∫x_i T^{0j}, unlike H, P and K. But the failing identity is the translation one. The momentum generator has no pair part, and the identity splits by particle number (proved, checked).
5. **What would work is the same as before.** Exact translations need either an infinite band tower or a discontinuous momentum symbol. The discontinuous symbol has 1/r tails along each axis (raw Fourier coefficients 1/n, nothing subtracted) and vertices that never cross the zone face. Smoothly decoupling the edge does not work: the failure moves into the transition shell (checked).
6. **So the registered test again has nothing to compute in.** No W2_pf-complete stress exists in the class. The reading is **OPEN**, with this no-go recorded for the referee. The TT one-loop numbers of R13-5 carry over unchanged as first-order (W1_pf) numbers. The extra scalar question (projectable Hořava) is prior art (RN L3), and it is now a second failure behind this first one.

---

## 1. Hypotheses and classes (stated before any title)

- **H-mat.** Free (quadratic) matter on Z³ × ℝ.
  - Scalars: ε² = m² + Σ_i u(k_i), m > 0, profiles G, L and NN of R8-2/R9-9 (`r99_profiles_copy.py`).
  - Finite-band generalization: a continuous Hermitian N×N Bloch symbol, N < ∞ (§3.2(iv)).
  - Pair channels allowed, with finite spatial pair kernels F^{ij}_pair (R13-5's P1 class, `C5_R13-5_report.md:143-160`).
- **H-grav.** R9-9's N-type box graviton at linear order, as in R13-5 (`C5_R13-5_report.md:82-84`). The FDiff fields are N(t), N_i(t,x), h_ij(t,x) (projectable: the lapse depends on t only, as registered at `TESTS:5135`).
- **W1_pf (first order, standard and deformed alike).** Gauge invariance of ∫(N_i T^{0i} + ½h_ij T^{ij}) at O(√κ) under δh_ij = D_iξ_j + D_jξ_i, δN_i = ∂_tξ_i:
  - the ν = j identity ω F^{0j} = Σ_i D_i F^{ij} in every channel (momentum conservation);
  - local energy conservation is *not* a gauge identity here (ξ⁰ = f(t) only); only ∫T^{00} = H is coupled, to N(t).
  - So T^{0j} (momentum density, couples to N_j) and the energy flux T^{j0} need not be equal.
- **W2_pf (second order), written out.** At O(κ), the linearized FDiff constraint algebra with matter must close:
  - (i) the momentum constraints H_i[ξ] = H_i^grav[ξ] + ∫ξ^i T^0{}_i close on spatial vector fields: matter's part is the momentum-density algebra;
  - (ii) every coupled matter density (T^{0i}, T^{ij}) transforms under H_i[ξ] as the corresponding tensor density (Lie derivative), up to seagull contact terms proportional to Dξ;
  - (iii) the global energy ∫N(t)H_⊥ is invariant under time-independent spatial diffeos, up to constraints.
  - **Standard W2_pf:** the transformation in (ii) is the continuum Lie derivative, or its lattice version with D_j(q) = q_j + O(q³).
  - **Deformed W2_pf (class 𝒟):** constant shifts act on h(q) by any odd, translation-covariant multiplier θ_j(q), and on matter through the zero mode of the momentum constraint, P_j = ∫T^{0j}. No other assumption is made about the Lie derivative.
- **Moment used.** The zeroth moment of (ii), i.e. constant ξ:
  - [P_j, T(q)] = θ_j(q) T(q) for T ∈ {T^{0l}, T^{il}}.
  - Seagull terms drop out, because Dξ = 0 for constant ξ.
  - Equivalently: the total FDiff translation charge P_grav + P_mat is conserved by the vertex ∫h(−q)T(q).
  - Gauge parameters restricted to vanish at p = 0 do not avoid this moment. The identity at p ≠ 0 tends to it as p → 0, because local kernels are continuous in p (proved, given quasi-locality).
- **Generator symbol.** P_j = dΓ(g_j), with g_j(k) := F^{0j}(k,k) the forward value of the momentum density. P_j has no pair part: by W1_pf, F^{0j}_pair = D_iF^{ij}_pair/ω with ω ≥ 2m and D(0) = 0, so it vanishes at q = 0 (R13-5 Lemma P1, `C5_R13-5_report.md:146-160`, which uses only the ν = j identity).
- **Subtractions (named before the runs).**
  - Fourier tails (§3.5): raw coefficients of the symbol, nothing subtracted.
  - Zone means: raw averages over a 2¹⁶-point periodic grid.
  - No pole-shift subtraction is used: no new pole number is computed.
- **Order of exactness.** W1_pf exact at O(√κ); W2_pf at O(κ), in moment form; pole statements at one loop.
- **Excluded (outside realizations):**
  - non-projectable lapse (N(t,x));
  - nonlinear gravity;
  - interacting matter;
  - infinite-band (tower) matter;
  - discontinuous symbols (treated as escapes, §3.5);
  - non-block-diagonal BV completions and gauge maps not generated by ∫T^{0j} (RFW's open class, `TESTS:2297`);
  - component-mixing deformations beyond the 1D-separable case of §3.3.

## 2. Prior art (each counted once)

- **R13-5 and verdict.** P1 (pair W1 completion), W0 (no Ward identity reaches TT at axial q), B2 (standard W2 fails; pair terms drop out of H, P, K) (`vR13-5:3-7`). The reading was OPEN both ways, because the standard-W2 class is empty (`vR13-5:13`). The paired residue is 2κm²J₂ (`vR13-5:15-19`). The G floor at a = ℓ_P is 4.37e-3 / 5.35e-3 / 5.46e-3 for T₂g at m = 1, 0.3, 0.01 (`vR13-5:9`).
- **C3's rotation theorem inside FDiff (C4 F1).** "The rotation sector is inside the momentum-constraint bracket"; lapse transport gives the same obstruction "in the fixed-generator, single-band ansatz" (`C4_F1_referee.md:9`; `C4_F1_report.md:207-219`). The projectable scalar is a ghost, a tachyon or strongly coupled (`C4_F1_report.md:250`).
- **RN L3.** "TDiff, unimodular and Hořava are not escapes. The projectable scalar has ω² = −(1−2c)Jg k²" (`TESTS:870`).
- **RFW F2.** For K2's fixed O(κ) pseudo-translation, "the constant-translation h·φ²·ξ coefficient already gives an impossible first-jet identity". Open there: "altered leading generators", "multiband", "singular, non-local or quasi-local completions" (`TESTS:2268-2280`). RFW F1: invariance of the affine-Killing projection under diagonal field-dependent generators (`TESTS:2283-2287`).
- **I2 (C4).** The band-and-zone-averaged anomaly is exactly −β per mode for every finite periodic C² Bloch matrix; I1: exact closure needs the reciprocal tower (`TESTS:1402-1418`).
- **Root obstruction** (`SUMMARY.md:397-413`): "Its momentum generates central differences, factor by factor, not translations."
- **R13-8 gauge kernel** (`vR13-8:11`): exact linearized diffeomorphism invariance leaves a two-dimensional degree-2 kernel. Not used below beyond its scope.
- **R15-1** (`vR15-1:5-7,19`): an elliptic lapse with a stress coupling g ≠ 0 signals superluminally. Bearing in §3.7.
- **R14-5 CMC discussion** (`vR14-5:86-88`): cuscuton and Bhattacharyya et al.; the instantaneous elliptic mode. Bearing in §3.7.
- **Comparators.** GW170817: −3e-15 ≤ c_T − 1 ≤ 7e-16 (`C4_F1_report.md:103`, not re-verified). Cosmological redshift of light, ν ∝ 1/a, and frame dragging (Gravity Probe B, LAGEOS) at the 10–20% level: RECALLED, not verified here.
- **Repo search.** grep for "Lense", "frame dragging" and "redshift" in `TESTS.md` gave only R12-x comparator lines (`:4204,4323,4357,4435`). No prior W2_pf statement exists; S17 records it as "unwritten" (`C5_S17_synthesis.md:107,179`).

**What is new here, against that prior art.**
1. The generator symbol g is arbitrary (any continuous symbol, not the fixed p = u′/2). This is RFW F2's "altered leading generators" open item, closed in this FDiff Hamiltonian moment class.
2. The deformation class 𝒟 (any multiplier θ) has only the trivial solution, and that solution is excluded by observation.
3. Finite-band (matrix) symbols are covered.
4. The pair channel: it enters FDiff's strain moments but cannot reach the translation jet.
5. Smooth edge decoupling fails; only sharp, non-local decoupling escapes.

---

## 3. Results

### 3.1 (a) What W2_pf requires at its zeroth moment. Proved

For T(q) = Σ_k F(k,k+q) a†_{k+q}a_k + (pair parts), the number-conserving part of [P_j, T(q)] is Σ_k [g_j(k+q) − g_j(k)] F(k,k+q) a†_{k+q}a_k. [P_j, ·] preserves particle-number grading, because P_j has no pair part (§1). So the identity [P_j, T(q)] = θ_j(q)T(q) requires

  **g_j(k+q) − g_j(k) = θ_j(q) wherever F(k,k+q) ≠ 0,**

separately from every pair-channel identity.
- **Standard W2_pf:** θ_j(q) = q_j + O(q³).
- **Class 𝒟:** θ_j is any odd function.

### 3.2 Theorem T_pf (translation jet). Proved

**Statement.** Let g_j be continuous on T³, covariant under the proper cubic rotations (in particular g_j changes sign under the C₂ rotations that reverse k_j), and not identically zero. Suppose the zeroth-moment identity of §3.1 holds for T = T^{0j}, whose kernel is continuous with F^{0j}(k,k) = g_j(k). Then:
- (i) θ_j(q) = 0 for all small q;
- (ii) g_j is constant on each connected component of U_j = {g_j ≠ 0};
- (iii) hence g_j ≡ 0. This contradicts the assumption, so **the only solution is g ≡ 0, θ ≡ 0 near q = 0.**

**Proof.**
1. For k in a compact K ⊂ U_j and |q| small, F^{0j}(k,k+q) ≠ 0 by continuity. So g_j(k+q) − g_j(k) = θ_j(q) there.
2. Chaining small steps gives θ_j(q₁ + q₂) = θ_j(q₁) + θ_j(q₂) near 0, with θ_j continuous (it equals a difference of values of g_j). So θ_j(q) = c_j·q near 0, and g_j is affine with gradient c_j on each component V of U_j.
3. Lift V to a connected component Ṽ ⊂ ℝ³. There g_j = c_j·k + a, a single affine function, because Ṽ is connected.
4. Suppose c_j ≠ 0, and let H = {c_j·k + a = 0}.
   - Every boundary point k₀ of Ṽ projects to ∂V, where g_j = 0 by continuity. So ∂Ṽ ⊂ H.
   - Ṽ does not meet H, because g_j ≠ 0 on V.
   - So Ṽ is open and closed in ℝ³ \ H, i.e. Ṽ is an open half-space (or all of ℝ³ if ∂Ṽ = ∅, which cannot avoid H when c_j ≠ 0).
   - Then g_j = c_j·k + a is unbounded on Ṽ. But g_j is continuous on the compact T³, hence bounded. Contradiction.
5. So c_j = 0: (i) and (ii).
6. With c_j = 0, g_j is constant on each component of U_j and zero on its boundary. So either U_j = ∅, or U_j = T³ with g_j ≡ a ≠ 0. The C₂ rotation that reverses k_j gives g_j(Rk) = −g_j(k), so a = −a = 0: (iii). ∎

**(iv) Finite-band version (proved).** Let Π_j(k) be a continuous Hermitian N×N symbol, P_j = dΓ(Π_j), with T^{0j}'s forward block equal to Π_j(k).
- Sandwich the identity Π_j(k+q)F − FΠ_j(k) = θ_j(q)F between spectral projectors. F(k,k+q) → Π_j(k) in norm, and the eigenvalue clusters move continuously. So each nonzero eigenvalue ν of Π_j(k) has a partner ν + θ_j(q) in spec Π_j(k+q).
- Applied to λ_max (where it is > 0) in both directions, this gives λ_max(k+q) = λ_max(k) + θ_j(q). The scalar argument of steps 1–5 then gives θ_j ≡ 0 near 0. (Use λ_min where λ_max ≤ 0.)
- With θ_j = 0, the partner argument in both directions makes the set of nonzero eigenvalues of Π_j(k) locally constant, hence constant on T³. A continuous branch cannot leave a finite set, so multiplicities are constant too. So **the spectrum of Π_j is k-independent.** If E(k) is non-degenerate and [Π_j, E] = 0, each band's forward momentum is a constant, and C₂ covariance makes it zero for any band mapped to itself.
- Degenerate crossings where bands are exchanged by C₂ are not treated: **suggested** there.

**(v) The pair channel cannot repair it (proved).**
- The identity is graded and P_j has no pair part (§1). So pair kernels enter only the pair-graded identities, never the number-conserving one that fails.
- This holds for every finite pair kernel: R13-5's P1 class, both with and without P46 pairing.

**(vi) Checked** (`r165_tpf.out`, block (1); G, L and NN at m = 1 and 0.3):
- The zone mean of g′ is ≤ 3e-16 for four symbols: p = u′/2 (R8-2's forward value), sin k, and smoothed sawtooths with δ = 0.5 and 0.1.
- The fraction of the zone where |g′ − 1| > 1e-6 is 0.34 (G), 0.35 (L), 1.0 (NN, sin k) and 0.15 / 0.03 (smoothed sawtooths).
- At q = 0.01, 0.1 and 1, the zone average of g(k+q) − g(k) is ≤ 1.1e-16. That average is the only candidate for θ(q), and it is 0. The spread over k is 2e-2 to 17, so it is not k-independent.

### 3.3 Deformations by cubic-covariant component mixing (1D separable). Proved; checked

- Allow constant shifts to mix components: [P_x, T^{0x}(q)] = θ q T^{0x} + d q T^{00} + e q T^{xx} + O(q²).
- The forward limit gives g′g = c g + dε + e v g.
- **C₂ parity:** g and v are odd, ε is even. So dε must equal its own negative: d = 0 unless g ≡ 0.
- **The rest:** where g ≠ 0, g′ = c + e v. Integrating around the circle, ∮g′ = 0 and ∮v = ∮ε′ = 0, so c = 0.
- Checked: ∮v dk ≤ 3e-12 on G, L and NN (block (7)).
- The same conclusion for the T^{00} identity (if T^{00} is coupled): g′ε = cε + e v g. With integrating factor ε^{−e}, c∮ε^{−e} = 0, so c = 0. Checked: ∮ε^{−e} > 0 for e ∈ {−2…5} (block (5)).
- **Scope.** Non-separable 3D bands with general mixing are **suggested** only.

### 3.4 Observational exclusion of the trivial solution g ≡ 0

- **Forward strain response (proved).** The W1_pf forward limit gives F^{ij}(k,k) = v_i g_j.
  - Proof: (q·v)F^{0j}(k,k) = q_iF^{ij}(k,k) + O(q²) for every direction q̂.
  - Checked to 1e-4 (G) and 6e-4 (L) at q = 1e-4, block (2).
  - So g ≡ 0 gives zero forward spatial stress.
- **No redshift (proved, given linear response).**
  - In the FDiff gauge N_i = 0, a uniform h_ij(t) = 2δa δ_ij is physical expansion (K_ij ≠ 0).
  - The one-particle energy shift is δε = −½h_ij F^{ij}(k,k) = −δa (v·g) = 0.
  - Under W2_pf, each later instant is gauge-equivalent to this one (a time-dependent dilation ξ = λ(t)x is in FDiff), so the shift is zero at every a.
  - So photon frequencies do not redshift. With g = k on the box, by contrast, δε = −δa·ε for massless box states: the ν ∝ 1/a law.
  - The observed cosmological redshift (comparator, RECALLED) excludes g ≡ 0.
  - The global lapse N(t) cannot supply it: it rescales every energy together, and redshift compares two energies.
- **No frame dragging (suggested).** The shift couples to T^{0i}. With g ≡ 0, the orbital part ½{x_i, g_j} of the angular-momentum moment vanishes. That suggests no Lense–Thirring source from rotating bodies, against Gravity Probe B and LAGEOS (comparator, RECALLED). The residual moment ∫x_iT^{0j} = dΓ(μ_ij(k)) + pairs is not computed.

**Combined (proved, in the stated class).**
- Standard W2_pf fails for every continuous single-band symbol, and for every continuous finite-band symbol, with or without any pair channel.
- Every deformation in class 𝒟 (and the 1D-separable mixing class) forces g ≡ 0, which observed redshift excludes.
- So no W2_pf-complete stress compatible with observed redshift exists in the class of §1.

### 3.5 The escapes, checked

- **Discontinuous symbol: exact crystal momentum (sawtooth).**
  - g = k on (−π, π). Raw Fourier coefficients are |c_n| = 1/n exactly (n|c_n| = 1.000, 1.000, 1.006 at n = 10, 100, 1000; nothing subtracted). That is a 1/r tail along each axis.
  - The anomaly ∮(g′ − 1) = −2π (checked, block (4)) is a delta on the face.
  - The identity also needs vertices that never straddle the face (no umklapp): another non-local constraint on the kernels.
  - Even then, the dilation and shear moments fail at the cutoff surface: a momentum-space box is not dilation-invariant (**suggested**).
  - **Whole-zone v_max:** a SLAC-type ε = √(m² + k²) on the cube gives |v| ≤ 1 (proved).
  - **Self-force:** P commutes with the free H, so a free moving body feels no self-force at O(κ⁰) (proved). The O(κ) self-force is not computed.
- **Smoothed sawtooth (δ = 0.5, 0.1).** Local (raw |c₁₀₀₀| = 1.3e-16 and 4.6e-10). But the anomaly −2π is spread over a strip of measure 0.96 and 0.19, where §3.2 applies (block (4)).
- **Smooth edge decoupling (R7-1's χ-cut, made smooth).** Take g = k·c(k), with c = 1 on |k| ≤ a and c = 0 beyond b.
  - The identity fails in the transition shell, by 8.3q, 11.6q and 30.5q for (a, b) = (2.0, 2.6), (2.5, 3.0), (2.9, 3.1) (block (6)).
  - The residual is O(q), so this is a failure of the identity, not a discretization effect.
  - Only a sharp cut (c an indicator) escapes, and that is a discontinuous symbol: non-local.
  - So P64's second option, "edge energy does not gravitate", protects the W2_pf translation jet only if the cut is sharp (proved, for continuous g, by §3.2).
- **Infinite tower.** I1's complete reciprocal tower (P64's first option) realizes g = k without periodicity. This is the continuum. Counted once.
- **Whole-zone v_max of the bands used** (block (1); any d, any m: |v|² ≤ max_i u_i′²/4u_i):
  - G: 1.0000 (subluminal; per axis 0.908 at m = 1, 0.990 at m = 0.3).
  - L: 4.185 (superluminal edge, as known).
  - NN: 1.0000.

### 3.6 (b) Gauge invariance of the poles

- **TT pole at one loop: gauge-parameter free (proved).** The one-loop TT self-energy has no internal graviton line. R13-5 Lemma W0's block argument (`C5_R13-5_report.md:184-207`) holds a fortiori here, because W2_pf has fewer identities (ν spatial only). So this needs no W2_pf.
- **Matter pole: not W2_pf-protected in the class.**
  - The Nielsen cancellation of the gauge-dependent (spatial-longitudinal) part of the graviton propagator needs the full W2_pf vertex and seagull identities. Their zeroth moment is §3.1's identity, which fails (or holds only at g ≡ 0).
  - The premise failing is **proved**. That the gauge dependence is actually nonzero is **suggested**; its size is not computed, as in R13-5 (`C5_R13-5_report.md:228-229`).

### 3.7 (c), (d) Pole split and the extra scalar

- **(c) Split.**
  - No W2_pf-complete stress exists, so there is no W2_pf-invariant split to compute.
  - **First-order numbers carry over (proved).** Ξ depends only on the TT vertex and the band (R9-9 Theorem T). The W1_pf class contains R13-5's W1 class, and conditions (i)–(ii) of 𝒲_V do not involve the ν = 0 identity. So R13-5's floor holds unchanged in the W1_pf-complete enlargement of 𝒲_V (count once): G at a = ℓ_P, T₂g 4.37e-3 to 5.46e-3 per species (`vR13-5:9`), about 10¹² times the GW170817 band.
  - With P46 pairing, Ξ ≡ 0 and the residue is 2κm²J₂ (`vR13-5:15-19`). J is a de Donder quantity, and de Donder is not an FDiff gauge. The matter side in an FDiff gauge is not computed.
- **(d) Extra scalar.**
  - Prior art (count once): the projectable scalar is a ghost (λ < 1), a tachyon (λ > 1) or strongly coupled (λ = 1) (`TESTS:870`; `C4_F1_report.md:250`).
  - After §3.4 it is a second failure: it matters only if an escape of §3.5 is bought.
  - **R15-1 bearing (reading).** The projectable lapse has no local elliptic equation. So there is no Lemma-S-type local instantaneous channel from it; its only instantaneous element is the global Hamiltonian constraint's zero mode, and N(t) is gauge.
  - Curing the scalar by going non-projectable (BPS, comparator) brings back a local elliptic lapse. R15-1's signalling test would then have to be rerun on that lapse (`vR15-1:19`; `vR14-5:86-88`). Not done.

---

## 4. Against the FIXED readings (`TESTS:5145-5148`)

**Worker reading: OPEN.**
- No W2_pf-complete stress is constructed.
- One is proved not to exist in the stated class, compatible with observed redshift (§3.2–3.4). This is a no-go, for the referee.
- **SPLIT-PRESENT is not available.** Its universal statement would be vacuous over an empty class, and "with numbers" cannot be met (as for R13-5, `vR13-5:13`).
- **SPLIT-ABSENT is not available**, for the same reason.

**Against the expectation (`TESTS:5149`).**
- "A W2_pf-complete stress exists, since boosts are no longer gauge": **not so.** Constant spatial shifts are still gauge, and the same zone-mean anomaly (⟨g′⟩ = 0 against 1) blocks them, standard or deformed.
- "Likeliest failure: a strongly coupled extra scalar": the scalar fails too (prior art), but the identity fails first, at its translation jet.
- Not expected:
  - the pair channel does enter W2_pf's strain moments (checked: |b(k)| up to 0.25 on G and 4.0 on L, block (3)), unlike R13-5's H, P and K, yet it cannot reach the failing identity;
  - smooth edge decoupling does not evade the identity.

## 5. Prices (named, not adopted)

- **P-pf1: exact preferred-frame translations need a discontinuous momentum symbol.**
  - Crystal momentum (sawtooth): 1/r tails along each axis, raw, nothing subtracted.
  - Plus vertices that never straddle the zone face.
  - Against Admissibility's nearest-neighbour rule (`AX:57-61`) and the source/action gate (`AX:187`).
  - Shear and dilation moments still fail at the cutoff surface (suggested).
- **P-pf2 (refines P64's χ-cut option).** Edge decoupling protects W2_pf only if it is sharp, i.e. non-local. It costs P-pf1's locality on top of non-universal coupling (equivalence principle for edge states).
- **P64's tower option** (Qubit fibre infinite-dimensional, `AX:47`) is unchanged. Count once.
- **Not a price, an exclusion:** trivial preferred-frame translations (θ ≡ 0, g ≡ 0) fail the observed redshift.

## 6. Strong-word check

- **"Proved":** Theorem T_pf (i)–(iii), single band, continuous g; (iv) finite-band, away from C₂-exchanged degeneracies; the grading/pair statement (v); the 1D-separable mixing result; the forward identity F^{ij} = v_ig_j; no redshift at g ≡ 0 (given linear response at each instant via the FDiff dilation); TT one-loop gauge-parameter freedom; the carry-over of R13-5's first-order floor.
- **"Checked":** every number in §3.2(vi), §3.3, §3.5 and §4.
- **"Suggested":** no frame dragging at g ≡ 0; shear/dilation failure at a hard cutoff; matter-pole gauge dependence nonzero; general 3D mixing.
- **"Does not exist":** only for W2_pf-complete stresses in §1's class (continuous finite-band symbols, finite pair kernels, translations by a multiplier θ(q) generated by ∫T^{0j}, projectable lapse), compatible with observed redshift.
- **"Standard / deformed":** every Ward statement above says which. Theorem T_pf covers both: standard as θ = q, deformed as any θ in 𝒟.
- **RECALLED:** redshift and frame-dragging comparators; BPS; the Nielsen identity's premise structure; the GW170817 band (as recorded at `C4_F1_report.md:103`).
- **Not claimed:**
  - non-projectable FDiff;
  - interacting or tower matter;
  - non-block-diagonal BV or field-dependent generators beyond RFW F1's invariance (`TESTS:2283-2287`);
  - any new pole number.

## 7. For the referee

1. Is the zeroth moment of W2_pf(ii), [P_j, T(q)] = θ_j(q)T(q) with P_j = ∫T^{0j}, a necessary condition for any deformation that keeps constant shifts as gauge? Is the continuity-in-p argument for restricted gauge parameters sound?
2. Theorem T_pf step 4 (the lifted half-space and boundedness argument) and the finite-band spectral-partner step (iv).
3. Does C₂ covariance legitimately make g odd along each axis? (`AX:37-41` gives only proper rotations.)
4. Is the redshift exclusion airtight given the FDiff dilation equivalence at each instant? Could a deformation make uniform strain act on matter other than through T^{ij}'s forward value?
5. Scope: is "OPEN with a no-go" the right reading, rather than a FAIL?

## 8. Files

All in `S/scripts/`:
- `r165_tpf.py` and `.out`. Blocks:
  - (1) zone means, the finite-q average and v_max;
  - (2) the forward-limit identity;
  - (3) pair moment and oddness;
  - (4) sawtooth tails and anomaly integrals;
  - (5) T^{00}-identity mixing;
  - (6) smooth χ-cut residuals;
  - (7) T^{0x}-identity mixing.
- `r99_profiles_copy.py`.

No downloads.
