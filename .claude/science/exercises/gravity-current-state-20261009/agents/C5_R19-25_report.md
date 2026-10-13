# C5 R19-25: the finite-site graviton with weakly imposed (Gupta–Bleuler / BRST-type) constraints. Does it escape Lemma J and Proposition C?

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-13, 06:37Z to about 07:30Z. **Unrefereed.** I edited no repository file and downloaded nothing. Scripts and outputs are in `S/scripts/` (s2–s6; s4 takes 4 min, the rest take seconds, all on 2 threads). Rechecks are in `S/recheck/`.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`. The registration is `TESTS:8322-8353`, with the FIXED readings at `TESTS:8349-8352`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `R19-22` = `P/agents/C5_R19-22_report.md`; `vR19-22` = `scratchpad/C5/ref_R19-22/REFEREE_VERDICT.md` (it landed at 06:48Z, during this run); `R15-5` = `P/agents/C5_R15-5_report.md`; `vR15-5` = `P/agents/C5_R15-5_referee_verdict.md`.
- `S` = `scratchpad/C5/R19-25/`.

**Labels.**
- proved: a derivation made here (unrefereed);
- checked: numerics run here;
- suggested: an argument, not a proof;
- reading: an interpretation;
- comparator: literature, RECALLED, not fetched.

**Recheck (checked).** These archived runners reproduce byte-for-byte (0 diff lines; `S/recheck/*.recheck.out`):
- R19-22 s2, s3 and s6;
- R15-5 s1.

**R19-22 referee (read before use).** It returned CONFIRMED WITH CORRECTIONS, reading OPEN:
- Lemma J is confirmed (`vR19-22:2`: no nonzero joint-kernel state for any S ≥ ½ in the linear HP embedding).
- Proposition C is corrected to E₀/V ≤ −(3/4)JS + O(J+U+g+V). It is an energy comparison, not a proved isolated-sector gap (`vR19-22:3`).
- The trace argument forbids CCR, not every exact finite constraint (`vR19-22:1`).

I rely on Lemma J as refereed and on Proposition C only in its corrected form.

---

## 0. Plain words

- **The question.** On finite slots, the graviton's two gauge constraints cannot hold exactly. They have no common solution (Lemma J), and penalties pull the ground state into a "trace-collapsed" configuration (Proposition C). The registered escape is to impose the constraints weakly instead, as quantum electrodynamics does in covariant gauges:
  - (a) **Gupta–Bleuler:** only the positive-frequency half of the constraint annihilates physical states, and the state space carries an indefinite metric;
  - (b) **BRST:** add fermionic ghost slots, and take physical states as the cohomology of a nilpotent charge Q.
- **BRST, in the forms the registration names, gives nothing at finite S (proved; checked).**
  - In the standard ghost polarization, the ghost-number-0 cohomology is exactly the strong joint kernel. Lemma J says that kernel is zero.
  - If you instead close the constraint algebra and use its Lie-algebra BRST charge, the closure is all of ⊕_a su(2)_a (Lemma J's ranks). Its cohomology is **zero in every ghost degree, in any polarization**: each spin-S slot has no singlet.
  - The naive charge with the S = ∞ (abelian) structure has Q² = (i/S)·Σ_a n_a·(ghost bilinear), where n_a is the HP occupation. Q² = 0 on the HP vacuum, and O(n/S) on low occupation, as expected.
- **Gupta–Bleuler is different: it really does escape Lemma J and Proposition C at the level of the vacuum.**
  - Its conditions use only lowering parts, and those commute, so the vacuum always satisfies them.
  - The indefinite metric turns the trace collapse's "negative energy" into "negative norm, positive frequency".
- **What blocks it at finite S** (proved, checked):
  1. **Lemma K (slot-by-slot nullness).** For Gupta–Bleuler to remove the unphysical pair, the positive-frequency constraint must have zero norm. At CCR that happens by *cancellation between slots*: a positive-norm and a negative-norm canonical commutator, +1 − 1. On finite slots a partial-trace argument shows the commutator must vanish *slot by slot*, so the cross-slot cancellation is impossible at every finite dimension. The Kugo–Ojima-type charge then has Q² ∝ that commutator ≠ 0.
  2. **With spin-S (HP) slots** (checked, two-slot quartet toy):
     - Q² ∝ (n_T − n_L)/S;
     - the Gupta–Bleuler space leaks out under a conserved-source coupling at rate 1/S;
     - every even level gets a spurious **positive**-norm "physical" state, with norm exactly 1/(4S − 1).
     - So "exactly two branches" fails at O(1/S), as the registration expected. No negative norms appeared in this toy.
  3. **With truncated-oscillator slots** (exact canonical commutator except on the top level):
     - **The decoupled quartet is exact.** Every level below the top is null; the physical quotient is the vacuum only, positive. The only defect sits on the top level (checked, d ≤ 17).
     - **But with local lattice dynamics,** the positive-frequency parts are Bogoliubov mixtures of raising and lowering operators. Then the Gupta–Bleuler space is **empty**: dimension 0 on a 3-site ring (d = 2–4) and on a 2-site ring (d = 2–7, two masses). Checked, small.
     - Only approximate solutions exist. Their residual falls roughly ×0.5–0.6 per level.
  4. **The N-type's own 6 spatial slots cannot carry Gupta–Bleuler,** even with CCR: no cubic per-slot sign metric makes the local vector constraint null (checked at three momenta, all four sign choices). Gupta–Bleuler needs the lapse and shift, i.e. the covariant 10-component field.
     - With CCR, that covariant version works: two positive TT states and four null ones at the four lattice momenta tested, and an attractive static T⁰⁰ coupling (numerator ½). Checked; the algebra holds for any lightlike k (comparator: Gupta, GR).
- **Reading: OPEN.**
  - No finite-S construction has a positive physical space, exactly two branches and a 1/r pull. So WEAK-ESCAPE is not met.
  - My no-gos cover stated classes and are unrefereed. Approximate Gupta–Bleuler on truncated slots is not excluded. So WEAK-OBSTRUCTED is not met.
  - The live window is narrow and named: approximate covariant Gupta–Bleuler on truncated slots, with residual decaying in d.
  - Its cost: 10 slots per cell, a Krein metric on the site space, and a state-selection rule.
  - Its exact version does not exist in the cases tested.

---

## 1. Hypotheses, classes, excluded realizations

**Setting** (`TESTS:8334-8340`): R15-5's N-type, H_N = J/2[E:E − ½(trE)²] + g/2 h:R(h) (`N0914:72-76`), with constraints (Gp)_e, (Sq)_y and N0914's integer stencils (`N0914:85-113`). Each canonical slot is replaced by:
- a spin-S slot (HP: q = S^y/√S, p = S^z/√S; `R19-22:64-66`); or
- a d-level truncated oscillator (A|n⟩ = √n|n−1⟩, so [A, A†] = 1 − d|d−1⟩⟨d−1|), the Z_N-clock-like case with CCR scaling.

**Classes examined.**
- **𝔅_c (BFV/BRST, c-polarization).** Q = Σ_α G_α ⊗ c^α + R. Every term of R contains at least one ghost momentum b, ordered to the right. The G_α are exactly the HP constraints. Structure functions are arbitrary.
- **𝔅_Lie (Lie-closure BRST).** The Chevalley–Eilenberg charge of the Lie algebra generated by the HP constraints, acting through the HP representation. Any ghost polarization.
- **𝔊_lin (Gupta–Bleuler, slot-linear).** Finite slots with arbitrary Krein metrics η_a (η = ⊗η_a, X^K := ηX†η). The constraint's positive-frequency part is a sum of single-slot operators, C⁺ = Σ_a Y_a. This includes Y_a = α_a A_a + β_a A_a^K, i.e. local-oscillator or Bogoliubov positive frequency on any slot type. Physical space V = ker C⁺; physical quotient V/(V ∩ V^⊥η).
- **Kugo–Ojima form.** Q = C⁺ ⊗ γ^K + C⁺^K ⊗ γ, with a null ghost pair (γ² = 0, {γ, γ^K} = 0).

**Excluded realizations** (nothing negative here covers them):
- positive-frequency parts that are not sums of single-slot operators (multi-slot nonlinear dressings);
- BRST charges whose c-linear part is not the HP constraints, e.g. covariant charges built on lapse/shift plus Nakanishi–Lautrup slots (this is the route left open in §8);
- state-dependent or approximate weak conditions with stated residual;
- emergent or interacting phases (P-N3″, P-r16-7a);
- the Z₂/aliasing window (R17-1);
- matter, nonlinear gravity, Λ.

---

## 2. Prior art (each counted once)

1. **R19-22 and vR19-22.**
   - Lemma Tr (`R19-22:127-132`).
   - Lemma J (`R19-22:134-149`), refereed (`vR19-22:2`).
   - Proposition C (`R19-22:151-164`), corrected (`vR19-22:3`).
   - The wrap identity for exact clocks (`R19-22:166-170`).
   - The trilemma for positive local completions: Jordan chain, tachyon, or 6 branches (`R19-22:172-184`).
   - Weak imposition is listed as excluded there (`R19-22:79,302`). This item fills that gap.
2. **R15-5 and vR15-5.**
   - Lemma E: the escape is indefinite energy plus exact first-class constraints (`R15-5:122-145`; `vR15-5:5-8`).
   - The ladder (`R15-5:158-170`).
   - Lemma T, the conserved-source requirement (`R15-5:204-209`; `vR15-5:37-40`).
   - P-r15-5b (`R15-5:259`).
3. **R15-3 refereed** (`TESTS:5184-5189`). Finite, continuous, PSD, cubic-covariant Gaussians have ≥ 4 gapless branches. I use it to dispose of **positive-metric** weak schemes at the Gaussian level (§3.4). Not re-derived.
4. **R16-7 and R16-11 refereed** (`TESTS:5582-5586`, `5894-5900`). These cover exact integer laws; not used here beyond context.
5. **N0914.**
   - The constraint complex and G Sᵀ = 0 (`N0914:85-113`).
   - Finite penalties: det K = −J²/2 (`N0914:262-270`).
   - The static scalar source, −g|ρ|²/(4k²) (`N0914:290-296`).
6. **Comparators (RECALLED).**
   - Gupta–Bleuler covariant quantization of the photon and of linearized gravity (Gupta 1950/1952).
   - The Kugo–Ojima quartet mechanism.
   - BFV / Henneaux–Teitelboim BRST.
   - Whitehead's lemmas: H^n(g, V) = 0 for semisimple g and nontrivial irreducible finite-dimensional V. Plus the Künneth formula for Lie-algebra cohomology.
   - Quantum link models: spin-S links tend to *compact* U(1).
   - Uniqueness of the finite-dimensional CAR representation.

---

## 3. (a) Consistency at finite S: does Q² = 0, and is the weak condition preserved?

### 3.1 BRST in c-polarization: H⁰ is the strong kernel (proved)

- **Statement.** In 𝔅_c, the ghost-degree-0 cohomology is ∩_α ker G_α.
- **Proof.**
  - States of c-degree 0 are ψ ⊗ |0⟩ with b|0⟩ = 0, so R annihilates them.
  - Qψ⊗|0⟩ = Σ_α G_αψ ⊗ c^α|0⟩, so ψ is closed iff every G_αψ = 0.
  - There is no degree −1, so nothing is exact. ∎
- **Consequence.** H⁰ = {0} at every S ≥ ½, by Lemma J (refereed). This holds for any structure functions and any ordering of b's to the right.
- **So BRST in this polarization is strong imposition in disguise,** and Lemma J kills it exactly, not at O(1/S).
- **Toy (checked, s2(c)).** On the 3-slot toy with g·s = 0 the joint kernel is zero at half-integer S and nonzero at integer S. This is consistent with R19-22's control (`R19-22:149`); the lattice statement is Lemma J.

### 3.2 Lie-closure BRST: zero cohomology in every degree (proved via RECALLED theorems; checked)

- **The closure is ⊕_a su(2)_a.**
  - Lemma J's double-commutator coefficient matrices have full column rank (refereed: 162/162 on 3³ and 750/750 locally; `vR19-22:2`).
  - So every q_a and p_a lies in the generated Lie algebra. Then S^x_a = −iS[q_a, p_a] does too.
  - The algebra therefore contains, and by linearity in spin components equals, ⊕_a su(2)_a.
- **Cohomology.** H*(⊕_a su(2)_a, ⊗_a V_S) = ⊗_a H*(su(2), V_S) (Künneth) = 0, because H^n(su(2), V_S) = 0 for S ≥ ½ (Whitehead, RECALLED).
- **Checked (s2(b)), Chevalley–Eilenberg ranks with Q² = 0 to ≤ 1.6e-15:**
  - dim H^n = 0 for n = 0..3 for su(2) on V_S, S = ½, 1, 3/2, 2, 3;
  - (1, 0, 0, 1) for the trivial representation (control);
  - all zero for su(2)⊕su(2) on V_½⊗V_½ and on V_1⊗V_½.
- **Polarization independence (proved).** The finite CAR algebra has one irreducible representation, so choosing a different ghost vacuum only relabels degrees. The total cohomology of a given Q does not change.
- **Reading.** Closing the algebra makes Q nilpotent exactly, but the physical space is then empty. That is the BRST face of "no singlet in a spin".

### 3.3 Naive abelian Q (the S = ∞ structure transplanted) (proved; checked)

- **Identity.** Q = Σ_e (Gp)_e c^e + Σ_y (Sq)_y c^y. Since [Gp, Gp′] = [Sq, Sq′] = 0, R19-22's identity (`R19-22:135`) together with G Sᵀ = 0 gives
  Q² = (i/S) Σ_a n_a C^G_a C^S_a,
  with C^G_a = Σ_e G_ea c^e, C^S_a = Σ_y S_ya c^y, and n_a = S − S^x_a.
- **Checked on the toy (s2(a)).**
  - |Q² − prediction| ≤ 1.3e-15 for S = ½..3.
  - ‖Q²‖ = 0 on the HP vacuum; 1/S on total occupation ≤ 1 (2.0, 1.0, 0.5, 0.333 at S = ½, 1, 2, 3); 2/S on occupation ≤ 2.
  - ‖Q²‖ = 2 on the full space at every S.
- **Reading.** This confirms the registered expectation "Q² ≠ 0 at O(1/S)" (`TESTS:8353`), in the precise form O(occupation/S).

### 3.4 Gupta–Bleuler with the slots' own (positive) metric

- **Lemma J is escaped trivially (proved).** With local HP lowering parts, (Gp)⁺ = Σ_a G_ea A_a and (Sq)⁺ = Σ_a S_ya A_a. All A_a commute, so the joint kernel always contains the HP vacuum.
- **But with a positive metric, nothing is null.** The "unphysical" modes are positive-norm degrees of freedom held in their vacuum by a choice of state.
  - At the Gaussian (linear-response) level these schemes are positive quadratic theories. They fall under R15-3's refereed ≥ 4 gapless branches (finite, continuous, PSD, cubic-covariant) and under R19-22's trilemma for local completions (`R19-22:172-184`).
  - Not re-derived; counted once.
  - A sourced, conserved T excites those modes with positive probability (reading, using `R15-5:204-209`).
- **So a weak scheme needs an indefinite (Krein) metric,** as in covariant QED (comparator). The rest of this section treats Krein slots.

### 3.5 Lemma K: on finite slots, nullness must hold slot by slot (proved; checked)

- **Statement.** In 𝔊_lin, [C⁺, C⁺^K] = Σ_a [Y_a, Y_a^K]. This vanishes iff [Y_a, Y_a^K] = 0 for **every** slot a.
- **Proof.**
  - Operators on different slots commute, so the cross terms vanish.
  - Take the partial trace over all slots except a. Every other term contributes (∏ d)·tr[Y_b, Y_b^K]·1 = 0, since the trace of a commutator is zero.
  - What remains is (∏_{b≠a} d_b)[Y_a, Y_a^K]. ∎
- **Checked (s3(5)).** On random 3-, 2- and 4-dimensional slots with random Krein signs, the partial-trace identity holds to 0.
- **Corollaries (proved).**
  - **(K1) No cross-slot cancellation.** For Y_a = α_a A_a + β_a A_a^K:
    [Y_a, Y_a^K] = (|α_a|² − |β_a|²)[A_a, A_a^K].
    - With CCR, [A_a, A_a^K] = η_a·1 = ±1. Nullness then comes from Σ_a (|α_a|² − |β_a|²)η_a = 0, a cancellation between positive- and negative-norm slots. That is how Gupta–Bleuler works.
    - On finite slots this is impossible: each slot needs (|α_a|² − |β_a|²)[A_a, A_a^K] = 0 separately.
    - For a slot that carries a canonical pair on its low levels, [A_a, A_a^K] ≠ 0. Its trace is zero, so it is at best ±1 on part of the space with a compensating defect.
  - **(K2) Positive slots.** If η_a = 1 and Y_a is a strict positive-frequency (nilpotent) slot operator, then Y_a is normal and nilpotent, so Y_a = 0.
  - **(K3) Kugo–Ojima.** With γ² = 0 and {γ, γ^K} = 0, Q = C⁺⊗γ^K + C⁺^K⊗γ gives Q² = [C⁺, C⁺^K] ⊗ γ^Kγ. So Q² = 0 needs exact nullness, and (K1) forbids it in the CCR-like form at any finite d.
- **What Lemma K does not say.** Gupta–Bleuler needs nullness only *on V*, not as an operator identity. The defect can sit outside V. §3.6 tests when it does.

### 3.6 The null pair on finite Krein slots (checked, s3)

**Model.**
- Slot L has metric +1; slot T has metric (−1)ⁿ (the negative-norm partner).
- C⁺ = A_L − A_T and H₀ = ω(n_L + n_T). The frequency is exact at every d (residual ≤ 1.2e-14).
- With CCR, V = span{Xᴺ|0⟩}, all null for N ≥ 1, and the quotient is the vacuum.

| | HP spin S (d = 2S+1) | truncated oscillator (d levels) |
|---|---|---|
| [C⁺, C⁺^K] (∝ Q²) | (n_T − n_L)/S; norm on N ≤ 2: 1.0, 0.5, 0.25 at d = 5, 9, 17 | d(P_top,T − P_top,L); **0 on N ≤ 2** |
| Krein inertia of V_N | **positive non-null vector at every even N ≥ 2**, Gram value 1/(4S−1) exactly (0.1429, 0.0667, 0.0323 at d = 5, 9, 17); odd N null | **all levels 1 ≤ N ≤ d−1 null**; V_N = 0 for N ≥ d |
| physical quotient | vacuum **plus** spurious positive-norm 2-, 4-, … quantum unphysical states | **vacuum only (exact, positive)** |
| leak ‖[C⁺, φ] on V_N‖ under a conserved-source coupling φ = (A_L + A_L^K) − (A_T + A_T^K) (CCR: 0) | 1/S on V₁ (0.5, 0.25 at S = 2, 4), growing with N | **0 for N < d−1**; nonzero only on the top level (1.77 at d = 5, 0.80 at d = 9) |

- **Reading.** With HP slots, Gupta–Bleuler fails at O(1/S): extra positive-norm states, so "exactly two" fails in multi-quantum sectors, plus a 1/S leak. This matches the registered expectation, except that the norm does not turn negative in this toy. With truncated oscillators and *decoupled* modes, Gupta–Bleuler is exact below the top level.

### 3.7 With local lattice dynamics, the Gupta–Bleuler space is empty at finite d (checked, small; s4)

**Model.**
- A 3-site ring with mass m = 1 and two fields: φ_L (metric +) and φ_T (Krein, wrong-sign action, positive frequency).
- Truncated d-level slots and a local nearest-neighbour H. H is Krein-self-adjoint, residual 0.
- Positive-frequency parts are the CCR Bogoliubov annihilators b_X(k) built from the truncated slot operators.
- The constraint is D_k = b_L(k) − b_T(k), which is null with CCR.

| d | Hilbert dimension | dim V = dim ∩_k ker D_k | min singular value of stacked {b_L(k)} (exact Fock vacuum?) | best joint approximate vacuum residual |
|---|---|---|---|---|
| 2 | 64 | **0** | 0.391 (none) | 0.553 |
| 3 | 729 | **0** | 0.121 (none) | 0.171 |
| 4 | 4096 | **0** | 0.109 (none) | 0.154 |

- **Scan on a 2-site ring (checked, s4b; ω computed from the actual lattice M; the L = 3, d = 2 row reproduces s4 exactly).**
  - dim V = **0** for every d = 2..7, at both m = 1 and m = 0.3.
  - The best approximate Gupta–Bleuler residual, the smallest singular value of the stacked D:
    - m = 1: 0.349, 0.116, 0.081, 0.036, 0.018, 0.0084;
    - m = 0.3: 0.204, 0.169, 0.115, 0.073, 0.044, 0.026.
  - That is roughly ×0.52 and ×0.63 per level from d = 3 to 7: consistent with exponential decay, with the rate not derived.
- **Reading.** With local dynamics, the positive-frequency parts mix raising and lowering slot operators. Then no exact physical state exists at any tested d: a Gupta–Bleuler analogue of Lemma J, checked only on 2- and 3-site rings.
- Approximate physical states exist, with a residual that decays roughly exponentially in d. This residual measures how well a single state satisfies the weak condition. It is not the leak rate under dynamics, which was not computed.
- **Single-mode fact (proved).** On one truncated slot, u A + v A^K with u, v ≠ 0 has a one-dimensional kernel iff d is odd (top-row recursion). So the d = 3 emptiness above is a multi-mode effect, not parity.
- **Not shown:** emptiness for general L, d, m, or a proof.

### 3.8 Sources inside the weak condition: exactly impossible, approximately trivial (proved; checked, s3b)

- **Exact statement.** A strict positive-frequency operator on a finite space is nilpotent. So (C⁺ − ρ)ψ = 0 with ρ ≠ 0 has only ψ = 0 (proved).
- **But the obstruction is immaterial.** The best approximate solutions have residuals 2.5e-46 (HP, d = 17, ρ = 0.1) and 3.7e-21 (truncated, d = 17, ρ = 1). These are truncated coherent states.
- I record it so that it is **not** used as a no-go.

---

## 4. (b) Physical spectrum and norm

- **Where Gupta–Bleuler can work at all (checked, s5(b)).** In the N-type's 6 spatial slots (temporal gauge), no cubic per-slot metric (η_diag, η_off) ∈ {±1}² makes the local vector constraint null. ‖G η Gᵀ‖ = 0.036 to 3.99 at three momenta, for every sign choice. Gupta–Bleuler needs the lapse and shift slots: the covariant 10-component h_μν (comparator: Gupta–Bleuler in temporal gauge fails for QED as well).
- **Covariant CCR, one particle (checked, s5(a)).** The DeWitt/Feynman-gauge one-particle metric has inertia (6, 4). At lightlike lattice k = (|q̂|, q̂), for four momenta including the zone interior:
  - the de Donder subspace is 6-dimensional with Krein inertia **(2, 0, 4)**;
  - the 4 gauge modes k_(μξ_ν) lie in it and are null (≤ 3.6e-15);
  - the positive part is the spatial TT pair, Gram (1, 1).
  
  So **exactly two positive helicity-±2 states, on the full lattice zone**, at CCR (comparator reproduced).
- **Finite slots.**
  - HP: spurious positive-norm states at O(1/S) (§3.6).
  - Truncated, decoupled: exact below the top (§3.6).
  - Truncated with local dynamics: no exact physical space (§3.7).
  - No finite-d 3D covariant computation was run. Its Hilbert space is d^{10·V}.

## 5. (c) The 1/r pull

- **CCR covariant (checked, s5(a)).** The Feynman-gauge propagator numerator for static T⁰⁰ is P^{00,00} = ½ > 0, giving an attractive 1/q̂² (comparator: GR's ½). It plays the role of the N-type's −g|ρ|²/(4k²) (`N0914:290-296`).
- **Mechanism.** The negative-norm trace and lapse components supply the attraction that the indefinite conformal mode supplies in the N-type (reading; `R15-5:201-202`).
- **Finite slots.**
  - The literal sourced weak condition has no exact solution (§3.8), but approximate solutions are excellent.
  - The physical way (background plus a homogeneous weak condition) needs an exact or controlled physical space on local truncated slots, which §3.7 did not find.
  - **No finite-S 1/r is established.**

## 6. (d) The S needed, and the ghost-slot price

- **HP.** Every Gupta–Bleuler/BRST defect found is O(occupation/S) (§§3.3, 3.6). R19-22's conditional table applies unchanged (`R19-22:233-237`; ε ~ 1/S: S ≥ 1e15 for 1e-15; not recomputed).
- **Truncated, scenario only (suggested; s6).** Assume the defects act with the per-slot top-level weight of the CCR lattice vacuum. For the 3D massless field in its optimal local basis:
  - ν = 0.5213, n̄ = 0.0213, tail ratio λ = 0.0209 per level.
  - Then d ≥ 9 for 1e-15 (GW170817 speed) and d ≥ 61 for 1e-102 (the (m_g a)² bound, from `R19-22:223`).
  - With 10 covariant slots per cell, that is 40–60 qubits per cell.
  - **This is conditional:** §3.7 shows no exact physical space with local dynamics, and the leak rate has not been derived.
- **Ghosts.** Free Gupta–Bleuler needs none. A Kugo–Ojima BRST for the 4 vector gauge parameters needs 4 complex ghost pairs (c^μ, c̄_μ), i.e. 8 fermionic modes per cell. That is 8 qubits per cell plus a local fermion encoding (comparator: local encodings such as Verstraete–Cirac add qubits). With Lie closure (§3.2) or c-polarization (§3.1) the ghosts buy nothing.

## 7. (e) Prices (named, never adopted)

| Price | Axiom touched | Buys |
|---|---|---|
| **P-r19-25a**: an indefinite (Krein) metric on the site space; negative-norm possibilities | Qubit `AX:47`, read with its Hilbert structure; Admissibility `AX:60-61`, since "probability distribution over the possibilities" fails on negative-norm states and probabilities exist only on the physical quotient; Record `AX:79-83`, since only quotient states can be locked and read | the only route that escapes Lemma J and Proposition C at the vacuum level (§§3.4–3.6) |
| **P-r19-25b**: lapse/shift slots, 10 tensor slots per cell instead of 6, 4 of them negative-norm (signature (6,4), s5) | Qubit `AX:47`, Lattice `AX:37`, or blocking | Gupta–Bleuler nullness (§4) |
| **P-r19-25c**: a weak physical-state rule (Gupta–Bleuler or BRST cohomology) as law-level state selection | not in the axioms (`AX:92-95`: a state is a configuration of records); sharpens P-r15-5b (`R15-5:259`) | removal of the partner modes without exact constraints |
| **P-r19-25d**: fermionic ghost slots per cell (8 modes) | Qubit `AX:47` (extra fermionic factors) | a nilpotent charge, only in the excluded covariant class (§1) |
| P-N1 (unchanged) | Qubit `AX:47` | every *exact* construction found here is CCR (s5) |

The matter side is unchanged: universal coupling still needs a conserved symmetric stress (Lemma T, P-r15-5c).

---

## 8. Readings against the FIXED clauses (`TESTS:8349-8352`)

- **WEAK-ESCAPE: no.**
  - No finite-S construction has a positive-norm physical space with exactly two light-like helicity-±2 branches and a 1/r pull, checked.
  - The exact successes are the CCR covariant one-particle space (s5) and the *decoupled* truncated quartet (s3), and the second is not local lattice dynamics.
  - With local dynamics on truncated slots, the physical space is empty at every tested size (s4: L = 3, d ≤ 4; s4b: L = 2, d ≤ 7).
- **WEAK-OBSTRUCTED: no.**
  - It needs a refereed, class-wide demonstration. These are no-go candidates for the referee:
    - §3.1, BRST in 𝔅_c: H⁰ = strong kernel = 0 by Lemma J;
    - §3.2, Lie-closure BRST: zero cohomology in all degrees and polarizations;
    - §3.5, Lemma K and (K1)–(K3): exact nullness slot by slot, no CCR-type cross-slot cancellation, Kugo–Ojima Q² ≠ 0;
    - §4: the 6 spatial slots admit no null vector constraint.
  - None of these covers approximate Gupta–Bleuler with a stated residual on truncated Krein slots, or BRST built on lapse/shift plus Nakanishi–Lautrup slots.
- **OPEN: yes.**
  - **Decisive missing item:** a covariant 10-slot truncated Krein model with local dynamics. It should give either
    - a controlled approximate physical space, with the leak rate derived as a function of d, two TT branches and a 1/r background, or
    - a proof that the Gupta–Bleuler space is empty (or the leak is O(1)) for every d.
  - §3.7's ring is the first data point for the second outcome.
- **Expectation check** (`TESTS:8353`: WEAK-OBSTRUCTED; Q² ≠ 0 and the condition not preserved at O(1/S)).
  - **Confirmed for HP slots:** Q² ∝ occupation/S, leak 1/S, spurious states of norm 1/(4S−1).
  - **Sharper for BRST than expected:** the physical space is exactly empty, not O(1/S)-leaky.
  - **Softer for truncated slots:** the defects sit on the top level, not at O(1/S). The open question there is local dynamics, not closure.
  - **Not observed:** "norm turns negative" did not occur in any toy.

## 9. Strong-word check and scope

- **"Proved"** is used for:
  - §3.1 (any structure functions, c-polarization, HP constraints as the c-linear part);
  - §3.2 (via RECALLED Whitehead and Künneth, plus the refereed Lemma J ranks);
  - §3.3's identity;
  - Lemma K and (K1)–(K3) (finite slots, sums of single-slot operators, any Krein metrics);
  - the nilpotency statement of §3.8;
  - the single-mode parity fact.
  
  All are unrefereed.
- **"Checked"** is used for s2–s6 (including s3b and s4b) and the four 0-diff rechecks. s4/s4b are 3-site (d ≤ 4, m = 1) and 2-site (d ≤ 7, m = 1 and 0.3) rings only.
- **"Suggested"** is used for the §6 scenario arithmetic.
- **"Empty"** in §3.7 means dim ∩_k ker D_k = 0 at the tested sizes. It is not a theorem.
- **"Exactly two"** is claimed only at CCR (s5, one-particle). It is never claimed at finite S.
- **"Every"** in §3.5 means every slot of a sum of single-slot operators. Multi-slot positive-frequency parts are excluded.
- **Not covered:**
  - interacting or emergent phases;
  - modular aliasing (R17-1);
  - a finite-d 3D covariant model;
  - matter coupling beyond the toy φ;
  - nonlinear gravity;
  - Λ;
  - readout bridges (`vR16-7:5`).

## Files (`S/`)

- `scripts/s2_brst_finite.py/.out`:
  - the naive Q² identity and norms (toy);
  - Chevalley–Eilenberg cohomology for su(2) and su(2)⊕su(2);
  - the c-polarization kernel toy.
- `scripts/s3_gb_quartet_krein.py/.out`: the Krein null pair, HP versus truncated (nullness, V_N inertia, leak); the Lemma K partial-trace check.
- `scripts/s3b_pseudospectrum.py/.out`: approximate sourced solutions.
- `scripts/s4_ring_gb_bogoliubov.py/.out`: Gupta–Bleuler with local dynamics on a 3-site truncated Krein ring (V = 0).
- `scripts/s4b_ring_scan.py/.out`: the same on a 2-site ring for d = 2..7 and m = 1, 0.3 (V = 0; approximate residuals), plus the L = 3 consistency row.
- `scripts/s5_covariant_onepart.py/.out`:
  - covariant de Donder Gupta–Bleuler at CCR, one particle (inertia (2, 0, 4)), and the T⁰⁰ numerator ½;
  - 6-slot non-nullness.
- `scripts/s6_slot_tail.py/.out`: the per-slot vacuum tail and the scenario d.
- `recheck/`: R19-22 s2, s3, s6 and R15-5 s1, all 0-diff.
