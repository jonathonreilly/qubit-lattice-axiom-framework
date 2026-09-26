---
claim_id: admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates and bond law (open PR #8581; not adopted), block 54's walk (#8570), block 82's alternating-amplitude identity (#8628) and the sea reading of block 76 (#8611) taken as a comparator: exact symbolic identities on the 16-dimensional block of the species at every wave vector, block 59's 3×3 law at the alternation wave vectors, the second-order balance in closed form, exact nullities on the ring of 12; the zone average chi, the curve E(delta), delta* against kappa and the least |E| with the scalar hop executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_sea_against_bond_law_one_rest_energy_2026_09_22.py
---

# Bond rates alternate on their own below a threshold stiffness: the sea against block 59's bond law gives every species one rest energy

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact identities and a closed-form balance; the balance's minimisation and the sea are comparator premises; the zone average and the curves are executed; nothing adopted or registered; unaudited)

This note works within block 59's bond rates and bond law and the sea reading of block 76 taken as a comparator; it reports the exact balance between the sea's gain and the bond law's stiffness under an alternation of the bond rates, and what the alternation gives the walk; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 82 (PR #8628) found that an alternation of the hop amplitudes gives every one of the walk's eight species the rest energy `√3β|δ|`; block 83 (PR #8632, corrigendum) found that the lane's lengths of blocks 61–64 cannot supply it, but that block 59's bond crossing rates — `H = Σ_b c_b h_b`, the hop across each bond timed by that bond's own rate — are exactly such an amplitude, sourced by the hop energy they time. This note asks whether block 59's bond rates alternate on their own. Under the sea reading they do, below a threshold of the bond law's stiffness, and the balance is in closed form.

1. **The sea's energy under an alternation, exactly (T1).** With independent alternations `δ_j` of the bond rates along the three axes, `H² = β²Σ_j(sin²k_j + δ_j²cos²k_j)` on the whole 16-dimensional block of the species at every reduced wave vector. So the sea's energy per site is exactly minus the zone average of `√(Σ_j sin²k_j + Σ_j δ_j²cos²k_j)`: even and concave in every `δ_j`, equal to `−√3` at `δ = 1` (the lattice fallen into disconnected `2×2×2` cubes with flat bands), and with the second-order coefficient `χ = ⟨Σ_j cos²k_j / √(Σ_j sin²k_j)⟩` on all three axes together, `χ/3` per axis.
2. **What block 59's law charges for it (T2).** At the alternation wave vector `πe_j` the bond law's `3×3` matrix has the bonds along `j` as an eigenvector with restoring coefficient `4α + 8β`, decoupled from the other two axes and independent of the parallel coupling `γ`; the alternation costs `2(α + 2β)δ_j²` per bond. The long-range stiffness of block 59 T3 is `α + 2β + 2γ`: two different combinations of the three numbers, and `γ` separates them.
3. **The threshold (T3).** Per site, to second order, the balance is `(6κ − χ/2)δ²` with `κ = α + 2β` for the three axes together and `(2κ − χ/6)δ_j²` for one axis: the uniform bond-rate field is a local minimum iff `κ ≥ χ/12`, and below it the rates alternate. Executed: `χ = 1.5381` (midpoint grids of side 16 to 128, settled to four places), so `κ_c = 0.1282` in units of the hop `β = 1`.
4. **What the alternation gives the walk.** Every species the rest energy `√3β|δ*|` (block 82 T3(a)), with `δ*` fixed by the balance; executed: `δ* = 0.10, 0.18, 0.33, 0.48` at `κ = 0.125, 0.120, 0.110, 0.100` and `δ* = 1` for `κ < 0.0897` (the concave gain beats the quadratic cost outright). The onset at `κ_c` is continuous; a rest energy small against the hop needs `κ` within a few per cent below `κ_c`. With the axioms' scalar hop timed by the same bond rates the corner energies cross zero exactly at `δ = 2a/β` (T4), and the rest energy survives only above that (executed least `|E|`).
5. **Walls (T5).** On a ring, a wall between the two alternation phases binds exactly two zero modes (four on the ring of 12 with two walls, none without): the lattice form of block 79's wall modes for this background, and the eight sign patterns of the three axes are eight degenerate phases related by one-step translations.

So, under the sea reading, a rest energy for all eight species is *derived* from a balance the lane already carries — block 59's bond rates sourced by the hop energy they time, against the bond law's stiffness — with one condition on block 59's supplied numbers: `α + 2β < χ/12`. What is supplied is the sea (a comparator, block 78), the bond law's three numbers, and the reading of the static balance as a minimisation; what is not tuned by anything is the size of the rest energy, which is of the order of the hop unless `κ` sits just below the threshold. In plain terms: if the ticking of the bonds is soft enough, the lattice settles into long-short-long-short steps along every axis, and every moving record then carries the same fixed cost of being at rest; how heavy depends on how soft the bonds are, and it is heavy unless they are barely soft enough.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 83 (PR #8632, corrigendum): 'whether block 59's bond rates alternate spontaneously - the sea's exact gain against the bond law's stiffness - is the next block'; decision record row 48"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the balance is closed-form: alternation below kappa = alpha + 2 beta < chi/12 (chi = 1.5381 executed), rest energy sqrt(3) beta |delta*| for all eight species; next: the same balance for the hard-core crowd instead of the free sea (block 80's machinery on small tori); the 3D wall sheets between alternation phases; whether block 59's other two combinations (long-range stiffness, gamma) are constrained elsewhere in the lane; the owner's reading of the sea"
conditional_surface_status: "T1, T2, T4 exact for every wave vector; T3 exact at second order with chi an executed number; T5 exact on the ring of 12; the curves are the control's; the minimisation of E_sea + F and the sea itself are comparator premises"
hypothetical_axiom_status: "block 59's bond rates and their law; the sea; the static balance as a minimisation; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom (sites, bonds, translations, proper rotations) and the Qubit axiom, and its silence on a time metric, amplitude dynamics and a conserved energy. Blocks 54, 59, 76, 82, 83 (open PRs #8570, #8581, #8611, #8628, #8632) supply the walk, the bond rates and their law, the sea reading, the alternating-amplitude identity and its scope. Nothing is adopted here.

- **Bond rates and the walk (block 59).** `H = Σ_b c_b h_b`, `h_b = (i/2)σ_j(|y⟩⟨x| − |x⟩⟨y|)` on the bond from `x` to `y = x + e_j`; uniform rates give block 54's walk with `β = 1`. **Alternation:** `c_b = 1 + δ_j(−1)^{x_j}` on the bonds along `j`.
- **The 16-dimensional block.** The three doublings `k → k + πe_j`; on the `j`-th pair the σ-hop is `β(−sin k_j τ_z + δ_j cos k_j τ_y)` (block 82 T3(a)); the scalar hop through the same bonds `2a(cos k_j τ_z + δ_j sin k_j τ_y)`.
- **The sea (comparator).** `E_sea = Σ_{E<0}E` of the one-record generator; per site, `E(δ)`. Block 78: the axioms' records compose under exclusion; the free sea is a comparator.
- **Block 59's bond law (T3 there).** `c₀u_b + αΣ_coll u + βΣ_perp u + γΣ_par u = s_b` with the shift symmetry `c₀ = −2α − 8β − 4γ` (block 59 writes `δ` for the parallel coupling; here `γ`, to keep `δ` for the alternation); its `3×3` matrix `M(k)` on the three bond fields, `M_jj = c₀ + 2α cos k_j + 2γΣ_{l≠j}cos k_l`, `M_jl = 4β cos(k_j/2)cos(k_l/2)`; the field energy whose stationarity is the law, `F = −½ Σ_k u(k)†M(k)u(k)`, positive on the long-range scalar (stiffness `α + 2β + 2γ`, block 59).
- **The balance.** The static configuration extremises `E_sea + F`; a local minimum of the uniform field means the second-order form is non-negative.
- **Zone averages.** `⟨f⟩ = (2π)⁻³∫f d³k`; `χ = ⟨Σ_j cos²k_j / √(Σ_j sin²k_j)⟩` (finite: the integrand is `∝ 1/|q|` near the corners).
- **Walls.** On a ring, `c_x = 1 + δ s_x(−1)^x` with `s_x = ±1` on two halves: two walls.

That a half-filled band on a lattice lowers its energy by alternating the bond amplitudes, at any stiffness in one dimension and below a threshold in three, is the instability of Peierls and the dimerisation of Su, Schrieffer and Heeger, with its solitons; that the second-order coefficient of a gapless band with vanishing density of states is finite in three dimensions and the onset is continuous with a logarithmic correction is the usual Landau-type expansion; the zone average with the singular integrand is of the kind evaluated by Watson. None is used as authority.

## Prior art and what is new

Block 59 gave the bond rates, their sourcing by the hop energy, and the three-number law; block 82 the alternating-amplitude identity for equal `δ`; block 83 the concavity and evenness of the sea's energy and the corrigendum placing the coupling in block 59. New, inside the framework's vocabulary: the identity with three independent alternations and the resulting closed form for the sea's energy at every strength; the bond law's exact response to the alternation (`4α + 8β`, decoupled, `γ`-free) against its long-range stiffness; the closed-form threshold `κ_c = χ/12` and the executed value; the corner crossing `δ = 2a/β` with the scalar hop; the exact wall zero modes. No gravitational claim is made.

## Exact target and obligation graph

Target: whether block 59's bond rates alternate spontaneously under the sea, and what that gives the walk. Obligations: (O1) the sea's energy as a function of the alternation; (O2) the bond law's cost; (O3) the balance and its threshold; (O4) the scalar hop; (O5) walls. T1–T5 discharge O1–O5 at the stated scope.

## Theorem T1 — the sea's energy under an alternation of the bond rates, in closed form

*Statement.* With `c_b = 1 + δ_j(−1)^{x_j}` on the bonds along `j` (independent `δ_j`), the 16-dimensional block obeys `H² = β²Σ_j(sin²k_j + δ_j²cos²k_j)` at every reduced wave vector. Hence every energy is `±β√(Σ_j sin²k_j + Σ_j δ_j²cos²k_j)`, and the sea's energy per site is `E(δ) = −β⟨√(Σ_j sin²k_j + Σ_j δ_j²cos²k_j)⟩`: even and concave in each `δ_j`; `E = −√3β` when every `δ_j = ±1`.

*Proof.* The `j`-th pair operator `h_j = β(−sin k_j τ_z^{(j)} + δ_j cos k_j τ_y^{(j)})` squares to `β²(sin²k_j + δ_j²cos²k_j)`; the `h_j` act on different pairs and commute; the `σ_j` anticommute; cross terms cancel (family B, symbolic, three independent `δ_j`). Evenness and concavity pointwise: block 83 T3. At `δ_j = ±1`, `sin² + cos² = 1` on every axis (family B on the `4³` grid, exactly `√3`). ∎

## Theorem T2 — what block 59's law charges for the alternation

*Statement.* At `k = πe_1`, `M = diag(−4α − 8β, [[−8β − 4γ, 4β], [4β, −8β − 4γ]])`: the alternation of the bonds along their own axis is an eigenvector of block 59's law with restoring coefficient `4α + 8β`, decoupled from the other two axes and independent of `γ`; its field energy is `2(α + 2β)δ_j²` per bond. The three alternations `πe_j` are three different wave vectors and do not mix at quadratic order. At long wavelength `(1,1,1)ᵀM(1,1,1) = −(α + 2β + 2γ)q²`, block 59's scalar stiffness. A single chessboard wave vector `(π, π, π)` for all three bond fields is a different pattern with coefficient `4α + 8β + 8γ`.

*Proof.* Substitution in block 59 T3's matrix (family C, symbolic). ∎

## Theorem T3 — the balance and its threshold

*Statement.* Per site, to second order in the alternation, `E_sea + F = E(0) + Σ_j (2κ − χ/6)δ_j²` with `κ = α + 2β` and `χ = ⟨Σ_j cos²k_j/√(Σ_j sin²k_j)⟩`; for equal `δ_j = δ`, `(6κ − χ/2)δ²`. The uniform bond-rate field is a local minimum of the balance iff `κ ≥ χ/12`; below it the field alternates, along one axis or all three alike (the per-axis coefficient is `χ/3` by the cubic symmetry and the axes are independent at this order). Because `E(δ)` is concave and even, below the threshold the minimum lies at a `δ* > 0` fixed by the full balance, and at `κ = 0` it runs to `δ = 1`.

*Proof.* T1 gives `E''(0) = −χ` on three axes (`−χ/3` on one, the cyclic permutation of the axes carrying the single-axis integrand to its partners, family D), T2 gives the cost; the threshold is the vanishing of the second derivative (family D, symbolic). Concavity: `∂²/∂δ²[−√(s² + δ²c²)] = −s²c²/(s² + δ²c²)^{3/2} ≤ 0` pointwise (family D). ∎

*Executed.* `χ = 1.52588, 1.53525, 1.53751, 1.53793, 1.53808` on midpoint grids of side `16, 32, 64, 96, 128` (`χ_1 = χ/3` to every digit): `χ = 1.538`, `κ_c = 0.1282`. The full balance (control W2): `δ* = 0.016, 0.098, 0.18, 0.33, 0.48, 0.56, 0.64, 0.73` at `κ = 0.128, 0.125, 0.120, 0.110, 0.100, 0.095, 0.090, 0.085`, and `δ* = 1` for `κ < 0.0897 = −(E(1) − E(0))/6`.

## Theorem T4 — the scalar hop through the same bond rates

*Statement.* With the axioms' scalar hop `a` timed by the same bond rates (block 82 D2's corner spectrum), the corner energies `±4a ∓ √(4a² + 3β²δ²)` vanish exactly at `δ = 2a/β`.

*Proof.* `16a² = 4a² + 3β²δ²` (family E, symbolic). ∎

*Executed.* Least `|E|` over the zone (control W3): at `a = 1/20` it is `0.008` at `δ = 0.05`, `0` at `δ = 0.1 = 2a`, then `0.069, 0.154, 0.325, 0.670, 1.016` at `δ = 0.15, 0.2, 0.3, 0.5, 0.7`; at `a = 1/10` it stays below `0.001` up to `δ = 0.2 = 2a` and is `0.126, 0.474, 0.822` at `δ = 0.3, 0.5, 0.7`. With the scalar hop present the alternation's rest energy is present only for `δ* > 2a/β`, and reduced below `√3βδ*`.

## Theorem T5 — walls between the alternation phases bind exact zero modes

*Statement.* On the ring of 12 with `c_x = 1 + δ s_x(−1)^x`, `δ = 3/10`, `s_x = +1` on one half and `−1` on the other (two walls), the walk has exactly `4` zero modes; with `s_x ≡ 1` it has none.

*Proof.* Exact rank of the `24 × 24` matrix (family E). ∎

*Remark.* Each wall carries two (one per coin state); the eight sign patterns of the three axes on `Z³` are degenerate phases related by one-step translations, and a wall between them is a sheet; its modes in three dimensions are not computed here.

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block84_bond_rate_alternation.py`, output in `.out.txt`; disjoint machinery: floating-point zone sums on midpoint grids and `16 × 16` blocks).

*W1 — the zone average.* `χ` on midpoint grids of side `16, 32, 64, 96, 128`: `1.52588, 1.53525, 1.53751, 1.53793, 1.53808`; `χ_1 = χ/3` to every digit; `κ_c = χ/12 = 0.12817`.

*W2 — the balance.* `E(δ)` per site (`64³`): `−1.1938, −1.2014, −1.2233, −1.3035, −1.4913, −1.7321` at `δ = 0, 0.1, 0.2, 0.4, 0.7, 1`; `E(1) − E(0) = −0.5383`; runaway to `δ* = 1` for `κ < 0.0897`.

| `κ = α + 2β` | `0.130` | `0.128` | `0.125` | `0.120` | `0.110` | `0.100` | `0.090` | `0.085` | `0.060` |
|---|---|---|---|---|---|---|---|---|---|
| `δ*` | `0` | `0.016` | `0.098` | `0.18` | `0.33` | `0.48` | `0.64` | `0.73` | `1` |
| rest energy `√3δ*` | `0` | `0.028` | `0.17` | `0.32` | `0.57` | `0.83` | `1.11` | `1.27` | `1.73` |

*W3 — with the scalar hop.* Least `|E|` over a `20³` grid, `a = 1/20, 1/10, 1/4`: zero (to the grid) at `δ = 2a` and below, opening above it (`0.325` at `a = 1/20, δ = 0.3`; `0.474` at `a = 1/10, δ = 0.5`; `0.277` at `a = 1/4, δ = 0.7`).

## No-Go Discipline Gate

The note's negative sentences: above the threshold the uniform bond-rate field is a local minimum (no spontaneous alternation); below the runaway value the alternation is complete; with the scalar hop the alternation gives no rest energy below `δ = 2a/β`.

### N1 — Routes by which the sentences could fail or mislead
1. *The sea.* The balance uses the one-record sea (all negative energies filled) as the source; the axioms' records compose under exclusion (block 78), and the crowd's response could differ in size and sign. Comparator premise, named as such.
2. *Minimisation.* "Static balance = minimum of `E_sea + F`" is a reading; the ledger fixes stationarity, not which stationary point.
3. *Other patterns.* Only the three axis alternations (and the `(π,π,π)` chessboard of bond fields at quadratic order) are examined; incommensurate or mixed patterns could have lower thresholds. Not excluded.
4. *Higher order.* The onset is continuous with a logarithmic fourth-order term (the fourth derivative of `E` at `0` diverges as `⟨c⁴/|s|³⟩`); the executed `δ*(κ)` is the full curve, not the expansion.
5. *The three numbers.* `α + 2β` is not fixed by anything in the lane; the result is a condition, not a value.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
`β = 1` in the executed parts; midpoint grids; the ring of 12 for walls; the scalar hop's `a₀` dropped.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice and Qubit axioms | yes (premise) |
| block 59 (open PR #8581) | the bond rates, their sourcing, the three-number law | yes (restated) |
| blocks 82, 83 (open PRs #8628, #8632) | the alternating-amplitude identity; concavity and evenness; the corrigendum | yes (restated) |
| block 76 (open PR #8611), block 78 (#8613) | the sea reading and its status as a comparator | yes (comparator premise) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sea's energy in closed form; the law's cost `4α + 8β`; threshold `κ = χ/12`; corner crossing `δ = 2a/β`; wall zero modes" | executed: the law's `3×3` at three wave vectors; the 16-block's square | executed: the cost per bond; the ring bond by bond | executed: the zone average at `δ = 1` exactly; control grids | executed: the balance symbolically; nullities | T1, T2, T4 by identity; T3 at second order with `χ` executed; T5 on the ring of 12

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "This is the Peierls instability with a threshold; the rest energy is a fitted number in disguise (`κ`)." Reply: the threshold and the curve are derived; `κ` is one of block 59's three supplied numbers, and the note says the rest energy's size is not fixed by anything — it is heavy unless `κ` is just below `κ_c`. What the note adds is that the lane already contains every ingredient, and that the alternation is the only field-based route left after blocks 81–83. Second objection: "The sea is not the axioms' state." Reply: agreed and stated; the crowd's balance is the next block.

### N8 — Cross-cycle echo
Block 59: bond rates sourced by the hop energy they time. Block 82: alternating amplitudes give one rest energy. Block 83: the lengths of blocks 61–64 cannot; block 59's rates can. Here: whether they do, and when.

## Falsifiers

- A wave vector at which `H² ≠ β²Σ_j(sin²k_j + δ_j²cos²k_j)` for independent `δ_j`.
- A wave vector `πe_j` at which block 59's matrix does not have the own-axis alternation as an eigenvector with coefficient `4α + 8β`, or at which it depends on `γ`.
- A second-order balance whose threshold is not `κ = χ/12`.
- A ring with two walls whose walk has other than four zero modes.

## Boundaries and non-claims

The sea is a comparator; the balance is read as a minimisation; three patterns only; `κ` is not fixed; the size of the rest energy is not derived; three-dimensional wall sheets are not computed. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Lattice and Qubit axioms. Blocks 54, 59, 76, 78, 82, 83 (open PRs): restated or placed.
- Named standard imports at definition level: block matrices and exact symbolic algebra; second-order expansions of zone averages; midpoint-rule zone sums for the control; exact ranks.

## Review record
Supervisor-run block, the thirty-second of the source-link direction; the third after the rest-energy panel; built after the corrigendum to block 83 that placed the bond-amplitude coupling in block 59. Lens pass, in writing, by the supervisor: a foundations lens — the sea is a comparator and the balance a reading, both said so; block 59's `δ` renamed `γ` to keep the alternation's `δ`; a rigour lens — the three-axis identity was re-derived with independent `δ_j` before use (the cross terms cancel by the coins' anticommutation, not by equal `δ`), block 59's matrix was evaluated symbolically rather than by hand, the single-axis coefficient was checked against the cyclic-permutation argument, and the concavity was made pointwise. Mutation census: seven mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_sea_against_bond_law_one_rest_energy_2026_09_22.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
