# Full-Law Inventory Adversarial Reduction

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact finite independence and dependency probe.
It is not the framework law, an axiom proposal, an audit verdict, or authority
to alter the live foundation, audit state, or the source notes it reviews.

## Purpose

The full-lattice FD-SLIR packet lists thirteen separately testable jobs. The
exchange-law reduction packet conditionally reduces a common-basis-covariant
two-qubit generator to identity plus SWAP. This note attacks both surfaces:

- identify jobs that were bundled too coarsely;
- identify jobs already determined by a fully typed instrument law;
- expose boundary, quotient, propagation, trial, and record-memory seams; and
- state the smallest corrected dependency DAG under explicit typing choices.

The reviewed sources are:

- [`FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md`](FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md)
- [`QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md`](QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md)

The source thirteen-item list remains useful as a **job checklist**. It is not
a list of thirteen independent physical atoms.

## 1. Open And Two Record Values Do Not Fit As Three Qubit Sectors

Three nonzero mutually orthogonal record-status sectors require total Hilbert
rank at least three. On one `M_2(C)` carrier,

```text
P_0 + P_1 = I_2
```

already exhausts the two-dimensional space. If the ready/open state is
`|+>`, then

```text
Tr(|+><+| P_0) = Tr(|+><+| P_1) = 1/2.
```

It is not a third perfectly distinguishable value.

An exact law must choose one typing:

1. `OPEN` is metadata—the absence of a record in a partial record map—not a
   third quantum sector;
2. a separate classical occupancy flag or at least a three-state pointer is
   supplied; or
3. a fresh pointer carrier is distinct from the working qubit.

Under the first route, preparation/program records elsewhere must reconstruct
the unrecorded working-qubit state. The one-site Qubit domain does not by
itself provide record status, address, or identity.

## 2. Law, Boundary Class, Boundary Instance, And Boundary Selection

The four roles must not be collapsed. Exact controls give:

```text
same law I + boundary |0>  -> Z law (1,0)
same law I + boundary |1>  -> Z law (0,1)

same boundary |0> + law I  -> Z law (1,0)
same boundary |0> + law X  -> Z law (0,1).
```

Therefore neither the law nor the boundary replaces the other.

- The **allowed boundary class/type** belongs to the event/domain contract.
- Decoding a **chosen boundary or preparation record** belongs to state/input
  reconstruction.
- Selecting or assigning a distribution to the **actual cosmological
  boundary** is not microscopic law content. It is an additional framework
  input only if unconditional prediction of this particular universe is
  demanded.

The word “boundary” may appear in both domain and state rows only when this
class-versus-instance distinction is explicit.

## 3. Composition And Physical Equivalence Must Be Ordered

Raw composition does not determine a physical quotient. Take four raw states

```text
(visible bit, hidden token).
```

If the only context reads the visible bit, future-transcript equivalence has
two classes, each containing two raw states. Adding one token-sensitive
context produces four singleton classes. The carrier did not change; the
physical quotient did.

The canonical operational quotient is downstream:

```text
h ~ h'
iff every allowed finite adaptive future protocol
    gives the same transcript law from h and h'.
```

It consumes the context repertoire, exact maps, exhaustive continuation, and
statistics. If a pre-operational gauge quotient is intended instead, that is
a separate physical atom. “No silent extra sector” and “quotient the silent
sector away” are alternative closure routes, not premises to count twice.

## 4. Strict Finite Propagation And Continuous Exchange Are Different

On a three-site chain, let

```text
H = SWAP_12 + SWAP_23,
O = Z_1.
```

The first commutator `[H,O]` still commutes with a site-three test, while

```text
[H,[H,O]]
```

does not. Continuous exchange therefore reaches site three at exact order
`t^2`. A finite-range continuous Hamiltonian normally supplies a
Lieb-Robinson/quasilocal cone with tails, not an exact circuit light cone.

A full law must choose and prove one propagation semantics:

1. discrete circuit/QCA layers with exact finite propagation;
2. continuous finite-range exchange with a Lieb-Robinson bound; or
3. a later relativistic microcausal limit.

Event locality, local atomic maps, gluing, finite causal depth, and a no-Zeno
condition derive finite propagation in **event steps**. Turning that into a
physical speed additionally consumes the time/rate calibration.

## 5. One-Shot Statistics Do Not Define Trial Frequencies

There are three exact projectively compatible binary processes with the same
one-time marginal `1/2`:

| process | adjacent `+/-1` correlation | eight-trial frequency support |
|---|---:|---|
| IID fair | `0` | binomial |
| one frozen hidden bit | `+1` | `0` or `1` |
| alternating hidden bit | `-1` | exactly `1/2` |

One-shot statistics plus projective extension therefore do not imply one
generic frequency theorem. A complete joint law may make IID, ergodicity, or
a martingale property a theorem, but a physical trial corpus and
re-preparation equivalence must first be identified.

`TRIAL_CORPUS` is an empirical-interface job unless the state and context
surfaces explicitly reconstruct it. It is not automatically a new
constitutional atom.

## 6. Record Identity And Preservation Are Independent Of Renewal

Two finite countermodels separate the jobs:

1. A one-site archive may map `OPEN -> R0/R1` and then keep both record states
   absorbing forever. It has exact identity/preservation and no second fresh
   carrier.
2. A process may allocate a genuinely fresh address every cycle while an
   allowed later map flips an old record. It has renewal capacity and no
   preservation.

Migratory preservation needs a lineage relation: the same `(fact,content)`
may move to a new address. Fresh renewal does not define that identity. Export
specifically **consumes** an identity notion because it claims the old fact
survives elsewhere.

## 7. Which Thirteen Jobs Reduce Under Exact Instrument Typing

### 7.1 Physical quotient

Split it from raw composition and derive the operational quotient downstream.

### 7.2 State and boundary

Keep predictive record completeness. Move allowed boundary **class** to the
domain surface and the chosen boundary **instance** to state/input decoding.
Actual boundary selection remains external.

### 7.3 Atomic maps, support, and statistics

If an atomic law is a normalized quantum instrument—a family of completely
positive trace-nonincreasing branch maps summing to a trace-preserving map—its
one-shot weights and positive support are already fixed:

```text
p(r|C,kappa) = Tr(I_r(sigma_C)) / Tr(sigma_C),
support = {r : p(r|C,kappa) > 0}.
```

Counting exact normalized branch maps and the same trace statistics as two
independent atoms is double counting. If “branch map” instead means only a
normalized post-state transformation, the statistics row remains necessary.

An algebraic PVM menu can still exceed positive support. On prepared `|0>`,
the menu `{P_0,P_1}` has weights `{1,0}`. A separate
`FORMATION_ELIGIBILITY` clause is required only for an additional policy such
as menu completeness; generic state-independent menu completeness is false.

### 7.4 Continuation and concurrency

Gluing/exhaustivity is content; continuation is its transitive theorem.
Disjoint concurrency follows from generated tensor factors plus local maps.
Overlap order belongs to the event/readiness and gluing contract, unless a
continuous generator replaces discrete layering.

### 7.5 Formation, writing, and preservation

Keep record status/address/identity as content. With an exhaustive exact law:

- writing follows from branch output typing;
- formation follows from writing plus actuality; and
- preservation follows by checking every later allowed map against the
  selected record identity/sector.

If the listed operation family is not exhaustive, preservation remains an
independent premise.

### 7.6 Actuality and sampling

One-history actuality is independent of a normalized measure. The statistics
row should state the selection distribution; it should not repeat the claim
that one history exists. They may instead be bundled honestly as one sampled
kernel.

### 7.7 Projective extension and renewal

Both remain independent. Individually normalized finite laws can have
incompatible marginals, and preservation does not supply fresh capacity.

## 8. Corrected Ten-Core Dependency DAG

Under strict FD-SLIR typing, the minimum **conditional-law core** has ten
semantic inputs:

| id | core input |
|---|---|
| `C1` | `RAW_GENERATED_CARRIER`, including working/pointer factor typing |
| `C2` | `RECORD_STATUS_AND_IDENTITY`, including address or lineage semantics |
| `C3` | `EVENT_READINESS_LOCAL_CAUSAL_DOMAIN`, including allowed boundary class and finite-depth/no-Zeno semantics |
| `C4` | `PREDICTIVE_RECORD_DECODER`, including the chosen preparation/program/boundary instance and no hidden process state |
| `C5` | `CONTEXT_INTERVENTION_REPERTOIRE` |
| `C6` | `EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT`, including one-shot trace weights |
| `C7` | `GLUING_AND_EXHAUSTIVE_CONTINUATION` |
| `C8` | `ONE_HISTORY_ACTUALITY` |
| `C9` | `PROJECTIVE_FULL_LATTICE_EXTENSION` |
| `C10` | `RENEWAL_FRESHNESS_OR_EXPORT` |

The main derived nodes and arrows are:

```text
C5 + C6 + C7 + C9
    -> operational physical-equivalence quotient

C6
    -> one-shot weights and positive support

C6 + C7
    -> continuation

C1 + C6
    -> disjoint concurrency

C3 + C7
    -> overlap order

C2 + C6 + C8
    -> record writing and formation

C2 + C6 + C7
    -> record preservation

C1 + C3 + C6 + C7
    -> finite causal propagation in event steps
       when strict layers/no-Zeno are supplied

C6 + C7 + C9
    -> global history measure

operational quotient + C4 separation
    -> state=records theorem inside the model.
```

### Optional and external nodes

- `C11 FORMATION_ELIGIBILITY` is needed only if algebraic availability is not
  defined by instrument support or a menu-completeness policy is demanded.
- `E1 TRIAL_CORPUS` is the re-preparation/trial equivalence needed before an
  applicable frequency theorem.
- `B* ACTUAL_BOUNDARY_SELECTION` is a contingent input or meta-law needed only
  for unconditional cosmological prediction.

The resulting counts are deliberately conditional on typing:

- ten core law atoms under normalized-instrument and operational-quotient
  conventions;
- eleven if formation eligibility is independent;
- twelve when empirical trial semantics are also required;
- thirteen with both; and
- a fourteenth **framework input**, not a microscopic-law atom, only if the
  actual boundary is to be selected rather than conditioned upon.

This corrects the dependency graph. It does not prove that no deeper rule can
derive two core inputs together.

## 9. Exchange-Reduction Audit

The diagonal `SU(2)` commutant calculation is correct:

```text
commutant(U tensor U) = span{I,SWAP}.
```

The exact source runner passes its finite classification. The following
boundaries should nevertheless be explicit.

1. “Continuous reversible generator” should mean an autonomous,
   time-independent self-adjoint generator if the result is to leave one
   constant coefficient. Both `SWAP` and `(1+t) SWAP` have the same diagonal
   covariance pointwise.
2. The pair classification does not construct the infinite-lattice
   quasilocal automorphism or an exact causal cone. The nested-commutator
   control above exposes the continuous propagation tail.
3. A scalar pair identity is only a harmless global phase on a fixed active
   graph/sector. Record-conditioned active-edge counts can turn it into a
   relative phase.
4. The exact ground-sector reversal is: `+SWAP` has the one-dimensional
   singlet ground sector; `-SWAP` has the three-dimensional triplet ground
   sector. Checking only the minimum energy does not certify this reversal.
5. The Bell-capability control should compute the exchange-generated state’s
   four correlators, rather than only restating `2 sqrt(1+1)=2 sqrt(2)`.
6. Exchange still needs the separate pointer/status carrier identified in
   Section 1 before it can participate in record formation.

These are repairs to the interface and tests, not a defeat of the exchange
reduction.

## 10. Narrow No-Go Boundary

The bounded result is only that the named jobs cannot be silently merged
under the current FD-SLIR and exchange typings. Live routes include:

1. an exact-causal discrete exchange circuit;
2. a continuous exchange law with a proved Lieb-Robinson/quasilocal limit;
3. a larger pointer dilation with a supplied blank-boundary interface;
4. an operationally reconstructed quotient and state space;
5. a full joint law whose ergodicity makes frequencies a theorem; and
6. a more primitive global rule deriving carrier, decoder, or renewal content.

If “generator” already means autonomous, if causal diamonds are bookkeeping
rather than strict physical light cones, or if the full law defines its
operational quotient exhaustively, the corresponding attacks retire. No
global one-law route is declared closed.

## Verification

Run:

```bash
python3 scripts/full_law_inventory_adversarial_reduction_probe_2026_07_14.py
```

The PASS total contains related controls and is not an independent evidence
count.
