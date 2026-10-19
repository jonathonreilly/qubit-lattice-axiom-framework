# Complete corrected argument: Universal determinant polynomial and finite curvature controls

This is inspectable mathematical source. The canonical claim is limited to: Full determinant proof, finite cubic closure, timing identity and contact calculation.

**Deferred continuation:** Terminal uniqueness/birefringence exclusions beyond the explicit polynomial and physical hypotheses, and any underived metric-Hessian bridge. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# Lattice graviton kernels: one TT cone, DeWitt closure, and an underived seagull in the induced bubble

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Parts A and B are exact within the stated domains; part C is finite-quadrature numerical evidence plus one exact identity. Nothing is adopted. It corrects the wording of one earlier note.

## Question

The repository has three candidate spin-2 kernels:

- the Regge second variation on the cubic-Coxeter complex;
- the curvature member of the admissibility-rule lane;
- the 2026-06-08 induced-graviton bubble of the staggered Kähler–Dirac sea.

Three questions:

- Can the two TT polarisations of these kernels travel on different cones at leading order (birefringence)?
- What fixes the curvature member's kinetic anisotropy?
- Is the induced bubble a gauge-invariant graviton kernel, and does it fix the coefficient of the Einstein–Hilbert term?

## Result

### A. Exact determinant factorization and its conditional Lorentzian reading

Setting: quadratic forms S(k,h) in a symmetric h_{μν} (d = 4, time index t), quadratic in k, with constant coefficients (550 monomials). Gauge invariance means S(k, h + kξᵀ + ξkᵀ) = S(k, h) for all k, ξ.

1. **The class (prior result, cited).**
   - The gauge-invariant forms are exactly L_M = ε^{aceα} ε^{bdfβ} M_{αβ} k_e k_f h_{ab} h_{cd} with M symmetric. The ten L_M are independent and span the 10-dimensional gauge-invariant space.
   - L_I = −(flat Fierz–Pauli), and For invertible M, L_M = −det(M) × (Fierz–Pauli about the background g₀ = M), checked as a polynomial identity for sampled rational M.
   - The class statement, "the 10-dimensional class is background-metric linearised EH", is the 2026-06-10 note's theorem; the εεM parametrisation is only a convenient basis for it.
2. **Characteristic polynomial (new).** In temporal gauge (h_{tμ} = 0), for every symmetric M, of any signature and including degenerate M:

   det(spatial 6×6 block of L_M) = −16 w⁸ Q², with Q = kᵀ adj(M) k,

   where w = k_t. The proof uses three exact symbolic identities, each checked by the runner with M, k and h symbolic:
   - **Temporal reduction.** L_M on spatial h equals ε₃ε₃ N h h, with N = BᵀMB and B the 4×3 matrix with columns w e_s − k_s e_t.
   - **Cauchy–Binet.** The columns of B span the kernel of the covector k, and their wedge product is w² times the dual of k. So det N = w⁴ Q.
   - **The Sym₃ determinant.** The quadratic form h ↦ ε₃ε₃ N h h on symmetric 3×3 h has determinant −16 det(N)².

   For w ≠ 0 the determinant has the factor Q². This polynomial identity holds for every symmetric M, including degenerate matrices, but does not by itself establish two propagating TT modes. That reading requires a nondegenerate Lorentzian background and an admissible time direction and gauge reduction. Under those hypotheses both physical polarizations share the metric null cone. For M = I, Q is positive definite and has no nonzero real null vector; for rank-three M it can be a squared linear form; for rank M ≤ 2, adj M = 0 and the determinant vanishes identically. These degenerate cases require their own constraint analysis.
3. **Exact counts** (invariant forms / gauge-invariant forms):

   | Symmetry | Invariant | Gauge-invariant | Spanned by |
   |---|---|---|---|
   | S4 (permutations; the Kuhn complex) | 38 | 2 | L_I, L_J (backgrounds I + c(J − I)) |
   | B4 (signed permutations) | 9 | 1 | L_I |
   | B3 × Z2 (spatial cube × time sign) | 26 | 2 | L_I, L_{E_tt} (backgrounds diag(1,1,1,s)) |
   | none, d = 4 | 550 | 10 | all L_M |
   | none, d = 3 | 126 | 1 | 3D linearised EH |

   So every gauge-invariant form with one of these symmetries is L_M with M in the group's fixed set: EH about such a background, up to scale and sign. For S4 the degenerate limits are at c = 1 and c = −1/3.

### B. Constraint closure selects the DeWitt ray in the cubic family (exact, finite tori)

The curvature member uses the 2026-09-24 note's clauses:

- the block-62 placement: h_jj on sites, h_ij on faces, relabellings on bonds;
- R₁ = p² tr h − p·h·p;
- the lapse constraint C[N];
- the bracket term linear in canonical momentum at flat strain.

The 09-24 note took the rotation-invariant kinetic term α tr ḣ² + β (tr ḣ)² and found closure only at β = −α. Here the kinetic term is widened to the cubic ultralocal inverse-kinetic family

  ∂H/∂P_jj = a P_jj + b Σ_i P_ii,  ∂H/∂P_ij = f P_ij (i < j),

which has cubic anisotropy ε₃ = a/(2f) − 1 and c = −b/a.

1. **ε₃ = 0 of the repo's kinetic term is supplied, not derived.** For α tr ḣ² + β (tr ḣ)², M₁ = α + β, M₂ = 2β and M₃ = 2α, so ε₃ = M₃/(2M₁ − M₂) − 1 = 0 identically. At β = −α (c = 1/2) the inverse kinetic form is the ray (a,b,f) ∝ (2,−1,1). This is the DeWitt kinetic form tr ḣ² − (tr ḣ)².
2. **Closure forces ε₃ = 0 (new).** For each lapse pair, the runner solves exactly, over Q, for every (a,b,f) whose bracket {C[N], C[M]} lies in the span of all lattice relabellings. On the 3³, 4³ and 5³ tori, for the generic lapse pairs computed (random integer lapses on all three; also δ(0), δ(e₁) on 3³ and 4³), mean-four timing is executed on all three sizes and opposite-pair timings only on 3³. The current 09-24 T1 local identity supplies the extension: opposite mean minus four-corner mean is ±dM/4, whose antisymmetrization cancels for every face coefficient and every side ≥ 3. For these equivalent timings, the closing set is exactly the one ray (2,−1,1). The rank of the relabelling map is 78, 189 and 372 on the three tori.
   - The set closing for all lapse pairs is contained in this ray.
   - The 09-24 note's T1 shows that the ray closes for every lapse.
   - So on these tori, the set of cubic ultralocal forms that close for all lapse pairs is exactly the DeWitt ray. Constraint closure fixes both c = 1/2 and ε₃ = 0.
   - This is a lattice analogue of the Hojman–Kuchař–Teitelboim result that closure of the deformation algebra fixes the DeWitt supermetric. It is conditional on the supplied clauses: closure rule, face timing, R₁ placement and the ultralocal kinetic ansatz.
3. **Caveats.**
   - Closure must be required for all lapse pairs. The pair δ(0), δ(e₁+e₂) closes for every (a,b,f), and a smooth lapse pair fixes only c (campaign check).
   - With single-corner face timing, nothing closes at generic lapse pairs.
   - The statement is about the flat-strain bracket term linear in P. It is leading order, not a nonlinear statement and not an all-n theorem.
4. **Label correction.** The campaign script labelled two non-DeWitt sample points "ε₃ = +0.1" and "ε₃ = −0.2". They are α_d = 1.1 α_f, which gives ε₃ = −1/11, and α_d = 0.8 α_f, which gives ε₃ = +1/4. The conclusion is unaffected.

### C. The induced bubble violates the Ward identity through an underived contact term (numerical)

The kernel is the one defined by the 2026-06-08 dispersion and telescope runners (vertex D):

Π_{μν,ρσ}(K) = N⁻⁴ Σ_P tr[G(P) V_{μν}(P̄) G(P+K) V_{ρσ}(P̄)], with V_{μν} = ½(Vel_μ sin P̄_ν + Vel_ν sin P̄_μ), Vel = ∂D/∂P and P̄ = P + K/2,

where D is the 16×16 hypercube-block staggered operator and the runners subtract Π(0).

- **Reconstruction.** Two constructions of D(P) agree, D D† = (m² + Σ sin²(P/2)) I, and the operator Ward telescope k̂·Vel(P̄) = D(P+K) − D(P) holds exactly. The runner-cache constant C_time(N = 6) = 0.08961606 is reproduced.
- **Vertex S excluded.** The runners' other vertex, S (sin(P̄/2)), is not Brillouin-zone periodic: shifting the BZ window changes Π at O(1) (relative 0.85 at N = 6). Vertex D is window-independent to 1e-15.

Results:

1. **The K² symbol violates the Ward identity at O(1).**
   - The measured symbol lies in the 9-dimensional B4 symbol space (3-direction fit; out-of-fit direction predicted). In that space the Ward map has rank 8, and its kernel is linearised EH alone.
   - The symbol ratio max|k̂·M₂|/max|M₂| is direction-dependent. It is 0.184–0.228 over the campaign checker's five directions and 0.130–0.231 over 409 sampled directions. The campaign quoted 0.18–0.23, with 0.23 the maximum.
   - The ratio is mass-insensitive: 0.189, 0.196 and 0.201 at m = 1.0, 0.7 and 0.5 (N = 12) along a fixed direction.
   - The lattice Ward residual scales as K^1.00 without the Π(0) subtraction and as K^2.99 with it. So the K² symbol itself is not transverse.
2. **The violation is a pure contact term.**
   - k̂·Π_bubble equals a sum of one-propagator loops: an exact identity, to 5e-15. These loops have exactly the shape of a two-graviton seagull's tadpole.
   - The local nearest-neighbour B4 K² seagull S(K) = (a·EH − T)[k̂,k̂] removes the violation. On an out-of-fit direction the residual power rises from 2.99 to 4.82, and at κ = 0.1 the residual falls from 7.8e-6 to 1.7e-10.
3. **The induced EH coefficient is not determined by the bubble.**
   - B4 allows 9 seagull coefficients. Demanding the Ward identity fixes 8 of them, tuned against the bubble. No examined lattice symmetry fixes them: the B4 point group and evenness in K allow all 9.
   - The ninth coefficient, along EH, is unconstrained: changing it leaves the Ward residual unchanged to 1e-12 or better.
   - The bubble's own EH projection, a_EH = 0.0288 (Frobenius; non-EH fraction 0.92), is norm-dependent.
   - So a_EH, the coefficient that would set 1/G, is a free contact coefficient until a seagull is derived.
4. **Correction to the 2026-06-08 transverse-seagull note.**
   - That note's two-component scheme (conserved vertex V_cons plus the q-only contact S = −B0 + B1 + B5) is described as "transverse to leading physical order", with an O(k³) residual. Its seagull tadpole is K-independent, so it can remove only the O(k) Π(0)-type contact term.
   - Its O(k³) residual is O(1) relative to k times the TT k² slope: ratio 0.877 at k = 0.2 and 0.1. So the scheme's K² symbol is not transverse, which is the same leading-order break as in item 1.
   - The phrase should read "removes the O(k) contact term; the K² symbol is not transverse". That note's statements about exact operator identities, and its list of open items, are unaffected.

## How this bears on the lane (interpretation, not a claim)

- **Birefringence.** For a nondegenerate Lorentzian background with admissible time/gauge reduction, the determinant factorization gives the shared TT characteristic at two derivatives. A split would have to come from higher-derivative terms or from a gauge-non-invariant kernel. Raw numbers from the uncompleted bubble, such as the [110] TT-pencil split of 5e-3 in the campaign, are not graviton speeds.
- **The curvature member.** Its kinetic anisotropy is no longer an extra free choice once constraint closure is imposed on the cubic ultralocal family. Within the supplied clauses, closure selects GR's DeWitt form.
- **The induced route to 1/G is open.** The bubble does not determine the EH coefficient. Two things are needed: a derived two-graviton vertex (for example from the metric Hessian of log det), or a symmetry that fixes the seagull.

## Premises

- **Axioms used.** Lattice (Z³, unit translations) as the setting of the supplied models; see the axioms memo. No axiom is added.
- **Supplied, part A.** Constant-coefficient two-derivative quadratic forms, and linearised gauge transformations h → h + kξᵀ + ξkᵀ.
- **Supplied, part B.** The 2026-09-24 note's clauses (block-62 placement, R₁, lapse constraint, closure rule, face timings), and the cubic ultralocal inverse-kinetic ansatz. The repo's ε₃ = 0 kinetic term is itself supplied.
- **Supplied, part C.**
  - The 2026-06-08 runners' bubble definition with vertex D, and the mass m = 0.7 (also 0.5 and 1.0).
  - Finite quadrature, N = 12 (N = 6 and 8 for identities).
  - Richardson symbol extraction from κ = 0.1, 0.05.
  - The two-component scheme as defined by its runner.
- **Standard facts used.** Cauchy–Binet; the Fierz–Pauli form of linearised EH; Reynolds averaging over a finite group.

## Relation to prior work

- **Repo, cited and not re-claimed.**
  - The 2026-06-10 action-selection note: the 10-dimensional gauge-invariant class equals background-metric linearised EH, and Regge realises −½ EH about δ.
  - Its 2026-06-09 companions: the second-variation notes.
  - The 2026-09-03 Regge note. The campaign confirmed numerically that its symbol is −½ EH, with g3/g1 = 3.8e-10. That follows from part A plus the supplied edge lengths realising δ (zero tilt).
- **Repo, extended.** The 2026-09-24 note: closure at β = −α within the rotation-invariant family. Part B widens the family and shows ε₃ = 0 is also forced.
- **Repo, corrected.** The 2026-06-08 transverse-seagull note (wording; see C4).
- **Repo, consistent.** The 2026-06-08 telescope, dispersion, isotropy and TT notes claim exact operator identities or finite-grid channel diagnostics, and disclaim the Ward bridge. Part C supplies the reason that bridge fails for the bare bubble.
- **Literature (recalled, not re-checked).**
  - Hojman, Kuchař and Teitelboim, Ann. Phys. 96, 88 (1976): closure of the hypersurface-deformation algebra fixes the DeWitt supermetric. Part B is a finite lattice analogue at leading order.
  - Kostelecký and Mewes, Phys. Lett. B 757, 510 (2016): in the linearised gravity sector, operators of mass dimension 4 give no birefringence, and birefringence first appears at higher dimension. Part A2 is an exact statement of that kind for every constant-coefficient two-derivative gauge-invariant form; this note relies on the recalled statement only as context.
  - Fierz–Pauli and the induced-gravity programme (Sakharov) are context.
- **New here.**
  - The one-cone determinant −16 w⁸ Q² with its symbolic proof.
  - The exact symmetry-restricted counts, which restrict the 06-10 class to each group.
  - The DeWitt ray as the full closing set in the cubic ultralocal family.
  - The contact-term diagnosis of the bubble's Ward violation, with the free EH seagull coefficient.
  - The correction to the transverse-seagull wording.

## Historical packet proposal (promotion deferred)

Part C contains a negative claim: the bubble does not determine a_EH, and the bare bubble is not Ward-covariant.

- **N1 — routes.**
  - Tried: the bare bubble; the Π(0) subtraction; the K-independent seagull (two-component scheme); and the full 9-parameter B4 nearest-neighbour K² seagull.
  - Not tried: a seagull derived from the metric Hessian of log det(D + J); longer-range seagulls; other vertex discretisations; symmetries beyond the B4 point group and evenness, such as staggered shift symmetries.
- **N2/N3 — scope.**
  - One vertex (D).
  - Masses 0.5, 0.7 and 1.0.
  - N = 12 quadrature. The campaign found a 1.7e-4 relative difference between N = 12 and N = 14, far below the effects reported.
  - B4 symbols at two derivatives only.
- **N4 — inputs.**
  - Parts A and B are exact rational arithmetic.
  - Part C uses floating quadrature. Its exact identity holds to 5e-15. Its symbol extraction uses Richardson extrapolation with O(κ⁴) error.
- **N5 — wording.**
  - "Not determined" means: the Ward identity plus B4 leave the seagull's EH coefficient free. It does not mean that no derivation could fix it.
  - "Ward violation" refers to the K² symbol of the kernel as the repo runners define it.
- **N6/N7 — strongest objections.**
  - A derived W-Hessian contact term might fix all 9 coefficients, including a_EH. That is exactly the open item.
  - The 0.18–0.23 range is direction-dependent and norm-dependent. The claim rests only on its being O(1) in every sampled direction.
- **N8 — earlier claims.** Corrects the 2026-06-08 transverse-seagull note's "transverse to leading physical order" wording. Every other earlier statement is unchanged.

## Historical checking narrative (not fresh evidence)

Provenance: both checks were run by fresh-context agents of the same model family as the authors. They are independent of the authors only in code path. They are not different-model reviews.

- **B4_check** (campaign `B4_check/REPORT.md`).
  - It re-derived the counts by exact orbit sums over Q, with no SVD. It confirmed S4 38/2, B4 9/1, B3×Z2 26/2, and none 10 (d = 4) and 1 (d = 3).
  - It proved the εεM characterisation, and the one-cone determinant at sampled rational M.
  - It solved the closure condition for the whole (a,b,f) space exactly, on 3³, 4³ and 5³, and found the single ray (2,−1,1).
  - It found the ε₃ label error (−1/11 and +1/4) and the caveats on lapse pairs and corner timing.
  - It noted that the original findings had not cited the 06-10 note. All of these are incorporated here.
- **B4b_check** (campaign `B4b_check/REPORT.md`).
  - It wrote its own bubble from the real-space staggered operator. That bubble matches the author's to 3e-15; the kernel definition is shared by design.
  - It confirmed the K¹ and K³ scaling, and the 9-dimensional B4 space with Ward rank 8 and kernel EH (cos 1.0).
  - It found that the symbol ratio is 0.18–0.23 across directions, with 0.23 the maximum, and nearly constant in m: 0.177 at m = 1.0 and 0.186 at m = 0.25 (N = 28).
  - It proved the one-propagator identity, and that the nearest-neighbour seagull restores Ward, giving a K⁵ residual.
  - It recast the defect as a missing seagull rather than an intrinsic break, and found the transverse-seagull overclaim, with ratio 0.88.
  - It recorded that the repo's telescope, dispersion, isotropy and TT notes do not contradict this.
- **This runner.** It is a consolidated adaptation of the checkers' code (plus a second construction of D(P) and the symbolic proof of A4). It is not a further independent check.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/lattice_graviton_kernels_one_cone_dewitt_closure_induced_bubble_seagull_2026_10_18.py
```

Expected: `TOTAL: PASS=37 FAIL=0` (about 3 minutes on 4 cores).

## Load-bearing sources

- Action-selection EH-class note (2026-06-10) (`docs/CUBIC_COXETER_REGGE_LINEARIZED_ACTION_SELECTION_EH_CLASS_NARROW_THEOREM_NOTE_2026-06-10.md`)
- 3+1 tick-extension second variation (2026-06-09) (`docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md`)
- Regge second variation equals linearised EH (2026-06-09) (`docs/CUBIC_COXETER_REGGE_SECOND_VARIATION_EQUALS_LINEARIZED_EH_NARROW_THEOREM_NOTE_2026-06-09.md`)
- Native linearised graviton on the 4D cubic-Coxeter complex (2026-09-03) (`docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md`)
- Curvature member constraint closure (2026-09-24) (`docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md`)
- Induced-graviton dispersion runner note (2026-06-08) (`docs/UNIVERSAL_GR_GRAVITON_DISPERSION_LORENTZ_ISOTROPY_BOUNDED_THEOREM_NOTE_2026-06-08.md`)
- Operator Ward telescope (2026-06-08) (`docs/UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md`)
- Transverse-seagull scheme, corrected here (2026-06-08) (`docs/UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`)
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
