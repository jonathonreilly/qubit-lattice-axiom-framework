---
claim_id: d4_zoom_direction_finite_rung_matter_weight_is_an_event_kernel_liv_set_by_the_event_rung_count_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "D4 event set, root slicing, free supplied model (NN Wilson seed, alpha = 1/2, forced W(F4) zoom kernel of #10098). (T) Blocking keeps poles, so the physical light-band dispersion E(K) is fixed by whichever kernel sits on the events; zooming UP from it only changes units (cell-unit beta_0/16^n at cell 2^n a = the same physics). (T+F) The factor-2 zoom map R acts on functions on the EVENT Brillouin zone (G_n = R^n(G_NN) is 2 pi D4*-periodic to 5e-15) and D_n = G_n^-1 is exponentially local on the events (envelope decay 2.2-2.3 per unit length, n = 1..3, L = 12, finite-size control 6e-3); so 'n rungs' needs no lattice finer than the events. Its event-scale dim-8 coefficient is beta_e(n) = beta_e(0)/16^n = -0.1185, -7.41e-3, -4.63e-4, -2.89e-5 (n = 0..3; slice fit 1.000-1.006), -> 0 only as n -> inf. Reading A (NN on the events) gives the n = 0 row for every n; reading B' (event weight = R^n(NN), which the finite-rung decision's own cost statement presupposes) reproduces the PR #10110 rows. Every row passes every measured bound."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/d4_zoom_direction_finite_rung_matter_weight_is_an_event_kernel_liv_set_by_the_event_rung_count_2026_10_26.py
---

# The finite-rung matter weight is a kernel ON the events: physical LIV is set by the event weight's rung count, and no finer lattice is needed

Runner: runner.py. TOTAL: PASS=6 FAIL=0 in 28 s, 81 MB peak, seeded, AUDIT_TIMEOUT_SEC = 120, 3.0 k characters.
Re-run under a unique filename (scratchpad copy): identical output apart from the runtime line.
Pre-registration: criteria_pre_run.txt (written before any computation here).
Labels: [T] exact, [F] finite diagnostic in a supplied free model, [E] estimate against measurement, [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Deviations from pre-registration, stated:
- The first run was launched at 1-minute load 8.15 (brief limit 8). It finished in 6 s at 31 MB; later runs were launched at load < 7.
- Z1 failed on the first run: the 256-point slice DFT aliases for small coarse energies (n = 1, k = 0.12, alias ratio
  e^-17). Nth was raised to 1024; the identity then holds to 8e-12. An in-run bar that I added (relative agreement of
  E/K - 1 to 1e-6) was tighter than the identity's absolute precision allows. It was replaced by |Delta(E/K - 1)| < 1e-10.
- Z3 "monotone shell maxima" FAILED as worded. D_n has real shell structure: a dip at |X|^2 = 8, then a bump at 10-16.
  The same values appear on the L = 8 and L = 12 tori, so this is not a finite-size effect. The check was replaced by the tail
  envelope max_{|X|^2 >= s} |D_n|, with a fitted rate > 1, an overall drop < 1e-3 to |X|^2 = 28, and L = 8 vs L = 12
  agreement < 1e-2.
- Z6: the first Newton seed converged to the light root. It was re-seeded at the pair (located by a scan; diagnostic
  scripts in the scratchpad).

## Builds on, uses, narrows
- d4-predictions-recompute (PR #10110): G_rung, threshold formulas, kappa = 1/90 and 1/1440 are reused. Its numbers are
  REPRODUCED. Its load-bearing reading [S] is NARROWED: it said rung n "sits on a 2^n-finer lattice (sub-site)". That
  is not needed (Z2, Z3). Its alternative sentence ("if the NN start were pinned to the events, the rungs would be a
  redescription") is exactly reading A, confirmed here (Z1).
- d4-zoom-fixed-point-fermion (#10098): the forced kernel, the refinement map, and the NN pair are reused. Its rung-n
  ghost weights (2e-4, 7e-7, < 1e-14) are quoted, not recomputed.
- zoom-fixed-point-tick (#10092): T2 (blocking keeps poles) is the engine. T1 (finitely many branches => LIV nonzero)
  explains why beta_n != 0 at finite n.
- CANDIDATE_AXIOM_RULES.md, the finite-rung decision ("Infinite image tower"): tested for which reading it presupposes (Z6).
- Owner principle (2026-09-02): the lattice is the smallest object; zoom out freely. Both readings respect it. Only
  the #10110 sub-site wording did not.

## Theorems and exact facts
- [T] Pole invariance under zoom-up. A rung is a positive sum of fine propagators at Q = (P + l)/2 plus a contact term,
  so E_coarse(P) = 2 E_fine(P/2).
  - Physical units: E_phys(K) = E_n(K a_n)/a_n = E_0(K a_0)/a_0, so beta_n (K a_n)^4 = beta_0 (K a_0)^4.
  - Zooming UP from an event kernel never changes physical LIV. It only rewrites it in cell units.
  - [F] Z1: E_n(2^n K)/2^n = E_0(K) to 8e-12 (n = 1..3, body ray), and the physical E/K - 1 at K = 0.06 is the same for
    n = 0..3 to 1e-11 absolute.
- [T] The zoom map is an operation on EVENT kernels. R[G](P) = sum_k (1/2) f(Q_k)^2 G(Q_k) + alpha(1 - sum_k (1/2) f(Q_k)^2)
  takes a 2 pi D4*-periodic function to a 2 pi D4*-periodic function.
  - "Q = (P + l)/2" is an evaluation point of the symbol, not a site.
  - So G_n = R^n(G_NN) is an n-step truncation of the fixed-point series, and it lives on the events. It has the same
    status as the fixed point's continuum image sum: an origin formula, not a degree of freedom.
  - [F] Z2: periodicity holds to 4.6e-15 for n = 0..3.
  - [F] Z3: D_0 is exactly NN (zero beyond the roots, 9e-16). D_1..D_3 are exponentially local on the events, with
    envelope decay 2.34, 2.24, 2.22 per unit length (D4 units). The ratio |X|^2 = 28 to |X|^2 = 2 is about 3e-5.
- [T+F] Z4: the event-scale dim-8 coefficient of the event kernel is beta_e(n) = beta_e(0)/16^n. It is read from the
  event-slice correlator of G_n itself, with no finer slices.
  - Values: -0.1185, -7.41e-3, -4.63e-4, -2.89e-5 for n = 0..3.
  - Fit/exact ratios: 1.000, 1.005, 1.006, 1.006 (k^8 contamination).
  - The coefficient approaches 0 geometrically WITHOUT finer lattices, but it is nonzero at every finite n (T1). It is
    exactly 0 only for the exact fixed point (#10110 C3: |beta_inf| < 1e-8).
- [T+F] Z6: the NN Lee-Wick pair (k = 0) at E_pair = 2.600 + 1.667i (D4 units) is a pole of G_n at 2^n E_pair
  (|G_n| blow-up 1e7 at a 1e-9 offset, n = 1, 2).
  - Under B', the event weight's pair is 2^n times heavier, and its buffered weight falls as quoted in #10098.
  - Under A, the event-scale pair stays at E_pair with its rung-0 weight 2e-4.
  - The decision's recorded cost ("< 1e-14 at rung 2") is therefore a statement about the event weight only under B'.
    The decision presupposes B'.

## Decision: which kernel sits on the events
- Reading A (NN on the events; rungs = zoom-up descriptions). The physical LIV is rung 0 for every n:
  - c_e = -0.1185 (ka)^4 (body);
  - gamma -> e+e- at 1.91e20 eV;
  - e -> e gamma closed;
  - nuclear wall 9.7e20 A eV;
  - E_QG,4 = 1.75e18 GeV.
  Under A, "finitely many rungs" has no physical content: the rung count only names a description scale.
- Reading B' (event weight = R^n(NN), finite n). This is the decision as recorded. It needs no sub-event structure.
  The physical LIV is the #10110 row n.
- Reading B (exact fixed point on the events) is the n -> inf limit of B'. The decision rejected it, but it gives the same
  nuclear wall as n >= 1 (link-limited, 1.53e21 A eV). Only the e -> e gamma line moves, from 2.88e20 to 2.79e20 eV.
- The UHECR margin does NOT require the exact fixed point. For the 3.2e20 eV event read as a proton, the margin is x3 under
  A and x4.8 under B' at any n >= 1.

## Verdict: TABLE STANDS (numbers), reading corrected
- The #10110 rows survive as properties of the EVENT kernel R^n(NN): matter dim-8, e/gamma ratio 16^(1-n),
  gamma -> e+e- closed for n >= 1, e -> e gamma 2.8-2.9e20 eV for n >= 2, wall 1.53e21 A eV, and E_QG,4.
- Rows independent of the zoom are untouched: photon, graviton 3.85e-80, cubic 80.4 PeV, nucleon lifetime, slab Ls >= 46/58.
- RETRACTED: the gloss "rung n = NN start on a 2^n-finer (sub-site) lattice blocked up".
- For the decision record [S], two points:
  - "Finitely many rungs" must mean "the matter history weight on the events is R^n(NN) for a stated n". It must not mean
    "an NN weight on the events, zoomed up", because zoom-up never lowers physical LIV.
  - n is a supplied integer, and the physical LIV depends on it (16^-n). No measured bound selects n, since every n passes.
    Leaving n open leaves the matter LIV prediction open by 16^n. The n = 0 case is reading A.

## Smuggling review
- Forced or exact: pole invariance; the periodicity of R; the 16^-n law; the location of the pair images; the kernel weights (#10098).
- Supplied: the NN Wilson seed; alpha = 1/2; the rung count n; free models; E* = hbar c/2L; m_e, m_p; the threshold
  formulas; the composite-flow wall reading (#10110).
- Fitted: none. No rule is proposed. Gate items are not applicable.
- Cost under B', stated: the event weight has finitely many heavy pole branches (16^n images, T1-consistent) and a
  multi-slice transfer. Per the decision, these add no site states.

## Open
- A rule that fixes n, or that replaces "n rungs" by a criterion (e.g. a residual-LIV or ghost-weight bar stated without measured numbers).
- p -> p gamma at n >= 2. Loop-level species dependence. The zoomed link weight, which would restore the ratio 16.
