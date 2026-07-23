# Physical paired-neutral gauge compiler discriminator — Cycle 635 (2026-07-23)

Status: bounded science discriminator; authority none; audit unset; author
artifact status accepted false.

This cycle tests whether pairing every one of the six Cycle-230 fermion
occupations with a local spectator occupation removes the remaining compiler
wall when the pair is fed into the Cycle-235 higher-form/BKSF map.  It does
not claim a physical-site compiler.  The strongest result is an exact
fixed-sector code and a local *relative* occupation map conditional on a
supplied gauge vacuum.  It is not full compiler closure.

## Exact target and construction

For an `N=L^3` torus, take two copies of the Cycle-235 dual graph and add one
rung at each of its `6N` mode vertices.  The physical register therefore has

`2(15N)+6N = 36N`

M2 factors, or 36 M2 per coarse cell.  Data and spectator vertex parities are
locked by local checks

`C_v = B_data,v B_spectator,v = +1`.

The `6N` displayed equality checks have rank `6N-1`: their product vanishes,
so there is exactly one relation.  The two copied graph layers plus rungs have
bounded loop/square rank `24N-2`; adding the three Wilson rows gives
`24N+1`.  The fixed-sector code count is consequently

`36N - (24N+1) - (6N-1) = 6N`.

The runner executes these ranks on L3/L6/L7.  It also deletes a redundant
displayed equality, an independent equality-basis row, and one Wilson row.
The redundant deletion leaves rank unchanged; either independent deletion
reduces rank by one.  Unequal local data/spectator words are rejected.  These
controls distinguish a real dependency from a duplicated-row count.

With an already prepared all-plus spin state `Omega_spin`, the relative map

`E|n> = product_v T_rung,v^(n_v) |Omega_spin>`

is local in the CSS-equivalent ladder presentation: a rung flux toggles data
and spectator vertex signs together and preserves the local equality and loop
checks.  This is an explicit relative basis map, not a bounded preparation of
`Omega_spin`.

## Intermediate occupation sign and physical support

The occupation-pair isometry is executed as an `8 -> 64` matrix on three
logical modes.  A nonadjacent endpoint-only paired swap has Frobenius residual
`2 sqrt(2)` and fails basis words 011 and 110.  Multiplying it by

`(-1)^[n_middle (n_left xor n_right)]`

restores the intermediate occupation CAR sign: the intertwining and code
leakage residuals are zero at machine precision.  Thus the endpoint shortcut
is rejected rather than credited.

Mapping the exact parity correction through the displayed graph gives maximum
support 112, 340, and 448 M2 factors on L3, L6, and L7 respectively.  The
algebraic correction is exact, but this realization is not bounded uniformly
in system size.  An isolated adjacent two-mode paired exchange does have an
exact bounded intertwiner; that smaller test is not promoted to the complete
Cycle-230 stream.

## Same-code onsite and state fixtures

The six-mode onsite coin is factored into explicit paired-basis phase and
two-level even-CAR factors, reconstructed, deletion-tested, and then assigned
its bounded doubled-graph image on at most 42 incident edge/rung M2 factors.
The contact phase is diagonal on the same paired basis.  Both use the same
fixed-sector code as the rank test.  This closes a bounded macro-operator
statement; literal one- or two-M2 primitive lowering is still open.

The one-particle fixture remains available as one local paired flux and keeps
the Cycle-219 mass equality.  The original L3 principal sea has rank 73; its
paired representative has 146 occupied physical modes and even combined
charge.  This is state-domain availability, not autonomous state preparation.

## Proper-cubic covariance

All24 proper-cubic frames act by permutation on both graph copies and the
rungs.  Every local loop, ladder square, and equality constraint maps into its
own family, while the three-Wilson fixed span is preserved.  The runner also
checks all576 ordered frame compositions at every L3 M2 role.  The all-plus
spin-sector label is frame invariant.  The fixed-order parity interval used by
the exact stream correction is not translation-free, so covariance of the
constraints does not turn that correction into a bounded stream compiler.

## Route dispositions

Route A, fixed-Wilson paired face/edge flux: partial positive.  It has exact
logical exponent `6N`, one relation in the paired equality family, a local
relative `E`, and bounded onsite coin/contact.  It still needs the supplied
gauge vacuum, and its executed full CAR sign repair has growing support.

Route B, local-only rough/subsystem reading: negative at route scope.  With
only bounded loop, ladder-square, and paired-equality rows, the code exponent
is `6N+3` on each tested size.  The equalities do not select the three
topological characters.  Calling them unspecified gauge data does not provide
one map `E`; cutting the periodic graph changes the declared seam and
translation problem.

The comparison point is Cycle 532, which already has a conditional full-Fock
algebra at 22 M2 per cell, bounded `B`, onsite, and contact words, and both
matter parity sectors.  Its remaining typed wall is preparation of three
topological spin signs.  These three topological characters are not selected
by the paired equality rows.  Cycle 635 uses more physical factors, lacks a bounded
complete stream, and retains those same signs.  Paired neutrality therefore
repackages rather than improves that wall.

## Exact receipts and residuals

The companion receipt records:

- common fixed-code and local-only ranks for L3/L6/L7;
- the equality dependency and deletion controls;
- exact pair-isometry, intermediate-sign, coherent-state, and leakage norms;
- the 112/340/448 mapped-support discriminator;
- the onsite factor word, factor-deletion signal, mass, and rank-73 fixtures;
- all24 constraint images and all576 composition checks;
- the complete supplied-structure inventory and route dispositions.

Numerical equality uses tolerance `3e-10`.  The run has a 300-second and 3-GiB
declared cap.

## Supplied structure and interpretation firewall

Supplied structure is: two labeled copies of the Cycle-235 graph; six rungs
per cell; data/spectator roles and equality signs; the CSS-equivalent framing;
three all-plus Wilson character labels; `Omega_spin`; a fixed Fock tensor
order; the exact middle-parity word; the Cycle-230 coin, beta, contact coupling,
factor order and precision; periodic L3/L6/L7 domains; and a future assignment
of each 36-role macro block to physical M2 sites.

The supplied spin vacuum is not a bounded `E`.  The relative rung map is not
state preparation.  A bounded even-algebra onsite word is not a full compiler.
An endpoint swap is not the actual CAR stream.  A factor schedule is not
causal time.  Wrapped phase is not physical energy, a group element is not a
rate, and a spectator copy is not a Record.  No axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit status is edited.

## No-go-discipline N1–N8

No broad impossibility or minimum-content claim ships.  The narrow positive
rank and conditional-encoding result ships with the following firewall.

N1 — normalized alternatives.  Attempted families are the fixed-Wilson paired
ladder, the exact intermediate-sign stream, the paired onsite even-algebra
word, the local-only subsystem reading, and an open/rough-cut comparator.
Cycle 532 is included as ruled-out-by-prior only for the narrower claim that
the bounded full-Fock algebra itself still needs discovery.  Live families
include direct spin-character preparation, auxiliary Majorana/link codes,
tensor pull-through codes, dissipative preparation with resource accounting,
and periodic topology repair.

N2 — wall independence.  The named walls are bounded stream support,
spin-vacuum preparation, literal primitive lowering, fine-site placement, and
a periodic rough repair.  Every directional pair is marked
`NOT_ESTABLISHED`; no conjunction is treated as an independent obstruction.

N3 — hidden-wall scan.  The note states every supplied graph, role split,
constraint sign, framing choice, Wilson label, spin vacuum, Fock order,
middle-sign rule, local law, domain, precision, and placement obligation.  A
machine phrase scan is part of the receipt.

N4 — residual matching.  Each inherited result records `same_scope`,
`exact_match`, and `use_as_closure`.  Cycle 235 closes the graph/rank slice;
Cycle 248 supplies the paired isometry but not stream locality; Cycle 532 and
Cycle 622 identify the same three-character initialization residual; Cycle 628
is retained only as a distinct non-diagonal comparator.

N5 — resolution rhetoric audit.  Each shipped sentence is expanded at
`per_element`, `per_site`, `per_mode`, `per_block`, and `lattice_wide`
resolution in the receipt.  This prevents a bounded onsite macro from being
silently promoted to a bounded lattice update.

N6 — partial closures.  Every pinned parent is listed with status and
`what_closes`: graph/rank, paired state map, conditional full-Fock algebra,
homology accounting, or the non-diagonal route boundary.  None closes spin
preparation plus stream plus primitive lowering together.

N7 — steelman.  A local measurement/reset or resource-accounted dissipative
law could prepare the three character signs, and an auxiliary
Majorana/subsystem representation could carry incident-edge Clifford signs
without the displayed parity surface.  The actionable terminal test is one
same code with bounded `E`, bounded stream/coin/contact, literal M2 lowering,
L3/L6/L7 and all24/all576 checks, with no supplied Wilson character.

N8 — cross-cycle echo.  Doubling retires Cycle 235's lost parity-dimension
slice, but Cycle 248's sign surface and the Cycle 532/Cycle 622 three-character
initialization residual survive.  Those echoes define the next constructive
tests; they are not a theorem about all auxiliary encodings.

The broad-negative, minimum-content, shared-obstruction, and axiom-pressure
gates remain `FAIL / DO NOT SHIP`.  There is no axiom pressure.  The optimal
next campaign is to attack Cycle 532's three spin characters directly with a
bounded measurement/reset protocol, a resource-accounted dissipative
preparation, or a translation-respecting periodic topology repair, then demand
literal M2 primitive lowering before adding more occupation spectators.
