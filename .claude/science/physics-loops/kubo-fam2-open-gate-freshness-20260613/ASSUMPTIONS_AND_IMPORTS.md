# Assumptions And Imports

Allowed source inputs:

- Finite Fam2 refinement data from the SHA-pinned `kubo_fam2_refinement`
  cache.
- Current Kubo parent/context packet source scope.

Forbidden hidden imports:

- A fitted Fam2 Kubo coefficient.
- An external convergence target.
- A same-surface family argument forcing Fam2 to share a Fam1/Fam3 limit.
- An exhaustive obstruction trichotomy.
- Any claim that the inventory resolves Fam2 non-convergence.

This repair adds an explicit re-audit trigger guard for parent/context or
cached-data movement.
