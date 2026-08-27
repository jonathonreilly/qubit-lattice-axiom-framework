---
claim_id: admissibility_dirac_kahler_three_direction_rule_geometry_bounded_theorem_note_2026-08-26
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md
claim_type: bounded_theorem
claim_scope: "Exact finite three-direction generator/parity identities; three- and six-face literal and shape-only cell systems; the unique uniform positive-volume literal-gluing point; one solvable but indefinite reciprocal point; and a declared exterior-algebra D3(g,V) candidate whose Schur identity holds on the three origin faces and fails on the three opposite faces. No unique lift, all-branch positivity classification, spacetime, dynamics, gravity, or continuum interpretation is supplied."
runner: scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the finite gluing principle does not select a physical three-dimensional lift, and the draft all-face Schur law fails on the opposite faces"
source_of_blocker_text: review_loop
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Classify the remaining nonuniform compatible branches and derive, rather than assume, any local face transport or physical selector before promoting a three-dimensional rule."
conditional_surface_status: "stacked on unmerged ancestor artifacts; scientific content is proposed for retention and remains audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-dimensional ranks, relation ideals, spectra, parity counts, compound identities, and explicit opposite-face counterexamples"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-axiom-closure-block202-record-pinning-mixture-diagnostics-20260826
parent_commit: 141b9e8da04319eb2f31c53389de6edd0cf723bf
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# Finite three-direction gluing algebra and the opposite-face boundary

**Date:** 2026-08-26

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author proposal only; independent audit is
required before any effective retained status.

**Standing:** conditional support on an unmerged PR stack. Nothing is
registered, adopted, or added to the axioms.

## Result

The runner retains six exact finite results.

1. The declared `4 x 4` generators square to identity and anticommute
   pairwise. With the declared corner staggering, every directed link on the
   three tested all-even extents scalarizes with the stated eta pattern. On
   `(4,3,2)`, exactly eight links fail, all on the wrap in the odd `x`
   direction.
2. The `8 x 8` corner sign matrix is well-defined at all 64 corner pairs and
   all eight anchor parities. Its word-form congruence is exact for any
   declared symmetric scalar target.
3. The three-origin-face literal system has ranks `(22,23)` and five exact
   compatibility relations. Its solution locus requires common volume and
   equal shear magnitudes but leaves the three signs unselected. The
   six-face literal system has ranks `(32,33)` and sixteen compatibility
   relations, including reciprocal cross-offset relations.
4. On the uniform positive-volume locus, the exact constraints
   `c^2+v^2-1=0` and `c^2 v=0` have only `(c,v)=(0,1)`. This is a theorem about
   that uniform branch, not all compatible cells. At the one reciprocal point
   `(c,v0,v1,c1)=(3/5,12/25,3/4,4/5)`, the system is solvable with four free
   complementary pairings, but its degree-1 and degree-2 principal blocks
   have spectra `(-3/20,6/5,6/5)` and `(-5/4,15/4,15/4)`. Those blocks contain
   none of the four free parameters, so no parameter choice makes that
   particular symmetric cell positive definite.
5. The declared exterior-algebra candidate

   ```text
   D3(g,V) = diag(V, V g^-1, E g E / V, 1/V),
   E = diag(1,-1,1)
   ```

   obeys the exact Jacobi/compound and duality identities. Its division by
   `V` is load-bearing. On the three origin faces, the restriction equals
   `diag(V,V S_p^-1,1/V)` with `S_p` the Schur complement of the missing
   direction.
6. The same Schur target is false on the opposite faces. At
   `(c_tx,c_ty,c_xy,V)=(1/5,1/7,1/9,2)`, the three exact residual matrices each
   have five nonzero entries, and their `(0,0)` defects are
   `1310/23159`, `2282/23159`, and `2682/23159`. Origin faces have global
   degrees `(0,1,1,2)`; opposite faces have `(1,2,2,3)`. No local regrading or
   transport map is constructed, so the origin identity is not promoted to an
   all-face theorem.

On the tested isotropic metric locus, exact Sylvester minors give positivity
ranges `0 <= kappa < 1` and `0 <= kappa < 1/2` for the two product-sign
classes. Both classes contain four sign patterns; only their interval endpoints
differ.

## Authority and dependencies

The construction is inherited from, and does not alter:

- [Block 202 finite substitution diagnostics](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md)
- [Block 128 curved-carrier dependency](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md)
- [Block 105 nonuniform Hodge overlap](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md)
- [Minimal Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Axiom/premise registry](audit/data/axiom_premise_nodes.json)
- [Gravity-mainline campaign charter](../.claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md)

The exact implementation is
[the Block-209 runner](../scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py).

## Finite generator and parity exhibit

Declare

```text
G1 = sx tensor I2,
G2 = sz tensor sx,
G3 = sz tensor sz,
Omega(t,x,y) = G1^t G2^x G3^y.
```

The exact link counts are

| extent | non-scalar counts by direction | wrap counts |
| --- | --- | --- |
| `(4,2,2)` | `(0,0,0)` | `(0,0,0)` |
| `(4,4,2)` | `(0,0,0)` | `(0,0,0)` |
| `(4,4,4)` | `(0,0,0)` | `(0,0,0)` |
| `(4,3,2)` | `(0,8,0)` | `(0,8,0)` |

This finite census supports a direction-local parity explanation for the
tested extents. It does not classify every extent or select these generators
physically.

## Literal and shape-only systems

The three origin faces impose 48 entry equations on the 36 independent entries
of a symmetric `8 x 8` matrix. Exact cokernel reduction gives five relations:

```text
v_tx-v_ty,
v_tx-v_xy,
c_tx^2 v_ty-c_ty^2 v_tx+v_tx-v_ty,
c_tx^2 v_xy-c_xy^2 v_tx+v_tx-v_xy,
c_ty^2 v_xy-c_xy^2 v_ty+v_ty-v_xy.
```

On the nonsingular domain, their common zero locus is common volume and equal
shear magnitudes. Four ordering/orientation convention variants give the same
ranks and primitive relations.

The shape-only systems are broader linear spaces. Three origin faces give rank
`14` and dimension `22`; twelve of 22 cross-degree pairs are forced zero. Six
faces give rank `22` and dimension `14`; the surviving pattern has four shared
degree diagonals, six within-degree couplings, and four complementary
cross-degree pairings. This is compatible with a Hodge-complement sparsity
pattern plus equal degree-1/degree-2 diagonals. It is not a uniqueness theorem
for all Dirac–Kähler forms.

## Declared `D3` candidate and the face-offset distinction

For the unit-diagonal symmetric metric

```text
g = [[1,c_tx,c_ty],[c_tx,1,c_xy],[c_ty,c_xy,1]],
```

the displayed `D3` is the standard exterior/Hodge extension conditional on the
chosen metric, global corner grading, wedge basis, and lower/upper
normalization split. The available premises do not force or uniquely select
that construction.

For origin faces, exact complementary-minor algebra gives the Schur restriction
and forces the comparison scale `lambda_p=1` and plane volume `v_p=V`. The
effective shear requires diagonal normalization; off the per-plane isotropy
locus, the Schur diagonal is not one. Exact equality with the landed 2D target
requires the two out-of-plane shears to vanish.

The opposite-face counterexample is structural, not numerical noise. Each
opposite face contains two degree-2 basis elements, so one of the three
2-form/2-form couplings becomes visible. Each origin face contains only one
degree-2 element and cannot see those pairings. A separately defined local
grading/transport could produce another face object, but none is part of this
claim.

## Interpretation boundary

- “Geometry” means a declared finite symmetric weight matrix and its
  positive-definiteness tests. It does not mean a metric field, spacetime,
  curvature, Einstein dynamics, or gravity.
- “Gluing” means a finite system of entry equalities. It does not mean
  propagation, evolution, field equations, or a continuum assembly rule.
- The uniform flat result applies only to the uniform literal-gluing branch.
  The reciprocal calculation excludes positivity only at its one exhibited
  point. Other nonuniform branches remain unclassified.
- `D3` is a standard candidate conditional on declared choices, not a
  framework-forced or uniquely selected lift.
- The origin-face Schur identity does not hold on the opposite faces without
  an additional map. The three 2-form couplings are invisible only to origin
  faces, not every coordinate-plane restriction.
- No landed number is corrected, no carrier equivalence is established, and
  no physical selection, generic-parameter, or continuum theorem is claimed.

## No-Go Discipline Gate

The gated negative is: **within the declared six-face literal-gluing system,
the uniform positive-volume branch contains only `(c,v)=(0,1)`, and the one
tested reciprocal curved point cannot be positive definite.** The note does
not claim that every nonuniform compatible cell is excluded.

### N1 — alternative-route enumeration

| normalized route | attack and exact outcome | honesty marker |
| --- | --- | --- |
| direct uniform elimination | Eliminate the six-face relations on the uniform locus; `c^2+v^2-1=0` and `c^2 v=0` with `v>0` give only `(0,1)`. | `ATTEMPTED` |
| reciprocal nonuniform branch | Use the reciprocal face relations rather than uniform equality; the exhibited curved point solves the system with four free parameters, so nonuniform compatibility is a genuine escape from the flat-only uniform statement. | `ATTEMPTED` |
| free-pairing positivity repair | Tune all four free complementary pairings at that reciprocal point; two parameter-free principal blocks remain indefinite, so this route cannot make that point positive definite. | `ATTEMPTED` |
| shape-only relaxation | Replace literal equality to the landed 2D target by its sparsity/equal-diagonal pattern; the solution space becomes 14-dimensional, showing that the stronger negative depends on literal gluing. | `ATTEMPTED` |
| metric-induced `D3` carrier | Use the declared exterior/Hodge candidate instead of the literal six-face ansatz; it has positive isotropic ranges but fails the same Schur target on opposite faces. This is a live alternative object and blocks any universal geometry no-go. | `ATTEMPTED` |

The routes differ in formulation and terminal obligation: polynomial
elimination, nonuniform compatibility, positive-definiteness completion,
constraint relaxation, and alternate carrier construction. No route is marked
ruled out by prior authority.

### N2 — wall-independence audit

The collapsed wall set is:

- `W1`: literal equality to the landed 2D target on six faces;
- `W2`: uniform face moduli for the flat-only theorem;
- `W3`: real shear and positive volume;
- `W4`: positive definiteness for interpreting a compatible matrix as a
  positive finite weight.

| pair | closing first closes second? | closing second closes first? | independent? |
| --- | :---: | :---: | :---: |
| `W1,W2` | no | no | yes |
| `W1,W3` | no | no | yes |
| `W1,W4` | no | no | yes |
| `W2,W3` | no | no | yes |
| `W2,W4` | no | no | yes |
| `W3,W4` | no | no | yes |

Uniformity does not imply literal face equality; compatibility does not imply
positivity; and positivity does not choose the target or moduli branch.

### N3 — hidden-wall scan

| phrase class | occurrence and classification |
| --- | --- |
| “declared” / “by construction” | Generator choice, global corner grading, plane target, and `D3` normalization are load-bearing imposed choices and are stated explicitly. |
| “standard” | “standard exterior/Hodge extension” is classified as a candidate conditional on the declared metric and basis; it carries no selection authority. |
| “framework provides” / “naturally” / “obviously” | No load-bearing positive use occurs. The note expressly says the framework does not select the lift. |
| “background” | No background is used to extend the uniform or reciprocal results beyond the finite systems. |
| “registered” / “canonical” | Nothing is registered or adopted; no premise weight is inferred. |

No hidden condition expands `W1-W4`.

### N4 — residual matching

| cited source | source residual | residual here | exact match? | disposition |
| --- | --- | --- | :---: | --- |
| [Block 105](ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md) | defines the finite 2D `shear_hodge` target | compatibility/positivity of one 3D six-face system | no | target authority only, not a no-go witness |
| [Block 128](ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md) | imports the curved target and records a carrier dependency | uniform/reciprocal six-face cell residual | no | import path only, not a witness |
| [Block 202](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md) | finite profile common-vector obstruction | cell-gluing compatibility and positivity | no | stack parent only, not a witness |

All nonmatching prior negatives are dropped from proof support. Exact polynomial
elimination and principal-block spectra are the sole negative certificates.

### N5 — rhetoric audit and five resolution levels

N5: per_element: The three generator matrices, corner grading, plane targets, and D3(g,V) are declared finite algebraic objects. Their exact identities do not select a physical rule, metric field, spacetime, dynamics, gravity law, or continuum limit; nothing is registered or adopted.
per_site: On the three tested all-even extents every directed link scalarizes with the stated eta pattern, while (4,3,2) has exactly eight non-scalar x-wrap links. This is a finite parity count for the declared generators, not an all-extent theorem.
per_mode: The three-origin-face literal system has ranks (22,23) with five overlap relations; the six-face system has ranks (32,33) with sixteen. On the uniform positive-volume locus the two exact constraints give only (c,v)=(0,1); one reciprocal curved point is solvable but has parameter-free indefinite principal blocks. Other nonuniform branches remain unclassified.
per_block: The standard exterior-algebra candidate D3=diag(V,V g^-1,E g E/V,1/V) obeys the compound identities and the Schur target on the three origin faces only. The same target fails on the three opposite faces with exact residual counts (5,5,5) because the global degree pattern changes; no local regrading or transport is supplied.
lattice_wide: On the tested isotropic metric locus, Sylvester minors give positivity endpoints kappa=1 and kappa=1/2 for the two product-sign classes. This does not classify all compatible cells, choose D3 over other lifts, or establish physical geometry; all content remains finite-instance proposed_retained and TOE movement is zero.

The executed resolutions are the finite site, mode, block, and selected metric
locus. The runner checks rather than executes physical interpretation at the
per-element and lattice-wide levels. No negative is phrased beyond those
tested resolutions.

### N6 — partial-closure path scan

| possible path | status | what it could close |
| --- | --- | --- |
| [Axiom/premise registry](audit/data/axiom_premise_nodes.json) | current authority, scanned | supplies no approved physical 3D-lift selector or face-transport primitive |
| local face regrading/transport | open convention/construction route | could map opposite faces to locally graded objects, after which a new target identity must be derived and tested |
| shape-only reframe | executed | replaces literal target equality with a broader sparsity principle and removes the flat-only rigidity claim |
| alternate metric-induced carrier | executed as `D3` candidate | supplies positive finite matrices on bounded loci but is not selected and does not satisfy the draft all-face identity |

No new axiom is declared necessary. Convention, transport, and alternate-carrier
routes remain legitimate partial closures.

### N7 — hostile steelman

A hostile reviewer should reject “literal gluing plus positivity permits only
flat geometry” outside the uniform and one tested reciprocal branches. The
six-face relation variety may contain other nonuniform points with positive
completions, and a local face grading could change the opposite-face object.
The strongest constructive counterroute is to parameterize the remaining
compatible variety, impose Sylvester inequalities before specialization, and
derive a face transport from the global corner representation. Those terminal
obligations are unclosed. This steelman defeats a universal no-go, so none is
claimed; it does not alter the exact uniform elimination or the one-point
principal-block obstruction.

### N8 — cross-cycle echo and decision cut

[Block 201](ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md)
and [Block 202](ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md)
both preserve finite algebra while leaving a physical selection map open. Those
walls have not been retired. Their repair mechanism—derive an independent
selector or instrument and then bridge it explicitly—applies here as “derive a
3D lift selector and face transport.” No similar wall is treated as permanently
closed by convention alone.

Decision: retain the finite parity, rank, relation, spectrum, compound, and
origin-face identities as `proposed_retained`; retain the opposite-face
counterexample; withdraw the all-face Schur, framework-forced lift, and global
flat-only readings. Register no premise, adopt no object, and move no TOE
percentage.

## Verification contract

The runner declares 36 claim-only mutations. Each must fail exactly its mapped
gate. Baseline output must remain below the runner-output cap, and the canonical
cache must bind the runner plus all declared authority inputs.

## Decision

This block is valuable finite gluing algebra. Its repaired form keeps the exact
three-direction and rigidity calculations while making the face-offset failure
and the missing physical selector explicit.
