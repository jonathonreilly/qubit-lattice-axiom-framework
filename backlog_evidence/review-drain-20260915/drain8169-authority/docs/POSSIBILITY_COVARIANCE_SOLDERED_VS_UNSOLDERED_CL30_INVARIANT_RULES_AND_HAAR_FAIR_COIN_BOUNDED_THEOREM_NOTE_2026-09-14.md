---
claim_id: possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "Conditional polynomial invariant/covariant census on the centre and six recorded-slot Bloch vectors for supplied independent SO(3), independent O(3), and diagonal proper-cubic actions. Degree0–3 stratum tables, selected scalar counts through6 and sphere quotient through10; explicit frame and normalized-menu comparisons; translation-invariant scalar functions on a parity cell. No all-axiom model, selected covariance action, physical probability law, role-range necessity, or formation theorem."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - admissibility_six_neighbor_affine_cq_channel_solder_support_boundary_bounded_theorem_note_2026-08-14
  - admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13
  - admissibility_axis_separable_barycenter_selector_bounded_theorem_note_2026-08-14
  - admissibility_sharp_qubit_record_writer_orientation_axiom_decision_bounded_theorem_note_2026-09-01
  - born_price_wordings_homogeneity_collinear_menus_four_outcome_fair_coin_2026_09_05
  - admissibility_handed_rule_pseudoscalar_invariant_census_and_parity_odd_record_correlators_bounded_theorem_note_2026-09-13
  - covariant_nn_support_rules_gauss_law_as_glued_support_and_hole_statistics_bounded_theorem_note_2026-09-14
runner: scripts/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.py
---

# Conditional possibility covariance and recorded frames

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** conditional mathematical source; independent audit owns retention.

## Result and scope

For three **supplied** group actions, the runner counts scalar invariants,
internal-vector covariants and lattice-by-internal frame covariants on one
centre plus six neighbour slots. Unsoldered independent internal rotations
exclude occupancy-only internal-vector outputs and degree-one **scalar**
invariants. They do not exclude linear vector covariants: `F(p,q)=p` is an
immediate counterexample to that broader statement. Soldering permits additional
scalar terms and an occupancy response on six of the ten slot strata.

These are consequences of selected mathematical representations, not a proof
that the current axioms select either action or that the displayed menu
functions satisfy all axioms and primitives. Bloch-state coordinates, access
to neighbour content, probability evaluation and group actions are supplied.
The calculation does not construct a global admissibility/Record formation law.

## Current authorities and conditional comparisons

The following links make the original declared inputs explicit. Source identity
is not scientific acceptance; only the stated bounded roles are used.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): current foundation and its
  boundary; no Hamiltonian, probability functional or internal covariance
  representation is inferred from it here.
- [Realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md):
  pointwise history reference only; no state or averaging measure is selected.
- [Six-neighbour solder boundary](ADMISSIBILITY_SIX_NEIGHBOR_AFFINE_CQ_CHANNEL_SOLDER_SUPPORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md):
  conditional affine occupancy intertwiner and distinct content-access boundary.
- [Q8 conditional-law comparison](ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md):
  precedent for comparing supplied covariance models, not imported all-axiom closure.
- [Axis-separable selector](ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-14.md):
  supplied formula `D(d)=[I+d.sigma/3]/2`; its original26-vector domain and
  calibration are not promoted to a universal menu law. The normalized means
  used below define a separately supplied extension, whose positivity is proved.
- [Sharp writer orientation boundary](ADMISSIBILITY_SHARP_QUBIT_RECORD_WRITER_ORIENTATION_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md):
  orientation/readout comparison, not a selected implementation.
- [Born-price wording comparison](THE_BORN_PRICE_WORDINGS_HOMOGENEITY_IS_PAYABLE_ON_THE_CONTINUUM_LAW_AS_IT_STANDS_THE_COLLINEAR_MENUS_NEED_A_SCALE_READING_RULE_THE_FOUR_OUTCOME_MENU_PAYS_WITH_NO_CLAUSE_AND_NONE_REMOVES_THE_FAIR_COIN_BOUNDED_NOTE_2026-09-05.md):
  fair-coin context; only the explicit antipodal probability evaluation below is used.
- [Handed-rule census](ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md):
  parity comparison: its normalized centre-dependent finite-menu rule
  `T(q)(v dot s)` has total degree5, while its own raw `T(q)` has degree3.
  This note counts the raw scalar, not that normalized rule; the parent also
  uses finite internal cubic actions where this note uses continuous SO(3).
- [Support-rule comparison](COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-14.md):
  supplied role configuration. Its current source distinguishes a nearest-neighbour
  parity skeleton from separate longer-range corner pins; this note proves no
  contrary range necessity and does not reproduce its four-role code.

## Supplied representations and counting method

Let `p` be the centre vector and `q_i` the recorded neighbours' vectors, each in
the closed unit Bloch ball for menu interpretations. Polynomial counting treats
their components as free real coordinates, with rational coefficients in the
implementation. Slots are `(+x,-x,+y,-y,+z,-z)`. Missing slots contribute no
coordinate. Proper signed permutation matrices of determinant1 give the24
cubic rotations. Their action on64 slot subsets has ten orbits shown below.

`U` is the direct product of the slot-permuting cubic group and independent
internal `SO(3)`. The latter is the group induced on Hermitian Bloch coordinates
by complex-linear star automorphisms of `M_2(C)`; arbitrary algebra automorphisms
are not being identified with `SO(3)`. `U3` additionally supplies inversion of
all internal vectors, giving `O(3)`. `S` supplies the diagonal cubic action on
slots and vector coordinates. Neither additional internal naturality, inversion,
nor a preferred spatial/internal identification is adopted as axiom content.

For a stratum stabilizer `H`, the degree-d dimension is the group average of
`chi_Sym^d(V) chi_output`. Symmetric-power characters obey
`d h_d=sum_(k=1)^d tr(g^k) h_(d-k)`. For `U`, the internal spin1 character is
`z+1+z^-1`; its Haar average on a symmetric Laurent class function is the
coefficient of `z^0` minus that of `z^1`. Averaging output characters counts
intertwiners. `U3` keeps precisely degrees with even `d+number_of_internal_output_factors`.
These are standard character, Haar and Reynolds-projection methods supplied
as mathematical machinery, not physics derived from the axioms.

The independent in-runner route intersects the three Lie-derivation kernels
and averages over `H` for `U`; for `S` it averages signed monomial orbits.
Its120 comparisons are exactly10 strata x2 readings (`U,S`) x2 output types
(scalar, internal vector) x3 degrees(1,2,3). They do not independently recompute
frame columns, degree0 or `U3`; those have character counts and separate
parity/fixed-space checks. A Frobenius orbit/fixed-space count independently
checks the soldered degree-one scalar row.

## 1. Finite census and occupancy responses

Put `d_occ=sum_(i recorded) r_i`. It is nonzero on six strata and zero on the
four antipodally closed strata. It is an occupancy sum, not the normalized
menu mean used in section4.

All entries below list degrees0,1,2,3 and include the centre vector.

| stratum | `d_occ != 0` | scalar, `U` | scalar, `U3` | scalar, `S` | internal vector, `U` | internal vector, `S` | frame map, `U` | frame map, `S` |
|---|---|---|---|---|---|---|---|---|
| `()` | no | 1,0,1,0 | 1,0,1,0 | 1,0,1,0 | 0,1,0,1 | 0,1,0,2 | 0,0,0,0 | 1,1,3,3 |
| `(0,)` | yes | 1,0,3,0 | 1,0,3,0 | 1,2,7,12 | 0,2,1,6 | 1,6,15,44 | 0,2,1,6 | 3,14,49,124 |
| `(0,1)` | no | 1,0,4,0 | 1,0,4,0 | 1,1,10,16 | 0,2,1,10 | 0,5,14,67 | 0,1,2,8 | 2,10,55,181 |
| `(0,2)` | yes | 1,0,4,0 | 1,0,4,0 | 1,4,25,80 | 0,2,1,10 | 1,14,65,250 | 0,4,5,26 | 5,40,205,740 |
| `(0,2,4)` | yes | 1,0,4,2 | 1,0,4,0 | 1,4,26,124 | 0,2,2,14 | 1,12,78,364 | 0,4,6,40 | 3,36,234,1092 |
| `(0,1,2)` | yes | 1,0,7,1 | 1,0,7,0 | 1,5,43,175 | 0,3,3,24 | 1,19,113,553 | 0,5,9,56 | 5,53,355,1631 |
| `(0,1,2,3)` | no | 1,0,5,0 | 1,0,5,0 | 1,1,21,75 | 0,2,1,16 | 0,7,39,265 | 0,1,4,22 | 2,16,141,755 |
| `(0,1,2,4)` | yes | 1,0,9,4 | 1,0,9,0 | 1,7,64,336 | 0,3,4,39 | 1,23,176,1024 | 0,7,16,111 | 5,67,544,3056 |
| `(0,1,2,3,4)` | yes | 1,0,8,4 | 1,0,8,0 | 1,5,46,280 | 0,3,4,37 | 1,15,126,860 | 0,5,12,95 | 3,41,388,2560 |
| full | no | 1,0,5,1 | 1,0,5,0 | 1,1,15,69 | 0,2,1,17 | 0,4,25,229 | 0,1,4,25 | 1,8,92,657 |

The final two columns count `out=veclat`, with output transformation
`M -> g M R^T`; they are frame maps, not ordinary lattice vectors. The separate
`out=lat` character computation equals the internal-vector result under `S`,
because both representations are then the same cubic vector. It differs under
`U`. In particular the empty soldered frame has dimension1 at degree0 although
the internal-vector output has dimension0.

For occupancy-only internal-vector outputs, independence of internal rotations
forces `v=Rv` for every `R`, hence `v=0`; this argument holds for any occupancy
window, not just nearest neighbours. Under `S`, the fixed vectors of each
stratum stabilizer have dimension1 exactly when `d_occ` is nonzero, and are
then spanned by it. Each stratum may have its own coefficient; the statement
is distinct from one globally affine occupancy compiler.

No unsoldered degree-one scalar invariant exists: independent rotations have
no invariant linear functional on any copy of the vector representation.
Internal-vector covariants such as `p` and `sum q_i` remain allowed.
The soldered linear scalar dimensions are
`0,2,1,4,4,5,1,7,5,1` in the displayed stratum order.

Additional full-window scalar counts through degree6 are:

| action | degrees0 through6 |
|---|---|
| U | 1,0,5,1,34,27,230 |
| U3 | 1,0,5,0,34,0,230 |
| S | 1,1,15,69,475,2171,9753 |

Strict enlargement is checked here for full-window scalar degrees1–6 only.
No universal claim for every positive degree or output type is needed.

## 2. Explicit invariants and recorded frame

The soldered scalar `S1=sum_i r_i dot q_i` has six monomials. Simultaneously
rotating slots and vectors preserves it; independent slot/internal actions do
not. The handed scalar
`T=sum_(i<j<k) det(r_i,r_j,r_k) det(q_i,q_j,q_k)` has48 monomials. Proper
internal rotations and slot rotations preserve it, while internal inversion
reverses its sign. It spans the full-window degree-three `U` scalar space.
A second independent scalar at that degree would contradict the census.

Five quadratics span the full-window `U` scalar space: `p dot p`, sum of
neighbour norms, `p dot sum q_i`, sum over antipodal pair inner products,
and sum over distinct non-antipodal pair inner products. Direct derivation,
slot invariance and exact rank checks establish their independence and matching
character dimension5.

Define the matrix `M=sum_i r_i q_i^T`, with lattice rows and internal columns.
It is a sum over the six slots, not a matrix whose columns are three selected
records. Reindexing gives `M' = g M R^T`. The runner exhibits an exact rational
configuration with nonzero determinant; therefore its determinant polynomial
is not identically zero, and invertibility holds on the nonzero-determinant
subset. No probability of forming such a configuration is claimed.
Where invertible, `M'^-1 (g n)=R M^-1 n`: recorded content can supply a
lattice-to-internal map covariantly. This consumes content beyond occupancy,
and is not a law-selected frame. Singular configurations remain outside this
inverse-map domain.

## 3. Empty-neighbourhood sphere laws

For the supplied pure-state sphere `|p|=1`, subtracting the degree(d-2) invariant
count from the degree-d count gives the graded sphere quotient:

| action | degrees0 through10 |
|---|---|
| U and U3 | 1,0,0,0,0,0,0,0,0,0,0 |
| S | 1,0,0,0,1,0,1,0,1,1,1 |

An invariant probability measure has the same expectation as the group average
of each polynomial. Thus all its moments through10 under `U` match uniform
sphere measure; the invariant functions reduce to constants on the sphere.
This argument uses the sphere relation and supplied invariant-measure meaning,
not just an unnormalized formal dimension count. Under `S`, quartic freedom
survives. Uniform sphere measure and equal mass1/6 on the six axes are both
cubic invariant. Their axial moments2,4,6 are respectively `(1/3,1/5,1/7)`
and `(1/3,1/3,1/3)`. Odd moments vanish for these two specific measures.
Their mixed fourth moment is1/15 versus0, and summed axial fourth moment3/5
versus1. Both return1/2 on an antipodal menu under the supplied linear
probability evaluation; no physical Born or event law is derived.

## 4. Conditional normalized-menu comparison

For nonempty recorded set `A`, define
`d_A=(sum_(i in A) r_i)/|A|`, `d_B=(sum_(i in A) q_i)/|A|`, and set both to0
when empty. With unit menu direction `m`, use supplied probabilities
`p_±=(1±d dot m/3)/2`, or matrix `D(d)=[I+d.sigma/3]/2`.
Both means have norm at most1, so both matrices have nonnegative eigenvalues
and trace1; all menus are normalized. This establishes mathematical positivity,
not a full law over possibilities, contexts, records and histories.

The actual separating configuration has a single **+z slot**, its recorded
Bloch vector **+x**, and menu along **z**. ModelA returns(2/3,1/3); ModelB
returns(1/2,1/2). A +x slot with a +x record on an x menu would instead make
them agree at2/3. Empty occupancy makes both fair.

Under `S`, both means rotate with the menu, so both probabilities are
covariant. ModelB is also covariant under independent internal rotations and
slot permutations. ModelA fails those independent actions. Exact tests cover
all64 subsets and24 cubic rotations with declared rational inputs and menu
vectors; the general covariance follows directly from the sums and inner
products. These are conditional test functions, not witnesses satisfying every
axiom and primitive. No soldering clause is adopted.

## 5. Translation toy and its limits

On the parity cell `(Z/2Z)^3`, translations act transitively. A scalar function
of one site invariant under all translations is therefore constant. The
staggered parity labelling is fixed by four translations. The runner's
`ROLE(v)=v` has **eight distinct labels**, fixed only by the identity; it is not
the four-role V/L/P/C pattern of the support-rule parent. If the codomain itself
transforms, the identity map is equivariant, so the scalar transitivity argument
does not prohibit equivariant role configurations or selected backgrounds.

Nearest-neighbour steps flip parity; the12 face-diagonal next-neighbour steps
preserve it. This is a parity fact, not a proof that roles require longer range.
Simultaneous translation orbits of ordered pairs are indexed by displacement,
so invariant scalar functions on ordered parity-cell pairs have dimension8.
This finite statement selects no physical range or role law. The current
support-rule comparison already permits a nearest-neighbour parity skeleton
and separates its additional longer-range corner pins.

## No-Go Discipline Gate

**N1 — alternatives.** Reading actual neighbour vectors or an invertible recorded
frame changes the input beyond occupancy. A smaller supplied internal group
or a different output representation changes the symmetry question. Merely
increasing the occupancy window does not evade independent-SO(3) fixed-vector
vanishing. Conditional role backgrounds and equivariant codomains survive.

**N2 — dependence.** Occupancy-vector vanishing and scalar-linear vanishing
both use the same absence of a trivial component in the internal vector
representation. The sphere result additionally uses transitivity and invariant
averaging; the parity-cell scalar result uses translation transitivity.
No independence of physical obstructions is proved.

**N3 — premises.** Group actions, Bloch coordinates, polynomial degree, centre
inclusion, scalar/vector/frame output distinctions, probability interpretation
and normalized menu formula are supplied. None is an approved new primitive.

**N4 — matching.** The affine solder parent concerns a supplied intertwiner,
not every law. The selector parent has a different finite input domain; the
normalized extension is explicit here. The role parent does not imply a
next-neighbour necessity, and this toy no longer claims one.

**N5 — resolutions.** Exact coordinate polynomials, all64 slot subsets,24 group
elements and stated degree counts are checked. The120 alternative-route counts
are U/S scalar/internal-vector degrees1–3 only. No lattice dynamics or
infinite-system formation law is executed. Five matching stdout lines record
that scope.

**N6 — partial results.** The explicit invariants, positive menu functions,
recorded frame inverse and conditional dimension tables remain useful without
a physical representation-selection theorem.

**N7 — strongest objection.** A physical law may use content-dependent frames,
a different covariance representation or an equivariant role codomain.
Those possibilities are not excluded. The calculation does not settle how
the framework presents or physically relates internal and spatial symmetry.

**N8 — prior scope.** Occupancy-only vanishing repeats the conditional solder
boundary with a ten-stratum census. The handed parent distinguishes raw degree3 `T(q)` from a normalized
centre-dependent degree5 rule on its finite menu, with different internal groups. Current support-parent range corrections are respected.
No universal no-go or axiom change follows.

## Imports, falsifiers and evidence

Imports are the explicitly supplied representations, state/menu interpretation,
selector extension and standard Molien-Weyl, Lie-kernel, Reynolds and invariant
measure machinery. The linked repository results have the limited roles above;
no audit grade, new axiom or primitive is imported. A scalar-linear unsoldered
invariant, a second independent full-window cubic U scalar, an erroneous
frame transformation or a failed listed dimension is a genuine falsifier.
A linear vector covariant is allowed and is not a falsifier.

The [original source at frozen PR8122 head](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/a293aa3b67d64eda29ba959d43c209056c9ef7e4/docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md)
retains the complete historical note, with original runner/cache recoverable in
that same commit. It reports an out-of-band72-value floating nullity check and
nine caught mutations plus one diagnosed non-defect. No executable source or
stdout/stderr receipts for those historical claims are in the original delta;
they remain author narrative, not current reproducible evidence. The original
reported94 checks and approximately15seconds are historical. Current evidence
is the actual canonical runner/cache and the focused independent review.
The old mutation names concern determinant filtering, slot permutation, Haar
residue, occupancy sum, axis measure, modelB input, test rotation, selector
scale and kernel epsilon; the two-generator non-defect uses Lie closure.
No historical counts are substituted for present coverage.

## Verification

Primary: [runner](../scripts/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.py).
Receipt: [canonical cache](../logs/runner-cache/possibility_covariance_soldering_fork_invariant_rules_2026_09_14.txt).
Run with Python3; the original900-second envelope is retained. The computation
uses exact rational arithmetic and no scientific data files. Declared source
inputs are bound by hashes before execution; hashes prove identity only.
Canonical stdout contains the actual `TOTAL: PASS=... FAIL=...` and five honest
resolution lines. The runner exits nonzero if any check fails. No full pipeline
or audit verdict is produced by this unit.
