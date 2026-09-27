# Campaign 5 (2026-09-26): probable work deferred to the backlog

Owner rule (2026-09-26): only validated science that moves the program forward goes into a PR; probable work goes on this backlog.

Campaign 5 opened #9313, #9328, #9350 and #9352 (and a 12^3 population series). Three lines of work did not meet the PR bar and are queued here:

| Unit | What is missing |
|---|---|
| `J:derive:campaign5-20260926-charged-ring-reptation-slow-mode:a1` | Reptation for the charged ring clause: end energies agree across guides on 6^3 at path 40, but the pure link expectation does not (flat path profiles). Identify the slow mode or a sampler that removes it. |
| `J:derive:campaign5-20260926-window-fluctuation-susceptibility:a1` | A population-free susceptibility from window fluctuations of the transverse modes: exact on 2^3, but on 8^3 its single-mode fit (1.41 +- 0.14) sits 2 sigma above the three-point energy estimate (1.12). Reconcile, then use it for chi(k) at several k. |
| `J:derive:campaign5-20260926-handover-double-weyl:a1` | The comparator's merged touching at the handover (J = 1, kappa = 1/2): exact rank-1 Hessian and positive weighted-degree-4 form (linear x quadratic). Certify the charge 2 and the exact count at kappa_h. |

Files: `reptation/` (continuous-time reptation library with probe fields and window modes; drivers used in the campaign) and `handover/` (the exact expansion). Results and numbers are in each directory's `RESULTS.md`.
