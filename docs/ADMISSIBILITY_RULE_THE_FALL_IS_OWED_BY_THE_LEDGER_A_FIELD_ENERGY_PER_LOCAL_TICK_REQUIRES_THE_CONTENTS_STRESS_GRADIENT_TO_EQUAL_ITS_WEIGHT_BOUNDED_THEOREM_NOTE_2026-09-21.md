---
claim_id: admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 55, 60, 63 and 64 (open PRs #8570, #8571, #8590, #8593, #8595; not adopted): block 54's walk timed by site rates, H_w = phi H phi with phi = sqrt(w), u = log w; block 55's energy density e = Re psi^dagger H_w psi as the source of the rates; block 60's ledger linear in the rates, F = sum_x w_x D_x; block 63's relabelling G_xi and bond current J; block 64's family of densities D built from the curls of a frame e = 1 + strain. (T1; continuum, exact symbolic algebra) for F = int exp(u) D(e) with D any member of block 64's family, the variational derivatives E_j^a = dF/de^j_a and U = dF/du satisfy E_j^a d_b e^j_a - d_a(E_j^a e^j_b) + U d_b u = 0 identically: it is the statement that F does not change when the sites are relabelled and the rates are carried along; checked through second order in nine strain functions and the log rate (the order at which the fall first appears) for the blind member and, in the runner and in the refuting pass, for two members that see the coin axes and have a volume term; without the rates' term the expression does not vanish. (T2; the fall is owed) with the rates' constraint U = -e and the strains' equations E = -(the content's response to the frame), any content coupled through such a ledger MUST satisfy d_a(J_j^a e^j_b) - J_j^a d_b e^j_a = e d_b u: at lowest order the divergence of its stress equals its energy density times the gradient of the log rate, its weight. The quantity that sources the rates is the quantity that is pulled: block 55's matched pulls and block 54's force = energy x gradient are one condition, and a content with no stress gradient cannot be static. (T3; the walk's own law, exact on the lattice, every state) i[phi, S_j] = -C_j[d_j phi]; i[H_w, G_xi] = phi (i[H, G_xi]) phi - (Lam H phi + phi H Lam), Lam = (1/2) sum_j {xi_j, C_j[d_j phi]}; hence d<G_xi>/dt = sum over bonds (d_a xi_j) J_a^j[phi psi] - sum_x xi_j(x) f_j(x) with the force density f_j(x) = Re[(C_j[d_j phi] psi)^dagger H phi psi + psi^dagger C_j[d_j phi] H phi psi](x); on stationary states the divergence of the bond current of phi psi equals minus the force density at every site. (T4) At leading order in the lattice spacing f_j = e d_j u: the walk's law has the form T2 requires. EXECUTED, NOT CLAIMED: a packet of the clocked walk in a rate well: the rate of change of its lattice momentum equals minus the total force to five digits at every sampled time, and the total force is 0.89 to 0.93 of the total weight, the cosine of its wave number; stationary states of H_w on a 6x5x4 torus with a smooth rate field: divergence of the bond current plus force density below 1e-16 at every site with force densities of 5e-3. NOT claimed: an exact lattice form of T1 (the lattice keeps relabelling-blindness of the curls exactly, block 64 T1, but a relabelling makes a weighted hop of a rate, not a rate); agreement of the two sides beyond leading order in the wave vector; the ledger's form; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_2026_09_21.py
---

# The fall is owed by the ledger: a field energy per local tick requires the content's stress gradient to equal its weight

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (an exact continuum identity of block 60's and 64's supplied ledger, and exact lattice identities of block 54's supplied clocked walk; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a ledger linear in the rates built from the strains of a frame; it reports an identity of such a ledger and the exact momentum balance of the clocked walk, and that the two agree; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The direction began with three supplied clauses. Clause B — the phase keeps local time — gave the law of fall: force = energy × gradient, exactly (block 54, open PR #8570). Clause C — the books balance — gave the source: what slows the clocks is energy, and pulls are matched iff each body sources in proportion to what is pulled (block 55, open PR #8571). Blocks 60 to 64 then built the field's side: an energy counted per local tick, from the strains of a frame, blind to relabellings. This note asks whether, once that field energy is there, the law of fall is still a separate clause.

1. **The field's identity.** Any field energy of the form `Σ_x w_x D_x`, with `D` built from the frame so that it does not care how the sites are labelled, obeys an identity: the divergence of the strains' field equations equals the rates' field equation times the gradient of the log rate. It holds for every member of block 64's family — it comes from the counting per tick and the blindness to relabellings, not from the curvature (T1).
2. **What it demands of the content.** Put in the field equations: the rates' one says "energy density", the strains' one says "stress". The identity then *requires* the content's stress gradient to equal its energy density times the gradient of the log rate — its weight. What sources the clocks is what is pulled; a content without a stress gradient cannot sit still (T2).
3. **What the walk does, exactly.** On the lattice a relabelling does not turn a rate into a rate but into a weighted hop. With that, the clocked walk has an exact momentum balance for every state: the change of its momentum is the divergence of its bond current *minus a force density*, given in closed form; for anything stationary the two cancel at every site (T3).
4. **They agree.** At leading order that force density is the energy density times the gradient of the log rate. The walk falls exactly as the ledger needs it to (T4).

In plain terms: once the field's energy is counted per tick of each local clock and does not care about labels, the field equations can only be solved if whatever feeds the clocks also feels their gradient as a weight, in exactly that proportion. The walker does — that is block 54's law of fall and block 55's matching of pulls, which now appear as *one* condition that the ledger imposes rather than two things supplied. Things fall because otherwise the books could not be balanced.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record (PR #8572), third addendum, 'What is still open': 'the fall of block 54 as a consequence of the ledger's consistency at the next order'; ai/probes task 'the-fall-from-the-ledgers-consistency'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an exact lattice form of the field's identity (what replaces 'the rates are carried along' when a relabelling makes a weighted hop of a rate); the agreement of the two sides at the next order in the wave vector; whether clause B can be dropped from the decision record's list in favour of the ledger plus 'the content is timed by the rates it sources'"
conditional_surface_status: "T1 exact for every frame and rate field (an invariance statement), checked through second order in the fields; T2 follows from T1 for every content coupled through a ledger of this kind; T3 exact for every state, rate field and displacement on every torus and on the infinite lattice; T4 exact at leading order in the lattice spacing"
hypothetical_axiom_status: "blocks 54, 55, 60, 63, 64's clauses; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 55, 60, 63, 64 (open PRs) supply everything else.

- **Clocked walk.** `H_w = φHφ`, `H = Σ_a σ_a S_a`, `φ = √w`, `u = log w`. **Energy density** `𝔢(x) = Re ψ†(x)(H_wψ)(x) = ∂⟨H_w⟩/∂u_x` (block 55).
- **Relabelling** `G_ξ = ½Σ_j{ξ_j, S_j}`; **bond current** `J_a^j[χ]` of a state `χ` (block 63); **symmetric hop** `C_j[v]` weighted by a bond function `v`; `d_jφ = φ(x + e_j) − φ(x)`.
- **Carried rate** `Λ_ξ = ½Σ_j{ξ_j, C_j[d_jφ]}`. **Force density** `f_j(x) = Re[(C_j[d_jφ]ψ)†(Hφψ) + ψ† C_j[d_jφ](Hφψ)](x)`.
- **Ledger** `F = ∫ e^{u} D(e)`, `D` a member of block 64's family for the frame `e = 1 +` strain; `E_j^a = δF/δe^j_a`, `U = δF/δu`. **Content's response** `𝒥_j^a = ∂⟨H⟩/∂e^j_a`; to first order it is minus block 63's bond current.

That the invariance of a field's energy under relabellings gives an identity among its field equations, and that with the rate of clocks as a multiplier this identity ties the divergence of the spatial equations to the constraint times the gradient of the rate, is Noether's second theorem applied to the formulation of Arnowitt, Deser and Misner; that the equations of motion of the content then follow from the field equations is the observation of Einstein and Grommer and of Infeld and Hoffmann. The balance of a stress gradient against weight is the hydrostatic equation. None is used as authority.

## Prior art and what is new

Classical in kind. New, inside the framework's vocabulary: that the decision record's clauses B (the fall) and C with block 55's matched pulls (the source) are *not independent* once the field's energy is counted per local tick and is blind to relabellings — the ledger's identity requires the pulled quantity to be the sourcing quantity, in the form of a stress gradient equal to the weight; that this holds for every member of block 64's family, so it does not depend on the blindness to the coin's axes; and the exact lattice momentum balance of the clocked walk, with its force density in closed form, which has the required form at leading order. No gravitational claim is made.

## Exact target and obligation graph

Target: whether the law of fall is a separate clause next to a ledger linear in the rates. Obligations: (O1) the ledger's identity; (O2) what it requires of any content; (O3) the walk's exact momentum balance; (O4) their agreement. T1–T4 discharge them.

## Theorem T1 — the field's identity

*Statement.* Let `F = ∫ e^{u} D(e)` with `D` a member of block 64's family. Then for `b = 1, 2, 3`: `E_j^a ∂_b e^j_a − ∂_a(E_j^a e^j_b) + U ∂_b u = 0`, identically in `e` and `u`.

*Proof.* Each term of `D` is a scalar density under `x → x + ξ(x)`: the coin index is inert, the bond indices are contracted with the frame and its inverse, `det e` is a density, and `∂_b(det e V^b)` is the divergence of a vector density. `e^u` is a scalar if `u` is carried along. So `F` is unchanged under `δe^j_a = ξ^b∂_be^j_a + e^j_b∂_aξ^b`, `δu = ξ^b∂_bu`; inserting these variations and integrating by parts gives the identity, `ξ` being arbitrary. The runner checks it through second order in the fields for three members (C1 and the refuting pass), and that the expression without `U∂_bu` does not vanish. ∎

## Theorem T2 — the fall is owed

*Statement.* Let a content with energy `⟨H⟩[e, u]` be coupled through the ledger `⟨H⟩ + F`, stationary in `u` and in `e`: `𝔢 + U = 0`, `𝒥_j^a + E_j^a = 0`. Then `∂_a(𝒥_j^a e^j_b) − 𝒥_j^a ∂_b e^j_a = 𝔢 ∂_b u`. At lowest order in the fields, `∂_a 𝒥_b^a = 𝔢 ∂_b u`.

*Proof.* Substitute into T1. ∎

Three readings. (i) *Static content* has a stress whose divergence balances its weight, site by site. (ii) *Content with no stress gradient* — a slow free body — cannot be static in a rate gradient: its momentum must change at minus its energy times the gradient, which is block 54's law. (iii) *The source is what is pulled.* The `𝔢` on the right is the same function that stands in the rates' equation. A content that sourced the rates by one density and were pulled through another (block 55 T2(b), T3) would leave the strains' equations without a solution: block 55's matched pulls are the ledger's consistency condition.

## Theorem T3 — the walk's own law, exactly

*Statement.* For every state, rate field and real displacement `ξ`: (a) `i[φ, S_j] = −C_j[d_jφ]`; (b) `i[H_w, G_ξ] = φ(i[H, G_ξ])φ − (Λ_ξ Hφ + φH Λ_ξ)`; (c) `d⟨G_ξ⟩/dt = Σ_{a,j,x}(d_aξ_j)(x) J_a^j[φψ](x → x + e_a) − Σ_{j,x} ξ_j(x) f_j(x)`; (d) if `ψ` is stationary for `H_w`, `Σ_a[J_a^j[φψ](x → x + e_a) − J_a^j[φψ](x − e_a → x)] = −f_j(x)` at every site; (e) for uniform `ξ`, the total lattice momentum changes at minus the total force.

*Proof.* (a) As in block 65 T1: `[φ, S_j]ψ(x) = (1/(2i))[(φ(x) − φ(x + e_j))ψ(x + e_j) − (φ(x) − φ(x − e_j))ψ(x − e_j)]`. (b) `[φHφ, G] = φ[H, G]φ + [φ, G]Hφ + φH[φ, G]` and `i[φ, G_ξ] = ½Σ_j{ξ_j, i[φ, S_j]} = −Λ_ξ`. (c) The first term is block 63 T2(b) for the state `φψ`; the second is `−2 Re⟨Λ_ξψ|Hφψ⟩`, and `Λ_ξ` is hermitian with real weights, which gives `f`. (d) `⟨ψ|[H_w, G]|ψ⟩ = 0`; summation by parts. (e) `dξ = 0`. ∎

A relabelling carries the rates along, as T1 assumes — but on the lattice what it makes of a rate is not a rate: it is the hop `Λ_ξ`. That is why T1 has no exact lattice form here, while T3 is exact.

## Theorem T4 — they agree

*Statement.* On a line with lattice spacing `h`, for smooth `φ` and a smooth complex amplitude, `f = 𝔢 · (u(x + h) − u(x))` at the leading order in `h` (both sides begin at order `h²`). Hence, by T3(d), stationary states of the clocked walk have a bond current whose divergence is minus their weight at leading order, which with `𝒥 = −J` is T2's requirement.

*Proof.* Expansion (runner D1): `C_j[d_jφ] → hφ'`, so `f → 2hφ' Re ψ†Hφψ = h(2φ'/φ)𝔢`. ∎

For a plane wave of wave number `k` the exact `f` carries a factor `cos k`: the momentum in T3 is the lattice's `sin k`, whose rate of change is `cos k` times that of `k`. Block 54's statement that the wave number falls at minus energy times gradient in every state is the same fact.

## Executed (supervisor control and refuting pass; evidence, not proof)

`specs/supervisor_control_block66_refuter.py`. W1: T3(a), (b) on a random complex state with a random positive rate field, `6 × 5 × 4` torus: `5×10⁻¹⁶`, `2×10⁻¹⁵`. W2: a packet of the clocked walk on a ring of 256 in a rate well (depth 0.3, width 40), wave number 0.35: the rate of change of `⟨S⟩` by finite differences of an accurate evolution equals minus the total force to five digits at five times (`1.652293×10⁻³` against `1.652372×10⁻³` at `t = 10`), and the total force is `0.926, 0.919, 0.910, 0.901, 0.889` of the total weight as the packet speeds up (`cos 0.35 = 0.939`). W3: stationary states of `H_w` on a `6 × 5 × 4` torus with a smooth rate field, by dense diagonalisation: `|div J[φψ] + f| < 10⁻¹⁶` at every site, with force densities up to `5×10⁻³` (the weight there is up to `9×10⁻³`; the wave numbers on so small a torus are not small). The first version of W3, on a ring, was empty: a non-degenerate stationary state of `i ×` (real antisymmetric) carries no momentum current and feels no force density, so it reported `0 = 0`. W4: the ledger's identity for a third member, `(c_0, …, c_4) = (−2/5, 3, 1/7, −5/3, 1/2)`: holds; without the rates' term: does not.

## No-Go Discipline Gate

The note's negative sentences: without the rates' term the identity fails; in a rate field the clocked walk's momentum is not conserved; a content with no stress gradient cannot be static; T1 has no exact lattice form here.

### N1 — Routes by which the sentences could fail
1. *A field energy not linear in the rates.* Blocks 55 and 56's ledgers are functions of the rates alone; they have no strains whose equations could be inconsistent, and the matching of pulls had to be argued separately (block 55 T3). T2 is a statement about ledgers of block 60's kind.
2. *A content that is not timed by the rates it sources.* T2 says such a content cannot be coupled consistently. It does not say that clocked content exists; clause B supplies it.
3. *The lattice.* The two sides agree at leading order in the wave vector. Beyond that the field's side has no unique lattice form (block 64 N1.3) and the content's side has the hop `Λ_ξ` in place of a carried rate; whether some lattice ledger has T3's exact force density on its right-hand side is the named next step.
4. *Non-static situations.* T2 is a statement about the static equations. With kinetic terms for the strains the identity acquires their momenta; not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T1 continuum; checked through second order in the fields. T2 static. T3 identity frame for the walk's coin, arbitrary positive rates. T4 one dimension, one coin component, leading order; the three-dimensional statement is the same computation along each axis.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Qubit axiom's one-site algebra; the absences that motivate the clauses | yes (premise) |
| block 54 (open PR #8570) | the clocked walk; force = energy × gradient | yes (restated) |
| block 55 (open PR #8571) | the energy density as the source; matched pulls | yes (restated) |
| blocks 60, 64 (open PRs #8590, #8595) | the ledger linear in the rates; the family of densities | yes (restated) |
| block 63 (open PR #8593) | the relabelling, the bond current | yes (restated) |
| block 65 (open PR #8596) | the commutator of a site function with `S_j` | restated |
| decision record (open PR #8572) | clauses B and C; the open item | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the ledger's identity; the content's stress gradient must equal its weight; the clocked walk's exact momentum balance and force density; agreement at leading order" | executed: `i[φ, S_j]` at all 60 sites of a `5×4×3` torus | executed: `i[H_w, G_ξ]` against its decomposition at all 60 sites; the force density site by site | executed: the identity through second order in nine strain functions and the log rate for two members | executed: `d⟨G_ξ⟩/dt` against current term minus force term; total momentum against total force; force density against weight at leading order in the lattice spacing | T1 every frame and rate field; T2 every content coupled through such a ledger; T3 every state, rate field and displacement; T4 leading order; the ledger, the strains, the relabellings and the clocked walk supplied; no exact lattice form of T1 |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The contracted identity implies the equations of motion; this has been known since 1927." Reply: yes, under the Premises. For the owner the content is about the *list of supplied clauses*: the record has B (fall) and C with matched pulls (source) as separate items; with a ledger linear in the rates they are one consistency condition. Second objection: "You still need clause B to have clocked content at all." Reply: correct, and N1.2 says so: T2 forbids inconsistent content, it does not manufacture consistent content. What changes is the status of the force law — from supplied to required. Third objection: "Leading order only." Reply: T3 is exact and T1 is exact; their comparison is at leading order because the field's side has no unique lattice form yet. That is stated, and it is the next step.

### N8 — Cross-cycle echo
Block 54: force = energy × gradient, exactly, in every state. Block 55: pulls are matched iff the source is proportional to what is pulled; the ledger fixes the source. Block 60: rates as multipliers. Block 63: a relabelling generates the bond current. Block 64: the field equations of any function of the curls are divergence-free. Here: with rates, "divergence-free" becomes "divergence equals weight" on both sides.

## Falsifiers

- A member of block 64's family, a frame and a rate field violating T1 at second order.
- A state, rate field and displacement violating T3(b) or (c); a stationary state of `H_w` with `div J[φψ] + f ≠ 0` at some site.
- A smooth amplitude and rate field with `f ≠ 𝔢 du` at leading order in the lattice spacing.

## Boundaries and non-claims

The ledger's form, the strains, the relabellings and the clocked walk are supplied. T1 is a continuum identity; no exact lattice form is given, and the agreement with T3 is at leading order in the wave vector. T2 is static. Nothing here derives clause B: it changes the status of the force law from supplied to required, given the ledger. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the Qubit axiom's one-site algebra, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 55, 60, 63, 64, 65 and the decision record (PRs #8570, #8571, #8590, #8593, #8595, #8596, #8572, open): restated or placed.
- Named standard imports at definition level: invariance of an integral of a scalar density under a change of coordinates; variational derivatives with second derivatives; commutators with shifts; summation by parts; expansions in a lattice spacing.
- Reference only: Noether; Arnowitt, Deser and Misner; Einstein and Grommer; Infeld and Hoffmann.

## Review record
Supervisor-run block, the fourteenth of the source-link direction and the tenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: nothing new is supplied; the note must not say that clause B is *derived* — T2 forbids inconsistent content and does not produce clocked content — and must say exactly which ledgers it concerns (linear in the rates, with strains). A rigour lens: the supervisor first thought the inconsistency would show at first order in the fields; counting orders (the content's energy is itself of first order, since it sources first-order fields) puts the fall at second order in the field equations, third order of the ledger, and the symbolic check was taken to that order. The lattice side was computed, not guessed: a relabelling makes a weighted hop of a rate, and the exact force density carries that hop; the factor `cos k` between force and weight was seen in the control and traced to the lattice momentum being `sin k`. A refuter test on a ring was found to be empty (`0 = 0`) and was replaced by a three-dimensional one. The first version of the symbolic check of T4 used the library's series and complex-conjugate machinery on shifted functions and failed for technical reasons; it was rewritten with explicit truncated expansions. A comparator lens: the contracted identity and the motion of the sources — under the Premises. A strategy lens: the decision record's list of supplied clauses can be re-read: B's force law is required by the ledger. Control and refuting pass: W1–W4 as reported under Executed. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_2026_09_21.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
