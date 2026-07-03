# Handoff

Branch: `physics-loop/newtonian-distance-pointer-rawrows-20260608`

Target claim: `newtonian_distance_law_confirmed`

What changed:

- Added raw replay rows to the historical pointer note.
- Added exact recomputation values from the verifier.
- Extended the pointer guard to parse the frozen log and check note row
  inclusion.

Verification:

```text
SCORECARD PASS=9 FAIL=0
SCORECARD PASS=20 FAIL=0
```

Remaining boundary:

This is still a bounded finite-lattice replay pointer, not a universal
Newtonian law theorem.
