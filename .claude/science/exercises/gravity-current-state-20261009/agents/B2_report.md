# B2 (framework-first backward reasoning): agent report (Claude Opus 5.5, xhigh; 2026-10-09)

Verbatim. Same-family. Refereed by codex sol: CONFIRMED WITH CORRECTIONS (`B_referee.md`); the corrected statements are in SUMMARY.md §8. Scripts in `scripts/B2/`.

# B2 (framework-first): reasoning backward from gravity to the substrate

**Agent:** Claude Opus 5.5, extra-high effort, lens B2 (framework-first). Same family as the supervisor. Nothing here is refereed or adopted. I did not see B1's work.
**Date:** 2026-10-09.
**Repository:** not edited. Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/B2/`.

**Labels.**
- **proved:** an exact argument given here (elementary unless stated otherwise).
- **checked:** a computation run here, or a computation the repo ran.
- **suggested:** an argument.
- **reading:** an interpretation.
- **comparator:** a literature result. (M) means cited from memory and not re-fetched.

**Evidence status.**
- **landed:** on `origin/main`. All the landed notes cited here are `unaudited` in the ledger.
- **refereed:** codex gpt-5.6-sol, usually CONFIRMED WITH CORRECTIONS (CWC).
- **same-family:** checked only by Claude agents.
- **branch:** `origin/claude/toe-viability-probes-20260927`, closed unmerged. Contested; evidence, not authority.

Paths are relative to the worktree unless they are absolute. "Packet" means `.claude/science/exercises/gravity-current-state-20261009/`. "Pack" means `.claude/science/candidates/candidate-law-20261008/`.

**What I read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- The three approved primitives' notes. The registry has 4 nodes: the axioms plus `scale_reference`, `kinetic_isotropy` and `realized_state`.
- The packet: SUMMARY, WALL, ASSUMPTIONS, ROUTES, APPROACH_REGISTRY, TESTS (all of it), the E1/E23 reports and referees, `supervisor_thread`, R3, R4, the F1a and F1b kills and their referees, and OUTSIDE_VIEW.
- The pack: DECISION_MATRIX, KILL_SHEET, TEST_LOG (K7a, K2a, G0–G0c, K3a, K3a′, K3a″, W1, W2, FR1, FR3) and CANDIDATE_1.
- On the branch:
  - the 09-29 exercise SUMMARY;
  - the viability map's front matter, its long-paths table and its gravity panels (lines 954–1237);
  - the claim scopes of all 22 branch notes;
  - the body of the record-event lapse note.
- Landed: block 122 in full; the 3+1D boost note's theorem, scope and non-claims; the headers of the 09-14 tensor note, the 09-24 oscillator-slot note, the no-per-site-CCR note, the proper-cubic-group note, the graviton-mass identity note and the conformal-class open gate.

---

## 0. What the axioms give and what the gravity work supplied

| Axiom clause (`docs/MINIMAL_AXIOMS_2026-06-29.md`) | Bears on gravity because |
|---|---|
| **Lattice** (:37–41): sites = Z³, nearest-neighbour adjacency, standard translations, proper cubic rotations; no site privileged | It fixes a **discrete** translation group and a **finite** point group. It fixes a label-space Brillouin zone. Space only: no time is supplied |
| **Qubit** (:45–53): M₂(C) per site | Finite local dimension. No exact CCR is possible: `NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` (landed; proved by the trace identity) |
| **Admissibility** (:57–61, reading notes :63–73): one fixed nearest-neighbour rule, covariant under translations and cubic rotations, fixing each site's distribution | Covariance group Z³ ⋊ O (24 proper turns). Not a dynamics: "does not choose a Hamiltonian … define a time metric" (:116–123) |
| **Record** (:77–83): records form, lock one possibility, at most one per site, permanent; only records readable | "A state is a configuration of records" (:92). The formation site and rate, the persistence dynamics and the time metric are open gates (:181–186) |
| Primitives | `kinetic_isotropy`: a hypercubic Z³ × Z_τ regulator, c_t = c_s (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:19–25`). `scale_reference`: a⁻¹ = M_Pl, units only (`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md:15–17, 39–41`). `realized_state`: "the laws do not pick the state; the world does" (`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:21–30`) |

Every gravity object in the repo is supplied, not given by the axioms (WALL.md:113–124): metrics, tensor slots, Hamiltonians, couplings, the member, and the vacuum states.

**Reading.** So "which clause blocks gravity" always means "which clause, together with the supplied structure, blocks the construction that was tried". The blocks below are stated that way.

---

## 1. Requirements and what blocks each one

**The requirements, briefly.**

| | Requirement | Bar |
|---|---|---|
| G1 | Massless helicity ±2, naturally (no tuned counterterm) | m_g ≲ 1e-23 eV ≈ 1e-51 M_P |
| G2 | Exactly two TT polarizations; no other gapless mode at gravitational strength | double pulsar; partners must be ≳ 12× faster (09-29 SUMMARY) |
| G3 | A mediator exists: a dynamical spin-2 field with an Einstein–Hilbert-type kinetic term | — |
| G4 | One cone: c_g = c_γ = c_matter | 1e-15 (GW170817), plus Lorentz tests |
| G5 | Universal coupling to the total conserved stress, binding energy included | 1e-15 |
| G6 | Newton and GR: 1/r, bending ×2, nonlinear closure (constraint algebra) | — |
| G7 | Stable, coherent propagation over Gpc | no exponential growth; no mass-type noise |
| G8 | Locality | down to about 1e-19 m |
| G9 | Small Λ, and no TT tadpole | — |
| G10 | Quantum consistency | Bell; positivity and unitarity; the conformal factor |

### The blocks

**Grades.**
- **P:** the block is proved within its stated class.
- **C:** checked in models.
- **S:** suggested.

| Req | Blocking clause, with the supplied structure | Evidence (file:line) | Status of the evidence | Grade |
|---|---|---|---|---|
| **G1** | **Lattice's fixed site set with discrete translations**, plus **Admissibility's finite covariance group** Z³ ⋊ O. Supplied with them: an interacting vacuum, the metric coupling (S7), and naturalness (S6). | Lemma R: for an ordinary interacting translation-covariant law with a translation-invariant vacuum, no continuous unitary implements a shear; only GL(3,Z) is reachable (`agents/R4_misframing.md:37–40`; ROUTES.md:28; R3_price.md:12). Narrowed by the T2 referee to "ordinary local, additively momentum-conserving" laws (TESTS.md:140). Schur: two free TT numbers under O (R3_price.md:11; R4:14). K3a″: c₂ = −0.01303 / +0.01247 per e² per cell (pack TEST_LOG.md:374–432). W1: the same stiffness with dynamical lengths, caused by the fixed index-space Brillouin zone (TEST_LOG.md:493). T0: a fixed window gives K₀⁴/(120π²), a following window gives 0 (TESTS.md:14). Rubakov–Tinyakov/Dubovsky (OUTSIDE_VIEW.md:7–18) | K3a″, W1: refereed CWC. Lemma R: same-family, referee-narrowed. T0: checked. RT/Dubovsky: comparator (V) | **P** for the symmetry count (see c2 below). **C** for the models. "Every fixed-site law is stiff" is only **S**: the W1 referee says "not a universal no-go" (TEST_LOG.md:523) |
| **G2** | **Qubit (finite local dimension)**, read as finite slots of the supplied tensor complex on a fixed grid, with harmonic comparators | Compact slots give O(k³) (`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_..._2026-09-14.md:13–19`). Linear dispersion needs non-compact slots in both canonical variables (`docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_..._2026-09-24.md:4`). Probes 10–21: slow, or light-like with helicity ±1 partners (WALL.md:96; branch notes, e.g. `THE_TENSOR_COMPLEX_ON_FINITE_SLOTS_..._2026-09-29.md` scope) | Landed (unaudited). Probes 10–21: branch; "sol-confirmed" per WALL.md:96 | **P/C** inside harmonic comparators on a fixed grid. One qubit per site is **untested** (viability map:1043–1047) |
| **G3** | **No clause supplies a tensor degree of freedom or a dynamics**: Admissibility is not a dynamics (:116–123). **Record** carries scalars and vectors only | FR3: moving-record models give diffusion, sound or a gapped tensor; no × polarization (TEST_LOG.md:615–649, refereed, model-specific; a tensor carried by records would be an explicit metric and meets K3a″, :647). FR1: no universal N/r (TEST_LOG.md:558–613, refereed; what gravity needs, :606). A liquid's displacement is a vector (`agents/kill_F1b_referee.md:72–76`). Weinberg–Witten (OUTSIDE_VIEW.md:39) | Refereed / comparator | **S**: no theorem that the axioms cannot produce a mediator. ROUTES.md:57 says "no named mechanism" |
| **G4** | **Lattice is spatial**: time is not supplied (:120–123, :185). The repo's only protection is the **primitive's** hypercubic regulator | T1: hypercubic Z⁴ gives Δ = 2e-9 by symmetry. A shape-fixed smooth spatial regulator with continuous time gives Δ ≈ −0.696 (TESTS.md:62–70, 79). For any regulator shape, Ξ ≥ 1 (`agents/kill_F1b.md:47–49`). K7a: the graviton's protection hangs on an exactly conserved stress (TEST_LOG.md:28). The proper cubic group has no boost (`docs/PROPER_CUBIC_GROUP_IS_24_..._2026-08-13.md`). Tension with chirality: K2a finds no mirror selector in the hypercubic form (TEST_LOG.md:74, 90–98) | Refereed CWC (T1, K7a, F1b-K2). Landed (cubic group) | **C** for sufficiency. The necessity of a time–space symmetry is **S**: the T1 referee says sufficiency only (TESTS.md:85) |
| **G5** | **Lattice's discrete translations** (crystal momentum is conserved only modulo umklapp), together with **Admissibility supplying no source or action** (open gate :187) | K3a: lattice-scale resonances obstruct every conserved momentum in the tested class (TEST_LOG.md:259). FR1: frozen records give no universal coupling (TEST_LOG.md:606) | Refereed: INCONCLUSIVE overall, the bounded obstruction confirmed | **C**, bounded class |
| **G6** | **Lattice is fixed**, so there are no diffeomorphisms; plus the supplied lapse and placement choices | Block 112: lapse closure only at β = −α, i.e. λ = 1. Block 150 T5: lattice brackets lack Leibniz and Jacobi; no finite-range placement closes (summarized at viability map:1091–1100). Branch lapse note: positive record-like kinetics (λ < 1/3) carry an extra scalar graviton (`A_LAPSE_SET_BY_RECORD_EVENTS_...md:40–46, 118`). The static Newton and ×2 bending are landed for a supplied member (WALL.md:47) | Landed (112, 150), unaudited. Branch (lapse) | **P** for the tested placements. **S** in general |
| **G7** | **Record's permanence plus `realized_state`** ("one realization is physical", E1_report.md:16), when the substrate is classical and frozen or random | F1a: a random TT tadpole and stiffness, IR-relevant (kill_F1a_referee items 1, 3, 5). E2/E3: dilution, quasicrystal, hyperuniform and growing sets all FAIL (TESTS.md:257–263). Lemma P (TESTS.md:249–256). E1: row noise gain diverges with the past (EXACT, TESTS.md:282), and the BD evolution is exponentially unstable at ε = 0.2. Block 122: undamped waves need signed weights (landed, `docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_...md:36–66`) | Refereed CWC; E1 INCONCLUSIVE leaning FAIL. Block 122 landed | **C**, bounded. General: **S** |
| **G8** | **Admissibility's nearest-neighbour (finite-valency) rule** against Lorentz invariance in law | Bombelli–Henson–Sorkin: no finite-valency equivariant graph on a Lorentz-invariant sprinkling (OUTSIDE_VIEW.md:48). The relabelling coupling gives exactly zero stiffness, but it is non-local and non-additive (TESTS.md:120–126) | Comparator (V); refereed | comparator / **C** |
| **G9** | No clause blocks it, and nothing supplies it | The CC is unsolved on the framework surface (R4:13). The trace channel is separate from the shear channels under O (R4:14), so a trace mechanism cannot fix the shear | Same-family | **P** for the separation; otherwise open |
| **G10** | The Qualification "a state is a configuration of records" (:92), against the need for a wave. The conformal factor | A wave is needed for Bell (09-24 dynamics clause, landed; viability map long-paths table). A Euclidean gravity form is indefinite (TEST_LOG.md:31). Under a unitary wave, a never-falling record count never rises (branch probe 7) | Landed / refereed / branch | **C/P** within scope |

### Two new small results used below

**c1 (checked; `checks/B2_c1_response_exponent.py`, `.out`).** This is one criterion for both faces of the stiffness wall.
- Write the graviton's TT self-energy from whatever it couples to as Π(ω) ≈ 16πG·G_T(ω), up to an O(1) normalization. G_T is the medium's zero-momentum transverse-stress response.
  - Its static part, Re G_T(0), is the shear modulus. That gives a mass (K3a″, Rubakov–Tinyakov).
  - Its dissipative part, Im G_T(ω) = ηω, gives damping at rate 16πGη. This is Hawking 1966 (comparator, M).
- Take a Planck-normalized medium, G_T = M_P⁴(ω/M_P)^n. Then:
  - the mass bound needs **n > 2.52 to 2.63** over 20 Hz–1 kHz;
  - a Gpc of undamped travel (< 10 % amplitude loss) needs **n > 2.49 to 2.59**.
- So the response must vanish at least as ω³.
- A classical dissipative liquid (n = 1) would need its Planck-unit product g·κ < 2e-63 over 1 Gpc.
- A Lorentz-invariant quantum vacuum gives n = 4 (Π ∝ k⁴ log k²; comparator, M): 6.6e-161 against the 1.1e-102 bar. **PASS.**
- **Grade.** The arithmetic is checked. The Π = 16πG·G_T bridge is suggested; it is the standard linear-response form.

**c2 (proved and checked; `checks/B2_c2_invariant_tt_forms.py`, `.out`). No finite point group can force the TT stiffness to zero.**
- The Frobenius form tr ε² is invariant under every G ⊂ O(3).
- The number of free stiffness numbers is O: 2, T: 2, D4: 4, I: 1. These match R3/R4 (O = 2) and the E3 referee (icosahedral = 1).
- So symmetry protection needs a **continuous** group that acts on the strain itself (SL(3) relabelling, or a gauge redundancy), not rotations alone. The proof is one line, character arithmetic checked.
- Also (proved): hop-count distance on Z³ is the ℓ¹ metric, and the body diagonal over the axis is √3. So the 09-29 Option-B wording "distances are counts of steps" (viability map:1105) is O(1)-anisotropic on any crystal-like graph. Geometry has to be read from wave propagation, not from hop counts.

---

## 2. The smallest unblocking change for each block

Columns:
- **Keeps Q:** the qubit.
- **Keeps R:** the records and readout.
- **Keeps F:** G0c's fermions (Chen–Kapustin face qubits, which need the cubic A10 framing; TEST_LOG.md:317–319).
- **Keeps L:** the Lorentz-boost results (the continuum limit of free fields on Z³; `docs/LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md:64–104, 362–383`).

| Block | Smallest change, priced on a clause | What else it breaks | Q | R | F | L |
|---|---|---|---|---|---|---|
| G1 (stiffness) | **(a) No axiom change:** add a tuned counterterm for 2 shear numbers at about 1e-98 (SUMMARY.md:82). The price is the naturalness premise S6. **(b) Lattice:** the law refers to no fixed positions or labels; only relations between sites enter ("relabelling is a gauge"). And the vacuum must not re-create labels by freezing (see G7) | (a) nothing in the axioms, but it is a second CC-sized tuning. (b) Z³, the cubic group, K7a's W(B4) construction, the staggered and walker constructions, and the landed U(1) lane as built | (a) yes, (b) yes | yes, yes | (a) yes, (b) no | (a) yes, (b) moot |
| G2 (partners) | **Qubit → M₂(C) ⊗ CCR**: option A, viability map:1131–1140. **Or** make no slot change, by taking geometry out of the slots and into the relations, as in G1(b) | Option A: "one record per site" stops bounding a site's information, and the exclusion results must be redone. The relations route: as G1(b) | A: extended; relations: yes | yes | yes / no | yes / moot |
| G3 (mediator) | **Make the relations dynamical**: geometry is the pattern of relations, and its fluctuations are the graviton, with relabelling as its gauge redundancy. On Record: "Records form" becomes the engine that grows the relations | The fixed background, and every result that uses one | yes | yes, with the formation rule changed | no | moot |
| G4 (one cone) | **Time and space treated alike by the law.** Either keep the grid with its hypercubic form (the primitive), or make the substrate a set of spacetime events with Lorentz invariance in law. A spatial liquid with continuous time is excluded: Ξ ≥ 1 for every shape (refereed) | Grid route: the stiffness is back (G1). Event route: finite valency (BHS) | yes | yes | grid: yes; events: no | grid: yes; events: superseded by exact Lorentz in law |
| G5 (universality) | **None extra, if** G1(b), G3 and G4 hold and every field lives on the same relations. "Metric universality" then holds by construction, and Weinberg's soft theorem gives it with IR Lorentz (comparator, M) | — | yes | yes | — | — |
| G6 (GR) | Relabelling invariance in law, i.e. a discrete general covariance. The growth or dynamics law has to give GR in the continuum. **No construction exists** | — | yes | yes | — | — |
| G7 (noise) | **Either** keep the micro-relations unrecorded (coherent; part of the wave), **or** keep them classical and find a dynamics whose noise couples only through derivatives. The latter is E1′'s question | Record: if (i), records may not lock the micro-relations | yes | (i) restricted; (ii) kept | no | moot |
| G8 (locality) | Admissibility's "nearest neighbour" becomes "linked events", whose count is unbounded under Lorentz. Locality holds only above a scale ℓ_k | the finite-valency reading | yes | yes | no | moot |
| G9 (Λ) | No clause change. Under "number of events = volume", the comparator offers "everpresent Λ" ~ 1/√N, of the observed order (Sorkin, M) | — | — | — | — | — |
| G10 | Qualification: "a state = records **plus** a wave over the unrecorded possibilities" | It is already needed for Bell; every beable candidate does this (pack CANDIDATE_1.md:96) | yes | yes | yes | yes |

---

## 3. Consistency: do the changes fit one substrate?

### 3a. The backward chain

Each step lists its hypotheses. Strong words are kept only where a hypothesis carries them.

**Step 1: G1 needs a continuous relabelling symmetry, and the realized vacuum must respect it.**
- *Hypotheses:*
  - **H1:** naturalness (S6);
  - **H2:** weak coupling and an EFT, with the mass equal to the static TT response at a stationary background (S2, S3);
  - **H3:** the graviton couples to everything, including the substrate's stress;
  - **H4:** no exact realization-wise conservation or coboundary identity for the stress (the E2/E3 referee's open exit, TESTS.md:263).
- *Argument:*
  - Finite point groups leave ≥ 1 free number (c2, proved).
  - Discrete translations reach only GL(3,Z) (Lemma R, proved same-family, narrowed).
  - The known protections are all continuous: gauge redundancy, no labels, or a fluid (comparator; OUTSIDE_VIEW.md:13–16).
  - If the symmetry holds only in law, each realization carries a random tadpole and stiffness (F1a, E2/E3: refereed).
- **Lemma Q (proved, elementary).** No locally finite classical configuration with at least two points is invariant under a one-parameter group of translations, SL(d) maps or boosts. An orbit would put uncountably many points in a bounded region.
- So a **classical realized substrate** can carry the protecting continuous symmetry only **in law, never in the realization**.
- **Reading.** A frozen realization *is* a set of labels (a glass), and labels are exactly the Stückelberg fields that give Rubakov–Tinyakov's mass. That is why the noise walls are mass-type: ω-independent, relevant in 3D.
- **Suggested.** If H4 fails, i.e. the per-realization coupling is gauge-invariant, the residual noise couples through derivatives. It then scatters like Rayleigh, ℓ⁻¹ ∝ ω⁴ in 3D (comparator), which is harmless (ℓ ~ 1e164 ℓ_P at LIGO frequencies, order of magnitude). That is why H4 is the one real exit.

**Step 2: G4 means the substrate cannot single out a frame.**
- *Hypotheses:* H1; interacting matter; no SUSY or other custodial mechanism (the referee's BGL list, kill_F1b_referee.md:86).
- A spatial liquid satisfies step 1 per configuration (R3_price.md:38). But its rest frame splits the speeds by (2/3)Ξ·g²/16π² with Ξ ≥ 1 (refereed).
- Flat space also forces ρ + p = 0, which removes the liquid's inertia (kill_F1b_referee.md:9–19). **Reading:** ρ + p = 0 is the vacuum's own, boost-invariant equation of state.
- Both facts point the same way. The relabelling has to include time–space mixing: Lorentz invariance in law, or a discrete time–space symmetry. The latter is known only on a grid, which step 1 rules out without tuning. **Suggested**, assembled from refereed parts.

**Step 3: Lorentz invariance in law plus discreteness means randomness in every realization.**
- BHS: the set must be Poisson-like and cannot carry an equivariant finite-valency graph (comparator, V).
- So a *classical* event substrate has white density noise in every realization. Lemma P does not apply in spacetime (supervisor_thread.md:80); power counting makes the noise marginal (E1_report.md:39).
- Whether the dynamics turns it into growing noise is E1's open question: BD has a diverging row gain (EXACT); E1′ is pending.

**Step 4: G3 and G6 need the relations to be dynamical.**
- *Hypotheses:* IR Lorentz invariance; Weinberg–Witten; the graviton is not a composite of matter with a covariant conserved T (comparator).
- No axiom supplies a tensor (section 1, G3). So the helicity-2 mode has to be the fluctuation of the substrate's own relations, with relabelling as its gauge redundancy. **Suggested.**

**Step 5: G5 then follows.** Every field lives on the same relations, so it shares one cone: E1's B̄ = F(p², sgn p⁰) for every species (TESTS.md:278). **Reading and comparator.**

**Result: five properties the substrate needs** (suggested, under H1–H4 and the step hypotheses).
- **(S1) Relational.** No fixed positions or labels in the law.
- **(S2) Spacetime-like.** No rest frame in the law.
- **(S3) Dynamical.** The relations *are* the gravitational field.
- **(S4) No frozen labels in the realized vacuum.** Either the micro-relations are coherent (unrecorded), or the realization-wise coupling is gauge-invariant.
- **(S5) Shared.** Every field lives on the same relations.

**Nothing here requires giving up the qubit** (finite local dimension). Positions are not variables, so no CCR is needed. That is a gain over F1b and over option A.

### 3b. The minimal changed axiom set: a candidate wording for the owner, not an adoption

It is the one closest to the current text: records as events. The changed words are marked.

> **Events** *(replaces Lattice)*. Physical sites are **events**. The only structure between events is **which can influence which**, and **their number: one per unit of spacetime volume**. No event, direction or frame is privileged; **the law never refers to event labels or positions**.
>
> **Qubit** *(unchanged)*. Each event has a domain of local possibilities, presented by M₂(C).
>
> **Admissibility** *(reworded)*. There is one fixed rule. For each event, the probability distribution over its possibilities is determined by, and varies with, the conditions at the events **immediately before it**. **The rule depends only on the influence relations, never on labels.**
>
> **Record** *(narrowed)*. Records form; **each record is an event, and forms with its relations to earlier records**. A record locks exactly one admissible possibility and is permanent. Only records are readable.
>
> **Qualification** *(extended)*. A state is a configuration of records **together with the wave over unrecorded possibilities**.

**What happens to the primitives.**
- `kinetic_isotropy` becomes unnecessary: time and space are alike by construction.
- `scale_reference` becomes the event density.
- `realized_state` is kept, and is load-bearing for the noise question.

**Fallback wording if B's noise fails** (candidate C, after the tests in section 5): "**Which events neighbour which is itself a possibility, not a record.** Records lock possibilities of matter; geometry is read only through records of matter." This changes Record further: records may not lock micro-relations. It is owner thought 5 in its coherent form.

**Contrast: the keep-the-grid package A.**
- Lattice is kept.
- Qubit becomes M₂(C) ⊗ CCR (viability map:1133–1140).
- A supplied tuned counterterm for 2 shear numbers is added.
- Still open: the conserved stress (K3a) and nonlinear closure (block 150). The cone is protected only if the stress is exactly conserved (K7a).

### 3c. What the B wording keeps, and what it still does not deliver

**Keeps:**
- the qubit (M₂(C));
- records and readout;
- "no site privileged", strengthened to label invariance;
- Admissibility's distribution form, which now reads as Bell-causal growth. That is formally close to Rideout–Sorkin sequential growth (comparator, M).
- "Records form" moves from an open gate to the engine of time;
- E1's exact mean results (shape-blind, one cone);
- owner thoughts 1 and 3 in their spacetime reading.

**Breaks or makes moot:**
- Z³ and the cubic group;
- K7a's W(B4) construction;
- G0c's face-qubit fermions (cubic framing);
- K2a's chirality selector;
- the landed Z³ U(1) lane as built;
- the member programme's lattice constructions (blocks 53–150);
- A36's "records carry no time" (TESTS.md:273): here the order *is* time;
- the Lorentz-boost results, which become comparators, superseded by exact Lorentz invariance in law.

**Still not delivered** (each open):
1. Noise control (E1 leaning FAIL for BD; E1′ pending).
2. A growth law that produces 3+1 manifold-like orders. Transitive percolation does not (comparator, M).
3. An Einstein–Hilbert kinetic term and GR dynamics. The BD action gives EH only in the mean, for a fixed sprinkling.
4. Quantum geometry. Classical growth gives classical geometry.
5. Fermions, chirality and gauge fields on events.
6. Locality: links are unbounded (BHS).
7. Λ, only as "everpresent Λ".
8. Where the wave lives on an order.
9. The black-hole area law. Horizon-crossing links give it in causal sets (Dou–Sorkin, comparator, M), not the frozen-record count; see owner thought 3.

---

## 4. The owner thoughts: help, hurt, or neither

| Thought | Verdict | Evidence |
|---|---|---|
| **1. Records are reality's grain** | **Helps only in the spacetime reading.** As spatial records on a fixed grid, it hurts G1 (Lemma R) and G7 (frozen labels: Lemma P, E2/E3). As record-events with count = volume, it helps: E1's means are exact for G1/G4, and everpresent Λ (G9, comparator). The noise question remains | TESTS.md:257–263, 275–297; c2 |
| **2. Records move between neighbours** | **Neutral to harmful for gravity.** Moving-record models carry no TT wave (FR3, refereed). Classical stochastic hopping has white "stress" noise. **Proved for dilute independent hoppers:** N_x and N_y are independent Poisson counts, so Var(N_x − N_y) = 4rρVT and S(0) > 0. That is n = 1, and c1 then needs g·κ < 2e-63 over 1 Gpc (suggested). **Reading:** in the event reading, records need not move; a gravitational wave is a 4D pattern among permanent records, which sidesteps FR3's "cannot oscillate" premise | TEST_LOG.md:615–649; c1 |
| **3. The count rises until frozen; a sealed box is a black hole** | **Mixed.** "The count rises" read as growth is time, which fits B, and number = volume gives Λ of the right order (comparator). "Frozen = black hole" hurts: crowding rules give a **volume**-law count of frozen states (branch note C, Fable-refereed, contested), whereas black-hole entropy is area. "Time = record creation" as a physical lapse hurts G2: positive kinetics (λ < 1/3) bring an extra scalar graviton (branch lapse note :40–46, 118). That is avoided only if record-count time is pure gauge, which label invariance in B provides (reading) | branch `THE_OWNERS_FROZEN_BOX_...` scope (C); `A_LAPSE_...md:40–46` |
| **4. Records as Bell beables in seats** | **Neutral for G1–G6, helpful for G10, harmful if gravity is sourced by the beables.** Beables give Born and Bell statistics (branch probe 5, T4: CHSH 2.81). But vacuum beables are at rest (probe 5, T6). A beable-sourced field would therefore see a frozen random pattern, i.e. mass-type noise as in F1a and E2 (suggested). So gravity has to couple to the wave, at least in the vacuum | branch `RECORDS_AS_BEABLES_UNDER_...` scope T4, T6 |
| **5. "The sites are just the substrate; the neighbourhood can move across it, including the qubits"** | **Depends on the reading. See below** | — |

### Thought 5 in detail

**(a) Canvas-visible: the law still sees the Z³ sites, and the qubits hop on them.**
- *No help.* The canvas keeps its Brillouin zone and discrete translations, so Lemma R applies.
- R4 c4 (checked, same-family): a dilute lattice gas on a fine canvas keeps a shear Hessian of −U·W″/2 (R4_misframing.md:41).
- FR3's swap and vacancy gases are this reading (refereed FAIL for TT).

**(b) Canvas-blind: the law sees only which qubits neighbour which, and site labels are pure gauge.**

| Question | Answer |
|---|---|
| Relabelling-protected? | **Yes, exactly in law, by construction.** Gauge-like: labels are a redundancy. Fluid-like: only if its vacuum is a liquid |
| Escapes the stiffness wall (Lemma R, Rubakov–Tinyakov)? | **Escapes Lemma R's premise**: the law has no fixed translations, and it avoids F1b's CCR cost on Qubit. **It does not escape on its own**, because the vacuum can re-create labels. A crystal-like graph re-creates Lemma R through spontaneous discrete translations (R4_misframing.md:51: "only if it breaks Z³ in the vacuum"). A frozen glassy graph gets a random mass (Lemma P, E2/E3) |
| Escapes the per-realization noise wall (Lemma P, E1)? | If the neighbourhoods **rearrange classically and stochastically**: Lemma P (a frozen-spatial result) no longer applies. Spacetime-white noise is marginal rather than relevant (E1_report.md:39). But the rearrangement is dissipative (n = 1), so gravitational waves die in Planck times (c1; Hawking 16πGη). It also has a rest frame, so Collins' Ξ ≥ 1 applies. **Fails.** If they **rearrange coherently** (the neighbourhood is an unrecorded possibility): there is no realization to be noisy. The vacuum *state* can carry the continuous symmetry, which Lemma Q forbids for any classical configuration. **Escapes in principle, and only this way.** Remaining risks: spontaneous crystallization, a missing kinetic term, and the frame |
| Keeps the qubit? | **Yes.** No positions are needed; this is its main advantage over F1b |

**Net (suggested).** Thought 5 is the right *shape* of escape: a relabelling-gauge substrate. It works only if the moving neighbourhoods are **coherent (not records) and frame-free (spacetime-like)**. It then becomes candidate C.

**A precondition to check whenever thought 5 is used.** "Distances are counts of steps" does not work on a crystal-like graph: it gives ℓ¹ geometry (c2). Distances have to be read from wave propagation.

---

## 5. The cheapest decisive tests (pre-registered here; readings fixed now)

**The candidates being discriminated.**
- **A:** the tuned grid.
- **B:** classical record-events.
- **C:** a coherent relational substrate (thought 5, coherent).
- **D:** a classical moving-record substrate (thoughts 2 and 5, classical).

**T-1. E1′, link-only influence on records-as-events.** Already pre-registered at TESTS.md:305–354 and running; I make no prediction. **Decides B.**
- Readings unchanged (TESTS.md:335–343).
- One addition, fixed now: **B survives only if both the gravity PASS and the M-PASS hold.** Universality (G5) requires matter to propagate coherently on the same substrate.
- Gravity-PASS with M-FAIL means B fails as a substrate.

**T-2. Coherent versus recorded substrate.** New; hours. **Decides whether the noise wall is a property of recording. Discriminates C from B and D at the level of mechanism.**
- **Setting.** A massless scalar on a 1D and on a 2D lattice. A local mass-type term δ·s_x, with s_x = ±1 drawn from **one law** in three versions:
  - (i) **recorded:** s_x frozen in each realization;
  - (ii) **moving records:** s_x is a telegraph process at rate γ;
  - (iii) **coherent:** s_x = σᶻ_x of substrate qubits with H_sub = −Δ Σσˣ − J Σσᶻσᶻ, in their ground state. Scan J/Δ through the transition, plus a random-J (glassy) control.
- **Measure.** The attenuation ℓ⁻¹(ω) of a low-frequency packet, elastic plus inelastic, and its exponent p in ℓ⁻¹ ∝ ω^p, at fixed δ.
- **PASS** (coherence is a real escape): on the symmetric side of (iii), with no tuning, ℓ⁻¹ = 0 below the substrate gap, or p ≥ 3. Meanwhile (i) gives finite ℓ and (ii) gives p ≤ 1.
- **FAIL:** (iii) shows p ≤ 1 or finite ℓ anywhere on its symmetric side.
- **INCONCLUSIVE:** otherwise.
- **Prediction (suggested).** PASS in the clean case, FAIL in the glassy control. If so, freezing (recording) of the substrate is the mechanism, and C is the fallback should T-1 fail.

**T-3. The response exponent of classical record substrates.** New; hours; reuses FR3's and E2's code. **Decides D.**
- **Setting.** FR3's swap gas and wind gas, and E2's frozen dilution. Hop rates along e scale as e·g⁻¹·e.
- **Measure.** As ω → 0: the zero-momentum TT stress (activity-anisotropy) spectrum S(ω), and the response G_T(ω).
- **PASS:** some record model has Re G_T(0) = 0, and both S(ω) and Im G_T(ω) vanish as ω^n with n ≥ 3 (c1: n > 2.6 is needed), with no tuning.
- **FAIL:** every model has Re G_T(0) ≠ 0 or n ≤ 1.
- **Prediction, written now.** FAIL. The gases have n = 1 (Poisson shot noise of hops, proved for independent hoppers); frozen dilution has n = 0 (E2).
- **What a FAIL decides.** No classical spatial record substrate, frozen or moving, can carry the micro-geometry. That leaves B (if T-1 passes), C, and the tuned grid A.

**The decisive owner question (not a computation).** Is the microscopic geometry **recorded** (classical, as in B) or **unrecorded** (part of the wave, as in C)? Section 3a says this choice decides which noise wall applies.

---

## 6. Plain summary

**In one sentence:** working back from what gravity needs, the framework's fixed grid of sites would have to become a growing web of events with no fixed positions, in which "space" is just the pattern of which events can influence which. The open question is whether those events can be permanent records or must stay quantum and unrecorded, and a test now running starts to settle it.

- **The grid itself is what blocks a weightless graviton.** On a fixed grid, the vacuum resists being sheared, the way a crystal does, and that resistance acts as a graviton mass. No finite symmetry of the grid can cancel it; a continuous one is needed. Keeping the grid costs a tuning about as extreme as the cosmological constant's.
- **"Space with a flowing substrate" does not escape.** Any medium that defines a rest frame makes particles' speeds of light differ. Flat space forces such a medium to have no inertia. If it flows by random hops, it damps gravitational waves within a Planck time.
- **What is left is a spacetime made of events,** whose law never refers to positions or labels and treats time and space alike. On average it has exactly the right properties: no stiffness and one light cone.
- **The qubit can stay.** Positions are not stored anywhere, so each event can still hold one qubit's worth of possibilities. Records, readout and "records form" survive, and "records form" becomes the engine of time.
- **The open problem is noise.** If the events are permanent classical records, every patch is randomly different. Whether waves cross a gigaparsec intact depends on the propagation rule. That is test E1′, now running.
- **If E1′ fails, the fallback is coherence.** The fine-grained connections would have to stay quantum and unrecorded, as in the owner's "neighbourhood moves across the substrate" idea in its quantum form. Records would then lock only matter.
- **Not delivered by any version:** the graviton's own dynamics (Einstein's equations from a growth rule), fermions and handedness on events, locality below about 1e-19 m, and the size of Λ.
- **Owner thoughts.**
  - "Records are the grain" helps only when records are spacetime events.
  - "Records move" does not carry gravitational waves.
  - "A frozen box is a black hole" gives entropy that grows with volume, not area.
  - Beables help quantum rules, but gravity must not be sourced by them.

---

## Appendix: scripts and files

All under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/B2/`.

- `checks/B2_c1_response_exponent.py` and `.out`: the GW-bound arithmetic for the low-frequency response exponent. Required n > 2.5–2.6; a dissipative Planck liquid needs g·κ < 2e-63; a Lorentz-invariant vacuum (n = 4) passes.
- `checks/B2_c2_invariant_tt_forms.py` and `.out`: invariant TT stiffness forms under T, O, D4 and I (2, 2, 4, 1); the ℓ¹ hop-distance ratio √3.
- `branchdocs/`: read-only copies of the 22 branch notes, made with `git show` for reading.
- `lorentz31.md`: a copy of the landed 3+1D boost note.
- This report: `B2_report.md`.

**Not refereed.**
- Lemma Q, c1's Π = 16πG·G_T bridge, the Rayleigh exit, and the dilute-hopper shot-noise lemma are mine (same-family).
- The five-property result (S1–S5) and both wordings are suggested, assembled from refereed parts. They need the codex sol referee before any necessity claim enters the summary, as TESTS.md:377 requires.
