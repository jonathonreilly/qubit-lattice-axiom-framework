---
claim_id: admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_under_either_reading_and_a_point_equivalent_source_has_an_exact_local_price_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 116's held-wall law as landed (a held cube of odd side with the wall held at phi = 1, g = (1 - A)^-1 inside with zero wall values, k = gamma/12, the static law ((1 - A) + kK) psi = k e with phi = 1 - psi, e = K1 for K_xy = Re chi_x^dag H_xy chi_y), its two readings (amplitude sourcing; records only) and its ledger-keeping price E' = Lambda/(1 - k Lambda g_yy) for one record forming at rest at y; a rule of radius R is any function of the amplitude and the pre-event rates within coordinate distance R of y: (T1) the ledger is the total effective source, Lambda = sum K phi = Q, E' = Q/phi'_y, and the post-event field is k Q g(., y); (T2) records only: the response at the record's site grows strictly with the box, so one amplitude placed in two boxes has identical window data and different prices, for every R; (T3) amplitude sourcing: a charged cage of total charge 1 on the two layers just outside the window, field zero inside, added as bodies at rest, leaves every window datum unchanged and shifts the ledger by its charge, for every R; (T4) when the effective source is point-equivalent (s - Q delta_y = (1 - A)f with f finitely supported, then computable in the window), E' = Q/(phi_y + k f_y) exactly in every held box; block 116's star is such a source and the distance-two cross is not. Exact (rational arithmetic, sympy). A harvest of probe #9175 (Claude Opus 5.5, the supervisor's family) confirmed by an other-family referee (#9311); nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_2026_09_26.py
---

# No local rule of any fixed radius sets the price of forming a record, under either reading, and a point-equivalent source has an exact local price

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 116's held-wall law; a harvest of probe #9175, confirmed by an other-family referee in #9311; nothing adopted or registered; unaudited)

This note works within block 116 as landed on main (the held-wall law, the two readings and the price that keeps the ledger when one record forms); it reports whether that price can be set from data near the record; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 116 found that forming one record keeps the ledger only at a price: the record's bare energy must be `E' = Λ/(1 − kΛ g_yy)`. This note asks whether a record could "know" that price from what is near it.

- **T1: the ledger is the total effective source.** `Λ = Σ Kφ = Q`. The price is `E' = Q/φ'_y`, and after the event the field is `kQ` times the unit response at `y`.
- **T2: records only, no local rule.** Before the event the rates are all `1`, so nothing near the record tells how far the walls are. The response at the record's site grows with the box. So the same amplitude in two boxes looks identical near `y` and has different prices, whatever the radius.
- **T3: amplitude sourcing, no local rule either.** A charged shell of total charge 1, sitting just outside the window, has no field inside. Adding it changes nothing near the record, yet it moves the ledger, and so the price, by its charge.
- **T4: an exact local price when the source is point-like.** If the effective source differs from a point charge by a finitely supported difference of the form `(1 − A)f`, the price is exactly `Q/(φ_y + k f_y)` in every box, and `f` is read from the window. Block 116's six-arm star is such a source, which is why its price ignored the walls. The distance-two cross is not.

In plain terms: the energy a record must take on so that the books still balance depends on the whole lattice, walls included, not only on what is near the record. This holds whether or not unrecorded amplitudes source the field. The exception is a source that looks like a single charge from outside. So the formation price is one of the things records alone, looking locally, cannot fix.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The held-wall law and the readings are supplied clauses. Nothing is adopted.
- **Block 116** (landed).
  - A held cube of odd side `n` whose boundary layer is the wall, where `φ = 1`. "`g = (1 − A)⁻¹` inside, with zero wall values", with `A` the six-neighbour average and `k = γ/12`.
  - An amplitude `χ` with Hermitian `H` gives `K_xy = Re χ_x†H_xyχ_y` and `e = K1`.
  - *Amplitude sourcing*: `((1 − A) + kK)ψ = k e`, with `φ = 1 − ψ`. *Records only*: "only records enter, and an unrecorded amplitude sources nothing."
  - A record at rest at `y`, with bare energy `E'`, "has ledger `E'/(1 + kE' g_yy)`". It keeps `Λ = Σ eφ` iff `E' = Λ/(1 − kΛ g_yy)`.
  - The star's price is "`E' = c/(1 − kc)`, with `c = m₀/(1 + km₀) + 6m₁`".
- **A rule of radius `R`.** Any function of the data within coordinate distance `R` of `y` (the largest coordinate difference), meaning the amplitude there and the pre-event rates there. The window is `B_R(y)`.
- **Standard imports, named at definition level.**
  - The discrete maximum principle.
  - Summation by parts.
  - Positive definiteness from an eigenvalue bound.
  - Exact rational linear algebra.

## Theorem T1 — the ledger is the total effective source

*Statement.*
- `Λ = Σ_x e_xφ_x = Σ_x (Kφ)_x = Q`, the total of the effective source `s = Kφ`.
- The static law is `ψ = k G s`, with `G` the held response.
- A record of bare energy `E'` at `y` has effective source `E'φ'_y δ_y`, so keeping the ledger means `E'φ'_y = Q`. Then `E' = Q/φ'_y`, and the post-event field is `kQ g(·, y)`.

*Proof.* `K` is symmetric, so `(K1)ᵀφ = 1ᵀKφ`. The rest follows from the law. It is checked in the side-7 cube with a uniform `3×3×3` of rest energies `1/27`: the four symmetry classes have four distinct prices, increasing towards the centre; each satisfies `E'φ'_y = Λ`; and each post-event field solves the law exactly. The uniform star costs `1188/1091` in the cubes of side 7 and 9 (runner B1). ∎

## Theorem T2 — records only: no local rule

*Statement.* Under records only, for every `R` there are two held boxes and one amplitude, supported in `B_R(y)`, whose data within radius `R` agree and whose prices differ.

*Proof.*
- Before the event `φ ≡ 1`, so the window data are the amplitude alone.
- `E' = E/(1 − kE g_yy)` increases strictly with `g_yy` while `0 < kE g_yy < 1`.
- For held cubes `Ω ⊂ Ω′` containing `y`, `g_{Ω′}(·, y) − g_Ω(·, y)` is harmonic inside `Ω`, positive on `Ω`'s wall, and so positive inside by the maximum principle.
- Centring the amplitude in the cubes of sides `n` and `n + 2`, with `n ≥ 2R + 3`, gives the pair.
- At the centre, `g_yy = 1, 22/17, 136/99, 79271956/56195761` for sides 3, 5, 7, 9. With `E = 1`, `γ = 1`, the prices are `12/11`, `102/91`, `297/263` and a fourth, all distinct (runner C1). ∎

## Theorem T3 — amplitude sourcing: no local rule either

*Statement.* Fix `R` and a held box, with `y` at least `R + 3` from the wall in every coordinate. Let `v = g(·, y)` outside `B_{R+1}(y)` and `v = 0` on `B_{R+1}(y)` and on the wall, and let `σ = (1 − A)v`. Then:
- (a) `σ` lives on the two layers at distance `R + 1` and `R + 2`. Its field is `v`, which is zero on `B_{R+1}`. Its total is exactly `1`.
- (b) Add `c σ` to any amplitude supported in `B_R(y)`, as bodies at rest with rest energies `cσ_x/φ₂(x)`, where `φ₂ = φ₁ − kcv`. Then `ψ₂ = ψ₁ + kcv` solves the static law, uniquely for small `|c|`. Every datum within radius `R` is unchanged, and the ledger moves by exactly `c`, so the price moves.

*Proof.*
- (a) Away from the two layers `v` is locally `0` or `g(·, y)`, both annihilated by `1 − A`. The total of `σ` is the flux of `g(·, y)` through the wall, which is `1`.
- (b) The law holds on the cage by construction, and nothing changes elsewhere. Uniqueness: the operator's smallest eigenvalue is at least `x²/2 − x⁴/24 + k·min(m, 0) > 0`, with `x = 3/(n − 1)`.
- Checked exactly, with zero residuals, for side 7 with `R = 0`, `c = 1/5`, and side 9 with `R = 1`, `c = 1/4` and `c = −1/7` (runner D1). ∎

## Theorem T4 — an exact local price when the source is point-like

*Statement.*
- (a) Suppose the effective source `s = Kφ` satisfies `s − Qδ_y = (1 − A)f` with `f` finitely supported. Then in every held box whose interior contains the source:
  - `ψ = kQ g(·, y) + k f`;
  - `φ'_y = φ_y + k f_y`;
  - `E' = Q/(φ_y + k f_y)`.
- (b) `f` is unique and lies inside the bounding box of the source, so it is found from the window.
- (c) Block 116's star is such a source, with `f = −6s₁δ_y`. The rule then reduces to `c/(1 − kc)`.
- (d) The distance-two cross is not point-equivalent.

*Proof.*
- (a) `ψ = kG s = kQ g(·, y) + kG(1 − A)f = kQ g(·, y) + k f`, since `f` vanishes on the wall. With T1, the post-event field is `ψ − kf`.
- (b) At a point of `f`'s support with maximal first coordinate, `(1 − A)f` one step further out equals `−f/6 ≠ 0`. So `f`'s support lies strictly inside the source's, and a finitely supported harmonic function is zero.
- (c) Symbolic reduction (runner E1).
- (d) If `w = (1 − A)f` with `f` finite, then `Σ P w = 0` for every discrete harmonic polynomial `P`. The quartic `x⁴ − 6x²y² + y⁴ − 2z²` is discrete harmonic. It pairs to `0` with the star's excess and to `48` with the cross's (runner E1).
- The rule is checked exactly for three asymmetric sources in cubes of side 7 and 9 (runner E1). ∎

## What this settles and what it does not

- **Settled.**
  - Under both readings, no rule of any fixed radius sets the formation price in every held box, for unrestricted amplitudes.
  - The walls enter the price, through the unit response under records only and through far charges under amplitude sourcing.
  - A point-equivalent source has an exact local price.
- **For the owner's reading of records.** A record that forms cannot keep the ledger using local information alone, except when its effective source is point-like from outside. The price is one of the things records alone, looking locally, do not fix.
- **Not settled.**
  - Sources confined to the window that are not point-equivalent. Whether the window field then determines the box is open.
  - Crowds of records near the window.
  - The delayed field law, block 57, the probe's conditional part (b), which is not used here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 116: forming one record keeps the ledger only at a price; can a local rule set it? (probes task a-formation-price-from-local-data)"
source_of_blocker_text: probes task J:derive:a-formation-price-from-local-data (after block 116)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "window-confined sources that are not point-equivalent; crowds of records; the delayed law"
conditional_surface_status: "held cubes; bodies at rest for the cage; unrestricted amplitudes for T2-T3"
hypothetical_axiom_status: "the held-wall law and its readings are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 116: the price of forming one record, the two readings, the star's wall-free price and the cross's box-dependent one.
- **Probes.**
  - #9175, worker `w-macbookpro9927a-jec8b`, Claude Opus 5.5, the supervisor's own model family, found T1–T4 with an exact checker.
  - #9311, a Grok worker, another model family, refereed it with its own checker: "HIT: confirmed - no local rule of any fixed radius sets the formation price in every held box, while a point-equivalent source has the exact local price Q/(phi_y + k f_y)."
- **In the literature.**
  - A charged shell with no field inside (Faraday's cage).
  - The discrete maximum principle.
  - Harmonic polynomials as moments (the multipole expansion).
  - The smallest-eigenvalue bound for a perturbed matrix (Weyl's inequality).
  - Reference only.
- **New here.** The harvest. The probe's decimal comparisons are replaced by exact ones, and its conditional delayed part is left out.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: whether a local rule sets block 116's price. The obligations are:
- (O1) the premises (A3);
- (O2) the ledger identity (B1);
- (O3) records only (C1);
- (O4) amplitude sourcing (D1);
- (O5) point-equivalent sources (E1).

The strongest missing step is window-confined sources that are not point-equivalent.

## No-Go Discipline Gate

The note's negative sentences:
- under records only, no rule of any fixed radius sets the price;
- under amplitude sourcing, no rule of any fixed radius sets the price.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The window data do see the box.* Under records only they are constant. Under amplitude sourcing the cage leaves them unchanged exactly (C1, D1). ATTEMPTED.
2. *The price does not depend on the box.* The response grows with the box, and the cage moves the ledger (C1, D1). ATTEMPTED.
3. *The cage's configuration is not a solution, or not unique.* Zero residual, and a positivity certificate (D1). ATTEMPTED.
4. *Point-equivalence is too special to matter.* Block 116's star is a case, and the cross is not (E1). ATTEMPTED.

Scope left open:
- window-confined sources;
- crowds;
- the delayed law;
- rules allowed to read the whole lattice.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- "By construction" appears once, for the cage solving the law, and the runner checks that residual.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 116 (landed) | the law, the readings, the price | yes (quoted, A3) |
| probe #9175 and referee #9311 | the result and its confirmation | yes (ported, rerun) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no local rule under either reading; the exact local price for point-equivalent sources" | executed: exact static solutions and residuals | executed: the response's growth site by site; the cage's layers | executed: the four prices; star and cross | executed: three cage pairs, three point-equivalent sources, the quartic | not executed: confined non-point sources; crowds; the delayed law |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A physical rule could read far data."
  - *Reply:* Then it is not local, which is the point.
  - The note does not say that no rule exists. It says that no rule of any fixed radius does.
  - The positive part, T4, gives the local rule where one exists.

### N8 — Cross-cycle echo
- Block 116: the price, and one price for every site only with the ambient at infinity.
- This note: no local rule sets it, except for point-equivalent sources.

## Falsifiers

- Two held boxes with identical window data under records only and equal prices for every amplitude.
- A cage that changes a window datum.
- A point-equivalent source whose price differs from `Q/(φ_y + k f_y)`.

## Boundaries and non-claims

- Block 116's held-wall law; held cubes.
- The cage is built from bodies at rest with signed rest energies, as block 116's witness allows.
- The delayed law is not used.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 116 (landed), restated and quoted.
- Named standard imports, at definition level:
  - the discrete maximum principle;
  - summation by parts with discrete harmonic polynomials (the multipole moments);
  - the smallest-eigenvalue bound (Weyl);
  - exact rational linear algebra.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9175 (Claude Opus 5.5) found the result.
  - #9311 (a Grok worker, another family) refereed it with its own checker.
  - The supervisor ported the exact families and replaced the decimal comparisons.
- **Before writing.** The own prior-art check covered memory, open PRs and main. It found block 116 and no earlier harvest.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_2026_09_26.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
