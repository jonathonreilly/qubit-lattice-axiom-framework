---
claim_id: admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_flat_links_leave_only_the_lengths_and_the_lengths_connection_adds_the_inversion_odd_curl_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed generator with bond matrix B = Ebar.s (landed) and block 65's coin turns (landed), for SU(2) turns U(x) acting as U(v.s)U^dag = (Rv).s: (T1) a varying turn gives the bond U_x (Ebar.s) U_y^dag, which differs from the rotated frame's by (1/2)[U_x (E_x.s)(U_y^dag - U_x^dag) + (U_x - U_y)(E_y.s)U_y^dag] and has a coin-scalar part that no frame bond has; (T2) with an SU(2) link W_b on each bond and bond matrix (1/2)(E_x.s W + W E_y.s), turning the coin (psi -> U psi, E -> R E, W -> U_x W U_y^dag) is an exact symmetry to all orders; links fixed flat by the frame's rotation part make every bond the stretch bond conjugated by the lifts, so the walker sees only S = sqrt(g); (T3) for every state, frame and link field, frame torque + link response = (1/2) d<psi^dag s_c psi>/dt at every site and axis; (T4, the supervisor's) a link W = exp((i/2) a.s) adds at first order the coin scalar (i/2)(E.a) to the bond, and with a the frame's own connection along the bond the long-wavelength scalar on smooth zero-corner states is (1/4) eps_abc omega_abc = (1/8) eps.C, the comparator's term that block 158 found the lengths-only walker needs. Exact (sympy; rational unit quaternions; generic jets). T1-T3 a harvest of probe #8843 (Claude Opus 5.5, the supervisor's family) confirmed by an other-family referee (#9308); nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_2026_09_26.py
---

# Links on the bonds make turning the coin a symmetry; flat links leave only the lengths, and the lengths' connection adds the inversion-odd curl

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact; T1–T3 a harvest of probe #8843, confirmed by an other-family referee in #9308; T4 the supervisor's, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 62 and 65 as landed on main (the walker's framed coupling and what turning the coin does at first order); it reports links on the bonds that make turning the coin a symmetry to all orders, what flat links and links carrying the lengths' connection give, and the torque balance; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 65 made turning the coin, differently at each site, a symmetry of the walk at first order. Its scope said that beyond first order "a rotation must be carried along each bond", and it did not construct one. This note constructs it, and ties it to block 158.

- **T1: why the frame alone cannot do it.** A varying turn changes each bond by more than a rotated frame. The extra piece has a coin-scalar part, and no frame bond has one.
- **T2: links do it, to all orders.** Put an SU(2) matrix `W` on each bond, in the form `(1/2)(E_x·σ W + W E_y·σ)`. Then turning the coin is an exact symmetry. If the links are fixed flat by the frame's own turning part, the walker sees only the lengths `√g`.
- **T3: the torque balance.** For every state, frame and link field, the frame's torque plus the links' response equals half the rate of change of the coin's spin, at every site. So on a stationary state the frame's torque vanishes exactly when the links' response does.
- **T4: which links block 158 needs** (the supervisor's). Block 158 found that the walker that sees only the lengths misses the member's relabellings at second order, unless it gets one extra coin-scalar term, `(1/8)ε·C`. Links whose angle along each bond is the lengths' own connection supply exactly that term at long wavelength. Flat links do not.

In plain terms: the coin can be turned freely from site to site if each bond carries a small turn of its own. If those bond turns are only the frame's own turning, the walker feels just the lengths, which block 158 showed is not enough at second order. If the bond turns follow how the lengths themselves bend, the walker gets exactly the missing piece.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The frame, the links and the comparator are supplied clauses. Nothing is adopted.
- **Block 62** (landed).
  - The generator is `H[E] = ½Σ_j{E^j·σ, S_j}`: the bond from `x` along `j` carries `ψ_x†(B/(2i))ψ_y + h.c.`, with `B = Ē·σ` and `Ē = (E^j(x) + E^j(y))/2`.
  - Its Premises say that the local rotation of the coin axes "in the comparator is compensated by a connection that this note does not have".
- **Block 65** (landed): turning the coin at first order gives the frame rotation plus the twist hop. "Beyond that a rotation must be carried along each bond", which it leaves unconstructed.
- **Turning the coin:** `U(x) ∈ SU(2)`, with `U(v·σ)U† = (Rv)·σ`.
- **Links:** `W_b ∈ SU(2)` on each bond, with bond matrix `B = (1/2)(E_x·σ W + W E_y·σ)`.
- **Polar decomposition:** `E = R_E S`, with `S = √(EᵀE)` symmetric positive and `Û` a lift of `R_E`.
- **The lengths' connection.** `ω_jab = e^a_k(∂_j E^k_b + Γ^k_jl E^l_b)`, with `Γ` the metric's own connection. Its vector form is `a_{j,c} = ½ε_cab ω_jab`.
- **The inversion-odd curl** `ε·C` and the comparator's two-component operator are as in block 158 (pushed). The comparator is Weyl's and Fock and Ivanenko's operator, named at definition level.
- **Standard imports, named at definition level.**
  - The product rule of the coin's three matrices.
  - Rational unit quaternions (Cayley).
  - Exact symbolic algebra.

## Theorem T1 — why the frame alone cannot do it

*Statement.* A varying turn changes block 62's bond matrix to `U_x (Ē·σ) U_y†`. This differs from the rotated frame's bond `((R_xE_x + R_yE_y)/2)·σ` by

`(1/2)[U_x (E_x·σ)(U_y† − U_x†) + (U_x − U_y)(E_y·σ) U_y†]`.

The transformed bond has a nonzero trace (a coin-scalar part). Every frame bond is traceless, so `U H[E] U†` is not `H[E′]` for any frame `E′`. At first order about the identity frame, the difference is block 65's frame rotation plus the twist `(i/2)(θ_y − θ_x)_j`.

*Proof.* Algebra of the bond matrices, checked exactly with rational SU(2) turns and rational frames (runner B1). ∎

## Theorem T2 — links do it, to all orders

*Statement.*
- (a) `B[R_xE_x, R_yE_y, U_x W U_y†] = U_x B[E_x, E_y, W] U_y†`. So `ψ → Uψ`, `E → RE`, `W → U_x W U_y†` is an exact symmetry. At `W = 1` the bond is block 62's.
- (b) With `E = R_E S` and flat links `W_b = Û_x Û_y†`, every bond equals `Û_x B[S_x, S_y, 1] Û_y†`. So `H[E, W(E)] = Û H[S, 1] Û†`, and the walker sees only `S = √g`. A lift fixes the link only up to a site sign.

*Proof.* Covariance is the product rule. Flatness follows by factoring the lifts (runner C1). ∎

## Theorem T3 — the torque balance

*Statement.* For every state, frame and link field, at every site `x` and axis `c`:

`(frame torque)_c(x) + (link response)_c(x) = ½ d⟨ψ†σ_cψ⟩(x)/dt`.

On a stationary state the frame torque vanishes exactly when the link response does.
- With no links it does not vanish: on the exactly stationary `4³` state of energy `+1`, it is nonzero at 136 of 192 site-axis pairs.
- With flat links fixed by the frame, the total torque vanishes.

*Proof.* Differentiating `⟨H[R(U)E, U W U†]⟩ = ⟨U H U†⟩` at the identity. This is checked exactly on a `3³` torus with random exact data (81 identities, every term nonzero), and on the stationary `4³` state (runner D1, D2). ∎

## Theorem T4 — which links block 158 needs

*Statement.*
- (a) A link `W = 1 + (i/2) a·σ` adds, at first order in `a`, `(i/2)(E·a)𝟙` to the bond matrix, that is, the scalar hop `(1/4)(E·a)(ψ_x†ψ_y + h.c.)`. On smooth states of the zero-corner species this is `½ E^j·a_j` per bond direction.
- (b) Take `a_j` to be the lengths' own connection along the bond, `a_{j,c} = ½ε_cab ω_jab`. Then

  `½ Σ_j E^j·a_j = ¼ ε_abc ω_abc = (1/8) ε·C`,

  checked through second order in the frame's strain, for general and symmetric frames with generic jets.
- (c) So with these links the walker is, at long wavelength, the comparator's operator `H_f + (1/8)ε·C` (block 158 T1). Block 158 T2 showed that this keeps the member's relabellings through order strain times relabelling. Flat links, by T2(b), leave the lengths-only walk, which does not.

*Proof.*
- (a) The product rule: `(1/2)(E·σ(i/2)a·σ + (i/2)a·σ E·σ) = (i/4){E·σ, a·σ} = (i/2)(E·a)𝟙`. The hop `ψ_x†ψ_y + h.c.` has symbol `2 cos k_j`, which is `2` at `k = 0`.
- (b) Runner E1, at a point with generic jets.
- (c) Blocks 158 T1 and T2. ∎

## What this settles and what it does not

- **Settled.**
  - Block 65's first-order symmetry extends to all orders with links on the bonds.
  - The frame alone cannot extend it.
  - Flat links fixed by the frame give the lengths-only walker.
  - The links that follow the lengths' own connection supply, at long wavelength, exactly the term block 158 needs. So a torsion-free rule for the links, which the probe named as missing, is what block 158's consistency asks for.
- **Not settled.**
  - A nearest-neighbour rule on the lattice fixing the links from the lengths (T4 is at long wavelength).
  - The links' own dynamics.
  - What the links do for the other seven species. At corner `A`, the hop `ψ_x†ψ_{x+e_j} + h.c.` has the value `2cos A_j`, so each bond direction is weighted by its own sign.
  - Relabellings in time.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 65: beyond first order a rotation must be carried along each bond (not constructed); block 158: which lattice object supplies (1/8) eps.C?"
source_of_blocker_text: landed block 65; block 158 (pushed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a nearest-neighbour link rule from the lengths on the lattice and its effect on the eight species; link dynamics; an other-family referee of T4"
conditional_surface_status: "T4 at long wavelength on smooth zero-corner states, through second order in the strain"
hypothetical_axiom_status: "the frame, the links and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the framed generator, which has no connection.
  - Block 65: the first-order twist hop, with "a rotation carried along each bond" named but not constructed.
- **Probes.**
  - #8843, worker `w-jonathonsmac4f50-j330f`, Claude Opus 5.5, the supervisor's own model family, found T1–T3 with an exact checker. Its "where the route stops" named "a discrete torsion-free condition" as missing.
  - #9308, a Grok worker, another model family, refereed it with its own checker: "HIT: confirmed - covariant SU(2) links make local coin rotations a symmetry to all orders, flat links leave only the stretch".
- **Block 158** (pushed; the supervisor's; unrefereed): the lengths-only walker needs `(1/8)ε·C` at second order.
- **In the literature.**
  - Variables carried along the bonds to keep a local symmetry on a lattice (Wilson).
  - The spin connection of a frame (Weyl; Fock and Ivanenko).
  - The balance of the local rotation (Belinfante and Rosenfeld).
  - Reference only.
- **New here.**
  - The harvest.
  - T4, which ties the links to block 158: the lengths' connection carried on the bonds supplies exactly the needed term, and flat links do not.

## Exact target and obligation graph

Target: block 65's unconstructed all-orders symmetry, and block 158's lattice object. The obligations are:
- (O1) the premises (A3);
- (O2) the frame alone fails (B1);
- (O3) links and flat links (C1);
- (O4) the torque balance (D1, D2);
- (O5) the connection's scalar (E1).

The strongest missing step is a lattice link rule from the lengths.

## No-Go Discipline Gate

The note's negative sentences:
- no frame alone makes turning the coin a symmetry;
- flat links do not supply block 158's term.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Some frame `E′` absorbs the turn.* The transformed bond has a trace, and frames do not (B1). ATTEMPTED.
2. *Flat links add a scalar after all.* With flat links the walk is unitarily the stretch walk, so any scalar is the twist of a pure turn (C1). ATTEMPTED.
3. *The link scalar is not `(1/8)ε·C`.* It is, through second order with generic jets (E1). ATTEMPTED.

Scope left open:
- links with other rules;
- the lattice rule;
- the species;
- time.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- T4's long-wavelength reading is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 62 (landed) | the framed generator | yes (quoted, A3) |
| block 65 (landed) | the first-order turn; the unconstructed carrier | yes (quoted, A3) |
| probe #8843 and referee #9308 | T1–T3 and their confirmation | yes (ported, rerun) |
| block 158 (pushed, unrefereed) | the needed term | T4(c) only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "links make turning a symmetry; flat links give only the lengths; the torque balance; the connection's scalar is (1/8) eps.C" | executed: bond identities with exact turns | executed: the torque balance at 81 pairs | executed: the stationary 4^3 state | executed: the link's bond term; the connection scalar at a point | not executed: lattice link rule; species; dynamics |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Links are a new field."
  - *Reply:* As a free field, yes: 3 numbers per bond.
  - T4 shows that the links block 158 needs are not free. They are fixed by the lengths, as the lengths' own connection. So at long wavelength the member's lengths supply them.
  - Whether a nearest-neighbour lattice rule does the same is open.

### N8 — Cross-cycle echo
- Block 62: no connection.
- Block 65: first order, with a carrier named.
- Block 158: the lengths-only walker needs `(1/8)ε·C`.
- This note: the carrier, flat versus connection-carrying, and the latter supplies the term.

## Falsifiers

- A frame `E′` with `U H[E] U† = H[E′]` for a varying turn.
- A state, frame and link field violating the torque balance.
- A generic frame at which the connection's scalar differs from `(1/8)ε·C` at second order.

## Boundaries and non-claims

- T4 holds at long wavelength, on smooth states of the zero-corner species, through second order in the strain.
- The lattice link rule, the species and time are not covered.
- T4 is not refereed.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62 and 65 (landed), restated and quoted.
- Named standard imports, at definition level:
  - the product rule of the coin's matrices;
  - rational unit quaternions;
  - exact symbolic algebra;
  - the spin connection of a frame (Weyl; Fock and Ivanenko), as a comparator.

## Review record

- **Who and when.** Supervisor-run harvest block with the supervisor's T4 (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - T1–T3: probe #8843 (Claude Opus 5.5), refereed by #9308 (a Grok worker, another family).
  - T4: the supervisor's.
  - The supervisor ported the probe's exact checks.
- **Before writing.** The own prior-art check covered memory, open PRs, main and the probes. It found blocks 62, 65 and 158, and no harvest of #8843.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_2026_09_26.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
