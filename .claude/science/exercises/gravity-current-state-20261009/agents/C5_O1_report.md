# C5 probe O1: what the Lorentz-invariance bounds force on the substrate's spacetime symmetry

**Probe.** O1 of campaign C5, round 1 (`TESTS.md:2329-2334`). Run by Claude Opus 5.5 (same family as the earlier workers), 2026-10-12, 10:57Z to 11:15Z. **Not refereed.** No codex referee has seen this report.
**Readings** (fixed at `TESTS.md:2316-2320`): DERIVED, SUGGESTED, REFUTED. Computations are labelled **checked** (they ran here). Results of the packet's earlier lanes are labelled **refereed** with their referee file.
**Scripts and outputs** (scratch `C5/O1/`):
- `o1_invariants.py/.out`: invariant-tensor counts for the candidate symmetry groups;
- `o1_continuum_counts.py/.out`: the same counts for SO(4) and SO(1,3), computed exactly from the Lie algebra;
- `o1_lorentz_lattice.py/.out`: the integer Lorentz group O(1,3;Z), and Lemma C;
- `o1_bounds.py/.out`: bound kinematics and tuning arithmetic.

No repository file was edited.

---

## 0. In plain words

1. **What the bounds force.** The law's symmetries must leave no spacetime direction special. That is required at the level of anything a particle's speed can couple to. Precisely, the law may have no invariant time-like vector, and no invariant symmetric two-index tensor other than the metric.
   - If it has one, every pair of species gets its own speed difference. Nothing forbids it, and one loop already makes it about 1e-2 (refereed F2).
   - Observation then requires each such number to be cancelled by hand, to about 3 parts in 10¹⁷.
2. **Who fails this test.** The test fails for three kinds of law:
   - every law that evolves in a time of its own on a fixed spatial grid (the axioms as written, with time added downstream);
   - every finite-range law in real (Lorentzian) spacetime that is exactly symmetric in each realization;
   - every law whose finite symmetry group keeps an arrow of time.
3. **Ways out.** Each one costs a change to axiom text.
   - **(II) A Euclidean spacetime grid with equal steps.** The whole law is hypercubic. Real time is recovered by reflection positivity. The arrow of time comes from the state, not from the law.
   - **(III) Lorentz invariance in law only.** Random events: P1 to P4. This route is already excluded at the shared non-locality scale by RZ.
   - **(IV) Exact boosts in every realization.** This needs continuous translations and unbounded energy per particle, i.e. a continuum field per cell (P10).
   - **(VII) Hide the preferred frame behind a separate high scale** (H3 escape). This is the open RF3 route.
4. **The registered expectation is too strong.** It said "only Lorentz-invariant-in-law substrates avoid tuning". That is **REFUTED as stated** for matter at dimension ≤ 4. The Euclidean hypercubic grid avoids the matter tuning by a finite symmetry (refereed F2: Δ(ξ = 1) = 0). For the matter kinetic form, that grid is already the framework's approved `kinetic_isotropy_primitive`.
   - **What is DERIVED instead:** the law needs time–space-mixing symmetry, not Lorentz invariance as such. Among real-time, or Lorentzian finite-range, exactly symmetric laws, none has it.
   - **Where the cost goes on the Euclidean grid:** gravity. It needs an exact lattice gauge identity or 11 tunings (K1). The arrow of time cannot sit in the law.

---

## 1. Observational inputs and how they were verified

Here c_s is the maximal attainable speed of species s, and δ_ss′ = c_s − c_s′.

| Observable | Bound | What it constrains | Source | Verification |
|---|---|---|---|---|
| LHAASO photon at 1.4 PeV survives (no γ → e⁺e⁻) | c_γ − c_e < **2.66449e-19** | e–γ, photon-fast sign (the sign F2's lattice gives) | Cao et al., Nature 594, 33 (2021) | Photon energy confirmed in `C4_F2_referee.md` (refereed). Threshold **checked** here from exact kinematics: d_th = E/√(E² − 4m²) − 1 = 2.66449e-19 (`o1_bounds.out:1`) |
| LHAASO spectra (PRL 128, 051102, 2022) | E_LV,1 > ~1e5 M_Pl; E_LV,2 > ~1e-3 M_Pl (superluminal photon decay) | Dimension-5 and dimension-6 photon terms | arXiv:2106.12350 | Abstract via search (exponents read from the snippet) |
| LHAASO GRB 221009A time of flight | E_QG,1 > 10 E_Pl; E_QG,2 > 6e-8 E_Pl | Linear and quadratic photon dispersion | arXiv:2402.06009 | B1 report "checked by search"; `C4_B1_referee.md` item 7: the citation is correct (refereed) |
| Pierre Auger 212 EeV primary (no vacuum Cherenkov) + HESS 30 TeV photon | **−9e-16 < κ̃_tr < 6e-20** (98% CL) | Photon against charged matter (proton-fast sign: 6e-20) | Klinkhamer–Schreck, PRD 78, 085026 (2008), Eq. 16 | **Fetched** (ar5iv). Addendum arXiv:0806.4351: isotropic one-sided at the 1e-19 level, 8 anisotropic two-sided at 1e-18 (abstract, fetched) |
| LEP 104.5 GeV e± + Tevatron 300 GeV photons | −5.8e-12 ≤ κ̃_tr − (4/3)c_e^00 ≤ 1.2e-11 | e–γ, both signs (laboratory) | Hohensee et al., PRL 102, 170402 (2009) | Search snippet |
| IceCube PeV neutrinos | δ_ν < O(1e-18) (superluminal) | ν–(e,γ) | Borriello et al. 2013 (arXiv:1303.5843) | Search snippet. The 1e-20 figure used in E2 (memory) is **not verified** |
| GW170817 + GRB 170817A | **−3e-15 ≤ (c_T − c)/c ≤ +7e-16** | Graviton against photon | arXiv:1710.05834 | **Fetched** abstract |
| Ne-Rb-K comagnetometer (Hughes–Drever type) | 4 of the 5 spatial c^n_jk at ~**1e-29** | Neutron anisotropy in the lab frame | Smiciklas et al., PRL 107, 171604 (2011) | Search snippet |
| CMB polarization (dimension-3 photon Chern–Simons) | (k_AF) combination < ~6e-43 GeV | Dimension-3, P-odd photon term | Kostelecký–Russell Data Tables (arXiv:0801.0287) | **Partial**: an OCR'd table snippet only |

**Correction to the brief's "≈1e-20 or better per species".** Only some species and signs reach that level.
- At ~1e-19 to 1e-20: e–γ on the photon-fast side, and p–γ on the proton-fast side.
- The opposite signs are 1e-11 (e) and 9e-16 (p).
- Neutrinos: 1e-18 as verified.
- The graviton: 1e-15.
- The 1e-29 neutron bound is on anisotropy in the lab frame. In a preferred-frame theory it reaches the isotropic c_00 only through the lab's velocity β. With the CMB frame as the preferred frame (an assumption), c_00^n ≲ 1e-29/β² ≈ 7e-24 (`o1_bounds.out:8`). That is an order of magnitude only: SME projection factors were not computed. **SUGGESTED.**

---

## 2. Hypotheses (stated once, used below)

- **H1 (effective theory and geometric symmetry).**
  - Below Λ = 1/a, the observed sector is a local, unitary 3+1 effective theory of the Standard Model fields (and a graviton), weakly coupled at the scales the bounds probe.
  - The substrate's exact symmetry group G acts on the IR fields geometrically. A linear "point part" ρ(g) acts on the tangent space T ≅ R⁴ (vectors, tensors, spinor lifts); internal transformations act on top.
  - Translations act trivially on constant tensors.
  - Covariance is either per realization or in law. Which one is stated in each case.
- **H2 (no tuning = natural coefficients).** Every operator allowed by ρ(G) and the effective theory's gauge invariance appears with at least its natural size. "Tuning by f" means the coefficient sits a factor f below natural with no symmetry reason.
  - The natural size of the e–γ dimension-4 speed difference is fixed by refereed instances. Z³ × ℝ non-compact naive/staggered QED gives −8.55e-3. The anisotropic Z⁴ grid at ξ = 2 gives −10.26·α/4π = −5.96e-3 (`C4_F2_referee.md`; arithmetic in `o1_bounds.out:4`).
- **H3 (same-scale violation).** The substrate regulates the matter fields themselves, so the matter loops see any preferred tensor at Λ. This excludes Pospelov–Shang-type sequestering.
- **H4 (no symmetry relating species).** No exact lattice supersymmetry or custodial symmetry sets c_e = c_γ. The F2 referee: super-Poincaré protection is "not established" on the lattice.
- **H5 (symmetries act linearly on displacements).** No nonlinear (DSR-type) action on momenta, and no non-geometric duality.
- **H6 (no strong-coupling rescue).** Between Λ and the bound's energy, the speed difference runs as weakly coupled fields do (E1 and E2, refereed: 8.55e-3 runs only to 7.34e-3 at 1.4 PeV).

---

## 3. Results

### 3.1 Lemma A: invariant-tensor criterion (DERIVED; standard)

Under H1, take a constant-coefficient local operator C^{μ…}·O_{μ…}[fields of species s]. It is G-invariant iff C lies in the ρ(G)-invariant subspace of its tensor representation. Hence, for each species:
- a dimension-4 speed operator c^{(s)}_{μν}T_s^{μν} (traceless part of c) is allowed iff V₂^tl(ρ) ≠ 0;
- the vector terms (a_μ, b_μ, (k_AF)_μ) need V₁(ρ) ≠ 0;
- the Myers–Pospelov dimension-5 terms need V₃ ≠ 0;
- the p⁴ dimension-6 terms need V₄^non-metric ≠ 0.

If u ∈ V₁ is nonzero, then u⊗u ∈ V₂ has a nonzero traceless part. **So V₂^tl = 0 implies V₁ = 0.**

**Counts (checked).** These are invariant-subspace dimensions; S2 includes the metric.

| Group ρ(G) | V | S2 | S3 | S4 | h·h mass forms | q·q·h·h kinetic forms |
|---|---|---|---|---|---|---|
| (a) Z³ × ℝ, proper cubic O only, time fixed (the axioms' group) | **1** | **2** | 2 | 4 | 6 | 30 |
| (b) Z³ × ℝ with O_h × time reversal | 0 | **2** | 0 | 4 | 6 | 26 |
| (c) Z⁴ at ξ = 1, proper hypercubic B4⁺ (order 192) | **0** | **1** | 0 | 2 | 3 | 9 |
| (d) Z⁴ at ξ = 1, full W(B4) (order 384) | 0 | 1 | 0 | 2 | 3 | 9 |
| (e) W(B4) elements that keep a time arrow (order 48) | **1** | **2** | 2 | 4 | 6 | 26 |
| SO(4) and SO(1,3), exact Lie-algebra null space | 0 | 1 | — | — | 2 | 4 |

Sources: `o1_invariants.out`; `o1_continuum_counts.out`.

**Consistency.**
- Rows (d) and SO(4) reproduce K1's refereed counts: 3 mass forms, 9 two-derivative forms and a four-dimensional O(4) subspace (`C4_K1_referee.md` item 1).
- Rows (a) and (d) in the S2 column reproduce the repo's B4 note (one coefficient under B4, two under the cubic group: `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`). That is prior art: count it once.
- Row (a)'s V = 1 confirms the F2 referee's point: proper cubic O allows b₀ and (k_AF)₀, which only the chosen action's parity forbids.

### 3.2 Lemma B: a real-time law has a preferred frame (DERIVED)

Suppose the law is a real-time evolution: a Hamiltonian H, or a one-step unitary or transfer U. Suppose also that every symmetry of the law commutes with that evolution, possibly up to an antiunitary U → U⁻¹. Then ρ(g)u = ±u for the time-translation direction u. So u⊗u ∈ V₂, with a nonzero traceless part.

**Proof.** U_g H U_g⁻¹ = H means g preserves the generator of time translations. In the IR, that generator is P_u. □

**Consequence.** Every Z³-site law whose time is a parameter of its evolution is in class I. That includes the four axioms as written plus any downstream real-time law that keeps Admissibility's covariance.

The refereed boost theorems say this cannot be avoided by adding boosts to such a law:
- C3: closure needs a constant Hessian, so only Carroll survives (`RC_C3_referee.md`);
- RB: no closure on bounded sectors, and no global action on the Brillouin torus (`C4_B1_referee.md`);
- I1: a complete tower is needed;
- RFW: field-dependent completions do not help (`RFW_F2_referee.md`).

### 3.3 Lemma C: finite point groups in Lorentzian signature (DERIVED; new here, elementary)

**Statement.** For every finite (more generally, compact) subgroup F ⊂ O(1,3), V₂^tl(F) ≠ 0.

**Proof.** Pick any time-like u and set S^{μν} = Σ_{g∈F} (gu)^μ (gu)^ν.
- S is F-invariant.
- As a quadratic form on covectors, S(w,w) = Σ_g (w·gu)² ≥ 0, and S ≠ 0.
- η^{μν} is indefinite, so S ≠ λη for every λ.
- The traceless part of S is therefore nonzero. □

Checked numerically on a boosted copy of O_h × Z₂: the eigenvalues of S are all positive and ‖S − λη‖ = 3.61 (`o1_lorentz_lattice.out`).

**Corollary C′ (summable laws have finite point groups; DERIVED).** Let N be the support of the law's translation-covariant couplings K(x), with x a displacement. Suppose N spans T and Σ_x‖K(x)‖ < ∞. Then ρ(G) is finite.
- **Proof.** Symmetry with a unitary internal action gives ‖K(ρ(g)x)‖ = ‖K(x)‖, so each x ∈ N has a finite orbit; otherwise the sum diverges. Take a finite spanning subset of N; the union of its orbits is a finite spanning set N′. ρ(G) permutes N′ and is determined by that permutation, so it is finite. □

**Together:**
- A Lorentzian-signature law that is exactly symmetric in each realization, with summable couplings that span, has an invariant speed tensor S ≠ λη.
- An infinite boost group needs couplings that are not summable: equal weights along infinite orbits.
- **Checked example.** O(1,3;Z) is generated by the signed spatial permutations and the reflection in r = (1,1,1,1).
  - Its only invariant symmetric tensor is η. It has no invariant vector.
  - Its orbit of e₀ grows 9 → 53 → 277 → 1401 at word lengths 2, 4, 6 and 8, reaching points such as (7, 4, 4, −4) on the unit hyperboloid (`o1_lorentz_lattice.out`).
  - A law on Z^{1,3} with that symmetry would be Lorentz-clean at every rank, but it would need unbounded valency. This is a lattice analogue of BHS (refereed: no Lorentz-equivariant finite-valency map on a sprinkling, `B_referee.md:52`).

### 3.4 Lemma D: exact connected boosts cannot normalize a lattice translation group (DERIVED; new here, elementary)

**Statement.** Let a connected group L act on the substrate by symmetries that normalize its translation group T = Z^d, i.e. g T_a g⁻¹ ∈ T. Then L commutes with every T_a.

**Proof.** Conjugation gives a homomorphism L → Aut(Z^d) = GL(d,Z). The target is discrete. Assume the action U_g is strongly continuous. Distinct lattice translations sit a fixed strong distance apart (take a state localized away from both images), so g ↦ U_g T_a U_g⁻¹ is locally constant. L is connected, so the image is trivial. □

**Consequence.**
- Boosts, and even continuous rotations, would then leave every quasi-momentum eigenspace invariant. So they cannot act on the IR momentum as p → p cosh η + E sinh η, unless the IR momentum is not the lattice quasi-momentum.
- **Exact per-realization Lorentz symmetry therefore needs a non-discrete translation group.** With RB's Theorem U (refereed: no undeformed positive-β closure on bounded exponentiating sectors), it also needs unbounded one-particle energy, i.e. a continuum fibre (I1's complete tower, P10).
- This needs no smoothness, Morse, positivity or band hypotheses. It is the Lorentz analogue of Lemma R's "only GL(3,Z) points are reachable" (`T2-REF:21`, refereed).
- **Not covered:** nonlinear (DSR) actions that do not normalize T, and symmetries in law (H5 and H1).

### 3.5 Lemma E: an arrow in a finite-group law gives a preferred frame (DERIVED)

**Statement.** Suppose the law's point group ρ(G) is finite and preserves a time orientation, for example an open cone or half-space of "future" directions. Then V₁ ≠ 0, so V₂^tl ≠ 0.

**Proof.** Average any future-pointing vector over the finite group. The cone is convex and invariant, so the average is nonzero and invariant. □

**Checked.** Count (e): W(B4) restricted to arrow-preserving elements has V = 1 and S2 = 2.

**The contrast with the continuum.** The orthochronous Lorentz group keeps an arrow and still fixes no vector, because it is non-compact. So an arrow in the law is compatible with exact Lorentz symmetry (classes III and IV), but **not** with protection by a finite group (class II).

### 3.6 Theorem O1-N: the necessity statement

**Statement.** Assume H1–H6 and the bounds B of §1. Then compatibility of the substrate with B without tuning requires
> **V₂^tl(ρ(G)) = 0, and hence V₁(ρ(G)) = 0.**

That is, the law's symmetry group leaves invariant no time-like (or any) vector, and no symmetric two-index tensor other than the metric.

**If it fails:**
- **e–γ.** The speed difference must be tuned by f ≤ 2.66e-19/8.55e-3 = **3.1e-17**. Refereed: F2's "about 3e-17"; untuned miss 3.2e16 (`o1_bounds.out:3`).
- **p–γ.** f ≤ 6e-20/(6–8.55)e-3 ≈ **(0.7–1)e-17**, one-sided (my arithmetic, `o1_bounds.out:5-6`).
- **Running cannot replace the tuning.** Running reaches only 7.34e-3 at 1.4 PeV (E2, refereed). A power law would need z ≥ 1.276 over 12.94 decades (reproduced, `o1_bounds.out:11`; E2's refereed 1.27564).
- **The graviton.** c_T needs f ≲ 7e-14 to 3e-13 of a ~1e-2 natural size.
  - That natural size is E2's estimate. The E2 referee calls it a "conditional estimate", so this line is **SUGGESTED**.
  - The E1 referee confirms that graviton–matter speed matching is an independent cost.
- **How many tunings.** At least one is refereed (F2). The bookkeeping count is 8 relative matter speeds plus the graviton. The F2 referee accepted that count but not "six independently bounded below 1e-15".

**Label: DERIVED** under H1–H6. Each premise is explicit; H2 is the definition of "no tuning"; the bound is given.

**Corollaries** (Lemmas B to E). V₂^tl = 0 is **impossible** for:
- (i) a real-time law whose symmetries commute with its evolution;
- (ii) a Lorentzian law, exactly symmetric in each realization, with summable spanning couplings;
- (iii) a finite point group that keeps a time arrow;
- (iv) exact connected boosts on a lattice translation group.

It is **possible** only for:
- (α) a law in Euclidean signature with a finite point group whose V₂^tl = 0 (B4⁺ suffices; counts c and d), with real time reconstructed by reflection positivity and the arrow not in the law;
- (β) symmetry in law only: a Lorentz-invariant random point process;
- (γ) exact continuous Lorentz symmetry in each realization, with continuous translations and unbounded one-particle energy;
- (δ) couplings that are not summable (an infinite discrete boost group, e.g. O(1,3;Z) on Z^{1,3}).

**Corollary on gravity (DERIVED for the count, SUGGESTED for c_T itself).**
- In (α), W(B4) leaves 9 two-derivative graviton forms, against 4 for O(4) and 1 that is gauge-invariant (checked counts; K1 refereed).
- So GW170817 without tuning needs the 5 non-O(4) forms to vanish. An exact lattice linearized-diffeomorphism identity does that (K7a: 1 of 9).
- Without that identity, K1's 11 gauge-restoring tunings apply.
- K1's TT restriction (rank 5) is "not a physical two-helicity floor" (refereed). So the number of physical c_T directions is not fixed here.
- The tested exact identities fail: K2 at O(κ²) (bounded) and RFW (bounded FAIL).

---

## 4. Classification of substrate classes and their refereed costs

| Class | How one cone arises | Example | Symmetry counts (V, S2) | Refereed costs | Status for B without tuning |
|---|---|---|---|---|---|
| **I. Preferred frame + tuning** | It does not: an invariant u exists, and counterterms cancel each split | The axioms as written (Z³, proper O, time downstream); preferred foliation (RF); Z³ × ℝ | (1, 2) | e–γ counterterm ~3e-17 (F2). Running misses by 2.76e16 (E2). Strong dynamics fixes neither the graviton speed nor the TT response (E1). P0's two TT tunings plus the free E_g term (V3, RP, RV4). Z³ × ℝ total ≥ 6 (a reading). The lattice cannot add boosts (C3, RB, I1, M1, RFW). P-odd dimension-3 b₀ and (k_AF)₀ are allowed by the axioms' proper-only rotations (F2 referee) | **Fails** (Theorem O1-N), unless P0-type tuning is paid per species |
| **II. Discrete time–space symmetry, Euclidean** | Accidental: B4⁺ allows no dimension ≤ 4 Lorentz-violating tensor; real time by reflection positivity | Z⁴ at ξ = 1 for the whole law. The approved `kinetic_isotropy_primitive` gives this for the matter kinetic form only | (0, 1) | Matter split exactly zero at ξ = 1 (F2; T1 controls). Dimension 6 harmless: (E/E_Pl)² passes LHAASO's E_QG,2 bound by ~7 decades in scale (`o1_bounds.out:10`). Graviton: N_tune = 11 without an exact gauge identity (K1); κ² Killing failure (K2); the field-dependent fix fails (RFW). Coupled reflection positivity unproved (K2). The hypercubic tick makes A25's leapfrog unstable (a real-time artefact; K2: the Euclidean transfer is fine). 4 tastes (K7a) | **Passes the matter bounds** if the whole law is B4⁺-covariant and the arrow is not law-level. Gravity is open or obstructed |
| **III. Lorentz invariance in law (random)** | Exact in distribution; no symmetry in any one realization | Poisson events (E1, E1′) | Lorentz in law | P1–P4. Valency ~5e122 (BHS). Lemma Q. **Noise: RL4 bounded FAIL; RZ FAIL at the controlled level for observed lensed light at the shared ℓ_k** (`TESTS.md:2125-2160`) | Passes B in the mean. **Excluded by noise** within RZ's scope; open: edgeless sources, a coherent substrate (C5 Q1) |
| **IV. Exact Lorentz in each realization on a continuum fibre** | Exact symmetry of continuous translations plus boosts | I1's complete tower; a continuum field per cell | Lorentz | Lemma D: needs continuous translations. Theorem U (RB): needs unbounded one-particle energy. I1: "an infinite-dimensional, unbounded one-particle fibre" (P10). Untested as a full substrate | Passes B by construction; the price is Qubit and Lattice (§5) |
| **V. Emergent by RG flow, no protection** | Relative speeds flow towards zero | Strongly coupled matter | as I | E1 and E2 bounded FAILs: log running too slow; a power law needs z ≥ 1.28 / 1.37 / 2.51; the graviton is not attracted | **Fails** for weakly coupled SM fields (a sub-case of I) |
| **VI. Deformed (DSR) symmetry** | Nonlinear action on momenta (violates H5) | Quantum walks (Bisio–D'Ariano–Perinotti) | Linearized: Lorentz | RB: no global smooth undeformed action on the torus; patchwise or singular DSR open. Lemma R blocks additive-momentum interacting laws (T2-REF). Linear deformation must sit below 0.1/E_Pl (LHAASO GRB) | **Open** |
| **VII. Sequestered preferred frame** | Violation confined to a sector coupled only irrelevantly (violates H3) | Pospelov–Shang; RF3 | as I, at a separate scale | F3: hierarchies of a few 1e9 in scale and 1e38–1e39 in a coefficient, "not automatically precision tunings"; INCONCLUSIVE | **Open** (hierarchy, not tuning) |

---

## 5. Translation into the axioms (named prices; none is adopted)

Read literally, the axioms plus any downstream real-time law are **class I** (Lemma B; count a). The axiom group has V = 1 because only proper rotations are named. Theorem O1-N then leaves four exits, each touching named axiom text. Both time and its metric are downstream content (`MINIMAL_AXIOMS_2026-06-29.md:185`).

**Price O1.1 (class II): hypercubic covariance of the whole law in spacetime.**
- **Lattice** (`:37-38`): "Physical sites are the points of the cubic lattice `Z^3` … proper cubic rotations about each site." The sites would become the points of Z⁴ with one step in every direction, and the rotations the proper hypercubic group B4⁺. Reflections are not needed: count c equals count d for V, S2 and S3.
- **Admissibility** (`:57-58`): "covariant under lattice translations and proper cubic rotations". This would read Z⁴ translations and B4⁺. Add reflection positivity of the specification, so that real time exists.
  - **Reading (SUGGESTED).** Admissibility's form — a per-site distribution "determined by … the nearest-neighbor conditions" — is a Gibbs specification. On Z⁴ that is a Euclidean lattice field theory. It fits class II naturally.
  - **The cost.** With fermions, the Euclidean weight is not a probability distribution in general. For chiral content, the determinant is complex (lattice lore, not computed here).
- **The `kinetic_isotropy_primitive`** (registry, approved 2026-06-09) is **too narrow as registered.** It supplies c_t = c_s for the matter kinetic form on the Z³ × Z_τ regulator block. Theorem O1-N needs B4⁺ covariance for every operator: interactions, gauge fields, the graviton, records. Under H2, any non-covariant piece regenerates u at loop level.
- **Record** (`:77-80`): "Records form. … records are permanent."
  - By Lemma E, if the arrow carried by formation and permanence is law-level, a finite group cannot protect: V₁ ≠ 0.
  - So in class II, the arrow must come from the state or a boundary condition, and records become spacetime events (as P4).
  - **SUGGESTED, not DERIVED:** that the arrow's operator content is generated at natural size depends on how strongly records couple at the cutoff. The axioms leave formation rate and site downstream.
- **Gravity.** An exact lattice linearized-diffeomorphism identity, or K1's 11 tunings. The tested candidates fail: K2 (bounded) and RFW (bounded FAIL).

**Price O1.2 (class III):** P1 + P2 + P3 + P4, unchanged (`PRICE_NOTE.md:163-166`). The noise is currently excluded at the shared ℓ_k (RZ).

**Price O1.3 (class IV): continuous translations and an unbounded fibre.**
- **Lattice:** "standard translations" of Z³ would become an exact continuous translation group, by Lemma D. The cubic lattice survives only as a labelling or a subgroup, not as the symmetry group.
- **Qubit** (`:47`): "The full one-site possibility domain has algebraic presentation `M_2(C)`". Theorem U and I1 need an unbounded one-particle fibre (P10), so the discreteness has to move off the translation group. That is O2's brief.

**Price O1.4 (class I kept, P0 extended): tuning and parity.**
- One relative-speed counterterm per independent species direction. At least one is refereed at about 3e-17. The bookkeeping total is 8 matter plus 1 graviton.
- **Plus the dimension-3 terms (SUGGESTED).** The axioms name only proper rotations, so b₀ and (k_AF)₀ are allowed (refereed F2 point). Removing them needs a law-level improper rotation (parity), or CPT.
  - The Standard Model's weak sector is chiral, so parity cannot be exact in a law carrying it.
  - CPT reverses time, so a law-level record arrow breaks it.
  - Then u-dependent dimension-3 terms are left unforbidden for chiral species. Their natural size is ~Λ (times loop factors), against CMB (k_AF) ≲ 6e-43 GeV (partially verified).
  - This chain is argued, not computed: the natural size of the record-sector contribution is unknown.

---

## 6. Against the registered readings and expectation

The expectation (`TESTS.md:2334`) was "DERIVED, either Lorentz invariance in law or tuning at about 1e-20 per species. Only Lorentz-invariant-in-law substrates avoid tuning."

| Claim | Reading | Basis |
|---|---|---|
| The disjunction, corrected: "time–space-mixing symmetry in law (V₂^tl = 0), or tuning" with f ≤ 3.1e-17 (e–γ) and ≈ 1e-17 (p–γ, one-sided); absolute bounds 2.7e-19 and 6e-20 | **DERIVED** under H1–H6 | Lemma A, counts, refereed F2/E2 numbers, verified bounds |
| "Only Lorentz-invariant-in-law substrates avoid tuning" (matter, dimension ≤ 4) | **REFUTED as stated** | Counterexample: the Euclidean B4⁺ / W(B4) law at ξ = 1. Refereed F2: Δ(1) = 0 exactly by symmetry; checked counts (c, d): V = 0, S2 = 1 |
| Restricted form: "among real-time, or Lorentzian, exactly-per-realization, summable laws, none avoids tuning; the escapes are Lorentz-in-law randomness, continuous translations with an unbounded fibre, non-summable couplings, or a Euclidean finite group without a law-level arrow" | **DERIVED** | Lemmas B, C, C′, D and E |
| Gravity: Euclidean class II needs an exact lattice gauge identity, or K1's tunings, to meet GW170817 | **DERIVED** for the form count; **SUGGESTED** for the number of physical c_T tunings | Checked counts 9/4/1; K1 refereed; K1 referee's caveat on rank 5 |
| "About 1e-20 per species" | **REFUTED as a uniform statement** | Verified bounds are 1e-19 to 1e-20 only for e–γ (photon-fast) and p–γ (proton-fast). Others: 1e-11 to 1e-16 (opposite signs), 1e-18 (ν), 1e-15 (graviton). Neutron anisotropy 1e-29 reaches c_00 only through β (≈ 7e-24 if the frame is the CMB's; SUGGESTED) |
| The P-odd dimension-3 cost of keeping class I with chiral matter and a law-level arrow | **SUGGESTED** | §5, price O1.4 |

---

## 7. What would change these verdicts (open items)

- **H3 (sequestering).** A separate gravitational or Lorentz-violating UV scale with matter shielded (RF3; Pospelov–Shang) turns tuning into hierarchy. It is INCONCLUSIVE in the packet (`C4_F3_referee.md`).
- **H5 (DSR).** Patchwise or singular deformed actions (RB open) evade Lemma D and Lemma A's linear setting. They need non-additive momentum composition, which Lemma R blocks for ordinary local laws.
- **Class II's gravity.** Does any finite-field, B4⁺-covariant lattice law have an exact linearized gauge identity beyond O(κ)? K2 and RFW leave open altered leading generators, auxiliary or multiband fields, and quasi-local towers.
- **The arrow.** Can the arrow sit in the state rather than in the law, compatibly with "records are permanent"? This connects to O4.
- **Reflection positivity and fermions** for a Z⁴ Gibbs reading of Admissibility (K2: coupled reflection positivity unproved). Also the Nielsen–Ninomiya constraint for chiral matter (beyond this probe; cf. P6).
- **Bounds not verified here:** IceCube 1e-20 for ν; clock-comparison c_TJ boost bounds; the electron b torsion-pendulum bound; exact SME projections for the β² conversion.
- **Referee requests.** Lemma C, Corollary C′, Lemma D and Lemma E are short proofs with no codex check yet. Check H2 as a definition. Check the REFUTED line against F2's scope: the referee's Δ(1) = 0 is "provided the action, masses, and regulator respect W(B4)".

---

## 8. Files and provenance

- **Packet sources read in full:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`;
  - `TESTS.md:2302-2371`;
  - `SUMMARY.md` §§15–20;
  - `PRICE_NOTE.md` (v5 and the v6 delta);
  - the referees `RC_C3`, `C4_B1`, `C4_K1`, `C4_K2`, `RFW_F1`, `RFW_F2`, `C4_F2`, `C4_E1` and `C4_E2`.
- **Prior art checked:**
  - `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`;
  - `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md` (same S2 count: count it once);
  - `docs/LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md` (a Collins-type comparator on the anisotropic surface).
- **New here (same family, unrefereed):**
  - Lemma C and Corollary C′ (Lorentzian finite groups; summability);
  - Lemma D (Aut(Z^d) for boosts);
  - Lemma E (the arrow);
  - the multi-rank invariant counts, including the arrow and continuum rows;
  - the price translations O1.1–O1.4.
- **External sources (untrusted downloads, not executed):**
  - [GW170817 (arXiv:1710.05834)](https://arxiv.org/abs/1710.05834);
  - [Klinkhamer–Schreck (arXiv:0809.3217)](https://ar5iv.labs.arxiv.org/html/0809.3217);
  - [Klinkhamer–Risse addendum (arXiv:0806.4351)](https://arxiv.org/abs/0806.4351);
  - [LHAASO LIV PRL (arXiv:2106.12350)](https://arxiv.org/abs/2106.12350v1);
  - [Hohensee et al. (arXiv:0904.2031)](https://arxiv.org/pdf/0904.2031);
  - [Smiciklas et al. (arXiv:1106.0738)](https://ar5iv.labs.arxiv.org/html/1106.0738);
  - [Borriello et al. (arXiv:1303.5843)](https://ar5iv.labs.arxiv.org/html/1303.5843);
  - [Kostelecký–Russell Data Tables (arXiv:0801.0287)](https://arxiv.org/pdf/0801.0287).
