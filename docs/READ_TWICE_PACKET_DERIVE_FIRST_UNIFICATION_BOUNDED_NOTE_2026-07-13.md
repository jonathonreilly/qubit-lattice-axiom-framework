# Finite Controlled-Copy Fan-Out and One-Qubit Frame-Function Boundary

**Date:** 2026-07-13

**Type:** bounded_theorem

**Claim type:** bounded_theorem

**Status authority:** independent audit lane only. This note does not set,
predict, or apply an audit outcome.

**Primary runner:**
[`scripts/read_twice_packet_derive_first_unification_2026_07_13.py`](../scripts/read_twice_packet_derive_first_unification_2026_07_13.py)

## Claim Reconciliation

The original version of this note treated two disjoint writes as a candidate
formation packet and bundled counting, permanence, probability, and a clock
rate around it. The later bare-metal, composition, continuation, and
measure-twice probes supersede those claims.

The surviving finite content is narrower:

1. a finite two-controlled-copy fan-out lemma;
2. an access-relative obstruction to restoring the complete pre-write state
   while an untouched outcome-bearing register survives;
3. a coincidence identity under an already supplied Hilbert-space pairing;
4. the one-qubit frame-function loophole; and
5. a conditional read-side representation statement with every import named.

This note no longer proposes a record-formation rule, treats two witnesses as
a unique or universal formation trigger, bundles a possibility-counting rule
with formation, claims unrestricted permanence, or derives physical time.

## Sources And Explicit Imports

- The live constitution is
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
- The controlled-copy classification is
  [`RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md`](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md),
  conditional on its declared readings C1-C4.
- The frame-extension condition, including its finite-additivity-to-frame gap,
  is stated in
  [`READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md`](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md).
- Gleason's theorem is an external mathematical import at dimension at least
  three.
- The prepared-state/frame-identification condition is independent: the state
  representing the frame weights is the state prepared by the record
  protocol.
- Ordinary composite algebra/Hilbert-space structure is explicit supplied
  carrier content here. The one-site Qubit axiom does not derive it. The
  category-relative generatedness theorem is
  [`GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md`](GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md).

## Lemma 1 -- Finite Fan-Out

On a supplied system-register-register tensor carrier, let two blank-input
controlled-copy isometries write the same pointer label to two separate
register factors. For

```text
|psi> = c_0 |0> + c_1 |1>,
```

their composition produces

```text
c_0 |0,r_0,s_0> + c_1 |1,r_1,s_1>,
```

where the two conditional rays in each register are orthogonal. The map is an
isometry; conditional on the pointer label, the two register vectors have
product form. This proves that the finite redundancy pattern is realizable.
It does not say that either register is already a permanent record or that
Nature uses this pattern as a formation criterion.

## Lemma 2 -- What Redundancy Does And Does Not Protect

A single classified copy can be removed by the adjoint of its write isometry,
restoring the complete pre-write state on that finite image.

With two copies, an operation whose support is disjoint from one surviving
register cannot erase that register. Consequently such a restricted operation
cannot restore the **complete** pre-write state. This is access-relative
robustness only. It must be distinguished from three stronger or different
claims:

- source coherence can be repacked locally while an outcome-bearing witness
  remains, as the later final-probe runner explicitly constructs;
- a global inverse of the complete fan-out remains available on its image; and
- repeat projection of a branch is repeatability, not preservation under every
  physically allowed future operation.

Nothing here proves site-fixed permanence, general history nonreconnection, or
the erasure of all unrecorded quantum coherence.

## Lemma 3 -- Coincidence Is A Consistency Identity

For the supplied fan-out state, evaluating the projector onto agreement for
outcome `i` with the standard Hilbert-space state pairing gives

```text
<Psi|A_i|Psi> = conjugate(c_i) c_i = |c_i|^2.
```

The value is nonnegative, normalized over the two pointer outcomes, and
unchanged by simultaneous changes of register representation and agreement
projector. Because the Hilbert-space pairing is already used, this is a
consistency identity, not a derivation of probability or Born's rule.

## Lemma 4 -- Dimension Two Does Not Force Density Form

On a single qubit,

```text
f(P_n) = (1 + n_z^3)/2
```

is nonnegative, normalized, and additive on each orthogonal pair, yet it is
not represented by one density operator. The runner verifies an exact
nonlinear witness.

An explicitly supplied composite factor can raise the mathematical dimension
into Gleason's range. A second witness is one construction of such a factor;
it is not uniquely load-bearing. The runner's supplied `M_4` block verifies
only a finite carrier and a density pairing on one realized menu. It does not
construct the full projection lattice or prove the hypotheses of Gleason.

## Conditional Read-Side Statement

Conditional on all of the following:

1. the controlled-copy readings C1-C4;
2. an explicit physical composite carrier;
3. the frame-extension condition over the required orthogonal decompositions;
4. Gleason's theorem in its declared dimension; and
5. the prepared-state/frame-identification condition identifying the
   representing state with the prepared record-conditioned state,

the frame-represented weight of the recorded outcome equals `|c_i|^2`, and on
the finite fan-out menu it equals the two-register coincidence identity.

This statement does not derive the frame-extension condition, the
prepared-state/frame-identification condition, physical composition, a
formation rule, an actuality selector, a trial denominator, or a frequency
law. The recent composite-qubit route likewise assumes ordinary composition
and probability consistency
([Fiorentino and Weigert, arXiv:2511.15607](https://arxiv.org/abs/2511.15607)).

## Counting And Time Are Separate

The runner retains the arithmetic map

```text
r(w) = (1-w)/(2w),
```

only as an exact regression control. It does not derive what counts as one
physical possibility or select a measured branch of that fork. Counting
belongs to the presentation/individuation lane.

Likewise, a supplied formation criterion defines an event indicator per
chosen update parameter. It does not turn that parameter into physical
duration, fix a clock normalization, or derive a local time rate. Idle-step
dilation is an explicit countercontrol in the later tournament.

## Runner Verification Map

| block | exact finite content | boundary |
|---|---|---|
| B1 | source needles for the constitution, frame premise, write classification, and formation gap | source checks, not physics tests |
| B2 | two controlled-copy isometries, fan-out, orthogonal conditional rays | supplied tensor carrier |
| B3 | coincidence evaluation and representation-change invariance | supplied Hilbert pairing |
| B4 | exact one-qubit nonlinear frame function | finite `M_2` control |
| B5 | supplied four-dimensional carrier and realized-menu density pairing | not a Gleason proof |
| B6 | arithmetic regression control for two proposed weights | no physical counting selection |
| B7 | no-write, one-write adjoint, two restricted local-unitary examples, corrupted-ray controls | examples, not universal permanence |
| B8 | symbolic additivity shape, slot support, repeat projection | fixture/compatibility checks |

The runner mixes computed tests with source and fixture checks. Its green total
certifies this finite verification map only; it does not ratify the broader
formation or constitutional claims that this reconciliation removes.

## No-Go Discipline Gate

**Status: PASS for the scoped finite boundaries below.** The only negative
claim is that the displayed fan-out, pairing, and finite frame-function checks
do not by themselves derive absolute permanence, physical probability, or
time. No claim is made that a larger operational reconstruction cannot derive
those objects.

### N1 -- alternative routes

| attempted route | marker | result against the scoped boundary |
|---|---|---|
| undo one controlled copy by its adjoint | `ATTEMPTED` | the complete pre-write state is restored on the one-copy image, so one finite copy is not absolute permanence |
| undo one side of the two-copy fan-out while leaving the other register untouched | `ATTEMPTED` | the untouched outcome-bearing marginal survives; this proves access-relative no-restore only |
| apply the global inverse of the full fan-out | `ATTEMPTED` | the inverse exists on the finite image, defeating any unrestricted permanence reading |
| derive density form from one-qubit orthogonal-pair additivity | `ATTEMPTED` | the exact nonlinear frame function is normalized and additive on orthogonal pairs but is not density form |
| enter Gleason dimension through a supplied composite | `ATTEMPTED` | this yields a conditional representation route but imports the composite and the full frame hypotheses |
| turn a formation indicator or update count into physical time | `ATTEMPTED` | the arithmetic regression contains no duration unit, trigger law, or clock calibration |

The [minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) do not supply the
missing composite, probability, or time bridges. The [controlled-copy
classification](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md)
and [frame-extension
condition](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md)
remain explicit dependencies rather than hidden authority.

### N2 -- wall independence

The conditional read-side statement has three independent premise groups.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| physical composite/write realization / frame representation | no | no | yes |
| physical composite/write realization / prepared-state identification | no | no | yes |
| frame representation / prepared-state identification | no | no | yes |

Gleason's theorem and its dimension requirement are part of the frame-
representation group. Formation, occurrence, frequency, and clock laws are
not additional walls of this finite conditional statement because it does not
claim those outcomes.

### N3 -- hidden-wall scan

The tensor carrier, blank registers, controlled-copy class, Hilbert pairing,
frame-extension condition, Gleason theorem, and prepared-state identification
are all named. Words such as `supplied`, `conditional`, and `restricted`
describe those imports; no appeal to “the framework provides,” “naturally,” or
“standard QFT” carries a hidden premise.

### N4 -- residual matching

| source | residual there | residual used here | match? |
|---|---|---|---:|
| [minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) | no composite, probability rule, or time metric is supplied | those objects are not inferred from finite fan-out | yes |
| [controlled-copy classification](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md) | conditional finite write class | the fan-out consumes that class only | yes |
| [frame-extension condition](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md) | finite additivity does not yet supply the full frame hypotheses | the conditional read-side statement names the gap | yes |
| [generated-composition theorem](GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md) | ordinary finite composition follows only under generatedness in the stated category | the supplied tensor carrier is not attributed to the one-site axiom | yes |
| [paired runner](../scripts/read_twice_packet_derive_first_unification_2026_07_13.py) | finite fan-out, pairing, nonlinear qubit control, and restricted undo examples | exactly the bounded content claimed here | yes |

No formation or time no-go is borrowed as evidence for the finite lemmas.

### N5 -- rhetoric and resolution audit

Fan-out is checked on one system qubit and two finite register factors.
Access-relative robustness is proved only for operations disjoint from the
surviving register; the global inverse is explicitly retained. The nonlinear
frame-function control is one-qubit-wide, while the supplied `M_4(C)` block is
only a finite realized menu. No lattice-wide permanence, full projection-
lattice theorem, frequency law, or continuum clock is claimed.

### N6 -- partial-closure paths

A retained generated-composition theorem could retire the supplied carrier; a
retained frame-extension theorem plus prepared-state identification could
close the conditional weight representation; a physical record-operation
restriction could strengthen access-relative robustness; and a separate clock
theorem could calibrate update order. These are derivation paths, not automatic
new-axiom requirements. Registered primitives supply none of the missing
content beyond their declared units, kinetic-form, and pointwise-state roles.

### N7 -- strongest steelman

A complete operational reconstruction could derive a generated composite,
prove the frame hypotheses, identify the representing state with the prepared
record-conditioned state, and restrict future lawful operations so that a
formed record is permanent. In that stronger construction the finite lemmas
here could become components of a probability and record theorem. This live
route defeats every broad no-go and leaves only the scoped finite boundaries.

### N8 -- cross-cycle echo

Earlier record work repeatedly separated copying from formation, local
redundancy from unrestricted permanence, update count from time, and a
Hilbert-space expectation from a probability derivation. The generated-
composition and continuation-refinement notes preserve the same separations.
No similar wall is treated here as retired by a naming convention.

## Boundary

- No axiom, primitive, premise registry, or audit status is changed.
- No read or write event ontology is adopted.
- No two-witness threshold, absolute permanence, probability rule, counting
  rule, physical clock rate, or mass result is derived.
- The full-lattice formation, state-sufficiency, actuality, statistics, and
  operational-equivalence questions remain open.
