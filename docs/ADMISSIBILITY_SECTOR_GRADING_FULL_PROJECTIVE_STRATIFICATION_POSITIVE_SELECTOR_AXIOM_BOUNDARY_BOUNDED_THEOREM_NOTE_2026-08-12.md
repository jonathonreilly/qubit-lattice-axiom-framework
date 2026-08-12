---
claim_id: admissibility_sector_grading_full_projective_stratification_positive_selector_axiom_boundary_bounded_theorem_note_2026-08-12
claim_type: bounded_theorem
claim_scope: "On the complete stipulated six-direction, three-sector, 1,296-support model of the Cycle-876 grading parent, every nonzero real projective grading is classified exactly. The 3-by-3 balance matrices split as 96 rank-one, 768 rank-two, and 432 rank-three. The rank-one kernels form six projective lines and the rank-two kernels form eleven projective points. Incidence gives unrestricted lawful-support maximum 216 at exactly [0:1:-1], [0:1:1], and [1:0:0]. On the strictly positive projective cone, [1:1:1] is the unique maximum, with 90 lawful supports; any nonspecial point has at most 36. On the closed nonnegative cone the unrestricted maximum remains twofold, at [0:1:1] and [1:0:0], so strict positivity is load-bearing. This closes the parent's open projective classification on its stipulated model and yields an exact conditional selector: strict positivity plus lawful-support maximization implies unit grading. Neither premise is current-axiom content, and direct adoption of [1:1:1] would be weaker than adopting that maximization principle. The model, vector-readout ansatz, physical object lineage, physical chirality/sign carrier, grammar exhaustiveness, and law-selection authority remain open. No physical grading, generation count, Koide relation, signed gravity result, axiom amendment, audit verdict, or TOE percentage movement is claimed."
upstream_dependencies:
  - minimal_axioms
  - grading_affine_chart_algebra_cycle876_support_note_2026-08-09
runner: scripts/admissibility_sector_grading_full_projective_stratification_positive_selector_boundary_2026_08_12.py
---

# Full Projective Sector-Grading Stratification And Positive Selector Boundary

**Date:** 2026-08-12

**Type:** `bounded_theorem`

**Role:** close the projective-classification problem explicitly left open by
the Cycle-876 salvage, test whether its unit grading is selected anywhere on
the complete stipulated model, and convert the result into a precise axiom
choice without confusing conditional selection with physical TOE closure.

**Audit-status authority:** independent audit lane only. This source note
authors no audit verdict and predicts none.

**Premise sources:**
[Minimal Axioms (2026-06-29)](MINIMAL_AXIOMS_2026-06-29.md) and the
[Cycle-876 affine-chart grading parent](GRADING_AFFINE_CHART_ALGEBRA_CYCLE876_SUPPORT_NOTE_2026-08-09.md).

**Primary runner:**
[admissibility_sector_grading_full_projective_stratification_positive_selector_boundary_2026_08_12.py](../scripts/admissibility_sector_grading_full_projective_stratification_positive_selector_boundary_2026_08_12.py)

## Result Up Front

The full projective calculation is now exact, and it gives both a selector and
the reason that selector is not yet physical.

On the parent package's stipulated one-block model, a support consists of an
incoming signed cubic direction `d` and one occupied direction in each of the
matter, field, and auxiliary sectors. For grading

~~~text
w = (w_m, w_f, w_a),
~~~

the support is lawful when its three-vector balance vanishes. Across all
`6*6^3=1,296` supports, the exact balance matrices have ranks

~~~text
rank 1:  96,
rank 2: 768,
rank 3: 432.                                             (1)
~~~

Rank one gives six projective kernel lines. Rank two gives eleven isolated
projective kernel points. Rank three gives no nonzero grading. Every possible
lawful grading therefore lies on the listed finite line arrangement, and all
line intersections are among the eleven listed points. This is a complete
classification of the real projective plane for the stipulated model, not a
grid scan or an affine-chart extrapolation.

The unrestricted lawful-support maximum is `216`, attained at exactly three
unrestricted maximizers:

~~~text
[0:1:-1], [0:1:1], [1:0:0].                              (2)
~~~

Thus lawfulness count alone does not select a grading. The result changes on
the strictly positive projective cone. There the unit class

~~~text
[1:1:1]                                                   (3)
~~~

is the unique maximizer, with `90` lawful supports. Every nonspecial point on
a lawful line has at most `36`, and every point off the six lines has zero.
However, strict positivity is load-bearing: on the closed nonnegative cone,
the two boundary points `[0:1:1]` and `[1:0:0]` both retain the unrestricted
maximum `216`.

Therefore the exact conditional theorem is:

> On the stipulated Cycle-876 model, strict positivity plus lawful-support
> maximization selects the unit projective grading uniquely.

Those two selector premises are not current-axiom content. The current
framework does not identify this stipulated grading with a physical
chirality/sign carrier either. Directly adopting the exact class `[1:1:1]`
would be a logically weaker constitutional change than adopting a general
maximization principle whose physical meaning has not been derived.

This closes one explicit Root-B algebra problem. It does not close Root B and
moves no TOE percentage.

## Exact Target And Proof-Obligation Graph

| Obligation | Evidence | Disposition |
|---|---|---|
| replace the parent's affine chart plus one infinity control by a full projective classification | exact rank stratification of all 1,296 balance matrices | closed on the stipulated model |
| enumerate every positive-dimensional lawful stratum | six primitive line normals with exact multiplicities | closed |
| enumerate every isolated lawful stratum | eleven primitive projective kernels with exact multiplicities | closed |
| include all incidence enhancements | direct counts equal rank-two multiplicity plus all incident rank-one families | closed |
| identify unrestricted maximizers | exactly three classes at count 216 | closed |
| test positivity as a selector | strict cone has unique unit maximum 90; closed cone has two maxima 216 | closed conditionally |
| derive strict positivity from the four axioms | no sector grading is named by the current foundation | open |
| derive lawful-support maximization as the physical selection rule | no such variational rule is supplied | open |
| identify the model grading with generation chirality or the gravity sign | parent and predecessor packages leave the physical lineage open | open |
| prove the stipulated model/grammar exhausts physical grading laws | no such theorem is attempted | open |

The strongest missing lemma is no longer “classify the projective grading
space.” It is:

> Derive one physical map from the framework's `M_2(C)` Record and
> Admissibility objects to this sector grading, including its sign meaning and
> selection rule, or adopt one exact grading class as extensional law content.

The current theorem makes that choice auditable. It does not make the choice.

## 1. Reconstructed Model

Let the six stipulated directions be

~~~text
D = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
~~~

For incoming direction `d` and occupied sector triple `(m,f,a)`, define the
three-by-three balance matrix by its columns:

~~~text
M(d;m,f,a) = [D_m-D_d | D_f | D_a].                       (4)
~~~

The grading `w=(w_m,w_f,w_a)` makes the support lawful exactly when

~~~text
M(d;m,f,a) w = 0.                                         (5)
~~~

Equation (4) is rebuilt independently from the parent package's declared
stipulations. No Cycle-876 result table is imported. The runner uses primitive
integer vectors throughout; projective representatives are divided by their
greatest common divisor and given a fixed sign.

The parent model and its supplied vector-readout ansatz remain conditions of
the theorem. Reconstructing them does not derive them from Lattice, Qubit,
Admissibility, or Record.

## 2. Why The Classification Is Exhaustive

For each support, exact matrix rank gives all possibilities:

- rank three: only `w=0`, so there is no projective lawful grading;
- rank two: the kernel is one-dimensional, hence one isolated projective
  point;
- rank one: the kernel is two-dimensional, hence one projective line; and
- rank zero: the whole projective plane would be lawful, but no such support
  occurs.

The exact census (1) accounts for all 1,296 supports. Canonicalizing identical
kernels gives the six lines and eleven points below. Every intersection of two
distinct listed lines occurs among the eleven points. Consequently:

1. a point off all six lines and eleven points has count zero;
2. a nonspecial point on one line has that line's displayed multiplicity;
3. an isolated point has its rank-two multiplicity plus every incident line's
   multiplicity.

There is no unexamined projective region or numerical continuity assumption.

## 3. Six Projective Lines

The table gives primitive line normal `n` for the locus `n dot w=0` and the
number of rank-one supports whose complete kernel is that line.

| line normal `n` | generic lawful-support count |
|---:|---:|
| `(0,1,-1)` | 36 |
| `(0,1,1)` | 36 |
| `(2,-1,-1)` | 6 |
| `(2,-1,1)` | 6 |
| `(2,1,-1)` | 6 |
| `(2,1,1)` | 6 |

The Cycle-876 affine balance plane is the line with normal `(2,-1,-1)`.
Its six always-lawful supports are therefore recovered as one stratum of the
full projective arrangement rather than treated as the whole domain.

## 4. Eleven Projective Points And Incidences

| projective class | rank-two multiplicity | incident-line contribution | total |
|---:|---:|---:|---:|
| `[0:1:-1]` | 168 | 48 | 216 |
| `[0:1:1]` | 168 | 48 | 216 |
| `[1:-2:0]` | 24 | 12 | 36 |
| `[1:-1:-1]` | 48 | 42 | 90 |
| `[1:-1:1]` | 48 | 42 | 90 |
| `[1:0:-2]` | 24 | 12 | 36 |
| `[1:0:0]` | 144 | 72 | 216 |
| `[1:0:2]` | 24 | 12 | 36 |
| `[1:1:-1]` | 48 | 42 | 90 |
| `[1:1:1]` | 48 | 42 | 90 |
| `[1:2:0]` | 24 | 12 | 36 |

The runner recomputes each total a second way by testing all 1,296 matrices
directly on the representative. The two routes agree exactly.

The coefficient-two point `[1:2:0]` emphasized by the provenance package has
count 36. The unit point has count 90. Neither is an unrestricted maximizer;
the chart-infinity counterexample was a real warning, not a nuisance to be
discarded.

## 5. Selector Domains

### Unrestricted real projective domain

The largest point total and largest generic line multiplicity are compared.
Equation (2) is the exact threefold maximum. Lawfulness maximization alone is
therefore underdetermined.

### Closed nonnegative cone

A projective class has a nonnegative representative when all nonzero entries
can be given one sign. Two unrestricted maxima survive:

~~~text
[0:1:1], [1:0:0].                                         (6)
~~~

Allowing a sector weight to vanish does not select the unit grading.

### Strictly positive cone

Among the eleven isolated points, `[1:1:1]` is the only class with three
strictly positive coordinates. Its count is 90. Every other strictly positive
point is either nonspecial on one of the six lines, with count at most 36, or
off the line arrangement, with count zero. Hence (3) is the unique strict-
positive maximum.

The strict/closed distinction is not rhetoric. It changes the maximizer from
one interior class to a twofold boundary fork.

## 6. Axiom-Choice Packet

The exact implication can be used in two constitutionally distinct ways.

### Derivation route

Prove from current structure that:

1. the physically relevant sector grading lies in the strictly positive
   projective cone; and
2. the physical law selects the grading with the largest lawful support family
   on this exact model.

Then the unit class follows as a theorem. At present, both statements are
additional physical content. Positivity of an Admissibility probability
measure does not automatically type these sector coefficients as
probabilities, and no current axiom says to maximize a finite candidate-law
support count.

### Direct extensional route

If governance chooses the grading rather than a general principle, the weaker
model-scoped datum is simply:

> On the declared three-sector carrier, the physical sector grading is the
> projective class `[1:1:1]`.

This is hypothetical wording, not an edit or recommendation. It supplies less
new law than “strict positivity plus maximize lawfulness,” because it does not
assert a variational principle beyond this carrier. It also remains
insufficient for Root-B closure until a theorem identifies the sector carrier
and its grading with the physical generation-chirality and sign observables.

Neither route is ready for a canonical axiom edit. The correct current output
is the exact choice packet and the remaining bridge, not an empty placeholder
called “physical grading.”

## Promotion Value Gate

| Gate | Assessment |
|---|---|
| V1 -- explicit high-fanout residual | closes the projective classification named open by Cycle 876, inside the Root-B grading gate |
| V2 -- exact next decision | separates direct unit adoption from the stronger positivity-plus-maximization principle and names the physical-lineage theorem still needed |
| V3 -- framework contact | evaluates the actual carried one-block grading model used by the chirality/sign program |
| V4 -- marginal content | adds the complete six-line/eleven-point stratification and all-domain maximizer theorem; no prior source states it |
| V5 -- independent reviewability | exact integer runner rebuilds every support, proves exhaustiveness by rank, and cross-checks incidence counts by direct evaluation |

The value gate passes for a Root-B axiom-choice theorem. It does not authorize
a TOE percentage move because the selector premises and physical carrier are
not derived or adopted.

Accordingly, no TOE percentage movement is claimed.

## No-Go Discipline Gate

The narrow negative statements are only:

1. lawful-support maximization on the unrestricted stipulated projective
   domain is not unique; and
2. the current axiom text does not state that this model's sector grading is
   strictly positive, lawfulness-maximizing, or physically identified.

No claim is made that the unit grading cannot be derived downstream or that
Root B requires a new axiom.

### N1 -- Alternative Route Enumeration

| normalized route | attack and outcome | marker |
|---|---|---|
| full unrestricted projective classification | rank every support matrix and assemble every kernel incidence | `ATTEMPTED`; exact threefold maximum |
| strict-positive maximization | restrict the completed arrangement to three nonzero equal-sign weights | `ATTEMPTED`; unique unit maximum |
| closed nonnegative maximization | allow sector deletion at the boundary | `ATTEMPTED`; twofold maximum survives |
| direct unit-class adoption | specify `[1:1:1]` without a new variational principle | live governance route; no adoption here |
| derive equal weights from a physical sector symmetry | matter, field, and auxiliary have different roles in (4); no such symmetry theorem is supplied | `ATTEMPTED` as premise search; route remains live on a richer carrier |
| derive grading from the `M_2(C)` Record/readout law | requires an explicit map from readable content to these three coefficients | live high-value bridge |
| select a different extensional joint law | a complete Root-A/Root-B law may choose a grading without maximizing this support count | live counterroute |

These routes differ in domain restriction, selection principle, direct law
datum, symmetry mechanism, Record carrier, and complete joint law. Multiple
routes remain live, so a universal no-go is unavailable.

### N2 -- Wall-Independence Audit

After collapsing dependent wording, four walls remain:

- `W_D`: the physical grading domain, including strict versus weak positivity;
- `W_S`: the selector or exact chosen projective class;
- `W_L`: the map from the stipulated sector ledger to the physical
  chirality/sign carrier; and
- `W_E`: exhaustion of the stipulated one-block model by the physical law.

| pair | does closing either close the other? | independent? |
|---|---|---:|
| `W_D,W_S` | no; a domain does not choose a point, and a direct point does not derive a domain principle | yes |
| `W_D,W_L` | no; positivity does not identify the carrier | yes |
| `W_S,W_L` | no; a unit vector on a stipulated ledger need not be physical chirality | yes |
| `W_E` with any other wall | no; model exhaustion is separate from selection inside the model | yes |

Projective classification is no longer counted as a fifth wall; this theorem
closes it on the declared model.

### N3 -- Hidden-Wall Scan

“Projective” means nonzero real triples modulo nonzero real scaling.
“Lawful” means equation (5) only. “Positive” means a representative with all
three entries strictly positive; it is not imported from probability
positivity. “Maximization” means cardinality of the 1,296 stipulated lawful
support family, not entropy, action minimization, or observed frequency.
“Unit” means the projective class `[1:1:1]`, not a derived unit of measurement.
The stipulated model, vector-readout ansatz, finite one-block scope, and lack
of physical-lineage authority are explicit.

### N4 -- Residual Matching

| prior residual | present target | match? |
|---|---|---:|
| Cycle-876 open full projective classification | all nonzero projective gradings for the same stipulated support balance | yes |
| Cycle-876 chart-infinity count 216 | one of three exact unrestricted maximizers | yes |
| Cycle-873 supplied unit grading | test whether the unit point is selected under explicit domains | yes |
| Cycle-868 physical-sign identification gap | not solved by projective algebra | preserved, not claimed closed |
| grammar/object-lineage exhaustion | not a projective-incidence question | preserved, not claimed closed |

The theorem closes exactly the parent's named algebraic residual and does not
borrow that closure for the physical interfaces.

### N5 -- Rhetoric And Resolution Audit

The runner executes every matrix element of all 1,296 supports
(`per_element`), the complete stipulated one-block model (`per_site`), all six
projective lines, eleven points, and incidences (`per_mode`), and all three
selector domains (`per_block`). It prints that no full-`Z^3` or physical-
lineage theorem is executed (`lattice_wide`). The note says “unique” only on
the strict-positive conditional domain and says “threefold” on the
unrestricted domain.

### N6 -- Partial-Closure And Primitive Scan

The current minimal-axiom source does not type these three sector coefficients
or supply their selector. It also does not forbid a downstream theorem.
Partial closure is now substantial: affine and projective
algebra are complete on the stipulated model, strict-positive selection is
exact, and direct unit adoption has a one-datum form. A physical Record
compiler, a complete joint law, or a retained sector-lineage theorem can still
derive the needed input without an axiom change.

### N7 -- Steelman

A hostile reviewer should object that “maximize the number of lawful finite
supports” is an invented objective, not a physical principle. The unit point's
conditional uniqueness therefore carries no more physical authority than the
premise that defines the optimization. The reviewer should also note that
directly choosing `[1:1:1]` is weaker than adding that objective, and that a
richer physical model may not preserve the same count. This steelman succeeds.
It forces the result to remain an exact classification plus choice packet.

### N8 -- Cross-Cycle Echo

The original Cycle-876 package overreached from an affine chart to a global
maximizer; review found `[0:1:-1]` with count 216 versus the unit count 90. The
salvage kept that point as a required negative control and declared the full
projective problem open. This block incorporates the counterexample, finds its
two equal-count partners, and proves the complete arrangement. It does not
resurrect the rejected unrestricted-unit claim. As in prior Root-A selector
work, a conditional unique optimum is not treated as physical law selection.

**N1--N8 status: `PASS` for the narrow stipulated-model classification and
axiom-choice boundary.** A universal Root-B no-go fails N1 and N7 and is not
shipped.

## Reproduction

From the repository root:

~~~bash
python3 scripts/admissibility_sector_grading_full_projective_stratification_positive_selector_boundary_2026_08_12.py
~~~

Expected final line:

~~~text
TOTAL: PASS=8 FAIL=0
~~~

## Conclusion

The projective grading question was worth completing because it is a Root-B
fanout point, not another gravity regulator. Its answer is exact: the complete
stipulated domain has three unrestricted maximizers, while strict positivity
turns the unit class into the unique maximum. That gives a sharp conditional
selector and an equally sharp warning about its premise cost.

The next qualifying work is the physical bridge: derive the sector grading
and sign carrier from Record/Admissibility or a complete joint law, or present
the exact unit-class datum for owner choice. More count grids inside this
already classified one-block model would be low leverage. Until the physical
carrier and selector are derived or adopted, Root B and all TOE percentages
remain unchanged.
