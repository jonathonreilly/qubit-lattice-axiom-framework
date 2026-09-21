---
claim_id: admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 63, 64, 66, 69 and 70 (open PRs #8570, #8593, #8595, #8597, #8601, #8602; not adopted): the clocked walk H_w = phi H phi; block 66: a field energy counted per local tick and blind to relabellings obeys an identity which, with the field equations, REQUIRES of the content that its stress gradient equal its weight (at lowest order: the divergence of the response to the strain equals the energy density times the gradient of u); for the relabelling generated with S_j (reach two) the walk's exact law is d<G>/dt = sum (d xi) J[phi psi] - sum xi f, and f = e du at leading order for a SMOOTH amplitude - the first species. (T1) For the relabelling generated with the two-step momentum P_j = S_j C_j (block 69, reach three), exactly and for every state, rate field and displacement: i[phi, P_j] = -(1/2) C2_j[d2_j phi], a hop over two steps weighted by the change of phi over them; i[H_w, G] = phi (i[H, G]) phi - (Lam H phi + phi H Lam); d<G>/dt = sum (d xi) K[phi psi] - sum xi fP with the two-step force density fP; on stationary states div K[phi psi] = -fP at every site. (T2) Under block 70's maps, for every state and rate field: e[V_n psi] = s_n e[psi]; f_j[V_n psi] = s_n D_j f_j[psi]; fP_j[V_n psi] = s_n fP_j[psi]. Per unit of energy density, the reach-two force density of a species reflected along j has the opposite sign; the reach-three one is the same for all eight. (T3) At leading order for smooth envelopes and rates: f_j = D_j e d_j u for species n and fP_j = e d_j u for every species. Hence block 66's requirement is met by all eight species under reach three; under reach two it is met only by species not reflected along any direction in which the rates vary, and for a reflected species the content's stress gradient is MINUS its weight - twice the weight is left unbalanced, and by block 66 T1 the strains' equations then have no solution at that order. EXECUTED, NOT CLAIMED: packets at wave number pi n + q in a smooth rate field: reach two F/W = +0.980, -0.980 (n = 0, 1; q = 0.2), reach three +0.921, +0.921; the lattice factors are cos q and cos 2q, so the three-step rule meets the requirement with four times the relative correction; site by site on a 5x6x7 torus div K + fP = 0 to 3e-17 on eigenvectors of H_w. NOT claimed: which coupling is supplied; which species are present; an exact lattice form of the field's identity (block 66: there is none here); anything beyond the leading order; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_which_species_fall_the_ledger_owes_reach_two_against_reach_three_2026_09_21.py
---

# Which species' fall the ledger owes: under reach two a reflected species has minus its weight; under reach three all eight agree

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about block 54's supplied walk in a rate field and the two supplied relabellings; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks and for a field energy counted per local tick and blind to relabellings; it reports for which of the walk's species the requirement that such a ledger places on its content is met, under the relabellings of reach two and of reach three; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 66 (open PR #8597) showed that a ledger whose field energy is counted per local tick and is blind to relabellings *requires* something of its content: the content's stress gradient must equal its weight. It then showed that the walk delivers exactly that — for a smooth amplitude, which is to say for the first of the walk's eight species, with the relabelling generated with the one-step momentum (reach two). Blocks 68–70 (open PRs #8599, #8601, #8602) have since found the other seven species, a relabelling of reach three, and the exact maps between species. This note puts the question again for all eight and for both relabellings.

1. **The walk's law for the three-step rule, exactly** (T1). Block 66 T3 carries over with the two-step momentum: the rate field leaves of it a hop over *two* steps weighted by the change of the rate's root over those two steps, and the force density is built from that hop.
2. **The species, exactly** (T2). Under the exchange maps the energy density picks up the species' sense `s_n`. The reach-two force density picks up `s_nD_j`; the reach-three one picks up `s_n` only. So *per unit of energy density* the reach-two force on a species reflected along `j` has the opposite sign, and the reach-three force is the same for all.
3. **What the ledger's requirement becomes** (T3). Under reach three it is met by all eight species. Under reach two it is met by the species the relabelling was written for, and for a species reflected along the gradient the content's stress gradient is **minus** its weight. Twice the weight is left over, and block 66's identity then leaves the strains' equations without a solution.

Executed: force over weight for packets of two species, `+0.980, −0.980` under reach two and `+0.921, +0.921` under reach three. The price of reach three is visible in the same numbers: its lattice factor is `cos 2q` where reach two's is `cos q`.

In plain terms: block 66 found that the books force the walker to fall. That was checked for one kind of walker. For the kinds that the lattice's one-step momentum reads backwards, the two-step rule's books demand a fall with the wrong sign — those kinds cannot sit in balance with such a field at all. The three-step rule's books demand the same fall of all eight kinds. Block 68 had the two-step rule showing the kinds different geometries; here it is inconsistent with them.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 (PR #8601) queue item 4: 'does block 66's force identity keep its form with P_j?'; block 66 T4 was proved for a smooth amplitude (the first species) only."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the ladder of reach gains a consistency rung: reach two is consistent with a per-tick relabelling-blind ledger only for unreflected species; reach three for all eight; next: the same comparison for the frame (reach one) beyond block 62's defect; the kinetic terms; the owner's forks on reach and on the species"
conditional_surface_status: "T1, T2 exact for every state, rate field and displacement (tori with sides of at least five for the two-step momentum, even sides for the maps); T3 at leading order for smooth envelopes and rates, with block 66 T1, T2 restated"
hypothetical_axiom_status: "block 54's clocked walk; the relabellings of blocks 63 and 69; block 66's ledger; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 63, 64, 66, 69, 70 (open PRs) supply the objects.

- **Clocked walk.** `H_w = φHφ`, `u = 2 log φ`; energy density `𝔢_x = Re ψ†_x(H_wψ)_x`.
- **Block 66, restated.** Field's identity (T1 there): for `F = ∫e^uD(e)`, `E_j^a∂_be^j_a − ∂_a(E_j^ae^j_b) + U∂_bu = 0`. With the field equations `𝔢 + U = 0`, `𝒥 + E = 0`: `∂_a𝒥_b^a = 𝔢∂_bu` at lowest order (T2 there). The identity concerns the field's energy alone and does not know with which momentum the content's coupling was generated. For the walk, `𝒥 = −J` (reach two) or `−K` (reach three), and by the exact laws below the requirement reads **`f = 𝔢 du`**, respectively `f^P = 𝔢 du`.
- **Reach two** (block 66 T3). `i[φ, S_j] = −C_j[d_jφ]`; `f_j = Re[(C_j[d_jφ]ψ)†Hφψ + ψ†C_j[d_jφ]Hφψ]`.
- **Reach three.** `P_j = S_jC_j`; `G = ½Σ_j{ξ_j, P_j}`; `d^{(2)}_jφ(x) = φ(x + 2e_j) − φ(x)`; `C^{(2)}_j[v]ψ(x) = ½[v(x)ψ(x + 2e_j) + v(x − 2e_j)ψ(x − 2e_j)]`; `Λ = ½Σ_j{ξ_j, ½C^{(2)}_j[d^{(2)}_jφ]}`; `f^P_j = Re[(½C^{(2)}_j[d^{(2)}_jφ]ψ)†Hφψ + ψ†½C^{(2)}_j[d^{(2)}_jφ]Hφψ]`; `K` of block 69.
- **Maps.** `V_n`, `s_n`, `D_n` of block 70.

That an invariance of a field's energy under relabellings gives an identity among its field equations is Noether's second theorem; nothing is used as authority.

## Prior art and what is new

New, inside the framework's vocabulary: block 66's exact law for the relabelling of reach three; the exact behaviour of both force densities under the species-exchange maps; and the consequence that the requirement a per-tick, relabelling-blind ledger places on its content fails with the opposite sign for reflected species under reach two, and holds for all eight under reach three. No gravitational claim is made.

## Exact target and obligation graph

Target: for which species the ledger's requirement is met, under each relabelling. Obligations: (O1) the exact law with the two-step momentum; (O2) the species; (O3) the requirement. T1–T3 discharge them.

## Theorem T1 — the walk's law for the two-step relabelling, exactly

*Statement.* For every state, rate field and real displacement `ξ`: (a) `i[φ, P_j] = −½C^{(2)}_j[d^{(2)}_jφ]`; (b) `i[H_w, G] = φ(i[H, G])φ − (ΛHφ + φHΛ)`; (c) `d⟨G⟩/dt = Σ_{a,j,x}(d_aξ_j)(x)K_a^j[φψ](x → x + e_a) − Σ_{j,x}ξ_j(x)f^P_j(x)`; (d) if `ψ` is stationary for `H_w`, the lattice divergence of `K^j[φψ]` equals `−f^P_j` at every site; (e) for uniform `ξ` the total two-step momentum changes at minus the total force.

*Proof.* (a) `[φ, P_j]ψ(x) = (1/(4i))[(φ(x) − φ(x + 2e_j))ψ(x + 2e_j) − (φ(x) − φ(x − 2e_j))ψ(x − 2e_j)]`, and `φ(x) − φ(x − 2e_j) = d^{(2)}_jφ(x − 2e_j)`. (b)–(e) as block 66 T3, with block 69 T3 for the bare term. ∎

## Theorem T2 — the species

*Statement.* For every state, every positive rate field, every species `n` and `j = 1, 2, 3`, at every site: `𝔢[V_nψ] = s_n𝔢[ψ]`; `f_j[V_nψ] = s_nD_jf_j[ψ]`; `f^P_j[V_nψ] = s_nf^P_j[ψ]`.

*Proof.* Block 70 T1(a): `C_j[v]V_n = D_jV_nC_j[v]`, `C^{(2)}_j[v]V_n = V_nC^{(2)}_j[v]` (two steps), `HφV_n = s_nV_nHφ`; `V_n` is unitary site by site, so it drops out of each bilinear. ∎

## Theorem T3 — what the ledger's requirement becomes

*Statement.* At leading order for smooth rates and an amplitude `V_n ×` (smooth): (a) `f_j = D_j𝔢 d_ju`; (b) `f^P_j = 𝔢 d_ju`. Hence: under reach three block 66's requirement is met by every species; under reach two it is met iff `D_j = 1` for every `j` along which `𝔢 d_ju ≠ 0`, and for a species reflected along such a `j` the remainder is `2𝔢 d_ju`, so that, by block 66 T1, the field equations of the ledger have no solution at that order with that content.

*Proof.* For a smooth amplitude `C_j[d_jφ] → hφ'` and `½C^{(2)}_j[d^{(2)}_jφ] → ½ · 2hφ' = hφ'`, so `f, f^P → 2hφ' Re ψ†Hφψ = 𝔢 du` (block 66 T4 and its two-step form; runner D1). For species `n` apply T2: `f_j[V_nψ] = s_nD_j𝔢[ψ]d_ju = D_j𝔢[V_nψ]d_ju`, and `f^P_j[V_nψ] = 𝔢[V_nψ]d_ju`. If the field equations held, block 66 T1 would give `f = 𝔢 du`. ∎

Both agreements are at leading order: for a packet at wave number `πn + q` the factors are `cos q` (reach two, first species) and `cos 2q` (reach three) — executed below.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block72_species_fall.py`. **W1** (dense matrices, `5×6×7` torus, random rate field, ten eigenvectors of `H_w`): `|div J[φψ] + f| ≤ 6e-17` and `|div K[φψ] + f^P| ≤ 3e-17` at every site (`|f^P|` up to `3e-3`). **W2** (ring of 2048 sites, `u = 0.2 sin(2πx/N)`, packets of width 60 at the steepest point, wave number `πn + q`; `F`, `F^P` the total forces and `W = Σ𝔢(u(x + 1) − u(x))`): `q = 0.2`: `F/W = +0.9800` (`n = 0`), `−0.9800` (`n = 1`); `F^P/W = +0.9207` for both; `q = 0.5`: `±0.8775`; `+0.5400`; `q = 0.9`: `±0.6215`; `−0.2273` for both — equal to `cos k` and `cos 2k` to three digits. **W3**: the same ratios site by site vary by less than `0.001` across the packet.

## No-Go Discipline Gate

The note's negative sentence: under reach two the ledger's requirement is not met by a species reflected along a direction in which the rates vary.

### N1 — Routes by which the sentence could fail or mislead
1. *A field energy that is not blind to relabellings.* Block 66 T1 then does not hold and nothing is required.
2. *Only unreflected species present.* Then nothing fails; which species are present is the owner's.
3. *Rates uniform along every reflected direction.* Then `𝔢 d_ju = 0` there.
4. *A mixture.* The requirement is on the total content; a mixture of species fails it by `2Σ_{reflected}𝔢 d_ju`, which vanishes only by cancellation between amplitudes of opposite energy density.
5. *Beyond leading order.* Neither relabelling meets the requirement exactly on the lattice (block 66: the field's identity has no exact lattice form here); the failure for reflected species is of order one, not a lattice correction.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Smooth rates and envelopes in T3; uniform frame (the strains enter at lowest order only through block 66's restated identity); tori with even sides for the maps and sides of at least five for the two-step momentum.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra | yes (premise) |
| block 66 (open PR #8597) | the field's identity and the requirement; the reach-two law (re-used machinery) | yes (restated) |
| blocks 63, 69 (open PRs #8593, #8601) | the two relabellings and their currents | yes (restated) |
| block 70 (open PR #8602) | the exchange maps | yes (restated; re-verified in C1, C2) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the two-step law; the species' signs; the requirement met under reach three and failing for reflected species under reach two" | executed: `i[φ, P_j]` against the two-step hop at all 150 sites | executed: the operator identity at all 150 sites; force and energy densities of `V_nψ` against `ψ` at all 216 sites, all eight species | executed: leading order of `f`, `f^P`, `𝔢 du` for smooth and staggered amplitudes (exact symbolic expansion) | executed: `d⟨G⟩/dt` against current and force terms; total momentum against total force | T1, T2 identities for every state, rate field, displacement; T3 leading order; which coupling and which species not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A continuum identity is being compared with a lattice law." Reply: as in block 66, and N1.5 says so; the point is a sign of order one. Second objection: "The reflected species' lattice momentum is simply minus its own wave number; nothing physical fails — it falls like the others." Reply: it does fall like the others (block 68 T1; block 71 T2). What fails is the *field's* side: the strain coupled through `S_j` is sourced by a current whose divergence, for that species, is minus what the field's identity allows. The species is fine; the reach-two ledger cannot hold it. Third objection: "Reach three's correction is four times larger." Reply: reported, with numbers.

### N8 — Cross-cycle echo
Block 66: the fall is owed by the ledger — for the first species. Block 68: reach two shows the species different geometries. Block 70: reach two alone breaks the energy reversal. Here: reach two's ledger cannot hold reflected species at all. Each block has taken something more from the middle rung of block 69's ladder.

## Falsifiers

- A state, rate field and species with `f_j[V_nψ] ≠ s_nD_jf_j[ψ]` or `f^P_j[V_nψ] ≠ s_nf^P_j[ψ]` at some site.
- A smooth-envelope amplitude of a reflected species whose reach-two force density equals plus its energy density times the gradient at leading order.
- A stationary state of `H_w` with `div K[φψ] ≠ −f^P` at some site.

## Boundaries and non-claims

The coupling is not chosen and no species is declared present or absent. The field's side is block 66's, restated, at lowest order in the strains. Kinetic terms, varying frames, the blind walk and records are outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, the memo's silence on amplitude dynamics. Blocks 54, 63, 64, 66, 69, 70 (PRs #8570, #8593, #8595, #8597, #8601, #8602, open): restated or placed.
- Named standard imports at definition level: commutators with shifts; expansion in the lattice spacing; identities among field equations from an invariance (Noether's second theorem), as restated from block 66.
- Reference only: Noether.

## Review record
Supervisor-run block, the twentieth of the source-link direction and the sixteenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: nothing new is supplied; the note must not turn a consistency failure of one supplied coupling into a recommendation of another — it reports what each ledger can hold. A rigour lens: block 66's note was re-read (T1–T4, statements and proofs) before writing, in particular that T4 is for a smooth amplitude and that `𝒥 = −J`; the species' signs are proved as exact identities for every state and only then combined with the leading-order statement; the symbolic expansion was run for the staggered amplitude directly as well, so T3(a) does not rest on the map alone; the control measures force over weight for packets, where the sign and both lattice factors are seen. A strategy lens: block 69's ladder had reach two as a viable rung with a price; blocks 70 and 72 show that, with reflected species present, it is not viable under block 66's ledger. Control: as reported under Executed. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_which_species_fall_the_ledger_owes_reach_two_against_reach_three_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
