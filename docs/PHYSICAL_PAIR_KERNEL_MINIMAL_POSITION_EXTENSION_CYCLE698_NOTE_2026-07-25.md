# The minimal position-carrying extension of the readout clause is a pair kernel, and covariance leaves one constant — Cycle 698

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted, and no reading of the axiom text is ratified.

Runner: `scripts/physical_pair_kernel_minimal_position_extension_cycle698_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0; exact integer and `Fraction` arithmetic in every
decisive row, with a negative control in each).

## The question

Cycle 693 showed that content determinacy plus finite additivity force every
scalar readout into the singleton-weight form. Cycle 697 showed that such a
readout is position-blind and never dimensionless, and named the missing
objects. Both are negative. This cycle asks the positive question the audit
verdicts actually need answered:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."
> — audit verdict on `ac_reta_hclass_hunit_readout_derivation_obligation`

What is the *smallest* structure that carries position, and what does the
framework's own covariance already say about its shape? This note classifies
that structure. It does not adopt it.

## M1 — read strictly, the additivity clause forbids interaction

Records occupy distinct sites, since a site never carries more than one record.
If "pairwise-disjoint records" therefore covers every pair of distinct records,
additivity applies to *every* splitting of *every* collection.

On a four-record fixture the runner solves the resulting linear system exactly:
the space of additive functionals is exactly 4-dimensional — one weight per
record — and a concrete one-body functional lies in it. Extending the unknowns
to the full 10-parameter two-body cluster space
`F(S) = sum_i w_i + sum_{i<j} K_ij` and re-imposing additivity returns the same
4-dimensional one-body space, with **every pair coefficient exactly zero**. The
unconstrained space has all 10 dimensions, which is the negative control.

So no interaction energy is a scalar readout, at any order above one. This is
the exact reason the audit verdicts can say Record additivity does not
determine a source action: a source action is a two-body object, and the clause
as read admits none.

### The reading is load-bearing, and this note rules on nothing

There is a second available reading in which "pairwise-disjoint" means
*separated* rather than merely *distinct*. The two readings are not
physically equivalent, and M3 below shows exactly where they part company: the
adjacent-pair readout is additive for well-separated collections and fails only
on contact. Under the strict reading the framework has no interactions; under
the separated reading a nearest-neighbor interaction is compatible with the
clause.

This note takes no position on which reading is intended. It records that the
choice has a physical consequence, that the consequence is exactly one contact
term, and that the runner exhibits it.

## M2 — covariance classifies the pair kernel, and range 1 leaves one constant

The minimal position-carrying extension adds a two-body term
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

The minimal covariant local two-body readout is therefore one constant times
the number of adjacent record pairs.

## M3 — the pair readout is additive at separation and fails exactly on contact

For `A = {(0,0,0), (1,0,0)}` the runner computes exactly:

| collections | pairs in union | sum of pairs | additive? |
|---|---|---|---|
| `A` with `B = {(5,0,0), (6,0,0)}` | 2 | 2 | yes |
| `A` with `B = {(2,0,0), (3,0,0)}` | 3 | 2 | no, excess 1 |

The two collections occupy disjoint sites in both rows; only adjacency differs,
and the excess is exactly the number of cross bonds. This is the precise sense
in which a two-body readout lives outside the Record class without being
pathological.

## M4 — the field is the marginal readout cost of a test record

The pair kernel supplies the site-anchored value cycle 697 showed was missing,
and it supplies it in one specific shape. The runner verifies exactly that for
every tested site

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

That is the same two-dimensional family that
[cycle 697](PHYSICAL_READOUT_POSITION_SCALE_LIMITS_AND_FORCED_LOCAL_LAW_CYCLE697_NOTE_2026-07-25.md)
derived from the law side, by an independent argument that never mentions a
source. Two different questions — "what operator can a covariant local law
use?" and "what field can a covariant local pair kernel induce?" — land on the
same two constants. The agreement is a consistency check on both, not a new
premise.

## What this does not do

- It does not adopt the pair kernel, a source action, a carrier, a dynamics, a
  Hamiltonian, a probability rule, or a formation rule. The pair kernel is
  exhibited as the classified *shape* of the missing object.
- It does not rule on the reading of "pairwise-disjoint". It records that the
  reading has a consequence and what that consequence is.
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
| reference normalization | untouched by this cycle; still the open object cycle 697 named. |
| carrier | untouched. |

## Scope for independent review

The classification in M2 is computed at the displacement level and is
box-independent; the `5^3` periodic box appears only in M5's operator identity,
where the comparison is entrywise and exact. M1's fixture has four records,
which is the smallest size carrying a nontrivial two-body space; the conclusion
that additivity kills every pair coefficient is a linear-algebra fact at that
size and is stated as such rather than as an asymptotic claim. Every decisive
equality is exact integer or `Fraction` arithmetic; there is no floating-point
comparison and no fit. Three-body and higher terms, content-dependent kernels,
infinite collections, and any physical interpretation of the constant are
outside scope.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md)
is cited for the singleton-weight factorization it established, and
[cycle 697](PHYSICAL_READOUT_POSITION_SCALE_LIMITS_AND_FORCED_LOCAL_LAW_CYCLE697_NOTE_2026-07-25.md)
for the position and scale limits and the law-side family that M5 compares
against; neither is load-bearing for this runner's arithmetic.

Closest standard-math analogue, cited so the distinction is explicit:
[Cubic-orbit Reynolds projector](CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md)
establishes the Reynolds-operator identity for the `D_4` stabilizer of a
*selected* forward direction acting on a forward-cone neighbour set. That the
invariants of a finite group action are the functions on its orbits is the
standard fact both notes use. It is not the result here: this note fixes no
preferred direction, uses the full proper cubic group about each site, and its
content is which axiom clause licenses each hypothesis and what the resulting
parameter count is for a two-body readout — one constant at range 1.
