# The Transpose-Sheet Sliver Strengthened on Three Angles: Expanded Fiber Search Finds No Second Branch in Two Independent Families, Both Sheets Pass Matching Rigidity Certificates, and Low-Multidegree Even Invariant Counts Are Pair-Generated (Bounded Evidence Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (deterministic rigidity certificates,
computed low-multidegree invariant counts, and honestly scoped search
evidence; not a uniqueness proof, and stated as such).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta's Tier-A admission is already
retired on main by the retained 2026-07-05 retirement decision. This note is
banked only as bounded historical/supporting evidence for the transpose-sheet
escape route; it does not reopen, modify, or supply authority for that
retirement record.
**Primary runner:**
[`scripts/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.py`](../scripts/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.txt`](../logs/runner-cache/theta_transpose_sheet_uniqueness_fiber_evidence_2026_07_02.txt)

## Question

The campaign's SU(3) star-reduction lane left the sliver (i-b''-a'):
prove — or strengthen the evidence — that transpose is the ONLY
pair-data-preserving sheet. This note is self-contained on that sliver and
does not consume an in-flight sibling PR as a premise. Question answered
here: what do an expanded fiber search, both-sheet rigidity certificates,
and computed low-multidegree invariant counting say?

## Answer

Three angles (runner 8/8; the search's refutation-reporting path is wired
to print any counterexample prominently — none appeared):

1. **Expanded fiber search: no second branch (evidence).** With (A, B)
   fixed, the 10 real C-constraints were solved over the FULL group from
   spread deterministic inits in two independent families: 28/60 and 10/30
   converged solutions, every one reproducing the original orbit's
   flip-odd invariant vector `(tr(A B C'), tr(A C' B))` to 1e-6. A
   converged solution matching the pair data with a DIFFERENT invariant
   vector would have been a refutation finding; none exists in either
   family. Honest scope: search evidence, not a proof.

2. **Both sheets pass matching deterministic rigidity certificates.** The
   10 x 8 constraint Jacobian has smallest singular value
   `7.811818e-02 > 1e-2` at the base point AND on the transpose sheet —
   the displayed values match because transpose is an isometry of the
   constraint geometry, a consistency signature of the sheet structure.

3. **Low-multidegree even invariant spaces are pair-generated in the
   computed singlet counts.** Via joint null spaces of the Gell-Mann
   generator action: `3 x 3 x 3` has invariant dimension 1 (the epsilon
   channel, not used here as an even pair-generated channel);
   `3 x 3bar x 3 x 3bar` and `3 x 3 x 3bar x 3bar` each have dimension 2,
   matching the delta-pairing counts with no computed room for a hidden
   beyond-pair invariant at these multidegrees.

**Sliver state.** (i-b''-a') is strengthened on all three available angles
short of an invariant-theoretic fiber proof: the two-sheet picture now has
matching deterministic rigidity certificates on both sheets, a two-family
search with a wired refutation path finding nothing, and computed
low-degree invariant counting leaving no room where a separating even
invariant could hide at those degrees. The remaining content is unchanged
in kind — a global fiber theorem. This note does not assert any downstream
star-reduction or chiral-sign conclusion.

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
| one-family 12-solution search | two independent families, 38 converged solutions, refutation path wired: no second branch |
| rigidity certificate at the base point only | BOTH sheets pass the same deterministic isolation certificate (transpose isometry signature) |
| no invariant-counting angle | computed singlet multiplicities at three low multidegrees: pair-generated in the two even quartic spaces; epsilon channel isolated as non-pair input |

## What remains

```text
(i-b''-a' residual): a global fiber theorem (invariant-theoretic or
    degree-bound argument) that the pair-data map's fiber is exactly
    {orbit, transpose-orbit} generically. Unchanged in kind; further
    narrowed in plausible failure modes by the three angles above.
```

## Non-claims

This note does not claim: a uniqueness proof; an exact symbolic Jacobian
or exact symbolic invariant-count proof beyond the displayed computations;
extension of the invariant counts beyond the three computed multidegrees;
that the search's coverage is exhaustive (convergence gates are stated:
observed local counts 28/60 and 10/30, with gates at >=15 and >=8);
Strong-CP closure or theta retirement; records registering
any object; any new axiom, import, primitive, or admission.

## No-Go Discipline Gate

**Gate result:** bounded evidence packaging only. **N1:** direct fiber proof
— open (the residual); search — done, two families; rigidity — deterministic
both-sheet certificates; invariant counting — computed at three multidegrees; higher-degree
counting — open, named. **N2:** nothing else binds on this sliver; the
campaign consequence chain is not asserted here. **N3:** the
refutation path prints counterexamples prominently; gates and thresholds
stated; the identical singular values are explained (isometry), not
suppressed. **N4:** consumes (i-b''-a') and returns it with the same kind
of residual, strengthened. **N5:** "no second branch found" framing
throughout; no uniqueness claim in any check name. **N6:** live paths: the
global fiber theorem via invariant theory; higher-multidegree counts; a
complex-fiber degree argument. **N7:** steelman — "search evidence cannot
prove uniqueness": agreed and stated; the bounded content is the two
certificates and three computed invariant dimensions. **N8:** echo guard — never
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
certificates (matched smallest singular values); C computed singlet
multiplicities at three low multidegrees.
