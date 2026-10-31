# GREENT.md — the lattice Green's-function estimate behind Proposition NL-8, and the price it buys

Owner: the Green's-tail worker, session 24. This file is append-only. It may be read by anyone; nobody else writes it.
Requests for other files are collected in the final section "FOR OTHER FILES (not edited)".

---

## §G0 PRE-STATED (first edit of this file, 2026-10-28 15:05:22 UTC; statements only; no constant derived in this session)

This is the first edit of this file. Nothing below §G0 existed when §G0 was written. §G0 fixes the targets, the admissible
outcomes and the failure modes so that the rest of the file can be read against them.

**On the no-constant rule.** Every number quoted in §G0 is read off a file that existed before this file's first edit:
NLOC.md (the (N-loc) worker's file, landed earlier in session 24), NORMS.md, LINEAR_PACKAGE.md v1.1 (frozen), PROOF.md.
No number in §G0, and no number in any `checks/gt1_*_criteria.md`, is produced by a derivation of mine. Where a criterion
needs a threshold, the threshold is either (a) a structural 0/1 verdict, (b) a number already in NLOC.md or
LINEAR_PACKAGE.md, or (c) a round order-of-magnitude bracket fixed in advance and wide enough that it is not a
reverse-engineered pass mark.

**Scope.** This file attacks exactly one hole: the one NLOC.md's Proposition NL-8 names as missing. Proposition NL-8 is
**ARGUED** there, and its stated hole is, verbatim: *"An explicit lattice bound |d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)} on
the torus with C_d explicit, and the first-moment cancellation made quantitative."* I prove that estimate and carry it
through to the constant in Theorem N1-15. I touch nothing else. In particular I do not touch NLOC.md, NORMS.md,
NQ_CHECK.md, LINEAR_PACKAGE.md or any REVIEW_* file; requests for them go in "FOR OTHER FILES (not edited)".

**T-G0 (the statement needed).** Derive, from Proposition NL-8's argument and from what Theorem N1-15 consumes
(NLOC.md §L3's (N-loc♯)), the **exact** Green's-function statement the Coulomb representative's tail requires: which
operator, on which torus, at which level, in which distance, with the constant's dependence on the side made explicit.
State it before proving anything. If Proposition NL-8's own phrasing is ambiguous or names the wrong object, say so and
give the repaired statement; a sharp statement is itself a deliverable.

**T-G1 (prove it).** Prove the estimate at d = 4 on the discrete torus (Z/R)^d, with constants that are **explicit and
independent of R**. Both derivatives are wanted: the kernel of d^*Δ^{−1} (one derivative of the Green's function) and
the kernel's own gradient (two derivatives), the second being what makes the first-moment cancellation quantitative.

**T-G2 (the zero mode and the torus, honestly).** On a torus Δ has a kernel, so Δ^{−1} exists only on the complement of
the constants. State which inverse is used; state what the harmonic/holonomy part contributes, using NLOC.md's Lemma
NL-2 (the chain's constant mode is exactly c_j = L^{−(k−j)}c_k) rather than leaving it in a seam; and state whether the
bound is uniform in the side R, and in T, up to the log.

**T-G3 (first-moment cancellation).** Proposition NL-8 (i) asserts that the leading |x|^{−(d−1)} tail cancels because
the total flux of the curvature response vanishes, and NLOC.md records F̂(0) = 0 as PROVEN from LINEAR_PACKAGE Lemma
4.4's identity 𝔅^v = Σ_μ ν_μ h_{μv}. Make that step quantitative: the gain of one power is a first-moment estimate and
it needs (a) the two-derivative kernel bound of T-G1 and (b) a first-moment bound on the curvature response, which must
be built from LINEAR_PACKAGE Theorem 4.2′'s strip, not assumed.

**T-G4 (carry through).** Report the improved price with its constant, and say explicitly:
 (i) what Corollary NL-4 becomes — the T^d ↦ (the new cell sum) replacement, with the number at NLOC.md's T = T_0;
 (ii) whether **Theorem N1-15 becomes uniform in T, or merely cheaper at fixed T**. NLOC.md §L8 records that N1-15 is
     unconditional at **fixed** T and **not** uniform in T, and that layer 2 needs T-uniformity. A log T is not
     T-uniform. Say plainly what is and is not achieved; do not let a log be read as a constant;
 (iii) whether anything else in NLOC.md's chain has to change — in particular whether the representative that carries
     the new ℓ¹ bound is the **same** representative that carries the sup bound (N-loc-a), which NLOC.md §L2 (A3)
     requires and Proposition NL-9 shows is the step where the naive near/far trade dies.

**T-G5 (scope).** d = 4, trivial background, abelian/linearised (Setting SC), unless proven otherwise. Say so on every
statement.

**Anti-overclaim, binding.**
- **(H-C)'s C_♭ clause is NOT discharged by anything in this file**, and no sentence here may imply it is. Theorem N1-15
  bounds D³E_k^br(1); (H-C) names the Lipschitz constant of Hess E_k^br **on the class**. **(N-bg) is untouched and is
  the larger wall** (NORMS.md Remark N6-5, NLOC.md §L8).
- **(N-loc) is not proven by this file either.** (N-loc-b) as stated in NLOC.md §L2 asserts **exponential** decay; a
  power tail is not exponential decay. What this file can at best deliver is (N-loc♯) with a T-dependent 𝔠_L, i.e. a
  cheaper fixed-T statement. (N-loc-cell) stays OPEN.
- **Imports are re-verified on our structures.** Any literature statement about lattice Green's functions is rebuilt
  here from the torus Fourier/heat-kernel representation of **our** Δ, on **our** torus, with the constant recomputed.
  No Sci-Hub/LibGen; pay for nothing.

**Admissible outcomes, pre-registered.**
- (G-O1) The estimate PROVEN at d = 4 with explicit R-uniform constants; Proposition NL-8 upgraded from ARGUED to
  PROVEN; Corollary NL-4's T^d replaced by a cell sum of size O(log T), with the constant exhibited.
- (G-O2) The estimate PROVEN but the carry-through blocked (e.g. the representative that has the tail is not the one
  with the sup bound, or the first moment is not available). Then say exactly which clause blocks it.
- (G-O3) CONDITIONAL on a named new input.
- (G-O4) **Proposition NL-8 FALSE as stated** — e.g. the tail is |x|^{−(d−1)} and does not improve to |x|^{−d}, or the
  cell sum is a power of T and not a log. To be reported as a refutation of NL-8, not dressed as progress.
- (G-O5) No progress. To be reported plainly.

**Pre-registered failure modes for this session's own work.**
- (G-F1) **The log that is really a power.** A cell sum claimed as log T whose constant secretly carries a power of T,
  or a bound uniform only after a T-dependent constant is absorbed. Any T-dependence outside the single log is a
  failure and is to be reported as one.
- (G-F2) **The R-leak.** A Green's-function constant that degrades as the torus side R → ∞ (or as R → small). The whole
  point is R-uniformity; a constant with an R in it is the same disease as NLOC.md's L-F1 one level down.
- (G-F3) **The wrong operator.** Proving a bound for Δ^{−1} (|x|^{−(d−2)}) or for the continuum kernel and calling it a
  bound for d^*Δ^{−1} on the lattice torus. The lattice kernel, our Δ, our torus, or it does not count.
- (G-F4) **The vacuous gate.** A numeric check assembled from the same primitives as the object it tests, or one whose
  verdict is its own script's definition. At least one check must be able to FAIL, and for each check I must name the
  independent construction it is tested against. A **designed-FAIL control** is mandatory.
- (G-F5) **The moment that is not there.** Using Σ_z F_0(z) = 0 without a bound on Σ_z |z||F_0(z)|: the gain of one
  power is a first-moment estimate and is worthless without the first moment being finite and bounded.
- (G-F6) **Switching representatives mid-proof.** Taking the sup bound from NLOC.md's spread-axial representative
  (Theorem NL-3′) and the ℓ¹ bound from the Coulomb representative. Theorem N1-15 needs **both** from the **same**
  admissible family (NLOC.md §L2 (A3), Proposition NL-9). If I cannot get both from one representative, that is
  outcome (G-O2) and must be said.
- (G-F7) **Admissibility dropped.** The Coulomb gauge at level 0 is a level-0 gauge choice; Lemma N1-2's admissible
  class (nested, trivial at the level-k roots) must be restored exactly as NLOC.md's Theorem NL-3 step (3) does, or
  Theorem N1-15's identity is not available. If the correction is omitted the result is void.
- (G-F8) **Quoting the improvement against the wrong comparator.** NLOC.md's T^d ≈ 2.8·10²⁸ is the price of its
  *unconditional* route; c_m ≈ 7.3·10⁶ is what a true (N-loc) would buy **at the proven rate m_*′ = 0.0384**. A log T
  must be scored against both, and the comparison must use the same rate in both, or it is a false gain.

**Not success.** Numerics in place of a proof. A bound with an unevaluated absolute constant ("C_d absolute, not
computed") — that is exactly what Proposition NL-8 already has and what this task exists to remove. A statement on Z^d
only, when the consumer is a torus. A statement at d = 4 claimed for general d without proof. Declaring Theorem N1-15
T-uniform on the strength of a log.

---

## §G1 What is needed (T-G0), derived from Proposition NL-8's own argument

### §G1.1 The consumer, traced back

NLOC.md §L3 (ii) isolates what Theorem N1-15 consumes: the **column-ℓ¹ mass of the potential-slot response**,

  **(N-loc♯)**  𝔏_j := sup_x Σ_{b ∈ links(level j)} |(ζ^c_{sm,j}δ_x)(b)| ≤ 𝔠_L·L^{(d−1)(k−j)},  n := k − j,

and §L3 (iii) shows that **the only thing 𝔠_L is**, once the sup bound (N-loc-a) |ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P L^{−n}|Y|_∞ is in
hand, is **the cell sum**: grouping the level-j links by the level-k cell containing them, with n_link(j) = d·L^{dn}
links per cell,

  𝔏_j ≤ d·L^{dn}·𝔠_P L^{−n}·𝒮,  𝒮 := Σ_{X ∈ (Z/T)^d} w(|X|_1),   so  **𝔠_L = d·𝔠_P·𝒮**,

where w(D) ∈ [0, 1] is whatever **decay profile in coarse (level-k) ℓ¹ distance** the representative has, normalised
against its own sup bound. So the three routes in the lane differ in **one number**:

| route | profile w | 𝒮 | status before this file |
|---|---|---|---|
| (N-loc) as hypothesised | e^{−m′D} | c_m = coth(m′/2)^d ≈ 7.3·10⁶ at m′ = 0.0384 | hypothesis; open half (N-loc-cell) |
| NLOC.md Cor. NL-4 + [NL-corr 1] | w ≡ 1 (no decay used) | T^d ≈ 2.8·10²⁸ at T = T₀ | PROVEN |
| Prop. NL-8 (Coulomb) | min(1, 𝔠·D^{−d}) | O(log T) | **ARGUED, hole = this file** |

**This is the exact sense in which the task "converts 10²⁸ into ~16": the object to be improved is 𝒮 and nothing else.**
Everything else in NORMS.md Theorem N1-15 — the four exponent counts, A_soft = 1/L, the summation — is untouched,
because 𝒮 enters only as a multiplicative constant in steps (2) and (4).

### §G1.2 The object: which operator, which torus, which level

NLOC.md Proposition NL-8 sets b := d_0^*Δ_0^{−1}(d_0B_0). Unwinding it:

- **Level.** Level 0 (the fine lattice). By NLOC.md Lemma NL-0, a representative of Setting SC's chain minimiser is fixed
  by the **level-0 gauge alone**, and levels j ≥ 1 are then forced by b^{(j)} = Q^j b^{(0)} − Σ_{i<j}Q^{j−1−i}r_i. So
  the only gauge choice to be made, and the only place a Green's function enters, is at level 0.
- **Torus.** The level-0 torus is Λ_0 = (Z/R_0)^d with **R_0 = T·L^k** (LINEAR_PACKAGE §1.1: T_j = T·L^{k−j}). Since
  k → ∞ at fixed T is the regime of interest, **R_0 → ∞**, so the Green's-function constants must be uniform in the side.
  A constant with an R_0 in it would reintroduce L^k and destroy every exponent count: this is failure mode (G-F2) and it
  is the whole content of the estimate.
- **Operator.** Δ_0 is the Hodge Laplacian d_0d_0^* + d_0^*d_0 on level-0 **2-forms**. On the cubic lattice the de Rham
  complex is the d-fold tensor product of the two-term complex, so Δ acts on k-forms **componentwise as the scalar
  Laplacian** (Δf)(z) = Σ_μ[2f(z) − f(z+e_μ) − f(z−e_μ)]. (Checked: gt1-A below; it can fail if a convention is wrong.)
  Hence the kernel of d_0^*Δ_0^{−1} is built from **one difference of the scalar lattice Green's function**, and
  Proposition NL-8's phrase "|d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)}" is exactly the statement that **∇G decays like
  |x|^{−(d−1)}**.
- **Inverse.** Δ on 2-forms has kernel = the constant 2-forms (dimension d(d−1)/2); Δ^{−1} is the inverse on the
  **mean-zero** complement. This is legitimate on our source because F_0 = d_0B_0 is **exact**, and on a torus every
  exact 2-form has zero mean componentwise:
  Σ_z (dB)_{μν}(z) = Σ_z[B_ν(z+e_μ) − B_ν(z)] − Σ_z[B_μ(z+e_ν) − B_μ(z)] = 0 − 0 = 0.   (T-G2, part 1)
  **So the zero mode of Δ is never excited, and no constant ambiguity enters b at all.**

### §G1.3 The two estimates needed, and why there are two

Write 𝒢 for the kernel of d_0^*Δ_0^{−1} and G for the scalar Green's function on (Z/R)^d (mean-zero inverse).
Proposition NL-8's claim is a **two-step** claim, and each step needs its own derivative:

1. The bare convolution bound gives the **|x|^{−(d−1)}** tail: |b(y)| ≲ Σ_z|∇G(y−z)||F_0(z)|, which at coarse distance
   D (fine distance ≍ D L^k) is ≍ (‖F_0‖_{ℓ¹})·(DL^k)^{−(d−1)}. **This is one power short of what is needed**: the
   resulting cell sum is Σ_X|X|^{−(d−1)} ≈ T, not log T. NLOC.md Proposition NL-7's "factor T" is this same power.
2. The gain of the missing power is a **first-moment** estimate: with Σ_zF_0(z) = 0 (§G1.2),
   b(y) = Σ_z[𝒢(y−z) − 𝒢(y−z_0)]F_0(z), and the difference is bounded by |z−z_0| times a **second** difference of G.
   So the upgrade to |x|^{−d} needs **∇∇G**, plus a bound on the first moment Σ_z|z−z_0||F_0(z)|.

Hence the statement to be proven is the pair:

  **(GT-1)** |(∇_μ G_R)(x)| ≤ C_1·|x|_2^{−(d−1)} for every x ≠ 0 in (Z/R)^d, every μ, uniformly in R;
  **(GT-2)** |(∇_μ∇_λ G_R)(x)| ≤ C_2·|x|_2^{−d} for every x with |x|_2 ≥ 2, every μ, λ, uniformly in R;

at **d = 4**, with C_1, C_2 **explicit numbers**. (Euclidean norm is the natural one for the proof; the application uses
coarse ℓ¹ distance and pays the conversion |x|_2 ≥ |x|_1/√d once, explicitly.) **Proposition NL-8's own phrasing names
only the first; the second is the one that does the work**, and NL-8's "the first-moment cancellation made quantitative"
is precisely (GT-2) plus the moment bound (GT-3) below. That is the repaired statement asked for by T-G0.

  **(GT-3)** 𝔐_1 := Σ_z |z − z_0|_1·|F_0(z)| ≤ d(d−1)²M·c_m^{(1)}·L^{(d−1)k}, where z runs over level-0 plaquettes, z_0
  is the level-0 site at the coarse link x, and c_m^{(1)} := Σ_{X∈Z^d}(|X|_1 + d)e^{−m′|X|_1} — the **first-moment
  companion of NORMS.md Lemma N1-7's c_m**, built from LINEAR_PACKAGE Theorem 4.2′'s strip and nothing else.

### §G1.4 Two statements in Proposition NL-8 that are repaired here, not merely proven

- **NL-8 (i) attributes the flux cancellation to F̂(0) = 0 via (J5).** True, but **unnecessary**: on a torus every exact
  2-form has zero mean by telescoping (§G1.2), so the cancellation is unconditional and needs no import. (J5)'s
  F̂(0) = 0 is a strictly stronger, per-fine-offset statement; it is not needed for the moment argument and the argument
  should not be made to depend on it.
- **NL-8 (ii) reads the |x|^{−d} off the symbol** ("bounded, homogeneous of degree 0, not smooth at p = 0"). That is the
  right mechanism but it is a **coarse-symbol** statement about a map that NLOC.md §L7 itself shows is **not**
  level-0-translation-covariant, so there is no fine symbol to be homogeneous and the coarse symbol of the composite is
  not literally ν̄F̂/|ν|². The real-space route — a fine, translation-covariant Green's function convolved against a
  coarse-exponentially-localised source with vanishing mean — needs no symbol for the composite and is the one proven
  below. **This is a repair of NL-8's argument, not only a filling of its hole.**

## §G2 The estimate, proven (T-G1, T-G2, T-G3)

### §G2.0 Setting and the one-dimensional reduction

Λ = (Z/R)^d, R ≥ 3. (Δf)(z) := Σ_{μ=1}^d[2f(z) − f(z+e_μ) − f(z−e_μ)]; (∇_μf)(z) := f(z+e_μ) − f(z);
φ(p) := Σ_μ φ_1(p_μ), φ_1(θ) := 4sin²(θ/2) = 2 − 2cos θ; p ∈ (2π/R)Z^d ∩ (−π, π]^d. G := the inverse of Δ on
mean-zero functions, G(x) = R^{−d}Σ_{p≠0}e^{ip·x}/φ(p), ΔG = δ_0 − R^{−d}, Σ_xG(x) = 0. Coordinates of x are taken
in (−R/2, R/2]; r := |x|_2, s := max_ν|x_ν| ∈ [r/√d, r].

**Lemma GT-0 (the Hodge Laplacian on 2-forms is the componentwise scalar Laplacian): PROVEN-HERE.**
*Statement.* On Λ, (d d^* + d^* d)F = ΔF componentwise, for forms of every degree; in particular
d_0^*Δ_0^{−1} is built from **one difference of the scalar G**, and (GT-1) is a statement about ∇G.
*Proof.* The cubic-lattice de Rham complex is the d-fold tensor product of the two-term complex
(R^{Z/R} →^{∂} R^{Z/R}), ∂f(σ) = f(σ+1) − f(σ): a k-form is a function on sites times a choice of k of the d
factors, and d = Σ_μ ε_μ⊗∂_μ with ε_μ exterior multiplication. Its adjoint is d^* = Σ_μ ε_μ^*⊗∂_μ^*,
∂^*g(σ) = g(σ−1) − g(σ). Then dd^* + d^*d = Σ_{μ,ν}(ε_με_ν^* + ε_ν^*ε_μ)⊗∂_μ∂_ν^*, and the exterior relations give
ε_με_ν^* + ε_ν^*ε_μ = δ_{μν}, so only μ = ν survives and dd^*+d^*d = Σ_μ ∂_μ^*∂_μ acting componentwise, with
(∂^*∂f)(σ) = 2f(σ) − f(σ+1) − f(σ−1). ∎  *(Checked entrywise: clause gt1-A; see §G4 — the check as first written
**FAILED**, for a sign convention in the script, and is re-run under id gt1b.)*

Since P_t := e^{−tΔ} factorises, P_t(z) = Π_{μ=1}^d q_t(z_μ) with q_t the one-dimensional kernel
q_t(σ) = R^{−1}Σ_{θ∈(2π/R)Z}e^{iθσ}e^{−tφ_1(θ)}, and since ∇_μ annihilates the constant R^{−d},

  **(★)  ∇_μ G(x) = ∫_0^∞ ∇_μP_t(x)dt,  ∇_μ∇_λG(x) = ∫_0^∞∇_μ∇_λP_t(x)dt,**

both absolutely convergent (small t: the integrands are bounded by 2 resp. 4; large t: Lemma GT-A (iv)).
**(★) is where T-G2 is answered: the zero mode of Δ does not appear in the kernel of d^*Δ^{−1} at all**, because
every entry of that kernel is a difference of G. It is therefore not the source of the log T; see §G3.3.

### Lemma GT-A (Fourier bounds, uniform in R): PROVEN-HERE

With a_0 := √π/4, a_1 := π/8, b_1 := π/√(2e), a_2 := √π π²/32, b_2 := π²/(2e)
(= 0.4431134627, 0.3926990817, 1.3473723598, 0.5466693227, 1.8154122758), for every t > 0, every R ≥ 3:
 (i) 0 ≤ q_t(σ) ≤ 1 and sup_σ q_t(σ) ≤ R^{−1} + a_0t^{−1/2};
 (ii) sup_σ|∇q_t(σ)| ≤ min{2, a_1t^{−1} + b_1R^{−1}t^{−1/2}};
 (iii) sup_σ|∇²q_t(σ)| ≤ min{4, a_2t^{−3/2} + b_2R^{−1}t^{−1}};
 (iv) with φ_* := 4sin²(π/R) ≥ 16R^{−2}, each of (i)-(iii) also holds with the bracket replaced by
   e^{−8t/R²} times its value at t/2, except that (i) keeps the additive R^{−1} (the zero mode).
*Proof.* q_t ≥ 0 and Σ_σ q_t = 1 because e^{−tΔ_1} is the transition semigroup of the continuous-time walk of
jump rate 1 in each direction; hence (i)'s first claim. For the rest, the symbols of ∇ and ∇² are ν(θ) := e^{iθ}−1
and ν(θ)², with |ν| = 2|sin(θ/2)| = √φ_1 ≤ |θ| and |ν|² = φ_1 ≤ θ². **The zero mode drops out of ∇ and ∇²**
(ν(0) = 0), so
 sup_σ|∇^jq_t(σ)| ≤ R^{−1}Σ_{θ≠0}φ_1(θ)^{j/2}e^{−tφ_1(θ)} ≤ R^{−1}Σ_{θ≠0}|θ|^je^{−aθ²}, a := 4t/π²,
using φ_1(θ) ≥ 4θ²/π² on [−π,π] (sin u ≥ 2u/π on [0,π/2]). For g even and either decreasing on [0,∞) (j = 0) or
unimodal there (j = 1, 2), (2π/R)Σ_{θ≠0}g(θ) ≤ 2∫_0^∞g + 2(2π/R)·max g, so
 R^{−1}Σ_{θ≠0}g ≤ (1/π)[∫_0^∞ g + (2π/R)max g].
With ∫_0^∞e^{−aθ²} = ½√(π/a), ∫_0^∞θe^{−aθ²} = 1/(2a), ∫_0^∞θ²e^{−aθ²} = (√π/4)a^{−3/2} and
max θe^{−aθ²} = (2ae)^{−1/2}, max θ²e^{−aθ²} = (ae)^{−1}, a = 4t/π², this gives exactly (i)-(iii) — for (i) with
the θ = 0 term kept separately as R^{−1}. The caps 2 and 4 are Σ|coefficients| of ∇ and ∇² against Σ_σ q_t = 1.
For (iv) write e^{−tφ_1} ≤ e^{−tφ_*/2}e^{−(t/2)φ_1} and use φ_* ≥ 16R^{−2}. ∎

### Lemma GT-B (the exponential tilt on Z: Gaussian decay **with** the right prefactor): PROVEN-HERE

Let q_t^Z be the kernel on Z. For every λ ≥ 0, with T := t cosh λ and δ := 1 − e^{−λ}:
 |∇^jq_t^Z(w)| ≤ e^{2t(coshλ−1)}·𝔭_j(T, δ)·e^{−λ(|w|−j)},  j = 0, 1, 2,
 𝔭_0 := a_0T^{−1/2},  𝔭_1 := a_1T^{−1} + δa_0T^{−1/2},  𝔭_2 := a_2T^{−3/2} + 2δa_1T^{−1} + δ²a_0T^{−1/2}.
*Proof.* E[e^{λX_t}] = e^{2t(coshλ−1)} =: Z_λ (differentiate and use the generator). Let m_λ(σ) := e^{λσ}q_t^Z(σ)/Z_λ,
a probability measure on Z. Its characteristic function is
 m̂_λ(θ) = Z_λ^{−1}e^{−t(2−2cos(θ−iλ))} = e^{−2T(1−cosθ)}·e^{2it sinθ sinhλ},  so  |m̂_λ(θ)| = e^{−2T(1−cosθ)}.
By Fourier inversion and the symbol computation of Lemma GT-A (with t replaced by T, and **no** R^{−1} term,
the circle being continuous),
 ‖m_λ‖_∞ ≤ a_0T^{−1/2},  ‖∇m_λ‖_∞ ≤ a_1T^{−1},  ‖∇²m_λ‖_∞ ≤ a_2T^{−3/2}.
Now q_t^Z(σ) = Z_λe^{−λσ}m_λ(σ) gives, for σ ≥ 0, the j = 0 claim. For j = 1,
 ∇q_t^Z(σ) = Z_λe^{−λσ}[e^{−λ}∇m_λ(σ) + (e^{−λ}−1)m_λ(σ)], so |∇q_t^Z(σ)| ≤ Z_λe^{−λσ}[‖∇m_λ‖_∞ + δ‖m_λ‖_∞].
For j = 2, writing e^{−λ} = 1 − δ,
 ∇²q_t^Z(σ) = Z_λe^{−λσ}[∇²m_λ(σ) − 2δ∇m_λ(σ+1) + δ²m_λ(σ+2)],
whence the stated 𝔭_2. For σ < 0 use q_t^Z(−σ) = q_t^Z(σ), ∇q_t^Z(σ) = −∇q_t^Z(−σ−1) and
∇²q_t^Z(σ) = ∇²q_t^Z(−σ−2), which replaces σ by min over the j+1 points involved, i.e. by |w| − j at worst. ∎
*Why this lemma and not Chernoff.* The plain Chernoff bound q_t(σ) ≤ 2e^{2t(coshλ−1)−λ|σ|} has **no** t^{−1/2}
prefactor, and with it the time integral (★) produces only |x|^{−(d−2)}, not |x|^{−(d−1)}: the Gaussian factor
cannot pay for a missing power of t. The tilt supplies prefactor and Gaussian **simultaneously**. This is the one
analytic step of the proof and it is where a naive assembly fails.

### Lemma GT-C (periodisation): PROVEN-HERE

For |σ| ≤ R/2 and every λ > 0, |∇^jq_t^R(σ)| ≤ Ω(λ,R)·Z_λ𝔭_j(T,δ)·e^{−λ(|σ|−j)}, where
**Ω(λ,R) := 1 + 2/(1 − e^{−λR})**.
*Proof.* q_t^R(σ) = Σ_{n∈Z}q_t^Z(σ+nR) and differences commute with the periodisation. For n ≠ 0,
|σ+nR| ≥ (|n| − ½)R, so Σ_{n≠0}e^{−λ|σ+nR|} ≤ 2Σ_{m≥1}e^{−λ(m−½)R} = 2e^{−λR/2}/(1−e^{−λR}) ≤ 2e^{−λ|σ|}/(1−e^{−λR}),
the last step because |σ| ≤ R/2. ∎  *(Ω ≤ 3 once λR ≳ 1; it is the entire cost of the torus.)*

### Theorem GT-1 / GT-2 (the estimate, with explicit R-uniform constants): PROVEN-HERE, d = 4 (d = 3 also computed)

Put, for t > 0, R ≥ 3 and the one-coordinate size s,
 U(t) := the right side of Lemma GT-A (i) ∧ (iv);  V(t), W(t) := those of (ii), (iii) ∧ (iv);
 U_s(t) := U(t) ∧ inf_λΩZ_λ𝔭_0e^{−λs};  V_s(t) := V(t) ∧ inf_λΩZ_λ𝔭_1e^{−λ(s−1)};  W_s(t) := W(t) ∧ inf_λΩZ_λ𝔭_2e^{−λ(s−2)};
 𝒱(t,s) := max{V_sU^{d−1}, V·U_s·U^{d−2}},  𝒲(t,s) := max{W_sU^{d−1}, W·U_s·U^{d−2}, V_s·V·U^{d−2}, V²U_sU^{d−3}}.
*Statement.* For every x ≠ 0 and every μ, λ, with s = max_ν|x_ν|,
 **|∇_μG(x)| ≤ Ĉ_1·max(1,s)^{−(d−1)} ≤ C_1·max(1,r)^{−(d−1)}, C_1 := d^{(d−1)/2}Ĉ_1,
   |∇_μ∇_λG(x)| ≤ Ĉ_2·max(1,s)^{−d} ≤ C_2·max(1,r)^{−d}, C_2 := d^{d/2}Ĉ_2,**
 Ĉ_1 := sup_{R≥3}sup_{0≤s≤R/2}max(1,s)^{d−1}∫_0^∞𝒱(t,s)dt,  Ĉ_2 := sup_{R≥3}sup_{0≤s≤R/2}max(1,s)^{d}∫_0^∞𝒲(t,s)dt,
and in **coarse ℓ¹ distance** (what NORMS.md's d_k uses), since s ≥ |x|_1/d,
 **|∇_μG(x)| ≤ C_1^{(1)}max(1,|x|_1)^{−(d−1)}, C_1^{(1)} := d^{d−1}Ĉ_1;  |∇_μ∇_λG(x)| ≤ C_2^{(1)}max(1,|x|_1)^{−d}, C_2^{(1)} := d^dĈ_2.**
*Proof.* By (★) it suffices to bound ∫_0^∞|∇_μP_t(x)|dt and ∫_0^∞|∇_μ∇_λP_t(x)|dt. Fix ν_* with |x_{ν_*}| = s.
Since P_t factorises, |∇_μP_t(x)| is a product of one ∇-factor and d−1 plain factors; bounding the ν_*-factor by
its s-dependent bound (Lemma GT-C, which is valid for **every** λ, so taking an inf over any set of λ is valid) and
every other factor by its sup bound (Lemma GT-A) gives |∇_μP_t(x)| ≤ 𝒱(t,s) — the two cases μ = ν_* and μ ≠ ν_*
being the two entries of the max. Likewise |∇_μ∇_λP_t(x)| ≤ 𝒲(t,s), the four entries of the max being
(μ=λ=ν_*), (μ=λ≠ν_*), (μ≠λ, one equal to ν_*), (μ≠λ, neither equal to ν_*). Integrating in t and multiplying by
max(1,s)^{d−1} resp. max(1,s)^d gives the claim with the stated suprema. The norm conversions use s ≥ r/√d and
s ≥ |x|_1/d. ∎
*The constants (COMPUTED exactly from the above formulas; `checks/gt1_const.py`, scalar arithmetic, upper
Riemann sums on a log-t grid, inf over a finite λ-grid — a finite grid is **valid**, every λ giving a true bound):*

| d | Ĉ_1 | worst (s,R) | C_1 (Euclidean) | C_1^{(1)} (ℓ¹) | Ĉ_2 | worst (s,R) | C_2 | C_2^{(1)} |
|---|---|---|---|---|---|---|---|---|
| 3 | 3.9637 | (2, 4) | 11.90 | 35.7 | 42.81 | (3, 6) | 222.5 | 1155.9 |
| **4** | **6.6948** | **(3, 6)** | **53.6** | **428.5** | **106.42** | **(3, 6)** | **1702.7** | **27242.5** |

**Reported (rounded up): at d = 4, C_1 = 54, C_2 = 1703 (Euclidean); C_1^{(1)} = 429, C_2^{(1)} = 27250 (ℓ¹).**
*Uniformity in R (T-G2, part 2).* The suprema above are attained at the **smallest** admissible side (R = 2s), and
the profile in s converges: at R ≫ s the quantity s^{d−1}∫𝒱 decreases monotonically to **1.0959** and s^d∫𝒲 to
**6.5567** (d = 4; printed in `gt1_const_out.txt`). **There is no logarithmic creep and no R-leak**: pre-registered
failure mode (G-F2) does not occur. The constants are uniform in R, which is what the application needs, R being
the level-0 side T·L^k.
*Looseness, stated.* The exactly computed maxima of the same quantities (clause gt1-C, exact rational Fourier
inversion on (Z/R)^4, R ∈ {3,4,6}) are **m_1 ≤ 0.1698** and **m_2 ≤ 1.7165**, and the continuum value of the
Euclidean constant is 1/(2π²) = 0.0507. So **the proven C_1, C_2 are loose by ≈ 3·10² and ≈ 10³.** That is
reported, not hidden: every number in §G3 inherits it, and sharpening Lemma GT-A's four integrals is the cheapest
way to take 10³ off the final constant.

### Lemma GT-3 (the first moment of the curvature response): PROVEN-HERE given (J4)

*Setting.* Level-0 torus Λ_0 = (Z/R_0)^d, R_0 = T·L^k. Y := δ_x, x a level-k link; F_0 := d_0B_0 the fine curvature
of Setting SC's chain minimiser; z_0 := the level-0 site at x; D(z) := the level-k ℓ¹ distance from z's level-k cell
to x.
*Statement.* (a) **|F_0(z)| ≤ F̄·e^{−m′D(z)}, F̄ := 2(d−1)M L^{−2k}** — this is NORMS.md Theorem N1-15 step (1)'s
input verbatim: by (J4) the B_k-kernel of f_0 obeys |K(X)| ≤ Me^{−m′|X|_1} in level-k units, d_0B_0 = L^{−2k}f_0,
and |d_kδ_x| is supported on 2(d−1) level-k plaquettes where it equals 1.
(b) **Σ_z F_0(z) = 0 componentwise** — unconditionally, because F_0 is exact on a torus (§G1.2); no import needed.
(c) **𝔐_1 := Σ_z|z − z_0|_1|F_0(z)| ≤ d(d−1)²M·c_m^{(1)}·L^{(d−1)k}**, the sum over all level-0 plaquettes and
components, with
 **c_m^{(1)} := Σ_{X∈Z^d}(|X|_1 + d)e^{−m′|X|_1} = c_m·d·[1 + 2w/(1−w²)], w := e^{−m′}, c_m = coth(m′/2)^d,**
the closed form following from Σ_Xw^{|X|_1} = ((1+w)/(1−w))^d and Σ_X|X|_1w^{|X|_1} = [2dw/(1−w²)]·c_m.
*Proof of (c).* A level-0 point in the level-k cell X is at level-0 ℓ¹ distance ≤ L^k(|X−x|_1 + d) from z_0 (each
coordinate differs by at most L^k(|X_μ−x_μ|+1)). There are (d(d−1)/2)L^{dk} level-0 plaquettes per cell, each with
|F_0| ≤ F̄e^{−m′|X−x|_1} by (a). Summing, 𝔐_1 ≤ (d(d−1)/2)L^{dk}·2(d−1)ML^{−2k}·L^kΣ_X(|X|_1+d)e^{−m′|X|_1}. ∎
*At the proven rate m′ = m_*′ = 0.0384 (κ = 1, L = 3): c_m = 7.36·10⁶ and **c_m^{(1)} = 108.1·c_m = 7.96·10⁸**.
At the located (not proven) rate ≈ 1.0: c_m = 21.9 and c_m^{(1)} = 7.40·c_m = 162.* **Failure mode (G-F5) does not
occur: the first moment is bounded, with an explicit constant, and it is where the rate is paid for a second time.*

### Lemma GT-5 (kernel mass against a coarse-exponentially-localised source): PROVEN-HERE

*Statement.* For every y ∈ Λ_0, Σ_{z∈Λ_0}max(1,|y−z|_1)^{−(d−1)}e^{−m′D(z)} ≤ L^k·𝔷, **𝔷 := 1 + 16d + c_m**
(sum over level-0 sites; D(z) the level-k ℓ¹ distance from z's cell to x).
*Proof.* Let 𝔰_{d−1}(N) := Σ_{1≤|w|_1≤N}|w|_1^{−(d−1)}; since #{|w|_1 = s} = Σ_{j≥1}2^jC(d,j)C(s−1,j−1) and at d = 4
that is 8, 32, 88, 192, … with #/s^{d−1} ↓ 2^d/(d−1)! = 8/3, one has **𝔰_{d−1}(N) ≤ κ_𝔰N with κ_𝔰 = 8** (the
maximum of 𝔰_3(N)/N is at N = 1). Group z by its level-k cell X and let σ := the coarse distance from X to y's
cell. For σ ≤ 1 (at most 1 + 2d cells): the z-sum is ≤ 1 + 𝔰_{d−1}(2dL^k) ≤ 1 + 16dL^k, and the weight is ≤ 1.
For σ ≥ 2: |y−z|_1 ≥ (σ−1)L^k and there are L^{dk} sites per cell, so the per-cell sum is
≤ L^{dk}((σ−1)L^k)^{−(d−1)} = L^k(σ−1)^{−(d−1)} ≤ L^k; summing the weight over cells gives L^k·c_m. ∎
*This is where the gain of L^k in the sup bound comes from* — the Coulomb kernel's ℓ¹ mass over one level-k cell
is L^k, not 1 — and it is the same L^k that NLOC.md §L7 identifies as the one that "must come from an integration
over a length L^k". The Coulomb construction supplies it with no box, no string and no T.

### Theorem GT-4 (the Coulomb representative: both legs, from one representative): PROVEN-HERE given (J1)-(J4)

*Statement.* At d = 4, trivial background, abelian/linearised (Setting SC), on the level-0 torus of side
R_0 = T·L^k, let b := d_0^*Δ_0^{−1}(d_0B_0) be the Coulomb representative of the chain minimiser for the level-k
datum Y (well defined by §G1.2, no zero mode). Then, **uniformly in k and in T**:
 **(a) [sup leg]** |b|_∞ ≤ 𝔠_C·L^{−k}|Y|_∞,  𝔠_C := 4d(d−1)²M·C_1^{(1)}·𝔷; for Y = δ_x the constant is
   𝔠_C^δ := 2(d−1)²M C_1^{(1)}𝔷.
 **(b) [tail leg]** for Y = δ_x and D := d_k(y,x) ≥ 8,
   |b(y)| ≤ L^{−k}·[ 𝔠_n·D^{−d} + 𝔠_{ii}·D^{−(d−1)}·Ξ(D/2) + 𝔠_i·(D+4)e^{−3m′D/4} ],
   𝔠_n := 2·4^d·d(d−1)²M·C_2^{(1)}·c_m^{(1)},  𝔠_{ii} := 8^{d−1}d(d−1)²M·C_1^{(1)},
   𝔠_i := κ_𝔰 d(d−1)²M·C_1^{(1)},  Ξ(u) := Σ_{s>u}#{|X|_1 = s}·e^{−m′s}.
 **(c)** b is a level-0 gauge choice, so by NLOC.md Lemma NL-0 it determines the whole family, and after NLOC.md
 Theorem NL-3 step (3)'s correction (Lemma N1-6's nested interpolant of the level-k gauge function) the family is
 **admissible** in Lemma N1-2's sense; the correction term is a pure gauge and is exponentially local by NLOC.md
 Theorem NL-12. Hence, with (J1) ‖Q^j‖_{∞→∞} ≤ 𝔮_0L^j and (J2)+(J3),
   **|ζ^c_{sm,j}Y|_∞ ≤ 𝔠_P^{coul}L^{−(k−j)}|Y|_∞,  𝔠_P^{coul} := (1+𝔮_0)[4d(d−1)²MC_1^{(1)}𝔷 + 1] + 𝔮_0·8dκ̂C_RL²/(L²−1) + 2,**
 which is **(N-loc-a) with a T-free constant**, structurally NLOC.md's 𝔠_P^{tor} with 8d²C_fT replaced by the
 T-free 4d(d−1)²MC_1^{(1)}𝔷. *(Failure modes (G-F6) and (G-F7) do not occur: (a) and (b) are bounds on the **same**
 field b, and (c) restores admissibility exactly as NLOC.md's Theorem NL-3 does.)*
*Proof.* (a) By Lemma GT-0, (d^*Φ)_ρ(y) = Σ_μ[Φ_{μρ}(y−e_μ) − Φ_{μρ}(y)] with Φ = Δ^{−1}F_0 componentwise, so
 b_ρ(y) = −Σ_{μ≠ρ}Σ_z(∇_μG)(y−e_μ−z)F_{μρ}(z);
each kernel entry is bounded by Theorem GT-1 in ℓ¹ form and each |F_{μρ}(z)| by Lemma GT-3 (a) with
F̄_Y := 2(d−1)ML^{−2k}sup|d_kY| ≤ 4d(d−1)ML^{−2k}|Y|_∞. Lemma GT-5 does the z-sum: (d−1)·C_1^{(1)}·F̄_Y·L^k𝔷.
(b) By Lemma GT-3 (b), Σ_zF_{μρ}(z) = 0, so b_ρ(y) = −Σ_{μ≠ρ}Σ_z[(∇_μG)(y−e_μ−z) − (∇_μG)(y−e_μ−z_0)]F_{μρ}(z).
 *Near region* (coarse distance of z to x at most D/2): the difference is a sum of |z−z_0|_1 one-step differences
 of ∇G at points w with |w|_1 ≥ (D/2 − 2)L^k ≥ (D/4)L^k (D ≥ 8), so by Theorem GT-2 in ℓ¹ form it is
 ≤ |z−z_0|_1·C_2^{(1)}(4/D)^dL^{−dk}; summing against |F| gives C_2^{(1)}4^dD^{−d}L^{−dk}·𝔐_1 and Lemma GT-3 (c)
 bounds 𝔐_1 by d(d−1)²Mc_m^{(1)}L^{(d−1)k}; the factor 2 is the μ ↔ ρ double count. **This is the step that buys
 the extra power, and it buys it with the first moment, not with the vanishing mean alone.**
 *Far region* (coarse distance of z to x above D/2): split again by whether z is within coarse distance D/4 of y.
 If it is, then D(z) ≥ 3D/4 and Lemma GT-5's first case (with radius D/4) gives the 𝔠_i term. If it is not, then
 |y−z|_1 ≥ (D/4−1)L^k, the total ℓ¹ mass of F_0 beyond coarse distance D/2 is
 ≤ (d(d−1)/2)L^{dk}F̄·Ξ(D/2), and 4^{d−1}·2^{d−1} = 8^{d−1} absorbs (D/4−1)^{−(d−1)} ≤ 8^{d−1}D^{−(d−1)}; the
 subtracted term (∇_μG)(y−e_μ−z_0) obeys the same bound. (c) is NLOC.md Theorem NL-3 steps (2)-(3) verbatim with
 b^{(0)} = b. ∎
*Status note.* (b) holds for D ≥ 8; for D < 8 the sup bound (a) is used, which is what the profile's min( · ) does.
**M cancels in every ratio below**, so the numbers in §G3 do not depend on LINEAR_PACKAGE's uncomputed M.

---

## §G3 The price, carried through (T-G4)

### §G3.1 The one number that changes

By §G1.1, 𝔏_j ≤ d·𝔠_P^{coul}·𝒮_T·L^{(d−1)n} with the **cell sum**
 **𝒮_T := Σ_{X∈(Z/T)^d} min{1, (𝔠_n/𝔠_C^δ)max(1,|X|_1)^{−d} + (𝔠_{ii}/𝔠_C^δ)max(1,|X|_1)^{−(d−1)}Ξ(|X|_1/2)
   + (𝔠_i/𝔠_C^δ)(|X|_1+4)e^{−3m′|X|_1/4}}.**
Everything else in NORMS.md Theorem N1-15 is untouched. COMPUTED (`checks/gt1_price.py`; exact shell counts
#{|X|_1 = s} = Σ_j2^jC(d,j)C(s−1,j−1), closed-form harmonic tail, scalar floats):

| | at the **proven** rate m_*′ = 0.0384 | at the **located** (not proven) rate ≈ 1.0 |
|---|---|---|
| c_m = coth(m′/2)^d | 7.362·10⁶ | 21.93 |
| c_m^{(1)} (Lemma GT-3) | 7.962·10⁸ = 108.1·c_m | 162.3 = 7.40·c_m |
| q_n := 𝔠_n/𝔠_C^δ | 7.034·10⁶ | 1.215·10⁵ |
| profile saturates (min = 1) out to shell | s = 52 | s = 19 |
| **𝒮_T at T = T_0 = 1.2932·10⁷** | **2.514·10⁸** | **4.664·10⁶** |
| NLOC.md Corollary NL-4's cell sum T^d | 2.797·10²⁸ | 2.797·10²⁸ |
| **gain over T^d** | **1.11·10²⁰** | 6.00·10²¹ |
| cost against an ideal (N-loc) at the same rate | **34.1×** | 2.1·10⁵× |

*T-dependence, checked:* 𝒮_T/log(2T) = 9.71·10⁶, 1.31·10⁷, 1.47·10⁷, 1.55·10⁷, 1.63·10⁷ at
T = 10³, 10⁵, 10⁷, 10⁹, 10¹² (proven rate). **The growth is logarithmic**; the slow drift of the ratio is the
saturated core (the ℓ¹ ball of radius 52, which contributes 8.2·10⁷ of the 2.5·10⁸ and is T-independent).
Pre-registered failure mode **(G-F1) does not occur**: there is no hidden power of T. *Sensitivity:* multiplying
𝔠_i by 100 moves 𝒮_T by 0.19%, so the crudest of the three far-region bookkeeping steps is immaterial.

### §G3.2 **The headline, stated honestly — and a correction to NLOC.md**

**NLOC.md's Proposition NL-8 and its FOR-OTHER-FILES item 7 say the estimate "would take Corollary NL-4's
T^d ≈ 10²⁸ down to log T ≈ 16". That is wrong as a statement about the price, and the error is a factor ≈ 1.6·10⁷.**
log T ≈ 16 is the **log factor**; the constant multiplying it is ≈ 1.5·10⁷ (table above), because the tail
coefficient q_n carries c_m^{(1)}/c_m ≈ 108 — the **first moment** of the already-weak proven kernel rate — on top
of C_2^{(1)}/C_1^{(1)} ≈ 64 and the geometric 4^d. The honest statement is:

> **The price falls from T^d ≈ 2.8·10²⁸ to 𝒮_T ≈ 2.5·10⁸: twenty orders of magnitude, not twenty-seven.** The
> remaining 2.5·10⁸ is **34 times** what a true (N-loc) would buy at the same proven rate (c_m ≈ 7.4·10⁶), so on
> the constants the Coulomb route is **nearly as good as (N-loc) itself** at the rate actually proven — and that
> is the sharper way to score it than the log.

Two further honest riders. (i) The proven Green's constants C_1, C_2 are loose by ≈ 3·10² and ≈ 10³ (§G2); since
𝒮_T is roughly linear in C_2^{(1)}, sharpening them would take most of 10³ off 𝒮_T, i.e. to ≈ 10⁵–10⁶, **below**
c_m. (ii) At the *located* rate the comparison reverses: c_m drops to 21.9 while 𝒮_T only drops to 4.7·10⁶,
because a log T cannot shrink. **So the Coulomb route is the better of the two exactly while the proven rate is
bad, and (N-loc) is worth 10⁵ exactly when the rate is good.** Failure mode (G-F8) is thereby answered: the
comparison is made at a single rate, twice.

### §G3.3 What Corollary NL-4 becomes

**Corollary NL-4′ (PROVEN-HERE given (J1)-(J4), at d = 4, trivial background, abelian/linearised).** NLOC.md's
Corollary NL-4 holds with the substitution **c_m ↦ 𝒮_T** in the two potential-slot ℓ¹ masses (steps (2) and (4) of
Theorem N1-15) and **𝔠_P ↦ 𝔠_P^{coul}**, i.e.
 **𝔚^{coul} + 13.5·𝔖^{coul} ≤ (𝔚 + 13.5𝔖)·(𝒮_T/c_m)·(𝔠_P^{coul}/𝔠_P)²,  𝒮_T/c_m = 34.1 at T = T_0,**
in place of Corollary NL-4's T^d/c_m = 3.80·10²¹. The soft level-ratio is unchanged, **A_soft = 1/L**; the four
exponent counts of §N6 are unchanged; the summation is unchanged. **The T^d of NLOC.md item 6 is replaced by
≈ 34·c_m, i.e. by a number of order 10⁸ instead of 10²⁸.**

**Where the log actually comes from (T-G2, part 3), against the brief's framing.** It is **not** the zero mode.
Every entry of the kernel of d_0^*Δ_0^{−1} is a difference of G, and ∇_μ annihilates the constant R^{−d}
exactly ((★) of §G2.0), so the torus zero mode never enters; and the source F_0 is exact, hence of vanishing
mean, so Δ^{−1} is applied only on its own range. The log T is the **ℓ¹ sum of a |X|^{−d} profile over a box of
side T**: Σ_{s≤2T}#{|X|_1=s}s^{−d} ≈ (2^d/(d−1)!)·log(2T). The harmonic/holonomy part is separately exact and
contributes nothing to the tail: NLOC.md's Lemma NL-2 computes it as the constant 1-form c_j = L^{−(k−j)}c_k with
|c_j|_∞ ≤ L^{−(k−j)}|Y|_∞, which is already inside the sup leg (a) and carries no T. **So the log is a geometric
fact about d = 4 and a box of side T, and it is irreducible by any sharpening of the Green's function.**

### §G3.4 Does Theorem N1-15 become uniform in T? **NO.** (T-G4 (ii), answered plainly)

**A log T is not T-uniform.** Theorem N1-15 is, after this file:
- **unconditional at d = 4, trivial background, abelian/linearised, at every fixed coarse side T ≥ T_0, with a
  constant that grows like (log T)** instead of NLOC.md's T^d — PROVEN-HERE, Corollary NL-4′;
- **not uniform in T, and therefore still not what layer 2 needs.** NLOC.md §L8's second table row is improved in
  its *constant* and unchanged in its *status*: the thermodynamic limit still requires (N-loc-b), i.e.
  (N-loc-cell). The logarithm diverges, slowly, and nothing here removes it.
- The sup leg **is** T-uniform (Theorem GT-4 (a), (c)), as [NL-corr 1] already was; the ℓ¹ leg is not.

So the correct scorecard entry is: **(N-loc) is still open, still needed for layer 2, and now worth a factor
≈ 34 rather than ≈ 10²¹ at fixed T ≥ T_0.** Anyone recording that this file retires (N-loc), or that Theorem
N1-15 is now T-uniform, is recording something false.

### §G3.5 What else in NLOC.md's chain has to change (T-G4 (iii))

1. **Nothing structural.** The representative changes (Coulomb at level 0 in place of Lemma NL-1's spread-axial
   gauge), both legs come from that one representative, Lemma NL-0 and Lemma N1-6 do the rest, and no exponent
   count moves.
2. **[NL-corr 1] is superseded, not contradicted.** Theorem NL-3′ removes the T from the sup leg using the
   gauge-invariant locality; Theorem GT-4 (a) removes it using the Coulomb kernel's ℓ¹ mass over one cell
   (Lemma GT-5). Either is enough, and the second one is the one that also carries the ℓ¹ leg, which is what
   NLOC.md §L2 (A3) requires. **Theorem NL-3′'s constant 𝔠_P^♭ = … + 2d(2d+1)C_fc_m and mine
   𝔠_P^{coul} = … + 4d(d−1)²MC_1^{(1)}𝔷 are both T-free and neither dominates the other.**
3. **Proposition NL-8 (i) should drop its appeal to (J5).** The flux cancellation is elementary on a torus
   (§G1.2, Lemma GT-3 (b)). (J5)'s F̂(0) = 0 is a stronger per-offset statement and is not needed.
4. **Proposition NL-8 (ii)'s symbol argument should be replaced by the real-space one.** There is no fine symbol
   for the composite (NLOC.md §L7's own observation), so "b̂ = ν̄F̂/|ν|² is homogeneous of degree 0" is not
   available for the object in question; the first-moment argument is, and it is what is proven here.
5. **Proposition NL-7 and Proposition NL-9 are untouched** — the axial gauge still fails by a factor T and the
   within-cell gauge still fails the sup budget; the Coulomb representative is a third construction and fails
   neither, at the price of a log.

---

## §G4 Record of the checks — **two clauses FAILED**, reported as FAILs

Criteria written first: `checks/gt1_criteria.md`, before any script existed, with no numeric threshold derived in
this session (every verdict is a 0/1 identity, a proof-vs-measurement comparison, or a growth separation).
Scripts and outputs: `gt1_green.py`/`gt1_out.txt` (exact integers + `fractions`, **no numeric lock**),
`gt1_const.py`/`gt1_const_out.txt` (scalar floats, no arrays, seconds, no lock),
`gt1_sweep.py`/`gt1_sweep_out.txt` (IEEE double, separable nested 1-D DFT, **numeric lock taken and released,
4 s wall, one thread**), `gt1_price.py`/`gt1_price_out.txt` (exact shell counts + scalar floats, 0.1 s, no lock),
`gt1_b.py`/`gt1_b_out.txt` + `gt1_posthoc_out.txt`. The clause names `gt2-E`, `gt2-F` are as pre-registered; they
live in `gt1_sweep.py` because this worker may only create `gt1_`-prefixed files.

**PASS**
- **gt1-B PASS** (solver validation, 6/6 configurations). ΔG = δ_0 − R^{−d} with zero residual and Σ_xG = 0,
  **exactly**, at (d,R) ∈ {3,4}×{3,4,6}. Labelled as solver validation, not as evidence for the theorem.
  *Independent cross-check:* the first and second runs of `gt1_green.py` computed the bare kernel column two
  different ways (a dense rational convolution with G, and the identity Δ^{−1}(δ_0−R^{−d}) = G) and produced
  **byte-identical** output (`gt1_out_run1.txt` vs `gt1_out.txt`).
- **gt1-C PASS.** Exactly computed maxima at d = 4: m_1 = max r^{d−1}|∇G| ≤ **0.16978** (R = 6),
  m_2 = max_{r≥2}r^d|∇∇G| ≤ **1.71652** (R = 4), against the proven **C_1 = 53.6** and **C_2 = 1702.7**.
  Proof ≥ measurement in every case, i.e. **§G2's constants are not refuted**; they are loose by ≈ 3·10² and ≈ 10³,
  which is reported in §G2 and inherited by §G3.
- **gt2-E PASS** (R-uniformity). M_1(R) = 0.0595, 0.0404, 0.0418, 0.0422 and M_2(R) = 0.960, 0.516, 0.404, 0.348
  at R = 8, 12, 16, 24: both **decrease**, growth factors ×0.709 and ×0.363 from R = 8 to R = 24, against the
  pre-registered bracket 2. **Pre-registered failure mode (G-F2), the R-leak, does not occur.**
- **gt1b-A PASS** (the re-run; see the FAIL below). 0 discrepancies out of 243–23328 entries at every
  (d,R) ∈ {3,4}×{3,4,6}, and 0 adjointness failures: **Lemma GT-0 is confirmed entrywise.**

**FAIL (reported as FAILs; the failing scripts and outputs are kept unaltered; criteria untouched)**
- **gt1-A FAIL.** 241/243 … 23143/23328 entries discrepant, 6/6 adjointness tests failed, at every (d,R).
  **Post-hoc diagnosis (labelled post-hoc):** `gt1_green.py`'s `dstar2`/`dstar3` return **minus** the true
  adjoint — they compute F(x) − F(x−e_μ) where ⟨dA,F⟩ = ⟨A,d^*F⟩ forces F(x−e_μ) − F(x) — so the script evaluated
  **−Δ** and the clause necessarily failed. This is a sign convention in the script, not in Lemma GT-0, and the
  adjointness sub-clause located it immediately, which is what it was there for. *Nothing in §G2 or §G3 depends on
  `gt1_green.py`'s d^*:* clauses gt1-B and gt1-C use `Gnum` directly, and gt1-D uses only |b|, which the sign does
  not change. **Re-run under the new id gt1b-A with the criteria untouched: PASS** (above).
- **gt1-D FAIL, and its re-run gt1b-D FAIL.** Pre-registered: "ρ_B strictly increasing over the available shells
  while ρ_A is not". At R = 6 (d = 4): ρ_B = 0.125, 0.340, 0.281, 0.177, 0.195, 0.125 — not increasing; ρ_A =
  0.431, 0.358, 0.499, 0.500, 0.723, 0.750 — increasing. **Both halves of the criterion failed.** Re-run at
  R = 24 (`gt1_sweep.py`, id gt1b-D): ρ_B = 0.125, 0.347, 0.402, 0.400, 0.408, 0.430, 0.457, 0.478, 0.482, 0.451,
  0.387, 0.345; ρ_A = 0.431, 0.361, 0.275, 0.232, 0.199, 0.180, 0.170, 0.165, 0.166, 0.175, 0.202, 0.262 —
  **also not strictly monotone, so gt1b-D FAILS too.**
  **Post-hoc diagnosis (labelled post-hoc): the criterion was mis-designed, in two ways.** (i) It quantified over
  shells up to the half-period |x|_2 ≈ R/2, where the torus reflection symmetry suppresses the kernel, so **no**
  true power law can be strictly monotone there — the criterion was unsatisfiable by construction, which is a
  defect of the gate, not evidence about Proposition NL-8. (ii) It took a **maximum over a shell** of r^d|b| while
  the kernel is evaluated at a *shifted* point (b_B,0(x) = ∇_1G(x−e_1)), so the shell maximum mixes radii.
  **What the data do say, read post-hoc and labelled as such** (`gt1_b.py P`, `gt1_posthoc_out.txt`; one **fixed**
  direction x = (s,0,0,0), interior shells only, R = 24 and R = 32 agreeing to 3-4 digits):
  | s | s³\|b_B\| | s⁴\|b_B\| | s³\|b_A\| | s⁴\|b_A\| | local exponent b_B | local exponent b_A |
  |---|---|---|---|---|---|---|
  | 2 | 0.1735 | 0.3470 | 0.1338 | 0.2677 | — | — |
  | 5 | 0.0820 | 0.4101 | 0.0399 | 0.1994 | 3.89 | 4.68 |
  | 10 | 0.0572 | 0.5722 | 0.0159 | 0.1585 | 3.49 | 4.13 |
  **s⁴|b_A| is bounded and decreasing (0.268 → 0.158) while s⁴|b_B| grows (0.347 → 0.572), and the local decay
  exponent of the zero-mean-source response exceeds that of the bare kernel at every s, by ≈ 0.7.** That is
  Proposition NL-8 (ii)'s mechanism, and it is the designed-FAIL control doing its job: the b_B arm does **not**
  satisfy the d-th-power claim, so the b_A arm's satisfying it is not vacuous. **But this is a post-hoc reading,
  not a passed gate, and it is recorded as such.**
- **gt2-F FAIL.** Pre-registered: "s³|∇G| bounded within a factor 2 over s ≥ 2 at R = 24 while s⁴|∇G| grows
  monotonically, and likewise for s⁴|∇²G| vs s⁵|∇²G|". Result: s⁵|∇²G| **is** monotone (PASS on that clause), but
  s³|∇G| varies by a factor 4.05 over s ∈ [2,12] and s⁴|∇G| is not monotone past s = 8. **FAIL.**
  **Post-hoc diagnosis (labelled post-hoc): the same mis-design** — the range included s up to R/2 = 12. On
  s ∈ [2,8]: s³|∇_1G| = 0.03965, 0.04219, 0.04180, 0.04151, 0.04111, 0.04002, 0.03758 — constant to **6%** — while
  s⁴|∇_1G| rises from 0.0793 to 0.3006, a factor **3.8**. So the exponent of ∇G is d−1 = 3 and not d = 4, as
  Theorem GT-1 asserts; and s⁴|∇²G| varies by 2.1× on [2,8] while s⁵|∇²G| rises monotonically by 8.5×, so the
  exponent of ∇∇G is d = 4. **Post-hoc, labelled.**

**What a hostile reviewer should take from §G4.** Two of my five criteria clauses failed; one failure was a script
sign bug that the re-run cleared, and the other two were a **badly designed gate** (a monotonicity test taken over
the torus half-period). The substantive content — Lemma GT-0, the exponents d−1 and d, R-uniformity, and
proof ≥ measurement for C_1 and C_2 — is carried by gt1-B, gt1-C, gt2-E and gt1b-A, which passed, plus a post-hoc
fixed-direction reading that is labelled post-hoc and is not counted as a gate.

---

## §G5 Tally, scope, and verdict

**PROVEN-HERE (complete proofs written out above, from stated hypotheses; the scope of every item is d = 4
(d = 3 also computed), trivial background, abelian/linearised — Setting SC — on the torus)**
1. **Lemma GT-0** — the lattice Hodge Laplacian is the componentwise scalar Laplacian in every degree, so
   d_0^*Δ_0^{−1} is built from one difference of the scalar Green's function. (Checked entrywise: gt1b-A PASS.)
2. **Lemma GT-A** — Fourier sup bounds on the 1-D torus heat kernel and its first two differences, with the five
   explicit constants a_0, a_1, b_1, a_2, b_2, uniform in R, including the spectral-gap form.
3. **Lemma GT-B** — the exponential-tilt bound on Z: Gaussian decay **with** the correct t^{−1/2}, t^{−1},
   t^{−3/2} prefactor, from the tilted measure's characteristic function. **This is the one step where a naive
   assembly fails**: plain Chernoff has no prefactor and yields only |x|^{−(d−2)}.
4. **Lemma GT-C** — periodisation of the tilt bound to (Z/R)^d, with the single cost Ω = 1 + 2/(1−e^{−λR}) ≤ 3.
5. **Theorem GT-1 / GT-2** — **the estimate the task asked for**: on (Z/R)^d at d = 4, uniformly in R,
   |∇G(x)| ≤ 54·max(1,|x|_2)^{−3} and |∇∇G(x)| ≤ 1703·max(1,|x|_2)^{−4}; in coarse ℓ¹ distance,
   429·max(1,|x|_1)^{−3} and 27250·max(1,|x|_1)^{−4}. Constants explicit, R-uniform, no logarithmic creep.
6. **Lemma GT-3** — the first-moment companion of NORMS.md Lemma N1-7: Σ_z|z−z_0|_1|F_0(z)| ≤ d(d−1)²Mc_m^{(1)}L^{(d−1)k}
   with c_m^{(1)} = c_m·d[1 + 2w/(1−w²)] in closed form; and (b) **Σ_zF_0(z) = 0 unconditionally**, by exactness
   on a torus, with **no appeal to (J5)**.
7. **Lemma GT-5** — the Coulomb kernel's ℓ¹ mass against a coarse-exponentially-localised source is L^k·(1+16d+c_m):
   this is where the L^k that (N-loc-a) needs comes from, with no box, no string and no T.
8. **Theorem GT-4** — **the Coulomb representative carries both legs**: the T-free sup bound (N-loc-a) with
   𝔠_P^{coul}, and the |D|^{−d} tail, from the **same** admissible family (Lemma NL-0 + Lemma N1-6 + Theorem NL-12).
9. **Corollary NL-4′ (§G3.3)** — Theorem N1-15 unconditional at fixed T ≥ T_0 with **𝒮_T ≈ 2.5·10⁸** in place of
   NLOC.md's **T^d ≈ 2.8·10²⁸**: a factor **1.1·10²⁰**, and only **34×** worse than an ideal (N-loc) at the same
   proven rate. A_soft = 1/L and the four exponent counts are untouched.

**COMPUTED (exact where stated)**
10. The constants of item 5 (`gt1_const.py`), the cell sums and the price table of §G3.1 (`gt1_price.py`, exact
    shell counts), and the exact maxima m_1, m_2 of gt1-C (`gt1_green.py`, exact rationals).

**ARGUED / repaired, not proven**
11. **Proposition NL-8 is upgraded from ARGUED to PROVEN in substance, and repaired in two places** (§G1.4, §G3.5):
    its (i) needs no (J5), and its (ii)'s symbol argument is not available for the composite map and is replaced by
    the real-space first-moment argument. **Its quantitative claim — "down to log T ≈ 16" — is CORRECTED: the
    number is 2.5·10⁸, not 16** (§G3.2).

**OPEN, unchanged by this file**
12. **(N-loc-b) / (N-loc-cell)** — still OPEN. A power tail is not exponential decay; the log T is irreducible by
    any sharpening of the Green's function (§G3.3), so **(N-loc) is still needed for layer 2**.
13. **T-uniformity of Theorem N1-15** — **NOT achieved** (§G3.4). The sup leg is T-uniform; the ℓ¹ leg carries log T.
14. **(N-bg)**, and **(H-C)'s C_♭ clause** — untouched, and (N-bg) is the larger wall. Theorem N1-15 bounds
    D³E_k^br(1); (H-C) names the Lipschitz constant of Hess E_k^br **on the class**. **Nothing in this file bears
    on that**, and nothing here should be read as discharging it.
15. **General d** — Theorem GT-1/GT-2 are stated and computed at d = 4 and d = 3; the proof is written for general
    d but the constants are evaluated only there. Nothing is claimed at other d.

**Pre-registered outcome reached: (G-O1), with the two riders of §G3.2 and the FAILs of §G4.** The estimate is
PROVEN with explicit R-uniform constants; Proposition NL-8's hole is closed and its arithmetic corrected;
Corollary NL-4's T^d is replaced by a cell sum of size O(log T) with the constant exhibited. **(G-O4) is not
reached** — Proposition NL-8 is not false; only its headline number was.

**Counted here: nothing.** This file is not a ledger and no item above is to be added to PROOF.md's tally by me.

---

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file.

**1. NLOC.md — Proposition NL-8's hole is closed, but its headline number is wrong by ≈1.6·10⁷, and item 13 of §L9
and item 7 of its FOR OTHER FILES should be corrected.** §L5 and §L9 item 13 say the missing lattice estimate
"would take Corollary NL-4's T^d ≈ 2.8·10²⁸ down to log T ≈ 16". The estimate is now PROVEN (Theorem GT-1/GT-2,
with C_1^{(1)} = 429, C_2^{(1)} = 27250 in coarse ℓ¹ distance, uniform in the torus side) and carried through
(Theorem GT-4, Corollary NL-4′). **The resulting cell sum is 𝒮_T = 2.5·10⁸ at T = T_0, not 16**: log T ≈ 16 is
only the log factor, and the constant in front of it is ≈1.5·10⁷, dominated by c_m^{(1)}/c_m ≈ 108 (the first
moment of the proven kernel rate) times C_2^{(1)}/C_1^{(1)} ≈ 64 times 4^d. The gain over T^d is **10²⁰, not 10²⁷**.
Recommended edit: replace "log T ≈ 16" by "𝔠·log T with 𝔠 ≈ 1.5·10⁷, i.e. ≈2.5·10⁸ at T = T_0 — a gain of 10²⁰
over T^d and a factor 34 worse than an ideal (N-loc) at the same rate".

**2. NLOC.md — Proposition NL-8 (i) should drop its appeal to (J5), and (ii) should drop the symbol argument.**
(i) On a torus every exact 2-form has vanishing mean componentwise, by telescoping: Σ_z(dB)_{μν}(z) = 0. So the
flux cancellation is unconditional and needs neither Lemma 4.4 nor F̂(0) = 0. (ii) NLOC.md §L7 itself establishes
that Y ↦ B_0 is covariant only under **level-k** translations, so there is no fine symbol for the composite and
"b̂ = ν̄F̂/|ν|², bounded and homogeneous of degree 0" is not a statement about the object in question. The
real-space route (fine translation-covariant Green's function, convolved against a coarse-exponentially-localised
source of vanishing mean, with a **first-moment** bound) is what proves it and is written out in §G2.6.

**3. NLOC.md — the tail is bought by the first MOMENT, not by the vanishing mean; the hole's statement should say
so.** NL-8's stated hole asks for "|d_0^*Δ_0^{−1}(x)| ≤ C_d|x|^{−(d−1)} … and the first-moment cancellation made
quantitative". The first half alone gives only |x|^{−(d−1)}, whose cell sum is ≈T, not log T. The upgrade needs
the **second** difference of G (Theorem GT-2) **and** a bound on Σ_z|z−z_0||F_0(z)| (Lemma GT-3 (c)), which is a
new constant c_m^{(1)} = Σ_X(|X|_1+d)e^{−m′|X|_1} that no file in this lane had. Recommended: record (GT-1),
(GT-2), (GT-3) as the three things NL-8 needs, not one.

**4. NORMS.md — Lemma N1-7 should gain its first-moment companion.** Lemma N1-7 converts a sup bound plus
exponential locality into an ℓ¹ mass with c_m = coth(m′/2)^d. Every power-tail argument in this lane needs the
companion **c_m^{(1)} := Σ_X(|X|_1+d)e^{−m′|X|_1} = c_m·d[1 + 2w/(1−w²)], w = e^{−m′}** (= 108.1·c_m at
m′ = 0.0384, 7.40·c_m at m′ = 1). It is one line and it is the constant that the proven-vs-located rate gap is
paid in a **second** time.

**5. NORMS.md — Theorem N1-15's hypothesis (N-loc) may now be replaced, at fixed T, by a THIRD option.** §N4
offers (N-loc) or "an explicit near/far split"; NLOC.md Proposition NL-9 shows the latter fails. The third option
is the Coulomb representative: it satisfies (N-loc-a) with a T-free constant **and** (N-loc♯) with
𝔠_L = d𝔠_P^{coul}𝒮_T, 𝒮_T = O(log T), **from one admissible family**. Recommended: record it as the standing
fixed-T route and keep (N-loc) named as what layer 2 still needs.

**6. PROOF.md / SF.md — the fixed-volume statement's constant improves by 10²⁰ and its STATUS does not change.**
Theorem N1-15 is unconditional at d = 4, trivial background, linearised, at every fixed coarse side T ≥ T_0, now
with a (log T)-sized constant. **It is still not uniform in T**; layer 2's cluster expansion and thermodynamic
limit still need (N-loc-b)/(N-loc-cell). If anyone records that (N-loc) is retired or that N1-15 is T-uniform,
that is false. **(N-bg) and (H-C)'s C_♭ clause are untouched.**

**7. Whoever owns the next slot — the cheapest remaining factor in THIS sub-lane is 10³, and it is in Lemma GT-A.**
The proven C_1 = 54, C_2 = 1703 are loose by ≈3·10² and ≈10³ against the exactly computed maxima 0.170 and 1.717
(gt1-C) and against the continuum constant 1/(2π²) = 0.0507. All of the looseness is in (a) the four crude
integral bounds of Lemma GT-A, (b) the single-coordinate reduction in Theorem GT-1's proof (which costs
d^{d−1} = 256 in the ℓ¹ form), and (c) the small-R corner s = 3, R = 6 where the sup is attained. Sharpening
(a) and (b) — using **all** d coordinates' tilt factors instead of only the largest — would take ≈10³ off
𝒮_T, bringing it to ≈10⁵–10⁶, i.e. **below c_m**, at which point the Coulomb route would be strictly better than
an ideal (N-loc) at the proven rate. That is a bounded, classical exercise with an explicit payoff.

**8. The lead — three claims of mine a hostile reviewer should attack first.**
(i) **Theorem GT-1/GT-2's constants are evaluated by grid quadrature**, not in closed form: the integrals
∫_0^∞𝒱(t,s)dt are upper Riemann sums on a log-t grid (70 points per decade, per-interval max over three points)
and the λ-infimum is over a finite geometric grid. The λ-grid is harmless (every λ gives a valid bound, so a
finite grid is a valid upper bound), but **the t-quadrature is an estimate of an upper sum, not a proof of one**;
a reviewer should either bound the quadrature error or replace the integrals by closed forms. The reported
constants are rounded up, and gt1-C's exact maxima are 300-1000× below them, so an error of a few per cent cannot
change any conclusion — but the status of "54" and "1703" is **COMPUTED upper sum**, not closed form.
(ii) **The far-region bookkeeping in Theorem GT-4 (b) is crude** (three sub-regions, with (D/4−1)^{−(d−1)}
absorbed into 8^{d−1}D^{−(d−1)} and a half-rate split of the exponential). I checked it is immaterial —
multiplying 𝔠_i by 100 moves 𝒮_T by 0.19% — but a reviewer should verify that the 𝔠_{ii} term really is
exponentially cut off and does not hide a factor T; that is the one place where a mistake would restore a power
of T rather than a log.
(iii) **Theorem GT-4 (c)'s admissibility step is imported from NLOC.md's Theorem NL-3 step (3) verbatim**, with
b^{(0)} = the Coulomb field in place of the spread-axial field. I checked that step (3) uses nothing about which
level-0 gauge was chosen — only Lemma NL-0 and Lemma N1-6 — but it is the clause that makes Theorem N1-15's
identity available at all, and failure mode (G-F7) would void everything. A reviewer should re-derive it for the
Coulomb field rather than take my word that the substitution is innocent.
