---
claim_id: admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Two supplied hard-core composition sectors for the fixed two-record walk: both preserve exclusion
  and exchange covariance, without claiming a complete realization of every axiom or a formation/readout theory.
  Local exchange-energy moments first differ at order4, with coin-summed exchange-trace density -8 per elementary
  plaquette on Z2/Z3; infinite total traces are not defined. Exact finite ring traces at N4/6/8 and an all-odd-N>=3
  spectral intertwiner for the reduced sigma3 ring walk, not equivalence of every observable or initial state. No
  complex-linear grading involution reversing the three two-state generators; a minimal doubled grading representation
  and the explicitly supplied graded product are algebraic comparators, not required site-algebra changes or a statistics
  derivation.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_2026_09_24.py
---

# Two supplied hard-core exchange sectors: fourth moments, odd-ring spectra and grading limits

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54 and 78 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and its reduced ring form; one record per site as an interaction); it reports whether the axioms fix the sign with which two records compose, and where that sign first shows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The supplied compressed two-record walk admits symmetric and antisymmetric sectors, each preserving one record per site. This construction does not model formation, every axiom sentence or a complete readout theory. It provides no mechanism selecting one exchange sign.

The local exchange-energy moment vanishes below order4; at order4 its coin-summed trace density is -8 per elementary plaquette. On the specified reduced odd rings an explicit unitary identifies the two sector spectra. It need not identify the same physical observable or initial state, so the sign is not declared invisible to every experiment.

A grading involution cannot reverse all three two-state generators on C2. A doubled representation can implement that particular grading demand. Neither the demand nor its graded composite is adopted as a physical site structure.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." The fixed two-record sector is an additional restriction; permanence does not exclude formation and does not itself impose fixed total number.
  - "A readout value is determined by record content alone." The quoted sentence alone specifies no full two-record observable algebra. We explicitly restrict any readout discussion here to permutation-invariant observables.
  - "The full one-site possibility domain has algebraic presentation `M_2(C)`." A `Cl(3,0)`-compatible real presentation "may be used equivalently and adds no further primitive structure".
  - "A choice not fixed by the supplied structure remains a named conditional or open dependency."
- **The walk** (block 54 as landed). `H = Σ_aσ_aS_a` with `S_a = −i(T_a − T_a†)/2`, and on `Z²` the two-axis form `σ₁S₁ + σ₂S₂`. On rings it is block 78's reduced walk `σ₃p`. One hop has amplitude `1/2`, so `2H` has Gaussian-integer entries.
- **Two records** (block 78 as landed, which calls the compression and the composition supplied model choices).
  - `HC = span{e_{x,a} ⊗ e_{y,b} : x ≠ y}`.
  - The exchange is `P(u ⊗ w) = w ⊗ u`.
  - The compressed generator is `H₂ = Π_HC(H ⊗ 1 + 1 ⊗ H)Π_HC`.
  - A composition rule is a `P`-invariant, `H₂`-closed subspace of `HC`. The sectors are `K± = HC ∩ ker(P ∓ 1)`.
  - For `X` commuting with `P`, `tr_{K±}X = ½[tr_HC X ± tr(PX)]`: the sectors differ exactly by the exchange traces `tr(PH₂^k)`.
- **Comparators, named only:**
  - the connection of spin and statistics, and its topological route (Finkelstein–Rubinstein);
  - hard-core bosons;
  - the Jordan–Wigner map;
  - the Clifford grading.
  - Landed repository notes reach the same boundary in the operator-algebra picture: the statistics-agnostic no-go of 2026-05-25, the rotation-exchange no-go of 2026-05-28 and the ring-monodromy note of 2026-06-04.

## Theorem T1 — two supplied invariant composition sectors

*Statement.*
- (a) `HC` is `P`-invariant and closed under `H₂`. `H₂` is hermitian, and `[P, H₂] = 0`.
- (b) So `K₊` and `K₋` are each closed, each have one record per site and a conserved record number, and each have dimension `2n(n − 1)` on `n` sites.
- (c) Every lattice symmetry acts on two records as `W ⊗ W`, and a common single-particle basis change acts on two records by W tensor W. Position-dependent coin basis changes are included as block-diagonal single-particle W. These commute with P and preserve HC. This is covariance of the transformed generator, not invariance of the fixed hopping matrices under every coin rotation.
- (d) An explicitly assumed permutation-invariant observable commutes with P and therefore preserves both sectors. Commutation alone does not imply equal restrictions: P itself is a counterexample. No general content-readout indistinguishability follows.

*Proof.* The free generator and the projector onto `HC` both commute with `P`. The dimensions follow because exchange pairs distinct ordered basis vectors without fixed points. The covariance and observable statements follow from their expressly stated tensor action and commutation hypotheses, not a complete model of all axiom sentences. ∎

*Checked (B1).* On block 78's ring of four, on every basis vector of `HC` (dimension `48`): closure, hermiticity, and commutation with `P`. Also the sector dimensions.

## Theorem T2 — where the sign first shows

*Statement.* On `Z²` (two-axis walk) and `Z³`:
- (a) The coin-summed exchange amplitude `Σ_{a,b}⟨Ps|(2H₂)^k|s⟩` vanishes for every separation at `k = 2` and `k = 3`.
- (b) At `k = 4`, the local exchange-trace density is -8 per elementary plaquette: `−8` per site on `Z²`, and `−24` per site on `Z³`.
- (c) Per pair on `Z³`, `Σ_{a,b}⟨Ps|H₂⁴|s⟩` is `−2` for neighbours, `−1` across a face diagonal and `0` at distance two along a line.

For these localized symmetrized/antisymmetrized basis states, the first energy moment that can see the sign is the fourth moment of the two-record energy of a localised pair, `⟨ψ±|H₂⁴|ψ±⟩ = ⟨s|H₂⁴|s⟩ ± Re⟨Ps|H₂⁴|s⟩`.

*Proof.*
- (a) An exchange path must carry each record to the other's site. With two hops each record hops once, onto a still-occupied site, so no path exists. On a bipartite lattice both records need hop counts of the same parity, so the total is even.
- (b) and (c) use exhaustive finite local enumeration, not an infinite trace. For an exchange in k hops each record travels at least the initial separation d, so 2d<=k. Thus every possible separation at k<=4 is in the executed distance-two list. At order0 exchange has no fixed configuration and order1 cannot exchange two distinct sites. Each four-hop exchange uses an elementary square; the finite path contributions per square are -1/2 per ordered adjacent starting pair (eight pairs) and -1 per ordered opposite pair (four pairs), totaling-8. Equivalently the full enumerator gives -1 per neighbor and -1 per face diagonal in2D, and -2 per neighbor and -1 per face diagonal in3D, with zero line-distance-two contribution. Summing these finite local entries gives -8 or-24 per choice of the first site; the actual infinite total trace is not trace-class and is not asserted.

∎

*Checked (C1).* The exact enumeration of every separation up to distance `2`, at orders `2`, `3` and `4`, with Gaussian integers.

## Theorem T3 — finite even-ring moments and odd-ring spectral equivalence

*Statement.*
- (a) On block 78's rings of `N = 4, 6, 8` sites, `tr(P(2H₂)^k) = 0` for `k < N`. At `k = N` it is `128`, `−1248` and `7680`.
- (b) On every odd ring N>=3 with the specified reduced walk the two sectors are unitarily equivalent: every spectral quantity agrees at every order.

*Proof.*
- (a) An exchange on a ring must wind, which takes at least `N` hops.
- (b) Let `J` be the sign of the order of the two positions, `G = (−1)^x` on each record, and `U = (σ₁ ⊗ σ₁)(G ⊗ G)J`.
  - `J` anticommutes with `P`. Under exclusion only a hop across the bond `(N − 1, 0)` changes the order, so `JH₂J` is the walk with that bond reversed.
  - For odd `N`, `G` maps the reversed walk to `−H`, and `σ₁` on each coin maps `−H` back to `H`.
  - So `UH₂U* = H₂` and `UPU* = −P`: `U` carries `K₋` onto `K₊`.

∎

*Checked (D1).* The exchange traces on the rings of `4`, `6` and `8`. The unitary `U` on every basis vector of the rings of `5` and `7`.

## Theorem T4 — the stated grading obstruction and a discrete half-turn

*Statement.*
- (a) No linear map `Γ ≠ 0` of `ℂ²` satisfies `Γσ_a = −σ_aΓ` for all `a`. The antilinear solutions are `cσ₂K`, and they square to `−|c|²`. Thus no complex-linear or antilinear involution on C2 implements reversal of all three generators. This does not exclude other uses of the word parity.
- (b) A complex-linear grading representation with three square-one anticommuting generators needs dimension at least4: for example `Γ = 1 ⊗ σ₃` and `e_a = σ_a ⊗ σ₁`, whose product of the three `e_a` squares to `−1`. This is a mathematical doubled representation, not a decision to enlarge the physical site algebra.
- (c) If the real graded tensor-product convention is separately imposed, two three-generator presentations give Cl(6,0): six anticommuting generators that square to one, with64 linearly independent products. That is not the complex composite `M₂(ℂ) ⊗ M₂(ℂ)`, and no axiom sentence names a composite.
- (d) The half-turn about e2 composed with a unit e1 translation exchanges sites0 ande1 and commutes with the walk. On one record its coin factor `D = −iσ₂` squares to `−1`. On two records `D ⊗ D` squares to `+1`, on both sectors alike.

*Proof.*
- (a) Expanding a linear2x2 matrix in the identity and three generators forces every coefficient to zero. Solving the conjugated equations gives c sigma2 K, whose square is -|c|^2.
- (b) The central product Omega=e1e2e3 has square-1. A complex-linear grading anticommutes with Omega and pairs its +i and -i eigenspaces. Each nonzero eigenspace carries a two-dimensional irreducible generator representation, so total dimension is at least4. The displayed matrices attain it.
- (c) Ordered monomials of the six displayed generators span at most64 dimensions by anticommutation. Every nonidentity monomial has trace0: conjugate by an included generator for even degree, or an omitted one for odd degree. Distinct monomials are therefore orthogonal in the trace inner product, proving independence and dimension64 over the reals (also over the complexes in the complexified representation). The ordinary complex two-factor matrix product M4(C) has real dimension32, so it is a different specified composite.
- (d) `D` conjugates `σ₁` and `σ₃` to their negatives and fixes `σ₂`, as the half-turn does to the axes. This discrete operator identity alone does not select the symmetric or antisymmetric sector; no general theorem about every possible statistics construction is claimed.

∎

*Checked (E1).*
- The linear and antilinear solutions.
- The `ℂ⁴` grading.
- The six generators and their `64` products.
- The coin half-turn.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 78 as landed: its finite moments 'do not prove that exchange signs are generally irrelevant, that every odd-ring spectrum coincides, or that all differences are classified by parity'"
source_of_blocker_text: block 78 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "three or more records: at which order the sign first matters for the ledger's source; a clause that would fix the plaquette amplitude's sign"
conditional_surface_status: "T1-T4 on the stated lattices and rings; T3(b) for every odd ring; the walk, the compression and the composition supplied"
hypothetical_axiom_status: "the composition rule is a supplied choice; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 78: one record per site as an interaction, the sectors on rings of `4` to `7`, and the fourth traces `5/6` and `7/6` at `N = 4`.
- **Repository notes on main**, in the operator-algebra picture:
  - `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25`;
  - `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28` (the Finkelstein–Rubinstein route needs a continuum);
  - `RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04`.
- **The probes attempt.** `the-exchange-sign-from-the-coin` a1 (Claude Opus 5.5) found T1–T4. A Grok referee confirmed it (#9073): "the axioms as stated do not choose the exchange sign". An earlier worker unit (#8642) had first seen the fourth-order difference.
- **In the literature.**
  - The connection of spin and statistics.
  - Hard-core bosons and the Jordan–Wigner map.
  - Clifford algebras and their gradings.
  - Majorana generators.

  All reference only.
- **New here:**
  - an independent exact runner in Gaussian integers;
  - T2 on the infinite lattices;
  - T3(b) for every odd ring, which settles an open item of landed block 78;
  - the third-column reading: the exchange sign is not supplied by records.

## Exact target and obligation graph

Target: whether the axioms fix the exchange sign, and where it first shows. The obligations are:
- (O1) the two rules (T1);
- (O2) the lattices (T2);
- (O3) the rings (T3);
- (O4) the grading and the discrete exchange (T4).

T1–T4 discharge them. Open: three or more records.

## No-Go Discipline Gate

The bounded negative result is that the displayed fixed-number exclusion and covariance construction does not select one exchange sector. It is not a proof that both constructions realize every axiom or that all possible statistics derivations fail.

### N1 — Routes by which the sentence could fail or mislead
1. *A composite named elsewhere.* A specified graded product would supply extra composite structure; whether it determines a physical exchange rule needs an additional connection. It is not on main; a proposal of that kind (PR #7829) was closed.
2. *The larger site algebra.* `M₄(ℂ)` per site allows graded records. That decision is parked and is not touched here.
3. *Continuum limits.* The topological route needs a continuous configuration space, which the lattice axioms do not supply.
4. *Many records.* T2's order is for two records. With more records the order at which the sign matters for sources is not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used as a premise. The landed operator-algebra notes are cited as prior art only.

### N3 — Hidden-wall scan
None beyond the supplied walk, compression and composition.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; readout by content; the one-site algebra; the named-conditional clause | yes |
| blocks 54, 78 (landed) | the walk; the compression and the sectors | yes (restated) |
| probes (Grok-refereed #9073) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "both sectors preserve the stated exclusion and covariance; the sign first shows at order four, `−8` per plaquette; equal spectra on the specified odd rings" | executed: closure, hermiticity and exchange commutation on the ring of four | executed: exchange amplitudes up to distance `2` on `Z²` and `Z³` | executed: exchange traces on rings of `4`, `6`, `8` | executed: the odd-ring unitary on `5` and `7`; the grading; the half-turn | the stated lattices and rings; every odd ring by proof; two records only |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration. The parked decision on a larger site algebra is named in N1 and not touched.

### N7 — Steelman
- *Objection:* "The spinor sign `D² = −1` is the spin–statistics connection, so the antisymmetric sector is forced."
  - *Reply:* On two records the discrete exchange squares to `+1` on both sectors.
  - Turning the spinor sign into an exchange sign needs a homotopy between the exchange and a full turn, and the lattice supplies none.

### N8 — Cross-cycle echo
- Block 78 found that one record per site is an interaction, and saw a fourth-order difference on one ring.
- This note shows that the sign itself is not supplied, finds where it first shows on the lattices, and settles the odd rings.

## Falsifiers

- A failure of the stated sector invariance or covariance under its supplied action.
- A nonzero exchange amplitude at order `2` or `3` on `Z²` or `Z³`.
- An odd ring on which the two sectors' spectra differ.

## Boundaries and non-claims

- The walk, the compression and the composition are supplied.
- Three or more records are not treated.
- The parked larger site algebra is not touched.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 78](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54 and 78, restated. The three landed operator-algebra notes, cited as prior art.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - linear algebra over `ℂ` and `ℝ`;
  - the Clifford algebra `Cl(6,0)` and its Jordan–Wigner generators;
  - Gaussian-integer arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-sixth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results. A Grok referee confirmed them (#9073).
  - The supervisor re-checked them with its own runner, in Gaussian integers.
- **Before writing.**
  - Main was re-fetched, and blocks 54 and 78 were read as landed.
  - The own-prior-art check found block 78's ring comparison and the three operator-algebra notes on main. This note is placed against them.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_exchange_sign_is_not_supplied_by_records_both_hard_core_sectors_meet_every_axiom_and_first_differ_in_the_fourth_moment_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
