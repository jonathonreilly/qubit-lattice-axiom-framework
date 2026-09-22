---
claim_id: admissibility_rule_many_records_under_exclusion_source_is_the_projected_density_chessboard_invisible_interacting_sea_stiffens_clocks_oppositely_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 55, 63, 76 and 78 (open PRs #8570, #8571, #8593, #8611, #8613; not adopted) and the Record axiom in the owner's reading: the clocked reduced walk H_w = phi sigma_3 D phi on a ring (and the two-dimensional walk on tori, executed); two records with anticommuting composition; the exclusion projector P onto configurations with the records on different sites; the compressed generator P H2 P, H2 = H_w (x) 1 + 1 (x) H_w. (T1) For the projected pair Psi_P = P Psi, the exact derivative of <Psi_P|H2|Psi_P> with respect to the tick rate u_x of any site equals the projected pair's own energy density at that site, e_x^(2) = sum over the two slots of Re <Psi_P| P_x H_w |Psi_P>, and not the unprojected pair's; the densities sum to the pair's energy (weight one): block 55's source law holds for records under exclusion, with the projected state. (T2) P commutes with every site field and with the simultaneous translation of both records, so a chessboard of clocks is invisible to the compressed generator (block 76 T1) and crystal momentum is conserved under exclusion. (T3) P does not commute with the one-step momentum S (x) 1 + 1 (x) S (it carries a record onto its neighbour's site), so block 63's conserved momentum is not conserved for records under exclusion. EXECUTED, NOT CLAIMED: under exclusion the free sea's filling (the negative branch has as many states as sites, fewer only by half the zero modes: a record on nearly every site) is a JAMMED lattice; the many-record ground state there, against the free sea, for the mode cos(2 pi x/L) on 2D tori, has a volume term three to four times smaller in magnitude (-0.19, -0.26 per site against -0.93, -0.90 on 3x3, 4x3) and a clock response whose gradient part has the OPPOSITE sign (-0.027, -0.043 per |q|^2 against +0.025, +0.015); at HALF filling the interacting crowd's gradient part has the free sea's sign and size (+0.014 against +0.015 on 4x3; -0.001 on 3x3); on rings the free sea's gradient part vanishes at this mode while the jammed one's is negative and grows with the ring. NOT claimed: the free-branch filling as a meaningful state of the interacting problem (block 78: it is not free); matched pulls under exclusion (open); anything about Z^3 beyond the tori; the exchange sign; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_many_records_under_exclusion_source_projected_density_interacting_sea_2026_09_22.py
---

# Many records under exclusion: the source is the projected density, a chessboard of clocks stays invisible, and the interacting sea stiffens the clocks the opposite way

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements for two records under the Record axiom's exclusion; executed many-record numbers labelled; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks and the Record axiom in the owner's reading; it reports which of the ledger's identities survive when two or more records compose under exclusion, and what the interacting sea does to the clocks when executed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 78 (open PR #8613) showed that "one record per site at a time" is an interaction: two of the axioms' records are not a free pair of either sign. Block 76 (open PR #8611) had probed a *free* sea. This note asks what the ledger keeps when records compose the axioms' way, and what the interacting sea does.

1. **The source law survives, with the projected state** (T1, exact). Change one site's tick rate: the projected pair's energy changes by the projected pair's own energy density there — block 55's law, because the exclusion projector does not depend on the rates. The unprojected pair's density is not the source. Weight one holds.
2. **A chessboard of clocks stays invisible; crystal momentum stays conserved; the one-step momentum does not** (T2, exact). The projector commutes with site fields and with moving both records together, and not with moving one record at a time.
3. **The interacting sea stiffens the clocks the opposite way — because it is jammed** (executed). Under exclusion the free sea's filling is a record on nearly every site: the negative branch has as many states as there are sites, fewer only by half the zero modes. The many-record ground state there has a volume term three to four times smaller than the free sea's and a clock response whose gradient part has the opposite sign, on every two-dimensional torus tried. At half filling — a mobile crowd — the gradient part has the free sea's sign and size. So the sea reading, carried over to the axioms' records, fills the lattice solid; what a mobile crowd of records does to the clocks is the free sea's kind of thing at half the density.

So block 76's reading, in which the sea's energy is the field's, does not carry over to the axioms' records as a sea at all — the corresponding state is jammed and its clock response has the opposite sign; what survives is the ledger's bookkeeping: source = energy density of whatever state the records are in.

In plain terms: when two walkers can never share a site, the rule "clocks are slowed by energy where it is" still holds exactly — one only has to use the energy of the pair as it actually is, not of two walkers imagined free. Their combined crystal momentum is still conserved; the one-step momentum of block 63 is not, because the crowding itself pushes. And filling the lattice with such walkers the way one fills a free sea means one walker on every site — a jam; a jam resists a change of clock rate in the *opposite* direction to a free sea, while a half-full crowd resists it the free sea's way. The "sea" reading does not carry over; a crowd does something of its own.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 78 (PR #8613), next_trace_action: 'the two-record ledger (does block 55's action = reaction survive exclusion?); the hard-core sea's energy on small tori against block 76's'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the ledger's source law and weight one survive exclusion with the projected state; the jammed filling's clock response has the opposite sign to the free sea's and neither the crowd nor the jam supplies a lengths' stiffness: the sea reading does not carry over; next: matched pulls under exclusion (the contact of the records carries one-step momentum); the interacting crowd at low filling as content; the owner's fork on how records compose"
conditional_surface_status: "T1-T3 exact for every pair state and every ring (proofs) and executed on the ring of 6; the many-record numbers are the control's (tori 3x3, 4x3; rings 6, 8, 10)"
hypothetical_axiom_status: "the clocked reduced walk; two or more records with anticommuting composition under the Record axiom's exclusion; hypotheses only, the composition rule an import"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Record axiom (one record per site), the Qubit axiom's coin, and the memo's silence on amplitude dynamics and on how records compose. Blocks 54, 55, 63, 76, 78 (open PRs) supply the clocked walk, the ledger's source, the conserved momentum, the free-sea reading and the exclusion.

- **Projected pair.** `Ψ_P = PΨ`, `Ψ = ψ₁ ⊗ ψ₂ − ψ₂ ⊗ ψ₁`, `P` the projector onto index pairs on different sites; the compressed generator is `PH₂P` and `⟨Ψ_P|PH₂P|Ψ_P⟩ = ⟨Ψ_P|H₂|Ψ_P⟩`.
- **Energy density of a pair at `x`.** `e_x^{(2)} = Re⟨Ψ_P|(P_x ⊗ 1)(H_w ⊗ 1)|Ψ_P⟩ + Re⟨Ψ_P|(1 ⊗ P_x)(1 ⊗ H_w)|Ψ_P⟩`.
- **Derivative.** With `φ_x → φ_x(1 + t)` the pair's energy is a quadratic polynomial in `t`; its `t`-linear coefficient is `φ_x∂/∂φ_x = 2∂/∂u_x`, so `∂/∂u_x = (F(1) − F(−1))/4`, exactly.
- **Many-record ground state (control).** The compressed generator on the antisymmetric hard-core space of `N` records, diagonalised (dense or sparse, floating point); `Π` the second-order coefficient of its ground energy in the amplitude of `u = ε cos(2πx/L)`; the local part is the uniform second derivative times the mode's mean square; the gradient part the remainder.

The projection of a hopping problem onto configurations with no double occupancy is the infinite-repulsion problem of many-body practice; named as a comparator only.

## Prior art and what is new

New, inside the framework's vocabulary: that block 55's source law is exactly a statement about whatever state the records are in, and so survives the Record axiom's exclusion unchanged in form; the exact list of what the exclusion commutes with; and the executed sign reversal of the interacting crowd's clock response at the free sea's filling. No gravitational claim is made.

## Exact target and obligation graph

Target: the ledger under the axioms' composition. Obligations: (O1) the source; (O2) invariances; (O3) the interacting sea (executed). T1, T2 discharge O1, O2.

## Theorem T1 — the source under exclusion

*Statement.* For any pair state and any positive rate field, `∂⟨Ψ_P|H₂|Ψ_P⟩/∂u_x = e_x^{(2)}` at every site, and `Σ_x e_x^{(2)} = ⟨Ψ_P|H₂|Ψ_P⟩`.

*Proof.* `∂H_w/∂u_x = ½{P_x, H_w}` (block 55 T1) and `P` does not depend on the rates; `Re⟨Ψ_P|½{P_x ⊗ 1, H_w ⊗ 1}|Ψ_P⟩ = Re⟨Ψ_P|(P_x ⊗ 1)(H_w ⊗ 1)|Ψ_P⟩`, and the same for the second slot. Weight one: `H₂` is homogeneous of degree one in the rates. Executed exactly on a ring of 6 with a varying rational rate field (runner B1): the `t`-linear coefficients at all six sites equal `e_x^{(2)}` of the projected pair and differ from the unprojected pair's densities; they sum to the energy. ∎

## Theorem T2 — what the exclusion commutes with

*Statement.* (a) `[P, φ ⊗ φ] = 0` for every site field `φ`; hence the compressed generator with a chessboard of rates equals the compressed free generator (block 76 T1). (b) `[P, T ⊗ T] = 0` for the simultaneous translation: crystal momentum is conserved under exclusion (with uniform rates).

*Proof.* `P` is diagonal in the position basis and its condition `x₁ ≠ x₂` is invariant under a common shift and under diagonal factors. ∎

## Theorem T3 — the one-step momentum under exclusion

*Statement.* `[P, S ⊗ 1 + 1 ⊗ S] ≠ 0`: the one-step momentum carries a record onto its neighbour's site, which `P` removes; block 63's conserved momentum is not conserved for records under exclusion.

*Proof.* Runner C1 exhibits the pair `(0, 2)` (sites 0 and 1) carried by `S ⊗ 1` onto a same-site pair, which the projector removes; the commutator on that pair is nonzero. ∎

The momentum whose conservation block 63 proved is the *free* walk's; for records under exclusion the contact itself exchanges it between them. Whether the two records' pulls through the rate field are nevertheless matched (block 55 T3) is not decided here (Boundaries).

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block80_interacting_sea.py` (antisymmetric hard-core many-record spaces, dense or sparse diagonalisation). **W1** (rings, reduced walk, the filling that occupies the free negative branch — 4, 6, 8 records on 6, 8, 10 sites): the free sea's response to `cos(2πx/N)` is exactly its local part (gradient part `0.00000`), the interacting one's gradient part is `−0.000, −0.070, −0.201` per `|q|²`; energies per site `−0.577, −0.604, −0.616` (free) against `−0.289, −0.231, −0.190` (interacting). **W2** (two-dimensional walk on tori): at the free-branch filling (8 of 9, 10 of 12 sites: jammed) `3×3` — free `c₀ = −0.929`, gradient `+0.025`; interacting `−0.191`, `−0.027`; `4×3` — free `−0.896`, `+0.015`; interacting `−0.265`, `−0.043`; at half filling the interacting gradient parts are `−0.001` (`3×3`) and `+0.014` (`4×3`, against the free `+0.015`). **W3** (`4×3`, strains through the reach-three coupling, gradient parts per `|q|²`): free sea — rates `+0.0151`, isotropic stretch `+0.0002`, traceless `+0.0002`; half-filled crowd — `+0.0141`, `+0.0004`, `+0.0004`; jammed — `−0.0430`, `−0.0017`, `−0.0017`: the interaction does not supply a lengths' stiffness either; the crowd's response to strain stays forty times below its response to the rates. The free two-dimensional sea's gradient part is positive and of the same size as the three-dimensional one's (block 76: `+0.024`), so the two-dimensional comparison is representative where the one-dimensional one is not.

## No-Go Discipline Gate

The note's negative sentences: the unprojected density is not the source; the one-step momentum is not conserved under exclusion; the interacting sea's clock response does not have the free sea's sign.

### N1 — Routes by which the sentences could fail or mislead
1. *The filling.* Under exclusion "the free negative branch's filling" is a jammed configuration (10 records on 12 sites); the reversal of sign is a statement about that state, not about a sea in any physical sense. Half filling is in the control.
2. *Symmetric composition.* T1, T2 hold for either sign (their proofs do not use it); the executed numbers are for the antisymmetric case.
3. *Small tori.* Three tori and three rings; no extrapolation is claimed.
4. *Matched pulls.* Not examined; the contact force between records is internal, and whether the pair's pulls through the rate field still cancel is open.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The reduced walk on rings; the two-dimensional walk on tori; uniform rates apart from the mode; two records in the exact parts.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Record axiom; the coin | yes (premise) |
| blocks 54, 55, 63 (open PRs #8570, #8571, #8593) | the clocked walk; the source law; the conserved momentum | yes (restated) |
| blocks 76, 78 (open PRs #8611, #8613) | the free-sea reading; the exclusion as an interaction | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "source = projected density; chessboard invisible; crystal momentum kept, one-step momentum not; interacting sea's sign reversed" | executed: the `t`-linear coefficient at each site; one basis pair carried onto a same-site pair | executed: derivative against density at all six sites; chessboard against free on the projected pair | executed: control — responses on three rings and three tori | executed: weight one; the simultaneous translation on the whole pair | T1, T2 by proof for every pair and ring; the sea's numbers executed only |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Of course the source is the actual state's density." Reply: yes — and that is the content: the ledger's law is about the state, so exclusion changes the state and not the law; block 76's hole argument, which used additivity, is what changes. Second objection: "A jammed lattice is not a sea." Reply: agreed, and the note says the sign reversal is about that state; it is reported because the free reading picked that filling.

### N8 — Cross-cycle echo
Block 55: source = energy density. Block 76: a free sea's energy as the field's. Block 78: the axioms' records are not free. Here: the source law is untouched, the sea reading is not.

## Falsifiers

- A pair state and rate field for which `∂⟨Ψ_P|H₂|Ψ_P⟩/∂u_x ≠ e_x^{(2)}` at some site.
- A site field or simultaneous translation that fails to commute with `P`.
- A two-dimensional torus on which the interacting ground state at the free-branch filling has a clock response of the free sea's sign.

## Boundaries and non-claims

Two records in the exact parts; the composition rule is an import; matched pulls under exclusion are open; the many-record numbers are on small tori. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record axiom; the Qubit axiom; the memo's silence on composition. Blocks 54, 55, 63, 76, 78 (PRs #8570, #8571, #8593, #8611, #8613, open): restated or placed.
- Named standard imports at definition level: derivatives of quadratic forms; projectors diagonal in a basis; sparse diagonalisation for the control.

## Review record
Supervisor-run block, the twenty-eighth of the source-link direction; the fifth after the fork probe. Lens pass, in writing, by the supervisor: a foundations lens — the Record axiom's exclusion is used as written; nothing about the sign of composition is assumed in the exact parts; a rigour lens — the first version of the density used `2UᵀP_xAV` for the real part of `⟨Ψ|P_x(−iA)|Ψ⟩`, which is right for the total (no `P_x`) and wrong site by site; the runner failed, the real part was recomputed as `UᵀP_xAV − VᵀP_xAU` per slot, and the identity then held at every site; the factor between `φ_x∂/∂φ_x` and `∂/∂u_x` was also caught by the weight-one check; the one-dimensional free sea was found to have no gradient part at the longest mode, so the two-dimensional walk was used for the comparison and its free stiffness checked against the three-dimensional one before any sign was read. A strategy lens — the ledger's bookkeeping is robust to the composition rule; the sea reading is not. Control: as reported under Executed. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_many_records_under_exclusion_source_projected_density_interacting_sea_2026_09_22.py
```

Expected: `TOTAL: PASS=9 FAIL=0`.
