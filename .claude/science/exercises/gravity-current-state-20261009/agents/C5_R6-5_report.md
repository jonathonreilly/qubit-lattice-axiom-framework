# C5 R6-5: set C's dimension-3 price. The CPT-odd terms b₀ and (k_AF)₀ allowed by the axioms' proper-only rotations

**Probe.** R6-5 of campaign C5, round 6. The pre-registration is at `TESTS.md:3181-3213` (line numbers as of 14:43Z; the file is being appended while this runs).
- Run by Claude Opus 5.5, the same family as the other C5 workers, on 2026-10-12 from 14:20Z to about 14:55Z.
- **Not refereed.** No codex referee has seen this report.
- No repository file was edited.

**Labels.**
- **proved**: an argument given here, complete under its stated hypotheses.
- **checked**: a computation that ran here (scripts and outputs below).
- **comparator**: a published result, cited and not re-derived. Where the source was fetched, that is said; otherwise it is RECALLED.
- **suggested**: argued, not proved.
- **reading**: an interpretation.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `S/` = scratch `C5/R6-5/` (scripts and outputs are in `S/scripts/`; the fetched data-table PDF and its text extraction are in `S/downloads_kr/`, untrusted and never executed)

---

## 0. In plain words

The axioms allow only proper rotations (`AX:37-38,57-58`). That lets the law prefer one handedness. Two handed, CPT-odd terms of lowest dimension follow, and they behave very differently.

1. **b₀, an energy offset between left- and right-handed fermions. It costs a tuning of about 43–49 decades.**
   - An explicit grid law in the class gives b₀ at whatever size its handed coupling has.
   - The handed couplings of different particle species feed into each other at one loop with an O(1) coefficient.
   - So with nothing to forbid it, b₀ sits near the grid scale. Observation requires it to be below 1e-26 to 1e-30 GeV.
   - That is one cancellation per bounded species, each to about 1 part in 10⁴⁵. Of the tunings priced so far in set C, these are the largest.
2. **(k_AF)₀, a handed "twist" term for light. No tuning is needed.**
   - It is not forbidden by symmetry. It is forbidden by stability.
   - If it were present, light of one handedness at long wavelengths would grow without bound, so the vacuum would not be the lowest-energy state.
   - In any equilibrium state, charged matter on a grid cannot produce the term. That is a known theorem: a lattice system in equilibrium carries no net current (Bloch's theorem). It is confirmed here numerically for the explicit law. The naive "anomaly" value is beaten by more than 10⁴, and the residual shrinks as the grid is refined.
   - A larger cousin of this term, one with two more derivatives, *is* generated, and nothing protects it. It affects only high-energy light, and costs roughly 10 decades if left to tuning (suggested).
3. **The cheapest symmetry fix is CPT in the law.** It removes all of these terms at once.
   - It needs spatial inversion added to the Lattice and Admissibility texts, and a time-reversing (antiunitary) symmetry of the real-time law.
   - So the law itself cannot carry an irreversible arrow, and the records' arrow must sit in the state.
   - CPT is compatible with chiral matter in the continuum. A chiral *lattice* law that keeps exact CPT is not exhibited here.

---

## 1. Hypotheses and class

**The class (fixed by `TESTS.md:3188-3191`).**
- Z³ × ℝ, with a Hermitian, finite-range, gauge-invariant Hamiltonian lattice law.
- Covariant under lattice translations and the 24 proper cubic rotations (O).
- No inversion and no antiunitary symmetry is required. A law may have them; the class does not demand them.
- Matter: naive, staggered or Wilson-type fermions coupled by Peierls phases (compact coupling); then chiral content.
- Sets B and B′ are excluded. There, V = 0 and Zariski density forbid invariant vectors (`TESTS.md:3191`, citing `:2379` and the Zariski-density item at `:2654`). Also, in Euclidean Z⁴ the total inversion x → −x lies in B4⁺, so CPT is automatic there (§5).

**Additional hypotheses, used only where named.**
- **(H-vac)** The physical vacuum is a ground state or a Gibbs state of the law.
- **(H-γ)** The photon is a long-lived excitation of that vacuum, described at small |q| by a local effective theory with positive Maxwell coefficients.
- **(H-gap)** All charged matter is gapped. This holds for the SM vacuum: the lightest charged particle is the electron.

**Outside realizations not covered.** These are listed before any title.
- non-equilibrium states (for example a primordial chiral imbalance μ₅);
- U(1) charges that are not sums of local densities (non-on-site symmetries of the kind used for some chiral lattice fermions);
- gapless charged matter;
- non-Hamiltonian (dissipative or record-producing) laws, for the stability argument;
- composite or strongly coupled matter beyond the free-fermion checks. The Bloch-type argument covers interacting finite-range laws; the numerics do not.

---

## 2. Prior art (each counted once)

| Source | What it gives | Used as |
|---|---|---|
| F2 referee, `TESTS.md:1440`; `P/agents/C4_F2_referee.md:9` | Proper O allows b₀ and (k_AF)₀. Both are C-even and T-even; only the chosen action's parity forbids them | Starting point; confirmed by explicit intertwiners (§3.1) |
| O1, `P/agents/C5_O1_report.md:92,104` (counts V = 1, S2 = 2 for the axioms' group) and `:240-246` (price O1.4, SUGGESTED) | Vector terms need V₁ ≠ 0, and the axioms' group has V = 1. Natural size argued only | The axioms' group allows exactly one invariant vector (time), so b₀ and (k_AF)₀ but no spatial b_j, (k_AF)_j |
| O1 referee, `P/agents/C5_O1_referee.md:27-36,89` | H2 "natural size" is not a definition; the k_AF bound is only partially verified and non-load-bearing | Natural sizes here are the explicit law's computed numbers, not H2. The bound is now verified (§4) |
| R2-4 referee, `P/agents/C5_R2-4_referee.md:44-63` | Lemma K: positivity gives an antiunitary K. No class-wide chiral no-go; Nielsen–Ninomiya is free and exact-chiral only | §5: law-level CPT and chiral content |
| `docs/CPT_EXACT_NOTE.md` (free staggered Θ_H = PK); `docs/PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md:10-30` (CPT-odd proxy vanishes on the free staggered lift; audited_conditional) | Exact antiunitary symmetry *of the free parity-symmetric staggered action* | This is "the chosen action's parity" in the F2 referee's sense. It does not cover the class |
| `docs/DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md:22,82-83` | The axioms name no improper element; every P statement is conditional | Agrees with the class definition |
| `docs/ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md:33-60` | Covariant, strictly positive *handed* Admissibility rules exist in every reading; the soldered lowest handed term is a lattice curl | Reading: handedness is native to the axioms' own rule class, so a P-odd law is not exotic in set C |
| `docs/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md:148-205` | A two-node Weyl carrier with nodes split along z has a nonzero Hall (spatial CS-vector) term, a gapped photon, and only model-changing escapes | The *spatial* analogue. It breaks cubic O, so it is outside this class (V = 1 allows no spatial vector). Its q = 0, ω-linear Hall response is not limited by Bloch's theorem; the timelike static term is (§3.3) |
| `docs/ARROW_CPT_ORIENTATION_DO_NOT_SOURCE_CP_ODD_ACTION_COEFFICIENTS_NO_GO_NOTE_2026-06-08.md:24-60` | CP-odd coefficients are free action coefficients, not selected by arrow, CPT or orientation routes; the record arrow enters through boundary data | Consistent with b₀ being a free coefficient. Supports "the arrow in boundary or state data" (§5) |

No repository hit was found for "Bloch theorem" combined with "Chern–Simons", "chiral magnetic" or "k_AF". `docs/` contains no b₀ natural-size or tuning computation.

---

## 3. Results

### 3.1 (a) An explicit law with b₀ ≠ 0 (checked)

**The law.** One four-component fermion per site, nearest-neighbour Peierls hopping, and an on-site term:

  h(k) = Σ_j α_j sin k_j + β(m + rΣ_j(1 − cos k_j)) + b γ⁵.

**Symmetry (checked, `S/scripts/r65_symmetry.out:1-5`).**
- It is covariant under all 24 proper rotations, with the spinor lift; the maximum error is 4.4e-15.
- The P, T and C maps were *solved for* on the b = 0 law (each solution space has dimension 1). The b·γ⁵ term is **P-odd, T-even, C-even**, and hence CPT-odd.
- A direct one-particle CPT intertwiner, U h(−k) U† = −h(k), exists and maps b γ⁵ to −b γ⁵ (`r65_symmetry.out:20`).
- This confirms the F2 referee's correction: C, T and shifts do not forbid the term (`TESTS.md:1440`).

**Low-energy content (checked, `S/scripts/r65_cme.out:1-5`).**
- The lattice dispersion is exactly E = √(M(p)² + (sin p ∓ b)²), to an error of 1e-16. That is the SME b₀ form, E² = m² + (|p| ∓ b₀)², with b₀ = b.
- The doublers are gapped at 2.3/a and above.
- With m = 0 the Dirac point splits into right- and left-handed Weyl nodes at energies ±b: the Weyl-node energy offset asked for in the brief.

**Qubit-native form (checked, `S/scripts/r65_symmetry.out:9-18`, `r65_staggered.out`).**
- Take the two-component naive Weyl law σ·sin k + t₃ cos k₁ cos k₂ cos k₃, with a body-diagonal scalar hop. It is covariant under proper O (error 1.2e-15).
- It puts all 4 right-handed nodes at +t₃ and all 4 left-handed nodes at −t₃: a taste-singlet b₀ = t₃.
- Controls: Σ cos k_j and Σ cos cos give a taste-singlet offset of 0.
- Kawamoto–Smit spin diagonalization maps this law exactly onto two copies of a one-mode-per-site (staggered) law. The deviation is 0, and the spectra agree to 5.8e-15 on L = 6.
- In that staggered law the body-diagonal hop has amplitude i·t₃/8 with sign phases. So b₀ ≠ 0 needs only one fermion mode, i.e. one qubit, per site.
- Not checked: the staggered form's covariance, which uses the standard staggered sign/taste action.

**Generation across species (checked, `r65_cme.out:6-8`).**
- For the filled Dirac sea of this law, χ₅ = d⟨ψ†γ⁵ψ⟩/db = −0.507 a⁻² per site, converged between N = 24 and N = 40.
- Add an on-site contact G(ψ†γ⁵ψ)(χ†γ⁵χ). It is O-invariant, P-even, gauge-invariant and Hermitian. A species χ with **no** tree-level P-odd term then acquires b₀^χ = G χ₅ b^ψ at one loop (Hartree).
- With G = g²a², that is −0.5 g² b^ψ: no suppression beyond the coupling.
- So once handedness is anywhere in the law, every species' b₀ is generated at O(coupling) × (lattice scale). No symmetry of the class stops it (proved: the class contains no P, CP, PT or CPT, and those are the only discrete combinations that flip b₀).

### 3.2 (c) Bounds and the b₀ tuning (bounds fetched; arithmetic checked)

**Source.** Kostelecký–Russell Data Tables, January 2026 update (arXiv:0801.0287v19), fetched and text-extracted to `S/downloads_kr/`.

| Coefficient | Electron | Proton | Neutron | Source in the tables |
|---|---|---|---|---|
| b̃_T, Sun-centred frame | ~1e-26 GeV. Heckel 2008 bounds the combination ½(b̃_T + …) = (0.9 ± 2.2)e-27 | ~1e-26 | ~1e-27 (Basson et al. 2025) | Summary S2; D6 [52]; D15 [91] |
| b̃_⊥ (spatial) | (−0.9 ± 1.4)e-31 (Heckel et al., PRD 78, 092006, 2008) | < 7.6e-33 (He/Xe, Stadnik–Flambaum 2015) | < 1.3e-33 (Allmendinger et al.) | D6 [52]; D10 [108]; D15 [124] |
| (k_AF), CMB | < 7.4e-45 GeV (Caloni et al., JCAP 2023). The isotropic k^(3)_(V)00 = (7.32 ± 2.94)e-45 GeV (Minami–Komatsu 2020 / Nilsson–Le Poncin-Lafitte 2024) is a ~2.5σ birefringence hint | | | D19 [142]–[144] |

**Boost route.** Set C has a preferred frame. If that frame is the CMB frame (an assumption), b₀ enters the spatial b̃_J through β = 1.234e-3. That gives:
- b₀^e ≲ 1.1e-28 GeV;
- b₀^p ≲ 6.2e-30 GeV;
- b₀^n ≲ 1.1e-30 GeV.

These are orders of magnitude only: SME projection factors and the d, g, H admixtures in b̃ were not computed.

**Natural sizes, from the explicit law with a = ℓ_P.** These are model numbers in lattice units, not a universal natural-size theorem.
- Tree level, b = 0.1/a: 1.2e18 GeV.
- One-loop induced, G = 0.1a², b = 0.1/a: 6.2e16 GeV.

**Tuning (checked, `r65_bounds.out`).**
- **43–46 decades** against the Sun-frame b̃_T bounds.
- **45–49 decades** by the boost route.

The tuning is per independently bounded species (e, p, n ↔ e, u, d axial directions): **≥ 3 conditions** (a reading; the flavour-matrix count is not done).
- b₀ is a dimension-3 (relevant) coupling, so the sensitivity is linear in the cutoff, not logarithmic. Compare F2's speed tuning of about 17 decades (`TESTS.md:1439`).
- The cancellation is a joint condition, because χ₅ mixes species at O(g²) (§3.1).

### 3.3 (b) (k_AF)₀: generated? (proved / checked / comparator)

**Lemma N: a bare term in a noncompact photon sector makes H unbounded below** (proved; checked, `r65_cs_photon.out`).
- *The term.* Average the cup-product Chern–Simons term A ∪ dA over the 24 proper rotations. The result is M(q) = Π_l cos(q_l/2) · ε_ijk 2i sin(q_j/2). Checked:
  - Hermitian (error 0);
  - gauge-invariant on both sides (1.2e-16);
  - O-covariant (2.2e-16);
  - **P-odd**;
  - equal to i ε_ijk q_j at small q.

  So locality, gauge invariance and hermiticity *allow* it in the noncompact theory.
- *The instability.* With it, the photon potential ½|curl A|² − k A·M A has eigenvalue ½|q|(|q| − 2|k|) on one helicity. That eigenvalue is negative for |q| < 2|k| for every k ≠ 0 (checked for k = 1e-3, 1e-2, 1e-1).
- Since H = ½E² + V, H is not bounded below. This is the lattice form of the Carroll–Field–Jackiw timelike instability, ω² = q² − 2kλq (comparator: CFJ 1990 and Kostelecký–Lehnert 2001, RECALLED).

**Compact U(1)** (suggested).
- The A·B density changes under a gauge transformation by ∂(λB), so δ∫A·B = −∫λ ∇·B.
- On the compact lattice, ∇·B = 2π × the monopole density. The term is therefore not gauge-invariant once monopoles are present.
- Monopole-free (modified-Villain) formulations would be needed to write it at all (comparator, RECALLED: Jacobson–Sulejmanpasic 2023, for 2+1D CS).
- Quantum-link (qubit) gauge fields have no A operator.

**Lemma S: stability** (proved at the EFT level, under H-vac and H-γ).
- Suppose the IR photon Lagrangian about a translation- and O-invariant vacuum is ½(εE² − B²/μ) + k A·B + higher derivatives, with ε, μ > 0.
- Then the helicity λ = sgn k has ε ω² = q²/μ − 2|k| q < 0 for 0 < q < 2|k|μ.
- In a ground state, the excitation energies (the spectrum of the GNS Hamiltonian) are real and nonnegative, which contradicts ω² < 0. Hence **k = 0** for the *total* IR coefficient, bare plus induced, compact or emergent. For Gibbs states the analogous step is suggested only: an exponentially growing mode contradicts stationarity and the boundedness of correlations of bounded observables.
- Under Qubit (finite site algebras), a Hermitian finite-range H is automatically bounded below per site, so H-vac's ground state exists. H-γ is the observational input.
- *Scope.* An exactly-zero statement in infinite volume. A k of order H₀ would make only super-Hubble modes unstable.

**Lemma B: no static induced term in equilibrium** (comparator; theorem abstract fetched).
- Watanabe, J. Stat. Phys. 177, 717 (2019), arXiv:1904.02700: for any Hamiltonian with finite-range terms and a U(1) charge, the current averaged over the whole system vanishes in the ground state and at thermal equilibrium (as O(1/L) for periodic boundary conditions).
- A static uniform B with an induced (k_AF)₀ would carry a bulk current 2kB. Hence the static induced coefficient is 0.
- Under H-gap the response is analytic in (ω, q). So the q-linear, ω⁰ coefficient seen by on-shell photons equals the static one: **(k_AF)₀^ind = 0**.
- Vazifeh–Franz (PRL 111, 027201, 2013; abstract fetched) found the same on a lattice Weyl model: no equilibrium CME in the semimetal or the insulator phase.

**Lattice check of Lemma B for the explicit law** (checked, `r65_cme2.out:1-7`, `r65_cme.out:12-23`).
- The Kubo antisymmetric response is k = i(Π^xy − Π^yx)/(4q), for q ∥ z and (ω, q) below the gap.
- Static limit, three-point q-extrapolation, N = 48:
  - on-site b = 0.1: k_static = −2.2e-8;
  - P-odd hopping c₅ = 0.1: −1.6e-8;
  - mixed: −4.0e-8.
- The naive anomaly value b_eff/(4π²) is 2.5e-3, 7.6e-3 and −1.3e-3 respectively. The ratios are **≤ 3e-5** at N = 48, and fall from N = 32 to N = 48 (the integrand is smooth because the system is gapped).
- At b = 0 the result is identically zero (1e-19).
- *Calibration of the code.* Same vertices and normalization: gapped slices of a Weyl test model give slice Chern number −1.0000 (`r65_ahe_slices.out`). The 3D AHE gives 0.00957 against Δk/(4π²) = 0.01015 (`r65_ahe_calib.out`). The 6% gap comes from unconverged near-node slices.
- The q = 0, imaginary-frequency line in `r65_cme2.out:13-14` is ill-conditioned (a grid point sits near a node) and is superseded by the Berry-form check.

**The protection does not reach dimension 5** (checked numbers; the price is suggested).
- Away from the static point, k(ω, q) ≈ k_ω ω² + k_q q² (`r65_cme2.out:8-12`). For m = 0.3/a and b = 0.1/a: k_ω = 2.5e-3 and k_q = −2.15e-3, so **the on-shell (ω = q) coefficient is ≈ 0.14 k_ω ≈ 3e-4**. That is not zero. The value was confirmed directly at ω = q: k/q² = 3.0e-4 and 3.2e-4.
- In a Lorentz-covariant continuum the odd form factor at linear order in b depends only on p², so it would vanish on shell.
- The surviving part is O(b³/m⁴) plus lattice artefacts. The two are not separated here: the m = 0.2 and 0.15 rows are not converged at N = 48.
- This is the d = 5 CPT-odd, helicity-dependent (birefringent) photon term, isotropic k^(5)_(V)00. P and CPT forbid it; stability and Bloch's theorem do not.
- Estimate: e² × 3e-4 × ℓ_P ≈ 2.3e-24 GeV⁻¹, against the table's isotropic d = 5 sensitivity of about 1e-34 GeV⁻¹ (S3). That is **≈ 10 decades** (suggested: toy natural size; √(4π)-type normalization factors not matched).
- Condensed-matter comparator (RECALLED): crystals of the chiral cubic classes 23 and 432 (e.g. NaClO₃) are isotropically optically active, with rotatory power ∝ ω² and none at ω → 0. That is the same pattern: dimension 3 absent in equilibrium, dimension 5 present.

### 3.4 (d) The cheapest symmetry price (proved for the forbidding; suggested for compatibility)

b₀ and (k_AF)₀ are C-even, P-odd and T-even. The discrete operations that flip them are P, CP, PT and CPT.

| Symmetry | Forbids b₀, (k_AF)₀? | Compatible with chiral SM content? | Verdict |
|---|---|---|---|
| P (inversion) | yes | no: the P-image of SM content is absent | fails |
| P′ = P ∘ (SM ↔ mirror) | no: it relates b₀^SM = −b₀^mirror | needs a mirror sector | fails |
| CP | yes | yes, if CKM CP violation is spontaneous (R2-4 Π-CP, `C5_R2-4_referee.md:50-53`). After the breaking, b₀ needs a further CPT-odd spurion (e.g. a law-level arrow) to regenerate (suggested spurion count) | possible, with a physics price (Nelson–Barr-type sector) |
| **CPT** | yes, and every CPT-odd SME term, including the d = 5 photon term of §3.3 | continuum: yes (CPT theorem). Lattice, vector-like: yes; checked one-particle CPT intertwiners for the Wilson–Dirac and naive-Weyl laws (`r65_symmetry.out:20-23`), and the repo's exact Θ_H = PK for free staggered (`docs/CPT_EXACT_NOTE.md`). Lattice, chiral: **not established**. Lattice CP in Ginsparg–Wilson chiral gauge theories is known to be problematic (comparator, RECALLED: Fujikawa–Ishibashi–Suzuki 2002). SMG constructions are not checked | **SYMMETRY-PRICED**, conditional (below) |

**Axiom text that law-level CPT touches** (the price is named, not adopted).
- **Lattice** `AX:37-38`: "proper cubic rotations about each site" would become the full cubic group, i.e. inversion about each site added.
- **Admissibility** `AX:57-58`: "covariant under lattice translations and proper cubic rotations" would add inversion, plus covariance of the downstream real-time law under an antiunitary Θ = inversion ∘ conjugation (CPT). The distribution itself is real, so the antiunitary part constrains the downstream law, which the Qualification (`AX:88-91`) already routes to a bridge.
- **Record** `AX:77-80`, conditionally: exact CPT needs Θ T_t Θ⁻¹ = T_{−t}, which needs an *invertible* (reversible) law. A law whose record formation is irreversible at law level (a semigroup with no inverse) cannot carry it (proved; elementary).
  - So "records form … permanent" must be realized with the arrow in the state or boundary data. That is the R2-5 issue, now also present in set C (`TESTS.md:2737-2740`).
  - The 06-08 no-go note's reading that the arrow enters through boundary data (`docs/ARROW_CPT_…_NO_GO_NOTE_2026-06-08.md:24-25`) points the same way.

**Where CPT comes free.** In Euclidean Z⁴ (sets B and B′), CPT corresponds to x → −x, which lies in B4⁺, so it is automatic. That is consistent with the exclusion of B and B′ in `TESTS.md:3191`.

---

## 4. Against the FIXED readings (`TESTS.md:3204-3209`)

| Operator | Reading | Basis | Scope |
|---|---|---|---|
| **b₀** | **TUNING-PRICED** | An explicit law in the class: b₀ = b exactly in the dispersion. One-loop mixing χ₅ = −0.507 a⁻², so every species acquires b₀ at O(g²) × the lattice scale. Computed natural size 6e16–1.2e18 GeV (a = ℓ_P). Verified bounds: b̃_T ~1e-26/1e-26/1e-27 GeV (e/p/n); boost route 1e-28 to 1e-30 GeV (CMB-frame assumption). **Tuning 43–49 decades, ≥ 3 joint conditions** | Natural size is the explicit law's, with O(0.1–1) lattice-unit couplings (not a universal theorem; cf. `C5_O1_referee.md:27-36`). Boost projections are order-of-magnitude |
| **(k_AF)₀** | **PROTECTED**, with the protection named: vacuum stability plus Bloch's theorem, not symmetry | Lemma S (proved, EFT level): any nonzero total IR (k_AF)₀ makes the photon vacuum unstable. Lemma N (proved and checked): the bare noncompact term is allowed by locality, gauge invariance and hermiticity but makes H unbounded below. Lemma B (comparator, theorem abstract fetched) plus the lattice check (ratio ≤ 3e-5, decreasing): the induced static term is 0 in equilibrium, hence on shell for gapped charged matter | Needs H-vac, H-γ and H-gap beyond the literal "gauge invariance, locality, hermiticity". Qubit supplies boundedness below; observation supplies H-γ. Open: non-on-site U(1) charges, non-equilibrium states, dissipative laws |
| **both, via law-level CPT** | **SYMMETRY-PRICED, conditional** | CPT forbids both, and the d = 5 term. Compatible with chiral content in the continuum and with vector-like lattice tastes (checked). Text touched: Lattice `AX:37-38`, Admissibility `AX:57-58`, and (if formation is a law-level arrow) Record `AX:77-80` | Chiral *lattice* realization with exact CPT not established. So "compatible with chiral content" holds at the continuum-EFT level only |

**Against the expectation (`TESTS.md:3211-3213`).**
- **b₀: TUNING-PRICED by tens of decades.** Met: 43–49 decades.
- **(k_AF)₀: PROTECTED or suppressed in equilibrium.** Met and sharpened. It is exactly zero in any stable equilibrium vacuum, not merely suppressed, and no tuning is needed. The registered "OPEN risk" lands somewhere else: the d = 5 CPT-odd photon term *is* generated and unprotected (≈ 10 decades, suggested).
- **SYMMETRY-PRICED via law-level CPT at a Lattice-text cost.** Met, but the cost is larger than registered:
  - Lattice and Admissibility text;
  - a reversible downstream law, so the record arrow sits in the state (a Record-reading cost shared with set B's R2-5);
  - an unbuilt CPT-exact chiral lattice law.

**Set C's price after R6-5** (reading).
- It grows by ≥ 3 b₀ tunings of about 45 decades each, plus (suggested) one d = 5 CPT-odd photon tuning of about 10 decades.
- Or it pays law-level CPT once, which removes all of these.
- (k_AF)₀ adds nothing.

**Strong words checked.**
- "exactly": used only for Lemma S, Lemma B in an equilibrium ground or Gibbs state, and the dispersion identity.
- "every species": the one-loop mixing is shown for an on-site contact coupling only.
- "cheapest": a reading among the four listed symmetries, not a theorem over all mechanisms. Sequestering, or a heavy P-odd sector coupled only irrelevantly, is not examined.

---

## 5. What would change these verdicts

- **A chiral lattice law with exact CPT** (GW/overlap in Hamiltonian form, or a mirror-SMG law) would turn the SYMMETRY-PRICED reading unconditional. A proof that none exists would leave tuning as the only route.
- **Non-on-site U(1) charges**, as used to put a single Weyl fermion on a Hamiltonian lattice, may evade Lemma B's hypotheses. Lemma S would still apply if H-vac and H-γ hold.
- **Referee requests:**
  - check Lemma S's EFT step (k = 0 exactly versus |k| ≲ H₀);
  - check the χ₅ mixing sign and size;
  - check the on-shell d = 5 extraction at smaller m with larger N, and its normalization to k^(5)_(V)00;
  - check the CMB-frame boost projection of b₀ into b̃_J.
- **The isotropic CMB birefringence hint** (2.5σ, D19 [142]) cannot be a constant law-level (k_AF)₀ in set C (Lemma S, for the photon vacuum). If confirmed, it would need state content, such as a slowly varying axion-like field (reading).

---

## 6. Files

All under `S/` = `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/R6-5/`.

**Scripts and outputs (`S/scripts/`).**
- `r65_symmetry.py/.out`: O covariance; P, T, C and CPT intertwiners; naive-Weyl node offsets.
- `r65_staggered.py/.out`: one-mode-per-site form.
- `r65_cme.py/.out`: dispersion; χ₅ mixing; Kubo k(ω, q) with commensurate q.
- `r65_cme2.py/.out`: static three-point extrapolation for three P-odd terms; on-shell d = 5 coefficient. Its §3 line is superseded.
- `r65_ahe_calib.py/.out` and `r65_ahe_slices.py/.out`: vertex and normalization calibration.
- `r65_cs_photon.py/.out`: bare lattice CS term and the instability.
- `r65_bounds.py/.out`: bounds and tuning arithmetic.

**Downloads (untrusted, not executed).**
- `S/downloads_kr/kr_tables.pdf` and `.txt`: Kostelecký–Russell Data Tables, January 2026 (arXiv:0801.0287v19). Text extracted with PyMuPDF run from `S/scripts` with `-I`.
- `summary_p23_28.txt`: the summary tables.

**External sources.**
- [Data Tables](https://arxiv.org/abs/0801.0287) (fetched)
- [Watanabe 2019](https://arxiv.org/abs/1904.02700) (abstract fetched)
- [Vazifeh–Franz 2013](https://arxiv.org/abs/1303.5784) (abstract via search)
- Heckel et al. 2008, [arXiv:0808.2673](https://arxiv.org/abs/0808.2673) (via the tables)
- Minami–Komatsu 2020, [arXiv:2011.11254](https://arxiv.org/abs/2011.11254) (via the tables)
