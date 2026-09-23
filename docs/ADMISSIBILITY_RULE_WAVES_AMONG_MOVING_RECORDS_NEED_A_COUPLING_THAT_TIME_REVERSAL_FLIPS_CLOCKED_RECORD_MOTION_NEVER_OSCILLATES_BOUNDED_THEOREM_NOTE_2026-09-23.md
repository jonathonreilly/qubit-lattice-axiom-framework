---
claim_id: admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_clocked_record_motion_never_oscillates_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading and block 95's clock-timed record motion; the routes to waves in the repository (block 44's direction-carrying records, the mobile-record lane's chiral pair exchange #8600 and link rotors #8650, block 54's walk) placed with their own supplied clauses. Exact: record motion in detailed balance, for every clock timing and with the clock field held or following the records, has a self-adjoint generator: real spectrum, no oscillation, no fronts, no orbits, and so has every function of the configuration (possibility or clock field slaved to the records); a record with direction memory but no exchange oscillates only at waves shorter than its memory length (exact on a line), its oscillating modes decaying at a rate that does not vanish at long waves; long waves in each route come from two conserved things coupled at first order in k by a term time reversal flips; content-blind records spread diffusively under every covariant rule. Executed: spectra of larger clocked chains; the direction-memory record over a grid of wave vectors. Nothing adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_2026_09_23.py
---

# Waves among moving records need a coupling that time reversal flips; clocked record motion never oscillates

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; the routes' clauses are theirs; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) and block 95's clock-timed motion; it reports what record motion can and cannot do about waves and places the routes in the repository; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner, on 2026-09-23: "I think we are in the third column of your chart, and we need to figure out the not from records alone bits (make sure to check latest PRs and repo though)". Block 95 (#8860) took the reciprocal `1/r` cell. This note takes the other cell, waves.

The repository has four routes to waves among moving records or on their lattice:
- block 44 (#8550): records whose content is a direction of travel, with collisions that redraw two directions at fixed total momentum; sound at `c² = (1 − ρ)/3`;
- the mobile-record lane's #8600: permanent record pairs exchanging places at a chiral context rate `γ`; two colour moments `X, Y` obey curl equations with `c = |γ| √(ρ_A ρ_B / 3)`, and every mode is static at `γ = 0`;
- the same lane's #8650: link rotors with quantum hopping; transverse waves;
- block 54 (#8570): possibility's own two-component state moving reversibly, the walk; frequencies `±β|sin k|`.

This note shows what they share, and why the record layer with block 95's clocks has none of it.

- **T1: clocked record motion never oscillates.** Record motion in detailed balance has a generator that is self-adjoint in the stationary law's inner product.
  - This covers block 39's pair-weight motion and block 95's motion for every timing, with the clock field held or following the records.
  - Its spectrum is real. Every autocorrelation is a nonnegative mixture of decaying exponentials: no oscillation at any wavelength, no front (block 94's T5) and no orbit of one record about another.
  - The same holds for every function of the configuration, including possibility slaved to the neighbourhood and the clock field slaved to the records.
  - A circulation, a rate that differs between the two directions of a bond, is what makes a mode oscillate.
- **T2: a memory of one's own direction gives only short, dying waves.** A record that keeps its last direction with probability `p` and otherwise turns oscillates only at waves shorter than its memory length. On a line this is exact: the modes are non-real if and only if `|sin k| > (1 − p)/p`. Longer waves spread diffusively, and the oscillating modes decay at a rate that does not vanish at long waves. As `p → 1` the waves become free streams along the six axes, not an isotropic wave.
- **T3: long waves need two conserved things coupled by a term that time reversal flips.** In each route the long waves come from such a pair, coupled at first order in `k`:
  - block 44: density and momentum;
  - #8600: the colour moments `X` and `Y`, coupled by `γ`;
  - block 54: the qubit's two components.

  Made symmetric, each coupling gives growth and decay, not waves. Content-blind records conserve only their number, and the 24 rotations leave no vector invariant. So under every covariant rule, reversible or not, their long waves spread diffusively.

So the piece of the waves cell that does not come from records alone is a coupling that time reversal flips. Inertia needs the same kind of thing, a momentum. T1 shows the clocked gas has neither, which is why block 95's pull clumps records instead of making them orbit. In the owner's picture (permanent contents, reversible motion, possibility shifting with its neighbourhood) such a coupling can enter in four ways:
- through the exchange of records, if the exchange is chiral (#8600);
- through links (#8650);
- through possibility keeping its own qubit state and moving it on reversibly (the walk);
- through momentum passed between records (block 44), which needs contents to change or an extra register.

In plain terms: things that only jostle and wait, however their clocks run, can clump but cannot ring. To ring, something must carry a direction that running the film backwards would reverse, and must hand it on without losing it. Records whose contents never change can't do that on their own. A twist in how they swap places can, and so can the unrecorded possibility at each site, if it keeps its own two-part state as it moves.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through its sentences:
- Lattice and Admissibility (one covariant nearest-neighbour rule, "covariant under lattice" symmetries).
- Record ("A site never carries more than one record; records are permanent"). A record's content never changes.
- The open gates on update laws and persistence dynamics.

The owner's reading (records move, one per site at a time; possibility shifts with the neighbourhood) is quoted as the owner's. Nothing is adopted.

- **Record motion.** The motion is block 39's (#8530) pair-weight motion and block 95's (#8860) clock-timed motion. The rate `w_x^a w_y^(1−a)` times a heat-bath factor, with the clock field held or slaved to the records by block 53's law, is in detailed balance with block 95's laws.
- **The routes' clauses.** These are block 44's streaming and redraw, #8600's chiral context rates, #8650's rotors and quantum hopping, and block 54's walk. They are used as their notes state them, and here only through their linear long-wave equations.
- **Waves.** A wave here is a mode that oscillates. At long wavelength that means a complex rate `±i c|k|` for small `k`; a front is a correlation peak that moves away from its origin.

## Theorem T1 — clocked record motion never oscillates

*Statement.* Let a record chain on a finite torus satisfy detailed balance with law `π`. Then:
1. The generator `Q` satisfies `π(C) Q(C, C') = π(C') Q(C', C)`, and `D^(1/2) Q D^(−1/2)` is symmetric (`D = diag π`). The spectrum is real and non-positive.
2. For every function `f` of the configuration, `⟨f(0) f(t)⟩_π − ⟨f⟩² = Σ_n c_n e^(λ_n t)` with `c_n ≥ 0` and `λ_n ≤ 0`. The correlation decays monotonically and never oscillates.
3. With translation invariance, block 94's T5 gives no fronts.

This covers block 39's pair-weight motion and block 95's clock-timed motion for every timing `a`, with the clock field held or slaved. It includes functions of the configuration such as possibility slaved to the neighbourhood and the slaved clock field. In particular two records never orbit one another: the phase of their relative position has a real, monotone correlation.

*Proof.* Symmetrise with `D^(1/2)`, then expand in the orthonormal eigenbasis. ∎

The runner checks detailed balance exactly for block 95's slaved field on a ring of six (base-4 clocks), for two and three records and the three timings `a = 1, 1/2, 0`: all 360 moves (family B). As the contrast, one record on a ring of six hopping at 2 one way and 1 the other has mode rates `2ω^j + ω^(−j) − 3` with imaginary part `√3/2` at `j = 1`; the density wave circulates. Control W1 finds real spectra to `10⁻¹⁵` for three records on a ring of ten and two records on `4³` (120 and 2016 states, all three timings). With a circulation added, the imaginary parts are `0.7` to `2.9`.

## Theorem T2 — a memory of one's own direction gives only short, dying waves

*Statement.*
1. **On a line.** A record that keeps its last direction with probability `p` and reverses otherwise has mode multipliers `μ` with `μ² − 2p cos(k) μ + (2p − 1) = 0`. At `k = 0` they are `1` and `2p − 1`. The density branch is `1 − (p/(2(1 − p))) k² + …`, which is diffusive. The branches are non-real exactly where `p² cos² k < 2p − 1`, that is `|sin k| > (1 − p)/p` (for `p > 1/2`): at waves shorter than about `2π p/(1 − p)` sites.
2. **In three dimensions.** A record keeps its direction with probability `p` and otherwise turns to one of the other five. Its mode matrix `M(k) = E(k) T` satisfies `conj(M(k)) = Π M(k) Π`, with `Π` the inversion, so its spectrum is closed under conjugation. At `k = 0` the multipliers are `1` and `(6p − 1)/5`, the latter five times. At `k = (π/2, 0, 0)` and `p = 9/10` the characteristic polynomial has real coefficients, exactly one root in `(9/10, 1)` (the real density branch) and two non-real roots.

*Proof.* The line: a 2×2 determinant; the threshold from the discriminant; the series of the larger root. Three dimensions: `Π T Π = T` and `Π E(k) Π = E(−k) = conj(E(k))`. The determinant at `k = 0` and the root count at `(π/2, 0, 0)` are exact (family C). ∎

Control W2 scans the zone on a `24³` grid:
- At `p = 1/2`, the leading multiplier is real for `|k| < 0.8`, to `10⁻¹⁵`.
- At `p = 9/10` and `99/100` it is real at the smallest grid wave vectors and non-real from `|k| = 0.45`. The memory length there is beyond the grid's resolution.
- Almost every wave vector has some non-real multiplier: direction modes oscillate while they decay. At `|k| < 0.3` their moduli stay at most `0.405`, `0.897` and `0.990`, close to the `k = 0` value `(6p − 1)/5`, so they decay at a rate that does not vanish at long waves.

As `p → 1` the memory length diverges and each record streams along its own axis. There are fronts, but only on the six axes (block 44 without its redraw), and no isotropic wave.

## Theorem T3 — long waves need two conserved things coupled by a term that time reversal flips

*Statement.*
1. **Density and momentum** (records whose direction is exchanged in collisions, block 44). `∂_t ρ = −i k·g` and `∂_t g = −i c² k ρ`. The characteristic polynomial is `μ² (μ² + c²|k|²)`, with rates `±i c|k|`.
2. **Colour moments** (the chiral pair exchange of #8600). `∂_t X = a i k × Y` and `∂_t Y = −b i k × X`. The characteristic polynomial is `μ² (μ² + ab|k|²)²`, with rates `±i √(ab) |k|`; here `ab = γ² ρ_A ρ_B / 3`.
3. **Possibility's qubit** (the walk, block 54). `H(k) = β Σ_j σ_j sin k_j` has `H² = β² Σ_j sin² k_j`, so the frequencies are `±β |sin k|`, which tend to `±β|k|`.
4. **Content-blind records.** The average of the 24 proper cubic rotations is the zero matrix, so no vector is invariant. The average of `R ⊗ R` projects onto `δ_ij`. A covariant rule therefore gives one conserved density no drift, and its long-wave current is `−D ∇ρ`. The mode is diffusive under every covariant rule, reversible or not.

In items 1–3 the first-order coupling is antisymmetric: it generates a rotation, not a decay. It joins quantities of opposite parity under time reversal:
- density and momentum, where the momentum `g` flips;
- `X` and `Y` through `γ`, where the reversed process has `−γ`;
- the real and imaginary parts of the amplitude, where conjugation flips the imaginary part.

Made symmetric, a coupling gives real rates, which means growth and decay, not waves; the runner's mutation does this for sound. At `γ = 0`, or with `β = 0`, or with no momentum, the long-wave rates vanish.

*Proof.* The three determinants, and `H²` from the anticommutation of the three content matrices, are exact algebra at general `k` (family D). The rotation averages are exact (family E). ∎

T1 is the case where the coupling T3 needs is absent. Under detailed balance the first-order couplings vanish, because a self-adjoint generator has no imaginary first-order part.

## Executed control

Script `specs/supervisor_control_block96_waves.py`, output in `.out.txt`; floating point, evidence and not proof.
- **W1.** Spectra of block 95's clocked chains with `log κ = −1`. Three records on a ring of ten and two records on `4³`, for `a = 1, 1/2, 0`: largest `|Im|` between `0` and `6·10⁻¹⁵`. With a circulation (`+x` hops at twice the rate of `−x` hops) it is `0.67` to `2.88`.
- **W2.** The direction-memory record over a `24³` grid (numbers under T2).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the owner's request of 2026-09-23 ('we need to figure out the not from records alone bits'); block 94's scorecard cell 'waves at the signal speed' for reading (iii)"
source_of_blocker_text: owner, 2026-09-23; block 94 (#8840); decision record #8572
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the waves cell mapped: the missing piece is a coupling odd under time reversal (chiral exchange, links, possibility's qubit, momentum); next candidates: the clock field acting on a route's waves (one geometry for records and waves); the delayed clock law; formation with the clock"
conditional_surface_status: "T1-T3 exact as stated; the routes' own results are cited under their clauses; W1-W2 executed"
hypothetical_axiom_status: "the owner's reading, block 95's clocked motion and the routes' clauses are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **This repository.**
  - Block 94's T5 (#8840) proved that reversible translation-invariant chains carry no fronts.
  - Block 44 (#8550) gave the direction-carrying record gas and its sound.
  - Block 54 (#8570) gave the walk and its symbol `a₀ + 2aΣcos k_j + βΣσ_j sin k_j`.
  - Block 57 (#8578) showed that the clock field's nearest-neighbour kinetic terms carry no delay.
  - The mobile-record lane's #8600 (colour waves through moving geometry, with chiral context rates) and #8650 (rotor fields and transverse waves) supply the chiral and link routes. They are cited here, not re-derived.
- **Literature, named at definition level.**
  - The self-adjointness of reversible Markov generators.
  - The persistent random walk, whose density obeys the telegraph equation of Goldstein and Kac.
  - Sound as the mode of conserved density and momentum (Landau and Lifshitz).
  - The fact that reactive (non-dissipative) couplings join variables of opposite time-reversal parity, per the reciprocal relations of Onsager and Casimir.
- **New here.**
  - T1 stated for block 95's clocked gas at every timing, including the slaved field and slaved possibility, with the conclusion that nothing orbits.
  - T2's exact line threshold and the three-dimensional conjugation structure for a record with direction memory.
  - The reading of the four routes as one requirement (T3), with the content-blind case closed by the rotation averages.
  - The statement that the waves cell and inertia share the missing piece.

## Exact target and obligation graph

Target: what, besides records, the moving-records column needs for waves. The obligations are:
- (O1) whether clocked record motion, or anything slaved to it, can oscillate;
- (O2) whether a record's own direction memory suffices;
- (O3) what the routes that do give waves have in common.

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- record motion in detailed balance never oscillates, under any clock timing;
- functions of its configuration never oscillate;
- a direction memory without exchange gives no long waves;
- content-blind records spread diffusively under every covariant rule.

### N1 — Routes by which the sentences could fail or mislead
1. *Record motion that is not in detailed balance* (a circulation, as in #8600). T1 does not apply: this is the chiral route.
2. *Collisions that exchange directions* (block 44). These change contents, against permanence, unless the direction is an extra register. This is the momentum route.
3. *Ordered contents.* A broken continuous symmetry gives slow modes, but without a coupling odd under time reversal they relax (T1 applies to any reversible rule).
4. *Quantum possibility or links.* These are not chains of records; they form the walk and link routes.
5. *T2 at short waves.* Oscillations there are real, and they are damped by the memory time.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The routes' clauses are named and cited, and their linear long-wave equations are used as their notes state them. T3's content-blind statement is at the level of the long-wave current allowed by covariance.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | Lattice, Admissibility and Record (permanence) sentences | yes |
| block 95 (#8860) | the clocked motion T1 covers | yes |
| block 94 (#8840) T5 | no fronts under detailed balance | yes |
| block 44 (#8550), block 54 (#8570) | the momentum and walk routes | yes (placed) |
| #8600, #8650 (mobile-record lane) | the chiral and link routes | no (placement; their clauses) |
| block 57 (#8578) | the clock field has no delay with nearest-neighbour terms | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "clocked record motion never oscillates; direction memory gives only short dying waves; long waves need two conserved things coupled by a term time reversal flips" | executed: detailed balance at all 360 moves on the ring for three timings; the line and 3D mode matrices | executed: the clock field on the ring; the inversion relation | executed: the ring's mode rates with and without circulation; the three routes' characteristic polynomials; control spectra | executed: rotation averages | T1 for every chain in detailed balance (proof); T2 exact on the line and at two 3D wave vectors; T3 at general k |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "This is textbook." Reply: the ingredients are textbook, and the note says so. The content is their application to the moving-records reading:
  - block 95's clocks cannot supply waves;
  - the owner's slaved possibility cannot either;
  - the four routes in the repository meet one requirement.
- Second objection: "Streams along the axes are waves." Reply: they are fronts, but not isotropic ones, and T2 says so.

### N8 — Cross-cycle echo
Block 94 put the waves cell in the amplitude layer. Block 95 put the reciprocal pull in the clock field. This note shows that the clock field, being slaved and reversible, adds no waves, and it names the one requirement that the chiral, link, walk and momentum routes each meet.

## Falsifiers

- A record chain in detailed balance with a non-real eigenvalue.
- On the line, a direction-memory record with non-real multipliers at `|sin k| < (1 − p)/p`.
- A covariant rule for content-blind records whose long-wave density mode propagates.

## Boundaries and non-claims

- The routes' results are theirs and are not re-derived beyond their linear long-wave equations.
- T3's content-blind statement concerns the long-wave current that covariance allows; it is not a hydrodynamic limit theorem.
- No route is adopted, and no identification with light or sound in nature is made.
- Known physics is not used.

## Imports
- `minimal_axioms`. Blocks 39, 44, 54, 57, 94, 95 and PRs #8600, #8650: restated or placed.
- Named standard imports at definition level:
  - self-adjointness of reversible generators and the spectral expansion;
  - the persistent random walk and the telegraph equation (Goldstein, Kac);
  - sound from conserved density and momentum (Landau–Lifshitz);
  - the reciprocal relations of Onsager and Casimir for couplings of opposite time-reversal parity;
  - the anticommutation of the Pauli matrices;
  - floating-point eigenvalues for the control.

## Review record
- **Who and when.** Supervisor-run block, the forty-fourth since the source-link direction opened and the seventh run on Claude Opus 5.5. Asked by the owner on 2026-09-23 (the waves cell of the moving-records column).
- **Survey.** The mobile-record lane's #8600 and #8650 were read for their mechanisms: chiral context rates, and link rotors with quantum hopping.
- **Own-prior-art check.** It found block 44 (the momentum route and its sound) and block 94's T5.
- **A correction made before writing.** The control showed that the density multiplier of a three-dimensional direction-memory record becomes non-real at short waves. T2 is therefore stated for long waves, with the exact line threshold.
- **Independence.** No independent review has taken place. Mutation census: eight mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
