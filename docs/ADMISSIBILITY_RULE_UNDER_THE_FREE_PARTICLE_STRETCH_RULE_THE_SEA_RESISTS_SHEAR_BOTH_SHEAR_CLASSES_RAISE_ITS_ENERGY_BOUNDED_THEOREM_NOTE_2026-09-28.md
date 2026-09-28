---
claim_id: admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_both_shear_classes_raise_its_energy_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed and block 147's filled negative-energy sea as landed (energy per site -average_k E, each reduced-zone pair counted once), with the walk stretched by the free-particle rule of blocks 184, 185 and 187 (pushed): (T1) for any per-axis completion F = s - lam s c^2 + lam^2 s(1/2 + a s^2 + b s^4) + O(lam^3), lam = log l, the sea's second-order energy is -sum_a lam_a^2 <s_a^2(1/2 + a s_a^2 + b s_a^4)/E> - (1/2)<(sum lam_a^2 s_a^2 c_a^4 - (sum lam_a s_a^2 c_a^2)^2/E^2)/E>, which is block 183 T2 when b = 0; (T2) block 184's rule has a = -4 and b = 7/2; (T3) for a volume-preserving diagonal stretch its second-order sea energy is exactly 0 on the side-4 torus, 4/27 + (34 sqrt 3 + 65 sqrt 6)/864 on side 6 and positive on side 8 (lam = (1, -1, 0)), while block 183's reach-three completions (q2 = -1/2) give negative values on sides 6 and 8, and with block 139's staggered mass (mu^2 = 1/4, 1) the side-6 value stays positive; (T4) through block 187's spectrum along g = exp(eps S), the off-diagonal volume-preserving shear raises the sea's energy too (25/648 + (9 sqrt 6 - 8 sqrt 3)/1728 per eps^2 on side 6, positive on side 8), and the diagonal case reproduces T3; (T5) on the infinite lattice, by exact outward-rounded interval sums (t = tan(k/2), 60005 adaptive boxes), the diagonal value for lam = (1, -1, 0) lies between 1/16 and 7/20 and the off-diagonal one between 1/40 and 3/40 per eps^2, both positive. By cubic symmetry the two classes are the two irreducible pieces of the traceless strains, so the second variation is positive definite on every volume-preserving direction at g = 1. So if the member sees the sea, under the free-particle rule the sea resists shear, reversing block 183's result for the reach-three completions. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_2026_09_28.py
---

# Under the free-particle stretch rule the sea resists shear: both shear classes raise its energy

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 69 and 147 as landed; blocks 183, 184, 185 and 187 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within blocks 69 and 147 as landed on main (the two-step coupling, and the filled sea with its energy per site) and asks whether the sea gives way under shear when the walk is stretched by the free-particle rule; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The zero-of-energy row of the third column asks whether the member sees the filled sea. Its worked consequences were first found under block 62's frame (blocks 147, 155, 167). Block 183 (pushed) re-derived the shear one under the two-step coupling, for block 176's reach-three completions. There the sea gives way under a volume-preserving stretch iff the completion's second-order number satisfies `q₂ < q₂*`, and both named completions do. Blocks 184, 185 and 187 (pushed) then found the free-particle rule, which is not a reach-three completion. This note asks the shear question again under that rule.

- **T1: the formula for any per-axis completion.** With second-order term `s(½ + a s² + b s⁴)`, the sea's second-order energy is `−Σ_a λ_a²⟨s_a²(½ + a s_a² + b s_a⁴)/E⟩` plus an interband term. Block 183 T2 is the case `b = 0`, `a = −(1 + q₂)`.
- **T2: the rule's numbers.** Block 184's rule has `a = −4` and `b = 7/2`.
- **T3: a diagonal shear raises the sea's energy.** For a volume-preserving diagonal stretch the second-order sea energy is:
  - exactly `0` on the side-4 torus;
  - `4/27 + (34√3 + 65√6)/864 ≈ +0.40` on side 6, for `λ = (1, −1, 0)`;
  - positive on side 8.
  - Block 183's reach-three completions give negative values on sides 6 and 8. With block 139's staggered mass the rule's side-6 value stays positive.
- **T4: so does an off-diagonal shear.** Through block 187's spectrum, the off-diagonal volume-preserving shear raises the sea's energy too: `25/648 + (9√6 − 8√3)/1728 ≈ +0.043` per `ε²` on side 6, and positive on side 8.
- **Positive definite** (third version). By cubic symmetry the traceless strains split into the diagonal and the off-diagonal pieces, and any invariant quadratic form is one number on each. So T3–T5 make the second variation positive definite on every volume-preserving direction at `g = 1`. The referee's floating fit is `E₂ = 0.025229 ΣS_aa² + 0.049109 Σ_{a<b}S_ab²` per `ε²`.
- **T5: on the infinite lattice too** (second version). Exact interval enclosures of the two lattice integrals, with outward rounding, give the following; both are positive.
  - Diagonal, for `λ = (1, −1, 0)`: between `1/16` and `7/20`.
  - Off-diagonal: between `1/40` and `3/40` per `ε²`.
  - The floating values are `0.2018` and `0.0491`.

In plain terms: if the member feels the filled sea, the earlier finding was that the sea gives way when the lattice is sheared. That finding used a short-range stretch rule. Under the rule in which every wave slows as a free particle does, the opposite holds: a small uniform shear costs the sea energy, in every direction of shear. So for small uniform shears this worry goes away under the free-particle rule. Long shear waves are not treated. The comparison with block 183 is between two supplied rules, so it is not independent evidence about the sea.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-28) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 69 and 147 are used as landed on main. Blocks 183, 184, 185 and 187 are pushed and placed; the facts used from them are re-derived (runner B1, C1, E1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
- **The sea** (block 147), quoted: "Counting each reduced-zone pair once gives the sea energy per site", with the massive form "`-average_k sqrt(mu²+sum sin²(k)/ell²)`". Here the walk is stretched by the rule instead of `1/ℓ`, so `E_sea = −average_k E` with `E² = |F|² + μ²`.
- **Per-axis completions.** `F_a = F(k_a; λ_a)` with `F = s − λ s c² + λ² s(½ + a s² + b s⁴) + O(λ³)`, `λ = log ℓ`. Block 183's reach-three family is `b = 0`, `a = −(1 + q₂)`.
- **Volume-preserving stretches.** Diagonal: `Σλ_a = 0`. General: `g = exp(εS)` with `S` traceless, so `det g = 1` exactly.
- **Block 187's spectrum** (pushed). Along `g = exp(εS)`, `W = E² − μ²` satisfies `W = W₀ + εw₁ + ε²w₂ + O(ε³)`. Here `w₁ = −¼p·S·p`, `w₂ = −⅛p·S²·p − ¼Σ_ab S_ab p_a ∂_b w₁`, and `p = ∇W₀ = sin 2k`.

## Domain qualifications

- Uniform volume-preserving stretches at second order. Long shear waves (block 183 T6) are not re-derived for the rule.
- Exact values are on the side-4, side-6 and side-8 tori. The infinite lattice is enclosed exactly by interval sums (T5), for the massless sea.
- The seen sea is block 147's supplied source reading; whether the member sees it remains the owner's row.

## Theorem T1 — the formula for any per-axis completion

*Statement.* For `F = s + d₁ + d₂` with `d₁` first order and `d₂` second order, the second-order term of `E = (|F|² + μ²)^{1/2}` is `s·d₂/E + (|d₁|² − (s·d₁)²/E²)/(2E)`. With `d₁_a = −λ_a s_a c_a²` and `d₂_a = λ_a² s_a(½ + a s_a² + b s_a⁴)`, the sea's second-order energy is

`−Σ_a λ_a²⟨s_a²(½ + a s_a² + b s_a⁴)/E⟩ − ½⟨(Σ_a λ_a² s_a² c_a⁴ − (Σ_a λ_a s_a² c_a²)²/E²)/E⟩`.

*Proof.* Series (runner B1, massless; the mass enters only through `E`). With `b = 0` and `a = −(1 + q₂)` this is block 183 T2. ∎

## Theorem T2 — the rule's numbers

*Statement.* Block 184's rule is `F = s − λ s c² + λ² s(½ − 4s² + (7/2)s⁴) + O(λ³)`, so `a = −4` and `b = 7/2`.

*Proof.* From `F = s + τ s c² + τ² s(3 − 10s² + 7s⁴)/2 + O(τ³)` with `τ = (1 − e^{2λ})/2` (block 184 T2; block 182 T4(b)). Runner C1. ∎

## Theorem T3 — a diagonal shear raises the sea's energy

*Statement.* For `λ = (1, −1, 0)`, the rule's second-order sea energy is:
- `0` on the side-4 torus, where every label is fixed (block 186 T2);
- `4/27 + (34√3 + 65√6)/864` on side 6;
- `17/256 + (756√10 + 11925√2 + 7400√6)/230400` on side 8.

Both nonzero values are positive. `λ = (1, 1, −2)` gives three times the side-6 value, in proportion to `Σλ²`. Block 183's reach-three completions with `q₂ = −½` give negative values on sides 6 and 8. With block 139's staggered mass, `μ² = ¼` and `μ² = 1`, the rule's side-6 value stays positive and the reach-three value stays negative.

*Proof.* Exact label sums (runner D1, D2). ∎

## Theorem T4 — so does an off-diagonal shear

*Statement.* Along `g = exp(εS)` with `S = e₁e₂ + e₂e₁`, the sea's second-order energy per `ε²` is:
- `0` on side 4;
- `25/648 + (9√6 − 8√3)/1728` on side 6;
- positive on side 8.

For `S = diag(1, −1, 0)` the same route gives exactly a quarter of T3's values, since `g = exp(εS)` is `λ = (ε/2, −ε/2, 0)`.

*Proof.* The second-order expansion of `W^{1/2}` from block 187's `w₁` and `w₂`, summed exactly over labels (runner E1). ∎

## Theorem T5 — on the infinite lattice too

*Statement.* The infinite-lattice values are the averages over the Brillouin zone, the limits of the torus averages. Under the rule:
- (a) for `λ = (1, −1, 0)` the second-order sea energy lies in `[1/16, 7/20]`;
- (b) along `g = exp(εS)` with `S = e₁e₂ + e₂e₁` it lies in `[1/40, 3/40]` per `ε²`.

Both are positive.

*Proof.*
- Both integrands depend on `k` only through `x_a = sin² k_a`. So the zone average equals the average over the octant `[0, π/2]³`.
- With `t = tan(k/2)`, `x = 4t²/(1 + t²)²` increases on `t ∈ [0, 1]`, and `dk = 2dt/(1 + t²)`.
- In `x` the diagonal integrand is `−Σ_{a=1,2} x_a p(x_a)/S − ½[x₁x₂(2 − x₁ − x₂)² + x₁x₃(1 − x₁)² + x₂x₃(1 − x₂)²]/S³`, with `p(x) = ½ − 4x + (7/2)x²` and `S² = Σx_a`. The interband term of T1 is written as a sum of squares:
  - `(Σλ²x c⁴)(Σx) − (Σλ x c²)² = ½Σ_ij x_ix_j(λ_ic_i² − λ_jc_j²)²`.
- The off-diagonal integrand is `−w₂/(2S) + w₁²/(8S³)`, where:
  - `w₁² = 4x₁x₂(1 − x₁)(1 − x₂)`;
  - `w₂ = −½(y₁ + y₂) + y₁(1 − 2x₂) + y₂(1 − 2x₁)`, with `y_a = x_a(1 − x_a)`.
- Interval arithmetic on integers scaled by `2⁶⁴`, rounded outward, encloses each integrand times `Π 2/(1 + t_a²)` on each box of an adaptive subdivision of `[0, 1]³` (60000 boxes).
- The box at the species corner is bounded by `|f| ≤ 2S` for the diagonal and `|f| ≤ S` for the off-diagonal. These hold since `max|p| = 9/14`, `x_ix_j ≤ S⁴/4` and `y_a ≤ x_a`.
- The octant's volume `(π/2)³` is bracketed by `(333/212)³` and `(355/226)³`.
- The torus averages are sums of a bounded function, continuous once set to `0` at the species points, so they tend to the zone average (named import).
- Runner I1 and I2. ∎

With block 191 (pushed), the member's uniform shear modes therefore have a gap on the infinite lattice, and not only on the tori.

## What this settles and what it does not

- **Settled.**
  - Under the free-particle rule, the seen sea's energy rises under every small uniform volume-preserving shear: on the tori examined and with the mass examined, and on the infinite lattice for the massless sea (T5 and cubic symmetry). It falls under the reach-three completions.
  - Hidden assumptions, declared:
    - the labels and the site count are held;
    - the sea is the filled negative band;
    - the mass is unchanged by the rule;
    - the rule is smooth for eigenvalues of `g` in `(0, 2)`.
    This is a local statement at `g = 1`, and the comparison with block 183 is between two supplied rules.
- **For the third column (the zero-of-energy row).** Under the member's own coupling completed by the free-particle rule, the sea's two worked dangers soften:
  - the bounce needs a small source (block 186);
  - the sea no longer gives way under uniform shear (this note).
  - The row's remaining cost is the comparator reading: the sea as content has negative energy and pressure.
- **Not settled.**
  - Long shear waves under the rule; block 183 T6's relation assumed a completion local in the strain.
  - The massive sea on the infinite lattice.
  - Whether the member should see the sea: that is the owner's row.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 183 (pushed): the sea gives way under shear for reach-three completions; the free-particle rule (184-187) is not reach three"
source_of_blocker_text: admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; long shear waves under the rule"
conditional_surface_status: "exact on the side-4, side-6 and side-8 tori, under the free-particle rule and block 147's sea"
hypothetical_axiom_status: "the rule and the seen sea are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Blocks 69, 139 and 147 (landed): the coupling, the staggered mass and the sea.
  - Block 183 (pushed): the reach-three formula and its result.
  - Blocks 184, 185 and 187 (pushed): the free-particle rule and its metric spectrum.
- **In the literature.** The comparator's filled Dirac sea under a background metric is a standard vacuum-energy problem; Parker's particle creation concerns its time dependence. None is used as authority.
- **New here.**
  - The formula with a reach-five term (T1).
  - The reversal under the free-particle rule for both shear classes (T3, T4).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: the shear consequence of the zero-of-energy row under the free-particle rule. The obligations are:
- (O1) the premises (A3);
- (O2) the formula (B1);
- (O3) the rule's numbers (C1);
- (O4) the diagonal values, the massive sea and the reach-three comparison (D1, D2);
- (O5) the off-diagonal values and the consistency of the two routes (E1).

## No-Go Discipline Gate

The note's negative sentence: under the free-particle rule, the seen sea does not give way under volume-preserving uniform shear on the tori examined.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *Finite-size effects.* Side 4 is degenerate (0). Sides 6 and 8 are positive, and the infinite-lattice values are enclosed exactly and are positive (T5). CLOSED.
2. *The mass.* It is positive on side 6 at `μ² = ¼, 1`; the floating infinite-lattice values are positive up to `μ = 2`. ATTEMPTED; stated.
3. *Long waves.* Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the rule, the seen sea, volume preservation, uniform strain, and the tori.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling | yes (quoted, A3) |
| block 147 (landed) | the sea's energy per site | yes (quoted, A3) |
| blocks 183, 184, 185, 187 (pushed) | the formula, the rule, its spectrum | re-derived (B1, C1, E1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "under the free-particle rule the seen sea's energy rises under both shear classes" | executed: the expansion; the rule's numbers | executed: exact label sums on sides 4, 6, 8; the massive sea on side 6 | executed: the off-diagonal route | executed: the two routes agree | executed: the infinite lattice by exact enclosure (T5); not executed: long waves |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Finite tori prove nothing about the infinite lattice."
  - *Reply:* T5 (second version) encloses both infinite-lattice values exactly, and both are positive.

### N8 — Cross-cycle echo
- Blocks 155 and 167 (frame): the sea gives way.
- Block 183 (reach three): it gives way iff `q₂ < q₂*`, and it does for both named completions.
- This note (the free-particle rule): it does not.

## Falsifiers

- A torus of even side at least 6 on which the rule's second-order sea energy under a volume-preserving shear is negative.
- A difference between T5's integrands and T1's or block 187's summands (runner I3 checks the identity symbolically).

## Boundaries and non-claims

- Uniform volume-preserving shear at second order; the tori examined.
- The rule and the seen sea are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 69 and 147 (landed), quoted. Blocks 139, 183, 184, 185 and 187 placed and re-derived.
- Named standard imports, at definition level:
  - second-order expansion of a norm;
  - matrix exponential;
  - exact symbolic arithmetic with radicals;
  - interval arithmetic with outward rounding;
  - the invariant quadratic forms of the cubic group on traceless symmetric matrices (one number per irreducible piece, Schur's lemma);
  - the limit of lattice sums of a continuous function on the torus.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-28, at the start of the owner's third 12-hour campaign.
- **Provenance.** The supervisor's own derivation.
- **Referee (2026-09-28; Claude Sonnet 5, same vendor family as the author, a separate model and session).** Verdict: confirmed with scope corrections, wording only.
  - Independently re-derived: T2's coefficients; T3 and T4 from the rule itself at 40 digits; T5's floating values on tori up to side 256. The referee read the interval code and found no defect, and wrote its own enclosure (diagonal `[0.0766, 0.3298]`, off-diagonal `[0.0366, 0.0619]`).
  - The corrections applied in this third version:
    - the plain summary narrowed to small uniform shears;
    - the comparison with block 183 described as between supplied rules;
    - hidden assumptions declared;
    - the box count;
    - the positive-definite corollary, which the referee pointed out.
- **Floating control in scratch.**
  - The infinite lattice by midpoint quadrature: the diagonal value is `+0.1009 Σλ²`, and a finite-difference check with the exact rule agrees. The off-diagonal value for `g = exp(εS)` is `+0.0491` per `ε²`.
  - The massive diagonal values are positive for `μ` up to `2`.
  - The reach-three value, `−0.0804 Σλ²`, reproduces block 183.
- **Before writing.** Block 183's formula and threshold are its own; this note extends the formula by a reach-five term and evaluates the free-particle rule, which block 183 did not name.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G. The second version adds family I (T5) with its own mutation.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_2026_09_28.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
