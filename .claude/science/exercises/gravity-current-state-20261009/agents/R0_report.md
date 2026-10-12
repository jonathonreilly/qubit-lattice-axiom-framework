# Lane R, probe R0: prior art (own repo and literature)

**Who and when.** Claude Opus 5.5, 2026-10-10, 10:28–10:45Z.
- Literature was checked by one same-family subagent (Opus 5.5, xhigh) with web access. It downloaded PDFs to `R0/downloads/` (never executed) and extracted text to `R0/text/`.
- I re-read six key quotes in the extracted text myself.
- **V** means verified in fetched text; **M** means from memory, unverified.
- Nothing here is refereed, and no repository file was edited.

**Labels.**
- **proved:** a theorem in a landed or sol-confirmed note, within its own scope.
- **checked:** a computation in such a note.
- **suggested:** an argument; mine unless attributed.
- **reading:** an interpretation.
- **comparator:** literature.

**Source status.**
- **"Main"** means landed. Mostly `proposed_retained` or conditional-support, and **unaudited**.
- **"PR #9363"** means branch `origin/claude/toe-viability-probes-20260927`. It is sol-confirmed (codex gpt-5.6-sol) but **not landed and unaudited**.
- **The 09-29 wall exercise** on that branch is same-family and unrefereed.

---

## 0. Bottom line in plain words

1. **Lane R has been run here before, under another name.** It was the "tensor / constraint route":
   - a note on main dated 09-14;
   - probes 10–21 on PR #9363 (09-28/29);
   - the 09-29 gravity-wall exercise.

   It used lane R's object: a symmetric tensor on finite slots of Z³, with exact local Gauss laws. One is a vector "momentum rule", ∂_iE_ij = 0. The other is a scalar "time rule", tr R(h) = 0.

2. **What it found** (bounded to harmonic models on the supplied tensor complex, with finite slots and PSD forms; proved there):
   - With every transverse slide exact, the spin-2 mode is protected but soft: ω = O(q²).
   - With both laws exact on compact (finite or clock) variables, every frequency is O(q³).
   - If the TT waves are light-like in every direction, a light-like mode with helicity ±1 content comes with them, whatever residual symmetry is kept.
   - Two pure light-like TT modes and nothing else gapless appear only in a weakly gauge-invariant comparator with continuous, unbounded variables (Gu–Wen's "N-type").

3. **The literature agrees, independently and in its own models (V).**
   - Pretko's classification of rank-2 Gauss laws: scalar charge has 5 polarizations, linear; traceless scalar has 4, linear; vector has 3, k²; traceless vector has 2, k³.
   - Xu–Hořava: in the z = 2 phase "the linear dispersion is ruled out by the gauge symmetry and the lattice symmetries".
   - Gu–Wen 2009: the L-type model gives helicity ±2 only at k³, which they call reliable. The N-type model gives ±2 only at k, and they write that "our result for the N-type model is not reliable". Gu–Wen 2006's linear claim uses the same total-derivative term.
   - **No paper was found** that shows a local lattice model with linear dispersion and ±2 alone (a search result, not a theorem).

4. **Protection, criterion (ii), passes in the literature's sense, with qualifiers (V).**
   - Emergent gauge invariance plus self-duality protects these phases against weak perturbations, with no symmetry needed.
   - Rasmussen–You–Xu: the gapless phase "is not stable to arbitrarily strong perturbations".
   - Gu–Wen's robustness is worded as expectation.
   - The spin-ice photon (Hermele–Fisher–Balents) is the clean analogue.

5. **Criterion (iii), universal coupling, is where prior art is most negative.**
   - **The lattice models' sources (V).** The "graviton" couples to the emergent gauge charge (fractons, vector charges, constraint defects), not to all matter's T^μν. Pretko reads the scalar charge as T⁰⁰, but has no momentum or stress coupling, and his attraction is "generically short-ranged".
   - **Marolf (V).** Universal coupling to energy, with energy readable as a boundary flux, cannot emerge from local kinematics, "on a lattice or in the continuum", without Lorentz or translation invariance, except where the bulk is frozen. It explicitly places "no constraints on … strictly linear spin-2". So it bites beyond linear order, which lane R's (iii) does not test.
   - **Own repo.** Route F6 (rank-2 / fracton Gauss law) is "blocked-equivalent to K3a's exact interacting stress" (`ROUTES.md:21`). For momentum to source the vector law, matter's momentum density must be an exactly conserved local charge, and none is known for interacting matter on Z³ (K3a: a bounded obstruction, refereed not-a-theorem).
   - **The 09-14 note (proved, isotropic quadratic comparators only).** A scalar (energy) source gets only contact energy under the strongly invariant Hamiltonian. It gets the attractive inverse-Laplacian kernel only under the weakly invariant H_N, the N-type structure that finite variables do not carry. Gu–Wen say the same: N-type gives m₁m₂/r², L-type does not (V).

6. **Criterion (iv), the speeds, is never derived in the literature (V).**
   - The spin-ice photon speed is √(UK)·a₀, a free parameter that goes to zero at the RK point.
   - Sindoni: lattice Lorentz recovery for Gu–Wen needs "custodial symmetry" or fine tuning, and its extra polarizations are "made massive by hand".
   - **Own repo** (probe 4, proved counting): on Z³ with continuous time, the relabelling-invariant TT speed is a free coefficient, which costs at least one speed tuning beyond P0. Only on the hypercubic Z⁴ or Z³×Z_τ block with 4D linearized relabellings is the invariant leading action unique (Euclidean Fierz–Pauli, TT speed 1).

7. **Prediction for lane R from prior art** (suggested):
   - (i) and (ii) pass together only with gapless ±1 (and 0) partners (scalar-charge type), or (i) fails on "linear" (vector charge; both laws, compact).
   - (iii) is blocked-equivalent to K3a for momentum. Its energy half needs the N-type (weak) structure.
   - (iv) needs at least one speed tuning off the hypercubic block.

   This matches the supervisor's registered expectation (`TESTS.md:716-721`), with one correction. Gu–Wen's *controlled* model fails (i): it is cubic. Only the uncontrolled N-type is linear with ±2 alone.

8. **A gap in the fixed reading, flagged before results** (the reading itself is not changed). Criteria (i)–(iv) do not exclude extra gapless modes. The packet's wall target does: "exactly two TT polarizations … no other gapless mode coupled at gravitational strength", and "extra gapless partners" is listed as a forbidden weakening (`WALL.md:86,89`).
   - A Pretko scalar-charge model meets (i) and (ii) as worded while carrying linear ±1 partners.
   - The 09-29 exercise found such partners excluded by the double pulsar unless they are about 12× faster than the spin-2 mode. That is same family and unrefereed, and is in `gravity-wall-finite-records-20260929/SUMMARY.md:66-73` on PR #9363.
   - R2 should report partner content and speeds whatever the verdict.

---

## 1. Own repo: what was already tried

### 1a. On main

| Item | Where | Status | What it says (its scope) | Bears on |
|---|---|---|---|---|
| Finite-clock tensor constraints on Z³ (the Gu–Wen complex, re-derived) | `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` | proposed_retained; conditional support; review pending (`:3,7-9`) | **Proved/checked.** (a) The commuting vector law G_j = ∂_iE_ij and scalar law S = tr R(h) leave exactly two TT pairs (`:62-67`). (b) Strongly invariant H_L: ω² = Jg k⁶. Weakly invariant linearized gravity H_N: ω² = Jg k² (`:69-74`). (c) Any regular compact-character H with both lifted gauge actions has all frequencies O(k³), "not a no-go for qubits, emergent nonlinear gauge symmetry or strongly interacting constraint phases" (`:186-216`). (d) Finite penalties on H_N give det K < 0 and a Jordan chain (`:260-278`). (e) A static scalar source gets contact energy only under H_L, and an attractive inverse-Laplacian kernel under H_N (`:280-296`). (f) Gu–Wen's N-type gap is "explicitly uncontrolled" (`:372-375`) | (i), (ii), energy half of (iii) |
| Tensor first moments | `docs/TENSOR_HELICITY_RATIONAL_CERTIFICATES_AND_TRACE_ELIMINATION_BOUNDED_THEOREM_NOTE_2026-09-29.md` | proposed_retained, conditional | **Proved:** ⟨H1⟩ ≥ ⟨TT⟩/4 for linear symmetric tensor moments (the landed form of probe 20's lemma) | (i): partners |
| Mixed constraint bracket | `docs/FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-30.md` | proposed_retained, conditional | **Proved:** no regular finite-support canonical tensor jet (stated stencils, cubic covariance) satisfies the next mixed lapse/shift identity at momentum degree 2 | closure beyond linear order |
| Tensor-electric dynamics | `docs/DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_…_2026-09-24.md`; `docs/DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_…_TWELFTH_ORDER_…_2026-09-24.md` | conditional, unaudited | **Proved/checked:** nearest-neighbour two-site generators that keep every vector row freeze every slot; a soft vector constraint generates curvature moves only at 12th order | (ii); the speed scale in (iv) is a high-order coefficient (reading) |
| U(1) photon from Z³ qubits (the framework's spin-ice analogue) | `docs/U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md`; `docs/THE_PURE_SPIN_HALF_LINK_MODEL_…_QUADRATIC_TRANSVERSE_MODE_NOT_A_MAXWELL_PHOTON_…_2026-09-04.md`; `docs/DYNAMICS_CLAUSE_CHARGES_ARE_GAUSS_DEFECTS_…_2026-09-24.md:4` | conditional | **Checked:** an ice rule plus ring moves gives a gapless deconfined phase, quadratic at the RK point. Charges are Gauss defects, and no qubit carries a covariant charge | analogue for (ii); (iii): charges are defects |
| Linear "member" (continuous variables) | 09-21 `…ANGLES_ARE_THE_TILT_…_PRICE_IS_A_CONSERVED_STRESS…`:4; block 112 `…CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA…`; block 135 `…ONE_LIGHT_CONE_EXACTLY_…_IFF_ALPHA_EQUALS_K_OVER_FOUR…` | conditional, unaudited | **Proved (supplied model):** two TT modes with one nearest-neighbour dispersion. The lattice constraint algebra closes only at β = −α. Coupling to the walker's stress keeps the books iff α = K/4 | (iii), (iv) for a *supplied* continuous field: the "2026-09-24 comparator", the only working Einstein-spectrum construction (probe 21 `:69`) |
| Gravity-sign gate | `docs/GRAVITY_SIGN_FROM_REFLECTION_POSITIVITY_…_2026-06-08.md:22-32` | bounded, conditional | The healthy branch needs the conformal wrong-sign sector "removed as gauge by an actual diffeomorphism or equivalent gauge structure". This is lane R's question | (ii), sign in (iii) |
| June universal-GR lane | `docs/UNIVERSAL_GR_BLOCK_CONSTRAINT_INTERPRETATION_NOTE.md:11-30`; `docs/UNIVERSAL_GR_SAKHAROV_…_METRIC_DOF_POSIT_…_2026-06-17.md:1,15` | audited_conditional | The block-to-constraint step is "a renaming/interpretation step". No redundancy is derived, and the residual wall is a metric posit | context |

### 1b. PR #9363 (sol-confirmed, unaudited, not on main)

All of these are bounded to the supplied tensor complex, harmonic comparators and finite slots. None tests one qubit per Z³ site under the axioms (probe 21 scope `:4`).

| Probe | Note prefix (line 4 = scope) | Result (as stated) | Bears on |
|---|---|---|---|
| 9 | `A_NEIGHBOURHOOD_CONSTRAINT_ON_Z3_QUBITS_…` | Re-check of the main U(1) lane. An ice rule on the Z³ sites with one odd coordinate acts as a nearest-neighbour constraint, and ring moves keep it | how a Gauss law sits in Lattice and Admissibility (reading) |
| 10 | `ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_…` | **Proved:** one qubit per slot with the momentum rule exact gives an f-sum bound ≤ C\|q\|⁴; a light-cone lowest mode needs S(q) ≤ C q³/c | (i) for qubit slots |
| 11 | `THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_…` | **Proved:** the curl of a photon triplet is linear in the helicity-2 channel. The isotropic sum-rule identity 4v₁ = v₂ + 3v₀ ties helicity-1 to helicity-2 | partners |
| 13 | `THE_LAMBDA_ONE_QUESTION_…` | **Proved:** DeWitt is PSD on ker G and only weakly invariant. Weak invariance adds nothing in lifted clock encodings, so finite slots need a non-additive time gauge | why N-type cannot be finite |
| 14 | `A_QUANTUM_LINK_DEFORMATION_OF_THE_LINEAR_SCALAR_CONSTRAINT_…` | **Proved:** the scalar quantum-link constraint needs S ≥ 2 per slot, and is not first-class on the whole surface | Qubit price |
| 15 | `THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_…` | **Proved:** Einstein–Hilbert is exactly invariant, but the TT f-sum is ≤ C q² | (i) |
| 16 | `THE_PHOTON_TRIPLET_COMPOSITES_PARTNERS_…` | **Proved:** no gauge-invariant local harmonic term gaps the partners (Proca or non-local terms would). Every tested constraint set that removes ±1 also removes the TT-visible first moments | (i), (ii) |
| 17 | `AN_EXACT_ADDITIVE_GAUSS_LAW_ON_DISCRETE_SLOTS_…` | **Proved:** an exact additive law needs its variable stored on every slot it touches; only pure assignments carry the full rules | carrier of the redundancy |
| 18 | `BREAKING_THE_MOMENTUM_RULE_…` | **Proved/checked:** breaking the vector law makes TT linear, but the ±1 partners move too: c₁² = c₀²/2 + c₂²/4 | partners; the repo's analogue of Pretko's scalar charge (reading) |
| 20 | `EVERY_GAUSS_LAW_COMPATIBLE_MOVE_…` | **Proved:** the quarter lemma, with Lemmas H and H2 | (i) |
| 21 | `THE_TENSOR_COMPLEX_ON_FINITE_SLOTS_…_WHATEVER_THE_RESIDUAL_SYMMETRY_…` | **Proved:** (i) all transverse diffeomorphisms exact gives ω_TT = O(q²); (ii) TT linear in every direction gives a linear mode with ±1 weight on a dense set (`:28-47,219-239`). Prior art: Xu–Hořava, Gu–Wen, Hořava, Pretko, Dubovsky (`:65-95`) | **the central prior result for R2** |
| 4 | `IF_THE_MEMBERS_LEADING_ACTION_RESPECTS_THE_HYPERCUBIC_TICK_SURFACE_…` | **Proved (counting):** space-cubic plus time reversal leaves 2 relabelling-invariant forms with a **free TT speed**. Z⁴ leaves exactly 1 (Euclidean Fierz–Pauli), with TT speed 1 | (iv) |
| 09-29 exercise | `.claude/science/exercises/gravity-wall-finite-records-20260929/SUMMARY.md` | **Suggested or checked; same family; unrefereed.** Partners are excluded unless more than about 12× faster (`:66-73`). The partner face is "the lattice face of Einstein's conformal-factor sign", whose negative weight ground-state systems cannot supply (`:74-84`). Price: (a) continuous unbounded variables, (b) local rules broken at O(1), or (c) a composite graviton with an unnamed mechanism (`:125-140`) | (i), (iii), (iv) |

### 1c. In this packet

- **F6** (emergent gauge redundancy, rank-2 or fracton) is "blocked-equivalent" to K3a: "That matter's charge equals its momentum" (`ROUTES.md:21`; `agents/R1_condensed_matter.md:18`).
- **C2** is likely wounded, because exact slides give ω ~ q² (`ASSUMPTIONS.md:34`; `agents/supervisor_thread.md:30`).
- **The emergent-graviton row** in the candidate pack (`candidate-law-20261008/TEST_LOG.md:540`) says there is no construction.
- **K3a** (`TEST_LOG.md:236-259`) found no conserved momentum in the tested class at O(e). Refereed as NOT CONFIRMED as a theorem; the bounded obstruction is confirmed.
- **The B1 referee:**
  - Weinberg–Witten says only that *some* assumption fails (`agents/B_referee.md:47`).
  - Marolf is "in tension with ordinary microscopic local kinematics" (`:48`).
  - Fractons are "not all … k² or k³" (`:176`).
  - B1 row VIII, condensed-matter emergent gravity, fails on Lorentz invariance, linear dispersion and partners (`agents/B1_report.md:301`).
- **G-C, refereed INCONCLUSIVE:** the no-go covers only frozen picture-I order functionals; the background-free quantum sum is open (`agents/C3_G-C_referee.md:3-5`). This is R3's start.
- **Target and forbidden weakenings:** `WALL.md:86,89`.

---

## 2. Literature (comparators; V/M as marked)

| Source | Redundancy | Gapless modes | Dispersion | Protection | Couples to | Lorentz, speeds, WW |
|---|---|---|---|---|---|---|
| Gu–Wen, gr-qc/0606100 | vector law plus a constraint on the potential, (δ∂² − ∂∂)θ = 0 (V) | claims ±2 only; ±1 and 0 gapped by a semiclassical argument (V) | claims linear (V), via the total-derivative term that 0907.1203 later calls unreliable (V, agent's comparison) | "expected" robust (V) | not treated (V) | not Lorentz invariant. WW evaded because T is not gauge-invariant (V) |
| Gu–Wen, 0907.1203, NPB 863 (2012) 90 | ∂_iE_ij = 0 plus R_ii = 0 on the potential (V) | ±2 only (V) | **L-type: k³, "reliable".** N-type: k, "not reliable" because gapping ±1 and 0 at the nonlinear level may affect ±2 (V; quote re-read) | k³ is robust: a locally invariant H cannot generate the linear term (V); same as the repo's 09-14 bound | violations of R_ii = 0 act as masses; N-type gives an m₁m₂/r² force (V) | — |
| Xu, cond-mat/0602443 and cond-mat/0609595 (PRB 74, 224433) | lattice vector law; A → A + ∂_if_j + ∂_jf_i (V) | ±2 and a scalar (trace) mode, 3 branches (V) | k² (V) | self-duality plus gauge structure; stable against instantons (V) | vector charges (M) | no Lorentz invariance (V) |
| Xu–Hořava, 1003.0009, PRD 81, 104033 | z = 2: ∇_iE_ij = 0. z = 3: adds E_ii = 0 (V) | z = 2: 2 TT plus a scalar. z = 3: 2 only (V) | z = 2: "the linear dispersion is ruled out by the gauge symmetry and the lattice symmetries" (V; re-read). z = 3: k³ | vertex operators irrelevant (V) | vector charges (M) | Lifshitz scaling (V) |
| Pretko, 1606.08857 (Table I) and 1604.05329 | scalar, traceless scalar, vector and traceless vector charge (V) | 5 / 4 / 3 / 2 polarizations; helicity labels M | k / k / k² / k³ (V) | Gauss law plus self-duality; monopoles "are not instantons", so deconfined (V) | fractons and sub-dimensional particles (V) | — |
| Pretko, 1702.07613, PRD 96, 024051 | scalar charge ∂_i∂_jE_ij = ρ (V) | graviton plus "extra gapless gauge modes with no analogue in Einstein gravity" (V) | linear (V) | gauge invariance (V) | scalar charge read as T⁰⁰; no momentum or stress coupling; full GR needs both laws; gravity "generically short-ranged" (V; re-read) | no Lorentz invariance. Appendix B on WW: fractons have no asymptotic momentum eigenstates (V) |
| Rasmussen–You–Xu, 1601.08235 | vector, traceless vector, scalar (and rank 3) (V) | scalar: 5 (V) | k² / k³ / k (V) | Gaussian fixed point plus self-duality; "not stable to arbitrarily strong perturbations" (V; re-read); no symmetry needed for weak ones | gauge charges (V) | rotation invariance assumed; weak breaking does not gap (V) |
| Benedetti–Casini–Magán, 2111.12089, JHEP 05 (2022) 045 | linearized GR written in curvature variables E_ij, B_ij (V) | ±2 (V) | linear (V) | generalized symmetries (V) | matter currents take a "peculiar form" (V) | Linearized GR is "an example of a 'traceless vector charge theory'", with the same conservation laws as Pretko's but different commutators (V; re-read). WW rederived from generalized symmetries. Nothing on emergence (V) |
| Hinterbichler–Hofman–Joyce–Mathys, 2205.12272, JHEP 02 (2023) 151 | biform symmetries (V) | graviton (V) | linear (V) | protected by an electric/magnetic biform anomaly (V) | gapped charged matter is fractonic (V) | linearized gravity has no stress tensor (WW). A UV parent "is unlikely to look anything like a local QFT" (V) |
| Marolf, 1409.2509, PRL 114, 031104 | — | — | — | — | universal coupling to energy as a boundary flux | Cannot emerge from local kinematics unless the bulk is frozen. Holds on a lattice and "requires neither Lorentz-invariance nor translation-invariance". "No constraints on … strictly linear spin-2" (V; re-read) |
| Weinberg–Witten, PLB 96 (1980) 59 | — | — | — | — | — | Loopholes used by emergent models (V via the sources above): no Lorentz invariance; T not gauge-invariant (Gu–Wen); no asymptotic momentum states (Pretko; Nandkishore–Hermele 1803.11196). Jenkins hep-th/0607239 discusses evasion by Lorentz-violating Goldstones (V) |
| Spin ice: Hermele–Fisher–Balents, cond-mat/0305401; Benton–Sikora–Shannon, 1204.1325 | div E = 0, U(1) (V) | 2 photon modes (V) | ω ∝ k with c = √(UK)·a₀ and g = 12J_±³/J_zz². Quadratic at the RK point (V) | "stable to ALL zero-temperature perturbations" (HFB, V) | emergent electric charges (gap ~g) and monopoles (V) | The speed is a non-universal parameter, untied to other speeds (M, inference) |
| Sindoni, 1110.0686 | — | — | — | — | universal coupling needs strong symmetry (§5.3, V) | "each mode will have, in general, different speed". Gu–Wen's Lorentz recovery needs "custodial symmetry" or tuning, and extra polarizations are "made massive by hand" (§7.1, V) |

**One lead from the literature** (the agent's, which I read as a reformulation, not an escape). In Benedetti–Casini–Magán, linearized GR has the *constraints* of a traceless vector charge theory (Pretko: 2 modes, k³) but disperses linearly because its commutators differ.
- A lattice with those commutators and a local H would be the missing model.
- My reading: those commutators are what weak (N-type) invariance with canonical (h, π) produces. So this is the same open N-type question in other variables, not a new route (suggested, unchecked).

---

## 3. Mapping onto (i)–(iv)

Classes are scored against the fixed reading (`TESTS.md:701-714`), each inside its own model. These are not lane verdicts.

| Class (examples) | (i) gapless ±2, linear | (ii) protected vs redundancy-respecting local terms | (iii) universal coupling to T^μν at linear order | (iv) tunings ≤ P0, speeds counted | Other gapless modes |
|---|---|---|---|---|---|
| **Vector law only, strong** (Xu; Xu–Hořava z = 2; Pretko vector; repo probe 21(i)) | **fails "linear"**: k² (V; repo proved O(q²) for harmonic finite slots) | passes: the lowest invariant is linearized curvature (V; repo 09-14 `:203-207`) | Momentum half: A_ij·T_ij is gauge-invariant if ρ_j = T_0j, which needs exact momentum conservation (suggested). On Z³ that is K3a, so F6 is blocked-equivalent. No lapse means no T⁰⁰ (Newton) coupling (suggested) | — | trace scalar (V) |
| **Traceless vector or both laws, strong, compact** (Gu–Wen L-type; Xu–Hořava z = 3; Pretko traceless vector; repo 09-14 H_L) | **fails**: k³ (V; proved in the regular compact class) | passes (V; proved) | Energy half: a static scalar source gets contact energy only (proved, isotropic H_L). Gu–Wen give the m₁m₂/r² force only for N-type (V) | — | none: ±2 only (V) |
| **Both laws, weak, noncompact** (Gu–Wen N-type; repo H_N) | passes in the Gaussian comparator (proved; V) | **not established**: the variables are unbounded; finite penalties give a Jordan chain (proved); authors "not reliable" (V); lifted clocks gain nothing (probe 13) | energy: inverse-Laplacian attraction for a supplied source (proved); momentum: K3a as above | ≥ 1 speed tuning off the hypercubic block (probe 4 T1); unique with speed 1 on Z⁴ with 4D relabellings (probe 4 T2) | none (Gaussian) |
| **Scalar charge** (Pretko; Rasmussen–You–Xu; repo probe 18 analogue) | **passes as worded** (V) | passes for weak perturbations (V); repo probe 16(B) analogous | Pretko: T⁰⁰ only, short-ranged, no momentum or stress (V). Suggested: with ρ = T⁰⁰ the conserved dipole freezes the centre of energy, which is fracton immobility, Pretko's Mach reading. The alternative ρ = ∂_jT_0j makes A_ij·T_ij gauge-invariant, but rest energy then sources nothing (no Newton) | graviton vs matter speed plus partner speeds, all free (V for "free", Sindoni); ≥ 1 | **±1 and 0, linear** (V; repo probes 11/18/20/21) |
| **U(1) spin-ice photon** (helicity 1, analogue) | n/a | passes (V) | emergent charges only (V) | speed free; c → 0 at RK (V) | — |
| **Events, quantum sum** (R3; G-C) | open | open (G-C INCONCLUSIVE, refereed) | open | one cone in law (E1′ scalar) | open |

**Repo against literature** (reading). Every literature model lands where the repo's harmonic theorems put it:
- strong vector law gives k²;
- both compact laws give k³;
- linear TT comes with ±1 partners.

The only linear ±2-only case is weak invariance on noncompact variables. This is consistency between two derivations of the same Gaussian structure, not independent confirmation of the repo's general lemmas.

**Suggested synthesis for (iii).**
- A lattice H that commutes with every local Gauss generator conserves every multipole the law fixes. With energy as the scalar charge, the centre of energy is conserved, so energy cannot move freely: fractons.
- In GR the Hamiltonian is itself a constraint plus a boundary term, and the lapse is gauge.
- So the Newtonian half of universality needs time evolution generated by the constraints. Three earlier findings point at the same thing:
  - probe 12: "only a gauge lapse is GR's";
  - Marolf: kinematic non-locality, beyond linear order;
  - the 09-29 exercise: the conformal-sign face.
- The weak (N-type) structure realizes this, and finite or compact local variables are not known to carry it.

---

## 4. Axiom prices (named only; none adopted)

| What the class needs | Axiom or primitive touched | Source |
|---|---|---|
| An exact local Gauss law as a hard constraint | **Admissibility**, read as the support of the nearest-neighbour distribution, like the ice rule in probe 9 (reading). The vector row uses the six neighbours of a link site in doubled coordinates (09-24 freeze note, `:4`). The scalar row touches all six slot types (probe 17); check its range against "nearest-neighbour" | probes 9, 17; 09-24 |
| A Hamiltonian or transfer law with constraint-respecting moves | outside the axioms: Admissibility "is not a dynamics axiom" (`MINIMAL_AXIOMS_2026-06-29.md:116-123`). A supplied law, already an open gate | axioms memo |
| Six tensor slots per coarse cell | **Lattice** reading: the coarse Z³ of spacing 2, with roles assigned to sites (reading) | probes 9, 17 |
| Spin S ≥ 2 per slot for the scalar quantum-link constraint | **Qubit**: M₂(C) → at least M₅(C) | probe 14 |
| Continuous unbounded (CCR) slots for N-type | **Qubit** (the 09-29 "option A"). One record per site no longer bounds information per site | 09-14; probe 13; 09-29 price (a) |
| The scalar constraint as gauge (energy sources the field; relational time) | **Record and time**: records carry no time (A36); a gauge lapse (probe 12). Beyond linear order, Marolf's kinematic non-locality touches **Lattice/Admissibility locality** and the site tensor product (suggested) | probe 12; Marolf (V) |
| Matter momentum as an exact vector charge | an exact interacting lattice stress (K3a open), or a new primitive making momentum a gauge charge | K3a; F6 |
| One speed with matter | **`kinetic_isotropy_primitive`** (approved: hypercubic Z³×Z_τ), *if* the redundancy includes 4D linearized relabellings (probe 4 T2). **Suggested caveat:** a Euclidean weight invariant under them carries Einstein's conformal-mode sign, so it is not a nonnegative probability weight. That is in tension with Admissibility's "probability distribution", the 09-29 conformal-sign face again | probe 4; RP gate note; 09-29 `:74-84` |
| Gapless partners removed by a negative-weight conformal sector | Admissibility (positivity); "ground-state systems cannot supply" it | 09-29 `:74-84` |

---

## 5. For R1, R2 and R3

- **R2**
  - State the class first: strong or weak invariance; compact or noncompact; vector law, scalar law, or both.
  - Do not re-derive probe 21, the 09-14 bound or Pretko's Table I. Cite them, and re-check only what is used.
  - The open cells are non-harmonic or strongly correlated phases, a softened time rule, composites, and one qubit per Z³ site under the axioms.
  - Always report partner content and partner speeds.
  - On the stiffness-wall terms (suggested): exact gauge invariance of the matter coupling needs an exactly conserved lattice stress, which is K3a. With only approximate conservation, integrating out matter can regenerate a TT mass at the K3a″ size, and the wall returns.
- **R1**
  - The U(1) lane already found that charges are Gauss defects and no qubit carries a covariant charge (09-24).
  - The tensor constraints are already known:
    - an exact additive law stores its variable on every slot it touches (probe 17);
    - one qubit per slot gives a q⁴ bound (probe 10);
    - the scalar law needs S ≥ 2 (probe 14).
  - Suggested open point: a compact Gauss law quantizes the charge in a region, while matter's momentum is continuous. So "matter momentum = vector charge" may also fail on quantization, not only on K3a. Unchecked.
- **R3:** start from G-C's referee scope (`C3_G-C_referee.md:5`). Hinterbichler et al. note that a UV parent of a protected graviton "is unlikely to look anything like a local QFT" (V). That fits the event-sum branch's non-locality, as a reading only.

## 6. Strong-word check

- **"Blocked-equivalent"** is the packet's word (`ROUTES.md:21`), not mine.
- **"Proved"** is used only for results proved in the cited notes, within their scopes. Those notes are unaudited, and the PR #9363 ones are not landed.
- **"Fails" and "passes"** in §3 are per class, inside each model, against the criterion's wording. They are not lane verdicts and not refereed.
- **"Never derived"** (§0 item 6) and **"no paper found"** (§0 item 3) are search results from a ~10-minute verified search, not theorems.
- **My own derivations, all suggested and unchecked by computation:** the (iii) arguments for the scalar-charge and vector-charge classes (ρ = T⁰⁰ vs ρ = ∂_jT_0j), the multipole synthesis, the Euclidean conformal-sign caveat, and the charge-quantization point.
