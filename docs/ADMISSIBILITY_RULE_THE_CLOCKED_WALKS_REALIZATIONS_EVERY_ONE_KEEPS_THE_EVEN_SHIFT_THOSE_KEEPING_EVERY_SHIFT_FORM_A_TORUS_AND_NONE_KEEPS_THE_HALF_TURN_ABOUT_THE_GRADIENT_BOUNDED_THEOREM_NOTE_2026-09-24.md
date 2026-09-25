---
claim_id: admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_and_none_keeps_the_half_turn_about_the_gradient_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 54's walk with the exponential clock field of blocks 108 and 109, all as landed on main; supplied. Exact, with the endpoint theory and the boundary-form description of self-adjoint extensions imported at definition level: (T1) on the line, at every energy z the four solutions (eps/mu)^n v_s sum_j c_j (z lambda^-n)^j, c_j = -2 i s eps c_(j-1)/(lambda^j - lambda^-j), are entire in z and square-summable at the fast end; on the zero-energy solutions the boundary form is diag(-i sigma_1, i sigma_1), the unit shift acts as eps mu and the shift by two as the scalar lambda. (T2) every realization keeps the even-shift identity; those keeping U(t)T_a = T_a U(lambda^a t) for every a are exactly L(v1, v2) = span(v1 (x) E+, v2 (x) E-) with v1, v2 isotropic for sigma_1 - a torus, containing block 108's circle of chain-separate realizations (v2 parallel to sigma_3 v1) and chain-mixing ones such as v1 = (1, 0), v2 = (1, i). (T3) the line walk commutes with the half-turn sigma_1 about the line, and no realization keeps both the half-turn and the identity for the unit shift. (T4) in three dimensions with w = lambda^(x1), a sector with 0 < |(sin k2, sin k3)| < sinh(g/2) has exactly four realizations keeping every x1-shift (the isotropic pairs ab, ad, bc, cd of its geometric zero-energy solutions); each is covariant under the rotations about x1, but as the transverse momentum goes to zero each tends to a plane that depends on its direction, so no choice is continuous at the four sectors with m = 0, where the half-turn keeps none. Harvest block from a Grok-refereed probes attempt, re-checked by an independent runner. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_none_the_half_turn_2026_09_24.py
---

# The clocked walk's realizations: every one keeps the even shift, those keeping every shift form a torus, and none keeps the half-turn about the gradient

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
  - Each is covariant under the rotations about the gradient.
  - But as the transverse momentum shrinks, each tends to a plane that depends on the direction it shrinks along. So no choice is continuous at the four sectors with `m = 0`, and there, by T3, the half-turn keeps none.
  - On `ℤ³` those four sectors are a null set, so a uniform choice still defines a realization. On a transverse torus they carry weight, and no realization keeps both the identity and the half-turn.

In plain terms: the walker needs a rule at the end where the clocks run infinitely fast, and the clauses do not supply one. This note lists every rule that respects how the clock field stretches time. There is a whole two-parameter family of them. None of them respects the lattice's own half-turn about the direction of the clock gradient. In three dimensions, any rule that works for every direction of travel has to jump at a few special directions. So the lattice's symmetries cannot pick the rule; if anything they rule them all out. The missing rule is another thing the records do not supply.

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

## Theorem T3 — the half-turn keeps none of them

*Statement.* The line walk commutes with `σ₁`, which commutes with the unit shift on the boundary space. A plane kept by both is spanned by joint eigenvectors `(1, ±1) ⊗ E_±`. Their `G`-norms are `∓2i` and `±2i`, never zero. So no realization keeps both the half-turn and the identity for the unit shift.

*Proof.* Direct (D1). ∎

## Theorem T4 — three dimensions, sector by sector

*Statement.*
- The witness is `λ = 4` and `(sin k₂, sin k₃) = (1/4, 1/3)`, where `m = 5/12 < m* = 3/4`. The zero-energy solutions `(r/μ)ⁿ v` with `Nv = ((r − 1/r)/2) v`, `N = sin k₂ σ₃ − sin k₃ σ₂`, have `r = 3/2, −2/3` (for `N = +m`) and `2/3, −3/2` (for `N = −m`). These are the geometric zero-energy solutions a, b, c, d.
- The unit shift acts on them as `4/3, −3, 3, −4/3`.
- The boundary form pairs only a with c and b with d. So the Lagrangian planes kept by the unit shift are exactly `ab`, `ad`, `bc` and `cd`.
- The quarter-turn about `x₁` carries `N(p)` to `N(−p₃, p₂)`, and the half-turn carries it to `N(−p)`. So the labels are kept, and each of the four choices is covariant under the rotations about `x₁`.
- As `m → 0`, each choice tends to a plane that depends on the direction of `(sin k₂, sin k₃)`. For `bc` it tends to `span((0,1) ⊗ E₊, (1,0) ⊗ E₋)` along `(1, 0)`, but to `span((1,i) ⊗ E₊, (1,−i) ⊗ E₋)` along `(0, 1)`.
- So no choice is continuous at the four sectors with `m = 0`, where T3 applies.

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
  - the reading for the third column: the lattice's half-turn about the gradient excludes every realization that keeps the clock's scaling identity, so neither a clause nor a symmetry supplies the fast-end rule.

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
1. *Giving up the unit shift.* Keeping only the shift by two leaves a sphere of choices in each sector. That may allow a continuous, rotation-covariant choice. It is not treated.
2. *Reflections.* Only rotations about `x₁` are examined.
3. *Locality.* "Continuous in the transverse momentum" stands in for a condition of finite range across the gradient. The implication is standard for translation-invariant finite-range operators, and it is used, not proved.

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
| "every realization keeps the even shift, those keeping every shift form a torus, none keeps the half-turn" | executed: the series' recursion and remainder at every energy (symbolic in `λ`); the boundary form of the four zero-energy solutions | executed: the boundary form at four cuts; the shifts on the boundary space | executed: the torus, the chain test, a chain-mixing witness, the half-turn's joint eigenvectors | executed: a sector with `0 < m < m*`: the four geometric zero-energy solutions, the pairing, the four kept planes, rotation labels and the direction-dependent limits | T1–T3 for the line walk with the endpoint theory imported; T4 sector by sector on `ℤ³` with `w = λ^{x₁}`; the walk, the clock and the field supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A symmetry should pick the fast-end rule." *Reply:* The half-turn about the gradient is the natural candidate, and T3 shows it keeps no realization that respects the clock's scaling. In three dimensions, T4 shows that rotation covariance and continuity across sectors cannot both hold.
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

## Review record

- **Who and when.** Supervisor-run block, the sixty-first since the source-link direction opened; 2026-09-24.
- **Provenance.** The probes attempt (Claude Opus 5.5, #9023) derived the results, and a Grok referee (#9068) confirmed them. The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and blocks 108 and 109 were read as landed (1cb2a082bf).
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_clocked_walks_realizations_every_one_keeps_the_even_shift_those_keeping_every_shift_form_a_torus_none_the_half_turn_2026_09_24.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
