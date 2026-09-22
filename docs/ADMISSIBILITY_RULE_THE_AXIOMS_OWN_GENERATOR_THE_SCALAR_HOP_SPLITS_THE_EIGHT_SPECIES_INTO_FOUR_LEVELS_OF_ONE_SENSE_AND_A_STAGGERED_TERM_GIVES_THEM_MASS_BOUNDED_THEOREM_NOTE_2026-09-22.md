---
claim_id: admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 62, 63, 65, 69 and 70 (open PRs #8570, #8592, #8593, #8596, #8601, #8602; not adopted): block 54 T1(a)'s complete hermitian covariant nearest-neighbour family on the qubit coin, a0 + 2a sum_j cos k_j + sum_j sigma_j sin k_j, from which block 54 T1(c) removed a0 and a by ADDING an inversion symmetry that the Lattice axiom does not contain (an import, flagged by the fork probe of 2026-09-22); and one further object, the staggered on-site term m eps(x), eps = (-1)^{x+y+z} - a coin scalar, invariant under the proper rotations about any site, breaking translation by one site (the form a chessboard background takes; supplied, not derived). (T1) With the a-term the eight zeros of the walk sit at the four energies a0 + 2a(3 - 2|n|), multiplicities 1:3:3:1, each level holding species of ONE sense, and none is gapped. (T2) For a != 0 the species-exchange maps of block 70 are broken exactly - V_n H_a V_n - det(D_n) H_a = (1 - det D_n) a0 + 2a sum_j (D_j - det D_n) C_j, nonzero for the seven species n != 0 - while the reversal of motion still commutes with H_a. (T3) eps anticommutes with every operator moving an odd number of steps (the walk, the a-hops, block 62's varying frame, block 65's twist hop, the reach-three strain term) and commutes with the reach-two strain term and with site fields; hence (H + m eps)^2 = H^2 + m^2 and phi (H + m eps) phi = phi H phi + m w eps: a rest energy m timed by the local clock, the same for every species. (T4) With both terms the wave vectors k and k + pi(111) mix in 2x2 blocks with energies a0 +- sqrt((2a sum cos k +- |sin k|)^2 + m^2); at the zeros the species pair as (n, n + (111)), opposite senses, into one pair of mass sqrt(m^2 + 36a^2) and three pairs of mass sqrt(m^2 + 4a^2); all four masses equal m iff a = 0. EXECUTED, NOT CLAIMED: a packet of the massive walk released from rest in a rate gradient accelerates at -0.0179 against -0.0200 (block 54's law, the momentum spread accounting for the rest); the filled sea WITH rest energy still has a clock stiffness kappa = 0.076-0.090 and reach-three strain stiffnesses six to sixteen times smaller (m = 0, 1/2, 1): rest energy does not make the sea induce the curvature member either. NOT claimed: that the a-term or a staggered background is present; the filling of levels; anything about which species are present; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_axioms_own_generator_scalar_hop_splits_species_staggered_term_gives_mass_2026_09_22.py
---

# The axioms' own generator: the scalar hop splits the eight species into four levels of one sense, and a staggered term gives them mass

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about the complete covariant nearest-neighbour family on the qubit coin and a supplied staggered term; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports what the complete family of covariant nearest-neighbour generators allowed by the axioms does to the walk's eight species once an imported inversion symmetry is dropped, and what a staggered on-site term does; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 54 (open PR #8570) found the complete family of hermitian, rotation-covariant, nearest-neighbour generators on the qubit coin — three numbers: an offset `a₀`, a coin-scalar hop `a`, and the walk — and then set `a₀ = a = 0` by adding an inversion symmetry. The Lattice axiom names proper rotations only; the fork probe of 2026-09-22 (`FORK_PROBE_source_link_20260922.md`) flagged the inversion as an import. This note keeps the axioms' own family, and adds the one further nearest-neighbour object the panel named: a staggered on-site term.

1. **The scalar hop splits the species and gaps none** (T1). The eight zeros move to four energies `a₀ + 2a(3 − 2|n|)`, with multiplicities 1:3:3:1, and each level holds species of one handedness only. At every zero the coin vector still vanishes: the two branches still meet.
2. **It breaks the exchange maps, not the reversal of motion** (T2). For `a ≠ 0` the eight species are no longer exact copies of one another; the reversal of motion still commutes.
3. **A staggered term is a rest energy** (T3). `ε(x) = (−1)^{x+y+z}` anticommutes with everything that moves an odd number of steps — the walk, the `a`-hops, the frame, the twist hop, the reach-three strain — and commutes with the reach-two strain and with the rates. So `(H + mε)² = H² + m²`, and with clocks the term becomes `m w_x ε(x)`: a rest energy timed by the local clock, the same for every species. The reach-two coupling is again the odd one out.
4. **Four massive pairs, two masses** (T4). With both terms the species pair across the lattice's checkerboard, `(n, n + (111))`, opposite handedness, into one pair of mass `√(m² + 36a²)` and three of mass `√(m² + 4a²)`. All four equal iff `a = 0`.

Executed: the massive walker released from rest falls toward slow clocks as a slow body (`−0.0179` against block 54's `−0.0200`); and block 76's sea, redone with rest energy, still induces the clocks' stiffness and almost none for the lengths.

In plain terms: the axioms allow the walker one more nearest-neighbour move than block 54 used — a hop that does not turn the coin. That hop does not remove any of the eight kinds; it sorts them into four energy levels, each level all left-handed or all right-handed. Separately, if the sites beneath the walker alternate like a checkerboard in one number, the walker acquires a rest energy that its local clock times, and it falls like a slow body. The two together pair the eight kinds into four heavy walkers: one heavier, three lighter. Whether the lattice has either of these is not decided here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "FORK_PROBE_source_link_20260922.md section 4, items 2 and 3: block 54's inversion is an import; the a-term splits the species 1:3:3:1; a staggered term gives a Kogut-Susskind-type mass; block 76 next_trace_action: does a sea with rest energy induce a lengths' stiffness?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "fork 5 (rest energy) has a nearest-neighbour mechanism inside M2(C) at the price of a staggered background; the massive sea does not induce the curvature member either; next: SU(2) bond links (block 78); the exchange sign (block 79); whether a chessboard record background (block 17's states) supplies the staggered term"
conditional_surface_status: "T1, T2, T4 exact for every a0, a, m; T3 an operator identity for every state and field on every even torus and on the infinite lattice; the executed numbers are the control's"
hypothetical_axiom_status: "block 54's family without the imported inversion; a staggered on-site term as a supplied background; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (proper rotations only; no inversion), the Qubit axiom's one-site algebra and "no possibility is privileged" (a coin-scalar term privileges no coin direction), and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 65, 69, 70 (open PRs) supply the family, the couplings and the maps.

- **The family.** `H_a = a₀ + 2aΣ_jC_j + Σ_jσ_jS_j`, symbol `a₀ + 2aΣcos k_j + σ·s`; block 54 T1(a).
- **Levels.** At `k = πn`: `Σcos k_j = 3 − 2|n|`, `|n|` the number of components equal to 1; sense `s_n = (−1)^{|n|}`.
- **Staggered term.** `ε(x) = (−1)^{x+y+z}`; `(H + mε)` with `m` real. Under the 24 proper rotations about a lattice site `x + y + z` keeps its parity; under translation by one site `ε → −ε`.
- **Odd and even operators.** An operator moves an odd (even) number of steps if every term carries an odd (even) total displacement; `ε` anticommutes (commutes) with it.

The energy offsets of the lattice's extra species by a scalar hop, and a mass carried on the lattice's sublattice grading rather than on the coin, are familiar from the Hamiltonian formulation of Kogut and Susskind; named as a comparator only.

## Prior art and what is new

New, inside the framework's vocabulary: the exact statement of what the axioms' own family (not block 54's restriction) does to the species — the 1:3:3:1 single-sense split and the exact breaking of the exchange maps; the exact algebra of the staggered term against every coupling the campaign has supplied, including that it commutes with the reach-two strain term alone; the two masses; and the executed massive sea. No gravitational claim is made.

## Exact target and obligation graph

Target: the species under the axioms' own generator and under a staggered term. Obligations: (O1) the levels; (O2) the maps; (O3) the staggered term's algebra; (O4) the masses. T1–T4 discharge them.

## Theorem T1 — the scalar hop splits the species and gaps none

*Statement.* At the eight zeros `k = πn` of the walk, `H_a(πn) = a₀ + 2a(3 − 2|n|)`: four levels for `|n| = 0, 1, 2, 3` with multiplicities `1, 3, 3, 1`; every species on a level has the sense `(−1)^{|n|}`; and `s(πn) = 0`, so the two branches of `H_a` meet at each level.

*Proof.* `cos(πn_j) = (−1)^{n_j}`; `Σ_j(−1)^{n_j} = 3 − 2|n|`; `sin(πn_j) = 0`. The number of `n` with `|n| = m` is `C(3, m)`. Block 70 T1(e) for the sense. ∎

## Theorem T2 — the exchange maps break, the reversal of motion does not

*Statement.* `V_nH_aV_n − s_nH_a = (1 − s_n)a₀ + 2aΣ_j(D_j − s_n)C_j`, which is nonzero for every `n ≠ 0` when `a ≠ 0` (and for odd `n` when `a₀ ≠ 0`). `Θ = σ₂K` commutes with `H_a`.

*Proof.* Block 70 T1(a): `U_nC_jU_n = D_jC_j`, and `R_n` commutes with coin scalars; the walk part gives `s_nH`. For `n ≠ 0` some `D_j − s_n ≠ 0`. `Θ` conjugates real coin scalars to themselves and the walk to itself (block 70 T3(b)). ∎

## Theorem T3 — a staggered term is a rest energy

*Statement.* (a) `ε` anticommutes with the walk, with `Σ_jC_j`, with block 62's frame coupling `½Σ{E^j·σ, S_j}` for any frame field, with block 65's twist hop and frame rotation, and with the reach-three strain term `Σσ_a½{C_a[B_a^j], P_j}` for any strain; it commutes with the reach-two strain term `Σσ_a½{C_a[B_a^j], S_j}` and with every site field. (b) `(H + mε)² = H² + m²`. (c) `φ(H + mε)φ = φHφ + m w ε`.

*Proof.* (a) An operator that moves `d` steps carries `ε(x)ε(x + d) = (−1)^{|d|₁}`: `S_j, C_j, C_a[v]` move one step; `P_j` two; `C_a[v]P_j` one or three; `C_a[v]S_j` zero or two; site fields none. (b) `Hε + εH = 0` and `ε² = 1`. (c) `φ` is a site field. ∎

For a body at rest the rest energy `m w_x` is the same for all eight species (T1's split is the `a`-term's, not the mass's), and block 54's fall law with the energy `≈ m w` applies: the control shows the fall. Under the reach-two coupling `(H₂[B] + mε)²` is not `H₂[B]² + m²`: the checkerboard grading that carries the mass is the grading that coupling breaks (block 70 T3(d)).

## Theorem T4 — four massive pairs, two masses

*Statement.* With `a` and `m` both present, `H` couples `k` with `k + π(1,1,1)` (where `Σcos k` and `s` change sign) in `2 × 2` blocks per coin branch, with eigenvalues `a₀ ± √((2aΣcos k ± |s|)² + m²)`. At the zeros the pairs `(n, n + (111))` — of opposite sense — have energies `a₀ ± √(m² + 4a²(3 − 2|n|)²)`: one pair with mass `√(m² + 36a²)` (`|n| = 0, 3`) and three with `√(m² + 4a²)` (`|n| = 1, 2`). The four masses are equal iff `a = 0`.

*Proof.* `ε` shifts the wave vector by `π(1,1,1)`; the block is `[[a₀ + 2ac + λ, m], [m, a₀ − 2ac − λ]]`, `λ = ±|s|`; its eigenvalues are as stated (runner D2, symbolic). At a zero `|s| = 0`, `c = 3 − 2|n|`, and `|3 − 2|n||` is 3 or 1. ∎

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block77_a_term_and_mass.py`. **W1** (`6³` torus, `a₀ = 0.3`, `a = 0.2`): eigenvalues within `2e-15` of the four levels `1.5, 0.7, −0.1, −0.9`. **W2** (`m = 0.7`): the spectrum of `H + mε` equals `±√(E_walk² + m²)` to `7e-15`, gap `0.7000`; with the `a`-term, eigenvalues within `2e-15` of `a₀ ± √(m² + 36a²)` and `a₀ ± √(m² + 4a²)`. **W3** (block 76's sea with rest energy, `L = 8`, one mode): `κ = 0.089, 0.090, 0.076` for `m = 0, ½, 1`; reach-three TT stiffness `0.0035, 0.0024, 0.0012`; isotropic stretch `0.0004, 0.0026, 0.0046`; the clocks' stiffness stays six to sixteen times the lengths' — rest energy does not turn the induced energy into the curvature member. **W4** (a `24 × 8` slice, `m = 0.6`, Gaussian packet of width 4 projected on the positive branch, rate gradient `0.02`): released from rest it accelerates at `−0.0179` toward slow clocks against `−w²g = −0.0200`; the packet's momentum spread (`~1/8` against `M = 0.6`) lowers the mean of `∂²E/∂p²` to about `0.94/M`, which accounts for the difference.

## No-Go Discipline Gate

The note's negative sentences: the `a`-term gaps no species; the reach-two coupling does not anticommute with the staggered term.

### N1 — Routes by which the sentences could fail or mislead
1. *Gapping by other means.* A coin-vector term would be needed at a zero (block 73 T1's structure); the stabiliser argument of the fork probe excludes every covariant one. Not a route.
2. *A different staggering.* `ε` is the only site sign invariant under rotations about a site up to overall sign (`(−1)^{x}` and `(−1)^{x+y}` are not); a staggered coin-vector term would privilege a coin direction.
3. *Translation.* `ε` breaks translation by one site; it is a background, not a law, and the note treats it as supplied.
4. *Filling.* Which levels are filled, and what the split means for a many-record state, is outside (block 79's question comes first).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even tori (the staggering is periodic); the identity frame for T1, T2, T4; the fields vary in T3 but the coupling to strains is first order as supplied.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice's proper rotations (no inversion); the coin's algebra; "no possibility is privileged" | yes (premise) |
| block 54 (open PR #8570) | the complete family (T1(a)); the imported inversion (T1(c)) | yes (restated) |
| blocks 62, 63, 65, 69 (open PRs #8592, #8593, #8596, #8601) | the couplings tested against `ε` | yes (restated) |
| block 70 (open PR #8602) | the exchange maps; `Θ`; the checkerboard map | yes (restated) |
| `FORK_PROBE_source_link_20260922.md` | the flag on the inversion; the staggered term | context |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "1:3:3:1 single-sense split, no gap; maps broken, reversal kept; the staggered term's algebra; two masses" | executed: the `a`-term and the coin vector at each zero; the exact difference `V_nH_aV_n − s_nH_a` for all eight species | executed: anticommutation with six kinds of operator and commutation with the rates and the reach-two term at all 216 sites; the square and the clocked form at all sites | executed: the `2 × 2` blocks' exact eigenvalues; the four masses | executed: the level count and the one-sense property | T1, T2, T4 for every `a₀, a, m`; T3 for every state and field; presence of the terms not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A staggered mass is the oldest trick in lattice fermions." Reply: as a comparator, yes; the content here is where it sits in this framework — a coin scalar the axioms allow, a background the lane already has in another layer (block 17's chessboard states), and an exact algebra against every coupling the campaign supplied, one of which it fails. Second objection: "One heavy and three light — you will be tempted to read that as something." Reply: it is a count, `C(3,0) + C(3,3)` against `C(3,1) + C(3,2)`, and the note says nothing more.

### N8 — Cross-cycle echo
Block 54: three numbers, two set to zero by an added symmetry. Block 68–70: eight exact copies. Here: the axioms' own third number breaks the copies into four levels of one handedness, and a checkerboard number pairs them into masses.

## Falsifiers

- A zero of the walk where `a₀ + 2aΣcos k` differs from `a₀ + 2a(3 − 2|n|)`, or a level with species of both senses.
- A state and field for which `ε` fails to anticommute with one of the odd operators of T3(a), or fails to commute with the reach-two term.
- A mass at a zero other than `√(m² + 36a²)` or `√(m² + 4a²)`.

## Boundaries and non-claims

Neither the `a`-term nor the staggered term is declared present. Which levels are filled is outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom and its proper rotations; the Qubit axiom; the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 65, 69, 70 (PRs #8570, #8592, #8593, #8596, #8601, #8602, open): restated or placed.
- Named standard imports at definition level: the algebra of shifts and site signs; `2 × 2` eigenvalues.
- Reference only: Kogut and Susskind.

## Review record
Supervisor-run block, the twenty-fifth of the source-link direction; the second after the fork probe (`FORK_PROBE_source_link_20260922.md`, four lenses). Lens pass, in writing, by the supervisor: a foundations lens — the inversion of block 54 T1(c) was conditional there and is not an axiom symmetry; the family with `a` is the axioms' own, and the note keeps it as such without proposing a value; the staggered term is a background and is presented as supplied. A rigour lens — the first draft claimed `ε` anticommutes with the reach-two strain term; the runner refuted it (that term moves an even number of steps), and T3 now states the commutation, which turns out to align with block 70's finding that reach two alone breaks the energy reversal; the control's first acceleration estimate carried a stray factor two and a second difference over a range where the rate had changed; it now uses the release from rest and names the momentum-spread correction. A strategy lens — fork 5 (rest energy) acquires a nearest-neighbour mechanism inside `M₂(ℂ)`, at the price of a background; block 76's negative on the induction route survives rest energy. Control: as reported under Executed. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_axioms_own_generator_scalar_hop_splits_species_staggered_term_gives_mass_2026_09_22.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
