# Branch-tracked theta_2 isolation and labeled vernier repair — Cycle 675

Claim type: bounded_theorem

Date: 2026-07-23. Authority: none. Audit: unset. Completion rows for the
Cycle-662 block (contract Addendum A, SHA
`174ce1cae3edce3f888f1ecb10e6d258d9ffd23c620aea5f92d6524c74e1bf32`, frozen
before output). Runner:
`scripts/physical_branch_tracked_isolation_labeled_vernier_cycle675_2026_07_23.py`
Cold: **2 PASS / 0 FAIL, exit 0**. Joint lane max 674 observed;
claiming 675.

1. **theta_2 isolation (keystone completion).** On the branch-informed narrow
   window the infinite-volume A2 equation has an ISOLATED TRANSVERSAL ZERO at
   **theta_2 = +0.3136861** — |b_A2| = 1.35e-12 at quadrature order 32,
   order-stable to <1e-3 through order 40, at the finite-L plateau. The
   Cycle-662 width-proxy fallback was not needed: the second line is a genuine
   transversal numerical zero on the declared narrow window, completing the
   quadrature-controlled two-line numerical statement
   (theta_b = -2.97557599, theta_2 = +0.3136861).
2. **Vernier repair.** Amplitude-labeled line pairing PLUS sidelobe exclusion
   (the second peak is searched outside the first peak's band; the Cycle-662
   row-4/5 failures were theta_b spectral-leakage sidelobes outmagnituding the
   genuine theta_2 peak at unfavorable bin alignments) reconstructs ALL SIX
   frozen alpha rows within two bins (max error 4.7e-4), gold row unchanged
   (R_rec = 1.24999 -> A-count 5:4). The passing implementation uses
   amplitude/position pairing plus sidelobe exclusion; the frozen predictions
   were not altered.

Firewalls: quadrature-controlled statements, not the open rigorous lemma; the
5:4 reachability carries the Cycle-612 association caveat verbatim.

## Dependency citations

This runner byte-pins
[Cycle 662](PHYSICAL_INFINITE_VOLUME_A2_TWO_LINE_VERNIER_TOURNAMENT_CYCLE662_NOTE_2026-07-23.md),
and the 5:4 wording retains the association caveat from
[Cycle 612](PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md).
