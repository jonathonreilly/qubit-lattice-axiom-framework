# Opportunity Queue

This block is self-contained and ready for reviewer/audit inspection.

Next campaign candidates after this PR:

1. Continue scanning newly audited conditional rows for blockers with exact verifier/source mismatches.
2. Prefer rows where the blocker offers a framework-native repair over status narrowing.
3. Avoid targets already covered by open repair PRs unless the new audit result names a different dependency.
