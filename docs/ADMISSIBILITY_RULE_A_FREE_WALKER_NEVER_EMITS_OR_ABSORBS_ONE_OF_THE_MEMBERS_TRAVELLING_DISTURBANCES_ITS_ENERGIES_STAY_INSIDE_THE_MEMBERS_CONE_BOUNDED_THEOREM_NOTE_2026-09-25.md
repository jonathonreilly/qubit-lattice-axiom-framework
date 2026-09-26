---
claim_id: admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk, block 139's staggered mass and block 62's member with its lattice differences at the kinetic normalization alpha = K/4 of blocks 134 and 135, all as landed on main; unit rate. (T1) exact: the walker's energy is |s(k)| with s_j = sin k_j and the member's travelling disturbances have frequency |p(q)| with p_j = 2 sin(q_j/2); since s_j(k) - s_j(k - q) = 2 cos(k_j - q_j/2) sin(q_j/2), every energy difference obeys |E(k) - E(k - q)| < |p(q)| for q != 0 (mod 2 pi), strictly (where the first step is an equality, every component with q_j != 0 changes sign, so |s(k)| = |s(k - q)|; 32768 exact rational configurations checked). (T2) exact: with the staggered mass the energies sqrt(mu^2 + |s|^2) differ by no more than the |s| do, so massive walkers stay strictly inside too. (T3) hence no walker transition within one band emits or absorbs one of the member's travelling disturbances while keeping energy and lattice momentum; above the filled sea every single-excitation move is within a band, so no single walker or hole does; outside that scope a walker dropping to the other band can emit one (T5 run backwards; exact at q = (pi/3, 0, 0)), and so can two walkers scattering within the upper band (kinematically open); against the walker's own dispersion the strict inequality would fail at the edge of the zone, so the member's half-angle frequency is what keeps the walker inside. (T4) along an axis the two agree at first order and separate at third, sin q - 2 sin(q/2) = -q^3/8 + ...: one cone at long wavelength, the walker's inside the member's at the lattice scale. (T5) exact: T1-T4 concern a walker's own transitions within its band; the member's frequency is exactly the energy of a symmetric walker pair, |p(q)| = 2|s(q/2)|, and the pair energy |s(k)| + |s(k + q)| equals |s(q)| < |p(q)| at k = 0 and 2|cos(q/2)| at k_a = pi/2 - q_a/2, which exceeds |p(q)| if and only if sum_a cos q_a > 0; so, wherever the sea is filled, a disturbance with sum_a cos q_a > 0 can lift a walker out of the sea (pair creation is kinematically open; the rate is not computed; with the staggered mass the channel closes for |p(q)| < 2 mu). The supervisor's own derivation (Claude Opus 5.5); not refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_2026_09_25.py
---

# Within one band a free walker never emits or absorbs one of the member's travelling disturbances: its energies stay inside the member's cone at every lattice momentum

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact at every lattice momentum within the landed walk, staggered mass and member at `α = K/4`; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 62, 101, 134, 135 and 139 as landed on main (the walk, the member and its lattice differences, the kinetic normalization and the staggered mass); it reports where a free walker's energies sit against the member's travelling disturbances at every lattice momentum; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The landing review scoped `α = K/4` (blocks 134–135) as a necessary condition at linear order, not a universal light cone. This note asks what the walker and the member do at the lattice scale, where their dispersions differ.

- **T1: the walker's energies stay strictly inside the member's cone.**
  - The walker's energy is `|s(k)|` with `s_j = sin k_j`. The member's travelling disturbances have frequency `|p(q)|` with `p_j = 2 sin(q_j/2)`.
  - Since `s_j(k) − s_j(k − q) = 2cos(k_j − q_j/2) sin(q_j/2)`, every energy difference obeys `|E(k) − E(k − q)| < |p(q)|` for `q ≠ 0`, strictly.
- **T2: massive walkers too.** With the staggered mass the energies `√(μ² + |s|²)` differ by no more than the `|s|` do.
- **T3: no emission or absorption within one band.** No walker transition within one band emits or absorbs one of the member's travelling disturbances while keeping energy and lattice momentum. Above the filled sea every single-excitation move is within a band, so no single walker or hole does.
  - Outside that scope the channel opens. A walker that drops to the other band can emit one: that is T5 run backwards. Two walkers scattering within the upper band can also emit one.
  - The half-angle in the member's frequency is what keeps the walker inside. Against the walker's own dispersion the inequality would fail at the edge of the zone.
- **T4: one cone at long wavelength only.** Along an axis the two agree at first order and separate at third, `sin q − 2 sin(q/2) = −q³/8 + ⋯`. At the lattice scale the walker's cone lies inside the member's.
- **T5: but the filled sea can absorb.** T1–T4 concern a walker's own transitions within its band. The member's frequency is exactly the energy of a symmetric walker pair, `|p(q)| = 2|s(q/2)|`. The pair energy `|s(k)| + |s(k + q)|` equals `|s(q)| < |p(q)|` at `k = 0` and `2|cos(q/2)|` at `k_a = π/2 − q_a/2`, which exceeds `|p(q)|` if and only if `Σ_a cos q_a > 0`. So wherever the sea is filled, a disturbance can lift a walker out of it: pair creation is kinematically open. The rate is not computed. With the staggered mass the channel closes for `|p(q)| < 2μ`.

In plain terms: at long wavelengths the walker and the member's ripples share a top speed. At the lattice scale the ripples are faster, and every walker energy change is smaller than any ripple's energy with the same momentum. So a walker moving freely within its band can never shake off one of the member's ripples, and can never swallow one: energy and momentum cannot both balance. A walker that drops to the other band can, and so can two walkers that collide. The same ordering has a second face. A ripple carries exactly the energy of a pair of walkers moving apart symmetrically, so wherever the sea of walkers is filled, a ripple can turn into a walker and a hole in the sea. The sea can absorb what a single walker cannot.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its staggered mass, the member and its kinetic normalization are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed): `H = Σσ_aS_a`, with plane-wave symbol `Σσ_a sin k_a`, so energies `±|s(k)|`. With block 139's staggered mass, `±√(μ² + |s(k)|²)`.
- **The member's travelling disturbances** (blocks 62 and 101 as landed): on the lattice the member's differences have symbol `p_j = 2 sin(q_j/2)`, and its two transverse disturbances have `ω² = Kw̄²p²/(4α)`. At `α = K/4` (blocks 134–135) and unit rate, `ω = |p(q)|`.
- **Emission and absorption.** The coupling between content and member is translation invariant, so it keeps the total lattice momentum. One walker at `k` emitting or absorbing one disturbance at `q` would need `k → k ∓ q` with `E(k) = E(k ∓ q) ± ω(q)`.
- **Standard imports.** Exact symbolic and rational arithmetic.

## Theorem T1 — the walker's energies stay strictly inside the member's cone

*Statement.* For every `k` and every `q ≢ 0` (mod `2π`), `|E(k) − E(k − q)| < |p(q)|`, with `E = |s|`.

*Proof.*
- `s_j(k) − s_j(k − q) = 2cos(k_j − q_j/2) sin(q_j/2)` (runner B1). So `|s(k) − s(k − q)| ≤ |p(q)|`, since each `|cos| ≤ 1`.
- The triangle inequality gives `||s(k)| − |s(k − q)|| ≤ |s(k) − s(k − q)|`.
- Equality in the first step needs `k_j ≡ q_j/2` (mod `π`) wherever `sin(q_j/2) ≠ 0`, and there `s_j(k − q) = −s_j(k)` (runner B3). The other components are equal. So `|s(k)| = |s(k − q)|`, and the energy difference is `0 < |p(q)|`.
- Otherwise the first step is strict. Either way `||s(k)| − |s(k − q)|| < |p(q)|` for `q ≢ 0`, including where `s(k) = 0`.
- Runner B2 confirms the strict inequality at 32768 configurations with rational sines and cosines, by rational comparison. ∎

## Theorem T2 — massive walkers too

*Statement.* `|√(μ² + a²) − √(μ² + b²)| ≤ |a − b|`, so with the staggered mass `|E(k) − E(k − q)| < |p(q)|` as well. The staggered mass keeps lattice momentum only up to `(π, π, π)`, and `E(k − q − (π, π, π)) = E(k − q)` because `|s|` is unchanged by that shift, so the same bound covers those processes.

*Proof.* `(μ² + a²)(μ² + b²) − (μ² + ab)² = μ²(a − b)² ≥ 0`, and `(√(μ² + a²) − √(μ² + b²))² − (a − b)² = 2(μ² + ab − √(μ² + a²)√(μ² + b²)) ≤ 0` (runner C1). With `a = |s(k)|`, `b = |s(k − q)|`, use T1. ∎

## Theorem T3 — no emission or absorption

*Statement.* No walker transition within one band, massless or massive, emits or absorbs one of the member's travelling disturbances while keeping energy and lattice momentum. Above the filled sea every single-excitation move, a walker above the sea or a hole in it, is within a band, so none does. Two processes lie outside this scope:
- (i) *an interband drop.* A walker at `k` in the upper band dropping to `k − q` in the lower band emits `q` when `|s(k)| + |s(k − q)| = |p(q)|`. That is T5's pair channel run backwards. At `q = (π/3, 0, 0)` the balance `|s(k)| + |s(k − q)| − |p(q)|` is `√3/2 − 1 < 0` at `k = q` and `√11 − 1 > 0` at `k = (2π/3, π/2, π/2)`, so it has a root.
- (ii) *two walkers.* `(π/2, 0, 0) + (−π/2, 0, 0) → (a*, 0, 0) + (π/3, 0, 0)`, plus a disturbance at `q = (−a* − π/3, 0, 0)`, keeps energy and lattice momentum with every walker in the upper band. Here `a*` is the one root in `(0, π/6)` of `sin a + √3/2 + 2 sin((a + π/3)/2) = 2`.

With the walker's own dispersion `|s(q)|` in place of `|p(q)|`, the strict inequality fails: in one dimension at `k = q = π/2` the difference is `1 = |sin q|`.

*Proof.* Within one band, T1 and T2 exclude `E(k) = E(k ∓ q) ± ω(q)` for `q ≢ 0`. The control is runner E1. (i) is runner E3: the balance changes sign between the two points, by rational comparison of squares, and is continuous on the torus. (ii) is runner E4: the balance `f(a) = sin a + √3/2 + 2 sin((a + π/3)/2) − 2` has `f(0) = √3/2 − 1 < 0 < f(π/6) = √3/2 + √2 − 3/2`, and `f′(a) = cos a + cos((a + π/3)/2) > 0` on `[0, π/6]`. ∎

## Theorem T4 — one cone at long wavelength only

*Statement.* Along an axis, `sin q − 2 sin(q/2) = −q³/8 + O(q⁵)`. The two agree at first order, one cone at long wavelength. Beyond it the walker's energy is below the member's frequency.

*Proof.* Series (runner D1). ∎

## Theorem T5 — the filled sea can absorb

*Statement.* T1–T4 concern transitions within one band. For transitions from the filled sea's band to the walker's band (pair creation):
- (a) the member's frequency is exactly the energy of a symmetric pair: `|p(q)| = 2|s(q/2)|`;
- (b) the pair energy `|s(k)| + |s(k + q)|` equals `|s(q)| < |p(q)|` at `k = 0`, and `2|cos(q/2)|` at `k_a = π/2 − q_a/2`, which exceeds `|p(q)|` if and only if `Σ_a cos q_a > 0`;
- (c) hence, by continuity, a disturbance with `Σ_a cos q_a > 0` can lift a walker out of the filled sea with energy and lattice momentum kept. This covers every small `q`.
- With the staggered mass every pair costs at least `2μ`, so the channel is closed for `|p(q)| < 2μ`.

Whether the member couples to the sea's pairs with a nonzero amplitude, and at what rate, is not computed here.

*Proof.* (a) by definition, since `2|sin(q_a/2)|` is `|s_a(q/2)|` doubled. (b) `sin(π/2 ∓ q_a/2) = cos(q_a/2)`, and `4cos²(q_a/2) − 4sin²(q_a/2) = 4cos q_a` (runner E2, with an exact example `1728/625 < 108/25 < 192/25`). (c) the pair energy is continuous on the torus. ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "landing review of blocks 134-135: alpha = K/4 is a necessary condition at linear order, not a universal light cone; how the walker and the member compare at the lattice scale"
source_of_blocker_text: the landing review (ef918c1910; unit 27); blocks 62 and 134-135 (landed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "two walkers and one disturbance (scattering through the member); records under exclusion; an other-family referee"
conditional_surface_status: "every lattice momentum on Z^3; one walker and one disturbance; the member at alpha = K/4 and unit rate"
hypothetical_axiom_status: "the walk, its staggered mass, the member and its normalization are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 62: the member's lattice differences and its two travelling disturbances.
  - Block 101: the member's quadratic action.
  - Blocks 134–135: `α = K/4`.
  - Block 139: the staggered mass.
  - Block 140: the walk's long-wave kinematics.
- **Probes.** None before this note. After it (all Claude Opus 5.5 workers, the same model family as the supervisor; none refereed by another family):
  - #9261 re-checked T1–T5. It gave the equality argument now in T1's proof, which also covers `s(k) = 0`; the earlier clause "s(k − q) a nonnegative multiple of s(k)" omitted that case. It found T3's two exceptions.
  - #9256 found that T5's channel has a nonzero single-disturbance amplitude at an exact non-symmetric resonance, and that the amplitude vanishes at the symmetric resonances `k = q/2 + πν`. The rate is still not computed.
- **In the literature.** A particle that moves slower than the waves it couples to cannot emit or absorb them singly; the kinematic condition behind radiation by fast particles in a medium. Reference only.
- **New here:**
  - T1: the strict inequality at every lattice momentum.
  - T2: the staggered-mass extension.
  - T3: the consequence within one band, its two exceptions, and the control that the member's half-angle frequency is what makes it hold.
  - T4: the third-order separation of the two cones.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: where a free walker's energies sit against the member's travelling disturbances at every lattice momentum. The obligations are:
- (O1) the inequality and its strictness (T1);
- (O2) the massive case (T2);
- (O3) the consequence within one band, its exceptions and the control (T3);
- (O4) the long-wave agreement (T4);
- (O5) transitions out of the filled sea (T5).

T1–T5 discharge them.

## No-Go Discipline Gate

The note's negative sentence: no walker transition within one band emits or absorbs one of the member's travelling disturbances.

### N1 — Routes by which the sentence could fail or mislead
1. *One walker, one disturbance, within one band.* Processes with two walkers or two disturbances are not excluded: two walkers scattering within the upper band can emit one (T3(ii)). An interband drop can emit (T3(i)), and pair creation out of the filled sea is kinematically open (T5).
2. *The member's normalization.* At `α ≠ K/4` the frequency is `|p|·√(K/(4α))`. For `α > K/4` the member's disturbances are slower and the conclusion can fail at long wavelength.
3. *The coupling* is assumed translation invariant, so lattice momentum is kept.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, mass, member and normalization.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 139 (landed) | the walk and its staggered mass | yes (restated) |
| blocks 62, 101 (landed) | the member's lattice differences and disturbances | yes (restated) |
| blocks 134, 135 (landed) | `α = K/4` | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "within one band a free walker never emits or absorbs one of the member's travelling disturbances" | executed: the difference identity | executed: 32768 rational configurations | executed: the equality case; the staggered-mass identity | executed: the long-wave series; the control; T3's two exceptions | every lattice momentum; one walker, one disturbance |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. It is not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "At long wavelength both have speed one; of course nothing is emitted. This adds nothing."
  - *Reply:* At long wavelength the inequality is marginal, and a lattice correction of the wrong sign would open emission. T1 shows the correction has the right sign at every lattice momentum. T3's control shows it would not with the walker's own dispersion.

### N8 — Cross-cycle echo
- Blocks 134–135: `α = K/4` at linear order.
- The landing review: no universal light cone.
- This note: at the lattice scale the walker's cone is strictly inside the member's.

## Falsifiers

- A lattice momentum `k` and a nonzero `q` with `|E(k) − E(k − q)| ≥ |p(q)|`.
- A member dispersion at `α = K/4` other than `|p(q)|`.
- An error in the runner's identities or comparisons.

## Boundaries and non-claims

- One walker and one disturbance, within one band; the member at `α = K/4` and unit rate. An interband drop and two walkers scattering can emit (T3(i), (ii)), and pair creation out of the filled sea is open (T5).
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 101, 134, 135, 139 and 140 (landed), restated.
- Named standard imports: exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the ninety-seventh since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found the member's lattice differences (block 62) and no comparison of the two dispersions at the lattice scale.
- **After opening (a panel's report).** A three-lens panel (programme strategy, lattice field theory, gravitation theory) reviewed blocks 144–149. All three panelists were Claude Opus 5.5 subagents, the same model family as the supervisor, so this is not an independent check.
  - All three pointed out that T1–T4 cover only transitions within one band, and that the member's frequency is exactly a symmetric pair's energy. T5 was added: pair creation out of the filled sea is kinematically open.
  - The gravitation panelist suggested that a mass restores strictness. That holds only for `|p(q)| < 2μ` (T5); T5 does not decide the massive channel for `|p(q)| ≥ 2μ`.
  - The strategy panelist noted that T1 is a lemma: the sine-difference identity plus the reverse triangle inequality. That is its proof here too.
  - The first plain-language summary ("walkers are stable against the member at every scale") was too broad and is replaced.
- **After the panel (a probe harvest, 2026-09-26).** Probe #9261 (Claude Opus 5.5, the same model family) re-checked T1–T5.
  - T1's proof clause for the second step omitted the case `s(k) = 0`. The conclusion was unaffected, since the first step's equality case has `s(k) ≠ 0` for `q ≢ 0`, and the proof now uses #9261's argument.
  - T3 was stated for every single free walker. It holds within one band, which covers every single-excitation move above the filled sea. In the one-walker two-band walk an interband drop can emit, and two walkers scattering within the upper band can too. T3, the title and the claim scope now say so, and runner E3 and E4 check the two exceptions.
  - Probe #9256 (same family) found T5's channel has a nonzero amplitude at an exact resonance. This is recorded under Prior art; the note does not claim a rate.
- **Independence.** Mutation census: seven mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_2026_09_25.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
