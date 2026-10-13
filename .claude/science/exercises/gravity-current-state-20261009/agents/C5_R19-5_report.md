# C5 R19-5 report: exact W1 for U, UD and VW, and the fate of the SM root

**Author and status.**
- Written by a Claude Opus 5.5 probe, the same model family as the supervisor and every other C5 worker.
- Unrefereed. Written 2026-10-13, 04:12Z to 04:45Z.
- No repository file was edited. Nothing was downloaded and no web lookups were made.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R19-5/`.
  - My scripts and `.out` files are in `S/scripts/`.
  - `S/arch9`, `S/arch13_5`, `S/arch16_5`, `S/arch18_5` (also copied to `S/arch18`) and `S/arch18_13` hold unmodified copies of the archived runners.
- Every run used `OMP_NUM_THREADS=2` and took under 80 s. Machine load was 3.3–4.1.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`:
  - C5 method (`:2302-2319`);
  - the round 17/18/19 rules (`:5688-5706`, `:6395-6406`, `:7117-7135`);
  - R9-9 (`:3862-3872`, `:3939-3950`), R13-5 (`:4668-4678`, `:4707-4714`), R16-5 (`:5130-5149`, `:5325-5335`, `:5437-5447`) and R17-5 (`:5849-5868`, `:6179-6191`);
  - R17-12 (`:6339-6362`, `:6601-6611`, `:6795-6801`), R18-5 (`:6631-6653`, `:6779-6789`, `:6964-6969`), R18-9 (`:6847-6869`, `:7044-7057`, `:7284-7296`) and R18-13 (`:7063-7091`, `:7297-7308`);
  - my item (`:7317-7349`).
- `P/agents/`:
  - `C5_R18-13_report.md` (all);
  - `C5_R17-12_report.md` (all) and its verdict;
  - `C5_R18-5_report.md` (all) and its verdict;
  - `C5_R16-5_report.md` (all) and its verdict;
  - `C5_R18-9_referee_verdict.md`;
  - `C5_R13-5_report.md:143-190` and its verdict;
  - `C5_R9-9_report.md:30-111`;
  - `C5_R8-2_report.md:73-92`.

**Runners rechecked (checked).**
- R9-9 `r99_graviton.py` reproduces its archived `.out` exactly, except for the timing line. That includes Construction A's Ward residual ≤ 2.7e-15 (`S/scripts/recheck_r99_graviton.out:17-30`).
- R13-5 `r135_w1_pair.py` and R16-5 `r165_tpf.py` are byte-identical to their archived `.out` files.
- R18-13's `vwface.vertex_geo` is used unmodified. Its full-zone photon rows at N = 128 reproduce R18-13's `vwface_root_lowN.out` (T₂g −3.5145e-3, face1 +0.207057, face2 +0.103155; `r195_corner_N128.out`).

**Labels.** proved (a complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Exact W1 is available. The expectation's "EXACT-IMPOSSIBLE" mixes up W1 and W2.**
   - W15/T_pf forbids the *second-order* identity: the zeroth moment of W2_pf, [P_j, T(q)] = θ_j(q)T(q) (`vR16-5:5-11`).
   - Exact W1 is the *first-order* conservation law ∂_μT^{μν} = 0 with the graviton's divergence D = d(q)e^{iq/2}.
   - These are different identities. Refereed prior art already contains exactly W1-conserved, symmetric, Hermitian, quasi-local stresses:
     - R8-2's Construction A, the scattering channel (`TESTS:3554`; `C5_R8-2_report.md:73-92,192`);
     - R13-5's Lemma P1, the pair channel, for any smooth spatial pair kernel (`C5_R13-5_report.md:143-182`; `vR13-5:3`).
   - R13-5 already joined the two into its class 𝒲_V (`C5_R13-5_report.md:87`).
   - Their momentum generator is P_j = dΓ(∇_j(ε²/2)), a periodic symbol, exactly as T_pf requires. So W1 is exact while W2 fails, and the two facts are consistent.
2. **For massive species, exactness constrains nothing that enters the cone rows (proved; checked for the Dirac case, new).**
   - The one-loop TT rows Ξ (axial and off-axis) are functionals of the spatial **pair** kernel plus the ultralocal seagull. The μ rows come from the stipulated SF.
   - Exact W1 is a pointwise linear condition in (k₁, k₂).
     - In the pair channel it only fixes the time components (P1).
     - In the scattering channel it fixes only data that never enter the TT rows.
   - So every pair kernel has an exact completion, and with it every placement datum:
     - the U stencils;
     - UD's midpoint;
     - own-direction smearings of any sign.
   - **Dirac, new (checked).** I built an exactly conserved Wilson-Dirac stress whose interband block is R18-5's UD, unchanged, on R18-9's refereed retuned Dirac edge. It satisfies W1 for all four ν to ≤ 2.4e-15 over the whole torus at m = 0.3 and 0.01. It is μν-symmetric and Hermitian, and its forward values converge to Lemma F's. The pair block equals UD to 5e-16.
   - **Dirac with own-direction smearing (checked).** Smearing the UD pair block with R18-13's own-direction factors at (w_d, w_o) = (−1.17, −0.196) and (−3, 2) also completes exactly (W1 ≤ 7e-15).
3. **R18-13's P-R18-13c holds only in a restricted class (proved).**
   - Lemma S is correct: superpotential improvements of a *fixed* operator cannot move d1 and d2 (`C5_R18-13_report.md:211-226`).
   - But "if exact W1 is required, these two tunings are not available" (`:354`) holds only in the **channel-tied class**, i.e. one fixed operator plus identically conserved improvements.
   - In the class the registered setting describes (δS/δh of a linearly gauge-invariant lattice action, a general local bilinear), the pair kernel and the scattering kernel are independent. There the own-direction data survive exactness: the Dirac case is the explicit counterexample.
4. **The photon has one extra step: the both-soft corner (proved in outline; row cost checked in sample).**
   - For the gapless photon, the W1 operator is invertible everywhere except in two places:
     - on the scattering shell ω₁ = ω₂, which is fixable in the scattering channel by division;
     - at the corner k₁ = k₂ = 0.
   - At the corner the channel split is singular.
   - The completion therefore replaces VW's pair kernel by the continuum Maxwell kernel on a small cube U_r around the corner, and keeps it unchanged elsewhere.
   - Cost to the rows, per vector, at the root photon (N = 128):

     | r | largest row change |
     |---|---|
     | 0.1 | ≤ 8.7e-8 |
     | 0.2 | ≤ 2.9e-6 |
     | 0.4 | ≤ 5.6e-5 |

     The change scales roughly as r⁴–r⁵. For 12 vectors at r = 0.1 it is about 1e-6, the same size as the root's own numerical residual.
   - This step is a proof outline. I did not build the photon completion numerically.
5. **The R18-9/R18-13 root.**
   - The scalar and Dirac rows are identical under exact vertices (proved).
   - The photon rows move by O(r⁴). By transversality the root persists with knob shifts that vanish as r → 0 (suggested; not re-solved).
   - The bill is unchanged: 6 equality tunings + 1 window selection. Exactness adds no tuned numbers, only untuned law data (the scattering kernel; r).
6. **Worker reading: OPEN.**
   - EXACT-IMPOSSIBLE is refuted for the gapped species by explicit construction, and argued false for the photon.
   - EXACT-KILLS is contradicted in the decoupled class.
   - EXACT-SURVIVES is met for the scalar and Dirac parts (proved; checked). For the photon it rests on the corner outline and a sampled row estimate, so it is not "checked" as the clause requires.

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Setting (`TESTS:7330-7335`).** Free scalar, Wilson-Dirac D1 and lattice Maxwell (R17-12) fields on the subluminal root edges, coupled at linear order to R9-9's N-type graviton:
- (h_ij, N_i, N);
- divergence symbol D_j(q) = d(q_j)e^{iq_j/2}, with d = q on |q| ≤ 1 and 2 sin(q/2) beyond 2.5 (`C5_R9-9_report.md:34-37`).

**W1 (exact).** R13-5's (W1-s), now as an operator identity in every channel, for ν = 0..3:

  h(k₁)M^{0ν}(k₁,k₂) − M^{0ν}(k₁,k₂)h(k₂) = Σ_j D_j(k₁ − k₂)M^{jν}(k₁,k₂),

where T^{μν}(q) = Σψ†(k₁)M^{μν}(k₁,k₂)ψ(k₂). The conditions carried with it:
- (H-sym) M^{j0} = M^{0j} and M^{ij} = M^{ji};
- (H-E) M^{00}(k,k) = h(k);
- Hermiticity M(k₂,k₁) = M(k₁,k₂)†.

Scalars and photons are the same statement in their (φ, π) or (E, B) bases.

**Noether/Hilbert reading (proved; mechanism is prior art).**
- An exactly W1-conserved bilinear stress is δS/δh of S = S₀ + ∫(N T^{00} + N_iT^{0i} + ½h_ijT^{ij}).
- That action is gauge-invariant at O(h⁰ξ) under R9-9's transformation, with the matter canonical transformation generated by ∫ξ_νT^{0ν}. This is R9-9 §3.2's absorption argument (`C5_R9-9_report.md:101`).
- Conversely, the gauge invariance of such an action implies W1.
- So "the stress is δS/δh of a lattice action, exactly conserved" is the same as "an exact W1 kernel". The action is quasi-local iff the kernels are smooth.

**Two classes.**
- **(𝒢) General local bilinear.** The couplings of h to φφ, φπ and ππ (or EE, EB, BB, in any channel) are independent smooth kernels. In the mode basis the scattering and pair channels are independent.
  - For a real scalar, the scattering and pair coefficients are A/(2√(ε₁ε₂)) ± B√(ε₁ε₂)/2 plus the φπ terms, with A and B independent. This is the class of Lagrangians coupled linearly to h.
- **(𝒯) Channel-tied.** One fixed operator (U, UD or VW as written, i.e. Maxwell products, 𝔇 or 𝒮) plus identically conserved improvements.
  - Here one kernel feeds every channel. This is the class used implicitly by Lemma X, Lemma D and Lemma S (`C5_R17-12_report.md:149-167`; `vR18-5:7`).

**Locality.** "Smooth" means C^∞ in (k₁, k₂), hence super-polynomially local, matching the graviton's own non-analytic symbol (R9-9's price, counted once).
- Kernels built from the D1 band inherit D1's regularity.
- The D1 W(k) is tabulated in the archived `dirac.py`; that limits the forward-value test below (O(q) convergence), not the exactness test.

**Rows.** The rows are those of R18-9/R18-13: Ξ_T2g, Ξ_Eg, face1 and face2 (body follows), plus μ_E and μ_T2 under SF.
- At one loop in the supplied vacuum, Ξ_e = ∂_{q²}Π_e + ∂_{ω²}Π_e with Π_e = −⟨Σ|e:V_pair|²/E⟩ + seagull. Only the **spatial pair kernel** enters; T(q)|0⟩ has only pair parts.
- The ultralocal seagull adds no q or ω dependence.
- Time components do not enter e:T for spatial TT e, by Lemma W0's block structure (`vR13-5:5`).

**Other conditions.**
- Excluded: M, V0, VU, VM; pairing.
- Signs of law data (`TESTS:7128`): every placement weight may be signed, as in R18-5/9/13.
- v_max: edges are unchanged from R18-9 (`vR18-9:15`).
- Locality of vertices: unchanged pair kernels, so Lemma M / M′ status is as in R17-12/R18-5. The photon corner kernel is the continuum one, which keeps VW's face zero (it has c = 1 only near k = 0).

**Removed hypothesis (`TESTS:7337`):** conservation only at O(q).

## 2. Prior art (each counted once)

- **R8-2 Construction A** (`C5_R8-2_report.md:73-92`; verdict `TESTS:3554`):
  - an exact W1, symmetric, Hermitian, quasi-local number-conserving stress for single-band matter, built from a dust kernel F^{00}u⊗u with telescoping divided differences;
  - "W1 is linear and pointwise in (k, q)", with partition-of-unity glue.
  - My gluing principle and my scattering-channel division are this, generalized.
- **R13-5** Lemma P1 and corollaries C1–C3 (`C5_R13-5_report.md:143-182`; `vR13-5:3`):
  - pair-channel completion of any smooth spatial pair kernel for m > 0;
  - "the pair stress is a law datum";
  - "the fermion pair channel … completes the same way. That is argued, not run" (`:181`).
  - R13-5's channels are Construction A plus P1 (`:87`). So **U already had an exact completion in refereed prior art**. The later "no exact completion constructed" statements (`vR17-12:15`, `vR18-5:20`, `vR18-9:21`) are right for VW and UD, but for U they missed this.
- **R9-9** §3.2: the lapse/shift absorption, i.e. the Noether reading (`C5_R9-9_report.md:101`).
- **R16-5 T_pf / W15** (`vR16-5:5-11,25`), **R17-5** (`TESTS:6179-6191`), **R18-4**: the W2 translation jet. Not W1.
- **R17-12:**
  - Lemma F, the forward test (`vR17-12:5`);
  - Lemma I, stencils differing by superpotentials (`vR17-12:15`);
  - the scope note "outside 𝔐 a scattering-only correction … could repair VU's forward values while keeping its pair vertex" (`C5_R17-12_report.md:164-167`).
- **R18-5:** V0* (`C5_R18-5_report.md:54`); P-R18-5b, "Lemma F fixes only the band-diagonal contraction, not the pair block" (`vR18-5:7`).
- **R18-9** root and transversality (`vR18-9:5-13`). **R18-13** Lemmas O and S, and P-R18-13c (`C5_R18-13_report.md:180-226,354`).
- **Lattice energy-momentum tensor literature** (Caracciolo et al.; RECALLED, not checked): a lattice EMT built from the naive (geometric) operator is not exactly conserved, and conservation needs extra operators and renormalization. That matches class 𝒯's difficulty, not class 𝒢's.
- **Grep.** I searched `P/agents/*.md` and `TESTS.md` for "exact W1", "Construction A", "dust kernel", "both-soft"/"soft corner" and "fermion pair channel". No exact Dirac or photon completion exists, and the combination R8-2 + P1 is used only for scalars in R13-5.

---

## 3. Results

### 3.1 (a) Exact completions

**Lemma G (gluing; prior art, R8-2).**
- W1, (H-sym) and Hermiticity are pointwise-linear in (k₁, k₂). At each point the solution set is affine.
- Smooth local solutions near every point therefore glue, by a smooth partition of unity on T³×T³, into a smooth global solution.
- Hermitization ½(M(k₁,k₂) + M(k₂,k₁)†) preserves W1, because D(−q)* = −D(q). Proved, and checked below.
- Cubic averaging preserves W1 when the graviton's gauge structure is covariant, as R9-9 states (`C5_R9-9_report.md:83`).

**Lemma Div (symmetric division in the scattering channel; proved).**
- Let V^i(k, q) be smooth with V(k, 0) = 0, and let ∂_{q_j}V^i(k, 0) be symmetric in (i, j).
- Then there is a smooth symmetric S^{ij} with Σ_jD_j(q)S^{ij} = V^i.
- Proof:
  1. Near q = 0, use Hadamard division in the ideal (D₁, D₂, D₃), which has a single simple common zero: V^i = Σ_jD_jA^{ij}.
  2. The antisymmetric part A^{[ij]} vanishes at q = 0 (that is the symmetric hypothesis), so A^{[ij]} = Σ_lD_lC^{ijl} with C antisymmetric in (i, j).
  3. Set S = A^{(ij)} + Σ_lD_l(C^{ilj} + C^{jli}). Then Σ_jD_jΣ_lD_l(C^{ilj} + C^{jli}) = Σ_{jl}D_jD_lC^{ijl}, because Σ_{jl}D_jD_lC^{jli} = 0 by antisymmetry.
  4. Away from q = 0, use (V⊗D̄ + D̄⊗V)/|D|² − (D·V)D̄⊗D̄/|D|⁴.
  5. Glue with Lemma G. ∎
- For a conserved forward energy flux the symmetric hypothesis is Lemma F, so it always holds. R8-2's rank-one dust kernel is a special case.

**Theorem E (gapped matter; proved).**
- Let the band be smooth with E ≥ m > 0: scalar, or Wilson-Dirac with degenerate bands handled through the smooth projectors P±.
- For **any** smooth spatial pair (interband) kernel there is a smooth exact W1 completion with (H-sym), (H-E) and Hermiticity, whose spatial pair kernel is the given one. Construction:
  - **scattering blocks (++, −−):** M^{00} = ±½(E₁+E₂)P±P±; M^{0j} by division of ½(E₁² − E₂²); M^{ij} by Lemma Div. The forward values are Lemma F's: ±p_ip_j/E and p_j.
  - **pair blocks (+−, −+):** the given M^{ij}; M^{0i} = ±Σ_jD_jM^{ji}/(E₁+E₂); M^{00} = ±Σ_jD_jM^{0j}/(E₁+E₂). This is P1, with E₁ + E₂ ≥ 2m.
- **Checked** (`r195_dirac_exact.py`, `r195_dirac_exact2.py`; `.out`). Inputs: D1(0.909103708, 0.555604226) (`vR18-9:11`); UD at the midpoint (`C5_R18-5_report.md:109-112`); m = 0.3 and 0.01.

  | test | result |
  |---|---|
  | W1, all ν, near region \|q_j\| ≤ 1 (300 random (k, q)) | ≤ 2.4e-15 |
  | W1, far region with R9-9's full D | ≤ 1.8e-15 |
  | W1, glued over the whole torus (300) | ≤ 2.3e-15 |
  | μν symmetry | ≤ 1.2e-16 |
  | Hermitized W1 | ≤ 2.4e-15 |
  | interband block − UD(midpoint), 100 points | ≤ 5.6e-16 |
  | forward values against Lemma F | 1.8e-2, 1.7e-3, 1.8e-4 at \|q\| = 1e-2, 1e-3, 1e-4 (O(q)) |

- **Scalars.** This is R8-2 plus P1, i.e. R13-5's 𝒲_V (prior art). The rerun gives P1 residuals ≤ 8.2e-15 and Construction A ≤ 2.7e-15 (`recheck_*.out`). It holds for any smooth pair kernel, including R17-4's E1 off-axis U and any stencil.

**Theorem E_γ (photon; proved in outline, not built numerically).**
- Take R17-12's photon (σ = sgn·d, d′ ∈ [0, 1], ω > 0 for k ≠ 0) and any smooth Hermitian covariant spatial (E, B) kernel whose scattering forward values satisfy Lemma F (VW does: `vR18-5:3`).
- Then there is a smooth exact W1 completion whose pair kernel equals the given one outside U_r = {|k₁|_∞, |k₂|_∞ < r} and the continuum Maxwell kernel inside U_{r/2}, for any r < ½.
- Local solvability, point by point:
  - **Off the shell ω₁ = ω₂ and off the corner,** the Sylvester map L(X) = J(k₁)†X + XJ(k₂) of the Maxwell flow J is invertible on physical (transverse) legs. That includes one-soft-leg points: J(0) = 0 and ω_other > 0, so the inverse is a convergent series smooth in the soft leg.
  - **On the shell with both legs hard,** the channel split is smooth. The pair channels are invertible (P1), and the scattering channel is fixed by Lemma Div at q = 0 or by the far formula at q ≠ 0.
  - **At the corner,** use the continuum Maxwell stress at h's site with exact per-leg interpolation. It is exact because σ = k and d = q there, it is C₂-covariant because h's site is fixed by the stabilizer, and the normalized smooth antiperiodic stencils have P ≡ 1 near s = 0.
  - Then glue (Lemma G). ∎ (outline)
- **Not written out:** the constraint bookkeeping (Gauss law, transverse projection) at a soft leg. **Not done:** a numerical construction.
- **Why the corner is needed (suggested).** Near the corner L → 0. For a kernel that differs from the continuum by O(q²) multipliers on some components (stencils, own-direction), P1's time components ~ D·δX/(ω₁ + ω₂) are homogeneous of degree 2 but not C^∞. That gives power-law, absolutely summable tails. Smooth locality forces the continuum kernel there.

**Answer to (a), W15 connection (proved).**
- Exactly conserved stresses exist in the stated class: scalars by prior art; Dirac checked here; the photon modulo the corner clause.
- T_pf is untouched. The constructed P_j = ∫T^{0j} = dΓ(∇(E²/2)) is periodic, so [P_j, T(q)] ≠ θ(q)T(q) and W2_pf fails, as `vR16-5:25` requires.
- W15 forbids exact *second-order* (translation-algebra) identities. It does not forbid exact first-order conservation.

### 3.2 (b) Comparison with U, UD and VW at O(q) and O(q²)

- **Spatial pair kernel.**
  - Identical to U and UD at all orders in q (proved; UD checked to 5.6e-16).
  - Identical to VW outside U_r.
  - Hence the O(q²) TT data entering Ξ are identical, up to the photon corner term (§3.4).
- **Scattering kernel.**
  - Equal to the tied operators' scattering parts at O(q⁰): Lemma F, which U, UD and VW pass (`vR18-5:3`).
  - Different at O(q) and beyond, where the tied operators are not shown to be conserved.
  - It does not enter any row.
- **Time components.** These are new: P1 time components for the pairs, divided-difference fluxes for the scattering channel. They do not enter the TT rows.

### 3.3 (c) Placement data under exactness

| datum | class 𝒢 (Noether, general bilinear) | class 𝒯 (fixed operator + improvements) |
|---|---|---|
| VW axial stencil a (photon) | survives; inside U_r replaced by λ = 0 (row cost O(r⁴)) | survives if any exact completion exists (Lemma I, `vR17-12:15`); none is known |
| own-direction w_d, w_o (photon) | survive; same corner caveat | **removed** (Lemma S, `C5_R18-13_report.md:211-226`) |
| own-direction on UD (Dirac) | survives exactly (checked: W1 ≤ 7e-15 at (−1.17, −0.196) and (−3, 2); `r195_dirac_owndir.out`) | removed (Lemma S) |
| UD midpoint, U stencils, P-R18-5b pair block | survive exactly | midpoint: Lemma I-type, if completion exists (suggested, `C5_R18-5_report.md:243`) |
| scattering kernel beyond Lemma F | free law datum, row-irrelevant | fixed by the operator |
| Lemma F forward values | fixed (scattering only) | fixed, and through the tie they fix the q = 0 pair vertex (Lemma X) |

- **Reading.** In 𝒢, exact W1 removes **no** row-relevant freedom. The rows are pure pair-kernel law data, which is R13-5's C3, now with exact rather than O(q) conservation.
- That also means Lemma F selects vertices only in tied classes: V0's and VU's pair blocks are admissible exact law data in 𝒢 (count once with `C5_R17-12_report.md:164-167` and `vR18-5:7`).
- In 𝒯, exactness is unestablished for every member: no exact completion of the Maxwell-product or 𝔇 operators is known. If one exists, Lemma S removes the off-axis placement route.

### 3.4 (d) The R18-9/R18-13 root

- **Scalar and Dirac rows.** Identical under the exact vertices (proved: the pair kernels are unchanged and μ is SF). The numbers are R18-9/R18-13's.
- **Photon rows.** The completion changes them only through U_r, where VWa-geo with (a, w_d, w_o) is replaced by the continuum kernel.
  - For Ξ only O(q²) matters, so the continuum kernel is VWa-geo with a = −1/8 (λ = 0) and w = 0.
  - Root data: a = −0.176095 (`vR18-9:11`); (w_d, w_o) = (−1.171554, −0.195418) (`C5_R18-13_report.md:58`).
  - Change per vector (`r195_corner.py`; masked pair sums, R18-13's Richardson):

    | row | N = 64, r = 0.2 | N = 64, r = 0.4 | N = 128, r = 0.1 | N = 128, r = 0.2 | N = 128, r = 0.4 |
    |---|---|---|---|---|---|
    | T₂g | 5.5e-7 | 1.3e-5 | 3.5e-8 | 7.9e-7 | 1.4e-5 |
    | E_g | 4.7e-7 | 1.1e-5 | 2.9e-8 | 7.1e-7 | 1.3e-5 |
    | face1 | 1.4e-6 | 4.6e-5 | 8.7e-8 | 2.9e-6 | 5.6e-5 |
    | face2 | 8.7e-7 | 2.7e-5 | 5.4e-8 | 1.7e-6 | 3.3e-5 |

  - **Scaling.** The successive ratios give r^4.2 to r^5, consistent with the O(r⁴) estimate λ·⟨ω⟩ over U_r.
  - **Resolution.** At r = 0.1 the cube has about 2 grid points per side, so the values are size estimates, not converged numbers. The N = 64 → 128 change at r = 0.2 is a factor of about 2.
  - **Mask artefact.** The masked corner row values themselves (2.7e-4 at r = 0.1) come from the mask boundary at q ≠ 0. They cancel in the same-mask differences (suggested).
- **Root survival (suggested).**
  - Twelve vectors at r = 0.1 give a total change of about 1e-6. That is at the root's own numerical residual: 1.7e-6 at the stored point (`vR18-9:7`) and face totals of 1.7e-6 (`C5_R18-13_report.md:58`).
  - The root is transversal: det J = −3.2e-4 and σ_min = 6.3e-4 for the axial rows (`vR18-9:13`); det 11.6 for the off-axis 2×2 (`C5_R18-13_report.md:280-282`).
  - By the implicit function theorem, an exact-vertex root exists with knob shifts O(r⁴/σ_min) → 0. Not re-solved.
- **Bill (reading, per-datum basis).**
  - Unchanged: **6 equality tunings + 1 window selection = 7 continuous law knobs** (`C5_R18-13_report.md:299`).
  - Exact W1 adds no tuned numbers. It adds untuned choices: the scattering kernel (any kernel with Lemma-F forward values) and the corner radius r (any small r).
  - Still unpaid: the LV tadpole, the CC, W2 (W15), the seagull's own Ward status, and two loops.

### 3.5 (e) Prices (named, not adopted)

- **P-R19-5a (new): channel-decoupled stress.**
  - What it costs: exact W1 with the root's placement data requires the stress's pair and scattering kernels to be independent law data (class 𝒢). Equivalently, h couples to ππ/φπ (EB) structures, not only to one geometric operator.
  - What it replaces: it is the exact version of R13-5 C3 and P-R18-5b.
  - Gates: source/action `AX:187`; dynamics downstream `AX:114-130`; qualification `AX:85-90`.
- **P-R19-5b (new, photon): the soft-corner continuum clause.**
  - What it costs: on a neighbourhood of k₁ = k₂ = 0 the photon pair kernel equals the continuum Maxwell kernel at h's site. That needs smooth antiperiodic stencils with P ≡ 1 near s = 0 there, so the stencils are not finite-range there.
  - Row cost: O(r⁴); no tuning.
  - Alternative: absolutely summable but power-law time components (suggested).
- **Correction to P-R18-13c (`C5_R18-13_report.md:354`).** "If exact W1 is required, Lemma S removes the placement route" holds only in class 𝒯. In 𝒢 the route survives.
- **Correction to the R19-5 expectation (`TESTS:7349`).** Exact W1 is available, so the O(q) convention is not "the best attainable". What W15 prices is exact W2.
- **No axiom text changes.** No sizes at a = ℓ_P are quoted.

---

## 4. Against the FIXED readings (`TESTS:7345-7348`)

**Worker reading: OPEN** (unrefereed).

| reading | status |
|---|---|
| **EXACT-SURVIVES** ("exact completions exist, and the SM all-rows root survives with exact vertices. Checked.") | **Partly met.** Scalar (prior art, rechecked) and Dirac UD (new, checked to 2.4e-15): exact completions exist, and their rows are identical to the O(q) root's, proved. Photon VW: existence proved in outline only (§3.1, Theorem E_γ); the row change from the corner clause is checked in sample (≤ 8.7e-8 per vector at r = 0.1); root persistence is by transversality, not re-solved. The "checked" clause is not met for the photon. |
| **EXACT-KILLS** | **Not supported.** In the Noether class 𝒢 exactness removes no row-relevant placement freedom: explicit Dirac counterexample, own-direction (−3, 2) completed to 7e-15. In class 𝒯, Lemma S would remove w_d and w_o, but no member of 𝒯 has an exact completion, so the premise is empty there too. |
| **EXACT-IMPOSSIBLE** | **Refuted** for the gapped species (constructions checked) and argued false for the photon. W15/T_pf concerns W2, not W1 (§3.1). |
| **OPEN** | **Met (otherwise).** |

**Expectation (`TESTS:7349`), "EXACT-IMPOSSIBLE for the translation part": refuted.** T_pf forbids the translation *algebra* (W2_pf's zeroth moment), not exact conservation. The exactly conserved stresses here have periodic momentum symbols and fail W2, as T_pf says they must.

**What would close the item to EXACT-SURVIVES (checked):**
1. A numerical field-basis construction of Theorem E_γ for VW: Sylvester inversion, shell division and the corner glue, with W1 checked to machine precision.
2. A re-solve of the 6-knob root with the corner-clause photon at r ≈ 0.05–0.1.

## 5. Strong-word check

- **"Exact"** means an algebraic identity holding to machine precision with smooth kernels.
  - Dirac: checked (≤ 7e-15).
  - Scalars: prior art, rechecked.
  - Photon: outline only.
- **"Any smooth pair kernel"** is said only for gapped bands (E ≥ m > 0), where it is proved.
- **"Proved"** is used for: Lemma G (prior art), Lemma Div, Theorem E, the Noether equivalence, Hermitization, and the W1/W2 distinction. Each is a short argument under the stated hypotheses. Theorem E_γ is an outline with a step not written out.
- **"Refuted"** (EXACT-IMPOSSIBLE) rests on explicit constructions, not on a no-go.
- **"Survives"** for the photon is suggested (implicit function theorem; sampled, under-resolved corner sizes).
- **Not claimed:**
  - exact W2;
  - the seagull or tadpole;
  - uniqueness of the completion;
  - that class 𝒯 has no exact member;
  - a re-solved root;
  - anything at two loops;
  - the m = 0.001 root, which follows identically for the gapped parts and was not run for the photon corner.

## 6. For the referee

1. **The W1/W2 distinction.** Does any reading of the registered setting make "exact W1" mean W2_pf's zeroth moment? If not, EXACT-IMPOSSIBLE as worded is excluded by R8-2 + P1 (scalars) and by Theorem E (Dirac).
2. **Class 𝒢 versus 𝒯.** Is a general local bilinear the right reading of "δS/δh of a lattice action coupled to h at linear order"? Real-scalar algebra: the ππ coupling decouples the channels.
3. **Lemma Div**, especially the antisymmetric-part step. Theorem E's block construction, including the hole sign (`r195_dirac_exact.py` docstring).
4. **Theorem E_γ.** The one-soft-leg Sylvester invertibility with Gauss-law bookkeeping, and the corner continuum kernel's C₂ covariance.
5. **The corner row sizes** (`r195_corner.py`). The masked Richardson is under-resolved at r = 0.1.

## 7. Files (`S/scripts/`)

- **Dirac completion:**
  - `r195_dirac_exact.py` → `.out` (near region; Hermitization; continuity);
  - `r195_dirac_exact2.py` → `.out` (forward O(q); pair block = UD; far region; glued torus);
  - `r195_dirac_owndir.py` → `.out` (own-direction-smeared UD, exact). Its `.out` first repeats `r195_dirac_exact2`'s checks, because it imports that module.
- **Photon corner:** `r195_corner.py` → `r195_corner_N64.out`, `r195_corner_N128.out`.
- **Runner rechecks:** `recheck_r99_graviton.out`, `recheck_r135_w1_pair.out`, `recheck_r165_tpf.out`.
