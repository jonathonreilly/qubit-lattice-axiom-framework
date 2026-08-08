# The readout clause forbids fields and pure numbers, and forces the local law to the Laplacian ray — Cycle 697

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

Runner: `scripts/physical_readout_position_scale_limits_and_forced_local_law_cycle697_2026_07_25.py`
(11 PASS / 0 FAIL, exit 0; exact integer and `Fraction` arithmetic in every
decisive row, with a negative control in each).

## The question

Four gravity rows and the two AC derivation obligations are
`audited_conditional` for what reads like one reason. Every quotation in this
section is audit-lane verdict text about those rows, not text from the notes
themselves; the notes are cited only for navigation.

The five-judge panel verdict on the
[Gravity law cleanup](GRAVITY_LAW_CLEANUP_NOTE.md) row recorded, with 5/5
matching tuples:

> "the minimal-axiom authority expressly withholds dynamics, weights,
> source/action, and physical-observable bridges, while the runner stipulates
> each of those ingredients."

The re-audit instruction on the
[Gate B far field](GATE_B_FARFIELD_NOTE.md) row asks to

> "cite or derive retained connections from the accepted framework premises to
> the growth rule, source field, propagation/action rule, and TOWARD/F~M
> physical readout before seeking a non-conditional physics verdict."

and the corresponding instruction on the Gravity law cleanup row asks to
"supply retained derivations of the field, propagation/action, geometry, and
detector-centroid prescriptions from the framework baseline".

The verdict on the AC eta-readout obligation
([AC R-eta h-class h-unit readout](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md))
states the obstruction as:

> "Record additivity and the approved primitives do not themselves determine
> the carrier, source action, or dimensionless readout normalization."

This cycle asks what the readout clause of [Record](MINIMAL_AXIOMS_2026-06-29.md)
plus the covariance content of Lattice actually settle, and it separates the
three named residuals. It does not build the carrier, the source action, or a
site-anchored readout.

## What the axioms supply here

From [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md):

```text
Lattice   Physical sites are the points of Z^3, with nearest-neighbor
          adjacency, standard translations, and proper cubic rotations about
          each site. No site is privileged.
Record    Only records are readable. A readout value is determined by record
          content alone. For any finite collection of pairwise-disjoint
          records, scalar readout I is additive, with I(empty)=0.
```

Cycle 693 ([Record readout carrier three-way split](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md))
already showed that these clauses force each readout into the singleton-weight
form `I(S) = sum_{r in S} f(c(r))` once a scalar codomain `G` and a realized
content set are supplied, and that they do not supply a finite alphabet, a
complex codomain, or an algebra product. This cycle adds what that form implies
about **position** and about **scale**, and adds a positive classification of
the laws such a source can enter.

## L1 — the local record-sourced law is forced to two constants, and to one ray

Let `L` act on `G`-valued site functions by a displacement kernel,
`(Lf)(x) = sum_v k(v) f(x+v)`. Additivity over disjoint records makes the
action of the law on a record-sourced quantity linear in the configuration, so
a kernel is the general form; translation covariance is the statement that `k`
does not depend on `x`; and proper-cubic covariance about each site is the
statement that `k(Rv) = k(v)` for every proper cubic rotation `R`.

**Theorem L1.** The space of such kernels supported in a rotation-closed set
`P` has dimension exactly the number of proper-octahedral orbits in `P`.

The runner solves the invariance system exactly over `Q` and matches the
nullity against an independent orbit count at six radii:

| support ball `|v|^2 <=` | points | orbits | invariant dimension |
|---|---|---|---|
| 1 | 7 | 2 | 2 |
| 2 | 19 | 3 | 3 |
| 3 | 27 | 4 | 4 |
| 4 | 33 | 5 | 5 |
| 5 | 57 | 6 | 6 |
| 6 | 81 | 7 | 7 |

**Corollary L1a (range 1).** At nearest-neighbor range the dimension is 2,
because the proper cubic rotations act transitively on the six face
displacements. The family is exactly

```text
L = A * I + B * Delta,     Delta = sum_{|v|=1} T_v - 6 I
```

with `A = k(0) + 6 k(e)` and `B = k(e)`. The runner confirms on a periodic
`5^3` box that each basis element of the exactly solved invariant space is an
exact rational combination of `I` and `Delta` — the two basis elements come out
as `(A,B) = (1,0)` and `(6,1)` — that `I` and `Delta` are independent, and that
the local but anisotropic forward difference `T_{e1} - I` is **not** in the
span. Dropping the rotations raises the dimension from 2 to 7, so the
covariance clause is load-bearing for the count, not decorative.

**Corollary L1b (the Laplacian ray).** `L` annihilates the constant field iff
`A = 0` iff `L` is a multiple of `Delta`. Adding that one condition to the
range-1 invariance system leaves exactly one dimension, and the runner confirms
the Laplacian spans it. At range `sqrt(2)` the same condition leaves **two**
dimensions, so the collapse to a single ray is specific to nearest-neighbor
range.

What L1 buys the gravity rows is narrow and exact: the propagation rule is not
a free stipulation. Once the source enters additively, the lattice is the
supplied one, and the range is nearest-neighbor, the operator is pinned to a
two-parameter family, and one further named condition pins it to `Delta` up to
overall scale. What remains stipulated is the range-1 restriction, the one
remaining constant (equivalently the ratio `A/B`), the overall scale, and — by
L2 below — the field itself.

## L2 — a Record readout is position-blind, so it cannot be a field

**Theorem L2.** Suppose a record-sourced quantity is required to be, at every
site `x`, a readout in the axiom's sense: determined by record content alone.
Then its displacement kernel is constant, and the resulting field takes the
same value at every site.

*Proof.* The singleton value at `x` of a record `r` is `k(x - s(r))`. "Content
alone" forbids dependence on `s(r)`, so `k(x-s) = k(x-s')` for all sites
`s, s'`, hence `k` is constant on displacements. Additivity then gives
`Phi_x(S) = |S| * k`, independent of `x`. []

The runner formalizes the hypothesis as row-equality of the induced circulant
operator, which is equivalent to `k` being constant, solves the resulting
system exactly on a `3^3` periodic box, and finds nullity exactly 1 — spanned
by the constant kernel. The negative control is that `Delta` applied to a point
source takes three distinct values, so the Laplacian is covariant but not
position-blind. The proof above, not the finite box, carries the universal
statement.

**Consequence.** A nonconstant record-sourced field is never a family of Record
readouts. Exactly one further structure is needed and it is nameable: a
**site-anchored readout**, i.e. a readout relativized to a site index rather
than determined by content alone. This is why every gravity runner in the lane
stipulates its observable: on the current axiom surface there is nothing else
to do. The stipulation is forced, not a defect of those particular runners.

## L3 — no nonzero Record readout is dimensionless

Call a quantity **dimensionless** if it is unchanged when the record collection
is duplicated by a distant lattice translate. This is the operational content
of "intensive": doubling the system does not change it.

**Theorem L3.** If a Record readout is dimensionless, it is zero.

*Proof.* Let `S'` be the image of `S` under a translation `t`. Translations are
lattice automorphisms and the admissibility rule is translation-covariant, so
`S'` is a configuration with the same content multiset as `S`. Choose `|t|`
larger than the support diameter of `S` plus one: then `S` and `S'` are
disjoint and mutually non-adjacent, so every occupied site keeps exactly the
nearest-neighbor occupancy pattern it had in its own copy, and any fixed
nearest-neighbor admissibility rule that admitted `S` admits `S union S'`.
Additivity gives `I(S union S') = 2 I(S)`; dimensionlessness gives
`I(S union S') = I(S)`; hence `I(S) = 0`. []

The runner checks the combinatorial legality step directly. The preserved
object is the full nearest-neighbor **content** condition, not merely
occupancy, because the Admissibility rule reads conditions and not a bit: for
a four-record fixture with three distinct contents translated beyond its
diameter, the copy is disjoint, non-adjacent, content-multiset preserving, and
every occupied site's neighbor content map is unchanged, while a unit translate
is the negative control that does change one. The
additive-and-duplication-invariant system is then solved exactly, giving
dimension 0.

**The conclusion does not depend on the reading of "dimensionless."** A second,
independent reading is invariance under rescaling the scalar unit,
`I_h -> lambda * I_h`. Imposing that for two distinct nonzero `lambda` on a
spanning family again leaves only `h = 0`; the vacuous `lambda = 1` condition
is the negative control and leaves the full space. Both readings give L3.

### The escape, and why the choice is load-bearing

The only remaining shape is a ratio of two readouts. Once a unit is supplied,
the record-count readout is the obvious candidate reference, and the runner
confirms the arithmetic: the count readout is itself extensive (it doubles),
and the quotient by it is duplication-invariant. This is a genuine
partial-closure path and it is named here rather than dismissed — supplying a
counting convention, not a new axiom, is what would discharge the residual.

But the choice is not a convention that washes out. On the same fixture, the
same numerator read against the count reference gives `6/35`, and against
another admissible reference gives `3/28`. Different admissible references
give different dimensionless values, so a normalization derivation has to
select the reference, not merely observe that some reference exists.

**Consequence.** A dimensionless target value is never the value of a single
Record readout. The only remaining shape is a **ratio of two readouts**, and
choosing the reference readout and reference collection is precisely the
"dimensionless readout normalization" the AC eta obligation names as missing.
The runner exhibits the ratio's behaviour exactly: `I_f/I_g` is
duplication-invariant, and it is not additive
(`ratio(S1 + S2) = 11/28` against `ratio(S1) + ratio(S2) = 11/14`), so no ratio
is itself a Record readout.

This also constrains the shape of any future normalization derivation: it must
deliver a pair — a numerator readout and a reference — because no single
additive readout can carry a pure number. Cycle 692
([hypercharge alpha scale freedom](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md))
found by enumeration that no tested mechanism fixes `alpha = 1/3` on the
two-block surface, and explicitly disclaimed classifying every dimensionless
construction. L3 is the general structural statement that cycle 692's
enumeration was probing: the obstruction is not the particular surface.

## L4 — the two limits are distinct deficiencies of one clause

The gravity obligation and the AC eta obligation are commonly read as naming
the same missing object. On the readout side they do not.

- Gravity needs L2 repaired: a **position-dependent** readout. Repairing it
  does not make anything dimensionless — a position-blind readout and a
  site-anchored one both double under duplication.
- The AC eta obligation needs L3 repaired: an **intensive** readout. Repairing
  it does not produce a field — a ratio of readouts is built from
  position-blind ingredients and remains position-blind.

The runner checks both non-implications exactly. So the readout clause has two
independent deficiencies, and they need two supplied objects, not one. The two
obligations do share the third named object — the source action — which neither
L1 nor L2 nor L3 supplies.

## What this does not do

- It does not repair the four gravity rows. Their runners operate on generated
  DAGs with a stipulated growth rule, not on `Z^3` record configurations, so L1
  does not apply to them as written. L1 states what an axiom-native replacement
  is forced to look like; it does not certify any existing runner.
- It does not supply the site-anchored readout, the reference normalization, the
  carrier, the source action, a dynamics, a Hamiltonian, a probability rule, a
  measurement rule, or a formation rule.
- It does not derive that the physical law is at nearest-neighbor range.
  Range-1 is a named condition; L1 gives the exact dimension at every other
  range, and L1b is false at range `sqrt(2)`.
- It does not derive the offset-insensitivity condition of L1b. That condition
  is stated, not supplied; by L2 the field is not an axiom object, so it carries
  no axiom-privileged zero, but that observation is a motivation and not a
  derivation.
- It does not change the status of any lane, row, or obligation, and it awards
  no N1–N8 verdict to its own negative content. L2 and L3 are negative results;
  that verdict is reviewer-owned.

## Named residuals after this cycle

| residual | what would discharge it | which rows it gates |
|---|---|---|
| site-anchored readout | a derivation that relativizes readout to a site index without importing the target field | the four gravity rows, T7 microcausality, T10 |
| reference normalization | a derived pair (numerator readout, reference collection) whose ratio is the target value | AC eta obligation, hypercharge `alpha`, every dimensionless target |
| source action | a derivation of the functional that couples a record configuration to a law | gravity and the AC obligations jointly |
| law range | a derivation that the physical range is nearest-neighbor | L1b, hence the Laplacian ray |

## Scope for independent review

The classification in L1 is computed at the displacement-kernel level and is
therefore free of the finite-box artifacts: the periodic `5^3` and `3^3` boxes
appear only in the operator-identity, span-rejection, and blindness rows, and
the accompanying proofs carry the universal statements. Every decisive equality
is exact integer or `Fraction` arithmetic; there is no floating-point
comparison and no fit. Each scored row carries a negative control, and the
orbit-count table is matched against an independently computed nullity rather
than asserted. Infinite record collections, non-scalar readouts, noncommutative
readout products, anisotropic laws with a supplied preferred axis, and any
physical interpretation of the scalar codomain are outside scope.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md)
and [Cycle 692](PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md)
are cited for what they already established and disclaimed;
[Gravity law cleanup](GRAVITY_LAW_CLEANUP_NOTE.md),
[Gate B far field](GATE_B_FARFIELD_NOTE.md), and
[AC R-eta h-class h-unit readout](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md)
are navigation context for the quoted obstructions, not load-bearing
dependencies.
