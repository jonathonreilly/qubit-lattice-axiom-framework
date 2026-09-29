---
claim_id: every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_the_helicity_one_channel_at_least_a_quarter_as_much_on_direction_average_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Supplied comparator premises (not supplied by the axioms): the landed tensor carrier and scalar stencil S, finite slots, harmonic comparators with positive-semidefinite analytic move weights. Probe 15's swapped assignment (metric stored; exact scalar Gauss law); moves r with S r = 0 and fixed range, whose O(q^2) kinetic form is fixed by first moments, r_hat(q) = -i M(q) + O(q^2). (A) For every finitely supported r with S r = 0, the leading symbol forces (q^2 delta - q q):M(q) = 0, a rank-10 map on the 18 first-moment unknowns whose 8-dimensional kernel is exactly M(q) = sym(q (x) xi) + sym(q x A) (xi in R^3, A symmetric traceless); the 2^3 box kernel realises all 8. (B) Proved analytically (sym(n x A) = (1/2) L_n A scales helicity m by i m) and checked by exact quadrature: <|M_+-1|^2> = (1/4) <|M_TT|^2> + (1/3)|xi|^2, no xi-A cross term on average; so for any move family the direction-averaged helicity +-1 kinetic weight is at least 1/4 of the TT weight (probe 11's T2 applied to the rotation-averaged family), and every nonzero first moment is helicity +-1 visible on an open dense set of directions. (C) Lattice families meet the bound (min exactly 1/4). (D) Every helicity +-1 tensor sym(qhat (x) e) is a TT tensor at qhat x e, and every traceless 2-plane contains a TT-type element; so an on-site stiffness positive on every TT plane is positive on every helicity +-1 plane and positive definite on TT(qhat) + helicity +-1(qhat) off a cone. Corollary (metric stored, with the TT mode linear in every direction and a positive-semidefinite on-site stiffness V): the modes inside the O(q^2) kinetic range split into linear modes and soft modes (the range meeting ker V); in an open dense set of directions the kinetic range has helicity +-1 content, so it is not carried by two pure-TT linear modes alone: some mode in the range, linear or softer, carries helicity +-1 weight. Under premise P (ker V meets the scalar-rule space ker s(qhat) only in 0), which holds off a quadric cone whenever ker V has dimension at most 1 (probe 18's stiffness: everywhere), that mode is linear. (E) Harmonic illustration with random non-covariant families. (F) Over all 18 first-moment dimensions the bound is still 1/4 (spin 2; spin 3 gives 8/5). (G) The referee's pointwise counterexample (pure-TT linear modes, helicity +-1 content in a soft mode) reproduced; premise P checked for kernels of dimension at most 1; a two-dimensional kernel meets ker s(qhat) in every direction. (H, added after confirmation) Even with a two-dimensional kernel (the trace direction plus a nonsingular traceless tensor, the only possibility), some linear mode is not pure TT on a dense set of directions: pure-TT linear modes would force every move's M(n) n parallel to a primitive cubic, hence zero. Registered after the scratch computation. Not shown: with a two-dimensional stiffness kernel, whether the linear modes' non-TT content must include helicity +-1 rather than helicity 0 only, O(q^3) kinetic terms, indefinite-weight or non-harmonic states, non-on-site symmetry breaking, one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
  - breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_makes_the_tt_harmonic_modes_linear_but_the_helicity_one_partners_move_with_them_bounded_theorem_note_2026-09-29
runner: scripts/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.py
---

# Every Gauss-law-compatible move that feeds the TT channel feeds the helicity-1 channel, at least a quarter as much on direction average

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** an analytic lemma, a symbol theorem and a linear-algebra
corollary, with exact and lattice checks; registered after the scratch
computation; unaudited. Revised after the first referees, and again after
the second round, which found that the kinetic range fixes the modes' content
only up to soft modes. Independent checks are recorded below.

## In one paragraph

In probe 18, a local stiffness broke the momentum rule and made the spin-2
(TT) waves linear, and the helicity ±1 directions moved too. That was shown
for isotropic move sets.

This probe shows it for every move set that respects the time rule.
- Each move's first moment either shifts the metric like a gauge change, or
  curls it.
- The curl feeds the helicity ±1 channel exactly a quarter as much as the
  spin-2 channel on direction average. The gauge part feeds only ±1 (and
  0).
- A stiffness that holds the spin-2 waves in every direction also holds
  every ±1 direction, because each ±1 tensor is a spin-2 tensor for another
  direction.

So when the spin-2 waves are linear in every direction, the waves are not
just two pure spin-2 waves: in an open, dense set of directions some mode
carries helicity ±1 weight. It is a linear mode when the stiffness leaves
at most one direction free (as in probe 18). In general it may instead be a
slower mode.

## Registration

Written in the probe's scratch file **after** the scratch computation that
found the ¼. So it fixes how the outcome is read; it is not independent
evidence.
- **PASS** if some move family feeds TT at O(q²) while its ±1 weight
  vanishes in every direction.
- **FAIL** if the ±1 weight is bounded below by a fixed fraction of the TT
  weight for every family.

**Outcome: FAIL, with fraction ¼.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils, the moment lemma).

Of this PR:
- **[Probe 11](THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md),
  T2.** In an isotropic family, 4v₁ = v₂ + 3v₀. Direction-averaged weights
  equal the channel weights of the rotation-averaged family, so B's ¼ is T2
  plus v₀ ≥ 0.
  - New here: the explicit split (the curl has no helicity-0 part, so a
    pure-curl family saturates ¼), positive definiteness on all 8
    dimensions, the extension to non-covariant families (T6's escape is only
    pointwise), and the corollary.
- **[Probe 15](THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md):**
  the first-moment space.
- **[Probe 18](BREAKING_THE_MOMENTUM_RULE_WITH_AN_ON_SITE_METRIC_STIFFNESS_IN_THE_SWAPPED_ASSIGNMENT_MAKES_THE_TT_HARMONIC_MODES_LINEAR_BUT_THE_HELICITY_ONE_PARTNERS_MOVE_WITH_THEM_BOUNDED_THEOREM_NOTE_2026-09-29.md):**
  the isotropic instance; its Fable referee already had ¼ for the curl
  family.

External, reference only:
- the div–Div elasticity complex (Pauly and Zulehner, arXiv:1609.05873) and
  its polynomial sym-curl complex (Chen and Huang, arXiv:2007.12399), the
  mathematics behind A;
- Schur's lemma.

## Premises (supplied)

The axioms supply none of these. They are the comparator premises of
probes 10–18:
- the tensor carrier and the scalar stencil S;
- finite slots;
- harmonic comparators, with kinetic form Σ_t c_t |w·r̂_t(q)|² and weights
  c_t ≥ 0 (positive semidefinite and analytic);
- the swapped assignment (metric stored, scalar Gauss law exact), except in
  F.

## A — the first-moment space (check A)

- For finitely supported r with S r = 0: at order q², the six independent
  quadratics of S's leading symbol force a zero zeroth moment. At order q³,
  (q²δ_ij − q_iq_j) M_ij(q) = 0 identically in q.
- That is a linear map from the 18 first-moment unknowns (M_ij,k symmetric
  in ij) to the 10 cubic monomials. It has rank 10 (checked), so its kernel
  is 8-dimensional.
- The 8 forms sym(q ⊗ ξ) and sym(q × A) lie in it, so they are the kernel.
- The 2³ box kernel realises all 8 (fit residual 1e-14, rank 8). For
  integer moves the image is a rank-8 lattice in this space.

## B — the lemma, proved (check B)

Normalisation: Frobenius norm; helicity states of unit norm; each channel
summed over its two states.
- **The curl rotates.** sym(n × A) = ½[N, A] = ½ L_n A, where N is the
  cross-product matrix of n and L_n the rotation generator about n. L_n
  multiplies the helicity-m part of A by i m. So, pointwise:
  - |C_TT|² = |P_TT A|²;
  - |C_±1|² = ¼|P_±1 A|²;
  - C_0 = 0.
- **The gauge part.** sym(n ⊗ ξ) has no TT part, and |G_±1|² = ½|ξ_⊥|².
- **Averages over directions.** ⟨P_m⟩ = (dim_m / 5) I on spin 2, and
  ⟨(n·ξ)²⟩ = |ξ|²/3. So:
  - ⟨|M_TT|²⟩ = (2/5)|A|²;
  - ⟨|M_±1|²⟩ = (1/10)|A|² + (1/3)|ξ|².
- **The cross term.** Pointwise it is ξ·(n × A n), which averages to zero
  because A is symmetric.
- Hence `⟨|M_±1|²⟩ = ¼⟨|M_TT|²⟩ + ⅓|ξ|²`. Summing over any family with
  c_t ≥ 0, the direction-averaged ±1 kinetic weight is at least ¼ of the TT
  weight.
- The ±1 form is positive definite on all 8 dimensions. Its value is a
  polynomial in n, so it is nonzero on an open dense set of directions.
- Exact quadrature confirms all of these numbers.
- **Weights of indefinite sign** (Fable check): since the curl vanishes on
  nn, positivity of the kinetic form on ker s(n) forces the gauge block
  Q_ξξ ⪰ 0, and ⟨±1⟩ − ¼⟨TT⟩ = ⅓ tr Q_ξξ ≥ 0. So the bound survives for
  stable forms with mixed-sign weights.

## C — lattice families (check C)

With lattice first moments and the exact quadrature:
- the box kernel: 0.81;
- 200 random integer combinations and 30 random 3-move sub-families:
  minimum exactly 0.2500, reached by pure-curl families.

## D — stiffnesses that hold TT hold ±1 (check D)

- **The ±1 tensors are TT tensors.** sym(q̂ ⊗ e), with e ⊥ q̂, has null
  vector q̂ × e and is traceless in the plane orthogonal to it. So it is a TT
  tensor at the direction q̂ × e (distance 1e-15 over 500 samples).
- **Every traceless 2-plane contains a TT-type element.** The determinant
  restricted to the plane is a real binary cubic, so it has a real root. A
  rank-2 traceless tensor has eigenvalues (a, −a, 0), so it is TT at its
  null vector. All 300 random planes contain one.
- **So:** a positive-semidefinite on-site stiffness that is positive on
  every TT plane:
  - is positive on every ±1 plane;
  - has at most a one-dimensional kernel among traceless tensors;
  - is therefore positive definite on TT(q̂) ⊕ ±1(q̂), except on the cone of
    q̂ where the kernel vector v has q̂·v·q̂ = 0.
- "Positive on every TT plane" is exactly what a TT mode linear in every
  direction needs in the metric-stored assignment, where the kinetic weight
  is O(q²).
- The Fierz–Pauli form is not in this class: it is negative on the trace,
  so it is not positive semidefinite on the six slots. On traceless
  tensors it equals |h|². It vanishes on q̂q̂, which lies in ker s(q̂), the
  kind of direction the corollary's soft alternative needs.

**Corollary (metric stored).** Suppose the TT mode is linear in every
direction and the on-site stiffness V is positive semidefinite. At a
direction q̂ let K be the O(q²) kinetic form and R its range. R lies in
ker s(q̂) = TT(q̂) ⊕ ±1(q̂) ⊕ span{q̂q̂}, where s is the leading symbol of
the scalar stencil.
- **The split.** The modes (ẍ = −q²KVx) with x in R are linear modes
  (KVx = ω²x with ω² > 0) and soft modes (Vx = 0). R is the direct sum of
  the two:
  - KV restricted to R is similar to the symmetric form K^½VK^½, so it is
    diagonalisable;
  - if x is in R and KVx = 0, then Vx lies in ker K = R⊥, so x·Vx = 0, and
    Vx = 0 because V is positive semidefinite.
- **Helicity ±1 content in R.** By B, R has a ±1 component on an open
  dense set of directions. There the modes in R are not just two pure-TT
  linear modes: some mode in R, linear or soft, carries ±1 weight. A soft
  mode is not TT, because V is positive on TT(q̂).
- **Premise P.** Suppose ker V ∩ ker s(q̂) = 0. Then R has no soft modes,
  so a linear mode carries the ±1 weight.
  - If ker V is spanned by one vector w, P fails only where
    q̂·w·q̂ = tr w, a quadric cone. It is never met when w is the trace
    direction, probe 18's case, since s(q̂)I = −2.
  - A two-dimensional kernel meets the hyperplane ker s(q̂) in every
    direction, so P fails everywhere. Lemma H below shows that even then the
    linear modes are not all pure TT on a dense set of directions. Whether
    their non-TT content must include helicity ±1, rather than helicity 0
    only, is open.
- **The referee's counterexample** (second round, reproduced in G) is
  pointwise, at q̂ = ẑ. Take u = (TT₁ + H1ₓ + q̂q̂)/√3, V = 1 − uuᵀ and
  K = P_TT + uuᵀ.
  - The linear modes are pure TT, with ω²/q² = 2/3 and 1.
  - u is a soft mode with ±1 weight ⅓.
  - V's kernel is u, so P fails only on the cone through ẑ where
    q̂·u·q̂ = tr u.

For example, two curl moves give exactly two linear modes, each mixed.

## E — harmonic illustration (check E)

- Random non-covariant 3-move families, with an |h|² stiffness.
- Every family whose linear modes carry TT weight also has a linear mode
  with ±1 weight in some sampled direction. The stiffness |h|² has no
  kernel, so premise P holds. The weights are in the cache.
- Only 8 families and 8 directions are sampled: an illustration of the
  corollary, not its proof.

## F — all 18 first-moment dimensions (check F)

- If the moves are not restricted by any rule, the first moments range over
  all 18 dimensions: two spin-1 parts, one spin-2 and one spin-3. This is
  the momentum-stored assignment with the momentum rule broken.
- The direction-averaged ±1/TT ratio, minimised over the TT-invisible parts
  (Schur complement), is ¼ (spin 2) or 8/5 (spin 3). So the bound holds for
  any local move.

## G — from the kinetic range to the modes (check G)

- **G1.** The referee's counterexample at q̂ = ẑ:
  - positive eigenvalues 2/3 and 1, both modes pure TT;
  - one soft mode, u, with ±1 weight ⅓;
  - V is positive on every sampled TT plane, with smallest eigenvalue at
    least 1/9, the value set by u's traceless part.
- **G2.** Two stiffnesses whose kernel has dimension one:
  - the trace (probe 18's);
  - a random vector.

  For 12 random 3-move families × 40 directions each (480 pairs):
  premise P held in every sampled direction, R had no soft mode, and some
  linear mode carried ±1 weight wherever the kinetic ±1 block was nonzero.
- **G3.** A kernel spanned by the trace and diag(1, 1, −2) meets ker s(q̂) at
  all 200 sampled directions. This is the open case.

## H — a two-dimensional stiffness kernel (check H; added after confirmation)

**Lemma H.** Let V be positive semidefinite and positive on every TT plane,
and let the moves feed TT. Then, with no premise P, some linear mode is not
pure TT on a dense set of directions.

**Proof.**
- **The kernel.** ker V contains no TT tensor, so its traceless part is at
  most one-dimensional (D). A nonzero element of that part is nonsingular,
  since a singular traceless tensor is TT at its null direction. So either
  dim ker V ≤ 1, where premise P holds off a cone, or ker V = span{t, k}
  with tr t = 1 and k traceless and nonsingular.
- **Take the second case.** In direction n, ker V meets ker s(n) along
  w(n) = (n·k·n) t − (n·t·n − |n|²) k.
- **What pure-TT linear modes would force.** Suppose every linear mode were
  pure TT on an open set of directions. By the split lemma, every move's
  first moment M(n) then lies in TT(n) ⊕ span{w(n)}. For a tensor T in
  ker s(n), the vector T n fixes T's non-TT part. So g(n) = M(n) n is
  parallel to f(n) = w(n) n on the open set, and hence everywhere, since g
  and f are homogeneous polynomials of degree 2 and 3.
- **f has only finitely many common complex zeros.**
  - If n·k·n ≠ 0, then f(n) = 0 gives t n = λ k n. Dotting with n gives
    |n|² = 0, so n lies on the smooth conic |n|² = 0 and is an eigenvector
    of k⁻¹t. Each eigenspace has dimension 1 or 2, because k⁻¹t is not a
    multiple of 1 (tr t = 1, tr k = 0). Projectively it is a point or a
    line, and a line meets a smooth conic in at most two points.
  - If n·k·n = 0, then k n ≠ 0 forces n·t·n = |n|². That is two conics
    with no common component: the first is smooth, and t − 1 is not a
    multiple of k, by the trace.
- **Conclusion.** So f has no common scalar factor. A quadratic g parallel
  to a primitive cubic f must vanish. So M(n) n = 0 for every n, which
  forces ξ = 0 and A = 0: no move feeds TT, a contradiction.

**Check H:**
- For 30 random admissible kernels, the parallel condition g ∥ f, sampled
  at 80 directions, has only the zero solution among the 8 first-moment
  parameters. This illustrates the proof; it is not the proof.
- Control: drop the nonsingularity. Take k = diag(−1, 0, 1)/√2, which is
  TT at ŷ, so positivity on TT planes excludes it, and
  t = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]. Then a nonzero move exists, so the
  nonsingularity step is load-bearing.

**Still open for a two-dimensional kernel:** whether the non-TT content of
the linear modes must include helicity ±1 rather than helicity 0 only.
That is one scalar condition, det(n, g, f) = 0, instead of the vector
condition. Check H finds only the zero solution for random kernels, but no
proof is given.

## What this means

On finite slots with the time rule exact, making the spin-2 waves linear in
every direction by breaking the momentum rule with a local stiffness never
gives just two pure spin-2 waves. In an open dense set of directions, some
mode in the kinetic range carries helicity ±1 weight:
- it is a linear mode when the stiffness kernel meets the scalar-rule space
  only in zero (premise P; probe 18's stiffness);
- otherwise it may be a softer mode.

The ±1 kinetic weight is at least a quarter of the spin-2 weight on average.

This closes probe 18's route "another move set" for harmonic comparators
with stable kinetic forms at O(q²).

## No-Go Discipline Gate

The bounded negative claims, inside the premises:
- (a) the ¼ bound on direction-averaged weights;
- (b) the corollary: with the TT mode linear in every direction (metric
  stored), some mode in the kinetic range carries ±1 weight on an open
  dense set of directions; under premise P that mode is linear.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *Gauge–curl cancellation.* ATTEMPTED (B): the cross term averages to
     zero. Fails for (a).
  2. *Anisotropic or non-covariant weighting.* ATTEMPTED (B, C): the
     average is exact for every weighting. Fails.
  3. *First moments outside the 8 forms.* ATTEMPTED (A: the rank-10 symbol
     map, proved for all finite supports). Fails.
  4. *A kinetic ±1 block and a stiffness ±1 block that are orthogonal.*
     ATTEMPTED (D): a stiffness positive on every TT plane is positive
     definite on TT ⊕ ±1 off a cone, so no orthogonality is possible there.
     Fails on TT ⊕ ±1. The helicity-0 direction q̂q̂ is route 7.
  5. *Indefinite move weights.* ATTEMPTED (B, the Fable check's
     argument): stability forces Q_ξξ ⪰ 0. Fails.
  6. *Moves unrestricted by any rule.* ATTEMPTED (F): the bound is still ¼.
     Fails.
  7. *A stiffness kernel inside ker s(q̂) that absorbs the ±1 content into
     a soft mode* (the second-round counterexample). ATTEMPTED (G).
     - It succeeds pointwise, so (b) keeps "linear or softer".
     - Premise P excludes it; with a kernel of dimension at most 1, P fails
       only on a cone.
     - With a two-dimensional kernel, Lemma H shows that the linear modes
       are still not all pure TT. Whether their non-TT content must
       include ±1 is open.

  **Open routes:**
  - (i) families with zero first moments, which are soft anyway;
  - (ii) non-on-site symmetry breaking;
  - (iii) non-harmonic states;
  - (iv) stiffnesses not positive on every TT plane, for which the TT mode
    is not linear in every direction;
  - (v) two-dimensional stiffness kernels (route 7), where the ±1 content
    may sit in soft modes, though the linear modes are not all pure TT
    (H).
- **N2 — pairwise table, with directions.**
  - W1: the exact scalar Gauss law.
  - W2: fixed range with analytic symbols.
  - W3: harmonic comparators with positive-semidefinite weights.
  - W4: an on-site stiffness, positive semidefinite and positive on every
    TT plane (for (b)).
  - W5: premise P, ker V ∩ ker s(q̂) = 0 (for (b)'s linear version only).

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: the scalar rule does not fix the range | no: range fixes no rule | independent |
  | W1, W3 | no | no | independent |
  | W1, W4 | no: the rule constrains moves, not the stiffness | no | independent |
  | W1, W5 | no | no: P is a property of V given s | W5 refers to W1's s |
  | W2, W3 | no: local forms can be indefinite | no: harmonic forms can be non-local | independent |
  | W2, W4 | no | no | independent |
  | W2, W5 | no | no | independent |
  | W3, W4 | no: kinetic weights say nothing of V | no | independent |
  | W3, W5 | no | no | independent |
  | W4, W5 | no: G3's kernel satisfies W4, not W5 | no: V = 1 satisfies both; P alone allows V negative | independent |

  (a) uses W1–W3. (b) adds W4, and its linear version adds W5. F drops W1.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "harmonic" and "positive semidefinite weights": explicit (W3);
  - "common support" of the kinetic and stiffness forms: proved on
    TT ⊕ ±1 (D). The helicity-0 direction q̂q̂ is a hidden condition,
    now explicit as W5 with its open case;
  - "quadrature": a check, not the proof;
  - "box": A is proved for all supports, and the box shows surjectivity;
  - "registered after": stated;
  - "canonical" (the cache path): not load-bearing.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md:137 | v₁ ≥ v₂/4 needs isotropy | applied to the rotation-averaged family | yes |
  | same note:229 | cubic forms evade T2 | only pointwise; the average holds | yes |
  | docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md:138 | the zeroth and first moments of ker S moves | proved in general (A) | yes |
  | docs/BREAKING_THE_MOMENTUM_RULE_WITH_AN_ON_SITE_METRIC_STIFFNESS_IN_THE_SWAPPED_ASSIGNMENT_MAKES_THE_TT_HARMONIC_MODES_LINEAR_BUT_THE_HELICITY_ONE_PARTNERS_MOVE_WITH_THEM_BOUNDED_THEOREM_NOTE_2026-09-29.md:108 | partners only for isotropic forms | extended (corollary) | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "at least a quarter" | each move's first moment | the scalar rule at every site touching the box | quadrature directions | 231 families | proved analytically for all families (B) |
  | "some mode in the kinetic range carries ±1 weight; linear under P" | not applicable | not applicable | the E and G samples (illustration) | random families | proved for the stated premises (D, the split lemma), on an open dense set of directions; the linear version needs W5 |

- **N6 — primitive scan.** None invoked. The tensor carrier, S and the
  spin slots are supplied comparator premises.
- **N7 — steelman, in a hostile reviewer's voice.** "Symmetry breaking that
  is not on-site, or by a second field, could stiffen TT with a
  q-dependent form that is positive on TT(q̂) only at q̂ itself. The
  TT-plane argument in D uses q-independence. Also, stability forms with
  exotic structure beyond O(q²), or strongly correlated states, are not
  covered. The terminal obligation is the classification of q-dependent
  breaking terms. And a stiffness with a two-dimensional kernel, which
  contains a trace direction, can meet ker s(q̂) in every direction and
  absorb the ±1 content into soft modes." Convincing against a broader
  claim. So the corollary is stated for on-site stiffnesses only, and its
  linear version under W5.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probe 11's isotropic partner identity | extended | rotation averaging | yes |
  | probe 18's isotropic partner result | extended | the ¼ lemma and the TT-plane lemma | yes |

- **Outcome.** PASS as scoped. The registered outcome is FAIL, with
  fraction ¼.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. The corollary was not proved: the kinetic and stiffness ±1 blocks
     could be orthogonal. Answered by the TT-plane lemma and the traceless
     2-plane lemma (D); the corollary is now "the linear modes are not pure
     TT".
  2. A needed a general proof. Given (the rank-10 symbol map).
  3. B confirmed, with the normalisation stated.
  4. The O(q²) statement needed its premises. Stated (W2, W3).
  5. The gate. Rewritten.
  6. Scope and prior art. The premises are marked supplied, and the
     elasticity-complex literature is added.
- **Fable check (same family): STANDS WITH CORRECTIONS.** No mathematical
  error. Its points, all applied here:
  - the analytic proof (B);
  - the probe 11 T2 attribution;
  - "no cross term" holds on average only;
  - "partners" means non-pure-TT linear modes;
  - the Fierz–Pauli premise;
  - E's mismatch with the cache;
  - the indefinite-weight sharpening.
- **gpt-5.6-sol, second round: FAILS.**
  - Resolved: A (rank 10 confirmed by exact arithmetic), B, the premises
    and scope.
  - The corollary's step from the kinetic range to the modes was false.
    The referee gave a pointwise counterexample: a positive-semidefinite V,
    positive on every TT plane, with pure-TT linear modes and the ±1
    content in a soft mode along q̂q̂ + H1.
  - Answered: the corollary is now the split lemma ("linear or softer"),
    with premise P for the linear version and the counterexample reproduced
    in G.
  - Also fixed: the Fierz–Pauli wording (not positive semidefinite on six
    slots), E's quoted maxima (now left to the cache), the N5 line, and gate
    items N1.4, N3 and N7.
- **gpt-5.6-sol, third round: CONFIRMED AS REVISED.** Every second-round
  finding was resolved. The referee checked the split lemma, the
  reproduced counterexample, the Fierz–Pauli wording, P's cone for
  one-dimensional kernels and the open-dense step independently, and found
  no material overreach.
- **Addendum after confirmation: check H.** A two-dimensional stiffness
  kernel cannot hide all non-TT content in soft modes. Fourth round:
  pending.

## Reproduction

`python3 scripts/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.py`
prints 8 checks, A–H, the N5 lines and TOTAL, in about 9 s. The canonical
cache is at
logs/runner-cache/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.txt.
