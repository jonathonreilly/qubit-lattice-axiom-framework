---
claim_id: admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_the_walks_force_is_a_bond_energy_times_a_clock_difference_and_no_ledger_can_demand_it_exactly_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54 (the clocked walk H_w = phi H phi, H = sum sigma_a S_a; as landed on main its exact packet-force reading is withdrawn and its ray model gives the wave number dk/dt = -E grad u), 63 (its momenta and bond currents), 64 (bond strains, plaquette curls, relabellings), 66 (the relabelling ledger and the force density f_j, with its corrigendum) and 72 (the two-step momentum). Exact: (T1) [X, T_n] = n T_n, so for any finite-reach momentum P commuting with the walk a plane wave in a uniform clock gradient changes <P> at first order by -E grad u . grad_k pbar, pbar the band value of P's symbol; the weight of the fall along j is d pbar/dk_j (cos k_j for the one-step momentum, cos 2k_j for the two-step one), and it has zero mean over every line of the zone: no local momentum that commutes with the walk falls with weight one at every wave number; weight one belongs only to the wave number of block 54's ray model, which is not a local density. (T2) For every state and rate field, f_j(x) = d_j phi(x) eps_j(x) + d_j phi(x - e_j) eps_j(x - e_j), eps_b the bond's cross energy: a bond energy times a clock difference (logarithmic-mean factor), equal to an energy-density part plus an exact remainder; a state on one sublattice has zero energy density everywhere and a nonzero force, so the force is no function of the energy density. (T3) Every ledger built from block 64's curls with site-multiplier rates demands no force (its identity has no rate term); a ledger that carries the rates exists (the volume member with the upwind transport) and demands a force built from the energy density and current; at first order the walk's force on plane waves is e cos k_j (centred difference of u)/2, and two waves with equal energy density and zero current get forces 0 and nonzero, so no such requirement matches the walk's force at every wave number. (T4) Reach three: the two-step bond form, weight cos 2k_j, the same obstruction. From probes workers (Claude Opus 5.5), refereed by another model family (a Grok model). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_2026_09_23.py
---

# No local momentum falls with weight one on the lattice: the weight is the slope of its band value, with zero mean; the walk's force is a bond energy times a clock difference, and no ledger that carries the rates can demand it at every wave number

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; probes workers' results refereed by another model family; nothing adopted or registered; unaudited)

This note works within the supplied clauses of blocks 54, 63, 64, 66 and 72 (the clocked walk, its momenta, the relabelling ledger and its force); it reports, from probes workers' results refereed by another model family, what falls with weight one on the lattice and whether a ledger can demand it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 54 (#8570), as landed on main (c3f8c47a58), keeps the clocked walk's finite-power translation identity and a ray model in which the wave number falls with weight one, `dk/dt = −E∇u`; on review it withdrew the original claim of an exact force on every packet. Block 66 (#8597), as landed, gives a continuum stress balance and states that the walk's lattice force equals energy density times the log-rate difference only at leading order; its corrigendum found that on the lattice curl-built ledgers forbid the fall. Blocks 69 and 72 found the lattice weights of two particular momenta: `cos k` and `cos 2k`.

Two probes workers (Claude Opus 5.5) settle the lattice picture in general, and a referee of another model family (a Grok model) confirmed both.

- **T1: no local momentum falls with weight one.**
  - For any local momentum that commutes with the walk, a plane wave in a clock gradient changes it at first order with weight `∂p̄/∂k_j`, the slope of the momentum's value on the band.
  - That slope has zero average over the zone. So along every line of wave numbers the momentum either never falls or rises somewhere.
  - Weight one at every wave number belongs only to the wave number of block 54's ray model, the spacing of a ray's crests. It is not a local density.
- **T2: the force is a bond energy times a clock difference.**
  - Exactly, for every state and rate field, block 66's force density is `d_jφ(x)ε_j(x) + d_jφ(x − e_j)ε_j(x − e_j)`, where `ε_b` is the energy on the bond.
  - The bond energy is the energy density's share plus an exact remainder, and the force is not a function of the energy density. A state on one sublattice has zero energy density at every site and a force.
- **T3: no ledger of the known classes demands the walk's force.**
  - Ledgers built from block 64's curls, with the rates as site multipliers, demand no force at all.
  - A ledger that carries the rates does exist, and it demands a force built from the energy density and the current.
  - But the waves `k = (π/2, 0, 0)` and `(0, π/2, 0)` have the same energy density and zero current at every site, and their forces along `e₁` are `0` and not `0`. No requirement built from those two quantities can match the walk at every wave number.
- **T4: the same with two-step moves.** With block 72's two-step momentum the force has the same bond form over two steps, the weight is `cos 2k`, and the obstruction is the same.

In plain terms: in the ray picture a wave's crest spacing falls alike for every wave, but that is not an amount of anything sitting at a place. Any local tally of momentum falls correctly only for long waves; for short waves it falls less, or even rises. The force behind the fall sits on the bonds, not on the sites, so bookkeeping in terms of how much energy sits at each site cannot demand it exactly. For the one-geometry question: the walk and the books agree about falling for long waves only.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk, the clocks and the ledger are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570).
  - `H = Σ_a σ_a S_a` with `S_a = (T_a − T_a†)/(2i)`, symbol `sin k_a`, and `H_w = φHφ` with `φ = √w`, `u = log w`.
  - As landed on main (c3f8c47a58), its translation identity is a finite-power identity on finite-support amplitudes; the evolution identity and the exact packet force are not established there, and its ray model (T4) gives `dk/dt = −E∇u`.
- **Momenta** (blocks 63, 69, 72, 73): `π_j = S_j`, and the two-step `P_j = S_jC_j`, `C_j = (T_j + T_j†)/2`. `p̄(k)` is a momentum's value on the positive band, away from the eight zeros.
- **Densities and force** (block 66, #8597).
  - `χ = Hφψ`, `ρ = Re ψ†χ`, the energy density `𝔢 = φρ`.
  - `f_j(x) = Re[(C_j[d_jφ]ψ)†χ + ψ†C_j[d_jφ]χ](x)`, with `C_j[v]ψ(x) = (v(x)ψ(x + e_j) + v(x − e_j)ψ(x − e_j))/2` and `d_jφ(x) = φ(x + e_j) − φ(x)`.
  - The bond cross energy is `ε_b = ½Re[ψ_y†χ_x + ψ_x†χ_y]`.
- **Ledgers** (blocks 64, 66).
  - Fields `B_a^j` on bonds, with plaquette curls, and the rates as site multipliers.
  - A ledger carries the rates if a relabelling moves `u` with it.
- **Provenance.**
  - `J:derive:the-fall-from-the-ledgers-consistency:a1`, worker `w-macbookpro90c72-j5c0d`. Referee `w-macbookpro90c72-jc358`, a Grok model, confirmed the commutator, the weights and the zero mean.
  - `J:derive:the-ledgers-force-identity-exactly-on-the-lattice:a1`, worker `w-macbookpro90c72-j152a`. Referee `w-macbookpro90c72-jf88c`, a Grok model, confirmed the logarithmic mean, the bond form's pieces, the sublattice counterexample, the upwind cancellation and the first-order no-go; it did not re-run the full torus suite.
  - Both workers are Claude Opus 5.5, the same family as the supervisor.
- **Names.** The `σ_a` are the Pauli matrices.

## Theorem T1 — no local momentum falls with weight one

*Statement.* Let `P` be a finite-reach, translation-invariant operator with `[P, H] = 0`. In a clock with a uniform gradient `φ = 1 + εg·x`, a plane-wave eigenstate of energy `E > 0` has, per site,

`d⟨P⟩/dt = −E ∇u · ∇_k p̄(k) |χ|² + O(ε²)`.

- The weight of the fall along `j` is `∂p̄/∂k_j`.
  - It is `cos k_j` for `π_j` and `cos 2k_j` for `P_j`.
  - It is `(4/3)cos k_j − (1/3)cos 2k_j = 1 − k_j⁴/6 + …` for the fourth-order stencil, which is `−5/3` at `k_j = π`.
- On every line of the zone that avoids the band's zeros, `∫_{−π}^{π} ∂p̄/∂k_j dk_j = 0`.
- So no local momentum commuting with the walk falls with weight one at every wave number. Weight one belongs only to the wave number of block 54's ray model, which is not a local density.

*Proof.*
- `[X_l, T_n] = n_l T_n`, so the symbol of `i[X_l, P]` is `−∂P/∂k_l`.
- At first order, `d⟨P⟩/dt = 2εE⟨ψ|i[φ₁, P]|ψ⟩`.
- Where the band is non-degenerate, `P(k)` has `χ(k)` as an eigenvector, so `⟨χ|∂P|χ⟩ = ∂p̄`.
- `p̄` is periodic, so its derivative has zero mean.
- The runner checks (family B):
  - the commutator, exactly on a nine-site chain;
  - the symbols and their `k`-derivatives, symbolically;
  - the band identity at `sin k = (3/5, 4/5, 0)`, where it is `−28/25`;
  - the weights and their zero means, including a random trigonometric polynomial and `|sin k|`. ∎

## Theorem T2 — the walk's force is a bond energy times a clock difference

*Statement.* For every state `ψ`, every positive rate field and every direction `j`:
- `f_j(x) = d_jφ(x)ε_j(x) + d_jφ(x − e_j)ε_j(x − e_j)`.
- `d_jφ = ½Λ_b d_ju`, with `Λ_b` the logarithmic mean of `φ` over the bond. So `f` is a bond-placed energy times a difference of `u`.
- `ε_b = ½(ρ_x + ρ_y) − ½Re[(d_jψ)_b†(d_jχ)_b]`: the energy density's share plus an exact remainder.
- A state supported on one sublattice has `𝔢 = 0` at every site and a nonzero force. So the force density is no function of the energy density.
- The map `Γ = (−1)^{x₁+x₂+x₃}` anticommutes with `H_w`, and satisfies `𝔢[Γψ] = −𝔢[ψ]` and `f[Γψ] = +f[ψ]`.

*Proof.*
- Expand `C_j[d_jφ]` on the bond and collect the cross terms.
- The logarithmic-mean identity is `φ_y − φ_x = Λ(log φ_y − log φ_x)`.
- A sublattice state has `χ = Hφψ` on the other sublattice, so `ρ = 0`, while the bond term is not zero.
- The runner checks everything exactly with random Gaussian-rational states and rational rate roots on `4³`, `5³` and `6³` tori (family C). ∎

## Theorem T3 — no ledger of the known classes demands the walk's force

*Statement.*
- (a) Every ledger `F = Σ_x w_x D_x(curls)`, with `D` any function of block 64's nine plaquette curls and the rates as site multipliers, obeys `Σ_a[E_a^j(x) − E_a^j(x − e_a)] = 0` exactly, where `E = ∂F/∂B`. The identity has no rate term, so the static equations demand `f = 0`: no fall.
- (b) A ledger that carries the rates exists: the volume member `F = c₀Σ_x w_x det(1 − B(x))`, with the upwind transport `δu_x = −Σ_a ξ_a(x)(1 − w(x − e_a)/w(x))`. At `B = 0` it satisfies its identity exactly, and it demands the force `f_a(x) = 𝔢_x(1 − e^{−(u_x − u_{x−e_a})})`, which is built from the energy density.
- (c) At first order in the rate gradient, every plane wave's force is `f_j = 𝔢 cos k_j (u(x + e_j) − u(x − e_j))/2`. The waves `k = (π/2, 0, 0)` and `(0, π/2, 0)` at energy one have `𝔢 = 2` and zero current at every site, and their forces along `e₁` are `0` and `𝔢(u(x + e₁) − u(x − e₁))/2`.

  A requirement built from `𝔢` and `J`, with coefficients that do not depend on the content, gives them equal forces. So it cannot match the walk's force at every wave number.

*Proof.*
- (a) The curls are exactly unchanged by relabellings `B → B + dξ`. The identity follows, with no rate term, for any `w`.
- (b) Direct substitution at `B = 0`: the two sums cancel.
- (c) By T2 at first order, with the plane waves' exact eigen-spinors.
- The runner checks (family D):
  - (a) for a random linear-plus-quadratic member on `4³`, with the derivative taken exactly;
  - (b) with random displacements;
  - (c) for all 48 plane waves of energy ±1 on `4³`. ∎

## Theorem T4 — reach three: the same obstruction with weight `cos 2k`

*Statement.*
- With the two-step momentum, `i[φ, P_j] = −½C^{(2)}_j[d^{(2)}_jφ]`.
- The force is `½[d^{(2)}_jφ(x)ε^{(2)}(x) + d^{(2)}_jφ(x − 2e_j)ε^{(2)}(x − 2e_j)]`, with `ε^{(2)}` the two-step bond's cross energy.
- At first order its plane-wave form is `𝔢 cos 2k_j (u(x + 2e_j) − u(x − 2e_j))/4`.

*Proof.* As in T2, over the two-step bond. The runner checks the operator identity and the bond form on `5³` and `6³` tori. It checks the first-order form for all 48 plane waves on `8³`, where the two-step difference is not identically zero (family E). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 66 (#8597, landed in c3f8c47a58) and its corrigendum: the fall is owed by the ledger in the continuum only; block 54 as landed withdrew its exact packet force; the one-geometry question of whether everything falls alike on the lattice"
source_of_blocker_text: blocks 54, 66, 69, 72; probes derivations J:derive:the-fall-from-the-ledgers-consistency and J:derive:the-ledgers-force-identity-exactly-on-the-lattice (refereed by another family)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "no local momentum falls with weight one; the force is bond-placed; no ledger of the known classes demands it; next: a ledger with a field that couples to the bond energy, and whether the records' own motion (block 95) falls with weight one"
conditional_surface_status: "T1-T4 exact within blocks 54, 63, 64, 66, 72's clauses (T1 and T3(c) at first order in the rate gradient)"
hypothetical_axiom_status: "the walk, the clocks and the ledger are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Block 54** (#8570; landed in c3f8c47a58 as "Clocked nearest-neighbour amplitudes: finite operator identities and conditional ray motion") gave the walk, a finite-power translation identity and the ray model; the owner's review withdrew the exact force on every packet, with an exact counterexample to its former reading.
- **Block 63** (#8593) gave the one-step momentum and its bond current. **Block 64** (#8595) gave the strains, the curls and the relabellings.
- **Block 66** (#8597; landed in c3f8c47a58 as "Continuum variational stress balance and the clocked walk's distinct exact lattice momentum identity"): the continuum identity, the lattice momentum identity, and the corrigendum incorporated; its lattice force statement is at leading order. T2 here gives the exact lattice form.
- **Blocks 69, 72 and 73** (#8601, #8605, #8606) gave the two-step momentum, the weights `cos q` and `cos 2q`, and the reflected species' failure.
- **The probes unit #8644** found that curl ledgers forbid the fall.
- **New here:**
  - the zero-mean theorem for every local conserved momentum;
  - the exact bond form of the force, and its failure to factor through the energy density;
  - a rate-carrying member, and the equal-content no-go at first order;
  - the reach-three bond form.

## Exact target and obligation graph

Target: what falls with weight one on the lattice, and whether a ledger can demand it. The obligations are:
- (O1) the weight of any local momentum;
- (O2) the exact force;
- (O3) what each class of ledger demands;
- (O4) the two-step case.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- (i) no local momentum commuting with the walk falls with weight one at every wave number;
- (ii) the force is not a function of the energy density;
- (iii) no ledger built from curls, or from a rate transport with a requirement in the energy density and current, demands the walk's force at every wave number.

### N1 — Routes by which the sentences could fail or mislead
1. *Non-local quantities.* In block 54's ray model the wave number falls with weight one. T1 concerns finite-reach operators only; no exact packet statement is made (block 54 as landed withdrew one).
2. *A ledger with a field that couples to the bond energy.* T2's force is a bond energy times a clock difference. A ledger whose requirement reads `ε_b`, rather than `𝔢` and `J`, is not excluded by T3. It would need a new field, and none is constructed here.
3. *Higher orders in the rate gradient.* T1 and T3(c) are first-order statements; the exact bond form (T2) holds at every order.
4. *Long waves.* All weights are `1 + O(k²)`: block 66's continuum statement stands.
5. *Records.* The theorems concern the walk. Whether records moving on their own clocks (block 95) fall with a weight independent of anything is a separate question.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The clauses of blocks 54, 63, 64, 66 and 72 are named and supplied.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 54, 63, 64, 66, 72 | the walk, momenta, ledger, force, two-step momentum | yes |
| blocks 69, 73, #8644 | placement | no |
| probes workers `w-macbookpro90c72-j5c0d`, `w-macbookpro90c72-j152a`; referees `w-macbookpro90c72-jc358`, `w-macbookpro90c72-jf88c` | the results; the confirmations | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no local momentum falls with weight one; the force is bond-placed; no ledger of the known classes demands it" | executed: the shift commutator on a chain; the symbols, weights and zone means of the momenta; the band identity at a rational point | executed: the force density at every site of `4³`, `5³`, `6³` for random Gaussian-rational states and rational rates; a sublattice state; the parity map | executed: all 48 plane waves of energy ±1 at first order in the rate gradient (one step on `4³`, two steps on `8³`) | executed: a random curl member and the volume member with the upwind transport on `4³` | T1 for every finite-reach momentum commuting with the walk; T2 for every state and rate field; T3 for every ledger of the stated classes at first order; blocks 54, 63, 64, 66, 72 supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The weight `cos k` is just the group velocity's lattice artefact." *Reply:* T1 is more than that. No local conserved momentum at all falls with weight one everywhere, since any periodic band value has a slope with zero mean. Weight one belongs only to the ray model's wave number.
- *Objection:* "A cleverer ledger would do it." *Reply:* Possibly, one whose requirement reads the bond energy (N1.2). The note says which classes are excluded and names that route.

### N8 — Cross-cycle echo
- Block 54 gave the walk's ray model, in which the wave number falls with weight one; its exact packet force was withdrawn on review.
- Block 66 found that the books owe it, in the continuum.
- Blocks 69 and 72 found the weights of two momenta.

This note makes the lattice statement general.

## Falsifiers

- A finite-reach momentum commuting with the walk whose weight is identically one on some line of the zone avoiding the band's zeros.
- A state and rate field where `f_j` differs from the bond form.
- A ledger requirement built from `𝔢` and `J` that gives the two stated plane waves different forces.

## Boundaries and non-claims

- The walk, the clocks and the ledgers are supplied, not adopted.
- T1 and T3(c) are first-order statements in the rate gradient.
- No statement is made about records' fall, about a ledger that reads bond energies, or about gravity.

## Imports

- `minimal_axioms`. Blocks 54, 63, 64, 66, 69, 72, 73 and #8644, restated or placed.
- Named standard imports, at definition level:
  - the Pauli matrices;
  - Gaussian-rational and symbolic arithmetic;
  - the logarithmic mean.

## Review record

- **Who and when.** Supervisor-run block, the fifty-fourth since the source-link direction opened, built from probes workers' results with other-family referees.
- **Provenance.**
  - Workers `w-macbookpro90c72-j5c0d` and `w-macbookpro90c72-j152a` are Claude Opus 5.5.
  - Referees `w-macbookpro90c72-jc358` and `w-macbookpro90c72-jf88c` are Grok models.
  - The supervisor ported the exact checks, with the arithmetic machinery kept verbatim. It moved the two-step plane-wave check to `8³`, where it is not vacuous: on `4³` the two-step difference vanishes identically, and the mutation census exposed that.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
