---
claim_id: admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk H = sum_a sigma_a S_a and block 78's reduced ring walk sigma_3 p with its hard-core compression, all as landed on main and supplied; two records in the hard-core space HC (one record per site), the exchange P, and the compressed generator H_2. Exact: (T1) HC is closed under H_2, which is hermitian and commutes with P; so the symmetric and antisymmetric parts of HC are two composition rules, each closed, each with one record per site, each covariant, and, since a readout is determined by record content alone, each invisible to readouts except through dynamics; no axiom sentence chooses between them. (T2) on the infinite lattices Z^2 and Z^3 the exchange amplitude vanishes at orders 2 and 3 and first appears at order 4: tr(P H_2^4) = -8 per plaquette (-8 per site on Z^2, -24 on Z^3); per pair on Z^3, coin-summed, -2 for neighbours, -1 on a face diagonal, 0 at distance 2 on a line. (T3) on block 78's even rings tr(P (2H_2)^k) = 0 for k < N and 128, -1248, 7680 at k = N = 4, 6, 8; on odd rings a unitary commuting with H_2 and anticommuting with P makes the two sectors unitarily equivalent, so the sign is invisible at every order (checked on 5 and 7, proved for every odd N). (T4) no linear or antilinear involution of C^2 reverses all three sigma_a, so a record's content has no parity; a graded record needs C^4; the graded composite of two presentations is Cl(6,0), not M_2(C) x M_2(C); the discrete half-turn exchange squares to -1 on one record and +1 on two, on both sectors. So the exchange sign is a supplied choice, first visible in the fourth moment of a localised pair. Harvest block from a Grok-refereed probes attempt, re-checked by an independent runner. Nothing adopted; three or more records not treated; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_2026_09_24.py
---

# The exchange sign is not supplied by records: both hard-core sectors meet every axiom, and they first differ in the fourth moment, by −8 per plaquette

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54 and 78 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and its reduced ring form; one record per site as an interaction); it reports whether the axioms fix the sign with which two records compose, and where that sign first shows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 78, as landed, found that one record per site is an interaction, and compared the symmetric and antisymmetric two-record sectors on small rings. It said its finite moments do not prove "that every odd-ring spectrum coincides". This note asks the underlying question: do the axioms fix the sign with which two records compose?

- **T1: two rules, both allowed.**
  - The hard-core two-record space is closed under the walk, and the walk commutes with the exchange.
  - So the symmetric and the antisymmetric parts are two composition rules. Each is closed, has one record per site, and is covariant.
  - A readout is determined "by record content alone". Readouts therefore commute with the exchange and cannot tell the sectors apart directly.
  - No axiom sentence chooses between them.
- **T2: where the sign first shows.**
  - On `Z²` and `Z³` the exchange amplitude vanishes at orders `2` and `3`.
  - It first appears at order `4`: `−8` per plaquette.
  - Per pair on `Z³`, summed over coins, it is `−2` for neighbours, `−1` across a face diagonal, and `0` at distance two along a line.
- **T3: rings.**
  - On even rings the sign first shows at order `N`, because an exchange must wind.
  - On odd rings the two sectors are unitarily equivalent, so the sign never shows. This settles for every odd ring what block 78 left open.
- **T4: the content has no parity.**
  - No involution of a record's two-state content reverses all three coin matrices, so the grading of the site algebra's real presentation gives a single record no parity.
  - A graded record needs four states, which is the parked larger site algebra.
  - The discrete exchange of two sites squares to `+1` on both sectors.

In plain terms, when two records meet, quantum rules allow two ways for the pair to behave under swapping: symmetric or antisymmetric. That is, like bosons or like fermions. The axioms say a site holds at most one record and that only a record's content can be read. Both ways obey both sentences, and no other sentence picks one. The difference is real but faint. Two records have to trace out a little square, four hops, before the choice shows, and on a ring of odd length it never shows at all. So the sign is something the records do not supply. It has to be named, or it has to come from a larger site algebra, which is a decision that is parked.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." This gives the hard-core space and a conserved record number.
  - "A readout value is determined by record content alone." Readouts do not see which record is which.
  - "The full one-site possibility domain has algebraic presentation `M_2(C)`." A `Cl(3,0)`-compatible real presentation "may be used equivalently and adds no further primitive structure".
  - "A choice not fixed by the supplied structure remains a named conditional or open dependency."
- **The walk** (block 54 as landed). `H = Σ_aσ_aS_a` with `S_a = −i(T_a − T_a†)/2`, and on `Z²` the two-axis form `σ₁S₁ + σ₂S₂`. On rings it is block 78's reduced walk `σ₃p`. One hop has amplitude `1/2`, so `2H` has Gaussian-integer entries.
- **Two records** (block 78 as landed, which calls the compression and the composition supplied model choices).
  - `HC = span{e_{x,a} ⊗ e_{y,b} : x ≠ y}`.
  - The exchange is `P(u ⊗ w) = w ⊗ u`.
  - The compressed generator is `H₂ = Π_HC(H ⊗ 1 + 1 ⊗ H)Π_HC`.
  - A composition rule is a `P`-invariant, `H₂`-closed subspace of `HC`. The sectors are `K± = HC ∩ ker(P ∓ 1)`.
  - For `X` commuting with `P`, `tr_{K±}X = ½[tr_HC X ± tr(PX)]`: the sectors differ exactly by the exchange traces `tr(PH₂^k)`.
- **Comparators, named only:**
  - the connection of spin and statistics, and its topological route (Finkelstein–Rubinstein);
  - hard-core bosons;
  - the Jordan–Wigner map;
  - the Clifford grading.
  - Landed repository notes reach the same boundary in the operator-algebra picture: the statistics-agnostic no-go of 2026-05-25, the rotation-exchange no-go of 2026-05-28 and the ring-monodromy note of 2026-06-04.

## Theorem T1 — two composition rules, both allowed

*Statement.*
- (a) `HC` is `P`-invariant and closed under `H₂`. `H₂` is hermitian, and `[P, H₂] = 0`.
- (b) So `K₊` and `K₋` are each closed, each have one record per site and a conserved record number, and each have dimension `2n(n − 1)` on `n` sites.
- (c) Every lattice symmetry acts on two records as `W ⊗ W`, and every relabelling of a record's possibilities as `Ad(U ⊗ U)` or its antilinear form. These commute with `P`, so both sectors are covariant and both are invariant under relabelling.
- (d) Readouts commute with `P`, so each sector is a superselection sector for them.

*Proof.* The free generator and the projector onto `HC` both commute with `P`. The rest is the statement read against the axiom sentences quoted above. ∎

*Checked (B1).* On block 78's ring of four, on every basis vector of `HC` (dimension `48`): closure, hermiticity, and commutation with `P`. Also the sector dimensions.

## Theorem T2 — where the sign first shows

*Statement.* On `Z²` (two-axis walk) and `Z³`:
- (a) The coin-summed exchange amplitude `Σ_{a,b}⟨Ps|(2H₂)^k|s⟩` vanishes for every separation at `k = 2` and `k = 3`.
- (b) At `k = 4`, `tr(PH₂⁴)` is `−8` per plaquette: `−8` per site on `Z²`, and `−24` per site on `Z³`.
- (c) Per pair on `Z³`, `Σ_{a,b}⟨Ps|H₂⁴|s⟩` is `−2` for neighbours, `−1` across a face diagonal and `0` at distance two along a line.

So the first quantity that sees the sign is the fourth moment of the two-record energy of a localised pair, `⟨ψ±|H₂⁴|ψ±⟩ = ⟨s|H₂⁴|s⟩ ± Re⟨Ps|H₂⁴|s⟩`.

*Proof.*
- (a) An exchange path must carry each record to the other's site. With two hops each record hops once, onto a still-occupied site, so no path exists. On a bipartite lattice both records need hop counts of the same parity, so the total is even.
- (b) and (c) are the local enumeration of four-hop hard-core paths.

∎

*Checked (C1).* The exact enumeration of every separation up to distance `2`, at orders `2`, `3` and `4`, with Gaussian integers.

## Theorem T3 — rings: order N when even, never when odd

*Statement.*
- (a) On block 78's rings of `N = 4, 6, 8` sites, `tr(P(2H₂)^k) = 0` for `k < N`. At `k = N` it is `128`, `−1248` and `7680`.
- (b) On every odd ring the two sectors are unitarily equivalent: every spectral quantity agrees at every order.

*Proof.*
- (a) An exchange on a ring must wind, which takes at least `N` hops.
- (b) Let `J` be the sign of the order of the two positions, `G = (−1)^x` on each record, and `U = (σ₁ ⊗ σ₁)(G ⊗ G)J`.
  - `J` anticommutes with `P`. Under exclusion only a hop across the bond `(N − 1, 0)` changes the order, so `JH₂J` is the walk with that bond reversed.
  - For odd `N`, `G` maps the reversed walk to `−H`, and `σ₁` on each coin maps `−H` back to `H`.
  - So `UH₂U* = H₂` and `UPU* = −P`: `U` carries `K₋` onto `K₊`.

∎

*Checked (D1).* The exchange traces on the rings of `4`, `6` and `8`. The unitary `U` on every basis vector of the rings of `5` and `7`.

## Theorem T4 — a record's content has no parity, and the discrete exchange carries no sign

*Statement.*
- (a) No linear map `Γ ≠ 0` of `ℂ²` satisfies `Γσ_a = −σ_aΓ` for all `a`. The antilinear solutions are `cσ₂K`, and they square to `−|c|²`. So the grading of the real presentation assigns a single record's content no parity.
- (b) A graded record needs `ℂ⁴`: for example `Γ = 1 ⊗ σ₃` and `e_a = σ_a ⊗ σ₁`, whose product of the three `e_a` squares to `−1`. That is the parked larger site algebra.
- (c) Two graded presentations compose to `Cl(6,0)`: six anticommuting generators that square to one, with `64` distinct products. That is not the complex composite `M₂(ℂ) ⊗ M₂(ℂ)`, and no axiom sentence names a composite.
- (d) The half-turn about `e₂` composed with a shift exchanges two neighbouring sites and commutes with the walk. On one record its coin factor `D = −iσ₂` squares to `−1`. On two records `D ⊗ D` squares to `+1`, on both sectors alike.

*Proof.*
- (a)–(c) Linear algebra.
- (d) `D` conjugates `σ₁` and `σ₃` to their negatives and fixes `σ₂`, as the half-turn does to the axes. The topological argument that turns the one-record sign into an exchange sign needs a continuous configuration space, which the axioms do not supply.

∎

*Checked (E1).*
- The linear and antilinear solutions.
- The `ℂ⁴` grading.
- The six generators and their `64` products.
- The coin half-turn.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 78 as landed: its finite moments 'do not prove that exchange signs are generally irrelevant, that every odd-ring spectrum coincides, or that all differences are classified by parity'"
source_of_blocker_text: block 78 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "three or more records: at which order the sign first matters for the ledger's source; a clause that would fix the plaquette amplitude's sign"
conditional_surface_status: "T1-T4 on the stated lattices and rings; T3(b) for every odd ring; the walk, the compression and the composition supplied"
hypothetical_axiom_status: "the composition rule is a supplied choice; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 78: one record per site as an interaction, the sectors on rings of `4` to `7`, and the fourth traces `5/6` and `7/6` at `N = 4`.
- **Repository notes on main**, in the operator-algebra picture:
  - `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25`;
  - `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28` (the Finkelstein–Rubinstein route needs a continuum);
  - `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04`.
- **The probes attempt.** `the-exchange-sign-from-the-coin` a1 (Claude Opus 5.5) found T1–T4. A Grok referee confirmed it (#9073): "the axioms as stated do not choose the exchange sign". An earlier worker unit (#8642) had first seen the fourth-order difference.
- **In the literature.**
  - The connection of spin and statistics.
  - Hard-core bosons and the Jordan–Wigner map.
  - Clifford algebras and their gradings.
  - Majorana generators.

  All reference only.
- **New here:**
  - an independent exact runner in Gaussian integers;
  - T2 on the infinite lattices;
  - T3(b) for every odd ring, which settles an open item of landed block 78;
  - the third-column reading: the exchange sign is not supplied by records.

## Exact target and obligation graph

Target: whether the axioms fix the exchange sign, and where it first shows. The obligations are:
- (O1) the two rules (T1);
- (O2) the lattices (T2);
- (O3) the rings (T3);
- (O4) the grading and the discrete exchange (T4).

T1–T4 discharge them. Open: three or more records.

## No-Go Discipline Gate

The note's negative sentence: no axiom sentence fixes the exchange sign of two records.

### N1 — Routes by which the sentence could fail or mislead
1. *A composite named elsewhere.* A graded product of site algebras would supply the sign. It is not on main; a proposal of that kind (PR #7829) was closed.
2. *The larger site algebra.* `M₄(ℂ)` per site allows graded records. That decision is parked and is not touched here.
3. *Continuum limits.* The topological route needs a continuous configuration space, which the lattice axioms do not supply.
4. *Many records.* T2's order is for two records. With more records the order at which the sign matters for sources is not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used as a premise. The landed operator-algebra notes are cited as prior art only.

### N3 — Hidden-wall scan
None beyond the supplied walk, compression and composition.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; readout by content; the one-site algebra; the named-conditional clause | yes |
| blocks 54, 78 (landed) | the walk; the compression and the sectors | yes (restated) |
| probes (Grok-refereed #9073) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "both sectors meet the axioms; the sign first shows at order four, `−8` per plaquette; never on odd rings" | executed: closure, hermiticity and exchange commutation on the ring of four | executed: exchange amplitudes up to distance `2` on `Z²` and `Z³` | executed: exchange traces on rings of `4`, `6`, `8` | executed: the odd-ring unitary on `5` and `7`; the grading; the half-turn | the stated lattices and rings; every odd ring by proof; two records only |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration. The parked decision on a larger site algebra is named in N1 and not touched.

### N7 — Steelman
- *Objection:* "The spinor sign `D² = −1` is the spin–statistics connection, so the antisymmetric sector is forced."
  - *Reply:* On two records the discrete exchange squares to `+1` on both sectors.
  - Turning the spinor sign into an exchange sign needs a homotopy between the exchange and a full turn, and the lattice supplies none.

### N8 — Cross-cycle echo
- Block 78 found that one record per site is an interaction, and saw a fourth-order difference on one ring.
- This note shows that the sign itself is not supplied, finds where it first shows on the lattices, and settles the odd rings.

## Falsifiers

- An axiom sentence that holds in one sector and fails in the other.
- A nonzero exchange amplitude at order `2` or `3` on `Z²` or `Z³`.
- An odd ring on which the two sectors' spectra differ.

## Boundaries and non-claims

- The walk, the compression and the composition are supplied.
- Three or more records are not treated.
- The parked larger site algebra is not touched.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54 and 78, restated. The three landed operator-algebra notes, cited as prior art.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - linear algebra over `ℂ` and `ℝ`;
  - the Clifford algebra `Cl(6,0)` and its Jordan–Wigner generators;
  - Gaussian-integer arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-sixth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results. A Grok referee confirmed them (#9073).
  - The supervisor re-checked them with its own runner, in Gaussian integers.
- **Before writing.**
  - Main was re-fetched, and blocks 54 and 78 were read as landed.
  - The own-prior-art check found block 78's ring comparison and the three operator-algebra notes on main. This note is placed against them.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
