# Physical detector-event to Record-clock-map candidate — Cycle 428

Date: 2026-07-19
Authority: none
Audit: unset

## Result

This cycle constructs a positive, fixed bounded candidate bridge from the Cycle-424 physical detector event sector to matched conditional Record endpoints carrying a physical recurrent clock word. It does not select a Record formation law and does not claim a metric theory of time.

The clock is a sixteen-M2 one-hot oscillator on a nearest-neighbor path. One fixed nearest-neighbor SWAP sweep advances its complete clock word by one position modulo sixteen, and the reversed sweep is the exact inverse. The code space is the one-excitation sector. The full sixteen-bit word distinguishes the offset-two alias that defeats a one-bit phase label. The transition from position 15 to 0 is explicit; wrap refusal is enforced unless a supplied epoch transition is added.

A reversible detector-controlled latch occupies a fixed `22 x 3 x 1` cubic-lattice box including the detector. A 21-M2 blank bus fans out the detector control. Sixteen connected three-M2 controlled gates copy the complete physical clock word, four copy a local four-M2 event identity, and one copies a valid bit into blank sidecars. The bus is then uncomputed. The fixed latch has 63 primitives, support at most three M2, support diameter at most two, and an exact reversed inverse. The complete auxiliary inventory is:

- 16 physical oscillator M2;
- 4 physical event-identity input M2;
- 21 blank bus M2;
- 16 blank latched-clock M2;
- 4 blank latched-identity M2;
- 1 blank valid M2.

Thus one active latch uses 62 physical M2 with constant overhead: 41 reusable oscillator/identity-input/bus M2 and a fresh blank endpoint sidecar of 21 M2. Retaining three endpoint sidecars while reusing the active oscillator, identity input, and uncomputed bus requires 104 M2. Fresh blank endpoint sidecar provisioning and its Record-relative placement remain supplied; the runner does not conceal them in the 30-M2 Record payload. Every active-layout and locality statement is checked under all 24 proper-cubic frames. The reversible detector-controlled latch runs before candidate commit. A reversible latch is not a Record.

## Conditional Record and clock map

The immediate candidate adapter is the Cycle-364 immediate site-tethered candidate. It is used conditionally and the candidate formation law is not selected. At each event the physical latch is complete before the candidate commit. The resulting immutable sidecar is bound to the candidate Record by an explicit supplied event-to-payload adapter; the 30-M2 Record payload does not secretly derive that binding.

Three matched endpoint Records are formed on the declared candidate branch. The complete endpoint match requires:

- a valid complete clock latch;
- distinct nonzero physical event identities;
- identical supplied oscillator, detector-device, and epoch identities;
- lawful typed permanent Cycle-364 candidate Records;
- a forward, non-wrapping oscillator position order.

The direct full-identity/full-content boundary from Routes 344–346 and Cycle 347 is preserved. Reusing a physical identity with altered content fails. A missing latch, changed device, changed epoch, or wrapped endpoint fails rather than decoding as a zero interval.

For training positions `(1,5,13)` and a held initial-phase-shifted set `(2,6,14)`, the matched dimensionless interval words are:

| endpoint interval | fine cells | pair-cell refinement | quartet-cell refinement |
|---|---:|---:|---:|
| 1 -> 2 | 4 | 2 | 1 |
| 2 -> 3 | 8 | 4 | 2 |
| 1 -> 3 | 12 | 6 | 3 |

The refinement ratios are exactly 2 and 4 and additivity is exact at every resolution. Pair-cell and quartet-cell refinements are physical partitions decoded from the same latched sixteen-M2 word, not separate host tick streams. These integers are a dimensionless interval candidate only.

The explicit event-to-Record edges are `detector-event-1 -> Record-1`, `detector-event-2 -> Record-2`, and `detector-event-3 -> Record-3`. The detector events and coherent latches are precommit candidates, not Records. Appending the three conditional Records to the Cycle-255 local dependency fixture gives Record depths 5, 6, and 7; deletion of those edges changes that dependency statement. The DAG remains nearest-neighbor and depth-preserving in all 24 proper-cubic frames. Post-commit overwrite is rejected by the inherited Cycle-364 candidate law.

## Physical update and calibration

The common fixed sequence is:

1. the Cycle-424 physical field/detector update;
2. one fixed oscillator SWAP sweep;
3. the reversible detector-controlled latch;
4. only then, on the conditional candidate branch, a Cycle-364 commit attempt.

The physical detector/source Q ledger is preserved to `4.44e-16`, as in Cycle 424. The one-source and two-source valid-latch sector weights both reproduce `sin(theta)^2/6 = 0.020983202688118967` (computed values `0.02098320268811897` and `0.020983202688118974`). Detector deletion gives zero valid-latch weight. Reversing latch, oscillator, and field/detector update gives one-source and two-source residuals `1.1443916996305594e-16` and `3.508775736563311e-16`. Auxiliary latch bits are not assigned the inherited field-Q meaning.

The separate Cycle-425 calibration uses the same fixed physical cubic update with an added local reversible detector SWAP:

- on periodic L=5 training and held L=9, a one-edge detector after one update has sector weight `0.02098320268811897`;
- a two-edge detector after one update has exactly zero sector weight;
- the same two-edge detector after two updates has sector weight `0.0023314669653465544 = (sin(theta)^2/6)/9`;
- total norm is one to `2.22e-16`; sparse inverse residuals are `1.595611289212673e-14` on L=5 and `3.84990794981243e-14` on held L=9; vertex or stream deletion gives zero one-edge detector response;
- the weights agree across all 24 proper-cubic frames.

This is one-edge and two-edge propagation calibration on periodic L=5 training and held L=9. It is a conditional event-sector transfer check, not arrival selection, propagation speed, physical duration, or a time-of-flight law. Update count is not time.

## Exact controls

The executable checks:

- all `2^16` clock basis words for inverse and Hamming-number preservation;
- all 512 lawful detector/position/identity latch inputs for exact inversion, blank-bus restoration, and false-trigger behavior;
- the full 16-position recurrence, a deleted clock SWAP, latch-gate deletions, malformed clock words, and the explicit wrap;
- Cycle-424 one-source/two-source detector weights, field-Q ledger, detector deletion, and common-update inverse;
- matched Record endpoint integrity, held phase shift, exact refinement ratios, interval additivity, wrap/device/epoch/latch refusals, DAG locality/depth, covariance, and overwrite rejection;
- Cycle-425 one-edge/two-edge transfer, held-size transfer, inverse, norm, deletions, false trigger, and all-frame covariance.

## Bridge hypothesis and firewall

The clock transition is a physical recurrent degree of freedom but its coupling, initial phase, word interpretation, unit, and calibration remain supplied. Also supplied are oscillator/device/epoch identities, local event identities, fresh blank endpoint sidecar provisioning and placement, their binding to Record payloads, and applicability of the Cycle-364 formation hypothesis.

Candidate formation is unselected. Detector-sector weight is not occurrence, probability, or a Born weight. Reversible detector absorption and pointer copying do not actualize a Record. The construction derives neither Record selection nor an occurrence distribution.

There is no metric time, rate, proper time, lapse, or Lorentz claim. In particular, the oscillator transition is not called a rate, the field update count is not time, and the dimensionless interval word has no unit until a separate physical clock calibration is supplied.

The Cycle-424 `(2,0,2)` threshold geometry remains route-specific and is not used as a general geometry law here. No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is made.

## Disposition

This is a constructive bridge candidate: physical recurrent oscillator plus coherent detector latch plus conditional matched Record endpoints gives an exact dimensionless, additive, refinement-consistent clock map on its declared non-wrapping domain. It closes neither the formation/selection law nor the physical unit/calibration import. Authority remains none and audit remains unset.
