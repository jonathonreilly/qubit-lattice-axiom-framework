# Color Orientation Three Vs Threebar From Succession: Candidate Conditional Bounded Theorem

**Date:** 2026-07-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set, predict, or apply an audit outcome.
**Primary runner:** [`scripts/color_orientation_three_vs_threebar_succession_candidate_2026_07_06.py`](../scripts/color_orientation_three_vs_threebar_succession_candidate_2026_07_06.py)
**Cache:** [`logs/runner-cache/color_orientation_three_vs_threebar_succession_candidate_2026_07_06.txt`](../logs/runner-cache/color_orientation_three_vs_threebar_succession_candidate_2026_07_06.txt)

## Summary
This bounded theorem note separates the exact algebraic fact that `3` and `3bar` are inequivalent for `su(3)` from the open question of what, if anything, supplies the orientation choice in the record framework.
The named premises are:
```text
SUPPLIED-C3:
at each site under discussion, a three-complex-dimensional color carrier is
supplied as endpoint data. This premise is inherited from prior color notes
and is not derived here.

ARROW:
a realized succession structure (a directed arrow on the record extension
order) exists. The four axioms do not supply this: the axiom memo itself
places "arrow, record-production dynamics, physical persistence dynamics,
time metric" outside axiom content, and extension order is mathematical
inclusion, not derived dynamics.

SUCCESSION-ORIENT:
conditional on comparability AND on ARROW, the arrow supplies the two-valued
orientation datum that chooses the supplied carrier as 3 rather than 3bar,
or conversely.
```
The exact content is:
```text
SUPPLIED-C3
  => 3 and 3bar are inequivalent complex-linear su(3) modules.
SUCCESSION-ORIENT plus comparability
  => candidate supplier for the orientation datum.
ANOMALY-CANCEL plus given 3-content
  => a 3bar partner cancels the cubic anomaly contribution.
```
The four axioms do not by themselves supply `C^3`, comparability, the succession-to-orientation bridge, anomaly cancellation, a gauge dynamics, or a physical color identification.

## The texts in play
The current axiom memo sets the admission discipline:

> "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise."

The Record axiom supplies formation and permanence:

> "Records form."

and:

> "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent."

Those sentences give the extension partial order on record configurations once configurations are compared by inclusion of permanent records. They do not by themselves decide total comparability.
The comparability one-pager is meta owner-surface context only:

> "This document carries no weight until you act on it; cite only as proposed."

It proposes the owner sentence:

> "There is one configuration of records."

This note's working shorthand for the comparability condition (shorthand,
not a source quote) is: of any two states, one extends the other. The
one-pager's own wording for the open content is:

> "**comparability**: that any two realized configurations are nested -- one
> world-line of records, rather than incomparable realized alternatives."

Its own status sentences (quoted; the pager is a routing/decision surface,
not an approval surface):

> "Comparability is not derivable from the current sentences."

with the decision framed as "Whether to append one sentence" and option
"(B) Leave it open" among the owner's choices. Comparability is therefore an
undecided owner surface; everything conditional on it below stays
conditional.

The graded-constraint program memo records the owner status as:

> "OPEN owner question; the arrow's only missing piece"

That status is meta program framing only, not authority.
The same memo gives the record-influence criterion as meta program framing:

> "Pre-record structure is real exactly to the extent it influences which records form and with what frequencies."

It also gives the succession/orientation program sentence as meta framing:

> "Orientation is not a separate insertion. With a growth direction (arrow) and a one-sided spectrum (stability clause on the carrier), the rotation sense is fixed relative to record succession."

and:

> "Nobody chooses `i` over `-i`; the pair is oriented by succession plus stability."

This note does not consume those memo sentences as authority. They set the owner/program target that SUCCESSION-ORIENT would need to satisfy.
The May-2 anomaly note is quoted as unaudited target/context only:

> "**Status:** independent audit required. This note is a candidate closing
> derivation for the parent"

Its claim sentence is quoted here in ASCII transcription, with `3bar` replacing the source overbar glyph:

> "Under P1+P2+P3, the SU(3) representation content of the RH (anti-)quark sector is forced to be exactly 2 LH-Weyl fermions in the 3bar representation, with no irreducible 3-rep fields and arbitrary number of singlets."

Claim-strength note: the May-2 source claims MORE than this note consumes --
it also asserts a "unique minimal-field-count anomaly-cancelling RH
completion" including minimality under higher-dimensional irreps, and an
SM identification of the fields. This note consumes NONE of that: it
recomputes only the sign arithmetic `A(3) = -A(3bar)` and the pair
cancellation, and takes the quoted sentence as unaudited target/context for
that arithmetic alone.

This note does not consume the May-2 row as authority. The runner recomputes the anomaly sign arithmetic self-contained.

## T1 -- Exact 3-vs-3bar inequivalence and the su(2) control
**T1 (exact, runner-verified):** Assume SUPPLIED-C3. Let the supplied carrier be the fundamental complex three-dimensional module for `su(3)`, represented on a rationally rescaled antihermitian Gell-Mann basis. The conjugate action is
```text
A -> -A^T.
```
The complex-linear intertwiner space
```text
{ W : W A = (-A^T) W for every basis generator A }
```
is exactly zero.
The runner solves the exact linear system over `Q[i]`, represented as real and imaginary `Fraction` pairs. Its result is:
```text
su3_nullity = 0.
```
Therefore the distinction between `3` and `3bar` is real representation-theoretic structure on a supplied `C^3` carrier, not a convention removable by a complex-linear change of basis.
The control gives the check teeth. For `su(2)`, using the three antihermitian Pauli generators and the same conjugate rule `A -> -A^T`, the exact nullspace has complex dimension one:
```text
su2_nullity = 1,
epsilon = [[0, 1], [-1, 0]].
```
The runner verifies directly that `epsilon A = (-A^T) epsilon` for every `su(2)` basis generator. Thus `2 ~= 2bar` while `3 != 3bar`.
Consequently, choosing `3` versus `3bar` on the supplied carrier is a
two-valued orientation datum. Scope note: the runner-verified fact is the
COMPLEX-LINEAR inequivalence only (nothing is claimed or checked about
real-linear or antilinear equivalence). The following two sentences are
definitional remarks, not runner-verified claims: the two choices are
related by an antilinear (conjugation) map, and in this note "T-odd" means
exactly that a supplied orientation datum is exchanged with its opposite by
the corresponding antiunitary reversal. No reversal action, antiunitary map,
or T-odd criterion is constructed or checked here; no time-reversal dynamics
is imported.

## T2 -- Candidate succession supplier, conditional on comparability
**T2 (conditional named premises; nothing here is a theorem):** The Record
axiom supplies formation and permanence. What that yields mathematically is
at most the INCLUSION partial order on record configurations (a static
extension order) -- NOT a succession relation, time index, successor map, or
physical arrow. Three separate open conditions gate this section:
comparability (whether any two realized configurations are nested -- the
undecided owner surface quoted above), ARROW (whether a realized directed
succession structure exists at all -- open; the axiom memo places the arrow
outside axiom content), and SUCCESSION-ORIENT itself (whether that arrow,
if it exists, supplies the T1 orientation datum).
Under those open conditions, SUCCESSION-ORIENT is the candidate bridge: the arrow, a preferred direction on the extension order, supplies the orientation datum of T1.
This bridge is NOT derived here. It is the named premise SUCCESSION-ORIENT. The quoted graded-memo orientation sentence is meta program framing only, not authority for the bridge.
The record-influence burden remains open. By the program's own meta criterion, a grading or orientation supplier that influences no record statistics is not real by that program standard. Whether SUCCESSION-ORIENT influences any record statistics, and with what frequencies, is not proved here.

## T3 -- Exact cubic-anomaly sign anchor
**T3 (exact anchor, runner-verified):** Define, on the same rationally rescaled Gell-Mann basis, the third-order symmetric trace tensor `D_R(a,b,c) = tr(({T_a,T_b}) T_c)`. The anomaly coefficient `A(R)` is the proportionality scalar against the fundamental tensor, `D_R = A(R) D_3`.
The runner computes this exactly over `Q[i]` for the fundamental and conjugate Hermitian generators. It verifies:
```text
D_3bar = -D_3,
D_3 != 0,
A(3) = +1,
A(3bar) = -1,
A(3) + A(3bar) = 0.
```
One exact nonzero witness in the runner's rational normalization is `D_3(0,0,7) = 4`.
This anchors only the anomaly bookkeeping. Given already-supplied `3` content and an anomaly-cancellation requirement, named here as the supplied condition ANOMALY-CANCEL, the `3bar` partner is forced as a consistency partner for cancellation. This is not a derivation of the orientation datum, not a derivation of ANOMALY-CANCEL, and not a physical identification of any field.

## Residuals and scope boundary (not a T-claim)
- R-succession-orient: SUCCESSION-ORIENT is an open named premise. The succession-to-orientation bridge is not derived here.
- R-comparability: comparability remains an undecided owner surface (see the pager's own quoted sentences). All T2 content is conditional on it.
- R-arrow: the succession/arrow structure itself is open -- extension order is inclusion, not dynamics; the axiom memo places the arrow outside axiom content. This is a separate premise from SUCCESSION-ORIENT, and T2 needs both.
- R-influence-burden: whether SUCCESSION-ORIENT influences record statistics is open.
- R-reversal-burden (stated self-contained; no external row consumed): by T1's own algebra the two orientation choices are exchanged by an antilinear map, so any genuine supplier must distinguish them in a way that is odd under the corresponding reversal and must not reduce to a pure convention/gauge choice. Whether any candidate meets this is open; this note does not close it.
- R-anomaly-cancel: anomaly cancellation is a supplied condition, ANOMALY-CANCEL, not axiom content and not derived here.
- R-supplied-c3: SUPPLIED-C3 is inherited and remains supplied rather than derived.

## Honest boundary
This note does not derive the `C^3` carrier, does not derive color from the four axioms, does not decide comparability, does not derive ARROW (no succession relation, time index, or dynamics is derived from formation plus permanence; extension order is mathematical inclusion only), does not derive SUCCESSION-ORIENT, does not establish that succession is T-odd, does not establish record-statistical influence for the orientation supplier, does not derive anomaly cancellation, does not identify physical quark fields, does not derive hypercharge or chirality, does not add an axiom, does not add a primitive, does not create Tier-A content, does not apply an audit verdict, and does not decide a landing.

## Citation contract
Citation is gated by the standard discipline: this note is Class C source material with no premise weight until audit ratification; after ratification, citation is at the audited claim scope exactly. Within that gate:
Downstream rows may cite T1's exact inequivalence:
```text
for supplied C^3, Hom_su3(3,3bar) = 0,
while Hom_su2(2,2bar) is one-dimensional with epsilon witness.
```
Downstream rows may cite T3's exact anomaly arithmetic:
```text
A(3) = +1,
A(3bar) = -1,
A(3) + A(3bar) = 0.
```
Downstream rows may cite T2 only as a named-premise candidate:
```text
ARROW and SUCCESSION-ORIENT, both open, conditional on comparability and
still subject to the record-influence and reversal burdens.
```
Downstream rows may NOT cite this note for: orientation as derived; comparability as decided; T-oddness of succession as established; anomaly cancellation as axiom content; a derived `C^3` carrier; physical color identification; quark-field identification; a gauge dynamics; a generator/rate/action package; hypercharge; chirality; or any audit-status upgrade.

## Dependencies table
| dependency | status/boundary used here | consumed content |
|---|---|---|
| [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) | current axiom memo; axioms are premises, not bounded-status sources | quoted formation, permanence, and premise-discipline sentences; no `C^3`, comparability, or anomaly rule imported |
| `GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md` | meta program framing; no theorem claim | record-influence and succession/orientation quotes as context only |
| `RECORD_COMPARABILITY_OWNER_ONE_PAGER_2026-07-04.md` | meta owner decision surface; proposed only | comparability candidate and no-weight quote only |
| `SU3_ANOMALY_FORCED_3BAR_COMPLETION_THEOREM_NOTE_2026-05-02.md` | unaudited target/context | claim target quote only; anomaly signs recomputed here |
| `COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md` | process reference only -- NOT a scientific dependency | formatting/discipline conventions; no technical claim consumed |

## Runner verification map
The runner verifies the exact `su(3)` fundamental-versus-conjugate intertwiner nullspace, the exact `su(2)` epsilon control, the cubic anomaly sign tensor, quote audits for the source snippets used above, and an AST self-scan for no-network/no-subprocess discipline. Expected output shape:
```text
[PASS] ...
DECLARATION premise=SUCCESSION-ORIENT; conditional_on=R-comparability; supplied=SUPPLIED-C3; anomaly_requirement=ANOMALY-CANCEL
EXACT su3_nullity=0 su2_nullity=1 epsilon=[[0, 1], [-1, 0]] ... A3=+1 A3bar=-1 pair_sum=0
TOTAL PASS=... FAIL=0
```
The cache linked in the header is generated from this runner's output.

## Source-note boundary
Hypothesis set: the four current framework axioms as context; the inherited named premise SUPPLIED-C3; the conditional named premise SUCCESSION-ORIENT; comparability as an open condition for T2; the supplied condition ANOMALY-CANCEL for T3; and standard finite-dimensional `su(n)` representation algebra.
Forbidden imports: no derived carrier, no comparability adoption, no record-statistical influence theorem, no T-odd succession theorem, no anomaly-cancellation derivation, no physical matter identification, no gauge dynamics, no generator, no rate, no action, no probability, no weight, no chiral bridge, no hypercharge bridge, no new axiom, no primitive, no Tier-A admission, no parent-row verdict, and no audit decision is imported. This note is a bounded conditional source note for independent review.
