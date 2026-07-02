# AC_phi_lambda Pointer-Labeled Refinement And The Finer-Record Doublet Clock
**Date:** 2026-07-02
**Claim type:** bounded theorem / registrable refinement + exact record-map algebra
**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_pointer_labeled_refinement_finer_record_clock_2026_07_02.py`](../scripts/acphilambda_pointer_labeled_refinement_finer_record_clock_2026_07_02.py)

## Claim
On the supplied C3 generation surface, let `C` be the 3-cycle shift and let `omega = exp(2 pi i/3)`.
The character basis vectors `|chi_k>` diagonalize `C`; `chi_0` is the singlet distinguished by `S = C + C^2`, and `{chi_1, chi_2}` is the doublet.
For
```text
H(a, |b|, delta) = a I + b C + conj(b) C^T,
b = |b| exp(i delta),
```
the pointer-labeled spectral identities are
```text
lambda_singlet - a = 2 |b| cos delta,
lambda_d1 + lambda_d2 - 2a = -2 |b| cos delta,
|lambda_d2 - lambda_d1| = 2 sqrt(3) |b| |sin delta|.
```
Thus the labeled data determine `(a, |b|, cos delta, |sin delta|)`; the pointer-labeled registrable content is `|delta|`: the distinguished singlet removes the `2 pi/3`-relabel quotient of the bare multiset.
For the finer character-basis record
```text
D_chi(rho) = sum_k P_k rho P_k,
P_k = |chi_k><chi_k|,
```
all `P_k` commute with every Brannen-form `H`.
The map is trace-preserving and idempotent, refines `D_S`, erases the `chi_1`-`chi_2` coherence in one application, and leaves all character occupancies invariant.
Under the pre-record step reconstruction
```text
U = exp(-i H),
rho_12 -> exp(i (lambda_d2 - lambda_d1)) rho_12.
```
Hence the within-doublet phase advances by exactly `2 sqrt(3) |b| sin delta` per native step.
The registrable magnitude is `2 sqrt(3) |b| |sin delta|`.
Off-locus capability is manifest: the K-real locus is exactly the zero-clock set.

## Frame And Retained Inputs
All claims live on the supplied record-formation frame of the retained record-preservation row: the Stage-1 forced form, the einselected pointer, and the quantum-Darwinism record reading marked there as a supplied bridge.
Nothing here is an axiom-level record claim.
The three dependency links are:
- [`BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md`](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md) supplies the `circulant form` and the `(a, |b|, delta)` sector dial.
- [`RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md`](RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md) supplies `D_S`, "dephasing onto `{P_singlet, P_doublet}`", the pin "only a finer character-basis record would touch it", and the pin "The couplings (a, |b|, delta) are the supplied sector dial".
- [`KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md) supplies the degenerate-stationary precedent: "its stationary candidates are degenerate".
In-flight context, not dependency links:
PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`;
PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`;
PR #4789 `ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`;
PR #4790 `ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01`;
PR #4794 `ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02`.

## Pointer-Labeled Registrable Refinement (W6-A)
The runner convention is `C |chi_0> = |chi_0>`, `C |chi_1> = omega^2 |chi_1>`, and `C |chi_2> = omega |chi_2>`.
The singlet is `chi_0`.
The ordered doublet used for the positive-rate formula is `(d1, d2) = (chi_2, chi_1)`.
The exact labeled identities are:
```text
lambda_singlet - a = 2 |b| cos delta,
lambda_d1 + lambda_d2 - 2a = -2 |b| cos delta,
(lambda_d2 - lambda_d1)^2 = 12 |b|^2 sin^2 delta.
```
Equivalently, `|lambda_d2 - lambda_d1| = 2 sqrt(3) |b| |sin delta|`.
The sign depends on the ordered doublet labeling; the magnitude does not.
This refines, and does not contradict, PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`.
That row is scoped to the unordered spectrum "from spectrum alone".
Here the singlet is distinguished by the pointer, so the `2 pi/3` relabel quotient of the bare multiset is removed at the labeled resolution.

## Finer Character-Basis Record: Exact Action (W6-B)
Let `P_k = |chi_k><chi_k|` and `D_chi(rho) = sum_k P_k rho P_k`.
(i) `[P_k, H] = 0` for every `k` and every `(a, |b|, delta)`.
The finer record is non-demolition for every Brannen-form generator and refines the einselected frame.
(ii) `D_chi` is trace-preserving and idempotent, and
```text
D_chi D_S = D_S D_chi = D_chi.
```
(iii) One application of `D_chi` sets the within-doublet coherence exactly to zero:
```text
<chi_1| D_chi(rho) |chi_2> = 0,
<chi_2| D_chi(rho) |chi_1> = 0.
```
At the same time,
```text
<chi_k| D_chi(rho) |chi_k> = <chi_k| rho |chi_k>
```
for all `k`.
At this resolution the finer record erases the within-doublet phase in one shot and converts the registered state data to occupancies.

## The Doublet Clock (W6-C)
The step unitary `U = exp(-i H)` is a pre-record reconstruction device.
The phase is counted per native step; no time metric is imported.
For `(d1, d2) = (chi_2, chi_1)`,
```text
rho_12 -> exp(i (lambda_d2 - lambda_d1)) rho_12,
lambda_d2 - lambda_d1 = 2 sqrt(3) |b| sin delta.
```
The doublet-internal rate is the delta-carrying rate.
Character occupancies are invariant under the unitary.
Singlet-doublet coherences rotate at rates `lambda_singlet - lambda_di`, already labeled-spectrum data from W6-A.
Consequently, `delta` enters state-level dynamics as an `R`-valued phase-accumulation rate on the doublet: an angle-native slot, phase per native step, capable of being off-locus.
Off-locus means `sin delta != 0`, equivalently a nondegenerate doublet and a nonzero clock rate.
The K-real locus is exactly the zero-clock set.
The retained modulus row's degenerate stationary points are the dial settings where the doublet clock stops.
Exactly, `sin(0) = 0` and `sin(pi) = 0`.
At `delta = 2/9`, the inequality `0 < 2/9 < pi` gives `sin(2/9) != 0`, so the clock runs.
The finer-record event erases the accumulated phase.
Between events the same exact rate re-accumulates.
This is only the map-level alternation; no occurrence statistics are asserted.

## Wall Relocation And Non-Evasion (W6-D)
Reading `delta` from the clock still needs the `|b|` unit.
The rate is `2 sqrt(3) |b| sin delta`.
Rescaling `|b|` rescales the rate.
Thus PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01` applies verbatim to the clock normalization.
The value equation `delta = 2/9` becomes:
```text
doublet clock advance per native step = 2 sqrt(3) |b| sin(2/9).
```
That value is still underived.
What moves is the identity-unit wall into a dynamical, angle-native, K-breaking-tied slot: doublet phase per native step on the retained record-formation frame.
Named next paths:
(a) a same-surface theorem fixing the splitting-to-`|b|` ratio, namely the dimensionless clock rate `2 sqrt(3) sin delta`, since pinning it pins `|delta|`;
(b) the record-occurrence lane, in-flight context only, for what finer-record event statistics register.

## What This Moves
| Before | After |
|---|---|
| Registrable resolution `cos(3 delta)` (bare) | `|delta|` (pointer-labeled) |
| `delta` as static coupling label | `R`-valued phase-accumulation rate, an angle-native dynamical slot |
| K-real locus as algebraic condition | zero-clock set as physical map condition |
| "degenerate stationary" in the modulus row | stopped clock |
| Beyond-spectrum requirement from PR #4794 | satisfied by the labeled, record-facing layer |

## What Does Not Move
- The value `delta = 2/9` is not derived.
- The `|b|` unit remains free.
- Occurrence statistics are not addressed.
- Decoherence is not derived.
- `r` is not forced; it remains a registered dial.
- Readout selection remains open under `W_defect_readout_selection`.

## Audit Consequence If Retained
Rows may cite the labeled refinement and clock algebra as exact reconstruction-layer facts on the retained frame.
The value wall citation is unchanged: `W_defect_identity_unit` / `W_cycle_holonomy_value` / R-eta (ii) one dependency.
The cited fact is narrow: the labeled record-facing layer upgrades the registrable content from bare `cos(3 delta)` to `|delta|`, and the finer record-map algebra identifies the doublet phase rate.
It does not determine the numerical value or the normalization unit.

## Non-Claims
- No axiom-level record claim; the quantum-Darwinism reading is a frame-supplied bridge.
- No occurrence/Born/probability content.
- No decoherence derivation.
- No derivation of `delta` or `r`.
- No additional wall label.
- No contradiction of PR #4788; the scopes are layered.
- No time-metric import; steps are the native reconstruction unit.

## No-Go Discipline Gate
**Status:** PASS for bounded refinement + exact map algebra; not a terminal no-go.

### N1
Alternative route enumeration:
bare-spectrum route, superseded at labeled resolution, PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`;
spectral-functional route, ruled out by PR #4794 `ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02`;
pointer-labeled refinement, ATTEMPTED here and succeeds, giving `|delta|`;
finer-record map algebra, ATTEMPTED here and exact;
clock-rate normalization, OPEN, the relocated wall;
occurrence-statistics route, OPEN and separate;
owner primitive, GOVERNANCE.

### N2
No additional wall is introduced.
The value wall is relocated into the clock normalization with the same single dependency.

### N3
Hidden-wall scan:
`einselected partition` is supplied by the retained frame, not derived;
`quantum-Darwinism record reading` is a supplied bridge of the retained row.
Identification checkpoint: the finer record is a reconstruction-layer refinement on that same supplied frame, not a licensed axiom-level record.
`native step` is a scale-reference reconstruction unit with no metric.
`clock` is a map-level alternation label with no occurrence claim.

### N4
Residual matching:
PR #4788 is layered with this note rather than contradicted;
PR #4789 gives zero-clock equals locus;
the modulus row gives degenerate equals stopped clock;
PR #4794 asks for a beyond-spectrum layer, met here by the labeled layer;
PR #4783 persists on the rate because rescaling `|b|` rescales it.

### N5
The proven sentences are exact 3x3 map and spectral identities on the supplied frame.
They are not claims about record occurrence, Born weights, or decoherence.

### N6
Live paths:
fix the dimensionless clock rate `2 sqrt(3) sin delta` by a same-surface theorem;
study occurrence-lane statistics separately;
or supply an owner primitive.

### N7
Steelman:
"the clock is a reconstruction artifact; nothing physical accumulates between records."
Reply: correct, it is reconstruction-layer and stated as such.
Its value is that the delta-slot's type is now fixed as an `R`-valued per-step rate tied to K-breaking.
The labeled refinement is registrable-level because the partition content is record-delivered on the retained frame.
The zero-clock, locus, and degeneracy identification unifies three landed structures.
Concession: no value is derived, and occurrence is untouched.

### N8
Echo:
representative-vs-invariant and static-vs-dynamical relocations recur in the holonomy waves and theta arg-det setting.
Uniform lesson: fix the slot's type first, then derive its value.

## Verification
Run command:
```bash
python3 scripts/acphilambda_pointer_labeled_refinement_finer_record_clock_2026_07_02.py
```
Measured expected close:
```text
TOTAL: PASS=110 FAIL=0
```
