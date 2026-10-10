# Lane R, probe R1: redundancies native to the framework (2026-10-10)

**Worker:** Claude Opus 5.5 (same model family as the supervisor). Nothing in the repository was edited. Scratch: `.../scratchpad/laneR/R1/`. **No codex referee has seen this.** Under lane R's rules (`TESTS.md:723`), the FAIL below cannot be recorded until it has been refereed.

**Labels.**
- **proved:** an elementary derivation given here.
- **checked:** a computation run here.
- **suggested:** an argument.
- **reading:** an interpretation.
- **comparator:** literature, or a repository note that is not refereed.

## 0. Verdict (worker, for R1's classes)

**FAIL, bounded to the classes examined.** For each class, one of the fixed FAIL conditions is shown:

| Class (the price is the redundancy) | (i) gapless ±2, linear | (ii) protected | (iii) universal coupling | (iv) tunings | Failing condition |
|---|---|---|---|---|---|
| **V.** Vector (relabelling-type) gauge δh = ∂₍ᵢλⱼ₎, compact qubit/clock slots | ±2 and a helicity-0 mode, **ω ∝ k²** | mass forbidden | see horns below | — | dispersion not linear |
| **VS.** V plus the scalar (Hamiltonian-type) constraint, compact | ±2 only, **ω ∝ k³** | mass forbidden | see horns below | — | dispersion not linear (prior art, reproduced) |
| **F.** Scalar-charge (fracton) gauge δh = ∂ᵢ∂ⱼα, compact | ±2, ±1 and 0, **all linear**, at different speeds | mass forbidden | **impossible:** needs ∂ᵢ∂ⱼTᵢⱼ = 0, but ∂ᵢ∂ⱼTᵢⱼ = ∂ₜ²T₀₀ ≠ 0 for moving matter | at least one speed tuning, plus extra light modes | universal coupling impossible |
| **VS-EH.** VS with the noncompact Einstein–Hilbert-type term | ±2, **ω = k** | mass forbidden | **matter on fixed Z³ sites cannot carry the charge** (§3, Lemma D) | — | universal coupling impossible on the fixed grid, within Lemma R's scope |

The supervisor's registered expectation was that (i) and (ii) pass for Gu–Wen-type models (`TESTS.md:717`). This disagrees in part:
- In the regular compact class, the redundancy that looks like relabelling (V, VS) gives quadratic or cubic dispersion, not linear.
- Only the fracton class F is linear, and it fails (iii) outright.

Lane-level reading: R1 alone does not close lane R. The loopholes in §6 remain at INCONCLUSIVE level.

## 1. Prior art found in the repo (grep of docs/)

All of these are supplied-model, conditional-support notes, unaudited unless stated otherwise.
- **`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`** (PR #8112; proposed_retained, review pending). This is the main prior result.
  - The vector constraint G on E and the scalar constraint S on h Poisson-commute (:56).
  - A compact finite-clock Hamiltonian with exact modular constraints is constructed. N > 36M is needed to lift the constraints (:111).
  - **Regular compact characters with both gauge symmetries ⇒ every frequency is O(k³)** (:212).
  - The noncompact H_N gives ω² = Jg·k², but finite penalties leave det K = −J²/2 < 0 and a nilpotent scalar Jordan chain (:260–278).
  - The scalar source gives the attractive inverse-Laplacian kernel only for H_N (:292).
  - The map to the one-qubit nearest-neighbour law is "a separate compiler" obligation (:182).
- **`docs/DYNAMICS_CLAUSE_THE_LANDED_TENSOR_CONSTRAINTS_FREEZE_UNDER_TWO_SITE_GENERATORS_...2026-09-24.md`.** Two-site nearest-neighbour generators freeze every tensor-electric slot (:34). Smith-factor obstructions block moves within one closed neighbourhood (:55).
- **`docs/DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_..._TWELFTH_ORDER_...2026-09-24.md`.** The first curvature move is ⟨δ|H_eff|0⟩ = −A·h¹²/U¹¹ with A = 111150053/31850496 (:46–47). Compare the U(1) ring of spin ice, which moves at 4th order.
- **`docs/COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_...2026-09-14.md`.** A covariant nearest-neighbour **support** rule (Admissibility's zero set) can carry a binary Gauss code, given a V/L/P/C role pattern on doubled coordinates (:36, :271). The roles are extra structure.
- **`docs/DYNAMICS_CLAUSE_CHARGES_ARE_GAUSS_DEFECTS_..._RECORD_PHASES_ARE_PURE_GAUGE_...2026-09-24.md`.**
  - Under full soldering, no one-qubit covariant scalar charge exists.
  - Its own "pure gauge" claim for record or link phases is **withdrawn** (:96–103): an on-link basis change is not a vertex gauge transformation.
- **`docs/FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`.** Local U(3) fibre-frame changes are passive trivialization changes (:23). This is an internal, Yang–Mills-type redundancy (helicity 1), not spin 2.
- **`docs/UNIVERSAL_GR_BLOCK_CONSTRAINT_INTERPRETATION_NOTE.md`** (audited_conditional). It reads a block split as the Hamiltonian/momentum constraints. The auditor calls that identification "a renaming/interpretation step", with the bridge theorem missing.
- **`docs/GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`.** This is a continuum identity m_g² = 2Λ/c² on S³, assuming GR. It is not a lattice protection mechanism and is not used here.
- **Packet.**
  - "Records carry only scalars and vectors (FR3)" (`SUMMARY.md:59`).
  - Lemma R, narrowed (`PRICE_NOTE.md:125`).
  - The gauge identity forbids an h-only mass and symmetry does not (`PRICE_NOTE.md:116`).
  - The 09-28 panel lead: "one-per-site records resemble fracton charges" (memory, panel 09-28).

## 2. Step 1: redundancies already in the axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)

| Transformation | Axiom text | Exact? | Local? | Tensor Gauss law? |
|---|---|---|---|---|
| Global translations and proper cubic rotations | Lattice :37–41 | Exact symmetry of the law (Admissibility :57–58). It is a redundancy only under a relational reading (no site privileged, :40) | **Global only.** Every adjacency-preserving bijection of Z³ is global. **Checked:** the 5³ cubic torus has exactly 6000 = 48·L³ automorphisms, the global group. **Comparator:** Sabidussi–Vizing/Imrich, Aut(Z³) = Z³ ⋊ B₃. **No local relabelling exists on the fixed grid** | No |
| Automorphisms of one site's algebra, PU(2) ≅ SO(3), applied globally | Qubit :47, :52–53; "a law privileges no states" :94 | A symmetry if the rule is covariant (reading). It is **not** a redundancy: it changes record content, which fixes readout (:82–83) | Global | No |
| The same automorphisms, independently per site | Qubit :52–53 | **Proved:** if the rule is covariant under independent U_x, the distribution at x is PU(2)-invariant and independent of the neighbours' orientations. The invariants of SO(3)×SO(3) on (r_x, r_y) are just \|r_x\| and \|r_y\|. **So local covariance trivializes all orientation coupling, unless a connection (link variables) is added.** Even then it is internal, giving helicity 1 (prior art: fibre-frame note) | Local | Not spin 2. Internal redundancies give vector bosons |
| Phase of a locked possibility (a ray) | Record :79, :82–83 | Exact, by projectivity | Local | Trivial: it acts on no field. The prior note's "pure gauge" for link phases is withdrawn |
| Order in which records form (A36: "records carry no time", `TESTS.md:273`) | Record :77, :82–83 (readout by content alone) | Exact: histories that differ only in formation order give identical readouts | **Local** (one formation time per site) | **Reading:** it has the shape of the *scalar / many-fingered-time (lapse)* half of GR's gauge group: the record content is frozen, as under a Hamiltonian constraint ψ-picture. But it acts on no tensor field in the axioms, so it generates no Gauss law |
| Transformations of unrecorded possibilities that never reach any record | :83 ("a site with no record cannot be read") | Exact only relative to a dynamics, which is not supplied (:116–123, :181–186) | Could be local | The only native *place* where a fluctuating gauge field could live (§4). No redundancy is supplied |

**Conclusion of step 1 (proved/checked, at the level of the axiom text).** The axioms contain no local redundancy tied to spatial directions. A local relabelling would change the fixed nearest-neighbour adjacency (Lattice :37). Local internal redundancies either trivialize the rule or are helicity-1 with a connection. The one local exact redundancy, record order, is scalar and acts on nothing tensorial. **A tensor Gauss law is therefore a price, not a derivation.**

## 3. Step 2: the minimal structure that hosts a rank-2 redundancy, and what it gives

**Setup.** Symmetric hᵢⱼ and Eᵢⱼ (6 pairs per coarse cell). The diagonal slots sit at vertices and the ij slots on faces. The vector rows sit on links, as in the prior note.

### Checked: `r1_modes.py`, `r1_modes2.py`

Exact lattice symbols use q = 2 sin(k/2). The identities RGᵗ = SGᵗ = BFᵗ = CSᵀ = 0 hold to 10⁻¹⁵.

| Class | Physical pairs per cell | Helicities (k ∥ z) | Slope of ω² vs k | ω² / k² (unit couplings) |
|---|---|---|---|---|
| V compact (E², R(h)²) | 6 − 3 = **3** | −2, 0, +2 | **4** (ω ∝ k²) | — |
| VS compact (C(E)², R(h)²) | 6 − 3 − 1 = **2** | ±2 | **6** (ω ∝ k³) | — |
| F compact (E², B(h)², B = curl h) | 6 − 1 = **5** | ±2, ±1, 0 | **2** (linear) | 0.5 (±1); 1 (±2, 0) |
| V + Einstein–Hilbert term h·R(h), DeWitt kinetic term | 3 | ±2, 0 | TT: ω = k | The scalar has a **zero** kinetic coefficient and potential −k²: a Jordan chain with linear secular growth |
| VS + Einstein–Hilbert term | 2 | ±2 | ω = k exactly | 1, 1 |

**Generic invariant compact Hamiltonians** (20 random positive coefficient sets each):
- V: slope exactly 4.
- VS: slope exactly 6.
- F: slope exactly 2. The median max/min ratio of mode speeds is 5.1, so the per-helicity speeds are independent numbers.

**Proved: V-class extension of the prior O(k³) bound to a single gauge.**
- Invariant h-characters satisfy kᵢmᵢⱼ = 0. By the prior note's moment argument (:186–223), m = O(k²).
- With no scalar gauge, the E-characters are O(1).
- So H_hh = O(k⁴), H_EE = O(1) and H_hE = O(k²). Rescaling x → k²x makes every entry of the Hamilton matrix O(k²).
- Hence **ω = O(k²) in the regular compact vector-gauge class.**

**Proved: the F class is linear.**
- kᵢkⱼmᵢⱼ = 0 forces m(0) = 0 but allows m = O(k), for example εᵢₐᵦkₐ.
- So H_hh = O(k²), H_EE = O(1), and ω = O(k).

**Proved: the DeWitt kinetic coefficient is fixed.** E·E − c(tr E)² is invariant under the scalar gauge δE = (q²I − qq)β on the vector-Gauss subspace iff **c = ½**. Checked: c = 0.5 gives a residual of 1e-16, other values give O(0.3–0.7) (`r1_dewitt.py`).
- So the closure of the constraint algebra, not a tuning, fixes the 3D DeWitt value.
- That value gives the transverse-trace mode zero kinetic energy. This is why V+EH without S has a Jordan chain (prior note :260–278 found the same with penalties).

**Proved: mass protection.**
- In every continuous class, an invariant h-character has zero zeroth moment, so tr h² is excluded. Its gauge variation is nonzero (checked).
- **A discrete (integer-valued) gauge parameter does not protect the mass.** If λ ∈ Z³, every function periodic in each hᵢⱼ is invariant: cos(2πhᵢⱼ) off the diagonal, and cos(πhᵢᵢ) on it. Its quadratic expansion is a full mass term. (Elementary.)

### Exact or energetic?

- **Vector Gauss law.** Each row uses exactly the six doubled-lattice neighbours of a link site (freeze note :34 context). So it *can* be a nearest-neighbour support rule of Admissibility, given a role pattern (glued-support note).
- **Scalar constraint (suggested, support-diameter count).** S takes a second difference of diagonal slots that are spaced 2 apart in doubled coordinates. Its support therefore has diameter ≥ 4, but a nearest-neighbour rule centred on a site has diameter ≤ 2.
  - On the coarse lattice, storing each face at one of its corners leaves one of the four faces at a vertex at distance 2.
  - **So S is not a nearest-neighbour rule under any covariant storage with one slot per site class.** That is a price against Admissibility :57 ("nearest-neighbor"), unless every site carries all three diagonal slots, which is a price against Qubit :47.
- **Energetic version.** This needs a supplied Hamiltonian (U_v, U_s, R and C terms), which is a price against :116–123 ("does not choose a Hamiltonian").
- **Twelfth-order magnetic scale.** In the soft-constraint version, curvature moves first at h¹²/U¹¹ (prior note). Any emergent graviton scale is then hierarchically separated from matter scales (suggested: a speed-tuning cost for (iv)).

### DOF and qubits

- **Slots needed.** There are 6 N-level slots per coarse cell, with N > 36·n·M to lift the constraints at perturbative order n (prior note :111). At first order (N ≥ 37) that is ≥ 6·⌈log₂ 37⌉ = 36 qubits per cell, plus penalties for the unused levels.
- **Three diagonal slots meet at each vertex class.** In any nearest-neighbour stencil with the vector-gauge parameter on links, ∂ⱼλⱼ lands on the same sublattice for every j. Checked by hand: the positions are equal mod Z³.
  - So **one qubit per site cannot host them**: a price against Qubit :47.
  - Or a finer lattice with longer stencils is needed: a price against Admissibility :57.
- **N = 2 slots (true qubits).** The constraints are only mod 2 and the compact bound does not apply. **Comparator** (literature, recalled; R0 to confirm): Z_N rank-2 theories are gapped fracton orders (Bulmash–Barkeshli; Ma–Hermele–Chen). They have no gapless graviton.
- **FR3.** One site's possibility algebra M₂(C) = 1 ⊕ 3 under SU(2), so a site holds no l = 2 value. Helicity-2 content must be relational, spread over slots on several sites (consistent with `SUMMARY.md:59`).

### Records as fracton charges: the analogy fails (proved, checked `r1_charges.py`)

- **No net charge from local moves.** Any compactly supported change of E leaves both the scalar charge ∂∂E and its dipole Σxρ at zero, and both the vector charge ∂·E and its angular charge Σ(xₐρᵦ − xᵦρₐ) at zero. Checked exactly on random blocks.
- **A forming record breaks this.** It adds +1 at one site: a net monopole, and a dipole change of x. So **record count cannot be a Gauss charge of any local tensor (or vector) gauge field**, scalar-charge or vector-charge.
- **Other differences.**
  - Records are unsigned and their count rises (Record :77, :80). Gauss charges are signed and conserved.
  - Records are immobile because the axioms make them permanent (:80), not because a dipole is conserved.
  - The only shared feature is immobility.

## 4. Step 3: relabelling without labels, the root cause, and (iii)

**Lemma C (proved, elementary).** Take a first-class vector Gauss law Cⱼ = ∂ᵢEᵢⱼ − ρⱼ with a gauge-invariant gravity Hamiltonian, and put H = H_grav + H_m(matter, h). Then Ċⱼ ≈ 0 iff ρ̇ⱼ + ∂ᵢTᵢⱼ = 0 with Tᵢⱼ = δH_m/δhᵢⱼ. Gauge invariance of H_m also needs ∫λ·ρ to generate the compensating transformation of matter.
- If ρ is to be matter's momentum density (the equivalence principle), **the redundancy must act on matter as local continuous translations by λ(x)**.

**Lemma D (duality obstruction; proved in its group-theory part, the matter part rests on refereed Lemma R).**
- On fixed Z³, matter's translation charge is crystal momentum, valued in the Brillouin torus T³. Its dual translation group is Z³: Bloch translations are e^{in·P} with n ∈ Z³.
- So a local relabelling redundancy *acting on lattice matter* has an integer parameter. By §3 an integer parameter permits cos(2πh), a mass. **Reading: this is the Peierls-type periodic stiffness, the lattice form of Rubakov–Tinyakov.**
- A continuous parameter forbids the mass, but then needs one of:
  - (a) integer charges: compact U(1) vector gauge, as in Gu–Wen, Xu and Pretko. Its charges are then momenta of internal circles, not spatial momentum, so (iii) fails;
  - (b) non-integer translations e^{iλ·P} on Z³. These are exactly T2's "relabelling of momenta": nonlocal in position, and blocked by Lemma R for ordinary local interacting laws that conserve momentum additively (Umklapp; `PRICE_NOTE.md:29,125`);
  - (c) matter with continuous positions (P5) or a Lorentz-invariant event substrate (P1).

**Answers to step 3.**
1. **Does a rank-2 redundancy address the root cause?** Only in the gravity sector, where it forbids tr h² (the refereed gauge-identity result). The stiffness wall's mass comes from *matter's* vacuum on labelled sites. A redundancy that does not act on matter's labels leaves that response intact, through the coupling.
   - To act on matter's labels continuously is Lemma D's horn (b) or (c).
   - To act discretely, by local integer relabelling (which means dynamical adjacency), allows the Peierls mass. **Giving up fixed adjacency by integer relabelling alone is not enough.** This agrees with the W1 referee's "suitably dynamical adjacency, which alone is not sufficient" (`PRICE_NOTE.md:205`).
2. **Is the graviton the metric that matter sees?** In every compact class, no. It is a separate field.
   - Its charges are internal vector charges (V, VS) or fractons (F), not matter's energy and momentum.
   - Making it the metric matter sees, by hopping that depends on hᵢⱼ, couples it to a lattice Tᵢⱼ that is not exactly conserved. By Lemma C the Gauss law is then explicitly broken, and the mass returns at the natural size of K3a″ (suggested).
3. **Does matter's stress source it (iii)?**
   - **F:** no. The invariance of ∫hᵢⱼTᵢⱼ under ∂ᵢ∂ⱼα needs ∂ᵢ∂ⱼTᵢⱼ = 0. With conservation this equals ∂ₜ²T₀₀, which is ≠ 0 for any moving matter, since ∂ₜ²δ(x − vt) = (v·∇)²δ. If T₀₀ were the fracton charge, an isolated body could not move, but d/dt∫xT₀₀ = P (proved, elementary).
   - **V/VS:** only via Lemma D's horns.
4. **Where could a fluctuating gauge field live? (reading)** Records are permanent (:80), so a recorded slot is frozen forever. Records may lock only gauge-invariant content (E or curvature, not h), since readout is content-determined (:82–83). A propagating graviton must therefore live in the *unrecorded* sector, whose dynamics the axioms leave open (:181–186). Densely recorded regions would pin E and stop propagation.

## 5. Prices named against the axiom text (none adopted)

| # | Price | Axiom line touched |
|---|---|---|
| R1-a | Tensor slots with a V/L/P/C role pattern: 6 slots per cell, N > 36nM levels each, 3 diagonal slots meeting at one vertex class | Lattice :40–41 ("No site is privileged … distinguished by the supplied lattice structure alone"); Qubit :47 (one M₂(C) per site); Qubit :52 (the slot clock basis is privileged) |
| R1-b | A supplied Hamiltonian (penalties plus R and C terms), or an exact support rule for the vector law | Admissibility :116–123 ("not a dynamics axiom … does not choose a Hamiltonian"); :181–186 (update laws and record-production dynamics are open) |
| R1-c | The scalar (Hamiltonian-type) constraint, needed to remove helicity 0 in V | Admissibility :57 ("nearest-neighbor": the support diameter is ≥ 4) |
| R1-d | For linear dispersion in V/VS: noncompact slots (an infinite-dimensional local domain), or an unproved non-regular mechanism | Qubit :47 (finite M₂(C)) |
| R1-e | For (iii): the redundancy acting on matter as continuous local translation. That means relabelling becomes gauge, with dynamical adjacency and continuous positions or events | Lattice :37–38 (fixed nearest-neighbour adjacency, "standard translations"); this is the same family as P1/P5 in `PRICE_NOTE.md` §5 |
| R1-f | If the graviton must fluctuate: a dynamics for the unrecorded sector | Record :80 (permanence) together with the open gates :181–186 |

## 6. Not established (open loopholes, bounded scope)

- Compact mechanisms outside the regularity hypotheses: singular Berry structure, strong coupling, nonlinear emergent gauge symmetry, infinite-order resummation, and characters with N-scaled support. The prior note lists these at :219–223.
- Matter that emerges as defects of the same tensor system. Whether the defects' Gauss charges coincide with their own energy and momentum (universality) is untested.
- The record-order redundancy (A36) as the lapse half of a gauge group on some supplied tensor sector: a reading only.
- Event substrates (lane R3) and the Lemma R escapes (non-ordinary interacting laws).
- The integer-relabelling (Peierls) statement shows that the mass is *allowed*, not its size in a given model.

## 7. Files (scratch)

- `r1_modes.py` / `r1_modes.out`: classes, counts, helicities, slopes and lattice identities.
- `r1_modes2.py` / `r1_modes2.out`: EH comparator Jordan structure, and generic invariant Hamiltonians.
- `r1_dewitt.py` / `r1_dewitt.out`: c = ½ closure.
- `r1_charges.py` / `r1_charges.out`: Gauss monopole/dipole and angular charge under local moves.
- `r1_aut.py` / `r1_aut.out`: 6000 = 48·5³ automorphisms of the cubic torus.
