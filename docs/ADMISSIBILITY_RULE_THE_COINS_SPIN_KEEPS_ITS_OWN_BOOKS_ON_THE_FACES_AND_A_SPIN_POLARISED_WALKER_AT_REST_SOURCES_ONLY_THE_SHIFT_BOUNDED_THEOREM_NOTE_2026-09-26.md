---
claim_id: admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk and blocks 120, 136 and 138 as landed (the two-step stress Theta_ij = phi_j^T K_i^j, the momentum P^B = (P'' + Q)/2 with the bond shift, and the face spin S~ = C1 C2 C3 S): (T1) exact, for every state of the walk on Z^3 and each l: dS~_l/dt + D(x) - D(x - e_l) = -sum_ij eps_lij (Theta_ij - Theta_ji), with D the body-diagonal overlap averaged over the eight body diagonals; so the spin current is isotropic, delta_il D, and the torque is exactly the antisymmetric part of the two-step stress; the curl of the law is block 138 T3. (T2) exact: a walker at rest, psi = f chi with f real, has e = pi = K = 0, so P'' = Theta = 0: it sources neither the clock nor the lengths; P^B = (1/4) curl S~; and at that instant d pi/dt = 0 and dS~/dt = -grad D with zero torque, so dP^B/dt = 0. (T3) exact on the lattice reading of block 136 T4's transverse shift constraint at a static source (declared): the static shift is N = curl (-Lap)^{-1} M with M = wbar S~/(16 alpha), the lattice vector potential of a magnetisation, with zero divergence; a b^3 box of spin n carries total face spin b(b - 1)^2 n. A harvest of probe #9214 (Claude Opus 5.5, the supervisor's own model family), confirmed by an other-family referee (grok-4.6, #9284), with the supervisor's port of its exact checks. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_2026_09_26.py
---

# The coin's spin keeps its own books on the faces, and a spin-polarised walker at rest sources only the shift

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (T1 and T2 exact; T3 exact on a declared lattice reading of block 136 T4; within block 54's walk and blocks 120, 136 and 138 as landed; a harvest of probe #9214, confirmed by an other-family referee (grok-4.6, #9284); nothing adopted or registered; unaudited)

This note works within blocks 54, 120, 136 and 138 as landed on main (the walk, the two-step stress, the momentum the shift sees, and the face spin); it reports the balance law of the coin's spin on the faces and what a spin-polarised walker at rest sources; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 138 (landed) found that the coin's spin enters the momentum the member's shift sees through its curl: `P^B = P″ + ¼∇̄ × S̃`. Its next item was the spin's own balance law and the member's response to a spin-polarised walker. Probe #9214 found both, and an other-family referee confirmed them (#9284).

- **T1: the spin keeps its own books.** For every state, `dS̃_l/dt + D(x) − D(x − e_l) = −Σ_ij ε_lij(Θ_ij − Θ_ji)`.
  - The spin current is isotropic, `δ_il D`, with `D` the overlap along the cube's body diagonals.
  - The torque is exactly the antisymmetric part of block 120's two-step stress.
  - Its curl is block 138 T3.
- **T2: a walker at rest sources only the shift.** For `ψ = fχ` with `f` real, the energy, the two-step momentum and every current vanish. So the walker sources neither the clock nor the lengths. It sources the shift through `P^B = ¼∇̄ × S̃`, which does not change at that instant.
- **T3: the shift is a vector potential.** On a declared lattice reading of block 136 T4, the static shift is `N = ∇̄ × (−Δ̄)⁻¹M`, with `M = w̄S̃/(16α)`. This is the lattice vector potential of a magnetisation. It has zero divergence, so the clock is not driven.

In plain terms: a walker whose coin points one way, and which is not moving, carries no energy flow and no momentum. It still stirs the member, through the curl of its spin, the way a small magnet stirs a vector potential. The member answers with a shift, and only with a shift.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its densities and their placements, the member and the shift are supplied clauses. Nothing is adopted.
- **The walk and its densities** (blocks 54, 69, 120, 136 and 138 as landed).
  - `H = Σ_aσ_aS_a` and `P_j = S_jC_j`.
  - `e`, `π_j = Re ψ†P_jψ`, `P″_j = φ_jᵀπ_j` with `φ_jᵀ = ½(1 + T_j)Π_{l≠j}C_l`.
  - `K_a^j` is block 69's current, `Θ_ij = φ_jᵀK_i^j`, `Q_j` as in block 138, and `P^B = (P″ + Q)/2`.
- **The face spin** (block 138). `S_l(x) = ½[Re ψ†(x)σ_lψ(x + e_j + e_k) + Re ψ†(x + e_k)σ_lψ(x + e_j)]`, on the face perpendicular to `l`, and `S̃ = C₁C₂C₃S`. The curl lands on bonds.
- **The overlap `D`.** `D₀(x)` is the mean of the four body-diagonal overlaps `Re ψ†(p)ψ(p′)` of the cube `[x, x + (1, 1, 1)]`, and `D = C₁C₂C₃D₀`.
- **The shift's static equation (declared reading).** Block 136 T4 gives, for one wave vector, `4αp(pN_x − ċ_x)/w̄ = P_x` across it. On the lattice this note reads `p²` as `−Δ̄` on bond fields, and takes `ċ = 0` for a static source.
- **Standard imports, named at definition level.** The spin of two-component waves (Weyl) and the symmetric momentum as the canonical one plus half the curl of the spin (Belinfante and Rosenfeld), as comparators only; the vector potential of a magnetisation, as a comparator; exact rational arithmetic, including the inverse Laplacian on the `6³` torus as a polynomial.

## Theorem T1 — the spin keeps its own books

*Statement.* For every state of the walk on `ℤ³` and each `l`, `dS̃_l(x)/dt + D(x) − D(x − e_l) = −Σ_ij ε_lij(Θ_ij(x) − Θ_ji(x))`.

*Proof.*
- Take two eigen-waves, `(σ·s)u = lu` and `(σ·s′)u′ = l′u′`, with `s = sin k`, `q = k − k′` and `k̄ = (k + k′)/2`. The face spin's beat is `u′†σ_lu cos k̄_a cos k̄_b e^{iq·c}`, where `c` is the face centre. The averages add `Π_m cos q_m`, and `d/dt` gives `i(l′ − l)`.
- The coin identity `(l′ − l)u′†σ_lu = (s′_l − s_l)u′†u + iε_mln(s_m + s′_m)u′†σ_nu` splits the rate.
  - The first term: `s_l − s′_l = 2cos k̄_l sin(q_l/2)`, and the mean of the four body-diagonal cosines is the product of the three. So it is `−∇̄_lD`.
  - The second term: `(s_a + s′_a)cos k̄_a = sin 2k̄_a cos(q_a/2)` matches the beat of `Θ`, so it is `2(Θ_ba − Θ_ab)` for cyclic `(l, a, b)`.
- By bilinearity the law holds for every state (runner B1–B3 check the identities and the law on random exact states of the `5³` and `6³` tori, with all three terms nonzero).
- The curl kills the gradient, and `−ε_jklε_lmn∇̄_kA_mn = 2Σ_k∇̄_kA_kj` for antisymmetric `A`, which gives block 138 T3 (runner B4 reproduces block 138 T1 with the same densities). ∎

## Theorem T2 — a walker at rest sources only the shift

*Statement.* Take `ψ = fχ`, with `f` real and `χ` a fixed spinor. Then:
- `e`, `π_j` and every `K_a^j` vanish, so `P″ = 0` and `Θ = 0`;
- `P^B = ¼∇̄ × S̃` on every bond;
- `dπ_j/dt = 0` and `dS̃_l/dt = −∇̄_lD` with zero torque, so `dP^B/dt = 0` at that instant.

*Proof.* Each of `e`, `π_j` and `K_a^j` is the real part of `i` times a real number: `S_j` takes real `f` to imaginary values, `C_j` keeps real values real, and `χ†σ_aχ`, `χ†χ` are real. `Q` survives, since `χ†σ_jσ_aχ = δ_ja + iε_jab n_b`. The rest is T1 with `Θ = 0` (runner C1, C2, C6, on a `3³` box of spin `(3/5, 4i/5)` in the `6³` torus). ∎

## Theorem T3 — the shift is the vector potential of a magnetisation

*Statement.* On the declared lattice reading, the static transverse shift solving `4α(−Δ̄)N = w̄P^B` is `N = ∇̄ × (−Δ̄)⁻¹M`, with `M = w̄S̃/(16α)`, which is `w̄S̃/(4K)` at `α = K/4`. It has zero lattice divergence. A `b³` box of spin `n = χ†σχ` has total face spin `b(b − 1)²n`.

*Proof.* `∇̄` and `Δ̄` commute, and `P^B = ¼∇̄ × S̃` by T2. On the `6³` torus, `−Δ̄` has the eigenvalues `0, …, 12`, and on zero-mean fields its inverse is the degree-12 polynomial interpolating `1/λ`. The runner solves the equation exactly and compares `N` with the vector potential at every bond (C4). It also checks the divergence (C5) and the total spin at `b = 3` (C3). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 138 (landed) next_trace_action: the spin's own balance law on the faces; the member's response to a spin-polarised walker"
source_of_blocker_text: block 138's landed trace line
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a lattice form of block 136's member (to make T3's reading a theorem); the response once the walker spreads; the total angular-momentum balance on the faces"
conditional_surface_status: "T3 on the declared lattice reading of block 136 T4 for a static source"
hypothetical_axiom_status: "the walk, its densities, the member and the shift are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 54 (the walk), block 69 (the two-step momentum and its current), block 120 (the placement `φ_jᵀ` and the two-step stress), block 136 (`P^B`, the shift and its constraint), block 138 (the face spin and `P^B = P″ + ¼∇̄ × S̃`).
- **Probes.** #9214 (Claude Opus 5.5 worker `w-macbookpro9927a-j2fce`, the supervisor's own model family) found T1–T3 with its own exact checker (14 checks). The other-family referee (grok-4.6, worker `w-macbookpro90c72-je8e2`, #9284) confirmed it: the law on a rational state of the `5³` torus, the box's zero energy and current, the shift as a quarter of the spin's curl on 144 bonds of the `6³` torus, and the vector potential. The supervisor ported the exact checks into this note's runner, with the landed notes in place of the branch versions the probe used.
- **In the literature.** The spin current of two-component waves; the symmetric momentum as canonical momentum plus half the curl of the spin; the vector potential of a magnetisation. Reference only.
- **New here:** T1 on the faces of the lattice; T2 and T3 for the member.
- **Provenance.** Harvest of a same-family probe result, confirmed by a referee of another family.

## Exact target and obligation graph

Target: block 138's next items. The obligations are:
- (O1) the balance law (T1: runner B1–B4);
- (O2) the walker at rest (T2: runner C1, C2, C6);
- (O3) the static shift (T3: runner C3–C5; conditional on the declared reading).

The strongest step taken as a premise: the lattice reading of block 136 T4's transverse constraint.

## No-Go Discipline Gate

The note's negative sentence: a walker at rest with a real envelope sources neither the clock nor the lengths.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The walker at rest carries some energy or current.* Each is the real part of `i` times a real number, so it vanishes (T2; runner C1). ATTEMPTED.
2. *The spin's torque is not the stress's antisymmetric part.* The law holds with zero residual on random exact states (T1; runner B1, B2). ATTEMPTED.
3. *The shift's source moves at once.* `dπ/dt = 0` and the spin moves only by a gradient (T2; runner C6). ATTEMPTED.
4. *The static shift has a divergence that drives the clock.* Its lattice divergence is zero (T3; runner C5). ATTEMPTED.
5. *The `4³` torus tests the torque.* On it `sin 2k = 0` and the two-step momentum vanishes, so the runner uses `5³` and `6³`. ATTEMPTED.

Scope left open: the walker's later spreading; a lattice form of block 136's member; the total angular-momentum balance.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The lattice reading in T3 is declared under Premises. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 69, 120 (landed) | the walk, the two-step momentum and its stress | yes (restated) |
| blocks 136, 138 (landed) | `P^B`, the shift constraint, the face spin | yes (restated; 138 T1 re-checked: runner B4) |
| probe #9214, referee #9284 | the route and an other-family confirmation | yes (ported and re-run here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a walker at rest sources neither clock nor lengths, only the shift, as a vector potential" | executed: the coin identity and the beat identities | executed: the law at every site and direction of the `5³` torus | executed: `P^B = ¼ curl S̃` on every bond of the `6³` torus | executed: the exact inverse Laplacian and the vector potential | every state by proof; T3 on the declared reading |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A walker at rest has no momentum, so nothing should drive the shift."
  - *Reply:* Its canonical momentum is zero, but the momentum the shift sees is the symmetric one, which carries half the curl of the spin (block 138). A uniformly spinning box has that curl on its surface.

### N8 — Cross-cycle echo
- Block 136: the shift couples to `P^B`.
- Block 138: `P^B` carries the spin's curl.
- This note: the spin keeps its own books, and at rest it is the shift's only source.

## Falsifiers

- A state for which the law of T1 has a nonzero residual.
- A real envelope times a fixed spinor with nonzero energy or current.
- A static shift from T3's equation that differs from the vector potential, or has nonzero divergence.

## Boundaries and non-claims

- T3 rests on the declared lattice reading of block 136 T4.
- The time-dependent response and the walker's spreading are not covered.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 69, 120, 136 and 138 (landed), restated.
- Named standard imports, at definition level: comparators only (the spin of two-component waves; the symmetric momentum; the vector potential of a magnetisation); exact rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block, 2026-09-26, during the owner's 12-hour campaign of that day.
- **Provenance.** The derivation is probe #9214's (Claude Opus 5.5, the supervisor's own model family). An other-family referee (grok-4.6) confirmed it (#9284). The supervisor line-checked the steps and ported the exact checks, with the landed texts of blocks 136 and 138.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found block 138's open items and no other attempt.
- **Independence.** Mutation census: at least one mutation per science family (B, C), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_2026_09_26.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
