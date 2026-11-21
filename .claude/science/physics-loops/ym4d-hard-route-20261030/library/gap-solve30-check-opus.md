lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T00:06Z

# gap-solve30-check-opus: line-by-line check of row 1262 (`library/gap-solve30-astra62.md`)

Row 1271 of FINISH.md. Checker: Claude Opus 5.5 (max reasoning), Mac mini worker. Cross-provider check of a row
written by another provider (astra62). Started 2026-11-20T12:06Z (date -u). Source pinned at commit 536662306.

## Plan (at most eight steps; one step per response, each appended here)

1. Read row 1262's file in full, its queue row, and the rules (FINISH.md head, GOAL.md); list every statement and
   its line; record which earlier rows it cites.
2. Check the conditional Wilson estimate: (15), (17) (finite-volume bound), (30), (35), by hand, line by line.
3. Check the variance loss (31)-(32) and the slow sheets (20), (25), by hand.
4. Check the remaining statements (everything else), in file order.
5. For each cited earlier row: read the cited statement and its proof where a step depends on it; verdict on the
   dependence.
6. Restatement question: is the main comparison a restatement of an earlier row (grep open-core.md and FINISH rows).
7. Optional guide-only numeric run (only at >= 50 percent memory free, under the numeric lock).
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line), open items, RESULT line.

## Status log

- 2026-11-20T12:06Z: file created; step 1 starting.

## Step 1. Inventory of row 1262 (done 2026-11-20T12:07Z)

Source: `library/gap-solve30-astra62.md`, 454 lines, read in full. Queue row 1262 is FINISH.md line 1343; it was a
plain-brief solve run (gpt-6.2-astra max, 10:50Z-11:59Z). Labels in the file: PROVED, ARGUED, GUIDE, OPEN.

Statements by equation, with the line of the statement and of its proof:

| Item | Statement line | Proof lines | Content |
|---|---|---|---|
| setup | L13 | - | Wilson law on even N^4 torus; D_x = 1 - P_x for side-s cube; H_s = s^-4 sum_x D_x; patch I_z of R^4 origins, t = R+s-1; Q_z, L_z |
| (1)-(2) | L15-29 | L31-51 | local patch variance (1) gives global gap of H_s at least b_R gamma - e_(s,R) |
| (3) | L31-36 | L31 | Cauchy-Schwarz with sine weights p |
| (4) | L38-47 | L38-47 | sum_z norm(W_z f)^2 <= B(norm(H_s f)^2 + e_(s,R) E) |
| kernel, b_R, e bound | L49, L51 | L49, L51 | ker H_s = constants; b_R >= 1/16; e_(s,R) <= 40 pi^2 (s/(R+1))^2 |
| (5) | L61-66 | L68-73 | conditional mean of a box average of q_p <= m_s, every exterior |
| (6)-(8) | L75-81 | L83-95 | energy fraction of bad exteriors on spectral subspace 1_[0,1](H_s) |
| (9) | L97-100 | L101 | gap with (1) known only on good exteriors |
| choice | L103 | L103 | beta -> infinity parameters make rho -> 0 |
| (10) | L107-109 | L111-113 | m_s = min(1, C(1/s + 1/beta)) from row 1155 (9) |
| (11) | L115-118 | L120 | exclusion by local conditional probabilities |
| (12)-(13) | L122-131 | L135-142 | face colour Poincare from row 1141 (3)-(7) |
| (14)-(15) | L148-156 | L158 | collar version of (1)-(2) and (9) |
| face readings | L160 | L160 | Q_z f = 0 for readings on the outer face, b >= 2 |
| collar tests | L162-166 | L162 | mesoscopic four-box tests at cost C(R/s)^3 e^(-c l^4) + Cs/R |
| (16) | L168-174 | L168-174 | sufficient physical-scale condition gamma >= C_* (s/R)^2 |
| (17) | L178-182 | L184-188 | gamma = 2^-8 exp(-440 beta t^3) for every outer exterior, dyadic t |
| oscillation | L190 | L190 | first bisection density ratio >= exp(c beta t^3) |
| (18) | L198-202 | L204 | at R ~ beta^delta, (14) cannot hold with gamma/(s/R)^2 -> infinity |
| collar cost | L206 | L206 | electric action of a w-step interpolation >= beta d_G^2/(2w) |
| (19) | L210-215 | L217 | relative two-face quaternion Poincare |
| (20)-(22) | L223-249 | L229-259 | slow conditional sheet: two-plane pinned sheet of time links, Rayleigh quotient <= C(d/s)^2 d^2 e^(-cd) |
| (23) | L263-270 | L272 | one released neighbouring plane kills the variance of F |
| (24) | L274-281 | L276-300 | fixed thickness w: another reading with quotient (20) |
| (25)-(26) | L304-308 | L310-337 | thickness w ~ sqrt(beta): quotient <= C(1+w/s)(d/s)^2 d^2 e^(-cwd) |
| (27)-(28) | L341-349 | L341-350 | loop deficit by peeling; probability of coherent end holonomies |
| (29) | L352-356 | L357 | energy cost of excluding perimeter banks |
| filling test | L359 | L359 | exterior test of existence of a common filling |
| (30) | L363-375 | L377-394 | patch comparison with a revealed codimension-two tube |
| (31) | L398-400 | L402 | the reading F of (20) in the full periodic Wilson law: Pr(F != +1) <= C d^2 e^(-c beta d) |
| (32) | L404-406 | L408-412 | the reading of (25) in the full law: Pr(F != 0) <= C d^2 e^(-cKd) |
| correlations | L414 | L414 | the readings have vanishing correlation with L^2-bounded families |
| (33) | L418-421 | L423-425 | larger right-side form; (17) holds for it at every pin value |
| (34) | L427-430 | L427 | dense pin grid costs c (s/h)^2 in (4) |
| dense grid | L434 | L436 | coefficient ((s-h+1)/s)^4 >= 1/16 with planes pinned in four directions |
| (35) | L440-444 | L446 | least local constant = sup over g of integrated squared semigroup norm |
| power tail | L448 | L448 | dyadic power tail suffices; 2-dimensional example |
| OPEN | L194, L450, L452 | - | (17) far below (16); no estimate of (35) at order (R/s)^2; continuum |

Earlier rows and sources it cites (each to be read where a step depends on it):

- row 1254 `gap-solve29-astra62.md`: (17), (18)-(19) overlap estimate, (20), (33), (37), (39), (1)-(4). Unchecked at the pin (row 1262 says so, L452).
- row 1155 `gap-solve7-astra62.md`: (9) periodic marked-plaquette moment; (20) angle lemma and gauge-optimized distance; check `gap-solve7-check-opus.md`.
- row 1141 `gap-crux2-astra62.md`: (3)-(7) acceptance probability and Poincare.
- row 1139 `gap-frameless-2d-astra.md`: template with two marked bonds; folded chessboard.
- row 1231 `gap-solve26-astra62.md` (35) packet, check `gap-solve26-check-opus.md`; row 1222 `gap-solve24-astra62.md` (1)-(2) wall factorization; row 1177 `gap-solve17-astra62.md` (22); row 1224 `gap-mini-solve-q-fable.md` 7.6; `gap-skeleton-max.md` B7 (inverse-square threshold proposal).
- Literature named: Knabe; Gosset-Mozgunov; Froehlich-Israel-Lieb-Simon (chessboard); Durhuus-Froehlich (layer representation); Bhattacharjee, Bhattacharya, Lockwood, Romanov (finite-speed bound); Sussman-Alpoge (transfer and insertion method).

Order of the check (row 1271): (15), (30), (35), (17) first; then (31)-(32) with (20), (25); then the rest.

## Step 2. The conditional Wilson estimate: (1)-(9), (14)-(17), (30), (35) (done 2026-11-20T12:13Z)

All checked by hand. Notation as in row 1262 L13: P_x = E[ . | links outside V_s(x)], D_x = 1 - P_x, H_s = s^-4 sum_x D_x,
E = <f, H_s f>, Pi_z = 1 - Q_z = E[ . | V_t(z)^c].

**(1) => (2), L15-L49: HOLDS.**
- Q_z W_z = W_z (L31): p(x-z) > 0 forces x in I_z, so V_s(x) is inside V_t(z); the tower property gives Pi_z P_x = Pi_z,
  so Pi_z D_x = 0. Sum_z W_z = A H_s and sum_z L_z = R^4 H_s: each x is counted with total weight A (resp. R^4); this needs
  R < N only.
- (3): A E = sum_z <f, W_z f> = sum_z <Q_z f, W_z f>; Cauchy-Schwarz and (1) summed over z give (3). Only the sum over z of
  (1) is used, as L29 says.
- (4): sum_z norm(W_z f)^2 = s^-8 sum_(x,y) B_(y-x) <D_x f, D_y f> with B_v = sum_i p(i) p(i+v). So the excess over
  B norm(H_s f)^2 is -s^-8 sum (B - B_(y-x)) Re<D_x f, D_y f>. Far pairs (periodic sup distance > s): the link base points of
  the two cubes differ by at least 2 in some coordinate, a plaquette's base points differ by at most 1, so no plaquette
  reads both cubes; the fillings are conditionally independent given the joint exterior, P_x P_y = P_y P_x, and
  <D_x f, D_y f> = norm(D_x D_y f)^2 >= 0. These terms are <= 0. Close pairs: |Re<.,.>| <= (norm^2 + norm^2)/2 and
  sum_x norm(D_x f)^2 = s^4 E give excess <= s^-4 E sum_(sup-norm v <= s) (B - B_v).
- The constant: u_k = sin(k theta), k = 1..R, zero at k = 0, R+1; u_(i-1) + u_(i+1) = 2 cos(theta) u_i holds at every
  support site including both ends, so norm(tau_1 u - u)^2 = 2(1 - cos theta) norm(u)^2; telescoping gives shift k at most
  k^2 times this; 1D overlaps c_k lie in [0,1]; 1 - prod c <= sum(1 - c). So 1 - B_v/B <= (1 - cos theta) |v|^2.
  Sum over v in [-s,s]^4 of |v|^2 = 4 (2s+1)^3 s(s+1)(2s+1)/3 = 4(2s+1)^4 s(s+1)/3. This gives e_(s,R) exactly as in L23.
- (2): (3)-(4) give norm(H_s f)^2 >= (b_R gamma - e) E with b_R = A^2/(R^4 B), which matches L21. Kernel: H_s f = 0 gives
  D_x f = 0 for all x; mutual absolute continuity with product Haar and composition of the commuting Haar integrations over
  the cubes (which cover all links) give f constant. Gauge covariance: the gauge action preserves each sigma-field
  sigma(V_s(x)^c) and the measure, so it commutes with P_x. The spectral step (no spectrum in (0, lambda)) is correct.
- b_R >= 1/16 and e <= 40 pi^2 (s/(R+1))^2 (L51): the mean of u is >= 1/2 (sum of 2 min(k/n, 1-k/n) is n/2 or
  (n^2-1)/(2n) for n = R+1, so the mean is n/(2(n-1)) or (n+1)/(2n)); u^2 <= u. The constant is
  (4/3)(5/2)^4 (3/2)(1/2) pi^2 = 39.06 pi^2 <= 40 pi^2. The threshold gamma >= 1280 pi^2 (s/(R+1))^2 gives gap >= gamma/32.

**(5), L61-L73: HOLDS.** Conditional law of the cube is proportional to exp(-beta S_y) times Haar (2 q_p = 1 - tr/2). Counts:
4s^4 updated links, each in 6 plaquettes (<= 24 s^4); a crossing plaquette has an updated base point in the inner boundary
layer (s^4 - (s-2)^4 <= 8 s^3 sites), 24 per site, so <= 192 s^3. On the cap (geodesic distance <= delta = beta^-1/2 for
every updated link) an internal plaquette has angle <= 4 delta and 2q_p = 1 - cos <= 8 delta^2; Haar cap mass
>= (8/(3 pi^3)) delta^3 from the density (2/pi) sin^2. Entropy: beta P_y S_y <= -log Z_y. Internal faces of Y_y are summed
in S_y, |J| = (s-1)^4 >= s^4/16. Result 8[192/beta + 384/s + 4(log(1/c) + 1.5 log beta)/beta], of the form (5).

**(6)-(8), L75-L95: HOLDS.**
- Nonnegativity: B_z is measurable outside V_t(z), hence outside every V_s(x) with p(x-z) > 0, so 1_B commutes with D_x and
  <1_B f, D_x f> = integral of 1_B |D_x f|^2.
- (7): with y = z + d - j the right side equals |J|^-1 sum_j sum_z p^+(x-z+j) int q_(z+d,nu) |g|^2, and
  p^+(x-z+j) >= p(x-z) (take j' = j). Sum of p^+ = (sum of 1D u^+)^4 because max over a product set of a product of
  nonnegative factors factorizes; the layer-cake argument gives sum u^+ <= sum u + s - 2 <= (1 + 2s/R) sum u.
- Split g = P_y g + D_y g: int Y |P_y g|^2 = int (P_y Y)|P_y g|^2 <= m_s norm(g)^2, and Y <= 1.
- (8): far pairs give norm(D_y D_x f)^2 = <D_x f, D_y f>; close pairs use norm(D_y D_x f)^2 <= norm(D_x f)^2 plus the
  absolute cross term; total s^8 norm(H_s f)^2 + 2(2s+1)^4 s^4 E.
- Constant: (2 s^4/A)[1 + 2(2+1/s)^4] E with A >= R^4/16 and (2+1/s)^4 <= 39.07 < 40 gives 32 * 81 = 2592 (s/R)^4. The
  first part gives 2(1+2s/R)^4 m_s per plaquette, times k/h after the Markov bound 1_B <= mean/h, summed over lists.

**(9), L97-L101: HOLDS.** Good part (1 - rho) A E on 1_[0,1](H_s); 1_G commutes with Q_z because G_z is exterior-measurable,
so <1_G f, W_z f> = <1_G Q_z f, W_z f>; integrating the conditional (1) over G_z gives
sum_z norm(1_G Q_z f)^2 <= R^4 E / gamma. The spectral argument on the reducing subspace 1_[0,1](H_s) gives the min with 1.

**(14)-(15), L148-L158: HOLDS.** Every outer cube V_s(x), x in I_z^out, lies inside V_(t+2b)(z - b1) (since
R' + s - 1 = t + 2b), so the outer cube updates and Q_z restrict to the conditional law mu_omega by the tower property.
Outer tests are exterior to V_t(z), so (6) and (11) apply unchanged. With sum_z L_z^out = (R')^4 H_s the Cauchy-Schwarz step
gives the coefficient b_R (R/R')^4 (1 - rho_*)^2. Correct as stated.

**Face readings, L160: HOLDS.** A function of links outside V_t(z) has Q_z f = 0 by definition (b >= 2 keeps the artificial
outer face outside V_t(z)).

**(16), L168-L174: HOLDS as a sufficient condition.** With R'/R <= 2 (b = floor(R/2)), b_R >= 1/16, rho_* <= 1/2, the
coefficient of gamma in (15) is >= 1/1024 and e <= 40 pi^2 (s/R)^2, so gamma >= C_*(s/R)^2 with C_* > 1024 * 40 pi^2 gives
v_s >= c (s/R)^2. The loss bookkeeping is right: with h = K/beta and m_s from (10),
rho = (k/K)[2C(beta/s + 1)(1 + o(1)) + 2592 beta (s/R)^4] = O(k/K) when s ~ beta^2 and beta (s/R)^4 -> 0; the (12) loss
tends to 0 with r ~ (D log R)^(1/3) and cD > 3; the collar loss C(R/s)^3 e^(-c l^4) with l = s/4 ~ beta^2/4 and
log R = O(beta) tends to 0. The sentences on row 1254 (17) and its continuum premises (L174) are a citation of an
unchecked row; see Step 5.

**(17), L178-L188: HOLDS.** Checked steps: (i) a cut of a rectangle with longest side l deletes at most 2 l^3 sites x 24
incidences = 48 l^3 plaquettes, each half-trace in [-1, 1], so the normalized density against the product law has
sup/inf <= e^(96 beta l^3); (ii) l <= dmu/dnu <= u compares variances and integrated conditional variances (both are
infima of squared error over constants or G-measurable functions); (iii) Efron-Stein on the two-factor product;
(iv) recursion with the sibling fixed, then integrate; (v) cuts in round j all have longest side t 2^-j, four cuts per
round: 384 beta t^3 (8/7) = 438.9 beta t^3 < 440 beta t^3; (vi) a tile of side s/2 at origin o lies in V_s(x) for
x in o - {0..s/2}^4, and these x lie in I_z^out because b >= s/2; a side-s cube holds at most 2^4 aligned tiles; nested
projections let the cube variance dominate the tile variance after integrating the collar. Constant 2^-4 * 2^-4 = 2^-8.

**Oscillation remark, L190: HOLDS.** The changed link U_2(m, x') turns the crossing 12-plaquette at (m-1, x') from +1 to -1;
its other plaquettes have all base points at x_1 = m and are not crossing; (t-4)^3 >= t^3/8 for t >= 8.

**(30), L363-L392: HOLDS.** Checked: retained origins (r > u = w_0 + 2s + 2) give cubes whose normal base coordinates stay
more than w_0 from the sheet centre, so no cube meets S_z, and Q_z^o W'_z = W'_z; A - A', B - B' <= C R^2 H^2 <= C u R^3 and
A, B >= R^4/16; the log cutoff energy: crossing edges at radius j number <= Cj, difference <= 1/(j log(H/u)), sum
<= C(1 + log(H/u))/log^2(H/u); the decomposition tau_v p' - p' = (tau_v chi)(tau_v p - p) + p(tau_v chi - chi), the pointwise
bound |tau_v p - p| <= C|v|/R, the support count C R^2 (H+s)^2 for the cross term, and the relative loss
(H+s)/(R sqrt(log)) <= C/log(R/u) (since (log x)^(3/2) <= C x^(1/2)). Tests on revealed links commute with the retained D_x
because no retained cube meets S_z. (A')^2/B' >= (1 - Cu/R)^2 A^2/B. The several-sheet extension (L392) is a sketch but is
routine.

**(35), L440-L446: HOLDS.** sup over f of |<g,f>|^2/<f,(L+eps)f> = <g,(L+eps)^-1 g>; monotone limit in eps (the ratio for
each f increases as eps decreases, so the two suprema and the limit interchange); Tonelli on the spectral measure gives
int_0^infty norm(exp(-uL/2) g)^2 du = <g, L^-1 g>, both infinite if g has mass at 0.

**Power tail and example, L448: HOLDS.** The semigroup norm is nonincreasing; the dyadic integral gives
T[1 + A_0/(1 - 2^-delta)]. Example: (1 - eta^2) e^-T + eta^2 e^(-eps T) <= e^-T + eta^2 and integral
1 - eta^2 + eta^2/eps.

No defect found in Step 2. Inputs not yet checked: (10) (row 1155 (9)), (11)-(13) (row 1141), and the row 1254 citations.

## Step 3. Slow sheets (20), (25) and their full-law variance loss (31)-(32) (done 2026-11-20T12:21Z)

Input read first: row 1155 (9) = `gap-solve7-astra62.md` L130-134, E exp(c beta sum_(p in S)(1 - w_p)) <= C^|S| for any set
S of distinct plaquettes, c = 1/8; checked HOLDS in `gap-solve7-check-opus.md` L349-351 (row 1156). Its proof (transfer
matrix in a direction shared by the marks, one-link multiplier ordering, Schatten Hoelder with exponent the period, Hoelder
over four direction classes) uses no property of the torus size. Row 1262 applies it on a periodic s^4 box, on the
periodic d^4 lattice and on "an even torus"; row 1155 states it "on either periodic torus" of its own setting. I take the
extension to any periodic torus as valid (the proof does not read the side lengths). Not a defect.

**(10), L107-L113: HOLDS.** Identify the 4 s^4 cube variables with the periodic s^4 links; internal faces agree; the other
terms (crossing in one, wrapping in the other) number <= C_1 s^3, each 2q_p in [0,2], so the normalized densities differ
by a factor <= exp(4 C_1 beta s^3) uniformly in the exterior. Moment comparison plus Jensen:
2c beta |J| P_y Y <= C beta s^3 + |J| log C_0, and |J| >= s^4/16 gives C(1/s + 1/beta). The restriction to even s is
not needed by the proof but is harmless.

**(11), L115-L120: HOLDS.** Same split as (7): int 1_B |g|^2 <= 2 int (P 1_B)|P g|^2 + 2 norm(D g)^2 <= 2u norm(g)^2 +
2 norm(D g)^2; first term gives 2u_i E, second gives 2592 (s/R)^4 E per event via (8). Union by 1_(union) <= sum 1.

**Setup (21), L229-L237: HOLDS.** The tx and ty plaquettes through q_x give Re(q_x V q_y^-1 U^-1) =
1 - |q_x - U q_y V^-1|^2/2, so the conditional density is exactly (21). The two tz plaquettes through q_x give
Re q_x - Re q_x = 0 with the pins +1 (z = -1) and -1 (z = +1). Prescribed-plaquette bounds: tangential plaquettes are
products of <= 4 factors of angle <= theta (1 - w <= 8K/beta); mixed plaquettes at t = 0, z != 0 are
g V g^-1 U^-1 with angle <= 2 theta; the t = d-1 plaquettes are U V^-1 with angle <= eta theta; arc plaquettes have angle
pi/(d-2) <= pi/sqrt(beta).

**Linear stiffness, L239: HOLDS.** On C_i + C_i j the marked map v -> e^(theta i) v e^(-(1-eta) theta i) is
a -> a e^(eta theta i), b j -> b e^((2-eta) theta i) j, so the displacement is >= 2 sin(eta theta / 2)|v|. The ten unmarked
template bonds connect the nine sites. Individual adjoint forms: rotations about i and j by 2(1-eta) theta and 2 theta give
>= 4 sin^2((1-eta) theta)|v|^2. All constants depend on the fixed eta, K.

**Bad-tile energy and (22), L241-L249: HOLDS.** Bad tile at eta = 0: 4 sin^2(theta)|u|^2 <= C E^0, distance to the nearer
sign <= sqrt(2)|u|, so E^0 >= c_0 theta^2. Only the marked i-bond differs at eta > 0, by at most eta theta, so
E^eta >= E^0/2 - eta^2 theta^2. Entropy: half the exponent pays (beta/2) M c_0 theta^2/4 = c_0 K M/8; a spanning tree gives
exactly z(beta/2)^(n-1); z(b) <= C b^(-3/2); the lower bound uses the beta^(-1/2) cap, mass >= (c beta^(-3/2))^n, bond
displacement <= 2 beta^(-1/2) + eta theta, 2n bonds. The exponents combine to (22), including the (3/2) log beta / M term.

**Chessboard, L251: HOLDS.** Every line of sites with even coordinate is a reflection line of the reflected template (the
pattern has period 4 and m is even), each line has an antipodal partner at distance d/2, the bond weight is invariant
under the reflection (|q_y - U^-1 q_x V|^2 = |q_x - U q_y V^-1|^2), and given the two line spins the halves are independent
with reflected laws. The maximizer argument (phi(S) = log Pr(S) - (|S|/M) log Pr(all), doubling a marked interval, m dyadic)
is the standard one and is correctly applied: intermediate maximizers may carry extra marks, which does not matter because
they contain the doubled interval.

**F and its centring, L253: HOLDS.** Caps are disjoint; a (1,0) and a (0,1) cycle on the coarse torus share a vertex, so
opposite signs cannot both qualify. Cap membership is Re q >= 1 - 1/32 (or <= -(1 - 1/32)), a function of one plaquette
trace. The global flip q -> -q preserves (21) and Haar measure and maps F to -F.

**Band bound and (20), L255-L257: HOLDS.** Duality on the cylinder: no open winding cycle gives a closed-edge dual crossing;
every face it enters is adjacent to a closed edge, so it is bad; >= h - 1 distinct faces; at most 4^l simple dual paths of
length l per start; chessboard p^l. Two horizontal and two vertical bands at offset m/2: a side-s update with s <= d/16
(= m/16 coarse rows) touches at most one band per direction, and the surviving horizontal and vertical cycles force the
same sign, so F is unchanged when the old configuration is good; if the new one is good the same holds by exchangeability;
so (1/2)E(F - F')^2 <= 2 Pr(exceptional). Origins hitting the sheet: s^2 normal times d^2 tangential, weight s^-4.
Var F >= 1 - C m^2 e^(-cm). Quotient C (d/s)^2 m^2 e^(-cm), which is (20).

**Open neighbourhood, L259: HOLDS** (qualitative; ties have zero Haar probability, dominated convergence).

**(23), L263-L272: HOLDS.** min over q' of -(q - 1).q' is -|q - 1|, and Re q = 1 - |q-1|^2/2 gives
3/2 + (|q-1| - 1)^2/2. Caps: |q - 1| <= 1/4 or >= 7/4 give excess >= 9/32. The comparison configuration
(e^(pi i/3), e^(2 pi i/3)) has vertical energy exactly 1/2 + 1/2 + 1/2. Each column marks at most 4 tiles, so >= M/4
columns pay. The M-th root bound exp[-9 beta/128 + C beta/d + C(1 + K + log beta)] is e^(-c' beta) once d >= sqrt(beta).

**(24) and the fixed-thickness sheet, L274-L300: HOLDS.** Antiperiodic extension to Z_(2L): odd modes only, least
eigenvalue 2(1 - cos(pi/L)), equality on modes 1, 2L-1; q_0 = 1 fixes a = 1; unit length at k = 1, L-1 gives Re v = 0, |v|
= 1 when L >= 3. The compactness argument for a_w is valid (bad set closed, excess continuous and nonnegative, zero
excess with the marked bond forces v = +-i). Perturbation by xi, eta: edge by edge |a + w|^2 >= |a|^2/2 - |w|^2. Symmetry
q_(k,x) -> -q_(L-k,x) fixes the pins (q_0 = -q_L = 1), the vertical and horizontal energies (identical backgrounds at all
heights) and negates the reading. Loop realization: (cos theta Re q - Re(e^(theta i) q))/sin theta = Im_i q. Origins meeting
a free link: s(s + w - 1). Reading magnitude on a good tile >= sqrt(3)/2 - 1/8 > 1/2.

**(25)-(26), L304-L337: HOLDS.** (26): the cross term after summation by parts is 2(1 - cos alpha) sum b.y and
2 b.y = -|y|^2. Mode split: the first Dirichlet mode cancels exactly; ratio of first to second eigenvalue
1/(4 cos^2(alpha/2)) <= 1/3 gives sum |Delta e|^2 <= 3 D_v; |e_k| <= sqrt(3 L D_v). At L/2 and L/4: ||v| - 1| <= eps, ||1+v|/sqrt
2 - 1| <= eps, so |Re v| <= C eps. Bad-tile bound: D_v <= 4D (weight >= 1/4), eps <= sqrt(12 u) L theta <= C sqrt u;
the first-sine-coefficient functional has norm sqrt(2/L), so |v_x - T v_y| <= C sqrt(D/L) <= C sqrt(u) theta; the marked
bond gives |v_perp| <= C sqrt u. Lower partition: |y_k| <= beta^(-1/2) gives D_v <= 2(w+1)/beta. The per-tile exponent
-cKw + Cw + C(eta^2 + xi^2)Kw + (3w/2M) log beta is right, and p = e^(-c'Kw) gives e^(-cwd) in the band bound.
Completion: L = 4 floor(sqrt(beta/K)/4) has L theta <= 1; inner tz plaquettes cost 1 - cos(pi/L) <= C K/beta; mixed
plaquettes C(eta^2 + xi^2) K/beta because the unperturbed maps fix C_i; arc steps pi/(d - L) <= pi/sqrt(beta).

**(27)-(28), L341-L350: HOLDS.** |1 - U_C| <= sum_p |1 - U_p| by bi-invariance, q_C = |1 - U_C|^2/4, Cauchy-Schwarz gives
J sum q_p. Markov with (9) on <= J M_0 distinct plaquettes gives (28). The d^2 rectangles 1 x L in tz have holonomy
1 . (-1)^-1 = -1 whatever the free links, q_C = 1; with J = L <= sqrt(beta/K) the exponent is
-d^2 (beta/L)(c - log C_0 / K), which is -c_1 beta d^2 / L for large K.

**(29) and the filling test, L352-L359: HOLDS.** (27) turns the indicator into J/(h M_0) times at most J M_0 plaquette
terms, each bounded by (7)-(8); only the event needs to be exterior-measurable. The filling test: a failing exterior makes
every filling, in particular the actual one, violate some list, so 1_fail <= sum of the k means / h.

**(31), L398-L402: HOLDS.** Outside the positive cap means q_p > 1/64 for that tz plaquette; distinct coarse vertices use
distinct plaquettes; (9) and Markov give (C_0 e^(-c beta/32))^j for j specified vertices. A closed edge (for positive-cap
openness) has an endpoint outside the cap; choosing one per crossed edge is at most 4-to-1 (a coarse vertex has degree 4),
so a dual path of n steps needs >= n/4 distinct bad vertices; at most 2^n choices and 4^n paths; n >= m/8 - 2. F != +1
needs a band without a positive winding cycle (two bands suffice). Var F <= E(F - 1)^2 <= 4 Pr(F != 1).

**(32), L404-L412: HOLDS.** |cos theta Re B - Re(AB)| <= (1 - cos theta) + |1 - A|; magnitude > 1/2 at one of the two
heights forces |1 - A| >= sin(theta)/2 - (1 - cos theta) >= 0.37 theta >= theta/4 for theta <= 1/4 (A is the same marked
loop for both heights). A is a conjugate of one elementary plaquette, distinct per coarse vertex, 2q_p = |1 - A|^2/2 >=
theta^2/32, so (9) gives (C_0 e^(-cK/32))^j with theta^2 = K/beta. F != 0 needs an open winding cycle, which has >= m
distinct vertices; m^2 4^l cycle count. Increasing K is compatible with (25), whose K only needs to be large.

**Correlations, L414: HOLDS** (Cauchy-Schwarz with the variances of (31)-(32)).

What (31)-(32) show and do not show: the two readings are nearly constant in the full periodic Wilson law, so the conditional
slow modes (20), (25) are not slow modes of the full law at these normalizations. As row 1262 says (L414), this gives
nothing about other interior observables. No defect found in Step 3.

## Step 4. Remaining statements, and the cited rows they read (done 2026-11-20T12:26Z)

**Parameter choice, L103: HOLDS.** With m_s from (5), h = beta^(-1/3), s = ceil(beta^2), R >= beta^4:
rho = k beta^(1/3)[C(beta^-2 + (1 + log beta)/beta) + C beta^-8] -> 0. Centre flux has q_p = (1 - (-1))/2 = 1 on its
plaquettes, so the face test rejects it.

**Last sentences of L113: HOLDS.** With h = K/beta and m_s = C(1/s + 1/beta), rho = (k/K)[2C(beta/s + 1)(1 + o(1)) +
2592 beta (s/R)^4], small for large K when s >= beta and beta (s/R)^4 is small.

**(12)-(13), L122-L142: HOLDS**, using row 1141 (3), (4), (6), (7) (`gap-crux2-astra62.md` L55-L101; checked HOLDS by row
1142, `gap-crux2-check-opus.md` S6-S12, Claude; I re-read the statements and proofs). Checked here: the face cells are
exterior to the patch but inside one translated side-s update, so (4) (acceptance >= 1/2 given everything outside the
cell, also given fewer links) gives P_y 1_B <= u uniformly in the update's exterior, as (11) needs; the iteration
E 3^(-sum G) <= (2/3)^N and Markov give e^(-gamma N), gamma = log(27/16)/4, N >= r^3/216; union over (s/r)^3 small
rectangles and C(R/s)^3 first rectangles gives (12) through (11). (13): on an accepted root |v|^2 <= C(1+beta) times the
eight bond terms (telescoping around the two squares; (5) is not even needed, D >= delta_b gives the factor 4/delta_b);
Neumann Poincare for |v| (Ad is an isometry); mean squared controlled through the root density rho; sum over rectangles.
r = ceil((D log(2+R))^(1/3)) gives C(R/r)^3 e^(-c r^3) <= C R^3 (2+R)^(-cD) -> 0, and r^2 + 1 + beta = O(beta) when
log R = O(beta). The ARGUED paragraph L144 is correctly labelled.

**Collar tests, L162-L166: HOLDS.** Moment comparison on an l^4 four-box with l >= beta: Markov gives
exp(-(l-1)^4 (2cK - log C_0) + C_3 beta l^3) <= e^(-c_1 l^4) for large K, since beta l^3 <= l^4 and (l-1)^4 >= l^4/16.
The four-box lies inside a side-s update (l = s/4), so the bound holds given that update's exterior (nested
conditioning). C(R/s)^3 four-boxes per face give C(R/s)^3 e^(-c_1 l^4) + C s/R by (11).

**(18), L198-L204: HOLDS, conditional on row 1231 (35).** rho_* -> 0: s^(1/3)(1/s + log beta/beta) -> 0 and
s^(1/3)(s/R)^4 -> 0 for s ~ R^(1/2) ~ beta^(delta/2); r ~ (log R)^(1/3) <= s/32 eventually. Inputs: (a) row 1231 (35)
(`gap-solve26-astra62.md` L357-L365, proof L376-L387): A = H_m, any lower bound varpi on gauge-invariant mean-zero
functions has varpi r/m -> 0 when m <= C_0 r, on beta -> infinity, beta <= B log N, r = floor(beta^delta). I read the proof:
finite-speed bound (36) for the Poisson-clock cube dynamics against the packet covariance K_mag(s) ~ s^-8 from its (9)-(11).
Checked HOLDS by row 1235 (`gap-solve26-check-opus.md` L268, L401, Claude Opus 5.5). I did not redo (9)-(11) of row 1231.
(b) row 1254 (37) (`gap-solve29-astra62.md` L468-L473), which I re-derived (below). The logic of L204 is right: a
subsequence with v_s (R/s)^2 >= c gives v_R >= 2^-20 min(1, c) by (37), against (35) at m = R; and (15) with
(R/R')^4 >= 1/16, b_R >= 1/16, rho_* -> 0 gives v_s >= min{1, c gamma - 40 pi^2 (s/R)^2}, so gamma/(s/R)^2 -> infinity
would force v_s (R/s)^2 -> infinity.

**Row 1254 (17)-(19) and (37), re-derived here (they are inputs of (18)).** (18): A norm(f)^2 = sum_z <(1 - P_t(z)) f, L_z>
since sum_z L_z = A H_s g = A f and L_z lives inside V_t(z); Cauchy-Schwarz. (19): far pairs have nonnegative cross terms;
close pairs cost s^-8 eps B (2s+1)^4 sum_x norm(D_x g)^2 = eps B (2+1/s)^4 <g, H_s g>. Trapezoid weight: sum of squared
increments 2/w, sum u^2 >= k - 2w >= k/2, so a unit shift costs norm^2 <= 4B/(kw), at most 4s unit shifts give
eps = 32 s^2/(kw); A^2/B >= (k - 2w)^4. (37): t < 8s by nesting, (s/t)^4 >= 8^-6 (t/s)^2; t >= 8s with w = floor(k/4):
(k - 2w)/t >= 7/16, (7/16)^4 > 1/64, denominator <= 1 + 1280 * 512/(49 x) <= 1 + 14000/x with x = (t/s)^2 v_s, and
x/(x + 14000) >= min(x,1)/14001, 64 * 14001 < 2^20. All HOLD. Row 1261 (`gap-solve29-check-opus.md`, Claude Opus 5.5,
same model as this checker) also found them HOLDS; mine is not an independent derivation path, but it was redone by hand.
Process note on that file: its step stamps run to 13:55Z, yet its last commit (07796730c) is 11:36Z, so those stamps are
not `date -u` values.

**Collar cost, L206: HOLDS**, using row 1155 (20) (`gap-solve7-astra62.md` L294-L318, checked HOLDS in row 1156). Temporal
gauge along normal lines; chord^2 between levels = 2 x normal plaquette deficit; Cauchy-Schwarz over w levels gives
beta d_G(X,Y)^2/(2w). The small-ball bound needs only marked plaquettes with disjoint edge sets and selected links whose
conditional law is a tilt with |k| <= 6 beta, so it holds on a box face with fixed exterior (stride-four subgrid). With
w = O(d), beta >= 1: beta c d^3/((1+beta) 2w) >= c''' d^2. The closing caveat (a difference of actions could cancel) is right.

**(19), L210-L217: HOLDS**, using row 1155's angle lemma (L301-L305). |v - H_U v H_V^-1| = |H_V - v^-1 H_U v| >= chord of
|alpha - alpha'| >= (2/pi)|alpha - alpha'| (class angle = distance to 1, conjugation invariant). Angle density
<= C sqrt(1 + 6 beta) with the reference angle alpha' fixed (the V face lies outside the update that holds the U cell),
so acceptance >= 1/2 for small c. Telescoping around the accepted plaquette with the linear isometries v -> U v V^-1,
then the scalar Neumann step for |v|.

**(33), L418-L423: HOLDS.** Conditioning on more (S_z) can only shrink the update residual, so each summand is
<= norm(D_x f)^2; cubes avoiding S_z give exactly D_x, so L-hat >= L-circ and the budget (R')^4 E is unchanged.

**(17) for (33), L425: HOLDS.** The bisection deletes the same <= 48 l^3 terms (an empty child is allowed); a terminal tile
updates its free subset, which every containing cube also resamples.

**(34), L427-L432: HOLDS.** Cubes avoiding pins have x_1 mod h in {1, ..., h-s}; a progression with step v_1 in [s/2, s]
cannot jump s consecutive zero layers and meets them within J = ceil(2h/s) + 2 steps; telescoping gives
norm(p_0)^2 <= J^2 norm(tau_v p_0 - p_0)^2; at least (s/2)(2s+1)^3 such v. The reading (a lower bound on the error term
of the method, not on the gap) is the one the file states.

**Dense pinned grid, L434-L436: HOLDS.** Free base points of different open cells differ by >= 2 in some coordinate, so no
plaquette couples two cells; the Efron-Stein components f_J over the cells; resampling the cells inside a cube counts each
f_J meeting it; each cell of side h - 1 lies in >= (s - h + 2)^4 cubes with origins in I_z^out (b >= s); h <= s/2 gives
((s-h+1)/s)^4 >= 1/16. The file correctly says this regime has no uncut origins for (3).

**GUIDE/OPEN statements.** L192 (sewing obstruction from row 1155 (20)) and L219 (Durhuus-Froehlich layer form; it is the
same identity as (21)) are fair GUIDE readings. L194 and L450 are true: 2^-8 e^(-440 beta t^3) at t ~ 1/a is far below
(s/R)^2. L452 is right that the continuum step is not done here.

No defect found in Step 4.

## Step 5. Cited rows, and the citations of the GUIDE paragraphs (done 2026-11-20T12:29Z)

Each cited statement that a step depends on, with what I read:

| Cited statement | Used at | Read | Standing |
|---|---|---|---|
| row 1155 (9), marked-plaquette moment, `gap-solve7-astra62.md` L130-L134 | (10), (28), (31), (32), collar tests L162 | statement and proof | checked HOLDS by row 1156 (`gap-solve7-check-opus.md` L349-L351, L464); proof reads no torus size, so its use on the s^4 box and the d^4 lattice is valid |
| row 1155 (20) and angle lemma, L294-L318 | (19), L192, L206 | statement and proof | checked HOLDS by row 1156; the disjoint-plaquette argument transfers to a box face with fixed exterior |
| row 1141 (3), (4), (6), (7), `gap-crux2-astra62.md` L55-L101 | (12)-(13) | statement and proof | checked HOLDS by row 1142 (S6-S12) |
| row 1254 (17)-(19), (37), `gap-solve29-astra62.md` L226-L251, L468-L473 | (18); method of (3)-(4) | statement and proof, re-derived by hand (Step 4) | HOLDS here; row 1261 (same model) also HOLDS. Row 1262 L452 calls row 1254 unchecked; at this pin it has that check |
| row 1231 (35)-(36), `gap-solve26-astra62.md` L357-L387 | (18) | statement and proof of (35)-(36); its packet input (9)-(11) not redone | checked HOLDS by row 1235 (`gap-solve26-check-opus.md` L268, L401) |
| row 1139 folded chessboard | (20)-(25) | not reopened: I checked the reflection structure directly (Step 3) | not needed |
| row 1254 (17), (1)-(4) continuum chain | (16) last sentences L174 | statement of (17), (20) only | a stated premise list, not a step of (5)-(15); (16) itself HOLDS without it |
| row 1222 (1)-(2), row 1177 (22), row 1224 7.6 | L434, L219, L55 | not needed | comparisons only, no step depends on them |

Citation checks of the GUIDE paragraphs (sources fetched into a scratch folder, not committed):

- **L5, Sussman-Alpoge: HOLDS.** At `31a47c543775`, outline L581-L599 (cyclic sector of the action density; polynomial
  clustering with spectral measure E e^-E dE gives no gap), L773-L780 ("This proves a scalar block-constrained gap"),
  L31860-L31882 (same two points in the conclusion); CA-I L2704-L2712 ("Not asserted: ... a mass gap") and L3213-L3222
  ("Clustering and uniqueness of the vacuum (OS4). Not asserted."). All five ranges say what row 1262 says.
- **L3, other branches: HOLDS where checked.** main is `8b11ae2` as cited; its `research/mass-gap/library/gap-phys-seed.md`
  L305-L312 is Corollary Z2 (uniform cube gap plus a state count D gives a seed). PR 10114
  `MASS_GAP_LOCAL_BLOCK_ASTRA.md` L4-L14: one-step plaquette witness, contraction only at 0 < beta <= 1/32. PR 10133
  `MASS_GAP_CROSSOVER_REDUCTION.md` L77-L86: MG2 (source transport) and CW open. PR 10141 `fp1.md` L299-L315: single-scale
  Landau-lift minimizer (classical). PR 10134 I1-I5 not checked. "The row-specific prior file is absent at the pin": no
  prior digest named for row 1262 exists; row 1218's digest `prior/gap-onebound-read-sol.md` was present at `ad8d21df2`
  (added in `c3b9f704d`). Wording only; nothing rests on it.

## Step 6. Is the main comparison a restatement of an earlier row? (done 2026-11-20T12:29Z)

The main comparison is (1) => (2): a local patch Poincare constant gamma for the side-t box with fixed exterior gives a
global gap of the side-s block heat bath of at least b_R gamma - e_(s,R), with e_(s,R) of order (s/R)^2. Its variants are
(9), (15), (30), with (33) and (35) as reformulations of the local input. Searched: `library/open-core.md` (no match for
finite-size, Knabe, inverse-square), the FINISH rows (perl context search for inverse square, Knabe, Gosset, finite-size
criterion: rows at FINISH lines 746, 763, 779, 790, 796, 812, 827, 836, 847, 1071, 1094, 1113, 1135), `library/` for
Knabe, Gosset, Mozgunov, Anshu, Lemm.

**Answer: not a restatement. It is the first proof on file of this inverse-square criterion for the Wilson block heat bath.
Its method is not new on file.** Details:

1. **Method = row 1254 (17)-(19).** The patch Cauchy-Schwarz with a projection that kills the weighted patch sum, far cubes
   with commuting projections and nonnegative cross terms, and the absolute close-pair bound are row 1254's (18)-(19).
   Row 1262's (4) is row 1254's (19) with the sine weight instead of the trapezoid, and with the explicit constant
   e_(s,R); row 1262 says so (L11, L38). The statements differ: row 1254 (17) goes from the global small-cube gap v_s to
   the global large-cube gap v_t (dual vector g = H_s^-1 f); row 1262 (2) goes from a local fixed-exterior constant to v_s.
2. **Statement proposed, not proved, in `gap-skeleton-max.md` B7** (L159-L165): the Knabe-type threshold of order n^-2 for
   the frustration-free heat-bath generator, recalled "from memory", with the crux (K) killed at perturbative n by the
   gap bound A.1, and the rule that a criterion can only work where it is not met at a perturbative scale. Row 1262 keeps
   that rule: (16) puts R at physical size (a R -> L > 0), and (18) is a proof, through rows 1231 and 1254, of B7's kill
   at R = beta^delta.
3. **Sharpens the six authors' Lemma G.2 / Theorem G.4** (A's Appendix G, read and checked in row 1224,
   `gap-mini-solve-q-fable.md` L179-L192): there a patch gap gamma gives a global gap only above a threshold of order 1/p
   (gamma p >= 148). Row 1262 moves the threshold to order (s/R)^2. Row 1262 L7 cites this reading correctly.
4. **Different from row 746's pair criterion PA / PA_g** (`gap-crux-exercise-astra.md` L768-L790, L1328-L1343): that one
   is an alternating-projection overlap bound for a coloured block cover, A^2 >= (1 - d eta) A, not a patch Poincare
   constant.
5. **Literature.** The weighted-patch inverse-square threshold for frustration-free quantum sums is Gosset and Mozgunov
   (arXiv:1512.00088; 1D, and 2D with 8/n^2), cited by row 1262. For general lattice dimension, Anurag Anshu,
   "Improved local spectral gap thresholds for lattices of finite dimension", arXiv:1909.01516 (2019), states a
   threshold optimal up to a dimension-dependent constant, by the detectability lemma and a coarse-grained Hamiltonian
   (abstract read; body not read). Row 1262 does not cite Anshu, and the lane's block-criteria digest
   `prior/gap-lit-block.md` does not list it. Row 1262's proof is its own (sine weights, conditional expectations, no
   detectability lemma), and FINISH row 755 (line 836) found no such criterion established for a continuous-group lattice
   gauge theory. Repair: add the Anshu citation as prior work on the quantum side.

## Step 7. Guide-only numeric run (status 2026-11-20T12:32Z)

Not started so far: `memory_pressure` reported 47, 48 and 40 percent free at 12:30Z-12:31Z, below the 50 percent
floor for this machine. Every statement above was checked by hand, so the verdicts do not wait on a run. Two guide
scripts are written in a scratch folder (not committed): (T1-T6) the constants b_R >= 1/16 and e_(s,R) <= 40 pi^2
(s/(R+1))^2, the 1D overlap bound, the lattice sum 4(2s+1)^4 s(s+1)/3, the closed form (23), the identity (26), and
the two forms of C_loc in (35); (T7) a d = 1 analog of (1) => (2) on an Ising ring of 14-16 spins with block heat bath,
pass criterion written first: v_s >= b gamma - e with b = (sum sin)^2/(R sum sin^2), e = (1 - cos theta)(s+1)(2s+1)/3.
If memory recovers before the end, the run goes under the numeric lock and its output is appended here.

Row 1262's own wording at L452 ("row 1254 ... is unchecked at this pin") was right for its pin `ad8d21df2`: the check
of row 1254 (`07796730c`) is not an ancestor of that commit.

## Step 8. Verdicts (done 2026-11-20T12:33Z)

Provenance: checked line by line by Claude Opus 5.5 (max), Mac mini worker 1, at commit `536662306`, by hand; a check,
not an audit. Author of row 1262: gpt-6.2-astra max (cross-provider). Verdict per statement, with the line in
`library/gap-solve30-astra62.md`.

| Statement | Lines | Verdict |
|---|---|---|
| **(15) conditional Wilson estimate with a collar**, with (14) | L148-L158 | **HOLDS** |
| **(30) with a revealed codimension-two sheet** | L363-L392 | **HOLDS** |
| **(35) integrated-correlation form of the local constant** | L440-L446 | **HOLDS** |
| **(17) finite-volume bound gamma = 2^-8 exp(-440 beta t^3)** | L178-L188 | **HOLDS** |
| (1) => (2), with (3), (4), kernel, b_R >= 1/16, e <= 40 pi^2 (s/(R+1))^2 | L13-L51 | HOLDS |
| (5) | L57-L73 | HOLDS |
| (6)-(8) | L75-L95 | HOLDS |
| (9) | L97-L101 | HOLDS |
| parameter choice, centre-flux exclusion | L103 | HOLDS |
| (10), on row 1155 (9) | L107-L113 | HOLDS |
| (11) | L115-L120 | HOLDS |
| (12)-(13), on row 1141 (3)-(7) | L122-L142 | HOLDS |
| ARGUED paragraph | L144 | correctly labelled |
| face readings have Q_z f = 0 | L160 | HOLDS |
| mesoscopic collar tests | L162-L166 | HOLDS |
| (16) sufficient physical-scale condition | L168-L174 | HOLDS (the last sentences cite row 1254's premises; they are listed, not proved, as the text says) |
| oscillation of the first bisection | L190 | HOLDS |
| GUIDE L192, OPEN L194 | L192-L194 | fair / true |
| (18), on row 1231 (35) and row 1254 (37) | L198-L204 | HOLDS (given row 1231 (35), checked HOLDS by row 1235) |
| collar electric cost, on row 1155 (20) | L206 | HOLDS |
| (19) | L210-L217 | HOLDS |
| GUIDE (Durhuus-Froehlich layer form) | L219 | fair |
| **(20)-(22) slow conditional sheet** | L223-L259 | **HOLDS** |
| (23) one released plane | L263-L272 | HOLDS |
| (24) and the fixed-thickness sheet | L274-L300 | HOLDS |
| **(25)-(26) thickness of order sqrt(beta)** | L304-L337 | **HOLDS** |
| (27)-(28) | L341-L350 | HOLDS |
| (29), common-filling test | L352-L359 | HOLDS |
| consequences for tubes | L394 | HOLDS |
| **(31) variance loss of the reading of (20) in the full law** | L398-L402 | **HOLDS** |
| **(32) variance loss of the reading of (25) in the full law** | L404-L412 | **HOLDS** |
| vanishing correlations | L414 | HOLDS |
| (33) and (17) for (33) | L418-L425 | HOLDS |
| (34) | L427-L432 | HOLDS |
| dense pinned grid | L434-L436 | HOLDS |
| power tail and two-dimensional example | L448 | HOLDS |
| OPEN | L450, L452 | true as stated |
| Repo search and Sussman-Alpoge citations (GUIDE) | L3-L11 | HOLDS where checked (Step 5); PR 10134 not checked |
| RESULT line | L454 | HOLDS |

FAILS: none. HOLDS AFTER CORRECTION: none needed for any proof step.

Defects, ranked (none breaks a statement):

1. Credit (L11). The inverse-square local-gap threshold in any lattice dimension has a prior quantum form: A. Anshu,
   arXiv:1909.01516, for frustration-free Hamiltonians, optimal up to a dimension constant (abstract read only).
   Row 1262 cites Knabe and Gosset-Mozgunov but not Anshu. Repair: cite it as the quantum analogue. Row 1262's proof
   (sine weights with conditional expectations) is its own.
2. Wording (L3). "The row-specific prior file is absent at the pin": true only if it means a digest named for
   row 1262. The row 1218 digest named in the brief was present at `ad8d21df2`, and L7 uses it.
3. Scope note (L111). Row 1155 states (9) "on either periodic torus" of its own setting; row 1262 uses it on the
   s^4 box and on d^4 lattices. The proof of (9) reads no side length, so this is valid. The restriction to even s in
   (10) and L162 is not needed.

Restatement (Step 6): the main comparison (1) => (2) and its variants (9), (15), (30) are not a restatement of an earlier
row. The method is row 1254's (18)-(19) (row 1262's (4) is row 1254's (19) with a sine weight). The statement was
proposed without proof in `gap-skeleton-max.md` B7. It sharpens A's Lemma G.2 (read in row 1224), whose threshold is of
order 1/p, to order (s/R)^2. It differs from row 746's pair criterion PA_g.

What the check does not show: nothing here proves the local input (14) or (35) at the scale (16) for the Wilson law.
The only bound on file is (17), which is exponentially small in beta t^3. (18) shows that at R = beta^delta the
constant cannot exceed (s/R)^2 in order. (31)-(32) remove only the two exhibited readings. The continuum chain behind
(16) (row 1254 (17), (20) and its premises) is outside this check. The mass gap stays open.

RESULT: Row 1271 check of row 1262 (Claude Opus 5.5 max, by hand, cross-provider): every statement HOLDS, no FAILS, no correction needed in a proof step. HOLDS: the conditional Wilson estimate (15), (30), (35) with the finite-volume bound (17); the full-law variance loss (31)-(32) of the slow sheets (20), (25); everything else. The main comparison (1) => (2) is not a restatement: it uses row 1254's (18)-(19) method and proves the inverse-square criterion that `gap-skeleton-max.md` B7 proposed. One citation to add (Anshu, arXiv:1909.01516). OPEN: the local input (14)/(35) at order (s/R)^2 for the Wilson law, the continuum premises of (16), and the mass gap. The guide run was not started (memory 40-48 percent free).
