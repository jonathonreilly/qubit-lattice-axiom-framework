lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T19:05Z

# gap-fctest-opus (FINISH row 946): GUIDE refutation test of (FC) for the vacuum slice chain

Status: in progress. Started 2026-11-14T07:05Z on Mac mini worker 2, at commit 77fc50935
(branch claude/ym4d-hard-route). Everything here is GUIDE unless marked otherwise: a run can
refute (FC) at a coupling, it cannot prove it. No statement of the chain rests on this file.

## Plan (at most eight steps; one per response)

1. Read row 941 (`library/gap-lsivac-max.md`) Steps 1, 5, 6: the exact definitions of the slice
   chain, P, nu, (A3), (FC), (GC), theta_GC, r_1; FINISH efficiency rules; grep open-core and
   FINISH rows for overlap. Record the definitions here verbatim with line references.
2. Write the estimator R(f) and the pass/fail criteria BEFORE any run (what counts as REFUTES,
   what counts as GUIDE-only, error and autocorrelation method).
3. Write code (lane946): SU(2) heat-bath + overrelaxation on a small periodic 4D lattice; frozen
   slice x; resampling of the rest; covariance estimator for grad P f via (A3).
4. Fact-check the code: (a) free photon / Gaussian chain, R = e^(-2 omega) per mode;
   (b) one-plaquette chain, theta_GC near r_1^2 as in row 941.
5. Run beta = 2.3 on the small lattice for the four observables (plaquette, smeared plaquette,
   odd function of (1/2) tr U_p, spatial Wilson line odd under the cut flip). About 45 min cap.
6. If time: beta = 2.6; exact one-cube chain (12 links, 6 plaquettes).
7. Report R(f) per f with error bars and integrated autocorrelation times; verdict per f.
8. RESULT line.

## Step log

(appended as each step completes)
