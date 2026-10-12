# C5 R9-7 report: two-loop closure of toy N with the complete crossing set

**Author.** Claude Opus 5.5 probe, the same model family as the supervisor and the R8-4 worker. Unrefereed. Run 2026-10-12, 16:58Z to about 17:45Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R9-7/`. Scripts and outputs are in `S/scripts/`. Every run took under 2 min with `OMP_NUM_THREADS=2`.
- `r97_common.py` → `r97_common_orderings.out`. Enumerates all 24 time orderings of the O(g_o²g_i²) graph of X: monomial types at each vertex, intermediate states, and the parity of backward fermion lines.
- `r97_fock.py` → `r97_fock_{B,F}.out` and `r97_fock_{B,F}_P2.out`. A new, independent Fock engine (bitset CAR; occupation-number bosons). It runs brute-force RS4 on the explicit Hamiltonian with the new monomials, and compares with the 24-ordering closed form.
- `r97_cont.py`. The infinite-volume 1+1D evaluation:
  - `_B_base`, `_B_family`, `_F_family`: prescriptions P1–P4 at both statistics;
  - `_B_local`, `_B_lamscan`, `_B_mscale`: the local-limit control and the scaling with m/Λ;
  - `_B_Mkernel`: the fixed inner-mass kernel;
  - `_B_swap`: the dressed line placed inside the plateau pair.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md`:
  - `:2302-2330` (C5 method);
  - `:3370-3420` and `:3495-3535` (R7-5, R8-4 and their referee entries);
  - `:3780-3838` (round 8 referee results and R9-7, `:3822-3835`).
- `agents/C5_R8-4_report.md` (all of it) and `agents/C5_R8-4_referee_verdict.md` (all of it).
- `agents/C5_R7-5_report.md:140-312` and `agents/C5_R7-5_referee_verdict.md` (all of it).
- `scripts/C5/R8-4/r84_toyN_fock.py`, `r84_toyN_cont.py`, `r84_toyN_cont_cuts.py` and `r84_fock.py`, with their `.out` files.
- The referee's own checks in `ref_R8-4/`: `r84_referee_checks.py`, `.out`, `_qmc.out` and `_fixed_rapidity.out`.

There is no `C5_R8-4_referee.md` beyond the verdict.

**Labels.** proved / checked (numerics here) / suggested / reading / comparator. A comparator marked **R** is recalled and was not verified this session.

---

## 0. In plain words

- **The full set of orderings removes the large toy-N failure.**
  - Toy N lacked two kinds of ordering. The first is the 2↔2 crossing XY ↔ AB. The second is the reverse decay Y ↔ XAB. Exactly 14 of the 24 time orderings of the graph use them.
  - With all 24 orderings and constant vertices (the local limit), the two-loop E² − p² is flat to the numerical floor. The 10-ordering toy-N subset stays at about −0.54% at p = m/3, however wide the plateaus are made.
  - So R8-4's −0.6% (boson) and −6% (fermion) is mainly a missing-orderings effect, as the R8-4 referee suspected.
- **The registered completion still does not close.** P1 is toy N's vertices plus "the plateau of the pairs each new vertex creates". At p = m/3 the relative p-dependence of the two-loop m² is:
  - bosons: +4.8e-4, about 12 times smaller than toy N but nonzero, and the same at both grids to 4 digits;
  - fermions: −1.3e-2 to −3.6e-2, depending on the sign choice for the new monomials.
- **One completion closes exactly, for bosons.**
  - Prescription P2 gives every outer vertex the plateau of the (A, B) pair only. That pair is created together and absorbed together in every ordering.
  - P2 is exactly Lorentz-invariant at two loops (proved by reduction to a local theory; checked to 4e-16).
  - But P2's vertex never sees the Y leg, so it confines no leg to the momentum box. In 3+1D the remaining Y loop would be UV-divergent.
- **Why the box-compatible versions fail (mechanism checked; general claim suggested).**
  - A Hamiltonian vertex function is evaluated on the bare mass shell of each line it touches. The inner bubble moves the Y line off that shell. In the large-inner-mass limit this is a pure Y mass insertion.
  - Every tested plateau that involves the dressed line mis-handles that insertion: P1, P3, P4, and P2 with the dressed line moved into the plateau pair.
  - Confining all legs to the box needs exactly such a plateau.
  - In a theory where every line can be dressed, closure at this order would need vertex functions blind to every leg. That means constant vertices: no plateau.
- **Size.** In this 1+1D toy the residual falls steeply as m/Λ → 0:
  - P1 drops by ×35 and then ×56 per doubling of Λ/m;
  - a frame-fixed-cutoff comparator drops only by ×11–12.
  - Every regulator effect is power-suppressed in a super-renormalizable 1+1D toy, so this does not settle the 3+1D marginal-coupling case.
- **Fermions.** No tested choice closes: 4 prescriptions × 4 sign conventions, and the F ≡ 1 limit. For real kernels, the Pauli sign of the inner Z orderings cannot be absorbed into per-monomial factors (proved, elementary).
- **Against the FIXED readings: INCONCLUSIVE** (worker reading).
  - PASS is not met: the registered completion fails for both statistics, and the exact closure P2 is bosons only and outside the box.
  - FAIL is not met: there is no class-wide proof, and P2 is an exact counterexample in the unrestricted bosonic invariant-mass class.

---

## 1. Hypotheses and classes (stated before titles)

**Setting.**
- The setting is R8-4's toy N (`C5_R8-4_report.md:62-67`):
  - 1+1D;
  - distinct species X, Y, A, B (outer quartet) and Y, U, C, D (inner quartet);
  - masses 0.30, 0.33, 0.37, 0.41 / 0.29, 0.35, 0.43;
  - plateau F(s) = 1 − σ((√s − Λ₁)/(Λ₂ − Λ₁)) with (Λ₁, Λ₂) = (1, 1.4) unless stated.
- The quantity computed is the mixed O(g_o²g_i²) coefficient of E(X_p) − E(vac), as m²_mix(p) = 2E_p·mix(p).
- "Closure" means m²_mix(p) is p-independent.

**Dispersion.**
- Infinite-volume runs use the continuum dispersion E = √(m² + k²) for every leg.
- R8-4's frame-fixed leg and total-momentum cutoffs were inactive (`r84_toyN_cont_cuts.out`), so they are omitted here.
- Statements about a lattice box are made separately (§3.6).

**The complete crossing set** (proved by enumeration, `r97_common_orderings.out`).
- The only connected O(g_o²g_i²) graph for X is the sunset X → YAB with the Y line dressed by the inner sunset. Each vertex carries one leg of each species, so the topology is forced.
- Its 24 time orderings use these outer monomial types (each with its h.c.):
  - `dec`: X → YAB (in toy N);
  - `vac`: 0 → XYAB (in toy N);
  - `22`: XY → AB (new);
  - `31`: Y → XAB (new).
- The inner vertices use only Y ↔ UCD and 0 ↔ YUCD, which toy N already has. U, C and D always travel together.
- Toy N contains 10 of the 24 orderings. The other crossings (XA ↔ YB, A ↔ XYB, …) cannot enter this graph.

**Prescriptions.** Each lists the outer kernel times Π(2E)^{-1/2}; the inner kernel is always toy N's Ψ(U,C,D).
- **P1 (registered, `TESTS.md:3826`).**
  - Toy N's `dec`/`vac` kernel Ψ(Y,A,B) = F(s_YA)F(s_YB)F(s_AB), with `dec` × √h for fermions.
  - `22` = s₂₂·F(s_AB).
  - `31` = s₃₁·F(s_XA)F(s_XB)F(s_AB), evaluated on the created X, A, B.
- **P2.** Every outer type gets F(s_AB), with `dec` × √h for fermions. Y-blind and equal across crossings.
- **P3.** Every outer type gets Ψ(Y,A,B), evaluated at the Feynman-orientation 3-momenta. Equal across crossings and energy-independent, so it is Feynman-equivalent with a non-covariant vertex.
- **P4.** Plateau on the whole created set: `dec`/`vac` get F(s_YAB), `22` gets F(s_AB), `31` gets F(s_XAB).
- **P2swap.** F(s_YB) on every type: the dressed line sits inside the plateau pair.
- **FF (comparator).** Frame-fixed leg plateaus χ(k_Y)χ(k_A)χ(k_B) on every type.
- **F ≡ 1.** The local limit: every prescription becomes the same local theory.

**Statistics.**
- **Bosons.** Real-field crossing set, all signs +. This is the only case with a local Lorentz-invariant limit.
- **Fermions.** h = (3W − E)/(W + E) on toy N's decay vertices (outer and inner) only. The new monomials carry signs s₂₂, s₃₁ = ±1, all four choices.

**Excluded:** d = 3, gauge fields, the lattice-box dispersion outside the box, orders beyond O(g_o²g_i²), other self-energies, and microcausality.

## 2. Prior art (each counted once)

- **R8-4 and its referee.**
  - Toy N's −6.2% (fermion) and −0.60% (boson) at p = m/3 are confirmed (`TESTS.md:3818`).
  - The referee did not add the crossings because "the submitted invariant-mass prescription does not define their vertex functions" (`C5_R8-4_referee_verdict.md:62`).
  - The referee's expectation was that "a complete local bosonic crossing set recombines old-fashioned time orderings into the covariant diagram" (same line). §3.4 confirms it in the local limit.
  - R8-4's suggested mechanism: "outer vertex functions … evaluated at the bare on-shell kinematics of the Y line" (`C5_R8-4_report.md:221-223`). §3.6 isolates it.
- **R7-5.** "Two loops in INV are not shown … plausibly fails unless the dynamics is reorganised in BT form" (`C5_R7-5_report.md:274`).
  - The super-renormalizable control there: frame-fixed regulators give only power-suppressed LV for dimensionful couplings (`C5_R7-5_report.md:166-169`). This bounds what a 1+1D toy can show.
- **Lemma INV-3F** (`C5_R8-4_report.md:153-158`). It is used here for the two-body (A,B) and three-body (U,C,D) clusters.
- **Comparator R.** Old-fashioned perturbation theory with momentum-independent local vertices, summed over all time orderings, equals covariant Feynman perturbation theory (Weinberg 1966; textbook). Spinless fermion fields have no Lorentz-covariant time-ordered product (spin–statistics).
- **Axioms.** Admissibility "does not choose a Hamiltonian or transfer operator" (`MINIMAL_AXIOMS_2026-06-29.md:116-121`). Every vertex function here is supplied dynamics.

## 3. Results

### 3.1 From the Hamiltonian: the 24-ordering closed form (checked)

- `r97_fock.py` builds the Fock Hamiltonian with every monomial of the complete set, adds explicit h.c., and computes brute-force RS4 for X_p minus the vacuum. It covers d = 1 at L = 5 (periodic) and L = 6 (X, Y, U antiperiodic).
- The mixed coefficient is compared with the closed form: the sum over the 24 orderings of the kernel products and three energy denominators, with sign (−1)^{number of backward fermion lines} for fermions (U, C, D count 3).

| statistics / kernels | rows | max \|RS4(H) − closed\| |
|---|---|---|
| B, P1 kernels, subsets {}, {22}, {31}, {22, 31} | 16 | 1.6e-15 |
| F, P1 kernels, the same subsets, every H sign | 52 | 1.9e-16 |
| B, P2 kernels | 16 | 3.4e-15 |
| F, P2 kernels | 52 | 3.2e-16 |

- **Fermion signs.** The match is unique, with the sign map s₂₂(closed) = s₂₂(H) and s₃₁(closed) = −s₃₁(H) for the operator orders a†_A a†_B a_X a_Y and a†_X a†_A a†_B a_Y. There were 0 violations in 104 rows. All four closed-form sign choices are therefore realised by explicit Hamiltonians.
- **Lattice detail.** A leg plateau (|k| ≤ 2 → 2.5) multiplies every lattice kernel. Without it, zone-edge pairs give spurious "small" invariant masses from unwrapped k₁ + k₂, which broke the reflection symmetry at L = 6. That artifact was found and removed.

### 3.2 Reproduction of toy N (checked)

The 10-ordering subset of the infinite-volume engine reproduces R8-4 (`r97_cont_B_base.out`, `_F_family.out` against `r84_toyN_cont_{B,F}.out`):

| | m²_mix(0), this run | m²_mix(0), R8-4 | rel(p = 0.1), this run | rel(p = 0.1), R8-4 |
|---|---|---|---|---|
| bosons | −2.653463e-3 | −2.6534630861e-3 | −5.976e-3 | −5.98e-3 |
| fermions | −6.295180e-4 | −6.2951797935e-4 | −6.204e-2 | −6.20e-2 |

- The one-loop controls are flat to ≤ 1e-10.
- The inner cluster enters through its invariant mass M alone (INV-3F; proved). Fixed-M kernels are interpolated with 32/48 Chebyshev nodes. Two grids (G = 401/601, rapidity range 7.5/8.5) agree to the digits shown.

### 3.3 The registered completion P1 (checked)

Relative deviation [m²_mix(p) − m²_mix(0)]/|m²_mix(0)|, masses ×1, (Λ₁, Λ₂) = (1, 1.4); grids G = 401 and 601 identical:

| p | 0.1 | 0.2 | 0.3 | 0.4 | 0.6 |
|---|---|---|---|---|---|
| bosons, all 24 (m²(0) = −1.0739e-2) | +4.76e-4 | +1.99e-3 | +7.41e-3 | +3.49e-2 | +0.132 |
| bosons, toy-N 10 | −5.98e-3 | −2.36e-2 | −5.17e-2 | −8.90e-2 | −0.184 |
| fermions, all 24, (s₂₂, s₃₁) = (+,+) | −3.38e-2 | −0.132 | −0.290 | −0.464 | −0.815 |
| fermions (+,−) | −2.84e-2 | −0.106 | −0.225 | −0.395 | −0.806 |
| fermions (−,+) | −1.35e-2 | −5.00e-2 | −0.102 | −0.156 | −0.253 |
| fermions (−,−) | −3.62e-2 | −0.133 | −0.273 | −0.456 | −0.859 |

- **Bosons.** The deviation scales as p² at small p, with c ≡ rel/(p/m)² = +4.3e-3 against toy N's −0.054.
- **Not closed.** The quadrature floor is about 1e-10 (the one-loop control), so P1 does not close for either statistics.

### 3.4 The local-limit control (checked): toy N's failure is a missing-orderings effect

Bosons, P1, plateau scale Λ₁ = λ (Λ₂ = 1.4λ), relative deviation at p = 0.1 (`r97_cont_B_local.out`, `_lamscan.out`):

| λ | 1 | 2 | 4 | 8 | 16 | ∞ (F ≡ 1) |
|---|---|---|---|---|---|---|
| all 24 orderings | +4.76e-4 | +1.36e-5 | +2.45e-7 | grid noise ≤ 4e-7 | floor 2e-5 | floor ≤ 2e-4 (sign flips between grids) |
| toy-N 10 orderings | −5.98e-3 | −5.55e-3 | −5.45e-3 | −5.44e-3 | −5.44e-3 | −5.43e-3 (both grids) |

- **The floor in the local limit.** At F ≡ 1 the integrands have power-law tails. The one-loop control there is flat only to 1e-5–7e-5, which sets the floor.
- **The complete set approaches covariance.** The 24-ordering residual falls ×35 and then ×56 per doubling of λ, and is within the floor in the local limit.
- **The toy-N subset does not.** It converges to a regulator-independent −0.54% at p = m/3. That is O(1) relative to the two-loop term even for a local Lorentz-invariant theory.
- **Answer to `TESTS.md:3827`.** Yes: with the complete set, E² − p² becomes p-independent as the plateaus widen. Toy N's subset does not.
- **Fermions.** At F ≡ 1 the complete set gives −0.33 at p = 0.1 and the subset −3.9e-2. Spinless fermions have no covariant local limit (comparator R), so no fermionic control exists.
- **Consistency check.** Halving all masses at fixed Λ reproduces the λ = 2 numbers exactly, and quartering reproduces λ = 4 (`_mscale.out`). This is dimensional analysis: only m/Λ matters in the toy.

### 3.5 A completion that closes exactly: P2 (proved; checked)

**Theorem A.**
- *Setting.* 1+1D bosons with the complete crossing set and the continuum dispersion on every leg.
- *Outer kernels.* Every type (`dec`, `vac`, `22`, `31` and the h.c.) carries Φ(s_AB)·Π(2E)^{-1/2}, with one bounded Φ for all types.
- *Inner kernels.* Ψ_in, any function of the U, C, D pair invariants, for both the decay and the vacuum monomial.
- *Conclusion.* Then 2E_p·mix(p) is independent of p.

*Proof.*
1. In all 24 orderings A and B are created at one outer vertex and absorbed at the other. U, C and D are likewise created and absorbed together at the inner vertices (`r97_common_orderings.out`). So each integrand depends on (k_A, k_B) only through Φ², 1/(4E_AE_B), E_A + E_B and k_A + k_B, and similarly for U, C, D.
2. By INV-3F, ∫dk_A dk_B δ(k_A + k_B − K)Φ²G(E_A + E_B)/(4E_AE_B) = ∫dμ²ρ_Φ(μ²)G(E_μ(K))/(2E_μ(K)). The same holds for U, C, D with ρ_in(M²).
3. Hence mix = ∫dμ²ρ_Φ∫dM²ρ_in·T(p; μ, M). Here T is the 24-ordering sum of the local theory H_int = φ_Xφ_Yφ_S + φ_Yφ_Φ: real scalars, unit couplings, masses (m_X, m_Y, μ, M). Its normal-ordered monomials are exactly the 8 + 4 types, with kernels Π(2E)^{-1/2}.
4. For momentum-independent local vertices, the all-ordering sum equals the Feynman 1PI two-loop Σ at P⁰ = E_p (comparator R). No intermediate state is degenerate with X_p, because every cut crosses at least two internal lines (enumeration). So 2E_p·mix = Σ(m_X²).
5. Convergence holds because the sunset is UV-finite in two dimensions. ∎

*Check.* m²_mix(0) = −1.1553e-2, with relative deviation ≤ 4.5e-16 at every p ≤ 0.6, on both grids (`r97_cont_B_base.out`). The fixed-M kernel is flat to ≤ 2.3e-16 for M = 1.2…64 (`_Mkernel.out`). The 10-ordering subset with the same P2 kernels gives −6.0e-3: again the missing orderings, not the plateau.

**Scope of Theorem A (strong words).**
1. **Lemma B (proved, elementary): P2 is not box-confining.**
   - At fixed p and fixed s_AB, the allowed (k_A, k_B) form a boost orbit of the pair. That orbit is unbounded, so k_A, k_B and k_Y = p − k_A − k_B are unbounded on the support.
   - In a lattice realization, legs leave the box, where ε̃ ≠ √(m² + k²). The INV-3F reduction then fails there.
   - The leakage is not computed. In 1+1D it is plausibly power-suppressed (suggested).
2. **In d = 3 the class is not finite.** The remaining X–Y–S_μ loop is log-divergent by power counting (R), so it needs a regulator that sees Y.
3. **Fermions: P2 fails.** For the four sign choices the deviations at p = 0.1 are −2.80e-2, −2.59e-2, −1.35e-2 and −3.66e-2 (`r97_cont_F_family.out`).
4. **Only one dressing pattern.** P2 is blind only to Y. With the dressed line placed inside the plateau pair (P2swap, plateau on (dressed, B)), the result is +3.4e-4 at p = 0.1 and +1.18e-2 at p = 0.6, on both grids (`_swap.out`).

### 3.6 Why the box-compatible plateaus fail (mechanism checked; general claim suggested)

**Box-confining family** (bosons, p = 0.1, λ = 1, both grids):

| prescription | rel.dev at p = 0.1 |
|---|---|
| P1 | +4.76e-4 |
| P3 | +5.24e-4 |
| P4 | +2.53e-2 |
| P2swap | +3.4e-4 |

All of these involve the dressed line in a plateau. The only closing case, P2, does not.

**The fixed inner-mass kernel K(p; M)** (`_Mkernel.out`, checked).
- K is the two-loop with the inner cluster replaced by a single mass M.
- Its relative p-dependence at p = 0.1 is nearly M-independent and does not vanish as M → ∞:
  - P1: 4.78e-4 (M = 1.2) → 4.26e-4 (M = 64);
  - P3: 5.28e-4 → 4.67e-4;
  - P4: 2.54e-2 → 2.39e-2;
  - P2: ≤ 2.3e-16.
- At large M the Y–Φ_M insertion acts as a local Y mass insertion −φ_Y²/M² (R, standard decoupling). So already a pure shift of Y's mass shell breaks P1, P3 and P4.
- **Every inner dressing fails for these outer vertices (checked on a 7-point M grid).** For P1, P3 and P4, K(0; M) < 0 and the p-induced change has one sign for every tested M. So no nonnegative inner spectral weight ρ_in on M ≥ 1.2 can cancel the p-dependence. This is checked on 7 M values with a smooth monotone trend; it is not proved for all M.

**Mechanism (suggested; a derivation at integrand level only).**
- Under m_Y² → m_Y² + δ, the old operators mix: a_Y = c·b + s·b†. So the new X → Y′AB kernel is c·κ_dec + s·κ_22 (and likewise for `vac` ↔ `31`).
- For local vertices (κ_dec = κ_22, no Y-energy dependence) this is a pure renormalization.
- For invariant-mass kernels the two pieces differ (κ_dec ≠ κ_22 in P1). The plateau arguments are also frozen on the old shell at fixed 3-momenta: ∂s_Yj/∂m_Y² = 1 + E_j/E_Y, which is frame-dependent.
- A Hamiltonian vertex function sees only bare on-shell Fock kinematics, so it cannot follow the dressed line's spectral mass.
- This makes R8-4's suggested mechanism precise (`C5_R8-4_report.md:221-223`).

**The general claim (suggested, not proved).**
- Box confinement needs every leg bounded at fixed external momentum (Lemma B forbids the Y-blind escape). So some plateau must involve each leg.
- In a theory where every species interacts, every leg is dressed somewhere at this order.
- Closure for every dressing would then require vertex functions blind to every leg's on-shell energy and equal across crossings, which means constant.
- So invariant-mass plateaus cannot be radiatively closed at two loops in the class "box-confining, all lines interacting".
- What is shown: the mechanism, checked in four prescriptions and P2swap. A proof for every function in the class is not given. Only integrated quantities must be covariant, so pointwise non-invariance is not a proof.

### 3.7 Size of the residual, and what the toy cannot decide (checked; reading)

Relative deviation at p = 0.1 against λ (`_lamscan.out`):

| | λ = 1 | λ = 2 | λ = 4 | factor per doubling |
|---|---|---|---|---|
| P1 | 4.76e-4 | 1.36e-5 | 2.45e-7 | 35, 56 |
| P3 | 5.24e-4 | 1.62e-5 | 3.03e-7 | |
| P4 | 2.53e-2 | 2.88e-4 | 2.63e-5 | 88, 11 |
| FF, one loop | 1.94e-3 | 2.54e-4 | 2.72e-5 | |
| FF, two loop | 1.38e-3 | 1.25e-4 | 1.00e-5 | 11, 12 |

- **Reading.** In 1+1D the box-confining invariant-mass residual is a regulator-scale effect that vanishes as m/Λ → 0, faster than the frame-fixed comparator.
- **What the toy cannot decide.** In a super-renormalizable toy every regulator's LV is power-suppressed (`C5_R7-5_report.md:166-169`). So the toy cannot tell whether the d = 3 marginal-coupling analogue leaves unsuppressed dimension-4 LV.
- **The d = 3 expectation (suggested).** The plateau is not a covariant regulator of the dressed subgraph, and Collins-type O(1) dimension-4 terms are generic there. This is not computed.

### 3.8 Fermions (checked; one elementary proof)

- **All tested choices fail.** Every combination of P1–P4 with each of the four sign choices fails, with deviations of −1.25e-2 to −0.135 at p = m/3, the same on both grids. F ≡ 1 also fails (−0.33).
- **The sign obstruction (proved, elementary).** Take the inner-Z orderings, e.g. (oa, i2, ob, i1). Both inner vertices are of the vacuum type, so their kernel product is |κ_v|² ≥ 0 for real kernels. The fermion ordering sign is (−1)³ = −1, against +1 for bosons. Therefore no choice of per-monomial real factors maps the fermionic ordering sum onto the bosonic one ordering by ordering.
- At one loop, h repairs this only in the sum (Lemma INV-3F of R8-4). No such factor was found at two loops. Kinematic h-type factors on the new vertices were not searched, so fermionic non-closure is checked only in the stated finite class.

## 4. Answer to the registered question

| item (`TESTS.md:3826-3828`) | result | label |
|---|---|---|
| complete toy N (XY ↔ AB, Y ↔ XAB), recompute E² − p² | bosons +4.8e-4, fermions −1.3e-2…−3.6e-2 at p = m/3; not closed | checked; closed form verified against brute-force RS4 to ≤ 3.4e-15 |
| local-limit control | complete set → p-independent as λ → ∞ (×35, ×56 per doubling; within the F ≡ 1 floor); toy-N subset stuck at −0.54% | checked |
| why closure fails | the vertex function lives on the bare shell of the dressed line; box confinement forces dependence on it; P2 (Y-blind) closes exactly but confines nothing | Theorem A and Lemma B proved; mechanism checked; class no-go suggested |

## 5. Strong-word check

- **"Exactly Lorentz-invariant" (P2).**
  - Bosons, 1+1D, O(g_o²g_i²), the continuum dispersion on every leg.
  - It uses comparator R (OFPT = Feynman for local vertices).
  - Numerically flat to ≤ 4.5e-16. That is exact up to rounding: the rapidity-grid trapezoid on smooth integrands converges super-algebraically.
  - Not box-confining, and not in d = 3.
- **"Fails" (P1, P3, P4, P2swap).**
  - At λ = 1 these are 5e6–2.5e8 times the one-loop floor (1e-10) for P1, P3 and P4, and about 55 times it for P2swap (whose one-loop floor is about 6e-6, because its legs are unbounded). All are stable across grids.
  - Fermions are only the tested finite class.
  - Not a theorem over all vertex functions.
- **"Missing-orderings effect."** The toy-N subset stays at −5.4e-3 to −6.0e-3 for every λ, including F ≡ 1, and under P2 kernels. The complete set is flat within each case's floor.
- **"Suppressed."** Only in 1+1D, where the coupling is super-renormalizable. No d = 3 statement is made.
- **"Every inner dressing fails" (P1, P3, P4).** The sign uniformity is checked on 7 M values, not proved.

## 6. Against the FIXED readings (`TESTS.md:3830-3833`)

**INCONCLUSIVE.** Worker reading, same model family, unrefereed.

- **PASS: not met.**
  - The registered completion (P1) is not p-independent for either statistics (§3.3).
  - P2 is p-independent to rounding for bosons, but not for fermions (§3.5). It also changes toy N's own `dec`/`vac` vertex functions, and it is not box-confining.
- **FAIL: not met.**
  - In the unrestricted bosonic class of invariant-mass plateaus on created pairs, P2 is an exact counterexample (proved and checked), so no no-go holds there.
  - In the box-confining subclass, non-closure is checked for four choices with a stated mechanism, but not proved for every choice.
  - For fermions, failure is checked in a finite list only.
  - Any FAIL needs the other-vendor referee.
- **The expectation** (`TESTS.md:3835`) "leaning FAIL" is half right. Box-compatible products of plateaus fail. But the toy-N failure was mostly missing orderings, and a Y-blind plateau set closes exactly.

## 7. Price (named, not adopted)

- **Supplied dynamics.** As in R8-4 (`MINIMAL_AXIOMS_2026-06-29.md:116-121`), plus the full crossing set: 2↔2 and reverse-decay monomials for every quartic vertex.
- **Two-loop closure condition (suggested).**
  - Each vertex function must be equal across crossings and blind to the on-shell energy of every line that can be dressed. For an all-interacting theory that leaves only local vertices, which cannot confine legs to the box.
  - The alternatives are:
    - (a) an order-by-order redesign of the vertex functions on the renormalized shells, an infinite tower of custodial conditions;
    - (b) a BT-type mass-operator reorganization, whose cluster-separability price is recorded at `C5_R8-4_referee_verdict.md:79`;
    - (c) give up exact closure, accept regulator-scale LV, and compute it in d = 3.
- **Fermions.** Spinless fermions need frame-dependent kinematic factors beyond h. None is known at two loops.

## 8. For the referee

1. **Ordering enumeration.** Check `r97_common.py:38-58`: the vertex-type map, the present-lines sets, and nback. Then confirm that only XY ↔ AB and Y ↔ XAB enter (§1).
2. **Brute-force check.** Rerun `r97_fock.py B`, `F`, `B P2` and `F P2`. Check the fermion sign map s₃₁(closed) = −s₃₁(H), and the leg plateau that removes zone-edge pairs.
3. **Theorem A.** Check the two-body INV-3F reduction in 1+1D and the identification of the 8 + 4 monomial types with the normal-ordered φ_Xφ_Yφ_S + φ_Yφ_Φ. Rerun `r97_cont.py B base`.
4. **The local-limit control.** Is λ = 1, 2, 4 (×35, ×56) with the F ≡ 1 floor (±2e-4, one-loop ±7e-5) sufficient? Is the toy-N subset's λ-independence (−5.4e-3) convincing?
5. **The large-M kernel.** Check the claim that M → ∞ is a pure local Y mass insertion, and the sign uniformity of K over M (`_Mkernel.out`).
6. **Fermion sign obstruction.** Check the (oa, i2, ob, i1) argument.
7. **Decisive open items.**
   - (i) A d = 3 version: whether a box-confining invariant-mass completion leaves O(g⁴/(16π²)²) dimension-4 LV.
   - (ii) A proof over all box-confining plateau functions.
   - (iii) The lattice-box leakage of P2.
