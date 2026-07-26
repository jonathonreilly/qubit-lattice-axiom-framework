# Cycle 705 Route A — direct reference-edge support-localization note

**Date:** 2026-07-25

**Type:** meta

**Authority:** none

**Audit:** unset

**Dependency:**
`CYCLE703_LOCAL_GAUSS_HELD_PATCH_GRAMMAR_ADDENDUM_2026-07-25.md`

## Result

Route A adds one intercell reference edge `r_x--r_y` beside every matter
stream edge `u--v`, and adds the bounded four-edge rectangle projector

```text
L_xy = loop(r_x,u,v,r_y) = +1.
```

This produces the strongest honest split result:

- **Phase-aware common E: positive.**  An explicit stabilizer-tableau common E
  is constructed on L, held 2x2/3x3, and periodic `L=3,4`.  Every graph-edge
  coin, contact, and directed stream summand restricts to its intended matter
  Pauli with zero phase failures and zero Wilson-gauge coordinates.
- **Matter law and degree count: unchanged.**  Every added edge brings one
  rank-active rectangle row.  Open/fixed-sector code dimension remains exactly
  `2^(6N)`; periodic local constraints leave `2^(6N+3)` and fixing the three
  Wilson characters leaves `2^(6N)`.  The new edge supplies no independent
  logical or propagating mode.
- **Support-localization objective: negative for this incidence.**  The direct
  stream reaches maximum Pauli weight/site diameter `23/32` on all three
  patches and `28/32` on periodic `L=3,4`.  The exactly equivalent path grammar
  remains at `17/28` on every fixture.  The new reference vertex incidence
  enlarges the `A(r_x,r_y)` order tail; a graph-theoretically shorter edge is
  not a smaller BKSF Pauli word.
- **Resource import: explicit.**  A matter and reference graph-edge qubit share
  each bond midpoint as two distinct typed abstract fiber slots.  Spatial
  midpoint collisions therefore equal the bond count, while typed abstract
  fiber-address collisions are zero.  This is placement data on the graph, not
  an injective one-M2-per-`Z^3`-site placement.  The fiber label is invariant
  under translations and all proper-cubic frames.
- **Retirement path: exact.**  On the full Pauli algebra,

  ```text
  A(r_x,r_y) = path_A(r_x,u,v,r_y) L_xy.
  ```

  Thus every direct stream term and its prior path term have identical
  common-E restriction.  Removing the added edge and rectangle returns to the
  lower-support Cycle-703 path route without changing the matter law.

This is not a finite dense completion and not a bounded preparation result.
No general reference-edge, incidence-order, gadget, or locality no-go follows.

## Exact ranks and phase-aware common E

| Fixture | cells `N` | bonds / added edge qubits | total edge qubits | local-loop rank | local-loop+`D` rank | fixed-Wilson rank | direct-sum exponent | fixed exponent |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L | 16 | 16 | 320 | 209 | 224 | 224 | 96 | 96 |
| held 2x2 | 20 | 20 | 400 | 261 | 280 | 280 | 120 | 120 |
| held 3x3 | 39 | 42 | 786 | 514 | 552 | 552 | 234 | 234 |
| periodic `L=3` | 27 | 81 | 648 | 457 | 483 | 486 | 165 = `6N+3` | 162 = `6N` |
| periodic `L=4` | 64 | 192 | 1536 | 1086 | 1149 | 1152 | 387 = `6N+3` | 384 = `6N` |

The local-loop ranks equal the full graph cycle rank on each patch.  On both
tori they are short by exactly three Wilson rows.  For every fixture:

- the number of rectangle rows equals the number of added reference edges;
- the full logical-pair commutator matrix has zero failures;
- every logical generator commutes with every loop/`D` code row;
- matter `Z_(x,a)=B(m_(x,a))`; and
- the phase-aware local logical flip is

  ```text
  X_(x,a) = i A(m_(x,a),r_x) product_(b>=a) B(m_(x,b)).
  ```

The maximum matter-logical-`X` weight/diameter is `19/16`, independent of
fixture size.  Periodic Wilson-conjugate `X` weights are `(18,18,18)` at
`L=3` and `(32,32,32)` at `L=4`; these are explicitly global gauge operators,
not local update words.

Let `|Omega_+>` be the unique simultaneous `+1` state of the local loops,
all `D`, the three Wilson `Z` rows when periodic, and all matter `Z` rows.  The
common E is the phase-fixed tableau map

```text
E |n,g> = product_i X_i^(n_i) product_j Xg_j^(g_j) |Omega_+>.
```

The vacuum tableau rank equals the number of graph-edge qubits on all five
fixtures, with zero inconsistent-phase relations.  Its columns are specified
by the tableau and logical actions; exponentially large dense vectors are not
materialized.  No preparation-depth conclusion is attached to this E.

## Support comparison

| Fixture | direct max weight | path max weight | direct max diameter | path max diameter | direct advantage |
| --- | ---: | ---: | ---: | ---: | --- |
| L | 23 | 17 | 32 | 28 | no |
| held 2x2 | 23 | 17 | 32 | 28 | no |
| held 3x3 | 23 | 17 | 32 | 28 | no |
| periodic `L=3` | 28 | 17 | 32 | 28 | no |
| periodic `L=4` | 28 | 17 | 32 | 28 | no |

Other bounded supports are:

| Family | patches | periodic `L=3,4` |
| --- | ---: | ---: |
| rectangle projector weight / diameter | 18 / 32 | 21 / 32 |
| local `D` weight / diameter | 12 / 16 | 12 / 16 |
| matter logical `X` weight / diameter | 19 / 16 | 19 / 16 |
| coin/contact maximum weight / diameter | 12 / 16 | 12 / 16 |

Diameter uses the minimal periodic metric on a torus.  The path comparator is
evaluated in the same direct-edge graph as well as inherited from Cycle 703;
both give `17/28`.  Therefore the comparison does not come from different
held geometry or a seam-wrapping coordinate artifact.

## Every-summand common-E tests

| Fixture | directed stream operands | stream Pauli summands | coin factors | contact factors | active onsite log summands |
| --- | ---: | ---: | ---: | ---: | ---: |
| L | 32 | 128 | 176 | 240 | 1792 |
| held 2x2 | 40 | 160 | 220 | 300 | 2240 |
| held 3x3 | 84 | 336 | 429 | 585 | 4368 |
| periodic `L=3` | 162 | 648 | 297 | 405 | 3024 |
| periodic `L=4` | 384 | 1536 | 704 | 960 | 7168 |

For every directed stream operand, all four restricted Pauli summands are
executed on all 4,096 two-cell matter columns in that operand's declared
source-target tensor order.  FSWAP action failures, common-E restriction
failures, Hermiticity failures, code-projector commutator failures, and
Wilson-gauge coordinates are all zero.  The maximum direct-versus-path
common-E mismatch is zero.  A bare matter edge anticommutes with exactly the
two endpoint `D` rows on every operand, so reference dressing is active.

For every listed coin/contact Hermitian-log summand:

- the graph-edge term restricts to the independently identified local matter
  Pauli with exact phase;
- the maximum logarithm reconstruction residual is
  `7.397092656394907e-18`;
- restriction, logical-summand, gauge-coordinate, Hermiticity, and projector
  failures are zero.

The one-particle coin eigen residual is `2.594441202963249e-16`.  The measured
mass is `0.45340565417488515` versus the Cycle-219 fixture
`0.4534056541748851`, residual `5.551115123125783e-17`.  Vacuum/one-particle
contact and double-occupation contact-phase residuals are zero.

## Translations and proper-cubic covariance

Every periodic translation is executed: 27 on `L=3` and 64 on `L=4`.
Corrected A/B, projector-family, direct-stream-summand, bond-fiber, and
phase-aware common-E failures are zero.

On L, held 2x2, and held 3x3, every one of the 24 proper-cubic frames and all
576 ordered frame products are executed.  The common-E comparator uses the
signed fermionic Fock lift of the six direction permutation, rather than a
phase-blind qubit permutation.

| Fixture | raw port mismatches | corrected A/B | projector | stream summand | typed address | common E | 576 common-E compositions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| L | 6945 | 0 | 0 | 0 | 0 | 0 | 0 |
| held 2x2 | 8682 | 0 | 0 | 0 | 0 | 0 | 0 |
| held 3x3 | 17034 | 0 | 0 | 0 | 0 | 0 | 0 |

The full Cycle-219 coin covariance residual and scalar-incidence contact
residual are also zero.

## Import, dynamics, and deletion audit

Supplied structure:

- one scalar reference fermion per cell and the local law
  `D_x=B(r_x) product_a B(m_(x,a))=+1`;
- one reference-stream graph-edge qubit per matter bond;
- a local two-channel bond-midpoint fiber distinguishing matter/reference
  graph-edge qubits without orienting the undirected bond;
- one rectangle constraint per added edge;
- the local incidence-order gauge and, periodically, a typed three-qubit
  Wilson input; and
- the Cycle-219 coin, Cycle-230 stream/contact data, and factor schedule.

The added resource changes the off-code graph and constraint family.  It does
not change the intended on-code matter update:

- every direct term equals the path term modulo its rectangle stabilizer;
- every update summand has zero Wilson `X` and `Z` coordinates, proving
  sector-identical `G_matter tensor I_8`, rather than mere sector preservation;
- every rectangle row is independently rank-active; and
- after all rectangles are enforced, there is no additional logical exponent.

Deletion controls are exact on every fixture:

- deleting any one rectangle row lowers stabilizer rank by one;
- deleting reference dressing from any stream reopens exactly two endpoint
  `D` constraints;
- deleting any one displayed `D` changes no rank because the full family has
  one product redundancy;
- deleting any two displayed `D` rows releases one logical bit;
- on both tori, deleting any Wilson row releases one gauge bit; and
- deleting the contact phase gives residual `0.36789306705608243`.

The direct edge is therefore a real, deletion-active off-code import, but not
a new matter degree.  Since its tested support cost is worse and its on-code
action is exactly the path action, the optimal Route-A disposition is to
retain the common-E theorem and retire the static edge import unless a new
incidence/gadget construction reverses the support table.

## No-Go Discipline Gate

**Gate result: FAIL for a general support/locality no-go.  Retain only the
fixed-incidence support negative and the algebraic common-E positive.**

- **N1 — Normalized alternative families.** (1) **ATTEMPTED:** a direct typed
  reference edge with a rectangle invariant; algebra closes but support is
  worse.  (2) **ATTEMPTED:** the three-edge path formulation with the same
  terminal logical action; it retains `17/28`.  (3) **UNTESTED:** reorder the
  BKSF incidence around reference bonds to reduce the direct `A` order tail.
  (4) **UNTESTED:** replace the co-located fiber by a proper-cubic symmetric
  split-edge gadget.  (5) **UNTESTED:** time-multiplex a reference ancilla and
  trade static edge-qubit count for schedule depth.  (6) **ATTEMPTED:** phase-aware
  tableau/Wilson subsystem encoding; it closes E and `I_8`, not support.
  Because at least three actionable families remain untested, a broad no-go
  fails.
- **N2 — Wall independence.** Let `W_s` be a smaller-support direct/gadget
  representative, `W_p` bounded autonomous preparation of the tableau E, and
  `W_g` autonomous choice of a matter-only Wilson vector.

  | pair | first closes second? | second closes first? | independent? |
  | --- | --- | --- | --- |
  | `W_s,W_p` | no | no | yes |
  | `W_s,W_g` | no | no | yes |
  | `W_p,W_g` | no | no | yes |

  The edge-cycle and rectangle-enforcement obligations are not counted as two
  walls: the rectangle row is precisely what removes the edge's extra cycle.
- **N3 — Hidden-condition scan.** The added graph-edge qubit, midpoint fiber, rectangle
  enforcement, incidence order, directed operand tensor order, periodic
  boundary, and Wilson input are explicit.  No appeal to “standard” or
  “obvious” physics carries a residual.
- **N4 — Residual matching.** The Cycle-703 held-patch grammar attacks the same
  four-summand stream residual and is a matching support comparator.  The
  Cycle-703 vacuum-genesis addendum attacks preparation, not Pauli support, so
  it is excluded as evidence for the support negative.  Cycle-232's uniform
  reference attack has a different parity residual and is also excluded.
- **N5 — Resolution/rhetoric audit.** Weight and site diameter are tested per
  summand and maximized per patch/torus.  The result does not cover alternate
  incidence orders, split gadgets, gate depth, noise sensitivity, decoding,
  or arbitrary lattice families.  “No support advantage” always means this
  direct-edge incidence on the five executed fixtures.
- **N6 — Partial closure/import retirement.** The exact identity
  `A_direct=path_A L_xy` retires the added edge and fiber without a new axiom
  or changed matter law.  The Cycle-703 path action, mass/contact, and
  covariance were independently retained.  Transporting this addendum's
  phase convention to a path-only tableau is a separate exact chart comparison,
  not silently credited here.
- **N7 — Steelman.** A hostile reviewer can point to the load-bearing
  incidence order: BKSF `A` weight is an order-tail property, not graph-edge
  length.  Reordering ports around `r_x--r_y`, or resolving the bond into a
  symmetric bounded gadget, could reduce that tail while preserving the
  rectangle identity.  The terminal test is a held-size table strictly below
  `17/28` with the same common-E and covariance residuals.  This runner does
  not attempt either mechanism.
- **N8 — Cross-cycle echo.** Repository no-go ledgers and notes with similar
  “support localization” language attack unrelated source/detector residuals.
  The relevant Cycle-232 parity failure was already retired by local `D`.
  That retirement mechanism—replace a global relation by a local constraint—
  is already used here and prevents echoing the older failure into Route A.

The failure of the broad gate is decisive: no impossibility, minimum-content,
or axiom-pressure claim is supported.

## Reproduction

```bash
PYTHONPATH=scripts python3 -u \
  scripts/frontier_cycle705_direct_reference_edge_support_localization_2026_07_25.py
```

Expected terminal:

```text
DIRECT_REFERENCE_EDGE_COMMON_E_EXACT_PATH_SUPPORT_ADVANTAGE_RETAINED
```

The retained run passes 9 checks and fails 0.  Runtime, peak RSS, and
certificate SHA-256 are recorded in the runner cache.
