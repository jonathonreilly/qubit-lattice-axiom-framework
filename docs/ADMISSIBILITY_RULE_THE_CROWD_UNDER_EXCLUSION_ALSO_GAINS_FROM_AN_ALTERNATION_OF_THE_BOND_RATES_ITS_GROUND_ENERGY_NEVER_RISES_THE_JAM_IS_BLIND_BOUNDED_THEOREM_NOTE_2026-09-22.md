---
claim_id: admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_its_ground_energy_never_rises_the_jam_is_blind_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN block 59's bond rates (open PR #8581; not adopted), block 80's composition of records under the Record axiom's exclusion (#8615), block 84's balance (#8652) and the free sea of block 76 (#8611) taken as a comparator: exact symbolic algebra on the compressed generators of one to four records on the ring of four; the crowd's ground energies on the 2D tori 3×3, 4×3, 4×4 executed only"
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_ground_energy_never_rises_jam_blind_2026_09_22.py
---

# The crowd under exclusion also gains from an alternation of the bond rates: its ground energy never rises, and the jam is blind

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements for records under exclusion on rings, holding on every even torus by their proofs; the crowd's coefficients on small two-dimensional tori executed; nothing adopted or registered; unaudited)

This note works within block 59's bond rates, block 80's composition of records under exclusion and the free sea taken as a comparator; it reports whether the crowd of records, and not only the sea, gains from an alternation of the bond rates; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 84 found that under the free sea block 59's bond rates alternate spontaneously below a threshold stiffness, giving all eight species one rest energy — with the sea a comparator, since the axioms' records compose under exclusion (block 78). This note asks whether the crowd of records under exclusion gains from the alternation too.

1. **The crowd's ground energy never rises (T1).** At every filling, translation by one site carries the compressed generator at `+δ` exactly to the one at `−δ` (checked on the ring of four for one, two and three records), so the crowd's ground energy is even in `δ`; being the minimum of affine functions of `δ`, it is concave; a concave even function is largest at `δ = 0`. Two records on the ring of four: `−√2` at `δ = 0` and `−√218/10` at `δ = 3/10`, exact algebraic numbers, the second lower.
2. **The sea's own filling is a jam, which is blind (T2).** Under an alternation no one-record energy vanishes (`E² ≥ 2δ²` in two dimensions, `3δ²` in three), so exactly half the one-record states are negative and the free sea fills one record per site. With a record on every site the compressed generator is exactly zero: the jam feels no bond rate at all. The sea's filling has no crowd counterpart that could gain or lose; the crowd's balance is a statement about fillings below the jam.
3. **A single record gains nothing (T3).** On the ring of four one record's lowest energy is exactly `−1` at `δ = 1/10, 3/10, 1/2` (its energies are `±|δ|, ±1`): the gain that drives the alternation belongs to a filled sea or a crowd, not to a walker.
4. **Executed (control; floating point).** On the tori `3×3`, `4×3`, `4×4` the crowd's ground energy per site falls under the alternation at every filling below the jam, with the same sign as the free sea's and a smaller size: fitting `E(δ) − E(0) = A|δ| + Bδ²` on `δ ≤ 0.3`, the quadratic coefficient is `−0.19, −0.09` (`3×3`, `4` and `6` of `9` records), `−0.30, −0.12` (`4×3`, `6` and `8` of `12`), `−0.03` (`4×4`, `4` of `16`) against the free sea's `−0.35, −0.35, −0.24`; the linear parts, from these small tori's exact zero modes, have the same sign. On `3×3` the coefficient grows with filling to `5` records and falls to zero at the jam.

So the direction of block 84's balance survives the axioms' composition: the crowd lowers its energy under the alternation as the sea does, by a smaller amount that depends on the filling. The threshold stiffness for the crowd is therefore lower than the sea's `χ/12`, by a factor the small tori put between a tenth and nine tenths, and the three-dimensional value is not computed. In plain terms: it is not only an imagined full sea that prefers long-short-long-short bonds; a crowd of actual records, none sharing a site, prefers them too, just less strongly, and a lattice packed solid prefers nothing.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 84: 'the same balance for the hard-core crowd instead of the free sea (block 80's machinery on small tori)'; N1.1 of block 84 (the sea as comparator)"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the crowd gains too (exact: even and concave; executed: quadratic coefficients a tenth to nine tenths of the sea's on 2D tori); next: the crowd's coefficient in three dimensions (out of exact reach; a sampling or a larger sparse computation), the size of the rest energy at the crowd's threshold, the 3D wall sheets, and the owner's reading of which filling the lattice carries"
conditional_surface_status: "T1 by proof at every filling on every even torus (translation and the minimum-of-affine argument) with exact instances on the ring of four; T2 by block 84 T1's bound and an exact zero generator; T3 exact on the ring of four; the crowd's coefficients are the control's on three small 2D tori"
hypothetical_axiom_status: "block 59's bond rates; records composing under exclusion with the anticommuting sign (block 80's import); the balance as a minimisation; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the Qubit axiom and the Record axiom (one record per site at a time, in the owner's reading). Blocks 59, 76, 78, 80, 84 (open PRs #8581, #8611, #8613, #8615; block 84 #8652) supply the bond rates, the sea reading and its status, the compressed generator and the balance. Nothing is adopted here.

- **Ring walk with alternating bond rates.** `H = (1/2i)(t_xT − T†t_x) ⊗ σ_x` on the ring of four, `t_x = 1 + δ(−1)^x` on the bond `x → x + 1` (block 84 T5); mode index `2x + coin`.
- **Compressed generator (block 80).** For `n` records with anticommuting composition, the generator `Σ_slots H` restricted to configurations with the records on distinct sites, in the antisymmetric basis of `n`-subsets of modes with distinct sites.
- **Translation.** `T` shifts every mode by one site (`o → o + 2 mod 2L`), with the sign of the re-ordering.
- **Two-dimensional tori (control).** `H = Σ_{a=x,y} (1/2i)(t_aT_a − T_a†t_a) ⊗ σ_a`, `t_a = 1 + δ(−1)^{x_a}`; block 80's sparse ground states.
- **The fit.** `E(δ) − E(0) = A|δ| + Bδ²` on `δ ∈ {0.05, 0.1, 0.2, 0.3}`; on these small tori the free walk has exact zero modes that split linearly in `δ`, which is `A`.

That the ground energy of a Hamiltonian affine in a parameter is a concave function of that parameter is the variational principle in its simplest form; that a filled band of hard-core particles on a bipartite lattice lowers its energy under dimerisation as free fermions do, with a reduced coefficient, is the comparator of the Peierls instability in interacting chains and the spin-Peierls effect; none is used as authority.

## Prior art and what is new

Block 80 gave the compressed generator and its symmetries; block 83 T3 the concavity and evenness of the free sea's energy; block 84 the sea's balance. New, inside the framework's vocabulary: the same concavity and evenness for the crowd at every filling under exclusion, with exact algebraic instances; the observation that the sea's own filling under an alternation is the jam, which is blind; that a single record gains nothing on the ring; and the executed crowd coefficients against the sea's on three tori. No gravitational claim is made.

## Exact target and obligation graph

Target: whether the crowd under exclusion gains from the alternation. Obligations: (O1) the sign of the crowd's response at every filling; (O2) the sea's filling under exclusion; (O3) the single record; (O4) sizes. T1–T3 discharge O1–O3; O4 is executed.

## Theorem T1 — the crowd's ground energy never rises under an alternation

*Statement.* For `n` records under exclusion on an even torus with bond rates `1 + δ(−1)^{x_a}` on the bonds along `a`: (a) `T H_n(δ) T† = H_n(−δ)` for the translation by one site along every alternated axis; (b) the ground energy `E_n(δ)` is even and concave in `δ`, hence `E_n(δ) ≤ E_n(0)` for every `δ`. (c) On the ring of four, `E_2(0) = −√2` and `E_2(3/10) = −√218/10`.

*Proof.* (a) The one-record generator satisfies `TH(δ)T† = H(−δ)` (block 83 D2; the alternation changes sign under the shift); the compressed generator is `Σ_slots H` restricted to a translation-invariant subspace, and the translation acts on the antisymmetric basis with the re-ordering sign (family B, exact for `n = 1, 2, 3`). (b) `H_n(δ) = H_n(0) + δV_n` is affine; `E_n(δ) = min_ψ ⟨ψ|H_n(δ)|ψ⟩` is a minimum of affine functions of `δ`, hence concave; even by (a); a concave even function has its maximum at `0`. (c) Exact eigenvalues of the `24 × 24` compressed generator (family B). ∎

## Theorem T2 — the sea's filling under an alternation is a jam, and the jam is blind

*Statement.* (a) For `0 < δ ≤ 1`, every one-record energy is nonzero: per axis `sin²k + δ²cos²k − δ² = (1 − δ²)sin²k ≥ 0`, so `E² ≥ 2δ²` on a two-dimensional torus (`3δ²` in three dimensions, block 84 T1); exactly `N` of the `2N` states are negative and the free sea's filling is one record per site. (b) With a record on every site the compressed generator is exactly the zero matrix (`16` coin configurations on the ring of four at `δ = 3/10`).

*Proof.* (a) Family C, symbolic; on the ring of four the energies are `±3/10, ±1`, twice each, four negative. (b) No hop has an empty site to go to (family C, exact). ∎

## Theorem T3 — a single record gains nothing on the ring of four

*Statement.* One record's lowest energy on the ring of four is exactly `−1` at `δ = 1/10, 3/10, 1/2`.

*Proof.* The energies are `±|δ|` and `±1`, twice each (family D, exact). ∎

## Executed (supervisor control; floating point; evidence, not proof)

Controls in the pack (`specs/supervisor_control_block85_crowd_balance.py`, output in `.out.txt`; disjoint machinery: dense and sparse many-record diagonalisation, block 80's).

*W1 — sea against crowd on three tori.* Energy per site at `δ = 0, 0.05, 0.1, 0.2, 0.3` and the fit `A|δ| + Bδ²`.

| torus | state | `E(0)` | `E(0.3)` | linear `A` | quadratic `B` |
|---|---|---|---|---|---|
| `3×3` | free sea | `−0.929` | `−1.055` | `−0.315` | `−0.351` |
| `3×3` | crowd, 4 of 9 | `−0.454` | `−0.523` | `−0.173` | `−0.192` |
| `3×3` | crowd, 6 of 9 | `−0.447` | `−0.500` | `−0.150` | `−0.089` |
| `4×3` | free sea | `−0.896` | `−1.027` | `−0.332` | `−0.346` |
| `4×3` | crowd, 6 of 12 | `−0.467` | `−0.519` | `−0.082` | `−0.300` |
| `4×3` | crowd, 8 of 12 | `−0.439` | `−0.475` | `−0.087` | `−0.119` |
| `4×4` | free sea | `−0.854` | `−0.982` | `−0.355` | `−0.241` |
| `4×4` | crowd, 4 of 16 | `−0.323` | `−0.326` | `0.000` | `−0.029` |

*W2 — every filling on `3×3`.* Quadratic coefficient `−0.051, −0.103, −0.124, −0.192, −0.172, −0.089, −0.064, −0.056, 0` for `n = 1 … 9`: growing to `5` records, falling to zero at the jam; the linear parts likewise (`0` at `n = 9`).

## No-Go Discipline Gate

The note's negative sentences: the crowd's ground energy never rises under an alternation; the jam is blind; a single record gains nothing.

### N1 — Routes by which the sentences could fail or mislead
1. *The composition sign.* T1's proof does not use it; the executed numbers are for the anticommuting composition (block 80's import).
2. *Small tori.* Three tori with exact zero modes at `δ = 0`, which give linear terms; the quadratic coefficients are fits, not limits; no three-dimensional crowd is computed.
3. *Which filling.* The balance for a crowd depends on the filling; the lane does not say how many records the lattice carries (block 39 T4: it grows). The threshold is a function of filling.
4. *The balance as a minimisation* remains a reading (block 84 N1.2).

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Ring of four for the exact parts; `δ = 3/10`; two-dimensional tori for the control; the fit's four points.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Record axiom's exclusion | yes (premise) |
| block 80 (open PR #8615) | the compressed generator and its translation | yes (restated) |
| blocks 59, 84 (open PRs #8581, #8652) | the bond rates; the balance and the sea's coefficient | yes (placed) |
| blocks 76, 78 (open PRs #8611, #8613) | the sea reading as a comparator | yes (comparator) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the crowd's ground energy is even and concave; the jam is blind; one record gains nothing; the crowd's coefficients are a fraction of the sea's" | executed: compressed generators entry by entry at `±δ` | executed: the jam on every coin configuration | executed: the ring's energies; control fillings | executed: exact ground energies as algebraic numbers | T1 by proof at every filling; T2 by the bound; T3 on the ring

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Concave-and-even is trivial; the content is the size, which you cannot compute in three dimensions." Reply: agreed on the second half, and the note says so; the first half is what block 84's N1.1 needed — that the direction of the balance is not an artefact of free composition — and the executed fractions bound the crowd's threshold from above by the sea's. Second objection: "The jam is the physical state (records keep forming)." Reply: then nothing alternates and there is no rest energy from this route; the note records that the jam is blind.

### N8 — Cross-cycle echo
Block 80: the compressed generator; the jam's opposite clock response. Block 84: the sea's balance. Here: the crowd's sign agrees with the sea's; the jam is blind.

## Falsifiers

- A filling at which `TH_n(δ)T† ≠ H_n(−δ)`.
- A two-record ground energy on the ring of four at `δ = 3/10` that is not `−√218/10`, or one above `−√2`.
- A one-record energy on a torus that vanishes at `δ ≠ 0`.
- A crowd on any torus whose ground energy rises under the alternation.

## Boundaries and non-claims

Small tori; fits; the composition sign an import; no three-dimensional crowd coefficient; the filling not derived; the balance a reading. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record axiom. Blocks 59, 76, 78, 80, 84 (open PRs): restated or placed.
- Named standard imports at definition level: the variational principle (minimum of affine functions is concave); exact eigenvalues of small matrices; sparse diagonalisation for the control.

## Review record
Supervisor-run block, the thirty-third of the source-link direction; the fourth after the rest-energy panel. Lens pass, in writing, by the supervisor: a foundations lens — the crowd is the axioms' composition and the sea a comparator; the jam's blindness is stated before any size is quoted, so that the sea's own filling is not mistaken for a crowd state; a rigour lens — the evenness was checked exactly on the compressed generators (not inferred from the one-record case), the algebraic ground energies compared exactly, and the fit's linear part named for what it is (the small tori's zero modes). A first draft of the runner used floating-point conversions (`N(`) to order algebraic numbers; the float scan caught them and exact comparisons replaced them. Mutation census: six mutations, each failing in its own family only. No independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_crowd_under_exclusion_also_gains_from_an_alternation_of_the_bond_rates_ground_energy_never_rises_jam_blind_2026_09_22.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
