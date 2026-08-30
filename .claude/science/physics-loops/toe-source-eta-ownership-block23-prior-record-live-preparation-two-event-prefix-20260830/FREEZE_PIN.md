# Block23 freeze pin

The corrected preregistration was committed at
`0645b86a3423a7767b35eeb62efe2acbfb6fa8c7` before any Block23 target runner,
cache, or target mutation existed or executed.

Frozen SHA-256 values:

```text
6378ed13a8c72caca749197127ec67f3c8263c4d622563ec6ba73db75a9b3ead  GOAL.md
c1b28a69298924cded8862987f1d26b292f9546c49b4ea797cd88f219bd310e1  AUTHORITY_GATE.md
c7098ef5c05f4a3b1bd3308c44a64e8bf1e0caa12fa40fb27580009b7672b163  PREFLIGHT_WITNESSES.md
7a16f2f4956d42c6bea387d92bbc0a4ce26004470d872cb3382d370d24dfdb63  PANEL_RETURN.md
f37da51570a3b448a3e430579171c40d934c941bd82704120cd98050d23719f8  INDEPENDENT_PREREG_ATTACK.md
95b733561940b4892b0631e8cb679df1aab1f40004954b9a6baf9a9ef2592618  APPROACH_REGISTRY.md
654eb51a2174b2453b0a4ccc3ff34b09ee6ea1973de50bc3c5ff323cd6edf679  MUTATION_PLAN.md
fea9d4a66f58b2a9fd2759b71fff24093a7a30112ff67d4d65b6cc31b1c00a93  NO_GO_DISCIPLINE_CHECKLIST.md
```

Primary and independent runners must verify these values before target
execution.  Post-execution adjudication, any completed N1--N8 packet, theorem
note, and state updates must be written to separate unfrozen artifacts.
