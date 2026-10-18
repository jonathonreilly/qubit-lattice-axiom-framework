---
claim_id: curvature_member_closure_with_matter_forces_one_common_cone_and_the_lorentzian_sign_and_has_an_order_a_squared_obstruction_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models only: the 2026-09-24 curvature-member clauses (block-62 staggered placement, R1, kinetic Legendre form at beta = -alpha, four-corner face timing) with the curvature term written C = kin + s K R1, s = +-1, plus a supplied real site scalar H_m(N) = sum_x N_x (pi_x^2/2 + mu phi_x^2/2) + sum_b Nbar_b (c/2)(Delta_b phi)^2 (Nbar_b = endpoint mean) and its supplied symmetric relabelling G_m[xi] = sum_b xi_b (Delta_b phi)(pi_x + pi_{x+e})/2; Poisson bracket {q,p} = +1; flat strain; power counting h, P ~ eps, phi, pi ~ eps^(1/2). (1) Exact on every torus of side >= 3 at order eps of {C(N),C(M)}: {H_m(N),H_m(M)} = G_m[-c xi~], xi~_b = N_(x+e) M_x - N_x M_(x+e); the total closes into one relabelling G_g[xi] + G_m[xi] for all lapse pairs iff c = -sK/(4 alpha); with the supplied K > 0, alpha > 0 and c > 0 this forces s = -1 (the hyperbolic, Lorentzian-signature deformation algebra; s = +1 closes only with c < 0, the Euclidean one); two species close iff c1 = c2 = K/(4 alpha). (2) Block 101's action carries the linearised-GR sign and its Legendre transform carries -K R1; read in the standard convention, the 2026-09-24 runner's bracket and displayed closing field are those of +K R1 - harmless for that note's gravity-only closure statement (both signs close) but inconsistent once this matter is coupled. (3) Exact rank certificates (L = 3; ansatz A also L = 4; three sampled configurations): no translation-invariant coupling in three stated ansatze (114 matched-timing, 708 free-lapse-placement, 804 longer-range operators) closes the pi-pi sector of {G[xi], C(N)} at order phi^2 into H_m(N') for any N'; the obstruction is the O(a^2) monomial -(1/4) xi_b (N_(x+e) - N_x)(pi_(x+e) - pi_x)^2; removing it, a verified exact solution exists on the sampled configurations (positive control, not a general proof). (4) Continuum leading order (exact jet calculus, nine-coefficient coupling ansatz): {C,C} forces c = K/(4 alpha); {G,C} selects the metric-variational stress of H_m(g) with unit strength plus one trace weight lambda, which the supplied scalar-lapse rule sets to 0. Not claimed: exact lattice closure at any order beyond eps, other matter fields or discretisations, nonlinear strain, any value of Newton's constant, or any physical identification."
upstream_dependencies:
  - admissibility_rule_the_curvature_members_constraint_algebra_closes_on_the_lattice_only_at_beta_equals_minus_alpha_and_there_the_walkers_own_states_cannot_be_its_content_bounded_theorem_note_2026-09-24
  - admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
runner: scripts/curvature_member_closure_with_matter_common_cone_2026_10_18.py
---

# Curvature-member closure with a supplied scalar: one common cone, the Lorentzian sign, and an O(a²) obstruction

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact within the supplied clauses. A same-model-family fresh-context check confirmed the core claims. Nothing is adopted.

## Question

The 2026-09-24 note shows that the curvature member's lapse constraints close on the lattice. The setting is flat strain, linear order in the momentum, and `β = −α`. Add a supplied scalar field with its own lapse-weighted Hamiltonian and relabelling. Three questions follow:

- Does the total algebra still close?
- What does closure require of the matter's propagation speed and of the curvature term's sign?
- Does any local coupling of the matter to the strain close the relabelling–lapse bracket `{G, C}` exactly on the lattice?

## Result

1. **Order ε of `{C, C}`: one common cone, exact on the lattice.**
   - `{H_m(N), H_m(M)} = G_m[−c ξ̃]` exactly, with `ξ̃_b = N_{x+e} M_x − N_x M_{x+e}`. The mass term cancels.
   - The gravity part gives `G_g[(sK/(4α)) ξ̃]`; this is 09-24 T1 for either sign `s`.
   - So the total closes into one relabelling `G_g[ξ] + G_m[ξ]` for every lapse pair iff `c = −sK/(4α)`.
   - The premises supply `K > 0`, `α > 0` and `c > 0`. Under them closure forces `s = −1`, that is `C = kin − K R1 + H_m`. This is the hyperbolic (Lorentzian-signature) deformation algebra. The opposite sign closes only with `c < 0`, which makes the matter elliptic: the Euclidean algebra.
   - Two species close iff `c₁ = c₂ = K/(4α)`. **Every species shares one matter cone.** The value `K = 4α` gives speed 1 in lattice units.
   - The endpoint-mean bond lapse is paired with the symmetric `G_m`. A one-endpoint bond lapse closes instead into the one-sided relabelling `Σ_b ξ_b (Δ_b φ) π_{x+e}`. So the timing is fixed only relative to the supplied relabelling.
2. **The curvature sign of block 101, and a correction to the 09-24 runner.**
   - `R1 = ∂_i∂_j h_ij − ∇² tr h` is the linearised scalar curvature of `g = δ + h`. So block 101's action `L = kin + K w̄ (u R1 + R2) − e u` has, in its `u R1` and `u e` terms, the sign of the linearisation of `K w̄ N√g R − N ρ` with `N = 1 + u`.
   - Its Legendre transform has `∂H/∂u = −K w̄ R1 + e`. The constraint therefore carries `−K R1`, that is `s = −1`.
   - The 09-24 runner computes `K (b₁ − b₂)`, with `b₁ = ∂R1[N]/∂h · ∂kin[M]/∂P`, and displays the closing field `ξ = +(K/(4α)) ξ̃`. In the standard convention `{h, P} = +1`, in which `G[ξ] = Σ P·δ_ξ h` generates `h → h + δ_ξ h`, these are the bracket of `C = kin + K R1`, that is `s = +1`. That sign is opposite to the runner's own action, and it gives the Euclidean structure function. In the continuum limit the displayed field is `ξ ≈ −κ(N∇M − M∇N)`.
   - This is harmless for 09-24's gravity-only statement, since T1's closure and its `β = −α` and timing conditions hold for both signs. It becomes inconsistent once matter with `c > 0` is coupled in the same convention.
   - Under the reversed convention `{P, h} = +1`, the same runner formula is the bracket of `−K R1`, and no mismatch arises. The convention-independent content is `sign(c) = −sign(sK/α)`, with `s` the sign in the constraint and one bracket convention used for both sectors.
3. **Order φ² of `{G, C}`: an exact lattice obstruction.**
   - Couple the matter to the strain by a lapse-weighted term `Σ lapse · h · Q(φ, π)`. At `h = 0` the π–π part of `{G_g[ξ] + G_m[ξ], H_m(N) + coupling(N)}` is

     `½ Σ_b ξ_b (π_x + π_{x+e})(N_{x+e} π_{x+e} − N_x π_x) − Σ lapse · (δ_ξ h) · Q_ππ`.

     Closure requires it to equal the π–π part of `H_m(N')` for some `N'`. At this order, any additional `G` term on the right is P-linear or φπ and does not contribute.
   - The ansätze impose no lattice symmetry, and their coefficients are translation-invariant:
     - **A (114 operators).** Matched timing: a site lapse on `h_jj`, the four-corner mean on `h_ij`. The π pairs come from the 7-point star and from the face corners.
     - **C (708 operators).** The lapse placement is free per term, within the star or the face corners.
     - **B (804 operators).** Longer range: 19-point diagonal pairs and 12-point face pairs.
   - No ansatz closes. The L = 3 torus is used, and also L = 4 for A, with three sampled integer configurations and `N'` free per configuration. Each verdict is certified by an exact rational vector `y` with `yᵀA = 0` and `yᵀb ≠ 0`.
   - A local identity on Z³ would restrict to periodic configurations, and hence to the torus. So the certificates also exclude closure on Z³ for the same translation-invariant families.
   - **The obstruction monomial.** Per bond, the matter term splits into diagonal `π_z²` pieces, which `N'` can absorb, and the cross term

     `ob = ½ ξ_b (N_{x+e} − N_x)[π_x π_{x+e} − (π_x² + π_{x+e}²)/2] = −¼ ξ_b (N_{x+e} − N_x)(π_{x+e} − π_x)²`.

     It carries two differences, so it is `O(a²)` relative to `ξ·∇N π²`.
   - **Positive control.** With `ob` subtracted, ansatz A has an exactly verified solution on the same sampled configurations (L = 3 and L = 4). This is evidence that `ob` is the whole obstruction within A. It is not a proof for all configurations.
4. **Continuum leading order (exact sympy jet calculus).**
   - `{C, C}`, with `C = kin − K R1 + H_m`, closes into `G_g[ξ₀] + G_m[ξ₀]`, `ξ₀ = κ(N∇M − M∇N)`, iff `c = K/(4α)`.
   - The coupling ansatz has nine coefficients: `T_jj` with seven terms and `U_ij` with two, with no isotropy imposed. Over it, `{G, C}` at order φ² is `H_m(s₁ ξ·∇N + s₂ N div ξ)` exactly on a one-parameter family. That family is the metric-variational stress of `H_m(g) = π²/(2√g) + √g (c g^{ij}∂_iφ∂_jφ + μφ²)/2` at unit strength, plus `λ δ_ij` times the `H_m` density, with `s₁ = 1` and `s₂ = −2λ`.
   - `{C, C}` alone does not fix the coupling: `T = 0` with structure function `ξ' = 0` solves its `O(hφπ)` part.
   - With the supplied scalar-lapse rule `s₂ = 0`, the coupling is unique and equals the metric-variational stress at `c = K/(4α)`. The `{C, C}` structure function is then forced to `ξ'_i = −κ h_ij ξ₀_j`, that is `g^{ij} = δ^{ij} − h^{ij}`.
   - A nonzero `λ` shifts the structure-function trace by `r₂ = −2λ`. Species with different `λ` therefore cannot share one `ξ'`, so `λ` is common to all species.
5. **A long-wavelength diagnostic, reported as found (`--e6`, floating point, one configuration, not gating).** The diagnostic takes the `{G, C}` φ² residual with the lattice image of the metric-variational stress as the coupling, and lattice transport `N'`. The runner reproduces the campaign values:

   | L | base `|{G_m,H_m}|` | residual (stress) | ratio | residual (no coupling) |
   |---|---|---|---|---|
   | 6 | 3.68 | 8.96 | 2.43 | 20.1 |
   | 8 | 1.72 | 7.51 | 4.36 | 26.2 |
   | 12 | 17.4 | 6.02 | 0.345 | 40.7 |
   | 16 | 39.5 | 5.42 | 0.137 | 59.7 |
   | 24 | 103 | 4.99 | 0.048 | 113 |

   - The absolute residual is roughly flat, falling slowly.
   - The falling ratio comes mainly from the growing base bracket.
   - At L = 6 and 8 the ratio exceeds 1.
   - The coupling removes most of the uncoupled residual at large L. That fits a small lattice artefact, but one configuration does not establish a scaling law, and no power law is fitted.

## How this bears on the gravity lane (interpretation, not a claim)

- **Which K sets the cone (campaign block B21, independently checked; continuum).** In the supplied member one K multiplies both the first- and second-order curvature terms. Invariantly, the cone is fixed by the second-order (TT) coefficient: the canonical rescaling (h, P) → (ρh, P/ρ) preserves every bracket while moving the ratio of the two coefficients. So "c = K/(4α)" here reads as "every matter cone equals the graviton's TT cone", given the member's single K.

- **The pattern.** Within these supplied models, requiring one lapse/relabelling algebra does three things:
  - it ties every matter field's cone to the gravity cone `K/(4α)`;
  - it fixes the curvature sign that the action already carries;
  - in the continuum, it selects the metric-variational stress as the source with universal strength.

  This is the known hypersurface-deformation route to universal coupling, realised here at order ε on the lattice.
- **The lattice limit.** Exact closure of `{G, C}` at order φ² fails at `O(a²)` in this discretisation. A lattice version of "the source is the Noether stress" therefore needs one of two things: a modified matter discretisation or relabelling, or a statement up to controlled `O(a²)` terms. Neither is supplied here.
- **Not shown.**
  - Newton's constant: nothing fixes it.
  - Fields other than one real scalar.
  - Nonlinear strain.
  - Whether the walker of the 09-24 note can be such matter.

## Premises

- **Axioms used.** None beyond the lattice and its translations. The memo `docs/MINIMAL_AXIOMS_2026-06-29.md` supplies no dynamics or time metric, so every clause below is supplied.
- **Supplied (gravity).** The 09-24 clauses as landed: the block-62 placement, `R1`, the kinetic Legendre form at `β = −α`, four-corner face timing, and `G_g[ξ] = Σ P·δ_ξ h`. Also block 101's action (09-23 note) for the sign in Result 2. The parameters satisfy `K > 0` and `α > 0`.
- **Supplied (matter).** The site scalar `H_m(N)` with endpoint-mean bond lapse and `c > 0`, and its symmetric relabelling `G_m`.
- **Supplied (coupling and rules).** The stated coupling ansätze; `δ_ξ h_ij = ∂_iξ_j + ∂_jξ_i`; and, in Result 4 only, the scalar-lapse rule `s₂ = 0`.
- **Convention.** The Poisson bracket `{q, p} = +1` for `(h, P)` and `(φ, π)`, applied to both sectors.
- **Standard facts used.**
  - The linearised scalar curvature.
  - Legendre transformation.
  - The Fredholm alternative for linear systems over Q.
  - Rational reconstruction: a certificate found modulo p is then verified exactly over Q.

## Proof sketches

- **Result 1.**
  - *The matter bracket.* Write `H_m(N) = ½ πᵀΛ_N π + ½ φᵀW_N φ`, with `Λ_N = diag N` and `W_N = μ diag N + c Σ_b N̄_b d_b d_bᵀ`. Then `{H_m(N), H_m(M)} = φᵀ(W_N Λ_M − W_M Λ_N)π`. The mass part cancels because diagonal matrices commute.
  - *Per bond.* `N̄(M_y π_y − M_x π_x) − M̄(N_y π_y − N_x π_x) = ½(N_x M_y − N_y M_x)(π_x + π_y)`, which gives `G_m[−c ξ̃]`.
  - *The iff.* `G_g` is P-linear and `G_m` is φπ, so a common `ξ` must satisfy `G_m[ξ + c ξ̃] = 0` and `G_g[ξ − (sK/(4α)) ξ̃] = 0`. On side ≥ 3 the bond monomials of `G_m` are independent, so `ξ = −c ξ̃`. Then `G_g[(c + sK/(4α)) ξ̃] = 0`. For `N = δ₀` and `M = 1`, `ξ̃` is a nonconstant gradient with `G_g[ξ̃] ≠ 0`. So `c = −sK/(4α)`.
  - *Two species.* Each species forces `ξ = −c_k ξ̃`, so `c₁ = c₂`.
  - *One-endpoint lapse.* The same algebra gives `(N_x M_y − M_x N_y)(Δφ) π_y`.
- **Result 2.** The symbolic linearisation of `R(δ + εh)`, and the Legendre transform of the `u`-dependent action.
- **Result 3.** Translation-invariant coefficients are shared across configurations, and `N'` is free in each. An exact left-null vector `y` with `yᵀb ≠ 0` certifies that the system has no solution. `C0` is the polynomial identity for `ob`.
- **Result 4.** Euler-operator tests in the lapse: a local functional that is linear in `N` vanishes for all `N` iff its Euler derivative vanishes. Solving the resulting coefficient equations exactly gives the stated solution sets.

## Relation to prior work

- **Closure forcing a common signature, a common cone and universal coupling.**
  - Teitelboim, Ann. Phys. 79, 542 (1973): the common signature and light cone from the surface-deformation algebra.
  - Kuchař, J. Math. Phys. 15, 708 (1974) and 17, 777, 792, 801 (1976).
  - Hojman, Kuchař and Teitelboim, Ann. Phys. 96, 88 (1976): geometrodynamics regained.
  - Deser, Gen. Rel. Grav. 1, 9 (1970): self-coupling and universal coupling to the stress.
  - Düll, Schuller, Stritzelberger and Wolz, PRD 97, 084036 (2018): gravitational closure, the constructive version for general matter.
  - The continuum part of Result 4, and the sign-and-cone logic of Result 1, are these known results specialised to this model.
- **Lattice breaking of the constraint algebra.**
  - Renteln and Smolin, CQG 6, 275 (1989).
  - Gambini and Pullin (consistent discretisations; e.g. PRL 90, 021301 (2003)).
  - Bahr and Dittrich, CQG 26, 225011 (2009), and related work on broken diffeomorphism symmetry in discrete gravity.
  - That lattice discretisations break `{G, C}` beyond leading order is expected.
- **Repository.**
  - 09-24 (T1: gravity-only closure at `β = −α`).
  - 09-23, block 101 (the action and the clock constraint).
  - 09-25 notes on `α = K/4` (one light cone for the walk's two-step content; `K/(4α) = 1` there).
- **New here, and narrow.**
  - The exact order-ε lattice realisation in this discretisation, with matter.
  - The pairing of bond-lapse timing with the chosen `G_m`.
  - The explicit `O(a²)` obstruction monomial, with exact non-closure certificates for three ansätze.
  - The sign mismatch between the 09-24 runner, read in the standard convention, and block 101's action.

## No-Go Discipline Gate

The negative sentences:
- the total order-ε algebra does not close for `c ≠ −sK/(4α)`, nor for two unequal species speeds;
- with `c > 0`, `s = +1` does not close;
- no coupling in the three stated ansätze closes `{G, C}` at order φ² on the lattice.

- **N1 — routes by which they could fail or mislead.**
  - Matter discretisations or relabellings other than `H_m` and `G_m`. For example, an improved `G_m` with a counterterm, or a field-dependent relabelling, might absorb `ob`.
  - Couplings outside the stated ranges or timings.
  - Nonlocal or field-dependent lapse timings.
  - Fields other than a scalar.
  - Higher strain orders.
- **N2/N3 — scope.**
  - Result 1 is exact on every torus of side ≥ 3. Its sampled tables at L = 3 and 4 corroborate the analytic proof.
  - Result 3 holds for the stated finite families, on L = 3 (and L = 4 for A), with three seeded configurations. Non-closure certificates for sampled configurations prove non-closure for every configuration. The positive control is sampled evidence only.
- **N4 — inputs.**
  - Exact rationals throughout the gating tests.
  - The Part C certificates are found by elimination modulo Mersenne primes, and then verified exactly over Q. Modular ranks are reported only as lower bounds.
  - E6 is floating point and non-gating.
- **N5 — wording.**
  - "Lorentzian" and "Euclidean" name the sign of the deformation algebra (hyperbolic or elliptic matter). They are not a physical identification.
  - "Common cone" means the equal coefficient `c = K/(4α)`.
  - "O(a²)" means two lattice differences in `ob`.
- **N6/N7 — strongest objections.**
  - *"The sign result only restates `c > 0`."*
    - Reply: yes. The theorem is the relation `c = −sK/(4α)`.
    - The sign follows only given the supplied positivity. Caveat 1 of the check says exactly this.
  - *"The obstruction is an artefact of one discretisation."*
    - Reply: yes. It is stated as conditional on `H_m` and `G_m`.
  - *"The 09-24 'error' is a convention."*
    - Reply: partly. Under `{P, h} = +1` the runner formula is the `−K R1` bracket.
    - The convention-free statement is the one in Result 2.
    - This note asks only that one convention be used for both sectors.
- **N8 — earlier claims.**
  - The 09-24 T1 statement is unchanged.
  - Only its displayed structure-function sign, read in `{h, P} = +1`, is flagged for any matter-coupled use.

## Independent check

A fresh-context agent of the same model family as the author re-derived the core claims; it is not independent in model lineage. Its implementation differs from the author's polynomial Poisson engine:
- matrix-form brackets;
- a position-space `R1`, built separately;
- different constants (`α = 2/5`, `K = 7/3`, `μ = 5/2`);
- larger ansätze with no symmetry imposed;
- exact rank computations over Q.

- **Confirmed.**
  - The analytic E2 bracket, and closure iff `c = −sK/(4α)` (L = 3, 4).
  - The two-species condition `c₁ = c₂`.
  - The block-101 sign: its Lagrangian is the linearised `N√g R − Nρ`, so the Hamiltonian carries `−K R1`.
  - Non-closure for all three ansätze (114, 708, 804 operators), and closure of the positive control.
- **Caveats raised, adopted here.**
  - The "forced GR sign" needs `c > 0` as a stated premise.
  - "Endpoint-mean timing required" holds only relative to the symmetric `G_m`. One-endpoint timing closes into a one-sided relabelling.
  - The obstruction is conditional on the `H_m` and `G_m` discretisation.
  - E6 had been reported selectively. The full table is given above.
- **Attribution.** The literature list above follows the check's attribution.

This runner incorporates the check's matrix path (A6) and its Part C ansätze. Re-running this runner is therefore not a further independent check.

## Verification

```bash
python3 scripts/curvature_member_closure_with_matter_common_cone_2026_10_18.py
```

Expected: `TOTAL: PASS=26 FAIL=0` (about one minute; Python 3 and sympy). Parts:
- A: lattice order ε, at L = 3 and L = 4, plus the matrix path;
- B: the sign;
- C: the φ² certificates;
- D: the continuum.

Optional:
- `--quick` skips the L = 4 repeats;
- `--e6 [L ...]` prints the non-gating diagnostic of Result 5; L = 24 takes about five minutes.

## Load-bearing sources

- [09-24 constraint-closure note](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [09-23 clock-constraint note (block 101)](ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
