# The gravity wall, current state: step 0 (history) and step 1 (the wall, stated twice)

**Setup.**
- The skill is the candidate exercise skill in PR #9472 (branch `claude/exercise-skill-lessons-20261009`). It is run here at the owner's request: "review and update the exercise skill if needed".
- The supervisor is Claude Opus 5.5. The route, kill, blind-check and literature agents are Claude Opus 5.5, so the whole exercise is same-family.
- Any test verdict of FAIL or no-go gets an other-vendor referee (codex gpt-5.6-sol, xhigh) before it is reported. That is the skill's new step-8 rule.

**Refresher read (supervisor):**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, with the generated baselines of all three approved primitives;
- `docs/audit/data/axiom_premise_nodes.json` (4 nodes);
- `docs/audit/data/derivation_obligations.json` (3 obligations, none on gravity);
- `docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md`;
- the review-loop skill.

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

## Step 1: the wall

### Plain version (draft for the blind check; at most about 150 words)

We want gravity to come out of the framework, not be put in. The framework is a fixed grid of sites. Real gravity has four checked features:
- its waves travel at light speed;
- they have no mass;
- they stretch and squeeze space in one pattern;
- gravity pulls on everything equally.

We can write Einstein's equations for small waves on the grid, but every way we have tried to make them come from the grid's own parts fails one feature:
- **qubit-like parts:** the waves come out too slow, or carry an extra sideways shake;
- **continuous parts:** the waves pick up a mass, because the grid's interacting vacuum resists being sheared the way a crystal does, and only a hand-tuned number removes it;
- **records as the carrier:** there is no long-range pull.

This is shown for small waves, specific models we built, and weak interactions. Getting past it means a grid construction with massless, pure, universal gravity and no hand-tuning, or naming the premise that must go.

*Analogy only:* a crystal resists shear; a liquid does not.

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

### Blind check

See `agents/blind_check.md` (Claude Opus 5.5, fresh context, given only the plain version).
