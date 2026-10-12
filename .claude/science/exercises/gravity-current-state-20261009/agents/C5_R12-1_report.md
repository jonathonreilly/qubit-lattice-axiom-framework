# C5 R12-1: graviton production beyond the linear constraint — a lattice hypersurface-deformation algebra at O(κ²) with finite-site matter

**Worker.** Claude Opus 5.5, the same model family as every C5 worker and the supervisor. Ran 2026-10-12 from 19:06Z to about 19:30Z. **Unrefereed.** No repository file was edited. Scripts and outputs are in `scratchpad/C5/R12-1/scripts/`; each run takes under 2 s on 2 threads.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `N0930` = `docs/FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-30.md`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full.
- `vR11-2` = `scratchpad/C5/ref_R11-2/REFEREE_VERDICT.md`. That referee verdict appeared during this run.
- Bare `TESTS` and `SUMMARY` refer to files in `P/`. The R12-1 registration is at `TESTS:4334-4348`.

**Labels.**
- **proved:** derived here; unrefereed.
- **checked:** computed numerically here.
- **suggested:** an argument, not a proof.
- **reading:** an interpretation.
- **comparator:** literature. V means verified on the web in this run; RECALLED means from memory.

---

## 0. Plain words

- **The question.** R11-2 found that if gravity's constraints are kept exactly linear and fed by matter's energy, matter cannot move (its X2). The proposed way out was the nonlinear, non-abelian constraint algebra of real gravity. Can a lattice constraint system close that algebra at the next order, O(κ²), with mobile finite-site matter?
- **What I found: on box states, the matter part closes.**
  - At O(κ²), the only thing the algebra demands of matter is that its global charges obey the exact Poincaré rules. These charges are energy, momentum, boost and rotation, i.e. the zeroth and first moments of its energy and momentum densities. That is necessary and sufficient (Theorem K, proved).
  - Everything else can be absorbed by gravity-dependent correction terms in the constraints, chosen explicitly.
  - R7-1's box matter has exact Poincaré rules on box states. So the O(κ²) matter brackets close there, with explicit quasi-local corrections (proved; checked).
  - The plain lattice fails in exactly the places C3 found.
- **The corrections are load-bearing.** Without them the local algebra fails even for box matter. The failing pieces are its higher-moment parts: the (2,1) jet is 0.11 to 0.35 (checked). That answers R7-1's open item W4.
  - Lemma F's freezing (X2) assumed constraints that are exactly linear, with no such corrections. With them, freezing does not follow.
  - The R11-2 referee independently found X2 not general (`vR11-2:11,15`).
- **The algebra forces one light cone.** Matter and graviton share one structure function, so the graviton's speed must equal matter's speed at tree level (proved at the Killing level).
- **What fails off the box.** The global-moment defect: the cos k factor, i.e. the edge anomaly with zone mean −1.
  - Correction terms with smooth (local or quasi-local) kernels cannot absorb it. Neither can any c-number deformation of the structure functions.
  - Correction terms with kernels singular at zero smearing momentum, of homogeneous degree −1, can absorb it. In real space these are power-law couplings of order 1/r^{d−1}: Coulomb-type non-locality (proved by degree counting; checked: the needed correction grows like 1/t).
- **What is not done: gravity's own O(κ²) sector.**
  - This is the graviton's cubic self-interaction: N0930's mixed identity and its companions.
  - Its necessary identity, which N0930 proved impossible for finite-support kernels, holds exactly on the box when the graviton's momentum symbol is the box symbol (checked; residual 4e-13 on box packets, 4.8 on edge packets).
  - The free-field reduction holds for a scalar proxy (checked).
  - The full six-component tensor completion was not built.
- **Reading: INCONCLUSIVE.** It is not PASS: the gravity-bilinear sector is not constructed, and the graviton is the supplied CCR comparator, not a qubit graviton. It is not FAIL: there is no no-go, and the evidence points the other way on box states.

---

## 1. Hypotheses (stated before titles) and excluded outside realizations

**H-grade (the meaning of "O(κ²)").** Give gravity fields (h, E) field degree 1 and give matter bilinears degree 2.
- Write C = C₁ + C₂ + C₃ + … by degree:
  - C₁ is the linear constraint (S = tr R(h), G = d·E);
  - C₂ contains matter's T₀₀ and P (degree 2) and the gravity quadratic densities (T2, G2);
  - C₃ contains completions: matter-bilinear × gravity-linear terms, and gravity-cubic terms.
- A bracket {C_a, C_b} has degree a + b − 2. Closure "to O(κ²)" means closure at degrees 0, 1 and 2.
- R11-2's [C_x, C_y] = κ²[ρ_x, ρ_y] (`C5_R11-2_report.md:213-221`) is the degree-2 matter term. So R12-1's O(κ²) is degree 2.
- At degree 2 the identity splits into a matter-bilinear sector and a gravity-bilinear sector. Mixed terms such as {T₀₀, completion} have degree 3.

**H-grav (the gravity side; the supplied comparator, price P-N1 of `C5_R11-2_report.md:256`).**
- R9-9's box graviton (`TESTS:3939-3950`): N0914's staggered tensor stencils with the derivative symbol replaced by a smooth, non-analytic box symbol. On the box this symbol equals q, and with the midpoint phase it vanishes only at q = 0.
- Gravity fields are CCR pairs (continuous canonical variables), not qubits.
- Degree 0 ({C₁, C₁} = 0) is R9-9's exact linear algebra.
- Degree 1 is the gravity seed {C₁[N], T2[M]} − (N↔M) = G₁[F₀(N, M)] (N0930:69-75, F0 at :74; the 09-24 β = −α note). §5 says what is and is not checked for the box symbols.

**H-mat (matter).** R7-1's free box fermion (`C5_R7-1_report.md:61-70`):
- one fermion mode per site of Z^d, a finite-site carrier (the qubit form is R9-5's vortex-free sector);
- number-conserving, with no sea;
- symbols s(k) = ρk + (1 − ρ) sin k and ε̃ = √(m² + Σ s(k_i)²), with plateau |k_i| ≤ b = 2.0;
- densities with midpoint (first-moment) placement: ⟨k+p|T₀₀[e^{ipx}]|k⟩ = ½(ε̃(k+p) + ε̃(k)) and ⟨k+p|P_j[e_j e^{ipx}]|k⟩ = ½(s_j(k+p) + s_j(k)).

Second quantization of number-conserving bilinears is an exact Lie homomorphism with no c-number term. So one-body symbols decide every degree-2 matter bracket, at every particle number.

**H-comp (completions).** The degree-3 terms are matter-bilinear × (h-linear or E-linear) terms with arbitrary symbols:
- T₀₀^{(1,h)}, T₀₀^{(1,E)}, P^{(1,h)}, P^{(1,E)}.
- **Regular** means C^∞ in all momenta: super-polynomially quasi-local kernels, the box price.
- **Singular** means anything else.

**H-SF (structure functions).** At degree 2 in the matter sector, structure functions are c-numbers (C3's Lemma 1, `RC_C3_report.md:25-33`, refereed). A structure function depending on h or on matter produces degree-3 terms. The undeformed flat hypersurface-deformation algebra (HDA) is the default, with conventions fixed below. A common c-number deformation is allowed (Bojowald-type β at flat background; comparator, §8).

**Domain.** "On the box domain" means acting on finite-particle states whose one-body momenta lie in the open plateau (the R7-1 box). Intermediate momenta are unrestricted.

**Excluded, and not covered by anything below:**
- pair-creating matter, except the scalar-proxy remark in §5;
- interacting matter (§4.4 is suggested only);
- degree ≥ 3, i.e. field-dependent structure functions and O(κ³);
- the full six-component gravity-bilinear sector;
- qubit gravity (R11-2/X1 territory);
- Λ;
- d = 1, where gravity has no gate (§6).

## 2. Prior art (each counted once)

1. **RC C3** (`TESTS:1207-1229`; `agents/RC_C3_report.md:25-80`; referee `agents/RC_C3_referee.md`). At the flat matter-bilinear order with the 09-14 stencils:
   - completions drop out of the Killing sectors (constant shift, affine lapse, rotations);
   - closure needs Hess(ω²/2) to be constant, which is impossible for periodic bands;
   - the certificate is the first Taylor coefficient (`RC_C3_report.md:66`).

   C3 proved necessity in the Killing sector. **My Theorem K adds the converse:** the Killing sector is the *only* condition at this order.
2. **R7-1** (`C5_R7-1_report.md:87-131`, Lemma L and Theorem P1): Poincaré relations are exact on the box domain. W3, the affine sector, is closed there; **W4, the local lapse, is OPEN** (`:205-213`). This probe answers W4 for free box matter.
3. **R11-2 Lemma F and X2** (`C5_R11-2_report.md:211-251`): exact linear sourced constraints force commuting densities. The O3 outside route is "O(κ²)-deformed constraint algebras" (`:48`). The referee confirmed the algebraic core and found X2 not general (`vR11-2:11,15`).
4. **N0930** (`N0930:1-8,97-107,180-215`): the finite-support canonical tensor seed fails its degree-two mixed identity, because z(tr D)′ = 2μ₁ has no Laurent-polynomial solution (eq. (4), `:213`). Its "finite support" hypothesis is `:103`. Its controls name D = log z as the formal (non-single-valued) solution (`:236-240`).
5. **R9-9** (`TESTS:3939-3950`): the box graviton is exact at tree level, with Ward coupling to number-conserving box stress. Theorem T: loops carry the edge anomaly into c_T.
6. **K2** (`agents/C4_K2_report.md:18-20`): on Z⁴ the O(κ²) Killing-sector closure fails for strictly local matter. **RFW** (`SUMMARY:520-532`; F2 referee): the constant-translation jet is the obstruction for finite-range h,φ completions. **RN L3** (`agents/RN_L3_referee.md:5`): a pointwise lapse constraint freezes T₀₀.
7. **R7-4** (`agents/C5_R7-4_referee_verdict.md:9-23`): universality and γ = 1 at linear order need equal couplings and a common matter–graviton cone. My §4.3 derives the common-cone condition from the degree-2 algebra.
8. **SUMMARY §17** (`:355-494`, the boost wall). Every refereed boost obstruction (C3, I1–I3, M1, K2, F1, V3) is a global-moment (Killing-sector) statement. That matches Theorem K's location of the obstruction. The "one obstruction" synthesis there is a reading.
9. **Outside view** (`OUTSIDE_VIEW.md:42`) cites Bahr–Dittrich (V there). The C4 B1 referee (`agents/C4_B1_referee.md:17`) notes that Bojowald's holonomy deformation is trivial at flat background (β = 1), while inverse-triad factors are not.

## 3. Theorem K: Killing reduction at degree 2 (proved; for any d ≥ 2)

**Setting.** H-grade, H-SF and H-comp. Gravity gauge actions:
- E → E + Sᵀ N, with symbol s(p) = d̂ ⊗ d̂ − |d̂|² I;
- h → h + Gᵀ ξ, with symbol Kill(p)ξ = d̂ ⊗ ξ + ξ ⊗ d̂;
- d̂ = R9-9's staggered box symbol, vanishing only at p = 0 on the torus (H-grav).

Matter densities T₀₀ and P are quasi-local, with C^∞ symbols.

**Statement.** With regular completions, the matter part of each degree-2 bracket closes iff the following **Killing jets** vanish on the domain:
- **{C_s, C_s}:** the Taylor part of bidegree ≤ (1,1) in the two lapse momenta (p, p′). This gives {H, H} = 0, {H, K_b} = P_b and {K_a, K_b} = J_ab, all with the HDA's c-number structure function.
- **{C_j, C_s}:** p_ξ-order 0, and the antisymmetric p_ξ-order-1 part, each to lapse order ≤ 1. This gives {P, H} = 0, {P_c, K_b} = δ_bc H, {L, H} = 0 and {L, K} = K.
- **{C_j, C_j}:** translation and rotation jets in both slots. This gives {P, P} = 0, {L, P} = P and {L, L} = L.

These are exactly the Poincaré relations of the global charges.

**Proof.**

1. **The brackets decouple.**
   - {C_s, C_s} receives completions only through T₀₀^{(1,E)}[M; E → SᵀN] − (N↔M). Its image is s(p)·τ(p′, p) − s(p′)·τ(p, p′).
   - {C_j, C_s} receives T₀₀^{(1,h)}[N; h → Gᵀξ] + P^{(1,E)}[ξ; E → SᵀN]. Its image is Kill(p_ξ)·A + s(p_N)·B.
   - {C_j, C_j} receives P^{(1,h)}. Its image is Kill(p)·A − Kill(p′)·A′.
   - The four completions are independent unknowns.
   - The right-hand sides at degree 2 are c-number structure functions × (T₀₀, P) (H-SF). Regular constraint mixing by matter-bilinear coefficients times C₁ has degree 3.
2. **Necessity.** s(p) = O(|p|²). Kill(p)ξ vanishes at p = 0, and its first-order part is the symmetrized gradient, which vanishes on rotations. So every image vanishes on the Killing jets, for any completion whose symbol is C² at zero smearing momentum. This is C3's certificate argument, generalized to all three brackets.
3. **Sufficiency, {C_s, C_s}.** Let D(p, p′) be the antisymmetric defect.
   - Set R(p, p′) = D − D(0, p′) − p·∂₁D(0, p′). By Hadamard's lemma R lies in the ideal of quadratics in p, for every p′ and k.
   - Set F₂(a, b) = D(0, b) + a·∂₁D(0, b). It lies in the b-quadratic ideal iff the jets (0,0), (0,1), (1,0) and (1,1) vanish.
   - Then G(p, p′) = ½[R(p, p′) − F₂(p′, p)] lies in the p-ideal, and D = G(p, p′) − G(p′, p) by antisymmetry.
   - The components s_ij(p) span all quadratic monomials near p = 0. Rank 3 of 3 for d = 2 and rank 6 of 6 for d = 3 (checked, script 1 (D)). Away from 0, s ≠ 0 and one divides.
   - A partition of unity gives a C^∞ τ with G = s(p)·τ. ∎
4. **Sufficiency, the Killing-operator ideal ({C_j, ·} brackets).** A vector symbol f(p)·ξ lies in {Kill(p)·A, A symmetric} near 0 iff f(0) = 0 and ∂f(0) is symmetric.
   - Write f_j = Σ_i p_i M_ij + Σ_il p_i p_l r_jil, with r symmetric in its last two indices.
   - Take A_ij = M_ij + Σ_l p_l (r_jil + r_ijl − r_lij). This is the Christoffel trick: A is symmetric and p·A = f.
   - The same Hadamard split as in step 3 then reduces {C_j, C_s} and {C_j, C_j} to their Killing jets. ∎
5. **Domain.** For the box, the jets vanish only for one-body momentum k in the plateau. Write the defect as (image) + Σ (monomials of bidegree ≤ (1,1)) × (Poincaré-defect operators). The second part annihilates box states. So closure holds as an operator identity on the box domain, not on all of Fock space.

**Corollary (singular completions).** If the Killing jets do not vanish, as on the NN lattice or off the box, degree counting gives the following.
- The completion needed to absorb the jet is homogeneous of degree −1 in the smearing momentum. For example, on the p_ξ = 0 slice, B = D(0, q)·s(q)/|s(q)|² with D = O(|q|).
- In real space that is a 1/r^{d−1} kernel coupling matter bilinears to E.
- So on the NN lattice, degree-2 closure is available at the price of a power-law non-local completion. This is the Coulomb-type, Marolf-type "kinematic non-locality" (`C5_R11-2_report.md:21`).
- Proved at this order. Consistency at degree 3 is not examined.

## 4. Box matter closes the degree-2 matter sector on the box domain (proved; checked)

### 4.1 Checks (`r121_matter_bilinear.out`)

**Conventions.** The structure functions were fitted from the (1,0) jet: σ = σ′ = σ″ = −1. That is the undeformed flat HDA with c = 1 in these conventions.

**Models.**
- "box": R7-1's law.
- "NN": the C3 comparator, ε² = m² + Σ(2 − 2cos k) with P symbol sin k.
- "naive": ε² = m² + Σ sin² k.

| d = 3 (d = 2 is the same pattern) | SS jets (00, 10, 01, 11) | JS jets (T q0, T q1, R q0, R q1) | JJ jets (TT, TR, RR) | SS non-Killing (2,1) jet |
|---|---|---|---|---|
| box, k in box | 0, 6e-12, 6e-12, 3e-8 | 0, 8e-12, 5e-10, 3e-9 | 0, 5e-12, 0 | **0.114** |
| box, k off box | 0, **7.0**, **7.0**, 2e-6 | 0, **7.7**, **2.7**, **2.2** | 0, **3.1**, 1e-13 | 11.3 |
| NN, k in box | 0, 8e-10, 8e-10, 9e-8 | 0, **1.3**, 1e-9, **0.15** | 0, **0.44**, 0 | 0.44 |
| naive, k in box | 0, **0.80**, **0.80**, 3e-8 | 0, **1.1**, **0.24**, **0.46** | 0, **0.67**, 0 | 0.44 |

- **Box, inside.** Every Killing jet is at finite-difference noise (≤ 1e-7).
- **NN.** This reproduces C3:
  - {H, K} = P is exact;
  - {P, K} fails (the cos k factor);
  - {L, K} and {L, P} fail;
  - {L, H} = 0 holds.

  This consistency check is prior art, counted once.
- **Required completion (script 1 (C), JS slice p_ξ = 0).** max|D|/|s(q)| along q = t·u, for t = 1e-1, 1e-2, 1e-3:
  - box, inside: 4e-14, 7e-13, 4e-10 (the defect is identically zero);
  - box, off box: 23, 254, 2559 (∝ 1/t);
  - NN: 3.6, 34, 333 (∝ 1/t).

  This is the degree −1 singularity of the Corollary.
- **Explicit SS completion (script 2 (E)).** max_q |G(t·u, q)|/t², for t = 1e-1 down to 3e-3:
  - box, inside: 0.107 to 0.113 (bounded, so τ is smooth);
  - box, off box: 4.3e2 to 4.8e5 (∝ 1/t²).
  - The decomposition identity D = G(p, q) − G(q, p) holds to 1.4e-17.
  - NN's SS completion is also bounded (0.25). NN's obstruction is in JS and JJ, not SS, consistent with C3.

### 4.2 Completions are load-bearing; R7-1's W4 answered

- Even on the box, the (2,1) jet of the lapse–lapse defect is nonzero: 0.35 (d = 2) and 0.11 (d = 3), checked.
- So the local Dirac–Schwinger algebra {T₀₀(x), T₀₀(y)} = (P(x) + P(y))∂δ fails for positive-energy, number-conserving densities. This confirms the suggestion at `C5_R7-1_report.md:212` for the box law.
- But the failure is non-Killing, so the E-linear completion T₀₀^{(1,E)} absorbs it (Theorem K).
- **W4 is closed at degree 2 on the box domain** (proved). It is not closed at degree 3.
- In d = 1 the gate s(p) is identically zero (no linearized curvature), so nothing can absorb the (2,1) jet. There is no 1+1 analogue (proved). This is irrelevant physically, but it shows the d ≥ 2 gravity structure is what makes closure possible.

### 4.3 One light cone is forced (proved, at the Killing level)

- The same c-number structure function multiplies the whole of C_j in {C_s, C_s} = C_j[F(N, M)]. So the gravity seed (degree 1, normalization c_g²) and the matter (1,1)/(1,0) jets (normalization c_m²) must agree: **c_g = c_m at tree level**.
- For box matter (c_m = 1 on the box) this requires R9-9's ω = |q| graviton. It is met by construction.
- This turns R7-4's "universality only by imposing a common cone" (`C5_R7-4_referee_verdict.md:73`) into a consequence of degree-2 closure. In the continuum this is the comparator fact that the HDA's structure function is one metric for all fields (Hojman–Kuchař–Teitelboim, RECALLED).
- Loops are not covered: R9-9's Theorem T and R11-1(b) concern one-loop shifts that run over off-box states (§6).

### 4.4 Lemma F / X2 and the physical sector

- **Outside X2's class (proved).** Our constraints are C_x = S_x − κρ_x − κ²Γ_x[E; matter] + (gravity terms). Lemma F's hypothesis C_x = S_x ⊗ 1 − κ 1 ⊗ ρ_x fails. On the kernel, [ρ_x, ρ_y]ψ is no longer forced to zero. Instead ([ρ_x, ρ_y] + κ⁻¹([S_x, Γ_y] − [S_y, Γ_x]) + F·P)ψ = O(κ), and Theorem K makes this vanish identically on box states.
- **Mobility (proved in R11-2's sense, `C5_R11-2_report.md:290`).** Closure at degree 2 imposes no condition on the box matter content. Any one-particle box wavepacket, for which [ρ_x, ρ_y] ≠ 0, is admissible. The flow of C_s[N] contains T₀₀[N], whose N = 1 part H_m = Σ ε̃ n_k transports box packets at k/ε.
- **Existence of the physical sector to O(κ²) (suggested).** This is the standard first-class perturbative argument: closure at degrees 0–2 is the integrability condition for an order-by-order dressing W with kernel(C) = W(kernel(S) ⊗ ℋ_box) + O(κ³). It is not written out. The dressing is non-local (Coulomb-type, as in QED's Dirac dressing). That non-locality is in the states, not in the law.
- **On a periodic torus,** Σ_x S_x = 0, so Σ_x C_x imposes a relational (closed-universe) Hamiltonian constraint H_m + H_g + O(κ) ≈ 0. That is the problem of time, not a freezing. On Z^d with fall-off, Σ S_x is the ADM boundary term instead (comparator, RECALLED).
- **Interacting box matter (suggested).** The proof of Theorem K uses bilinearity only to exclude c-numbers. For quasi-local interacting densities whose global charges obey Poincaré on a domain (R7-1 P2, R8-1), the same Hadamard split goes through with operator-valued symbols. Not checked.

## 5. Gravity's own sector at degrees 1–2 (partly checked; the full tensor completion is OPEN)

- **N0930's necessary mixed identity on the box (checked, script 2 (F)).**
  - Take the box momentum symbol D = iμ₁ s(K) I, with F = I/(4α) and A = 0.
  - Then D F + F D^♯ = 0 (s is odd), so μ₀ = 0, and [D, X] = μ₁ s′(K) = μ₁ on the box.
  - In real space on an L = 4096 ring: residual 4.0e-13 and 7.0e-13 for packets at k₀ = 0.8 and 1.7; 4.84 at the edge (k₀ = 2.6). The zone mean of s′ is 7e-16. The defect is parked at the edge with zone mean −μ₁ per component, the gravity-side twin of the matter −1.
  - N0930's hypothesis "finite support" (`:103`) is exactly what the box symbol drops. So N0930's theorem does not apply.
- **Free-field reduction (checked for a scalar proxy, script 2 (G)).**
  - The pair (a†a†) coefficient of the lapse-smeared energy density of a free field is (ω_q − ω_{q′})²/(8√(ω_q ω_{q′})), with q + q′ = p. This vanishes to second order at p = 0: c/t² is bounded at 0.08 and 0.43 for box, and 0.08 and 0.005 for NN.
  - So H, P and the boost K are number-conserving, and the graviton's Killing relations reduce to one-body identities, i.e. Lemma L on box Fock states (proved for the scalar proxy).
  - Non-Killing pair channels are then absorbable by gravity-cubic completions (Theorem K's argument; suggested for the tensor case).
- **Not done.** The six-component staggered tensor sector, i.e.:
  - the degree-1 seed with box symbols;
  - the full degree-2 gravity identities modulo linear constraints, with h-linear structure functions and midpoint phases.

  Without this sector, no PASS can be claimed.
- **Degree-1 seed, a remark (suggested).** With a box symbol, M(d²N) − N(d²M) = d·F₀ needs F₀(p, p′) = (|d(p′)|² − |d(p)|²)/d(p + p′). Its numerator vanishes on p + p′ = 0, so F₀ is smooth (Hadamard), and it equals p′ − p exactly on the box (1D). So a quasi-local F₀ exists. It agrees with the matter structure function at the Killing level; the differences are non-Killing and absorbable.

## 6. (b) What fails, and where

- **Off the box (proved and checked):**
  - The Killing jets, i.e. Hess(ε̃²/2) − I and j − P, are the edge anomaly (zone mean −1, R7-1 and C3).
  - No regular completion absorbs them (necessity).
  - No c-number structure-function deformation does either. A common β only rescales c (C3: "even with arbitrary constant deformations", `RC_C3_report.md:70-75`). The jets are not c-number multiples of H or P.
  - A Bojowald holonomy-type deformation is trivial at flat background (`agents/C4_B1_referee.md:17`).
  - Only singular (1/r^{d−1}) completions absorb them.
- **The lattice spacing (proved).** It produces no O(a²) defect inside the box. It enters only through the box size (the rapidity budget) and through the completions' quasi-locality: super-polynomial, not exponential, the box price (`C5_R7-1_report.md:128-131`).
- **Structure functions (proved).** They are undeformed at degree 2 on the box (β = 1). Field-dependent structure functions first enter at degree 3, which was not analysed.
- **Domain (reading).** Closure holds on box states, not as an operator identity on Fock space.
  - At degree 3, products of a constraint and a completion act on states already moved by p.
  - Vacuum loops sum over all modes.
  - So the edge defect can re-enter there. R9-9's Theorem T, the edge in c_T at one loop, is that re-entry for pair-creating matter.
  - The degree-2 algebra on box states does not protect the one-loop graviton speed.
- **d = 1 (proved).** There is no gate, and the local Dirac–Schwinger failure is not absorbable.
- **Pair-creating matter (suggested).** Free fields keep number-conserving Killing generators (§5), so the Killing jets reduce to one-body ones. Non-Killing c-number Schwinger terms would need c-number E-linear completions. Not checked.

## 7. (c) Do R7-1's box tricks help?

**Yes, at degree 2, on the box domain, for the matter sector** (proved and checked).
- The trick gives exactly the one thing degree-2 closure requires: Poincaré jets.
- The same trick lifts N0930's gravity-side obstruction, eq. (4), on the box (checked).
- The full gravity sector is not built.

## 8. Literature (comparators)

- **Dirac / Hojman–Kuchař–Teitelboim (RECALLED).** The HDA has structure functions h^{ij}. A minimally coupled scalar closes it (C3's continuum control reproduced this, `RC_C3_report.md:65,112`).
- **Bojowald et al. (V).**
  - Holonomy corrections deform the HDA, giving a signature change: Bojowald–Paily, arXiv:1112.1899; the algebroid treatment in arXiv:1610.08355 (PRD 94, 104032).
  - Self-dual variables keep the algebra undeformed, with the corrections moved into the diffeomorphism constraint (arXiv:1610.07467).
  - Transfer: at flat background the deformation is a c-number at most. Box matter needs none.
- **Bahr–Dittrich (V in the repo, `OUTSIDE_VIEW.md:42`; RC C3 referee).** Discretization breaks diffeomorphism symmetry away from flat backgrounds. Perfect actions restore it but are non-local. Transfer: our regular box completions are quasi-local, and the NN alternative is power-law non-local, consistent with them.
- **Gambini–Pullin consistent discretization (V, gr-qc/0512065).** The multipliers are fixed by consistency, so the discrete theory has no diffeomorphism constraints. Transfer: that is the price route (a preferred foliation, P11), not used here.
- **Thiemann QSD (RECALLED).** On-shell closure only.
- **Henderson–Laddha–Tomlin, arXiv:1204.0211 (V)**, the U(1)³ model: earlier anomaly freedom was on-shell, with a trivialization concern.
- **Tomlin–Varadarajan, arXiv:1210.6869 (V); Laddha, arXiv:1401.0931 (V); Varadarajan, arXiv:2205.10779 (V).** Off-shell closure on special state spaces ("habitats").
- **Transfer (reading).** Like these, our closure holds on a restricted state space (the box domain), not on all states.

## 9. Prices (named, never adopted)

| Price | Axiom touched | What it buys |
|---|---|---|
| P12-1. The box (smooth, non-analytic symbols; quasi-local, non-exponential completions; a frame-fixed box) | Admissibility's nearest-neighbour rule (`AX:57-61`), already priced by R6-1/R7-1 | degree-2 closure on box states |
| P-N1 (from R11-2). A supplied CCR graviton | Qubit (`AX:45-53`) | the gravity side |
| P12-2. On the NN lattice: singular, degree −1 completions (1/r^{d−1} couplings of matter bilinears to E) | Admissibility's nearest-neighbour rule | degree-2 closure without the box (consistency at degree 3 unknown) |
| P12-3. Matter–graviton common cone at tree level | none; forced by the algebra (§4.3) | — |

## 10. Readings against the FIXED clauses (`TESTS:4345-4348`)

- **PASS: not met.**
  - The matter-bilinear sector meets it on the box domain, explicitly, and checked.
  - The gravity-bilinear sector of the O(κ²) algebra is not constructed: only N0930's necessary identity and a scalar proxy were checked.
  - The graviton is supplied (CCR), not finite-site.
- **FAIL: not met.** No no-go is claimed. The degree-2 analysis points towards closure on box states.
- **Reading: INCONCLUSIVE**, with these sub-results:
  - (a) matter sector: closes at O(κ²) on the box domain with mobile finite-site matter (proved; checked);
  - (b) the failure is located entirely in the Killing jets (the edge anomaly). It is absorbable only by power-law non-local completions;
  - (c) yes, for matter, and for N0930's gravity-side identity.
- **Against the registered framing.** "Mobile matter needs non-abelian O(κ²)": the completed system is non-abelian ({C_s, C_s} ∝ C_j with a c-number structure function). What mobility actually needs is the degree-3 completion Γ plus Killing-exact matter. Non-abelianness alone does not suffice: the NN lattice is non-abelian too, and it fails.

## 11. Strong-word check and scope

- **"Closes":** only at degree 2, only in the matter-bilinear sector, only on box states, only for free number-conserving box fermions, with regular completions.
- **"iff" (Theorem K):** under H-SF and H-comp, for d ≥ 2, with gate symbols whose only zero is p = 0. Necessity needs completion symbols that are C² at zero smearing momentum.
- **"Forced" (common cone):** Killing-level, tree-level only.
- **"Only singular completions"** off the box: by degree counting at degree 2. Higher-order consistency is unknown.
- **Numbers:** finite differences with steps 1e-3 to 1e-5. The floors (1e-7 to 1e-12) are step-limited. All checks are at sample momenta (3 in-box and 3 off-box k per model, plus the rays).
- **No tail or decay clause** was registered. Completion decay is stated as a class property (C^∞ gives super-polynomial decay; degree −1 gives 1/r^{d−1}), not measured. No channel limit is subtracted.

## Files

- `scripts/r121_matter_bilinear.py` / `.out`:
  - (A) Killing jets for SS, JS and JJ (box, naive and NN; d = 2, 3);
  - (B) the non-Killing (2,1) jet;
  - (C) the required-completion ray test;
  - (D) rank of the quadratic ideal.
- `scripts/r121_completion_and_gravity.py` / `.out`:
  - (E) the explicit Hadamard SS completion and decomposition identity;
  - (F) N0930's identity with the box symbol on an L = 4096 ring;
  - (G) the scalar-proxy pair coefficient.

Sources (web, this run): [arXiv:1112.1899](https://ar5iv.arxiv.org/html/1112.1899), [arXiv:1610.08355](https://export.arxiv.org/abs/1610.08355), [arXiv:1610.07467](https://ar5iv.arxiv.org/html/1610.07467), [gr-qc/0512065](https://arxiv.org/pdf/gr-qc/0512065), [arXiv:1204.0211](https://ar5iv.labs.arxiv.org/html/1204.0211), [arXiv:1210.6869](https://arxiv.org/pdf/1210.6869), [arXiv:1401.0931](https://ar5iv.arxiv.org/html/1401.0931), [arXiv:2205.10779](https://arxiv.org/pdf/2205.10779).
