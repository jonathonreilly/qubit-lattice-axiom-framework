# Review History — theta lane block03 (2026-07-18): DEMOTED, NO PR

## Round 0 — supervisor pre-battery
5/5 on the draft identities; supervisor-authored 12-gate runner, five
mutation families verified; cluster-cap evaluation drafted (moot — no PR).

## Round 1 — combined adversarial lens: 4 blockers / 4 major / 1 minor
ALL ACCEPTED. The block's central claim ("the Record/log bridge is forced,
not chosen") is REFUTED as stated:

1. The axiom-lift fails semantically: the Record axiom's additivity
   quantifies over REALIZED finite disjoint record collections, not over
   arbitrary positive reals. Exact countermodel (lens-constructed,
   supervisor-verified): I(A) = |A| with channel datum d(A) = 2^|A| —
   fixed, nonnegative, nondegenerate, Record-additive, multiplicative in
   the datum on every disjoint pair. The realized datum monoid need not
   be inverse-closed or full, so the sibling incompatibility does not
   lift without an explicit record-to-datum realizability premise.
2. Codomain sign-switch: T1 excluded nonnegative raw readouts while T2
   used signed log readouts; with signed scalars, F = log x already
   solves F(xy) = F(x) + F(y) nondegenerately, so the exclusion does not
   force the log presentation.
3. "Pinned up to one slope" used the bounded-additive theorem without its
   boundedness premise anywhere in (R1)/(R2).
4. "Only nondegenerate interface" is not exhaustive: partial-domain
   escape H(2^a 3^b) = b (additive under multiplication, nondegenerate,
   non-monotone, not s·log x), plus unregularized Cauchy maps.

Plus: the empty-collection/unit-block anchor identification was
unsupported; the runner certificate did not test the load-bearing lift;
the N-gate was incomplete against the decisive routes.

## Disposition: DEMOTE AND ARCHIVE (no repair, no PR)

A repaired version needs: an explicit record-to-datum composition premise
with universal disjoint realizability (or realized-monoid scoping with
inverse closure), declared codomains per case, the boundedness hypothesis,
and exhaustiveness scoped to total regular maps — after which the
remainder is a near-restatement of block02's T1 normal form with premises,
failing the value gate as churn. The draft note and runner are archived in
this pack (ARCHIVED_BLOCK03_DRAFT_*); the manifest is restored to the
block02 state; no PR is opened.

## What the lane learned (durable)

Block02's named open link — the Record/log bridge — is GENUINELY open, and
the countermodel shows exactly why: closing it requires a premise about
the record-to-datum map's realizability structure that nothing landed
supplies. Any future attempt must start from that premise, named as such.
