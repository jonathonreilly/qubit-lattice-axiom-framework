# Coherent causal-close detector compiler — Cycle 209

**Date:** 2026-07-16

**Authority:** none

**Status:** bounded conditional detector construction; loading, arming, and
record occurrence remain supplied

**Constitutional effect:** none

**Audit:** unset

**Packaging:** draft parking branch and draft PR only

Companion runner:

```text
scripts/coherent_causal_close_detector_compiler_cycle209_2026_07_16.py
```

## Attribution boundary

The interacting two-fermion walk and its molecular bound states are prior
work of Bisio, D'Ariano, Mosco, Perinotti, and Tosini, *Solutions of a
Two-Particle Interacting Quantum Walk*:

<https://arxiv.org/abs/1804.08508>

That paper supplies the one-dimensional Thirring-QCA engine and solves its
two-particle scattering and bound sectors.  It does not supply this third
distinguishable carrier, this relational outcome compiler, or the framework's
record interpretation.  Cycle 209 is an extension relative to that paper.
Broader literature novelty has not been established.

## Question

Cycle 208 replaced a Fourier-channel label with the relational partition

```text
close := |x1 - x2| <= 2
q     := 2 xp - x1 - x2
T     := close and q < 0
R     := close and q > 0
X     := not (T or R).
```

But it still applied that partition as a supplied projective readout at tick
70.  Can the comparison itself be performed by a finite nearest-neighbour
process without recording the individual positions, consulting an outcome
table, or treating silence until a timeout as evidence?

## Result up front

Yes, conditionally and in a bounded apparatus.

The runner constructs a sixteen-site, three-rail coherent detector.  A
generic one-hot encoder feeds ripple adders and unsigned comparators built
only from `NOT`, `XOR`, `AND`, and `OR`.  The resulting fresh-target Boolean
DAG is converted into a reversible `X/CNOT/TOFFOLI` circuit.  It copies only
the final one-hot `T/R/X` value and then reverses the entire computation.
Consequently every position-dependent workspace bit returns to zero: two
different configurations in the same outcome class retain their coherence
instead of leaking which-position information into detector garbage.

The reversible primitives are explicitly routed with adjacent swaps.  Every
operation is radius one on a line embedded in the cubic lattice, and the
apparatus-carried embedding has all 24 proper-cubic images.  This is a
covariance property of the detector apparatus, not yet a proper-cubic
interacting matter law; the proper-cubic interacting lift remains open.

The finite truth-table tournament exhausts all `16^3 = 4,096` lawful position
triples.  The circuit agrees exactly with the relational predicate, is
unchanged by pair exchange and every common translation that remains inside
the aperture, and exchanges `T` with `R` under reflection.  Random complex
amplitudes retain positive normalized class weights.  Copying the outcome to
a second record changes none of those weights.

The exact bounded census is:

| quantity | result |
|---|---:|
| one-hot input rails | 48 |
| reversible logical qubits including outcome | 291 |
| logical reversible primitives | 871 |
| explicitly routed nearest-neighbour primitives | 500,703 |
| routing swaps | 499,832 |
| lawful basis triples exhausted | 4,096 |
| in-aperture common translations checked | 32,896 |
| causal process events | 878 |
| sampled logical asynchronous schedules | 128 |
| sampled physical causal schedules | 64 |

Applied to the strong-collision Cycle-208 state, the compiled predicate keeps
the same transmitted, reflected, and breakup weights and the transmitted
record still selects the independently calibrated molecular mass branch.
Deleting the pair-close comparator changes the partition, so binding is not
silently replaced by projectile direction alone.

```text
strong T/R/X                 0.92961929 / 0.02392843 / 0.04645228
T-conditional intact pair   0.99175378
T-conditional coherence     0.99829583
collision secant mass       0.96301544
curvature/inertial mass      0.95013098
relative difference         1.3561 percent

delete pair-close:
T/R/X                        0.95853135 / 0.04108250 / 0.00038615
```

## Why causal completion is not a timeout

The detector interface contains three explicit causal close facts, one for
each loaded particle rail.  `ARM` is unavailable until all three exist.  A
program head then traverses the finite reversible circuit, uncomputes the
workspace, and appends `DONE`.  The outcome port is enabled only by `DONE` and
the one-hot output rail.  Thus `DONE` has every close fact and every circuit
stage in its causal ancestry.  Deleting any close fact leaves the detector
open forever; elapsed ticks do not create an `X` record.

This follows the finite causal-completion discipline already established by
the Cycle-16 and Cycle-69 probes.  It proves completion only for the declared
finite interface.  It does not establish that the universe supplies such a
closeable interface for every event.

## What is and is not now physical

The comparator need not interact only through records.  Its intermediate
registers are coherent, constrained possibilities at nonrecord sites.  Only
the final outcome is offered to a record port.  This is necessary: writing
the three input positions as permanent records would over-measure the
scattering state and destroy within-channel coherence.

The construction therefore removes two imports from Cycle 208:

1. no Fourier basis is used; and
2. no host-language `T/R/X` lookup is applied at the record boundary.

It does **not** remove these imports:

- the apparatus and its one-particle rails are supplied;
- the loading event and supplied arming/close process are supplied;
- the reversible gate law is a candidate local law, not derived from the
  current axioms;
- the final transition from a coherent outcome rail to an occurring,
  permanent record is supplied; record formation remains imported;
- squared amplitudes are normalized weights, but there is no Born-frequency
  theorem or occurrence theorem;
- the matter and collision engine remains one-dimensional; and
- no gravitational source law follows.

## Bare-metal interpretation

The useful substrate distinction is now explicit:

```text
coherent local possibilities carry and compare the interaction history;
causal close certifies that the finite comparison is complete;
the final class, not the hidden working data, is eligible to become a record.
```

That is materially closer to an actual detector than Cycle 208's supplied
projector.  It is not yet an autonomous measurement theory.  The decisive
next interface is to derive the loading and close facts from the scattering
and separation history itself, then couple the same construction to a
proper-cubic interacting object.

## Scope

This is a finite conditional construction on the draft parking branch.  It
does not establish empirical novelty, a mass prediction, an unconditional
detector, record formation, probability occurrence, a clock law, gravity, or
a TOE.  It makes no axiom conclusion and changes no foundation, primitive,
registry, policy, queue, or audit surface.

## Verification

```text
python3 scripts/coherent_causal_close_detector_compiler_cycle209_2026_07_16.py
```
