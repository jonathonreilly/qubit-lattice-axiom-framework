---
claim_id: admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_the_flat_band_theorem_and_a_walk_clocked_to_relative_eps_squared_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clock clause of blocks 53 and 54 (a site's rate is a local clock w_x; block 54's walk hops on bonds timed by sqrt(w_x w_y); as landed on main its translation identity is a finite-power identity whose evolution form is conditional on a realization not established there), run in discrete ticks. Exact: (T1) the partial-swap walk - rotations exp(-i eps_b sigma_x) on the pairs {(up,x),(down,x+1)} then {(down,x),(up,x+1)}, bond angle eps_b = eps0 sqrt(w_x w_(x+1)) - is unitary with range 2 for every clock field, equals two ticks of the coined walk at coin angle pi/2 - eps (so it is the square of a range-1 step), and its first-order generator is, after the gauge psi_x -> i^x psi_x, twice block 54's clocked line walk; (T2) at a uniform angle sin(omega/2) = sin eps |cos k|, omega = 2 eps |cos k|(1 - (eps^2/6) sin^2 k) + O(eps^5): the frequencies follow the local clock to relative eps^2; the rays obey dv/dt = (2v^2 + Psi) d_x log w with Psi in closed form, block 54's law plus O(eps^4); (T3) this walk has no exact clock: tr U(2 eps)/2 - cos 2 omega(eps) = 2 sin^4 eps sin^2 2k, and for any field U[w]^2 reaches four sites while U[2w] reaches two; (T4, the flat-band theorem) a translation-invariant unitary on l^2(Z^d; C^N) of range R whose first N((2R+1)^d + 1) powers keep range R, or whose eigenphases scale exactly with a clock over an interval, has a spectrum independent of k and never moves a walker more than (N-1)R sites; a local, covariant rule continuous in the clocks that obeys the discrete clock identity for all integer ratios up to that bound in exponential gradients has flat bands; the bound is attained by the range-1 group cos c - i sin c H with H^2 = 1. EXECUTED, NOT CLAIMED: a packet in a clock gradient follows the exact discrete rays (0.21 of 326.6 sites), not block 54's law (off 2.1). From probes workers (Claude Opus 5.5 and Claude Opus 5), refereed by another model family (a Grok model). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_2026_09_23.py
---

# In discrete ticks a local clock is exact only for walks that do not move: the flat-band theorem, and a partial-swap walk that follows block 54's clock to relative ε²

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within the supplied clock clause; probes workers' results refereed by another model family; nothing adopted or registered; unaudited)

This note works within the supplied clock clause of blocks 53 and 54 (a site's rate is a local clock; the walk hops on bonds timed by the geometric mean of their ends); it reports, from a probes worker's result refereed by another model family, what happens to that clause when time comes in discrete ticks; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 54 (#8570) put possibility's walk on local clocks, every bond timed by the geometric mean of its ends' rates, in continuous time. Its PR text read a translation identity as "a packet moved up a uniform clock gradient by `a` does everything `λ_a` times faster". As landed on main (c3f8c47a58), the identity is a finite-power identity on finite-support amplitudes; the evolution form needs a self-adjoint realization that is not established, and the exact packet force is withdrawn. The question here is whether the walk can run in discrete ticks and keep the clock exactly, in the discrete form of that identity.

Two probes workers answered, and a referee of another model family (a Grok model) checked both.
- Attempt a1 (`w-jonathonsmac4f50-j0f4f`, Claude Opus 5) showed that three natural formulations fail:
  - a coin angle acts as a mass;
  - a fraction of a tick is not unitary;
  - the `w`-th power of a step is not local.
- Attempt a3 (`w-macbookpro90c72-jf02d`, Claude Opus 5.5) found the best formulation available, together with a general no-go.

- **T1: the partial-swap walk.** Each tick rotates the pairs `{(up, x), (down, x+1)}`, then `{(down, x), (up, x+1)}`, by the bond's angle `ε_b = ε₀√(w_x w_{x+1})`.
  - It is unitary, with range two, for every clock field.
  - It is exactly two ticks of the coined walk at coin angle `π/2 − ε`, so it is the square of a range-one step.
  - Its first-order generator is block 54's clocked walk.
- **T2: a clock to relative `ε²`.** At a uniform angle, `sin(ω/2) = sin ε |cos k|`, so `ω = 2ε|cos k|(1 − (ε²/6)sin²k) + …`. Every frequency follows the local clock up to a relative `ε²`. The rays obey block 54's law plus a closed-form correction of order `ε⁴`.
- **T3: but not exactly.** Doubling every bond angle is not two ticks: `tr U(2ε)/2 − cos 2ω(ε) = 2 sin⁴ε sin²2k`. For any field, two ticks reach four sites, while the doubled step reaches two.
- **T4: the flat-band theorem.** Consider a unitary step of finite range that commutes with translations. Suppose its powers up to a fixed number stay within that range, or its eigenphases scale exactly with a clock over an interval. Then its bands are flat and it never moves a walker more than a bounded distance.
  - Consequently, a local, covariant rule that obeys the discrete clock identity exactly in exponential gradients moves nothing.
  - The bound is attained: the group `cos c − i sin c H` with `H² = 1` is exactly clocked, has range one, and moves nothing.

**Executed control (not claimed).** A packet runs 400 ticks in a clock gradient. It follows the exact discrete rays to `0.21` of the `326.6` sites it travels, and misses block 54's continuous law by `2.1`: the `ε²` term is seen.

In plain terms: if time comes in ticks and each place keeps its own clock, then a walker cannot move while ticking exactly at its local rate. It can do so only approximately, with an error that grows as the square of how much happens per tick. In ticks, an exact local clock needs a walker that stays put; whether continuous time allows one is block 54's open realization question.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". Steps and clocks are therefore supplied clauses. Nothing is adopted.
- **Block 53's clock clause** (#8568, open): positive local rates `w_x`, scale covariant.
- **Block 54's walk** (#8570, open).
  - On the line, `(T_eψ)(x) = ψ(x − e)` and `D = (i/2)(T − T†)`, with symbol `sin k`; the walk is `σ D`.
  - The clocked walk is `H_w = W^{1/2} H W^{1/2}`, with every bond carrying `√(w_x w_y)`.
  - The translation identity (T3), as landed on main, says that if `w(x + a) = λ_a w(x)`, then `H_w^n T_a = λ_a^n T_a H_w^n` on finite-support amplitudes; the evolution form `U_w(t) T_a = T_a U_w(λ_a t)` is conditional on a self-adjoint realization not established there.
  - The ray law (T4) is `dv/dt = −w²(ε²/2)″ ∂_x log w + 2v² ∂_x log w` for `E = w(x)ε(k)`.
- **Discrete ticks.**
  - A step is a unitary `U[w]` on `ℓ²(Z; C²)` (two components, up and down), depending on the clock field.
  - Its range is the largest distance between sites it connects.
  - Its symbol `Û(k)` is its matrix on plane waves.
  - The discrete clock identity is `U[w] T_a = T_a U[w]^m` for a gradient with `λ_a = m`.
- **Provenance.**
  - a3 is by worker `w-macbookpro90c72-jf02d` (Claude Opus 5.5), and a1 by `w-jonathonsmac4f50-j0f4f` (Claude Opus 5). Both are the same family as the supervisor.
  - The referee of a3, `w-macbookpro90c72-j7daf`, and the referee of a1, `w-macbookpro90c72-j991c`, are Grok models, another family. They confirmed a3's S1–S6, including the flat-band proof, and a1's three failures.
- **Names.** Block 54's `σ_a` are the Pauli matrices. The ray equations are Hamilton's. The symbol `Û(k)` is the Bloch matrix. The two-layer product is a Trotter splitting, and its palindromic form is Strang's. The interpolation step uses the Vandermonde determinant.

## Theorem T1 — the partial-swap walk

*Statement.* Let `A[w]` be the product over bonds `b = (x, x+1)` of `exp(−iε_b X_b^A)`, where `X_b^A` swaps `(up, x)` and `(down, x+1)`. Let `B[w]` be the same with the pairs `{(down, x), (up, x+1)}`. Set `ε_b = ε₀√(w_x w_{x+1})` and `U[w] = B[w]A[w]`.
- (a) `U[w]` is unitary, with range two, for every positive clock field.
- (b) `U[w] = −G^{−1}(S R(θ))² G`, where:
  - `S` moves up by `+1` and down by `−1`;
  - `R(θ_x)` is the coin at `θ_x = π/2 − ε_{(x,x+1)}`;
  - `G` shifts the down component by `−1` and multiplies it by `−i`.

  So `U = V²` with `V = iG^{−1}S R G` of range one. The coin angle acts as a rate near `π/2`, read every second tick, and as a mass near `0` (a1).
- (c) The first-order generator has symbol `2 cos k σ_x`. The gauge `ψ_x → i^xψ_x` turns it into `2 sin k σ_x`. So `U[w] = 1 − iε₀·2(σ_x D)_w + O(ε₀²)`: to first order the step is block 54's clocked walk.

*Proof.*
- (a) Each layer is a product of commuting rotations on the pairs of a perfect matching, so it is unitary for any angles. An amplitude reaches at most two sites.
- (b) `R(π/2 − ε) = (−iσ_y)exp(iεσ_y)`, `Y S Y = S^{−1}`, and conjugation by `G`.
- (c) The layer generators sum to `σ_x ⊗ (T + T†)`, and `G T G^{−1} = iT`.
- The runner checks (a) and (b) exactly on a ring of six sites with six different rational angles, and (c) symbolically (family B). ∎

## Theorem T2 — a clock to relative `ε²`, and the rays

*Statement.*
- At a uniform angle `ε`, `tr Û/2 = 1 − 2 sin²ε cos²k` and `det Û = 1`, so `sin(ω/2) = sin ε |cos k|`.
- `ω = 2ε|cos k|(1 − (ε²/6)sin²k) + O(ε⁵)`, and `ε ∂_ε ω = ω(1 − (ε²/3)sin²k + …)`. With `ε = ε₀w`, every frequency follows the local clock up to a relative `ε²`.
- Any separable `ω = w(x)f(k)` obeys block 54's ray law exactly. The walk's own rays obey `dv/dt = (2v² + Ψ)∂_x log w` with `Ψ = 4 sin ε(ε cos ε − 2 sin ε sin²k)/(1 − sin²ε cos²k)`. This is `Ψ = 4ε² cos 2k + (ε⁴/3)(2 cos 2k + 3 cos 4k − 1) + O(ε⁶)`: with `k′ = k + π/2`, block 54's law for `E = 2ε|sin k′|`, plus a term of order `ε⁴`.

*Proof.*
- The pair symbols are involutions, so each layer is `cos ε − i sin ε M`.
- The series and the ray identity are symbolic, on both branches of `|cos k|` (family C). ∎

## Theorem T3 — this walk has no exact clock

*Statement.*
- `tr Û(2ε)/2 − cos 2ω(ε) = 8 sin⁴ε cos²k sin²k = 2 sin⁴ε sin²2k`. This is nonzero unless `sin ε sin 2k = 0`.
- For any field, `⟨up, x+4|U[w]²|up, x⟩ = Π_{j=0}^{3} sin ε_{(x+j, x+j+1)}`, while `U[2w]` has range two.
- So `U[2w] ≠ U[w]²`, and the discrete clock identity fails at ratio two.

*Proof.*
- With `s = sin ε` and `c = cos k`: `sin²2ε = 4s²(1 − s²)`, and the difference factors as `8s⁴c²(1 − c²)`.
- The matrix element counts the one path of length four: up two sites, twice.
- Both are checked exactly, the second on a ring of ten sites with ten different angles (family D). ∎

## Theorem T4 — the flat-band theorem

*Statement.* Let `V` be a unitary on `ℓ²(Z^d; C^N)` that commutes with translations and has range `R`, measured in the max-norm.
- (a) Suppose `V, V², …, V^M` all have range `≤ R`, where `M = N((2R+1)^d + 1)`. Then:
  - the eigenvalues of the symbol `V̂(k)`, with multiplicity, do not depend on `k`;
  - every power `V^n` has range `≤ (p − 1)R`, where `p` is the number of distinct eigenvalues.

  So `V` never moves a walker more than `(N − 1)R` sites.
- (b) The same conclusion holds if `V_c` has range `≤ R` for all `c` in an open interval, and there are real functions `f_b` with the eigenvalues of `V̂_c(k)` equal to `e^{−icf_b(k)}` (exact clock scaling).
- (c) Let a rule `w ↦ U[w]` be of range `≤ R` for every field, translation covariant, and continuous in the clocks within a fixed distance. Suppose it satisfies `U[w]T_a = T_aU[w]^m` near the origin for the fields `w = c e^{gx}`, `g = (log m)/a`, for every `c > 0`, every `a ≥ 1` and every `m = 2..M`. Then every uniform-clock step `U[c]` has flat bands.
- (d) The bound cannot be improved from "flat" to "trivial". `H = [[0, e^{−ik}], [e^{ik}, 0]]` has `H² = 1` and eigenvalues `±1` at every `k`. `e^{−icH} = cos c − i sin c H` is a group of range-one steps with exact clock scaling, and it moves nothing beyond one site.

*Proof.*
1. **Interpolation.** A trigonometric polynomial of degree `≤ R` in each variable is fixed by its values at `(2R+1)^d` distinct grid nodes; in one variable this is the determinant of powers of distinct points.
2. **Traces.** `tr V̂(k)^m` is such a polynomial for `m ≤ M`. So `Σ_b z_b(k)^m = Σ_i ℓ_i(k)Σ_b z_b(k_i)^m`, where the `z_b` are the eigenvalues and the `ℓ_i` are the interpolation weights.
3. **Finitely many eigenvalues.** Collect the at most `M` distinct values among `{z_b(k)}` and `{z_b(k_i)}`. The power-sum system is invertible, since the values are distinct and nonzero. So every eigenvalue at every `k` lies among the node values. In case (b), use the derivatives in `c` at one point of the interval instead of the powers.
4. **Constancy.** The characteristic polynomial is continuous in `k` and takes values in a finite set, so it is constant on the connected torus.
5. **No transport.** `V̂` is diagonalizable with constant eigenvalues `s_q`. The spectral projections `Π_{r≠q}(V̂ − s_r)/(s_q − s_r)` have range `≤ (p − 1)R`, and `V^n = Σ_q s_q^n P_q`.
6. **Part (c).** Covariance turns the identity into `U[mw] = U[w]^m` near the origin. As `a → ∞`, continuity gives `U[mc] = U[c]^m`, and (a) applies.

The runner checks the ingredients and the sharp example (family E):
- the interpolation determinants for `R = 1, 2, 3` at rational points of the circle;
- the group property and eigenvalues of `H`;
- that a moving walk escapes the hypothesis at once: the ranges of `U, U², U³` are `2, 4, 6` at the uniform angle with `cos ε = 3/5`. ∎

## Executed control

The script is `specs/supervisor_control_block105_packet.py`, the worker's executed part re-run; its output is in `.out.txt`.
- A line of 1600 sites with `ε = 0.6 e^{0.001(x−500)}`, and a packet of width 30 at `k = π/3` on the upper band.
- After 400 ticks the centroid has moved `−326.59` sites.
- The exact discrete rays of T2 give `−326.80`, off by `0.213`.
- Block 54's separable law gives `−324.47`, off by `2.118`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 54 (#8570): the clocked walk runs in continuous time; whether discrete ticks can keep the clock clause"
source_of_blocker_text: blocks 53, 54; probes derivation J:derive:discrete-step-walk-under-the-clock-clause (a1, a3; both refereed by another family)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "discrete ticks keep block 54's clock only to relative eps^2; an exact local clock needs continuous time or a walker that does not move; next: the three-dimensional partial-swap walk (a palindromic six-layer step), its dispersion and packets, and the sideways drift block 54 measured"
conditional_surface_status: "T1-T3 exact on the line for every clock field; T4 exact for every finite-range translation-invariant unitary in any dimension; the packet executed, not claimed"
hypothetical_axiom_status: "blocks 53 and 54's clock clause and walk are hypotheses; discrete ticks are a hypothesis; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 54** (#8570; landed in c3f8c47a58 as "Clocked nearest-neighbour amplitudes: finite operator identities and conditional ray motion") gave the clocked walk, the bond timing, the finite-power translation identity and the conditional ray law, in continuous time; the owner's review withdrew the exact packet force. **Block 53** (#8568; landed in c3f8c47a58) gave the clock clause and its "no master clock" covariance.
- **Block 57** (#8578) found that the time parameter is a label: kinetic terms see only rate differences.
- **Block 96** (#8866) found that waves need a coupling time reversal flips; the walk is such a coupling.
- **Blocks 26 and 90–94** worked formation in discrete levels. This note is about the walk, not formation.
- **The literature.** Discrete-time unitary walks are the quantum walks of the literature, and the coined walk is the standard form. The two-layer product is a Trotter splitting and its palindromic form Strang's. The power-sum argument uses the Vandermonde determinant. None is used as authority.
- **New here,** from the probes workers and their referees:
  - the partial-swap walk as the clocked walk in ticks, with its exact dispersion and ray law;
  - the exact failure at ratio two;
  - the flat-band theorem and its sharp example;
  - a1's three failed formulations.

## Exact target and obligation graph

Target: whether block 54's clock clause survives discrete ticks. The obligations are:
- (O1) a unitary local step for every clock field;
- (O2) its relation to block 54's walk;
- (O3) how well it keeps the clock;
- (O4) whether any local step keeps it exactly.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- (i) the partial-swap walk has no exact clock;
- (ii) no finite-range unitary that moves packets has exact clock scaling;
- (iii) no local covariant continuous rule obeys the discrete clock identity exactly unless its bands are flat.

### N1 — Routes by which the sentences could fail or mislead
1. *Ranges that grow with the clock.* T4 assumes a uniform range. A step whose range grows with `w` is not local in the axioms' sense.
2. *Rules discontinuous in the clocks.* T4(c) uses continuity in the nearby clocks. A rule that switches formulations at thresholds escapes (c), not (a) or (b).
3. *Non-periodic tick schedules.* a1's fraction-of-ticks schedules with angles in `{0, π/2}` are unitary tick by tick. T4 applies to them only through their period products.
4. *Continuous time.* T4 says nothing against continuous time. Whether block 54's continuous-time walk keeps the clock exactly depends on a self-adjoint realization that block 54, as landed, leaves open.
5. *Three dimensions.* T4 holds in any dimension. The three-dimensional partial-swap walk (a3's plan: six layers, palindromic) is not worked here.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The clock clause and the walk are supplied, and the tick formulation is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 53, 54 (#8568, #8570) | the clock clause; the walk, its identity and its ray law | yes |
| blocks 26, 57, 90–94, 96 | placement | no |
| probes workers `w-macbookpro90c72-jf02d`, `w-jonathonsmac4f50-j0f4f`; referees `w-macbookpro90c72-j7daf`, `w-macbookpro90c72-j991c` | the results; the confirmations | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "in discrete ticks a local clock is exact only for walks that do not move; the partial-swap walk keeps block 54's clock to relative ε²" | executed: the one-bond rotations and the two-by-two symbols; the dispersion, its series and the ray law (symbolic) | executed: the step on rings of 6, 10 and 12 with exact rational angles: unitarity, range, the two-tick identity, the four-site element | executed: the doubling defect `2 sin⁴ε sin²2k`; the interpolation determinants for `R = 1, 2, 3`; control: a packet in a clock gradient | executed: the sharp flat-band example; the ranges of `U, U², U³` of a moving walk | T1–T3 for every clock field on the line; T4 for every finite-range translation-invariant unitary in any dimension (proof); block 54 supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Nobody said time is discrete." *Reply:* Right. The note makes no claim that it is. It says what a discrete tick costs: exact local clocks go, and the clock is kept only to relative `ε²`. That is a sharp statement about a reading of the axioms that no text excludes.
- *Objection:* "Flat bands are a technicality." *Reply:* T4(d) shows the conclusion is sharp. An exactly clocked group of local steps exists, and it moves nothing.

### N8 — Cross-cycle echo
- Block 53 set the clock.
- Block 54 put the walk on it, in continuous time.
- Block 96 found that waves need the walk.

This note adds that in ticks the walk and the clock agree only approximately.

## Falsifiers

- A finite-range translation-invariant unitary with non-constant spectrum whose powers up to `N((2R+1)^d + 1)` all have range `≤ R`.
- A local, covariant, continuous tick rule that moves packets and satisfies `U[mw] = U[w]^m` for all integer `m` up to the bound.
- A different closed form for `sin(ω/2)` or for `Ψ`.

## Boundaries and non-claims

- The clock clause, the walk and discrete ticks are supplied, not adopted.
- T1–T3 are on the line; T4 is in any dimension.
- Nothing is claimed about whether time is discrete, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 26, 53, 54, 57, 90–94 and 96 (PRs), restated or placed.
- Named standard imports, at definition level:
  - the Pauli matrices;
  - Hamilton's ray equations;
  - the Bloch matrix;
  - the Trotter and Strang splittings;
  - the Vandermonde determinant;
  - the continuity of polynomial roots;
  - the diagonalizability of unitary matrices;
  - exact rational and symbolic arithmetic;
  - in the control, floating-point stepping.

## Review record

- **Who and when.** Supervisor-run block, the fifty-third since the source-link direction opened, built from probes workers' results with other-family referees.
- **Provenance.**
  - a3: worker `w-macbookpro90c72-jf02d` (Claude Opus 5.5). Referee `w-macbookpro90c72-j7daf` (a Grok model) confirmed S1–S6 with no broken step. The 3D walk and the sideways drift remain open.
  - a1: worker `w-jonathonsmac4f50-j0f4f` (Claude Opus 5). Referee `w-macbookpro90c72-j991c` (a Grok model) confirmed the three failures. It corrected a factor in a1's prose that does not change the conclusion.
  - The supervisor re-ran a3's check and ported it. It replaced a floating comparison with the exact identity `2 sin⁴ε sin²2k`, used rational circle points for the interpolation determinants, and re-ran the packet as the control.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.

## Corrigendum 2026-09-23 (after the owner's landings)

Block 54 was landed on main in c3f8c47a58 with its evolution identity left conditional and its exact packet force withdrawn. This note now cites the landed finite-power identity, and no longer says that block 54's continuous-time walk keeps the clock exactly. T1–T4, and every check, are unchanged.
