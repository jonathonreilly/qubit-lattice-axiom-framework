# Physical source-to-clock-response law tournament — Cycle 431

Date: 2026-07-19
Authority: none
Audit: unset

## Result

Cycle 431 constructs a positive competing-law result on one declared physical common code. The common input is the Cycle-425 periodic Q1 hard-core scalar field, inheriting the Cycle-426 physical occupation boundary, tensor the Cycle-428 sixteen-M2 one-hot oscillator and a blank fifteen-M2 control rail.

After the same fixed three-sweep oscillator baseline, two reversible hypotheses act:

- the **delay law** applies one or two occupation-controlled inverse oscillator sweeps;
- the **advance law** applies one or two occupation-controlled forward oscillator sweeps.

The local scalar-field occupation M2 coherently controls the circuit through an occupation-controlled Fredkin schedule. No expectation or host branch controls a gate. Both laws take exactly the same source, evolved field, clock word, local target, event identity, and response strength. Neither law is selected.

For the training input—periodic L=5, the Cycle-425 reservoir source seed evolved to a one-edge target, response strength one, and initial clock position 2—the free word is position 5. In the occupied local-field sector the delay law predicts position 4 and the advance law predicts position 6. Their dimensionless clock-word displacement candidates from the initial word are therefore 2 and 4. The same physical occupation coordinate has weight

```text
sin(theta)^2 / 6 = 0.02098320268811897.
```

This weight quantifies the coherent event sector; it is not an occurrence, probability, or Born law.

## Bounded physical circuit

The selected field M2 is adjacent to a fifteen-M2 blank control rail. A fixed nearest-neighbor CNOT fan copies its computational-basis control along that rail. Each rail M2 controls the neighboring pair of the sixteen-M2 oscillator through one connected three-M2 Fredkin primitive. The response sweep is repeated once or twice according to the supplied strength, then the fan is reversed.

Each primitive has support at most three M2 and diameter at most two; every three-site support is a connected nearest-neighbor path. The active installation fits a fixed `17 x 2 x 1` box. The response circuit is an exact basis permutation. Its inverse uses the opposite controlled sweep, field occupation is unchanged, oscillator Hamming number remains one, and all fifteen blank rail M2 return to zero. The layout and support audit passes in all 24 proper-cubic frames.

The common three-sweep baseline is candidate-law content, not three units of physical duration. Response sign and response strength are supplied. The circuit is bounded for the declared strength domain `{1,2}`; no claim is made that this is a unique or minimum coupling.

On the declared common code `Cycle425 cubic Q1 field x Cycle428 one-hot clock`, the executable checks 128 logical control/clock columns spanning both occupation sectors, all sixteen clock words, both laws, and both strengths. The maximum forward E/G residual in

```text
E G_logical = G_physical E
```

is exactly `0.0`; the maximum basis inverse residual is `0.0`. The maximum field-Q residual, clock-Hamming residual, blank-rail cleanup residual, and 24-frame support-covariance residual are each `0.0` on this operator-level control.

## Transient tournament

The predeclared cases are:

| case | periodic size | target distance | response strength | occupied-sector weight |
|---|---:|---:|---:|---:|
| training | L=5 | one edge | 1 | `0.02098320268811897` |
| held size | L=9 | one edge | 1 | `0.02098320268811897` |
| held distance | L=9 | two edges | 1 | `0.0023314669653465544` |
| held strength | L=9 | one edge | 2 | `0.02098320268811897` |
| held joint | L=9 | two edges | 2 | `0.0023314669653465544` |

For strength one and initial position 2, occupied branches predict delay/free/advance positions `4/5/6`. For strength two they predict `3/5/7`. The delay-versus-advance joint-state residual is exactly the expected `sqrt(2 w)` for the relevant occupied-sector weight because the two laws put that sector in orthogonal complete clock words while leaving the same unoccupied sector at the free word.

The full update applies the Cycle-425 field evolution and then the response permutation. Reversing the response and applying the Cycle-425 adjoint returns the common input with maximum residual `3.237200381486609e-16`. The maximum field-Q and clock-Hamming ledger residuals are both `2.220446049250313e-16`. The maximum all-24-frame transient occupation covariance residual is `0.0`. Source deletion, coupling deletion, and clock deletion each give delay-versus-advance state residual `0.0`; source deletion also gives zero event-sector latch weight.

No counter step is called time. Update count and eigenphase are not time or a rate.

## Stationary dressed input

The same two laws are also evaluated on the supplied Cycle-425 stationary dressed input at L=5 training and held L=9. The selected local component weights are approximately `0.003151434407904416` and `0.0026621256376302325`. The common field update preserves those component weights because the selected state is an eigenstate. With initial position 7 and strength one, the delay and advance occupied sectors latch positions 9 and 11.

The stationary eigenstate and its preparation are supplied. Eigenphase is not time or a rate, and no eigenphase-to-clock calibration is used.

## Event/Record boundary

The Cycle-428 event/Record latch boundary is explicit. In the occupied field sector, the same event identity is coherently latched with the complete predicted clock word before a Cycle-364 candidate commit. The delay and advance hypotheses therefore bind different physical clock words to otherwise matching candidate inputs. In separate hypothesis evaluations both Cycle-364 immediate candidate attempts form; this does not select either source-to-clock law or the Cycle-364 formation law.

The latch has an exact inverse. A reversible latch is not a Record. An unoccupied field branch leaves the valid latch blank and the conditional Record attempt blocked. Candidate formation, Record occurrence, empirical selection, and frequency remain open.

## Dimensionless response and receiver typing

The only response exported is a complete clock word plus fine, pair, and quartet partition displacements decoded from that same physical word. These are dimensionless clock-word displacement candidates. Wrapped outputs are refused as within-epoch intervals; parity aliases with offset two remain distinct in the complete word.

Cycle-416 and Cycle-420 matching coordinates are used narrowly:

- the Cycle-416 physical source/mediator angle equals the Cycle-425 hard-core angle to numerical precision;
- Cycle 420’s matching coordinate is positive hard-core field occupation, with total first-emission occupation `sin(theta)^2 = 0.12589921612871371` and the selected one-edge component one sixth of that;
- Cycle 420’s signed-density and signed phase-bearing amplitude/history coordinates are not imported;
- the Cycle-416 candidate dependency graph is not promoted to an actual clock or metric receiver.

Metric, lapse, proper-time, and Lorentz flags remain false. No metric time, rate, lapse, proper time, Lorentz structure, or gravitational response is derived.

## Controls and supplied structure

The executable checks exact inverse, field-Q and clock-Hamming ledgers, blank control rail cleanup, bounded/nearest-neighbor support, all 24 proper-cubic frames, transient source seed, stationary dressed input, periodic L=5 training and held L=9, held distance and response strength, source, coupling, and clock deletions, and alias, wrap, and lawful-domain controls.

The coupling, initial phase, response sign and strength, unit, calibration, formation law, occurrence, and empirical selection remain supplied or open. Also supplied are local-site choice, source preparation, three-sweep baseline, stationary-state preparation, nonwrap epoch, event identity, blank sidecar, and Record-payload binding.

Field occupation is not energy, source, stress, or a Born weight. It is not physical source strength, work, force, or a universal metric source. Pointer copying is not Record formation. Candidate formation is unselected.

This is a positive competing-law result. No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made. No axiom, foundation, Qualification, primitive, registry, policy, queue, or audit-status surface is edited.

## Disposition

The physical substrate now supports two distinct, local, reversible, falsifiable source-to-clock response hypotheses with exact different latched-word predictions on identical inputs. The tournament does not decide between them. Experimental calibration and a selected occurrence/Record law would be required before either candidate could become an operational clock-response law.
