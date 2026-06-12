# Opportunity Queue

1. **Wilson corrected V_taste artifact drift**
   - Status: executed.
   - Why: exact audit repair target says no physics derivation change is
     needed, only runner docstring/comment synchronization.

2. **Taste-scalar CW isotropy source-scope sync**
   - Status: executed.
   - Why: audit repair target offered a safe narrowing path; the algebraic
     identity is independent of the physical staggered-Dirac context gate.

3. **Higgs channel `u_0` drift**
   - Status: deferred because similar work may already exist in an open review
     PR; avoid duplicate branches until reviewer landing state is clear.

4. **Staggered-Dirac realization gate**
   - Status: hard open science.
   - Why: many conditional rows depend on this gate, but it needs a dedicated
     physics block rather than artifact cleanup.
