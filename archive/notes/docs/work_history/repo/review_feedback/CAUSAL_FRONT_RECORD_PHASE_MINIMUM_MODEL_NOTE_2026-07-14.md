# Causal-Front Record Phase: Minimum Model

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact finite conditional model used to test the
thought that a clock makes a record finally locked. It is not an axiom
proposal, an audit verdict, a Born-rule derivation, or a physical clock theorem.

## Result In Plain Language

The thought survives if “clock” means a **causal transaction phase**, not an
oscillator reading or a metric-time value.

A qubit can carry the two mutually exclusive locked contents `0` and `1`. It
cannot by itself also expose a third perfectly distinguishable status called
`open`. The missing occupancy bit—open versus locked—must live in the causal
history, a frontier/control state, another physical carrier, or an equivalent
law-level sector label.

The lean model is therefore:

```text
open causal phase
    -> one outcome is sampled and written
    -> history advances to locked, carrying record r
    -> later admissible operations preserve r.
```

The phase transition, sampling, writing, and operation restriction are one
joint commit event. In this exact sense the clock can be the lock: advancing
the causal-front closes the transaction and changes which future operations
are lawful. The phase does not choose the outcome or its probability.

In this model, phase monotonicity is stipulated as part of the continuation
law. A physical phase bit could otherwise be flipped. The finite graph below
derives nonreconnection **from that stipulated monotone law**; it does not
derive the law or a moving causal front from spatial Admissibility alone.

The minimum occupancy phase may be outcome-blind: it says only that the qubit
now carries a valid record, while the qubit carries `r`. If the outgoing front
has distinct orthogonal states `front-0` and `front-1`, it additionally carries
the outcome and is literally a second witness. These are different physical
models.

## Why One Bare Qubit Does Not Carry Three Readable Statuses

Perfectly distinguishable quantum states have orthogonal supports. Three
nonzero pairwise-orthogonal supports require dimension at least three, while
`M_2(C)` has Hilbert dimension two. The concrete proposed statuses

```text
open = |+>,    record-0 = |0>,    record-1 = |1>
```

make the issue visible: the locked states are orthogonal, while `|+>` overlaps
each by squared amplitude `1/2`.

This is not a contradiction in the live framework. Only records are readable;
an open site need not be a third local readout value. The rule can know that a
site is open from the record configuration or causal history. It does mean
that the quasilocal `M_2` algebra alone is not the whole record-status state;
the occupancy bit is carried by history/control semantics.

## Exact Joint Commit

For any predictive qubit state `rho`, use the sharp branches

```text
J_0(rho)=P_0 rho P_0,
J_1(rho)=P_1 rho P_1.
```

For `rho=|+><+|`, their trace weights are `1/2,1/2`; for a general `rho`, the
weights are its two pointer-basis diagonal entries. The physical law samples one branch,
appends the selected record, and changes the history phase from `open` to
`locked` with content `r`. A repeat read then returns `r` with certainty.

The paired runner implements this as a hybrid quantum/classical instrument
returning `(locked, r, post-state)`. Its explicit seed is the stipulated
actuality input; tuple construction is not offered as a derivation of one
actual outcome.

The Lüders branch form can be reduced from sharp rank-one effect plus exact
repeatability. The normalized trace law, the prepared-state link, and the
instruction that one branch is actual remain physical content. This model
uses them openly; it does not derive Born sampling from the clock phase.

## Three Different Meanings Of “The Clock Locks It”

1. **Outcome-blind tick.** A clock changes phase while the source remains
   unsettled. No outcome has been written. This is not a lock.
2. **Reversible correlation.** A controlled unitary correlates source and clock
   labels. The complete unitary reverses exactly. This is a timestamp/witness,
   not objective commit by itself.
3. **Causal-front commit.** The law samples and writes one outcome while moving
   from the open operation domain to the record-preserving domain. This is a
   real lock, because its definition includes the future-operation restriction.

Earlier clock probes ruled out meanings 1 and 2 as universal formation
mechanisms. They did not rule out meaning 3; meaning 3 is simply a precise
sampled continuation law rather than a clock slogan.

If the front is required to be a second outcome witness, the exact unitary map

```text
|s>|0>|front> -> |s>|s>|front-s>,       s in {0,1},
```

takes a superposed source to a GHZ state. Both witness copies are then
orthogonal and perfectly correlated, but the global state still contains both
amplitudes and the map reverses exactly. Two witnesses can certify redundant
classical readability after selection; they still do not supply selection.

## Bare-Metal State Graph

At the record level:

```text
                 R0 -> R0+future -> ...
open transaction
                 R1 -> R1+future -> ...
```

`R0` and `R1` never return to open and never reconnect. That nonreconnection
comes from the changed continuation/operation domain, not from having two
witness devices. The frontier orders events, but any monotone reparameterization
can assign different durations to the same order. Metric time and lapse remain
downstream.

The exact locked operation contract is not the four example unitaries in the
runner. For a record projector `P_s`, every declared future channel must obey

```text
Phi*(P_s)=P_s,
```

or the appropriate one-way branch-absorption condition when open-to-record
inflow remains possible. In the two-sided case every Kraus operator is block
diagonal in the record decomposition; such channels are closed under
composition. Nondemolition read interactions have controlled form
`sum_s P_s tensor U_s` and preserve the record algebra. This operation class
is supplied or derived by the exact law—it is not forced by a phase label.

The model does not require a third onsite level. It does require the complete
state supplied to the law to include record presence/history, not merely the
instantaneous qubit density matrix. This fits `A state is a configuration of
records` only if complete record configurations determine the causal phase,
preparation/process memory, and every future transcript law.

A dynamically relevant phase therefore cannot be a hidden annotation on the
past. It must be recoverable from the present record/front configuration. If
two histories have the same present record configuration but different phase
labels and different lawful futures, the complete state is history-dependent
and the live `state = records` qualification fails its own predictive test.

## What It Retires And What It Does Not

The model retires several drafting temptations:

- no primitive reader device or fixed witness-count trigger is required;
- no separate onsite `open` basis state is required;
- the clock need not be a second copy of the outcome; and
- permanence follows once the locked-phase operation algebra is supplied or
  derived.

It does not select:

- when and where a transaction becomes ready;
- the exact context/instrument or prepared predictive state;
- the outcome weights, one actual sample, or trial-frequency theorem;
- a metric clock rate or universal lapse response;
- fresh record export/renewal;
- matter, interactions, continuum control, or gravity.

Those items must be entries or theorems of the exact law reference. The causal
phase is a useful unification of readiness, write, and post-write operation
scope; it is not a substitute for the exact law value.

## Constitutional Consequence

This result changes the language target in one important way. Do not say
simply “a clock locks the record,” because ordinary clock readings and
reversible timestamps fail. The substrate idea worth preserving is:

> formation is the causal-phase transition after which the selected recorded
> distinction is invariant under every lawful continuation.

That remains target semantics, not locked axiom prose. If the eventual law
derives the phase transition and invariant continuation sectors, Record needs
no new trigger clause. If it does not, the exact transition belongs in the
law specification referenced from Admissibility, while Record states only the
irreducible meaning of permanence.

## Verification

Run:

```bash
python3 scripts/causal_front_record_phase_minimum_model_probe_2026_07_14.py
```

The PASS total contains related checks and is not an independent evidence
count.
