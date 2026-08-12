---
claim_id: admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "For the repository's supplied four-dimensional Kuhn/Coxeter Regge-plus-deficit-square action at alpha=1/1024, the flat repaired Hessian has exactly four vertex-displacement null directions and satisfies the corresponding Ward identity at every one of the 2,254 nonzero modes on periodic L=3 through L=6 carriers. Reconstructing the interval-certified Block-21 Bundle-B affine continuation gives a full-rank fifteen-by-fifteen length-length Hessian at every one of those modes, with inherited-generator residuals 0.199804055 and 0.441617350 on two generic-ray points. Correction: the supplied source is linear and its reactions and constraints are affine, so their length-length Hessians vanish identically; the displayed matrix is the complete length-length block of that affine KKT Lagrangian, not a bare block missing affine connection terms. The rank-ten affine constraints freeze all ten metric tangents, leave only five nonmetric edge modes, and have rank four on the generic displacement columns. The finite-rank result therefore characterizes a gauge-fixed nonmetric ensemble surrogate and is not a physical curved-metric gravity test. A covariant nonlinear source/generator law would replace rather than complete the supplied affine law. No gravitational anomaly, nonlinear gravity no-go, selected law, perfect action, physical inner product, full-Z3 theorem, axiom amendment, audit verdict, or TOE percentage movement is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_regge_curvature_squared_sourced_continuation_constraint_localization_boundary_bounded_theorem_note_2026-08-10
  - admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_bounded_theorem_note_2026-08-11
runner: scripts/admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_2026_08_12.py
---

# Affine Regge Pseudo-Constraint / Perfect-Action Route Gate (Corrected)

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** preserve the finite Hessian census after correcting its physical
interpretation: the Block-21 continuation is a five-nonmetric-mode affine
ensemble surrogate, not the first genuinely curved metric/source test.

**Audit-status authority:** independent audit lane only. This source note
authors no audit verdict and predicts none.

**Primary runner:**
[admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_2026_08_12.py](../scripts/admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_2026_08_12.py)

## Result Up Front

Block 53 solved a real problem: a local, positive-energy, causal finite-depth
update exists for the supplied *linear* two-transverse-traceless sector. It did
not solve nonlinear gravity. The nonlinear question is whether the four
gravity constraints remain an exact first-class system away from the flat
anchor when the same Record source and same geometry law are evolved.

On the supplied Regge-plus-deficit-square family

~~~text
S_alpha = sum_h A_h (epsilon_h + alpha epsilon_h^2),
alpha = 1/1024,                                               (1)
~~~

the answer for the length-length Hessian on the Block-21 affine continuation
is sharply negative, but only for that gauge-fixed nonmetric surrogate.

At flatness, the Hessian `Q_0(k)` and the four exact vertex-displacement
columns `Gamma(k)` obey

~~~text
Q_0(k) Gamma(k) = 0.                                         (2)
~~~

The runner exhausts every nonzero momentum on periodic four-tori
`L=3,4,5,6`: all `2,254` matrices have rank eleven, hence exactly four null
directions, and the maximum Ward residual is `1.544e-13`.

The runner then reconstructs rather than imports the Block-21 Bundle-B source
continuation at coupling `1/100`. Its five normal coordinates agree with the
parent interval-certified root and its maximum nonzero deficit is
`0.058009759...`. Differentiating the same bare action (1) at that point gives

~~~text
rank Q_J(k) = 15                                             (3)
~~~

at every one of the same `2,254` nonzero modes. The smallest observed absolute
eigenvalue is `4.488559e-6`. On the generic ray
`k=x(1,0.7,-0.4,0.2)`, direct inherited-generator residuals are

| `x` | flat `||Q_0 Gamma||` | sourced `||Q_J Gamma||` |
|---:|---:|---:|
| `0.4` | `3.10e-14` | `0.199804055` |
| `1.0` | `7.15e-14` | `0.441617350` |

This is not evidence that gravity cannot work. The Block-21 source is linear,
and its reaction and constraint functions are affine. Their second length
derivatives therefore vanish: `Q_J` is the complete length-length block of the
supplied affine KKT Lagrangian, not a bare block missing affine reaction terms.
The linear source and affine reaction terms have identically zero
length-length Hessians.

That clarification changes the interpretation. The affine constraint matrix
has rank ten, freezes all ten metric tangents, and leaves only the five
nonmetric edge directions used by the continuation. At generic momentum its
product with the four displacement columns has rank four, so the constraints
explicitly remove those directions. Equations (2)--(3) therefore characterize
a gauge-fixed, nonmetric ensemble surrogate. A covariant nonlinear source,
generator, and connection law would be a replacement joint law, not a term
silently omitted from the supplied affine law. This result does not test a
genuinely nonuniform curved metric response.

This correction withdraws the original route decision based on the affine
surrogate alone. Primary literature on
canonical Regge calculus reports that curved solutions on an ordinary fixed
discretization generally lose exact gauge symmetry and replace constraints by
background-dependent pseudo-constraints; it equates recovery of a consistent
constraint algebra with recovery of an exactly symmetric action
([Bahr--Dittrich, 2009](https://arxiv.org/abs/0905.1670)). The constructive
routes are not mysterious: improved/perfect actions are designed to recover
the continuum dynamics and symmetries on a discrete carrier
([Bahr--Dittrich, 2009](https://arxiv.org/abs/0907.4323)), while canonical
Pachner evolution implements local changes of triangulation on extended phase
spaces and exactly tracks the covariant discrete dynamics
([Dittrich--Hoehn, 2011](https://arxiv.org/abs/1108.1974)). These citations are
primary-literature route context, not framework premises or evidence that the
required four-dimensional construction already exists here.

The immediate high-value target is therefore a genuinely nonuniform full-edge
solution driven by an exactly conserved zero-total metric source, with only
the flat displacement directions gauge-fixed. If that branch also loses the
nonlinear Ward identity, a source-complete improved/perfect action or a
variable-triangulation Pachner/tent law becomes the constructive target. This
block alone does not establish that antecedent. It closes no TOE lane and
moves no percentage.

## Exact Target Contract And Proof-Obligation Graph

| Obligation | Evidence | Disposition |
|---|---|---|
| reproduce the repaired flat four-null sector | all `2,254` nonzero periodic modes have rank eleven and machine-zero `Q_0 Gamma` | closed on `L=3...6` |
| reconstruct the declared nonlinear sourced point | parent five-normal equations solved again; nonzero deficits and coordinates checked | closed for Bundle B at coupling `1/100` |
| test inherited flat generators at the affine point | full ranks plus two direct generic-ray residuals | closed for the complete length-length block on the declared finite inventory |
| distinguish affine surrogate from physical gravity | linear source and affine constraints have zero length-length Hessian; ten constraints freeze all metric tangents and remove all four displacement columns | closed as a correction |
| construct a complete nonlinear constraint algebra | no source-complete invariant action or canonical constraint brackets are built | open |
| construct a perfect action or Pachner update | literature supplies route mechanisms only | open |
| bind the update to Record formation, clock, source, and physical state | Block-46/53 joint-law fields | open |
| prove full-`Z^3`, continuous-zone, or nonlinear stability | no extrapolation from four finite carriers | open |
| select or amend the framework law | owner/derivation decision | not attempted |

The immediate missing test is precise:

> Solve a genuinely nonuniform full-edge branch for a conserved zero-total
> metric source while fixing only the flat displacement directions, and test
> the joint nonlinear Ward residual through second order in source strength.

The strongest closure lemma beyond that test remains:

> Construct one local or controlled-quasilocal joint Record--geometry action
> or canonical move family whose source-complete discrete Noether identity
> yields four first-class nonlinear constraints, whose flat quadratic limit is
> the Block-44/53 two-TT law, and whose physical update is positive, causal,
> and projectively consistent.

The second lemma is target-equivalent to nonlinear gravity closure on this
campaign surface. The affine-surrogate result proves neither lemma.

## 1. Reconstructed Objects

The calculation consumes only repository-local science objects:

- the current [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md), used only
  to enforce the dynamics and source/action boundary;
- the actual fifteen-edge, fifty-hinge Kuhn/Coxeter Regge carrier;
- the Block-20 deficit-square repair at `alpha=1/1024`;
- the Block-21 Bundle-B source row and five-normal continuation equation;
- the exact lattice vertex-displacement map `Gamma(k)`; and
- Block 53's requirement that nonlinear constraint propagation replace the
  linear TT-only construction.

The runner solves the sourced equations again. It does not place the five
displayed coordinates directly into the Hessian. It also reconstructs every
area, deficit, and deficit-Hessian contribution through the parent action
code. The numerical rank tolerance is `1e-9`; the smallest sourced gap on the
finite inventory is more than three orders of magnitude above it.

## 2. Why The Flat Identity Is Exact

For an exactly invariant discrete action `S(e)`, a gauge generator `R(e)` obeys

~~~text
S_,a R^a_alpha = 0.                                       (4)
~~~

Differentiating gives

~~~text
S_,ab R^b_alpha + S_,a R^a_alpha,b = 0.                  (5)
~~~

At an unsourced stationary point the second term vanishes, so the Hessian has
the gauge null `S_,ab R^b_alpha=0`. This is the discrete Noether implication
behind (2). The flat repaired action leaves the same ten metric tangents at
zero momentum and the same four displacement columns at every nonzero mode.

Equation (5) is also why an off-background Hessian null test cannot be read in
isolation. In the supplied affine KKT law the linear source and affine
reaction terms contribute no length-length Hessian, while the fixed affine
constraints are not a covariant gauge system: they explicitly cut the metric
and displacement directions. A physical nonlinear law must instead transform
its source and generator jointly. The exhaustive rank result is therefore an
affine-surrogate route gate, not evidence that an omitted affine Hessian term
would restore the nulls.

## 3. Finite Inventory

The complete nonzero-mode census is:

| `L` | modes | flat rank counts | affine length-block rank counts |
|---:|---:|---:|---:|
| `3` | `80` | `rank 11: 80` | `rank 15: 80` |
| `4` | `255` | `rank 11: 255` | `rank 15: 255` |
| `5` | `624` | `rank 11: 624` | `rank 15: 624` |
| `6` | `1,295` | `rank 11: 1,295` | `rank 15: 1,295` |
| total | `2,254` | `rank 11: 2,254` | `rank 15: 2,254` |

The finite census is deliberately not promoted to a continuous-Brillouin-zone
theorem. Its role is to reject the idea that the Block-21 loss is an isolated
one-ray numerical accident. Conversely, it does not exclude isolated zeros
off these root-of-unity grids, nor would such zeros alone construct the needed
four-dimensional constraint bundle.

## 4. Route Decision And Axiom Boundary

The current axioms do not select (1), the sourced continuation, an improved
action, a refinement prescription, a Pachner sequence, or any physical
Hamiltonian. The three approved primitives supply units, Euclidean kinetic
form isotropy, and permission for pointwise evaluation at a realized state;
they supply no nonlinear constraint law.

No axiom is amended here. If a complete improved/perfect or Pachner joint law
is derived from current structure, the constitutional question disappears. If
construction repeatedly reaches an extensional fork, the Block-46 conclusion
still applies: any owner choice must reference one exact law binding the Record
instrument, event precedence, clock, constraint intertwiner, and source
decoder. A generic sentence that “constraints propagate” would leave every
physical coefficient and move rule unselected.

## Promotion Value Gate

| Gate | Assessment |
|---|---|
| V1 -- specific correction | identifies the prior continuation as a five-nonmetric-mode, gauge-fixed affine ensemble rather than a physical curved metric |
| V2 -- exact next action | retires fixed-action TT projection and coefficient tuning; promotes improved/perfect action and variable-triangulation construction |
| V3 -- framework contact | uses the actual campaign Regge action, sourced continuation, gauge generator, and Block-53 update target |
| V4 -- marginal content | adds an exhaustive `2,254`-mode full-rank contrast and a primary-literature formulation correction not present in prior blocks |
| V5 -- independently reviewable | runner reconstructs both backgrounds, prints all resolution classes, and uses wide rank/finite-residual margins |

The value gate passes for a route-decision theorem. It does not authorize a
TOE percentage move: no nonlinear constraint algebra is constructed.

## No-Go Discipline Gate

The narrow negative is only:

> The inherited flat vertex-displacement columns are not null directions of
> the complete length-length block on the declared Block-21 affine nonmetric
> continuation across the executed `L=3...6` inventory.

It is not “Regge gravity fails,” “no discrete gravity has first-class
constraints,” or “no local nonlinear completion exists.”

### N1 -- Alternative Route Enumeration

| normalized route | attack and outcome | marker |
|---|---|---|
| affine Regge-plus-deficit-square length block | Reconstruct the five-nonmetric-mode affine continuation and test the inherited generators directly; all `2,254` nonzero modes are full rank. | `ATTEMPTED`; surrogate only |
| genuine nonuniform conserved metric source | Solve the full-edge branch while fixing only displacement directions, then test the second-order Ward identity. | `UNTRIED` in this block; preferred immediate test |
| complete source/constraint action | Replace the affine surrogate with a dynamical source, transformed generator, and nonlinear constraint identity required by (5). | `ATTEMPTED` as formulation diagnosis; construction remains live |
| improved/perfect action | Refine and integrate interior data so the coarse action recovers exact symmetry; primary literature gives explicit lower-dimensional and restricted four-dimensional constructions, not this campaign's source-complete law. | `ATTEMPTED` as primary-literature route check; construction remains live |
| variable-triangulation Pachner/tent evolution | Replace a fixed lattice tick by canonical local moves on extended phase spaces; the route is mathematically consistent but not yet bound to this Record/source carrier. | `ATTEMPTED` as primary-literature route check; construction remains live |
| independent connection/tetrad constraint system | Reinstate connection, lapse, and shift variables so constraint preservation is an exact local identity rather than a TT projection; Blocks 35--42 give partial carriers but no selected stable nonlinear law. | `RULED OUT BY PRIOR` only as already-complete; route remains live |
| continuum-limit pseudo-constraint convergence | Allow background-dependent pseudo-constraints at finite spacing and prove convergence to first-class constraints under refinement; no controlled limit is executed here. | `ATTEMPTED` as literature route check; construction remains live |

Because multiple concrete escape routes remain live, the universal no-go fails.
The shipped claim is the narrow executed fixed-action statement only.

### N2 -- Wall-Independence Audit

After collapsing downstream consequences, three independent walls remain:

- `W_A`: construct/select the complete invariant nonlinear geometry action or
  canonical move family;
- `W_S`: bind the Record transition to a conserved general-matter source and
  the same constraint identity; and
- `W_P`: construct the positive physical state/inner product and causal
  history realization.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `W_A,W_S` | no | no | yes |
| `W_A,W_P` | no | no | yes |
| `W_S,W_P` | no | no | yes |

The four nonlinear constraints are not counted separately from `W_A`; they
are the defining Noether/first-class obligation of that action.

### N3 -- Hidden-Wall Scan

“Sourced background” means exactly the Block-21 affine KKT continuation and is
an explicit fixture. “Canonical” describes the Pachner formulation in the
cited paper, not framework authority. “Perfect action” is a route class, not
an assumed solution. “By construction” is avoided as evidence: the runner
recomputes ranks and residuals. The proper-cubic lattice, action coefficient,
source coupling, affine reactions, Euclidean signature, finite carriers, and
rank tolerance are all explicit boundaries rather than hidden conditions.

### N4 -- Residual Matching

| witness | witness residual | current residual | match? |
|---|---|---|---:|
| [Block 21](ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), Sections 5--6 | five-normal affine continuation with all metric tangents fixed | inherited flat-generator nullity on the same nonmetric surrogate | yes after the present interpretation correction |
| [Block 53](ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md), Sections 5 and N2 | nonlinear extension of the linear two-TT constraint circuit | identify whether fixed-action projection is that extension | yes |
| Bahr--Dittrich 2009 | fixed-discretization curved Regge gauge breaking and pseudo-constraints | possible formulation class after a genuine curved metric test | no as direct witness; route context only |
| Bahr--Dittrich perfect actions | symmetry recovery through improved/perfect action | live repair route | no as negative witness; retained only as counterroute |
| Dittrich--Hoehn Pachner evolution | consistent varying-phase-space canonical evolution | live repair route | no as negative witness; retained only as counterroute |

No prior TT-projection or generic lattice-gravity no-go is used as evidence.

### N5 -- Rhetoric And Resolution Audit

The runner checks all fifteen edge rows (`per_element`), the homogeneous
fifty-hinge cell (`per_site`), every nonzero mode on four declared finite
carriers (`per_mode`), and the exact Block-21-to-Block-53 handoff
(`per_block`). It explicitly prints that continuous-zone and full-`Z^3`
claims are not executed (`lattice_wide`). Accordingly the claim says
“full rank on the executed finite inventory,” never “no gauge symmetry exists
on every lattice” or “gravity is impossible.”

### N6 -- Partial-Closure And Primitive Scan

The registered scale, kinetic-isotropy, and realized-state primitives close
none of `W_A,W_S,W_P`; their current source text explicitly supplies no
dynamics, selector, state, boundary, or dimensionless law. Existing partial
closure paths are substantial: Block 53 supplies the linear causal update,
Block 39 supplies a fixed-background increasing-region Record phase, Blocks
35--38 supply connection/plaquette carriers, and the primary literature
supplies the improved-action and Pachner mechanisms. These are construction
routes, not reasons to add an axiom. A downstream imported perfect action with
an explicit later import-retirement audit is also legitimate. The note
therefore does not say a new axiom is required.

### N7 -- Steelman

A hostile reviewer should object that the Hessian is not incomplete: linear
source and affine reaction terms have identically zero length-length Hessians.
The real defect is that the ten affine constraints freeze all metric tangents
and explicitly remove the displacement columns, so the continuation is not a
physical curved-metric test. That steelman succeeds and is adopted here.
Moreover, a dynamical source law, refined/perfect action, or Pachner evolution
can restore a joint Noether identity. The claim is forced down to the narrow
affine-surrogate diagnostic.

### N8 -- Cross-Cycle Echo

Blocks 19--21 initially tried affine constraints and coefficient repair; Block
21 correctly kept a covariant constraint localization and refined/perfect
action live. Blocks 42--53 then repaired the flat linear sector by changing
the quotient and update rather than declaring gravity failure. The same
mechanism applies again: change the formulation to a dynamical nonlinear
connection/source law or add refinement data. Earlier source-additive-zero and
flat-projection walls were likewise retired by endogenizing the joint law.
The present route decision incorporates those escapes instead of repeating a
fixed-carrier no-go.

**N1--N8 status: `PASS` for the narrow finite-inventory affine-surrogate claim.**
The universal gravity no-go fails N1 and N7 and is not shipped.

## Reproduction

From the repository root:

~~~bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
python3 scripts/admissibility_curved_regge_pseudoconstraint_perfect_action_route_gate_2026_08_12.py
~~~

Expected final line:

~~~text
TOTAL: PASS=7 FAIL=0
~~~

## Conclusion

We were at risk of mistaking repeated linear and fixed-action repairs for TOE
progress. The corrected result is more useful: the linear causal sector works,
but the first affine continuation was not a physical curved metric: it froze
all ten metric tangents and varied only five nonmetric modes. Its full-rank
Hessian therefore cannot carry the interpretation previously assigned to it.
The missing object is not an affine Hessian term or another integrator
parameter. It is a replacement source-complete nonlinear Noether identity,
realized either by a dynamical source/connection action, an improved/perfect
action, or a variable-triangulation canonical move law.

That is now the gravity priority. Until one of those constructions exists and
is bound to the Record clock/source/state fields, gravity/source/resources
stays at the same TOE percentages.
