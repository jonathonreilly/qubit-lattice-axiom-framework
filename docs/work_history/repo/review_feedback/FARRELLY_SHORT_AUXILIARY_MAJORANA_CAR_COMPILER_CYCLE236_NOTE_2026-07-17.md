# Farrelly–Short auxiliary-Majorana CAR architecture — Cycle 236

**Date:** 2026-07-17

**Type:** conditional all-size even-algebra representation plus a falsified
bounded-local encoding/preparation attempt

**Status:** bounded physical update gates on all `L=3,4,5` matter parity
sectors and the contact seam block, but nonlocal Jordan–Wigner constraint and
preparation surfaces

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** draft parking branch and existing draft PR #5389 only

Companion runner:

```text
scripts/FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_2026_07_17.py
```

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, audit, or queue surface.

## Result up front

The Farrelly–Short mechanism gives the strongest all-size **update-gate**
representation in the campaign so far, but it does **not** give the requested
bounded-radius local encoding.

For each of the three positive-axis coarse links, add one auxiliary complex
fermion at each endpoint.  This is six auxiliary modes per cell, in addition
to the six Cycle-230 matter modes.  For link `e=<xy>`, define

```text
m_(x,y) = c_(x,y) + c_(x,y)^dagger,
M_e = i m_(x,y) m_(y,x).
```

These are the auxiliary Majoranas and link operators of Farrelly–Short
equations `III.12–III.14` and `D.2–D.5`.  Distinct links use distinct auxiliary
modes, so all `M_e` commute.  The prepared link state in their equations
`G.2–G.3` also has odd complex-fermion parity on each link.  Declaring

```text
M_e = +1,
P_aux,e = (-1)^(n_(x,y)+n_(y,x)) = -1
```

fixes the two auxiliary qubits on every link and leaves exactly six logical
matter qubits per cell.  The second condition is not an extra Farrelly–Short
dynamical requirement; it makes explicit the particular Appendix-G state and
removes its otherwise unused Majorana partner from the code count.

The Cycle-230 intercell stream factor on matter modes `a_x,b_y` is

```text
FSWAP_(xy) = exp[i pi Q_(xy)/2],
Q_(xy) = n_a+n_b-a^dagger b-b^dagger a.
```

Replace its generator by

```text
Q_tilde_(xy)
  = n_a+n_b-a^dagger M_e b-b^dagger M_e a.
```

On `M_e=+1`, the two generators and their exponentials agree.  In a
site-major Jordan–Wigner order, each physical fermion and its endpoint
Majorana are consecutive within one bounded cell block.  Their two strings
cancel.  The runner obtains

```text
|| exp(i pi Q_tilde/2) E_e - E_e FSWAP ||
    = 3.2078929115721493e-16,
maximum dressed Pauli weight = 14       for L=3,4,5,
constraint/update leakage residual = 0.
```

The onsite Cycle-230 `A` swaps, `Gamma(C)` coin, and contact are already even
within one cell and remain bounded in the same presentation.  Thus, for the
globally prepared auxiliary state and the complete coarse update,

```text
E_global G_coarse = G_physical E_global.
```

This is a **conditional global isometry**, not a bounded-radius local
encoding.

The load-bearing failure is on the code and preparation surface.  The qubit
image of `M_e` itself is the Jordan–Wigner string

```text
JW(M_e) = +/- Y_(x,y) [product of intervening Z qubits] X_(y,x).
```

Its maximum weight grows as

| Domain | `max wt(JW(M_e))` | sum of `M_e` weights | Appendix-G prefix touches |
|---|---:|---:|---:|
| `L=3` | 216 | 5,724 | 26,811 |
| `L=4` | 576 | 24,480 | 148,800 |
| `L=5` | 1,200 | 75,000 | 565,125 |

The last column counts the Jordan–Wigner prefix qubits entering the two odd
endpoint operators used in Farrelly–Short equation `G.4`.  Dividing by
`N_c^2` gives `36.78, 36.33, 36.17`, matching their Appendix-G statement that
parity-flag preparation costs `O(N^2)` two-qubit operations.  The same
appendix states that preparing a physical fermion costs `O(N)` steps.  Those
are efficient simulation procedures, but they are a global parity service,
not a bounded-radius physical compiler.

Changing the order does not close the literal construction.  If the two
auxiliary endpoints of every link are made consecutive, `wt(M_e)=2`, but the
dressed update weights become `112,292,604` at `L=3,4,5`.  The string has been
moved back into the update because `a_x m_(x,y)` is no longer site-local.

Therefore Route 5 passes constant overhead, all-size sector capacity, local
runtime evolution, mass, contact, seam, and ideal leakage.  It fails locally
enforced link constraints, bounded local preparation, no global ordering
service, and full qubit-level proper-cubic covariance.  It does not pass the
compiler contract.  No axiom conclusion follows.

## Exact fixture instantiation

### Modes and lawful code

Use a site-major Jordan–Wigner order.  Each coarse cell block contains:

```text
matter modes a=0,...,5,
auxiliary endpoint modes c_(x,a), a=0,...,5.
```

The three canonical positive-axis links per cell use `c_(x,+a)` and
`c_(x+e_a,-a)`.  The Cycle-230 `B` FSWAP on that bond acts on matter ports
`(x,-a)` and `(x+e_a,+a)`.  The `A` layer is the three onsite opposite-port
FSWAPs.  The coin and contact act only on the six matter modes.

There are `12 N_c` qubits and `3 N_c` disjoint auxiliary links.  The `M_e=+1`
and `P_aux,e=-1` conditions have independent total rank `6 N_c`, leaving
`6 N_c` logical qubits.  Actual site-major Pauli checks give:

| `L` | Physical qubits | Links | Constraint rank | Logical matter qubits |
|---:|---:|---:|---:|---:|
| 3 | 324 | 81 | 162 | 162 |
| 4 | 768 | 192 | 384 | 384 |
| 5 | 1,500 | 375 | 750 | 750 |

All stabilizers commute, every dependent relation has phase `+I`, and neither
matter parity is projected out.  Vacuum, one-particle, and rank-73 sea sectors
all occur for `L=3,4,5`.  Unlike the Cycle-232 scalar-reference attempt, there
is no odd/even volume split.

The exact link isometry used by the dense check is

```text
E_e |psi> = K_e |psi> tensor |00>_aux,
K_e = (c_(x,y)^dagger - i c_(y,x)^dagger)/sqrt(2).
```

It satisfies `M_e E_e=E_e` and `P_aux,e E_e=-E_e`.  The globally ordered
product of all `K_e` gives `E_global`.  Because every `K_e` is fermion-odd,
its qubit implementation carries the global Jordan–Wigner parity prefixes
audited above.  Merely drawing each pair on a local spatial bond does not make
their globally ordered product a local qubit isometry.

### Bounded update and deletion controls

Each dressed cross-cell Majorana monomial has the form

```text
gamma_(a_x,s) M_e gamma_(b_y,t),  s,t in {0,1}.
```

The runner expands all four components on every link and every axis at
`L=3,4,5`.  Every support lies in the two endpoint cell blocks and has maximum
Pauli weight 14, independent of `L`.  Deleting `M_e` restores the bare
Jordan–Wigner hopping strings, whose maximum weights are `218,578,1202`.

The `M_e=-1` sector does not reproduce the coarse swap; its nonidentity
residual is `4.0`.  Thus deleting the lawful-sector condition is a real
falsifier, not a redundant presentation change.  All dressed generators
commute with every auxiliary link constraint, so ideal leakage is zero.

At `g=0`, the contact is exactly identity.  Auxiliary modes remain inert under
the coin, onsite `A`, and contact gates.  The construction neither calls a
wrapped phase physical energy nor calls a Hermitian generator a rate.

## Proper-cubic covariance

The abstract matter-plus-auxiliary link graph is exactly preserved by all 24
proper-cubic frames.  Port orientation signs can be repaired by a bounded
endpoint convention.  The Cycle-219 coin has frame residual zero, the contact
is permutation invariant, and the dressed `B` link family maps as a set.

The qubit constraint surface does not share that covariance.  A frame
permutation maps the site-major string between two spatial neighbors to a
different set from the site-major string assigned to the rotated link.  Even
ignoring the removable endpoint phase, the runner finds:

| `L` | Graph failures | JW constraint mismatches | Maximum support symmetric difference |
|---:|---:|---:|---:|
| 3 | 0 | 1,764 | 230 |
| 4 | 0 | 4,196 | 650 |
| 5 | 0 | 8,210 | 1,358 |

The growing symmetric difference cannot be called a bounded local port-gauge
repair.  It is another manifestation of the supplied global Jordan–Wigner
order.  Thus the runtime fermionic/link law is cubic, but the complete qubit
encoding and constraint declaration is not covariant under the required
bounded local meaning.

## Physical `M_2` placement and translation marker

Use physical macro spacing eight, with direction vectors `D_a`, and place

```text
matter mode (x,a):       8x - 2 D_a,       six-site orbit,
aux endpoint (x,a):      8x + 3 D_a,       six-site orbit,
supplied block marker:   8x,               one site.
```

This uses **12 data M2 carriers plus one supplied marker per coarse cell**.
Every active carrier is one `M_2(C)` site.  The offset set is invariant under
all 24 frames.  The two auxiliary endpoints on a coarse link are two physical
nearest-neighbor steps apart; the matter endpoints are four steps apart.
Onsite and dressed-link routing therefore has constant physical diameter.

Finite periodic patches contain exactly `13 L^3` active-plus-marker sites:
`351,832,1625` at `L=3,4,5`.  A unit physical translation changes `22 L^3`
active positions: `594,1408,2750`.  The marker set alone changes at `2 L^3`.
The layout is period eight, not a unit-translation theorem.  The location and
preparation of the period-eight marker pattern remain supplied; no host-side
schedule reads the marker during evolution.

The macro routing and gate coloring are supplied spatial-QCA law structure.
They are not a clock, physical elapsed time, a rate, or realized history.

## Mass, sea, contact, and seam

The auxiliary link state is inert under all matter observables.  Consequently
the conditional global isometry preserves matter matrix elements exactly.
The runner verifies:

- all `L=3,4,5` matter parity sectors;
- rank-73 principal-sea availability with the 81-link `L=3` auxiliary state;
- held-out `beta=-0.35` mass residual `3.68005641515623e-08`;
- contact identity on `N<=1` and exact deletion at `g=0`;
- Cycle-230 seam singular values `0.49577141,0.45566605`;
- direct `1/L^3` seam residual `7.163369603754572e-18`;
- all-24 seam covariance residual `1.2947314098277875e-15`; and
- zero ideal constraint leakage.

These are conditional algebraic equalities.  They do not make `E_global`
bounded-local.

## Supplied-structure inventory

The construction supplies:

1. six auxiliary complex fermion modes per coarse cell;
2. one oriented Majorana pair and one odd-parity state per coarse link;
3. a site-major global Jordan–Wigner order;
4. the Appendix-G global parity-flag preparation;
5. a fixed ordering of the fermion-odd `K_e` preparation factors;
6. the dressed FSWAP logarithm and gate schedule;
7. the spacing-eight 12-data-site layout, blanks, routing, and period-eight
   marker pattern;
8. local endpoint phase conventions under cubic frames; and
9. the Cycle-219 coin, Cycle-230 contact, coupling, gate order, and sea.

No runtime gate queries global matter parity.  The preparation does query and
transport Jordan–Wigner prefix parity.  This distinction is explicit.

## Prior work and novelty boundary

The construction class is not new.  T. C. Farrelly and A. J. Short,
“Causal Fermions in Discrete Space-Time,” *Physical Review A* **89**, 012302
(2014), <https://doi.org/10.1103/PhysRevA.89.012302> and
<https://arxiv.org/abs/1303.4652>, provide:

- the causal-fermion-to-qubit-QCA subsector theorem;
- auxiliary-Majorana string cancellation in equations `III.12–III.14`;
- the explicit link construction in equations `D.2–D.6`; and
- the parity-flag preparation and `O(N^2)` bound in Appendix G.

Farrelly–Short do not claim that their Appendix-G initialization is a
bounded-depth local state encoding.  Calling that a defect relative to this
tournament is a stronger fixture requirement, not a criticism of their
theorem.

The fixture-specific contribution is the explicit six-port cubic link
assignment, dressed Cycle-230 FSWAP, all-size code ranks, exact update
intertwining, support-scaling and ordering-tradeoff controls, 24-frame
constraint audit, physical coordinates, marker accounting, and retained
mass/contact/seam tests.  Global priority is not claimed.  Thirring machinery
is neither used nor compared.

## TOE dependency ledger after Route 5

| Workstream | Route-5 effect | Remaining content |
|---|---|---|
| `C_ref` | unchanged | physical phase origin, sea, and preparation remain unselected |
| `C_num` | all-size sector capacity gain | both matter parities are present, but auxiliary link-state preparation is globally ordered |
| `C_wrap` | unchanged | no link bit, marker, or schedule layer is a clock or winding carrier |
| `C_int` | bounded representation gain | the supplied contact is carried exactly; interaction selection and rate/protection remain open |
| `C_local` | materially narrowed, still open | bounded all-size update gates exist, but bounded local constraints, `E`, cubic qubit covariance, and marker selection fail |
| `C_source` | unchanged | no physical energy/stress/source ledger is selected |

The evidence does not change the 0–5 TOE scores: operational quantum/records
`2`, time `1`, inertia/matter `3`, gravity/source `2`, Born/probability `1`.
This is substrate compatibility evidence, not Record formation, time, source,
or probability.

## No-go discipline gate

No route-independent compiler impossibility, minimum overhead, or axiom
pressure is claimed.  The current `origin/main` no-go discipline was applied.

**N1–N8 result:** **PASS for the literal Farrelly–Short site-major
instantiation, its exact bounded update representation, and its exact
constraint/preparation/order tradeoff.  FAIL for a general auxiliary-fermion
no-go, a general `M_64 -> M_2` compiler no-go, minimality, uniqueness, or axiom
pressure.**

### N1 — alternative routes

| Route | Marker | Disposition |
|---|---|---|
| site-major Farrelly–Short cancellation | **ATTEMPTED** | update weight 14 for all sizes; link constraints and Appendix-G preparation grow |
| link-major auxiliary ordering | **ATTEMPTED** | makes `M_e` weight 2 but dressed update weights grow `112,292,604` |
| scalar-reference BKSF | **ATTEMPTED** | bounded update architecture, but bounded `E` contradiction and even-size failure |
| exact 3D higher-form bosonization | **LIVE, NOT RULED OUT** | may replace JW strings by local Gauss-law data; fixture not instantiated |
| generalized superfast/different edge code | **LIVE, NOT RULED OUT** | may give local constraints and all-size parity; not exhausted |
| alternate local stabilizer presentation of the FS state | **LIVE, NOT RULED OUT** | no bounded generating set or preparation was found; absence is not proved |

At least three live alternatives defeat every route-independent negative or
minimum-content inference.

### N2 — condition independence

The raw conditions collapse to two:

- `K_JW`: the same site-major global order makes dressed updates local while
  making `M_e`, preparation, and qubit covariance nonlocal; and
- `K_marker`: the physical macro-layout and period-eight marker selection.

Preparation and frame mismatch are consequences of `K_JW`, not inflated into
independent constitutional walls.  `K_marker` does not fix the string order;
`K_JW` does not select a physical block origin.  The two conditions are
independent and neither is called axiom content.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `K_JW`, `K_marker` | no | no | yes |

### N3 — hidden-condition scan

The mandatory scan for “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,” “obviously,”
“standard QFT,” “registered,” and “canonical” promotes no hidden condition.

The global mode order, link orientation, odd link parity, preparation-factor
order, parity flags, gate logarithm, macro blanks, marker, routing, coin,
contact, sea, and gate order are all inventoried.  No compiler substep is
renamed physical time.

| Scan hit | Classification |
|---|---|
| “construction” | descriptive label; the load-bearing choices are in the supplied inventory |
| “canonical positive-axis links” | finite presentation convention; all 24 frames are tested and the JW failure is retained |
| “global priority” | novelty qualifier, not a physical premise |
| “background,” “naturally,” “obviously,” “standard QFT” | no load-bearing use |

### N4 — residual matching

| Witness | Residual | Route-5 match |
|---|---|---|
| Cycle 230 physical `M_2` compiler absent | intrinsic CAR update needs bounded qubit realization | builds bounded update gates but not bounded `E` or constraints; partial |
| Cycle 234 auxiliary-Majorana route live | primary mechanism not fixture-instantiated | executes exact cubic link construction on `L=3,4,5`; yes |
| Farrelly–Short III.12–III.14 | `a_x b_y -> a_x M_xy b_y` on `M=+1` | dense FSWAP residual `3.21e-16`; yes |
| Farrelly–Short Appendix G | preparation uses parity flags and `O(N^2)` gates | prefix touches scale about `36 N_c^2`; yes |
| minimal physical site is `M_2(C)` | each active carrier must be one qubit | 12 data carriers plus one supplied marker per cell; interface only |
| Cycle-230 seam | local contact block must survive | exact inherited block and all-24 residual; yes |

No cited result is used for a uniqueness, lower bound, or general
impossibility claim.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| one dressed link | exact dense isometry, constraints, leakage, deletion | fault tolerance |
| every `B` link on `L=3,4,5` | maximum update weight 14, endpoint support | infinite-volume representation theorem |
| whole auxiliary code | exact rank and both matter parities | bounded local preparation |
| site-major `M_e` | exact JW Pauli support scaling | impossibility of another stabilizer generating set |
| Appendix-G preparation | exact prefix-touch scaling and primary-source circuit | lower bound on every preparation algorithm |
| link-major order | exact update-string recurrence | every possible hybrid ordering |
| all 24 frames | abstract graph and coin/contact pass; JW constraints fail | a different local gauge encoding |
| physical layout | 13 sites/cell, routing distances, marker differences | autonomous marker dynamics |
| mass and seam | retained fixture residuals | dressed interacting mass or selected vacuum |
| physical time | not tested | clock, metric, winding, or rate |

The negative is therefore only: **this literal auxiliary-Majorana/JW compiler
does not meet the bounded local constraint and preparation contract.**

### N6 — partial-closure and primitive scan

The fresh no-go skill and primitive-registry check were followed.  Scale
reference supplies units only, kinetic isotropy supplies only the form
`c_t=c_s`, and realized state supplies only a pointwise evaluation slot.  None
selects the auxiliary graph, Jordan–Wigner order, link state, preparation,
marker, coin, or contact.

Live partial-closure paths are:

| Path | Status | Possible effect |
|---|---|---|
| local Gauss-law/higher-form bosonization | primary-source live | replace JW link strings by bounded gauge constraints |
| bounded local generators for the FS auxiliary state | unbuilt | retain the update construction while repairing preparation |
| hybrid block/link ordering with local gauge ancillas | unbuilt | cancel both update and constraint strings |
| derive marker/layout from admissibility | unbuilt | retire the period-eight supplied origin |
| infinite-volume graded representation | unbuilt | reframe finite JW preparation without claiming an `M_2` compiler |

These are constructive routes, not proposed premises.

### N7 — steelman

> Farrelly and Short prove an efficient finite-overhead qubit-QCA simulation,
> not constant-depth initialization.  Their Appendix G explicitly permits
> `O(N^2)` state preparation, so the runner confirms rather than refutes their
> theorem.  The update cancellation is exact and works at every tested size,
> unlike the scalar-reference repair.  A different local stabilizer generating
> set, higher-form gauge presentation, or hybrid ordering might prepare the
> same auxiliary sector locally.  Therefore the result is a sharp failure of
> one JW realization under a stronger compiler contract, not a no-go for
> auxiliary fermions or for physical qubit compilers.

That steelman is convincing.  It preserves the constructive update result and
blocks any route-independent obstruction or axiom-pressure claim.

### N8 — cross-cycle echo

The prescribed repository phrase search and the walk of every
`.claude/science/physics-loops/**/NO_GO_LEDGER.md` were rerun after confirming
that the local no-go skill and `origin/main` copies have identical SHA-256
hashes.  No retired convention-only wall supplies a local fermion-to-qubit
state encoding here.

| Earlier boundary | New mechanism | Effect here |
|---|---|---|
| Cycle 229 spectral JW is not a spatial compiler | auxiliary Majoranas cancel update strings | update locality closes, encoding locality does not |
| Cycle 232 bounded gauge updates but nonlocal sectorwise `E` | all-size link state replaces parity bus | parity-size failure retires; global preparation remains |
| Cycle 234 auxiliary route left live | exact primary-source fixture instantiation | route-specific boundary is now executable |
| prior macro-origin warning | explicit period-eight marker audit | marker remains supplied, not hidden |
| earlier winding/phase work | link state and JW parity are not time | `C_wrap` remains unchanged |

The recurrence is a dependency distinction: local evolution does not imply a
local state encoding.  It is not a shared substrate obstruction because live
gauge/bosonization and alternative-stabilizer routes remain.

## Route disposition and next discriminator

**Route-5 disposition:** retain the exact all-size bounded update-gate
architecture, code-rank result, and physical placement.  Reject it as a full
compiler because its literal lawful constraints, state encoding/preparation,
and qubit covariance use size-growing global Jordan–Wigner structure.

The next discriminator is a local Gauss-law or alternate stabilizer
presentation of the same six-mode cubic update.  It must retain the Route-5
all-size parity coverage and weight-14 update bound while replacing every
`M_e` string and Appendix-G parity flag by bounded physical constraints and a
bounded-radius preparation.  It must be tested on `L=3,4,5`, all 24 frames,
and the same marker audit.

`C_local` is materially narrowed but not closed.  There is no shared
obstruction and no axiom pressure.  No axiom conclusion follows.

## Verification

```text
python3 scripts/FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_2026_07_17.py
```
