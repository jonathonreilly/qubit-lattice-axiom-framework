# Two cells side by side: what a seam costs when the long axis is spatial

Date: 2026-08-04

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted. Cycle 728 of the emergent-geometry lane.

Primary runner:
[`scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py`](../scripts/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.py)
(65 PASS / 0 FAIL, fail-closed).
Canonical primary cache:
[`logs/runner-cache/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.txt`](../logs/runner-cache/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04.txt).
Primary receipt:
[`outputs/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_spatial_block_seam_dichotomy_cycle728_2026_08_04_receipt_2026-08-04.json).

Independent checker:
[`scripts/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04.py`](../scripts/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04.py)
(15 PASS / 0 FAIL, fail-closed), with canonical cache
[`logs/runner-cache/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04.txt`](../logs/runner-cache/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04.txt)
and receipt
[`outputs/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04_receipt_2026-08-04.json`](../outputs/physical_spatial_block_seam_dichotomy_cycle728_independent_check_2026_08_04_receipt_2026-08-04.json).

## Supplied model and premise boundary

Every result below is a theorem of a **supplied finite structural model**, not
of the framework axioms alone. The supplied model chooses a coordinate box,
five-corner normalized-volume-one simplex pieces, an all-pairs adjacency charge,
and a dissection rule based on exact interior disjointness and volume filling.

- The **Lattice** axiom of
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  the spatial `Z^3` nearest-neighbour adjacency used to grade pairs and the 24
  proper cubic rotations.
- The registered
  [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  supplies only equal tick/edge graining. It supplies no cell selection and no
  rule-to-tick correspondence.
- The corner-simplex/dissection structure and charge are declared inputs. The
  physical tick–Admissibility realization bridge and the identification of
  physical assembly cells with pairwise-adjacency simplices remain open.

The landed
[`PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md`](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md)
is prior authority for the same supplied one-cell model and its `[108,128]`
bracket. This package also reconstructs that bracket locally before using it.

## What this settles

Take two lattice cells side by side and carry them through one tick. Cut the resulting
box into minimal pieces and charge each piece for the pairs of its corners that sit more
than one step apart in space. Two facts about that cost are settled here, both without a
solver anywhere in the artifact.

First, within the supplied model, **a dissection that respects the seam between
the two cells costs between 216 and 256**, and both ends are attained. The lower
end follows from a certificate that holds on
every one of the 2672 minimal pieces of a single cell at denominator 2, the upper end from
a certificate at denominator 3, and both certificates are checked here piece by piece
rather than taken on trust. Respecting the seam means no piece straddles it; the note
shows that this condition is equivalent to the piece lying inside one closed cell, so a
seam-respecting dissection *is* a pair of one-cell dissections and its cost is the sum of
two one-cell costs.

Second, **every global cost maximizer crosses the seam.** An explicit 48-piece
dissection is exhibited that costs 318, verified here to be a genuine dissection — every
piece of volume one, every one of its 1128 pairs separated by an integer normal produced
on the spot — and 318 sits above 256. Thirty-one of its 48 pieces cross the seam. Thus no
seam-respecting dissection can maximize the cost. A seam-respecting dissection attains
216, but the global minimum is not proved: a seam-crossing dissection below 216 remains
open. The global maximum is pinned from above by a ceiling certificate over 1080
piece orbits, carried at denominator 12 and checked against every one of the 17280 minimal
pieces, gives 324. The dearest dissection of this box therefore costs between 318 and 324,
where the bound available from the charge alone is 432.

A third result is structural rather than numerical. **No dissection is invariant
under the carried order-16 group** consisting of the proper-spatial block stabilizer
and tick reversal. An invariant dissection
would be a union of whole piece orbits, all orbits have size 16, and 48 pieces over orbits
of 16 leaves exactly 3 orbits. Only 23 of the 1080 orbits can appear in any exact cover at
all, and a direct sweep over triples of those 23 finds none that covers every sample point
exactly once. This excludes invariance under that entire carried group; it does not
classify which proper subgroups an individual dissection may preserve. Since the full
coordinate symmetry group contains the carried group, full-group invariance is excluded
as a corollary, but the order-16 group is never called the full box symmetry group.

## Objects

The supplied box is `{0,1,2} x {0,1} x {0,1}` in space and `{0,1}` in tick:
24 corners, spatial volume 2. Normalized lattice 4-volume is
`|det(v_1-v_0,...,v_4-v_0)|`, or `4!` times Euclidean volume. Its minimal pieces
are the 5-corner subsets of unit normalized volume; there are
17280 of them, and a dissection into minimal pieces uses 48. A single cell, `{0,1}` in each
of the four coordinates, has 16 corners, 2672 minimal pieces, and 24 pieces per dissection.
Every number quoted for the single cell is measured in the same artifact, so nothing about
it enters as a supplied constant.

Three charges are read on the same pieces:

- the **spatial adjacency charge**, counting corner pairs whose separation in the three
  spatial coordinates exceeds one step. Its range on minimal pieces is 3 to 9.
- the **transposed charge**, counting separation in the tick together with the two short
  spatial coordinates instead. Its range is 3 to 7.
- the **long-axis span charge**, counting pairs separated by more than one step along the
  long spatial direction. Its range is 0 to 4.

The two authority links above supply adjacency, proper rotations, and equal
tick/edge graining only. The coordinate box, simplex piece class, dissection rule,
and charge convention are supplied by this theorem's declared model.

## Method: certificates and witnesses, no solver in the artifact

A **floor certificate** is an integer weight `u` per piece orbit together with an integer
constant `Z` and a denominator `D`, such that on every minimal piece the orbit weights it
meets, summed and offset by `Z`, stay at or below `D` times its charge. Summing that
inequality over the pieces of any dissection gives a lower bound on the cost, and the bound
depends only on `u`, `Z`, `D` — not on the dissection. A **ceiling certificate** reverses
the inequality and bounds the cost above. Both are verified here by direct integer
arithmetic against every piece.

The certificate needs the sample points it is written over to be generic. Rather than hope
for that, the weights are built to force it: the largest barycentric integer any corner
sees on any piece is measured first, and the corner weights are then chosen superincreasing
and large enough that no barycentric coordinate of a sample point can vanish. The artifact
then checks the consequence directly — zero boundary incidences over all 17280 pieces — so
every sample point lies in the interior of exactly one piece of any dissection, and the
bound holds with no symmetry assumption at all. Symmetry is used to shrink the certificate,
never to justify it.

A **witness** is an exhibited dissection. Each is checked three ways: every piece has
volume one, the volumes sum to the box, and every pair of pieces carries an integer normal,
produced on the spot, that separates them. Volume plus pairwise separation is already an
exact cover, so no solver is needed to certify a witness either.

The cost-108 one-cell witnesses are the monotone stencils: for each of the 24 orderings of the
four coordinates, the piece spanned by the corresponding monotone corner path. The
higher-cost carried witnesses are explicit piece lists. Their author-side search provenance is not a
retained regularity claim; only the piece lists and the properties recomputed from them
enter the result.

## Results

**The seam is a real barrier in the charge, not just in the geometry.** A piece with span
zero sits inside one closed cell; there are 5344 such pieces, and they are exactly two
translated copies of the 2672 one-cell pieces with the charge unchanged by the translation.
Their charge spectrum is the one-cell spectrum doubled. The remaining 11936 pieces all
reach from one face of the box to the other, and the cheapest of them costs 5 where a
confined piece can cost 3. Crossing the seam costs at least two extra, piece by piece.

**One cell brackets exactly at [108, 128].** The floor certificate holds on all 2672 pieces
with least slack zero and equality on 1984 of them, and its value is exactly 108. The
ceiling certificate holds with least slack zero and equality on 944, value exactly 128. Two
witnesses attain the two ends. Stacking each of them over the two cells gives block
dissections at exactly 216 and exactly 256, both with no seam crossings at all — so the
seam-respecting bracket [216, 256] is attained at both ends.

**The carried attained values span [216, 318].** The trivial counting bounds —
48 pieces times the least and greatest charge a single piece can carry — are 144
and 432; both carried values sit strictly inside. This is not a global-minimum
statement. The global floor is open. The 318 witness exceeds the exact
seam-respecting ceiling 256, which proves the maximizer-seam exclusion.

**The block maximum is bracketed at [318, 324].** A ceiling certificate over the block's
own 1080 piece orbits, carried at denominator 12, holds on every one of the 17280 minimal
pieces with least slack zero and equality on 1200 of them, and its value 3888 over 12 gives
324. The 318 witness sits six below that. The bound available from the charge alone — 48
pieces times the greatest charge a single piece can carry — is 432, so the certificate
removes most of the trivial slack without closing the window.

**The two charges part company on the 318 dissection and agree on the 216
stencil.** The
same 48 pieces of the 318 dissection read 238 under the transposed charge. On the stacked
stencil the two charges agree exactly, at 216. That agreement is structural,
not a coincidence: the stencil is built from all 24 orderings of the four coordinates, so
exchanging the long spatial axis with the tick permutes its 24 pieces among themselves, and
the two charges are then forced equal — 108 both ways on one cell. The cost-128 one-cell
dissection has no such symmetry: the same exchange moves it, and its two charges read 128
against 116. Neither charge dominates the other across the piece set — spatial is the
larger on 12208 pieces and the smaller on 1952 — so the two are genuinely different
functions that happen to coincide on this coordinate-permutation-invariant witness.

**A denominator divisibility condition follows from the carried certificate
form.** A block certificate value is
`16 T + 48 Z`, with `T` the sum of the orbit weights and `Z` the constant, so it is always
a multiple of 16; the bound it gives is that value divided by `D`. A bound of `c` therefore
needs 16 to divide `c D`: a bound of 216 forces `D` even, and a bound of 324 forces `D`
divisible by four. The certificate carried here has `D = 12`. This condition is
necessary for this exact point-orbit form; it does not exclude sharper bounds at
another denominator, with other weights, or from another point family.

## Independent reconstruction and hostile controls

The landed independent checker imports no primary implementation. It reads the
primary's carried integer witnesses and multipliers from the Python AST, then uses
a separate exact determinant expansion, adjugate inverse, group construction,
incidence builder, and witness verifier. Its 15 gates reconstruct:

- all 42,504 five-subsets, 17,280 block minimal pieces and 2,672 one-cell
  minimal pieces, with the full volume and charge spectra;
- the confined/crossing split `5,344/11,936` and least piece charges `3/5`;
- the one-cell certificate bracket `[108,128]`, the block ceiling `324`, and
  the exact witnesses `216/256/318` with transposed cost `238` and 31 crossing
  pieces for the last;
- the carried order-16 action, 1,080 size-16 piece orbits, 23 eligible orbits,
  and zero exact-cover triples;
- a second generic sample chamber with different superincreasing weights,
  again zero boundary incidences, 23 eligible orbits, and zero exact-cover
  triples.

Hostile mutations lower the tight block ceiling constant, strengthen both
zero-slack one-cell certificates, and duplicate a simplex in the 318 witness.
Each mutation is detected. A separate review mutation changing the expected 318
charge to 319 makes the primary runner exit nonzero, exercising its fail-closed
contract.

## Boundary and honest read

**No global floor is carried.** The theorem proves the seam-respecting minimum
216 and exhibits a global value 216. It does not prove 216 is the global minimum;
a seam-crossing dissection below 216 remains open. No failed certificate search is
retained as evidence or promoted to an impossibility.

**The block maximum remains a six-unit window.** The carried certificate gives
324 and the carried witness gives 318. Another certificate, point family,
denominator, or witness may close that window; none is excluded.

**Regularity is not claimed.** The 318 piece list is certified as an exact
dissection with attained cost 318. Its author-side lifting/search provenance is
not a retained lower-hull certificate and does not enter the theorem.

**The symmetry exclusion is exact but narrow.** It quantifies over invariance
under the entire carried order-16 proper-spatial-stabilizer-times-tick-reversal
group. It does not classify invariant dissections under proper subgroups, orbit
structures under another group, or other boxes.

**Two conventions are choices, and both are named.** The charge counts corner pairs
separated by more than one lattice step; the pieces are minimal in normalised volume. Both
use the lattice adjacency, but neither the all-pairs charge nor the simplex piece
class is forced by it.

Nothing here derives a metric, curvature, field equation, physical assembly cost,
arbitrary-box law, thermodynamic limit, or continuum statement. Those readings
require the open physical bridges and/or new domain work.

## Artifacts

The linked primary and independent runners, canonical caches, and generated
receipts at the top of this note are the complete evidence surface. The primary
prints `TOTAL: PASS=65 FAIL=0`; the independent checker prints
`TOTAL: PASS=15 FAIL=0`. Certificate weights and witness lists are carried data
and are verified, not derived, by the primary. The independent checker reconstructs
their claimed implications through separate code.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — spatial nearest-neighbour
  adjacency and proper cubic rotations only.
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) —
  equal tick/edge graining only.
- [Cycle 725 exact one-cell bracket](PHYSICAL_EXACT_ADJACENCY_DISSECTION_BRACKET_CYCLE725_NOTE_2026-08-03.md) —
  prior authority for the supplied one-cell model and `[108,128]` bracket. The
  present package nevertheless reconstructs the bracket locally.

The predecessor Cycle 726 and Cycle 727 branches are ordering context, not
scientific imports: no source, certificate, witness, or numerical result from
either is consumed here.

## Proof-obligation disposition

CONDITIONAL. The finite combinatorial implications are closed on the supplied
model: the seam-respecting bracket, maximum window, maximizer-seam exclusion,
and carried-group invariant-cover exclusion all have exact certificates or
exhaustive finite censuses. Any physical reading is conditional on the two open
bridges named above. The global floor and the six-unit maximum gap remain open.

## Review record

The submitted branch passed its own 65 gates, but review found five material
scope/evidence defects: it called 216 a global least while later admitting no
global floor, called the carried order-16 subgroup the full box group, promoted
an uncarried lifting search to regularity, promoted a finite failed certificate
search to an impossibility, and exited zero on failed gates. The repair makes the
runner fail closed, generates its receipt, adds canonical input-bound caches and
an independent 15-gate reconstruction, declares the supplied-model and premise
boundary, and narrows every result to the exact finite evidence. The submitted
cold transcript is replaced by canonical runner caches. No audit verdict is
authored or applied.

## No-Go Discipline Gate

This is the committed N1–N8 record for two exact finite exclusions that survive
review: (A) no global maximizer can be seam-respecting, because every such
dissection costs at most 256 while an exact dissection attains 318; and (B) no
dissection is invariant under the entire carried order-16 group, because every
such dissection would be a three-orbit exact cover and the exhaustive census has
zero such triples. No universal `no_go` claim ships. The primary cache contains
the required five-line N5 resolution certificate.

**N1 — Alternative route enumeration.** Every route uses the `ATTEMPTED`
marker and is executed in the landed runners.

1. `ATTEMPTED` — seam-factorization attack: all 17,280 pieces are classified;
   span zero is equivalent to confinement in one closed cell, and the 5,344
   confined pieces are exactly two translated one-cell censuses.
2. `ATTEMPTED` — seam-ceiling attack: independent exact one-cell floor/ceiling
   certificates reconstruct `[108,128]`, so factorization gives `[216,256]`.
3. `ATTEMPTED` — witness-validity attack: two separately written exact
   verifiers show the 318 list has 48 unit-volume pieces, volume 48, and all
   1,128 piece pairs separated; its charge is independently 318.
4. `ATTEMPTED` — orbit-size/stabilizer attack: the carried group is rebuilt
   from coordinate maps; all 16 maps are distinct, close on the 24 corners,
   and partition all minimal pieces into exactly 1,080 size-16 orbits.
5. `ATTEMPTED` — missed-cover attack: the full primary-chamber incidence
   census filters all 1,080 orbits to 23 candidates and exhausts all candidate
   triples, returning zero exact covers.
6. `ATTEMPTED` — sample-chamber attack: an independently implemented second
   generic chamber with different weights again has zero boundary incidences,
   the same 23 candidates, and zero exact-cover triples.

These routes are distinct in primary object and terminal obligation:
factorization, dual ceiling, primal witness, group action, exhaustive exact-cover
census, and independent chamber reconstruction.

**N2 — Wall-independence audit.** The six open walls are GF (global floor),
MX (close the 318–324 maximum window), TR (physical tick–Admissibility bridge),
SI (physical simplex identification), DE (other boxes/repeated domains), and PS
(classification under proper subgroups or alternative acting groups). Every
unordered pair is audited below; “first→second” and “second→first” answer whether
closing one automatically closes the other.

| pair | first→second | second→first | independent? | reason |
|---|---|---|---|---|
| GF–MX | no | no | yes | a lower-bound certificate does not sharpen a maximum, and a maximum witness/certificate does not lower-bound all covers |
| GF–TR | no | no | yes | finite-model optimization and physical rule-to-tick realization are different obligations |
| GF–SI | no | no | yes | a model floor neither selects physical simplices nor follows from that selection |
| GF–DE | no | no | yes | one-block minimization does not classify other domains, or conversely |
| GF–PS | no | no | yes | cost minimization and subgroup stabilizers are independent finite questions |
| MX–TR | no | no | yes | closing a model maximum does not realize a physical tick |
| MX–SI | no | no | yes | the maximum window and physical cell identification do not imply one another |
| MX–DE | no | no | yes | exactness on this block does not extend the domain |
| MX–PS | no | no | yes | maximum cost and partial-symmetry classification are separate censuses |
| TR–SI | no | no | yes | rule-to-tick correspondence and cell-shape identification are distinct bridges |
| TR–DE | no | no | yes | a physical tick bridge does not prove arbitrary-box combinatorics |
| TR–PS | no | no | yes | physical realization does not classify finite stabilizers |
| SI–DE | no | no | yes | identifying one physical cell shape does not prove domain extension |
| SI–PS | no | no | yes | cell identification and subgroup classification are distinct |
| DE–PS | no | no | yes | domain extension does not decide acting-group stabilizers, or conversely |

No wall follows from another, so the collapsed set remains six.

**N3 — Hidden-wall scan.** “By construction” occurs only for the generic point
weights and is backed by the measured barycentric bound plus zero boundary
incidences. “Framework supplies” has been replaced by the explicit three-part
premise ledger above. The coordinate box, volume normalization, simplex class,
all-pairs charge, acting group, and two physical bridges are all explicit.
“Box symmetry” was narrowed to the carried order-16 group. No background,
canonical, natural, obvious, or standard-QFT premise remains hidden.

**N4 — Residual matching.** The witnesses match their residuals exactly:

| finite exclusion | landed witness | residual tested | match? |
|---|---|---|---|
| maximizer cannot respect seam | one-cell dual ceilings plus exact 318 primal witness | `max(seam-respecting) <= 256 < 318 <= max(all)` | yes |
| no carried-group invariant dissection | 1,080 size-16 orbit census, 23 eligible, zero exact-cover triples | invariance under the entire declared order-16 action on this one block | yes |
| chamber robustness | independent second point family | same finite invariant-cover residual under a different generic chamber | yes |

The uncarried lifting search and failed certificate ladder are dropped as
witnesses; neither supports a retained negative.

**N5 — Rhetoric audit.** The exact resolution record lands in primary cached
stdout: `per_element` covers every minimal piece and certificate inequality;
`per_site` covers only the supplied one- and two-cell coordinate boxes;
`per_mode` is not executed because the model has no mode decomposition;
`per_block` covers the complete declared witness/certificate/orbit census; and
`lattice_wide` is not executed, with no lattice-wide negative asserted. All
headings and conclusions use the narrowest tested resolution.

**N6 — Partial-closure path scan.** GF can close through a valid global lower
certificate or a lower witness plus proof; MX can close through a stronger upper
certificate or witness; PS can close by repeating the exact cover census for
named subgroups/alternative groups; DE closes by rebuilding the finite proof on
new domains. TR and SI may be explicit imports in a consuming bounded theorem
and later retired by theorem/audit. The registered kinetic-isotropy primitive
supplies equal graining only and silently closes neither physical bridge. No new
axiom is declared necessary.

**N7 — Steelman.** The strongest hostile response is that a seam-crossing
dissection may cost below 216, a different certificate family or denominator may
lower 324 to 318, and individual dissections may preserve substantial proper
subgroups even though none preserves the entire carried group. Those are concrete
routes and remain open as GF, MX, and PS. They do not challenge the two narrow
finite exclusions: neither a lower-cost seam-crossing cover nor partial symmetry
can make a seam-respecting cover exceed 256 or create a three-orbit cover under
the full carried action.

**N8 — Cross-cycle echo.** Cycle 725 previously required this lane to distinguish
the supplied corner-simplex model from physical assembly, to price negative
statements to carried point families, and to keep domain extension open. This
repair carries that boundary forward rather than turning one failed certificate
search or one coordinate box into a universal obstruction. Its second-chamber
check directly answers the closest prior chamber-dependence failure mode.

**Status: PASS.** All eight checks are answered; all six N1 routes are
`ATTEMPTED`; the full N2 pair table lands; the N5 resolution certificate lands in
the primary cache; and no failure condition or universal no-go remains.
