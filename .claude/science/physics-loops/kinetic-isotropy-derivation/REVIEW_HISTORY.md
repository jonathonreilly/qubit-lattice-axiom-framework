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


## block02, review round 1 (adversarial agent, 2026-06-09)

Verdict: NO BLOCKERS. Central theorem correct — referee independently
re-derived every leg (degree table, two-circles, dispersive-cell unitarity,
single-mover structure, cell-to-site factor via wavepacket evolution on a
64-site ring) and STRENGTHENED the lemma (det confined to ONE value, not two,
for T != 0).

| # | severity | finding | resolution |
|---|---|---|---|
| 1 | MAJOR | B5 acceptance gate (cost < 1e-16) silently discarded 61/86 starts including 5/6 dispersive-biased seeds; "EVERY dispersive" label rode on n=1 of one branch; cached log non-reproducible | rebuilt: acceptance via fine-grid residual < 1e-6 after LM, both branches seeded, counts reported (now 24 dispersive covering w = -1 and w = +1, 0 discards), label scoped to "every dispersive solution FOUND" |
| 2 | MAJOR | "P4 DISCHARGED" overclaim: the residual "the realized tick is dispersive (nonflat)" was missing from the remaining conditional set | ledger row reworded to REDUCED; "+ a dispersive realized tick" added to the conditional set everywhere (note, certificate, runner docstring) |
| 3 | MAJOR | B2/B3/B4 were cannot-fail checks (hardcoded winding phases; differentiating hand-written linear functions; K-free roots) | rebuilt: B2 computes det confinement at both intersection points (= 1 exactly) AND the licensed dispersive det sweeping the BZ; B3 derives omega from eigenvalues of the actual T=0 cell; B4 from eigenvalues of an actual w=0 cell |
| 4 | MINOR | A3 verified its own algebra; column orthogonality never imposed | full unitarity system: cross terms + orthogonality forcing alpha = delta = 0 on the dispersive branch (completes C1); dead code removed |
| 5 | MINOR | Part C heading overclaimed ("ARE the staggered structure"); two-mover tension under-flagged | heading -> "share the staggered hopping shape"; added: no licensed period-2 tick reproduces the landed two-mover sin(k) surface (larger-cell content, sharpens N7) |
| 6 | MINOR | C4 per-axis sentence presupposed tick factorization | reworded: "applies to any per-axis FACTOR, where the tick factorizes (3D simultaneous tick = named open)" |
| 7 | MINOR | D2 was a verbatim duplicate of A2 inflating the scorecard | replaced with the brickwork-fold illegality check (block01's cell-level winding construction is also site-license-illegal: diagonal z-entries = 2-site moves) |
| 8-10 | NIT | B1 empty-intersection case; A4 weak predicate; omega presentation mismatch | B1 asserts y^2 < 0 at t=3; A4 predicate tightened to "at most one nonconstant z power"; presentation unified |

Runner after fixes: 16/16. **Disposition: pass.**
