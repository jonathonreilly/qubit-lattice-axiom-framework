# SOURCE-EXPOSED bounded delta check

This check covers only the two prose clarifications made after SOURCE_CHECK.md.
It does not repeat the full source review or create new computational evidence.
The original restricted-input proof/checker/checkpoint and SOURCE_CHECK.md are
preserved. This file is a separately labeled, source-exposed continuation.

## Exact revision and recovery identities

All primary paths below are under
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/detector_refinement/`.

| Artifact | Verified SHA-256 |
|---|---|
| outputs/result_before_clarifications.md | `b3a9bd60ae8aaa5390add43d282771541ebcc649af11fb89dd83bcf5a42f60f8` |
| outputs/result_clarifications.patch | `41aea4867dfbeb6872af4396ff6cfe44ac7905954bcd554f64e55b1e421374a2` |
| RESULT.md after clarification | `7f0d0aa5c0c6316c3066882de71734463a9260c50530711ae8cf38f75b5ee0b2` |
| check.py, unchanged | `20d2fe3b1cd4e2120b67c32270a70cc81ee7ca15c5efafdab265030cbf754501` |
| ASSUMPTIONS.md, unchanged | `ccd5ca22454914ef7df72d0df108ffa924ccd86c79310176c7a519a79b02d845` |

The archived original has exactly the identity reviewed in SOURCE_CHECK.md.
I read the entire saved patch and independently viewed the actual old/new diff.
A deterministic, in-memory unified-patch replay checked every context/removal
line and both hunk counts against the archived bytes, then asserted that the
reconstructed text exactly equaled the current RESULT.md. It reported:

    exact-patch-replay: 2 hunks; recovered bytes equal current RESULT.md; no files written

This is a text/recovery check, not a numerical science job. No other content
change to RESULT.md is present between these pinned revisions.

## The two arguments

**All-site rate confinement.** The first addition is correct on its explicitly
named isolated-prefix domain. A positive-rate local query must parse all four
unique headers. On that domain they are the same four records used by the
emitter's global candidate helper, so both recover the same frame. Every
enabling branch then restricts the center to a race or output site in that
frame. Consequently omitted sites have zero formation rate; every candidate
is within radius 16 of all other patch records because the patch diameter is
at most 15. This is the needed analytic justification for finite candidate
enumeration on the stated domain. The addition correctly avoids extending
that enumeration claim to arbitrary multi-patch/global record configurations.

**Four-outcome refinement scope.** The second change correctly limits the
q=1 merge/refinement equality to programs whose fine outcomes fit the four
available fine labels. The 25 individual quarter-grid diagonal effects fit
binary menus; the 225 summable ordered pairs fit menus consisting of the two
effects and their residual. Those realizations need no more than three
nonzero outcomes. They do not establish every quarter-grid POVM: four copies
of P0/4 and four copies of P1/4 already require eight separately labeled fine
outcomes. The added restriction therefore closes the explicitness issue noted
in SOURCE_CHECK.md without weakening any proved in-family identity.

Both changes clarify existing premises and proof coverage. They add no axiom,
clock law, preparation calibration, hidden quantum capacity assumption, or
claim that the whole apparatus is one qubit. The existing classical-label
boundary remains unchanged: the dimension bound concerns compression of the
entire declared interface into one qubit without additional side information.

## Evidence reuse and limits

The native parser, emitted case definitions, checker, and numeric inputs did not
change. The existing baseline and six control receipts reviewed in SOURCE_CHECK.md
therefore remain relevant to their exact code/certificate identities; no numeric
rerun is needed for these two prose-only changes. The receipts remain evidence
for a finite diagnostic bank and the named controls, not an exhaustive native
execution over all legal programs or a cryptographic execution attestation.

No additional mathematical defect was found in this delta. No governing or
primary source edit, numeric execution, commit, push, or audit action was
performed by this worker.
