# Local relational late detector — Cycle 208

Date: 2026-07-16

Status: finite conditional readout construction; audit unset

Authority: none

Companion runner:
`scripts/local_relational_late_detector_cycle208_2026_07_16.py`

This note and runner live only on the draft parking branch and draft PR #5389.
They change no foundation, axiom, primitive, registry, policy, audit, or queue
surface.

## Attribution boundary

The two-particle bound-state engine remains prior work of Bisio, D'Ariano,
Perinotti, and Tosini:

<https://doi.org/10.1103/PhysRevA.97.032132>

The simplified two-particle derivation and simulations are due to Bisio,
D'Ariano, Mosco, Perinotti, and Tosini:

<https://doi.org/10.3390/e20060435>

The cited papers supply and solve the two-particle Thirring walk and its bound
states. This repository calls the selected localized bound-state packet a
“molecule.” The third carrier, fixed-total-momentum scattering extension, and
this detector tournament are additions relative to those papers. No broader
novelty claim is made.

## Result up front

Cycle 207 used a supplied momentum-space instrument to distinguish
transmitted, reflected, and breakup channels. Cycle 208 replaces that Fourier
classification with one local relational partition at tick 70.

Write

```text
r = x_first - x_second,
q = 2 x_projectile - x_first - x_second.
```

The three record alternatives are

```text
T_local: abs(r) <= 2 and q < 0,
R_local: abs(r) <= 2 and q > 0,
X_local: every remaining basis state.
```

The predicate is pair-exchange invariant: swapping the two identical
fermions sends `r` to `-r` and leaves `q` unchanged. The alternatives are
disjoint and exhaustive, use the same radius and readout tick for every
coupling, and contain no Fourier transform or protocol-output lookup.

At the strong reference collision, the local distribution is approximately

```text
(T_local, R_local, X_local)
  = (0.929619, 0.023928, 0.046452),
```

versus the exact spectral distribution

```text
(T, R, X) = (0.926629, 0.023951, 0.049420).
```

The largest absolute difference is about `0.00299`. The same fixed local
rule differs by about `0.00164` for the weak collision and `0.00310` for the
deleted-collision control. All local alternatives are positive and normalize
to one.

This removes the global spectral basis from the outcome label. It does not
yet derive a detector or record.

## Record-conditioned mass

Conditioning on `T_local` gives a state that is more than 99.6% intact
transmitted molecular channel for the weak collision and more than 99.1% for
the strong collision. Its molecular momentum coherence remains above `0.998`.

The conditional secant masses are approximately

| collision | local-`T` mass | Cycle-205 curvature/inertial mass | relative difference |
|---|---:|---:|---:|
| `eta=0.03 pi` | 0.95705 | 0.95013 | 0.73% |
| `eta=0.06 pi` | 0.96302 | 0.95013 | 1.36% |

The loss relative to Cycle 207's spectral branch is the finite resolution of
the position partition: a local half-space record is not an exact momentum
eigenchannel. It nevertheless preserves the operational mass bridge within a
declared percent-level resolution.

As before, the band velocity is not an independent second inertia
measurement. Cycle 205 supplied the independent `F/a` calibration; this probe
shows that a locally recognizable scattering outcome selects the same matter
sector.

## Deletion, timing, and redundancy

With the collision phase deleted, the local rule gives more than 99.6%
transmitted and less than 0.2% in either false-reflected or unresolved output.
Those finite tails are explicitly retained rather than rounded to zero.

The discrepancy from spectral channels falls from tick 64 to fixed tick-70 for the
deleted, weak, and strong trajectories. A later tick is not monotonically
better on a finite ring because packet tails eventually wrap. Tick 70 is
therefore a supplied operational readout time, not a derived clock event.

Appending a second correlated copy of `T_local/R_local/X_local` leaves the
three probabilities unchanged. The outcome record is not the molecule and
does not add mass.

## What remains imported

The local relational partition is a readout specification, not yet a physical
apparatus. It asks for pair closeness and the projectile's side relative to
the pair center at one supplied tick. A microscopic implementation must build
those comparisons from onsite and nearest-neighbour interactions, carry the
reference frame with the recoiling molecule, and append an irreversible
record without later feeding back.

Thus the supplied projective readout is smaller than Cycle 207's spectral
import but remains an import. Nearest-neighbour detector dynamics remains
open, as do the formation event, occurrence probabilities, and repeated-run
frequencies.

## Cross-lane effect

### O — operational quantum

One fixed phase-insensitive local geometry now approximates the exact quantum
channel instrument and selects an intact coherent future. This is a useful
route-D plus readout witness for Cycle 200, but it is not route-complete: the
record configuration does not yet generate the working state or detector,
and record-only, decoder, relational-history, and boundary-memory routes
remain live.

### T — time

The outcome stabilizes only in a late separation window. The test exposes the
physical task for the clock lane: generate an arming/readout event from local
process state rather than name tick 70 externally. Quasiphase composition also
remains open.

### I — matter

Generated scattering, intact-object recognition, and record-conditioned mass
now survive a local relational readout rather than requiring momentum-space
postselection. The construction remains a supplied species with supplied
couplings and incoming sector.

### G — gravity

The local `T/R/X` alternatives offer a position-space matter ledger for a
future source law. No source current, lapse, tensor response, or universal
coupling is generated.

### B — boundary

The initial state, readout tick, comparison radius, and record operation are
prepared. Boundary/history dynamics must generate an apparatus and its timing
without tuning them to the coupling.

## Next construction

Compile the `abs(r)<=2` and sign-of-`q` comparisons into a finite moving
detector made of actual local roles or qubits. Its arming event should be
triggered by separation/contact history, its record should remain permanent,
and it should reproduce the same distribution without a host-side tick or
relative-coordinate calculation.

## Scope boundary

This is a finite one-dimensional conditional detector result. The
proper-cubic lift remains open. It is not nearest-neighbour apparatus
dynamics, record formation, a Born-frequency theorem, an empirical detector
or particle prediction, a gravity result, or a route-complete ontology test.
It makes no broad no-go or minimum-content claim and supports no axiom
conclusion.
