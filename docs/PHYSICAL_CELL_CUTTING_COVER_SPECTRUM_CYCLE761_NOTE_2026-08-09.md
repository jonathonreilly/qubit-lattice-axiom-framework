# Exact spectrum, relation-product witnesses, and row-space character overlaps for the finite eight-piece Gram

Date: 2026-08-09

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem

Constitutional effect: none. This note changes no axiom, primitive, registry,
policy, audit verdict, or effective status.

Runner and cache:

- [finite rebuild-and-certificate runner](../scripts/physical_cell_cutting_cover_spectrum_cycle761_2026_08_09.py)
- [content-pinned runner cache](../logs/runner-cache/physical_cell_cutting_cover_spectrum_cycle761_2026_08_09.txt)

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "submit the exact bounded row to independent audit; downstream consumers, if identified later, must carry this finite protocol unchanged"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact integer certificates for one explicitly stipulated finite combinatorial protocol, with exhaustive construction, factor-kernel multiplicities, and fixed mutation controls"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

For the finite object reconstructed from the stipulated protocol below, prove
the complete spectrum and degree-19 minimal polynomial of the 192 by 192
eight-set Gram matrix, exhibit the measured sharing-relation product
variations, and compute the invariant row-space character inner products for
the cutting and eight-set incidence tables under the 384 signed-coordinate
relabellings.

## Imports and stipulated conditions

### Load-bearing scientific imports

None. The runner reads no repository data file, observation, fitted value,
literature table, or earlier-cycle artifact. Python, NumPy, and the standard
library are software dependencies only.

### Finite protocol conditions

These conditions define the theorem's domain. They are supplied by the runner,
rather than derived from the framework axioms.

| supplied condition | role | provenance | open bridge status |
|---|---|---|---|
| the sixteen vertices `{0,1}^4` | finite corner set | in-file definition | any physical cell interpretation is outside this target |
| five-corner simplices of normalized determinant magnitude one | piece class | exhaustive in-file enumeration | any identification with physical assembly pieces is outside this target |
| the all-four-coordinate L1 pair cost and its minimum over those pieces | piece filter | in-file definition and exhaustive minimum | any physical cost interpretation is outside this target |
| the integer-weight sample family generated from `OFF = [0,1,7,49,343]` | exact-cover search device | in-file construction | no external provenance is claimed |
| all signed permutations of four coordinates | computational relabelling group | exhaustive in-file construction | any identification with a complete physical symmetry is outside this target |

The current framework memo `docs/MINIMAL_AXIOMS_2026-06-29.md` is contextual
only. Its Lattice axiom supplies neither this four-dimensional finite protocol
nor the stipulated piece, cost, sample, or relabelling choices, so it is not a
claim dependency.

## Proof-obligation graph

1. **Finite object and cutting census — proved here.** The runner enumerates
   all determinant-one five-corner pieces, selects the exact cost floor, and
   exhausts the sample-cover search. A finite separating-direction sweep over
   `{-4,...,4}^4` proves pairwise interior disjointness for every enumerated
   24-piece cover. Since every piece has normalized volume one and the box has
   normalized volume 24, the 15,800 covers are genuine cuttings.
2. **Incidence identities — proved here.** The cutting-by-piece table has
   15,800 rows and 192 used pieces, with row degree 24 and column degree 1,975.
   The 192 eight-piece rows form a zero-one table with row and column degree 8,
   and each meets each cutting once.
3. **Spectral factor list — proved here.** Exact factor-kernel nullities,
   irreducibility, pairwise coprimality, and an exact annihilator account for
   all 192 eigenvalues.
4. **Per-root multiplicities — proved here.** The integral symmetric Gram has
   characteristic polynomial in `Z[x]`. Roots conjugate over `Q` therefore
   have equal algebraic multiplicity, while real symmetry makes the matrix
   diagonalizable. Hence an irreducible factor's kernel has dimension equal to
   its degree times the common multiplicity of each of its roots.
5. **Trace and minimal-polynomial checks — proved here.** The root sums give a
   trace checksum, and the 19 distinct roots make the squarefree annihilator
   the degree-19 minimal polynomial.
6. **Sharing-relation witnesses — proved here.** Direct products of the five
   relation matrices are evaluated entrywise, and variation inside each
   sharing class is measured without an interpretive extension.
7. **Character overlaps — proved here.** Exact scaled orthogonal projectors are
   checked for symmetry, idempotence, row-space fixation, rank, trace, and
   invariance under every relabelling. Their traces against the permutations
   are therefore characters, so ordinary finite-group character inner
   products apply.

Every lemma used by the exact target is proved in the paired runner or by the
elementary algebra stated above. The strongest missing lemma for any broader
use would be a bridge from this stipulated finite protocol to a claimed
physical carrier or to a general explanation of the ranks; that bridge is not
part of this target.

## The rebuilt finite object

The runner finds 15,800 cuttings using 192 pieces. Every cutting contains 24
pieces and every used piece lies in 1,975 cuttings. The separating-direction
certificate verifies pairwise interior disjointness for every sample cover.

It then exhausts sets of eight pieces in which no pair shares a cutting. There
are 192 such sets. Their incidence matrix `M` is 192 by 192, every row and
column has eight ones, and the cutting incidence matrix times `M^T` is the
all-ones matrix. Thus each eight-piece set meets each cutting exactly once, and
the double counts read `192 = 24 * 8` and `15,800 = 8 * 1,975`.

The Gram matrix is

```text
S = M M^T.
```

It is an integral symmetric 192 by 192 matrix with diagonal 8, row sum 64,
and trace 1,536.

## Exact spectrum and minimal polynomial

The ten integer eigenvalues and their multiplicities are:

```text
0:87, 2:8, 4:8, 8:3, 10:8, 12:6, 16:2, 20:10, 24:3, 64:1.
```

They account for 136 eigenvalues. The remaining 56 are roots of these monic
irreducible factors, each root repeated at the stated common multiplicity:

```text
x^2 - 20x + 80                 multiplicity 6
x^2 - 44x + 400                multiplicity 6
x^2 - 52x + 320                multiplicity 4
x^3 - 44x^2 + 516x - 1280      multiplicity 8
```

The quadratic discriminants are 80, 336, and 1,424, all nonsquares. The monic
cubic has no root among the signed divisors of 1,280, so the rational-root
test makes it irreducible over `Q`; its nonzero discriminant 8,640,512 also
certifies distinct roots. Together with the ten distinct linear factors, these
are fourteen pairwise coprime irreducible factors and 19 distinct roots.

The runner measures each factor-kernel nullity by exact fraction-free integer
elimination. The linear-factor nullities are the ten multiplicities above; the
quadratic nullities are 12, 12, and 8; and the cubic nullity is 24. By the
conjugacy lemma in the proof-obligation graph, division by factor degree gives
the per-root multiplicities. All fourteen nullities add to 192.

The product of the fourteen factors, evaluated at `S` in exact integer
arithmetic, is the zero matrix. It is squarefree and has 19 roots, while the
real symmetric matrix has all 19 as eigenvalues. Its degree-19 product is
therefore the minimal polynomial of `S`.

The sum-of-roots checksum, using those nullity-derived multiplicities, splits
the trace into

```text
592 + 592 + 352 = 1536.
```

This is a consistency checksum on the multiplicity certificate, rather than a
separate measurement of the multiplicities.

## Sharing-relation product witnesses

For two distinct eight-piece sets, the number of shared pieces takes the four
values 0, 1, 2, and 4. Every row has the same profile:

```text
0:157, 1:20, 2:10, 4:4.
```

Let `R_share=v` be the zero-one matrix of the off-diagonal relation “shares
exactly `v` pieces.” Then the runner checks the exact identity

```text
S = 8 I + R_share=1 + 2 R_share=2 + 4 R_share=4.
```

It directly evaluates all 25 ordered products formed from `I` and the four
sharing-relation matrices. Sixteen ordered products take more than one value
inside at least one fixed sharing class; the first in enumeration order is the
square of the zero-sharing relation. These are explicit finite product-
variation witnesses, with no conclusion attached to untested larger matrix
families.

## Row-space character overlaps

The 384 signed-coordinate maps are checked to be distinct permutations, closed
under composition, and transitive on the 192 pieces. The piece permutation
character has self-inner-product 104.

For each incidence table, the runner constructs an exact integer multiple of
the orthogonal projector onto its row space. It verifies the projector
identities and checks exact conjugation invariance under all 384 maps. Thus the
projector trace against each permutation is the character of the invariant row
space, and subtracting it from the piece character gives the character of the
orthogonal complement.

The character inner products are:

| table row space | rank | row space with itself | complement with itself | cross | row space with constants | complement with constants |
|---|---:|---:|---:|---:|---:|---:|
| cutting incidence | 88 | 29 | 33 | 21 | 1 | 0 |
| eight-set incidence | 105 | 34 | 28 | 21 | 1 | 0 |

The sum checks are `29 + 33 + 2*21 = 104` and
`34 + 28 + 2*21 = 104`. Character orthogonality expresses the cross value as
the sum of products of irreducible multiplicities. The positive value 21
therefore certifies that at least one irreducible type occurs in both the row
space and its complement for each table.

## Runner gates and mutations

The runner emits 24 descriptive gates:

- object census; eight-set table; piece frames; exact-cover double count;
- rebuild mutation control; Gram invariants;
- integer, quadratic, and cubic spectrum; spectrum completeness;
- annihilating polynomial; irreducible factors; trace checksum;
- spectrum mutation control; sharing product witnesses; sharing mutation control;
- four-cube relabelling action; group-action mutation control;
- cutting characters; eight-set characters; character decomposition control;
- character mutation control; exact character division; resource bounds.

The fixed mutations exercise every load-bearing family:

- a table-bit flip and a piece replacement break the incidence and cutting
  certificates;
- changing the cubic constant makes the annihilator nonzero, while changing
  the multiplicity at eigenvalue 20 makes the kernel dimensions total 191;
- changing one shared-piece entry breaks the sharing identity;
- duplicating one image in a proposed relabelling breaks the permutation gate;
- a coordinate line supplies a valid rank-one projector but fails exact
  invariance, so the character gate rejects it.

Measured result: `TOTAL: PASS=24 FAIL=0`; stdout length and the elapsed-time and
peak-memory bounds are emitted by the cache-bound run.

## Review record

Iteration 1 used the configured independent Sol reviewer. It returned
`FIX_THEN_PROCEED`: the exact finite spectrum and character numbers survived
independent reconstruction, while the original general claims about structural
and symmetry routes exceeded the evidence and failed the N1-N8 gate. This
revision removes those route conclusions from every landing surface, preserves
the bounded finite theorem, adds the missing conjugacy and invariance lemmas,
declares the finite conditions and canonical metadata, replaces bare numbered
gate labels, adds family-specific mutations, fixes platform-aware peak-memory
normalization, and declares the cache timeout.

Review-time corroboration, not a load-bearing landing artifact, used direct
SymPy characteristic-polynomial factorization, NumPy diagonalization, direct
relation-product multiplication, and floating orthogonal projectors. It
reproduced the 19 spectral targets within `5.684e-14`, trace 1,536, all stated
character inner products, and exact projector invariance under all 384 maps.

## Boundary

The theorem domain is exactly the one finite object defined by the five
protocol conditions above. The spectrum includes its zero eigenspace and all
repeated algebraic conjugates; the action checks every one of the 384 specified
maps. Other piece classes, cost functions, sample constructions, dimensions,
cells, relabelling groups, physical interpretations, and general explanations
of ranks lie outside the claim. The source note proposes bounded status only;
independent audit owns any effective retained classification.

## No-Go Discipline applicability

The landed scope consists exclusively of positive finite identities, exact
character overlaps, and explicit product-variation witnesses. Route analysis
is reserved for a separate artifact. N1-N8 and the five-resolution execution
certificate are therefore not applicable to this narrowed artifact.
