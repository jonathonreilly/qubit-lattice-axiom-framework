# Cycle 610 — conditional proper-cubic coarse-grid stream placement

Date: 2026-07-22
Authority: none
Audit: unset
Author artifact status accepted: false
Breakthrough: false
Broad-negative gate: FAIL / DO NOT SHIP
Constitutional effect: none

## Corrected verdict

Cycle 610 preserves a large exact **conditional coarse-grid construction**.
Given a supplied `K=129` periodic partition/origin, structural role coloring,
and role orientation,
each `129^3 = 2,146,689`-site cell has explicit A/B storage, work, face-channel,
and bus coordinates. The coordinate word is bounded, support-one/two, and
nearest-neighbor relative to that supplied partition. The accepted factor order
is

```text
Cycle-230 coin -> Cycle-606 register stream -> Cycle-230 contact.
```

The previous promotion to a one-site translation-covariant physical M2 law is
false. The runner now directly reproduces the decisive code-space falsifier:

| L | split | tagged sites | overlap with +x unit translate | symmetric difference |
|---:|---|---:|---:|---:|
| 3 | train | 2,457 | 972 | 2,970 |
| 6 | held | 19,656 | 7,776 | 23,760 |
| 7 | held-out-size | 31,213 | 12,348 | 37,730 |

The declared persistent tagged motif contains 91 sites per supplied coarse
cell: 42 A/B word/equality roles, 24 orientation roles, 24 predicate-work
roles, and one onsite-work role. Only 36 roles per cell overlap the motif
translated by one fine site in x. The nonzero symmetric differences show that
the declared tagged code support is not invariant under a standard physical
unit translation. The earlier “translation” loops covered only 27, 216, and
343 coarse-cell displacements—physical displacements by multiples of 129 fine
sites.

Therefore this artifact is not a completed physical M2 compiler, not a physical
intertwiner, and not a one-fine-site translation-covariant law. It is a bounded
conditional placement with useful exact register and coordinate evidence.

## Promotion test contract

The runner byte-checks `docs/MINIMAL_AXIOMS_2026-06-29.md` against current
`origin/main`. Lines 37-41 state the test contract: physical sites form the
cubic `Z^3` lattice with nearest-neighbor adjacency, standard translations,
proper rotations about each site, and no privileged site. Those lines are used
only as a promotion contract. No axiom or foundation text is edited, and no new
dynamics is inferred from the contract.

The present 129-period motif fails the standard-translation/no-privileged-site
promotion test. This is route-specific narrowing, not a shared obstruction, so
no axiom pressure is established.

## Frozen dependency shore

The runner directly byte-pins the final accepted Cycle-606 quartet and the
final Cycle-603 quartet, plus the Cycle-230 seam runner/note. It reconstructs
and verifies the complete inherited transitive science graph and enumerates
the actual runtime science modules. Git status, ancestry, PR numbering, and
author status are not scientific evidence.

This local supercell Cycle 610 is distinct from the causal-time Cycle 610 in
PR #5557. The repeated cycle number is only a naming collision; no causal-time
claim or evidence is imported here.

## What remains exact

### Conditional fine-coordinate schedule

Within the supplied cell partition, the base stream schedule has 44,544
coordinate gate instances per coarse cell, support at most two, and zero
nearest-neighbor adjacency failures. One orientation-controlled branch has
770,876 lowered primitive descriptors and 102,693,692,972 returned bus SWAPs.
The full 24-branch product counts 18,501,024 primitives and
2,464,648,631,328 returned SWAPs per coarse cell. These are enormous constant
resource upper bounds, not energy or gravity source terms.

The Hamiltonian bus covers all 2,146,689 sites. All 2,146,688 consecutive bus
edges and the coordinate/index inverse pass. The maximum route distance is
1,168,111. Each move/apply/restore descriptor identifies the exact opening
SWAP interval, adjacent application edge, and returned interval.

The dual-neighbor cross-face comparator compiles 72 controlled SWAP rows per branch on
literal five-site lines with 110 microsteps each. Its controlled-SWAP residual
is `7.795215032290469e-16`, scratch-return leakage is
`2.157913621781963e-16`, and full-unitarity residual is
`6.055588362377014e-15`.

These are conditional coordinate and local-circuit facts. The runner does not
compose a literal physical encoder, does not evaluate a physical intertwiner
residual, and does not evaluate full physical-code leakage; those fields are
`false`/`null`.

### Register EG, inverse, deletion, and malformed controls

The Cycle-606 double-buffer semantics are reexecuted at L3/L6/L7:

| L | lawful rows | register EG / inverse EG | random inverses | deletion scatter/clear/swap | collisions leaving code / inverse failures |
|---:|---:|---:|---:|---:|---:|
| 3 | 729 | 0 / 0 | 10 / 0 | 2 / 1 / 2 | 15 / 0 |
| 6 | 5,832 | 0 / 0 | 10 / 0 | 2 / 1 / 2 | 15 / 0 |
| 7 | 9,261 | 0 / 0 | 10 / 0 | 2 / 1 / 2 | 15 / 0 |

All 105 word-label pairs commute within scatter and clear; the tested label order
is explicit, and reverse plus
all24-rotated enumerations reproduce each sublayer. Duplicate-carrier states
remain reversible but leave the declared code; they are not repaired.

The exact identity established here is only

```text
E_register G_coarse = G_conditional-register E_register
```

on the declared register sector. It is not
`E_physical G_coarse = G_physical E_physical`.

### Mass, contact, seam, and factor order

The inherited one-particle mass fixture remains preserved at the conditional
routing scope. Exact residuals are:

```text
full-16 compiled mass coin                 8.619648052454238e-14
cubic coin symmetry                        1.731958809481102e-16
coin scratch return                        2.890151575626252e-15
contact / inverse-contact phase            0 / 0
Cycle-600 coin EG                          1.154543706932542e-15
Cycle-600 contact EG                       0
Cycle-600 local stream/seam EG             0
compiled word-coin EG                      4.0336968129257627e-13
```

The Cycle-230 free factorization residual is zero. Reversing the accepted
schedule changes the result by `0.5202793649337463`. Deleting coin, stream, or
contact changes the seeded probe by `1.9020837629144585`,
`1.9968896435700219`, and `0.08827995040981686`. The contact/free-generator
noncommutation witness is `2.3934793937974876`.
Factor order is supplied law content; the schedule is not time.

## Exact covariance scope

- Coarse-grid translations: all 27/216/343 cell displacements pass. Each step
  is 129 fine sites. These are not one-fine-site translations.
- Unit translations: the one-fine-site x code-support test is directly
  executed and fails invariance by 2,970/23,760/37,730 sites. All six unit
  direction differences are recorded in the receipt.
- All 24: rotated role/path/bus branch coordinate realizations are executed
  about supplied coarse-cell origins.
- All 576: 859,392 route-generator coordinate composition checks pass, as do
  35,808 rotated-bus realization checks. This is a conditional coordinate
  group action, not 576 physical update-covariance tests.
- Proper rotations about every fine physical site are not executed.
- L3/L6/L7 wrap-seam adjacency, conditional bus conflicts, and five-line
  support conflicts remain zero at their declared coarse-grid scope.

## Constraint audit

Cycle 610 executes the 24 lawful exactly-one truth rows and the zero-hot,
two-hot, and all-hot identity-extension tables. It also counts a six-edge
coarse-cell syndrome for one changed orientation word at each L. The C24X
predicate computation/uncomputation is a literal conditional gate word.

None of those is a locally enforced nearest-neighbor admissibility gadget; the
supplied code conditions are not locally enforced.
There is no literal fine-NN exactly-one enforcement law, no literal fine-NN
uniform-equality enforcement law, and no preparation, rejection, repair,
cooling, or penalty dynamics. The exactly-one and equality sectors remain
supplied code conditions. A truth table or syndrome counter is not enforcement.

## Supplied structure

The construction explicitly supplies:

1. the K-periodic coarse partition/origin and structural role coloring;
2. the identity-frame canonical motif and its 24 coarse-origin rotations;
3. the uniform one-hot orientation table and genesis;
4. blank B/path/flag/predicate work;
5. the global exactly-one-carrier-per-species sector;
6. coin -> stream -> contact and scatter -> clear -> swap factor order;
7. beta/contact-g parameterized rotations;
8. periodic L3/L6/L7 fixtures.

There is no runtime Jordan-Wigner parity string, nonlocal parity service,
carrier ordering, frame query, or size query. That does not remove the supplied
static coarse origin/coloring.

## Route disposition

- Route A retains an exact conditional K-grid coordinate construction and
  exact register semantics, but fails physical promotion under a one-fine-site
  translation.
- Route B’s Cycle-606 lane result remains a register comparator. It is not
  silently credited as a physical repair of the translation-phase problem.
- Route C’s state-carried scheduling phase suggests the strongest repair
  pattern, but its current phase is not a translation-origin phase and is not
  physical time.
- A naive unlabelled union of all `K^3` translated motif supports fills the
  fine cell and is translation-invariant as a set, but aliases distinct role
  labels. It is not an injective encoder.

The strongest live repair is a state-carried translation phase
`phi in Z_129^3`, or an injective co-present union of translated role copies.
A unit translation must map `phi -> phi+e_i`, while mutually exclusive
`P_(phi,h)` branches select the translated and rotated coordinate word. The
repair must construct literal fine-NN phase recognition/admissibility and test
one-fine-site code-domain plus update covariance.

## Six-wall ledger

- `C_ref`: not retired. Proper-cubic coordinate orbits pass conditionally, but
  the K-periodic origin/coloring privileges a translation phase.
- `C_num`: unchanged. Beta/contact-g precision remains imported.
- `C_wrap`: unchanged. Wrapped phase is not called energy.
- `C_int`: advanced only conditionally. Register stream and mass/contact/seam
  fixtures compose inside a supplied coordinate word; physical EG/leakage and
  collision repair remain open.
- `C_local`: narrowed. Bounded conditional placement passes, while one-site
  translation covariance and locally enforced admissibility fail promotion.
- `C_source`: unchanged. Site, role, and gate counts are bookkeeping, not
  source or energy.

## No-Go Discipline Gate — N1 through N8

### N1 — normalized alternatives

Six qualifying families use only exact markers:

1. `ATTEMPTED`: fixed-origin K-periodic conditional supercell; conditional
   routing passes, unit-translation promotion fails.
2. `ATTEMPTED`: compact double-buffer register stream; register EG/inverse and
   deletion pass, physical encoder/covariance remains open.
3. `ATTEMPTED`: 24 proper-cubic orientation-controlled branches; coarse-origin
   coordinate action passes, translation phase remains supplied.
4. `ATTEMPTED`: Hamiltonian-bus/five-line primitive descriptors; conditional
   routing residuals pass, full physical intertwiner/leakage is absent.
5. `ATTEMPTED`: unlabelled union of all translated motif supports; set support
   becomes invariant but role-label injectivity fails.
6. `RULED OUT BY PRIOR`: independent crossed-link tables alone; Cycle-603 note
   lines 153-172 explicitly says they are not one torus update.

The state-carried translation phase and injective translated-copy union are
`OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT`.

### N2 — wall independence

The collapsed walls are: supplied K-periodic origin/coloring; fine-NN
admissibility enforcement; physical encoder/intertwiner/leakage; global
one-carrier sector; blank-work genesis; analog calibration; and macro factor
order. All 21 unordered pairs are recorded in both directions. No automatic
implication or shared witness is constructed. This is a dependency inventory,
not a shared obstruction.

### N3 — hidden-wall scan

The required phrases are classified in the receipt. `canonical` is
load-bearing here: it names the supplied identity-frame motif/path convention,
so it is promoted to the K-periodic origin/coloring wall. Blank work,
one-carrier sector, periodic sizes, one-hot/equality tables, spacer sites, and
the frozen origin are explicit. No “standard QFT” or “obvious” step carries
weight.

### N4 — residual matching

Cycle-606 note lines 25-29 and 104-107 names the missing physical
encoder/product/intertwiner/leakage and one-site covariance. That residual
matches and remains open: physical residual is null and the exact translation
symmetric differences are nonzero. Cycle-603 note lines 120-130 matches the
analog-angle import; it remains open. Cycle-606 note lines 80-88 and 167-180
matches the collision/sector residual; all 15 collision pairs leave code and
are reversible, not repaired. No mismatched witness is used.

### N5 — rhetoric at multiple resolutions

The receipt separately audits coarse-cell versus one-fine-site translation;
literal coordinates versus encoder/intertwiner; truth tables versus NN
enforcement; role/path group action versus physical update covariance; register
EG versus physical EG; factor schedule versus causal time; and counts versus
source/energy. Untested resolutions remain open.

### N6 — partial-closure paths

The file/status/what-closes table retains Cycles 580, 603, 606, and this local
Cycle 610 at their exact scopes. The priority open path is a state-carried
`Z_129^3` phase with literal fine-NN recognition and unit-translation tests.
Other live paths are an injective union of translates, explicit admissibility
gadgets, physical encoder/intertwiner/leakage, reversible collision syndrome,
and certified epsilon synthesis. These are constructive import-retirement
routes, not requests for new axioms.

### N7 — hostile steelman

A hostile reviewer can replace the privileged origin by a state-carried
translation phase, make unit translations permute that phase, and compile all
translated/rotated conditional words under one local rule. Alternatively, an
injective co-present translated-copy code could let translations permute copy
labels. Cycle 610 tests only one supplied phase and finds no contradiction to
either route; the naive union fails merely by role aliasing. The terminal
obligation is literal NN admissibility, one-site domain/update covariance,
every-site rotations, physical encoder/intertwiner/leakage, deletion, and held
sizes. Status is `OPEN / no retained authority`.

This actionable steelman makes the broad-negative gate FAIL / DO NOT SHIP.

### N8 — cross-cycle echo

Cycles 560/563 retired decoder and ordering services using explicit encoders
and transported colors. Cycle 580 materialized one bounded physical layout.
Cycle 603 materialized local role-event gates. Cycle 606 materialized the
global register stream. Local Cycle 610 materializes only a conditional
coordinate placement. The same constructive pattern points to a transported
translation phase and explicit local gadgets, so no impossibility,
minimum-content, shared-obstruction, or axiom-pressure claim is justified.

## Final disposition

The narrowed conditional positive artifact passes. Physical-M2-law promotion,
the broad negative, minimum-content claim, shared obstruction, axiom pressure,
and breakthrough all fail or remain false. The next campaign is the
state-carried translation-phase/injective-union repair with literal local
admissibility and one-fine-site covariance tests, followed by physical
encoder/intertwiner/leakage and collision controls.
