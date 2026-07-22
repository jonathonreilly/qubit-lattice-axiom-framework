# Physical Regge Static-Scalar / Prediction Bridge Tournament — Cycle 585

**Date:** 2026-07-22  
**Authority:** none  
**Audit:** unset  
**Status:** positive partial construction with explicit residuals  
**Runner:** `scripts/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_2026_07_22.py`

Machine-readable scope contract: authority: none; audit: unset. The metric-image
constraint is not locally enforced, and the extra edge zero is handled only by
the declared reduction/range comparison. There is no fit to the graph or held
surface. The actual-source result is a contact response in this scalar readout.
It is not gravity, not physical energy, not physical stress, and not a
Newtonian calibration. Gauge-penalty invariance is executed below. There is no
axiom pressure.

## Question and firewall

This cycle asks whether the actual Cycle-576 raw Regge Hessian and raw
unnormalized deficit source, together with the Cycle-581 finite symmetric
update, constructively reach the independently derived cubic graph-Laplacian
Green surface

```text
G_graph(r) = 1/(4 pi r) + [5/(32 pi)] K4(nhat)/r^3 + O(r^-5).
```

The answer is a useful but incomplete separation:

1. a gauge-invariant static scalar Schur operator exists and has a `1/k^2`
   inverse pole;
2. its cubic-harmonic correction is not the graph value in this reduction;
3. the actual reduced deficit source vanishes at the same `k^2` order as the
   operator and therefore gives a contact-like `h_44` response rather than
   exciting that pole;
4. a finite-range local approximant and a finite-volume reversible-tape solver
   can be built from the frozen scalar symbol; and
5. a Cycle-581 Cesaro phase filter approximates the range pseudoinverse, but
   the raw edge source has a nonzero component in the fifth, nonmetric edge
   zero branch.

These are results about this explicit construction. They are not a shared
obstruction, a minimum-content theorem, or axiom pressure. The result is not
called gravity, physical energy, physical stress, a Newtonian calibration, or
an Einstein equation. The graph surface is a comparison target. The derived
`5/(24pi)` coefficient below is an operator-surface consequence conditional on
this scalar reduction; it is not a physical gravity prediction because neither
the required source/readout nor a physical static solver has been joined.

Cycle 460 is not evidence or a premise. It was read only to preserve its
boundary: it compiles supplied finite receiver kernels and cannot be used as
an anchor for the homogeneous law derived here. No Cycle-460 held kernel or
receiver value is consumed.

The Cycle-230 shore is preserved exactly. The actual Cycle-230 contact, the
one-particle mass fixture, the seam block, leakage controls, and the all-24 / 576
covariance fixtures are not changed. Wrapped phase is not called energy, a
generator is not a rate, and update/filter steps are not physical time.

## Exact-pinned inputs and reconstruction order

The load-bearing inputs are:

- Cycle 576: the actual 15-edge cubic-Coxeter Regge Hessian `Q_R(k)`, the raw
  deficit row `d_R(k)=sum_t d_t(k)`, the exact line-averaged metric map `M(k)`,
  24 co-present proper-cubic frame sectors, source sign/coupling, and the
  derived long-wave coefficient `-1/2` relative to the R3/EH comparator;
- Cycle 581: the generalized symmetric finite-update law and its exact inverse
  product; and
- the independent graph-Laplacian heat-kernel/correction results, used only
  after the Regge reduction and its coefficients are frozen.

The runner checks hashes for all three surfaces. Cycle 420, Cycle 460, and
Cycle 216 are separately hash-pinned as reconnaissance-only comparison
boundaries, not premises. In particular, Cycle 216's supplied identity
`<scalar|K^+|scalar>=3/L` does not derive the Cycle-576 scalar law.

## Route A — metric-image, gauge-fixed static Schur reduction

### A1. Scalar and source projection

At zero fourth momentum, `k=(kx,ky,kz,0)`, define the metric-image objects

```text
Q_h(k) = M(k)^dag Q_R(k) M(k),
j_h(k) = [d_R(k) M(k)]^dag.
```

The co-present proper-cubic scalar is obtained by the Cycle-576 uniform
24-sector projection. This is not a new stochastic average and does not add a
host-selected frame.

The static scalar variable is `h_44`. Under a static gauge displacement,
`delta h_44` is proportional to `k_4`, so it is zero. Numerically, the exact
metric block has four gauge null modes at every tested nonzero static momentum;
`Q_h Z`, `Z^dag j_h`, and the `h_44` row of `Z` are tested directly. A unit
penalty `Z Z^dag` is added only on that null space. Schur elimination of the
other nine metric components then defines

```text
S_44 = Q_44 - Q_4r (Q_rr + gauge penalty)^-1 Q_r4,
J_44 = j_4  - Q_4r (Q_rr + gauge penalty)^-1 j_r.
```

The normalized scalar operator is

```text
K_R(k) = -2 S_44(k).
```

The factor `-2` is not an autonomous calibration and is not fit here. It is the
exact-pinned normalization choice inherited from Cycle 576's independently
derived long-wave Regge/R3 coefficient `-1/2`. No Green value, receiver value,
held momentum, or empirical datum selects it.

The corresponding actual raw source is `B_R=-2 J_44`, and its scalar response
is

```text
h_44(k) = B_R(k)/K_R(k) = J_44(k)/S_44(k).
```

The unit coefficient of the null-space penalty is not merely assumed harmless.
The runner recomputes `K_R`, `B_R`, and `h_44` with positive penalties
`0.25`, `1`, and `4` on train-axis, train-contact, held-generic, held-body, and
generic-covariance momenta. It reports the maximum change of all three objects
relative to unit penalty. The penalty set is frozen and not selected from held
response.

### A2. Freeze before comparison

Training uses only small axis and face-diagonal momenta. For a direction `n`,
the runner evaluates

```text
q_n(t) = [K_R(t n)-t^2 |n|^2]/t^4
```

at `t` and `t/2` and removes the leading `O(t^2)` error by Richardson
extrapolation. Cubic covariance leaves two quartic invariants, so the training
values freeze

```text
K_R(k) = k^2
       + a sum_i k_i^4
       + b sum_(i<j) k_i^2 k_j^2
       + O(k^6),

a = -1/12,
b = +1/18
```

to the runner tolerances. Three differently oriented held directions are then
evaluated with zero refit and show `O(k^6)` residuals.

Only after this freeze is the graph symbol compared. The graph Laplacian has

```text
L(k) = k^2 - (1/12) sum_i k_i^4 + O(k^6),
```

with no mixed quartic term. To expose the long-range part of the Regge scalar
symbol, use

```text
sum_(i<j) k_i^2 k_j^2
  = [(k^2)^2 - sum_i k_i^4]/2.
```

Therefore

```text
K_R(k)
  = k^2 + (1/36)(k^2)^2 - (1/9) sum_i k_i^4 + O(k^6).
```

The `(1/36)(k^2)^2` piece contributes a momentum-analytic/contact-supported
term after inversion away from the source. The cubic-harmonic coefficient is
controlled by `-1/9`, whereas the graph value is `-1/12`. Their ratio is
exactly

```text
(-1/9)/(-1/12) = 4/3.
```

Thus the conditional Green surface of this reduced operator is

```text
K_R^+(r) = 1/(4 pi r) + [5/(24 pi)] K4(nhat)/r^3 + O(r^-5),
```

not the independent graph value `5/(32pi)`. This is a clean, held-tested
operator mismatch without fitting. It is route-specific: another scalar,
constraint, or physical source/readout could produce a different reduction.

### A3. Operator pole versus actual source overlap

The distinction between operator and source is load-bearing:

- `K_R(k)` vanishes as `k^2`, so `K_R^+` has a scalar Green pole.
- The actual raw deficit source `B_R(k)` also vanishes as `k^2`.
- Their ratio approaches a bounded value, `h_44 -> 2`, on train and held
  directions.
- Consequently this actual deficit source does not excite a `1/r` tail in this
  readout. The observed response is contact-like at long wavelength.

No momentum-dependent normalization is applied to manufacture a pole. In
particular, dividing the raw source by `k^2` would violate the Cycle-576
downstream firewall.

### A4. Fifth edge zero and range condition

The full 15-edge Hessian has five zero modes at nonzero momentum: four discrete
gauge modes plus the exact nonmetric branch already identified by the Regge
theorem. The raw edge deficit source is Ward-orthogonal to the four gauge
modes, but it has a nonzero projection on the fifth branch. The runner measures
that projection on train L3 and held L4/L5 fibers.

Hence the unprojected equation `Q_R e=d_R^dag` is not solvable as written. Route
A avoids this by declaring the exact metric-image constraint before reduction.
The constraint is supplied by the Cycle-576 metric map; its local physical-M2
enforcement is not compiled here. This is a route-specific range-condition
failure, not an obstruction to constrained codes or alternate sources.

## Route B — local 19-point approximant and reversible-tape solver

Route B freezes the Route-A mixed coefficient from training and constructs

```text
K_app = L + beta sum_(i<j) L_i L_j,
beta = b ~= 1/18,
```

where `L_i=2-T_i-T_i^-1`. This operator:

- reproduces Route A through quartic order;
- is positive semidefinite on every periodic finite volume because `beta>0`;
- has only the uniform zero mode;
- has a 19-point stencil: onsite, six axial neighbours, and twelve
  face-diagonal neighbours;
- has exact proper-cubic covariance under all 24 frames; and
- uses no Cycle-460 receiver kernel or held anchor.

On the zero-mean source code, the finite-volume update is Richardson iteration

```text
x_(n+1) = x_n + omega (b-K_app x_n),
omega = 2/(lambda_min+lambda_max).
```

For each volume the spectrum of the declared operator fixes

```text
q = (lambda_max-lambda_min)/(lambda_max+lambda_min),
||e_N||_2 <= q^N ||e_0||_2.
```

The target error is frozen before train L5 and held L7/L9. The host FFT inverse
is used only after execution as a comparator. It never appears in the update.

Reversibility is explicit but resource-heavy: every previous field is retained
on a tape. Reverse execution pops the tape and verifies the local forward
equation exactly. The runner reports `(N+2)L^3` signed-real registers, equation
and solution residuals, reverse consistency, deletion, and held no-refit.

This is a finite-volume local reversible declared approximant, not a physical
M2 solver. Physical M2 arithmetic remains open: signed finite-precision
registers, add/multiply gates, local precision constraints, the literal
geometric layout, and an off-domain full-space law are not compiled. The exact
nonlocal Schur symbol is also not solved; only its frozen local quartic
approximant is.

## Route C — Cycle-581 in-state Cesaro phase filter

For each of the 24 co-present edge sectors, Route C uses the actual scaled
Cycle-576 edge Hessian and the Cycle-581 generalized symmetric update with
eight repetitions. Let that finite product be `U`. The in-state response
program accumulates

```text
F_N b = theta sum_(n=1)^N (1-n/(N+1)) (U^-n-U^n)/(2i) b.
```

There is no host inverse in the update. Forward and inverse powers are enacted
by the same exact inverse finite product. For exact
`U=exp(-i theta H)` and nonzero eigenvalue `lambda`, the Cesaro multiplier
tends to

```text
(theta/2) cot(theta lambda/2)
  = 1/lambda + O(theta^2 lambda).
```

The multiplier at an exact zero phase is zero. The frozen schedule is
`N=2048 L^2`; train L3 and held L4/L5 use no refit. Host eigendecomposition is
used only after execution to compare with the Moore-Penrose range response and
to measure zero-subspace leakage.

Controls include:

- update unitarity and exact inverse oddness;
- source deletion;
- all 24 co-present sectors and all 576 frame products;
- held-size response and equation residuals;
- the raw source's null projection; and
- leakage of the finite-product filter output into the target zero subspace.

The filter approximates the range pseudoinverse, but it does not close the full
raw equation because the raw source retains its fifth-zero component. A
physical coherent accumulator/program layout, endogenous schedule, literal M2
layout, and exact constrained-source preparation remain open. Filter steps are
not physical time, and the supplied finite-volume momenta remain host
parameters.

## Route dispositions

| Route | Constructed | Exact residual | Disposition |
|---|---|---|---|
| A — metric Schur | Gauge-invariant `h_44` operator and actual raw-source reduction; train-frozen quartic law; held directions | operator correction is `4/3` of graph; raw response is contact-like; fifth edge zero requires constraint | strongest analytic construction; does not join the actual source to the graph Green surface |
| B — local solver | positive 19-point proper-cubic approximant; reversible-tape Richardson law; rigorous finite-volume error | exact Schur operator and physical-M2 arithmetic/layout remain open | constructive approximant and resource law, not physical compiler |
| C — phase filter | in-state Cesaro range response of Cycle-581 symmetric edge update; inverse/deletion/covariance/held controls | raw source has nonzero fifth-zero component; finite-product and accumulator leakage remain | positive range-response partial, not full raw-source solve |

No route failure is treated as constitutional evidence. The three routes have
different residuals, and several normalized route families remain unattempted.

## Cold results and exact residuals

The final cold run reports `TOTAL: PASS=16 FAIL=0`.

Route A:

- maximum metric-null residual: `5.953535738288963e-16`;
- maximum raw metric-source Ward residual: `3.064175366435204e-15`;
- maximum static-scalar/gauge overlap: `1.4322618290199035e-14`;
- maximum all-24 scalar covariance residual: `2.914335439641036e-16`;
- positive null-space penalty invariance is tested at `0.25`, `1`, and `4` on
  five train/held/generic momenta: maximum normalized-operator change
  `4.679416576447437e-16`, normalized-source change
  `1.8735013540549517e-15`, and scalar-response change
  `3.5260683262095e-13`;
- frozen `a`: `-0.08333333824522242`;
- frozen `b`: `0.05555556396305736`;
- frozen correction ratio: `1.3333334427210133`;
- frozen conditional correction coefficient: `0.06631456506211993`
  (`5/(24pi)` within runner tolerance), versus graph
  `0.0497359197162173`;
- held quartic absolute residuals: `7.989819743314808e-12`,
  `5.390213015515899e-13`, and `7.246404431365816e-12`;
- train/held scalar responses: `1.9999999188108237`,
  `1.9999999949212053`, and `1.9999999919247664`; and
- raw-source fifth-zero projection fractions: `0.3656944047875198`,
  `0.5171803585775666`, and `0.5066984382913546`.

Route-B exact residuals:

| Fixture | Iterations | Rigorous relative bound | Observed solution residual | Equation residual | Full-tape real registers |
|---|---:|---:|---:|---:|---:|
| train L5 dipole | 87 | `9.092067019340068e-9` | `4.169339647372556e-9` | `3.2380118036544916e-9` | 11,125 |
| held L7 quadrupole | 169 | `9.790215423950217e-9` | `1.567779763438272e-9` | `2.8422691513134008e-9` | 58,653 |
| held L9 random | 279 | `9.582802079693651e-9` | `4.57795064772583e-9` | `9.880941720230414e-10` | 204,849 |

The 19-point operator's all-24 covariance residual is
`9.419082675407656e-15`; reverse-tape consistency, restoration, and source
deletion residuals are exactly zero in all three fixtures.

Route C:

| Fixture | Cesaro terms | Range-response residual | Range-equation residual | Raw-source null fraction across frames | Maximum target-zero leakage |
|---|---:|---:|---:|---:|---:|
| train L3 axis | 18,432 | `0.03018596939867213` | `0.01148603692518695` | `0.3656944047875196`–`0.36569440478751974` | `9.69598367321276e-5` |
| held L4 face | 32,768 | `0.007722630331651129` | `0.0038531957411399595` | `0.23600536867583632`–`0.5171803585775665` | `0.00038323769690008547` |
| held L5 body | 51,200 | `0.006456460601985149` | `0.0031928736314509086` | `0.44460044241654784`–`0.5066984382913547` | `0.000948648854662332` |

The maximum symmetric-product unitarity residual is
`1.960188175432285e-14`; inverse-filter oddness, source deletion, and all-576
sector-product momentum residuals are exactly zero. Runtime and memory are
reported by the cold transcript rather than treated as scientific constants.

## Supplied / derived / open inventory

### Supplied

- Cycle-576 edge variables, Regge action orientation, raw deficit row, metric
  map, source sign/coupling, update scale, and 24-sector carrier;
- Cycle-576 derived `-1/2` coefficient used only to normalize `K_R=-2S_44`;
- zero fourth momentum and the choice of `h_44` readout;
- Cycle-581 angle, symmetric factor order, eight repetitions, and finite
  filter schedule;
- train/held momenta, periodic volumes, zero-mean source fixtures, solver
  tolerance, full reversible tape, and terminal readout; and
- the independent graph Green theorem as a post-freeze comparison surface.

### Derived

- four-null gauge-controlled metric Schur operator and raw-source projection;
- `a=-1/12`, `b=+1/18` quartic coefficients and their held predictions;
- the conditional `4/3` cubic-correction ratio and `5/(24pi)` operator surface;
- the actual contact-like `h_44 -> 2` raw-source response;
- the raw source's nonzero overlap with the fifth edge zero;
- the 19-point local positive approximant and rigorous relaxation law; and
- the Cycle-581 Cesaro range-response construction.

### Open

- locally enforced metric-image/nonmetric-zero constraints on physical M2;
- an independently derived physical scalar source/readout that exposes rather
  than cancels the scalar pole;
- an explanation or constructive change of the `4/3` cubic-correction mismatch
  without fitting;
- an exact local implementation of the Schur operator rather than its quartic
  approximant;
- signed finite-precision M2 arithmetic, coherent filter accumulation,
  program genesis/readout, physical layout, and off-domain law; and
- nonlinear recurrence/backreaction, empirical scale, physical gravity, and
  any Newtonian identification.

## Six-wall TOE ledger

| Wall | Cycle-585 movement |
|---|---|
| `C_ref` | unchanged: the `h_44` scalar, zero-fourth-momentum surface, frame-sector preparation, filter schedule, and source/readout interpretation remain supplied; no physical reference genesis is derived |
| `C_num` | advances at a bounded mathematical level: the scalar symbol, two quartic coefficients, `4/3` ratio, finite-volume spectra, iteration counts, and errors are exact/numerically controlled; no empirical scale or number reference is selected |
| `C_wrap` | unchanged: inverse finite products and filter indices are explicit, but no step is time, no wrapped phase is energy, and no unbounded history carrier is derived |
| `C_int` | preserves the actual Cycle-230 contact and constructs linear Regge/static response approximants; no source/contact unification, nonlinear backreaction, rate, or protection theorem is derived |
| `C_local` | advances conditionally: a 19-point proper-cubic operator and reversible finite-volume solver are explicit, while exact metric constraints, signed arithmetic, literal M2 layout, coherent filter program, and off-domain law remain open |
| `C_source` | sharpens materially: the actual raw deficit source cancels the scalar pole in this readout and overlaps the fifth edge zero; a physical source that excites the scalar Green tail remains open |

## Maturity read

Cycle 585 does not rebase global maturity from one route. The carried
repo-wide / strict physical-M2 / evidence-ceiling coordinates remain:

| Lane | Carried coordinates | Cycle-585 delta |
|---|---:|---|
| operational quantum / records | `96 / 93 / 99` | held steady; mass/contact/seam/update controls are preserved, with no new Record or occurrence law |
| causal time | `79 / 76 / 99` | held steady; finite inverse/filter indices are not physical time |
| inertia / matter | `94 / 97 / 99` | held steady; the one-particle mass and contact fixtures are replayed, not re-derived |
| gravity / source | `82 / 77 / 94` | held steady pending source/constraint/static-physical closure; Cycle 585 sharpens the scalar operator, source cancellation, fifth-zero range condition, and local-solver target without completing the physical join |
| Born / probability | `84 / 73 / 99` | held steady; no norm, filter weight, or response is promoted to probability |

The qualitative delta is therefore a sharper gravity/source dependency surface,
not a global maturity promotion or setback. The coordinates are campaign
diagnostics, not audit statuses.

## No-Go Discipline Gate

The fresh `origin/main` no-go-discipline skill and registry/freshness checks
were read before writing this packet.

### N1 — Alternative route enumeration

1. **Metric-image Schur reduction — ATTEMPTED.** It derives a scalar pole but
   the actual source cancels it and the correction ratio is `4/3`.
2. **Finite-range relaxation with reversible tape — ATTEMPTED.** It solves a
   frozen local approximant, while exact-Schur and physical-M2 arithmetic remain
   open.
3. **Unitary Cesaro phase filter — ATTEMPTED.** It approximates the range
   response, while the unprojected source has a fifth-zero component.
4. **Cycle-216 six-mode scalar resolvent — RULED OUT BY PRIOR ONLY AS A
   DERIVATION FROM REGGE.** It proves `3/L` for its supplied operator, not for
   the Cycle-576 raw law, so it does not qualify as a failed route to the full
   terminal.
5. **Locally constrained edge/metric gauge code — OPEN / NOT COUNTED.** It
   could remove the fifth edge zero before response.
6. **Multigrid/domain decomposition — OPEN / NOT COUNTED.** It could improve
   finite-volume resource scaling.
7. **Block encoding and QSP inverse — OPEN / NOT COUNTED.** It could improve
   range handling and coherent inversion.

Only three normalized families qualify as `ATTEMPTED` or terminally
`RULED OUT BY PRIOR`. N1 therefore fails. Broad negative gate: FAIL / DO NOT
SHIP.

### N2 — Wall independence

The collapsed walls are:

- `W_constraint`: locally enforce the metric/nonmetric-zero constraint;
- `W_source`: derive a physical source whose reduced symbol does not cancel
  the scalar pole;
- `W_surface`: reconcile the `4/3` correction mismatch without fitting;
- `W_solver`: compile signed finite-precision solver arithmetic into M2; and
- `W_filter`: compile coherent phase accumulation and exact range handling.

Every pair is tested in the runner. Closing any one supplies neither direction
of implication for any other: a constraint does not derive a source, a source
does not alter the operator correction, an operator correction does not compile
arithmetic, and a solver does not compile a unitary accumulator. The five-wall
set therefore does not collapse further in this cycle.

### N3 — Hidden-wall scan

Action orientation, metric map, frame average, gauge penalty, `-2`
normalization, train momenta, held momenta, finite volumes, solver tolerance,
filter repetitions, filter length, host momentum, tape, and readout are all
explicit. “By construction” is not used to hide locality or physical
provenance. Cycle 460 is explicitly non-load-bearing.

### N4 — Residual matching

| Witness | Witness residual | Current residual | Match? |
|---|---|---|---|
| Cycle 576 | raw Regge law exists; downstream static scalar open | actual raw-law static reduction | yes |
| Cycle 581 | finite symmetric raw-Regge update | phase-filter response from that update | yes |
| Cycle 216/420 | supplied scalar operator and unconstructed physical solver | comparison surface/solver only | no; not closure evidence |
| Cycle 460 | compile supplied finite receiver kernel | derive homogeneous Regge response | no; not evidence or premise |

### N5 — Rhetoric audit

- “The raw source has no inverse-`L` pole” is restricted to the tested
  gauge-invariant `h_44` metric-image reduction at `k_4=0`. Other observables,
  nonlinear sectors, and alternative sources are untested.
- “The reference surface does not match” is restricted to the quartic
  long-wave coefficient of Route A's normalized scalar Schur operator. Other
  constraint reductions are untested.
- “The phase filter does not solve the full raw equation” is restricted to
  the three finite fibers, all24 sectors, and this unprojected source. A
  constrained preparation or QSP route is untested.

No broader lattice-wide or constitutional negative is stated.

### N6 — Partial-closure paths

Three live constructive paths are explicit: derive and locally enforce the
metric-image constraint; derive a matter/source coupling to the gauge-invariant
scalar rather than to the deficit row; and compile either the local relaxation
or a block-encoded inverse with precision/M2 resources. The fresh primitive
registry check was read. No “no retained primitive,” “new axiom required,” or
equivalent claim is made.

### N7 — Hostile steelman

A hostile reviewer should reject any no-go here: Route A already exhibits the
desired scalar pole, and Route B gives a local positive approximation to its
operator. A local constrained edge code could remove the fifth zero branch; a
matter-derived `h_44` source could then expose the pole rather than cancel it;
and a block-encoded/QSP inverse could replace the Cesaro filter. The terminal
obligation is concrete: derive the constraint and source from the physical
code, compile their M2 select/prepare/inverse layout, and reproduce held
response and all24 covariance with no momentum normalization. This steelman is
actionable, so any broad negative is premature.

### N8 — Cross-cycle echo

Cycle 576 repaired a normalized-source error by returning to the raw local
action. Cycles 579/581 converted a generator-only wall into explicit finite
product programs. Cycle 495 supplied multiple local solver approximants while
leaving physical arithmetic explicit. Those cycles show that constraint,
program, and solver walls can narrow constructively; the same mechanisms remain
live here.

**Gate status:** FAIL. The artifact is demoted to positive partial construction
with explicit residuals. No shared obstruction, minimum-content claim, or axiom
pressure may ship.

## Optimal next campaign

The highest-value next campaign is a constrained-source join:

1. derive a finite-range real-space constraint whose code is exactly the
   metric image or another range-complete physical edge sector;
2. prove that the constraint removes the fifth zero locally and is preserved
   by the actual Cycle-581 update;
3. derive, rather than choose, a physical scalar source/readout and determine
   whether its reduced symbol exposes the `K_R` pole;
4. compile a block encoding or rigorously local solver for the exact
   constrained operator, with precision and M2 resources; and
5. freeze before comparing the leading and cubic Green surfaces on new held
   momenta and volumes.

That campaign tests whether the present residual is source/constraint-specific.
It does not edit axioms and does not presume that the graph correction must be
recovered.

## Frozen verification receipt

- runner SHA-256:
  `70d98e5493df503f5fe353f31caf50f967b7e35c7471f01ba529de3a6a4a7c99`;
- frozen cold transcript SHA-256:
  `ebebc5bf0eaa26fe957c9295d997da613071f1e5c98fbeb5b66311baa125d703`;
- cold result: `PASS=16 FAIL=0`, external elapsed `26.72 s`, maximum
  resident set size `141,950,976` bytes, and zero swaps.

Parent verification checked the Schur/gauge algebra, the quartic-to-Green
coefficient rewrite, raw-source scaling, the fifth-zero range condition, the
Route-B error theorem, Cycle-460 nonuse, maturity coordinates, and N1--N8.
It then independently reran the frozen runner: 16/16 passes in `20.85 s`,
maximum resident set size `142,737,408` bytes, peak memory footprint
`125,895,208` bytes, and zero swaps. The parent transcript SHA-256 is
`6cf1a3ea43eab79f60b084634f56c7dd3957fc5b5e001b95ac7412a44d5e5ea9`.

This receipt-only note edit changes neither the runner nor the frozen cold
transcript.
