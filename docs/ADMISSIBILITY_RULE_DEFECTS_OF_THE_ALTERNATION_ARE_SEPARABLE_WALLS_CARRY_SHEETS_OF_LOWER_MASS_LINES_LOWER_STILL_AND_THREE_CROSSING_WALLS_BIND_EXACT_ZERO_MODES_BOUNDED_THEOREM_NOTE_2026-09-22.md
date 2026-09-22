---
claim_id: admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates (open PR #8581; not adopted) alternating as in block 84 (#8652), with walls where the alternation's phase slips, supplied as configurations: exact symbolic algebra on the 4³ torus (128-dimensional walk) for four wall configurations, and on the rings of four and eight; the 6³ and 8³ tori and the ring of 16 executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_lines_and_three_crossing_walls_bind_exact_zero_modes_2026_09_22.py
---

# Defects of the alternation are separable: walls carry sheets of lower mass, lines lower still, and three crossing walls bind exact zero modes

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact operator identities and nullities on the 4³ torus and on rings, holding on every even torus by their proofs; executed spectra labelled; the alternation and its walls are supplied configurations; nothing adopted or registered; unaudited)

This note works within block 59's bond rates alternating as in block 84, with walls where the alternation's phase slips; it reports the exact spectrum of the walk in the presence of such defects; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 84 (PR #8652) found that block 59's bond rates alternate on their own below a threshold stiffness, giving every species the rest energy `√3β|δ|`, and that the alternation has eight degenerate phases (the sign of `δ` on each axis) related by one-step translations. Where two phases meet the alternation's phase slips: two weak bonds in a row, or two strong ones. This note gives the walk's exact spectrum with such walls.

1. **Separable, walls included (T1).** The alternated walk is `H = Σ_j σ_j ⊗ h_j` with `h_j` acting on the `j`-th coordinate alone; the `h_j` commute and the coins anticommute, so `H² = Σ_j h_j² ⊗ 1` exactly — for any pattern of amplitudes along each axis, walls or not. Every energy squared is a sum of three one-axis energies squared.
2. **One wall, one zero mode (T2).** A one-axis operator with two walls on a ring has exactly two zero modes and none without: one per wall, each living on one sublattice and falling off from its wall by the ratio `(1 − δ)/(1 + δ)` per two sites, exactly (`7/13` at `δ = 3/10`).
3. **Sheets, lines, points (T3).** The least energy squared is the sum of the least one-axis energies squared: `δ_x² + δ_y² + δ_z²` in the bulk (block 84); a wall across `x` carries a sheet whose mass is `√(δ_y² + δ_z²)` — the two transverse alternations combined; two crossing walls carry a line of mass `|δ_z|`; three crossing walls bind states of exactly zero energy. On the `4³` torus with two walls per axis the exact nullity is `0, 0, 0, 16` for walls across none, one, two, three axes: eight crossing points, one zero mode per coin state.
4. **The zero modes are products (T4).** The sixteen zero modes are exactly the products of the three one-axis wall modes with the two coin states: each sits at a crossing point, on one sublattice of each axis, falling off by `(1 − δ_j)/(1 + δ_j)` per two sites along axis `j`.
5. **Executed (control; floating point).** On `6³` and `8³` the zero-mode counts and least energies agree with the separable prediction to every digit shown (`0.5196, 0.4243, 0.3000, 0` for equal `δ = 3/10`; `0.6164, 0.5385, 0.5000, 0` for `δ = (3/10, 1/5, 1/2)`); with walls across `x` only the whole `1024`-fold spectrum on `8³` equals `±√(e_x² + e_y² + e_z²)` over all triples to `2·10⁻¹⁴`, and the wall-bound branch is a massive two-dimensional band from `√(δ_y² + δ_z²) = 0.5385` to `√2`; on the ring of 16 the wall modes decay by `0.8182, 0.5385, 0.3333, 0.1765` per two sites at `δ = 1/10, 3/10, 1/2, 7/10`, the ratios `(1 − δ)/(1 + δ)` exactly.

So the alternation's own defects carry lighter matter: a wall a two-dimensional band with two-thirds of the bulk mass squared (for equal alternations), a line one-third, and a point a state of exactly zero energy bound where three walls cross. In plain terms: if the lattice's steps settle into long-short-long-short along every axis, then wherever the pattern stumbles — two long steps together, or two short ones — a moving record finds it cheaper to sit; on a stumbling sheet it is lighter, on a stumbling line lighter still, and at a point where the pattern stumbles in all three directions at once it costs nothing at all to be there.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 84 T5 remark: 'the eight sign patterns of the three axes are degenerate phases related by one-step translations, and a wall between them is a sheet; its modes in three dimensions are not computed here'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the defects' spectra are exact and separable; next: whether the balance of block 84 makes walls (the energy of a wall per unit area under the sea and block 59's law: does the alternation prefer domains?); the zero modes' response to the scalar hop and to a rate field (do they fall?); the owner's reading of what a bound zero-energy state is"
conditional_surface_status: "T1 by proof on every torus; T2 on the ring of eight, and on every even ring by the recurrence; T3, T4 exact on the 4^3 torus with the least-energy statement following from T1 and the one-axis bound; the alternation, its strength and its walls are supplied configurations"
hypothetical_axiom_status: "block 59's bond rates; the alternation (block 84's balance); walls as supplied configurations; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (a product of three rings) and the Qubit axiom. Blocks 54, 59, 82, 84 (open PRs #8570, #8581, #8628, #8652) supply the walk, the bond rates, the alternating-amplitude identity and the balance. Nothing is adopted here.

- **One-axis operator.** `h = (1/2i)(tT − T†t)` on a ring of `L` sites, `t_x = 1 + δ s_x(−1)^x` on the bond `x → x + 1`; `s_x = +1` everywhere (no walls) or `+1` on the first half and `−1` on the second (two walls: where `s` changes, two consecutive bonds carry the same amplitude — weak-weak at one wall, strong-strong at the other).
- **The walk with walls.** `H = Σ_j σ_j ⊗ h_j`, `h_j` the one-axis operator on the `j`-th coordinate with its own `δ_j` and its own choice of walls, embedded in the `L³` torus.
- **Zero modes.** The nullspace of `H` (exact rank over `ℚ(i)`); of `h` on a ring.
- **Least energy.** `min|E|` over the spectrum; by T1, `E² = e_x² + e_y² + e_z²` for one-axis energies `e_j`.
- **Control.** Dense spectra on `6³`, `8³`; the ring of 16.

That a slip of a dimerisation binds a mid-gap state on one sublattice with exponential fall-off is the soliton of Su, Schrieffer and Heeger (and the zero mode of Jackiw and Rebbi); that the intersection of three such defects in three dimensions binds a zero-energy state is the lattice form of a zero mode at a point defect of a mass with three independent sign changes; none is used as authority.

## Prior art and what is new

Block 82 T3(a) gave the alternated walk's `H²` for a uniform alternation; block 84 T5 the two zero modes of a ring with two walls (with the coin). New, inside the framework's vocabulary: that the separability holds with walls on any axes, so every defect's spectrum is a sum of one-axis spectra; the exact structure of the one-axis wall modes (sublattice, ratio `(1 − δ)/(1 + δ)`); the sheet, line and point masses `√(δ_y² + δ_z²)`, `|δ_z|`, `0`; and the exact sixteen product zero modes on the `4³` torus. No gravitational claim is made.

## Exact target and obligation graph

Target: the walk's spectrum with walls in the alternation. Obligations: (O1) separability with walls; (O2) the one-axis wall modes; (O3) the least energies by wall configuration and the zero-mode counts; (O4) the zero modes' form. T1–T4 discharge O1–O4.

## Theorem T1 — separable, walls included

*Statement.* For any amplitudes `t_j(x_j)` along each axis (walls or none), `H² = Σ_j h_j² ⊗ 1`.

*Proof.* `h_j` acts on the `j`-th coordinate only, so `[h_j, h_l] = 0`; `σ_jσ_l = −σ_lσ_j` for `j ≠ l`; the cross terms of `(Σσ_j ⊗ h_j)²` cancel in pairs and `σ_j² = 1`. Family B checks the identity exactly on `4³` for four wall configurations with `δ = (3/10, 1/5, 1/2)`. ∎

## Theorem T2 — one wall, one zero mode on one sublattice

*Statement.* On the ring of eight with `δ = 3/10` and two walls (amplitudes `13/10, 7/10, 13/10, 7/10, 7/10, 13/10, 7/10, 13/10`), `h` has exactly two zero modes and none without walls. One lives on the even sites, peaked at the weak-weak wall, the other on the odd sites, peaked at the strong-strong wall; along its sublattice each falls off from its wall by the ratio `(1 − δ)/(1 + δ) = 7/13` per two sites, exactly.

*Proof.* `hψ = 0` reads `t_xψ(x + 1) = t_{x−1}ψ(x − 1)`: a two-term recurrence on each sublattice with ratio `t_{x−1}/t_x`, which is `(1 ∓ δ)/(1 ± δ)` and flips at a wall; a normalisable solution on the ring exists on the sublattice that decays away from its wall in both directions, one per wall. Family C: exact nullspace and ratios. ∎

## Theorem T3 — sheets, lines and points

*Statement.* By T1 the least `E²` is `Σ_j min e_j²`. Without walls on axis `j`, `e_j² = sin²k_j + δ_j²cos²k_j ≥ δ_j²`, attained (on even rings) at `k_j ∈ {0, π}`; with walls, `min e_j² = 0` (T2). Hence: bulk `δ_x² + δ_y² + δ_z²`; a wall across `x` carries a sheet of mass `√(δ_y² + δ_z²)`; two crossing walls a line of mass `|δ_z|`; three crossing walls a point of zero energy. On the `4³` torus with two walls per axis and `δ = (3/10, 1/5, 1/2)`: nullities `0, 0, 0, 16` for walls across none, one, two, three axes; least `E² = 19/50, 29/100, 1/4, 0`.

*Proof.* T1, T2 and the one-axis bound; family D computes the exact ranks of the `128`-dimensional walk and the one-axis spectra on the ring of four (`±δ_j, ±1` without walls; containing `0` with). ∎

## Theorem T4 — the zero modes are products

*Statement.* On the `4³` torus with two walls per axis, the sixteen vectors `(one-axis wall mode along x) ⊗ (along y) ⊗ (along z) ⊗ (coin state)` are annihilated by the walk and are linearly independent: they are its whole nullspace.

*Proof.* `H` applied to a product of one-axis zero modes gives `Σ_j σ_j ⊗ (h_jψ_j = 0)` termwise; the sixteen products are independent since each one-axis pair is; by T3 the nullity is sixteen. Family E. ∎

*Remark.* Each zero mode is bound at one of the `2³` crossing points, on one sublattice of each axis, falling off by `(1 − δ_j)/(1 + δ_j)` per two sites along axis `j`; the two coin states are degenerate.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block86_defects.py`, output in `.out.txt`; disjoint machinery: dense floating-point spectra).

*W1 — counts and least energies.* On `6³` and `8³`, for `δ = (3/10, 3/10, 3/10)` and `(3/10, 1/5, 1/2)`, walls across none, one, two, three axes: zero modes `0, 0, 0, 16` in every case; least `|E| = 0.5196, 0.4243, 0.3000, 0` and `0.6164, 0.5385, 0.5000, 0`, the separable predictions to four places.

*W2 — the whole spectrum with walls across `x`.* On `8³` (`δ = (3/10, 1/5, 1/2)`) the `1024` energies equal `±√(e_x² + e_y² + e_z²)` over all triples of one-axis energies to `2·10⁻¹⁴`; `h_x` has two zero modes; the wall-bound branch runs from `0.5385 = √(δ_y² + δ_z²)` to `√2`: a massive two-dimensional band whose mass is the transverse alternations combined.

*W3 — decay on the ring of 16.* The wall modes fall off per two sites by `0.8182, 0.5385, 0.3333, 0.1765` at `δ = 1/10, 3/10, 1/2, 7/10`: `(1 − δ)/(1 + δ)` to four places (the strong-strong mode has two equal peak sites, ratio `1` between them).

## No-Go Discipline Gate

The note's negative sentences: without walls there are no zero modes; a wall across one or two axes leaves a gap.

### N1 — Routes by which the sentences could fail or mislead
1. *Sharp walls only.* The walls are sharp slips of the alternation (two equal bonds in a row); a smooth wall (the alternation's amplitude passing through zero over several sites) binds the same modes in the comparator but is not computed here.
2. *Walls as supplied.* Whether the balance of block 84 makes walls — their energy per unit area under the sea and block 59's law — is not examined; the walls here are configurations.
3. *The zero modes' physics.* A bound state of exactly zero energy is, in the lane's language, content at rest with no rest energy; what it is (a record that has stopped? a particle?) is the owner's reading and not claimed.
4. *The scalar hop.* With the axioms' scalar hop through the same bonds (block 84 T4) the one-axis operators are no longer of the pure alternating form; separability of `H²` needs the cross terms to cancel, which the scalar hop's commutation with the coin does not give. Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Even tori and rings; two walls per axis (a ring needs an even number); `δ = (3/10, 1/5, 1/2)` in the exact checks (the identities are algebraic in `δ`).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice axiom (product of rings); the coin | yes (premise) |
| blocks 54, 59 (open PRs #8570, #8581) | the walk; the bond rates | yes (restated) |
| blocks 82, 84 (open PRs #8628, #8652) | the alternating identity; the balance and the phases | yes (placed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "separable with walls; one zero mode per wall on one sublattice with ratio (1 − δ)/(1 + δ); sheet, line, point masses; sixteen product zero modes" | executed: `H²` entry by entry for four configurations | executed: wall-mode amplitudes at every site | executed: one-axis spectra; control on `6³`, `8³`, ring of 16 | executed: exact nullities; the rank of the products | T1 by proof; T2 by the recurrence; T3, T4 on `4³` with T1

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Product structure makes this trivial; the walk is three decoupled chains." Reply: the coin couples them — the spectrum is not a sum of energies but a sum of energies *squared*, which is why a wall lowers the mass without removing it and only three crossings give zero; the exactness is the content. Second objection: "Walls cost energy and will not form." Reply: not examined here and said so (N1.2); the block gives what walls carry if they are there.

### N8 — Cross-cycle echo
Block 79: a wall in the chessboard mass binds zero modes when the defect layer is odd. Block 84: the alternation's eight phases; two zero modes per pair of walls on a ring. Here: with walls the spectrum is separable; sheets, lines, points; sixteen exact zero modes.

## Falsifiers

- A wall configuration on any torus with `H² ≠ Σ_j h_j² ⊗ 1`.
- A ring with two walls whose one-axis operator has other than two zero modes, or a wall mode not confined to one sublattice or not decaying by `(1 − δ)/(1 + δ)` per two sites.
- A `4³` torus with two walls per axis whose walk has other than sixteen zero modes, or a zero mode outside the span of the products.

## Boundaries and non-claims

Sharp walls as supplied configurations; no wall energy; no scalar hop; the zero modes' meaning not claimed. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 54, 59, 82, 84 (open PRs): restated or placed.
- Named standard imports at definition level: exact nullspaces and ranks over `ℚ(i)`; two-term recurrences; dense diagonalisation for the control.

## Review record
Supervisor-run block, the thirty-fourth of the source-link direction; the fifth after the rest-energy panel. Lens pass, in writing, by the supervisor: a foundations lens — walls are supplied, their energy is not computed, and the zero modes are not given a physical name; a rigour lens — the separability was checked as an exact operator identity with walls on every subset of axes and unequal `δ_j` (not inferred from the wall-free case), the one-axis wall modes were solved exactly and their ratios read off, and the sixteen zero modes were shown to be the products by exact rank rather than by count alone. Mutation census: seven mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_lines_and_three_crossing_walls_bind_exact_zero_modes_2026_09_22.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
