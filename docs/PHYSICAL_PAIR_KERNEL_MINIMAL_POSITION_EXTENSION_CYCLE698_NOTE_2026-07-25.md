# The minimal relational position-carrying extension is a pair kernel, and conditional covariance leaves one constant — Cycle 698

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted, and no reading of the axiom text is ratified.

Runner: `scripts/physical_pair_kernel_minimal_position_extension_cycle698_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0; exact integer and `Fraction` arithmetic in every
decisive row).

## The question

Cycle 693 showed that content determinacy plus finite additivity force every
scalar readout into the singleton-weight form. An earlier block in this
campaign added that such a readout is blind to record position and that an
additive readout cannot also be duplication-invariant; that block was rejected
as submitted and only its abstract kernel classification was salvaged and
landed, as
[Proper-cubic finite-support linear-kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md).
Nothing below relies on the rejected parts.

One wording correction inherited from that review, made here so it is not
repeated: **"cannot be duplication-invariant" is not "cannot be
dimensionless."** The record count `I(S) = |S|` is a nonzero, finitely
additive, dimensionless pure number, and it doubles under duplication. The
correct statement is about intensive (degree-zero) quantities only. This note
uses the narrow form throughout.

This cycle asks the positive question the audit verdicts actually need
answered:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."
> — audit verdict on `ac_reta_hclass_hunit_readout_derivation_obligation`

What is the *smallest relational* structure that carries position, and what
does proper-cubic covariance say about its shape under a named downstream-law
class? This note classifies that conditional structure. It does not adopt it.

## M1 — read strictly, additivity forbids irreducible multi-record readout terms

Records occupy distinct sites, since a site never carries more than one record.
If "pairwise-disjoint records" therefore covers every pair of distinct records,
additivity applies to *every* splitting of *every* collection.

For any finite collection `S`, the strict reading gives the disjoint
decomposition `S = disjoint-union_{r in S} {r}`. Iterating the axiom's
additivity sentence therefore gives

```text
I(S) = sum_{r in S} I({r}),
```

with the empty case supplied by `I(empty)=0`. Thus every Möbius/cluster
coefficient supported on two or more records is zero. This uses the Record text
alone; none of M2's conditions 1–4 enters.

This arbitrary-finite singleton factorization is already proved on `main` in
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md).
M1 is its interaction-term corollary and scoped application, not a new
additivity theorem.

On a four-record fixture the runner reproduces the result by solving the
resulting linear system exactly:
the space of additive functionals is exactly 4-dimensional — one weight per
record — and a concrete one-body functional lies in it. Extending the unknowns
to the full 10-parameter two-body cluster space
`F(S) = sum_i w_i + sum_{i<j} K_ij` and re-imposing additivity returns the same
4-dimensional one-body space, with **every pair coefficient exactly zero**. A
concrete pair-only term has a nonzero additivity defect, which is the negative
control.

So, under this reading, the scalar Record readout itself contains no
irreducible multi-record interaction term. This does **not** exclude
interactions in a separate action or dynamics, exclude one-body readout values
whose record contents carry environment-correlated information, or say that
every possible source action is two-body. It explains only why Record
additivity does not by itself supply an interacting pair term in the scalar
readout.

### The reading is load-bearing, and this note rules on nothing

There is a second available reading in which "pairwise-disjoint" means
*separated* rather than merely *distinct*. The two readings are not
physically equivalent, and M3 below shows exactly where they part company: the
adjacent-pair readout is additive for well-separated collections and fails only
on contact. Under the strict reading the scalar readout has no irreducible
multi-record term; under the separated reading a nearest-neighbor pair term is
compatible with the clause. Neither reading decides whether a separate
interaction law or dynamics exists.

This note takes no position on which reading is intended. It records that the
choice has a physical consequence, that the consequence is exactly one contact
term, and that the runner exhibits it.

## M2 — covariance classifies the pair kernel, and range 1 leaves one constant

The minimal relational extension that preserves translation covariance and
introduces displacement dependence adds a two-body term
`K(s(r) - s(r'), c(r), c(r'))`. Translation covariance makes it depend on the
displacement alone. Proper cubic covariance about each site makes it a function
on proper-octahedral orbits of the displacement.

At nearest-neighbor range the proper rotations act transitively on the six face
displacements, so the runner's exact solve returns kernel dimension **1**.
Displacement reversal is already inside the proper rotation group — the 180°
rotation about `z` sends `e_1` to `-e_1` — so no separate symmetry assumption is
needed to make the kernel two-sided; the runner checks that containment
explicitly. Dropping the rotations leaves all six free, which is the negative
control.

Within the named class below, the range-1 covariant local two-body readout is
therefore one constant times the number of adjacent record pairs. This is the
face-shell specialization of the already-landed general kernel
classification, not a new orbit-count theorem.

### The hypotheses of M2 are supplied, not derived

A prior review of an earlier block in this campaign found that Record
additivity was being asked to carry more than it does. The correction applies
here and is stated up front. M2 assumes, as explicit conditions:

1. a rational scalar/module structure for the kernel values — cycle 693
   supplies only an arbitrary additive scalar group `G`;
2. that the two-body term enters **linearly**, as a sum over unordered record
   pairs of a kernel value;
3. **finite support** for the kernel;
4. **covariance** of the kernel under translations and proper cubic rotations.

The Lattice axiom supplies `Z^3`, its translations, and the proper cubic
rotations. It does **not** supply conditions 1–4 for a downstream physical law,
and Record additivity does not make a law linear. These are the named boundary
of M2, exactly as they are the named boundary of the landed
[proper-cubic kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md).
What M1 establishes from the axiom text alone is the *negative* half — that a
strictly additive readout has no pair term at all — and that half needs none of
1–4.

The orbit-count step itself is standard and is not claimed as new here; see
`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md`, which
proves that invariant functions are constant on orbit classes and that the
invariant dimension equals the orbit count.

## M3 — the pair readout is additive at separation and fails exactly on contact

For `A = {(0,0,0), (1,0,0)}` the runner computes exactly:

| collections | pairs in union | sum of pairs | additive? |
|---|---|---|---|
| `A` with `B = {(5,0,0), (6,0,0)}` | 2 | 2 | yes |
| `A` with `B = {(2,0,0), (3,0,0)}` | 3 | 2 | no, excess 1 |

The two collections occupy disjoint sites in both rows; only adjacency differs.
In general every adjacent pair in `A union B` is either internal to `A`,
internal to `B`, or a cross bond, so

```text
pairs(A union B) - pairs(A) - pairs(B) = cross_bonds(A,B).
```

The runner compares the two sides directly and exhausts every ordered pair of
disjoint subsets of a five-site line, including empty subsets. This is the
precise sense in which a two-body readout lives outside the strict Record class
without being pathological.

## M4 — the field is the marginal readout cost of a test record

The pair kernel supplies a site-anchored value — the thing a position-blind
readout can never supply — and it supplies it in one specific shape. The runner
verifies exactly that for every tested site

```text
pairs(S + {x}) - pairs(S) = number of occupied neighbors of x
```

so the "field at `x`" is the **marginal** readout cost of placing a test record
at `x`. On the fixture `S = {(0,0,0), (1,0,0), (0,1,0), (3,3,3)}` the value is
1 at `(2,0,0)`, 1 at `(0,0,1)`, and 0 at `(9,9,9)`; at occupied records it is
2, 1, 1, 0. It varies across sites, which is what a position-blind readout can
never do.

Two consequences worth stating plainly:

- A field value at an **empty** site exists only through the test record. There
  is no reading of an empty site in this construction, consistent with "only
  records are readable".
- The construction is *relational*, so it privileges no site. Position enters
  through record-to-record displacement, never through an absolute coordinate.

## M5 — the source route and the law route give the same family

The field operator induced by the range-1 pair kernel is, entrywise and exactly
on a periodic `5^3` box, `6*I + Delta`. An exact solve over `Q` confirms it lies
in `span{I, Delta}` and that a single-axis pair kernel does not.

That is the same two-dimensional family the landed
[proper-cubic kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
gives at range 1, by an argument that never mentions a source. Two different
questions — "what operator can a covariant local law use?" and "what field can
a covariant local pair kernel induce?" — land on the same two constants. The agreement is a consistency check on both, not a new
premise or a new operator-classification theorem. The runner checks the matrix
identity entrywise and, through a separate nonconstant probe-vector action,
checks the adjacency and Laplacian actions without relying only on the shared
matrix constructor.

## What this does not do

- It does not adopt the pair kernel, a source action, a carrier, a dynamics, a
  Hamiltonian, a probability rule, or a formation rule. The pair kernel is
  exhibited as the classified *shape* of the missing object.
- It does not rule on the reading of "pairwise-disjoint". It records that the
  reading has a consequence for irreducible multi-record terms in the scalar
  readout and what that consequence is.
- It does not fix the one remaining constant, its sign, or its units, and it
  does not claim the physical range is nearest-neighbor. Range 1 is a named
  condition; at larger range the kernel has one constant per octahedral orbit.
- It does not repair any gravity row or any AC obligation, and changes no
  status.
- It awards itself no N1–N8 verdict. M1's strict-reading consequence is a
  negative result; that verdict is reviewer-owned.

## Named residuals after this cycle

| residual | state after 698 |
|---|---|
| site-anchored readout | **shape derived**: the marginal cost of a test record. Its existence still requires the two-body extension, which the strict reading of the additivity clause excludes. |
| source action | **shape classified**: a two-body kernel on octahedral orbits; one constant at range 1. Value, sign, and range remain open. |
| reference normalization | untouched by this cycle; still open. A dimensionless *intensive* target needs a selected reference; a dimensionless extensive count does not. |
| carrier | untouched. |

## Scope for independent review

The classification in M2 is computed at the displacement level and is
box-independent; the `5^3` periodic box appears only in M5's operator identity,
where the comparison is entrywise and exact. M1's fixture has four records,
which is the smallest size carrying a nontrivial two-body space; the conclusion
that additivity kills every irreducible multi-record term is carried by the
arbitrary-finite singleton proof above, while the runner reproduces its
two-body specialization on that fixture. Every decisive
equality is exact integer or `Fraction` arithmetic; there is no floating-point
comparison and no fit. Explicit three-body and higher kernel classifications,
content-dependent kernels, infinite collections, and any physical
interpretation of the constant are outside scope.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md)
is prior art for the arbitrary-finite singleton-weight factorization used in
M1, and
[Proper-cubic finite-support linear-kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
for the range-1 family that M5 compares against; neither is load-bearing for
this runner's arithmetic.

`FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md` records that
the framework permits both intensive local densities and extensive quasi-local
sums. It is named here as the cross-cycle surface a prior review found missing
from an earlier block's scan; it is consistent with M1-M5 and is not
load-bearing.

Closest standard-math analogue, cited so the distinction is explicit:
[Cubic-orbit Reynolds projector](CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md)
establishes the Reynolds-operator identity for the `D_4` stabilizer of a
*selected* forward direction acting on a forward-cone neighbour set. That the
invariants of a finite group action are the functions on its orbits is the
standard fact both notes use. It is not the result here: this note fixes no
preferred direction, uses the full proper cubic group about each site, and its
content is which axiom clause licenses each hypothesis and what the resulting
parameter count is for a two-body readout — one constant at range 1.
