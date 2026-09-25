---
claim_id: admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk (as landed on main) for two records, either exchange sign, with any finite-range translation-invariant hermitian interaction W acting on block 78's one-record-per-site space (as landed) or on the full two-record space, and any local placement of the energy; blocks 136, 137 and 140 (open) placed. (T1) exact: the total two-step momentum of two records at total wave vector K and relative wave vector q is g_a = sin K_a cos 2q_a in every band; in two and three dimensions its derivative along the collision shells (fixed K and energy) is nonzero at explicit points for all four band pairs, so, being analytic, g is constant on no shell component for almost every K and energy. (T2) exact: a one-body placement adds nothing to a record's current within a band. (T3) proof with named standard imports: if the total energy current of such a pair is kept, then for almost every K the pair's scattering operator commutes with the total two-step momentum and is therefore the identity: the pair is transparent, and its records never scatter. (T4) on the line every shell is two points on which g takes one value, so a kept current puts no condition there. (T5) proof with named standard imports: near a total wave vector K0 at which the free pair's band functions have only nondegenerate stationary points, a transparent finite-rank change of the free pair has perturbation determinant identically one, so it removes no state and binds no pair. (T6) exact: such K0 exist, tan K0 = (5/6, 18/5) on Z^2 and (5/6, 18/5, 1/2) on Z^3 (exact resultants, exact root isolation, rational interval arithmetic). Hence under one record per site no finite-range interaction and no local placement keeps two records' books in the plane or in space, and without exclusion an interaction that keeps the books binds nothing. The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_2026_09_25.py
---

# Exact books need records that never scatter or bind: nothing local keeps them under one record per site

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact kinematics, an exact nondegeneracy proof at one wave vector in each dimension, and proofs from named standard scattering theory, within the landed walk and exclusion, with blocks 136, 137 and 140 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 136, 137 and 140 placed; it reports that no local interaction keeps two records' books under one record per site in two or three dimensions; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 137 (open) found that two records under one record per site lose their total energy current in the plane and in space. Block 141 (open) found that no coin term between neighbouring records restores it. The member's identity needs the current kept (block 137 T3). This note asks what any interaction, and any placement of the energy, would have to do to keep it.

- **T1: collisions do not keep the total two-step momentum.** Take two records at total wave vector `K` and relative wave vector `q`. Their total two-step momentum is `g_a = sin K_a cos 2q_a`, in every band. A collision keeps `K` and the energy. In the plane and in space, the set of pairs with a given `K` and energy (the collision shell) is a curve or a surface, and `g` varies along it.
- **T2: a placement adds nothing within a band.** Moving the energy's placement by a local one-body term changes a record's current only between its two bands.
- **T3: a kept current makes the pair transparent.** Suppose the total energy current is kept, for any local placement and any finite-range interaction, on the one-record-per-site space or on the full space. Then far apart the records carry their two-step momenta, so every collision must keep `g`. A finite-range interaction's scattering amplitude is analytic along the shells, and it can keep `g` only by vanishing. So the records never scatter.
- **T4: the line is different.** On a line each collision shell is two points, and `g` takes one value on them. So a kept current puts no condition on the line's collisions. That is why excluded records keep their books on a line (block 137).
- **T5: a pair that never scatters has nothing removed and nothing bound.** For a transparent pair the perturbation determinant, which measures how the interaction shifts the pair's spectrum, is identically one. It would have to vanish at every state the interaction removes or binds. One record per site removes the coincident states. So no finite-range interaction and no local placement keeps two records' books under one record per site in the plane or in space. Without exclusion, an interaction that keeps the books binds no pair.
- **T6: the needed nondegeneracy, proved exactly.** At one total wave vector in each dimension, every stationary point of the free pair's energy bands is nondegenerate. Exact resultants, exact root isolation and rational interval arithmetic show this. So T5 holds on a neighbourhood of that wave vector, which is enough.

In plain terms: the member's books require energy to flow exactly as the records' two-step momentum. A collision keeps the records' total wave vector and their total energy. On this lattice, in the plane and in space, those two do not fix the total two-step momentum, so a collision can trade some of it away. Books that hold exactly therefore allow no collisions at all. Records that cannot share a site do collide, and no local rule can make their collisions invisible: a pair that never scatters must also have lost nothing and bound nothing, and one record per site has lost the pair on one site. So, in the plane and in space, exact books belong to records that pass through each other unchanged and never stick together.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, one record per site, the interaction and the placements are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed): `H₂` on `ℤ^d`, with the pair states antisymmetric or symmetric. Under one record per site, coincidence is removed.
- **The interaction.** `W` is hermitian, commutes with the lattice's translations, and acts only when the records are within a fixed distance `R`. It acts on the one-record-per-site space or on the full two-record space. `H' = H₂ + W`.
- **A placement** (block 137). This is any energy density of `H'` that is a translation-invariant sum of local terms. Its first moment is `D' = D + F`, with `F` a sum of local terms. The total energy current is `J' = i[H', D']`.
- **The books.** The member's identity with a local stress needs `J'` kept, `[H', J'] = 0` (block 137 T3). For one free record, `i[H, D] = P` with `P` the two-step momentum (block 140 T1), and free records keep the books (block 136).
- **Fibers.** Everything commutes with the joint translations. At total wave vector `K`:
  - the pair is described in the relative coordinate `r = x₁ − x₂`;
  - `h₀(K)` is the free fiber generator and `h'(K)` the interacting one;
  - `ι` identifies the two spaces (the projection onto the one-record-per-site space, or the identity).
- **Standard imports, named at definition level.**
  - Wave operators, and their existence and completeness when the perturbation is of finite rank: the two-space Kato–Rosenblum theorem.
  - Decay of compact operators along a motion with purely continuous spectrum: the RAGE theorem, after Ruelle, Amrein, Georgescu and Enss.
  - The Riemann–Lebesgue lemma.
  - The stationary form of the scattering operator for finite-rank perturbations: a kernel on each energy shell, built from finitely many form factors.
  - The perturbation determinant and its relation to the scattering matrix: the Birman–Krein formula.
  - Continuous boundary values of the free resolvent away from thresholds (limiting absorption).
  - The Schwarz reflection principle, removable isolated singularities, and Liouville's theorem.
- **Nondegenerate stationary points at one wave vector** (proved in T6). At `tan K₀ = (5/6, 18/5)` in the plane and `(5/6, 18/5, 1/2)` in space, the free pair's four band functions have only nondegenerate stationary points, away from the cone points where a record's energy vanishes.
  - Nondegenerate stationary points persist under small changes of `K` (implicit function theorem). So the same holds for every `K` in a neighbourhood `U` of `K₀`.
  - For such `K` there are finitely many thresholds. Near each one the free pair's resolvent entries grow at most logarithmically in the plane and stay bounded in space; the cone points are no worse, since their tilt is below one (T6).

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

## Theorem T3 — a kept current makes the pair transparent

*Statement.* On `ℤ²` or `ℤ³`, let `W` and a placement be as declared, on either space. If `[H', J'] = 0`, then for almost every `K` the pair's scattering operator `S(K)` is the identity on the free pair's continuous states: the records never scatter.

*Proof.*
1. **Fibers.** `h'(K)` differs from `ι h₀(K) ι*` only on the finitely many relative positions within `R` of coincidence, together with the coincident states that one record per site removes. Give the removed states a fixed energy `λ` outside the spectrum: `h''(K) = h'(K) ⊕ λ` is then a finite-rank perturbation of `h₀(K)` on one space, and it scatters exactly as `h'(K)` does.
2. **Wave operators.** For a finite-rank difference, the wave operators `Ω±(K)`, the strong limits of `e^{ih't} ι e^{−ih₀t}` as `t → ±∞`, exist and are complete (Imports). `S(K) = Ω₊*Ω₋` is unitary and commutes with `h₀(K)`.
3. **The current far apart.** `J'` is the free pair's current plus local terms.
   - The free pair's current is `P ⊗ 1 + 1 ⊗ P` (block 140 T1) plus `i[H₂, F₁]`, where `F₁` is the one-body part of the placement.
   - Every two-body term, from `W`, from exclusion and from the placement, acts within a finite distance of coincidence. So in the fiber, `j'(K) = ΣP + i[h₀, f₁] + c(K)`, with `c(K)` of finite rank.
4. **Asymptotics.** Take `φ` among the free pair's continuous states.
   - Along the free motion, `c(K)` averages to zero: compact operators decay (Imports).
   - So does `i[h₀, f₁]`. Within a band it vanishes (T2). Between bands it carries phases `e^{i(E_b − E_{b'})t}`, whose differences are non-constant for almost every `K`, so they average away (Imports).

   Since `j'` commutes with `h'`, its mean in `Ω₋φ` does not change in time. As `t → −∞` it tends to `⟨φ, ΣP φ⟩`. Because `Ω₋φ = Ω₊ Sφ`, as `t → +∞` it tends to `⟨Sφ, ΣP Sφ⟩`. So `S*ΣP S = ΣP`: `S` commutes with the total two-step momentum.
5. **On the shell.** `S(K) = 1 − 2πi T(K)`. For a finite-rank difference, `T(K)` acts on each energy shell by a kernel `t(ω′, ω)`. This kernel is a finite sum of products of analytic form factors (Imports). Commuting with `ΣP` means `t(ω′, ω)(g(ω′) − g(ω)) = 0` almost everywhere.
6. **Kinematics.** By T1, for almost every `K` and energy, `g` is constant on no shell component. So `g(ω′) ≠ g(ω)` on a dense set, and the analytic kernel `t` vanishes. Hence `T(K) = 0` and `S(K) = 1`.

∎

*Checked.* T1 and T2 are the exact inputs; steps 1–5 are standard (Imports).

## Theorem T4 — the line, and the removed states

*Statement.*
- **The line.** On `ℤ` with walkers `σ_z D`, each collision shell is two points:
  - equal coins have `E = 2 sin(K/2) cos q` and shell `{q₀, −q₀}`;
  - opposite coins have `E = 2 cos(K/2) sin q` and shell `{q₀, π − q₀}`.

  On both, `g = sin K cos 2q` takes one value. So a kept current puts no condition on the line's collisions, as block 137 found.
- **The removed states.** One record per site removes, at every total wave vector, the coincident coin states: one (the singlet) for antisymmetric pairs and three for symmetric pairs. The singlet overlaps every band pair, with weight `(1 − s₁s₂ n₁·n₂)/4 ≠ 0` at the test directions. So the removed state couples to the continuum, and exclusion scatters, as block 137's lost current requires.

*Proof.* Direct computation. ∎

*Checked (D1, E1).* Both items.

## Theorem T5 — transparency leaves nothing removed and nothing bound

*Statement.* Let `K₀` be as in T6, and let `K` lie in a neighbourhood `U` of `K₀` on which the stationary points stay nondegenerate. Let `h''(K)` be a finite-rank change of `h₀(K)`, as in T3's step 1, with the removed states placed at an energy `λ` outside the spectrum. Suppose the pair is transparent, `S(K, E) = 1` for almost every `E`. Then the perturbation determinant `Δ(z) = det(1 + (h'' − h₀)(h₀ − z)⁻¹)` is identically one, so `h''(K)` has no eigenvalue outside the spectrum of `h₀(K)`.

Consequences:
- **(i) One record per site.** The removed states are eigenvalues of `h''` at `λ`. So no finite-range interaction makes the excluded pair transparent at any `K` in `U`. If the books held, T3 would make the pair transparent for almost every `K`, including almost every `K` in `U`, a set of positive measure. So no finite-range interaction and no local placement keeps two records' books in the plane or in space.
- **(ii) Without exclusion.** An interaction that keeps the books binds no pair at any `K` in `U`, since every bound pair is an eigenvalue outside the free spectrum.

*Proof.*
1. `Δ` is analytic off the spectrum of `h₀`, tends to one at infinity, and vanishes exactly at the eigenvalues of `h''` off that spectrum. Also `Δ(z̄)` is the complex conjugate of `Δ(z)`.
2. `det S(E) = Δ(E − i0)/Δ(E + i0)` (Imports). Transparency gives `det S = 1`, so `Δ(E + i0)` is real for almost every `E`. By the continuity of the boundary values away from thresholds (Imports), it is real on every open interval of the continuum between thresholds.
3. Real boundary values let `Δ` be continued across those intervals by reflection, and the continuation from below is `Δ` itself (Imports). So `Δ` is analytic except at the finitely many thresholds.
4. Near a threshold, for `K` in `U`, the free pair's resolvent entries grow at most logarithmically (plane) or stay bounded (space). `Δ` is a polynomial in finitely many of them, so it grows slower than any pole, and the singularity is removable (Imports).
5. `Δ` is then entire and tends to one, so it is identically one (Imports). An eigenvalue of `h''` off the spectrum would be a zero of `Δ`.

∎

*Checked (E2).* On a finite truncation of the line's relative problem with the coincident state removed and placed at `λ`, the identity `Δ(z) = det(h'' − z)/det(h₀ − z)` holds symbolically in `z`, and `Δ(λ) = 0`. This illustrates step 1; the analytic steps are imports.

## Theorem T6 — nondegenerate stationary points at one wave vector

*Statement.* Take `tan K₀ = (5/6, 18/5)` on `ℤ²` and `(5/6, 18/5, 1/2)` on `ℤ³`, and the band functions `E(q) = s₁ε(K₀/2 + q) + s₂ε(K₀/2 − q)`.
- Every stationary point of every band pair, away from the cone points, is nondegenerate.
- Per cell of a quarter period in each coordinate there are 4 stationary points for `(+, +)` and 2 for `(+, −)` in the plane, and 8 and 6 in space; `(−, −)` and `(−, +)` have the same points with the Hessian negated.
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

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 137 and 141 (open): one record per site loses the books in two and three dimensions; whether any local interaction or placement restores them (probes problems no-local-interaction-keeps-excluded-records-books, a-placement-that-keeps-excluded-records-books, a-possibility-shift-that-keeps-the-books)"
source_of_blocker_text: blocks 137 and 141 (open); probes refill n
reachability_to_target: advances
artifact_role: no_go
next_trace_action: "more than two records; how far the books hold at long wavelength for interacting records; scattering through the member"
conditional_surface_status: "two records; finite-range interactions; almost every total wave vector"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 54: the walk. Block 78: one record per site is an interaction.
- **Opened, not landed.**
  - Block 136 (PR #9196): free records keep symmetric books.
  - Block 137 (PR #9197): one record per site loses the current in the plane and in space, and keeps it on the line.
  - Block 140 (PR #9203): `i[H, D] = P`.
  - Block 141 (PR #9205): no neighbour coin term restores the current.
- **Probes.** The problem `no-local-interaction-keeps-excluded-records-books` (refill n) poses this question, with this route suggested. No attempt yet.
- **In the literature.**
  - Scattering theory for finite-rank perturbations: the Kato–Rosenblum theorem, the RAGE theorem, the Riemann–Lebesgue lemma and stationary scattering. Reference only; used as named imports.
  - The related fact that integrable one-dimensional systems keep extra currents because their collisions only exchange momenta.
- **New here:**
  - T1: the closed form of `g` and its variation on the shells.
  - T3: a kept energy current makes two interacting records transparent in two and three dimensions.
  - T4: the line's shells.
  - T5: a transparent pair removes and binds nothing, so nothing local keeps the books under one record per site.
  - T6: the exact nondegeneracy that T5 needs, at one wave vector in each dimension.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: what an interaction must do for two records to keep their total energy current. The obligations are:
- (O1) the shells' kinematics (T1);
- (O2) placements (T2);
- (O3) the scattering argument (T3);
- (O4) the line and the removed states (T4);
- (O5) transparency against removed and bound states (T5);
- (O6) nondegenerate stationary points at one wave vector (T6).

T1–T6 discharge them.

## No-Go Discipline Gate

The note's negative sentence: in the plane and in space, no finite-range interaction and no local placement keeps the total energy current of two records under one record per site; without exclusion, a kept current forces the pair to be transparent and unbound.

### N1 — Routes by which the sentence could fail or mislead
1. *The persistence step.* T6 proves nondegeneracy at one wave vector in each dimension. T5 uses it on a neighbourhood, by the implicit function theorem (Imports).
2. *Exceptional wave vectors.* The statements hold for almost every `K`; a measure-zero set of `K` (flat bands, band touchings) is not treated. The books are an operator identity, so failing at almost every `K` suffices.
3. *Infinite reach.* Interactions without a finite reach are not treated.
4. *More records.* The argument is for two records.
5. *Imports.* The scattering steps rest on standard theorems named under Imports and are not re-proved here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The standard scattering theory named under Imports; nothing else beyond the supplied walk, exclusion and interaction.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 78 (landed) | the walk; exclusion | yes (restated) |
| blocks 136, 137, 140 (open) | free records' books; the lost current; `i[H, D] = P` | yes (restated) |
| standard scattering theory | wave operators, decay, stationary kernels | yes (named imports) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "nothing local keeps two records' books under one record per site in the plane or in space" | executed: `g`'s closed form symbolically | executed: the shell derivative at an exact point for all four band pairs | executed: the placement lemma for any one-body term | executed: the line's shells; the removed states; the determinant identity on a truncation; T6's exact nondegeneracy proof | two records; finite reach; almost every `K` |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Some cleverly tuned neighbour term, or a push, might make excluded records pass each other invisibly."
  - *Reply:* T5 and T6 rule this out for every finite-range term. A pair that never scatters would have to have lost no state, and one record per site loses one (or three) at every total wave vector.

### N8 — Cross-cycle echo
- Block 137: one record per site loses the current.
- Block 141: coin terms don't restore it.
- This note: nothing local can restore it; exact books need records that never scatter or bind.

## Falsifiers

- A finite-range interaction and a placement that keep the current of two records under one record per site, in the plane or in space.
- A transparent finite-range change of the free pair with a bound pair outside the continuum.
- An error in T6's resultants, root isolation or interval bounds.
- A shell of positive measure on which `g` is constant, at a set of `K` of positive measure.

## Boundaries and non-claims

- Two records; finite-range interactions; almost every total wave vector.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54 and 78, restated. Blocks 136, 137 and 140, restated.
- Named standard imports, at definition level:
  - exact symbolic arithmetic;
  - the two-space Kato–Rosenblum theorem, for the existence and completeness of wave operators under finite-rank perturbations;
  - the RAGE theorem, after Ruelle, Amrein, Georgescu and Enss, for the decay of compact operators along a continuous motion;
  - the Riemann–Lebesgue lemma;
  - the stationary scattering kernel of a finite-rank perturbation;
  - the Birman–Krein formula;
  - limiting absorption for the free pair away from thresholds;
  - the Schwarz reflection principle, removable singularities and Liouville's theorem;
  - the implicit function theorem, for the persistence of nondegenerate stationary points;
  - resultants, exact isolation of real roots of rational polynomials, and interval arithmetic with rational endpoints.

## Review record

- **Who and when.** Supervisor-run block, the ninety-first since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check found blocks 137 and 141 and the probes problems of refills m and n. None has an attempt.
- **Checks during the work.**
  - The first shell check compared unsimplified trigonometric expressions with zero, which is not a proof. The runner instead uses angles with rational sines and cosines, so that nonvanishing is a comparison of rationals.
  - A first counting argument, following the phase of the continuum, forced only bound pairs inside the continuum, not a contradiction. The argument through the perturbation determinant (T5) closes the question, given the nondegeneracy proved in T6, because transparency makes the determinant real on the continuum and hence entire.
  - A first version assumed nondegenerate stationary points at almost every wave vector. Since the books are an operator identity, one wave vector and its neighbourhood suffice, and T6 proves that case.
  - A floating-point search at `K₀ = (0.7, 1.3)` in the plane found 16, 8, 8 and 16 stationary points for the four band pairs, all nondegenerate (smallest `|det Hess|` about `0.27`). At `K₀ = (0.7, 1.3, 0.45)` in space it found 64, 48, 48 and 64, all nondegenerate (smallest about `0.29`).
  - T6 then proved the nondegeneracy exactly at nearby wave vectors with rational half-angle data. The counts agree with the search, divided by the four (plane) and eight (space) quarter-period cells.
- **Independence.** Mutation census: seven mutations in families B–E (four in E), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_exact_books_need_records_that_never_scatter_or_bind_nothing_local_keeps_them_under_one_record_per_site_2026_09_25.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
