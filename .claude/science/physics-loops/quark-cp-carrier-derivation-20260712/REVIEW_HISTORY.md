# Review History

## Iteration 1 — fixes required

Three independent review lanes inspected the math/code, the physics/no-go
boundary, and imports/governance. They found five load-bearing issue groups:

1. the historical optimizer still described diagonal-label ratios as physical
   masses and overclaimed full-package closure;
2. the numerical spectrum mismatch needed an exact certificate;
3. the shared weak-basis orbit had been described too broadly;
4. positive dependents still consumed the retyped target as an existence
   result; and
5. the paired log, terminal-synthesis check, and loop pack were stale.

The fixes relabel the historical runner and add singular-value diagnostics;
add exact rational characteristic-polynomial sign brackets; narrow the orbit
claim to non-invariance; separate all positive reopening walls; make the
source dependents historical/non-load-bearing; make terminal synthesis accept
the pending re-audit transition; refresh and preserve the log; and complete
the loop pack.

The reviewers also requested canonical/publication weaving. That is recorded
for the landing/audit owner rather than performed here because the physics-loop
contract forbids editing repo-wide authority/publication surfaces in this
science PR.

## Iteration 2 — pass

Focused re-review of only the repaired files passed all three lanes:

- code/math independently verified the exact rational brackets, optimizer
  spectrum firewall, paired log, and historical/pending/ratified terminal
  transition;
- physics/no-go passed N1-N8 after confirming the non-invariance-only orbit
  scope, separate reopening walls, residual-provenance firewall, and strongest
  steelman; and
- imports/governance verified that direct positive science dependencies are
  gone, regenerated target/scope rows have no dependencies, strict audit lint
  passes, and authority/publication weaving is honestly deferred.

No audit verdict was authored or applied. Independent audit remains required
after landing.
