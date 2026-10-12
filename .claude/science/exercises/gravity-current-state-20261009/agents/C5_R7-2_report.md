# C5 R7-2: set E, a holographic or lower-dimensional substrate. Does it escape the walls that bind A, B, B′ and C?

**Worker.** Claude Opus 5.5 (same family as every C5 worker and the supervisor). 2026-10-12, 14:47Z–15:08Z. **Unrefereed.** No repository file was edited.

**Scripts and outputs.** In `scratchpad/C5/R7-2/scripts/`; each has a `.out` beside it, and each ran in under 1 s on 2 threads (`python3 -I`, except `r72_cube_rule_balls.py`, which imports its sibling script).
- `r72_numbers.py`: hyperbolic honeycombs, dS entropy and N-bound counts, Cohen–Kaplan–Nelson (CKN) cutoffs, dS/CFT weights, graviton polarization counts.
- `r72_cube_rule.py`: exact GF(2) counts of admissible configurations for a cubic-covariant local rule on Z³.
- `r72_markov_tail.py`: the inverse-covariance range of a scale-invariant Gaussian record field on Z³.
- `r72_cube_rule_balls.py`: the cube-rule counts on lattice balls up to R = 14.

**Literature.** A verification helper (same family) fetched or search-checked arXiv abstracts, and I fetched three more myself. **V** means fetched or search-verified this session. **M** means from memory, unverified.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY`, `OUTSIDE_VIEW` are in `P/`; bare `C5_*`, `C4_*`, `B_referee.md`, `B1_report.md` are in `P/agents/`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

**Labels.** proved / checked (script) / suggested / reading / comparator (V or M).

---

## 0. In plain words

- **The question.** In holography, gravity lives in a "bulk" and is encoded in a lower-dimensional system without gravity. Can a qubit lattice use this to dodge the walls found so far? Those walls are:
  - the graviton must be put in by hand (R6-2);
  - lattice momentum spoils boosts (C3, RB, RFW);
  - exact momentum needs the continuum (R6-1);
  - a positive local weight bends light by half GR's amount (R2-4).
- **Where holography works, Λ has the wrong sign.** The anti-de Sitter (AdS) version is the only setting in the literature I know of where a graviton is produced rather than supplied (comparator). There the walls are dodged in the infrared, because the graviton is the dual of the boundary's single stress tensor. But that bulk has Λ < 0. A pure AdS bulk is ruled out by the observed accelerating universe (Ω_Λ ≈ 0.69 under ΛCDM).
  - The escapes found:
    - the dark energy is a rolling scalar on top of a negative Λ (Antonini–Simidzija–Swingle–Van Raamsdonk–Waddell; V, abstract);
    - we live in a de Sitter bubble hidden behind a black-hole horizon (FHMMRS; V), encoded only in a mixed boundary state;
    - we live on a dS₄ brane in AdS₅ (Karch–Randall; V). This meets every observation listed, but its graviton is supplied.
- **Where Λ has the right sign, no 4D construction produces a graviton.** The explicit de Sitter constructions named in the item are in 2 or 3 spacetime dimensions: double-scaled SYK (dS₂/dS₃) and TT̄ + Λ₂ (dS₃). There, gravity has no gravitational waves at all (D(D−3)/2 = 0). The one 4D attempt counts the de Sitter entropy as states in a symmetric sector only. Its gravitons come from an algorithm matched to bulk GR, i.e. supplied (Silverstein–Torroba 2024; V).
- **The one structural surprise.** dS₄/CFT₃ puts the dual theory on a three-dimensional Euclidean space with no time: the future boundary. That is exactly the axioms' Z³ without time.
  - The late-time frozen field values are one value per site, permanent, like Record's records.
  - It is the only route that keeps Lattice's dimension.
  - It pays elsewhere:
    - the dual must be non-unitary, with complex weights for every massive particle (Im Δ ≈ 4×10³⁸ for the electron);
    - each site needs about 10¹²² internal components;
    - the one explicit example (the Sp(N) higher-spin model) has no Einstein gravity.
- **A new count wall.** A Planck-spaced 3D qubit lattice filling one de Sitter static patch has 10⁶¹ times more sites than the patch's maximum entropy allows (Bousso's N-bound).
  - Keeping independent qubits at every site would need spacing ≥ 3.4 fm, which colliders exclude.
  - Under the N-bound, records read as readable bits would be capped at 1 per 10⁶¹ sites per patch.
  - A local, cube-covariant support rule on Z³ (the 8 corner bits of every unit cube sum to zero mod 2) cuts the admissible count to an area law exactly (checked). So "holographic counting" can live in Admissibility without changing Lattice. It gives no gravity.
- **Bottom line.** No route is VIABLE. Pure-AdS codes are EXCLUDED under ΛCDM (referee required); their Λ < 0 + scalar, bubble and brane variants are OPEN (the brane variant reduces to set A or C). The dS routes are OPEN; their explicit D ≤ 3 realizations are EXCLUDED as descriptions of 4D gravity (referee required). Set E escapes the A/B/B′/C walls only in the AdS case, and it pays for that in the sign of Λ.

---

## 1. Prior art, counted once

The grep covered `docs/` and `.claude/science/` for "holograph", "tensor network", "HaPPY", "MERA", "de Sitter", "dS/CFT", "SYK", "TT̄", "Bousso", "Banks/Fischler".

**Repository docs.**
- `docs/HOLOGRAPHIC_PROBE_NOTE_2026-04-11.md:8-11,106-114`. A boundary-law fit of free-fermion Dirac-sea entanglement on a 2D staggered lattice. It says "not ... holography in the stronger AdS/CFT or quantum-gravity sense".
- `docs/TENSOR_NETWORK_CONNECTION_NOTE.md:18-19,38-40,75-77`. The propagator is an MPO. The RT, MERA and AdS/CFT language is explicitly **non-load-bearing**, and the RT inverse-coupling fit fails (R² = 0.6465).
- `docs/BOUNDARY_LAW_ROBUSTNESS_NOTE_2026-04-11.md:5,23,157` ("not a holography proof").
- `docs/HUBBLE_LANE5_C3_VACUUM_TOPOLOGY_NO_ACTIVE_ROUTE_NOTE_2026-04-27.md:27,145-147`: the holographic probe is not a derivation of Ω_Λ.
- `docs/AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md:246-256`. C3 gives a dS correction with S_dS = π/(GΛ). **This is off by a factor of 3** (§3.4, checked). C4 marks the Bousso covariant bound "future work". It is the only "Bousso" hit.
- `docs/AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md`: the simple-fiber Widom class cannot give 1/4 by entanglement.
- `docs/PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md`: c_cell = 1/4, conditional.
- `docs/COSMOLOGICAL_CONSTANT_RESULT_2026-04-12.md:15-30`: Λ = 3/R², conditional.
- **No hits** for dS/CFT proper (every grep hit for "dS/CFT" is the substring of "AdS/CFT"), HaPPY, SYK, TT̄ or Banks–Fischler outside the R7-2 pre-registration (`TESTS:3275-3276`). MERA appears only in the non-load-bearing tensor-network note.

**Packet.**
- WW and its holography exit: `B_referee.md:47,53,165,175` ("Holography: it is specifically a Weinberg–Witten/Marolf loophole; boundary Lorentz violation need not survive in the IR").
- `B1_report.md:300`: class VII "Holographic … AdS … lacks: our de Sitter 3+1 world; dimension count".
- `SUMMARY:169`; `PRICE_NOTE:148`; `C5_O5_synthesis.md:505`; `C5_S5_synthesis.md:579`; `supervisor_thread.md:115-117,157`.
- `C5_R6-2_report.md:257` (holography row: "Not available without a Lattice dimension change"; corrected in §8).
- `C5_R2-4_report.md:51` and `TESTS:2729-2731` (the positive-weight wall; escapes are "non-real or non-local bridges").
- `C4_E1_report.md:39-55,179,222-239` and `C4_E1_referee.md:17,19` (holographic Lifshitz flows; RE's bounded FAIL is for **spectator** gravitons and explicitly leaves out "emergent diffeomorphism invariance").
- `C5_R3-3_report.md:44-45,209-226` (exact dS/AdS LRL); `C3_G-L_referee.md:58` (dS null rays do not focus); `C5_R5-3_report.md:210` (Λ = 3/R² restated).

**What is new here** (worker claims, unrefereed):
- the per-route sorting;
- the D ≤ 3 count applied to the explicit constructions named in the item;
- the {5,3,4} lattice identification and its curvature cost;
- the N-bound count against Planck-spaced Z³ and against record density;
- the cube-rule area-law count;
- the Markov-range price for late-time records;
- the dS/CFT–Z³ structural match.

---

## 2. Hypotheses, stated before titles

- **(H1) Bulk-gravity readout.** "4D gravity" means a bulk with propagating helicity-±2 waves on the matter cone. GW170817 needs D ≥ 4. It couples universally to bulk stress (GR as the bulk's low-energy theory).
- **(H2) Holographic production.** A graviton counts as produced when it is the bulk dual of a boundary stress tensor in a boundary theory without dynamical gravity. Its masslessness follows from exact IR conservation of the unique boundary T. This needs large N and a large gap: HPPS 0907.0151 (V). Several decoupled CFTs give several gravitons; coupling them gives masses, and at most one interacting massless graviton exists (Aharony–Clark–Karch hep-th/0608089; Kiritsis hep-th/0608088; V).
- **(H3) Observations, as in (c).**
  - Dark energy: Ω_Λ = 0.6889 ± 0.0056 (Planck 2018 + BAO; V). Read as Λ > 0 only under ΛCDM.
  - Ω_K = 0.001 ± 0.002 (V); DESI DR2 10³Ω_K = 2.3 ± 1.1 (`TESTS:2993`).
  - GW170817: −3e-15 ≤ Δc/c ≤ 7e-16 (`C5_O2_report.md:48`).
  - Locality to about 1e-19 m (`SUMMARY:492`).
  - MICROSCOPE / universality (O2).
- **(H4) The N-bound.** Bousso's N-bound, N = 3π/Λ = ln dim H in Planck units (hep-th/0010252; V), is a theoretical bound, not an observation. Anything resting on it is labelled "under the N-bound".

**Outside realizations this report excludes:**
- string compactifications with dS uplifts (KKLT etc.), which have no qubit-lattice form;
- causal-set or spin-foam holography;
- non-commutative routes (S5 §6 lists them separately);
- relational routes without a boundary dual.

---

## 3. Checks and lemmas

### 3.1 No gravitational waves in D ≤ 3 (proved, standard count; `r72_numbers.out` §6)

**The count.** A massless spin-2 field in D spacetime dimensions has D(D−3)/2 propagating polarizations: 0 for D = 3, none for D = 2, 2 for D = 4.

**The explicit constructions named in the item, as built, all have D ≤ 3:**
- **HaPPY.** A {5,4} tiling of H², so the bulk is AdS₃ (Pastawski–Yoshida–Harlow–Preskill 1503.06237; V). Exact RT for connected regions is proved for holographic *states*, not for the code with bulk legs (V).
- **Random tensor networks** in their worked 2D form (Hayden et al. 1601.01694; V). Their flat Rényi spectrum is fixed only for single regions (V).
- **DSSYK.** Related to dS₂ (Susskind 2109.14104, 2209.09999, via JT gravity with Λ > 0) and to dS₃ (Narovlansky–Verlinde 2310.16994; V).
- **TT̄ + Λ₂.** dS₃: Gorbenko–Silverstein–Torroba 1811.07965; microstates counted in Coleman et al. 2110.14670 (V).

**Consequence (proved given H1).** None of these can carry GW170817's tensor waves or a Newtonian 1/r² pull mediated by propagating gravitons. As **descriptions of 4D gravity they fail by construction.** This says nothing about 4D generalizations (§4).

### 3.2 Regular hyperbolic lattices have Planck-scale curvature (checked; `r72_numbers.out` §1)

**The computation.** A Coxeter-simplex Gram computation gives the edge length of each regular honeycomb of H³ in units of the curvature radius:

| Honeycomb | Edge length | Neighbours per site |
|---|---|---|
| {5,3,4} | 1.061275 | 6 |
| {4,3,5} | 1.616922 | 12 |
| {3,5,3} | 1.736596 | 20 |
| {5,3,5} | 1.992769 | 12 |

Z³ = {4,3,4} comes out with a degenerate (Euclidean) Gram matrix.

**{5,3,4} keeps every per-site clause of Lattice** (`AX:37-41`):
- its vertex figure is the octahedron {3,4}, the same as Z³'s;
- so each site has 6 nearest neighbours and an octahedral site stabilizer, i.e. "proper cubic rotations about each site";
- it loses only "the cubic lattice Z³ … standard translations": its cells are dodecahedra, 4 around each edge.

This is the cheapest Lattice text change for a 3D hyperbolic tensor-network bulk (reading).

**But the curvature radius is fixed at a/1.06.** At a = ℓ_P:
- as an AdS₄ bulk, Λ = −1.29e70 m⁻² = −1.19e122 Λ_obs: wrong sign, and 122 decades too large;
- as a spatial slice, the curvature radius misses the |Ω_K| < 0.002 bound by 10^62.3 in radius.

A semiclassical bulk (ℓ_AdS ≫ a) needs non-regular tilings that are locally Z³-like, with sparse disclination edges (5 cubes about an edge). Locally that brings back the Z³ bulk lattice (suggested).

### 3.3 Qubits make a Planck-size bulk (checked arithmetic; comparator inputs V)

**The area per bond.** In tensor networks the RT "area" is (number of cut bonds) × ln χ (HaPPY; RTN, V). With RT, S = A/(4G), one qubit bond (χ = 2) is 4 ln 2 ℓ_P² = 2.77 ℓ_P² of area, about 1.67 ℓ_P across (`r72_numbers.out` §2).
- A regular tiling has one tile per AdS radius. A semiclassical bulk then needs ln χ ~ (ℓ_AdS/ℓ_P)².
- That is the Qubit price `AX:47`: M₂(C) → M₂(C)^{⊗n} with n ~ (ℓ/ℓ_P)².
- Equivalently, the boundary needs central charge c_T ∝ ℓ²/G ≫ 1 (HPPS's large N).

**Perfect tensors (comparator V).** Qubit absolutely-maximally-entangled states exist only for n = 2, 3, 5, 6 legs (Huber–Gühne–Siewert 1608.06228; the n ≥ 8 cases are via earlier work, search summary only). So:
- a HaPPY-type perfect-tensor code with one bulk qubit per tensor cannot be built from qubit perfect tensors on any of these placements:
  - {5,3,4} vertices (6 + 1 = 7 legs);
  - {4,3,5} cells (6 faces + 1 = 7);
  - {5,3,4} cells (12 faces + 1 = 13);
- without bulk legs, the AME(6,2) vertex tensor gives a holographic *state* on {5,3,4}, with no bulk Hilbert space, hence no bulk matter and no graviton (reading).
- *Scope:* this rules out perfect qubit tensors only. Block-perfect or approximate codes are not addressed.

**The nearest qubit-like prior construction** is Kohler–Cubitt 1810.08992 (V). It gives a 3D hyperbolic bulk dual to a 2-local nearest-neighbour Hamiltonian on a 2D boundary (≅ S²). But:
- the couplings range from O(1) to Δ_L^{poly(n log n)};
- the duality holds only below Δ_L ("above Δ_L there is no longer any meaningful duality");
- the bulk has no gravity.

Against Admissibility `AX:57-58`, the rule is nearest-neighbour but neither fixed nor translation-covariant: its strengths grow with system size (reading).

### 3.4 de Sitter counts, the N-bound and a Planck Z³ (checked; `r72_numbers.out` §2–§4)

**The de Sitter numbers.** With Λ = 1.089e-52 m⁻² (Planck 2018 central values; M for H₀):
- R_dS = 1.660e26 m;
- S_dS = 3π/(Λℓ_P²) = 3.313e122 nats = 4.78e122 qubits;
- one qubit per 4 ln 2 ℓ_P² of horizon.

**The Bekenstein note's C3 slip.** `docs/AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md:248` writes S_dS = π/(GΛ) = 1.10e122. The 4D value is 3π/(GΛ) (checked; it is a qualitative pointer there, so nothing downstream is load-bearing).

**Under the N-bound (H4):**
- A Planck-spaced Z³ in the static patch has 4.54e183 sites, which is 10^60.98 more than N_q.
- A volume-filling lattice of *independent* qubits meets the N-bound only at spacing a ≥ (V/N_q)^{1/3} = 3.42e-15 m. Colliders exclude that by at least 4 decades (`SUMMARY:492`).
- The CKN entropy form gives the same 3.3e-15 m.
- The CKN black-hole form gives Λ_UV < 4.19 meV and ρ ~ Λ_UV⁴ = 12 ρ_Λ. This is the known holographic-dark-energy coincidence (CKN hep-th/9803132, V). A Hubble-radius cutoff then gives w = 0, so Li uses the future event horizon (Hsu hep-th/0403052; Li hep-th/0403127; V).
- **Reading (under H4).** This wall is new for sets B, B′ and C. A Planck lattice's Hilbert space cannot be a tensor product of independent site spaces at the scale of a static patch. Alternatively, only a ≤ 1e-61 fraction of sites can hold readable records at once. That fits O4's "records must be rare" (`TESTS:2408-2412`) on independent grounds. **R4-5's Z³ cap** of 8.24e184 record events (`TESTS:2941`) is 10⁶² above N_q.

**Λ is a count in every dS route (reading).** Banks: "the cosmological constant is an input … rather than a quantity to be calculated" (hep-th/0007146; V, body). In each route Λ's size is the inverse of a count:
- Λℓ_P² = 3π/S, with S = ln dim H (static patch);
- ~3/N (dS/CFT, ℓ²/G ∝ N; M);
- ~1/√V₄ (everpresent Λ, R4-5).

The counts are consistent: S_dS/√V₄ = 13 with R4-5's past-cone V₄ = 6.389e242 (`TESTS:2939`). None derives the count. This is the third restatement after Λ = 3/R² (`C5_R5-3_report.md:210`).

### 3.5 An area-law count from a local cubic rule on Z³ (checked; `r72_cube_rule.out`)

**Rule C.** Bits on Z³ sites; on every unit cube, the XOR of its 8 corners is 0. The rule is invariant under translations and all 48 elements of O_h (checked). Its range is one unit cube (distances 1, √2, √3), so it is **not** nearest-neighbour.

**Exact counts** (GF(2) rank; log₂ of the admissible count, N_adm):
- **Open L³ box and L³ torus:** log₂ N_adm = 3L² − 3L + 1 for L = 2…9 (box) and L = 2…8 (torus). The admissible configurations are exactly f(y,z) ⊕ g(x,z) ⊕ h(x,y), i.e. one bit per axis-parallel line (random f, g, h checked).
- **Any finite region (proved).** The unit-cube constraints inside a region are linearly independent. Order the cubes by their top corner t = (x+1, y+1, z+1). The site t lies only in cubes whose top corner is ≥ t componentwise, so the system is triangular. Hence log₂ N_adm = |sites| − |unit cubes inside the region| exactly. Every run confirms rank = number of cubes (`r72_cube_rule_balls.out`).
- **Lattice balls:** log₂ N_adm/(4πR²) runs as follows, versus a predicted asymptote of ½⟨|n_x|+|n_y|+|n_z|⟩ = 0.75 (suggested; the approach is slow because of the rough lattice surface):
  - R = 2…8: 0.50, 0.59, 0.60, 0.67, 0.67, 0.65, 0.67;
  - R = 10, 12, 14: 0.707, 0.690, 0.712.

  The per-site fraction falls as 1/R.

**Against Bekenstein–Hawking** (1/(4 ln 2) = 0.361 bits per ℓ_P²), Rule C meets the area bound for balls when a ≳ 1.44 ℓ_P (suggested arithmetic).

**Contrast (proved).** For one-bit sites, every symmetric nearest-neighbour pair rule, which cubic covariance forces, has a count that is either O(1) or volume-law. The rules: equal, antiequal, hard-core ({00, 01, 10}), or all. Hard-core already admits every subset of one sublattice, so log₂ N ≥ ⌊L³/2⌋. So a one-bit area law needs range beyond nearest neighbour (Rule C), or more states per site.
- An 8-state site (s_x, s_y, s_z) whose i-component is constant along i-bonds is nearest-neighbour, covariant and exactly 3L² (proved, trivial).

**Reading.** Holographic *counting* can be paid inside Admissibility without changing Lattice: a line-subsystem-symmetric (fracton-type) support rule with Z³ kept. The price is Admissibility's "nearest-neighbor" (`AX:57`) → unit-cube range, or Qubit's one bit → 3 bits. It produces no gravity and no dynamics, only the count.

### 3.6 Late-time records and Admissibility's nearest-neighbour clause (checked; `r72_markov_tail.out`)

**The setting.** In dS/CFT and inflation, super-horizon modes freeze. Their late-time values φ(x) at the future boundary are distributed by |Ψ[φ]|², with Ψ = Z_CFT (Maldacena astro-ph/0210603; V). The observed spectrum is P ∝ k^{n_s−4}, n_s ≈ 0.965.

**What fails (Gibbs reading).** For a Gaussian field, the conditional law of φ_x given all other sites involves exactly the sites where the inverse covariance Q ≠ 0. A nearest-neighbour Markov field therefore needs 1/P to be a degree-1 trigonometric polynomial.
- With the lattice symbol (k̂²)^{(4−n_s)/2}, the inverse covariance Q is nonzero at every range checked, up to r = 24. The tail goes as r^{−6.09} (fit over r = 16–24), approaching the continuum r^{−(7−n_s)} = r^{−6.04}.
- The Laplacian control vanishes beyond nearest neighbours (≤ 2e-16).
- **So under the Gibbs (all-sites-conditional) reading of `AX:60-61`, the observed primordial record field is not nearest-neighbour determined** (proved, elementary, plus checked).
  - The proof covers any stationary Gaussian field whose inverse spectrum behaves as |k|^α with α ∉ 2ℕ at small k. Such a symbol is not analytic at k = 0, so it is not a trigonometric polynomial, so Q has infinite range.
  - Only the observed small-k (cosmological-scale) behaviour is used. The unobserved Planck-scale spectrum does not matter.

**Under the sequential-formation reading** (`AX:66-69`: "conditional on formation at that site"), local growth rules can generate power-law correlations (KPZ/SOC-type; M). Inflation's scale invariance comes from modes freezing in time order. So **there is no price under the sequential reading** (suggested).

### 3.7 A finite Hilbert space has no permanent quantum record (proved, elementary)

For finite dim H, U(t) = e^{−iHt} is almost periodic. For every ε > 0 and T₀ there is t > T₀ with ‖U(t) − 1‖ < ε (simultaneous Dirichlet approximation of the phases E_j t/2π). So any record encoded as a projector expectation returns arbitrarily close to its unformed value. Recurrence scales are of order e^S or longer (Dyson–Kleban–Susskind hep-th/0208013: the paper is V from its abstract, which speaks of "very deep paradoxes"; the recurrence content is M).

**Consequence for static-patch and TT̄ + Λ₂ routes** (both have finitely many states; Coleman et al. V). "Records are permanent" (`AX:79-80`) holds only if records sit outside the unitary Hilbert-space dynamics, as the Record axiom's fixed reality. Then the N-bound caps readable records per patch at N_q, so formation must stop or records must leave the patch.
- Leaving the patch is what Λ > 0 expansion does to comoving sites. A Planck-spaced physical lattice in an expanding patch needs new sites at a rate of 3H per site (reading). The owner's thought "count rises until frozen" (`records-count-rises-until-frozen`) is touched here only as a hypothesis; it is not used.

### 3.8 dS₄/CFT₃ weights for observed matter (checked; `r72_numbers.out` §5)

**The weights.** Δ = 3/2 ± √(9/4 − m²ℓ²). They are complex for m > 3ħ/(2cℓ_dS) = 1.78e-33 eV, i.e. for every massive SM particle:

| Particle | Im Δ |
|---|---|
| ν at 0.05 eV | 4.2e31 |
| electron | 4.3e38 |
| proton | 7.9e41 |
| Higgs | 1.1e44 |

The dual is non-unitary: complex weights appear "if there are sufficiently massive stable scalars" (Strominger hep-th/0106113; V). So its Euclidean weight cannot be a positive reflection-positive probability. This is exactly the "non-real bridge" escape that R2-4's γ ≤ ½ wall leaves open (`TESTS:2731`).

---

## 4. Per route: what each supplies against observations (item (c))

### (a) Tensor-network or holographic codes with an AdS bulk (HaPPY, RTN, AdS₄/CFT₃ on a lattice boundary)

**Two geometries.**
- **(a1) The axioms' Z³ + time as the boundary.** The bulk is AdS₅ (4+1), the wrong dimension, unless a braneworld (a‴) is used.
- **(a2) A 3D bulk network.** The network sits on {5,3,4} or {4,3,5} (§3.2), with a 2D boundary lattice; the bulk is AdS₄.

**What it supplies:**
- **Λ.** Λ_bulk = −3/ℓ² < 0.
  - Under ΛCDM this violates Ω_Λ = 0.6889 ± 0.0056 (V).
  - A regular Planck tiling also misses Ω_K by 10⁶² in radius (§3.2).
- **One light cone and GW speed.** Automatic for bulk fields if the bulk is semiclassical Einstein. That needs a large-N, large-gap boundary (HPPS; V) and ln χ or ln d ~ (ℓ/ℓ_P)² per site (§3.3). HaPPY and RTN have no dynamics, so they have no graviton.
- **Universal coupling.** Produced, not supplied, given a unique boundary T (H2). WW is evaded because the graviton lives one dimension up (`B_referee.md:175`).
- **Records / arrow.** None supplied. The boundary law is unitary and time-symmetric, so the arrow is in the state, as in B (`TESTS:2738`).

**Walls.**
- **Boost wall and exact momentum.** These move to the boundary, where only IR (fixed-point) exactness of T is needed. Broken boundary translations are dual to a Lorentz-breaking bulk graviton mass (Vegh 1301.0537, "massive gravity as a holographic framework"; V). That this mass decays into the interior for an irrelevant lattice is suggested.
- **RE's FAIL** is bounded to spectator gravitons and lists "emergent diffeomorphism invariance" as outside (`C4_E1_referee.md:17,19`). Holography is outside its class.
- **The remaining wall** is that no qubit-lattice holographic (large-N, gapped) CFT₃ is known (comparator M). The Kohler–Cubitt boundary is local but size-dependent (§3.3).

**Variants that are not excluded:**
- **(a′) Λ < 0 plus a rolling scalar.** Antonini–Simidzija–Swingle–Van Raamsdonk–Waddell 2212.00050 (V): accelerated expansion without fine-tuning at the background level, and "arbitrarily close to ΛCDM" with more tuning, ending in a crunch. The dual is a 3D Euclidean holographic CFT coupled to a 4D CFT on M × I (Van Raamsdonk 2102.05057; V).
  - Prices: a scalar dark-energy component (coincidence tuning), a future crunch, and a 3D Euclidean + interval substrate.
  - Data: the abstract claims no data fit. DESI DR2 analyses prefer dynamical dark energy:
    - exponential quintessence over ΛCDM at 3.3–3.8σ (Akrami–Alestas–Nesseris 2504.04226; V, search);
    - a 93.8% preference for a future transition to AdS in a Higgs-like potential (2506.21542; search summary only, unconfirmed).

    So "Λ > 0" is a ΛCDM inference. The data do not exclude a vacuum Λ ≤ 0 with a rolling scalar (comparator).
- **(a″) A dS bubble behind a horizon.** In FHMMRS hep-th/0510046 (V), large dS bubbles look like black holes from the boundary and are "described by mixed states". So our patch would be encoded only in a mixed state, outside simple reconstruction.
- **(a‴) A dS₄ brane in AdS₅** (Karch–Randall hep-th/0011156; V, body). There is a massless bound graviton separated by a mass gap from the continuum, so it meets Λ > 0 (by tuned brane tension), one cone, GW speed and universality.
  - Its graviton is the 5D metric (supplied), or, in the 4D dual, the induced metric of a cut-off CFT, i.e. a spectator graviton. So it reduces to set A (continuum 5D) or to set C plus induced gravity (RE's bounded class) (reading).
  - It is the only construction found that meets every observational item of (c). The exception is record formation, which no route supplies. It produces nothing.

### (b1) dS/CFT (Strominger; Anninos–Hartman–Strominger)

**What it supplies:**
- **Λ > 0** by construction. Its size is a count, Λℓ_P² ~ 3/N, with N ≈ (ℓ_dS/ℓ_P)² = 1.05e122 (§3.4). Not derived.
- **One cone, GW speed, universal coupling.** Automatic if an Einstein dS₄ dual exists. None is known (comparator).
- **The explicit dual.** The Sp(N) anticommuting-scalar Euclidean CFT₃, dual to Vasiliev higher-spin dS₄ (1108.5735; V). It has conserved higher-spin currents (gap 0), so its bulk carries an unbroken tower of massless higher-spin fields and has no locality below ℓ_dS. Observation:
  - only spin ≤ 2 massless particles;
  - local physics at 1e-19 m ≈ 10⁻⁴⁵ ℓ_dS.
  - This instance is **EXCLUDED** (worker reading, bounded to free and critical vector-model duals; referee required).
- **Arrow.** Bulk time runs IR → UV, and "the monotonic decrease of the Hubble parameter corresponds to the irreversibility of renormalization group flow" (Strominger hep-th/0110087; V).
  - Reading: this is the one route where an arrow could come from a law-level monotone (RG irreversibility) rather than from the state.
  - Caveat: the c/F-theorems use unitarity (reflection positivity, strong subadditivity), which the dS dual lacks (§3.8). So the monotone is not established (suggested).
- **Records.** The late-time frozen values, one per future-boundary point and permanent, are the cleanest textual match to "a state is a configuration of records" plus "one record per site, permanent" (`AX:79-80,92`) of any route (reading).

**Structural match (reading).** dS₄'s flat-slicing future boundary is R³. Its isometry group SO(1,4) acts there as the Euclidean conformal group: translations, rotations, dilation (= bulk time translation), and special conformal maps. Z³ with cubic rotations is a discrete subgroup of the boundary Euclidean group, and the substrate has no time. That matches `AX:116-123`: Admissibility "does not … define a time metric".
- One Grassmann pair per site with the nearest-neighbour, second-order action Σ(χ_{x+i} − χ_x)(χ̄_{x+i} − χ̄_x) on Z³ is the lattice form of the Sp(2) AHS dual (symplectic fermions). Its bulk would have N = 2, so it is Planck-curved and strongly quantum higher-spin (reading; G ∝ 1/N is M).
  - The axioms' finite-Grassmann gate (`AX:178`) is a first-order staggered-Dirac realization, so this is a neighbouring structure, not the same one.

**Reading for Einstein dS/CFT: OPEN.**

### (b2) Static-patch holography, DSSYK, Banks–Fischler

**What it supplies:**
- **Λ > 0, size = count.** Λ = 3π/(G ln dim H), so N_q = 4.78e122 qubits. Banks treats Λ as input (V).
- **4D gravity.** None. DSSYK is tied to dS₂/dS₃ (§3.1). The static patch's stretched horizon is S² × time, with all-to-all (fast-scrambling) couplings (Susskind; V titles, M content).
- **One cone, GW speed, universality.** Not addressed in any construction.
- **Records.** Finite dim H means no permanent quantum record (§3.7).

**Reading: OPEN** for 4D. The existing D ≤ 3 realizations fail H1 by construction (§3.1). That is not a refereed exclusion of the route.

### (b3) TT̄ + Λ₂ and its T² + Λ₃ extension (Silverstein et al.)

**What it supplies:**
- **dS₃** (1811.07965, 2110.14670; V): the Gibbons–Hawking entropy counted as microstates. No gravitons (D = 3).
- **dS₄** (Silverstein–Torroba 2409.08709, JHEP 03 (2025) 156; V). A restricted T² deformation of a CFT₃ on S² × R, keeping only the diagonal energy density and pressure. It reproduces the radial geometry and the GH entropy as a state count in the dominant band.
  - Gravitons and local bulk excitations come from a deformation algorithm "matched to bulk local calculations", including an uplift from AdS₄/CFT₃. So the graviton is **supplied by matching**, not produced (reading from the abstract).
- **Λ > 0.** Yes; its size is again the count (finite number of states, §3.7).
- **One cone, GW speed, universality.** Only through the matched algorithm.

**Reading: OPEN.** This is the most advanced dS₄ holographic construction, and it does not yet produce gravitons.

---

## 5. Prices against the axiom text (named, none adopted)

| # | Route | Text touched | Price |
|---|---|---|---|
| E1 | (a2) | Lattice `AX:37-41` | Z³ → {5,3,4}: the per-site clauses are kept (6 neighbours, octahedral rotations). Translations become [5,3,4]. The curvature radius is pinned at a/1.06, so a semiclassical bulk needs non-regular tilings (§3.2) |
| E2 | (a), (a′) | Lattice `AX:37` | Z³ → Z² (+ time) for AdS₄/CFT₃; or 3D Euclidean M plus an interval (a′) |
| E3 | (a), (b1), (b3) | Qubit `AX:47` | M₂(C) → M₂(C)^{⊗n}, with n ~ (ℓ/ℓ_P)² ~ 10¹²² for an Einstein bulk (large N). Qubit perfect tensors are excluded for 7- and 13-leg codes (§3.3) |
| E4 | (a), (b) | Admissibility `AX:57-61` | The boundary rule must sit at a large-N, gapped critical point (unbuilt). Kohler–Cubitt-type local boundaries have size-dependent couplings |
| E5 | (b1) | Admissibility `AX:60-61` ("probability distribution") | Becomes a complex, non-reflection-positive Euclidean weight; probabilities = \|Z\|² over late-time data. This is R2-4's non-real escape. Under the Gibbs reading the record field is not nearest-neighbour determined (§3.6) |
| E6 | (b2) | Lattice `AX:37` and Admissibility `AX:57` | A finite set of 4.78e122 qubits with all-to-all p-body random couplings; "one fixed rule" → a disorder instance |
| E7 | (b2), (b3) | Record `AX:79-80` ("permanent") | No permanent quantum record in finite dim H (§3.7). Records must be outside the Hilbert dynamics and are capped at N_q per patch (H4) |
| E8 | any lattice set, under H4 | Qubit / Record | Planck Z³ with independent sites over-counts the static patch by 10⁶¹. Escapes: non-factorized site spaces, record density ≤ 1e-61, or an area-law support rule (Rule C: Admissibility range → unit cube; §3.5) |
| E9 | all dS routes | none (input) | Λ's size becomes a count (N or ln dim H), not derived |

**The cheapest per text** (reading):
- **(b1)** keeps Lattice's dimension and the timeless substrate. It pays Qubit (E3) and Admissibility (E5).
- **Rule C** keeps Lattice and Qubit. It pays Admissibility's range, but buys only the count.

---

## 6. The walls of A, B, B′ and C: escaped or not

| Wall (refereed source) | AdS route (a) | dS routes (b) |
|---|---|---|
| Graviton supplied (R6-2 worker; WW `B_referee.md:47`) | **Escaped**: produced as the dual of a unique boundary T (H2), given large N + gap | Would be escaped if an Einstein dual existed; none does. AHS has a higher-spin tower. (b3) supplies gravitons by matching |
| Boost wall (C3/RB/RFW, `SUMMARY:397-412,520-527`) | Moved to the boundary IR; lattice breaking → bulk mass decaying inward (suggested). Outside RE's spectator class (`C4_E1_referee.md:17`) | Same if a dual existed; at I⁺ the lattice cutoff is a late-time cutoff (reading) |
| Exact momentum (R6-1, Lemma G, `TESTS:2391-2395`) | Needed only for the IR CFT's T (emergent) (suggested) | Same |
| Positive weight gives γ ≤ ½ (R2-4, `TESTS:2729-2731`) | Escaped by the non-local bulk reconstruction bridge (reading) | (b1) escapes by non-real weights (§3.8) |
| Records (R2-5 `TESTS:2738`; O4) | Arrow in the state | (b1): possible RG-monotone arrow (unproved). (b2)/(b3): permanence conflicts with finite H (§3.7) |
| Λ mean (R5-3, `TESTS:2985-2993`) | Wrong sign under ΛCDM | Sign right by construction; size = count (E9); the zero-mean problem becomes "why N ≈ 10¹²²" |
| Lensing noise (RZ) | None (no random events) | None |
| **N-bound count (new, under H4)** | Satisfied by construction (holographic) | Satisfied by construction. **B, B′ and C as volume lattices fail it unless E8 is paid** |

---

## 7. Readings against the FIXED readings (`TESTS:3280-3283`)

| Route | Reading | Basis |
|---|---|---|
| **(a)** AdS codes / AdS₄ bulk, pure Λ < 0 | **EXCLUDED** (worker; referee required), bounded to "our patch is in an AdS vacuum region with dark energy = Λ" (ΛCDM) | Λ_bulk < 0 vs Ω_Λ = 0.6889 ± 0.0056 (V). Regular Planck tilings also miss Ω_K by 10⁶² (§3.2). HaPPY and RTN as built are D = 3 with no dynamics (§3.1) |
| (a′) Λ < 0 + rolling scalar (3D Euclidean holographic dual) | **OPEN** | No data fit claimed (V); DESI DR2 analyses prefer dynamical dark energy (V, search). Predicts a crunch. Lattice, Qubit and Admissibility prices E2–E4 |
| (a″) dS bubble behind a horizon | **OPEN** | Encoded only in mixed states (V); no reconstruction of the interior |
| (a‴) dS₄ brane in AdS₅ | **OPEN**: meets (c) except records, but reduces to A or C | Graviton supplied (5D) or a spectator (induced); Λ tuned by brane tension |
| **(b1)** dS/CFT, Einstein dual | **OPEN** | No construction. Prices E3 and E5; keeps Z³ (§4) |
| (b1) AHS Sp(N) higher-spin instance | **EXCLUDED** (worker; referee required), bounded to vector-model duals | Gap 0, so a massless higher-spin tower and no sub-ℓ_dS locality. Observation: spin ≤ 2 massless only; locality at 10⁻⁴⁵ ℓ_dS |
| **(b2)** Static patch / DSSYK / Banks–Fischler | **OPEN** for 4D | Existing realizations dS₂/dS₃ have no gravitons (§3.1). Prices E6 and E7 |
| **(b3)** TT̄ + Λ₂ / T² + Λ₃ | **OPEN** | dS₃: no gravitons. dS₄: state count in a solvable sector, gravitons by matching (V) |

**No route is VIABLE.** None gives 4D gravity with Λ > 0 that is produced from a qubit-lattice substrate, carries matter on one cone, and couples universally.
- The one construction that meets every observational item, (a‴), supplies the graviton.
- **Against the expectation in the S5/R6-2 framing.** "Holography only through AdS, against Λ > 0" is **confirmed for pure AdS under ΛCDM**, with two corrections:
  - the Λ < 0 + scalar escape (a′) is not excluded by the sign of today's dark energy;
  - dS₄/CFT₃ keeps the Lattice dimension (next section).

---

## 8. Corrections to earlier records

1. **`C5_R6-2_report.md:257`** ("Holography … Not available without a Lattice dimension change"; "dS holography is unestablished (comparator M)").
   - dS₄/CFT₃ puts the dual on a 3D Euclidean space, so Z³ is kept and only the time direction is absent from the substrate, which the axioms never had (`AX:116-123`).
   - dS holography is unestablished *for Einstein gravity in 4D*. Partial 4D work exists (Silverstein–Torroba 2409.08709; V).
   - The AdS exclusion needs the qualifier "if dark energy is Λ" (a′).
2. **`docs/AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md:248`.** S_dS = π/(GΛ) should be 3π/(GΛ) in 4D (checked). A one-line corrigendum candidate; nothing in this report depends on it.

---

## 9. Scope and strong-word check; referee items

- **"No gravitational waves in D ≤ 3"** is the standard massless spin-2 count. It concerns propagating bulk gravitons only. It does not exclude higher-dimensional generalizations of those constructions.
- **"EXCLUDED" for (a)** uses ΛCDM's identification of dark energy with Λ. It does not cover (a′), (a″) or (a‴).
- **"EXCLUDED" for AHS** concerns vector-model duals (gap 0 or 1/N-small). It is not a statement about any Einstein dS/CFT.
- **The N-bound wall (E8)** rests on H4, a theoretical bound, not an observation. "Fails" there means "fails under H4".
- **Rule C**'s count, |sites| − |cubes|, is proved for every finite region. It is checked for boxes (L ≤ 9), tori (L ≤ 8) and balls (R ≤ 14). The asymptote 0.75 for balls is suggested. It is a count, not a dynamics, and its range is a unit cube, not nearest neighbour.
- **§3.6** is proved only for the Gibbs (all-sites-conditional) reading of Admissibility. There is no price under the sequential-formation reading.
- **§3.3**'s perfect-tensor obstruction rests on qubit AME existence (V) and covers perfect tensors only. "ln χ ~ (ℓ/ℓ_P)²" is RT bookkeeping for regular tilings (one tile per AdS radius), not a theorem for general codes.
- **§4's structural match** of dS/CFT with Z³, and the RG-monotone arrow, are readings. The F-theorem's unitarity premise fails in dS duals.
- **Referee required** (EXCLUDED readings):
  - (a) pure AdS under ΛCDM;
  - (b1) the AHS higher-spin instance;
  - the D ≤ 3 statement as applied to the explicit realizations.
- **Not done:**
  - no construction of a qubit-lattice large-N holographic CFT₃;
  - no data fit of (a′);
  - no check that Rule C supports any propagating dynamics.
