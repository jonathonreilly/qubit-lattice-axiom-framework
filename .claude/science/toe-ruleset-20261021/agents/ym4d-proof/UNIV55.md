Reviewer model: claude-opus-5-5

# UNIV55 — rotated-lattice universality in a bounded region (P4's S2 / H2): statement, the UV-or-IR question, a conditional reduction

## PRE-STATED — 2026-10-28T23:43:26Z (written before any derivation in this file)

**Role.** Opus 5.5 worker (model ID above, verbatim from my system prompt), effort max. Rules: scratchpad
`REVIEW_BRIEF_55.md` (worker; rules apply). No git. I write only this file and `checks/un55_*`. Inputs read before this
pre-statement: REVIEW_BRIEF_55.md; PANEL_P4.md (all, incl. §5, §8, §9); PANEL_P1.md §1-§4; PANEL_P3.md §1-§7;
ROTDEF.md (pre-statement only; its target is the flat-torus rotation-defect identity — I do not duplicate it);
REVIEW_S22.md `Statement (BFT)`; PROOF.md §0, §1 (S1-S7), L7.0/L7b (E7), S5', L8c-L9 (incl. L9b, R9.1, E9.1),
the Decision-4 kernel definition (string "Decision 4: the RG kernel"); PLAN_S26.md §1-§2. No derivation yet.

**Targets.**
- U1. State the lemma precisely: regions, boundary conditions, observable class, tuning rule, the common coarse space
  for two differently oriented lattices, and the mode of convergence.
- U2. Decide whether it is genuinely ultraviolet. Test P4 §5.3 S2(ii) ("compactness of SU(N) bounds the coarse curvature
  by O(ℓ_0^{-2}) for EVERY coarse configuration ... so the grid dependence ... is O((a/ℓ_0)^θ) per block") and (iii)
  ("summed error O((R/ℓ_0)^4 (a/ℓ_0)^θ) → 0 at fixed R"). Find the step where IR (or other non-UV) information could
  enter, and say whether it does.
- U3. Prove what can be proved, CONDITIONAL on named layer-1 inputs (BFT clauses, large-field bounds, coupling flow),
  or give the exact first point where information beyond them enters.
- U4. Assess Gantumur, arXiv:2512.22072 (v2), read-only via web: does it help this lemma, give an alternative OS1 route,
  or is it irrelevant; its stated limitations.

**What would count as a refutation (of P4's "S2 is UV" claim), stated before deriving.**
- R-a. An explicit mechanism by which a lattice-orientation-dependent quantity of size o(1) per block but NOT summable
  over the (R/ℓ_0)^4 blocks — or a quantity of size O(1) on a set of coarse configurations of non-negligible probability —
  changes a local expectation by O(1) in a fixed bounded region. Example class: a tunnelling/selection effect between
  coarse "phases" at the fixed region scale, or a relevant/marginal orientation-dependent coupling.
- R-b. A step in S2(ii) that uses a bound valid only in the small-field region, while the large-field contribution at
  the coarse scale ℓ_0 is not small (the coarse integral at ℓ_0 is strongly coupled at distances ≫ ℓ_0, so "uniformly
  over all coarse configurations" must be checked against the actual large-field architecture).
- R-c. Showing that a DIFFERENCE estimate summed over the whole region necessarily needs a bound on a covariance
  integral ∫ Cov(F, O(x)) dx over the region (P1 §3's identity) with no UV smallness, i.e. a long-distance quantity.
  At FIXED R this is finite-volume, but I must check whether its constant is controlled without IR input.
- R-d. Showing that no common coarse space exists in which the two regularisations' laws are comparable by an estimate
  of the claimed form (e.g. the two grids' block variables are not functions on one space, and the comparison of laws
  requires an identification step that is itself not local).
Conversely, P4's claim survives (as CONDITIONAL) if I can write the difference as a sum of per-block terms, each bounded
by a UV quantity uniformly in the conditioning coarse field (including large coarse fields), with the number of
summands polynomial in R/ℓ_0 and each term o(1) as a → 0, using only named inputs.

**What would count as a refutation of my own reduction.** If my reduction's per-block bound is uniform only on the
small-field set at scale ℓ_0, or if the normalization makes the defect trivially small (a check that cannot fail), or
if I silently assume the UV RG is controlled with the coarse field held at a fixed configuration that has zero
probability weight in the full measure, I will say so.

**Labels used.** PROVEN (complete argument here), CONDITIONAL (named inputs), ARGUED (stated gap), OPEN, [m] (literature
from memory, unverified). Every inherited PROVEN label is treated as an unverified claim.

**Numeric checks.** Only if a number decides something; criteria file `checks/un55_<id>_criteria.md` first, exact
rational arithmetic in plain python.

---

**Independence note.** §1-§3 below were written before I opened CODEX_REVIEW_P4.md, FLOW55.md, or the current (grown)
ROTDEF.md. Gantumur's paper was read (arXiv abstract pages v2/v3 and the v2 HTML, via WebFetch summaries; nothing
downloaded or saved) before §4. A comparison with CODEX_REVIEW_P4.md, read afterwards, is §6.

---

## 1. The lemma, stated precisely (U1)

### 1.1 First, what the lemma can NOT mean (a trivial reading and an ill-posed one). PROVEN
- **Trivial reading.** If grid R is the rotated image of grid 1 *together with* its volume, boundary data and coupling
  profile, then the two lattice measures are exactly conjugate: ω^{(R)}_a((α_R F)_a) = ω^{(1)}_a(F_a) at every a, provided
  the approximant of α_R F on grid R is the R-image of the approximant of F on grid 1 (transport of structure: Haar
  measure and the Wilson action are carried by R). So "|ω^{(1)}_a(F_a) − ω^{(R)}_a((α_R F)_a)| → 0" is content-free in that
  reading. ∎
- **The content.** The volume (or the observable) must stay FIXED while only the lattice turns. Then exact conjugacy turns
  the lemma into a statement about ONE lattice theory: on S^4_R, E_{g𝒦}[O] = E_𝒦[g^{-1}O] (P4 §5.3 S2), so
  "E_𝒦[O] − E_{g𝒦}[O] → 0" says the 𝒦-limit is g-invariant; on a fixed torus (below), it says the limit on a torus is
  determined by the torus as a Riemannian manifold, not by how the lattice sits in it. Every non-trivial version
  compares the SAME continuum observable in two regularizations that are not conjugate by any isometry of the fixed
  geometry.
- **Ill-posed reading.** "Two lattices restricted to one bounded region Ω ⊂ R^4, with boundary" needs a boundary condition
  that both lattices can carry. Grid 1 and grid R meet ∂Ω differently, so the comparison then contains a SECOND
  universality question: two discretizations of the same boundary condition (a codimension-1 lattice-scale defect, of the
  same kind as P4's seam S4(b)). I therefore state the lemma on closed fixed-volume geometries (§1.2, §1.3) and, separately,
  in an exterior-conditioned form (§1.4) that is what the flat route needs.

### 1.2 Version T (fixed flat torus, rational rotations)
- **Geometry.** T_ℓ := R^4/ℓZ^4 at fixed physical side ℓ (no boundary). Grid 1: Λ_a := aZ^4/ℓZ^4. Grid R: Λ^R_a := R(aZ^4)/ℓZ^4,
  for R ∈ SO(4) ∩ M_4(Q) with common denominator q_R, along the spacings a ∈ A_R := {ℓ/(q_R n) : n ∈ N}. Then R^{-1}ℓZ^4 ⊂ aZ^4,
  i.e. ℓZ^4 ⊂ R(aZ^4), so grid R is a periodic lattice on T_ℓ. PROVEN (one line: R^{-1}(ℓe_i) = a·(ℓ/a)R^{-1}e_i and
  (ℓ/a)R^{-1}e_i ∈ n q_R R^{-1}e_i ∈ Z^4).
- **One rotation suffices.** Rational rotations exist with angle θ ∉ πQ, e.g. the (1,2)-plane rotation with cos θ = 3/5,
  sin θ = 4/5 (q_R = 5). θ/π is irrational by Niven's theorem (the only rational values of cos at rational multiples of π
  are 0, ±1/2, ±1) [m: Niven]. Together with the hypercubic group this generates a dense subgroup of O(4) — this is P2's
  group lemma as adopted by P4 §9.3; I did not re-derive it.
- **What it says geometrically.** Λ^R_a on T_ℓ is the R-image of Λ_a on the torus R^{-1}T_ℓ := R^4/R^{-1}ℓZ^4, which is
  ISOMETRIC to T_ℓ. So Version T says: the continuum limit of grid-1 lattice YM on a flat torus depends only on the torus
  up to isometry, not on the orientation of the period lattice relative to the grid. On the flat route this is exactly
  the UV half of P4's IR input (I2) ("torus limits converge independently of the orientation of the period lattice").
- **Tuning rule.** One bare-coupling function g_0(a), the same number for both grids at each a (e.g. the two-loop AF
  formula with a fixed Λ_phys). No renormalization condition is needed: because the two grids are not conjugate by an
  isometry of T_ℓ, the content of the lemma is precisely that the SAME bare rule yields the same limit.
- **Observables 𝒜_flow.** The *-algebra generated by Re/Im tr W_t(γ): the trace of the holonomy of the Wilson-flowed
  lattice field at fixed physical flow time t > 0, along a fixed piecewise-C^1 loop γ ⊂ T_ℓ, approximated by a nearest
  staircase loop γ_a^G on grid G. Bounded (|tr W| ≤ N), gauge invariant, defined on every grid, rotation acts by
  γ ↦ Rγ. (Unflowed lattice Wilson loops are NOT usable: their perimeter self-energy drives ⟨tr W(γ_a)⟩ to 0 as a → 0
  [m: standard; linear divergence of the Wilson-line self-energy in 4D].) 𝒜_flow is a determining class for the state only
  CONDITIONALLY (it needs the flowed fields to converge and to separate states; this is the γ2/H5 obligation, not part
  of this lemma). Any other observable class with the same three properties (defined on every grid, continuum meaning,
  bounded) may replace it.
- **Statement (UNIV-T).** For each F ∈ 𝒜_flow, Δ_a(F) := |E_{Λ_a}[F_a] − E_{Λ^R_a}[F_a]| → 0 as a → 0 along A_R.
- **Mode of convergence.** Difference form, no rate, no convergence of either sequence. Consequence (PROVEN): along any
  subsequence a_j ∈ A_R on which both sequences of states converge on 𝒜_flow, the two limits coincide. E7-type
  convergence is not needed (agreeing with P4 §4.4).

### 1.3 Version S (S^4_R, P4's sphere route)
- **Geometry and regularization.** P4 §5.2: stereographic grids Λ_± with seam, position-dependent bare coupling
  g_0(x; a) fixed by one rule, cellulation 𝒦_a; and g𝒦_a for g ∈ G_0 ⊂ SO(5) countable dense (coupling transported).
- **Observables.** 𝒜_flow(S^4_R): as in 1.2, with the flow defined as the gradient flow of the regularization's own action
  in physical flow time (local lattice rate t/(aΩ(x))^2); loops in S^4_R approximated on each cellulation.
- **Statement (UNIV-S = P4's S2).** For each O ∈ 𝒜_flow(S^4_R) and g ∈ G_0: E_{𝒦_a}[O_a] − E_{g𝒦_a}[O_a] → 0 at FIXED R, with
  constants allowed to depend on R. Locally, 𝒦_a and g𝒦_a differ by a rotation AND a dilation (a Möbius map is locally a
  rotation times a scale), and their seams sit in different places; so UNIV-S contains UNIV-T-type orientation
  universality plus scale and seam universality (P4 S4(a)-(b)).
- **Consequence (P4, re-derived).** E_{g𝒦}[O] = E_𝒦[g^{-1}O] exactly; hence every subsequential limit μ_R satisfies
  μ_R(g^{-1}O) = μ_R(O) for g ∈ G_0, hence (continuity of g ↦ μ_R(g^{-1}O), which needs equicontinuity of 𝒜_flow under
  SO(5) — CONDITIONAL) SO(5)-invariance. Uniformity in R is NOT needed here; it is needed later, in P4's S5.

### 1.4 Version Ω (bounded region, conditioned on the exterior; what the flat route needs)
- Ω: a bounded union of coarse blocks of side ℓ_0 in R^4; F ∈ 𝒜_flow supported (up to Gaussian flow tails) in Ω shrunk
  by a collar of width w ≫ ℓ_0 + √t.
- The conditioning variable must be COMMON to both grids. Fine configurations of different grids live on different
  spaces, so the exterior datum is the coarse field ξ outside Ω on the common coarse lattice (§2.3), not a fine boundary
  condition. Statement: sup_ξ |E^{(1)}_a[F | ξ] − E^{(R)}_a[F | ξ]| → 0, with constants depending on |Ω|, w, F.
- This is UV in exactly the sense of §2 (the interior coarse integral is finite-dimensional, uniformly in ξ). It does NOT
  give orientation independence on R^4: that needs the exterior LAWS ν^{(1)}(dξ), ν^{(R)}(dξ) to agree, which is the IR
  selection question (P4 §4.1, P1 §3, P2 TORQUE). §2.2 locates the exact point.

**Erratum to 1.2 (wording, written at once).** The periodicity line should read: (ℓ/a)R^{-1}e_i = n·(q_R R^{-1}e_i) ∈ Z^4,
because q_R R^{-1}e_i ∈ Z^4; hence R^{-1}(ℓe_i) ∈ aZ^4 and ℓe_i ∈ R(aZ^4). **Group lemma, now re-derived (PROVEN):** the
closure of ⟨H_4, R_θ⟩ with θ ∉ πQ contains the closure of {R_θ^n}, i.e. all of SO(2)_{12}; conjugating by axis permutations
in H_4 gives every SO(2)_{μν}; these generate SO(4) (their generators span so(4)); with the reflections in H_4, O(4). ∎

---

## 2. Is the lemma genuinely ultraviolet? (U2)

### 2.0 Set-up shared by all versions (soft-kernel representation; lane: "Decision 4: the RG kernel")
- Grid G ∈ {1, R}: fine law μ^G(dU) ∝ e^{-S^G(U)} dU (Haar product). A COMMON coarse lattice E_0 at the fixed scale ℓ_0
  (where the running coupling is still small, g_0), the same for both grids (§2.3 says how grid R reaches it).
- The composite of all soft RG steps from grid G down to E_0 is a Markov kernel k^G(V | U) dV (product of soft kernels;
  each step integrates to 1 in its output). Joint law μ^G(dU) k^G(V|U) dV. Coarse marginal ν^G(dV) = ρ^G(V) dV,
  ρ^G(V) = ∫ k^G(V|U) μ^G(dU). Conditional expectation E^G[F | V] = ∫ F k^G(V|·) dμ^G / ρ^G(V). Exact identity:
  E_{μ^G}[F] = ∫ ν^G(dV) E^G[F | V]. (Exactness uses only ∫k dV = 1.)

### 2.1 Proposition T (fixed volume: the coarse integral drops out). PROVEN
**Claim.** Suppose, for one F with ||F||_∞ ≤ 1:
- (U-cond) sup_V |E^1[F|V] − E^R[F|V]| ≤ δ_c;
- (U-dens) there is a constant c with sup_V |log ρ^1(V) − log ρ^R(V) − c| ≤ δ_d.
Then |E_{μ^1}[F] − E_{μ^R}[F]| ≤ δ_c + (e^{2δ_d} − 1).

**Proof.** Both ρ^G are probability densities, so 1 = ∫ρ^1 ∈ [e^{c−δ_d}, e^{c+δ_d}]·∫ρ^R gives |c| ≤ δ_d and hence
ρ^1/ρ^R ∈ [e^{−2δ_d}, e^{2δ_d}]. Write E_{μ^1}F − E_{μ^R}F = ∫ν^1(E^1[F|V] − E^R[F|V]) + ∫(ρ^1 − ρ^R)h dV with
h := E^R[F|·], |h| ≤ 1. The first term is ≤ δ_c. The second is ≤ ∫|ρ^1/ρ^R − 1| ρ^R |h| ≤ e^{2δ_d} − 1. ∎

**Per-block form.** If log ρ^G = −c^G + Σ_X P^G(X; ·) (sum over connected sets X of coarse blocks) and, for every coarse
block b, Σ_{X∋b} sup_V |P^1(X;V) − P^R(X;V)| ≤ η, then (U-dens) holds with δ_d ≤ N_b η, N_b := number of coarse blocks.
(Σ_X|δP(X)| ≤ Σ_b Σ_{X∋b}|δP(X)|.) So δ_d ≤ (Vol/ℓ_0^4)·η — P4's S2(iii), as an implication.

**What this does and does not use.** Nothing about ν^G enters: not its correlations, not whether the coarse integral is
strongly coupled at distances ≫ ℓ_0, not uniqueness. The only volume dependence is the factor N_b, harmless at fixed
volume. This is the precise sense in which UNIV-T and UNIV-S are ultraviolet: **every input is a statement about the
integration of scales below ℓ_0 with the coarse field held fixed** — but held fixed at EVERY coarse configuration
(sup_V), not only at typical ones (§2.4).

**Well-posedness of sup_V (soft kernel). PROVEN.** Each soft factor obeys k_c ≥ e^{−2κ/g²}: its numerator exponent
1 − N^{-1}Re tr(V_c^{-1}M̄_c) ∈ [0, 2] because ||M̄_c||_op ≤ 1 (lane), and 𝒩 ≤ 1 because its integrand is ≤ 1. Applying this
to the last step only, ρ^G(V) ≥ e^{−2κ_0|E_0|/g_0²} > 0 for EVERY V, where κ_0/g_0² is the last step's kernel coupling.
So E^G[F|V] is defined at every V, and (U-cond), (U-dens) are meaningful as sup-statements.

### 2.2 The exact point where infrared information enters — and why it does not on a fixed volume. PROVEN (identity, example)
- **Identity.** On a box Λ_n (flat route, before n → ∞), put log ρ_s := log ρ^1 + s Σ_X δP(X), s ∈ [0, 1] (normalized).
  Differentiating numerator and normalization (P1 §3's formula): d/ds E_{ρ_s}[h] = Σ_X Cov_{ρ_s}(h, δP(X)). Hence
  |E_{ν^R}h − E_{ν^1}h| ≤ sup_s Σ_X |Cov_{ρ_s}(h, δP(X))|.
- **Fixed volume.** The trivial bound |Cov| ≤ 2||h||·sup|δP(X)| gives 2N_b η — the per-block form above. No decay is used.
- **Volume-uniform version (needed on R^4).** N_b = ∞; a bound uniform in n needs Σ_X sup_s |Cov_{ρ_s}(h, δP(X))| < ∞,
  i.e. summable decay, in dist(X, supp h), of coarse-field covariances, uniformly along the interpolation — information
  about the coarse law at distances ≫ ℓ_0. **That is the first, and on this architecture the only, entry point of IR
  information.** It is weaker than a gap (polynomial decay faster than |x|^{-4} of the uniform covariance suffices) but
  it is a mixing statement for the strongly coupled coarse field (ARGUED: the comparison with P2's TORQUE, which needs
  only the stress channel, is that this condition is stronger; both are IR).
- **Example: per-block smallness is not enough in infinite volume, and is enough at fixed volume. PROVEN.** On
  {±1}^{Λ_n} let ν = (δ_{+} + δ_{−})/2 (all spins +1 or all −1; P1 §2's two-phase mixture) and ν_η ∝ e^{ηΣ_xσ_x}ν: a
  per-site perturbation of size η. Then E_{ν_η}[σ_0] = tanh(η|Λ_n|). At fixed n it is ≤ η|Λ_n| → 0 as η → 0 (the fixed
  volume bound); for any fixed η > 0 it → 1 as n → ∞ (infinite volume: an arbitrarily small extensive perturbation moves a
  local expectation by O(1); here Cov(σ_0, σ_x) = 1 for all x, so the summability condition fails). ∎
- **Consequence for the routes.** On S^4_R (and on T_ℓ) the lemma is applied at fixed volume, so §2.1 suffices. On the
  flat R^4 route, Version Ω (§1.4) is UV, and the passage from Version Ω to R^4 is exactly the summability condition — the
  IR selection that P2 calls TORQUE and P4 calls (I1)-(I3).

(Sign convention in 2.2: δP(X) := P^R(X) − P^1(X), so that ρ_1 ∝ ρ^R; only absolute values are used.)

### 2.3 The common coarse space is what makes the lemma UV (P4's "crux"). ARGUED, with one PROVEN step
- **Without it.** By exact conjugacy (§1.1) the lemma is E_{μ^1}[F] − E_{μ^1}[α_{R^{-1}}F] → 0 inside ONE theory. In grid 1's
  OWN representation (coarse lattice aligned with grid 1) both terms integrate against the same coarse law, so the
  difference is ∫ν^1_own(dV)(h_F − h_{RF})(V), h_F := E^1[F|V] (PROVEN, by the identity of §2.0). For supp F of diameter
  d_F ≫ ℓ_0, h_F and h_{RF} are different functions of ≈ (d_F/ℓ_0)^4 coarse variables, and no symmetry of the coarse
  lattice relates them. The difference is then a statement about how the coarse integral responds to rotating a
  large observable — strongly coupled once d_F·Λ ≳ 1. Nothing in the UV machinery bounds it (ARGUED: I cannot exclude a
  UV argument in this representation, but none is available: it is OS1 restated at the coarse level).
- **With it.** Grid R is brought to grid 1's coarse lattice E_0. Then both expectations integrate DIFFERENT conditional
  data against the SAME kind of coarse integral, and §2.1 removes the coarse integral entirely. All orientation dependence
  now sits in the steps from scale a to ℓ_0. So the common coarse space is not a convenience; it is the step that turns
  the lemma into a UV statement.
- **How grid R reaches E_0, and the constraint on it (ARGUED).** The first RG step on grid R must be misaligned (block a
  rotated grid onto an aligned coarse lattice); the soft kernel allows this exactly (any contour family gives a Markov
  kernel; P4 §8 is right on this). Three options:
  - (a) *Misaligned step with fixed ratio L at the first level.* Grid R's first coarse variable is then a DIFFERENT block
    variable (staircase contours of grid R approximating aligned segments, relative shape error O(1/L)). See 2.4(D): this
    creates an O(1) difference in the marginal direction that a per-step contraction estimate cannot remove.
  - (b) *One step straight from scale a to a fixed fraction of ℓ_0.* Not viable in 4D: its block variable averages fine
    transporters along paths of physical length ~ℓ_0, i.e. ~ℓ_0/a links, whose fluctuations grow like g(a)^2·ℓ_0/a → ∞
    (the linear Wilson-line self-energy [m: standard]); the variable has no continuum limit.
  - (c) *One misaligned step with a slowly diverging ratio r(a): r(a) → ∞ and g(a)^2 r(a) → 0* (possible since
    g(a)^2 ~ 1/(2β_0 log(1/aΛ)) → 0), followed by the common aligned hierarchy. The shape error is O(1/r) and the
    self-energy mismatch is O(g(a)^2 r) [a staircase in direction (3/5, 4/5) has 7/5 times as many links as the straight
    path it replaces, so the two grids' contour self-energies differ by an O(1) FACTOR times g^2 r]. Both → 0. This is the
    option I use in §3. It requires a one-step RG estimate with diverging block ratio (constants at most polynomial in r,
    beaten by powers of g(a)) — new, UV, item (N2) below.

(Precision on 2.3(b)-(c): the soft kernel averages transporter MATRICES, M̄_c = mean of T^σ_y. Transporters along paths of
n links of a rough 4D field deviate from the smooth transport by a random factor with Lie-algebra variance ~ g^2 n, so
the mean is shrunk by ≈ e^{−c g^2 n} [m: linear self-energy of the 4D Wilson line]. For g^2 n ≫ 1, M̄ → 0 and the coarse
variable is kernel noise; for g^2 n → 0 the shrinkage is 1 − O(g^2 n), and the 7/5 path-length mismatch between grids
changes it by O(g^2 n). With S4'-type log-averaging the same regime is the out-of-domain failure of D'.)

### 2.4 Testing P4 S2(ii) — "compactness of SU(N) makes lattice dependence uniformly small over all coarse configurations"

**(A) What compactness gives, and why it is true for SU(N) for a reason P4 does not state. ARGUED.**
- Trivially true (PROVEN): every coarse plaquette angle is bounded, ||log V_p|| ≤ π (eigenphases in (−π, π]).
- Load-bearing form: every coarse configuration admits an interpolating connection with |F| ≤ C_N ℓ_0^{-2} everywhere, so
  every coarse configuration looks smooth at fine scales (curvature ≤ C_N (s/ℓ_0)^2 in units of the scale s).
- Sketch: extend cell by cell. Extending from the boundary of a k-cell meets an obstruction in π_{k−1}(G); π_1(SU(N)) =
  π_2(SU(N)) = 0, so 2- and 3-cells are unobstructed, and a 4-cell is unobstructed because every bundle over S^3 is
  trivial (π_2 = 0). A uniform C_N then follows from compactness of the boundary data, piece by piece (the face-filling
  map is continuous off the eigenvalue −1 branch set, so finitely many closures suffice). Not written as a proof here.
- For U(1) (π_1 = Z) it is FALSE: a coarse 3-cube whose principal face angles sum to 2π forces a Dirac monopole, with
  self-energy ∝ ℓ_0/(g^2 a). For SO(3) = SU(2)/Z_2 (π_1 = Z_2) thin Z_2 vortices play the same role. (Such configurations
  have vanishing probability, so even there the route need not fail; but P4's "compactness" is not the reason.)

**(B) The comparison must hold ON large fields; they cannot be discarded. PROVEN for coarse, lane-cited for fine.**
- *Coarse.* By the lower bound of §2.1, ν^G(A) ≥ e^{−2κ_0|E_0|/g_0^2}·Haar(A) for every Borel set A of coarse
  configurations, uniformly in a. So the set {some coarse plaquette has ||log V_p|| ≥ ε_0} has ν^G-probability bounded
  below by a positive constant independent of a (and its probability tends to 1 as R grows at fixed g_0). BFT
  (REVIEW_S22 `Statement (BFT)`: "max_P|log V^r_{k,P}| ≤ ε ≤ ε_0") does not reach it. ∎
- *Fine.* The lane's E8.3 ("lattice-scale failures are dense", PROOF.md, inequality PROVEN-HERE there, AF reading
  CONDITIONAL on L4a; I did not re-verify it) gives, per link, a conditional probability ≥ h_N(δ)e^{−β(d−1)x^2} of a
  large deviation; at AF couplings β ~ λK this is ≥ L^{−cK}, against L^{4K} links per unit region. So typical
  configurations in a fixed region contain lattice-scale large fields. PLAN_S26 §11 adds (secondary sources) that
  Balaban's thresholds ε_0, ε_1 are FIXED, consistent with this.
- *Consequence.* "The conditional fine integral is a weak-coupling Gaussian around a smooth background" is the right
  picture of the BACKGROUND (A), not of the measure. The per-block comparison has to pass through Balaban's large-field
  machinery (the lane's Theorem RLF / Theorem TS-R1), and in DIFFERENCE form — which no lane item states.

**(C) The most dangerous large coarse fields are UV-safe (topology, small instantons). ARGUED, semiclassical [m].**
- A coarse 4-cell whose boundary data have non-integer Chern-Simons invariant must carry fractional topological charge
  inside. Classically YM is scale invariant, so the charge could sit in a structure of any size ρ ∈ [a, ℓ_0].
- Semiclassical weight: 't Hooft density ∝ ρ^{−5} exp(−8π²/g(ρ)^2) = ρ^{−5}(ρΛ)^{16π²β_0} = ρ^{−5}(ρΛ)^{11N/3}, using
  1/g(ρ)^2 = 2β_0 log(1/ρΛ) and β_0 = 11N/(48π²). Inside a cell of volume ℓ_0^4 the size law is ∝ ρ^{11N/3−5} on
  [a, ℓ_0], and P(ρ ≤ 2a) ≈ (2a/ℓ_0)^{11N/3−4}.
- 11N/3 − 4 > 0 for every N ≥ 2 (10/3 at N = 2). So lattice-scale (grid-dependent) structure carries vanishing weight even
  where the coarse field forces topology: consistent with UV-ness, and a natural nonperturbative exponent θ ≤ 11N/3 − 4
  for any per-block bound. This is the one place where I expected a genuine counterexample to P4 and did not find one.

**(D) The marginal direction — the step P4's sketch omits. ARGUED (the obstruction to a proof technique, not to the lemma).**
- The lane's E7 (PROOF.md L7b, "E7.2 (contraction) ... The marginal direction is fixed by RC", "E7.3 (tuning
  stability)") compares two theories whose marginal parameters are matched by TUNING. In UNIV the bare rule must be
  common: exact conjugacy (§1.1) is what converts UNIV-S into invariance, and separate tuning of grid R would break it.
  So the marginal component of the difference of the two common-representation effective actions is NOT removed by
  tuning, and an E7.2-type contraction does not touch it (marginal = eigenvalue 1, up to logarithms).
- With option 2.3(a) (fixed-ratio misaligned first step) the two grids use different blocking schemes at the first level,
  and the scheme constant c in g_eff^{-2} = 2β_0 log(1/sΛ) + c differs between them by O(1) at one loop: an O(1)
  marginal difference at scale La. Physically it is redundant (a change of variables): at tree level the first-step
  kernel enters the law of the ℓ_0 variable only through ζ̂_first(p·La) = 1 + O((La/ℓ_0)^2) at p ~ 1/ℓ_0, so the ℓ_0 law
  is insensitive to it, and the O(1) marginal difference must be cancelled by feedback from the O(1) irrelevant
  differences. But a coupling-plus-polymer induction sees a preserved marginal difference plus contracting irrelevant
  ones; proving the cancellation is a new nonperturbative statement ("first-step redundancy", N3-red).
- With option 2.3(c) (ratio r(a) → ∞, g(a)^2 r(a) → 0) every component of the first-step difference is
  O(1/r) + O(g(a)^2 r) → 0, including the marginal one. Thereafter the coupling flow preserves a marginal difference up to a
  bounded factor: with μ d(g^{-2})/dμ = 2β_0 + 2β_1 g^2 + O(g^4), a perturbation δ of g^{-2} obeys dδ/dlog μ = O(g^4)δ,
  and ∫ g^4 dlog μ < ∞ along an AF trajectory (g^2 ≈ 1/(2β_0 log(μ/Λ))). So option (c) trades N3-red for N2.
- A partial alternative pin, on S^4_R only: the whole-sphere flowed energy ∫_{S^4_R} E(t_0) has EXACTLY equal expectations
  under 𝒦 and g𝒦 (conjugacy plus g-invariance of the integral). It fixes one linear functional of the marginal
  difference, not the difference itself (with P4's position-dependent coupling the marginal parameter is a function on
  S^4). On T_ℓ even this fails (grid R on T_ℓ is grid 1 on an isometric but differently oriented torus).

**(E) The rate. ARGUED.** P4 writes O((a/ℓ_0)^θ) per block. Physically (Symanzik) an O(a^2)-type rate up to logarithms is
expected, and (C) gives θ ≤ 11N/3 − 4 from lattice-scale topology. But the only route to a common coarse space that I can
make work (2.3(c)) delivers per-block errors O(1/r + g(a)^2 r) ≥ 2g(a)·O(1), i.e. a LOGARITHMIC rate ~ (log 1/a)^{−1/2}.
Irrelevant: the lemma is in difference form and needs no rate at fixed volume. But any later use that multiplies the
per-block error by a growing volume (e.g. letting R grow with a) would need the rate, and this architecture does not give
a power.

### 2.5 Verdict on U2

**The lemma is ultraviolet at fixed volume. No infrared input enters UNIV-T or UNIV-S.**
- PROVEN as an implication (§2.1): with the common coarse space, the coarse integral at ℓ_0 — however strongly coupled —
  drops out; only sup-over-coarse-configurations comparisons of the integration of scales below ℓ_0 remain, times the
  fixed number of coarse blocks.
- The step where IR information WOULD enter is identified exactly (§2.2): removing the volume factor, which the flat route
  must do and the sphere route at fixed R need not. The two-phase example shows it cannot be removed without decay.
- P4's least-sure step survives, but **P4's stated mechanism is not the right one**: compactness gives smooth BACKGROUNDS
  for every coarse configuration (true for SU(N) by π_1 = π_2 = 0, not by compactness alone), but the comparison must be
  uniform over large-field sets of non-vanishing probability (coarse, PROVEN) and probability → 1 (fine, lane E8.3), and
  must handle the marginal direction, which no contraction estimate touches. Those are UV, but they are not BFT, not E7
  as stated, and not consequences of compactness. P4 S2(ii) as written is therefore NOT-VERIFIED (and its rate claim is
  not delivered by any architecture I can make work).
- **If S2 needed IR, route 1 would collapse to route 2 (P4 §7).** It does not; the sphere route keeps its claimed
  advantage on this point. Its remaining costs are elsewhere (H1, H3, S4, S5's volume-uniform local bounds).

---

## 3. What can be proved, and on what (U3)

### 3.1 Theorem U (CONDITIONAL). UNIV-T, and UNIV-S at each fixed R, hold given the inputs below.
Inputs. Notation: common hierarchy = soft-kernel RG on the common (aligned) coarse lattices from scale s_1 := r(a)·a to ℓ_0,
n(a) = log_L(ℓ_0/s_1) levels; at level j the difference of the two grids' effective densities is split into a marginal
part m_j (difference of the effective g^{-2}) and an irrelevant part d_j (polymer-norm difference of the remainders),
each measured per block and uniformly over all field configurations at that level.
- **Layer-1 (named).**
  - (L1-BFT) REVIEW_S22 `Statement (BFT)`, clauses 0-5, for each level of the common hierarchy (small-field part).
  - (L1-LF) the large-field R-operation bounds: PROOF.md "Theorem RLF (the target the R-operation must deliver, soft
    kernel, all quantifiers ...) ... stays OPEN inside L5"; and the lane's Theorem TS / R1 large-field gas.
  - (L1-FLOW) the effective coupling stays ≤ γ at every scale in [a, ℓ_0] along the common bare rule (the hypothesis on
    which, per PLAN_S26 §11, Balaban's CMP 122 II is conditional; the lane's FLOW and the running FLOW55).
- **New, all ultraviolet (none is in the lane).**
  - **(N1) Two-theory contraction through large fields.** One common soft step maps (m_j, d_j) to
    d_{j+1} ≤ L^{−κ}d_j + C g_j^p m_j and m_{j+1} ≤ (1 + C g_j^4) m_j + C d_j, with κ, p > 0 and C uniform in j and in
    the configuration, INCLUDING large-field regions (Balaban's R-operation in difference form, with localization of the
    large-field polymers' dependence on the coarser field). This is the lane's E7.2 ("including across the
    large-field/small-field interface") restated for two theories, with the marginal part tracked instead of tuned.
  - **(N2) The misaligned first step.** One soft RG step of block ratio r(a) → ∞ with g(a)^2 r(a) → 0, from grid G
    (G = 1 aligned, G = R misaligned) onto the common lattice at s_1, with Balaban-type bounds whose constants grow at most
    polynomially in r, giving m_{s_1}, d_{s_1} = O(1/r + g(a)^2 r) → 0 (§2.3(c), §2.4(D)).
  - **(N3) The last levels at large coarse fields.** The sup over ALL coarse configurations at ℓ_0 (§2.4(B)) requires
    (N1) to hold where the induced background has own-unit curvature up to C_N (§2.4(A)) — the last j_0 levels below ℓ_0,
    with L^{2j_0} ≥ 2C_N/ε_0. Either BFT extended to backgrounds of bounded but not small curvature (needs the constrained
    Hessian positive there: κ large against C_N), or the large-field form of (N1) covering them.
  - **(N4) Observable comparison (U-cond).** sup_V |E^1[F|V] − E^R[F|V]| → 0 for F ∈ 𝒜_flow: a source-inserted version of
    (N1)-(N3), plus convergence of the two lattice gradient flows at fixed physical flow time (part of the lane's
    γ2/H5 obligation; P4 H5).
- **For UNIV-S additionally** (P4 S4): the inputs above with a slowly varying bare coupling g_0(x) and across the seam;
  dilations between charts enter (N2) as a second misalignment (scale), handled identically.

**Proof (from the inputs).** Iterate (N1) from level s_1 (where (N2) gives m, d = o(1)) to ℓ_0. Then
d_j ≤ L^{−κ(j)}d_{s_1} + C Σ_{i<j} L^{−κ(j−i−1)} g_i^p m_i, and m_j ≤ exp(C Σ_i g_i^4)(m_{s_1} + C Σ_{i<j} d_i). Since
Σ_i g_i^4 < ∞ on an AF trajectory and Σ_i d_i ≤ C'(d_{s_1} + sup_i m_i), a Gronwall step gives sup_j (m_j + d_j) ≤
C''(m_{s_1} + d_{s_1}) = o(1), uniformly in a, for C·C'·e^{CΣg^4} < 1 or, in general, after absorbing the finitely many
early levels where g_i is not yet small into the constant. [The absorption needs C' < ∞ independent of n(a); it is the
quantitative content of (N1), not proved here.] At ℓ_0 the per-block bound η = o(1) holds uniformly over all coarse
configurations by (N3). Hence (U-dens) with δ_d ≤ N_b·o(1), and (U-cond) by (N4); Proposition T gives Δ_a(F) → 0. ∎

**What the proof does NOT use.** E7 (convergence of the whole sequence); a renormalization condition or separate tuning;
uniqueness, clustering, decay of coarse correlations, or a mass gap; constants uniform in the volume; chessboard
(FILS) estimates. The last point matters for P4's H3: UNIV itself uses only action-based large-field bounds (L1-LF), so
it is not a source of extra cost on the sphere.

### 3.2 The first point where information beyond the named layer-1 inputs enters
In proof order:
1. **The common coarse space itself (N2).** BFT and RLF are stated for one hypercubic hierarchy ("every torus whose
   level-k side is ≥ T_0 (and every non-wrapping box ...)"); a misaligned step, and a step of diverging ratio, are
   outside them. This is P4's flagged crux, and it is a UV construction problem.
2. **sup over large coarse fields (N3).** BFT's domain is max_P|log V| ≤ ε_0; the comparison must hold on a set of
   coarse probability bounded below (PROVEN, §2.4(B)).
3. **The marginal direction (N1's m-equation).** The lane's E7 fixes it by tuning, which UNIV may not do.
None of the three involves scales above ℓ_0, so **no infrared information enters at fixed volume.** On R^4 the first IR
entry is the volume factor (§2.2).

### 3.3 Status of what is claimed here
- PROVEN here: §1.1 (trivial/ill-posed readings), the periodicity of Λ^R_a on T_ℓ and the group lemma (1.2 + erratum),
  Proposition T and its per-block form, the soft-kernel lower bound and its consequence §2.4(B)-coarse, the identity and
  two-phase example of §2.2, the implication "inputs ⇒ UNIV" in 3.1 up to the bracketed quantitative point.
- ARGUED: §2.3 (necessity of a common coarse space; options (a)-(c)), §2.4(A) (uniform interpolation for SU(N)),
  §2.4(C) (semiclassical exponent 11N/3 − 4), §2.4(D) (marginal redundancy; flow-preservation), §2.4(E).
- OPEN: (N1)-(N4), and every layer-1 input.

**Correction to the proof in 3.1 (written immediately after; the bracketed step made precise).** Index the common
hierarchy from fine (j = 0 at s_1) to coarse (j = n at ℓ_0); along the AF trajectory g_j^2 ≈ (g_0^{-2} + 2β_0(n−j)log L)^{-1},
so g grows toward ℓ_0 and is largest (= g_0) there. Write λ := L^{−κ} and M_j := max_{i≤j} m_i. From (N1),
d_j ≤ λ^j d_0 + C Σ_{i<j} λ^{j−1−i} g_i^p m_i ≤ λ^j d_0 + (C/(1−λ))·max_{i<j}(g_i^p)·M_j, and
m_{j+1} ≤ e^{C S_4}[m_0 + C Σ_{i≤j} d_i], S_4 := Σ_i g_i^4. Summing the d-bound over i ≤ j:
Σ_i d_i ≤ d_0/(1−λ) + (C/(1−λ)) M_j Σ_i g_i^p. Hence M_{j+1} ≤ e^{CS_4}[m_0 + C d_0/(1−λ)] + G·M_{j+1}, with loop gain
G := (C^2/(1−λ)) e^{CS_4} Σ_i g_i^p. **This needs p > 2**: then Σ_{k≥0}(g_0^{-2} + 2β_0 k log L)^{−p/2} ≤ g_0^p + g_0^{p−2}/((p−2)β_0 log L)
uniformly in n, and S_4 ≤ g_0^4 + g_0^2/(2β_0 log L). For g_0 small, G ≤ 1/2, so sup_j m_j ≤ 2e^{CS_4}(m_0 + Cd_0/(1−λ)) and
sup_j d_j ≤ d_0 + (C/(1−λ))g_0^p sup m — both O(m_0 + d_0) = o(1), uniformly in a. (p = 4 is what one expects: a shift of
g^{-2} moves the O(g^2) irrelevant remainder by O(g^4).) So (N1) must be stated with p > 2; with p ≤ 2 the marginal-to-
irrelevant feedback is not summable along an AF trajectory and the argument fails.

---

## 4. Gantumur, arXiv:2512.22072 (U4). Read-only, via WebFetch summaries of the arXiv abstract pages (v2, v3) and the v2 HTML

**Bibliographic facts (as returned by the fetch; the lead may want to re-verify).** v1 26 Dec 2025; v2 13 Jan 2026 ("minor
revision focused mostly on presentation", 49 pp.); v3 5 Jul 2026, whose comments field reads, per the fetch, "Published
version ... JHEP 07 (2026) 036". PLAN_S26 §10 says this JHEP citation "could not be confirmed"; the arXiv v3 metadata is
where it comes from. I assessed v2 as asked; per the fetch, v3's abstract makes the same claims.

**What it does (paraphrase).** A fixed abstract hypercubic graph; the embedding x: Λ → R^d of its sites is a dynamical field
integrated with flat measure over an admissible set (edge lengths ≤ C_ℓ a, oriented cell volumes ≥ c_V a^d, the connected
component of the regular embedding); gauge links and matter on the abstract graph; all actions depend on x only through
Euclidean invariants (Gram matrices, volumes), and are averaged with their index-time reflection.

**Its theorems and their exact scope (from the v2 text, via the fetch).**
- Reflection positivity (its Theorem 4.3, bosonic sector; Lemma 4.1 for invariance of the admissible set) on a FINITE
  cylinder Λ_{T,L} (open in index time, periodic in space), for the INDEX-time reflection n_1 ↦ 1 − n_1, for functionals
  of (x, U, φ) supported in the index half Λ_+. Nothing requires the embedded positions x(n) of index-positive sites to
  lie in the physical half-space. Fermions: a separate Theorem 4.5 with an extra slab-positivity hypothesis.
- Exact global SE(d) covariance of the partition function at every spacing (on Z^d, where the paper says the partition
  function is formal; the periodic finite-volume version is not rotation covariant).
- Universality is NOT proved: it is Conjecture 4.9, conditional on the short-range-geometry Hypothesis 4.7 (SR), which is
  assumed, to be checked per geometry action; the d = 4 one-loop check is scalar φ⁴ only; no gauge-theory continuum
  analysis; numerics d = 2 scalar only.

**Limitations the author states (paraphrase).** (SR) is an assumption; whether the d = 4 geometry stays short-range is
unmapped (crumpling or crystallisation possible; a stiffness term likely needed); universality is a conjecture; the
one-loop check is for a scalar test theory; the simulations are a d = 2 scalar proof of concept; fermion doubling is not
removed; the admissible set breaks improper motions (expected harmless, unproved); local constraints do not exclude
global self-intersection; topological freezing in gauge theories is left to future work.

**Assessment. ARGUED.**
- **It does not help prove UNIV.** UNIV compares two FIXED lattices. Gantumur replaces the lattice by a coupled
  (embedding + gauge) system; the counterpart of UNIV for it is (SR) + Conjecture 4.9, a UV universality statement for a
  system with a new field sector and no constructive theory at all. It is not a tool for UNIV.
- **It is not by itself an alternative route to OS1 on R^4.** Two gaps remain. (a) *Support identification:* its RP is for
  index-supported observables; OS2 needs physically supported ones, and x(n) fluctuates across the physical plane, so
  the transfer needs control of embedding fluctuations near the reflection plane (P3 §3 flagged the same). (b) *IR
  selection:* exact SE(d) covariance holds for the infinite-volume specification; the RP finite volumes (spatially
  periodic) break it. By P4's Lemma B, a covariant local rule plus RP and translations does not force a rotation-invariant
  selected state. So on R^4 it removes the UV half of the flat-route problem (if (SR)/Conj. 4.9 hold) and leaves the IR
  half untouched.
- **On the sphere route it is a conceivable, more expensive, substitute for UNIV-S.** A dynamical embedding of a fixed
  reflection-symmetric abstract cellulation of S^4 into S^4_R, with an SO(5)-invariant geometry measure, would make SO(5)
  invariance EXACT at every cutoff (the joint law is invariant under g acting on embeddings), so S2 would not be needed.
  The price: (SR)/Conjecture 4.9 on S^4 for a gauge theory, plus the support identification (a), plus the large-field
  and flow programme for a coupled system. Since UNIV-S is already UV (§2.5), this buys nothing on the IR side and costs
  more on the UV side. I would not switch.
- **A question for anyone building on it (my concern, not the paper's).** In the regime where the embedding stays close
  to a regular grid at large scales (an elastic "solid"), the global SE(d) of the target is spontaneously broken and
  long-wavelength strain (phonon) modes are gapless: for a harmonic elastic action, strain correlations decay like
  |n|^{−d}, a power law, whereas (SR) asks for a finite correlation length after quotienting the GLOBAL modes (which removes
  only wave-number zero). The fetched text does not discuss Goldstone or phonon modes. By power counting the leading
  phonon coupling ∂u·T_{μν} has dimension 6 in d = 4 (∂u dimension 2, T dimension 4), so universality may survive without
  (SR); but then the paper's Symanzik argument, which assumes (SR), would need replacing. Unverified; the stiff-geometry
  limit or the actual d = 4 phase structure may settle it either way.
- **Consistency with P4's Lemma C.** Gantumur's regulator has discrete index time, so it sits in the loophole Lemma C leaves
  (lattice-like, not smooth); no conflict.

### 3.4 A second architecture, available for UNIV-S only: the global Ward identity on S^4_R. ARGUED
(Written after reading ROTDEF.md §1 — the flat-torus version of the identity — and CODEX_REVIEW_P4.md; see §6.)
- **Identity (PROVEN, one line).** For any smooth vector field Ξ on the compact configuration space (a product of SU(N)'s)
  with Haar measure, integration by parts gives ω(ΞF) = Cov_ω(F, 𝔚), 𝔚 := ΞS − div Ξ (and ω(𝔚) = ω(Ξ1) = 0).
- **On S^4_R take Ξ = the gauge-covariant lattice Lie derivative along a GLOBAL Killing field v of SO(5).** No radial cutoff
  is needed, so ROTDEF's boundary-flux term — its IR term TQ_ν — does not exist. Then
  E_𝒦[O] − E_{g𝒦}[O] = −∫_0^1 (d/ds)E_𝒦[g_s^{-1}O] ds, and d/ds E_𝒦[g_s^{-1}O] = Cov(g_s^{-1}O, 𝔚) + (observable-side
  error: the lattice flow and interpolation do not commute exactly with Ξ; O(a²/t)-type, UV).
- **Fixed-R bound, no decay.** |Cov(O, 𝔚)| ≤ Σ_x |Cov(O, 𝔚_x)| ≤ N_sites·sup_x|Cov(O, 𝔚_x)|, i.e. the volume times a local
  sup. No clustering, no coarse-law covariance, no CD-type input (ROTDEF needed CD only for torus-uniformity).
- **What it avoids.** It differentiates inside ONE theory along an exact symmetry of the geometry, so it needs NO common
  coarse space (N2) and no first-step redundancy (N3-red). The marginal direction reappears only as the local
  Λ-matching of P4's coupling profile (below), which is part of the coupling-flow programme.
- **What it needs (all UV, none in the lane):**
  - (W0) A selection-rule analysis of 𝔚_x in each chart for ALL components of the conformal Killing field there (rotation,
    translation, dilation, special conformal), not only rotations. ROTDEF's rule (no dimension-4 gauge-invariant operator
    in the rotation-generator representation of H(4); dimension 5 excluded by inversion) covers the rotation component;
    the dilation component gives a dimension-4 insertion ∝ (div v)·tr F² whose coefficient vanishes only to the extent
    that the coupling profile makes the local Λ uniform — O(g_0(a)^2) by P4's two-loop rule, if the lattice Λ-parameter
    has two-loop asymptotics nonperturbatively (Λ-matching; L1-FLOW).
  - (W1) Source-inserted local bounds sup_x|Cov(O, 𝔚^{ren}_x)| ≤ C(O) uniformly in a (renormalized insertions; for O in
    𝒜_flow the flow smoothing removes contact singularities, as in ROTDEF's observable choice).
  - (W2) Seam transparency in Ward form: the seam's contribution to 𝔚 must obey the same bound. By CODEX_REVIEW_P4 §1.2
    (β_p ≡ 0 decouples the hemispheres) this is FALSE for some admissible seams; it needs a tuned seam (§6).
  - (W3) Observable side: lattice flow + interpolation commute with Ξ up to o(1).
- **Not available for UNIV-T**: rotations are not isometries of a flat torus, so there is no Killing field to integrate;
  UNIV-T needs the common-coarse-space architecture of 3.1.
- **Normalization (precision on the fixed-R bound).** In physical units 𝔚 = Σ_x a^4 [a^2 c_6 O_6(x) + c_4(x) tr F^2(x) + seam
  terms], with c_4 = O(g_0(a)^2)·(div v) by (W0). So |Cov(O, 𝔚)| ≤ Vol(S^4_R)·[a^2|c_6| sup_x|Cov(O, O^{ren}_6(x))| +
  sup|c_4| sup_x|Cov(O, tr F^2_{ren}(x))|] + seam: → 0 at fixed R (the first term like a^2, up to logarithms; the second
  only like g_0(a)^2 ~ 1/log(1/a)), provided (W1) bounds both sups uniformly in a. (W1) is a statement about the full
  measure, but it is a one-point local bound times ||O||, not a decay estimate.
- **Correction to the last sentence (written at once).** "(W1) is a one-point local bound times ||O||" is wrong for point
  composites: E|O_6(x)| on the lattice grows like a^{-6}, so 2||O||·E|O_6(x)| is useless. The correct form: condition on the
  coarse field V at ℓ_0 (§2.0), Cov(O, O_6(x)) = E[Cov(O, O_6(x) | V)] + Cov(E[O|V], E[O_6(x)|V]). The second term is
  ≤ 2||O||·sup_V|E[O^{ren}_6(x)|V]| (a conditional one-point bound: for every coarse V the coarse curvature is
  ≤ C_N ℓ_0^{-2} by §2.4(A), so this is O(ℓ_0^{-6}) if the conditional renormalized insertion is controlled — UV). The
  first is a conditional covariance, which decays in dist(x, supp O)/ℓ_0 by the constraint-induced locality of the
  conditional fine measure (UV, BFT-3-type) and near supp O is a contact estimate between a flowed observable and the
  insertion. All three pieces are UV and need no decay of the coarse law; but they are three estimates, not one.

---

## 5. Verdicts on the P4 claims this target tests (locating strings in PANEL_P4.md)

- **V1. "Since E_{g𝒦}[O] = E_𝒦[g^{-1}·O] exactly" — CONFIRMED.** Transport of structure, when ALL decorations (poles,
  seam, coupling profile, observable maps) are transported (§1.1). Same verdict and same proviso as CODEX_REVIEW_P4 §2.1.
- **V2. "E7-type convergence is not needed" (difference form suffices) — CONFIRMED** as an implication (§1.2 consequence;
  §1.3), given covariant observable maps and equicontinuity under SO(5) for the extension from G_0 to SO(5).
- **V3. S2(i) "its law is a density on a compact finite-dimensional space" — CONFIRMED** for the soft kernel, with more:
  the density is bounded below by e^{−2κ_0|E_0|/g_0^2} everywhere (§2.1), so conditional expectations exist at every V.
- **V4a. S2(ii), first half: "Compactness of SU(N) bounds the coarse curvature by O(ℓ_0^{-2}) for EVERY coarse
  configuration" — CONFIRMED for plaquette angles (trivial); ARGUED-true for the load-bearing smooth-interpolation form,
  for a topological reason (π_1 = π_2 = 0 of SU(N)) P4 does not give; false for U(1) and SO(3) (§2.4(A)).**
- **V4b. S2(ii), second half: "So the grid dependence of the conditional fine-field integrals is a weak-coupling lattice
  artefact, O((a/ℓ_0)^θ) per block" — NOT-VERIFIED; the inference is invalid.** It needs the comparison on large-field
  sets of non-vanishing coarse probability (PROVEN, §2.4(B)) and of probability → 1 at fine scales (lane E8.3), the
  marginal direction (§2.4(D)), and a common coarse space (§2.3). None follows from compactness. The rate is not
  delivered by any architecture I can make work (§2.4(E)). Agrees with CODEX_REVIEW_P4 §3.1.
- **V5. S2(iii) "The summed error is O((R/ℓ_0)^4 (a/ℓ_0)^θ) → 0 at fixed R. No decay of correlations is used." —
  CONFIRMED as an implication** (Proposition T, per-block form), given SUP-over-coarse-configurations per-block bounds; the
  displayed rate NOT-VERIFIED.
- **V6. "S2 ... OPEN, UV-type (ARGUED)" and §7 "Least sure of. That S2 ... is genuinely UV" — CONFIRMED as a reduction:**
  S2 ⇐ (U-cond) + (U-dens) in sup form (PROVEN), and those concern only the integration of scales below ℓ_0 with the
  coarse field held fixed; no IR input appears at fixed R. **NOT-VERIFIED that the sup-form inputs hold.** If only
  small-field or averaged comparisons can be proved, the coarse law re-enters through Cov(·, δP) (§2.2) — the same
  caveat as CODEX_REVIEW_P4 §3.2.
- **V7. §8 "A smooth blocking kernel can block a ROTATED fine grid onto an axis-aligned coarse grid, which gives the
  common coarse variables that S2 needs" — CONFIRMED representationally (exact Markov kernel), INCOMPLETE as a proof
  device:** a fixed-ratio misaligned step is a scheme change with an O(1) marginal component that contraction does not
  remove; a step of ratio r(a) → ∞ with g(a)^2 r(a) → 0 works (ARGUED); a single step to ~ℓ_0 fails (self-energy). The
  claim that Balaban's hard constraint "does not do this naturally" was only spot-checked (plausible).
- **V8. §9.3 "It does not hit S2: S2 compares the LAWS of coarse variables blocked onto a common grid" — CONFIRMED.**
  Proposition T is a statement about laws and conditional expectations, never pathwise.
- **V9. §9.2 "P1's a^η∫Cov is bounded by a^η·Vol(S^4_R)·sup|Cov| → 0 with no volume uniformity needed" — NOT-VERIFIED as
  written; correct in structure.** With bare point insertions sup|Cov| need not be bounded (E|O_6| ~ a^{-6}); the
  dilation component of a Killing field in a stereographic chart contributes a dimension-4 insertion with coefficient
  O(g_0(a)^2), not a^η; and the seam contributes. Corrected form: §3.4 and its correction. Agrees with CODEX_REVIEW_P4 §3.2.
- **V10. Remark D (Jordan) "An increasing union of finite subgroups of SO(5) is never dense" — CONFIRMED** (spot-check,
  re-derived): a Hausdorff sub-limit of the index-≤J(5) abelian normal subgroups is a closed abelian subgroup of finite
  index in the Hausdorff limit SO(5), hence contains the identity component, contradiction. Jordan's theorem itself [m].
- **V11. §5.2 "f(g_0(x)) = aΛ_phys Ω(x)/C_W ... corrections are O(g_0²) → 0" — NOT-VERIFIED** beyond the perturbative
  reading: it is the Λ-matching that UNIV-S needs for its dilation part (§3.4 (W0)); it presupposes nonperturbative
  two-loop asymptotics of the lattice Λ-parameter (L1-FLOW). Agrees with CODEX_REVIEW_P4 §2.3.
- **V12. S4(b) seam "irrelevant by the same counting" with "Weights β_p ≥ 0 on the crossing plaquettes" — REFUTED as an
  implication (CODEX_REVIEW_P4 §1.2's counterexample, re-derived here):** with β_p = 0 every crossing plaquette has
  weight 1, so the crossing links are free Haar variables in no weighted plaquette, and e^{-S} = e^{-S_-}e^{-S_+}: the
  two hemispheres are independent at every cutoff. Rotating the seam through two nearby observables then changes their
  connected correlation from 0 to its bulk value, so UNIV-S is FALSE for that admissible seam. **Correction to my §1.3:**
  UNIV-S must specify a seam prescription and is CONDITIONAL on seam transparency (an additional UV input, N5).
- (Proviso to V12, written at once: "FALSE" needs the hemisphere limit to have SOME nonzero connected correlation between
  two nearby gauge-invariant observables, which holds for any limit that is not ultralocal — in particular for any
  non-free limit, and for free Maxwell.)

---

## 6. Comparison with CODEX_REVIEW_P4.md and ROTDEF.md (both read only after §1-§4 and §3.1-§3.3 were written)

**CODEX_REVIEW_P4.md (Codex; as on disk now; its last section "## 8. Ranking and the single most likely failure" ends
with complete sentences — it looks finished).**
- **Agree: §2.1 transport identity, §2.2 difference form suffices** (my V1, V2).
- **Agree, independently derived: §3.2 "A sufficient comparison that really avoids IR decay".** Its displayed estimate
  (sup_V|log(q̃_a/q_a) − c_a| ≤ δ, sup_V|õ_a − o_a| ≤ ε ⇒ |ω̃ − ω| ≤ ε + ||o||(e^{2δ} − 1)) is my Proposition T, written
  before I opened the file. Two families reached the same mechanism.
- **Agree: §3.1** (compactness does not yield S2(ii); its {0,1} example shows conditional agreement alone does not give
  state agreement — which is why Proposition T has two hypotheses). **I add** three things it does not have: a PROOF that
  the large-field coarse set has probability bounded below uniformly in a (so the sup must cover it; §2.4(B)); the
  marginal-direction obstruction to an E7-type proof (§2.4(D)); and evidence that the sup-form is nevertheless plausible
  for SU(N) (smooth interpolation by π_1 = π_2 = 0; small-instanton weight (a/ℓ_0)^{11N/3−4}; §2.4(A), (C)).
- **Partial disagreement, about words more than substance: "Fixed volume is not a synonym for ultraviolet".** Codex: "That
  is the entry point for information from scales ℓ_0 through R: the normalized coarse law ...". I agree this is where such
  information WOULD enter, and that it enters if only averaged or small-field comparisons are available. I disagree that
  it must enter: with the sup-form inputs it provably does not (Proposition T), and the sup-form inputs are statements
  about the conditional integral of scales below ℓ_0 at a fixed coarse field — UV by construction, though unproved.
  Codex itself says the same conditionally ("A uniform conditional UV comparison could avoid an additional IR decay
  theorem"). So: the classification "UV" is CONFIRMED as a reduction; the inputs are NOT-VERIFIED. That is my V6.
- **Agree, re-derived: §1.2 seam counterexample** (β_p ≡ 0 factorizes; my V12), and its conclusion that seam transparency
  belongs inside S2. My §1.3 statement of UNIV-S is corrected accordingly (N5).
- **Agree: §2.3** (the coupling rule is an asymptotic proposal; my V11). Its Weyl-anomaly remark bears on the dilation
  component of my §3.4 (W0): the c-number anomaly terms cancel in normalized expectations; the operator part is the
  Λ-matching, which is what (W0) requires.
- **Agree: §8's ranking caution** in the narrow sense that the sphere route's superiority is not proved. My contribution to
  that question: the specific fear that S2 secretly needs IR (P4 §7: "If S2 secretly needs IR input, route 1 collapses to
  route 2") is answered NO at the level of logical structure; the sphere route's remaining risks are UV (N1-N5 or W0-W3)
  plus H1, H3 and S5's radius-uniform local bounds.

**ROTDEF.md (Opus 5.5, flat torus; read §1 only; not reviewed).** Consistent with this file: its only IR term, TQ_ν, is the
coarse-law covariance with the angular-momentum flux through the cutoff shell of a radially cut-off rotation field. On
S^4_R the rotation field is a global Killing field, no cutoff is needed, and that term does not exist (§3.4) — the precise
form of P4's "b ≡ 0". Its observable-side mixing is O(g_bare^2), i.e. logarithmic in a, matching my §2.4(E) remark that
these architectures give logarithmic rates. I did not check its selection-rule computation (its `checks/rd55_*`), which
my (W0) cites for the rotation component only.

**Re-check of my own PROVEN items before the table (2026-10-28, after §6).**
- Soft-kernel lower bound (§2.1): the bracket 1 − N^{-1}Re tr(V^{-1}M̄) lies in [0, 2] because |N^{-1}tr(V^{-1}M̄)| ≤
  ||V^{-1}M̄||_op ≤ 1; 𝒩 ≤ 1 because its integrand is ≤ 1 under Haar probability. ✓
- §2.4(B) "probability → 1 as R grows" — made precise: given U the kernel factorizes over coarse links, each with density
  ≥ e^{−2κ_0/g_0^2}; so for m coarse plaquettes with disjoint link sets the events {||log V_p|| ≥ ε_0} are conditionally
  independent with probability ≥ q := e^{−8κ_0/g_0^2}·Haar{W : ||log W|| ≥ ε_0} > 0 each (a product of independent Haar
  variables is Haar), so P(none) ≤ (1 − q)^m, and m ≍ (R/ℓ_0)^4. ✓ PROVEN.
- §3.1 implication: valid with p > 2 (correction above). ✓ — V12 factorization ✓ — group lemma ✓ — Prop T ✓.

---

## 7. Summary table (every claim in this file)

| # | Claim | Label / verdict | Where |
|---|---|---|---|
| U1a | Rotating volume + lattice together is exact conjugacy; the lemma must fix the volume or the observable | PROVEN | §1.1 |
| U1b | "Two lattices in a bounded region with boundary" contains a second (boundary) universality | PROVEN (as a structural remark) | §1.1 |
| U1c | Λ^R_a is periodic on T_ℓ for rational R, a ∈ A_R; one Pythagorean rotation + H_4 is dense in O(4) | PROVEN (Niven [m]) | §1.2 + erratum |
| U1d | Precise statements UNIV-T, UNIV-S (with seam prescription: N5), UNIV-Ω; observable class 𝒜_flow; common bare rule; difference-form convergence | statements | §1.2-1.4, V12 |
| U2a | Proposition T (sup-form conditional comparisons ⇒ state comparison; coarse integral drops out) | PROVEN | §2.1 |
| U2b | Soft-kernel coarse density ≥ e^{−2κ_0|E_0|/g_0^2}; large-field coarse set has probability ≥ c > 0 uniformly in a, → 1 as R grows | PROVEN | §2.1, §2.4(B), §6 re-check |
| U2c | Interpolation identity; IR enters exactly when the volume factor must be removed; two-phase example | PROVEN | §2.2 |
| U2d | The common coarse space is what makes the lemma UV | ARGUED | §2.3 |
| U2e | Fixed-ratio misaligned step: O(1) marginal scheme difference; one step to ~ℓ_0 fails (self-energy); ratio r(a) → ∞, g^2 r → 0 works | ARGUED | §2.3, §2.4(D) |
| U2f | Uniform smooth interpolation for SU(N) (π_1 = π_2 = 0); false for U(1), SO(3) | ARGUED | §2.4(A) |
| U2g | Topologically forced small structure has weight (a/ℓ_0)^{11N/3−4}, exponent > 0 for N ≥ 2 | ARGUED [m: 't Hooft] | §2.4(C) |
| U2h | Architectures available give logarithmic, not power, rates | ARGUED | §2.4(E) |
| U2i | **Verdict: no IR input enters UNIV-T / UNIV-S at fixed volume; P4's mechanism is not the right one** | reduction PROVEN; inputs OPEN | §2.5 |
| U3a | Theorem U: (L1-BFT, L1-LF, L1-FLOW) + (N1 with p > 2, N2, N3, N4) [+ N5 for UNIV-S] ⇒ UNIV | CONDITIONAL (implication PROVEN) | §3.1 + correction |
| U3b | First points beyond layer-1: common coarse space; sup over large coarse fields; marginal direction — none IR | ARGUED | §3.2 |
| U3c | Ward identity ω(ΞF) = Cov(F, ΞS − div Ξ) | PROVEN | §3.4 |
| U3d | Global-Killing-field architecture for UNIV-S: no flux term, no common coarse space; needs W0-W3 + N5 | ARGUED | §3.4 + corrections |
| U4 | Gantumur: does not help prove UNIV; not alone an OS1 route on R^4 (support identification, IR selection); on S^4 a costlier substitute; (SR) vs Goldstone question | ARGUED | §4 |
| V1-V12 | P4 claims: 8 CONFIRMED (V1, V2, V3, V5, V6, V7, V8, V10), 4 NOT-VERIFIED (V4a load-bearing form, V4b, V9, V11), 1 REFUTED (V12, as implication) | as listed | §5 |

---

## 8. Symbol disambiguation (REVIEW_BRIEF_55 defect 1, applied to this file; overrides earlier usage)
- **κ.** κ_0 (§2.1, §2.4(B)) = the soft-kernel constraint strength of the LAST RG level (PROOF.md "Decision 4: the RG
  kernel", k_c with κ/g²). The contraction exponent in (N1) and in §3.1's correction ("λ := L^{−κ}") is a DIFFERENT
  object: read it as κ_E, the irrelevant-direction exponent of the lane's E7 ("There are κ > 0 and C < ∞ ..."). They are
  unrelated numbers.
- **m.** In §3.1 and its correction, m_j / m_0 denote the MARGINAL DIFFERENCE at level j / at the first common level;
  read them as 𝔪_j / 𝔪_{s_1}. They are not BFT-3's locality mass m_0, nor P1's mass m. Likewise d_j = 𝔡_j (irrelevant
  difference); d also denotes the dimension (= 4) where written "d".
- **θ.** In §1.2 θ is the rotation angle (cos θ = 3/5). In §2.4(C), (E) "θ ≤ 11N/3 − 4" refers to P4's per-block rate
  exponent θ in "O((a/ℓ_0)^θ)". Neither is BFT's θ_w nor P4's reflection θ_eq.
- **g.** g ∈ SO(5) (P4's notation) versus couplings g_0, g(a), g_j, g(ρ); unambiguous by subscript/argument. g_0 is the
  running coupling at the fixed scale ℓ_0 (P4's "resolution 0"), NOT P4 §5.2's bare g_0(x; a); where the bare coupling
  is meant I wrote g(a) or g_0(x; a).
- **c.** c in Proposition T is the normalization offset; c in §2.4(D) is the one-loop scheme constant; c_4, c_6 in §3.4
  are insertion coefficients; C, C', C'' are generic constants.
- **ε_0** is BFT's small-field threshold throughout (REVIEW_S22 "max_P|log V^r_{k,P}| ≤ ε ≤ ε_0").
- **β_0, β_1** are the universal one- and two-loop coefficients (β_0 = 11N/(48π²)); not the lane's bare β_K.

## 9. What should change in the lane (for the lead)
1. **The consensus target (PLAN_S26 §10) should be stated as UNIV-T / UNIV-S / UNIV-Ω (§1), not "in bounded regions".**
   With a boundary, the statement silently contains boundary-discretization universality; on S^4 it must name the seam
   prescription (V12).
2. **Its UV status is settled as a reduction, not as a theorem.** Proposition T (PROVEN) plus §2.2 locate the only IR entry
   point (removing the volume factor), absent at fixed volume. The sphere route's S2 does not collapse to the flat route.
3. **New UV items, none in the lane, should go on the OS1 critical path:** N1 (two-theory contraction through large fields,
   with the marginal direction tracked, p > 2), N2 (misaligned first step with diverging ratio r, g^2 r → 0), N3 (sup over
   large coarse fields at the last levels), N4 (observable comparison for flowed observables), N5 (seam transparency); or,
   for UNIV-S only, the Ward route W0-W3 + N5. **The lane's E7, as stated, does not cover UNIV** (it fixes the marginal
   direction by tuning, which UNIV may not do).
4. **BFT's quantifier "max_P|log V| ≤ ε_0" is insufficient for UNIV**: the comparison must hold where it fails (PROVEN
   positive probability). Any BFT revision aimed at OS1 should consider backgrounds of bounded but non-small own-unit
   curvature at the last levels (N3).
5. **Gantumur (PLAN_S26 §10 "a JHEP citation ... could not be confirmed"):** per the arXiv v3 comments field (fetched),
   v3 is the published version, JHEP 07 (2026) 036. It does not help UNIV; see §4.
6. No numeric check was run. No number in this file decides a verdict except 11N/3 − 4 > 0 for N ≥ 2 and the identity
   16π²·11N/(48π²) = 11N/3 (one line each).

## 10. For the Codex reviewer: load-bearing steps, in the order to check
1. Proposition T (§2.1) — two lines; check the normalization step |c| ≤ δ_d.
2. The soft-kernel lower bound and its consequences (§2.1, §2.4(B), §6 re-check) — uses ||M̄_c||_op ≤ 1 from the lane.
3. §2.2: the interpolation identity and the two-phase example (tanh(η|Λ_n|)).
4. §3.1 + correction: the Gronwall/loop-gain step and the p > 2 requirement (sum bound via integral comparison).
5. §2.4(D): whether a fixed-ratio misaligned first step really leaves an O(1) marginal difference invisible to E7.2-type
   contraction (ARGUED; the place I am least sure of — see below).
6. §3.4: whether a global Killing field removes ROTDEF's flux term and whether (W0)'s dilation component is correctly
   O(g_0(a)^2).

**Least sure of.** (i) §2.4(D)'s claim that the marginal difference after a fixed-ratio misaligned step is O(1) in g^{-2}
(one-loop scheme constants) yet redundant: if it is in fact absent for a structural reason I missed, option (a) works and
N2 is unnecessary. (ii) §2.4(A)'s uniform interpolation constant C_N: I gave an obstruction-theory sketch, not a proof.
Neither affects the main verdict (no IR at fixed volume), which rests only on Proposition T and §2.2.

## 11. Closing statement (2026-10-28, after all of the above)
The rotated-lattice universality lemma is ultraviolet at fixed volume in the following exact sense: it follows (Proposition
T, PROVEN) from comparisons of the conditional integration of scales below ℓ_0, uniform over ALL coarse configurations,
with no information about the coarse law; infrared information enters only when the volume factor must be removed, which
the flat route must do and the sphere route at fixed R need not. P4's least-sure step therefore survives, but its
mechanism ("compactness makes the lattice dependence uniformly small") does not: the comparison must be uniform over
large-field sets of non-vanishing probability, must control the marginal direction (which E7 tunes away and UNIV may not),
and needs a constructed common coarse space; on S^4 it also needs a transparent seam (Codex's counterexample). Those are
the next UV targets. Gantumur's regulator does not supply any of them.

## 12. Errata from my own re-read (append-only; each item overrides the text it names)
- **E1 (§1.1, last sentence of "The content").** "Every non-trivial version compares the SAME continuum observable in two
  regularizations that are not conjugate by any isometry of the fixed geometry" is wrong for UNIV-S: 𝒦 and g𝒦 ARE
  conjugate by the isometry g of S^4_R. Correct: every non-trivial version compares the same continuum observable in two
  regularizations of one fixed geometry that are EITHER not conjugate by any of its isometries (UNIV-T), OR conjugate by an
  isometry g, in which case the content is g-invariance of the limit of ONE regularization (UNIV-S).
- **E2 (§2.3, "Without it").** "the lemma is E_{μ^1}[F] − E_{μ^1}[α_{R^{-1}}F] → 0 inside ONE theory" holds for UNIV-S (and
  on R^4). For UNIV-T, conjugacy maps grid R on T_ℓ to grid 1 on the isometric but differently oriented torus R^{-1}T_ℓ,
  so the own-representation comparison involves two coarse laws (two tori); the conclusion of that paragraph (the
  difference then lives in strongly coupled coarse integrals) is unchanged.
- **E3 (§2.4(C)).** A coarse 4-cell's boundary data fix only the FRACTIONAL part of the interior charge, and that part is
  carried by a field smooth at the cell scale ℓ_0 (it cannot shrink: instantons carry integer charge). Integer charge can
  sit in instantons of any size ρ ∈ [a, ℓ_0], but it is never forced by the coarse data; lattice-scale instantons occur
  with their natural weight ∝ (a/ℓ_0)^{11N/3−4} per cell (the background modifies the 't Hooft density only at relative
  order (ρ/ℓ_0)^4). So topology never forces lattice-scale structure, and the conclusion of (C) — UV-safe, exponent
  11N/3 − 4 > 0 — stands, by a simpler argument than the one written.
- **E4 (§8, item g).** In §1.2 "One bare-coupling function g_0(a)" denotes the BARE coupling as a function of a (with its
  argument), as in P4 §5.2's g_0(x; a). Without an argument, g_0 is the running coupling at ℓ_0. The claim in §8 that the
  bare coupling is always written g(a) or g_0(x; a) is corrected accordingly.
- **E5 (addendum to §2.1 "What this does and does not use"; strengthens it). PROVEN.** Write Z^G(V) := ∫k^G(V|U)e^{−S^G(U)}dU
  (the conditional partition function at coarse field V) and Z^G := ∫e^{−S^G}. Then ρ^G(V) = Z^G(V)/Z^G, and Z^G is a
  constant, so (U-dens) is EQUIVALENT to sup_V|log Z^1(V) − log Z^R(V) − c'| ≤ δ_d with c' := c + log Z^1 − log Z^R.
  Likewise E^G[F|V] = ∫F k^G(V|·)e^{−S^G}dU / Z^G(V). So both hypotheses of Proposition T are properties of the
  conditional fine measures μ^G(dU | V) ∝ k^G(V|U)e^{−S^G(U)}dU and their normalizations, one coarse configuration at a
  time. The coarse law ν^G does not appear in them at all. This is the exact content of "UV" in §2.5: the inputs are about
  the theory below ℓ_0 with the coarse field pinned, for every pinning.
- **E6 (layout).** §3.4 sits after §4 in the file because the file is append-only; it belongs to §3 and was written after
  §4, as its first line says.
