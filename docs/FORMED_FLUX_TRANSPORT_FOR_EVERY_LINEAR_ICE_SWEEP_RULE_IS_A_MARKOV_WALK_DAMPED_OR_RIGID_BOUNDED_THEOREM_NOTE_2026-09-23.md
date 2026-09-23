---
claim_id: formed_flux_transport_for_every_linear_ice_sweep_rule_is_a_markov_walk_damped_or_rigid_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formation reading, sweep order, ice rule in arrow form (open PRs 8687, 8701). Sweep rules symmetric under reversing all arrows place the forward minority by a law pi^(j) given the back minority at j. The mean forward arrows are a linear function M b of the back arrows, for all eight back patterns, exactly when sum_j pi^(j) = 1: M is doubly stochastic with columns pi^(j) (of the 27 deterministic rules, exactly the 6 permutations; random mixtures of permutations linear, random laws off the Birkhoff polytope not). For these rules the layer transforms of the mean arrow field obey F_t(q) = M E(q) F_(t-1)(q), E(q) = diag(e^(-i q_j)): a Markov walk on directions. Mixtures with every transition positive have spectral radius below 1 at every quarter-period wavevector with nonzero transverse part (certified exactly by norm bounds on powers); the six permutation rules translate flux rigidly along axes or helices with unimodular monomial powers. The straight-continuation family reproduces open PR 8701's spreading rate (2/9)(1 + p)/(1 - p). No linear sweep rule gives isotropic undamped transport. For every arrow-reversal-symmetric rule, linear or not, a single reversed arrow in the saturated ice state (every arrow forward) walks exactly by the column-stochastic kernel pi^(j), with spectral radius below 1 at the same wavevectors for 20 random rules off the polytope. Nonlinear rules in disordered states are not analysed. No rule, reading or order law is adopted."

upstream_dependencies:
  - minimal_axioms
  - spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03
runner: scripts/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.py
---

# Formed flux transport for every linear ice sweep rule is a Markov walk, damped or rigid

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** next-steps campaign after the TOE derivation campaign by
underdetermination witnesses. Open PR 8701 showed that one family of
sweep rules for ice, straight continuation with probability p, moves
formed flux as a persistent walk. It is ballistic along axes, then
diffusive, and never an undamped isotropic wave. So photon dynamics stays
with the landed supplied Hamiltonian, an open edge of the assembly (open
PR 8648). This block extends that from one family to every sweep rule
whose mean response is linear.

## Result up front

1. **Which rules are linear.** Take rules symmetric under reversing every
   arrow. When the back arrows are not all equal, one is the minority, and
   the rule places the forward minority by a law π^(j) given the back
   minority at j. The mean forward arrows are then a linear function M b of
   the back arrows, for all eight back patterns, exactly when
   Σ_j π^(j) = 1. In that case M is doubly stochastic, with columns π^(j).
   - Of the 27 deterministic rules, exactly the 6 permutations are linear.
   - Every doubly stochastic M arises, as a mixture of the permutation
     rules (Birkhoff).
   - Open PR 8701's family is the line M = p I + (1 - p) J / 3.

2. **The mean arrow field is a Markov walk.** For a linear rule,
   linearity of expectation gives, layer by layer,
   F_t(q) = M E(q) F_(t-1)(q), with E(q) = diag(e^(-i q_j)). A flux
   fluctuation's mean moves as a walk whose direction changes by the
   Markov kernel M.

3. **Damped or rigid, never an isotropic wave.**
   - A mixture with every transition positive has spectral radius below 1
     at every wavevector with nonzero transverse part.
   - The six permutation rules have unimodular, monomial powers. They
     translate flux rigidly along axes or helices, neither damping it nor
     spreading it.
   - Partially mixing rules split into blocks of these two kinds. Their
     undamped modes are still rigid motion along lattice vectors.

   No linear sweep rule gives isotropic undamped transport. The
   straight-continuation family reproduces open PR 8701's spreading rate
   (2/9)(1 + p)/(1 - p).

4. **Every rule, one defect in the saturated state.** In the saturated
   ice state every arrow points forward along the sweep, so every vertex
   passes its arrows on. Take any rule, linear or not, and reverse one
   arrow. It enters each vertex as the back minority and leaves along i
   with probability π^(j)_i, while the rest stays saturated. So it walks
   exactly by the column-stochastic kernel π. With every transition
   positive, the same damping holds; a deterministic rule moves it along a
   rigid path.

5. **What this means for the photon lane.** Across every linear sweep
   rule, formation moves flux either diffusively or by rigid translation.
   The same holds for every rule in the saturated state's dilute-defect
   regime.
   Undamped isotropic transport, the photon's propagation, does not come
   from formation in this class. Photon dynamics stays with the supplied
   Hamiltonian, as the assembly's open edge records. Nonlinear rules in
   disordered states are not analysed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "photon dynamics rests on the landed quantum Hamiltonian (open edge of open PR 8648); formed flux shown damped only for one rule family (open PR 8701)"
source_of_blocker_text: open_prs_8648_8701
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "record on the photon-dynamics edge: every linear sweep rule gives damped or rigid transport; nonlinear rules remain open"
conditional_surface_status: "formation reading; sweep order; ice rule in arrow form; rules symmetric under arrow reversal with linear mean response"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "an exact characterisation of linear rules, an exact recursion, exact norm certificates of damping, and exact rigid powers"
```

## Premises and declared objects

- **Arrows.** σ = ±1 on links, with σ = +1 along +e_i. The ice rule in
  arrow form: at each vertex the forward arrows sum to the back arrows'
  sum (open PRs 8687, 8701).
- **Sweep rules.** A law for the three forward arrows given the three back
  arrows, symmetric under reversing all six. When the back sum is ±3 the
  forward arrows equal the back ones. Otherwise the rule places the
  forward minority by the law π^(j), where j is the back minority.
- **Layers.** t = x_1 + x_2 + x_3. F_t(q) is the transform of the mean
  arrows on layer t.

## Prior art and what is new

- Open PR 8687: directed ice, with the uniform-consistent rule M = J/3.
- Open PR 8701: the straight-continuation family and its spreading rate.
- Standard mathematics:
  - Birkhoff's theorem on doubly stochastic matrices;
  - Markov chains and their occupation variances;
  - Wielandt's condition for a unimodular spectral radius.
- New here:
  - the characterisation of linear rules;
  - the Markov-walk recursion for all of them;
  - the damping and rigidity dichotomy.

## Theorem 1 — Linear rules

For the back pattern 1 - 2e_j, the mean forward arrows are 1 - 2π^(j).
For the all-plus pattern they are 1. A linear map M therefore needs
M e_j = π^(j) and M 1 = 1. This happens exactly when Σ_j π^(j) = 1, and
reversing every arrow then gives the remaining patterns. The runner
checks all 27 deterministic rules, 40 random mixtures of permutations and
40 random laws off the polytope, over all eight back patterns exactly.

## Theorem 2 — Damped or rigid

T(q) = M E(q) has spectral radius at most 1. By Wielandt's condition,
equality needs phases consistent along every allowed transition. When
every transition is allowed, that forces q_1 ≡ q_2 ≡ q_3, so the
transverse part is 0. The runner certifies spectral radius below 1 at all
60 quarter-period wavevectors with nonzero transverse part, for 7 such
rules, by a power with infinity norm below 1.

For a permutation, T(q) is monomial with unimodular entries, and so are
its powers: rigid translation.

## Theorem 3 — One defect in the saturated state

In the saturated state every back sum is 3, and the rule passes the
arrows on. A single reversed arrow entering along j makes the back sum 1
with minority j. The rule places the forward minority at i with
probability π^(j)_i, and every other vertex stays saturated. So the
defect's direction is a Markov chain with transition j → i of
probability π^(j)_i. Its matrix is column-stochastic with spectral
radius 1, and Wielandt's condition applies as in Theorem 2. The runner
checks the forward laws exactly for 20 random rules off the Birkhoff
polytope. It certifies spectral radius below 1 at all 60 transverse grid
wavevectors.

## No-Go Discipline Gate

The negative content is scoped: linear, arrow-reversal-symmetric sweep
rules, mean transport.

- **N1 alternative routes.** The following are outside this block:
  - nonlinear rules in disordered states;
  - rules that see more than the back arrows;
  - orders other than sweeps;
  - fluctuations beyond the mean.
- **N2 wall independence.** Exact algebra, exact recursions and exact
  norm certificates.
- **N3 hidden walls.** Linearity is a declared class. The recursion is
  for means.
- **N4 residual matching.** The photon-dynamics residual is nonlinear
  formation rules, or the supplied Hamiltonian.
- **N5 rhetoric audit.** "No isotropic undamped transport" refers to the
  linear class.
- **N6 partial-closure paths.** Nonlinear rules in disordered states;
  second moments.
- **N7 steelman.** For formed photon dynamics: rigid translation is
  undamped. Against it: it is anisotropic, and everything else damps.
  Both are recorded.
- **N8 cross-cycle echo.** Open PRs 8687 and 8701 are cited;
  straight continuation reproduces open PR 8701's rate.

## Falsifiers

- A linear rule with M not doubly stochastic falsifies Theorem 1.
- A doubly stochastic mixture with every transition positive and
  spectral radius 1 at a nonzero transverse grid wavevector falsifies
  Theorem 2.

## Boundaries and non-claims

- The linear class, and one defect in the saturated state for every
  rule; nonlinear rules in disordered states are not analysed.
- Mean transport only.
- No rule, reading or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

Open PRs 8687 and 8701 are cited. Birkhoff's theorem, Markov chains and
Wielandt's condition are standard mathematics. No audit grade, no new
axiom, no new primitive, no new comparator and no new framing is
imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:**
  - linearity is checked over all eight patterns from exact laws;
  - the damping certificates are exact norm bounds;
  - the spreading rate is compared with open PR 8701's closed form.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| mutant | change | outcome |
|---|---|---|
| minority placed with the majority sign | output signs swapped | caught (4 FAIL) |
| all-equal patterns not kept | forward arrows reversed | caught (4 FAIL) |
| matrix transposed | columns read as rows | caught (3 FAIL) |
| damping certificate always granted | false branch returns true | caught (1 FAIL) |
| phase grid off by one | e^(-i pi) to 1 | caught (2 FAIL) |
| grid keeps the diagonal wavevectors | zero transverse part not excluded | caught (2 FAIL) |
| occupation rate without the factor 2 | 2 Z h to Z h | caught (1 FAIL) |
| complex product sign error | minus to plus | caught (2 FAIL) |
| saturated state leaks a second reversed arrow | one minority to two | caught (1 FAIL) |

9 of 9 caught. The certificate mutant was first missed; a control was
added in which the certificate must fail for every permutation rule.

- **Vacuity guard:** counts of rules, wavevectors and rates are printed.
- **Budget:** 6 checks, stdout 1758 characters (ceiling 6000), under a
  second (ceiling 900 s), exact Fractions and Gaussian rationals.

## Verification

```bash
python3 scripts/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=6 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/formed_flux_transport_for_every_linear_ice_sweep_rule_birkhoff_markov_walks_2026_09_23.txt`.
