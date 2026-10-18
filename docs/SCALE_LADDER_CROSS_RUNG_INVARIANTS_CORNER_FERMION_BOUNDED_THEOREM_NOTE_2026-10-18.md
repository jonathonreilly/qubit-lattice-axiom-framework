---
claim_id: scale_ladder_cross_rung_invariants_corner_fermion_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model: the corner fermion of the companion notes (flux square = plaquette = tube = pi, triangle = 0, translation-invariant gauge, L = 4 torus, number-conserving one-fermion Hamiltonians). (1) Exact on the L = 4 torus, by exhaustive computation: each of the 24 twisted site rotations maps every 12-dimensional Bloch space onto exactly one Bloch space, by k -> R k + pi s_R with one shift vector s_R per rotation (all eight shift classes occur), and exactly the two momenta k* = (pi/2)(1,-1,1) and -k* are fixed by all 24. (2) Exact representation statement with numerical certificate: the twelve Bloch states at k* (and at -k*) form a linear representation of the binary octahedral group 2O, after the GF(2) lift of the companion note, in which the central element acts as -1, decomposing as E1/2 + E5/2 + 2 G3/2. Consequently every one-fermion Hamiltonian on this torus that commutes with the 24 twisted site rotations and the translations has, at k* and -k*, only levels of even multiplicity carrying spin-1/2-class irreps; the runner illustrates this with six random symmetric Hamiltonians of strength 1 and every range on the torus, and a control at Gamma (not rotation-fixed) shows odd multiplicities. (3) Numerical, one parameter point (t1 = -1, t2 = 0.2, conjugation-odd term strength 0.05): the Weyl cone at k* has relative angular spread of its speed 2.60e-4, 6.49e-5, 1.62e-5 at |q| = 0.04, 0.02, 0.01 (ratio 4.00 per halving); the O-invariance argument that a rank-2 symmetric tensor and the linear spinor coupling are isotropic is standard. (4) Representation argument with numerical illustration: when, in addition, the site inversion and the translations up to the staggered sign (-1)^(x+y+z) are kept, every level of the 24 x 24 folded Hamiltonian at k* is 4-fold (three backgrounds with random uniform and staggered symmetric terms of strength 0.3 added to the Weyl model), so no splitting of a node quartet into two doublets (a Dirac mass) occurs at any strength or order within this symmetry class; an A2 imaginary staggered on-site term of strength eps (rotations reduced to T about a site) splits every quartet with gap/eps constant to 4e-3 relative for eps = 2e-3, 1e-3, 5e-4; with inversion broken but rotations kept, every level stays even and some are 2-fold. (5) Exact group theory: symmetric rank-2 tensors on (t,x,y,z) invariant under the 4D hyperoctahedral group (384 signed permutations) form a one-dimensional space, and under spatial O_h times time reversal (96 elements) a two-dimensional space. Not claimed: completeness of the sampled symmetric families, any interaction or many-body statement, infinite-volume or general-L statements beyond the stated representation arguments, any coarse-graining map from a one-qubit-per-site rung producing this model, a common speed across different fields, or any physical identification."
upstream_dependencies:
  - corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_bounded_theorem_note_2026-10-17
  - corner_fermion_long_wavelength_theory_is_one_isotropic_spin_half_doublet_and_one_qubit_block_embedding_bounded_theorem_note_2026-10-17
  - corner_fermion_qubit_code_genuine_cube_rotation_action_emergent_fermion_carries_spin_half_class_bounded_theorem_note_2026-10-17
runner: scripts/scale_ladder_corner_fermion_cross_rung_invariants_2026_10_18.py
---

# The scale ladder on one worked chain: what the corner fermion carries from the lattice to its long-wavelength theory

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact statements on the L = 4 torus for a supplied model, plus representation arguments; the program sections are interpretation, not claims. Nothing is adopted.

## Question

The framework's grid has one qubit per site at the finest resolution. Most results are stated much further out: neighbourhood blocks, Bloch bands, wavepackets many sites wide. Call each zoom level a **rung**. The question is whether thinking in rungs unifies the lanes.

A ladder is useful only if some data provably survives the climb, so that a statement proved at one rung can be used at another. This note tests that on the one chain where every rung is built: the corner fermion. The program sections then look at the ladder from five directions and record what probes on other lanes found.

## Result (supplied model, L = 4 torus)

1. **Lattice gauge data becomes long-wavelength momentum.**
   - Every twisted site rotation sends each Bloch space wholly onto one Bloch space, by k → Rk + πs_R. There is one shift vector s_R per rotation, and all eight shift classes occur.
   - Exactly two momenta are fixed by all 24 rotations: k* = (π/2)(1,−1,1) and −k*.
   - So the valley positions of the long-wavelength theory are read off from the lattice projective symmetry group. Without the shifts (all s_R = 0), the fixed momenta would instead be Γ and (π,π,π), the two points fixed by the linear action.
2. **The spin-½ class is carried at every strength.**
   - The twelve Bloch states at k* form a linear representation of the binary octahedral group 2O in which the central element acts as −1. It decomposes as E1/2 + E5/2 + 2 G3/2, and the same holds at −k*.
   - Hence every one-fermion Hamiltonian commuting with the twisted rotations and the translations has only spin-½-class levels at ±k*, each of even multiplicity. This holds whatever its strength or range.
   - The runner checks six random symmetric Hamiltonians of strength 1, real and complex, of every range on the torus. Level multiplicities are 2 or 4, all spinorial.
   - Control: at Γ, which is not rotation-fixed, the same Hamiltonians have some nondegenerate levels.
3. **Isotropy emerges with quadratic suppression.**
   - O-invariance forces the linear Weyl term to be v σ·q, isotropic, and any rank-2 symmetric tensor to be a multiple of the identity.
   - The first anisotropy enters at relative order |q|². In the Weyl model the angular spread of the cone speed is 2.60e−4, 6.49e−5 and 1.62e−5 at |q| = 0.04, 0.02 and 0.01: a ratio of 4.00 per halving.
   - A packet of width w has |q| ~ 1/w, so its anisotropy is of order (a/w)², with a the lattice spacing.
4. **The Dirac mass is natural in 't Hooft's sense.**
   - Keep the site rotations, the site inversion and the translations (allowing the staggered sign (−1)^(x+y+z)). Then every level of the folded Hamiltonian at k* is 4-fold.
   - Representation argument. The rotations decouple the E1/2, E5/2 and G3/2 sectors. Inversion maps k* to −k* and maps the E1/2 sector onto the E5/2 sector (the two differ by the pseudoscalar character A2), so their levels coincide. Each G3/2 level is already 4-dimensional.
   - So within this symmetry class no node quartet splits into two doublets, at any strength or order. The runner illustrates this with three backgrounds that add random symmetric uniform and staggered terms of strength 0.3.
   - An A2 imaginary staggered term of strength ε reduces the site rotations to T and splits every quartet. The gap/ε is constant to 4e−3 relative for ε = 2e−3, 1e−3 and 5e−4.
   - Control: with the rotations kept and inversion broken, every level stays even but some become 2-fold. The two valleys separate in energy, and the Weyl doublets stay pinned.
5. **What fixes a common speed (exact group theory).**
   - Only one symmetric rank-2 tensor on (t,x,y,z) is invariant under the 4D hyperoctahedral group of signed permutations of all four axes: the identity.
   - Under spatial O_h times time reversal there are two, δ_00 and δ_ij.
   - So a leading kinetic term of the form K_μν k_μ k_ν has one common speed for every field only if time is on the same footing as space. Otherwise each field's speed is a separate parameter.

## How the ladder looks from five directions (interpretation, not claims)

The worked chain is:

| Rung | Degrees of freedom | Map to the next rung | Source |
|---|---|---|---|
| 0 | one qubit per fine site | equivariant placement of 48 qubits on two free orbits of a 5×5×5 block (77 spectators; range ≤ 9 fine spacings) | long-wavelength note, item 5 |
| 1 | 48-qubit corner site | stabilizer code: fluxes and parities fixed, logical corner fermion (12 modes per site) | corner-code note; qubit dictionary, campaign C20 |
| 2 | corner fermion, 12 bands | Bloch projection to the isolated levels at ±k* | long-wavelength note, Dirac-pair note |
| 3 | four node states (two Weyl doublets) | small-q expansion, packets of width w ≫ a | Dirac-pair note, this note |
| 4 | continuum Weyl/Dirac field | — | — |

The rung 0 → 1 map is an encoding chosen by hand. A uniform one-qubit dynamics producing it is open.

### 1. Coarse-graining maps

Each rung transition is an encoding (an isometry from coarse to fine) followed by a projection onto a slow or low-energy subspace (a Bloch band, a Schrieffer–Wolff block).

- **The upside.** Every rung is explicit, so statements are maps, not slogans.
- **The cost.** The composite map is not unique. The question is not "is there a ladder" but "which data does every admissible ladder preserve". That question is the next direction.

### 2. Invariants that survive every rung

Anomaly matching ('t Hooft), Lieb–Schultz–Mattis-type constraints and projective symmetry classes are statements that some data cannot change under any symmetric map. Items 1 and 2 are instances.

- **The class.** The projective class of the lattice symmetry action reappears as the spin-½ class at the fixed momenta. It does so for every symmetric Hamiltonian, not just the one studied.
- **The shifts.** The gauge-data shifts s_R reappear as the valley positions.

This is the strongest unifying mechanism found. An obligation stated as an invariant can be discharged at whichever rung it is easiest to compute, then transported. The Maxwell probe below found the same pattern for the Gauss law: block sums of Gauss operators equal boundary flux exactly, so the electric 1-form symmetry survives coarse-graining.

### 3. Effective field theory and naturalness

Universality says a higher rung depends on a lower one only through its invariants and a few relevant couplings. Irrelevant operators are suppressed by powers of a/w.

- **Isotropy (item 3).** It costs nothing extra. O forbids every anisotropy below relative order (a/w)².
- **Small masses (item 4).** They are technically natural: m → 0 restores a symmetry, so the mass is proportional to the breaking.
- **Objection: per-field isotropy is not a common light cone.** Cubic symmetry makes each field's rank-2 kinetic tensor isotropic. It does not force two fields to share one speed. Loop corrections generically move speeds apart at order one, the fine-tuning problem of Collins et al. (2004).
  - The Weyl speed here, v ≈ 0.110 in lattice units, is unrelated to any gauge-field speed.
  - The Maxwell probe found the same gap in the gauge lane: a two-doublet coin has photon speeds 0.618 and 1.618, which is a consistent infrared theory.
  - A common light cone needs its own mechanism: a common dynamical origin, or a flow to a Lorentz-invariant infrared fixed point (Chadha and Nielsen 1983, where speeds converge only logarithmically).

  This is the clearest place where the ladder does not supply the answer by itself. Item 5 shows what would: time on the same footing as space (see the answer below).

### 4. Information-theoretic coarse-graining

A rung map is a quantum channel. Data processing then says that distinguishability can only fall going up.

- **What a higher rung can resolve.** Only what survives the channel: invariants, conserved charges and redundantly recorded data.
- **Records.** This is the natural home for the Record lane. A record is information copied redundantly enough to survive coarse-graining, the quantum Darwinism picture.
- **Conservation.** The channel view also shows what coarse-graining cannot give. A channel that discards fine data is generically dissipative, so energy conservation at a higher rung needs a Hamiltonian at that rung. The Maxwell probe reached the same conclusion for its conservation item.

### 5. Codes at every scale

Every rung is an encoding of the one below:

- block placement;
- the corner stabilizer code, whose checks are the fluxes;
- Bloch states spread over L³ sites;
- wavepackets spread over (w/a)³ sites.

A packet's logical content is spread over a "huge neighbourhood". A local operator at the finest rung therefore moves it only by order (a/w)³ per site touched. This is the code-theoretic reading of why large objects are robust to finest-scale structure. It has the same shape as the holographic and multiscale-entanglement codes (Vidal 2007; Swingle 2012; Almheiri, Dong and Harlow 2015).

## Lane probes (interpretation, not claims)

Four fresh-context agents of the same model family probed eight scorecard lanes. They are not independent reviewers. Scripts and logs are in `.claude/science/physics-loops/toe-campaign-20261017/scale_ladder_probes/`.

Each verdict is the probing agent's, with its own numbers. None is checked here beyond what the runner does. "Resolved" means a precise answer to a sub-question, not a closed lane.

| Lane | Resolved or sharply diagnosed | Reframed | Not helped |
|---|---|---|---|
| Emergent electron (this note) | Valley positions and the spin-½ class carried from the lattice to every symmetric Hamiltonian; isotropy to (a/w)²; mass natural | Mass mechanism: campaign C20 (in progress) finds that interaction susceptibilities favour a different channel | Global low-energy feature; charge |
| Finite-spin EM response | The historical stiffness 0.0756 is exactly K_T(π,π,π)/3, a zone-corner quantity. The 1/3 is the transverse fraction for k ∝ (1,1,1). The physical target is lim_{q→0} K_T(q) | Flux-sector target becomes the scaling of conserved winding-sector energies with 1/L | Sampling health; readout time |
| Conditional Maxwell dynamics | Kernel B(q²−qqᵀ) is unique; anisotropy is irrelevant (speed spread/q² = 1/36) | "Radius one" is not an infrared observable; a coin is excluded only by a branch count (one coin passes with two light cones, 0.618 and 1.618) | Time rule; conservation, where coarse-graining adds dissipation |
| Gravity / source-action | With exact linearised diffeo redundancy and hypercubic symmetry in four dimensions, one gauge-invariant two-derivative spin-2 form remains: linearised Einstein–Hilbert, with two polarisations at speed 1 along every tested axis | Hamiltonian time with only spatial O_h allows a cubic invariant g3 that gives leading-order birefringence ({1, 1.10} along [100] at g3 = 0.1); source universality becomes a Noether identity | Supplied continuum actions; cosmological constant (unprotected) |
| Native transfer / spatial gauge | One-link 1/β coefficients are scheme: matching gives τ_eff = (3/β)(1 + 7/(4β) + …) | Mass gap: carry the centre 1-form symmetry (area law) across β; a Gaussian-limit gap ~2π/L is kinematic | The gap proof itself (Balaban/Clay) |
| Formation | iid-priority finite-range formation is a finitary factor of iid noise with super-exponential coding radius, hence at the trivial fixed point (proof to be written); explains the uniform-ice no-go | Static versus formation readings differ only in non-universal data at the native triple | Formation-time support |
| Handedness | Nielsen–Ninomiya makes the corner Weyl pair forced and minimal | The four handedness notions become four different cross-rung invariants; a lattice chiral-magnetic probe shows the infrared Weyl theory alone mispredicts a current that the lattice cancels | Selection of the matter representation |
| Record apparatus | — | The 1e-13 mediated fine-tuning looks like a hidden phase-reference (clock) obligation: in a toy model only the differential endpoint detuning is relevant (tolerance ≈ 0.115 λ_eff); the decay rate and GKSL time could come from a weak-coupling (Davies) limit | Permanent halt; preparation (needs a non-unital low-entropy resource) |
| Readout weights | Frequency consistency for order-blind formation from 1-dependence, hence ergodicity (conditional; to be checked) | Block-rung Gleason plus rung-consistency; finite Clifford-closed apparatus leaves 205 free frame-function dimensions against 15 | Menu abundance; the fair-coin weight class |

## Answer to the question (interpretation)

The ladder does unify the lanes, but not by deriving everything from the finest rung. It gives three exact tools that every lane can use. It also collects what is left open onto a short list of shared primitives.

**The three tools.**

1. **Transport of invariants.** Data that no admissible coarse-graining can change can be computed at whichever rung is easiest, then used at any other:
   - projective classes;
   - affine momentum shifts;
   - Gauss laws and 1-form symmetries, whose block sums equal boundary flux exactly;
   - winding sectors;
   - Weyl monopole charges;
   - anomaly data.
2. **Uniqueness from symmetry plus redundancy, with power-law suppression.**
   - Lattice symmetry and a gauge redundancy leave one leading form in three lanes: Weyl/Dirac, Maxwell and linearised Einstein–Hilbert.
   - Corrections are of order (a/w)².
   - Masslessness and small masses are protected.
3. **Limits from treating coarse-graining as a channel.** This says what coarse-graining cannot supply:
   - conservation, which needs a Hamiltonian at that rung;
   - purity and preparation, which need a low-entropy start;
   - permanence;
   - Born weights from a finite apparatus set.

**Wrong-rung diagnoses.** Several open items turned out to be questions asked at the wrong rung:
- the 0.0756 stiffness;
- one-link 1/β coefficients;
- kinematic 2π/L gaps;
- iid-priority formation, which cannot carry long-range order;
- the six qubits per site that the corner code replaced.

**The answer the probes converge on.** Three lanes independently hit the same wall: a common light cone.
- Per-field isotropy is free.
- A common speed across fields is not, and neither is spin-2 isotropy, when time is treated apart from space: item 5 and the gravity probe's g3.
- With time on the same footing as space, as a 4D hypercubic step of a transfer matrix, the invariant kinetic tensor is unique. One speed then serves the electron, the photon and the graviton at leading order. Lorentz violation starts at dimension six, suppressed by (a/w)². This is how Euclidean lattice field theory recovers Lorentz invariance.
- Real-time physics then also needs reflection positivity, so the transfer matrix defines a Hamiltonian. That is the Maxwell lane's open transfer route, and it would also supply conservation.

**The single highest-leverage primitive** is therefore a reflection-positive transfer step with 4D hypercubic symmetry, acting on the one-qubit-per-site grid. It is a target to derive or propose to the owner, not an adopted axiom. If supplied, it would discharge at once:
- the common-cone obligations of the electron, Maxwell and gravity lanes;
- Maxwell items 2 and 6;
- the Collins fine-tuning at dimension four.

**The other shared primitives the ladder isolates.**
- **Exact redundancies at the coarse rung.** Gauss is exact; diffeo is only locus-closed.
- **A low-entropy start.** Needed for preparation, records and any formation order.
- **Values of relevant couplings.** Masses, scales and the cosmological constant are transported by the ladder but never fixed by it.

**What the ladder does not touch.** The Born abundance assumption, permanence, the mass-gap proof, and band-structure questions such as whether the Dirac point is the global minimum.

## Premises

- **Axioms used.** Lattice (Z³, unit translations, proper cubic rotations about sites).
- **Supplied.**
  - The corner model and flux pattern.
  - The one-fermion Hamiltonians and the sampled symmetric terms.
  - The twisted realization of the companion notes, for the spin labels.
- **Standard facts used.**
  - Schur's lemma and character theory of 2O.
  - The O-invariant tensors of low rank.

## Relation to prior work

- **Projective symmetry groups and fractionalization.** Wen, PRB 65, 165113 (2002).
- **Lieb–Schultz–Mattis-type constraints.** Lieb, Schultz and Mattis, Ann. Phys. 16, 407 (1961); Oshikawa, PRL 84, 1535 (2000); Hastings, PRB 69, 104431 (2004).
- **Anomaly matching.** 't Hooft, NATO Sci. Ser. B 59, 135 (1980).
- **Renormalization group.** Wilson and Kogut, Phys. Rep. 12, 75 (1974).
- **Emergent Lorentz invariance and its fine-tuning problem.**
  - Chadha and Nielsen, NPB 217, 125 (1983).
  - Collins, Perez, Sudarsky, Urrutia and Vucetich, PRL 93, 191301 (2004).
- **Multiscale and holographic codes.**
  - Vidal, PRL 99, 220405 (2007).
  - Swingle, PRD 86, 065007 (2012).
  - Almheiri, Dong and Harlow, JHEP 04 (2015) 163.
- **Quantum Darwinism.** Zurek, Nat. Phys. 5, 181 (2009).
- **Reflection positivity of lattice gauge theories.** Osterwalder and Seiler, Ann. Phys. 110, 440 (1978).
- **Fermion doubling.** Nielsen and Ninomiya, NPB 185, 20 (1981).
- **Results cited by the lane probes.**
  - Gleason, J. Math. Mech. 6, 885 (1957).
  - Davies, Commun. Math. Phys. 39, 91 (1974).
  - van den Berg and Steif, Ann. Probab. 27, 1501 (1999).
- **New here.**
  - The fixed-momentum spinor statement for every symmetric corner-fermion Hamiltonian.
  - The O × I protection of the Dirac quartet at every strength.
  - The cone anisotropy scaling.
  - The cross-lane reading.

## No-Go Discipline Gate

- **N1 — routes.** Interacting and many-body versions of items 2 and 4; other flux patterns; general L.
- **N2/N3 — scope.** One flux pattern, L = 4, sampled symmetric families.
- **N4 — inputs.** Floating-point diagonalization with tolerance 1e-8 for degeneracies.
- **N5 — wording.** "Rung" and "ladder" are organizing words for the program sections, not defined objects of a theorem.
- **N6/N7 — strongest objections.**
  - The rung 0 → 1 encoding is not derived from dynamics.
  - Item 3 is one parameter point.
  - A common speed across fields is not addressed.
- **N8 — earlier claims.** Extends the corner-fermion notes. It does not change them.

## Verification

```bash
python3 scripts/scale_ladder_corner_fermion_cross_rung_invariants_2026_10_18.py
```

Expected: `TOTAL: PASS=12 FAIL=0` (about three minutes).

## Load-bearing sources

- [Dirac-pair note](CORNER_FERMION_MASSLESS_DIRAC_PAIR_PROTECTED_BY_CUBE_ROTATIONS_AND_PSEUDOSCALAR_DIRAC_MASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Long-wavelength note](CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Corner-code note](CORNER_FERMION_QUBIT_CODE_GENUINE_CUBE_ROTATION_ACTION_EMERGENT_FERMION_CARRIES_SPIN_HALF_CLASS_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
