# C5 R12-5: graviton production outside X1 (non-regular / strong-coupling / emergent-constraint phases of qubit N-type models)

**Worker.** Claude Opus 5.5 (same family as every C5 worker and the supervisor). 2026-10-12, 19:30Z to about 20:05Z. **Unrefereed.** No repository file was edited. Scripts and outputs: `scratchpad/C5/R12-5/scripts/` (s1, s1b, s1c, s2, s2b, s3; each run < 5 min on 2 threads).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`. `N0924o` = `docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md`. `N0924s` = `docs/DYNAMICS_CLAUSE_A_SOFT_VECTOR_CONSTRAINT_AND_SLOT_FIELDS_GENERATE_THE_LANDED_TENSOR_FIELD_S_CURVATURE_MOVES_AT_TWELFTH_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md`. `vR11-2` = `P/agents/C5_R11-2_referee_verdict.md`. `R11-2` = `P/agents/C5_R11-2_report.md`. `TESTS` = `P/TESTS.md` (R12-5 registration at `TESTS:4463-4476`).

**Labels.** proved = derivation here (unrefereed); checked = numerics here; suggested = argument; reading = interpretation; comparator = literature (V = verified on the web in this run, abstract or full text as stated; RECALLED otherwise).

---

## 0. Plain words

- **The question.** R11-2 (refereed) showed that a qubit model with exact, commuting N-type constraints, whose dynamics is a smooth low-harmonic function of the clock variables expanded around small fields, gives gravitons with ω = O(k³), not light-like. Can a strongly coupled phase, or constraints imposed by energy penalties instead of exactly, do better?
- **(a) Which X1 assumption breaks.** Two kinds of model are outside X1, for different reasons:
  - **Gu–Wen's own N-type lattice model** (the literature's only candidate) breaks the *exactness* assumption. Its constraints are energy penalties that do not commute with the dynamics (V). It also sits at U ~ J ~ g, with no small parameter.
  - **A strongly coupled phase of an exact model** cannot break exactness. Lemma A_c holds at any coupling. It breaks two other assumptions:
    - the "small-field linearization" assumption, by definition;
    - the "lifted" assumption. The effective dynamics contains high harmonics, or arbitrarily long words, whose integer syndromes are multiples of N (aliasing).
  - **Unblocked qubits (N = 2)** violate lifting outright (checked: explicit aliased invariant operators). But on the E side the aliasing found on small blocks touches only the trace, which the TT waves do not see. The h side has one aliased family (s1c).
- **New result (proved; checked numerically).** A non-invariant "weak" kinetic term can only contribute if the constraint it violates is itself fuzzy.
  - Quantitatively, |⟨X^r⟩| ≤ 2√(2σ)/|1 − ω^c|, where σ is the local constraint-violation of the state.
  - Gu–Wen's linear-graviton argument needs both things at once: such weak cosines at full strength, and a sharply "frozen" scalar constraint. The inequality says these are incompatible.
  - The in-between regime, where the constraint is fuzzy at the scale of one quantum, is the energy-penalty Gaussian theory. That theory is unbounded below at every penalty strength: a conformal-mode-type instability, prior art in N0914, re-checked here at generic momenta.
- **The one-constraint cases (including normalizable rotor sectors).** If either constraint is exact on compact lifted variables, one of the two "dressings" is killed, so the graviton goes at best like k². GW170817 excludes that.
- **What is left.** A light-like N-type graviton from qubits must be *genuinely non-Gaussian*. Both constraints must be energetic and fuzzy at their quantum scale, yet the compact model must avoid the Gaussian instability. No method controls that regime, and no one has computed it, Gu–Wen included.
- **(b) Numerics.** A quantum many-body dispersion is not computable here: the smallest dispersion-resolving exact qubit sector is 2⁵⁸-dimensional (checked). What I did compute:
  - exact Z_N algebra of the qubit code;
  - Gaussian spectra of energetic models;
  - the new inequality, on random and ground states.
- **(c) Literature.** I found no qubit model with a numerically demonstrated linear, gapless, two-polarization spin-2 mode without partners.
  - Gu–Wen say plainly that their linear N-type result is unreliable and that "numerical calculations are needed" (V).
  - Linear spin-2 modes in rank-2 U(1) liquids come with ±1/0 partners (scalar charge).
- **Reading: OPEN.** Not PRODUCED. Not EXCLUDED: no refereed extension of X1 exists yet. I send two candidates to the referee (§6).

---

## 1. Hypotheses, classes, excluded realizations

- **X1** (refereed, `vR11-2:15,17`):
  - **(H-ex)** an exact constraint sector, invariant under H;
  - **(H-lf)** locally finite, pairwise-commuting, finite-slot constraint generators;
  - **(H-reg)** the averaged sector Hamiltonian has a summable character expansion with moments (`N0914:239-252`);
  - **(H-lift)** its characters lift: modular zero syndrome implies integer zero syndrome, guaranteed if N > 36M (`N0914:109-115`, `:218-223`);
  - **(H-lin)** a nonsingular smooth canonical small-field linearization governs the low-energy spectrum (`N0914:197-216`).
  - **Conclusion:** every small-field frequency is O(k³).
- **Classes examined here:**
  - **Q-ex:** exact sector, any coupling, any N.
  - **Q-en-p:** energetic penalties with a gap Δ ≫ the local dynamic norm J.
  - **Q-en-s:** energetic penalties with U ~ J ~ g, the Gu–Wen regime.
  - **Q-2:** unblocked qubits, N = 2.
  - **Q-1ex:** one constraint exact, the other energetic. This includes the normalizable rotor versions of R11-2's classes A and B.
- **Excluded, as registered:** nonlinear gravity, matter, Λ.

## 2. Prior art (each counted once)

1. **R11-2 and its referee:**
   - X1, Lemma A_c, the dressing law ω ∝ k^{3−n}, and classes A and B (`R11-2:135-176`; `vR11-2:7-9,15,17`);
   - O1–O6 (`R11-2:45-51`).
2. **N0914:**
   - the integer clock complex and finite-clock H (`:85-184`);
   - the regular compact bound (`:186-216`);
   - aliasing and high-harmonic escapes (`:218-223`);
   - "every surviving [returning] word commutes with the constraints" (`:117-124`);
   - finite penalties give det K = −J²/2 < 0 and a Jordan chain (`:260-278`);
   - the N-type strong-coupling gap is uncontrolled (`:372-376`).
3. **N0924o:**
   - the exact lattice N-type comparator, ω² = 4Jg Σ sin²(k_i/2) (`:73`);
   - one tested cosine replacement fails scalar invariance (`:105-108`);
   - penalties cannot make the comparator bounded below (`:116`);
   - noncompact exact constraints can be non-normalizable (`:143`).
4. **N0924s:**
   - a soft (energetic) vector constraint generates S-curvature moves at order 12, with coefficient (111150053/31850496) h¹²/U¹¹ (`:46`);
   - the selected cosine comparator gives ω² = 2Jgλ = O(k⁴), so quadratic dispersion (`:113`);
   - "the supplied E² term does not preserve the scalar stabilizer" (`:124`).

   This is the closest prior art to my energetic-class analysis.
5. **Lane R, R2:**
   - the strong-class counts 5/4/3/2 with dispersions k, k, k², k³;
   - scalar charge is linear only with partners;
   - breaking the redundancy brings back P0's μ_E and μ_T2 (`TESTS:752-756`; `P/agents/R2_referee.md:5-8,16`).
6. **R0's literature table** (`P/agents/R0_report.md:131,157-158`), and probe 13: "weak invariance adds nothing in lifted clock encodings" (`R0_report.md:99`; full text unlanded, not read).
7. **Gu–Wen, Xu, Pretko** etc. are in §7.

## 3. Probe (a): which X1 hypothesis a strong-coupling phase violates

| Model / phase | H-ex | H-lf | H-reg | H-lift | H-lin |
|---|---|---|---|---|---|
| Gu–Wen N-type lattice model (0907.1203 §VII; V, read via ar5iv summary) | **violated:** constraints are penalties with [H_U, H_J] ≠ 0 and [H_U, H_g] ≠ 0 (V) | n/a (not exact) | holds for the bare H | bare H_J and H_g are low-harmonic cosines (V) | assumed for ±2 ("1/n_G ≪ δφ ≪ 1", V); fails for helicity 0/±1, "an uncontrolled approximation" (V) |
| Exact model, lifted bare H, strong-coupling liquid (Q-ex) | holds (by class) | holds | holds for the bare H (finite range ⇒ finite character sum); may fail for the *effective* H at criticality | can fail for the **effective** dynamics: order-n words have exponents up to nM, so lifting needs N > 36nM (`N0914:112-115`). An infinite-order resummation has unbounded n | **fails by definition** of strong coupling: no small-field point |
| Exact model, generic local terms (projectors etc.) | holds | holds | holds | **fails generically.** A generic local operator contains all harmonics (exponents up to N/2), and after Lemma A_c averaging the *aliased* invariant characters (S r ≡ 0 mod N, S r ≠ 0) survive | fails or undefined |
| Unblocked qubits, N = 2 (Q-2) | holds if exact | holds | holds | **fails** (checked, s1) | **undefined:** Z₂ has no small field |

**Precise answer to (a) (proved, as a statement about the hypotheses).**
- In the exact class, H-ex and H-lf are microscopic and hold at every coupling. Lemma A_c is an operator identity on the sector (`vR11-2:7`), so strong coupling cannot change the microscopic symmetry class.
- What a strongly coupled phase violates is:
  - H-lin (by definition);
  - H-lift for the effective dynamics. The sector Hamiltonian may be dominated by aliased invariant characters, or by unbounded-length returning words.
- H-reg is violated only if the effective Hamiltonian has non-summable moments, i.e. at criticality.
- The Gu–Wen model additionally violates H-ex.

**Checked (s1, `s1_alias.out`).**
- G Sᵀ = 0 holds exactly as integers on 3³, 4³ and 5³ tori.
- **Code size.** The exact qubit code has logical qudits = 2V + 4 for generic (N, L). That is exactly two TT pairs per site, plus four global modes. Extra torus-dependent logicals appear in every tested case with N | L: +8 at (N, L) = (2, 4); +6 at (3, 3) and (5, 5). These are global aliasing.
- **Single-site aliased invariant E-characters** exist iff N is even (N = 2…12 tested). They are r = (N/2)(1,1,1,0,0,0), i.e. (−1)^{tr E}, with integer syndrome {−6N, N}. There are no single-site aliased h-characters.
- **On 2³ and 3³ blocks at N = 2:**
  - +2 E-characters beyond the integer count, whose zeroth moments are **trace-only** (TT-blind; s1b);
  - +1 h-character family: a corner pattern of off-diagonal slots, integer syndrome ±2, with zero zeroth moment and nonzero first moment mod 2 (s1c).
- At N = 3 there is no local aliasing on blocks up to 3³. So 36M < N is sufficient but not necessary.
- **Reading.** Qubit aliasing exists but, at small supports, supplies no TT-visible O(1) E-character. Since N = 2 has no small-field expansion, the derivative-order statement cannot even be formulated there.

## 4. New result: the frozen-constraint bound and the strong-coupling dichotomy

**Lemma DW-q (proved; checked in s3).**
- **Setting.** Z_N clocks with X^r Z^s = ω^{r·s} Z^s X^r. W = Z^s is a constraint stabilizer, and X^r is an E-character with c = r·s ≢ 0 mod N. Let ψ be any state, and σ = ⟨1 − Re W⟩_ψ.
- **Claim:** |⟨X^r⟩_ψ| ≤ 2√(2σ)/|1 − ω^c|. The same holds with E and h exchanged, using the G stabilizers.
- **Proof.**
  - W†X^rW = ω^c X^r, so (1 − ω^c)⟨X^r⟩ = ⟨ψ|X^r|ψ⟩ − ⟨Wψ|X^r|Wψ⟩.
  - For unit vectors a, b and a unitary X, |⟨a|X|a⟩ − ⟨b|X|b⟩| ≤ 2‖a − b‖.
  - ‖ψ − Wψ‖² = 2σ. ∎
- **Checks.**
  - Random and near-frozen states, N = 2, 3, 5, 8, three (r, s) pairs, 900 states each: max(|⟨X^r⟩| − bound) = 0.0.
  - Ground states of −J Re X^r − U Re W: at N = 5, ⟨X^r⟩ tracks the bound (0.142 against 0.202 at U/J = 10).
  - At N = 64 the weak stiffness survives (⟨X^r⟩ = 0.75 at U/J = 100) only because σ = 2.1e-3 is above the single-quantum threshold |1 − ω|²/8 = 1.2e-3. That is, the constraint is not sharp at its quantum scale (`s3_dw_bound.out`).

**Consequence 1: first order, frozen sectors (proved).**
- In any state with sharp S-syndrome (σ → 0), every E-character that is not S-invariant mod N has zero expectation. Its first-order (projected, PHP) contribution vanishes.
- Every single-slot E-character of any N ≥ 2 clock is non-invariant: its S-row coefficients are ±1 (neighbouring rows) and −4 (own site), and the ±1 rows are never ≡ 0 (s1: no single-slot invariant exists).
- Higher orders give only returning words, which are strongly invariant (`N0914:117-124`).

**Consequence 2: Gu–Wen's two ingredients are in tension** (proved inequality; its application to their exact Hamiltonian is a reading, because I read their §VII through a summary that lists H_J as single-component cosines 1 − cos[2πL^{aa}/n_G], V).
- Their ±2 spin wave expands those non-invariant cosines about E = 0, which requires ⟨cos⟩ ≈ 1.
- Their "quantum freeze" of the scalar sector (δπ = 0, δf = ∞, V) makes the S-syndrome sharp. That forces ⟨cos⟩ → 0 by Lemma DW-q.
- Both hold only if the S-syndrome fluctuates on the scale of one quantum (σ ≳ |1 − ω^c|²/8 ≈ (πc/n_G)²/2). That is the soft-penalty regime.

**Consequence 3: in the soft regime the Gaussian theory is unbounded** (prior art re-checked at generic k).
- With both constraints as finite penalties on H_N, the scalar kinetic determinant is −J²/2 at every U (`N0914:262-270`; `N0924o:116`).
- s2 (`s2_gauss_energetic.out`), over 200 random BZ momenta × 6 modes:
  - ω² is negative or complex at U = W = 1, 10, 100 and 10⁴ (e.g. neg 411 and cplx 338 at 10⁴);
  - min eig K < 0;
  - the TT block decouples (leakage 6e-16) and is exactly linear (exponent 1.000).
- So the energetic N-type has the linear TT at Gaussian level, sitting on an unstable (conformal-mode-type) scalar sector.

**Consequence 4: the one-exact cases cap at k²** (proved by power counting; checked as prior art, R11-2 exponents 2.000/2.001, `R11-2:166,170`).
- **Exact S on compact lifted E.** Lemma A_c, restricted to the S family, replaces every E-term on the sector by S-invariant characters. Then r = O(k) (`N0914:204-207`), so H_EE^TT = O(k²).
  - With the best weak h-side term (h:R, O(k²) on TT), ω = O(k²).
- **Exact G on compact lifted h**, symmetrically: H_hh^TT = O(k⁴), and with O(1) weak E-stiffness, ω = O(k²).
- These are R11-2's classes A and B. With the *other* constraint energetic instead of exact, they are normalizable, which removes the referee's objection (`vR11-2:9`).
- **Both one-exact Gaussians are stable, with TT exponent 2** (checked, s2b `s2b_one_exact.out`):
  - **GX** (exact G, energetic S, weak K_N on E): reduced K ≥ 0 (min eig −3e-16, the E_t null direction; K_N is PSD on ker G, `R0_report.md:99`) and B > 0 (min 0.25) over 200 random k; TT exponents 2.000, 2.000.
  - **SX** (exact S, energetic G, weak h:R): K > 0 (min 0.35) and B ≥ 0 (min −3e-15); TT exponents 2.000, 2.000.
  - The remaining non-TT modes have ω = 0 (free gauge/scalar directions). In a compact model they are gapped only by quantization; whether they stay gapped is not shown (suggested).
- **So normalizable rotor sectors are a real but insufficient escape:** at most one dressed side, hence k², which GW170817 excludes (`P/agents/C5_R6-2_report.md:169`).
- Mixed per-component assignments (R11-2's O5) were not analysed.

**The dichotomy (suggested; each leg proved or prior art; the overall framing is a reading).** For compact lifted slots with the N-type stencils:

| Regime | Outcome | Status |
|---|---|---|
| Both constraints exact | X1: O(k³) under H-lin | refereed |
| One exact | ≤ k² | proved, power counting |
| Both energetic and sharp (σ ≪ quantum²) | weak terms suppressed at first order (DW-q); perturbatively strongly invariant; X1-type | DW-q proved; perturbative part = §6 candidate |
| Both energetic and soft (σ ≳ quantum²) | Gaussian unbounded (det K < 0) unless gauge-breaking masses are added, which bring back μ_E and μ_T2 (P0 tunings, `TESTS:756`) | prior art, re-checked |
| Both energetic, neither sharp nor Gaussian-soft: compactness itself stabilizes the conformal-like scalar sector, with ±2 expanded about a non-trivial (possibly non-zero-field) state | **open**. This is the only window left for a light-like N-type graviton from finite slots | **open** |

## 5. Probe (b): numerics

- **Registered target:** the smallest qubit N-type or rank-2 toric-code-like model with an energetic constraint term, looking for a linear TT mode. **Not achievable by ED** (checked, s1 counts).
  - The smallest torus with a non-zero, non-π momentum is L = 3: 162 qubits unrestricted, or 2^58 states in the exact qubit sector (58 logical qubits).
  - An exponent fit needs ≥ 2 momentum shells, so L ≥ 4 (140 logical qubits) or L ≥ 5 (254).
  - Thin tori L × 1 × 1 collapse the y and z stencils and are effectively one-dimensional.
  - **No quantum many-body TT dispersion was computed.** I state this plainly rather than fit lattice-scale momenta.
- **Computed instead:**
  - (i) exact Z_N algebra: code size, aliasing, moments (s1, s1b, s1c);
  - (ii) Gaussian spectra of energetic N-type and L-type models at generic k: energetic L-type gives TT exponent 3.000 with zero-frequency gauge directions; energetic N-type gives TT 1.000 on an unstable scalar sector (s2);
  - (iii) Lemma DW-q, on random and ground states (s3).
- **Comparison with k³:**
  - every controlled regime gives k³ (both exact), ≤ k² (one exact) or an unstable Gaussian (both soft);
  - no controlled regime gives a stable linear TT branch without partners.

## 6. EXCLUDED candidates for the referee (stated-class no-gos; each is unrefereed)

**X1-E (emergent constraints, perturbative regime).**
- **Class.** Finite-slot local models H = H₀ + V on Z³, where:
  - H₀ = Δ Σ_a Π_a, with Π_a the projector onto a non-zero syndrome of each N-type stabilizer (commuting, integer spectrum);
  - V has finite range and local norm J;
  - Δ/J is large.
- **Claim (suggested; assembled).**
  - By the Abanin–De Roeck–Ho–Huveneers closed-system prethermal theorem (CMP 2017, arXiv:1509.05386; existence and scope V, constants RECALLED), there is a quasi-local unitary rotating H to H₀ + D + V′, with [D, H₀] = 0 and V′ quasi-exponentially small in Δ/J, up to times τ* ~ exp[c(Δ/J)/log³(Δ/J)].
  - P₀DP₀ is a sector Hamiltonian, so by Lemma A_c it equals a quasi-local strongly invariant one.
  - If its characters lift up to the truncation order (N > 36 n* M with n* ~ Δ/J) and H-lin holds, every small-field TT frequency is O(k³) for k ≳ τ*^{−1/3}.
- **Ingredients:** ADHH, Lemma A_c (`vR11-2:7`), `N0914:117-124,186-216`.
- **Not covered:** U ~ J ~ g (Gu–Wen), non-lifted N, and phases where H-lin fails.

**DW-q dichotomy (proved inequality; the dichotomy is suggested).** As in §4, for the referee to check the inequality and its scope.

## 7. Probe (c): literature

| Work | What it shows | Dispersion / modes | Numerics? |
|---|---|---|---|
| Gu–Wen, arXiv:0907.1203 (NPB 863 (2012) 90) | L-type qubit model: ±2 only, ε ∝ k³, reliable. N-type: linear ±2 "argued" by spin-wave/quantum freeze; "an uncontrolled approximation", "not a reliable result" | L: k³, 2 modes; N: k claimed, 0/±1 gapping hoped | **None.** "Numerical calculations are needed to show it convincingly" (V, conclusion via ar5iv) |
| Gu–Wen, gr-qc/0606100 | Lattice bosonic model, "linearized Einstein action", at least at linear level (V, abstract) | Quadratic with helicity 0 (search-engine summary only, not verified) | none in abstract |
| Xu, cond-mat/0602443 (PRB 74, 224433) | fcc boson liquid with "soft graviton" excitations | ω ~ k² (V, abstract) | none in abstract |
| Xu–Hořava, arXiv:1003.0009 | Lifshitz z = 3 emergent gravity; stability from gauge symmetry and self-duality (V, abstract) | k³. A remark that a Chern–Simons-like term gives linear dispersion but is only boundary-invariant comes from a search summary and is **not verified** | — |
| Pretko, arXiv:1606.08857 (PRB 96, 035119) | Higher-rank U(1) spin liquids, generalized electromagnetism (V, abstract); Table I: scalar charge 5 modes linear, vector charge k² (verified by R2's referee, `R2_referee.md:5`) | Linear spin-2 **with ±1/0 partners** (scalar charge) | no |
| Rasmussen–You–Xu, arXiv:1601.08235 | Stable gapless Bose liquids "without any symmetry" (V, abstract; dispersions not in abstract) | linear rank-2 liquids with partners (RECALLED) | no |
| Benton–Jaubert–Yan–Shannon, Nat. Commun. 7, 11572 (2016), arXiv:1510.01007 | Pinch-line tensor spin liquid on pyrochlore (V, abstract; classical/quantum not stated there) | — | classical MC (RECALLED) |
| Yan–Benton–Jaubert–Shannon, PRL 124, 127203 (2020) | Rank-2 U(1) spin liquid on the breathing pyrochlore (title V) | — | classical MC (RECALLED) |
| Shannon et al., PRL 108, 067204 (2012) (QMC of quantum ice) | rank-1 emergent photon, linear (RECALLED) | rank-1 only | QMC |

**Answer to (c).**
- No qubit or spin model in what I found has a *numerically demonstrated* linear, gapless spin-2 mode with two polarizations and no partners.
- Linear spin-2 modes in compact rank-2 U(1) liquids come with partners (scalar charge).
- Partner-free models are k³ (L-type, Lifshitz) or k² (Xu 2006).
- The only partner-free linear proposal (Gu–Wen N-type) is uncontrolled and unsimulated by its authors' own account.
- Scope of the search: 3 web searches and 7 abstract/full-text fetches. An absence in what I found is not a proof of absence.
- **Mechanism reading:**
  - the regular-class robustness of k³ is the same statement as Gu–Wen's "a locally invariant H cannot generate the linear term" (R0 table, `R0_report.md:131`);
  - Lemma DW-q gives it a quantitative non-perturbative form at first order.

## 8. Escapes that remain (named; none built)

| Escape | Criterion it must meet (from §3–4) | Status |
|---|---|---|
| E1. Gu–Wen regime (Q-en-s) | Both constraints fuzzy at the scale of their quantum (DW-q), yet compactness stabilizes the conformal-like scalar sector that the Gaussian leaves unbounded | open; needs numerics beyond ED. QMC on the N-type is likely sign-problematic (suggested, unchecked) |
| E2. Exact sector dominated by aliased or high-harmonic invariant characters (incl. N = 2) | IR Hamiltonian non-local in the IR curvature fields on *both* sides (dressing law, `R11-2:146-158`), i.e. emergent IR potentials with non-compact gauge orbits | open; small-support aliasing at N = 2 is TT-blind (checked, s1b) |
| E3. Induced terms from a gapped topological sector (Chern-band analogue of emergent CS) | The term must be invariant only up to total derivatives (h side) or only on shell (E side). Gapped sectors with *convergent* hopping/cluster expansions over compact link couplings give only closed-loop, invariant characters (suggested), so the term needs a topological obstruction to that expansion | open; no known mechanism induces parity-even h:R(h) this way (reading) |
| E4. Normalizable rotor sectors | Only one dressed side ⇒ ≤ k² (§4, Consequence 4) | **closed at power counting** for light-likeness; excluded by GW170817 |
| E5. Mixed per-component assignments (R11-2's O5) | — | not analysed |

## 9. Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| P-N1. Continuous canonical pairs on both h and E (supplied N-type) | Qubit (`AX:45-53`) | light-like TT at tree level |
| P-N3′. An *uncontrolled non-Gaussian compact mechanism* (E1/E2), stated as a hypothesis | none named; unbuilt | possibly light-like |
| P0 gauge-breaking masses (μ_E, μ_T2) to stabilize the soft energetic Gaussian | Admissibility rule content | stable linear TT, at P0's tunings (R2) |
| Rotor slots on one side | Qubit | k² only (excluded by GW170817) |

## 10. Readings against the FIXED clauses (`TESTS:4473-4476`)

- **PRODUCED: no.** No qubit model with a numerically demonstrated linear gapless TT mode was built or found.
- **EXCLUDED: not reached.** No refereed extension of X1 exists. Two candidates go to the referee:
  - X1-E, the emergent-constraint class in its perturbative regime;
  - DW-q with the one-exact ≤ k² cap.

  The strong-coupling class proper (E1) is not covered by any candidate.
- **Overall: OPEN.**

## 11. Strong-word check and scope

- **"Proved"** is used for:
  - Lemma DW-q, a two-line inequality, checked numerically;
  - the hypothesis audit in §3;
  - the one-exact ≤ k² cap, at the power-counting level for decoupled TT blocks (cf. `vR11-2:9`: power counting, not equality, in mixed blocks).
- **"Unbounded" / "unstable"** refers only to the quadratic (Gaussian) energetic N-type with finite gauge-invariant penalties (`N0914:262-270`; s2). The compact model is bounded. Its true ground state may simply not be near zero field.
- **The Gu–Wen tension** (Consequence 2) is proved as an inequality. Its application to their exact §VII Hamiltonian rests on a summary, not a verbatim reading. If their H_J used S-invariant characters, the tension would not apply. But then [H_U, H_J] = 0 on the scalar part, which contradicts their stated [H_U, H_J] ≠ 0 (V); this inference assumes the non-commutation they report involves the scalar part.
- **X1-E** is assembled from a comparator theorem whose constants I did not re-derive. It says nothing beyond τ*.
- **"No qubit model has shown…"** is bounded to the searched literature.
- **No tail or decay clause** was registered or used.

## Files

- `scripts/s1_alias.py` / `.out`: integer G Sᵀ = 0; code sizes over Q and GF(p); single-site aliased characters for N = 2…12.
- `scripts/s1b_moments.py` / `.out`: aliased characters on 2³ and 3³ blocks (N = 2, 3); zeroth and first moments.
- `scripts/s1c_hchar.py` / `.out`: explicit aliased qubit characters.
- `scripts/s2_gauss_energetic.py` / `.out`: Gaussian energetic N-type and L-type spectra at generic k.
- `scripts/s2b_one_exact.py` / `.out`: one-exact-constraint Gaussians (GX, SX); stability and TT exponent.
- `scripts/s3_dw_bound.py` / `.out`: Lemma DW-q on random states; ground-state trade-off for N = 5, 16, 64.

Sources (web, this run):
- [Gu–Wen 0907.1203](https://arxiv.org/abs/0907.1203) and [ar5iv full text](https://ar5iv.labs.arxiv.org/html/0907.1203)
- [Gu–Wen gr-qc/0606100](https://arxiv.org/abs/gr-qc/0606100)
- [Xu cond-mat/0602443](https://arxiv.org/abs/cond-mat/0602443)
- [Rasmussen–You–Xu 1601.08235](https://arxiv.org/abs/1601.08235)
- [Pretko 1606.08857](https://arxiv.org/abs/1606.08857)
- [Xu–Hořava 1003.0009](https://arxiv.org/abs/1003.0009)
- [Benton et al. 1510.01007](https://arxiv.org/abs/1510.01007)
- [ADHH 1509.05386](https://ar5iv.arxiv.org/html/1509.05386)
