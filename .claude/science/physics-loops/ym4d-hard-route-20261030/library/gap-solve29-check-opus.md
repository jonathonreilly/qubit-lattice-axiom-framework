lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:11Z

# Check of row 1254 (`library/gap-solve29-astra62.md`)

Queue row 1261, `gap-solve29-check-opus`. Cross-provider check: the author
of row 1254 is gpt-6.2-astra max (Mac mini Codex runner); this checker is
Claude Opus 5.5 max on the Mac mini Claude worker 3. Started 2026-11-20T11:11Z
(date -u). Source file read at commit f2d7eba78.

Verdict labels: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of
the checked file. Every step below is checked by hand. No numeric run is a
proof step here.

## Plan (at most eight steps)

1. Read the checked file in full; inventory its labelled statements with line
   numbers; read FINISH.md rules and the earlier rows it cites.
2. Check the same-torus Wilson cube comparison (37) line by line.
3. Check the local-source criterion (32)-(33) line by line.
4. Check the remaining PROVED statements, in order.
5. Check the ARGUED, GUIDE and OPEN statements and the RESULT line.
6. Restatement question: is (37) a restatement of an earlier row? Grep
   `library/open-core.md`, the FINISH rows and the earlier `gap-solve*` files.
7. Read each cited earlier statement and its proof where a step depends on it.
8. Verdict table and RESULT line.

## Progress

(Steps are appended below as they finish.)

### Step 1. Inventory (done 2026-11-20T11:40Z)

Read in full: the checked file (504 lines, 76,630 bytes, commit 916a430c6,
unchanged at f2d7eba78); `FINISH.md` lines 1-84 and 320-351; row 1254 and
row 1261. Every statement of the checked file carries a label. Line numbers
below are those of the checked file at f2d7eba78.

| Line(s) | Label | Statement |
|---|---|---|
| 3, 5, 7 | GUIDE | repo search |
| 11 | PROVED | summary of (37) |
| 13 | OPEN | summary |
| 21-33 | PROVED cond. | (1)-(3): uniform cube constant v gives H >= 16v/(625e^2 l) |
| 35-40 | PROVED | (4) reflection interpolation |
| 42-48 | PROVED, cites B | endpoint decay from B's covariance theorem |
| 50, 52 | PROVED | spectral conclusion of (3); example diagonal |
| 58-72 | PROVED, cites B | (5)-(6) marginal comparison |
| 74-89 | PROVED | (7) elimination of private variables |
| 91-95 | PROVED | (8) gauge averaging |
| 97-111 | PROVED | (9)-(10) two directions |
| 113-118 | PROVED | theta -> 1 on the window |
| 122-149 | PROVED, cites row 1145 | (11)-(13) pinned path relaxation |
| 153-183 | PROVED | (14)-(15) reduced width; example |
| 185-196 | PROVED | necessary width O(beta) in (11) |
| 202-218 | PROVED | (16) adjoint coercivity on a fibre; example |
| 220 | PROVED | failure of pointwise convexity |
| 226-251 | PROVED | (17)-(19) upward comparison |
| 253 | PROVED | physical scale: v_t >= 1/2 at t >= 4096u |
| 255-259 | PROVED cond. | (20) microscopic sufficient condition |
| 261-266 | PROVED | (21) form version |
| 272-299 | PROVED | (22)-(24) gradient Poincare to cube constant |
| 303-308 | PROVED, cites row 1231 | (25) |
| 310-315 | PROVED cond. | (26) necessary bounds |
| 317 | PROVED | Haar comparison is too weak |
| 319-330 | PROVED | (27) negative Gamma_2 at one field |
| 337-342 | PROVED | (28) layered operator K, finite propagation |
| 344-355 | PROVED | (29) Chebyshev filter |
| 357-368 | PROVED cond. | (30) local sufficient condition; example |
| 371-375 | PROVED, cites row 1231 | (31) |
| 377 | PROVED | primitives (I-K)g give zero vectors |
| 380-397 | PROVED | (32) Poisson-clock filter for H_s |
| 399-403 | PROVED cond. | (33) local-source criterion |
| 406-414 | PROVED, cites row 1231 | (34) slow weight of the packet |
| 416-422 | PROVED cond. | (20) re-derived through (32) |
| 425-435 | PROVED | (35) removing time-independent modes |
| 437 | OPEN | |
| 440-447 | PROVED, cites row 1231 | slow weight at nonzero temporal momentum |
| 452-463 | PROVED, cites B | (36) and its two consequences |
| 468-473 | PROVED | (37) |
| 476-492 | PROVED | (38) negative Bakry-Emery quotient on the fibre |
| 495-500 | PROVED | (39) one stochastic time suffices |
| 502, 504 | OPEN, RESULT | |

Cited inputs a step depends on: B's finite-volume covariance theorem (TeX
lines 5850-6077), B's path-interior lemma (5); row 1145 (1)-(2); row 1231
(packet covariance limit, its (35)-(36)); row 1222 (reflection interpolation).

### Step 2. The same-torus Wilson cube comparison (37), with (17)-(19), (21) and line 253 (done 2026-11-20T12:05Z)

Notation as in the checked file: V_s(x) is the set of all links whose base
point lies in x+[0,s)^4; P_x^{(s)} is conditional expectation on the links
outside V_s(x); D_x = 1-P_x^{(s)}; H_s = s^{-4} sum_x D_x; v_s is the optimal
constant in v Var(f) <= <f,H_s f> on gauge-invariant f.

**(17), lines 226-251: HOLDS.** Each step redone by hand.

- Line 232, gauge-invariant subspace. The Wilson law and every exterior
  sigma-field are gauge invariant, so each P_x commutes with gauge
  transformations and preserves the invariant subspace. H_s >= v_s on its
  centered part, so g = H_s^{-1} f exists there and <g,H_s g> = <f,H_s^{-1}f>
  <= ||f||^2/v_s.
- Line 234, commutation. If the origins x, y have periodic maximum distance
  >= s+1, then in one coordinate the base points of the two cubes differ by
  at least (s+1)-(s-1) = 2. The links of one plaquette have base points at
  maximum distance <= 1. So no plaquette reads both cubes, the conditional
  law of the two cubes given the joint exterior is a product, and
  P_x P_y = P_y P_x = conditional expectation on the joint exterior. Then
  D_x D_y is a projection and <D_x g, D_y g> = ||D_x D_y g||^2 >= 0.
- Line 240, (18). For p(x-z) != 0 one has V_s(x) inside V_t(z), so the
  exterior of V_t(z) is coarser and P_t(z) D_x = P_t(z) - P_t(z) = 0. Next,
  sum_z p(x-z) = A for every x, so sum_z L_z = A H_s g = A f. Then
  A||f||^2 = sum_z <(1-P_t(z)) f, L_z>, and Cauchy-Schwarz gives (18).
- Line 244, (19). sum_z ||L_z||^2 - B||H_s g||^2
  = s^{-8} sum_{x,y} (B_{xy}-B) Re<D_x g, D_y g>. The far pairs give terms
  <= 0, because B_{xy} <= B and Re<D_x g,D_y g> >= 0. A near pair gives at
  most eps B (||D_x g||^2+||D_y g||^2)/2. Each x has (2s+1)^4 near partners,
  and sum_x ||D_x g||^2 = s^4 <g,H_s g>. This gives (19) exactly as written.
  The identity B - B_{xy} = ||p - tau_{x-y} p||^2/2 holds on the torus
  because the support of p has side k < N/2.
- Line 251, the weight. u(i) = 1 for w-1 <= i <= k-w, so
  sum u^2 >= k-2w+2. The two ramps give sum (u(i+1)-u(i))^2 = 2/w exactly
  (the ramps do not overlap since w <= k/4). Since u <= 1,
  (sum u)^2/sum u^2 >= sum u >= k-2w, so A^2/B >= (k-2w)^4. One unit shift:
  ||p - tau p||^2 = (2/w)(sum u^2)^3 = (2/w) B/sum u^2 <= 4B/(kw). A near
  displacement has l1 length <= 4s, so ||p-tau p||^2 <= 64 s^2 B/(kw) and
  eps = 32 s^2/(kw). Substitution gives (17).

**(21), lines 261-266: HOLDS.** For any f, g:
|A<f,H_s g>|^2 <= t^4 E_t(f) B <g,(H_s^2+e' H_s)g>, e' = eps(2+1/s)^4.
With g = (H_s+e')^{-1} f both sides contain q = <f,H_s(H_s+e')^{-1}f>, and
q^2 <= (t^4B/A^2) E_t(f) q gives (21). No inverse of H_s is used.

**(37), lines 468-473: HOLDS.** Case t < 8s: V_s(z) lies in V_t(z), so
||f-P_t(z)f|| >= ||f-P_s(z)f|| for each z; summing gives
v_t >= (s/t)^4 v_s = (s/t)^6 (t/s)^2 v_s >= 8^{-6}(t/s)^2 v_s, and
8^{-6} = 2^{-18}. Case t >= 8s: k = t-s+1 > 7t/8 >= 14, w = floor(k/4) is
>= 3 and >= k/8 (true for k >= 6), k-2w >= k/2 >= 7t/16, and
(7/16)^4 = 2401/65536 >= 1/64. With kw >= 49t^2/512 and (2+1/s)^4 <= 39.07:
32 (2+1/s)^4 s^2/(k w v_s) <= 655360/(49 X) < 13375/X, X = (t/s)^2 v_s.
So v_t >= (1/64) X/(X+14000) >= min(1,X)/(64*14001), and
64*14001 = 896,064 < 2^20 = 1,048,576. The case v_s = 0 is trivial.
The line-11 summary states the same inequality with the same hypotheses.

What (37) uses: finite-range conditional independence of the Wilson law
(separated cubes commute), nesting of exterior sigma-fields, and the
spectral bound v_s. It uses no estimate on the Wilson coupling. It is a
general fact about heat-bath block dynamics of a finite-range Gibbs measure
on a torus; nothing in it is specific to SU(2). The exponent 2 is the right
one: for a massless Gaussian field in a box of side N the block constants
scale like (s/N)^2, and (37) then gives (t/N)^2 up to the constant. (This is
a plausibility check by the checker, not part of the proof.)

**Line 253 (physical scale): HOLDS.** u = ceil(s/sqrt(min(v_s,1))) >= s;
k >= 4096u - s + 1 > 4095u; w = u; s^2/v_s <= u^2, so the denominator is
<= 1 + 1280/4095 < 4/3; k-2w >= t-3u, so the numerator is
>= (1-3/4096)^4 > 2/3. The upper bound v_t <= 1+2/t: a centered plaquette
trace is moved only by cubes containing one of its three base points, and
the union of three unit translates of a t^4 cube has at most t^4+2t^3
origins. The limit v_t -> 1 as t/u -> infinity follows from (17) with
w = sqrt(tu).

### Step 3. The local-source criterion (32)-(33), with (28)-(30) (done 2026-11-20T12:30Z)

**(28), lines 337-342: HOLDS.** Origins in one layer o+(2sZ)^4 are at
maximum distance >= 2s > s, so their projections commute (Step 2) and P_o is
an orthogonal projection. Translations permute the layers, so K commutes
with them. If F is measurable off every cube that meets the current support
of G, then <F, P_o G> = <P_o F, G> = <F, G>. A cube meeting a support S has
its links and their plaquette neighbours within base-point distance s of S,
so the stated growth s+1 per application is an upper bound. Induction on r
gives <F, K^r G> = <F, G> for r <= h when the separation exceeds h(s+1).

**(29), lines 344-355: HOLDS.** p_h(1) = 1 and the moment identity give
<F,G> = <F,p_h(K)G>. On [0,1-sigma] the argument of T_h lies in [-1,1]; on
(1-sigma,1] the ratio is <= 1 because T_h increases on [1,infinity). With
cosh(tau) = (1+sigma)/(1-sigma) one gets e^tau = (1+sqrt(sigma))/(1-sqrt(sigma))
exactly, and log of that is 2 artanh(sqrt(sigma)) >= 2 sqrt(sigma). So
1/T_h(...) <= 2 e^{-2h sqrt(sigma)}. Splitting G at Pi_sigma gives (29).

**(30), lines 357-366, and line 368: HOLD.** With a_j T_j =
(1+alpha)B_j/kappa' + O(a_j), the largest admissible h satisfies
2h sqrt(sigma_j) >= kappa' a_j T_j - O_F(1) (the rounding costs at most
2 sqrt(sigma_j) < 2). Then (29) gives
|C_j(T_j)| <= e^{-alpha B_j} + 2e^{O(1)} e^{-(1+alpha)B_j} e^{B_j}
= O_F(e^{-alpha B_j}); time translation commutes with Pi_sigma because it
permutes the layers. T_j is even, so C_j(T_j) >= 0, and T_j stays inside a
quarter of the torus because B_j = o(a_j N_j). Then (4) gives
H >= kappa' alpha/(1+alpha). The example at line 368 is direct.

**(32), lines 380-397: HOLDS.** Each step redone:

- Poisson representation: e^{-uH_s} = e^{-uR} sum_n (uR)^n Q^n/n! with
  R = N^4/s^4 and Q the average of the P_x. This is the average over
  rate-s^{-4} clocks of time-ordered products of projections.
- No chain, no change. Induct along a history. A ring whose cube misses the
  current support fixes the function. A ring whose cube meets the support
  but misses S_F keeps <F, .> unchanged, since P_x F = F. So the pairing can
  change only if some infected ring meets S_F. Tracing infection backwards
  gives a time-ordered chain: its first cube meets S_G, and each later cube
  meets the cube-plus-plaquette neighbourhood of its predecessor. That
  allows (2s+1)^4 <= (2s+3)^4 <= 625 s^4 origins per later step.
- Length. A chain of k cubes spans base-point distance < (k+1)s <= 2k(s+1).
  So reaching S_F needs k >= d.
- Count. The expected number of time-ordered ring tuples on a fixed list of
  k origins is (u/s^4)^k/k!, also with repeated origins. The union bound
  over prefixes of length d gives P(chain) <= M_s(S_G)(625u)^d/d!. For
  u <= h <= d/10000 we have (625eu/d)^d <= 0.17^d, and
  sum_{k>=d} 0.17^k <= 2*4^{-d}. Every history is an L^2 contraction, so
  |<F,S_u G> - <F,G>| <= 4 M_s(S_G) 4^{-d} ||F|| ||G|| for 0 <= u <= h.
- Filter. The affine map has absolute coefficient sum 2/(1-sigma)+1 <= 5
  for sigma <= 1/2, i.e. for lambda <= log 2. The recursion gives the bound
  a_{h+1} <= 10 a_h + a_{h-1} <= 11^{h+1}, and T_h((1+sigma)/(1-sigma)) >= 1.
  Since S_1^i = S_i, the filtered pairing differs from <F,G> by at most
  11^h * 4M_s 4^{-d} <= 4M_s 2^{-d}, because h log 11 <= d log 2. Under
  x = e^{-mu}, the band J_lambda = 1_{[0,lambda)}(H_s) maps to (1-sigma,1].
  So the spectral split is the one of (29). When h = 0 the inequality is
  trivial, because the error term exceeds 2||F|| ||G||.

**(33), lines 399-403: HOLDS.** Here sqrt(1-e^{-lambda_j}) =
sqrt(c) a_j(s_j+1)(1-o(1)), so 2h sqrt(sigma_j) >= (sqrt(c)/10000)(1-o(1))
a_j D - O(1). This is >= kappa' a_j T_j - O_F(1) for each kappa' below
sqrt(c)/10000, because a_j T_j -> infinity. At a_j T_j =
(1+alpha)B_j/kappa' one has B_j/(a_j(s_j+1)) = Theta(d) and B_j = o(d)
(since a_j(s_j+1) -> 0). Hypothesis (33) gives log M_s = o(d), so the chain
term has log <= -(log 2)d(1-o(1)), which is much smaller than -alpha B_j. The slow
term is <= ||A_j|| ||J A_j|| <= e^{-alpha B_j}, by translation invariance of
H_s and ||theta conj(A_j)|| = ||A_j||. The rest is (30). The constant
sqrt(c) alpha/(10000(1+alpha)) is correct.

**Relation to earlier rows.** (32) combines two earlier things. The first is
the Poisson-clock chain bound of row 1231 (`gap-solve26-astra62.md`, (36),
lines 377-385; the row cites it). The second is a Chebyshev filter in the
elapsed stochastic time, used in (29). What is new against row 1231 (36):
the band projection J_lambda replaces the global relaxation rate varpi;
the bound is in L^2 with no supremum norm; the sources are arbitrary local
functions. Row 1222 (`gap-solve24-astra62.md`, (8)-(9), line 151) uses a
deterministic sweep with a global contraction q, not a spectral band. So
(32)-(33) are not a restatement of either row. Chebyshev filtering of an
operator with finite propagation is a classical device. The checked file
does not claim it as new, and this check does not either.

### Step 4. The remaining PROVED statements, in file order (done 2026-11-20T13:05Z)

Cited inputs read for this step: row 1145 (`gap-solve2-astra62.md` L18-L36,
(1)-(3)); row 1231 (`gap-solve26-astra62.md` L355-L387, (35)-(36) and the
torus correlation) with its check, row 1235 (`gap-solve26-check-opus.md`
L248-L275, L355-L432); row 1224 (`gap-mini-solve-q-fable.md` L190-L210, the
check of A's Lemma 6.2, Theorem 6.3, Corollary 6.4, Theorem B); row 1218
(`prior/gap-onebound-read-sol.md` L127-L195).

- **(1)-(3), L21-L33, with L35-L50: HOLDS given the cited covariance
  theorem.** (4): the Hankel kernel C_j(r+t) is positive semidefinite on the
  stated range, so c_r = C_j(2r) >= 0 and c_r^2 <= c_{r-1}c_{r+1}. That is
  log-convexity, and (4) follows. The zero case is also right as written:
  adding eps to every entry adds eps times the all-ones matrix, which keeps
  the kernel positive and Hankel. L42-L48: the argument uses only that the
  bound has the form (prefactor polynomial in k, |S_j|, ||F_j||_inf) times
  exp(-v k/(e^2 q_n)), with k >= T_j/n_j - O(1). B's exact prefactor (TeX
  L5850-L6077) was not re-read here; B is not in the papers folder. A's
  Theorem 6.3 has the same structure and the same constant
  16v/(625e^2 l) (Corollary 6.4); it was checked line by line, HOLDS, in
  row 1224; row 1218 L145-L148 records the same constant for B's Theorem 66.
  The arithmetic at L48 and the limit at L50 are right: alpha_j -> 0,
  alpha_j a_j T_j -> t - eps, and the spectral step is the closed range of
  1_{[m_0,infinity)}(H). The qualitative implication does not need B. L416-L422
  re-derive it from (32) with a smaller constant (see below). (3) is a
  joint-diagonal form of B's Theorem 66 and of A's Theorem B (torus limit
  first there). The file says so at L19.
- **L52 (example): HOLDS** (a_j n_j = a_0 n_0; N_j/n_j = L_j/n_0 ~ j^2/n_0;
  the logarithmic prices are O(j)). The claim that these tori lie in B's
  Corollary 166 range is B's statement, as quoted in row 1218 L182-L187.
- **(5)-(6), L58-L72: HOLDS; (5) re-derived independently on the range the
  file uses.** Given W, the interior links share no plaquette with each other
  or with other paths (b >= 4). So they are independent, with densities that
  are translates of p_s, 0 <= s <= 6 beta. Row 1145 (1) proves
  R_k = I_{k+1}/I_k <= u_k = sqrt(x^2+1) - x, x = (k+1/2)/s. Here
  u_1 = s/(sqrt(s^2+9/4)+3/2) <= s/(s+3/2), and for s <= 6 beta this is
  <= 4beta/(1+4beta) =: q. Also u_k <= u_1, so each link multiplies the
  dimension-d coefficient by at most q^{d-1}. Row 1145 (2) then gives
  ||p_e - 1||_inf <= sum_{d>=2} d^2 q^{(d-1)(b-2)} <= 6 q^{b-2} when
  q^{b-2} <= 1/8. On the used range eta < 1 one has q^{b-4} < 1/48, so the
  condition holds and 6q^{b-2} <= eta. This proves (5) without B. The rate q
  matters: row 1145's cruder per-link rate e^{-1/(1+6beta)} would not give
  M eta -> 0 on the window of L113, since 1/(6j+13) < 4/(17j). (6) is Bayes'
  formula for the law of W given C = c.
- **(7), L74-L89: HOLDS.** D contains the fine exterior. f - E[f|D] and h are
  orthogonal, both lie in the kernel of E[.|X], and <f,v> = ||v||^2 for both.
  Hence ||f-E[f|X]||^2 >= ||f-E[f|D]||^2 + ||h||^2. The group counts are
  m^4 (link) and m^3(m-b+3) >= m^3(m-b) (path). The conditional independence
  of W inside B and the outside groups given W outside B follows because
  every needed staple or endpoint link lies within base-point distance r of a
  private link outside V_m(z).
- **(8), L91-L95: HOLDS.** Ran P_x is contained in Ran prod_{interior y} G_y,
  and each nonempty vertex set meets the interior of (s-1)^4 cubes.
- **(9)-(10), L97-L111: HOLD.** Marginal passage (W-exterior inside fine
  exterior); two-sided density transfer with loss l/u >= theta (both forms
  are infima of mean square errors over the same classes); E[.|W] commutes
  with gauge transformations, so g is invariant in (9); (8) then (7) at
  r = b+2 in (10). Constants as displayed.
- **L113-L118 (window): HOLDS.** log(4beta/(1+4beta)) <= -1/(4j+9);
  1/(4j+9) - 4/(17j) = (j-36)/(17j(4j+9)) >= 1/(170j) for j >= 62. So
  log(M eta) <= -2^j/(170j) + O(log j) and |log theta| <= 4M eta eventually.
- **(11)-(13), L122-L149: HOLD given row 1145 (1)-(2).** (12) is row 1145 (2)
  with h = d-1; (h+1)^2 <= 4^h. The coupling: the r-step density and the
  d'-step density lie in [1-delta,1+delta], so the two tail laws overlap in
  mass >= (1-delta)/(1+delta) >= 1 - 4delta/(1-delta). Expected new
  differences <= (r-1) + (4delta/(1-delta))(d'-r). Count of starts: m-1
  erase, 2 endpoint starts, the rest keep distance 1, which gives (13). Then
  2r <= m/4-2 and 8delta/(1-delta) < 8/127 < 1/8. Path coupling, the
  oscillation bound and t-th roots give the one-path gap 1/2. The tensor step
  uses prod_i P_{i,z} <= P_{e,z} (x) 1 and the m^3 transverse starts per line.
- **(14)-(15), L153-L181: HOLD.** The density of the required product given
  the visible increments, and its unconditional density, both read at least
  h-3 invisible increments. Conjugation invariance moves the fixed
  translations out, so both lie in [1-d_h, 1+d_h]. Bayes and Cauchy-Schwarz
  give |E[u|Y,V]| <= e_h (E[|u|^2|Y])^{1/2}; X lies in sigma(Y,V). In (14):
  ||u_z|| <= ||k_z|| + e_h||f||, the sum over z of ||u_z||^2 is
  s^4 E_s(g), Minkowski, then the Euclidean triangle inequality in R^2.
- **L183 (example): HOLDS** (d_{h_j} <= C e^{-cj^2}, 8M d_h N^2 -> 0).
- **L185-L196 (width of order beta is necessary): HOLDS.** I_2/I_1 is the
  fundamental multiplier; normalizer >= cB^{-3/2}, numerator <= C'B^{-5/2};
  the bridge-to-stationary density in [1/2,2]; Var >= cJ beta from
  covariances lambda^k/4 >= 1/8 for k <= c'beta; prediction error
  m sum_{k<m}(1-lambda^k) <= Cm^3/beta; O(J) starts; ratio C(m/beta)^2.
- **(16), L202-L216, and L218: HOLD.** iji^{-1} = -j and iki^{-1} = -k, so the
  coarse 12 and 13 holonomies are -j and -k; their adjoints are half-turns.
  |v-R_j v|^2 + |v-R_k v|^2 = 4(2|v|^2 - v_j^2 - v_k^2) >= 4|v|^2. Each fine
  edge lies in at most four loops. Each cube edge serves at most b^4 targets
  x on coordinate-ordered paths, so the total is 2b^4(4bE) + 8b^5 E =
  16 b^5 E. The optimality example has quotient <= 4bL^4(pi/b)^2/(bL)^4.
- **L220: HOLDS.** At a link at distance >= 3 from the paths, the marginal
  density reads only its six plaquettes; second derivative -6 beta.
- **(22)-(24), L272-L299: HOLD.** (D_e^a)^* = -D_e^a + (D_e^a V); the
  commutator computation gives (24) exactly. J_ef <= beta (two links share at
  most one plaquette; a unit quaternion has |Re| <= 1), and
  sum_{f != e} J_ef <= 18 beta. Near pairs have l1 displacement <= 4, so
  eps = 32/(tw) is a safe upper bound. <g,Lg> <= ||Lg||^2/rho. Density of
  the range: ground-state transform, Peter-Weyl core, bounded potential,
  gauge averaging. The constants at L276 check
  ((1-1/1024)^4/(1+576/2048) > 0.77).
- **(25), L303-L308: HOLDS given row 1231 (35)** (checked HOLDS as claim D in
  row 1235). If v_s(R/s)^2 >= alpha then u = O(R), t = 4096u = O(R) and
  v_t >= 1/2, contrary to v_t R/t -> 0. The second part uses (22) the same
  way.
- **(26), L310-L315: HOLDS** given (3)'s hypotheses. t_j/u -> infinity in
  both cases of the minimum.
- **L317: HOLDS.** The checkerboard plaquette is
  U_{x,mu}(-U_{x,nu})U_{x,mu}^{-1}U_{x,nu}^{-1} = -1.
- **(27), L319-L330: HOLDS.** The gradient lies only on the four edges of p
  (Im U_p = 0 at the field); every affected face is -1 with one common axis;
  sum dX(p')^2 = 16 + 4*5 = 36, so the Hessian is -36 beta <= -16 beta;
  Ric = 2g on the unit sphere S^3. The private-link densities do not read
  these links.
- **(30) example L368, (31) L371-L375, L377: HOLD.** (31) uses row 1231's
  packet (bounded, centered, one time slice) and its torus correlation
  K_mag(u) ~ u^{-8}, checked HOLDS in row 1235. Then
  2h sqrt(sigma) >= 2u sqrt(lambda) - 6. L377: <F,(I-K)g> = 0 exactly, by
  the moment identity at r = 1.
- **(34), L406-L414: HOLDS given row 1231.** M_s <= C(1+b')^3; the bound
  sqrt(1-e^{-lambda}) >= sqrt(lambda/2) holds on lambda <= log 2. With
  u = A eta^{-1/2}(1+log(1/eta)) and c_1 A > 6, both errors are o(eta^4/log^8).
- **L416-L422 (second proof of the (20) implication): HOLDS.** We have
  lambda_j <= (4c/9) a_j^2 (3s_j/2)^2 = c(a_j s_j)^2 <= v_{s_j}, so J kills
  invariant centered sources. Also lambda_j <= (9/16) log 2, and
  M_s(S) <= |S|. Both liminf bounds at L420 check.
- **(35), L425-L435: HOLDS.** Z_j U_j = Z_j; (I-U^m)Z = 0; the closure of the
  range of I - e^{-tau H} is (ker H)^perp. The file states correctly that
  without vacuum uniqueness only the bound above the zero eigenspace follows.
- **L440-L447: HOLDS given row 1231.** 2K(u) - K(eps u) - K((2-eps)u)
  <= 2Cu^{-8} - c eps^{-8} u^{-8} < -2Cu^{-8}; the separation is
  n - m >= eps uR - 1. The phase split with q = sqrt(c') u^{-5}/4 leaves
  mass >= (15/64) c' u^{-8}.
- **(36), L452-L459: HOLDS.** |psi - 1| <= theta^{-1} - 1 for the density
  ratio of C given W; H_s >= I - P_W from the private-link expansion (each
  private link lies in s^4 cubes); split at P_W.
- **L461: HOLDS AFTER CORRECTION (wording).** The example needs the window
  coupling beta_{W,j} <= j+2 of L113 for theta^{-1} - 1 = o(2^{-j}). The
  example does not restate it. With it, (33) applies for every c, so the
  vector is zero.
- **L463: HOLDS.** F is W-measurable, so <F,A> = <F,P_W A>.
- **(38), L476-L492: HOLDS.** The 12 trace is 1-2sin^4 r. The deficit
  2(sin^2 r - sin^2 t phi)^2 has second derivative -8 phi^2 sin^2 r at 0.
  The side faces give 4(1-cos(pi/(R+1))) after division by 2N^2 sum phi^2.
  Lines through D carry no path link. The gradient of cos(2N r + 2t) is
  -2 sin(2Nr) along the line's axis only.
- **(39), L495-L500: HOLDS.** 1_{[0,lambda)}(x) <= e^{t lambda} e^{-tx}
  with t lambda = B_j; e^{-tH} = (e^{-tH/2})^2 gives the two-history formula.

No PROVED statement fails. One wording correction (L461). One credit note:
the chain count in (32) is, through row 1231 (36), the finite-speed Lemma
6.2 of A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and
Singha Roy, "One Bound at One Scale"). Row 1235 asked for this credit at
row 1231 (36). The checked file credits the companion paper's finite-speed
argument at L19 and L224, but not at L393.

### Step 5. GUIDE, OPEN and RESULT statements (done 2026-11-20T13:25Z)

No GUIDE statement is used as a proof step. Spot checks of the GUIDE
references that lie in this checkout:

- L5, row 1246 (27): `gap-solve28-astra62.md` L378-L386 states (27) as OPEN,
  a sufficient uniform bound on the neutral transfer ratio. This matches the
  GUIDE wording. The main-branch file at 8b11ae2bb9 is not in this checkout,
  so L305-L329 of `gap-phys-seed.md` were not read. Not verified.
- L200, row 1141 (4)-(8): `gap-crux2-astra62.md` L76 and L130 are
  probabilistic lower bounds in the ordinary measure, as the GUIDE says.
- L270 and L319, `gap-gamma2-astra.md`: the Bochner identity is in its Section
  1 (L75, L106); Section 5.1 (L469-L480) is the checkerboard example with
  Hessian -beta sum |dX_p|^2. Both match.
- L7 (CA-I L2704-L2712 exclude a mass-gap assertion): consistent with
  `GOAL.md`, which reads CA-I 2706-2710 the same way. The SA files themselves
  were not re-read.
- L3 (PRs 10114, 10133, 10134, 10141) and the B line numbers (L19, L56, L224,
  L335): not in this checkout; not verified. They carry no proof weight.
- L17, L19 credit Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford
  and Singha Roy (A) and the first four authors (B) by name. That is correct.

OPEN statements: **L13, L437 and L502 are honest.** They agree with what the
PROVED steps give. (20) and (23) are sufficient conditions that the file
does not prove. (36) controls the straight-path algebra, which (L461-L463)
yields only zero continuum vectors. (34) and L440-L447 show that the known
Wilson slow modes carry weight in the ultraviolet band. Whether any of them
enter the narrower band of (33) is open.

**RESULT line L504: HOLDS.** (37) and the criterion (32)-(33) are proved, as
checked in Steps 2-3. The weak-coupling estimate for surviving observables,
the continuum construction and the mass gap stay open. The line does not
overstate (33): it is a conditional criterion, and the line calls it one.

No home-directory path appears in the checked file.

### Step 6. Is (37) a restatement of an earlier row? (done 2026-11-20T13:35Z)

**No.** Searches run, with the hits read:

- `library/open-core.md`: no match for cube comparison, same-torus, upward
  or BP(n.
- FINISH rows: the only matches are rows 1218, 1254 and 1261.
- The library `gap-*.md` and `prior/*.md` files, searched for Knabe,
  upward transfer, side ratio, 6520, H_s^{-1}, dual estimate, inverse of the
  smaller, ascent, Corollary 102, cube side, larger cubes. The hits that
  concern cube dynamics are these:
  1. Row 1224 (`gap-mini-solve-q-fable.md` L180-L189) checked A's Lemma G.2
     and Theorem G.4. That is a Knabe-type step: a patch gap on every fibre
     (every exterior) gives BP(2d-1, eps/16). It goes from a conditional
     local gap to a global cube constant. It does not compare two global
     cube constants of one law.
  2. Row 1218 (L182-L195) and row 1220 (`gap-mini-solve-p-fable.md`
     L160-L172, Lemma NULL) concern B's ascent (H2)/(S). That compares the
     fine law with a different, blocked law of straight-path variables.
  3. Row 1231 (35), checked in row 1235, is a necessary bound on v_m for
     m <= C_0 beta^delta. It is not a comparison of sides.
  4. Rows 1238 and 1246 use "cube" for spatial cubes of the transfer matrix.
     They contain no cube-dynamics comparison.
- The case t < 8s of (37) is the trivial nesting bound v_t >= (s/t)^4 v_s.
  The file attributes this bound to B's comparison at TeX L6520-L6574
  (L224, L473). The new part is the case t >= 8s, with exponent +2 in place
  of -4. It comes from the dual estimate (18)-(19) with g = H_s^{-1} f.

Lineage of the method (checker's note, recalled from memory and not
re-verified here, no proof weight): the smoothed patch weight with ramps of
width w, the error eps ~ s^2/(kw), and the use of commuting separated terms
are the device of Knabe-type finite-size criteria as improved by Gosset and
Mozgunov (2016) and by Anshu (2020) for frustration-free Hamiltonians. The
file names Knabe's method and A's Appendix G at L224. As far as the
repository shows, the form of (37) is new here: two global heat-bath block
constants of one finite-range Gibbs law, compared through H_s^{-1}.

Two smaller restatement notes, outside (37):

- (36), first half (||P_W A(C)|| <= (theta^{-1}-1)||A(C)||), is the dual
  form of row 1220's Lemma NULL. Both state the near-independence of
  sigma(W) and sigma(C), and maximal correlation is symmetric. Row 1145 (4)
  and row 1222 (4) use the same Bayes estimate; the file credits row 1222
  and B at L463, not row 1220. The second half (H_s >= I - P_W, which
  controls the band J_lambda) is new.
- The chain count inside (32) is A's finite-speed Lemma 6.2 in continuous
  time (see Step 4). Row 1235 already recorded this for row 1231 (36).

### Step 7. Cited statements a step depends on (done 2026-11-20T13:45Z)

| Cited | Where read | Used by | State |
|---|---|---|---|
| Row 1145 (1)-(2) (Bessel ratio; product density) | `gap-solve2-astra62.md` L18-L30 | (5) re-derivation, (12), (11), (14), L185-L196 | re-derived here: Riccati comparison R_k' = 1-(2k+1)R_k/s-R_k^2 and its root u_k; Fourier bound sum d^2 prod p-hat. HOLDS |
| Row 1231 (35), torus correlation K_mag ~ u^{-8}, packet f_R | `gap-solve26-astra62.md` L357-L387 | (25), (31), (34), L440-L447 | checked HOLDS in row 1235 (`gap-solve26-check-opus.md` L248-L275), claim D and the torus correlation. Read; consistent with the uses here (f_R in [-1,1] centered, one slice, m <= C_0 r) |
| Row 1231 (36), Poisson clocks | same, L375-L385 | (32) | checked HOLDS in row 1235; restates A's Lemma 6.2 (row 1235 defect 1) |
| A's Theorem 6.3, Corollary 6.4, Theorem B | row 1224 `gap-mini-solve-q-fable.md` L203-L210 | (3) (B's analogue cited) | checked HOLDS in row 1224 (same constant 16v/(625e^2 l)) |
| B's covariance theorem, B's path-interior lemma, B's Corollary 166 range | B v7 TeX, not in this checkout | (3) L42-L48; (5); L52 | B not re-read. (5) re-derived here on the used range; (3)'s use needs only the form; L52's range as quoted in row 1218 L182-L187 |
| Bochner identity, checkerboard example | `gap-gamma2-astra.md` L75-L106, L469-L480 | (27) | standard Bakry-Emery identity; HOLDS |
| Row 1222 (4), (8)-(9) | `gap-solve24-astra62.md` L63-L73, L137-L151 | credit only (L56, L335, L463) | not a proof dependency |
| Row 1220 Lemma NULL | `gap-mini-solve-p-fable.md` L160-L172 | not cited; dual of (36) first half | credit note (Step 6) |

### Step 8. Verdicts and report (done 2026-11-20T13:55Z)

Provenance: Claude Opus 5.5, max effort, Mac mini Claude worker 3, commit
f2d7eba78, check of row 1254 (author gpt-6.2-astra max). Cross-provider.
One reading by hand. This is not an audit. No numeric run was made.

**Positive claims first.**

| Statement | Lines | Verdict |
|---|---|---|
| **(37) same-torus Wilson cube comparison** | L468-L473 (summary L11) | **HOLDS** |
| (17)-(19) upward comparison | L226-L251 | HOLDS |
| (21) form version | L261-L266 | HOLDS |
| physical scale, v_t >= 1/2 | L253 | HOLDS |
| **(32) Poisson-clock band filter** | L380-L397 | **HOLDS** |
| **(33) local-source criterion** | L399-L403 | **HOLDS** |
| (28)-(29) layered K, Chebyshev filter | L337-L355 | HOLD |
| (30) and example | L357-L368 | HOLD |

**Everything else.**

| Statement | Lines | Verdict |
|---|---|---|
| (1)-(4), (3) | L21-L50 | HOLDS given B's finite-volume covariance theorem (only its form is used; A's Theorem 6.3 with the same constant is checked in row 1224). The qualitative implication also follows from (32), by L416-L422. |
| example diagonal | L52 | HOLDS |
| (5)-(6) | L58-L72 | HOLDS ((5) re-derived from row 1145 on the range eta < 1) |
| (7), (8), (9)-(10) | L74-L111 | HOLD |
| window, theta -> 1 | L113-L118 | HOLDS |
| (11)-(13) | L122-L149 | HOLD |
| (14)-(15), example | L153-L183 | HOLD |
| width of order beta is necessary | L185-L196 | HOLDS |
| (16), example; L220 | L202-L220 | HOLD |
| (20) | L255-L259 | HOLDS given (3) |
| (22)-(24) | L272-L299 | HOLD |
| (25) | L303-L308 | HOLDS given row 1231 (35) (checked HOLDS, row 1235) |
| (26) | L310-L315 | HOLDS given (3)'s hypotheses |
| Haar comparison | L317 | HOLDS |
| (27) | L319-L330 | HOLDS |
| (31); L377 | L371-L377 | HOLD (31 given row 1231) |
| (34) | L406-L414 | HOLDS given row 1231 |
| (20) through (32) | L416-L422 | HOLDS |
| (35) | L425-L435 | HOLDS |
| nonzero temporal momentum | L440-L447 | HOLDS given row 1231 |
| (36) | L452-L459 | HOLDS |
| what (36) can construct | L461 | **HOLDS AFTER CORRECTION**: add the window coupling beta_{W,j} <= j+2 of L113; without it (5)-(6) do not give theta^{-1}-1 = o(2^{-j}) |
| direct test | L463 | HOLDS (same window as L461) |
| (38) | L476-L492 | HOLDS |
| (39) | L495-L500 | HOLDS |
| GUIDE | L3-L7, L17-L19, L56, L200, L224, L270, L335 | labels honest; not proof steps; spot-checked in Step 5 |
| OPEN | L13, L437, L502 | honest |
| RESULT | L504 | HOLDS |

First failing step: none. FAILS: none.

**Defects, ranked by what each breaks.** None breaks a consumer.

1. L461 (and L463 through it): the example omits beta_{W,j} <= j+2.
   Wording repair as in the table.
2. L393: the chain count is A's finite-speed Lemma 6.2 (Bhattacharjee,
   Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy, "One Bound at One
   Scale") in continuous time. Row 1235 already asked for this credit at row
   1231 (36). Add it at L393.
3. L459: the first half of (36) is the dual of row 1220's Lemma NULL
   (near-independence of sigma(W) and sigma(C)). Add the credit.
4. L42-L48: B's exact prefactor was not re-read, because B is not in the
   checkout or the papers folder. The step is robust to the prefactor,
   and L416-L422 give the implication without B.

**Restatement.** (37) is not a restatement of an earlier row (Step 6). Its
case t < 8s is the trivial nesting bound. The case t >= 8s, exponent +2
against -4, is new in this repository. The method is Knabe/Gosset-Mozgunov
smoothed patches applied through H_s^{-1} (lineage recalled from memory, see
Step 6). (32) combines row 1231 (36), which is A's Lemma 6.2, with a
Chebyshev filter. Its band version is not in earlier rows.

**What the checked results do and do not show.** (37) reduces the Wilson
input to a microscopic cube bound (20), v_{s_j} >= c(a_j s_j)^2, at any
microscopic side. (26) shows that the same scale is necessary up to the
constant for a nontrivial matched theory. So (20) is the sharp form of the
remaining estimate on this route. Nothing in the file proves (20), (23),
(30) or (39) for a family that creates nonzero continuum vectors.
(36) controls only the straight-path algebra, and L461-L463 show that this
algebra gives only zero vectors. (34) and L440-L447 show actual Wilson slow
weight in the ultraviolet band. The checked file says all of this itself.

RESULT: Row 1261 check of row 1254 (Claude Opus 5.5 max, by hand, cross-provider, first failing step none): the same-torus Wilson cube comparison (37) HOLDS, with (17)-(19) and (21); the local-source criterion (32)-(33) HOLDS, with (28)-(30); every other PROVED statement HOLDS, (3) given the form of B's covariance theorem (A's version checked in row 1224) and (25), (31), (34) given row 1231 (checked in row 1235); one HOLDS AFTER CORRECTION (L461, add beta_{W,j} <= j+2); no FAILS; two credit notes (L393 A's Lemma 6.2, L459 row 1220 Lemma NULL); (37) is not a restatement of an earlier row; OPEN: the microscopic Wilson bound (20) (or (23), (30), (39)) on observables that survive the limit, the nontrivial continuum construction, and the Jaffe-Witten mass gap.
