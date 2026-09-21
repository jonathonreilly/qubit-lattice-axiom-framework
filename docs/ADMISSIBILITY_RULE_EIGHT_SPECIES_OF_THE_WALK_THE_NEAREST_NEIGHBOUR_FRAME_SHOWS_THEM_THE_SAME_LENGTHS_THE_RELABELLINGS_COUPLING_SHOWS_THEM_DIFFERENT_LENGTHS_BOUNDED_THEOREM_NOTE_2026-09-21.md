---
claim_id: admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 59, 62, 63 and 64 (open PRs #8570, #8581, #8592, #8593, #8595; not adopted): block 54's walk H(k) = sum_a sigma_a sin k_a with the qubit as coin; the two couplings of lengths to it found so far: block 62's nearest-neighbour FRAME, H(k) = sum_j (E^j.sigma) sin k_j, and blocks 63 and 64's bond STRAIN coupled as the deformation a relabelling generates, with second-neighbour reach, H(k) = sum_a sigma_a [sin k_a + cos k_a sum_j B_a^j sin k_j]; block 59's ratio of a ray's bending to a slow body's fall. Block 63 left the choice between the two as a fork: the first misses the walk's conserved current at second order in the wave numbers, the second meets it exactly. (T1) H(k)^2 = sum_a sin^2 k_a vanishes at the eight wave vectors with every k_a in {0, pi}; near k = pi n + q the walk is sum_a D_a sigma_a q_a, D = diag((-1)^n_a): eight species of walker with the same top speed. A rate multiplies H, so every species feels the same force, energy x gradient, and falls alike. (T2) For a uniform frame H^2 = sum_ij g^ij sin k_i sin k_j at every wave vector, so species n sees, in its own wave vector q, the inverse metric D g D: the same three lengths as every other species; the angle between axes i and j with the opposite sign iff n_i != n_j. (T3) For a uniform strain H^2 = sum_a [sin k_a + cos k_a (B s)_a]^2 exactly, and species n sees the inverse metric (1 + B D)^T (1 + B D): a stretch b of the bonds along a is (1 + b)^2 for species with n_a = 0 and (1 - b)^2 for species with n_a = 1. (T4) With lengths l = (wbar/w)^beta the ratio of bending to fall is 1 + beta for all eight species under the frame; under the strain coupling it is 1 - beta for a species with n_a = 1 moving along a: no bending at all for beta = 1. EXECUTED, NOT CLAIMED: packets of species (0,0) and (1,0) on a 160 x 128 slice crossing a gradient of the stretch of the x-bonds: sideways displacements (part odd in the stretch) -15.06 and -15.06 under the frame, -12.64 and +12.64 under the strain coupling; distances travelled in a uniform stretch 0.2: 39.2 and 39.2 under the frame, 35.5 and 29.5 under the strain coupling. NOT claimed: which coupling the framework has; whether the eight species are all physical or some are to be removed (block 54 named the walk's eight zero-energy points under its prior art; the campaign has not examined them until now); non-uniform frames and strains beyond the executed control; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_2026_09_21.py
---

# Eight species of the walk: the nearest-neighbour frame shows them the same lengths; the relabelling's coupling shows them different lengths

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about block 54's supplied walk and the two supplied couplings of blocks 62 to 64; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for the two couplings of lengths to them found in blocks 62 to 64; it reports what each of the walk's eight species sees of a frame and of a strain; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 63 (open PR #8593) left a fork. The walk conserves momentum exactly through a current that a *relabelling* generates, and that coupling reaches second neighbours. Block 62's *frame* talks to nearest neighbours only and misses that current by the cosine of the wave number. Block 64 (open PR #8595) took the relabelling's side and found the static equations exactly consistent. Which side to take was left to the owner, with one argument on each side: exact books against nearest-neighbour reach. This note adds a second argument, and it is not a small one.

Block 54's walk has **eight species**. Its energy vanishes not only at zero wave vector but wherever each wave number is 0 or `π`; near each of those eight points it is a walker with top speed one. Block 54 named the eight points under its prior art and went no further; the campaign's packets and rays have all been of the first species. The other seven are as much solutions of the supplied clause as the first.

1. **Clock rates treat the eight alike.** A rate multiplies the whole generator; every species falls the same (T1).
2. **The nearest-neighbour frame shows all eight the same lengths.** Its energy squared is the metric form in the *sines* of the wave numbers, exactly, everywhere. A species with reflected axes sees the same three lengths, and mirrored angles (T2).
3. **The relabelling's coupling shows them different lengths.** There the stretch enters through the *cosine* of the wave number, which is `+1` for some species and `−1` for others. A bond that is stretched for one species is compressed for another (T3).
4. **So the bending is not universal under that coupling.** With lengths that give the full bending for the first species (`β = 1`), a species reflected along its direction of motion bends by `1 − β` times its fall: not at all. Under the frame all eight bend alike (T4).

In plain terms: the walker comes in eight kinds, which differ in how their wave number sits on the lattice. Slow clocks pull all eight the same. If lengths are told to the walker through the way its coin is set against the bonds, all eight see the same lengths and bend alike. If lengths are told to it the way a relabelling of the sites would — the coupling that keeps the momentum books exactly — then, for a stretch along any one axis, half the kinds see it as a squeeze, and light of those kinds would bend the wrong way or not at all. Exact books, or one set of lengths for all kinds: with the two couplings found so far, not both.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 63 (PR #8593), next_trace_action: 'whether the second-neighbour coupling keeps block 62 T1 (H^2 as a metric) and what it does to the walker's top speed; ... the owner's decision between the two'; decision record (PR #8572), third addendum, fork (iii): 'May a coupling reach second neighbours?'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether the eight species are all to be kept (block 54's clause has them; removing seven needs a term that the clause does not contain, or a reading under which they are one object); a coupling that keeps BOTH the exact current and species-blind lengths, if any (for instance through a momentum that is the same for all species); the owner's fork between the two couplings, now with this on the scale"
conditional_surface_status: "T1 to T3 exact for every uniform frame, strain and rate and every wave vector; T4 exact for rays at first order in the log rate"
hypothetical_axiom_status: "block 54's clause (the walk); block 62's frame; blocks 63 and 64's strain with the relabelling's coupling; block 59's lengths l = (wbar/w)^beta; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule as the model for "nearest-neighbour", and the memo's silence on amplitude dynamics. Blocks 54, 59, 62, 63, 64 (open PRs) supply the walk, the ratio of bending to fall, and the two couplings.

- **Walk.** `H(k) = Σ_a σ_a s_a`, `s_a = sin k_a`, `c_a = cos k_a`. **Species** `n ∈ {0, 1}³`: wave vectors `k = πn + q` with `q` small; `D = diag((−1)^{n_a})`; then `s = D sin q`, `c = D cos q`.
- **Frame coupling** (block 62): `H(k) = Σ_j (E^j·σ) s_j`, `g^{ij} = Σ_a E_a^i E_a^j`.
- **Strain coupling** (blocks 63, 64): `H(k) = Σ_a σ_a [s_a + c_a Σ_j B_a^j s_j]` for a uniform strain — the symbol of `σ_a ½{C_a[B_a^j], S_j}`.
- **Rates.** `H → wH` for a uniform rate (block 54).
- **Bending over fall** (block 59 T4): for a ray, `d log(`hop rate along its direction of motion`)/du`.

That a lattice walker built on the symmetric difference has `2^d` species is the doubling of Nielsen and Ninomiya, and the remedies that remove the extra species by terms reaching further or breaking a symmetry are those of Wilson and of Kogut and Susskind. None is used as authority, and none of the remedies is applied here.

## Prior art and what is new

The eight species are classical. New, inside the framework's vocabulary: that the campaign's supplied walk has them and that they now matter — the two couplings between which block 63 left a fork differ at *order one* on seven of the eight species; that the nearest-neighbour frame is species-blind in the lengths exactly and mirrors the angles; that the relabelling's coupling reverses the sign of a stretch for a species reflected along that axis, and with it the bending. No gravitational claim is made.

## Exact target and obligation graph

Target: what the walk's species see under the two couplings. Obligations: (O1) the species and the rates; (O2) the frame; (O3) the strain; (O4) the bending. T1–T4 discharge them.

## Theorem T1 — eight species, falling alike

*Statement.* (a) `H(k)² = Σ_a sin² k_a`; it vanishes iff every `k_a ∈ {0, π}`: eight wave vectors. (b) Near `k = πn + q`, `H = Σ_a D_a σ_a q_a + O(q³)`. (c) For a uniform rate `H → wH`: the energy of every species is `w` times a function of the sines that does not depend on the species.

*Proof.* The three coin matrices anticommute; `sin(πn_a + q_a) = (−1)^{n_a} sin q_a`. ∎

By block 54 the force on every state is its energy times the gradient of the log rate; the eight species fall alike.

## Theorem T2 — the frame: the same lengths, mirrored angles

*Statement.* For a uniform frame and every `k`, `H(k)² = Σ_ij g^{ij} s_i s_j`. In the species' own wave vector, `H² = Σ_ij (DgD)^{ij} sin q_i sin q_j`: the diagonal of `DgD` is that of `g` for every species, and `(DgD)^{ij} = −g^{ij}` iff `n_i ≠ n_j`.

*Proof.* Block 62 T1 and `s = D sin q`. ∎

## Theorem T3 — the strain: different lengths for different species

*Statement.* For a uniform strain and every `k`, `H(k)² = Σ_a [s_a + c_a(Bs)_a]²`. Near `k = πn + q`, `H² = qᵀ(1 + BD)ᵀ(1 + BD)q + O(q⁴)`. For `B = diag(b, 0, 0)` the entry along axis 1 is `(1 + b)²` if `n_1 = 0` and `(1 − b)²` if `n_1 = 1`.

*Proof.* Anticommutation gives the sum of squares. With `s = Dq`, `c = D` at leading order, `s_a + c_a(Bs)_a = D_a[q + BDq]_a`. ∎

The reason is visible in block 63 T2: a relabelling is generated with the lattice's own momentum `S_j`, whose symbol `sin k_j` has the sign `D_j` on species `n`; what it generates carries the hop `C_a`, whose symbol `cos k_a` has the sign `D_a`. The exactly conserved momentum of block 63 is, species by species, `D` times the species' own.

## Theorem T4 — the bending

*Statement.* Let `ℓ = (w̄/w)^β` (block 59). (a) Carried by the frame, `E = (1/ℓ)·1`, the hop rate along every axis is `w/ℓ` for every species and the ratio of bending to fall is `1 + β`. (b) Carried by the strain coupling, `1 + b = 1/ℓ`, a species with `n_a = 1` has the hop rate `w(1 − b)` along `a` and the ratio `1 − β` for motion along `a`.

*Proof.* Block 59 T4 with T2 and T3; `log(1 − b) = −b + … = −βu + …` where `log(1 + b) = +βu…` has the other sign. ∎

## Executed (supervisor control; floating point; real space; evidence, not proof)

`specs/supervisor_control_block68_species.py`: a two-dimensional slice of the walk on a `160 × 128` torus with a stretch of the x-bonds `b(y) = 0.2 sin(2πy/128)`, carried by the frame (on the sites, symmetrised) or by the strain coupling (on the bonds). Packets of species `(0, 0)` and `(1, 0)`, wave number `0.6` from their zero, moving along `+x` through the largest gradient, `T = 60`. Sideways displacement, part odd in the stretch: `−15.06` and `−15.06` under the frame; `−12.64` and `+12.64` under the strain coupling — the second species is pushed the other way. In a uniform stretch `0.2`, distance travelled in `T = 40`: `39.2` and `39.2` under the frame (`(1 + b) cos q × 40 = 39.6`); `35.5` and `29.5` under the strain coupling (`(cos q ± b cos 2q) × 40 = 35.9, 30.1`); the packets' spread in wave number accounts for the one to two per cent.

## No-Go Discipline Gate

The note's negative sentences: under the relabelling's coupling the species do not see the same lengths and do not bend alike; under the frame they do not see the same angles.

### N1 — Routes by which the sentences could fail
1. *Fewer species.* If seven species are removed, or are one object with the first under some reading, the sentences lose their subject. Block 54's clause does not remove them; a term that does would reach further or break a symmetry of the walk. Not examined.
2. *Another relabelling.* T3's sign comes from generating relabellings with `S_j`. A momentum whose symbol has the same sign on all species (none exists within nearest-neighbour hops that vanishes at all eight zeros with slope `+1`) would give another coupling. Not examined.
3. *Both at once.* A coupling with the exact current *and* species-blind lengths is not excluded by this note.
4. *Mirrored angles.* Under the frame the angle's sign flips for species with `n_i ≠ n_j`; for such a species this is the same as looking at the sheared lattice in a mirror, but the metric's components are not mirrored with it. Whether that is observable depends on what else distinguishes species.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Uniform frames, strains and rates in T1 to T3 (the control has slowly varying ones). First order in the log rate in T4. Identity coin frame for the strain coupling.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra; nearest-neighbour as the Admissibility rule's form | yes (premise) |
| block 54 (open PR #8570) | the walk; force = energy × gradient for every state | yes (restated) |
| block 62 (open PR #8592) | the frame; `H² = g^{ij}s_is_j` | yes (restated) |
| blocks 63, 64 (open PRs #8593, #8595) | the relabelling's deformation; the strain coupling; the fork | yes (restated) |
| block 59 (open PR #8581) | bending over fall | yes (restated) |
| decision record (open PR #8572) | fork (iii) of the third addendum | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "eight species falling alike; the frame shows them `DgD`; the strain shows them `(1 + BD)ᵀ(1 + BD)`; bending `1 + β` against `1 − β`" | executed: `H²` at rational sines for all eight sign patterns; the zeros on the grid of wave numbers `0, π/2, π, 3π/2`; the walk near each | executed: the strain coupling applied in real space to plane waves of three species on a `4³` torus against the wave-vector form at all 64 sites | executed: for a uniform rational frame, `H²` against `g^{ij}s_is_j` and `DgD` at all eight species' wave vectors; for a uniform rational strain, `H²` against the sum of squares; the species' inverse metric for a general strain by exact symbolic expansion | executed: the ratio of bending to fall for the two couplings and the two signs | T1–T3 every uniform frame, strain, rate and wave vector; T4 rays at first order; non-uniform fields in the control only; which coupling, and whether all species are physical, not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Doublers are a lattice artefact; nobody keeps them." Reply: in a theory that has a continuum to go to, perhaps. Here the lattice is the first axiom and block 54's clause is what was supplied: its walk has eight species, and any reading that discards seven is a further clause that the owner would have to supply. Until then a statement like "the bending is twice the fall" needs the qualifier "for which species", and this note says for which. Second objection: "This kills the relabelling's coupling." Reply: it puts a weight on the scale; block 63's exact current is a weight on the other side, and N1.3 leaves room for a coupling with both. Third objection: "Why was this not seen in block 54?" Reply: block 54 named the eight zero-energy points, but its packets and rays were of the first species, and rates do not distinguish species (T1); lengths are what does.

### N8 — Cross-cycle echo
Block 54: the walk; inversion an added symmetry; direction dependence of second order — for the first species. Block 62: `H² = g^{ij}s_is_j`. Block 63: a relabelling brings the cosine. Block 64: the relabelling's side taken. Here: the cosine's sign.

## Falsifiers

- A wave vector other than the eight at which the walk's energy vanishes.
- A uniform frame and species for which the diagonal of the seen inverse metric differs from `g`'s.
- A uniform strain and species `n` whose seen inverse metric is not `(1 + BD)ᵀ(1 + BD)`.
- A species with `n_a = 1` that, under the strain coupling, bends by `1 + β` times its fall along `a`.

## Boundaries and non-claims

The note does not choose between the couplings and does not say the eight species are all physical; it says what each coupling shows each species. Non-uniform frames and strains are executed only. Angles under the strain coupling, the species' response to the disturbances of block 62, and any coupling beyond the two are outside. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the nearest-neighbour form of the Admissibility rule, and the memo's silence on amplitude dynamics. Blocks 54, 59, 62, 63, 64 and the decision record (PRs #8570, #8581, #8592, #8593, #8595, #8572, open): restated or placed.
- Named standard imports at definition level: anticommutation of the coin's matrices; `sin(π + q) = −sin q`, `cos(π + q) = −cos q`; expansion to second order; rays of an energy function.
- Reference only: Nielsen and Ninomiya; Wilson; Kogut and Susskind.

## Review record
Supervisor-run block, the sixteenth of the source-link direction and the twelfth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: nothing new is supplied; the species are a property of block 54's clause, named there and not examined since (the supervisor first wrote that the campaign had never raised them; a search of the fifteen earlier notes found block 54's sentence, and the wording was corrected), and the note must say so plainly rather than treat them as a nuisance; it must not choose the coupling. A rigour lens: all statements are identities at rational sines or exact symbolic expansions; the resolution line for sites was first empty ("not a site-resolved block") and a real-space check of the strain coupling on plane waves of three species was added instead; in the control, an explanatory line gave the speeds as `(1 ± b cos q)` — they are `cos q ± b cos 2q` — and was corrected before the note was written. A comparator lens: the doubling and its remedies, named under the Premises, none applied. A strategy lens: block 63's fork now has a weight on each side — exact books against one geometry for all species — and the owner should see both before choosing. Control (`specs/supervisor_control_block68_species.py`, sparse real-space evolution, machinery disjoint from the runner's): packets of two species under the two couplings, as reported under Executed. Mutation census: 9 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
