---
claim_id: admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_and_a_wall_between_out_of_step_domains_binds_exact_zero_modes_when_odd_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53, 54, 76 and 77 (open PRs #8568, #8570, #8611, #8612; not adopted), with block 17's chessboard-ordered record states (open PR #8151) as the background, and ONE FURTHER SUPPLIED CLAUSE, not adopted: a record at a site adds a coin-scalar energy c to the walker's generator at that site. (T1) A chessboard record background n(x) = (1 + eps(x))/2 gives the walker the generator H + c/2 + (c/2) eps(x): an offset a0 = c/2 (block 77 T1: it moves every level and gaps nothing) and a staggered rest energy m = c/2, the same for all eight species (block 77 T3); the same background enters the rates (block 53) as a uniform part, removed by clause A, plus a chessboard of clocks, which the walk cannot see (block 76 T1): the walker feels a chessboard record background only as a rest mass. (T2) Where two chessboard domains meet out of step along an axis, at each transverse corner k_perp in {0, pi}^2 the walker reduces exactly to sigma_x S_x + m(x) eps on the line; on a ring of 24 with two such walls (m = 3/5) the exact Gaussian-rational nullspace has dimension 4 (two zero modes per wall) when each wall's defect layer - the sites carrying no staggered term - has odd thickness (1 or 3), and dimension 0 when it has even thickness (0 or 2) or when the mass has no sign change: the walls bind exact zero modes iff the defect layer is odd. (T3) With the axioms' scalar hop a (block 77) a wall's four transverse corners sit at a0 + 4a, a0, a0, a0 - 4a with two-dimensional senses +, -, -, +: levels 1:2:1, each of one sense. EXECUTED, NOT CLAIMED: on 16x6x6 and 24x6x6 tori the odd walls carry 16 exact zero modes (2 walls x 4 corners x 2), localised to within one or two sites, and the even walls carry gapped wall states at |E| = 0.281 (thickness 0) and 0.137 (thickness 2); the wall modes' transverse speed is far below the bulk's 1 and grows with m (0.07, 0.26, 0.59 at m = 0.3, 0.6, 1.2). NOT claimed: that the clause holds or that a chessboard background is present; the wall modes' senses (handedness) in two dimensions; anything about a filling of the wall levels; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_walls_bind_zero_modes_2026_09_22.py
---

# A chessboard record background is felt only as a rest mass; a wall between out-of-step domains binds exact zero modes when its defect layer is odd

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements under one further supplied clause; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks, for records that enter the rates, and for one further clause, that a record adds a coin-scalar energy to a walker at its site; it reports what a chessboard record background does to the walker and what happens where two such backgrounds meet out of step; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 77 (open PR #8612) found that a staggered on-site term — one number alternating like a checkerboard over the sites — is a rest energy for the walker, the same for all eight of its kinds. It presented the term as "the form a chessboard background takes" and did not say where such a background could come from. The record layer has one: block 17 (open PR #8151) found chessboard-ordered states of the six-axis static law. This note connects the two layers with one supplied clause and then asks what happens at the boundary between two chessboard regions that are out of step.

1. **The background is felt only as a mass** (T1). If a record adds a coin-scalar energy `c` at its site, a chessboard of records is an offset `c/2` plus a staggered term `c/2`: every kind of walker acquires the rest energy `c/2`. The same records also slow the clocks (block 53) — but a chessboard of clocks is exactly invisible to the walk (block 76). So the record background reaches the walker through the on-site term and nothing else.
2. **Walls bind exact zero modes — when the defect layer is odd** (T2). Two chessboard domains out of step by one site meet along a plane. If the plane's defect layer (sites with no staggered term) is one or three sites thick, the walker has exact zero-energy states bound to the wall, two at each of the four transverse corners; if it is zero or two sites thick, or if there is no sign change, there are none — only gapped wall states. Exact, by Gaussian-rational nullspaces of the corner-reduced operator.
3. **The scalar hop sorts a wall's corners by handedness** (T3). With the axioms' own hop `a`, the four corners of a wall split 1:2:1, each level of one two-dimensional sense — block 77's statement one dimension down.

Executed: on tori the count is 16 zero modes (2 walls × 4 corners × 2), localised within a site or two; the wall modes move sideways much more slowly than bulk walkers (speed 0.07–0.59 for `m` = 0.3–1.2).

In plain terms: if records sit on the lattice in a checkerboard, a walker passing through gains a weight it can rest with — and it feels nothing else of that checkerboard, because the clocks it alternately speeds and slows cancel on every hop. Where two checkerboard regions meet out of step there is a seam; if the seam is an odd number of sites wide, walkers can sit on it at exactly zero energy, and they crawl along it far more slowly than free walkers move. Whether the seam's walkers are one-handed is not decided here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 77 (PR #8612), next_trace_action: 'whether a chessboard record background (block 17's states) supplies the staggered term'; FORK_PROBE_source_link_20260922.md section 1: the chiral tension; the lattice lens's known exit 'a wall'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the record layer can give the walker a mass through one clause; walls of the chessboard order bind exact zero modes with a parity rule; next: the senses of the wall modes at each corner (executed in scratch, not settled); the a-term's 1:2:1 split with a filling (block 78's exclusion applies); what block 17's law says about the width and parity of its domain walls"
conditional_surface_status: "T1 exact for every chessboard background on every even lattice under the clause; T2 exact for the corner-reduced operator on the ring tried (the reduction is exact for backgrounds varying along one axis); T3 symbolic; the tori and the wall speeds are the control's"
hypothetical_axiom_status: "block 54's walk; block 53's rule for records in the rates; block 17's chessboard states as a background; the clause 'a record adds a coin-scalar energy at its site'; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (proper rotations, under which `ε` is invariant about any site), the Record axiom (one record per site), the Qubit axiom ("no possibility is privileged": a coin-scalar term privileges no coin direction), and the memo's silence on how records act on amplitudes. Blocks 17, 53, 54, 76, 77 (open PRs) supply the background, the rates' rule, the walk, the invisibility and the staggered term.

- **Background.** `n(x) = (1 + ε(x))/2`, `ε(x) = (−1)^{x+y+z}`: records on one sublattice (block 17's ordered states; either sublattice is a state, and translation by one site exchanges them).
- **The clause.** `H → H + c Σ_x n(x)P_x`, `P_x` the projector on site `x`, `c` real: supplied here, not derived, not adopted.
- **Walls.** Along `x` the background is `n(x) = (1 + s(x)ε(x))/2` with `s(x) = ±1` on the two domains; the mass profile is `m(x) = (c/2)s(x)` except on the defect layer, where `m = 0`.
- **Corner reduction.** On a torus with even transverse sides, transverse plane waves at `k_⊥ ∈ {0, π}²` have `S_yψ = S_zψ = 0`; for a background varying along `x` only, the walk restricted to such states is `σ_xS_x + m(x)ε` on the line.
- **Kernel dimension.** The nullspace dimension of the `2N × 2N` Gaussian-rational matrix of the line operator, by exact elimination.

Bound states at a sign change of a fermion's mass are the comparator of Jackiw and Rebbi; the surface modes of a mass wall in one extra dimension are those of Callan and Harvey and of Kaplan's domain-wall fermions; named here only.

## Prior art and what is new

New, inside the framework's vocabulary: that block 17's chessboard states, with one clause, are block 77's mass and nothing else to the walker; the exact parity rule for walls between out-of-step domains — zero modes iff the defect layer is odd, with none for even layers and none without a sign change — which the comparator's continuum picture (a zero mode at every sign change) does not contain; and the wall corners' 1:2:1 split by sense under the axioms' scalar hop. No gravitational claim is made.

## Exact target and obligation graph

Target: the record background as the walker's mass, and its walls. Obligations: (O1) the background's action on the walker and on the clocks; (O2) walls; (O3) the scalar hop on walls. T1–T3 discharge them.

## Theorem T1 — the background is felt only as a mass

*Statement.* (a) `c Σ_x n(x)P_x = c/2 + (c/2)ε`. (b) Under the clause, the walker in a chessboard background has the generator `H + c/2 + (c/2)ε`: an offset (block 77 T1) and a staggered rest energy `m = c/2` (block 77 T3), the same for every species; with the axioms' hop `a` the masses are `√(c²/4 + 36a²)` (one pair) and `√(c²/4 + 4a²)` (three pairs) (block 77 T4). (c) Under block 53's rule a record enters the rates as a factor; a chessboard of records gives rates `κ` on one sublattice and `1/κ` on the other (times a uniform factor, removed by clause A), whose bond products are all equal: the clocked walk is the free walk (block 76 T1).

*Proof.* (a) `n = (1 + ε)/2`. (b) Block 77. (c) `κ · (1/κ) = 1` on every bond; block 76 T1(b). ∎

## Theorem T2 — walls bind exact zero modes when the defect layer is odd

*Statement.* Let the background vary along `x` only, with `m(x) = m₀ > 0` on one domain, `−m₀` on the other, and `m = 0` on the defect layers of thickness `z` at the two walls of a ring of 24. At each transverse corner the walker is `σ_xS_x + m(x)ε` on the line, and the kernel of that operator has dimension 4 for `z = 1, 3` and 0 for `z = 0, 2`; with `m = +m₀` on both domains and isolated zero sites it has dimension 0.

*Proof.* The reduction: at `k_⊥ ∈ {0, π}²`, `sin k_y = sin k_z = 0`. The dimensions: exact Gaussian-rational elimination (runner C1) on the `48 × 48` matrix for each profile. ∎

The rule is a parity rule of the lattice: across a wall the two domains are the same chessboard shifted by one site; with an even defect layer the staggered signs on the two sides are in step and the mass never passes through zero in the sense the zero mode needs, with an odd layer they are out of step around a site where the term vanishes. The comparator's continuum argument gives a bound state at every sign change; the lattice does not.

## Theorem T3 — the scalar hop on a wall

*Statement.* At a wall the transverse corners `(0,0), (π,0), (0,π), (π,π)` carry the scalar hop's values `a₀ + 4a, a₀, a₀, a₀ − 4a`, and their two-dimensional senses (the sign of `cos k_y cos k_z`) are `+, −, −, +`: three levels 1:2:1, each of one sense.

*Proof.* `2a(cos k_y + cos k_z)` at the corners. ∎

Whether the wall's zero modes at a given corner form a two-dimensional cone of a definite handedness — and whether the handedness matches the corner's sense — is not decided here (Boundaries).

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block79_walls.py`. **W1** (`16 × 6 × 6` torus, `m₀ = 0.6`, walls at `x = 4, 12`): thickness `z = 0`: no zero modes, wall states at `|E| = 0.281`; `z = 1`: 16 exact zero modes, weight within one site of a wall `≥ 0.83`; `z = 2`: none, wall states at `0.137`; `z = 3`: 16, weight within two sites `≥ 0.84`. **W2** (transverse dispersion by the plane-wave reduction along `y, z`, ring of 48 along `x`): the wall modes' `|E|` at transverse momentum `q` gives speeds `0.07, 0.05, 0.03` (`m₀ = 0.3`), `0.26, 0.26, 0.23` (`0.6`), `0.59, 0.59, 0.57` (`1.2`) for `q = 0.05, 0.1, 0.2` — far below the bulk's 1, rising with `m₀`. **W3** (`24 × 6 × 6`): 16 zero modes; their transverse-momentum content is equally shared by the four corners (four per corner).

## No-Go Discipline Gate

The note's negative sentences: an even defect layer binds no zero mode; a defect without a sign change binds none; the walker feels a chessboard record background only through the on-site term.

### N1 — Routes by which the sentences could fail or mislead
1. *Other clauses.* A record could act on the walker through a coin-vector term (privileging a coin direction — excluded by the Qubit axiom's sentence), through bond rates (block 59: then the background's chessboard is not invisible), or through the lengths. Only the coin-scalar site term is examined.
2. *Other walls.* Walls not along an axis, or curved, are outside; the corner reduction needs a background varying along one axis.
3. *Thickness beyond 3.* The parity rule is checked for `z = 0–3` (and `z = 4` in scratch: none); the pattern is read off, not proved for all `z`.
4. *Filling.* Whether the zero modes are occupied is a many-record question (block 78's exclusion applies); nothing here says they are.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even lattices (the chessboard is periodic); the identity frame; uniform rates apart from the background's own; the background's clause.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice's proper rotations; the Record and Qubit axioms | yes (premise) |
| block 17 (open PR #8151) | the chessboard-ordered record states | yes (the background) |
| block 53 (open PR #8568) | records enter the rates as factors | yes (T1(c)) |
| blocks 76, 77 (open PRs #8611, #8612) | chessboard clocks invisible; the staggered term's algebra and masses | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "felt only as a mass; zero modes iff the defect layer is odd; corners 1:2:1 by sense" | executed: the background's bond products on all 192 bonds; the corner values | executed: the generator with the background against `a₀ + mε` at all 64 sites; the clocked walk against the free walk at all sites | executed: exact nullspace dimensions for five profiles on a ring of 24; control: dispersions and counts on tori | executed: the corners' split and senses | T1 every even lattice; T2 the profiles tried (parity read off); T3 symbolic; the clause and the background not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Domain-wall zero modes are textbook." Reply: the comparator's rule is "a zero mode at every sign change"; the lattice's rule here is a parity rule with none at half the walls, and the connection to a background the record layer already has is the framework's own. Second objection: "You have not shown the wall modes are chiral, which is the whole point." Reply: correct, and the note says so; T3 shows only that the scalar hop sorts the corners by sense, which makes the question well-posed.

### N8 — Cross-cycle echo
Block 17: chessboard order in the record layer. Block 77: a chessboard number is a rest mass. Block 76: a chessboard of clocks is invisible. Here the three meet: records in a checkerboard weigh the walker down and do nothing else to it, and their seams hold walkers at zero energy.

## Falsifiers

- A chessboard background under the clause whose generator differs from `H + c/2 + (c/2)ε` at some site.
- A wall with an odd defect layer (thickness 1 or 3) and no zero mode, or an even one (0 or 2) with a zero mode, on the corner-reduced ring.
- A corner whose scalar-hop value or sense differs from T3.

## Boundaries and non-claims

The clause and the background are supplied, not derived. The wall modes' handedness, their filling, and walls not along an axis are outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice, Record and Qubit axioms; the memo's silence on how records act on amplitudes. Blocks 17, 53, 54, 76, 77 (PRs #8151, #8568, #8570, #8611, #8612, open): restated or placed.
- Named standard imports at definition level: Gaussian-rational elimination; the plane-wave reduction along the transverse axes for backgrounds varying along one axis (Bloch).
- Reference only: Jackiw and Rebbi; Callan and Harvey; Kaplan.

## Review record
Supervisor-run block, the twenty-seventh of the source-link direction; the fourth after the fork probe. Lens pass, in writing, by the supervisor: a foundations lens — the clause is one sentence and is named as supplied; the Qubit axiom's "no possibility is privileged" is what limits a record's action to a coin scalar; a rigour lens — the first scratch used sharp walls and found no zero modes, the second used smooth walls and found exact ones, and the difference was tracked down to the parity of the defect layer, which became the theorem; the transverse speed of the wall modes was measured before any statement about "cones" was made, and the note makes none; the wall modes' handedness was attempted in scratch (velocity matrices in the coin's frame) and not settled — left open. A strategy lens — this is the first place in the direction where the record layer and the amplitude layer touch through a mechanism (mass) rather than a source term, and the first place a one-handed content is even well-posed. Control: as reported under Executed. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_chessboard_record_background_is_felt_only_as_a_rest_mass_walls_bind_zero_modes_2026_09_22.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
