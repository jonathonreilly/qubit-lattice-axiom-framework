# Review History — kinetic-isotropy derivation loop

## block01, review round 1 (adversarial agent, 2026-06-09)

Verdict: NOT shippable as-is — 1 BLOCKER, 4 MAJOR, 5 MINOR/NIT. Core theorem
(monomial lemma + band-winding saturation) survived all attacks, including
independent numerical family sweeps.

| # | severity | finding | resolution |
|---|---|---|---|
| 1 | BLOCKER | D6 brickwork claim false under the standard symmetric partial-swap convention (actual trace `2cos^2 t - 2sin^2 t cos k`, permanently gapless at k=pi, winding-0, tunable) and the check was a trig tautology unable to detect it | I reproduced the counter-computation independently (confirmed exactly), then REBUILT D6 from explicit one-particle brickwork constructions: D6a symmetric family = a SECOND P4 hostile witness; D6b asymmetric (full x partial) family = the true gapped mass family (`tr = -2 sin t cos k`, gap pi/2 - t); D6c full x full = the winding cell, slope computed; D6d dichotomy sweep added |
| 2 | MAJOR | B2 "exhaustive" sympy solve silently dropped 2 of 3 branches | replaced with the complete 2-case analysis (top coefficient => a=0 or c=0; middle coefficient kills the second survivor in each case) |
| 3 | MAJOR | Part D checks verified converses/tautologies; load-bearing steps were prose | D1 now derives the FORWARD direction (real-on-circle => conjugate-symmetric, Fourier matching); D2 computes the unitarity bound `|tr| = 2|cos omega| <= 2`; D3 derives the spectrum from the quadratic; D6d adds the numerical dichotomy sweep |
| 4 | MAJOR | P3 "retained" provenance over-claimed (CPT note constrains continuous-time H, not the strict tick) and the P3 drop-out witness was missing | P3 regraded to a named conditional reading in note + runner; the `S_+ C(theta)` witness added (complex trace, det-winding 1, branch velocity sweeping [0.087, 0.913]) — referee's counter-example reproduced |
| 5 | MAJOR | real-time cone slope -> OS0 Euclidean ratio bridge asserted, not derived | promoted to the explicit named bridge B-W in the premise table; theorem headline reworded to cone-slope quantization with `c_t = c_s` under the named bridge |
| 6-10 | MINOR/NIT | F's false contrast; B3 dead code; "all artifact orders" qualifier; P1/P2 bookkeeping asymmetry; "#3360 reproduced" wording | all fixed: F1 now verifies the joint-rescale invariance for BOTH carriers; B3 derives v = u'/(iu); D3/D4 scoped to the free single-particle dispersion of the winding band; P1 regraded "retained theorem + reading"; A relabeled "re-derives the stated formula" |

Runner after fixes: 29/29 (4 new checks added by the fixes; 4 transient FAILs
during the rebuild were numerical band-tracking artifacts at degeneracies,
replaced by the principal-branch/both-poles criterion and det-winding).

**Disposition: pass** (all BLOCKER/MAJOR findings resolved with computed
fixes; no finding threatened the core 1D theorem, per the referee's own
verdict: "correct under its premises").
