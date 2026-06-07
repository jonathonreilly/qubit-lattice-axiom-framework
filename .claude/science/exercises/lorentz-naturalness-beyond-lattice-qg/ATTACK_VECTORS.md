# Attack-vector portfolio (synthesis)

| Rank | Route | source exercise | expected status if done | first artifact | stop condition |
|---|---|---|---|---|---|
| 1 | **Compute the species-differential marginal δv** (turn the prior into a posterior) | Two/Five | a definite PASS or FALSIFY (not a naturalness argument) | lattice-PT self-energy on shared sin(pa) kernel, two reps differing only in C₂(R), native continuous-time surface, × (μ/M_Pl)^γ flow | δv < bound → pass; > bound → falsify |
| 2 | **UHECR dim-6 prediction** (near-edge, near-term testable) | One/Five | a sharp falsifiable prediction | the tree result 5.6e-18 vs bound 1e-17 at E~10¹¹ GeV (0.3 orders) | sharpen the UHECR coefficient + current bound |
| 3 | quantify the (μ/M_Pl)^γ IR suppression on the DIFFERENCE | Three | tightens route 1 | integrate the coupled velocity-RG (#3121) for the rep difference over the Planck→lab hierarchy | γ_eff |
| 4 | reframe note: naturalness → computation (the framing correction) | One/Five | corrects the prior verdict's framing | the synthesis runner + note | — [BUILT] |
| 5 | (fallback) custodial symmetry / new strong UV | — | only relevant IF route 1 lands above bound | #3126/#3129/#3131 (done: excluded / new-physics) | — |

## Assumptions most likely wrong (prior analysis)
- "the framework's δv = the Collins α_s/4π estimate" — it's a PRIOR, not the framework's posterior (the
  shared-kernel difference + flow + c_t-fixing are unquantified).
- "this is a naturalness/tuning problem" — category error for a fixed theory (no free coupling).

## Most expensive to be wrong
- Route 1's outcome: if the computation lands at ~10⁻³, the framework is FALSIFIED on Lorentz (high stakes).

## Worth a physics-loop PR
- Route 4 (the framing correction) — BUILT this exercise.
- Route 1 (the computation) — the genuine open task; a real multi-step lattice-PT computation.

## What NOT to do
- Don't keep arguing naturalness/symmetry as if it were the primary question (it's the EFT framing's
  fallback). The fixed-theory's primary task is the NUMBER (route 1).
- Don't claim the reframe SOLVES the obstruction — the shared kernel does not cancel the species difference.
