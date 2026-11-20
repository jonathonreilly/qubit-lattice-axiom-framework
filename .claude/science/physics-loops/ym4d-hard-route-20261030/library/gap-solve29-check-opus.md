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
