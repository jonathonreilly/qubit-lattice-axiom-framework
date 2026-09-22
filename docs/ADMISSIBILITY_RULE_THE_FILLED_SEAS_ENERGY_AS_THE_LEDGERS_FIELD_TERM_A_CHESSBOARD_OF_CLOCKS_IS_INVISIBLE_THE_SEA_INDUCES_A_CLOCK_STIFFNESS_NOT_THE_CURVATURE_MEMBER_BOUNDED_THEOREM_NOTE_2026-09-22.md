---
claim_id: admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 55, 63, 69, 70 and 71 (open PRs #8570, #8571, #8593, #8601, #8602, #8603; not adopted), PROBING one reading of them, itself not adopted: every negative-energy state of the walk is occupied (a many-record state with anticommuting composition - an import beyond the Record axiom's one record per site, flagged) and the sea's energy E_sea = sum of the negative eigenvalues of H_w is booked as the field's term of the ledger, so that the field's energy would be induced rather than supplied. (T1) A chessboard of clock rates, phi_x = c^{eps(x)} with eps = (-1)^{x+y+z}, has phi_x phi_y = 1 on every bond, so phi H phi = H exactly at any amplitude; more generally clause B's coupling sees the rates only through the bond products: two rate fields with the same bond products give the same clocked walk. (T2) Under the reach-two strain coupling U_(111) H2[B] U_(111) = -H2[-B] and tr H2[B] = 0, so E_sea[-B] = E_sea[B]: the filled sea has no first-order response to a reach-two strain. (T3) With anticommuting composition the energy and every one-body energy density of a two-record state are the sums over the two occupied one-record states (exact on a ring with a varying rate field), so the ledger's source is additive over occupied states and removing an occupied negative-energy state changes the source by minus that state's density: a hole sources as a positive body does. (T4) With the measured signs c < 0 < kappa and c + 12 kappa < 0 (declared as rounded rationals), the linearised static law of this reading puts a FASTER clock at a positive body (repulsion), and with the volume term removed a slower one (attraction); by T1 the exact second variation vanishes on the chessboard mode, so the linearised law never fixes the clocks' chessboard component. EXECUTED, NOT CLAIMED (floating point; tori 6^3 to 12^3): volume term c0 = -1.193 per site (weight one); the rates' polarisation has a gradient part +0.0236 x lattice |q|^2 per site, isotropic to 1 percent and converging with L: the clocks' stiffness kappa = 0.095 - the induced energy is NOT counted per local tick; it is the simplest member's kind (block 56), with induced coupling gamma = 1/kappa = 10.5 when the volume term is removed; the strains' polarisation under reach three is ten to sixty times smaller (+0.0004 to +0.0035 per |q|^2). NOT claimed: that the sea is filled; the exchange sign; that the field's energy is induced; anything about the curvature member being induced (it is not, on this lattice, by this sea); any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_chessboard_clocks_invisible_2026_09_22.py
---

# The filled sea's energy as the ledger's field term: a chessboard of clocks is invisible; the sea induces a clock stiffness, not the curvature member

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about a probed reading of supplied clauses; executed numbers labelled; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks and probes one reading of them, in which every negative-energy state is occupied and the sea's own energy is booked as the field's term of the ledger; it reports what that reading gives exactly and what it gives when executed; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 71 (open PR #8603) left the owner a fork: which amplitudes are present. The reading of that fork that matches established physics — the panel of 2026-09-22 (`FORK_PROBE_source_link_20260922.md`) was unanimous — fills every negative-energy state; a missing one is then a positive source, and block 71's chase does not arise. That reading offers something more: the sea's own energy is a function of the clocks and lengths, and if it is booked on the field's side of the ledger, the field's energy is *induced*, not supplied — clause C's `F` would go, `γ` would be a number, and blocks 64's two demands (per-tick counting, blindness) might come for free. This note probes that reading.

1. **A chessboard of clocks is invisible** (T1, exact, one line). Clause B's coupling weights the hop across a bond by `√(w_x w_y)`; on a chessboard of fast and slow clocks every bond's product is the ambient rate. The walk, its spectrum and the sea's energy are exactly unchanged at any amplitude. More generally the walk sees the rates only through the bond products.
2. **Under the reach-two coupling the sea does not respond to strain at first order** (T2, exact): its energy is even in the strain, because block 70's checkerboard map sends `B` to `−B` and reverses the energy.
3. **With anticommuting composition the source is additive and a hole sources positively** (T3, exact): the two-record state's energy density is the sum of the two one-record densities.
4. **What the sea induces, executed** (T4 and the control). A volume term `c₀ = −1.193` per site (weight one). A **stiffness for the clocks**, `κ = 0.095`, isotropic and converging with the torus: the induced energy is not counted per local tick; it is block 56's kind. Almost no stiffness for the lengths (ten to sixty times smaller). With the volume term kept, the linearised static law makes clocks *faster* at a body — repulsion — and is singular at the chessboard mode by item 1. With it removed, attraction with an induced coupling `γ = 1/κ = 10.5`.

The reading therefore does not deliver the curvature member. Fork (i) — whether the field's energy is counted per local tick — stays a genuine supplied clause; fork 8's number is fixed only in a reading that gives half of the comparator's bending.

In plain terms: suppose empty space is already full of negative-energy walkers, and suppose their energy is what we have been calling the field's energy. Then a checkerboard of fast and slow clocks costs nothing at all, because every hop crosses one fast and one slow site. What the full sea does resist is a smooth change of clock rate — and it resists that in the way the simplest, half-bending theory does, not in the way the full-bending one does. Its total energy is large and negative, and if that counts, matter would speed clocks up rather than slow them down.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 71 (PR #8603), fork (v): which amplitudes are present; FORK_PROBE_source_link_20260922.md section 3: the panel's first-ranked probe, 'the sea's response (sigma_u, K_ind, c0) - one computation decides (v), 8, 1 and tests (i)'."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the induced field energy of the free massless sea is the simplest member's, not the curvature member's: fork (i) remains supplied; next: the axioms' own generator (the scalar hop a), SU(2) bond links, the exchange sign; whether a sea with rest energy (a staggered on-site term) induces a lengths' stiffness"
conditional_surface_status: "T1 exact for every chessboard of rates on even lattices and for every pair of rate fields with equal bond products; T2 exact for every strain; T3 exact for every pair of orthogonal one-record states; T4 exact for the declared rounded values on a 4x4x4 torus, the values themselves executed"
hypothetical_axiom_status: "block 54's clocked walk; the strain couplings of blocks 63 and 69; the reading: a filled negative branch with anticommuting composition, its energy as the field's term; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom's one-site algebra, the Record axiom (one record per site at a time), and the memo's silence on rates and amplitude dynamics. Blocks 54, 55, 63, 69, 70, 71 (open PRs) supply the walk, the ledger's source, the couplings, the maps and the negative branch.

- **Clocked walk.** `H_w = φHφ`, `φ = e^{u/2}`; the hop across the bond `xy` carries `φ_xφ_y`.
- **Chessboard.** `ε(x) = (−1)^{x+y+z}`; a chessboard of rates is `φ_x = c^{ε(x)}`.
- **Sea.** `E_sea = Σ_{E<0} E` over the spectrum of `H_w` (with strains, of `H_w[B]`); on an even torus the zero eigenvalues contribute nothing.
- **Many-record state.** Two records with anticommuting composition: `Ψ = ψ₁ ⊗ ψ₂ − ψ₂ ⊗ ψ₁`; one-body operators act as `O ⊗ 1 + 1 ⊗ O`; the energy density at `z` is the expectation of `E_z = ½{P_z, H_w}`, `P_z` the projector onto site `z`.
- **Polarisation.** For a mode `u = ε cos(q·x)`: `E_sea(ε) − E_sea(0) = Π(q) ε² N + O(ε⁴)` per site `Π(q) = c₀/4 + (κ/4)|q|²_lat + …`, `|q|²_lat = Σ_a 2(1 − cos q_a)`; `κ` is the coefficient of `½Σ_bonds(u_x − u_y)²`.
- **Declared values (T4).** `c = −1193/1000`, `κ = 95/1000`: the control's numbers rounded; the runner uses them as declared inputs and claims nothing about them.

The occupied negative branch with holes as positive sources is Dirac's reading; the vacuum energy of matter fields as a functional of the geometry inducing the field's energy is Sakharov's; the runaway of a mixed pair is Bondi's. Named here as comparators only.

## Prior art and what is new

New, inside the framework's vocabulary: the exact invisibility of a chessboard of clocks to clause B's coupling; the exact evenness of the sea's energy in a reach-two strain; the executed induced ledger of the free massless sea — its volume term, its clock stiffness, its near-absence of a lengths' stiffness — and what those signs do to the static law. No gravitational claim is made.

## Exact target and obligation graph

Target: what the filled sea's energy, booked as the field's term, gives. Obligations: (O1) exact invariances of `E_sea`; (O2) the many-record source; (O3) the induced second-order structure; (O4) its static law. T1, T2 discharge O1; T3 O2; T4 with the control O3, O4.

## Theorem T1 — a chessboard of clocks is invisible

*Statement.* (a) For `φ_x = c^{ε(x)}` with any `c > 0`: `φ_xφ_y = 1` on every bond, hence `φHφ = H`. (b) For any two positive rate fields with `φ_xφ_y = φ'_xφ'_y` on every bond, `φHφ = φ'Hφ'`. (c) Hence `E_sea`, every eigenvalue of `H_w`, and every second variation of `E_sea` are exactly unchanged along the chessboard mode of the rates, at any amplitude.

*Proof.* `H` has only one-step hops; `(φHφψ)(x) = φ_x Σ_y H_{xy} φ_y ψ_y`, and neighbouring sites have opposite `ε`. ∎

T1 is stated for the walk and for one-step couplings (block 62's frame, block 63's reach-two strain), whose hops carry `φ_xφ_y` across one bond. A clocked reach-three coupling, `φH₃[B]φ`, contains two-step hops carrying `φ_xφ_{x+2e_j} = φ_x²` on a chessboard, which is not invariant; the sea's invisibility is for the rates alone and for one-step couplings.

## Theorem T2 — under reach two the sea is even in the strain

*Statement.* `E_sea[H₂[−B]] = E_sea[H₂[B]]` for every strain `B`.

*Proof.* Block 70 T3(d): `U_{(111)}H₂[B]U_{(111)} = −H₂[−B]`, so the spectrum of `H₂[−B]` is minus that of `H₂[B]`; `tr H₂[B] = 0` (every term carries one of the coin's three matrices, which are traceless); hence `Σ_{E<0}` of `H₂[−B]` equals `−Σ_{E>0}` of `H₂[B]` `= E_sea[H₂[B]] − tr H₂[B]`. ∎

Under reach three the sea is not even (the control's strain polarisations are its second variations; the first variation of a uniform reach-three strain is nonzero).

## Theorem T3 — a many-record ledger and the hole

*Statement.* For two orthogonal one-record states `ψ₁, ψ₂` and `Ψ = ψ₁ ⊗ ψ₂ − ψ₂ ⊗ ψ₁`: (a) `⟨Ψ|H_w ⊗ 1 + 1 ⊗ H_w|Ψ⟩/⟨Ψ|Ψ⟩ = ⟨H_w⟩₁ + ⟨H_w⟩₂` (normalised expectations); (b) the same for the energy density at every site; (c) hence for any set of occupied orthogonal states the ledger's source at `x` is `Σ_k e^{(k)}_x`, and removing an occupied state changes it by `−e^{(k)}_x`; for a state of negative energy, whose total density is negative, the change is positive in total.

*Proof.* (a), (b): expand; the cross terms carry `⟨ψ₁|ψ₂⟩ = 0`; `⟨Ψ|Ψ⟩ = 2‖ψ₁‖²‖ψ₂‖²`. (c) By (b) and block 55 T1 applied to each occupied state. ∎

The exchange sign is the import: with symmetric composition (a) still holds, but the many-record state has no lowest energy (block 71's negative branch can be occupied without bound) and no sea. "One record per site at a time" (the Record axiom, in the owner's reading) forbids two records at a site whatever their coins — a hard-core condition — and says nothing about the sign under exchange.

## Theorem T4 — what the linearised static law does with the sea's second variation

*Statement.* Let the sea's second variation along modes be `Π(q) = c/4 + (κ/4)|q|²_lat` with declared `c < 0 < κ` and `c + 12κ < 0`. (a) The linearised static law for a unit body at the origin on a torus, with the mean removed, is `(c + κ|q|²_lat)u_q = −1/N` for `q ≠ 0`, and `u(0) = −(1/N)Σ_{q≠0}1/(c + κ|q|²_lat) > 0`: the clock at the body runs faster (repulsion). (b) With `c = 0`, `u(0) < 0` (attraction), and far away `u ≈ −1/(4πκr)`: the induced coupling in block 55's normalisation is `γ = 1/κ`. (c) By T1 the exact second variation vanishes on the chessboard mode, so the exact linearised law has a zero mode there and does not fix the clocks' chessboard component.

*Proof.* (a) Every denominator is negative since `|q|²_lat ≤ 12`. (b) Every denominator is positive; block 55 T4(c)'s law `u_x −` average `= −(γ/6)e_x` is `κ(−Δu) = −e` with `γ = 1/κ`. (c) T1(c). ∎

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block76_sea_ledger.py` (dense eigenvalues; second differences with two amplitudes). **W1** (rates): `c₀ = −1.181, −1.190, −1.192, −1.193` for `L = 6, 8, 10, 12`; the gradient part of `Π(q)` over `|q|²_lat` is `+0.0202` (L = 6), `+0.0221, +0.0234` (L = 8), `+0.0231, +0.0237` (L = 10), and at `L = 12` for six modes along `(100), (200), (300), (110), (111), (220)`: `+0.0236, +0.0239, +0.0240, +0.0238, +0.0238, +0.0237` — isotropic to 1%; **`κ = 0.0952 ± 0.0016`**. **W2** (strains under reach three, `L = 8`): gradient parts `+0.0035` (TT cross), `+0.0021` (TT plus), `+0.0004` (isotropic stretch) per `|q|²`; the local (uniform) parts `−0.020, −0.020, −0.009`. **W3**: the chessboard mode costs `0` to `1e-13` at amplitudes `0.25, 0.5, 1.0`; the modes `cos(πx)` and `cos(π(x + y))` have gradient parts exactly `|c₀|/2 × |q|²_lat/12` (`0.19836`, `0.39672`), as T1's bond-product picture predicts (such a mode is a chessboard along some axes and a uniform rate along the others). **W4**: with `c₀, κ` as measured, `u` at a unit body is `+2.01` (volume term kept), `−2.46` (removed); `c₀ + 12κ = −0.051`; `γ_ind = 10.51`.

## No-Go Discipline Gate

The note's negative sentence: the free massless sea, booked as the field's energy, does not induce the curvature member on this lattice — its second-order energy has a clock stiffness.

### N1 — Routes by which the sentence could fail or mislead
1. *A different sea.* A walker with rest energy (a staggered on-site term, `FORK_PROBE` §4.3) or a sea with several coins per site could induce a lengths' stiffness; not examined.
2. *Exponentiated couplings.* The reach-three coupling is first order in `B`; the sea's response to strain depends on the completion beyond first order (block 69 N3). The rates' coupling `φHφ` has no such ambiguity, and it is the rates' stiffness that decides the sentence.
3. *Finite size.* `κ` rises from `0.020` to `0.024` between `L = 6` and `12` and is flat across `q` and direction at `L = 12`; a limit near `0.024–0.025` per `|q|²` is indicated, not proved.
4. *Normal ordering.* Removing the uniform part of the sea's energy is a rule outside the clauses; both readings are reported.
5. *The exchange sign.* Without it there is no sea (T3's remark); the whole reading rests on an import.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even tori (the chessboard is periodic); the identity coin frame; the reach-three coupling for strains; the free walk's sea (no interaction between records beyond exclusion).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the Record axiom's one record per site | yes (premise) |
| blocks 54, 55 (open PRs #8570, #8571) | the clocked walk; the ledger's source; `γ`'s normalisation | yes (restated) |
| blocks 63, 69, 70 (open PRs #8593, #8601, #8602) | the strain couplings; the checkerboard map | yes (restated; T2 uses block 70 T3(d)) |
| block 71 (open PR #8603) | the negative branch; the fork | yes (restated) |
| `FORK_PROBE_source_link_20260922.md` | the panel's ranking and criteria | context |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a chessboard of clocks is invisible; reach-two sea even; additive source, positive hole; clock stiffness, no lengths' stiffness, repulsive with the volume term" | executed: bond products on all 192 bonds; the trace over all 128 basis states | executed: the clocked walk against the free walk at all 64 sites (two rate fields); the mirror identity at all sites; the two-record density at a site | executed: every mode's denominator sign on a `4×4×4` torus; the chessboard as exact zero; control: six modes at `L = 12` | executed: the 144-component two-record energy against the sum; the clock at a body in both readings | T1 every even lattice; T2 every strain; T3 every orthogonal pair; T4 for the declared values; `c₀`, `κ` executed only |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; the realized-state primitive supplies no filling rule. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A cutoff that breaks the symmetry between space and time always induces a `(∇N)²` term; you have rediscovered that." Reply: yes, and inside this framework the lattice is not a cutoff to be removed — the number is the framework's, and it decides which supplied member the sea would induce. Second objection: "The volume term is the cosmological-constant problem; every induced-gravity programme has it." Reply: agreed, and the note reports both readings without choosing. Third objection: "The chessboard invisibility is trivial." Reply: it is one line, and it makes the sea-as-ledger reading's static law singular; block 55–60 never met it because their field energies were supplied with their own stiffness.

### N8 — Cross-cycle echo
Block 55: the source must be the energy density. Block 56: the simplest member, half bending. Block 60/64: the curvature member, full bending, per-tick counting. Block 71: negative energies exist in the clauses. Here: if their sea is what the field's energy *is*, the framework lands back on block 56's member, with `γ = 10.5`, and with a cosmological term it cannot cancel.

## Falsifiers

- A chessboard of rates and a state with `φHφψ ≠ Hψ` at some site.
- A strain `B` with `E_sea[H₂[−B]] ≠ E_sea[H₂[B]]`.
- A torus and mode on which the rates' polarisation's gradient part is zero or negative (the control finds `+0.020–0.024` per `|q|²` on every torus and mode tried).

## Boundaries and non-claims

Whether the negative branch is filled, and the exchange sign, are not decided and are the owner's. The field's energy is not declared induced; the note shows what induction would give. Content with rest energy, several coins per site, and exponentiated couplings are outside. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice axiom; the Record axiom; the memo's silence on rates and amplitude dynamics. Blocks 54, 55, 63, 69, 70, 71 (PRs #8570, #8571, #8593, #8601, #8602, #8603, open): restated or placed.
- Named standard imports at definition level: spectra of similar matrices; traces; antisymmetric tensor products; second differences.
- Reference only: Dirac; Sakharov; Bondi.

## Review record
Supervisor-run block, the twenty-fourth of the source-link direction; the first after the fork probe of 2026-09-22 (four-lens panel; synthesis in `FORK_PROBE_source_link_20260922.md`). Lens pass, in writing, by the supervisor: a foundations lens — the reading probed rests on an exchange sign the axioms do not supply, and the note says so before anything else is built on it; a rigour lens — the exact statements (T1–T3) were separated from the executed second-order structure, whose values enter the runner only as declared rounded inputs; the chessboard invisibility was found by the control (a zero to `1e-13` at finite amplitude) and then proved in one line, after which the corner-type modes' exact factors `|q|²_lat/12` were predicted and confirmed; the clock stiffness was measured across four tori, six modes and three directions before being called nonzero. A strategy lens — the panel's first-ranked probe returns a clear negative for the completion route and a number (`γ_ind`) for the reading in which it lives. Control: as reported under Executed. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_chessboard_clocks_invisible_2026_09_22.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
