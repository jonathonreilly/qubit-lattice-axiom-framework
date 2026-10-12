# C5 Round 1, probe O2: universality → translation and stress structure

**Probe.** Claude Opus 5.5 (same family as the workers). Started 10:57Z, report 11:16Z, 2026-10-12. Nothing in the repo was edited. Scratch: `.../scratchpad/C5/O2/` (two scripts plus their outputs).

**Readings** (fixed, `TESTS.md` "Campaign C5"):
- **DERIVED:** proved from the stated observations and hypotheses, with the bound given.
- **SUGGESTED:** argued, not proved.
- **REFUTED:** a counterexample exists.

**Evidence labels:** proved / checked / suggested / reading.
- "Own" means proved here by the same model family. No codex referee has seen any of it.
- The no-go items in §6 need the codex referee before they are recorded.
- Observational figures are **from memory** and should be checked before landing.

## 0. In plain words

1. **The equivalence principle (MICROSCOPE) does not see the grid directly.**
   - At tree level, a Planck-spacing grid breaks momentum conservation in real collisions by about (p·a)².
   - That is 1e-41 for nucleons and 1e-34 at the LHC. Every test is blind to it.
   - What forces exactness is three other channels:
     - the vacuum (the graviton mass);
     - loop corrections, which feed the grid into each particle's own light speed;
     - the boost algebra (C3).
   - In each channel the choice is the same: an exact symmetry, or a tuning of stated size.
2. **New, exact (own): a body on a Hamiltonian grid falls at the rate β∇Φ.** Here β is the curvature of E²/2 at the bottom of its band.
   - So MICROSCOPE measures **one common β for all species and composites**. That is the k = 0 half of C3's closure condition, and the gravity-side twin of O1's "one light cone".
   - Per channel this means |δβ/β| ≲ 1e-13 to 2e-10.
   - An untuned lattice-QED split of F2's size would violate the equivalence principle at about 3e-5, roughly 5e9 times the MICROSCOPE bound.
3. **A massless spin-2 with only its two physical polarizations needs a charge that adds up exactly in every collision** (the Ward charge).
   - On an interacting grid in d ≥ 2 no regular local vector charge does this (Spohn; RS/RN/RG, all refereed).
   - "Exact continuous translations on asymptotic states" follows, in the S-matrix sense.
   - Nothing forces those translations to move the substrate's own sites. With exact boosts (O1) they need an unbounded momentum spectrum, which is I1's tower.
4. **Discreteness cannot sit in "finitely many states per cell" if translations are exact and geometric.** Three results (one-particle, many-body qubits, relativistic nets) close that door.
   - What is left: discreteness only in law (events, which hit RZ), in sparse records (count), in finite state counts at finite energy (which every continuum theory already has), or in deformed translations (Snyder/DSR, which gives up exactness).
5. **The minimal price.**
   - Lattice becomes a continuum base.
   - Qubit becomes a per-point fibre (infinite-dimensional local algebras).
   - Admissibility becomes a local rule covariant under the continuous group.
   - Discreteness survives only in Record.
   - The grid then regulates nothing, and the UV problem returns.

## 1. Observations used (figures from memory)

| Observation | Value | What it bounds |
|---|---|---|
| MICROSCOPE (Ti vs Pt) | η = (−1.5 ± 2.3 stat ± 1.5 syst)×1e-15; I use \|η\| ≤ 7e-15 (about 2σ) | universality of free fall |
| Eöt-Wash; LLR | η(Be,Ti) ≈ (0.3 ± 1.8)×1e-13; Earth–Moon Δ(m_G/m_I) ~ 1e-13; Nordtvedt η_N ≲ few×1e-4 | WEP; self-gravity (SEP) |
| GW170817 | −3e-15 ≤ (c_g − c)/c ≤ 7e-16 | graviton TT kinetic term against light |
| LIGO dispersion (GWTC-3) | m_g ≤ 1.27e-23 eV | Π_TT(0) ≤ μ = 2.39e8 eV⁴ (refereed P0 arithmetic, `B_referee.md:26-35`) |
| Cassini | γ − 1 = (2.1 ± 2.3)×1e-5 | scalar or vector admixture in the coupling |
| Weinberg soft theorem (1964) | theorem, not data | universal coupling to conserved P^μ, under W1–W5 (§2.1) |

## 2. Part (1): what universality requires

### 2.1 Theorem 1 (Weinberg, restated). DERIVED (standard; comparator)

**Hypotheses.**
- **W1.** A Poincaré-invariant S-matrix on asymptotic Fock states with continuous 4-momenta.
- **W2.** A massless helicity-2 particle. Lorentz covariance makes its polarizations shift by ε^{μν} → ε^{μν} + q^μξ^ν + ξ^μq^ν with ξ·q = 0, and such pure-gauge polarizations must decouple.
- **W3.** Soft emission is dominated by external-line poles: internal insertions are O(q⁰). This is locality/analyticity.
- **W4.** Constant soft couplings κ_i.
- **W5.** Generic kinematics: the hard amplitudes are nonzero on an open set.

**Conclusion.**
- The gauge variation of the soft factor is 2ξ·V, with V = Σ_i η_i κ_i p_i.
- Decoupling for every ξ ⊥ q, and for every null q, forces V = 0.
- Momentum conservation plus W5 then forces κ_i = κ: universal coupling to the conserved 4-momentum.

**Corollary (Weinberg–Witten, standard).** If the theory has a Lorentz-covariant conserved T_μν, the massless helicity-2 particle cannot be a composite whose stress is carried by that T.
- So O2's necessary T plus WW means the graviton must carry its own gauge redundancy (elementary, or an emergent gauge field that is not a covariant operator, as in Gu–Wen), or Lorentz invariance or locality must fail.

### 2.2 Lemma W: the Ward charge must add up (lattice relaxation). DERIVED (own; elementary)

**Hypotheses.**
- Drop W1.
- Keep:
  - continuous time with exactly conserved energy;
  - lattice crystal momentum, conserved mod G;
  - W2's decoupling, now as an observational requirement (no extra polarizations: Cassini, and the m_g bound);
  - W3: the lattice pole is 1/(E(k+q) − E(k) − ω_q);
  - continuity of the one-particle vertex V^{μν}(k, k′).

**Claim.**
- The soft gauge variation is ξ_ν Σ_i η_i Q^ν(k_i)·M₀.
- Q^ν is the Ward charge of the vertex: on shell, q_μV^{μν}(k, k+q) = [ΔD⁻¹]·Q^ν(k) + O(q).
- Decoupling therefore needs Σ η_i Q^ν(k_i) = 0 on the support of every amplitude. That is, Q^ν must be an **additive collision invariant**.

**Consequences on the lattice.**
- **Time component.** Q⁰ is energy, which is exactly conserved. So Weinberg's argument still gives universal κ for the static coupling (B1's note, `B1_report.md:157`).
- **Spatial components.**
  - For d ≥ 2, interacting lattice matter with a regular open set of umklapp collisions has no continuous vector collision invariant with nonzero slope (Spohn).
  - Refereed instances:
    - RS S1/S2: bounded FAIL, momentum only;
    - RN-L2 strongest statement: no odd periodic C¹ scalar invariant;
    - RG G1: an additive diagonal charge forces the amplitudes to vanish on umklapp sets.
- **Hence** exact decoupling in all processes, plus a regular local vertex, plus d ≥ 2 interacting grid matter, gives a **contradiction**. The exits are exactly the refereed ones:
  - umklapp amplitudes vanish identically (no finite analytic network does this: C1, G1);
  - a discontinuous charge, i.e. SLAC-type non-local hopping (P14);
  - a complete tower (P10).

### 2.3 Check 1: the tree-level size. REFUTED (checked): "observed EP/soft precision forces exact translation at tree level"

`o2_soft_ward_defect.py` uses nearest-neighbour KG on Z³, where the Ward charge per particle is ∇(E²/2) = sin k, equal to the lattice momentum.
- **Defect.** On exactly on-shell 2→2 collisions without umklapp, D/κ ∝ κ^p with p = 2.004 (m = 1) and 1.975 (m = 0).
- **Translated to physical momenta**, with a⁻¹ = 1.22e19 GeV:

| Momentum | Relative defect D/κ |
|---|---|
| 10 keV (atomic) | ~3.5e-50 |
| 0.25 GeV (nucleon Fermi) | 2.2e-41 |
| 1 TeV | 3.5e-34 |
| 1e11 GeV (UHECR) | 3.5e-18 |

- **Umklapp collisions** have an O(1) defect: 2π for the linear charge, 1.23 for sin k in the sample.
- **Counterexample.** For asymptotic low-energy states, the soft theorem and the EP tests are passed by a Planck-spacing grid at tree level.
- **So** the necessity at observed precision must come through loops, the vacuum or the boost algebra (§2.4–2.5). This agrees with B1's note that the lattice defect enters m_g and c_g, not the Newtonian EP.

### 2.4 Lemma F: the fall law. DERIVED (own; exact semiclassically; checked)

**Setting.** A Hamiltonian lattice whose static gravity enters as H → Σ_x (1 + Φ(x)) h(x), i.e. h₀₀ coupled to the conserved energy density.

**Claim.** A wavepacket of any band E_B (elementary or composite) obeys k̇ = −∇Φ·E_B and ẋ = (1 + Φ)∇_k E_B. At k → 0 this gives

  **ẍ = −E_B(0)·Hess E_B(0)·∇Φ = −β_B ∇Φ**, with β_B = Hess(E_B²/2)|_{k=0}.

The rest energy cancels. **Universality of free fall holds if and only if β_A = β_B**, and η_AB = (β_A − β_B)/β.

**Check** (`o2_ep_beta.py`). Leapfrog fall on lattice bands gives a/g = 1.000000 and 1.020000 for β = 1 and 1.02, independent of E₀ = 1 or 5.

**Meaning (reading).**
- C3/I1/M1 need Hess(E²/2) = βI with a common β across the whole band.
- The EP tests that condition at k = 0, across species and composites.
- On the grid this is O1's one-cone condition seen through gravity: Schiff's conjecture, realized.

**Channel bounds** (SUGGESTED: assumes the inertia of energy adds by sector, β_B⁻¹ = Σ_s f_s/β_s; pure Ti and Pt; semi-empirical a_C = 0.711 MeV):

| Channel | Δf (Pt − Ti) | \|δβ/β\| ≤ |
|---|---|---|
| nuclear Coulomb (photon against matter) | +2.03e-3 | 3.4e-12 |
| strong binding | +1.18e-3 | 5.9e-12 |
| electron rest energy | −3.2e-5 | 2.2e-10 |
| neutron against proton | +5.8e-2 | 1.2e-13 |

- **F2's size.** F2's refereed one-loop split c_e − c_γ = −8.55e-3 on Z³ × ℝ gives δβ/β = 1.7e-2 for photon against matter.
- That predicts η ≈ 3.5e-5, about 5e9 above the bound. (Using the electron–photon number as the scale for the photon–nucleon split is a reading.)
- This is independent of, and weaker than, O1's 1e-20 bounds. But it is a **gravity** observation demanding the same thing.

### 2.5 The vacuum and the graviton speed: exact or tuned (refereed numbers; reading for the counts)

- **m_g.** Π_TT(0) ≤ 2.39e8 eV⁴. That is 5.7e-99 of the natural lattice value (B1 c1, CWC). This needs the full off-shell Ward identity q_μ⟨T^{μν}T^{ρσ}⟩ = contact, over all virtual momenta up to the cutoff, where Planck-scale modes are not suppressed. Free local matter already violates it in E_g (V3, CWC; RV4 FAIL bounded). The only structural cancellations found are a symmetry (exact relabelling: RV4 S1 Theorem D, conditional) or exactly matched spectra (RP).
- **c_g.** (c_g − c)/c ≤ 1e-15 needs the graviton's TT kinetic coefficient to share matter's cone. With no shared exact Lorentz symmetry, that costs R2's graviton-speed codimensions (reading; lane R INCONCLUSIVE).
- **DERIVED form of the necessity.** The pair is "exact Ward identity (symmetry or exact structural cancellation) **or** tuning", at:
  - 5.7e-99 (shear masses);
  - about 1e-15 (graviton speed);
  - about 1e-12 to 1e-13 per matter channel (β, §2.4).
- That exactness *requires* a continuous translation symmetry, rather than some other structure, is **SUGGESTED** (naturalness). It is consistent with `B_referee.md:156-163`.

### 2.6 The stated weaker alternatives

| Alternative | Status | Why |
|---|---|---|
| T **local** | **REFUTED as necessary** | The SLAC stress satisfies the linear first-class identities and is power-law non-local (`RG_G3_referee.md`, strongest statement). Locality is not in W1–W5. On the grid SLAC fails boosts (C3 face delta), which is a boost problem, not a locality one |
| T conserved only up to a gradient (unimodular/TDiff) | **DERIVED (own)**: it does not weaken the soft conclusion | W2's redundancy already uses only ξ ⊥ q. V ∝ q for every null q gives V = 0. A gradient source J^ν = ∂^νQ couples only to the longitudinal ξ ∥ q, so it is allowed off-shell. It does nothing for the TT shear walls, since TDiff still forbids h_μν h^μν |
| conserved only in law (ensemble) | REFUTED (bounded) by RZ, RL4 (refereed) | Per-realization non-conservation is the per-shot lensing noise |
| translation not geometric (an internal ℝ³ on asymptotic states: Shannon/SLAC) | allowed by Lemma W | With exact boosts (O1) the ℝ³ must sit inside a positive-energy Poincaré representation, so its spectrum is unbounded and needs a complete tower (I1, N1 Theorem 4, refereed) |
| deformed, non-additive composition (κ-Poincaré/Snyder) | **SUGGESTED**: it violates Lemma W at the order of the deformation | Tree level is Planck-suppressed, like §2.3. Macroscopic bodies meet the "soccer-ball" problem (EP and LLR for planets) unless the deformation is rescaled per composite. Untested here |

### 2.7 Verdict on (1)

- **DERIVED (conditional; hypotheses W2–W5 and regularity).** Gauge decoupling of a massless helicity-2 requires a universal Ward charge Q^μ that is additively conserved in every process. Q⁰ = energy gives universality (the static coupling survives on the grid). Exact additive spatial Q on all processes means S commutes with e^{ia·Q} for every a ∈ ℝ³ (continuous translations on asymptotic states). On an interacting d ≥ 2 grid with a regular local vertex this is impossible (Spohn plus refereed RS/RN/RG).
- **"At the observed precision": REFUTED at tree level** for asymptotic low-energy states (§2.3). DERIVED in the form "exact or tuned", through the β channel (§2.4) and the vacuum and speed channels (§2.5).
- **"local": REFUTED as necessary.** "Geometric translations": not forced by the S-matrix. Forced by exact boosts plus the fall law only at the level of an unbounded P spectrum (I1).

## 3. Part (2): which rule gives exact continuous translations and keeps discreteness

### 3.1 Lemma S: one particle, finite fibre. DERIVED (own, elementary; no-go: needs referee)

**Statement.** On H = ℓ²(Z^d) ⊗ ℂ^n with n < ∞ and site labels N^j, there is no system of commuting self-adjoint X^j and self-adjoint P^j obeying the Weyl relations e^{iaP^j} f(X) e^{−iaP^j} = f(X + a e_j) for all real a, with sup_j ‖X^j − N^j‖ ≤ b < ∞. In plain words: a momentum cannot exactly and continuously translate a position that stays within a bounded distance of the site.

**Proof.**
1. The Weyl relations make E_X(C) and E_X(C + a) unitarily equivalent, where C = [0,1)^d.
2. C is a disjoint union of 2^d translates of C/2, so dim E_X(C) = 2^{dk} dim E_X(2^{−k}C) for every k. Hence the dimension is 0 or ∞. It is not 0: translates of C tile ℝ^d, so 0 would give H = 0.
3. Take ψ ∈ E_X(C)H that is orthogonal to E_N(box_B)H. Then Σ_j‖(N^j − ½)ψ‖² ≥ (B + 3/2)²‖ψ‖², while each ‖(N^j − ½)ψ‖ ≤ (b + ½)‖ψ‖.
4. With (B + 3/2)² > d(b + ½)², projecting onto E_N(box_B) is injective on E_X(C)H. So dim E_X(C) ≤ n(2B + 2)^d < ∞, which contradicts step 2. ∎

**Escapes.**
- n = ∞. Then L²(ℝ^d) ≅ ℓ²(Z^d) ⊗ L²(cell) (the Zak transform) realizes it: I1's "continuum-cube cells" and complete tower.
- Unbounded X − N: positions not tied to sites.
- Composites, whose relative coordinates make the fibre infinite. This is consistent with the I1/M1 open lists.

**Reading.** This is the kinematic root of C3's face delta: i[X, Π] = 1 − 2πδ_face for Shannon/SLAC (`C4_I1_report.md` §3c). It needs no energy, no boost and no interaction.

### 3.2 Lemma G: many-body qubits with geometric isotony. DERIVED (own, conditional on GNVW; no-go: needs referee)

**Statement.** There is no strongly continuous group α_a (a ∈ ℝ) of automorphisms of the qubit-chain quasi-local algebra with α_a(A_[m,n]) ⊆ A_[m+⌊a⌋, n+⌈a⌉]. The same holds for Z³ with a finite transverse torus L².

**Proof.**
1. For a ∈ [0,1], α_a is a QCA with neighbourhood {0, +1}. Strong continuity is norm continuity on the finite-dimensional A_[m,n+1].
2. The GNVW index is multiplicative and constant along continuous QCA paths (Gross–Nesme–Vogts–Werner 2012; from memory). So ind α₁ = ind α₀ = 1.
3. But V = T⁻¹α₁ maps every A_[m,n] into itself. It is therefore on-site, with index 1. So ind α₁ = ind T = 2 (or 2^{L²}). This contradicts step 2. ∎

**Relation to earlier results.** This closes the I1 referee's commutant loophole ("T = UV merely forces V to carry the shift index", `C4_I1_referee.md`) **for geometric translations**.

**The loophole left:** a non-geometric continuous ℝ³ acting only on the asymptotic sector, with T = U(1)V and V an index-carrying symmetry that is not on-site. RN2/N1 left this open: "Lemma F remains plausible but unproved".

### 3.3 Lemma RS: relativistic nets. DERIVED (standard: Reeh–Schlieder 1961)

**Statement.** Take a local net with continuous translations, the relativistic spectrum condition (joint spectrum in V̄₊, which O1's exact Lorentz invariance supplies) and a vacuum, with translates of a region's algebra generating an irreducible algebra. Then the vacuum is cyclic for every A(O), so every nontrivial local algebra is infinite-dimensional.

**So** "finitely many states per unit volume" is incompatible with exact translations plus Lorentz invariance in any local quantum net. It is the quantum analogue of Lemma Q (classical configurations) and BHS (graphs).

**Without the spectrum condition** (finite minimal-length nets, not additive): an index-flow sketch like Lemma G suggests these are excluded too. **SUGGESTED** only; it would contradict O1 in any case.

### 3.4 The candidates

| Candidate | Exact continuous translations? | Discreteness lives in | Refereed walls it meets | Tested? |
|---|---|---|---|---|
| **Events** (Poisson sprinkling) | In law only (Lemma Q) | Count | Per-realization noise: RZ FAIL (bounded), RL4, E1 crackle, M-A/M-D massive coherence, formation F. In O2's terms, the frozen realization absorbs momentum and Lemma W fails per shot | Yes. The coherent version is Q1, running |
| **Qubits on continuous positions** (a fluid of qubit carriers) | Yes (Σp_j) | Carrier number, plus the internal ℂ² | Qubit price, since each carrier is L²(ℝ³) ⊗ ℂ² (P5). Fluid wall F1b: the rest frame splits speeds, and flat space forces ρ + p = 0. A Lorentz-invariant "fluid" is a vacuum, so this collapses into the next rows | Yes (F1b, P5) |
| **Finite Hilbert space per unit volume** | No, if geometric (Lemmas S, G); no, if relativistic (Lemma RS) | — | Excluded by §3.1–3.3 | **New no-gos** (need referee) |
| **Continuum fibre per cell** (I1 tower) | Yes, exact Poincaré | Nowhere: the cells are bookkeeping (Zak) | Qubit price P10. The grid regulates nothing; the interacting UV problem returns (I1 §3a caveat). Stiffness vanishes with a Lorentz vacuum (T0 analogue: the cutoff moves with the geometry). The mediator is still not produced | Yes, as a construction (I1 §3a) |
| **Band-limited / Shannon** (Kempf) | Yes, as an internal ℝ³ (P bounded), no boosts | Information density (one degree of freedom per Nyquist cell) | C3 face delta (I1 §3c); T1(a2) speed split for smooth spatial regulators with continuous time (CWC); P14 non-locality. A geometry-covariant cutoff gives zero stiffness (T0) | Partly (I1 §3c, T0, T1) |
| **Emergent exact ℝ³ on the asymptotic sector of a qubit grid** (T = U(1)V) | On asymptotic states only | The sites | Vacuum Ward identity (P0, V3, RV4); M1 bounded FAIL for isolated composite bands; RN2 INCONCLUSIVE leaning FAIL; boosts need the tower (N1 Theorem 4) | Partly. The open d ≥ 2 index lemma |
| **Snyder / fuzzy coordinates** (discrete spatial spectra, exact Lorentz, deformed translations) | No: deformed | Coordinate spectra | Predicted (suggested): Lemma W defect at the deformation order, and the soccer-ball problem against EP/LLR for macroscopic bodies. RB covers only torus momentum spaces, not Snyder's de Sitter momentum space | **Not tested** (0 repo hits) |
| **Continuum substrate plus sparse, covariant-in-law records** (relativistic GRW flashes, Tumulka's rGRWf) | Yes in the dynamics; records break it per event | Records (count) | Needs P10/Π-B anyway. Per-event kicks are a stochastic ∂_μT^{μν} = J^ν, which the Bianchi identity tolerates only as a gradient (unimodular; Josset–Perez–Sudarsky 2017). Heating and decoherence bounds (CSL type; §8's 4e-151 at Planck density). O4's question | **Not tested against the gravity walls.** Listed as records fork F in `DECISION_MATRIX.md`, on the grid only |

**Is there a candidate not yet tested?**
- **Yes, two:**
  - **Snyder-type** non-commutative coordinates;
  - **continuum plus sparse covariant record flashes.**
- Neither gives *exact discrete positions with exact translations*. Lemmas S, G and RS say nothing of that kind exists under their hypotheses. Snyder keeps discrete spectra by giving up exact translations, which Lemma W charges for. The flash candidate is the only one that keeps exactness and puts the discreteness where the axioms already have it: Record.

### 3.5 The minimal rule (SUGGESTED as the minimal one; each leg derived above)

**The rule.**
- Positions on a continuum base with exact geometric translations. Per O1, this is Minkowski space with exact Poincaré invariance.
- A finite fibre per **point** (M₂(ℂ)), giving infinite-dimensional, type III local algebras.
- A local (differential/microcausal) admissibility rule, covariant under the continuous group.
- Discreteness only in records: sparse, covariant in law, and locking only coarse or conserved data (O4).

**What it gives back.** The C3/I1 closure, one cone, zero shear stiffness up to the cosmological constant, and conserved additive momentum.

**What it does not give.** A graviton. The WW corollary (§2.1) says the graviton needs its own gauge redundancy.

## 4. Part (3): the axiom changes, named as prices (none adopted)

| # | Price | Axiom touched | What it buys, per the record |
|---|---|---|---|
| Π-A | Z³ replaced by a continuum base with exact geometric translations (and Lorentz, per O1). The grid survives at most as a sampling partition | Lattice (`MINIMAL_AXIOMS_2026-06-29.md:37`) | Removes C3, RS, RN, RG, C1, RB at their root (Lemma S, Lemma G); conserved additive momentum |
| Π-B | Local algebras infinite-dimensional: M₂(ℂ) as a per-point fibre, equivalently I1's per-cell tower (P10 in Zak form) | Qubit (`:47`), in its per-volume reading. **Forced** by Π-A (Lemmas S, G, RS) | Exact Poincaré representations; boosts close |
| Π-C | A local rule covariant under the continuous group, replacing "one fixed nearest-neighbour rule" | Admissibility (`:57`) | Locality on a continuum. "Nearest neighbour" has no meaning there |
| Π-D | Record formation covariant in law and sparse. A record locks only coarse, conserved or gauge-invariant data | Record (`:77-80`), plus a formation law (downstream, `:184`) | Keeps a discrete element without breaking translations in the dynamics. Bounded by heating and decoherence (P4; O4) |
| Π-E | The framework stops being a regulator | none (consequence of Π-A and Π-B) | The interacting UV completion of matter and gravity must come from elsewhere (I1 §3a caveat) |
| P0′ | **Alternative, no axiom change:** keep the grid and tune | none | Existing P0 (5.7e-99 per shear number; 11 counterterms on Z⁴) **plus** about 1e-12 to 1e-13 per matter channel in β to meet MICROSCOPE (§2.4), if loop splits are not otherwise protected. This is weaker than O1's 1e-17 to 1e-20, so it adds no new tuning beyond O1's, but it confirms the same one-β requirement from the gravity side |

## 5. Against the brief's expectation

The registered expectation was: "DERIVED: an exact continuous translation symmetry is necessary; discreteness must live off the translation group."

- **Partly met, with two corrections.**
  1. **Necessity** is DERIVED in the S-matrix sense (exact additive momentum, i.e. continuous translations on asymptotic states), under W2–W5 and regularity. **At the observed precision** it is DERIVED only as "exact or tuned" through the β, vacuum and speed channels. The tree-level EP/soft route is REFUTED as a source of the necessity (§2.3).
  2. **"Discreteness off the translation group"** is DERIVED in the sharper form of Lemmas S, G and RS: no finite-information-per-cell substrate carries exact geometric continuous translations, or relativistic ones.
- **Two adjustments to the brief.**
  - "Local T" is not necessary: REFUTED by SLAC (refereed G3).
  - The unimodular gradient alternative does not weaken the soft conclusion.

## 6. For the referee: no-go items needing codex sol before recording

1. **Lemma S** (§3.1). Check the halving step for unbounded X, the box comparison constant, and the claim that it underlies C3's face delta.
2. **Lemma G** (§3.2). Check that GNVW homotopy invariance applies to strongly continuous groups (via norm continuity on finite-dimensional local algebras), the "V on-site" step, and the transverse-torus extension.
3. **Lemma F** (§2.4). Check the exact fall law, its semiclassical scope (wavepacket width, band isolation), and the sector-additivity assumption behind the channel table.
4. **The REFUTED tree-level claim** (§2.3). Check exponent 2 and its scope: the low-energy, non-umklapp on-shell manifold; nearest-neighbour KG only.
5. **The unimodular soft argument** (§2.6, row 2).

## 7. Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/O2/`:
- `o2_soft_ward_defect.py` and `.out`: the tree-level Ward-defect scaling and the umklapp example.
- `o2_ep_beta.py` and `.out`: the fall-law integration and the MICROSCOPE channel table.
- `O2_report.md`: this report.
