# Neutral brief for route agents (gravity, current state, 2026-10-09)

You are one of several independent route agents in a repo 'exercise' on a physics wall. You get the wall, its history and the assumption ledger. You do NOT get the supervisor's favoured routes or other agents' results, by design.

Repository (read-only for you): /Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790 (branch claude/candidate-law-20261008 = main + candidate pack + this exercise packet). Candidate pack with all test logs and referee verdicts: .claude/science/candidates/candidate-law-20261008/ (TEST_LOG.md, KILL_SHEET.md, checks/referee_*/REFEREE_VERDICT.md). The 2026-09-29 gravity exercise packet is on branch origin/claude/toe-viability-probes-20260927 at .claude/science/exercises/gravity-wall-finite-records-20260929/ (read with git show). Campaign 8: `git show origin/ai/probes:probes/work/campaign8-tick-moving-records-20261002/FINAL_REPORT.md`.

FRAMEWORK REFRESHER READ (required before conclusions; state which you read): docs/MINIMAL_AXIOMS_2026-06-29.md (in full); docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md (approved primitives: scale reference = units only, a = l_P NOT derived; kinetic isotropy c_t = c_s = hypercubic regulator form only; realized state = pointwise evaluation only); docs/audit/data/axiom_premise_nodes.json. Every premise, the axioms included, is an assumption in this exercise; you may challenge any of them, but you may not adopt axioms or primitives — name a premise change only as a price.

CONCRETE-RETURN CONTRACT: return one to three routes. Each route must contain at least one of: a formal lemma with a proof or proof skeleton whose open steps are named; an explicit construction with admissibility checks; equations, an invariant, or a dependency reduction; a counterexample, falsifier or exhaustive finite certificate; an exact missing lemma with the step that fails. Reject your own vague returns ('topology might help'). For each route give:
Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes | What you would have to believe for it to work | First artifact (a concrete test with a pass/fail reading) | Cost | What it would change if it worked
Also: the theorem-strength gap test — is your route's terminal obligation weaker than, equivalent to, or stronger than the target? If equivalent, say so (the route is then 'blocked-equivalent' unless it brings a new mechanism).
You may run small Python checks in your scratch folder. Label every claim EXACT / CHECKED / ARGUED / COMPARATOR (literature from memory unless you verified it; if you can browse, cite precisely). Plain language first. Report at most about 1,200 words.

## Step 0: what is already known

This exercise **extends** the 2026-09-29 gravity exercise. Its packet is on branch `claude/toe-viability-probes-20260927`, at `.claude/science/exercises/gravity-wall-finite-records-20260929/`. It does not repeat it.

That exercise ended with the following price for Einstein's graviton on a fixed grid of finite sites with exact local rules (a wounded lemma, same-family):
- (a) continuous, unbounded local variables, the only working construction;
- (b) local rules broken at order one in the vacuum;
- (c) a composite graviton whose extra modes some unnamed mechanism removes.

What has happened since. Nothing below is audited. "Refereed" means codex gpt-5.6-sol confirmed it with corrections.

| When | Surface | What it found |
| --- | --- | --- |
| 09-28 | held blocks 190 and 191 (backlog 39–40, DR branch) | The free sea resists shear: exact infinite-lattice enclosures, diagonal [1/16, 7/20] and off-diagonal [1/40, 3/40]. A member that sees the sea gets a gap in its uniform traceless modes, with ω² = 2w̄E₂/K, on a static background. |
| 09-28 | held block 193 v3 | Missing records do not stretch the walk. A periodic vacancy pattern gives axis speed 1 or 0, and random vacancies act as local scatterers with damping. |
| 10-02 to 10-04 | campaign 8, §6 (`ai/probes`) | A record gas swallowed by clumps gives 1/r clock slowing, but half of Einstein's next-order term, half the light bending, no waves, no frame dragging, and a moving body's field only as a wake. The field route (A23/A25) reaches linear Einstein form with a fixed 2×2×2 job pattern and continuous payload. |
| 10-08 | candidate pack `claude/candidate-law-20261008`, K7a (refereed) | A staggered linearized-gravity action on the 16 half-shift role classes of Z⁴. It is exactly W(B4)-covariant and exactly lattice-gauge-invariant, with no doublers, and reduces exactly to A25. Exact gauge invariance leaves 1 of 9 hypercubic two-derivative forms, so it protects one graviton speed **if** the coupled stress is exactly conserved. |
| 10-08 | K3a / K3a′ (refereed) | Interacting lattice QED has lattice-scale resonances that break every finite-range conserved stress in the tested class. The defect falls as about R^-2.9. An extrapolation cannot decide the outcome: INCONCLUSIVE. |
| 10-08 | **K3a″ (refereed)** | **On the rigid grid, the interacting vacuum has a transverse-traceless (TT) shear stiffness of about 1e-2·e² per cell, converged, with no protecting symmetry.** An explicit metric coupled to it is massive unless a counterterm is tuned. The free part is O(1) (blocks 190/191). A coupling that moves the embedding, cutoff and measure together is untested. |
| 10-08/09 | **W1 (refereed), W2** | **Dynamical edge lengths on fixed adjacency (Regge/Kuhn, Whitney Hodge stars) keep the same TT stiffness**: O(1) at e⁰ and about (−1.4e-2, +5.5e-3)·e² at O(e²). The mechanism is the fixed label-space Brillouin zone: for the free IR cone a fixed window gives −1/(60π²), while a window that follows the strain gives 0. W2: the vacuum Regge graviton is healthy, with 4 gauge modes and 1 spurious mode off shell, plus 2 TT modes on the pole. |
| 10-09 | **FR1 (refereed)** | With records freezing sites, a compact frozen cluster gives no universal N/r field. In a free sea it is a short-range scatterer (about r^-5 to r^-7). In a Goldstone magnet it gives a 1/r tilt set by capacitance, which grows with size not N, and live excitations feel it only at about r^-4. |
| 10-09 | FR3 | Running in parallel, not part of this exercise: can moving records carry TT waves? |
| 10-08 | G0c (refereed) | Not gravity, but relevant to "one qubit per site". Chen–Kapustin face qubits carry covariant spinless lattice fermions under all 24 turns. |

**Not to be re-derived here:**
- every item above;
- every item on the 09-29 list: the stored-variable swap, quantum links, photon composites, on-site stiffness, move sets, residual symmetries, exact additive Gauss laws, and induced gravity given a metric;
- static bending and perihelion (blocks 59, 60, 144, 145).

**Not yet tried anywhere in the repo:**
- a vacuum or structure whose **static shear modulus is zero** ("liquid-like"), as opposed to a crystal-like vacuum;
- adjacency that is itself dynamical or recorded (option B of 09-29);
- a coupling that moves the cutoff covariantly with the geometry;
- a strongly correlated finite-slot phase;
- an emergent graviton protected by an exact lattice constraint, with matter coupled through it.


### Precise version

**Exact target contract** (proof-search governance).

| Field | Content |
| --- | --- |
| Target statement | A law on the framework's grid (sites of Z³ with nearest-neighbour adjacency) whose low-energy sector contains a massless helicity-±2 mode. It has exactly two TT polarizations, ω = c_g\|q\| with c_g = c_light (to the GW170817 level, about 1e-15), and no other gapless mode coupled at gravitational strength. It couples universally to the conserved energy-momentum of interacting matter (equivalence to about 1e-15). Its masslessness is natural: no counterterm tuned beyond what the axioms and approved primitives supply. |
| Quantifiers and domain | It must hold with interacting matter at weak coupling (at least O(e²)) in the law's own vacuum. A free-field-only construction does not count. |
| Allowed premises | The four axioms, the three approved primitives, and named supplied premises, each stated. |
| Forbidden weakenings | Tuning the graviton mass away; restricting to free matter; approximate masslessness above the LIGO bound; a non-universal coupling; extra gapless partners at gravitational strength. |
| Required edge cases | Static sources (Newton, bending ×2); radiating sources (two TT modes, double-pulsar partner bound); bound composites (equivalence). |
| Completion witness | A construction plus a proof or decisive check, refereed. |
| Outcomes that do not count as closure | Linear equations with free or supplied matter only; a metric supplied as a continuous field with a tuned mass; an emergent mode without an exact protecting mechanism; a no-go proved for one supplied model presented as a no-go for the axioms. |

**Current status** (bounded, unaudited; refereed where step 0 says so). Every constructible graviton on the fixed grid tested so far is one of:
- **(i) slow or partnered**, with finite slots: probes 10–21 (sol-confirmed) and the 09-29 exercise;
- **(ii) massive from the interacting vacuum's TT shear stiffness unless tuned**, with continuous variables on a rigid grid or with dynamical lengths on fixed adjacency: K3a″ and W1, refereed;
- **(iii) absent**, when records carry it, frozen or as a gas: FR1 refereed, campaign 8 argued.

The emergent route (iv) has no construction.

**The sharpest one-line form** (a reading).
- On a fixed grid, the low-energy fields' cutoff is set by adjacency and does not move with the geometry. So the vacuum has a TT modulus at the cutoff scale, the "shear modulus of a crystal".
- A massless graviton needs that modulus to vanish or to be cancelled exactly.
- Finite slots fail earlier, on purity or speed.

**Progress would be one of:**
- a construction with a vanishing TT modulus that is protected, not tuned;
- a mechanism that makes the modulus irrelevant to the graviton;
- a proof that the wall is equivalent to one named premise (the price);
- a demonstration that the wall is misframed, with the cheaper question that replaces it.

### What the axioms say / what we supplied / what was proved

| What the axioms say | What we supplied | What was proved (bounded, unaudited) |
| --- | --- | --- |
| Sites are the points of Z³, with nearest-neighbour adjacency, translations and proper cubic rotations; no site privileged | A fixed embedding (rigid), or edge lengths on a fixed complex with diagonals (Kuhn); a 2×2×2 or 16-class role pattern | Fixed adjacency means a fixed label-space Brillouin zone, which gives a TT modulus for any field theory regulated on it. Checked for the free IR cone (−1/(60π²)) and computed for lattice QED (K3a″, W1) |
| One site's possibilities: M₂(C) | Continuous canonical pairs (oscillators); several qubits per site; face-qubit fermions | No exact canonical pair on M₂(C) (landed 05-02). Finite slots give slow or partnered gravitons (probes 10–21) |
| One nearest-neighbour admissibility rule fixes each site's odds; it is not dynamics | Hamiltonians, ticks, couplings (minimal, vielbein, Whitney/DEC); the Fock vacuum of weakly interacting lattice fields | O(e²) TT stiffness ≈ 1e-2·e² per cell, unprotected (K3a″, W1); free part O(1) (190/191) |
| Records form, one per site, permanent; only records are read | Records as frozen sites, as a gas, or as Bell beables | No universal N/r from frozen clusters (FR1). Gas: half bending, no waves (campaign 8) |
| Approved primitive: kinetic isotropy, c_t = c_s with a hypercubic regulator | A hypercubic Euclidean form for every sector (K7a) | One speed for photon and matter protected; for the graviton only if the stress is exactly conserved (K7a); interacting stress not exactly conserved in the tested class (K3a) |
| Approved primitive: scale reference a⁻¹ = M_Pl (units only; a = l_P is not derived) | The lattice cutoff at the Planck scale | The induced graviton mass² scales like (TT modulus)·a⁻⁴/M_P², so its size depends on a/l_P (reading) |

**Reading.** As in 09-29, every middle-column entry is supplied. The axioms say nothing about gravity, a metric or dynamics. The new element since 09-29 is that the stiffness face of the wall rests on **fixed adjacency**, which is the one ingredient in the left column (the Lattice axiom). The partner face rests on the supplied finite-slot reading of Qubit.


## Step 2: the ledger

| ID | Kind | Assumption, in plain words | Where the wall uses it | What if it is wrong? | Already tested? | Cheapest test | Changes an owner decision? |
|---|---|---|---|---|---|---|---|
| L1 | axiom (Lattice), read geometrically | The grid's neighbour structure is fixed, so the low-energy fields' momentum cutoff is fixed in label space | K3a″ and W1. The mechanism is in Pack `TEST_LOG.md`, W1 referee section (fixed window −1/(60π²) vs strain-following 0) | The TT modulus need not arise. A cutoff that follows the geometry gives 0 in the free IR cone | Only "cutoff follows strain" in the continuum control (about 1e-12). Never on a lattice whose adjacency can change | A toy whose neighbour structure rearranges ("liquid"): does its vacuum TT modulus vanish? | **Yes**: this is the Lattice axiom |
| L2 | axiom (Qubit) with the supplied finite-slot reading | Each site's possibilities are finite (M₂(C)) | The 09-29 partner and speed face (probes 10–21) | Continuous slots remove the partner face, but then L1's stiffness face bites (K3a″) | Yes (09-29; K3a″) | none new | Yes, but the stiffness face survives |
| L3 | axiom (Admissibility) plus supplied dynamics | The law is a local Hamiltonian or tick on fixed sites | everywhere | Non-local or non-Hamiltonian laws are untested | partly (A42; campaign 8) | — | maybe |
| L4 | axiom (Record) | Records are permanent and one per site | FR1 and FR3 (record-carried gravity) | Moving records: FR3 is running | FR1 refereed; FR3 running | FR3 | yes (decision 7 of campaign 8) |
| P1 | approved primitive (kinetic isotropy) | c_t = c_s, with a hypercubic regulator | K7a (one cone) | Without it, the photon and matter speeds are also unprotected | K7a | — | no |
| P2 | approved primitive (scale reference), with a = l_P **not derived** | The cutoff sits at the Planck scale | the size of the induced mass, m_g² ~ (TT modulus)·a⁻⁴/M_P² (reading) | A coarser cutoff gives a smaller mass. A cutoff near 1e-3 eV would put m_g near 1e-33 eV, but such a coarse grid is excluded by Lorentz tests (suggested) | no | an order-of-magnitude scan | no |
| S1 | supplied model | Matter is ordinary interacting lattice fields (staggered fermions plus U(1)) | K3a″, W1 | The free part can be designed away; interactions bring the modulus back | K3a″ (O(e²), several coupling rules) | — | no |
| S2 | supplied definition | Graviton mass = the zero-momentum TT Hessian of the vacuum energy, for an independent metric field | K3a″ and W1 interpretation; referee caveat: needs a stationary background and kinetic normalization | For an emergent graviton the modulus is "a diagnostic only" (referee); the true mass needs the collective field's 1PI inverse propagator | no | build any emergent-graviton toy and compute its 1PI TT mass | maybe |
| S3 | supplied method | Harmonic or perturbative level: linearized gravity, O(e²) | everywhere | Strongly correlated phases could differ (the 09-29 "most likely wrong") | no | — | maybe |
| S4 | supplied state | The vacuum is the weakly interacting Fock vacuum of lattice fields on a crystal-like substrate | K3a″, W1 | A vacuum with zero static shear modulus (liquid-like, defect-proliferated) could remove the stiffness | no | as L1 | yes, if it needs a dynamical substrate |
| S5 | reading | Gravity is a local wave pattern (a lattice graviton mode) | everywhere | Gravity as non-local, global or thermodynamic (Jacobson) | Jacobson-type is dead on the grid (16–18% anisotropy) | — | maybe |
| S6 | target choice | Naturalness: no tuned counterterm for m_g | the wall's FAIL lines (K3a″, W1) | Nature already tolerates the cosmological-constant tuning, the trace twin of this modulus. A single mechanism could tune both | no | check whether any known CC mechanism, such as equilibrium self-tuning, also kills a **second** derivative (modulus), not just the first (tadpole) | yes |
| S7 | supplied coupling | The metric enters through a fixed rule: minimal, vielbein, Whitney | K3a″, W1 | A rule that moves the embedding, cutoff and measure together is untested on a lattice (referee) | continuum only | as L1 | maybe |
| H1 | hidden | Translation invariance of the substrate (a crystal) | K3a″, W1 | A random or disordered substrate (a glass) is untested; a glass also has a static shear modulus (suggested) | no | — | no |
| H2 | hidden | One vacuum, with no relaxation dynamics for anisotropy | K3a″, W1 | A dynamical relaxation of the modulus ("self-tuning") is untested | no | — | maybe |

**Rows the wall survives without:** P1, H1 and S1 (any interacting matter does it). L2 is load-bearing only for the partner face.

**Load-bearing for the stiffness face:** L1, S4, S7 (the fixed substrate and cutoff), S2 (what counts as a mass), S6 (naturalness) and S3.


