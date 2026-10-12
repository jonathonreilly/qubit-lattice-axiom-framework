# C5 S8: synthesis after rounds 5–8 (refereed through 16:25Z; R8-1, R8-4, R8-5 pending)

**Author.** Claude Opus 5.5 (S8), the same model family as every C5 worker, the supervisor and S5. **This synthesis is not refereed and gives no verdicts.** Every verdict quoted is a codex gpt-5.6-sol (xhigh) referee verdict as recorded in `TESTS.md` or in the cited `C5_*_referee_verdict.md`. Written 2026-10-12, 16:24Z to about 16:36Z. No repository file was edited.

**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:2302-2436` and `:2900-3573` (C5 method, round 1, round 4 results to the end; `:2436-2900` was taken from S5's reading); `agents/C5_S5_synthesis.md`; `SUMMARY.md:534-606` (§§21–23); `PRICE_NOTE.md:150-414` (§5–§7 and the v6 delta); referee verdicts `C5_R7-1`, `C5_R8-2`, `C5_R7-5`, `C5_R6-1`, `C5_R7-6`, `C5_R7-4`, `C5_R6-4`, `C5_R8-3`, `C5_R7-3`, `C5_R6-2`, `C5_R6-3`, `C5_R5-4`, `C5_R5-5` (`_referee_verdict.md`). **Read in part:** `C5_R7-2_referee_verdict.md:1-56`; `C5_R8-2_report.md:1-60` and grep hits `:64-70,:130-131,:152,:177-178`; `C5_R7-1_report.md` grep hits on rapidity; `C5_R8-1_report.md:1-60` and `:127,:164,:258,:279,:290` (pending; used only as "pending").

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `PRICE_NOTE` are in `P/`; bare `C5_*`, `C4_*` are in `P/agents/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.**
- **[ref]** a referee-confirmed statement, with the referee's scope.
- **[ref, bounded: …]** a refereed FAIL, EXCLUDED or no-go, with its class.
- **[ref-rerun]** a worker number the referee reports as reproduced by rerun, without a separate ruling on its interpretation.
- **[worker]** a worker statement with no referee (none was required, because no FAIL was claimed).
- **[pending]** R8-1 (referee running), R8-4, R8-5 (workers running).
- **[S8 reading]** an interpretation made here; same family; unrefereed.

**Sets.** A = continuum base, discreteness only in records. B = Euclidean Z⁴, whole law hypercubic. B′ = the Lorentz-random lattice (LRL). C = the axioms' Z³ (with continuous time) and tune. **C-box** (new) = set C's Z³ × ℝ with one fermion mode per site, a box dispersion that is exactly √(m² + k²) on an open momentum box and smooth and periodic outside, super-polynomially (not exponentially) quasi-local hopping, and interactions that are box-supported or invariant-mass structured (`TESTS:3242-3255,3398-3407`). **E** (new) = holographic or lower-dimensional substrates (`TESTS:3272-3283`).

---

## 1. What changed since S5, in plain words

### 1.0 The short version

At S5 (14:05Z) every road to exact gravity ended in one of two places: the continuum (set A) or a tuning (set C). Since then three things moved.

1. **A third kind of road opened: relativity that is exact on a patch.** Keep the 3D grid. For momenta inside a box, give each particle exactly the relativistic energy. Outside the box, bend the energy back smoothly so it is periodic. Boosts then work exactly, not approximately, for every state inside the box, until a boost pushes some particle to the box edge. This is the campaign's first PASS (R7-1). It slips past every earlier boost no-go because each of them assumed one of three things: boosts on all momenta, boosts of any size, or bands that are analytic.
2. **Set A's records can be the classical metric again, at Newtonian level.** The published "32 orders of magnitude" exclusion of classical–quantum (CQ) gravity came from an invalid step. With that step fixed, gravity smeared over 4e-10 to 5e-6 m fits the lab bounds (R6-4). The simplest relativistic versions fail (R8-3), but the no-go names its own escapes.
3. **The Lorentz-random lattice (B′) is losing.** A single copy still has no long-distance law (R5-2), no generated particle shell (R5-4), and its frame superposition helps only if the frame is declared unobservable (R5-5). Its event count fluctuates too little to give Sorkin's Λ; the predicted fluctuation comes out too large, by about 1e30 (R6-3).

**What did not move.** No set produces the graviton (R6-2: A, B, B′, C all OPEN). Nothing makes the vacuum's average weight zero without tuning (R5-3: all four routes OPEN). Holography helps only for negative Λ, or is unbuilt in 4D (R7-2).

**[S8 reading], the honest frame for C-box.** The box law supplies the continuum dispersion as data on the box, much as P10 supplied a continuum tower per cell. The difference is cost: one mode per site and a finite rapidity budget, instead of an infinite fibre. So C-box does not *derive* relativity; it shows that a finite-per-site grid can *carry* exact relativity on a patch. Whether that patch survives interactions, loops, gauge fields and gravity on bound bodies is the open question of round 9.

### 1.1 The box route, item by item (what is refereed, with scope)

Think of it as a ladder. Each rung adds physics. Here is how far up it has been checked.

**Rung 1: free particles, any number. PASS WITH SCOPE [ref; `TESTS:3398-3407`].**
- *What holds.* A graded-CAR, continuous-time law with smooth, non-analytic, super-polynomially quasi-local hopping. On compactly supported finite-particle wavefunctions inside the open box, the boost, momentum and rotation generators satisfy the undeformed Poincaré Lie algebra exactly (`TESTS:3399`).
- *The finite-boost statement.* Finite boosts agree with continuum boosts until support reaches the box edge. For one axis-boosted leg, the budget is η* = asinh(b/m⊥) − |θ|. Leakage is bounded by ‖(U_lat − U_cont)ψ‖ ≤ 2‖1_E ψ‖ (`C5_R7-1_referee_verdict.md:150-171`).
- *Scope (the referee's words, condensed; `C5_R7-1_referee_verdict.md:60-66,266-271`).*
  - graded CAR;
  - continuous time;
  - free algebra at all finite particle numbers;
  - non-analytic, super-polynomial but sub-exponential tails;
  - a local Lie-algebra domain, **not** an invariant or exponentiating Poincaré sector;
  - no gauge fields, pair creation, loop protection, local-lapse algebra or universal coupling.
- *Numbers.* At Planck spacing the budget is about 45 units of rapidity for a proton and 53 for an electron. The fastest cosmic rays use about 27 (`SUMMARY:574`). These are arithmetically right, but the Planck-spacing bridge is a reading (`C5_R7-1_referee_verdict.md:173-176`; `AX:187-190`).
- *How it stands against earlier walls.* It lies outside C3/I2 (a global Hessian average), I1/I3 (integrated covariance), B1 (exponentiating sectors) and C1/R2-1/RFW (analytic or finite-Fourier symbols). It avoids their hypotheses; it does not overturn them (`C5_R7-1_referee_verdict.md:178-207`).
- *Hidden price.* The referee names it: an inert, non-gravitating edge violates universal coupling (`C5_R7-1_referee_verdict.md:212-219`).

**Rung 2: two interacting particles. Repairable, not confirmed as written [ref; `TESTS:3403-3404`]; repair pending.**
- R7-1's two-body Bakamjian–Thomas (BT) law had a boost-sign error and a CAR normalization the referee read as a factor-of-two error. A corrected d = 1 BT construction is available. In d ≥ 2 a rotationally invariant channel is needed (`C5_R7-1_referee_verdict.md:93-129`).
- Interacting leakage was unproved (`TESTS:3404`).
- **[pending] R8-1** (worker; `C5_R8-1_report.md:22-44`):
  - claims the repair in d = 1 (lattice ring) and in d = 2 (p-wave doublet plus a spin term), and proves interacting leakage using the internal-mass spectrum;
  - disputes the ¼ factor as a convention mismatch (`C5_R8-1_report.md:164`);
  - reports the d = 2 lattice-native check as resolution-limited (`:258,:290`).

  Not a verdict.

**Rung 3: three bodies. INCONCLUSIVE [ref; `TESTS:3506-3510`].**
- Summing pair BT interactions fails: the bound trio's invariant mass drifts with total momentum. The drift survives a ¼ rerun (δ ≈ 0.019) and widening the plateau and the box (`C5_R7-6_referee_verdict.md:36-46`).
- *Consequence.* Given P = Q and a self-adjoint, locally exponentiating K, no boost completes the pair-sum H. A connected three-body term is required (`:52-67`).
- *P = Q is an added bridge*, not a consequence of the Lattice axiom (`:85-91`).
- *Sokolov packing* is a formal route only. It was not built as a lattice operator, and its tails are unproved. A power law fits the separation data better over 40–320 than exp(−0.8√r) does (`:118-137`).

**Rung 4: loops with pair creation. Bounded FAIL for classes P and FF; INV conditional [ref; `TESTS:3500-3504`].**
- *The FAIL.* Point Yukawa and frame-fixed smooth vertices on the box dispersion give δc² = (g²/16π²)·XI, with XI_P ≈ 1.7–1.94 and XI_FF ≈ 10.9. This is unsuppressed dimension-4 Lorentz violation (`C5_R7-5_referee_verdict.md:9-11`).
  - Scope: one scalar kinetic coefficient from a fermion loop; not a complete QED split (`:11`).
- *INV, a conditional lemma.* Suppose continuum on-shell legs stay in the box, and both pole orderings carry the same compact invariant-mass weight. Then the scalar self-energy, and the scalar self-energy with a Dirac loop, are exactly Lorentz-invariant spectral functions inside the momentum budget (`:15-19`).
  - No stable finite-per-site Hamiltonian realizing it was built. The vacuum-triple cubic term is generically unbounded below (`:22`).
  - The invariant-mass form is an imposed functional custodial condition, not derived, and not shown radiatively closed (`:34`).
- *BT here* is a bounded-sector mass-operator model, not a field theory (`:24-28`).
- **[pending] R8-4** (an explicit INV Hamiltonian) and **R8-5** (gauge fields in the box).

**Rung 5: gravity on free matter. INCONCLUSIVE against the physical PASS [ref; `TESTS:3550-3557`], with three refereed parts.**
- *Universal free stress exists.* For free number-conserving matter there is a smooth, quasi-local, symmetric, Hermitian box-plus-edge stress kernel with an exact linear Ward identity. Its energy integral is the full H, and its first energy moment is R7-1's boost on box states (`C5_R8-2_referee_verdict.md:5-21`).
- *Lemma U.* Continuity forces box–edge matrix elements. States near a box face couple across it with small momentum transfer (`:25-29`).
- *Theorem E* [ref, bounded: free, finite periodic band, first-moment uniform-lapse coupling; `:31-47`]. Ṗ_i = −g_j[δ_ij H + dΓ(εA_ij)], with A = Hess(ε²/2) − I. Over a C² periodic band, A averages to −I. **So every finite periodic band has states that fall non-universally.**
  - Not covered: non-periodic towers, singular bands, non-adiabatic multiband dynamics, altered source bridges, interacting composites (`:47`).
  - Plain: in a uniform field, a quantum with lattice momentum k falls with weight Hess(ε²/2) at k. Over the whole zone that weight averages to zero, not one. Inside the box it is exactly one, so somewhere outside it is not. The boost-wall anomaly has been moved to the edge, not removed.
- *Doublers.* R7-1's literal band has exactly 2^d − 1 extra mass-m valleys at the zone corners (`:49-51`).
  - At rest they fall correctly, with weight 1. The weight is about −30 at the s-maximum k* = 2.234; energy-weighted edge means are −1.7 and −3.7 [ref-rerun; `C5_R8-2_report.md:68,130-131,177`; rerun at `C5_R8-2_referee_verdict.md:7`].
- *Gapped edge.* A monotone edge can remove the doublers, but continuity caps the edge threshold at √(m² + b²)/a. That is a ceiling, not an equality for every extension (`:53-58`).
- *What is missing.* η = 0 holds only as a free-packet proxy. No interacting universal stress and no bound-body Eötvös observable were built (`:60-66`).
- *R7-4's exclusion* of box-supported scattering is only conditional (`:68-72`, below).

**Rung 5′: the global-bridge exclusion. A conditional bounded FAIL [ref; `TESTS:3496-3497`; `C5_R7-4_referee_verdict.md:43-55,75`].**
- Constraint preservation gives the formal i[H,D] = J and [H,J] = 0.
- If D is moreover essentially self-adjoint and globally exponentiating, with domain-compatible Møller intertwining and short-range clustering, then every proper box-supported scattering amplitude vanishes.
- R7-1 evades this by claiming only a local algebra within a rapidity budget.
- [S8 reading] Any C-box gravity can therefore be exact only inside the budget, never as an integrated statement.

### 1.2 The exact-momentum results feeding the box route

- **R6-1. SUGGESTED, with derived parts [ref; `TESTS:3316-3329`].**
  - *Witness W.* One fermion mode per site on Z² (graded CAR) has exact sawtooth momentum, exact many-body conservation, and genuinely non-forward, umklapp-free 2→2 scattering. It is super-polynomially, not exponentially, local.
  - *Outside the fixed class.* It is not in the fixed ⊗M₂ spin class (`C5_R6-1_referee_verdict.md:17`).
  - **DERIVED in every dimension:** no uniformly range-bounded, H-TI strict-QCA path, and no strict-range root, of the lattice shift (`:23`).
  - *T = UV.* The factorization is exact, but V is not on-site generated; it realizes I1’s non-geometric loophole (`:25`).
- **R7-3. SUGGESTED, with derived parts [ref; `TESTS:3543-3548`].**
  - *Kitaev route.* On the flux-free invariant sector of a one-qubit-per-site Kitaev model, a spin-string image of W has exact additive momentum and non-forward scattering.
  - *Not superselection.* The flux sectors are dynamically invariant, not superselection sectors: a single σ^z connects them (`C5_R7-3_referee_verdict.md:31`).
  - *Lemmas.* Lemma S (flat-band defects) and Lemmas I/L (hard-core obstructions) hold under their hypotheses (`:5,:19`).
  - *What is missing.* No all-sector ⊗M₂ witness exists.

### 1.3 Set A: records as the metric

- **R6-4 [ref; `TESTS:3409-3418`].**
  - **(i) VIABLE.** Smeared Newtonian CQ is viable on the conservative subwindow 4e-10 ≲ ℓ_s ≲ 5e-6 m.
    - Class: homogeneous Markovian Gaussian continuous CQ with additive dephasing.
    - The true lower end is about 1e-10 m after an 8π correction to the DP floor (`C5_R6-4_referee_verdict.md:7`).
  - **(ii) OPEN.** The covariant theory is open; only Layton et al.'s unregulated point-particle Newtonian limit is EXCLUDED (cubic UV heating, Corollary U) (`:15`).
  - **(iii) A reading with prices** on Lattice, Qubit, Admissibility and Record, plus a source/readout/permanence bridge (`:19`).
  - **Dated correction.** The R3-4 "32-decade empty window" falls: OSSW's F8–F10 torsion reduction is invalid by 9.45e44 (`TESTS:3418`; `:9`).
- **R8-3. OPEN, with a conditional no-go [ref; `TESTS:3559-3573`].**
  - *The no-go.* At golden-rule order, consider a Lorentz-invariant linearized Gaussian CQ model with:
    - a common scalar stress form factor (or a nonzero GR-normalized spin-2 one);
    - a retarded propagator;
    - a pointwise decoherence–diffusion bound;
    - additive decoherence.

    Such a model cannot simultaneously keep the light-cone coupling, give finite radiation, and have a finite vacuum-excitation rate.
  - *What it excludes.* e^{ℓ²□} and bounded scalar factors in that subclass.
  - *What it does not exclude* (`C5_R8-3_referee_verdict.md:19`):
    - non-Markovian or correlated histories;
    - OWD as a framework;
    - trace-only or spin-separated kernels;
    - light-cone-renormalized distributions;
    - jumps, non-Gaussian dynamics, mediators.
  - *Preferred frame.* The preferred-frame route is OPEN, with 1e-8 to 5e-6 m as a search target, not a demonstrated window (`:15`).

### 1.4 Sets B′, C, E and the shared items (refereed since S5)

- **B′.**
  - R5-1: FAIL, bounded. Covariant families on supports with infinite stabilizers carry no shell and no four-charge. Theorem Q: continuous full-Γ event rules are condition-independent, and full DLR versions are products (`TESTS:2970-2981`).
  - R5-2: INCONCLUSIVE. Exact reduction; full-lattice sums give P(−□)δ(k), not −k² (`TESTS:3287-3298`).
  - R5-4: INCONCLUSIVE. Theorem Δ: Haar-null or Haar-conull kernel sets; no generated L₇ shell (`TESTS:3300-3307`).
  - R5-5: INCONCLUSIVE. Exact ensemble-mean unitarity is excluded only under imposed superselection (`TESTS:3309-3314`).
  - R6-3: count SUB-VOLUME (diamonds O(T² log T), cones O(T³)). Literal Lemma V is REFUTED by Lorentz-random affine Z⁴ (null vectors, T⁶). V′ (gap including the null cone) is DERIVED. Strict lensing silence is OPEN. Under H1/H2/H4, δΛ is too large by 1.4e30 (cone) and 1.4e59 (diamond) (`TESTS:3420-3428`).
- **C.**
  - R7-4: two decoupled species admit an exact linear-order N-type bridge with γ_s = c_s²/c_g². Universality and γ = 1 come only by imposing equal couplings and a common cone (`TESTS:3485-3494`).
  - R6-5 [worker; no referee]:
    - b₀ is TUNING-PRICED at 43–49 decades;
    - (k_AF)₀ is PROTECTED by vacuum stability plus Bloch/Watanabe;
    - the dimension-5 CPT-odd photon term is about 10 decades (suggested);
    - law-level CPT is conditional (`TESTS:3264-3268`).
- **E.** R7-2 (`TESTS:3430-3439`):
  - pure AdS is EXCLUDED only as our bulk with constant Λ < 0;
  - AHS higher-spin dS/CFT is EXCLUDED narrowly;
  - everything else is OPEN;
  - the explicit D ≤ 3 realizations give no local graviton (random tensor networks are not covered);
  - {5,3,4} is Planck-curved (10^62.3);
  - the N-bound is 4.78e122 qubits.
- **Shared.**
  - R5-3: all four ⟨Λ⟩ routes OPEN. Lemma PT within G1–G3 (electroweak shift needs 1 part in 4.7e54). Global Kaloper–Padilla sequestering is EXCLUDED, bounded (|Ω_k0| ≥ 0.917). "Records form until frozen" leaves an additive constant (`TESTS:2985-2993`).
  - R6-2: A, B, B′ and C all OPEN for producing the graviton. WW forbids elementary and composite spin-2 alike under its premises, so "supplied" is not forced (`TESTS:3331-3343`).

**Calibration of S5's expectations [S8 reading].**
- Right in direction:
  - R6-1 (SUGGESTED);
  - R6-3 (SUB-VOLUME, now for sharp windows too);
  - R6-4(i) (a narrow VIABLE window);
  - R6-5 (b₀ tens of decades, worker).
- Wrong: R6-2 for set A. S5 expected SUPPLIED-FORCED; it is OPEN.
- Unforeseen: R6-1's witness opened the box route, which S5 did not foresee.

---

## 2. Table: forced / dead (bounded) / open

**Legend.**
- **F** = forced or met, under stated hypotheses.
- **D(b)** = dead, bounded to the named class.
- **O** = open.
- **P** = premise (supplied by hand).
- **pend** = R8-1/R8-4/R8-5 running.

Cells unchanged since S5 are shortened to "as S5" with S5's cite (`C5_S5_synthesis.md:227-238`).

| Item | A: continuum + records | B: Euclidean Z⁴ | B′: LRL | C: Z³ + tune | C-box: Z³ + box law | E: holographic |
|---|---|---|---|---|---|---|
| **One light cone** | F by exact Poincaré (as S5) | F at dim 4 (as S5) | F for regular null/spacelike branches (Lemma Z). O: timelike; no generated shell (`TESTS:3307`) | P: speeds tuned (F2: 3.1e-17). [worker] b₀ 43–49 decades; k_AF protected (`TESTS:3265-3266`) | F for free matter inside the box, by construction (`TESTS:3399`). **D(b):** point Yukawa (P) and frame-fixed (FF) loops give δc² = (g²/16π²)XI, XI ≈ 1.7–10.9 (`TESTS:3501`). O: INV conditional lemma (`TESTS:3502`). pend: R8-4, R8-5 | O. dS/CFT keeps 3 dims, but Z³ breaks conformal symmetry (`TESTS:3437`) |
| **Graviton: exact gauge identity** | O (not SUPPLIED-FORCED; `TESTS:3332`). Still supplied in every built A | D(b): finite one-particle fibre (as S5). O: R6-2 (`TESTS:3331`) | D(b): conservative finite fibres (as S5); infinite-stabilizer supports (`TESTS:2971-2974`). O: link cells (`TESTS:3307`) | Linear N-type bridge for decoupled species (`TESTS:3486-3491`). D(b), conditional: box-supported scattering cannot feed a *global* exact bridge (`TESTS:3497`) | F (free, linear order): box⊕edge stress, exact Ward identity, ∫T⁰⁰ = H, first moment = boost (`TESTS:3554`). O: interacting W2 and local-lapse W4 (`TESTS:3405`). pend: R8-1 (algebra only) | D(b): explicit D ≤ 3 realizations (`TESTS:3434`). O: random tensor networks, dS/CFT |
| **Graviton: tuning count** | 0 beyond Λ (supplied) | 11 (as S5) | 5, conditional (as S5) | 2 TT + speeds (≥ 6 is a reading). N-type: + equal a_s and c_s = c_g imposed per species pair (`TESTS:3492`) | Not computed. [S8 reading] Matter-speed tunings are traded for P28; the graviton's own TT masses and speeds are untouched unless it also gets a box law. Whether the edge feeds the E_g shear mass is open (R9-2a) | n/a |
| **Equivalence principle** | F, exact | SUGGESTED from dim-4 protection (as S5) | O | Tuned via speeds. Untuned N-type pair: symmetric η = 0.513 (`TESTS:3494`) | **Theorem E** [ref, bounded: free periodic band, first-moment lapse]: every finite periodic band has non-universally falling states (`TESTS:3556`). Free box packets: η = 0 as a proxy only (`TESTS:3557`). Doublers at rest: weight 1 [ref-rerun]. O: bound bodies (R9-2), edge population (R9-1) | n/a |
| **Vacuum energy, mean (Λ)** | P | P | P | P | P. The tested class has an empty Fock vacuum: no sea, no pair creation (`C5_R8-2_report.md` H-int) | P. Pure AdS as our bulk: EXCLUDED (`TESTS:3431`) |
| **— shared mean results** | All four ⟨Λ⟩ routes OPEN; Lemma PT within G1–G3; global KP sequestering D(b) (`TESTS:2985-2993`) | ← | ← | ← | ← | ← |
| **Λ fluctuation** | GRW flashes 3.3e-72 Λ_obs (as S5). CQ zero-mean noise excludes only an additive mean source (`C5_R6-4_referee_verdict.md:17`) | Frame-dependent (as S5) | **D(b) under H1/H2/H4:** sub-volume, so δΛ is too large by 1.4e30 (cone) and 1.4e59 (diamond) (`TESTS:3428`) | Cap 8.24e184 (as S5) | Not addressed | N-bound 4.78e122 qubits (`TESTS:3438`) |
| **Records & interference** | F: budget (as S5). Metric-as-record: VIABLE Newtonian window, with prices on all four texts (`TESTS:3410,3416`). 32-decade exclusion falls (`TESTS:3418`) | D(b): classical RP (as S5) | Theorem Q (`TESTS:2975`); frame superposition only under superselection (`TESTS:3310`) | Shared budget | Not addressed (shared budget) | O |
| **Lensing noise** | Passes if records steer nothing (as S5) | One crystal | Ideal 1→1 F (as S5); strict silence O (`TESTS:3427`); V′: a null-inclusive gap forces sub-volume counts (`TESTS:3426`) | One crystal | One crystal, so no realization noise [S8 reading] | O |
| **Per-realization effective law** | n/a | Exists; γ ≤ ½ under W1–W3 (as S5) | D(b): finite orbits (as S5). R5-2: full sums give P(−□)δ, not −k² (`TESTS:3297`); three four-shell symbols unstable (`TESTS:3313`) | Exists; preferred frame | Exists (one crystal). The preferred frame is hidden up to the rapidity budget (reading at Planck spacing: about 45 for a proton; `SUMMARY:574`); no integrated Poincaré sector (`TESTS:3402`) | O |

**Closed since S5 (bounded deaths, no price).**
- B′:
  - R5-1 infinite-stabilizer supports (`TESTS:2971-2974`);
  - the 1+1 two-term scalar link class (auxiliary; `C5_R5-4_referee_verdict.md:13`);
  - literal Lemma V (`TESTS:3425`);
  - everpresent-Λ magnitude on LRL, under heuristic premises (`TESTS:3428`).
- C-box:
  - P/FF box loops (`TESTS:3501`);
  - the pair-sum three-body H (`TESTS:3507-3508`);
  - global box-scattering bridges, conditional (`TESTS:3497`);
  - universal fall on every state of a finite periodic band (Theorem E, `TESTS:3556`).
- Set A: point-particle CQ (Corollary U); e^{ℓ²□} and the scalar subclass (`TESTS:3567`).
- Shared: global KP sequestering (`TESTS:2988`).
- Set E: pure AdS as our bulk; AHS higher-spin dS/CFT (`TESTS:3431-3432`).
- Grid sets: strict-range roots and paths of the shift, in every dimension (`TESTS:3323`).

---

## 3. Price ledger delta since S5 (named only, none adopted)

The v6 delta ends at P14 (`PRICE_NOTE:364-368`); S5 added P15–P23 (`C5_S5_synthesis.md:253-261`).

**Axiom lines.**
- Lattice `AX:37-41`.
- Qubit `AX:45-53`.
- Admissibility `AX:57-61`; reading notes `:63-73`; "not a dynamics axiom" `:116-130`.
- Record `AX:77-83`.
- Qualification `AX:87-95`.

| # | Price (named only) | Text touched | Set | What the refereed record says it buys or costs |
|---|---|---|---|---|
| P24 | **No continuous covariant event rule on LRL can "vary with the nearest-neighbor conditions"** (Theorem Q). Keeping the clause on LRL needs a discontinuous rule, less than full Γ-covariance, or a non-DLR retarded law. S5's pending price, now refereed | Admissibility `AX:60-61`, *via a bridge only*: Q "does not directly refute Admissibility as written" (`TESTS:2977`) | B′ | `TESTS:2975-2977` |
| P25 | **Frame superselection**: make LRL's ensemble-mean law physical by declaring the frame unobservable (decomposable observable algebra) | A new primitive (a superselection rule); arguably Record's "Only records are readable" `AX:82` [S8 reading] | B′ | It excludes an exact mean unitary law in that class; it does not prove decoherence (`TESTS:3310-3314`) |
| P26 | **Box-confined Poincaré matter law**, three parts: (a) non-analytic hopping, super-polynomially but not exponentially local; (b) local-domain boost covariance with a state-dependent rapidity budget η* = asinh(b/m⊥) − \|θ\| and leakage ≤ 2‖1_E ψ‖; (c) graded CAR composition | (a) No axiom text: a Hamiltonian is downstream content needing a bridge or registered primitive (`AX:116-130`; cf. P14 at `TESTS:979-981`). (b) None directly; it gives up integrated covariance. (c) Qubit `AX:47` fixes the one-site M₂(C); the cross-site composition is not stated in `AX` [S8 reading]. It is a price against the campaign's ⊗M₂ reading (`TESTS:3039`) | C-box | It buys an exact undeformed Poincaré algebra for free matter at all N inside the box (`TESTS:3399`). The referee collapses the price to two parts, loss of integrated covariance and loss of analytic locality, plus the hidden universal-coupling cost (`C5_R7-1_referee_verdict.md:209-219`) |
| P27 | **The edge sector**, one of: (a) a gravitating edge whose states fall non-universally (Theorem E), so the edge must stay unpopulated; (b) a gapped edge, threshold ≤ √(m²+b²)/a, with the 2^d − 1 doublers removed; (c) a non-periodic momentum space, i.e. an infinite one-particle tower or loss of uniformly site-tied geometry. R7-1 as written (an inert edge) violates universal coupling | (a)/(b): none (law choice). (c): Qubit `AX:47` at the one-particle level and Lattice `AX:37-41`. The referee narrowed (c): not unconditionally "violate the Qubit axiom" (`C5_R8-2_referee_verdict.md:78`) | C-box | `TESTS:3550-3557`; `C5_R8-2_referee_verdict.md:31-58`; `C5_R7-1_referee_verdict.md:212-219` |
| P28 | **Loop protection**, one of: (a) invariant-mass custodial vertices, an imposed functional condition (infinitely many restrictions on kernels), with no stable Hamiltonian yet and no radiative closure shown; (b) tune the one-loop speed terms back, as in set C | None. A law choice that the supplied structure does not fix "remains a named conditional" (`AX:89-90`) | C-box | (a) `TESTS:3502-3504`; `C5_R7-5_referee_verdict.md:22,34`. (b) `TESTS:3501`. pend: R8-4, R8-5 |
| P29 | **Many-body closure**: connected three-body (and N-body) terms invisible in the two-body sector (Sokolov / Coester–Polyzou), plus the H-P bridge that identifies lattice translations with the Poincaré momentum (P = Q) | H-P: Lattice `AX:37-41` supplies translations, not that identification (`C5_R7-6_referee_verdict.md:85-91`) | C-box | `TESTS:3507-3510`. The packed lattice law is unbuilt; its tails are unproved |
| P30 | **Exact additive momentum on a grid**: graded (fermionic) composition with non-quasi-analytic form factors; or a gauge-constrained qubit encoding restricted to a dynamically invariant sector (Kitaev flux-free) | Qubit `AX:47` (composition, as P26c). [S8 reading] a constraint sector might be read as an Admissibility-type rule; that is unexamined | B, C, C-box | `TESTS:3316-3329,3543-3548`. Strict-range paths and roots are excluded in every dimension (`TESTS:3323`) |
| P31 | **N-type universality by imposition**: equal couplings a_A = a_B and a common matter–graviton cone c_s = c_g | None (tunings/impositions) | C | `TESTS:3486-3494`. Energy-exchanging scattering forces them only under regular collision-invariant hypotheses (`C5_R7-4_referee_verdict.md:31-33`) |
| P32 | **Records as a smeared classical metric (Newtonian CQ)**: a smearing length ℓ_s in about [1e-10 (conservatively 4e-10), 5e-6] m as a new law constant; no graviton; Newtonian-only; a preferred time slicing; built-in decoherence and heating; a source/readout/permanence bridge | Lattice, Qubit, Admissibility, Record (all four), plus the bridge (`C5_R6-4_referee_verdict.md:19`) | A | VIABLE in the stated class (`TESTS:3410-3413`). SUMMARY lists the four physical prices (`SUMMARY:590-594`) |
| P33 | **Covariant CQ must leave the R8-3 subclass.** Give up one of: the common-scalar or GR-normalized spin-2 light-cone form factor; the retarded propagator; the pointwise trade-off (go non-Markovian or correlated); additive decoherence; Gaussianity (jumps or mediators). Or keep a preferred frame | None beyond P32; the preferred-frame option adds a frame to the law | A | `TESTS:3559-3573`; `C5_R8-3_referee_verdict.md:7-19` |
| P34 | **A holographic substrate**: change Lattice's dimension or geometry ({5,3,4}: Planck curvature, 10^62.3 mismatch); D ≤ 3 explicit codes give no local graviton; dS/CFT keeps 3 dims but not the literal Z³; at most 4.78e122 qubits | Lattice `AX:37-41`; Qubit (count); Admissibility locality | E | `TESTS:3430-3439`. Only pure AdS-as-our-bulk and AHS are EXCLUDED; the rest is OPEN |

**Not a price, a trade-off (refereed).**
- V′ (`TESTS:3426`): finite local second moments plus a reciprocal gap that includes the null cone force sub-volume counts.
- [S8 reading] A Lorentz-invariant classical substrate that is silent to light across the null cone cannot give everpresent-Λ's Poisson-size count. A count-based Λ needs null-cone spectral weight. In affine Z⁴ that weight overshoots, to T⁶ (`TESTS:3425`).
- Strict lensing silence is itself OPEN (`TESTS:3427`).

**Worker prices, unrefereed (carried, not counted).**
- R6-5 (`TESTS:3264-3268`): b₀ tuning of 43–49 decades with ≥ 3 joint conditions.
- Law-level CPT would need:
  - inversion in Lattice and Admissibility covariance (`AX:37-41,57-58`);
  - a reversible law;
  - an unbuilt chiral lattice construction.

**[S8 reading] on how the price structure has shifted.**
- **A** now has a gravity–record coupling that works at Newtonian level (P32). Its relativistic form needs one of the P33 escapes.
- **B′** adds P24/P25 and still has no law.
- **C-box** pays no numerical tunings for free matter. Its price is structural instead: P26–P29, plus P28's choice between a custodial condition and C's tunings. Every price in it is a law choice outside the four axiom texts except P26(c) and P27(c). Because the axioms do not fix dynamics (`AX:116-130`), each still needs registration or derivation before use.
- **C** is unchanged, plus P31.

---

## 4. Big open problems, ranked by leverage

"Leverage" means how far a definite answer moves the choice among A, C and C-box (B′ is now low-leverage; B is near-exhausted). Problems 6 and 7 are the largest for the TOE as a whole. They are kept first-class, but no C-box answer decides them.

1. **Does C-box gravity hold for interacting matter?**
   - *The gaps:*
     - an interacting stress tensor (W2);
     - the local-lapse algebra (W4);
     - bound bodies falling universally, i.e. binding energy weighing like mass.
   - *Decides:* whether the box breaks the *gravitational* wall or only the kinematic one.
   - *State:*
     - free universal stress F (R8-2);
     - Theorem E;
     - R7-4's global exclusion is conditional, and C-box must stay outside its hypotheses, i.e. exact only inside the rapidity budget.
   - → **R9-2.**
2. **Do loops with pair creation and gauge fields keep one light cone in C-box?**
   - *Decides:* whether C-box's speeds are protected (price P28a) or tuned (P28b, i.e. back to set C).
   - *State:* P/FF D(b); INV conditional; the obstruction named for gauge fields is that minimal coupling by Peierls phases is point-local (`TESTS:3534`).
   - pend: R8-4, R8-5. No round-9 item, to avoid overlap.
3. **Is the edge populated, and if so, what do we see?**
   - *Decides:* whether Theorem E's wrong-falling states are harmless, excluded, or a dark component.
   - *State:*
     - the literal law has 2^d − 1 mass-m doublers, which fall correctly at rest and feel no box-supported interaction;
     - the gapped edge's ceiling is √(m²+b²)/a;
     - Lemma U box–edge matrix elements exist.
   - → **R9-1.**
4. **Many-body closure with lattice tails.**
   - *Decides:* whether C-box is a theory of matter or a two-body model.
   - *State:* pair sums fail (R7-6); Sokolov is formal; the tail fit leans to a power law over 40–320.
   - → **R9-3.**
5. **Covariant CQ: can A's records be the metric relativistically?**
   - *Decides:* whether A's discreteness does gravitational work without a preferred slicing.
   - *State:* Newtonian VIABLE window; conditional covariant no-go with named escapes.
   - → **R9-4.**
6. **Producing the graviton (first-class).**
   - *State:* every set OPEN (R6-2); C-box supplies a matter law for a graviton to couple to, but no graviton.
   - [S8 reading] The next natural C-box question is the graviton's own box law: does a box-confined spin-2 field keep its TT mass zero under box-matter loops? Proposed for round 10, not drafted here.
7. **The mean of Λ (first-class).**
   - *State:* a premise in every set (R5-3); C-box's tested vacuum is empty.
   - Unchanged.
8. **A qubit realization of the box law.**
   - *Decides:* whether P26(c)/P30 cost anything against the campaign's ⊗M₂ reading.
   - *State:* Kitaev-sector exact momentum (R7-3).
   - → **R9-5.**
9. **d = 3 with rotations.**
   - *State:* suggested only (`C5_R8-1_report.md:127,279`).
   - → **R9-6**, conditional.
10. **B′ effective law.** Demoted (`SUMMARY:596-599`). No item.

**Decision map [S8 reading].**
- **C-box becomes a genuine third option.** This needs R8-4 and R8-5 PASS, R9-2 PASS, R9-1 HARMLESS (some profile) and R9-3 PASS. The result would be a grid with one mode per site and exact relativity inside a finite budget, priced by P26–P29. The graviton would still be supplied.
- **R8-4 or R8-5 FAIL.** C-box keeps exact kinematics only for non-pair-creating matter. Interacting speeds return to set C's tuning.
- **R9-2 FAIL** (bound bodies fall non-universally). The gravitational wall stands for composite matter in C-box unless that is tuned too.
- **R9-1 EXCLUDED for both profiles.** Only P27(c) remains, i.e. an infinite tower, which is set A in lattice coordinates.
- **R9-4 VIABLE.** A's records do gravitational work covariantly, and A's price becomes P32 + P33, with no graviton.

---

## 5. Draft round-9 pre-registrations (readings fixed before any run)

**Rules (as for rounds 2–8).**
- Probes: Opus 5.5 at xhigh.
- Every FAIL, EXCLUDED or no-go goes to the codex gpt-5.6-sol (xhigh) referee before it is recorded.
- Prices are named, never adopted.
- Each probe greps the repository and packet for prior art first, and counts each match once.
- Hypotheses are stated before titles; excluded outside realizations are listed.
- Numbers from memory are labelled RECALLED unless verified.

**Overlap check against R8-1, R8-4 and R8-5.**
- R8-1 builds the two-body algebra and leakage in d = 1 and d = 2, and excludes W1–W4, N ≥ 3 and d = 3 (`C5_R8-1_report.md:34-44`).
  - R9-2 uses R8-1's law for the stress tensor only.
  - R9-3 is N = 3.
  - R9-6 is d = 3, conditional on R8-1's referee.
- R8-4 builds the INV Hamiltonian. No R9 item builds pair-creating vertices.
- R8-5 covers gauge fields. R9-1 conditions on R8-5's coupling form but builds no gauge field.

**Priority.** R9-2, R9-1, R9-3, R9-4, R9-5; R9-6 conditional.

---

**R9-1. Edge-sector population: are the wrong-falling edge quanta harmless, observable, or dark-matter-like?**

- **Plain question.** Theorem E says every finite periodic band has states that fall the wrong way. In C-box they live outside the box, in the edge. The literal law also has 2^d − 1 copies of each particle at the zone corners, with the same mass m. These fall correctly at rest and feel no box-supported interaction, only gravity. Does anything put particles in the edge? If so, what would we see: a violation in lab free-fall tests, a cosmic relic, or something that behaves like dark matter?
- **Setting.**
  - R7-1/R8-2's free law in d = 3, with two edge profiles:
    - (L) literal, with doublers;
    - (G) gapped, edge threshold E_e ≤ √(m² + b²)/a.
  - Gravity: R8-2's universal box⊕edge stress at linear order, with the first-moment lapse.
  - Interactions: box-supported and number-conserving (R7-1/R8-1).
  - Lattice spacing a is a parameter; a = ℓ_P is a reading.
  - Excluded: pair-creating vertices (R8-4). Gauge couplings are treated conditionally: (G-in) gauge vertices box-supported; (G-out) point-local Peierls coupling that reaches the corners. Take the form from R8-5 if it has reported.
- **Prior art (count once).**
  - R8-2 (`TESTS:3550-3557`; `C5_R8-2_report.md:64-70,130-131,152,177-178`);
  - the referee's leakage correction (states near the face couple with small q; `C5_R8-2_referee_verdict.md:29`);
  - Theorem E scope (`:47`);
  - O2 Lemma F (`C5_O2_report.md:118`);
  - R7-1 leakage (`TESTS:3399`);
  - the I2 zone average (`SUMMARY:403-405`);
  - MICROSCOPE, as cited at `C5_R8-2_referee_verdict.md:66`.
- **Probes.**
  - (a) **Production.** Compute the rate of edge population by:
    - (i) gravitational box→edge transitions through Lemma U matrix elements, for matter near the face and for a thermal gas at temperature T;
    - (ii) thermal equilibrium at an early-universe temperature T_max (a parameter);
    - (iii) gravitational particle production in an expanding background (comparator literature RECALLED unless verified);
    - (iv) under G-out, ordinary gauge production of corner copies.
  - (b) **Fall and clustering.** For each populated edge state, give the A(k) tensor of Theorem E and the energy-weighted means. Then:
    - (1) the admixture η in test bodies against 1e-15;
    - (2) a relic gas's density, equation of state, and whether it clusters like cold dark matter or falls up or anisotropically;
    - (3) for doublers under G-in: a gravitationally-only interacting mass-m copy of every species. State the dark-matter equivalence-principle bound used (verify or label RECALLED).
  - (c) **Momentum balance.** Theorem E's Ṗ contains dΓ(εA). Identify where momentum goes in a uniform field (into the field, or not conserved), i.e. active versus passive mass.
  - (d) Name the price for each outcome.
- **FIXED readings, per profile (L, G) and gauge case:**
  - **HARMLESS:** computed edge population, for every T_max up to a stated bound, stays below every stated observational bound (η < 1e-15; relic Ω_edge below a stated limit), checked.
  - **EXCLUDED:** a computed population violates a stated bound for every parameter in the profile class (refereed).
  - **DARK-CANDIDATE:** a computed relic abundance can equal Ω_DM in a stated parameter range without violating the stated bounds, including a dark-matter EP bound. Recorded as a lead, not adopted.
  - **OPEN:** otherwise.
- **Expectation.**
  - G: HARMLESS for T_max well below E_e (Boltzmann suppression; E_e is Planckian for b of order one); OPEN near Planckian T_max.
  - L under G-out: EXCLUDED (charged mass-m copies of the electron).
  - L under G-in: OPEN, leaning HARMLESS (purely gravitational production), with a DARK-CANDIDATE risk worth computing.

---

**R9-2. The interacting stress tensor on the box, and the fall of bound bodies (plus the free shear mass)**

- **Plain question.** Gravity must pull on binding energy exactly as on rest mass. MICROSCOPE tests this to about 1e-15 for bodies whose binding fractions differ. R8-2 built a universal stress only for free particles. Is there an exactly conserved stress for the *interacting* box law whose bound states fall with weight one? Separately, does R8-2's free box⊕edge stress bring back the E_g shear mass that free lattice matter generates (V3)?
- **Setting.**
  - The law: R8-1's repaired two-body law (d = 1, d = 2), conditional on R8-1's referee. If R8-1 is not confirmed, use the d = 1 BT law as repaired per the R7-1 referee (`C5_R7-1_referee_verdict.md:93-104`).
  - The free stress: R8-2's Construction A.
  - Gravity: first-moment lapse coupling.
  - Test bodies: two bound states with different binding fractions (vary λ or κ), at rest and moving within the budget.
  - Excluded: pair creation (R8-4), gauge fields (R8-5), N ≥ 3 (R9-3).
- **Prior art (count once).**
  - R8-2 (`TESTS:3554-3557`);
  - R7-1 W2/W4 (`C5_R7-1_referee_verdict.md:237-250`);
  - R7-4 Lemma 1 and the conditional exclusion (`TESTS:3496-3497`; `C5_R7-4_referee_verdict.md:35-55,75`);
  - R7-6 instant form and P = Q (`TESTS:3508-3509`);
  - V3 μ_E = 1.97038864e-3 per cell (`PRICE_NOTE:290-295`);
  - the RN L1 seagull correction (`PRICE_NOTE:341-352`);
  - O2 Lemma F.
- **Probes.**
  - (a) **Free shear.** Compute the uniform-strain (E_g, T_2g) susceptibility of R8-2's box⊕edge stress for profiles L and G, against V3's μ_E. Does the edge carry it?
  - (b) **Interacting stress.** Construct T_int^{μν} for the two-body law with these properties:
    - symmetric, Hermitian, quasi-local (tails stated);
    - an exact linear Ward identity on the two-body box sector;
    - ∫T⁰⁰ = H;
    - first energy moment = the interacting K.
  - (c) **Bound-body fall.** Compute the operator identity for Ṗ in a uniform lapse (Theorem E plus the interaction term), the acceleration of each bound state, and η between two binding fractions, at rest and in motion.
  - (d) **R7-4's hypotheses.** Identify which of R7-4's global hypotheses the construction violates (self-adjoint exponentiating D; Møller intertwining). State the rapidity range on which (b) is exact.
- **FIXED readings.**
  - **PASS:** (b) and (c) met, with computed η between two binding fractions below 1e-15 at linear order (or exactly zero), checked.
  - **FAIL:** a refereed no-go that no stress with (b)'s properties exists for box-supported two-body interactions in a stated class; or a computed bound-body η > 1e-15 that no choice in the class removes.
  - **INCONCLUSIVE:** otherwise.
  - (a) is reported as **SHEAR-PRESENT / SHEAR-ABSENT / OPEN**, with the number.
- **Expectation.**
  - (a) SHEAR-PRESENT [S8 reading: Theorem E moves the anomaly to the edge; the zone average still feeds the uniform-strain response].
  - (b)–(c): INCONCLUSIVE, leaning PASS in d = 1. BT bound states have H = √(M² + P²), so a stress built as the mass-operator density should give weight one at rest. The risk is the locality of that density, and a global-exponentiation requirement sneaking back in.

---

**R9-3. Sokolov-packed three-body box law, built and checked on the lattice (d = 1)**

- **Plain question.** For three bodies, adding up pair interactions breaks relativity (R7-6). The textbook cure, Sokolov packing, adds connected three-body terms so the algebra closes and far-apart particles stop affecting each other. Does the cure work on the lattice, with tails that still fall faster than any power?
- **Setting.**
  - d = 1, three spinless fermions on a ring.
  - The pair law: R8-1's (or the R7-1-referee-repaired) pair law, with R7-6's plateau and box.
  - The packed H_S and K_S are built as explicit operators, not formally.
  - Excluded: d ≥ 2, pair creation, gravity.
- **Prior art (count once).**
  - R7-6 (`TESTS:3506-3510`; `C5_R7-6_referee_verdict.md:52-67,93-137`);
  - Keister–Polyzou, Coester–Polyzou, Reichelt–Schweiger–Klink, as cited there;
  - R7-1 Lemma Sm (`C5_R7-1_referee_verdict.md:131-137`).
- **Probes.**
  - (a) Construct H_S, K_S on the three-body box sector.
  - (b) Check [K,P] = iH, [K,H] = iP and [H,P] = 0 on rings of at least three sizes.
  - (c) **Cluster separability.** Translate one particle by r over at least 1.5 decades. Measure ‖(H_S − H_{12} ⊗ 1 − 1 ⊗ h₃)ψ_r‖ and the same for K.
    - Pre-registered model comparison: an information criterion on log residuals over the full range, super-polynomial (e.g. exp(−c r^β)) against a power law.
  - (d) Measure the real-space tails of H_S − H_BT and of the packing unitary.
  - (e) Check the trimer invariant mass at P = 0, ±P₁, ±P₂.
- **FIXED readings.**
  - **PASS:** (b) residuals → 0 with L; (e) drift at the discretisation floor; (c) and (d) super-polynomial by the pre-registered comparison; checked.
  - **FAIL:** a refereed proof that, in a stated class (box-supported pair interactions, smooth plateau), the connected term or the packing unitary has power-law or slower tails, or that cluster separability fails.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE. The algebra should close by construction; the tails are the real risk, since the R7-6 referee found a power law fits better over 40–320 (`C5_R7-6_referee_verdict.md:125-128`).

---

**R9-4. Covariant CQ gravity outside the R8-3 subclass: spacelike-supported, spin-separated and non-Markovian kernels (set A)**

- **Plain question.** Smeared classical gravity works at Newtonian level (R6-4). Its simplest relativistic forms cannot keep light bending, finite radiation and a quiet vacuum all at once (R8-3). The no-go lists what it does not cover. Test the cheapest member of each uncovered class.
- **Setting.** Linearized, translation-invariant Gaussian CQ models; variants:
  - (i) **Spacelike-supported kernels** [S8 suggestion]. Noise kernels Lorentz-invariant and supported on spacelike transfer q² > 0 only.
    - Reason: R8-3's vacuum divergence (Lemma 1) lives on the future timelike cone, where pair creation needs q. Static Newtonian exchange is at q⁰ = 0, which is spacelike.
    - The question is the null cone, where radiation and lensing live.
  - (ii) **Spin-separated.** Spin-2 is GR-normalized at the light cone; a separate scalar kernel carries the decoherence and diffusion.
  - (iii) **Non-Markovian.** Temporally correlated kernels that violate the pointwise additivity H3′ while keeping complete positivity.
  - (iv) **Preferred frame.** R8-3's search target 1e-8 to 5e-6 m, with D₀'s excess near the null cone computed.
- **Prior art (count once).**
  - R6-4 (`TESTS:3409-3418`; `C5_R6-4_referee_verdict.md:5-25`);
  - R8-3 (`TESTS:3559-3573`; `C5_R8-3_referee_verdict.md:5-19`);
  - R4-4 Lemma N (a BMV-type positive result excludes every variant; `TESTS:2935`);
  - Bedingham and Tumulka (as cited in `C5_R8-3_referee_verdict.md:5`);
  - OWD's trace-only kernel (`:13`).
- **Tests.**
  - complete positivity at finite c;
  - γ = 1 and Shapiro delay;
  - c_T (GW170817), and finite radiation (Lemma 3's light-cone log);
  - a finite vacuum-excitation rate (Lemma 1);
  - decoherence and diffusion against R6-4's bounds: Cs-133 for 70 s; LPF as a γ = 1 prediction; torsion with the corrected integration σ_a² = (48π/5)G²D₂/(RT);
  - the Newtonian limit must land in R6-4's window.
- **FIXED readings, per variant:**
  - **VIABLE:** passes all stated tests with named prices.
  - **EXCLUDED:** violates a stated bound or is inconsistent, for every parameter in the variant (refereed).
  - **OPEN:** otherwise.
- **Expectation.**
  - (i) OPEN. The risk is at q² = 0: radiation and lensing sit on the support's boundary, and Lemma 3's log may return.
  - (ii) OPEN; the scalar channel's lensing contribution needs a computed bound.
  - (iii) OPEN.
  - (iv) OPEN, with a computed window, or EXCLUDED.

---

**R9-5. Box-confined Poincaré on a qubit lattice (⊗M₂), with honest sector accounting**

- **Plain question.** Every box PASS uses fermion modes, which compose across sites with signs. The campaign's reading of Qubit is one qubit per site with the plain tensor product. Can the free box law live on qubits? R7-3 put R6-1's witness into the flux-free sector of a Kitaev spin model. Does the same work for R7-1's box law? What lives in the other sectors, at what energy, and what does it cost?
- **Setting.**
  - ⊗_{Z^d} M₂(C), d = 2 (d = 3 if cheap). Two routes:
    - (A) a Kitaev honeycomb or brick-wall model whose matter Majoranas carry the box dispersion in the flux-free sector. Massive box dispersion needs a gap-opening term; state which.
    - (B) a gauge-constrained fermion encoding (Bravyi–Kitaev superfast or Chen–Kapustin–Radičević), with the constraint sector counted.
  - Excluded: interactions beyond R7-1's free law; gravity.
- **Prior art (count once).**
  - R7-3 (`TESTS:3543-3548`; `C5_R7-3_referee_verdict.md:5-35`);
  - R6-1 (`TESTS:3316-3329`; `C5_R6-1_referee_verdict.md:17`);
  - R7-1 (`TESTS:3398-3407`);
  - R8-2 doublers and edge (`TESTS:3552-3553`).
- **Probes.**
  - (a) The explicit spin Hamiltonian, with norm-certified super-polynomial tails (the gap the R7-3 referee named).
  - (b) R7-1's free box algebra on the invariant sector at every particle number, checked.
  - (c) The complementary sectors: vison and defect energies and dispersions; whether they form a non-Poincaré, edge-like sector; and whether sector-connecting local operators (a single σ^z flips two fluxes) are generated by the dynamics.
  - (d) Name the price: sector restriction, a constraint, and the Qubit-text question in P26(c).
- **FIXED readings.**
  - **PASS:** an explicit quasi-local ⊗M₂ law (tails certified) whose stated invariant sector carries the exact free box Poincaré algebra at every particle number, with the complementary sectors' gap and dynamics computed and the price named, checked.
  - **FAIL:** a refereed no-go for ⊗M₂ quasi-local laws carrying the free box algebra on a stated class of sectors.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** INCONCLUSIVE overall. The flux-free algebra is likely: the Kitaev map is exact there, and the law is free. The risks are certifying the tails and a vison sector whose gap sets a new, possibly low, edge-like threshold.
- **Context [S8 reading].** `AX:47` fixes the one-site algebra and states no cross-site composition. Whether graded composition is a price on the axiom text, or only on the campaign's ⊗M₂ reading (`TESTS:3039`), is an owner question this probe does not settle.

---

**R9-6 (conditional: run only if R8-1's referee confirms the d = 2 construction, with or without corrections). The d = 3 rotation-multiplet box law**

- **Plain question.** R8-1 (pending) builds the interacting two-body box law in d = 2 with a p-wave doublet and a spin term. In d = 3 the channel becomes a p-wave triplet, and the spin term becomes (P × S)/(M + H) (suggested, `C5_R8-1_report.md:127`). Separately, the box is a cube, and finite rotations push corner states out of a cube. Does the full ten-generator algebra close in d = 3? What is the rotation budget?
- **Setting.**
  - d = 3, with g_a(q) = q_a b(|q|²) for a = 1..3.
  - The exact region is taken in two forms: (i) the cube |k_i| < b; (ii) the inscribed ball |k| < b.
- **Prior art (count once).**
  - R8-1 (pending; `C5_R8-1_report.md:22-44,127,258,279`);
  - R7-1 (`TESTS:3398-3407`);
  - the R7-1 referee's d ≥ 2 channel requirement (`C5_R7-1_referee_verdict.md:99-104`).
- **Probes.**
  - (a) All 45 commutators of {H, P_i, J_i, K_i} in the canonical chart, with the spin term.
  - (b) Lattice spectrum: the bound triplet's invariant mass against |P| and direction, at three L.
  - (c) Finite-rotation and finite-boost leakage for the cube and for the ball. Give the rotation-angle budget, and prove a 2‖1_E ψ‖-type bound for rotations.
  - (d) The cubic anisotropy of the bound state where only the cube, not the ball, is exact.
- **FIXED readings.**
  - **PASS:** (a) closes to a stated tolerance; (b) the mass is P-independent to converging precision; (c) leakage bounds proved and checked for rotations and boosts.
  - **FAIL:** a refereed obstruction to the d = 3 interacting algebra on the box sector.
  - **INCONCLUSIVE:** otherwise.
- **Expectation.** PASS in the canonical chart. Lattice-native checks are likely resolution-limited, as in d = 2 (`C5_R8-1_report.md:258`), so INCONCLUSIVE overall is likely. [S8 reading, elementary] On the ball, finite rotations preserve |k|, so the rotation budget is unlimited. Only boosts leak.

---

## 6. Caveats

- **Same family, unrefereed.** The set construction for C-box and E, the table cells marked "[S8 reading]", the price numbering P24–P34 and the rankings are S8's. Every verdict quoted is a codex verdict at the cited line.
- **Pending.**
  - R8-1's worker claims (repair in d = 1 and d = 2, interacting leakage, the ¼-factor dispute) are not verdicts.
  - R8-4 and R8-5 have no report here.
  - R9-2, R9-3 and R9-6 depend on R8-1's referee; R9-1 depends partly on R8-5's coupling form.
- **Not refereed at all.** R6-5 (worker; no referee recorded).
- **Scale bridge.** Every rapidity budget in Planck units uses a = ℓ_P, which the axioms leave as an open gate (`AX:189-190`).
- **The sets are still not exhaustive.** Relational and non-commutative constructions outside D's class stay unexamined (`C5_S5_synthesis.md:579`).
- **The pre-registration drafts are proposals for the driver.** Their readings are fixed here so they cannot be adjusted after a run; the driver may reorder or drop items.
