# C9 findings: do field-dependent structure functions evade the arc lemma?

Provenance: a worker of the same model family. **Unchecked.** Saved by the supervisor from the hand-back (the worker's file write was blocked). The runner is new code and imports nothing from the lane runner. This is pure lattice mathematics with supplied vector fields: no dynamics is adopted and no physical identification is made.

| Runner | Method | Result |
|---|---|---|
| `c9_structure_functions_runner.py` | exact (sympy QQ, QQ(λ), QQ[w]/Φ_L, Gröbner); one `F_` line (mpmath, 40 digits) | PASS=79 FAIL=0, 75 s |

The first run (`c9_run1_with_L3_expectation_bug.log`) had one FAIL, R4 at L = 3. The test wrongly expected a non-zero Jacobiator; at L = 3 the zeroth-order bracket is sl2, the lemma's own exception. The expectation was fixed, not the computation.

**Answer.** Yes, but only through background dependence (or discontinuity at the vacuum). Enlarged generator sets also evade the lemma. Once structure functions are allowed, "closes within its span" is nearly vacuous without extra conditions.

## Setup

The lane note's definitions are used:
- G is linear, injective and translation-covariant.
- X_n = G[e^{2πinx/L}] and D = X_0.
- Λ_n = c(0,n).
- (S) means Λ_1 ≠ 0 and [X_1, X_{−1}] ≠ 0.
- An arc is a run of consecutive momenta in {2, …, L−2} carrying one sl2-irreducible, with Λ_n/Λ_1 = n − (arc centre).

(P2) is replaced by the following:
- **(SF) closure with structure functions.** V_ξ = G[ξ] are vector fields on a field manifold M (one L-periodic sector). On a T-invariant open set U, [V_a, V_b] = Σ_e C_ab^e(Φ) V_e. The Poisson form X_a = ⟨p, V_a⟩ has the same C.
- **Covariance.** T_*V_n = ω^n V_n. C can be T-averaged to a covariant solution, C_ab^e ∘ T^{−1} = ω^{a+b−e} C_ab^e.
- **Background.** Φ̄ with TΦ̄ = Φ̄. Zeroth-order data are c̄(a,b) := C_ab^{a+b}(Φ̄) and Λ_n := c̄(0,n); equivalently [V_0, V_n](Φ̄) = Λ_n V_n(Φ̄).
- **(S′)** means (S) together with [X_1, X_{−1}] = cD, c ≠ 0. It equals (S) when there is one generator per momentum.

## Results

### Stage 1: linearisation about a uniform background

- **L1 (grading) [exact].** C_ab^e(Φ̄) = 0 unless e ≡ a+b. So c̄ is field-independent, antisymmetric and graded, the same shape as the lemma's data. *Proof:* evaluate the covariance relation at the fixed point.
- **L2 (Jacobiator = background-velocity term) [exact; R4, M2, M2b, M4, X1].** For each e = a+b+c with V_e(Φ̄) ≠ 0:
  `Jac(c̄)_abc = Σ_cyc ⟨dC_ab^{a+b+c}(Φ̄), V_c(Φ̄)⟩`.
  - So c̄ fails Jacobi only through first-order structure functions contracted with the background velocities.
  - When c̄ satisfies Jacobi and (S) holds, the arc lemma applies to c̄ verbatim.
- **L3 (common zero ⇒ arc lemma on the linearisation) [exact; gap form certified by H2].**
  - If V_n(Φ̄) = 0 for all n and C is continuous at Φ̄, then A_n := DV_n(Φ̄) satisfy [A_a, A_b] = c̄(a,b) A_{a+b}. This is a graded Lie algebra on the support S = {n : A_n ≠ 0}.
  - **Gap form of the arc lemma.** Its proof does not need every momentum to be present: arcs are runs of consecutive momenta inside S. If 0, ±1 ∈ S and (S) holds, then Λ_2/Λ_1 ≤ 0 whenever 2 ∈ S.
  - H2 checks this by Gröbner bases for supports Z_6∖{3}, Z_7∖{3}, Z_7∖{4} and Z_8∖{4}.
  - This is the standard isotropy-algebra fact for Lie algebroids.
- **L4 (homogeneity) [exact; H1].**
  - If the V_n are linear vector fields and C is continuous at 0, then [V_a, V_b] = C(0)^e V_e identically. The same holds for quadratic Poisson generators.
  - **So for the note's linear matter relabellings about the vacuum, continuous structure functions add nothing**, and B19 and the arc lemma stand.
  - Structure functions that help must be homogeneous of degree 0, hence discontinuous at the vacuum. H1 shows this for δφ = ξΔφ at L = 3–6.
- **Degeneracy answer [exact].**
  - *At a common zero*, "closes within its span" survives. The only loopholes are:
    - (S) degenerating at linear order;
    - 2 ∉ S;
    - C discontinuous at Φ̄.
  - *At a background the relabellings move* (some V_c(Φ̄) ≠ 0):
    - the zeroth-order truncation is abelian;
    - c̄ may satisfy (S) but closes only up to first-order field-dependent terms (L2).
  - This moved-background case is the loophole, and L5 shows it is unrestricted.

### Stage 2: first order and an explicit 1D model

- **L5 (realisation) [exact; X1].**
  - For any graded antisymmetric c̄, the T-covariant frame `V_a = ∂_a − ½ Σ_k c̄(a,k) u_k ∂_{a+k}` on C^L closes with rational structure functions, with C(0) = c̄. This is checked for random rational c̄ with Λ_1 = 1 and Λ_2 = 2 at L = 4–6.
  - **Λ_n is zeroth-order by definition.** First-order structure functions decide whether a value is consistent; at a moved background any value can be.
- **P6 (ruler-background scalar relabelling in the note's 1D setting) [exact; R1–R6, M1–M3, M5; F_R7].**
  - The model is δu_x = ξ_x(1 + (Δu)_x), i.e. δφ = ξΔφ with φ = x + u, where Δ is translation-invariant with Δ1 = 0 and has symbol λ_k.
  - It closes exactly on {g_x ≠ 0}, g = 1 + Δu, with C_ij^j = Δ_ji g_i/g_j and C_ij^i = −Δ_ij g_j/g_i. These are rational, field-dependent and have the range of Δ.
  - *Zeroth order:* c̄(a,b) = λ_a − λ_b, so Λ_n = −λ_n.
  - *First order:* ∂_c C_ab^{a+b+c}(0) = λ_c(λ_{a+c} − λ_{b+c} − λ_a + λ_b), which equals Jac(c̄).
  - **Central difference:**
    - (S) holds, and **Λ_2/Λ_1 = 2cos(2π/L)**, exact in QQ[w]/Φ_L for L = 3–12.
    - This is positive for every L ≥ 5 (checked L = 5–40) and tends to 2, against the arc lemma's ≤ 0 for constants. At L = 4 it is 0.
    - Jac(c̄) ≠ 0 for L = 4–7 and Jac(c̄) = 0 at L = 3.
  - **SLAC difference (L = 5, 7):** Λ_n = n̄Λ_1 for every n, with (S), and exact closure with structure functions. Jac(c̄) ≠ 0, consistent with the note's B3 certificate that this spectrum is impossible with constants.
  - **Forward difference:** Λ_1 + Λ_{−1} ≠ 0 (L = 3–9).
  - The model also evades Theorem A, which assumes constants.
  - Remark (series argument, not certified): the first-order terms are O(k³) against O(k) for c̄.
- **P7 (Poisson form) [exact; P1].** The cotangent lift X_a = ⟨p, V_a⟩ gives {X_a, X_b} = −C_ab^e(u) X_e.
  - The lowest-order generators p_a Poisson-commute, and c̄ first appears one order up.
  - Whether B14's G_m, with its density weights, reduces to this form was not checked.
- **Why closure is vacuous here [exact].** L generators on an L-dimensional configuration space form a frame, so any bracket closes with structure functions. Extra conditions are needed for closure to constrain anything:
  - a common-zero background (L3);
  - continuity of C at the vacuum for linear relabellings (L4);
  - restrictions on the form of C.

### Stage 3: enlarged generator sets (brief)

Setting: g is finite-dimensional and Z_L-graded with any dim g_n; D ∈ g_0; X_{±1} are ad_D-eigenvectors.

- **L8 [exact; E1–E3].**
  - **(i) survives.** Under (S′), the spectrum of ad_D lies in (Λ_1/2)Z.
  - **Necessity.** Under (S′), an ad_D-eigenvector in g_n with eigenvalue n′Λ_1, n′ ≡ n mod L, |n′| ≥ 2, forces dim g_m ≥ 2 for m = 0, ±1. Gröbner at L = 5 confirms this, with controls.
  - **Sufficiency.** sl2 ⋉ V_{L−1} (L odd) has three extra generators at momenta 0, ±1. It satisfies (S′) and has Λ_n = n̄Λ_1 for all n (L = 5, 7, 9). Span G is not a subalgebra.
  - **Literal (S) only.** D ⋉ Heisenberg, with one central extra generator, has Λ_n = n̄.
- **Covered:**
  - doubled fields with one diagonal generator per momentum;
  - two independent copies that each close separately.
- **Not covered:**
  - infinite-dimensional enlargements;
  - non-covariant auxiliaries;
  - enlargement combined with structure functions;
  - realisation by lattice relabellings.

## Status

- **Exact:** L1–L5, L8, P6, P7.
- **Numerical:** the `F_R7` sign line only.
- **Conditional:** L3 assumes C is continuous at the background and (S) for the linearisation. L4 assumes linear (or quadratic Poisson) generators.
- **Interpretation only:** the parallel with continuum structure functions, where spatial diffeomorphisms move flat space and the linearised constraints are abelian.
- **Novelty:** L3 and L5 are standard facts (isotropy algebras; frames close with anholonomy coefficients) applied to the arc lemma's setting. No literature search was done.
- **Suggested sharpening of the lane note's "Not claimed":**
  - Structure functions and enlarged generator sets are not excluded; both evade the arc lemma, by explicit constructions.
  - Structure functions help only at backgrounds the relabellings move, or by being discontinuous at the vacuum.
  - For linear matter relabellings about the vacuum they add nothing (L4).
  - Theorems A–C are not contradicted.

## Open

- Restricted structure-function classes (polynomial, field-linear, globally smooth); the ruler model's C is singular where g_x = 0.
- Mixed backgrounds, where some V_n(Φ̄) = 0 and others do not.
- Higher order at a common zero.
- Whether a moved-background relabelling acts consistently on matter; the {G, C} and {C, C} brackets were not examined.
- Phase-space closure off the constraint surface.
- Whether the L8 algebras are realised by lattice relabellings.
