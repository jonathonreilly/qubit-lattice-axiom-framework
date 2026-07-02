# AC_phi_lambda Ambient Equivariant Heat-Trace Face
**Date:** 2026-07-02
**Claim type:** bounded theorem / ambient face + unit-junction persistence
**Status authority:** independent audit lane only. This note does not set an audit
verdict, edit registries, register primitives, change axioms, or claim
`AC_phi_lambda` retirement.
**Primary runner:**
[`scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py`](../scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py)
## Claim
Let `Z_N^3` be the periodic cubic lattice, let `A` be nearest-neighbor
adjacency, and let `Delta = 6I - A`. Let `R` be the proper cubic coordinate
cycle
```text
R(x1,x2,x3) = (x3,x1,x2).
```
For `j = 1, 2` and any function `f`,
```text
Tr(f(Delta) R^j) =
  sum_{R^j k = k} f(Delta_hat(k)).
```
The fixed momenta are exactly the `[111]` diagonal momenta
`k = (kappa,kappa,kappa)`, each with unit trace weight. Therefore
```text
Tr(exp(-t Delta) R^j) =
  sum_{m=0}^{N-1} exp(-t (6 - 6 cos(2 pi m/N))).
```
For the per-axis-site amplitude
```text
A(t,N) = (1/N) sum_{m=0}^{N-1} exp(-t (6 - 6 cos(2 pi m/N))),
```
the two continuum normalizations are
```text
per axis site:                 A(t) -> (12 pi t)^(-1/2),
per unit Euclidean [111] length: A(t)/sqrt(3) -> (1/3)(4 pi t)^(-1/2).
```
In this precise sense, the fixed-locus density acquires its ambient face: the nontrivial-sector group average of the per-unit-`[111]`-length equivariant heat-trace amplitudes of the `Z^3` lattice.
At the same time, the unit junction persists verbatim in ambient coordinates: per-site versus per-unit-length is a `sqrt(3)` rescale of the density normalization.
And nothing here derives the physical normalization or the phase value.
## Frame And Retained Inputs
The dependency source is
[KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md).
It supplies the pinned local row: "**(B) The weight `(1,2)` is forced and gives local density `2/9`.**"
It also pins the scope exclusion: "It does **not** supply the physical single-summand readout".
The axiom memo `docs/MINIMAL_AXIOMS_2026-06-29.md` supplies the lattice objects:
"Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations."
Campaign context is `PR #4783
ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`,
`PR #4788 ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`,
`PR #4789 ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`, `PR #4790
ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01`, `PR #4794
ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02`, and
`PR #4798
ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02`.
The ambient Laplacian `Delta = 6I - A` is a reconstruction-side operator built
from the Lattice axiom's adjacency, like the ring Laplacian in `PR #4790`. It is
a calculational device, not a claimed dynamics.
## Exact Diagonal-Momentum Reduction (T7-1)
Plane-wave momentum labels are integer triples `m = (m1,m2,m3)` modulo `N`,
with `k_i = 2 pi m_i/N`. The rotation permutes momentum labels. For both
nontrivial powers,
```text
R^j m = m mod N  <=>  m1 = m2 = m3 mod N.
```
The trace of `f(Delta) R^j` in the momentum basis therefore receives
contributions only from the diagonal set `{(m,m,m)}`.
The diagonal matrix element at a fixed momentum has unit weight. Equivalently,
the character sum
```text
sum_x exp(2 pi i (m . x - m . R^j x)/N)
```
equals `N^3` at a fixed momentum and vanishes off the fixed set. After
normalization by the plane-wave volume, the weight is exactly one.
On the diagonal,
```text
Delta_hat(kappa,kappa,kappa) = 6 - 6 cos(kappa),
```
so the trace identity is
```text
Tr(exp(-t Delta) R^j) =
  sum_{m=0}^{N-1} exp(-t (6 - 6 cos(2 pi m/N))).
```
The fixed sets for `j = 1` and `j = 2` coincide. Dense diagonalization on
`N = 4, 5, 6` confirms the trace identity at `t = 0.3, 1.0, 3.0`. The anchored
checks are
```text
N = 4, t = 0.3: 1.357921498890
N = 6, t = 1.0: 1.099827100556
```
Three rejectors are part of the theorem surface. The identity component
`j = 0` gives the full heat trace, not the diagonal sum. A `C4` face rotation
has a different fixed-momentum count at `N = 4`. Replacing `6 - 6 cos(kappa)`
by `6 - 2 cos(kappa)` breaks the dense trace equality.
## Continuum Bookkeeping And The Lefschetz Factor (T7-2)
The per-axis-site amplitude is
```text
A(t,N) = (1/N) sum_m exp(-t (6 - 6 cos(2 pi m/N))).
```
The lattice dispersion has the axial continuum expansion
```text
6(1 - cos(kappa)) = 3 kappa^2 + O(kappa^4).
```
Thus the per-axis-site normalization tends to
```text
A(t) -> (12 pi t)^(-1/2) = (1/sqrt(3))(4 pi t)^(-1/2).
```
Dividing by the Euclidean length per diagonal step gives
```text
A(t)/sqrt(3) -> (1/3)(4 pi t)^(-1/2).
```
The factor `1/3` is recovered only per unit Euclidean `[111]` length. Per site,
the coefficient is `1/sqrt(3)`. The `sqrt(3)` between them is the metric dial
between diagonal lattice sites and Euclidean length.
The runner checks `t = 25, 100, 400` with `N = ceil(12 sqrt(t))`. It verifies
that `sqrt(12 pi t) A(t,N)` approaches one with decreasing error and ratios in
the expected dispersion-correction range. It applies the same convergence gate
to `sqrt(4 pi t) A(t,N)/sqrt(3)` approaching `1/3`, and it checks that
`sqrt(4 pi t) A(t,N)` remains separated from `1/3` and instead approaches
`1/sqrt(3)`.
## Face Wiring And Unit-Junction Persistence (T7-3)
For the two nontrivial `C3` sectors, the transverse factors are exact:
```text
1 / |omega^j - 1|^2 = 1/3,  j = 1,2.
```
The core identity is
```text
(omega - 1)(omega^2 - 1) = 3.
```
Therefore the unaveraged nontrivial-sector sum is
```text
S_sum = 1/3 + 1/3 = 2/3,
```
and the `C3` group average is
```text
L3 = (1/3) S_sum = 2/9.
```
This matches the fixed-locus density value exactly. Combining T7-1 and T7-2:
the fixed-locus density acquires its ambient face: the nontrivial-sector group average of the per-unit-`[111]`-length equivariant heat-trace amplitudes of the `Z^3` lattice.
The dial does not close: the unit junction persists verbatim in ambient coordinates: per-site versus per-unit-length is a `sqrt(3)` rescale of the density normalization.
The ambient face gives future work the axiom-level object, the `Z^3`
equivariant heat kernel, on which K-breaking record-facing mechanisms can be
posed.
## What This Moves
| Surface | Before | After |
| --- | --- | --- |
| density faces | ring-internal face per `PR #4790` | ambient `Z^3` face from Lattice-axiom objects |
| unit junction | abstract `c` normalization | concrete metric dial: site versus Euclidean length, `sqrt(3)` |
| future mechanism surface | ring return amplitude | ambient equivariant heat kernel |
## What Does Not Move
- No value derivation is supplied.
- No physical-normalization selection is supplied.
- No dynamics claim is made for `Delta`.
- Readout selection remains open under `W_defect_readout_selection`.
- No occurrence/Born content is supplied.
## Audit Consequence If Retained
Rows may cite the ambient face as exact reconstruction-layer arithmetic. The
value wall citation is unchanged: one dependency line can remain
`W_defect_identity_unit` / `W_cycle_holonomy_value` / R-eta (ii).
## Non-Claims
- The heat kernel is not claimed to be the physical dynamics.
- The normalization is not derived; per-site versus per-length remains the open
  dial.
- The fixed-locus row's scope is not extended.
- No additional `W_` label is introduced.
- No continuum-limit physics claim is made beyond the stated asymptotics of the
  stated lattice sums.
## No-Go Discipline Gate
**Status:** PASS for bounded ambient-face theorem; not a terminal no-go.
### N1
Alternative-route inventory:
- ring-internal faces: landed, `PR #4790
  ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01`.
- ambient equivariant reduction: ATTEMPTED here, exact.
- continuum Lefschetz recovery: ATTEMPTED here, numeric with ratio gates.
- ambient normalization selection: OPEN, the unit junction in ambient form.
- rescale-invariant derivation: RULED OUT by `PR #4783
  ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01` context.
- owner primitive: GOVERNANCE.
### N2
There is no additional wall label. The same unit junction appears in ambient
coordinates as the site-versus-length normalization dial.
### N3
Hidden-wall scan:
- `ambient Laplacian`: reconstruction device from the Lattice axiom's adjacency,
  not dynamics.
- `continuum limit`: asymptotics of the stated lattice sums only.
- `Euclidean [111] length`: the metric dial, the open normalization, not assumed
  physical.
- `group average`: the `C3` order, as in the fixed-locus row.
### N4
Residual matching: the fixed-locus row keeps the same density while gaining a
new face; readout remains excluded. `PR #4790` supplies the ring face now joined
by the ambient face. `PR #4783` says the rescale persists on the ambient dial.
### N5
The proven sentences are the exact reduction identity and the stated numeric
asymptotics with ratio gates. No physical readout statement is proved.
### N6
Live paths remain: pose K-breaking record-facing mechanisms on the ambient
equivariant kernel; derive the physical normalization, site versus length, from
a record-facing theorem; supply an owner primitive.
### N7
Steelman: "equivariant heat-trace localization is classical mathematics, so
this is textbook." Reply: the exact lattice reduction with unit weights and the
per-site/per-length dichotomy carrying the campaign's unit junction are the
specific content; classical localization is the continuum shadow. Concede: no
value is derived; the mathematics is elementary once stated.
### N8
Echo: the same number appearing in ring-internal and ambient presentations is
handled as identity-of-object under no-coincidences discipline, extending the
`PR #4790` pattern.
## Verification
Run:
```text
python3 scripts/acphilambda_ambient_equivariant_heat_trace_face_2026_07_02.py
```
Measured close:
```text
TOTAL: PASS=77 FAIL=0
```
