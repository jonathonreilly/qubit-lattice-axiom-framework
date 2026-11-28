lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1114

Checker: Claude Opus 5.5, effort max, laptop subagent.
This is a cross-provider check. The writer of row 1110 is gpt-6-astra max.

## Plan (brief read; one item per response)

Brief: FINISH row 1114 at clone commit `eef915fdb`, branch
`claude/ym4d-hard-route`. Object: `library/gap-face-order-one-astra.md`
(row 1110, 855 lines), read in full. Cited lemmas read at the named
lines: row 1076 `gap-bridge-vectors-max.md` L200-400 (CB-T, P4-ORB,
CB-CH, SING); row 1084 `gap-checkerboard-singlet-astra.md` L49-186,
L402-607, L711-763; row 1091 `gap-face-stability.md` L1-195 (M1, M2,
FST-BD with its proof, FST-P, FST-F). During the check the branch moved
to `a71aba758` (two commits by others for row 1113); `git diff` from
`eef915fdb` leaves all four input files unchanged.

Items, each with HOLDS, HOLDS AFTER CORRECTION or FAILS:

1. (O1)-(O3), with the trace density (O2).
2. (O4)-(O5): the reduction to one right-twisted bond of strength at most
   2b, and the use of OpenAI (3.61) inside its stated class (source pages).
3. (O6)-(O7) and the statement NR.
4. (K1)-(K4), the constrained end.
5. (K5)-(K8), the first correction.
6. (K9), the limit.
7. (B1)-(B4), the block sum.
8. The claim X >= 1/4 in 4.2.
9. SSB with the hand inequality (B7).
10. The U(1) control (U1).
11. The stop by the third rule, and the nature of the three failures.
12. RESULT line.

Status: all twelve items done (2026-11-17). Verdicts below; RESULT at the end.

## Item 1. (O1)-(O3) and the trace density (O2): HOLDS

Read line by line: note L127-178, with P4-ORB (row 1076).

- (O1) is the orbit map of the base point `p_t = (1, 1, 1, h(t)^(-1))`
  under the corner action of P4-ORB:
  `q_1 -> g_1 q_1 g_2^(-1)`, `q_2 -> g_2 q_2 g_3^(-1)`,
  `q_3 -> g_4 q_3 g_3^(-1)`, `q_4 -> g_1 q_4 g_4^(-1)`.
  Put `p_t` in and (O1) comes out exactly. The holonomy is
  `g_1 g_2^(-1) g_2 g_3^(-1) g_3 g_4^(-1) g_4 h g_1^(-1) = g_1 h g_1^(-1)`,
  so `Re H = t`. By P4-ORB the level set `{Re H = t}` is one orbit (the
  trace fixes the SU(2) conjugacy class). So the image is the whole level set.
- The uniqueness argument is correct: for an invariant `nu`,
  `int f dnu = int int f(g p) dg dnu(p)`, and the inner integral does not
  depend on p by right invariance of Haar measure.
- The sentence "both laws are invariant" uses the standard fact that a
  disintegration of an invariant measure over an invariant map can be
  chosen invariant for almost every t. That is correct but compressed.
  A direct proof, which I checked: take `g_1, ..., g_4, h` independent
  Haar and map them by `q_1 = g_1 g_2^(-1)`, `q_2 = g_2 g_3^(-1)`,
  `q_3 = g_4 g_3^(-1)`, `q_4 = g_1 h^(-1) g_4^(-1)`. Given `(g_2, g_3)`,
  `q_1` and `q_3` are independent Haar, while `q_2 = g_2 g_3^(-1)` is a
  Haar function of `(g_2, g_3)` alone; so `q_1, q_2, q_3` are independent
  Haar. Given all `g_j`, `q_4` is Haar. So the image law is product Haar, and
  `Re H = Re h`. Given `Re h = t`, `h = k h(t) k^(-1)` with k Haar.
  Replace each `g_j` by `g_j k` (again independent Haar): this is (O1).
  So the conditional law given t is the pushforward of (O1) for every t.
- (O2): Haar measure is `(2/pi) sin^2(theta) dtheta dn` in polar form;
  `int_0^pi sin^2 = pi/2`; `t = cos(theta)` gives
  `(2/pi) sqrt(1 - t^2) dt`, of total mass one. Correct.
- (O3): apply the one-site disintegration at every site with independent
  lifts. Since `x_u = t_u`, the marginal and the conditional law are as
  displayed, and the conditional law does not depend on kappa. `W_b` is
  positive and continuous (S_b is continuous on a compact set; h(t) is
  continuous on [-1, 1]); `W_0 = 1`. Correct.

Verdict: **HOLDS.** No change of statement. The direct lift above can
replace the compressed invariance sentence.

## Item 2. (O4)-(O5), the conditional charged port: HOLDS, given (3.61)

Read line by line: note L180-244.

**The reduction (O4).** I computed all four corners. Each `g_j` enters
exactly two sheets. With cyclicity of Re and `Re x = Re x^(-1)` (the
note's "inversion and cycling"), the two bond terms of corner j on the
bond uv are `b Re(g_j(u) [U + V] g_j(v)^(-1))` with:

| corner | U | V |
|---|---|---|
| 1 | `g_2(u)^(-1) g_2(v)` | `h_u^(-1) g_4(u)^(-1) g_4(v) h_v` |
| 2 | `g_1(u)^(-1) g_1(v)` | `g_3(u)^(-1) g_3(v)` |
| 3 | `g_2(u)^(-1) g_2(v)` | `g_4(u)^(-1) g_4(v)` |
| 4 | `g_3(u)^(-1) g_3(v)` | `h_u g_1(u)^(-1) g_1(v) h_v^(-1)` |

U and V are unit quaternions. The kappa term depends on t only. So, given
t and the other three sheets, `g_j` has the density proportional to
`exp(sum_uv c_uv Re(g_j(u) T_uv g_j(v)^(-1)))` with `c_uv = b|U+V|` in
`[0, 2b]` and T_uv a unit quaternion. There is no on-site field. The
reduction of two transverse edges to one right-twisted bond of strength
at most 2b is right.

**The source.** I read the LaTeX source at the cited commit `4eaee875`,
already on this laptop at `/tmp/opus-face2d-openai.NylL2Z/src/`
(no new download). Its `paper.pdf` there has the SHA-256 that row 1084
records (`e87f407d...`). `main.tex` inputs `preliminary.tex` third, so it
is Section 3. Counting its numbered displays gives `eq:pre:10-3` as
(3.61), `eq:pre:10-4` as (3.62), and `eq:pre:1-4` as (3.7). I did not
check the PDF page numbers (pp. 13, 27-29): this laptop has no PDF text
tool. What the source says, at `preliminary.tex` lines:

- L76-80 (Section 3.1): for an oriented edge `e = x -> y`,
  `t_e + s_e = q_y U_e q_x^(-1)` with "any fixed unit quaternion" U_e;
  signed coefficients `|b_e| <= b <= B`; boundary spins fixed; density
  `exp(sum w_e t_e)`.
- L57-59: constants are independent of lattice size, couplings and pins.
- L884: pins lie outside the collar of the coarse cells.
- L1002-1005: (3.61), `|E O| <= C ||O||_inf |A| e^(-c d_pin/s)`, for a
  bounded observable on A "whose average under a common left rotation is
  identically zero".
- L1007-1016: the source's own two-point deduction (3.62) conditions on
  the boundary of a coarse region within a third of the distance,
  applies (3.61) inside, and multiplies by the far observable; free
  subgraphs by zero padding; periodic sides at least C s; "Right twists
  and signed couplings are still allowed in this step".
- L1020: Section 3.11 uses "the untwisted zero-field ferromagnet" and
  says "This restriction is essential."

**Inside the stated class.** The conditional bond is `t_e` for the edge
`e = v -> u` with `U_e = T_uv` and `b_e = c_uv` in `[0, 2b]`: an exact
match, with B at least max(2b, the source's threshold). The conditioning
in (O5) fixes `g_j` outside a coarse-cell region with collar, so the pins
are outside the collar. F, as a function of `g_j` on its support, has
identically zero common-left average (corner j acts on the lift as left
multiplication of `g_j`; I checked this for j = 1 and j = 3). H is fixed
by the conditioning. This is the source's (3.62) deduction with a
multi-site F and a bounded H, so (O5) follows. `E[F | t] = 0` follows
from the invariance of `e^(S_b)` under left multiplication of a whole
`g_j` sheet. The constants do not depend on t or kappa. The rate is
`c/s(2b)` with the scale of coupling bound 2b, and L_0 must be at least
C s(2b); the note states both.

Verdict: **HOLDS, given (3.61).** (3.61) is posted and unrefereed, and I
did not check its proof. The port uses it inside its stated class:
fixed right twists, couplings in [0, 2b], pins outside a collar, and
charged observables only.

## Item 3. (O6)-(O7) and the statement NR: HOLDS

Read line by line: note L246-311.

- In (O1) only `q_4(u) = g_1(u) e^(-i theta_u) g_4(u)^(-1)` depends on
  `theta_u`. The path `e^(-i theta)` has unit speed, so each bond at u
  adds at most b to `|Y_u|`: `|Y_u| <= b deg(u)`. Correct.
- (O6) is the standard first and second log-derivative of a finite
  integral with a smooth integrand on a compact set. Correct. For
  nonadjacent u, v no bond contains both angles, so `d_v Y_u = 0`.
- Invariance. `S_b` is invariant under left multiplication of a whole
  `g_j` sheet for every theta, so its theta-derivative `Y_u` is too.
  So `Y_u - E Y_u` has corner average equal to itself, and the hypothesis
  of (O5) fails unless `Y_u` is constant. Correct.
- Explicit form (my addition; it confirms the point). With
  `n_u = g_1(u) i g_1(u)^(-1)`, the unit imaginary direction of `H_u`
  for `0 < theta_u < pi`, one has `d_theta q_4(u) = -n_u q_4(u)`, so
  `Y_u = -b sum_(v~u) Re(n_u q_4(u) q_4(v)^(-1))`.
  This is a function of q alone and is invariant under all four corner
  actions (corner 1 conjugates both factors; corner 4 cancels in
  `q_4(u) q_4(v)^(-1)`; corners 2 and 3 do not move `q_4` or `H`).
  So the effective trace couplings are covariances of a neutral bond
  observable of the conditional four-sheet law: the (SING) object of
  row 1076.
- (O7): `x_u = t_u` is t-measurable, so the conditional covariance is
  zero and the law of total covariance gives
  `Cov_mu(x_u, x_v) = Cov_nu(t_u, t_v)`. Correct.
- NR: the mixed derivative at z = 0 is `Cov_nu(t_u, t_v)` (the variance
  at u = v). An l1 shell of radius r >= 1 has at most 4r sites, also with
  the periodic distance. So pointwise decay at rate a' gives NR for every
  a < a', and NR gives pointwise decay at rate a. Correct.

By (O7), NR at kappa = b is the minimal target of row 1110 itself, up to
the exponent. The note says this (L302-303). It is not a reduction.

Route 1 fails as written: its output (the effective law of x) needs the
locality of `log W_b`, and (O6) shows that its couplings are neutral
covariances that the charged estimate (O5) does not reach. No short
argument from (O5) closes this, because the obstruction is the symmetry
class of `Y_u`, not a constant.

Verdict: **HOLDS.**

## Item 4. (K1)-(K4), the constrained end: HOLDS (fixed finite volume)

Read line by line: note L318-377.

- (K1): `H = q_1 q_2 q_3^(-1) q_4^(-1) = D q_4^(-1)`, so `q_4 = H^(-1) D`.
  At fixed A, B, C the map `q_4 -> D q_4^(-1)` is an inversion followed
  by a left multiplication, so it preserves Haar measure. Correct.
- (K2)-(K3): `Re(q_4(u) q_4(v)^(-1)) = Re(H_u^(-1) D_u D_v^(-1) H_v)
  = Re(h_u^(-1) K_uv h_v)` with h = H, and the on-site term is
  `kappa Re h_u`. Integrating h gives `z_kappa^|V| Psi_kappa(D)`. Correct.
  `K_vu = K_uv^(-1)`, so `c_uv` does not depend on the orientation.
- `z_kappa = 2 I_1(kappa)/kappa`: from the Poisson integral
  `I_1(z) = (z/pi) int_0^pi e^(z cos theta) sin^2(theta) dtheta` and the
  polar Haar density `(2/pi) sin^2(theta)`. Correct.
- Concentration: `lambda_kappa(Re h <= 1 - eps)` is at most
  `e^(kappa(1-eps)) / (e^(kappa(1-eps/2)) Haar(Re h > 1 - eps/2))`.
  Correct. The bond factor is continuous on a compact set, hence
  uniformly continuous, and equals `e^(b E(D))` at h = 1. So
  `Psi_kappa -> e^(b E(D))` uniformly in D at fixed V. Since
  `e^(b E(D)) >= e^(-b |bonds|) > 0`, the normalized laws converge in
  total variation to (K4).
- (K4): at the limit H = 1, that is `q_1 q_2 = q_4 q_3`. The set
  `{H = 1}` is the corner orbit of (1, 1, 1, 1); its stabilizer is the
  diagonal SU(2) (all `g_j` equal). So it is `SU(2)^4/SU(2)_diag`, of
  dimension 12 - 3 = 9, with global coordinates A, B, C. Correct.
- `x_u = 1` at the endpoint, so the covariance vanishes there for a
  kinematic reason only. Correct, and the note draws no rate from it.

Verdict: **HOLDS** at fixed finite volume, as the note marks it. This end
is outside the window (kappa tends to infinity), as the note says.

## Item 5. (K5)-(K8), the first correction: HOLDS (fixed finite volume)

Read line by line: note L379-452.

- (K5)-(K6). `h = exp(v)` with `|v|` the round distance is the Riemannian
  exponential map of the unit S^3 at 1 (`cos s + n sin s` has unit speed).
  So the Hessian trace in v at 0 is the Laplacian at 1, and coordinate
  functions satisfy `Delta h_alpha = -3 h_alpha`. The weight is
  `e^(kappa(cos r - 1)) (sin r / r)^2`. The note's comparison with
  `e^(-kappa r^2/2)` (after `|kappa O(r^4)| <= kappa r^2/4` on a small
  ball) gives the error `C (r^2 + kappa r^4) e^(-kappa r^2/4)`. In
  `z = sqrt(kappa) v` this is a relative error O(1/kappa) for the
  normalization and O(1/kappa^2) for the second moments, so
  `E v_a v_b = delta_ab/kappa + O(kappa^-2)` and `E|v|^4 = O(kappa^-2)`.
  Odd moments vanish (radial law); cross-site moments factor. The
  fourth-order remainder is at most `C ||D^4 f|| |V|^3 sum_u E|v_u|^4`.
  The complement of the small balls is `O(e^(-c kappa))`. So (K5) holds
  with coefficient `1/(2 kappa)`, with a constant that depends on f and V.
  Correct.
- (K7). `Delta_u e^Phi = e^Phi (Delta_u Phi + |grad_u Phi|^2)`. An
  incoming bond at u, with the other h at 1, is
  `Re(K_vu h_u) = Re(h_u^(-1) K_vu^(-1)) = Re(h_u^(-1) K_uv)`, so every
  bond at u has the outgoing form. `Re(h^(-1) K) = h . K` is a linear
  function restricted to S^3: its Laplacian at 1 is `-3 Re K`, and its
  derivative along `e^(t e_a)` is `(Im K)_a`. Hence
  `Delta_u Phi(1) = -3b sum_v c_uv` and `grad_u Phi(1) = b J_u(D)`, which
  is (K7). Correct.
- (K8). `Psi_kappa = e^(bE) [1 + (2 kappa)^(-1) sum_u Q_u + O(kappa^-2)]`.
  `sum_u sum_(v~u) c_uv = 2 E(D)`, so
  `(2 kappa)^(-1) sum_u Q_u = -(3b/kappa) E + (b^2/(2 kappa)) sum_u |J_u|^2`.
  The error is uniform in (A, B, C) at fixed V: D ranges over a compact
  set and `e^(bE) >= e^(-b |bonds|)`. Correct.

Verdict: **HOLDS** at fixed finite volume. The error constant depends on
V; the note says so and exchanges no limit.

## Item 6. (K9), the limit: HOLDS (fixed finite volume)

Read line by line: note L454-513.

- With a separate `kappa_u` at each site, `Z = prod_u z_(kappa_u) Z~(t)`,
  `t_u = 1/kappa_u`. The product has zero mixed derivative, so
  `Cov(x_u, x_v) = d_(kappa_u) d_(kappa_v) log Z~` for u != v. Since
  `d_(kappa_u) = -t_u^2 d_(t_u)`, this is `t_u^2 t_v^2 d_(t_u) d_(t_v) log Z~`.
  Correct.
- Smoothness in t up to t = 0. The note's sketch (L470-486: cutoff at
  `|z| <= t^(-1/12)`, parity, Taylor remainders) is compressed but its
  conclusion is right. A shorter complete proof, which I checked: put
  `w = 2 sin(r/2) n` for `h = cos r + n sin r` (so `|w| = |1 - h|`).
  This maps `r < pi` onto `|w| < 2`, is smooth, equals v up to cubic
  terms, and makes the weight exact: `e^(kappa(cos r - 1)) = e^(-kappa|w|^2/2)`.
  Haar measure becomes a constant times `cos(r/2) d^3w`, an even bounded
  density J with `J(0) > 0`. With a smooth cutoff near 0, the normalized
  one-site average is a ratio of two heat-semigroup values
  `(e^(t Delta/2) g)(0)` for compactly supported smooth g, plus tails
  `O(t^(-3/2) e^(-c/t))` that are flat at t = 0 with all derivatives. So
  it is C-infinity on `[0, t_0]`, and the product over sites is
  C-infinity on the closed orthant. Its first coefficient is
  `(1/2) Delta f(1)`, because `grad J(0) = 0` and `w = v + O(|v|^3)`.
  This confirms (K5) as well.
- For nonadjacent u, v no bond contains `h_u` and `h_v`, so
  `Delta_u Delta_v e^Phi |_(h=1) = Q_u Q_v e^(b E(D))`. The coefficients of
  `Z~` are `Z_inf`, `Z_inf E_inf[Q_u]/2` and `Z_inf E_inf[Q_u Q_v]/4`;
  the logarithm gives `Cov_inf(Q_u, Q_v)/4` for `t_u t_v`. The C^3 bound
  gives `d_(t_u) d_(t_v) log Z~ = Cov_inf(Q_u, Q_v)/4 + O(1/kappa)` at
  `t = 1/kappa`, hence (K9) with the stated `O(kappa^-5)` remainder.
  Correct.
- `Q_u` is a corner singlet: the corner action sends `D_u` to
  `g_1 D_u g_4^(-1)`, so `K_uv` is conjugated by `g_1`; Re K and |J_u|
  are invariant. Correct.

Verdict: **HOLDS** at fixed finite volume. (K9) does not claim that
`Cov_inf(Q_u, Q_v)` is nonzero, and it needs no such claim.

## Item 7. (B1)-(B4), the block sum: HOLDS (as a conditional criterion)

Read line by line: note L544-618, against FST-BD and M1 of row 1091.

- (B1): `Re(q_1 q_2 q_3^(-1) q_4^(-1)) = Re(D q_4^(-1)) = D . q_4` with
  `D = A B C^(-1)`. So, given A, B, C, sheet 4 is an O(4) sheet with the
  field `kappa D_u`, of norm exactly kappa. The same holds for each sheet
  (for `q_1` the direction is `q_4 q_3 q_2^(-1)`). A change of one other
  quaternion at u moves the direction isometrically, so the field moves
  with Lipschitz constant kappa. Three other sheets, not six. Correct.
- Influence of another sheet. Along a unit-speed geodesic in `q_j(v)`,
  `|d mathcal H_v/ds| = kappa`, and `dE_s F/ds = Cov_s(F, (d mathcal H_v/ds) . q(v))`.
  Integrating (B2) gives `k = kappa R(v, w)`. This needs (B2) for every
  field on the path, that is for all fields of norm kappa and all pins,
  which is how the note states the hypothesis. No zero field enters.
  Correct.
- (B3) counting. Blocks are the translates of one l-by-l square in each
  sheet, so `n_x = l^2`. The law of a block depends on the outside only
  through the same-sheet outer neighbours y and the three other sheets
  at the sites of the block. For a target at position w of the reference
  square there is exactly one translate per w. The pin terms carry
  `e^(a|w-y|)`, the other-sheet terms `e^(a(|v-w|+1))` and the factor 3.
  Dividing by `n = l^2` gives `Gamma_l(a)`, and `Gamma_l(a) < 1` is
  (D_a) of FST-BD with `gamma = Gamma_l(a)`. Correct.
- (B4): with `R(v, w) <= X e^(-2a|v-w|)`, the bulk term is at most
  `3 kappa e^a X l^(-2) sum_(w in square) sum_v e^(-a|v-w|) <= 3 kappa e^a X S_a`,
  and `S_a = ((1 + e^-a)/(1 - e^-a))^2`. Correct. A decaying pin
  response gives a boundary term of order l, so `l^(-2)` beats it; the
  field term is an area sum and gets no factor that tends to zero.

Verdict: **HOLDS.** (B1)-(B4) are a correct application of FST-BD. (B2)
and the pin response p are hypotheses that no cited input supplies, as
the note says.

## Item 8. The claim X >= 1/4 in 4.2: HOLDS

Read line by line: note L620-635, against FST-F of row 1091 (L151-195).

- FST-F(h_0, a, X) quantifies over all fields with `sup |H_u| <= h_0`,
  and its proof of (C) uses the convex combinations `H + s delta`, whose
  norm can drop below kappa. Adapted to P4 (field norm kappa, three
  other sheets, Lipschitz constant kappa), it needs `h_0 >= kappa` and
  `3 kappa X e^a S_a < 1`. The note's reading is right.
- Zero field is in that class. On an unpinned torus the zero-field law is
  invariant under a global left rotation, so each one-site marginal is
  Haar. For `F = G = q_alpha(u)`: mean 0, and the four equal second
  moments add to one, so the variance is 1/4. Round distance dominates
  chordal distance, so `Lip_u = 1` (equality along a great circle through
  `q_alpha = 0`). FST-F's right side is then `X . 1 . 1 . e^0 = X`. So
  `X >= 1/4`, and with `e^a S_a >= 1` the condition needs
  `3 kappa/4 < 1`, false for kappa >= 2.3 (3(2.3)/4 = 1.725). Correct.
- The note limits the conclusion to that explicit sufficient bound. That
  limit is right. Consistency check (mine): if FST-F is restricted to
  fields of norm exactly kappa (the sphere path of 4.1), the one-site
  law with no bonds is the von Mises-Fisher law on S^3, whose transverse
  coordinate has variance `m(kappa)/kappa` (from
  `E[(q . D)^2] = 1 - 3 m(kappa)/kappa`). Then `3 kappa X >= 3 m(kappa) > 1`,
  the same number as SSB (item 9). So the restriction to the sphere does
  not escape on bond-free graphs; on tori with bonds it is open.

Verdict: **HOLDS.**

## Item 9. SSB with the hand inequality (B7): HOLDS

Read line by line: note L637-700, against FST-BD (C) and (D_a).

- Setting. On a bond-free graph the sites are independent one-site P4
  laws. FST-BD defines `mu_V^eta` for every eta by the density, so a
  single configuration is a legitimate test. Given the other three
  quaternions at u, `q_4(u)` has the density proportional to
  `e^(kappa D . q_4)`: the von Mises-Fisher law on S^3, with mean
  `m(kappa) D`, `m = I_2/I_1`. Correct (the mean resultant length on
  `S^(p-1)` is `I_(p/2)/I_(p/2-1)`, here p = 4).
- Influence. Take the other three at 1 and `F` the i-coordinate of
  `q_4(u)` (`Lip_u F = 1`, no other dependence). Rotating `q_1(u)` or
  `q_2(u)` to `e^(ti)` gives `D = e^(ti)`; rotating `q_3(u)` gives
  `D = e^(-ti)`. So `E F` moves by `+- m sin t`, with input distance |t|.
  For every one-sheet block V that contains (u, 4), these three
  variables are outside V, and (C) forces `k^V_(x->u) >= m(kappa)` for
  each. Coefficients are nonnegative, so (D_0) gives
  `3 m(kappa) n_u <= gamma n_u`: (B6). Correct.
- (B7). The recurrence `I_1 - I_3 = (4/kappa) I_2` gives
  `m = kappa/(4 + kappa I_3/I_2)`. The lower bound needs
  `I_3/I_2 <= kappa/6`. I checked it by hand from the series:
  `kappa I_2 = sum_k 2 (kappa/2)^(2k+3) / (k! (k+2)!)` and
  `6 I_3 = sum_k 6 (kappa/2)^(2k+3) / (k! (k+3)!)`; the ratio of the
  k-th terms is `3/(k+3) <= 1`. So `m >= 6 kappa/(24 + kappa^2)`. I did
  not identify "GL4"; the series check makes the step independent of it.
  Arithmetic: `18 (23/10) = 1035/25` and `24 + (13/5)^2 = 769/25`, so
  `3m >= 1035/769 > 1` on [2.3, 2.6]. Correct; no special-function value
  is used.
- Scope. A per-sheet rescaling of the round metric does not escape: for
  the sheet with the largest scale factor the three ratios are each at
  least one, so the sum is still at least `3m`. (My extension; other
  metrics are not covered.) SSB is a counterexample to the single-sheet
  FST-BD method over the free-subgraph class, not to P4-MIX, whose
  sites are independent on these graphs. The note says this.

Verdict: **HOLDS.**

## Item 10. The U(1) control (U1): HOLDS (guide grade, as marked)

Read line by line: note L729-780.

- (U1): `b cos(grad phi_i) = b - (b/2)(grad phi_i)^2 + ...` and
  `kappa cos(psi) = kappa - (kappa/2) psi^2 + ...` with
  `psi = phi_1 + phi_2 - phi_3 - phi_4`. The on-site Hessian is
  `kappa v v^T`, `v = (1, 1, -1, -1)`: rank one, so three combinations
  are massless. Gradient energies are invariant under the constant shifts
  by which `U(1)^4` acts: singlets. In two dimensions a massless gradient
  covariance has a `|x|^-2` tail, and Wick's rule gives `|x|^-4` for its
  square. Correct.
- The quadratic form is diagonal in the split `phi = (psi/4) v + chi`,
  `v . chi = 0`, so at this order x = cos(psi) is independent of the
  massless modes; psi has `mass^2 = 4 kappa/b`. So the note's sentence
  "x itself reads the massive combination" is right at the Gaussian level.
- Holonomy branches: a U(1) class is a point, and `cos(theta) = t` has
  the two classes `+-theta`. Correct. The stop of (O5) for U(1) is right:
  the source's (3.7) (`eq:pre:1-4`) has the cross product
  `(eta_y + eta_x) x s_e`, and L68-69 of `preliminary.tex` say the
  noncommuting term "determine[s] the quantitative stiffness gain".
- 5.2 (product with a U(1) face) is immediate and correct.

**Addition (GUIDE; perturbative, not proved).** The Gaussian decoupling of
x does not persist at the next order, so the U(1) test likely binds the
minimal target too.
(a) The quartic term `b (grad phi_i)^4 / 24` contains
`(b/64) (grad psi)^2 sum_i (grad chi_i)^2`, and for a Gaussian psi,
`Cov(cos psi(0), (grad psi(y))^2) = -E[cos psi] (E[psi(0) grad psi(y)])^2`,
which is nonzero for y near 0. At second order this gives the
x-covariance a `|x|^-4` tail.
(b) The note's own (K9) works verbatim for U(1) (circle Laplacian). In the
U(1) constraint law, write `a_1, a_2, a_3` for the phases of A, B, C.
Then `d = a_1 + a_2 - a_3` is a massless Gaussian at large b with
covariance `(3/(4b)) (-Delta)^(-1)` (the stiffness matrix is `I + w w^T`,
`w = (1, 1, -1)`, and `w^T (I + w w^T)^(-1) w = 3/4`). `J_u` is about `-(Delta d)(u)`, which
has only short-range correlations, but `Q_u` contains the gradient energy
`(b/2) sum_v (grad_uv d)^2`. So `Cov_inf(Q_u, Q_v)` has a `|u - v|^-4` tail.
If this holds, any proof of NR must use a step that fails for U(1). The
note's three routes all stop for U(1), so no verdict changes. But L760-762
should not be read as saying that the minimal target is U(1)-blind.

Verdict: **HOLDS** as guide. The addition above is guide grade only.

## Item 11. The stop by the third rule, and the nature of the failures

Rule (row 1110 brief): "one named step that failed in three written
ways, the three ports of row 1084 not counted".

**Validity: VALID as written, with one caveat.** The note names NR and
writes three attempts at it, each with a first failing point: (O6)
(route 1), (K9) plus the continuation (route 2), (B3)-(B7) (route 3).
The mechanisms are distinct (orbit elimination, large-kappa expansion,
block contraction). They are the three routes of the brief's order of
work. None is P4-NA, P4-SIGN or P4-LIFT, and the note does not count
those (L310-311, L803-804). Caveat: by (O7) NR is the minimal target
itself (the note says so, L302). So the stop localizes nothing below
"the neutral sector". The three routes stop at three different
sub-statements, and all three are neutral estimates for an interacting
multi-sheet law: the (SING) item of row 1076. The rule does not forbid a
named step that equals the target, so I count the stop as valid.

**Failures of the methods, not short gaps.**

- Route 1. The obstruction is a symmetry class: the effective couplings
  are covariances of `Y_u`, which is invariant under every corner
  (item 3). (O5) is a theorem about observables with zero corner average
  only. A repair needs neutral decay of the conditional four-sheet law,
  which is (SING) itself. Not a short gap.
- Route 2. The expansion is fixed-volume, and its first correction has
  relative size `3/kappa > 1` on the window. So the method has no small
  parameter at kappa = b. A repair needs a volume-uniform neutral bound
  for (K4) and a uniform continuation from kappa = infinity to kappa = b;
  row 1077's example (16) blocks the shortcut "the endpoint has a gap".
  Item 10(b) adds (guide) that the U(1) analogue of (K4) is massless, so
  the first of these must read the group. Not a short gap.
- Route 3. SSB is a proved counterexample to the single-sheet method over
  the free-subgraph class (item 9). On tori the note shows only that (B2)
  is not supplied and that the FST-F constants fail. A further check
  (GUIDE; an exact identity with unproved size inputs) says the torus
  case is not a short gap either. Fix a one-sheet block V in sheet 4, put
  the other three sheets at 1 everywhere and the pins at 1, and rotate
  every spin of V in the (1, i)-plane. Haar integration by parts gives
  `E q_0(u) = kappa sum_(v in V) C_v + b sum_(boundary bonds (v,y)) C_v`,
  `C_v = Cov(q_1(u), q_1(v))`. Each of the three other sheets at v adds
  at least `kappa |C_v|` to the influence sum at u, and each pin y adds
  at least `b |sum_(v~y) C_v|`. So
  `sum_(x not in V) k^V_(x->u) >= 3 m_u - 2 P_u`, with `m_u = E q_0(u)` in
  this aligned block and `P_u` the pin term. In a large block `P_u` should
  be small away from the boundary. Then (D_a) needs `m_u` below about
  1/3, but the bond-free value is `m(kappa) >= 0.47` on the window, and
  aligned bonds should raise it (no O(4) correlation inequality is
  claimed). One-site blocks fail by an exact count: where the total
  field on `q_4(u)` cancels (possible, since `kappa/b = 1 <= 4`), the
  conditional law is Haar with second moments I/4, so the four pins give
  at least `b` and the three other sheets at least `3 kappa/4`, and
  `b + 3 kappa/4 > 1`. I did not check blocks of intermediate size. So
  the single-sheet method very likely fails in the bulk of large tori
  too. The repair is a different block family, which is the note's next
  decision.

The next decision in note 5.4 (a neutral bound for joint four-sheet
blocks, or (K4) plus a controlled continuation) agrees with this. If
item 10's guide is right, either option must contain a step that reads
SU(2): a finite-block criterion checked by a group-blind estimate would
also give exponential x-decay for the U(1) analogue.

Not checked here: 5.3 (Ising example (16) and the port compatibility),
the repository and literature search of step 1, and the full proof of
OpenAI (3.61).

## Item 12. Summary and RESULT

| Item | Verdict |
|---|---|
| (O1)-(O3), (O2) | HOLDS |
| (O4)-(O5) | HOLDS, given OpenAI (3.61); used inside its stated class |
| (O6)-(O7), NR | HOLDS; NR is the minimal target itself |
| (K1)-(K4) | HOLDS at fixed finite volume |
| (K5)-(K8) | HOLDS at fixed finite volume |
| (K9) | HOLDS at fixed finite volume |
| (B1)-(B4) | HOLDS as a conditional criterion |
| X >= 1/4 (4.2) | HOLDS |
| SSB, (B7) | HOLDS |
| (U1) | HOLDS as guide; guide addition: beyond Gaussian order the U(1) x-covariance likely has a `|x|^-4` tail |
| Stop by the third rule | VALID as written; the named step equals the minimal target |
| Nature of the failures | failures of the methods as written; none is a short gap |

No line of row 1110 needs a correction. Checked by hand by Claude Opus 5.5
(max effort); no run, no numerical step and no Lean check was used. This
is a check of research text; it grants no status. No mass gap is claimed.

RESULT: row 1110 checked line by line by Claude Opus 5.5 max (cross-provider; writer gpt-6-astra max): (O1)-(O3), (O6)-(O7)/NR, (K1)-(K9), (B1)-(B4), X >= 1/4 and SSB with (B7) HOLD, (O4)-(O5) HOLDS given OpenAI (3.61) used inside its stated class (LaTeX source read at 4eaee875; PDF page numbers not checked), (U1) HOLDS as guide with a guide-grade addition that the U(1) x-covariance likely has an |x|^-4 tail beyond Gaussian order; no correction needed; the stop at NR by the third rule is valid as written, though NR is the minimal target itself, and the three failures are failures of the methods (symmetry class, no small parameter, SSB plus a Ward-identity guide for tori), not short gaps; no mass gap claimed.
