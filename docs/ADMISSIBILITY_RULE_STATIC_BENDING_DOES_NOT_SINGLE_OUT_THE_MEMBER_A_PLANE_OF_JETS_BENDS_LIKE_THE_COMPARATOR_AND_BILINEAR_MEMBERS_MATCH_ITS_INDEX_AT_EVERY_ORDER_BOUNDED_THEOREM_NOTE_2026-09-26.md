---
claim_id: admissibility_rule_static_bending_does_not_single_out_the_member_a_plane_of_jets_bends_like_the_comparator_and_bilinear_members_match_its_index_at_every_order_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 60's weight-one static field energies of rates w = e^u and lengths l = e^lam (landed), in their long-wave form F = -K int e^u [A(lam) grad u.grad lam + C(lam)|grad lam|^2 + D(lam)|grad u|^2] (the long-wave reduction is assumed, not derived for the lattice exterior), with block 60 T3's second-order jet A(0) = 1, C(0) = 1/2 (beta = 1), D(0) = 0, around a spherical body with charges L1, U1 (sigma = -U1/L1), and the index n = l/w = chi^3/N of block 110 (landed): (T1) the second-order index coefficient is nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4D1 s - 2s^2 - s - 2)/(1 + s)^2, so at s = 1 the comparator's 7M^2/4 holds exactly on the plane 4A1 - 2C1 - 6D1 = 3 of third-order jets (the curvature member one point of it; constant coefficients give 5/2), and at third order the comparator's value is one further linear condition on the fourth-order jet; (T2) among bilinear members F = -c sum (dX)(dY), with X = w f(l), Y = g(l), the index equals the comparator's at every order iff l f = ((1 + g)/2)^3 (one member for every g; among power laws Y = l^gamma only gamma = 1/2, the curvature member); (T3) the named clauses (weight one, a variational ledger, the ledger's wall term A(0) L1, blindness to coin rotations) leave the third-order jet free. Exact (sympy). A harvest of probe #9202 (Claude Opus 5.5, the supervisor's family) confirmed by an other-family referee (#9294); nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_static_bending_does_not_single_out_the_member_2026_09_26.py
---

# Static bending does not single out the member: a plane of jets bends like the comparator, and bilinear members match its index at every order

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact, at long wavelength with the long-wave reduction assumed; a harvest of probe #9202, confirmed by an other-family referee in #9294; nothing adopted or registered; unaudited)

This note works within blocks 55, 60 and 110 as landed on main (the ledger per tick, the weight-one field energies of rates and lengths with their second-order jet, the curvature member and the index its rays see); it reports which static completions bend rays like the comparator; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 110 found that the walk's rays around a body match the comparator's at every order in the curvature member, when the body's two charges agree. This note asks the converse. Do rays single out the curvature member among the static field energies that block 60 allows?

They do not.
- **T1: the second-order bend fixes a plane, not a point.** The static field energies of weight one differ at third order by a jet `(A₁, C₁, D₁)`. The comparator's second-order bend holds exactly on the plane `4A₁ − 2C₁ − 6D₁ = 3`. The curvature member, `(1, 1/2, 0)`, is one point of it. Each further order of the bend adds one more linear condition, on the next jet.
- **T2: whole families match every order.** Among bilinear members there is one member for every function `g` whose rays are the comparator's at every order, capture included. The curvature member is `g = 2√ℓ − 1`. Others include `g = ℓ` and `g = 1 + log ℓ`. Among power laws the curvature member is the only one.
- **T3: the named clauses leave the jet free.** Weight one, a variational ledger, the ledger's wall term, and blindness to the coin's axes all leave the third-order jet free.

In plain terms: watching how rays bend around a body cannot tell the curvature member from many others. Block 157 found that consistency with relabellings, once the member keeps all its fields, fixes the member's next order to the comparator's. So what singles out the curvature member is consistency, not static bending. The tie between block 157's variables and this note's jets is not made here.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The field energies, the ray model and the comparator are supplied clauses. Nothing is adopted.
- **Block 60** (landed).
  - Rates `w = e^u` have weight one; lengths `ℓ = e^λ` have weight zero; `χ = √ℓ`, `N = wχ`.
  - T3: the part of `F` of second order in `(u − ū, λ)` is `K w̄ [a u·Δλ + (ap − b) λ·Δλ]`, and "there is no term in `u` alone". In the long-wave form below this is the jet `A(0) = a`, `C(0) = ap − b`, `D(0) = 0`.
  - The curvature member is `F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`.
- **Block 55** (landed): a variational field equation keeps the ledger. An on-site term spoils the uniform vacuum.
- **Block 110** (landed): rays see the index `n = χ³/N`. Outside a body the curvature member gives `χ = 1 + a/r`, `N = 1 − p/r`.
- **The family.**
  - The long-wave form is `F = −K ∫ e^u [A(λ) ∇u·∇λ + C(λ) |∇λ|² + D(λ) |∇u|²]`, normalised to `A(0) = 1`, `C(0) = 1/2` (`β = 1`, the curvature member's), `D(0) = 0`.
  - The free data are the jets `(A₁, C₁, D₁)` and `(A₂, C₂, D₂)`.
  - This is the probe's long-wave reduction. It is assumed here, not derived for the lattice exterior.
- **The body.**
  - Outside a spherical body `u ≈ U₁/r` and `λ ≈ L₁/r`, with `σ = −U₁/L₁`. A body at rest at weak field has `σ = 1/β`.
  - The index is `n = ℓ/w = 1 + ν₁/r + ν₂/r² + ν₃/r³ + …`, with `ν₁ = 2M`.
- **The comparator**, named at definition level: the index `(1 + M/2r)³/(1 − M/2r)`, which is the isotropic form of Schwarzschild's exterior, as a comparator.
- **Standard imports, named at definition level.**
  - Series solutions of radial field equations.
  - The ray invariant `ρ = r n(r)` of a spherically symmetric index (Bouguer's) and its turn integral.
  - Exact symbolic algebra.

## Theorem T1 — the second-order bend fixes a plane, not a point

*Statement.*
- (a) With `β = 1`, `ν₂/M² = −2(2A₁ − C₁ + D₁σ² − 4D₁σ − 2σ² − σ − 2)/(1 + σ)²`. At `σ = 1` this is the comparator's `7/4` iff `4A₁ − 2C₁ − 6D₁ = 3`.
  - The curvature member `(1, 1/2, 0)` is on the plane.
  - Constant coefficients, `(0, 0, 0)`, give `5/2`.
- (b) At `σ = 1`, `ν₃/M³` is linear in `(A₂, C₂, D₂)` with slopes `(−1/3, 1/6, 1/2)`. So the comparator's third-order bend is one more linear condition on the fourth-order jet. The curvature member meets it.
- (c) For a body at rest at general `β` (`σ = 1/β`), `ν₂/M² = −(2A₁β² + 2A₁β − 2C₁β² − 4D₁β − 2D₁ − 2β² − 5β − 3)/(β + 1)²`.

*Proof.*
- **The exterior.** The radial field equations are solved order by order in `1/r`. At first order both fields are harmonic, and the charges are free. At orders two and three the equations are linear, with unique solutions (runner C1, C2).
- **The machinery reproduces the curvature member.** For its jets, the solution is its exact exterior, and `ν₂ = 3a² + 3ap + p²` (runner A3).
- **The bend.** Along a ray `ρ = r n(r)` is kept. Expanding `log n` in `1/ρ` gives the turn `2ν₁/b + π(ν₂ + ν₁²/2)/b² + (4ν₁³/3 + 8ν₁ν₂ + 4ν₃)/b³` (runner B1). So matching the bend order by order is matching `ν₂`, then `ν₃`. ∎

## Theorem T2 — whole families match every order

*Statement.* Take bilinear members `F = −c Σ (X_y − X_x)(Y_y − Y_x)`, with site functions `X`, `Y` of `(w, ℓ)`.
- (a) Weight one and `D(0) = 0` force `X = w f(ℓ)` and `Y = g(ℓ)`. The jet forces `f′(1) = 1/2`. Normalise `g(1) = g′(1) = 1`.
- (b) Outside the body `X` and `Y` are exactly harmonic. With `σ = 1`, the index `ℓf(ℓ)/X` equals the comparator's `(1 + M/2r)³/(1 − M/2r)` identically iff `ℓ f(ℓ) = ((1 + g(ℓ))/2)³`. That gives one member for every `g`.
- (c) Power laws `Y = ℓ^γ` (with `X = w√ℓ`) give `ν₂ = (17 − 6γ)M²/8`. This is the comparator's only at `γ = 1/2`, the curvature member.

*Proof.*
- (a) With `X = w^s f` and `Y = w^{1−s} g`, the `|∇u|²` coefficient is `s(1 − s)`, so `s ∈ {0, 1}`. With `s = 1`, `C(0)/A(0) = f′(1)`.
- (b) The field equations are `X ΔY = 0` and `X_λ ΔY + Y_λ ΔX = 0`, so outside the content `X = 1 − p/r` and `Y = 1 + q/r`. At first order `σ = 1` means `p = q/2`. The identity follows (runner D1). Five choices of `g` each give `ν₂ = 7/4` and `ν₃ = 1` by T1's formulas (runner D1).
- (c) Series (runner D2). The comparator's index has its capture minimum `r n = 3√3 M`, so every matched member captures there too. ∎

## Theorem T3 — the named clauses leave the jet free

*Statement.*
- Every member of the family has weight one by construction.
- Every member has a variational field equation, so it keeps the ledger (block 55).
- The ledger's wall term, the far-field flux of `∂L/∂u′`, is `A(0)L₁`, which does not depend on `(A₁, C₁, D₁)`.
- Turning the coin does not act on `(w, ℓ)`.

So none of these clauses picks out the plane, still less the curvature member on it.

*Proof.* The wall term is runner D3. The rest follows from the definitions. ∎

## What this settles and what it does not

- **Settled.** Static bending does not single out the curvature member.
  - At each order in `1/r`, matching the comparator's bend is one linear condition on one jet.
  - Among bilinear members, a function's worth match every order.
  - The static clauses named in blocks 55 and 60 do not select either.
- **With block 157** (pushed, unrefereed). With all fields and both relabellings, the member's first-order cubic completion is unique at leading order and is the comparator's. The static isotropic sector alone is not selective: block 157 T2 found four classes in the scalar sector. So a candidate for the clause that picks out the plane is relabelling consistency with all fields. Showing that it lands on the curvature member's jet `(1, 1/2, 0)` needs the dictionary between block 157's fields, up to field redefinitions, and this note's jets. That dictionary is not made here.
- **Not settled.**
  - The exact lattice exterior (the long-wave reduction is assumed).
  - Clauses beyond the three named.
  - Bodies with `σ ≠ 1`, beyond T1's general formula.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "which clause singles out the curvature member among block 60's weight-one field energies? (the fall-and-rays lane, blocks 94-110; probes task the-completions-that-bend-like-the-comparator)"
source_of_blocker_text: probes task J:derive:the-completions-that-bend-like-the-comparator
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the dictionary between block 157's cubic class and the static jets (does relabelling consistency with all fields land on (1, 1/2, 0)?); the exact lattice exterior"
conditional_surface_status: "long-wave reduction assumed; sigma = 1 for the classification; bilinear members read as F = -c sum (dX)(dY) with site functions of (w, l)"
hypothetical_axiom_status: "the field energies, the ray model and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60: the weight-one family's second-order jet, and the curvature member doubling the bend.
  - Block 110: rays match the comparator's at every order in the curvature member when the charges agree.
  - Block 55: a variational ledger.
- **Probes.**
  - #9202, worker `w-macbookpro9927a-j8782`, Claude Opus 5.5, the supervisor's own model family, found T1–T3. Its checker's exact families are ported here; its floating-point radial integrations are not used.
  - #9294, a Grok worker, another model family, refereed it: "Confirmed partial. With the long-wave reduction assumed, a weight-one completion bends like the comparator at second order exactly on the plane".
- **In the literature.**
  - The ray invariant of a spherically symmetric index (Bouguer).
  - The isotropic form of Schwarzschild's exterior and its bend coefficients (Eddington's expansion).
  - Reference only.
- **New here.** The harvest itself. The observation that relabelling consistency with all fields (block 157) is the candidate selecting clause, while the static and scalar sectors are not selective.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: does static bending single out the curvature member? The obligations are:
- (O1) the machinery reproduces the landed curvature member (A3);
- (O2) the turn (B1);
- (O3) the plane (C1, C2);
- (O4) the bilinear families and the clauses (D1–D3).

The strongest missing step is the dictionary with block 157.

## No-Go Discipline Gate

The note's negative sentences:
- static bending does not single out the curvature member;
- the named clauses leave the third-order jet free.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The plane is an artefact of the series.* Its equations are linear with unique solutions at each order, and the curvature member's exact exterior is reproduced (A3, C1). ATTEMPTED.
2. *Higher orders of the bend select the point.* Each order adds one linear condition on the next jet, so no finite order selects it (C2). Bilinear families match every order (D1). ATTEMPTED.
3. *A named clause selects it.* The wall term is blind to the jet (D3). The other clauses hold by construction. ATTEMPTED.
4. *Power laws are the natural reading.* Then only the curvature member matches (D2). ATTEMPTED.

Scope left open:
- clauses beyond the three named;
- the lattice exterior;
- relabelling consistency with all fields (block 157).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The long-wave reduction is a declared premise.
- "By construction" appears once, for weight one, which defines the family.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 60 (landed) | the family, its jet, the curvature member | yes (quoted and checked, A3) |
| block 110 (landed) | the index | yes (quoted and checked, A3) |
| block 55 (landed) | a variational ledger | yes (restated) |
| probe #9202 and referee #9294 | the result and its confirmation | yes (ported, rerun) |
| block 157 (pushed, unrefereed) | the candidate selecting clause | context only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a plane at second order; bilinear families at every order; the clauses blind" | executed: field equations order by order, general jets | executed: the turn and the comparator's index | executed: the plane, the slopes, general beta | executed: bilinear members, power laws, capture, wall term | not executed: lattice exterior; other clauses |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Bilinear members with arbitrary `g` are contrived."
  - *Reply:* They are the simplest nearest-neighbour energies of weight one, the curvature member's own form.
  - Within power laws the curvature member is unique (T2(c)). That is the precise sense in which rays select it, and it rests on the choice of power laws.

### N8 — Cross-cycle echo
- Block 60: the curvature member doubles the bend.
- Block 110: its rays match the comparator's at every order.
- Block 157: consistency fixes the member's next order.
- This note: static bending alone does not.

## Falsifiers

- A weight-one completion off the plane whose second-order bend is the comparator's at `σ = 1`.
- A bilinear member with `ℓf ≠ ((1 + g)/2)³` whose index is the comparator's at every order.

## Boundaries and non-claims

- Long wavelength, with the long-wave reduction assumed.
- A spherical body, classified at `σ = 1`.
- Bilinear members with site functions of `(w, ℓ)`.
- The three named clauses.
- The tie to block 157 is a candidate, not shown.
- No gravitational claim is made, and nothing is adopted.

## Imports

- `minimal_axioms`. Blocks 55, 60 and 110 (landed), restated and quoted.
- Named standard imports, at definition level:
  - series solutions of radial equations;
  - the ray invariant of a spherical index (Bouguer);
  - the comparator's isotropic exterior index (Schwarzschild; Eddington's expansion), as a comparator;
  - exact symbolic algebra.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9202 (Claude Opus 5.5) found the result.
  - #9294 (a Grok worker, another family) refereed it with its own checker, a confirmed partial with the long-wave reduction assumed.
  - The supervisor ported the probe's exact families into this runner and dropped its floating-point family.
- **Before writing.** The own prior-art check covered memory, open PRs and main. It found blocks 55, 60 and 110 and no earlier harvest.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_static_bending_does_not_single_out_the_member_2026_09_26.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
