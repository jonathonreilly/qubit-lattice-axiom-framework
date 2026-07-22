# Non-diagonal link/qudit same-code fermion compiler tournament — Cycle 628

Date: 2026-07-22
Authority: none
Audit: unset
Constitutional effect: none
Classification: partial-attempt-with-named-untested-routes

Cycle 628 is a constructive compiler tournament. It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface. There is no axiom pressure.

## Exact target and frozen shore

The target remains one bounded physical code on M2 sites, one local encoding
`E`, and one local update `G_physical` satisfying

`E G_coarse = G_physical E`

on the complete Cycle-230 six-mode Fock space. This includes coherent odd/even
states, arbitrary finite-density occupations, the free coin and stream, local
contact, one-particle mass, and seam. Success also requires constant overhead,
support-two nearest-neighbor primitives or an exact disclosed bounded macro,
locally enforced auxiliaries, all 24 proper-cubic frames, all 576 frame pairs,
L3/L6/L7, and leakage, deletion, malformed, lawful-domain, and held-size
controls.

The accepted Cycle 622 and Cycle 620 runner, note, receipt, and cold artifacts
are pinned byte for byte. The diagonal Cycle-622 result is only a route-specific
boundary. It is not evidence against a non-diagonal qudit.

The common candidate register has 48 active M2 roles per 129^3 coarse cell:

- six data roles on a radius-60 shell;
- four tangential face-ring roles on each of six faces, 24 total;
- six radius-32 auxiliary-A roles for prefix or syndrome;
- six radius-31 auxiliary-B roles for twist or archive; and
- six radius-30 auxiliary-C roles for prefix buffer or clean resource.

The entire role set closes under all 24 frames and all 576 products without a
24-one-hot orientation. Corresponding sites of neighboring face rings are
literal nearest neighbors. The twelve off-diagonal cross-face phase pairs per
face block have move/apply/restore paths of at most four sites. The coarse
centers, role shells, and initial blank rings/auxiliaries remain supplied.

## Route A — non-diagonal four-M2 face qudit

### Local coherent isometry

Each directional data occupation is moved into the uniform one-particle mode
of a four-M2 face ring. The five-mode one-particle unitary swaps the data basis
vector with

`|W4> = (|1000>+|0100>+|0010>+|0001>)/2`

and is identity on the orthogonal ring subspace. Its exterior lift is an exact
32-dimensional unitary. Vacuum, occupied data, and a seeded coherent
zero/one-particle superposition have zero residual. The total block commutes
with all 24 permutations of the four ring sites. One support-two Givens macro
uses angles `asin(1/2)`, `asin(1/sqrt(3))`, `pi/4`, and `pi/2`; this
factorization is supplied schedule content, not time.

### Actual block swap rather than a name

Four corresponding cross-face `fSWAP = CZ SWAP` gates do not by themselves
exchange the two face qudits as graded blocks. On the sector with one uniform
particle in each ring, their code projection amplitude is 1/2, leakage is
`sqrt(3/4)`, and the residual from the desired graded exchange is `sqrt(3)`.

This is the raw-versus-complete graded block swap test. Adding the twelve
off-diagonal cross-face CZ phases completes the full sixteen
pair phases. Exhausting all 256 pairs of four-bit face words then gives

`|l>|r> -> (-1)^(N_l N_r) |r>|l>`

with zero phase, inverse, or code residual. Deleting one off-diagonal CZ is
distinguished by `l=0001`, `r=0010`. Thus the non-diagonal face code and its
graded block exchange are real constructive results, not an ordinary endpoint
swap renamed as fermionic.

### Full Cycle-230 stream sign

The completed local block braid contributes a phase only when both
counterpropagating face blocks on one undirected bond are occupied. The runner
exhausts every two-particle coefficient of the actual Cycle-230 mode
permutation:

| L | modes | all pairs | ordinary block mismatches | graded block mismatches | local face pairs |
|---:|---:|---:|---:|---:|---:|
| 3 | 162 | 13,041 | 4,194 | 4,113 | 81 |
| 6 | 1,296 | 839,160 | 155,664 | 155,016 | 648 |
| 7 | 2,058 | 2,116,653 | 341,922 | 340,893 | 1,029 |

Zero- and one-particle transport is exact. Because both the target and the
physical phases are quadratic, the exhaustive pair comparison decides the
full occupation-basis phase equality. A vacuum-plus-witness coherent state has
intertwiner residual `sqrt(2)`. Applying the inverse local coin to that witness
and then the unitary contact shows that the mismatch survives the complete
coin-stream-contact update; it is not removed by the preserved one-particle
mass, contact, or seam fixtures.

Disposition: retain the exact non-diagonal face isometry and complete graded
block swap. Route A does not supply the full-lattice exterior stream phase.
This classifies this declared uniform four-M2 face block only, not all
non-diagonal qudits.

## Route B — dynamical prefix/twist spin structure

Route B changes the mathematical mechanism rather than adding another local
face phase. It groups the one-particle modes into the exact cyclic orbits of
the Cycle-230 stream. On each length-L directed line it introduces occupation
`n_j`, prefix qubit `g_j`, and a repeated twist qubit `p_j`. The local checks
are

`p_j = p_(j+1)`,

`g_(j+1) = g_j xor n_j` away from the seam, and

`g_0 = g_(L-1) xor n_(L-1) xor p_0` at the seam.

They have rank `2L-1`, maximum weight four, retain all L occupation bits plus
one gauge-root bit, and force `p` to equal line parity. Deleting the seam row
loses one rank. The support-two local update

`n'_j=n_(j-1)`, `p'=p`,

`g'_0=g_(L-1) xor p`, `g'_j=g_(j-1)` for `j>0`

preserves every valid word. The seam phase

`Z(n_last) CZ(n_last,p) = (-1)^[n_last(P xor 1)]`

equals the fermionic cyclic-shift phase on every occupation. All words and
both gauge roots are exhaustive for L3/L6/L7. The seam family is closed under
all 24 proper-cubic frames and all 576 frame products.

This gives an exact matrix-valued full-Fock stream intertwiner after changing
from the canonical mode order to the grouped-cycle order. The runner exhausts
every pair coefficient and finds zero conjugacy failures. The exact grouped
cycle phase contains 108, 1,080, and 1,764 pair terms on L3/L6/L7.

The cost is also exact. The canonical-to-grouped encoder phase contains
5,562, 370,980, and 937,566 pair terms. Its maximum torus separation is 3, 9,
and 9. The fixed seam is invariant under proper-cubic frames but not under
nonidentity coarse translations. Prefix preparation uses a chosen root and a
line-length sweep.

Most decisively, the full update does not stay local. Conjugating an onsite
coin hop by the reordering phase introduces as many as 146, 1,250, and 1,998
spectator modes on L3/L6/L7, reaching torus distances 3, 9, and 9. Contact is
diagonal and remains onsite; the one-particle coin and mass are unchanged
because the encoder phase begins at quadratic degree. The multiparticle coin
is not bounded.

Disposition: retain the exact both-parity prefix/twist stream construction and
weight-four local constraint code. It is not the required bounded same-code
full update because `E`, prefix preparation, translation handling, and the
conjugated coin remain lattice-scale. A fixed seam/root is supplied structure,
not a host-side physical law.

## Route C — reversible resource-accounted blank renewal

For each of six auxiliary channels, Route C uses adjacent syndrome, archive,
and clean-resource M2s. Two simultaneous support-two nearest-neighbor swaps
give

`|s>|0_archive>|0_fresh> -> |0>|0>|s_spent>`.

All 64 syndrome words, a coherent superposition, number conservation, inverse,
all 24 frames, all 576 products, and L3/L6/L7 pass. Deleting either swap leaves
an explicit syndrome or archive witness. Across all 4,096 archive/fresh input
pairs, the 4,095 nonblank malformed pairs leak from the reset code.

The ledger debits six clean M2 registers per coarse cell per invocation and
retains six spent registers. L3/L6/L7 therefore debit `6L^3` clean registers
per update. The inverse renews them only by returning the syndrome. Discarding
the spent register would have Gram residual `sqrt(64*63)` and is not this
unitary mechanism. No host reset, erasure, bath, or entropy sink is silently
used.

Disposition: retain the exact one-invocation resource mechanism. A finite
reservoir supports only `reservoir_M2/(6L^3)` invocations; indefinite renewal
still needs an explicit source/resource law.

## Joint disposition and fixtures

The three routes occupy the same 48-role register but do not define the same
code or one bounded `E` and `G_physical`. Route A has a local face code and
misses global signs. Route B repairs stream signs with a nonlocal encoder and
coin. Route C renews blanks by consuming a clean register. Joining those
sentences would not create a compiler, so the strict same code identity is
withheld. The route controls explicitly include an odd/even coherent target.

The byte-pinned Cycle-622 one-particle mass, local contact, Cycle-230 seam,
factor order, deletion, and noncommutation fixtures pass. Wrapped phase is not
called energy, a generator element is not called a rate, the factor schedule
is not called time, and no archive or spent register is called a Record. This
cycle does not touch detector/readout semantics.

## Supplied-structure inventory

- 129^3 coarse centers and the radial/tangential 48-role shells;
- blank face-qudit, prefix-buffer, archive, clean-resource, and routing M2s;
- the uniform face mode, exact Givens angles, and macro factorization;
- the Cycle-230 CAR target, beta, contact coupling, coin-stream-contact order,
  and angle precision;
- periodic L3/L6/L7 domains, grouped mode order, fixed seam/root, and initial
  or boundary-state selection;
- finite clean-reservoir capacity; and
- any future bath, erasure, measurement, entropy-export, or preparation law.

No global Jordan-Wigner string or runtime parity service is used by Route A.
Route B's explicit lattice-scale ordering phase and fixed seam are recorded as
failed locality/reference obligations, not hidden as local auxiliaries.

## Prior-art and novelty boundary

No literature novelty is claimed for W-state encodings, graded swaps,
prefix-parity automata, spin-structure twists, or reversible garbage transfer
as broad mechanism classes. The Cycle-628 contribution is the exact executable
comparison at this framework contract: completing the four-site block swap,
measuring its actual full-stream residual, constructing the prefix/twist
intertwiner, and measuring the encoder/coin support it induces. No external
prior-art result is used as a premise of the finite certificates.

## Dependency ledger

- `C_ref`: sharpened; grouped ordering and fixed seam/root are now measured
  reference imports. Role-shell genesis remains supplied.
- `C_num`: advanced by the coherent non-diagonal face isometry and exact
  matrix-valued stream identity; a bounded full update remains open.
- `C_wrap`: advanced by explicit line-twist seam handling on L3/L6/L7; seam
  genesis remains supplied.
- `C_int`: contact and one-particle mass remain local, while the conjugated
  multiparticle coin becomes lattice-wide.
- `C_local`: advanced by exact graded face blocks and weight-four prefix
  constraints; no one bounded same-code compiler yet composes them.
- `C_source`: advanced to an exact six-clean-M2-per-cell-per-use debit; no
  indefinite renewal/source law is derived.

Maturity remains operational quantum/records 3.0, causal time 2.0,
inertia/matter 3.5, gravity/source 2.5, and Born/probability 1.5.

## Fresh no-go discipline

The newer origin/main no-go-discipline skill is followed. Families are
normalized by object, mechanism, and terminal obligation.

### N1 — normalized alternatives

ATTEMPTED here are the non-diagonal face-qudit block buffer, dynamical
line-prefix/twist code, and resource-accounted reversible reset. RULED OUT BY
PRIOR only at their exact scopes are Cycle 622's occupation-diagonal dressing
and Cycle 617's rough-terminal Pauli subsystem. Two materially distinct
families remain UNTESTED_LIVE: a translation-invariant fermionic PEPS/MPO
pull-through encoder and a non-Abelian higher-group fixed-point gauge code.
Therefore the broad negative gate fails.

### N2 — wall independence

The collapsed current walls are full-lattice stream phase, bounded onsite coin
after conjugacy, bounded translation-free prefix/twist preparation, literal
common NN composition, and indefinite clean-resource renewal. All ten pairs
are recorded. Current evidence does not make one automatically close another.

### N3 — hidden-condition scan

The face-ring role shell is an explicit layout/genesis import. Grouped order
and fixed seam/root are explicit reference/preparation conditions. Blank face,
archive, and clean-resource M2s are explicit resource imports. Beta, coupling,
factor order, and precision remain pinned supplied law content.

### N4 — residual matching

Cycle 622's scalar diagonal cocycle is not Route B's matrix-valued prefix code
and is not used as its proof. Cycle 617's direct endpoint-B sign is not the
four-mode face-block/full-S residual and is only adjacent prior. Cycle 622's
retained archive garbage exactly matches the renewal residual continued by
Route C, which moves rather than deletes that garbage.

### N5 — resolution audit

Route A classifies the declared uniform four-M2 face block, not all
non-diagonal qudits. Route B tests one Z2 prefix/twist construction, not every
higher group. Route C tests one finite reversible reservoir, not every
open-system reset law. No minimum-content claim is made.

### N6 — partial-closure paths

The face-qudit channel and exact prefix/twist stream identity are reusable.
A tensor-network encoder could absorb the reordering phase; a source-accounted
bath could retire the resource debit. Neither possibility is automatically a
new axiom.

### N7 — steelman

A hostile reviewer can replace the fixed grouped-order phase by a
translation-invariant fermionic PEPS/MPO tensor whose virtual parity index is
the local prefix qubit, promote the seam to a mobile gauge defect, and keep the
coin local through a tensor pull-through identity. The terminal obligation is
an explicit bounded tensor on this 48-role-or-smaller register, exact all-24
and all-576 covariance, a bounded coin conjugacy, and a locally prepared
parent-code state. Cycle 628 does not test that mechanism.

### N8 — cross-cycle echo

Cycles 610 and 620 retired packing walls with large clean-role macros. Cycles
617 and 622 partially retired parity/Wilson walls by changing representation
and resolution. That constructive history weighs against foreclosure.

N1 is FAIL for a broad negative, as it should be. Cycle 628 ships only as a
partial-attempt-with-named-untested-routes. It asserts no impossibility,
minimum content, route-independent shared obstruction, or axiom pressure.

## Optimal next campaign

Construct one translation-invariant fermionic PEPS/MPO pull-through tensor that
absorbs Route B's canonical-to-grouped phase while keeping the onsite coin
bounded. Make the spin-structure defect mobile and locally prepared, then test
the exact face-qudit stream, contact, mass, seam, all 24/all 576, and L3/L6/L7
inside that one code before any renewed negative claim.
