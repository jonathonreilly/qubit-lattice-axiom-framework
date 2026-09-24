---
claim_id: admissibility_rule_the_rules_own_clock_has_no_far_field_the_pull_needs_a_rate_law_with_a_monopole_a_rest_energy_and_a_coupling_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading and the supplied rate clauses of blocks 50 (the local clock 1/pi_x, pi_x the product of the record's pair weights c omega), 53 (u = log w; a record enters as a source log kappa in u_x - (1/6) sum u_(x+e) = (log kappa) n_x), 54 (the walk; as landed on main its exact packet force is withdrawn) and 55 (the kept ledger, its linearized law L_avg(delta u) = -(gamma/(6 wbar))(e - mu) with mu = ledger/N, and its separately supplied point-force model). Exact: (T1) for every rate field on a torus the sources of block 53's law sum to zero, and a clock whose rate at a site is any function of the records within a fixed distance R is ambient beyond R, so its field and sources vanish beyond R + 1: no monopole, no tail, no pull at a distance; block 53's clock gives an n-record body the total source n log kappa, which no such clock can. (T2) The Admissibility rule's own clock (block 50's 1/pi_x) as block 53's kappa at (3,1,2), c0 = 1/2: an isolated record has kappa = 1 exactly; one record neighbour 12/17, 12/7, 1 (equal, opposite, orthogonal); two 1/2 to 3; averages over the partner 382/357 (uniform) and 352/357 (pair law); in block 53's geometric form kappa = pi_x^(-5/6) when each neighbour's only record neighbour is x; its field is u = -log pi exactly, confined to records that have neighbours. (T3) In block 55's supplied point-force model equal and opposite pulls need S/E universal; identifying a packet's source with the linearized law (S/E = -gamma/6, an identification the landed block 55 does not make) gives log kappa = -(gamma/6) E_rec; no on-site 2x2 term anticommutes with the walk's sigma_1, sigma_2, sigma_3, so a walker at rest has E_rec = 0 and kappa = 1; the field energy (2/gamma) sum (sqrt(w_x) - sqrt(w_y))^2 has weight one for every gamma and the weak-field pull depends on gamma: gamma is a free physical number. EXECUTED, NOT CLAIMED: a clump's field under both clocks on a 24^3 torus; block 39's law sampled at densities 0.05 and 0.2 (records' own clocks slow on average, repaid exactly at empty sites). From a probes worker (Claude Opus 5.5), refereed by another model family (a Grok model). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_rules_own_clock_has_no_far_field_2026_09_23.py
---

# The rule's own clock has no far field: the pull needs a rate law with a monopole, a rest energy and a coupling that records do not supply

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; a probes worker's result refereed by another model family, with the supervisor's general form of its key step; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading and the supplied rate clauses of blocks 50, 53, 54 and 55; it reports, from a probes worker's result refereed by another model family, what the Admissibility rule's own clock can and cannot supply to the pull between records; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 95 (#8860) found that records on their own clocks attract with a one-over-distance potential when each record slows the clocks around it (block 53's `κ`). Block 53's PR text (#8568, T4) remarked that block 50's local clock `1/π_x` is such a ratio at contact; the version landed on main (c3f8c47a58) does not carry that remark. So the question is whether the Admissibility rule's own odds supply `κ`, or whether it has to be supplied. A probes worker answered it (task `J:derive:kappa-from-the-rule:a2`, worker `w-macbookpro90c72-j9337`, Claude Opus 5.5), and a referee of another model family (`w-macbookpro90c72-j6891`, a Grok model) confirmed it. This note restates the result, proves its key step in general, and adds a control.

- **T1: a clock set by nearby records has no far field.** For any rate field on a torus, the sources `u_x − (1/6)Σu_{x+e}` of block 53's law sum to zero. Now suppose a site's rate is a function of the records within a fixed distance `R`. Then it is ambient beyond `R`, so its field and its sources vanish beyond `R + 1`: no monopole, no tail, no pull at a distance. Block 53's clock gives an `n`-record body the total source `n log κ`, and no such clock can.
- **T2: the rule's own clock, read as `κ`.** Block 50's clock `1/π_x` at `(3,1,2)` and `c₀ = 1/2`:
  - An isolated record has `κ = 1` exactly.
  - With one record neighbour, `κ = 12/17, 12/7, 1` for equal, opposite and orthogonal contents; with two, `κ` ranges from `1/2` to `3`.
  - Its average over the partner's content is `382/357 > 1` uniformly but `352/357 < 1` under the pair law.
  - In block 53's geometric form, `κ = π_x^{−5/6}`: below one exactly where the record's own pair weights are favoured.
  - Its field is `u = −log π`, which stays on the records that have neighbours.
- **T3: what the pull needs instead.**
  - In block 55's supplied point-force model, equal and opposite pulls need the ratio of source to energy to be universal. If a packet's source is identified with block 55's linearized field law, that ratio is `−γ/6` and a record needs `log κ = −(γ/6)E_rec`, so `κ` gives way to the record's energy. The landed block 55 keeps its point-force coupling separate from `γ` and does not make this identification.
  - No on-site `2×2` term anticommutes with the walk's `σ₁, σ₂, σ₃`. A walker at rest therefore has `E_rec = 0` and `κ = 1`, as T2's isolated record does. A rest energy needs a term like block 77's staggered one.
  - The coupling `γ` meets every clause of blocks 53–56 at every positive value, and the pull depends on it. So `γ` is a free physical number.

**Executed control (not claimed).**
- On a `24³` torus, a clump of 27 records under the rule's clock has a field on 25 sites, all inside the clump, and no pull anywhere outside it. Under block 53's clock the same clump has total source `n log κ` and a field across the box.
- Block 39's law, sampled at densities `0.05` and `0.2`, gives records a mean source of `−0.007` and `−0.033`: records' clocks slow on average. The empty sites repay it exactly (`+0.0004`, `+0.008`), and the total is zero to rounding.

In plain terms: under the rule's own odds, a record whose neighbours it likes ticks slowly, but its empty neighbours tick fast by exactly the same total. Nothing is left over to reach a distant body, so the rule alone gives no long-range pull. The one-over-distance pull of block 95 needs three things that records do not supply:
1. a law in which each site's clock is set by its neighbours' clocks, not only by nearby records (block 53);
2. a rest energy, which comes from the walk's species structure (block 77), not from the records;
3. a coupling `γ` that nothing yet fixes.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."; "Admissibility is not a dynamics axiom." It does not "define a time metric", so rates are supplied clauses. Nothing is adopted.
- **The owner's reading** (records move, one per site at a time).
- **The six-axis rule at `(p, q, r) = (3, 1, 2)`.** The neutral scale is `c₀ = 6/(p + q + 4r) = 1/2`, and the pair weights are `c₀ω = 3/2, 1/2, 1` for equal, opposite and orthogonal contents (block 40, #8546, a working value, not registered).
- **Rates.**
  - Block 50 (#8562): the local clock runs the event of the record at `x` at rate `1/π_x`, where `π_x` is the product of its pair weights with its record neighbours. An empty site or an isolated record has `π = 1`, the ambient rate (the worker's stated assumption).
  - Block 53 (#8568): `u = log w`. A record enters as the source `log κ` of `u_x − (1/6)Σ_e u_{x+e} = (log κ)n_x`, where `κ` is the ratio of its rate to a degree-one mean of its neighbours' rates; the geometric mean makes the law exact.
- **The pull and the ledger.** Block 54 (#8570) gives the walk; as landed on main (c3f8c47a58) its exact force on every packet is withdrawn. The pull used here is block 55 T3's separately supplied point-force model: a body feels minus its energy times the central difference of the other body's field. Block 55 (#8571, landed in c3f8c47a58) gives the kept ledger and the linearized law `L_avg(δu) = −(γ/(6w̄))(e − μ)`, with `μ` the ledger over `N`; as landed, the point-force model carries its own coupling, not implicitly `γ`. `G` denotes the even kernel of `1 − A`, with `A` the average over the six neighbours.
- **Provenance.**
  - The worker (Claude Opus 5.5) is the same family as the supervisor. The referee is a Grok model, another family; it confirmed the pair weights, both neighbour tables, the two averages, the zero total of the rate-field sources, and the pull identity with its `κ`. It left `γ` free, as the worker did.
  - T1's general form is the supervisor's. The worker's step is its case of the rule's clock.
- **Names.** The weak-field law is the lattice form of the second static theory of Einstein of 1912 (block 55's placement). The `σ_a` are the Pauli matrices.

## Theorem T1 — a clock set by nearby records has no far field

*Statement.*
- (a) For every rate field on a torus, `Σ_x (u_x − (1/6)Σ_e u_{x+e}) = 0`.
- (b) Suppose the rate at each site is any function of the records within graph distance `R`, and ambient when there are none. Then for records on a torus, or for a finite cluster of records on `Z³`:
  - `u` vanishes beyond distance `R` of the records;
  - block 53's sources vanish beyond `R + 1`;
  - the sources sum to zero.

  Such a clock has no monopole and no tail, and the pull `−E∇u` on a body farther than `R + 1` away is zero.
- (c) Block 53's clock gives a body of `n` records the total source `n log κ`. For `κ ≠ 1`, no clock of kind (b) produces it.

*Proof.*
- (a) Each `u_y` appears once with weight `1` and six times with weight `−1/6`.
- (b) The rate at `x` depends on nothing beyond distance `R`, so it is ambient there. The source at `x` involves `u` at `x` and its neighbours only. The total is (a), or on `Z³` the same count over the finite support.
- (c) This is the contrapositive of (b).
- The runner checks (a) with a symbolic `u` at all 64 sites of `4³`, and (b) with arbitrary symbolic values per local pattern for `R = 1, 2` on `9³` (family B). ∎

## Theorem T2 — the rule's own clock, read as block 53's `κ`

*Statement* (exact at `(3,1,2)`, `c₀ = 1/2`).
- (a) An isolated record has `π = 1`, so `κ = 1` in any mean.
- (b) In the arithmetic mean, with record neighbours that have no other record neighbours:

| neighbours | `κ` |
|---|---|
| one equal / opposite / orthogonal | `12/17` / `12/7` / `1` |
| two: equal–equal, equal–opposite, equal–orthogonal | `1/2`, `6/5`, `12/17` |
| two: opposite–opposite, opposite–orthogonal, orthogonal–orthogonal | `3`, `12/7`, `1` |

- (c) Averaged over one partner's content: `382/357 > 1` uniformly, but `352/357 < 1` under the pair law.
- (d) In block 53's geometric form, `κ = π_x^{−5/6}` when each neighbour's only record neighbour is `x`, so `κ < 1` exactly where the record's pair weights are favoured.
- (e) Read as block 53's rate field, the clock is exactly `u = −log π`. Its sources sum to zero on every torus, and they vanish at every site whose own and whose neighbours' pair weights are one.

*Proof.*
- (b) and (c) are direct evaluations in rationals.
- (d): `κ = (1/π_x)/Π_y(1/π_y)^{1/6}` with `π_y = cω_{xy}`, so `Π_y π_y = π_x`.
- (e) is T1 with `R = 1`. The runner also checks it on 40 random configurations of the `3³` torus with formal logarithms (family C). ∎

## Theorem T3 — what the pull needs instead

*Statement.*
- (a) In block 55's point-force model, take a body with source `S_A` and energy `E_A`, and one with `S_B`, `E_B`. The pulls on them sum to `−(E_A S_B − E_B S_A)∇G`, which is zero at every separation where `∇G ≠ 0` if and only if `S/E` is the same for both. If a packet's source is identified with block 55's linearized law, `S/E = −γ/6`, and then a record needs `log κ = −(γ/6)E_rec`. The landed block 55 does not make that identification: its point-force coupling is its own.
- (b) No `2×2` on-site term anticommutes with `σ₁`, `σ₂` and `σ₃`. So the walk has no on-site rest energy: a walker at rest has `E_rec = 0` and `κ = 1`, in agreement with T2(a). A rest energy needs a term outside the on-site `2×2` class, such as block 77's staggered `mε`, which gives `κ = e^{−γm/6}`.
- (c) The field energy `(2/γ)Σ(√w_x − √w_y)²` has weight one under `w → tw` for every `γ > 0`. The weak-field pull `−(γ/4π)E_AE_B/R` depends on `γ`. Every clause of blocks 53–56 holds for the whole family `γ > 0`, so `γ` is a free physical number.

*Proof.*
- (a) The pull on `A` is `−E_A S_B ∇G`, and on `B` it is `+E_B S_A ∇G`, because `G` is even. Block 55 T3 is re-derived here (family D).
- (b) Solving `Mσ_a + σ_aM = 0` for `a = 1, 2, 3` gives `M = 0` (family E).
- (c) Direct substitution (family E); the clauses are block 55 T4's. ∎

## Executed control

The script is `specs/supervisor_control_block104_clump_fields.py`; its output is beside it in `.out.txt`.

**A 27-record clump on a `24³` torus.**
- Under the rule's clock:
  - the total source is `−9·10⁻¹⁶`;
  - the field is nonzero at 25 sites, all inside the clump;
  - the pull on a test site is `0` from three steps out.
- Under block 53's clock with `log κ = −0.1`:
  - the total source is `n log κ = −2.7`;
  - the field reaches across the box: `r·u = −0.92, −0.70, −0.43, −0.20` at `r = 2, 4, 6, 8`, where the removed mean flattens it;
  - the pull is nonzero at every distance.

**Block 39's law with vacancies**, sampled by exchanges and content re-draws at `(3,1,2)` and `c₀`:

| density | mean source at records | mean source at empty sites | total over all sites | mean `u` at records |
|---|---|---|---|---|
| `0.05` | `−0.0066` | `+0.00035` | `4·10⁻¹⁵` | `−0.0081` |
| `0.2` | `−0.0328` | `+0.0082` | `3·10⁻¹⁴` | `−0.0499` |

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 95 (#8860): the pull needs block 53's kappa; block 53 T4's remark that block 50's local clock is such a ratio at contact; the owner's 'not from records alone' question"
source_of_blocker_text: blocks 50, 53, 55, 95; probes derivation J:derive:kappa-from-the-rule (refereed by another family)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the rule's clock supplies no monopole; the pull needs a rate law in which rates set rates (block 53), a rest energy (block 77's staggered term), and gamma; next: a clause that fixes gamma (block 76's induced reading with its volume term), and the rest energy of a record rather than a walker"
conditional_surface_status: "T1 exact for every rate field and every finite-range clock; T2 exact at (3,1,2); T3 symbolic within blocks 53-55's clauses; the clump and the sampled law executed, not claimed"
hypothetical_axiom_status: "blocks 50, 53, 54, 55's rate clauses and block 40's neutral scale are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 53** (#8568; landed in c3f8c47a58): T3 showed that only the zero-sum part of a source enters on a torus, and T4 introduced records as a ratio `κ`. The PR text's remark that block 50's local clock is such a ratio at contact is qualified here: at contact it is, but its sources sum to zero, so it has no far field. The landed version omits the remark.
- **Block 50** (#8562) gave the local clock.
- **Block 55** (#8571; landed in c3f8c47a58 with its point-force model separated from the ledger's `γ` and no exact packet force established): the PR text's corollary gave `log κ = −(γ/6)E/w̄`. **Block 97** (#8872) used it for the sign of the pull.
- **Block 54** (#8570) gave the walk. **Block 77** (#8612) gave the staggered rest term. **Block 76** (#8611) found `γ_ind ≈ 10.5` under an induced reading, not adopted, which is repulsive once the volume term is kept.
- **Blocks 40 and 41** (#8546, #8547) found that at `c₀` a single record leaves an empty neighbour's formation rate unchanged, a neighbouring neutral-scale fact.
- The weak-field law is the lattice form of Einstein's second static theory of 1912 (block 55's placement).
- **New here:**
  - the rule's clock as `κ`, with its table and averages (the worker's);
  - the zero-total structure and its general form for every finite-range clock (T1);
  - the qualification of block 53 T4's remark;
  - the account of what the pull needs beyond records;
  - the control.

## Exact target and obligation graph

Target: whether the rule's own clock supplies block 53's `κ`, and if not, what the pull needs. The obligations are:
- (O1) the field of any finite-range clock;
- (O2) the rule's clock as `κ`;
- (O3) the pull's matching condition and a record's rest energy;
- (O4) the status of `γ`.

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- (i) no clock set by the records within a fixed distance has a far field;
- (ii) the rule's own clock cannot be block 53's `κ`;
- (iii) a walker at rest has no on-site rest energy;
- (iv) no present clause fixes `γ`.

### N1 — Routes by which the sentences could fail or mislead
1. *A clock whose range grows with the configuration.* For example, a rate set by the size of the cluster a site belongs to. T1 covers fixed ranges only. Such a clock is not local in the axioms' sense, and block 53's is the covariant local alternative.
2. *Rates that condition rates.* Block 53's clause C2 is exactly this. It is how a monopole enters, and it is a clause, not a consequence of the records.
3. *A different energy for a record.* T3(b) concerns on-site `2×2` terms in the walk. A rest energy from another clause (block 77's staggered term, or a record's own content) changes `E_rec`.
4. *A clause for `γ`.* Block 76's induced reading is the one candidate. Its sign with the volume term is repulsive.
5. *Motion and formation.* The clocks here time events. Block 99 showed that formation on the site's clock places records by `e^{+U}`, while motion gathers them by `e^{−U}`. Neither changes T1.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The rate clauses are named and supplied. The on-site class in T3(b) is stated.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the distribution sentence; no dynamics or time metric in the axioms | yes |
| blocks 50, 53 (#8562, #8568) | the local clock; the rate law and `κ` | yes |
| blocks 54, 55 (#8570, #8571) | the walk and the pull; the ledger and `γ` | yes |
| block 40 (#8546) | the neutral scale | yes (T2) |
| blocks 41, 76, 77, 95, 97, 99 | placement | no |
| probes worker `w-macbookpro90c72-j9337`, referee `w-macbookpro90c72-j6891` | the result; the confirmation | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no clock set by nearby records has a far field; the rule's clock is not block 53's `κ`; the pull needs a monopole law, a rest energy and `γ`" | executed: the pair weights, the `κ` table for one and two neighbours and its averages, exact | executed: symbolic rates at every site of `4³`; range-one and range-two clocks at every site of `9³`; the rule's clock on 40 configurations of `3³` | executed: the anticommutation equations for an on-site rest term; control: a clump's field and pull under both clocks | executed: bodies of up to six records; the pair identity for two bodies (symbolic) | T1 for every rate field and every finite-range clock on any torus or finite cluster of `Z³`; T2 at `(3,1,2)`; T3 symbolic; blocks 50, 53, 55 supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "T1 is trivial." *Reply:* It is short, and that is the point. Any clock the records set locally has zero net source, so the long-range pull cannot come from the rule's odds. It needs a law in which rates condition rates. Block 53 T4's remark suggested otherwise, and this note corrects it.
- *Objection:* "Records do slow their own clocks under the pair law." *Reply:* Yes: the mean source at records is negative at both densities sampled. It is repaid at the empty sites, so the total is zero and there is no monopole.

### N8 — Cross-cycle echo
- Block 53 made the rate law and left `κ` supplied.
- Block 95 found the pull.
- Block 97 fixed its sign.

This note says where `κ` cannot come from, and what the pull needs from outside the records.

## Falsifiers

- A clock set by the records within a fixed distance whose sources have a nonzero total, on a torus or a finite cluster.
- A `κ` in T2's table that differs from its exact value at `(3,1,2)`.
- A nonzero `2×2` on-site matrix anticommuting with all three `σ_a`.

## Boundaries and non-claims

- The rate clauses of blocks 50, 53, 54 and 55 are supplied, not adopted.
- T2 is at `(3,1,2)` and the neutral scale.
- T3(b) concerns on-site `2×2` terms only.
- No value of `γ` is claimed. No force law beyond blocks 55 and 95 is claimed, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 40, 41, 50, 53, 54, 55, 76, 77, 95, 97, 99 (PRs), restated or placed.
- Named standard imports, at definition level:
  - the Pauli matrices;
  - exact rational arithmetic and formal logarithms;
  - fast transforms, and the exchange sampler in the control.

## Review record

- **Who and when.** Supervisor-run block, the fifty-second since the source-link direction opened, built from a probes worker's result with an other-family referee.
- **Provenance.**
  - Worker `w-macbookpro90c72-j9337` (Claude Opus 5.5). Referee `w-macbookpro90c72-j6891` (a Grok model), which confirmed Steps 1–5 of the worker's derivation.
  - The supervisor re-ran the worker's check (all checks pass) and ported it. It proved T1's general form and ran the control.
- **Independence.** Mutation census: five mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_rules_own_clock_has_no_far_field_2026_09_23.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.

## Corrigendum 2026-09-23 (after the owner's landings)

Blocks 53, 54 and 55 were landed on main in c3f8c47a58 with review changes. This note now cites them as landed: block 53's remark about block 50's clock is in its PR text only; block 54's exact packet force is withdrawn; block 55's point-force model carries its own coupling, so T3(a)'s link to `γ` is stated as an identification the landed note does not make. T1 and T2, and every check, are unchanged.
