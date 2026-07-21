# Physical covariant parity-chain gadget and dynamic pump — Cycle 544 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_covariant_parity_chain_dynamic_pump_cycle544_2026_07_21.py`.

## Result

Cycle 544 constructs a literal nongeometric stabilizer gadget in unused
Cycle-527 microgrid sites.  It uses **six oriented open parity chains**, one
for each signed cubic direction.  Opposite chains impose the same unoriented
axial Wilson character.  Their single relation leaves exactly one stabilizer
**rank surplus** per axial character.  The six-chain set is one fixed physical
object: its sites, checks, and incidences rotate into themselves under all 24
proper-cubic frames and all 576 products, with no runtime selector.

This closes several parts of the requested route constructively.  The fixed
physical adjacency is injective and collision-free; every check has support
at most ten and physical L1 diameter at most 20; the L5 and held-L6 stabilizer
codes have exactly Cycle 537's target-times-gauge ranks, both matter parities,
and full commutant.  Full-Fock `Gamma(P)`, mass, onsite Givens, contact, seam,
inverse, leakage, and deletion controls replay.

The fixed gadget nevertheless fails the required uniform dressing locality.
A local rough constraint crossing an open-chain cut has a unique chain
syndrome solution using `L-1` auxiliary `X` factors.  The explicit maximum is
four at L5 and five at held L6 in one oriented chain; across all six chains the
witness uses 15 and 18 factors.  Its physical diameter grows `72 -> 88`.
This is a route-specific falsifier, not a minimum-content theorem or a general
no-go for bounded stabilizer gadgets.

Cycle 544 therefore also executes a distinct **dynamic pump**.  Six reset
syndrome tokens coherently extract the three Wilson signs with local routed
controlled-Pauli gates.  A reset-averaged choice of the two signed dual
membranes corrects each negative sign.  The channel is trace preserving,
uses no postselection, maps the lawful rough local-code domain into the
all-plus sector in one sweep, and is idempotent.  Every routed two-M2 edge is
nearest neighbour and reverses its path; the coherent pre-reset circuit has a
literal reverse dagger.  The terminal reset is intentionally irreversible and
is not called a Record or an inverse unitary.

The pump is not a completed product/reset-input code-space isometry.  Each
dual membrane has support `L^2`, its route radius grows, and no Wilson-flipping
Pauli commuting with the complete matter/gauge target algebra exists in the
exact affine solve.  The two signed membranes also differ by target logical
action, so the covariant average dephases that unresolved choice.  The pump
closes sector convergence from an already lawful rough-code input; it does not
preserve arbitrary target data transparently or prepare the full rough code
from product inputs.

Broad negative gate: **FAIL / DO NOT SHIP**.  There is no shared substrate
obstruction and no axiom pressure.

## Exact target contract

| field | Cycle-544 contract |
|---|---|
| target | Build one fixed, local, collision-free, proper-cubic auxiliary gadget that removes the three Wilson characters with exact target factor and a local product/reset encoder or autonomous pump. |
| domain | Cycle-532 rough code at L5 and held L6, Cycle-527 installed microgrid, all six directions, all 24 frames and 576 products. |
| allowed inputs | target data inputs, declared reset M2, bounded local checks/gates, explicit dissipative reset for an autonomous pump. |
| forbidden weakenings | No abstract cap, global Wilson initializer, parity callback, host branch, runtime frame selector, postselection, or route schedule called physical time. |
| static completion | Exact rank surplus three, bounded check and dressing support, target×gauge factor, fixed all-24 placement, literal local encoder. |
| dynamic completion | Local defect/sign extraction, covariant correction, proved convergence, lawful-domain preservation, inverse for coherent work, explicit reset boundary, target-transparent encoding. |
| not completion | Rank alone, bounded checks with growing dressings, an all-plus projection, or convergence that scrambles target data. |

## Fixed six-chain hypergraph

For each signed direction `d` and positions `j=0,...,L-1`, let

```text
x_j(d) = j D_d mod L.
```

The chain has auxiliary M2 `p_(d,j)` for `j=0,...,L-2`, physically placed at

```text
r[p_(d,j)] = 16 x_j(d) + 4 D_d  mod 16L.
```

These are genuine points in the already installed integer microgrid, not
abstract cap edges.  They do not collide with one another or with any of the
`22L^3` rough M2.  Positive and negative chains occupy the two signed axial
corridors, while the three axes meet no common site because the offset is
nonzero.

Let `w_x` be Cycle 537's bounded Wilson chunk owned by coarse cell `x`.  The
chain checks are

```text
C_(d,0)     = w_0 Z[p_(d,0)]
C_(d,j)     = w_(x_j(d)) Z[p_(d,j-1)] Z[p_(d,j)]
C_(d,L-1)   = w_(x_(L-1)(d)) Z[p_(d,L-2)].
```

Their product is the exact axial Wilson Pauli, including phase.  Opposite
directions give the same product.  Across six chains there are `6(L-1)` new
M2 and `6L` displayed checks, with three relations between opposite products.
The net rank gain is therefore

```text
6L - 3 = 6(L-1) + 3,
```

exactly new-M2 count plus the three desired character fixings.

## Exact factor and held-size recurrence

| quantity | L5 | held L6 |
|---|---:|---:|
| rough M2 | 2,750 | 4,752 |
| chain M2 | 24 | 30 |
| total M2 | 2,774 | 4,782 |
| displayed chain checks | 30 | 36 |
| stabilizer rank | 1,900 | 3,271 |
| code exponent | 874 | 1,511 |
| matter dimension/rank | `1499/1498` | `2591/2590` |
| gauge dimension/rank | `249/248` | `431/430` |
| full commutant dimension/rank | `249/248` | `431/430` |
| both matter parities | nonempty | nonempty |

Check products, check-check commutators, matter/gauge stabilizer commutators,
and matter-gauge commutators have zero failures.  Matter parity and gauge
parity remain the same center on code.  The chain code is therefore exactly
the Cycle-537 target full-Fock factor tensor the `(N-1)` gauge factor,
sectorwise across the shared parity.

Maximum M2 supports are:

| family | L5 | held L6 |
|---|---:|---:|
| chain check | 10 | 10 |
| dressed local | 38 | 40 |
| dressed matter | 16 | 17 |
| dressed gauge | 23 | 24 |

The check bound is genuinely constant.  The dressed bounds are not.

## Unique dressing and static-route failure

For a Wilson-commuting Pauli `P`, write `s_j=1` when `P` anticommutes with
chunk `w_(x_j(d))`.  Dressing by chain `X` variables `u_j` requires

```text
u_0 = s_0,
u_j = u_(j-1) XOR s_j,
s_(L-1) = u_(L-2).
```

Even Wilson syndrome makes the last equation consistent, but the solution is
unique.  When a bounded rough constraint straddles the omitted chain edge,
`s` is supported at the two endpoints and every `u_j=1`.  No alternative
short path exists inside that open chain.

The exact worst witness is a bounded local constraint:

```text
L5: per signed direction (4,1,4,1,4,1), total 15
L6: per signed direction (5,1,5,1,5,1), total 18.
```

Thus one orientation makes each physical seam short, but the opposite member
of the fixed covariant pair makes it long.  Both sets of checks must be
commuted with, so duplicating orientations does not repair locality.  Maximum
dressed-local physical L1 diameter grows from 72 to 88 even though check
diameter stays 20.

This is unfinished implementation of one hypergraph family, not evidence that
all nongeometric stabilizer gadgets fail.

## One fixed proper-cubic placement

A proper-cubic frame maps

```text
(d,j) -> (frame(d),j)
```

and rotates `16x_j(d)+4D_d` to the corresponding installed site exactly.  The
runner checks every auxiliary coordinate and every displayed check incidence
at L5 and held L6 under all 24 frames.  It checks all 576 signed-direction
products.  Coordinate, incidence, group, and collision failures are zero.

This is not a 24-presentation schedule orbit.  All six signed chains are
simultaneously present as one fixed set.  No runtime frame selector or hidden
choice of positive axis is used.

## Dynamic sector pump

The dynamic route starts from the lawful Cycle-532 bounded-local rough-code
domain and six reset syndrome tokens.  For one Wilson `W`, the coherent
measurement macro is

```text
H(token); routed controlled-w_0; ...; routed controlled-w_(L-1); H(token).
```

It realizes the standard decomposition into `P_plus=(I+W)/2` and
`P_minus=(I-W)/2` without measuring or postselecting.  A token-controlled dual
membrane `Q` anticommutes with its Wilson and commutes with every bounded local
rough stabilizer and the other two Wilsons.  There are two signed membranes.
The fixed covariant channel retains both as reset-averaged Kraus branches:

```text
K_plus       = P_plus,
K_minus,+/-  = 2^(-1/2) Q_(+/-) P_minus.
```

Hence

```text
K_plus^dag K_plus + sum_(+/-) K_minus,+/-^dag K_minus,+/- = I.
```

Every output is in the plus sector.  Reapplying the channel changes nothing,
so convergence is exact in one sweep and the channel is idempotent.  The
coherent gates before reset have a reverse-dagger list.  The final local token
reset supplies the entropy sink; the resulting channel is deliberately not
claimed to have a unitary inverse.

Every controlled factor is routed by ordinary tensor SWAP along a shortest
periodic Manhattan path and the path is reversed.  All axis-order and
antipodal-sign variants are retained as a covariant route family.  Exact
counts are:

| dynamic control | L5 | held L6 |
|---|---:|---:|
| dual membrane weight per axis | 25 | 36 |
| controlled Wilson factors, six tokens | 190 | 226 |
| controlled membrane factors, six tokens | 150 | 216 |
| shortest route variants enumerated | 1,028 | 1,862 |
| maximum one-way route distance | 76 | 108 |
| non-nearest-neighbour edges / endpoint failures | 0 / 0 | 0 / 0 |

The route lengths and membrane weights grow.  A compiler count is not called
physical time, a generator is not called a rate, and reset output is not
called realized history.

## Why the pump is not yet the requested encoder

The exact affine problem asks for a Pauli `Q_a` that

- commutes with every bounded local stabilizer;
- commutes with all matter and gauge generators;
- commutes with the other two Wilsons; and
- anticommutes with `W_a`.

At both L5 and held L6 it is inconsistent for all three axes.  The displayed
dual membranes do preserve the local rough code and flip only the intended
Wilson, but they have 300/432 matter-gauge commutator failures.  The two
parallel signed membranes are not equivalent modulo local stabilizers; their
difference is a target logical action.  Reset-averaging restores proper-cubic
covariance at the channel level but dephases this target-logical choice.

Thus the channel autonomously fixes the sector of an already lawful rough
state, but it does not intertwine the target algebra as identity and does not
prepare the rough code itself from product inputs.  A full encoder must either
carry the membrane branch as a protected relational degree and uncompute it,
or build a code deformation whose target identification is explicit.

Deletion controls are load-bearing: deleting one membrane Pauli factor
creates four local-stabilizer syndromes on every axis.  Omitting the correction
leaves negative-sector output; omitting reset leaves the token branch present.
These are distinct from postselection failure.

## Retained physics fixtures

Cycle 544 reruns the full Cycle-537 certificate.  `Gamma(P)` retains
280,875/839,160 mode-pair tests with zero coefficient failures and
281,626/840,457 complete low-sector tests.  The 4,096 two-cell and 988
straight/corner three-cell controls pass.  Onsite/contact/B maximum supports
remain `7/16/17` in the Cycle-537 realization.

The Cycle-219 mass residual is `2.220446049250313e-16`.  Onsite
intertwiner/inverse/leakage residuals are `5.272182555577386e-15`,
`7.504184205291937e-15`, and zero.  The Cycle-230 contact deletion residual is
`0.36789306705608243`; seam singular values are
`[0.49577140670498115,0.45566604871445016]`, with six pass and zero fail
subchecks.  FSWAP matrix/unitarity/inverse residuals are zero and deleting its
fourth term leaves residual one.

Cycle-537 deletion ranks and dressing syndromes also replay.  These results
remain conditional physics comparators for the exact factor; the growing
static dressing and target-nontransparent pump prevent calling Cycle 544 a
full physical encoding.

Put explicitly: this is **not postselection**, and the **lawful domain** is
the bounded-local Cycle-532 rough code.

## Cold certificate

The final cold invocation was

```text
python3 scripts/physical_covariant_parity_chain_dynamic_pump_cycle544_2026_07_21.py \
  --mode parity-chain-pump-certificate
```

and returned status
`cycle544-fixed-chain-rank-positive-locality-negative-dynamic-pump-partial`,
with all `11/11` groups passing.  The runner's internal resource envelope was
`216.46758133301046 s`, `150,650,880` maximum RSS bytes, and zero process
swaps.  The external `/usr/bin/time -l` envelope was `218.32 s`, with the same
maximum RSS and zero swaps.  The strengthened run also maps both signed
membranes in every frame; L5 and held L6 each return zero all-24
signed-membrane-set failures.

## Supplied, derived, and open

Supplied:

- Cycle-527 installed microgrid and ordinary H/controlled-Pauli/SWAP/reset
  primitive laws;
- Cycle-532 rough local code, matter/gauge algebra, and axial Wilson chunks;
- macro origin `(0,0,0)`, six signed corridors at offset `4D`, and finite
  L5/held-L6 domains;
- one open-chain cut at the macro origin for each orientation;
- six reset syndrome tokens and the reset-averaged signed-membrane choice;
- Cycle-219/Cycle-230 target coefficients and Cycle-537 factor order.

Derived:

- injective collision-free fixed physical adjacency;
- exact check products, three rank surplus, target×gauge factor, and both
  parities;
- bounded check support and exact growing-dressing witness;
- all-24/576 fixed-object covariance;
- a trace-preserving, idempotent, one-sweep Wilson-sector pump;
- literal NN route families, coherent reverse dagger, reset boundary, and
  deletion syndromes.

Open:

- a fixed hypergraph with uniformly bounded dressings;
- a target-transparent membrane/branch identification;
- a product/reset-input encoder for the rough local code and filled sector;
- a unitary realization of the dissipative reset, if required by a stronger
  closed-system target;
- full recurrent physical update on the prepared code.

There is no runtime frame selector, host-side parity service, postselection,
global Jordan-Wigner order, or growing Wilson initializer in the static check
list.  Thirring machinery is not used.

## Dependency disposition

- `C_ref`: advances diagnostically.  Wilson signs can be pumped without a host
  parity query, but target-transparent reference preparation remains open.
- `C_num`: retained in the exact static factor; both matter parities survive.
- `C_wrap`: advances through a literal covariant sector-convergence channel;
  the membrane branch and reset remain supplied structures.
- `C_int`: retained algebraically through the fixed factor, not through the
  nontransparent pump.
- `C_local`: fixed check adjacency and all primitive route edges are local;
  static dressings and dynamic route radius still grow.
- `C_source`: unchanged.

No maturity score is raised by a partial sector pump.

## N1–N8 no-go discipline

Broad gate: **FAIL / DO NOT SHIP**.  Disposition:
`static-chain-partial-plus-dynamic-sector-pump-partial`.

### N1 — normalized alternatives

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| six open parity chains | fixed signed-axis hypergraph / exact rank surplus / uniformly bounded dressing | **ATTEMPTED — rank/covariance positive, dressing negative** |
| local cycle-space gadget | bounded graph with local cycle stabilizers / local right inverse / eliminate winding cycle without global row | **OPEN** |
| non-CSS mixed-Pauli gadget | commuting symplectic hypergraph / evade CSS incidence obstruction / exact target factor and local dress | **OPEN** |
| dynamic membrane pump | reset channel / coherent sign extraction plus correction / target-transparent product-input encoder | **ATTEMPTED — sector convergence positive, transparency negative** |
| reversible code deformation | moving cut or puncture / transport defect and restore checks / branch uncompute and exact inverse | **OPEN** |
| relational frame field | protected signed membrane label / keep correction branch coherent / local update and cleanup | **OPEN** |
| general local Clifford encoder | reset/data tableau / routed stabilizer Gaussian elimination / fixed proper-cubic circuit | **OPEN** |

These families differ in primary object, invariant, and terminal obligation.
Several live families block a broad impossibility or minimum-content claim.

### N2 — wall-independence audit

The collapsed wall set is:

```text
W_static-local:
find a fixed rank-correct covariant gadget whose complete target algebra has a
uniformly bounded physical dressing.

W_prepare:
construct a target-transparent encoder or convergence channel from declared
product/reset inputs, including the rough local code rather than assuming it.
```

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_static-local`, `W_prepare` | no | no | yes |

Rank, collision, check locality, and covariance are closed inside the chain
candidate and are not separate walls.  The membrane's growing support and its
target nontransparency are two symptoms of `W_prepare` for the dynamic route,
not claimed as independent constitutional admissions.

### N3 — hidden-wall scan

The proof was scanned for “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  The macro origin,
open cuts, signed corridors, reset tokens, membrane pair, reset averaging,
finite sizes, target tables, growing paths, and missing rough-code encoder are
explicit supplies or walls.  “Local” is always resolved separately for check
support, physical gate edges, operator dressing, and total schedule radius.

### N4 — residual matching

| witness | witness residual | Cycle-544 use | match? |
|---|---|---|---:|
| Cycle 537 rooted chain | open-chain root dressing grows `4->5` | same unique prefix solution, now in fixed all-24 six-chain object | yes |
| Cycle 542 cubical homology | geometric cap cannot bound axial cycle | motivation for nongeometric check hypergraph only | yes for route selection, not negative evidence |
| Cycle 532 Wilson rows | three characters remain beyond bounded rough checks | exact three rank surplus of chain gadget | yes; closed algebraically |
| Cycle 533 fixed reference | selected-seam encoder assumes fixed Wilson state | product/reset reference preparation | yes; still open |
| Cycle 527 NN router | routed controls restore intermediates | dynamic token/membrane route | yes for routing, not target transparency |

Cycle 533 separator failures and Cycle 526 endpoint conflicts are dropped; they
do not match either current residual.

### N5 — rhetoric audit

| resolution | tested | disposition |
|---|---:|---|
| one chain check | every check L5/L6 | support <=10, diameter <=20 |
| one oriented chain | exact product/rank and unique dressing | cut-crossing support `L-1` |
| six-chain fixed object | all coordinates/incidences | collision-free, all24/576 |
| complete static algebra | L5/L6 ranks and commutants | exact target factor, nonuniform dress |
| one pump Kraus family | exact Pauli algebra | trace preserving and plus-sector output |
| routed primitive | all enumerated path variants | nearest neighbour, reverse-restored |
| target algebra under pump | exact affine solve and commutators | not transparent |
| arbitrary stabilizer hypergraph | not tested | no negative claim |
| product-input full encoder | not constructed | open |

“The fixed chain fails locality” means its dressed operator family, not its
checks or primitive gates.  “The pump prepares the sector” does not mean it
prepares the full code or preserves target data.

### N6 — partial-closure paths

The chain gadget is an import-retirement attempt: explicit corridors replace
abstract cap topology and growing Wilson rows, then the held-size dressing
audit exposes the residual.  The pump retires host-side Wilson selection via
an explicit reset channel, then exposes target-branch transparency.  A local
cycle-space gadget, non-CSS stabilizer, relational membrane branch, or
reversible puncture can attack these residuals without axiom language.

### N7 — hostile steelman

> A hostile reviewer should reject any claim that the growing prefix solution
> is fundamental.  It follows because Cycle 544 chose six independent open
> incidence chains.  A bounded non-CSS cluster gadget can add local
> anticommuting gauge generators whose center fixes the Wilson while short
> representatives move through gauge, or a reversible puncture can carry the
> missing cut past each update and return it.  Likewise the two membrane
> branches need not be reset-averaged: retaining their sign as a protected
> local frame field could make the target identification coherent and permit
> uncomputation.  The exact obligations are a local symplectic right inverse
> and a branch-aware target intertwiner, not a new axiom.

The steelman is actionable and keeps the broad gate at FAIL.

### N8 — cross-cycle echo

Cycles 247/269 exposed topological multiplicity; Cycle 532 turned its
extensive portion into a gauge subsystem; Cycle 537 removed three residual
characters after importing cap topology; Cycle 542 showed why an unchanged
cubical cap cannot be the physical realization.  Cycle 533 replaced a dense
isometry by a literal auxiliary compiler despite earlier separator failures.

Cycle 544 repeats both lessons.  Nongeometric local checks close rank and
covariance but one graph choice leaves growing dressings.  A local reset pump
closes sector convergence but leaves coherent target identification.  Prior
global walls have been retired by relational carriers, so neither residual is
axiom pressure.

## Next campaign

Retain the membrane side as a protected relational frame qubit instead of
reset-averaging it.  Construct a branch-controlled target-algebra
intertwiner, transport the frame locally with a reversible puncture, and
uncompute it after restoring periodic checks.  In parallel search a non-CSS
bounded gauge gadget whose local gauge equivalences provide a constant-support
right inverse for every seam syndrome.  Require L5/held-L6, fixed all24/576,
literal product/reset encoder, full target replay, and deletion/leakage before
promotion.
