# Finite Oriented-Diagonal Stencil and Projection Census — Cycle 722

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit status is set only by the independent audit lane. This
note changes no axiom, approved primitive, premise registry, policy, queue, or
audit-status surface.

Primary runner:
`scripts/physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02.py`;
canonical cache:
`logs/runner-cache/physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02.txt`;
paired receipt:
`outputs/physical_oriented_diagonal_stencil_orbit_cycle722_2026_08_02_receipt_2026-08-02.json`.

This cycle classifies the eight Kuhn path stencils of one 4-cell and their
finite assembled forms. Exact signed-permutation arithmetic distinguishes
spatial determinant, reversal of a stencil's diagonal orientation, and tick
sense. Numerical assembly at the declared sizes then measures when tick
projections identify complementary stencils and which exact spatial subgroup
is admitted by each projected form.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "classify wider admissible stencil families and separate projection-induced frame classes from supplied triangulation choices"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "enumerate additional cell triangulations and test their proper-frame orbit decomposition"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "Exact finite group arithmetic and numerical Cycle-696 assembly/projection censuses for the declared Kuhn family, sizes, tick lengths, and projections."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the group action is exhaustively enumerated on a finite family, while assembled-form identities use the supplied finite-difference compiler on a finite parameter grid"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied setting and imported inputs

The [Cycle-696 compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
supplies the 15 direction classes, length-class map, analytic simplex and area
gradients, and finite-difference Hessian step. Its transitive Cycle-576 and
Regge script imports are declared in `AUDIT_INPUT_PATHS`. The runner rebuilds
the same local pieces on a spatially open, tick-periodic complex rather than
copying assembled matrices.

The [tick-extension note](CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md)
supplies the interpretation of this 3+1 path complex. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
supply spatial translations, nearest-neighbour adjacency, and the 24 proper
cubic rotations. The eight Kuhn path stencils, their equal-weight average,
the open finite boxes, the projections, and the `1.0e-09` comparison tolerance
are analysis choices in this cycle rather than axiom content. Reported scalar
relations use `1.0e-06`, and the contraction rejector shifts the factor by
`1.0e-03`; both are declared runner constants and receipt fields.

For `a in {0,1}^3`, stencil `S_a` contains the 24 monotone 4-simplex chains
from `(a,0)` to `(1-a,1)`. Its main diagonal is oriented by that ordered pair.
The complement pair `S_a,S_(1-a)` shares one unoriented diagonal line.

The executed assembly surfaces are:

- static contractions at `L in {3,4}` and `LT in {2,3}`;
- full stencil covariance at `(L,LT)=(3,3),(4,2)`;
- eight-form/frame-label scans at `L=3`, `LT in {2,3,5}`;
- twelve projection rows at `L=3`, `LT in {2,3,5}`;
- temporal-removal and fold discriminator rows at `L=3`,
  `LT in {3,4,5}`;
- tick-sense subgroup scans at `L=3`, `LT in {2,3,4,5}`;
- equal-weight orbit-average tests at `(L,LT)=(3,3)`.

## Exact target and proof-obligation graph

The exact target is to determine the finite spatial-frame action on the eight
declared stencils and to classify, on the executed assembly grid, whether each
projection admits the oriented-diagonal stabilizer or the unoriented-line
stabilizer.

1. **Stencil geometry — CLOSED exactly.** The runner reconstructs every path
   simplex and all 1,920 edge slots. The sign-absorbing edge classifier agrees
   with the supplied source stencil on all 240 source slots and satisfies the
   anchor law on all eight stencils.
2. **Finite frame action — CLOSED exactly.** All 48 signed spatial permutation
   matrices, the 24 determinant-`+1` members, their corner actions, subgroup
   closures, coset relation, and determinant splits are enumerated in integer
   arithmetic.
3. **Tick-resolved compiler extension — CONDITIONAL/numerical.** The same local
   gradient and finite-difference Hessian machinery is applied at the declared
   tick lengths. Its static contractions are compared directly with Cycle 696.
4. **Projection/subgroup identification — CLOSED on the finite numerical
   surface.** Each of twelve rows gates equality with the exact expected matrix
   subgroup, not only its cardinality. Complementary-stencil identification is
   tested at the declared tolerance.
5. **Wider physical interpretation — OPEN.** Other triangulation families,
   selection laws, cell structures, boundary conditions, and continuum limits
   are future targets.

**Proof-obligation disposition:** `CONDITIONAL`. The exact combinatorial group
claims are closed. Every assembled-form statement remains conditional on the
supplied Cycle-696 local compiler and is finite/numerical on the grid above.

## Exact finite orbit and grading structure

The 24 proper rotations act transitively on both the eight oriented diagonals
and the four unoriented lines:

| acting set | orbit size | stabilizer size |
|---|---:|---:|
| 24 proper frames, oriented diagonal | 8 | 3 |
| 24 proper frames, unoriented line | 4 | 6 |
| 48 signed spatial frames, oriented diagonal | 8 | 6 |
| 48 signed spatial frames, unoriented line | 4 | 12 |

The order-six oriented stabilizer and order-twelve line stabilizer are closed
matrix subgroups. The six elements in their nontrivial coset reverse the
diagonal orientation. This orientation grading is distinct from spatial
determinant:

| diagonal action inside the line stabilizer | determinant `+1` | determinant `-1` |
|---|---:|---:|
| preserves the diagonal orientation | 3 | 3 |
| reverses the diagonal orientation | 3 | 3 |

Consequently, the proper line sextet contains three orientation-preserving and
three orientation-reversing elements. “Proper/improper” and “preserves/reverses
the diagonal orientation” are separate binary classifications.

The eight Kuhn stencils form one proper-frame orbit, and no individual member
is fixed by all 24 proper frames. Therefore a choice of one member within this
declared family is additional supplied structure. This is a finite orbit fact,
not a classification of every admissible cell triangulation or every covariant
selection rule.

## Tick-resolved assembly and finite covariance

Folding the tick-resolved form onto static spatial variables reproduces
`(LT/2) Q_static` below `1.0e-09` in all four declared contraction rows. The
largest supplied static-form entry is `2.945214e+01`; changing the factor by
`1.0e-03` produces deviation `2.945214e-02`.

At `(L,LT)=(3,3)` and `(4,2)`, all 192 proper-frame/stencil pairs satisfy

    m_g Q[S_a] m_g^T = Q[S_(g.a)]

below `1.0e-09`. Holding `S_000` fixed while applying the same frame action is
a discriminating alternative and reaches deviation `2.789850e+00`.

Spatial box-centre reflection maps `S_000` to `S_111`. At both executed box
rows it intertwines their forms below tolerance; applying it while holding the
stencil fixed costs `2.789850e+00`, equal to the nearest different-stencil
separation on those rows.

At `L=3` and `LT=2,3,5`, the eight supplied stencils give eight distinct forms
and eight proper-frame classes. These classes name oriented diagonals on the
declared tick-resolved fixture.

## Projection and tick-sense census

For the complement pair `S_000,S_111`, the twelve declared projection rows give:

| tick length | tick-resolved, all classes | tick-resolved, temporal removed | tick-folded, all classes | tick-folded, temporal removed |
|---:|---|---|---|---|
| 2 | separated `2.789850`, oriented stabilizer 6 | identified, line stabilizer 12 | identified, line stabilizer 12 | identified, line stabilizer 12 |
| 3 | separated `2.789850`, oriented stabilizer 6 | separated `1.000000`, oriented stabilizer 6 | identified, line stabilizer 12 | identified, line stabilizer 12 |
| 5 | separated `2.789850`, oriented stabilizer 6 | separated `1.000000`, oriented stabilizer 6 | identified, line stabilizer 12 | identified, line stabilizer 12 |

Every row checks exact set equality with the relevant signed-spatial matrix
subgroup and checks subgroup closure. The tick fold also identifies the pair at
`LT=4`, while temporal-class removal leaves separation `1.000000` at
`LT=3,4,5`. Thus these two projections coincide on this comparison at `LT=2`
and differ on the three tested longer ticks.

On the unprojected `L=3` complex, allowing tick translations admits exactly the
oriented stabilizer at each `LT=2,3,4,5`. Allowing tick reversal as well admits
exactly the line stabilizer. The additional six spatial frames reverse the
stencil-diagonal orientation; their spatial determinants remain split `3+3`.

## Orbit average and adjacency seam

At `(L,LT)=(3,3)`, the equal-weight average of the eight forms admits all 24
proper axiom frames. On this finite fixture it additionally admits all 24
orientation-reversing signed spatial frames. The latter numerical extension is
reported separately from the axiom's proper-frame grant. The averaged form has
one proper-frame class and lies `1.394925e+00` from `Q[S_000]`, half the measured
different-stencil separation.

The source stencil contains 240 simplex edge slots with multiplicity. Of its
120 purely spatial slots, 72 use an axis nearest-neighbour class and 48 use a
longer diagonal class. This locates the supplied triangulation structure beyond
the minimal nearest-neighbour adjacency without turning that inventory into an
axiom-level selection statement.

## Claim boundary

The claim domain is the eight declared Kuhn stencils, the exact finite matrix
groups above, the supplied Cycle-696 local assembly, and the explicitly listed
finite grid. Numerical equality means the declared `1.0e-09` threshold.
“Oriented” always refers to the ordered stencil diagonal; “proper” always refers
to spatial determinant `+1`; “tick reversal” refers to the relabeling in the
runner. These labels are intentionally non-interchangeable.

Other admissible triangulations, enriched vertices, varying stencil fields,
state-dependent selection laws, larger cells, other regions or boundary rules,
arbitrary tick lengths, source/readout observables, and continuum interpretations
remain separate questions. The measured form distances are fixture outputs rather
than physical costs or selected constants.

## Runner and evidence

The primary runner declares its complete transitive script input closure and
`AUDIT_TIMEOUT_SEC = 300`. It recomputes all exact group rows and numerical
assembly rows, writes the paired receipt with unique descriptive gates, and is
cached through `scripts/runner_cache.py` so runner and input bytes are bound in
the canonical header.

## Load-bearing dependencies

- [Cycle 720](PHYSICAL_AMBIENT_DOMAIN_SYMMETRY_SPLIT_CYCLE720_NOTE_2026-08-02.md)
  supplies the finite distinction between the axis-permutation factor, spatial
  determinant, and the proper half; this cycle reproduces that distinction on
  the narrower oriented-diagonal/line subgroups.
- [Cycle 721](PHYSICAL_STENCIL_DERIVED_CENTRALITY_CYCLE721_NOTE_2026-08-02.md)
  supplies the exact folded-stencil and proper-sextet reading that this cycle
  resolves before and after tick projections. The present tick-sense census
  supersedes only the earlier expectation about longer ticks, not Cycle 721's
  repaired finite group facts.
- The linked Cycle-696 script supplies the executable local assembly contract.
  The tick-extension and minimal-axiom notes supply only the setup and the
  proper-frame scope stated above.

Cycle 690's eight-vertex triangulation ceiling and Cycle 695's distinction
between direction-set and triangulation covariance are contextual comparisons;
their conclusions are independently recomputed where relevant rather than used
as premises.

## Review record

Review replaced the submitted framework-level “axioms select no stencil” claim
with the exact finite orbit/fixed-point statement supported by the eight-member
census. It corrected the submitted identification of the diagonal-orientation-
reversing coset as an “improper half”: each orientation class is determinant
`3+3`, while the proper sextet draws three from each. It separated the 24-frame
axiom grant from the additional 48-frame numerical invariance of the orbit
average; made the reflection's two-box evidence explicit; and strengthened the
twelve projection gates from a one-sided count predicate to exact subgroup set
equality and closure. It also added direct Cycle-720/721 edges, complete status
and proof surfaces, transitive input declarations, a timeout, structured receipt,
and canonical cache. The repaired package is a positive finite classification;
independent audit remains required before any effective retained grade.
