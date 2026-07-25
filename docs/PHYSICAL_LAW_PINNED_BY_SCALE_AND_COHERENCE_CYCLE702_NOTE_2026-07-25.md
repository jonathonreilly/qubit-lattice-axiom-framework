# The law's form is pinned by the scale primitive's own clause, and the neighbour rule is constrained by readout coherence — Cycle 702

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. **No counting convention is adopted, no
dimensionless value is supplied, no reading of the axiom text is ratified, and
no exhibited rule is claimed to be the framework's rule.** No observed or
empirical input is used.

Runner: `scripts/physical_law_pinned_by_scale_and_coherence_cycle702_2026_07_25.py`
(8 PASS / 0 FAIL, exit 0; exact integer, rational, and symbolic arithmetic, with
a negative control on each decisive row).

## Why this route

The normalization residuals in this framework are usually approached by asking
which convention to adopt. This note deliberately adopts none. It asks instead
what the **approved scale-reference primitive** and the **coherence of the axiom
text** already pin, on their own.

The lever is a clause of the primitive itself. `SCALE_REFERENCE_PRIMITIVE_NOTE.md`
fixes the lattice unit by `a^{-1} = M_Pl` and then says:

> "This is a units conversion, not a physics axiom. It carries zero
> dimensionless content: no mass ratio, coupling, mixing angle, phase, selector,
> readout bridge, or empirical fit is supplied by it."

and

> "It does not supply any dimensionless quantity. Dimensionless physics must
> derive from retained-grade framework content or remain conditional/open."

Taking the scale as given therefore does more than supply a ruler: it makes
explicit that **any dimensionless number in a law is an unsupplied input**. Part
I turns that into a statement about which law the framework can write down
without supplying one.

## Part I — the field law

The landed
[proper-cubic finite-support linear-kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
gives, at nearest-neighbour range and under its named conditions, a
two-dimensional family

```text
L = A·I + B·Delta.
```

**P1.** The lattice symbol is `A + B·Dhat(k)` with
`Dhat(k) = 2(cos k1 + cos k2 + cos k3) − 6`. At zero momentum it equals exactly
`A`. So the response is long-ranged precisely when `A = 0`; any nonzero `A`
leaves a gap, for every `B`.

**P2.** Expanding along a general direction — the full three-dimensional
quadratic form, not a single-axis slice — gives `A − B|k|²`, isotropically. So a
nonzero `A` is a Yukawa mass term with `m² = A/B` and screening length
`1/√(A/B)` **in lattice units**.

**P3.** Confirmed exactly on a periodic `4³` box: the constant field is
annihilated exactly when `A = 0`, and for nonzero `A` the constant is scaled by
exactly `A`.

**P4.** The overall scale `B` factors out. Checked as an exact entrywise matrix
identity `op(A,B) = B·op(A/B, 1)` over several exact rationals, with a wrong
rescaling rejected as the negative control. So the family's only physical input
is the single dimensionless ratio `A/B`.

### What this pins, stated precisely

Combining P1–P4 with the primitive's clause:

> **On the current surface, `A = 0` is the only member of the family that can be
> written down without supplying a new dimensionless quantity.** It is picked
> out by a structural condition — the operator annihilates constants — which
> requires no number. Every other member is specified by a dimensionless `A/B`,
> which the scale primitive explicitly does not supply and which the framework
> must therefore derive or leave open.

In the primitive's units, a nonzero `A/B` of order one screens the response
within a few lattice units, which is the Planck scale; making the screening
length macroscopic requires `A/B` to be a very small dimensionless number, which
is precisely the kind of quantity the primitive declares it does not supply.

**This is not a proof that `A = 0`.** A future retained derivation could supply
`A/B`, and the note says so. The claim is about what can currently be written
without an import, and it is a claim of that exact strength — no convention is
adopted anywhere in it.

## Part II — the neighbour rule

The Record axiom asserts additivity "for any finite collection of
pairwise-disjoint records". For the unrestricted reading to be well posed, both
sub-collections and disjoint unions of admissible configurations must themselves
be admissible. Write `A(p)` for the available set at a site whose
nearest-neighbour occupancy pattern is `p`.

```text
closure under sub-collection  <=>  A antitone   (A(q) ⊇ A(p) whenever q ⊂ p)
closure under disjoint union  <=>  A monotone   (A(q) ⊇ A(p) whenever q ⊃ p)
```

**Q1.** Every occupancy pattern is comparable to both the empty and the full
pattern, so the two closures together force `A` to be constant on the pattern
lattice. A constant rule satisfies both; a genuinely varying rule fails at least
one.

**Q2.** The two failure modes are complementary and both are natural: a rule
whose availability *shrinks on crowding* keeps sub-collections and loses unions;
a rule whose availability *grows on contact* keeps unions and loses
sub-collections.

**Q3.** Exhaustive scan of **all 2187** count-only availability rules on a
two-letter alphabet: **no** rule is both sub-collection-closed and union-closed
while genuinely varying.

**Q4 (negative control).** The same scan finds **24** genuinely varying rules
with exactly one of the two closures, so Q3's emptiness is a real constraint and
not a broken filter.

### What this says about the law

The Admissibility axiom requires the available possibilities to *vary* with the
nearest-neighbour conditions. Part II shows that requirement is incompatible
with the unrestricted reading of the additivity clause. One of the two must be
narrowed, and **which one is narrowed is law content, not a convention**:

- Narrow additivity to **decomposition only**. This is the direction the landed
  cycle-698 M1 argument actually uses, and it survives.
- Narrow additivity to **separated collections**. The sufficient separation is
  known: disjoint closed one-neighbourhoods.
- Keep additivity unrestricted. Then the rule is constant, contradicting "vary
  with".

The third branch is closed. The first two are live and differ in what they let
later arguments do.

## What this does not do

- It does not adopt a counting convention, a unit convention, or any reading.
- It does not prove `A = 0`; it identifies `A = 0` as the unique member needing
  no supplied dimensionless input on the current surface.
- It does not claim the physical law is at nearest-neighbour range. Range 1 is
  the named condition inherited from the landed classification, together with
  that note's other named conditions (rational scalars, linearity, finite
  support, covariance).
- It does not identify the framework's admissibility rule, and the rules used in
  Part II are witnesses, not proposals.
- It uses no observed value, fitted selector, or literature comparator.
- It changes no lane, row, or obligation status, and awards itself no N1–N8
  verdict; Part II's Q3 is a negative result and that verdict is reviewer-owned.

## Scope for independent review

Part I's P1–P3 are exact symbolic and exact rational computations; P4 is an
entrywise matrix identity with a wrong-rescaling control. The step from those to
"the only member needing no supplied number" is an argument about the primitive's
declared content, quoted verbatim above, not a computation — it should be
reviewed as such. Part II's Q1 is a lattice-comparability argument whose decisive
step is verified over all 64 patterns; Q3 is exhaustive over the full count-only
rule space on a two-letter alphabet, and Q4 shows the filter is live. Larger
alphabets, rules of range greater than one, and non-count-only patterns are
outside scope: Q3's exhaustiveness is over the space it names.

## Dependency citations

The runner imports nothing from the repository. Load-bearing:
[Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and the landed
[proper-cubic finite-support linear-kernel classification](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md)
for the two-dimensional family Part I starts from. The scale clause quoted in
full is from `SCALE_REFERENCE_PRIMITIVE_NOTE.md`. Part II's question was raised
by a review finding on an earlier block of this campaign; the separation
condition it refers to is on the branch recorded in that campaign's
`PR_BACKLOG.md`.
