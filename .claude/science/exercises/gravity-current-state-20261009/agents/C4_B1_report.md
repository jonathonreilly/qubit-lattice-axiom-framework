# Lane RB, probe B1: boost generators that are not first moments

**Provenance.** Worker: Claude Opus 5.5, the same model family as the supervisor. Ran 19:17Z to about 19:50Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/B1/`

| Script | Output | What it checks |
|---|---|---|
| `b1_1d.py` | `b1_1d.out` | 1D: exact deformed algebra for the first moment (sympy); orbit sum rule for random V; Magueijo–Smolin-type V; exact Poincaré needs V → ∞; Fock non-additivity; where the deformation sits |
| `b1_2d3d.py` | `b1_2d3d.out` | d = 2, 3: the deformed rotation J∇u and its hyperbolic zeros and periods; why rotations cannot act on a vector P; double points for the lapse-smearing algebra (random cubic u); so(3) failure for first-moment rotations; orbit-average sum rule in 2D |

**Read in full first:** the axioms memo; TESTS.md, the C4 waves and Lane RB; RC_C3, C4_I1, C4_M1 and C4_K2, each with its referee report.

**Notation.**
- One-particle space L²(T^d), with H = ω(k), u = ω²/2, and P_c = p_c(k).
- A boost-like generator acts as K = ½{V(k), i∂_k} + φ(k), where V is a vector field on the Brillouin zone (BZ).
- With this convention i[K, f] = −V·∇f.
- "First moment" means V = ω e_b, i.e. K_b = ½{X_b, H} + a_b(k).

## Reading against the FIXED lines

**PASS: not met.**
- No generator was found in d ≥ 2.
- In 1D, nonlinear algebras exist, but they have no rotations, and gravity cannot use them (§4).

**FAIL (bounded): met.** Scope: free matter; a single isolated band, or band-diagonal finite bands; cubic-covariant dispersion; d = 2, 3. The fixed FAIL clause allows either of two disjuncts, and both hold.

1. **No generator of any form closes the algebra.**
   - Undeformed algebra: Theorem U.
   - DSR-type algebra, where the Lorentz/rotation part is undeformed and the action on momenta is nonlinear: Theorem R.
   - Both hold for any K: local, quasi-local or non-local, any moment.
2. **None can arise from a local smearing.**
   - The N = x lapse smearing of a translation-covariant constraint is always a first moment (Theorem S).
   - At the matter-bilinear order, the structure functions of the gravitational algebra are c-numbers (C3's Lemma 1). So Theorem U applies.
   - Even if (H,P)-dependent structure functions were allowed, the first-moment algebra fails for Morse cubic dispersions (Theorem D).

**What stays INCONCLUSIVE:**
- fully deformed algebras built on non-first-moment V, with structure functions in (H,P), in d ≥ 2. They are probably realizable algebraically, but they are not gauge-usable (§3.4);
- bands that touch;
- interacting matter;
- singular structure functions;
- non-Morse (fine-tuned) dispersions;
- a globally Euclidean (β < 0) algebra. It is not excluded by boundedness, but it is not Lorentzian.

**Against the supervisor's expectation.** The expectation is confirmed, with three differences.
- **The d ≥ 2 obstruction is topological, not umbilic.**
  - The BZ is a torus, which is aspherical. No nontrivial smooth circle action on T^d has a fixed point.
  - This kills every undeformed rotation subgroup, whatever K is.
  - It supersedes I1's argued Darboux step. It needs neither first moments nor d = 3.
- **The 1D curiosity carries a mandatory "signature change".** The structure function [K,P] = iF integrates to zero over the band: ∫F dH = 0.
- **Bojowald-type deformations cannot help.** They depend on the gravitational extrinsic curvature and are trivial on the flat background where C3's Killing-sector obstruction sits.

## 1. Which generators are possible (free matter)

**Theorem 0 (form of the generator; PROVED).**
- **Statement.** Let K be any operator on L²(T^d) whose commutators with H and with P_c are translation-invariant, i.e. functions of k. Assume dω and dp_c span T*T^d almost everywhere. Then K = V·∂ + φ(k) + C, where C commutes with H and P.
- **Proof.**
  - Write K as a kernel K(k,k′). The condition (f(k′) − f(k))K(k,k′) ∈ (diagonal distributions) for f = ω, p_c forces K to be supported on the diagonal, plus a commutant part.
  - A diagonal distribution of order n gives commutators with n-th derivatives of f against δ^{(n−1)}. These vanish only for n ≤ 1.
- **Consequences:**
  - Higher moments (Σx²q, …) are excluded: they are second-order operators, and their commutator with H is not translation-invariant.
  - "Quasi-local non-density" generators do not exist as a separate class. In position space every allowed K equals Σ_x x·q_V(x) + (translation-invariant), where q_V is the density of the conserved one-body charge Q_V with symbol V.
  - **So a non-first-moment boost is a first moment of a different conserved density (V ≠ ω).**
  - Number-changing (Bogoliubov) parts commute with H and P, so they can be dropped.
  - For finite bands, [K,H] = g(H,P) makes K band-diagonal away from degeneracies, as in I1 Prop. 1, so each band carries its own V^α.

**Theorem U (undeformed algebra, any K; PROVED).**
- **Statement.** Let K be self-adjoint, of any form, local or not. Suppose i[K_b,H] = −P_b and i[K_b,P_c] = −βδ_bc H with β > 0, on a sector where H and P are bounded (one band, finitely many bands, or bounded fibres). Then H = P = 0 there.
- **Proof.** This is M1's T2, which never used the first-moment form. Set A_± = H ± P_b/√β. Then e^{iηK}A_± e^{−iηK} = e^{∓√β η}A_±, and the norm is invariant under unitary conjugation.
- **This closes the non-first-moment loophole for the undeformed algebra outright.**
- Only an unbounded fibre escapes, namely I1's tower.

**Theorem S (lapse smearing forces the first moment; PROVED).**
- **Statement.** Let h(x) be any lattice-translation-covariant density with Σ_x h(x) = H. It may be local or not, and may be improved. Then K = Σ x·h(x) obeys T_j K T_j⁻¹ = K − j·H. So K − ½{X,H} commutes with every T_j, and on one band it is multiplication by a(k). Hence V = ω.
- **Gravity version.**
  - In the HDA, {H[N], H[1]} = −D[∇N] is a global charge only for affine N.
  - Constraints are linear in the lapse.
  - So a boost that gravity generates is the N = x smearing of the Hamiltonian constraint, and is a first moment.
- **Corollary.** A non-first-moment K_V (V ≠ ω) obeys T_j K_V T_j⁻¹ = K_V − j·Q_V with Q_V ≠ H. It is the smearing of a different density.
  - Gauging it means adding a new constraint for Q_V.
  - In Fock space, ad_K then generates (V·∇)ⁿω, an infinite tower of one-body charges. This is a higher-spin-like gauge structure (READING; COMPARATOR from memory: Vasiliev higher-spin gravity).

## 2. One dimension: deformed boosts exist (the curiosity confirmed and sharpened)

**Classification (PROVED).**
- Any smooth even V gives a closed nonlinear algebra [K,H] = iP, [K,P] = iF(H), [H,P] = 0, where P = Vω′ and F = V(Vω′)′.
- F is a smooth function of H alone, because ω is monotone on [0,π].
- The Casimir is P² − 2∫F dH.
- The IR is Poincaré iff V(0)² ω″(0) = βm, i.e. V(0) = ω(0).

**First-moment example (lattice KG, exact).**
- P = sin k and F = H(1 − (H² − m²)/2).
- Residual exactly 0 (sympy, `b1_1d.out` (a)).
- **So the first moment already closes a deformed 1+1 algebra.** C3's obstruction concerns only the linear algebra.

**Two types:**
- **V ≠ 0 everywhere.** The rapidity is periodic: τ = 2∫dk/ω = 4.79 at m = 0.7, as in M1.
- **V(π) = 0: Magueijo–Smolin type.** The rapidity is infinite and H → ω_max, an invariant maximal energy.
  - With V = ω cos(k/2): s = 11.3 gives H = ω_max to 7 digits, while m cosh s = 2.8e4.

**Orbit sum rule (PROVED; CHECKED).**
- P = Vω′ vanishes at both ends of the boost orbit, so ∫_orbit F dH = [P²/2] = 0.
- **Every** 1D deformed boost therefore has F < 0 near the band top: an obligatory Euclidean, "signature-changed" region.
- Checked for 6 random V and for the MS-type V, with relative residual ≤ 6e-10. In every case F(0) equals the IR value and min F < 0.
- This is the boost-orbit analogue of the −β zone average found in C3, I1 and M1.

**Exact Poincaré on the band** needs V = √(ω² − m²)/ω′. This blows up at the edge: V(3.14) = 2.7e3. CHECKED.

**Fock space (CHECKED, (e)).**
- Pairs of states with equal (H_tot, P_tot) to 1e-15 have Σ F(k_i) differing by 0.22–0.54.
- So the many-body bracket is **not** F(H,P). It closes only on the tower of one-body charges. This is the soccer-ball problem in lattice form.

**Where the deformation sits.**
- With local P = sin k, {H[1], H[x]} is undeformed, and the factor cos k lands in {D, H}, i.e. [P,K] = iH cos k.
- Moving the deformation into {H,H}, in Bojowald form with β(k) = sin k / k, requires the SLAC momentum P = k, which is non-local.

## 3. d = 2, 3

### 3.1 Theorem R: rotations cannot act as a group on the BZ (PROVED; any K)

**Lemma (PROVED).** A nontrivial smooth circle action on T^d has no fixed point.

**Proof.**
1. Let the circle fix 0. Every orbit is homotopic to the orbit of 0, which is a point, so every orbit is contractible.
2. The action therefore lifts to R^d as a circle action that commutes with the Z^d translations. At 0̃ the lifted flow returns, so Φ̃_{2π} = id.
3. Define the barycentre f(x) = (1/2π)∫Φ̃_θ(x)dθ. Then f(x + n) = f(x) + n, so f descends to T^d → T^d and is homotopic to the identity. Its degree is 1, so f is surjective.
4. But f is constant on orbits, so its rank is ≤ d − 1 off the fixed set F.
5. F is a union of submanifolds of codimension ≥ 2 (slice theorem), so it has measure zero.
6. By Sard, f(T^d) has measure zero. Contradiction. ∎

This is consistent with Conner–Raymond (COMPARATOR, from memory): effective torus actions on closed aspherical manifolds have injective orbit maps on π₁.

**Applications. Each produces a circle action with fixed point 0, the rest momentum.**
- **(R1) d ≥ 3, undeformed so(d).**
  - Smooth vector fields on compact T^d are complete.
  - By Palais, an undeformed so(d) of such fields integrates to Spin(d), which is compact.
  - Its U(1) subgroups fix 0.
  - No condition on P or on K is needed.
- **(R2) d = 2, undeformed so(2,1), analytic generators** (exponentially quasi-local symbols are analytic).
  - The central element exp(2πL) fixes the open orbit of 0 pointwise.
  - Analyticity makes it the identity everywhere, so L generates a circle action.
- **(R3) d = 2, rotation acting on P as a vector** (W·∇p = Jp), smooth, with isolated zeros of p.
  - Zeros of W are exactly zeros of p.
  - Each isolated zero of W has index +1:
    - W is tangent to the level curves of |p|;
    - a hole in a sublevel disk would need an interior zero of W, which does not exist;
    - Hopf's Umlaufsatz then gives index +1.
  - Poincaré–Hopf gives Σ ind = χ(T²) = 0. But 0 is a zero. Contradiction.
  - **CHECKED** (`b1_2d3d.out` (b)), for p = sin k and 4 random odd C4-covariant p:
    - the degrees of p sum to 0, with zeros of degree −1 present;
    - so a fold det Dp = 0 exists;
    - on 79–97% of fold cells, adj(Dp)Jp ≠ 0, so Jp ∉ range Dp and **no W exists there at all**.

**Consequences.**
- DSR / κ-Poincaré-type realizations need an undeformed Lorentz algebra acting nonlinearly on momenta. **They are impossible on the lattice BZ in d ≥ 2, for any generator.**
- **This kills I1's DSR class before its umbilic step.**

**Comparator, checked against the source (ar5iv abstract-level fetch): Bisio–D'Ariano–Perinotti, [arXiv:1503.01017](https://arxiv.org/abs/1503.01017).**
- Their nonlinear Lorentz action for the 3+1 Weyl automaton is defined region by region.
- The BZ is split along the surface F where the Jacobian of their map vanishes, and a further set H is removed.
- The regions are invariant "up to null sets".
- This is exactly the fold set found in (R3). Their construction is consistent with Theorem R: it is not a smooth global action on T³.

### 3.2 What survives algebraically: non-compact "rotations" (CHECKED)

In d = 2, W = J∇u commutes with H exactly. It is C3's first-moment rotation.
- Its zeros at Γ and M are elliptic.
- At the van Hove points X and X′ they are **hyperbolic**: eigenvalues ±1, so there the "rotation" acts as a boost.
- Orbit periods: T/2π − 1 = 3.1e-4 at k = 0.05, matching k²/8. T diverges at the van Hove separatrix (T = 62.6 at k = 3.14).
- Angular momentum 2πn/T is therefore not quantized at nonzero momentum. The deviation is O((ka)²) in the IR.

In d = 3 (sympy, exact): [L₁₂, L₂₃] = cos k₂ · L₁₃ for the lattice KG. The rotation algebra is deformed by the same cos k factor.

### 3.3 Theorem D: the gravity-usable algebra fails even when deformed (PROVED for Morse u; CHECKED)

**Setting.** Theorem S fixes V_b = ω e_b, and C1 fixes P = ∇u. Then i[K_a,P_b] = −ω ∂_a∂_b u.

**Statement.** Suppose this bracket is to be any function F_ab(H,P) at all, smooth or not. Let s be a critical point of u off the O-fixed points. The orbit partners Rs have the same (ω, P = 0), so Hess u(Rs) = Hess u(s). Hence Hess u is O-invariant, i.e. ∝ I, so every critical point has index 0 or d. But Morse theory on T^d needs index-1 critical points (b₁ = d). Contradiction.

**CHECKED** (`b1_2d3d.out` (c)) for the lattice KG and for 3 random cubic u in each of d = 2 and 3:
- every case is Morse;
- index-1 points exist;
- 4 (d = 2) and 96–192 (d = 3) partner pairs have equal (H,P) but different Hessians, with |ΔHess| up to 3.2.

The d = 2 KG also collides along the van Hove lines: at (a, π−a) and (π−a, a), ω and P are equal but Hess u = ±diag(c, −c).

### 3.4 Orbit sum rule in any d (PROVED; CHECKED)

**Statement.** Take any complete boost flow, of any V, with H and P bounded. Along each orbit, d²H/ds² = F_bb, so its orbit average is lim (P(S) − P(0))/S = 0.

**Check.** For a random non-first-moment 2D V₁, the running average falls as 4e-2 → −5.6e-3 → −8.4e-4 for S = 10, 100, 1000. F at rest is +1.007 and min F on the orbit is −0.95.

**Reading.** A Euclidean region is unavoidable for any deformed boost on bounded bands.

**Non-first-moment fully deformed algebras (SUGGESTED, not settled).**
- With a generic smooth cubic-covariant V and P, the symmetry-forced double points are only the zeros of P.
- There C4 compatibility requires [K_a,P_b] ∝ αI + βJ, which looks satisfiable.
- So such algebras probably exist at the one-particle level. They are:
  - not lapse smearings (Theorem S);
  - non-closing on (H,P) in Fock space (§2(e));
  - built on non-compact rotations.

## 4. Gravity: is a deformed HDA available? (Part 2)

**Structure functions at the relevant order.**
- C3's Lemma 1 (refereed, confirmed) shows that at flat background and matter-bilinear order, structure functions are c-numbers. Field-dependent ones give cubic or quartic terms.
- So the global sector must be a Lie algebra with constant structure constants on the Killing smearings {H, P, K, L}.
- (H,P)-dependent or k-dependent deformations do not exist at that order. Writing F(k) amounts to choosing a different bilinear density, i.e. a new constraint.
- Theorem U then excludes every K on bounded bands (READING built on the proved pieces).

**Bojowald-type deformed HDA.** References: Bojowald–Paily, PRD 86, 104018, [arXiv:1112.1899](https://arxiv.org/abs/1112.1899); signature change in Bojowald–Brahma, PRD 95, 124014, and in Mielczarek and Cailleteau et al.
- The algebra is {H[N],H[M]} = D[β(N∇M − M∇N)], with β = cos(2δK_grav). Its {D,H} bracket is undeformed.
- **On the flat background K_grav = 0, β = 1.** The Killing sector where C3, K2 and I1 sit is therefore undeformed (READING, from the cited form).
- An undeformed {D,H} forces, by Theorem S, a first moment and an exact translation symbol (p = k, SLAC).
- The deformation the lattice actually produces sits in {D,H} (P acting on H as cos k), or in the rotation brackets. Effective LQG keeps both of these undeformed.
- **Analogy (READING).**
  - The lattice factors cos k (1D: F/H = cos k; d = 3: [L₁₂,L₂₃] = cos k₂ L₁₃) mirror Bojowald's cos(2δK).
  - Our 1D sum rule makes β < 0 regions mandatory, matching his signature change.
  - But on the lattice these are functions of matter momentum, which C3's Lemma 1 excludes as structure functions.
- **A globally Euclidean algebra (β < 0)** survives the boundedness argument, but it is not Lorentzian. For first moments, C3 kills it anyway: Hess u = βI with periodic u.

**DSR and relative locality (COMPARATOR, from memory except where noted).**
- Sources: Amelino-Camelia (gr-qc/0012051), Magueijo–Smolin (hep-th/0112090), AFKS relative locality (arXiv:1101.0931).
- These need an observer-independent, undeformed Lorentz group acting nonlinearly. Theorem R excludes that on T^d for d ≥ 2.
- So a lattice substrate is a preferred-frame theory (lane RF), not DSR.
- The soccer-ball problem appears as §2(e).
- Hossenfelder's nonlocality bound (PRL 104, 140402) targets n = 1 DSR and is moot here.

**Observational viability of the lattice-scale deformation itself.**
- A cubic, even ω gives no linear (n = 1) term.
- **n = 1 bounds (E_QG,1 > M_Pl) do not apply.**
  - Fermi-LAT GRB 090510 gives E_QG,1 ≳ 1.2 E_Pl (from memory).
  - LHAASO GRB 221009A gives E_QG,1 > 10 E_Pl (PRL 133, 071501, [arXiv:2402.06009](https://arxiv.org/abs/2402.06009); checked by search).
- **The n = 2 bound passes.**
  - Axis dispersion ω = (2/a)sin(ka/2) gives E_QG,2 = √12/a ≈ 3.5 E_Pl for a = ℓ_Pl. The body diagonal differs by an O(1) factor.
  - LHAASO gives E_QG,2 > 6×10⁻⁸ E_Pl, which passes by about 8 orders.
- **GW170817** (|c_T − 1| ≲ 1e-15 at ~100 Hz): the lattice-scale shift (E/E_Pl)² ~ 1e-81 is irrelevant.
- **What is not viable without tuning** is the IR Lorentz violation from loops. That is lanes RF/F2, not this lane.

## 5. Map to the FIXED readings

| Class | Exists? | Gravity-usable? |
|---|---|---|
| Undeformed, any K, bounded band | No (Theorem U) | — |
| DSR type (undeformed Lorentz/rotations, nonlinear on momenta), d ≥ 2 | No (Theorem R) | — |
| 1D nonlinear (any even V; MS type at V(π) = 0) | Yes; ∫F dH = 0, Euclidean region forced | No: no rotations; at bilinear order the structure functions must be c-numbers; Fock non-additive |
| First moment, deformed with F(H,P), d = 2, 3 | No for Morse cubic u (Theorem D) | It is the only smearing-generated one (Theorem S) |
| Non-first-moment, fully deformed, d ≥ 2 | Probably yes (one particle; SUGGESTED) | No: not a lapse smearing; needs a tower of new constraints |

**Lane reading for B1: FAIL (bounded)** to the scope stated at the top. Both FAIL disjuncts are met: no closing generator exists in classes U and DSR, and no smearing-generated generator closes in any class.

## Labels

**PROVED (same-family, unrefereed):**
- Theorems 0, U, S, D (Morse);
- the circle-action lemma and R1–R3 (R2 needs analyticity; R3 needs isolated zeros);
- the 1D classification and the orbit sum rules.

**CHECKED:** `b1_1d.out` and `b1_2d3d.out`, as cited above.

**SUGGESTED:** existence of fully deformed non-first-moment algebras.

**READING:**
- the higher-spin tower;
- Bojowald's analogy;
- the HDA Killing sector being undeformed on a flat background;
- "preferred frame, not DSR".

**COMPARATOR:**
- From memory: Conner–Raymond, Palais, Vasiliev, Amelino-Camelia, Magueijo–Smolin, AFKS, Hossenfelder, the Fermi-LAT numbers.
- Checked by search or fetch: BDP 1503.01017, Bojowald–Paily 1112.1899, LHAASO 2402.06009.

**Scope of "impossible":**
- free one-particle Bloch matter;
- the IR band isolated, so that the shell is a torus;
- smooth generators, with analyticity only where stated;
- cubic covariance for D;
- band touching and interacting or composite matter are not covered.
