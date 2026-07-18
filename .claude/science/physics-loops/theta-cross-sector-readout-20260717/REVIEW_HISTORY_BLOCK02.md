# Review History — theta lane block02 (2026-07-18)

## Round 0 — supervisor pre-battery
7/7 on the draft mathematics; worker runner (20/0) reviewed line-by-line;
7 mutation families verified.

## Round 1 — combined adversarial lens: 1 blocker / 4 major / 2 minor,
ALL accepted; the blocker REFUTED the draft's central claim and the block
was rewritten to the corrected science.

- BLOCKER (accepted, note renamed): the draft identified the parent's
  scalar record-additivity (P-add) with log-coordinate additivity. They
  differ: F(x)=x is multiplicative with additive log but 6 != 5 breaks
  scalar additivity. The corrected block: (P-hom) <-> (P-log) only
  (T1), and the NEW sharper result the refutation exposed — on the
  erased slice the scalar-additive shape admits only the degenerate
  readout (F(1)=0 then F(x)+F(1/x)=0 with F>=0), so the parent's two
  routes are genuinely distinct there and the viable odd-side
  ingredient is the homomorphism form (T2). The draft's "one supply /
  entirely Record-facing" corollary withdrawn; the honest tail (T4)
  names the Record/log bridge as the exact open link.
- Major fixes adopted: strict positivity stated for (P-log)'s domain;
  the bounded-additive theorem named as standard mathematics with
  runner cells labeled consistency instances; T3 retitled
  non-reconstruction with the lens's two-readout discriminator
  (z/|z| vs e^{i sin(arg z)}, 1 != e^{2i} at (i,i)) gated; overclaim
  language replaced; N-gate and dependency-role repairs.
- Note and runner renamed to match the corrected content
  (..._log_equivalence_and_additivity_incompatibility_...).

## Mutation checks — 9 families, all FAIL correctly
M, T1, D, INC1-anchor, INC2, INC3(via B cascade), B, N (plus the
worker-round families on the withdrawn draft). Unmutated runner:
`TOTAL: PASS=18 FAIL=0`; cache SHA-pinned; `__TOTAL__` resolved after
final state. One runner repair during landing: INC2's two-symbol
reduce_inequalities raised NotImplementedError and was re-encoded
single-symbol (the crash was caught because the clean run is always
re-executed after every edit).

## Round 1 disposition after rewrite: pass
