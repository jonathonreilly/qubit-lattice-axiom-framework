# Physical recurrent shared-volume compiler — Cycle 545

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_recurrent_shared_volume_compiler_cycle545_2026_07_21.py`

## Result

Cycle 545 gives the first constructive recurrence certificate for two
differently addressed, overlapping updates on one shared physical patch.  It
uses one fixed four-cell degree-three star and one **single global S4**
compute/select/uncompute isometry.  It does not place independent order
registers on the two overlapping three-cell updates.

The Cycle-539 star code is widened from all 301 columns through total particle
number `n<=2` to all **2,325** four-cell columns through `n<=3`:

```text
1 + 24 + 276 + 2,024 = 2,325.
```

Two corner updates are then applied on that same volume:

```text
A_xy acts on cells (leaf-x, center, leaf-y), using seams (x,y),
B_xz acts on cells (leaf-x, center, leaf-z), using seams (x,z).
```

They share leaf-x, the center, and the x seam.  Both lawful orders are
compiled and tested:

```text
A_then_B: U_B U_A,
B_then_A: U_A U_B.
```

The orders are not silently identified.  Their raw maximum matrix difference
is `0.751201387068515`, with 1,084,860 nonzero difference entries.  Both are
unitary, covariant, invertible, and recurrent.  On the declared code space,

```text
G_AB E_V = E_V U_B U_A,
G_BA E_V = E_V U_A U_B,
(G_AB)^k E_V = E_V (U_B U_A)^k,
(G_BA)^k E_V = E_V (U_A U_B)^k.
```

The compiler decodes once with `W_V^dagger`, executes both local updates on
the one persistent 24-M2 occupation register, and re-encodes once with `W_V`.
Thus the intermediate `W_V^dagger W_V` between separately conjugated patch
updates cancels exactly.  Shared cells, q M2, branch M2, the S4 register, and
the fixed reference occur once.

This is a fixed bounded shared volume, not a translation-equivariant periodic
volume compiler.  It is also not autonomous causal time.  **No schedule is
time.**

## Exact target contract

| item | Cycle-545 declaration |
|---|---|
| physical placement | one fixed Cycle-539 degree-three star |
| overlapping updates | two three-cell corners sharing two cells and one seam |
| logical domain | complete four-cell sectors `n=0,1,2,3` |
| sizes | periodic L5 train and held L6 |
| isometry | one global S4 compute/select/uncompute `W_V` |
| runtime | decoded q coin, two FSWAP seams, contact; then re-encode |
| order controls | both `A_then_B` and `B_then_A`, without equating them |
| recurrence | repeat counts 1–4 numerically plus arbitrary-k induction |
| primitive requirement | explicit one-/two-M2 gates and nearest-neighbour routes |
| covariance | all 24 proper-cubic frames and all 576 products |
| excluded closure | fixed-reference genesis, blank genesis, all-size tiling, carrier transduction |

The patch address, two update addresses, factor order, coupling, exact analog
angles, L5/L6 boundary, `n<=3` cutoff, and compile-time frame are explicit.

## One global code-space isometry

### Widened branch and order preparation

The four persistent cell occupation words drive the same exact local branch
preparations as Cycles 533 and 539.  Each of the four cells uses three branch
M2.  The shared five-M2 order register is prepared uniformly on the 24 S4
orders.  The preparation retains:

- 384 exact two-ray branch Givens;
- 128 controlled Gray-path `X` macros;
- 23 exact S4 order Givens; and
- zero forward or inverse preparation residual above numerical tolerance.

The new `n=3` sector introduces 32 logical columns with 48 branch products;
the other 2,293 columns have 16 products.  Direct enumeration at L5 and held
L6 gives:

| item | L5 | held L6 |
|---|---:|---:|
| logical columns | 2,325 | 2,325 |
| branch histogram | `2293 x 16; 32 x 48` | same |
| order-resolved decoder rows | 917,376 | 917,376 |
| native role M2 | 50 | 50 |
| equality controls | 79 | 79 |
| decoder collisions | 0 | 0 |
| normalized decoder digest | `43d162470685...` | identical |

The exact normalized digest is
`43d162470685b53ff04a78af4b540749109737fe9cd2147a2bf1d341a9c47402`.
Every column has unit norm.  Within each `(q,S4-order)` block, the native role
pattern is injective, so the 12 branch bits can be erased reversibly.  All 320
local role pairs retain zero pairing, port-constraint, and fixed-sector
commutator failures at both sizes.  The same table supplies the bounded
legality projector.  This proves an algebraic code-space isometry on the
declared fixed patch; it does not prepare the reference from product M2.

### Exact recurrence mechanism

Let

```text
E_V |q> = W_V |q>|Omega_fixed>|0_branch,order,work>.
```

`W_V` is a circuit, so its reverse dagger decodes every lawful encoded ray to
the same q register, fixed reference, and blank work state.  During the
decoded interval both overlapping updates act on the same q M2.  Reapplying
`W_V` rebuilds the unique global S4 code ray.  No pairwise tensor surrogate or
copy of the shared center is introduced.

For either sweep `S`, `G_S=W_V S W_V^dagger` preserves `im(E_V)`.  The
arbitrary-repeat identity follows by induction from `W_V^dagger W_V=I`.
The runner additionally tests deterministic normalized vectors in every
sector `n=0,1,2,3`, both orders, and repeats 1–4.  The maximum norm residual is
`4.440892098500626e-16`; the maximum reverse-roundtrip residual is below
`5e-15`.

Intermediate primitives may leave the encoded subspace.  The result is a
terminal code-space compiler: branch, order, conjunction work, q tag, and
route displacement all return exactly at the end of the sweep.

## Logical update and preserved fixtures

Each local update has the Cycle-525 form

```text
U_patch = D_patch S_second S_shared Gamma(C on the three addressed cells),
```

with the Cycle-219 `beta=-0.3` six-mode coin, two Cycle-230 fermionic seams,
and `g=0.37` onsite contact.  The spectator fourth cell is unchanged during
that local update.  The complete declared sector dimensions and maximum raw
unitarity residuals are:

| n | dimension | A residual | B residual |
|---:|---:|---:|---:|
| 0 | 1 | below `4e-15` | below `4e-15` |
| 1 | 24 | below `4e-15` | below `4e-15` |
| 2 | 276 | below `4e-15` | below `4e-15` |
| 3 | 2,024 | below `4e-15` | below `4e-15` |

For each update, the uniform one-particle state on its 18 active modes has

```text
compiled rest mass       0.4534056541748851,
Cycle-219 mass fixture   0.4534056541748851,
eigenvector residual     3.534751832054436e-16.
```

Each patch contact is nontrivial on 915 columns.  Each update uses two exact
fermionic seams, including their CAR sign.  The runner separately replays the
Cycle-532 full-Fock `Gamma(P)` target and the Cycle-219/Cycle-230 mass,
contact, and seam fixtures.

## Literal one-/two-M2 schedule

During the decoded interval, the 24 occupation-shadow M2 are physical qubits,
not host-side bits.  Cycle 523's exact QR coin uses one-M2 phases, arbitrary
two-M2 fermionic Givens cores, and its clean tag.  The 15 contact factors use
arbitrary two-M2 controlled-phase cores.  This is the arbitrary one-/two-M2
core convention already made explicit by the Cycle-533 compiler.

Every FSWAP core—including the tag-routing FSWAPs inside coin/contact and the
four intercell seam calls per two-update sweep—is replaced by Cycle 540's
verified **four pi/4** rotation identity:

```text
R_-(B_u) R_-(B_u) R_-(Ahat) R_+(B_u B_v Ahat) = -i FSWAP
```

in physical application order.  Each adjacent block is materialized as
`H,S,Sdg,Rz` one-M2 gates and CNOT two-M2 gates.  A complete sweep contains
304 four-rotation blocks.  Since `304 mod 4 = 0`, their raw `(-i)^304` product
is exactly `+1`; the complete sweep needs no residual global-phase
correction.

Remote two-M2 calls use Cycle 533's deterministic Manhattan routing pattern:
ordinary tensor-factor SWAPs move one wire next to the target, the core is
applied, and the route reverses.  Every ordinary SWAP is expanded to three
nearest-neighbour CNOTs.  Intermediate route data are restored without
requiring a zero-valued bus.

The runner materializes and hashes every decoded-runtime primitive:

| size/order | primitives | one-M2 | two-M2 | schedule SHA256 |
|---|---:|---:|---:|---|
| L5 `A_then_B` | 38,552 | 4,870 | 33,682 | `15a89d5295739ae1381a3de8b1c77e9b7a5a75cbd02617399b06aa2edfdcf976` |
| L5 `B_then_A` | 38,552 | 4,870 | 33,682 | `4ec9780558bc32eb41aa07f90d5617f0093079ff22c6d44df6462a7cb743502e` |
| L6 `A_then_B` | 38,552 | 4,870 | 33,682 | `925534b5de302f06b9cd70b4fa9b994a2a5de7ddad0fc617d8c03cdec0e1098a` |
| L6 `B_then_A` | 38,552 | 4,870 | 33,682 | `98424f2f2baa682e5cadb26a4785fce53b97d8b20ac7e7cb22affe4bfd00b82f` |

All primitive supports are one or two M2, and every two-M2 call is nearest
neighbour.  L5 and L6 each use 273 compiler-live M2 and have maximum routed
pair length 64.

`W_V^dagger` and `W_V` retain Cycle 539's exact equality-controlled macro
decomposition: every Toffoli expands into the strict 15-call one-/two-M2
schedule and every pair is routed on the same integer microgrid.  Widening to
`n<=3` raises the conservative forward-`W_V` Toffoli upper count to
295,393,418 and the sweep `W_V^dagger+W_V` count to 590,786,836.  These are
finite constant upper bounds for this fixed patch, not efficiency or
minimality claims.  The runner materializes the 38,552-gate decoded runtime;
it verifies the inherited exact macro expansion and universal router for the
much larger `W` rather than allocating billions of repeated primitive rows.

## Collision and color audit

`W_V^dagger`, decoded runtime, and `W_V` are sequential phases and may reuse
the same clean work positions.  Within each decoded coin, seam, or contact
stage, the runner builds the actual route-support conflict graph of the two or
three nominally parallel blocks.  Greedy coloring uses at most three classes,
with zero same-color support collisions at L5 and held L6.

Blocks within one color have disjoint route support.  Colors and within-block
gate indices are compiler layers only.  No gate count, color, layer, or update
order is interpreted as duration, causal time, rate, or realized history.

## Proper-cubic covariance

At the logical level, each of the two overlapping updates and both ordered
sweeps are recompiled in all 24 proper-cubic frames on the complete 2,325-state
domain.  The maximum update covariance raw residual is
`1.8619006149354548e-16`; the maximum two-update sweep residual is
`4.47545209131181e-16`.  All 576 frame products close exactly.

At the schedule level, every live wire and every actual route edge is rotated
through the 24-member compile-time orbit at L5 and held L6.  Site injection,
nearest-neighbour, and color-intersection failures are zero.  The base-chart
periodic tie is transported with the route; it is not recomputed by a runtime
frame query.

This is a mapped schedule orbit, not one raw gate list invariant under every
frame and not a host-side orientation selector.

## Four obligations kept separate

1. **Algebraic code-space isometry.**  The normalized S4 branch construction
   and injective 917,376-row decoder prove `W_V` on all declared columns.
2. **Fixed-Wilson/reference preparation.**  `Omega_fixed` and its initial
   preparation remain supplied.  No genesis theorem is inferred from the
   isometry.
3. **Route blank genesis.**  Branch, order, conjunction, and tag work M2 are
   supplied blank.  The route itself may carry data and is exactly reversed;
   the tags return blank.
4. **Volume recurrence.**  Both overlapping orders recur exactly on this one
   fixed shared volume.  Adjacent stars and periodic tiling remain open.

These are not four names for one residual.  In particular, successful volume
recurrence does not prepare the fixed reference, and a reference initializer
would not supply a translation-equivariant overlap schedule.

## Cycle-532 target-times-gauge interface

Cycle 532 is rerun at L5 and held L6.  Its fixed-spin rough code still factors
sectorwise as the complete target Fock factor times the `N-1` gauge factor,
and its full-Fock `Gamma(P)`, mass, contact, and seam controls pass.  Cycle 540
still gives a literal support-13 rough-code FSWAP implementation of that same
target seam.

The carrier boundary is important: Cycle 539's selected carrier is based on
the Cycle-269 physical code, whereas Cycle 532/540 acts on the rough-terminal
Cycle-247 carrier.  Cycle 545 does **not** equate those physical Hilbert
spaces.  Their shared object is the target CAR update.  No physical
`E_539 <-> E_532` transducer is supplied here.

Consequently:

- the recurrent compiler theorem is physical on the Cycle-539 selected
  carrier and its persistent q M2;
- the Cycle-532 target-times-gauge theorem is an independent exact semantic
  and physical comparator for the same target update; and
- combining the two carriers into one unconditional rough-code preparation
  would require an explicit transducer or a new rough-code isometry compiler.

This separation prevents a logical equality from being presented as a gate
between unrelated encodings.

## Inverse, leakage, and deletions

The certificate distinguishes each load-bearing part:

- deleting the first special branch Givens leaves residual above `0.4`;
- deleting a joint-order Givens leaves residual above `0.1`;
- deleting one S4 order amplitude gives Gram residual `1/24`;
- deleting one new `n=3` decoder minterm leaves branch amplitude;
- deleting one legality minterm rejects one lawful `n=3` ray;
- deleting the second overlapping update gives raw residual
  `1.316097915613727`;
- deleting the shared seam gives raw residual `0.8740010519307571`;
- Cycle 540's rotation, Rz, CNOT, and bad-blank controls remain nonzero; and
- deleting a return routing SWAP leaves displaced intermediate data.

The exact reverse schedule uses reverse gate order and daggered cores.
Terminal branch/order/work/tag leakage and route displacement are zero on the
lawful domain.  Primitive intermediate code preservation is not claimed.

## Supplied structure and novelty boundary

Supplied rather than derived are:

1. the fixed-Wilson reference and fixed-sector preparation;
2. blank branch, order, conjunction, and tag M2;
3. Cycle-533 selected coefficients, physical representatives, decoder style,
   exact Toffoli, and integer router;
4. Cycle-539's S4 order grammar and fixed star placement;
5. Cycle-219 coin and Cycle-230 contact, coupling, seam ports, and factor order;
6. exact analog Givens, contact, and Rz angles;
7. the 917,376-entry compile-time decoder/legality table;
8. the two patch addresses and either supplied sweep order;
9. L5/L6 finite periodic boundaries and compile-time frame; and
10. the `n<=3` lawful-domain cutoff.

New here are the exact `n=3` S4 decoder extension, one-global-role overlapping
compiler, both noncommuting lawful sweep orders, repeat recurrence, the
materialized 38,552-call nearest-neighbour runtime schedules, collision/color
audit, full-sector-through-`n=3` covariance, and the explicit Cycle-539 versus
Cycle-532 carrier interface audit.

The result is not a minimum-gate theorem, an all-sector four-cell compiler, an
all-volume tiling, an autonomous update-choice law, a fixed-reference
preparation theorem, a physical clock, a Record theorem, a Born rule, or a
gravity/source derivation.  Thirring machinery is neither used nor compared.

## Dependency-ledger effect

- `C_ref`: unchanged.  One global S4 role removes independent patch-order
  duplication, but fixed-Wilson/reference preparation, exact tables, patch
  addresses, and compile-time frame remain supplied.
- `C_num`: advances.  The four-cell star is widened from `n<=2` through the
  complete `n=3` sector.  Sectors `n=4,...,24`, number change, and arbitrary
  volume remain open.
- `C_wrap`: unchanged.  Two explicit sweep orders are compiler inputs; no
  schedule is time, interval, energy, rate, Record, or realized history.
- `C_int`: advances materially.  Mass, contact, four literal seams per sweep,
  inverse, both update orders, and repeats now sit behind one recurring shared
  patch compiler.
- `C_local`: advances materially.  Cycle 539's “differently overlapping patch
  recurrence” boundary closes for one degree-three shared volume, with NN
  gates, collision colors, held size, and all frames.  Periodic adjacent-star
  recurrence and carrier transduction remain open.
- `C_source`: unchanged.

No maturity score changes are proposed from this compiler-only result.  There
is no shared obstruction and no axiom pressure.

## No-go discipline N1–N8

Broad impossibility, minimum-content, and axiom-pressure gate status:
**FAIL / DO NOT SHIP**.  The cycle is constructive and leaves several concrete
extensions open.

### N1 — alternative-route normalization

| normalized family | primary object / mechanism / terminal obligation | honesty and disposition |
|---|---|---|
| one global S4 volume isometry | fixed four-cell selected code / one decoder and role / two overlapping recurrent updates | **ATTEMPTED — succeeds through complete n<=3** |
| independent overlapping patch roles | two S3/S4 registers / local commuting constraints / shared-cell recurrence | **ATTEMPTED BY PRIOR — fails only for the independent-role ansatz in Cycles 319/324** |
| larger adjacent-star permutation role | two-star code / one larger joint group / injective decoder and recurrence | **OPEN / UNTESTED** |
| transported staggered slot | persistent local slot / serialize incident patches / autonomous return and covariance | **OPEN / UNTESTED** |
| rough-factor direct compiler | Cycle-532 target x gauge / literal Cycle-540 blocks plus onsite rotations / prepared recurrent rough code | **OPEN / PARTIAL: runtime factors exist, transducer/preparation absent** |
| translation-equivariant colored tiling | periodic block graph / bounded local coloring / all-size recurrent volume | **OPEN / UNTESTED** |
| measurement/reset preparation | local syndromes / prepare fixed reference and blanks / convergence and reuse | **OPEN / UNTESTED** |

These families differ in object, load-bearing mechanism, and terminal
obligation.  The positive first route and six open/partial routes prohibit a
broad negative.

### N2 — wall-independence audit

The collapsed residual set is:

```text
W_ref       fixed-Wilson/reference genesis,
W_blank     branch/order/tag blank genesis and renewal,
W_bridge    selected-carrier <-> rough-carrier physical transduction,
W_number    four-cell sectors n=4,...,24 and number change,
W_volume    adjacent-star/all-size translation-equivariant recurrence.
```

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_ref,W_blank` | no | no | yes |
| `W_ref,W_bridge` | no | no | yes |
| `W_ref,W_number` | no | no | yes |
| `W_ref,W_volume` | no | no | yes |
| `W_blank,W_bridge` | no | no | yes |
| `W_blank,W_number` | no | no | yes |
| `W_blank,W_volume` | no | no | yes |
| `W_bridge,W_number` | no | no | yes |
| `W_bridge,W_volume` | no | no | yes |
| `W_number,W_volume` | no | no | yes |

Literal runtime routing, fixed-patch overlap recurrence, and the `n=3` decoder
are closed here and are not counted as residual walls.  The order choice is
supplied schedule data, but an autonomous choice law belongs to `W_volume`
rather than a sixth duplicated wall.

### N3 — hidden-wall scan

The mandatory scan covers “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  None discharges a
proof obligation.  Fixed reference, blank registers, coefficient and decoder
tables, angles, q input, S4 preparation, patch addresses, update order,
cutoff, finite boundary, compile-time frame, carrier mismatch, and router are
all explicit supplies.  “Standard” appears only in descriptions of an exact
cited decomposition and is not load-bearing authority.

### N4 — residual matching

| witness | witness residual | Cycle-545 residual | match? |
|---|---|---|---:|
| Cycle 539 runner `:570` | differently overlapping patch recurrence not proved | two shared-cell corner updates on one global S4 star | yes; fixed-patch residual retired |
| Cycle 539 runner `:244` | injective decoder only through star `n<=2` | same decoder mechanism through complete star `n=3` | yes; sector widened |
| Cycle 540 runner `:425` | four-rotation target equals `-i FSWAP` | every decoded-runtime FSWAP core | yes |
| Cycle 540 runner `:296` | literal NN parity-rotation compilation | adjacent two-M2 specialization plus routed calls | yes for FSWAP primitive form |
| Cycle 532 runner `:296` | rough fixed code equals target x gauge | common target comparator | yes for target semantics, not carrier transduction |
| Cycle 532 runner `:911` | full-Fock `Gamma(P)` target | seam target replay | yes |
| Cycle 532 runner `:935` | mass/contact/seam logical fixtures | same fixture values | yes |

The Cycle-532 factor theorem is explicitly dropped as evidence for a physical
Cycle-539-to-rough transducer because those residuals differ.

### N5 — rhetoric audit

| resolution | tested disposition |
|---|---|
| one primitive | every runtime gate has support one/two M2 and every pair is NN |
| one FSWAP block | exact Cycle-540 four-rotation identity |
| one local cell block | Cycle-523 coin/contact reconstruction and blank tag return |
| one three-cell update | complete four-cell `n<=3` embedding, mass/contact/two seams |
| two overlapping updates | both distinct orders, inverse, deletions, repeats |
| one fixed four-cell volume | exact single-S4 recurrence |
| held L6 | identical decoder plus literal schedule and all-frame orbit |
| adjacent stars / periodic volume | not tested; no closure or negative claimed |
| infinite volume / continuum | not tested; no statement |

“Recurrent volume” is always narrowed to the one fixed four-cell volume.
“Literal schedule” distinguishes the materialized decoded runtime from the
exact macro-expanded but non-materialized billion-row `W` schedule.

### N6 — partial-closure path

Retain the one-global-S4 fixed patch and its `n=3` decoder.  A direct extension
can place two adjacent stars under either one larger joint permutation role or
a transported local slot, compile one collision-free translated layer, and
test recurrence before increasing volume.  Independently, measurement/reset
or dissipative stabilization could retire the reference and blank supplies.
These are constructive import-retirement paths; no new axiom is implied.

### N7 — hostile steelman

> A hostile reviewer should reject any claim that fixed-patch success proves
> periodic-volume recurrence.  The compiler decodes the whole four-cell star,
> uses a supplied S4 register and enormous truth table, and re-encodes it; two
> adjacent stars would overlap both native roles and decoder domains.  But that
> is also why no no-go follows: Cycles 319, 324, and 539 already show that a
> larger joint role or a transported slot can replace incompatible independent
> registers.  The actionable terminal is one two-star injective decoder or one
> autonomous slot-return theorem with a collision-free all-frame schedule.

This concrete route keeps the broad no-go gate failed.

### N8 — cross-cycle echo

Cycle 319 replaced incompatible independent edge companions with one S3 role.
Cycle 324 replaced three overlapping S3 checks with one S4 role or a slot
cycle.  Cycle 533 replaced failed invariant pair separators with a joint
decoder.  Cycle 539 combined those mechanisms on one patch but stopped before
differently addressed recurrence.  Cycle 545 uses one global S4 decoder and
decodes only once, retiring that fixed-patch recurrence residual.  Each prior
apparent overlap wall yielded to a relational auxiliary rather than an axiom.

No cross-cycle evidence supports a route-independent obstruction, minimum
content, or constitutional change.

## Disposition and next campaign

Retain Cycle 545 as the strongest fixed-volume recurrent compiler candidate:

- one global shared-cell S4 isometry;
- complete four-cell sectors through `n=3`;
- two genuinely overlapping, noncommuting update orders;
- exact repeats, inverse, and terminal leakage controls;
- literal 38,552-call decoded one-/two-M2 NN schedules;
- 304 Cycle-540 FSWAP blocks with exact net phase one;
- collision-free stage coloring;
- L5/held-L6 and all-24/576 covariance; and
- mass, contact, seam, and full-target comparators.

The highest-value next compiler campaign is not route-blank compression.  It
is a two-adjacent-star recurrence tournament: compare one larger joint role,
a transported slot, and a translated color schedule, requiring one persistent
q/reference allocation and exact return after both star updates.  In parallel,
the independent fixed-reference preparation campaign remains higher-level
infrastructure.  A selected-to-rough physical transducer should be attempted
only if the campaign wants Cycle-532's rough carrier, rather than silently
conflating the two encodings.
