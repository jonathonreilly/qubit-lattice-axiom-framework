# AC_phi_lambda Fluxed-Ring Spectral-Functional Route No-Go

**Date:** 2026-07-02
**Claim type:** no_go
**Scope:** bounded spectral-functional route no-go plus spectral reduction theorem.
**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_fluxed_ring_spectral_functional_route_no_go_2026_07_02.py`](../scripts/acphilambda_fluxed_ring_spectral_functional_route_no_go_2026_07_02.py)

## Claim
On the fluxed `N`-ring with cycle shift `C_N`,
```text
H_Phi = exp(i Phi/N) C_N + exp(-i Phi/N) C_N^T
L_Phi = 2 I - H_Phi
```
the flux enters the fluxed-ring characteristic polynomial only through the constant term, as `2 cos Phi`.

Equivalently, the eigenvalue multiset is controlled by `cos Phi`, while the non-constant elementary spectral faces are flux-blind:
```text
spec(H_Phi) = { 2 cos(Phi/N + 2 pi k/N) : k = 0,...,N-1 }
spec(L_Phi) = { 2 - 2 cos(Phi/N + 2 pi k/N) : k = 0,...,N-1 }
```
For any spectral functional on this surface,
```text
F(Phi) = g(cos Phi)
F'(Phi) = -g'(cos Phi) sin Phi.
```
Thus, for every outer function `g` differentiable at `cos Phi = +-1`, the stationary set contains the real-holonomy locus `{0, pi}`. Interior stationary points are supplied by the chosen outer function `g`, not by the ring spectrum itself: selecting the off-locus member through a spectral functional requires tuning the outer function to the target.

## Retained Inputs
- [BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md) supplies the C3 generation surface and shift `C`; pinned fragments: "circulant form" and "(a, |b|, delta)".
- [KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04](KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md) is the retained modulus no-go precedent. Its ledger scope is: "Conditional on the stated C3-circulant lepton Yukawa and modulus-only objective V_mod = log|det M|, the clean determinant-modulus route does not select the non-degenerate physical phase δ≈2/9; its stationary candidates are δ=kπ/3 and are degenerate." Pinned file fragments: "stationary **only** at `δ = k·60°`" and "its stationary candidates are degenerate".

## Program Context (not citation-graph dependencies)
- PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`: campaign context for the restatement-circularity warning; not authority for this note.
- PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`: campaign context for the holonomy notation; not authority for this note.
- PR #4789 `ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`: campaign context for the real-holonomy locus; not authority for this note.
- PR #4790 `ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01`: in-flight transport-face context only; not authority for this note.
- `RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15`: next-path surface, named as context only.

## Flux Localization (T-S1)
For the symmetric-gauge fluxed ring, the characteristic polynomial
```text
det(lambda I - L_Phi)
```
has all non-constant coefficients independent of `Phi`. The constant term is
```text
(-1)^N det L_Phi = (-1)^N (2 - 2 cos Phi).
```
This was checked exactly for `N = 3,4,5,6` in the paired runner. The calculation uses the matrix entries directly and derives the coefficients by exact symbolic determinant expansion.

At `N = 3`, the Laplacian elementary spectral faces are
```text
e_1(L_Phi) = 6
e_2(L_Phi) = 9
det L_Phi = 2 - 2 cos Phi.
```
The hopping form has the same localization shape. For `N = 3`,
```text
e_1(H_Phi) = 0
e_2(H_Phi) = -3
det H_Phi = 2 cos Phi.
```
The combinatorial reading is that characteristic-polynomial coefficients are signed sums over vertex-disjoint cycle covers. A cover sees the flux only when it contains the full winding cycle. Those winding contributions appear only in the constant term, and their two orientations contribute
```text
exp(i Phi) + exp(-i Phi) = 2 cos Phi.
```
All smaller cycle-cover faces are therefore blind to the flux.

The localization is a single-cycle property. It is robust to edge-modulus
defects: with one edge weight `w` at `N = 3`, the constant term becomes
`2 w^2 + 2 w cos Phi - 4` while every non-constant coefficient stays
flux-blind. It fails on graphs with a second independent cycle: on the
4-ring with one chord, the `lambda^1` coefficient becomes flux-dependent.
The generation ring's one-holonomy topology is what forces the entire
spectral route through the single scalar `cos Phi`.

## Stationarity And The Tuned-Selector Classification (T-S2)
Every spectral functional on the fluxed-ring surface factors as
```text
F(Phi) = g(cos Phi).
```
Differentiating gives
```text
F'(Phi) = -g'(cos Phi) sin Phi.
```
(a) For `g` differentiable at `cos Phi = +-1`, the stationary set contains `{0, pi}`. This is the real-holonomy locus named in the campaign context. (Members singular at the locus, such as `log det L_Phi` at `Phi = 0`, are monotone up to the singularity and select nothing interior either.)

(b) An interior stationary point `Phi* in (0, pi)` exists iff
```text
g'(cos Phi*) = 0.
```
That is a property of the selected outer function `g`, not a property forced by the fluxed ring.

(c) The canonical members checked here are monotone on `(0, pi)` and have no interior stationary point:
```text
det L_Phi = 2 - 2 cos Phi
d/dPhi det L_Phi = 2 sin Phi > 0
```
```text
d/dPhi log det L_Phi = sin Phi / (1 - cos Phi) > 0
```
```text
Tr L_Phi^{-1} = 9 / (2 - 2 cos Phi)       at N = 3
d/dPhi Tr L_Phi^{-1} < 0                  on (0, pi)
```
```text
det H_Phi = 2 cos Phi.
```
Consequently, selecting `Phi = 2/3` by a spectral functional requires writing an outer function with
```text
g'(cos(2/3)) = 0.
```
That is a tuned selector. It restates the target value in the same restatement-circularity class as the clause `I({D}) := L`; this note does not use that campaign context as authority. The ring spectrum does not provide an untuned off-locus value selector.

## Flux-Blind Faces (T-S3)
For `N = 3,4,5,6`, the elementary symmetric faces
```text
e_1(L_Phi), ..., e_{N-1}(L_Phi)
```
are all flux-independent.

The penultimate face has the exact value
```text
e_{N-1}(L_Phi) = N^2.
```
At `Phi = 0`, this is the adjugate-trace / spanning-tree face. Matrix-tree gives every cofactor of the `N`-cycle Laplacian as `N`, so `Tr adj(L_0) = N^2`. Since `e_{N-1}` is flux-blind, the same value persists for all `Phi`.

The tree and adjugate faces cannot read `Phi`. They are useful invariants of the ring, but they cannot select the holonomy value.

## Consequence For The Wall (T-S4)
The route map for `W_cycle_holonomy_value` sharpens.

Any mechanism that selects `Phi = 2/3` must read data beyond the fluxed-ring spectrum: record/state-facing content on the ring, such as record formation, occupancy, orientation data, or boundary data.

That content would have to carry `K`-breaking content, because the spectral stationary loci land on the real-holonomy face `{0, pi}` unless an outer function is tuned to the off-locus target.

The named next path is the retained record-dynamics surface:
```text
RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15
```
This note marks that surface as the next path opened by the spectral classification. It does not assess that surface.

## What This Moves
| Item | Before | After |
| --- | --- | --- |
| spectral/effective-action route | unmapped | mapped: on-locus or tuned |
| modulus no-go precedent | clean modulus row on the circulant-M surface | extended to the full spectral-functional class on the fluxed ring |
| live mechanism space | broad spectral language still available | record/state-facing content beyond the spectrum |

## What Does Not Move
- No derivation of `Phi = 2/3` is supplied here.
- The retained modulus row's scope is unchanged.
- The record-dynamics surface is not assessed here.
- `W_defect_readout_selection` remains open.

## Audit Consequence If Retained
Rows should not cite fluxed-ring spectral functionals as selectors of the phase value.

The wall citation shape is unchanged: `W_cycle_holonomy_value` remains the value-selection wall, with the spectral-functional route now bounded to on-locus selectors or tuned selectors.

## Non-Claims
- This note does not claim non-spectral routes succeed.
- This note does not claim the record-dynamics surface delivers the value.
- This note does not extend the retained modulus row's audited scope; the extension is this note's own claim on its own surface.
- This note does not mint an additional wall label.
- This note says nothing about `r`, occurrence, Born, or theta.

## No-Go Discipline Gate
This checklist supports a bounded spectral-route no-go; it is not a terminal no-go.

### N1
Routes checked:
- det/modulus on fluxed ring: RULED OUT HERE, monotone on `(0, pi)`.
- trace-inverse/return-amplitude-as-functional: RULED OUT HERE, monotone.
- general spectral functional: CLASSIFIED HERE, on-locus or tuned.
- adjugate/tree faces: RULED OUT HERE, flux-blind.
- record/state-facing route beyond the spectrum: OPEN, the named strike direction.
- rescale-invariant derivation: OUT OF SCOPE HERE; the live rescale wall is not discharged by the spectral classification.
- owner primitive: GOVERNANCE.

### N2
No additional wall is introduced. The spectral-route no-go bounds mechanisms, not the wall set.

### N3
Hidden-wall scan:
- `fluxed ring`: symmetric-gauge presentation of the retained surface's hopping data; gauge-invariance of the spectrum noted.
- `spectral functional`: any function of the eigenvalue multiset.
- `outer function g`: the classification variable, not a physical object.
- `canonical vs tuned`: canonical means written without reference to the target value.

### N4
Residual matching:
- Retained modulus row: same on-locus conclusion, wider class, different surface.
- Campaign holonomy/transport context: same wall, mechanism space narrowed.
- Real-holonomy campaign context: this note's stationary sets land on that locus.

### N5
Proven sentences are the exact characteristic-polynomial facts, the monotonicity facts, and the factor-through-`cos Phi` classification at the stated finite resolution: `N = 3,4,5,6` for generality checks, and `N = 3` for the campaign surface.

### N6
Live paths:
- record/state-facing theorem on the ring carrying `K`-breaking content, with the next-path surface named.
- rescale-breaking registration theorem.
- owner primitive.

### N7
Steelman: "factor-through-cos-Phi is obvious from gauge invariance, so the no-go is trivial."

Reply: gauge invariance gives dependence on `Phi`; the sharper content is where flux sits, namely in the constant term only, plus the flux-blind faces `e_{N-1} = N^2`, canonical-member monotonicity, and the tuned-selector classification. Those statements do not follow from gauge invariance alone. The single-cycle characterization (robust to edge defects, broken by a chord) shows the reduction is a statement about the generation ring's one-holonomy topology, not a generic spectral triviality.

Concede: no value is derived, and the classification is at the stated finite resolution.

### N8
Echo: extremal and stationarity selectors landing on symmetry loci or requiring tuned weights are recurring patterns: the retained modulus row and the campaign's counting route pinning the wrong member. Uniform lesson: canonical functionals see the locus, targets need mechanisms.

## Verification
Run from the worktree root:
```bash
python3 scripts/acphilambda_fluxed_ring_spectral_functional_route_no_go_2026_07_02.py
```
Expected close:
```text
TOTAL: PASS=127 FAIL=0
```
