# Physical same-species two-carrier path/sign compiler — Cycle 639 (2026-07-23)

Status: bounded local theorem plus route discriminator. Authority none.
Audit unset. Author artifact status is not accepted.

## Result

Cycle 639 widens the Cycle-632 direct sector to the smallest domain that can
see identical-fermion exchange: exactly two identical carriers of one
Cycle-219 species on the six-direction Cycle-230 torus.  The other two
distinguishable species are omitted so that no spectator label can hide the
exchange sign.  The fixed particle-number sector is supplied; sector genesis
is not derived.

There are two separate results.

First, a positive local theorem: six occupation M2 factors exactly host the
full 15D onsite antisymmetric two-carrier contact space used by Cycle 583,
including its rank-one proper-cubic A2 ray.  Two labeled separated cells use a
4096 by 36 computational-basis isometry for the 36D relative direction fiber.
The onsite exterior coin, separated relative coin, contact phase, inverse,
leakage, deletion, one-particle mass, all24 frames, and all576 frame
compositions pass at machine precision.  This supplies a physical local host
for the Cycle-583 onsite dimer payload.

Second, a route discriminator: the obvious endpoint-local FSWAP does not give
one path-independent cubic CAR stream on that same computational basis.  An
explicit link scratch in a supplied vacuum `|0>` realizes one FSWAP exactly
and returns the scratch, using only support-one and support-two M2 gates.  A
contractible square exchange loop on word `1010` has amplitude `-1`, while
ordinary SWAP gives `+1`.  Thus the new domain sees the exchange sign that the
Cycle-632 one-carrier sector cannot see.

That one-edge success does not survive alternate paths.  On three modes,
direct `FSWAP_13` differs from `FSWAP_12 FSWAP_23 FSWAP_12` by Frobenius norm
`2 sqrt(2)`.  The three occupied-pattern controls are `011`, `101`, and `110`:
`101` agrees at phase `-1`, while `011` and `110` acquire the extra adjacent-
path minus sign.  On a cubic square, the two length-two routes between
opposite vertices disagree on four weight-two words and have restricted norm
`4`.  This is a tensor-order FSWAP inconsistency for the tested encoding, not
a result about every fermionization.

The complete depth-two Cycle-230 stream, including every periodic seam edge,
is then evaluated on every two-carrier basis state.  Endpoint-local FSWAP has
exact failure counts

```text
L3:   4,140 of    13,041
L6: 154,800 of   839,160
L7: 340,452 of 2,116,653
```

An explicit intermediate-occupation parity correction reduces every count to
zero, but its largest ordered interval has support 110, 1082, and 1766 M2
factors on L3/L6/L7.  The associated prefix chain is not invariant under all
proper-cubic frames.  It is therefore an exact nonlocal comparator, not a
bounded compiler result.

The strongest constructive result is the local Cycle-583 A2 physical host,
not a same-species lattice `E G_coarse = G_physical E` theorem.  Cycle 639 is
not full M64.

## Exact local A2 theorem

Let the six physical occupation factors in one coarse cell be ordered only in
the test representation by the six Cycle-210 direction labels.  For every
pair `a<b`, the column of

`E_15 : C^15 -> (C^2)^(tensor 6)`

is the computational word with bits `a,b` occupied.  The runner checks

```text
E_15^dagger E_15 = I_15,
Gamma(C) E_15 = E_15 (J_2^dagger (C tensor C) J_2),
(I-E_15 E_15^dagger) Gamma(C) E_15 = 0.
```

It also multiplies the inverse coin, removes one factor from an explicit
two-level factorization, and deletes the contact.  Both deletion controls have
nonzero signals.  The contact obeys

`W_g E_15 = exp(i g) E_15`

because every lawful onsite word has particle number two.  Vacuum,
one-carrier, repeated assignment of one mode, and three-carrier words are
rejected by the declared local domain.

For separated particles, `E_36` uses two supplied labeled cell slots: left
anchor cell first, right relative cell second, with direction-pair order
`6 a+b`.  Applying the physical 64-state exterior coin independently in the
two cells agrees with `E_36 (C tensor C)`.  This left/right relative reference
is supplied representation data.  It is not a particle identity and cannot
be carried through exchange without the still-open graded stream rule.

The A2 ray maps into the physical 15D code and transforms with the executed
one-dimensional A2 characters.  all24 ray residuals and all576 character and
wedge-representation compositions are checked.  The one-particle mass fixture
is unchanged.  These facts make the local dimer payload suitable for a future
Cycle-612 matter slot; they do not supply seam-complete tick/endpoint hardware.

An unlanded external shore appeared during packaging:
`origin/causal-time/cycle629-a2-line-discriminator-20260722` at commit
`1085e03fddcf8c2ea2575ba27d554aa92c7e7f9f`.  It reports a second finite-box
contact-generated A2 spectral concentration near wrapped phase `+0.30` with
4 PASS / 2 frozen FAIL and held-size, species, isolation, and width still
open.  Cycle 639 takes no scientific credit from that branch.  Algebraically,
`E_15` spans the entire onsite wedge-two space and hence its unique A2 internal
ray, so it necessarily represents the local internal A2 component used by
both reported spectral concentrations.  It does not represent either full
spatial spectral state: that requires the seam-complete lattice stream that
remains open here.  Neither wrapped phase is called energy or clock output.

## Route A — local Z2 link or edge sign carrier

For endpoint occupations `a,b` and a link scratch `q=0`, compute
`q <- q xor (a and b)`, apply `Z_q`, uncompute, and SWAP the endpoints.  The
runner lowers both Toffolis and the remaining gates into 32 support-one/two M2
primitives.  The exact edge intertwiner and leakage residual are zero; deleting
the phase or the uncompute produces a nonzero signal.

The scratch returns after each edge, so it carries no memory of an alternate
route.  It reduces to endpoint-local `CZ SWAP` and consequently has the
three-mode and cubic-square discrepancies above.  A static flat cubic Z2
connection has `+1` plaquette holonomy, whereas the exchange witness requires
`-1`.  Binding a dynamic flux or framing ribbon to each charge could change
that conclusion, but no such local constraint, preparation, or pull-through
law is executed here.  That non-diagonal link/gauge family remains open.

A cumulative prefix-parity auxiliary does reproduce the exterior signs
exactly.  Its local constraint and initial state use a supplied global chain,
and the edge correction reads an interval whose extent grows as
110/1082/1766.  It is recorded as a failed no-preferred-order route rather
than hidden as a parity service.

## Route B — paired/doubled occupation with local equality

The local map `|n> -> |n>_data |n>_spectator` and the data/spectator equality
checks are exact.  An adjacent sequence consisting of data FSWAP plus
spectator SWAP intertwines the three-mode exchange.  Applying the same paired
gate directly to modes 1 and 3 again has residual `2 sqrt(2)`.  Doubling does
not carry the intermediate occupation sign.  The Cycle-635 growing-surface
numbers are listed only as a comparator; no Cycle-635 result is credited as a
Cycle-639 closure.

## Route C — state marker or contractible block

The six-dimensional wedge-two space of four modes embeds in three
computational M2 factors.  The block exterior permutation and exchange phase
are exact, including deletion and malformed labels.  A supplied local `|->`
phase marker can carry the displayed contractible-loop minus sign.

Fixed cell blocks are not preserved by the intercell stream: three undirected
stream bonds per cell cross their boundaries, including periodic seams.  A
single stream-closed direction lane contains `6L` mode roles, so enlarging one
contractible block to close that orbit grows with L.  No local marker-owner,
split/merge, reblocking, or seam rule is supplied.  This is a local block
positive and an unfinished lattice construction.

## Exact sparse, covariance, and lawful-domain controls

For L3/L6/L7, the runner hashes every unordered two-mode computational-basis
column, checks every stream basis action, counts seam-source failures, and
checks the exact ordered repair.  Sparse full coin-stream-contact columns
include an explicit seam input, a preimage of local contact, an onsite pair,
and failing path patterns.  The ordered comparator has zero residual; the
endpoint-local product has a nonzero residual.

The direction and stream permutations, both edge families, and the exterior
two-particle frame action pass all24.  The exterior action passes all576 mode
and pair-sign compositions.  The endpoint-local sign rule fails covariance
against that graded target, while the ordered prefix chain is preserved by
fewer than all 24 frames.  Covariance of edge labels alone is not credited as
covariance of the fermionic physical update.

The lawful Route-A code is Hamming weight exactly two on `6L^3` data M2s,
with every optional link scratch zero.  The Route-B code additionally requires
data/spectator equality.  Dirty link, unequal pair, vacuum, one-carrier,
three-carrier, repeated-mode, deleted-phase, deleted-uncompute, deleted-coin,
deleted-contact, and invalid-block-label controls are explicit.

Supplied structure is: six direction roles per cell; exactly-two sector;
test-only lexicographic serialization; Cycle-230 coin/contact/order and
coupling; periodic L3/L6/L7 domains; optional all-zero link vacuum; the prefix
chain only for the nonlocal comparator; paired equality signs; the
contractible block partition and marker; the left-anchor/right-relative
reference for `E_36`; the Cycle-583 A2 source axis; and the unlanded Cycle-629
branch/commit metadata as an external comparator only.

## Cycle 583 and Cycle 612 boundary

Cycle 583 is pinned and compared without back-credit.  Cycle 639 newly gives
its onsite 15D wedge-two/A2 contact and separated 36D relative coin an actual
bounded computational-M2 host.  It does not inherit Cycle 583's spectral
results as compiler evidence.

This local payload is compatible with the matter slot of the Cycle-612
endpoint packet.  It is not sufficient for the full physical endpoint packet,
because the same code lacks a path-independent seam-complete stream.  The
Cycle-612 clock harness is unchanged and is not rerun.  A factor ordinal is
not a tick, a group element is not a rate, wrapped phase is not energy, and no
Record or proper-time claim is added.

## No-go-discipline N1–N8

No general fermionization impossibility, minimum-content result, shared
substrate obstruction, or axiom-pressure claim ships.

N1 — normalized alternatives.  Six distinct families are recorded: direct
occupation endpoint-FSWAP; cubic Z2 edge connection; ordered prefix parity;
paired/doubled equality; contractible wedge block/state marker; and the
Cycle-532 higher-form rough comparator.  The first five are `ATTEMPTED`.
Cycle 532 is `RULED OUT BY PRIOR` only for repeating its already executed
conditional algebra; its remaining initializer is not used to close this
cycle.  Live routes include twisted charge-ribbon, auxiliary Majorana,
tensor-pull-through, bounded gauge-sector preparation, and overlapping
covariant block codes.

N2 — wall independence.  The named walls are path-independent same-code
stream, auxiliary genesis, cubic covariance without a chain, extension beyond
the fixed sector, and rerunning the full endpoint harness.  Every directional
pair is `NOT_ESTABLISHED`; none is counted as an independent constitutional
wall.

N3 — hidden-wall scan.  Every supplied role, sector, serialization, vacuum,
chain, equality sign, block marker, local law, periodic domain, relative
reference, and A2 axis is inventoried.  A machine phrase scan is part of the
receipt.

N4 — residual matching.  Each citation records `same_scope`, `exact_match`,
and `use_as_closure`.  Cycle 230 matches the intrinsic-versus-M2 stream
residual; Cycle 632 matches the missing exchange witness; Cycle 635 matches
the paired intermediate sign; Cycle 583 closes only the local A2 payload;
Cycle 612 has a different endpoint/clock scope and is not closure evidence.

N5 — rhetoric audit.  Every conclusion is expanded at `per_element`,
`per_site`, `per_mode`, `per_block`, and `lattice_wide` resolution.  In
particular, the one-edge exact gate, local A2 theorem, square disagreement,
and lattice failure counts remain distinct.

N6 — partial closures.  The receipt lists each pinned parent with status and
`what_closes`: target intrinsic CAR law, local A2 target, distinguishable
fixed-sector direct code, paired comparator, or conditional endpoint packet.

N7 — steelman.  A twisted cubic gauge code could bind a locally transported
Z2 flux or framing ribbon to each charge, use plaquette pull-through moves to
identify alternate strings, and prepare the spin sector by a bounded
measurement/reset or dissipative law.  The actionable terminal test is one
computational-basis or explicitly prepared gauge `E` with zero exchange-path
and full-stream residual, bounded support, local genesis, L3/L6/L7 seams,
A2/contact, and all24/all576 on the same code.

N8 — cross-cycle echo.  Cycle 230's physical compiler boundary survives;
Cycle 632's missing exchange witness is retired but reveals the path defect;
Cycle 635's intermediate sign survives pairing; Cycle 583's local physical
payload is retired; Cycle 532's spin-sector repair remains a comparator and a
live possible mechanism.

The broad-negative, minimum-content, shared-obstruction, and axiom-pressure
gates are `FAIL / DO NOT SHIP`.  There is no axiom pressure.  The optimal next
campaign is to construct the twisted cubic charge-ribbon or auxiliary-
Majorana pull-through code and demand exact alternate-path, square exchange,
full seam stream, local vacuum genesis, A2/contact, and all24/all576 results on
one code before any Cycle-612 clock rerun.
