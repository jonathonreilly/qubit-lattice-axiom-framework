# C5 probe O5: round-1 synthesis (forced properties, minimal axiom sets, round-2 design)

**Worker.** Claude Opus 5.5 (probe O5), the same model family as O1–O4, Q1 and the supervisor. **This synthesis is not refereed.** Run 2026-10-12, 11:34Z to 11:52Z. No repository file was edited.
**Scratch.** `scratchpad/C5/O5/`: `o5_checks.py` and `o5_checks.out` (two small checks, §2.6); `O5_round2_prereg.md` (the round-2 pre-registration text only).
**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md` "Campaign C5" (lines 2302–2371); `SUMMARY.md` §§14–20; `PRICE_NOTE.md` v5 and the v6 delta with its wrap-up additions; the five round-1 worker reports; the five codex verdicts listed below; `O2_referee.md` §§7–8; `O3_referee.md` §§1–2. **Prior art checked:** T2 (`TESTS.md:86-126`; perfect-action kernels already tested for TT stiffness). The repository has no hits for Snyder, Malament, Halvorson or Ginsparg–Wilson.

**Inputs and their status when this was written (11:50Z; all five referees are in).**

| Probe | Worker reading | Codex referee (gpt-5.6-sol, xhigh) | What survives refereeing |
|---|---|---|---|
| O1, Lorentz invariance | DERIVED "V₂^tl = 0 or tuning"; REFUTED "only Lorentz-in-law substrates avoid tuning" | **NOT CONFIRMED** | The invariant counts; Lemma A's implication V₂^tl = 0 ⇒ V₁ = 0; Lemma C; C′ with norm-preserving covariance; the abstract Lemma D; Lemma E with a proper convex cone; Lemma B only under its commuting-evolution premise. **O1-N is SUGGESTED**, because H2 imports a natural size. REFUTED is correct only for dimension-4 matter. The full matter-plus-gravity claim stays open. The UHECR 6e-20 bound is based on an iron nucleus, so it is not a clean p–γ bound. The dimension-6 margin is 7.76 decades, not 6.68. There are N−1 independent relative-speed directions, not N(N−1)/2 |
| O2, universality | DERIVED (exact translations in the S-matrix sense) | **CONFIRMED WITH CORRECTIONS** | Lemma W, conditional on the exact Ward-residue identity. Lemma F, conditional (an isolated band bottom, leading weak-field order). Tree-level necessity REFUTED, narrowly. Lemmas S and G and Reeh–Schlieder, DERIVED in their bounded domains. The minimal rule and the prices Π-A to Π-E are SUGGESTED. Π-B conflates a per-point fibre, region algebras and a per-cell tower |
| O3, vacuum and shear | DERIVED (free class); qubit pairing FAIL (bounded) | **CONFIRMED WITH CORRECTIONS** | Theorem 1(a), with finite species, c_s > 0 and compact spectra. Theorem 1(b) is false. **Qubit pairing: INCONCLUSIVE**, with a bounded FAIL for on-site CCR + CAR pairs. FS M1 is a genuine escape, but it has no bridge to the gravitational E_g, and visible partners are not shown |
| O4, records | DERIVED "records copy, never measure" | **NOT CONFIRMED** | Lemma 1 (V ≤ BC), given orthogonality (H0). The Poisson BC formula is exact. Theorem C holds in its narrow model. The 0.1 µm heat bound holds. Bell non-factorization holds. The trilemma is incomplete. **P4′ is a sufficient policy, not a necessity.** The 70 s experiment used Cs-133, at 1.9 µm |
| Q1, coherent event substrate | FAIL (bounded); INCONCLUSIVE leaning FAIL if structured phases count | **CONFIRMED WITH CORRECTIONS** (arrived 11:49Z) | **FAIL is proved** for orthogonal sprinkling labels with configuration-diagonal coupling and **fixed Poisson Born weights**, when the substrate is traced out or later acted on only by itself. The light then carries \|Ψ\|² + V, inheriting RZ's ln(N_B/S) ≥ 43,986 within RZ's scope. Uniform postselection with same-mode circular-Gaussian noise fails conditionally, by extinction: 2Ψ/(2+V) is exact, but transferring RZ's variance into that mode is a conditional bridge. **The full class is INCONCLUSIVE, leaning FAIL.** Still open: structured multimode amplitudes, a tuned joint unitary that erases the branch information (so projection is not logically necessary), other spectral mechanisms, and matter-induced decoherence (only the toy readout's sensitivity is shown). **P-Q1 is a sufficient candidate price, not a necessity.** The vacuum lemma excludes non-collinear spacelike absorption by a local operator; complete silence needs, in addition, a gap or no null spectral weight |

**Labels.**
- **refereed:** a codex verdict confirms the item, with its corrections applied.
- **SUGGESTED:** argued only, or downgraded to SUGGESTED by a referee.
- **O5:** new here; same family; unrefereed.
- **naturalness:** the item needs a no-tuning premise. It is not forced by data and logic alone.

---

## 0. In plain words

**What round 1 asked.** What must the rules do so that the world looks the way experiments say it does?

**What the observations require.** Eight kinds of observation give eight requirements. Most have the form "a symmetry, or a number set by hand".
1. **One light speed.** All matter shares one light speed, to parts in 10¹⁷–10¹⁹. Either the law has no special direction in spacetime that a particle's speed can feel, or each speed difference is tuned by hand.
2. **Massless gravitational waves at light speed.** The graviton needs an exact gauge identity, or about 11 hand-set numbers on a spacetime grid.
3. **Everything falls alike.** At the measured precision this follows from item 1. It adds no new cost.
4. **One universal spin-2 force.** Momentum must add up exactly in collisions. A finite qubit per site cannot carry exactly continuous translations.
5. **The vacuum barely gravitates.** This needs one of:
   - boson and fermion spectra matched exactly, which what we see excludes;
   - a supercharge structure, whose partners are not seen;
   - a tuning;
   - an imposed rule.
6. **Lensed images are sharp.** The grain of spacetime must not scatter light differently shot by shot.
   - Random events do (refereed).
   - Making them a plain quantum superposition does not help (refereed). Exotic quantum versions are not closed (INCONCLUSIVE, leaning FAIL).
7. **Big molecules interfere.** Any record that learns "which way" must be rare and coarse.
8. **Bell tests.** Records cannot be drawn site by site, each independently.

**Three ways are left to meet all eight, and they contradict each other.**
- **A. A continuum, with discreteness only in records.**
  - Space and time are continuous. Records are rare flashes.
  - It passes everything except the vacuum energy.
  - But the grid then does no work, and the graviton is still put in by hand.
- **B. A 4D grid with equal steps in time and space (Euclidean).**
  - The grid's own symmetry protects the matter light speeds.
  - Gravity still needs an exact gauge identity on that grid, which nobody has found; otherwise 11 tunings.
  - The arrow of time must sit in the state, not in the law.
  - With chiral matter, the grid's weights are probably not probabilities.
- **C. Keep the 3D grid and tune.** No axiom changes. The hand-set numbers:
  - at least one to 3 parts in 10¹⁷, for matter speeds;
  - two to about 1 part in 10⁹⁹, for shear;
  - the vacuum energy.

**What none of them does.** None of the three produces the graviton. All three leave the vacuum energy (Λ) unexplained.

**Two things that are now (nearly) closed.**
- **Random spacetime events that steer light.** These are excluded at the shared scale (refereed). A plain quantum superposition of them does not rescue them (refereed); the exotic quantum versions are unclosed.
- **A quantum vacuum with countable events.** O5 sketches a short proof that a positive-energy quantum vacuum cannot contain countable events at all. It needs a referee.

**What round 2 should test (§3).**
- Can the 4D grid have an exact gauge identity without secretly being a continuum? This decides between B and A.
- Can any Lorentz-invariant discreteness of events exist? This closes or reopens the event routes.
- Do rare record flashes clash with gravity? This decides whether A is consistent.
- Are B's weights probabilities, and can B's arrow of time sit in the state?
- Does Snyder's discrete space with exact Lorentz symmetry give a fourth option?

---

## 1. The forced-properties list

Each entry gives the observation class, then:
- the property it forces on the rules;
- the kind of force;
- the status;
- the escape routes left.

"Escape" means a route the refereed record does not close. It does not mean a construction exists.

### F0 (internal, refereed walls): the boost wall

This is not an observation. It is the theorem that turns F1, F2 and F4 into prices for every grid set.
- **The wall.** A regular local lattice law has no boost that closes with its own momentum. Six refereed appearances:
  - C3;
  - I1–I3;
  - M1;
  - K2, at O(κ²);
  - RB;
  - RFW (`SUMMARY.md` §§15–20).
- **What follows.** The lattice is a preferred-frame theory (RB, refereed).
- **Escapes:**
  - a continuum tower per cell (P10);
  - non-local (SLAC) matter (P14);
  - patchwise or singular DSR;
  - fully deformed non-first-moment algebras;
  - quasi-local perfect actions (RFW open);
  - altered leading generators;
  - multi-band matter.

### F1: matter light-cone bounds

**Observations** (bounds verified by O1; the O1 referee checked the numbers):
- LHAASO 1.4 PeV photon: c_γ − c_e < 2.66e-19;
- Auger/HESS: 6e-20, one-sided, iron-based and indicative;
- LEP/Tevatron: about 1e-11, two-sided;
- IceCube: about 1e-18;
- LHAASO dimension-5 and dimension-6 limits.

**Property.** No dimension-4 preferred-tensor speed operator may be present at natural size. Two ways to meet that:
- **(i) A symmetry condition.** The law's point group has V₂^tl = 0, which implies V₁ = 0. This is a **sufficient** condition (refereed).
- **(ii) Tuning.** Each of the N−1 independent relative-speed directions is tuned.
  - The one refereed instance is F2's lattice QED: −8.55e-3 natural, so a tuning to 3.1e-17.
  - That instance is regulator-specific (O1 referee).

**Kind.** Logical for the counts. **Naturalness** for "(i) or (ii)": O1-N is SUGGESTED, since H2 imports a universal natural size.

**Status.**
- **Counts (refereed):**
  - Z³ × ℝ with proper cubic O only, i.e. the axioms' group: (V, S₂) = (1, 2);
  - B4⁺ or W(B4) on Z⁴ at ξ = 1: (0, 1);
  - the arrow-keeping subgroup of W(B4): (1, 2).
- **Lemma C (refereed):** every compact subgroup of O(1,3) has V₂^tl ≠ 0.
- **Lemma C′ (refereed after correction):** summable spanning couplings with norm-preserving covariance give a finite point group.
- **Lemma D (refereed, abstract form only):** a connected symmetry that normalizes Z^d acts trivially on it. Its "continuum fibre, Qubit price" consequence is SUGGESTED.
- **Lemma E (refereed, with a proper convex cone):** a finite group that keeps a time orientation has V₁ ≠ 0.
- **Lemma B (refereed only under its premise):** a real-time law whose symmetries all commute with its evolution has a preferred frame.
- **Refereed counterexample to "only Lorentz in law":** a whole-law W(B4) Euclidean grid at ξ = 1 gives Δ = 0 for dimension-4 matter (F2). It forbids dimension-5 terms (S₃ = 0). It leaves dimension-6 terms at (E/E_Pl)², 7.76 decades inside LHAASO's quadratic bound.

**Escapes.** This list is not a proved classification (O1 referee).
- (α) A Euclidean finite group with V₂^tl = 0, and no arrow in the law.
- (β) Lorentz invariance in law, i.e. random events. These meet F6.
- (γ) Exact continuous Poincaré symmetry.
- (δ) Non-summable couplings, i.e. unbounded valency.
- (VI) DSR or Snyder deformation.
- (VII) A sequestered preferred frame (RF3, INCONCLUSIVE).
- Tuning.

### F2: graviton speed and mass

**Observations.**
- GW170817: −3e-15 ≤ (c_T − c)/c ≤ 7e-16.
- m_g ≤ 1.27e-23 eV.

**Property.** One of the following:
- an exact linearized-diffeomorphism Ward identity. It forbids every h-only mass and leaves 1 of the 9 W(B4) two-derivative forms;
- **11 tunings on Z⁴**, the exact codimension of gauge restoration (K1, refereed);
- 2 TT tunings, each to 5.7e-99 of natural size (refereed), plus speed tunings. The Z³ × ℝ total of at least 6 is a reading.

**Kind.** Logical for the counts. Naturalness for "identity or tunings". The B referee already listed non-gauge exits: tuning, extra symmetries, non-locality, holography, constrained sectors, correlations, strong flows, and no local graviton variable.

**Status.**
- Refereed.
- Every lattice identity tested fails:
  - K2 at O(κ²), bounded;
  - RFW, a bounded FAIL;
  - T2: the perfect-action kernels give a p = 4 stiffness floor when coupled through proper distance. The κ ≡ 0 relabelling is a free-level escape that Lemma R blocks for interacting matter.

**Escapes.**
- Quasi-local perfect or Ginsparg–Wilson-type lattice identities with interacting matter (untested at O(κ²)).
- Altered leading generators.
- Multi-band matter.
- A continuum (set A).

### F3: universality of free fall

**Observations.**
- MICROSCOPE: about 1e-15.
- Eöt-Wash and LLR: about 1e-13.

**Property.** All species and composites share one β = Hess(E²/2) at their band bottom. That is the k = 0 half of C3's closure condition, and the gravity-side twin of F1.

**Kind.** Conditional logic.
- Lemma F is refereed CWC for an isolated adiabatic band, a slowly varying potential and a supplied energy coupling.
- MICROSCOPE constrains only the two bodies' effective-β difference.
- The per-channel bounds (1e-13 to 2e-10) are SUGGESTED, one channel at a time.

**Status.**
- The grid's tree-level momentum defect, C(pa)² ≈ 2e-41 at 0.25 GeV, cannot force exactness. This was REFUTED narrowly (refereed).
- An F2-size untuned split would give about 3.5e-5. The arithmetic is refereed; the mapping is model-dependent.

**Escapes.** Whatever meets F1 by symmetry gives a common β at this order. F3 adds no independent price. That last statement is SUGGESTED, a naturalness reading.

### F4: a massless spin-2 field coupling universally

**Basis.** Theory (Weinberg's soft theorem) plus the existence of gravitational waves.

**Property.** The soft residue is a charge that adds up in every collision channel. With continuous time, its time component is the energy. On asymptotic states, that means exact additive momentum.

**Kind.** Conditional logic, refereed CWC. It holds given the exact Ward-residue identity; the identification Q⁰ = E needs a Noether bridge.
- A local stress is **not** necessary. That was REFUTED by SLAC (G3, refereed).
- The class-wide lattice spatial no-go is not DERIVED. It holds only for Spohn's class and the RS and RG classes.

**Status** (refereed in bounded domains). Exact geometric continuous translations are incompatible with:
- finite fibres tied uniformly to the sites (Lemma S);
- a strictly local continuous interpolation of a qubit chain's shift (Lemma G, in 1D or a finite cylinder);
- finite-dimensional bounded-region algebras in a positive-energy relativistic net (Reeh–Schlieder).

**Escapes.**
- Non-geometric asymptotic translations (T = U(1)V; RN2's index lemma in d ≥ 2 is open).
- Unbounded site displacement.
- Quasi-local or asymptotic-sector actions.
- The infinite-transverse many-body case.
- Snyder deformation, which gives up exact additivity (SUGGESTED soccer-ball cost).

### F5: vacuum energy and the E_g shear

**Observations.**
- ρ_Λ/M_Pl⁴ = 1.1e-123.
- The E_g response must be ≤ 5.7e-99 of natural size, and free local matter alone produces the natural size (V3, RP and RV4 refereed).

**Property** (free class, refereed CWC: Theorem 1(a)). Take finitely many species with positive common mass scaling and compact rescaled spectra. If the cancellation is untuned on an open mass interval, the aggregate signed density-of-states measures must be equal.
- The tolerances are weighted mass-squared mismatches: ≤ 1.48e-84 GeV² for Λ and ≤ 1.6e-63 GeV² for E_g. Their square roots are not physical mass splittings (referee).

**Kind.**
- The "open interval" is a sufficient robustness hypothesis, not forced (referee).
- Theorem 1(b) is false.
- Interacting necessity is SUGGESTED.

**Status.**
- **Qubit site (refereed):**
  - a site cannot carry an exact CCR boson plus a CAR fermion;
  - Jordan–Wigner and exact bosonizations give one spectrum, not a pair;
  - the full qubit-pairing test is **INCONCLUSIVE**.
- **FS M1 lattice SUSY on one fermion mode per site (refereed as legitimate).** It gives E_vac(ε) ≡ 0 exactly when the strain enters through Q. But:
  - no bridge identifies that strain with gravitational E_g;
  - many-body doublets do not establish visible superpartners. The "excluded" label is too strong.
  - The 3D index growth is shown only for 3×3×L_z tubes.

**Escapes.**
- Tuning (P0, Λ).
- R₀/P13 (vacuum-referenced; it must subtract only the state-independent vacuum c-number, SUGGESTED from the equivalence principle).
- Unimodular gravity (Λ only).
- Exact continuous translations plus a diffeomorphism Ward identity (E_g only).
- A supercharge rule: H = {Q, Q†}, gravity coupling through Q, graded sites. It owes an account of unseen partners.

### F6: coherent lensed images (radio, optical, VLBI)

**Property.** Spacetime microstructure that steers propagation must not carry per-realization weight at spacelike momentum transfer, at the shared ℓ_k.
- **Refereed.** RZ is a FAIL at the controlled level for Poisson events. It is bounded to the scalar readout, sources with a definite switch-on and a shared ℓ_k. RL4 gives the noise growth.

**Q1 (refereed CWC):**
- **FAIL, proved for a subclass:** orthogonal sprinkling labels, configuration-diagonal coupling, **fixed Poisson Born weights**, with the substrate traced out or later acted on only by itself. The light is then exactly the classical mixture: ⟨a⟩ = Ψ (the RL2 mean) and ⟨a†a⟩ = |Ψ|² + V (RZ's variance).
- **Final-state projection, conditional.** Uniform postselection with same-mode circular-Gaussian noise dims the image by 2/(2+V), which is exact. Mapping that onto RZ's e^(−4.4×10⁴) needs a conditional bridge: RZ's in-band variance must sit in that one mode.
- **Structured amplitudes.** The single-mode construction is mathematically correct.
  - Its input-dependent postselection is not itself a Born-rule violation.
  - Deterministic renormalized final-state evolution would be nonlinear.
  - The multimode case is open, and so is a tuned joint unitary that erases the branch information. These keep **the full class at INCONCLUSIVE, leaning FAIL**.
- **The vacuum lemma.** A local operator in a translation-invariant positive-energy vacuum cannot absorb non-collinear spacelike momentum. Complete silence also needs a gap or no null spectral weight.
  - It does not forbid γγ → γγ.
  - Exact Poisson density covariance is incompatible with a local vacuum Wightman correlator.
  - **P-Q1 is a sufficient candidate price, not a necessity.**
- **Matter decoherence.** Only the toy readout's regional sensitivity is shown (s_R = 0.19–0.47 near the source). Environmental recording is unproved.

**O5 (§2.6, unrefereed):**
- In such a vacuum there are no local, additive, integer-valued event counts at all (Lemma N-Q sketch).
- Separately, Q1's suggested "boundary-law count variance" test is not general. A vacuum spectral measure supported on the forward cone gives exactly volume-law variance (CHECKED).

**Escapes.**
- Sources with no definite switch-on.
- A ℓ_k not shared with matter (events that carry only gravity).
- The scalar-to-photon transfer.
- Events that steer nothing (inert).
- Non-Poisson classical Lorentz-invariant processes: open; R2-2's Lemma P-L.
- Born weights that are not Poisson.
- Structured multimode final-state amplitudes.
- A tuned joint unitary that erases the branch information (Q1 referee).

### F7: matter-wave interference and long coherence

**Observations.**
- 25 kDa molecules.
- Cs-133 at 1.9 µm for 70 s.
- Ions coherent for more than 1 h.
- Earth's heat flow.

**Property.** A permanent, perfectly distinguishable record that acquires branch information caps the visibility at V ≤ BC(p_A, p_B) (refereed, given H0 orthogonality). Read together with the Record axiom, every observed interference experiment is a bound on record formation.

**Kind.** Logical for the bound. The necessity "records copy, never measure" is **not DERIVED** (refereed NOT CONFIRMED): P4′ is a sufficient policy.

**Status** (refereed numbers):
- **Fixed-cell Poisson records** at ℓ_P⁻⁴√−g in branchwise Newtonian metrics give −ln BC = 2π m²c³ d T/ħ².
  - That is 4.88e40 for 25 kDa.
  - For Cs-133 at 1.9 µm it is 9.88e40 (fine) or 2.98e24 (coarse).
- **A Gaussian lock at 0.1 µm** is limited to ≤ 5.3e-11 s⁻¹ per nucleon by the Earth-heat allowance. The Planck-width figure is not physical.
- **A lock of a conserved quantity** injects no energy only if it commutes with H. Local densities generally do not.

**Escapes.**
- Branch-insensitive collective records.
- Weak or rare records.
- Correlated records.
- Gauge-redundant data.
- Records of data already decohered.
- A coarse flash budget (P4′-f).

### F8: Bell violations

**Property.** Under measurement independence, single outcomes, no retrocausality and Bell-local conditional independence, the joint law of record formation cannot factorize given local data (refereed CWC).

**No axiom change.** Admissibility's per-site distribution must be read as a **marginal**, not as a complete independent formation law. Read that way, it does not conflict as written (refereed).

**Escapes.** Retrocausal or two-boundary laws, superdeterminism, and many outcomes. This matters for set B (§2.2, B3).

---

## 2. Minimal sets of axiom changes

### 2.0 What every surviving set shares (no choice involved)

1. **Records (F7, F8).** Fresh "which-way" records must be rare and coarse, inside the refereed budget. Admissibility's distribution must be a marginal of a non-factorizing joint law. Both are readings or downstream rules, not axiom text changes (refereed for F8; O4's P4′/P4′-f wording is a suggested policy).
2. **Λ.** It is unexplained in every set: either tuned to 1e-123 or left as a unimodular integration constant.
3. **The graviton.** It is supplied, not produced, in every set. That is a reading, as on 09-29.

### 2.1 Set A: continuum base, discreteness only in records

**Prices.** Named, not adopted.

| # | Price | Axiom text touched | Earlier label |
|---|---|---|---|
| A1 | Sites become the points of Minkowski space, with the exact Poincaré group | Lattice: "Physical sites are the points of the cubic lattice `Z^3` …" (`MINIMAL_AXIOMS_2026-06-29.md:37-38`) | Π-A, O1.3 (sufficient, not uniquely forced: O2 referee) |
| A2 | M₂(C) stays the per-point value domain. Bounded-region algebras become infinite-dimensional, as Reeh–Schlieder forces. This is not P10's per-cell tower verbatim | Qubit (`:47`), in its per-volume reading | Π-B, as corrected by the O2 referee |
| A3 | A microcausal local rule, covariant under Poincaré, replaces "one fixed nearest-neighbor rule … proper cubic rotations". The per-site distribution is read as a marginal (F8) | Admissibility (`:57-61`) | Π-C |
| A4 | Records form rarely and coarsely: covariant in law (flash-like), inside the F7 budget, with a non-factorizing joint law (rGRWf type) | Record (`:77-80`), plus a formation rule, which is downstream (`:184`) | Π-D, P4′-f |
| A5 | The graviton is an independent diffeomorphism gauge field: a supplied primitive, not derived | none (a new primitive) | B referee's condition list |
| A6 | The framework no longer regulates the theory, unless another covariant regulator is supplied | none (a consequence) | Π-E |

**What A passes.**
- F1: by symmetry, exactly.
- F2: with A5.
- F3 and F4: exact.
- F5, E_g: the diffeomorphism Ward identity forbids it. SUGGESTED: this needs a covariant regulator.
- F6: if records do not steer propagation. SUGGESTED, untested.
- F7 and F8: with the flash budget and a non-factorizing law.

**What A leaves.** Λ (2.0); no graviton produced; no role for discreteness in gravity.

**Plain reading.** Set A is standard relativistic quantum field theory plus a sparse collapse or record layer. The framework's distinctive content shrinks to the Record axiom.

**What decides A.**
- **R2-3:** do covariant flash records clash with the gravity walls (the Bianchi identity, stress noise, Λ drift, heating)?
- **R2-2:** Lemma N-Q. If it holds, a discrete event layer cannot sit inside A's vacuum as local counts. Discreteness is then only in records.
- Whether anything observable distinguishes A from "no lattice at all". That is a reading, not a test.

### 2.2 Set B: a Euclidean Z⁴ grid, the whole law hypercubic

**Prices.**

| # | Price | Axiom text touched | Earlier label |
|---|---|---|---|
| B1 | Sites become the points of Z⁴, with one step in every direction, and the proper hypercubic group B4⁺. Reflections are not needed for the V, S₂, S₃ counts | Lattice (`:37-38`) | O1.1, P12 |
| B2 | **Whole-law** covariance under Z⁴ translations and B4⁺: matter, gauge fields, the graviton and records. This extends the registered `kinetic_isotropy_primitive`, which covers only the matter kinetic form on Z³ × Z_τ | Admissibility (`:57-58`) | O1.1 |
| B3 | The per-site distribution becomes the conditional of a reflection-positive Gibbs specification on Z⁴. Physical probabilities come only after Osterwalder–Schrader reconstruction. **Likely extra price (R2-4):** for chiral fermions and Euclidean gravity the weight is not a positive normalizable probability (RECALLED lore: the complex chiral determinant; the unbounded conformal factor). Chiral fermions without doublers need quasi-local Ginsparg–Wilson/overlap couplings, not nearest-neighbour ones (RECALLED; Nielsen–Ninomiya) | Admissibility (`:60-61`; the reading notes at `:63-73`) | new (O5); O1.1's Gibbs reading |
| B4 | No arrow of time in the law (Lemma E, refereed). The arrow comes from a state or boundary condition. "Records form" and "permanent" must be read in a block (4D) sense | Record (`:77-80`); arrow is an open gate (`:185`) | O1.1 (Record clause); new (O5) |
| B5 | An exact lattice linearized-diffeomorphism identity, or K1's 11 tunings (refereed codimension). No candidate identity is known: K2 is bounded, RFW is a bounded FAIL, and T2's perfect kernels have a p = 4 floor | none (a gravity-sector primitive) or P0-type tunings | K1, P12 |
| B6 | Λ, plus the E_g and K1 mass forms: tuning, R₀ (P13), or a supercharge rule (FS-type; no E_g bridge) | none | P0, P13 |

**What B passes.**
- F1: exactly for dimension-4 matter (refereed under whole-action W(B4)). Dimension 5 is forbidden. Dimension 6 has a 7.76-decade margin. The P-odd dimension-3 terms vanish (V = 0).
- F3: a common c gives a common β (SUGGESTED).
- F6: one crystal, so no per-realization noise.
- F8: through the reconstructed quantum mechanics (standard, RECALLED), with records as marginals.

**What is open or costly in B.**
- F2: B5.
- F4: momentum is exact only up to (pa)², which is fine at tree level (refereed, narrowly). Loops and the vacuum need B5.
- F5: B6.
- F7: the same budget as every set.

**What decides B.**
- **R2-1.** Does a quasi-local, B4⁺-covariant law with finitely many fields per site carry an exact gauge identity through O(κ²)? Or does that identity exist only for a blocked continuum, in which case B collapses into A?
- **R2-4.** Is the weight a probability with chiral content and gravity? If not, B pays B3's extra price.
- **R2-5.** Can the arrow sit in the state? If Record forces a law-level time orientation, Lemma E returns B to the preferred-frame class (class I).
- Coupled reflection positivity (K2 open).

### 2.3 Set C: keep Z³ (time added downstream) and tune

**Prices.**

| # | Price | Axiom text touched | Earlier label |
|---|---|---|---|
| C1 | **Tunings.** See the list below | none | P0 revised, O1.4, P0′ |
| C2 | A downstream real-time law and time metric. These are class I by Lemma B, whose premise holds because the lattice has no boosts (RB) | none (open gate `:185`) | P11 if the foliation is made primitive |
| C3 | The graviton is a supplied lattice field, not produced | none | P0 |

**C1, the tunings in full.**
- **Matter speeds.** One refereed instance at 3.1e-17 (F2, regulator-specific). In general, N−1 relative-speed directions.
- **Graviton speed.** One or three directions (R2 INCONCLUSIVE).
- **Shear.** 2 TT tunings at 5.7e-99. The E_g natural size includes free matter's term (V3).
- **Λ.** About 1.1e-123.
- **P-odd dimension-3 terms.** b₀ and (k_AF)₀ are allowed by the axioms' proper-only rotations (SUGGESTED cost).
- **Total.** At least 6 on Z³ × ℝ (a reading).

**What C passes.** Every observation, but only through C1. F6 holds (one crystal). F7 and F8 hold under the marginal reading and a small record rate.

**Variant C′.** Sequester the preferred frame behind a separate scale (P11 + RF3). Its explicit subcases need hierarchies of about 1e9 in scale and 1e38–1e39 in a coefficient. INCONCLUSIVE.

**What decides C.** No calculation can rule C out, because tuning is always available. It is an owner decision. The open items:
- Is the count finite and stable under the RG? K1's 11 is a linear codimension; the nonlinear completion is not done.
- Can any principle cut the count? RV4 found none; P13 holds by definition; a supercharge rule covers the vacuum only.
- The C′ window.

### 2.4 Observation against set

| | A: continuum + records | B: Euclidean Z⁴ | C: Z³ + tuning | E: events (P1–P4), for comparison |
|---|---|---|---|---|
| F1 matter light cone | exact, by symmetry | dimension ≤ 4 exact by finite symmetry (refereed); dimension 6 inside the bound by 7.76 decades | tuned (≥ 1 at 3e-17) | exact in law |
| F2 c_T, m_g | with a supplied gauge graviton | **open** (R2-1) or 11 tunings | 2 at 5.7e-99, plus speed tunings | G-A/G-B/G-C open |
| F3 free fall | exact | follows from F1 (SUGGESTED) | tuned through F1 | in mean |
| F4 additive momentum | exact | up to (pa)²; loops need R2-1 | preferred frame (RB) | in law only |
| F5 Λ | unexplained | unexplained | unexplained | unexplained (Sorkin's count fluctuation: SUGGESTED) |
| F5 E_g | forbidden by the Ward identity (SUGGESTED) | the identity or tunings | tuning or R₀ | 0 in mean |
| F6 lensing | passes if records steer nothing (SUGGESTED) | passes | passes | **FAIL** at the shared ℓ_k (refereed). A plain quantum superposition fails too (Q1, refereed for fixed Poisson weights); the full quantum class is INCONCLUSIVE, leaning FAIL |
| F7 interference | flash budget | flash budget | flash budget | records-as-events excluded at Planck density (refereed Theorem C, narrow model) |
| F8 Bell | non-factorizing flash law | reconstructed QM | marginal reading | supplied order (P3) |
| Where discreteness lives | records only | spacetime grid | spatial grid | event count |
| Where the arrow lives | may be in the law (the orthochronous group fixes no vector) | the state only (Lemma E) | in the law | supplied order |

### 2.5 Why A, B and C cannot be combined

- **A against B.** An exact connected boost group cannot normalize a lattice translation group (Lemma D, refereed abstract form). B's translations are discrete, and its Lorentz invariance is only that of its long-distance limit.
- **B against C.** B needs the whole law to be hypercubic and has no law-level arrow (Lemma E). C has time as an evolution parameter (Lemma B) and a law-level arrow.
- **A against C.** Continuous translations against the grid.

### 2.6 Not yet minimal sets, and two O5 remarks

**D. Snyder coordinates.**
- What it is: spatial coordinates with discrete spectra, exact Lorentz symmetry, and deformed translations with a de Sitter momentum space.
- Why it matters: it is the only known candidate that keeps discrete space together with exact Lorentz symmetry.
- It is untested. RB covers only torus momentum spaces. The soccer-ball and Lemma W costs are SUGGESTED (O2, refereed as SUGGESTED). It becomes a fourth set only if R2-6 passes.

**E. Events (P1–P4).**
- Excluded at the shared ℓ_k (RZ, refereed bounded).
- The plain coherent rescue fails (Q1, refereed for fixed Poisson weights). The full quantum class is INCONCLUSIVE, leaning FAIL.
- What is left: edgeless sources, a ℓ_k not shared with matter, inert events, non-Poisson weights, multimode final-state amplitudes, joint-unitary erasure.
- R2-2 tests the general case.

**A′. P-Q1, a positive-energy quantum vacuum substrate.**
- The Q1 referee calls it a sufficient candidate price, not a necessity.
- Reeh–Schlieder (refereed) gives it infinite-dimensional region algebras, so it lies inside set A's price list.
- O5 remark 2 below argues that it cannot carry countable events.
- The Q1 referee notes that a local vacuum correlator "does not exclude Poisson measurement outcomes". Remark 2 addresses that case: such outcomes cannot come from local, additive, integer-valued counts in the vacuum. They need non-local or non-additive counts, or records.

**O5 remark 1: volume-law variance needs no spacelike support** (CHECKED, `o5_checks.out` §2).
- Take a vacuum density whose spectral measure is Lebesgue measure restricted to the forward cone V̄₊ (a generalized free field with a constant Källén–Lehmann density). Its count variance in a window of size L is exactly L^d × Var(1), because the cone is invariant under dilation.
- Monte Carlo ratios for L = 1, 2, 4:
  - d = 2: 3.987 and 4.009, against 4;
  - d = 4: 15.98 and 16.01, against 16.
- **So "volume-law count variance" does not single out Poisson.** Q1's suggested distinguishing statistic ("sub-Poissonian, boundary-dominated for a local vacuum") is not general.
- The distinguishing property is the spacelike support itself, i.e. on-shell light scattering, as Q1's Lemma E has it.

**O5 remark 2: Lemma N-Q sketch.** No countable events in a positive-energy vacuum. SUGGESTED: a no-go, so it needs the codex referee before it is recorded.

*Hypotheses:*
- **(N1)** Translations are unitary, with spectrum in V̄₊ and a unique invariant vector Ω.
- **(N2)** Locality, with Ω separating for every bounded-region algebra (Reeh–Schlieder hypotheses).
- **(N3)** Each bounded 4D region O has a count N(O) affiliated with A(O), with spectrum in {0, 1, 2, …}.
- **(N4)** Additivity over finite disjoint unions, at every separation, timelike included.
- **(N5)** Fine-scale simplicity: any finite family of regions has a common refinement into regions on which N is a projection.
- **(N6)** Covariance, U(a)N(O)U(a)* = N(O+a), with ⟨N(O)⟩ = ρ·vol(O) and ρ > 0.

*Sketch:*
1. **Disjoint fine regions commute.** For disjoint fine regions, P = N(O₁) and Q = N(O₂) are projections, and P + Q has integer spectrum by N3 and N4. Halmos's two-projection theorem says the generic part of P + Q has spectrum 1 ± cos θ with θ ∈ (0, π/2), never an integer. So PQ = QP (`o5_checks.out` §1).
2. **All counts commute.** By N4 and N5, every N(O) commutes with every N(O′), translates included.
3. **The count is a constant.** Let F(a) = ⟨Ω, N(O)N(O+a)Ω⟩, the Fourier transform of the spectral measure of ψ = N(O)Ω, which N1 supports in V̄₊. Commutation and invariance give F(a) = F(−a). So the measure is supported in V̄₊ ∩ (−V̄₊) = {0}. Then ψ is translation-invariant, so ψ = ⟨N(O)⟩Ω. By N2 (Ω separating), N(O) = ρ·vol(O)·1.
4. **Contradiction.** Pick O with ρ·vol(O) not an integer. That contradicts N3. ∎

*Meaning.*
- If it holds, discreteness of spacetime events cannot be observable counts in a positive-energy vacuum. Discreteness then needs one of:
  - a mixed classical state with spacelike support, i.e. noise if the events steer light (F6);
  - counts that are non-additive, non-local, or defined only on slices (which needs a frame);
  - records.
- It is close to Malament (1996) and Halvorson–Clifton (2002), "no localizable particles" (RECALLED; count once). What may be new is the spacetime-event version, with additivity across timelike separations.

---

## 3. Round 2: the decisive tests (summary)

The full pre-registration text is in `O5_round2_prereg.md`. The tests are listed in priority order.

| ID | Test | Decides | Expectation |
|---|---|---|---|
| R2-1 | Class II gravity. An exact lattice gauge identity on Z⁴, via quasi-local, perfect or Ginsparg–Wilson-type actions, through O(κ²), with finitely many fields per site | B survives, B collapses into A, or B pays 11 tunings | INCONCLUSIVE, leaning COLLAPSES-TO-A |
| R2-2 | Lorentz-invariant discreteness. Lemma N-Q (a quantum vacuum has no integer event counts) and Lemma P-L (no classical Lorentz-invariant point process has zero spacelike structure factor) | Closes E and A′ in general, or reopens them | N-Q DERIVED; P-L SUGGESTED |
| R2-3 | Record flashes on a continuum against the gravity walls: Bianchi/unimodular, TT stress noise, Λ drift, heating, Bell | Whether A is consistent | PASS at GRW-type rates, with the reading that the flashes are gravitationally inert |
| R2-4 | Set B's weight. Positivity, normalizability and reflection positivity with chiral fermions and gravity on Z⁴ | B's extra Admissibility price (distribution becomes weight; nearest-neighbour becomes quasi-local) | DERIVED for chiral nearest-neighbour; SUGGESTED for gravity |
| R2-5 | The arrow in the state. Can "records form, records are permanent" hold under a time-symmetric whole-law B4⁺ rule? | Whether B is compatible with Record | SUGGESTED (block reading), with a REFUTED risk |
| R2-6 | Snyder coordinates. Discrete spatial spectra with exact Lorentz symmetry, tested against LHAASO, MICROSCOPE/LLR (soccer ball) and the soft theorem | Whether a fourth set D exists | FAIL for per-constituent composition; INCONCLUSIVE with N-dependent deformation |

**Deferred** (lower decisive value):
- Edgeless sources for E (R2-2 covers E more generally).
- The RG stability of C's tuning count.
- The FS supercharge rule as a gravity coupling (a bridge for B6 and C1).

---

## 4. Caveats

- **Same family, unrefereed.** Everything here is the same model family. The synthesis itself, remarks 1–2 and the set construction are not refereed.
- **Q1.** Q1's referee (CWC, 11:49Z) is used throughout. Its FAIL is proved only for fixed Poisson Born weights with a traced-out or self-evolving substrate. The full class is INCONCLUSIVE, leaning FAIL. R2-2 does not depend on Q1; it stands on its own hypotheses.
- **Downgraded readings.** O1 and O4 are NOT CONFIRMED. Their headline necessities are SUGGESTED, and the list above uses only their refereed sub-results.
- **The sets are not exhaustive.** A, B and C are minimal among the routes the refereed record leaves open. The record does not prove that no other set exists: the referees list non-gauge exits and holographic, relational and non-commutative constructions (B referee; O2 referee §7).
- **"Minimal" means fewest axiom texts touched for the observations used.** By that count A touches all four texts plus one primitive; B touches three (Lattice, Admissibility and Record; Qubit is unchanged) plus a gravity primitive or tunings; and C touches none but tunes.
