# Deferred original campaign narrative

This submitted narrative is preserved for inspection, not as active scientific authority. Historical statements that claim checks, absent phase-two evidence or broad exclusions are not adopted. The corrected canonical note and live mathematical sources state the current premises and boundaries. All original bytes are additionally preserved in the recovery archive.

## How the ladder looks from five directions (interpretation, not claims)

The worked chain is:

| Rung | Degrees of freedom | Map to the next rung | Source |
|---|---|---|---|
| 0 | one qubit per fine site | equivariant placement of 48 qubits on two free orbits of a 5×5×5 block (77 spectators; range ≤ 9 fine spacings) | long-wavelength note, item 5 |
| 1 | 48-qubit corner site | stabilizer code: fluxes and parities fixed, logical corner fermion (12 modes per site) | corner-code note; qubit dictionary, campaign C20 |
| 2 | corner fermion, 12 bands | Bloch projection to the isolated levels at ±k* | long-wavelength note, Dirac-pair note |
| 3 | four node states (two Weyl doublets) | small-q expansion, packets of width w ≫ a | Dirac-pair note, this note |
| 4 | continuum Weyl/Dirac field | — | — |

The rung 0 → 1 map is an encoding chosen by hand, and campaign block C6 (checked) found no derivation: the flux is a free sector label of the local fermionization, and no translation-covariant formation rule from an empty start can register a coarse block lattice (summary item 7). A uniform one-qubit dynamics producing it is open.

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
- **Objection: per-field isotropy is not a common light cone.** Cubic symmetry makes each field's rank-2 kinetic tensor isotropic. It does not force two fields to share one speed. Loop corrections move speeds apart by amounts set by the couplings rather than suppressed by the cutoff: the fine-tuning problem of Collins et al. (2004).
  - The Weyl speed here, v ≈ 0.110 in lattice units, is set by the supplied term X and is unrelated to any gauge-field speed.
  - The Maxwell probe found the same gap in the gauge lane: a two-doublet coin has photon speeds 0.618 and 1.618, which is a consistent infrared theory.
  - A common light cone needs its own mechanism: a common dynamical origin, or a flow to a Lorentz-invariant infrared fixed point (Chadha and Nielsen 1983, where speeds converge only logarithmically).

  This is the clearest place where the ladder does not supply the answer by itself. Item 5 gives one sufficient route: time on the same footing as space. The campaign found a second route, constraint closure with gravity; it comes with a derivation, but one that is conditional and leading-order (see the answer below).

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

A packet's logical content is spread over a "huge neighbourhood". Heuristically, a local operator at the finest rung acts on it with amplitude of order (a/w)^(3/2) per site touched. This is the code-theoretic reading of why large objects are robust to finest-scale structure. It has the same shape as the holographic and multiscale-entanglement codes (Vidal 2007; Swingle 2012; Almheiri, Dong and Harlow 2015).

## Lane probes (interpretation, not claims)

Four fresh-context agents of the same model family probed eight scorecard lanes. They are not independent reviewers. Scripts and logs are in `.claude/science/physics-loops/toe-campaign-20261017/scale_ladder_probes/`.

Each verdict is the probing agent's, with its own numbers. None is checked here beyond what the runner does. Entries the campaign later superseded are marked. "Resolved" means a precise answer to a sub-question, not a closed lane.

| Lane | Resolved or sharply diagnosed | Reframed | Not helped |
|---|---|---|---|
| Emergent electron (this note) | Valley positions and the spin-½ class carried from the lattice to every symmetric Hamiltonian; isotropy to (a/w)²; mass natural | Mass mechanism (campaign C20, since done: see the follow-up table) | Global low-energy feature; charge |
| Finite-spin EM response | The historical stiffness 0.0756 is exactly K_T(π,π,π)/3, a zone-corner quantity. The 1/3 is the transverse fraction for k ∝ (1,1,1). The physical target is lim_{q→0} K_T(q) | Flux-sector target becomes the scaling of conserved winding-sector energies with 1/L | Sampling health; readout time |
| Conditional Maxwell dynamics | Cubic covariance plus gauge invariance fix the kernel B(q²−qqᵀ) (as in the repo's kernel-uniqueness note); anisotropy is irrelevant (speed spread/q² = 1/36) | "Radius one" is not an infrared observable; a coin is excluded only by a branch count (one coin passes with two light cones, 0.618 and 1.618) | Time rule; conservation, where coarse-graining adds dissipation |
| Gravity / source-action | With exact linearised diffeo redundancy and hypercubic symmetry in four dimensions, one gauge-invariant two-derivative spin-2 form remains: linearised Einstein–Hilbert, with two polarisations at speed 1 along every tested axis | Hamiltonian time with only spatial O_h allows a cubic invariant g3 that gives leading-order birefringence ({1, 1.10} along [100] at g3 = 0.1; in the repo's curvature member, constraint closure forces ε₃ = 0: campaign B4); source universality becomes a Noether identity | Supplied continuum actions; cosmological constant (unprotected) |
| Native transfer / spatial gauge | One-link 1/β coefficients are scheme: matching gives τ_eff = (3/β)(1 + 7/(4β) + …) (campaign B12: the 7/4 is the 2D shift) | Mass gap: carry the centre 1-form symmetry (area law) across β; a Gaussian-limit gap ~2π/L is kinematic | The gap proof itself (Balaban/Clay) |
| Formation | iid-priority finite-range formation is a finitary factor of iid noise with super-exponential coding radius, hence at the trivial fixed point (proof since written and checked: campaign B3); largely explains the uniform-ice no-go (heavy-tailed finitary codings not excluded) | Static versus formation readings differ only in non-universal data at the native triple, and may sit in different phases at strong coupling (finite Monte Carlo) | Formation-time support |
| Handedness | Nielsen–Ninomiya makes the corner Weyl pair forced and minimal | The four handedness notions become four different cross-rung invariants; in a two-band toy Weyl model (not the corner model; sign convention unresolved), the infrared Weyl theory alone mispredicts a current that the lattice cancels | Selection of the matter representation |
| Record apparatus | — | The 1e-13 mediated fine-tuning looks like a hidden phase-reference (clock) obligation: in a toy model only the differential endpoint detuning is relevant (tolerance ≈ 0.115 λ_eff); the decay rate and GKSL time could come from a weak-coupling (Davies) limit | Permanent halt; preparation (needs a non-unital low-entropy resource) |
| Readout weights | Frequency consistency for order-blind formation from 1-dependence, hence ergodicity (conditional; since checked: campaign B8) | Menu abundance and regularity become block-rung Gleason plus rung-consistency; finite Clifford-closed apparatus leaves 205 free frame-function dimensions against 15 | The fair-coin weight class |

### Campaign follow-up, 2026-10-18 (interpretation)

A campaign of two 12-hour phases converted the strongest probe leads into proofs or decisive computations. Workers and checkers are fresh-context agents of the same model family, not independent human reviewers. Here "checked" and "independently checked" mean a different code path, not a different model lineage. Evidence is in `.claude/science/physics-loops/scale-ladder-campaign-20261018/`; the proved lane statements are in companion lane notes (PR #9718).

| Lane | Campaign result |
|---|---|
| Formation | **Proved.** Every iid-priority, finite-range formation rule (iid activation times, or a fixed, state-independent rate profile; the 09-22 state-dependent rates are not covered) is a finitary factor of iid noise with a factorial coding-radius tail. From an empty start, no long-range order, power laws, pinch points or proper 3-colourings arise. Checked. |
| Readout weights | **Proved, partial.** Spatial frequencies converge with explicit rates for that class. This is a partial, conditional discharge of the frequency-consistency obligation; the limits equal the rule weights only for order-blind rules. Checked. |
| Emergent electron | **Corner model.** Parameter-free step rules (item 6): an isotropic spin-½ Weyl step at speed √2/3 with six cube-point doublers. **Proved** (checked): odd filling is forced gapless by anticommuting gauge-dressed C2 lifts. The doubling corollary (checked) holds for gapped steps and pocket-free odd-filling Hamiltonians. In mean-field RPA, interaction channels favour the chiral triangle term over the Dirac mass for T ≲ 0.03; at higher temperature the channel is unresolved (checked; C20 lane note). The step is an exact range-1 circuit of two-mode fermionic gates on the corner code, with two-mode depth ≤ 16. In the many-body Gaussian sense its shift is Clifford and its link reflection is Clifford plus π/8 rotations, but its on-site factors are not exact Clifford+T (B11, checked). Constraint closure rejects its doublers (B17–B22, below). |
| Gravity | **One cone, closure.** Every gauge-invariant two-derivative form gives both TT polarisations one cone (symbolic determinant). Lattice constraint closure leaves only the DeWitt ray, conditional on supplied clauses (Hojman–Kuchař–Teitelboim analogue). With matter, closure forces one common matter cone and the Lorentzian sign at leading order; the relabelling bracket fails at O(a²). The 06-08 induced bubble needs an underived seagull, so the induced 1/G is not fixed. Checked. |
| Native transfer | **One loop.** The heat-kernel saddle action vs Wilson in 4D gives Λ_HK/Λ_W = 1.819 for SU(3); the probe's 7/4 was the 2D shift. Checked. |
| Record apparatus | **Hypothesis refuted.** The hidden-clock hypothesis fails for the certified tolerances, which are budget and linewidth choices with large margins. The nominal-clock term is an undetectable global phase. The physically real 1/T effects are clock-rate errors: receiver and global onsite errors. Checked. |
| Finite-spin EM | **Partly settled.** The ring model is exactly the cubic spin-½ U(1) quantum link model, and it is sign-free: the sign of J is a gauge choice on even L. Diffusion Monte Carlo with forward walking and a twisted-energy cross-check gives a magnetic-source curvature χ ≈ 0.23–0.25 on 4³–8³ for 0.5 ≤ V ≤ 1, with no size dependence. That is consistent with, but does not prove, a Coulomb-type stiffness. For V ≤ 0 population bias is uncontrolled, and 4³ shows a real suppression whose cause is unexplained. Checked. |

## Answer to the question (interpretation)

### What the campaign established (summary)

Labels: "checked" means a fresh-context agent of the same model family re-derived the load-bearing step with its own code: a different code path, not a different model lineage. C20's check is recorded in the Independent-check section of its lane note; its folder `C20_check` holds scripts and outputs but no REPORT.md. The lane theorems live in the companion lane notes; this list only points to them.

1. **Lattice data reaches the top rung (this note; exact on L = 4, plus representation arguments).** The PSG fixes the valleys ±k* and the spin-½ class for every symmetric one-fermion Hamiltonian. Isotropy holds to (a/w)², and O × I protects the Dirac quartet. At the eight cube points every level is even: ±k* have little group O, so cones there are isotropic; the two 3-orbits have little group D4, which allows uniaxial cones.
2. **Filling (B7 and C20, checked).** Odd filling is forced gapless for free fermions, and a pocket-free state at odd filling touches μ at all eight points. With full translations a many-body obstruction holds conditionally. In the doubled-cell class a symmetric interacting insulator exists, so the quartet protection is free-fermion only. In mean-field RPA the chiral term beats the Dirac mass for T ≲ 0.03.
3. **Parameter-free steps (item 6).** The diagonal-shift step has isotropic spin-½ Weyl nodes at ±k*, with speed √2/3. It also has six uniaxial doublers and a mirror eight-node set at −π/2. The doubling corollary (checked) says that a gapped symmetric step cannot reach a k* Weyl doublet's quasi-energy only at ±k*.
4. **One cone from constraint closure (B14–B16, B19, B21; checked; supplied matter and gravity clauses; leading order).** A scalar, a naive Weyl field and a lattice Maxwell field close against the 09-24 curvature member only on one common cone, with the Lorentzian sign (given K, α > 0). Invariantly that cone is the graviton TT cone K2/(4α); it reads K/(4α) only in block 62's normalisation. Beyond leading order the lattice relabellings do not close: O(a²) for the scalar and the endpoint-mean fermion, O(a) for one-sided Maxwell. Newton's constant is not fixed.
5. **A selection rule on steps (B17, B18, B20 and B22; checked).** Closure rejects anisotropic cones, so the corner step's uniaxial doublers fail. This is conditional on the step coupling to a lapse. The generator lapse (B22) gives that coupling only by a choice, and it needs a branch cut in a quasi-energy gap, which the gapless corner step lacks. No uniform taste maps the doublers to ±k* (B18). No tested word passes: none of 69,894 Weyl pairs, and none of the 10,174 isotropic Dirac levels in those families (B20 check and B23, both checked). Levels with spin-3/2 content, mixed or pure, are unscreened (B23).
6. **Other lanes (checked; companion notes).**
   - **Formation.** iid-priority formation with state-independent rates is a finitary factor of iid noise: an empty start gives no long-range order.
   - **Record frequencies.** Spatial Record frequencies converge, a partial discharge.
   - **Graviton kernels.** They have one TT cone, and closure selects DeWitt. The induced bubble needs an underived seagull, so the induced 1/G is not fixed.
   - **Λ ratio.** Λ_HK/Λ_W = 1.819 for SU(3) at one loop.
   - **Record clock.** The hidden-clock hypothesis is refuted.
   - **Ring model.** χ ≈ 0.23–0.25 for 0.5 ≤ V ≤ 1; nothing is claimed for V ≤ 0.
7. **Phase 2 (C1–C4b, C6–C12, B24–B26; each checked by a fresh-context same-family agent).**
   - **Exact lattice closure (C3; C3 arc-lemma note).** Take a translation-covariant relabelling algebra of any range that closes within its span with field-independent structure constants, and whose longest-wavelength mode acts nontrivially. Then Λ_n/Λ_1 = n − (arc centre) on arcs of momenta, so Λ_2/Λ_1 ≤ 0 against the continuum value 2. Such algebras exist: exact closure is possible, but not with the continuum spectrum. The uniform-lapse bracket needs a non-local product (anti-aliased SLAC or band-limited). Campaign block C9 (checked) bounds the lemma's scope:
     - At a background the relabellings move, field-dependent structure functions evade it. A 1D ruler model (an affine field-space model, not a relabelling of a periodic field) closes exactly with Λ_2/Λ_1 = 2cos(2π/L), or Λ_n ∝ n for SLAC. There closure is automatic (a frame), so it no longer constrains the spectrum.
     - At a common zero with continuous structure functions the lemma holds in gap form, so for linear relabellings about the vacuum it stands.
     - Enlarged generator sets reach Λ_n ∝ n only with at least two generators at each of the momenta 0 and ±1. The examples are abstract graded algebras; realisation by lattice relabellings is open.
   - **Lattice Hamiltonian constraint (C10; lane note in PR #9718).** In 1D, with one clock pair and no local degrees of freedom (a 0-dimensional reduced phase space), the naive lattice H and D are first class on an explicit open set for every antisymmetric difference. At a uniform background (a winding sector) they reproduce the Dirac algebra with δ′ replaced by the difference. That closure is cheap: the constraints factorise, and this is C9's moved-background mechanism carried over to constraints.
     - For lattice parametrised field theory, which has local degrees of freedom, the naive constraints are anomalous for every antisymmetric difference. When the constraint is solvable for the embedding momentum with a diagonal coefficient, first-classness is exactly a local zero-curvature equation for the Kuchař density.
     - Exact certificates (central difference) exclude flat germs in the listed small windows, including those where the embedding enters only through its difference. A broader shift-invariant window has flat first-order jets; higher order, and so whether an exact finite-range solution exists, is open.
     - At a background the gauge flow moves, whether the continuum-like structure appears depends on the basis chosen for the constraints; first-classness depends only on the constraint surface.
   - **Normalisation of h (C4, C4b; C4b walker-closure note).** The walker's frame identification fixes unit matter coupling, a_s = 1, by definition (C4). Closure with the walker as matter then forces γ = a_s K1/K2 = 1, so K1 = K2 in block-62 variables. With the walker's speed 1, both cones sit at that speed and α = K2/4. This holds in the continuum, at leading order, with isotropic ansätze and the k = 0 species. Within those premises it answers block 62 T4's "nothing forces that value". At the next order the walker needs the totally antisymmetric Levi-Civita spin-connection term, whose first-order lattice form is block 65. For spin ½ a connection term absorbs the Kosmann remainder, so {G, G} closes without a triad.
   - **Doublers (C1; C1 doubler note).** Under full O a single pair condensate is all-or-nothing at the eight cube points, and keeping ±k* gapless tunes one number. The doublers alone, and ±k* alone, carry the Weyl dipole π(1,1,1): half a Hall quantum per layer. So gapping either set alone into a symmetric short-range-entangled state is excluded. This Z2 obstruction is conditional on a Hamiltonian reading of the step and on Hall quantisation. A compensating sector (gapless, topologically ordered or symmetry-breaking) is required. With O broken, selective channels exist, but they do not protect ±k*.
   - **Seagull and 1/G (C2; campaign evidence, no lane note).** Within ≤ 2 derivatives, closure fixes the seagull: the minimal covariant one. Its tadpole is a pure contact, so it does not cure the 06-08 Ward break, which depends on regulator and measure. Covariant dimension-6 couplings respect closure and Ward and shift the induced 1/G by O(1) on a lattice, so closure cannot fix 1/G.
   - **Rung 0 → 1 (C6; C6 registration note).** No map is derived. The 12-corner space, the π-flux background and the block embedding are supplied. Local fermionization leaves the flux a free sector label, the PSG exists for all 16 uniform patterns, and node-filling energetics ranks the corner pattern 15th–16th of 16. The registration lemma is exact: no measurable translation-equivariant factor of iid noise registers a coarse block lattice or has Bragg peaks off 2πZ³, so no covariant formation rule from an empty start does.
   - **Emergent corner fermions (C7; campaign evidence, no lane note).** A translation-invariant Kitaev-type Γ-matrix model on the corner graph (36 qubits per site, Cl(7)) is exactly solvable: its partons hop in a static Z2 field. Majorana hopping cannot carry π on the triangles, so the corner pattern is not available. At the model's natural filling, the lowest of the searched static sectors has π on every 4-cycle and ±π/2 triangles. It is a gapped Z2 spin liquid with spontaneous T- and mirror-breaking flux order and no O-fixed momentum, so not the corner model. No member of the corner family with the chiral λ term is gauge-equivalent to it. This is a comparison of searched sectors with no Lieb-type theorem, and the margin to the runner-up is O(t2⁴) at small t2.
   - **Taste routes (B24, B25; campaign evidence).** No rotation-invariant translation lattice, at any scale, makes every commuting-C2-pair point T-fixed (exact). Enlarging the tastes only moves the bad points: 0 of 449 classified survivors pass, and 353 were not classified. Pinning follows the unitary taste lattice and isotropy the spectral one. B25's index lemma (exact) shows that tastes with k-independent intertwiners give only bad pairs. A good pair therefore needs tastes with no such intertwiner, and a 2,008-word census realises none. The closest family (2,340 words) gives 0 clean steps. Pinning at C2-pair points is observed (225 of 225), not proved.
   - **New shift letters (B26; lane note with C8 in PR #9718).** Within translation-invariant monomial letters that are O-covariant up to a character, the only letters are z·S^a and A2 "half-letters" z·A0·S^a, with A0 the on-site antipodal map (exact proof; enumeration to range 4 in the check). A0 conjugates S to S⁻¹ and maps the on-site palettes to themselves up to phases, so every symmetric word with A letters equals a phase times an old-palette word. This adds no velocity source and no new taste, and L1 holds with a sign-flipped effective n_S. A screen of about 73k enlarged-palette words found 0 passing steps (negative search; it does not cover the S^{±3} reductions some such words produce).
   - **Letters beyond monomials (C8; lane note with B26 in PR #9718).** Momentum-shifting letters reduce to old words wherever this was settled exactly. The one O-compatible shift, by π(1,1,1), is the existing k* ↔ −k* taste. Antiunitary steps reduce to their squares, which are old words. Among the π/4 exponentials examined, exp(±iπ/4·R_L) is the only new letter. It adds no velocity source, and its tastes stay on B24 lattices (120-word census). A screen of 69,660 levels with it found 0 passing steps. Every O-symmetric letter tested acts as a scalar on the k* doublet and only rescales its speed; C8 observed this numerically, and C11 below proves it for isolated doublets. So new letters cannot help at k*; the obstruction sits at the other nodes and in the tastes.
   - **Generalised speed law (C11; lane note in PR #9718).** By Schur's lemma and Wigner–Eckart at the full-O point ±k* (exact, given numerically certified model facts), any product of O-covariant letters has an untilted isotropic cone on an isolated spin-½ doublet. Its speed is |Σ_j v_j|, one real coefficient per letter: ±√2/3 for S, 0 for R_L, Rt, exp(iθR_L) and all on-site letters. L1 and B26's sign-flipped n_eff are special cases.
     - With generic symmetric letters, a 4-fold level at ±k* made of both doublets (D₊⊕D₋) generically carries two cones of different speeds. In about 30% of cases they have the same chirality, total Berry charge ±2 (checked by Berry flux). This replaces, for generic letters, the equal-speed, opposite-chirality Dirac point of the B20 word class.
     - The zero-winding lemma (B20's L3) extends exactly to words in these letters. So a same-chirality node forces a compensating ∓2 charge elsewhere at the same quasi-energy, at points where isotropy is not forced on the basic translation lattice (conditional on Bessho–Sato, as for L3). B20's conditional obstruction therefore reaches these levels too. The opposite-chirality ones generically have two speeds, so they are not one-speed nodes either; only v₊ = −v₋ escapes both, and it needs tuning.
   - **Winding letters: the obstruction is a locality statement (C12; campaign evidence).** O covariance does not constrain the 3D winding W₃ (exact). An explicit analytic, exponentially local, O-covariant letter has W₃ = 1. It is built from a degree-1 map on one spin-½ doublet, with one parameter m and the same topology for all m ∈ (1, 3).
     - On its own, as a step, it reaches E = π only at −k*: a single isotropic Weyl cone of one speed with Berry charge ∓1. So the selection rule is met at that quasi-energy in the node-counting sense. The price is no spectral gap at any quasi-energy: closed surfaces at every other E, and a flat band at E = 0.
     - Conversely, every strictly finite-range unitary has W₃ = 0. This is exact, given the standard algebraic K-theory result SK₁(C[Z³]) = 0 (recalled, not re-derived). It also holds for any step generated by a continuous Hamiltonian. The letter is at operator-norm distance 2 from every finite-range unitary.
     - So for finite-range steps the zero-winding input to the doubling obstruction is exact (net chirality still uses Bessho–Sato), and admitting the quasi-local letter is a genuine change of premise. No step combining it with S passed the screen.
8. **Net reading.** The ladder carries classes, valley positions and multiplicity structure exactly. The only common-cone mechanism with a derivation is constraint closure. It is conditional and leading-order, it ties every matter cone to the graviton's, and (C3) with field-independent structure constants and one generator per momentum it has no exact lattice form with the continuum spectrum. The structure-function examples that evade this do so where closure is automatic (C9's frames at backgrounds the relabellings move) or cheap (C10's 1D model with no local degrees of freedom); for lattice parametrised field theory, which has local degrees of freedom, exact closure is open (C10). No parameter-free step found passes its selection rule. A one-parameter, exponentially local letter with nonzero 3D winding does meet it at one quasi-energy (C12), but no strictly finite-range step can have nonzero winding. Whether steps must be strictly finite range is therefore a premise the owner has to fix.
   - **Open:**
     - the premise decision: are quasi-local (exponentially decaying, not finite-range) step letters admissible? If yes, C12's winding letter evades the doubling obstruction at one quasi-energy, and the next question is whether a parameter-free, finite-depth-generated variant or a closure-compatible step built from it exists. If no, zero winding is exact for every step;
     - exact closure with structure functions that is not automatic (a proper distribution, generators not linear in π, or restricted structure functions), on mixed backgrounds, or realised by periodic lattice relabellings; for lattice parametrised field theory, a finite-range flat Kuchař density beyond first order (C10);
     - a step whose node quasi-energy avoids the non-T-fixed C2-pair points (by the doubling corollary, a step with no quasi-energy gap), or that uses tastes with no k-independent intertwiner;
     - 4-fold levels at ±k*: levels with G3/2 content (unscreened, B23), and generic-letter D₊⊕D₋ levels with v₊ = −v₋ (C11; this needs tuning);
     - a constructed topologically ordered doubler sector;
     - the induced 1/G, from a complete microscopic action, spectral sum rules or a perfect-action principle;
     - shift letters beyond those examined (B26, C8): exp(iθR_L) at other rational angles, non-monomial doubled-cell letters, larger cells, further O-symmetric involutions (by C11 such letters can only rescale an isolated k* doublet's speed, so they matter through the other nodes and the tastes);
     - rung 0 → 1, via emergent corner quasiparticles of a translation-invariant fine Hamiltonian (the C7 Γ-matrix model selects a different phase; other fine Hamiltonians and fillings are untried) or a fractional-translation encoding.

### Detail

The ladder does unify the lanes, but not by deriving everything from the finest rung. It gives three tools that every lane can use: the first two rest on exact statements, and the third is a reading. It also collects what is left open onto a short list of shared primitives.

**What the campaign added (2026-10-18).** A fourth tool appeared, and three of the probe reframings became proved or decisive statements.

- **Fourth tool: the lattice fixes the species content at the top rung.** The gauge-dressed symmetry action forces even levels at the momenta fixed by commuting C2s, and odd filling without pockets then forces touchings at all of them. So the long-wavelength content is not free. In the corner model the forced touchings are one isotropic spin-½ pair at ±k* plus three axis-labelled pairs, whose cones are uniaxial (isotropy not forced). This is a lattice LSM and doubling statement carried up the ladder: the top rung inherits a multiplicity structure, not just a class.
- **Formation.** Rung-0 formation with random priorities (state-independent rates) is provably mixing, with factorially decaying correlations: the trivial fixed point, in RG language. Any long-range structure in Records must therefore come from the Hamiltonian rung, from the start, or from rules outside the class. Spatial Record frequencies then converge; they equal the rule weights only for order-blind rules (a partial, conditional discharge).
- **Gravity.** Every gauge-invariant two-derivative kernel gives the two TT polarisations a single cone, and lattice constraint closure selects DeWitt (supplied clauses, leading order). The induced-gravity item is now precise: the 06-08 bubble needs an underived seagull, so the induced 1/G is not fixed. C2 adds that the seagull which closure fixes is not the one needed, and that closure cannot fix 1/G. With matter, see the closure route below.

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
   - At one-fermion level, masslessness is protected and small masses are technically natural. Interactions can escape the quartet protection (B7).
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

### The common light cone

**The answer the probes converge on.** Three lanes independently hit the same wall: a common light cone.
- Per-field isotropy is free.
- A common speed across fields is not free when each field's speed is a tunable coupling. Neither is spin-2 isotropy with Hamiltonian time and only spatial O_h (the probe's g3). In the repo's curvature member, though, constraint closure forces ε₃ = 0 (B4). In the corner Hamiltonian the speed scales with a supplied term; the Maxwell probe found a coin with two light cones.
- The grid's own speed limit does not help. A local qubit grid does give a hard limit (one site per step for a circuit; a Lieb–Robinson bound for a Hamiltonian). But a limit is a ceiling that fields can sit below at different speeds, not a common speed.

#### Constraint closure (campaign blocks B14–B22)

**Another route to a common cone: closure of the gravity constraint algebra (campaign block B14, independently checked).** This is the Teitelboim / Hojman–Kuchař–Teitelboim mechanism realised on the repo's lattice gravity model.

- In the 2026-09-24 curvature-member model, add a supplied scalar matter sector and require the total constraint algebra to close. At leading order, exactly on the lattice:
  - every matter species is forced onto one common cone, set by the gravity coefficients: c = K/(4α) in block 62's normalisation (K1 = K2 = K, unit relabelling weight). The invariant form is B21's graviton cone K2/(4α);
  - the curvature term is forced to the Lorentzian sign. The 09-24 runner's sign is opposite to its own action and corresponds to the Euclidean algebra.
- In the continuum at leading order, the relabelling bracket then forces the universal metric-stress coupling.
- On the lattice that bracket fails at O(a²), with an explicit obstruction monomial.
- **Supplied:** the matter Hamiltonian, its positivity, the relabelling generators and their normalisation (δ_ξh = 2∂ξ; B19 and B21 say what is later derived), and the scalar-lapse rule. Newton's constant is not fixed.
- **Consequence:** a common light cone does not require a parameter-free step rule or 4D hypercubic symmetry. It can come from requiring the coarse rung's gravity constraints to close with matter. Exact lattice closure beyond leading order is open. A translation-covariant relabelling algebra that closes within its span with field-independent structure constants cannot carry the continuum spectrum (C3, checked). So exact closure needs field-dependent structure functions or more generators, or accepts a non-continuum spectrum. Both evade the lemma (C9, checked): the structure-function examples sit at backgrounds the relabellings move, where closure is automatic, and the enlarged sets are so far abstract algebras (summary item 7).

**The closure route extends across spins and acts as a selection rule (campaign blocks B15–B17).**
- **Spin ½ (B15, independently checked).** A naive lattice Weyl/Dirac field closes against the same constraints only on the scalar's cone, v² = K/(4α). Hermitian Clifford generators square to +1, which gives v² > 0. So, given K, α > 0 and a common relabelling orientation, the Lorentzian sign follows without a positivity premise on the matter. All eight naive doublers share the cone; six of them need momentum-dependent spin structure in the lattice relabelling (B15 check).
- **Exact lattice closure fails.** No linear relabelling of any range closes the fermion bracket. The obstruction is O(a²) at endpoint-mean timing and O(a) otherwise.
- **Spin 1 (B16, independently checked).**
  - A lattice Maxwell field closes on the same cone, independently of g.
  - Among translation-invariant timings supported on link endpoints and plaquette corners, this needs one of eight one-sided timings. Reflection-symmetric alternatives break unit translations and appear to fail elsewhere.
  - The one-sided timing forces an O(a) lattice obstruction.
- **What sets the cone's value, for every species (B19 and B21, independently checked).** The relabelling normalisation is partly derived.
  - In the continuum at leading order, {G, G} and the single lapse rule force the scalar and Maxwell generators onto one structure constant. So those matter cones equal each other with no normalisation premise, given one total constraint and one lapse rule.
  - For spin ½ the h-independent Kosmann relabellings do not close. On the joint metric–spinor phase space, a connection term absorbs the remainder (09-13 native-Weyl note; C4b, checked), and the spinor weight is then forced equal as well.
  - Their value relative to the gravity coefficients additionally needs gravity's own {G, C} at order h, with a quadratic relabelling term. That bracket gives every matter cone = the graviton's TT cone, K₂/(4α). This is K/(4α) because block 62 carries one K on both curvature terms, reading block 101's quadratic Hamiltonian as the unit-lapse value of one lapse-smeared constraint. Further premises: one total constraint and relabelling, a local first-order lapse rule, and a one-derivative quadratic relabelling term.
  - On the lattice the relabellings do not close: the scalar at O(a²), Maxwell at O(a). There the normalisation is selected only in the continuum limit.
  - **Invariant form (B21).** The canonical rescaling (h, P) → (ρh, P/ρ) preserves every bracket while moving K2/K1. So the coordinate-invariant statement is v² = K2/(4α) for every species, where K2 is the coefficient of the TT (second-order √gR) term: the matter cone is the graviton cone. Every "K/(4α)" above is this value in block 62's normalisation.
  - "K/(4α)" with the linear-curvature coefficient holds only once h is normalised as g − δ. Equivalently: unit matter coupling, structure function δ − h, DeWitt metric on δ + h, or block 62's single K. No bracket can force this normalisation unless one of these is fixed. For the walker, its frame identification fixes unit matter coupling by definition (C4), and closure with it then forces K1 = K2 (C4b, checked).
- **Prior art.** In the continuum this is the known Teitelboim / Hojman–Kuchař–Teitelboim / Schwinger universality. What is new is its exact lattice realisation and the explicit obstructions.
- **Selection rule (B17, independently checked).**
  - Closure needs every low-energy species to carry the gravity sector's cone metric. That metric is isotropic when the gravity relabelling is cubic-covariant: {G, G} alone would also allow a constant anisotropic metric, but then all species would have to share it. Lapse rescalings, density improvements, anisotropic relabellings and coordinate changes cannot evade this.
  - The repo's 2026-09-25 walk passes the leading-order cone test. It is naive-type, and the invariance of Σ sin² k_j under k_j → k_j + π makes all eight species isotropic at one speed, so the closure route reproduces its α = K/4 (with the walker as matter, C4b gives α = K2/4 and K1 = K2). It passes only that test: six of its species need momentum-dependent spin structure, and exact closure fails at O(a²) (B17 check).
  - The parameter-free corner step fails. Its ±k* cones are isotropic, but the doublers at the same quasi-energy are uniaxial. They sit at D4 points that no species-exchanging symmetry relates to ±k*: k → k + π(1,1,1) exchanges only orbits of the same type.
  - This is conditional on the step's long-wavelength, band-projected theory coupling to a lapse as a scalar-weighted energy density. A global local Floquet Hamiltonian is not asserted, since the step is gapless away from ±π/2.
  - **Can a step couple to a lapse? (B22, independently checked.)** Two definitions were examined.
    - **The step's own causal timing:** path independence is automatic, but it carries no bracket. An exact defect lemma forces lattice-scale defects at the same order as the bracket; this is intrinsic for the massless 1D walk.
    - **A lapse built from the step's generator, H(N) = ½{N, i log W}:** this reproduces the deformation bracket with each node's own cone metric, spin term included. In particular, uniaxial nodes get direction-weighted shifts.
    - So, of the two definitions examined, the premise can be met only by a choice, Definition B. That choice adds three conditions: the node at quasi-energy 0 (for the corner step, a two-step lapse −W², inferred), node-relative momentum, and a branch cut inside a quasi-energy gap. Without the gap, the smeared step W_N has non-summable 1/r tails for non-integer N, so it is not quasi-local.
    - **For the corner step the gap condition fails.** The step is gapless away from ±π/2 (B17 check). Its band-projected bracket still has the direction-weighted form, so B17's rejection holds at the level of the low-energy bracket. That is an inference: the step's circuit was not run with a lapse.
    - Gate-modulation lapses are an untested third route.
- **Consequence for the target below (given B17's premise).** A parameter-free step can feed a closing gravity sector only if every species at its node quasi-energy is isotropic at one speed. Apart from accidental (non-generic) isotropy, that takes one of two things. The first is a taste-type symmetry relating the D4-point nodes to T-fixed ones. The second is having no such nodes, which by the doubling corollary needs gaplessness in quasi-energy or broken axis C2s.
- **The taste route, in the corner model (B18, independently checked).**
  - The diagonal shift S has no translation-covariant taste moving k* off ±k*. Its allowed affine momentum maps are exactly the PSG lifts times k → k + π(1,1,1).
  - Stabiliser orders, 24 at k* against 8 at k* + πe_i, mean any taste must enlarge the symmetry group.
  - Adding the link hopping's plane tastes leaves no spin-½ doublet at k*.
  - For the eight-node step, an exhaustive spectral test and the velocity-determinant invariant exclude every such map: v*³ = 0.1048 against v_ax v_tr² = 0.0841.
  - Words in S² do have exact tastes, which make their Weyl copies isotropic at √2/3 per S. But they carry uniaxial nodes at the same quasi-energy, at (π/4)-type points, or nodal lines.
  - So no step found so far passes the closure selection rule. Enlarged and spectral taste groups (B24, B25) and new letters (B26, C8), all checked, do not change this; see summary item 7.
- **Wider search and lemmas (B20, independently checked).**
  - Of 69,894 parameter-free (word, node quasi-energy) pairs with up to six letters and an exactly 2-fold (Weyl) level at k*, no tested step reaches its node quasi-energy only at isotropic cones of one speed. Each has an explicit failure witness. Four-fold levels are treated in the last lemma below.
  - Lemmas for this word class (exact unless marked):
    - every spin-½ doublet at ±k* has speed |n_S|·√2/3, where n_S is the net power of the diagonal shift;
    - the 3D winding vanishes for every word (exact). With the Floquet Nielsen–Ninomiya theorem (Bessho–Sato 2021, checked at abstract level only), the net chirality at any point-node quasi-energy is then zero (conditional);
    - isotropy is symmetry-forced only at momenta whose little group contains T (T-fixed points found exhaustively on a (π/8)Z³ grid). The cube doublers and the X- and M-type points have only D4.
    - in this word class, a 4-fold level at ±k* made of both spin-½ doublets is an exact isotropic Dirac point: two cones of one speed and opposite chirality, so the chirality argument does not exclude it, and here the conditional obstruction applies to 2-fold doublets only. Screening all 10,174 such Dirac levels in the searched families found none passing (B20 check; campaign block B23, checked). With generic symmetric letters (C11, summary item 7) the two speeds generically differ, and the levels whose two cones share a chirality fall under the obstruction. Four-fold G3/2 levels are not covered by these lemmas, and levels with spin-3/2 content, mixed with these doublets or pure, are not screened (B23).
  - The observed blocking pattern is a uniaxial doublet pinned at a D4 point. Moving it off the node quasi-energy with continuous phases (a control, not parameter-free) opened Fermi pockets in every tested case; there is no counting proof.
  - This is a negative search over the tested palettes, not a no-go.

### The information-minimal target and its status

**The information-minimal target.** One local step rule on the base grid with no continuous parameters, from which every field is built. Then:
- each speed is a pure number fixed by the grid geometry (item 6);
- composites of collinear constituents inherit it;
- full octahedral symmetry at the node pushes anisotropy to (a/w)².
- **Status after the campaign:** no parameter-free step found so far meets the closure selection rule (B17, B18, B20, B23–B26, C8). Each tested step reaches its node quasi-energy somewhere other than at isotropic cones of one speed: a band crossing, or an anisotropic, tilted, flat or other-speed node. By C11 an isolated doublet at ±k* is always an untilted isotropic cone, so the obstruction lies at the other momenta and in the tastes. C12 shows the obstruction is about strict locality: a quasi-local letter with nonzero winding meets the rule at one quasi-energy, and no finite-range step can.

This replaces a heavier earlier formulation: a reflection-positive transfer step with 4D hypercubic symmetry (item 5). That remains a sufficient alternative, with these conditions:
- the group acts on spinors through its double cover;
- the redundancies are exact;
- the time step equals the spacing;
- the symmetry is not spontaneously broken;
- the doubler trade-off: removing time doublers Wilson-style breaks the w1-odd protection.

It is a target to derive or propose to the owner, not an adopted axiom.

**What item 6 adds.** The corner model supports parameter-free, symmetric, exactly unitary step rules whose speeds are pure numbers fixed by the grid.

- **The reflection step** has a spin-½-class six-fold node at speed exactly 1/√3.
- **The diagonal-shift step** has genuine isotropic spin-½ Weyl nodes at ±k*, speed √2/3. Like naive lattice fermions, they come with doublers: six uniaxial Weyl nodes at the other cube points.
- **The lemma** shows why the shift is needed: an isolated spin-½ doublet cannot move under any symmetric operator algebra generated by constant-spectrum factors.

The doubling corollary settles the question for gapped steps and pocket-free odd-filling Hamiltonians: with the axis C2s, the doublers are forced, as in Nielsen–Ninomiya. The minimal clean form puts them at the other six cube points. The remaining escape routes are steps gapless in quasi-energy, as the eight-node step is (certified in the corollary check; not tested across the searched families), or giving up the axis C2s. Pairing does not remove the doublers selectively either: under full O a single symmetric pair condensate is all-or-nothing at the eight cube points (C1, checked).

**Next tests of common origin.**
- Is a gauge-like field built from the same rule (for example, a bilinear of its cone states) a second field with the same speed?
- Do interactions keep the speeds together?

### What stays open

**The other shared primitives the ladder isolates.**
- **Exact redundancies at the coarse rung.** Gauss is exact. Diffeo is only locus-closed, and the lattice relabellings close only at leading order: O(a²) for the scalar and O(a) for one-sided Maxwell (B14, B16, B19). Exact closure with the continuum spectrum is excluded within field-independent structure constants and one generator per momentum (C3). C9's structure-function evasions sit at backgrounds the relabellings move, where closure is automatic, and for lattice parametrised field theory the naive constraints are anomalous (C10).
- **A low-entropy start.** Needed for preparation, records and any formation order.
- **Values of relevant couplings.** Masses, scales and the cosmological constant are transported by the ladder but never fixed by it.

**What the ladder does not touch.** The Born abundance assumption, permanence, the mass-gap proof, and band-structure questions such as whether the Dirac point is the global minimum.

## Independent check (original note, items 1–5)

A fresh-context agent of the same model family checked the note; it is not an independent human reviewer. It used its own gauge solve, with explicit translation rows, and its own 2O lift, found by search from the C4z and C3[111] generators. Scripts, logs and REPORT.md are in `.claude/science/physics-loops/toe-campaign-20261017/scale_ladder_note_check/`.

- **Item 1: confirmed.**
  - s_R is derived from gauge signs.
  - On finer grids (π/4, π/6, π/12) the same two points are fixed.
- **Item 2: confirmed.**
  - Without any lift, (C2 axis)², (C2 edge)² and (C4)⁴ equal −I on the k* block.
  - Random symmetric Hamiltonians with strengths from 1e-2 to 1e3 give only even levels.
  - Bare (ungauged) permutations, or only the C3 subgroup, give 1-fold levels. So the wording now names the gauge-dressed operators.
- **Item 3: confirmed** at six further parameter points and on two further X seeds. The ratio is 4.0000 ± 0.0003 for q ≤ 0.02.
- **Item 4: confirmed with corrections, now applied.**
  - Multiplicity divisible by 4 replaces "4-fold".
  - The anticommutation mechanism is stated.
  - Splitting is necessary, not sufficient, for a Dirac mass.
  - The inversion-broken control splits inversion partners rather than valleys.
- **Item 5: confirmed, and extended to Dirac and gauge-field forms.** The answer section has been narrowed:
  - the route is sufficient, not necessary;
  - the conditions are listed;
  - the doubler trade-off is noted;
  - the corner model is not such a step;
  - no physical identification.
- **Item 6: checked in parts, by campaign checkers (fresh-context, same family).**
  - B1_check (report recovered from the session transcript) covers the minimal automaton, the reflection step (H_link² = 2, M³ = (|q|²/3)M, the six-fold node) and the constant-spectrum lemma.
  - B17_check and B18_check re-derived the eight-node step's cones, chiralities and second node set.
  - The anticommuting C2 lifts are B7-checked.
  - The doubling corollary was checked independently (`COROLLARY_check`, which also confirmed the D4 axis assignment of the 1 + 3 orbit statement). B1_check's report was recovered from the session transcript and saved.
- **Lane table.** Four rows were corrected against the probe reports.
- **Citations.** All were checked from memory. van den Berg–Steif is the least certain.
