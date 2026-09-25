---
claim_id: admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_and_none_keeps_the_half_turn_about_the_gradient_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied exponential walk, lambda>1, with the current parents endpoint-domain results imported. T1
  entire line solutions and boundary form. T2 all line extensions preserve even shifts and unit-shift-compatible
  ones form a torus. T3 no line extension preserves both the half-turn and unit-shift identity. T4 each nonzero
  small transverse sector has four shift-compatible boundary planes, covariant under proper cubic rotations fixing
  x1, with no continuous extension to zero sine momentum. Three-dimensional conclusions concern decomposable transverse-translation-preserving
  extensions only; almost-everywhere covariance on the infinite lattice is possible. No physical selection or general
  locality theorem.
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23
- admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_the_sectors_with_small_transverse_momentum_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_none_the_half_turn_2026_09_24.py
---

# Exponential-walk boundary domains: line classification and sector-wise continuity obstruction

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54, 108 and 109 as landed, with the endpoint theory and the boundary-form description of self-adjoint extensions imported at definition level; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within the clocked walk of block 54 and the exponential clock field of blocks 108 and 109, all as landed on main; it reports which self-adjoint realizations keep the clock's scaling identity and the lattice's half-turn about the gradient; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 108 and 109, as landed, found where the walk in an exponential clock field needs a boundary condition at the fast-clock end. On the line it always does. In three dimensions it does in the sectors whose transverse momentum is below `sinh(g/2)`. Block 108 found a circle of chain-separate conditions that keep the clock's scaling identity `U(t)T_a = T_a U(λ^a t)` for every translation. It left the chain-mixing conditions unclassified. This note classifies them all, and asks whether the lattice's own symmetry can pick one.

- **T1: explicit solutions.** On the line, at every energy there are four solutions, explicit series that are entire in the energy. All four are square-summable at the fast end, so the count of block 108 follows directly. On the boundary space the unit shift acts as `±μ` and the shift by two as the number `λ`.
- **T2: the classification.**
  - Every realization keeps the identity for even shifts.
  - The realizations that keep it for every shift form a torus, `L(v₁, v₂)`, with `v₁` and `v₂` on the isotropic circle of `σ₁`.
  - Block 108's circle is the part of the torus that separates the two chains. Every other point is a chain-mixing realization that keeps every shift, for example `v₁ = (1, 0)`, `v₂ = (1, i)`.
- **T3: the half-turn.** The line walk is unchanged by the half-turn of the content about the line, `σ₁`. No realization keeps both the half-turn and the identity for the unit shift.
- **T4: three dimensions.**
  - A sector with `0 < m < sinh(g/2)` has exactly four realizations keeping every shift along the gradient.
  - Each is covariant under the proper cubic rotations fixing the gradient axis.
  - But as the transverse momentum shrinks, each tends to a plane that depends on the direction it shrinks along. So no choice is continuous at the four sectors with `m = 0`, and there, by T3, the half-turn keeps none.
  - On `ℤ³` those four sectors are a null set, so a uniform choice still defines a realization. On a transverse torus the zero sector has weight: no extension preserving transverse translations keeps both the x1 unit-shift identity and the half-turn. Extensions that mix transverse sectors are not classified.

The supplied infinite operator needs boundary-domain data. On the line, imposing the unit-shift identity and the half-turn together is inconsistent. In three dimensions, uniform sector labels are rotation-covariant almost everywhere; this is not a global symmetry obstruction on the infinite transverse lattice. Continuity of the boundary-plane field at zero sine momentum is an additional requirement that the four shift-compatible choices cannot satisfy.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The walk and its clock are supplied clauses. Nothing is adopted.
- **The walk** (block 54, #8570, landed): `H_w = W^{1/2} H W^{1/2}`, with `H = Σ_j σ_j D_j`, `D = (i/2)(T − T†)` and `(Tψ)(x) = ψ(x − 1)`.
- **The field** (blocks 108, #8945, and 109, #8950, landed): `w = λ^{x₁}`, `λ = μ² = e^g > 1`.
  - Block 108 as landed: deficiency indices `(2,2)` on the line through the stated endpoint theory; a circle of translation-compatible chain-separated domains; chain-mixing extensions not classified; the inverse-clock sum is not an arrival-time theorem.
  - Block 109 as landed: in three dimensions `(2,2)` below `m* = sinh(g/2)` and `(0,0)` at or above it.
- **Sectors.** `(Jψ)(n) = (i/2)σ₁[λ^{n−1/2}ψ(n−1) − λ^{n+1/2}ψ(n+1)] + λⁿ(p₂σ₂ + p₃σ₃)ψ(n)`, with `p = (sin k₂, sin k₃)` and `m = |p|`. The line is `p = 0`.
- **Realizations.** Self-adjoint extensions of `J` on finitely supported vectors. Each one is `{ψ in the maximal domain : B_∞(ξ, ψ) = 0 for ξ ∈ L}` for a Lagrangian plane `L` of the boundary form on the fast end's solutions. A realization keeps the identity for `T_a` iff `T_a` maps its plane to itself.
- **Names.** The extension theory is von Neumann's; its description by boundary forms is Glazman's, Krein's and Naimark's. The limit-point/limit-circle alternative for the slow end is Weyl's. The zero-energy solutions `(r/μ)ⁿ v` are Floquet solutions.

## Theorem T1 — solutions at every energy, and the boundary space

*Statement.*
- On the line, `ψ(n) = (ε/μ)ⁿ v_s S(zλ^{−n})` with `σ₁ v_s = s v_s` (`s, ε = ±1`) solves `Jψ = zψ` iff `(isε/2)(S(λX) − S(X/λ)) = X S(X)`.
- The series `c₀ = 1`, `c_j = −2isε c_{j−1}/(λ^j − λ^{−j})` solves it. Its coefficients fall like `λ^{−j²/2}`, so each solution is entire in `z` and behaves as `(±1/μ)ⁿ` at the fast end. All four are square-summable there, at every energy.
- On the zero-energy solutions `(ε/μ)ⁿ v`, the boundary form is `G = diag(−iσ₁, +iσ₁)` in the blocks `ε = +1, −1`, the same at every cut.
- The unit shift acts as `εμ` and the shift by two as `λ`, so `G(T₁x, T₁y) = λ G(x, y)`.

*Proof.* Divide the equation by `(ε/μ)ⁿ λⁿ`; the bonds become `λ^{±1/2}` shifts of `X = zλ^{−n}`. The runner checks the recursion's exact remainder `−c₅X⁶` for all four `(s, ε)`, symbolically in `λ` (B1). It computes the boundary form at four cuts, and the shifts on the boundary space (B2). The slow end is limit point by the imported alternative, so the deficiency indices are `(2,2)`, as in block 108. ∎

## Theorem T2 — the torus of realizations that keep every shift

*Statement.*
- Every Lagrangian plane is kept by the shift by two, a scalar. So every realization keeps `U(t)T₂ = T₂U(λ²t)`.
- A plane kept by the unit shift is `L(v₁, v₂) = span(v₁ ⊗ E₊, v₂ ⊗ E₋)`, because each block is nondegenerate for `G`. It is Lagrangian iff `v₁` and `v₂` are isotropic for `σ₁`: `v = (1, it)` or `(0, 1)`. These form a torus.
- `L(v₁, v₂)` contains a vector of each chain, `(x, σ₃x)` and `(x, −σ₃x)`, iff `v₂ ∥ σ₃v₁`: block 108's circle.
- The point `v₁ = (1, 0)`, `v₂ = (1, i)` is Lagrangian, kept by every shift, and chain-mixing.

*Proof.* The unit shift has eigenvalues `±μ` on the two blocks, so a kept plane is the sum of its intersections with them. The runner checks the isotropy, the Lagrangian condition symbolically in `t₁` and `t₂`, the chain test, and the witness (C1). ∎

## Theorem T3 — the half-turn keeps no unit-shift-compatible line domain

*Statement.* The line walk commutes with `σ₁`, which commutes with the unit shift on the boundary space. A plane kept by both is spanned by joint eigenvectors `(1, ±1) ⊗ E_±`. Their `G`-norms are `∓2i` and `±2i`, never zero. So no realization keeps both the half-turn and the identity for the unit shift.

*Proof.* Direct (D1). ∎

## Theorem T4 — three dimensions, sector by sector

*Statement.*
- The witness is `λ = 4` and `(sin k₂, sin k₃) = (1/4, 1/3)`, where `m = 5/12 < m* = 3/4`. The zero-energy solutions `(r/μ)ⁿ v` with `Nv = ((r − 1/r)/2) v`, `N = sin k₂ σ₃ − sin k₃ σ₂`, have `r = 3/2, −2/3` (for `N = +m`) and `2/3, −3/2` (for `N = −m`). These are the geometric zero-energy solutions a, b, c, d.
- The unit shift acts on them as `4/3, −3, 3, −4/3`.
- The boundary form pairs only a with c and b with d. So the Lagrangian planes kept by the unit shift are exactly `ab`, `ad`, `bc` and `cd`.
- The quarter-turn about `x₁` carries `N(p)` to `N(−p₃, p₂)`, and the half-turn carries it to `N(−p)`. So the labels are kept, and each of the four choices is covariant under the proper cubic rotations fixing `x₁`.
- As `m → 0`, each choice tends to a plane that depends on the direction of `(sin k₂, sin k₃)`. For `bc` it tends to `span((0,1) ⊗ E₊, (1,0) ⊗ E₋)` along `(1, 0)`, but to `span((1,i) ⊗ E₊, (1,−i) ⊗ E₋)` along `(0, 1)`.
- So no choice is continuous at the four sectors with `m = 0`, where T3 applies within the unit-shift-compatible class.

*Proof.*
- The form of two solutions at a cut is `−(i/2)(r_i r_j)^N (r_i + r_j) v_i†σ₁v_j`. Only `r_i r_j = 1` gives a nonzero form that is independent of the cut, and that happens for a–c and b–d.
- Every other pair vanishes. Either each spinor is isotropic, because `σ₁` swaps the two eigenspaces of `N`, or `r_i + r_j = 0`.
- The runner checks every step at the witness, and the limits along both axes (E1–E3). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 108 as landed: chain-mixing extensions not classified; blocks 108-109: which fast-end condition, if any, a symmetry or a clause selects"
source_of_blocker_text: blocks 108 and 109 as landed; the probes problem the-clocked-walk-in-an-exponential-field-self-adjoint-realizations
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a rule for the fast end from the framework (slabs whose far wall recedes); the kernel across the gradient of the four uniform choices; whether the shift by two alone allows a continuous rotation-covariant choice"
conditional_surface_status: "T1-T4 exact, with the endpoint theory and the boundary-form description imported at definition level"
hypothetical_axiom_status: "the walk, the clock and the exponential field are hypotheses; no condition follows from any clause; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 108 (landed) gave the deficiency indices on the line, through the imported endpoint theory, and a circle of translation-compatible chain-separated domains. It left chain-mixing domains unclassified.
  - Block 109 (landed) gave the sector threshold in three dimensions.
  - Block 54 (landed) posed the realization question.
- **The probes attempt.** `the-clocked-walk-in-an-exponential-field-self-adjoint-realizations` a2 (worker `w-macbookpro9927a-j119b`, Claude Opus 5.5, issue #9023) found T1–T4. It was queued as refill f by the supervisor. A Grok referee (`w-macbookpro90c72-jde08`, issue #9068) confirmed T1's fast end, the torus and the four sector realizations. The referee noted that the slow end stays the imported alternative.
- **In the literature.** The extension theory is von Neumann's; its boundary-form description is Glazman's, Krein's and Naimark's; the endpoint alternative is Weyl's. Teschl's treatment of three-term operators is the source block 108 cites.
- **New here:**
  - an independent runner for T1–T4;
  - the classification placed against blocks 108 and 109 as landed;
  - the reading for the third column: the line half-turn excludes every unit-shift-compatible line realization; three-dimensional conclusions require the stated sector and continuity restrictions.

## Exact target and obligation graph

Target: which realizations of the clocked walk keep the scaling identity, and whether a symmetry selects one. The obligations are:
- (O1) the solutions and the boundary space;
- (O2) the classification;
- (O3) the half-turn;
- (O4) three dimensions.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- no realization keeps both the half-turn and the unit-shift identity;
- no choice in three dimensions is continuous across the sectors with `m = 0`.

### N1 — Routes by which the sentences could fail or mislead
1. *Giving up the unit shift.* Keeping only the shift by two admits additional boundary planes; their classification is not supplied here. That may allow a continuous, rotation-covariant choice. It is not treated.
2. *Reflections.* Only rotations about `x₁` are examined.
3. *Locality.* Continuity refers to the boundary-plane field in the fixed zero-energy boundary coordinates. No equivalence or implication between this condition and finite-range or local unbounded-operator domains is established.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The operator theory is imported at definition level and named under Premises and Imports.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| blocks 54, 108, 109 (landed) | the walk, the field, the deficiency counts, the circle | yes |
| probes (#9023; Grok-refereed, #9068) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "every realization keeps the even shift, those keeping every shift form a torus, none on the line keeps both the half-turn and unit-shift identity" | executed: the series' recursion and remainder at every energy (symbolic in `λ`); the boundary form of the four zero-energy solutions | executed: the boundary form at four cuts; the shifts on the boundary space | executed: the torus, the chain test, a chain-mixing witness, the half-turn's joint eigenvectors | executed: a sector with `0 < m < m*`: the four geometric zero-energy solutions, the pairing, the four kept planes, rotation labels and the direction-dependent limits | T1–T3 for the line walk with the endpoint theory imported; T4 sector by sector on `ℤ³` with `w = λ^{x₁}`; the walk, the clock and the field supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A symmetry should pick the fast-end rule." *Reply:* The half-turn about the gradient is the natural candidate, and T3 shows it keeps no realization that respects the clock's scaling. In three dimensions, T4 excludes continuity at zero sine momentum for these four unit-shift-compatible sector choices; covariance alone is possible almost everywhere.
- *Objection:* "On `ℤ³` the bad sectors are a null set." *Reply:* Yes, and the note says so: a uniform choice still defines a realization there. On a transverse torus they carry weight.

### N8 — Cross-cycle echo
- Block 108 found the circle; block 109 found the sectors.
- This note classifies all realizations and shows the lattice's symmetry does not select one.

## Falsifiers

- A Lagrangian plane kept by the unit shift that is not of the form `L(v₁, v₂)`.
- A realization of the line walk kept by both `σ₁` and the unit shift.
- A sector with `0 < m < m*` with a fifth realization keeping every shift.

## Boundaries and non-claims

- The walk, the clock and the exponential field are supplied.
- The operator theory is imported at definition level.
- No realization is proposed, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 54, 108 and 109, restated or placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - von Neumann's extension theory and its boundary-form description (Glazman, Krein, Naimark);
  - Weyl's endpoint alternative;
  - the functional calculus;
  - the direct integral over transverse momenta;
  - exact symbolic arithmetic.

## Review record — historical author provenance

- **Who and when.** Supervisor-run block, the sixty-first since the source-link direction opened; 2026-09-24.
- **Provenance.** The probes attempt (Claude Opus 5.5, #9023) derived the results, and a Grok referee (#9068) confirmed them. The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and blocks 108 and 109 were read as landed (1cb2a082bf).
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_none_the_half_turn_2026_09_24.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.

## General arguments and precise domain restrictions

All three actual parent notes below are premises only in their current narrowed form. In particular no packet-force or arrival claim is imported. The line boundary space is the four-dimensional quotient of the maximal domain by the minimal domain: cut off each zero-energy germ at the slow end. The current endpoint results give deficiency (2,2); the displayed nondegenerate form then identifies these four germs with that quotient. Self-adjoint domains correspond to maximal isotropic two-planes, an explicit standard extension-theory import. The identity J T_a=lambda^a T_a J maps the maximal domain onto itself and maps cutoff germs by the displayed shift matrix modulo the minimal domain. Therefore invariance of the plane supplies operator-domain covariance and the functional-calculus identity, rather than only a formal recurrence identity.

For T1 the exact coefficient modulus is 2^j lambda^(-j(j+1)/2) divided by product_(k=1)^j(1-lambda^(-2k)). The infinite product has positive limit for lambda>1, so the power series has infinite radius. As n tends to the fast end its argument tends to zero; the four leading germs have two distinct parity factors and independent content eigenvectors, so form a fundamental solution basis. This proves entire solutions and fast-end square summability without extrapolating a degree-five check.

For T4 put rho=sqrt(1+m^2)+m>1 and let v+ and v- span the two eigenspaces of N/m. The four roots are rho,-1/rho,1/rho,-rho, with labels a,b,c,d and spinors v+,v+,v-,v-. Below the threshold all four cutoff germs belong to the maximal domain. Their shifts mu/r are distinct. Anticommutation of sigma_1 with N makes the same-eigenspace form vanish and makes the cross-eigenspace pairing nonzero. The root sum cancels a-d and b-c; the only nonzero pairs are a-c and b-d. Hence exactly ab,ad,bc,cd are invariant maximal isotropic planes for every m in the stated open interval, not just at the executed rational witness.

At m approaching zero, use fixed boundary coordinates given by the values at sites 0 and 1 (equivalently the two parity-root germs). The projectors onto v+ and v- are (I +/- N/m)/2 and depend on the sine-momentum direction. Along the positive p2 and p3 axes the four possible limiting planes are distinct, and each label has different limits along those axes. On a small punctured neighborhood the four branches are separated; any continuous selection among them is locally constant in its label and hence constant on the connected punctured neighborhood. Thus switching labels cannot repair the limit. Only the cubic quarter-turn and its powers are spatial symmetries used here, not arbitrary continuous rotations of lattice momentum.

The full three-dimensional assertion is restricted to measurable decomposable extensions, equivalently extensions preserving all transverse translations. Uniform labels on small nonzero sectors together with the unique extension at/above threshold give a measurable direct-integral realization; values on the four zero-sine-momentum points are irrelevant to the infinite-lattice direct integral. No classification of sector-mixing domains or implication for finite-range boundary conditions is claimed. On a periodic transverse torus the zero mode has positive weight, so the line obstruction applies within the translation-preserving class.

## Current canonical dependencies

- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied parent, current scope only.
- [admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_IN_AN_EXPONENTIAL_CLOCK_FIELD_THE_WALKS_DYNAMICS_NEEDS_A_BOUNDARY_CONDITION_AT_THE_FAST_CLOCK_END_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied parent, current scope only.
- [admissibility_rule_in_three_dimensions_the_clocked_walk_needs_a_fast_end_condition_exactly_in_the_sectors_with_small_transverse_momentum_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_IN_THREE_DIMENSIONS_THE_CLOCKED_WALK_NEEDS_A_FAST_END_CONDITION_EXACTLY_IN_THE_SECTORS_WITH_SMALL_TRANSVERSE_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied parent, current scope only.

## Countercontrol for the symmetry qualifier

The boundary plane {(v,v): v in C^2} is maximal isotropic for diag(-i sigma_1,+i sigma_1) and is invariant under diag(sigma_1,sigma_1). It is not invariant under diag(mu I,-mu I). Thus half-turn-compatible line extensions do exist when the unit-shift condition is dropped; the exclusion is only joint.
