# C5 S17: synthesis after rounds 13–14 (refereed: R12-5 … R12-7, R13-1 … R13-8, R14-1 … R14-5; round 15 pending)

**Author.** Claude Opus 5.5 (S17), the same model family as every C5 worker, the supervisor and S5/S8/S11/S14. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict as recorded in `TESTS.md` or in the cited `C5_*_referee_verdict.md`. Written 2026-10-12, 22:05Z to about 22:16Z. No repository file was edited.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:4447-4988` (round 12 items 4–5 to the end); `agents/C5_S14_synthesis.md`; `SUMMARY.md:534-675` (§§21–25); referee verdicts `C5_R12-5`, `R12-6`, `R12-7`, `R13-1` … `R13-8`, `R14-1` … `R14-5` (`_referee_verdict.md`). **Read in part:** price sections of the worker reports `C5_R12-5:220-238`, `C5_R12-6:265-284`, `C5_R12-7:147-155`, `C5_R13-1:254-263`, `C5_R13-2:167-176`, `C5_R13-3:272-283`, `C5_R13-4:216-224`, `C5_R13-5:382-393`, `C5_R13-6:420-458`, `C5_R13-7:30-81,236-241`, `C5_R13-8:236-262`, `C5_R14-1:124-213`, `C5_R14-2:250-273`, `C5_R14-3:243-261`, `C5_R14-4:144-154`, `C5_R14-5:285-341`; `TESTS:3403,3796-3797,3839-3846,3889-3900` (the ¼ correction, R9-1, R9-2). **Pending, used only as pending:** R15-1, R15-2, R15-4 (workers running; registrations `TESTS:4926-4951,4971-4988`); R15-3 (referee running; worker reading `TESTS:4962-4967`, `C5_R15-3_report.md:228-243`).

**Paths and abbreviations.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY` are in `P/`; bare `C5_*` are in `P/agents/`; `vR13-4` abbreviates `C5_R13-4_referee_verdict.md` (and so on). `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `S14` = `C5_S14_synthesis.md`.

**Labels.**
- **[ref]** referee-confirmed, with the referee's scope.
- **[ref, bounded: …]** a refereed FAIL, EXCLUDED or no-go, with its class.
- **[worker]** a worker claim the referee did not confirm or did not rule on.
- **[pending]** round 15 (R15-1, R15-2, R15-4 workers; R15-3 referee).
- **[S17 reading]** an interpretation made here; same family; unrefereed.

**Sets** (as S8–S14). A = continuum base, discreteness only in records. B = Euclidean Z⁴. C = the axioms' Z³ with continuous time, tuned. C-box = Z³ × ℝ with a box-exact law. C-box-S = C-box with boson–fermion pairing per cell.

**Record-keeping note.** `SUMMARY` now runs to §25 (rounds 10–12, `SUMMARY:637-675`). Rounds 13–14 are recorded only in `TESTS`. §1 below could serve as the plain-words source for a §26; this synthesis does not write it.

---

## 1. What changed since S14, in plain words

### 1.0 The short version

S14 named three lattice routes that might still tie the electron's light cone to the photon's without tuning, one unpriced window for producing the graviton, and two ways out for set A. Two rounds later:

1. **Every named route for the electron–photon split stopped, each in its own subclass.** None stopped in general. In one regulated subclass it is now proved that the split cannot vanish over any range of masses (R13-7). The worker's reading, not refereed as a theorem, is that one tuning at small mass then fixes it for every light particle.
2. **The graviton still is not produced.** Two more linear (Gaussian) escapes are closed by refereed theorems: plain six-pair tensors (R13-2) and the same with position–momentum mixing (R14-4). A third, extra fields (R15-3), awaits its referee. What is left is non-smooth or non-local kernels, constrained theories with an indefinite energy, and strongly coupled phases.
3. **The box laws used so far moved faster than light at the lattice scale.** That has been repaired: a slower-than-light box keeps every matter result (R13-4, R14-1). On a slower-than-light edge the shear mass can be cancelled by one shape choice (R14-3). On edges without extra valleys the graviton is provably slower than matter (a stated class); with extra valleys one polarization can be brought to zero, and the other has not been.
4. **Set A's two exits now cost about the same.** The start-time model's literal kernel drags a neutron star; double-pulsar timing kills it by 11 orders of magnitude (R13-6). A signed kernel repairs it. The leaky-wave route drags too, which limits the leak to a few percent of the Hubble rate (R14-2). Both are OPEN, and on the stated tests they tie.
5. **Λ got a sharper candidate and a sharper bill.** Any smooth mechanism that soaks up vacuum-energy changes this way must use constant-mean-curvature slices as lattice time, with one global number per instant (R14-5, Lemma C). The mechanism is credible in idealized settings. It is not shown through phase transitions, in a lumpy universe, or for causality.

**[S17 reading], the one-sentence picture.** Since S14 the campaign has turned most "maybe" routes into theorems inside stated classes. The remaining choices are now mostly prices Jon can name (a counterterm, an edge shape, a start time or a leak, a global clock), not unknowns. The graviton is the exception: nothing produces it except supplying it.

### 1.1 The electron–photon split: every named route stopped in its subclass

S14 listed three candidates (`S14:86`). All three now have refereed outcomes.

- **R12-6, twisted N=4 Kähler–Dirac box QED: INCONCLUSIVE, with a sharp 𝒦₀ obstruction [ref; `TESTS:4696-4703`; `vR12-6:21-23`].**
  - The equivariant (σ, η) completion gives Q² = iσL and H ≥ 0. Cochain symbols give finite-range locality; box symbols only quasi-locality. The free photino is doubler-free, with K² = Δ (`vR12-6:5-7`).
  - **In the minimal-Hessian class 𝒦₀** the photon log coefficient is −8 and the matched electron's is −2 (units e²/16π²). So c_e − c_γ contains +6 ln(1/m): not protected, not zero (`vR12-6:13-15`).
  - The B repair removes the photon log. It leaves an electron log, shown only numerically.
  - **Theorem L′:** the scalar Q plus cubic symmetry does not fix c_γ/c_e. It does not prove that a full extended N=4 algebra adds no relation (`vR12-6:17`).
  - **The neutral scalar σ is excluded as massless:** with complex σ the anomalous moment shift is α/2π ≈ 1.16e-3, against agreement at about 1e-12. Correction: the worker's 3α/2π is the one-real-scalar value (`vR12-6:19`). A bare σ mass breaks the displayed Q.
  - Still open: τ-coupled, non-Hessian and full extended-N=4 completions.
- **R13-1, momentum in the superalgebra: INCONCLUSIVE, with a rigorous bounded Theorem B [ref; `TESTS:4715-4720`; `vR13-1:43`].**
  - **Theorem B:** take a C¹ periodic one-body band-scalar momentum and a whole-zone Peierls vertex. Then Jacobi plus the nonvanishing transverse vertex forbids an exact supercharge algebra on the full zone (D2). The algebra forces p_e(k_x + q) − p_e(k_x) = p_γ(q) for all k_x, and periodicity forces p_e constant (`vR13-1:9-18`).
  - At the free level the algebra does not identify p with lattice momentum, and does not bound a massive particle's IR speed. Correction: the worker's 1 − m²/b² bound is false; a counterexample gives c_e² = 0.5 (`vR13-1:3-7`).
  - Corollary BPS holds only for the photon half (c_γ = 1 for short multiplets) (`vR13-1:20`).
  - For the chosen off-D1 completion, the one-loop split is negative in all 24 sampled laws. The literal-edge photon coefficient is a sign-indefinite moment of the product-rule defect (`vR13-1:22-39`).
  - Not covered: dressed or higher-body, band-matrix, non-local or infinite-flavour momentum.
- **R13-4(i), the BF photon multiplet's tail: PHYSICALLY NON-LOCAL in class 𝓔 [ref, bounded: 𝓔; `TESTS:4772-4775`; `vR13-4:22`].**
  - For the charged BF quotient law with the inherited flat measure, reduction produces a four-fermion neutral-pair transfer with a Coulomb 1/r kernel. A bounded local gauge-invariant observable detects it, so no finite-range or super-polynomially quasi-local extension in 𝓔 keeps the same physical content.
  - Correction: the full norm is 213.897751074 e²G(r), not 56 e²G(r). This strengthens the no-go (`vR13-4:5`).
  - The zero-fermion sector is constraint-solving, as in Coulomb-gauge QED. R12-6 localizes the interaction only by adding physical modes.
  - S14's expectation ("LOCAL-EQUIVALENT for the bosonic part") was right for the bosons and wrong for the content that matters.
- **R13-7, is the split a theorem? SUGGESTED overall, DERIVED in a regulated literal-edge subclass [ref; `TESTS:4844-4858`; `vR13-7:30`].**
  - **The subclass:** one loop, fixed photon-mass regulator λ > 0, literal-edge Peierls Dirac electron. S is odd and periodic with S(q) = q in its box. t = d² is even and periodic (correction to the worker's "d even", `vR13-7:22`). |S| ≤ |q|, and the heavy-limit weight is convex on the electron edge.
  - **The result:** Δ_λ(m) = c_e − c_γ is real-analytic for m > 0. δc_γ = O(m⁻³), and δc_e → ¼⟨A(W² − d_x²)/(d_x²W³)⟩ < 0, a lattice "4/3 problem". So Δ_λ cannot vanish on any open mass interval.
  - **Not covered:** Wilson edges, general ℓ¹ generators, partners, arbitrary photon shapes, λ = 0. Outside H2 the heavy constant changes sign (−2.3723 to +1.7484) and can be tuned to zero. The next coefficient stays nonzero (re-tuned e₁·16π² ≈ −24, `vR13-7:26`).
  - **The referee on "per-mass tuning":** the registered gloss is too strong. Exact interval cancellation and agreement for finitely many tiny lattice masses are different demands. The worker's "one light-mass tuning suffices physically" (|c_e − c_γ| ≲ 1e-25 after one tuning of Δ(0⁺), against the 2.66e-19 photon-decay bound; `C5_R13-7_report.md:50,211`) is "a plausible finite-precision reading, not a theorem" (`vR13-7:28`).
  - **[S17 reading] about the subclass.** The proved subclass uses the literal edge (R8-5's BQ law with r = 0; `C5_R13-7_report.md:60`). That is the law whose seven same-mass electron corner valleys add about 588 MeV to the Z width (R9-1, L under G-out EXCLUDED, `TESTS:3840`). The physically usable Dirac edges are Wilson edges, including R14-1's subluminal D1(r) (§1.3), and these are outside the theorem. The Wilson control grows linearly in m with a shape-dependent sign (`C5_R13-7_report.md:48,144-148`). R16-1 below targets this gap.

**[S17 reading] Where the split stands.** No untuned zero exists in any refereed subclass: minimal box QED (R8-5), photon-only pairing (R10-1), SUSY in 𝒮 (R10-5), N=4 KD in 𝒦₀ (R12-6), spinor SUSY with one-body band-scalar momentum (R13-1 Theorem B), BF without extra modes (R13-4(i)), and the literal edge (R13-7). Still open: τ-coupled, non-Hessian and full extended-N=4 completions; dressed or infinite-flavour momentum (the KSS escapes); Wilson edges. The cheapest named price is one tuning of the light-mass value (P48, refined as P73).

### 1.2 The graviton: two more Gaussian escapes closed (a third pending), three windows left

- **R12-5: OPEN [ref; `TESTS:4543-4550`; `vR12-5:17`].** DW-q exactly removes non-invariant Weyl characters at first order in a sharp constraint sector. The finite-penalty Gaussian is unstable (scalar determinant −J²/2). **Correction:** "one exact constraint caps TT at k²" is not class-wide. An exact-S/energetic-G control with a regular local h-potential has five linear modes, two TT and three partners (`vR12-5:7`). Gu–Wen's freeze argument has a genuine first-order tension with DW-q, but strong coupling is not shown to fail X1's hypotheses (`vR12-5:11`). Xu's model is not partner-free (`vR12-5:15`).
- **R13-2: EXCLUDED, bounded X-G [ref, bounded: six symmetric-tensor pairs, PSD Gaussian; `TESTS:4758-4770`; `vR13-2:25`].**
  - In a real, local, C⁴, cubic-covariant PSD Gaussian Hamiltonian of exactly the six symmetric-tensor pairs, two gapless axial TT modes force two vector partners and one scalar partner at k = 0 (Lemma P, by Schur at the cubic point, `vR13-2:11`).
  - If the vectors are instead flat through a one-sided transverse gauge kernel, positivity forces ω_TT = O(k²) (Theorem G, now exact over ℚ, `vR13-2:15`).
  - The Monte Carlo shows only that PRODUCED was not demonstrated (`vR13-2:19`). Corrections: factor-two energies, Z₄ labels (896 negative coefficients, not 512), harmonic √6 not √3.
  - S14 expected OPEN; the referee changed the reading to EXCLUDED because X-G met the fixed rule (`vR13-2:23`).
- **R14-4: EXCLUDED, extension of X-G to mixed h–E kernels (G-mix) [ref, bounded; `TESTS:4898-4902`; `vR14-4:40`].** Six pairs per cell, C² symbol at k = 0, proper-cubic covariance, arbitrary h–E mixing: if both axial TT polarizations are linear, some direction has at least three positive linear branches. Parity-odd terms are covered (`C5_R14-4_report.md:153`). Corrections: "gyroscopic terms only add branches" is too strong; the Williamson rank identity is replaced by an inertia argument that gives the same bound (`vR14-4:7,17-19`).
- **[pending] R15-3, auxiliary irreps.** Worker Theorem C, by characters at C4 and C2′: in class 𝒜 (any finite auxiliary content, PSD, O-covariant, symbol continuous at k = 0), two gapless TT branches force at least 4 gapless branches, or at least 5 with an h coupling. Exactly 2 only for a discontinuous symbol (`TESTS:4962-4967`). Referee running.
- **What is left [S17 reading, from `vR13-2:25`, `vR14-4:40`].** Non-C² or non-local symbols (a k²P_TT(k̂) symbol has flat partners); indefinite exact-constraint theories (P-N3″, `C5_R13-2_report.md:172`); non-Gaussian strongly coupled phases. The only known source of a light-like TT branch is still the supplied non-compact CCR graviton (P-N1).

### 1.3 The box route: faster than light at the lattice scale, then repaired

- **R13-4(iii): the box profiles actually used are superluminal [ref; `TESTS:4777`; `vR13-4:9-14`].**
  - **Lemma V** (odd-symbol square-root laws): v_max ≥ (√(m² + b²) − m)/(π − b), with threshold b*(m) = π(2m + π)/(2(m + π)).
  - The reruns give v_max 4.1161, 12.4157 and 4.5691 for the laws in use. Merely lowering b in the old blend is not enough (b = 1.4 still gives 2.3078). A derivative-controlled construction gives 0.9927 in 3D.
  - Leakage in the superluminal window decays only as a power: an independent CAR calculation gives ‖[n_r(t), n₀]‖ ~ t^{−1/2} (`vR13-4:16`).
  - The earlier box results survive within their scopes after the edge is replaced. Old edge velocities, tail constants and parameter-specific numbers do not automatically transfer (`vR13-4:20`).
- **R14-1: PASS, every listed box result survives a subluminal box [ref; `TESTS:4808-4813`; `vR14-1:19`].**
  - A smooth, Gevrey, whole-zone subluminal b = 1.4 odd-symbol completion keeps R7-1, R8-1, R9-2, R9-6 and R11-4 within their inherited scopes, once the d = 2, 3 transition support shrinks to Π₂ < 0.992. Global edge stresses and shell quantities must be recomputed.
  - **Correction to R9-2:** its whole-zone stress operator changes. Only box-to-box matrix elements and the uniform-lapse first moment are unchanged (`vR14-1:5`).
  - **Cost of the odd completion:** seven exact d = 3 corner valleys, exact copies of the box at mass m, with componentwise sign-flipped boosts (`vR14-1:9`). Box-supported vertices never reach them; a Peierls vertex does (`C5_R14-1_report.md:134`).
  - **Lemma V re-scoped:** a separate even gapped completion is subluminal for every b < π, with no light corners. This disproves only TESTS' overbroad paraphrase "every one-band box law" (`TESTS:4782`); the actual theorem was already restricted to odd-symbol laws (`vR14-1:11`). R8-2's own gapped band has v_max = 0.9966425.
  - **Dirac matter:** oddness is forced by the axis π-rotations with spinor covariance (`C5_R14-1_report.md:186`, worker). The Wilson construction is rigorously subluminal for r ≤ 1/√d, with light doublers (`vR14-1:15`): corner masses m + nW_π with W_π = 0.095/a at b = 1.4, at most 0.597/a in the family (`C5_R14-1_report.md:200-211`, worker). R8-5's Ward no-go and cone split were not rerun on it.
- **R14-3: REFUTED, so the shear mass is not a causality-versus-tuning dilemma [ref; `TESTS:4915-4922`; `vR14-3:22`].**
  - In the separable periodic one-band class, |σ′| ≤ 1 certifies whole-zone subluminality.
  - **(a) refuted:** the smooth gapped G_w(1.4) family has an exact conditional shear zero at each fixed mass (w* = 0.3896, 0.3494, 0.3449, 0.3444 for m = 1, 0.3, 0.1, 0.01). One common massless-limit setting suppresses, not cancels, the shear of all light common-edge species, by O((ma)²) (`vR14-3:12,18`).
  - **(b) refuted outside 𝒰₀ only.** Theorem B: Ξ < 0 for every nonnegative nonzero transverse vertex independent of k_z, on the no-gapped-valley class 𝒰₀ (`vR14-3:14`). Outside 𝒰₀, the subluminal W08/W14 bands give positive E_g shifts, so E_g has a zero by interpolation. Every tested T₂g shift stayed negative; no nonnegative T₂g witness was found (`vR14-3:16,22`).
  - The empty Fock vacuum has zero shear, as before.
  - The worker's revised dilemma: for the shear, a tuning; for the graviton, "a tuning plus heavy edge valleys, or an unremovable Ξ < 0" (`C5_R14-3_report.md:250`, worker reading).

### 1.4 The graviton–matter cone (GW170817)

- **R13-5: OPEN both without and with pairing [ref; `TESTS:4707-4714`; `vR13-5:21`].**
  - **Lemma P1:** for a massive free scalar and a smooth spatial pair kernel, the first-order Ward identity (W1) uniquely fixes the time components. The conjugate channel restores Hermiticity.
  - **Lemma B2 (the blocker):** under the standard undeformed Dirac–Schwinger meaning of the second-order Ward identity (W2), the pair terms drop out of H, P and K. The periodic-band boost anomaly (Theorem E) is then a bounded obstruction to second-order closure. This holds for the standard W2, not for every preferred-background or deformed identity (`vR13-5:7`). So the registered test, which demanded a W2-complete stress, has an empty class to compute in (`vR13-5:13`).
  - **In the W1-only class 𝒲_V** (an extra law assumption): the G edge has a strictly negative TT floor, 4.37e-3 to 5.46e-3 at a = ℓ_P for m = 1 to 0.01 (correction: not uniformly ≥ 5e-3, `vR13-5:9`). Light-L doublers destroy that floor.
  - **Correction to R11-1(b):** birefringence is removable by a one-mass edge tuning (G-U: E_g weight c = 6.140189; L-U: T₂g weight c = 4.160499). R11-1's "at most one cone" holds for M/U, not class-wide (`vR13-5:11`).
  - **Pairing** cancels the stipulated TT response and leaves 2κ_lat m²J₂. Correction: not 4κ_lat m²J₂ (`vR13-5:15-19`; the worker's price text `C5_R13-5_report.md:392` still has 4).
- **[S17 reading]** On every grid set, GW170817 is now a question about which second-order Ward identity the law obeys. The standard one cannot be met. A preferred-frame (deformed) one has not been written down. R16-5 below drafts it.

### 1.5 Set A: the start time and the leak, on equal terms

- **R12-7, E2 (GW friction): OPEN [ref; `TESTS:4551-4559`; `vR12-7:17`].** For each preferred-frame scalar mode the finite bank works and the telegraph propagator is causal, boost-stable and exactly Newtonian at zero frequency. A classical outgoing Lamb string realizes noiseless friction for a toy mode. Spatial-TT-only friction is generically acausal at O(γ). No current comparator excludes γ ≲ H₀; Lu et al.'s 2.98 H₀ is only a fixed-distance benchmark, and the EM-counterpart scale is about 62 H₀ (`vR12-7:11`). PPN is unclosed. Missing: a spin-2 dilation, a conserved gravitating bath, and a nonlinear completion.
- **R13-6, E1 (start time): EXCLUDED for the literal class; OPEN once the gain is repaired [ref; `TESTS:4728-4732`; `vR13-6:43`].**
  - **Lemma D:** within the linearized preferred-CMB-frame model with R11-5's literal causal gain e^{−k²ℓ²/2}(1 − iωℓ/c)^{−n}, n ≥ 3, a compact body acquires a self-drag −(4πG/3)(nℓ/c)(∫ρ²)v. Double-pulsar timing then needs ℓ < 3.74e-21 m, excluding every ℓ_s in the class by 1e11 to 1e15 (`vR13-6:7`).
  - **This is a dated correction to R11-5:** its literal kernel 𝒦_ε is excluded; R11-5's OPEN applies only to the repaired, zero-first-moment gain (`TESTS:4732`). Lemma D does **not** touch R6-4, whose backreaction is instantaneous (δ = 0) (`vR13-6:9`).
  - **The repair (P-r13b of R13-6):** a signed, zero-first-moment gain such as (1 − 4ix)(1 − ix)^{−4}. It passes the τ = ℓ/c test. It is a changed class (`vR13-6:15`).
  - **Lemma S:** R11-5's s₀ = 0 profile has a Stieltjes density that is negative on ε² < t < ε, so no positive cone-centred Lorentzian synthesis exists for it (`vR13-6:25`).
  - Correction: ḣ = ξ − Ω(J₁ * ξ) contains a white-noise term, so pointwise Var ḣ needs a bandwidth regulator (`vR13-6:31`).
  - S14 expected "OPEN leaning VIABLE; the noise-fed PPN term is the likeliest failure". The failure came from self-drag instead.
- **R14-2, E1 against E2 with the drag fixed: both OPEN and observationally tied [ref; `TESTS:4891-4897`; `vR14-2:13`].**
  - **E2's own drag:** Γ_i = 2γ|U_i|/(3M_ic²), Ṗ_b/P_b = −3Γ_eff. That bounds γ to 0.032–0.047 H₀ (conservative), or 0.016–0.024 H₀ from the signed timing measurement (`vR14-2:3`).
  - So **genuine stationarity of E2 needs a history of 44–65 Hubble times, or 86–127 with the signed limit** (`vR14-2:9`).
  - A causal passive high-pass friction kernel (P-r14a of R14-2) allows faster damping: 62 H₀ conservative, about 31.7 H₀ signed, at ω_c = 3000 rad/s. It costs a cutoff, frequency-dependent GW damping and a larger sink budget (`vR14-2:5`).
  - **E1's window:** the CMB velocity enters the orbit average. The conservative τ_c ceilings are 4.969 ps (in-plane) and 5.792 ps (normal); the in-plane window closes at 1.73e-9 m, or about 3.98 ps and 3.38e-9 m with the signed limit (`vR14-2:7`).
  - The E1/E2 content equivalence (T_eq = 0.56146/γ) and the ≤ 8% budget difference hold asymptotically under shared premises. **E1 is cheaper only under the report's price-counting convention**; no cost metric is defined, and E1's initial-state interpretation is unresolved (`vR14-2:11`).
- **[pending] R15-2** builds E1's spin-2 conserved-noise assembly with the repaired gain.

### 1.6 Λ: from a creation law to a global clock

- **R13-3, P-T in a lumpy universe: NOT CONFIRMED as EXCLUDED; OPEN [ref; `TESTS:4721-4727`; `vR13-3:59`].**
  - **Lemma F:** in a literal smooth continuum V3 completion with ADM lapse N = 1, conserved stress, adiabatic synchronous data and no sufficiently negative C-density or non-smooth reset, slice normals are geodesic and focus in a collapsing top-hat. A scalar creation rule does not remove this caustic. Kinked, lattice-scale or alternative nonlinear completions are not excluded (`vR13-3:12`).
  - **Lemma T:** V2 restores the homogeneous Hamiltonian constraint, so the specified decaying-memory F-law is incompatible with a nonzero constant vacuum unless a tuned compensator is added. Not "every P-T completion forces ρ_v = 0" (`vR13-3:20`).
  - At linear k ≠ 0 the system is GR plus an effective dust component, given the same background and initial data (`vR13-3:32`).
  - Corrections: a top-hat formula error; a falsely printed inequality; the transition runner never tests Prony-node reality and misplaces its tail point (`vR13-3:10-11,49-51`).
- **R14-5, the averaged-lapse model: NOT CONFIRMED as VIABLE; OPEN [ref; `TESTS:4903-4914`; `vR14-5:96`].**
  - **Lemma C (correct):** with E_ni = 0, traceless E_ij = 0 and a spatially uniform E_nn = λ(t), Bianchi gives N(λ + p_E) = g(t) and λ̇ = −gθ_n. Any smooth interval of active vacuum compensation forces CMC slicing. g ≡ 0 on an interval is GR with a constant effective Λ (`vR14-5:16-25`).
  - **A genuine narrow symmetry:** ρ_v → ρ_v + C with λ → λ − κC leaves the geometry unchanged. If the algebraic expansion law is fundamental, λ is a slice multiplier, not a tuned constant. This is **not** standard unimodular gravity (`vR14-5:29-35`).
  - **What fails or is missing:** the homogeneous runner computes λ algebraically, so the endpoint check is mostly of the projector; the reconstructed ρ̂/ρ_nc reaches −3.43, −482 and −34.3 in three runs, giving H² < 0 (`vR14-5:39-42`). The inhomogeneous model gives Λ̃ = ½⟨R⟩ − ½⟨σ²⟩, not zero (`vR14-5:44`). The positivity bound drops curvature and shear terms (`vR14-5:55-62`). Global CMC existence is assumed; Gerhardt's theorem does not cover this model, and Einstein-dust spacetimes exist with a CMC slice but no CMC foliation (`vR14-5:64`). g ≠ 0 causality and Hamiltonian stability are unproved; the cuscuton no-information argument does not transfer automatically (`vR14-5:86-88`).
  - **The worker's own kill round** (unrefereed) finds the model fails if the vacuum is the grid's zero-point (w ≥ 0, R11-3): then g/H² ~ 1e122 (K5, `C5_R14-5_report.md:317-320`). So the model needs a w = −1 vacuum supplied by a bridge.
- **[pending] R15-1** (causality, stability, strong coupling, CMC through collapse, and the vacuum it needs) and **R15-4** (a regular reader through transitions and lumps).

### 1.7 Set C's count

- **R13-8: OPEN, not COUNTED [ref; `TESTS:4803-4807`; `vR13-8:24`].** Under proper cubic rotations the on-shell TT ranks are (2, 2, 5) at derivative degrees 0, 1, 2; with P and T, (2, 0, 4). Exact linearized diffeomorphism invariance leaves a two-dimensional degree-2 kernel whose TT image is the single graviton-speed direction; every other TT structure is a Ward-defect candidate. Bookkeeping, not an established one-loop count: **N_s + 7** (P,T-even: N_s matter speeds, 1 graviton speed, 3 anisotropies, 2 masses, 1 LV tadpole) plus the CC; generic **3N_s + 8**, or **3N_s + 10** without the unproved removal of two degree-1 terms, or **3N_s + 11** before k_AF's protection (`vR13-8:15-20`). The earlier "≥ 6" (`SUMMARY:435`) was incomplete bookkeeping and remains only a reading (`vR13-8:20`).

### 1.8 Corrections the record now carries (dated 2026-10-12)

| Correction | What it was | What it is now | Source |
|---|---|---|---|
| **R11-5 Lemma D drag** | R11-5's literal causal kernel 𝒦_ε read OPEN | Excluded by double-pulsar self-drag; OPEN applies only to the zero-first-moment repair. R6-4 untouched | `TESTS:4729,4732`; `vR13-6:7-9` |
| **¼ prefactor withdrawn** (earlier, kept for completeness) | R7-1 referee: "the quartic prefactor must be ¼" | Withdrawn by the R8-1 referee: ½ is correct for the ordered kernel; R7-6's drift is δ ≈ 0.074, not 0.019 | `TESTS:3403,3796-3797`; `SUMMARY:614` |
| **Lemma V re-scoped** | TESTS paraphrase: every one-band box law with b > b*(m) is superluminal | Only odd-symbol square-root laws. An even gapped completion is subluminal for every b < π | `TESTS:4782,4811`; `vR14-1:11` |
| **Box superluminality and its repair** | R7-1, R8-1, R9-2, R9-5, R9-6, R8-5 laws treated as causal | Superluminal at lattice scale (v_max 4.1–12.4), power-law leakage; repaired by a subluminal b = 1.4 completion (PASS within scope), whose odd form has seven exact corner valleys; old edge constants do not transfer | `TESTS:4777,4808-4813`; `vR13-4:14,20`; `vR14-1:19` |
| **R9-2 shear wording** | "profile-family zero at t* = 0.287922, an edge tuning" | That zero sits on a superluminal edge (d = 3 v_max 1.73396; 1.595 is the d = 1 value). On subluminal G_w the zero exists at each fixed mass; a common setting suppresses by O((ma)²), not exactly. R9-2's whole-zone stress operator changes under the repair | `TESTS:3900`; `vR14-1:5,13`; `vR14-3:18` |
| R11-1(b) birefringence | "a scalar matter cone can coincide with at most one graviton polarization's cone" | Holds for M/U only; removable by a one-mass edge tuning | `vR13-5:11` |
| R12-5 cap | "one exact constraint caps TT at k²" | Not class-wide (five-linear-mode control) | `vR12-5:7` |
| R13-5 paired residue | 4κ_lat m²J₂ | 2κ_lat m²J₂ | `vR13-5:15-19` |
| R12-6 a_e | 3α/2π | α/2π ≈ 1.16e-3 for complex σ; still excluded | `vR12-6:19` |
| R13-1 massive bound | IR speed ≥ 1 − m²/b² from the algebra | False without an extra hypothesis | `vR13-1:3-7` |
| R13-7 photon symbol | "d even and periodic" | t = d² even and periodic | `vR13-7:22` |

### 1.9 Calibration of S14's round-13 expectations [S17 reading]

- **Right:** R13-1 INCONCLUSIVE ("leaning FAIL" is fair for the sampled continuation, `vR13-1:41`); R13-3 OPEN; R13-4(ii) OPEN.
- **More decisive than expected:** R13-2 (expected OPEN; got bounded EXCLUDED, X-G).
- **Half right:** R13-4(i) (expected LOCAL-EQUIVALENT for the bosonic part; true for bosons, but the charged law is PHYSICALLY NON-LOCAL); R13-4(iii) (expected v ≤ 1 achievable and leakage negligible; achievable yes, but the laws in use were superluminal with power-law leakage).
- **Wrong:** R13-5 (expected SPLIT-PRESENT; got OPEN because the standard W2 class is empty); R13-6 (expected PPN as the failure point; it was self-drag).
- **Missed by S14's drafts:** both the superluminality of the box and Lemma D were found by workers inside other items. Registrations should ask for the group velocity of every law used and for the self-force of every frame-tied kernel.

---

## 2. The wall map

"DERIVED" here means the wall is a refereed no-go or confirmed lemma in a stated class (including bounded EXCLUDED and FAIL). "OPEN" means the route's registered question has no refereed no-go covering its class and no PASS. "Cheapest named price" is the least expensive price on record that passes the wall. Nothing is adopted.

| # | Wall | Refereed statement (scope) | DERIVED or OPEN | Cheapest named price | Price status |
|---|---|---|---|---|---|
| W1 | **Electron–photon split** (C, C-box, C-box-S) | No interval zero in 𝒬_lit⁻ (R13-7). Subclass obstructions: 𝒦₀ +6 ln(1/m) (R12-6); Theorem B (R13-1); BF non-local in 𝓔 (R13-4(i)); photon doubler in 𝒮 (R10-5) | **DERIVED in subclasses; OPEN overall** (SUGGESTED, `vR13-7:28`). The DERIVED subclass is the R9-1-excluded literal edge [S17 reading] | One tuning of the light-mass value Δ(0⁺), by a counterterm or a shape condition (P73 = P48 refined) | "One suffices physically" is a worker reading (`C5_R13-7_report.md:50`), not a theorem (`vR13-7:28`). R16-1, R16-2 |
| W2 | **Graviton production** | X1: O(k³) (R11-2); X-G (R13-2); G-mix (R14-4); aux irreps pending (R15-3) | **DERIVED (three bounded exclusions); production OPEN** | Supplied non-compact CCR graviton (P-N1 = P41/P49) | The only known light-like TT source. Unpriced windows: non-C²/non-local, indefinite constrained (P-N3″), non-Gaussian |
| W3 | **Graviton–matter cone** | Standard W2 empties the test (Lemma B2, conditional); Ξ < 0 on 𝒰₀ for every nonnegative vertex (R14-3 Theorem B; R9-9 vertex scope); E_g zero by interpolation outside 𝒰₀; T₂g never zeroed | **DERIVED in 𝒰₀; OPEN overall** (R13-5 OPEN both ways) | Pairing P46: leaves 2κm²J₂ (negligible), stipulated TT vertex. Unpaired: a per-polarization TT seagull counterterm, or heavy edge valleys + tuning (P63) for E_g only | T₂g has no named untuned or edge-tuned zero. Deformed W2 unwritten (R16-5) |
| W4 | **Free shear μ_E** (supplied zero-point vacuum) | REFUTED as a dilemma: subluminal G_w zero at each mass; common setting O((ma)²) (R14-3) | **Not a wall in the empty vacuum; one shape tuning otherwise** | P62 (P-W*): one edge-shape parameter shared by light species | Tuning, no axiom text (`AX:116-123`) |
| W5 | **Lattice-scale superluminality** | Lemma V for odd-symbol laws (R13-4); subluminal repair PASS (R14-1) | **DERIVED (cause) and repaired** | P61: a subluminal edge. Scalars: even gapped G(b), no doublers. Dirac: Wilson D1(r ≤ 1/√d), corner masses m + nW_π (W_π = 0.095/a at b = 1.4) | R8-5's Ward no-go and split not rerun on D1; global edge stresses need recomputing |
| W6 | **BF photon multiplet** | PHYSICALLY NON-LOCAL in 𝓔 (R13-4(i)) | **DERIVED in 𝓔** | P60: accept the 1/r O'Neill pair transfer, or add σ, η (R12-6: then 𝒦₀ split and a σ that a_e excludes unless massive, which breaks Q) | — |
| W7 | **Off-box gravity tail** (nonlinear closure) | Ansatz needs 1/r^{d−1} (R12-1); gauge vs physical unresolved (R13-4(ii)) | **OPEN** | P50 (unchanged) | — |
| W8 | **Set A, covariant** | 𝒰 no-go (R12-4); literal E1 gain EXCLUDED by Lemma D (R13-6); E2 drag γ ≲ 0.016–0.047 H₀ (R14-2) | **DERIVED walls; repaired E1 and E2 both OPEN, tied** | E1: P65 (start time + age-long memory + signed gain). E2: P66 (dissipative metric + sink + memory + long history or high-pass kernel) | Spin-2 assembly missing (R15-2 pending); "E1 cheaper" holds only under the worker's count |
| W9 | **Λ, fixed grid** | V1: two tadpoles, w ≥ 0 (R11-3); V2/V3 cannot expand | DERIVED (unchanged) | P51 | Unchanged |
| W10 | **Λ, site creation + P-T** | Lemma F (smooth N = 1 continuum caustics, conditional); Lemma T (V2 + decaying F-law needs a tuned compensator); Lemma C (active compensation forces CMC) | **DERIVED lemmas; mechanism OPEN** | P68 (CMC lattice time) + P67 (global reader, regular reader) + P70 (w = −1 vacuum bridge) + P69 (arrow) + P52/P53 | Not shown: CMC through collapse, transitions (H² < 0), lumps (Λ̃ ≠ 0), causality. R15-1, R15-4 pending |
| W11 | **Set C count** | TT ranks and gauge kernel (R13-8) | **OPEN** (bookkeeping N_s + 7 to 3N_s + 11) | P72 | Not an established count |
| W12 | **Matter on the box** (linear gravity) | R11-4 PASS WITH SCOPE; survives subluminal (R14-1) | No wall at linear order | P56 (quadrupole) | Unchanged |
| W13 | **Set B** | R10-2 (RP fails for smooth box symbols) | DERIVED (unchanged) | Give up RP (5 + Λ) or whole-zone SLAC | Unchanged |
| W14 | **Λ, set A q-charge** | μ fixed by the final vacuum to 2.1e-55 (R10-4) | Minimal realization excluded; OPEN beyond | P54 (Q4 or Q5) | Unchanged |

**[S17 reading] The shape of the map.** The DERIVED entries now outnumber the OPEN ones, and every DERIVED entry has a stated class. The OPEN entries split two ways. Four are open because a construction is unbuilt: W2's non-Gaussian windows, W7, W8's spin-2 assembly, and W10's global questions. Two are open only because the proof does not yet cover the physically used law: W1 (Wilson edges) and W3 (T₂g, deformed W2). The second kind is what the next round can close.

---

## 3. Price ledger delta since S14 (P58 onward; named only, none adopted)

S14 ended at P57 (`S14:188`). **Naming collision:** worker labels repeat across items. "P-r13a/b/c" mean different things in R13-3 (Λ) and R13-6 (set A), and "P-r14a" means a friction kernel in R14-2 and CMC lattice time in R14-5. The S-numbers below are unique; the wrap-up should use them.

**Axiom lines.** Lattice `AX:37-41` (sites "points of the cubic lattice Z³" `:37`; "No site is privileged" `:40`). Qubit `AX:45-53` (M₂(C) `:47`). Admissibility `AX:57-61` ("one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations" `:57-58`); reading notes `:63-73`. Record `AX:77-83` ("Records form" `:77`; "records are permanent" `:80`; "Only records are readable" `:82`). Qualification `AX:87-95` ("A law privileges no states" `:94`). Not a dynamics axiom `AX:116-130` (no Hamiltonian, transfer operator or time metric). Open gates `AX:173-190` (formation rules `:182-184`; arrow, record-production dynamics, time metric `:185-186`; source/action `:187`; scale reference `:189-190`).

**Status changes to earlier prices.**
- **P47** (photon multiplet outside 𝒮): the menu is now three refereed options, each with a cost: a doubler (𝒮), a physically non-local O'Neill term (BF, `vR13-4:22`), or N=4 KD content whose 𝒦₀ completion leaves +6 ln(1/m) and an a_e-excluded massless σ (`vR12-6:23,19`).
- **P48** (no momentum in the superalgebra): now also bounded by Theorem B (`vR13-1:18`). Refined as P73.
- **P49** (graviton menu): P-N2 unchanged; P-N3 sharpened to P-N3″ (P71).
- **P55** (set A past 𝒰): split into P65 (E1) and P66 (E2).
- **P57** (dD-M coupling): "at most one cone" corrected to M/U only (`vR13-5:11`).
- **R11-5's literal gain** (the 𝒦_ε family behind P-r9b′'s bank): excluded by Lemma D (`TESTS:4732`). Its role passes to P65's J₀ channel and signed gain.

| # | Price (named only) | Axiom text touched | Set | What the refereed record says it buys or costs |
|---|---|---|---|---|
| P58 | **N=4 KD content and its σ (R12-6).** Per site: gauge multiplet 9 real CCR (8 physical) + 8 CAR; matter 16 CCR + 16 CAR. H = ½{Q, Q†}, Q² = iσL. A selectron degenerate with the electron. A neutral σ with Yukawa √2e: massless is excluded by a_e (α/2π vs 1e-12); a mass (worker: ≳ 1e2 GeV) breaks Q softly and brings back the O3 vacuum and mass-split residuals | Qubit `AX:47`; dynamics `AX:116-130` | C-box-S | Buys a local (cochain) or quasi-local (box) doubler-free photino. Does not buy the split in 𝒦₀ (+6 ln(1/m)). `vR12-6:5-23`; `C5_R12-6_report.md:265-283` |
| P59 | **Spinor SUSY with momentum in the algebra (R13-1).** About 7 CCR + 6 CAR per site (the cheapest SUSY content tried). The algebra's P is a symbol momentum, equal to lattice momentum only on box states; an exact whole-zone algebra is forbidden in the one-body band-scalar class (Theorem B). Exactness needs dressed, band-matrix, non-local or infinite-flavour momentum (the KSS escapes), or set A | Qubit `AX:47`; `AX:116-130`; Admissibility `AX:57` if the escape is non-local | C-box-S | Buys c_γ = 1 for short multiplets (Corollary BPS, photon half). Does not buy the electron. `vR13-1:18-20`; `C5_R13-1_report.md:254-262` |
| P60 | **The BF non-local term (P13-4a).** A four-fermion neutral-pair transfer with a Coulomb e²G(r) kernel, physically non-local in 𝓔 | Dynamics downstream (`AX:116-130`); against `AX:57` only if "nearest-neighbor" is read as a range limit on dynamics, which `AX:116-130` do not support [S14/S17 reading] | C-box-S | `vR13-4:5,22`; `C5_R13-4_report.md:220` |
| P61 | **A subluminal edge (P13-4b, re-scoped).** Odd-symbol laws need b < b*(m) or a derivative-controlled step: seven exact same-mass corner valleys (reached by Peierls vertices, R9-1-type), interaction plateau shrinks to Π₂ < 0.992, shell sources grow about 7.5× (worker). Scalars: even gapped G(b), subluminal for every b < π, no light corners. Dirac: Wilson D1(r ≤ 1/√d), corner masses m + nW_π | Admissibility `AX:57` (quasi-locality, already priced); dynamics downstream `AX:116-130`. No new axiom text | C-box | Buys whole-zone v_max < 1 and keeps R7-1…R11-4 within scope (`vR14-1:19`). Leaves global edge stresses to recompute; leaves R8-5 on D1 unrerun. `vR13-4:14`; `C5_R14-1_report.md:126-211` |
| P62 | **P-W*, edge-shape tuning for the shear.** One drop-width parameter w = w*(m), shared by all light species with that edge up to O((ma)²). Needed only with a supplied zero-point vacuum | None; the edge dispersion is downstream dynamics (`AX:116-123`). The supplied vacuum is an open gate (`AX:184-187`) | C, C-box | `vR14-3:12,18`; `C5_R14-3_report.md:254` |
| P63 | **Graviton-cone edge prices.** (i) P-V: heavy edge valleys (extra band minima at about 0.7–0.94/a) plus a tuning, to reach Ξ_Eg ≥ 0; T₂g not reached. (ii) A one-mass edge-weight tuning to remove birefringence (G-U c = 6.140189; L-U c = 4.160499). (iii) P-TTV: the TT pair vertex's edge-transverse values are a law datum (neither W1 nor any two-point Ward identity fixes them). (iv) Unpaired alternatives: a per-polarization TT seagull counterterm, or a ≳ 1.5–8.7e6 ℓ_P per species (worker) | (i)–(ii): none (dynamics); (iii): source/action `AX:187`; (iv): scale reference `AX:189-190` | C-box | `vR14-3:16`; `vR13-5:11,13`; `C5_R13-5_report.md:384-388`; `C5_R14-3_report.md:255` |
| P64 | **W2 protection of the matter pole.** The standard second-order Ward identity needs exact Poincaré on the whole zone (Lemma B2 + Theorem E). Either a complete tower (Qubit fibre infinite-dimensional, R8-2 option (c)) or non-universal edge coupling (edge energy does not gravitate, R7-1's χ-cut) | Qubit `AX:47`; source/action `AX:187` | C-box | `vR13-5:7`; `C5_R13-5_report.md:389-391`. A deformed preferred-frame W2 is unpriced (R16-5) |
| P65 | **Set A, route E1 (start time).** P-r11a: a finite frame age t₀, at which every meter starts in its vacuum and h = ḣ = 0 (a temporal boundary, not a privileged site). P-r13a(R13-6): a half-retarded J₀ meter channel with memory as long as the age, no stationary locally finite state. P-r13b(R13-6): a signed zero-first-moment gain, n ≥ 4 (forced by Lemma D inside the model). Optional P-r13c(R13-6): τ_c ≲ 4–5 ps, window closing at 1.7–3.4e-9 m | Lattice `AX:40` (not breached, `vR12-4:15`); open gates `AX:185-186` (a time origin, record-production dynamics); "A law privileges no states" `AX:94` for the initial state (owner question) | A | `vR13-6:7-15,43`; `vR14-2:7,11`; `C5_R13-6_report.md:422-434`; `C5_R14-2_report.md:264-271` |
| P66 | **Set A, route E2 (leaky waves).** P-r12a′: friction on every component of harmonic-gauge h̄ (TT-only is acausal at O(γ)); the h-equation is no longer gauge invariant. P-r12b: a noiseless T = 0, outgoing-only, gravitating classical sink with frame recoil (an arrow at its boundary). P-r12c: meter memory ~2/γ (~70 t_H at 0.03 H₀). Plus either P-r14b: γ ≲ 0.016–0.047 H₀ and a history ≫ t_H (44–127 t_H), or P-r14a(R14-2): a zero-integral high-pass friction kernel (a ms frame time, frequency-dependent damping, a larger sink budget) | Admissibility `AX:57-61` (frame-tied dissipative law); Record readout `AX:82-83` (holds only because the sink is noiseless, worker reading); open gates `AX:185-186` (arrow) | A | `vR12-7:7-17`; `vR14-2:3-11`; `C5_R12-7_report.md:149-154`; `C5_R14-2_report.md:264-271` |
| P67 | **P-T readers (from R13-3, R14-5).** A global (slice-averaged) reader of ρ̄_tot (P-r13b of R13-3/R14-5); a transition clamp or regularized reader (P-r13d, still needed; R15-4 pending); a simple w ≠ −1 dark energy, since a finite Prony reader does not reconstruct CPL (P-r13f, S6). Dropped by R14-5's model: long memory (P-r13c of R13-3) and C-dust as a datum (P-r13e) | `AX:57` (range); source/action `AX:187`; `AX:94` for P-T's time-constancy (S14 Q4) | C, C-box | `vR13-3:20,53`; `vR14-5:39-44`; `C5_R13-3_report.md:276-281`; `C5_R14-5_report.md:333-341` |
| P68 | **CMC lattice time (P-r14a of R14-5).** ⟨N⟩ = 1 with one global multiplier λ(t). The lapse solves (6 + a²Q̃_i)N_i − ΣN_j = a²S(t), nearest-neighbour in form, with a global S(t): instantaneous and elliptic, Yukawa range 0.4–0.8 c/H (~1e61 spacings). Forced by Lemma C for smooth active compensation | Admissibility `AX:57` (a global time-dependent number and a simultaneous solution, not one fixed local rule); `AX:116-130` (lattice time = York time); Lattice `AX:37` via site creation | C, C-box | Lemma C refereed (`vR14-5:16-25`). Existence through collapse, causality and stability not shown (`vR14-5:64,86-88`). R15-1 pending |
| P69 | **P-arrow.** Creation c = θ ≥ 0 at every site, so H > 0 forever: no recollapse; the arrow of lattice time is the arrow of site count; lattice time freezes (N → 0) inside black holes | Record permanence `AX:80` (reading); arrow is an open gate `AX:185-186` | C, C-box | Worker (`C5_R14-5_report.md:299-303,337`). The referee notes a c = max(0, ·) clamp would give H = 0 and conflict with it (`vR14-5:42`) |
| P70 | **P-vac, the w = −1 vacuum bridge.** The vacuum enters the imposed equations as a w = −1 c-number. Under the grid zero-point (w ≥ 0, R11-3) the CMC model fails (g/H² ~ 1e122; worker K5, suggested) | Source/action `AX:187` | C, C-box | `C5_R14-5_report.md:317-320,338`. Ties W10 to W9 and to pairing (R15-1(d) pending) |
| P71 | **Graviton production, sharpened menu.** P-N1 (supplied non-compact CCR graviton) unchanged and still the only known source. P-N3″: an IR fixed point with an indefinite local quadratic form, consistent only through emergent exact constraints below a charge gap; no sign-free product-basis Euclidean form (Lemma S), no stable local Gaussian substitute (Theorem G). Non-local degree-0 symbols (flat partners). Sign-free deformations D-λ (λ_H ≤ ⅓, adds a helicity-0 partner) and D-h (z ≥ 2 or vector partners). Auxiliary irreps: R15-3 pending | P-N1: Qubit `AX:45-53`; non-local symbols: `AX:57`; P-N3″: none named (a dynamical hypothesis) | All grid sets | `vR13-2:23-25`; `vR14-4:38-40`; `C5_R13-2_report.md:171-175`; `C5_R14-4_report.md:146-153` |
| P72 | **Set C bookkeeping.** P,T-even: N_s + 7 LV conditions plus the CC. Generic proper-O: 3N_s + 8, + 2 if two degree-1 terms are not stability-protected, + 1 for k_AF | None; each is a tuning | C | `vR13-8:15-24`. Not an established one-loop count |
| P73 | **P48 refined: one light-mass e–γ tuning.** In 𝒬_lit⁻ no structural (interval) zero exists, so the split needs a tuning; the worker reads one tuning of Δ(0⁺) (one counterterm or one shape condition) as enough for every light species, leaving ≲ 1e-25 at a = ℓ_P | None (dynamics downstream, `AX:114-130`); the size uses a = ℓ_P (`AX:189-190`) | C, C-box, C-box-S | `vR13-7:28,30`; `C5_R13-7_report.md:50,211,239-240`. The "one suffices" step is not a theorem (R16-2) |

**[S17 reading] How the price structure shifted since S14.**
- **Field prices** were not cured, but the bill became itemized. Every lattice-SUSY route has a refereed per-site content and a refereed reason it does not reach the electron (P58–P60). What remains is a tuning (P73), and possibly only one.
- **Box prices** got cheaper in one place: lattice-scale causality costs nothing new for scalars (P61, even gapped edge). For Dirac matter it costs Wilson corner masses below 1/a.
- **Set A** now has two complete, comparable bills (P65, P66), with no cost metric to rank them.
- **Cosmology** has its first priced mechanism tied to a global clock (P68). Its price lands on `AX:57` and on the vacuum bridge (P70), which links back to the fixed-grid w ≥ 0 result.

---

## 4. Owner decision memo (for Jon; supersedes S14 §4; options with prices; nothing adopted)

### 4.1 The question in one line [S17 reading]

Matter on a slower-than-light grid behaves exactly as relativity says. What separates the options now is which prices you accept, and those prices can be stated precisely:
- a tuned electron–photon counterterm, or an edge shape;
- a start time or leaky gravitational waves;
- a global clock for Λ.

In every option the graviton is supplied by hand.

### 4.2 Options

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, exact equivalence principle, no LV tunings. Newtonian records-as-metric VIABLE (R6-4, instantaneous kernel, untouched by Lemma D, `vR13-6:9`).
- *Pays:* set-A axiom prices (`C5_S5_synthesis.md:94`); a supplied graviton; to go covariant, **E1 (P65) or E2 (P66)**; Λ through a q-charge (P54).
- *Open:* both exits OPEN and tied (R14-2). The spin-2 conserved-noise assembly (R15-2 pending). PPN at second order for E2.

**Option C: keep the four texts and tune.**
- *Buys:* no text changes.
- *Pays:* the bookkeeping list P72 (N_s + 7 plus the CC with P and T; up to 3N_s + 11 without them); two fixed-grid tadpoles (P51); a supplied graviton. Possibly far fewer matter-speed tunings if one light-mass tuning covers every species (P73; R16-2).
- *Open:* the actual one-loop count (R13-8 OPEN).

**Option C-box: Z³, a box-exact law, qubits in a sector.**
- *Buys:* exact relativity for number-conserving matter inside a rapidity budget, now with a subluminal whole zone (P61); exactly universal fall (d = 1), von Laue, γ, geodetic 3/2 and Schiff for bound bodies (R9-2, R11-4; both survive the subluminal edge, R14-1).
- *Pays:* S11's P26–P29, P35–P41, P45; P50, P56, P57; P61 (Wilson corner masses for Dirac); P62 (one shear shape tuning, only with a zero-point vacuum); P63 or pairing for the graviton cone; P73 (one e–γ tuning). It also pays option C's other conditions at one loop.
- *Open:* T₂g's cone shift (no zero found); the W2 needed to make GW170817 a gauge-invariant test (R16-5).

**Option C-box-S: C-box with boson–fermion pairing per cell.**
- *Buys:* the photon's one-loop shift (Theorem P); matched vacuum energy; the stipulated TT response (residual 2κm²J₂).
- *Pays:* P46 plus one of P58, P59 or P60 (each with its refereed cost), **and still P73** (no tested completion removes the electron's split).
- *Open:* τ-coupled, non-Hessian and full extended-N=4 completions; dressed or infinite-flavour momentum.

**Cosmology overlay (any grid option).**
- *V1:* the spacing grows; two tadpoles; a/ℓ_P drifts.
- *Site creation + P-T with CMC lattice time (P52, P53, P67–P70):* untuned removal of a constant vacuum in the ideal homogeneous case, by a genuine vacuum-shift symmetry. Costs a global clock, a w = −1 vacuum bridge and a forever-expanding arrow. Not shown through collapse, transitions or lumps. R15-1 and R15-4 pending.

### 4.3 Questions only Jon can answer (sharpened)

1. **E1 or E2 (set A).** Both pass every stated test and tie (R14-2). Choose which you would pay for:
   - **E1:** a beginning (records start forming at t₀; `AX:185-186` gains a time origin), a meter memory as long as the age, and a signed record filter.
   - **E2:** gravitational waves that leak into a hidden, noiseless, outgoing-only sink with an arrow, plus either a history of 44–127 Hubble times or a millisecond frame time scale.
   - The one text question that could flip the worker's count: **is a fixed initial state at t₀ a "privileged state" under `AX:94`?** R16-4 asks whether late-time observables even depend on it.
   - Or neither, which leaves set A Newtonian (R12-4).
2. **CMC lattice time (Λ).** Would you accept these four together?
   - One global number per instant, λ(t), and a lapse that every site solves simultaneously, against "one fixed nearest-neighbor admissibility rule" (`AX:57`).
   - Lattice time equal to York (mean-curvature) time.
   - An arrow that is the site count, with no recollapse ever.
   - A vacuum supplied as w = −1, which the grid's own zero-point is not (R11-3).

   If not, Λ on the grid reduces to tunings or the q-charge datum.
3. **Edge-shape tuning.** The shape of the band beyond the box is dynamics, so choosing it touches no axiom text (`AX:116-123`). Is choosing it to cancel an effect a tuning you accept? One parameter cancels the shear for all light species to O((ma)²). The graviton's E_g cone needs heavy edge valleys plus a tuning, and no edge choice has reached T₂g.
4. **One e–γ counterterm.** Nothing structural removes the electron–photon split in any tested class (§1.1). Is one tuned number acceptable: one counterterm, or one shape condition, at the ~1e-17 level (F2's 3.1e-17, `TESTS:2380`)? Be aware that "one is enough for all light particles" is a worker reading, not a theorem (R16-2 tests it).
5. **Pairing per cell (`AX:47`).** Pairing is necessary for any untuned cancellation in 𝒞_A (N*). It buys the photon, the matched vacuum and the TT response, not the electron. Every SUSY completion tried has a refereed per-site bill (P58–P60), and each still leaves P73. Is a graded cell worth that, given it does not remove the one tuning you would still pay?
6. **Carried from S14, unchanged.** Site creation (`AX:37`); a law that reads only changes in stress (`AX:94`); range (box tails, the BF 1/r term); sector selection (P45).

### 4.4 Open in every option

- **Producing the graviton.** X1, X-G and G-mix closed (a fourth, R15-3, pending); production nowhere.
- **The electron–photon split's structural zero.** None found; the proved no-go covers only the literal edge.
- **Nonlinear gravity** (R12-1 INCONCLUSIVE; off-box tail OPEN).
- **The one-loop tuning count** (R13-8 OPEN).
- **Λ beyond homogeneous idealizations.**
- **N ≥ 3 tails** (R11-6) and the **body quadrupole** (P56).
- **GW170817 as a gauge-invariant test on any grid** (no usable W2).

---

## 5. Draft round-16 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–15).**
- Probes run on Opus 5.5 at xhigh. Every FAIL, EXCLUDED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted. Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses come before titles, and excluded outside realizations are listed. Numbers from memory are labelled RECALLED.
- Every tail or decay clause names its subtraction before any run. A PRODUCED or PASS clause names the perturbative order of each exactness condition.
- **New rules (from rounds 13–14):**
  - Every lattice law used states its whole-zone v_max (R13-4).
  - Every frame-tied kernel states its leading self-force on a moving compact body (R13-6).
  - Every Ward-identity requirement names which identity (standard or deformed) it means (R13-5).

**Overlap check.**
- R15-1 covers CMC causality, stability, collapse and the vacuum it needs. R15-4 covers a regular P-T reader. R16 has no Λ item.
- R15-2 builds E1's spin-2 noise. R16-4 asks only about initial-state dependence, using R13-6's finite-start covariance, and should use R15-2's kernel if it lands first.
- R15-3 covers auxiliary irreps. R16 has no graviton-production item.

**Priority.** R16-2 and R16-1 (owner Q4; run in parallel; they share R13-7's runners), then R16-4 (owner Q1), then R16-3 (owner Q3), then R16-5 (largest; launch only if the ~12-hour window allows).

---

**R16-1. Is the electron–photon split a theorem on the edges physics would actually use? The interval no-go for Wilson edges, including the subluminal D1(r).**

- **Plain question.** R13-7 proved that the split cannot vanish over any mass range, but only for the literal edge. That edge has seven same-mass electron copies and is already excluded by the Z width (R9-1). Usable Dirac edges are Wilson edges, and R14-1's subluminal Dirac is one. On those, R13-7's control saw the split grow linearly in mass with a shape-dependent sign. Does the no-go hold where it matters?
- **Setting.**
  - Class 𝒬_W: R8-5's BQ electron with a Wilson term W even, periodic and C², including R8-5's r = 1 box and R14-1's D1(r) with r ≤ 1/√d (b = 1.4, 1.2, 1.0).
  - R13-7's photon class: t = d² even and periodic, H2′ shapes.
  - Peierls coupling, Feynman gauge, fixed λ > 0, one loop, on-shell c_e.
  - Variant 𝒬_W^P: add two complex selectrons with R13-1's gauging.
  - Excluded: λ = 0; non-Peierls vertices; two loops; N=4 content.
- **Prior art (count once).** R13-7 and verdict (`vR13-7:3-30`; Wilson control `C5_R13-7_report.md:48,144-148,202`); R8-5 (`vR8-5:7`, non-decoupling under r); R14-1 D1(r) (`C5_R14-1_report.md:184-211`); R9-1 (`TESTS:3840`); R10-1 Theorem D; R13-1 partner gauging.
- **Probes.**
  - (a) Extend Lemma A (real-analyticity for m > 0) to 𝒬_W.
  - (b) The large-m expansion. Identify the linear-in-m coefficient (worker suggestion: a zero-mean W″-moment). Prove a sign or nonvanishing on a stated subclass containing D1(r ≤ 1/√d), or show it can vanish. If it vanishes, carry on to the next coefficient.
  - (c) Numerics on D1 at b = 1.4, r = 1/√3: Δ_λ(m) for m ∈ [0.01, 3] and Δ_λ(0⁺), at three resolutions.
  - (d) Repeat (b)–(c) for 𝒬_W^P.
  - (e) Prices.
- **FIXED readings.**
  - **DERIVED:** a refereed proof that Δ_λ cannot vanish on an open mass interval in a stated Wilson class containing D1(r ≤ 1/√d) at fixed λ > 0.
  - **REFUTED:** an explicit untuned law in 𝒬_W (or 𝒬_W^P, stated) with Δ_λ ≡ 0 on an interval, checked.
  - **SUGGESTED:** otherwise.
- **Expectation.** SUGGESTED. The linear coefficient's sign already varies across shapes, so a class-wide sign is unlikely. A DERIVED subclass on D1 is possible if r ≤ 1/√d fixes the W″-moment's sign. REFUTED is not expected: isolated zeros (m ≈ 3.3 in R13-7's Wilson S1) are not interval zeros.

---

**R16-2. How many tunings put every light charged particle and the photon on one cone? (The matter-speed rows of the count.)**

- **Plain question.** R13-8's bookkeeping charges one tuning per matter species (the N_s in N_s + 7). The R13-7 worker argues the opposite: the split is analytic in mass, and physical masses are ~1e-17 to 1e-23 in Planck units, so one tuning at zero mass fixes every light species. The referee called that a plausible reading, not a theorem: it is not uniform in λ, band shape, species or counterterm structure. Charges differ, spins differ, and the photon's own shift sums over every species. So is the number of tunings 1, 2, one per spin class, or N_s?
- **Setting.**
  - One-loop QED on Z³ × ℝ with N_s charged species: charges q_i ∈ {1, 2/3, 1/3}, spins 0 and ½, masses m_i a ∈ [1e-23, 1.5e-17] (the SM charged range at a = ℓ_P, a reading on `AX:189-190`).
  - Every species on one common edge family per spin: literal and D1(r) for Dirac, G(b) for scalars. Peierls coupling.
  - Allowed tunings: edge-shape parameters, a photon-kinetic counterterm, matter-kinetic counterterms. Each one counts.
  - Excluded: non-abelian sectors, W±, two loops.
- **Prior art (count once).** R13-7 (`C5_R13-7_report.md:50,211`; `vR13-7:28`); R13-8 (`vR13-8:15-22`); R14-3's common-setting result (`vR14-3:18`, the shear analogue); R8-5's comparators (`C5_R8-5_report.md:261`, 2.66e-19); F2's 3.1e-17 (`TESTS:2380`); R10-1 Lemma N(m).
- **Probes.**
  - (a) The small-m expansion δc_i(m) = q_i²[F_s(0⁺) + F_s′·(ma) + O((ma)² ln ma)] and δc_γ = Σ_j q_j² G_s(m_j), with constants, at fixed λ > 0 and as λ → 0 (state the IR treatment).
  - (b) The minimal set of tunings that makes |c_i − c_γ| below the stated comparators for every SM charged species. Show that one fewer does not suffice in the stated class.
  - (c) Can one shape condition null F_{1/2}(0⁺) and F_0(0⁺) together, or does each spin class need its own?
  - (d) The residual after tuning, for the heaviest species (top-like m a ≈ 1.4e-17).
  - (e) Map the result onto R13-8's N_s rows.
- **FIXED readings.**
  - **COUNTED:** an explicit number n_t, with a refereed proof that n_t tunings suffice for every species in the setting, to the stated comparators, and that n_t − 1 do not, in a stated class.
  - **OPEN:** otherwise.
- **Expectation.** COUNTED with n_t independent of N_s, most likely 2 or 3: one photon-side condition plus one shape or counterterm condition per spin class. Residuals scale with (ma) and fall far below comparators except possibly for the heaviest species. A λ → 0 obstruction (IR logs) is the likeliest reason for OPEN.

---

**R16-3. The second graviton polarization: can any slower-than-light edge put T₂g on the matter cone?**

- **Plain question.** On slower-than-light edges without extra valleys, the graviton is always slower than matter (R14-3 Theorem B). With heavy valleys one polarization (E_g) can be zeroed, but the other (T₂g) stayed negative in every test. If T₂g is negative for every allowed edge, then the box route's graviton cone needs pairing or a per-polarization counterterm, and edge shaping cannot do it.
- **Setting.**
  - R14-3's separable periodic one-band class with |σ′| ≤ 1, gapped valleys allowed (outside 𝒰₀).
  - R9-9's TT vertex with its assumed Ward completion. This is prescription-scoped; state it in every claim.
  - Nonnegative nonzero transverse vertices; m ∈ {1, 0.3, 0.1}.
  - Excluded: pairing; deformed W2 (R16-5); matter's own graviton-loop shift (R11-1(b)).
- **Prior art (count once).** R14-3 and verdict (`vR14-3:14-22`; W08/W14); R14-1 (`vR14-1:13`); R13-5 (`vR13-5:9-13`; T₂g weight tuning on L-U); R11-1(b) (`vR11-1:17-19`); R9-9 Theorem T.
- **Probes.**
  - (a) Prove Ξ_T2g < 0 for every nonnegative nonzero vertex in a stated class strictly larger than 𝒰₀, including W08/W14-type gapped valleys. Or exhibit a subluminal law with Ξ_T2g ≥ 0.
  - (b) If (a) finds a zero, find one law with Ξ_Eg = Ξ_T2g = 0 at a common mass, and count the tunings, with and without P62's shear condition.
  - (c) Prices.
- **FIXED readings.**
  - **DERIVED:** a refereed proof of Ξ_T2g < 0 in a stated class containing 𝒰₀ and gapped-valley laws.
  - **REFUTED:** an explicit subluminal law with Ξ_T2g ≥ 0, checked. Report separately whether a simultaneous E_g/T₂g zero was found.
  - **SUGGESTED:** otherwise.
- **Expectation.** SUGGESTED leaning DERIVED for T₂g, because every tested shift is negative and T₂g weights mixed derivatives that the valley trick does not reach. A simultaneous zero is not expected.

---

**R16-4. Set A, E1: does anything observable remember the start? (Initial-state dependence, for `AX:94`.)**

- **Plain question.** E1's start time comes with a fixed initial state: meters in their vacuum, h = ḣ = 0. The worker's price count favours E1 unless that state counts as a "privileged state" under `AX:94` (`C5_R14-2_report.md:273`). The J₀ channel has a memory as long as the age, and Var h grows like ln T. Do late-time observables depend on the initial state, or does any reasonable start give the same universe?
- **Setting.**
  - R13-6's linearized preferred-frame E1 model with the repaired gain (P-r13b) and its finite-start covariance (`vR13-6:27-31`), with a stated bandwidth regulator for ḣ. Use R15-2's spin-2 kernel if it has been refereed.
  - Initial-state class: Gaussian meter and metric states with finite energy per mode (thermal, squeezed, displaced), up to a stated bound.
  - Observables: R11-5/R13-6's test list (lab decoherence, near-cone budget, PPN-type, double-pulsar drag, record growth) evaluated at t − t₀ ≥ t_H.
  - Excluded: E2; non-Gaussian initial states.
- **Prior art (count once).** R13-6 and verdict; R14-2 and verdict (`vR14-2:11`); R11-5; R12-4 (`vR12-4:15`, a temporal boundary is not a privileged site); Lemma S (`vR13-6:25`).
- **Probes.**
  - (a) For each listed observable, the difference between the vacuum start and the worst state in the class at t − t₀ = t_H, with constants.
  - (b) Whether an attractor exists, and its rate (J₀ tails, t^{−1/2}).
  - (c) Which quantity, if any, keeps an O(1) memory of the start at every time.
  - (d) Prices.
- **FIXED readings.**
  - **WASHED-OUT:** every listed observable at t − t₀ ≥ t_H differs between any two states in the class by less than its observational comparator, with proof, checked.
  - **STATE-DEPENDENT:** a refereed demonstration that some listed observable differs beyond its comparator between two states in the class.
  - **OPEN:** otherwise.
- **Expectation.** WASHED-OUT for every listed observable. The J₀ channel's exact memory should leave an unobservable logarithmic dependence. The owner question then becomes whether an unobservable initial datum counts as a privileged state.

---

**R16-5. GW170817 on the grid: a preferred-frame second-order Ward identity, and the graviton–matter poles under it.** *(Launch only if time allows.)*

- **Plain question.** R13-5 found that the standard second-order Ward identity cannot hold on any periodic band: the pair-creating stress drops out of H, P and K, and the lattice's boost anomaly blocks closure. So the gauge-invariant comparison of graviton and matter cones, which is what GW170817 tests, had nothing to compute in. On a grid with a preferred frame, the natural gauge group is the foliation-preserving one, as in khronometric or Hořava gravity. Is there a deformed W2 with that group that admits the pair stress? If so, what are the physical pole positions, and what does the extra scalar mode do?
- **Setting.**
  - R9-9's N-type box graviton. R8-2's stress plus R13-5's W1 pair kernel.
  - W2_pf: the second-order identity for foliation-preserving deformations (lapse a function of time only, shifts arbitrary).
  - Complex scalars and Clifford-flat fermions on G(b) and literal edges; m = 1 and 0.3; with and without P46 pairing.
  - Excluded: standard W2 (R13-5 covers it); nonlinear gravity.
- **Prior art (count once).** R13-5 and verdict (`vR13-5:7,13`); R13-8's gauge kernel (`vR13-8:11`); RN L3 (projectable Hořava strong coupling); R14-5's CMC discussion (`vR14-5:86-88`, cuscuton, Bhattacharyya et al.); RFW.
- **Probes.**
  - (a) Write W2_pf. Construct a pair stress satisfying it, or prove none exists in a stated class.
  - (b) Show that the TT and matter pole positions are W2_pf-gauge-invariant.
  - (c) Compute c_m − c_T for both polarizations, in κ_lat units and at a = ℓ_P, with and without pairing.
  - (d) The extra scalar graviton mode: its dispersion and whether it is strongly coupled.
  - (e) Prices.
- **FIXED readings.**
  - **SPLIT-PRESENT:** a nonzero W2_pf-invariant pole split for every W2_pf-complete stress in a stated class (refereed if class-wide), with numbers.
  - **SPLIT-ABSENT:** the split vanishes identically for the W2_pf-complete stress (pairing stated), with the reason, checked.
  - **OPEN:** otherwise, including no W2_pf-complete stress constructed.
- **Expectation.** A W2_pf-complete stress exists, since boosts are no longer gauge. SPLIT-PRESENT without pairing, at the edge-anomaly size. SPLIT-ABSENT for TT with matched pairing (residual 2κm²J₂). The likeliest failure is a strongly coupled extra scalar, as in projectable Hořava.

---

### 5.1 What the final wrap-up (10:20Z) should contain (proposal)

1. **A plain-words SUMMARY §26** (rounds 13–16), in the style of §25, with refereed status per line.
2. **The final wall map** (§2 format): each wall with its refereed statement and class, DERIVED or OPEN, cheapest named price, and the axiom line touched.
3. **The consolidated price ledger P1–P7x** under unique S-numbers. Resolve the worker-label collisions (P-r13a/b/c, P-r14a). Mark every price as named, never adopted.
4. **The final owner memo**: options, their bills, Jon's questions (from §4.3, updated by R15/R16), and "open in every option".
5. **The theorem list**: every DERIVED or bounded EXCLUDED result of C5, with exact class, referee file:line and date. This is the campaign's durable output.
6. **The dated-corrections table** (§1.8 plus any from R15/R16), so downstream text does not cite the superseded forms (R11-5's literal kernel, the ¼ prefactor, the Lemma V paraphrase, R9-2's t*, R11-1(b)'s "at most one cone").
7. **Pending at close**: every item with no referee verdict, with its worker reading labelled as such.
8. **Calibration**: synthesis expectations against outcomes across S5–S17, as a check on the drafting.
9. **Provenance**: all workers and syntheses are Opus 5.5 (same family); every verdict is codex gpt-5.6-sol (xhigh); list any finding that never reached a referee.
10. **What would change the picture**: the specific results that would move an option (for example, an untuned interval zero on a Wilson edge, a produced linear TT branch, a VIABLE CMC model under R15-1/R15-4, an E1/E2 cost metric).
11. **Handoff**: per `pr-or-delete`, the keepers to land by PR (packet files, runners worth keeping) and what to delete. No repository edits in the wrap-up without the owner.

---

## 6. Caveats

- **Same family, unrefereed.** The wall map's DERIVED/OPEN column and "cheapest price" column, the P58–P73 numbering, every "[S17 reading]", the owner questions and the R16 drafts are S17's.
- **Pending.** R15-3's Theorem C is a worker claim. R15-1, R15-2 and R15-4 have no reports. If R15-1 finds signalling or a ghost, W10 and owner Q2 change. If R15-2 finds conserved spin-2 noise impossible with the repaired gain, E1 changes and owner Q1 changes.
- **Bounded, not class-wide.** R13-7 covers 𝒬_lit⁻ only (and is the R9-1-excluded edge, an S17 reading); R13-1 covers the one-body band-scalar class; R12-6 covers 𝒦₀; R13-4(i) covers 𝓔; R13-2 and R14-4 cover six-pair PSD Gaussians; R14-3's Theorem B covers 𝒰₀; Lemma D covers the frame-tied E1 model; Lemma F covers smooth N = 1 continua; Lemma C covers the stated E_μν form. **No refereed result says the split, the graviton or Λ is impossible in general.**
- **Prescription scope.** Ξ statements use R9-9's vertex and an assumed Ward completion. R13-5's floors are W1-only class 𝒲_V.
- **Scale bridge.** Every Planck-unit number (m a, a ≳ 1e6 ℓ_P floors, 1e61 spacings, residuals ≲ 1e-25) uses a = ℓ_P, which the axioms leave open (`AX:189-190`).
- **The sets are not exhaustive.** Relational and non-commutative constructions remain unexamined.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items.
