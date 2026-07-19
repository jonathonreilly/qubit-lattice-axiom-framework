# Physical recoil/contact to hard-core field bridge — Cycle 426

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is edited or proposed.

Companion runner:

```text
scripts/physical_recoil_hard_core_field_bridge_cycle426_2026_07_19.py
```

## Result up front

Cycle 426 supplies the missing bounded near-side join between the carried
matter-recoil source of Cycle 322 and the literal hard-core reservoir/field
sites transported in Cycle 423.

The common logical code is

```text
M64 tensor M64 tensor complete total-Q<=2 fourteen-M2 field code,
dimension = 4096 x 106 = 434176.
```

The field installation is two ordinary seven-M2 stars: one reservoir M2 and
six directional field M2 at each endpoint. It has no global zero/one-field
blockade. The `Q=2` sector contains all 91 two-excitation placements of the
fourteen hard-core bits.

On each endpoint, one **fixed hard-core recoil generator** extends the
Cycle-322 source law from its seven abstract `Q=1` labels to ordinary
reservoir and field occupations. On the old `Q=1` sector the encoding and
generator intertwiner are exact. On the new `Q=2` sector the same expression
acts without a separate branch law and supports simultaneous two-source
emission, transport, collision, and absorption.

Together with the existing Cycle-315 physical matter compiler, the common
encoding is

```text
E_common = E_315 tensor I_(complete Q<=2 field code).
```

The runner checks on a seeded mixed `Q=1/Q=2` probe

```text
E_common G_common = G_physical,common E_common
```

with forward residual `1.3914314946587405e-15`, adjoint-inverse residual
`2.4377304619541554e-15`, and output norm
`0.9999999999999982`. The factor construction preserves the declared code;
the finite probe is not advertised as exhaustive materialization of the
434,176-column operator.

This is a constructive common-code result. It makes no claim that excitation
number is energy, that the prepared reservoir is a selected physical source,
or that the schedule is physical time.

The certified controls include field emission, transport, and absorption;
one-source and two-source histories; reciprocal A-to-B and B-to-A response;
source coupling, calibration, and blank preparation; and source, coupling,
contact, and transport deletions.

## Fixed source law

For direction `d`, let `bar(d)` be its opposite. On one local six-mode CAR
cell and one seven-M2 reservoir/field star, define

```text
H_rec = sum_d [
    a^dagger_bar(d) a_d sigma_R^- sigma_d^+
  + a_d^dagger a_bar(d) sigma_R^+ sigma_d^-
],

V_rec(theta) = exp(+i theta H_rec).
```

The hard-core raising operator acts only when field bit `d` is blank; the
conjugate term absorbs only when it is occupied. The even-CAR matter hop
reverses the carried direction at the same time. No global Jordan--Wigner
ordering, nonlocal parity service, or host-side expectation query is used.

The supplied coupling and calibration are

```text
theta = 0.8 m = 0.3627245233399082,
m = Cycle-219 analytic mass = 0.4534056541748851.
```

The normalization `0.8`, angle sign, source invocation, reservoir occupation,
and blank field preparation remain supplied candidate-law content. The same
mass-normalized angle appears in Cycles 416 and 422 to within
`1.6653345369377348e-16`; that numerical agreement does not select a physical
source interpretation.

The source generator has these complete sparse-sector controls:

| local `Q` | dimension | nonzero entries | Hermiticity | `[H,N_matter]` | `[H,Q]` | three recoil commutators |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 64 | 0 | 0 | 0 | 0 | `(0,0,0)` |
| 1 | 448 | 192 | 0 | 0 | 0 | `(0,0,0)` |
| 2 | 1344 | 960 | 0 | 0 | 0 | `(0,0,0)` |

The vector coordinate is

```text
P_rec = P_matter + 2 sum_d n_field,d direction(d).
```

It is the Cycle-318/322 coefficient-two recoil ledger. It is not physical
momentum calibration, energy, stress, source work, force, or a rate.

## Exact Cycle-322 seam

The local isometry is

```text
|mask; R>   -> |mask> |R=1,F=000000>,
|mask; F,d> -> |mask> |R=0,F=1_d>.
```

On all 448 old local basis states:

| control | residual |
|---|---:|
| isometry Gram | `0.0` |
| generator intertwiner | `0.0` |
| finite-unitary seeded forward intertwiner | `1.2386832183404543e-16` |
| finite-unitary seeded inverse | `1.6128901471693564e-16` |

Thus the Cycle-322 source is not merely relabeled: it is exactly the
one-excitation restriction of the new physical seven-M2 law. The `Q=2`
extension is the same hard-core expression with spectator occupations, not a
second source rule.

## One fixed reversible schedule

The two-cell update is

1. the complete Cycle-315 matter onsite coin;
2. the Cycle-423 full hard-core field coin on each six-field block;
3. the fixed recoil source at A and then at B;
4. the literal Cycle-315 edge FSWAP;
5. one exact Cycle-423 directed boundary field-bit SWAP; and
6. the literal Cycle-230 contact.

The adjoint uses the exact reverse factor order. Scheduled adjoint return is
not autonomous recurrence and the factor order is not physical time.

Each onsite source preserves its block `Q`; only the boundary SWAP changes
block `Q`. Therefore

```text
Delta Q_A = boundary current A
```

for the stream layer. On the one-source history the current is
`-0.020983202688118992`, exactly the neighboring field gain within the stated
tolerance. On the symmetric two-source history the signed net current is zero
while two opposite transfers occur; the block-continuity residual is `0.0`.
This is an excitation/current ledger, not energy, source, work, rate,
probability, or a Record.

## One-source history and reciprocity

Preparation is explicit:

```text
R_A=1, R_B=0; all twelve field M2 blank;
matter = symmetric one-particle-per-endpoint Cycle-322 fixture.
```

After one update, neighboring-block field weight is

```text
0.020983202688118992
```

against `sin^2(theta)/6 = 0.020983202688118957`. Total `Q` remains one. The
adjoint returns to the prepared state with residual
`2.132775682859071e-15`.

After two forward updates the fixed-schedule reservoir response is

```text
[[0.668995977708231,     0.0003174846213078961],
 [0.0003174846213078959, 0.668995977708231    ]].
```

The A-to-B/B-to-A reciprocity residual is
`2.168404344971009e-19`; maximum norm drift is
`3.552713678800501e-15`. Deleting the receiver source or transport sets the
A-to-B entry to zero. Unequal endpoint couplings preserve off-diagonal
reciprocity but split the diagonal entries:

```text
[[0.668995977708231,      0.00042755700725233823],
 [0.00042755700725233785, 0.5728843763990464    ]].
```

These are coherent occupation weights, not Born probabilities.

## Two-source and hard-core controls

The two-source preparation is

```text
R_A=R_B=1; all twelve field M2 blank; Q_total=2.
```

After one update:

| control | result |
|---|---:|
| total two-field weight | `0.015850612621824613` |
| expected `sin^4(theta)` | `0.01585061262182457` |
| same-block two-field weight after transport | `0.0044029479505068355` |
| same-block two-field weight with transport deleted | `0.0` |
| total `Q` residual | below `3e-12` |
| adjoint return | `2.196979120236114e-15` |

A second forward update retains positive two-field weight
`0.10102814250675797` and exact `Q=2` conservation. An occupied/occupied
boundary `11` input remains `11` under SWAP with residual `0.0`. The local
`R=1,F=111111` state has no emission edge; the saturated generator has zero
entries on that sector.

This supplies genuine same-law two-source histories rather than the old
global-`Q=1` blockade.

## Physical support, covariance, and held controls

The physical installation inherits 29 matter M2 per coarse cell from Cycle
315 and adds seven literal reservoir/field M2 per cell:

| surface | M2 support |
|---|---:|
| homogeneous common installation per cell | 36 |
| two-cell matter patch | 83 |
| two-cell common patch | 97 |
| one endpoint matter support | 18 |
| one endpoint recoil-source union | 25 |
| local field coin | 6 |
| boundary SWAP | 2 |

The matter constraints are the inherited local checks plus the declared
Wilson sector. The hard-core field sites are literal M2 and add no auxiliary
gauge constraint.

The runner checks:

- source-generator covariance in all 24 proper-cubic frames through `Q=2`,
  with maximum residual `0.0`;
- directed-edge transport covariance in all 24 frames, maximum residual
  `0.0`;
- the inherited matter/contact edge-role family in all 24 frames, including
  12 endpoint-preserving and 12 endpoint-reversing frames;
- 93,312 inherited edge-role group-law tests and 4,374 L3 translation tests,
  with zero failures;
- 186 new origin/direction edge-layout tests across `L=3,4,6`, including
  held `L=6`, with zero failures; and
- the 4,096-column matter Gram operator through `L=3,4,6`, with reported
  operator-norm residual `0.0` at every size.

The fixed two-block boundary is a bounded patch result. A homogeneous
multi-edge cubic transport network is not constructed here.

## Mass, contact, deletions, and lawful domain

The one-particle mass fixture remains

```text
Cycle-219 mass            0.4534056541748851
two-cell rest mass        0.4534056541748851
uniform eigenvector error 3.8571762755144336e-16.
```

The literal Cycle-230 contact remains nontrivial on 4,047 matter columns.
Its deletion operator norm is `1.9923680249729583`; a seeded common-history
contact deletion changes the state by `1.5270510754000866`. Contact remains a
factor of the same update, but no contact-work continuity equation is claimed.

Deletion controls are independent:

- coupling deletion `theta=0` produces zero field emission;
- receiver-source deletion produces zero A-to-B reservoir response;
- transport deletion produces zero neighboring field and zero same-block
  two-field arrival;
- contact deletion is visibly nontrivial; and
- field-coin deletion changes a seeded history by `1.1547005383792526`.

The runner rejects a negative local-Q label, an invalid omitted direction, an
invalid endpoint, an invalid edge direction, and a total-`Q=3` state outside
the declared common code. The latter is a lawful-domain control, not evidence
against broader sectors.

## Relation to Cycles 294, 221, 416, 422, and 423

Cycle 294 Route B supplied a bounded `mN tensor X_s` deformation with exact
physical support and covariance. It did not supply recoil or a common
matter-field continuity law. Its `0.6322439777544321` port residual is a
direct-source mismatch for a supplied additive port, not a residual of this
hard-core autonomous history; no match is claimed.

Cycle 221 showed conditional consistency of a supplied mass operator across
separate effective kernels and explicitly found that equal-direction contact
geometry, not that mass operator, supplied its tested binding. Cycle 426 uses
only the Cycle-219/315 mass/contact fixture and makes no operator-equivalence,
binding, or gravity inference.

Cycle 416 made an exact three-M2 source/mediator number balance but passed its
mediator expectation to the far-side field on the host through a supplied
expectation-to-source map. Cycle 422 physically moved that one excitation
into a seven-M2 scalar field star while matter/recoil/contact remained
spectators. Cycle 426 instead couples the seven-M2 star directly to the even
CAR matter hop, so recoil, source depletion, contact, field coin, and boundary
transport now coexist on one physical code. It does not inherit Cycle 416's
strict-response control or its far-side Cycle-213/216 receiving map.

Cycle 423 supplied complete two-block total-`Q<=2` hard-core transport with
matter/contact as spectators. Cycle 426 replaces the spectator source vertex
by the recoil-balanced matter-controlled vertex while preserving the field
coin, collision-safe SWAP, total-`Q<=2` basis, and two-source transport.

## Supplied, derived, and open

Supplied:

1. the Cycle-315 complete `M64 tensor M64` physical matter seam, its local
   checks/Wilson sector, coin, FSWAP, and Cycle-230 contact;
2. the Cycle-322 coefficient-two recoil convention and local six-mode CAR
   ordering;
3. two reservoir M2, twelve directional field M2, and the complete
   total-`Q<=2` preparation;
4. the Cycle-423 full hard-core field coin, directed boundary SWAP, and factor
   order;
5. `theta=0.8m`, including normalization, sign, zero, source invocation, and
   blank reservoir/field preparations; and
6. the two-cell boundary, histories, frames, origins, and tolerances.

Derived:

1. the fixed hard-core recoil generator through `Q=2` and exact Cycle-322
   `Q=1` isometry;
2. a 434,176-dimensional common logical code and its physical-M2 factorwise
   intertwiner;
3. local matter-number, total-excitation, coefficient-two recoil, and
   boundary-current ledgers;
4. one-/two-source emission, transport, absorption, reciprocal response,
   collision, saturation, inverse, and deletion controls; and
5. bounded support, all-24-frame covariance, and held-size/origin controls.

Open:

1. primitive synthesis of the bounded source-star exponential and autonomous
   same-forward recurrence;
2. a homogeneous full cubic multi-edge field network, `Q>2` histories,
   autonomous prepared-source creation, and a contact-work ledger;
3. selection/calibration as physical energy, stress, source, force, universal
   clock response, tensor/metric response, or gravity;
4. actual Records, physical time, Born law, and empirical calibration.

No host expectation controls a gate. A generator is not called a rate;
wrapped phase is not called energy; number is not called energy/source/work;
the schedule is not called time; and coherent weights are not called Born
probabilities.

## Six-wall ledger effect

| wall | Cycle-426 effect | still open |
|---|---|---|
| `C_ref` | the explicit reservoir removes a common-phase ambiguity from the local number balance | source preparation, coupling zero/normalization, physical calibration |
| `C_num` | one common physical code now carries complete `Q<=2`, local matter number, and coefficient-two recoil ledgers | `Q>2` histories and physical energy/stress interpretation |
| `C_wrap` | unchanged; no update count or wrapped phase is promoted | event equivalence, clock admission, interval/rate calibration |
| `C_int` | matter recoil, field emission/absorption/transport, FSWAP, and literal contact now share one reversible schedule | contact-work balance, stable dressed objects, autonomous recurrence |
| `C_local` | exact Q1 source isometry plus bounded Q2 extension, 97-M2 patch, all frames, and held L6 | primitive synthesis and homogeneous multi-edge lattice execution |
| `C_source` | a prepared reservoir is consumed/restored locally without an expectation-derived gate or far-side host injection | source selection/calibration, far-side response under the same law, tensor/metric dynamics |

`C_int`, `C_local`, and the near side of `C_source` are narrowed. No wall is
declared closed.

## Scientific disposition

This positive construction does not trigger a negative N1--N8 verdict. The
no-go-discipline guardrail was applied as a rhetoric check: no impossibility,
minimum-content, shared-obstruction, or axiom-pressure conclusion is made.
Broader `Q`, lattice, work, clock, and metric sectors are left as unfinished
constructive work.

No negative, no-go, minimum-content, shared-obstruction, or axiom-pressure
claim is made. Authority remains none and audit remains unset.

## Verification

```bash
python3 -m py_compile \
  scripts/physical_recoil_hard_core_field_bridge_cycle426_2026_07_19.py

python3 -u \
  scripts/physical_recoil_hard_core_field_bridge_cycle426_2026_07_19.py
```

Expected cold result:

```text
RESULT PHYSICAL_RECOIL_HARD_CORE_FIELD_BRIDGE_CERTIFIED
```
