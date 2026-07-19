# Physical signed transverse source / test-matter prediction — Cycle 432

Date: 2026-07-19
Authority: none
Audit: unset

## Scope and result

This cycle constructs a bounded **phase-coded transverse dipole seam** from the
Cycle-425/426/429 substrate.  Three physical M64 matter cells are compiled into
physical M2: two transversely separated source cells and one distinct receiver
cell.  Each lattice cell has one reservoir M2 and six directional field M2,
and the field declaration is the complete global Q=1 sector.  The two source
reservoirs are prepared as

\[
  (|R_{S_1}\rangle+e^{i\phi}|R_{S_2}\rangle)/\sqrt{2}.
\]

Thus the two source occupations are always `(0.5, 0.5)` and **no occupation is
negative**.  The sign is carried by local relative phase and appears as an
interference contrast at a physical test-matter receiver effect.  No
expectation value controls a gate.

On the declared physical code,

\[
  E_{432}G_{432}=G_{\mathrm{physical},432}E_{432},
\]

with an exact inverse up to floating-point residual.  This is a positive
near-side bridge.  It is not the full Cycle-420 impact-parameter or
quadrupole-width prediction surface.

Runner contract: `E_432 G_432 = G_physical,432 E_432`.

## Fixed construction

The fixed update order is:

1. the Cycle-219 local matter coin on all three matter cells;
2. the Cycle-425 six-direction field coin on every cubic cell;
3. the same Cycle-426 coefficient-two even-CAR recoil vertex at source one,
   source two, and receiver;
4. the Cycle-425 nearest-neighbor cubic field stream;
5. the Cycle-230 local contact phase.

The matter code is the Cycle-319/396 988-column `n=0,...,3` three-cell code.
Its Cycle-269 local checks and Wilson sector locally enforce the inherited
auxiliary/gauge constraints.  All six local matter-factor orders are tested.
There is no global Jordan–Wigner string, nonlocal parity service, or preferred
global ordering.  The displayed factor order is supplied candidate-law
content; it is not derived or autonomous.  Once supplied, it is fixed: no
runtime host branch, state query, expectation query, or adaptive control
selects or changes a factor.  Identity completion outside the declared code
image is supplied, as in the inherited physical compiler.

The receiver effect is the local rank-one scalar-mode effect
`|uniform,n=1><uniform,n=1|` on the third M64 matter cell, tensored with the
identity on the other matter cells and the field.  The receiver reservoir is
also read out.  These are coherent finite-state coordinates, not occurrence
counts or probabilities.

## Training and blind held geometries

The update, source coupling, phase convention, receiver effect, and propagation
rule are frozen before the held rows.

| row | L | sources | receiver | depth | role |
|---|---:|---|---|---:|---|
| train `b1_d2` | 5 | `(0,2,1)`, `(0,2,3)` | `(2,2,2)` | 4 | calibration |
| held translated `b1_d2` | 6 | `(1,3,2)`, `(1,3,4)` | `(3,3,3)` | 4 | translated origin |
| held `b1_d3` | 6 | `(0,3,2)`, `(0,3,4)` | `(3,3,3)` | 5 | longitudinal separation |
| held `b2_d2` | 6 | `(0,3,1)`, `(0,3,5)` | `(2,3,3)` | 5 | transverse separation |

This is the held translated origin, longitudinal separation, and transverse
separation family.  There is **no refit** on any held row.  Linear propagation
gives the frozen phase law

\[
 W(\phi)=B+\operatorname{Re}(e^{i\phi}K).
\]

The signed coordinate reported below is the coherent contrast about the
incoherent two-source baseline `B`; it is not a negative occupation.

## Numerical prediction rows

### Receiver reservoir

| geometry | `W(0)` | `W(pi)` | signed contrast at `0` | signed contrast at `pi` |
|---|---:|---:|---:|---:|
| train `b1_d2` | `1.993104010517520e-5` | `1.268338915783875e-5` | `+3.623825473668225e-6` | `-3.623825473668225e-6` |
| held translated | `1.993104010517520e-5` | `1.268338915783875e-5` | `+3.623825473668225e-6` | `-3.623825473668225e-6` |
| held `b1_d3` | `9.059563684170564e-6` | `5.435738210502330e-6` | `+1.811912736834117e-6` | `-1.811912736834117e-6` |
| held `b2_d2` | `6.945665491197451e-6` | `5.133752754363326e-6` | `+9.059563684170624e-7` | `-9.059563684170624e-7` |

### Local physical test-matter receiver effect

| geometry | effect at `0` | effect at `pi` | signed contrast at `0` | signed contrast at `pi` |
|---|---:|---:|---:|---:|
| train `b1_d2` | `0.9999853991551550` | `0.9999901320355971` | `-2.366440221008881e-6` | `+2.366440221008881e-6` |
| held translated | `0.9999853991551532` | `0.9999901320355952` | `-2.366440221007620e-6` | `+2.366440221007620e-6` |
| held `b1_d3` | `0.9999939748491573` | `0.9999955527717983` | `-7.889613205507204e-7` | `+7.889613205507204e-7` |
| held `b2_d2` | `0.9999952755820130` | `0.9999959303275752` | `-3.273727811347154e-7` | `+3.273727811347154e-7` |

At `phi=+-pi/2` the signed contrasts are at most `7.4e-18`, as required by
the reflection-symmetric geometry.  The translated train/held readout
residual is `1.887379141862766e-15`.  Norm errors over the independently
propagated source bases are below `1.8e-14`.

## Compiler, inverse, covariance, and ledgers

The train and held-transverse matter encodings both have shape
`(261728, 988)`.  The exact checks are:

| control | maximum residual |
|---|---:|
| all-six-order matter Gram | `7.771561172376096e-16` |
| `E_432 G_432 - G_physical,432 E_432` | `6.697144058277748e-15` |
| physical adjoint inverse | `4.719092552162576e-15` |
| output norm error | `4.279e-13` |
| matter coin/contact/receiver all-frame covariance | `1.668319065437718e-16` |
| recoil source all-frame covariance | `8.807749891993861e-16` |
| field coin/stream all-frame covariance | `0` |
| rotated phase-labelled geometry seed | `0` |

All 24 proper-cubic frames are tested.  The phase labels travel with their
source cells under a frame; no preferred axis is retained.

The Cycle-219 one-particle mass fixture is preserved:
`m=0.4534056541748851`, with uniform one-particle eigenvector residual
`3.534751832054436e-16`.  The Cycle-230 contact remains nontrivial on 645
logical columns.

The coefficient-two direction ledger is exact at the receiver vertex.  On the
reflection-symmetric prepared history the matter-direction and twice-field
direction changes are individually null to roundoff, and their sum has norm
below `2.3e-19`.  This is a direction ledger only: **direction is not force,
momentum, energy, stress, or gravity**.

Resource ledger:

- train matter-support union: 132 M2;
- held-transverse matter-support union: 136 M2;
- maximum joint matter branch before the local role register: 51 M2;
- seven field M2 per cubic cell;
- inherited homogeneous matter-plus-field accounting: 36 M2 per active
  coarse cell;
- maximum active recoil-vertex support: 25 M2;
- common logical dimensions: `988 * 875 = 864500` on L=5 and
  `988 * 1512 = 1493856` on L=6.

These are bounded constants per installed coarse cell.  The physical ray count
is not itself an on-site Hilbert dimension.

## Deletions

The runner includes source-one, source-two, receiver, stream, coherence, and
contact deletions.

The training reservoir signed contrast is `3.623825473668225e-6`.  Deleting
source-one coupling, source-two coupling, receiver coupling, the stream, or
coherence independently changes that contrast to exactly zero at the runner
tolerance.  Blank or incoherent source preparation cannot create the signed
coordinate.

Contact deletion is intentionally reported with its scope.  It changes a
declared two-particle code state by `0.36789306705608243`, proving that the
Cycle-230 factor is present.  It changes this prepared one-particle-per-cell
prediction history by exactly zero because local number is fixed at one.  The
contact is therefore not called a driver of the present response.

## Exact Cycle-420 boundary

The bounded phase-source seam and bounded physical receiver effect are both
constructed.  Nevertheless, the Cycle-420 impact and quadrupole named-surface
flags remain false:

| surface | near-side phase source | near-side physical receiver | Cycle-420 `physical_source_EG` | Cycle-420 `physical_test_matter_readout` | named surface closed |
|---|---|---|---|---|---|
| impact parameter | true | true | false | false | false |
| quadrupole width | true | true | false | false | false |
| diamond/NV | true | true | false | false | false |

For impact parameter, this source is not the frozen positive host
`strength/r` family at `b=(5,6,7,8,10)`, and the receiver effect is not the
host detector centroid or its log-log fit.  For quadrupole width, two coherent
sources are not the host signed `(+1,-2,+1)` profile, and there is no propagated
packet centroid/width.  For diamond/NV, the relative phase is physical but the
receiver is not the frozen host lock-in `X,Y,phi` surface.  There is no host
profile join, packet join, centroid join, width join, or fitted continuum law.

## Supplied / derived / open

Supplied:

- the Cycle-319/396 physical three-cell M64 compiler, local gauge constraints,
  six factor orders, and identity completion;
- the Cycle-426 coefficient-two even-CAR recoil vertex and fixed calibration;
- the Cycle-425 cubic hard-core Q=1 field coin and stream;
- the Cycle-420 exact comparison contracts;
- the relative phase, coordinates, preparation, receiver effect, and update
  depths.

Derived here:

- a bounded phase-coded transverse source seam with positive occupations;
- a distinct physical test-matter receiver effect with a signed contrast;
- translated, longitudinal, and transverse held propagation without refit;
- physical E/G, inverse, deletion, coefficient-two, mass/contact, resource,
  and all-frame checks;
- the exact reason the Cycle-420 named surfaces remain open.

Open:

- a physical positive `strength/r` family on the Cycle-420 frozen impact
  domain and its detector-centroid/log-fit join;
- a physical three-source `(+1,-2,+1)` quadrupole profile, propagated test
  packet, and centroid/width join;
- autonomous phase preparation and recurrence;
- primitive synthesis replacing inherited matrix-unit identity completion;
- higher-Q histories, a contact-work law, physical clock, Records, Born law,
  energy/stress/source selection, metric, and gravity.

Step count is not time.  Coherent weight is not a Born law or a Record.  The
reservoir and field occupation are not physical energy or gravitational
source.  No no-go, minimum-content, shared-obstruction, or axiom-pressure
claim is made.

## Reproduction

```bash
python3 scripts/physical_signed_transverse_source_test_matter_prediction_cycle432_2026_07_19.py
```

Expected cold result: `PASS 12 / FAIL 0` and
`PHYSICAL_SIGNED_TRANSVERSE_SOURCE_TEST_MATTER_PREDICTION_CERTIFIED`.
