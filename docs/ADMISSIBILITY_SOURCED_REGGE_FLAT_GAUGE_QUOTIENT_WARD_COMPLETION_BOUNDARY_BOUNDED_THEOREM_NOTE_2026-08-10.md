---
claim_id: admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the four-dimensional Kuhn/Coxeter Regge action sum_h A_h(epsilon_h+epsilon_h^2/1024), the flat-connected quotient along k=x(1,0.7,-0.4,0.2) has a six-dimensional massless sector whose O(x^2) Schur-limit inertia is 5-negative/1-positive. Differentiating the three retained homogeneous stationary source branches at zero coupling instead gives nonzero O(coupling) physical mass matrices with inertias 3-/3+, 4-/2+, and 2-/4+. Their positive generalized-pencil roots predict two, one, and three crossovers with x/sqrt(coupling) ratios that agree with direct coupling-1e-5 roots within 1.2e-4. On the interval-backed Bundle-B continuation at coupling 1/100, the quotient escapes both Block-21 high-momentum fixed-normal witnesses but has four numerical crossings at x=0.051280258968..., 0.069887007257..., 0.088715895888..., and 0.204407087875.... Its Frobenius-nearest Hermitian inherited-gauge completion (I-P)Q(I-P) has the same quotient spectrum. A deterministic 11,279-point inventory finds five inertia chambers, while all 8,749 nonzero L=3 through L=8 torus modes miss the narrow infrared defect. This is a bounded diagnosis of the inherited flat gauge map and supplied external-source homogeneous branches, not a continuous-zone theorem, local covariant source-connection construction, full nonuniform coupled solution, Lorentzian stability result, action selection, physical-history selection, covariant-gravity no-go, or axiom adoption."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - kinetic_isotropy_primitive
  - realized_state_primitive
  - admissibility_regge_curvature_squared_sourced_continuation_constraint_localization_boundary_bounded_theorem_note_2026-08-10
  - admissibility_flat_regge_curvature_squared_branch_lift_boundary_bounded_theorem_note_2026-08-10
  - cubic_coxeter_regge_3plus1_tick_extension_second_variation_narrow_theorem_note_2026-06-09
runner: scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py
---

# Sourced Regge Flat-Gauge Quotient And Ward-Completion Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** execute the most immediate momentum-covariant escape left by Block
21, then identify exactly which sourced gauge/connection data remain missing.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py](../scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py)

**Retained dependency surface:**
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[scale reference](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
[kinetic isotropy](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md),
[realized state](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md),
[Block 21 sourced continuation](ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[Block 20 flat branch lift](ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), and the
[retained Regge carrier](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md).

## 1. Result Up Front

Block 21 isolated a failure of the constant five-normal localization. It did
not exclude a momentum-dependent gauge quotient. This block executes the
simplest such alternative: remove the image of the exact **flat**
vertex-displacement map `G_0(k)` at every nonzero momentum.

That move succeeds at the two high-momentum witnesses which closed scalar
coefficient retuning for the fixed normal matrix. The resulting eleven-
dimensional quotient has inertia `9-/2+` at both, with nonzero gaps
`0.123891195790...` and `0.145884042301...`.

The failure mechanism is already visible at infinitesimal source coupling.
At zero coupling the quotient contains five massive directions and six
massless physical directions. The six-mode Schur limit has the intended
`O(k^2)` inertia `5-/1+`. Differentiating the stationary branch at zero
coupling gives the following source-induced `O(c)` mass matrices:

| retained source | mass-matrix inertia | smallest absolute eigenvalue | positive `x/sqrt(c)` roots |
|---|---:|---:|---:|
| two-stream | `3-/3+` | `0.02774481...` | `0.185251...`, `0.363637...` |
| Bundle A | `4-/2+` | `0.14017315...` | `0.827791...` |
| Bundle B | `2-/4+` | `0.04034727...` | `0.304643...`, `0.538340...`, `0.594215...` |

Direct coupling-`1e-5` roots reproduce every ratio within `1.2e-4`, and the
three deep-infrared quotient inertias are respectively `7-/4+`, `8-/3+`, and
`6-/5+`. Thus the supplied external-source continuation inserts an `O(k^0)`
term which dominates the required `O(k^2)` graviton sector at sufficiently
small momentum. This is not a fitted scaling law; both matrices are derived
independently and the roots are then recomputed on the nonlinear branches.

At the retained finite Bundle-B coupling `1/100`, the quotient has four
crossings on the named generic path

    k(x) = x (1, 0.7, -0.4, 0.2),                                  (1)

with the following simple numerical determinant brackets:

| crossing | `x` | inertia before | inertia after |
|---|---:|---:|---:|
| `r_1` | `0.0512802589684685...` | `7-/4+` | `8-/3+` |
| `r_2` | `0.0698870072573606...` | `8-/3+` | `9-/2+` |
| `r_3` | `0.0887158958882546...` | `9-/2+` | `10-/1+` |
| `r_4` | `0.204407087874502...` | `10-/1+` | `9-/2+` |

The lesson is sharper than “try a different projector.” Importing the flat
gauge directions can evade the fixed-normal high-momentum obstruction, but
the sourced geometry Hessian does not annihilate those directions and its
physical six-mode restriction acquires the wrong leading order. A genuine
sourced gauge law must supply the background-dependent generator, source
transformation, and differentiated connection terms.

## 2. Carrier And Sourced Background

The action is exactly the Block-21 action

    S(ell) = sum_h A_h(ell) [epsilon_h(ell)
                             + epsilon_h(ell)^2 / 1024].             (2)

The supplied source is retained Bundle B at coupling `1/100`. The five-normal
stationary continuation is reconstructed before any quotient is formed:

    x_B = (-0.0002118903455527,
            0.0012366779546983,
            0.0012366779546975,
            0.0012366779546977,
            0.0093762842804963).                                    (3)

Block 21 interval-certifies a unique root in a radius-`2e-9` box around this
center. This block re-solves the normal equation at 40 digits and rebuilds the
complete 50-hinge off-flat Bloch Hessian `Q_B(k)`. It inherits, rather than
relabels, the interval statement.

The background remains a homogeneous affine-reaction representative. It is
not a solution of a full nonuniform coupled source/geometry field law.

## 3. Inherited Flat-Gauge Quotient

For nonzero `k`, let `G_0(k)` be the `15 x 4` vertex-displacement map of the
flat Regge carrier. It has rank four on every declared point. Define

    P_0(k) = G_0(k) [G_0(k)^dagger G_0(k)]^(-1) G_0(k)^dagger,       (4)

and choose any orthonormal `15 x 11` matrix `B_0(k)` spanning
`ker G_0(k)^dagger`. The inherited flat-gauge quotient is

    Q_perp(k) = B_0(k)^dagger Q_B(k) B_0(k).                         (5)

Changing the orthonormal complement conjugates (5) unitarily, so its inertia
and determinant are basis-independent.

The two Block-21 witness results are:

| momentum | fixed-`N` role in Block 21 | inherited-gauge quotient |
|---|---|---|
| `(2pi/3,-pi/2,2pi/3,-pi/2)` | forces `alpha>21/4096` | `9-/2+`, gap `0.123891195790...` |
| `(0,3pi/4,3pi/4,3pi/4)` | forces `alpha<20/4096` | `9-/2+`, gap `0.145884042301...` |

Thus the fixed-normal two-witness negative does **not** transfer to this
momentum-covariant quotient. That is a real escape, not a rhetorical caveat.

## 4. Algebraic Ward Completion

One may enforce the inherited kernel algebraically without choosing a
quotient basis:

    Q_W(k) = (I-P_0(k)) Q_B(k) (I-P_0(k)).                           (6)

In abstract projector notation this is `(I-P) Q (I-P)`.

### Proposition 1 — kernel and spectrum

`Q_W` is Hermitian, `Q_W G_0=0`, and its eleven nonzero eigenvalues are
exactly the eigenvalues of (5).

**Proof.** Decompose edge space orthogonally as
`im P_0 direct-sum ker P_0`. In this block basis, `(I-P_0)Q_B(I-P_0)` has a
zero `4 x 4` gauge block, zero off-diagonal blocks, and lower block (5).
Hermiticity and the spectral statement follow. `square`

### Proposition 2 — Frobenius-nearest Hermitian completion

Among Hermitian matrices `H` satisfying `H P_0=P_0 H=0`, equation (6) is the
unique minimizer of `||H-Q_B||_F`.

**Proof.** The allowed matrices form the linear subspace whose only nonzero
block in the same orthogonal decomposition is the lower `11 x 11` block.
Orthogonal projection in the Frobenius inner product deletes the other three
blocks of `Q_B` and retains the lower block. That projection is (6) and is
unique. `square`

This theorem is mathematical, not a locality or physical-selection theorem.
Because (4) contains the inverse momentum-dependent Gram matrix, (6) is not
asserted to arise from a finite-range local source/constraint action.

## 5. Why Ward Projection Alone Is Insufficient

The raw sourced geometry Hessian has substantial inherited-Ward defects:

| witness | `||Q_B G_0||_2` |
|---|---:|
| lower | `0.441292407701...` |
| upper | `0.508760488208...` |

Across the declared path the maximum is `0.547993138870...`. Equation (6)
sets that defect to zero, but Proposition 1 says it cannot change the quotient
spectrum. It therefore retains the four roots in Section 1.

This is the precise distinction between a kernel repair and a sourced
connection law. For an invariant full action with variables `z` and gauge
generator `R(z)`, differentiating

    grad S(z) R(z) = 0                                               (7)

gives

    Hess S(z) R(z) + grad S(z) · dR(z) = 0.                          (8)

At a stationary full coupled solution the combined geometry, source, and
constraint terms satisfy the appropriate version of (8). Here the geometry
gradient is balanced only on a supplied affine normal equation, while
`G_0` is frozen at the flat carrier. The missing `grad S · dR`, source-
transformation, mixed-Hessian, and multiplier-connection terms are exactly
the pieces that cannot be manufactured by the orthogonal projection (6).

## 6. Weak-Source Infrared Mechanism

Let `d=(1,0.7,-0.4,0.2)`. The inherited flat generator has the expansion

    G_0(x d) = i x G_1(d) + O(x^2),                                (9)

and `G_1(d)` has rank four. Choose a fixed complement `C` of its image. At
`x=0`, `C^dagger Q_0(0) C` has five nonzero directions and six zero
directions. Schur-complementing the five nonzero directions and taking the
even path limit gives the six-mode kinetic matrix

    K = lim_(x->0) [S_0(x)+S_0(-x)]/(2 x^2).                       (10)

Its eigenvalues are numerically

    (-2.52728450, -1.86940264, -1.10144308,
     -0.96480264, -0.70222258, 1.58057201),                         (11)

so the intended weak-field physical inertia is `5-/1+`. Step halving and
Richardson extrapolation change (10) by `6.459e-7` relative in spectral norm;
the flat Ward residual `||Q_0(0)G_1||_2` is below `8e-14`.

For retained source `s`, let `z_s(c)` be its five-normal stationary branch:

    grad_z S(z_s(c)) = c t_s.                                      (12)

The nondegenerate flat normal Hessian gives the derived tangent

    z_s'(0) = H_N(0)^(-1) t_s.                                    (13)

No source prefactor is fitted. The runner perturbs the actual edge lengths
along (13), rebuilds the complete 50-hinge off-flat Hessian at two centered
step sizes, and Richardson-extrapolates `dQ_s/dc`. Restriction to the six
physical zero modes gives `M_s`. Its spectra are:

| source | eigenvalues of `M_s` |
|---|---|
| two-stream | `(-0.144921,-0.069607,-0.027745,0.056954,0.109294,0.154893)` |
| Bundle A | `(-1.084760,-0.408923,-0.358176,-0.140173,0.352280,0.523174)` |
| Bundle B | `(-0.380684,-0.272518,0.040347,0.152369,0.342471,0.676983)` |

The largest relative step-halving discrepancy is below `3e-8`. The three
Ward-defect slopes `||(dQ_s/dc)G_1||_2` are respectively
`11.721712...`, `5.567366...`, and `36.669691...`, whereas the flat value is
zero to reconstruction precision.

For `x` and `c` jointly small, the physical low block therefore has the
controlled numerical expansion

    S_s(x,c) = c M_s + x^2 K + O(c^2 + c |x| + |x|^3).             (14)

Putting `x=rho sqrt(c)` reduces the leading root problem to

    det(M_s + rho^2 K) = 0.                                       (15)

The positive real roots of (15) are the ratios listed in Section 1. Direct
nonlinear branches at `c=1e-5` give:

| source | pencil prediction | direct `x/sqrt(c)` | deep-IR inertia |
|---|---|---|---:|
| two-stream | `(0.185251,0.363637)` | `(0.185205,0.363620)` | `7-/4+` |
| Bundle A | `(0.827791)` | `(0.827790)` | `8-/3+` |
| Bundle B | `(0.304643,0.538340,0.594215)` | `(0.304657,0.538430,0.594330)` | `6-/5+` |

The direct difference quotients reproduce the tangent mass matrices within
`3.91e-4` relative and their Ward slopes within `9.12e-5`. Hence this is not
merely a finite-`1/100` anomaly: for each of the three retained external
sources, the supplied homogeneous continuation changes the leading infrared
operator before the flat `O(k^2)` term can dominate. It does not show that a
joint dynamical source/geometry action, its background-dependent generator,
or a law-selected massive phase has the same defect.

## 7. Bounded Stress And Finite-Torus Inventories

The deterministic inventory contains:

- six 512-point symmetry lines from `x=0.005` through `pi`;
- all fifteen nonzero `{0,pi}^4` corners; and
- 8,192 seed-fixed uniform Brillouin samples.

Its 11,279 quotient matrices split as follows:

| inertia | count |
|---|---:|
| `6-/5+` | 6 |
| `7-/4+` | 35 |
| `8-/3+` | 19 |
| `9-/2+` | 11,150 |
| `10-/1+` | 69 |

The minimum sampled absolute eigenvalue is `6.974883...e-6`. This inventory
is a reproducible bounded diagnostic, not a continuous-zone theorem and not
an interval certificate for every matrix or root.

Independently, every nonzero momentum on the periodic `L=3,...,8` four-tori
has the target `9-/2+` quotient inertia:

    8,749 modes, zero failures, minimum gap 0.08831735... .         (16)

The smallest torus momenta lie beyond the narrow infrared chambers. Thus a
coarse finite-torus inventory can pass while the continuous path already
fails. This is an explicit aliasing diagnosis, not a criticism of the earlier
flat finite-torus theorem, whose background and operator are different.

## 8. Candidate Geometry-Law Refinement (Unadopted)

The Block-21 candidate becomes more explicit:

> A realized geometry/history law selects a local lattice-covariant geometry
> action and coefficients, a sourced background or boundary sector, and the
> joint local transformation law of geometry, constraints, and sources. On a
> selected full coupled solution, the differentiated source Ward identity
> fixes the background-dependent gauge generator and all gradient,
> connection, multiplier, and mixed-Hessian terms. The resulting local
> covariant quotient has no unselected source-induced `O(k^0)` term in a
> law-selected massless gravity phase, has no unintended zero modes or inertia
> crossings on realized momentum support, preserves the infrared gravitational
> pole, and admits stable Lorentzian nonlinear evolution with the same source
> law. A selected massive or curved phase must instead derive its scale,
> boundary sector, and stability from that same law.

This wording is sufficient or target-equivalent only. It is unadopted, not
proved minimal or necessary, and does not edit the canonical axiom memo. A
stronger admissibility or realized-history theorem may derive it downstream.

## 9. No-Go Discipline Gate

The only negative statement eligible to ship is:

> On the three named homogeneous external-source continuations, the inherited
> flat vertex-displacement quotient acquires the reported source-dependent
> `O(c)` six-mode mass matrices and direct weak-source crossover roots. On the
> fixed finite-coupling Bundle-B representative, that quotient and its
> Frobenius-nearest Hermitian Ward completion do not have uniform inertia along
> the named generic path or the declared deterministic inventory.

This is not a covariant-gravity no-go.

### N1 — Alternative route enumeration

| normalized family | mechanism and attempted calculation | outcome | marker |
|---|---|---|---|
| constant five-normal localization | project with the fixed Block-19 `N` and retune `alpha` | [Block 21](ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) gives a two-witness no-overlap | `ATTEMPTED` |
| inherited flat-gauge complement | use `ker G_0(k)^dagger` at every nonzero momentum | escapes both high-momentum witnesses but has four path crossings | `ATTEMPTED` |
| Hermitian Ward completion | use the unique Frobenius projection `(I-P_0)Q_B(I-P_0)` | restores the inherited kernel exactly; quotient crossings are unchanged | `ATTEMPTED` |
| weak-source tangent pencil | differentiate all three stationary branches at `c=0` and solve `det(M_s+rho^2 K)=0` | every source has a non-target mass signature and positive real roots | `ATTEMPTED` |
| direct nonlinear weak-source branches | independently solve all three branches at `c=1e-5` and bracket their roots | every pencil root is reproduced with the predicted square-root scaling | `ATTEMPTED` |
| finite-volume disguise | exhaust all 8,749 nonzero `L=3,...,8` momenta and compare with a fine infrared path | all torus modes pass, but the path roots lie below their resolution | `ATTEMPTED` |
| alternate momentum inventory | six symmetry lines, all nonzero `{0,pi}^4` corners, and 8,192 seed-fixed points | five quotient inertia chambers occur | `ATTEMPTED` |

The counted families differ in primary object and invariant: fixed normals,
flat gauge orbits, orthogonal matrix completion, a tangent generalized pencil,
direct nonlinear roots, exhaustive periodic sampling, and a broader momentum
inventory. The background-dependent local gauge/source connection is not
counted as a failed route; it remains the actionable steelman in N7.

### N2 — Wall-independence audit

The raw list separated action, coefficient, external source, homogeneous
representative, inherited generator, and orthogonal quotient. Those choices
are collapsed into one selected-model wall because a joint sourced geometry
law would choose them together. The collapsed walls are:

- `W1`: the supplied Euclidean model package: action/coefficient, homogeneous
  external-source branches, inherited flat generator, and orthogonal quotient;
- `W2`: bounded momentum coverage: one infrared path, two witnesses, 11,279
  stress points, and the finite `L=3,...,8` inventory;
- `W3`: double-precision tangent, root, and spectrum certification rather than
  interval matrix bounds; and
- `W4`: Euclidean Hessian inertia rather than Lorentzian nonlinear evolution.

| Pair | close first => second? | close second => first? | independent? |
|---|---|---|---|
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W3,W4` | no | no | yes |

No pair in the collapsed set follows from another. In particular, changing
the model package does not prove continuous momentum coverage or Lorentzian
stability, and interval certification would not select a physical source law.

### N3 — Hidden-wall scan

| phrase/hit | classification | disposition |
|---|---|---|
| “gauge quotient” | hidden condition if read as the realized gauge law | promoted to `W1`; always called the inherited flat-gauge quotient |
| “Ward completion” | hidden condition if read as local physics | promoted to `W1`; only Frobenius-nearest Hermitian algebra is proved |
| “sourced background” | hidden condition if read as a full solution | promoted to `W1`; it is the homogeneous normal-equation representative |
| “four crossings” | hidden certification assumption | promoted to `W2,W3`; numerical brackets on one path only |
| “for nonzero coupling” | hidden universalizer if read beyond the perturbative branches | narrowed to the three retained branches and the controlled small-`c` expansion |
| “all momenta” | unsupported universalizer | forbidden; only the declared inventory is reported |
| “physical instability” | rhetoric inflation | promoted to `W4` and forbidden; Euclidean inertia is not Lorentzian dynamics |
| “canonical axiom memo” | governance-only context | non-load-bearing; it records that no axiom edit occurs and supplies no physics step |

### N4 — Residual matching

| prior negative or residual | same residual here? | disposition |
|---|---|---|
| `ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:119` — fixed-`N` two-witness no-overlap | no | this quotient is `9-/2+` at both witnesses, so that residual is retired here |
| `ADMISSIBILITY_REGGE_CURVATURE_SQUARED_SOURCED_CONTINUATION_CONSTRAINT_LOCALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:82` — raw 15-dimensional crossing `0.0240...` | no | projection changes the space and the first quotient crossing is `0.05128...` |
| `ADMISSIBILITY_FLAT_REGGE_CURVATURE_SQUARED_BRANCH_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md:170` — coefficient nonselection | no | `alpha` is fixed; the new variable is constraint/source geometry |
| this block's `O(c)` mass matrices | yes | this is the exact inherited-flat-quotient weak-source residual proved here |
| finite-torus success | no | it is an aliasing control, not evidence against the continuous infrared roots |
| missing continuous-zone proof | yes | explicitly remains open |
| missing background-dependent source connection | yes | promoted to the exact terminal obligation in Section 11 |
| missing Lorentzian nonlinear evolution | yes | explicitly remains open |

The new content is therefore not an echo of the fixed-normal obstruction. It
constructs and tests a live escape, retires the old witnesses for that escape,
and finds a different infrared boundary.

### N5 — Resolution-class execution

| resolution | executed evidence |
|---|---|
| per element | all fifteen edge classes enter `Q_B`, `P_0`, and `Q_W` |
| per site | all fifty hinge classes are rebuilt in the sourced action Hessian |
| per mode | weak-source roots, two high-momentum witnesses, four finite-source roots, 11,279 stress points, and 8,749 torus modes |
| per block | all three weak-source branches plus Bundle-B source reconstruction, quotient, Ward algebra, path, and stress inventory |
| lattice wide | checked and not executed: finite tori and sampled paths are not a continuous zone, local connection, nonuniform field, or Lorentzian theorem |

The cached stdout carries all five lines with these scope boundaries.

### N6 — Primitive boundaries

| primitive/current premise | use | non-use |
|---|---|---|
| `minimal_axioms` | establishes that admissibility is not a dynamics axiom and source/action identification remains open | does not select (2), `G_0`, Bundle B, or (6) |
| `scale_reference_primitive` | keeps every reported number dimensionless in lattice units | supplies no action coefficient or source law |
| `kinetic_isotropy_primitive` | licenses the retained flat weak-field carrier only within its approved role | does not turn Euclidean quotient inertia into Lorentzian stability |
| `realized_state_primitive` | separates supplied possibilities from a selected realized history | does not select this background, projector, or source |

No primitive is edited or silently enlarged.

The partial-closure scan found four relevant paths:

| path | present status | what it closes or leaves open |
|---|---|---|
| Block 20 local curvature-square term | retained bounded theorem | repairs the flat fifth branch but does not select a sourced law |
| Block 21 interval source continuations | retained bounded theorem | closes local normal-root existence for three sources but not their covariant quotient |
| this block's algebraic `(I-P_0)Q(I-P_0)` | exact matrix proposition | closes the inherited kernel convention only; it cannot change the quotient spectrum or establish locality |
| joint background-dependent source/geometry action | unconstructed live route | would supply the missing mixed, connection, and constraint Hessian terms if derived and solved |

No naming, labeling, or convention-only reframe generates the missing terms in
equation (8). Conversely, this note asserts neither axiom necessity nor
primitive exhaustion. The candidate in Section 8 may be a downstream theorem
or law interface; adoption and minimality remain owner-governance questions.

### N7 — Actionable steelman

The strongest alternative is accepted: a background-dependent gauge/source
connection. Construct local coupled variables
`z=(ell,J,lambda,...)` and a background-dependent generator `R_*(z)` from the
realized history/source law. Solve the full nonuniform coupled equations, not
only the homogeneous normal equation. Then differentiate the exact joint Ward
identity to obtain every `grad S · dR`, mixed source, and multiplier-curvature
term in (8). Only after forming that local covariant Hessian should one take
its gauge/constraint quotient and prove continuous-zone and Lorentzian
stability.

The terminal obligation is concrete: provide repository-local formulas for
`R_*(ell,J)`, the source transformation, the nonlinear constraint functions,
and the full coupled stationary background; verify the differentiated Ward
identity mode by mode; then certify the quotient over continuous momentum
support. If that selected construction still fails, enlarge the local action
basis with law-derived coefficients.

### N8 — Cross-cycle echo

| earlier block | wall removed later | instruction retained here |
|---|---|---|
| Block 19: mixed inertia on a fixed affine normal surface | Block 20 changed the action and repaired the flat full symbol | do not promote a supplied-surface result to gravity |
| Block 20: full flat quotient viable but sourced law open | Block 21 found interval-backed sourced normal roots | preserve nonlinear source completion |
| Block 21: constant `N` has a two-witness no-overlap | this block's momentum-dependent quotient escapes both witnesses | test live alternatives before shipping a negative |
| this block: inherited `G_0` has sourced infrared crossings | the `O(c)` mass matrices and `sqrt(c)` roots localize the mechanism, while the background/source connection remains unconstructed | derive `R_*` and (8), rather than echo “all quotients fail” |
| finite-torus inventories can miss an infrared chamber | the continuous path exposes roots below the `L<=8` momentum resolution | pair every finite inventory with an analytic infrared-order test |

**N1--N8 status: `PASS` only** for the inherited-flat-gauge calculation on the
three named homogeneous weak-source branches and the finite-coupling Bundle-B
named-path-and-inventory diagnosis.

## 10. Promotion Value And Cluster Gate

| gate | evidence |
|---|---|
| V1 — specific obstruction | Block 21 explicitly leaves a momentum-covariant quotient live; this block executes it |
| V2 — new derivation | Propositions 1--2, the six-mode kinetic limit, three source mass matrices, square-root crossover law, and four finite-source roots are not in the parent |
| V3 — generic machinery | orthogonal projection and perturbation pencils are generic, but the sourced 50-hinge carrier, mass signatures, roots, and chamber counts are specific |
| V4 — marginal content | both fixed-`N` witnesses are retired for this route, and the missing Ward connection is sharpened to an explicit unwanted `O(k^0)` term |
| V5 — independently reviewable | three branch tangents, direct weak-source controls, source reconstruction, algebraic completion, roots, finite tori, and deterministic inventory are one executable object |

This is distinct enough from Block 21 to review separately: Block 21 closes a
constant-normal coefficient route; this block tests a momentum-dependent
gauge route and derives the infrared-order mechanism behind its boundary.

## 11. Exact Next Obligation

1. Derive the local joint geometry/source transformation `R_*(ell,J)` from
   the realized history law.
2. Solve one full nonuniform coupled sourced background.
3. Reconstruct the complete Hessian including source, mixed, multiplier, and
   `grad S · dR` connection terms required by (8).
4. Verify the source Ward identity and prove that the selected massless phase
   starts at `O(k^2)` rather than inheriting the `O(k^0)` matrices found here.
5. Certify the continuous Brillouin quotient and then Lorentzian nonlinear
   evolution; if the law instead selects a massive/curved phase, derive its
   scale and stability rather than importing them.

Until those objects exist, the gravity/source lane has stronger diagnostic
support but no physical-law selection. The fixed TOE percentages do not move.

## 12. Reproduction

Run:

```bash
python3 scripts/admissibility_sourced_regge_flat_gauge_quotient_ward_completion_boundary_2026_08_10.py
```

The runner reconstructs (3), the flat six-mode kinetic limit, all three source
tangent mass matrices, their direct coupling-`1e-5` roots, the complete
finite-source kernel, both witnesses, the Ward completion, all four
coupling-`1/100` determinant roots, the 11,279-point inventory, and all 8,749
nonzero `L=3,...,8` torus modes. No external scientific inputs are used.
