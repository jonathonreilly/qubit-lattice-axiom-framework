---
claim_id: admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_on_a_chain_two_records_are_two_free_fermions_of_the_charge_band_and_action_equals_reaction_survives_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN blocks 54, 55, 78 and 80 as landed on main (the reduced walk H_w = phi sigma_3 D phi on a ring or chain; two records under one record per site with generator P H2 P, H2 = H_w (x) 1 + 1 (x) H_w, P removing coincident sites, either exchange sign; the one-record density e_x = Re chi_x^dag (H_w chi)_x), all supplied. Exact: (T1) the pair's source is its compressed density - d<P H2 P>/du_x is the local density summed over the two slots, and the densities sum to the pair's energy (block 80 T1), and on block 78's ring they differ from the one-record densities at every site. (T2) on a chain, in the ordered basis with the gauge (-1)^x on down coins, P H2 P is the hop of two free spinless fermions of the up-coin band (bond weights phi_x phi_y) times the identity on the coin sequence: records never pass and keep their coins, so exclusion is the charge band's own exclusion principle. (T3) the compressed density is additive over the charge orbitals: it is the charge band's one-particle trace. (T4) in a uniform gradient w = lambda^(2 x_1) the excluded pair's generator obeys P H2 P T = lambda^2 T P H2 P under the joint translation, on a chain and for the three-dimensional walk alike, so with block 54's conditional argument the pair's passive mass is its compressed energy, equal to its active mass (T1), and block 55 T3's pulls are matched; the additive source over the original one-record states would give S/E = E_free/E_hc = 3356276805253/2833481402466 on block 78's ring. Harvest block from two Grok-refereed probes attempts, re-checked by an independent runner. The chain reduction (T2-T3) needs records that cannot pass, so it is one-dimensional; T1 and T4 hold in every dimension. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_two_records_are_two_free_fermions_on_a_chain_2026_09_24.py
---

# Under one record per site the source is the compressed density: on a chain two records are two free fermions of the charge band, and action equals reaction survives

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54, 55, 78 and 80 as landed; T2–T3 in one dimension, T1 and T4 in every dimension; T4's passive mass through block 54's conditional argument; harvest block from two Grok-refereed probes attempts; nothing adopted or registered; unaudited)

This note works within blocks 54, 55, 78 and 80 as landed on main, with two records under one record per site moving by the reduced walk; it reports what sources the clock field for such a pair and whether exclusion breaks action and reaction; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner's reading is that records move, never more than one at a site at a time. Block 78, as landed, found that one record per site is not a free sea: the excluded pair is not additive over its original one-record states. Block 80 found that the source of an excluded pair is its compressed density. Block 116 asked what sources the field under the record reading. This note asks whether exclusion breaks action and reaction.

- **T1: the source is the compressed density.**
  - The pair's energy responds to each clock by a local density, summed over the two slots, and these densities add up to the pair's energy (block 80 T1).
  - On block 78's ring they differ, at every site, from the sum of the two one-record densities.
- **T2: on a chain, two records are two free fermions.**
  - Order the records left to right and put the sign `(−1)^x` on down coins.
  - The excluded pair's generator is then the hop of two free spinless fermions of the up-coin band, times the identity on the coin sequence.
  - The records never pass each other and never change their coins. The exclusion is the charge band's own exclusion principle.
- **T3: so the source is additive after all, over the charge orbitals.** The compressed density is the charge band's one-particle trace. Block 78's non-additivity is with respect to the original coin-carrying one-record states, which are not these orbitals.
- **T4: action equals reaction survives exclusion, in every dimension.**
  - In a uniform clock gradient the excluded pair obeys the same scaling identity as one walker (block 54 T3), on a chain and in three dimensions alike. With block 54's conditional argument, the pair's passive mass is its compressed energy, which T1 makes its active mass: `S/E = 1`, so block 55 T3's pulls are matched.
  - Had one used the additive source, the sum of the original one-record densities, the pulls would miss by the exact factor `E_free/E_hc = 3356276805253/2833481402466 ≈ 1.18` on block 78's ring.

In plain terms, when two moving records may never share a site, the pair pulls on the clocks and is pulled by them with the same weight, provided the pair's source is its actual energy with the exclusion included. The naive guess, adding what each record would source on its own, gets it wrong by about 18% in the example. On a line the whole effect of exclusion is simple: the two records behave exactly like two free particles that cannot pass each other, carrying their coins along unchanged. In two or three dimensions records can go around each other, and that simplification is not available. The balance of pull and push does not need it: it holds in three dimensions too.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." This is the exclusion `P`. The owner's reading that records move is supplied.
  - "Each site has a domain of local possibilities." This is the coin.
  - "Admissibility is not a dynamics axiom." The walk is a supplied clause. Nothing is adopted.
- **The reduced walk** (blocks 54 and 55 as landed).
  - `H_w = φσ₃Dφ` with `(Dψ)(x) = (ψ(x+1) − ψ(x−1))/(2i)` and `w = φ² = e^u`, on a ring or an open chain.
  - The one-record density is `e_x = Re χ_x†(H_wχ)_x`.
- **Two records under exclusion** (blocks 78 and 80 as landed).
  - The generator is `PH₂P` with `H₂ = H_w ⊗ 1 + 1 ⊗ H_w`, where `P` removes coincident sites.
  - The pair state is `Ψ = ψ₁ ⊗ ψ₂ ± ψ₂ ⊗ ψ₁`, projected by `P`. Either exchange sign is allowed.
  - The compressed density is `e⁽²⁾_x = Σ_slots Re⟨PΨ|P_x^{[s]}H_w^{[s]}|PΨ⟩/⟨PΨ|PΨ⟩`.
- **Block 78's ring of 6.** Its runner's rates `φ_x = 1 + ((3x² + x) mod 5)/7`, and its two orthogonal complex states, reproduced exactly.
- **Pulls** (block 55 T3 as landed). A supplied reciprocal point-force model: the pulls between bodies are matched iff each body's source `S` is proportional to its energy `E` with one ratio.

## Theorem T1 — the source is the compressed density

*Statement.*
- For every rate field and either exchange sign, `∂⟨PH₂P⟩/∂u_x = e⁽²⁾_x`, and `Σ_x e⁽²⁾_x = ⟨PH₂P⟩`.
- On block 78's ring, the antisymmetric pair has `E_hc = 12349656/122046701`, while the two one-record energies sum to `E_free = 16169964/134909593`. The pair's density differs from `e₁ + e₂` at all six sites.

*Proof.* `P` is diagonal and does not depend on the rates. `∂H_w/∂u_x = ½{P_x, H_w}`, and `Σ_x P_x = 1`. This is block 80 T1. ∎

*Checked (B1).* At fixed state the energy is linear in each bond factor, so `(φ_x/2)∂E/∂φ_x` is an exact central difference. It equals the compressed density at every site, and the numbers above are exact.

## Theorem T2 — on a chain, two records are two free fermions

*Statement.* On an open chain with any positive rates and either exchange sign, write the pair in the ordered basis (`x_L < x_R`, coins in that order), with the sign `(−1)^x` on each down coin. Then `PH₂P = h₂ ⊗ 1_coins`, where `h₂` is the hop of two free spinless fermions with the up coin's amplitude and bond weights `φ_xφ_y`.

*Proof.*
- `σ₃` is diagonal, so coins are kept.
- A nearest-neighbour hop cannot carry a record onto or past the other under `P`, so the order is kept and no exchange sign ever arises.
- The gauge turns a down coin's hop `−(…)` into the up coin's, because `(−1)^x(−1)^{x±1} = −1`.
- Hard-core hopping of ordered particles on a chain is free fermion hopping, with no boundary term. ∎

*Checked (C1).* On a chain of 7 with generic rational rates, every nonzero matrix element (480, both exchange signs):
- keeps the coin sequence;
- moves exactly one record by one site;
- equals the gauged up-coin hop times `φ_xφ_y`.

## Theorem T3 — the source is additive over the charge orbitals

*Statement.* For a pair in the coin sector (up, down) with antisymmetric charge amplitude `c(x, y)`, the compressed density is
`e⁽²⁾_x = 2 Re Σ_z Σ_b c(x,z)* h(x,b) c(b,z)/‖c‖²`,
the trace of the charge band's one-particle density matrix against its hop.

*Proof.* The gauge is diagonal and commutes with `P_x`. So `Re⟨Ψ|P_xH|Ψ⟩` is the same in the gauged picture, where the pair is two free fermions (T2). ∎

*Checked (D1).* For a generic rational charge amplitude on the chain of 7, the equality holds exactly at every site.

Block 78's non-additivity and block 80 T3's non-preservation of the one-step momentum are statements about the original coin-carrying variables. In the charge picture the pair is two free fermions, whose crystal momentum is conserved at uniform rates (block 80 T2).

## Theorem T4 — action equals reaction survives exclusion

*Statement.*
- (a) In a uniform gradient `w = λ^{2x₁}`, `PH₂_wP T = λ² T PH₂_wP` on the interior, where `T` is the joint translation up the gradient. This holds on a chain and for the three-dimensional walk alike. It is block 54 T3's finite-power identity, carried to the excluded pair.
- (b) So, with block 54's conditional argument, the pair's crystal momentum changes at `−g⟨PH₂P⟩`: its passive mass is its compressed energy. T1 makes that its active mass too. So `S/E = 1`, and block 55 T3's pulls between the pair and any body with `S = E` are matched.
- (c) The additive source `e₁ + e₂` would give the pair `S/E = E_free/E_hc = 3356276805253/2833481402466` on block 78's ring. The pulls would then not match.

*Proof.*
- (a) Every hop, along or across the gradient, carries `φ_xφ_y`, so the joint translation multiplies each by `λ²`. Exclusion is translation invariant.
- (b) Block 54's argument, as landed (conditional), and block 55 T3.
- (c) The ratio of T1's energies. ∎

*Checked (E1).*
- (a) holds entrywise on every interior column checked: 12 of a chain with `w = 4^x`, and 400 of the three-dimensional walk `Σ_a σ_a S_a` in a `5×3×3` box with `w = 4^{x₁}`.
- The ratio in (c) is exact.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 78 as landed: one record per site is not a free sea (non-additivity); block 80 as landed: one-step momentum does not preserve the exclusion subspace, 'This alone establishes no nonconservation theorem'; block 116: what sources the field under the record reading"
source_of_blocker_text: blocks 78, 80 and 116
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the charge picture in two and three dimensions, where records can pass around each other; the overlap bound for far-apart records made exact"
conditional_surface_status: "T2-T3 exact on chains; T1 and T4(a) exact in every dimension; T4(b) through block 54's conditional argument and block 55 T3's supplied pull model"
hypothetical_axiom_status: "the walk, the moving records and the pull model are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the reduced walk and its finite-power identity.
  - Block 55: the energy density and the point-force model.
  - Block 78: exclusion as an interaction, with its ring of 6.
  - Block 80: the source identity and the subspace statement.
  - Block 116: sources under the record reading.
- **The probes attempts**, both written by Claude Opus 5.5 and refereed by a Grok model, confirmed.
  - `the-two-record-ledger-under-exclusion` a2 (issue #8736, referee #8974): T1 on block 78's ring, T4 and the additive ratio.
  - `the-two-record-pull-under-exclusion` a1 (issue #8737, referee #9056): T2, T3, and a bound on how far the source departs from additivity when the records are far apart. That bound is not re-run here.
- **In the literature.**
  - That hard-core particles on a line are free fermions is the Jordan–Wigner correspondence, as in the Tonks–Girardeau gas.
  - That the gravitating energy of a composite is its total energy, not the sum of its parts' free energies, is the classical statement about binding energy. Reference only.
- **New here:**
  - an independent exact runner, reproducing the exact numbers;
  - the results placed against blocks 78, 80 and 116 as landed.

## Exact target and obligation graph

Target: whether exclusion breaks action and reaction for moving records. The obligations are:
- (O1) the source;
- (O2) the chain reduction;
- (O3) the charge picture's additivity;
- (O4) active against passive mass.

T1 and T4 discharge O1 and O4 in every dimension; T2 and T3 discharge O2 and O3 in one.

## No-Go Discipline Gate

The note's negative sentences:
- exclusion adds no failure of action and reaction, in any dimension (T4, conditional as stated);
- the additive source over the original states does not give matched pulls.

### N1 — Routes by which the sentences could fail or mislead
1. *Two and three dimensions.* Records can pass around each other, so the reduction to free fermions (T2–T3) fails there. T1 and T4 do not use it: the source identity and the scaling identity hold in every dimension, so the matched pulls survive exclusion there too.
2. *Block 54's argument.* It is conditional as landed. T4(b) inherits that.
3. *The pull model.* Block 55 T3's point-force model is supplied, and the exact lattice law departs from it for free records too.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- T2–T3 are one-dimensional.
- The pull model is supplied.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; a site's possibilities; no dynamics in the axioms | yes |
| blocks 54, 55, 78, 80 (landed) | the walk, the density, the pair and the source identity | yes (restated) |
| block 116 | sources under the record reading | placement |
| probes (#8736, #8737; Grok-refereed #8974, #9056) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "under exclusion the source is the compressed density; on a chain two records are two free fermions; action equals reaction survives" | executed: `E_hc`, `E_free` and their ratio | executed: the source identity at six sites; the charge trace at seven | executed: all 480 matrix elements of the reduction | executed: the scaling identity on the interior columns | T1 and T4 in every dimension; T2–T3 on chains; T4(b) conditional; the clauses supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 78 showed exclusion is an interaction, so it must break something." *Reply:* It is an interaction relative to the coin-carrying one-record states. On a chain, relative to the charge orbitals, it is only the exclusion principle of free fermions, which breaks nothing.
- *Objection:* "One dimension is special." *Reply:* For the free-fermion picture, yes. The balance of pull and push rests on T1 and T4, which hold in every dimension.

### N8 — Cross-cycle echo
- Block 78 found exclusion as an interaction, and block 80 found the source identity.
- Block 116 found what a formation event requires.
- This note finds that, for moving records under exclusion, the books balance with the compressed source in every dimension, and on a line the pair is two free fermions.

## Falsifiers

- A rate field on a chain for which the compressed generator in the gauged ordered basis differs from the free two-fermion hop.
- A pair state whose compressed density differs from the charge trace.
- An interior column of the gradient chain on which the scaling identity fails.

## Boundaries and non-claims

- The walk, the moving records and the pull model are supplied.
- T2–T3 are one-dimensional; T1 and T4 hold in every dimension.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 55, 78, 80 and 116, restated or placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - hard-core particles on a line as free fermions;
  - exact rational arithmetic.
- Reference only: Jordan; Wigner; Tonks; Girardeau.

## Review record

- **Who and when.** Supervisor-run block, the sixty-ninth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - Two probes attempts by Claude Opus 5.5 derived the results (#8736, #8737). Grok referees confirmed them (#8974, #9056).
  - The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched. Blocks 78 and 80 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_two_records_are_two_free_fermions_on_a_chain_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
