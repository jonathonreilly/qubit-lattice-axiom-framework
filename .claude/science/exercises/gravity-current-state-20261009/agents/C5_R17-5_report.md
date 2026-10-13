# C5 R17-5 report: GW170817 on the grid, second attempt — multi-band W2_pf completions

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Not refereed. 2026-10-13, 00:35Z to about 00:58Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R17-5/`.
- `S/scripts/r175_mb.py` and `S/scripts/r175_mb.out`: every check below, nine blocks, about 1 s at `OMP_NUM_THREADS=2`.
- `S/r165_recheck/`: the R16-5 runner and profile file, copied unmodified from `P/scripts/C5/R16-5/`. The rerun is byte-identical to the saved `r165_tpf.out` (`diff` empty).
- No downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`:
  - the C5 method (`:2302-2320`);
  - Round 16 head and R16-5 (`:5037-5039,5130-5149`);
  - Round 17 in full (`:5685-5922`); R17-5 is `:5849-5868`;
  - RFW (`:2263-2300`), C4 first wave (`:1398-1420`), R2-1 (`:2746-2754`), RC (`:1218-1240`).
- `agents/C5_R16-5_report.md` in full, and `agents/C5_R16-5_referee_verdict.md` (`vR16-5`) in full. No `C5_R16-5_referee.md` exists in `agents/`.
- `agents/C5_R13-5_referee_verdict.md` (`vR13-5`) in full; `agents/C5_R16-8_referee_verdict.md:13`; `agents/C4_I1_referee.md:7,21`.
- `agents/C5_S20_synthesis.md`: `:1-80,170-200`, the W3/W15 rows `:280,292`, and R17-5's lines `:763-782`. `agents/C5_S17_synthesis.md`: grep hits `:107,218,415-434`.
- `SUMMARY.md`: §17's root obstruction (`:397-413`), §20 RFW (`:520-533`), §26 (`:677-714`).

**Not read.** R9-9's report (the N-type graviton enters only through its multiplier θ); RN L3's report (used through `TESTS:870` as quoted in R16-5); the other R17 scratch reports. I relied on no unrefereed R16/R17 claim.

**Labels.**
- **proved:** complete under the stated hypotheses.
- **checked:** numerics in `r175_mb.out`.
- **suggested:** argued, not proved.
- **reading:** interpretation.
- **comparator:** literature or observation, RECALLED unless verified.

---

## 0. In plain words

1. **The referee's six-band construction labels bands. It does not carry momentum.**
   - Each of its six species carries a fixed "momentum" ±1 along one axis, whatever its wave number.
   - On a grid, a quantity like that behaves as a charge, not as momentum. Shifting space does nothing to it.
2. **This holds for every finite number of bands, not only six.** Take any finite-band matter whose momentum symbol is continuous, and ask that constant shifts act on it by a multiplier, as R16-5 assumed. Then:
   - the shift multiplier must vanish near q = 0 (θ ≡ 0);
   - the momentum's eigenvalues cannot depend on the wave number.

   R16-5 had this away from degeneracies. The proof here holds with any degeneracy, so it covers bands that a C₂ rotation exchanges (proved, §3.1).
3. **The momentum-conservation identity (W1_pf) then splits every band into one of two kinds** (proved, §3.3):
   - bands with zero momentum label: gravity sees no stress from them at zero wave number;
   - bands with a fixed nonzero label c: they can move only along c. The six-band construction made consistent with W1_pf is six species of one-directional "axis movers".
4. **None of this matter has physical (redshifting) momentum.** Each of three stated tests fails:
   - standard W2_pf, where a constant shift translates every density (§3.2);
   - one site of P_j-translation being a lattice translation (winding; prior-art tool, §3.5);
   - the redshift bridge: under a uniform stretch, an axis mover's energy changes in proportion to its velocity, not its momentum. For an optical photon at a = ℓ_P that is about 5e27 times the cosmological redshift, with a sign that depends on the direction of motion (§3.4).

   Under the standard rotation bracket, any such momentum must vanish outright (§3.6).
5. **What would work is unchanged:**
   - an infinite band tower (P64);
   - a discontinuous momentum symbol (P90);
   - generators outside the multiplier class (component mixing, field-dependent or altered generators), which are not tested here.
6. **Worker reading: EXCLUDED-MB, pending the referee.** If the referee does not confirm it, the reading is OPEN. (c), the pole split, is not reached.

---

## 1. Hypotheses and classes (stated before any title)

- **H-mat (class 𝓜_N).** Free quadratic matter on Z³ × ℝ.
  - N bands, N < ∞.
  - A continuous Hermitian Bloch Hamiltonian h(k), periodic on T³.
  - Positive-energy quasiparticle bands, ε_a(k) + ε_b(−k) > 0 almost everywhere. Massive or massless; pair channels allowed, with continuous pair kernels.
  - This contains the six-band signed-axis family (Π_j = diag(v_j), `vR16-5:13-17`), every C₂-exchanged family (bands swapped by the C₂ that reverses k_j), and twisted families (Π(k) = U(k)DU(k)†).
- **H-ker (quasi-locality).**
  - Every coupled density T(q) = Σ_k a†_{k+q}F(k,k+q)a_k + (pair parts) has a kernel continuous on T³ × T³.
  - For §3.3, a kernel C¹ in q at q = 0 (a finite first real-space moment).
- **H-gen (multiplier-generated shifts, KEPT from R16-5's class 𝒟, `C5_R16-5_report.md:55`).**
  - Constant shifts are generated by P_j = ∫T^{0j} = dΓ(Π_j), with Π_j(k) := F^{0j}(k,k).
  - They act on each coupled density by an odd multiplier: [P_i, T(q)] = θ_i(q)T(q).
  - **Standard** W2_pf: θ_i(q) = q_i + O(q³). **Deformed:** any θ.
  - The graviton (R9-9's N-type) enters only through θ: a single universal graviton forces one common θ for all species.
- **H-W1 (W1_pf, `C5_R16-5_report.md:46-49`).**
  - The ν = j identity ω F^{0j} = Σ_i D_i(q)F^{(ij)}, with D_i(q) = q_i + O(q²).
  - F^{(ij)} is the symmetric stress coupled to the symmetric h_ij.
  - Projectable lapse.
- **H-RB (redshift bridge; a hypothesis on `AX:187`, not axiom content).**
  - Take an excitation of band a near an extremum k₀, with p = k − k₀. Its linear energy shift under a slow homogeneous isotropic strain h_ij = 2δa δ_ij, in gauge N_i = 0, is −½h_ij⟨F^{ij}(k,k)⟩ = −δa·R_a(k).
  - "Physical (redshifting) momentum" means R_a(k) = p·v_a(k) at leading order in p. This is the continuum dilation p → p/(1+δa).
  - It is stated with the caveats of `vR16-5:19`: an instantaneous forward matrix element is not proven to be cosmological frequency transport.
- **IR-regular extremum.** Massive: the Hessian M at k₀ is positive definite. Massless: the leading homogeneous dispersion φ(p) is > 0 for p ≠ 0.
- **Excluded realizations (outside, with why):**
  - single-band (R16-5 covers it);
  - discontinuous symbols (P90);
  - towers, N = ∞ (P64);
  - non-multiplier generators: component mixing beyond R16-5's 1D-separable case, field-dependent or non-block-diagonal generators, and altered leading generators. These are RFW's open class (`TESTS:2275,2298`) and `vR16-5:9`;
  - non-symmetric (vielbein-type) stress couplings, which are not R9-9's graviton (but see §3.4, Remark 2);
  - interacting matter;
  - non-projectable lapse.
- **Subtractions (named before any run).** None. All raw values: spectral differences, residuals, ratios.
- **Order.** W1_pf exact at O(√κ). W2_pf at O(κ), zeroth moment, plus the rotation bracket where stated. The redshift response is at linear order in δa.

## 2. Prior art (each counted once)

- **R16-5 and its verdict.**
  - Theorem T_pf (single band) is confirmed (`vR16-5:11`).
  - The finite-band step (iv) "can support θ_j = 0 and a k-independent spectrum", but not Π_j = 0 (`vR16-5:17`).
  - Pair grading is confirmed (`vR16-5:19`).
  - The zeroth moment is necessary only in the multiplier class (`vR16-5:9`).
  - The redshift exclusion is bridge-conditional (`vR16-5:19`).
  - R16-5's own step (iv) left "degenerate crossings where bands are exchanged by C₂" as suggested (`C5_R16-5_report.md:130-134`).
  - **Counted once.** §3.1 re-proves (iv) without the non-degeneracy restriction. The λ_max device is R16-5's.
- **I1 (C4).** "for continuous P(k), determinant winding prevent[s] finitely many patches from closing on the torus" (`C4_I1_referee.md:21`); I1 assumes Nelson integrability (`C4_I1_referee.md:7`). §3.5's lattice-translation test reuses this tool for the translation generator. Not new.
- **R2-1.** On Z⁴, the constant-ξ Ward identity plus analyticity makes a finite fibre impossible (`TESTS:2748-2752`). Related, different setting (Euclidean, analytic). Counted once.
- **I2 and the root obstruction.** The zone-averaged anomaly is −β per mode for every finite periodic C² Bloch matrix (`TESTS:1411-1415`; `SUMMARY:397-413`). It is the same zone-mean mechanism, but for boosts.
- **R13-5** (`vR13-5:7,13,21`): pair terms drop out of H, P, K, and standard-W2 classes are empty.
- **R16-8's P-pf1/W7 relation** (`C5_R16-8_referee_verdict.md:13`): "same root, different object". Not used beyond prices.
- **RN L3** (projectable Hořava scalar is a ghost, tachyon or strongly coupled; `TESTS:870` via `C5_R16-5_report.md:80`): not reached.
- **RFW F1:** invariance under diagonal field-dependent generators, in a narrow class (`TESTS:2279-2296`). It bears only on the excluded generator class.
- **Repo grep** for "six-band", "signed-axis", "C₂-exchanged", "multiband", "multi-band" and "winding" in `TESTS.md`. The hits are only the R16-5 verdict line, R17-5 itself, I1, R2-1 and the RC/RFW open lists. A grep over `docs/` for the same words returned unrelated admissibility notes ("six-axis" etc.). No prior multi-band W2_pf construction exists.

## 3. Results

### 3.1 Theorem MB-A (zeroth moment ⇒ θ ≡ 0 near 0 and k-independent spectrum, any finite N, any degeneracy). Proved

**Statement.** In 𝓜_N with H-ker and H-gen, let Π_j ≢ 0 and let the zeroth moment Π_j(k+q)F(k,k+q) − F(k,k+q)Π_j(k) = θ_j(q)F(k,k+q) hold for T = T^{0j} (F = F^{0j}) at all small q. Then:
- (i) θ_j(q) = 0 for all small q;
- (ii) the multiset spec Π_j(k) is independent of k.

**Proof.**
1. **Partner step.** Let ε_q = sup_k ‖F(k,k+q) − Π_j(k)‖. It tends to 0 by uniform continuity on the compact T³ × T³.
   - If Π_j(k)|y⟩ = y|y⟩ with |y| > ε_q, then F|y⟩ = y|y⟩ + O(ε_q) ≠ 0 and Π_j(k+q)(F|y⟩) = (y + θ)F|y⟩. So y + θ_j(q) ∈ spec Π_j(k+q).
   - The adjoint identity F†Π_j(k+q) − Π_j(k)F† = θF† gives the converse: x − θ ∈ spec Π_j(k) for x ∈ spec Π_j(k+q) with |x| > ε′_q.
   - No non-degeneracy is used.
2. Let λ(k) = λ_max Π_j(k), which is continuous. Assume U = {λ > 0} ≠ ∅; otherwise use −Π_j and −θ. On {λ > δ}, for |q| < r(δ), step 1 applied to y = λ(k) and x = λ(k+q) gives **λ(k+q) = λ(k) + θ_j(q)**.
3. So θ_j is continuous at 0 and locally additive, hence θ_j(q) = c·q near 0. λ is then affine with gradient c on each component of U.
4. R16-5's half-space argument (`C5_R16-5_report.md:121-128`, confirmed at `vR16-5:11`) applies verbatim to the bounded continuous λ. The lifted component's boundary lies in {c·k + a = 0}, so the component is a half-space on which λ is unbounded. Hence c = 0, which is (i).
5. **(ii).** With θ = 0, step 1 shows that for every x ≠ 0 the set {k : x ∈ spec Π_j(k)} is open, with radius ∝ |x|. It is also closed, by continuity of the spectrum. T³ is connected, so it is empty or all of T³. Multiplicities in a small window are locally constant. ∎

**Checked** (`r175_mb.out:10-15`). spread_k[λ(k+q) − λ(k)]/|q| is:
- 11.1 for a random 4-band range-1 family;
- 0.566 for a C₂-exchanged two-band family with k-dependent spectrum;
- ≤ 6e-12 for a twisted constant-spectrum family;
- 0 for the six-band family.

So no common θ(q) exists unless the spectrum is constant.

### 3.2 Corollary S (standard W2_pf has no finite-band solution with a momentum density). Proved

- Standard W2_pf needs θ_j(q) = q_j + O(q³), which is ≠ 0 for small q ≠ 0. MB-A forces θ_j ≡ 0 unless Π_j ≡ 0.
- If Π_j ≡ 0, the identity reads 0 = θ_j(q)F^{0j}(k,k+q), so F^{0j}(q) ≡ 0 for small q ≠ 0. There is then no momentum density at all.
- Pair parts cannot help. P_j has no pair part: F^{0j}_pair(k,q=0) = D_iF^{ij}_pair/ω_pair vanishes wherever ω_pair > 0, which is almost everywhere under H-mat, and hence everywhere by continuity. So the identity separates by particle-number grade (`vR16-5:19`, extended to positive-energy massless bands by the same division).
- This covers the six-band and C₂-exchanged families.
- **Checked** (`r175_mb.out:2-8`): with a sector-diagonal kernel the six-band identity holds at θ = 0 to 0.0. On the same-label entries the residual |θF_aa| is minimized only at θ = 0, and equals q·|c_{a,x}| at θ = q, for q = 1e-1, 1e-2 and 1e-3.

### 3.3 Lemma F and Theorem MB-B (sector structure forced by W1_pf). Proved

**Lemma F (multi-band forward stress).**
- Under H-W1 and H-ker (C¹), the order-q⁰ term gives [h(k), Π_j(k)] = 0.
- At order q: F^{(ij)}(k,k) = (∂_ih)Π_j + [h, G_{j,i}], where G is the first q-derivative of F^{0j}.
- Compress to an eigenspace E of h(k). The commutator drops out, so **P_E F^{(ij)}(k,k) P_E = V_i Π_j|_E**, with V_i = P_E ∂_ih P_E.
- F^{(ij)} is Hermitian, so [V_i, Π_j|_E] = 0.
- **Checked** (`r175_mb.out:62-64`): a 1D twisted two-band model, non-degenerate and exactly degenerate, agrees to 1.7e-6 at q = 1e-6, which is O(q).

**Theorem MB-B.** Under the hypotheses of MB-A plus H-W1, with the zeroth moment for all (i, j) (so [Π_i, Π_j] = θ_i(0)Π_j = 0):
1. One-particle space splits into continuous sector bundles Q_c(k), labelled by the constant joint eigenvalues c ∈ ℝ³ of (Π_x, Π_y, Π_z). The set C of labels is finite and k-independent (MB-A). h is block-diagonal in these sectors.
2. **Sector c = 0:** F^{(ij)}(k,k) = 0 on every band. There is no forward momentum and no forward stress.
3. **Sector c ≠ 0:** symmetry of F^{(ij)} gives V_ic_j = V_jc_i, so V_i = ĉ_iW. Every sorted energy branch of the sector is constant along every direction ⊥ c, so ε(k) = f(ĉ·k) (**axis movers**).
   - Proof of the last step: sorted branches are Lipschitz. Where a one-sided directional derivative along u exists, it is an eigenvalue of P_E(u·∂h)P_E = (u·ĉ)W|_E. That is first-order degenerate perturbation theory, a standard fact (RECALLED, Kato). It is 0 for u ⊥ c.
4. **The six-band construction, made W1_pf-consistent, is exactly six species of axis movers, ε_{±e_i}(k) = f(±k_i).**

**Checked** (`r175_mb.out:17-24`).
- A 3D-dispersing band labelled +e_x violates stress symmetry: max|v_yc_x − v_xc_y| = 0.908 (G, m = 1), 0.989 (G, 0.3), 0.616 (NN, 1) and 0.860 (NN, 0.3).
- An explicit axis-mover completion satisfies W1_pf exactly:
  - T^{0x} is the number density of the +x sector;
  - T^{xx} on x-links is F^{xx} = (f(k_x+q_x) − f(k_x))/D_x(q), with D_x(q) = −i(e^{iq_x} − 1);
  - every other F^{ij} is 0.
- Its residual is 4.4e-16 over 2000 random (k, q), and its Hermiticity defect is 0. Its forward F^{xx} tends to v_xc_x (0.860630).
- Its zeroth moment holds with θ = 0, so it is in the deformed class only.

### 3.4 (b) Lemma RB (no band has physical momentum under the redshift bridge). Proved

- By Lemma F, a non-degenerate band a has R_a(k) = Σ_i F^{ii}_{aa}(k,k) = v_a(k)·c_a, with c_a constant (MB-A). Take an IR-regular extremum k₀ and p = k − k₀.
- **Massive (M > 0).** R = c·Mp + O(p²) and p·v = p·Mp + O(p³). Equality at leading order forces Mc = 0, so c = 0. Then R ≡ 0 ≠ p·Mp.
- **Massless (φ > 0 off 0).** R = c·∇φ has degree 0; p·v = φ(p) has degree 1 (Euler). Equality needs c·∇φ ≡ 0, which forces φ(tc) = 0 and contradicts φ > 0, unless c = 0. Then R ≡ 0 ≠ φ.
- **Axis movers (MB-B), any extremum.** R = f′(ĉ·k)|c| against p·v = f′(ĉ·k)(ĉ·p). The homogeneity degrees always differ by one, so RB fails at leading order for every non-flat band.
- So **no band in 𝓜_N satisfying the W2_pf zeroth moment passes (b)**. A homogeneous strain does shift the axis movers' energies: δε = −δa·v·c. But the shift is proportional to velocity, not momentum. Its sign flips for movers going against their label (a blueshift on expansion).
- **Remark 2 (non-symmetric couplings).** Without stress symmetry, the massive and massless cases above still fail. Only bands that are flat along c at leading order escape, and those are not IR-regular.

**Checked** (`r175_mb.out:26-41`).
- **Axis mover.** R/R_phys = 1/k exactly: 3.33, 10, 33.3 and 100 at k = 0.3, 0.1, 0.03 and 0.01, and −100 at k = −0.01. The same holds at m = 1, 0.3, 0.01 and 0.
- **Physical controls.** These measure the same observable in models known to carry physical momentum:
  - the complete tower (Π = k + G, N = ∞; the continuum): R/R_phys = 1.000000, and δε/(−δa·ε) = 1.000000 for massless states, i.e. ν ∝ 1/a;
  - the single-band G law (g = u′/2): R/R_phys = 1.000000 on its box. It passes RB but fails the zeroth moment (R16-5; rerun identical).
- **Sector c = 0:** R = 0.
- So the method does report redshift where it exists. RB and the zeroth moment are each satisfiable separately on a finite band, but not together.
- **Size** (`r175_mb.out:66-67`). For an axis-mover optical photon at a = ℓ_P (|c| = 1/a; λ = 500 nm and ℓ_P are RECALLED), ka = 2.03e-28. The strain response is 4.9e27 times the physical redshift.

### 3.5 Lattice-translation test (bridge-free; prior-art tool). Proved

- For continuous finite-band Π_j, e^{i tr Π_j(k)} has zero winding around the k_j cycle. A lattice translation acts as e^{ik_j}W, with W k-independent and internal, and has det-winding N.
- So exp(iP_j) is never a lattice translation, with or without W2_pf. This is I1's determinant-winding tool (`C4_I1_referee.md:21`), counted once.
- **Checked** (`r175_mb.out:49-53`): the winding is ≤ 4e-16 for all four families, against the required N = 4, 2, 4 and 6.

### 3.6 Lemma R (standard rotation bracket ⇒ Π ≡ 0). Proved, given integrability

- Suppose the FDiff rotations keep their standard bracket [J_a, P_b] = iε_abc P_c, integrated to e^{iαJ}Pe^{−iαJ} = R(α)P. The integrability is assumed, as in I1.
- Unitary conjugation preserves joint spectra, so the finite label set C (MB-A) would equal R(α)C for all α about two axes. That forces C = {0}, so Π ≡ 0.
- So in the "deformed translations, standard rotations" class (θ any, rotation sector standard), only R16-5's trivial solution survives, now for every N.
- **Checked** (`r175_mb.out:42-47`): spec(cos α Π_x + sin α Π_y) differs from spec Π_x by 0.259, 0.500 and 0.707 at α = π/12, π/6 and π/4, and by 0 at π/2.

### 3.7 (a) and (c)

- **(a) Can the six-band construction be completed?**
  - **Standard W2_pf: no completion exists** in 𝓜_N, any N (Corollary S, proved).
  - **Deformed class (θ = 0): the W1_pf + zeroth-moment level is achievable only by axis movers** (MB-B, proved; explicit example checked).
  - Class 𝒟 specifies nothing beyond the zeroth moment (`C5_R16-5_report.md:55`), so a "complete" deformed algebra is not further defined. With standard rotations it collapses to Π ≡ 0 (Lemma R).
- **(c) Not reached.** No completion passes (b), so no pole split is computed. R13-5's numbers stay W1-scoped (`vR16-5:23`).

### 3.8 Escapes, and what would work

Each is outside 𝓜_N or H-gen:
- **P64, the complete tower:** passes both tests (control, §3.4).
- **P90, a discontinuous symbol:** 1/n tails, a face delta, no umklapp (`C5_R16-5_report.md:234-238`).
- **Non-multiplier generators** (3D component mixing; field-dependent, altered or non-block-diagonal generators): untested. The MB-A partner step breaks there, because mixing terms enter at the same order q as θ. Open.
- **Non-universal θ per species:** impossible with one graviton. It would need non-universal coupling (P91-type).
- **Flat-along-c bands:** not IR-regular, so not physical matter. Comparator: every observed particle propagates isotropically (RECALLED).

## 4. Against the FIXED readings (`TESTS:5864-5867`)

**Worker reading: EXCLUDED-MB, which needs a referee.**
- **The stated class.** 𝓜_N for every finite N, with continuous quasi-local kernels, multiplier-generated shifts (standard or deformed θ), W1_pf with the symmetric coupled stress, and a projectable lapse. It contains the six-band, C₂-exchanged and twisted families.
- **The no-go.** Every member satisfying the W2_pf zeroth moment (necessary in this class, `vR16-5:9`) fails physical momentum under each of three stated bridges:
  - standard θ (Corollary S);
  - the lattice translation (§3.5);
  - RB (Lemma RB).

  Under the standard rotation bracket it is trivial outright (Lemma R).
- **If the referee does not confirm, the reading is OPEN.**
- **SPLIT-PRESENT and SPLIT-ABSENT are not available.** Each needs a W2_pf-complete multi-band stress that passes (b), and none exists in the class.

**Against the expectation (`TESTS:5868`).** As expected: "k-independent spectra … labels bands rather than carrying kinetic momentum … fails (b)". Not expected:
- W1_pf alone already forces the six-band completion into one-directional movers (MB-B);
- the rotation sector kills even the label (Lemma R).

## 5. Round-17 rules (`TESTS:5688-5706`)

- **Whole-zone v_max** (`r175_mb.out:55-60`):
  - axis mover ε = √(m² + 4 sin²(k_x/2)): 0.618 (m = 1), 0.861 (0.3), 0.995 (0.01), 1.000 (0), along its axis, and 0 transverse;
  - G control: 1.0000.
- **Gauge fields too.** R9-9's graviton enters only through θ; its v_max is not used or recomputed. A finite-band photon is inside 𝓜_N as matter (massless, positive energy), so the theorems cover it.
- **Self-force.** No frame-tied kernel is introduced. P commutes with H, so there is no O(κ⁰) self-force. O(κ) is not computed.
- **Standard or deformed.** Each statement says which: S is standard; MB-A, MB-B and RB hold for any θ; R assumes standard rotations.
- **Counting conventions; enforced or stipulated.** Not applicable: no tuning count and no Λ mechanism.
- **Physical controls.** The tower (continuum) and the G single band measure the same strain response (§3.4).
- **Readout bridges.** RB is named as a hypothesis on `AX:187`, and two bridge-free tests are added.
- **Forks.** MB-B's dichotomy (c = 0 or axis mover) is exhaustive in 𝓜_N. It excludes, with reasons:
  - mixed labels on one band (impossible: a 1-dim eigenspace);
  - k-varying labels (MB-A);
  - N = ∞, discontinuous Π and non-multiplier generators (outside the class).
- **Generic GR comparison.** No initial-state or memory claim is made.
- **Changed hypothesis.** Single-band is removed. Cubic and C₂ covariance are no longer used by MB-A, MB-B or RB (only by Lemma R's continuum extension). Kept: continuity, quasi-locality, multiplier-generated shifts.

## 6. Prices (named, not adopted)

- **P64 (tower)** and **P90 (discontinuous symbol)**: unchanged, counted once.
- **P-r175a, altered shift generators.** Constant FDiff shifts generated by something other than a multiplier action of ∫T^{0j}: component mixing, field-dependent or altered generators. It is the only finite-band local route left. Unpriced and untested. It touches the source/action gate (`AX:187`).
- **Exclusion, not a price.** One-directional (axis-mover) matter: no observed particle propagates along one axis only (comparator, RECALLED).

## 7. Strong-word check

- **"Proved":**
  - MB-A (any degeneracy; continuity and multiplier class);
  - Corollary S;
  - Lemma F;
  - MB-B (the branch step uses a standard RECALLED perturbation fact);
  - Lemma RB (IR-regular extrema; axis movers at any extremum);
  - §3.5 (prior-art tool);
  - Lemma R (integrability assumed).
- **"Checked":** every number cited from `r175_mb.out`, and the R16-5 rerun.
- **"Every / no":** only within 𝓜_N, H-ker, H-gen and H-W1 (and H-RB where stated).
- **RECALLED:** ℓ_P, λ = 500 nm, the isotropy comparator, and Kato's degenerate first-order fact.
- **Not claimed:** interacting matter, N = ∞, mixing generators, the pole split, and anything about non-projectable lapse.

## 8. For the referee

1. MB-A's partner step and the λ_max chain at degenerate points: is uniform continuity of F^{0j} enough, with no spectral-gap hypothesis?
2. MB-B: symmetric F^{(ij)} ⇒ v ∥ c, and the Lipschitz-branch step at degeneracies.
3. Is RB, an instantaneous forward strain response near an IR-regular extremum, an acceptable statement of the redshift bridge? The other two bridges do not depend on it.
4. Does the pair-grading extension to positive-energy massless bands hold (ω_pair > 0 almost everywhere)?
5. Scope: is EXCLUDED-MB met, given that the class is "multiplier-generated" (the item's KEPT hypothesis) and mixing is excluded?

## 9. Files

- `S/scripts/r175_mb.py` and `S/scripts/r175_mb.out`. Blocks:
  - (1) six-band zeroth moment;
  - (2) MB-A spectral test;
  - (3) stress symmetry and the axis-mover W1 completion;
  - (4) RB with controls;
  - (5) rotation lemma;
  - (6) winding;
  - (7) v_max;
  - (8) the multi-band forward formula;
  - (9) size at a = ℓ_P.
- `S/r165_recheck/{r165_tpf.py, r99_profiles_copy.py, r165_tpf.out, rerun.out}`: the R16-5 rerun, identical.
