---
claim_id: admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN the member at alpha = K/4, beta = -alpha with the bond shift, in its landed long-wave quadratic form S2 (blocks 62, 101, 124, 136 and 144 as landed), at leading order in the spacing: the first-order problem delta0 V3 + delta1 S2 = 0 over local cubic vertices V3 with two derivatives (T-even, at most one time derivative per field, rotation-invariant) and local one-derivative deformations delta1, counted modulo local field redefinitions. Exact over Q: (T1) with all fields and both relabellings (in space, and in time for every clock profile) there is exactly one class, the comparator's (the third-order part of N sqrt(gamma)(K_ij K^ij - K^2 + R)); (T2) restricted to the scalar sector there are four, so the scalar-sector test pre-registered for this question is not selective; (T3) with all fields and relabellings in time required only for spatially uniform clock profiles there is still exactly one class, the comparator's (also for cubic-symmetric vertices at general momenta, by a separate run), while with no relabellings in time there are five (scalar sector: five and eight). So at leading order the comparator's cubic vertex is forced once the transverse fields and at least the uniform relabellings in time are kept. The exact lattice lift at range 1-2 and the tie to the walker's coupling are not examined. A harvest of probe #9283 (Claude Opus 5.5, the supervisor's own model family; unrefereed) for T1-T2, with the supervisor's variants for T3 run on the probe's machinery. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_2026_09_26.py
---

# At leading order the member's cubic completion is unique and is the comparator's, with all fields, even with only uniform relabellings in time

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact over the rationals, at leading order in the spacing, within the landed member; T1–T2 a harvest of probe #9283, T3 the supervisor's variants on its machinery; not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 62, 101, 124, 136 and 144 as landed on main (the member, its lapse and shift, its two relabellings and its quadratic action at the closing values); it reports the member's first-order cubic completion at leading order in the spacing; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Programme A's step A1 (decision-record addendum 40) asks which cubic terms the member can have. The member's quadratic action and its two relabellings are landed. The first-order consistency condition `δ₀V₃ + δ₁S₂ = 0` then decides which cubic vertices can extend it. Probe #9283 solved that condition exactly at leading order in the spacing. This note adds the dependence on the reading of relabellings in time.

- **T1: one class with all fields.** With all fields and both relabellings, exactly one class of cubic completions exists, modulo field redefinitions: the comparator's.
- **T2: the scalar sector is not selective.** Restricted to the scalar sector there are four classes. The test pre-registered in addendum 40 was posed on that sector, so it could not have singled out the comparator.
- **T3: uniform relabellings in time suffice.** With all fields, requiring relabellings in time only for spatially uniform clock profiles still leaves one class, the comparator's. Dropping relabellings in time altogether leaves five.

In plain terms: once the member keeps its sideways fields and at least the freedom to reset one clock for the whole lattice, there is only one way to add its next order at long wavelength, and it is the comparator's. Addendum 44 found that the same reading, only uniform clock resets, is the one that keeps free walkers exactly consistent. So that reading keeps the walkers consistent and fixes the member's next order as well.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The member, its relabellings and the comparator are supplied clauses. Nothing is adopted.
- **The member** (blocks 62, 101, 124, 136 and 144 as landed), at `α = K/4`, `β = −α`, with the bond shift, `K = w̄ = 1`: `S₂ = ∫ ¼[tr(Ḣ²) − (tr Ḣ)²] + nR₁ + R₂`, with `Ḣ = ḣ − ∂N − ∂Nᵀ` and block 62's `R₁`, `R₂`.
- **Its relabellings.** In space, `δh = ∂ξ + ∂ξᵀ`, `δN = ξ̇`. In time, `δn = ξ̇⁰`, `δN = −∇ξ⁰`.
- **The problem at leading order.** Local cubic vertices `V₃` with two derivatives, T-even, at most one time derivative per field, rotation-invariant; local one-derivative deformations `δ₁`; classes modulo local field redefinitions. At long wavelength every difference has symbol `p_j → k_j`, so the leading symbols of any lattice solution solve this problem.
- **The readings of relabellings in time** (addenda 39 and 44; block 150 T1).
  - Every clock profile: `ξ⁰` arbitrary.
  - Only uniform profiles: the time part of the condition is required at zero spatial momentum.
  - None: only spatial relabellings are required.
- **The comparator**, named at definition level: the third-order part of `N√γ(K_ijK^ij − K² + R)`, whose quadratic part equals `S₂` (block 144 T1).
- **Standard imports, named at definition level.** Exact linear algebra over the rationals (domain matrices, reduced row echelon form, null spaces); formal plane-wave symbols, with integration by parts as momentum conservation; the known uniqueness of the comparator's cubic vertex among consistent completions of the massless symmetric tensor theory (a comparator only; T1 reproduces it without using it).

## Theorem T1 — one class with all fields

*Statement.* With all fields and both relabellings, the consistent vertices modulo local field redefinitions form exactly one class, and the comparator's cubic vertex represents it. No class is strictly gauge invariant.

*Proof.* The identity is graded by the number of derivatives. So only one-derivative deformations meet two-derivative vertices, and redefinitions change `V₃` by `E·F` with `F` of zero derivatives. Hence the classes are the consistent space modulo the span of `E·F`. With rotation invariance, 1122 vertex monomials reduce to 87 independent symbols. The consistent space has dimension 18, and redefinitions span 17 of it, all consistent. The comparator's vertex is consistent and not a redefinition (runner C1). The scalar-sector vertices `V_n` and `V_h` of T2 are not consistent here (C2). The probe's run with cubic-symmetric vertices at general momenta also gives one class. ∎

## Theorem T2 — the scalar sector is not selective

*Statement.* Restricted to the scalar sector (`n`, `N = ∇B`, `h = 2ψδ + 2∂∂E`; parameters `ξ⁰`, `ξ = ∇χ`), there are four classes. The comparator's is one. `V_n = n|∂_ih_ij − ∂_jtr h|²` and an eight-term static lengths-only cubic `V_h` are two others.

*Proof.* There are 67 independent symbols, a consistent space of dimension 21, and 17 redefinitions (runner B1). `V_n` and `V_h` are consistent and nontrivial, and independent of the comparator's class (B2). On scalar configurations `∂_ih_ij − ∂_jtr h = −4∂_jψ`, which is invariant under longitudinal relabellings only. The probe's cubic-symmetric run again gives four. ∎

## Theorem T3 — uniform relabellings in time suffice

*Statement.* With all fields:
- if relabellings in time are required only for spatially uniform clock profiles, there is exactly one class, the comparator's;
- with no relabellings in time there are five, the comparator's among them.

In the scalar sector the counts are five and eight.

*Proof.* The same machinery, with the time part of the condition either imposed at zero spatial momentum of the parameter or dropped, together with the time-type deformations (runner D1–D3). A separate run with cubic-symmetric vertices at general momenta and uniform relabellings in time gives 183 independent symbols, a consistent space of 27 and 26 redefinitions: one class, the comparator's (154 s; not in the runner, whose time budget it would exceed). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision-record addendum 40, programme A1: all local cubic vertices and first-order deformations of the member's gauge symmetry; is the continuum part one-dimensional and equal to the comparator's?"
source_of_blocker_text: decision-record addendum 40 (pre-registered)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the exact lattice lift at range 1-2 of the comparator's class, or the order in the spacing at which it fails; the tie to the walker's coupling; an other-family referee"
conditional_surface_status: "leading order in the spacing; rotation-invariant vertices in the runner (cubic-symmetric in the probe's runs)"
hypothetical_axiom_status: "the member, its relabellings and the comparator are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 62 (the member's fields and `R₁`, `R₂`), block 101 (the rate as a multiplier), block 124 (relabellings in time), block 136 (the bond shift), block 144 T1 (the quadratic action as the comparator's quadratic part). Block 150 T1 (landed) ties the readings of relabellings in time to the momentum constraint.
- **Probes.** #9283 (Claude Opus 5.5 worker `w-jonathonsmac4f50-j542d`, the supervisor's own model family; unrefereed) found T1 and T2, with its exact checker (22 checks without its longest run, rerun here in 688 s, all passing). The supervisor ported its machinery into this runner and ran the variants of T3.
- **In the literature.** The uniqueness of the cubic vertex of the massless symmetric tensor theory (Gupta, Kraichnan, Feynman, Deser, Boulware; Wald), which T1 reproduces. Reference only.
- **New here:** T3, the dependence on the reading of relabellings in time; the observation that the pre-registered scalar-sector test is not selective.
- **Provenance.** Same-family results. No other model family has refereed them.

## Exact target and obligation graph

Target: addendum 40's A1 at leading order. The obligations are:
- (O1) the member's invariance and its identity with the comparator's quadratic part (runner A3);
- (O2) the scalar sector (T2: B1, B2);
- (O3) all fields (T1: C1, C2);
- (O4) the readings (T3: D1–D3).

The strongest missing step: the exact lattice lift.

## No-Go Discipline Gate

The note's negative sentences: with all fields no class other than the comparator's exists at leading order; the scalar-sector test cannot single out the comparator.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Other consistent vertices exist with all fields.* The consistent space is the redefinitions plus one class (T1; runner C1). ATTEMPTED.
2. *The scalar-sector classes survive with all fields.* `V_n` and `V_h` are not consistent there (T1; runner C2). ATTEMPTED.
3. *Uniqueness needs every clock profile to be a relabelling.* Uniform profiles suffice (T3; runner D1). ATTEMPTED.
4. *Uniqueness needs no relabelling in time at all.* Without them there are five classes (T3; runner D2). ATTEMPTED.
5. *Anisotropic vertices add classes.* The probe's cubic-symmetric runs give the same counts (reported, not rerun here). ATTEMPTED.

Scope left open: the exact lattice lift; the tie to the walker's coupling; higher orders.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical". The locality class and the readings are stated under Premises. No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 62, 101, 124, 136, 144 (landed) | the member, its relabellings, its quadratic action | yes (re-checked: runner A3) |
| block 150 T1 (landed) | the readings of relabellings in time | context |
| probe #9283 (unrefereed, same family) | the machinery and T1–T2 | yes (rerun and ported) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "one class, the comparator's, with all fields, even with only uniform relabellings in time" | executed: invariance of `S₂` for every field component | executed: the vertex and deformation enumerations | executed: the consistent space and the quotient over Q | executed: the two readings, all fields and scalar sector | leading order; rotation-invariant in the runner |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This only reproduces a known uniqueness theorem."
  - *Reply:* T1 does, and that validates the machinery. The new points are these. The scalar-sector test pre-registered for this lane cannot decide the question (T2). The uniqueness survives the weaker reading of relabellings in time, the one under which free walkers are exactly consistent (T3).

### N8 — Cross-cycle echo
- Block 144: the quadratic action is the comparator's.
- Block 150 T1: the readings of relabellings in time.
- This note: at leading order the cubic completion is the comparator's under either reading that keeps the uniform relabellings.

## Falsifiers

- A consistent cubic vertex with all fields, not a redefinition and not the comparator's.
- A rank computation in the runner that differs on recomputation.

## Boundaries and non-claims

- Leading order in the spacing; two-derivative vertices; rotation-invariant vertices in the runner.
- The lattice lift, higher orders and the walker's coupling are not covered.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 101, 124, 136, 144 and 150 (landed), restated.
- Named standard imports, at definition level: exact linear algebra over the rationals; plane-wave symbols; the known uniqueness of the comparator's cubic vertex (Deser; Boulware; Wald), as a comparator.

## Review record

- **Who and when.** Supervisor-run harvest block, 2026-09-26, during the owner's 12-hour campaign of that day.
- **Provenance.** T1 and T2 are probe #9283's (Claude Opus 5.5, the supervisor's own model family). The supervisor read its checker, reran it (688 s, 22/22), ported its machinery, and ran T3's variants. No other model family has refereed it.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found addendum 40's pre-registration and no other attempt at A1.
- **Independence.** Mutation census: at least one mutation per science family (A, B, C, D), each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_2026_09_26.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
