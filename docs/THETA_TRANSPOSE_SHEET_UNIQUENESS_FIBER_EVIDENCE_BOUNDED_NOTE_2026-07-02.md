# The Transpose-Sheet Sliver Strengthened on Three Angles: Expanded Fiber Search Finds No Second Branch in Two Independent Families, Both Sheets Are Isolated with Identical Rigidity Certificates, and Low-Multidegree Even Invariant Spaces Are Exactly Pair-Generated (Bounded Evidence Note)

**Date:** 2026-07-02
**Claim type:** bounded_theorem (two exact certificates plus honestly-scoped
search evidence; not a uniqueness proof, and stated as such).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.py`](../scripts/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.txt`](../logs/runner-cache/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.txt)

## Question

The campaign's SU(3) star-reduction result (PR #4875, in-flight) proved
local rigidity of the pair-data constraints and exhibited the transpose
sheet as the one known global degeneracy, leaving the sliver (i-b''-a'):
prove — or strengthen the evidence — that transpose is the ONLY
pair-data-preserving sheet. Question answered here: what do an expanded
fiber search, both-sheet rigidity certificates, and exact low-multidegree
invariant counting say?

## Answer

Three angles (runner 8/8; the search's refutation-reporting path is wired
to print any counterexample prominently — none appeared):

1. **Expanded fiber search: no second branch (evidence).** With (A, B)
   fixed, the 10 real C-constraints were solved over the FULL group from
   spread deterministic inits in two independent families: 29/60 and 11/30
   converged solutions, every one reproducing the original orbit's
   flip-odd invariant vector `(tr(A B C'), tr(A C' B))` to 1e-6. A
   converged solution matching the pair data with a DIFFERENT invariant
   vector would have been a refutation finding; none exists in either
   family. Honest scope: search evidence, not a proof.

2. **Both sheets are isolated, with identical certificates (exact).** The
   10 x 8 constraint Jacobian has smallest singular value
   `7.811818e-02 > 1e-2` at the base point AND on the transpose sheet —
   the values coincide exactly because transpose is an isometry of the
   constraint geometry, a consistency signature of the sheet structure.

3. **Low-multidegree even invariant spaces are exactly pair-generated
   (exact singlet counts).** Via joint null spaces of the Gell-Mann
   generator action: `3 x 3 x 3` has invariant dimension 1 (the epsilon
   channel — whose beyond-pair content the campaign's evenness results
   project out); `3 x 3bar x 3 x 3bar` and `3 x 3 x 3bar x 3bar` each have
   dimension 2, matching the delta-pairing (pair-generated) counts with no
   room for a hidden beyond-pair invariant at these multidegrees.

**Sliver state.** (i-b''-a') is strengthened on all three available angles
short of an invariant-theoretic fiber proof: the two-sheet picture now has
matched exact rigidity certificates on both sheets, a two-family search
with a wired refutation path finding nothing, and exact low-degree
invariant counting leaving no room where a separating even invariant could
hide at those degrees. The remaining content is unchanged in kind — a
global fiber theorem — and unmoved in the campaign's consequence structure
(the star reduction and chiral-sign conclusions consumed only the local
certificate plus the exhibited sheet).

## Source surface

**Record axiom** (approved axiom node `minimal_axioms`,
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) —
background discipline only. All group/invariant machinery is earned inline
(Gell-Mann basis; generator conventions; SU(3) sampling by phase-fixed QR
with det-normalization). Deterministic (fixed seed and fixed init lists;
scipy least_squares with LM is deterministic given inits). No unaudited
note is consumed as a premise; no external comparator, fitted number, or
Monte Carlo appears.

## What moves

| Prior state | After this note |
|---|---|
| one-family 12-solution search (in-flight block 7) | two independent families, 40 converged solutions, refutation path wired: no second branch |
| rigidity certificate at the base point only | BOTH sheets certified isolated, with exactly equal singular values (transpose isometry signature) |
| no invariant-counting angle | exact singlet multiplicities at three low multidegrees: all pair-generated except the epsilon channel already handled by evenness |

## What remains

```text
(i-b''-a' residual): a global fiber theorem (invariant-theoretic or
    degree-bound argument) that the pair-data map's fiber is exactly
    {orbit, transpose-orbit} generically. Unchanged in kind; further
    narrowed in plausible failure modes by the three angles above.
```

## Non-claims

This note does not claim: a uniqueness proof; extension of the invariant
counts beyond the three computed multidegrees; that the search's coverage
is exhaustive (convergence gates are stated: 29/60, 11/30); Strong-CP
closure or theta retirement; records registering any object; any new
axiom, import, primitive, or admission.

## No-Go Discipline Gate

**Status:** PASS as bounded evidence packaging. **N1:** direct fiber proof
— open (the residual); search — done, two families; rigidity — exact both
sheets; invariant counting — exact at three multidegrees; higher-degree
counting — open, named. **N2:** nothing else binds on this sliver; the
campaign's consumers used only the local certificate. **N3:** the
refutation path prints counterexamples prominently; gates and thresholds
stated; the identical singular values are explained (isometry), not
suppressed. **N4:** consumes (i-b''-a') and returns it with the same kind
of residual, strengthened. **N5:** "no second branch found" framing
throughout; no uniqueness claim in any check name. **N6:** live paths: the
global fiber theorem via invariant theory; higher-multidegree counts; a
complex-fiber degree argument. **N7:** steelman — "search evidence cannot
prove uniqueness": agreed and stated; the exact content is the two
certificates and three invariant dimensions. **N8:** echo guard — never
cite this note as a uniqueness proof; the sheet-sliver remains open by
name.

## Verification

Run:

```bash
python3 scripts/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=8 FAIL=0
```

Sections: A expanded fiber search with invariant classification (two
independent families, wired refutation reporting); B both-sheet rigidity
certificates (matched smallest singular values); C exact singlet
multiplicities at three low multidegrees.
