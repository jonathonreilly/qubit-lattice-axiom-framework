# T-2AMP pre-registration (written 2026-10-18T21:55Z, before any run)

Item: T-2AMP in `masswall/TESTS.md` (readings fixed there; copied below unchanged in meaning).
Background: `masswall/R1/REPORT.md`; code reused from `masswall/R1/scripts/native_menu.py` (group, reps,
equivariant-image construction) and `native_fit*.py` (scoring, control generator).

## Model (fixed now)

- Group: G' = Z2^3 x| O (192 elements), R1's law (t1,R1)(t2,R2) = (t1 + |R1| t2 mod 2, R1 R2).
- Spurion pairs (both isotropy-safe singly in R1's census):
  - (a) sigma1 = A2 pseudoscalar, n1 = +1; sigma2 = C111 staggered sign field, n2 = +1.
  - (b) sigma1 = A2 pseudoscalar, n1 = +1; sigma2 = S (hw1 corner star) along (111), n2 = (1,1,1)/sqrt3.
- Generation labels (primary): V = P (axis permutation) and V = S (hw1 node triplet).
- Placement (primary, "every particle type shares one label"): Q = u^c = d^c = L = e^c = V.
- Yukawa: Y_f(e1,e2) = sum over bi-degrees (k1,k2), k1 + k2 <= 8, of e1^k1 e2^k2 sum_j c^f_{k1k2j} B_{k1k2j},
  with B an orthonormal basis of span{h(n1,n2)} over bi-degree-(k1,k2) equivariant polynomial maps
  (sigma1, sigma2) -> V_L (x) V_R (group-averaged monomials, R1's construction extended to two fields);
  c complex standard normal, independent per sector (up, down, lepton) and per draw.
- Draws: 5 coefficient draws; the reading uses draws 1-3 (as TESTS asks for >= 3); draws 4-5 are reported
  as robustness only.
- Free parameters: e1, e2 on a common 40 x 40 log grid in [1e-3, 0.6] each (shared by all sectors),
  and one scale per sector (absorbed analytically, as R1). No other freedom.

## Data (comparator only; recalled, not fetched)

HIER-2's three mass sets (branch `claude/hierarchy-scale-ladder-20261018`, `H2/PREREG.md` lines 35-38):
- MZ: u 1.27e-3, c 0.619, t 171.7; d 2.90e-3, s 0.055, b 2.89; e 0.48657e-3, mu 0.102718, tau 1.74624.
- GUT: u 0.48e-3, c 0.235, t 74.0; d 1.14e-3, s 0.022, b 1.00; e 0.469652e-3, mu 0.0991466, tau 1.68558.
- MIX: u 2.16e-3, c 1.27, t 172.69; d 4.67e-3, s 0.0934, b 4.18; e 0.511e-3, mu 0.1057, tau 1.777.
- CKM (HIER-2's recalled values, used for all three sets): |V_us| 0.225, |V_cb| 0.041, |V_ub| 0.0037.

## Score (R1's, unchanged)

Per sector: half-spread of log(model singular values / observed masses), sorted ascending (= best sector
scale). CKM: |log|V_model| - log V_obs| for (us, cb, ub), V = U_u^dag U_d with columns ordered light to
heavy. Total = max over the four. Factor = exp(total). Within x3 means factor <= 3.
Search = min over the e1-e2 grid and over the 4 primary models {(a),(b)} x {P,S}, per draw.

## Control

300 random spectra, R1's generator (seed 7 stream): per sector r21, r32 log-uniform in [1e-4, 1], masses
(r21 r32, r32, 1); |V_us|, |V_cb|, |V_ub| independently log-uniform in [1e-3, 0.5]. Same search, same draws.
Random pass rate = fraction of control spectra meeting the PASS criterion (best within x3 in >= 2 of draws 1-3).

## Readings (from TESTS.md, fixed)

- 2AMP-PASS: best fit within x3 on all 12 numbers in at least 2 of 3 draws, and random pass rate <= 5%.
- 2AMP-FAIL: no fit within x3, or random pass rate > 20%.
- OPEN: otherwise.
Applied per mass set; the overall reading is PASS only if all three sets PASS, FAIL if all three FAIL.

## Checks also run

1. Up/down ratio check: exponent structure per sector (numerical bi-degree orders of each singular value),
   and at the best fit the model (m1/m3)_up / (m1/m3)_down against the observed x136 (MZ), x176 (GUT), x89 (MIX).
2. Isotropy at every order: (i) rank of equivariant images (sigma1, sigma2) -> W (traceless symmetric
   2-tensors, trivial translation) at the vacuum for every bi-degree with k1 + k2 <= 8; (ii) symmetry count
   of generation-dependent speed tensors, dim Inv_H(V (x) V (x) W) versus dim Inv_G'(V (x) V (x) W).
3. Residual group H = stabiliser of (n1, n2): order, rotation part, action on V (scalar / irreducible /
   number of distinct characters), and the commutator ||[Y_u Y_u^dag, Y_d Y_d^dag]||.

## Secondary arms (reported, do NOT enter the reading)

- chiralL placement: Q = L = V, u^c = d^c = e^c = internal (triv3), V in {P, S}.
- R1's character labels D_A1_A1_A2, D_A1_A2_A2, D_A1_C111_C111A2, D_A1_A2_C111, D_A1_A1_C111, blind and chiralL.
  Each secondary arm gets its own control pass rate under its own search.

## My prediction (stated before running)

2AMP-FAIL on all three sets, with no primary fit near x3, for structural reasons I expect to hold exactly:
- Pair (a) residual H = {(t,R): R in T, t even}; pair (b) residual H = {(0,R): R in T}. Both contain the C3
  about the body diagonal, so isotropy holds at every order (proved by the stabiliser argument; check 2(i)
  should give rank 0 throughout).
- Same reason kills CKM (R1 Lemma B; main's shared-C3 theorem, `THE_SMALL_MIXING_ANGLES_..._C3_BREAKING`):
  P restricted to T is 1 + omega + omega-bar, so V_CKM is a permutation matrix (P in both pairs, S in pair b);
  S restricted to pair (a)'s H is irreducible, so all three masses are exactly degenerate.
- Blind placement allows the identity Yukawa at order zero, so no sector gets a 1e-5 hierarchy anyway.
- Control pass rate near 0%.
