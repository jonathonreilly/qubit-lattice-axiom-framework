# Block08 plan — gauged-kernel weighted-activity feed (fixed background)

Date: 2026-07-18. Eighth block, the candidate next step B07's evaluator
named. Content: the CT note's fixed-background log-transfer kernel
bound (G5: ||<x|h[U]|y>|| <= Const(m,d) e^{-gamma_CT ||x-y||_inf},
BOTH constants independent of U and of volume) feeds the
second-quantized bilinear generator into block07's weighted class:
for every mu < gamma_CT/3,

  kappa <= K + 8 K x (13 + 10x + x^2)/(1-x)^3,  x = e^{-(gamma_CT - 3 mu)},

so block07's LR display applies to the fixed-background many-body
log-transfer bilinear dynamics, with a background-independent kappa
bound — the fixed-background half of the CT note's open item (iii)
many-body LR composition. The U-integrated measure side stays open.

## Supervisor ground truth (verified pre-worker, sympy session)

- numerator 24x(1+x) + 2x(1-x)^2 = 26x + 20x^2 + 2x^3 = 2x(13+10x+x^2)
- kappa/K at x = 1/2: 585 exactly
- l_inf shells: 26, 98, 218 = 24r^2+2 at r = 1,2,3
- ||z||_1 <= 3 ||z||_inf (enumeration instances; per-coordinate proof)
- factor bookkeeping: ||h_{xy}|| <= 2K e^{-eta r} (Hermitian kernel
  pair, ||c^dag_x c_y|| = 1) times |S| = 2 gives the 4K; times the
  shell closed form gives the 8K in the total.
- threshold mu < gamma_CT/3 matches Note 3's d mu < eta pattern at
  d = 3.

## Worker (Opus 4.8 max, workflow w0l0lo43p)

Independent line-by-line verification of steps 1-9 including the toy
Z_2-background uniformity exhibit design (3-site chain, all 8 sign
backgrounds, identical pair norms hence identical kappa). Graded
against the above before use.

## Scope honesty

The kernel bound is SUPPLIED (cited to the CT note's own surface;
Combes-Thomas is not re-proved); the second-quantization step and the
CAR norm facts are this note's content, gated; "fixed background" is
load-bearing everywhere; U-integration, sharp constants, and the
transfer-operator spectral side beyond the kernel bound remain open.

## Cluster discipline

PR #8: evaluator recorded before PR; honors B07's forward statement
(this is the named candidate next step, not a reopening).
