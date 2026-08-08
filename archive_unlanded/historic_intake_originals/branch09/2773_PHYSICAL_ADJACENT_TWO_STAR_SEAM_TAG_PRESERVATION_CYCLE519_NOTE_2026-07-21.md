# Physical adjacent-two-star seam-tag preservation — Cycle 519 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

## Result

Cycle 519 gives a positive bounded repair of the Cycle-518 Gram defect while
preserving the native Cycle-311/315 branch grammar.  On the oriented
twelve-cell adjacent-two-star patch, append one dedicated M2 whose binary
value is

\[
\tau=N_L\pmod 2,
\]

where cell 0 is the anchored left center and \(N_L\) is the number in its six
logical modes.  The tag changes no native face representative, role toggle,
amplitude, or factor order.  It only appends \(X_\tau\) to branches with odd
left-center number.

At train L=5 and held L=6, the exact seed census is:

| item | L=5 | L=6 |
|---|---:|---:|
| excitation seeds | 238,681 | 238,681 |
| \(\tau=1\) seeds | 39,660 | 39,660 |
| tagged quotient fibers | 238,681 | 238,681 |
| singleton fibers | 238,681 | 238,681 |
| maximum fiber | 1 | 1 |
| tagged collisions | 0 | 0 |

The count \(39,660\) is structural: 60 one-particle branches at the left
center plus \(11\cdot60\cdot60=39,600\) split-particle branches with exactly
one occupied left-center mode.  Vacuum and same-cell two-particle seeds have
even left-center number.

Cycle 518 found 24 native doubletons.  The tag splits all 24.  Sixteen have
endpoint-parity sets \(\{(p_L,p_R)=(1,0),(0,1)\}\); eight have
\(\{(1,1),(0,0)\}\).  Hence both left parity and right parity differ across
every doubleton.  This matters under true endpoint reversal.

The quotient proof lifts to all native vacuum-role expansions because the
twelve pure vacuum toggles remain independent and the appended tag is not a
vacuum toggle.  Therefore all 245,518,336 expanded branch rows are unique at
each tested size without literally materializing them.  Exact per-column
branch weights are unchanged:

| logical sector | branches per column | squared branch weight | norm |
|---|---:|---:|---:|
| vacuum | 4,096 | \(1/4,096\) | 1 |
| one particle | 20,480 | \(1/20,480\) | 1 |
| same-cell two particle | 4,096 | \(1/4,096\) | 1 |
| split-cell two particle | 102,400 | \(1/102,400\) | 1 |

Disjoint row support plus those exact normalizations gives

\[
E_\tau^\dagger E_\tau=I_{2629}
\]

on the declared global-\(N\leq2\) code space.  This is an exact structural
identity, not a numerical-tolerance statement.

## Local seven-M2 constraint

Let the six port-occupation M2s at the anchored center have Z operators
\(Z_v\), and let \(Z_\tau\) act on the new tag.  The tagged code obeys the
bounded algebraic constraint

\[
C_\tau=Z_\tau\prod_{v\in\operatorname{star}(L)}Z_v=+1.
\]

Every native local \(n=0,1,2\) gauge term has port-tag parity equal to its
logical number parity.  The runner checks 1,104 terms per size: 92 terms on
each of twelve cells, with zero failures at L5 and L6.  On the anchored cell,
deleting any one of the six port factors produces exactly 15 failures among
92 terms, for every factor and at both sizes.  Thus the tested constraint has
support exactly seven M2s and every port factor is operationally necessary
for this representative grammar.

This is constraint identification, not primitive synthesis.  No Cycle-519
gate constructs a local projector, penalty-free invariant subspace, or
autonomous update whose lawful states are exactly the \(C_\tau=+1\) sector.

## Proper-cubic frames and endpoint reversal

All 24 anchored proper-cubic frames preserve the claim.  A frame fixes the
anchor role, permutes its six ports, and carries the adjacent patch to one of
the six directed-neighbor placements.  The tag is a scalar under this
anchored action because local number parity is invariant.  The runner checks
24 frames at L5 and 24 at L6, plus all 576 frame products, with zero graph or
closure failures.  The inherited Cycle-517 physical frame witnesses are not
modified: the appended tag commutes with their native branch factors.

There is a necessary distinction between an anchored frame that sends the
positive-x neighbor to another directed neighbor and a true reversal of the
same unoriented bond.  The proper-cubic ordered-bond stabilizer has four
elements.  The unoriented-bond stabilizer has eight, split into four
order-preserving elements and a four-element reversing coset.

For a true endpoint reversal, an independently left-labelled seam tag obeys
the exact reversal cocycle

\[
\rho:(p_L,p_R,\tau)\longmapsto
(p_R,p_L,\tau\mathbin\oplus p_L\mathbin\oplus p_R).
\]

On the constrained code, \(\tau=p_L\), so the transformed tag is
\(p_R\), the parity of the new left endpoint.  The runner checks all 64
products in the eight-element stabilizer, 512 tag-action truth-table cases,
32 ordered-tag invariance cases, and the reversal involution, with zero
failures.  Treating \(\tau\) as a scalar under true endpoint reversal fails
on two of the four constrained endpoint-parity states.  The cocycle is
therefore not optional for the one-seam realization.

## Free-plus-contact tag transport

The eleven dynamic seams are the six seams incident on the anchored center
and the five other seams incident on the right center.  The four transverse
Cycle-517 anticommutation rungs are not physical free-stream seams.

The coin exterior lift preserves the number in each cell, so it preserves
\(\tau\).  The onsite contact block is diagonal in occupation and likewise
preserves \(\tau\).  For a free FSWAP on a left-incident seam with pre-swap
endpoint occupations \(n_a,n_b\), the unique local tag rule is

\[
\tau\longmapsto\tau\mathbin\oplus n_a\mathbin\oplus n_b.
\]

The five right-only seam swaps leave \(\tau\) unchanged.  The update uses the
tag plus the two local occupation controls; it has no global parity string,
ordering service, or host-side intervention.

The runner exhausts all 2,629 logical configurations with total number zero,
one, or two:

- 28,919 single-seam checks, with zero tag-constraint failures;
- exactly 142 tag changes on each of the six left-incident seams and zero on
  each of the five right-only seams;
- 2,629 complete eleven-seam schedule checks, with zero failures and 732 tag
  changes;
- 289,190 pairwise order checks across all 55 seam pairs, all 2,629
  configurations, and both input tag values, with zero differences in final
  occupation, tag, or inherited FSWAP phase.

This proves the tagged logical free-plus-contact transport and its pairwise
order independence.  It does not synthesize the required controlled tag-X as
a primitive M2 operation inside the dense Cycle-515/516 branch shell.  A
dense on-image lift can be declared from the exact encoding, but that lift is
supplied structure rather than a primitive compiler.

The runner also constructs the explicit 72-mode one-particle logical update
and its 144-dimensional tagged ambient extension.  The tag embedding and
tagged intertwiner residuals are zero, and the tagged update unitarity
residual is \(6.06\times10^{-15}\).  The uniform tagged one-particle residual
is \(7.07\times10^{-16}\).  The recovered mass is
`0.45340565417488493`, versus the Cycle-219 fixture
`0.4534056541748852`, a residual of \(2.78\times10^{-16}\).  Contact is the
identity in the one-particle sector.  This is a direct tagged logical mass
retest; the primitive physical tagged update and its physical mass retest
remain open.

## Recurrent architecture: preferred, not yet certified

The exact certificate above uses one independently left-labelled tag for one
oriented adjacent-center patch.  For a recurrent lattice architecture, the
preferred construction is one shared per-center star-parity tag

\[
\tau_A=N_A\pmod2
\]

reused on every bond incident on center \(A\).  Its restriction to the tested
patch is exactly \(\tau_0\), and endpoint reversal exchanges the two center
roles instead of manufacturing an unrelated seam resource.  This architecture
has the right locality and overlap shape, but Cycle 519 does not prove that
overlapping seven-cell stars preserve all shared tags under a recurrent
schedule.  Recurrent overlap consistency, simultaneous constraint
enforcement, and update compatibility across several adjacent patches remain
terminal tests.

The resource theorem actually proved is therefore conservative: one extra
M2 per oriented adjacent-center patch, branch support increased by at most
one, static constraint support seven M2s, reversal supported on the tag plus
the twelve endpoint ports, and logical seam transport supported on the tag
plus two occupation controls.  Per-center reuse may reduce the global
overhead, but that reduction is not a Cycle-519 theorem.

## Deletion, comparator, and lawful-domain controls

Deleting or freezing the dedicated tag restores the complete Cycle-518
defect: 24 native doubletons, 6,144 expanded row collisions, and exact Gram
residual \(1/400\).  Replacing \(p_L\) by bond parity
\(p_L\oplus p_R\) separates zero of the 24 doubletons.  Deleting any one port
factor from the seven-M2 constraint yields 15 local term failures.  Treating
the tag as a scalar under true reversal violates two of four constrained
parity states.

The lawful domain remains L=5 and held L=6, the exact twelve distinct cells
in the Cycle-517 adjacent-center patch, all 24 determinant-+1 cubic frames,
and global total number at most two.  L=4 is rejected because of the extra
periodic wrap edge.  Duplicate centers, nonadjacent centers, determinant--1
frames, and \(N>2\) are rejected.  No boundary or thermodynamic-limit claim
is inferred.

The final target certificate passed all 11 gates in 21.694 seconds with
maximum RSS 268,713,984 bytes and process swap count zero.  This includes the
explicit tagged one-particle mass gate.  The ordered tagged
seed-key stream digests were
`18559365b43922f75f7ca69ad3c7b03d82146169f4d5cc5cdb32473d7038c026`
at L5 and
`5780b09f1df16a978c84db50be689bb8b0814ef76df8ae90e0ce061d5e3e1886`
at L6.  The digests need not match across sizes because physical auxiliary
bit positions depend on lattice size; the abstract sector census and
doubleton endpoint-parity signature match exactly.

An independently tested opposite-carrier comparator can also split the
native fibers with no new M2.  It has 10,009 singleton excitation fibers and
10,768,384 full branches and passes its bounded singleton-mask and frame
selector tests.  But it changes branch support and amplitudes, so it must
re-earn the Cycle-311 local column, Cycle-515 dense-star isometry, physical
update, and mass fixtures.  It is a useful live comparator, not part of the
Cycle-519 preservation theorem and not evidence that the seam tag is
minimal.

## Exact claim boundary and supplied structure

The exact positive statement is:

> On the Cycle-517 twelve-cell global-\(N\leq2\) domain at L5 and held L6,
> append one anchored tag \(\tau=N_L\bmod2\) to the native Cycle-311/315
> branch grammar.  The compressed seed census then has 238,681 singleton
> fibers, all 245,518,336 expanded rows are structurally unique, and the
> encoding is exactly isometric.  The code obeys the displayed local
> seven-M2 constraint, transforms covariantly under all 24 anchored
> proper-cubic frames and the displayed endpoint-reversal cocycle, and is
> preserved by the tested logical free-plus-contact seam transport.

The supplied inventory is explicit:

| supplied item | imported role | not proved here |
|---|---|---|
| Cycle-311/315 local M64 branches | face representatives, carrier sums, stream slice, amplitudes | primitive generation from bare M2 laws |
| Cycle-515/516 dense-star shell | product grammar, Koszul/frame bridge | tagged controlled update inside that shell |
| Cycle-517 patch | twelve-cell geometry, 15-edge anticommutation graph, 24 anchored frames | recurrent volume tiling |
| Cycle-518 quotient | vacuum-toggle orbit criterion, exact native doubletons and \(1/400\) deletion residual | any universal obstruction |
| logical coin exterior lift | local-number preservation | autonomous primitive realization |
| onsite contact diagonal | occupation preservation | primitive contact synthesis |
| local occupation controls | pre-swap \(n_a,n_b\) exposed to tag rule | bounded M2 circuit or law exposing them |

The theorem does not yet establish a primitive physical
\(G_{\rm physical}\) satisfying

\[
E_\tau G_{\rm coarse}=G_{\rm physical}E_\tau.
\]

The logical tagged action is exact, and a dense on-image linear extension can
be supplied, but primitive synthesis and off-code lawful completion remain
open.  The explicit tagged logical one-particle update preserves the
Cycle-219 mass fixture to residual \(2.78\times10^{-16}\); a separate primitive
physical mass retest must follow tagged-update synthesis.  Full number,
recurrent overlap, the Cycle-514 response/source bridge, causal time, and the
Born/probability and Record bridges are not imported.

## N1–N8 no-go discipline

Gate status for any impossibility, minimum-content, or axiom-pressure claim:
**FAIL / DO NOT SHIP**.  Cycle 519 is constructive, two materially different
repairs remain live, and no shared substrate obstruction is present.

### N1 — alternative-route map

1. **Native fixed order — ATTEMPTED.**  Cycle 518 found 24 exact overlaps of
   magnitude \(1/400\).
2. **Weighted order character — ATTEMPTED.**  Cycle 518 cancelled sixteen
   overlaps but left eight zero-character pairs of magnitude \(1/400\).
3. **Dedicated anchored seam tag — ATTEMPTED.**  Cycle 519 succeeds on the
   bounded static encoding and logical free-plus-contact transport, subject
   to the primitive and recurrence walls stated above.
4. **Opposite-carrier representative — ATTEMPTED.**  The independent bounded
   comparator gives singleton fibers with zero added M2 but changes the
   branch grammar and must re-earn the older fixtures.
5. **Reuse a free per-cell r role as the tag — ATTEMPTED.**  The narrow
   attempted reuse does not separate the native doubletons because the
   relevant vacuum role is quotiented exactly where it is free.
6. **Changed non-stabilizer faces — UNTESTED / LIVE.**  A local face-path
   representative could separate the fibers without an added tag but must
   preserve the local column and frame bridge.
7. **Edge- or plaquette-flux role — UNTESTED / LIVE.**  A relational bounded
   gauge character may encode the endpoint parity with different recurrence
   properties.
8. **Autonomous staggered schedule — UNTESTED / LIVE.**  A microstep role may
   separate and transport the fibers, but it needs explicit covariance,
   coherent lumpability, and schedule closure.

The two successful bounded constructions alone rule out a broad negative
claim.  The four untested families additionally prevent any minimum-content
claim about one extra M2.

### N2 — wall-independence audit

After closing the static separation defect, the surviving walls collapse to:

- **W_primitive:** synthesize and enforce the seven-M2 constraint from lawful
  primitive M2 operations;
- **W_update:** synthesize the physical controlled tag transport and off-code
  completion, then retest the already-closed logical mass fixture on that
  primitive realization;
- **W_recur:** prove one shared per-center tag is consistent across recurrent
  overlapping stars and autonomous schedules;
- **W_prediction:** connect the compiled matter update to response/source,
  causal-time, and Born/Record prediction bridges.

The pairwise independence audit is:

| pair | same failed object? | does closing either automatically close the other? | separable tests? |
|---|---|---|---|
| W_primitive / W_update | no | no | yes |
| W_primitive / W_recur | no | no | yes |
| W_primitive / W_prediction | no | no | yes |
| W_update / W_recur | no | no | yes |
| W_update / W_prediction | no | no | yes |
| W_recur / W_prediction | no | no | yes |

The primitive physical mass retest is downstream validation of W_update, not
an independent wall.  Static injectivity, exact normalization, constraint
identification, and logical transport are closed only on the bounded domain.

### N3 — hidden-wall scan

The packet does not hide an ordering, parity service, scheduler, vacuum
choice, or continuum bridge.  Every imported object is listed in the supplied
inventory.  “Covariant” is split into anchored 24-frame covariance and true
same-bond reversal, with the latter carrying an explicit cocycle.  “Local” is
accompanied by support counts.  “Preserves” refers to the logical tagged code;
primitive physical realization is explicitly open.  The preferred
per-center architecture is labelled a proposal, not a certified recurrent
compiler.

### N4 — residual matching

Cycle 517 supplies only the adjacent-star geometry, anticommutation graph,
and anchored frame witnesses.  Cycle 518 supplies the exact native quotient
defect and its \(1/400\) residual.  Cycles 311/315 supply the local branch
grammar; Cycles 515/516 supply only the dense-star product and frame/Koszul
bridge.  None of those cycles is cited as a physical tagged update or
recurrent compiler.  No response/source, time, Born, Record, or prediction
residual is used to close a Cycle-519 wall.

### N5 — rhetoric audit

“All rows” means all 245,518,336 analytic branch rows generated by the native
grammar on this exact twelve-cell, global-\(N\leq2\) domain.  “Exact isometry”
means the structural identity Gram on its 2,629 columns.  “Local constraint”
means a seven-M2 algebraic relation, not synthesized enforcement.  “Update”
means the exhaustive logical occupation/tag rule plus inherited FSWAP phase,
not a bare-M2 law.  “Mass preserved” refers to the explicit tagged logical
one-particle matrix; the primitive physical realization remains untested.  No
“minimum,” “necessary in every
compiler,” or constitutional language follows.

### N6 — partial-closure path

Cycle 519 itself is the partial-closure witness: one bounded parity tag closes
the entire static Cycle-518 collision residual without changing the native
branch grammar.  The opposite-carrier comparator closes the same residual by
a different primary object.  The next constructive path is to synthesize a
bounded parity-controlled tag operation and constraint, then test shared
per-center reuse on three or more overlapping stars.  None of these steps
requires an axiom revision.

### N7 — hostile steelman

A hostile reviewer can still reject this as a physical compiler because the
runner reads logical occupations to update the tag and does not derive that
controlled-X from the primitive M2 substrate.  The dense on-image lift may
hide a nonlocal implementation, and one independent tag per oriented patch
may become inconsistent or unnecessarily expensive under recurrent overlap.
The opposite-carrier route may ultimately dominate by avoiding the added M2.
These objections keep W_primitive, W_update, and W_recur live; they do not
undo the bounded static isometry theorem and they forbid a no-go inference.

### N8 — cross-cycle echo

Cycles 311, 315, 515, and 516 repaired apparent branch collisions through
bounded gauge roles, overlap-aware representatives, exact order structure,
and the Koszul frame bridge.  Cycle 518 exposed a new adjacent-star collision
only after those fixes.  Cycle 519 again closes the static defect by retaining
one explicit relational role.  This repeated pattern warns against promoting
an unfinished implementation wall into a substrate obstruction.  The new
scientific burden is primitive synthesis and recurrence, not constitutional
revision.

## TOE dependency ledger and next attack

| wall | Cycle-519 change | remaining exact obligation |
|---|---|---|
| \(C_{\rm ref}\) | unchanged; fixed-Wilson reference structure remains supplied | derive or replace the reference substrate |
| \(C_{\rm num}\) | advanced: local center-number parity is retained as an explicit bounded tag and exact constraint | extend beyond global \(N\leq2\); derive tag initialization/enforcement |
| \(C_{\rm wrap}\) | unchanged; L4 wrap alias remains rejected | recurrent/boundary/thermodynamic controls |
| \(C_{\rm int}\) | advanced at logical level: contact and all eleven seam transports preserve the tagged code, and the explicit tagged one-particle mass fixture passes | primitive physical controlled tag update and physical mass retest |
| \(C_{\rm local}\) | materially advanced: exact bounded isometry, seven-M2 constraint, 24-frame covariance, and reversal cocycle | primitive constraint synthesis and overlapping per-center reuse |
| \(C_{\rm source}\) | unchanged | autonomous source/response bridge and new prediction |

The optimal next campaign is a primitive-and-recurrence tournament.  First,
synthesize the seven-M2 parity constraint and the three-M2 logical tag update
from the allowed local M2 operations inside the native dense shell.  In
parallel, instantiate one shared per-center tag on the smallest three-star
overlap, require simultaneous local constraints, all proper-cubic placements,
seam-order independence, leakage/deletion controls, and a direct
primitive physical one-particle mass retest against the now-explicit logical
fixture.  Keep the opposite-carrier comparator alive as the
zero-new-M2 branch-grammar route.  Only after one route supplies an actual
primitive \(G_{\rm physical}\) should the campaign connect it to the open
response/source and prediction bridges.
