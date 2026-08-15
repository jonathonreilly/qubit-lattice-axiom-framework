# Constant algebraic visibility in the finite four-cube cutting system: leverage 11/24 and full-projector denominator 960

Date: 2026-08-09

Authority: none

Audit: unset

Status: proposed_retained

Claim type: bounded_theorem

Runner:

- [self-contained rebuild-and-gate runner](../scripts/physical_cell_cutting_visible_fraction_cycle760_2026_08_09.py)

Scope: exact rational and whole-number identities of one finite cutting
system. Every number below is machine-checked by the runner, which rebuilds the cell
complex, the least-volume pieces, the cuttings at the adjacency cost floor,
the cutting-by-piece table and the eight-piece exact covers, then builds the
relabellings got by permuting the four coordinates of the four-cube and
flipping any of them, measures the blocks they cut the pieces into, certifies
an exact whole-number multiple of the orthogonal projector onto the span of
the cuttings, reads its diagonal, finds the smallest whole multiplier that
clears the full matrix, sets that multiplier beside the invariant factors of the same
side's Gram matrix, and checks the exact identity tying the two sides
together, gating each quantity in place. In this note **algebraic visibility**
means a coordinate leverage score, the diagonal entry of an orthogonal
row-space projector. It is not the frequency with which that piece occurs in
the cutting list: the latter is separately 1975/15800 = 1/8. Six of the gates carry
controls whose job is to show that each hypothesis the argument leans on is
doing work, and that the routines report something other than the answer
being looked for when the answer is not there. Constitutional effect: none.
This package changes no axiom, no framework Admissibility rule, no primitive,
no policy, and no audit status, and it adds no import and no assumption to
`MINIMAL_AXIOMS_2026-06-29.md`.

The runner is scientifically self-contained: it reads no repository file and
imports no ancestral scientific artifact. Its load-bearing inputs are only the
finite definitions written in the runner itself.

## Trace gate

```yaml
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "determine the exact row-space projector invariants of the finite four-cube cutting and exact-cover incidence systems"
source_of_blocker_text: frontier_question
reachability_to_target: none
artifact_role: runner_certificate
next_trace_action: "seek a structural decomposition that derives the projector denominators 960 and 320 and the 23 orbital entry values without exhaustive reconstruction"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact certificates for ranks, transitive coordinate actions, rational orthogonal projectors, common diagonal leverage scores, least full-projector denominators, Gram invariant factors, and a linked-projector identity on one explicitly rebuilt finite object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target and obligation graph

**Exact target.** For the two finite incidence matrices rebuilt by the runner,
prove that their rational row-space projectors have constant diagonals 11/24
and 35/64, least full-matrix clearing multipliers 960 and 320, and satisfy the
linked-projector identity `Q = I - P + J/192`.

The proof has six load-bearing obligations, all proved in this package rather
than cited:

1. rebuild the finite row sets and certify their counts (C0);
2. construct a 384-element coordinate-relabeling subgroup, certify that it
   preserves both row sets, and certify that it is transitive on the 192
   coordinates (C1-C3);
3. certify the two rational ranks, saturation witnesses, and exact scaled
   orthogonal projectors (C4-C7, C12);
4. reduce the full integer numerator matrices against their proposed scales to
   certify the least full-projector denominators (C10, C12);
5. certify saturated selected Gram bases and their invariant factors, then use
   the integral-right-inverse argument below to identify the largest factor
   with the projector denominator (C13-C15); and
6. certify the linked-projector identity entry by entry (C17).

No completeness claim about the full automorphism group is an obligation or a
conclusion. The strongest missing structural lemma is a non-enumerative
decomposition that predicts 960, 320, and the two invariant-factor chains.

## What this answers

The object is the unit four-cube on sixteen corners, cut into least-volume
pieces at the adjacency cost floor. There are 15800 such cuttings; between
them they draw on 192 pieces, 24 pieces to a cutting, and each piece lies on
1975 cuttings. Those same 192 pieces admit 192 eight-piece exact covers.

The ordinary incidence frequency is already uniform: each piece occurs in
1975 of 15800 cuttings, hence in 1/8 of them. The different quantity studied
below is algebraic visibility. For the cutting row space its value is the same
at all 192 coordinates, namely 11/24. It is forced once the row space is
invariant under a transitive coordinate action, and the controls show both
hypotheses doing work.

The integer 960 belongs to a different exact statement. It is the least
positive integer `D` for which every entry of the full matrix `D P` is an
integer. The scalar diagonal 11/24 has reduced denominator 24, not 960; its
integer diagonal in `960 P` is 440. Off-diagonal entries require the larger
full-matrix denominator. The cover projector analogously has leverage 35/64,
full-projector denominator 320, and integer diagonal 175.

## The certified coordinate action

The runner's adjacency cost sums the same four-coordinate L1 rule over all
four coordinates. It therefore makes no spatial-versus-tick distinction. The
runner constructs the 384 signed coordinate relabellings obtained by
permuting those four coordinates and independently flipping them. All 384
induce distinct permutations of the 192 pieces and carry both the 15800
cuttings and the 192 exact covers onto themselves (C1, C2).

The ladder of blocks on the 192 pieces:

| relabellings | what they are | blocks on the 192 pieces |
| --- | --- | --- |
| 24 | proper turns of a chosen first three coordinates | 8 of 24 |
| 48 | those, with the fourth-coordinate flip allowed | 4 of 48 |
| 96 | all signed relabellings that keep the fourth coordinate in place | 2 of 96 |
| 384 | all four-coordinate permutations and flips | 1 of 192 |

Read down this chosen subgroup ladder: the 192 pieces fall into eight orbits
of 24 under proper turns of the first three coordinates, four orbits of 48
once the fourth-coordinate flip is allowed, two orbits of 96 under all signed
coordinate relabellings that keep the fourth coordinate in place, and one
orbit under all 384 signed coordinate relabellings. Thus the explicitly
constructed 384-element subgroup is transitive, which is all the projector
argument needs (C3). The runner does not compute the full automorphism group,
so no claim of completeness or exact identification with every symmetry of
the incidence systems is made.

## The visibility matrix, exactly

Write the cutting-by-piece table as a matrix on the 192 pieces, one row per
cutting, and let `P` be the orthogonal projector onto the span of its rows.
`P` is a rational matrix on the 192 coordinates. Its diagonal entry is that
coordinate's leverage score, called algebraic visibility here, and the
diagonal sums to the rank. This definition is distinct from incidence
frequency.

The rank over the rational numbers is 88, and the row lattice is saturated:
two independently chosen 88 by 88 minors both have absolute value 1, which
forces every invariant factor to be 1 (C4). The cover side is the same
statement at rank 105 with 105 by 105 minors of absolute value 1.

The runner certifies `N = 960 P` as an exact matrix of whole numbers. A
floating-point inverse proposes the simplex inverse table and is checked
immediately by exact integer multiplication (C0). The modular projector step
likewise only proposes the lift; what certifies that lift is arithmetic over
the whole numbers, carried out in Python integer arithmetic so nothing can
overflow:

- `N` is symmetric.
- `N N = 960 N`, which is the projector identity cleared by 960.
- applied to the selected basis rows, `N` returns 960 times them, so it fixes
  the span it is supposed to fix.
- `trace N = 84480`, which is 960 times 88.

Its entries run from -121 to 440 and take 23 different values. Every one of
the 192 diagonal entries is 440, and 440 times 192 is 84480 (C5, C6). The
cover side is certified the same way at multiplier 320 and rank 105: trace
33600, which is 320 times 105, with every diagonal entry 175, entries from
-42 to 175, and 23 different values (C12).

## Why algebraic visibility is forced

The argument is two lines once the previous two sections are in hand.

A relabelling that carries the row set onto itself acts on the pieces by a
permutation matrix that commutes with the projector onto the span of those
rows, because it carries that span onto itself. A permutation matrix
commuting with `N` moves the diagonal of `N` along its own blocks, so the
diagonal is constant on each block. All 384 relabellings carry the row set
onto itself and `N` is unchanged by every one of them (C7). The 384 have one
block. So the diagonal is constant everywhere.

A constant diagonal on 192 pieces summing to 88 leaves no freedom: every
entry is 88 over 192, which in lowest terms is 11 over 24. The same two lines
on the cover side give 105 over 192, which is 35 over 64.

Both hypotheses are load-bearing, and the runner shows it by taking each one
away in turn.

Take away the one block. Two of the four blocks of the 48, taken as two
indicator rows with multiplier 96, give a row set that is carried onto itself
by the 48 but not by the 384. Its projector has rank 2, and its diagonal is 0
on 96 pieces and 2 on the other 96 — two values, not one, even though 96
times the rank over 192 is the whole number 1 (C8). With four blocks instead
of one, constancy fails.

Take away the row set being carried onto itself. The indicator of one single
piece, a coordinate vector rather than a table row, with multiplier 1, has
rank 1 and a diagonal that is 1 at that one piece and 0 at the other 191
(C9). The 384 still have one block; the diagonal is still not constant,
because this row set is not carried onto itself. Neither hypothesis is idle.

## The full-projector denominator and the Gram exponent

The exact integer matrix `N = 960 P` has entry gcd 1. Reducing all entries of
`N/960` therefore gives common full-matrix denominator
`960/gcd(960, gcd(N_ij)) = 960`; this excludes every smaller positive clearing
integer, not merely a list of candidates. The checks that 192, 320, and 480
leave noninteger entries are additional controls (C10). The same exact gcd
reduction gives full-projector denominator 320 on the cover side, with 64 and
160 as non-clearing controls (C12).

On each side this full-projector denominator equals the largest invariant
factor of the selected basis Gram matrix: 960 on the cutting side, whose chain
has 42 nontrivial factors, and 320 on the cover side, whose chain has 41
(C13). Equivalently, it is the exponent of the explicitly defined finite
abelian group `Z^k / G Z^k`, where `G = B B^T`; no broader lattice-gluing
interpretation is needed here.

The equality has an algebraic proof independent of the invariant-factor
routine. For a selected integer row basis `B`,

    P = B^T (B B^T)^(-1) B.

Therefore the denominator of `P` divides the denominator of `G^(-1)`. C13
also certifies a unit minor of each selected `B`, so `B` has an integer right
inverse `C` with `B C = I`. Consequently

    G^(-1) = C^T P C,

and the reverse divisibility holds. In Smith normal form, the least integer
clearing `G^(-1)` is the largest invariant factor of `G`. Hence the two
denominators are equal. Saturation is load-bearing: the line through (1, 2)
is saturated and gives 5 against 5, whereas the line through (2, 0) is not
saturated and gives Gram factor 4 against projector denominator 1 (C14).

The two sides are not two separate tables whose agreement is a coincidence,
and this note does not claim they are. Gate C17 checks, entry by entry over the whole
numbers, that

    3 N2 = 960 I - N + 5 J

with `N2 = 320 Q`, `I` the identity on the 192 coordinates, and `J` the
all-ones matrix. Dividing by 960 gives the claimed linked-projector identity

    Q = I - P + J/192.

This identity is itself the self-contained explanation of the relation. C17
also certifies `P 1 = 1`. Thus `I-P` is the orthogonal projector onto
`ker(P)`, while `J/192` is the orthogonal projector onto the all-ones line,
which lies in `im(P)` and is orthogonal to `ker(P)`. Their sum is therefore
the projector onto `ker(P)` plus the all-ones line. Since the runner already
certifies that `Q` is the cover row-space projector, the cover row space has
exactly that decomposition. Its rank follows as
`105 = 192 - 88 + 1`, and transitivity then gives leverage 35/64. The
coefficients are fixed by `960/320 = 3` and `960/192 = 5`; the C17 control
with `4 J` fails.

## Runner

`physical_cell_cutting_visible_fraction_cycle760_2026_08_09.py` rebuilds the
object from the cell complex up and gates eighteen quantities, printing
`TOTAL: PASS=18 FAIL=0`. All definitions needed for the construction are
restated in this runner; no sibling runner or repository data file is read.
Exact ranks and determinants are computed by fraction-free elimination; basis
rows are selected over a prime field and the resulting whole-number identities
are then checked exactly in Python integer arithmetic.

- C0 the object: exact simplex inverses, 15800 cuttings, 192 pieces, 24 pieces
  to a cutting, 1975 cuttings through a piece (incidence 1/8), 192 exact covers.
- C1 the 384 relabellings exist, are pairwise distinct, and permute the 192
  pieces; they come from the 16 corners of the four-cube.
- C2 each of the 384 carries the 15800 cuttings onto themselves and the 192
  covers onto themselves. Control: one of them followed by a swap of two
  pieces does not.
- C3 the four rungs of the ladder: 8 of 24, 4 of 48, 2 of 96, 1 of 192.
- C4 saturation on both sides: 88 by 88 and 105 by 105 minors of absolute
  value 1, two independent choices each.
- C5 the cutting-side certificate: symmetric, `N N = 960 N`, fixes the rows,
  trace 84480.
- C6 every one of the 192 diagonal entries is 440, so every coordinate has
  leverage score 11/24.
- C7 `N` is unchanged by every one of the 384 relabellings.
- C8 control: two blocks of the 48 with multiplier 96 give rank 2, kept by
  the 48 and not by the 384, diagonal 0 on 96 pieces and 2 on 96.
- C9 control: one piece's indicator with multiplier 1 gives rank 1 and
  diagonal 1 at one piece, 0 at the other 191.
- C10 exact gcd reduction makes 960 the least full-projector clearing
  multiplier on the cutting side; 192, 320 and 480 each leave noninteger entries.
- C11 `N` is constant on each of the 104 classes of ordered piece pairs and
  takes 23 different values.
- C12 the cover side: certificate at rank 105, diagonal 175, trace 33600,
  leverage 35/64, exact full-projector denominator 320 with 64 and 160 leaving
  noninteger entries, constant on the same 104 classes, 23 values.
- C13 the selected Gram bases have unit-minor saturation witnesses; their
  largest invariant factors are 960 with 42 nontrivial on the cutting side and
  320 with 41 on the cover side.
- C14 control: the saturated line agrees at 5 and 5; the line that is not
  saturated gives 4 against 1.
- C15 control: the invariant-factor routine returns 1 6 from the diagonal
  2 3 and 2 12 from the diagonal 4 6, which are not its own entries.
- C16 elapsed and peak memory, both measured in the run.
- C17 the tie `3 N2 = 960 I - N + 5 J` over the whole numbers, `N` times the
  all-ones vector equal to 960 times it, and 192 - 88 + 1 = 105. Control:
  the same identity with 4 J in place of 5 J fails.

Measured totals: 18 gates, `TOTAL: PASS=18 FAIL=0`, elapsed under 300 s, peak
resident memory under 500 MB, stdout under 6000 characters.

## Imports and derived surface

### Imports (load-bearing)

- the in-runner definitions of the sixteen binary four-cube corners,
  unimodular five-corner pieces, the symmetric four-coordinate adjacency
  cost, minimum-cost exact cuttings, eight-piece exact covers, and rational
  orthogonal-projector visibility;
- ordinary integer, rational, finite-group, and linear-algebra identities used
  explicitly in the proof above.

There are no external scientific inputs, no ancestral runner imports, and no
load-bearing repository-file reads.

### Derived

- all finite counts and orbit sizes listed under Runner;
- ranks 88 and 105, leverage scores 11/24 and 35/64, and full-projector
  denominators 960 and 320;
- the two selected Gram invariant-factor chains and their largest factors;
- `Q = I - P + J/192` and the resulting cover-row-space decomposition.

## Boundary

- **Everything here is a count about one finite object.** The cutting system
  is a finite combinatorial object and every statement made about it is a
  count or a whole-number identity between counts. Nothing here bears on any
  physical claim.
- **A transitive subgroup is proved; completeness is not.** The 384 signed
  coordinate relabellings form an explicitly constructed transitive subgroup
  preserving both row sets. The full automorphism group is not computed.
- **Algebraic visibility is not incidence or volume.** The projector diagonal
  is a coordinate leverage score. Ordinary cutting-incidence frequency is
  1/8. Neither quantity is a physical fraction of a material piece.
- **960 is a full-matrix denominator, not the denominator of 11/24.** The
  scalar leverage has reduced denominator 24. The value 960 is the least
  integer clearing every projector entry; no geometric subdivision of a piece
  is asserted.
- **The relation between sides is self-contained.** The exact identity
  `Q = I - P + J/192`, together with `P 1 = 1`, proves the stated row-space
  decomposition without an imported blind-space result.
- **Saturation is checked by a sufficient condition.** A minor of absolute
  value 1 proves the lattice is saturated; failing to find one would prove
  nothing. Every witness reported here succeeded, so the asymmetry does not
  bite, but it bounds what the technique could be used to deny.
- **No emergent-time interpretation is made.** The cost in this runner is
  symmetric in all four binary coordinates. Calling one coordinate a tick is
  only a presentation choice for the displayed subgroup ladder.

## Next

Three things are open and reachable from here.

Which of the 23 entry values of `N` sit on which of the 104 classes of
ordered piece pairs. `N` is constant on every class, so the 23 values
partition the 104 classes, and the shape of that partition is a direct next
measurement.

Whether the explicitly constructed order-384 subgroup is the full
automorphism group of either incidence system. Nothing in this package
computes or claims that larger-group question.

The structure behind the Gram discriminant groups. The cutting side has 42
nontrivial invariant factors and the cover side 41, with the two largest
being 960 and 320. A decomposition of the 192-dimensional space that named
those parts one by one would say what the exponent counts, which is the
question the full-projector denominator leaves open.

## Review record

On 2026-08-09 this packet was narrowed to remove reliance on the unavailable
Cycle-759 dependency and to drop the unsupported claim that the constructed
384-element subgroup is the full automorphism group. The surviving surface is
only the self-contained bounded theorem on the finite object rebuilt here:
the projector leverages and full-matrix denominators, the saturated-Gram
comparison, and the linked-projector identity. The primary runner is
self-contained, so there is no helper-runner mapping or other hard landing
condition.
