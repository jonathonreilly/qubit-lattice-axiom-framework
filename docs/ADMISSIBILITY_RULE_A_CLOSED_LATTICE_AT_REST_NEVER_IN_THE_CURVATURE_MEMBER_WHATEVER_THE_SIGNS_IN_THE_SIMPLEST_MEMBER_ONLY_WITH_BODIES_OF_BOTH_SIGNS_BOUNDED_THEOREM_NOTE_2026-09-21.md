---
claim_id: admissibility_rule_a_closed_lattice_at_rest_never_in_the_curvature_member_whatever_the_signs_in_the_simplest_member_only_with_bodies_of_both_signs_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 55, 56, 60 and 71 (open PRs #8571, #8573, #8590, #8603; not adopted): a ledger of rates (and, in block 60, lengths) with bodies at rest as its content, e_z = m_z w_z, the bare energies m_z of EITHER sign (block 71); the two supplied static members - block 56's simplest bond energy, F = (2/gamma) sum_bonds (phi_x - phi_y)^2 with phi = sqrt(w), whose law is (2/gamma)(-Delta phi)_z + m_z phi_z = 0, and block 60's curvature member, (Delta chi)_z = -mu_z/chi_z, (Delta N)_z = (Q_z/chi_z) N_z, Q_z = mu_z/chi_z, mu = m/(8K), w = N/chi; and a CLOSED lattice: a torus, no walls, every rate (and length) a variable. Block 60 T1: with every rate varied the ledger's total vanishes; block 60 found no closed lattice at rest for positive bodies; block 71 admitted negative ones and left 'a ledger whose total is zero' unexamined. (T1) For a positive function f on a closed lattice, sum_z (Delta f)_z/f_z = sum over bonds of (f_x - f_y)^2/(f_x f_y), which is positive unless f is uniform. (T2) Curvature member: if the lengths' equation holds, then for every positive N the residuals of the rates' equation per unit rate sum to sum_bonds (dN)^2/(N N') + sum_bonds (dchi)^2/(chi chi'); so both equations hold with positive fields only if both fields are uniform and there are no bodies: NO closed lattice is at rest in the curvature member, whatever the number, places and signs of the bodies. (T3) Simplest member: a closed lattice at rest with positive rates has sum m = (2/gamma) sum_bonds (dphi)^2/(phi phi') > 0 and sum m w = -F < 0, hence bodies of both signs, the negative ones sitting at the faster clocks, and the ledger's total is exactly zero; conversely every positive phi is at rest for the bare energies the law assigns to it. For two bodies it is at rest iff m_A > 0 > m_B and 1/|m_B| - 1/m_A = gamma (G_0 - G_d), G the closed lattice's zero-mean unit-source potential and d the separation; then phi = c - p(G_A - G_B) with every rate positive. EXECUTED, NOT CLAIMED: on a 6x6x6 torus the pair (3t, -2t) is at rest at t* = 1.529829 numerically and by the closed form; three bodies (3, -1, -3/2)t at t* = 0.802959 with a positive lowest mode; the closed form against the numerical root on tori of side 4, 6, 8 to six digits; in the curvature member a least-squares search with the mean length held never reaches zero residual, and the residual can be made small only by inflating every length (never attained). NOT claimed: anything about content that moves or about fields that move; that a closed lattice is or is not the framework's arena; which amplitudes are present; stability of the configurations at rest; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_closed_lattice_at_rest_curvature_member_never_simplest_member_both_signs_2026_09_21.py
---

# A closed lattice at rest: never in the curvature member, whatever the signs; in the simplest member only with bodies of both signs

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about two supplied static members on a closed lattice; nothing adopted or registered; unaudited)

This note works within supplied clauses for a ledger of rates and lengths with bodies at rest as its content; it reports when a closed lattice can be at rest in the two supplied static members once bodies of negative bare energy are admitted; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

On a closed lattice there are no walls to hold a rate, so every rate is a variable, and block 60 (open PR #8590) showed that the ledger's total must then vanish. With positive bodies only, that cannot happen at rest. Block 71 (open PR #8603) admitted bodies of negative bare energy and left the question open: can a closed lattice then sit still, with the books summing to zero?

1. **One identity** (T1). For any positive function on a closed lattice, the sum of its lattice Laplacian divided by the function is a sum of squares over the bonds.
2. **Curvature member: never** (T2). The lengths' equation and the rates' equation feed the identity with *opposite* signs, so the two sums of squares must add to zero: both fields are uniform and there is nothing there. No number, placing or choice of signs of bodies at rest escapes.
3. **Simplest member: only with both signs, and then exactly on a surface** (T3). At rest, the bare energies must sum to a positive number while the energies counted in local ticks sum to a negative one — the negative bodies sit at the faster clocks — and the ledger's total is exactly zero. For a pair the condition is a closed form: `1/|m_B| − 1/m_A = γ(G_0 − G_d)`.

Executed: a pair and a triple found at rest numerically at the predicted scale, with every rate positive; in the curvature member a search finds no configuration at rest.

In plain terms: take a universe with no edge. If the field's energy is the curvature of the stretched lattice, such a universe cannot sit still, no matter how ordinary and negative bodies are mixed. If the field's energy is the simplest one, it can — but only if it contains both ordinary and negative bodies, tuned so that the books sum to exactly nothing.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 71 (PR #8603), next_trace_action and queue: 'a ledger whose total is zero' - block 60 T1 (all rates varied => total zero) read together with negative bodies; block 60: no closed lattice at rest for positive bodies."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the two members part ways on a closed lattice: the curvature member has no rest whatever the content at rest; the simplest member has rest on a surface of bare energies of both signs; next: content that moves (does hop energy change T2?); stability of the pair at rest; the owner's fork on which amplitudes are present"
conditional_surface_status: "T1 exact for every positive function on every finite closed lattice (any graph without boundary); T2 exact for every number, place and sign of bodies at rest; T3 exact, with the pair in closed form"
hypothetical_axiom_status: "block 55's ledger; the static members of blocks 56 and 60; bodies at rest of either sign; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom and the memo's silence on rates and on amplitude dynamics. Blocks 55, 56, 60, 71 (open PRs) supply the objects.

- **Closed lattice.** A finite torus; `Δ` the lattice Laplacian (sum over the six neighbours minus six times the value). `Σ_zΔf_z = 0` and `Δ` is symmetric.
- **Simplest member** (block 56). `φ = √w`; law `(2/γ)(−Δφ)_z + m_zφ_z = 0`; `F = (2/γ)Σ_bonds(φ_x − φ_y)²`; content `Σm_zw_z`.
- **Curvature member** (block 60 T4's equations, whose derivation does not use the sign of `m`; block 71 T3). `(Δχ)_z = −μ_z/χ_z`; `(ΔN)_z = (Q_z/χ_z)N_z`, `Q_z = μ_z/χ_z`; lengths `χ² > 0`, rates `w = N/χ > 0`.
- **Potential.** `G`: `−ΔG = δ_0 − 1/V`, `ΣG = 0`; `G_0` its value at the source, `G_d` at separation `d`.

Nothing classical is used beyond summation by parts.

## Prior art and what is new

That a static closed universe needs a balance of attraction and repulsion is an old theme (Einstein's static universe of 1917 is the classical instance; named here only). New, inside the framework's vocabulary: the identity and its two uses — an exclusion in the curvature member that holds for bodies of any signs, and in the simplest member the exact conditions of rest, with the pair in closed form and the ledger's total exactly zero. No gravitational claim is made.

## Exact target and obligation graph

Target: whether a closed lattice can be at rest with bodies of both signs. Obligations: (O1) a tool; (O2) the curvature member; (O3) the simplest member. T1–T3 discharge them.

## Theorem T1 — an identity

*Statement.* For `f > 0` on a closed lattice: `Σ_z(Δf)_z/f_z = Σ_bonds(f_x − f_y)²/(f_xf_y)`. It is positive unless `f` is uniform.

*Proof.* `Σ_z(Δf)_z/f_z = Σ_bonds[(f_y − f_x)/f_x + (f_x − f_y)/f_y] = Σ_bonds(f_y − f_x)(1/f_x − 1/f_y)`. The lattice is connected. ∎

## Theorem T2 — the curvature member: never

*Statement.* Let `χ > 0` satisfy the lengths' equation on a closed lattice for some bare energies of any signs, and let `N > 0` be any function. Then `Σ_z[(ΔN)_z − (Q_z/χ_z)N_z]/N_z = Σ_bonds(N_x − N_y)²/(N_xN_y) + Σ_bonds(χ_x − χ_y)²/(χ_xχ_y)`. Hence the rates' equation holds at every site only if `N` and `χ` are uniform, and then every `μ_z = 0`.

*Proof.* By T1 for `N`, the first part of the left side is the first sum of squares. `Σ_zQ_z/χ_z = −Σ_z(Δχ)_z/χ_z`, which by T1 is minus the second sum of squares. If `χ` is uniform, `Q = −Δχ = 0`. ∎

Necessary conditions for rest follow without positivity: `ΣQ_z = 0`, `ΣQ_zw_z = 0`, and, from `Σ_z(NΔχ − χΔN) = 0`, `Σm_zw_z = 0` — the content's energy in local ticks would have to vanish by itself. For two bodies these already contradict each other (`w_A = w_B`, `m_A = −m_B`, and then `χ_A = χ_B` against `χ_A − χ_B = 2Q(G_0 − G_d)`). T2 closes every case at once.

With held walls the identity acquires a wall term, and rest exists (block 60 T4; block 71 T3).

## Theorem T3 — the simplest member: both signs, on a surface

*Statement.* (a) If `φ > 0` is at rest on a closed lattice: `Σ_zm_z = (2/γ)Σ_bonds(φ_x − φ_y)²/(φ_xφ_y) > 0`; `Σ_zm_zw_z = −F < 0`; the ledger's total is zero; bodies of both signs are present. (b) Conversely, every positive `φ` is at rest for the bare energies `m_z = (2/γ)(Δφ)_z/φ_z`. (c) Two bodies `m_A`, `m_B` at separation `d` are at rest with positive rates iff `m_A > 0 > m_B` (or the reverse) and `1/|m_B| − 1/m_A = γ(G_0 − G_d)`; then `φ = c − p(G_A − G_B)`, `p = (γ/2)m_Aφ_A > 0`, `φ_A = c/(1 + (γ/2)m_A(G_0 − G_d))`, and the clock at the negative body is the faster.

*Proof.* (a) Divide the law by `φ_z` and sum: `(γ/2)Σm_z = Σ(Δφ)_z/φ_z`; T1. Multiply the law by `φ_z` and sum: `Σm_zφ_z² = (2/γ)ΣφΔφ = −(2/γ)Σ_bonds(dφ)² = −F`. A sum that is positive with weights `1` and negative with weights `w_z > 0` has terms of both signs. (b) Definition. (c) The right side of `−Δφ = −p_Aδ_A − p_Bδ_B`, `p_i = (γ/2)m_iφ_i`, must sum to zero: `φ = c − p(G_A − G_B)`. Then `p(1 + (γ/2)m_Ah) = (γ/2)m_Ac` and `−p(1 + (γ/2)m_Bh) = (γ/2)m_Bc` with `h = G_0 − G_d`; for `c ≠ 0` their ratio gives `m_A + m_B = −γhm_Am_B`, which needs opposite signs and is the stated condition; `c = 0` gives `φ_A = −φ_B`. `G_A − G_B` is largest at `A`, so `φ ≥ φ_A > 0`. ∎

The condition ties the scale of the bodies to their separation: at each separation a one-parameter family of pairs is at rest. Whether such a configuration is stable is not examined.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block75_closed_lattice.py`. **W1** (curvature member, `6×6×6` torus, three bodies, four choices of `μ` with mixed signs; least squares over positive `χ`, `N` with the rates' residual taken per unit rate and the mean of `χ` held at `c`): the smallest residual norms from six random starts are `0.031–0.129` at `c = 1`, `0.002–0.031` at `c = 2`, `0.001–0.016` at `c = 4`; at every best point the sum of the residuals per unit field equals the two sums of squares to four digits. The residual falls only as every length is inflated, which makes the bodies negligible; it is not attained. **W2** (simplest member, same torus, `γ = ½`): the lowest eigenvalue of `−Δ + (γ/2)tM` for the pair `(3, −2)` rises from zero, turns, and vanishes again at `t* = 1.529829` — the closed form gives `1.529829` — with a lowest mode positive at every site and rates `0.64` and `1.44` at the bodies; for three bodies `(3, −1, −3/2)` at `t* = 0.802959`, rates `0.78, 1.09, 1.15`. **W3**: on tori of side 4, 6, 8 and two separations the numerical `m_B` and the closed form agree to six digits (`−2.407524`, `−2.295278`, `−2.402224`, `−2.273643`, `−2.400938`, `−2.267981`).

## No-Go Discipline Gate

The note's negative sentence: no closed lattice is at rest in the curvature member with bodies at rest of any signs.

### N1 — Routes by which the sentence could fail or mislead
1. *Content that moves.* A body's hop energy enters the two field equations differently (a relation in the campaign's probes queue, not in any note, has `e` in the lengths' equation and `e + 2τ` in the rates'); the two uses of T1 then no longer cancel exactly. Outside this note.
2. *Fields that move.* Block 60 T5: a closed lattice in uniform motion exists for a suitable kinetic sign. Outside.
3. *Rates or lengths that change sign.* Excluded by the supplied objects (rates and lengths are positive).
4. *Walls.* With held walls rest exists; the sentence is about closed lattices.
5. *The first control.* The supervisor's first search minimised a residual that is homogeneous in `N` and drove `N` to zero — a meaningless "solution"; see the Review record.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Bodies at rest with `e = mw`; a finite connected closed lattice (T1 holds on any such graph); the two supplied members only.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; silence on rates | yes (premise) |
| block 56 (open PR #8573) | the simplest member's law and field energy | yes (restated) |
| block 60 (open PR #8590) | the curvature member's equations; the ledger's total on a closed lattice | yes (restated) |
| block 71 (open PR #8603) | bodies of negative bare energy | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the identity; never in the curvature member; both signs and a surface in the simplest member" | executed: the identity on the 192 bonds of a `4×4×4` torus | executed: the simplest member's law for the tuned pair at all 64 sites, rates positive; the curvature member's residuals at all 64 sites for arbitrary positive fields | executed: the determinant of the simplest member's operator at the tuned and a detuned negative body | executed: the ledger's total for the pair (zero); the two sums for an arbitrary positive field | every positive function, every closed lattice; every number, place and sign of bodies at rest; content or fields that move outside |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A torus is a device, not a universe." Reply: the note says nothing about what the arena is; it answers the question block 60 T1 and block 71 left together on the table, for the closed lattices the campaign's runners use throughout. Second objection: "Rest on a tuned surface is of no interest." Reply: it is the simplest member's exact analogue of block 60's statement and shows the two members parting ways: in one, negative bodies make rest possible; in the other nothing does. That is information for the owner's fork on which amplitudes are present, not an argument for either answer.

### N8 — Cross-cycle echo
Block 55: with every rate varied the ledger vanishes, so the unit of rate is not a variable — for positive content. Block 60: a closed lattice is not at rest. Block 71: negative content exists in the clauses. Here: with it the ledger *can* vanish at rest, in the simplest member and not in the curvature member.

## Falsifiers

- A positive function on a closed lattice violating T1.
- Positive `χ`, `N` on a closed lattice solving both equations of the curvature member with some `μ_z ≠ 0`.
- A pair at rest with positive rates in the simplest member that violates `1/|m_B| − 1/m_A = γ(G_0 − G_d)`.

## Boundaries and non-claims

Bodies at rest only; content or fields that move are outside. No statement about stability, about the arena, or about which amplitudes are present. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom; the memo's silence on rates and amplitude dynamics. Blocks 55, 56, 60, 71 (PRs #8571, #8573, #8590, #8603, open): restated or placed.
- Named standard imports at definition level: summation by parts on a finite graph; linear systems and determinants over the rationals.
- Reference only: Einstein (1917).

## Review record
Supervisor-run block, the twenty-third of the source-link direction and the nineteenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the note must not suggest that a closed lattice is the arena, nor that negative bodies are wanted because they permit rest. A rigour lens: the supervisor first derived three necessary sum rules and the two-body contradiction, then found that one identity closes every case — the note keeps the sum rules as a remark and proves the general statement; the pair's condition was derived by hand, then confirmed exactly (runner C1, C2) and numerically on three tori (W3). **The first control was wrong in kind:** it minimised the raw residual of an equation homogeneous in `N`, the optimiser sent `N` to `2e-5`, and the script printed "0.0000 (never zero)". The theorem was re-derived and the identity evaluated on that point (it held: `0.147 = 0.147`), which located the fault in the control; the residual is now taken per unit rate and the mean length is held, because inflating every length is the other way to make the bodies negligible. This is the error of block 60's first refuting pass over again. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_closed_lattice_at_rest_curvature_member_never_simplest_member_both_signs_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
