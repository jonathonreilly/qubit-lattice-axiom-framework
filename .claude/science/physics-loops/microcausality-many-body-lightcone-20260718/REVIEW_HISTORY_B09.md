# Review history — block09 (matrix-fiber trace-norm lemma and feed)

## Round 0 — supervisor ground truth (pre-build, recorded in
BLOCK09_PLAN.md)

No workhorse worker this block. The pair trace-norm lemma was
discovered and verified in the supervisor's pre-build session (seven
instances; on-site strictness/saturation; the S1 <= n_f op chain; the
n_f-scaled envelope with the n_f = 1 consistency reduction). During
the session the initial guess ||T|| = ||k||_op was REFUTED by the
identity-fiber computation (norm 2, not 1) and corrected to the trace
norm before any note text existed.

## Mid-lens supervisor additions (timing disclosed)

While the lens ran, the supervisor preemptively added the
complex-kernel instance and the complex-unitary CAR gate (anticipating
the real-only coverage gap), then pinned instance indices after
noticing the complex instance coincidentally shares Sigma sigma = 
sqrt(10) with the non-normal one (|det| = 2 both). The lens read some
mixture of these states; its findings are dispositioned against the
final state.

## Round 1 — combined adversarial lens (codex, read-only,
cross-family), 2026-07-18

Spec: `lens_b09_spec.md`. Output: `lens_b09_out.txt`. Verdict: the
generic lemma/feed survives (its own independent tests: complex 3x3,
degenerate singular values, complex rank-one, I_3, complex-rotation
CAR, joint-spectrum sums — no counterexample found); one BLOCKER on
source-scoping, one BLOCKER on the N-section, one MAJOR on runner
coverage, three MINORs. Dispositions:

1. **BLOCKER — "the CT kernel is scalar" was FALSE.** The CT note
   declares backgrounds in "any compact gauge group `G` (here `U(1)`
   and `SU(2)`)" with a per-site block-kernel convention — the
   supervisor's vocabulary grep (fiber/internal/color/spinor) missed
   it because the CT word is "block". ACCEPTED and REPAIRED
   throughout: the note now carries the source-scope correction
   (needled CT quotes), the framing inverts in this block's favor
   (the SU(2) case NEEDS the fiber feed; the sibling's scalar feed
   covers the abelian case), the sibling's mis-scoping is corrected
   here and flagged on its PR, and fixed-representation-dimension /
   n_f^max language is added. LESSON RECORDED: vocabulary greps must
   include the source's own terms.
2. **BLOCKER — N-section not earned.** Rebuilt: five attempted routes
   (the CT contradiction is route 5 and steelman material), corrected
   residual matching, the false "non-real eigenvalues" sentence
   fixed ([[2,1],[0,1]] has real eigenvalues 2,1; non-normality is
   the point).
3. **MAJOR — runner coverage.** Closed: complex kernel + complex
   unitary gates (added mid-lens), M1b n_f = 3 with DEGENERATE
   singular values (2, 2, 1/2) via an explicit adjacent-pair
   eigenvector plus triangle (no 64x64 eigendecomposition; the first
   attempt hit JW string signs on non-adjacent pairs and was
   corrected to adjacent pairs), M3 full joint-spectrum equality,
   M6 on-site parity, honest gate-kind prose.
4. **MINOR — the sharper direct feed.** Adopted: both envelopes gated
   and displayed (direct exact-pair 293 n_f K; sibling-compatible
   inherited 585 n_f K).
5. **MINOR — eigenvalue sentence** (fixed, above) and **cache at
   landing** (generated below).

## Post-repair state

Runner 14/0 under the ordered label manifest (M1, M1b, M2-M7, six
needles). Batteries: 10 + 4 + 6 = 20 probes, each flipping exactly
its target.
