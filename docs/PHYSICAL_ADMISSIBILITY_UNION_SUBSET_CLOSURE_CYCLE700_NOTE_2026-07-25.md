# Admissible configurations are closed under neither disjoint union nor sub-collection, and the exact separation that restores union closure — Cycle 700

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted, no reading of the axiom text is ratified, and **no rule exhibited here
is claimed to be the framework's rule**.

Runner: `scripts/physical_admissibility_union_subset_closure_cycle700_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0; exact integer and set arithmetic in every decisive
row).

## The question

The Record axiom makes scalar readout additive "for any finite collection of
pairwise-disjoint records". Reading that clause requires knowing which
collections are configurations at all, and that is decided by Admissibility:

```text
There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations. For each site, the available
possibilities are determined by, and vary with, the nearest-neighbor conditions.
```

The axiom fixes *that there is* one such rule. It does not say *which*. So any
argument that splits a collection, or joins two of them, is quantifying over
whatever that rule turns out to be. This cycle asks what such arguments are
entitled to assume.

The question is not academic for this campaign. A prior review of an earlier
block rejected exactly such a step: a duplication argument that joined a
configuration to a distant translate and assumed the union remained admissible.
The reviewer's counterexample is reproduced and generalized below, and the
condition that repairs the step is proved.

## U1 — the two exhibited rules are legitimate instances

Two rules are used as witnesses:

```text
A2plus : the available set is empty exactly when a site has >= 2 occupied
         nearest neighbors
A0     : the available set is empty exactly when a site has no occupied
         nearest neighbor
```

These two are the simplest witnesses; the stronger never-empty versions are in
U2b/U3b below. Both depend only on the nearest-neighbor conditions; the runner verifies each
is translation-covariant and proper-cubic-covariant on a `5^3` window against
translations and rotations, and that each available set genuinely *varies* with
the neighbor conditions, as the axiom requires. Neither is proposed as the
framework's rule. They are witnesses that the axiom text, as written, permits
rules with the closure behaviour below.

## U2 — union closure fails, under both site semantics

The axiom does not say whether availability must be consistent only where
records sit, or at every site. Both readings fail, with different witnesses.

**Occupied-site semantics.** Under `A2plus`, take
`S1 = {(0,0,0)}` and `S2 = {(1,0,0), (-1,0,0)}`. Each is admissible on its own
— every occupied site has zero occupied neighbours. The sites are disjoint. In
the union, `(0,0,0)` acquires two occupied neighbours, so its available set is
empty and the union is inadmissible.

**Every-site semantics.** Under the same rule, take `T1 = {(0,0,0)}` and
`T2 = {(2,0,0)}`. Each is admissible, the sites are disjoint, and the two
records are not even adjacent. But the *empty* midpoint `(1,0,0)` acquires two
occupied neighbours, so its available set is empty and the union is
inadmissible.

The runner also verifies that this second union **is** admissible under
occupied-site semantics, so the two readings are not equivalent: they disagree
on a concrete configuration.

## U3 — sub-collection closure fails too

The additivity clause splits a collection into parts. That direction fails as
well. Under `A0`, the configuration `{(0,0,0), (1,0,0)}` is admissible — each
record has one occupied neighbour. Its strict subset `{(0,0,0)}` is
inadmissible, because the remaining record now has none.

So for some legitimate instances of the axiom, a sub-collection of a readable
configuration is not itself a readable configuration.

## U2b / U3b — the same two failures with never-empty availability

The obvious objection to `A2plus` and `A0` is that an empty available set is
degenerate, so the witnesses might be strawmen. Both failures survive without
one.

Take availability to be a proper **nonempty** subset that varies with the
neighbour conditions, and let a configuration record *which* possibility each
record locked. Write `c0` for a central element of the one-site algebra and
`c1` for a non-central one; nothing depends on which, only that there are at
least two.

**Union, with availability shrinking on crowding.** Available set is both
possibilities until two neighbours are occupied, then `c0` only. Let
`P1 = {(0,0,0) locks c1}` and `P2 = {(1,0,0) locks c0, (-1,0,0) locks c0}`.
Each is admissible. In the union, `(0,0,0)` has two occupied neighbours, so `c1`
is no longer available to it — a possibility that was already locked is
withdrawn — and the union is inadmissible.

**Sub-collection, with availability growing on contact.** Available set is `c0`
only when isolated, both on contact. `Q = {(0,0,0) locks c1, (1,0,0) locks c0}`
is admissible. Dropping the second record leaves `(0,0,0)` isolated, where `c1`
is unavailable, so the strict subset is inadmissible.

The runner verifies that neither rule ever returns an empty available set. So
the closure failures are not an artefact of degenerate availability; they follow
from availability varying at all, which the axiom requires.

## U4 — the exact separation, valid for every nearest-neighbor rule

**Theorem.** Let `S1, S2` be configurations whose closed one-neighbourhoods are
disjoint, `N[S1] ∩ N[S2] = {}`. Then no site has occupied neighbours in both
parts, every site's neighbour count in `S1 ∪ S2` is the sum of its counts in
the parts, and therefore every site's nearest-neighbor condition in the union
equals its condition in whichever part contains it. Availability is unchanged
everywhere, so the union is admissible under either semantics.

*Proof.* If a site `x` had an occupied neighbour in each part then
`x ∈ N[S1]` and `x ∈ N[S2]`, contradicting disjointness. `[]`

The point is the quantifier: the proof uses nothing about the rule beyond its
being a function of the nearest-neighbor conditions, so it holds for **every**
nearest-neighbor rule, including the framework's unspecified one. The runner
checks the combinatorial content exhaustively over a window: 2070 site-disjoint
configuration pairs examined, 316 of them separated, and on every separated
pair the count is additive and no site sees both parts.

**Tightness.** At closed-neighbourhood contact the conclusion fails: the `U2`
every-site witness has `N[T1] ∩ N[T2] = {(1,0,0)}`, one site, and its union is
inadmissible.

## U5 — what a duplication argument actually needs

Site-disjointness is strictly weaker than the U4 hypothesis and is reached
earlier. For a three-record base translated along one axis:

| shift | sites disjoint | closed neighbourhoods disjoint |
|---|---|---|
| 1 | no | no |
| 2 | yes | no |
| 3 | yes | no |
| 4 | yes | **yes** |

So a duplication argument that only separates *sites* is not licensed; it must
separate closed one-neighbourhoods. This is the exact hypothesis the earlier
block's duplication step was missing, and adding it repairs that step rather
than abandoning it.

## Consequences, stated but not ratified

- **The additivity clause carries an implicit domain condition in both
  directions.** Reading it as quantifying over all splittings of all
  collections presumes both that the parts are configurations (U3 can fail) and
  that joins are configurations (U2 can fail). Which collections are in scope
  depends on the unspecified rule.
- **Composition arguments must state the separation hypothesis.** Any argument
  that joins two configurations — duplication, independent subsystems,
  cluster decompositions — needs U4's condition explicitly, or a rule for which
  closure is known.
- **The two site semantics are inequivalent** and the axiom text does not
  choose. U2 exhibits a configuration on which they disagree.

These are clarity items. This note takes no position on which reading or which
semantics is intended, and records only what each entails.

## What this does not do

- It does not identify the framework's admissibility rule, nor claim `A2plus`
  or `A0` is it. They are witnesses that the axiom permits such behaviour.
- It does not show closure fails for the framework's actual rule. It shows
  closure cannot be *assumed* without knowing the rule, which is the property
  arguments have been relying on.
- It does not derive a formation rule, dynamics, probability, or readout, and
  changes no lane, row, or obligation status.
- It awards itself no N1–N8 verdict. U2 and U3 are negative results; that
  verdict is reviewer-owned.

## Scope for independent review

Every decisive row is exact integer or set arithmetic on explicit finite
configurations; there is no sampling of the decisive witnesses and no
floating-point comparison. U1's covariance checks run over a `5^3` window
against two translations and six rotations, which is a check on the exhibited
rules rather than a proof for all rules — the rules' covariance is also
immediate from their depending on the neighbour count alone, which is
rotation-invariant. U4's proof is general and box-free; the exhaustive window
check is corroboration, not the argument. Rules of range greater than one,
content-dependent availability, and infinite configurations are outside scope.

## Dependency citations

The runner imports nothing from the repository. The load-bearing framework
authority is [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md). The
closure question was raised by a review finding on an earlier block of this
campaign; the block itself is not cited because it was rejected as submitted
and its salvaged content, the abstract kernel classification, is unrelated to
this result.
