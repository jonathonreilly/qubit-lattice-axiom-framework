# Physical L41 local streaming/reuse tournament — Cycle 584

Date: 2026-07-22

Authority: none

Audit: unset

Authority remains none. Audit remains unset. This cycle changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, audit status,
or PR control surface.

Runner:

`scripts/physical_l41_local_streaming_reuse_tournament_cycle584_2026_07_22.py`

## Result up front

Route A closes the literal finite-`H=3` layout residual left by Cycle 582. It
embeds the 42-M2 quantum factor, eleven-rail phase head, and three-rail cursor
into a 56-site proper-cubic line. A cursor-dependent packet permutation puts
the selected 12-M2 packet at a fixed station. Controlled-H, Toffoli, Fredkin,
and controlled-CZ identities expand the Cycle-580 gates, packet rotation,
cursor increment, and phase increment into 740 one-/two-M2 primitives. Routing
each primitive out and back yields one fixed manifest of 14,320 explicit
nearest-neighbor two-M2 gates, including 13,580 routing SWAPs.

The compilation alphabet is broader than Cycle 580's H/CNOT/CZ/SWAP list.
The 15-call Toffoli identity uses the supplied T/T† phase gate
`diag(1,e^{±iπ/4})`, embedded physically as `T tensor I` or
`T† tensor I` on an adjacent spectator. The exact two-M2 controlled-H matrix
is also supplied and is not decomposed further. Thus the positive result is an
arbitrary-two-M2-gate compiler with these local matrices admitted, not a
derivation using only the Cycle-580 elementary alphabet. Their physical
derivation or import retirement remains open.

On the declared controller code, all 33 phase/cursor rows satisfy

```text
E G_coarse = G_physical E
```

with maximum residual zero. Two complete routed basis witnesses, one crossing
the packet/cursor wrap and one activating the controlled H, differ from the
direct physical law by `7.669733616450728e-15` and
`7.301383309274022e-15`. Every routed wire certificate passes. The circuit is
a full-space unitary: on off-code bitstrings it applies the same ordered list,
so multiple occupied phase rails activate multiple controlled macros before
the rails are permuted. No refusal or host-selected phase/cursor branch is
hidden in that rule.

This is exact finite-H3 compilation, not uniform arbitrary-H closure. Its
serial manifest has depth 14,320 and a 56-site finite routing diameter. The
exactly-one phase/cursor constraints and controller genesis remain supplied;
an explicit separated two-head word passes adjacent hard-core checks, so such
checks do not enforce the declared controller code.

Route B gives a finite-corridor translation-invariant streaming-QCA candidate.
Each 31-M2 macrocell has six station-system M2, one program marker, and two
12-M2 packet buffers `A,B`. The bulk law is the same at every cell: apply the
marker-controlled Cycle-580 scatter, swap `A_i <-> B_i`, then swap
`B_i <-> A_(i+1)`. The two SWAP layers translate packets by one macrocell and
return all `B` buffers blank. Quantum train `N=2` and held `N=3` rows reproduce
the direct recurrence with zero residual; the inverse residual is
`9.42055475210265e-16`, a deleted cross-lane SWAP changes the state by
`2.82842712474619`, and first reentry changes the reused packet archive by
`0.5077524002897471`.

The bulk rule is translation invariant; the finite periodic corridor state is
not. Its supplied cut, `A` packet preparation, blank `B` buffers, one station
marker, and finite low-entropy capacity are boundary data. Lengths `2..17`
pass symbolic shift, full inverse, deletion, and macrocell collision tests,
and the two-layer permutation identity is valid for every integer `N>=2`.
This does not produce an infinite stationary state or a resource-balance law.

Route C finds a different positive answer to the Cycle-582 reset probes. Pair
each of the 18 active output M2 with one M2 of a fresh fixed blank block and
apply 18 parallel SWAPs. The named active role becomes the exact blank while
the neighboring block receives the entire 18-M2 output. State residual and
inverse residual are zero; archive-output and active-blank density residuals
are `4.440892098500626e-16` and `9.992007221626409e-16`. Symbolic conjugation of
all 36 single-site `X_i,Z_i` generators shows that the full output algebra,
not only a pointer word, is transported faithfully and independently.

This is role reset by export. It consumes one fresh 18-M2 blank and produces
one spent 18-M2 archive per invocation. The active *role* is reusable, but no
catalyst is returned and no low-entropy resource is regenerated. Finite
archive conservation is not renewal. Boundary-supplied preparation is not
thermodynamics. Neither result is a temperature, entropy-production, work,
energy, stress, source, backreaction, or gravity law.

Program phase is not time, duration, lapse, or rate. Exported conditional
output is not a framework Record or actual branch. Candidate traces are not
derived Born probabilities. No shared obstruction or axiom pressure is
claimed. Exact contract phrase: no axiom pressure.

## Exact target contract

| field | Cycle-584 contract |
|---|---|
| target statement | compile Cycle-582 H3 controller/conveyor locally; probe a uniform finite streaming law; probe faithful archive-preserving role reset |
| quantifiers/domain | all 11 phase values and all 3 cursor values; the full 42-M2 quantum factor by exact circuit identity and linearity; quantum corridors N2/N3; symbolic packet corridors every `N>=2`; the full 18-M2 output algebra for Route C |
| allowed premises | exact-pinned Cycles 580/582, Cycle-563 mass receipt, finite pure packets/blanks, finite noiseless gates including supplied `T/T† = diag(1,e^{±iπ/4})` and exact two-M2 controlled-H matrices, declared controller/marker code, proper-cubic presentation |
| forbidden weakenings | no host phase/cursor choice, nonlocal parity service, global Jordan-Wigner order, hidden discard, Record/Born/time/energy/source relabeling, or finite-stock renewal claim |
| required controls | full-space unitarity/off-code rule, inverse, deletion, leakage/identity, boundary/capacity, controller enforcement/genesis audit, mass fixture, all24 geometry, supplied/derived/open inventory |
| completion witness | exact EG plus an explicit two-M2 NN manifest for A; exact uniform scatter/shift and N-parametric permutation proof for B; algebra-faithful block-SWAP and debit for C |
| outcomes not counting as global closure | finite-H3 routing, finite periodic stock, a supplied marker, named-role reset that consumes a fresh block, or route-specific failure |

## Dependency and mass fixture control

Cycle 584 exact-pins:

- Cycle-580 runner, note, and parent receipt;
- Cycle-582 runner, parent-augmented note/receipt, and frozen transcript; and
- the Cycle-563 parent receipt.

The Cycle-580 receipt transitively validates its frozen transcript, parent
`10/10`, and authority/audit boundary. The Cycle-582 transcript reports `7/7`,
and its note contains the parent transcript hash and the explicit
simultaneous-independent-readability scope of the earlier rank-32 bound.

The Cycle-563 receipt retains the Cycle-219 one-particle mass-fixture residual
`8.7159799596118e-16`. Cycle 584 does not rederive or refit that fixture; exact
intertwining leaves the pinned coarse target unchanged. “Mass fixture
preserved” here means dependency and map preservation, not a new matter or
inertia derivation.

## Route A — literal H3 two-M2 controller/conveyor compiler

Let `R_c` rotate the three coarse resource packets so packet `c` occupies the
physical station. For coarse quantum state `psi`, phase `p`, and cursor `c`,
define

```text
E |psi,p,c> = |R_c psi> tensor |e_p>_H11 tensor |e_c>_H3.
```

For `p<10`, the physical law applies the Cycle-580 layer selected by `e_p` at
the station and increments only the phase head. At `p=10`, it additionally
left-rotates all three physical packets and increments the cursor. Therefore
the station again contains the next coarse packet and the result equals
`E G_coarse`. The proof uses packet permutations and controlled gate identities
and hence acts on the full `2^42` quantum factor; that square matrix is not
materialized. The 33 reported rows exercise the exact supplied preparation and
every lawful controller coordinate.

### Primitive expansion and routing

The exact local identities are:

| identity | calls | residual |
|---|---:|---:|
| Toffoli | 15 | `7.346882794269506e-16` |
| Fredkin = CNOT / Toffoli / CNOT | 17 | `7.346882794269506e-16` |
| controlled-CZ = H / Toffoli / H | 17 | `1.1335532999722767e-15` |
| supplied controlled-H unitarity | one two-M2 gate | `3.1560822113208575e-16` |

The Toffoli rows use four supplied `T` and three supplied `T†` calls together
with inherited H/CNOT calls. These phase matrices introduce the exact angle
`π/4`; Cycle 580 did not derive or inventory that angle. The physical gate
alphabet of the routed manifest is therefore

```text
CNOT, SWAP, H tensor I, T tensor I, T† tensor I, controlled-H.
```

This inventory is load-bearing. Exact matrix reconstruction proves the
compiler conditional on that alphabet; it does not prove the alphabet follows
from the retained M2 substrate.

Deleting the first Toffoli call changes that unitary by `4`. Every one-M2 call
is represented as `U tensor I` on an adjacent spectator M2. For a nonadjacent
two-M2 call, the right operand is moved next to the left operand by adjacent
SWAPs, the ordered gate is applied, and the SWAPs are reversed. A symbolic
wire certificate checks the operand order at the middle gate and restoration
of every wire after each of the 740 primitive routes.

The final manifest contains:

| item | count |
|---|---:|
| controlled Cycle-580 gate macros | 20 |
| packet-conveyor Fredkins | 24 |
| cursor-increment Fredkins | 2 |
| phase-increment SWAPs | 10 |
| expanded primitives | 740 |
| routed nearest-neighbor two-M2 gates | 14,320 |
| routing SWAPs | 13,580 |

Its SHA-256 is
`9a632c499c6f602678efb9f4161b437edf992c586f5d12afdf07b1082511521c`.
Maximum local unitarity residual is `4.463374267214424e-16`; adjacency,
routing-certificate, and all24 edge/collision failures are zero.

### Covariance and controller boundary

For every proper-cubic frame `F`, the covariance action is

```text
(x,0,0) -> F (x,0,0)
```

on all 56 sites, with the same internal two-M2 matrix on each rotated edge.
There are 343,680 rotated edge tests. This is one complete covariant line
embedding per frame. It is not one simultaneously isotropic occupied volume,
nor a continuum or Lorentz-covariance result.

The H11/H3 one-excitation code is preserved on lawful rows, but neither its
genesis nor local exactly-one enforcement is derived. In particular,
`10100000000` contains two separated heads and violates no adjacent hard-core
constraint. A full-space unitary prevents an undefined off-code action; it
does not turn off-code states into lawful ones. Noise repair and thresholds
remain open.

Route-A disposition: **exact literal finite-H3 physical-site compiler**. It
does not close uniform arbitrary-H gate count, depth, causal radius, local
controller enforcement, or controller genesis.

## Route B — finite streaming-QCA candidate

Each cell has

```text
S_i(6 M2), marker_i(1 M2), A_i(12 M2), B_i(12 M2).
```

The same marker-controlled Cycle-580 full-space scatter is installed at every
cell. Relabeling Route A's phase control as the local marker gives the same
controlled-H/Toffoli/Fredkin two-M2 compiler inside the 31-M2 macrocell. The
transport portion is

```text
layer 1: SWAP(A_i[lane], B_i[lane])          for every i,lane
layer 2: SWAP(B_i[lane], A_(i+1)[lane])      for every i,lane.
```

For arbitrary distinct packet labels `P_i` and blank labels `Z_i`, this maps

```text
A_i -> P_(i-1),    B_i -> Z_(i+1).
```

Thus identical zero `B` states return blank, while their formal labels undergo
a reversible permutation. Reversing layer 2 and then layer 1 recovers every
distinct `P_i,Z_i`. Both layers are collision-free at the declared macrocell
level. The proof is N-parametric; explicit rows `N=2..17` test it, its inverse,
and a deleted cross-edge.

The quantum quotient omits known-zero spectator systems and markers away from
the single station. It runs the exact Cycle-580 scatter at that marked cell
and both packet layers. Results are:

| control | result |
|---|---:|
| N2/N3 EG maximum | `0` |
| one-step inverse maximum | `9.42055475210265e-16` |
| deleted cross-lane residual | `2.82842712474619` |
| first held overrun global change | `3.937003937005905` |
| reentered packet archive change | `0.5077524002897471` |
| symbolic shift/inverse/deletion/collision failures | `0/0/0/0` |

Each packet lane occupies a cubic `C_(2N)` perimeter with alternating `A_i,B_i`
sites. Twelve lanes are disjoint. Train/held layouts yield 2,880 all24 edge
tests with zero edge or collision failures.

The law is translation invariant in the bulk. The finite periodic state has a
supplied station marker, a supplied cut, pure fresh `A` packets, blank `B`
buffers, and capacity `N`. At the `(N+1)`th encounter the first spent packet
reenters. Boundary-supplied inflow is not autonomous preparation, an infinite
stationary state, renewal, or resource thermodynamics. The marker does not
create an actual branch or clock time.

Route-B disposition: **positive finite-corridor, arbitrary-length transport
law with train/held quantum scatter**. Infinite-state existence, marker
genesis/enforcement, boundary physics, and stationary resource balance remain
open.

## Route C — role reset by full-output export

Let `V psi` be the full 18-M2 Cycle-580 output and let `b` be a fixed 18-M2
blank consisting of encoded-plus system, encoded-plus reset environment, and
zero pointer/dephasing carriers. Interleave the active and fresh blocks on
proper-cubic edges and apply

```text
S_block = product_(i=0)^17 SWAP(active_i, fresh_i).
```

Then exactly

```text
S_block (V psi tensor b) = b tensor V psi.
```

The 18 SWAPs have parallel depth one in the declared interleaved layout.
Deleting the first pair SWAP changes the state by `2.82842712474619`; applying
the block SWAP twice returns the input with residual zero.

For every operator `O` on the full active block,

```text
S_block (O tensor I) S_block^dagger = I tensor O.
```

The runner tracks all 36 Pauli generators through the actual pair permutation
with zero mapping failures. Because those generators generate the full matrix
algebra, this is a faithful independent output-algebra transfer, not a
four-label compression and not an invocation of Cycle 582's contract-scoped
rank bound.

The exact resource ledger is:

| invocations | fresh blank M2 consumed | spent archive M2 retained | named active blocks returned blank |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 18 | 18 | 1 |
| 2 | 36 | 36 | 2 |
| 3 | 54 | 54 | 3 |

This is not catalytic reuse: the fresh block does not return. It is exact role
reset by outward export. Arbitrary new system input would also require its own
preparation; only the fixed blank is returned here. The result defeats a broad
“faithful output always prevents named carrier reset” statement, but it does
not solve fresh-resource balance.

Route-C disposition: **positive faithful full-output export and exact named-
role reset at 18 fresh M2 per event**. Teleportation, a returned catalyst, and
low-entropy regeneration remain untested.

## Route-by-route disposition

| route | strongest exact result | residual boundary |
|---|---|---|
| A | finite H3 56-M2 full-space unitary, 14,320 two-M2 NN gates, exact EG | controller enforcement/genesis; arbitrary-H depth/radius |
| B | uniform radius-one macrocell shift for every N>=2; N2/N3 quantum scatter | supplied finite state/cut/marker; no stationary boundary balance |
| C | full 18-M2 output algebra exported; named active block exactly blank | consumes 18 fresh M2/event; no catalyst or renewal |

No route-specific failure is constitutional evidence.

## Supplied / derived / open

### Supplied

1. exact Cycle-580 and Cycle-582 circuits, code domains, finite H3 packets, and
   conditional candidate-output semantics;
2. Cycle-563 mass receipt and the Cycle-580 base proper-cubic presentation;
3. pure encoded-plus/zero packets, fixed 18-M2 blanks, one-hot phase/cursor and
   station-marker states;
4. finite noiseless two-M2 gates, including a supplied exact controlled-H
   matrix and supplied one-M2 `T/T† = diag(1,e^{±iπ/4})` phases embedded as
   `T/T† tensor I` on an adjacent spectator;
5. ordered gate manifest, finite corridor cut, periodic capacity, and host
   invocation of the same fixed candidate law.

### Derived

1. exact finite-H3 `E G_coarse = G_physical E`, full-space off-code unitary,
   literal 56-site proper-cubic line, and explicit 14,320-gate two-M2 NN list;
2. exact controlled-gate identities, routing certificates, routed witnesses,
   deletion, and all24 finite-layout checks;
3. a translation-invariant bulk scatter/shift candidate, quantum N2/N3 rows,
   arbitrary-N packet-permutation identity, inverse, deletion, collision,
   boundary, and capacity controls;
4. exact 18-pair full-output-algebra export, named-role blank return, deletion,
   inverse, and fresh/spent debit;
5. unchanged exact-pinned one-particle mass fixture.

### Open

1. local exactly-one controller and station-marker enforcement, genesis,
   repair, noise threshold, and lawful-state preparation;
2. uniform arbitrary-H microscopic gate count/depth/radius and a full infinite
   quasi-local QCA state;
3. derivation or import retirement of the supplied `π/4` phase and
   controlled-H matrices from a physical M2 local-gate family;
4. stationary fresh/spent balance, low-entropy regeneration, renewal, entropy,
   temperature, work, energy, stress, source, backreaction, or gravity;
5. a returned catalyst or coherent teleportation route with exact syndrome and
   resource ledgers;
6. active interacting-matter dynamics beyond exact preservation of the pinned
   mass fixture;
7. actual occurrence, branch selection, framework Record, realized history,
   derived Born/frequency law, or physical time.

## TOE dependency ledger and maturity coordinates

| wall | Cycle-584 movement | remaining dependency |
|---|---|---|
| `C_ref` | fixed manifest plus in-state phase/cursor removes host branch selection at finite H3; TI bulk scatter is state-driven by marker | controller/marker preparation and genesis supplied |
| `C_num` | 33 EG rows, 14,320-gate manifest, N2/N3 quantum corridors, arbitrary-N transport proof, and exact algebra export | finite sparse/routed witnesses; no arbitrary-volume noise theorem |
| `C_wrap` | complete output algebra has an explicit independent archive owner | no actual branch, framework Record, permanence, or realized history |
| `C_int` | one-particle mass fixture is exact-pinned and unchanged | active interacting-matter composition not advanced |
| `C_local` | finite H3 literal two-M2 NN compiler and radius-one macrocell transport constructed | arbitrary-H microscopic causal depth, controller enforcement, and derivation/retirement of supplied `π/4` and controlled-H matrices open |
| `C_source` | fresh/spent debits are exact for packet flow and 18-M2 export | no renewal, thermodynamics, energy/stress/source, backreaction, or gravity law |

Global evidence coordinates remain unchanged because the results close finite
compiler/resource mechanisms rather than the semantic or dynamical lane ends:

| lane | repo-wide evidence | strict-M2 evidence | Cycle-584 delta |
|---|---:|---:|---|
| operational quantum / Records | `96/100 (4.80/5)` | `93/100 (4.65/5)` | literal recurrence compiler and faithful output algebra; actuality unchanged |
| causal time | `79/100 (3.95/5)` | `76/100 (3.80/5)` | spatial program/shift order only; no physical time |
| inertia / matter | `94/100 (4.70/5)` | `97/100 (4.85/5)` | pinned mass fixture preserved; no new active matter law |
| gravity / source | `82/100 (4.10/5)` | `77/100 (3.85/5)` | exact finite debits only; no source response |
| Born / probability | `84/100 (4.20/5)` | `73/100 (3.65/5)` | conditional output algebra retained; no probability derivation |

These coordinates are planning evidence, not probabilities, audit grades, or
constitutional status.

## No-Go Discipline gate

The latest `origin/main` no-go-discipline skill and proof-search governance
were read completely before this artifact was written. A broad recurrence,
renewal, archive-reset, minimum-content, shared-obstruction, or axiom-pressure
negative does not pass.

### N1 — normalized families

| family | object / invariant | terminal obligation | status |
|---|---|---|---|
| finite routed unary controller | H3 line; supplied-matrix controlled identities and reversible routing | local enforcement/genesis, uniform arbitrary-H causal depth, and derivation/retirement of the `π/4`/controlled-H alphabet | **ATTEMPTED — POSITIVE FINITE H3** |
| finite-corridor streaming QCA | marker-controlled scatter; doubled-buffer radius-one shift | infinite stationary state and autonomous resource balance | **ATTEMPTED — POSITIVE FINITE CORRIDOR** |
| full-block archive SWAP | algebra transport; fresh blank export | account for or regenerate blank archive stock | **ATTEMPTED — POSITIVE ROLE RESET** |
| coherent teleportation reuse | Bell resource, coherent syndrome, correction | local exact correction and Bell-resource ledger without actuality import | **UNTESTED / NOT COUNTED** |
| error-corrected catalytic workspace | encoded catalyst with outward syndrome/history | exact catalyst return and faithful resource balance | **UNTESTED / NOT COUNTED** |

Only three families qualify. N1 status: **FAIL**. The two untested families are
not misreported as ruled out.

### N2 — wall independence

The corrected residual set is:

- `W_E`: controller-code/marker enforcement and genesis;
- `W_Q`: uniform arbitrary-H depth plus stationary boundary state; and
- `W_R`: fresh low-entropy archive/reservoir balance; and
- `W_G`: derivation or retirement of the supplied `π/4` phase and controlled-H
  gate alphabet.

| pair | first closes second? | second closes first? | disposition |
|---|---|---|---|
| `W_E,W_Q` | no—valid local words do not prepare a stationary boundary or bound routing depth | no—a QCA shift does not create its marker/head | independent |
| `W_E,W_R` | no—enforcement does not regenerate blanks | no—resource balance does not create the program word | independent |
| `W_E,W_G` | no—enforcement supplies no phase angle or controlled-H law | no—a gate alphabet does not create the controller word | independent |
| `W_Q,W_R` | no—uniform flow may merely move finite stock | no—fresh balance supplies no controller/scatter compiler | independent |
| `W_Q,W_G` | no—uniform transport does not derive local compilation matrices | no—a gate alphabet does not prepare a stationary state or bound arbitrary-H routing | independent |
| `W_R,W_G` | no—resource balance does not derive the local matrices | no—the gate alphabet does not regenerate low-entropy blocks | independent |

No pair collapses.

### N3 — hidden-condition scan

The runner scans this note for the required hidden-premise phrases. Every
premise carrying load is in the Supplied inventory: pure packets/blanks,
one-hot heads/markers, gate order, finite cut/capacity, noiseless gates, and
law invocation. The `π/4` T/T† phases and exact two-M2 controlled-H matrix are
explicit supplied conditions, not hidden inside “Toffoli decomposition.” Any
prior-art wording is non-load-bearing attribution. No hidden condition is used
to close a wall.

### N4 — residual matching

| witness | witness residual | Cycle-584 use | match |
|---|---|---|---|
| `PHYSICAL_L41_AUTONOMOUS_RECURRENCE_RESOURCE_TOURNAMENT_CYCLE582_NOTE_2026-07-22.md:27` | code-coordinate H3 exact, literal controller/conveyor layout open at lines 29–32 and 141–160 | finite H3 literal routing closure only | yes |
| same note, line 166 | finite debit/conveyor, no stationary balance at lines 186–200 | finite uniform transport only; boundary balance remains open | yes |
| same note, line 202 | three copy/uncompute maps fail reset while swap/teleport/catalytic paths remain open at lines 208–234 | different full-block SWAP route | yes |
| `outputs/physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json:72` | Cycle-219 mass residual | exact target preserved, not rederived | yes |
| `PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md:182` | 18-M2 single-invocation base layout | recurrent 56-M2 controller layout | no; retained for base covariance, dropped as closure evidence |

Four witnesses match exactly. The Cycle-580 base layout is not counted as
evidence that the recurrent layout was already closed.

### N5 — rhetoric and resolution audit

Tested resolutions are: individual two-M2 gates and a complete finite-H3
manifest; N2/N3 quantum corridors and macrocell packet permutations for every
finite `N>=2`; and one 18-M2 full-block SWAP contract. Untested resolutions are
uniform arbitrary-H microscopic depth, an infinite stationary QCA state,
catalytic/teleportation reuse, resource thermodynamics, and derivation of the
supplied `π/4`/controlled-H alphabet from a physical M2 gate family. Every
negative is restricted to the named finite route or left unshipped.

### N6 — partial-closure paths

1. replace one-hot heads by a locally constrained domain-wall program with an
   explicit initialization front;
2. extend the finite-corridor automorphism to an infinite quasi-local algebra
   with a specified shift-invariant lawful state;
3. coherently teleport the returned blank while retaining syndrome and output
   algebras; and
4. derive a separate low-entropy preparation/export balance rather than
   relabeling a finite boundary stock; and
5. derive `π/4` phase and controlled-H matrices from a retained physical M2
   gate family, or retain them as bounded imports with an explicit retirement
   audit.

These are constructive import-retirement paths. None authorizes new axiom
language.

### N7 — hostile steelman

A translation-invariant, locally constrained domain-wall program QCA could
stream a shift-invariant encoded-plus reservoir through the exact Cycle-584
scatter, export spent packets on a second ray, and coherently correct a
catalytic station while preserving the full output algebra. Its terminal
obligation is an explicit two-M2 rule together with the lawful infinite state,
derived local gate matrices, controller genesis, catalyst return, and
arbitrary-volume collision/resource proofs. That mechanism is concrete and
untested, so broad negative claims are premature.

### N8 — cross-cycle echo

- Cycle 574 retired representation/readiness gaps by explicit encodings rather
  than constitutional change.
- Cycle 577's isometry-only gap was retired by Cycle 580's full-space circuit.
- Cycle 582's code-coordinate controller gap is narrowed here by literal H3
  routing.
- Cycle 44's protected block-SWAP showed that named carrier reuse can coexist
  with outward information export; Route C applies that mechanism to the full
  Cycle-580 output.

Constructive reopening remains mandatory.

Artifact status: **POSITIVE FINITE CONSTRUCTIONS WITH EXPLICIT RESOURCE AND
GENESIS RESIDUALS**.

Broad no-go: **FAIL / DO NOT SHIP**.

Minimum-content theorem: **FAIL / DO NOT SHIP**.

Shared-obstruction claim: **DO NOT SHIP**.

Axiom-pressure claim: **DO NOT SHIP**.

## Prior-art and novelty boundary

Unary program registers, reversible circuit iteration, controlled-gate
decomposition, SWAP routing, partitioned cellular automata, doubled-buffer
translation, and block-SWAP algebra transport are generic circuit/QCA methods.
The Clifford+T Toffoli identity and exact controlled-H matrix are circuit
prior art, but prior-art availability is not physical derivation: Cycle 584
supplies their local matrices and the exact `π/4` angle. No general novelty or
priority claim is made.

The repo-local result is the exact-pinned joining of the Cycle-580 instrument
and Cycle-582 controller to (i) one finite H3 literal two-M2 NN manifest, (ii)
one finite-corridor uniform transport law, and (iii) one faithful full-output
role-reset/export circuit, with controller genesis, arbitrary-H scaling,
gate-alphabet imports, boundary state, resource balance, matter,
occurrence/Record, Born, time, and source boundaries explicit.

## Cold verification

Frozen command:

```bash
/usr/bin/time -l python3 -u scripts/physical_l41_local_streaming_reuse_tournament_cycle584_2026_07_22.py
```

Frozen replacement receipt:

- runner SHA-256:
  `556e3e4759033706c795c9b65f55f12afaaaf84b8858dc4bb06b1c0a93400ab3`;
- transcript SHA-256:
  `76455ca1d04a9f6cef400268e83a5df7c25d37959f674c80cd2161cee85ca69f`;
- `RESULT pass=6 fail=0`;
- every Cycle-580/582 and Cycle-563 hash matches its exact pin; Cycle-580
  base all24 edge tests `816` and all576 role tests `6,336` remain validated,
  and the Cycle-219 mass-fixture residual remains
  `8.7159799596118e-16`;
- supplied compilation alphabet: `T` angle `0.7853981633974483` radians,
  T SHA-256
  `f9203f40d54bd38c70ed741465103c917e11691bf88ec6b5df6109d51becd49c`,
  T† SHA-256
  `e022459238788f401f6e594af09080583dc0060fd39752b7fa26eef2199cd2ca`,
  and controlled-H SHA-256
  `b2f6431af8c0fc10917ef921e524337b463f5eaeef4c72c7afa330f21f9613d2`;
  `compiler_uses_only_Cycle580_H_CNOT_CZ_SWAP_alphabet` is `false`;
- Route A: all 33 controller EG rows have maximum residual `0`; Toffoli,
  Fredkin, and controlled-CZ residuals are `7.346882794269506e-16`,
  `7.346882794269506e-16`, and `1.1335532999722767e-15`; 740 primitives
  compile to 14,320 two-M2 NN gates with 13,580 routing SWAPs; 740 wire
  certificates, 343,680 all24 edges, and all adjacency/collision tests have
  zero failures; routed wrap/H residuals are `7.669733616450728e-15` and
  `7.301383309274022e-15`;
- Route B: N2/N3 quantum EG maximum `0`, inverse maximum
  `9.42055475210265e-16`, deletion residual `2.82842712474619`, reentry
  archive change `0.5077524002897471`, N2..N17 symbolic
  shift/inverse/deletion/collision failures all `0`, and 2,880 all24 conveyor
  edge tests have zero failures;
- Route C: block-SWAP and inverse residuals `0`, deleted-pair residual
  `2.82842712474619`, archive-output density residual
  `4.440892098500626e-16`, active-blank density residual
  `9.992007221626409e-16`, and all 36 full-output-algebra Pauli generators map
  with zero failures; the debit is exactly 18 fresh M2 per event;
- N1 has three qualifying attempts against five required, so it is `FAIL`;
  N2 now includes the independent supplied-gate-alphabet wall; broad no-go,
  minimum-content, shared-obstruction, and axiom-pressure claims are all
  `DO_NOT_SHIP`;
- external elapsed `55.41 s`, maximum resident set size `243,662,848` bytes,
  peak memory footprint `238,502,512` bytes, and swaps `0`;
- internal scientific-section elapsed `55.2562189999735 s`, reported RSS
  `231,636,992` bytes;
- authority `none`; audit `unset`.

The run is below 360 seconds and 3 GiB. The transcript is frozen evidence;
this receipt-only note edit does not alter the runner or transcript.

Independent parent verification reran the frozen command and returned
`RESULT pass=6 fail=0` in `54.55 s` external wall time, with `244,416,512`
bytes maximum resident set, `238,715,480` bytes peak memory footprint, and
`0` swaps. The independent transcript SHA-256 is
`916194174ba5dde6b317e29dfa41b711bae16f73249d047959ef5535d74cd4c2`.
