# Route 3 staggered CAR compiler probe — Cycle 233

**Date:** 2026-07-17

**Type:** constructive compiler attempt with exact finite discriminators

**Status:** partial-attempt-with-named-untested-routes

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** draft PR #5389 parking branch only

Companion runner:

```text
scripts/ROUTE3_STAGGERED_CAR_COMPILER_CYCLE233_2026_07_17.py
```

This note and runner alter no axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit surface.

## Result up front

Route 3 produces a useful but incomplete compiler component: a four-phase
autonomous update-law register can schedule the Cycle-230 exterior coin,
two-layer stream, and contact without host-side phase changes. The update-law
phases are

```text
q=0: onsite Gamma(C)
q=1: onsite opposite-direction FSWAP layer A
q=2: all three disjoint axis edge-FSWAP layers B
q=3: onsite contact W_g
q -> q+1 mod 4.
```

This is the **four-phase autonomous schedule** tested below.

Neighbor equality of the two-bit `q` registers is a local synchronization
constraint and is exactly preserved. At the end of four supplied substeps the
register returns to `q=0`. All three axis edge layers can fire together because
they use distinct direction modes. This removes a preferred `x,y,z` order and
gives a proper-cubic schedule at every phase. The register is only supplied
update-law control. It is not physical time, a clock, a metric, a rate, a
winding carrier, or progress on the emergent-dynamics single-generator gate.

With six occupation qubits in each ideal coarse block, the onsite exterior coin
and the contact are exact `64 x 64` bounded gates. The contact is identity for
`N<=1`; the scheduled stream is also exact in the one-particle sector. The
Cycle-219 rest, curvature, and forced-inertia fixture is therefore preserved.
The qubit contact generator reproduces the Cycle-230 local modular-seam block,
including its two nonzero reduced singular values near `0.49577141` and
`0.45566605` and the raw `1/L^3` normalization.

In short, the one-particle mass fixture and the Cycle-230 seam block survive as
isolated controls even though the complete many-particle update does not.

The decisive intertwining contract nevertheless fails for this plain
occupation-qubit schedule. For a fixed occupation-basis order `O`, a geometric
two-qubit FSWAP on a pair that is not adjacent in `O` does not equal the
exterior lift of that mode transposition. On periodic axial reductions of
sizes `L=3,4,5`, exhaustive searches over every cell-contiguous local mode order
leave respectively `4,6,8` wrong two-particle signs; all `6!` unrestricted
orders at `L=3` still leave four. Any nonzero sign mismatch gives

```text
|| E_O Gamma(S) - S_FSWAP E_O ||_op = 2.
```

Unitary multiplication by the same coin and contact cannot reduce this norm.
Thus the proposed macrostep does not satisfy

```text
E G_coarse = G_physical E
```

on the declared many-particle code space.

A second exact defect appears in the frame audit. The coarse cell transforms
by the exterior lift `Gamma(P_R)` of the six-direction permutation. Physical
port qubits transform by ordinary tensor-factor permutation `T(P_R)`. The
Cycle-219 exterior coin commutes with `Gamma(P_R)` in all 24 frames but fails
to commute with `T(P_R)` in 22 frames, with maximum Frobenius residual about
`9.2376`. The two 64-dimensional group actions have different characters for
some rotations, so changing a fixed local basis or local mode order cannot
identify the full representations. An enlarged code subspace or local
auxiliary transformation remains a live escape.

These are two defects of the tested schedule-only occupation code. They are
not a route-independent compiler impossibility. In particular, an open axial
chain has exact orderings, a bounded plaquette phase repairs the four-site
exchange witness, and the primary literature contains higher-dimensional
auxiliary/gauge and distinguishable-walker escapes. There is no axiom pressure
from this result.

## Frozen contract and code space

Let `j=(x,a)` label the six Cycle-230 direction modes at coarse cell `x`. For a
finite declared order `O=(j_0,...,j_(M-1))`, the plain route maps the ordered
Fock occupation basis to physical data qubits:

```text
E_O |n_0,...,n_(M-1)>_Fock
    = |n_0> tensor ... tensor |n_(M-1)> tensor |q=0>_uniform.
```

The ideal code space contains all data occupations and the locally lawful
uniform update-phase sector. Two schedule qubits are supplied per coarse cell.
The local lawful-domain constraints are:

```text
q_x in {0,1,2,3},
q_x = q_y for every neighboring pair x,y.
```

The homogeneous increment preserves those constraints and has zero ideal
leakage. `E_O` is an exact isometry for every fixed `O`. The question is whether
the scheduled ordinary tensor-product unitary intertwines the coarse exterior
unitary and whether `E_O` respects all geometric frames.

At the ideal block-graph level the supplied macrostep is

```text
G_tilde_O(g) = W_g F_B F_A Gamma_O(C),
```

where `F_A` and `F_B` are products of ordinary two-qubit FSWAP matrices on the
named geometric pairs. This already inventories a block tiling, six port
roles, a phase origin `q=0`, the four-phase order, FSWAP as a gate primitive,
the full exterior coin, and the contact strength. An explicit nearest-neighbor
embedding and gate decomposition into the physical `Z^3` sites was not
completed because the ideal block-graph candidate fails the exact
intertwining and frame tests first. That unfinished embedding is not counted
as an obstruction.

## Exact sign comparison

For a mode permutation `P`, the exterior action on occupation set `I` is

```text
Gamma(P)|I>_O = (-1)^inv_O(P;I) |P I>_O,
```

where `inv_O(P;I)` is the inversion parity of the occupied destination list.
A circuit of geometric two-qubit FSWAPs `e=(u,v)` instead accumulates

```text
(-1)^sum_e n_u(e)n_v(e),
```

with the occupations evaluated when each gate fires. The output occupation
permutation agrees exactly, but the two quadratic sign functions need not.

For the axial Cycle-230 stream, `A` swaps `+` and `-` at every cell and `B`
swaps `(x,-)` with `(x+1,+)`. The exhaustive periodic results are:

| size | searched order family | two-particle dimension | best wrong signs | exact orders |
|---:|---|---:|---:|---:|
| 3 | every cell order and both local mode orders per cell | 15 | 4 | 0 |
| 4 | every cell order and both local mode orders per cell | 28 | 6 | 0 |
| 5 | every cell order and both local mode orders per cell | 45 | 8 | 0 |
| 3 | all `6!` unrestricted mode orders | 15 | 4 | 0 |

The matched open-chain control has two exact unrestricted orders at `L=3`.
This localizes the tested defect to cycles/seams and incompatible
multidirectional order requirements; it blocks a universal schedule no-go.

For one consistent periodic order, the target/local sign difference is exactly
a product of CZ phases over the wrong two-particle pairs. Exhausting every
occupation at `L=3,4` verifies that adding the entire CZ inventory reduces the
monomial-unitary residual from `2` to `0`. The inventory is not bounded in the
held-out-size sequence:

| `L` | correction CZ pairs | maximum periodic graph range |
|---:|---:|---:|
| 3 | 8 | 1 |
| 5 | 16 | 2 |
| 7 | 24 | 3 |
| 9 | 32 | 4 |

Thus this exact correction is a global parity seam in the tested order family,
not a constant-radius repair.

## Changing the JW order between axis substeps

Changing order labels is not free. If `O_x` orders cells with `x` fastest and
`O_y` orders them with `y` fastest, their occupation bases differ by

```text
D_xy(n) = (-1)^sum_{(u,v) in Inv(O_x,O_y)} n_u n_v.
```

The runner verifies this identity directly on sampled occupations. An exact
implementation by the corresponding pair phases contains the following
long-range terms:

| `L` | inversion CZ pairs | maximum Manhattan range | NN light-cone depth lower bound |
|---:|---:|---:|---:|
| 2 | 2 | 2 | 1 |
| 3 | 27 | 4 | 2 |
| 4 | 144 | 6 | 3 |
| 5 | 500 | 8 | 4 |
| 7 | 3087 | 12 | 6 |

The last column is the minimum depth for information from the two endpoints of
the most distant displayed phase to meet under nearest-neighbor gates without
pre-shared nonlocal resources. It grows with `L`. A schedule that silently
changes from an axis-friendly `O_x` to `O_y` therefore replaces the parity
string with a non-bounded rephasing/routing step. A local parity/gauge field
could change that conclusion, but that is Route 2 structure rather than a
schedule-only repair.

## Schedule and covariance audit

### Preferred-axis micro-schedule

The first attempted register used

```text
C -> A -> B_x -> B_y -> B_z -> W_g.
```

The `B` factors commute and their macroproduct is invariant under proper-cubic
frames. The phase transition itself does not commute with rotations that
permute axes: a rotation maps, for example, the `B_x` register value to `B_y`
without mapping the fixed successor relation to itself. Host-side switching
has the same preferred-phase defect and is forbidden by the contract.
The explicit six-phase register fails this microstep commutator in 20 of the
24 frames, with maximum Frobenius residual `2.82842712`.

### Four-phase repair of the schedule only

Because the six direction modes split into three disjoint axis pairs, all
`B_mu` edge gates can fire in one phase. The repaired supplied schedule is

```text
C -> A -> B_all -> W_g.
```

The phase value is a proper-cubic scalar. The `A` and `B_all` pair sets map to
themselves under all 24 frames, and the local contact is invariant. The runner
checks exact pair-set covariance in all frames and direct action covariance on
held-out two-particle samples. It also checks that all `3!` sequential axis
orders have the identical stream macroproduct. Therefore preferred axis order
is not the cause of the remaining sign residual.

The plain port-qubit exterior coin remains the frame defect. For a direction
permutation `P_R`, the two cell representations have characters

```text
chi_exterior(R) = det(I + P_R),
chi_tensor(R)   = 2^(number of cycles of P_R).
```

They differ on some proper-cubic rotations. Consequently no fixed `64 x 64`
local change of basis can turn the complete ordinary six-port permutation
representation into the complete exterior one. A larger physical block may
contain the desired representation as a code subspace; this route did not
construct or exclude that possibility.

## Worldline exchange discriminator

On a four-site square, apply disjoint local swaps on `(0,1),(2,3)` and then on
`(1,2),(3,0)`. Two particles initially at opposite corners `0,2` follow
separated worldlines and return to the same occupation while exchanging their
labels. The exterior target gives amplitude `-1`; the local FSWAP circuit gives
`+1`, hence residual `2`. No FSWAP ever sees two occupied endpoints.

The runner also derives and applies the complete diagonal correction on this
four-site system. It repairs every occupation exactly. This is important
negative discipline: a local plaquette exchange phase can fix a bounded
witness. What remains unbuilt is a translation- and proper-cubic-covariant
family of such phases that is mutually consistent on every three-dimensional
loop and has bounded overhead on held-out sizes. Supplying local flux/parity
variables is a live constructive route, not evidence against the substrate.

## Inherited physics controls

### One-particle mass

Every FSWAP equals ordinary SWAP in the zero- and one-particle sectors. The
full `L=3` stream therefore agrees with the Cycle-230 one-particle permutation
on all 162 one-particle basis states. The runner reruns the Cycle-219 rest,
curvature, and forced-response checks at `beta=-0.3`; all remain within their
declared tolerances. In the same full cube, `4140` of the `13041`
two-particle basis states have the wrong sign under the plain schedule.

### Contact and seam

On six occupation qubits,

```text
W_g = exp[i g N(N-1)/2]
```

is an exact bounded diagonal gate. It is identity for `N<=1` and acts as
`exp(i g)` on the local two-particle sector. Direct contraction of that
15-dimensional sector reproduces the Cycle-230 reduced `L=3` seam generator
block to machine precision, including the universal raw `1/27` factor.
Setting `g=0` deletes the contact exactly.

This is reproduction of the local generator block, not reproduction of the
full free-plus-contact law. Since the stream intertwining residual is `2`, the
seam states are not transported by the required coarse many-body update under
this route.

### Leakage, deletion, held-out size, and lawful domain

- The ideal four-value update register is unitary and preserves every
  neighbor-equality synchronization constraint exactly.
- The ideal six-qubit coin/contact block is unitary; the contact has exact
  `g=0` deletion.
- Axial sign residuals persist at `L=3,4,5`; correction range grows through the
  held-out `L=7,9` cases.
- Axis-order rephasing depth grows through held-out `L=7`.
- The ideal data code itself is the entire occupation-qubit Hilbert space, so
  the detected mismatch is not leakage; it is wrong action inside the code.
- A physical nearest-neighbor block embedding and decomposition were not
  completed and receive no pass credit.

## Supplied-structure inventory

The attempted construction supplies all of the following:

1. a coarse-cell blocking/port layout with six named direction occupations;
2. a finite occupation-basis order `O` and its fermionic sign convention;
3. two phase-register qubits per coarse cell, the distinguished boundary value
   `q=0`, neighbor synchronization constraints, and the four-phase successor;
4. the full `64 x 64` exterior coin `Gamma(C(beta=-0.3))`;
5. two-qubit FSWAP as a primitive bounded gate and the `A,B` pair lists;
6. the supplied contact `W_g` with `g=0.37` for finite gate controls;
7. periodic finite-torus boundary conditions and an induced parity seam;
8. ordinary physical permutation of port qubits under geometric frames;
9. the Cycle-230 principal-phase sea and seam preparation for the inherited
   generator-block comparison; and
10. ideal bounded-block gates without an executed nearest-neighbor physical
    layout/decomposition.

Items 2, 3, 7, and 8 are load-bearing schedule/representation choices. None
is selected by locality alone. The phase-register substep count supplies no
physical time coordinate or rate.

## Route-3 disposition

| Candidate | Constructed gain | Exact residual | Disposition |
|---|---|---|---|
| fixed cell-local mode order | bounded onsite coin/contact; exact one-particle stream | periodic two-particle signs; norm `2` | rejected for the declared periodic code |
| arbitrary static order | all `6!` tested at `L=3` | at least four wrong pair signs | rejected for that finite fixture |
| edge-colored axis schedule | autonomous four-phase schedule; no preferred axis; stream pair-set covariance | sign residual unchanged | schedule layer retained, compiler claim rejected |
| changing JW order by phase | exact rephasing formula | range and NN depth grow with `L` | violates bounded-support contract in tested family |
| separated worldline routing | exact one-particle paths | exchange amplitude `+1` instead of `-1` | needs extra plaquette/parity content |
| local plaquette correction | exactly repairs four-site witness | global 3-D consistency unbuilt | live next construction, overlaps Route 2 |
| plain six-port frame action | contact and stream covariance | exterior coin fails 22/24 ordinary frames | enlarged/signed auxiliary code remains live |

The strongest Route-3 output is therefore the proper-cubic, autonomous
four-phase schedule plus exact local physics preservation, paired with two
executable reasons it is not yet a CAR compiler.

## TOE dependency effect

Only `C_local` changes resolution. It remains open, but now contains two exact
Route-3 targets: a bounded local realization of the stream sign cocycle and a
physical-frame code carrying the exterior cell representation. Dynamic JW
reordering and preferred-axis phase control are removed as free fixes.

The other five-wall entries are unchanged:

| Wall | Route-3 effect |
|---|---|
| `C_ref` | none; phase origin, sea, and preparation remain supplied |
| `C_num` | none; number reference/superselection remains open |
| `C_wrap` | none; the update phase register stores no quasienergy winding and is not a physical clock |
| `C_int` | none; the selected interaction and rate/protection result remain open |
| `C_local` | partial narrowing only; schedule constructed, exact intertwiner not constructed |
| `C_source` | none; physical conserved energy/stress/source remains open |

TOE maturity scores remain `2/5` operational quantum/records, `1/5` time,
`3/5` inertia/matter, `2/5` gravity/source, and `1/5` Born/probability. The
schedule register is implementation control, so it does not raise the time
score.

## Primary-source boundary

This finite sign and frame census is repository-specific. It does not claim a
new general fermionization theorem.

- Farrelly and Short construct local decompositions of causal fermionic
  evolution and qubit-QCA simulations, with higher-dimensional auxiliary
  structure: T. C. Farrelly and A. J. Short, “Causal Fermions in Discrete
  Space-Time,” *Physical Review A* **89**, 012302 (2014),
  <https://doi.org/10.1103/PhysRevA.89.012302>, arXiv:1303.4652.
- Mlodinow and Brun prove a scoped obstruction for their direct
  occupation/local-creator construction in dimensions above one and explicitly
  discuss escapes; that theorem is not enlarged into a no-go for this
  tournament: L. Mlodinow and T. A. Brun, *Physical Review A* **102**, 042211
  (2020), <https://doi.org/10.1103/PhysRevA.102.042211>, arXiv:2006.08927.
- The same authors construct a distinct three-dimensional route using
  distinguishable-walker registers and a global antisymmetric subspace:
  L. Mlodinow and T. A. Brun, *Physical Review A* **103**, 052203 (2021),
  <https://doi.org/10.1103/PhysRevA.103.052203>, arXiv:2011.05597.
- Eon, Di Molfetta, Magnifico, and Arrighi construct a `3+1`-dimensional
  fermion/gauge QCA in which local gauge degrees of freedom supply structure
  absent from this schedule-only attempt: *Quantum* **7**, 1179 (2023),
  <https://doi.org/10.22331/q-2023-11-08-1179>, arXiv:2205.03148.

These are primary research sources. They bound the claim and keep auxiliary,
gauge, and antisymmetric-register routes live; they are not used as substitutes
for the executable residuals above.

## No-go discipline gate

**Status:** N1-N8 **PASS** for the narrow statement that the tested plain
occupation-qubit schedule/order family fails the exact periodic/cubic compiler
contract. N1-N8 **FAIL** for a general `M_64 -> M_2` compiler impossibility or
minimum-content claim. The broad claim is not shipped.

### N1 — alternative-route enumeration

Every marker below is backed by the named control in the
[companion runner](../../../../scripts/ROUTE3_STAGGERED_CAR_COMPILER_CYCLE233_2026_07_17.py),
which is the current-cycle executable evidence rather than an authority claim.

| Attack or escape | Marker | Runner control | Outcome |
|---|---|---|---|
| change the local order in every cell | **ATTEMPTED** | `axial_order_and_boundary_controls` | exhaustive `L=3,4,5` searches retain `4,6,8` wrong pair signs |
| abandon cell contiguity and try any static order | **ATTEMPTED** | `axial_order_and_boundary_controls` | all `6!` orders at periodic `L=3` retain at least four wrong signs |
| edge-color and permute `B_x,B_y,B_z` | **ATTEMPTED** | `schedule_and_covariance_controls` | all `3!` orders give the same macro stream and the same residual |
| change JW order between axis phases | **ATTEMPTED** | `axis_order_change_controls` | exact order-change phase contains terms of range `2(L-1)` and NN light-cone depth at least `L-1` on the tested open cubes |
| make the phase control autonomous | **ATTEMPTED** | `schedule_and_covariance_controls` | local synchronization and zero leakage pass; the data sign is unchanged |
| remove preferred-axis phase order | **ATTEMPTED** | `schedule_and_covariance_controls` | `B_all` makes the schedule proper-cubic, but it does not repair the sign or cell-frame representation |
| route separated worldlines and add local plaquette phases | **ATTEMPTED** | `worldline_exchange_controls` | bare routing has the wrong exchange sign; a bounded plaquette correction repairs the four-site witness, so a gauge/flux construction remains live |
| use open boundaries | **ATTEMPTED** | `axial_order_and_boundary_controls` | exact axial orders exist; this defeats any universal schedule no-go but does not meet the declared periodic held-out contract |

The local plaquette and open-chain successes force the negative conclusion to
remain route- and domain-specific.

### N2 — wall-independence audit

The tested defects collapse to two route residuals:

- `R_sign`: the ordinary local FSWAP schedule and exterior stream have
  different many-occupation sign cocycles for the declared periodic code;
- `R_frame`: the ordinary port-qubit and exterior six-mode frame actions are
  inequivalent on the complete plain 64-state cell.

| Pair | first closes second? | second closes first? | independent? | Reason |
|---|---:|---:|---:|---|
| `R_sign`, `R_frame` | no | no | yes | a parity/plaquette repair need not change the cell rotation representation; a larger covariant cell code need not fix stream signs |

The phase register is not a third wall: its ideal local code and autonomy are
constructed. The physical block embedding is unfinished implementation, not a
demonstrated obstruction. A single gauge/auxiliary construction may close both
residuals, but neither closure logically supplies the other.

### N3 — hidden-wall scan

The scan covered `we assume`, `by construction`, `as is standard`, `the
framework provides`, `bridge context`, `background`, `naturally`, `obviously`,
`standard QFT`, `registered`, and `canonical`, plus close variants.

| Hit | Classification | Disposition |
|---|---|---|
| “registry” in metadata and primitive audit | non-load-bearing governance statement | retained only to state that protected surfaces are untouched |
| “construction/construct” in route descriptions | ordinary verb, not an authority shortcut | each load-bearing step has an equation or executable control |
| no other scientific trigger hit | — | no hidden wall promoted |

The global occupation order, phase origin, boundary condition, port roles,
gate tables, interaction, and sea are all explicit in the supplied-structure
inventory.

### N4 — residual matching

| Witness | Witness residual | Route-3 residual | Match? | Use |
|---|---|---|---:|---|
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:109-130` | compile six-mode `M_64` CAR cell into bounded physical `M_2` sites without losing graded locality | schedule-only occupation code fails exact signs and frames | yes, partial attempt only |
| same file `:160-180` | intrinsic `S=BA` fermionic swaps and exterior coin | ordinary local FSWAP/port actions tested against those exact layers | yes |
| `FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md:172-188` | exterior lift was not a spatial onsite-qubit compiler | Route 3 attempts that interface and leaves it open | yes |
| `MINIMAL_AXIOMS_2026-06-29.md:35-61` | physical `Z^3`, `M_2`, NN admissibility, proper-cubic covariance | exact target contract | yes |
| Mlodinow-Brun 2020 | scoped direct-construction obstruction | general compiler impossibility | no | scope boundary only, not a witness for a broad no-go |

No external theorem is used to promote the finite census to a substrate claim.

### N5 — rhetoric and resolution audit

| Resolution | Tested result | Untested remainder |
|---|---|---|
| per local mode | exact occupation encoding and FSWAP matrix | other encodings of one fermion mode |
| per six-mode block | exact coin/contact and full frame-character comparison | larger block/code subspaces |
| one-particle | exact full `L=3` stream and inherited mass | interacting/dressed mass |
| two-particle | exhaustive axial order censuses; full-cube mismatch census | every possible auxiliary code |
| one plaquette | exchange sign failure and exact diagonal repair | consistent all-plaquette 3-D law |
| periodic axial lattice | `L=3,4,5` order failures; held-out correction range | open/infinite spin structures |
| 3-D proper-cubic frames | exact layer pair-set covariance and cell representation audit | covariant enlarged code |
| seam generator block | exact contact reproduction | full seam state under an intertwined free-plus-contact update |
| physical time/source/records/Born | not tested | all corresponding TOE lanes |

“Does not satisfy the intertwining” means this declared `E_O` and scheduled
`G_tilde_O` fail on exhibited two-particle states. It does not mean no bounded
encoding exists.

### N6 — partial-closure paths

The approved primitive registry and its source notes were checked. Scale
reference supplies units, kinetic isotropy supplies only `c_t=c_s`, and the
realized-state primitive supplies only a pointwise evaluation slot. None is
used to choose the update schedule, parity convention, frame code, interaction,
or sea. They remain approved premises rather than compiler walls.

Live partial-closure paths are:

| Path | Current status | Possible closure |
|---|---|---|
| local edge/plaquette parity or gauge variables with local Gauss constraints | Route 2 live | `R_sign`, possibly `R_frame` |
| enlarged cubic block containing the exterior frame representation as a code subspace | unbuilt | `R_frame` |
| a consistent bounded plaquette-phase schedule | four-site witness only | part of `R_sign` without a global parity service |
| distinguishable walkers plus an antisymmetric code | primary-source precedent, uninstantiated here | alternative physical encoding |
| open/infinite spin-structure treatment with explicit boundary audit | axial control only | periodic seam, not automatically 3-D loops |

These are construction routes, not proposed axiom edits.

### N7 — steelman

> The negative is premature outside the exact plain code. The runner itself
> constructs a bounded plaquette correction and an exact open-chain order, so
> the sign defect is not intrinsically nonlocal on every domain. A local `Z_2`
> edge/plaquette field can store precisely the loop information that the
> schedule register lacks, and a larger cubic block can carry the exterior
> frame representation on a constrained subspace even though the full six-port
> tensor representation has the wrong character. Farrelly-Short and Eon et al.
> provide primary precedents for auxiliary/gauge locality, while Mlodinow-Brun
> provide an antisymmetric-register escape. Until those encodings are applied
> to this exact coin, contact, and seam fixture, Route 3 cannot support a
> substrate obstruction.

This steelman is convincing. The broad no-go is demoted; the next target is the
local gauge/auxiliary route plus a covariant code-space construction.

### N8 — cross-cycle echo

| Prior echo | Prior status | Route-3 effect | Retirement mechanism applicable? |
|---|---|---|---|
| Cycle 229 spatial onsite-qubit compiler | open | schedule and exact finite discriminators added | yes, constructive import-and-test; not retired |
| Cycle 230 `C_local` coarse CAR-to-physical-site bridge | open | plain occupation schedule narrowed; contact and mass coexist | yes, Route 2 remains the priority |
| earlier one-dimensional order-based fermionization expectations | domain-specific | open-chain control passes while periodic seam fails | boundary/spin structure matters |
| Cycle 230 warning that auxiliary/gauge encodings are live | open | plaquette repair and frame mismatch sharpen their target | directly applicable |
| past convention-retirement patterns | not a match | changing the name of the order or phase does not implement the missing signs | no terminology-only retirement |

No similar wall is retired by relabeling. The applicable retirement mechanism
is an explicit local encoding followed by the same intertwining, covariance,
deletion, leakage, held-out-size, and seam tests.

## Final boundary

Route 3 does not compile the Cycle-230 coarse CAR update to physical sites. It
does construct the strongest schedule-only candidate found here, preserve the
one-particle and contact fixtures, remove host-side and preferred-axis control,
and isolate two exact residuals. Those residuals remain `C_local` work. They do
not select physical time, energy, source, records, probabilities, or an axiom.

There is no route-independent obstruction and no axiom pressure.

## Verification

```text
python3 scripts/ROUTE3_STAGGERED_CAR_COMPILER_CYCLE233_2026_07_17.py
```

Verified result: `20 PASS / 0 FAIL`; `py_compile` and `git diff --check` pass.
