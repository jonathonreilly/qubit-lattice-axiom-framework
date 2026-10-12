# C5 R8-2 report: the edge-mode universality problem in box-confined Poincaré

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 15:38Z to 16:06Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R8-2/`. Script and output: `S/scripts/r82_edge.py`, `S/scripts/r82_edge.out` (about 3 min at `OMP_NUM_THREADS=2`).
**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `TESTS.md`: C5 method and round 1 (`:2302-2420`), rounds 7–8 (`:3240-3481`), lane RN (`:777-898`), lane RC (`:1093-1244`). `SUMMARY.md` §§12–20 and §23. `agents/C5_R7-1_report.md`, `agents/C5_R7-1_referee_verdict.md`, `agents/C5_R7-4_report.md` (unrefereed), `agents/C4_M1_referee.md`, `agents/C4_I1_referee.md`, `agents/C5_O2_report.md:120-140` and `agents/C5_O2_referee_full.md:132-135` (Lemma F). The R7-1 scripts.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED (from memory, not verified here).
**Comparator.** MICROSCOPE final result: η(Ti, Pt) = [−1.5 ± 2.3 (stat) ± 1.5 (syst)] × 10⁻¹⁵, Phys. Rev. Lett. 129, 121102 (2022) (arXiv 2209.15487). The companion paper gives 2.7e-15 with the errors combined (arXiv 2209.15488). Verified by web search this run. The registered bar is 1e-15.

---

## 0. In plain words

- **The edge can be made to gravitate.** I build a stress tensor for R7-1's law that covers every momentum on the grid, box and edge alike. It is exactly conserved, symmetric and quasi-local. Its total energy is the whole Hamiltonian, so all energy now pulls and is pulled the same way at first order. Inside the box it is exactly the continuum stress. Checked to 1e-15 in d = 2. This removes the referee's specific complaint that edge energy does not gravitate (`TESTS.md:3406`).
- **But the edge then falls the wrong way.** Universal coupling is not the same as universal free fall. A quantum of lattice momentum k in a uniform field falls with the anomaly Hess(ε²/2) − I at k. That is exactly the boost-wall anomaly. Its average over the zone is −1, so it cannot vanish everywhere (proved; checked by wavepacket fall). Edge quanta at rest fall with weights such as −30 ("falling up") or −2.2.
- **So the anomaly can be moved, not removed.** In R7-1 the edge carries energy and does not gravitate. With the new stress it gravitates and violates the equivalence principle. Neither choice is observable while nothing in ordinary matter sits in the edge, and in R7-1's class nothing does. The Eötvös contribution from edge modes is then exactly zero at first order, under every option.
- **A defect in R7-1's literal law.** Its "Planck-scale" edge contains 2^d − 1 light doublers of mass m at the zone corners. They are degenerate with the physical particle (checked: ε = 0.300000 at every corner). They are harmless only while no interaction reaches the edge. Option (b) removes them: the edge can be gapped up to the box-face energy √(m² + b²)/a, and no higher.
- **Option (c)** (non-periodic momentum space) is the same as I1's complete tower, i.e. a continuum in every cell. It passes trivially, at the price of the finite Qubit fibre.
- **The real block is interacting matter, and it is not about the edge.** By R7-4's argued flow theorem (unrefereed), any exactly conserved linear-order stress, universal or not, forces R7-1-type box-supported scattering to vanish in d ≥ 2. The suggested d = 1 extension to the bounded BT plateau is my own. So the equivalence principle for bound test bodies is not established in any exact linear theory of this class.
- **Against the FIXED readings.** Worker reading: **PASS WITH SCOPE** on the letter of the clause, for free matter at linear order. If the referee requires interacting test bodies, the strongest correct reading is **INCONCLUSIVE**. FAIL is not available in the registered sense, because §3.2 is an explicit counterexample to "universal coupling cannot hold with an exact box sector".

---

## 1. Hypotheses and class (stated before any title)

- **H-law.** R7-1's free law (`agents/C5_R7-1_report.md:63-71`): one CAR mode per site of Z^d, graded composition, continuous time. H₀ = Σ_k ε(k) n_k, with ε = √(m² + |k|²) on the box B = [−b, b]^d and smooth and periodic outside.
  - Literal profile: ε² = m² + Σ s(k_i)², with s = ρk + (1 − ρ)sin k.
  - Gapped profile (option b): ε² = m² + Σ u(k_i), where u = k² on the box and u′ = ρ·2k + (1 − ρ)·C sin k > 0 on (0, π).
  - Numerics: b = 2.0, b₂ = 3.1, m = 0.3 (R7-1 script 1).
- **H-int.** Interactions are number-conserving and box-supported (R7-1's BT law, `:73-81`). The vacuum is the empty Fock vacuum: no sea, no pair creation.
- **H-grav.** Linearized gravity couples as h_{μν}T^{μν}, with T^{μν}(q) = Σ_k F^{μν}(k+q, k) a†_{k+q} a_k.
  - The lattice divergence symbol D_j(q) is quasi-local.
  - **W1** is ω F^{0ν} = Σ_j D_j(q_j) F^{jν}, with ω = ε(k+q) − ε(k), and F symmetric and Hermitian.
  - "Universal" means F^{00}(k,k) = ε(k) on the whole torus, so ∫T^{00} = H.
  - "Linear order" means O(h), i.e. O(√κ) in the constraint algebra (as in `agents/C5_R7-4_report.md:58`).
- **H-EP.** The static field enters through the lapse, H → Σ_x (1 + Φ(x)) T^{00}(x). This is O2's Lemma F setting (`agents/C5_O2_report.md:120-126`). The Eötvös η of a body is read sector-additively, as in O2's channel bounds: η ≈ |Δf_edge|·|Ā_edge|. This reading is O2's, SUGGESTED per `agents/C5_O2_referee_full.md:132-135`.
- **Excluded, not addressed:**
  - pair-creating QFT and loops (R7-5);
  - gauge fields;
  - N ≥ 3 interacting sectors;
  - the local-lapse algebra W4;
  - the graviton's own nonlinear terms;
  - ungraded ⊗M₂ realizations;
  - set B (Z⁴);
  - LRL and quasicrystal "non-periodic" momentum spaces.

## 2. Prior art (each counted once)

- **R7-1 and its referee.**
  - The PASS WITH SCOPE came through free P1 alone (`TESTS.md:3398-3407`).
  - W1 holds only on the χ = 1 subbox, where ∫T^{00} = Σχ²εn ≠ H₀ (`C5_R7-1_referee_verdict.md:223-235`).
  - "inert non-gravitating edge modes violate universal gravitational coupling" (`:212-219, :275`).
  - The box subspace is invariant under the pair Hamiltonian (`:50-58`).
- **I2/C3.** A periodic C² band has zone-averaged Hess(ε²/2) − βI = −β (`SUMMARY.md:403-405`; `TESTS.md:1211-1213`).
- **I1.** Exact closure needs "an infinite-dimensional, unbounded one-particle fibre" (`C4_I1_referee.md:15,21`).
- **O2, Lemma F (conditionally DERIVED).** At a stationary band minimum ẍ = −Hess(E_B²/2)∇Φ. "C3/I1/M1 need Hess(E²/2) = βI … The EP tests that condition at k = 0" (`C5_O2_report.md:120-131`; `C5_O2_referee_full.md:132`). **The fall law and its link to the boost anomaly are O2's.** §3.3 extends them to every k as an operator identity, and adds the zone mean.
- **O2, Lemma S.** Exact translations are incompatible with finite, uniformly site-tied fibres (`C5_O2_referee.md:15`).
- **RN L1 and R7-4 §2.** Free species carry exact local stresses. Universality is not forced for free species, because a_s is a free parameter (`C5_R7-4_report.md:71-75`). **So the free-matter universality in §3.2 is a choice, the named tuning T2, not a consequence.**
- **R7-4 §4 (unrefereed).** Lemma 1: an exact linear bridge gives i[H,D] = J and [H,J] = 0. Lemma 2: S commutes with the free first-moment flow. Corollary: "every box-supported construction … cannot feed the bridge" (`C5_R7-4_report.md:123-186`).

---

## 3. Results

### 3.1 Finding D: R7-1's literal edge holds 2^d − 1 light doublers. Proved (elementary); checked

- **Proof.** s is continuous, odd and 2π-periodic, so s(π) = −s(−π) = −s(π), hence s(π) = 0. Then ε(k) = m at every corner with k_i ∈ {0, π}.
- **Check** (`r82_edge.out`, part A): ε = 0.300000 at (π,0,0), (π,π,0) and (π,π,π). The minimum edge energy is 0.3000 in d = 2 and d = 3.
- **At rest these doublers fall correctly.** Hess(ε²/2) = s′² + ss″ = 1 at π, because s = sin k there. Checked: a/g = −0.99623 against −0.99654 at k = 0 (part D).
- **Away from rest they do not.** Near π the anomaly is A = cos 2k − 1 ≈ −2δk².
- **Consequence.** R7-1's "Planck-scale edge" (`C5_R7-1_report.md:225`) is not Planck-scale in energy. It holds light species that are kept out only because every interaction is box-supported. R7-1 §5.6 already notes that any lattice gauge coupling would reach them. This is the fermion-doubling problem in this law's clothing.
- **The fix is option (b), §3.4.** For Dirac matter it needs a Wilson-type momentum-dependent mass equal to m on the box (suggested; Nielsen–Ninomiya as comparator, RECALLED).

### 3.2 Construction A (option a): a universal, exactly conserved stress on box ⊕ edge. Proved; checked

**The kernel.**
- On box pairs with small transfer, F is the continuum on-shell kernel: F_c^{μν} = [k′^μk^ν + k^μk′^ν − η^{μν}(k′·k − m²)]/(2√(ε′ε)).
- Everywhere else, F is a "dust" kernel: F_d^{μν} = F^{00}_d u^μu^ν, with F^{00}_d = ½(ε(k′) + ε(k)) and u = (1, Δ(k,q)).
  - Δ_j is the staircase-symmetrized divided difference, Δ_j = [Σ over the two staircases of the ε-increment along j]/(2D_j(q_j)). It obeys Σ_j D_j Δ_j = ω identically (telescoping).
- The glue: F = φF_c + (1 − φ)F_d.
  - φ = χ₁(k)χ₁(k′)η(q) is real and symmetric.
  - χ₁ = 1 for |k_i| ≤ 1.6 and 0 beyond 1.9, inside the exact box.
  - η = 1 for |q_i| ≤ 0.5 and 0 beyond 0.9.

**Why it is conserved and symmetric (proved).**
- W1 is linear and pointwise in (k, q). F_c satisfies it with D = q, an algebraic identity (`C5_R7-1_report.md:199-202`), and D = q on supp φ.
- F_d satisfies it for any D. The ν = 0 component is Σ_j D_jF^{j0} = F_d^{00}Σ_j D_jΔ_j = ωF^{00}. The ν = i components are Σ_j D_jF^{ji} = F_d^{00}Δ_iω = ωF^{0i}.
- Both kernels are symmetric in μν, so the blend is too.
- **Hermiticity** needs D(q)* = −D(−q). That holds for D = s_c + iψ with s_c odd and ψ even, and for D = q on supp φ.
- **Forward values.** Everywhere, F(k,k) = ε(1, v)(1, v)^T with v = ∇ε. So ∫T^{00} = H (box plus edge), and ∫T^{0i} = Σ ε∇ε n_k = J_E is the total energy current. On the box this is k, R7-1's momentum.
- **First moment.** The first moment of T^{00} is ½{X, ε}. F^{00} is real and symmetric, so the Weyl term Y = 0. On 𝒟_B this is R7-1's K exactly. So **P1's whole algebra (`C5_R7-1_report.md:96-109`) now consists of integrals of a universal stress.** The R7-1 referee's χ = 1 restriction on W1 no longer applies.

**The divergence symbol.**
- D(q) = s_c(q) + iψ(q), a generalized forward difference. Here s_c = q on |q| ≤ 1, and ψ = (1 − ρ)(1 − cos q) vanishes on |q| ≤ 1.
- **D vanishes only at q = 0.** Checked: min |D| = 0.0503 over |q| ≥ 0.05, and max |D − q| = 4.4e-16 on |q| ≤ 1. The graviton's |D|² then has no zone-boundary zero, so there are no graviton doublers.
- **The real odd symbol D = s used in R7-1 does not work as is.** It vanishes at q = π, so the divided difference diverges there (checked: |Δ| ~ 1e16 within 0.05 of π). It works only if T is switched off near q ≈ π. Then the graviton doublers that s creates decouple from matter (suggested).

**Checks** (`r82_edge.out`, part B; d = 2; 4000 random pairs per set; both profiles):

| set | Ward residual (max abs) | Hermiticity | μν symmetry |
|---|---|---|---|
| random (k, q) on the torus | 1.9e-15 / 2.0e-15 | 2.5e-12 / 6.5e-14 | 9e-16 |
| box pairs, φ = 1 (continuum kernel) | 1.8e-15 / 1.7e-15 | 7e-16 | 0 |
| box → edge across the face | 8.9e-16 / 4.4e-16 | 4e-13 | 2e-16 |
| edge → edge | 3.6e-15 / 1.8e-15 | 2e-12 | 2e-15 |

- Forward values match ε(1,v)(1,v)^T to 3e-8 and 2e-9 (finite-difference v).
- **Locality** (part C, d = 1). The Fourier coefficients of F^{00}, F^{01} and F^{11} fall from O(1) to 8e-12, 5e-11 and 1e-10 at sup-distance 200 (literal profile), and similarly for the gapped profile. That is super-polynomial, as expected for C^∞ Gevrey-class data. Only a finite range is resolved. The proved statement is C^∞-smoothness of F on T^d × T^d, which holds because D's only zero is at q ≡ 0, where ω vanishes too (Hadamard).

**Lemma U (proved, elementary; checked).**
- **Claim.** Let F^{00} be continuous on T^d × T^d with F^{00}(k,k) = ε(k) > 0. Then F^{00} couples B to its complement: there are k ∈ B and k′ ∉ B with F^{00}(k′, k) ≠ 0.
- **Proof.** Take k₀ ∈ ∂B. Continuity gives F > 0 near (k₀, k₀), and that neighbourhood contains pairs straddling ∂B.
- **Check.** F^{00}((b − δ, 0.3) → (b + δ, 0.3)) = 2.04453, 2.04451, 2.04450 for δ = 0.05, 0.01, 0.001, against ε at the face = 2.04450.
- **Meaning.** A universal local graviton breaks the dynamical closure of the box at its face. The box is exact under matter dynamics, not under matter plus gravity. The leak needs lattice-frame momentum transfer up to the face, i.e. b/a.

### 3.3 Theorem E: universal coupling forces the boost anomaly into free fall. Proved (one-body, free); checked

- **Setting.** Uniform lapse field g, so H_g = dΓ(ε + g·D₁) with D₁ = ½{X, ε} (§3.2). The gravitating momentum is P_grav = dΓ(p), p = ∇(ε²/2).
- **Identity.** With X = i∂_k, [D₁j, p_i] = ½{i∂_j p_i, ε} = iε∂_j∂_i(ε²/2). Hence, as an operator identity on the domain of D,

  **dP_grav/dt = −g·(H + 𝒜), with 𝒜 = dΓ(ε·A) and A(k) = Hess(ε²/2)(k) − I.**

  For relativistic quanta the force is energy × g; A is the deviation.
- **Semiclassically** (Hamilton's equations for (1 + g·x)ε(k)): ẍ = [2(v·g)v − g] − A(k)g, at every k, not only at band minima. This is O2's Lemma F extended.
- **Zone mean.** ∫_{T^d} A = −I (I2/C3; counted once). So **no C² periodic band coupled universally to energy has universal free fall for all of its quanta.** Universal free fall for a quantum is the same condition as R7-1's boost closure for it. This is Einstein's elevator in lattice form: a uniform field is a boost, so EP and W3 are one statement.
- **Checks** (part D, d = 1). L = 1024, g = 5e-4, Gaussian packets with σ_x = 40, exact evolution:

| packet | a/g measured | semiclassical ⟨2v² − Hess(ε²/2)⟩ | Hess(ε²/2)(k₀) |
|---|---|---|---|
| literal, box rest k = 0 | −0.99654 | −0.99655 | +1.0000 |
| literal, doubler k = π | −0.99623 | −0.99624 | +1.0000 |
| literal, s-maximum k* = 2.234 | **+29.909** | +30.158 | −30.385 |
| gapped, box rest k = 0 | −0.99654 | −0.99655 | +1.0000 |
| gapped, edge top k = π | **+2.1995** | +2.1995 | −2.1995 |

- The −0.9965 at rest is the 2v² term from the packet's momentum spread. The 0.8% gap at k* comes from the anomaly varying fast across the packet.
- **Edge anomaly sizes** (part A). The zone mean of tr A/d is −1.000000 for both profiles in d = 2 and d = 3. On the edge:

| profile | edge mean | energy-weighted mean | low-T (T = 0.1) weighted mean |
|---|---|---|---|
| literal, d = 2 / d = 3 | −1.69 / −1.35 | −3.70 / −2.47 | +1.24 / +1.14 |
| gapped, d = 2 / d = 3 | −1.69 / −1.35 | −1.81 / −1.46 | −0.11 / −0.08 |

  So |Ā_edge| = O(0.1–4), whatever population is assumed.

### 3.4 Option (b): the gap, and its ceiling. Proved; checked

- **Ceiling (proved).** ε is continuous across ∂B, so inf over the edge of ε equals min over ∂B of ε = √(m² + b²). **No band can gap the edge above the box-face energy**, i.e. √(m² + b²)/a in physical units, below π/a.
- **Attained (checked).** The gapped profile has no light corners: ε = 2.73, 3.84 and 4.70 at the corners in d = 3. The edge minimum on the grid is 2.033, against the face value 2.022.
- **Physical reading** (labelled reading, not derived). With a = ℓ_P and b = 2, the edge starts at about 2E_P.
  - Static fields conserve energy, so a body made of box matter at energies ≪ E_P cannot make a real transition into the edge at any order in a static field.
  - A transition by graviton emission needs Planck momentum and energy.
  - In the literal law the doublers are degenerate in energy, but reaching them still needs momentum π/a. The graviton then carries energy |D(π)|/a ~ E_P, because D has no zero at π. So the real transition is also closed there, at linear order.

### 3.5 Option (c): non-periodic momentum space. Proved (elementary) plus prior art

- **Proof.** For a finite fibre, ℓ²(Z^d) ⊗ C^n = L²(T^d) ⊗ C^n, and momentum space is the dual group T^d. A one-particle energy equal to √(m² + |k|²) on all of ℝ^d needs n = ∞: the unfolded bands form a complete reciprocal-lattice tower.
- **This is I1's tower** (`C4_I1_referee.md:21`). With uniformly site-tied position it also meets O2's Lemma S.
- **Outcome.** No edge, universal coupling, no anomaly, η = 0. **The price is the Qubit axiom** (`AX:43-53`: a finite M₂(C) site domain becomes infinite-dimensional) and, in effect, a continuum per cell, which is O5's set A.
- Non-periodic momentum from a non-lattice set (quasicrystal, LRL) is outside this class. The LRL results are losing (`SUMMARY.md` §23).

### 3.6 Interacting matter: R7-4's flow obstruction applies, independent of the edge. Suggested (conditional on R7-4 Lemma 2, unrefereed)

- **The chain.** Exact W1 with a symmetric T for the interacting law gives [H, J] = 0 and i[H,D] = J (R7-4 Lemma 1). R7-4 Lemma 2 then gives [S, e^{isn·D₀}] = 0 for all s.
- **Universal T.** D₀ = dΓ(½{X, ε}), and each leg flows by dk/ds = ε(k)n. On the box this is an exact boost. It leaves any bounded interaction support at finite s: R7-1's BT plateau |P| < Π₂ is left at rapidity shift about asinh(Π₂/M) − asinh(P/M). Outside the support T = 0, so the T-matrix must vanish (R7-4 Lemma 3).
- **χ-cut T** (R7-1's original). The flow is dk/ds = χ²εn. It is slowed in the χ-shell and is not a boost there, but it still leaves the BT plateau. So the same conclusion follows.
- **Consequence.** R7-1's open W2 ("interacting stress") is obstructed in R7-4's class, not merely open. This holds in d ≥ 2 by R7-4's theorem, and in d = 1 for the BT plateau law as built.
  - In d = 1 every leg has the same flow period τ = ∮dk/ε. A flow-covariant extension of the interaction onto the edge might evade this. Not constructed.
- **This block concerns exact linear coupling of any kind, not universality.** It is the main reason the equivalence principle for bound test bodies (MICROSCOPE's actual objects) is not established here.

### 3.7 Eötvös η from edge modes, per option

η_edge ≈ |Δf_edge(Pt − Ti)|·|Ā_edge|. This is O2's sector-additive reading, SUGGESTED.

| option | universal coupling (linear) | edge free-fall weight (at rest) | edge content f of ordinary bodies | η from edge modes |
|---|---|---|---|---|
| R7-1 as built (χ-cut T) | **no** (edge and χ-shell excluded) | β = 0 on the edge (no fall); χ² in the shell | 0 exactly in class (proved) | **0** at linear order |
| (a) universal T, literal band | **yes**, free matter, all N (checked) | 1 at doubler rests; −30.4 at s-max; edge means −1.7 / −3.7 (energy-weighted) | 0 in class; Lemma U leak needs momentum ≥ b/a | **0** at linear order |
| (b) universal T, gapped band | **yes** (checked) | −2.2 at the edge top; edge means −1.7 / −1.8 | 0; leak needs energy ≥ √(m²+b²)/a | **0** at linear order |
| (c) non-periodic momentum | yes, trivially | no edge | none | **0** |

- **Allowance (reading).** With |Ā| between 1 and 4, η < 1e-15 needs |Δf_edge| ≲ 3e-16. That is, the edge may hold less than about 3e-16 of the Ti–Pt difference in energy fraction.
- **Beyond linear order (suggested).** Edge admixture from gravitational dressing at Planck transfer is of order (m_N/M_P)² ≈ 6e-39. This is a naive estimate, not computed.
- **The dangerous channels are outside the class:**
  - lattice gauge couplings, which reach the literal law's light doublers;
  - pair-creating loops, which reach the edge at the cutoff (R7-5). Once loops reach the edge, f_edge for UV-sensitive self-energies need not be suppressed, and η of order Δf_EM·α/π·|Ā| ~ 1e-6 is possible (suggested).

---

## 4. Against the FIXED readings (`TESTS.md:3463-3466`)

**Worker reading: PASS WITH SCOPE.** Referee required. Option (a) + (b) meets the clause's four items in the free class:
- **Universal coupling at linear order, box plus edge.** Construction A gives ∫T^{00} = H and an exact W1 on all of Fock space for free matter at every N, with a symmetric, Hermitian, quasi-local kernel. Checked to 1e-15.
- **η below 1e-15.** The edge-mode contribution is exactly 0 at linear order for every body made of box matter. The edge is unoccupied and the box is closed under matter dynamics (proved, R7-1 referee `:50-58`). With option (b), real edge production needs energy ≥ √(m²+b²)/a.
- **Prices named.** See §5.
- **Checked.** Parts A–D.

**Scope that must travel with the PASS.**
- Free (non-scattering) matter only. Universality there is a choice, R7-4's T2, not forced.
- The edge quanta themselves violate the EP at O(1) (Theorem E). The PASS is "η = 0 because the edge is empty", not "the edge falls universally".
- The O(κ) affine closure W3 holds on 𝒟_B (Lemma L) and fails on edge states (I2; Theorem E is its EP form).
- Gravity couples the box to the edge at the face (Lemma U), so box closure is exact only under matter dynamics.
- No loops, no pair creation, no gauge fields.

**If the referee requires interacting (bound) test bodies: INCONCLUSIVE.** Exact linear coupling of R7-1's box-supported scattering is obstructed by R7-4's flow argument (§3.6, argued and unrefereed), whether or not the edge gravitates. So the composite EP is not established in this class.

**FAIL is not available in the registered sense.** Construction A is an explicit counterexample to "universal coupling cannot hold with an exact box sector".

**What is proved negative (a bounded no-go, not the registered FAIL).** In the class of C² periodic one-body bands with lapse coupling to a universal, real-symmetric T^{00}, **universal coupling plus universal free fall for every gravitating quantum is impossible** (Theorem E + I2). Equivalently, option (a)'s "Ward identities closing on box ⊕ edge" holds for W1 and fails for W3, and that failure is the equivalence principle failing on the edge.

## 5. Prices (named, not adopted)

- **(a)** R7-1's price (`C5_R7-1_report.md:274`), plus:
  - an edge sector whose quanta violate the EP at O(1) (or, under R7-1's χ-cut, do not gravitate at all). Under a universal coupling this cannot be avoided (Theorem E);
  - a gravitating momentum J_E = ∇(ε²/2), which differs from the lattice translation generator on the edge;
  - a lattice divergence symbol with a single zero (generalized forward difference), or T switched off near transfers q ≈ π;
  - box closure exact only under matter dynamics (Lemma U).

  No axiom text changes: Admissibility does not fix dynamics or a stress (`AX:114-130`), and gravity and source bridges are outside the axioms (`AX:173-190`).
- **(b)** A band shape chosen to have no corner zeros (for Dirac matter, a Wilson-type momentum-dependent mass, suggested). The gap is capped at the box-face energy √(m²+b²)/a. No axiom text changes.
- **(c)** The Qubit axiom's finite site domain (`AX:43-53`) becomes infinite-dimensional: I1's tower, O5's set A.

## 6. Strong-word check

- "Exact" applies only to: the W1 identity of Construction A (machine precision, every set tested); Lemma L on 𝒟_B; and the operator identity of Theorem E for free one-body dynamics.
- "Proved" applies to: Finding D, Construction A's conservation, symmetry and Hermiticity, Lemma U, Theorem E (free, one-body, lapse coupling; domain technicalities for the unbounded X on the torus are handled as in R7-1's H-gen), the gap ceiling, and (c)'s n = ∞.
- "Quasi-local" means C^∞ kernels. Super-polynomial decay is the proved class; the numbers resolve only a finite range.
- "η = 0" holds at linear order, in the number-conserving, box-supported, empty-vacuum class. It is not a statement about loops.
- R7-4's obstruction is used as **argued, unrefereed**. §3.6 is suggested.
- The η estimates beyond linear order and the gauge/loop risk sizes are suggested.
- Literature (Nielsen–Ninomiya; the Collins et al. loop mechanism) is RECALLED, comparator only.

## 7. For the referee

1. W1 for the glued kernel. In particular, that D = q holds on supp φ, and that the real difference equals the wrapped q there (|q_i| ≤ 0.9 with both legs in [−1.9, 1.9]).
2. Hermiticity with a complex D, and the condition D(q)* = −D(−q).
3. That Y = 0 for a real-symmetric F^{00}, so the first moment is ½{X, ε} and Theorem E's identity holds.
4. Lemma U, and whether it, combined with I2, gives any stronger no-go than stated.
5. Whether PASS may be met by free matter, as the R7-1 referee allowed (`TESTS.md:3407`), or needs interacting bodies, in which case INCONCLUSIVE, with §3.6.
6. Finding D: R7-1's s(π) = 0 doublers.

## 8. Files

- `S/scripts/r82_edge.py`, `.out`: parts A (spectrum, doublers, anomaly statistics), B (Construction A residuals, Lemma U), C (locality, and the real-symbol contrast), D (wavepacket free fall). `S/scripts/r82_edge.log` is the run log.
- Sources: [MICROSCOPE final results, arXiv 2209.15487](https://arxiv.org/pdf/2209.15487); [PRL 129, 121102](https://physics.aps.org/featured-article-pdf/10.1103/PhysRevLett.129.121102); [MICROSCOPE WEP result, arXiv 2209.15488](https://arxiv.org/pdf/2209.15488).
