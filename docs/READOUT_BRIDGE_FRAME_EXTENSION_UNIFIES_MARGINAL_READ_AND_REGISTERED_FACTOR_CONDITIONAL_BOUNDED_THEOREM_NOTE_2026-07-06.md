# Readout-Bridge Frame Extension Unifies MARGINAL-READ And REGISTERED-FACTOR: Conditional Bounded Theorem

**Date:** 2026-07-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set, predict, or apply an audit outcome.
**Primary runner:** [`scripts/readout_bridge_frame_extension_unification_2026_07_06.py`](../scripts/readout_bridge_frame_extension_unification_2026_07_06.py)
**Cache:** [`logs/runner-cache/readout_bridge_frame_extension_unification_2026_07_06.txt`](../logs/runner-cache/readout_bridge_frame_extension_unification_2026_07_06.txt) -- supervisor generated from the runner output; this drafting worker does not generate cache.

## Summary
This note is a follow-on to the color-derivation campaign. It does not derive Born weights, does not derive the Born quadratic form, and does not consume adjacent PR #4922, which is scoped to Born weights.

The color campaign introduced two readout-bridge premises with the same shape: records-as-marginals and record-typed factor structure. This note reduces both to one named premise:
```text
FRAME-EXT (four clauses; the premise's full strength lives here):
for each record configuration, the record readout extends to a
(1) content-determined,
(2) nonnegative,
(3) normalized
frame function on the projection lattice of every nearest-neighbor
composite, where (4) the composite domain itself (M_2 tensor M_2 = M_4 and
its projection lattice) is part of what the premise supplies -- the axioms
alone do not assign readout authority over all composite projections.
```

Each clause is load-bearing: without (2) and (3), Gleason gives only a
self-adjoint quadratic representation, not a density operator; without (1),
the represented operator need not be determined by record content; without
(4), the domain of the extension is unowned. The premise count still drops
eight to seven, but honestly only because FRAME-EXT carries these four
clauses inside one named premise.

The reduction chain is conditional:
```text
FRAME-EXT
AND Gleason's theorem on Hilbert spaces of dimension at least 3
  => REP on nearest-neighbor composites
  => the content of MARGINAL-READ
  => the compatibility shape of REGISTERED-FACTOR.
```

This is a reduction, not a discharge. The color campaign's named-premise ledger goes from eight to seven only in this bookkeeping sense:
```text
{MARGINAL-READ, REGISTERED-FACTOR} are replaced by {FRAME-EXT}.
```

The exact open crux is:
```text
FINITE-ADDITIVITY-TO-FRAME gap:
Record additivity is over finite collections of pairwise-disjoint records
that actually occur; FRAME-EXT needs additivity over all orthogonal
decompositions of the composite projection lattice, including mathematical
menus never realized as records.
```

## The texts in play
The current Record axiom supplies content-only readout:
> "Only records are readable. A readout value is determined by record content alone."

It also supplies finite additivity only at realized-record grade:
> "For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`."

The graded-constraint program memo is META program framing only, never authority. Its Gleason target is quoted as orientation only:
> "The form of the weights is a theorem target, not a postulate."

and:
> "If grading exists, is additive over exclusive alternatives, and does not depend on which compatible menu embeds an alternative, then Gleason-type uniqueness forces the quadratic (Born) form."

Its dimension-2 exception sentence is ASCII-normalized here:
> "The known dimension-2 exception is exactly one `M_2` site alone; neighbor composites are `M_4` and above, where the theorem holds -- the lattice, which the axioms supply for free, is what eliminates the loophole."

Its status boundary is also META:
> "This is a theorem target, not a landed result: the landed Class D proposal `docs/GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md` records that any live use must arrive as a fresh, self-contained conditional note through review/audit."

The block-03 color source is an UNLANDED sibling. Its premise definition is quoted verbatim and consumed only as campaign bookkeeping:
```text
MARGINAL-READ (named premise, introduced here): record-visible data about an
edge state is represented at the state level by single-site reduced density
matrices.
```

The block-04 gauge source is an UNLANDED sibling and the format exemplar. Its premise definition is quoted verbatim and consumed only as campaign bookkeeping:
```text
REGISTERED-FACTOR (named premise, introduced here):
the record/readout structure registers a fixed factor subalgebra of the local domain; equivalently, the split
  M_3 tensor I_2 / I_3 tensor M_2
is record-typed data.
```

## Definitions
CONSUME is a record-content consumption map on a nearest-neighbor composite: an assignment of readout values to record content, additive over finite collections of pairwise-disjoint records, content-only, and site-indexed. The additivity and content-only clauses are exactly the quoted Record axiom sentences above.

REP is the representation property for CONSUME on an audited composite domain: there is a content-determined positive unit-trace operator `rho` on the composite such that
```text
readout(P) = tr(rho P)
```
for every projection `P` in the audited domain.

FRAME-EXT is the named conditional premise of this note, with the four-clause statement given in the Summary (content-determined, nonnegative, normalized extension, with the composite projection-lattice domain itself part of the premise). FRAME-EXT is not axiom content and is not established here.

## T1 -- REP implies the two campaign readout-bridge shapes

(T1(a) is exact and runner-verified. T1(b) is convention-strength
bookkeeping, mirroring the block-04 sibling's own framing; it is NOT an
exact theorem and is labeled accordingly below.)
**T1(a) (exact, runner-verified) and T1(b) (convention-strength bookkeeping):** REP implies the content of MARGINAL-READ exactly, and yields the compatibility shape of REGISTERED-FACTOR at convention strength only.

For MARGINAL-READ, take `M_2 tensor M_2 = M_4`. If REP supplies `readout(P) = tr(rho P)` on the composite, then the restriction to a site's subalgebra `M_2 tensor I` is exactly
```text
A |-> tr(rho (A tensor I)) = tr(rho_site A),
```
where `rho_site` is the partial-trace marginal. The runner verifies this over `Q` by checking all `16 x 4` basis pairs for the first factor (`M_2 tensor I`) AND, by the symmetric check, all pairs for the second factor (`I tensor M_2`): matrix units for a general `4 x 4` `rho` and matrix units for the site observable `A`.

Thus REP supplies the state-level marginal representation that block 03 carried as MARGINAL-READ. This does not say the four axioms alone supply REP.

For REGISTERED-FACTOR, assume additionally that record content is typed by a subalgebra `A` of the composite. Under REP, the restriction `P in A |-> tr(rho P)` is a state on that typed subalgebra. Transformations preserving the typed readout preserve the typed algebra, hence normalize `A`. This is block-04-strength compatibility bookkeeping, not a selection theorem; the four axioms supply no transformation group and no independent definition of "record-compatible."

## T2 -- The M2 exception is exact
**T2 (exact, runner-verified):** per-site readout cannot be forced to density form from finite additivity alone.

On one site, rank-1 projections in `M_2` are labeled by unit Bloch vectors `n`. Define
```text
f(P_n) = (1 + n_z^3) / 2,   f(0) = 0,   f(I) = 1.
```

For every antipodal pair, `f(P_n) + f(P_-n) = 1`. This satisfies the `M_2` frame-additivity requirement because orthogonal rank-1 projections in `M_2` are antipodal Bloch pairs.

But no density matrix can reproduce it. If a density matrix with Bloch vector `r` represented `f`, then every rational unit vector in the runner family would satisfy `r . n = n_z^3`. The exact affine system over `Q` is inconsistent:
```text
rank(A) = 3,   rank([A|b]) = 4.
```

So the dimension-2 exception is load-bearing. Per-site additivity does not force REP. The composite domain, here `M_4`, is where external Gleason applies. Observation only, not a new claim: this mirrors the color campaign's need for a composite arena; the lattice nearest-neighbor structure is doing the same job on both sides.

## T3 -- FRAME-EXT gives the unification conditionally
**T3 (conditional):** FRAME-EXT plus external Gleason gives REP on nearest-neighbor composites, and T1 then gives the content of both prior readout-bridge premises.

The external theorem used here is the standard Gleason theorem in the form needed: on a Hilbert space of dimension at least `3` (here the finite-dimensional composite `C^4`, where countable-additivity subtleties do not arise), every NONNEGATIVE, NORMALIZED frame function on the projection lattice is represented by a unique density operator. Boundedness alone would give only a self-adjoint quadratic representation; the positivity and normalization hypotheses are therefore carried inside FRAME-EXT, not assumed silently. Content-determination of the representing operator likewise comes from FRAME-EXT clause (1) plus the uniqueness in Gleason: a content-determined extension has a content-determined representer. This note does not re-prove Gleason and the runner cannot finitely recompute it; the runner only verifies finite instances and T2's exact `M_2` obstruction.

The chain is exactly:
```text
FRAME-EXT
AND Gleason (external, dim >= 3)
  => REP on nearest-neighbor composites
  => T1(a): MARGINAL-READ's content
  => T1(b): REGISTERED-FACTOR's compatibility shape.
```

This replaces two named campaign premises with one named campaign premise. It does not establish FRAME-EXT, does not discharge either sibling premise from the axioms, and does not derive Born weights or the Born form.

## T4 -- The honest crux is FINITE-ADDITIVITY-TO-FRAME
**T4 (gap statement, scope observation only -- NOT a non-derivability proof):** FRAME-EXT is not supplied by the Record axiom's additivity sentence as written. That sentence quantifies over finite collections of pairwise-disjoint records: record configurations that actually occur. A frame function requires additivity over every orthogonal decomposition of the composite projection lattice, including mathematical measurement menus never realized as records. Whether OTHER landed structure forces the extension is open; no candidate theorem is identified here and no non-derivability theorem is proven (T2 proves the per-site obstruction only).

That is the exact content of the open premise:
```text
FINITE-ADDITIVITY-TO-FRAME gap =
realized-record finite additivity does not by itself supply all-frame
additivity on the composite projection lattice.
```

Two forward routes remain open. The derivation route would prove that realized-record additivity plus some landed structure forces a frame-function extension; this note identifies no candidate theorem. The registration route is the graded-constraint primitive proposal route named in the META program memo. That memo is not authority here. Whether to register such a premise is an owner surface. This note makes no ruling and requests none.

## Landing order (required)

This note reduces two premises whose scopes are defined in the UNLANDED
sibling notes of the color-derivation campaign (blocks 03 and 04, PRs #5040
and #5041). Until those siblings land, there is no landed premise scope to
reduce and this note's T3 is vacuous as a ledger operation. This note must
land AFTER blocks 03 and 04 (or jointly), and its T3 becomes citable only
once their premise scopes are landed.

## Residuals and scope boundary (not T-claims)
- R-frame-ext: FRAME-EXT itself remains open; its principal gap is FINITE-ADDITIVITY-TO-FRAME, and its four clauses (content-determination, positivity, normalization, composite-domain authority) are each separately unsupplied by the axiom text.
- R-sibling-landing: the ledger reduction is contingent on blocks 03 and 04 landing (see Landing order); until then T3 is a statement about unlanded premise scopes.
- R-uniqueness: REP asserts existence of a representing `rho` on the audited domain; uniqueness and state-supply are separate and open unless supplied by the external theorem's hypotheses.
- R-born: Born weights and Born form are not derived here. Adjacent work PR #4922 is distinct in scope and not consumed.
- R-singlet-gap and all color-campaign residuals remain unchanged.
- R-h4-menus: which nearest-neighbor composite menus are physically bonded remains open for this note; the META memo's `M_4` composite language is program framing, not a physical menu specification.

## Honest boundary
This note does not add an axiom, primitive, Tier-A admission, or audit verdict. It does not edit any audit ledger. It does not derive FRAME-EXT from Record. It does not establish that every record readout has a frame-function extension. It does not derive Born weights, Born form, gauge selection, color-singletness, a formation rule, measurement contexts, or a physical menu-bonding rule.

It reduces two named unlanded campaign premises to one named unlanded premise, under the external standard Gleason theorem and the explicit FRAME-EXT premise.

## Citation contract
Citation is gated by the standard discipline: this is Class C source material with no premise weight until audit ratification; after ratification, citation is only at audited claim scope exactly.

Downstream rows may cite this note for T1(a)'s exact reduction under REP (the partial-trace restriction identity, both factors). T1(b) may be cited only as convention-strength bookkeeping, never as a selection theorem.

Downstream rows may cite T2 for the exact `M_2` counterexample: per-site frame additivity does not force density-matrix representation.

Downstream rows may cite T3 only after blocks 03 and 04 have landed, and then only as the conditional reduction:
```text
FRAME-EXT + external Gleason => REP => MARGINAL-READ content and
REGISTERED-FACTOR shape.
```

Downstream rows may cite T4 for the named gap statement FINITE-ADDITIVITY-TO-FRAME.

Downstream rows may NOT cite this note for: FRAME-EXT as established; Born form as derived; Born weights as derived; either color premise as discharged; the graded-constraint proposal as registered; a physical composite-menu specification; any audit-status upgrade; or any ruling request.

## Dependencies table
| dependency | supervisor status used here | consumed content |
|---|---|---|
| [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) | current axiom memo; axioms are premises, not bounded-status sources | quoted Record content-only and finite-additivity sentences |
| [GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md](GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md) | META program framing only, never authority | quoted theorem-target and dimension-2 exception orientation |
| [COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md](COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md) | UNLANDED sibling | MARGINAL-READ definition and format discipline only |
| [GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md](GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md) | UNLANDED sibling and format exemplar | REGISTERED-FACTOR definition and citation-contract style only |
| Gleason theorem (external standard mathematics; dim >= 3, nonnegative normalized frame functions -> unique density operator) | external theorem | consumed as stated in T3; not re-proven, not finitely recomputable |

## Runner verification map
The runner text-audits all quoted source sentences against the four permitted files. It verifies T1's partial-trace/restriction identity exactly over `Q`, using all matrix-unit basis elements of a general `4 x 4` composite operator and all site-observable basis elements. It verifies typed-subalgebra bookkeeping by exact closure/unit checks for the representative site subalgebra.

It verifies T2 with exact rational sphere points, exact antipodal additivity, and exact rank inconsistency over `Q`. It performs an AST self-scan for read-only/no-network/no-subprocess discipline. Expected output shape:
```text
[PASS] ...
DECLARATION FRAME-EXT=conditional_premise gap=FINITE-ADDITIVITY-TO-FRAME ...
TOTAL PASS=6 FAIL=0
```

The cache linked in the header is generated by the supervising agent from this runner's output.

## Source-note boundary
Hypothesis set: the four current framework axioms as context; the named conditional premise FRAME-EXT; the external standard Gleason theorem in dimension at least `3`; standard finite-dimensional partial traces; and exact rational linear algebra recomputed by the runner.

Forbidden imports: no new axiom, primitive, Tier-A admission, audit verdict, FRAME-EXT discharge, Born-weight derivation, physical carrier landing, color-campaign residual discharge, or owner ruling is imported. This note is a drafting surface for supervisor review.
