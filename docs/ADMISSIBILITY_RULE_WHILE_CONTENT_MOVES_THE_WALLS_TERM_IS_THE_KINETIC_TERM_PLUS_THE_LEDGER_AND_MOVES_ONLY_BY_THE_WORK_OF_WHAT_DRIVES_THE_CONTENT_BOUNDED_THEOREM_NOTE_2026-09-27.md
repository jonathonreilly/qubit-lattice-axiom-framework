---
claim_id: admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_and_moves_only_by_the_work_of_what_drives_the_content_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 60 as landed (a finite box with walls held at w = l = 1; a ledger E = <H> + F of weight one in the rates, F the curvature member in bond form; lengths' kinetic terms quadratic in the lengths' rates, of weight -1, block 60's instance sum c_k l^s lamdot^2/w with the comparator's s = 3, c_k = -6K; the rates as multipliers) with content either supplied at rest, <H> = sum w rho(t), or a walker on block 54's walk crossing bonds at sqrt(w_x w_y)/(chi_x chi_y), and assuming (A1) that solutions differentiable in the label exist (proved by block 60 T4 for bodies at rest under the static law): (T1) at every configuration h := K_lambda + E satisfies h - Wt = -sum_interior dL/du, so on solutions h equals the walls' term Wt = 8K x (the flux of chi into the walls), at every label time; (T2) along solutions dh/dt = -dL/dt, the content's explicit label dependence; (T3) for supplied content at rest dWt/dt = sum w rhodot exactly, the work the supply does, and at weak field with the curvature member and c_k = -6K, Wt = sum rho - (rho.g rho + 3 rhodot.g^2 rhodot)/(8K) + O(rho^3), whose first rate is -(1/4K) rhodot.g rho; on the 3^3 interior with K = 1/2 a body carried from the centre to a face raises Wt by 3/952, and one carried from the opposite face onto the centre beside a fixed face body lowers it by 61/2856; (T4) a walker moved by its ledger's own generator with slaved fields keeps the walls' term constant (with the kinetic term, K_lambda + E), while a walker moved by another generator G changes it at i<[G, H_eff]>. A harvest of probe #8757 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9344, Grok). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_2026_09_27.py
---

# While content moves, the walls' term is the kinetic term plus the ledger, and moves only by the work of what drives the content

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 60 as landed, with existence of solutions assumed where block 60 does not prove it; a harvest of probe #8757, confirmed by an other-family referee in #9344; nothing adopted or registered; unaudited)

This note works within block 60 as landed on main (the walled box, the ledger of weight one, the curvature member and the lengths' kinetic term) and asks what the walls' term does while content moves; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 60 (landed) showed that with the walls held, the static ledger of the box equals its walls' term, the flux of `χ` into the walls. This note is a harvest of a probe result that another model family has confirmed. It asks what happens while the content moves.

- **T1: the walls' term at every moment.** On solutions, the lengths' kinetic term plus the ledger equals the walls' term, at every label time.
- **T2: what moves it.** It changes only through the content's explicit dependence on the label.
- **T3: content carried along a path.**
  - The walls' term changes at exactly the rate `Σ w ρ̇`, the work done by whatever carries the content.
  - At weak field, `Wt = Σρ − (ρ·gρ + 3ρ̇·g²ρ̇)/(8K) + O(ρ³)`, so the first change is of first order in the speed.
  - Carrying a body from the centre of a `3³` box to a face raises the walls' term by `3/952` times its energy squared.
- **T4: a walker.**
  - A walker moved by its own ledger's generator, with the fields following it, keeps the walls' term fixed.
  - A walker moved by any other generator changes it at `i⟨[G, H_eff]⟩`.

In plain terms: the flux of the stretching field into the box's walls counts all the energy inside, including the energy of the lengths' motion. It changes only when something outside the rules pushes the content around, and then by exactly the work done. Content that moves under its own rules leaves the count unchanged.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The member, the kinetic term, the content and its motion are supplied clauses. Nothing is adopted.
- **Block 60 (landed on main).** Quoted by the runner (A3).
  - T1(c): with the rates of `W` held and `𝓔` stationary in every other `u_x`, `𝓔 = Σ_{x∈W} ∂𝓔/∂u_x`.
  - The bond form `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`.
  - The kinetic instance `Σ_x c_k ℓ_x^s (dλ_x/dt)²/w_x`, with the comparator's values `s = 3` and `c_k = −6K`.
- **The box.** An interior `I` of `ℤ³`, and walls `W` (the outside sites next to `I`) held at `w = ℓ = 1`. Rates `w = e^u`, lengths `ℓ = e^λ = χ²`, `N = wχ`.
- **Content.**
  - Supplied content at rest: `⟨H⟩ = Σ_x w_x ρ_x(t)`, carried along given paths.
  - Or a walker on block 54's walk restricted to `I`, crossing bonds at `√(w_x w_y)/(χ_x χ_y)`: `⟨H⟩ = ⟨ψ|H_eff|ψ⟩` with `H_eff = AHA` and `A = √w/χ`.
- **The Lagrangian.** `L = K_λ − 𝓔`, where `K_λ` is quadratic in the lengths' rates, of weight `−1` in the rates, holds no rate of change of a rate, and does not involve the walls' rates. A walker adds its own term linear in `ψ̇`.
- **Solutions.** Stationarity in `u_x` (the rates are multipliers) and the lengths' equations for `x ∈ I`; the walker obeys `iψ̇ = H_eff ψ`.
- **Assumption A1.** Solutions differentiable in the label exist. Block 60 T4 proves this for bodies at rest under the static law. For walker content, and with a kinetic term, it is assumed.

## Domain qualifications

- The walls are held at `w = ℓ = 1`, and the content lives in the interior.
- T1–T2 are exact identities; on solutions they need A1. T3's weak-field form is a series to second order in the bare energies.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — the walls' term at every moment

*Statement.* At every configuration, `h := K_λ + 𝓔` satisfies `h − Wt = −Σ_{x∈I} ∂L/∂u_x`, where `Wt = Σ_{x∈W} ∂𝓔/∂u_x = 8K Σ_{x∈W} (Δχ)_x`, which is `8K` times the flux of `χ` into the walls. On solutions, `h = Wt` at every label time. With `K_λ = 0` this is block 60 T1(c).

*Proof.*
- Scale every rate, the walls' included. `𝓔` has weight one and `K_λ` weight `−1`, so `Σ_all ∂L/∂u_x = −K_λ − 𝓔 = −h`.
- `K_λ` does not involve the walls' rates, so the walls contribute `−Wt`. On solutions every interior `∂L/∂u_x` vanishes.
- For the member, `∂F/∂u_x = 8K N_x(Δχ)_x`, with `N = 1` at the walls.
- The runner checks all of this exactly on the `2³` box with its 24 walls, at a rational point with the walls at 1, for rest content and for a two-component walker (B1). ∎

## Theorem T2 — what moves it

*Statement.* Along solutions, `dh/dt = −∂L/∂t = ∂𝓔/∂t` at fixed fields.

*Proof.*
- `K_λ` is quadratic in the lengths' rates, so `h = Σ λ̇ ∂L/∂λ̇ − L`. The walker's term, linear in `ψ̇`, contributes nothing.
- Then `dh/dt = Σ λ̇(d/dt ∂L/∂λ̇ − ∂L/∂λ) − Σ u̇ ∂L/∂u − ∂L/∂t`. This is checked exactly along arbitrary polynomial paths (C1).
- On solutions the brackets vanish. ∎

## Theorem T3 — content carried along a path

*Statement.* For supplied content at rest, `⟨H⟩ = Σ w ρ(t)`:
- **The exact rate.** `dWt/dt = Σ_x w_x ρ̇_x`. By block 54's pull `−m∇w` on a body of bare energy `m`, this is the work done on the supplied motion. It is not zero.
- **Weak field** (curvature member, `c_k = −6K`, `g` the inverse of `−Δ` on the interior with zero walls): `Wt = Σρ − (ρ·gρ + 3ρ̇·g²ρ̇)/(8K) + O(ρ³)`.
  - Its first change is `−(1/4K) ρ̇·gρ`, of first order in the speed.
  - Over a closed cycle the second-order change is zero.
- **On the `3³` interior with `K = 1/2`** (`g_cc = 11/51`, `g_face = 145/714`):
  - a body carried from the centre to a face raises `Wt` by `3/952` times its energy squared;
  - a body carried from the opposite face onto the centre, beside a body fixed on a face, lowers it by `61/2856`.

*Proof.*
- By T1 and T2, `dWt/dt = ∂𝓔/∂t = Σ w ρ̇`.
- At weak field, the first-order fields are `χ₁ = gρ/(8K)` and `w₁ = −2χ₁ + (c_k/K)gχ̈₁`.
- `Wt⁽²⁾ = −ρ·gρ/(8K) + c_k Σ λ̇₁²`, with `λ₁ = 2χ₁`. For `c_k = −6K` this is the stated form.
- Along the smooth step `3t² − 2t³` between the centre and a face, `dWt⁽²⁾/dt = Σ w₁ ρ̇` holds as a polynomial identity in `t` (D1). The values of `g` and both changes are exact (D1).
- The second-order change is a total derivative, so it vanishes over a cycle. ∎

## Theorem T4 — a walker

*Statement* (given A1).
- A walker moved by its ledger's own generator `H_eff`, with the fields following the static law, keeps `𝓔 = Wt` constant.
- With the lengths' kinetic term, `K_λ + 𝓔 = Wt` is constant.
- A walker moved by another generator `G`, with the fields static, changes the walls' term at `i⟨ψ|[G, H_eff]|ψ⟩`. An example is `G = √w H √w` while the ledger crosses bonds with the lengths.

*Proof.* By T2, since the walker's generator carries no explicit label dependence. For a generator `G`, `d⟨ψ|H_eff|ψ⟩/dt = i⟨ψ|[G, H_eff]|ψ⟩`, and the fields' own derivatives vanish by stationarity (E1). ∎

## What this settles and what it does not

- **Settled.** Within block 60's box:
  - the walls' term keeps the full count, the lengths' kinetic term included, at every moment;
  - it changes only by work done on the content from outside the rules;
  - content moving under its own generator keeps it.
- **For the books programme.** This is block 60 T1(c) with motion. Block 55's kept ledger per site is carried here by the flux into the walls.
- **Not settled.**
  - Existence of solutions for walker content and with the kinetic term (A1).
  - The strong-field motion beyond the static law.
- **Not ported.** The probe's 80-digit strong-field check and its floating-point walker run.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 60 T1(c) as landed: the static ledger is the walls' term; what the walls' term does while content moves (probes task the-walls-term-while-content-moves)"
source_of_blocker_text: probes task J:derive:the-walls-term-while-content-moves
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "existence of slaved branches for walker content and with the kinetic term; strong-field motion"
conditional_surface_status: "exact identities in block 60's walled box; on solutions given A1; weak-field series to second order"
hypothetical_axiom_status: "the member, the kinetic term, the content and its motion are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60: the walls' term for static fields, and the kinetic instance.
  - Block 55: the kept ledger per site.
  - Block 54: the walk and the pull `−m∇w`.
- **Probes.**
  - #8757, worker `w-macbookpro90c72-ja303`, Claude Opus 5.5, the supervisor's own model family, found T1–T4.
  - #9344, worker `w-macbookpro90c72-jca56`, `grok-4.6`, another model family, refereed #8757 with its own checker. It confirmed the Green values, both changes, the first-order rate, the ledger on the `2³` box and the walker's rate. It noted that the strong-field root and the slaved walker time step were not rebuilt, and that existence of those branches stays assumed.
- **In the literature.** That a bounded system's energy is a surface term when the rates enter linearly is the formulation of Arnowitt, Deser and Misner, named in block 60. The energy function of a Lagrangian quadratic in velocities, and its conservation when there is no explicit time dependence, are standard. Both are imports at definition level.
- **New here.**
  - The harvest.
  - A new exact runner, including the energy-function identity along arbitrary paths and the smooth step's rate as a polynomial identity.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: the walls' term while content moves. The obligations are:
- (O1) the premises (A3);
- (O2) the identity at every configuration (B1);
- (O3) the energy function (C1);
- (O4) carried content (D1);
- (O5) the walker (E1).

## No-Go Discipline Gate

The note's negative sentence: carried content changes the walls' term; the change is not zero in general.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The kinetic term breaks the walls' identity.* It has weight `−1` and enters `h` exactly (B1). ATTEMPTED.
2. *The change vanishes at first order in the speed.* It is `−(1/4K)ρ̇·gρ`, not zero (D1). ATTEMPTED.

Scope left open: existence of solutions (A1).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- A1 is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 60 (landed) | T1(c), the bond form, the kinetic instance | yes (quoted, A3) |
| blocks 54, 55 (landed) | the walk and pull; the kept ledger | placement |
| probe #8757 and referee #9344 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the walls' term is the kinetic term plus the ledger and moves only by outside work" | executed: the weights under scaling | executed: the walls' term as flux, both contents | executed: the energy function along polynomial paths | executed: the values of `g`, two moves, the smooth step's rate | not executed: existence (A1); strong-field motion |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is only energy conservation."
  - *Reply:* It locates the conserved quantity. It is the flux into the walls, and with lengths in motion it includes the kinetic term, which is negative for `c_k < 0`.
  - It also measures the work of an outside driver, exactly.

### N8 — Cross-cycle echo
- Block 60: the static ledger is the walls' term.
- This note: the same at every moment, with motion.

## Falsifiers

- A configuration of block 60's box with `h − Wt ≠ −Σ_I ∂L/∂u`.
- A smooth supplied motion on the `3³` interior with `dWt⁽²⁾/dt ≠ Σ w₁ρ̇`.

## Boundaries and non-claims

- Block 60's walled box; A1 where block 60 does not prove existence.
- The member, the kinetic term, the content and its motion are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 60 (landed), restated and quoted. Blocks 54 and 55 (landed), placed.
- Named standard imports, at definition level:
  - homogeneity (scaling) identities;
  - the energy function of a Lagrangian quadratic in velocities;
  - the inverse of the lattice Laplacian with zero walls;
  - exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - Probe #8757 (Claude Opus 5.5) was refereed by #9344 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner and did not port the probe's high-precision and floating-point checks.
- **Before writing.** Origin was re-fetched. Block 60 was read as landed. The own prior-art check covered memory (block 60, block 110 T2(e)), the held branches, open PRs and main.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_2026_09_27.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
