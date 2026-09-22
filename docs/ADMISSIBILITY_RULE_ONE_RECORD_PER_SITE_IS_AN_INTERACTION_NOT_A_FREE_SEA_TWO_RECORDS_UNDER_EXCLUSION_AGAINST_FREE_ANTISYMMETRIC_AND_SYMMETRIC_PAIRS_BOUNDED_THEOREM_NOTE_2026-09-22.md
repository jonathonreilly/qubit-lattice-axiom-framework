---
claim_id: admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 54, 55, 71 and 76 (open PRs #8570, #8571, #8603, #8611; not adopted) and the Record axiom in the owner's reading (one record per site at a time): the clocked reduced walk H = phi sigma_3 D phi on a ring; two records as two one-record amplitudes; the FREE two-record generator H (x) 1 + 1 (x) H on the product space with its antisymmetric and symmetric sectors (an exchange sign the axioms do not supply); and the HARD-CORE sectors - the configurations with the two records on different sites, the generator compressed to them - which is what 'one record per site at a time' gives, with either exchange sign or with none. (T1) On rings of 4, 5, 6 and 7 sites the hard-core two-record generator has tr H^2/dim different from the free antisymmetric pair's and from the free symmetric pair's (exact rationals: 2/3 against 6/7 and 10/9 on the ring of 4; 3/4 against 8/9 and 12/11; 4/5 against 10/11 and 14/13; 5/6 against 12/13 and 16/15), and N fewer states than the free antisymmetric sector: the exclusion is an interaction, not a free pair of either sign. (T2) Under exclusion the antisymmetric, symmetric and sign-free generators have the same tr H^2/dim on every ring, the same tr H^4/dim on the rings of 5, 6, 7 and the same tr H^6/dim on 5 and 7; on even rings the sign shows at fourth (ring of 4) or sixth order (ring of 6): the exchange sign is invisible at second order and where it shows it is a parity effect of the ring. (T3) For two exactly orthogonal complex one-record states in a varying rate field, the antisymmetric pair's energy under the free generator is the sum of the one-record energies (block 76 T3) and under the hard-core generator it is not: the ledger's source of two records is not the sum of their one-record sources. EXECUTED, NOT CLAIMED: full spectra on rings of 4 to 8 and on a 4x4 torus with the two-dimensional walk (hard-core antisymmetric and symmetric spectra coincide on odd rings and differ on even ones and on the torus); three records on a ring of 6 under exclusion: 160 states against the free triple's 220, mean E^2 0.90 against 1.23. NOT claimed: anything about Z^3 or about many records beyond three; the exchange sign; that a filled sea exists; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_2026_09_22.py
---

# One record per site is an interaction, not a free sea: two records under exclusion against free antisymmetric and symmetric pairs

**Date:** 2026-09-22
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about two records under the Record axiom's exclusion on small rings; nothing adopted or registered; unaudited)

This note works within supplied clauses for amplitudes on the lattice timed by local clocks and the Record axiom in the owner's reading; it reports what one record per site at a time does to two records against the free pairs of either exchange sign; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 76 (open PR #8611) probed the reading in which the walk's negative-energy states are all occupied — a *free* sea of records with anticommuting composition — and found what it would induce. The fork probe of 2026-09-22 flagged the import in that reading: the axioms say one record per site at a time, which is a hard-core condition (no two records at a site, whatever their coins), and say nothing about a sign under exchange. This note asks what two records under the axioms' own exclusion actually are.

1. **Not a free pair of either sign** (T1). Restrict the two-record generator to configurations with the records on different sites. Its normalised second trace differs from the free antisymmetric pair's and from the free symmetric pair's on every ring tried — exact rationals, e.g. `2/3` against `6/7` and `10/9` on four sites. The exclusion removes states and changes the spectrum: it is an interaction.
2. **The exchange sign hardly matters under exclusion** (T2). With exclusion, the antisymmetric, symmetric and sign-free generators have identical second traces on every ring, identical fourth traces on rings of 5, 6, 7, and differ only through parity effects of even rings.
3. **The source is not additive** (T3). Under the free generator the antisymmetric pair's energy is the sum of the two one-record energies (block 76 T3); under exclusion it is not. So block 76's additive many-record source — the basis of "a hole sources as a positive body" — is a property of the free pair, not of the axioms' records.

Executed: full spectra confirm the picture on rings up to 8 and on a `4×4` torus; three records under exclusion have 160 states against the free triple's 220.

In plain terms: the axioms say two records can never sit on the same site. That rule alone changes how two walkers move together — it is a genuine interaction, and it does most of the work; whether the two walkers are "fermions" or "bosons" barely shows at low order. So a sea of the axioms' own records would be a crowd of interacting walkers, not the free sea of block 76, and its energy would have to be computed as such.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "FORK_PROBE_source_link_20260922.md section 4 item 1 (the exchange sign is not in the axioms; hard-core exclusion is not antisymmetry); block 76's reading rests on a free sea with anticommuting composition."
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the axioms' records form an interacting many-record problem: block 76's free sea is a comparator, not the framework's; next: the two-record ledger (does block 55's action = reaction survive exclusion?); the hard-core sea's energy on small tori (executed) against block 76's; SU(2) bond links (block 79)"
conditional_surface_status: "T1-T3 exact on the rings stated (4 to 7 sites, the reduced walk, uniform rates in T1-T2, varying in T3); nothing is claimed for Z^3 or for more than two records beyond the executed triple"
hypothetical_axiom_status: "the clocked reduced walk; two records as two amplitudes with a composition rule; hypotheses only, the composition rule an import"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Record axiom ("a site never carries more than one record"; the owner's reading: at a time), the Qubit axiom's coin, and the memo's silence on amplitude dynamics and on how records compose. Blocks 54, 55, 71, 76 (open PRs) supply the clocked walk, the ledger and the sea reading.

- **One-record space.** A ring of `N` sites with a two-component coin, dimension `d = 2N`; `H = φσ₃Dφ`, `D` the symmetric difference.
- **Free two-record generator.** `H₂ = H ⊗ 1 + 1 ⊗ H` on the `d²`-dimensional product space. **Antisymmetric sector:** span of `e_i ⊗ e_j − e_j ⊗ e_i` (`d(d − 1)/2`); **symmetric:** `e_i ⊗ e_j + e_j ⊗ e_i` and `e_i ⊗ e_i` (`d(d + 1)/2`).
- **Hard-core sectors.** The same with the pairs `(i, j)` restricted to different sites (`d(d − 2)/2` for either sign; `d(d − 2)` without a sign); the generator restricted (compressed) to the sector: `PH₂P`.
- **Normalised traces.** `tr H^k/dim` of the compressed generator; the exact runner works with `A = iH` (real antisymmetric) so that `tr H² = −tr A²`, `tr H⁴ = tr A⁴`, `tr H⁶ = −tr A⁶`.

The restriction of a hopping generator to configurations with no double occupancy is the infinite-repulsion (projected) problem of many-body practice; named as a comparator only.

## Prior art and what is new

New, inside the framework's vocabulary: that the Record axiom's exclusion, taken as the composition rule for two of the framework's records, gives an interacting two-record generator whose spectrum differs exactly from both free pairs; that under it the exchange sign is invisible at second order; and that the additivity of the ledger's source, which block 76's hole argument used, fails. No gravitational claim is made.

## Exact target and obligation graph

Target: what "one record per site at a time" is for two records. Obligations: (O1) against the free pairs; (O2) the sign's visibility; (O3) the ledger's additivity. T1–T3 discharge them.

## Theorem T1 — not a free pair of either sign

*Statement.* On rings of `N = 4, 5, 6, 7` with uniform rates, `tr H²/dim` of the hard-core generator (either sign, or none) is `2/3, 3/4, 4/5, 5/6` (the pattern `(N − 2)/(N − 1)` is read off, not proved), while the free antisymmetric pair has `6/7, 8/9, 10/11, 12/13` and the free symmetric pair `10/9, 12/11, 14/13, 16/15`. The hard-core antisymmetric sector has `N` fewer states than the free one.

*Proof.* Computed exactly (runner B1) by compressing `A ⊗ 1 + 1 ⊗ A` to each sector's orthogonal basis; the sector dimensions are `d(d − 1)/2 − N` against `d(d − 1)/2`. The values quoted are those computed; the closed forms in `N` are read off the four rings and not proved for general `N`. ∎

The `N` removed states are the same-site pairs of opposite coin, which free antisymmetry allows and the Record axiom forbids.

## Theorem T2 — the exchange sign under exclusion

*Statement.* With exclusion, the antisymmetric, symmetric and sign-free generators have the same `tr H²/dim` on `N = 4, 5, 6, 7`; the same `tr H⁴/dim` on `N = 5, 6, 7` and the same `tr H⁶/dim` on `N = 5, 7`; on `N = 4` the fourth traces differ (`5/6` against `7/6`), on `N = 6` the sixth.

*Proof.* Computed exactly (runner C1). ∎

The differences appear only where a closed path of the two records around the ring depends on the sign — a parity effect of even rings. The control's full spectra show the hard-core antisymmetric and symmetric spectra coinciding on odd rings and differing on even rings and on the `4×4` torus.

## Theorem T3 — the source is not additive under exclusion

*Statement.* On a ring of 6 with a varying rational rate field and two exactly orthogonal complex one-record states `ψ₁, ψ₂`: the antisymmetric pair's energy under the free generator equals `e₁ + e₂` (block 76 T3), and under the hard-core generator — the pair projected to different-site configurations and the generator compressed — it does not.

*Proof.* Computed exactly (runner D1): free `16169964/134909593 = e₁ + e₂`; hard-core a different rational. The projection removes the same-site components of the pair, and the compressed generator's expectation is not a sum of one-body expectations. ∎

Block 76's T3(c) — a hole in an occupied negative state sources as a positive body — used additivity; for the axioms' records it does not hold as stated, and the sea's source would have to be computed for the interacting problem.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block78_hard_core.py`. **W1** (rings 4–8, full spectra): dimensions as stated; the hard-core antisymmetric and symmetric spectra coincide to `1e-15` on `N = 5, 7` and differ (spectral distance `0.44, 0.21, 0.14`) on `N = 4, 6, 8`; mean `E²`: free antisymmetric `0.857 … 0.933`, free symmetric `1.111 … 1.059`, hard-core `0.667 … 0.857`. **W2** (`4×4` torus with the two-dimensional walk): dimensions `496/528` free, `480` hard-core; mean `E²` `1.935, 2.061` free against `1.867` hard-core; hard-core antisymmetric and symmetric differ at fourth order (`7.93` against `7.80`). **W3** (three records on a ring of 6): the free antisymmetric triple has 220 states, mean `E²` `1.227`; under exclusion 160 states, mean `E²` `0.900`.

## No-Go Discipline Gate

The note's negative sentence: two of the axioms' records under exclusion are not a free pair of either exchange sign.

### N1 — Routes by which the sentence could fail or mislead
1. *A different reading of the Record axiom.* If "one record per site" meant one record per site and coin state (two records of opposite coin allowed), the antisymmetric free pair would be recovered. The memo's sentence and the owner's reading exclude two records at a site outright.
2. *The coin as occupation.* The QFT lens of the fork probe named a reading in which `M₂(ℂ)` is the algebra of one fermionic mode and the coin lives on the sublattice; that changes clause B and is not examined.
3. *Large systems.* The exclusion's effect per pair falls with the number of sites (`tr H²/dim` ratios approach 1); for many records at high density it does not.
4. *Rings.* T1–T3 are on rings with the reduced walk; the `4×4` torus is executed only.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Uniform rates in T1–T2; the reduced walk; two records (three executed).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Record axiom's one record per site; the coin | yes (premise) |
| blocks 54, 55 (open PRs #8570, #8571) | the clocked walk; the ledger's source | yes (restated) |
| blocks 71, 76 (open PRs #8603, #8611) | the negative branch; the free-sea reading and its additivity | yes (restated; T3 refers to block 76 T3) |
| `FORK_PROBE_source_link_20260922.md` | the flag on the exchange sign | context |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "hard-core ≠ free pair; sign invisible at second order; additivity fails" | executed: two-body matrix elements of five generators on four rings | executed: the sectors defined site by site; their dimensions | executed: `tr H²/dim`, `tr H⁴/dim`, `tr H⁶/dim`, exact | executed: the pair's energy under both generators against the one-record sum | rings 4–7 exact; `Z³` and many records not claimed |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Hard-core bosons in one dimension are free fermions." Reply: for a one-component particle; here each record carries a coin, and the exclusion forbids opposite coins on a site — the traces differ from free fermions on every ring, exactly. Second objection: "You have only shown two particles on a ring." Reply: yes, and the note claims exactly that; the point is that the free sea of block 76 is not what the axioms' exclusion gives even for two records.

### N8 — Cross-cycle echo
Block 71: negative energies exist in the clauses. Block 76: fill them, and what follows for a free sea. Here: the axioms' records are not free — the sea, if there is one, is interacting, and block 76 is the comparator.

## Falsifiers

- A ring on which the hard-core `tr H²/dim` equals the free antisymmetric or free symmetric value.
- Two orthogonal one-record states whose antisymmetric pair has an additive energy under the hard-core generator on a ring with varying rates (the note exhibits one pair for which it fails; additivity as a theorem is refuted by that instance).

## Boundaries and non-claims

Two records on rings; the exchange sign and the filling are not decided; nothing about `Z³` or many records is claimed beyond the executed triple. No statistical statement, no gravitational statement, no adoption.

## Imports
- `minimal_axioms`: the Record axiom; the Qubit axiom; the memo's silence on composition. Blocks 54, 55, 71, 76 (PRs #8570, #8571, #8603, #8611, open): restated or placed.
- Named standard imports at definition level: compression of a matrix to a subspace; traces of powers.

## Review record
Supervisor-run block, the twenty-sixth of the source-link direction; the third after the fork probe. Lens pass, in writing, by the supervisor: a foundations lens — the Record axiom's sentence is used as written and in the owner's reading, and the exchange sign is named as the import it is; a rigour lens — the first version of T3 compared expectations of `H²`, which is not a one-body operator on the pair (its cross term `2H ⊗ H` is two-body), so additivity had no reason to hold even for the free pair; the test was rebuilt with complex one-record states and the generator itself; the closed forms `(N − 2)/(N − 1)` etc. are stated as read off four rings and not proved; T2 was sharpened after the control's full spectra showed the signs differing on `N = 6, 8` where the fourth traces agree (the sixth trace was added). A strategy lens — the block turns block 76 from a candidate reading into a comparator: the framework's own sea, if any, is interacting. Control: as reported under Executed. Mutation census: 6 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_2026_09_22.py
```

Expected: `TOTAL: PASS=10 FAIL=0`.
