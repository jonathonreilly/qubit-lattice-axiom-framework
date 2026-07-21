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

## Factor-local seven-M2 descriptor and overlap countercontrol

Let the six port M2s owned by one cell factor have Z operators \(Z_v\), and
let \(Z_\tau\) act on the new tag.  Before neighboring cell factors are
multiplied in, one local factor obeys the parity descriptor

\[
C_\tau=Z_\tau\prod_{v\in\operatorname{star}(L)}Z_v=+1.
\]

The corrected runner checks the complete local M64 grammar, \(n=0,\ldots,6\):
3,072 factor terms per size, 256 at each cell, with zero parity failures at L5
and L6.  On the anchor, deleting any one port produces exactly 72 failures.
This establishes an exact seven-M2 **factor-local descriptor**.

It is not a constraint on the final overlapping code.  Neighboring cell
representatives act on the same nominal anchor-port M2s.  Multiplying one
occupied cell factor by the canonical vacuum factors at the other eleven
cells gives 1,080 exact branches for each endpoint.  Ninety branches per
endpoint violate \(C_\tau=+1\), identically at L5 and L6.  For example, an
odd carrier choice at the right center can flip the left-center port parity
while the logical left number remains zero.

There is also an information-theoretic countercontrol.  If \(W\) is any fixed
unitary applied to the native encoding and blank auxiliaries, then

\[
 (W(E\otimes|0\rangle))^\dagger W(E\otimes|0\rangle)=E^\dagger E.
\]

Thus post-processing the already-collided native row cannot create two
different tag values for the Cycle-518 doubleton.  The independently appended
logical tag still proves the static isometry above, but its local preparation
must occur before the distinguishing factor information is lost, or a
different global constraint/representative must be constructed.  Cycle 519
does neither.

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
schedule.  Recurrent overlap consistency, tag preparation before factor
collapse, and update compatibility across several adjacent patches remain
terminal tests.

The resource theorem actually proved is therefore conservative: one extra
M2 per oriented adjacent-center patch, branch support increased by at most
one, a factor-local parity descriptor supported on seven M2s, reversal
supported abstractly on the tag plus the endpoint parity labels, and logical
seam transport supported on the tag plus two occupation controls.  No
globally enforced seven-M2 constraint is part of the theorem.  Per-center
reuse may reduce the global overhead, but that reduction is not a Cycle-519
theorem.

## Deletion, comparator, and lawful-domain controls

Deleting or freezing the dedicated tag restores the complete Cycle-518
defect: 24 native doubletons, 6,144 expanded row collisions, and exact Gram
residual \(1/400\).  Replacing \(p_L\) by bond parity
\(p_L\oplus p_R\) separates zero of the 24 doubletons.  Deleting any one port
factor from the seven-M2 factor descriptor yields 72 local-term failures over
the full M64 grammar.  The overlap countercontrol then finds 90 final-product
violations per endpoint, so this deletion test must not be read as constraint
enforcement.  Treating the tag as a scalar under true reversal violates two
of four abstract parity-labelled states.

The lawful domain remains L=5 and held L=6, the exact twelve distinct cells
in the Cycle-517 adjacent-center patch, all 24 determinant-+1 cubic frames,
and global total number at most two.  L=4 is rejected because of the extra
periodic wrap edge.  Duplicate centers, nonadjacent centers, determinant--1
frames, and \(N>2\) are rejected.  No boundary or thermodynamic-limit claim
is inferred.

The corrected revision-2 target certificate passed all 12 gates in 28.843
seconds with maximum RSS 280,281,088 bytes and process swap count zero.  This includes the
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
> encoding is exactly isometric.  The independently appended tag transforms
> covariantly under all 24 anchored proper-cubic frames and the displayed
> endpoint-reversal cocycle, and is preserved by the tested logical
> free-plus-contact seam transport.  The seven-M2 parity relation holds for
> isolated cell factors but fails as a final overlapping-code constraint in
> 90 of 1,080 exact single-occupied-cell branches per endpoint.

The supplied inventory is explicit:

| supplied item | imported role | not proved here |
|---|---|---|
| Cycle-311/315 local M64 branches | face representatives, carrier sums, stream slice, amplitudes | primitive generation from bare M2 laws |
| Cycle-515/516 dense-star shell | product grammar, Koszul/frame bridge | tagged controlled update inside that shell |
| Cycle-517 patch | twelve-cell geometry, 15-edge anticommutation graph, 24 anchored frames | recurrent volume tiling |
| Cycle-518 quotient | vacuum-toggle orbit criterion, exact native doubletons and \(1/400\) deletion residual | any universal obstruction |
| logical coin exterior lift | local-number preservation | autonomous primitive realization |
| onsite contact diagonal | occupation preservation | primitive contact synthesis |
| logical occupation controls | pre-swap \(n_a,n_b\) supplied to the tag rule | physical controls exposing them before overlap information is lost |
| independent tag preparation | append \(\tau=N_L\bmod2\) before product-row collision | any local preparation or final-code constraint realizing that append |

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
   bounded static encoding and logical free-plus-contact transport.  The
   simple seven-M2 relation is then falsified as a final overlapping-code
   constraint, so tag preparation remains supplied.
4. **Opposite-carrier representative — ATTEMPTED.**  The independent bounded
   comparator gives singleton fibers with zero added M2 but changes the
   branch grammar and must re-earn the older fixtures.
5. **Post-encoding six-port parity fanout — ATTEMPTED / NARROWLY
   FALSIFIED.**  Unitary Gram invariance preserves all 24 native doubletons,
   and the exact overlap countercontrol has 90 final-port parity failures in
   1,080 branches per endpoint.
6. **Pre-overlap factor-local tag write — OPEN / LIVE.**  The full local M64
   parity descriptor and commuting six-CNOT algebra are positive, but no
   reversible factor-preparation interface retains the tag through the
   overlapping product yet.
7. **Reuse a free per-cell r role as the tag — ATTEMPTED.**  The narrow
   attempted reuse does not separate the native doubletons because the
   relevant vacuum role is quotiented exactly where it is free.
8. **Changed non-stabilizer faces — UNTESTED / LIVE.**  A local face-path
   representative could separate the fibers without an added tag but must
   preserve the local column and frame bridge.
9. **Edge- or plaquette-flux role — UNTESTED / LIVE.**  A relational bounded
   gauge character may encode the endpoint parity with different recurrence
   properties.
10. **Autonomous staggered schedule — PRIOR PARTIAL / LIVE.**  A four-state
   scalar cursor gives a conditional host-free C/A/B/contact macrocycle and
   the orbit-wide decorated stream is frame covariant, but tag preparation,
   final-code enforcement, cursor synchronization, and primitive decorated
   gates remain open.

The two successful bounded constructions alone rule out a broad negative
claim.  The four untested families additionally prevent any minimum-content
claim about one extra M2.

### N2 — wall-independence audit

After closing the static separation defect, the surviving walls collapse to:

- **W_prepare:** prepare the independent tag before overlapping-factor
  information is lost, or construct a genuine final-code local constraint;
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
| W_prepare / W_update | no | no | yes |
| W_prepare / W_recur | no | no | yes |
| W_prepare / W_prediction | no | no | yes |
| W_update / W_recur | no | no | yes |
| W_update / W_prediction | no | no | yes |
| W_recur / W_prediction | no | no | yes |

The primitive physical mass retest is downstream validation of W_update, not
an independent wall.  Static injectivity, exact normalization, the
factor-local parity descriptor, and logical transport are closed only on the
bounded domain.  Final-code constraint identification is explicitly open.

### N3 — hidden-wall scan

The packet does not hide an ordering, parity service, scheduler, vacuum
choice, or continuum bridge.  Every imported object is listed in the supplied
inventory.  “Covariant” is split into anchored 24-frame covariance and true
same-bond reversal, with the latter carrying an explicit cocycle.  “Local” is
split into factor-local and final-code claims; the countercontrol prevents
their conflation.  “Preserves” refers to the logical tagged code; primitive
physical realization is explicitly open.  The preferred
per-center architecture is labelled a proposal, not a certified recurrent
compiler.

### N4 — residual matching

Cycle 517 supplies only the adjacent-star geometry, anticommutation graph,
and anchored frame witnesses.  Cycle 518 supplies the exact native quotient
defect and its \(1/400\) residual.  Cycles 311/315 supply the local branch
grammar; Cycles 515/516 supply only the dense-star product and frame/Koszul
bridge.  None of those cycles is cited as a physical tagged update or
recurrent compiler.  No response/source, time, Born, Record, or prediction
residual is used to close a Cycle-519 wall.  The corrected negative matches
the same native encoding exactly: fixed-unitary postprocessing retains its 24
doubletons and \(1/400\) residual, while the L5/L6 full-product witness gives
90/1,080 failures per endpoint.  It is not generalized to other encodings.

### N5 — rhetoric audit

“All rows” means all 245,518,336 analytic branch rows generated by the native
grammar on this exact twelve-cell, global-\(N\leq2\) domain.  “Exact isometry”
means the structural identity Gram on its 2,629 columns.  “Seven-M2 parity”
means a factor-local descriptor and explicitly not a global code constraint.
“Update” means the exhaustive logical occupation/tag rule plus inherited
FSWAP phase, not a bare-M2 law.  “Mass preserved” refers to the explicit tagged logical
one-particle matrix; the primitive physical realization remains untested.  No
“minimum,” “necessary in every
compiler,” or constitutional language follows.

### N6 — partial-closure path

Cycle 519 itself is the partial-closure witness: one bounded parity tag closes
the entire static Cycle-518 collision residual without changing the native
branch grammar.  The opposite-carrier comparator closes the same residual by
a different primary object.  The next constructive path is to synthesize a
tag write while the distinguishing factor-local information still exists, or
find a different global constraint, then test shared per-center reuse on three
or more overlapping stars.  None of these steps requires an axiom revision.

### N7 — hostile steelman

A hostile reviewer must reject this as a physical compiler because the tag
cannot be computed by post-processing the already-collided native row and the
seven-port descriptor fails on exact overlapping products.  The runner also
reads logical occupations to update the tag rather than deriving physical
controls.  The dense on-image lift may hide a nonlocal implementation, and
one independent tag per oriented patch
may become inconsistent or unnecessarily expensive under recurrent overlap.
The opposite-carrier route may ultimately dominate by avoiding the added M2.
These objections keep W_prepare, W_update, and W_recur live; they do not
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
| \(C_{\rm num}\) | advanced: logical center-number parity is retained as an explicit bounded tag; the full local M64 factor grammar has the exact parity descriptor | prepare the tag before overlap information loss or find a final-code constraint; widen the adjacent-star theorem beyond global \(N\leq2\) |
| \(C_{\rm wrap}\) | unchanged; L4 wrap alias remains rejected | recurrent/boundary/thermodynamic controls |
| \(C_{\rm int}\) | advanced at logical level: contact and all eleven seam transports preserve the tagged code, and the explicit tagged one-particle mass fixture passes | primitive physical controlled tag update and physical mass retest |
| \(C_{\rm local}\) | advanced but corrected: exact bounded static isometry, 24-frame covariance, and reversal cocycle; the proposed seven-M2 final constraint is falsified | local tag preparation/final-code enforcement, primitive update, and overlapping per-center reuse |
| \(C_{\rm source}\) | unchanged | autonomous source/response bridge and new prediction |

The optimal next campaign is an information-retention-and-recurrence
tournament.  First, write the tag while each cell factor's number parity is
still locally available, or construct an alternative final-code constraint
that survives overlapping multiplication; post-processing the collided row
is ruled out exactly.  In parallel, instantiate one shared per-center tag on
the smallest three-star overlap, require genuine simultaneous final-code
constraints, all proper-cubic placements, seam-order independence,
leakage/deletion controls, and a direct
primitive physical one-particle mass retest against the now-explicit logical
fixture.  Keep the opposite-carrier comparator alive as the
zero-new-M2 branch-grammar route.  Only after one route supplies an actual
primitive \(G_{\rm physical}\) should the campaign connect it to the open
response/source and prediction bridges.
