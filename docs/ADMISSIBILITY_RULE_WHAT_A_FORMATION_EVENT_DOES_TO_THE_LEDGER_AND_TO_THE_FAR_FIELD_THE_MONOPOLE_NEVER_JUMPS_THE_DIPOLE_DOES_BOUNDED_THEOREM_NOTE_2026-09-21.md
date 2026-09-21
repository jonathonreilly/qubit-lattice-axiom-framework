---
claim_id: admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_the_monopole_never_jumps_the_dipole_does_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 56 (open PRs #8568, #8570, #8571, #8573; not adopted), with block 56's setting: the simplest bond energy of weight one, a box whose walls are held at the ambient rate, and the exact static law ((1 - A) + (gamma/12) M) phi = 0, phi = sqrt(w). An amplitude AT REST spread over sites with weights |chi_x|^2 (summing to one) and bare rest energy m is, for that law, a set of bodies at rest with bare energies m_x = m |chi_x|^2 (block 55: e_x = m w_x |chi_x|^2); its ledger is E = sum_x m_x phi_x and its charges are q_x = (gamma/12) m_x phi_x. A FORMATION EVENT replaces it by one record at a site y: a body at rest with bare energy m'. NO RULE for where, when or whether records form is assumed, and none is proposed. (T1) The ledger after the event is m'/(1 + (gamma/12) g_y m'), g_y the potential of 1 - A at y. It equals E iff m' = E/(1 - (gamma/12) g_y E), which exists iff E < 12/(gamma g_y): an amplitude whose ledger exceeds what one site can show cannot become one record with the ledger kept. With the bare energy kept instead (m' = m) the ledger falls. (T2) For every discrete-harmonic h, sum over bonds from a wall site to an interior site of (1 - phi_inside) h_wall = 6 sum_x q_x h_x. With h = 1: the total flux through the walls is (gamma/2) E, so with the ledger kept it does not change when the record forms, wherever it forms: the monopole never jumps. With h a coordinate: the first moment of the wall flux is six times the dipole P = sum_x q_x x. (T3) P goes from Q Xbar to Q y, Q = (gamma/12) E, Xbar the centre weighted by q_x, that is by |chi_x|^2 phi_x; the jump Q (y - Xbar) cannot be removed by any choice of m'. For ANY odds p_y of forming at y (the ledger kept at each y) the mean jump is Q (sum_y p_y y - Xbar): zero for every amplitude when p is proportional to |chi_x|^2 phi_x; equal to Q (probability centre - Xbar) when p is proportional to |chi_x|^2, which is not zero once the rates differ across the amplitude, and its own field suffices for that. (T4) If the amplitude sources nothing (records only), the rates are ambient and the flux through the walls is zero before the event and (gamma/2) m' phi'_y after: a monopole from nothing at every formation event. EXECUTED, NOT CLAIMED: in a 41^3 box at gamma = 0.05 and 1 the wall flux changes by 2e-7 and 4e-6 (the accuracy of the probe for g_y) while the first moments jump by Q (y - Xbar) to five digits at three sites; the charge-weighted, probability and energy-weighted centres differ (-1.8225, -1.8449, -1.7999 along one axis at gamma = 1); under block 57's wall-referred law the change of the field at r = 8, 16, 24 stays below 2 per cent of its largest value until t = 6.0, 13.5, 21.25. In the refuting pass the walls see the quadrupole and the octupole moments as well, and of the three densities |chi|^2, |chi|^2 phi, |chi|^2 phi^2 only the second holds the centre. NOT claimed: that an amplitude which has formed no record sources anything, or that it does not; that a formation event keeps the ledger; any rule of formation or any statement of the parked statistical postulate; bodies with a rest energy (supplied); motion; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_2026_09_21.py
---

# What a formation event does to the ledger and to the far field: the monopole never jumps, the dipole does

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 56, in block 56's setting; no rule of formation is assumed; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger, with the simplest bond energy of weight one; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The decision record of this direction (PR #8572) leaves one fork that touches the Record axiom: does an amplitude that has formed no record source the rate field (block 55's reading), or do only records (block 53's)? The axioms say records form, are permanent and sit one to a site. This note does not decide the fork and assumes no rule for where records form. It asks a narrower, exact question: **when a spread amplitude at rest is replaced by one record at a site, what happens to the ledger and to what the outside sees?** Block 56's law makes it exactly solvable: a spread amplitude at rest is a set of bodies at rest with bare energies `m|χ_x|²`.

1. **The ledger through the event.** Before: `E = Σ m|χ_x|² φ_x`. After: `m'/(1 + (γ/12) g_y m')`. The ledger is kept iff the record's bare energy is `m' = E/(1 − (γ/12) g_y E)` — *more* than the amplitude's, because a point slows its own clock more than a spread does. And it is possible only if `E` is below what one site can show, `12/(γ g_y)`: an amplitude that shows more than that cannot become one record with the books balanced (T1).
2. **The monopole never jumps.** The ledger is what the walls see (block 56). Keep the ledger and the total flux through the walls is the same before and after, wherever the record forms (T2).
3. **The dipole jumps.** The walls also see the first moment of the charges, exactly. It goes from `Q X̄` to `Q y`, where `X̄` is the amplitude's centre weighted by `|χ_x|² φ_x`. No choice of the record's energy removes the jump `Q(y − X̄)`. Every higher harmonic moment is seen too, and changes (T2, T3).
4. **A condition on any rule of formation.** For *any* odds `p_y` of forming at `y`, the mean jump is `Q(Σ p_y y − X̄)`. It vanishes for every amplitude if the odds go as `|χ_x|² φ_x`. For odds that go as `|χ_x|²` it is `Q ×` (probability centre `− X̄`), and that is not zero once the rate differs across the amplitude — which the amplitude's own field already brings about. For odds that go as the energy density `|χ_x|² φ_x²` it is not zero either. The note proposes no rule; it states what any rule would have to satisfy for the centre the outside sees to stay put on average (T3).
5. **If only records source.** Then nothing is seen before the event and `m'φ'_y` after: every formation event makes a monopole appear from nothing. The two readings of the fork differ at leading order in what the outside sees (T4).
6. **Executed.** `41³` box, weak and strong coupling: the flux through the walls unchanged to the accuracy of the solve, the first moments jumping by `Q(y − X̄)` to five digits; under block 57's law with a front the change reaches distance `r` at about `r/(c w̄)`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record (PR #8572), fork 4: 'Does an amplitude that has formed no record source anything? ... what happens to the ledger when a record forms is open'; block 55 (PR #8571): 'whether an amplitude that has formed no record sources anything is not settled'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the owner's fork 4 now has an exact discriminator (a monopole from nothing at every formation, or never) and an exact condition on any rule of formation (the first moment of the odds equals the charge-weighted centre); next: the same event for an amplitude in motion (K not diagonal), and for several records; bond rates and lengths (block 57's open end)"
conditional_surface_status: "T1 to T4 exact for any amplitude at rest and any site in any box with walls at the ambient rate, for the simplest bond energy; T2's flux identity exact for every discrete-harmonic weight; the statement about odds is about any odds and assumes none"
hypothetical_axiom_status: "blocks 53 to 56's clauses; the simplest bond energy; an amplitude at rest with a rest energy; walls at the ambient rate; for T1-T3 that the amplitude sources (block 55) and for T4 that it does not; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, through the Record axiom's statement that a record is permanent, and through the memo's silence on a time metric, amplitude dynamics and a conserved energy. How and where records form is an open gate of the memo and the subject of the parked statistical postulate (registry entry 1); this note assumes nothing about it and makes no statement of it.

- **Setting.** Block 56's: `w = φ²`; `F = (2/γ) Σ_bonds (φ_x − φ_y)²`; walls held at `φ = 1`; `A` the average over the six neighbours; `G` the inverse of `1 − A` inside the box with zero walls, `g_y = G(y, y)`.
- **The amplitude at rest.** Weights `|χ_x|² ≥ 0` summing to one, bare rest energy `m`; by block 55 T2(c) its energy density is `m w_x |χ_x|²`, so in block 56's law it is the diagonal `M = diag(m_x)`, `m_x = m|χ_x|²`. Ledger `E = Σ m_x φ_x`; charges `q_x = (γ/12) m_x φ_x`; `Q = Σ q_x = (γ/12)E`; dipole `P = Σ q_x x`; `X̄ = P/Q`.
- **The record.** One body at rest at `y` with bare energy `m'`; ledger `m'φ'_y`.
- **Discrete-harmonic** `h`: `h_x` equals the average of `h` over the six neighbours at every interior site (constants, coordinates, `x² − y²`, `xyz`, …).
- **Odds.** Any non-negative `p_y` summing to one over sites where T1's condition holds. They are a free input; nothing is said about what they are.
- **Three densities** are compared: `|χ_x|²` (the conserved density of block 54), `|χ_x|² φ_x` (the charge density of block 56) and `|χ_x|² φ_x²` (the energy density of block 55).

The identity behind T2 is the second identity of Green on a lattice. That a sudden localization does not in general keep energy and the centre of energy is the known difficulty of the collapse models of Ghirardi, Rimini and Weber and of Pearle, and the question of what a spread amplitude sources is that of the semiclassical coupling discussed by Diósi and by Penrose. None is used as authority, and no statement of the rule of Born is made or used.

## Prior art and what is new

That localization events and conservation laws pull against each other is well known. What is new is the exact form the question takes inside blocks 53 to 56: the amplitude at rest and the record are both exactly solvable; the ledger can be kept through the event by one explicit bare energy, and only below an explicit bound; what the outside sees is given exactly by harmonic moments of the wall flux; the monopole never jumps and the dipole always does; any rule of formation faces one exact linear condition if the centre the outside sees is to be steady on average, and of the three natural densities only one meets it; and the two readings of the owner's fork differ at leading order. No rule is proposed and no gravitational claim is made.

## Exact target and obligation graph

Target: the effect of one formation event on the ledger and on what the walls see. Obligations: (O1) the ledger before and after; (O2) what the walls see, exactly; (O3) which moments jump, and what any odds would have to satisfy; (O4) the records-only reading. T1–T4 discharge them.

## Theorem T1 — the ledger through the event

*Statement.* `E' = m'/(1 + (γ/12) g_y m')`. `E' = E` iff `m' = E/(1 − (γ/12) g_y E)`, and such an `m' > 0` exists iff `E < 12/(γ g_y)`. With `m' = m` instead, and `y` a site of the largest `g` on the support, `E' ≤ E`.

*Proof.* Block 56 T3(a) gives `E'`; solve for `m'`. `E'` is increasing in `m'` with supremum `12/(γ g_y)`. The ledger is a concave function of the vector of bare energies (it is `(12/γ)` times `1ᵀ(D⁻¹ + G_B)⁻¹1`, a parallel sum), so on the simplex of bare energies with a given total it is smallest at a vertex, and the vertex with the largest `g` is the smallest of those. ∎

A region can show more than any one of its sites can (block 56 T3b). An amplitude spread over such a region, with a ledger above `12/(γ g_y)` for every `y`, cannot become one record with the books balanced. With one record to a site — the Record axiom — a record shows at most `12/(γ g_0)`, `7.9/γ` on `Z³`.

## Theorem T2 — what the walls see

*Statement.* For a static solution with charges `q` and any discrete-harmonic `h`, `Σ_{x inside, y wall, x∼y} (1 − φ_x) h_y = 6 Σ_x q_x h_x`.

*Proof.* `ψ = 1 − φ` vanishes on the walls and `(1 − A)ψ = q` inside. Then `Σ_x h_x q_x = Σ_x [h_x((1 − A)ψ)_x − ψ_x((1 − A)h)_x]`, the second term being zero. The terms with both sites inside cancel by symmetry; the terms with a wall neighbour leave `(1/6) Σ ψ_x h_y`. ∎

With `h = 1` this is block 56's statement that the flux is `(γ/2)E`: keep the ledger and the monopole does not move. With `h` a coordinate the walls read off the dipole; with `x² − y²` or `xyz`, the higher moments. Nothing about the arrangement of charges that a harmonic weight can see is hidden from the walls.

## Theorem T3 — the dipole jumps; a condition on any odds

*Statement.* With the ledger kept, `P' − P = Q(y − X̄)`, whatever `m'` is chosen to be otherwise it would also change `Q`. For odds `p`, the mean of `P' − P` is `Q(Σ_y p_y y − X̄)`. It is zero for every amplitude at rest if `p_y = q_y/Q`. For `p_y = |χ_y|²` it is `Q(X̄_prob − X̄)`, and `X̄_prob = X̄` iff `Σ_x |χ_x|² φ_x (x − X̄_prob) = 0`; for an amplitude on two sites of equal potential `g` with unequal weights this fails, because `φ` is lower at the heavier site.

*Proof.* `P' = q'_y y` with `q'_y = (γ/12) m'φ'_y = Q`. The mean is linear in `p`. For two sites `a, b` with `g_a = g_b = g`, mutual potential `c < g` and `d_a > d_b` (`d = (γ/12)m|χ|²`), block 56 T4 gives `φ_a = (1 + d_b(g − c))/det` and `φ_b = (1 + d_a(g − c))/det`, so `φ_a < φ_b`: the charge weights `d_aφ_a : d_bφ_b` are less unequal than the probability weights `d_a : d_b`, and the charge-weighted centre lies nearer `b`. ∎

The three densities `|χ|²`, `|χ|²φ` and `|χ|²φ²` differ only through the amplitude's own field, by amounts of order `γ`; at weak field and uniform rate they coincide. The statement is a constraint any rule would face, not a rule. It concerns the first moment only.

## Theorem T4 — if only records source

*Statement.* If the amplitude sources nothing, `φ = 1` before the event and the flux through the walls is zero; after it the flux is `(γ/2) m'φ'_y > 0`.

*Proof.* Block 56's law with `M = 0`, and T2 with `h = 1`. ∎

Under the records-only reading the outside sees a monopole appear at every formation event — under the static law at once and everywhere, under block 57's law with a front as a wave that starts at the record. Under block 55's reading with the ledger kept it sees the monopole never change. That is a difference at leading order between the two answers to the owner's fork. The note does not choose.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block58_formation.py` — a two-lump amplitude at rest (bare energy 6) in a `41³` box; records at three sites; the record's bare energy from T1, with `g_y` read from a probe.

| | ledger | record's bare energy | wall flux changed by | first moments of the flux / 6 jumped by, against `Q(y − X̄)` |
|---|---|---|---|---|
| `γ = 0.05` | 5.985594 | 6.2174, 6.2173, 6.2173 | `+2×10⁻⁷` | `(−0.028836, −0.007208, 0.000001)` against `(−0.028836, −0.007209, 0)`; `(0.170685, 0.042672, …)` against `(0.170684, 0.042671, 0)`; `(0.045984, 0.092552, −0.074819)` against `(0.045984, 0.092551, −0.074820)` |
| `γ = 1` | 5.725552 | 19.976, 19.946, 19.954 | `+4×10⁻⁶` | `(−0.561796, −0.140465, …)` against `(−0.561807, −0.140478, 0)`; `(3.255243, 0.813795, …)` against `(3.255228, 0.813781, 0)`; `(0.869593, 1.768055, −1.431378)` against `(0.869581, 1.768040, −1.431388)` |

Centres along the first axis, relative to the box centre, at `γ = 1`: charge-weighted `−1.8225`, probability `−1.8449`, energy-weighted `−1.7999` (at `γ = 0.05`: `−1.8438, −1.8449, −1.8426`). Before the event the first moments of the flux divided by six equal `Σ q_x x` to six digits. The same event under block 57's wall-referred law at weak field (`61³` box, the source changing from a spread of radius about 4 to a point with the monopole kept): the change of the field at `r = 8, 16, 24` stays below 2 per cent of its largest value until `t = 6.0, 13.5, 21.25`.

## No-Go Discipline Gate

The note's negative sentences: above `12/(γ g_y)` no single record keeps the ledger; no choice of the record's energy removes the dipole's jump; odds that go as `|χ|²` or as the energy density do not hold the centre on average.

### N1 — Routes by which the sentences could fail
1. *A record spread over several sites.* The Record axiom has one record to a site; several records could share the ledger and then the bound is that of block 56's capacity. Not worked.
2. *A ledger that is not kept through a formation event.* Possible; then the outside sees the monopole change by the amount of T1's second sentence. The note states both.
3. *An amplitude in motion.* Then `K` is not diagonal (block 56, Remark to T1), the charges are `φ_x(Kφ)_x` with bond parts, and a record "at rest" does not carry the momentum. Not worked.
4. *Another bond energy.* T2 holds for every bond energy of weight one in the form "the ledger is a surface term"; the harmonic-moment identity uses the linear law of the simplest one. T1's bound changes (block 56's second member stops a clock at `18/γ`).
5. *Records that move* (the owner's reading of 2026-09-20). Then the record is an amplitude again after it forms, and the event is a change of shape, not a freezing. Not worked.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Everything is in block 56's setting: the simplest bond energy, bodies at rest with a rest energy (supplied), walls at the ambient rate. The event is instantaneous and the law is static; the control with a front is at weak field. The statement about odds requires the ledger to be kept at every site that has positive odds. It is a statement about first moments; it does not single out one rule.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; a record is permanent and sits one to a site; the absences that motivate the clauses | yes (premise) |
| block 56 (open PR #8573) | the exact static law, the ledger `Σ m φ`, the surface term, saturation, monotonicity | yes (restated) |
| block 55 (open PR #8571) | the energy density of an amplitude at rest; the two readings of the source | yes (restated) |
| block 57 (open PR #8578) | the wall-referred law used in the control | executed comparison |
| decision record (open PR #8572) | fork 4 | placement |
| registry entry 1 (`docs/repo/DEFERRED_DECISIONS.md`) | the parked statistical postulate | not used; named so that it is clear nothing of it is assumed |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "ledger kept iff `m' = E/(1 − (γ/12)g_yE)`, only below `12/(γg_y)`; wall flux moments = harmonic moments of the charges; monopole fixed, dipole jumps by `Q(y − X̄)`; mean over any odds; records only: a monopole from nothing" | executed: exact rates of a five-site amplitude and of its record in a `7³` box | executed: the record's bare energy; the ledger's fall with the bare energy kept; a seven-site amplitude no single site can hold | executed: the total wall flux and its three first moments before and after, against the ledger and six times the dipole | executed: the dipole's jump; mean jumps for two kinds of odds; records-only flux | any amplitude at rest, any site, any box with walls at the ambient rate, simplest bond energy; T2 for every discrete-harmonic weight; the odds are arbitrary; the fork itself not decided |

### N6 — Partial-closure paths and primitive scan
`realized_state_primitive` grants evaluation at a supplied state and supplies no rule of formation, no odds and no density; it is not used. `scale_reference_primitive` and `kinetic_isotropy_primitive` do not bear on the event. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is the parked postulate by the back door." Reply: no odds are assumed, derived or proposed. T3 is a linear identity valid for every choice of odds, stated so that whoever takes up the parked question knows one exact constraint the clauses of blocks 53 to 56 would put on it; the note names the registry entry to make plain that nothing of it is used. Second objection: "A spread amplitude at rest with a rest energy is two supplied things at once." Reply: yes (blocks 54 to 56 say so); the note is exact within that setting and lists motion as not worked. Third objection: "Bare energy is not observable, so T1 says nothing." Reply: what is observable from outside is the ledger, and T1's content is the bound: above `12/(γg_y)` no bare energy works.

### N8 — Cross-cycle echo
Block 41 made a source a record; block 53 let a record enter as `log κ`; block 55 made the source the amplitude's energy density and left the two unreconciled; block 56 made both exactly solvable. Here the two readings are set side by side for one event, and they differ in the first thing the outside sees. Block 24 (unrecorded sites) asked a related question of the record layer: when is a window with unrecorded sites the same as the integrated exterior; there too the answer turned on what the unrecorded part is allowed to do.

## Falsifiers

- An amplitude at rest and a site `y` with `E < 12/(γg_y)` for which `m' = E/(1 − (γ/12)g_yE)` does not keep the ledger, or with `E ≥ 12/(γg_y)` for which some `m'` does.
- A static solution and a discrete-harmonic `h` for which the wall sum differs from `6Σ q_x h_x`.
- A formation event with the ledger kept whose dipole does not jump by `Q(y − X̄)`.
- Odds proportional to `|χ_x|²φ_x` with a non-zero mean jump; an amplitude on two sites with unequal weights whose probability centre equals `X̄`.

## Boundaries and non-claims

The note does not decide whether an amplitude that has formed no record sources anything, nor whether a formation event keeps the ledger; it computes both cases. It assumes and proposes no rule of formation and makes no statement of the parked statistical postulate; T3 is an identity in arbitrary odds and concerns first moments only. Everything is in block 56's setting: the simplest bond energy, supplied bodies at rest with a rest energy, walls at the ambient rate, a static law. Motion, several records and records that move are not worked. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom; the Record axiom (a record is permanent; one to a site); the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 55, 56, 57 and the decision record (PRs #8571, #8573, #8578, #8572, open): restated or placed.
- Named standard imports at definition level: the second identity for the lattice operator `1 − A`; discrete-harmonic functions; concavity of a parallel sum.
- Reference only: Green; Ghirardi, Rimini and Weber; Pearle; Diósi; Penrose; Born (not used).

## Review record
Supervisor-run block, the sixth of the source-link direction and the second of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the block sits next to the parked statistical postulate; the rule adopted for it is that no odds are assumed, derived or proposed, every statement about odds is an identity in arbitrary odds, the registry entry is named as not used, and the fences are kept verbatim; the Record axiom's "permanent" and "one to a site" are what make the event a replacement of a spread by a point. A rigour lens: "iff" in T1 is for the explicit scalar equation; the bound comes from block 56's supremum; `m' ≥ m` needs the site of largest potential (or `Z³`) and is stated so; T3's "only one of three densities" is a statement about those three, and the refuting pass checks it on random amplitudes. A comparator lens: the tension between localization and conservation is known from collapse models; named under the Premises and Prior art. A strategy lens: the block turns the owner's fork 4 into two exact alternatives that differ at leading order, and hands any future work on formation one exact constraint. Refuting pass (`specs/supervisor_control_block58_refuter.py`, machinery disjoint from the runner's): W1 the record's bare energy by root-finding on the ledger, against the closed form (`2×10⁻¹³`), and the wall flux (`8×10⁻¹⁴`); W2 the flux identity with the weights `x² − y²`, `xyz`, `x² + y² − 2z²` (`10⁻¹³`) and its failure for `x²` (0.36); W3 thirty random amplitudes: distance between the mean site of formation and the centre the walls see, by density: probability `0.043` sites, charge `0`, energy `0.043`; W4 midpoint concavity of the ledger for 200 random pairs, and `m' ≥ m` at the site of largest potential. All pass. Findings folded: the supervisor's first expectation was that the *energy* density would hold the centre (block 55 makes the energy density the source); the computation shows it is the *charge* density `|χ|²φ` of block 56, the energy density missing by as much as the probability density, on the other side. The control first carried an unfinished comparison of the far field with a dipole formula; it was removed in favour of the exact flux moments. Mutation census: 9 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
