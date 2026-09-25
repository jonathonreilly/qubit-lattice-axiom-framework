---
claim_id: admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Exact two-walker shell kinematics, band-diagonal placement identity, fixed-channel line shells, removed
  coin dimensions and rational-interval nondegeneracy certificates at the stated total momenta. Conditional scattering
  implications require the explicitly stated absolutely-continuous wave-operator, local-current, shell-kernel and
  complex threshold hypotheses. The determinant conclusion excludes off-continuum eigenvalues only in the specified
  momentum neighbourhood; embedded states and a global no-binding theorem are not established. The unrestricted
  local-interaction no-go remains deferred pending the analytic bridge.
upstream_dependencies:
- admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25
- admissibility_rule_one_record_per_site_no_possibility_shift_among_neighbours_restores_the_books_no_neighbour_coin_term_keeps_two_excluded_records_energy_current_bounded_theorem_note_2026-09-25
- admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_bounded_theorem_note_2026-09-25
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_2026_09_25.py
---

# Two-walker shell geometry and a conditional scattering obstruction

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact kinematics, an exact nondegeneracy proof at one wave vector in each dimension, and proofs from named standard scattering theory, within the landed walk and exclusion, with blocks 136, 137 and 140 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note retains exact two-walker algebra and interval enclosures, with scattering conclusions conditional on an unresolved analytic bridge; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Exact two-walker shell kinematics, band-diagonal placement identity, fixed-channel line shells, removed coin dimensions and rational-interval nondegeneracy certificates at the stated total momenta. Conditional scattering implications require the explicitly stated absolutely-continuous wave-operator, local-current, shell-kernel and complex threshold hypotheses. The determinant conclusion excludes off-continuum eigenvalues only in the specified momentum neighbourhood; embedded states and a global no-binding theorem are not established. The unrestricted local-interaction no-go remains deferred pending the analytic bridge.

T1, T2, the fixed-coin-channel part of T4 and the interval enclosures in T6 are retained exact calculations. T3 and T5 below state conditional implications, not a completed all-local-interactions theorem. In particular, nondegenerate stationary energies do not by themselves document all complex resolvent estimates, coin-projector behaviour at cones and shell regularity needed by the analytic continuation step.

The recovery task is to prove that bridge with the actual matrix-valued free resolvent and finite-relative-range current. Original broader claims remain on the frozen source branch. A passing finite determinant example or interval runner is not evidence that the scattering bridge has been discharged.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, one record per site, the interaction and the placements are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed): `H₂` on `ℤ^d`, with the pair states antisymmetric or symmetric. Under one record per site, coincidence is removed.
- **The interaction.** `W` is bounded and hermitian, commutes with the lattice's translations, and acts only when the records are within a fixed distance `R`. It acts on the one-record-per-site space or on the full two-record space. `H' = H₂ + W`.
- **A placement** (block 137). Here restrict to bounded finite-range densities whose current away from coincidence is the additive one-body current, with a bounded finite-relative-support remainder. No claim covers arbitrary nonlocal placements. Its first moment is `D' = D + F`, with `F` a sum of local terms. The total energy current is `J' = i[H', D']`.
- **The books.** The member's identity with a local stress needs `J'` kept, `[H', J'] = 0` (block 137 T3). For one free record, `i[H, D] = P` with `P` the two-step momentum (block 140 T1), and free records keep the books (block 136).
- **Fibers.** Everything commutes with the joint translations. At total wave vector `K`:
  - the pair is described in the relative coordinate `r = x₁ − x₂`;
  - `h₀(K)` is the free fiber generator and `h'(K)` the interacting one;
  - `ι` identifies the two spaces (the projection onto the one-record-per-site space, or the identity).
- **Standard imports, named at definition level.**
  - Wave operators, and their existence and completeness when the perturbation is of finite rank: the two-space Kato–Rosenblum theorem.
  - Time-averaged decay of compact operators on the continuous subspace: the RAGE theorem, after Ruelle, Amrein, Georgescu and Enss.
  - The Riemann–Lebesgue lemma.
  - The stationary form of the scattering operator for finite-rank perturbations: a kernel on each energy shell, built from finitely many form factors.
  - The perturbation determinant and its relation to the scattering matrix: the Birman–Krein formula.
  - Continuous boundary values of the free resolvent away from thresholds (limiting absorption).
  - The Schwarz reflection principle, removable isolated singularities, and Liouville's theorem.
- **Nondegenerate stationary points at one wave vector** (proved in T6). At `tan K₀ = (5/6, 18/5)` in the plane and `(5/6, 18/5, 1/2)` in space, the free pair's four band functions have only nondegenerate stationary points, away from the cone points where a record's energy vanishes.
  - Nondegenerate stationary points persist under small changes of `K` (implicit function theorem). So the same holds for every `K` in a neighbourhood `U` of `K₀`.
  - For such K the band geometry suggests finitely many thresholds. The uniform complex resolvent bounds needed by T5, including the coin projectors at cones, are an explicit unresolved analytic hypothesis.

## Theorem T1 — the collision shells

*Statement.* For two records at total wave vector `K`, with `k₁ = K/2 + q` and `k₂ = K/2 − q`, the total two-step momentum is `g_a = ½(sin 2k₁ₐ + sin 2k₂ₐ) = sin K_a cos 2q_a`. It is the same in every band, since the two-step momentum is a multiple of the identity on the coins.

On `ℤ²` and `ℤ³`, take:
- the band pair `(s₁, s₂)` and the pair energy `E = s₁ ε(k₁) + s₂ ε(k₂)`, with `ε = (Σ sin²k)^{1/2}`;
- the point with `k₁ = (a₁, a₂, a₃)` and `k₂ = (b₁, b₂, b₃)`, whose sines and cosines are `(3/5, 4/5)`, `(5/13, 12/13)`, `(20/29, 21/29)` and `(8/17, 15/17)`, `(7/25, 24/25)`, `(9/41, 40/41)`.

There the two-form `dg₁ ∧ dE` on `(q₁, q₂)` is nonzero for all four band pairs.

Since `g` and `E` are analytic away from the band-touching points, `dg₁ ∧ dE` then vanishes only on a set of measure zero. For almost every `K` and almost every energy, therefore, `g` is constant on no component of the shell.

*Proof.*
1. The identity is `sin(x + y) + sin(x − y) = 2 sin x cos y`.
2. At the point, `dg₁/dq₁ = −2 sin(a₁ + b₁) sin(a₁ − b₁)` is a nonzero rational.
3. `∂E/∂q₂ = s₁ sin 2a₂/(2ε(k₁)) − s₂ sin 2b₂/(2ε(k₂))`. The squares of its two terms differ, a comparison of rationals, so it is nonzero for every sign.
4. If `g` were constant on a shell component `C`, `dg` would be parallel to `dE` along `C`, and `C` would lie in the zero set of `dg₁ ∧ dE`. Integrating over energies, this happens only on a set of shells of measure zero.

∎

*Checked (B1).* The identity symbolically in both dimensions; the minor exactly at the point.

## Theorem T2 — placements within a band

*Statement.* Take one record with `h(k) = Σ_a sin k_a σ_a` and any translation-invariant one-body placement `f(k) = f₀ + f·σ`. Then the change `i[h(k), f(k)]` of its current has zero trace against each band projector `(1 ± h/ε)/2`. The free record's current, its two-step momentum `sin k cos k`, is a multiple of the identity on the coins and commutes with `h(k)`.

*Proof.* The trace of `[h, f]` is zero, and so is the trace of `h[h, f]`, by cyclicity. ∎

*Checked (C1).* Symbolically on `ℤ³`.

## Theorem T3 — conditional transparency implication

*Statement.* In addition to T1 and T2, assume the analytic bridge stated below: complete absolutely-continuous wave operators for the identified finite-rank pair, the displayed bounded local-current decomposition, time-averaged free current asymptotics, and a continuous finite-rank shell kernel on regular shells. On `ℤ²` or `ℤ³`, let `W` and a placement be as declared, on either space. If `[H', J'] = 0`, then for almost every `K` the pair's scattering operator `S(K)` is the identity on the free pair's absolutely continuous states: the records never scatter.

*Proof.*
1. **Fibers.** `h'(K)` differs from `ι h₀(K) ι*` only on the finitely many relative positions within `R` of coincidence, together with the coincident states that one record per site removes. Give the removed states a fixed energy `λ` outside the spectrum: `h''(K) = h'(K) ⊕ λ` is then a finite-rank perturbation of `h₀(K)` on one space, and it scatters exactly as `h'(K)` does.
2. **Wave operators.** For a finite-rank difference, the wave operators `Ω±(K)`, the strong limits of `e^{ih't} ι e^{−ih₀t}` as `t → ±∞`, exist and are complete (Imports). `S(K) = Ω₊*Ω₋` is unitary and commutes with `h₀(K)`.
3. **The current far apart.** `J'` is the free pair's current plus local terms.
   - The free pair's current is `P ⊗ 1 + 1 ⊗ P` (block 140 T1) plus `i[H₂, F₁]`, where `F₁` is the one-body part of the placement.
   - Every two-body term, from `W`, from exclusion and from the placement, acts within a finite distance of coincidence. So in the fiber, `j'(K) = ΣP + i[h₀, f₁] + c(K)`, with `c(K)` of finite rank.
4. **Asymptotics.** Take `φ` among the free pair's absolutely continuous states.
   - Along the free motion, `c(K)` averages to zero: compact operators decay (Imports).
   - So does `i[h₀, f₁]`. Within a band it vanishes (T2). Between bands it carries phases `e^{i(E_b − E_{b'})t}`, whose differences are non-constant for almost every `K`, so they average away (Imports).

   Since `j'` commutes with `h'`, its mean in `Ω₋φ` does not change in time. Its negative-time Cesaro mean tends to `⟨φ, ΣP φ⟩`. Because `Ω₋φ = Ω₊ Sφ`, its positive-time Cesaro mean tends to `⟨Sφ, ΣP Sφ⟩`. So `S*ΣP S = ΣP`: `S` commutes with the total two-step momentum.
5. **On the shell.** `S(K) = 1 − 2πi T(K)`. For a finite-rank difference, `T(K)` acts on each energy shell by a kernel `t(ω′, ω)`. This kernel is a finite sum of products of analytic form factors (Imports). Commuting with `ΣP` means `t(ω′, ω)(g(ω′) − g(ω)) = 0` almost everywhere.
6. **Kinematics.** By T1, for almost every `K` and energy, `g` is constant on no shell component. So `g(ω′) ≠ g(ω)` on a dense set, and the analytic kernel `t` vanishes. Hence `T(K) = 0` and `S(K) = 1`.

∎

*Checked.* T1 and T2 are the exact inputs; steps 1–5 use the additional analytic hypotheses; their lattice application is not proved by the runner.

## Theorem T4 — the line, and the removed states

*Statement.*
- **The line.** On `ℤ` with walkers `σ_z D`, each collision shell is two points:
  - equal coins have `E = 2 sin(K/2) cos q` and shell `{q₀, −q₀}`;
  - opposite coins have `E = 2 cos(K/2) sin q` and shell `{q₀, π − q₀}`.

  On both, `g = sin K cos 2q` takes one value. Within a fixed coin channel this scalar current gives no extra condition on those two points. Coin-changing multichannel collisions are not covered by that statement.
- **The removed states.** One record per site removes, at every total wave vector, the coincident coin states: one (the singlet) for antisymmetric pairs and three for symmetric pairs. The singlet overlaps every band pair, with weight `(1 − s₁s₂ n₁·n₂)/4 ≠ 0` at the test directions. This establishes the displayed nonzero overlap only. It does not alone prove scattering or a current obstruction.

*Proof.* Direct computation. ∎

*Checked (D1, E1).* Both items.

## Theorem T5 — conditional determinant implication near the stated momentum

*Statement.* Assume the determinant boundary identity, continuous boundary values on all regular spectral intervals and a uniform complex sub-pole bound at every threshold, including cones, as specified below. Let `K₀` be as in T6, and let `K` lie in a neighbourhood `U` of `K₀` on which the stationary points stay nondegenerate. Let `h''(K)` be a finite-rank change of `h₀(K)`, as in T3's step 1, with the removed states placed at an energy `λ` outside the spectrum. Suppose the pair is transparent, `S(K, E) = 1` for almost every `E`. Then the perturbation determinant `Δ(z) = det(1 + (h'' − h₀)(h₀ − z)⁻¹)` is identically one, so `h''(K)` has no eigenvalue outside the spectrum of `h₀(K)`.

Consequences:
- **(i) One record per site.** The removed states are eigenvalues of `h''` at `λ`. So no finite-range interaction makes the excluded pair transparent at any `K` in `U`. If the books held, T3 would make the pair transparent for almost every `K`, including almost every `K` in `U`, a set of positive measure. Thus the stated current cannot be conserved for an excluded pair if all of the additional analytic hypotheses hold on a positive-measure neighbourhood. Verifying them is still open in this landing.
- **(ii) Without exclusion.** Under these additional hypotheses, an interaction that keeps the current has no eigenvalue outside the free spectrum at the covered K in U. Embedded eigenstates and momenta outside U are not excluded.

*Proof.*
1. `Δ` is analytic off the spectrum of `h₀`, tends to one at infinity, and vanishes exactly at the eigenvalues of `h''` off that spectrum. Also `Δ(z̄)` is the complex conjugate of `Δ(z)`.
2. `det S(E) = Δ(E − i0)/Δ(E + i0)` (Imports). Transparency gives `det S = 1`, so `Δ(E + i0)` is real for almost every `E`. By the continuity of the boundary values away from thresholds (Imports), it is real on every open interval of the continuum between thresholds.
3. Real boundary values let `Δ` be continued across those intervals by reflection, and the continuation from below is `Δ` itself (Imports). So `Δ` is analytic except at the finitely many thresholds.
4. By the additional complex threshold hypothesis, near each threshold the relevant free resolvent entries grow at most logarithmically (plane) or stay bounded (space). `Δ` is a polynomial in finitely many of them, so it grows slower than any pole, and the singularity is removable (Imports).
5. `Δ` is then entire and tends to one, so it is identically one (Imports). An eigenvalue of `h''` off the spectrum would be a zero of `Δ`.

∎

*Checked (E2).* On a finite truncation of the line's relative problem with the coincident state removed and placed at `λ`, the identity `Δ(z) = det(h'' − z)/det(h₀ − z)` holds symbolically in `z`, and `Δ(λ) = 0`. This illustrates step 1; the analytic steps are imports.

## Theorem T6 — nondegenerate stationary points at one wave vector

*Statement.* Take `tan K₀ = (5/6, 18/5)` on `ℤ²` and `(5/6, 18/5, 1/2)` on `ℤ³`, and the band functions `E(q) = s₁ε(K₀/2 + q) + s₂ε(K₀/2 − q)`.
- Every stationary point of every band pair, away from the cone points, is nondegenerate.
- The enclosure classifier returns 4 and 2 candidate boxes for `(+, +)` and `(+, −)` in the plane, and 8 and 6 in space, on which the respective Hessian excludes zero and the gradient has not been excluded. These are candidate counts, not a proof of existence of one stationary point in every box. The implication needed here is only that every stationary point is enclosed and nondegenerate. Negating both bands negates the Hessian.
- At the cone points, the other record's energy has squared gradient `139761000/606502321` (plane) and `2653455542/8714332815` (space), below one.

*Proof.*
1. **Coordinates.** Everything depends on `k` through `sin²k` and `sin k cos k`, which have period `π`. With `tₐ = tan k₁ₐ` and `tan K₀ₐ` rational, `sin²`, `sin cos` and `cos 2k` of both records are rational in `tₐ`.
2. **No stationary point on a coordinate line.** At a stationary point, `sin k₁ₐ cos k₁ₐ` and `sin k₂ₐ cos k₂ₐ` are both nonzero. If one vanished, the stationary condition would force the other to vanish too, and then `K₀ₐ ∈ {0, π/2}` modulo `π`, which is false here. So every stationary point has every `tₐ` finite and nonzero.
3. **Polynomial system.** A stationary point satisfies the ratio equations `(sin k₁₁cos k₁₁)(sin k₂ₐcos k₂ₐ) = (sin k₁ₐcos k₁ₐ)(sin k₂₁cos k₂₁)`, which carry no sign. It also satisfies the square of the first component of the stationary condition. Clearing denominators gives polynomials with rational coefficients.
4. **Elimination.** The resultant in the other variables is a nonzero polynomial in `t₁`, of degree 16 in the plane and 40 in space. So every stationary point has `t₁` among its real roots. For each root, the ratio equations are quadratics in each other `tₐ`, which never vanish identically. This gives at most two candidates per coordinate.
5. **Isolation and sign checks.**
   - The real roots are isolated exactly in rational intervals.
   - The candidates are enclosed by rational interval arithmetic, with rational bounds for square roots.
   - At every candidate and for each band pair, either some component of the gradient excludes zero (not stationary), or the Hessian determinant excludes zero (nondegenerate).
   - No candidate is left undecided.
6. **Cones.** Near a cone point the band function is a cone in one record's momentum, tilted by the other record's energy gradient. The squared tilts are the exact rationals above, below one.

∎

*Checked (E3).* All of the above, exactly (about 2 s).

## Analytic bridge and actual scope

T3 requires bounded local current decomposition, existence and completeness of wave operators on the absolutely continuous subspaces, and the shell representation. The finite-rank operator theorem supplies the wave-operator part; it does not by itself supply every matrix-valued lattice threshold estimate. In the current argument use Cesaro expectations: compact remainders vanish in time mean; the finite band off-diagonal commutator terms have zero time mean outside zero-measure band coincidences. A conserved expectation then has equal incoming and outgoing means. T1 uses connectedness away from cone sets, analyticity, Fubini and the regular-shell coarea formula to pass from its nonzero joint momentum witness to almost-every-shell variation.

T5 additionally requires the determinant boundary relation, real continuous regular boundary values and a uniform bound slower than any pole for complex z approaching each isolated threshold from the cut complement. Under these hypotheses reflection glues the two half-plane functions, the isolated singularities are removable and the determinant is one by its normalization at infinity. T6's finite stationary-point certificate is relevant input but is not substituted for the uniform complex estimate. The original assertion that naming standard theorems completed this bridge is withdrawn. General finite-rank scattering theory does not automatically certify every local-placement hypothesis in this application.

## Prior art and what is new

The retained additions are exact shell and coin identities and the rational interval certificate, plus explicit conditional implications. Primary references: [Behrndt, Malamud and Neidhardt, Finite Rank Perturbations, Scattering Matrices and Inverse Problems, sections 3 and Appendix A](https://arxiv.org/abs/0902.3568) for absolutely-continuous scattering, and [Scattering matrices and Weyl functions, section 4](https://arxiv.org/abs/math-ph/0604013) for the determinant/spectral-shift relation in its stated extension setting. These references do not establish the unresolved application-specific threshold bridge.

## No-Go Discipline Gate

### N1 — Routes and quantifiers
Only the defined bounded finite-relative-range model and conditional analytic bridge are covered. Longer range, nonadditive asymptotic currents, cone singularities, embedded states and exceptional momenta remain open.

### N2 — Wall independence
No repository no-go wall is a premise.

### N3 — Hidden imports
Absolutely-continuous scattering and the complex threshold bridge are explicit; the latter remains an obligation.

### N4 — Dependencies
The linked current walk and exclusion notes supply only their stated models. The original broader source-current obstruction is not imported as a landed theorem.

### N5 — Executed coverage
The runner tests scalar momentum identities, a rational nonzero shell derivative for all four band pairs, the band-diagonal placement identity, fixed-coin line shells, coin exclusion ranks, a finite determinant example, and interval enclosures. It does not execute an infinite-volume scattering proof. Candidate counts are not existence certificates.

### N6 — Partial closure
The exact algebra and interval enclosure remain useful even with the scattering bridge open. No new primitive is adopted.

### N7 — Strongest alternative
A specially designed interaction or placement can evade an unstated asymptotic or threshold assumption. It is not ruled out by the retained runner. Resolving the bridge is required before an unconditional exclusion theorem.

### N8 — Continuation
Send the original six-theorem argument, current narrowed parents, exact rational certificate and analytic hypotheses to the deferred probes campaign. The work is open, not a claimed universal closure.

## Boundaries and non-claims

Two records and the stated conditional setting only. Off-continuum eigenvalue exclusion, when its assumptions hold, is local in total momentum. No global no-binding theorem, physical gravity conclusion or audit verdict is asserted. The original branch preserves all historical arguments and campaign reports.

## Imports

Exact symbolic arithmetic, polynomial elimination and rational root enclosures are used for T6. The analytic assumptions are specified above. RAGE gives time means, not unrestricted pointwise compact decay.

## Review record

Original author source is frozen at PR #9229 head `136eb4f7a61b7e1b98b829593bace4f8b7cbc240`. Same-session primary review narrows the global no-binding claim, the line-channel statement and the analytically unsupported no-go, corrects interval candidate counts and fails closed on any unresolved cone enclosure. No second reviewer or audit is claimed.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_2026_09_25.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.

## Dependencies

- [Current narrowed source 9196](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current narrowed source 9197](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_TWO_EXCLUDED_RECORDS_LOSE_THEIR_ENERGY_CURRENT_IN_TWO_AND_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current narrowed source 9203](ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current narrowed source 9205](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_NO_POSSIBILITY_SHIFT_AMONG_NEIGHBOURS_RESTORES_THE_BOOKS_NO_NEIGHBOUR_COIN_TERM_KEEPS_TWO_EXCLUDED_RECORDS_ENERGY_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
