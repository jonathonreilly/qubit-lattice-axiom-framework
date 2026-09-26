---
claim_id: admissibility_rule_no_finite_range_interaction_keeps_two_excluded_records_total_energy_current_on_the_plane_or_in_space_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk and block 78's one record per site, two records of either exchange sign on Z^2 or Z^3, with any bounded hermitian translation-invariant interaction acting within a fixed relative distance and any placement in block 143's class (the member's density plus a bounded finite-range one-body change, with a bounded remainder of finite relative support), all as landed on main: the total energy current J' = i[H', D'] is not conserved, [H', J'] != 0, so no such interaction and placement keeps the books. Proof in the fibers of total wave vector K near block 143's K0: (i) a kept current forces the one-body placement current to vanish, since a multiplication operator of finite rank is zero; (ii) the resolvent identity [g, T(z)] = (h0 - z)[F2, R''(z)](h0 - z) and the spectral theorem make the on-shell T-matrix vanish at almost every energy, by block 143 T1; (iii) the determinant identity det(1 + AB) = det(1 + BA) then makes the perturbation determinant real on the continuum; (iv) bounded spectral densities, from block 143 T6, put Delta - 1 in H^2 of both half-planes, whose boundary values meet only in zero, so Delta = 1; (v) the removed on-site states make Delta vanish at their energy, a contradiction. (T2) The same holds for any number N >= 2 of records and any finite-range interaction of any body number: separating all but two records reduces a kept current exactly to the pair's, since a free record keeps its own current. (T3) The proof uses only the form of the current (the free two-step momentum plus a one-body placement change plus a finite-rank remainder), so the same holds for the total two-step momentum in any such placement: no local momentum of that form is conserved either. This proves block 143's deferred conclusion within that class, without its scattering hypotheses. Found by probe #9251 (Claude Opus 5.5, the supervisor's own model family), line-checked by the supervisor, with an independent exact runner for the algebraic steps; the analytic steps rest on named standard theorems. Not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_no_finite_range_interaction_keeps_two_excluded_records_total_energy_current_on_the_plane_or_in_space_2026_09_26.py
---

# No finite-range interaction keeps two excluded records' total energy current on the plane or in space

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (a proof within the stated class of interactions and placements, from named standard analysis and block 143's landed exact inputs; a harvest of probe #9251, Claude Opus 5.5, the supervisor's own model family, line-checked by the supervisor; not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 78, 121, 137, 140 and 143 as landed on main (the walk, one record per site, the exclusion's compression, the placement class, the two-step momentum and the shell geometry); it proves that no finite-range interaction keeps two excluded records' total energy current on the plane or in space; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 137 (landed) found that under one record per site, two records keep their total energy but not their total energy current, so they cannot keep the member's books exactly. Block 143 (landed) asked whether some local interaction restores them. It proved the kinematics and the nondegenerate shell geometry exactly, but kept its no-go conditional on an analytic bridge: wave operators, a local-current decomposition, shell kernels, and complex threshold bounds including the cones. Probe #9251 proved the conclusion by a different route that needs none of those hypotheses. This note states that proof and checks its algebra exactly.

- **The theorem.** Take two records of the walk under one record per site, on the plane or in space, with either exchange sign.
  - Add any bounded hermitian interaction that commutes with the lattice's translations and acts only within a fixed distance of coincidence.
  - Use any placement in block 143's class.
  - Then the total energy current `J′ = i[H′, D′]` is not conserved: `[H′, J′] ≠ 0`.
- **The chain.** In each fiber of total wave vector `K` near block 143's `K₀`:
  - a kept current forces the one-body placement current to vanish;
  - the pair then scatters nothing on almost every energy shell;
  - the perturbation determinant is then real on the continuum, and a complex-analysis argument makes it identically one;
  - but the removed on-site states make it vanish at their own energy.

- **Any number of records.** The same holds for any number of records, `N ≥ 2`, and any finite-range interaction of any body number (T2).
- **The momentum too.** The proof never uses that `J′` is the energy current, only its form: the free two-step momentum, a one-body placement change and a finite-rank remainder. The total two-step momentum in any such placement has the same form, so it is not conserved either (T3). Move all but two records far apart; a free record keeps its own current, so a kept current for all `N` would be a kept current for the pair.

In plain terms: the books need the pair's total energy current to stay constant. When two records meet, the current can change unless the collision does nothing at all, exactly, on every energy shell. A collision that does nothing leaves a certain determinant equal to one everywhere. But one record per site deletes the coincident states, and deleting states always leaves a zero in that determinant. So a pair of excluded records always scatters in a way that changes its energy current, whatever short-range force acts between them.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, one record per site, the interaction and the placement are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed). `h(k) = Σ_a sin k_a σ_a`, `ε(k) = |sin k|`, `H₂ = H ⊗ 1 + 1 ⊗ H` on `ℤ^d`, `d = 2` or `3`, with the pair states symmetric or antisymmetric. One record per site removes the coincident coin states: the singlet for antisymmetric pairs and three states for symmetric pairs (block 143 T4).
- **The interaction.** `V` is bounded and hermitian, commutes with the joint translations, and acts only when the records are within a fixed relative distance `R`, on the one-record-per-site space. `H′ = P H₂ P + V`, with `P` the projection onto that space.
- **The placement** (blocks 137 and 143). The energy densities are local. Away from coincidence the current is the additive one-body current of the member's density `e_x = ½(Π_xH + HΠ_x)`, plus the current of any bounded translation-covariant one-body placement change of finite range. The rest is a bounded remainder of finite relative support. The first moment is `D′`, and the total current is `J′ = i[H′, D′]`.
- **The books** (block 137 T3). The member's identity with a local stress needs `J′` kept, `[H′, J′] = 0`.
- **Fibers.** At total wave vector `K` the pair lives on `L²(𝕋^d_q) ⊗ ℂ⁴`, or its exchange subspace, with `k₁ = K/2 + q`, `k₂ = K/2 − q`. The free generator `h₀(K)` is multiplication by `h(k₁) ⊗ 1 + 1 ⊗ h(k₂)`, and the free total current `g` is multiplication by `g_a = sin K_a cos 2q_a`, the total two-step momentum, with `[h₀, g] = 0` (blocks 140 and 143 T1).
- **Landed exact inputs** (block 143).
  - T1: for almost every `K` and almost every energy, `g` is constant on no component of the shell.
  - T4: the removed states exist in every fiber.
  - T6: at `tan K₀ = (5/6, 18/5)` (plane) and `(5/6, 18/5, 1/2)` (space), every stationary point of every band function away from the cones is nondegenerate, and the cone tilts are below one. Both persist on a neighbourhood `U` of `K₀`.
- **Standard imports, named at definition level.**
  - The spectral theorem.
  - Boundary values: the transform `∫dμ(E′)/(E′ − z)` of a finite measure has boundary values at almost every real point, and their jump is `2πi` times the density of the absolutely continuous part (Fatou and de la Vallée Poussin).
  - The coarea formula.
  - The quadratic normal form at a nondegenerate stationary point (the Morse lemma).
  - `H^p` below means the Hardy space of the upper (or lower) half-plane. The transform above maps `L^p(ℝ)` densities into `H^p` for `1 < p < ∞` (M. Riesz); products obey Hölder's inequality.
  - The boundary values of `H²` of the upper and of the lower half-plane meet only in zero (Paley–Wiener).
  - The direct-integral decomposition of translation-invariant operators.
  - The identity theorem for real-analytic functions.
  - The determinant identity `det(1 + AB) = det(1 + BA)` (Sylvester).

## Theorem — no finite-range interaction keeps the current

*Statement.* Under the premises above, `[H′, J′] ≠ 0` on `ℤ²` and on `ℤ³`, for either exchange sign.

*Target.* In the fibers, `[h′(K), j′(K)] ≠ 0` for almost every `K` in `U`, a set of positive measure. That gives the statement, by the direct-integral decomposition.

*Proof.* Fix `K ∈ U` outside the null set excluded by block 143 T1.

- **S0. Extension past the removed states.** Let `Π₀ = 1 − P`, of finite rank. Place the removed states at an energy `λ` outside the spectrum of `h₀`: `h″ = h′ ⊕ λΠ₀` and `j″ = j′ ⊕ μΠ₀`. Then `[h′, j′] = 0` iff `[h″, j″] = 0`.
  - `h″ − h₀ = F₁ = AWA*`, with `W` a hermitian `r × r` matrix and the columns of `A` of finite relative support, so trigonometric polynomials in `q`.
  - Every two-body term, from `V`, from the exclusion and from the placement, acts within a finite relative distance. So `j″ = g + i[h₀, m] + F₂`, with `m` the symbol of the one-body placement change and `F₂ = A₂W₂A₂′*` of finite rank with trigonometric-polynomial columns.
- **S1. A kept current has no one-body placement current.** Suppose `[h″, j″] = 0`. Every term of the commutator is of finite rank except `i[h₀, [h₀, m]]`, a multiplication operator by a bounded matrix function. A multiplication operator of finite rank on `L²(𝕋^d) ⊗ ℂ⁴` is zero, since a nonzero one is nonzero on a set of positive measure. So `[h₀, [h₀, m]] = 0` almost everywhere.
  - The double commutator splits as `[h₁, [h₁, f₁]] ⊗ 1 + 1 ⊗ [h₂, [h₂, f₂]]`, with traceless parts. A partial trace shows each part vanishes (runner B2).
  - For one record, `[h·σ, [h·σ, f·σ]] = −4(h × (h × f))·σ` and `[h·σ, f·σ] = 2i(h × f)·σ`: the double commutator vanishes iff the single one does (runner B1).
  - So `i[h₀, m] = 0` and `j″ = g + F₂`.
- **S2. The resolvent identity.** Let `R₀ = (h₀ − z)⁻¹`, `R″ = (h″ − z)⁻¹` and `T(z) = F₁ − F₁R″F₁`, for `z` not real. Then `R″ = R₀ − R₀TR₀`. Since `j″` commutes with `R″` and `g` with `R₀`,
  `[g, T(z)] = (h₀ − z)[F₂, R″(z)](h₀ − z)`.
  - Using `(h₀ − z)R″ = 1 − F₁R″` and `R″(h₀ − z) = 1 − R″F₁`, the right side is `(h₀ − z)F₂(1 − R″F₁) − (1 − F₁R″)F₂(h₀ − z)`. Its kernel is a finite sum of trigonometric polynomials in `(q′, q)` times finitely many scalars `⟨φ|R″(z)|ψ⟩`.
  - Sandwich between band eigenvectors `⟨u_b(q′)|` and `|u_a(q)⟩` with `E_b(q′) = E_a(q) = E`, at `z = E + iη`. The `F₂` terms cancel, and
  `(g(q′) − g(q)) T_ba(z; q′, q) = iη ⟨u_b(q′)|(F₂R″F₁ − F₁R″F₂)(q′, q)|u_a(q)⟩`.
  - Runner C1 checks both identities exactly in a finite model with `[j″, h″] = 0`.
- **S3. A kept current makes the pair transparent at almost every energy.**
  - By the spectral theorem, `iη⟨φ|R″(E + iη)|ψ⟩ → −⟨φ|1_{E}(h″)|ψ⟩` as `η → 0`. This is zero unless `E` is one of the countably many eigenvalues of `h″`. So the right side of S2 tends to zero.
  - The kernel of `T` is `A(W − WQ″W)A*` with `Q″ = A*R″A`. Its entries are transforms of finite measures, so `T(E + i0)` exists for almost every `E` (Premises).
  - Hence, for almost every `E`, `(g(q′) − g(q)) t_ba(q′, q) = 0` at every pair of shell points, with `t = T(E + i0)`.
  - For almost every `E` the shell avoids the cones and the stationary points, and its components are connected real-analytic hypersurfaces. By block 143 T1, `g` is constant on no component. By the identity theorem it is then constant on no open subset, so `g(q′) ≠ g(q)` on a dense subset of each product of components.
  - `t_ba` is continuous there: trigonometric polynomials with fixed coefficients, and continuous band vectors away from cones and band contacts. So `t_ba = 0` on every shell, including the forward direction: the on-shell T-matrix vanishes.
- **S4. The determinant is real on the continuum.** Let `Δ(z) = det(1 + WQ₀(z))`, with `Q₀ = A*R₀A`.
  - `T = AW(1 + Q₀W)⁻¹A*` and `det(1 + WQ₀)det(1 − WQ″) = 1` (runner D1). So where the boundary values exist, `Δ(E + i0) ≠ 0` and `M = W(1 + Q₀(E + i0)W)⁻¹` is defined.
  - Let `Γ(E) = (Q₀(E + i0) − Q₀(E − i0))/(2πi)`, the density matrix of `⟨a_i|dE_{h₀}|a_j⟩`. At a regular `E`, `Γ = 𝓡*𝓡`, where `𝓡` restricts `c ↦ Σc_ia_i` to the shell with the measure `dσ/|∇E_a|` (coarea).
  - S3 gives `𝓡M𝓡* = 0`, so `ΓMΓ = 0`. Then `X = Γ^{1/2}MΓ^{1/2}` vanishes, since `Γ^{1/2}` is invertible on the range of `Γ`, which contains the ranges of both sides of `X`.
  - The determinant identity gives `det(1 + W(Q₀⁺ − 2πiΓ)) = det(1 + WQ₀⁺) det(1 − 2πiX)` (runner D1). So `Δ(E − i0) = Δ(E + i0)`.
  - `Δ(z̄)` is the conjugate of `Δ(z)`, since `W` is hermitian and `Q₀(z̄) = Q₀(z)*` (D1). So `Δ(E + i0)` is real for almost every `E`.
- **S5. Bounded spectral densities.** For `K ∈ U` and bounded weights `φ`, the push-forward of `φ dq` under each band function has a density in `L^∞` on `ℤ³`, and in every `L^p`, `p < ∞`, on `ℤ²`. It suffices that the volume of `{e < E_a < e + δ}` is at most `Cδ` in space, or `Cδ(1 + log(1/δ))` in the plane. Cover the torus by finitely many open sets:
  - where `|∇E_a| ≥ c > 0`, flow-box coordinates with `E_a` as one coordinate give `Cδ`;
  - near a nondegenerate stationary point (T6), the quadratic normal form gives `E_a = τ + Σε_iy_i²` with a bounded Jacobian: in space the slab has volume at most `Cδ` for every signature; in the plane extrema give `πδ` and saddles a logarithmic density, in every `L^p`;
  - near a cone of one record, `E_a = s₁ω + ψ` with `ω = |sin(ρθ)|` along rays from the cone point and `ψ` the other record's smooth energy, with `|∇ψ| = t < 1` (T6): so `|dE_a/dρ| ≥ (1 − t)/4` near the point, each ray meets the slab in length at most `4δ/(1 − t)`, and the volume is at most `Cδ`. The coin projectors are discontinuous at the cone but bounded, which is all that is used.

  So the entries of `Q₀` are transforms of compactly supported densities in `L¹` and in every `L^p`. They lie in `H^p` of the upper half-plane for every `1 < p < ∞` (Premises), and are `O(1/|z|)` at large `|z|`.
- **S6. `Δ = 1`.** `Δ − 1` is a sum of products of `k ≤ r` entries of `WQ₀`. Each entry lies in `H^{2r}`, so each product lies in `H^{2r/k}`, is locally square-integrable on lines parallel to the real axis uniformly, and is `O(|z|^{−k})` at infinity. So `Δ − 1 ∈ H²` of the upper half-plane, and by `Δ(z̄) = conj Δ(z)` also of the lower one. By S4 the two boundary functions agree almost everywhere. The boundary values of the two `H²` spaces meet only in zero (Premises), so `Δ = 1` on both half-planes, and by analyticity on the whole complement of the spectrum of `h₀`.
- **S7. The contradiction.** `λ` lies outside the spectrum of `h₀`, and `h″Π₀ = λΠ₀` with `Π₀ ≠ 0` (T4). Since `h″ − λ = (h₀ − λ)(1 + R₀(λ)F₁)`, the factor `1 + R₀(λ)F₁` is not injective, so `Δ(λ) = det(1 + R₀(λ)F₁) = 0` (the determinant identity; runner H1). This contradicts `Δ = 1`. So `[h″(K), j″(K)] ≠ 0` for almost every `K ∈ U`, and `[H′, J′] ≠ 0`. ∎

## Theorem T2 — any number of records

*Statement.* Take `N ≥ 2` records under one record per site on `ℤ²` or `ℤ³`, either exchange sign, with a bounded hermitian translation-invariant interaction of finite range, of any body number, and a placement whose one- and two-record parts are in block 143's class. Then `[H_N, J_N] ≠ 0`.

*Proof.*
- **One record.** If the one-body placement change makes a single record lose its current, `[H_1, J_1] ≠ 0`. Records placed far apart then give `[H_N, J_N] ≠ 0` directly, by the reduction below with every cluster a single record. Otherwise `[H_1, J_1] = 0`, as for the free record (block 140 T1).
- **Clusters.** Take two-record states `ψ, ψ′` and one-record states `φ_m, φ′_m` (`m = 3, …, N`), all of finite support in position space, and translate record `m` by `a_m`. Once the translated supports lie farther apart than the interaction's range plus the hop, every term coupling different clusters acts as zero on these states: the commutator's cross terms, the exclusion between clusters, and the exchange overlaps between different assignments of records to clusters. So, exactly,
  `⟨Ψ_a, [H_N, J_N] Ψ′_a⟩ = ⟨ψ, [H₂, J₂] ψ′⟩ Π_m ⟨φ_m, φ′_m⟩ + Σ_m ⟨φ_m, [H₁, J₁] φ′_m⟩ (…)`,
  where `H₂`, `J₂` are the pair's generator and current, built from the two-record parts of the interaction and placement. The same holds for exchange-symmetrized states, term by term.
- **Contradiction.** If `[H_N, J_N] = 0`, the left side vanishes. With `[H₁, J₁] = 0` and `φ′_m = φ_m` normalized, `⟨ψ, [H₂, J₂] ψ′⟩ = 0` for a dense set of `ψ, ψ′`, so `[H₂, J₂] = 0`. This contradicts the theorem above. The step that commutators of sums over separated clusters are sums of cluster commutators is runner I1. ∎

## Theorem T3 — no conserved local two-step momentum either

*Statement.* Under the premises of the theorem, let `Π′` be any operator whose fiber form is `g + i[h₀, m′] + F₂′`, with `m′` a bounded finite-range one-body change and `F₂′` of finite rank with trigonometric-polynomial columns. This covers the total two-step momentum `Σ P^B` in any placement of block 143's class. Then `[H′, Π′] ≠ 0`, and the same holds for any number of records.

*Proof.* The proof of the theorem, S0–S7, uses `j″` only through that form and through `[h″, j″] = 0`. Replace `j″` by `Π′″ = Π′ ⊕ μΠ₀` and repeat it word for word. T2's reduction applies unchanged, since a free record's two-step momentum commutes with its generator. ∎

So under one record per site the records conserve their energy locally, but neither their energy current nor any local two-step momentum. The member's lapse needs the first, and its shift needs the second.

## Consistency

- **The line.** On `ℤ` each shell is two points carrying one value of `g` (block 143 T4). S3's density step has nothing to act on, which matches block 137's kept current on the infinite line.
- **Free records.** Without exclusion the same chain shows that a kept current forces transparency and `Δ = 1`. That forbids eigenvalues off the free spectrum near `K₀`, not every interaction: for example `h″ = Uh₀U*`, with `U − 1` of finite rank commuting with `g`, keeps `j″ = UgU*` and has `Δ = 1`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 143 (landed): the unrestricted local-interaction no-go remains deferred pending the analytic bridge"
source_of_blocker_text: block 143's landed claim scope (25b8c1874f); the landing review record unit-29
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "exponentially decaying interactions (determinants of trace-class perturbations); the long-range pull with exclusion; what the member sees when the books fail; an other-family referee"
conditional_surface_status: "two records; bounded interactions of finite relative range; placements in block 143's class; K near K0"
hypothetical_axiom_status: "the walk, one record per site, the interaction and the placement are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk. Block 78: one record per site.
  - Blocks 121 and 137: the exclusion's compression, and the loss of the energy current.
  - Block 140: the two-step momentum as the free current.
  - Block 143: the shell geometry (T1), the removed states (T4), the nondegenerate stationary points and cone tilts (T6), and the conditional no-go.
- **Probes.** #9251 (Claude Opus 5.5 worker, the supervisor's own model family; not refereed by another family) found the proof, with its own exact checker (7 checks). Its route: Fatou boundary values, the Morse lemma, M. Riesz's theorem, the Paley–Wiener theorem and Sylvester's identity, in place of block 143's wave operators and threshold bounds. The supervisor read every step and reran that checker; this note's runner checks the algebraic steps independently. #9249 (same family) found the first-order version for the long-range pull without exclusion.
- **In the literature.** Perturbation determinants and the scattering matrix (the Birman–Krein relation, which this proof avoids); Hardy spaces and the Paley–Wiener theorem; Fredholm determinants for trace-class perturbations; lattice scattering of two particles. Reference only.
- **New here:** the no-go within the finite-range class, without wave operators, time averages, shell kernels or complex threshold bounds; the one-body lemma S1.
- **Provenance.** A harvest of a same-family probe result, line-checked by the supervisor. No other model family has refereed it.

## Exact target and obligation graph

Target: `[h′(K), j′(K)] ≠ 0` for almost every `K` in a neighbourhood of `K₀`. The obligations are:
- (O1) the one-body placement current vanishes if the current is kept (S1: proved here);
- (O2) the resolvent identity and its shell sandwich (S2: proved here, runner C1);
- (O3) transparency at almost every energy (S3: proved here from the spectral theorem, boundary values of transforms of finite measures, block 143 T1 and the identity theorem);
- (O4) the determinant's reality (S4: proved here, runner D1);
- (O5) bounded spectral densities near `K₀` (S5: proved here from block 143 T6, the coarea formula and the quadratic normal form);
- (O6) `Δ = 1` (S6: proved here from the `H^p` bound on transforms, products of `H^p` functions, and the uniqueness of `H²` boundary values);
- (O7) `Δ(λ) = 0` at the removed states (S7: block 143 T4, runner H1);
- (O8) the reduction from `N` records to the pair (T2: proved here; runner I1 for the commutator of cluster sums);
- (O9) the momentum (T3: the same proof, since only the form of `j″` is used).

The strongest step not checked by a runner is O5, the volume bounds near cones and stationary points; it is proved in the text.

## No-Go Discipline Gate

The note's negative sentence: no bounded interaction of finite relative range and no placement in block 143's class keeps two excluded records' total energy current, on the plane or in space.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A one-body placement change compensates the collision.* It is forced to vanish before any collision is considered (S1; runner B1–B2). ATTEMPTED.
2. *The collision scatters, but only into states with the same total current.* The resolvent identity makes every on-shell amplitude between different values of `g` vanish, and `g` separates a dense set of shell pairs (S2–S3; runner C1). ATTEMPTED.
3. *Eigenvalues or thresholds hide the scattering.* Eigenvalues are countable, and thresholds are handled by bounded densities (S3, S5). ATTEMPTED.
4. *The determinant has a zero or pole where no bound applies.* It lies in `H²` of both half-planes with equal boundary values, so it is one (S4–S6; runner D1). ATTEMPTED.
5. *The removed states are not seen by the determinant.* They are exact eigenvalues of the extended generator off the spectrum, so they are zeros of `Δ` (S7; runner H1). ATTEMPTED.
6. *The line escapes.* It does, and the note says so: the shells are two points with one value of `g` (Consistency). ATTEMPTED.
7. *Many records compensate the pair.* Separating all but two records reduces a kept current exactly to the pair's (T2; runner I1). ATTEMPTED.
8. *A different local momentum is conserved.* Any operator of the current's form, including the total two-step momentum in any local placement, fails the same way (T3). ATTEMPTED.

Scope left open: interactions of infinite range (including exponentially decaying ones, which need determinants of trace-class perturbations); placements whose currents are not of finite rank off the free one; the long-range pull with exclusion.

### N2 — Wall-independence audit
No no-go wall of the repository is used. The inputs are block 143's exact T1, T4 and T6.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". Every analytic step names its standard theorem under Premises. The finite rank of `F₁` and `F₂` follows from the finite relative range, stated as a premise. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 78 (landed) | the walk; one record per site | yes (restated) |
| blocks 121, 137 (landed) | the compression; the books need `J′` kept | yes (restated) |
| block 140 (landed) | the free current is the two-step momentum | yes (restated) |
| block 143 (landed) | T1, T4, T6 | yes (T1 and T6 recomputed in part: runner E1) |
| probes #9251 (unrefereed, same family) | the proof's route | yes (re-derived and line-checked here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no finite-range interaction keeps two excluded records' total energy current" | executed: the one-body double-commutator identity and the partial trace | executed: the resolvent identity and shell sandwich in an exact finite model | executed: push-through, determinant product, the determinant identity and conjugation | executed: block 143's T1 minor and T6 cone tilts recomputed; the removed state's zero | almost every `K` near `K₀`; the analytic steps proved in the text |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration. Partial routes that stay open: exponentially decaying interactions (the same chain with determinants of trace-class perturbations), and more than two records.

### N7 — Steelman
- *Objection:* "The proof leans on block 143 T6 at one wave vector; the bounded densities might fail elsewhere."
  - *Reply:* The no-go needs a set of `K` of positive measure, and T6's nondegeneracy persists on a neighbourhood of `K₀`. A current kept for every `K` would have to be kept there.
- *Objection:* "A placement outside block 143's class might keep the current."
  - *Reply:* Placements whose current differs from the free one by more than a finite-rank operator are outside the theorem, and the note says so. S1 shows that one-body changes cannot help.

### N8 — Cross-cycle echo
- Block 137: the excluded pair loses its energy current at a single collision.
- Block 141: no neighbour coin term restores it.
- Block 143: exact kinematics and a conditional no-go.
- This note: the unconditional no-go within the finite-range class.

## Falsifiers

- A bounded interaction of finite relative range and a placement in block 143's class with `[H′, J′] = 0` on `ℤ²` or `ℤ³`.
- An error in the resolvent identity, the determinant identities or the recomputed inputs.
- A gap in S3's density argument or S5's volume bounds.

## Boundaries and non-claims

- Bounded interactions of finite range; placements in block 143's class; any number of records (T2). Infinite-range interactions and non-local placements are not covered.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 78, 121, 137, 140 and 143 (landed), restated or recomputed in part.
- Named standard imports, at definition level: the spectral theorem; boundary values of Borel transforms (Fatou and de la Vallée Poussin); the coarea formula; the Morse lemma; M. Riesz's theorem and Hölder's inequality; the Paley–Wiener theorem; direct-integral decompositions; the identity theorem for real-analytic functions; Sylvester's determinant identity.

## Review record

- **Who and when.** Supervisor-run harvest block, 2026-09-26, during the owner's 12-hour campaign of that day.
- **Provenance.** The proof is probe #9251's (Claude Opus 5.5 worker `w-macbookpro9927a-j84a4`, the supervisor's own model family). The supervisor read every step (S0–S7) against block 143's landed text, reran the probe's exact checker (7/7), and wrote this note's runner independently. No other model family has refereed it.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 143's deferred bridge, #9249 (the long-range pull without exclusion) and no other attempt at the unrestricted no-go.
- **Line-check notes.** S3 needs the shell components to be analytic, which holds for almost every energy since the cones and stationary values are finitely many near `K₀`. S4's `X = 0` uses that `Γ^{1/2}` is invertible on the range of `Γ`. S6's `H²` membership uses the uniform local `L²` bounds and the `O(|z|^{−k})` decay together.
- **After the first push (2026-09-26).** T2, the reduction from any number of records to the pair, was added by the supervisor, with runner I1. T3 followed: the proof uses only the form of the current, so the total two-step momentum in any local placement is not conserved either.
- **Independence.** Mutation census: one mutation per science family (B, C, D, E, H, I), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_finite_range_interaction_keeps_two_excluded_records_total_energy_current_on_the_plane_or_in_space_2026_09_26.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
