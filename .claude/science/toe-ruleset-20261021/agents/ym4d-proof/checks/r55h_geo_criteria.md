# r55h_geo — criteria (written BEFORE checks/r55h_geo.py exists). Reviewer: claude-opus-5-5 (REVIEW55_HWPLD).

Exact integer arithmetic only (Python ints and sets; no floats in any verdict; no numpy, no BLAS).
Conventions exactly as HW.md §35.2: level-j cubes indexed by Z^4, pi = coordinatewise floor(./3),
N_t = l-infinity radius-t neighbourhood, Sigma(X) = N_1(pi(X)), sh_{j+r}(X) = Sigma^r(X),
||X||_sh = sum_{r=0..M} |Sigma^r(X)| over the levels j..j+M.
Every constant below is quoted from a file written before this review (source named); none is derived here.

## G-A  Proposition SH-neg (HW.md §35.4, "excess = 27M + 55", PRE-REGISTERED as a reproduction of a prior-session claim)
Construction verbatim from HW §35.4: zeta = (3^{M+1}-1)/2, z = (zeta,zeta,zeta,zeta), y = z + 8 e_1, P = {z}, Y = {y}.
- G-A1: compute E(M) := ||P u Y||_sh - ||P||_sh by DIRECT 4D set computation for M = 2..7.
- G-A2: compute E(M) by the coordinatewise product reduction HW §35.4 (iii) uses, for M = 2..60.
- PASS iff G-A1 and G-A2 agree wherever both are computed AND E(M) = 27M + 55 for every M computed.
  FAIL (Proposition SH-neg REFUTED) iff any computed E(M) differs from 27M + 55.
- G-A3 (records the sentence "the two projections stay at distance 1 for ever", HW §35.4 diagnosis paragraph and §40
  W1 (b)): record d_r := pi^r(y)_1 - pi^r(z)_1 for r = 0..M at M = 30. The sentence is CONFIRMED iff |d_r| = 1 for every
  r with 2 <= r <= M; REFUTED iff |d_r| != 1 for some such r. (Either outcome is reported; G-A3 does not affect G-A's PASS.)

## G-B  The "depth-free" per-cube shadow excess of PLD §16.6 (b) / §18.5 (b') (PRE-REGISTERED; outcome unknown when written)
PLD claim (§18.5 (b'), l.2266-2270): for every level-k cube Q and every level-(k-1) cube x_Q under Q,
sum_m (|sh_m(x_Q)| - |sh_m(Q)|) <= Delta_sh = 3073361, depth-free; hence ||x(S)||_sh <= ||S||_sh + (1 + Delta_sh)|S|.
Test family (chosen because it is the all-ones base-3 mechanism of HW §35.4 applied one level down, not because its answer
is known): Q = (q,q,q,q) with q = 3*w, w = (3^{D}-1)/2, S = {Q}, x_Q = the child (3q,3q,3q,3q); depth D levels above Q.
- G-B1: direct 4D set computation of ||x(S)||_sh - ||S||_sh for D = 2..7 (validates the product reduction).
- G-B2: product (1D interval) reduction for D = 2..60, and for D = 20000 (single evaluation).
- REFUTED (the depth-free claim is false) iff the computed excess at some D exceeds 1 + 3073361 = 3073362, OR the
  per-level increments are bounded below by a positive constant over D = 10..60 (which makes the excess unbounded in D).
  CONFIRMED (no counterexample in this family) iff the excess is bounded by 3073362 at every computed D and the increments
  are not bounded below by a positive constant.
- G-B3 negative control (must NOT refute): the same computation at Q = (q,q,q,q) with q = w (all-ones position itself);
  PLD's bound must hold there for all computed D (if it fails there too, the family is not discriminating and G-B carries
  less weight; reported either way).

## G-C  Ring set identities (HW §35.6 Lemma RING; PLD §19.1 Finding (BUF-CC)) — PRE-REGISTERED
Samples: 200 random finite sets Gamma (1..6 level-(j+1) cubes in a box of side 30, random positions incl. positions whose
coordinates are all-ones in base 3), and 200 random sets X (1..8 level-j cubes), seeded, depths M = 8.
- G-C1: pi(N_1(col(Gamma))) == N_1(Gamma) as sets (col = the 81 children). PASS iff equality on every sample.
- G-C2: for every r = 1..M, pi^r(N_1(X)) is a subset of Sigma^r(X). PASS iff inclusion on every sample and every r.
- G-C3 (records, no pass/fail): max over samples of [sum_{r>=1}|pi^r(N_1 X)|] / [sum_{r>=1}|Sigma^r X|] and of
  [|N_1 X| + sum_{r>=1}|pi^r(N_1 X)|] / ||X||_sh.
- G-C4 (control on the HW quoted bound, CONFIRMATORY of a proven statement): |Sigma^r(N_1 X)| <= 16|Sigma^r X| for r >= 1.
  PASS iff 0 violations.
A violation in G-C1 or G-C2 would refute the reviewer's own hand derivations in REVIEW55_HWPLD.md; it is reported as such.

## Scope
Exact geometry of floor blocking on Z^4 only. Nothing here tests any measure, (E2^F), (CEM^COL), or Theorem CRC-2T'.
