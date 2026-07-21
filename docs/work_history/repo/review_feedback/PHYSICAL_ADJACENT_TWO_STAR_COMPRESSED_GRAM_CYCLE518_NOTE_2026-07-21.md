# Physical adjacent-two-star compressed Gram — Cycle 518 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

## Result

Cycle 518 resolves the 245,518,336-branch injectivity question left open by
Cycle 517 without materializing that branch set.  The answer for the native
Cycle-311/315 representatives is negative, but narrowly so.

Each of the twelve cells has two vacuum gauge terms whose quotient is one
pure auxiliary-X role toggle.  The twelve toggles are independent, commute
with the tested representatives, and change neither the fixed-Wilson face ray
nor the branch amplitude.  Removing only toggles available on vacuum cells
reduces the exact census to

| sector | excitation seeds | vacuum expansion | physical branches |
|---|---:|---:|---:|
| vacuum | 1 | (2^{12}) | 4,096 |
| one particle | 720 | (2^{11}) | 1,474,560 |
| same-cell two particle | 360 | (2^{11}) | 737,280 |
| split two particle | 237,600 | (2^{10}) | 243,302,400 |
| total | **238,681** | — | **245,518,336** |

At both train (L=5) and held (L=6), the 238,681 seeds occupy 238,657
quotient fibers: 238,633 singletons and exactly 24 doubletons.  No fiber is
larger than two.  All 24 doubletons are cross-column split-particle pairs.
For every pair the vacuum-toggle coefficient difference is zero, the two
canonical face representatives are the same fixed-Wilson ray, and eight cells
are vacuum on both sides.  Consequently each seed pair expands to exactly
(2^8=256) shared physical rows.  The complete count is

\[
24\,2^8=6,144
\]

collision pairs and therefore

\[
245,518,336-6,144=245,512,192
\]

unique rows per size, with maximum row multiplicity two.  The relative-ray
phase histogram is 4,096 phase-zero rows and 2,048 phase-two rows.  All 48
logical columns involved in the 24 pairs are distinct.

Every split-sector branch has amplitude magnitude (1/320).  Thus the fixed
factor-order Gram has 24 isolated off-diagonal pairs of exact magnitude

\[
\frac{256}{320^2}=\frac1{400}.
\]

Its operator residual is exactly (1/400), and its squared Frobenius residual
is (3/10,000).  The native fixed-order encoding is therefore not isometric.
This conclusion follows from exact support, exact stabilizer phases, and
rational branch weights; a numerical zero or magnitude cutoff never selects
a branch.

## What the order character repairs—and what it does not

Sixteen collision pairs have different singleton anticommutation characters.
Exact subset dynamic programming over all (12!) factor orders gives zero
signed character sum for each of those differences.  The correctly weighted
Cycle-517 orientation quotient therefore cancels all sixteen.

The other eight zero-character pairs have character `(0,0)`: neither branch
has any active order-character edge.  Their signed order sum is (12!), so
their exact (1/400) overlaps survive both the full uniform S12 role and its
correctly weighted 19,208-orientation compression.  The weighted construction
has eight isolated off-diagonal Gram pairs, operator residual (1/400), and
squared Frobenius residual (1/10,000).  Equal orientation weighting remains
incorrect for the independent Cycle-517 reason; the present counterexample
persists even after the correct linear-extension weights are used.

One explicit order-invisible witness is:

- first seed: cell 0, mode 0, aggregate term 4; cell 8, mode 1,
  aggregate term 2;
- second seed: cell 1, mode 3, aggregate term 2; cell 3, mode 2,
  aggregate term 0.

The coefficient difference is zero, the joint-vacuum mask is `0xEF4`, the
face-ray relative phase is two, and both fifteen-bit characters are zero.
All 256 aligned vacuum branches collide at L5 and L6.

The eight zero-character collision fibers prove that order information alone
does not repair this particular native encoding.  They do not prove that a
different bounded physical encoding is impossible.

## Exact orbit criterion

For an excitation seed (s), let (V_s) be its vacuum-cell set, (a_s) its
canonical auxiliary word, and ([P_s]) its fixed-Wilson face ray.  Let
(R_V) be the GF(2) span of the pure vacuum toggles on (V).  Two seed orbits
share a physical row exactly when

\[
[P_s]=[P_t],\qquad a_s\mathbin\oplus a_t\in R_{V_s\cup V_t}.
\]

When the twelve toggles are independent, an intersecting pair has exactly
(2^{|V_s\cap V_t|}) aligned vacuum choices.  This is an intersection test,
not an equality-of-cosets test.  It is also occupation-aware: a toggle cannot
be removed at a cell occupied in both seeds.  The runner retains the GF(2)
coefficient mask, checks that its support is available on at least one side,
then checks the canonical face rays and expands every common-vacuum choice.

This closes two tempting but invalid shortcuts.  Globally clearing all role
bits creates false collisions when a cleared cell is occupied on both sides.
Requiring complete vacuum-orbit equality misses real partial intersections.
An auxiliary-only row key is likewise insufficient unless one face ray per
auxiliary word has already been proved.

## Proper-cubic, deletion, and lawful-domain controls

The runner transports all 24 collision witnesses through all 24 proper-cubic
frames at both L5 and L6: 1,152 reconstructed collision tests.  Auxiliary-word
equality, face-ray equivalence, and the ordered pair of physical characters
are preserved.  The eight zero-character witnesses therefore give 384
zero-character transport tests.  This is covariance of the counterexample
set, not synthesis of a covariant repair.

L4 remains outside the lawful domain because the patch acquires the extra
periodic wrap edge already identified by Cycle 517.  The maximum number is
two.  No higher-number, recurrent-volume, boundary, or thermodynamic limit is
inferred.

Deletion controls explicitly reject:

- clearing a role toggle on a jointly occupied cell;
- requiring orbit equality instead of orbit intersection;
- merging inequivalent face rays under one auxiliary-only key;
- deleting the Cycle-517 linear-extension weights;
- claiming the order character repairs the displayed `(0,0)` witness.

A single additional binary discriminator has enough address capacity because
every collision fiber has size two.  Capacity is not a physical construction:
the runner does not supply the local rule, its constraint, its initialization,
or its frame action.

The final target certificate passed all 9 gates in 45.281 seconds with maximum
RSS 259,276,800 bytes and process swap count zero.  It executed 1,152 proper-frame
collision transports, including 384 transported zero-character witnesses.
The train and held abstract collision signature is
`85c36d610d60d6abcab18caaa9e44ebcc3165cafec1deda8df2a19181700d2b3`;
the full per-size collision-row digest is
`6def9bd6f18b500eebe14b237fa60d363eefe19c3264bc741806507f3098b806`.

## Claim boundary and supplied structure

The exact statement is:

> On the twelve-cell global-(N\leq2) patch at L5 and held L6, the native
> Cycle-311/315 representatives are non-isometric in a fixed factor order and
> remain non-isometric after the exact weighted Cycle-517 order character is
> included.  The maximum Gram residual is exactly (1/400); eight
> zero-character collision pairs remain.

This is a route-specific falsification.  It is not an obstruction to a local
CAR compiler, not a lower bound on all encodings, not a minimum-content
theorem, and creates no axiom pressure.  It does not establish

\[
E G_{\rm coarse}=G_{\rm physical}E.
\]

The supplied inputs are the Cycle-311/315 role-gauge representatives and
amplitudes, the Cycle-517 twelve-cell geometry and exact order character, the
fixed-Wilson reference-vacuum reducer, and the uniform S12 order state with
its exact linear-extension compression.  Physical constraint synthesis,
off-code completion, the free-plus-contact update, the mass fixture on the
repaired code, recurrent overlap, autonomous scheduling, time, Records,
source/gravity response, and Born weights remain open.

## N1–N8 no-go discipline

Gate status for any broad compiler no-go: **FAIL / DO NOT SHIP**.  The result
is demoted to a bounded route-specific counterexample with explicit live
repairs.

### N1 — alternative-route map

The normalized approach families are:

1. **Native fixed-order representatives — ATTEMPTED.**  Exact compressed Gram
   evaluation finds 24 nonzero overlaps of magnitude (1/400).
2. **Uniform full-S12 or weighted orientation character — ATTEMPTED.**  Exact
   signed order sums cancel sixteen overlaps but leave eight `(0,0)` pairs.
3. **Binary fiber discriminator — UNTESTED / LIVE.**  One bit has sufficient
   capacity for every size-two collision fiber; a local covariant rule is the
   next terminal obligation.
4. **Changed carrier/path representatives — UNTESTED / LIVE.**  Alter the
   native face or auxiliary rays while preserving each local M64 column and
   retest the 238,681-seed Gram.
5. **Plaquette-local gauge or flux tag — UNTESTED / LIVE.**  Attach a bounded
   relational character to the four collision plaquettes and prove its local
   constraints and proper-frame transport.
6. **Tagged staggered schedule — UNTESTED / LIVE.**  Separate the colliding
   branches in an autonomous microstep role and prove coherent lumpability
   and terminal-order independence.
7. **Exact interference repair — UNTESTED / LIVE.**  Modify branch phases or
   amplitudes subject to local M64 isometry and the free-plus-contact update,
   then require every surviving off-diagonal Gram entry to cancel.

These are materially different in primary object, separation mechanism, and
terminal proof obligation.  Because five constructive families remain live,
the broad no-go gate necessarily fails.

### N2 — wall-independence audit

The raw list contains collision separation, covariance of the chosen repair,
local constraint enforcement, update intertwining, and recurrent overlap.
They are not five independent causes of the present failure.  The only
current encoding defect is **W_sep**, separation of eight zero-character
fibers.  Covariance and constraint enforcement are downstream admissibility
conditions on a selected separator; update intertwining and recurrence are
later compiler obligations.  The collapsed Cycle-518 wall set therefore has
one member, W_sep.  Closing W_sep does not by itself close any later compiler
obligation.

### N3 — hidden-wall scan

The proof does not use “we assume,” “naturally,” “obviously,” “standard QFT,”
or unspecified bridge context.  “Supplied” is restricted to the four inputs
listed above.  The fixed-Wilson vacuum, amplitude grammar, patch geometry,
and role weights are hash-bound executable inputs; their primitive synthesis
is explicitly outside the claim.

### N4 — residual matching

Cycle 517 is cited only for the twelve-cell graph, exact static character, and
linear-extension weights; it explicitly left the Gram open.  Cycle 515 is
not used as evidence that twelve cells are injective: its exact injectivity
theorem covers one seven-cell star only.  Cycle 516 is used only through the
proper-frame physical reconstruction inherited by Cycle 517.  No mediator,
source, response, time, Record, Born, or prediction residual is cited against
this Gram defect.

### N5 — rhetoric audit

“Not isometric” means only the two explicitly tested twelve-cell maps on the
declared global-(N\leq2) code: native fixed order and native representatives
with the exact weighted order character.  The runner does not test every
bounded encoding, every representative grammar, higher number, adjacent
patch tilings, or a lattice-wide compiler.  “Order information alone” means
the branch character generated by reordering these same representatives; it
does not include a new branch-dependent role.

### N6 — partial-closure path

The smallest live repair is to assign opposite values of one additional role
bit inside each of the 24 doubletons, derive that assignment from bounded
local data, transport it covariantly, and rerun the same compressed Gram.  A
representative change or plaquette gauge tag can close the same W_sep defect
without changing an axiom.  Only after an isometry passes should the physical
free-plus-contact block, mass fixture, schedule, and recurrent overlap be
tested.

### N7 — hostile steelman

A hostile reviewer should reject any obstruction claim immediately: the
defect is only eight isolated size-two fibers, so one bit of separation has
ample information-theoretic capacity.  The collisions lie on a finite family
of local adjacent-center plaquettes already exposed by the physical graph.
A proper-cubic plaquette tag or a revised carrier-path convention could split
them while retaining constant overhead and no global ordering.  The concrete
terminal obligation is to give one uniform local formula, prove its 24-frame
action and local constraints, and obtain an exact identity Gram at L5/L6.

### N8 — cross-cycle echo

Cycles 311, 315, 515, and 516 repeatedly retired apparent collisions by
adding a bounded role, retaining a relational order, or inserting the exact
Koszul correction.  Cycle 518 exposes the same repair shape at the
adjacent-star level.  Those precedents make a broad no-go less credible, not
more credible.  The next cycle must try the bounded discriminator and changed
representative routes before any shared-substrate conclusion is reconsidered.

## TOE dependency impact and next attack

This result narrows (C_local): local capacity and the fifteen-bit order
character are not the issue, but the native representative grammar identifies
eight pairs that the order character cannot see.  It also sharpens (C_num) by
showing exactly where an additional discrete role would enter.  It does not
change (C_ref), (C_wrap), (C_int), or (C_source).

The optimal next attack is constructive and now has two zero-new-M2
candidates.  On the transverse-polarized survivor subspace, test a controlled
orientation character formed from the two outer axial order edges.  In the
native gauge realization, test the corresponding product of the two existing
outer-axial vacuum-role Z phases.  Neither candidate is a Cycle-518 theorem:
both still require an exact Gram, an eight-element unordered-bond stabilizer
audit, all 24 placements, local controlled-constraint synthesis, deletion,
and held-L6 controls.  If both fail, the one-bit discriminator and changed
representative routes remain live.  An accepted repair must make the
compressed Gram exactly the identity before the free-plus-contact update is
lifted.
