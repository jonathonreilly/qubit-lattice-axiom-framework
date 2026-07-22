# Physical rational-Regge / reciprocal-response / prediction bridge — Cycle 604 (2026-07-22)

- authority: none
- audit: unset
- constitutional effect: none
- status: three constructive partials; no shared no-go and no axiom pressure

## Frozen tournament

Cycle 604 continues accepted Cycle601 with three independent routes:

1. Route A, priority: a fixed-state Padé / continued-fraction line transfer,
   a finite lossless termination with retained garbage, and a co-designed
   Regge product that preserves its declared expanded image.
2. Route B: a reciprocal modular source/field kick-drift candidate with an
   exact conserved word and local continuity.
3. Route C: a frozen finite-horizon Cesaro bridge to the Cycle585/588 static
   Green prediction and the Cycle451/570 matched-event surface.

The runner byte-pins Cycles 601, 576, 579, 585, 588, 451, and 570.  Nothing in
this cycle edits their laws or status.

## Route A — rational transfer and image-preserving Regge product

### Exact rational object

Writing `w=exp(i z)`, the fixed `[1/1]` Padé candidate is

`R(w) = 2(1+2w)/(5+w)`.

It is the exact transfer function of the one-state realization

`T = [[-1/5, 3 sqrt(2)/5], [3 sqrt(2)/5, 2/5]]`.

Its singular values are `1` and `4/5`, so it is contractive.  The runner forms
the four-channel Julia dilation from the two defect operators and tests its
unitarity and the state-transfer identity directly.

This does not make `R` a finite-depth compiler.  Exact stationary use of the
denominator `1+w/5` needs an unbounded recurrence or a prepared fixed-point
state.  Cycle604 supplies neither and therefore scopes the exact rational
object as a mathematical local recurrence, not as the delivered physical
compiler.

### Exact finite FIR unitary dilation

The executed physical object is the frozen degree-eight DC-corrected
termination

`P8(w) = sum_(n=0)^8 c_n w^n`,

with `c0=2/5`, geometric Padé coefficients through order seven, and the final
coefficient chosen before fixtures so `P8(1)=1`.  A minimum-phase
Fejer-Riesz factor `Q8` is constructed.  The runner verifies the Laurent
coefficient identity

`1-|P8(w)|^2 = |Q8(w)|^2`

coefficient by coefficient.  This proves nonnegative defect over the full
unit circle; it is not an inference from the momentum sampling grid.

The two-by-two polynomial

`[[P8, -reverse(Q8)], [Q8, reverse(P8)]]`

is paraunitary.  Its second output is retained garbage, never erased or
measured.  Recursive leading-coefficient reduction extracts eight rank-one
delay sections plus a constant two-by-two base unitary.  Reconstruction of the
complete polynomial, section walls, base unitarity, full-circle maximum
defect, and deletion of one delay section are tested.

Each abstract delay section has an explicit bounded M2 schedule:

1. an onsite frozen parameterized two-M2 basis rotation;
2. one selected-rail proper-cubic stream permutation, with at most three axial
   permutation sublayers for a body-diagonal direction;
3. the inverse onsite rotation.

The all-frame encoder has 720 data M2 rails per coarse cell.  The receipt
places them injectively in a frozen `9x9x9` block by
`rail=30*frame+2*edge+channel` and
`(x,y,z)=(rail mod 9, floor(rail/9) mod 9, floor(rail/81))`; it also prints
the eight projector vectors and constant base matrix.  This is a concrete
bounded block layout, not an accepted-gate-alphabet synthesis.

The stream is a local QCA permutation layer.  It is not claimed to be a finite
circuit of nearest-neighbor swaps on a closed torus.  Likewise, the arbitrary
base/projector/Givens matrices are frozen parameterized one-/two-M2 gates; no
lowering to an accepted finite gate alphabet is executed.  Thus “fixed-state
and fixed-width” is established, while “constant accepted alphabet” remains
open.

The numerical functions `apply_filter` and `physical_product` execute the
resulting block-circulant operator directly.  They do not replay every delay
gate.  The independently reconstructed delay-section factorization is the
local realization certificate.  This distinction is explicit in the receipt.

### Co-designed Regge product

Cycle601 applied the raw edge product and measured code-image leakage.  Here
the Cycle576 Regge kernel is first conjugated into ten metric rails by the
zero-momentum polar isometry.  Its finite spatial kernel is then factored into
diagonal and translated two-rail layers entirely inside those ten rails.
The five complementary rails are idle.  Conjugating this metric-rail product
by the onsite 15-rail completion and the paraunitary line encoder gives

`G_physical E_FIR = E_FIR G_metric`

exactly on the expanded code.  This is co-design, not post-update projection.
The runner evaluates the intertwining residual, exact inverse, leakage, and
factor deletion on train L4, held L6/L8, and out-family L10.

Same-role translated hopping is split by a bipartite matching color.  This is
tested only on even periodic tori.  Odd-torus coloring and a translation-
covariant QCA replacement remain open.  Every frame sector uses its local
color and local directions; all 24 proper-cubic sectors and all 576 frame
products are checked.  Proper-cubic covariance is not Lorentz covariance.
This is the declared even torus scope.

The metric product is an ordered product at the supplied Cycle579 angle.  Its
error against the target exponential is measured and retained.  A generator
is not a rate, a factor schedule is not time, and no phase is physical energy.

Exact theorem: the degree-eight paraunitary, retained-garbage dilation,
expanded-image intertwining, inverse, and even-torus factor product are exact
up to reported numerical residuals.

Approximate theorem: `P8` approximates `R` uniformly at the measured small
termination error; `R` approximates the exact Cycle576 line factor only to
low-momentum order `O(z^3)`.  Full-BZ error is explicitly large.  Neither the
Padé transfer nor `P8` is the exact sinc line factor, and the ordered product
is not the exact target exponential.

Disposition: **constructive exact fixed-parameter FIR image compiler;
Padé, sinc, accepted-alphabet, odd-torus, and exponential terminals remain
scoped**.

## Route B — reciprocal modular response

Every cell carries four signed 31-bit modular words:

- source coordinate `q` and source momentum `p_s`;
- field coordinate `phi` and field momentum `p_f`.

For coupling sign `s=+1` or `-1`, the reciprocal kick is

`p_s <- p_s - L q - s(q-phi)`

`p_f <- p_f - L phi + s(q-phi)`,

and drift is `q<-q+p_s`, `phi<-phi+p_f`, all modulo `2^31`.  Both kick-then-
drift and drift-then-kick are executed.  Each has an algebraic inverse and
uses only current local words; neither needs a host future-source service.

The declared ledger is

`sum_x (p_s+p_f) mod 2^31`.

The exchange cancels locally and the two Laplacians are divergences, so the
runner tests both the global word and cellwise continuity.  The ledger is only
a conserved modular word.  It is not stress-energy, not physical energy, and
not gravity.  The source word has not been joined to accepted
matter and is not called physical recoil.

Controls include exact inverse, source-off, source deletion, field deletion,
recoil deletion, no-wrap fixtures, an explicit wrap-and-inverse fixture,
positive/negative coupling, both factor orders, all 24 frames, and all 576
products.  Both undeleted orders and signs remain valid and distinguishable.
No response order or sign is selected.

The arithmetic has radius one, three-M2 ripple gates, fixed word width, and a
stated depth upper bound.  The test harness reads the conserved global sum but
the update does not compute or consume it.

Disposition: **constructive exact reciprocal ledger and continuity;
physical source/recoil, sign, order, calibration, and backreaction remain
open**.

## Route C — finite response to static and matched-event predictions

The freeze precedes every output:

- response law: reversible wave recurrence with `alpha=1/12`;
- source normalization: one point minus uniform `1/L^3`, with no fitted
  amplitude;
- train: L5 and 192 updates;
- held: L7 and 384 updates;
- out-family: L9 and 768 updates;
- precision: float64 with a long-double repetition.

The Cesaro mean is compared with the exact finite-torus solution of
`L phi=rho`.  Absolute response residual, relative response residual, absolute
equation residual, relative equation residual, precision residual, and a
non-applied projection-scale diagnostic are reported.  The frozen residuals
must decrease across the three fixtures.  Update count is not time, endpoint
norm is not probability or occurrence, and this stable comparison law does
not yet have a physical-M2 arithmetic compiler.

The bridge to Cycle585/588 is exact at the operator level: the Cesaro fixed
equation and the accepted static surface use the same cubic Laplacian `L`.
Cycle604 independently reevaluates the frozen axis/face/body infinite-lattice
fixtures and the coefficient `5/(32pi)` with no parameter refit.  A finite
Cesaro horizon does not directly measure that cubic coefficient; it approaches
the finite inverse whose infinite-volume surface has the coefficient.

Cycle451 and Cycle570 contribute exact matched candidate-event words:
source-off and receiver-zero `4:4`, delay `3:4`, and advance `5:4`.  Cycle604
keeps those rational words exact.  The association from response sign to delay
or advance is explicitly supplied.  Neither those cycles nor the Cesaro
surface selects sign, order, event actuality, a Record, or empirical
calibration.

Disposition: **constructive common-operator prediction bridge; finite-limit,
physical compiler, and matched-event calibration remain supplied/open**.

## Supplied and open inventory

Supplied: Padé order one; H=8 termination; minimum-phase choice; vacuum garbage
input; even-torus matching color; all factor schedules and parameterized gate
matrices; Cycle576 kernel and Cycle579 angle; 31-bit word width; initial source
word; coupling sign and kick/drift order; alpha; zero-mean source; finite
Cesaro horizons; arithmetic precision; Cycle451/570 identities; and the
response-sign/event association.

Derived or executed: contraction and Julia dilation; Fejer-Riesz coefficient
identity; exact paraunitary and eight-section factorization; exact expanded-
image Regge intertwining and inverse; reciprocal modular ledger and local
continuity; finite Cesaro/static comparison; and the inherited no-refit cubic
coefficient comparison.

Not derived: finite-depth exact rational fixed-point preparation; an accepted
finite gate-alphabet lowering; exact sinc; color-free odd-torus product; exact
target exponential; physical matter/recoil or stress-energy identification;
response sign/order; time; gravity; finite/static equality; event calibration;
Born probabilities; Records; or a joint Cycle590/recurrent-pair compiler.

## Full no-go discipline

### N1 — alternative route enumeration

1. one-state rational transfer / Padé recurrence plus Julia dilation / exact
   `R(w)` — attempted mathematically, finite preparation open;
2. two-channel FIR filter / Fejer-Riesz plus eight delay sections / bounded
   fixed-parameter encoder — attempted positive;
3. midpoint path dilation / Cycle601 coherent `q=4` recombination / bounded
   line approximation — prior attempted;
4. finite DFT code / Cycle596 quadrature / exact finite line map — prior ruled
   out only for constant overhead;
5. metric-rail product / project kernel before factorization / exact expanded-
   image preservation — attempted positive;
6. raw edge product / Cycle579 factors / actual Regge update — prior ruled out
   only for image preservation;
7. paired modular fields / reciprocal kick-drift / conserved response ledger —
   attempted positive;
8. unilateral modular wave / Cycle601 leapfrog / local response — prior
   attempted;
9. stable reversible wave / alpha-Cesaro / finite-to-static bridge — attempted
   positive;
10. static constrained inverse / Cycles585/588 / `1/r` plus cubic surface —
    prior attempted.

Finite-state rational and finite FIR families remain distinct.

### N2 — wall independence

The receipt audits every pair among: exact sinc; rational-state preparation;
accepted gate alphabet; even-torus color; target exponential; physical source
identity; sign/order selection; finite/static limit; event calibration; and
the joint Cycle590 compiler.  Closing any one does not logically close another.

### N3 — hidden-wall scan

The audit exposes Padé order, termination horizon, spectral-factor branch,
garbage vacuum, even color, schedules, parameterized matrices, word width,
sign, factor order, alpha, source normalization, finite horizons, precision,
and event calibration.

### N4 — residual matching

Each measured residual is assigned to its route: line error to exact sinc;
fixed-point preparation to exact rational use; arbitrary matrices to alphabet
lowering; parity color to odd tori; product error to the target exponential;
modular words to physical source identity; alternative outputs to sign/order;
Cesaro residual to the finite/static limit; and `3:4`/`5:4` association to event
calibration.  None is promoted to a shared substrate obstruction.

### N5 — rhetoric audit

“Exact” is limited to the Julia/FIR identities, factor reconstruction,
expanded-image preservation, inverse, modular ledger/continuity, and the
common operator.  Sinc, exponential, physical-source, static-limit, time,
gravity, event, and alphabet claims remain explicitly scoped.

### N6 — partial closure

The FIR closes finite local dilation and image preservation without exact sinc
or alphabet lowering.  Kick-drift closes a reciprocal ledger without physical
source identity or order selection.  Cesaro closes a prediction bridge without
making update count time or calibrating events.

### N7 — concrete steelman

A higher-order Schur colligation with autonomously prepared invariant state
could improve full-zone accuracy; a translation-covariant QCA metric product
could remove the even-torus color; and an accepted-matter symplectic coupling
plus autonomous matched detector could select sign/order.

### N8 — cross-cycle echo

Cycles596/601 separated exact size-growing DFT from bounded midpoint
approximation and exposed raw-image leakage.  Cycle604 adds a different finite
paraunitary family and moves the Regge product into metric rails, closing the
finite dilation/image walls but not exact sinc.  Cycles585/588 supply the same
static operator and cubic surface.  Cycles451/570 preserve matched event words
but not their calibration.

**Broad negative gate: FAIL / DO NOT SHIP.**  Multiple constructive routes
advance different walls, stronger rational/QCA and matter/detector steelmen
remain live, and there is no shared route-independent obstruction.  Therefore
there is no axiom pressure.

## Dependency ledger and next campaign

- `C_ref`: unchanged; frame, sign/order, and event calibration remain supplied.
- `C_num`: partial advance from explicit fixed coefficients and modular ledger;
  physical scale remains supplied.
- `C_wrap`: unchanged; wrapped words/phases and update counts are not energy,
  rates, or time.
- `C_int`: mathematical advance from reciprocal exchange and continuity;
  accepted matter, physical recoil/stress, and joint compilation remain open.
- `C_local`: advance from the exact fixed-parameter FIR and exact expanded
  image on even tori; alphabet lowering, exact sinc, odd tori, and target
  exponential remain open.
- `C_source`: partial advance from the reciprocal ledger and prediction bridge;
  source identity, response selection, calibration, and gravity remain open.

Maturity 0–5: operational quantum/records 4.0; time 3.0; inertia/matter 4.0;
gravity/source 3.25; Born/probability 2.0.

The strongest result is the exact degree-eight two-channel fixed-parameter
paraunitary with retained garbage, conjugated around a metric-rail Regge
product so the expanded approximate image is preserved exactly.

The optimal next campaign is a translation-covariant QCA replacement for the
even-torus metric coloring, followed by a reciprocal coupling to accepted
matter and an autonomous matched detector capable of selecting sign/order.

## Independent parent verification

The parent inspected the explicit FIR matrices, full-circle coefficient
identity, delay-section factorization, metric-product construction, modular
kick signs, continuity equation, and finite/static interpretation before
re-executing every scientific route without invoking the receipt-writing
`main` function.  All twelve route/shore/N1--N8 checks passed again.  Route A
reproduced maximum intertwining, leakage, and inverse residuals
`2.793359906207423e-15`, `2.7799003194654083e-15`, and
`5.626398463373706e-15`.  Route B reproduced exact-zero inverse, conserved
ledger, local-continuity, and all-24 covariance residuals.  Route C reproduced
the frozen relative Cesaro residuals
`0.006794530460511728`, `0.005751565018220709`, and
`0.003728477636657561`.

The parent accepts the fixed-parameter FIR dilation, expanded approximate-code
intertwiner, reciprocal modular ledger, and common-Laplacian prediction bridge.
It does not accept an exact sinc compiler, an accepted finite gate alphabet,
a closed-torus nearest-neighbour QCA realization, physical stress-energy or
matter/recoil identification, selection of sign or factor order, a finite
static-limit equality, calibrated event response, gravity, shared obstruction,
or axiom pressure.  The frozen worker receipt and cold transcript were not
overwritten by this spot reproduction.
