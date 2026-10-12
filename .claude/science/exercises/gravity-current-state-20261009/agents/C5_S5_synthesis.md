# C5 S5: mid-campaign synthesis (rounds 1–4 refereed; round 5 pending)

**Author.** Claude Opus 5.5 (S5), the same model family as every C5 worker and the supervisor. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict as recorded in `TESTS.md`. Written 2026-10-12, 14:05Z to about 14:55Z. No repository file was edited.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:2302-2966` (Campaign C5 through the R5-4/S5 pre-registration); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–22 (`:334-567`); `PRICE_NOTE.md` §5–§6 and the v6 delta (`:156-210`, `:251-413`); the referee verdicts `C5_R2-1_referee_verdict.md`, `C5_R2-2_referee.md`, `C5_R2-3_referee.md`, `C5_R2-4_referee.md`, `C5_R2-5_referee.md`, `C5_R2-6_referee.md`, `C5_R3-1_referee_verdict.md`, `C5_R3-2_referee_verdict.md`, `C5_R3-4_referee_verdict.md`, `C5_R4-{1..5}_referee_verdict.md`; `C5_O1_referee.md:1-40`. **Read in part:** `scratchpad/C5/R5-1/R5-1_report.md` §0 (pending; used only as "pending"); `TESTS.md:714-767` (lane R), `:1023-1080` (lane RG), `:1434-1442` (F2 referee); `OUTSIDE_VIEW.md:39`; `B_referee.md:47`.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `PRICE_NOTE` are in `P/`; bare `C5_*`, `C4_*`, `B_referee.md` are in `P/agents/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.**
- **[ref]** a referee-confirmed statement, with the referee's scope.
- **[ref, bounded: …]** a refereed FAIL or no-go, with its class.
- **[worker]** a worker statement the referee did not rule on (no FAIL claimed, so no referee was required).
- **[pending]** an unrefereed round-5 item.
- **[S5 reading]** an interpretation made here; same family; unrefereed.

**Sets.** A = continuum base, discreteness only in records. B = Euclidean Z⁴, whole law hypercubic, arrow in the state. B′ = the Lorentz-random lattice (LRL): X = g(L₇ + u), g Haar-random, L₇ = diag(√7,1,1,1)ℤ⁴. C = keep the axioms' Z³ and tune. (Definitions: `TESTS:2424-2428`, `:2647-2651`.)

---

## 0. In plain words

**What the observations do to the rules, after four refereed rounds.**

- **Matter's single light speed** does not force exact Lorentz symmetry. A hypercubic 4D grid protects it for ordinary matter, and so does a Lorentz-random grid. The axioms' own 3D grid with separate time does not: each speed difference must be tuned.
- **A universal massless graviton** needs momentum that adds up exactly. Every construction found so far that gives exact momentum on a discrete substrate does so by smuggling in the continuum: a full tower of bands per cell, or a continuum mass shell folded onto the grid. On Z⁴ this is now a bounded theorem for one-particle states. On the Lorentz-random grid it is a bounded theorem for one class of particles, and the only working example imports the continuum.
- **The vacuum's weight (Λ).** Nothing in any set makes the mean zero; it is a premise everywhere. The size of the observed value comes out right only if events in our past are counted like a Poisson process at Planck density. Poisson events are excluded by lensing. The Lorentz-random grid passes lensing, but its counts look sub-Poisson so far.
- **Records** must be rare, coarse and jointly (not site-by-site) random. If they jump the matter stress, Einstein's equations need a compensator or a preferred slicing. At the rates interference allows, they are gravitationally inert.

**Where each set stands.**
- **A** passes every observation used, by symmetry, but only because the graviton is put in by hand. Its discreteness does nothing for gravity.
- **B** (Euclidean Z⁴) is close to exhausted:
  - exact gravity with finite particles is impossible in a bounded class;
  - a positive local weight bends light by only half GR's amount;
  - in its classical class, records can form only at a boundary.
- **B′** (Lorentz-random grid) is the best kinematic substrate found: Lorentz-clean where it has been checked, and silent to light below a gap. But nobody has put a working law of motion on one copy.
  - Laws on finitely many orbits scatter from copy to copy.
  - The representative kernel is unstable.
  - Particles on single sites carry no momentum.
  - The one particle that works is the continuum, supplied as data.
- **C** passes everything by tuning: speeds, two shear masses, Λ, and (suggested) two CPT-odd terms the axioms' proper-only rotations allow.

**The one-line picture [S5 reading].** Every route to exact gravity so far ends in one of two places: the continuum (set A, whatever the coordinates) or a tuning (set C, or B/B′ with 11 or 5 tunings). Round 5 is testing whether B′ is a third place. Round 6 (§5) asks the class-wide version of that question, whether any set can produce rather than supply the graviton, whether Λ's size can live anywhere lensing allows, and what C's full price is.

---

## 1. What observations now force on the rules, set by set

Each entry gives the statement, the label and source, and the scope. "Forced" means forced under the stated hypotheses, never class-wide unless said.

### 1.0 Shared by every set

1. **One light cone → a symmetry condition or a tuning.**
   - If the law's point group has no invariant traceless rank-2 tensor (V₂^tl = 0), dimension-4 speed operators are forbidden, and that implies V₁ = 0 [ref; `TESTS:2378`].
   - The invariant counts (V, S2):
     - the axioms' proper cubic group: (1, 2);
     - B4⁺ and W(B4): (0, 1) [ref; `TESTS:2379`].
   - *Scope.* The condition is sufficient, not necessary. "Only Lorentz-in-law substrates avoid tuning" is refuted for dimension-4 matter only (`TESTS:2381-2384`; `C5_O1_referee.md:3`).
2. **A universal spin-2 → an additive asymptotic charge.**
   - The soft residue is an additive collision invariant, conditional on the exact Ward-residue identity [ref CWC; `TESTS:2386-2389`].
   - Exact geometric continuous translations are incompatible with each of the following [ref, bounded; `TESTS:2391-2395`]:
     - finite fibres tied uniformly to sites (Lemma S);
     - a strictly local continuous interpolation of the qubit-chain shift (Lemma G; 1D and finite cylinders only);
     - finite-dimensional region algebras in a positive-energy net (Reeh–Schlieder).
   - Open: non-geometric or asymptotic translations, quasi-local actions, infinite-transverse many-body systems (`TESTS:2396`).
3. **Free fall.**
   - A band-bottom wavepacket falls as −β_B∇Φ [ref; `TESTS:2391`].
   - MICROSCOPE constrains only differences in effective β.
   - A grid's tree-level momentum defect (about 2e-41) cannot force exactness [ref; `TESTS:2390`].
4. **Vacuum.**
   - For finitely many free species, untuned cancellation on an open mass interval forces equal signed density-of-states measures [ref; `TESTS:2400`].
   - A qubit site cannot hold independent exact CCR and CAR modes [ref, bounded: on-site/free; `TESTS:2402`].
   - FS M1 lattice SUSY is a genuine but costly escape, with no E_g bridge [ref; `TESTS:2403`].
5. **Records.**
   - V ≤ BC for a permanent, distinguishable branch-information record [ref; `TESTS:2408`].
   - At most 5.3e-11 s⁻¹ per nucleon at 0.1 µm (Earth heat) [ref; `TESTS:2410`].
   - Bell data exclude independently factorized joint record laws [ref; `TESTS:2411`]. Admissibility's per-site distribution is therefore a marginal (`C5_O5_synthesis.md:304`).
   - "Records copy, never measure" is sufficient, not necessary [ref; `TESTS:2411-2412`].
6. **Discreteness in a Lorentz-invariant world** [ref; `TESTS:2711-2712`]:
   - N-Q′: covariant nonnegative integer counts in a positive-energy vacuum, with the stated hypotheses, annihilate the vacuum;
   - P-L′: every stationary integer-valued random measure of positive intensity has spacelike weight in every cone about every hyperplane.
   - *Scope.* Neither places that weight in a given band (`C5_R2-2_referee.md:7,24`).
   - [S5 reading] Lorentz-invariant discreteness is classical, with spacelike spectral weight somewhere, or lives in records. It is not a vacuum count.
7. **Deformed momentum (set D) is closed in one class.**
   - The canonical Snyder total does not factor through an additive charge, so the soft spin-2 coupling vanishes [ref, bounded: canonical transvection product, standard unitary S-matrix, leg-local soft poles; `TESTS:2741-2744`; `C5_R2-6_referee.md:17`].
8. **Λ's size.**
   - The observed order follows only under three premises [ref; `TESTS:2939`]:
     - unimodular conjugacy;
     - a count–volume bridge;
     - a Poisson-like 4D count at Planck density.
   - Neither the coefficient nor the zero mean is derived.

### 1.1 Set A (continuum + records)

**Plain.** A meets the light-cone, free-fall and universality observations by its symmetry. It pays for that in every axiom text: Lattice becomes Minkowski points, and bounded-region algebras become infinite-dimensional (`C5_O5_synthesis.md:324-329`, unrefereed set construction).

**What the observations force on A's records.**
- A spatially decaying stress jump on one non-compact collapse surface gives a non-integrable non-conservation current. Neither semiclassical Einstein gravity nor its unimodular form then has a global solution without a compensator or a metric-reset rule [ref; `TESTS:2722`; `C5_R2-3_referee.md:23`].
  - *Scope:* one surface, decaying jump, the global distributional Einstein reading.
- Isolated pointer flashes are limited to about 20 s⁻¹ by Earth heat; environmental amplification can exceed 10³ s⁻¹. GW signals are negligible by 4–80 decades [ref; `TESTS:2723-2724`; `C5_R2-3_referee.md:11`].
  - Bounded FAIL for bare, independently flashing position laws (`TESTS:2725`).
  - Open: non-local dressed operations, collective or coloured laws, other compensators (`TESTS:2726`).
- Bare localized beable stress cannot source linearized Einstein or trace-free gravity when Bohmian momentum changes. Adding the realized quantum-potential energy does not restore run-wise conservation for generic states [ref; `TESTS:2931-2932`].
- The surviving gravity–record couplings:
  - fixed-foliation equilibrium beables (E3), VIABLE only in explicit preferred-foliation scope [ref; `TESTS:2777`];
  - "R": gravity stays quantum and the beable metric is inert, viable outside beable-sourced gravity [ref; `TESTS:2936`];
  - DGNSZ gives a covariant foliation only for timelike total momentum, not for the vacuum or null states [ref; `TESTS:2936`].
- Excluded or open:
  - ultra-local continuous Newtonian CQ is EXCLUDED by a 32-decade empty window; covariant CQ-GR is OPEN [ref; `TESTS:2776`];
  - JKMS metric jumps (E1), dressed Kraus operators (E4) and reservoirs (E5) are OPEN [ref; `TESTS:2775-2779`].
- **Λ fluctuation:** matter-following GRW flashes give about 3.3e-72 Λ_obs [ref; `TESTS:2940`]. This is not a class-wide bound.

**[S5 reading].**
- In A the records either do no gravitational work (inert at allowed rates) or need a new structure: a compensator, a reset rule, or a foliation.
- The graviton is supplied (A5, `C5_O5_synthesis.md:328`).
- A is also where every discrete exact-gravity construction lands (§1.3, §1.2): B → A at one-particle level (R2-1); B′'s only charge-carrying examples are the continuum hyperboloid (R4-2 Example E; R5-1 Example D, pending).

### 1.2 Set B (Euclidean Z⁴, ξ = 1, whole law B4⁺/W(B4))

**Plain.** B protects matter's light cone for dimension-4 operators. It fails or stalls everywhere gravity enters.

- **One cone.**
  - Dimension 4 is protected [ref; `TESTS:2379`]; ξ = 1 removes F2's QED split [ref; `SUMMARY:424`].
  - Dimension 5 is forbidden, and dimension 6 is 7.76 decades inside LHAASO's bound (`C5_O5_synthesis.md:132`, from the O1 referee).
- **Exact graviton with finite particles: dead (bounded).**
  - Hypotheses: a quasi-local Z⁴ law; an unbroken additive asymptotic charge on an interacting simple scalar band; nondegenerate analytic dispersion, d ≥ 2; globally periodic real-analytic finite one-particle charge and Hamiltonian matrices, or W(B4) parity.
  - Under these, the constant-ξ Ward identity forces a finite matrix to have infinitely many roots. So the one-particle fibre cannot be finite [ref, bounded: one-particle/spectral; `TESTS:2748-2751`; `C5_R2-1_referee_verdict.md:11`].
  - *Scope:* not a theorem that the site ontology must be a continuum. Finite fields per site do not imply a finite one-particle fibre (`C5_R2-1_referee_verdict.md:9`).
  - The perfect-action Gaussian time-blocked covariance fails OS reflection positivity, so its poles are Euclidean, not physical (`TESTS:2752`).
- **Graviton by tuning.**
  - 11 = 3 + 8 is the gauge-restoration codimension [ref; `SUMMARY:418`].
  - Lack of protection does not prove all eleven are generated (`C5_R2-1_referee_verdict.md:9`).
  - K2 fails Killing closure at O(κ²) [ref, bounded; `SUMMARY:406`].
- **Weight.**
  - Assumptions: a positive source-tilted measure; a real finite-range or exponentially local source functional; an isotropic unscreened 1/p² response.
  - Under these, the trace projector forces a ≤ 1/3, i.e. γ ≤ 1/2. GR needs γ = 1 (Cassini). So linear GR cannot arise from such a positive local Gibbs realization [ref, DERIVED under W1–W3; `TESTS:2729-2731`; `C5_R2-4_referee.md:81`].
  - Escapes: non-real or non-local source bridges.
  - No class-wide chiral no-go exists (`TESTS:2732-2735`).
- **Records.**
  - Class: classical nonnegative nearest-neighbour slice transfer laws with a reflection-positive twisted kernel and a θ-equivariant record map.
  - In that class, strict permanence forbids every bulk formation step; only boundary-only formation survives [ref; `TESTS:2738`; `C5_R2-5_referee.md:76`].
  - Outside the class: time-odd tagged non-RP laws (P2), probabilistic permanence, quantum slices, OS-reconstructed records (`TESTS:2739`; `C5_R2-5_referee.md:11,35-37`).
- **Arrow.** A finite group that keeps a proper convex time cone has V₁ ≠ 0 (Lemma E) [ref; `C5_O1_referee.md:21`]. So B's arrow must sit in the state.
- **Λ count.** A crystal's count variance depends on the frame [ref; `TESTS:2942`].

**[S5 reading].** B survives only by paying all of these together:
- 11 tunings (or the continuum);
- a weight that is not a positive local probability, or a non-real/non-local bridge;
- record formation outside the classical RP class.

### 1.3 Set B′ (Lorentz-random lattice)

**Plain.** B′ is good kinematics with no dynamics yet.

- **Kinematics (refereed positives).**
  - Poincaré-invariant in law, with a uniform hard core (`TESTS:2713-2718`).
  - No Bragg support for 0 < |q²| < (2π)²/7, or on the nonzero null cone.
  - Ideal 1→1 Bloch silence below the gap [ref; `TESTS:2713-2718`; `C5_R2-2_referee.md:11-18`].
  - A realization has no conventional rest frame, but it breaks continuous Lorentz symmetry to Γ_L (`C5_R2-2_referee.md:20`).
- **Momentum.** Conserved only modulo the reciprocal lattice. Multiparticle umklapp can use low individual momenta, so in-band momentum conservation is not exact [ref; `TESTS:2791`].
- **Per-realization Lorentz violation (LV).**
  - Lemma Z: every Γ_L orbit on the punctured null cone is dense in direction and scale. Regular null/spacelike scalar dispersion is therefore Lorentz-invariant per realization [ref; `TESTS:2925`].
  - Open: bounded timelike (mass-like) branches and singular Bragg-cone sectors.
  - At a = ℓ_P, every listed process is 27.2–44.2 decades below the gap [ref; `TESTS:2924`].
- **What a law can be.**
  - Lemma M: invariant L² scalar torus symbols are constant, so nonzero invariant hopping kernels are non-summable and do not decay along their infinite orbits [ref; `TESTS:2785`].
  - Prop. P: the convergent Poincaré series is an orbit weight, not a hopping operator. "Power-law quasi-locality" is refuted [ref; `TESTS:2786`].
  - Prop. R: a nonzero past-timelike, polynomially bounded kernel converges exactly in the forward tube. Retardation supplies an arrow without a rest-frame vector, and Lemma E does not apply [ref; `TESTS:2787`; `C5_R3-1_referee_verdict.md:9`].
- **Per-realization effective law: dead for finite orbits (bounded).**
  - Four-shell retarded weights exist with Haar mean −k² + O(a²k⁴ log ak) [ref; `TESTS:2905`].
  - But every fixed linear retarded scalar kernel on finitely many Γ_L orbits, with a nonzero off-site weight, has a per-realization deviation that does not vanish relative to □φ [ref, bounded: finite-orbit, linear, ensemble-rms; `TESTS:2906-2907`].
  - The representative five-shell kernel has a robust forward-tube zero, i.e. a growing mode that e-folds in about 2 lattice times [ref; `TESTS:2927`].
- **Particles.**
  - Conservative class: a unitary Γ⋉L₇ representation with finite multiplicity, a closed rational charge multiplet, and support conservative for the coordinate boosts. Every Lorentz component of every finite-fibre charge then vanishes [ref, bounded; `TESTS:2915`].
  - Strictly on-site bounded operators acting on an invariant vacuum stay in that class: no continuous dispersive branch (`TESTS:2916`).
  - The only charge-carrying example is the dissipative folded continuum hyperboloid, with no lattice law (`TESTS:2917`; `C5_R4-2_referee_verdict.md:13`).
- **Graviton.** Given a Γ-covariant quadratic action with a symmetry-preserving expansion through q² [ref; `TESTS:2758-2763`]:
  - the codimension falls from 11 to 5;
  - the E/T2 split disappears, leaving one tuned spin-2 mass;
  - a tuned TT pole sits on the background cone;
  - the scalar sector needs b = −2a, one more matching condition.
  - Theorem T_Γ: a nonzero four-vector gauge charge cannot be bounded under a unitary Γ action; this does not force a tower (`TESTS:2761`).
- **Λ fluctuation.** Sub-volume-like through T = 108; the asymptotic law is open (Lemma V) [ref; `TESTS:2943`]. A volume term with F ~ 1e-4–1e-3 is not excluded (`C5_R4-5_referee_verdict.md:13`).
- **Worker, unrefereed (R3-3; `TESTS:2765-2773`).**
  - The mean link kernel is massless-retarded at long range.
  - Benincasa–Dowker (BD) weights fail on LRL.
  - A single realization deviates from the mean by 30–40% of Poisson scatter.
  - Exact de Sitter/AdS LRL needs ℤ[√2].
  - Curvature-defect disorder sits ≥ 30 decades below RZ's bar (suggested).
- **Pending.**
  - **R5-1** (worker FAIL bounded in four classes, unrefereed): clusters with infinite stabilizers create no particle. A continuous covariant event rule cannot vary with its neighbours. Commuting records give time-symmetric spectra. Example D reproduces the continuum.
  - **R5-2:** infinite-orbit kernels.
  - **R5-4:** timelike-link laws.

**[S5 reading].**
- B′ is the only set where the discreteness is physical, Lorentz-clean where checked, and silent to light.
- It is also where Admissibility's nearest-neighbour rule cannot survive in any form tried: invariant couplings are infinite-orbit and non-summable.

### 1.4 Set C (axioms' Z³, tuned)

**Plain.** C keeps the four texts and tunes every observation in.

- **Speeds.**
  - N − 1 relative directions. One refereed instance needs about 3.1e-17, and it is regulator-specific [ref; `TESTS:2380`; `C5_O1_referee.md:34`].
  - The lattice is a preferred-frame theory [ref, bounded; `SUMMARY:394`; `PRICE_NOTE:405-408`].
- **Graviton.**
  - 2 TT tunings, each to 5.7e-99 (`PRICE_NOTE:162`).
  - Free local matter alone produces the E_g natural size [ref; `SUMMARY:426-428`].
  - No principle removes it: RV4 bounded FAIL (`SUMMARY:510-516`); RP needs exactly matched spectra (`SUMMARY:393`); RFW bounded FAIL (`SUMMARY:520-527`).
  - A Z³ × ℝ total of at least 6 tunings is a reading, not refereed (`SUMMARY:435`).
- **Dimension-3 CPT-odd terms.** b₀ and (k_AF)₀ are allowed by proper-only rotations; only the chosen action's parity forbids them [ref; `TESTS:1440`]. Their natural size against the CMB bound is SUGGESTED only (`C5_O1_report.md:242-245`).
- **Λ count.** Permanence plus one record per Z³ site caps distinct record events at 8.24e184 in the stated embedding [ref; `TESTS:2941`; `C5_R4-5_referee_verdict.md:9`]. The count variance is frame-dependent (`TESTS:2942`).
- **Emergent graviton on Z³.** The exact-constraint weak VS (N-type) theory is the one live construction. Nothing derives its coupling to matter's energy-momentum [ref; lane R, `TESTS:767`].

**[S5 reading].** C cannot be excluded by calculation. Its price is the count and the size of the tunings, and that count is not final (§3, §5 R6-5).

---

## 2. Table: forced / dead (bounded, with class) / open

**Legend.**
- **F** = forced or met, under stated hypotheses.
- **D(b)** = dead, bounded to the named class.
- **O** = open.
- **P** = premise, i.e. supplied by hand.
- **pend** = round-5 item running.

| Item | A: continuum + records | B: Euclidean Z⁴ | B′: LRL | C: Z³ + tune |
|---|---|---|---|---|
| **One light cone** | F by exact Poincaré; the necessity is not derived (`TESTS:2381-2384`) | F at dimension 4 by W(B4) (`TESTS:2379`); dimension 5 forbidden; dimension 6 7.76 decades inside (`C5_O5_synthesis.md:132`) | F for regular null/spacelike scalar branches per realization (Lemma Z, `TESTS:2925`). O: timelike mass-like and singular Bragg sectors | P: N−1 tunings; one refereed instance at 3.1e-17, regulator-specific (`TESTS:2380`) |
| **Graviton: exact gauge identity** | P: supplied primitive A5 (`C5_O5_synthesis.md:328`); not produced | D(b): finite one-particle fibre, interacting simple band, analytic periodic matrices (`TESTS:2748-2751`). D(b): K2 κ² closure, regular NN (`SUMMARY:406`) | D(b): conservative finite-fibre Γ⋉L₇ representations (`TESTS:2915`). O: dissipative sectors (only known example = continuum, `TESTS:2917`); pend: R5-1, R5-4 | D(b) for every principle tried: RV4, RP, RFW, RB (`SUMMARY:393-394,510-527`). O: exact-constraint N-type coupling (`TESTS:767`) |
| **Graviton: tuning count** | 0, beyond Λ (graviton supplied) | 11 by codimension, not all shown generated (`SUMMARY:418`; `C5_R2-1_referee_verdict.md:9`) | 5, conditional on a Γ-covariant quadratic action; + scalar b = −2a (`TESTS:2758-2763`) | 2 TT at 5.7e-99 + speeds; ≥ 6 total is a reading (`SUMMARY:435`) |
| **Equivalence (free fall)** | F (exact) | Follows from dimension-4 protection (SUGGESTED, `C5_O5_synthesis.md:186`) | O: follows only if a per-realization law exists | Tuned through the speeds; tree-level defect 2e-41 (`TESTS:2390`) |
| **Vacuum energy, mean (Λ, E_g)** | P: Λ (unimodular constant or tuned). E_g forbidden by the Ward identity, SUGGESTED (`C5_O5_synthesis.md:335`) | P: Λ + separate tadpole tuning (`SUMMARY:418`) | P: Λ; one shear tuning (`TESTS:2759`) | P: Λ to 1e-123; E_g tuned (`SUMMARY:426-428`) |
| **— shared mean results** | Zero mean derived nowhere (`TESTS:2939`). Free class needs equal signed DOS (`TESTS:2400`). Qubit CCR+CAR D(b) (`TESTS:2402`). FS SUSY O (`TESTS:2403`). pend: R5-3 | ← | ← | ← |
| **Λ fluctuation (everpresent)** | D(b) for matter-following GRW flashes: ~3.3e-72 Λ_obs, not class-wide (`TESTS:2940`) | Frame-dependent crystal variance (`TESTS:2942`); no Lorentzian count | O: sub-volume through T = 108; Lemma V open; F ~ 1e-4–1e-3 not excluded (`TESTS:2943`; `C5_R4-5_referee_verdict.md:13`) | Count capped at 8.24e184 (`TESTS:2941`); frame-dependent (`TESTS:2942`) |
| **Records & interference** | F: rare, coarse, non-factorizing (`TESTS:2408-2412`). Pointer ≤ ~20 s⁻¹ by Earth heat (`TESTS:2723`). D(b): bare independent position flashes (`TESTS:2725`). Gravity coupling: compensator, foliation (E3 VIABLE) or inert metric (R) (`TESTS:2722,2777,2936`) | D(b): bulk formation under strict permanence in the classical RP NN class (`TESTS:2738`). O: tagged non-RP, probabilistic, quantum slices (`TESTS:2739`) | F (positive): retarded law with an arrow and no rest frame (`TESTS:2787`). pend: R5-1 (commuting records → time-symmetric spectra) | Shared budget only; the arrow may be in the law (`C5_O5_synthesis.md:420`) |
| **Lensing noise** | Passes if records steer nothing, SUGGESTED (`C5_O5_synthesis.md:416`); flashes inert (`C5_R2-3_referee.md:11`) | Passes: one crystal | F for ideal 1→1 below the gap (`TESTS:2718`). O: multiparticle umklapp (`TESTS:2791`), finite sources, curvature (`TESTS:2719`). Worker: 30–40% smooth anisotropy (`TESTS:2768`) | Passes: one crystal |
| **Per-realization effective law** | n/a (continuum QFT) | Exists (one crystal), but its weight fails γ for GR (`TESTS:2729-2731`) | D(b): finite-orbit linear retarded scalar kernels (`TESTS:2906`). Representative kernel unstable (`TESTS:2927`). Mean exists (`TESTS:2905`). pend: R5-2 | Exists; preferred frame (`SUMMARY:394`) |

**For comparison (routes closed since v6).**
- Poisson events: lensing FAIL (bounded) (`SUMMARY:502`).
- Plain coherent superposition of events: FAIL for fixed Poisson weights (`TESTS:2416`).
- Snyder (set D): FAIL (bounded) (`TESTS:2741-2744`).

---

## 3. Price ledger delta since PRICE_NOTE v6 (named, none adopted)

The v6 delta ends at P14 (`PRICE_NOTE:364-368`). The round-1 set prices A1–A6, B1–B6 and C1–C3 are named in `C5_O5_synthesis.md:322-387`. They are unrefereed as a set construction, but each cites refereed parts; they are carried here, not repeated. The new prices from rounds 2–4 follow. Axiom lines: Lattice `AX:37-41`; Qubit `AX:45-53`; Admissibility `AX:57-61` (reading notes `:63-73`); Record `AX:77-83`.

| # | Price (named only) | Text touched | Set | What the refereed record says it buys or costs |
|---|---|---|---|---|
| P15 | **An exact Z⁴ Ward identity requires an infinite one-particle fibre**: P10 extended to Z⁴ and to an interacting simple band | Qubit `AX:47`, one-particle reading only | B | Bounded one-particle/spectral; not a site-ontology theorem (`TESTS:2748-2751`; `C5_R2-1_referee_verdict.md:11`). Reading "B → A in lattice coordinates" |
| P16 | **The Lorentz-random lattice**: Lattice's Z³ becomes a Haar-random Poincaré frame of the cocompact arithmetic L₇; covariance becomes Γ_L ⋉ L₇ per realization, Poincaré in law | Lattice `AX:37-41`; Admissibility covariance `AX:57-58` | B′ | Poincaré in law, hard core, Bragg gap, 1→1 silence (`TESTS:2713-2718`). Not a viable event route by itself (`TESTS:2719`) |
| P17 | **A retarded, infinite-orbit law in place of "one fixed nearest-neighbor rule"**: invariant kernels are non-summable and constant on infinite orbits; ordinary symbols exist only in the forward tube | Admissibility `AX:57` ("nearest-neighbor") | B′ | It buys an arrow in the law with no rest-frame vector (`TESTS:2785-2787`). Finite-orbit linear versions give no per-realization law (`TESTS:2906`); the representative kernel is unstable (`TESTS:2927`) |
| P18 | **LRL particles cannot live on the Qubit fibre**: matter must be multi-site or dissipative; the only charge-carrying sector known is the folded continuum hyperboloid | Qubit `AX:47` (and Admissibility, if a law must generate it) | B′ | Conservative finite-fibre charge vanishes (`TESTS:2915-2916`). Example E: charge but no lattice law (`TESTS:2917`). Pending R5-1 (Example D, continuum) |
| P19 | **LRL graviton tunings**: 5 (2 mass + 4 kinetic forms, 1 gauge-invariant combination), plus b = −2a in the scalar sector | none (tuning) | B′ | Conditional on a Γ-covariant quadratic action with a symmetry-preserving expansion (`TESTS:2758-2763`) |
| P20 | **B's weight is not a positive local probability for GR**: give up positivity of the sourced weight, or make the metric–source bridge non-real or non-local | Admissibility `AX:60-61` ("probability distribution") | B | DERIVED under W1–W3: γ ≤ 1/2 otherwise (`TESTS:2729-2731`; `C5_R2-4_referee.md:77`) |
| P21 | **B's records**: in the classical RP class formation is boundary-only. Otherwise a time-odd tagged non-RP law, probabilistic permanence, or quantum slices | Record `AX:77-80` ("Records form", "permanent") | B | `TESTS:2738-2739`; P2 is the tagged escape, not RP (`C5_R2-5_referee.md:35-37`) |
| P22 | **Set A's gravity–record coupling**, one of: (a) a compensator or metric-reset rule for stress jumps; (b) a preferred foliation in the guidance law (E3); (c) gravity quantum, with the record/beable metric inert (R) | none directly (extends primitive A5); (b) adds a frame to the guidance law | A | (a) `TESTS:2722`; (b) VIABLE in fixed-foliation scope (`TESTS:2777`); (c) viable outside beable-sourced gravity (`TESTS:2936`). Literal beable sourcing (C0), naive CQ and ultra-local Newtonian CQ are closed (`TESTS:2776,2931-2932`) |
| P23 | **Everpresent Λ's three premises**: unimodular conjugacy, a count–volume bridge, and a Poisson-like 4D count at Planck density. On the axioms' Z³, a growing 4D count also needs a Lattice change | Lattice `AX:37`; Record `AX:79-80` (one per site, permanent) for the count cap; a gravity bridge (none in the axioms) | any | Gives 1.389 Λ_obs for the past cone (range 0.695–34.9); the zero mean is not derived (`TESTS:2939,2941`; `C5_R4-5_referee_verdict.md:5,9`) |

**Routes closed in this interval (no price; recorded as bounded deaths).**
- Snyder set D (`TESTS:2741-2744`).
- Finite-fibre exact identity on Z⁴ (`TESTS:2748-2751`).
- Gaussian time-blocked perfect action as physical states (`TESTS:2752`).
- Bare independent flash laws (`TESTS:2725`).
- Ultra-local Newtonian CQ (`TESTS:2776`).
- Literal C0 beable sourcing and naive CQ (`TESTS:2931-2932`).
- LRL finite-orbit linear kernels (`TESTS:2906`).
- LRL conservative finite fibres (`TESTS:2915`).

**Pending price [pending, R5-1 worker].** On LRL, a covariant event rule that depends continuously on its neighbours cannot depend on them at all. If refereed, Admissibility's "varies with the nearest-neighbor conditions" (`AX:61`) survives on LRL only through dependence on the far tails of the infinite neighbour families.

**[S5 reading] on how the price structure has shifted.**
- A pays in every text, plus a primitive graviton, plus P22.
- B pays Lattice, Admissibility and Record, plus P15/P20/P21, plus 11 tunings or the continuum.
- B′ pays Lattice, Admissibility and Qubit (P16–P18), plus 5 tunings (P19), and still has no law.
- C pays tunings only: ≥ 6 (a reading), plus Λ, plus the suggested dimension-3 CPT-odd pair.

---

## 4. Big open problems, ranked by leverage on the A / B′ / C decision

**What "leverage" means here.** How far a definite answer would move the choice, with hard problems treated as first-class rather than down-ranked. B is listed under B′ and C where it shares their questions; on its own it is close to exhausted (§1.2).

1. **Can one LRL copy carry a law of motion with real particles, without supplying the continuum?**
   - *Decides:* whether B′ is a genuine third option or collapses to "A in lattice coordinates", as B did (R2-1).
   - *State:*
     - finite-orbit linear kernels D(b) (R4-1);
     - conservative finite fibres D(b) (R4-2);
     - representative kernel unstable (R4-3);
     - in flight: R5-1 (pending referee), R5-2 (infinite-orbit kernels), R5-4 (timelike-link laws).
   - *If yes:* B′ becomes the only set where discreteness is physical, Lorentz-clean and lensing-silent, with 5 graviton tunings instead of 11.
   - *If no:* the decision reduces to A against C.
   - Round 6 adds only a conditional stability test (R6-6), to avoid overlap.
2. **Can a finite-per-site interacting lattice law have an exactly additive momentum on its scattering states?** This is the continuum-from-qubits problem.
   - *Decides:* whether any grid set (B, C, or B′ in Z⁴ form) can host an exact graviton Ward identity without importing the continuum.
   - *State:*
     - Lemma G holds in 1D only (`C5_O2_referee_full.md:333`);
     - RN2's d ≥ 2 index lemma is open (`SUMMARY:395`);
     - the I1 referee's T = UV escape is open (`C4_I1_referee.md:15`);
     - umklapp-free interactions are dead only in the analytic/meromorphic classes (`TESTS:1080`).
   - *If yes:* the boost wall has a door for every grid set.
   - *If no (class-wide):* "exact gravity ⇒ continuum" becomes a theorem in that class, and every grid set pays tuning. → **R6-1.**
3. **Can any set produce the graviton rather than supply it?**
   - *Decides:* whether "the TOE produces gravity" is compatible with "Lorentz invariance in law".
   - *State:*
     - every set supplies it (`C5_O5_synthesis.md:316`);
     - Weinberg–Witten exits are listed with their hypotheses (`B_referee.md:47`; `OUTSIDE_VIEW.md:39`);
     - on Z³ the emergent N-type graviton is live but uncoupled to matter's stress (`TESTS:767`).
   - [S5 reading] If WW's hypotheses hold in A and B′, only a Lorentz-violating set (C-type) can host an emergent graviton, and it pays speed tunings. → **R6-2.**
4. **The mean of Λ.**
   - *Decides:* little between sets, since it is a premise in all of them (`TESTS:2939`). But it is the largest open problem for the TOE as a whole.
   - *State:* in flight as R5-3 (unimodular boundary/record condition, Baum–Hawking/Coleman, sequestering, the "count rises until frozen" hypothesis).
   - A set-specific success would make it top-ranked. No round-6 item, to avoid overlap.
5. **Λ's size, and whether it can coexist with sharp lensing.**
   - *Decides:* whether B′ can carry everpresent Λ, and whether any substrate allowed by lensing can.
   - *State:*
     - Poisson gives the right order (`TESTS:2939`) but is lensing-excluded (`SUMMARY:502`);
     - LRL is sub-volume-like so far, with Lemma V open (`TESTS:2943`);
     - the A and C counts fail as stated (`TESTS:2940-2941`).
   - [S5 reading] For a Lorentz-invariant classical process, "no structure factor in band" means no support in a Euclidean ball about q = 0, which suggests sub-volume count variance for smooth windows. Lensing silence and Poisson-size Λ fluctuation may then exclude each other; sharp causal windows are the open case. → **R6-3.**
6. **Can set A's records do gravitational work without a preferred slicing?**
   - *Decides:* whether A's discreteness is more than decoration.
   - *State:*
     - E3 needs a foliation;
     - R leaves the metric inert;
     - covariant CQ-GR is OPEN;
     - only the ultra-local Newtonian CQ is EXCLUDED (`TESTS:2776-2777,2936`).
   - [S5 reading] In CQ gravity the classical metric is itself a record of the mass distribution. If a covariant CQ window survives, A's records become gravity. → **R6-4.**
7. **Set C's full price.**
   - *Decides:* the size of C's bill; it cannot exclude C.
   - *State:*
     - the dimension-3 CPT-odd b₀ and (k_AF)₀ are allowed (`TESTS:1440`), with natural size against the CMB bound only SUGGESTED (`C5_O1_report.md:242-245`);
     - the ≥ 6 total is a reading;
     - RG stability of the counts was deferred (`TESTS:2642`).
   - → **R6-5.**

**Decision map [S5 reading].**
- (1) yes → B′ leads, whatever (2) says.
- (1) no and (2) no → the owner chooses between A (supplied graviton, inert or foliated records, Λ a premise) and C (axioms kept, ≥ 6 tunings + Λ + dimension-3, ± a parity price).
- (3) "only Lorentz-violating sets can produce gravity" → producing gravity forces a C-type substrate.
- (5) "silence excludes Poisson-size count fluctuations" → everpresent Λ has no home in any lensing-allowed set.

---

## 5. Draft round-6 pre-registrations (readings fixed before any run)

**Rules (as for rounds 2–5).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, REFUTED, EXCLUDED or no-go goes to the codex gpt-5.6-sol (xhigh) referee before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Derivation readings: DERIVED / SUGGESTED / REFUTED, as at `TESTS:2315-2318`.

**Overlap check against R5-1..R5-4.**
- R6-1 excludes LRL (covered by R5-1/R5-4).
- R6-3 concerns count fluctuations, not ⟨Λ⟩ (R5-3).
- R6-6 is conditional on R5-2 and tests stability only.

**Priority:** R6-1, R6-2, R6-3, R6-4, R6-5; R6-6 conditional.

---

**R6-1. Exact additive momentum from finite-per-site interacting laws (sets B and C; the continuum-from-qubits problem)**

- **Plain question.** Every exact-graviton route on a grid needs momentum that adds up exactly in collisions. The known obstructions are piecemeal:
  - a 1D qubit chain's shift cannot be interpolated continuously by strictly local maps (Lemma G);
  - a finite one-particle fibre cannot carry the Z⁴ Ward identity (R2-1);
  - umklapp-free interactions are impossible in analytic and meromorphic classes (RG).

  Does the obstruction hold for interacting qubit lattices in d ≥ 2? Or is there a door: a momentum defined only on scattering states, or an internal symmetry V carrying the shift's index (T = UV)?
- **Setting.** Quasi-local spin systems on ⊗_{Z^d} M₂(C), d = 2, 3, with:
  - (i) strict-range QCA paths;
  - (ii) approximately local automorphism groups with Lieb–Robinson tails;
  - (iii) Heisenberg dynamics of quasi-local Hamiltonians with nontrivial 2→2 scattering (Haag–Ruelle on the lattice).

  Euclidean B enters through the OS-reconstructed transfer matrix on Z³ × Z_τ. LRL is excluded.
- **Prior art (count once).**
  - O2 Lemmas S and G (`TESTS:2392-2394`; `C5_O2_referee_full.md:195,333`);
  - I1 referee on T = UV and GNVW/RWW conventions (`C4_I1_referee.md:15`);
  - RN2 (`SUMMARY:395`; `C4_N1_referee.md`);
  - R2-1 Theorem T (`TESTS:2748-2751`);
  - RG G1 umklapp-free classes (`TESTS:1023-1028,1080`);
  - RS (`PRICE_NOTE:323`).
- **Probes.**
  - (a) **Index in d ≥ 2.** Prove or refute that no continuous path, and no strongly continuous one-parameter group α_s with α_1 = the unit lattice shift, exists among:
    - strict-range QCAs, using flow per unit cut length;
    - approximately local automorphisms, extending RWW from 1D; state exactly which d ≥ 2 index theorem is used, or prove the needed one.
  - (b) **T = UV.** Under what conditions can an on-site-generated internal symmetry V carrying the inverse shift index commute with an interacting dynamics with nonzero scattering? Does V force an infinite on-site or one-particle structure (P10)?
  - (c) **Asymptotic-only charge.** Assume a lattice S-matrix that conserves quasi-momentum modulo the reciprocal lattice. Prove or refute: an additive ℝ^d-valued charge extending quasi-momentum on asymptotic states exists only if every umklapp amplitude vanishes. Then search outside RG's classes for a nonzero-scattering umklapp-free qubit law: integrable, kinematically constrained, or non-analytic.
  - (d) **Transfer to Z⁴.** Carry (a)–(c) to the OS-reconstructed Euclidean Z⁴ transfer matrix; state what reflection positivity adds.
- **FIXED readings** (derivation):
  - **DERIVED:** (a) and (c) proved in a stated class covering interacting finite-per-site laws in d ≥ 2. In that class, an exact graviton Ward identity on any grid set then requires the continuum. Record: "grid sets pay tuning or import the continuum (class …)".
  - **SUGGESTED:** argued only, for (a) or (c); record which.
  - **REFUTED:** an explicit finite-per-site interacting law in d ≥ 2 with nonzero 2→2 scattering and an exact additive ℝ^d asymptotic momentum, checked numerically on scattering data.
- **Expectation.**
  - (a) DERIVED for strict-range paths, SUGGESTED for approximately local ones.
  - (c) SUGGESTED.
  - Overall SUGGESTED. There is a real REFUTED risk from integrable umklapp-free sectors.

---

**R6-2. Can any set produce the graviton? A Weinberg–Witten sorting with the B′ specifics**

- **Plain question.** In every set the graviton is put in by hand. The Weinberg–Witten theorem says a Lorentz-invariant theory with a Lorentz-covariant conserved stress tensor has no massless spin-2 particle. So an emergent graviton needs one of the theorem's assumptions to fail:
  - Lorentz invariance;
  - a covariant T;
  - a particle pole;
  - locality or holography.

  Which sets can produce, rather than supply, a graviton that couples universally to matter's energy-momentum?
- **Setting.** The four sets as defined (`TESTS:2424-2428,2647-2651`). Matter: the minimal content each set's refereed results allow. Graviton: any emergent massless helicity-±2 mode.
- **Prior art (count once).**
  - `B_referee.md:47,175` (WW hypotheses and exits);
  - `OUTSIDE_VIEW.md:39`;
  - lane R on Z³: Gu–Wen and rank-2 models, the exact-constraint N-type theory live, its coupling to matter's T open (`TESTS:714-767`);
  - O2 Lemma W (`TESTS:2386-2389`);
  - R2-6 (non-additive momentum kills the soft coupling).
- **Probes.**
  - (a) Per set, state WW's hypotheses and check each against the set's refereed low-energy content: an IR Lorentz-covariant conserved T^{μν} with nonzero forward one-particle matrix elements, and particle poles.
  - (b) **B′ specifics.**
    - A realization has only Γ_L. Does WW's small-angle helicity argument go through with Γ_L alone, using Zariski density and Lemma Z (`TESTS:2925`)?
    - Does multiparticle umklapp (`TESTS:2791`) spoil the covariance of the forward matrix element?
  - (c) **B specifics.** WW concerns IR matrix elements. Does dimension-4 Lorentz protection with dimension-6 breaking (`C5_O5_synthesis.md:132`) suffice for its hypotheses?
  - (d) **C specifics.** Can the lane-R N-type graviton couple universally to matter's energy-momentum? State the minimal speed tunings: the graviton–matter Collins split (`TESTS:719`).
  - (e) **Exits.** For each exit (holography, non-particle gravity, non-covariant T as in GR's pseudotensor), say which set's axioms could host it and at what price.
- **FIXED readings, per set:**
  - **PRODUCIBLE:** a stated mechanism evades WW in that set, with universal coupling to matter's energy-momentum and the prices named.
  - **SUPPLIED-FORCED:** WW's hypotheses are shown to hold in that set's low-energy content, so the graviton must be an elementary gauge field (supplied). Referee required.
  - **OPEN:** otherwise.
- **Expectation.**
  - A: SUPPLIED-FORCED.
  - B: SUPPLIED-FORCED at the IR level, or OPEN.
  - B′: OPEN, leaning SUPPLIED-FORCED via Lemma Z.
  - C: OPEN; WW is evaded by Lorentz violation, and universal coupling is the barrier.

---

**R6-3. Lemma V: does the Lorentz-random lattice's count fluctuate like a volume? Does lensing silence exclude Poisson-size Λ fluctuations?**

- **Plain question.** Everpresent Λ gets its size from the number of events in our past fluctuating like a Poisson count. Poisson events are excluded by lensing. The Lorentz-random grid passes lensing, but its counts looked sub-Poisson through T = 108.
  - Does its count in a causal diamond or past cone of size T fluctuate as T⁴, slower, or faster?
  - Is there a general trade-off between lensing silence and Poisson-size count fluctuation?
- **Setting.**
  - The cocompact L₇ LRL ensemble, with the Haar measure on ISO⁺(1,3)/(L ⋊ Γ_L) (`C5_R2-2_referee.md:9`).
  - Windows: causal diamonds D_T and truncated past cones, each sharp and smoothed.
  - Comparators: Poisson at equal density, and Z⁴ in two frames.
- **Prior art (count once).**
  - R4-5 numerics and Lemma V (`TESTS:2943`; `C5_R4-5_referee_verdict.md:13,15`);
  - P-L′ (`TESTS:2712`);
  - O5 remark 1, quantum forward-cone volume law (`C5_O5_synthesis.md:447-453`);
  - E2/E3 frozen hyperuniform sets, spatial (`TESTS:243-263`);
  - Siegel densities (`TESTS:2905`).
- **Probes.**
  - (a) **Variance formula.** Write Var N(W) = ∫ S(q)|Ŵ(q)|², with S = the Haar average of the Bragg combs, i.e. a sum over shells Q(n) of the Siegel mass times the invariant measure on q² = (2π)²Q(n)/7. State convergence.
  - (b) **Shell asymptotics.** Find the asymptotics in T of ∫_{q²=c}|Ŵ_T|² dμ for sharp diamonds and past cones. Null boundaries make Ŵ decay slowly along null directions, where the hyperboloids accumulate. Find the exponent and the shell-sum convergence.
  - (c) **Numerics.** Extend R4-5 to larger T with sampling that is genuinely Haar on the quotient (R4-1's sampling correction, `TESTS:2909`). Fit with and without a T⁴ term.
  - (d) **Trade-off lemma.** For a Lorentz-invariant classical stationary point process with no structure-factor support for 0 < |q²| < c, prove or refute o(T⁴) count variance in diamonds.
    - Smooth windows: expected easy, since there is no support in the Euclidean ball of radius √c.
    - Sharp windows: the real case.
  - (e) **Λ size.** Translate the result into δΛ/Λ_obs under R4-5's three premises (`TESTS:2939`).
- **FIXED readings.**
  - For the LRL count:
    - **VOLUME:** Var ∝ T⁴ with a computed F > 0; state the resulting δΛ/Λ_obs.
    - **SUB-VOLUME:** o(T⁴) proved for sharp diamonds and past cones; record "everpresent-Λ magnitude excluded on LRL under the three premises" (referee required).
    - **DIVERGENT:** the shell sum diverges for sharp windows; report the regularization dependence.
    - **OPEN:** otherwise.
  - For (d) (derivation): **DERIVED / SUGGESTED / REFUTED.**
- **Expectation.**
  - Smooth windows: SUB-VOLUME (DERIVED).
  - Sharp windows: OPEN, leaning SUB-VOLUME with boundary-dominated growth.
  - (d): SUGGESTED.

---

**R6-4. Set A: can the records be the classical metric? (covariant classical–quantum gravity against the decoherence–diffusion bounds)**

- **Plain question.** In set A the records either do nothing for gravity or need a preferred slicing. In classical–quantum (CQ) gravity, the metric is classical: it is a record of where the mass is. It must then diffuse enough to keep quantum mechanics consistent, and lab experiments bound both the diffusion and the decoherence it causes. The simplest version is excluded by 32 decades. Does any version survive?
  - a smeared one;
  - the diffeomorphism-invariant one.

  And would its metric record satisfy "one record per site, permanent"?
- **Setting.** The variants:
  - (i) Newtonian CQ with a smearing length ℓ_s (non-ultralocal);
  - (ii) the diffeomorphism-invariant CQ-GR candidate cited in R3-4 (Oppenheim–Weller-Davies);
  - (iii) the Record reading: the metric history as the record set.

  Bounds:
  - Cs-133 at 1.9 µm for 70 s; 25 kDa molecules; ion coherence (`TESTS:2538-2541`);
  - torsion-balance and Cavendish mass-precision diffusion bounds, as published, verified or labelled from memory.
- **Prior art (count once).**
  - R3-4 E2 (`TESTS:2776`; `C5_R3-4_referee_verdict.md:13`);
  - R4-4 Lemma N: a classical channel gives zero entanglement (`TESTS:2935`), so a BMV-type positive result would exclude every variant; state that as a falsifier;
  - R2-3 Bianchi lemmas (`TESTS:2722`);
  - O4 Lemma 1 (`TESTS:2408`).
- **Probes.**
  - (a) Derive the decoherence–diffusion trade-off for (i) as a function of ℓ_s, and find the allowed window in ℓ_s.
  - (b) For (ii), state whether the covariant theory has a computed weak-field trade-off. If it does, apply the bounds; if not, say what is missing.
  - (c) Energy-momentum: does CQ diffusion source a Λ-like drift? Compare with R4-5's 17-decade Bianchi gap (`TESTS:2944`).
  - (d) Record reading:
    - Is a diffusing classical metric a set of permanent, one-per-site records in a block sense?
    - Which axiom text changes? Name the price.
- **FIXED readings, per variant:**
  - **VIABLE:** passes the stated bounds with named prices.
  - **EXCLUDED:** violates a stated bound for every parameter in the variant (referee required).
  - **OPEN:** otherwise.
- **Expectation.**
  - (i): a narrow VIABLE window at macroscopic ℓ_s, or EXCLUDED.
  - (ii): OPEN.
  - (iii): a reading with a Record price.

---

**R6-5. Set C's dimension-3 price: CPT-odd terms the axioms' proper-only rotations allow**

- **Plain question.** The axioms name only proper cubic rotations (`AX:37-41,57-58`). That allows two CPT-odd terms of dimension 3 (`TESTS:1440`):
  - an axial chemical potential b₀ for fermions;
  - a photon Chern–Simons term (k_AF)₀.

  Their natural size on a Planck lattice would be near the cutoff, while observation bounds (k_AF) to about 6e-43 GeV (`C5_O1_report.md:49`, partially verified). Are they generated? How large are they? Is the cheapest fix a tuning, or a symmetry added to the law?
- **Setting.**
  - Z³ × ℝ, with a gauge-invariant local Hamiltonian lattice law covariant under translations and proper cubic rotations only: no inversion and no antiunitary symmetry.
  - Matter: naive/staggered or Wilson-type fermions with compact U(1); then chiral content as R2-4 allows.
  - Sets B and B′ are excluded: V = 0 and Zariski density forbid invariant vectors (`TESTS:2379`; `TESTS:2788`).
- **Prior art (count once).**
  - F2 referee (`TESTS:1440`);
  - O1's counts and dimension-3 note (`C5_O1_report.md:82,104,242-245`);
  - the R2-4 chirality and CP scope (`C5_R2-4_referee.md:44-63`).
- **Probes.**
  - (a) An explicit local law in the class with b₀ ≠ 0 at natural size: a Weyl-node energy offset.
  - (b) Is (k_AF)₀ induced? Points to settle:
    - compact lattice U(1) admits no local A·B term;
    - the equilibrium chiral-magnetic response vanishes on lattices (Vazifeh–Franz, RECALLED; verify);
    - so state whether k_AF is PROTECTED, or induced through non-equilibrium or non-compact sectors.
  - (c) Observational bounds on b₀ for electron, proton and neutron (torsion pendulum, comagnetometer, boost-suppressed timelike components) and on k_AF (CMB). Verify or label from memory. Give the tuning in decades.
  - (d) The cheapest symmetry price: law-level CPT, i.e. CRT with spatial inversion, added to Lattice/Admissibility covariance. Is it compatible with chiral SM content and doublers/tastes on the lattice? Name the axiom text it touches.
- **FIXED readings.**
  - **TUNING-PRICED:** an explicit law in the class generates the term(s) at a computed natural size; state the tuning in decades against the stated bounds.
  - **SYMMETRY-PRICED:** a stated symmetry forbids them, is compatible with chiral content, and the axiom text it touches is named.
  - **PROTECTED:** proved forbidden by gauge invariance, locality, hermiticity and the axioms as written; C's price does not grow.
  - **INCONCLUSIVE:** otherwise.
  - More than one reading may apply, one per operator.
- **Expectation.**
  - b₀: TUNING-PRICED, by tens of decades.
  - (k_AF)₀: PROTECTED or suppressed in equilibrium (OPEN risk).
  - SYMMETRY-PRICED is available through law-level CPT, at a Lattice-text cost.

---

**R6-6 (conditional: run only if R5-2 returns PASS or INCONCLUSIVE with an explicit kernel). Stability of an LRL d'Alembertian**

- **Plain question.** R4-3 found that the representative five-shell kernel has a growing mode that e-folds in about two lattice times. Does any Γ_L-invariant retarded kernel whose mean is □ have no such mode? That includes R5-2's infinite-orbit kernel, if it exists.
- **Setting.**
  - Retarded Γ_L-invariant kernels on L₇, finite-shell and infinite-orbit, with Haar mean □ + O(a²).
  - Symbols in the forward tube (Prop. R, `TESTS:2787`).
- **Prior art (count once).**
  - R4-3's tube zeros (`TESTS:2927`; `C5_R4-3_referee_verdict.md:15`);
  - R4-1's weights (`TESTS:2905`);
  - Aslanbeigi–Saravani–Sorkin on stability of causal-set d'Alembertians (comparator, `C5_R4-3_referee_verdict.md:15`).
- **Probes.**
  - (a) An argument-principle certificate for forward-tube zeros of the mean symbol over a stated domain.
  - (b) Construct a moment-cancelled family with no tube zero, or prove that every family in a stated class has one.
  - (c) Apply (a) to R5-2's kernel.
- **FIXED readings.**
  - **PASS:** an explicit kernel with mean □ + O(a²) and a certified zero-free forward-tube symbol.
  - **FAIL:** a proof that every kernel in a stated class has a forward-tube zero (referee required).
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. Stable families are known for causal-set d'Alembertians in some dimensions (comparator, RECALLED); whether moment cancellation on LRL shells allows one is open.

---

## 6. Caveats

- **Same family, unrefereed.** The set table, the readings, the price numbering P15–P23 and the rankings are S5's. Every verdict quoted is a codex verdict at the cited line. Where a cell says "F" for a set, it means met under the cited hypotheses, not proved necessary.
- **Round 5 is not in this synthesis.** R5-1's worker reading (FAIL bounded) is unrefereed. Its referee folder exists (`scratchpad/C5/ref_R5-1/`) with no verdict yet. R5-2, R5-3 and R5-4 had no report at 14:05Z.
- **The sets are not exhaustive.** Holographic, relational and non-commutative constructions outside D's class remain unexamined (`C5_O5_synthesis.md:505`; `C5_R2-6_referee.md:17`).
- **The pre-registration drafts are proposals for the driver.** Their readings are fixed here so they cannot be adjusted after a run; the driver may reorder or drop items.
