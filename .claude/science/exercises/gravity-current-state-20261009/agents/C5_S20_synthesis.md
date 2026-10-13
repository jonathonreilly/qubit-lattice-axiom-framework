# C5 S20: synthesis after rounds 15–16 (refereed: R15-1 … R15-6, R16-1 … R16-9; R16-10 … R16-14 pending)

**Author and provenance.** Claude Opus 5.5 (S20). This is the same model family as every C5 worker, the supervisor and S5/S8/S11/S14/S17. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict, as recorded in `TESTS` or in the cited `C5_*_referee_verdict.md`. The one exception is R16-9's verdict, which is not yet in `TESTS` (see the pending table). Written 2026-10-12 23:47Z to 2026-10-13 00:05Z. No repository file was edited.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `agents/C5_S17_synthesis.md`, the base for this synthesis.
- `TESTS:4924-5664`: everything from "C5 Round 15" to R16-14, including pre-registrations, worker readings and referee records.
- `SUMMARY:677-714` (§26).
- Referee verdicts `C5_R15-1` … `C5_R15-6` and `C5_R16-1` … `C5_R16-8` (`_referee_verdict.md`). The R16-6/7/8 files in `agents/` are byte-identical to `scratchpad/C5/ref_R16-{6,7,8}/REFEREE_VERDICT.md` (checked with `cmp`).
- The R16-9 referee's full verdict, `SP/ref_R16-9/R16-9_referee_verdict.md` (cited as `vR16-9`).

**Read in part.**
- Price sections:
  - `C5_R15-1_report.md:249-256`, `C5_R15-2:252-261`, `C5_R15-3:218-226`, `C5_R15-4:313-336`, `C5_R15-5:253-261`, `C5_R15-6:291-298`;
  - `C5_R16-1:297-301`, `C5_R16-2:263-298`, `C5_R16-3:236-293`, `C5_R16-4:293-313`, `C5_R16-5:232-241`, `C5_R16-6:1-66,239-252`, `C5_R16-7:22-33,259-280`, `C5_R16-8:298-322`, `C5_R16-9:1-80,200-300`;
  - `C5_R16-10_report.md:19-51,236-262`, `C5_R16-11_report.md:26-57,278-327` and `C5_R16-12_report.md:48-70,263-313` (workers; archived in `agents/`, byte-identical to the scratchpad copies).
- Line checks in `C5_R14-5_report.md` (`:51,222,227,303,317-320,338`), `C5_R15-1_report.md` (`:46-47,199-233`) and `C5_R16-7_report.md` (`:224-230,266`).

**Pending, and one verdict not yet in `TESTS`.**

| Item | State at 00:00Z | Where its claim is |
|---|---|---|
| R16-9 (one law, every cone) | **Referee: NOT CONFIRMED; reading OPEN.** Both the full verdict file and the runner's summary `SP/ref_R16-9/REFEREE_VERDICT.md` (00:03Z, same reading) exist; the `TESTS` record does not yet. Used here as **[ref]** | `TESTS:5550-5562` (worker); `vR16-9` |
| R16-10 (Lemma F, λ → 0) | worker archived; referee running | `TESTS:5563-5572`; `C5_R16-10_report.md` |
| R16-11 (dressing transfer) | worker archived (TRANSFERS); referee running | `TESTS:5614-5626`; `C5_R16-11_report.md` |
| R16-12 (W7 fork) | worker archived (OPEN); referee running | `TESTS:5654-5664`; `C5_R16-12_report.md` |
| R16-13 (fermion/photon TT and shear vertices) | worker running | `TESTS:5593-5613` |
| R16-14 (set A noise-fed PPN, E1 and E2) | pre-registered 23:55Z; running | `TESTS:5628-5653` |

**Paths and abbreviations.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS` and `SUMMARY` are in `P/`; bare `C5_*` are in `P/agents/`.
- `vR16-6` abbreviates `C5_R16-6_referee_verdict.md`, and so on. The exception is `vR16-9`, which is `SP/ref_R16-9/R16-9_referee_verdict.md`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `S17` = `C5_S17_synthesis.md`.
- `SP/` = `scratchpad/C5/` (session scratchpad).

**Labels.**
- **[ref]**: referee-confirmed, within the referee's scope.
- **[ref, bounded: …]**: a refereed FAIL, EXCLUDED or no-go, with its class.
- **[worker]**: a worker claim that the referee did not confirm or has not ruled on.
- **[pending]**: R16-10 … R16-14, as in the table above.
- **[S20 reading]**: an interpretation made here. Same model family; unrefereed.

**Sets** (as S8–S17). A = continuum base, discreteness only in records. B = Euclidean Z⁴. C = the axioms' Z³ with continuous time, tuned. C-box = Z³ × ℝ with a box-exact law. C-box-S = C-box with boson–fermion pairing per cell.

**Record-keeping notes.**
- `SUMMARY` §26 (`SUMMARY:677-714`) covers rounds 13–15. It still labels R15-4 and R15-6 as worker results (`SUMMARY:711-714`), but both were refereed at 22:57Z (`TESTS:5301-5324`).
- Round 16 is recorded only in `TESTS`.
- §1 below could serve as the plain-words source for a §27; this synthesis does not write it.

---

## 1. What changed since S17, in plain words

### 1.0 The short version

S17 left five things open: the electron–photon split on usable edges, the graviton's second polarization, a start-time datum, a CMC clock for Λ, and the count of tunings. Since then:

1. **Λ's global clock fails on causality, and the escape is a tuning.**
   - The CMC mechanism lets a local push change the density everywhere at once, whenever it is absorbing a vacuum change [ref, R15-1 FAIL].
   - Switching that off (g ≡ 0) gives exactly general relativity with one constant subtracted. Making that constant the late vacuum is, per the referee, the old counterterm (Lemma PT) again [ref, R16-6 INCONCLUSIVE].
   - [S20 reading] No route on record removes Λ without either faster-than-light influence or a tuned number.
2. **The electron–photon split now has a theorem on the edge physics would use.**
   - On the subluminal Wilson edge D1, the split grows linearly with mass, so it cannot vanish over any range of masses [ref, R16-1 DERIVED].
   - The number of tunings is conditional: 3 with one counterterm per (spin, |q|) class, or 7 with one per species [ref, R16-2 OPEN].
   - A worker finds that 2 suffice if the photon may be faster than light at the grid scale [worker, R16-10].
3. **Both graviton polarizations can be put on the matter cone by shaping the edge. Whether the shear can then use the same edge is OPEN.**
   - A zigzag subluminal edge makes T₂g positive. Two shape tunings zero E_g and T₂g together [ref, R16-3 REFUTED universal negativity].
   - A worker's scans found no edge that also zeroes the shear. The referee calls this credible evidence of tension, not a class-wide conflict [ref, R16-9 NOT CONFIRMED → OPEN].
   - The bill for SM content, 9 + CC (one counterterm per charge class) or 13 + CC (one per species), is arithmetically right but is "conditional bookkeeping", not a demonstrated count. Three of its rows are uncomputed [ref, `vR16-9:19,21`]. R13-8's generic bookkeeping was 16 + CC.
4. **GW170817 is still not a gauge-invariant test on any grid tested.**
   - A preferred-frame second-order Ward identity admits no nontrivial pair stress for single-band matter [ref, R16-5 OPEN with Theorem T_pf].
   - The obstruction moved from boosts to translations.
5. **The graviton is still not produced. The finite-slot window narrowed.**
   - Extra hidden fields: two graviton modes force at least four gapless branches [ref, bounded, R15-3 EXCLUDED].
   - Finite slots with an exact integer vector Gauss law: the TT-electric f-sum is O(k⁴), so no Einstein–Hilbert stiffness through that probe [ref, R16-7 Theorem B, INCONCLUSIVE overall].
   - Sign-free models conserving the scalar charge cannot attract like Newton [ref, R16-7 Theorem D].
   - A worker says the bound survives any quasi-local dressing [worker, R16-11].
   - What is left: law-violating phases with no such dressing, small-N clocks (including literal qubits as Z₂ clocks), and readout bridges.
6. **Set A's start-time route needs an initial datum.**
   - Free gravitational waves present at the start keep their energy forever. One quantum per mode up to 1/ℓ exceeds the ρ_Λ budget by 2.4e3 to 5.9e19 [ref, R16-4 STATE-DEPENDENT].
   - This is generic GR free-data memory, not an E1 mechanism.
   - So E1 must either record nonzero initial TT data or impose zero, which makes the `AX:94` question physical.
7. **W7 (the off-box tail) is still OPEN** [ref, R16-8]. Its 1/r² kernel and 1/r⁴ curvature are real objects, but not shown physical. The (α)/(β) fork is not exhaustive (`vR16-8:9`).
   - A worker finds the translation part repairable. The obstruction sits in the boost bracket, as a world-line Coulomb kernel [worker, R16-12 OPEN].
   - Whether the result reads as "non-local" depends on the variables chosen [worker].
   - Any effect needs edge quanta of at least 1.7e19 GeV [worker].

**[S20 reading], the one-sentence picture.** The campaign's remaining choices are now almost all counted tunings or named non-localities. The two things nobody can yet price are a produced graviton and an untuned Λ.

### 1.1 The electron–photon split (W1)

- **R16-1: DERIVED [ref; `TESTS:5416-5421`; `vR16-1:19`].**
  - **The statement.** At one loop, in Feynman gauge with Peierls coupling and fixed λ > 0, take any box-exact Wilson law with nonnegative, nonzero W, an H2′ photon, and (H3) or (H3′). Then δc_e = Lm + O(1) with L > 0, while the photon part is O(m⁻²). So no interval zero exists.
  - **Covers:** D1 for 0 < r ≤ 1/√3 at b = 1.4, 1.2 and 1.0, and the selectron-only variant P-a. On D1, L·16π² = 0.2265459594 (`vR16-1:5`).
  - **Corrections:**
    - the denominator bound is ≥ λ/2, not ≥ λ;
    - the sharp threshold is b* = 0.504032…, so 0.505 is conservative;
    - (H0) W ≥ 0 is not part of the registered 𝒬_W and defines 𝒬_W⁺ (`vR16-1:5-9`).
  - **Not covered:** P-b (photino loop), λ = 0, photon transitions on the Wilson edge, and the uniqueness of the observed zero at m ≈ 24.0–24.5 (`vR16-1:11-13`).
  - D1's Δ(0⁺)·16π² ≈ −10.877, so a tuning is needed (`vR16-1:11`). D1 is subluminal, with v_max = 1 at r = 1/√3; the R8-5 Wilson boxes are superluminal (v = 3.31 and 4.65) (`vR16-1:15`).
  - **This closes S17's gap.** S17 noted that the DERIVED subclass was the R9-1-excluded literal edge (`S17:63,192`); it now includes the edge physics would use.
  - **[worker]** R16-1 reads D1's corner doublers (m + nW_π, W_π = 0.095/a) as Planckian, so R9-1's Z-width exclusion would not transfer (`C5_R16-1_report.md:301`). No referee has checked a Z width on D1.
- **R16-2: OPEN [ref; `TESTS:5422-5426`; `vR16-2:17`].**
  - **Confirmed:**
    - Lemma Q: the species shift is q_i²F_s(m_i), and the photon shift is one charge-weighted sum, independent of λ and of the internal photon symbol;
    - the scalar runner;
    - Lemma T′: a strictly negative tadpole/seagull bound for non-rising matter symbols with a nondecreasing photon.
  - **Conditional count.** Given class-wide F_s(0⁺) ≠ 0, uniform mass control and additive-counterterm conventions, the nine SM charged Dirac flavours cost 7 tunings (per species) or 3 (per charge class). Residuals are 1.696e-22 and 7.278e-21 (`vR16-2:13`).
  - **Not proved:** class-wide F_s(0⁺) ≠ 0, the λ → 0 bound, the literal-corner accounting, and convention-independent minimality.
  - **Correction: κ_γ is replaceable, not required.** All three matter classes may be tuned instead. A literal-family shape near b₂ = 2.31 also replaces it (`vR16-2:13`).
- **[pending] R16-10, the closure attempt [worker; `TESTS:5563-5572`; `C5_R16-10_report.md:19-51,236-262`].**
  - **Theorem L:** the λ → 0 limit exists jointly with m → 0, with no log. F_s(0⁺) = K_s + Λ_s, with K_0 = −1/3 (closed form) and K_½ = +2/3 (checked).
  - **Dirac REFUTED-ZERO.** Take D1(1.4, 1/√3) with an R8-5 photon whose lattice branch is stiffened by G. This gives F_½(0⁺) = 0 at G* ≈ 3.1264. That photon has whole-zone v_max = 7.35. If superluminal photons are outside "admissible deformations", Dirac is OPEN.
  - **Subluminal photons:** tadpole ≤ −2.02 (proved), with samples ≤ −3.8.
  - **Scalars:** OPEN; every resolved sample is below −1/3.
  - **Count:** n_t = 2 for SM Dirac content with the superluminal photon (G* plus one photon-side condition); 7/3 survives only on the subluminal-photon subclass.
- **[S20 reading] Where W1 stands.**
  - No untuned zero exists in any refereed subclass, now including the subluminal Wilson edge.
  - The cheapest refereed bill is 3 tunings, conditional. The cheapest claimed bill (2) trades the photon's grid-scale causality for 5 tunings. That trade is exactly what S17's subluminality rule was written to expose, and the round-17 rules below extend it to gauge fields.

### 1.2 Producing the graviton (W2)

- **R15-3: EXCLUDED [ref, bounded: finite, continuous, PSD, cubic-covariant Gaussian with any finite auxiliary O-irreps; `TESTS:5184-5189`; `vR15-3:15`].**
  - Two genuine TT branches on an axis and a face diagonal force dim G ≥ 8, hence at least 4 strict gapless branches and two partners.
  - The ≥ 5 bound needs a rank-2 axial TT residue.
  - The minimizer list omitted 4A₁ + 4A₂ (that case disappears only under C3). Lemma N is conditional.
  - **Outside the result:** axis-only aliases, discontinuous symbols, infinite-mode, indefinite/constrained, non-Gaussian, and flat-is-gauge constructions.
- **R15-5: INCONCLUSIVE [ref; `TESTS:5309-5316`; `vR15-5:47`].**
  - **The exact noncompact N-type works but is unreduced-indefinite.** It has a positive two-pair TT quotient with ω² = Jg|q̂|², IR helicity-±2 characters and an attractive 1/r. Its TT projector cannot be continuous at k = 0.
  - **Regular lifted compact-character Hamiltonians give ω = O(k³)** at each liftable finite Schrieffer–Wolff order, provided N > 36nM. This is not "every finite order" for a fixed N (`vR15-5:33`).
  - The GR source would need symmetric, locally conserved matter stress; T′ covers only its stated smooth one-band class (`vR15-5:40`).
  - **The decisive computation is more than a static χ_TT ~ 1/k².** The dual rotor also has 1/k² at z = 2. It needs the dynamical TT spectral function, scalar/vector gaps, and a reciprocal conserved source test (`vR15-5:45`).
- **R16-7: INCONCLUSIVE [ref; `TESTS:5582-5586`; `vR16-7:17`].**
  - **Theorem B (corrected with V^{−1/2} normalization).** For quasi-local rotor or quantum-link H with an exact integer vector Gauss law and summable second moments, the TT-electric f-sum is O(k⁴). A nonvanishing TT-electric susceptibility then forces an E_TT-connected mode with ω ≤ Ck².
  - **What it does not do.** It does not identify the optimized probe ratio with the physical finite-clock metric susceptibility; that needs an observable bridge (`vR16-7:5`).
  - **Theorem D (diamagnetic) holds in Hessian/PSD form.** E-basis stoquasticity plus an exact scalar-shift symmetry gives W(k) ≥ 0, so no pure unscreened attractive inverse Laplacian. It does not make a sign problem the unique escape; scalar-law violation or a different source bridge also escape. The screening formula is inverted: m⁻¹ ≤ √(c/a) (`vR16-7:9`).
  - N0914's displayed Hamiltonian is stoquastic but L-type (`vR16-7:11`).
  - **The control did not pass.** The s2 model is 2D and confining; no 3D emergent-photon susceptibility was measured. So NOT-PRODUCED-EVIDENCE is not permitted (`vR16-7:13`).
  - "Only window" is too exclusive (`vR16-7:15`).
- **[pending] R16-11 [worker; `TESTS:5614-5626`; `C5_R16-11_report.md:26-57,307-327`]: TRANSFERS.**
  - If a quasi-local unitary W (tails Σr¹³Φ(r) < ∞) carries the true ground state into the exact-law sector, the dressed f-sum is ≤ 2S²K₂k⁴.
  - Spin ice is reconciled: the U(1) photon never violated the analogous k² bound.
  - **Gap 1** (observable) narrowed to zero-vertex or non-local curvature readouts. **Gap 2** (U(1) control) not closed.
  - **Left open:** phases with no such dressing, mod-N clocks, rotors, and the scalar channel (Theorem D does not transfer).
- **[S20 reading] Where W2 stands.**
  - Four Gaussian families are closed (X1, X-G, G-mix, auxiliary irreps).
  - The finite-slot integer-law class is closed in its probe form, conditional on a readout bridge, and possibly under dressing (pending).
  - The axiom's own one-site domain is M₂(C). If a site's metric slot is a literal qubit in the Weyl (Z₂-clock) presentation, rather than a spin-½ quantum link with an integer law, it lies in the one window both R16-7 (`C5_R16-7_report.md:228,266`) and R16-11 (`:288`) leave open. R17-1 targets it.
  - P-N1, the supplied CCR graviton, remains the only known source of a light-like TT branch.

### 1.3 The graviton–matter cone and the shear (W3, W4)

- **R16-3: REFUTED in 𝒮; DERIVED on the B″ subclass [ref; `TESTS:5427-5432`; `vR16-3:15-19`].**
  - **Witness Z1:** Ξ_M,T2g = +3.9047e-4 and Ξ_U,T2g = +2.8101e-4 at m = 0.3, on a smooth whole-zone subluminal zigzag edge with v_max(0.3) = 0.98456.
  - **A common E_g/T₂g zero:** for M at m = 0.1, (u, v) = (0.955977637884, 0.024523462318), with residuals < 1.5e-17, v_max = 0.998292503599 and a nonzero Jacobian. This establishes two locally independent tunings in this family, not a universal lower bound (`vR16-3:13`).
  - **Theorem B″:** strict negativity for every admissible weight when every stretch incident to a positive valley has |σ′| ≤ 1/√5.
  - **Tails understated:** the zero law has |ε₁₂₈| = 3.67e-5 (`vR16-3:17`).
  - **Scope:** R9-9's M/U vertex, the assumed standard W1, axial momentum, ultralocal seagull, supplied zero-point vacuum. These are bare-cone shifts, not dressed poles.
- **R16-9: NOT CONFIRMED (the CONFLICT); reading OPEN [ref; `vR16-9:3,21`; worker `TESTS:5550-5562`, `C5_R16-9_report.md:17-31,216-235,279-300`].**
  - **Confirmed:**
    - Lemma R as a continuous occupation-measure relaxation at fixed exact parameters;
    - the necessary inequalities of Lemma R_U;
    - the fast-state identity;
    - the zigzag-Dirac tadpole monotonicity under pointwise ordering (`vR16-9:5-7,11,17`).
  - **One M cell reproduced independently:** μ_E = +1.255274e-3, Ξ_Eg = +2.3137e-4, Ξ_T2g ≈ 6.7e-14 (`vR16-9:13`).
  - **Why OPEN, not CONFLICT:**
    - the scanned finite programs are not proved supersets of the continuous class;
    - local optimizers give upper bounds, not lower bounds;
    - b, lo, hi, s_min and m are sampled, not exhausted;
    - the thin U margin (~1.3e-4) needs a certified enclosure (`vR16-9:5-9`).
  - **Block split:** shown only for the truncated scalar-loop prescription, not for the full SM one-loop problem (`vR16-9:15`).
  - **Bill:** the arithmetic 9 + CC and 13 + CC is right. It is conditional bookkeeping, not a demonstrated minimal count. μ_T2 = 0 is coupling-specific (`vR16-9:19`).
  - The referee's own summary: "credible search evidence for tension" (`vR16-9:21`).
  - **Biggest open item:** Dirac, photon and gluon zero-point vertices. **R16-13 is running on exactly this** (`TESTS:5593-5613`).
- **[S20 reading]** S17's "T₂g never zeroed" is superseded (§5). The graviton cone on the box route now has a shape-only price (P87), within the prescription. Whether P62 (shear by shape) and P87 can both be paid on one scalar edge is OPEN, with numerical evidence against.

### 1.4 GW170817 as a gauge-invariant test (W3, new W15)

- **R16-5: OPEN [ref; `TESTS:5437-5447`; `vR16-5:25`].**
  - **The no-go (Theorem T_pf).** Take massive free single-band matter on T³ with continuous quasi-local kernels, finite smooth pair channels, and constant shifts generated by P = dΓ(g). Then the zeroth moment of W2_pf forces θ = 0 and, by proper cubic rotations, g = 0.
  - Pair terms cannot repair this, because the identity separates by particle-number grade.
  - So **no W2_pf-invariant graviton–matter pole split is available.** The one-loop TT matter part is gauge-parameter-free, the matter pole is unprotected, and R13-5's numbers stay W1-scoped.
  - **Overclaims corrected:**
    - the finite-band extension: a six-band signed-axis construction Π_j = diag(v_j) satisfies the zeroth moment with θ = 0 (`vR16-5:13`);
    - the redshift exclusion of g ≡ 0 is conditional on a source/observable bridge (`vR16-5:19`).
  - **Live counter-routes:** C₂-exchanged bands, general 3D component mixing, singular or non-local generators.
- **[S20 reading]** The boost wall of SUMMARY §17 reappears as a translation wall once boosts are no longer gauge. It is recorded below as W15 so it is not lost inside W3.

### 1.5 Set A (W8)

- **R15-2: OPEN [ref; `TESTS:5177-5183`; `vR15-2:23`].**
  - **Built:** conserved spin-2 noise from a finite start, needing f(0) = f′(0) = 0, which the repaired gain has.
  - **Lemma B:** the initial-value term B repairs the finite-start mean-source defect, and decays for arbitrary data only with a zero first moment.
  - **TT weight:** ¼ of the earlier normalization.
  - **Corrections:**
    - Lemma CU (one common gain) holds only within the channel-diagonal common-profile ansatz;
    - a dropped derivative (K′ = f(t)J₀(0) + f*J₀′) invalidates c₁ = 0.657, the ratio 0.2524 and the budget endpoints, but not the ¼ (`vR15-2:7,13`).
  - **Unproved:** exact full-instrument CP; premise (iii), that constraint-channel noise gravitates. So the 1e12 ρ_Λ overshoot is conditional (`vR15-2:15-17`).
- **R16-4: STATE-DEPENDENT for 𝒢(1, 1/ℓ); OPEN for small classes [ref; `TESTS:5433-5436`; `vR16-4:19`].**
  - **The memory:** free TT data keep their energy. One quantum per polarization for |k| ≤ 1/ℓ gives Δρ = ħc/(4π²ℓ⁴), which is 2.4308e3, 1.5192e6 and 5.9345e19 times ρ_Λ at 5 µm, 1 µm and 0.4 nm.
  - **Generic:** this is undamped linearized-GR free-data memory. The J₀ perturbation decays as t^{−1/2}.
  - **Consequence:** E1 must record nonzero initial TT data or impose zero (P88). Whether imposing zero is an allowed boundary condition or a privileged state is unresolved by `AX:94` (`vR16-4:17`).
  - **Corrections:** the pulse-energy coefficient is 2× too large; Lemma M needs a product-vacuum hypothesis (`vR16-4:7-9`).
  - **[worker]** E2 keeps 95.6–98.5% of initial TT energy at t_H at the drag-allowed γ, so the start question does not separate E1 from E2 (`C5_R16-4_report.md:311-313`).

### 1.6 Λ (W10)

- **R15-1: FAIL [ref; `TESTS:5166-5176`; `vR15-1:19`].**
  - **Lemma S.** With g ≠ 0, the elliptic lapse becomes a constraint-fluid channel. A smooth compact conserved source gives a gauge-invariant remote response with no light-cone delay.
  - **It counts as signalling.** Preferred-time ordering prevents only backward-in-time messages (`vR15-1:7`).
  - **It is unavoidable** during active vacuum compensation (Lemma C).
  - **Ghost band:** g > 6H² at low k is exact. The 1–5H² tachyon thresholds are frozen-background diagnostics.
  - **Lemma F′:** a positive lapse floor N ≳ 1.51875(mH₀)² on each regular slice. It is not a collapse theorem. Global CMC existence is open.
  - **Lemma V:** any-w grid vacuum is absorbed only if the source bridge allows momentum exchange; otherwise ρ_v + p_v = 0.
- **R15-4: bounded FAIL in 𝓡⁺ [ref, bounded: causal linear LTI readers, exact on dust, positive after reheating; `TESTS:5301-5308`; `vR15-4:60`].**
  - **The readers.** D1 and R* repair Prony's singularities. EW and QCD residuals are 7.97e-13 and 8.89e-5. The e⁺e⁻ equivalent shifts are +0.431 (D1) and ≤ +0.156 (R*), not BBN-network results.
  - **Lemma N+:** G(x) ≤ x(4−x)/3, and G ≤ 0 for phantom content. So no reader in 𝓡⁺ tracks the full DESI DR2 CPL histories.
  - **The escape:** inverse reading leaves g/H₀² = −0.289 to −1.085 today. That is active signalling under R15-1 (`vR15-4:52,58`).
- **R15-6: INCONCLUSIVE [ref; `TESTS:5317-5324`; `vR15-6:19`].**
  - MR gives Λ̃ = 0 and g ≤ 0 on H1, but with no uniform influence bound.
  - Theorem L: no linear fading-memory reader exact on dust and radiation keeps g ≤ 0 after sharp releases.
  - 0.05H₀² is a heuristic proxy, not an observational bound (`vR15-6:13`).
- **R16-6: NOT CONFIRMED (the PASS); INCONCLUSIVE [ref; `TESTS:5576-5581`; `vR16-6:64`].**
  - **Theorem Z:** g = (κ/3)(ρ_tot − R)′, so g ≡ 0 ⇔ R = ρ_tot − C, i.e. GR with one constant.
  - Choosing C = ρ_v,late lets earlier phase energy (false vacua, the inflaton plateau) gravitate and avoids signalling.
  - **Why not PASS.** C = ρ_v,late is obtained only by stipulating the law's T = 0 gravitational zero. IE additionally fixes its integration constant to about 1e-120 to 1e-123. Without a derived symmetry, constraint or mechanism, this is Lemma PT's counterterm (`vR16-6:18-28`).
  - **Theorem NA (narrowed):** a causal common reader cannot cancel exactly on two initially indistinguishable branches with unequal late vacua (`vR16-6:54`).
  - The inflation run used a one-exact-state-read reader, not IE as defined (`vR16-6:16`).
- **[S20 reading]** Every Λ route tested on any grid set ends in one of three places: Lemma PT's tuning (R5-3, R16-6), signalling (R15-1), or a q-charge datum (R10-4). Theorem NA suggests why a causal law cannot do better: it cannot know the final vacuum before the history reaches it, so the final vacuum's energy must be a law constant. Making gravity ignore exactly that constant is the tuning. This is unrefereed; R17-3 tests it.

### 1.7 W7, the off-box tail

- **R16-8: OPEN [ref; `TESTS:5587-5591`; `vR16-8:17`].**
  - **Confirmed:** the 1/r² kernel and the Bianchi-fixed non-TT 1/r⁴ linear curvature tail, and box-inertness under a smooth placement.
  - **Not physical non-locality.** The curvature transforms under the completed momentum constraint. No closed degree-3 system or invariant physical domain exists, and no bounded gauge-invariant instantaneous responder exists.
  - **Lemma A is not confirmed broadly.** A local non-dynamical elliptic auxiliary with primary/secondary constraints can follow moving sources without propagating modes; solving its multiplier is non-local (`vR16-8:7`).
  - **The (α)/(β) fork is not exhaustive.** Higher momentum-constraint terms, field-dependent structure functions, constraint-proportional cancellations, canonical relocations and second-class formulations remain (`vR16-8:9`).
  - Whole-zone v_max confirmed: L-box 4.1209, S(1.4) 0.99270, G(1.4) 0.99386, SLAC 0.99848 (`vR16-8:15`).
  - P-pf1 shares the zone-mean root but is a different object (`vR16-8:13`).
- **[pending] R16-12: OPEN [worker; `TESTS:5654-5664`; `C5_R16-12_report.md:48-70,230-313`]. All results at leading order in the Killing sector of class 𝒞.**
  - **Translation sector (Theorem T3):** (β) works. An h-linear singular momentum-constraint term cancels R16-8's term with no new Hamiltonian input, and it is the JJ repair (Lemma J3). Closure is only weak, with 1/r² structure functions.
  - **Lemma C:** every defect-carrying mode must be subluminal. S(1.4) and G(1.4) pass; the superluminal L-box gives a Cherenkov resonance.
  - **Boost sector (Theorem B3, a no-go in 𝒞):** the center-of-energy bracket forces a world-line Coulomb kernel X_T ∝ 1/(q·v) in the boost generator, which is unbounded. So (β) fails in 𝒞.
  - **Lemma W:** the (β) correction is {P⁰_c, W} for one singular W, so "(α) or (β)" depends on the canonical variables. Only constraint-invariant observables can decide, and none is built. This makes the referee's "canonical relocation" explicit.
  - **Escapes outside 𝒞:** non-local H, world-line boost kernels, degree-4 shells, canonical relocations, auxiliary fields.
  - **Size:** defect quanta carry ≥ 1.41/a ≈ 1.7e19 GeV. Their thermal occupation is 10^(−3.3e31) at T_CMB (reading).
- **[S20 reading]** R16-12 confirms what `vR16-8:9` predicted: the fork does not decide W7. The wall now sits in the boost bracket, as SUMMARY §17's root obstruction did, and any physical effect is population-suppressed beyond observability. R17-2 is redrafted around the boost-sector escapes and the missing invariant observables.

### 1.8 The count (W11)

- **R16-9's bill** in R13-8's P,T-even rows (`C5_R16-9_report.md:216-229`). The referee confirmed the arithmetic and called the totals "candidate bookkeeping totals, not established minimal bills" (`vR16-9:19`).

  | Row | Tunings |
  |---|---|
  | Charge matter speeds | 3 per class / 7 per species [ref, conditional] |
  | Axis graviton speed and birefringence | 2 shape tunings [ref] |
  | Off-axis TT anisotropies | 2 [not computed] |
  | E_g shear | 1 non-shape knob (rests on the unproved CONFLICT) |
  | T₂g shear | 0 at one loop, for V3's coupling only [ref, `vR13-8:22`; `vR16-9:19`] |
  | LV tadpole | 1 [not computed] |
  | CC | 1 |
  | **Total** | **9 + CC per class, 13 + CC per species** (R13-8: 16 + CC) |

- **[S20 reading]**
  - With R16-10's superluminal photon (worker), the charge rows would be 2, giving 8 + CC.
  - Under the per-edge zero-point convention (`C5_R16-9_report.md:231-233`), every further edge with zero-point stress adds +3. Under the sum convention, R16-13 may remove the non-shape shear knob.
  - Tuning precisions: ~1e-16 for the charge rows; ~1e-13 relative for the graviton-cone shape tunings (`C5_R16-3_report.md:276`).

---

## 2. Updated wall map

"DERIVED" means a refereed no-go or confirmed lemma in a stated class, including bounded EXCLUDED and FAIL. "OPEN" means no refereed no-go covers the route's class and there is no PASS. "Cheapest named price" is the least expensive price on record that passes the wall. Nothing is adopted. Axiom lines are cited as in S17 (`S17:200`).

| # | Wall | Refereed statement (scope) | DERIVED or OPEN | Cheapest named price | Axiom lines touched by that price |
|---|---|---|---|---|---|
| W1 | **Electron–photon split** (C, C-box, C-box-S) | No interval zero in 𝒬_lit⁻ (R13-7) **and in 𝒬_W⁺ ⊃ D1(0 < r ≤ 1/√3)** (R16-1). Subclass obstructions as S17 (R12-6, R13-1, R13-4(i), R10-5). Count: q²F_s factorization; conditional 7/3 (R16-2) | **DERIVED on the used subluminal Dirac edge; OPEN overall** (P-b, λ = 0, non-Peierls). Count OPEN | P73 refined: **3** (per (spin, \|q\|) class) or **7** (per species), each ~1e-16, conditional on Lemma F [ref]. **2** with a lattice-superluminal photon (P101) [worker, R16-10] | None (dynamics downstream, `AX:114-130`); sizes use `AX:189-190`. P101 gives up lattice-scale causality for the photon (no axiom line; S17 rule) |
| W2 | **Graviton production** | X1 (R11-2); X-G (R13-2); G-mix (R14-4); **auxiliary irreps (R15-3, ≥ 4 branches)**; **finite-slot integer-law TT f-sum O(k⁴) (R16-7 Thm B, probe form; readout bridge open)**; compact-character O(k³) per liftable order (R15-5) | **DERIVED (five bounded exclusions); production OPEN** (R15-5, R16-7 INCONCLUSIVE). R16-11 dressing transfer [pending] | Supplied non-compact CCR graviton (P-N1 = P41/P49) | Qubit `AX:45-53` (`:47`) |
| W3 | **Graviton–matter cone** (bare-cone, prescription-scoped) | Ξ < 0 on 𝒰₀ (R14-3 Thm B) and on B″ gentle-valley laws (R16-3); **universal T₂g negativity REFUTED (Z1); common E_g/T₂g zero by two shape tunings (R16-3)** | **DERIVED in 𝒰₀ ∪ B″; REFUTED as universal; OPEN as a physical (dressed, gauge-invariant) statement** (W15) | **P87 (P-Z): zigzag edge + 2 shape tunings at ~1e-13**, within R9-9's vertex and assumed W1. Or pairing P46 | None for the shape (`AX:116-123`); P-TTV and the supplied vacuum touch the source/action gate `AX:187` and open gates `AX:184-187` |
| W4 | **Shear μ_E** (supplied zero-point vacuum) | Zero per mass on G_w; O((ma)²) common setting (R14-3). Joint zero with P87 on one subluminal scalar edge: OPEN, with credible search evidence of tension (R16-9, `vR16-9:21`) | **Not a wall in the empty vacuum; one tuning otherwise.** Shape-compatibility with the graviton cone OPEN | P62 alone. With P87, the safe price is **P100** (counterterm, pairing, Fock vacuum, or superluminal edge), unless a joint shape zero exists. R16-13 may lift it [pending] | None for counterterm/shape (`AX:116-123`); pairing `AX:47`; superluminal edge gives up P61 |
| W5 | **Lattice-scale superluminality** | Lemma V (odd laws); subluminal repair PASS (R14-1); D1 v_max ≤ 1, equality at r = 1/√3 (R16-1); independent v_max table (R16-8) | **DERIVED (cause) and repaired for matter.** [worker, R16-10] The cheapest Dirac charge-row bill needs a photon with v_max 7.35 | P61 | `AX:57` (quasi-locality, already priced) |
| W6 | **BF photon multiplet** | PHYSICALLY NON-LOCAL in 𝓔 (R13-4(i)) | **DERIVED in 𝓔** (unchanged) | P60 | Dynamics downstream; `AX:57` only under a range reading (S17) |
| W7 | **Off-box gravity tail** | 1/r² kernel; Bianchi-fixed non-TT 1/r⁴ curvature; box-inert under smooth placement; not shown physical; fork non-exhaustive (R16-8). [worker, R16-12] Translations close weakly via (β); boosts need a world-line kernel in 𝒞; "(α) vs (β)" is presentation-dependent | **OPEN** (R16-12 referee pending) | P50 refined + **P104** (world-line boost kernel, or non-local H) + **P105** (weak closure with 1/r² structure functions) + **P106** (defect modes subluminal; met by P61) [worker]. Alternatives P98, P99, P90 | `AX:57-61` (P50, P98, P104, P90); `AX:47` (P99); `AX:187` (P90); P105 deforms the hypersurface algebra (no axiom line) |
| W8 | **Set A, covariant** | 𝒰 no-go (R12-4); literal E1 gain excluded (R13-6 Lemma D); E2 drag (R14-2); spin-2 assembly built, CP and premise (iii) open (R15-2); **initial TT data permanently remembered (R16-4)** | **DERIVED walls; E1 and E2 both OPEN.** E1 is STATE-DEPENDENT unless the initial TT datum is supplied | E1: P65 + **P76 (initial-value record B)** + **P88 (initial TT datum)**. E2: P66 (also needs P-r14b's long history for the TT memory, worker) | E1: open gates `AX:185-186` (time origin, initial condition); `AX:94` for the datum (owner). E2: `AX:57-61`, `AX:82-83`, `AX:185-186` |
| W9 | **Λ, fixed grid** | V1 tadpoles, w ≥ 0 (R11-3) | DERIVED (unchanged) | P51 | Source/action `AX:187` |
| W10 | **Λ, site creation + P-T** | Lemma F, Lemma T, Lemma C (S17); **R15-1 FAIL: active compensation signals superluminally**; **R15-4 bounded FAIL in 𝓡⁺** (DESI); **R16-6 Theorem Z: g ≡ 0 ⇔ GR + one constant**; Theorem NA (narrow) | **DERIVED: in the R14-5 class there is no non-signalling route that is not a counterterm.** OPEN only for a mechanism that enforces the constant | P92 (law-fixed T = 0 gravitating zero) + P93 + P94 (+ P95 for IE). The referee classes this as Lemma PT's counterterm, i.e. **the same price as P51** [S20 reading]. Signalling (P74) is a refereed FAIL, not a payable price under the fixed reading | `AX:187`; `AX:94` reading; `AX:37` via site creation (P52/P53) |
| W11 | **Set C count** | TT ranks and gauge kernel (R13-8); q²F_s (R16-2); two-tuning graviton axis cone (R16-3); R16-9's 9 + CC / 13 + CC is conditional bookkeeping (`vR16-9:19`) | **OPEN.** 3 rows uncomputed; shear row rests on an unproved conflict | P72 refined by P73, P87, P100 | None (tunings) |
| W12 | **Matter on the box** (linear gravity) | R11-4 PASS WITH SCOPE; survives subluminal (R14-1) | No wall at linear order (unchanged) | P56 | Unchanged |
| W13 | **Set B** | R10-2 | DERIVED (unchanged) | Give up RP, or whole-zone SLAC | Unchanged |
| W14 | **Λ, set A q-charge** | μ fixed to 2.1e-55 (R10-4) | Minimal realization excluded; OPEN beyond (unchanged) | P54 | Unchanged |
| **W15 (new)** | **Translation Ward wall** (preferred-frame second-order identity) | **T_pf:** standard W2_pf admits no nontrivial pair-stress completion for massive free single-band matter; pair terms cannot repair it (R16-5) | **DERIVED in the single-band class; OPEN overall** (C₂-exchanged bands, 3D mixing, singular generators) | **P90 (P-pf1)**: discontinuous momentum symbol, 1/n tails, face delta, no-umklapp. Or P64's tower (`AX:47`). P91 (sharp edge decoupling) adds P90's locality cost | `AX:57-61`; `AX:187`; `AX:47` for the tower |
| **W16 (new)** | **Newtonian attraction from a sign-free finite-slot model** | **Theorem D:** E-basis stoquastic + exact scalar-shift symmetry ⇒ W(k) ≥ 0, so no pure unscreened attractive 1/k² (R16-7, Hessian/PSD form) | **DERIVED in the stoquastic conserving class**; not a sole-escape theorem | **P97**: a sign problem, scalar-law violation, or a different source bridge | None (dynamical choices); a source bridge touches `AX:187` |

**[S20 reading] The shape of the map.**
- **Changed since S17.** W1 is now DERIVED on the used edge. W3 has a shape-only price. W10 collapsed onto W9's price. Two new walls (W15, W16) are DERIVED in their classes.
- **Still OPEN because a construction is unbuilt:** W2's remaining windows, W7, W8's CP and premise (iii), W11's three rows, W15's multi-band routes.
- **Under the lattice routes, the open walls the axioms' own Qubit text bears on directly** are W2 (literal-qubit clocks, R17-1) and the source/observable bridge that W2, W10, W15 and W16 each end on (`AX:85-90,187`).

---

## 3. Price ledger delta since S17 (P74 onward; named only, none adopted)

S17 ended at P73 (`S17:227`).

### 3.1 Worker-label collisions, resolved

| Worker label | Item | Meaning | S-number |
|---|---|---|---|
| P-r15a | R15-1 | instantaneous g-influence (signalling) | **P74** |
| P-r15a | R15-2 | initial-value record B at t₀ | **P76** |
| P-r15a | R15-4 | register reader (P-r13d built) | **P80** |
| P-r15b | R15-1 | reader stability g < g_crit | **P75** |
| P-r15b | R15-2 | metric record gauge-fixed (Poisson gauge) | **P77** |
| P-r15b | R15-4 | slow-content degravitation (inverse reading) | **P81** |
| P-r15c | R15-1 | CMC foliation existence | = P68's existence hypothesis (no new number) |
| P-r15c | R15-2 | under-recorded constraint channels | **P78** |
| P-vac′ | R15-1 | vacuum bridge (d-i)/(d-ii) | **P70 refined** (no new number) |
| P-EoS | R15-6 | creation law carries the EoS | folded into **P92** (count once) |
| P-r16-7a, P-r16-11a | R16-7, R16-11 | emergent vector Gauss law, no quasi-local dressing | **P96** (R16-11 sharpens it) |
| P-r16a vs P-r166a vs P-r16-10a | R16-4, R16-6, R16-10 | three different prices with near-identical spellings | **P88**, **P92**, **P101** |

`TESTS:5004` already renamed R15-1's labels to P-r15-1a/b/c. The wrap-up should use only S-numbers.

**Theorem-name collisions (for the wrap-up's theorem list).** Cite each as "item + name".
- "Theorem B": R13-1 (supercharge), R14-3 (Ξ < 0 on 𝒰₀), R16-7 (f-sum O(k⁴)); plus R16-3 B″ and R16-11 B′.
- "Theorem L": R15-6 (linear readers), R16-10 (IR excision).
- "Lemma S": R13-6 (Stieltjes), R15-1 (signalling), R16-8 (inertness), R16-11 (support moments).
- "Lemma V": R13-4 (odd-law superluminality), R15-1 (grid vacuum), R16-3 (every-vertex form).
- "Lemma D": R13-6 (self-drag), R16-8 (the fork).
- "Lemma F": R13-3 (caustic), R16-2 (F_s numerics), R16-8 (shell); and R15-1's F′.
- "Lemma T": R13-3 (compensator), R15-5 (source preservation), R16-4 (free-TT memory).
- "Theorem D": R10-1, R16-7.
- "Lemma W": R15-5 (Schrieffer–Wolff orders), R16-12 (canonical relocation).
- "Lemma C": R14-5 (CMC forced), R16-12 (subluminality necessary).

### 3.2 Status changes to earlier prices

- **P50** (off-box tail). Refined by R16-8: singular completion confined to the spatial-diffeomorphism generator; kernel 1/r², curvature 1/r⁴; inert on box states. Harmless only if a quasi-local degree-3 closure exists, which is unbuilt and whose fork is non-exhaustive (`vR16-8:7-9`; `C5_R16-8_report.md:302`).
- **P61** (subluminal edge). On D1 the split has no structural zero (R16-1), so P61 for Dirac matter carries P73 with it.
- **P62** (shear shape tuning). Whether it is compatible with P87 on one subluminal scalar edge is OPEN. The scans give credible evidence of tension (`vR16-9:21`).
- **P63.**
  - (i) "E_g only; T₂g not reached" is superseded by P87 (`vR16-3`; `TESTS:5432`).
  - (iv) The per-polarization seagull is no longer the cheapest unpaired option within the prescription.
  - (iii) P-TTV is unchanged: the vertex is a law datum.
- **P64** (W2 protection by tower or χ-cut). The χ-cut option is refined by P91. The tower is unchanged.
- **P65** (E1). Adds P76 and P88; optionally P77. Lemma CU is a constraint only inside its ansatz (`vR15-2:7`).
- **P66** (E2). [worker, R16-4] TT initial-state memory also needs P-r14b's long history.
- **P67** (P-T readers). P-r13d is built as P80. The whole family is dropped on the g ≡ 0 route (`C5_R16-6_report.md:250`).
- **P68** (CMC lattice time).
  - As an active clock it is the R15-1 FAIL.
  - Global existence stays a hypothesis (P-r15-1c).
  - On the g ≡ 0 route it is not needed as a physical clock.
- **P69** (P-arrow). "Lattice time freezes inside black holes" is withdrawn. R15-1 Lemma F′ gives a positive floor per slice (`vR15-1:13`; `C5_R15-1_report.md:208`). The no-recollapse arrow is carried.
- **P70** (vacuum bridge). K5's "g/H² ~ 1e122" is withdrawn (`C5_R15-1_report.md:233`). Now:
  - (d-i): any-w grid vacuum absorbed if the source bridge allows energy-momentum exchange with the constraint sector;
  - (d-ii): otherwise ρ_v + p_v = 0, needing pairing or one enthalpy tuning (`vR15-1:15`).
- **P71** (graviton menu).
  - Finite auxiliary irreps are excluded (R15-3).
  - Discontinuity is necessary only within the finite PSD class (`vR15-3:9`).
  - P-N3″ is sharpened by P96 and P97.
- **P72** (set C bookkeeping). See W11. 9 + CC / 13 + CC is conditional bookkeeping with 3 rows uncomputed (`vR16-9:19`).
- **P73** (e–γ tuning). Refined to 3 per (spin, |q|) class or 7 per species, conditional (`vR16-2:13,17`). κ_γ is replaceable. [worker, R16-10] 2 with P101.

### 3.3 New prices

| # | Price (named only) | Axiom text touched | Set | What the record says it buys or costs |
|---|---|---|---|---|
| P74 | **Instantaneous g-influence** (R15-1 P-r15a). A local impulse moves the comoving density rate everywhere at once, through a Yukawa kernel of range ~½ Hubble. Present in every absorbed vacuum change; ordered by the CMC time | `AX:57` (a simultaneous slice-wide response, not one nearest-neighbour rule); `AX:185-186` (time metric) | C, C-box | **Refereed as superluminal signalling: FAIL under the fixed reading** (`vR15-1:7,19`). Named so the owner can see it; it is not a payable price under the registered reading. `C5_R15-1_report.md:253` |
| P75 | **Reader stability** (R15-1 P-r15b): keep g below the exact low-k ghost line 6H² | `AX:185-187` | C, C-box | Ghost band exact; 1–5H² tachyon lines diagnostic only (`vR15-1:11`). Impossible for linear readers exact on dust and radiation after sharp releases (R15-6 Theorem L, `vR15-6:9`). `C5_R15-1_report.md:254` |
| P76 | **Initial-value record B** (R15-2 P-r15a). A record of matter's T^{0ν} at t₀ that repairs the finite-start mean-source defect. Transient only with the zero-first-moment gain | Record `AX:77-80` unaffected; open gate `AX:185` gains an initial measurement | A (E1) | Lemma B confirmed (`vR15-2:11`). `C5_R15-2_report.md:254-256` |
| P77 | **Gauge-fixed metric record** (R15-2 P-r15b): record in the CMB frame's Poisson gauge, or only gauge-invariant content | Rides on P-r1 (Record readout `AX:82-83`) | A (E1) | Worker reading. `C5_R15-2_report.md:257` |
| P78 | **Under-recorded constraint channels** (R15-2 P-r15c): γ_{S,V} ≪ 1, raising matter decoherence and heating by up to 1/γ. Needed only if premise (iii) holds | Admissibility/Record as R6-4 (iii) | A | Premise (iii) not established, so conditional (`vR15-2:17`). `C5_R15-2_report.md:258` |
| P79 | **Tolerate decoupled ("dark") gapless partners** of the TT branches | None; observational (extra radiation) | All grid sets | Worker reading, untested. Outside R15-3's strict count only if partners are physically accepted. `C5_R15-3_report.md:226` |
| P80 | **Register reader** (R15-4 P-r15a; P-r13d built): a causal two-register linear filter on S(t) | `AX:57` (law constants); `AX:116-123`; `AX:94-95` (LTI is a model choice, `vR15-4:43`) | C, C-box | Regular, nonnegative on 𝓗₄, exact on dust and radiation; **bounded FAIL for DESI CPL in 𝓡⁺** (`vR15-4:55,60`). Dropped on the g ≡ 0 route. `C5_R15-4_report.md:331` |
| P81 | **Slow-content degravitation** (R15-4 P-r15b): observed DE = R̂[true non-phantom DE] | `AX:185-187`; `AX:57` via P68 | C, C-box | Background-level escape confirmed; g₀/H₀² = −0.289 to −1.085, so R15-1 signalling is active today (`vR15-4:52,58`). `C5_R15-4_report.md:335` |
| P82 | **Dual rotor** (R15-5 P-r15-5a): one integer slot per site on the h side | Qubit `AX:47` | All grid | EH static response with z = 2 TT modes; observationally excluded. Rotor rungs are linearized comparators (`vR15-5:27`). `C5_R15-5_report.md:258` |
| P83 | **Exact first-class constraint pair as a redundancy** (R15-5 P-r15-5b; lane R price) | Not in the axioms; `AX:57` supplies no redundancy | All grid | Removes partners as gauge. `C5_R15-5_report.md:259` |
| P84 | **Symmetric, locally conserved matter stress** (R15-5 P-r15-5c), T⁰ⁱ = Tⁱ⁰ as an exact collision invariant | Source/action `AX:187` (the boost wall) | All grid | Needed for the GR source map; T′ fails it only in its stated smooth one-band class (`vR15-5:40`). `C5_R15-5_report.md:260` |
| P85 | **Running-minimum reader MR** (R15-6 P-r156a) | `AX:57`; `AX:184-187` | C, C-box | Λ̃ = 0 and g ≤ 0 on H1 after a quiet start; no uniform influence bound (`vR15-6:7,15`). `C5_R15-6_report.md:295` |
| P86 | **Fast-transition exclusion or large \|g\|** (R15-6 P-r156b) | `AX:186` | C, C-box | Conditional (Lemmas L/U, `vR15-6:11`). `C5_R15-6_report.md:298` |
| P87 | **P-Z, zigzag edge for the graviton cone** (R16-3). Full-slope zigzag scalar edge with valleys at 0.35–0.9/a and tails \|ε₁₂₈\| ≈ 3.67e-5, **plus two shape tunings** (Ξ_Eg = Ξ_T2g = 0) per vertex prescription, each to ~1e-13 relative | None; edge dispersion is downstream (`AX:116-123`). P-TTV and vacuum touch `AX:184-187` | C-box | Refereed witness and common zero (`vR16-3:3-13,17`). Bare cone, R9-9 prescription. `C5_R16-3_report.md:280-285` |
| P88 | **Law-supplied initial TT datum** (R16-4 P-r16a): either h_TT = ḣ_TT = 0 at t₀, or nonzero data stored as initial records | Open gate `AX:185-186` gains an initial condition; `AX:92-94` (owner question) | A (E1); any theory with a beginning | Required: free TT data are remembered permanently (`vR16-4:17,19`). The worker reads zero as the unique record-compatible datum (`C5_R16-4_report.md:298`). `C5_R16-4_report.md:295-301` |
| P89 | **Product initial states for meters** (R16-4 P-r16b), or a total-energy bound if correlated starts are allowed | None (class restriction) | A | Lemma M needs a product-vacuum hypothesis (`vR16-4:9`). `C5_R16-4_report.md:302-305` |
| P90 | **P-pf1, discontinuous momentum symbol** (R16-5). Sawtooth/SLAC momentum with 1/n tails along each axis, a face delta, and vertices that never straddle the face (no-umklapp). Also an alternative payment for W7 at degree 2 | `AX:57-61`; `AX:187` | C-box | Escapes T_pf; shares W7's zone-mean root but is a different object (`vR16-8:13`). `C5_R16-5_report.md:234-238` |
| P91 | **P-pf2, sharp edge decoupling** (refines P64's χ-cut): non-local, plus non-universal coupling of edge states | `AX:57`; equivalence principle for edge states (`AX:187`) | C-box | Worker. `C5_R16-5_report.md:239` |
| P92 | **Law-fixed gravitating zero** (R16-6 P-r166a, absorbing R15-6's P-EoS): the creation law's zero is the T = 0 vacuum of the supplied dynamics | Source/action bridge `AX:187`; `AX:116-130` (EoS not supplied); `AX:94` reading | C, C-box | **Refereed as Lemma PT's late-vacuum counterterm, i.e. a tuning, unless a symmetry/constraint/mechanism enforces it** (`vR16-6:18-26,62`). `C5_R16-6_report.md:243` |
| P93 | **Late-vacuum stability** (P-r166b): our vacuum is the law's T = 0 state; SM metastability needs stabilizing physics | `AX:187`; downstream | C, C-box | Genuine conditional requirement, not established for the SM (`vR16-6:62`). `C5_R16-6_report.md:244` |
| P94 | **No later pick among causally indistinguishable branches with unequal late vacua** (P-r166c, Theorem NA) | `AX:57-62` (distribution form downstream); `AX:63-66` reading note | C, C-box | Narrow: early labels, endpoint records, equal-energy vacua or accepted residuals lie outside (`vR16-6:54`). `C5_R16-6_report.md:245` |
| P95 | **Exact first reading** (P-r166d, IE only): integration constant exact to ~1e-120 to 1e-123 for a Planck-era start | `AX:94`; `AX:185-186` | C, C-box | Refereed as an exact-boundary cancellation (`vR16-6:28,62`). `C5_R16-6_report.md:246` |
| P96 | **Emergent vector Gauss law with no quasi-local dressing** (R16-7 P-r16-7a, sharpened by R16-11 P-r16-11a): an IR fixed point where (W1) or (W2) fails, e.g. a critical or power-law dressing | None named; a dynamical hypothesis | All grid | The only finite-slot integer-law route left to an EH TT f-sum, if R16-11's transfer holds [worker]. `C5_R16-7_report.md:277`; `C5_R16-11_report.md:300` |
| P97 | **Sign problem, scalar-law violation, or another source bridge** (R16-7 P-r16-7b, widened by `vR16-7:9`) | None (dynamical); a source bridge is `AX:187` | All grid | The routes to an unscreened Newtonian scalar attraction left by Theorem D. `C5_R16-7_report.md:278` |
| P98 | **P-W7α, non-local Hamiltonian-constraint completion**: instantaneous dynamics at 1/r^{d−1} through edge quanta | `AX:57-58`; dynamics `AX:116-123` | C-box | One of several unclosed repairs (`vR16-8:9`). `C5_R16-8_report.md:303` |
| P99 | **P-W7aux, dynamical auxiliary tensor field** carrying the defect locally: new massless modes coupled to Q_D | Qubit `AX:47`; new particle content | C-box | Worker. `vR16-8:7` notes a non-dynamical constrained auxiliary also exists, with a non-local multiplier. `C5_R16-8_report.md:304` |
| P100 | **Shear by a non-shape knob** (R16-9 P-R16-9a): once the graviton cone is shape-tuned, μ_E is paid by an E_g shear counterterm, pairing (P46), the Fock vacuum, or a superluminal edge | None for a counterterm; `AX:47` for pairing; the vacuum is `AX:184-187` | C-box | Named as a sufficient price. Its **necessity is not refereed**: the CONFLICT was NOT CONFIRMED and the reading is OPEN (`vR16-9:3,21`). R16-13 may replace it by fermion/photon loops [pending]. `C5_R16-9_report.md:262-269` |
| P101 | **Lattice-superluminal photon** (R16-10 P-r16-10a): photon symbol with v_max ≈ 7.35, d(π) ≈ 6.25, stiffness fixed to ~8.5e-16, plus one photon-side condition: 2 tunings for SM Dirac content | None (dynamics); gives up the subluminal programme for gauge fields | C, C-box | **[worker; referee running]** (`TESTS:5563-5572`). `C5_R16-10_report.md:258-260` |
| P102 | **Power-law-ranged invariant hops** (R16-11 P-r16-11b), weight ≲ r⁻³ to r⁻⁵: m₁ ~ k^{p−1}, k² at p = 3 | `AX:57` if fundamental; P96 if emergent | All grid | [worker; unrefereed]. Also needs P97 for attraction. `C5_R16-11_report.md:301` |
| P103 | **Non-local or zero-vertex curvature readout** (R16-11 P-r16-11c) | Record readout bridge `AX:82`, `AX:85-90` | All grid | [worker]; escapes R16-11's Corollary B-inv. `C5_R16-11_report.md:302` |
| P104 | **P-W7K, world-line boost kernel** (R16-12): the boost generator carries X_T = 2ib_T/(q·v), the Coulomb field of the moving defect along its whole world-line, or else H is non-local (P98). Forced in 𝒞 by the center-of-energy bracket at degree 3 | `AX:57-61` (range); Poincaré structure is downstream (`AX:116-123`) | C-box | [worker; referee running]. Presentation-bound (Lemma W). `C5_R16-12_report.md:296` |
| P105 | **P-W7sf, weak translation closure** (R16-12): matter-dependent structure functions with 1/r^{d−1} kernels, or a non-local change of constraint basis | None directly; it deforms the standard hypersurface algebra the setting assumes | C-box | [worker]. `C5_R16-12_report.md:297` |
| P106 | **P-W7v, subluminal defect modes** (R16-12 Lemma C, a necessity): every defect-carrying mode has \|v\| < 1, else a Cherenkov resonance forces a non-local H | `AX:57-61`, already paid by P61 | C-box | [worker]. Met by S(1.4) and G(1.4); fails for the L-box. `C5_R16-12_report.md:298` |

**Named gap, not a price.** G-R16-9b: no Dirac, photon or gluon TT/shear vertex exists in the chain (`C5_R16-9_report.md:273`). R16-13 is running on it.

**[S20 reading] How the price structure shifted since S17.**
- **Cone prices became counts.** The box route's cone bill is now a list of tuned numbers with stated precisions (P73, P87, P100), with three rows uncomputed. No row has a refereed untuned zero.
- **Cosmology lost its only candidate.** P68's mechanism fails on causality (P74). The causal alternative (P92) is refereed as a counterterm. W10's cheapest price is now P51's in substance.
- **Set A gained an initial-condition price** (P88). The worker reads it as forced on any theory with a beginning, not specific to E1.
- **Graviton production gained no price.** It gained three more exclusions (R15-3; R16-7 B/D; R16-11 pending). The prices left (P96, P97, P102, P103) are hypotheses about phases nobody has built.

---

## 4. Owner decision memo (for Jon; supersedes S17 §4; options with prices; nothing adopted)

### 4.1 The question in one line [S20 reading]

On a slower-than-light grid, everything that has been computed can be made to agree with relativity, at a count of tuned numbers. The candidate count is about 9 plus the cosmological constant, each held to between 1e-13 and 1e-16. The referee calls that count bookkeeping, not proven minimal. Two things cannot be bought at any named price except by supplying them: the graviton, and a cosmological constant that is neither tuned nor faster than light.

### 4.2 Options (updated)

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, no LV tunings. Newtonian records-as-metric VIABLE (R6-4).
- *Pays:*
  - a supplied graviton;
  - to go covariant, E1 (P65 + P76 + **P88**) or E2 (P66);
  - Λ by a q-charge (P54).
- *New since S17:*
  - E1's spin-2 assembly exists and is OPEN, with CP and premise (iii) unproved (R15-2).
  - E1 remembers its initial waves permanently, so it needs an initial TT datum (R16-4).
  - [worker] E2 does too, over a Hubble time.
- *Open:* exact CP; second-order PPN (R16-14 running, `TESTS:5628-5653`); whether constraint-channel noise gravitates.

**Option C: keep the four texts and tune.**
- *Buys:* no text changes.
- *Pays:*
  - the R13-8 rows: candidate 9 + CC or 13 + CC on a box law (conditional bookkeeping, `vR16-9:19`), with 16 + CC as the generic bookkeeping;
  - two fixed-grid tadpoles (P51);
  - a supplied graviton.
- *Open:* the three uncomputed rows; whether the per-class counterterm convention is allowed.

**Option C-box: Z³, a box-exact law, qubits in a sector.**
- *Buys:* as S17 (relativity for number-conserving matter on a subluminal zone; universal fall; bound-body tests).
- *Pays:* S17's list, plus:
  - P73 as 3/7 (or 2 via P101);
  - P87 for the graviton axis cone;
  - for the shear, P62 if it can share the edge with P87 (OPEN, evidence against), otherwise P100 (R16-13 pending).
- *Open:*
  - GW170817 has no gauge-invariant formulation (W15, R16-5);
  - W7 (R16-8 OPEN; R16-12 worker: the obstruction is in the boost bracket);
  - off-axis TT rows.

**Option C-box-S: C-box with boson–fermion pairing per cell.**
- *Buys:* the photon's one-loop shift, matched vacuum energy, the stipulated TT response. It is also one of the named non-shape knobs for the shear (P100).
- *Pays:* P46 plus one of P58–P60, and **still P73** (3 or 7).
- *Open:* as S17; and whether R16-13's fermion loops do pairing's job without pairing.

**Cosmology overlay (any grid option).**
- *Active CMC compensation:* refereed FAIL on causality (R15-1).
- *g ≡ 0:* GR plus one constant fixed by the law's T = 0 normalization. The referee classes this as a counterterm (R16-6).
- So the overlay currently offers nothing beyond P51 or P54. **This replaces S17's Q2 (CMC lattice time), which R15-1 made moot.**

### 4.3 Questions only Jon can answer

**Q1 (new). Λ: faster-than-light compensation, or a law-fixed zero?** Three choices, each with its refereed status:
- **(a) Accept active compensation.**
  - Whenever the universe sheds vacuum energy, a local push changes the density everywhere at once, ordered by a global time (P74).
  - The referee counts this as superluminal signalling, so the registered reading is FAIL (`vR15-1:7`).
  - The DESI escape keeps it active today (g₀/H₀² ≈ −0.3 to −1.1, `vR15-4:52`).
  - Accepting it means overriding a registered reading.
- **(b) Write into the creation law that only energy above the law's ground state gravitates (P92).**
  - It also needs late-vacuum stability (P93) and no branching among unequal late vacua (P94).
  - The integrating version also needs an exact first reading, to ~1e-120 (P95).
  - The referee's ruling: as supplied, this is the same as tuning a counterterm to cancel the late vacuum (`vR16-6:18-26`).
  - It stops being a tuning only if some symmetry, constraint or mechanism forces it. **Your question:** do you regard "the vacuum of the law does not weigh" as a principle you would state, or as a tuning? R17-3 tests whether anything in the four texts can force it.
- **(c) Neither.** Λ stays a tuned number (P51) or a q-charge datum (P54).

**Q2 (new). The initial gravitational-wave datum (P88).** A universe with a beginning must say what free gravitational waves it starts with. They never fade, and one quantum per mode at the 5 µm to 0.4 nm scale would outweigh dark energy by 1e3 to 1e19 (R16-4). Two choices:
- **Zero.** "No metric content that is not a record at the first instant." The worker reads this as the only datum compatible with "only records are readable" (`AX:82-83`).
- **Nonzero.** Nonzero waves written as initial records.

**Your question:** is "the state at the first instant has no non-record content" a *privileged state* under "A law privileges no states" (`AX:94`)? The referee says `AX:94` does not settle it (`vR16-4:17`). This now bears on any option with a start, not only E1, since it is generic GR behaviour (`vR16-4:13`).

**Q3 (new). The cone bill.** For SM content on one subluminal box law, the candidate count (R16-9's bookkeeping; the referee confirms the arithmetic, not the minimality, `vR16-9:19`) is:

| Item | Tunings |
|---|---|
| Charged-matter cones (per (spin, \|q\|) class) | 3 |
| Graviton axis cone (two edge shapes) | 2 |
| Shear (non-shape knob, or a shape if a joint zero exists) | 1 |
| Off-axis TT speeds (not computed) | 2 |
| LV tadpole (not computed) | 1 |
| Cosmological constant | 1 |
| **Total** | **9 + CC** (13 + CC with one counterterm per species) |

- **Precision:** each tuning is held to ~1e-13 (graviton) to ~1e-16 (charge).
- **[worker]** A photon that is faster than light at the grid scale cuts the charge part to 2.
- **Still to come:** R16-13 (fermion/photon loops in the gravity rows) and R17-4 (the uncomputed rows) can move this table.
- **Your three questions:**
  1. Is a bill of about nine numbers at this precision an acceptable price for keeping all four axiom texts?
  2. Is "same-charge particles share one counterterm" (3, not 7) a structural choice you would make?
  3. Is lattice-scale superluminality for the photon alone (P101) excluded, as S17's rule assumed?

**Q4 (carried, updated). E1 or E2.**
- Both remain OPEN (R15-2; R14-2).
- E1 now also pays P76 and P88.
- [worker] The start-state question does not separate them over a Hubble time.
- R16-14 (running) may break the tie on PPN α₁/α₂.

**Q5 (carried, updated). Edge-shape tuning.**
- Edge shapes now reach both graviton polarizations (P87).
- Whether the shear can share that edge is OPEN; the scans give evidence against (`vR16-9:21`).
- The question is the same as S17's: does choosing an edge shape to cancel an effect count as an acceptable tuning?

**Q6 (carried, updated). Pairing per cell (`AX:47`).**
- Pairing is one of the named knobs for the shear (P100) and buys the TT response.
- It still does not remove P73.
- R16-13 tests whether ordinary fermion loops do the shear's job without pairing.

**Q7 (carried from S14/S17).** Site creation (`AX:37`); a law that reads only changes in stress (`AX:94`); range (box tails, the BF 1/r term, W7's 1/r², P90's 1/n tails); sector selection (P45).

### 4.4 Open in every option

- **Producing the graviton.** Five bounded exclusions are on record. The open windows are:
  - law-violating phases with no quasi-local dressing (P96);
  - literal-qubit Z₂ clocks;
  - readout bridges (P103).
- **Λ without tuning and without signalling.**
- **GW170817 as a gauge-invariant test on any grid** (W15).
- **Nonlinear gravity and the off-box tail** (W7).
- **The full tuning count** (three rows uncomputed; shear row OPEN after R16-9; R16-13 pending).
- **N ≥ 3 tails** (R11-6) and **the body quadrupole** (P56).

---

## 5. Dated corrections (this period; dated 2026-10-12)

| Correction | What it was | What it is now | Source |
|---|---|---|---|
| **S17 "T₂g never zeroed"** | "No edge choice has reached T₂g"; P63(i) "T₂g not reached" (`S17:95,179,217,263,288`) | Z1 gives Ξ_T2g > 0 (M and U); two shape tunings zero E_g and T₂g together; strict negativity only on the B″ gentle-valley subclass. Prescription-scoped | `TESTS:5432`; `vR16-3:3,13-15` |
| **R14-5 "lattice time freezes in black holes"** (and S17's P69) | N → 0 inside black holes (`C5_R14-5_report.md:51,222,227,303`; `S17:223`) | Positive lapse floor on each regular slice, N ≳ 1.51875(mH₀)² (Lemma F′). Not a collapse-continuation theorem; global CMC existence open | `vR15-1:13`; `C5_R15-1_report.md:208` |
| **K5** (R14-5; S17's P70 and §1.6) | Under the grid zero-point, g/H² ~ 1e122, so the CMC model fails (`C5_R14-5_report.md:317-320,338`; `S17:138,224`) | The 1e122 is the E-sector's own unobservable share. Any-w grid vacuum is absorbed if the source bridge allows momentum exchange (d-i); otherwise ρ_v + p_v = 0 (d-ii) | `vR15-1:15`; `C5_R15-1_report.md:233` |
| **κ_γ "required"** (R16-2 worker, `TESTS:5218`) | The photon counterterm is a required tuning | Replaceable: tune the three matter classes instead, or use a literal-family shape near b₂ = 2.31 (8G = F). Still 3 | `TESTS:5426`; `vR16-2:13` |
| **Lemma CU** (R15-2) | One common gain for every channel is required | Holds only in the channel-diagonal common-profile ansatz. Momentum-dependent differences can cancel the inverse Laplacian; Gaussian smearing is non-compact | `vR15-2:7` |
| R15-2 constants | c₁ = 0.657; ratio 0.2524; exact budget endpoints | Invalid: dropped derivative, K′ = f(t)J₀(0) + f*J₀′. The ¼ stands | `vR15-2:13` |
| R15-1 tachyon thresholds | 1–5H² as stability bounds | Frozen-background diagnostics. The g > 6H² ghost band (low k) is exact | `vR15-1:11` |
| R15-3 bounds | "≥ 5 with an h coupling"; minimizer list; Lemma N | ≥ 5 needs a rank-2 axial TT residue; list omits 4A₁ + 4A₂; Lemma N conditional | `vR15-3:5-11` |
| R15-4 numbers | κ(−dρ_tot/du) = 2S; DESI H(z) errors 24–43%; R* +0.16 at 0.07 MeV | −d𝓔/du = 2S; 29.9–42.7% (D1), 21.8–26.0% (R*) with Table 5 Ω_m; R* max +0.156, +0.130 at 0.070 MeV | `vR15-4:5-10,23,45` |
| R15-5 Lemma W; dispersion | "O(k³) at every finite order"; ω = \|k\| | Only for orders with N > 36nM (not fixed N, not N = 2); ω² = Jg\|q̂\|². X2 identification not literal | `vR15-5:5-15,33` |
| R15-6 PASS on H1 | PASS (class H1) | INCONCLUSIVE: no uniform influence bound. 0.05H₀² is a heuristic, not a bound; transition formula needs the comoving gain (~2×) | `vR15-6:13-15` |
| R16-1 class and constants | Denominators ≥ λ; b₀ = 0.505 threshold; 𝒬_W | ≥ λ/2; sharp b* = 0.504032…; (H0) defines 𝒬_W⁺. P-b SUGGESTED. Zero at m ≈ 24 not shown unique | `vR16-1:5-13` |
| R16-2 Lemma F | F_½(0⁺) ∈ [−16.1, −4.5], F_0 ∈ [−3.6, −1.6] as class values; "no IR log" | Finite-m/λ/N samples, not controlled limits; class theorem not confirmed; "no IR log" is non-observation. [worker, R16-10] the class as registered contains a Dirac zero (superluminal photon) | `vR16-2:11`; `TESTS:5563-5569` |
| R16-3 P-Z tails | ~1e-7 to 1e-6 at r ~ 128–512 | \|ε₁₂₈\| = 3.67e-5 for the checked zero law. Lemma V strict form needs nondegeneracy; B″'s "ending at" means every incident stretch | `vR16-3:9-11,17` |
| R16-4 constants | Pulse-energy coefficient; Lemma M network scope | Coefficient 2× too large; examples omit the gain factor; Lemma M needs a product-vacuum hypothesis | `vR16-4:7-9` |
| R16-5 extensions | Finite-band no-go; "light would not redshift" exclusion | Finite-band closure overclaimed (six-band signed-axis construction); redshift exclusion conditional on a source/observable bridge | `vR16-5:13,19` |
| R16-6 claims | "The FAIL text is false"; IE run through inflation; Theorem NA "excludes landscape-type laws" | "False given the late-vacuum counterterm premise"; the inflation run used an exact state read, not IE; NA excludes only causally indistinguishable branches ending in unequal vacua | `vR16-6:16,48,54` |
| R16-7 | Per-volume m₁; screening range √(a/c); NOT-PRODUCED-EVIDENCE; "only window" | Missing V factor (V^{−1/2} normalization); m⁻¹ ≤ √(c/a); not permitted (control failed); too exclusive | `vR16-7:5,9,13,15` |
| R16-8 | Lemma A broadly; exhaustive (α)/(β) fork; Bianchi-fixed curvature physical; SLAC band discontinuous | Lemma A only in its narrow class; fork not exhaustive; curvature transforms under the completed constraint; the SLAC positive band is continuous (momentum symbol discontinuous) | `vR16-8:5-13` |
| **R16-9 CONFLICT and its bill** (worker, `TESTS:5550-5562`) | CONFLICT class-wide; "block split (proved)"; μ_E "≥ +1.25e-3 / +1.3e-4" as bounds; 9 + CC / 13 + CC as the bill | OPEN: the scans are not enclosed supersets and local optima are upper bounds. The split is shown only for the truncated scalar-loop prescription. The totals are conditional bookkeeping; μ_T2 = 0 is coupling-specific | `vR16-9:3-9,15,19,21` |
| S17's W1 subclass reading | "The DERIVED subclass is the R9-1-excluded literal edge" (`S17:63,192`) | Status change, not an error: DERIVED now covers 𝒬_W⁺ including D1 | `vR16-1:19` |
| SUMMARY §26 labels | R15-4 and R15-6 listed as worker results (`SUMMARY:711-714`) | Both refereed: R15-4 bounded FAIL in 𝓡⁺, R15-6 INCONCLUSIVE | `TESTS:5301-5324` |
| S17 owner Q2 and §4.2 cosmology overlay | CMC lattice time as a priced option (`S17:272,281-287`) | Active compensation is a refereed FAIL (signalling); the g ≡ 0 alternative is a counterterm | `vR15-1:19`; `vR16-6:64` |

Carried, still in force: S17 §1.8's table (R11-5 literal kernel, ¼ prefactor withdrawn, Lemma V re-scoped, box superluminality, R9-2 t*, R11-1(b), R12-5 cap, R13-5 2κ, R12-6 a_e, R13-1 bound, R13-7 photon symbol).

---

## 6. Calibration of S17's round-16 expectations [S20 reading]

| Item | S17 expectation (`S17:346,368,389,411,434`) | Refereed outcome | Calibration |
|---|---|---|---|
| R16-1 | SUGGESTED; DERIVED subclass possible if r ≤ 1/√d fixes the sign | DERIVED in 𝒬_W⁺ (L > 0 under (H3)/(H3′)) | **More decisive than expected.** The "possible" branch happened, through a convexity lemma rather than r alone |
| R16-2 | COUNTED, n_t 2 or 3; λ → 0 IR logs the likeliest reason for OPEN | OPEN (conditional 7/3). The reason was Lemma F's unbounded remainder, not IR. [worker, R16-10] no log, and n_t = 2 only with a superluminal photon | **Wrong reading, wrong reason.** "2 or 3" survives only conditionally (3 per class) or with P101 (2) |
| R16-3 | SUGGESTED leaning DERIVED; simultaneous zero not expected | REFUTED (Z1) plus a simultaneous zero; DERIVED only on B″ | **Wrong on both counts.** The premise that valleys "do not reach mixed derivatives" held only for slope-limited valleys (`C5_R16-3_report.md:267`) |
| R16-4 | WASHED-OUT; only an unobservable log dependence | STATE-DEPENDENT for 𝒢(1, 1/ℓ) | **Wrong.** S17's own registration listed the near-cone budget, and undamped free TT data fail it. S17 did not apply "E1 leaves G_R undamped" (`vR16-4:13`) |
| R16-5 | A W2_pf-complete stress exists; SPLIT-PRESENT without pairing; failure most likely a strongly coupled scalar | OPEN: no W2_pf-complete stress in the single-band class (T_pf) | **Wrong on existence.** The wall moved from boosts to translations; the scalar question was never reached |

**Score.** One of five right in direction (R16-1, and that one more decisive than expected); four wrong. S14's round-13 score was about one in three right (`S17:161-167`).

**Pattern.** S17 twice expected that changing the setting would change the outcome:
- R16-5: a preferred frame would remove the boost wall. It moved to translations.
- R16-4: one more channel would wash out the start. GR's free data do not wash out.

S17 also twice expected obstructions to persist where a new degree of freedom broke them: R16-3's zigzag valleys, and R16-10's stiffened photon (worker). **Lesson for the drafts below:** state for each expectation which hypothesis of the previous no-go the new setting removes, and which it keeps.

**Supervisor-registered round-16 items (not S17's; for the wrap-up's record).**

| Item | Expected | Outcome |
|---|---|---|
| R16-6 | FAIL at inflation's end unless reheating counts as equilibrium (`TESTS:5245`) | INCONCLUSIVE (tuning); equilibrium was not the deciding issue |
| R16-7 | INCONCLUSIVE from system size (`TESTS:5285`) | INCONCLUSIVE because the control failed, not because of size |
| R16-8 | OPEN or PHYSICALLY NON-LOCAL, same price as P-pf1 (`TESTS:5358`) | OPEN; same root, different object |
| R16-9 | JOINT without P62, count 5–6; CONFLICT or OPEN with P62 | Refereed OPEN; worker CONFLICT not confirmed. Listed-condition count 6 as conditional bookkeeping (`vR16-9:19`) |
| R16-10 | COUNTED for scalars, OPEN for Dirac | [worker] the reverse, in effect: Dirac REFUTED-ZERO (superluminal photon), scalar OPEN; pending |
| R16-11 | TRANSFERS | [worker] TRANSFERS; pending |
| R16-12 | NON-LOCAL in the class, effect suppressed by the edge-quanta population (`TESTS:5549`) | [worker] OPEN: (β) works for translations and fails in the boost bracket in 𝒞. The population suppression agrees; pending |
| R16-13, R16-14 | — | No result |

---

## 7. Draft round-17 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–16).**
- Probes run on Opus 5.5 at xhigh. Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses come before titles, and excluded outside realizations are listed. Numbers from memory are labelled RECALLED.
- Every tail or decay clause names its subtraction before any run. A PRODUCED or PASS clause names the perturbative order of each exactness condition.
- **Round-16 head rules (`TESTS:5039`):**
  - every law states its whole-zone v_max;
  - every frame-tied kernel states its self-force on a moving compact body;
  - every Ward requirement says standard or deformed.
- **New rules (from round-16 verdicts):**
  - **Gauge fields too.** The v_max rule applies to photon, gluon and graviton symbols, not only matter (R16-10's v_max 7.35 photon).
  - **Counting conventions.** Every tuning count states its counterterm basis: per species, per (spin, |q|) class, or q²-correlated (`vR16-2:13`).
  - **Enforced or stipulated.** Every Λ mechanism states whether any number it needs is enforced (by a symmetry, constraint or theorem) or stipulated, and checks radiative stability (`vR16-6:26`).
  - **Physical controls.** A "control" must measure the same physical observable in a model known to have the target phase. An operator identity is not a control (`vR16-7:13`).
  - **Readout bridges.** Every finite-slot susceptibility or stiffness claim names its readout (observable) bridge (`vR16-7:5`; `AX:85-90`).
  - **Forks.** Every dichotomy offered as exhaustive lists the alternatives it excludes and why (`vR16-8:9`).
  - **Generic GR comparison.** Every initial-state or memory claim says whether the effect is generic GR behaviour or specific to the model (`vR16-4:13`).
  - **Changed hypotheses.** Every expectation names which hypothesis of the governing prior no-go the new setting removes (§6).

**Overlap check.**
- R16-13 covers fermion/photon TT and shear vertices; no R17 item repeats it.
- R16-14 covers set A's noise-fed PPN; no R17 item is on set A.
- R16-11 covers quasi-local dressing; R17-1 covers only small-N clocks and readouts, which R16-11 leaves open (`C5_R16-11_report.md:288,290`).
- R16-12 covers the (α)/(β) fork in class 𝒞. R17-2 covers the boost-sector escapes it leaves undecided (`C5_R16-12_report.md:263-276`) and the constraint-invariant observables.
- R16-10 covers Lemma F; R17-4 covers only the three uncomputed bill rows and R16-9's missing enclosure.

**Priority.**
1. R17-1 (graviton, axiom-level) and R17-3 (Λ), in parallel.
2. R17-4 (bill rows, owner Q3). Its probe (f) only if R16-13 does not return LIFTED.
3. R17-2 (W7), preferably after R16-12's referee.
4. R17-5 (W15) only if time allows.

---

**R17-1. Literal qubits: does the k⁴ obstruction survive on Z₂ and Z₃ clocks, where integer lifting fails?**

- **Plain question.** R16-7 (refereed) proves that finite slots with an exact *integer* vector Gauss law cannot give Einstein–Hilbert TT stiffness through the electric f-sum. R16-11 (worker) extends this to every phase reachable by a quasi-local dressing. Both leave out mod-N clocks at small N. There "divergence-free" holds only mod N, so the moment lemma's integer lift fails. The axioms' one-site algebra is M₂(C), so a qubit metric slot in the Weyl presentation is a Z₂ clock. Is the qubit case inside the obstruction, or is it the window?
- **Setting.**
  - Z_N clock tensor model on Z³ (N0914's slot positions and stencil), N ∈ {2, 3, 4}.
  - Exact mod-N vector Gauss law, plus any local Hamiltonian, bounded below and quasi-local.
  - Probes: TT-component clock operators (state the operator used for E_TT at N = 2, e.g. the Hermitian part of the clock Z^{ε}) and gauge-invariant curvature probes (R16-11's B-inv form).
  - A stated readout bridge for "metric susceptibility".
  - Excluded: rotors; integer-law QLMs (R16-7, R16-11 cover them); non-local hops.
- **Prior art (count once).** R16-7 and its verdict (`vR16-7:5-7`; `C5_R16-7_report.md:224-230`, its suggested §8 on mod-N); R16-11 Lemma S (`C5_R16-11_report.md:94-135,288`); N0914's moment lemma and lifting bound (`N0914:109-129,218-250`); R15-5 Lemma W's N > 36nM (`vR15-5:33`); X-cube/Z_N rank-2 fracton literature (comparator, RECALLED: gapped at large penalty).
- **Hypothesis that changes from the prior no-go.** Integer lifting (removed). Kept: finite slots, exact law, quasi-locality.
- **Probes.**
  - (a) Enumerate the minimal gauge-invariant hops at N = 2, 3, 4 up to a stated support size. For each, compute its zeroth and first moments as integers of a minimal lift. Identify every invariant hop with no lift of vanishing moments.
  - (b) Compute m₁(k) for the TT probe with those hops present. Is it still ≤ Ck⁴, or does a k² or k⁰ term appear? Give exact symbols.
  - (c) If the bound fails, state what the failure buys. A k⁰ f-sum gives no exclusion and no production; say which. Check one explicit qubit model's static TT response by exact diagonalization on the largest feasible cluster, labelled with its size limit.
  - (d) The readout bridge: which record-readable quantity is "the metric" at N = 2 (`AX:82-83`)?
  - (e) Physical control: the 3D Z₂ vector gauge theory (toric code). The method must not report a gapless photon there (comparator, RECALLED: gapped deconfined phase).
  - (f) Prices.
- **FIXED readings.**
  - **EXTENDS:** a refereed proof that m₁(E_TT) ≤ Ck⁴ (or the B-inv curvature bound) holds at N = 2 (and stated N) in the stated class, with the readout bridge named.
  - **WINDOW:** an explicit qubit (N = 2) model in the class with an invariant hop giving m₁ ≥ ck² (or k⁰) for the TT probe, checked. This is a window, not a production claim.
  - **OPEN:** otherwise.
- **Expectation.** WINDOW at the f-sum level. At N = 2 every shift is its own inverse, so invariant patterns need not lift to moment-free integer patterns. But no gapless TT phase follows from that, and every known Z₂ tensor phase is gapped (comparator). If so, the obstruction moves from "the f-sum" to "whether any gapless Z₂ tensor phase exists", which no method here decides.

---

**R17-2. W7 in the boost bracket: does any escape outside class 𝒞 close degree 3, and is anything physical left?** *(Preferably launched after R16-12's referee. The readings are fixed now.)*

- **Plain question.** R16-8 (refereed OPEN) gives the off-box tail as a 1/r² kernel with a 1/r⁴ curvature, inert on box states but not shown physical or harmless. R16-12 (worker OPEN) finds three things:
  - the translation part is repaired by (β), with weak closure only;
  - the boost bracket {H[x_b], H[1]} = D[e_b] forces a world-line Coulomb kernel X_T ∝ 1/(q·v), unbounded on q ⊥ v. So in class 𝒞 (homogeneous kernels bounded on the sphere) there is no quasi-local completion;
  - by Lemma W, whether this reads as "(α) non-local" or "(β) quasi-local" depends on the canonical variables. Only constraint-invariant observables can decide.

  Two questions remain: does an escape outside 𝒞 close the boost bracket with quasi-local dynamics, and does any constraint-invariant observable respond at a distance?
- **Setting.**
  - R12-1's completion with R16-8's Lemma-P placement and R16-12's Theorem T3 translation repair.
  - The R14-1 S(1.4) or G(1.4) box (whole-zone v_max 0.99270 or 0.99386; R16-12's Lemma C needs |v| < 1).
  - d = 3; linear in matter bilinears; through κ³, plus degree-4 shell terms where an escape needs them.
  - Standard hypersurface algebra, unless the deformation is the escape under test, in which case it is stated (standard or deformed, per rule).
  - Excluded: pairing; P90 matter; nonlinear gravity beyond the stated degree.
- **Prior art (count once).**
  - R16-8 and its verdict (`vR16-8:5-17`);
  - R16-12 and its referee when back (`C5_R16-12_report.md:230-313`; Theorem B3, Lemma W, escapes 1–7 at `:263-276`);
  - R12-1 and its verdict; R13-4's criterion (`vR13-4:18`);
  - R16-5's grading lemma (`vR16-5:19`), which already excludes pair channels;
  - SUMMARY §17's boost wall;
  - RFW F2's first-jet obstruction;
  - the hypersurface-deformation literature with field-dependent structure functions (comparator, RECALLED).
- **Hypothesis that changes from the prior no-go.** Theorem B3 assumes homogeneous kernels bounded on the sphere and a fixed presentation. This item allows world-line (non-homogeneous) boost kernels, degree-4 shell terms, constrained auxiliaries (`vR16-8:7`) and canonical relocations.
- **Probes.**
  - (a) Escapes 2, 3 and 5 of `C5_R16-12_report.md:269-274`. For each, close {P_c, K_b} = δ_bc H and {K_a, K_b} = J at degree 3, or prove inconsistency in a stated class.
  - (b) For any closed system, build at least one bounded observable invariant under the completed constraints, at distance r from a defect-carrying quantum. Test R13-4's criterion: an instantaneous response, and its r-dependence.
  - (c) If a response exists, state its size at a = ℓ_P per edge quantum and for thermal populations at T_CMB and 1e16 GeV, with the subtraction named. R16-12's ≥ 1.41/a quantum energy is the input.
  - (d) Settle Lemma W's question: is the non-locality removable by a canonical map on the physical (invariant) domain, or only relocated?
  - (e) Prices.
- **FIXED readings.**
  - **LOCAL-EQUIVALENT:** a closed degree-3 completion with an invariant physical domain on which no bounded invariant observable responds outside the light cone, checked through the stated degree.
  - **PHYSICALLY NON-LOCAL:** a refereed demonstration of a bounded constraint-invariant observable responding instantaneously through the tail, in a class containing escapes 2, 3 and 5, with its size.
  - **OPEN:** otherwise.
- **Expectation.** PHYSICALLY NON-LOCAL in principle and unobservable in practice, or OPEN. Theorem B3's kernel is the Coulomb field along the defect's world-line, which is the hallmark of a constraint carrying non-local charge (as in Coulomb-gauge QED). Its invariant content is likely real but tied to Planckian edge quanta, whose thermal occupation is 10^(−3.3e31) at T_CMB. The likeliest failure is that no invariant observable can be built at this degree, which would give OPEN.

---

**R17-3. Λ after R16-6: can anything in the four axioms force the gravitating zero, or is it necessarily a tuning?**

- **Plain question.** R16-6 (refereed INCONCLUSIVE) shows that the only non-signalling route is GR with one constant: the law's late (T = 0) vacuum. Choosing that constant is Lemma PT's counterterm unless something forces it. Theorem NA suggests why a causal law cannot do better [S20 reading]: it cannot know the final vacuum before reaching it, so that energy must be a law constant. Three candidates might force it:
  - (i) **Record sourcing.** "Only records are readable; a site with no record cannot be read" (`AX:82-83`). Read as a source bridge, gravity sees only recorded content, so the unrecorded ground state never weighs.
  - (ii) **A global constraint** that fixes the constant from the whole history's average (sequestering-type; RECALLED).
  - (iii) **The vacuum-shift symmetry** ρ_v → ρ_v + C, λ → λ − κC of R14-5 (`vR14-5:29-35`), extended to the creation law.

  Does any of these force C = ρ_v,late without a tuned number, keep inflation, and stay causal?
- **Setting.**
  - R16-6's homogeneous equations (Theorem Z, `vR16-6:5-14`), plus the R15-1 linear k ≠ 0 sector for causality.
  - Histories: SM crossovers, supercooling control, m²φ² inflation + reheating (65 e-folds), DESI-like CPL, as in R16-6.
  - Radiative stability: one-loop SM shifts of ρ_v,late (RECALLED sizes).
  - The source bridge for (i) is stated as a hypothesis on `AX:187`, not as axiom content. The owner's "records are mass" picture is a thought, not a rule (`owner-readings-are-thoughts`); it is tested here as a hypothesis.
  - Excluded: active compensation (R15-1 covers it); readers in 𝓡⁺ (R15-4 covers them).
- **Prior art (count once).** R16-6 and its verdict; R5-3 Lemma PT (`TESTS:2985-2988`); R14-5 vacuum-shift symmetry (`vR14-5:29-35`); R15-1 Lemma V and the (d-i)/(d-ii) bridge (`vR15-1:15`); R10-4 q-charge (`TESTS` R10-4 entry); R11-3 (grid zero-point w ≥ 0); the stadium/records-are-mass thread (owner thought; memory); sequestering (comparator, RECALLED).
- **Hypothesis that changes from the prior no-go.** R16-6 stipulated C. Here C must follow from a stated law structure.
- **Probes.**
  - (a) Under (i), what gravitates during inflation? Is a homogeneous false vacuum "recorded"? If it is, why is the late vacuum not? If it is not, does inflation fail (R16-6 §4.2)?
  - (b) Under (ii), state the global constraint, check that it fixes C = ρ_v,late, and test causality: does a late vacuum change alter early-time gravity?
  - (c) Under (iii), find whether the symmetry plus any creation-law structure selects C, or leaves it a free datum (`vR14-5:35`).
  - (d) Radiative stability of whichever mechanism survives (a)–(c).
  - (e) Prices.
- **FIXED readings.**
  - **ENFORCED:** a stated law structure, in class (i), (ii) or (iii), that forces C = ρ_v,late with no independent number, keeps 60+ e-folds of inflation, has no R15-1-type signalling, and is radiatively stable, checked.
  - **TUNING:** a refereed proof that in a stated class containing (i)–(iii), every law with g ≡ 0 and Λ̃_late = 0 needs an independent exact number, or an acausal (final-state) input.
  - **OPEN:** otherwise.
- **Expectation.** TUNING for (i) and (iii). Under (i), inflation needs the false vacuum to gravitate; any rule that lets it, but not the true vacuum, must single out the true vacuum's energy, which is the counterterm again. (ii) can force C only with a whole-history (final-state) input, which is the acausal price. The likeliest outcome is a refereed "tuning or acausal" theorem. This would turn owner Q1(b) into a plain choice between a tuning and a final-state law.

---

**R17-4. The cone bill's three uncomputed rows (off-axis graviton speeds, LV tadpole), and a certified answer for the shear row.**

- **Plain question.** R16-9's bill is 9 + CC (per class) or 13 + CC (per species). The referee confirmed the arithmetic but called it conditional bookkeeping (`vR16-9:19`). Three of its rows were never computed:
  - the two off-axis TT speed anisotropies (R16-3 zeroed only the axis speeds);
  - the LV tadpole.

  Do the zigzag laws that zero E_g and T₂g on the axis also zero the off-axis speeds? Or does each cost a further edge shape, with longer tails? Is the tadpole a separate tuning?
- **Setting.**
  - R13-8's P,T-even degree-2 TT basis (graviton speed + 3 anisotropies; `vR13-8:15-18`).
  - R9-9's M and U vertices extended to q along a face diagonal and a body diagonal. State the extension and the assumed standard W1.
  - Scalar edges in 𝒮: R16-3's checked zero law and R16-9's M-best/U-best laws, with v_max and raw tails stated. Masses m = 0.1 and 0.01. Supplied zero-point vacuum.
  - Excluded: Dirac/photon/gluon vertices (R16-13); pairing; deformed W2 (R16-5).
- **Prior art (count once).** R16-3 and its verdict (Z1, IBP identity Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩, `C5_R16-3_report.md`); R16-9 and its verdict (`C5_R16-9_report.md:216-235`; Lemma R and R_U and the fast-state identity confirmed in continuous form, `vR16-9:5-11`); R13-8 (`vR13-8:11-22`); R9-9 Theorem T; R14-3 analyticity in m² (`vR14-3:18`).
- **Hypothesis that changes from the prior no-go.** R16-3 restricted q to an axis. Here q is off-axis.
- **Probes.**
  - (a) The off-axis generalization of the IBP identity, giving the four degree-2 TT speed parameters in closed form.
  - (b) Evaluate them on the axis-zero laws. Count how many further shape conditions are needed, and find one law with all four zero at a common light mass, or show that two conditions conflict in the family. A conflict needs a certified enclosure, since R16-9's scans did not meet that clause (`vR16-9:9`).
  - (c) The LV tadpole row on the same laws: is it a separate condition, or fixed by the others?
  - (d) The resulting v_max and raw tails.
  - (e) The total in R13-8's rows.
  - (f) *Only if R16-13 does not return LIFTED.* A certified answer to R16-9's shear row. Run an outward-rounded, interval-enclosed version of Lemma R_U's continuous relaxation, covering continuous b, lo, hi, s_min and m ∈ [0.01, 0.1], first for the U vertex, whose margin is thinner. It should either prove μ_E > 0 at every graviton-cone zero in 𝒮, or return a certified feasible point with μ_E ≤ 0 (`vR16-9:5-9`).
- **FIXED readings.**
  - **COUNTED-ROWS:** an explicit law with every TT speed parameter and the tadpole zero at a common light mass, checked, with the number of shape conditions. Or a proof that some rows vanish identically given the axis zeros.
  - **For (f) separately: CERTIFIED-CONFLICT** (an enclosure proof, refereed) **or JOINT** (a certified law with Ξ_Eg = Ξ_T2g = μ_E = 0).
  - **CONFLICT:** a demonstration, refereed if class-wide, that the off-axis rows cannot be zeroed together with the axis rows in 𝒮.
  - **OPEN:** otherwise.
- **Expectation.**
  - COUNTED-ROWS with two further shape conditions. That would confirm 9 + CC per class as a count, with tails growing beyond R16-3's 3.67e-5 at r = 128.
  - The main alternative is a CONFLICT inside separable 𝒮, since off-axis zeros need more zigzag structure than a single-axis separable law may have. That would push the off-axis rows to non-separable laws.
  - For (f): CERTIFIED-CONFLICT for M. The U vertex is likelier to yield a JOINT point if one exists, because its margin is ~10× thinner.

---

**R17-5. GW170817 on the grid, second attempt: a multi-band W2_pf completion.** *(Launch only if time allows.)*

- **Plain question.** R16-5 (refereed OPEN) proves that single-band matter admits no nontrivial pair stress under the preferred-frame second-order identity. The referee exhibited a six-band signed-axis construction (Π_j = diag(v_j), v ∈ {±e_x, ±e_y, ±e_z}) that satisfies the zeroth moment with θ = 0 (`vR16-5:13`). Can it, or a C₂-exchanged band family, be completed into full W2_pf matter whose momentum generator carries physical (redshifting) momentum? If so, what is the gauge-invariant graviton–matter pole split?
- **Setting.**
  - Six-band and C₂-exchanged band families with proper cubic covariance; continuous quasi-local kernels; finite pair channels; projectable lapse.
  - R9-9's N-type graviton.
  - The redshift test needs a stated source/observable bridge (`vR16-5:19`).
  - Excluded: single-band (covered), discontinuous symbols (P90), tower matter (P64).
- **Prior art (count once).** R16-5 and its verdict (`vR16-5:5-25`); R13-5 (`vR13-5:7,13`); R16-8's relation of P-pf1 to W7 (`vR16-8:13`); RN L3 (projectable Hořava); RFW F1.
- **Hypothesis that changes from the prior no-go.** Single-band (removed). Kept: continuity, quasi-locality, multiplier-generated shifts.
- **Probes.**
  - (a) Complete the six-band construction to a W2_pf-complete stress, or prove none exists in a stated multi-band class.
  - (b) Does its P_j generate physical translations? Test whether a homogeneous strain shifts its one-particle energies (the redshift bridge, stated).
  - (c) If (a) and (b) succeed, compute c_m − c_T for both polarizations, gauge-invariant, at a = ℓ_P.
  - (d) Prices.
- **FIXED readings.**
  - **SPLIT-PRESENT / SPLIT-ABSENT:** as R16-5 (`TESTS:5145-5148`), with a W2_pf-complete multi-band stress that passes (b).
  - **EXCLUDED-MB:** a refereed no-go for W2_pf-complete stresses with physical momentum in a stated multi-band class containing the six-band and C₂-exchanged families.
  - **OPEN:** otherwise.
- **Expectation.** EXCLUDED-MB or OPEN. The signed-axis Π_j has k-independent spectra, so it labels bands rather than carrying kinetic momentum. It is likely to fail (b) for the same reason T_pf forces g ≡ 0. A physical multi-band completion would be the first gauge-invariant GW170817 test on a grid and would change W15.

---

## 8. Proposed contents of the 10:20Z wrap-up (updates S17 §5.1)

1. **A plain-words SUMMARY §26 completion and §27.**
   - Correct §26's worker labels for R15-4 and R15-6 (`SUMMARY:711-714`).
   - Add §27 for round 16 in §25's style, with refereed status per line. §1 above is a source.
2. **The final wall map**, in §2's format (W1–W16):
   - each wall's refereed statement and class;
   - DERIVED or OPEN;
   - the cheapest named price;
   - the axiom lines it touches.

   W15 and W16 are new and should not be folded back into W3 or W2.
3. **The consolidated price ledger P1–P106+** under unique S-numbers:
   - the §3.1 collision table (P-r13a/b/c, P-r14a, P-r15a/b/c, P-r16a vs P-r166a vs P-r16-10a, P-r16-7a = P-r16-11a);
   - every price marked "named, never adopted";
   - the refereed rulings that make some named prices non-payable under registered readings: P74 is a FAIL; P92 is a counterterm.
4. **The final owner memo**, from §4:
   - Q1 (Λ: signalling vs law-fixed zero vs tuning);
   - Q2 (initial TT datum and `AX:94`);
   - Q3 (the cone bill and its counting conventions);
   - carried Q4–Q7;
   - "open in every option".
5. **The theorem list.** Every DERIVED or bounded EXCLUDED/FAIL result of C5, with exact class, referee file:line and date, cited as "item + name" (§3.1). New in rounds 15–16:

   | Item | Result | Verdict |
   |---|---|---|
   | R15-1 | Lemma S (FAIL) | `vR15-1:19` |
   | R15-3 | Theorem C(i) | `vR15-3:15` |
   | R15-4 | Lemma N+ (bounded FAIL in 𝓡⁺) | `vR15-4:60` |
   | R15-5 | compact-character O(k³), liftable orders | `vR15-5:47` |
   | R15-6 | Theorems M and L | `vR15-6:19` |
   | R16-1 | Theorem W | `vR16-1:19` |
   | R16-2 | Lemmas Q and T′ | `vR16-2:17` |
   | R16-3 | Z1 and B″ | `vR16-3:19` |
   | R16-4 | free-TT memory | `vR16-4:19` |
   | R16-5 | T_pf | `vR16-5:25` |
   | R16-6 | Theorems Z and NA (narrowed) | `vR16-6:64` |
   | R16-7 | Theorems B (normalized) and D | `vR16-7:17` |
   | R16-8 | kernel and curvature statement | `vR16-8:17` |
   | R16-9 | continuous Lemma R / R_U relaxations, fast-state identity (no conflict theorem) | `vR16-9:21` (not yet in `TESTS`) |

6. **The dated-corrections table**: S17 §1.8 plus §5 above, so downstream text does not cite superseded forms. Most exposed: "T₂g never zeroed", "freezes in black holes", K5's 1e122, "κ_γ required", Lemma CU's universality, R15-2's constants, R16-6's "FAIL text is false".
7. **Pending at close.** Every item without a referee verdict, with its worker reading labelled: R16-10 REFUTED-ZERO/OPEN, R16-11 TRANSFERS, R16-12 OPEN, R16-13, R16-14, and any R17 launched. Record R16-9's verdict (OPEN) in `TESTS` if it is not yet there.
8. **Calibration** across S5–S20 (§6 here; `S17:161-167` for S14), with the "changed hypothesis" lesson.
9. **Provenance.**
   - All workers and syntheses are Claude Opus 5.5 (same family); every verdict is codex gpt-5.6-sol (xhigh).
   - List the findings that never reached a referee, at minimum: R16-1's Z-width transfer to D1 (`C5_R16-1_report.md:301`); R16-4's E2 memory figure; R16-9's uncomputed rows and the shear-row minimality; R15-3's dark-partner option.
10. **What would change the picture.**
    - A gapless Z₂ tensor phase, or an f-sum WINDOW at N = 2 (R17-1).
    - A mechanism that forces the gravitating zero (R17-3 ENFORCED).
    - R16-13 lifting the shear tension, or R17-4(f) certifying it.
    - A multi-band W2_pf completion (R17-5).
    - R16-10's referee ruling on superluminal photons.
    - A physical-domain closure of W7 (R16-12, R17-2).
    - R16-14 breaking the E1/E2 tie on PPN.
11. **Handoff**, per `pr-or-delete`:
    - keepers to land by PR: packet files, and runners worth keeping, e.g. R16-1 Theorem W, R16-3 Z1/IBP, R16-5 T_pf, R16-6 identity scripts;
    - everything else in `SP/` to delete.

    No repository edits in the wrap-up without the owner.

---

## 9. Caveats

- **Same family, unrefereed.** Everything in this synthesis written by S20 is unrefereed and from the same model family as the workers:
  - the DERIVED/OPEN and "cheapest price" columns, W15/W16 as walls, the P74–P106 numbering;
  - every [S20 reading], including the Theorem NA argument in §1.6 and the "W10 collapses onto P51" reading;
  - the owner questions and the R17 drafts.
- **Pending.**
  - R16-9's verdict (OPEN) is taken from the referee's files in `SP/ref_R16-9/` before its `TESTS` record. If the recorded verdict differs, §1.3, W4, W11, P62, P100 and Q3 change.
  - R16-10's Dirac zero depends on whether superluminal photons are in the class.
  - R16-11's TRANSFERS and R16-12's Theorem B3 are worker no-gos, with referees running.
  - R16-13 and R16-14 have no reports.
- **Bounded, not class-wide.**
  - R16-1 covers 𝒬_W⁺ at fixed λ > 0;
  - R16-3's B″ covers gentle-valley laws, and Z1 is prescription-scoped;
  - R16-5's T_pf covers massive free single-band matter;
  - R16-6's Theorem Z covers the homogeneous R14-5 equations;
  - R16-7's Theorems B and D cover exact integer-law finite slots and the stoquastic conserving class, with no readout bridge;
  - R15-1's FAIL covers the smooth continuum R14-5 model on an existing CMC foliation;
  - R15-3 covers finite continuous PSD Gaussians.

  **No refereed result says the split, the graviton or Λ is impossible in general.**
- **Prescription scope.** Every Ξ and μ_E statement uses R9-9's vertex, an assumed standard W1, and a supplied zero-point vacuum. They are bare-cone shifts, not dressed poles. No W2_pf-invariant split exists to replace them (R16-5).
- **Scale bridge.** Every Planck-unit number uses a = ℓ_P, which the axioms leave open (`AX:189-190`): the ~1e-13 to 1e-16 precisions, the 1e-120 initialization, W_π = 0.095/a.
- **The sets are not exhaustive.** Relational and non-commutative constructions remain unexamined.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items. R17-2 should follow R16-12's referee, and R17-4(f) is conditional on R16-13.
