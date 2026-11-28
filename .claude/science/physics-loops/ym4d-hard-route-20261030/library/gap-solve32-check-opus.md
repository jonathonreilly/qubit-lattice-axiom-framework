lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:21Z

# Check of row 1283 (`library/gap-solve32-astra62.md`), FINISH row 1289

Research-stage working state. It grants no status and is not a public claim.

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, at commit 1ce538a51
on branch `claude/ym4d-hard-route`. The checked file was written by a
gpt-6-astra lane (row 1283), so this is a cross-provider check. It is one
check by one model; it is not an independent derivation unless a step below
says it uses a different route.

## Plan (at most eight steps; each response does one step and appends here)

1. Read FINISH rules (Build on published work, efficiency), the row 1283
   text, and the checked file in full; list its numbered claims and the
   earlier rows it cites.
2. Check the short-time slice information bounds (29)-(32), line by line.
3. Check the recovery (35) of flux sector ratios from neutral histories.
4. Check the endpoint removal (36)-(40).
5. Check everything else in the file (setup, definitions, remaining
   numbered statements, the conclusion), with cited earlier rows read where a
   step depends on them.
6. Decide whether the main comparison is a restatement of an earlier row
   (grep `library/open-core.md`, FINISH rows, cited files).
7. Optional numeric guide only if useful and memory allows (guides only;
   no verdict rests on it).
8. Verdict table per statement and the RESULT line.

## Step log

(Each step appends below as it finishes.)

### Step 1 (done): inventory and cited rows

Read in full: `library/gap-solve32-astra62.md` (541 lines, at 1ce538a51), the
row 1283 text, GOAL.md, FINISH.md (opening sections, How we work, Working
efficiently, Rules).

Numbered claims of the checked file, by section and line:

| Lines | Claims | Label in file |
|---|---|---|
| L16-56 | (1) adjoint-mode count, (2) two-plaquette defect, (3) block Poincare, (4) | PROVED |
| L59-84 | (5) rare-slice probability, (6) energy-band bound, (7) trace ratios | PROVED; L84 OPEN |
| L87-126 | (8) annealed Green bound, (9) kernel domination, (10) walk bounds | PROVED |
| L129-170 | (11) temporal law, (12) covariance, (13)-(14) patch coherence | PROVED |
| L173-220 | (15)-(18) recovery of Ad g_x, (19) replica overlap | PROVED |
| L223-268 | (20)-(22) chessboard and strip bounds, (23) global sign | PROVED |
| L271-343 | (24)-(26) contraction, (27)-(28) endpoint recovery | PROVED; L343 ARGUED |
| L346-401 | (29) separating event, (30) prism identity, (31)-(32) information | PROVED |
| L404-451 | (33) twist candidates, (34) decoding, (35) sector ratios | PROVED |
| L454-487 | (36) singlet bound, (37) restricted kernel | PROVED |
| L490-521 | (38) orbit volume, (39) layer information | PROVED; L521 OPEN |
| L524-539 | (40) rank-one distance | PROVED; L537-539 OPEN |

Earlier rows the positive claims depend on, with their checks (FINISH RESULT
lines read): row 1141 (`gap-crux2-astra62.md`, check 1142 HOLDS); row 1145
(`gap-solve2`, check 1146 HOLDS); row 1149 (`gap-solve4`, check 1150 HOLDS);
row 1151 (`gap-solve5`, check 1152 HOLDS); row 1153 (`gap-solve6`, check 1154
HOLDS); row 1155 (`gap-solve7`, check 1156 HOLDS); row 1215 (`gap-solve23`,
check 1221 HOLDS); row 1231 (`gap-solve26`, check 1235 HOLDS, one credit
correction); row 1262 (`gap-solve30`, check 1271 HOLDS); row 1272
(`gap-solve31`, check 1282 HOLDS). Each was checked once by Claude Opus 5.5;
those checks are not evidence here. I read the cited statements and proofs
where a step below depends on them.

### Step 2 (done): the short-time slice information bounds (29)-(32)

Inputs read for this step: row 1231 (`gap-solve26-astra62.md` L17-135:
(1), (2), (4), (7)-(11)); row 1151 (`gap-solve5-astra62.md` L302-317: (24)
and the pointwise density bound at L313); row 1153 (`gap-solve6-astra62.md`
L80-110: (3)-(6)).

**(29), L350-386: HOLDS.** Redone by hand:

- *Gaussian separation of means (L356-362).* For one colour, two centred
  Gaussians with variances v and covariance D give
  E e^{-a^2-b^2} = det(I+2Sigma)^{-1/2} = [(1+2v)^2-4D^2]^{-1/2}; three
  independent colours give the joint mean [(1+2v)^2-4D^2]^{-3/2}, and
  independence gives (1+2v)^{-3}. D(s) > 0 on [1,2] since the integrand of
  row 1231 (10) is nonnegative and not a.e. zero; D decreases in s, so the
  least joint mean is at s = 2. Since r is the largest power of two at most
  k, k/r lies in [1,2). Image terms: with numerator at most |xi-hat|^2,
  2 sinh(omega) >= c|xi-hat| and k <= N/2, the time images sum to at most
  2e^{-N omega/2}/(1-e^{-N omega}); with |W(q)|^2 <= C r^4 and xi = 2 pi m/N
  the frequency sum is at most C r^4 N^{-4}. So the finite-cutoff Gaussian
  means are within o(1) of the limits, uniformly in k/r in [1,2]. Correct.
- *Prism identity (30), L364-374.* For F = dB, the Bianchi relation gives
  F_12(t+1,z) - F_12(t,z) = (nabla_1 F_02 - nabla_2 F_01)(t,z) up to the
  square convention, and summation by parts (f has compact support) gives
  a_{j+1} - a_j = <nabla_1^* f, F_02> - <nabla_2^* f, F_01>. The telescoping
  identity is exact: r^{-1} sum_{j<r} a_j = a_0 + sum_{i<=r-2}(1-(i+1)/r)
  (a_{i+1}-a_i). Each face carries one coefficient, so the squared l2 weight
  is at most r^{-1}||f||^2 + r sum_i ||nabla_i^* f||^2 <= C_phi, using
  ||f||^2 <= C r and ||nabla f||^2 <= C/r. Only dF = 0 inside the prism is
  used, so any open box containing the prism suffices. HOLDS.
- *Comparison costs (L376-384).* Action cutoff (L236): Z >= e^{-CV log beta}
  from the radius-beta^{-1/2} Haar balls (each plaquette deficit <= C/beta,
  6V plaquettes, ball measure ~ beta^{-3/2} per link), so
  P(S_W > C_0 V log beta) <= e^{-(C_0-C)V log beta}. A bad box needs internal
  deficit >= c/h^8, so on the cutoff the bad boxes cover a fraction
  <= C h^{12} log(beta)/beta = o(1) (gamma < 1/12). Full-to-linear error of
  the global mean: each product moves by an absolute constant times the two
  reading errors; each reading error is <= ||f||_2 <= C sqrt(r) times the l2
  colour error on its faces; Cauchy-Schwarz over n_p ~ V/r^4 readings and
  row 1231 (8) give C r^{5/2}(h^{-1} + r h^{-7/2}) sqrt(S_W/V), which is o(1)
  because gamma > 4 delta > 5 delta/2. I recomputed this exponent.
  Open-box to periodic coupling: Tr(P_H - P) <= CV(1/h + h/N) (row 1231 (1));
  the difference is exact inside each kept cube, so (30) applies; the error
  per reading is C r^2/sqrt(h) = o(1) exactly because gamma > 4 delta.
  Lipschitz constant C/sqrt(J L_0^3) of the average: the reading map Z ->
  (A_i) is linear with bounded norm only through (30) on exact arrays, and
  the reference arrays are exact in each box, including the diluted Gaussian
  replacements. Correct.
- *Density transfer (L384).* Row 1151 L313 states the pointwise bound: the
  law of the tree-chart array with bad boxes replaced by independent
  Gaussians has density at most exp(CV Delta) times the product Gaussian
  (per-box factor 1 + e^{C' b^3}, V/b^4 boxes). A pushforward keeps a
  pointwise density bound. With r^4 Delta_h = o(1) this beats
  exp(-cV/r^4). Correct; the remark that an entropy bound alone would not
  suffice is right.
- *Chessboard and counting (L376, L386, L234).* The product of two
  independent Wilson tori is reflection positive for the diagonal site
  reflections (its action is a sum of two Wilson actions). Tile functions
  read only spatial links on two interior slices (times 2r, 2r+k <= 4r < T),
  inside the closed tile; reflected prisms fit forward or backward. Per tile
  cost exp(-c 8^4 L_0^3) with c independent of L_0 (the forced deviation and
  the overlap bound do not depend on L_0). Union over at most 2^G subsets and
  c L_0^3/2 > 2 log 2 give exp(-c' L_0^3 G), G = (N/(8 L_0 r))^3 ~ (N/k)^3.
  Dyadic N, r, L_0 make tiles divide the periods. Correct.

**(31), L391-396: HOLDS.** The pair density e^{-g_N}K_k(x,y)K_{N-k}(y,x),
the bound K_j(x,y) <= sqrt(K_j(x,x)K_j(y,y)) for a continuous kernel of a
positive operator, the normalizer bound by Cauchy-Schwarz and Mercer
(int K_j(x,x) dx = Tr U^j), and the chain rule
D(P||nu x nu) = I + D(P_1||nu) + D(P_2||nu) give I_k <= g_k + g_{N-k} - g_N.
Convexity: (g_N - g_{N-k})/k >= (g_{N-k} - g_k)/(N-2k), and g_{N-k} >= 0
(the Perron term), give the second inequality. Data processing covers the
neutral orbits.

**(32), L397-401: HOLDS.** Affinity split: int_A sqrt(pq) <= sqrt(P(A)Q(A))
<= sqrt(Q(A)), likewise on A^c; Jensen gives D >= -2 log(affinity). Row 1153
(5) is (m^3/N_sites) log Tr[(F/||F||)^m] -> pi^2/15 for m -> infinity with
m^4 eps_beta -> 0, F the gauge-projected transfer with temporal holonomy;
k <= beta^delta, delta < 1/48 gives k^4 eps_beta -> 0. The file's note that
row 1153's N counts sites is right. Lower bound from (29) for large N/k.

Notes (no correction needed): the limit used in (29) at L362 is uniform in
s in [1,2] because row 1231's majorant in (10) does not depend on s >= 1.

### Step 3 (done): recovery (35) of flux sector ratios, with (33)-(34) and their inputs

(35) rests on (34), which rests on (33), which rests on (28), the k-strip
bound (L341), the estimator (16) at time k, (17), d_N(k) >= c/u^4, the
chessboard (L234), the action cutoff (L236) and the comparisons of rows 1151
and 1231 checked in Step 2. I checked each of these.

**d_N(k) >= c/u^4 and (17) at time k (L320): HOLD.** All terms of the
periodized symbol are positive; restricting the three frequencies to
[1/u, 2/u] leaves >= c(N/u)^3 grid points; on them the numerator is
>= c/u^2, 1/(2 sinh omega) >= c u and e^{-k omega} >= c, so each term is
>= c/u and d_N(k) >= N^{-3} c (N/u)^3 c/u = c/u^4. (17) by Isserlis: the variance of
an entry is m^{-6} sum_{z,z'} (two products of P-entries), each row of the
projection has squared norm <= 1, so <= 2/m^3 per entry; no k enters.

**(28), L331-339: HOLDS.** I recomputed every exponent. H_k divides by
d_N(k), so its Lipschitz factor is C u^4 K; Cauchy-Schwarz over J m^3 ~ V/u
readings gives the factor sqrt(u); total squared transport error <=
C (h^{-2} + (3m+k+2)^2 h^{-7}) S_W. So the Wilson-to-linear cost is
C K u^{9/2}(h^{-1} + (l+k+2) h^{-7/2}) sqrt(S_W/V) = o(1) since
u^{9/2} <= C beta^{9/512} << h ~ beta^{1/16}. Gaussian free mean
<= C u^4 (m^{-3/2} + e^{-cK^2}) -> 0 since 4/256 < 3/80. Lipschitz
C K u^{9/2}/sqrt(V) gives exp(-cV/(u^9 log beta)); the density factor
exp(CV Delta_h) is absorbed since u^9 log^2(beta)/h -> 0 (9/256 < 1/16).
The 1/J power with J = V/(T l^3), T ~ u, l^3 ~ m^3 gives
exp(-c m^3/(u^8 log beta)). Time reversal maps M R^T to (R^T M)^T and H_k is
invariant under transpose and orthogonal changes, so reflected tiles are
covered.

**k-strip bound (L341): HOLDS.** The strip boundary chord is
|G_z - X_{zz'} G_{z'} Y_{zz'}^{-1}|; shelling gives chord <= sum_p |1-U_p|
and |1-U_p|^2 = 2(1-w_p), so chord^2 <= 2kl sum(1-w_p). The half-coupling
moment of (21) holds for any set A of electric faces on one time step: in
the transfer, halving the coupling on A replaces each convolution factor by
one that is at most C times the original in positive-operator order
(normalized character coefficients increase in beta; one-link normalizer
ratio c_0(beta/2)/c_0(beta) <= C); tensor products and the sandwich with
positive factors keep the order (rows 1149 (16), 1153; checks 1150, 1154).
Hoelder over the k steps gives C^{l|E|}, and Markov gives
exp(-c beta |E|/(k^2 l) + C l |E|). With l ~ beta^{1/40}, k <= beta^{1/256},
beta/(k^2 l^2) -> infinity.

**(33), L408-428: HOLDS.**
- Construction: a matrix within 2 eps of SO(3) has singular values within
  2 eps of 1 and positive determinant, so its polar factor is the unique
  nearest rotation; ||pol(A) - R|| <= 2||A - R|| by nearest-point
  optimality. Polar factors and their lifts transform as
  pol -> Ad(h) pol Ad(h')^T, v -> +-h v h'^{-1}.
- Covariance: u.w = Re(u^{-1}w) is invariant under left and right unit
  multiplication, so independent gauge changes leave the recorded signs fixed
  up to the lift coboundary; a vertex coboundary is a holonomy-preserving
  bijection of flat cochains preserving the cost, so the minimizing classes
  are fixed. Flat flips leave M_{z,k} and the retention fixed (Ad kills the
  signs, plaquettes are contractible) and multiply the record by the grid
  restriction of alpha*beta, which is flat (grid squares bound contractible
  fine loops) with holonomy ab (a grid winding cycle is a fine straight
  winding cycle). So D(aX,bY) = ab D(X,Y). Gauge conventions are consistent:
  R = Ad G_z maps the upper root frame to the lower one, as in (16).
- Probability: on an accurate root (||M/d_N - Ad G_z|| <= eps) the vertex is
  retained and t_z v_z is O(eps) from G_z; with a small strip chord the
  recorded dot product is 1 - O(eps + eps_1) > 0, so the bond is unerased
  and equals (dt). Defect sets: three causes, one sample, (28) with degree
  six and the k-strip bound, sum over 3^j assignments. Contour: for a
  minimizer sigma with nontrivial class, tau = sigma dt is a cocycle with
  the same class; its support is a mod-2 closed dual surface; each
  edge-connected component is closed; some component C carries a nontrivial
  class, so the n^2 disjoint homologous straight periods in a suitable
  direction each meet C oddly and |C| >= n^2. Flipping sigma on C is flat,
  gains one on every nondefective bond of C (there sigma disagrees with
  record = dt) and loses at most one on a defective bond, so minimality
  forces at least half of C defective. Counting C_0^j shapes, 3n^3 roots and
  2^j subsets gives (33). Ties are covered, since D != {1} only needs one
  minimizer with nontrivial class.

**(34), L430-442: HOLDS.** With the actual slices as representatives,
covariance gives D(X_{N-k}, X_0) = D(X_{N-k}, c(cX_0)) = c D(X_{N-k}, cX_0),
so the closed product is c when all actual pairs decode to {1}; other
representatives change two adjacent factors by a, and a^2 = 1. B commutes
with c because D(cx, cy) = c^2 D(x,y) = D(x,y) and K_k is flip invariant.
Tr(cBU^{N-k}) = <(B U^{(N-2k)/2})^*, U^{N/2} c>_HS; ||U^{N/2}c||_HS^2 = Z_1
(c is unitary); bounding the second B by K_k inside the nonnegative
integral gives Tr(B^* B U^{N-2k}) <= Tr(B^* U^{N-k}) = Z_1 P_k{D != {1}}
(U is self-adjoint). Divide by sum_d Z_d >= Z_1, sum over 8 twists and N/k
blocks.

**(35), L444-451: HOLDS.** Fourier inversion on G gives
Tr(P_chi U^N)/Tr(P_triv U^N) = E_M chi(c); |chi(c) - chi(c-hat)| <= 2 on
failure (failure value 0 gives <= 1), so the error is <= 2 M{c-hat != c}.
The error vanishes along aN -> L, beta <= B_0 log N, since n = N/l grows
like a power of N and L_{beta,k} grows like a power of beta. The file
correctly leaves open the separate decoded-class probabilities and the
absolute neutral trace.

### Step 4 (done): the endpoint removal (36)-(40)

**(36), L456-479: HOLDS.**
- w >= 1: |F_z| <= max(m_*, 1-m_*) < 1, so ||F||^2 <= M and
  |<F, DF'>| <= M; the event is empty.
- Tail at t = Br: the centred product has Gaussian limit
  E[OO'] - 2 m_* E[O] + m_*^2 -> K(B,0) of row 1231 (11), which tends to
  0 as B -> infinity since D(B) -> 0 by dominated convergence. The tile
  argument of (29) applies with time tile >= 4(B+1)r; the per-tile cost
  exp(-c_{w,B} L_0^3) has c_{w,B} independent of L_0 (forced deviation
  w/4 - w/12 = w/6, probes ~_B V/r^4). Tile averages lie in [-1,1], so a
  spatial mean > w/2 forces more than wG/4 excessive tiles (mean <= f +
  w/4). With G = M/L_0^3 the union over 2^G subsets is absorbed for L_0
  large, giving P_{Br}(G_stat > wM/2) <= e^{-b_w M}, and
  E e^{sigma G_stat} <= e^{sigma w M/2} + e^{(sigma - b_w)M} since
  G_stat <= M.
- Propagation: [f,h]_t = E_t f(X_0)h(X_t) (pair density
  K_t(x,y)K_{N-t}(y,x)/Tr U^N); [f,f]_t = ||U^{(N-t)/2} M_f U^{t/2}||_HS^2
  / Tr U^N >= 0 and symmetry holds since both kernels are symmetric. For a
  PSD Gram matrix H, |tr(A^T H)| <= ||A||_op tr H; with A = D^{(x)j} this
  gives |E_t <F,DF'>^j| <= tr H_j(t) = E_t <F,F'>^j. In an eigenbasis,
  tr H_j(t) is a sum of terms u_p^{N-t} u_q^t |<p, M q>|^2, each convex in t,
  and the sum is symmetric under t <-> N-t (swap p, q; M real symmetric),
  so tr H_j(t) <= tr H_j(Br) on [Br, N-Br]. All E_{Br} G_stat^j >= 0, so
  E_t e^{+-sigma <F,DF'>} <= E_{Br} e^{|sigma| G_stat}. Markov at wM with
  sigma near b_w/2 gives e^{-sigma w M/2} + e^{-(b_w - sigma)M} per sign,
  hence 4 e^{-c_w M}. I recomputed the constants.

**(37), L481-487: HOLDS.** For t <= N/2 and band [0, aE],
1_{[0,aE]}(-log U) <= e^{(N-2t)aE} U^{N-2t} <= e^{aNE} U^{N-2t}.
Tr(B^*B U^{N-2t}) is a nonnegative triple integral; bounding the second B
by K_t gives Tr(B^* U^{N-t}) = e^{g_N} P_t{event}. g decreases, so
g_N <= g_{h_0} = (pi^2/15 + o(1))(N/h_0)^3 by row 1153 (5) with
h_0^4 eps_beta -> 0 (delta' < 1/16), and (N/h_0)^3 / M = (8r/h_0)^3 -> 0.
At t = N/2 the projector is not needed. Correct.

**(38), L494-503: HOLDS.** Lower side: Z <= e^{-(beta-s)d} int e^{-sD};
dropping non-tree bonds (each term >= 0) and integrating leaves with
q = g_z^{-1} X_e g_{z'} Y_e^{-1} gives z_s^{v_3-1}, z_s <= C(1+s)^{-3/2};
s d = beta d/(1 + beta d/v_3) <= v_3. Upper side: on great-circle paths of
speed <= C rho, rho = c/sqrt(1+beta), the first derivative at the minimizer
vanishes and each bond term has |f_e''| <= C rho^2; Taylor gives
D <= d + C v_3/(1+beta); the balls have Haar mass >= (c' rho^3)^{v_3}.

**L505-511 (typical-set form): HOLDS.** 1 - g_z.R_e g_{z'} =
(1/2)|g_z^{-1} X_e g_{z'} - Y_e|^2 for unit quaternions, so d_XY is half the
squared orbit chord distance. The lower tail is row 1155 (20) (read at its
L300: P{d_G^2 <= eps_0^2 N/(1+beta)} <= e^{-cN}, also for V determined by
other slices). The upper tail follows from d <= D(actual g) and the
half-tilt moment. Since (1+s)(1 + beta d/v_3) = 1 + beta + beta d/v_3 >=
1 + beta, log((1+beta)/(1+s)) <= log(1 + beta d/v_3), whose mean is O(1) by
Jensen. Only the upper tail is needed for the displayed formula.

**(39), L513-519: HOLDS.** Gauge invariance under independent left
multiplication at each lower vertex makes the law of the temporal layer
invariant under all left translations, hence product Haar. Then
I(g; (X,Y)) = E log(dpi_{X,Y}/dHaar) = E[-log Z - beta D_XY(g)], and
E beta D_XY(g) = O(v_3).

**(40), L526-535: HOLDS.** The excluded set is flip invariant because F is;
(average)^2 <= average of squares and the change of variables y -> cy give
||1_{C^c} K^+_{T/2}||_HS^2 <= ||1_{C^c} K_{T/2}||_HS^2 <= e^{g_T}
P_{T/2}(C^c). K^+_{T/2} is the kernel of P_triv U^{T/2}; its top singular
value is 1 (the Perron vacuum is flip invariant) and its squared HS norm is
Tr(P_triv U^T), so by Eckart-Young its HS distance to rank <= 1 is
sqrt(Tr(P_triv U^T) - 1); distance to a set is 1-Lipschitz. The extension
to T = N/2 (L535) holds: row 1231 (1)-(2) were stated for time period
M >= n, but their only time-period dependence is the boundary fraction
O(b/M), still o(1) at M = n/2; the image bound becomes O((r/T)^4). This is
a precision note, not a defect.

The OPEN paragraphs L521, L537 and L539 are accurate: (38) leaves an O(N^3)
remainder per step; (40) leaves the rank-one error at a fixed physical side
unbounded; no energy threshold is proved.

### Step 5 (done): everything else, (1)-(28) and the labelled remarks

All checked by hand; each HOLDS. Key verifications, so a reader can redo them:

**(2), L33-37.** With u_i = Im q_i and Ad q_i a rotation by 2 theta_i about
u-hat_i, |v - A_i v|^2 = 4|u_i x v|^2, so D = 4 lambda_min of
(|u_1|^2+|u_2|^2)I - u_1u_1^T - u_2u_2^T, which equals the small Gram
eigenvalue |u_1 x u_2|^2/mu_+ >= |u_1 x u_2|^2/(2|u_1|^2) when
|u_1| >= |u_2|. Hence D >= 2|u_2 x u-hat_1|^2, as stated. The event is a
codimension-two tube of width sqrt(v) around a great circle; under a tilt
of parameter <= 6 beta its mass is <= C b v (row 1141 cap estimate, check
1142). Spatial link tilt <= 6 beta: four spatial staples plus two bridge
terms of size <= beta.

**(3)-(4), (1), L39-56.** Telescoping round a four-edge loop gives
|s_x - A_i s_x|^2 <= 4 sum over its edges, so v|s_x|^2 <= 4 sum over both
loops. With f = |s|, sum (f_x - f-bar)^2 <= C r^2 Q_B and
f-bar^2 <= (2/#good) sum_good [(f_x - f-bar)^2 + f_x^2] give (3) with
|B|/M <= 6^3. Choice r = floor(kappa u^{-1/2}), v = K u makes the form
>= 2u ||s||^2 on good rectangles. Successive conditioning on disjoint cells
gives (Cbv)^j; failing (3) needs > M/2 bad cells, so <= 2^M (Cbv)^{M/2}
= exp(-(M/2) log(1/(4Cbv))), M >= c u^{-3/2}. Min-max with
L_Y >= direct sum of Neumann blocks gives the upper side of (1). Lower
side: one-link density >= e^{-12 beta} Haar (tilt <= 6 beta); cap mass
>= c eta^3; for s_x = phi_x t, |phi_x t - phi_y A t|^2 = (phi_x - phi_y)^2
+ phi_x phi_y |t - At|^2, with |t - At| <= 2|Y - 1| <= 2 eta and
sum phi_x phi_y <= 3||phi||^2; quotient <= 3 pi^2/(s+1)^2 + u/4 < 7u/16.
Packed cubes with a vacant layer have no cross terms. (4) follows with
b = O(log(1/u)).

**(5)-(7), L61-82.** Markov gives (5). The bridge law of the middle slice
has the same one-link tilt bound, so (R 1_A R)(X,Z) <= p R^2(X,Z);
||1_A R f||^2 <= p || |f| ||^2 and R^{-1} <= e^{aE} on the band give (6).
In (7): <Q psi, R Q psi> = 1 - 2d + <1_A psi, R 1_A psi> >= 1 - 2d and
||Q psi||^2 = 1 - d; Tr((QT)^k)/Tr(T^k) is the periodic-chain probability
that no slice lies in A, and each slice's law given its neighbours is a
bridge. Twisted seams keep the bridge bound (A is flip invariant). L82:
p decays like exp(-c (log 1/a)^{3/2}), faster than any power of a.

**(8)-(10), L91-126.** P_U = I/2 + (adjacency with transports)/(4d) inside
D. |v + A_1 v + A_2 v|^2 = 9 - (sum of the three pairwise squared
distances) <= 9 - D_z, so ||I + A_1 + A_2|| <= 3 - D_z/6 and the diagonal
loss is h c_0/(6b) at good sites (a loop leaving D removes weight h). The
walk lemma: H ~ Binomial(n,p) by independent increments; E J <= C'n since
d >= 3; the Caro-Wei bound sum 1/(deg+1) >= H^2/J with
sum(deg+1) <= J; Doob's inequality with variance <= 16n. Slabs of half
width L around planes 4L apart are disjoint, so trials read disjoint links;
successive conditioning gives a kill probability >= a constant per plane,
hence exp(-cR/sqrt(b)). Strong Markov at the halfway plane plus the free
Green bound (10) gives (8); the Neumann series converges in a finite box.
L126 summing: int r e^{-cr/sqrt(b)} dr ~ b.

**(11)-(14), L133-170.** The electric plaquette for edge e is
Re(g_x^{-1} X_e g_y Y_e^{-1}) = g_x . R_e g_y; the action is even in g.
(12): trace duality |tr(O C^T)| <= ||C||_*; the thin rectangle is the r-th
moment of a nonnegative eigenvalue ratio under a probability (row 1153;
also row 1169 (1), check 1170), and Jensen. L146: min_q |q - X_p q Y_p^{-1}|^2
= 2 - 2 cos(theta_X - theta_Y) (rotate the axis of q^{-1} X_p q onto that
of Y_p); the class-angle density under a tilt <= 6 beta is <= C sqrt(b)
(row 1155, check 1156); ||I + A||^2 = 4 - min|q - Aq|^2. (13): segment
mismatch mean <= 2Ch/beta from (12); 1 - |F|^2 is the site variance;
||O||_F = 2 gives E||C_xy||_F^2 >= (1 - C l/beta)_+^2/4; the replica
expansion gives int s_x s_y = ||C_xy||_F^2. L170: centred components,
pointwise squared gradient <= 1/|B|.

**(15)-(19), L175-220.** d_N >= d_*: P_{12,12} = (k_1^2+k_2^2)/|k|^2 is the
12,12 entry of the projection k ^ i_k/|k|^2 onto exact two-forms; the time
coefficient e^{-|j| omega}/(2 sinh omega) with 2 cosh omega = 2 + s^2;
q_1 in [pi/3, 2pi/3] gives numerator >= 1. (17) as in Step 3. (18): the
translated average moves by <= 2K||dF||_2/sqrt(V); each term of (18) is
O(beta^{-eta}) because 3 gamma/5 > eta and gamma/2 > eta. (15): projection
onto the radius-sqrt(3) Frobenius ball is 1-Lipschitz and fixes rotations;
||R-hat - R||^2 <= C H. (19): conditional variance <= estimator loss;
||Ad g - Ad g'||_F^2 = 8(1 - (g.g')^2) since tr Ad q = 4(Re q)^2 - 1;
|a.b - c.d| <= |a-c| + |b-d| for unit vectors;
1 - s-bar^2 = mean(1 - s^2) + var(s).

**(20)-(23), L225-268.** (20) is (28) at k = 1 (exponents recomputed:
1/J power of exp(-cV/log beta) with J = N^4/(4 l^3)). (21): chord^2 <=
2l sum(1-w_p), Markov with beta/2, l^2 = o(beta). (22): six causes, degree
six, 6^k assignments; each copy has the Wilson marginal. Sign rule L259:
s^2 >= 1 - eps^2/(2 d_*^2) > 9/16 and |s_z - s_z'| <= 2 eps_1. L261 contour
count: the component boundary is a mod-2 dual cycle; a primal path crosses
it oddly, so some simple circuit crosses oddly; a circuit shorter than n is
contractible and surrounds one endpoint; longer circuits are counted with
all n^2 starts; sum C(k+1)^2 4^k theta^k <= C theta. (23): 1 - |a||b| <=
(1 - a^2) + (1 - b^2); off-grid steps cost C(l/beta + beta^{-eta}).

**(24)-(26), L273-308.** sum_e e-bar v e = 4 Re v and tr(L_v R_w) =
4 Re v Re w give (1/4) tr(rho(a,b)^T rho(c,d)) = (a.c)(b.d). (24): the
conditional density of g_x is e^{r cos theta} with r <= 6 beta; the
interval [(2 sqrt(1+r))^{-1}, (1+r)^{-1/2}] has mass >= c; E cos theta in
[0, 1 - c/(1+r)]; E[Ad q | theta] = (1 - (4/3) sin^2 theta) I; rho is
linear in its first argument. (25): rho(ab, cd) = rho(a,c) rho(b,d), layers
independent given the slices; 4 - ||AB||_F^2 = 4 - ||B||_F^2 +
tr((I - A^T A) B B^T) <= (4 - ||A||_F^2) + (4 - ||B||_F^2) for
contractions. (26): conditional independence turns both trace identities
into squared Frobenius norms of conditional means.

**(27), L313-341.** One-root loss: estimator error O(beta^{-1/128}) (the
worst term is u^4 K sqrt(Delta_h) = O(beta^{-1/64} log beta); u^4 m^{-3/2}
= beta^{-7/320}); multiple roots (28) and the k-strip bound (Step 3); each
copy has the one-slab Wilson marginal; O_e is read from X_0, X_k only, so
the sign rule applies to both copies; off-grid strips have mean squared
chord <= C k^2 l^2/beta. HOLDS.

**ARGUED L343, OPEN L84, L521, L537, L539:** accurate as labelled.

No statement in Steps 2-5 FAILS and none needs a correction to a proof
step. Precision notes are collected in Step 8.

### Step 6 (done): is the main comparison a restatement of an earlier row?

Searched: `library/open-core.md` (no entry on two-slice information,
flux sectors, twist decoding or the neutral trace), the FINISH rows (no row
claims these statements), and the files the checked text cites, plus rows
1147, 1165, 1186 and 839 found by grepping `library/gap-*.md` for "mutual
information", "rank", "prism", "convex" and "Gram".

Answer: **the main comparison, (29) with (32), is not a restatement.** Its
lower half is new: the extensive bound c(N/k)^3 on the information of two
neutral slices comes from a large-deviation form of row 1231's (9)-(11)
Gaussian comparison, made possible by the closed-curl prism identity (30)
(no earlier `prism` use in `library/gap-*.md` is this identity) and the
chessboard estimate. Row 1231 gave only expectations of paired readings.

Partial overlaps, each a credit precision, not a defect:

1. **(31), first inequality.** At the antipodal time k = N/2 it is exactly
   the upper inequality of row 1165 (`gap-solve11-astra62.md` L42-47, (3)):
   I_{2t} <= 2 log X_t - log X_{2t} = J(t), proved there from the diagonal
   law at the shorter period. (31) extends it to every k < N/2 by the same
   argument. Row 1165 (check 1166, HOLDS AFTER CORRECTION of constants only)
   is not cited in the checked file and should be. Row 839's identity I1
   (`gap-compress-opus.md` L36-46), cited at L348, is the vacuum-chain
   version: I(X_0; X_n) <= g_{2n}, which is sharper than the N -> infinity
   limit g_k of (31) because g decreases.
2. **(33)-(35).** Row 1155 (`gap-solve7-astra62.md` (29), (34)) already
   decodes the twist class in the centre-summed ensemble, by a
   minimum-face estimator, from short adjoint collars, and expresses the
   strict test through class frequencies u_p. (33)-(35) do the same from
   neutral spatial slices at spacing k only, with the twisted-ensemble
   transfer by the Hilbert-Schmidt Cauchy-Schwarz bound of (34). That is a
   real strengthening of the observation set. The file credits row 1155 at
   L406.
3. **(40).** The quantity Tr(P_triv U^T) - 1 as a squared Hilbert-Schmidt
   distance to the vacuum part is the trace split used in row 1231 (42) and
   row 1227 (27). New in (40) is only the exponentially small removal of the
   excluded pairs from (37). Citing row 1231 (42) at L526 would help the
   reader.
4. **(36).** The propagation by the PSD Gram matrix and the convexity of
   t -> Tr(U^{N-t} M U^t M) is a standard transfer fact (row 1153 uses the
   same convexity for J_s); its use to carry a large-deviation bound to all
   separations B r <= t <= N - B r is new as far as this search shows.
5. **(8) vs rows 1244 and the `ac` row.** The file says so itself at L89:
   those rows prove a deterministic Combes-Thomas bound given a spectral
   gap; (8) is an annealed bound in the Wilson law with no gap hypothesis.
   Not a restatement.

Timing note: Steps 1-6 were written between 14:21Z and 14:41Z (date -u). An
earlier draft of their headers carried guessed clock times; those were wrong
and have been removed.

### Step 7 (done 14:41Z): numeric guide (guide only; no verdict rests on it)

Memory 64 percent free; run under `lab_ops.py numeric-lock` (acquired and
released), one thread, nice, RSS self-check at 2 GB. A scratch script outside
the repository tested, with random unit quaternions, rotations, contractions
and positive kernels on a six-point space (worst value over all draws):

| Statement tested | Worst value |
|---|---|
| (1/4) tr(rho(a,b)^T rho(c,d)) = (a.c)(b.d), L275 | 2e-16 error |
| ||Ad g - Ad g'||_F^2 = 8(1 - (g.g')^2), L220 | 6e-15 error |
| tr Ad q = 4 (Re q)^2 - 1 | 8e-16 error |
| (2) Gram step: 2|u_2 x u-hat_1|^2 - D <= 0 | -7e-5 |
| ||I + A_1 + A_2|| - sqrt(9 - D) <= 0, L100 | -1e-4 |
| min_q |q - X q Y^{-1}|^2 = 2 - 2cos(theta_X - theta_Y), L143 | 4e-15 error |
| (25) contraction deficit inequality <= 0 | -0.54 |
| (30) telescoping identity | 3e-16 error |
| (29) Gaussian determinant formula | 1e-16 error |
| (31) I_k - (g_k + g_{N-k} - g_N) <= 0, finite chain | -5e-7 |
| (31) second inequality <= 0 | -1e-6 |
| (36) |E_t <F,DF>^j| - E_s <F,F>^j <= 0, j <= 4, s <= t <= N-s | -3e-3 |

The guide agrees with every hand verdict. It is not evidence for any
verdict; each verdict rests on the hand checks of Steps 2-5.

### Step 8: verdicts per statement

Provenance: Claude Opus 5.5, max effort, Mac mini worker 3, at commit
1ce538a51; one cross-provider reading of a gpt-6.2-astra row, by hand. Not an
audit; it grants no status. Every verdict below is an implication from the
cited checked rows (1141, 1145, 1149, 1151, 1153, 1155, 1169, 1231), whose
statements and proofs I read where a step depends on them.

Positive claims named in row 1289, first:

| Statement | Lines | Verdict |
|---|---|---|
| (29) separating neutral event, P_k(A^c) + Q_k(A) <= C e^{-c(N/k)^3} | L350-386 | HOLDS |
| (30) closed-curl prism identity and bounded weight | L364-374 | HOLDS |
| (31) I_k <= g_k + g_{N-k} - g_N <= (1 + k/(N-2k)) g_k | L391-396 | HOLDS (credit row 1165 (3), see Step 6) |
| (32) c(N/k)^3 <= -2 log affinity <= I_k <= (pi^2/15 + o(1))(N/k)^3 | L389, L397-401 | HOLDS |
| (35) flux sector ratios from neutral slice histories | L444-451 | HOLDS |
| (36) singlet large-deviation bound at all B_w r <= t <= N - B_w r | L456-479 | HOLDS |
| (37) restricted kernel on a physical energy band | L481-487 | HOLDS |
| (38) orbit-volume estimate | L494-503 | HOLDS |
| (39) layer information (3/2) v_3 log(1+beta) + O(v_3 + log(1+beta)) | L513-519 | HOLDS |
| (40) rank-one distance form of the neutral trace | L526-535 | HOLDS (precision note 3) |

Everything else:

| Statement | Lines | Verdict |
|---|---|---|
| (1) adjoint-mode count, both sides | L25-31, L45-49 | HOLDS |
| (2) two-plaquette defect | L33-37 | HOLDS |
| (3) block Poincare | L39-43 | HOLDS |
| (4) and the positive-fraction remark | L51-56 | HOLDS |
| (5), (6) and the n_Y(u) variant | L61-71 | HOLDS |
| (7) and the neutral-sector version; L82 | L73-82 | HOLDS |
| (8) annealed Green bound | L91-96, L122-124 | HOLDS |
| (9) kernel domination | L98-110 | HOLDS |
| (10) walk bounds; walk lemma L120; crossing L122 | L112-122 | HOLDS |
| L126 summed and source-pairing bounds | L126 | HOLDS |
| (11) conditional temporal law | L133-139 | HOLDS |
| L141-146 (8) for L_{X,Y} by a one-loop test | L141-146 | HOLDS |
| (12) covariance lower bound; L156 comparison | L148-156 | HOLDS |
| (13), (14); L170 relaxation bounds | L158-170 | HOLDS |
| (15)-(18), L186 equivariance, L211 projection | L175-211 | HOLDS |
| (19) replica overlap | L213-220 | HOLDS |
| (20) inaccurate roots; L234 chessboard; L236 action cutoff | L225-244 | HOLDS |
| (21) strip marks | L246-251 | HOLDS |
| (22) defective bonds; L259 sign rule; L261 contours | L253-261 | HOLDS |
| (23) global replica sign | L263-268 | HOLDS |
| L273-278 trace identity for rho | L273-278 | HOLDS |
| (24) one-step contraction | L280-286 | HOLDS |
| (25) layer product and its lower bound | L288-298 | HOLDS |
| (26) conditional overlaps | L300-308 | HOLDS |
| (27) endpoint recovery with hidden slices | L313-329, L341 | HOLDS |
| (28) multiple inaccurate roots at time k | L331-339 | HOLDS |
| (33) candidate classes, covariance and error | L408-428 | HOLDS |
| (34) twist decoding in the twisted mixture | L430-442 | HOLDS |
| L505-511 typical-set form of (38) | L505-511 | HOLDS |
| ARGUED L343; OPEN L13, L84, L521, L537, L539 | | accurate as labelled |
| GUIDE paragraphs (repo search L3-9, L89, L131, L348, L406, L492) | | not verdicts; cited rows read where used |

FAILS: none. HOLDS AFTER CORRECTION: none; no proof step needs a change.

Precision and credit notes (none breaks a statement):

1. (31): its first inequality at k = N/2 is the upper inequality of row 1165
   (3) (`gap-solve11-astra62.md` L42-47), extended to all k by the same
   argument; cite row 1165.
2. (35) extends row 1155's twist-class recovery ((29), (34) there) from
   adjoint collars to neutral spatial slices; already credited at L406.
3. L535 (T = N/2): row 1231 (1)-(2) were stated for time period M >= n; at
   M = n/2 only the boundary fraction O(b/M) changes, which stays o(1). One
   line saying so would close the reading.
4. (40) uses the trace split of row 1231 (42); citing it at L526 would help.
5. L120 is the Caro-Wei bound and L533 the Eckart-Young theorem; naming them
   would help a Lean formalization. L362's limit is uniform in s in [1,2]
   because row 1231 (10) has an s-independent majorant.

What stays open (as the checked file says): the absolute neutral trace at a
fixed physical side (the rank-one error in (40)), hence the thermal
criterion; the separate decoded-class probabilities in (35); the
nontrivial continuum construction; the four-dimensional SU(2) mass gap.

RESULT: row 1283 HOLDS, checked line by line by hand by Claude Opus 5.5 max (Mac mini worker 3; cross-provider check of a gpt-6.2-astra row; grants no status): every numbered statement (1)-(40) and every PROVED paragraph HOLDS, 0 FAILS, 0 corrections. Positive claims: (29)-(32) short-time neutral-slice information bounds, (35) flux sector ratios from neutral histories with (33)-(34), (36)-(40) endpoint removal. The main comparison (29)/(32) is not a restatement; (31) restates row 1165 (3) at k = N/2 and should cite it. OPEN: the absolute neutral trace at a fixed physical side, the nontrivial continuum construction, the mass gap. Output library/gap-solve32-check-opus.md.
