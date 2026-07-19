# Cluster-cap evaluation — microcausality family, PR #11 (block10, factorization discharge)

Date: 2026-07-18. Trigger: house rule (evaluator from the third PR
onward, recorded before the PR opens). B09's evaluation listed the
remaining items as the U-integrated measure side, sharp constants,
and "the factorization/spectral surface" — with the first and third
judged to genuinely need other machinery.

## Honest reopening basis (for the factorization item only)

The "other machinery" for the factorization item turned out to be
LANDED repo content: the corner-transfer notes display the many-body
Gaussian identity T_hat^2 = Gamma(t) (free surface) and the
gauge-extension engine DEFINES the fixed-background many-body
transfer as Gamma(t1^(2)[U]) — while importing the functorial
relation as "standard free-fermion". What was missing was one
elementary finite-mode identity (Gamma = e^{dGamma(ln t)}, its trace,
multiplicativity, and log consequences) plus careful object matching
— both within toolkit. Same honest-reversal pattern as B07/B09,
recorded transparently. The U-integrated measure side remains
genuinely outside toolkit and is untouched.

## Criteria

- **Same-surface test.** New content: the native rebuild of the
  imported functorial relation (retiring an import row, per the
  owner's standing rebuild directive); the composition to
  H_MB = dGamma(h[U]) with C = 1; the native 1D activity envelope
  for the corner surface; the worker-verified convention
  reconciliation (a_tau = 1; the T_hat^2 glyph; the channel bridge).
  No sibling touches transfer operators.
- **Marginal value.** This closes the loop the lane opened at
  block08: the conditional transfer-operator reading becomes
  unconditional on the landed corner surface — the lane's
  "transfer identification" item now has its honest final shape
  (done at d = 1 on the corner surface; d = 3 named open with the
  precise missing piece: a 3+1d free-fermion second-quantization
  surface).
- **Worker discipline.** One Opus 4.8 max worker verified the
  four-note object matching against pre-recorded ground truth; its
  two convention flags and its dimension-mismatch finding (the
  biggest catch: corner = 1+1d, sibling envelopes = Z^3) are
  load-bearing parts of the final text.
- **Independent reviewability.** Runner standalone (14 gates, ordered
  manifest); cross-family codex lens before landing.
- **Family shape after this PR.** Remaining: the U-integrated measure
  side (outside toolkit), sharp constants (optimization frontier),
  the d = 3 second-quantization surface (named, precise), and the
  engine note's own realization residuals (its surface). Any further
  family PR re-runs this evaluator against THIS statement.

Verdict: PROCEED. Recorded before PR creation.
