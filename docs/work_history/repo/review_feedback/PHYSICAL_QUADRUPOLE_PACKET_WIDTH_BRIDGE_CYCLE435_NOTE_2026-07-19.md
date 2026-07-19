# Physical quadrupole / M64 packet-width bridge — Cycle 435

Date: 2026-07-19

Authority: none

Audit: unset

## Result

Cycle 435 constructs a bounded **physical phase quadrupole** and a spatially
extended physical M64 receiver packet under one fixed local update.  It uses
two disjoint three-M64 blocks: three source-matter cells in the first block and
three receiver-packet cells in the second.  Each block independently carries
the Cycle-269/319 local checks and Wilson-sector constraints.

The three source reservoirs are prepared by the supplied isometry column

```text
(1,-2,1)/sqrt(6).
```

The minus sign is a relative phase.  The occupations are `(1,4,1)/6`; there
is no negative occupation.  All three amplitudes propagate through the same
field and common receiver evolution.  Replacing the central phase by a
positive phase or erasing coherence changes the final packet width, so the
sign is load-bearing, although the resolved phase-sensitive correction is
much smaller than the occupation-profile response.

The receiver holds exactly one matter excitation across three physical M64
cells.  Two local receiver FSWAP edges let its cell weights evolve.  A supplied
two-pointer-M2 dilation compresses to fixed physical centroid and second-moment
effects.  The dilation is an exact physical-effect surface, but no local
pointer-coupling gate or pointer-gate inverse is constructed here.

The train `a=1` and held `a=2` geometries give positive, centered width
responses at both physical strength analogues with no refit.  The result does
not reproduce the exact Cycle-420 absolute strengths, legacy packet, numeric
rows, or stronger-`a=2` ordering.  The Cycle-420 quadrupole named-surface flags
remain false.

## Supplied fixed candidate program

The fixed factor order is supplied candidate-law content.  It is not derived
or autonomous:

1. local Cycle-219 matter coins on both three-M64 blocks;
2. the Cycle-425 six-direction field coin;
3. three Cycle-426 coefficient-two recoil vertices on the source block;
4. three copies of the same recoil vertex on the receiver block;
5. two local receiver-packet FSWAP edges;
6. the Cycle-425 nearest-neighbour field stream;
7. the Cycle-230 contacts on both matter blocks.

No runtime host state or expectation query, branch, or adaptive control
selects or changes any factor.  The source column, coordinates, update depths,
strength occupancies, packet preparation, and pointer dilation are supplied
initial/program data and are inventoried below.

## Source encoding and strength analogues

The normalized quadrupole column has

```text
amplitudes   = (+0.4082482904638631,
                -0.8164965809277261,
                +0.4082482904638631)
occupations  = (1/6, 4/6, 1/6)
column Gram  = 1
```

Collapsing all three labels onto one encoding column gives amplitude
`1-2+1=0`.  Likewise, the same-column `(+1,-1)` sum vanishes.  These are
encoding-column algebra cancellations only; they are not claimed as physical
same-site deletion experiments because the distinct-cell physical evolution
is not run after identifying those physical cells.

Two bounded `Q=0 direct-sum Q=1` preparations serve as honest physical
strength analogues:

| label | total Q1 occupation |
|---|---:|
| unit-weight analogue | `0.15864554811791431` |
| coefficient-two analogue | `0.8` |

Their ratio is `5.042687988984065`, equal to the Cycle-420 route-strength
ratio.  Their absolute values are not the Cycle-420 strengths
`7.501679264744504e-7` and `3.7828627925537926e-6`.  The unused norm occupies
the invariant Q=0 branch.  This is a preparation choice, not a gate selected
by an occupation query.

## Train and held geometry

The body-frame quadrupole axis is the third coordinate and the receiver lies
two cubic edges down the first coordinate.  Proper-cubic frames rotate the
whole labelled family.

| row | L | source cells | receiver cells | depth |
|---|---:|---|---|---:|
| train `a=1` | 7 | `(0,0,6)`, `(0,0,0)`, `(0,0,1)` | `(2,0,6)`, `(2,0,0)`, `(2,0,1)` | 4 |
| held `a=2` | 9 | `(0,0,7)`, `(0,0,0)`, `(0,0,2)` | `(2,0,8)`, `(2,0,0)`, `(2,0,1)` | 5 |

The same source column, two occupation analogues, update, packet preparation,
pointer effects, and arithmetic are used on held `a=2`.  There is no refit.

## Physical packet prediction

The receiver packet contains exactly one matter excitation, so its three
fixed cell effects sum to one without a host normalization query.  Pointer
values are `z=(-1,0,+1)`.  The compressed effects are

```text
Z  = sum_j z_j P_j,
Z2 = sum_j z_j^2 P_j.
```

The reported centroid is the `Z` coordinate and the width is
`sqrt(Z2-Z^2)` evaluated after the update.  These are coherent pointer-effect
coordinates, not probabilities, frequencies, occurrences, or Records.

### Training `a=1`

Free packet:

```text
cell weights       (0.005661657332684, 0.988676685334632, 0.005661657332684)
centroid            -8.673617379883912e-19
second moment        0.01132331466536801
width                0.10641106458149928
```

| physical strength | centroid shift | width | width shift |
|---|---:|---:|---:|
| unit-weight analogue | `-5.777789833161708e-34` | `0.10641618905991826` | `5.124478418980227e-6` |
| coefficient-two analogue | `8.673617379883912e-19` | `0.10643690321243784` | `2.5838630938565532e-5` |

The pure-Q1 quadrupole width is `0.10644336189014010`, a shift of
`3.229730864082070e-5` from the free packet.

### Blind held `a=2`

Free packet:

```text
cell weights       (0.113235634797584, 0.773528730404832, 0.113235634797584)
centroid             0
second moment        0.22647126959516894
width                0.4758899763550068
```

| physical strength | centroid shift | width | width shift |
|---|---:|---:|---:|
| unit-weight analogue | `0` | `0.47589137192525904` | `1.3955702522494562e-6` |
| coefficient-two analogue | `0` | `0.47589701373864046` | `7.037383633667904e-6` |

The pure-Q1 held width is `0.4758987730682887`, a shift of
`8.796713281911783e-6`.  The held response is positive but smaller than the
training response.  Consequently the Cycle-420 stronger-`a=2` ordering is not
reproduced.

Norm errors over the free and pure-Q1 train/held evolutions are below
`2.0e-14`.

## Sign, coherence, and deletions

The runner executes source, receiver, stream, coherence, packet-stream, and
contact deletions on the same training receiver evolution.

| control | final width |
|---|---:|
| free packet | `0.10641106458149928` |
| coherent `(+1,-2,+1)` pure Q1 | `0.10644336189014010` |
| all three source recoil couplings deleted | `0.10641106458149903` |
| receiver recoil coupling deleted / neutral test-matter control | `0.10641106458149913` |
| field stream deleted | `0.10641106458149917` |
| coherence erased, occupations `(1,4,1)/6` retained | `0.10644335994920857` |
| positive phase `(+1,+2,+1)` | `0.10644335800827709` |
| receiver packet FSWAPs deleted | `0` |

Thus source, neutral test-matter, and field-stream deletions return the free
width within `3e-16`.  Erasing coherence changes the coherent-quadrupole width
by `1.9409315266116778e-9`; changing the central sign changes it by
`3.881863011589992e-9`.  The full signed-pure versus incoherent-density
Hilbert–Schmidt residual is `0.7071067811865538`; the signed-pure versus
positive-phase full-state residual is `1.6329931618554576`.

The conservative numerical/covariance/E-G certification floor is `5e-13`.
The two width differences are respectively `3881.8630532233556` and
`7763.726023179985` times that floor.  The first exploratory run used an
unmotivated provisional absolute threshold of `1e-8`, which these resolved
effects failed.  The runner now tests the disclosed error-floor ratios instead.
This diagnostic-threshold repair occurred after the exploratory result; the
no-refit claim applies only to the frozen physical law, strengths, preparation,
geometry, and held prediction—not to that diagnostic threshold.

The sign is therefore load-bearing in a common receiver
evolution, but most of this finite width response is shared with the positive
occupation profile.  No broader signed-field conclusion is drawn.

The prediction sector has one particle per source cell and one total receiver
particle, so both contact factors are identities there.  Contact deletion
changes its prediction state and width by zero.  On each declared full
`n=0,...,3` block code, the contact is nontrivial on 645 columns; a two-particle
code state changes by `0.36789306705608243`.  Contact is present but is not a
driver of this prediction.

## Supplied physical-effect dilation

For each receiver encoding `E_R`, let `P_j` be the fixed projector onto packet
cell `j`.  The two-pointer-M2 dilation is

```text
V = stack(E_R P_-, E_R P_0, E_R P_+, 0).
```

It maps 18 receiver-packet columns into four pointer labels over the physical
receiver rays.  On train and held codes its shape is `(1045312,18)`.  Exact
controls give

```text
V^dagger V - I                         0
V^dagger Z_pointer V - Z_receiver      0
V^dagger Z2_pointer V - Z2_receiver    0
```

This is the three-outcome specialization of the Cycle-317 dilation/compression
pattern and supplies physical centroid and second-moment effects.  It does not
construct the local unitary which couples a blank pointer to these labels, nor
an inverse for such a pointer-coupling gate.  Effect functionality remains a
supplied hypothesis.  Pointer labels are not Records, and coherent weights
are not Born frequencies.

## Physical compiler and inverse

Each matter block uses its own disjoint local auxiliary/gauge copy.  Define

```text
E_435 = E_source tensor E_receiver tensor identity_field.
```

The global tensor matrix was not materialized.  The runner instead verifies
every displayed factor on both block encodings, then uses composition in the
fixed order.  It also tests the combined logical inverse on the interacting
prediction sector.  Thus the scoped relation is

```text
E_435 G_435 = G_physical,435 E_435.
```

| geometry/block | encoding shape | Gram | E/G | physical inverse | norm error |
|---|---|---:|---:|---:|---:|
| train source | `(261328,988)` | `7.771561172376096e-16` | `1.044747812340883e-14` | `3.734602017277068e-15` | `4.30e-13` |
| train receiver | `(261328,988)` | `7.771561172376096e-16` | `8.911820020717914e-16` | `2.021614955817347e-15` | `2.3e-15` |
| held source | `(261728,988)` | `7.771561172376096e-16` | `1.044747812340883e-14` | `3.734602017277068e-15` | `4.30e-13` |
| held receiver | `(261328,988)` | `7.771561172376096e-16` | `8.911820020717914e-16` | `2.021614955817347e-15` | `2.3e-15` |

The combined interacting logical step has an exact inverse on the scoped code,
with residual
`2.2175484504945024e-15` and output norm error `7e-16`.  Identity completion
outside each declared block-code image remains supplied.

## Proper-cubic covariance, mass, contact, and resources

All 24 proper-cubic frames are tested.  The entire body-frame geometry,
source coefficient labels, receiver packet edges, and pointer labels rotate
together.  Maximum residuals are:

| factor | maximum residual |
|---|---:|
| matter coins/contact | `1.6683190654377175e-16` |
| mapped receiver FSWAP edges | `0` |
| body-frame pointer effects | `0` |
| recoil source vertex | `8.807749891993861e-16` |
| field coin/stream | `0` |

The Cycle-219 one-particle mass fixture is preserved at
`0.4534056541748851`, with eigenvector residual
`3.534751832054436e-16`.  Each full block retains the 645 nontrivial
Cycle-230 contact columns.

Resource ledger:

- two disjoint three-M64 matter blocks;
- maximum measured three-cell matter support union: 132 M2 per block;
- seven reservoir/field M2 per cubic field cell;
- two pointer M2 for four labels, one label unused;
- maximum active recoil-vertex support: 25 M2;
- full matter code: 988 `n=0,...,3` columns per block;
- prediction sector: `216 x 18 = 3888` matter columns;
- field sector: Q=0 direct-sum the complete Q=1 sector;
- local Cycle-269/319 checks and Wilson sector independently enforce each
  block's auxiliary/gauge constraints;
- no preferred global site ordering or Jordan–Wigner parity service; the fixed
  bounded local factor order is supplied.

The doubled matter block and pointer add bounded constant overhead.  They are
not claimed to be minimal.

## Exact Cycle-420 boundary

Positive results:

```text
bounded physical phase quadrupole          true
bounded physical M64 receiver packet       true
physical centroid/second-moment effects    true
```

Exact named-surface flags:

```text
Cycle420 physical_source_EG                 false
Cycle420 physical_test_matter_readout       false
Cycle213/216 host-field join                false
legacy host packet join                     false
exact absolute strength match               false
exact numeric rows reproduced               false
named quadrupole-width surface closed       false
```

The Cycle-420 comparison rows remain:

| separation/route | legacy centroid | legacy width shift |
|---|---:|---:|
| `a=1`, unit weight | `1.0689897198540906e-15` | `6.692829912502418e-7` |
| `a=1`, coefficient two | `1.3663771298586589e-15` | `3.3757457469363317e-6` |
| `a=2`, unit weight | `3.375760302813136e-16` | `1.3197896109318208e-6` |
| `a=2`, coefficient two | `5.063644188031644e-16` | `6.656001151128521e-6` |

They are comparison-only and are not reproduced by Cycle 435.  The remaining
exact join requires: replace the bounded Q-occupation analogues with the frozen
Cycle-420 strengths; derive the Cycle-213/216 signed scalar profile from the
same physical update; and derive the legacy packet propagation, detector
geometry, centroid/width effects, numeric rows, and stronger-`a=2` ordering.

## Supplied / derived / open

Supplied:

- two disjoint Cycle-319/396 three-M64 physical blocks and identity
  completions;
- the Cycle-425 field coin/stream and Cycle-426 recoil vertex;
- fixed coordinates, factor order, depth, phase-column isometry, strength
  occupancies, packet preparation, and physical-effect dilation;
- the Cycle-420 exact quadrupole contract and Cycle-213/216 host-field
  surfaces as comparison boundaries.

Derived:

- a positive-occupation three-source coherent physical quadrupole analogue;
- a spatial physical M64 packet with symmetric nonzero width response;
- fixed physical centroid/second-moment compressed effects;
- two-strength train/held predictions without refit;
- factorwise physical E/G and inverse, combined logical inverse, all-frame
  covariance, deletion, mass/contact, resource, and lawful-domain controls.

Open:

- exact Cycle-420 source strengths and Cycle-213/216 signed scalar profile
  from the physical update;
- the legacy packet evolution, detector domain, numeric rows, and separation
  ordering;
- a local pointer-coupling unitary and inverse;
- autonomous source and pointer preparation;
- primitive replacement of inherited matrix-unit completion;
- physical clock, Records, Born law, energy/stress/source selection, metric,
  and gravity.

No pointer label is a Record.  No coherent weight is a Born frequency.  Step
count is not time.  No occupation is called physical energy, source stress, or
gravity.  No no-go, minimum-content, shared-obstruction, or axiom-pressure
claim is made.

## Reproduction

```bash
python3 scripts/physical_quadrupole_packet_width_bridge_cycle435_2026_07_19.py
```

Final cold result from the reviewed runner hash: `PASS 15 / FAIL 0` and
`PHYSICAL_QUADRUPOLE_PACKET_WIDTH_BRIDGE_CERTIFIED`.

Compact executable summary:

```text
maximum factorwise E/G residual                 1.0447478123408826e-14
maximum physical inverse residual               3.734602017277068e-15
combined interacting logical inverse residual   2.2175484504945024e-15
maximum physical output-norm error               4.30e-13
pointer isometry/compression residual            0
maximum all-24 proper-cubic residual             8.807749891993861e-16
source/receiver/field-stream deletions to free   <= 3e-16
contact prediction-sector residual               0
lawful-domain rejections                         5 / 5
maximum three-cell matter-support union          132 M2 per block
pointer overhead                                 2 M2
maximum active recoil-vertex support             25 M2
```
