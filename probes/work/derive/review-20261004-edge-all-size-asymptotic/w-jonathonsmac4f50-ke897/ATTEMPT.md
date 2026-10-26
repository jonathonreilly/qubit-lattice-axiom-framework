# J:derive:review-20261004-edge-all-size-asymptotic:a1 — the all-N lowest level of the cell-cut slab at the top zero line

Worker: Claude Sonnet 5.5 (same family as the source notes; unrefereed, no cross-model confirmation was possible in this task).
Files: `check.py` (13 checks, TOTAL PASS=13 FAIL=0, about 20 s), `RECOVERY_STATUS.json`.

## Plain-language summary

The landed note shows that a half-infinite cell-cut slab has an exact zero-energy surface state that decays by a factor rho per layer, and
that a 50-digit N = 10, 12 comparison at one point (J = (1,1,1), v = 0.2) agrees with "energy shrinks by rho^2 per added layer". That is
a diagnostic. Here the finite-slab lowest level is computed for every N from the layer recurrence.

- Result 1 (proved, explicit constants). For J_x = J_y, kappa J_z != 0, 0 < v < 1, N large enough, the lowest |E_N| equals
  `s_N^2/|q0|` up to a relative error that is at most a computable multiple of rho^N, where s_N is the smallest singular value of the
  one-sided block matrix U_N and `q0` is a closed-form number proportional to `cos(pi v) * Br`. In the limit,
  `E_N / rho^(2N) -> -(1 - rho^2)^2 X / q0`, with a closed-form X.
- Result 2 (counterexample to reading the diagnostic as a law). `q0 = 0` at v = 1/2 and, for every other v, at one value `J_x*(v)` of the equal
  in-plane coupling. There the lowest level is of order rho^N (one power, a plus-minus pair), not rho^(2N), with explicit two-sided bounds.
  So "rho^2 per layer" holds exactly on the domain `q0 != 0`, not on all of the coupling domain.
- Result 3. At v = 0 the compact layer-0 mode is an exact zero mode of every finite slab: E_N = 0 for all N.

The first unresolved step (Step 12): the proved relative remainder is O(rho^N); numerics show O(rho^(2N)) (possibly with a polynomial prefactor).

## 0. Provenance and what was read (stated as required)

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (the four axioms: Lattice, Qubit, Admissibility, Record, lines 33-83; qualification and
  "Axioms and approved primitives are the complete supplied foundation", lines 85-112) and
  `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive`, lines 29-130). None of the three primitives is used or needed below. Nothing here is derived from the axioms.
- Source objects, sha256 verified at `2868a0c453e667d1267f0e1e7403732a11893d78` and identical at current main `a77a3449c91a753b06ce2a63876cd460b62cb4cf`
  (2868a0c is an ancestor): the note `docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_THE_CELL_CUT_SLAB_...BOUNDED_THEOREM_NOTE_2026-10-01.md`
  (`0e547659...12e41f8`) and the runner `scripts/composite_site_network_flux_free_exact_surface_zero_line_of_the_cell_cut_slab_2026_10_01.py`
  (`9bda5e19...4d1`).
- Prior art search: other `COMPOSITE_SITE_NETWORK_FLUX_FREE_*` notes on main (surface arcs note, cubic flip note), the ai/probes `work/derive` tree and
  open PRs matching slab/surface/edge/composite. No landed or open note derives a finite-N level or a coupling domain for the rho^2 ratio. The only
  finite-N statement is note line 73 ("N = 10,12 ... not a proved all-N asymptotic"). The related task `deferred-20260925-band-gauge` concerns a different
  model (relaxed compass carvings) and has no overlap.
- `claim.py`, `run_probe.py`, commits: not used. The task bars repository edits; this attempt wrote only in the output folder.

## 1. Setting and premises (ASSUMED, all supplied)

A1. (ASSUMED, supplied) The u = +1 quadratic Majorana comparator of the landed notes, one copy, landed hopping-sign convention, H(f) = iM(f),
cell-cut stack along a3, layers 0..N-1, hoppings leaving the stack dropped (so the finite slab is the plain truncation), momenta (f1, f2) = (u, v).
The network is transcribed in `check.py` from the landed definition. This is a supplied model, not framework-law content, and no axiom is used to
select it.

A2. (ASSUMED, scope) J_x = J_y real (any sign, zero allowed), kappa != 0, J_z != 0 real, u = 1/2, v in (0,1) except Step 11 (v = 0).
Notation: q = e^{i pi v}, z2 = q^2, sigma = sin(pi v), c = cos(pi v). Only J_z^2 enters rho; J_z J_x enters q0 (use |J_z| in rho).

A3. (READING, not used) Layer states with these quantum numbers are "surface" states; no physical identification is made.

## 2. Block form of the finite slab (PROVED from the landed block structure; CHECKED S1, S2)

Let A = H_{L,L}, B = H_{L,L+1}, B^dagger = H_{L+1,L}. At u = 1/2, J_x = J_y, with p = sites {0,1}, q = sites {2,3}:

- A_pp = 0 (landed note:35-42, the p-block is -2(J_x - J_y) sigma_y); B has only the entries [2,0], [3,0], [3,1], i.e. rows q, columns p, so B_pp = B_pq = B_qq = 0 (note:35-39);
- A_qp = A_s = [[4ik, 2iJ_z],[0, 2ik(z2-1)]], B_qp = B_s = [[-2ik(z2-1)/z2, 0],[-2iJ_z, 4ik]] (landed runner:242);
- A_qq = Q = [[2ik(z2^2-1)/z2, 2iJ_x(z2+1)/z2],[-2iJ_x(z2+1), 2ik(1-z2^2)/z2]]. This block is not displayed in the landed note. It is Hermitian and
  traceless with eigenvalues +-qbar, `qbar = 4|c| sqrt(4k^2 sigma^2 + J_x^2)`. `check.py` S1 rederives it, and A_pp = 0, from the hopping list with free symbols.

Ordering all p-components first, then all q-components, H_N = [[0, U^dagger],[U, Qhat]], where U is the 2N x 2N upper block-bidiagonal matrix with
A_s on the diagonal and B_s above it, and Qhat = 1_N (x) Q. (Row q_L meets p_L through A_s and p_{L+1} through B_s.) S2 confirms numerically against the slab built
straight from the hopping list. The remaining steps use only this block form.

Since the p-p block vanishes, det H_N = +- |det U|^2 = |det A_s|^{2N} (landed note, runner (9)), so E_N != 0 for v != 0.

## 3. U^{-1} (PROVED; CHECKED exactly at a rational point, S4)

For v != 0, det A_s = -8k^2(z2-1) != 0, so U is invertible and block triangular with `(U^{-1})_{L,L'} = T^{-(L'-L)} A_s^{-1}` for L' >= L, 0 otherwise,
where `T = -B_s^{-1} A_s` (the landed transfer matrix; det B_s = 8k^2(z2-1)/z2 != 0). Proof: U = D(1+Nil), D = diag(A_s), Nil_{L,L+1} = A_s^{-1}B_s,
U^{-1} = sum_k (-Nil)^k D^{-1} and -A_s^{-1}B_s = T^{-1}. S4 verifies this for N = 4 exactly (Gaussian rationals).

## 4. Spectral data of T in closed form (PROVED; CHECKED symbolically S3 and exactly S4)

Let rho in (0,1) solve rho + 1/rho = tau := sigma + (4k^2 + J_z^2)/(4k^2 sigma). It exists and is unique because tau >= sigma + 1/sigma + J_z^2/(4k^2 sigma) > 2. It is the landed
rho. Since tau - (sigma + 1/sigma) = J_z^2/(4k^2 sigma) > 0 and x + 1/x is decreasing on (0,1): `rho < sigma < 1` (the landed note's remark).

Write lam = -i q rho (= rho e^{i pi(v - 1/2)}), lam_out = -i q/rho. The relation `J_z^2 = 4k^2 (sigma(rho + 1/rho) - sigma^2 - 1)` is symmetric under rho <-> 1/rho. With M(l) = A_s + l B_s,

- e = (1, r), r = -J_z rho/(2k(sigma - rho)), satisfies M(lam) e = 0;
- w = (2ik q (sigma - rho), -J_z) (a row) satisfies w M(lam) = 0;
- `w B_s e = 2i sigma W/(sigma - rho)`, `W := |w|^2 = 4k^2(sigma-rho)^2 + J_z^2`, and `w Q w^dagger = 8 k c Br`,
  `Br := sigma(J_z^2 - 4k^2(sigma-rho)^2) + 2 J_x J_z (sigma - rho)`.

Each is a polynomial identity modulo the relation; S3 verifies them exactly for free symbols (q, rho, k, J_z, J_x), and the same with rho -> 1/rho for lam_out. Hence T e = lam e, and since lam lam_out = -z2 = det T
(landed) the eigenvalues of T are lam (modulus rho) and lam_out (modulus 1/rho): distinct, T diagonalisable. With f := w B_s/(w B_s e) one has f T = lam f, f e = 1 and `g^dagger := f A_s^{-1} = -w/(lam (w B_s e))`.
Write e', f', g' for the same objects at lam_out (rho -> 1/rho). Then
`T^{-k} A_s^{-1} = lam^{-k} e g^dagger + lam_out^{-k} e' g'^dagger`, with `||e g^dagger|| = 1/(rho sqrt X)`, `||e' g'^dagger|| = rho/sqrt X'`, where
`X = 16 k^2 sigma^2 W/(4k^2(sigma-rho)^2 + J_z^2 rho^2)` and X' is X with rho -> 1/rho. (Scale-free ratio `|wB_s e|^2/(|e|^2 |w|^2)`; checked numerically S5e.)

Define the real number `q0 := g^dagger Q g/|g|^2 = w Q w^dagger/|w|^2 = 8 k c Br/W` (g is parallel to w^dagger). Note it contains the factor cos(pi v).

## 5. Rank-one part and remainder of U^{-1} (PROVED; CHECKED S5e)

Put `R_{L,L'} := lam^{L-L'} e g^dagger` for ALL L, L' in 0..N-1 (a rank-one matrix: R = (a (x) e)(b (x) g)^dagger, a_L = lam^L, b_{L'} = conj(lam^{-L'})),
and `Delta := U^{-1} - R`. Then Delta is block Toeplitz: block k = L' - L equals `lam_out^{-k} e' g'^dagger` for k >= 0 and, for k <= -1, `-lam^{-k} e g^dagger`.
A block Toeplitz matrix has operator norm at most the sum of its block norms, so
`||Delta|| <= delta := (rho ||e g^dagger|| + ||e' g'^dagger||)/(1 - rho) = (1/sqrt X + rho/sqrt X')/(1 - rho)`.
Also `||R|| = Sigma_N := |a||b| ||e|| ||g|| = (S1 S2)^{1/2}/(rho sqrt X)` with S1 = sum rho^{2L}, S2 = sum rho^{-2L} (L < N). Since S1 S2 = rho^{2-2N}(1-rho^{2N})^2/(1-rho^2)^2,
`Sigma_N = rho^{-N}(1 - rho^{2N})/((1 - rho^2) sqrt X)`. R = Sigma_N xi eta^dagger with unit vectors xi (p-space, profile a (x) e: the landed surface mode, truncated) and
eta (q-space, profile ~ lam^{-L} g, growing toward the last layer). Because Q is the same on every layer, `eta^dagger Qhat eta = q0` exactly, for every N.

## 6. Theorem A: the smallest singular value (PROVED)

s_N := sigma_min(U_N) = 1/||U^{-1}||, so by Step 5: `|1/s_N - Sigma_N| <= delta`. If Sigma_N > delta, then
`s_N = (1-rho^2) sqrt X rho^N (1 + theta_N)/(1 - rho^{2N})`, `|theta_N| <= delta/(Sigma_N - delta) = O(rho^N)`.
CHECKED S5a, S5e (5 couplings x N = 8, 12, 16 and N = 8).

## 7. The universal bound |E_N| <= s_N (PROVED; CHECKED S5b)

With x0 the unit right singular vector of U for s_N, the vector (x0, 0) obeys ||H_N (x0,0)|| = s_N, so min |eig| <= s_N.

## 8. Theorem B: the level when q0 != 0 (PROVED, conditional on the explicit inequality N0; CHECKED S5c, S5d)

H_N is invertible with `H_N^{-1} = [[-U^{-1} Qhat U^{-dagger}, U^{-1}],[U^{-dagger}, 0]]` (solve H(x;y) = (f;g): y = U^{-dagger} f, x = U^{-1}(g - Qhat y)).
Substitute U^{-1} = R + Delta: `H^{-1} = H0 + V`, where H0 uses R only, V collects every term containing Delta, so
`||V|| <= v_N := 2 Sigma_N qbar delta + qbar delta^2 + delta`.
H0 is supported on span{(xi,0),(0,eta)} where it is `Sigma_N [[-a, 1],[1, 0]]`, `a := Sigma_N q0`; its other eigenvalues are 0. Its two nonzero eigenvalues are
`mu_d = -sgn(a) Sigma_N (|a| + sqrt(a^2+4))/2` and `mu_s = sgn(a) 2 Sigma_N/(|a| + sqrt(a^2+4))`, with |mu_d| >= Sigma_N^2 |q0| and |mu_s| <= 1/|q0|.
Equivalently 1/mu_d = E_pred is the root of smaller modulus of `E^2 - q0 E - 1/Sigma_N^2 = 0`: [[0, s],[s, q0]] with s = 1/Sigma_N.

Claim: if (N0) `|mu_d| - v_N > |mu_s| + v_N`, then `E_N := lowest |eig H_N|` satisfies `E_N = 1/(mu_d + eps)` with `|eps| <= v_N`, hence
`|E_N/E_pred - 1| <= eta/(1 - eta)`, `eta := v_N/|mu_d| <= v_N/(Sigma_N^2 |q0|)`.
Proof. Weyl's inequality for the extreme eigenvalue of the Hermitian matrices H0 and H0 + V on the side of mu_d; the other eigenvalues of H^{-1} have modulus at most |mu_s| + ||V||
(0 and mu_s each move by at most ||V||), which under (N0) is below |mu_d| - ||V||. So the extreme eigenvalue of H^{-1} on the mu_d side is 1/E_N. QED.
Since Sigma_N >= rho^{-N}(1-rho^{2N})/((1-rho^2) sqrt X), v_N = O(rho^{-N}) and |mu_d| = O(rho^{-2N}) for q0 != 0, (N0) holds for all large N and eta = O(2 qbar delta/(Sigma_N |q0|)) = O(rho^N).
S5c checks the inequality with the exact levels (5 couplings x N = 8, 12, 16; all 15 runs satisfy (N0)). The bound is loose: the observed relative errors are several orders below the bound in every run (see the S5c output).

## 9. Corollary: the all-N asymptotic with constants (PROVED from Steps 6, 8; limit CHECKED S6)

For q0 != 0: `E_N = E_pred(N)(1 + O(rho^N))`, `E_pred(N) = (q0 - sgn(q0) sqrt(q0^2 + 4 s_N^2))/2 = -s_N^2/q0 (1 + O(s_N^2))` where s_N is replaced by 1/Sigma_N, and therefore

  `lim_{N->inf} E_N/rho^{2N} = -(1 - rho^2)^2 X / q0 = -sgn(k c Br) * C`,
  `C = 2|k| sigma^2 (1-rho^2)^2 W^2 / (|c| |Br| (4k^2(sigma-rho)^2 + J_z^2 rho^2))`.

(Algebra: X/|q0| = [16 k^2 sigma^2 W/(...)] * W/(8|k c Br|).) The sign law is sign(E_N) = -sign(k c Br). Domain: any real J_x = J_y, kappa J_z != 0, v in (0,1), v != 1/2, Br != 0.
CHECKED S6: five parameter sets, including negative kappa, negative J_z, v > 1/2 and J_x of either sign; signs agree with 40-digit slabs, and the relative remainder of E_N/rho^{2N} against the limit at N = 6, 9, 12 decays at the rate rho^{2N} up to a modest prefactor (the check requires at most 1000 rho^{24} at N = 12
and a factor at most 30 rho^6 per three layers).

The landed N = 10, 12 ratio is the special case: S8 reproduces `(E12/E10)^(1/2)/rho^2 - 1 = -1.6e-16` (k = 0.3) and `-8.9e-10` (k = 0.6) and finds
`E_10 = E_pred(10)(1 + 3e-16)` and `(1 + 1.7e-9)`, i.e. the diagnostic is an instance of Step 9 (the ratio of consecutive layers of E_pred is rho^2 (1+O(rho^(2N))) because Sigma_N^{-2} ~ rho^{2N}(1-rho^2)^2 X).

## 10. Theorem C: q0 = 0 gives one power of rho, and this happens inside the coupling domain (PROVED; CHECKED S7)

q0 = 0 iff `c = 0` (v = 1/2) or `Br = 0`. For given (kappa, J_z, v), v != 1/2, Br = 0 is linear in J_x:
`J_x*(v) = sigma(4k^2(sigma-rho)^2 - J_z^2)/(2 J_z (sigma - rho))` (sigma - rho > 0, J_z != 0, so it exists for every v in (0,1)). So for every (kappa, J_z, v) there is a real equal in-plane coupling at which q0 = 0.

Then R Qhat R^dagger = Sigma_N^2 q0 xi xi^dagger = 0, the first block of H^{-1} reduces to cross terms, and
`||H_N^{-1}|| <= 2 Sigma_N qbar delta + qbar delta^2 + ||U^{-1}|| <= v_N + Sigma_N`, hence `1/(v_N + Sigma_N) <= |E_N| <= s_N <= 1/(Sigma_N - delta)` (Step 7).
Both ends are of order rho^N. So `|E_N| = Theta(rho^N)` and `|E_N| / rho^{2N} -> infinity`: the rho^2-per-layer ratio does not hold there.
S7: three (kappa, J_z, v) at J_x = J_x*(v) (v = 0.2, 0.7, 0.35; mixed signs) and v = 1/2 at J = (1,1,1), kappa = 0.3. Checked: `|E_N|/rho^N` at N = 6, 10, 14 equals 1.68090632, 1.68090631, 1.68090631
(first set), and the explicit two-sided bound holds. At q0 = 0 the exact asymptotic coefficient of rho^N is `(1-rho^2) sqrt X / sqrt(1 + nu)` with nu = O(1) (READING from a Schur-complement sketch, not checked: the first set gives 2.36018 for the
nu = 0 value versus 1.68091 observed, which would mean nu ~ 0.97). nu is not derived here (Step 12).

## 11. v = 0 (PROVED; CHECKED exactly S4b)

At v = 0 (z2 = 1): A_s (z2=1) (J_z, -2k)^T = 0 and B^dagger has zero p-columns, so psi = (J_z, -2k, 0, ..., 0) (layer 0 only, p-sites) obeys H_N psi = 0 for every N >= 1, and J_x enters nowhere.
Thus E_N = 0 exactly (consistent with det A_s = 0 at v = 0 and with rho -> 0 as sigma -> 0 in the rho^{2N} law).
S4b verifies H_N psi = 0 for N = 1..8 in exact rational arithmetic at J_x = 1/2, J_z = 8/5, kappa = 1. The compact mode is not part of the rho law and is handled separately, as the task asks.

## 12. FIRST UNRESOLVED STEP

Upgrading the proved relative remainder O(rho^N) (Step 8, crude `||V||` bound inside Weyl) to the observed O(rho^{2N}). The cross terms R Qhat Delta^dagger + Delta Qhat R^dagger give a first-order shift <V> in the dominant
eigenvector that is, by the profile of a and b, bounded by a polynomial in N (a sum of unimodular phases against geometric profiles), not by Sigma_N; a second-order Feshbach bound would then give O(N^k rho^{2N}).
This is `suggested`, with the observed ratios (S6: rel. error 1e-9, 1e-12, 1e-14 at N = 6, 9, 12 for J = (1,1,1), k = 0.3) as support; it is not proved.

Other open items: (i) the sharp coefficient of rho^N at q0 = 0 (needs nu); (ii) the inequality (N0) is explicit and computable but is not turned into a closed-form N0;
(iii) J_x != J_y (A_pp = -2(J_x - J_y) sigma_y != 0, first-order shift, outside this chiral structure); (iv) the mirror statement on the bottom line v = 1/2;
(v) an independent (different-model-family) referee of Steps 3-10.

## 13. What is new, what is not

Not new: the block structure, the transfer matrix T, rho, the exact zero-mode line and the N = 10, 12 ratio at v = 0.2 (landed note and runner); the v = 0 compact mode (landed, but only for the half-infinite slab).
New in this attempt (same-family, unrefereed): the reduction of H_N to [[0,U^dagger],[U,Qhat]] with the explicit A_qq; closed forms for Sigma_N, delta, q0, X, the sign law and the constant C;
the proved O(rho^N) relative remainder with explicit constants and condition (N0); the exact finite-N zero at v = 0; the coupling-domain statement that q0 = cos(pi v) Br decides between the rho^{2N} law and a Theta(rho^N) law, and the explicit family J_x*(v).
The finite-slab constant depends on J_x through Q, even though the transfer matrix does not.
Nothing here is an axiom consequence; the lane supplies the comparator, the cut and the couplings; "surface state" and any link to the spin model remain readings and are not used.
