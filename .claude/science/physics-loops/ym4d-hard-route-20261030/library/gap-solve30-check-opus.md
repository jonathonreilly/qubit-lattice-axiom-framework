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
eigenvalue 2(1 - cos(pi/L)), equality on modes 1, 2L-1; q_0 = 1 fixes a = 1; unit length at k = 1, L-1 gives Re v = 0,
|v| = 1 when L >= 3. The compactness argument for a_w is valid (bad set closed, excess continuous and nonnegative, zero
excess with the marked bond forces v = +-i). Perturbation by xi, eta: edge by edge |a + w|^2 >= |a|^2/2 - |w|^2. Symmetry
q_(k,x) -> -q_(L-k,x) fixes the pins (q_0 = -q_L = 1), the vertical and horizontal energies (identical backgrounds at all
heights) and negates the reading. Loop realization: (cos theta Re q - Re(e^(theta i) q))/sin theta = Im_i q. Origins meeting
a free link: s(s + w - 1). Reading magnitude on a good tile >= sqrt(3)/2 - 1/8 > 1/2.

**(25)-(26), L304-L337: HOLDS.** (26): the cross term after summation by parts is 2(1 - cos alpha) sum b.y and
2 b.y = -|y|^2. Mode split: the first Dirichlet mode cancels exactly; ratio of first to second eigenvalue
1/(4 cos^2(alpha/2)) <= 1/3 gives sum |Delta e|^2 <= 3 D_v; |e_k| <= sqrt(3 L D_v). At L/2 and L/4: ||v| - 1| <= eps,
||1+v|/sqrt 2 - 1| <= eps, so |Re v| <= C eps. Bad-tile bound: D_v <= 4D (weight >= 1/4), eps <= sqrt(12 u) L theta <= C sqrt u;
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
