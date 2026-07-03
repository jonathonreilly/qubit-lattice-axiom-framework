# Koide Occupancy: Individuation Route Factorizes The Bridge And Does Not Escape The Walls (Bounded Note)

**Date:** 2026-07-03
**Type:** open_gate
**Claim type:** open_gate (bounded factorization + sharpened wall; the
current axioms do not decide the conjugate-sector relative-phase
registrability question).
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_occupancy_possibility_individuation_2026_07_03.py`](../scripts/frontier_koide_occupancy_possibility_individuation_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_occupancy_possibility_individuation_2026_07_03.txt`](../logs/runner-cache/frontier_koide_occupancy_possibility_individuation_2026_07_03.txt)

A three-seat adversarial refutation pass returned a convergent negative on the derivation form of this note; this is the repaired convergent wording.

## Question

The prior bridge sentence was:

> one record locking one admissible local possibility is one statistical slot,
> and the relevant locked possibilities for the generation doublet are the
> K/CPT record-outcome orbits rather than the real components of the
> fluctuation coordinate.

This note no longer claims that sentence is derived. The honest result is a
factorization of that sentence into three named premises, plus a sharper wall
showing exactly where the current axioms stop.

## Source sentences

The paired runner guards the live axiom sentences:

> A state is a configuration of records.

> When present, a record locks exactly one admissible local possibility. A site
> never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

> No possibility is privileged. Possibilities are distinguished by the supplied
> algebraic structure alone.

> No site is privileged. Sites are distinguished by the supplied lattice
> structure alone.

> For each site, the available possibilities are determined by, and vary with,
> the nearest-neighbor conditions.

> A law privileges no states. Its domain is a supplied condition, and at every
> state where the condition holds it gives exactly one answer.

The scope boundary is also guarded:

> These axioms state only their named primitive content. Further physical
> structure requires derivation, bridge, explicit admission, or approved
> primitive registration before use as a premise.

The scalar blindness note supplies two guarded sentences:

> The requirement is simple: a separator must make `Tr(O R)` non-real.

> No scalar-ambient functional on that surface separates the conjugate isotypes.

Those two sentences cover the trace-of-`R` scalar surface. They do not give a
completeness theorem for every possible supplied functional of the doublet
coordinate `b`.

## What the scalar check actually shows

The runner enumerates the same six scalar quantities used by the earlier note:
the doublet norm, doublet energy, scalar trace of `R`, scalar trace of `R^2`,
isotypic difference, and an even quartic scalar. The computed result is exact:
the six-item class is K-even on `b` versus `conj(b)`.

For the quantities that depend on `b`, the dependence is only through
`|b|^2`. That is the June 8 measure-neutrality wall restated at this grade:
these quantities are invariant under the native `J_cs` phase rotation. The
distinction sentence does not turn that restatement into a count. It adds a
premise about what the supplied algebraic structure is allowed to distinguish.

The negative result is therefore narrow. The six checked quantities do not
separate the conjugates, but the list is a sample of the scalar class used here,
not a proof that no supplied `b`-functional can ever separate them.

## The explicit separator

The supplied coordinate functional

```text
Im(b) = (b - conj(b)) / (2i)
```

is K-covariant and separates the test conjugates. At `b = 2 + 3i`, it gives
`3`; at `conj(b) = 2 - 3i`, it gives `-3`.

That separator is excluded only by supplying this premise:

> P-phase: record content fixes the orbit magnitude `|b|^2` and not the
> conjugate-sector relative phase.

Equivalently, P-phase supplies a `U(1)` rephasing on the doublet coordinate.
Under that rephasing, `Im(b)` is not invariant while the six enumerated scalar
quantities are invariant. The premise is not answered by the current axioms.

## The decisive open question

P-phase asks: IS THE CONJUGATE-SECTOR RELATIVE PHASE A REGISTRABLE RECORD OUTCOME?

If the answer is no, there is one possibility per conjugate orbit. If the answer
is yes, there are two. The next target is prepared in exactly those terms: a
supplied-structure construction registering the sector phase decides "two
possibilities", while a no-go closing all supplied phase readouts decides "one".

## Slot range is conditional

The slot-range leg is not independent of the individuation answer. It assumes
which possibility set is available.

The runner tests both gradings against both candidate possibility sets:

| Candidate possibility set | Orbit grading | Real-coordinate grading |
|---|---:|---:|
| `{singlet, conjugate-orbit}` | lawful | unlawful |
| `{singlet, real-part, imaginary-part}` | unlawful | lawful |

The verdict flips with the possibility set. That exposes the dependence instead
of hiding it. Slot range does not derive the orbit set; it only follows once the
individuation question has already been answered.

## Occupancy is a separate premise

The one-record-one-slot half of the old bridge is also separate. It is a uniform
occupancy or weighting rule, not an axiom sentence.

The June 8 wall says:

> The Record axiom itself supplies no weighting, normalization, or occupancy rule

Its N1 table says:

> Record names realized outcomes but supplies no weighting/occupancy rule; the
> orbit-count route is pruned in
> `KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md`.

The June 7 route-pruning note states the operative point:

> The K/CPT orbit count is not a weighting rule and does not select `(1,1)` by
> itself.

The current minimal axiom memo still lists downstream gates outside the axioms,
including "context selection, measurement basis selection, Born weights,
probability rules, update laws, decoherence mechanisms, and occurrence rules."
It contains no occupancy rule. The July additions do not change that.

## Honest factorization

The old bridge sentence is exchanged for three named premises:

> P-transport: the one-site individuation discipline transports to the derived
> generation doublet.

> P-phase: record content fixes the orbit magnitude `|b|^2` and not the
> conjugate-sector relative phase.

> P-occupancy: one admissible possibility supplies one statistical slot.

Nothing is eliminated. The theta mass-side composition's surviving conditional
therefore does not drop to zero. It factors into P-transport, P-phase, and
P-occupancy.

## What survives

Two bounded pieces survive.

First, the six-item scalar enumeration is exactly K-even. It is computed over
exact rational data, real where required, and falsifiable by adding a supplied
K-odd readout.

Second, the factorization localizes the remaining question. P-phase is now the
sharp open surface. It can be decided by construction or by no-go as stated
above.

The adjacent K-odd trace note
[`ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md`](ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md)
is evidence for the shape of this boundary, not proof of this note. It builds a
projective K-odd observable on an extended surface, while leaving what value it
registers as a wall. Those registered data still do not deliver the fixed-locus
density or value. The scalar blindness note likewise names projective and
complex-hopping openings as extensions beyond the scalar trace surface.

## Relation to the walls

The individuation route does not escape the June walls. It relocates their
unproved step into P-transport, P-phase, and P-occupancy.

The category-slip wall still blocks counting `b` once merely because it is one
complex number:

> Transferring an operator-symmetry onto "the energy counts `b` once" is a
> category slip and is **circular** (it assumes the asymmetric `(1,1)` split it
> claims to derive).

The measure-neutral selector wall still blocks a static `J_cs` selection of the
count:

> A static complex structure that commutes with `M` and preserves every measure
> can **define** a holomorphic readout but provably cannot **select** it — both
> `(1,1)` and `(1,2)` are `J_cs`-invariant.

The third wall applies directly: Record supplies no occupancy rule, and the
Record-orbit-count route has already been pruned. This note addresses that wall
head-on by naming P-occupancy as a premise rather than reporting a derivation.

## Consequence

The prior consequence does not follow from the current axioms plus the scalar
enumeration. It follows only under the three-premise factorization:
P-transport, P-phase, and P-occupancy.

Under those premises, the orbit grading gives the same arithmetic as before:
`Z_sector / Z_orbit = 2`, `rho = 1`, and `r = 1/2` on the orbit grading. Without
those premises, the current result is only the factorized wall.

This note changes no registry row, no axiom text, and no audit status.

## Primary runner

Run:

```bash
python3 scripts/frontier_koide_occupancy_possibility_individuation_2026_07_03.py
```

Expected terminal form: `CHECK NN: PASS/FAIL -- <description>` lines,
`TOTAL: PASS=<n> FAIL=0`, then five `SUMMARY` lines naming the files, check
count, three premises, decisive open question, and remaining uncertainties.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) - guarded
  live axiom sentences and open-gate boundary.
- [`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md)
  - category-slip, measure-neutral selector, and no-occupancy walls.
- [`KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`](KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md)
  - bridge sentence factored here.
- [`ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md`](ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md)
  - scalar blindness sentences used for the narrow negative surface.
- [`KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md`](KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md)
  - orbit-count pruning wall.
- [`ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md`](ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md)
  - adjacent boundary evidence only, not proof of this note.
