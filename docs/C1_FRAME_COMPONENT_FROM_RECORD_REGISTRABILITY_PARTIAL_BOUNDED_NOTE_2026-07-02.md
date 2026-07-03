# C1 Frame Component From Record Registrability -- Partial Bounded Note

**Date:** 2026-07-02
**Type:** bounded theorem (partial supplier derivation, conditional on the named registrability reading R*)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Paired runner:**
[`scripts/frontier_c1_frame_component_from_record_registrability_partial_2026_07_02.py`](../scripts/frontier_c1_frame_component_from_record_registrability_partial_2026_07_02.py)
**Cached output:**
[`logs/runner-cache/frontier_c1_frame_component_from_record_registrability_partial_2026_07_02.txt`](../logs/runner-cache/frontier_c1_frame_component_from_record_registrability_partial_2026_07_02.txt)

## Purpose

This note gives a self-contained `hw=1` finite registrability argument for the
frame component C1a: no imported basis in a scalar readout. It is conditional on
one named interpretive premise, the registrability reading R* below.

The result is partial. Conditional on the registrability reading R*; C1b remains
open: R* excludes imported-basis scorings, but it does not exclude
realized-state-dependent partitions.

## Supplied Structure And R*

The supplied finite structure used here is only:

- the `hw=1` circulant algebra `A` on `C^3`, with unit `I`, cyclic shift `U`,
  and Hilbert-Schmidt inner product;
- the realized Yukawa/circulant readout `Y`, available only through the
  realized-state primitive interface quoted below;
- the Record axiom sentences quoted below;
- the landed Block01 and Block02 finite witness classes.

The Record axiom surface is:

```text
When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.
```

The realized-state primitive interface is:

```text
The laws do not pick the state; the world does, among the states the laws
permit.

Derivations may evaluate at the realized state, pointwise.

Nothing more is supplied: no averaging over alternatives, no typical or
generic claim, and no quoting a number that would differ had another
law-admissible state been realized.
```

It also states:

```text
The framework takes one realized-state reference: a law-admissible state
supplied by the physical history.

This is pointwise evaluation, not a state-selection rule. It carries zero
state-contingent content: no state, averaging over alternatives, measure,
weighting, probability rule, typicality claim, genericity claim, preferred
state, default state, boundary condition, normalization rule, or value is
supplied by it.
```

The complement-registration precedent is quoted only as a pattern, not as a
transport theorem. Its boundary says:

```text
This note proves only that, on the supplied finite three-slot circulant slot
model, the two Hamming-complement readings have the same Record-registrable
scalar content.
```

Its theorem states, in part:

```text
(T1) the registrable surface is the symmetric-function algebra of the
unordered spectrum [by the cited registrability theorem, Consequence B];
```

and its T1 statement is:

```text
The registrable surface is the symmetric-function algebra of the unordered
spectrum [by the cited registrability theorem, Consequence B].
```

Its T3 non-registrability statement is:

```text
Frame-dependent components are not constant on the supplied frame orbit, so
they are not registrable.
```

These statements are made for that note's supplied finite three-slot circulant
slot model only. This note uses the mechanism as a precedent pattern; it does
not treat the complement note as a transportable general registrability theorem.

The repo's existing registrability characterization is
[`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
(bounded theorem, unaudited at the time of writing): **in a supplied readout
context** with a finite central-sector decomposition, registrable scalar
readouts are finitely additive and orbit-constant, and its Conditional
Implication B carves the registrable surface as symmetric spectral content.
That theorem's own boundary conditions everything on the context being
SUPPLIED. R* below addresses the complementary question — what happens to
readout data that is NOT supplied — by the same orbit-constancy mechanism.
The upstream theorem is cited as the mechanism's in-repo source, not as a
proof of R*; its conditionality is inherited here, not resolved.

**Registrability reading R*.** A registrable scalar readout is a scalar function
of the supplied structure that is:

1. additive over pairwise-disjoint records, with `I(empty)=0`; and
2. well-defined given only the supplied structure, meaning constant on the orbit
   of any unsupplied auxiliary choice.

An imported basis or imported frame is an unsupplied auxiliary choice; its orbit
is the choice set. The definition-level reading from Record is: because "Only
records are readable" and "a record locks exactly one admissible local possibility", a
value that varies with an unsupplied choice is not locked by any record of the
supplied structure.

R* is this note's single interpretive premise. R* is not asserted as new axiom
content and is not registry content; it is flagged for audit adjudication.

## T1 - Orbit-Constancy Criterion

**Claim.** Conditional on the registrability reading R*; C1b remains open. A
scoring readout is R*-registrable only if it is constant on the imported-choice
orbit.

**Finite witness.** In the two-channel coefficient plane, the Hadamard unitary

```text
H = (1/sqrt(2)) [[1, 1], [1, -1]]
```

sends the equal-split vector to a non-equal vector:

```text
H (1, 1)^T = (sqrt(2), 0)^T.
```

So the same supplied `Y`, expressed in two imported bases in the same choice
orbit, gives different S2 per-mode verdicts: equal in the first basis and
non-equal in the Hadamard-mixed basis. Therefore S2-class imported-basis
scorings are not R*-registrable.

This is a bounded exclusion of imported-basis scorings under R*. It is not a
claim about all possible readout rules in all models.

## T2 - S1 Compatibility

**Claim.** Conditional on the registrability reading R*; C1b remains open. The
S1 generator-channel Hilbert-Schmidt partition is R*-registrable-compatible.

On the `hw=1` circulant surface, S1 uses the algebra unit direction and the
Hilbert-Schmidt orthocomplement inside the supplied circulant span. For `N=3`,
with `B = J - I`, the supplied Hilbert-Schmidt data are:

```text
||I||^2 = 3,   ||B||^2 = 6,   <I, B> = 0.
```

No imported basis enters the definition of the partition. The scoring value is
a function of supplied algebraic data, so it is trivially constant on the
imported-choice orbit.

This does not select S1 among all conceivable rules. It only says S1 passes the
R* no-imported-basis test that S2-class imported-basis scorings fail.

## T3 - S3 Boundary: The Honest Limit

**Claim.** Conditional on the registrability reading R*; C1b remains open. R*
does not exclude `Y`-dependent partitions.

The S3 idempotent/eigenvalue frame is determined by `Y` itself. `Y` is supplied
only through the realized-state primitive's pointwise interface quoted above:
one law-admissible realized state is available for pointwise evaluation, but no
state content, averaging, probability, typicality, or value is supplied by the
primitive.

For the parent S3 root, with `a = 1` and

```text
t = -2 + (3/2) sqrt(2),
```

the eigenvalue data are

```text
lambda_0 = 1 + 2t,        lambda_1 = lambda_2 = 1 - t,
```

and the S3 condition is

```text
lambda_0^2 = 2 lambda_1^2.
```

The value

```text
r = t^2 = 17/2 - 6 sqrt(2)
```

is a function of `Y`'s supplied spectral data. Equivalently, for this normal
circulant surface,

```text
a = tr(Y)/3,
|b|^2 = (tr(Y*Y) - 3 |a|^2)/6,
r(Y) = |b|^2/|a|^2,
```

so `r(Y)` is built from symmetric spectral data of `Y` and is constant under
imported basis changes. Thus registrability/orbit constancy does not exclude
S3-class `Y`-dependent partitions.

R* discharges only the imported-basis half of C1.

## T4 - Basis-Averaging Check

**Claim.** Conditional on the registrability reading R*; C1b remains open.
Basis-averaging is not an S2 rescue.

Let the per-mode square functional in an imported two-channel frame be
`(|c_1|^2, |c_2|^2)`. Average it over the 16-element finite real unitary subgroup
generated by the Hadamard matrix `H` and the sign flip `diag(1,-1)`. The exact runner
checks that, for a symbolic real vector `(x, y)`, the averaged per-mode squares
are:

```text
((x^2 + y^2)/2, (x^2 + y^2)/2).
```

Only the invariant total `x^2 + y^2` survives. Therefore basis-averaging changes
the rule into invariant-content scoring; it does not preserve an imported-basis
S2 rule as an R*-registrable per-mode rule.

## T5 - Consequence Map

C1 has two pieces:

- **C1a:** no imported basis;
- **C1b:** no realized-state-dependent partition.

Conditional on the registrability reading R*; C1b remains open. R* implies C1a:
imported-basis scorings are not R*-registrable because they vary along an
unsupplied imported-choice orbit.

C1b remains open. T3 is the witness: S3's `Y`-dependent frame is not excluded
by orbit constancy because `Y` is supplied via the realized-state primitive's
pointwise interface.

The next attack shape is candidate-only: Record says that the locked
possibility is "invariant under repeated readout." A future note could test
whether repeated-readout invariance supplies partition state-independence and
therefore C1b. This note makes no such claim.

## What This Note Does NOT Claim

- R* is not asserted as axiom content.
- R* is not registry content; it is a reading flagged for audit adjudication.
- S1 is not selected among all conceivable rules.
- C1b remains open.
- No `kappa_EW` value is claimed.
- No parent wall is closed.
- No new axiom, primitive, admission, normalization, probability rule, state
  selector, or observable bridge is introduced.
- The complement-registration note is used as a scoped precedent pattern only,
  not as a transportable theorem.

## Load-Bearing Inputs

| path | role |
|---|---|
| [`ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](ACPHILAMBDA_HW_COMPLEMENT_READING_REGISTRATION_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md) | Supplies the scoped precedent pattern: on its supplied slot model, registrable scalar content is symmetric spectral content and frame-dependent components are not registrable. |
| [`FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md`](FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md) | Landed Block01 dependency; supplies the three parent-named scoring rules, Hadamard witnesses, and the no-imported-frame residual. Independent audit still owns its verdict and any retained-grade dependency closure. |
| [`SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md`](SUPPLIED_READOUT_CONTEXT_TWO_COMPONENT_DECOMPOSITION_BOUNDED_NOTE_2026-07-02.md) | Landed Block02 dependency; supplies the C1/C2 separation and the independence of C1a from C2 at witness level. Independent audit still owns its verdict and any retained-grade dependency closure. |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Supplies the Record locking, repeated-readout invariance, readability, and finite-additivity sentences; also shows measurement basis and context selection remain outside axiom content. |
| [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | Supplies the pointwise realized-state evaluation interface and the no-state-content boundary for `Y`. |
| [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md) | The repo's existing registrability characterization (supplied-context boundary; Conditional Implication B). Role: in-repo source of the orbit-constancy mechanism that R* transports to unsupplied choices. Dependency class: unaudited bounded theorem; independent audit must adjudicate it before retained-grade dependency closure. |

## Paired Runner

Paired runner:

```text
scripts/frontier_c1_frame_component_from_record_registrability_partial_2026_07_02.py
```

Expected terminal line:

```text
TOTAL: PASS=19 FAIL=0
```
