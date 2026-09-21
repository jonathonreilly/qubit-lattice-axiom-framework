---
claim_id: admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 62, 63, 64, 65, 68 and 69 (open PRs #8570, #8592, #8593, #8595, #8596, #8599, #8601; not adopted): block 54's walk H = sum_a sigma_a S_a, its eight species n in {0,1}^3 with D_n = diag((-1)^{n_a}); a rate field (phi H phi, w = phi^2); block 62's frame H[E] = (1/2) sum_j {E^j.sigma, S_j}; block 65's blind walk H[theta] (frame rotation plus the twist hop); the relabelling's strain couplings of reach two (with S_j) and of reach three (with P_j = S_j C_j). Blocks 68 and 69 compared the species in UNIFORM fields through H^2. Here, for fields that VARY and as operator identities: (T1) with U_n = (-1)^{n.x}, s_n = det D_n, rho_n = s_n D_n (the identity or a half turn about an axis), R_n the coin's half turn for rho_n and V_n = R_n U_n: V_n H V_n = s_n H, and the same in any rate field; V_n V_n = 1; the even maps anticommute pairwise; the site density is unchanged, the coin densities are turned by rho_n, the energy density is multiplied by s_n; s_n is the sense of species n, four of each. (T2) V_n H[F] V_n = s_n H[F'] with: rates unchanged; frame E -> rho E rho; twist theta -> rho theta; reach-two strain B -> B D (a change on one side only); reach-three strain unchanged. (T3) With rates and reach-three strains the even maps are exact symmetries for every field configuration; the reversal of motion Theta = sigma_2 x conjugation commutes with the walk in all five kinds of real field, and for odd n the antilinear A_n = Theta V_n carries every solution to a solution in the same fields with the same site densities and the energy reversed: the sixteen branches (eight species, two signs of the energy) fall into two classes of eight exact copies, labelled by s_n x sign(E); the inversion x -> -x sends the walk in each field to minus the walk in the mirror-image field, so the two classes are mirror images of each other; U_(111) reverses the energy for rates, frames, twists and reach-three strains, whose spectra are therefore symmetric about zero, while it sends a reach-two strain to its negative, and the spectrum of the walk in a varying reach-two strain is not symmetric: tr H^3 = -735/8192 for an executed rational strain field on a 4x4x4 torus. NOT claimed: that the species are physical or that any is to be removed; which coupling is supplied; that no other map joins the two classes; anything about the field's own energy; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_2026_09_21.py
---

# The eight species are exchanged by site signs and a half turn of the coin: what each varying field becomes

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact operator identities about block 54's supplied walk in the supplied kinds of field; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for the couplings of rates, frames, twists and bond strains to them; it reports the exact maps that exchange the walk's eight species and what each varying field becomes under them; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 68 and 69 (open PRs #8599, #8601) compared the walk's eight species through `H²` in *uniform* fields. This note finds the maps behind those comparisons and shows that they are exact for fields that vary in any way.

1. **The maps.** Flip the sign of the amplitude on every other site along the reflected axes, and give the coin a half turn. That carries species `n` to the first species. The walk goes to itself for the four species with an even number of reflected axes and to *minus* itself for the four odd ones. The sign is the species' **sense** (handedness): four of each (T1).
2. **What each field becomes** (T2). Rates: unchanged. A frame, and the twist of the blind walk: turned by the same half turn — the geometry's mirror image in its angles, the same lengths. A reach-two strain: changed **on one side only** (`B → BD`), which is no turn of anything — a stretch becomes a squeeze. A reach-three strain: **unchanged**.
3. **Sixteen branches, two classes** (T3). Count a species with positive energy and the same species with negative energy as two branches. With rates and reach-three strains, in *any* configuration, the maps (with the reversal of motion where the energy flips) carry solutions to solutions in the **same fields** with the **same site densities**. The sixteen branches fall into two classes of eight exact copies. The inversion `x → −x` carries one class to the other in the mirror-image fields: the two classes are mirror twins.
4. **The reach-two strain alone breaks the energy reversal.** Rates, frames, twists and reach-three strains all hop an odd number of steps; the checkerboard of all three axes reverses their energy, so their spectra are symmetric about zero. The reach-two term hops an even number of steps, and the spectrum of the walk in it is not symmetric — exactly, `tr H³ = −735/8192` for an executed field.

In plain terms: the eight kinds of walker are one walker seen through a checkerboard of signs. Clocks cannot tell the kinds apart. The three-step rule for lengths cannot either. A frame tells them apart only as a mirror would. The two-step rule tells them apart outright, and it is also the only one of the five that spoils the balance between positive and negative energies.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 68 (PR #8599) and block 69 (PR #8601), opportunity queue: 'are the eight species all kept?'; 'the species under block 62's disturbances and block 65's twist hop'; blocks 68 and 69 proved their comparisons for uniform fields only."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the species question becomes a question of multiplicity (two classes of eight exact copies under rates and reach-three strains); next: what a ledger that counts energy does with sixteen branches; whether the two senses are both kept; the owner's forks on reach and on the species"
conditional_surface_status: "T1, T2 and T3's maps are operator identities for every state and every field on every torus with even sides and on the infinite lattice; T3's cubic trace is one executed rational strain field"
hypothetical_axiom_status: "block 54's walk and the five supplied kinds of field; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (whose symmetries are the proper cubic rotations; it names no inversion), the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 64, 65, 68, 69 (open PRs) supply the walk, its species and the five kinds of field.

- **Walk and fields.** `H = Σ_a σ_a S_a`; rates `φHφ`; frame `H[E] = ½Σ_j{E^j·σ, S_j}`; blind walk `H[ϑ] = H + ½Σ_j{(ϑ × e_j)·σ, S_j} + ½Σ_a C_a[d_aϑ_a]`; strains `H₂[B] = H + Σσ_a½{C_a[B_a^j], S_j}`, `H₃[B] = H + Σσ_a½{C_a[B_a^j], P_j}`, `P_j = S_jC_j`. All fields real.
- **Species data.** `D_n = diag((−1)^{n_a})`, `s_n = det D_n`, `ρ_n = s_nD_n` (a diagonal rotation: the identity, or the half turn about the one axis it keeps).
- **Maps.** `U_n = (−1)^{n·x}`; `R_n` the identity or `σ_c` for the axis `c` that `ρ_n` keeps; `V_n = R_nU_n`. Reversal of motion `Θ = σ_2 ×` (complex conjugation). Inversion `Π: x → −x`, no action on the coin.
- **Branch.** A species together with a sign of the energy.

The equal numbers of the two senses among the zeros of a lattice walker are the theorem of Nielsen and Ninomiya; the doubling of levels by a reversal of motion squaring to minus one is that of Kramers; the antilinear reversal is Wigner's (named in block 54). The site-sign maps are familiar from the literature on staggered lattice fermions (Kogut and Susskind). Nothing is used as authority; what is used is proved below.

## Prior art and what is new

New, inside the framework's vocabulary: the exchange maps stated for each of the campaign's five supplied kinds of *varying* field, with the table of what each field becomes; that the reach-three strain is invariant and the reach-two strain is changed on one side only; the two classes of eight exact copies under rates and reach-three strains; and the parity of the number of steps as the reason the reach-two term alone breaks the energy reversal. No gravitational claim is made.

## Exact target and obligation graph

Target: the comparisons of blocks 68 and 69 for varying fields, and what they imply for the count of species. Obligations: (O1) the maps; (O2) each field's image; (O3) the classes and the energy reversal. T1–T3 discharge them.

## Theorem T1 — the exchange maps

*Statement.* (a) `U_nT_aU_n = D_aT_a`; hence `S_a → D_aS_a`, `C_a[v] → D_aC_a[v]` for every bond function `v`, `P_a → P_a`, and site functions are unchanged. (b) `V_nHV_n = s_nH`, and `V_n(φHφ)V_n = s_n φHφ` for every rate field. (c) `V_n² = 1`; `V_{(110)}V_{(011)} = −V_{(011)}V_{(110)} = iV_{(101)}`. (d) At every site `ψ†ψ` is unchanged, `ψ†σ_aψ` is multiplied by `(ρ_n)_a`, and `Re ψ†(Hψ)` by `s_n`. (e) Near `k = πn + q`, `H ≈ Σ_a D_aσ_aq_a`: the map from `q` to the coin's vector has determinant `s_n` — the sense of the species; four species have each sense.

*Proof.* (a) `(U T_a U ψ)(x) = (−1)^{n·x}(−1)^{n·(x + e_a)}ψ(x + e_a)`. `P_a` moves two steps. (b) `U_nHU_n = Σ D_aσ_aS_a = s_n Σ(ρ_n)_aσ_aS_a`, and `R_nσ_aR_n = (ρ_n)_aσ_a` because `ρ_n` is a proper rotation. `φ` is a site function. (c) `U_n` and `R_n` are commuting involutions; `σ_3σ_1 = iσ_2`. (d) `V_n` is a unitary acting site by site. (e) The slopes of `sin k_a` at `0` and `π` are `±1`. ∎

## Theorem T2 — what each varying field becomes

*Statement.* For all real fields, varying in any way:

| Field | `V_n H[·] V_n` |
|---|---|
| rates `φ` | `s_n φHφ` (unchanged) |
| frame `E` | `s_n H[ρ_nEρ_n]` |
| twist `ϑ` | `s_n H[ρ_nϑ]` |
| reach-two strain `B` | `s_n H₂[BD_n]` |
| reach-three strain `B` | `s_n H₃[B]` (unchanged) |

*Proof.* Term by term with T1(a), `R_nσ_aR_n = ρ_aσ_a`, `D_a = s_nρ_a`, and `ρ_aρ_j = ρ_b` for `a, b, j` distinct. Frame: `½{E_a^jρ_aσ_a, D_jS_j} = s_n½{(ρ_aE_a^jρ_j)σ_a, S_j}`. Twist: `ρ_aD_jε_{abj}ϑ_b = s_nε_{abj}(ρϑ)_b`, and `D_aC_a[d_aϑ_a] = s_nC_a[d_a(ρϑ)_a]`. Reach two: `ρ_aD_aD_j σ_a½{C_a[B_a^j], S_j} = s_n σ_a½{C_a[B_a^jD_j], S_j}`. Reach three: `P_j` is unchanged, so only `ρ_aD_a = s_n` appears. ∎

The frame's inverse metric `g = EᵀE` becomes `ρgρ = DgD`: block 68 T2, now for frames that vary. `B → BD` acts on one index only; it is not a rotation of the strain, and the inverse metric becomes `(1 + BD)ᵀ(1 + BD)`: block 68 T3. Block 69 T4 is the last row. The blind walk of block 65 is blind for every species.

## Theorem T3 — two classes of eight, mirror twins, and the energy reversal

*Statement.* (a) With rates and reach-three strains in any configuration, the three even maps commute with the generator: they carry every solution to a solution in the same fields with the same site densities and energy densities. (b) `Θ` commutes with the walk in all five kinds of field, and `Θ² = −1`, so every level is at least doubly degenerate. For odd `n`, `A_n = ΘV_n` is antilinear with `A_nH = −HA_n` for rates and reach-three strains: it carries every solution to a solution in the same fields with the same site densities and the energy reversed. The sixteen branches fall into two classes of eight, labelled by `s_n × sign(E)`, and the maps of (a), (b) act within each class. (c) `ΠH[F]Π = −H[F∘Π]` for each of the five kinds of field, `F∘Π` the mirror image (a site field at `−x`; a bond field on the inverted bond): `ΘΠ` carries a solution of one class in `F` to a solution of the other class in `F∘Π`. (d) `U_{(111)}HU_{(111)} = −H` for rates, frames, twists and reach-three strains, so their spectra are symmetric about zero in every configuration; `U_{(111)}H₂[B]U_{(111)} = −H₂[−B]`, and the spectrum of `H₂[B]` is not symmetric in general: `tr H₂[B]³ = −735/8192` for the rational strain field of the runner on a `4×4×4` torus.

*Proof.* (a) T2 with `s_n = 1`. (b) `ΘS_jΘ⁻¹ = −S_j`, `ΘP_jΘ⁻¹ = −P_j`, `ΘC_a[v]Θ⁻¹ = C_a[v]`, `Θσ_aΘ⁻¹ = −σ_a`, real fields unchanged; each term of each generator contains an even number of reversed factors. If `Hψ = Eψ` then `HΘψ = EΘψ`; an antiunitary map has `⟨Θa|Θb⟩ = ⟨b|a⟩`, so `⟨Θψ|Θ²ψ⟩ = ⟨Θψ|ψ⟩`, while the left side is `−⟨Θψ|ψ⟩`: `Θψ` is orthogonal to `ψ`. An antilinear `A` with `AH = −HA` gives `i∂_t(Aψ) = −A(i∂_tψ) = −AHψ = HAψ`. Even maps keep the species' parity and the energy; odd maps flip both; `Θ` keeps both. (c) `ΠS_jΠ = −S_j`, `ΠP_jΠ = −P_j`, `ΠC_a[v]Π = C_a[v∘Π]`, and the difference of `ϑ_a∘Π` along the inverted bond is minus the image of `d_aϑ_a`. `Π` keeps the species and reverses the energy. (d) T2 with `ρ = 1`, `D = −1`. The rate, frame, twist-hop and reach-three terms move an odd number of steps; the reach-two term moves none or two. A spectrum symmetric about zero has vanishing cubic trace. ∎

The Lattice axiom names the proper rotations only; the mirror image of (c) is not among the symmetries the axioms supply (block 54 T1(c) added an antilinear inversion as a supplied symmetry).

## Executed (supervisor control; floating point; dense matrices; evidence, not proof)

`specs/supervisor_control_block70_species_exchange.py`: every generator as a `432 × 432` matrix on a `6×6×6` torus with random real fields. W1: all forty identities of T2 hold with residual `0.0e+00` as matrix identities; with the field left unchanged the residuals are `0.64–0.85` (frame, twist; zero for `ρ = 1`), `0.32–0.38` (reach two), `0.00` (rates, reach three). W2: every level has multiplicity two in all four cases; the spectrum's asymmetry is `6e-15` (rates with a reach-three strain), `5e-15` (frame), `9e-15` (twist), and `1.2e-2` for the reach-two strain. W3: the cubic trace in floating point, `−0.0897216796875`, equals the runner's `−735/8192`; that spectrum runs from `−1.9219` to `+1.9069`. W4: for three odd species, `A_n e^{−iHt}ψ − e^{−iHt}A_nψ` has norm at most `7e-16`, the site densities of the two movies agree to `1e-17`, the energies are `∓0.024148`; without `Θ` the same difference has norm `1.50`.

## No-Go Discipline Gate

The note's negative sentences: a reach-two strain is not unchanged by the maps; the spectrum of the walk in a reach-two strain is not symmetric about zero.

### N1 — Routes by which the sentences could fail or mislead
1. *Another map.* A different unitary might carry species `n` in a reach-two strain `B` to the first species in `B` itself. Not excluded in general. For `n = (1,1,1)` a map with `XH₂[B]X⁻¹ = −H₂[B]` would make the spectrum symmetric, which E1 refutes for the executed field; maps of other forms are not excluded.
2. *Uniform strain.* For a uniform reach-two strain the spectrum *is* symmetric (`H²` is a multiple of the identity at each `k`); the asymmetry needs a varying strain.
3. *Other maps between the classes.* The note says which of its maps join the classes and which do not; it does not claim a classification of all maps.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Tori with even sides (the site signs must be periodic); a side of at least six where `P_j` is used; real fields; the identity coin frame at zero field; the twist at first order, as block 65 supplied it.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its proper rotations; the Qubit axiom's one-site algebra | yes (premise) |
| blocks 54, 62, 65 (open PRs #8570, #8592, #8596) | the walk; the frame; the blind walk (its identity re-verified in C2) | yes (restated) |
| blocks 63, 64, 69 (open PRs #8593, #8595, #8601) | the strain couplings of reach two and three | yes (restated) |
| block 68 (open PR #8599) | the species; the uniform-field comparisons now extended | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the maps exchange the species exactly for varying fields; reach three unchanged, reach two changed on one side; two classes of eight; reach two alone breaks the energy reversal" | executed: `V_n² = 1`, the anticommutation, the site, coin and energy densities at all 216 sites | executed: every identity as an equality of spinor fields at all 216 sites, all eight species, fields varying with every coordinate | executed: the cubic trace over all 128 basis states of a `4×4×4` torus; the sense of each zero | executed: block 65's identity re-verified; all nine components varied at once; the reversal of motion and the inversion against all five kinds of field | operator identities for every state and field on even tori and the infinite lattice; the cubic trace is one executed field; whether the species are physical, which coupling is supplied and how far it may reach are not decided |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is the textbook symmetry of naive lattice fermions." Reply: for the free walk, yes, and the Premises say so. The content here is the table for the campaign's own five kinds of varying field — in particular that the twist hop and the reach-three strain respect the maps, and that the reach-two strain, the coupling blocks 63–67 worked with, is the one that does not. Second objection: "Two classes of exact copies means the species are unobservable; say so." Reply: the note says what it proved: no rate field and no reach-three strain tells the members of a class apart, and a record of site densities cannot. A ledger that counts energy counts every branch present; how many are present is not a question these maps answer.

### N8 — Cross-cycle echo
Block 68 found the species seeing different lengths under reach two; block 69 found a coupling that treats them alike. Here the reason is one line — the two-step momentum is untouched by the site signs, the one-step momentum is not — and it comes with a second, unlooked-for mark against reach two: the loss of the energy reversal.

## Falsifiers

- A state, species and field violating any row of T2's table.
- A rate field and reach-three strain field in which some solution's image under `V_n` (even `n`) or `A_n` (odd `n`) is not a solution.
- A configuration of rates, frames, twists or reach-three strains whose spectrum is not symmetric about zero.

## Boundaries and non-claims

The species are not declared physical, and none is removed. The coupling is not chosen. The field's own energy (block 64) is outside: whether its equations respect `B → BD` is not examined. The twist is block 65's, at first order. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom and its proper rotations, the Qubit axiom's one-site algebra, and the memo's silence on amplitude dynamics. Blocks 54, 62, 63, 64, 65, 68, 69 (PRs #8570, #8592, #8593, #8595, #8596, #8599, #8601, open): restated or placed.
- Named standard imports at definition level: conjugation of shifts by site signs; half turns in the coin's algebra; antilinear maps; the trace of a cube.
- Reference only: Nielsen and Ninomiya; Kramers; Wigner; Kogut and Susskind.

## Review record
Supervisor-run block, the eighteenth of the source-link direction and the fourteenth of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the maps are properties of a supplied walk, not of the axioms; the site signs are not among the Lattice axiom's symmetries, and the mirror image that joins the two classes is not either — the note says both; nothing is removed or kept by fiat. A rigour lens: blocks 68 and 69 argued through `H²` in uniform fields, which cannot see the sign `s_n`; here the identities are for the generator itself and were checked as equalities of spinor fields with all components of every field varying; block 65's operator was re-verified before use so that the twist row is about the right object; the cubic trace was chosen as an exact witness after a scratch scan showed that single-bond strains give zero (N1.2's cousin: the asymmetry needs several components together). A strategy lens: the species question, which block 68 left as "kept or removed", becomes a question of multiplicity under the couplings that respect the maps, and reach two acquires a second cost. The supervisor's scratch expectation that the even maps would add a further doubling of levels was wrong — the executed multiplicity is two in every case, which the reversal of motion already accounts for; no such claim is made. Control: as reported under Executed, with a contrast line so that W4's zero is seen to have teeth. Mutation census: 11 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_2026_09_21.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
