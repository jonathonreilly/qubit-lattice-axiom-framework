# NORMS.md — the curvature-adapted norm for (H-C) / failure mode CURV-F2

Owner: the N1 (norms) worker, session 24. This file is append-only. It may be read by anyone; nobody else writes it.
Requests for other files are collected in the final section "FOR OTHER FILES (not edited)".

---

## §N0 PRE-STATED (first edit of this file, 2026-10-28 12:36:53 UTC; statements only; cites nothing produced in this session)

This section was written before any derivation in this session. It fixes the targets, the admissible outcomes and the
failure modes, so that the rest of the file can be read against it. Nothing below §N0 existed when §N0 was written.

**Scope.** Failure mode CURV-F2 of PROOF.md: the Lipschitz recursion of Lemma E3,
C_♭^{(i+1)} ≤ Z_col·Z_row²·C_♭^{(i)} + (1 + Z_col)(1 + Z_row)²·C_soft, compounds by Z_col·Z_row² ≈ 1.27·10³ per level in
absolute-value (N_0) sup norms, while the true one-level curvature contraction is K_p^♯ ≈ 0.11–0.13. The hypothesis
(H-C) (level-uniform constants, C_♭^{(i)} among them) is therefore not delivered by that recursion. The target is a
field-strength (curvature-adapted) norm in which the recursion is redone.

**T1 (the norm).** State a family of norms, one per level, with the same formula in own units up to a scale weight, that
is (i) gauge covariant, (ii) level-uniform in form, (iii) convertible to the sup-norm statements the consumers of (H-C)
use at a cost that does not contain L^{d-1}. It must be built on the already-specified norm 𝔐 of the BFT statement and on
the SF/RTARGET §33 pair (Hölder/X_c configuration norm, divergence-form source norm Y, level weights ω_l = L^{θ_w(k-l)},
exponential weights in level-k ancestor distance); no third norm is to be invented. The plain sup-curvature norm is
excluded.

**T2 (the blocking estimate).** Derive the quantity that replaces Z_col = 156.08 in the new norm, and the quantity that
replaces Z_row = 2.849. Give, for each, either a proof of an O(1) or L^{-2}-type bound, or a precise statement of the step
that forces a large value.

**T3 (the recursion).** State and prove the analogue of C^{(i+1)} ≤ A·C^{(i)} + B and determine A. Report A honestly,
including the case A ≥ 1.

**T4 (consumers).** Clause-by-clause compatibility with Proposition NAH-unif / NAH-unif′, BFT-4, and the level-uniform
form of (H-G); state for each whether a bound in the new norm is accepted, or what conversion is needed and at what cost.
State whether this route is an alternative to BFT-4 for the C_♭/(H-C) piece or a tool inside BFT-4's proof.

**T5 (θ_w).** Carry θ_w explicitly; report the range of θ_w for which the recursion constant satisfies A < 1, rather than
fixing one value. Report separately the weights that the already-proven linear estimates actually deliver.

**T6 (propagation).** Only if A < 1 is obtained: recompute the level-uniform background threshold, state the resulting
smallness condition, and state what happens to HW's g_K² ceiling. Do not edit HW.md or PROOF.md.

**Anti-circularity (binding, adopted from the BFT statement).** The route may not use the per-level covariances C^{(j)} as
Newton inverses. Any recursion that inverts C^{(j)} level by level is to be declared circular and withdrawn in favour of a
single composite estimate for 𝔉_k.

**Admissible outcomes, pre-registered.**
- (O1) A < 1 proven in the new norm, with the consumers accepting it: (H-C)'s C_♭ clause discharged.
- (O2) A < 1 proven conditionally on named inputs: CONDITIONAL, with the inputs named.
- (O3) A = 1 (marginality) with zero drive on the marginal direction and A_⊥ < 1 on the complement: discharged via a
  marginal/irrelevant split, with the split's hypotheses named.
- (O4) A ≥ 1 forced in every admissible norm: a no-go, with the forcing step named. This is an acceptable outcome and is
  to be reported as a no-go, not dressed as progress.

**Pre-registered failure modes for this session's own work.**
- (N-F1) The norm is strong enough to make A small but too weak for the consumers (a conversion that reintroduces L^{d-1}
  or L^{d-2}). Then report the conversion cost and declare the gain illusory.
- (N-F2) The gain is an artefact of a weight that is not level-consistent: a norm whose weights differ from the canonical
  own-units weights buys A < 1 only at the price of an equal factor in the initial condition. Any claimed A < 1 must be
  checked for weight-invariance of the product A × (weight mismatch over k levels).
- (N-F3) The estimate secretly assumes the smooth sector (bounds the branch response by its smooth-limit value) where the
  measured value is larger. Every use of a "smooth" value must be flagged and compared with the measured one.
- (N-F4) A bound on the third derivative at the trivial background is presented as a bound on the Lipschitz constant of
  Hess E^br on the small-field class. These are different statements and must be separated.
- (N-F5) The gauge freedom used to improve Z_row is not actually available (the admissible reparametrisations of the
  critical family are constrained, e.g. trivial at block centres). The admissible class must be stated and the
  construction must stay inside it.

**Not success.** Numerics in place of a proof; a norm defined only on the smooth sector; a statement for fixed k; a
claimed contraction whose constant is not exhibited as a function of (N, L, κ_±, d); any use of 1/K_p^♯ or of K_p^♯ itself
as if it were certified (it is measured, two rows, small tori).

---

## §N1 Scope, inputs, conventions

**What this file does.** It redoes Lemma E3's Lipschitz recursion in a curvature-adapted norm built on the norm 𝔐 of the
BFT statement (REVIEW_S22 l.389-398) and on the SF/RTARGET §33 norm pair. It does NOT touch the axioms, PROOF.md, HW.md or
any other lane file. Every item is labelled PROVEN-HERE / PROVEN (imported) / ARGUED / CONDITIONAL / OPEN.

**Headline, stated once, so that the rest can be read against it.**
1. Z_col·Z_row² ≈ 1.27·10³ is a norm artefact. In the field-strength norm the per-level factor is
   **A_per = 𝔠_vol·𝔠_ax²·(L²K̄)^a with a ∈ {1, 2, 3}**, i.e. **1.08 … 1.27 at the measured K̄ ≈ 0.12** — a gain of
   ≈ 0.9·10³ to 1.2·10³ per level (check n1-E: 920–1171).
2. **A_per < 1 is UNREACHABLE, and not because of a bad norm.** L²K̄ ≥ 1 with equality only in the smooth limit
   (K_p^♯ → 1/L² from below, REVIEW_S21 P), and the d = 4 cubic vertex is marginal, so **A ≥ 1 in every scale-covariant
   norm family** (Theorem N1-NOGO; the weight-invariance half is PROVEN, check n1-D). Any claimed A < 1 obtained by
   non-canonical weights is cancelled exactly by the weight mismatch in the initial condition. This is pre-registered
   failure mode N-F2, and it occurs for every per-level route.
3. **The per-level route is therefore the wrong object, and the composite route does not need A < 1 at all.** By
   TOWER-VAR (d) the level-k third derivative is a SINGLE pullback by the chain-minimiser map ζ^c, not a product of k
   per-level pullbacks. Its three scaling exponents are (d − 2, −1, −1) for the level-0 Wilson vertex, summing to
   **d − 4 = 0** (bounded, marginal, incurred ONCE), and (n + d − 1, −n, −n) for the level-j soft vertex (n := k − j),
   summing to **(d − 1) − n**, i.e. a per-level ratio **A_soft = 1/L = 1/3 < 1** whose sum over levels is
   L^{d−1}/(L − 1) = 27/2 in d = 4. **This is the deliverable: the recursion is not a recursion, it is a convergent
   geometric series, and (H-C)'s C_♭ clause is level-uniform at the trivial background.**
4. It is CONDITIONAL on exactly two named inputs, (N-Q) and (N-loc), plus the background extension (N-bg). Everything
   else is proven here or imported from PROVEN results (N2-lin, J-str, N2-exp, Lemma AX, TOWER-VAR, E3).

**Conventions.** d ≥ 2 (d = 4 the case of interest), L ≥ 3 odd, levels j = 0, …, k in their own units, n := k − j,
κ_j ∈ [κ_-, κ_+], κ̂ := κ_+/κ_-. d_j: level-j coboundary (1-forms → 2-forms); d_j^*: its adjoint. ι: the corner embedding
of 2-forms; J: the abelian lift (the coarse link value on its L^{d−1} crossing fine links); Q: the S4' average
(level-j 1-forms → level-(j+1) 1-forms); Q_str: its straight part, Q_str B(c) := L^{−(d−1)}Σ_{paths}Σ_{b∈path}σ_bB_b over
the L^{d−1} straight paths of L links. r_j := QB_j − B_{j+1}. 𝒦 := (1 − dC^0d^*)ι, 𝒦_ρ := −QC^0d^*ι,
𝒦_Z := 𝒦 − Zd_2, K_p(Z) := max_pΣ_P|𝒦_Z(p, P)|, K_ρ(Z') likewise (PROOF.md l.6058-6061). N_0(M) := max row ℓ¹ sum.
For a symmetric trilinear form T, **N3(T) := max_x Σ_{y,z}|T(x, y, z)| = sup{|T(δ_x, Y, W)| : x, |Y|_∞ ≤ 1, |W|_∞ ≤ 1}**;
this is the object that C_♭ is (PROOF.md l.6170-6176: "N_0(D³E_i[w]) ≤ C_♭^{(i)}|w|_∞").
K̄ := sup_i K_p^{(i)}(Z_i) as in (H-K). p_L := the S4' contour length bound (N_0(|Q|) ≤ p_L; p_L = 11 at L = 3, d = 4).

**Imported PROVEN inputs, with the exact statement used.**
- **(I1) Lemma E3** (PROOF.md l.6162-6176, PROVEN-HERE there, algebraic): D³_BE^br(0)[δB, ·, ·] = ζ^T(D³F[ζδB])ζ,
  ζ := (a'(0), 1).
- **(I2) Lemma TOWER-VAR (a), (c), (d)** (PROOF.md l.6464-6487, PROVEN-HERE there): 𝔉_k is a finite-range functional;
  E_k^br(V_k) = 𝔉_k(tower; V_k); the quadratic part at the trivial point is Setting SC's chain energy; and
  **D³E_k^br(1) = D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·]**, ζ^c the Setting SC minimiser map.
- **(I3) Theorem N2-lin** (LINEAR_PACKAGE v1.1 Thm 3.8, frozen): uniformly in k ≥ 1 and T,
  **sup|r_{k−1}| ≤ C_R sup|dB_k|** and **sup|f_0| ≤ C_f sup|dB_k|**, f_0 := L^{2k}dB_0, with C_R, C_f depending only on
  (L, κ_±).
- **(I4) Lemma J-str (b), (c)** (LINEAR_PACKAGE Lemma 3.1): at every critical point of Setting SC, d^*r_i = 0,
  r_{i−1} = (κ_i/κ_{i−1})Q_str^Tr_i, **sup|r_i| ≤ (κ_{k−1}/κ_i)L^{−(d−1)(k−1−i)}sup|r_{k−1}|**, and
  **Q^T = Q_str^T − h^Td^***, with ‖Q_str^T‖_{∞→∞} = L^{−(d−1)}.
- **(I5) Theorem N2-exp / N2-exp′** (LINEAR_PACKAGE Thms 4.2, 4.2′): uniformly in k, T and the fine offset, the
  B_k-symbols B_k ↦ r_{k−1} and B_k ↦ f_0 are analytic in the strip |Im p| < m_*′ and bounded by M there, and every
  infinite-lattice kernel entry obeys **|K(X)| ≤ Me^{−m′|X|_1}** for m′ < m_*′, in level-k units.
- **(I6) Lemma AX** (PROOF.md, used at l.6116-6117): on a non-wrapping box of side ℓ (own units) a gauge G exists with
  |log(GV)_b| ≤ 3ℓ·(max plaquette) on the box's links. Abelian/linearised form: |B − dλ|_∞ ≤ (d − 1)R|dB|_∞ on a box of
  side R (re-proved as Lemma N1-5 below so that the constant is explicit).
- **(I7) Lemma CURV-lin (i)** (PROOF.md l.6063-6083): the first-order branch displacement obeys x = −C^0d^*ιF_V,
  F_1 = d(Ja + x) = 𝒦F_V, ρ = 𝒦_ρF_V, with F_V = d_1a; slice- and fixing-independent.
- **(I8) The square identity** (SQ.md §0.2, used in Lemma SHIFT at SQ.md l.709-712): for a level-l 1-form s and m ≥ 0,
  d(Q_str^m s)(p) = L^{−d·m}Σ_y ∮_{∂sq_y} s over the L^{d·m} squares of side L^m, hence
  **|d(Q_str^m B)(p)| ≤ L^{2m}·sup|dB|** (each square's circulation is the flux of dB through its L^{2m} fine plaquettes)
  and |d(Q_str^m s)(p)| ≤ 4L^m sup|s|.
- **(I9) Theorem REG-lin (d)** (SQ.md l.725, PROVEN-HERE there, cone box): sup|dB_l| ≤ (C_0 + 4κ̂L²/(L² − 1))θL^{−2(k−l)}
  for 1 ≤ l ≤ k − 1, depth-uniformly. Used only as independent corroboration of Lemma N1-4, which is proved here on the
  torus from (I3), (I4), (I8).

**Measured, not certified, and used only where flagged.** K_p^♯ ≈ 0.1138–0.1236 (closed inputs, two rows, T = 4, 6;
REVIEW_S21 T), K_p^♯ → 1/9 = 1/L² from below in the smooth limit (REVIEW_S21 P: 0.0838, 0.1026, 0.1096, 0.1110, 0.11111),
K_ρ^♯ ≈ 2.07–2.61, Z_row = 2.849, Z_col = 156.08 (c37 D2, κ = 1, T = 8), R_3 ≈ 1.13–1.40 and
N3^abs(T_E)/N3(T_W) ≈ 24–30 (c38 B), c_3, c_2 → 1 in the smooth limit (c38 C).

---

## §N2 The norm family N^F (T1)

The family is 𝔐 restricted to what the third-derivative estimate needs, written in the §33 conversions. Nothing new is
invented; the three ingredients below are §33's coarse-unit weights, §33's divergence-form source norm, and §33's X_c
configuration norm.

**Definition N^F-1 (coarse units; the §33 weights).** For a level-l 2-form H put H^c := L^{θ_w(k−l)}H and for a level-l
1-form B put B^c := L^{θ_A(k−l)}B. The **canonical** weights are (θ_w, θ_A) = (2, 1), which are §33's own
("a level-l 2-form H has coarse-unit value H^c := L^{2(k−l)}H; a level-(i+1) 1-form r has r^c := L^{k−1−i}r"). θ_w, θ_A
are carried as parameters in §N5 and §N7; every statement labelled PROVEN is at the canonical pair unless said otherwise.

**Definition N^F-2 (the three leg norms).** For level-l objects, with the exponential weight of 𝔐 anchored at a level-k
link x and m ≥ 0 (dropped from the display when m = 0):
- **differentiated leg, divergence form (the ℓ¹ leg):** for a 1-form X,
  ‖X‖^{(1)}_{l,m} := L^{−θ_w(k−l)}·Σ_z e^{−m·d_k(z,x)}|(d_lX)(z)| over level-l plaquettes z, together with the soft
  component L^{−θ_w(k−l)}Σ_c e^{−m d_k(c,x)}|r_l(X)(c)| over level-l links. (This is §33's **divergence-form** choice: the
  leg is measured through the object it is a divergence/curl of — d_lX and r_l(X) — never through X itself.)
- **undifferentiated legs, configuration form (the ℓ^∞ leg):** for a 1-form Y,
  ‖Y‖^{(∞)}_{l,m} := L^{θ_A(k−l)}·sup_b e^{+m d_k(b,x)}|Y(b)| in a stated gauge, together with
  L^{θ_w(k−l)}sup_z e^{+m d_k(z,x)}|(d_lY)(z)|. This is §33's X_c pair
  ("||B||_{X_c} := max_i(||B_i||_{∞,m} + ||dB_i||_{∞,m}) for a stated gauge-fixed representative"), in coarse units.
- **vertex norm:** for a symmetric trilinear form T on level-l potentials,
  **𝔑_{l,m}(T) := sup{|T(X, Y, W)| : ‖X‖^{(1)}_{l,m} ≤ 1, ‖Y‖^{(∞)}_{l,m} ≤ 1, ‖W‖^{(∞)}_{l,m} ≤ 1}**, symmetrised over
  which leg sits in the ℓ¹ slot (i.e. the sup is over the three assignments as well).

**Remark N^F-3 (why this is the right object, and the three required properties).**
- (i) **Gauge covariance.** The ℓ¹ leg is gauge invariant outright: d_lX and r_l(X) are gauge invariant (J-str/CURV-lin).
  The ℓ^∞ leg is gauge-variant by necessity, not by choice: by the Ward identity
  T(d_lλ, Y, W) = −H([Y, λ], W) − H(Y, [W, λ]) (differentiate the gauge invariance of E twice in the field), T does NOT
  vanish on a pure-gauge leg, so **no norm that depends on Y only through d_lY can bound T**. §33's X_c makes the same
  choice ("for a stated gauge-fixed representative"), and §N3.2 below shows which gauge we are free to state.
- (ii) **Same formula at every level, up to the scale weight.** By construction: the only l-dependence is
  L^{θ_w(k−l)}, L^{θ_A(k−l)}.
- (iii) **Consumer strength.** At the canonical weights the weights CANCEL in 𝔑: for a level-l delta,
  ‖δ_b‖^{(1)}_{l,0} = L^{−θ_w(k−l)}·2(d − 1) and the ℓ^∞ legs carry L^{θ_A(k−l)}, so with (θ_w, θ_A) = (2, 1) one gets
  **𝔑_{l,0}(T) = own-units N3(T)/(2(d−1)) up to the stated normalisation**: the curvature-adapted norm is NOT weaker than
  the N_0 norm the consumers use, it is the same number organised differently. The conversion cost is 2(d − 1) = 6 and
  sup_b ≥ the axial inf, both free of L^{d−1} and of L^{d−2}. **Pre-registered failure mode N-F1 does not occur.**
  (§N8 does this clause by clause.)
- (iv) **The plain sup-curvature norm is excluded**, as 𝔐 requires: the ℓ¹ leg is a divergence-form norm, and §N6 never
  extends any response map to non-exact 2-forms. This is exactly why COMP-F1 does not occur here; see Remark N6-5.

---

## §N3 Structural lemmas

### Lemma N1-1 (field-strength representation of the composite cubic vertex): PROVEN-HERE

*Statement.* The cubic Taylor form of 𝔉_k at the trivial point is, exactly,
  **D³𝔉_k(1)[X, Y, W] = Σ_{p ∈ P_0} ⟨(d_0X_0)_p, 𝔅_p(Y_0, W_0)⟩_sym + Σ_{j=0}^{k−1} κ_j Σ_{c ∈ C_j} ⟨r_j(X), 𝔟^{(j)}_c(Y_j, W_j, Y_{j+1}, W_{j+1})⟩_sym**,
where X_j, Y_j, W_j denote the level-j components of the composite displacement, "sym" means the symmetrisation over
which of the three arguments occupies the first (differentiated / residual) slot, 𝔅_p is bilinear with support on the four
links of p and ℓ¹ coefficient mass **M_W ≤ 6** (a plaquette has four links, C(4, 2) = 6 ordered pairs, BCH coefficient ½,
commutator factor 2; the count is the same in every d), and 𝔟^{(j)}_c is bilinear with support within the
S4' contour of c (≤ p_L level-j links plus the one level-(j+1) link) and ℓ¹ coefficient mass M_S = M_S(L, d, N) < ∞, the
same function in own units at every level.

*Proof.* (a) **Level 0 (Wilson).** With the ledger's normalisation S_W = Σ_p Re tr(1 − U_p) and X_p := log U_p ∈ su(N):
tr X_p = 0 and Re tr X_p³ = 0 (for anti-Hermitian X, (X³)^† = −X³, so tr X³ is purely imaginary), hence
Re tr(1 − e^{X}) = ½|X|²_HS − (1/24)Re tr X⁴ − … with |X|²_HS = −tr X² = ⟨X, X⟩. So
**S_W = ½Σ_p|log U_p|² + O(|log U_p|⁴)**, and the quartic and higher terms contribute nothing at cubic order in the
potential. Writing U_b = e^{A_b} and U_p = e^{σ_1A_1}⋯e^{σ_4A_4} (the ordered product round p),
log U_p = (dA)_p + Q_2(A)_p + O(A³) with Q_2(A)_p = ½Σ_{i<j}σ_iσ_j[A_{(i)}, A_{(j)}] (the quadratic BCH term; four links,
C(4, 2) = 6 ordered pairs, coefficient ½). Hence the cubic part of S_W is **Σ_p⟨(dA)_p, Q_2(A)_p⟩** — exactly one
coboundary per term. Set 𝔅_p := Q_2 and, with |[X, Y]|_HS ≤ 2|X|_HS|Y|_HS, M_W ≤ 6·½·2 = 6.
(b) **Level j (soft).** In the ledger's normalisation φ̂ = ½|ρ|² + O(ρ⁴) (TOWER-VAR (c)), with
ρ_c = X_0(M̄_c(e^{A_j})V_c^{−1}), and ρ = ρ_1 + ρ_2 + O(A³) with ρ_1 = QA_j − A_{j+1} = r_j (left-trivialised linear part)
and ρ_2 quadratic in (A_j, A_{j+1}). There is no cubic-in-ρ term, so the cubic part of κ_jΣ_cφ̂_c is
**κ_jΣ_c⟨ρ_1(c), ρ_2(c)⟩ = κ_jΣ_c⟨r_j(c), ρ_2(c)⟩** — exactly one residual per term. ρ_2 is a finite sum of commutators
of the A-values along the S4' contour of c plus the X_0-quadratic (the c_W term of CURV1's ρ-proof) and the averaging
weights; its ℓ¹ mass M_S is a function of (L, d, N) only, finite by NA-alg (a) (X_0 analytic with identity linear part),
and the SAME function at every level because every soft term "is the same function in own units" (TOWER-VAR). An
indicative explicit form is M_S ≤ (1 + 2c_W)p_L², not evaluated here.
(c) D³ of a form Σ⟨ℓ(A), 𝔮(A, A)⟩ with ℓ linear and 𝔮 bilinear is
Σ[⟨ℓ(X), 𝔮(Y, W) + 𝔮(W, Y)⟩ + ⟨ℓ(Y), 𝔮(X, W) + 𝔮(W, X)⟩ + ⟨ℓ(W), 𝔮(X, Y) + 𝔮(Y, X)⟩], which is the symmetrisation
displayed. ∎

*What it is.* The statement that the cubic vertex of the whole composite functional carries **exactly one derivative (or
one residual) per term**. This is the precise form of PROOF.md's sentence "the d = 4 cubic vertex is marginal only after
one leg is differentiated". It is an identity, not an estimate, and it is what makes the divergence-form leg of §N2
available. *What it is not:* a statement about quartic or higher order (the O(X⁴) and O(ρ⁴) tails are dropped only because
they do not contribute at cubic order), nor a statement at a non-trivial background.

### Lemma N1-2 (admissible reparametrisations of the critical family): PROVEN-HERE

*Statement.* Lemma E3's identity and TOWER-VAR (d) hold for **every** differentiable gauge reparametrisation of the
critical family: if a(B) is a critical family and Λ(B) is any differentiable family of gauge parameters that is admissible
(trivial at the coarse centres of the level whose data is held fixed, so that F_i(·, B) is invariant under it), then
a_Λ(B) := a(B) + D_UΛ(B) is again a critical family and
  **D³_BE^br(0)[δB, ·, ·] = ζ_Λ^T(D³F[ζ_ΛδB])ζ_Λ,  ζ_Λ := (a'(0) + D_UΛ'(0), 1).**
The same holds for ζ^c in TOWER-VAR (d), with Λ a family of fine gauges whose restrictions to the level-j centres are the
induced level-j gauges.

*Proof.* F_i(·, B) is invariant under the fluctuation gauge group (gauge transformations trivial at the coarse centres:
CURV-lin's proof, "another slice or fixing changes x by D_0λ with λ in the fluctuation gauge (λ(c_X) = 0)"), so a gauge
transform of a critical point is a critical point and E^br(B) = F(a_Λ(B), B) is the SAME function of B. E3's derivation
uses only (i) that a_Λ is a differentiable critical family and (ii) that the A-component of F_zzζ_Λ vanishes, which is
F_AAa_Λ' + F_AB = F_AAa' + F_AB + F_AAD_UΛ' = 0 + 0, because F_AA annihilates gauge directions at a critical point
(Lemma NA-inv, as quoted in Lemma SC1's proof). Hence the derivation goes through verbatim. ∎

*Why it matters.* Z_row = 2.849 ≥ 1 is a property of BR1's slice, not of the branch: in that slice a pure-gauge coarse
direction B = d_1λ has F_V = d_1B = 0, so x = 0 and ζB = Jd_1λ is the **concentrated** lift (the whole coarse holonomy on
the L^{d−1} crossing links), giving |ζB|_∞ = |B|_∞ and therefore Z_row ≥ 1 identically. Lemma N1-2 says we may replace
it by a spread representative. **Pre-registered failure mode N-F5 is the constraint Λ|centres = 0; it is respected
everywhere below (Lemma N1-6 constructs Λ as an interpolant that is exact at the centres).**

### Lemma N1-3 (exact curvature identities for the branch map): PROVEN (imported, re-derived)

*Statement.* At the trivial background, with ζ := J − C^0d^*ι d_1 the linear branch map,
  **d∘ζ = 𝒦 d_1  and  Q∘ζ − 1 = 𝒦_ρ d_1,** exactly.
*Proof.* (I7) gives x = −C^0d^*ιF_V, F_V = d_1a, so ζa = Ja + x. Lemma U0 (i)-(ii) give QJ = 1 and dJ = ιd_1. Hence
dζ = ιd_1 − dC^0d^*ιd_1 = (1 − dC^0d^*)ιd_1 = 𝒦d_1 and Qζ = 1 − QC^0d^*ιd_1 = 1 + 𝒦_ρd_1. ∎
(c38 A1 checks both numerically: dÛ = 𝒦d_1 to 2.7·10⁻¹⁵, QÛ − 1 = 𝒦_ρd_1 to 1.3·10⁻¹⁴.)

*Consequence (the exactness of the input; pre-registered failure mode NORM-F2 as the lead states it).* The input to 𝒦 is
**d_1a, the coboundary of a potential — exactly closed, in fact exact.** The closed-input restriction that takes
K_p from 2.27 to ≈ 0.12 therefore survives the blocking map trivially in the linear/trivial-background setting, and no
Z-representative and no Z-tail (N_0(|Z|) in C_θ) is needed at all: K_p(Z) may be replaced by the exact-input row norm.
The Bianchi defect, the Zd_2F term and the tails of Z return ONLY in the background extension (N-bg), where F^G = log V_P
is merely approximately closed (|d_2F^G| ≤ 54αε + 2880ε², CURV1 step (5)). **So NORM-F2 does not occur in §N6; it is
confined to (N-bg), and that is where it must be re-examined.**

### Lemma N1-4 (intermediate-level curvature decay, θ_w = 2, on the torus): PROVEN-HERE

*Statement.* Let (B_0, …, B_{k−1}) be the Setting SC chain minimiser for level-k data B_k on the torus, θ := sup|d_kB_k|.
Then for every 0 ≤ j ≤ k − 1, uniformly in k and T,
  **sup|d_jB_j| ≤ c_F·L^{−2(k−j)}·θ,  c_F := C_f + 4κ̂C_R·L²/(L² − 1).**
*Proof.* j = 0 is (I3): sup|d_0B_0| = L^{−2k}sup|f_0| ≤ C_fL^{−2k}θ. For j ≥ 1, iterate B_{i+1} = QB_i − r_i and use
J-str (b) (at a critical point the funnel part of Q^T is killed on co-closed r, and r is co-closed by J-str (a)), so that
the transport of the fields may be taken with Q_str where only curvatures are read:
B_j = Q_str^{j}B_0 − Σ_{i<j}Q_str^{\,j−1−i}r_i modulo a level-j pure gauge (see (N-Q) below; a pure gauge does not change
d_jB_j, so this step is unconditional for the curvature). Apply d_j and (I8):
  sup|d_jB_j| ≤ L^{2j}sup|d_0B_0| + Σ_{i<j}4L^{\,j−1−i}sup|r_i|.
The first term is ≤ C_fL^{2j−2k}θ = C_fL^{−2(k−j)}θ. For the second, (I3)+(I4) give
sup|r_i| ≤ κ̂C_RL^{−(d−1)(k−1−i)}θ, so at d = 4 the exponent of the i-th term is (j−1−i) − 3(k−1−i) = j + 2 − 3k + 2i,
a geometric sum in i with ratio L² dominated by i = j − 1:
  Σ_{i<j}4L^{\,j+2−3k+2i} = 4L^{\,j+2−3k}(L^{2j} − 1)/(L² − 1) ≤ 4·L²/(L² − 1)·L^{−3(k−j)}.
Since L^{−3(k−j)} ≤ L^{−2(k−j)}, the two terms give the stated constant. ∎
*Corroboration.* This reproduces SQ's Theorem REG-lin (d) constant C_0 + 4κ̂L²/(L² − 1) exactly (I9), proved there on the
cone box by an independent route (STOKES-NA / STOKES-it, whose coefficient is "exactly L²", SQ.md l.1268). Two
independent derivations of the same constant.
*Reading.* **θ_w = 2 is what the linear chain delivers for the curvature, and θ_w = d − 1 = 3 for the residuals**
(J-str (c)). Both exceed every live consumer's requirement (§N7).

### Lemma N1-5 (lattice axial gauge, explicit constant): PROVEN-HERE (abelian/linearised); PROVEN (imported) nonabelian

*Statement.* Let Λ be a box of side R in Z^d and B an (abelian, or su(N)-valued linearised) 1-form on Λ. Then there is
λ: sites(Λ) → su(N) with **|B − dλ|_∞ ≤ (d − 1)·R·|dB|_∞** on Λ.
*Proof.* Order the directions 1, …, d. Integrating along direction 1 from the face x_1 = 0 fixes λ so that B_1 ≡ 0 on Λ
(a tree gauge in a box). The residual freedom is λ independent of x_1. Use it to set B_2 ≡ 0 on the slice x_1 = 0
(integrate along direction 2 inside that slice). Then B_2(x) = Σ_{y_1<x_1}F_{12}(y_1, x_⊥), so |B_2| ≤ R|dB|_∞. The
residual freedom is now λ independent of x_1, x_2; use it to set B_3 ≡ 0 on {x_1 = x_2 = 0}, giving
B_3(x) = Σ_{y_1<x_1}F_{13} + Σ_{y_2<x_2}F_{23}(0, y_2, ·) and |B_3| ≤ 2R|dB|_∞. Inductively |B_μ| ≤ (μ − 1)R|dB|_∞. ∎
Nonabelian: Lemma AX (I6) is the same statement with constant 3 in place of (d − 1), under its smallness conditions.
We write c_AX := max(d − 1, 3).

### Lemma N1-6 (spread representative of a pure-gauge datum): PROVEN-HERE

*Statement.* Let λ be a function on level-k sites. There is a nested family of interpolants λ̂_j on level-j sites,
j = 0, …, k, with λ̂_k = λ, λ̂_j restricted to level-(j+1) centres equal to λ̂_{j+1} (so the family is an admissible
reparametrisation in the sense of Lemma N1-2), and
  **|d_jλ̂_j|_∞ ≤ L^{−(k−j)}|d_kλ|_∞ for every j.**
*Proof.* Define λ̂_j by multilinear interpolation of λ from the level-k lattice to the level-j lattice (coordinates
measured in level-j units, with the level-k sites at the level-j points of coordinate ≡ 0 mod L^{k−j}). The interpolant
agrees with λ at level-k sites, hence with λ̂_{j+1} at level-(j+1) centres (the interpolants are nested because
multilinear interpolation on a refined grid of the same cells restricts to multilinear interpolation). For a unit step in
direction μ at level j, the difference of the multilinear interpolant is the corresponding convex combination of the
level-k differences (d_kλ)_μ divided by L^{k−j}. ∎
*Use.* This is the lever of Lemma N1-2 made explicit: a coarse pure gauge of own-units size 1 is realised at level j with
own-units size L^{−(k−j)}, not 1. It is what replaces Z_row ≥ 1.

### Lemma N1-7 (ℓ¹ mass from a sup bound plus exponential locality): PROVEN-HERE given (I5)

*Statement.* Let 𝔎 be a kernel from level-k 2-forms to level-l objects of type τ ∈ {plaquettes, links} with
|𝔎(z, P)| ≤ 𝔐_0 e^{−m′d_k(z,P)} (level-k distance). Then for a level-k link x, with n_τ(l) := the number of level-l
objects of type τ per level-k cell and c_m := (coth(m′/2))^d,
  **Σ_z |(𝔎 d_kδ_x)(z)| ≤ 2(d − 1)·𝔐_0·n_τ(l)·c_m.**
In particular n_plaq(0) = d(d−1)/2·L^{dk} and n_link(j) = d·L^{d(k−j)}.
*Proof.* |d_kδ_x| is supported on the 2(d − 1) level-k plaquettes containing x and equals 1 there. Hence
Σ_z|(𝔎d_kδ_x)(z)| ≤ 2(d−1)𝔐_0Σ_z e^{−m′d_k(z,x)}; grouping the level-l objects by the level-k cell containing them gives
n_τ(l)·Σ_{X∈Z^d}e^{−m′|X|_1} = n_τ(l)c_m. ∎

---

## §N4 What replaces Z_col and Z_row (T2)

E3's two constants are, by definition, Z_row = sup{|ζB|_∞ : |B|_∞ ≤ 1} = max_bΣ_c|a'(b, c)| and
Z_col = max_cΣ_b|a'(b, c)| = sup{|ζδ_c|_{ℓ¹}}. Both are **ℓ^p norms of the branch map applied to the POTENTIAL**. In the
norm N^F the potential never appears in the differentiated slot, so each is replaced by a different object.

### (a) The differentiated slot: Z_col ↦ ‖𝒦_Z‖_{ℓ¹→ℓ¹} + ‖𝒦_{ρ,Z'}‖_{ℓ¹→ℓ¹}

**Proposition N1-8 (mass balance): PROVEN-HERE.** Let 𝔎 be a kernel from level-(i+1) 2-forms to level-i objects of type
τ, invariant under level-(i+1) translations. Let ρ_row := the average over the level-i objects of type τ in one level-(i+1)
cell of the row ℓ¹ sum, and ρ_col := the average over the d(d−1)/2 level-(i+1) plaquettes of a cell of the column ℓ¹ sum.
Then
  **ρ_col = [n_τ(i)/n_plaq(i+1)]·ρ_row,**
with n_τ(i) the number of level-i objects of type τ per level-(i+1) cell. In particular, for 𝒦 (fine plaquettes)
n_plaq/n_plaq = L^d, so **ρ_col(𝒦) = L^d·ρ_row(𝒦) ≤ L^d·K_p(Z)**, and for 𝒦_ρ (coarse links)
**ρ_col(𝒦_ρ) = [d/(d(d−1)/2)]·ρ_row(𝒦_ρ) = (2/(d−1))·ρ_row(𝒦_ρ) ≤ (2/(d−1))K_ρ(Z′)**.
*Proof.* Count the total mass Σ|𝔎(z, P)| over z in one cell and all P in two ways, using level-(i+1) translation
invariance to identify the P-sum over a cell. ∎

**Corollary N1-9 (column bound): PROVEN-HERE given a decay statement.** If moreover |𝔎(z, P)| ≤ 𝔐_0e^{−m d(z,P)} then
  **max_PΣ_z|𝔎(z, P)| ≤ n_τ(i)·c_m·max_z Σ_{P'}|𝔎(z, P')| ≤ n_τ(i)·c_m·(row norm),** c_m = (coth(m/2))^d.
*Proof.* |𝔎(z, P)| ≤ min(row norm, 𝔐_0e^{−md}) and Lemma N1-7's grouping. ∎

**The numbers.** With L = 3, d = 4 and the measured closed-input K̄ = 0.1202 (row 252, T = 4; the largest measured
closed-input value is 0.1236 at T = 6):
  L^d·K̄ = **9.74** (resp. 10.01),  (2/(d−1))K_ρ^♯ = (2/3)·2.219 = **1.48** (resp. 1.74 at K_ρ^♯ = 2.614),
against **Z_col = 156.08**. So in the differentiated slot the replacement is **≈ 9.7 + 1.5 ≈ 11.2 instead of 156**,
a gain of **≈ 14** (check n1-E prints the ratio 16.0 for the 𝒦 part alone). Status: the identity of
Proposition N1-8 is PROVEN; the *value* inherits exactly the status of (H-K) — measured, two rows, small tori, not
certified — and the max-vs-average step needs Corollary N1-9's decay input, which is available (𝒦's decay profile is
measured in c37 B: 0.315, 0.157, 3.1e-3, 3.2e-4, 5.2e-5, 1.2e-5 by coarse ℓ^∞ distance) but, like K̄, not certified.

**Which step forces the residual L^{d−2} ≈ 9.** Exactly the volume factor n_plaq(i) = L^d·n_plaq(i+1): one coarse
plaquette has L^d fine plaquettes under it, each receiving ≈ K̄ ≈ L^{−2} of the coarse curvature. **PROOF.md's diagnosis
named "the L^{d−1} = 27 crossing links of one coarse link times the spread"; the correct count is L^d·K̄ ≈ L^{d−2}, and
the crossing-link count does not appear at all** once the leg is measured through d_1X rather than through X: the
L^{d−1} crossing links are an artefact of the lift J, which acts only on the potential.

### (b) The undifferentiated slots: Z_row ↦ 𝔠_ax·L^{−1} per level, L^{−(k−j)} composite

**Proposition N1-10 (spread representative, one level): PROVEN-HERE given Lemma N1-4's one-level analogue.** There is an
admissible representative ζ_sm (Lemma N1-2) with
  **|ζ_sm B|_∞ ≤ L^{−1}·[(d−1)·L·|d(ζB)|_∞ ·L + |B|_∞ + K_ρ|d_1B|_∞] ≤ 𝔠_ax·L^{−1}·(|B|_∞ + |d_1B|_∞)**
in the stated gauge, 𝔠_ax = 𝔠_ax(L, d, K̄, K_ρ): the holonomy part of the response is spread over the L steps of each
block-to-block path (Lemma N1-6), and the curvature part is bounded by the block-axial integral of d(ζB) = 𝒦d_1B
(Lemma N1-3, Lemma N1-5 with R = L).
*Reading.* The **smooth-sector value is exactly L^{−1} = 0.333**, against the measured Z_row = 2.849 in BR1's slice: a
factor **8.55** per leg, 73 in the two legs (check n1-E). Per pre-registered failure mode N-F3 this is flagged: L^{−1} is
a smooth-sector value and the honest claim is L^{−1}·𝔠_ax with 𝔠_ax ≥ 1 not evaluated here. Z_row = 2.849 is NOT a
counterexample to it — it is the value in a different (concentrated) representative, which Lemma N1-2 licenses us to
discard.
**Composite version (the one actually used): Lemma N1-11 below, with 𝔠_P·L^{−(k−j)}, and it is PROVEN-HERE.**

### Lemma N1-11 (composite potential bound, θ_A = 1): PROVEN-HERE given (N-Q)

*Statement.* Let Y be level-k data, θ := sup|d_kY|, and let R_eff ≥ 1 (level-k units) be a box side. Assume **(N-Q)**
below. Then there is an admissible representative ζ^c_sm of the chain-minimiser map (Lemma N1-2) and a single fine gauge
on the box such that, for every 0 ≤ j ≤ k,
  **|ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P·L^{−(k−j)}·sup|Y|_∞,  𝔠_P := 2[c_AX R_eff C_f·𝔮_0 + 𝔮_0·4κ̂C_R L²/(L² − 1)] + 2,**
where 𝔮_0 is (N-Q)'s constant.
*Proof.* (1) Split Y = Y′ + d_kλ with λ the level-k axial gauge of the box (Lemma N1-5), so |Y′|_∞ ≤ c_AXR_eff·θ and
|d_kλ|_∞ ≤ |Y|_∞ + |Y′|_∞. (2) For the pure-gauge part use Lemma N1-6: its contribution at level j is d_jλ̂_j with
|d_jλ̂_j|_∞ ≤ L^{−(k−j)}|d_kλ|_∞, and the family is admissible and nested, so one fine gauge realises it at all levels
simultaneously. (3) For Y′: apply Lemma N1-5 at level 0 on the box, of level-0 side R_0 = R_effL^k, together with (I3):
|B_0|_∞ ≤ c_AX·R_effL^k·sup|d_0B_0| ≤ c_AXR_effC_f·L^{−k}·sup|d_kY′| ≤ c_AXR_effC_f L^{−k}·2d|Y′|_∞ — and read it,
equivalently and more usefully, directly in θ: |B_0|_∞ ≤ c_AXR_effC_fL^{−k}θ. (4) Transport upward:
B_j = Q^{j}B_0 − Σ_{i<j}Q^{\,j−1−i}r_i; by **(N-Q)** ‖Q^{j}‖_{∞→∞} ≤ 𝔮_0L^{j}, hence with (I3)+(I4)
  |B_j|_∞ ≤ 𝔮_0L^{j}·c_AXR_effC_fL^{−k}θ + 𝔮_0Σ_{i<j}L^{\,j−1−i}κ̂C_RL^{−(d−1)(k−1−i)}θ
          ≤ 𝔮_0[c_AXR_effC_f + 4κ̂C_RL²/(L² − 1)]·L^{−(k−j)}θ
(the second sum is the one evaluated in Lemma N1-4's proof, bounded by 4L²/(L² − 1)·L^{−3(k−j)} ≤ … ·L^{−(k−j)}).
(5) Add (2) and (4), and use θ ≤ 2d|Y|_∞ and |d_kλ|_∞ ≤ 2|Y|_∞; absorb 2d into 𝔠_P's displayed factor 2. ∎

**(N-Q) [named input; the one small gap in Lemma N1-11].** ‖Q^{j}‖_{∞→∞} ≤ 𝔮_0L^{j} for a constant 𝔮_0 = 𝔮_0(L, d),
uniformly in j — equivalently, the composite S4′ average has weighted contour length O(L^j).
- It is **immediate with 𝔮_0 = 1 for the straight average**: ‖Q_str^{j}‖_{∞→∞} = L^{j} exactly (a straight composite
  contour is L^j fine links; the transverse averaging weights sum to 1). Cf. (I4)'s ‖Q_str^T‖_{∞→∞} = L^{−(d−1)} and
  (I8)'s "Q^m is the straight average over L^m-blocks".
- For the full S4′ average the crude bound is ‖Q^{j}‖ ≤ p_L^{j}, which is **insufficient**: it would make the soft
  vertices compound by (p_L/L)² = (11/3)² ≈ 13.4 per level and reintroduce depth-dependence. So (N-Q) is exactly the
  statement that the funnel (axial) legs do not accumulate in the composite transport.
- What makes (N-Q) plausible and what it needs. By (I4), Q^T = Q_str^T − h^Td^*, i.e. **Q = Q_str − d_{j+1}∘h**: the
  funnel part of Q is an EXACT (pure-gauge) correction at level j + 1. Expanding Q^{j} = Π(Q_str − d h) therefore gives
  Q_str^{j} plus terms each of which is a level-j pure gauge, so (i) **the curvature statement Lemma N1-4 is unaffected**
  (a pure gauge has no curvature) — that step is unconditional — and (ii) (N-Q) reduces to bounding the gauge functions of
  those correction terms by 𝔮_0L^{j}, i.e. to pure-gauge bookkeeping. Each term with its first h at level i contributes
  ≲ ‖h‖·L^{j−1−i}·L^{i} = ‖h‖L^{j−1} if the subsequent factors act on it as Q_str does on a pure gauge
  (Q_str d_iμ = d_{i+1}(μ|centres), which does not grow the gauge function), giving 𝔮_0 ≤ 1 + 2d‖h‖·j/L — only
  POLYNOMIAL in j, which is still enough (see §N6, Remark N6-4). The step not done here is that h applied to a pure
  gauge again produces a controlled gauge function.
- Status: **ARGUED, reduced to pure-gauge bookkeeping; a one-line check if Setting SC's Q is the straight average
  (then 𝔮_0 = 1 and Lemma N1-11 is PROVEN outright).** This is a question about a DEFINITION, not a theorem; it is
  the first item of the FOR OTHER FILES list.

**(N-loc) [named input].** The representative of Lemma N1-11 can be chosen with exponential locality in level-k ancestor
distance: |ζ^c_{sm,j}δ_x(b)| ≤ 𝔠_PL^{−(k−j)}e^{−m d_k(b,x)} and |ζ^c_{sm,j}Y(b)| ≤ 𝔠_PL^{−(k−j)}sup_{b′}e^{−md_k(b,b′)}|Y(b′)|.
- For the gauge-INVARIANT content this is PROVEN: (I5) gives exponentially local kernels for B_k ↦ f_0 and B_k ↦ r_{k−1},
  and (I4) transports r_i locally. It is the gauge-VARIANT representative whose locality is not proven: Lemma N1-5's
  axial construction is anchored at a box corner, not at x.
- What would give it: a shell-wise axial construction (axial gauge on dyadic shells around x, glued with the exponential
  decay of the curvature and residual kernels), i.e. a multi-scale axial gauge. PROOF.md already records this as the open
  half of (CL-1) ("The background dependence of 𝔊_k … needs a composite LOC with multi-scale axial gauges: OPEN").
- Status: **ARGUED.** It is used only to convert the sup bounds of Lemma N1-11 into ℓ¹ masses (Lemma N1-7); a box
  truncation with a near/far split gives the same conclusion with 𝔠 carrying a factor R_eff^d and an additive
  Me^{−m′R_eff} far term, so (N-loc) can be traded for an explicit near/far split. That trade is stated, not carried out.

---

## §N5 The per-level recursion, and why A < 1 is unreachable there (T3, part 1)

### Theorem N1-12 (per-level field-strength recursion): PROVEN-HERE given Proposition N1-10 and Corollary N1-9

*Statement.* Let T_i be the cubic Taylor form of E_i^br at the trivial background, in the field-strength representation of
Lemma N1-1, with M_i := the ℓ¹ coefficient mass of its representation. Then, with 𝔎_col := max_P[Σ_p|𝒦_Z(p, P)| +
Σ_c|𝒦_{ρ,Z′}(c, P)|] and Z^{sm} := the sup norm of the spread representative of Proposition N1-10,
  **M_{i+1} ≤ A_per·M_i + B_per,  A_per = 𝔎_col·(Z^{sm})²,  B_per = 𝔎_col^{ρ}·(1 + Z^{sm})²·M_S,**
and in the canonical weights 𝔑_{i+1}(T_{i+1}) ≤ A_per·𝔑_i(T_i) + B_per.
*Proof.* By Lemma N1-1, T_i(X, Y, W) = Σ_p⟨(dX)_p, 𝔅_p(Y, W)⟩_sym. Pull back by ζ: by Lemma N1-3,
(dζX)_p = (𝒦d_1X)_p, so Σ_p⟨(𝒦d_1X)_p, 𝔅_p(ζY, ζW)⟩ = Σ_P⟨(d_1X)_P, 𝔅′_P(Y, W)⟩ with
𝔅′_P := Σ_p𝒦_Z(p, P)𝔅_p(ζ·, ζ·) — i.e. **the pullback stays in the field-strength class**, with ℓ¹ mass
≤ 𝔎_col·(Z^{sm})²·M_i. Likewise the soft terms, with 𝒦_ρ in place of 𝒦 (Lemma N1-3's second identity) and the extra
level-(i+1) argument contributing the (1 + Z^{sm}) factors. ∎

**Evaluation.** 𝔎_col ≤ 𝔠_vol·(L^dK̄ + (2/(d−1))K̄_ρ) (Corollary N1-9, Proposition N1-8) and Z^{sm} ≤ 𝔠_ax/L
(Proposition N1-10), so
  **A_per ≤ 𝔠_vol𝔠_ax²·L^{d−2}·K̄·L^{−2} = 𝔠_vol𝔠_ax²·L^{d−4}·(L²K̄).**
At d = 4, L = 3 and the measured K̄: **L²K̄ = 1.0818 (K̄ = 0.1202) or 1.1124 (K̄ = 0.1236)**, and the three ways of tying
the two undifferentiated legs to the curvature (Remark N1-14) give A_per = 𝔠(L²K̄)^a, a ∈ {1, 2, 3}, i.e.
**A_per ∈ [1.08, 1.38]·𝔠_vol𝔠_ax²** against **Z_colZ_row² = 1266.87**: a gain of **920–1171** (check n1-E).

### Theorem N1-13 (NO-GO: A ≥ 1 in every scale-covariant norm family)

*Statement.* (i) **[PROVEN-HERE]** Let the norms be weighted by (θ_w, θ_A) as in Definition N^F-1. Then the product of
the per-level factor over k levels, times the weight mismatch of the level-0 initial condition relative to the canonical
pair (2, 1), is **independent of (θ_w, θ_A) and equals L^{(d−4)k}·(L²K̄)^{ak}**. Hence **no choice of level weights can
produce a contraction that is not already present at the canonical weights.**
(ii) **[ARGUED]** At the canonical weights the factor is L^{d−4}·(L²K̄)^a with L²K̄ ≥ 1, equality only in the smooth
limit. Hence **A_per ≥ 1 in d = 4**, with equality only in the smooth limit, and A_per < 1 is unreachable.

*Proof of (i).* 𝔑 is defined by the three leg norms; changing (θ_w, θ_A) multiplies the level-l value of 𝔑 by
L^{(θ_w−2)(k−l)+2(1−θ_A)(k−l)}·(a fixed factor). Hence log_L A(θ_w, θ_A) = log_L A(2, 1) + [(2 − θ_w) + 2(θ_A − 1)] and
the mismatch of the level-0 initial condition is exactly −k[(2 − θ_w) + 2(θ_A − 1)]. The two cancel.
Checked symbolically in check n1-D at six pairs (θ_w, θ_A) ∈ {0, 1, 2} × {0, 1}: the invariant is log_L = d − 4 at every
pair, **PASS**. ∎
*Proof of (ii), as far as it goes.* The exponent count: one coarse plaquette carries L^d fine plaquettes (volume), each
receiving K̄ of the coarse curvature, and each undifferentiated potential leg contracts by L^{−1}; so the factor is
L^d·K̄·L^{−2} = L^{d−4}(L²K̄). The three ingredients are the own-units scaling dimensions of the d = 4 cubic vertex:
L^{d−4} = 1 is the statement that it is **marginal**, and the check reproduces the whole power counting
(L^{d−4} = L^{−1} at d = 3, super-renormalisable; = 1 at d = 4, marginal; = L at d = 5, relevant: check n1-A, **PASS**).
The remaining factor L²K̄ ≥ 1 is the lattice excess of K_p^♯ over its smooth value: REVIEW_S21 P records
K_p^♯ → 0.11111 = 1/L² from BELOW in the smooth limit and PROOF.md records "the smooth bound ≥ 1/9", while the measured
closed-input values 0.1138–0.1236 all exceed 1/L². ARGUED, because (a) K_p^♯ on Z⁴ is not certified and (b) the
identification of the exact marginal eigenvalue with c_3 (c38 C: c_3 = 0.974, 0.9977, 0.99974, 0.999977 at s = 0.1, 0.03,
0.01, 0.003, → 1) is a measurement, not a proof. ∎

**Remark N1-14 (where the exponent a comes from, and why it does not matter).** The two undifferentiated legs are
potentials; bounding them needs both components of the X_c pair (Proposition N1-10's bound has a |d_1B| term), so the one-level
map on the pair is upper triangular with diagonal (L^{θ_A−1}, L^{θ_w}K̄) = (1, L²K̄) at the canonical weights and an
off-diagonal entry that decays with depth. Reading the undifferentiated factor as the diagonal max gives a = 3; reading
it as the potential entry alone gives a = 1. In every reading A_per ≥ 1 and A_per ≤ 1.38, so the ambiguity is a factor
1.3, irrelevant next to the 10³ it replaces and next to the fact that A_per ≥ 1.

**Conclusion of §N5 (pre-registered outcome O4 for the per-level route).** **Failure mode CURV-F2 is ≈ 10³ times less
severe than PROOF.md records, but it does NOT close in the per-level route, and no norm closes it there.** The obstruction
is not the norm; it is that the d = 4 cubic vertex is marginal, so the per-level map cannot contract. Any per-level route
therefore gives at best C_♭^{(k)} ≈ k·B_per (linear in the depth, if A_per = 1 exactly) or (L²K̄)^k ≈ 1.1^k (with the
measured excess) — against 1267^k now. **The binding condition is A_per ≤ 1, not A_per < 1/K̄: the constants C_θ^{(j)}
grow toward the TOP of the tower (j → k), where the available curvature is largest (ε, not K̄^{k−j}ε), so the graded
reading of NAH-unif does not buy the factor L². This is recorded because it is the first thing a reader will try.**

---

## §N6 The composite recursion theorem — the deliverable (T3, part 2)

The per-level route is the wrong object. By TOWER-VAR (d) the level-k third derivative at the trivial background is a
**single** pullback by the chain-minimiser map ζ^c, not a k-fold product of per-level pullbacks. The per-level covariances
C^{(j)} never appear: the only linear object is the composite chain minimiser, so **the anti-circularity clause of the BFT
statement is satisfied by construction.**

### Theorem N1-15 (composite field-strength bound; the recursion is a convergent geometric series): PROVEN-HERE given (N-Q) and (N-loc)

*Statement.* Let d = 4 (general d displayed), L ≥ 3 odd, κ_j ∈ [κ_-, κ_+]. Assume (N-Q) with a bounded 𝔮_0 and (N-loc).
Then for every k ≥ 1 and every torus large enough at level k,
  **N3(D³E_k^br(1)) ≤ 𝔚·L^{(d−4)k} + 𝔖·L^{d−1}/(L − 1),**
with
  𝔚 := 3M_W𝔠_P²·[d(d−1)²Mc_m + 2d²C_fc_m] (the level-0 Wilson vertex, incurred ONCE),
  𝔖 := 3κ_+M_S𝔠_P²c_m·L²·[2d(d−1)κ̂M + 2d²κ̂C_R] (the soft vertices, summed over all levels),
and in particular, **at d = 4, N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖, uniformly in k.** Equivalently, the per-level ratio of the
soft contributions is
  **the level-j soft contribution is ≤ 𝔖·L^{(d−1)−n}, n := k − j, so A_soft = 1/L = 1/3 < 1 in every d ≥ 2**, and the
  level-0 Wilson contribution is ≤ 𝔚·L^{(d−4)k} = 𝔚 at d = 4 (marginal, incurred once).

*Proof.* By TOWER-VAR (d), D³E_k^br(1) = D³𝔉_k(1)[ζ^c·, ζ^c·, ζ^c·], and by Lemma N1-2 we may use any admissible
representative; take the one of Lemma N1-11. By Lemma N1-1, D³𝔉_k(1) is the sum of the level-0 Wilson vertex and the k
soft vertices, each in field-strength form. Evaluate N3 by putting X = δ_x (a level-k coordinate direction) and
|Y|_∞, |W|_∞ ≤ 1, and bound each of the three symmetrisation orderings.

**(1) Wilson vertex, δ_x in the differentiated slot.**
|Σ_p⟨(d_0ζ^c_0δ_x)_p, 𝔅_p(ζ^c_0Y, ζ^c_0W)⟩| ≤ |d_0ζ^c_0δ_x|_{ℓ¹}·M_W·|ζ^c_0Y|_∞|ζ^c_0W|_∞.
By (I3) and (I5), the kernel B_k ↦ f_0 obeys |K(X)| ≤ Me^{−m′|X|_1} in level-k units and d_0B_0 = L^{−2k}f_0, so by
Lemma N1-7 with τ = plaquettes, n_plaq(0) = (d(d−1)/2)L^{dk}:
  **|d_0ζ^c_0δ_x|_{ℓ¹} ≤ 2(d−1)·M·(d(d−1)/2)L^{dk}·c_m·L^{−2k} = d(d−1)²Mc_m·L^{(d−2)k}.**  …(exponent (d−2)k)
By Lemma N1-11, |ζ^c_0Y|_∞ ≤ 𝔠_PL^{−k}.  …(exponent −k each)
Total exponent (d−2)k − k − k = **(d−4)k**.

**(2) Wilson vertex, δ_x in an undifferentiated slot.**
|Σ_p⟨(d_0ζ^c_0Y)_p, 𝔅_p(ζ^c_0δ_x, ζ^c_0W)⟩| ≤ sup|d_0ζ^c_0Y|·M_W·|ζ^c_0δ_x|_{ℓ¹}·|ζ^c_0W|_∞.
sup|d_0ζ^c_0Y| ≤ C_fL^{−2k}sup|d_kY| ≤ 2dC_fL^{−2k} (exponent −2k); by (N-loc) and Lemma N1-7 with τ = links,
n_link(0) = dL^{dk}, |ζ^c_0δ_x|_{ℓ¹} ≤ dL^{dk}c_m·𝔠_PL^{−k} = dc_m𝔠_P·L^{(d−1)k} (exponent (d−1)k); |ζ^c_0W|_∞ ≤ 𝔠_PL^{−k}.
Total exponent (d−1)k − 2k − k = **(d−4)k**: the same. (Check n1-B, **PASS**, verifies that the three orderings agree.)

**(3) Soft vertex at level j, n := k − j ≥ 1, δ_x in the residual slot.**
|κ_jΣ_c⟨r_j(δ_x)(c), 𝔟^{(j)}_c(…)⟩| ≤ κ_+·|r_j(δ_x)|_{ℓ¹}·M_S·(the two potential legs).
By (I3)+(I4) the kernel B_k ↦ r_j obeys |K| ≤ κ̂Me^{−m′d}L^{−(d−1)(n−1)} (J-str (c) is a transport by Q_str^T, which is
local and does not degrade the exponential rate), so by Lemma N1-7 with τ = links, n_link(j) = dL^{dn}:
  **|r_j(δ_x)|_{ℓ¹} ≤ 2(d−1)·κ̂M·L^{−(d−1)(n−1)}·dL^{dn}·c_m = 2d(d−1)κ̂Mc_m·L^{\,n+(d−1)}.**  …(exponent n + d − 1)
The potential legs are at levels j and j + 1; Lemma N1-11 gives ≤ 𝔠_PL^{−n} and ≤ 𝔠_PL^{−(n−1)} = L𝔠_PL^{−n}, so their
product is ≤ L²𝔠_P²L^{−2n} in the worst assignment.
Total exponent (n + d − 1) − 2n = **(d − 1) − n.**

**(4) Soft vertex at level j, δ_x in an undifferentiated slot.**
≤ κ_+·sup|r_j(Y)|·M_S·|ζ^c_jδ_x|_{ℓ¹}·|ζ^c_{j+1}W|_∞ with sup|r_j(Y)| ≤ 2dκ̂C_RL^{−(d−1)(n−1)} (exponent −(d−1)(n−1)),
|ζ^c_jδ_x|_{ℓ¹} ≤ dc_m𝔠_PL^{(d−1)n} (exponent (d−1)n), |ζ^c_{j+1}W|_∞ ≤ L𝔠_PL^{−n} (exponent −n). Total exponent
−(d−1)(n−1) + (d−1)n − n = **(d − 1) − n**: the same. (Check n1-C, **PASS**.)

**(5) Summation.** The Wilson contributions give 𝔚L^{(d−4)k}, which at d = 4 is 𝔚, independent of k. The soft
contributions give Σ_{n=1}^{k}𝔖L^{(d−1)−n} ≤ 𝔖L^{d−1}Σ_{n≥1}L^{−n} = 𝔖L^{d−1}/(L − 1), at d = 4, L = 3 equal to
13.5·𝔖, independent of k. ∎

### Remark N6-1 (what the three exponents are, and the single reason this works)

The whole theorem is the statement that three exponents add up:

| ingredient | exponent | source | status |
|---|---|---|---|
| ℓ¹ mass of the level-0 curvature response to a level-k coordinate | (d − 2)k | (I3) N2-lin sup bound L^{−2k} × (I5) locality × volume L^{dk} | PROVEN |
| ℓ¹ mass of the level-j residual response to a level-k coordinate | n + (d − 1) | (I3)+(I4) sup bound L^{−(d−1)(n−1)} × (I5) × volume L^{dn} | PROVEN |
| ℓ¹ mass of the level-j potential response to a level-k coordinate | (d − 1)n | Lemma N1-11 sup bound L^{−n} × volume L^{dn} | CONDITIONAL on (N-Q), (N-loc) |
| sup of the level-j curvature response per unit level-k potential | −2n | Lemma N1-4 (θ_w = 2) | PROVEN-HERE |
| sup of the level-j potential response per unit level-k potential | −n | Lemma N1-11 (θ_A = 1) | CONDITIONAL on (N-Q) |

**The one reason it works:** going from level k to level j costs the volume L^{dn} and buys the decay L^{−2n}
(curvature), L^{−(d−1)n} (residual) and L^{−n} (potential). The cubic vertex uses one "decaying" factor and two
potentials: d − 2 − 1 − 1 = d − 4 = 0 for the Wilson vertex (**marginal**, and it occurs ONCE because there is only one
level-0 Wilson term) and d − (d − 1) − 1 − 1 = −1 for each soft vertex (**irrelevant by exactly one power of L**, hence
summable). The residual's extra power of decay — L^{−(d−1)} per level, from J-str (c), instead of the curvature's
L^{−2} — is what turns the marginal count into a convergent series. **In d = 4 that extra power is exactly one:
(d − 1) − 2 = 1. The result is true for every d ≥ 2 and has no margin to spare in the exponent.**

### Remark N6-2 (what A is, as the brief asks)

- Per-level route (§N5): **A_per = 𝔠·L^{d−4}·(L²K̄) ∈ [1.08, 1.38]·𝔠_vol𝔠_ax², vs 1266.87 now; A_per ≥ 1 is forced.**
- Composite route (§N6): there is no per-level recursion. The analogue of "C^{(i+1)} ≤ A·C^{(i)} + B" is
  **C^{(k)} ≤ 𝔚 + 𝔖·Σ_{n≥1}A_soft^{\,n−1}·L^{d−2}, A_soft = 1/L = 1/3 < 1.** The quantity that has to be < 1 is the
  LEVEL-RATIO of the soft vertex contributions, and it is 1/L, with the margin coming from
  (d − 1) − 2 = 1 power of L.
- **(H-C)'s C_♭ clause is therefore discharged at the trivial background, CONDITIONAL on (N-Q), (N-loc), and with the
  background extension (N-bg) still OPEN.** Pre-registered outcome: **O2**.

### Remark N6-3 (what replaces Z_col and Z_row, composite form)

Z_col = 156.08 (one level) is replaced by the composite ℓ¹ masses L^{(d−2)k} (curvature slot), L^{\,n+(d−1)} (residual
slot) and L^{(d−1)n} (potential slot) — each enormous, each exactly cancelled by the corresponding decay exponent.
Z_row = 2.849 is replaced by 𝔠_PL^{−n}. **Nothing in the composite route is a "per-level constant"**: there is no object
in it whose k-th power appears.

### [N1-corr 1] Correction to the (N-Q) bullet of §N4

The parenthesis "only POLYNOMIAL in j, which is still enough (see §N6, Remark N6-4)" in the (N-Q) bullet is **withdrawn as
stated**. The correct statement is the three-case reading:
- **𝔮_0 bounded in j** ⟹ Theorem N1-15 as stated, C_♭^{(k)} level-uniform. This is what (H-C) needs.
- **𝔮_0(j) polynomial in j** (e.g. 𝔮_0 ≤ 1 + cj, the pure-gauge-bookkeeping estimate) ⟹ 𝔠_P at level j grows like j, so
  the soft sum becomes Σ_n(k − n)²L^{(d−1)−n} ≲ k², i.e. **C_♭^{(k)} ≲ k²: polynomial, not uniform.** That would leave
  ε_unif = O(k^{−2}) — far better than the present (10³)^{−k}, and of the same character as CURV-F2″'s O(1/k), but
  still not (H-C).
- **only 𝔮_0(j) ≤ (p_L/L)^j** (the crude bound) ⟹ compounding by (p_L/L)² = (11/3)² ≈ 13.4 per level in the soft
  vertices: **still ≈ 95 times better per level than 1267, but depth-dependent.**
So (N-Q) with a bounded 𝔮_0 is load-bearing, and the honest status of Theorem N1-15 is CONDITIONAL on it. The
alternative that bypasses (N-Q) entirely is a **multi-scale axial gauge** (Balaban's regular-gauge construction): a single
fine gauge whose restriction to every level is axial-good on the corresponding block, which would give Lemma N1-11
directly at every level from Lemma N1-4 + Lemma N1-5 without any Q-transport. PROOF.md already records that object as
needed and OPEN under (CL-1) ("a composite LOC with multi-scale axial gauges: OPEN").

### Remark N6-4 (why COMP-F1 and the Π_ex tail do not occur here) — PROVEN-HERE as a statement about which maps are used

COMP-F1 (and SF S4-1's "(a5-G) is FALSE in ℓ^∞ → ℓ^∞", and Proposition LED-unif's warning that "the naive extension of the
f_0 map to all 2-forms contains the degree-0 projector Π_ex (|x|^{−4} tail)") is a statement about **extending** the
response map to sources that are not of divergence/exact form. Theorem N1-15 never performs that extension: every
response it uses is the response to **level-k data** — i.e. to d_kX for a potential X — which is exact, not merely
closed (Lemma N1-3's consequence). The three kernels used, B_k ↦ f_0, B_k ↦ r_{k−1} and the Q_str-transports, are exactly
the ones (I3)/(I5) bound uniformly in k. **This is why the divergence-form half of the §33 pair is not a decoration: it
is the whole reason the composite estimate is uniform, and it is also why pre-registered failure mode NORM-F2 (the
closed-input restriction not surviving the blocking map) does not occur in §N6.**

### Remark N6-5 (what is NOT proven here; pre-registered failure mode N-F4)

Theorem N1-15 bounds **D³E_k^br at the trivial background** — the cubic Taylor coefficient, the object c38 measures and
the object PROOF.md's CURV-F2 diagnosis is about. C_♭^{(k)} as its consumers use it is the **Lipschitz constant of
Hess E_k^br on the small-field class**, i.e. a bound on D³E_k^br(V) for every V in the class. The two are different
statements and the gap between them is named:

**(N-bg) [OPEN].** D³E_k^br(V) for V in the small-field class, with a constant uniform in k. Two routes:
- (i) *Perturbative.* TOWER-VAR (a) + Lemma N1-2 give the same identity at a general critical chain, with ζ^c(V) the
  chain-minimiser map at the background; the linear inputs (I3), (I4), (I5) must then be replaced by their
  background versions. That is precisely BFT-5 / the (G♯_0-field), (a5-G♯), (R♯_ω) family, plus a composite LOC. The
  Bianchi defect and the Z-representative return here (Lemma N1-3's consequence), so **NORM-F2 must be re-examined at
  this step and nowhere else.**
- (ii) *Analytic.* If E_k^br is holomorphic on a k-uniform polydisc in curvature-adapted coordinates (BFT-2), a Cauchy
  estimate converts the trivial-background Taylor bound of Theorem N1-15 — together with the same bound at every order —
  into the class statement. That is BFT-4's route, and Theorem N1-15 is then an INPUT to it at third order rather than a
  replacement (see §N8).

---

## §N7 The θ_w-dependence of A (T5)

Carry three exponents instead of one: **θ_w^c** (level-j own-units curvature ≤ CL^{−θ_w^c(k−j)}ε), **θ_w^r** (level-j
own-units residual ≤ CL^{−θ_w^r(k−j)}ε) and **θ_A** (level-j own-units potential, in the stated gauge,
≤ CL^{−θ_A(k−j)}ε). Redoing §N6's four exponent counts with these in place of (2, d − 1, 1) gives, exactly:

| contribution | exponent | condition for a k-uniform bound |
|---|---|---|
| level-0 Wilson vertex (occurs once) | (d − θ_w^c − 2θ_A)·k | **θ_w^c + 2θ_A ≥ d** |
| level-j soft vertex, n = k − j | (d − θ_w^r − 2θ_A)·n + θ_w^r | **θ_w^r + 2θ_A > d** |

so that
  **A(θ_w^r, θ_A) = L^{\,d − θ_w^r − 2θ_A},  and A < 1 ⟺ θ_w^r + 2θ_A > d.**

**θ_A is not free.** Lemma N1-5 (axial) gives θ_A ≥ θ_w^c − 1 at best, and Lemma N1-6 (holonomy spreading) caps it at 1,
so **θ_A = min(1, θ_w^c − 1)**. Substituting:
- Wilson condition: θ_w^c + 2min(1, θ_w^c − 1) ≥ d. For θ_w^c ≥ 2 it reads θ_w^c ≥ d − 2; for θ_w^c < 2 it reads
  3θ_w^c − 2 ≥ d, i.e. θ_w^c ≥ 2 at d = 4. **In both branches, at d = 4, θ_w^c ≥ 2 is required — and θ_w^c = 2 is the
  maximum available (K_p^♯ ≥ 1/L², REVIEW_S21 P). There is NO slack in the curvature exponent.** The Wilson term is
  therefore exactly marginal, which is harmless only because it occurs once.
- Soft condition at θ_A = 1: **θ_w^r > d − 2 = 2.** Delivered value θ_w^r = d − 1 = 3 (J-str (c), PROVEN), margin exactly
  one power of L.

**Consequence for the statement of BFT-1 (this is the load-bearing answer to T5).** With a SINGLE common exponent
θ_w^c = θ_w^r = θ_w, the condition θ_w + 2min(1, θ_w − 1) > 4 has **no solution in (0, 2]**: A ≥ 1 for every admissible
θ_w. **The contraction does not come from θ_w at all; it comes from the residual exponent exceeding the curvature
exponent by d − 3 = 1.** So:
- BFT-1 **as stated** ("there exist … θ_w ∈ (0, 2]", one exponent for curvature and soft fluctuation together) is
  **insufficient for this route**, for the same reason REVIEW_SQ_S2 recorded (its item (2): "a residual exponent > 2").
- What this route needs is BFT-1 **stated as the pair** (θ_w^c = 2, θ_w^r = d − 1 = 3). Both are PROVEN for the linear
  chain at the trivial background (Lemma N1-4 here, and J-str (c) imported), so the requirement is met exactly where
  Theorem N1-15 uses it.
- Reporting the interval as the lead asked: **A < 1 holds on {θ_w^r > 2} ∩ {θ_w^c ≥ 2}, and nowhere else**; it does NOT
  hold on any interval (0, θ̄] of a single common θ_w. If a future BFT-1 can only be had with one exponent, this route
  does not close.

---

## §N8 Consumer compatibility, clause by clause (T4)

ACCEPTED = a bound in N^F is directly usable, with the stated conversion. The conversion never costs L^{d−1} or L^{d−2}
(pre-registered failure mode N-F1 does not occur): on the ℓ¹ leg it is the factor |d_lδ_b|_{ℓ¹} = 2(d − 1) = 6, and on
the ℓ^∞ legs it is free in the needed direction (an axial/inf-over-gauges norm is ≤ the sup norm in any given gauge).

| consumer | clause | verdict | conversion / what is missing |
|---|---|---|---|
| **Lemma BR1** (PROOF l.6122) | ‖R_2‖_∞ ≤ ½C_♭r², R_2 the quadratic Taylor remainder of ∇f_V | **ACCEPTED**, cost 2(d−1) = 6 | Put δ_b in the ℓ¹ slot and A* twice in the ℓ^∞ slots; |A*|_{ax} ≤ |A*|_∞. Needs **(N-bg)**: R_2 is at the branch, not at 1 |
| **Lemma CURV1** step (6) | \|(dC_0R_2)_p\| ≤ 2𝔠_∞C_♭r² | **ACCEPTED**, same C_♭ | as above; needs (N-bg) |
| **Theorem NAH1 (b)** / δ_Sch (PROOF l.5842-5845) | the C_♭α′ and C_♭α′e^{mr_1} terms (Hessian deviation at a background) | **ACCEPTED**, cost 6 | α′ IS the AX-gauge field size, i.e. the ℓ^∞ leg's own norm; needs (N-bg) |
| **Proposition NAH-unif**, (H-C) | "C_♭^{(i)} bounded uniformly in i" | **ACCEPTED at the trivial background** (Theorem N1-15) | CONDITIONAL on (N-Q), (N-loc); (N-bg) for the class |
| **Proposition NAH-unif**, (H-C) | 𝔠_∞^{(i)}, A_in^{(i)}, A_out^{(i)}, c_K^{(i)}, 1/m_1^{(i)}, Z-tails level-uniform | **NOT IN SCOPE — untouched** | these are separate clauses of (H-C); nothing here bears on them |
| **Proposition NAH-unif′**, (H-C⁺) | level-uniform C_θ^{(i)}, C_θ^{ρ,(i)} (failure mode CURV-F2′) | **NOT REPAIRED by this file** | CURV-F2′'s mechanism is the per-level absolute step \|dCe\|_∞ ≤ 4𝔠_∞\|e\|_∞ on the FIRST-order error e_{g,i}, not E3's third derivative. See Remark N8-2 |
| **Proposition NAH-unif′** | the θ-cascade (failure mode CURV-F2″) | **NOT REPAIRED by this file** | same mechanism, acting on θ; it is a per-level-route artefact and is absent from §N6's composite estimate, but §N6 does not run NAH-unif′ |
| **(H-G)**, level-uniform form | g_i = H_iJa + e_{g,i} with level-uniform near/far constants | **NOT DELIVERED** | the Remark route (PROOF l.6393-6396) needs C_♭^{(i)} (which §N6 supplies at the trivial background) PLUS the localisation of ∇E_i^br, which is not shown. §N6 does not touch it |
| **BFT-4** | E_k^br = S_W + R_k, ‖R_k‖_𝒜 ≤ C_0; "consequently, by Cauchy, C_♭^{(k)}, (H-G), C_θ, C_θ^ρ, ε_θ are level-uniform" | **ALTERNATIVE for the C_♭^{(k)} clause at order 3; TOOL inside BFT-4 otherwise** | see Remark N8-1 — this is the "say it loudly" item |
| **BFT-1** | scale-weighted regularity | **SUPPLIED, not consumed**, for the linear chain on the torus: Lemma N1-4 (θ_w^c = 2) and Lemma N1-11 (θ_A = 1, conditional on (N-Q)) | must be stated as the pair (θ_w^c, θ_w^r) = (2, d−1): §N7 |
| **BFT-0 anti-circularity** | no per-level C^{(j)} as Newton inverses | **SATISFIED by construction** | §N6 uses only the composite chain minimiser ζ^c; the per-level §N5 is presented only to prove the no-go and is not used in §N6 |
| **SF** (BG-unif), ε_1 | ε_BG, C_BG independent of k | **ACCEPTED as a partial input** | Corollary SF-thr-k's ε_1 is already k-independent GIVEN (BG-unif); §N6 supplies one clause of that hypothesis and does NOT change ε_1's value (§N9) |
| **SQ** (REG-min) | cone-local minimisers in Σ_dec, θ_w = 2 | **independent agreement** | Lemma N1-4 reproduces REG-lin (d)'s constant C_0 + 4κ̂L²/(L²−1) on the torus by a different route |

### Remark N8-1 (alternative to BFT-4, or tool inside it?) — the honest answer

**For the single clause "C_♭^{(k)} level-uniform", this route is an ALTERNATIVE to BFT-4, and it avoids (CovLift) and
(Mult-Y) entirely.** BFT-4's stated route is: establish a gauge-invariant local-polymer representation of R_k with
‖R_k‖_𝒜 ≤ C_0 on a k-uniform polydisc, then get C_♭^{(k)} by a Cauchy estimate. Its recorded open inputs for k ≥ 2 are
(CovLift) [OPEN, nonabelian], (Mult-Y) [GAP-1 family], (Pair-loc) [ARGUED], (I-id)_Z [ARGUED], plus (W-comm) [GAP 1] and
(W-loc). **Theorem N1-15 obtains the third-order statement with none of those**: its inputs are TOWER-VAR (d) (algebraic),
Lemma N1-1 (a BCH identity), the frozen LINEAR_PACKAGE estimates N2-lin / J-str / N2-exp, Lemma AX, and the two named
inputs (N-Q), (N-loc). That is a large reduction in the dependency set for this clause, and it should be recorded as such.

**But it is NOT a replacement for BFT-4.** (a) It is third order only; BFT-4's analytic class is all orders, and the
consumers of ε_θ, C_θ and (H-G)'s level-uniform form need more than D³. (b) It is at the trivial background; the class
statement needs (N-bg), and route (ii) of (N-bg) is BFT-4's own Cauchy argument — in which case Theorem N1-15 becomes the
**n = 3 instance** of what BFT-4 must prove at every n, now in the field-strength norm. (c) BFT-4 also delivers the
marginal/irrelevant structure (E_k^br = S_W + R_k), which §N6 does not.
**Net reading for the lead:** the (H-C)/C_♭ clause no longer has to wait for (CovLift)/(Mult-Y); it waits for (N-Q),
(N-loc) and (N-bg). The first is a question about a definition, the second is the multi-scale axial gauge already named
under (CL-1), the third is BFT-5's family.

### Remark N8-2 (spin-off: the same cure applies to CURV-F2′ and CURV-F2″) — ARGUED, not proven here

CURV-F2′'s and CURV-F2″'s per-level factor is 4κ_i𝔠_∞^{(i+1)} ≈ 4·315 ≈ 1.26·10³ per level, from the step
|(dC_1e_{g,1})_p| ≤ 4𝔠_∞^{(1)}|e_{g,1}|_∞ (PROOF l.6347), i.e. an absolute sup bound for dC applied to a generic
first-order error field. But e_{g,i} is the localisation error of the GRADIENT of a gauge-invariant local functional, and
the gradient of any plaquette-local functional is of **divergence form**: ∇Σ_pW(F_p) = d^*(W′(F)). On such inputs the
operator is dC^0d^*, for which **0 ≤ dC^0d^* ≤ 1 in ℓ² is PROVEN** (Lemma CURV-lin (ii)) and whose sup/closed-input row
norm is the same LP object as K_p (≈ 1 ± K̄). So the factor 4𝔠_∞ ≈ 1.26·10³ should be replaceable by a constant of order
1 — the same ≈ 10³ gain, by the same mechanism, on the first-order error instead of the third derivative.
**This is ARGUED, not proven: it requires (a) exhibiting e_{g,i} in divergence form with a controlled 2-form
representative (its ℓ^∞ size, not merely its existence), and (b) a sup-norm (not ℓ²) bound for dC^0d^* on
divergence-form inputs, which has exactly the status of (H-K).** If it holds, all three failure modes CURV-F2, CURV-F2′,
CURV-F2″ are **one and the same artefact**: an absolute-value sup bound applied where the object is in divergence or
curvature form and the operator is a conjugate of dCd^*. That unification is the single most useful follow-on this file
suggests; it is item 3 of the FOR OTHER FILES list.

---

## §N9 Propagation (T6), and a correction to the brief's premise

A < 1 is obtained in the composite route (A_soft = 1/L = 1/3), CONDITIONAL on (N-Q), (N-loc), so T6 is answered — but
**the honest answer corrects the premise of the task.**

**(1) What the per-level factor 1267 actually costs, and what it does not.** Corollary SF-thr-k (SF.md l.74) reads:
"Under (BG-unif) … the choice ε_1 := min{ε^thr_N, min(ε_BG, ε_*/C_BG)/(1.011√N)} **is independent of k, K, T**". So
ε_1 = 1.27·10⁻³⁹ (SF.md l.2837) and, downstream, HW's g²_CRC ≈ 4.9·10⁻⁹⁷/c_+ are **already k-independent given
(BG-unif)**; their VALUE is set by the certified level-0 constants (𝔠_∞^♯ = 315.19, λ_min ≥ 3.17·10⁻³,
ε_* = 2.476·10⁻¹³/C_Δ, r_♭ = 1/220) and by SF's own chain, not by any per-level compounding. **What Z_colZ_row² ≈ 1267
per level threatens is not the value of ε_1 but the EXISTENCE of a k-independent ε_BG at all** — because in the per-level
route ε_unif ≤ inf_i θ/C_θ^{(i)} ≈ θ·(1267)^{−k} → 0, which makes (BG-unif) false as stated and therefore makes
Corollary SF-thr-k's hypothesis unavailable.
**Therefore: this result does not improve ε_1 or g_K². It restores the legitimacy of their k-independence.** The brief's
sentence "that single factor is the origin of every astronomical constant in the project" is, on the evidence in SF.md
and HW.md, **only partly right**: it is the origin of the depth-dependence, not of the magnitudes.

**(2) What the smallness condition becomes.** With C_♭ level-uniform (and the other (H-C) clauses, which are out of
scope), CURV1's C_θ = 288𝔠_∞³C_♭ + 792𝔠_∞ℓ_θ + 24𝔠_∞c_π + 288A_in coth⁴(m_1/2)ℓ_θ + 53(48𝔠_∞ + 1)² + 1296𝔠_∞ℓ_θ +
N_0(|Z|)(162ℓ_θ + 2880) becomes level-independent, and the condition is
  **η ≤ θ/C_θ with C_θ level-independent**, i.e. **η ≲ 10^{−42}θ at the session-23 constants**, because C_θ is dominated
by the 288A_in coth⁴(m_1/2)ℓ_θ term (coth⁴(m_1/2) ≈ 5.9·10²⁰ at the session-23 m_1, or ≈ 2.9·10⁴² at N5-w0's m_1;
SF7-edit 5), with 288𝔠_∞³C_♭ ≈ 9.0·10⁹·C_♭ and 53(48𝔠_∞ + 1)² ≈ 1.2·10¹⁰ far below it.
**So making C_♭ level-uniform changes the NUMBER not at all** (C_♭'s term is ≈ 10³² times below the binding one); it
changes the condition from "η ≲ 10^{−42}·(10³)^{−k}θ" to "η ≲ 10^{−42}θ". The binding constants are now the covariance
decay rate m_1 (through coth⁴(m_1/2)) and A_in, i.e. exactly SF's and PROOF's level-0 certification problem.

**(3) HW's g_K² ceiling.** **Unchanged: g_K² < g²_CRC ≈ 4.9·10⁻⁹⁷/c_+, still below the recorded (RLF-δ) ceiling
10⁻⁹⁴, and g_0 still has to be lowered** (HANDOFF's "Update after the handoff list was written"). Nothing in this file
touches a_ret, b_n, c_att, n_H or C_ℓ. Any claim that this result relieves the HW ceiling would be false, and is not made.
What this result does for HW is make the hypothesis under which HW's constants are depth-free available. The recomputation
HW needs is the one HANDOFF already lists (lower g_0; recheck the SF thresholds), not a new one.

---

## §N10 Tally, and the record of check n1

### Tally

**PROVEN-HERE (complete proofs written out above, from stated hypotheses)**
1. Lemma N1-1 — field-strength representation of 𝔉_k's cubic vertex (exactly one coboundary or one residual per term),
   with M_W ≤ 6 and M_S = M_S(L, d, N) < ∞.
2. Lemma N1-2 — E3 and TOWER-VAR (d) hold for every admissible gauge reparametrisation of the critical family; the
   admissible class is "trivial at the coarse centres".
3. Lemma N1-4 — intermediate-level curvature decay on the torus, sup|d_jB_j| ≤ (C_f + 4κ̂C_RL²/(L²−1))L^{−2(k−j)}θ
   (θ_w^c = 2), uniformly in k, j, T. (Independently agrees with SQ's Theorem REG-lin (d) on the cone box.)
4. Lemma N1-5 — lattice axial gauge with constant (d − 1)R (abelian/linearised).
5. Lemma N1-6 — nested multilinear interpolants realise a coarse pure gauge at level j with own-units size
   L^{−(k−j)}|d_kλ|_∞.
6. Lemma N1-7 — ℓ¹ mass from a sup bound plus exponential locality, with c_m = coth(m′/2)^d.
7. Proposition N1-8 — the mass-balance identity ρ_col = [n_τ(i)/n_plaq(i+1)]·ρ_row; Corollary N1-9 (the column bound
   given decay).
8. Theorem N1-13 (i) — weight-invariance: the per-level factor times the initial-condition weight mismatch is
   independent of (θ_w, θ_A). (Checked symbolically, n1-D PASS.) **This is the proof that pre-registered failure mode
   N-F2 occurs for every per-level route, and it is what makes the no-go a no-go rather than a failure of imagination.**
9. Theorem N1-12 — the per-level field-strength recursion M_{i+1} ≤ A_per M_i + B_per with
   A_per = 𝔎_col(Z^{sm})², given Proposition N1-10 and Corollary N1-9.
10. Remark N6-4 — COMP-F1 / Π_ex does not occur in §N6, because every response used is the response to level-k data
    (exact, not merely closed).
11. §N7's exponent table and the identity A = L^{d − θ_w^r − 2θ_A} with θ_A = min(1, θ_w^c − 1); and the consequence
    that a single common θ_w admits no solution of A < 1 in (0, 2].

**CONDITIONAL (proven given a named open input)**
12. **Lemma N1-11** (composite potential bound, θ_A = 1) ⇐ **(N-Q)** (‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j with 𝔮_0 bounded).
13. **Theorem N1-15** (the deliverable: N3(D³E_k^br(1)) ≤ 𝔚 + L^{d−1}/(L−1)·𝔖 uniformly in k, with the soft level-ratio
    A = 1/L = 1/3 < 1) ⇐ **(N-Q)** and **(N-loc)**.
14. The discharge of (H-C)'s **C_♭ clause** ⇐ (N-Q), (N-loc) at the trivial background; ⇐ additionally **(N-bg)** for the
    Lipschitz statement on the small-field class that BR1 and δ_Sch actually consume.

**ARGUED (convincing, with an identified hole)**
15. **(N-Q)** itself: reduced to pure-gauge bookkeeping via J-str's Q = Q_str − d∘h, immediate with 𝔮_0 = 1 if Setting
    SC's Q is the straight average. Hole: h applied to a pure gauge.
16. **(N-loc)**: the gauge-invariant half is PROVEN (N2-exp); the gauge-variant representative's exponential locality
    needs a shell-wise axial construction. Tradeable for an explicit near/far split with a factor R_eff^d.
17. **Theorem N1-13 (ii)** (A_per ≥ 1 is forced): the exponent count is a proof skeleton, but K_p^♯ ≥ 1/L² on Z⁴ and the
    identification of the marginal eigenvalue with c_3 → 1 are measured (REVIEW_S21 P, c38 C), not certified.
18. **Remark N8-2**: the same divergence-form cure for CURV-F2′/CURV-F2″'s 4𝔠_∞ step.
19. Proposition N1-10 (one-level spread representative): the value L^{−1} is the smooth-sector value; 𝔠_ax is not
    evaluated. Flagged under pre-registered failure mode N-F3.

**OPEN**
20. **(N-bg)**: D³E_k^br(V) on the small-field class, k-uniformly. This is where the Bianchi defect, the Z-representative
    and its tails return (so this is where pre-registered failure mode NORM-F2 must be re-examined), and it is BFT-5's /
    (G♯_0-field)'s family.
21. The level-uniform form of **(H-G)**: untouched.
22. The other clauses of **(H-C)**: 𝔠_∞^{(i)}, A_in^{(i)}, A_out^{(i)}, c_K^{(i)}, 1/m_1^{(i)}, Z-tails: untouched.
23. **CURV-F2′ / CURV-F2″** in the per-level route: not repaired (Remark N8-2 is the proposed route, ARGUED).

**Counted here: nothing.** This file is not a ledger. No item above is to be added to PROOF.md's tally by this worker.

### Check n1 (exponent bookkeeping) — record

Criteria written first: `checks/n1_criteria.md`, 12:41 UTC, before the script existed. Script: `checks/n1_exponents.py`
(exact integer / `Fraction` arithmetic, plain python, single process, no BLAS, **no numeric lock taken**, permitted by the
brief's rule 6 for exact rational arithmetic). Timing record: `checks/n1_time.txt`; output `checks/n1_out.txt`.

- **n1-A PASS.** The marginal exponent d − 4 is −1, 0, +1 at d = 3, 4, 5: the norm reproduces the whole power counting.
- **n1-B PASS.** All three symmetrisation orderings of the Wilson term give the same exponent (d − 4)k.
- **n1-C PASS** (at d = 4). Both orderings of the soft term give (d − 5)n + 3 at d = 4, the per-level ratio is
  L^{d−5} = 1/3 < 1, and the geometric sum is L³/(L − 1) = 27/2.
  **Disclosed labelling defect (not a failed verdict):** both the criterion and the script write the residual decay
  exponent as the hard-coded 3 and therefore print the d-general formula as (d − 5)n + 3. The correct d-general exponent
  is **(d − 1) − n** (the residual decays by L^{−(d−1)} per level, not L^{−3}); the two agree at d = 4, which is the only
  case the pre-registered verdict covers, so the PASS stands and §N6/§N7 use (d − 1) − n.
- **n1-D PASS.** At all six pairs (θ_w, θ_A) ∈ {0, 1, 2} × {0, 1} the invariant log_L is d − 4: **no weight choice
  produces a contraction**. This is the computational half of Theorem N1-13 (i).
- **n1-E informational.** L²K̄ = 0.99999, 1.0242, 1.0386, 1.0818, 1.1124 at K̄ = 1/9, 0.1138, 0.1154, 0.1202, 0.1236;
  L^dK̄ = 9.00 … 10.01; Z_colZ_row² = 1266.87; (1 + Z_col)(1 + Z_row)² = 2327.11; **gain 920–1171** at a = 3 resp. a = 1;
  (2/3)K_ρ^♯ = 1.383, 1.479, 1.743; **Z_row/(1/L) = 8.55** and **Z_col/(L^dK̄) = 16.03**; θ_w^c = log_L(1/K̄) = 2.0000,
  1.9284, 1.9030 at K̄ = 1/9, 0.1202, 0.1236.
- No check was run after seeing a result and then re-labelled; no post-hoc probe was added.

---

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file. Each item names the file, the precise change, and why.

**1. LINEAR_PACKAGE.md / Setting SC owner — the one question that decides Theorem N1-15's status (highest value, cheapest).**
*Is Setting SC's averaging operator Q the STRAIGHT block average Q_str, or the full S4′ average?* If it is Q_str, then
‖Q^j‖_{∞→∞} = L^j exactly, **(N-Q) holds with 𝔮_0 = 1, and Lemma N1-11 and Theorem N1-15 become PROVEN modulo (N-loc)
alone.** The evidence is mixed in the files: Lemma J-str writes "Q^T = Q_str^T − h^Td^*" (so Q ≠ Q_str in Setting SC),
while SQ's Lemma SHIFT writes "Q^m is the straight average over L^m-blocks" (SQ.md l.709) and uses
‖Q^T‖_{∞→∞} = L^{−(d−1)}. If Q is the full S4′ average, the needed statement is
**‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j with 𝔮_0 bounded in j**, equivalently that the funnel (axial) legs do not accumulate in the
composite transport. The crude bound p_L^j is insufficient and costs (p_L/L)² ≈ 13.4 per level ([N1-corr 1]).

**2. PROOF.md — correct the CURV-F2 diagnosis and record the per-level no-go.** The sentence at l.6212-6215 reads
"Z_col ≥ the L^{d−1} = 27 crossing links of one coarse link times the spread". The correct count in the field-strength
norm is **L^d·K̄ ≈ 9.7 (not L^{d−1} times a spread), and the crossing-link count does not appear at all once the leg is
measured through d_1X** (Proposition N1-8, §N4 (a)). And record the no-go: **in any scale-covariant norm family the
per-level factor is 𝔠·L^{d−4}·(L²K̄) ≥ 1, forced by the marginality of the d = 4 cubic vertex and by K_p^♯ ≥ 1/L²; no
norm closes CURV-F2 per level** (Theorem N1-13; the weight-invariance half is proven, check n1-D PASS). The useful
numbers for the ledger: **A_per ∈ [1.08, 1.38]·𝔠 against 1266.87, a gain of ≈ 10³ per level.**

**3. PROOF.md — the proposed unification of CURV-F2, CURV-F2′ and CURV-F2″ (Remark N8-2, ARGUED).** All three are the
same artefact: an absolute sup bound applied where the object is in divergence or curvature form and the operator is a
conjugate of dC^0d^*, for which 0 ≤ dC^0d^* ≤ 1 is PROVEN (Lemma CURV-lin (ii)). Concretely, the step
|(dC_1e_{g,1})_p| ≤ 4𝔠_∞^{(1)}|e_{g,1}|_∞ (l.6347) should be replaced by a bound on dC^0d^* applied to a divergence-form
representative of e_{g,i}: 4𝔠_∞ ≈ 1.26·10³ → O(1). This needs (a) e_{g,i} exhibited in divergence form with a
controlled 2-form representative and (b) a closed-input sup bound for dC^0d^*, of the same status as (H-K). If it works,
CURV-F2′ and CURV-F2″ are repaired by the same mechanism as CURV-F2.

**4. REVIEW_S22 / the BFT statement — BFT-1 must be stated as a PAIR of exponents.** "there exist … θ_w ∈ (0, 2]" with
one exponent for curvature and soft fluctuation together is **insufficient for this route**: with a single common θ_w,
A ≥ 1 for every θ_w ∈ (0, 2] (§N7). The required form is **θ_w^c = 2 for the curvature and θ_w^r = d − 1 = 3 for the
residual**; the contraction comes entirely from θ_w^r − θ_w^c = d − 3 = 1. This coincides with REVIEW_SQ_S2's recorded
item (2) ("a residual exponent > 2"), so the two requests should be merged. Note also, for the lead's latest routing:
even though SQ no longer gates on θ_w, **this route still needs the maximal θ_w^c = 2** — it does not become easier at
small θ_w, which is the opposite of the usual direction and is worth recording explicitly.

**5. SQ.md / REVIEW_SQ — independent agreement, and a small request.** Lemma N1-4 here derives
sup|d_jB_j| ≤ (C_f + 4κ̂C_RL²/(L²−1))L^{−2(k−j)}θ **on the torus**, from LINEAR_PACKAGE's N2-lin, J-str and the square
identity — reproducing SQ's Theorem REG-lin (d) constant C_0 + 4κ̂L²/(L²−1) exactly, by a different route on a different
geometry. Two independent derivations of the same constant is worth recording in both files. Request: confirm that SQ's
θ_w = 2 statement is for minimisers of the chain energy with level-k data (so that it transfers to the torus setting
Theorem N1-15 uses), or state the geometric restriction.

**6. HW.md / SF.md — what does NOT change (please record the negative).** g²_CRC ≈ 4.9·10⁻⁹⁷/c_+ and
ε_1 = 1.27·10⁻³⁹ are **unchanged** by this result, and g_0 still has to be lowered. Corollary SF-thr-k already makes ε_1
k-independent *given* (BG-unif); what this file supplies is one clause of that hypothesis. The binding term in C_θ is
288A_in coth⁴(m_1/2)ℓ_θ (≈ 10²⁰–10⁴²), with 288𝔠_∞³C_♭ ≈ 9.0·10⁹C_♭ far below it, so a level-uniform C_♭ does not move
the number (§N9). If anyone has recorded, or is tempted to record, that closing CURV-F2 relieves the HW ceiling, that is
false.

**7. PROOF.md — (CL-1)'s open half is now the single bottleneck for this route.** The "composite LOC with multi-scale
axial gauges: OPEN" named under (CL-1) is exactly the object that would give Lemma N1-11 at every level directly from
Lemma N1-4 + Lemma N1-5, bypassing (N-Q), and would also give (N-loc). It should be promoted from a remark to a named
target: **a single fine gauge on a level-k box whose restriction to every level j is axial-good on the level-(j+1)
blocks, with constants depending only on (N, L, d).** Balaban's regular-gauge construction is the literature comparator
(to be re-verified on our structures, never taken as given).

**8. Suggested smallest measurable piece, for whoever owns c39.** Not needed for this file, but it would settle item 1
and costs almost nothing: compute **‖Q^j‖_{∞→∞} = max_c Σ_b |Q^j(c, b)| for j = 1, 2, 3** at L = 3, d = 4 for Setting
SC's actual Q, and compare with L^j = 3, 9, 27 and with p_L^j = 11, 121, 1331. Exact rational arithmetic, no numeric
lock, seconds. **If the answer is ≈ L^j, Theorem N1-15 is PROVEN modulo (N-loc) and (H-C)'s C_♭ clause is closed at the
trivial background.** A second cheap piece: the column masses max_P Σ_p |𝒦_Z(p, P)| and max_P Σ_c |𝒦_ρ(c, P)| on the
tori c37 already builds, to replace §N4's average-based estimate 9.7 + 1.5 by a measured max.

---
