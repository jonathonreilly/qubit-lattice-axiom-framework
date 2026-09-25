---
claim_id: admissibility_rule_the_species_symmetry_forces_only_doubling_every_nonzero_level_in_a_varying_field_is_a_pair_and_a_rate_field_keeps_exactly_sixteen_zero_modes_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied static Hermitian walk on finite even periodic tori, positive scalar rate fields and real site
  frames. Even species maps and antiunitary reversal admit a two-dimensional corepresentation; symmetry requires
  even multiplicity but permits higher degeneracy. Positive invertible rate congruences preserve exactly sixteen
  zero modes. Exact modular witnesses on the fixed 4x4x4 torus establish generic multiplicity two for nonzero rate-field
  levels and all frame levels within those finite parameter spaces. No genericity theorem at other sizes, infinite-volume
  spectrum, physical mass, or record-gas gap is supplied.
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_species_symmetry_forces_only_doubling_and_a_rate_field_keeps_sixteen_zero_modes_2026_09_24.py
---

# Species symmetry: even multiplicity, sixteen rate-field zero modes, and a fixed-size generic-pair theorem

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 70 as landed, with supplied rate and frame fields; certificates modulo a prime; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within block 70's exchange maps of the walk's eight species, as landed on main, with supplied rate and frame fields on even tori; it reports that the stated symmetry relations force even multiplicity, with exact doubling generic at the checked size and that a rate field keeps the species' sixteen zero modes; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 70, as landed, says that the reversal "doubles finite static eigenlevels". It also says that "formal uniform branch-label orbits do not establish eightfold degeneracy in arbitrary varying fields". Its checker's further claim, that "multiplicity two for every level in every case", was deferred. This note settles a restricted generic statement on the fixed 4x4x4 torus, not the original every-field claim.

- **T1: the reversal anticommutes with the even exchange maps.** `ΘV_nΘ⁻¹ = −V_n`. The even maps anticommute with each other, with `V₁₁₀V₀₁₁ = iV₁₀₁`, and they commute with the walk in rate fields.
- **T2: so the symmetry forces doubling and nothing more.** The relations have a two-dimensional irreducible corepresentation. So every eigenspace is `ℂ² ⊗ W`, with the even maps acting on the first factor and a real structure on `W`. These relations alone do not force multiplicity four or eight; special operators can have it.
- **T3: a rate field keeps exactly sixteen zero modes.** `ker(ΦHΦ) = Φ⁻¹ ker H`. On every even torus that is the eight species' zero-momentum states times the two coin states, whatever the positive rate field.
- **T4: generically on 4x4x4, every other rate-field level is exactly a pair.** This is verified on the `4×4×4` torus for a varying rate field, and for a varying frame, where the even exchange symmetries need not remain. By the discriminant it holds outside a proper algebraic set in these fixed-size real parameter spaces only.

The uniform walk has large degeneracies. Varying positive rate fields need not split all of them, but the fixed-size witness proves that extra nonzero-level degeneracy is exceptional on 4x4x4. Zero remains exactly sixteenfold on any finite even torus. This excludes an open spectral gap about zero for the supplied rate-congruence operator; it does not establish a physical rest-energy mechanism or require one particular alternative coupling.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "Each site has a domain of local possibilities." "No possibility is privileged." The two-component coin and its half-turns are separately supplied mathematical structure, not inferred from these sentences.
  - "Admissibility is not a dynamics axiom." The walk and its fields are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed).
  - `H = Σ_a σ_a S_a` on an even torus, with `(S_aψ)(x) = (ψ(x + e_a) − ψ(x − e_a))/(2i)`.
- **Fields** (supplied).
  - A rate field `w = φ² > 0` gives `H_w = ΦHΦ`.
  - Block 62's site-placed frame is `H_E = ½Σ_j{E^j(x)·σ, S_j}`, with `E^j_a = δ_aj + ε^j_a(x)`.
- **The exchange maps** (block 70 as landed).
  - `V_n = R_n ⊗ U_n` for `n ∈ {0,1}³`, with `U_n = (−1)^{n·x}`.
  - The coin parts are `R₁₁₀ = σ₃`, `R₁₀₁ = σ₂`, `R₀₁₁ = σ₁` for the even maps, and `σ₁, σ₂, σ₃, 1` for `100, 010, 001, 111`.
- **The reversal.** `Θ = σ₂K`, antiunitary, with `Θ² = −1`.
- **Certificates.**
  - Characteristic polynomials and ranks are computed modulo `p = 1000033`, a prime `≡ 1 (mod 4)`, with `i ↦ 649529`.
  - The matrices have `p`-integral Gaussian-rational entries. So a squarefree polynomial modulo `p` is squarefree over `ℚ(i)`, and a rank modulo `p` bounds the rank over `ℚ(i)` from below.

## Theorem T1 — the reversal anticommutes with the even maps

*Statement.* On every even torus:
- `V_n² = 1`, and `V_nH_wV_n = (−1)^{|n|}H_w` in every rate field. This is block 70's commutation for even `n` and its spectral reversal for odd `n`.
- The even maps anticommute pairwise, and `V₁₁₀V₀₁₁ = iV₁₀₁`.
- `ΘH_wΘ⁻¹ = H_w` and `ΘH_EΘ⁻¹ = H_E`.
- `ΘV_nΘ⁻¹ = −V_n` for the three even maps.
- A general frame need not commute with the even maps: an off-diagonal frame component can break them. Special varying diagonal frames can preserve them. The nearest-neighbor frame still has the bipartite spectral reversal U111 H_E U111=-H_E; reversal is not its only symmetry.

*Proof.*
- The site sign `U_n` reverses `S_a` exactly when `n_a = 1`. The half-turn `R_n` reverses the matching `σ_a`.
- `ΘV_nΘ⁻¹ = σ₂ V̄_n σ₂ = (σ₂σ̄_cσ₂)U_n = −σ_cU_n`, because `σ₂σ̄_cσ₂ = −σ_c` for each of the three coin matrices `σ_c`. That is the new relation.
- A frame term `ε^j_aσ_aS_j` with `a ≠ j` picks up the sign `(−1)^{n_a + n_j}`, which is `−1` for some even `n`. ∎

*Checked (B1, B2).* All of these are operator identities on the 128 states of the `4×4×4` torus, in a varying rate field and in a varying frame with all nine components random.

## Theorem T2 — symmetry forces doubling and nothing more

*Statement.* The assignment `V₁₁₀, V₁₀₁, V₀₁₁ ↦ σ_z, σ_x, −σ_y` with `Θ ↦ σ_yK` satisfies every relation of T1. On every eigenspace `E_λ` of the walk in a rate field:
- `E_λ ≅ ℂ² ⊗ W`, with the even maps acting on the first factor;
- `Θ = σ_yK ⊗ Θ_W` with `Θ_W² = +1`, a real structure on `W`.

So the multiplicity is `2 dim W`. It is even, and the symmetry forces no more: never four or eight.

*Proof.* The even maps generate an algebra isomorphic to `M₂(ℂ)`, so `E_λ ≅ ℂ² ⊗ W`.
- `J₀ = σ_yK ⊗ K_W` anticommutes with the generators, as `Θ` does, so `ΘJ₀⁻¹` commutes with them and equals `1 ⊗ u_W`.
- Then `Θ² = (σ_yK)² ⊗ Θ_W² = −Θ_W²`, and `Θ² = −1` gives `Θ_W² = +1`.
- A real structure forces no degeneracy on `W`. ∎

*Checked (C1).* The relations of the `2×2` corepresentation.

## Theorem T3 — a rate field keeps exactly sixteen zero modes

*Statement.* For every positive rate field on an even torus, `ker(ΦHΦ) = Φ⁻¹ker H`. `ker H` is spanned by the plane waves at `k ∈ {0, π}³` times the two coin states, so the zero level has multiplicity exactly 16.

*Proof.*
- `Φ` is invertible, so `ΦHΦψ = 0 ⟺ H(Φψ) = 0`.
- `H`'s symbol `Σ_a σ_a sin k_a` is invertible unless every `sin k_a = 0`. That happens exactly at the eight momenta `{0, π}³`, which even sides allow. ∎

*Checked (D1).* On the `4×4×4` torus in a varying rate field:
- the sixteen vectors `Φ⁻¹(plane wave ⊗ coin state)` are annihilated exactly;
- `H_w` has rank 112 modulo `p`, so exactly sixteen zero modes over `ℚ(i)`.

## Theorem T4 — generic multiplicity two on the fixed 4x4x4 torus

*Statement* (verified on the `4×4×4` torus by certificates modulo `p`).
- (a) **The uniform walk** has characteristic polynomial `E¹⁶(E² − 1)²⁴(E² − 2)²⁴(E² − 3)⁸`. Its levels have multiplicities 16, 24, 24 and 8.
- (b) **A varying rate field.** The `V₁₁₀ = +1` block (64 states) has characteristic polynomial `E⁸ q(E)`, with `q` of degree 56, squarefree, and `q(0) ≠ 0`. `V₁₀₁` carries this block onto the `−1` block. So every nonzero level has multiplicity exactly 2.
- (c) **A varying frame.** The characteristic polynomial is `q²`, with `q` of degree 64 and squarefree. So every level is exactly a reversal pair.
- (d) **Genericity.** The block polynomial with the forced `E⁸` removed has coefficients polynomial in the field values. Its discriminant is nonzero at the witness, so it is not identically zero. Outside the algebraic set where it vanishes, every nonzero level is exactly doubled. For the frame no quaternion determinant import is needed. For every real frame the Hermitian matrix has an antiunitary symmetry squaring to -1: if v is an eigenvector, Theta v has the same real eigenvalue and is orthogonal to v. Thus its monic characteristic polynomial f is a square at every real parameter point. Write a monic degree64 candidate q and recursively match the highest 64 coefficients of q^2=f: each new coefficient is half a polynomial in coefficients already obtained and those of f. Hence q has polynomial parameter coefficients with powers of2 in denominators. The remaining coefficients of q^2-f vanish at every real point, so vanish identically. At the rational witness the modular test proves q squarefree; the only possible denominators used here are invertible modulo the odd prime. Its discriminant is therefore not identically zero. This proves genericity only in this 4x4x4 real frame parameter space. For rates, parameterize by positive phi, not directly by w=phi^2; remove the eight identically zero roots in the plus block. The discriminant and q(0) are nonzero at the witness. Their nonvanishing defines the asserted generic subset of positive phi.

*Proof.*
- `V₁₁₀` is diagonal in the site–coin basis, so its blocks are principal submatrices.
- `V₁₀₁` anticommutes with `V₁₁₀` and commutes with `H_w`, so it maps each eigenvector of one block to one of the other.
- A squarefree `q` modulo `p` is squarefree over `ℚ(i)`.
- For the frame, `gcd(f, f′) = q` with `f = q²` and `q` squarefree modulo `p`. ∎

*Checked (E1, E2).* All four certificates, modulo `p`. The uniform case also validates the characteristic-polynomial routine against a known answer.

The deferred claim therefore holds in the exact form "every nonzero level is exactly a pair, generically". The frozen "two classes of eight exact copies" stays a statement about formal labels. What survives exactly beyond the pairs is the rate field's sixteen zero modes.

## Spectral scope

The positive rate congruence cannot remove the zero eigenvalue on these finite tori. This is a statement about a supplied operator's spectrum, not a physical rest mass. Other added operators may remove zero, but neither uniqueness of such a mechanism nor a gap on a fluctuating record-gas background is derived here. Earlier binding, staggered-coupling and gas discussions are historical motivation only.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 70 as landed: 'Formal uniform branch-label orbits do not establish eightfold degeneracy in arbitrary varying fields'; its checker's deferred 'multiplicity two for every level in every case'"
source_of_blocker_text: block 70 as landed; the deferred PR #8602 sources
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "twist fields and a second torus size per kind; the exceptional set where the discriminant vanishes; the gap of the walk on a staggered record background with defects"
conditional_surface_status: "T1-T3 exact on every even torus; T4 verified and generic only within the fixed 4x4x4 parameter spaces; reach-three and twist fields not re-run here"
hypothetical_axiom_status: "the walk and its fields are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 70: the exchange maps and the reversal's doubling.
  - Block 54: the walk.
  - Block 62: the frame.
  - Blocks 77 and 79: staggered terms.
  - Blocks 104, 115 and 117: the rest-energy thread.
- **The probes attempt.** `deferred-20260924-species` a1 (Claude Opus 5.5) found T1's new relation, T2, T3 and the certificates, including a reach-three strain on `6×4×4` that is not re-run here. A Grok referee confirmed it (issue #9123).
- **In the literature.**
  - The doubling by an antiunitary symmetry with `Θ² = −1` is Kramers degeneracy.
  - The classification of eigenspaces under a symmetry group with antiunitary elements is Wigner's theory of corepresentations.
  - The walk's eight species are the lattice's doublers, whose persistence is the subject of the no-go theorem of Nielsen and Ninomiya.
  - Splitting doublers with a staggered term is the staggered construction of Kogut and Susskind.
- **New here:**
  - an independent exact runner, with its own operators and certificates;
  - the statement placed against block 70 as landed;
  - the consequence for the rest-energy thread.

## Exact target and obligation graph

Target: the deferred multiplicity statement of block 70. The obligations are:
- (O1) the relations;
- (O2) the corepresentation;
- (O3) the zero modes;
- (O4) the certificates.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- the symmetry never forces a four- or eightfold level;
- no rate field gaps the species' zero modes.

### N1 — Routes by which the sentences could fail or mislead
1. *Special fields.* Fields with extra lattice symmetry can have more degeneracy. For a concrete nonconstant positive counterexample, let phi be2 on odd sites and3 on even sites. Every nearest-neighbor product is6, so Phi H Phi=6H and all uniform-walk extra degeneracies remain. The exceptional set is not fully classified.
2. *Twist fields and other torus sizes.* Not re-run here. The attempt verified a reach-three strain on `6×4×4`.
3. *Other couplings.* A term that is not a rate field, such as a staggered term, can gap the zero modes. That is the point of the last section.
4. *Infinite volume.* Continuous spectra are not addressed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The certificates are modulo one prime, with `p`-integral entries.
- The frame polynomial square follows from Hermiticity, antiunitary pairing and coefficient recursion as shown in T4.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no possibility privileged; no dynamics in the axioms | yes |
| block 70 (landed) | the exchange maps and the reversal | yes (restated) |
| blocks 54, 62 (landed) | the walk and the frame | yes |
| blocks 77, 79, 104, 115, 117 | the rest-energy thread | placement |
| probes (deferred-20260924-species a1; Grok-refereed, #9123) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the species symmetry forces only doubling; a rate field keeps sixteen zero modes; nonzero levels are generically pairs on the fixed 4x4x4 torus" | executed: the corepresentation's relations; `V_n² = 1` and `V_nH_wV_n = (−1)^{\|n\|}H_w` | executed: the sixteen zero-mode vectors annihilated at every site | executed: the characteristic polynomials modulo `p` | executed: the reversal's relations as operator identities on 128 states | T1–T3 on every even torus; T4 verified on `4×4×4` and generic by the discriminant; the walk and its fields supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Eight species should give eightfold levels." *Reply:* Extra degeneracies also occur in special varying fields. The even maps and reversal admit a two-dimensional corepresentation; the 4x4x4 witness proves generic splitting there, not for every varying field. Only the rate field's zero level keeps all sixteen states.
- *Objection:* "A certificate modulo one prime is not a proof." *Reply:* Squarefreeness and rank lower bounds lift from `F_p` to `ℚ(i)` for `p`-integral matrices; that is what is used.

### N8 — Cross-cycle echo
- Block 70 found the maps and the reversal.
- This note finds what they force: pairs, and sixteen zero modes that no clock can lift.
- Alternative gap mechanisms and their physical realization remain outside this result.

## Falsifiers

- A varying rate field on an even torus whose zero level is not sixteenfold.
- An exact relation `ΘV_nΘ⁻¹ ≠ −V_n` for an even map.
- A field outside the exceptional set with a nonzero level of multiplicity four.

## Boundaries and non-claims

- The walk and its fields are supplied.
- The certificates are on the `4×4×4` torus. Other sizes, twist fields and the exceptional set are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 62, 70, 77, 79, 104, 115 and 117, restated or placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - reduction modulo a prime of `p`-integral matrices;
  - finite Hermitian spectral decomposition, antiunitary pairing and polynomial coefficient recursion;
  - the structure of `M₂(ℂ)`-modules.
- Reference only: Kramers; Wigner; Moore; Nielsen; Ninomiya; Kogut; Susskind.

## Review record

- **Who and when.** Supervisor-run block, the sixty-seventh since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (`deferred-20260924-species` a1). A Grok referee confirmed them (#9123).
  - The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and block 70 was read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_species_symmetry_forces_only_doubling_and_a_rate_field_keeps_sixteen_zero_modes_2026_09_24.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.

## Current source dependencies

- [Current conditional operator source](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional operator source](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current conditional operator source](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
