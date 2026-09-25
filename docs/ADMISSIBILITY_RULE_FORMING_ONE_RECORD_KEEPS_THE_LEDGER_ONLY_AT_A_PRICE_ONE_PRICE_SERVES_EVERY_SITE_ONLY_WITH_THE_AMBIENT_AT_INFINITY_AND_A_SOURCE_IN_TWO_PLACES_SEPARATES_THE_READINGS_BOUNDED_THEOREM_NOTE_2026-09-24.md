---
claim_id: admissibility_rule_forming_one_record_keeps_the_ledger_only_at_a_price_one_price_serves_every_site_only_with_the_ambient_at_infinity_and_a_source_in_two_places_separates_the_readings_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Supplied held-boundary quadratic static model: ledger identity for a fixed finite-support Hermitian
  amplitude with a positive static solution; positive replacement energy only below target capacity; site independence
  exactly on equal-diagonal target sets; finite-box counterexamples; star price under feasibility and cubic symmetry.
  Infinite-lattice statements additionally use the explicitly constructed transient potential for compact nonnegative
  sources. The two-source calculation distinguishes stipulated first-order field functionals, not an established
  record measurement or ensemble-average test.'
upstream_dependencies:
- admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
- admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21
- admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_the_monopole_never_jumps_the_dipole_does_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_forming_one_record_keeps_the_ledger_only_at_a_price_site_blind_only_with_the_ambient_at_infinity_2026_09_24.py
---

# Conditional formation energy: target capacity, a symmetric star and two static source conventions

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within the static clock law of blocks 55, 56 and 58 as landed, with a supplied formation event; harvest block from two Grok-refereed probes attempts; nothing adopted or registered; unaudited)

This note works within the static clock law of blocks 55, 56 and 58, as landed on main, with a supplied formation event that replaces an amplitude by one record at rest; it reports what the record's energy must be for the ledger to be kept, where the record forms, and what a source in two places does under the two readings of what sources the field; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 58, as landed, set two readings side by side. Either a spread amplitude sources the clock field (amplitude sourcing), or only records do (records only). It also found what one formation event does to the ledger. This note asks what the axioms leave to be supplied under either reading when a record forms.

- **T1: forming a record has a price.**
  - For any amplitude, moving ones included, the static ledger is `Λ = Σ_x e_x φ_x`, with `e` the amplitude's energy density at the ambient rate.
  - A record formed at `y` keeps the ledger only if its bare energy is `E' = Λ/(1 − kΛ g_yy)`.
  - At weak field this is `E' − E = k(E² g_yy − e·g·e)`: the record must carry the field energy gained when the source contracts to a point.
  - Under records only the amplitude sourced nothing, and the price is the whole self-energy of a point, `kE² g_yy`.
- **T2: where the record forms.**
  - On `ℤ³`, with the ambient at infinity, `g_yy` is the same at every site. One price then keeps the ledger wherever the record forms, and for an amplitude at rest the record is never lighter than the amplitude.
  - In a general box with its walls held, the price can depend on the site. Equal-diagonal target sets instead have one price. A 3³ cube needs four different energies at its four kinds of site. A specified low-self-potential target in the counterexample admits a *lighter* record; low self-potential alone is not a sufficient general criterion.
- **T3: the seven-site star.**
  - An amplitude at rest on a site and its six neighbours is exactly a point charge everywhere but at its centre.
  - Its feasible positive price, `c/(1 − kc)` with `kc < 1` with `c = m₀/(1 + km₀) + 6m₁`, is the same in every box symmetric about it: `1188/1091` for the uniform star at `γ = 1`.
  - The 19-site ball and the seven-site cross at distance two have prices that change with the box.
- **T4: a source in two places.**
  - At first order, a test body passing a source spread over two places is kicked by the weighted mean of its two one-place kicks if the unformed amplitude sources. Under records only it is not kicked at all.
  - So the mean kick occurs under amplitude sourcing only, and zero under records only, when each differs from the one-place kicks.
  - An exact witness in a box of side 9 gives four distinct values.

In plain terms, when a spread-out thing becomes one record at one site, the energy books balance only if the record is given the right energy. That right energy is its old energy plus the extra field energy of being squeezed to a point. With the walls infinitely far away, the right energy is the same wherever the record forms. With walls nearby, it depends on where the record forms. The axioms say nothing about a record's energy, so this is one thing records alone do not supply. The seven-site star is the one tested spread whose right energy never notices the walls. The last result distinguishes four stipulated field-functional values under named per-passage conditions; it does not derive what a body's records measure. Under records only, an unformed source in two places pulls nothing. Under amplitude sourcing it pulls with the average of the two places.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "Records form." "A state is a configuration of records."
  - Among the open gates outside the axioms the memo lists "source/action and physical-observable identification".
  - "Admissibility is not a dynamics axiom."
  - The clock law, the amplitude and the formation event below are supplied clauses. Nothing is adopted.
- **The static law** (blocks 55 and 56 as landed; block 56's Remark to T1).
  - A finite box has odd side `n`, and its boundary layer is the wall. Rates are `w = φ²`, with `φ = 1` held on the wall.
  - `F = (2/γ) Σ_bonds (φ_x − φ_y)²` with `γ > 0`, and `k = γ/12`.
  - An amplitude `χ` and a Hermitian `H` give `K_xy = Re χ_x†H_xy χ_y`. Its energy density at the ambient rate is `e = K1` (block 55 T1 at `φ ≡ 1`), and `E = Σ e`.
  - The ledger is `⟨χ|φHφ|χ⟩ + F = φᵀKφ + F`. At a fixed amplitude its static law is `((12/γ)(1 − A) + K)φ = 0` inside, `A` the average over the six neighbours.
  - With `ψ = 1 − φ`, which is zero on the wall, the law is `((1 − A) + kK)ψ = k e`.
  - `g = (1 − A)⁻¹` inside, with zero wall values. On `ℤ³` the same objects are taken with the ambient held at infinity, and `g_yy = G₀(0)` at every site.
- **Bodies at rest.** `K = diag(m)`, and `e = m`.
- **The two readings** (block 58 T4 as landed: two static source conventions).
  - *Amplitude sourcing*: the amplitude's `K` enters the law.
  - *Records only*: only records enter, and an unrecorded amplitude sources nothing.
- **The formation event** (block 58, supplied). An amplitude is replaced by one record at rest at `y`, with bare energy `E'`.
  - `E'` is not derived here. The note computes what it must be for the ledger to be kept (the *price*).
  - No rule for whether, where or when a record forms is assumed, and no odds are used.
- **The moving witness.**
  - `H_xx = μσ₃` with `μ = 3/2`, and `H_{x,x±e_j} = ∓(i/2)σ_j`, a walk of block 54's form.
  - The spinor amplitude sits on four sites, with a phase `((3 + 4i)/5)ⁿ` along one axis.
  - T1 holds for every Hermitian `H`; this one only witnesses it.

## Theorem T1 — the price of one record, for every amplitude

*Statement.*
- (a) If the static law at a fixed amplitude has a solution, its ledger is `Λ = Σ_x e_x φ_x`.
- (b) A record at rest at `y`, with bare energy `E'`, has ledger `E'/(1 + kE' g_yy)`. It keeps `Λ` iff `E' = Λ/(1 − kΛ g_yy)`, for a positive record energy exactly when `0 < kΛ g_yy < 1`. The algebraic formula alone does not ensure feasibility; at or above capacity no positive finite record energy works.
  - Under records only the amplitude sources nothing: `φ ≡ 1` before the event, `Λ = E`, and `E' = E/(1 − kE g_yy)`.
- (c) At fixed amplitude, as `k → 0`: `Λ = E − k e·g·e + O(k²)`, and
  `E' − E = k(E² g_yy − e·g·e) + O(k²)`.
  - Under records only, `E' − E = kE² g_yy + O(k²)`.

*Proof.*
- (a) With `ψ = 0` on the wall, summing by parts gives `Σ_bonds (φ_x − φ_y)² = Σ_bonds (ψ_x − ψ_y)² = 6ψᵀ(1 − A)ψ`. So at a solution `Λ = φᵀKφ + (1/k)ψᵀ(1 − A)ψ`.
  - The law says `(1 − A)ψ = k(e − Kψ) = kKφ`, so `(1/k)ψᵀ(1 − A)ψ = ψᵀKφ`.
  - Hence `Λ = (φ + ψ)ᵀKφ = 1ᵀKφ = Σ_x e_x φ_x`.
- (b) For `K = E' δ_y δ_yᵀ` the law gives `ψ = kE' φ_y g(·, y)`. So `φ_y = 1/(1 + kE' g_yy)`, and by (a) the ledger is `E' φ_y`. Solve for `E'`.
- (c) `ψ = kg(e − Kψ) = kge + O(k²)`, so `Λ = E − eᵀψ = E − k e·g·e + O(k²)`. Put this into (b). ∎

*Checked (B1, B2).*
- **The moving witness, at `γ = 1` in the box of side 7.** It has `E = 21/20`, of which the hopping part is `39/80`.
  - The ledger computed from its definition equals `Σ e φ` exactly, with every rate positive: `Λ = 0.993783…`.
  - The record at the centre keeps it at `E' = 1.121356…`. Under records only the same record needs `E/(1 − kE g_yy) = 1.193455…`.
- **Weak field.** At `γ = 10⁻⁴` and `10⁻⁵` the exact ratio `(E' − E)/(k(E² g_yy − e·g·e))` exceeds 1 by less than `k`.

For bodies at rest, (a) is block 56's `Σ m φ`, and (b) is block 58 T1. What is new here is (a) for amplitudes that move, (c), and the price under records only. `e` can have entries of either sign for a moving amplitude.

## Theorem T2 — where the record forms

*Statement.*
- (a) **One feasible price on equal-diagonal target sets.**
  - On `ℤ³` the price `E'_y = Λ/(1 − kΛ G₀(0))` is the same at every site.
  - In a held box it depends on `y` through `g_yy`. The uniform 3³ cube at rest (`E = 1`, `γ = 1`) in the box of side 7 has `Λ = 0.984627…` and needs:
    - `1.105484…` at its corners;
    - `1.106710…` at its edge midpoints;
    - `1.108108…` at its face centres;
    - `1.109712…` at its centre.
  - A formation energy that does not depend on the site keeps the ledger at every site of `ℤ³`. In a held box it does so only at sites sharing one value of `g_yy`.
- (b) **Never lighter on `ℤ³`.**
  - On `ℤ³`, for an amplitude at rest (`e ≥ 0`), `E'_y ≥ E` at every feasible target, exactly. A spread source can exceed the capacity of a single target, in which case there is no positive replacement energy. At first order the price `E² G₀(0) − e·g·e` is non-negative.
  - In a held box this fails at sites of low self-potential. Take the box of side 7 with `99/100` of `E = 1` at the centre and `1/100` at an interior corner `c`:
    - the first-order price at `c` is `(g_cc − ⟨ρ, gρ⟩)E² = −0.233350…`, and at `γ = 1`, exactly, `E'_c = 0.981042… < 1`;
    - at the centre, `E' = 1.002376… > 1`.

*Proof.*
- (a) Translation invariance on `ℤ³`; the box values are exact solves.
- (b) **Exact statement.** The argument is block 58 T1's. At fixed `φ` the ledger is affine in the bare energies, so its minimum over `φ` is concave in them.
  - On the simplex of bare energies with total `E`, that minimum is smallest at a vertex.
  - On `ℤ³` every vertex gives the same `E/(1 + kE G₀(0))`, so `Λ ≥ E/(1 + kE G₀(0))`.
  - The record's ledger increases with its bare energy, so `E'_y ≥ E`.
- (b) **First order.** A potential of `(1 − average)` is largest at its source, so `g(x, y) ≤ g(y, y) = G₀(0)` and `e·g·e ≤ G₀(0)E²` for `e ≥ 0`. ∎

*Checked (C1, C2).*
- The four prices of the cube are exact rationals from four solves, and strictly increase from corner to centre.
- The corner example is exact at `γ = 1`, on both sides of `E`.
- `g(x, y) ≤ g(y, y)` holds at every interior `x` of the box of side 7, for `y` the centre and for `y` the interior corner.

## Theorem T3 — the seven-site star

*Statement.* Take an amplitude at rest with bare energy `m₀` at `y` and `m₁` at each of its six neighbours `n_i`. Place it in a held box symmetric about `y` under the 48 signed permutations, or on `ℤ³`.
- (a) `ψ(x) = Q g(x, y)` at every site `x ≠ y`, with `Q = kΛ`. Away from its centre, the star's field is exactly a point charge's. At the centre, `ψ(y) = Q g_yy − 6q₁`, with `q₁ = km₁φ(n_i)`.
- (b) When `kc < 1`, the positive price of forming the record at `y` is `E' = c/(1 − kc)`, with `c = m₀/(1 + km₀) + 6m₁`. It is the same in every such box and on `ℤ³`.
  - For the uniform star at `γ = 1` it is `1188/1091`.
  - For `m₀ = 1/2`, `m₁ = 1/12`, `γ = 7/3` it is `5436/4631`.
- (c) At first order, `E' − E = k(12m₀m₁ + 36m₁²)`, whatever the box.
- (d) Larger symmetric spreads do not share (b). The prices in the boxes of side 7, 9 and 11 are:
  - the uniform 19-site ball (`y`, its six neighbours and the twelve sites at distance `√2`): `1.105562…`, `1.105646…`, `1.105662…`;
  - the uniform seven-site cross at distance two (`y` and the six sites `2e_j` away): `1.105773…`, `1.105054…`, `1.104955…`.

*Proof.*
- (a) The equation `(1 − A)g(x, ·) = δ_x`, evaluated at `y`, gives `Σ_i g(x, n_i) = 6g(x, y) − 6δ_xy`. By symmetry the six neighbours share one rate `b` and one charge `q₁ = km₁b`, and `q₀ = km₀a` at `y`, where `a` is the root rate phi at `y`. So `ψ(x) = q₀ g(x, y) + q₁ Σ_i g(x, n_i) = Q g(x, y)` for `x ≠ y`, and `ψ(y) = Q g_yy − 6q₁`.
- (b) By symmetry and the equation at `y`, `g(n_i, y) = g_yy − 1`. So `b = 1 − Q(g_yy − 1)`, and `a = 1 − Q g_yy + 6q₁ = b − km₀a`, giving `a = b/(1 + km₀)`.
  - Then `Λ = m₀a + 6m₁b = bc` with `Q = kΛ`, so `1/Λ = 1/c + k(g_yy − 1)`.
  - Hence `E' = 1/(1/Λ − k g_yy) = 1/(1/c − k)`. The walls entered only through `g_yy`, which has cancelled.
- (c) Expand in `k`.
- (d) Exact solves. ∎

*Checked (D1–D3).*
- (a) holds at every interior site of the boxes of side 7, 9 and 11, for both weightings.
- (b) holds exactly in all three boxes.
- (c) is a symbolic expansion.
- (d) The prices are exact rationals that differ from box to box.

The six arms average exactly to their centre, because the average over six neighbours is what `1 − A` subtracts. A spread that reaches past the nearest neighbours meets differences of the potential that the walls change, and its price then depends on where the walls are.

## Theorem T4 — a source in two places

*Setting.*
- A source `B` of energy `E_B`, at rest, is either unformed or formed.
  - Unformed, its amplitude has weights `p_L + p_R = 1` at two sites `L` and `R`.
  - Formed, it is one record at `L` or at `R`.
- A light test body `T` passes along a line. Its transverse kick is a fixed linear functional `κ` of the field `ψ`.
- Everything is at first order in `k`.

*Statement.*
- (a) **The kicks.**
  - `B` formed at `S ∈ {L, R}`, under either reading: `δ_S = kE_B κ(g(·, S))`.
  - `B` unformed, under records only: `0`.
  - `B` unformed, under amplitude sourcing: `p_Lδ_L + p_Rδ_R`.
- (b) **What separates the readings.**
  - A kick `p_Lδ_L + p_Rδ_R`, when that value is not `0`, `δ_L` or `δ_R`, occurs under amplitude sourcing only.
  - A kick `0`, when `0` is none of `δ_L`, `δ_R`, `p_Lδ_L + p_Rδ_R`, occurs under records only.
  - Neither statement uses how often or when `B` forms. It uses only that `B` is unformed during some passages.
- (c) **A witness.** The box of side 9, `L = (0, −2, 0)`, `R = (0, 2, 0)`, `T`'s line `(x, −1, 0)` with `|x| ≤ 3`, and `κ(ψ) = Σ_x (ψ(x, 0, 0) − ψ(x, −2, 0))/2`.
  - Per unit `kE_B`: `δ_L = −0.967409…` and `δ_R = 0.201858…`.
  - The mean for `p_L = p_R = 1/2` is `−0.382775…`, and for `p_L = 1/3` it is `−0.187897…`.
  - With `0`, that makes four distinct values in each case.

*Proof.*
- (a) At first order `ψ = kg e` is linear in the source.
  - A record at `S` is a point source of energy `E_B + O(k)` (T1).
  - An unformed `B` sources `E_B(p_L δ_{·L} + p_R δ_{·R})` under amplitude sourcing, and nothing under records only.
- (b) Compare the two sets of possible kicks.
- (c) Exact solves (a symmetry-reduced solve for `g(·, L)`, and its mirror for `R`). ∎

*The conditions, named and not assumed:*
1. `T`'s own records resolve its kick well enough to separate the values.
2. `B` is unformed during some passages. If it forms, it forms whole at one site (the Record axiom: a record locks one possibility at one site).
3. `T` is light (its own source is negligible) and does not cause `B` to form.
4. The field follows its sources statically during the passage. Block 57's delay is not treated.

*Remark (records only, from landed results).*
- Under records only an unrecorded packet is pulled and pulls nothing back. In block 55 T3's point-force model, with the packet's source zero, the force sum is the packet's pull.
- A formation event then keeps the ledger's number at T1(b)'s price. The flux at the walls still jumps from zero (block 58 T4).
- Under amplitude sourcing, keeping the ledger keeps that flux (block 58 T2).

## A reading of the axioms (not a theorem)

- **Where the readings differ.** The memo says: "A state is a configuration of records." and "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
  - Under records only, the field is a function of the configuration of records: one answer per state.
  - Under amplitude sourcing, the field depends on the amplitude, which is not a configuration of records. It gives one answer per state only if the amplitude belongs to its supplied condition.
- **Neither is axiom content.** The memo lists "source/action and physical-observable identification" among the open gates outside the axioms. The choice between the readings stays a named conditional; this note does not make it.
- **What records alone do not supply, under either reading:**
  - a formation clause that sets the record's energy, which must know the site if walls are near (T1, T2);
  - under records only, the reaction to an unrecorded body's pull, and the far field's jump at formation.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 58 as landed: two static source conventions; 'Motion, several records and records that move are not worked'; its N1 route 3 (an amplitude in motion) not worked; block 56 as landed: 'sources under the record reading' among its next trace actions"
source_of_blocker_text: blocks 56 and 58 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a formation clause that assigns the record's energy, or a proof that no local one keeps the ledger in a held box; T4 executed with block 54's walk as the test body and a named rule for its records; the curvature member (block 67); records that move after formation"
conditional_surface_status: "T1-T3 exact within the static law and the supplied event; T2(b) and T3 on Z^3 through the named potential; T4 exact at first order under four named conditions"
hypothetical_axiom_status: "the clock law, the amplitude, its energy density and the formation event are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 55 gave the energy density, the ledger's rate and the point-force model.
  - Block 56 gave the linear static law, its Remark that linearity does not need rest, and the ledger `Σ m φ`.
  - Block 58 gave the formation event: the price for bodies at rest (T1), the harmonic moments at the walls (T2), the dipole (T3) and the flux from nothing under records only (T4).
  - Block 57 gave the delay, and block 67 the curvature member. Neither is used.
- **The probes attempts**, both written by Claude Opus 5.5 and refereed by a Grok model, confirmed (#8982, #8998).
  - `sources-under-the-record-reading` a3 (issue #8653) found:
    - T1(c) for bodies at rest;
    - the average of T2(b)'s price over odds, and the box counterexample;
    - the star's box-independence, claimed for every symmetric amplitude, which a4 showed false past the star;
    - a numerical passage of a walk packet past an unrecorded lobe, not re-run here.
  - a4 (issue #8748) found:
    - T1 for every amplitude;
    - the star's closed form, with a proof, and the two counterexamples;
    - the cube's four prices;
    - T4's discriminator.
  - The referees did not rebuild T4's kicks or the moving witness. This runner does, but it is by the same model family.
  - Related earlier units by the same model: #8736 (a two-record ledger) and #8739 (the point body on `ℤ³`). Neither is a premise.
- **In the literature (reference only).**
  - What an unformed amplitude sources is the question of the semiclassical coupling of Møller and Rosenfeld, and of the models of Diósi and Penrose.
  - T4 is the lattice form of the test of Page and Geilker. They reported that a source whose placement was set by a random quantum outcome pulled as the realized outcome, not as the mean.
  - T3(a) is a lattice counterpart of Newton's shell statement. For a fixed amplitude, the note establishes it for the one-step star.
  - T2(b) uses the concavity argument of block 58 and the maximum principle.
- **New here:**
  - an independent exact runner;
  - T1(a) and (c) for moving amplitudes, and the price under records only;
  - T2(b) exact on `ℤ³`;
  - T3 with its proof, placed against boxes of side 7 to 11;
  - T4 with exact kicks;
  - the reading of where the two conventions part.

## Exact target and obligation graph

Target: what a formation event requires beyond records under each reading. The obligations are:
- (O1) the price for any amplitude;
- (O2) its dependence on the site;
- (O3) when the price is local;
- (O4) a discriminator between the readings;
- (O5) where the readings meet the axioms' sentences.

T1–T4 and the reading discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- a feasible site-blind price requires equal self-potentials on the allowed target set;
- in the displayed held-box counterexample the specified target gives a lighter record;
- the 19-site ball and the seven-site cross have box-dependent prices;
- under records only an unformed source gives no kick.

### N1 — Routes by which the sentences could fail or mislead
1. *Another bond energy.* T1(a) uses the linear law of the simplest bond energy. Another member's law is not linear (block 56).
2. *A record not at rest, or several records sharing the ledger.* Not treated. Block 58 N1 route 1 lists the second.
3. *The curvature member* (block 67). Not treated.
4. *A formation event that does not keep the ledger.* Then T1(b) says by how much the ledger changes.
5. *Beyond first order.* T4 is a first-order statement, and exact values beyond it differ.
6. *Records that move after forming.* Not treated. Block 58 N1 route 5 reads the event as a change of shape.
7. *Other spreads with a point-charge field.* Charges proportional to the walk's two-step distribution also give a point charge away from the centre and its neighbours. For a fixed amplitude those charges depend on the box. (d) is two witnesses, not a classification.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The law is static; block 57's delay is not treated.
- The walls are held at the ambient rate.
- The statements on `ℤ³` rest on the named potential of `(1 − average)` there.
- T4's conditions are listed.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | records form; a state is a configuration of records; source/action outside the axioms; no dynamics in the axioms | yes |
| blocks 55, 56, 58 (landed) | the energy density and point-force model; the linear static law and its Remark; the formation event and its price at rest | yes (restated) |
| blocks 57, 67 (landed) | the delay; the curvature member | placement only |
| probes (#8653, #8748; Grok-refereed #8982, #8998) | T1–T4 first derived | yes (re-derived) |
| registry entry 1 (`docs/repo/DEFERRED_DECISIONS.md`) | the parked statistical postulate | not used; no odds are assumed |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "forming a record keeps the ledger only at a price; one feasible price serves every site of an equal-diagonal target set; the star's price does not see the walls; a source in two places separates the readings at first order" | executed: the moving witness's ledger from its definition against `Σ e φ`; the record's ledger; the weak-field ratio at two couplings | executed: the cube's four prices; the corner example on both sides of `E`; `g(x, y) ≤ g(y, y)` at every interior site | executed: the star's field against a point charge at every interior site of three boxes; the first-order price symbolically | executed: the star's price, the ball's and the cross's in boxes of side 7, 9, 11 | T1 is an algebraic stationary identity; a positive formation price additionally requires the stated capacity bound; T2(a) applies to equal-diagonal targets, T3 to its interior star and symmetric domains; T2(b) on `ℤ³` for amplitudes at rest; T4 at first order for every linear kick; the law, the amplitude and the event are supplied |

### N6 — Partial-closure paths and primitive scan
- No registered primitive is used, and nothing is proposed for registration.
- The parked statistical postulate is not used. T4's condition that `B` is unformed during some passages concerns occurrence, not odds.

### N7 — Steelman
- *Objection:* "T4 is a known test with a source in two places (Prior art); nothing new." *Reply:* Yes in spirit. The note makes it exact within the supplied clauses and names what it needs from formation.
- *Objection:* "Records only fails action and reaction, so it is wrong." *Reply:* The axioms contain no conservation law. Which reading holds is the owner's call. The note gives the price of each.
- *Objection:* "The star is a curiosity." *Reply:* It gives one symmetric sufficient case of box independence. The two larger-spread witnesses do not classify every shape or establish an iff for locality.

### N8 — Cross-cycle echo
- Block 41 made a source a record, and block 55 made it the amplitude's energy density.
- Block 58 set the two readings side by side for one event.
- This note prices feasible positive-ledger replacements at a fixed amplitude, finds where the price depends on the site, and gives a first-order discriminator that uses only a test body's records.

## Falsifiers

- An amplitude whose static ledger differs from `Σ e φ`.
- A record whose ledger-keeping energy differs from `Λ/(1 − kΛ g_yy)`.
- A star in a symmetric box whose field away from its centre differs from a point charge's, or whose price differs from `c/(1 − kc)`.
- A first-order kick of an unformed two-place source under amplitude sourcing that is not the weighted mean of the one-place kicks.

## Boundaries and non-claims

- The clock law, the amplitude and the formation event are supplied.
- The record's energy is not derived. The price is what keeping the ledger would require.
- The choice between the readings is not made.
- T4 is first order and conditional on four named conditions.
- Motion after formation, several records and the curvature member are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 55, 56, 57, 58 and 67, restated or placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - summation by parts on the lattice;
  - the mean-value identity of `1 − A`;
  - the maximum principle;
  - concavity of a minimum of affine functions;
  - the potential of `1 − A` on `ℤ³` and its value `G₀(0)` (Watson), used only for its translation invariance and its maximum on the diagonal;
  - exact rational arithmetic.
- Reference only: Møller; Rosenfeld; Diósi; Penrose; Page; Geilker; Newton.

## Review record — historical author provenance

- **Who and when.** Supervisor-run block, the sixty-fourth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - Two probes attempts by Claude Opus 5.5 derived the results (#8653, #8748). Grok referees confirmed their exact parts (#8982, #8998).
  - The supervisor re-checked everything with its own runner. That includes T4's kicks and the moving witness, which no referee of another model family has run.
- **Before writing.** Main was re-fetched. Blocks 55, 56 and 58 were read as landed, and the axioms memo in full.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_forming_one_record_keeps_the_ledger_only_at_a_price_site_blind_only_with_the_ambient_at_infinity_2026_09_24.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.

## Current domain, feasibility and interpretation corrections

The matrix K is real symmetric and supported entirely inside the held boundary; any support at or coupling to a wall needs additional boundary terms. T1(a) is an algebraic stationary identity and does not imply existence, uniqueness, stability or phi>0 for indefinite K. These are separate requirements; the moving witness checks positivity for itself. The weak-field expansion is at fixed finite matrix K and fixed geometry near k=0, where the grounded operator is invertible.

For k>0 and Lambda>0 below every considered target capacity, y -> Lambda/(1-k Lambda g_yy) is strictly increasing in g_yy. Thus one price is site-independent iff g_yy is constant on the allowed target set. Infinite translation invariance is sufficient, not necessary: a finite box's symmetry-related targets already have equal diagonals. Lambda=0 is a separate trivial zero-energy case. Nothing here supplies a positive replacement at an infeasible target.

For T2(b) on the infinite lattice require compactly supported nonnegative masses and the ambient value at infinity. The zero-energy potential can be constructed as the integral of exp(ip.(x-y))/(1-(sum cos p_j)/3) over the normalized zone. Near p=0 the denominator is comparable to |p|^2, whose reciprocal is locally integrable in three dimensions. Equivalently its nonnegative walk-series representation gives the decaying positive potential; translation invariance gives a constant diagonal. Grounded-box exhaustion gives the same finite-support potential matrices. The finite-box strictly convex diagonal-mass minimizers and their concavity inequality pass to that limit through these finite matrices. Consequently the original ledger is at least the one-point ledger of total bare mass E. Inverting the increasing one-point ledger then gives E'>=E only if the positive replacement is feasible. This explicitly supplies the infinite-volume argument; the current parent notes themselves claim only finite geometry. No infinite-distance force or arbitrary noncompact-source theorem follows.

The star requires nonnegative m0,m1, its six neighbors in the interior, cubic symmetry of the held domain around its center and k>0. Its exact positive formation energy exists iff kc<1. For kc>=1 the cancellation in the rational formula identifies infeasibility rather than a negative physical record energy. The field identity still holds for the positive static star. The 19-site ball and distance-two cross are two box-dependent examples, not a theorem about every larger support.

T4 defines a fixed linear functional of a static first-order field. Its four values distinguish the stipulated per-passage alternatives only if the listed readout, source-persistence and backreaction assumptions hold. A random mixture of localized sources can have exactly the same ensemble mean as the distributed source by linearity; a mean measurement alone is not a discriminator. No rule turning this field functional into a record, no formation statistics and no microscopic trajectory are established. The optional point-force comments use a separately supplied force model; they are not a consequence of the clocked quantum walk or an argument choosing a source convention.

## Current canonical dependencies

- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): current narrowed parent only.
- [admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md): current narrowed parent only.
- [admissibility_rule_what_a_formation_event_does_to_the_ledger_and_to_the_far_field_the_monopole_never_jumps_the_dipole_does_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md): current narrowed parent only.
